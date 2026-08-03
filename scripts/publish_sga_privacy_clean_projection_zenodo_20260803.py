#!/usr/bin/env python3
"""Derive and publish an SGA package with private build paths removed."""

from __future__ import annotations

import copy
import csv
import hashlib
import json
import os
import re
import shutil
import time
import urllib.parse
import zipfile
from pathlib import Path, PurePosixPath

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
REPO = Path(__file__).resolve().parents[1]
SOURCE_ROOT = Path(os.environ["SGA_PRESENTATION_CLEAN_SOURCE_ROOT"]).resolve()
CONTROL_PATH = Path(os.environ["SGA_DUAL_DOI_CONTROL_PATH"]).resolve()
TEMP = REPO / "tmp/zenodo/sga-presentation-clean-privacy-remediation-20260803"
OUTPUT_ROOT = TEMP / "privacy-clean-public-projection"
OUTPUT_ZIP = TEMP / (
    "00_Current_SGA1-7II_English_Presentation_Clean_Readers_and_"
    "Buildable_Source_20260803.zip"
)
ZIP_VALIDATION = TEMP / (
    "SGA_English_1_7II_presentation_clean_checkpoint_20260803_r2_"
    "COMPLETE_ZIP_VALIDATION.json"
)
STATE = TEMP / "state.json"
CURRENT_RECORD = 21_778_605
CURRENT_FILES = 33
CURRENT_BYTES = 178_234_035
CONCEPT_DOI = "10.5281/zenodo.20410947"
DEFAULT_PREVIEW = "00_SGA_1-7II_English_Global_Reader.pdf"
PRIMARY_ZIP = OUTPUT_ZIP.name
CONTROL_REL = "controls/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
CONTROL_BYTES = 2_296
CONTROL_SHA256 = "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679"
TRANSFORM_LEDGER = "ARCHIVE_PRIVACY_TRANSFORMATIONS.csv"
PACKAGE_CONTROLS = {
    "PACKAGE_PREMANIFEST_VALIDATION.json",
    "PACKAGE_PAYLOAD_MANIFEST.csv",
    "PACKAGE_MANIFEST_VALIDATION.json",
}
TEXT_SUFFIXES = {
    ".csv", ".json", ".md", ".ps1", ".py", ".sty", ".tex", ".txt", ".xml", ".yaml", ".yml"
}
PRIVATE_WINDOWS = re.compile(r"(?i)[A-Z]:\\+Users\\+[^\\/\r\n\"']+")
PRIVATE_POSIX = re.compile(r"(?i)/Users/[^/\s\"']+")
PRIVATE_NAME = re.compile(r"(?i)\bFloris\b")


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


def identity(entry: dict) -> tuple[int, str]:
    return int(entry["size"]), base.normalized_md5(entry["checksum"])


def file_row(path: Path) -> dict[str, object]:
    return {
        "path": path,
        "bytes": path.stat().st_size,
        "sha256": sha256_path(path),
        "md5": md5_path(path),
    }


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def save_json(path: Path, value: object) -> None:
    base.save_json(path, value)


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def privacy_hits(data: bytes) -> list[str]:
    text = data.decode("utf-8", errors="ignore")
    hits = []
    if PRIVATE_WINDOWS.search(text):
        hits.append("absolute_windows_user_path")
    if PRIVATE_POSIX.search(text):
        hits.append("absolute_posix_user_path")
    if PRIVATE_NAME.search(text):
        hits.append("private_operator_name")
    return hits


