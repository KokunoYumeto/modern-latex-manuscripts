import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "20260702T011500Z"
OUT_JSON = ROOT / "logs" / f"VISUAL_INSPECTION_COVERAGE_LEDGER_{STAMP}.json"
OUT_MD = ROOT / "logs" / f"VISUAL_INSPECTION_COVERAGE_LEDGER_{STAMP}.md"


VISUAL_PATTERNS = re.compile(r"(visual|contact|render|pdf|page|inspection)", re.IGNORECASE)


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def read_json(rel_path: str) -> dict:
    return json.loads((ROOT / rel_path).read_text(encoding="utf-8-sig"))


def file_record(path: Path) -> dict:
    return {
        "path": rel(path),
        "bytes": path.stat().st_size,
        "modified_utc": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
    }


def find_files(root: str, suffix: str) -> list[Path]:
    base = ROOT / root
    if not base.exists():
        return []
    return sorted(p for p in base.rglob(f"*{suffix}") if p.is_file())


def classify_pdf(path: Path) -> str:
    s = rel(path).lower()
    if "simplified_chinese" in s or "zh" in s:
        return "simplified_chinese"
    if "japanese" in s:
        return "japanese"
    if "spanish" in s or "cum_es" in s:
        return "spanish"
    if "french" in s or "cum_fr" in s:
        return "french"
    if "ukrainian" in s:
        return "ukrainian"
    if "russian" in s:
        return "russian"
    if "interslavic_cyrillic" in s or "interslavic-cyrillic" in s:
        return "interslavic_cyrillic"
    if "interslavic" in s:
        return "interslavic_latin"
    if "cumulative" in s:
        return "cumulative_other"
    return "other"


def page_count(path: Path) -> int | None:
    # Prefer pypdf when available; avoid failing the ledger if a PDF is malformed.
    try:
        from pypdf import PdfReader

        return len(PdfReader(str(path)).pages)
    except Exception:
        return None


def scan_log_refs(log_paths: list[Path]) -> dict[str, list[str]]:
    refs: dict[str, list[str]] = {}
    for path in log_paths:
        if path.stat().st_size > 2_500_000:
            continue
        text = path.read_text(encoding="utf-8-sig", errors="ignore")
        if not VISUAL_PATTERNS.search(path.name) and not VISUAL_PATTERNS.search(text[:5000]):
            continue
        for match in re.finditer(r"[\w./\\-]+\.pdf", text, flags=re.IGNORECASE):
            token = match.group(0).replace("\\", "/").strip("`'\"),.;:")
            refs.setdefault(token.lower(), []).append(rel(path))
    return refs


def record_refs(pdf: Path, refs: dict[str, list[str]]) -> list[str]:
    pdf_rel = rel(pdf).lower()
    name = pdf.name.lower()
    hits = []
    for token, log_list in refs.items():
        if token in pdf_rel or name == Path(token).name.lower():
            hits.extend(log_list)
    return sorted(set(hits))


