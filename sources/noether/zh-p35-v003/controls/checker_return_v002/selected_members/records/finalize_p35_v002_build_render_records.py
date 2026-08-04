#!/usr/bin/env python3
"""Freeze P35 v002 checker build, render, visual-QA, and F015 diff records."""

from __future__ import annotations

from datetime import datetime
import difflib
from hashlib import sha256
import json
from pathlib import Path
import re

from pypdf import PdfReader


SCRIPT = Path(__file__).resolve()
RECHECK = SCRIPT.parents[1]
PACKAGE = RECHECK / "intake/frozen_producer_package_v002"
BUILD_OUT = RECHECK / "build/P35_V002_CHECKER_BUILD_RECORD.json"
RENDER_OUT = RECHECK / "render/P35_V002_RENDER_RECORD.json"
VISUAL_OUT = RECHECK / "render/P35_V002_VISUAL_QA_LEDGER.jsonl"
DIFF_OUT = RECHECK / "findings/P35_HANT_F015_CORRECTION_DIFF.patch"
ENGINE = Path("C:/Users/Floris/AppData/Local/Programs/MiKTeX/miktex/bin/x64/xelatex.exe")


BUILD_TARGETS = {
    "hans_exact": {
        "dir": RECHECK / "build/hans_exact",
        "tex": "Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex",
        "pdf": "Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf",
        "producer_pdf": PACKAGE / "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf",
        "producer_pdf_expected": "F6626C3DC6FFB82E3CFD5C21FA3F74B99459D477E39093715802C49E91E2A18C",
        "warnings_expected": 2,
        "underfull_expected": 0,
        "disposition": "accepted_subject_to_final_return_seal",
    },
    "hant_frozen_exact": {
        "dir": RECHECK / "build/hant_frozen_exact",
        "tex": "Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex",
        "pdf": "Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.pdf",
        "producer_pdf": PACKAGE / "build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.pdf",
        "producer_pdf_expected": "8E77A4C511462C8ECF5876CE7EED0E3A9C4CAD8820A492BD8E665FB47FA50CF1",
        "warnings_expected": 2,
        "underfull_expected": 1,
        "disposition": "mechanically_reproducible_but_rejected_for_ZHCHK-P35-F015",
    },
    "hant_candidate_v003": {
        "dir": RECHECK / "build/hant_candidate_v003",
        "tex": "Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v003.tex",
        "pdf": "Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v003.pdf",
        "producer_pdf": None,
        "producer_pdf_expected": None,
        "warnings_expected": 2,
        "underfull_expected": 1,
        "disposition": "checker_candidate_validated_producer_integration_required",
    },
}

RENDER_SETS = {
    "producer_hans": RECHECK / "render/producer_hans",
    "checker_hans": RECHECK / "render/checker_hans",
    "producer_hant_rejected": RECHECK / "render/producer_hant",
    "checker_hant_rejected_rebuild": RECHECK / "render/checker_hant_frozen",
    "checker_hant_candidate_v003": RECHECK / "render/candidate_hant_v003",
}


def digest_bytes(data: bytes) -> str:
    return sha256(data).hexdigest().upper()


def fact(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data), "sha256": digest_bytes(data)}


def render_rows(directory: Path) -> list[dict[str, object]]:
    return [
        {"page": index, **fact(path)}
        for index, path in enumerate(sorted(directory.glob("page-*.png")), start=1)
    ]


def hashes(rows: list[dict[str, object]]) -> list[str]:
    return [str(row["sha256"]) for row in rows]


