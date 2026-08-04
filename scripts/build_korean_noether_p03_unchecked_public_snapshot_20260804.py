#!/usr/bin/env python3
"""Freeze and privacy-project the bounded Korean Noether Paper 3 handoff."""

from __future__ import annotations

import json
from pathlib import Path

import build_korean_noether_unchecked_public_snapshots_20260804 as engine


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = (
    engine.SOURCE_BASE / "noether_paper03_ko_translation_001_20260804"
)
PRIVATE_ROOT = (
    engine.CJK_CONTROL.parent
    / "90_logs"
    / "private_archive_custody"
    / "KOREAN_NOETHER_P03_SNAPSHOT_20260804_r1"
)
HANDOFF_CJK_LOG_BYTES = 609_367
HANDOFF_CJK_LOG_SHA256 = (
    "4FD40DC661474165665E8CAF4BB9021FA7084E836CA6840018FE3E9B1D453187"
)
PUBLIC_ROOT = (
    REPO_ROOT / "sources" / "noether" / "korean-unchecked-paper-03-20260804"
)
CONFIG = {
    "root": SOURCE_ROOT.name,
    "targets": 3,
    "structural": "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl",
    "difficulty": "evidence/difficulty/difficulty_ledger.jsonl",
}

EXPECTED = {
    SOURCE_ROOT / "targets" / "Noether_P03_Korean_U01_UNCHECKED.tex": (
        3_209,
        "057D6EAECAAB02C4D19C6908276C11E32953748726BD36B628712AB5C5E78ECB",
    ),
    SOURCE_ROOT / "targets" / "Noether_P03_Korean_U02_UNCHECKED.tex": (
        4_468,
        "A2A9F68B55C15EEFEAE178B4F24CB5D56222E563F6B5A126F46D1AA75BEA38B1",
    ),
    SOURCE_ROOT / "targets" / "Noether_P03_Korean_U03_UNCHECKED.tex": (
        4_131,
        "7942126177C707C89F67444BE020F90F2139C0C5036A153297C0A7F83119F4B4",
    ),
    SOURCE_ROOT / "SOURCE_CUSTODY.md": (
        2_433,
        "0475B7BED3D5190C4A6C29D75F8E4FD7BB5E74DB4D943AB54E729E4696A252A5",
    ),
    SOURCE_ROOT / "STATUS.md": (
        2_955,
        "AFC0DFA2EB79BCBDBEF04E7CB7E06C250E938CD70E171A50FAB0E54F6A19078D",
    ),
    SOURCE_ROOT / "CHECKER_HANDOFF_U01_U03.md": (
        3_373,
        "6394663B34D6A654A8BD8D2864EC5EF13E2F25150FA8EDE04FC257A3706585EA",
    ),
    SOURCE_ROOT / "TRANSLATION_CHOICES_U01_U03.md": (
        6_157,
        "3299C07345D907C6FA387EBB2B18A7E656EF95A6181F4D38EC07EED402ED4AB3",
    ),
    SOURCE_ROOT / "evidence" / "structural_index" / "PRODUCER_STRUCTURAL_INDEX.jsonl": (
        310_637,
        "F2D3B6D6FE6DE0837AFF24CF2A314B8A7F8C4F6DFE78D8E2D91E8AD5B052EAE0",
    ),
    SOURCE_ROOT / "evidence" / "difficulty" / "difficulty_ledger.jsonl": (
        57_815,
        "861F7C2B62696214AABAE435FCD3A97B77E291495BAB549F98DFEBDAC2803DF9",
    ),
    SOURCE_ROOT / "evidence" / "visual" / "visual_evidence_index.jsonl": (
        0,
        "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855",
    ),
    engine.CJK_CONTROL / "KOREAN_ARCHIVE_PUBLICATION_POLICY_RECEIPT_20260804.md": (
        2_552,
        "9BD4FEA2B6116896DDCAA0840F159965E5AD3AB478C37EF7EE99CA144B2D83AB",
    ),
    engine.METHODOLOGY_SOURCE: (
        136_992,
        "CA9ECB51C813FADBBBBB6C7F1EA5888D94A406D3EB2F5558306F89E3F9BFDB9D",
    ),
    engine.POINTER_SOURCE: (
        15_345,
        "932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197",
    ),
}


