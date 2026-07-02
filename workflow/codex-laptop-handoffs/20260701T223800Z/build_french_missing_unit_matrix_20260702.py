import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "20260702T031500Z"
OUT_JSON = ROOT / "logs" / f"FRENCH_MISSING_UNIT_MATRIX_{STAMP}.json"
OUT_MD = ROOT / "logs" / f"FRENCH_MISSING_UNIT_MATRIX_{STAMP}.md"

FRENCH_MANIFEST = ROOT / "logs" / "FRENCH_CUMULATIVE_STATUS_MANIFEST_20260701T161500Z.json"
SOURCE_INVENTORY = ROOT / "sources" / "PAPERS_01_43_PLUS_POST_NUMBERED_SOURCE_INVENTORY.json"
SOURCE_INVENTORY_VALIDATION = ROOT / "sources" / "PAPERS_01_43_PLUS_POST_NUMBERED_SOURCE_INVENTORY_VALIDATION.json"
ENDMATTER_INVENTORY = ROOT / "sources" / "endmatter" / "ENDMATTER_SOURCE_INVENTORY.json"
ENDMATTER_VALIDATION = ROOT / "sources" / "endmatter" / "ENDMATTER_SOURCE_INVENTORY_VALIDATION.json"
P40_COMPLETION_LOG = ROOT / "logs" / "FRENCH_P40_S09_COMPLETION_TRANSLATION_20260630.json"
CHECKPOINT_TEX_ROOT = (
    ROOT
    / "sources"
    / "non_slavic_existing_translation_artifacts"
    / "zenodo_20836874_20260628"
    / "extracted"
    / "14_Noether_-_French_and_Simplified_Chinese_Checkpoint_P19s06_20260612"
    / "tex"
)


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def sha256_file(path: Path) -> str | None:
    if not path.is_file():
        return None
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def file_record(path: Path | None) -> dict:
    if path is None:
        return {"path": None, "present": False}
    return {
        "path": rel(path),
        "present": path.is_file(),
        "bytes": path.stat().st_size if path.is_file() else None,
        "sha256": sha256_file(path),
    }


def glob_records(patterns: list[str]) -> list[dict]:
    paths: list[Path] = []
    for pattern in patterns:
        paths.extend(ROOT.glob(pattern))
    return [file_record(path) for path in sorted(set(paths)) if path.is_file()]


