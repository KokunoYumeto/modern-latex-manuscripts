#!/usr/bin/env python3
"""Freeze and project the sealed EGA I printed-p.138 R61/R82 checkpoint.

The producer roots remain mutable.  This script accepts only the exact sealed
R61/R82 identities, writes an immutable raw private custody tree, and derives a
separate minimally transformed public projection.  It never writes into either
producer root and it excludes the NUMDAM scan and authority-page images.
"""

from __future__ import annotations

import csv
import importlib.util
import json
import re
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "ega_p127_builder", SCRIPT_DIR / "build_ega_p127_custody_projection_20260803.py"
)
if _spec is None or _spec.loader is None:
    raise RuntimeError("cannot load the bounded predecessor builder")
base = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(base)
# TeX build logs and sidecars are textual provenance surfaces and must pass
# through the same path/task/email transformation as source and ledgers.
base.TEXT_SUFFIXES.update({".aux", ".log", ".out"})

WORKTREE = SCRIPT_DIR.parent
PROJECT_ROOT = Path(r"C:\Users\Floris\Documents\interlanguage")
LANE_ROOT = PROJECT_ROOT / r"03_projects\language_management\english_germanic"
FRENCH_ROOT = (
    PROJECT_ROOT
    / r"Transcription\03_working_transcriptions\EGA_French_NUMDAM_canonical_TeX_20260801_r1"
)
ENGLISH_ROOT = (
    LANE_ROOT
    / r"03_working_translations\EGA_English_Global_0_IV_french_recheck_source_successor_20260802_r1"
)
LANE_CONTROL = LANE_ROOT / "00_lane_control"
PRIVATE_FINAL = (
    LANE_ROOT
    / r"90_logs\private_archive_custody\EGA_I_P138_R61_R82_PRIVATE_RAW_CUSTODY_20260804_r1"
)
PUBLIC_FINAL = (
    WORKTREE
    / r"sources\ega\checkpoints\ega1-p138-diplomatic-prestacks-r1-20260804"
)

R82_MANIFEST = ENGLISH_ROOT / r"controls\SOURCE_INPUT_SHA256_R82.json"
R81_MANIFEST = ENGLISH_ROOT / r"controls\SOURCE_INPUT_SHA256_R81.json"
R82_DIFF = ENGLISH_ROOT / r"controls\SOURCE_DIFF_VALIDATION_R82.json"
R61_FRENCH_VALIDATION = FRENCH_ROOT / r"controls\EGA1_CHAPTER1_P138_VALIDATION_R61.json"
SCAFFOLD = LANE_CONTROL / "EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_20260802.md"
DUAL_DOI_CONTROL = LANE_CONTROL / "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
SUCCESSOR_PROTOCOL = LANE_CONTROL / "SUCCESSOR_SESSION_BOOTSTRAP_AND_LOGBOOK_PROTOCOL_20260803.md"

EXPECTED = {
    R82_MANIFEST: (51613, "CE696DDADDBAD9D41D2086BC0B849F9D57531BA086B77826DC1FA0F0BFA771F9"),
    R81_MANIFEST: (51101, "14D779D7976E566C3AB0BFF09862C0BD2DB68EE46758F46AC7309CF57D5F6FAF"),
    R82_DIFF: (15740, "9B73FA281982CBC243DDEA33272650265A40A64E1FF7FBB18D217D9C63F4E58A"),
    R61_FRENCH_VALIDATION: (13736, "61DEE7FD8760F32CF965CB8D10E85FC4572B766ADCDFC16978EA297FCFA22E73"),
    SCAFFOLD: (98950, "1B024552FFE71D56EB1BB2BA50304961073B55B0CEE76D5F514EDDFB65D49BB4"),
    DUAL_DOI_CONTROL: (2296, "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679"),
    SUCCESSOR_PROTOCOL: (4603, "2799FE59BDE0FA93334FE45EB2B0AC9C63F250B006C1DE0D5FF946160EE65ECC"),
    FRENCH_ROOT / "LOGBOOK.md": (386143, "E8ACB6CC01CA1C91097B07018C408DCA25CDAC2D3FCF3149A44301E5C123BD7D"),
    FRENCH_ROOT / "STATUS.md": (240235, "F36548BF3E5D3B4A3F95D269F3805C1F7D63698C1A13E29B516802189705DBAC"),
    FRENCH_ROOT / "CONTINUATION_HANDOFF.md": (123698, "F8012E9B7EAA6D14CB4D731F1FEEFC84D1E102B37435D1346F5D3F353C42DB12"),
    FRENCH_ROOT / "README.md": (858, "70D6B44C93313E4FF153544EAB7260991C5F57FE66C96E0B193E9A2392713D59"),
    ENGLISH_ROOT / "LOGBOOK.md": (166796, "044E4A709806604718ACBFA4568F235F333793EFCC204C61C63644836CA16DE6"),
    ENGLISH_ROOT / "STATUS.md": (99445, "05BB5529F6DB7689F999843C935A866BAC0D8EFC442EE0140FF2EF93C0AE8872"),
}