def main() -> None:
    pdfs = find_files("renders", ".pdf")
    visual_files = [
        p
        for p in find_files("visual_inspection", ".png")
        + find_files("visual_inspection", ".jpg")
        + find_files("visual_inspection", ".jpeg")
        + find_files("visual_inspection", ".pdf")
        + find_files("visual_inspection", ".md")
        + find_files("visual_inspection", ".json")
    ]
    log_paths = find_files("logs", ".md") + find_files("logs", ".json")
    refs = scan_log_refs(log_paths)

    key_manifests = {
        "slavic": read_json("logs/SLAVIC_MAINTENANCE_STATUS_MANIFEST_20260701T204500Z.json"),
        "spanish": read_json("logs/SPANISH_CUMULATIVE_STATUS_MANIFEST_20260701T160000Z.json"),
        "french": read_json("logs/FRENCH_CUMULATIVE_STATUS_MANIFEST_20260701T161500Z.json"),
        "chinese_japanese": read_json("logs/CHINESE_JAPANESE_CUMULATIVE_STATUS_MANIFEST_20260701T170500Z.json"),
        "cross_lane": read_json("logs/CROSS_LANE_PROMOTION_READINESS_AUDIT_20260702T003500Z.json"),
    }

    records = []
    for pdf in pdfs:
        kind = classify_pdf(pdf)
        ref_logs = record_refs(pdf, refs)
        important = (
            "cumulative" in rel(pdf).lower()
            or kind
            in {
                "simplified_chinese",
                "japanese",
                "spanish",
                "french",
                "ukrainian",
                "russian",
                "interslavic_latin",
                "interslavic_cyrillic",
            }
        )
        if not important and len(records) > 250:
            continue
        rec = file_record(pdf)
        rec.update(
            {
                "lane": kind,
                "page_count": page_count(pdf),
                "referenced_by_visual_or_render_logs": ref_logs,
                "has_visual_or_render_log_reference": bool(ref_logs),
                "promotion_visual_gate": "covered_by_existing_log" if ref_logs else "needs_visual_inspection_before_promotion",
            }
        )
        records.append(rec)

    lane_summary: dict[str, dict] = {}
    for rec in records:
        lane = rec["lane"]
        item = lane_summary.setdefault(
            lane,
            {
                "pdf_count": 0,
                "pdfs_with_visual_or_render_log_reference": 0,
                "pdfs_needing_visual_inspection_before_promotion": 0,
                "total_pages_counted": 0,
                "page_count_unknown": 0,
            },
        )
        item["pdf_count"] += 1
        if rec["has_visual_or_render_log_reference"]:
            item["pdfs_with_visual_or_render_log_reference"] += 1
        else:
            item["pdfs_needing_visual_inspection_before_promotion"] += 1
        if rec["page_count"] is None:
            item["page_count_unknown"] += 1
        else:
            item["total_pages_counted"] += rec["page_count"]

    priority = [
        rec
        for rec in records
        if rec["promotion_visual_gate"] == "needs_visual_inspection_before_promotion"
        and rec["lane"]
        in {
            "simplified_chinese",
            "japanese",
            "spanish",
            "french",
            "ukrainian",
            "russian",
            "interslavic_latin",
            "interslavic_cyrillic",
            "cumulative_other",
        }
    ][:120]

    result = {
        "artifact": "visual_inspection_coverage_ledger",
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "completion_claim": False,
        "scope": "Rendered PDF visual/render-log coverage audit for promotion discipline; no new visual inspection performed.",
        "tooling": {
            "pypdf_page_count_available": True,
            "visual_log_reference_method": "PDF path/name references in visual/render/contact-sheet logs.",
        },
        "manifest_anchors": {
            "slavic": "logs/SLAVIC_MAINTENANCE_STATUS_MANIFEST_20260701T204500Z.json",
            "spanish": "logs/SPANISH_CUMULATIVE_STATUS_MANIFEST_20260701T160000Z.json",
            "french": "logs/FRENCH_CUMULATIVE_STATUS_MANIFEST_20260701T161500Z.json",
            "chinese_japanese": "logs/CHINESE_JAPANESE_CUMULATIVE_STATUS_MANIFEST_20260701T170500Z.json",
            "cross_lane": "logs/CROSS_LANE_PROMOTION_READINESS_AUDIT_20260702T003500Z.json",
        },
        "inventory": {
            "render_pdf_count_scanned": len(pdfs),
            "visual_inspection_file_count": len(visual_files),
            "visual_or_render_log_reference_count": len(refs),
            "ledger_pdf_records": len(records),
        },
        "lane_summary": lane_summary,
        "priority_visual_inspection_queue": priority,
        "current_decision": {
            "new_visual_inspection_performed": False,
            "promotion_allowed_from_this_ledger_alone": False,
            "reason": "This ledger inventories existing visual/render evidence and queues missing visual checks; it does not inspect pages itself.",
        },
        "rules": [
            "Before public promotion of any cumulative reader, require explicit visual inspection notes or contact-sheet evidence for sampled front/middle/back pages and any known dense formula/table pages.",
            "A successful TeX compile is not the same as visual inspection.",
            "A render-log reference can support continuity but does not by itself close native/external authority gates.",
            "When a correction changes TeX that affects layout, regenerate the PDF and refresh visual inspection evidence.",
        ],
    }

    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Visual Inspection Coverage Ledger",
        "",
        f"- Generated UTC: `{result['generated_utc']}`",
        f"- Completion claim: `{result['completion_claim']}`",
        f"- Render PDFs scanned: `{result['inventory']['render_pdf_count_scanned']}`",
        f"- Visual-inspection files found: `{result['inventory']['visual_inspection_file_count']}`",
        f"- New visual inspection performed: `{result['current_decision']['new_visual_inspection_performed']}`",
        "",
        "## Lane Summary",
        "",
        "| Lane | PDFs | With visual/render refs | Needing inspection | Pages counted | Unknown pages |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for lane, summary in sorted(lane_summary.items()):
        lines.append(
            f"| {lane} | {summary['pdf_count']} | {summary['pdfs_with_visual_or_render_log_reference']} | "
            f"{summary['pdfs_needing_visual_inspection_before_promotion']} | {summary['total_pages_counted']} | "
            f"{summary['page_count_unknown']} |"
        )
    lines.extend(["", "## Priority Queue", ""])
    for rec in priority[:40]:
        lines.append(f"- `{rec['path']}` ({rec['lane']}, pages `{rec['page_count']}`): {rec['promotion_visual_gate']}")
    lines.extend(["", "## Rules", ""])
    for rule in result["rules"]:
        lines.append(f"- {rule}")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"json": rel(OUT_JSON), "markdown": rel(OUT_MD), "pdf_records": len(records)}, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