def assert_exact(path: Path, expected: tuple[int, str]) -> None:
    observed = (path.stat().st_size, engine.sha256_file(path))
    if observed != expected:
        raise RuntimeError(f"Exact P03 handoff identity changed: {path}: {observed!r}")


def project_control_bytes(data: bytes, source_name: str, destination: Path) -> dict:
    transformed, applied = engine.transform_text(data)
    engine.assert_privacy_clean(destination.name, transformed)
    destination.write_bytes(transformed)
    return {
        "filename": destination.name,
        "source_name": source_name,
        "source_bytes": len(data),
        "source_sha256": engine.sha256_bytes(data),
        "public_bytes": len(transformed),
        "public_sha256": engine.sha256_bytes(transformed),
        "privacy_occurrences": sum(count for _, count in applied),
    }


def main() -> int:
    if PRIVATE_ROOT.exists() or PUBLIC_ROOT.exists():
        raise RuntimeError("P03 snapshot output already exists; never overwrite a frozen revision")
    source_rows = engine.inventory(SOURCE_ROOT)
    if len(source_rows) != 33 or sum(int(row["bytes"]) for row in source_rows) != 848_460:
        raise RuntimeError("P03 bounded producer root count/bytes changed")
    for path, expected in EXPECTED.items():
        assert_exact(path, expected)
    current_cjk_log = (
        engine.CJK_CONTROL / "CJK_DECISION_LOGBOOK_20260718.md"
    ).read_bytes()
    handoff_cjk_log = current_cjk_log[:HANDOFF_CJK_LOG_BYTES]
    if (
        len(handoff_cjk_log) != HANDOFF_CJK_LOG_BYTES
        or engine.sha256_bytes(handoff_cjk_log) != HANDOFF_CJK_LOG_SHA256
    ):
        raise RuntimeError("Exact append-only P03 handoff log prefix is not recoverable")

    engine.PRIVATE_ROOT = PRIVATE_ROOT
    engine.PUBLIC_ROOT = PUBLIC_ROOT
    engine.EXCLUDED_RELATIVE_PATHS = {}
    PRIVATE_ROOT.mkdir(parents=True)
    PUBLIC_ROOT.mkdir(parents=True)
    paper = engine.build_paper("P03", CONFIG)

    common_sources = [
        (
            engine.CJK_CONTROL / "KOREAN_ARCHIVE_PUBLICATION_POLICY_RECEIPT_20260804.md",
            "70_KO_ARCHIVE_PUBLICATION_POLICY_RECEIPT_20260804.md",
        ),
        (
            engine.CJK_CONTROL / "CJK_DECISION_LOGBOOK_20260718.md",
            "70_KO_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md",
        ),
        (
            engine.METHODOLOGY_SOURCE,
            "70_KO_CJK_PRODUCTION_METHODOLOGY_PRIVACY_CLEAN_20260804.md",
        ),
        (
            engine.ARCHIVE_WIDE_POLICY,
            "70_KO_ARCHIVE_WIDE_IMMEDIATE_PUBLICATION_NO_HOLD_POLICY_20260804.md",
        ),
        (
            engine.POINTER_SOURCE,
            "70_KO_NOETH_DE_AUTHORITY_POINTER_v003_20260804.json",
        ),
    ]
    raw_controls = [
        (name, source.read_bytes()) for source, name in common_sources
        if source.name != "CJK_DECISION_LOGBOOK_20260718.md"
    ]
    raw_controls.append(
        ("70_KO_CJK_DECISION_LOGBOOK_HANDOFF_EXACT_20260804.md", handoff_cjk_log)
    )
    raw_controls.sort(key=lambda row: row[0])
    private_controls_zip = (
        PRIVATE_ROOT / "P03_COMMON_CONTROLS_EXACT_PRIVATE_SNAPSHOT_20260804.zip"
    )
    engine.deterministic_zip(private_controls_zip, raw_controls)
    private_control_members = [
        {
            "filename": name,
            "bytes": len(data),
            "sha256": engine.sha256_bytes(data),
        }
        for name, data in raw_controls
    ]
    common = []
    for source, name in common_sources:
        data = (
            handoff_cjk_log
            if source.name == "CJK_DECISION_LOGBOOK_20260718.md"
            else source.read_bytes()
        )
        common.append(project_control_bytes(data, str(source), PUBLIC_ROOT / name))

    index_path = PUBLIC_ROOT / "70f_KO_P03_SNAPSHOT_INDEX_20260804.csv"
    engine.write_csv(
        index_path,
        [
            "paper",
            "source_files",
            "source_bytes",
            "source_tree_sha256",
            "public_source_files",
            "privacy_occurrences",
            "excluded_files",
            "public_zip",
            "public_zip_bytes",
            "public_zip_sha256",
            "public_zip_members",
            "target_units",
            "structural_relative_path",
            "difficulty_relative_path",
            "state",
        ],
        [
            {
                **{key: value for key, value in paper.items() if not key.startswith("private_")},
                "state": "UNCHECKED;uncompiled;unrendered;unassembled;unreviewed",
            }
        ],
    )
    readme_path = PUBLIC_ROOT / "README.md"
    engine.write_text(
        readme_path,
        """# Korean Noether Paper 3 — bounded public snapshot

This snapshot preserves all 33 files in the bounded Paper 3 producer root: three editable Korean TeX units, source custody/status/checker/translation-choice documents, the complete 148-record structural index, the append-only 14-record difficulty/failure history, zero-image visual evidence, validators, scripts, and continuation surfaces.

State: **UNCHECKED, uncompiled, unrendered, unassembled, and unreviewed**. These are honest scope labels, not release holds. Archive maintenance performed no source correction, mathematical or linguistic review, compilation, rendering, assembly, certification, or approval.

The complete privacy-clean ZIP is the coherent public projection. Exact producer bytes are separately frozen in private custody. Public transformations replace only private local path/operator tokens; no producer file is excluded, and no image or special-rights byte exists in this handoff.
""",
    )
    before_validation = engine.inventory(PUBLIC_ROOT)
    validation = {
        "schema": "korean_noether_p03_public_snapshot_closeout_v1",
        "status": "PASS_READY_FOR_SAME_CONCEPT_PUBLICATION",
        "errors": [],
        "paper": paper,
        "common_controls": common,
        "private_common_controls_zip": {
            "path": str(private_controls_zip),
            "bytes": private_controls_zip.stat().st_size,
            "sha256": engine.sha256_file(private_controls_zip),
            "members": private_control_members,
        },
        "public_root_files_excluding_this_validation": len(before_validation),
        "public_root_bytes_excluding_this_validation": sum(
            int(row["bytes"]) for row in before_validation
        ),
        "public_root_tree_sha256_excluding_this_validation": engine.tree_sha(
            before_validation
        ),
        "private_custody_root": str(PRIVATE_ROOT),
        "public_projection_root": str(PUBLIC_ROOT),
        "total_source_files": 33,
        "total_source_bytes": 848_460,
        "total_target_units": 3,
        "total_explicit_exclusions": 0,
        "compile_performed": False,
        "render_performed": False,
        "review_performed": False,
        "release_hold": False,
    }
    validation_path = PUBLIC_ROOT / "SNAPSHOT_VALIDATION.json"
    engine.write_json(validation_path, validation)
    final_rows = engine.inventory(PUBLIC_ROOT)
    result = {
        **validation,
        "public_root_files": len(final_rows),
        "public_root_bytes": sum(int(row["bytes"]) for row in final_rows),
        "public_root_tree_sha256": engine.tree_sha(final_rows),
        "validation_path": str(validation_path),
        "validation_bytes": validation_path.stat().st_size,
        "validation_sha256": engine.sha256_file(validation_path),
        "index_path": str(index_path),
        "index_bytes": index_path.stat().st_size,
        "index_sha256": engine.sha256_file(index_path),
        "readme_bytes": readme_path.stat().st_size,
        "readme_sha256": engine.sha256_file(readme_path),
    }
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