P138_LEDGER_EXPECTED = {
    "FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P138_20260804.jsonl": (
        5177,
        "81D5831F7E7C7A300DE9CC8CBB51BB367D677294907038B2D2D7DC370FC3FC20",
    ),
    "ENGLISH_CORRECTION_RECHECK_APPEND_P138_20260804.jsonl": (
        9564,
        "1917D2EF35BC1AADB57074D45481DF3899F120402E915595608A3573D4E3226A",
    ),
    "WORKFLOW_ERROR_APPEND_P138_20260804.jsonl": (
        18861,
        "A1FFA5B192BE640F4BE13E876823E1F255AF2CF1E0560DCB3B89DA76D8EEB7C4",
    ),
}

ENGLISH_BUILD_DIR = ENGLISH_ROOT / r"controls\ega1_p138_english_bounded_build_r1"
FRENCH_BUILD_DIR = (
    FRENCH_ROOT
    / r"qa\ega1_chapter1_build\chapter1-p79-138-build-r1-xelatex"
)
FRENCH_WRAPPER = FRENCH_ROOT / r"qa\ega1_chapter1_build\chapter1-p79-138-check-r1.tex"

DIRECT_NAMES = [
    "00_EGA_I_P138_Diplomatic_French_Paired_English_PreStacks_Source.zip",
    "01_READ_ME_FIRST.md",
    "02_EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P138.md",
    "03_EGA_FRENCH_PROJECT_LOGBOOK_P138_PUBLIC_PRIVACY_CLEAN.md",
    "04_EGA_ENGLISH_RECHECK_LOGBOOK_P138_PUBLIC_PRIVACY_CLEAN.md",
    "05_EGA_CONTINUATION_HANDOFF_P138_PUBLIC_PRIVACY_CLEAN.md",
    "06_EGA_FRENCH_STATUS_P138_PUBLIC_PRIVACY_CLEAN.md",
    "07_EGA_ENGLISH_STATUS_P138_PUBLIC_PRIVACY_CLEAN.md",
    "08a_EGA1_CHAPTER1_P138_VALIDATION_R61.json",
    "08b_EGA_ENGLISH_SOURCE_DIFF_VALIDATION_R82.json",
    "09a_FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P138_20260804.jsonl",
    "09b_ENGLISH_CORRECTION_RECHECK_APPEND_P138_20260804.jsonl",
    "09c_WORKFLOW_ERROR_APPEND_P138_20260804.jsonl",
    "10_RIGHTS_AND_PROVENANCE.md",
    "11_PRIVACY_TRANSFORMATIONS.csv",
    "12_PRIVACY_VALIDATION.json",
    "13_PACKAGE_PAYLOAD_MANIFEST.csv",
]


def copy_exact(target_root: Path, relative: str, source: Path, expected=None) -> bytes:
    if expected is not None:
        data = base.require_identity(source, expected)
    else:
        data = base.stable_copy_bytes(source)
    base.write_bytes(target_root, relative, data)
    return data


def validate_jsonl(path: Path, expected_rows: int) -> None:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(rows) != expected_rows:
        raise RuntimeError(f"JSONL row count mismatch for {path}: {len(rows)} != {expected_rows}")
    ids = [
        str(
            row.get("stable_id")
            or row.get("id")
            or row.get("decision_id")
            or row.get("event_id")
            or ""
        )
        for row in rows
    ]
    if any(not item for item in ids) or len(ids) != len(set(ids)):
        raise RuntimeError(f"missing or duplicate stable JSONL IDs: {path}")