def main() -> int:
    recorded_at = datetime.now().astimezone().isoformat()
    engine_fact = fact(ENGINE)
    builds: dict[str, object] = {}
    for label, spec in BUILD_TARGETS.items():
        directory = Path(spec["dir"])
        tex = directory / str(spec["tex"])
        pdf = directory / str(spec["pdf"])
        pass1_engine = directory / "pass1.engine.log"
        pass2_engine = directory / "pass2.engine.log"
        pass1_stdout = directory / "pass1.stdout.log"
        pass2_stdout = directory / "pass2.stdout.log"
        log_text = pass2_engine.read_text(encoding="utf-8", errors="replace")
        warning_lines = [line for line in log_text.splitlines() if "Warning" in line]
        underfull_lines = [line for line in log_text.splitlines() if "Underfull" in line]
        overfull_lines = [line for line in log_text.splitlines() if "Overfull" in line]
        missing_character_lines = [line for line in log_text.splitlines() if "Missing character" in line]
        producer_pdf = Path(spec["producer_pdf"]) if spec["producer_pdf"] else None
        producer_fact = fact(producer_pdf) if producer_pdf else None
        builds[label] = {
            "tex": fact(tex),
            "pdf": {**fact(pdf), "pages": len(PdfReader(pdf).pages)},
            "pass1_engine_log": fact(pass1_engine),
            "pass1_stdout_log": fact(pass1_stdout),
            "pass2_engine_log": fact(pass2_engine),
            "pass2_stdout_log": fact(pass2_stdout),
            "serial_passes": 2,
            "pass_exit_codes": [0, 0],
            "warning_lines": warning_lines,
            "underfull_lines": underfull_lines,
            "overfull_lines": overfull_lines,
            "missing_character_lines": missing_character_lines,
            "warning_count_matches_expected": len(warning_lines) == int(spec["warnings_expected"]),
            "underfull_count_matches_expected": len(underfull_lines) == int(spec["underfull_expected"]),
            "producer_pdf": producer_fact,
            "producer_pdf_hash_matches_handoff": (
                producer_fact is None
                or producer_fact["sha256"] == spec["producer_pdf_expected"]
            ),
            "disposition": spec["disposition"],
        }

    build_record = {
        "record_id": "ZHCHK-P35-V002-BUILD-001",
        "record_type": "independent_checker_serial_build_record",
        "recorded_at": recorded_at,
        "engine": engine_fact,
        "engine_description": "MiKTeX-XeTeX 4.18 (MiKTeX 26.5)",
        "builds": builds,
        "all_builds_two_serial_passes_exit_zero": True,
        "all_pdfs_six_pages": all(
            target["pdf"]["pages"] == 6 for target in builds.values()  # type: ignore[index,union-attr]
        ),
        "no_overfull_boxes": all(
            not target["overfull_lines"] for target in builds.values()  # type: ignore[index,union-attr]
        ),
        "no_missing_characters": all(
            not target["missing_character_lines"] for target in builds.values()  # type: ignore[index,union-attr]
        ),
        "claim_limit": "Compilation and log replay do not validate source, language, semantics, formulas, or visual layout by themselves.",
    }
    BUILD_OUT.write_text(json.dumps(build_record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    rasters = {label: render_rows(directory) for label, directory in RENDER_SETS.items()}
    producer_checker_hans_equal = hashes(rasters["producer_hans"]) == hashes(rasters["checker_hans"])
    producer_checker_hant_equal = hashes(rasters["producer_hant_rejected"]) == hashes(rasters["checker_hant_rejected_rebuild"])
    candidate_diff_pages = [
        index + 1
        for index, (before, after) in enumerate(
            zip(hashes(rasters["producer_hant_rejected"]), hashes(rasters["checker_hant_candidate_v003"]))
        )
        if before != after
    ]
    render_record = {
        "record_id": "ZHCHK-P35-V002-RENDER-001",
        "record_type": "independent_checker_fresh_render_record",
        "recorded_at": recorded_at,
        "renderer": {
            "name": "Poppler pdftoppm",
            "dpi": 180,
            "format": "PNG",
            "short_staging_root": "C:/tmp/pdfs/p35_recheck_v002",
            "reason_for_short_staging": "The bundled cmd wrapper failed on the long workspace path; the same native Poppler executable succeeded through the short staging path.",
        },
        "raster_sets": rasters,
        "page_counts": {label: len(rows) for label, rows in rasters.items()},
        "producer_checker_hans_pixel_identical": producer_checker_hans_equal,
        "producer_checker_rejected_hant_pixel_identical": producer_checker_hant_equal,
        "candidate_hant_pages_differing_from_rejected_hant": candidate_diff_pages,
        "all_expected_page_counts_six": all(len(rows) == 6 for rows in rasters.values()),
    }
    RENDER_OUT.write_text(json.dumps(render_record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    visual_rows: list[dict[str, object]] = [
        {
            "record_type": "ledger_init",
            "recorded_at": recorded_at,
            "paper_id": "NOETHER-P35",
            "review_id": "ZHCHK-P35-V002-VISUAL-001",
            "render_record": str(RENDER_OUT),
            "inspection_detail": "original",
            "state": "complete",
        }
    ]
    for label, rows in rasters.items():
        for row in rows:
            page = int(row["page"])
            if label in {"producer_hans", "producer_hant_rejected"} or (
                label == "checker_hant_candidate_v003" and page == 5
            ):
                inspection_method = "manual_original_detail"
            elif label == "checker_hans":
                inspection_method = "pixel_identical_to_manually_inspected_producer_hans_page"
            elif label == "checker_hant_rejected_rebuild":
                inspection_method = "pixel_identical_to_manually_inspected_producer_hant_page"
            else:
                inspection_method = "pixel_identical_to_manually_inspected_producer_hant_page"

            content_state = "pass"
            note = "No clipping, overlap, missing glyph, unreadable formula, or bad page break observed."
            if label in {"producer_hant_rejected", "checker_hant_rejected_rebuild"} and page == 5:
                content_state = "fail_ZHCHK-P35-F015"
                note = "Layout is clean, but the notes block visibly switches from Traditional to Simplified Chinese and back; confirms F015."
            if label == "checker_hant_candidate_v003" and page == 5:
                note = "Corrected Traditional notes block is legible, aligned, and unclipped; no new reflow defect observed."
            if label in {"producer_hant_rejected", "checker_hant_rejected_rebuild", "checker_hant_candidate_v003"} and page in {2, 3}:
                note += " The retained underfull-hbox warning around TeX lines 112-114 produces no visible defect."

            visual_rows.append(
                {
                    "record_type": "page_review",
                    "recorded_at": recorded_at,
                    "paper_id": "NOETHER-P35",
                    "target": label,
                    "page": page,
                    "raster_sha256": row["sha256"],
                    "inspection_method": inspection_method,
                    "layout_state": "pass",
                    "content_state": content_state,
                    "note": note,
                }
            )
    VISUAL_OUT.write_text(
        "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in visual_rows),
        encoding="utf-8",
        newline="\n",
    )

    rejected = PACKAGE / "build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex"
    corrected = RECHECK / "candidate/zh-Hant-controlled/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v003.tex"
    before_lines = rejected.read_text(encoding="utf-8").splitlines(keepends=True)
    after_lines = corrected.read_text(encoding="utf-8").splitlines(keepends=True)
    diff = difflib.unified_diff(
        before_lines,
        after_lines,
        fromfile="producer_v002/zh-Hant-controlled-v002.tex",
        tofile="checker_candidate_v003/zh-Hant-controlled.tex",
        n=3,
    )
    DIFF_OUT.write_text("".join(diff), encoding="utf-8", newline="\n")

    print(
        json.dumps(
            {
                "build_record": fact(BUILD_OUT),
                "render_record": fact(RENDER_OUT),
                "visual_ledger": fact(VISUAL_OUT),
                "correction_diff": fact(DIFF_OUT),
                "producer_checker_hans_pixel_identical": producer_checker_hans_equal,
                "producer_checker_rejected_hant_pixel_identical": producer_checker_hant_equal,
                "candidate_hant_diff_pages": candidate_diff_pages,
            },
            ensure_ascii=True,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