def transform_text(relative: str, data: bytes) -> tuple[bytes, int, list[str]]:
    if relative == CONTROL_REL:
        if len(data) != CONTROL_BYTES or hashlib.sha256(data).hexdigest().upper() != CONTROL_SHA256:
            raise RuntimeError("Authoritative public control identity changed")
        return data, 0, ["authorized_exact_public_control"]
    text = data.decode("utf-8")
    rules: list[str] = []
    count = 0
    text, changed = PRIVATE_WINDOWS.subn("PRIVATE_HOME", text)
    if changed:
        rules.append("absolute_windows_user_path_to_PRIVATE_HOME")
        count += changed
    text, changed = PRIVATE_POSIX.subn("PRIVATE_HOME", text)
    if changed:
        rules.append("absolute_posix_user_path_to_PRIVATE_HOME")
        count += changed
    text, changed = PRIVATE_NAME.subn("PRIVATE_OPERATOR", text)
    if changed:
        rules.append("private_operator_name_to_PRIVATE_OPERATOR")
        count += changed
    return text.encode("utf-8"), count, rules


def validate_source_zip_members(root: Path) -> dict[str, object]:
    hits: list[dict[str, str]] = []
    members = 0
    zips = sorted(path for path in root.glob("10*.zip") if path.is_file())
    for path in zips:
        with zipfile.ZipFile(path) as archive:
            for info in archive.infolist():
                if info.is_dir():
                    continue
                members += 1
                if not safe_member(info.filename):
                    hits.append({"zip": path.name, "member": info.filename, "hit": "unsafe_member_path"})
                    continue
                if Path(info.filename).suffix.lower() in TEXT_SUFFIXES:
                    for hit in privacy_hits(archive.read(info)):
                        hits.append({"zip": path.name, "member": info.filename, "hit": hit})
    return {"zips": len(zips), "members": members, "hits": hits}


def transform_source_zips(root: Path, ledger: list[dict[str, object]]) -> list[str]:
    transformed_zips: list[str] = []
    for path in sorted(item for item in root.glob("10*.zip") if item.is_file()):
        member_changes: list[dict[str, object]] = []
        temp = path.with_name(path.name + ".privacy-clean.tmp")
        with zipfile.ZipFile(path) as source:
            for info in source.infolist():
                if info.is_dir() or Path(info.filename).suffix.lower() not in TEXT_SUFFIXES:
                    continue
                original = source.read(info)
                if not privacy_hits(original):
                    continue
                transformed, replacements, rules = transform_text(
                    f"{path.name}!/{info.filename}", original
                )
                if privacy_hits(transformed):
                    raise RuntimeError(f"ZIP member privacy residual: {path.name}!/{info.filename}")
                member_changes.append(
                    {
                        "relative_path": f"{path.name}!/{info.filename}",
                        "source_bytes": len(original),
                        "source_sha256": hashlib.sha256(original).hexdigest().upper(),
                        "public_bytes": len(transformed),
                        "public_sha256": hashlib.sha256(transformed).hexdigest().upper(),
                        "replacement_count": replacements,
                        "rules": ";".join(rules),
                        "source_preserved": "unchanged in private producer custody and record 21778605 history",
                    }
                )
        if not member_changes:
            continue
        original_zip = file_row(path)
        replacements = {row["relative_path"].split("!/", 1)[1]: row for row in member_changes}
        with zipfile.ZipFile(path) as source, zipfile.ZipFile(temp, "w") as target:
            for info in source.infolist():
                data = source.read(info) if not info.is_dir() else b""
                if info.filename in replacements:
                    data, _, _ = transform_text(f"{path.name}!/{info.filename}", data)
                copied = copy.copy(info)
                target.writestr(copied, data)
        temp.replace(path)
        public_zip = file_row(path)
        ledger.extend(member_changes)
        ledger.append(
            {
                "relative_path": path.name,
                "source_bytes": original_zip["bytes"],
                "source_sha256": original_zip["sha256"],
                "public_bytes": public_zip["bytes"],
                "public_sha256": public_zip["sha256"],
                "replacement_count": sum(int(row["replacement_count"]) for row in member_changes),
                "rules": "privacy-clean member projection; all other ZIP members byte-identical",
                "source_preserved": "unchanged in private producer custody and record 21778605 history",
            }
        )
        transformed_zips.append(path.name)
    return transformed_zips


