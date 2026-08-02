#!/usr/bin/env python3
"""Build exact private custody and a privacy-clean all-session provenance tranche.

The tranche is deliberately provenance-first.  It captures project-authored
logbooks, status/continuation surfaces, and every text control file from the
active FAC, EGA, Deligne D001--D007, SGA7 I, and SGA7 II producer roots.  Raw
bytes are copied only to private custody.  Public objects are separately
redacted, structurally replayed, grouped into complete per-corpus provenance
ZIPs, and accompanied by loose core logbooks plus exact manifests.

Exactly 34 public objects are produced so the current 66-file methodology
record can receive the complete tranche without exceeding Zenodo's 100-file
record limit.  The same upload manifest is intended for the replication DOI.
No GitHub or Zenodo mutation is performed by this builder.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import time
import zipfile
from collections import Counter
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any

from build_fac_ega_live_custody_snapshot_20260802 import (
    TEXT_EXTENSIONS,
    decode_text,
    encode_text,
    redact_text,
    residual_text_findings,
    sha256_bytes,
    sha256_path,
    write_zip,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
INTERLANGUAGE = Path("C:/Users/Floris/Documents/interlanguage")
ENGLISH_GERMANIC = (
    INTERLANGUAGE
    / "03_projects/language_management/english_germanic"
)
WORKING_TRANSLATIONS = ENGLISH_GERMANIC / "03_working_translations"
TRANSCRIPTIONS = INTERLANGUAGE / "Transcription/03_working_transcriptions"
CONTROL_ROOT = ENGLISH_GERMANIC / "00_lane_control"

METHODOLOGY_DOI = "10.5281/zenodo.21124403"
REPLICATION_DOI = "10.5281/zenodo.20461174"
CONCEPT_DOIS = {
    "FAC": "10.5281/zenodo.21720996",
    "EGA": "10.5281/zenodo.20414353",
    "DELIGNE": "10.5281/zenodo.20410853",
    "SGA7": "10.5281/zenodo.20410947",
}
CONTROL_IDENTITIES = {
    "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md": (
        2_296,
        "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679",
    ),
    "ARCHIVE_PROACTIVE_PRIVACY_AND_SUBSTANTIVE_UPDATE_REQUIREMENT_20260802.md": (
        3_818,
        "098B41A98D9BE38E67316F5F34E4E2FE8F72613231268FC66C07801809C8613E",
    ),
}
PROVENANCE_NAME_RE = re.compile(
    r"(?i)(LOGBOOK|STATUS|CONTINUATION|HANDOFF|DECISION|REVISION|"
    r"REVERSAL|ERROR|CORRECTION|REPAIR|VALIDATION|PROGRESS|IDENTIT|"
    r"NORMALIZATION|SEMANTIC|LINEAGE|SOURCE_INPUT|MANIFEST|POLICY|RULE)"
)
EXPECTED_UPLOAD_OBJECTS = 34


@dataclass(frozen=True)
class Project:
    group: str
    key: str
    root: Path
    loose_paths: tuple[str, ...]


PROJECTS = (
    Project(
        "FAC",
        "FAC",
        WORKING_TRANSLATIONS / "serre_fac_english_source_aligned_successor_20260802_r1",
        ("LOGBOOK.md", "EDITORIAL_DECISION_LOGBOOK.md", "STATUS.md"),
    ),
    Project(
        "EGA",
        "EGA_EN",
        WORKING_TRANSLATIONS / "EGA_English_Global_0_IV_french_recheck_source_successor_20260802_r1",
        ("LOGBOOK.md", "STATUS.md"),
    ),
    Project(
        "EGA",
        "EGA_FR",
        TRANSCRIPTIONS / "EGA_French_NUMDAM_canonical_TeX_20260801_r1",
        ("LOGBOOK.md", "CONTINUATION_HANDOFF.md", "STATUS.md"),
    ),
    Project("DELIGNE", "D001", TRANSCRIPTIONS / "D001_bilingual_parallel_layout_successor_20260802_r1", ("LOGBOOK.md",)),
    Project("DELIGNE", "D002", TRANSCRIPTIONS / "D002_bilingual_parallel_layout_successor_20260802_r1", ("LOGBOOK.md",)),
    Project("DELIGNE", "D003", TRANSCRIPTIONS / "D003_bilingual_parallel_layout_successor_20260802_r1", ("LOGBOOK.md",)),
    Project("DELIGNE", "D004", TRANSCRIPTIONS / "D004_bilingual_parallel_layout_successor_20260802_r1", ("LOGBOOK.md",)),
    Project("DELIGNE", "D005_R1", TRANSCRIPTIONS / "D005_bilingual_source_aligned_successor_20260801_r1", ("LOGBOOK.md",)),
    Project("DELIGNE", "D005_R2", TRANSCRIPTIONS / "D005_bilingual_parallel_layout_successor_20260802_r1", ("LOGBOOK.md",)),
    Project(
        "DELIGNE",
        "D006",
        TRANSCRIPTIONS / "D006_bilingual_source_aligned_successor_20260802_r1",
        (
            "LOGBOOK.md",
            "LOGBOOK_RECOVERED_FROM_THREAD_HISTORY_20260802.md",
            "controls/LOGBOOK_STATUS_NUL_CORRUPTION_AND_RECOVERY_20260802.md",
        ),
    ),
    Project("DELIGNE", "D007", TRANSCRIPTIONS / "D007_bilingual_source_aligned_successor_20260802_r1", ("LOGBOOK.md",)),
    Project(
        "SGA7",
        "SGA7I",
        WORKING_TRANSLATIONS / "sga7i_english_complete_translation_successor_20260731_r1",
        ("FRENCH_SOURCE_CORRECTION_LOGBOOK.md",),
    ),
    Project(
        "SGA7",
        "SGA7II",
        WORKING_TRANSLATIONS / "sga7ii_english_complete_translation_successor_20260801_r1",
        ("LOGBOOK.md",),
    ),
)


@dataclass(frozen=True)
class CapturedFile:
    group: str
    project: str
    relative_path: str
    source_path: Path
    data: bytes
    bytes: int
    sha256: str
    mtime_ns: int
    loose: bool


@dataclass(frozen=True)
class PublicFile:
    original: CapturedFile
    public_data: bytes
    public_bytes: int
    public_sha256: str
    encoding: str
    action_count: int
    rules: tuple[str, ...]


def csv_data(header: tuple[str, ...], rows: list[tuple[Any, ...]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def json_data(value: Any) -> bytes:
    return (
        json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2) + "\n"
    ).encode("utf-8")


def md5_path(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def is_selected(project: Project, path: Path) -> bool:
    relative = path.relative_to(project.root).as_posix()
    pure = PurePosixPath(relative)
    if pure.suffix.casefold() not in TEXT_EXTENSIONS:
        return False
    if relative in project.loose_paths:
        return True
    if pure.parts and pure.parts[0].casefold() == "controls":
        return True
    return bool(PROVENANCE_NAME_RE.search(pure.name))


def scan_project(project: Project, include_data: bool) -> list[CapturedFile]:
    if not project.root.is_dir():
        raise RuntimeError(f"Missing producer root: {project.key}: {project.root}")
    rows: list[CapturedFile] = []
    for path in sorted(project.root.rglob("*")):
        if not path.is_file() or not is_selected(project, path):
            continue
        relative = path.relative_to(project.root).as_posix()
        data = path.read_bytes()
        stat = path.stat()
        rows.append(
            CapturedFile(
                group=project.group,
                project=project.key,
                relative_path=relative,
                source_path=path,
                data=data if include_data else b"",
                bytes=len(data),
                sha256=sha256_bytes(data),
                mtime_ns=stat.st_mtime_ns,
                loose=relative in project.loose_paths,
            )
        )
    present = {row.relative_path for row in rows}
    missing = sorted(set(project.loose_paths) - present)
    if missing:
        raise RuntimeError(f"Missing mandatory loose logbooks for {project.key}: {missing}")
    if not rows:
        raise RuntimeError(f"No provenance files selected for {project.key}")
    return rows


def stable_identity(rows: list[CapturedFile]) -> list[tuple[str, str, int, str, int]]:
    return sorted(
        (
            row.group,
            f"{row.project}/{row.relative_path}",
            row.bytes,
            row.sha256,
            row.mtime_ns,
        )
        for row in rows
    )


def validate_structure(relative: str, data: bytes) -> None:
    suffix = PurePosixPath(relative).suffix.casefold()
    decoded = decode_text(data, relative)
    if decoded is None:
        raise RuntimeError(f"Projected provenance is not text: {relative}")
    text = decoded[0]
    if suffix == ".json":
        try:
            json.loads(text)
        except json.JSONDecodeError as error:
            raise RuntimeError(f"Invalid projected JSON: {relative}: {error}") from error
    elif suffix == ".jsonl":
        for line_number, line in enumerate(text.splitlines(), start=1):
            if not line.strip():
                raise RuntimeError(f"Blank JSONL row: {relative}:{line_number}")
            try:
                json.loads(line)
            except json.JSONDecodeError as error:
                raise RuntimeError(
                    f"Invalid projected JSONL: {relative}:{line_number}: {error}"
                ) from error
    elif suffix in {".csv", ".tsv"}:
        dialect = "excel-tab" if suffix == ".tsv" else "excel"
        list(csv.reader(io.StringIO(text), dialect=dialect))


def redact_json_value(
    value: Any, relative: str
) -> tuple[Any, list[tuple[str, str, int, int]]]:
    actions: list[tuple[str, str, int, int]] = []
    if isinstance(value, str):
        redacted, found = redact_text(value, relative)
        actions.extend(found)
        return redacted, actions
    if isinstance(value, list):
        projected = []
        for item in value:
            redacted, found = redact_json_value(item, relative)
            projected.append(redacted)
            actions.extend(found)
        return projected, actions
    if isinstance(value, dict):
        projected: dict[str, Any] = {}
        for key, item in value.items():
            redacted_key, key_actions = redact_text(str(key), relative)
            redacted_item, item_actions = redact_json_value(item, relative)
            if redacted_key in projected:
                raise RuntimeError(
                    f"JSON key collision after privacy projection: {relative}: {redacted_key}"
                )
            projected[redacted_key] = redacted_item
            actions.extend(key_actions)
            actions.extend(item_actions)
        return projected, actions
    return value, actions


def project_public(row: CapturedFile) -> tuple[PublicFile, list[tuple[str, str, int, int]]]:
    public_relative = f"{row.group}/{row.project}/{row.relative_path}"
    decoded = decode_text(row.data, public_relative)
    if decoded is None:
        raise RuntimeError(f"Selected provenance file is not text: {public_relative}")
    suffix = PurePosixPath(row.relative_path).suffix.casefold()
    if suffix == ".json":
        value = json.loads(decoded[0])
        projected, actions = redact_json_value(value, public_relative)
        redacted = json.dumps(
            projected, ensure_ascii=True, sort_keys=True, indent=2
        ) + "\n"
        actions.append((public_relative, "json_structural_reencode", 1, 1))
        encoding = "utf-8-json-reencoded"
        data = redacted.encode("utf-8")
    elif suffix == ".jsonl":
        projected_lines: list[str] = []
        actions = []
        for line_number, line in enumerate(decoded[0].splitlines(), start=1):
            if not line.strip():
                raise RuntimeError(f"Blank source JSONL row: {public_relative}:{line_number}")
            value = json.loads(line)
            projected, found = redact_json_value(value, public_relative)
            projected_lines.append(
                json.dumps(
                    projected,
                    ensure_ascii=True,
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
            actions.extend(found)
        redacted = "\n".join(projected_lines) + "\n"
        actions.append((public_relative, "jsonl_structural_reencode", 1, 1))
        encoding = "utf-8-jsonl-reencoded"
        data = redacted.encode("utf-8")
    else:
        redacted, actions = redact_text(decoded[0], public_relative)
        encoding = decoded[1]
        data = encode_text(redacted, decoded[1])
    residual = residual_text_findings(redacted)
    if residual:
        raise RuntimeError(f"Privacy residual in {public_relative}: {residual}")
    validate_structure(public_relative, data)
    return (
        PublicFile(
            original=row,
            public_data=data,
            public_bytes=len(data),
            public_sha256=sha256_bytes(data),
            encoding=encoding,
            action_count=len(actions),
            rules=tuple(sorted({action[1] for action in actions})),
        ),
        actions,
    )


def safe_prepare(path: Path, allowed_parent: Path) -> None:
    resolved = path.resolve()
    parent = allowed_parent.resolve()
    if resolved == parent or parent not in resolved.parents:
        raise RuntimeError(f"Output outside allowed parent: {resolved}")
    if resolved.exists():
        raise RuntimeError(f"Output already exists: {resolved}")
    resolved.mkdir(parents=True)


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def zip_inventory(path: Path) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError(f"ZIP CRC replay failed: {path}")
        for info in archive.infolist():
            if info.is_dir():
                continue
            data = archive.read(info.filename)
            rows.append(
                {
                    "name": info.filename,
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                }
            )
    rows.sort(key=lambda row: row["name"])
    return {
        "zip_member_count": len(rows),
        "zip_uncompressed_bytes": sum(int(row["bytes"]) for row in rows),
        "zip_inventory_sha256": sha256_bytes(
            json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8")
        ),
    }


def upload_row(output: Path, name: str, role: str, dual: bool = True) -> dict[str, Any]:
    path = output / name
    row: dict[str, Any] = {
        "name": name,
        "path": name,
        "bytes": path.stat().st_size,
        "md5": md5_path(path),
        "sha256": sha256_path(path),
        "role": role,
        "dual_doi_provenance": dual,
        "privacy_clean": True,
        "supersession_state": "APPEND_ONLY_HISTORY_PRESERVED_IN_CAPTURED_SURFACES",
    }
    if path.suffix.casefold() == ".zip":
        row.update(zip_inventory(path))
    return row


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot-id", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--private-custody-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not re.fullmatch(r"[A-Za-z0-9_.-]{12,100}", args.snapshot_id):
        raise RuntimeError("Unsafe snapshot id")
    public_parent = REPO_ROOT / "manifests/provenance-tranches"
    private_parent = Path("C:/Users/Floris/Documents/Codex/archive-private-custody")
    safe_prepare(args.output_dir, public_parent)
    safe_prepare(args.private_custody_dir, private_parent)
    output = args.output_dir.resolve()
    private = args.private_custody_dir.resolve()
    capture_started = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    captured: list[CapturedFile] = []
    for project in PROJECTS:
        captured.extend(scan_project(project, include_data=True))

    control_rows: list[CapturedFile] = []
    for name, (expected_bytes, expected_sha) in CONTROL_IDENTITIES.items():
        path = CONTROL_ROOT / name
        data = path.read_bytes()
        if (len(data), sha256_bytes(data)) != (expected_bytes, expected_sha):
            raise RuntimeError(f"Controlling archive file changed: {name}")
        control_rows.append(
            CapturedFile(
                "ARCHIVE",
                "ARCHIVE_CONTROL",
                name,
                path,
                data,
                len(data),
                sha256_bytes(data),
                path.stat().st_mtime_ns,
                True,
            )
        )
    shared_log = CONTROL_ROOT / "ENGLISH_GERMANIC_DECISION_LOG_v1.jsonl"
    shared_data = shared_log.read_bytes()
    control_rows.append(
        CapturedFile(
            "ARCHIVE",
            "SHARED_DECISION_LOG",
            shared_log.name,
            shared_log,
            shared_data,
            len(shared_data),
            sha256_bytes(shared_data),
            shared_log.stat().st_mtime_ns,
            True,
        )
    )
    captured.extend(control_rows)

    private_manifest_rows: list[tuple[Any, ...]] = []
    raw_members: list[tuple[str, bytes]] = []
    for row in captured:
        logical = f"{row.group}/{row.project}/{row.relative_path}"
        target = private / "raw" / PurePosixPath(logical)
        write_bytes(target, row.data)
        private_manifest_rows.append(
            (
                row.group,
                row.project,
                row.relative_path,
                str(row.source_path),
                row.bytes,
                row.sha256,
                row.mtime_ns,
                "EXACT_PRIVATE_ORIGINAL",
            )
        )
        raw_members.append((f"raw/{logical}", row.data))
    private_manifest = csv_data(
        (
            "group",
            "project",
            "relative_path",
            "absolute_source_path",
            "bytes",
            "sha256",
            "mtime_ns",
            "custody_status",
        ),
        private_manifest_rows,
    )
    write_bytes(private / "PRIVATE_ORIGINAL_PROVENANCE_MANIFEST.csv", private_manifest)
    raw_members.append(("PRIVATE_ORIGINAL_PROVENANCE_MANIFEST.csv", private_manifest))
    private_zip = private / f"{args.snapshot_id}__EXACT_PRIVATE_PROVENANCE.zip"
    private_zip_receipt = write_zip(private_zip, raw_members, zipfile.ZIP_DEFLATED)

    public: list[PublicFile] = []
    privacy_actions: list[tuple[str, str, int, int]] = []
    for row in captured:
        projected, actions = project_public(row)
        public.append(projected)
        privacy_actions.extend(actions)

    by_identity = {
        (row.original.group, row.original.project, row.original.relative_path): row
        for row in public
    }
    upload_names: list[str] = []
    group_summaries: dict[str, Any] = {}
    for group in ("FAC", "EGA", "DELIGNE", "SGA7"):
        rows = sorted(
            [row for row in public if row.original.group == group],
            key=lambda row: (row.original.project, row.original.relative_path),
        )
        manifest_name = f"{group}__COMPLETE_PROVENANCE_MANIFEST.csv"
        manifest_rows = [
            (
                row.original.project,
                row.original.relative_path,
                row.original.bytes,
                row.original.sha256,
                row.public_bytes,
                row.public_sha256,
                row.encoding,
                row.action_count,
                ";".join(row.rules),
                "PASS_PRIVACY_CLEAN_PUBLIC_PROJECTION",
                "CC0-1.0_PROJECT_AUTHORED_PROVENANCE",
                CONCEPT_DOIS[group],
                METHODOLOGY_DOI,
                REPLICATION_DOI,
                "PRESERVED_AS_CAPTURED_WITH_APPEND_ONLY_HISTORY",
            )
            for row in rows
        ]
        manifest = csv_data(
            (
                "project",
                "relative_path",
                "original_bytes",
                "original_sha256",
                "public_bytes",
                "public_sha256",
                "encoding",
                "privacy_action_count",
                "privacy_rules",
                "privacy_result",
                "license",
                "corpus_concept_doi",
                "methodology_concept_doi",
                "replication_concept_doi",
                "supersession_state",
            ),
            manifest_rows,
        )
        write_bytes(output / manifest_name, manifest)
        zip_name = f"{group}__COMPLETE_PROVENANCE.zip"
        members: list[tuple[str, bytes]] = [
            (
                f"payload/{row.original.project}/{row.original.relative_path}",
                row.public_data,
            )
            for row in rows
        ]
        members.append((manifest_name, manifest))
        write_zip(output / zip_name, members, zipfile.ZIP_DEFLATED)
        upload_names.extend((manifest_name, zip_name))
        group_summaries[group] = {
            "projects": sorted({row.original.project for row in rows}),
            "files": len(rows),
            "original_bytes": sum(row.original.bytes for row in rows),
            "public_bytes": sum(row.public_bytes for row in rows),
            "privacy_actions": sum(row.action_count for row in rows),
            "corpus_concept_doi": CONCEPT_DOIS[group],
            "manifest": manifest_name,
            "archive": zip_name,
        }

    for project in PROJECTS:
        for relative in project.loose_paths:
            row = by_identity[(project.group, project.key, relative)]
            suffix = PurePosixPath(relative).suffix
            stem = relative[: -len(suffix)] if suffix else relative
            remote = f"{project.key}__{stem.replace('/', '__')}{suffix}"
            write_bytes(output / remote, row.public_data)
            upload_names.append(remote)

    public_controls: dict[str, PublicFile] = {
        row.original.relative_path: row
        for row in public
        if row.original.group == "ARCHIVE"
    }
    for control_name in CONTROL_IDENTITIES:
        row = public_controls[control_name]
        write_bytes(output / control_name, row.public_data)
        upload_names.append(control_name)
    shared_remote = "ENGLISH_GERMANIC_DECISION_LOG_v1.jsonl"
    write_bytes(
        output / shared_remote,
        public_controls[shared_log.name].public_data,
    )
    upload_names.append(shared_remote)

    readme_name = "ALL_SESSION_PROVENANCE_TRANCHE_README.md"
    readme = (
        "# All-session mathematical transcription and translation provenance tranche\n\n"
        f"Snapshot: `{args.snapshot_id}`. This tranche exposes the reasoning surfaces "
        "needed to audit AI-assisted transcription and translation: complete project "
        "control/log histories grouped in four ZIPs, exact public manifests, and every "
        "current core logbook as a loose file. It preserves decisions, rejected paths, "
        "errors, recoveries, reversals, validation records, and continuation state; it "
        "does not select only attractive outputs.\n\n"
        f"The identical 34-object tranche is intended for methodology `{METHODOLOGY_DOI}` "
        f"and replication `{REPLICATION_DOI}`. Each group ZIP and manifest is also bound "
        "to its existing corpus concept DOI. Raw originals remain exact in private "
        "custody; public bytes are separate privacy-clean projections with every "
        "transformation recorded.\n\n"
        "These records make the model's reasoning and correction history inspectable. "
        "They do not certify mathematical correctness, source completeness, translation "
        "quality, native-language review, critical-edition status, or peer review.\n"
    ).encode("utf-8")
    write_bytes(output / readme_name, readme)
    upload_names.append(readme_name)

    index_name = "ALL_SESSION_PROVENANCE_TRANCHE_INDEX.json"
    controlling_name = (
        "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
    )
    controlling_original_bytes, controlling_original_sha256 = CONTROL_IDENTITIES[
        controlling_name
    ]
    controlling_public = public_controls[controlling_name]
    index = {
        "schema": "all-session-provenance-tranche-v1",
        "snapshot_id": args.snapshot_id,
        "capture_started_utc": capture_started,
        "methodology_concept_doi": METHODOLOGY_DOI,
        "replication_concept_doi": REPLICATION_DOI,
        "control_binding": {
            "relative_path": controlling_name,
            "original_bytes": controlling_original_bytes,
            "original_sha256": controlling_original_sha256,
            "public_bytes": controlling_public.public_bytes,
            "public_sha256": controlling_public.public_sha256,
            "privacy_result": "PASS_PRIVACY_CLEAN_PUBLIC_PROJECTION",
            "status": (
                "BOUND_EXACT_ORIGINAL_IDENTITY_WITH_PRIVACY_CLEAN_PUBLIC_PROJECTION"
            ),
            "public_disclosure_of_original": False,
        },
        "groups": group_summaries,
        "private_original": {
            "files": len(captured),
            "bytes": sum(row.bytes for row in captured),
            "manifest_sha256": sha256_bytes(private_manifest),
            "archive_sha256": private_zip_receipt["sha256"],
            "public_disclosure": False,
        },
        "public_projection": {
            "files": len(public),
            "bytes": sum(row.public_bytes for row in public),
            "privacy_actions": len(privacy_actions),
            "residual_privacy_findings": 0,
        },
        "scope": (
            "FAC, EGA English corrections, EGA French canon, Deligne D001-D007 "
            "including D005 and D006 recovery history, SGA7 I, SGA7 II, archive "
            "controls, and the locked shared English/Germanic decision log"
        ),
        "completion_claimed": False,
        "mathematical_certification_claimed": False,
        "errors": [],
    }
    write_bytes(output / index_name, json_data(index))
    upload_names.append(index_name)

    sums_name = "ALL_SESSION_PROVENANCE_TRANCHE_SHA256SUMS.csv"
    sums = csv_data(
        ("name", "bytes", "sha256"),
        [
            (
                name,
                (output / name).stat().st_size,
                sha256_path(output / name),
            )
            for name in sorted(upload_names)
        ],
    )
    write_bytes(output / sums_name, sums)
    upload_names.append(sums_name)

    if len(upload_names) != EXPECTED_UPLOAD_OBJECTS or len(upload_names) != len(
        set(upload_names)
    ):
        raise RuntimeError(
            f"Expected {EXPECTED_UPLOAD_OBJECTS} unique public objects; "
            f"got {len(upload_names)} / {len(set(upload_names))}"
        )

    upload_rows = [
        upload_row(
            output,
            name,
            (
                "complete corpus provenance archive"
                if name.endswith("__COMPLETE_PROVENANCE.zip")
                else "exact corpus provenance manifest"
                if name.endswith("__COMPLETE_PROVENANCE_MANIFEST.csv")
                else "privacy-clean first-class producer logbook or continuation surface"
                if name.endswith((".md", ".jsonl"))
                else "all-session provenance control and index"
            ),
        )
        for name in sorted(upload_names)
    ]
    upload_manifest = {
        "schema": "zenodo-upload-manifest-v1",
        "snapshot_id": args.snapshot_id,
        "identical_methodology_replication_payload": True,
        "files": upload_rows,
    }
    write_bytes(output / "UPLOAD_MANIFEST.json", json_data(upload_manifest))

    after: list[CapturedFile] = []
    for project in PROJECTS:
        after.extend(scan_project(project, include_data=False))
    for row in control_rows:
        data = row.source_path.read_bytes()
        stat = row.source_path.stat()
        after.append(
            CapturedFile(
                row.group,
                row.project,
                row.relative_path,
                row.source_path,
                b"",
                len(data),
                sha256_bytes(data),
                stat.st_mtime_ns,
                row.loose,
            )
        )
    if stable_identity(captured) != stable_identity(after):
        raise RuntimeError("Producer provenance changed during stable capture replay")

    for path in sorted(output.iterdir()):
        if not path.is_file() or path.suffix.casefold() == ".zip":
            continue
        decoded = decode_text(path.read_bytes(), path.name)
        if decoded is not None and residual_text_findings(decoded[0]):
            raise RuntimeError(f"Generated public privacy residual: {path.name}")

    action_counts = Counter(action[1] for action in privacy_actions)
    validation = {
        "schema": "all-session-provenance-tranche-build-v1",
        "status": "PASS_EXACT_PRIVATE_AND_PRIVACY_CLEAN_PUBLIC_PROVENANCE_TRANCHE",
        "snapshot_id": args.snapshot_id,
        "capture_started_utc": capture_started,
        "capture_completed_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "producer_sources_mutated": False,
        "github_mutation_performed": False,
        "zenodo_mutation_performed": False,
        "private_original": {
            "files": len(captured),
            "bytes": sum(row.bytes for row in captured),
            "manifest_bytes": len(private_manifest),
            "manifest_sha256": sha256_bytes(private_manifest),
            "archive": private_zip_receipt,
        },
        "public_projection": {
            "files": len(public),
            "bytes": sum(row.public_bytes for row in public),
            "privacy_actions": len(privacy_actions),
            "privacy_actions_by_rule": dict(sorted(action_counts.items())),
            "residual_findings": 0,
        },
        "groups": group_summaries,
        "upload_objects": len(upload_rows),
        "upload_manifest": {
            "bytes": (output / "UPLOAD_MANIFEST.json").stat().st_size,
            "sha256": sha256_path(output / "UPLOAD_MANIFEST.json"),
        },
        "methodology_successor_file_count": 66 + len(upload_rows),
        "replication_successor_file_count": 11 + len(upload_rows),
        "identical_methodology_replication_payload": True,
        "completion_or_certification_inferred": False,
        "errors": [],
    }
    write_bytes(output / "BUILD_VALIDATION.json", json_data(validation))
    write_bytes(
        private / "PRIVATE_CUSTODY_VALIDATION.json",
        json_data(validation["private_original"] | {"errors": [], "status": "PASS"}),
    )
    print(json.dumps(validation, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