def source_sections(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    sections = []
    for match in re.finditer(r"\\subsection\*\{§\s*(\d+)\.\s*([^}]*)\}", text):
        line = text[: match.start()].count("\n") + 1
        sections.append({"section_number": int(match.group(1)), "title": match.group(2).strip(), "line": line})
    return sections


def numbered_record(inventory: dict, paper_number: int) -> dict:
    for record in inventory.get("records", []):
        if record.get("paper_number") == paper_number:
            return record
    raise KeyError(f"missing inventory record for paper {paper_number}")


def source_file_records_from_numbered(record: dict) -> dict:
    keys = ["primary_german_source", "primary_english_control", "final_scan_pdf"]
    return {key: file_record(ROOT / record[key]) for key in keys if record.get(key)}


def source_file_records_from_endmatter(record: dict) -> dict:
    result = {}
    if record.get("body_tex_witness"):
        result["body_tex_witness"] = file_record(ROOT / record["body_tex_witness"])
    for key in ["component_pdf_witnesses", "component_tex_witnesses"]:
        result[key] = [file_record(ROOT / item) for item in record.get(key, [])]
    return result


def existing_french_evidence_for_numbered(paper_number: int) -> dict:
    p = f"{paper_number:02d}"
    return {
        "logs": glob_records([f"logs/FRENCH_P{p}*.json", f"logs/FRENCH_P{paper_number}*.json"]),
        "translation_tex": glob_records([f"translations/paper{p}/french/**/*.tex", f"translations/paper{paper_number}/french/**/*.tex"]),
        "checkpoint_tex": glob_records([f"sources/non_slavic_existing_translation_artifacts/**/tex/*P{paper_number}*fr*.tex"]),
        "cumulative_tex": glob_records([f"sources/non_slavic_existing_translation_artifacts/**/tex/cum_fr_P{paper_number}*.tex"]),
        "render_pdfs": glob_records([f"renders/**/*P{paper_number}*fr*.pdf", f"renders/**/*paper{paper_number}*french*.pdf"]),
    }


def existing_french_evidence_for_endmatter(record_id: str, logical_number: str) -> dict:
    patterns = [
        f"logs/FRENCH_*{record_id.upper()}*.json",
        f"logs/FRENCH_*P{logical_number}*.json",
        f"translations/**/*{record_id}*french*.tex",
        f"translations/**/*P{logical_number}*French*.tex",
        f"sources/non_slavic_existing_translation_artifacts/**/tex/*{record_id}*fr*.tex",
        f"sources/non_slavic_existing_translation_artifacts/**/tex/*P{logical_number}*fr*.tex",
        f"renders/**/*{record_id}*fr*.pdf",
        f"renders/**/*P{logical_number}*fr*.pdf",
    ]
    hits = glob_records(patterns)
    return {
        "logs": [item for item in hits if item["path"].startswith("logs/")],
        "translation_or_checkpoint_tex": [item for item in hits if item["path"].endswith(".tex")],
        "render_pdfs": [item for item in hits if item["path"].endswith(".pdf")],
        "all_hits": hits,
    }


def evidence_status(evidence: dict) -> str:
    total = 0
    for value in evidence.values():
        if isinstance(value, list):
            total += len(value)
    return "present" if total else "absent"


def required_artifacts(unit_label: str) -> list[str]:
    return [
        f"source-fidelity French translation log for {unit_label}",
        f"French body TeX and wrapper TeX for {unit_label}",
        "cumulative French TeX integration from current cum_fr_P40_s09 baseline",
        "standalone render PDF/log/console validation",
        "cumulative render PDF/log/console validation",
        "visual inspection notes for standalone and cumulative pages",
        "terminology/rationale sidecar for any hard terms touched",
        "manifest/workflow-log update and GitHub handoff pointer",
    ]


def main() -> None:
    french_manifest = load(FRENCH_MANIFEST)
    source_inventory = load(SOURCE_INVENTORY)
    source_inventory_validation = load(SOURCE_INVENTORY_VALIDATION)
    endmatter_inventory = load(ENDMATTER_INVENTORY)
    endmatter_validation = load(ENDMATTER_VALIDATION)
    p40_completion = load(P40_COMPLETION_LOG)

    p40_source = ROOT / "sources" / "paper40" / "source_fidelity" / "Noether_Paper40_ORIGINAL_MathZ37_R124plusP40_repaired_witness_v001.tex"
    p40_sections = source_sections(p40_source)
    p40_max_section = max((item["section_number"] for item in p40_sections), default=None)

    units = []
    units.append(
        {
            "unit_id": "paper40_s10_stale_manifest_wording",
            "unit_type": "stale_gap_wording_check",
            "paper": 40,
            "section": 10,
            "title_de": None,
            "title_en": None,
            "status": "not_expected_paper40_complete_at_s09",
            "missing_translation": False,
            "source_authority": {
                "p40_completion_log": file_record(P40_COMPLETION_LOG),
                "p40_completion_flag": p40_completion.get("paper40_completion"),
                "next_french_lane_start": p40_completion.get("next_french_lane_start"),
                "source_line_start": p40_completion.get("source_line_start"),
                "source_line_end": p40_completion.get("source_line_end"),
                "next_source_line": p40_completion.get("next_source_line"),
                "controlling_source": file_record(p40_source),
                "source_sections_found": p40_sections,
                "max_source_section_number": p40_max_section,
            },
            "existing_french_evidence": {
                "completion_log": file_record(P40_COMPLETION_LOG),
                "cumulative_tex": french_manifest["current_branch_records"]["cum_fr_p40_s09_tex"],
                "cumulative_pdf": french_manifest["current_branch_records"]["cum_fr_p40_s09_pdf"],
            },
            "decision": (
                "Do not open a P40 S10 unit unless a newer source witness contradicts the P40 S09 completion ledger. "
                "Current source headings reach §9 and the French ledger marks Paper 40 complete."
            ),
            "required_next_artifacts": [],
        }
    )

    for paper_number in [41, 42, 43]:
        record = numbered_record(source_inventory, paper_number)
        evidence = existing_french_evidence_for_numbered(paper_number)
        units.append(
            {
                "unit_id": f"paper{paper_number:02d}",
                "unit_type": "numbered_paper",
                "paper": paper_number,
                "section": None,
                "title_de": record.get("title_de"),
                "title_en": record.get("title_en"),
                "printed_pages": record.get("printed_pages"),
                "final_audit_pdf_pages": record.get("final_audit_pdf_pages"),
                "status": "missing_french_translation_render_and_cumulative_integration",
                "missing_translation": evidence_status(evidence) == "absent",
                "source_inventory_record": {
                    key: record.get(key)
                    for key in [
                        "paper_number",
                        "primary_german_source",
                        "primary_english_control",
                        "final_scan_pdf",
                        "german_line_range_final_audited",
                        "english_line_range_final_audited",
                        "source_decision",
                    ]
                },
                "source_files": source_file_records_from_numbered(record),
                "inventory_sha256": record.get("sha256"),
                "existing_french_evidence": evidence,
                "required_next_artifacts": required_artifacts(f"Paper {paper_number}"),
            }
        )

    for record in endmatter_inventory.get("records", []):
        record_id = record.get("record_id")
        logical_number = str(record.get("logical_number"))
        evidence = existing_french_evidence_for_endmatter(record_id, logical_number)
        label = f"post-numbered {logical_number}" if logical_number != "terminal" else "terminal bibliography"
        units.append(
            {
                "unit_id": record_id,
                "unit_type": "post_numbered_material",
                "paper": int(logical_number) if logical_number.isdigit() else None,
                "logical_number": logical_number,
                "section": None,
                "title_de": record.get("title_de"),
                "title_en": None,
                "printed_pages_evidence": record.get("printed_pages_evidence"),
                "source_pdf_pages_evidence": record.get("source_pdf_pages_evidence"),
                "status": "missing_french_translation_render_and_cumulative_integration",
                "missing_translation": evidence_status(evidence) == "absent",
                "source_inventory_record": {
                    key: record.get(key)
                    for key in [
                        "record_type",
                        "record_id",
                        "logical_number",
                        "body_tex_witness",
                        "source_decision",
                        "segment_validation",
                    ]
                },
                "source_files": source_file_records_from_endmatter(record),
                "inventory_sha256": record.get("sha256"),
                "existing_french_evidence": evidence,
                "required_next_artifacts": required_artifacts(label),
            }
        )

    missing_units = [unit for unit in units if unit.get("missing_translation")]
    payload = {
        "artifact": "french_missing_unit_matrix",
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "status": "matrix_only_no_translation_or_render_change",
        "scope": (
            "Authoritative French completion matrix after current cum_fr_P40_s09 baseline. "
            "Retires stale P40 S10 wording unless a newer source witness appears; actual missing queue begins at Paper 41."
        ),
        "inputs": {
            "french_cumulative_status_manifest": file_record(FRENCH_MANIFEST),
            "source_inventory": file_record(SOURCE_INVENTORY),
            "source_inventory_validation": {
                "file": file_record(SOURCE_INVENTORY_VALIDATION),
                "missing_required_files": source_inventory_validation.get("missing_required_files"),
                "checks": source_inventory_validation.get("checks"),
            },
            "endmatter_inventory": file_record(ENDMATTER_INVENTORY),
            "endmatter_inventory_validation": {
                "file": file_record(ENDMATTER_VALIDATION),
                "validation_failures": endmatter_validation.get("validation_failures"),
                "checks": endmatter_validation.get("checks"),
            },
            "paper40_completion_log": file_record(P40_COMPLETION_LOG),
        },
        "current_french_baseline": {
            "baseline_unit": "cum_fr_P40_s09",
            "current_branch_records": french_manifest.get("current_branch_records"),
            "paper40_completion_log": {
                "paper40_completion": p40_completion.get("paper40_completion"),
                "next_french_lane_start": p40_completion.get("next_french_lane_start"),
                "next_source_line": p40_completion.get("next_source_line"),
            },
        },
        "summary": {
            "matrix_unit_count": len(units),
            "missing_translation_unit_count": len(missing_units),
            "not_expected_or_retired_unit_count": len([unit for unit in units if unit["status"].startswith("not_expected")]),
            "missing_unit_ids": [unit["unit_id"] for unit in missing_units],
            "next_translation_unit": "paper41",
            "source_inventory_validated": not source_inventory_validation.get("missing_required_files"),
            "endmatter_inventory_validated": not endmatter_validation.get("validation_failures"),
        },
        "units": units,
        "next_actions": [
            "Start French source-fidelity translation at Paper 41, not at a non-existent Paper 40 section 10.",
            "After Paper 41, continue with Papers 42 and 43 from the final audited numbered-paper inventory.",
            "Then translate post44, post45, and postbibliography from the endmatter source inventory before making any full-volume French completion claim.",
            "For every unit, render standalone and cumulative PDFs and visually inspect page fit before promotion.",
        ],
        "boundary": (
            "This matrix creates no French translation, no TeX integration, no render, and no term promotion. "
            "It is a planning/control artifact for the next French completion work."
        ),
    }

    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# French Missing Unit Matrix",
        "",
        f"Generated UTC: `{payload['generated_utc']}`",
        "",
        "## Result",
        "",
        f"- Status: `{payload['status']}`",
        f"- Current French baseline: `{payload['current_french_baseline']['baseline_unit']}`",
        f"- Missing translation units: `{payload['summary']['missing_translation_unit_count']}`",
        f"- Missing unit IDs: `{', '.join(payload['summary']['missing_unit_ids'])}`",
        f"- Next translation unit: `{payload['summary']['next_translation_unit']}`",
        f"- P40 S10 decision: `{units[0]['status']}`",
        "",
        "## Matrix",
        "",
        "| Unit | Type | Status | Existing French evidence | Source witness |",
        "|---|---|---|---|---|",
    ]
    for unit in units:
        if unit["unit_id"] == "paper40_s10_stale_manifest_wording":
            evidence = "completion log + cum_fr_P40_s09"
            source = unit["source_authority"]["controlling_source"]["path"]
        else:
            evidence_count = 0
            for value in unit["existing_french_evidence"].values():
                if isinstance(value, list):
                    evidence_count += len(value)
            evidence = f"{evidence_count} file hit(s)"
            if unit["unit_type"] == "numbered_paper":
                source = unit["source_inventory_record"]["primary_german_source"]
            else:
                source = unit["source_inventory_record"]["body_tex_witness"]
        lines.append(f"| `{unit['unit_id']}` | `{unit['unit_type']}` | `{unit['status']}` | {evidence} | `{source}` |")
    lines.extend(
        [
            "",
            "## Next Actions",
            "",
        ]
    )
    for action in payload["next_actions"]:
        lines.append(f"- {action}")
    lines.extend(["", "## Boundary", "", payload["boundary"], ""])
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"json": rel(OUT_JSON), "markdown": rel(OUT_MD), "summary": payload["summary"]}, indent=2))


if __name__ == "__main__":
    main()