def build_projection() -> dict[str, object]:
    source_files = sorted(path for path in SOURCE_ROOT.rglob("*") if path.is_file())
    if len(source_files) != 125 or sum(path.stat().st_size for path in source_files) != 99_112_600:
        raise RuntimeError("Producer source snapshot boundary changed")
    source_zip_validation = validate_source_zip_members(SOURCE_ROOT)
    if OUTPUT_ROOT.exists():
        if not OUTPUT_ROOT.resolve().is_relative_to(TEMP.resolve()):
            raise RuntimeError("Unsafe derived projection cleanup target")
        shutil.rmtree(OUTPUT_ROOT)
    shutil.copytree(SOURCE_ROOT, OUTPUT_ROOT)
    ledger: list[dict[str, object]] = []
    json_count = 0
    csv_count = 0
    csv_nonrectangular: list[str] = []
    for source in source_files:
        relative = source.relative_to(SOURCE_ROOT).as_posix()
        if relative in PACKAGE_CONTROLS:
            continue
        target = OUTPUT_ROOT / Path(relative)
        original = target.read_bytes()
        if target.suffix.lower() in TEXT_SUFFIXES:
            transformed, replacements, rules = transform_text(relative, original)
            if transformed != original:
                target.write_bytes(transformed)
                ledger.append(
                    {
                        "relative_path": relative,
                        "source_bytes": len(original),
                        "source_sha256": hashlib.sha256(original).hexdigest().upper(),
                        "public_bytes": len(transformed),
                        "public_sha256": hashlib.sha256(transformed).hexdigest().upper(),
                        "replacement_count": replacements,
                        "rules": ";".join(rules),
                        "source_preserved": "unchanged in private producer custody and record 21778605 history",
                    }
                )
            if target.suffix.lower() == ".json":
                load_json(target)
                json_count += 1
            elif target.suffix.lower() == ".csv":
                with target.open("r", encoding="utf-8-sig", newline="") as handle:
                    rows = list(csv.reader(handle))
                if rows and any(len(row) != len(rows[0]) for row in rows):
                    csv_nonrectangular.append(relative)
                csv_count += 1
    transformed_source_zips = transform_source_zips(OUTPUT_ROOT, ledger)
    public_zip_validation = validate_source_zip_members(OUTPUT_ROOT)
    if public_zip_validation["hits"]:
        raise RuntimeError("Derived source ZIP member privacy scan failed")
    ledger_path = OUTPUT_ROOT / TRANSFORM_LEDGER
    with ledger_path.open("w", encoding="utf-8", newline="") as handle:
        fields = [
            "relative_path", "source_bytes", "source_sha256", "public_bytes", "public_sha256",
            "replacement_count", "rules", "source_preserved"
        ]
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(ledger)
    residuals: list[dict[str, object]] = []
    authorized_control_mentions = 0
    for path in sorted(item for item in OUTPUT_ROOT.rglob("*") if item.is_file()):
        relative = path.relative_to(OUTPUT_ROOT).as_posix()
        if relative in PACKAGE_CONTROLS:
            continue
        hits = privacy_hits(path.read_bytes())
        if relative == CONTROL_REL:
            authorized_control_mentions = len(hits)
            continue
        if hits:
            residuals.append({"relative_path": relative, "hits": hits})
    if residuals:
        raise RuntimeError(f"Derived projection privacy residuals: {residuals[:10]}")
    unchanged_public_artifacts = []
    transformed_public_artifacts = []
    for path in sorted(SOURCE_ROOT.iterdir(), key=lambda item: item.name.casefold()):
        if not path.is_file() or path.name in PACKAGE_CONTROLS:
            continue
        derived = OUTPUT_ROOT / path.name
        if derived.read_bytes() == path.read_bytes():
            unchanged_public_artifacts.append(
                {"name": path.name, "bytes": path.stat().st_size, "sha256": sha256_path(path)}
            )
        elif path.name in transformed_source_zips:
            transformed_public_artifacts.append(
                {
                    "name": path.name,
                    "source_bytes": path.stat().st_size,
                    "source_sha256": sha256_path(path),
                    "public_bytes": derived.stat().st_size,
                    "public_sha256": sha256_path(derived),
                    "scope": "private operator labels in TeX comments only",
                }
            )
        else:
            raise RuntimeError(f"Untracked substantive top-level change: {path.name}")
    premanifest = {
        "schema": "sga-presentation-clean-archive-privacy-projection-v1",
        "status": "PASS",
        "errors": [],
        "source_snapshot": {
            "files": 125,
            "bytes": 99_112_600,
            "custody": "unchanged private producer source and immutable record 21778605 history",
        },
        "public_projection": {
            "transformed_files": len(ledger),
            "replacement_events": sum(int(row["replacement_count"]) for row in ledger),
            "privacy_residuals": residuals,
            "authorized_control_identity": {
                "relative_path": CONTROL_REL,
                "bytes": CONTROL_BYTES,
                "sha256": CONTROL_SHA256,
                "explicitly_required_public_identity": True,
                "privacy_pattern_classes_present": authorized_control_mentions,
            },
            "substantive_top_level_artifacts_unchanged": unchanged_public_artifacts,
            "privacy_transformed_source_zips": transformed_public_artifacts,
            "json_files_parsed": json_count,
            "csv_files_parsed": csv_count,
            "source_inherited_nonrectangular_csvs": csv_nonrectangular,
            "source_zip_member_scan_before": source_zip_validation,
            "source_zip_member_scan_after": public_zip_validation,
            "render_or_rebuild_performed": False,
        },
    }
    save_json(OUTPUT_ROOT / "PACKAGE_PREMANIFEST_VALIDATION.json", premanifest)
    manifest_path = OUTPUT_ROOT / "PACKAGE_PAYLOAD_MANIFEST.csv"
    validation_path = OUTPUT_ROOT / "PACKAGE_MANIFEST_VALIDATION.json"
    manifest_rows = []
    excluded = {manifest_path.resolve(), validation_path.resolve()}
    for path in sorted(
        (item for item in OUTPUT_ROOT.rglob("*") if item.is_file() and item.resolve() not in excluded),
        key=lambda item: item.relative_to(OUTPUT_ROOT).as_posix(),
    ):
        manifest_rows.append(
            {
                "file_id": f"SGA-PC-{len(manifest_rows) + 1:04d}",
                "relative_path": path.relative_to(OUTPUT_ROOT).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
                "manifest_scope": "archive-derived privacy-clean public projection",
            }
        )
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["file_id", "relative_path", "bytes", "sha256", "manifest_scope"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(manifest_rows)
    manifest_validation = {
        "schema": "sga-presentation-clean-archive-manifest-validation-v1",
        "status": "PASS",
        "errors": [],
        "manifest": {
            "path": manifest_path.name,
            "bytes": manifest_path.stat().st_size,
            "sha256": sha256_path(manifest_path),
            "rows": len(manifest_rows),
            "self_excluding": True,
            "excluded_files": [manifest_path.name, validation_path.name],
        },
        "replay": {"rows_checked": len(manifest_rows), "byte_mismatches": 0, "hash_mismatches": 0},
    }
    save_json(validation_path, manifest_validation)
    for row in manifest_rows:
        path = OUTPUT_ROOT / Path(str(row["relative_path"]))
        if path.stat().st_size != int(row["bytes"]) or sha256_path(path) != row["sha256"]:
            raise RuntimeError(f"Derived manifest replay changed: {row['relative_path']}")
    files = sorted(
        (item for item in OUTPUT_ROOT.rglob("*") if item.is_file()),
        key=lambda item: item.relative_to(OUTPUT_ROOT).as_posix(),
    )
    if OUTPUT_ZIP.exists():
        OUTPUT_ZIP.unlink()
    with zipfile.ZipFile(OUTPUT_ZIP, "w", compression=zipfile.ZIP_STORED) as archive:
        for path in files:
            relative = path.relative_to(OUTPUT_ROOT).as_posix()
            info = zipfile.ZipInfo(relative, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    with zipfile.ZipFile(OUTPUT_ZIP) as archive:
        if archive.namelist() != [path.relative_to(OUTPUT_ROOT).as_posix() for path in files]:
            raise RuntimeError("Derived complete ZIP member order changed")
        for path in files:
            relative = path.relative_to(OUTPUT_ROOT).as_posix()
            payload = archive.read(relative)
            if payload != path.read_bytes():
                raise RuntimeError(f"Derived complete ZIP member replay changed: {relative}")
    zip_validation = {
        "schema": "sga-presentation-clean-archive-complete-zip-validation-v1",
        "status": "PASS",
        "errors": [],
        "zip": {
            "name": OUTPUT_ZIP.name,
            "bytes": OUTPUT_ZIP.stat().st_size,
            "sha256": sha256_path(OUTPUT_ZIP),
            "members": len(files),
        },
        "replay": {"members_checked": len(files), "missing": 0, "byte_mismatches": 0, "hash_mismatches": 0},
        "privacy": {
            "transformed_files": len(ledger),
            "residual_private_path_or_operator_hits": 0,
            "authoritative_control_exception": CONTROL_REL,
        },
        "supersession": {
            "supersedes_record": CURRENT_RECORD,
            "reason": "remove absolute private build paths and private operator labels from public audit controls",
            "source_bytes_preserved": True,
        },
    }
    save_json(ZIP_VALIDATION, zip_validation)
    return {
        "source_files": len(source_files),
        "public_files": len(files),
        "public_bytes": sum(path.stat().st_size for path in files),
        "transformed_files": len(ledger),
        "replacement_events": sum(int(row["replacement_count"]) for row in ledger),
        "transformed_source_zips": transformed_source_zips,
        "zip": {key: value for key, value in file_row(OUTPUT_ZIP).items() if key != "path"},
        "zip_validation": {
            key: value for key, value in file_row(ZIP_VALIDATION).items() if key != "path"
        },
    }


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
    print(f"upload {name} ({path.stat().st_size} bytes)", flush=True)
    with path.open("rb") as handle:
        base.check(
            session.put(
                f"{bucket.rstrip('/')}/{urllib.parse.quote(name, safe='')}",
                headers={"Authorization": f"Bearer {token}", "Content-Type": "application/octet-stream"},
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


def save_state(value: dict) -> None:
    save_json(STATE, value)


def main() -> None:
    build = build_projection()
    uploads = {
        PRIMARY_ZIP: file_row(OUTPUT_ZIP),
        "PACKAGE_PREMANIFEST_VALIDATION.json": file_row(OUTPUT_ROOT / "PACKAGE_PREMANIFEST_VALIDATION.json"),
        "PACKAGE_PAYLOAD_MANIFEST.csv": file_row(OUTPUT_ROOT / "PACKAGE_PAYLOAD_MANIFEST.csv"),
        "PACKAGE_MANIFEST_VALIDATION.json": file_row(OUTPUT_ROOT / "PACKAGE_MANIFEST_VALIDATION.json"),
        ZIP_VALIDATION.name: file_row(ZIP_VALIDATION),
        TRANSFORM_LEDGER: file_row(OUTPUT_ROOT / TRANSFORM_LEDGER),
    }
    for name in build["transformed_source_zips"]:
        uploads[str(name)] = file_row(OUTPUT_ROOT / str(name))
    session = base.make_session()
    token = base.find_token()
    auth_legacy = {"Authorization": f"Bearer {token}"}
    auth_modern = {**MODERN, "Authorization": f"Bearer {token}"}
    state = json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {}
    current = base.check(
        session.get(f"{API}/records/{CURRENT_RECORD}?expand=true", headers=MODERN, timeout=(30, 300)), {200}
    ).json()
    current_entries = base.modern_entries(current)
    latest = base.check(session.get(current["links"]["latest"], headers=MODERN, timeout=(30, 300)), {200}).json()
    if (
        current.get("is_published") is not True
        or current["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or len(current_entries) != CURRENT_FILES
        or sum(int(row["size"]) for row in current_entries.values()) != CURRENT_BYTES
        or (
            int(latest["id"])
            != int(state.get("published_record", CURRENT_RECORD))
        )
        or current["files"].get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("Privacy-remediation predecessor guard changed")
    desired = set(current_entries) | {TRANSFORM_LEDGER}
    if state.get("published_record"):
        record_id = int(state["published_record"])
    else:
        probe = session.get(
            f"{API}/records/{CURRENT_RECORD}/draft?expand=true", headers=auth_modern, timeout=(30, 300)
        )
        if state.get("draft_id"):
            if probe.status_code != 200 or int(probe.json()["id"]) != int(state["draft_id"]):
                raise RuntimeError("Tracked privacy-remediation draft is not active")
            draft_id = int(state["draft_id"])
        else:
            if probe.status_code != 404:
                raise RuntimeError("Untracked active SGA draft exists")
            deposition = base.check(
                session.get(f"{API}/deposit/depositions/{CURRENT_RECORD}", headers=auth_legacy, timeout=(30, 300)),
                {200},
            ).json()
            created = base.check(
                session.post(deposition["links"]["newversion"], headers=auth_legacy, timeout=(30, 600)), {201}
            ).json()
            draft = base.check(
                session.get(created["links"]["latest_draft"], headers=auth_legacy, timeout=(30, 300)), {200}
            ).json()
            draft_id = int(draft["id"])
            state = {"status": "OPEN_TRACKED_DRAFT", "draft_id": draft_id, "predecessor": CURRENT_RECORD}
            save_state(state)
            print(f"created tracked privacy-remediation draft {draft_id}", flush=True)
        deposition = base.check(
            session.get(f"{API}/deposit/depositions/{draft_id}", headers=auth_legacy, timeout=(30, 300)), {200}
        ).json()
        staged = base.legacy_entries(deposition)
        for name, row in uploads.items():
            if name in staged:
                observed = int(staged[name]["filesize"]), base.normalized_md5(staged[name]["checksum"])
                wanted = int(row["bytes"]), str(row["md5"])
                if observed == wanted:
                    continue
                base.check(session.delete(staged[name]["links"]["self"], headers=auth_legacy, timeout=(30, 300)), {204})
            upload_file(session, token, deposition["links"]["bucket"], name, Path(row["path"]))
        draft = base.check(
            session.get(f"{API}/records/{draft_id}/draft?expand=true", headers=auth_modern, timeout=(30, 300)), {200}
        ).json()
        entries = base.modern_entries(draft)
        if set(entries) != desired:
            raise RuntimeError("Privacy-remediation staged file boundary changed")
        for name, row in uploads.items():
            if identity(entries[name]) != (int(row["bytes"]), str(row["md5"])):
                raise RuntimeError(f"Privacy-remediation staged identity changed: {name}")
        for name in set(current_entries) - set(uploads):
            if identity(entries[name]) != identity(current_entries[name]):
                raise RuntimeError(f"Privacy-remediation retained identity changed: {name}")
        metadata = copy.deepcopy(current["metadata"])
        metadata["publication_date"] = "2026-08-03"
        metadata["version"] = "2026-08-03 presentation-clean SGA 1-7 II privacy-remediated public projection"
        metadata["description"] = current["metadata"]["description"]
        metadata.pop("additional_descriptions", None)
        remaining = sorted(desired - {PRIMARY_ZIP, DEFAULT_PREVIEW}, key=str.casefold)
        order = [PRIMARY_ZIP, DEFAULT_PREVIEW, *remaining]
        payload = {
            "access": current["access"],
            "files": {"enabled": True, "default_preview": DEFAULT_PREVIEW, "order": order},
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
            or patched["files"].get("default_preview") != DEFAULT_PREVIEW
            or patched["metadata"]["description"] != current["metadata"]["description"]
        ):
            raise RuntimeError("Privacy-remediation presentation patch changed")
        published = base.check(
            session.post(patched["links"]["publish"], headers=auth_modern, timeout=(30, 1200)), {200, 202}
        ).json()
        record_id = int(published["id"])
        state.update({"status": "PUBLISHED_READBACK_PENDING", "published_record": record_id})
        save_state(state)
        print(f"published privacy-remediated SGA record {record_id}", flush=True)
    record = None
    for attempt in range(90):
        response = session.get(f"{API}/records/{record_id}?expand=true", headers=MODERN, timeout=(30, 300))
        if response.status_code == 200 and response.json().get("is_published"):
            candidate = response.json()
            if set(base.modern_entries(candidate)) == desired:
                record = candidate
                break
        time.sleep(min(attempt + 1, 5))
    if record is None:
        raise RuntimeError("Privacy-remediated SGA record did not become publicly stable")
    entries = base.modern_entries(record)
    readback = {}
    for name, row in uploads.items():
        print(f"readback privacy-remediation {name}", flush=True)
        observed = stream_readback(session, entries[name]["links"]["content"])
        wanted = int(row["bytes"]), str(row["sha256"])
        readback[name] = {
            "bytes": observed[0], "sha256": observed[1], "match": observed == wanted,
            "content_url": entries[name]["links"]["content"],
        }
        if observed != wanted:
            raise RuntimeError(f"Privacy-remediation public readback changed: {name}")
    for name in set(current_entries) - set(uploads):
        if identity(entries[name]) != identity(current_entries[name]):
            raise RuntimeError(f"Privacy-remediation public retained identity changed: {name}")
    latest = base.check(session.get(record["links"]["latest"], headers=MODERN, timeout=(30, 300)), {200}).json()
    draft_probe = session.get(f"{API}/records/{record_id}/draft", headers=auth_modern, timeout=(30, 300))
    if (
        int(latest["id"]) != record_id
        or draft_probe.status_code != 404
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or record["metadata"]["description"] != current["metadata"]["description"]
    ):
        raise RuntimeError("Privacy-remediation public closeout changed")
    result = {
        "status": "PASS_PRIVACY_REMEDIATED_PUBLISHED_AND_PUBLIC_READBACK",
        "record_id": record_id,
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": CURRENT_RECORD,
        "files": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "default_preview": DEFAULT_PREVIEW,
        "landing_description_unchanged_whole_project": True,
        "build": build,
        "replaced_public_objects": sorted(set(uploads) - {TRANSFORM_LEDGER}),
        "added_public_objects": [TRANSFORM_LEDGER],
        "retained_predecessor_files": len(set(current_entries) - set(uploads)),
        "raw_public_readback": readback,
        "active_draft": False,
        "duplicate_concept": False,
        "adverse_history": {
            "record": CURRENT_RECORD,
            "state": "superseded; contained absolute private build paths in audit controls inside the complete ZIP",
            "source_package_mutated": False,
        },
    }
    receipt = REPO / "manifests/published-zenodo" / (
        f"20260803_sga_privacy_remediation_record_{record_id}_public_readback.json"
    )
    save_json(receipt, result)
    state.update({"status": "CLOSED_PUBLIC_READBACK_PASS", "receipt": receipt.relative_to(REPO).as_posix()})
    save_state(state)
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    main()
