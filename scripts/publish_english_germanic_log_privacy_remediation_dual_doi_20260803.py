#!/usr/bin/env python3
"""Publish the corrected v2 English/Germanic log privacy projection.

The immutable raw append-only log remains unchanged in private lane custody and
all superseded Zenodo versions remain immutable.  This publisher creates one
new version only under each existing methodology and replication concept.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import os
import re
import shutil
import time
import urllib.parse
import zipfile
from dataclasses import dataclass
from pathlib import Path

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
REPO = Path(__file__).resolve().parents[1]
CONTROL_ROOT = Path(os.environ["ENGLISH_GERMANIC_CONTROL_ROOT"]).resolve()
SOURCE_ROOT = REPO / "sources/sga/sga1-7ii-presentation-clean-complete-20260803-r2"
TEMP = REPO / "tmp/zenodo/english-germanic-log-privacy-remediation-v2-20260803"
STATE = TEMP / "state.json"

RAW_LOG_NAME = "ENGLISH_GERMANIC_DECISION_LOG_v1.jsonl"
PREDECESSOR_CLEAN_LOG_NAME = "00_ENGLISH_GERMANIC_DECISION_LOG_1_PUBLIC_PRIVACY_CLEAN_v1.jsonl"
PREDECESSOR_LEDGER_NAME = "00_ENGLISH_GERMANIC_DECISION_LOG_2_PRIVACY_TRANSFORMATIONS_20260803.csv"
PREDECESSOR_ZIP_NAME = "SGA_1-7II_PRESENTATION_CLEAN_PROVENANCE_20260803.zip"
PREDECESSOR_MANIFEST_NAME = "SGA_1-7II_PRESENTATION_CLEAN_PROVENANCE_MANIFEST_20260803.csv"
PREDECESSOR_REPLACE_NAMES = {
    PREDECESSOR_CLEAN_LOG_NAME,
    PREDECESSOR_LEDGER_NAME,
    PREDECESSOR_ZIP_NAME,
    PREDECESSOR_MANIFEST_NAME,
}
CLEAN_LOG_NAME = "00_ENGLISH_GERMANIC_DECISION_LOG_1_PUBLIC_PRIVACY_CLEAN_v2.jsonl"
LEDGER_NAME = "00_ENGLISH_GERMANIC_DECISION_LOG_2_PRIVACY_TRANSFORMATIONS_v2_20260803.csv"
VALIDATION_NAME = "ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_VALIDATION_v2_20260803.json"
NOTE_NAME = "ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_REMEDIATION_v2_20260803.md"
ZIP_NAME = "SGA_1-7II_PRESENTATION_CLEAN_PROVENANCE_v2_20260803.zip"
MANIFEST_NAME = "SGA_1-7II_PRESENTATION_CLEAN_PROVENANCE_MANIFEST_v2_20260803.csv"
CONTROL_NAME = "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
CONTROL_SHA256 = "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679"
REMEDIATION_DECISION_NAME = (
    "ARCHIVE_DECISION_RECORD_ENGLISH_GERMANIC_LOG_PRIVACY_REMEDIATION_20260803.json"
)
REMEDIATION_DECISION_ID = (
    "EG-ARCHIVE-ENGLISH-GERMANIC-LOG-PRIVACY-REMEDIATION-20260803-0001"
)
COUNT_CORRECTION_NAME = (
    "ARCHIVE_DECISION_RECORD_ENGLISH_GERMANIC_LOG_PRIVACY_COUNT_CORRECTION_20260803.json"
)
COUNT_CORRECTION_ID = (
    "EG-ARCHIVE-ENGLISH-GERMANIC-LOG-PRIVACY-COUNT-CORRECTION-20260803-0001"
)
RESIDUAL_REMEDIATION_DECISION_NAME = (
    "ARCHIVE_DECISION_RECORD_ENGLISH_GERMANIC_LOG_PRIVACY_RESIDUAL_TASK_ID_REMEDIATION_20260803.json"
)
RESIDUAL_REMEDIATION_DECISION_ID = (
    "EG-ARCHIVE-ENGLISH-GERMANIC-LOG-PRIVACY-RESIDUAL-TASK-ID-REMEDIATION-20260803-0001"
)
PRIOR_DECISION_FILES = (
    "ARCHIVE_DECISION_RECORD_SGA_GITHUB_PR257_MERGED_20260803_2025.json",
    "ARCHIVE_DECISION_RECORD_SGA_PRESENTATION_CLEAN_DUAL_DOI_PUBLISHED_20260803_2025.json",
    "ARCHIVE_DECISION_RECORD_SGA_PRIVACY_REMEDIATION_PUBLISHED_20260803_2025.json",
)
STALE_ATTEMPT_NAMES = {
    "ENGLISH_GERMANIC_DECISION_LOG_PUBLIC_PRIVACY_CLEAN_v1.jsonl",
    "ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_TRANSFORMATIONS_20260803.csv",
    "ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_VALIDATION_20260803.json",
}


@dataclass(frozen=True)
class Target:
    key: str
    predecessor: int
    concept_doi: str
    files: int
    total_bytes: int
    version: str


TARGETS = (
    Target(
        "methodology",
        21_779_952,
        "10.5281/zenodo.21124403",
        100,
        4_990_612_147,
        "2026-08-03 privacy-clean English/Germanic decision-log closure v2",
    ),
    Target(
        "replication",
        21_779_957,
        "10.5281/zenodo.20461174",
        65,
        9_013_124,
        "2026-08-03 privacy-clean English/Germanic decision-log closure v2",
    ),
)


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
TASK_ID = re.compile(
    r"(?i)019[0-9a-f]{5}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
)
PRIVATE_EMAIL = re.compile(r"(?i)\bmemo_lepthy@live\.nl\b")
CODEX_PATH_SEGMENT = re.compile(r"(?i)(?P<sep>[\\/])\.codex(?=(?:[\\/]|$))")
RESIDUAL_USER_HOME = re.compile(
    r"(?i)(?:[A-Za-z]:[\\/]Users[\\/][^\\/\s\"']+|/(?:Users|home)/[^/\s\"']+)"
)
HARDCODED_SECRET = re.compile(
    r"(?i)(?:access[_-]?token|api[_-]?key|github[_-]?token)\s*[:=]\s*[\"'][A-Za-z0-9_\-]{16,}"
)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5_path(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def file_row(path: Path) -> dict[str, object]:
    return {
        "path": path,
        "bytes": path.stat().st_size,
        "sha256": sha256_path(path),
        "md5": md5_path(path),
    }


def identity(entry: dict) -> tuple[int, str]:
    return int(entry["size"]), base.normalized_md5(entry["checksum"])


def file_surface_sha256(entries: dict[str, dict]) -> str:
    lines = [
        f"{name}\t{int(entries[name]['size'])}\t{base.normalized_md5(entries[name]['checksum'])}"
        for name in sorted(entries, key=str.casefold)
    ]
    return sha256_bytes("\n".join(lines).encode("utf-8"))


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"targets": {}}


def save_state(value: dict) -> None:
    TEMP.mkdir(parents=True, exist_ok=True)
    base.save_json(STATE, value)


def current_guard(session, target: Target) -> tuple[dict, dict[str, dict]]:
    current = base.check(
        session.get(
            f"{API}/records/{target.predecessor}?expand=true",
            headers=MODERN,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    entries = base.modern_entries(current)
    latest = base.check(
        session.get(current["links"]["latest"], headers=MODERN, timeout=(30, 300)),
        {200},
    ).json()
    if (
        current.get("is_published") is not True
        or current["parent"]["pids"]["doi"]["identifier"] != target.concept_doi
        or len(entries) != target.files
        or sum(int(row["size"]) for row in entries.values()) != target.total_bytes
        or int(latest["id"]) != target.predecessor
        or not PREDECESSOR_REPLACE_NAMES.issubset(entries)
        or RAW_LOG_NAME in entries
    ):
        raise RuntimeError(f"{target.key} predecessor guard changed")
    return current, entries


def prepare_drafts(session, token: str, state: dict) -> dict:
    auth_legacy = {"Authorization": f"Bearer {token}"}
    auth_modern = {**MODERN, "Authorization": f"Bearer {token}"}
    for target in TARGETS:
        current, _entries = current_guard(session, target)
        tracked = state["targets"].get(target.key, {})
        if tracked.get("draft_id"):
            probe = session.get(
                f"{API}/records/{int(tracked['draft_id'])}/draft?expand=true",
                headers=auth_modern,
                timeout=(30, 300),
            )
            if probe.status_code != 200 or int(probe.json()["id"]) != int(tracked["draft_id"]):
                raise RuntimeError(f"Tracked {target.key} draft is not active")
            continue
        probe = session.get(
            f"{API}/records/{target.predecessor}/draft?expand=true",
            headers=auth_modern,
            timeout=(30, 300),
        )
        if probe.status_code != 404:
            raise RuntimeError(f"Untracked active {target.key} draft exists")
        deposition = base.check(
            session.get(
                f"{API}/deposit/depositions/{target.predecessor}",
                headers=auth_legacy,
                timeout=(30, 300),
            ),
            {200},
        ).json()
        created = base.check(
            session.post(
                deposition["links"]["newversion"],
                headers=auth_legacy,
                timeout=(30, 600),
            ),
            {201},
        ).json()
        draft = base.check(
            session.get(
                created["links"]["latest_draft"],
                headers=auth_legacy,
                timeout=(30, 300),
            ),
            {200},
        ).json()
        draft_id = int(draft["id"])
        state["targets"][target.key] = {
            "status": "OPEN_TRACKED_PRIVACY_REMEDIATION_DRAFT",
            "predecessor": target.predecessor,
            "draft_id": draft_id,
            "predecessor_file_surface_sha256": file_surface_sha256(
                base.modern_entries(current)
            ),
        }
        save_state(state)
        print(f"created tracked {target.key} draft {draft_id}", flush=True)
    state["status"] = "PREPARED_TRACKED_DRAFTS"
    save_state(state)
    return state


def json_path_child(parent: str, key: object) -> str:
    if isinstance(key, int):
        return f"{parent}[{key}]"
    return f"{parent}[{json.dumps(str(key), ensure_ascii=False)}]"


def sanitize_log(source: Path, destination: Path, ledger_path: Path) -> dict:
    source_lines = source.read_text(encoding="utf-8-sig").splitlines()
    transformed_lines: list[str] = []
    ledger: list[dict[str, object]] = []
    source_ids: list[str] = []

    def record_event(
        record_number: int,
        decision_id: str,
        field_path: str,
        transform_class: str,
        original: str,
        replacement: str,
    ) -> None:
        ledger.append(
            {
                "event": len(ledger) + 1,
                "record_number": record_number,
                "decision_id": decision_id,
                "json_path": field_path,
                "transform_class": transform_class,
                "source_match_utf8_bytes": len(original.encode("utf-8")),
                "source_match_sha256": sha256_bytes(original.encode("utf-8")),
                "replacement": replacement,
            }
        )

    def transform_string(
        value: str, record_number: int, decision_id: str, field_path: str
    ) -> str:
        output = value
        for transform_class, pattern, replacement in ROOT_TRANSFORMS:
            def root_callback(match: re.Match[str]) -> str:
                record_event(
                    record_number,
                    decision_id,
                    field_path,
                    transform_class,
                    match.group(0),
                    replacement,
                )
                return replacement

            output = pattern.sub(root_callback, output)

        def codex_callback(match: re.Match[str]) -> str:
            replacement = f"{match.group('sep')}[PRIVATE_CODEX_STATE]"
            record_event(
                record_number,
                decision_id,
                field_path,
                "private_codex_state_segment",
                match.group(0),
                replacement,
            )
            return replacement

        output = CODEX_PATH_SEGMENT.sub(codex_callback, output)

        def task_callback(match: re.Match[str]) -> str:
            original = match.group(0)
            replacement = (
                "[PRIVATE_TASK_"
                + hashlib.sha256(original.lower().encode("ascii")).hexdigest()[:16].upper()
                + "]"
            )
            record_event(
                record_number,
                decision_id,
                field_path,
                "internal_task_id",
                original,
                replacement,
            )
            return replacement

        output = TASK_ID.sub(task_callback, output)

        def email_callback(match: re.Match[str]) -> str:
            replacement = "[PRIVATE_EMAIL]"
            record_event(
                record_number,
                decision_id,
                field_path,
                "private_email",
                match.group(0),
                replacement,
            )
            return replacement

        return PRIVATE_EMAIL.sub(email_callback, output)

    def transform_value(
        value: object, record_number: int, decision_id: str, field_path: str
    ) -> object:
        if isinstance(value, str):
            return transform_string(value, record_number, decision_id, field_path)
        if isinstance(value, list):
            return [
                transform_value(
                    item,
                    record_number,
                    decision_id,
                    json_path_child(field_path, index),
                )
                for index, item in enumerate(value)
            ]
        if isinstance(value, dict):
            return {
                key: transform_value(
                    item,
                    record_number,
                    decision_id,
                    json_path_child(field_path, key),
                )
                for key, item in value.items()
            }
        return value

    for index, line in enumerate(source_lines, start=1):
        value = json.loads(line)
        decision_id = str(value.get("decision_id", ""))
        if not decision_id:
            raise RuntimeError(f"Missing decision_id on source log row {index}")
        source_ids.append(decision_id)
        transformed = transform_value(value, index, decision_id, "$")
        transformed_lines.append(
            json.dumps(transformed, ensure_ascii=False, separators=(",", ":"))
        )

    if len(source_ids) != len(set(source_ids)):
        raise RuntimeError("Source decision log has duplicate decision IDs")
    if source_ids.count(REMEDIATION_DECISION_ID) != 1:
        raise RuntimeError("Remediation decision is not bound exactly once in source log")
    if source_ids.count(COUNT_CORRECTION_ID) != 1:
        raise RuntimeError("Count correction is not bound exactly once in source log")
    if source_ids.count(RESIDUAL_REMEDIATION_DECISION_ID) != 1:
        raise RuntimeError("Residual-ID remediation is not bound exactly once in source log")

    output_text = "\n".join(transformed_lines) + "\n"
    if (
        RESIDUAL_USER_HOME.search(output_text)
        or TASK_ID.search(output_text)
        or PRIVATE_EMAIL.search(output_text)
        or CODEX_PATH_SEGMENT.search(output_text)
        or HARDCODED_SECRET.search(output_text)
    ):
        raise RuntimeError("Privacy-clean log has a residual private token")
    destination.write_text(output_text, encoding="utf-8", newline="\n")

    fields = [
        "event",
        "record_number",
        "decision_id",
        "json_path",
        "transform_class",
        "source_match_utf8_bytes",
        "source_match_sha256",
        "replacement",
    ]
    with ledger_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(ledger)

    public_lines = destination.read_text(encoding="utf-8").splitlines()
    public_values = [json.loads(line) for line in public_lines]
    public_ids = [str(value.get("decision_id", "")) for value in public_values]
    if public_ids != source_ids:
        raise RuntimeError("Privacy projection changed decision ID order or membership")
    counts: dict[str, int] = {}
    for row in ledger:
        key = str(row["transform_class"])
        counts[key] = counts.get(key, 0) + 1
    return {
        "source_records": len(source_ids),
        "public_records": len(public_ids),
        "decision_ids_exact_order_match": True,
        "transformation_events": len(ledger),
        "transformation_classes": counts,
        "residual_private_tokens": 0,
        "source_bytes": source.stat().st_size,
        "source_sha256": sha256_path(source),
        "public_bytes": destination.stat().st_size,
        "public_sha256": sha256_path(destination),
        "ledger_bytes": ledger_path.stat().st_size,
        "ledger_sha256": sha256_path(ledger_path),
    }


def build_outputs(state: dict) -> tuple[dict[str, dict[str, object]], list[dict[str, object]]]:
    TEMP.mkdir(parents=True, exist_ok=True)
    raw_log = CONTROL_ROOT / RAW_LOG_NAME
    clean_log = TEMP / CLEAN_LOG_NAME
    ledger = TEMP / LEDGER_NAME
    validation_path = TEMP / VALIDATION_NAME
    note_path = TEMP / NOTE_NAME
    manifest_path = TEMP / MANIFEST_NAME
    zip_path = TEMP / ZIP_NAME
    decision_path = CONTROL_ROOT / RESIDUAL_REMEDIATION_DECISION_NAME
    if not decision_path.is_file():
        raise RuntimeError("Residual-ID remediation decision record is missing")

    report = sanitize_log(raw_log, clean_log, ledger)
    validation = {
        "schema": "english-germanic-decision-log-public-privacy-projection-v2",
        "status": "PASS",
        "errors": [],
        "source_custody": {
            "state": "immutable private append-only source; not redistributed on current public heads",
            "records": report["source_records"],
            "bytes": report["source_bytes"],
            "sha256": report["source_sha256"],
        },
        "public_projection": {
            "file": CLEAN_LOG_NAME,
            "records": report["public_records"],
            "bytes": report["public_bytes"],
            "sha256": report["public_sha256"],
            "decision_ids_exact_order_match": True,
            "records_omitted": 0,
            "transformation_events": report["transformation_events"],
            "transformation_classes": report["transformation_classes"],
            "residual_private_tokens": 0,
        },
        "transformation_ledger": {
            "file": LEDGER_NAME,
            "bytes": report["ledger_bytes"],
            "sha256": report["ledger_sha256"],
            "one_row_per_replacement_event": True,
            "source_tokens_bound_by_hash_not_disclosed": True,
        },
        "privacy_transforms_only": True,
        "production_content_changed": False,
        "reader_bytes_changed": False,
        "superseded_adverse_records": [target.predecessor for target in TARGETS],
        "target_drafts": {
            target.key: int(state["targets"][target.key]["draft_id"])
            for target in TARGETS
        },
    }
    base.save_json(validation_path, validation)

    note = f"""# English/Germanic decision-log privacy remediation v2

