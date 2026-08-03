#!/usr/bin/env python3
"""Freeze the coherent EGA I printed-p.127 generation without touching live work.

The live producer has already advanced into printed p.128.  This builder uses
the producer's exact inverse bindings and R50/R59 validators to reconstruct the
immediately preceding p.127 source generation, preserves a raw private custody
tree, and creates a separate minimally transformed public projection.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import shutil
import tempfile
import zipfile
from pathlib import Path


WORKTREE = Path(
    r"C:\Users\Floris\Documents\Codex\2026-05-26\there-is-currently-an-ongoing-process\wt-sga-global-reader-provisional-20260803"
)
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
PRIVATE_PARENT = LANE_ROOT / r"90_logs\private_archive_custody"
PRIVATE_FINAL = PRIVATE_PARENT / "EGA_I_P127_R50_PRIVATE_RAW_CUSTODY_20260803_r1"
PUBLIC_FINAL = (
    WORKTREE
    / r"sources\ega\checkpoints\ega1-p127-diplomatic-prestacks-r1-20260803"
)

P127_VALIDATION = FRENCH_ROOT / r"controls\EGA1_CHAPTER1_P127_VALIDATION_R50.json"
R59_MANIFEST = ENGLISH_ROOT / r"controls\SOURCE_INPUT_SHA256_R59.json"
R59_DIFF = ENGLISH_ROOT / r"controls\SOURCE_DIFF_VALIDATION_R59.json"
SCAFFOLD = LANE_CONTROL / "EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_20260802.md"
DUAL_DOI_CONTROL = LANE_CONTROL / "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
SUCCESSOR_PROTOCOL = LANE_CONTROL / "SUCCESSOR_SESSION_BOOTSTRAP_AND_LOGBOOK_PROTOCOL_20260803.md"

EXPECTED_VALIDATION = (11010, "D631DC20C4EF98C822AA61FF29A02176382A23E40077C1D36338FE359E80EA25")
EXPECTED_R59 = (42723, "3D874D60FA7AB1CE4C0A0496BD20C3B096481E0A35463D851ACD295CCBD08569")
EXPECTED_R59_DIFF = (7763, "C68E010B34CF050695FCDC5AC8A1AC5F405A4AC05661A0558979214547426C73")
EXPECTED_P127_SCAFFOLD = (51566, "5DD244CCB3A223D0EEDB67E233027A1A338ACD24232C7639023723F8B98BACBC")
EXPECTED_DUAL_DOI = (2296, "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679")
EXPECTED_SUCCESSOR_PROTOCOL = (4603, "2799FE59BDE0FA93334FE45EB2B0AC9C63F250B006C1DE0D5FF946160EE65ECC")

TEXT_SUFFIXES = {
    ".bib",
    ".cfg",
    ".cls",
    ".csv",
    ".json",
    ".jsonl",
    ".md",
    ".ps1",
    ".py",
    ".sty",
    ".tex",
    ".txt",
    ".yaml",
    ".yml",
}

ROOT_TRANSFORMS = (
    (
        "project_root",
        re.compile(r"(?i)C:[\\/]Users[\\/]Floris[\\/]Documents[\\/]interlanguage"),
        "[PROJECT_ROOT]",
    ),
    (
        "archive_worktree_root",
        re.compile(r"(?i)C:[\\/]Users[\\/]Floris[\\/]Documents[\\/]Codex"),
        "[ARCHIVE_WORKTREE_ROOT]",
    ),
    (
        "private_documents_root",
        re.compile(r"(?i)C:[\\/]Users[\\/]Floris[\\/]Documents"),
        "[PRIVATE_DOCUMENTS_ROOT]",
    ),
    (
        "private_download_root",
        re.compile(r"(?i)C:[\\/]Users[\\/]Floris[\\/]Downloads"),
        "[PRIVATE_DOWNLOAD_ROOT]",
    ),
    (
        "private_operator_home",
        re.compile(r"(?i)C:[\\/]Users[\\/]Floris"),
        "[PRIVATE_OPERATOR_HOME]",
    ),
    (
        "other_windows_user_home",
        re.compile(r"(?i)(?<![A-Za-z0-9])(?:[A-Za-z]:)[\\/]Users[\\/][^\\/\s\"']+"),
        "[PRIVATE_USER_HOME]",
    ),
    (
        "other_posix_user_home",
        re.compile(r"(?i)(?<![A-Za-z0-9])/(?:Users|home)/[^/\s\"']+"),
        "[PRIVATE_USER_HOME]",
    ),
)
TASK_ID = re.compile(r"(?i)019[0-9a-f]{5}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
PRIVATE_EMAIL = re.compile(r"(?i)\bmemo_lepthy@live\.nl\b")
CODEX_PATH_SEGMENT = re.compile(r"(?i)(?P<sep>[\\/])\.codex(?=(?:[\\/]|$))")
RESIDUAL_USER_HOME = re.compile(
    r"(?i)(?:[A-Za-z]:[\\/]Users[\\/][^\\/\s\"']+|/(?:Users|home)/[^/\s\"']+)"
)
ANY_EMAIL = re.compile(r"(?i)(?<!@)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
HARDCODED_SECRET = re.compile(
    r"(?i)(?:access[_-]?token|api[_-]?key|github[_-]?token)\s*[:=]\s*[\"'][A-Za-z0-9_\-]{16,}"
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    return len(data), sha256(data)


def require_identity(path: Path, expected: tuple[int, str]) -> bytes:
    data = path.read_bytes()
    actual = (len(data), sha256(data))
    if actual != expected:
        raise RuntimeError(f"identity mismatch for {path}: {actual} != {expected}")
    return data


def write_bytes(root: Path, relative: str, data: bytes) -> Path:
    target = root / Path(relative)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    return target


def write_text(root: Path, relative: str, text: str) -> Path:
    return write_bytes(root, relative, text.encode("utf-8"))


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def rows_for_tree(root: Path, excluded: set[str] | None = None) -> list[dict[str, object]]:
    excluded = excluded or set()
    rows: list[dict[str, object]] = []
    for path in sorted((p for p in root.rglob("*") if p.is_file()), key=lambda p: p.relative_to(root).as_posix()):
        rel = path.relative_to(root).as_posix()
        if rel in excluded:
            continue
        data = path.read_bytes()
        rows.append({"relative_path": rel, "bytes": len(data), "sha256": sha256(data)})
    return rows


def canonical_tree_sha(rows: list[dict[str, object]]) -> str:
    payload = "".join(
        f"{row['relative_path']}\t{row['bytes']}\t{row['sha256']}\n"
        for row in sorted(rows, key=lambda r: str(r["relative_path"]))
    ).encode("utf-8")
    return sha256(payload)


def write_manifest(path: Path, rows: list[dict[str, object]], extra_fields: tuple[str, ...] = ()) -> None:
    fields = ("relative_path", "bytes", "sha256") + extra_fields
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fields})


def stable_copy_bytes(path: Path) -> bytes:
    before = identity(path)
    data = path.read_bytes()
    after = identity(path)
    if before != after or before != (len(data), sha256(data)):
        raise RuntimeError(f"file changed during bounded snapshot: {path}")
    return data


def reconstruct_p127_scaffold() -> bytes:
    current = stable_copy_bytes(SCAFFOLD)
    marker = b"\n## Incremental EGA I p.128 scaffold\n"
    if current.count(marker) != 1:
        raise RuntimeError("p.128 scaffold boundary is not unique")
    result = current.split(marker, 1)[0]
    if (len(result), sha256(result)) != EXPECTED_P127_SCAFFOLD:
        raise RuntimeError("reconstructed p.127 scaffold does not match R50")
    return result


def reconstruct_p127_english(current: bytes) -> bytes:
    text = current.decode("utf-8")
    operations = (
        (r"\mathfrak{I}\subset\mathfrak{j}_x", r"\mathfrak{I}_x\subset\mathfrak{j}_x"),
        (r"reduced thus means that $X=X_\red$", r"reduced thus implies that $X=X_\red$"),
    )
    for current_text, restore_text in operations:
        count = text.count(current_text)
        if count != 1:
            raise RuntimeError(f"English inverse token count {count}: {current_text}")
        text = text.replace(current_text, restore_text, 1)
    return text.encode("utf-8")


def build_private(temp_root: Path) -> dict[str, object]:
    validation_bytes = require_identity(P127_VALIDATION, EXPECTED_VALIDATION)
    validation = json.loads(validation_bytes.decode("utf-8"))
    if validation.get("errors") != [] or validation.get("printed_page") != 127:
        raise RuntimeError("R50 is not the expected p.127 PASS validator")

    manifest_bytes = require_identity(R59_MANIFEST, EXPECTED_R59)
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    if manifest.get("file_count") != 127:
        raise RuntimeError("R59 file count is not 127")
    require_identity(R59_DIFF, EXPECTED_R59_DIFF)
    require_identity(DUAL_DOI_CONTROL, EXPECTED_DUAL_DOI)
    require_identity(SUCCESSOR_PROTOCOL, EXPECTED_SUCCESSOR_PROTOCOL)

    reconstruction_events: list[dict[str, object]] = []
    copied_english = 0
    for row in manifest["files"]:
        rel = str(row["relative_path"])
        source_path = ENGLISH_ROOT / "source" / Path(rel)
        current = stable_copy_bytes(source_path)
        desired = current
        if (len(current), sha256(current)) != (int(row["bytes"]), str(row["sha256"])):
            if rel != "ega1/ega1-5.tex":
                raise RuntimeError(f"unexpected post-R59 English delta: {rel}")
            desired = reconstruct_p127_english(current)
            reconstruction_events.append(
                {
                    "relative_path": f"source/english/{rel}",
                    "operation": "two exact inverse substitutions bound by P128 inverse ledger",
                    "live_bytes": len(current),
                    "live_sha256": sha256(current),
                    "restored_bytes": len(desired),
                    "restored_sha256": sha256(desired),
                }
            )
        if (len(desired), sha256(desired)) != (int(row["bytes"]), str(row["sha256"])):
            raise RuntimeError(f"R59 reconstruction failed: {rel}")
        write_bytes(temp_root, f"source/english/{rel}", desired)
        copied_english += 1

    french_expected = {
        str(row["relative_path"]).removeprefix("source/"): (int(row["bytes"]), str(row["sha256"]))
        for row in validation["french_sources"]
    }
    copied_french = 0
    for source_path in sorted((p for p in (FRENCH_ROOT / "source").rglob("*") if p.is_file())):
        rel = source_path.relative_to(FRENCH_ROOT / "source").as_posix()
        current = stable_copy_bytes(source_path)
        desired = current
        if rel == "ega1/ega1-5-fr.tex":
            desired = current[:681]
            reconstruction_events.append(
                {
                    "relative_path": f"source/french/{rel}",
                    "operation": "truncate to first 681 UTF-8 bytes bound by P128 inverse ledger",
                    "live_bytes": len(current),
                    "live_sha256": sha256(current),
                    "restored_bytes": len(desired),
                    "restored_sha256": sha256(desired),
                }
            )
        if rel in french_expected and (len(desired), sha256(desired)) != french_expected[rel]:
            raise RuntimeError(f"p.127 French identity mismatch: {rel}")
        write_bytes(temp_root, f"source/french/{rel}", desired)
        copied_french += 1

    controls = {
        "controls/EGA1_CHAPTER1_P127_VALIDATION_R50.json": P127_VALIDATION,
        "controls/FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P127_20260803.jsonl": FRENCH_ROOT / r"controls\FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P127_20260803.jsonl",
        "controls/ENGLISH_CORRECTION_RECHECK_APPEND_P127_20260803.jsonl": FRENCH_ROOT / r"controls\ENGLISH_CORRECTION_RECHECK_APPEND_P127_20260803.jsonl",
        "controls/WORKFLOW_ERROR_APPEND_P127_20260803.jsonl": FRENCH_ROOT / r"controls\WORKFLOW_ERROR_APPEND_P127_20260803.jsonl",
        "controls/SOURCE_INPUT_SHA256_R59.json": R59_MANIFEST,
        "controls/SOURCE_DIFF_VALIDATION_R59.json": R59_DIFF,
        "controls/EGA1_P127_ENGLISH_BOUNDED_CHECK_R1.tex": ENGLISH_ROOT / r"controls\EGA1_P127_ENGLISH_BOUNDED_CHECK_R1.tex",
        "controls/EGA1_P127_ENGLISH_SECTION4_CONTINUATION_R1.tex": ENGLISH_ROOT / r"controls\EGA1_P127_ENGLISH_SECTION4_CONTINUATION_R1.tex",
        "controls/EGA1_P127_ENGLISH_SECTION5_PREFIX_R1.tex": ENGLISH_ROOT / r"controls\EGA1_P127_ENGLISH_SECTION5_PREFIX_R1.tex",
        "controls/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md": DUAL_DOI_CONTROL,
        "controls/SUCCESSOR_SESSION_BOOTSTRAP_AND_LOGBOOK_PROTOCOL_20260803.md": SUCCESSOR_PROTOCOL,
    }
    for rel, source_path in controls.items():
        write_bytes(temp_root, rel, stable_copy_bytes(source_path))

    write_bytes(temp_root, "semantic/EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P127.md", reconstruct_p127_scaffold())
    write_bytes(temp_root, "provenance/PROJECT_LOGBOOK_RAW.md", stable_copy_bytes(FRENCH_ROOT / "LOGBOOK.md"))
    write_bytes(temp_root, "provenance/STATUS_RAW.md", stable_copy_bytes(FRENCH_ROOT / "STATUS.md"))
    write_bytes(temp_root, "provenance/CONTINUATION_HANDOFF_RAW.md", stable_copy_bytes(FRENCH_ROOT / "CONTINUATION_HANDOFF.md"))

    write_text(
        temp_root,
        "PRIVATE_CUSTODY_README.md",
        (
            "# Private exact custody: EGA I printed p.127\n\n"
            "This immutable custody snapshot reconstructs the exact coherent R50/R59 generation immediately before live printed-p.128 work. The live producer tree was not changed. English `ega1/ega1-5.tex`, French `ega1/ega1-5-fr.tex`, and the pre-Stacks scaffold were restored only in this snapshot using producer-recorded exact inverse operations, and each restored byte stream matches the R50/R59 identity. Raw logbook, status, and continuation surfaces remain private here; public transport must use the separately ledgered privacy-clean projection. Authority scans and page rasters are excluded.\n"
        ),
    )
    write_bytes(temp_root, "controls/P127_SOURCE_RECONSTRUCTION.json", json_bytes({"events": reconstruction_events}))

    manifest_rows = rows_for_tree(temp_root, {"PRIVATE_CUSTODY_MANIFEST.csv", "PRIVATE_CUSTODY_VALIDATION.json"})
    write_manifest(temp_root / "PRIVATE_CUSTODY_MANIFEST.csv", manifest_rows)
    private_validation = {
        "status": "PASS_PRIVATE_EXACT_CUSTODY_P127",
        "errors": [],
        "printed_page": 127,
        "english_source_files": copied_english,
        "french_source_files": copied_french,
        "reconstruction_events": reconstruction_events,
        "represented_files": len(manifest_rows),
        "represented_bytes": sum(int(row["bytes"]) for row in manifest_rows),
        "canonical_tree_sha256": canonical_tree_sha(manifest_rows),
        "producer_validation": {"bytes": EXPECTED_VALIDATION[0], "sha256": EXPECTED_VALIDATION[1]},
        "english_r59_manifest": {"bytes": EXPECTED_R59[0], "sha256": EXPECTED_R59[1]},
        "p127_scaffold": {"bytes": EXPECTED_P127_SCAFFOLD[0], "sha256": EXPECTED_P127_SCAFFOLD[1]},
        "authority_scans_included": 0,
        "producer_tree_mutated": False,
    }
    write_bytes(temp_root, "PRIVATE_CUSTODY_VALIDATION.json", json_bytes(private_validation))
    return private_validation


def record_event(
    events: list[dict[str, object]],
    relative_path: str,
    transform_class: str,
    matched: str,
    replacement: str,
) -> None:
    raw = matched.encode("utf-8")
    events.append(
        {
            "relative_path": relative_path,
            "transform_class": transform_class,
            "original_token_bytes": len(raw),
            "original_token_sha256": sha256(raw),
            "replacement": replacement,
        }
    )


def privacy_transform(relative_path: str, data: bytes, events: list[dict[str, object]]) -> bytes:
    if Path(relative_path).suffix.lower() not in TEXT_SUFFIXES:
        return data
    text = data.decode("utf-8")
    for transform_class, pattern, replacement in ROOT_TRANSFORMS:
        def root_callback(match: re.Match[str], tc: str = transform_class, rep: str = replacement) -> str:
            record_event(events, relative_path, tc, match.group(0), rep)
            return rep
        text = pattern.sub(root_callback, text)

    def codex_callback(match: re.Match[str]) -> str:
        replacement = f"{match.group('sep')}[PRIVATE_CODEX_STATE]"
        record_event(events, relative_path, "private_codex_state_segment", match.group(0), replacement)
        return replacement

    text = CODEX_PATH_SEGMENT.sub(codex_callback, text)

    # The exact 2,296-byte dual-DOI control is a mandated identity exception.
    if not relative_path.endswith("PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"):
        def task_callback(match: re.Match[str]) -> str:
            digest = sha256(match.group(0).encode("ascii"))[:12]
            replacement = f"[PRIVATE_TASK_{digest}]"
            record_event(events, relative_path, "internal_task_id", match.group(0), replacement)
            return replacement
        text = TASK_ID.sub(task_callback, text)

    def email_callback(match: re.Match[str]) -> str:
        replacement = "[PRIVATE_EMAIL]"
        record_event(events, relative_path, "private_email", match.group(0), replacement)
        return replacement

    return PRIVATE_EMAIL.sub(email_callback, text).encode("utf-8")


def make_zip(zip_path: Path, root: Path, members: list[str]) -> dict[str, object]:
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for rel in sorted(members):
            data = (root / rel).read_bytes()
            info = zipfile.ZipInfo(rel, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    with zipfile.ZipFile(zip_path, "r") as archive:
        bad = archive.testzip()
        names = archive.namelist()
        if bad is not None or names != sorted(members):
            raise RuntimeError(f"ZIP replay failed: bad={bad}, names_match={names == sorted(members)}")
        for rel in names:
            if archive.read(rel) != (root / rel).read_bytes():
                raise RuntimeError(f"ZIP member mismatch: {rel}")
    data = zip_path.read_bytes()
    return {"members": len(members), "bytes": len(data), "sha256": sha256(data)}


def build_public(temp_root: Path, private_root: Path, private_validation: dict[str, object]) -> dict[str, object]:
    path_map = {
        "provenance/PROJECT_LOGBOOK_RAW.md": "03_EGA_PROJECT_LOGBOOK_P127_PUBLIC_PRIVACY_CLEAN.md",
        "provenance/CONTINUATION_HANDOFF_RAW.md": "04_EGA_CONTINUATION_HANDOFF_P127_PUBLIC_PRIVACY_CLEAN.md",
        "provenance/STATUS_RAW.md": "05_EGA_STATUS_P127_PUBLIC_PRIVACY_CLEAN.md",
        "semantic/EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P127.md": "02_EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P127.md",
        "controls/EGA1_CHAPTER1_P127_VALIDATION_R50.json": "06_EGA1_CHAPTER1_P127_VALIDATION_R50.json",
        "controls/FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P127_20260803.jsonl": "06a_FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P127_20260803.jsonl",
        "controls/ENGLISH_CORRECTION_RECHECK_APPEND_P127_20260803.jsonl": "06b_ENGLISH_CORRECTION_RECHECK_APPEND_P127_20260803.jsonl",
        "controls/WORKFLOW_ERROR_APPEND_P127_20260803.jsonl": "06c_WORKFLOW_ERROR_APPEND_P127_20260803.jsonl",
    }
    excluded_private = {"PRIVATE_CUSTODY_MANIFEST.csv", "PRIVATE_CUSTODY_VALIDATION.json", "PRIVATE_CUSTODY_README.md"}
    events: list[dict[str, object]] = []
    file_bindings: list[dict[str, object]] = []
    for source_path in sorted((p for p in private_root.rglob("*") if p.is_file())):
        private_rel = source_path.relative_to(private_root).as_posix()
        if private_rel in excluded_private:
            continue
        public_rel = path_map.get(private_rel, private_rel)
        raw = source_path.read_bytes()
        public = privacy_transform(public_rel, raw, events)
        write_bytes(temp_root, public_rel, public)
        file_bindings.append(
            {
                "private_relative_path": private_rel,
                "public_relative_path": public_rel,
                "private_bytes": len(raw),
                "private_sha256": sha256(raw),
                "public_bytes": len(public),
                "public_sha256": sha256(public),
                "transformed": raw != public,
            }
        )

    write_text(
        temp_root,
        "01_READ_ME_FIRST.md",
        (
            "# EGA I diplomatic French / paired-English / pre-Stacks checkpoint through printed p.127\n\n"
            "This is a coherent working checkpoint, not completion of EGA I or the eight-publication EGA corpus. It preserves the exact R50 diplomatic French generation through printed p.127, the matching R59 127-file English source tree, the page-bound decision and error ledgers, and the stable pre-Stacks semantic scaffold. The live producer had already entered p.128, so the three changed surfaces were reconstructed only in this immutable snapshot from the producer's exact inverse bindings and independently matched the p.127 hashes.\n\n"
            "The French source is diplomatic: printed wording and catalogued source errors remain visible rather than being silently corrected. English corrections are a separate, individually reasoned layer. The NUMDAM authority PDF and page rasters are not redistributed in this package. Existing complete EGA readers remain the front-facing readers; this package is source/provenance custody.\n"
        ),
    )
    write_text(
        temp_root,
        "07_RIGHTS_AND_PROVENANCE.md",
        (
            "# Rights and provenance\n\n"
            "The source authority is the eight-publication NUMDAM EGA corpus identified in the included controls. No NUMDAM PDF, publisher scan, page raster, or third-party comparison file is included. Underlying-work and scan rights remain with their rightsholders. No package-wide license is invented.\n\n"
            "French TeX is a diplomatic project transcription. English TeX is a source-rechecked project layer and is not authority for the French. The p.127 source restoration is deterministic and hash-exact; it does not mutate the later live producer tree. Raw private provenance remains in separate custody. Public provenance is a minimally transformed projection with every replacement event bound by token length and SHA-256.\n"
        ),
    )

    event_fields = ("relative_path", "transform_class", "original_token_bytes", "original_token_sha256", "replacement")
    with (temp_root / "08_PRIVACY_TRANSFORMATIONS.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=event_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(events)

    residuals: list[dict[str, object]] = []
    remaining_emails: list[dict[str, object]] = []
    mandated_task_ids = 0
    for path in sorted((p for p in temp_root.rglob("*") if p.is_file())):
        rel = path.relative_to(temp_root).as_posix()
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8")
        for pattern_name, pattern in (
            ("user_home", RESIDUAL_USER_HOME),
            ("private_codex_state", CODEX_PATH_SEGMENT),
            ("private_email", PRIVATE_EMAIL),
            ("hardcoded_secret", HARDCODED_SECRET),
        ):
            count = len(pattern.findall(text))
            if count:
                residuals.append({"relative_path": rel, "pattern": pattern_name, "count": count})
        task_count = len(TASK_ID.findall(text))
        if task_count:
            if rel == "controls/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md":
                mandated_task_ids += task_count
            else:
                residuals.append({"relative_path": rel, "pattern": "internal_task_id", "count": task_count})
        for email in ANY_EMAIL.findall(text):
            remaining_emails.append({"relative_path": rel, "email_sha256": sha256(email.encode("utf-8"))})
    if residuals or remaining_emails or mandated_task_ids != 3:
        raise RuntimeError(
            f"public privacy gate failed: residuals={residuals}, emails={remaining_emails}, mandated={mandated_task_ids}"
        )

    privacy_validation = {
        "status": "PASS",
        "errors": [],
        "files_bound": len(file_bindings),
        "transformed_files": sum(1 for row in file_bindings if row["transformed"]),
        "transformation_events": len(events),
        "residual_private_patterns": 0,
        "remaining_email_addresses": 0,
        "mandated_task_id_exceptions": 3,
        "mandated_exception_file": "controls/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md",
        "raw_private_source_mutated": False,
        "file_bindings": file_bindings,
    }
    write_bytes(temp_root, "09_PRIVACY_VALIDATION.json", json_bytes(privacy_validation))

    payload_excluded = {
        "00_EGA_I_P127_Diplomatic_French_Paired_English_PreStacks_Source.zip",
        "10_PACKAGE_PAYLOAD_MANIFEST.csv",
        "11_ZENODO_UPLOAD_MANIFEST.csv",
        "12_PACKAGE_VALIDATION.json",
    }
    payload_rows = rows_for_tree(temp_root, payload_excluded)
    write_manifest(temp_root / "10_PACKAGE_PAYLOAD_MANIFEST.csv", payload_rows)
    zip_members = [str(row["relative_path"]) for row in payload_rows] + ["10_PACKAGE_PAYLOAD_MANIFEST.csv"]
    zip_identity = make_zip(
        temp_root / "00_EGA_I_P127_Diplomatic_French_Paired_English_PreStacks_Source.zip",
        temp_root,
        zip_members,
    )

    direct_names = [
        "00_EGA_I_P127_Diplomatic_French_Paired_English_PreStacks_Source.zip",
        "01_READ_ME_FIRST.md",
        "02_EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P127.md",
        "03_EGA_PROJECT_LOGBOOK_P127_PUBLIC_PRIVACY_CLEAN.md",
        "04_EGA_CONTINUATION_HANDOFF_P127_PUBLIC_PRIVACY_CLEAN.md",
        "05_EGA_STATUS_P127_PUBLIC_PRIVACY_CLEAN.md",
        "06_EGA1_CHAPTER1_P127_VALIDATION_R50.json",
        "06a_FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P127_20260803.jsonl",
        "06b_ENGLISH_CORRECTION_RECHECK_APPEND_P127_20260803.jsonl",
        "06c_WORKFLOW_ERROR_APPEND_P127_20260803.jsonl",
        "07_RIGHTS_AND_PROVENANCE.md",
        "08_PRIVACY_TRANSFORMATIONS.csv",
        "09_PRIVACY_VALIDATION.json",
        "10_PACKAGE_PAYLOAD_MANIFEST.csv",
    ]
    upload_rows: list[dict[str, object]] = []
    for rel in direct_names:
        data = (temp_root / rel).read_bytes()
        upload_rows.append(
            {
                "relative_path": rel,
                "bytes": len(data),
                "sha256": sha256(data),
                "ega_concept": "10.5281/zenodo.20414353",
                "methodology_concept": "10.5281/zenodo.21124403",
                "replication_concept": "10.5281/zenodo.20461174",
                "direct_public": "true",
            }
        )
    write_manifest(
        temp_root / "11_ZENODO_UPLOAD_MANIFEST.csv",
        upload_rows,
        ("ega_concept", "methodology_concept", "replication_concept", "direct_public"),
    )

    final_rows = rows_for_tree(temp_root, {"12_PACKAGE_VALIDATION.json"})
    package_validation = {
        "status": "PASS_READY_FOR_EXACT_ARCHIVE_CUSTODY_AND_PUBLICATION",
        "errors": [],
        "scope": "EGA I diplomatic French and paired English through printed p.127; whole EGA remains incomplete",
        "printed_page": 127,
        "next_producer_cursor_at_freeze": "printed p.128; live producer work deliberately excluded",
        "private_custody": {
            "status": private_validation["status"],
            "represented_files": private_validation["represented_files"],
            "represented_bytes": private_validation["represented_bytes"],
            "canonical_tree_sha256": private_validation["canonical_tree_sha256"],
        },
        "public_projection": {
            "files_before_validation": len(final_rows),
            "bytes_before_validation": sum(int(row["bytes"]) for row in final_rows),
            "canonical_tree_sha256": canonical_tree_sha(final_rows),
            "payload_manifest_rows": len(payload_rows),
            "zip": zip_identity,
            "direct_upload_objects": len(upload_rows),
        },
        "privacy": privacy_validation,
        "rights": {
            "authority_pdfs_included": 0,
            "authority_rasters_included": 0,
            "third_party_comparison_files_included": 0,
            "package_wide_license_invented": False,
        },
        "routing": {
            "ega_existing_concept": "10.5281/zenodo.20414353",
            "methodology_existing_concept": "10.5281/zenodo.21124403",
            "replication_existing_concept": "10.5281/zenodo.20461174",
            "fac_payload_included": False,
            "gaga_payload_included": False,
            "new_concept_authorized": False,
        },
    }
    write_bytes(temp_root, "12_PACKAGE_VALIDATION.json", json_bytes(package_validation))
    return package_validation


def atomic_build(final: Path, build_function, *args):
    if final.exists():
        raise RuntimeError(f"refusing to overwrite existing immutable root: {final}")
    final.parent.mkdir(parents=True, exist_ok=True)
    temp = Path(tempfile.mkdtemp(prefix=f".{final.name}.building-", dir=final.parent))
    try:
        result = build_function(temp, *args)
        os.replace(temp, final)
        return result
    except Exception:
        print(json.dumps({"status": "FAILED", "preserved_incomplete_temp": str(temp)}, indent=2))
        raise


def main() -> None:
    private_validation = atomic_build(PRIVATE_FINAL, build_private)
    public_validation = atomic_build(PUBLIC_FINAL, build_public, PRIVATE_FINAL, private_validation)
    summary = {
        "status": "PASS",
        "private_root": str(PRIVATE_FINAL),
        "private_files": len([p for p in PRIVATE_FINAL.rglob("*") if p.is_file()]),
        "private_bytes": sum(p.stat().st_size for p in PRIVATE_FINAL.rglob("*") if p.is_file()),
        "private_tree_sha256": private_validation["canonical_tree_sha256"],
        "public_root": str(PUBLIC_FINAL),
        "public_files": len([p for p in PUBLIC_FINAL.rglob("*") if p.is_file()]),
        "public_bytes": sum(p.stat().st_size for p in PUBLIC_FINAL.rglob("*") if p.is_file()),
        "public_tree_sha256": public_validation["public_projection"]["canonical_tree_sha256"],
        "zip": public_validation["public_projection"]["zip"],
        "privacy_events": public_validation["privacy"]["transformation_events"],
        "privacy_errors": public_validation["privacy"]["errors"],
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