def build_private(temp_root: Path) -> dict[str, object]:
    for path, expected in EXPECTED.items():
        base.require_identity(path, expected)

    manifest = json.loads(R82_MANIFEST.read_text(encoding="utf-8"))
    diff = json.loads(R82_DIFF.read_text(encoding="utf-8"))
    french_validation = json.loads(R61_FRENCH_VALIDATION.read_text(encoding="utf-8"))
    if (
        manifest.get("file_count") != 127
        or manifest.get("canonical_tree_sha256")
        != "863DC6BD6E3C752E94DDA9B58EEBD8AE9378CF64B525F663359EFDAE146E85CD"
    ):
        raise RuntimeError("R82 manifest identity or tree is not the sealed generation")
    if diff.get("errors") != [] or "READY_PRINTED_P139" not in str(diff.get("status")):
        raise RuntimeError("R82 English validation is not terminal PASS/ready p.139")
    if french_validation.get("errors") != [] or french_validation.get("printed_page") != 138:
        raise RuntimeError("R61 French validation is not sealed printed p.138")

    copied_english = 0
    for row in manifest["files"]:
        rel = str(row["relative_path"])
        source = ENGLISH_ROOT / "source" / Path(rel)
        copy_exact(temp_root, f"source/english/{rel}", source, (int(row["bytes"]), str(row["sha256"])))
        copied_english += 1

    french_expected = {
        str(row["relative_path"]).removeprefix("source/"): (int(row["bytes"]), str(row["sha256"]))
        for row in french_validation["french_sources"]
    }
    copied_french = 0
    for source in sorted((p for p in (FRENCH_ROOT / "source").rglob("*") if p.is_file())):
        rel = source.relative_to(FRENCH_ROOT / "source").as_posix()
        copy_exact(temp_root, f"source/french/{rel}", source, french_expected.get(rel))
        copied_french += 1
    if copied_french != 9:
        raise RuntimeError(f"unexpected French source closure count: {copied_french}")

    controls = {
        "controls/SOURCE_INPUT_SHA256_R81.json": R81_MANIFEST,
        "controls/SOURCE_INPUT_SHA256_R82.json": R82_MANIFEST,
        "controls/SOURCE_DIFF_VALIDATION_R82.json": R82_DIFF,
        "controls/EGA1_CHAPTER1_P138_VALIDATION_R61.json": R61_FRENCH_VALIDATION,
        "controls/EGA1_P138_ENGLISH_BOUNDED_CHECK_R1.tex": ENGLISH_ROOT / r"controls\EGA1_P138_ENGLISH_BOUNDED_CHECK_R1.tex",
        "controls/EGA1_P138_ENGLISH_SECTION5_CONTINUATION_R1.tex": ENGLISH_ROOT / r"controls\EGA1_P138_ENGLISH_SECTION5_CONTINUATION_R1.tex",
        "controls/chapter1-p79-138-check-r1.tex": FRENCH_WRAPPER,
        "controls/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md": DUAL_DOI_CONTROL,
        "controls/SUCCESSOR_SESSION_BOOTSTRAP_AND_LOGBOOK_PROTOCOL_20260803.md": SUCCESSOR_PROTOCOL,
    }
    for name, expected in P138_LEDGER_EXPECTED.items():
        controls[f"controls/{name}"] = FRENCH_ROOT / "controls" / name
    for rel, source in controls.items():
        expected = EXPECTED.get(source)
        if source.parent == FRENCH_ROOT / "controls" and source.name in P138_LEDGER_EXPECTED:
            expected = P138_LEDGER_EXPECTED[source.name]
        copy_exact(temp_root, rel, source, expected)

    validate_jsonl(temp_root / "controls/FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P138_20260804.jsonl", 9)
    validate_jsonl(temp_root / "controls/ENGLISH_CORRECTION_RECHECK_APPEND_P138_20260804.jsonl", 14)
    validate_jsonl(temp_root / "controls/WORKFLOW_ERROR_APPEND_P138_20260804.jsonl", 22)

    for source in sorted((p for p in ENGLISH_BUILD_DIR.iterdir() if p.is_file())):
        copy_exact(temp_root, f"qa/english/{source.name}", source)
    for source in sorted((p for p in FRENCH_BUILD_DIR.iterdir() if p.is_file())):
        copy_exact(temp_root, f"qa/french/{source.name}", source)

    copy_exact(temp_root, "semantic/EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P138.md", SCAFFOLD, EXPECTED[SCAFFOLD])
    copy_exact(temp_root, "provenance/FRENCH_PROJECT_LOGBOOK_RAW.md", FRENCH_ROOT / "LOGBOOK.md", EXPECTED[FRENCH_ROOT / "LOGBOOK.md"])
    copy_exact(temp_root, "provenance/FRENCH_STATUS_RAW.md", FRENCH_ROOT / "STATUS.md", EXPECTED[FRENCH_ROOT / "STATUS.md"])
    copy_exact(temp_root, "provenance/CONTINUATION_HANDOFF_RAW.md", FRENCH_ROOT / "CONTINUATION_HANDOFF.md", EXPECTED[FRENCH_ROOT / "CONTINUATION_HANDOFF.md"])
    copy_exact(temp_root, "provenance/FRENCH_README_RAW.md", FRENCH_ROOT / "README.md", EXPECTED[FRENCH_ROOT / "README.md"])
    copy_exact(temp_root, "provenance/ENGLISH_RECHECK_LOGBOOK_RAW.md", ENGLISH_ROOT / "LOGBOOK.md", EXPECTED[ENGLISH_ROOT / "LOGBOOK.md"])
    copy_exact(temp_root, "provenance/ENGLISH_RECHECK_STATUS_RAW.md", ENGLISH_ROOT / "STATUS.md", EXPECTED[ENGLISH_ROOT / "STATUS.md"])

    base.write_text(
        temp_root,
        "PRIVATE_CUSTODY_README.md",
        "# Private exact custody: EGA I printed p.138\n\n"
        "This immutable snapshot freezes the exact terminal French R61 / English R82 generation. It contains all 127 English source inputs, the complete nine-file French source closure, both human logbooks and status surfaces, continuation, the p.138 decision/reversal/error ledgers, pre-Stacks scaffold, and bounded build/QA artifacts. The NUMDAM authority PDF and authority-page image are not copied. The producer roots are not modified. A separate privacy-clean projection is required for public transport.\n",
    )

    rows = base.rows_for_tree(temp_root, {"PRIVATE_CUSTODY_MANIFEST.csv", "PRIVATE_CUSTODY_VALIDATION.json"})
    base.write_manifest(temp_root / "PRIVATE_CUSTODY_MANIFEST.csv", rows)
    validation = {
        "status": "PASS_PRIVATE_EXACT_CUSTODY_EGA_I_P138_R61_R82",
        "errors": [],
        "printed_page": 138,
        "next_cursor": "printed p.139, continuation of Proposition 5.5.10",
        "english_source_files": copied_english,
        "english_source_bytes": int(manifest["total_bytes"]),
        "english_source_tree_sha256": manifest["canonical_tree_sha256"],
        "french_source_files": copied_french,
        "represented_files": len(rows),
        "represented_bytes": sum(int(row["bytes"]) for row in rows),
        "canonical_tree_sha256": base.canonical_tree_sha(rows),
        "r82_manifest": {"bytes": EXPECTED[R82_MANIFEST][0], "sha256": EXPECTED[R82_MANIFEST][1]},
        "r82_validation": {"bytes": EXPECTED[R82_DIFF][0], "sha256": EXPECTED[R82_DIFF][1]},
        "r61_validation": {"bytes": EXPECTED[R61_FRENCH_VALIDATION][0], "sha256": EXPECTED[R61_FRENCH_VALIDATION][1]},
        "authority_pdfs_included": 0,
        "authority_page_images_included": 0,
        "producer_roots_mutated": False,
    }
    base.write_bytes(temp_root, "PRIVATE_CUSTODY_VALIDATION.json", base.json_bytes(validation))
    return validation