## Scope

Methodology record `21779952` and replication record `21779957` corrected the
earlier verbatim-log path disclosures, but an independent UUID-shape scan found
nine internal task identifiers still present across six historical finding
fields.  The v1 matcher required a leading word boundary; the missed UUIDs were
concatenated directly after prose such as `thread` or `task`.  Both v1 records,
and their earlier raw-log predecessors `21778949` and `21778962`, remain
immutable adverse history.

This successor preserves all {report['source_records']} decision records in
their exact order and omits none.  It replaces only private path roots, private
state-directory segments, the private project email, and every complete
internal task-ID shape even when adjacent to prose.
Task IDs receive stable SHA-256-derived pseudonyms so repeated references remain
linkable without exposing the source identifiers.  The event ledger binds every
source token by length and SHA-256 without repeating the private token.

## Exact projection

- Private source custody: {report['source_records']} records / {report['source_bytes']} bytes /
  SHA-256 `{report['source_sha256']}`; not redistributed on the current heads.
- Public projection: `{CLEAN_LOG_NAME}` — {report['public_records']} records /
  {report['public_bytes']} bytes / SHA-256 `{report['public_sha256']}`.
- Transformation ledger: `{LEDGER_NAME}` — {report['transformation_events']} events /
  {report['ledger_bytes']} bytes / SHA-256 `{report['ledger_sha256']}`.
