#!/usr/bin/env python3
"""Freeze the exact v038 release manifest, README, and owner handoff record."""

from __future__ import annotations

import hashlib
import json
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "release"
SOURCE = RELEASE / "source"
PDF = RELEASE / "pdf"
EVIDENCE = RELEASE / "evidence"
VISUAL = RELEASE / "visual"
LANE = ROOT.parent
DECISION_LOG = LANE / "00_lane_control" / "SLAVIC_INTERSLAVIC_DECISION_LOG_v1.jsonl"
DIFFICULTY_LOG = (
    LANE
    / "00_lane_control"
    / "difficulty_ledger"
    / "SLAVIC_INTERSLAVIC_DIFFICULTY_LEDGER_v1.jsonl"
)
LESSONS = (
    ROOT.parents[3]
    / "04_handoffs"
    / "methodology_lessons_20260718"
    / "SLAVIC_INTERSLAVIC_MANAGER_LESSONS_20260718.md"
)
TARGETS = ("ru", "uk", "isv", "isv-cy")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def record(path: Path, role: str, disposition: str = "proposed_public") -> dict:
    return {
        "role": role,
        "disposition": disposition,
        "path": path.resolve().as_posix(),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def last_jsonl(path: Path) -> dict:
    lines = [line for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    return json.loads(lines[-1])


def main() -> int:
    qa_path = EVIDENCE / "qa_report.json"
    qa = json.loads(qa_path.read_text(encoding="utf-8"))
    if not qa["pass"]:
        raise RuntimeError("release QA is not PASS")
    build = json.loads((EVIDENCE / "build_manifest.json").read_text(encoding="utf-8"))
    pages = {item["target"]: item["pdf"]["pages"] for item in build["cumulative_records"]}
    latest_decision = last_jsonl(DECISION_LOG)
    latest_difficulty = last_jsonl(DIFFICULTY_LOG)

    # Copy current lane-level evidence into the bounded payload; original custody
    # paths remain unchanged and are recorded inside each report.
    for name in (
        "human_unit_validation.json",
        "authority_reconciliation_v038.json",
        "human_edited_ed0004_incomplete_snapshot.json",
    ):
        shutil.copy2(ROOT / "evidence" / name, EVIDENCE / name)

    reconciliation = json.loads(
        (EVIDENCE / "authority_reconciliation_v038.json").read_text(encoding="utf-8")
    )
    lineage_dependencies = []
    for item in reconciliation["numbered_paper_bases"]:
        lineage_dependencies.append(
            {
                "surface": item["surface"],
                "archive_normalized_tex": item["archive_normalized_tex"],
                "producer_v014_pdf": item["producer_v014_pdf"],
                "disposition": (
                    "exact lineage source retained in existing custody; not duplicated as a proposed public file"
                ),
            }
        )

    proposed = []
    for target in TARGETS:
        proposed.append(record(PDF / f"noether-{target}-v038.pdf", "complete cumulative reader PDF"))
        proposed.append(
            record(SOURCE / f"noether-{target}-v038.tex", "portable cumulative pdfpages TeX recipe")
        )
        proposed.append(
            record(
                SOURCE / f"base-papers1-43-{target}.tex",
                "exact editable archive-normalized Papers 1--43 base source",
            )
        )
        proposed.append(
            record(PDF / f"base-papers1-43-{target}.pdf", "rebuilt Papers 1--43 base PDF")
        )
        for stem in ("44-book", "45", "bib"):
            proposed.append(record(SOURCE / f"{stem}-{target}.tex", "editable post-P43 TeX source"))
            proposed.append(record(PDF / f"{stem}-{target}.pdf", "standalone post-P43 component PDF"))

    evidence_names = (
        "source_assembly.json",
        "inherited_continuation_audit.json",
        "german_authority_source_conflicts_v038.json",
        "build_manifest.json",
        "qa_report.json",
        "human_unit_validation.json",
        "authority_reconciliation_v038.json",
        "human_edited_ed0004_incomplete_snapshot.json",
        "structural_index_schema.json",
        "structural_index.jsonl",
        "structural_index.csv",
        "structural_index_build_report.json",
        "structural_index_validation.json",
        "visual_render_manifest.json",
        "visual_review.json",
        "visual_evidence_schema.json",
        "visual_evidence_index.jsonl",
        "visual_evidence_index.csv",
        "visual_evidence_build_report.json",
        "visual_evidence_validation.json",
    )
    for name in evidence_names:
        proposed.append(record(EVIDENCE / name, "reproducibility/review evidence"))
    for image in sorted(VISUAL.rglob("*.png")):
        proposed.append(
            record(
                image,
                "project-generated visual QA evidence",
                "proposed_public_subject_to_archive_owner_underlying_text_rights_decision",
            )
        )

    rights_blocked_files = [
        record(
            path,
            "source-scan research-evidence render",
            "rights_blocked_not_proposed_public",
        )
        for path in sorted((RELEASE / "rights_blocked").rglob("*"))
        if path.is_file()
    ]

    tool_names = (
        "extract_authority_units.py",
        "validate_human_units.py",
        "transliterate_isv_cyrillic.py",
        "reconcile_authority_v038.py",
        "assemble_release_sources.py",
        "validate_inherited_continuations.py",
        "build_release.py",
        "build_structural_index.py",
        "validate_structural_index.py",
        "render_visual_qa.py",
        "build_visual_index.py",
        "validate_visual_index.py",
        "qa_release.py",
        "build_handoff.py",
    )
    release_tools = RELEASE / "tools"
    release_tools.mkdir(parents=True, exist_ok=True)
    for name in tool_names:
        copied = release_tools / name
        shutil.copy2(ROOT / "tools" / name, copied)
        proposed.append(record(copied, "reproducibility tool"))

    manifest = {
        "schema": "noether-slavic-v038-release-manifest/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "authority": {
            "pointer_id": "NOETH-DE-AUTH-v038-20260805",
            "pointer_sha256": "666FCB863C8599778BB1B48DCD0D4E444D6486133B7FE703E6CDE073F15FFBAE",
            "german_authority_id": "NOETH-DE-ED-0005",
            "german_authority_sha256": "1A44F967B29972E8F99E5C323A479162AD82A23FC457395915A4BB9DDF51AD41",
            "post_p43_identity_sha256": "662BBFC0926381E0D45A2356BF19959FCAEE6282F6F049E85B0BD5D553E80B58",
        },
        "scope": {
            "numbered_paper_base": (
                "complete numbered Papers 1--43 / 219 exact units per surface, rebuilt from archive-normalized editable TeX"
            ),
            "new_continuation": "BOOK_TITLE_INTRO, BOOK_S01--BOOK_S31, POST45, POSTBIB",
            "numbered_paper_surface_units": 876,
            "new_continuation_surface_units": 136,
            "total_surface_units": 1012,
            "new_model_authored_section_units": 93,
            "deterministic_cyrillic_section_projections": 31,
            "editable_release_source_files": 20,
            "cumulative_pages": pages,
            "continuation_cursor": (
                "ED0005 line 24145 / POSTBIB terminal unit; next verified German authority change or native-language review"
            ),
        },
        "proposed_files": proposed,
        "rights_blocked_files_not_proposed_public": rights_blocked_files,
        "lineage_dependencies_not_duplicated": lineage_dependencies,
        "counts": {
            "proposed_files": len(proposed),
            "proposed_bytes": sum(item["bytes"] for item in proposed),
            "rights_blocked_files": len(rights_blocked_files),
            "rights_blocked_bytes": sum(item["bytes"] for item in rights_blocked_files),
            "lineage_dependency_surfaces": len(lineage_dependencies),
        },
        "review_state": {
            "build": "two-pass serial XeLaTeX PASS for each base, component, and cumulative recipe",
            "structure_and_formula": (
                "93 editable post-P43 section units PASS; ED0005 P06 loci PASS on four numbered-paper bases; deterministic Cyrillic projection PASS"
            ),
            "text_and_page": "PASS",
            "visual": "bounded rendered samples reopened PASS",
            "language": "model-authored; no independent native-speaker review",
            "source_claim": (
                "reconciled against exact ED0005 authority, with explicit direct-source exceptions retained where "
                "ED0005 conflicts with the surviving witnesses: five Post45 equation groups, the Bertini reading "
                "x^2-y^5, and nine PostBibliography loci. Exact locators are in "
                "german_authority_source_conflicts_v038.json. No native-language certification, independent full "
                "original-print reaudit, or source-certification claim is made"
            ),
        },
        "rights": {
            "source_images": (
                "one exact source-scan page render is preserved under release/rights_blocked/source_visual; "
                "redistribution rights are unresolved, so the image is excluded from proposed public files and "
                "only its hash/page/coordinate metadata is proposed"
            ),
            "visuals": (
                "project-generated QA renders/contact sheets; underlying-text redistribution status not independently reassessed; archive owner decides publication"
            ),
        },
        "supersession": [
            "v014 cumulative Slavic readers as latest cumulative endpoint (retained as exact lineage)",
            "r19 Slavic top-level Papers 1--43 files as latest complete Global German endpoint",
            "interrupted incomplete ED0004 post-P43 human-edited pass (retained as adverse lineage)",
            "2026-06-28 cumulative readers",
            "old synopsis-heavy Post44 files as candidate complete current Work 44 translations",
        ],
    }
    manifest_path = RELEASE / "release_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    page_lines = "\n".join(f"- `{target}`: {pages[target]} pages" for target in TARGETS)
    readme_text = f"""# Noether Slavic cumulative readers — v038

This bounded checkpoint rebuilds the complete 219-unit Papers 1–43 bases and adds the complete post-P43 continuation: the 31-section 1929/30 lecture book, the Kapferer–Noether item, and the post-numbered bibliography. The exact German alignment authority is `NOETH-DE-ED-0005` under pointer `NOETH-DE-AUTH-v038-20260805`.

## Reader pages

{page_lines}

Russian, Ukrainian, and Latin Interslavic Sections 1–31 are model-authored translations checked against exact per-paragraph mathematical/TeX occurrence invariants. They have not received independent native-speaker review. Cyrillic Interslavic is a deterministic reader projection of Latin Interslavic and is not an independent translation witness.

Each cumulative TeX file is a portable `pdfpages` recipe over four locally rebuilt, hash-bound components. Exact editable Papers 1–43 base TeX, complete editable Work 44/Post45/PostBib TeX, and standalone PDFs for every component are included. The prior v014 and r19 artifacts remain exact lineage and are not duplicated as proposed public files. One Post45 target reading, Bertini's example `x^2-y^5`, is preserved from the direct witness and scan even though German ED0005 says `x^2+y^3`; the discrepancy is explicit evidence for German-canon adjudication, not a silent target divergence.

Build, source, structure, page, text-extraction, render, and bounded visual-review evidence is hash-bound in `release_manifest.json`. This checkpoint claims exact ED0005 reconciliation with the explicitly logged direct-source exceptions above; it does not claim native certification, an independent original-print reaudit, a critical edition, or independent source certification.
"""
    readme_path = RELEASE / "README.md"
    readme_path.write_text(readme_text, encoding="utf-8", newline="\n")

    handoff = {
        "schema": "noether-slavic-v038-owner-handoff/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "payload_path": RELEASE.resolve().as_posix(),
        "scope": manifest["scope"],
        "authority": manifest["authority"],
        "public_caveats": manifest["review_state"],
        "rights": manifest["rights"],
        "proposed_public_file_count": len(proposed) + 2,
        "proposed_public_files": proposed
        + [record(manifest_path, "release manifest"), record(readme_path, "public README")],
        "rights_blocked_files_not_proposed_public": rights_blocked_files,
        "lineage_dependencies_not_duplicated": lineage_dependencies,
        "build_render_source_review_evidence": {
            "qa": record(qa_path, "release QA"),
            "decision_log": {
                **record(
                    DECISION_LOG,
                    "append-only lane decision log",
                    "custody_reference_not_duplicated_in_payload",
                ),
                "latest_decision_id": latest_decision["decision_id"],
            },
            "difficulty_ledger": {
                **record(
                    DIFFICULTY_LOG,
                    "append-only difficulty ledger",
                    "custody_reference_not_duplicated_in_payload",
                ),
                "latest_issue_id": latest_difficulty["issue_id"],
            },
            "methodology_lessons": record(
                LESSONS,
                "private methodology-synthesis intake",
                "custody_reference_not_duplicated_in_public_payload",
            ),
        },
        "superseded": manifest["supersession"],
        "continuation_cursor": manifest["scope"]["continuation_cursor"],
        "archive_owner": {
            "thread_id": "019fca5c-0e73-7c72-92fb-5b507b710598",
            "instruction": (
                "Owner decides GitHub/Zenodo publication and rights disposition; do not create a competing draft."
            ),
        },
    }
    handoff_path = RELEASE / "HANDOFF.json"
    handoff_path.write_text(
        json.dumps(handoff, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "payload": RELEASE.resolve().as_posix(),
                "manifest": record(manifest_path, "release manifest"),
                "readme": record(readme_path, "public README"),
                "handoff": record(handoff_path, "owner handoff"),
                "pages": pages,
                "latest_decision": latest_decision["decision_id"],
                "latest_difficulty": latest_difficulty["issue_id"],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