def scan_public(root: Path) -> dict[str, object]:
    residuals: list[dict[str, object]] = []
    emails: list[dict[str, object]] = []
    mandated_task_ids = 0
    public_toolchain_email_occurrences = 0
    binary_private_hits: list[dict[str, object]] = []
    binary_needles = (b"C:\\Users\\", b"C:/Users/", b"Floris", b".codex", b"memo_lepthy@live.nl")
    for path in sorted((p for p in root.rglob("*") if p.is_file())):
        rel = path.relative_to(root).as_posix()
        data = path.read_bytes()
        if path.suffix.lower() in base.TEXT_SUFFIXES:
            text = data.decode("utf-8")
            for name, pattern in (
                ("user_home", base.RESIDUAL_USER_HOME),
                ("private_codex_state", base.CODEX_PATH_SEGMENT),
                ("private_email", base.PRIVATE_EMAIL),
                ("hardcoded_secret", base.HARDCODED_SECRET),
            ):
                count = len(pattern.findall(text))
                if count:
                    residuals.append({"relative_path": rel, "pattern": name, "count": count})
            task_count = len(base.TASK_ID.findall(text))
            if task_count:
                if rel.endswith("PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"):
                    mandated_task_ids += task_count
                else:
                    residuals.append({"relative_path": rel, "pattern": "internal_task_id", "count": task_count})
            for email in base.ANY_EMAIL.findall(text):
                if email.lower() == "krisrose@tug.org":
                    public_toolchain_email_occurrences += 1
                else:
                    emails.append({"relative_path": rel, "email_sha256": base.sha256(email.encode("utf-8"))})
        elif path.suffix.lower() != ".zip":
            for needle in binary_needles:
                if needle.lower() in data.lower():
                    binary_private_hits.append(
                        {"relative_path": rel, "needle_sha256": base.sha256(needle), "count": data.lower().count(needle.lower())}
                    )
    if residuals or emails or binary_private_hits or mandated_task_ids != 3:
        raise RuntimeError(
            f"public privacy gate failed: residuals={residuals}, emails={emails}, "
            f"binary={binary_private_hits}, mandated={mandated_task_ids}"
        )
    return {
        "residual_private_patterns": 0,
        "remaining_email_addresses": 0,
        "binary_private_hits": 0,
        "mandated_task_id_exceptions": mandated_task_ids,
        "public_toolchain_email_sha256": base.sha256(b"krisrose@tug.org"),
        "public_toolchain_email_occurrences": public_toolchain_email_occurrences,
    }