- Validation: `{VALIDATION_NAME}` — PASS; records omitted 0; residual private
  tokens 0; reader/production content changes 0.
- Methodology successor record: `{state['targets']['methodology']['draft_id']}`
  under existing concept `10.5281/zenodo.21124403`.
- Replication successor record: `{state['targets']['replication']['draft_id']}`
  under existing concept `10.5281/zenodo.20461174`.

The controlling 2,296-byte dual-DOI requirement remains byte-exact in the
provenance ZIP as an explicitly mandated three-identifier exception.  The v1
false residual-closure claim is preserved by predecessor identity and by the
new append-only remediation decision.  No SGA reader, TeX, translation,
mathematical statement, source decision, error, reversal, or continuation
record is changed or curated away.
"""
    note_path.write_text(note, encoding="utf-8", newline="\n")

    inputs: list[tuple[str, Path, str, str]] = [
        (
            "controls/LOGBOOK_PRIVACY_CLEAN.md",
            SOURCE_ROOT / "controls/LOGBOOK_PRIVACY_CLEAN.md",
            "privacy-clean producer logbook",
            "current SGA producer decision surface",
        ),
        (
            "controls/DECISION_LOG.csv",
            SOURCE_ROOT / "controls/DECISION_LOG.csv",
            "producer decision ledger",
            "current SGA producer decision surface",
        ),
        (
            "controls/REVISION_HISTORY.csv",
            SOURCE_ROOT / "controls/REVISION_HISTORY.csv",
            "producer revision/reversal history",
            "current SGA producer decision surface",
        ),
        (
            f"controls/{CONTROL_NAME}",
            CONTROL_ROOT / CONTROL_NAME,
            "controlling dual-DOI provenance requirement",
            "authoritative exact public control; explicit identifier exception",
        ),
        (
            f"archive/{CLEAN_LOG_NAME}",
            clean_log,
            "privacy-clean append-only English/Germanic decision log",
            "current public projection; raw predecessor retained as adverse history",
        ),
        (
            f"archive/{LEDGER_NAME}",
            ledger,
            "event-level privacy transformation ledger",
            "current public projection control",
        ),
        (
            f"archive/{VALIDATION_NAME}",
            validation_path,
            "privacy projection validation",
            "current public projection control",
        ),
        (
            f"archive/{NOTE_NAME}",
            note_path,
            "human-readable privacy remediation and adverse-history note",
            "current public projection control",
        ),
    ]
    for name in PRIOR_DECISION_FILES + (
        REMEDIATION_DECISION_NAME,
        COUNT_CORRECTION_NAME,
        RESIDUAL_REMEDIATION_DECISION_NAME,
    ):
        inputs.append(
            (
                f"archive/{name}",
                CONTROL_ROOT / name,
                "archive decision/error/reversal record",
                "bound in privacy-clean append-only log",
            )
        )
    control_path = CONTROL_ROOT / CONTROL_NAME
    if control_path.stat().st_size != 2_296 or sha256_path(control_path) != CONTROL_SHA256:
        raise RuntimeError("Authoritative dual-DOI control identity changed")

    rows: list[dict[str, object]] = []
    for member, path, role, supersession in inputs:
        if not path.is_file():
            raise RuntimeError(f"Missing provenance member: {member}")
        rows.append(
            {
                "member_path": member,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
                "role": role,
                "privacy_result": (
                    "PASS exact mandated public control"
                    if member == f"controls/{CONTROL_NAME}"
                    else "PASS privacy-clean public projection"
                ),
                "supersession_state": supersession,
                "source_path": path,
            }
        )

    fields = [
        "member_path",
        "bytes",
        "sha256",
        "role",
        "privacy_result",
        "supersession_state",
        "methodology_concept_doi",
        "replication_concept_doi",
    ]
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {key: row[key] for key in fields if key in row}
                | {
                    "methodology_concept_doi": TARGETS[0].concept_doi,
                    "replication_concept_doi": TARGETS[1].concept_doi,
                }
            )

    public_rows = [{key: value for key, value in row.items() if key != "source_path"} for row in rows]
    public_rows.append(
        {
            "member_path": "MANIFEST.csv",
            "bytes": manifest_path.stat().st_size,
            "sha256": sha256_path(manifest_path),
            "role": "self-excluding direct member manifest",
            "privacy_result": "PASS",
            "supersession_state": "current privacy-remediation manifest",
        }
    )
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for row in rows:
            info = zipfile.ZipInfo(str(row["member_path"]), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, Path(row["source_path"]).read_bytes(), compresslevel=9)
        info = zipfile.ZipInfo("MANIFEST.csv", date_time=(1980, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, manifest_path.read_bytes(), compresslevel=9)
    with zipfile.ZipFile(zip_path) as archive:
        if archive.namelist() != [str(row["member_path"]) for row in public_rows]:
            raise RuntimeError("Provenance ZIP member order changed")
        for row in public_rows:
            payload = archive.read(str(row["member_path"]))
            if (len(payload), sha256_bytes(payload)) != (int(row["bytes"]), str(row["sha256"])):
                raise RuntimeError(f"Provenance ZIP member mismatch: {row['member_path']}")

    uploads = {
        ZIP_NAME: file_row(zip_path),
        MANIFEST_NAME: file_row(manifest_path),
        CLEAN_LOG_NAME: file_row(clean_log),
        LEDGER_NAME: file_row(ledger),
    }
    return uploads, public_rows


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
    print(f"upload {name} ({path.stat().st_size} bytes)", flush=True)
    with path.open("rb") as handle:
        base.check(
            session.put(
                f"{bucket.rstrip('/')}/{urllib.parse.quote(name, safe='')}",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/octet-stream",
                },
                data=handle,
                timeout=(30, 1800),
            ),
            {200, 201},
        )


def stream_readback(session, url: str) -> tuple[int, str]:
    response = base.check(session.get(url, stream=True, timeout=(30, 1800)), {200})
    digest = hashlib.sha256()
    total = 0
    with response:
        for block in response.iter_content(4 * 1024 * 1024):
            if block:
                digest.update(block)
                total += len(block)
    return total, digest.hexdigest().upper()


def publish_target(
    session,
    token: str,
    target: Target,
    uploads: dict[str, dict[str, object]],
    zip_rows: list[dict[str, object]],
    state: dict,
) -> dict:
    auth_legacy = {"Authorization": f"Bearer {token}"}
    auth_modern = {**MODERN, "Authorization": f"Bearer {token}"}
    current, current_entries = current_guard(session, target)
    tracked = state["targets"].get(target.key, {})
    draft_id = int(tracked.get("draft_id", 0))
    if not draft_id:
        raise RuntimeError(f"No tracked {target.key} draft")
    if tracked.get("published_record"):
        record_id = int(tracked["published_record"])
    else:
        draft_probe = base.check(
            session.get(
                f"{API}/records/{draft_id}/draft?expand=true",
                headers=auth_modern,
                timeout=(30, 300),
            ),
            {200},
        ).json()
        if int(draft_probe["id"]) != draft_id:
            raise RuntimeError(f"Tracked {target.key} draft changed")
        deposition = base.check(
            session.get(
                f"{API}/deposit/depositions/{draft_id}",
                headers=auth_legacy,
                timeout=(30, 300),
            ),
            {200},
        ).json()
        staged = base.legacy_entries(deposition)
        remove_names = PREDECESSOR_REPLACE_NAMES | STALE_ATTEMPT_NAMES
        for name in sorted(remove_names | set(uploads), key=str.casefold):
            if name in staged:
                wanted = uploads.get(name)
                observed = (
                    int(staged[name]["filesize"]),
                    base.normalized_md5(staged[name]["checksum"]),
                )
                if wanted and observed == (int(wanted["bytes"]), str(wanted["md5"])):
                    continue
                base.check(
                    session.delete(
                        staged[name]["links"]["self"],
                        headers=auth_legacy,
                        timeout=(30, 300),
                    ),
                    {204},
                )
        deposition = base.check(
            session.get(
                f"{API}/deposit/depositions/{draft_id}",
                headers=auth_legacy,
                timeout=(30, 300),
            ),
            {200},
        ).json()
        staged = base.legacy_entries(deposition)
        for name, row in uploads.items():
            if name in staged:
                continue
            upload_file(session, token, deposition["links"]["bucket"], name, Path(row["path"]))

        draft = base.check(
            session.get(
                f"{API}/records/{draft_id}/draft?expand=true",
                headers=auth_modern,
                timeout=(30, 300),
            ),
            {200},
        ).json()
        entries = base.modern_entries(draft)
        desired = (set(current_entries) - remove_names) | set(uploads)
        if set(entries) != desired or PREDECESSOR_REPLACE_NAMES & set(entries):
            raise RuntimeError(f"{target.key} staged privacy boundary changed")
        for name, row in uploads.items():
            if identity(entries[name]) != (int(row["bytes"]), str(row["md5"])):
                raise RuntimeError(f"{target.key} staged upload changed: {name}")
        for name in desired - set(uploads):
            if identity(entries[name]) != identity(current_entries[name]):
                raise RuntimeError(f"{target.key} retained file changed: {name}")

        metadata = copy.deepcopy(current["metadata"])
        metadata["publication_date"] = "2026-08-03"
        metadata["version"] = target.version
        prior_description = str(current["metadata"]["description"])
        if prior_description.startswith(
            "<p><strong>Current privacy-remediated audit surface.</strong>"
        ):
            _old_prefix, separator, remainder = prior_description.partition("</p>")
            if not separator:
                raise RuntimeError(f"{target.key} predecessor description prefix changed")
            prior_description = remainder
        privacy_prefix = (
            "<p><strong>Current privacy-remediated audit surface v2.</strong> "
            f"Predecessor record {target.predecessor} removed historical private paths but its "
            "v1 projection missed nine UUID-shaped internal task identifiers because they were "
            "concatenated directly after prose. This version uses a complete UUID-shape matcher "
            "and publishes the corrected projection, event-level transformation ledger, "
            "validation, and append-only adverse-history decision while retaining every "
            "decision, error, reversal, and continuation in exact order. Earlier raw-log and "
            "v1 records remain immutable adverse history. "
            "No reader, translation, TeX, mathematical, or production bytes changed. The "
            "dedicated FAC quality-assessment concept remains "
            "<a href=\"https://doi.org/10.5281/zenodo.21779392\">10.5281/zenodo.21779392</a> "
            "(version <a href=\"https://doi.org/10.5281/zenodo.21779393\">"
            "10.5281/zenodo.21779393</a>); its payload is not duplicated here, and GAGA "
            "remains separate.</p>"
        )
        metadata["description"] = privacy_prefix + prior_description
        metadata.pop("additional_descriptions", None)
        predecessor_order = list(current["files"].get("order") or [])
        retained_order = [name for name in predecessor_order if name not in remove_names]
        payload = {
            "access": current["access"],
            "files": {
                "enabled": True,
                "default_preview": current["files"].get("default_preview"),
                "order": retained_order,
            },
            "metadata": metadata,
            "custom_fields": current.get("custom_fields", {}),
        }
        if draft.get("pids"):
            payload["pids"] = draft["pids"]
        patched = base.check(
            session.put(
                f"{API}/records/{draft_id}/draft",
                headers={**auth_modern, "Content-Type": "application/json"},
                json=payload,
                timeout=(30, 600),
            ),
            {200},
        ).json()
        if (
            set(base.modern_entries(patched)) != desired
            or patched["files"].get("default_preview")
            != current["files"].get("default_preview")
            or patched["files"].get("order") != retained_order
            or "Current privacy-remediated audit surface v2" not in patched["metadata"]["description"]
        ):
            raise RuntimeError(f"{target.key} staged presentation changed")
        published = base.check(
            session.post(
                patched["links"]["publish"],
                headers=auth_modern,
                timeout=(30, 1200),
            ),
            {200, 202},
        ).json()
        record_id = int(published["id"])
        if record_id != draft_id:
            raise RuntimeError(f"{target.key} published record differs from tracked draft")
        tracked.update(
            {"status": "PUBLISHED_READBACK_PENDING", "published_record": record_id}
        )
        save_state(state)
        print(f"published {target.key} privacy-remediation record {record_id}", flush=True)

    record = None
    desired = (
        set(current_entries)
        - (PREDECESSOR_REPLACE_NAMES | STALE_ATTEMPT_NAMES)
    ) | set(uploads)
    for attempt in range(90):
        response = session.get(
            f"{API}/records/{record_id}?expand=true", headers=MODERN, timeout=(30, 300)
        )
        if response.status_code == 200 and response.json().get("is_published"):
            candidate = response.json()
            if set(base.modern_entries(candidate)) == desired:
                record = candidate
                break
        time.sleep(min(attempt + 1, 5))
    if record is None:
        raise RuntimeError(f"{target.key} successor did not become publicly readable")
    entries = base.modern_entries(record)
    readback = {}
    for name, row in uploads.items():
        observed = stream_readback(session, entries[name]["links"]["content"])
        wanted = int(row["bytes"]), str(row["sha256"])
        readback[name] = {
            "bytes": observed[0],
            "sha256": observed[1],
            "match": observed == wanted,
            "content_url": entries[name]["links"]["content"],
        }
        if observed != wanted:
            raise RuntimeError(f"{target.key} public readback changed: {name}")
    response = base.check(
        session.get(entries[ZIP_NAME]["links"]["content"], timeout=(30, 600)), {200}
    )
    with zipfile.ZipFile(io.BytesIO(response.content)) as archive:
        observed_rows = []
        for name in archive.namelist():
            payload = archive.read(name)
            observed_rows.append(
                {
                    "member_path": name,
                    "bytes": len(payload),
                    "sha256": sha256_bytes(payload),
                }
            )
    expected_rows = [
        {
            "member_path": str(row["member_path"]),
            "bytes": int(row["bytes"]),
            "sha256": str(row["sha256"]),
        }
        for row in zip_rows
    ]
    if observed_rows != expected_rows:
        raise RuntimeError(f"{target.key} ZIP member public readback changed")
    retained = set(entries) - set(uploads)
    predecessor_retained = set(current_entries) - PREDECESSOR_REPLACE_NAMES
    if retained != predecessor_retained:
        raise RuntimeError(f"{target.key} retained public boundary changed")
    retained_mismatches = [
        name for name in retained if identity(entries[name]) != identity(current_entries[name])
    ]
    latest = base.check(
        session.get(record["links"]["latest"], headers=MODERN, timeout=(30, 300)), {200}
    ).json()
    draft_probe = session.get(
        f"{API}/records/{record_id}/draft", headers=auth_modern, timeout=(30, 300)
    )
    if (
        retained_mismatches
        or int(latest["id"]) != record_id
        or draft_probe.status_code != 404
        or PREDECESSOR_REPLACE_NAMES & set(entries)
    ):
        raise RuntimeError(f"{target.key} closeout guard changed")
    result = {
        "status": "PASS_PRIVACY_REMEDIATED_LOG_V2_PUBLISHED_AND_PUBLIC_READBACK",
        "target": target.key,
        "record_id": record_id,
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": target.concept_doi,
        "predecessor_record": target.predecessor,
        "files": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "default_preview_unchanged": True,
        "lexical_file_order_front": sorted(entries, key=str.casefold)[:8],
        "raw_predecessor_log_present_on_current": False,
        "v1_predecessor_projection_present_on_current": False,
        "retained_predecessor_files": len(retained),
        "retained_identity_mismatches": retained_mismatches,
        "file_surface_sha256": file_surface_sha256(entries),
        "raw_public_readback": readback,
        "zip_member_readback": observed_rows,
        "active_draft": False,
        "duplicate_concept": False,
        "fac_payload_files_added": 0,
        "gaga_payload_files_added": 0,
    }
    receipt = REPO / "manifests/published-zenodo" / (
        f"20260803_english_germanic_log_privacy_remediation_v2_{target.key}_record_"
        f"{record_id}_public_readback.json"
    )
    base.save_json(receipt, result)
    tracked.update(
        {
            "status": "CLOSED_PUBLIC_READBACK_PASS",
            "receipt": receipt.relative_to(REPO).as_posix(),
        }
    )
    save_state(state)
    return result


def mirror_outputs(uploads: dict[str, dict[str, object]]) -> None:
    archive_dir = SOURCE_ROOT / "archive"
    archive_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(Path(uploads[ZIP_NAME]["path"]), SOURCE_ROOT / ZIP_NAME)
    shutil.copyfile(Path(uploads[MANIFEST_NAME]["path"]), SOURCE_ROOT / MANIFEST_NAME)
    for name in (CLEAN_LOG_NAME, LEDGER_NAME):
        shutil.copyfile(Path(uploads[name]["path"]), archive_dir / name)
    for name in (VALIDATION_NAME, NOTE_NAME):
        shutil.copyfile(TEMP / name, archive_dir / name)
    for name in (
        REMEDIATION_DECISION_NAME,
        COUNT_CORRECTION_NAME,
        RESIDUAL_REMEDIATION_DECISION_NAME,
    ):
        shutil.copyfile(CONTROL_ROOT / name, archive_dir / name)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("prepare", "publish"))
    args = parser.parse_args()
    session = base.make_session()
    token = base.find_token()
    state = load_state()
    if args.action == "prepare":
        result = prepare_drafts(session, token, state)
        print(json.dumps(result, indent=2), flush=True)
        return
    if state.get("status") != "PREPARED_TRACKED_DRAFTS":
        raise RuntimeError("Run prepare and append the exact remediation decision first")
    uploads, zip_rows = build_outputs(state)
    results = [
        publish_target(session, token, target, uploads, zip_rows, state)
        for target in TARGETS
    ]
    mirror_outputs(uploads)
    state["status"] = "CLOSED_BOTH_PUBLIC_READBACK_PASS"
    save_state(state)
    print(json.dumps({"status": state["status"], "results": results}, indent=2), flush=True)


if __name__ == "__main__":
    main()