def build_public(temp_root: Path, private_root: Path, private_validation: dict[str, object]) -> dict[str, object]:
    path_map = {
        "semantic/EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P138.md": "02_EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P138.md",
        "provenance/FRENCH_PROJECT_LOGBOOK_RAW.md": "03_EGA_FRENCH_PROJECT_LOGBOOK_P138_PUBLIC_PRIVACY_CLEAN.md",
        "provenance/ENGLISH_RECHECK_LOGBOOK_RAW.md": "04_EGA_ENGLISH_RECHECK_LOGBOOK_P138_PUBLIC_PRIVACY_CLEAN.md",
        "provenance/CONTINUATION_HANDOFF_RAW.md": "05_EGA_CONTINUATION_HANDOFF_P138_PUBLIC_PRIVACY_CLEAN.md",
        "provenance/FRENCH_STATUS_RAW.md": "06_EGA_FRENCH_STATUS_P138_PUBLIC_PRIVACY_CLEAN.md",
        "provenance/ENGLISH_RECHECK_STATUS_RAW.md": "07_EGA_ENGLISH_STATUS_P138_PUBLIC_PRIVACY_CLEAN.md",
        "controls/EGA1_CHAPTER1_P138_VALIDATION_R61.json": "08a_EGA1_CHAPTER1_P138_VALIDATION_R61.json",
        "controls/SOURCE_DIFF_VALIDATION_R82.json": "08b_EGA_ENGLISH_SOURCE_DIFF_VALIDATION_R82.json",
        "controls/FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P138_20260804.jsonl": "09a_FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P138_20260804.jsonl",
        "controls/ENGLISH_CORRECTION_RECHECK_APPEND_P138_20260804.jsonl": "09b_ENGLISH_CORRECTION_RECHECK_APPEND_P138_20260804.jsonl",
        "controls/WORKFLOW_ERROR_APPEND_P138_20260804.jsonl": "09c_WORKFLOW_ERROR_APPEND_P138_20260804.jsonl",
    }
    excluded = {"PRIVATE_CUSTODY_MANIFEST.csv", "PRIVATE_CUSTODY_VALIDATION.json", "PRIVATE_CUSTODY_README.md"}
    events: list[dict[str, object]] = []
    bindings: list[dict[str, object]] = []
    for source in sorted((p for p in private_root.rglob("*") if p.is_file())):
        private_rel = source.relative_to(private_root).as_posix()
        if private_rel in excluded:
            continue
        public_rel = path_map.get(private_rel, private_rel)
        raw = source.read_bytes()
        public = base.privacy_transform(public_rel, raw, events)
        base.write_bytes(temp_root, public_rel, public)
        bindings.append(
            {
                "private_relative_path": private_rel,
                "public_relative_path": public_rel,
                "private_bytes": len(raw),
                "private_sha256": base.sha256(raw),
                "public_bytes": len(public),
                "public_sha256": base.sha256(public),
                "transformed": raw != public,
            }
        )

    base.write_text(
        temp_root,
        "01_READ_ME_FIRST.md",
        "# EGA I diplomatic French / paired-English / pre-Stacks checkpoint through printed p.138\n\n"
        "This is a coherent source-and-provenance successor, not completion of EGA I or of the eight-publication EGA corpus. It advances the public source-critical checkpoint from printed p.127 to p.138 while the complete EGA 0–IV English reader remains the front-facing default reader.\n\n"
        "The package contains the exact terminal R61 diplomatic French generation, the matching 127-file R82 English source tree, four p.138 English fidelity repairs, all p.138 decision/reversal/error ledgers, both human logbooks and status surfaces, the continuation record, bounded build/QA evidence, and the current pre-Stacks scaffold. Printed French is retained diplomatically; English corrections remain a separate reasoned layer. The next source cursor is printed p.139.\n\n"
        "The NUMDAM authority PDF and authority-page image are identified by hash but are not redistributed. Existing readers and predecessor versions remain intact.\n",
    )
    base.write_text(
        temp_root,
        "10_RIGHTS_AND_PROVENANCE.md",
        "# Rights and provenance\n\n"
        "The authority is the NUMDAM EGA corpus identified in the validators. No authority PDF, publisher scan, source-page raster, or third-party comparison file is included. Underlying-work and scan rights remain with their rightsholders; no package-wide license is invented.\n\n"
        "French TeX is a diplomatic project transcription. English TeX is a separately ledgered source-rechecked project layer. Generated bounded readers and their QA artifacts are included as reproducibility evidence, not as critical-edition or mathematician-review certification. Raw private logs remain in separate custody; the public surfaces are minimally transformed with every replacement event recorded by token length and SHA-256.\n",
    )

    event_fields = ("relative_path", "transform_class", "original_token_bytes", "original_token_sha256", "replacement")
    with (temp_root / "11_PRIVACY_TRANSFORMATIONS.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=event_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(events)

    privacy = {
        "status": "PASS",
        "errors": [],
        "files_bound": len(bindings),
        "transformed_files": sum(1 for row in bindings if row["transformed"]),
        "transformation_events": len(events),
        "raw_private_source_mutated": False,
        "file_bindings": bindings,
    }
    base.write_bytes(temp_root, "12_PRIVACY_VALIDATION.json", base.json_bytes(privacy))
    privacy.update(scan_public(temp_root))
    base.write_bytes(temp_root, "12_PRIVACY_VALIDATION.json", base.json_bytes(privacy))

    payload_excluded = {
        "00_EGA_I_P138_Diplomatic_French_Paired_English_PreStacks_Source.zip",
        "13_PACKAGE_PAYLOAD_MANIFEST.csv",
        "14_ZENODO_UPLOAD_MANIFEST.csv",
        "15_PACKAGE_VALIDATION.json",
    }
    payload_rows = base.rows_for_tree(temp_root, payload_excluded)
    base.write_manifest(temp_root / "13_PACKAGE_PAYLOAD_MANIFEST.csv", payload_rows)
    zip_members = [str(row["relative_path"]) for row in payload_rows] + ["13_PACKAGE_PAYLOAD_MANIFEST.csv"]
    zip_identity = base.make_zip(
        temp_root / "00_EGA_I_P138_Diplomatic_French_Paired_English_PreStacks_Source.zip",
        temp_root,
        zip_members,
    )

    upload_rows: list[dict[str, object]] = []
    for rel in DIRECT_NAMES:
        data = (temp_root / rel).read_bytes()
        upload_rows.append(
            {
                "relative_path": rel,
                "bytes": len(data),
                "sha256": base.sha256(data),
                "ega_concept": "10.5281/zenodo.20414353",
                "methodology_concept": "10.5281/zenodo.21124403",
                "replication_concept": "10.5281/zenodo.20461174",
                "direct_public": "true",
            }
        )
    base.write_manifest(
        temp_root / "14_ZENODO_UPLOAD_MANIFEST.csv",
        upload_rows,
        ("ega_concept", "methodology_concept", "replication_concept", "direct_public"),
    )

    final_rows = base.rows_for_tree(temp_root, {"15_PACKAGE_VALIDATION.json"})
    validation = {
        "status": "PASS_READY_FOR_EXACT_ARCHIVE_CUSTODY_AND_THREE_CONCEPT_PUBLICATION",
        "errors": [],
        "scope": "EGA I diplomatic French and paired English through printed p.138; complete EGA remains in progress",
        "printed_page": 138,
        "next_cursor": "printed p.139, continuation of Proposition 5.5.10",
        "private_custody": private_validation,
        "public_projection": {
            "files_before_validation": len(final_rows),
            "bytes_before_validation": sum(int(row["bytes"]) for row in final_rows),
            "canonical_tree_sha256": base.canonical_tree_sha(final_rows),
            "payload_manifest_rows": len(payload_rows),
            "zip": zip_identity,
            "direct_upload_objects": len(upload_rows),
        },
        "privacy": privacy,
        "rights": {
            "authority_pdfs_included": 0,
            "authority_page_images_included": 0,
            "third_party_comparison_files_included": 0,
            "package_wide_license_invented": False,
        },
        "routing": {
            "ega_existing_concept": "10.5281/zenodo.20414353",
            "methodology_existing_concept": "10.5281/zenodo.21124403",
            "replication_existing_concept": "10.5281/zenodo.20461174",
            "new_concept_authorized": False,
            "fac_payload_included": False,
            "gaga_payload_included": False,
        },
    }
    base.write_bytes(temp_root, "15_PACKAGE_VALIDATION.json", base.json_bytes(validation))
    final_privacy = scan_public(temp_root)
    if (
        final_privacy["residual_private_patterns"] != 0
        or final_privacy["remaining_email_addresses"] != 0
        or final_privacy["binary_private_hits"] != 0
        or final_privacy["mandated_task_id_exceptions"] != 3
        or final_privacy["public_toolchain_email_occurrences"] != 2
    ):
        raise RuntimeError(f"final privacy replay failed: {final_privacy}")
    return validation


def main() -> None:
    if PRIVATE_FINAL.exists():
        private = json.loads((PRIVATE_FINAL / "PRIVATE_CUSTODY_VALIDATION.json").read_text(encoding="utf-8"))
        if private.get("status") != "PASS_PRIVATE_EXACT_CUSTODY_EGA_I_P138_R61_R82" or private.get("errors") != []:
            raise RuntimeError("existing immutable private custody root is not the expected PASS generation")
        rows = list(csv.DictReader((PRIVATE_FINAL / "PRIVATE_CUSTODY_MANIFEST.csv").open(encoding="utf-8", newline="")))
        for row in rows:
            path = PRIVATE_FINAL / str(row["relative_path"])
            if base.identity(path) != (int(row["bytes"]), str(row["sha256"])):
                raise RuntimeError(f"existing private custody replay mismatch: {row['relative_path']}")
        if base.canonical_tree_sha(rows) != private.get("canonical_tree_sha256"):
            raise RuntimeError("existing private custody canonical tree replay mismatch")
    else:
        private = base.atomic_build(PRIVATE_FINAL, build_private)
    public = base.atomic_build(PUBLIC_FINAL, build_public, PRIVATE_FINAL, private)
    summary = {
        "status": "PASS",
        "private_root": str(PRIVATE_FINAL),
        "private_files": len([p for p in PRIVATE_FINAL.rglob("*") if p.is_file()]),
        "private_bytes": sum(p.stat().st_size for p in PRIVATE_FINAL.rglob("*") if p.is_file()),
        "private_tree_sha256": private["canonical_tree_sha256"],
        "public_root": str(PUBLIC_FINAL),
        "public_files": len([p for p in PUBLIC_FINAL.rglob("*") if p.is_file()]),
        "public_bytes": sum(p.stat().st_size for p in PUBLIC_FINAL.rglob("*") if p.is_file()),
        "public_tree_sha256": public["public_projection"]["canonical_tree_sha256"],
        "zip": public["public_projection"]["zip"],
        "direct_upload_objects": public["public_projection"]["direct_upload_objects"],
        "privacy_events": public["privacy"]["transformation_events"],
        "privacy_errors": public["privacy"]["errors"],
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
