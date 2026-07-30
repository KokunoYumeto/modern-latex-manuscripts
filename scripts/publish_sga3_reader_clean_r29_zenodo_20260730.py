#!/usr/bin/env python3
"""Prepare and anonymously verify the SGA3 R29 Zenodo successor.

The authenticated file mutation is intentionally performed in the signed-in
Zenodo UI. This script owns the deterministic release controls and the public
post-publication replay, so the browser step cannot silently change scope.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PREDECESSOR_RECORD = 21_703_611
SUCCESSOR_DRAFT = 21_704_696
CONCEPT_DOI = "10.5281/zenodo.20410947"
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
GITHUB_COMMIT = "e771e8c582465311cc399ba2db503cc3dd4fa9ab"

PACKAGE_REL = Path(
    "sources/sga/"
    "sga3-english-reader-clean-r29-complete-native-reference-v2-20260730"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
REPLAY_REL = Path(
    "sources/sga/"
    "sga3-english-reader-clean-r29-independent-replay-20260730"
)
REPLAY_ROOT = REPO_ROOT / REPLAY_REL
BUNDLE_REL = Path(
    "sources/sga/"
    "sga1-6-current-readers-and-buildable-tex-bundle-20260730"
)
BUNDLE_ROOT = REPO_ROOT / BUNDLE_REL

TEMP_ROOT = Path(r"C:\tmp\sga3-r29-zenodo-20260730")
CONTROLS_ROOT = TEMP_ROOT / "release-controls"
READBACK_ROOT = TEMP_ROOT / "public-readback"
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260730_sga1_reference_v2_record_21703611_public_readback.json"
)

LEADING_BUNDLE = (
    "00_Current_SGA1-6_English_Readers_and_Buildable_TeX_20260730.zip"
)
SGA3_PDF = "00c_SGA3_English_Reader.pdf"
SGA3_TEX = "02c_SGA3_English_Master.tex"
OLD_SGA3_ZIP = "10c_SGA3_English_Source_R28_20260730.zip"
SGA3_ZIP = "10c_SGA3_English_Reader_and_Buildable_TeX_R29_20260730.zip"
SGA3_QA_ZIP = "10c3_SGA3_English_Reference_and_QA_Controls_R29_20260730.zip"
CONTROLS_ZIP = "10z_SGA_Current_Release_Controls_20260730.zip"

REPLACED = {
    LEADING_BUNDLE,
    SGA3_PDF,
    SGA3_TEX,
    OLD_SGA3_ZIP,
    CONTROLS_ZIP,
}

README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
PACKAGE_VALIDATION_NAME = "09c_SGA3_PACKAGE_VALIDATION.json"
PACKAGE_MANIFEST_NAME = "09d_SGA3_PACKAGE_SHA256SUMS.csv"
REPLAY_NAME = "09e_SGA3_INDEPENDENT_REPLAY.json"
BUNDLE_VALIDATION_NAME = "09f_SGA1-6_BUNDLE_VALIDATION.json"
GITHUB_READBACK_NAME = "09g_GITHUB_PUBLIC_READBACK.json"
PACKED_MANIFEST_NAME = "PACKED_CONTROL_SHA256.csv"

LOCAL_FILES = {
    LEADING_BUNDLE: BUNDLE_ROOT / LEADING_BUNDLE,
    SGA3_PDF: PACKAGE_ROOT / SGA3_PDF,
    SGA3_TEX: PACKAGE_ROOT / SGA3_TEX,
    SGA3_ZIP: PACKAGE_ROOT / SGA3_ZIP,
    SGA3_QA_ZIP: PACKAGE_ROOT / (
        "20c_SGA3_English_Reference_and_QA_Controls_R29_20260730.zip"
    ),
}

EXPECTED_LOCAL = {
    LEADING_BUNDLE: (
        23_366_264,
        "511B9363B98F9A64BC81F0044CDD714C09D8B6A9D6087679E3C78FD3C091299C",
    ),
    SGA3_PDF: (
        11_859_958,
        "FE7211BA4288E66430E64C574E808E9BAD596E99366777D2DDC2349CB9BD427C",
    ),
    SGA3_TEX: (
        9_121,
        "B0106C64F7D3FB63F78A2F18C2684B27E14FDAD0D51B923EBA61F2A1980AF988",
    ),
    SGA3_ZIP: (
        8_984_977,
        "FC08B10DC0B2F82C994939F325251FB20E06D9E5EEF48E14780B0E9E3D55FD25",
    ),
    SGA3_QA_ZIP: (
        22_563_396,
        "0F19250A0DDCAE9177F097B47C45F82ADC38CD1113A3C7BAE8377164691A3D26",
    ),
}

ZIP_SPECS = {
    LEADING_BUNDLE: {
        "members": 1_394,
        "manifest": (
            "SGA_Current_English_Readers_and_TeX_20260730/SHA256SUMS.csv"
        ),
        "manifest_rows": 1_393,
    },
    SGA3_ZIP: {
        "members": 918,
        "manifest": "SHA256SUMS.csv",
        "manifest_rows": 917,
    },
    SGA3_QA_ZIP: {
        "members": 32,
        "manifest": "SHA256SUMS.csv",
        "manifest_rows": 31,
    },
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5_file(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def identity(path: Path) -> dict[str, object]:
    return {
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
        "md5": md5_file(path),
    }


def fetch_bytes(url: str, timeout: int = 900) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "modern-latex-manuscripts-readback"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def fetch_json(url: str) -> dict:
    return json.loads(fetch_bytes(url).decode("utf-8"))


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=True, indent=2) + "\n").encode(
        "utf-8"
    )


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def read_csv_bytes(data: bytes) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(data.decode("utf-8-sig"))))


def safe_zip_name(name: str) -> None:
    normalized = name.replace("\\", "/")
    if (
        not normalized
        or normalized.startswith("/")
        or ":" in normalized.split("/")[0]
        or any(part in {"", ".", ".."} for part in normalized.split("/"))
    ):
        raise RuntimeError(f"Unsafe ZIP member: {name}")


def inspect_zip(path: Path, spec: dict[str, object]) -> dict[str, object]:
    with zipfile.ZipFile(path, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError(f"CRC failure: {path.name}")
        infos = [info for info in archive.infolist() if not info.is_dir()]
        if len(infos) != int(spec["members"]):
            raise RuntimeError(f"ZIP member boundary mismatch: {path.name}")
        for info in infos:
            safe_zip_name(info.filename)
        manifest_data = archive.read(str(spec["manifest"]))
        rows = read_csv_bytes(manifest_data)
        if len(rows) != int(spec["manifest_rows"]):
            raise RuntimeError(f"ZIP manifest boundary mismatch: {path.name}")
        seen: set[str] = set()
        manifest_parent = str(spec["manifest"]).replace("\\", "/").rsplit("/", 1)
        prefix = manifest_parent[0] + "/" if len(manifest_parent) == 2 else ""
        for row in rows:
            relative = row.get("path") or row.get("relative_path")
            if not relative:
                raise RuntimeError(f"ZIP manifest path field missing: {path.name}")
            member = prefix + relative.replace("\\", "/")
            if member in seen:
                raise RuntimeError(f"Duplicate ZIP manifest member: {member}")
            seen.add(member)
            data = archive.read(member)
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(f"ZIP member mismatch: {path.name}/{member}")
        return {
            "filename": path.name,
            "member_count": len(infos),
            "manifest_rows": len(rows),
            "manifest_sha256": sha256_bytes(manifest_data),
            "uncompressed_bytes": sum(info.file_size for info in infos),
            "identity_errors": 0,
        }


def predecessor_state() -> tuple[dict, dict[str, dict], list[dict[str, str]]]:
    record = fetch_json(f"https://zenodo.org/api/records/{PREDECESSOR_RECORD}")
    if (
        int(record["id"]) != PREDECESSOR_RECORD
        or record.get("doi") != f"10.5281/zenodo.{PREDECESSOR_RECORD}"
        or record.get("conceptdoi") != CONCEPT_DOI
        or len(record["files"]) != 67
        or sum(int(row["size"]) for row in record["files"]) != 449_693_682
    ):
        raise RuntimeError("Live predecessor boundary changed")
    api_files = {
        row["key"]: {
            "bytes": int(row["size"]),
            "md5": row["checksum"].split(":", 1)[1].lower(),
            "content_url": row["links"]["self"],
        }
        for row in record["files"]
    }
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8-sig"))
    if (
        receipt["status"] != "PASS_PUBLIC_READBACK"
        or int(receipt["record_id"]) != PREDECESSOR_RECORD
        or receipt["concept_doi"] != CONCEPT_DOI
        or receipt["default_preview"] != DEFAULT_PREVIEW
        or receipt["outer_file_identities"] != {
            name: {"bytes": row["bytes"], "md5": row["md5"]}
            for name, row in api_files.items()
        }
    ):
        raise RuntimeError("Predecessor public receipt no longer matches API")
    controls = fetch_bytes(api_files[CONTROLS_ZIP]["content_url"])
    if (
        len(controls) != api_files[CONTROLS_ZIP]["bytes"]
        or hashlib.md5(controls, usedforsecurity=False).hexdigest()
        != api_files[CONTROLS_ZIP]["md5"]
    ):
        raise RuntimeError("Predecessor controls readback mismatch")
    with zipfile.ZipFile(io.BytesIO(controls), "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Predecessor controls CRC mismatch")
        rows = read_csv_bytes(archive.read(MANIFEST_NAME))
    if len(rows) != 66:
        raise RuntimeError("Predecessor release manifest boundary mismatch")
    row_map = {row["filename"]: row for row in rows}
    if len(row_map) != 66 or set(row_map) != set(api_files) - {CONTROLS_ZIP}:
        raise RuntimeError("Predecessor release manifest set mismatch")
    for name, row in row_map.items():
        if int(row["bytes"]) != api_files[name]["bytes"]:
            raise RuntimeError(f"Predecessor release size mismatch: {name}")
    return record, api_files, rows


def github_readback() -> dict[str, object]:
    roots = [PACKAGE_REL, REPLAY_REL, BUNDLE_REL]
    observed: dict[str, dict[str, object]] = {}
    for relative_root in roots:
        local_root = REPO_ROOT / relative_root
        for path in sorted(local_root.iterdir(), key=lambda item: item.name.casefold()):
            if not path.is_file():
                continue
            rel = (relative_root / path.name).as_posix()
            url = (
                "https://raw.githubusercontent.com/KokunoYumeto/"
                "modern-latex-manuscripts/"
                f"{GITHUB_COMMIT}/{rel}"
            )
            remote = fetch_bytes(url)
            local = path.read_bytes()
            if remote != local:
                raise RuntimeError(f"GitHub public readback mismatch: {rel}")
            observed[rel] = {
                "bytes": len(remote),
                "sha256": sha256_bytes(remote),
                "url": url,
            }
    if len(observed) != 15:
        raise RuntimeError("GitHub public readback file boundary mismatch")
    return {
        "status": "PASS_PUBLIC_GITHUB_READBACK",
        "commit": GITHUB_COMMIT,
        "files": observed,
    }


def local_state() -> tuple[dict[str, dict[str, object]], dict[str, dict[str, object]]]:
    identities: dict[str, dict[str, object]] = {}
    for name, path in LOCAL_FILES.items():
        if not path.is_file():
            raise RuntimeError(f"Missing local upload: {path}")
        observed = identity(path)
        if (observed["bytes"], observed["sha256"]) != EXPECTED_LOCAL[name]:
            raise RuntimeError(f"Local upload identity mismatch: {name}")
        identities[name] = {**observed, "path": str(path)}
    zip_results = {
        name: inspect_zip(LOCAL_FILES[name], spec)
        for name, spec in ZIP_SPECS.items()
    }
    return identities, zip_results


def build_controls() -> dict[str, object]:
    _, predecessor_files, predecessor_rows = predecessor_state()
    local_files, zip_results = local_state()
    github = github_readback()
    retained = {
        name: row for name, row in predecessor_files.items() if name not in REPLACED
    }
    if len(retained) != 62:
        raise RuntimeError("Retained predecessor boundary mismatch")
    prospective = {**retained, **local_files}
    if len(prospective) != 67:
        raise RuntimeError("Prospective non-control boundary mismatch")
    prior_rows = {row["filename"]: row for row in predecessor_rows}
    roles = {
        LEADING_BUNDLE: "current_reader_bundle",
        SGA3_PDF: "english_reader",
        SGA3_TEX: "english_tex",
        SGA3_ZIP: "source_archive",
        SGA3_QA_ZIP: "qa_archive",
    }
    provenance = {
        LEADING_BUNDLE: (
            "current cumulative English SGA1-6 PDFs and complete buildable "
            f"TeX closures; GitHub commit {GITHUB_COMMIT}"
        ),
        SGA3_PDF: (
            "clean complete 1470-page cumulative SGA3 R29 reader; "
            f"GitHub commit {GITHUB_COMMIT}"
        ),
        SGA3_TEX: (
            "clean complete SGA3 R29 editable master; "
            f"GitHub commit {GITHUB_COMMIT}"
        ),
        SGA3_ZIP: (
            "one-click cumulative SGA3 R29 PDF plus 914-file buildable TeX "
            f"closure; GitHub commit {GITHUB_COMMIT}"
        ),
        SGA3_QA_ZIP: (
            "optional SGA3 R29 reference and QA controls; "
            f"GitHub commit {GITHUB_COMMIT}"
        ),
    }
    rows: list[dict[str, object]] = []
    for name in sorted(prospective, key=str.casefold):
        item = prospective[name]
        if name in local_files:
            role = roles[name]
            source = provenance[name]
            status = "current"
        else:
            prior = prior_rows[name]
            role = prior["role"]
            source = prior["provenance"]
            status = prior["status"]
        rows.append(
            {
                "filename": name,
                "bytes": item["bytes"],
                "sha256": (
                    item["sha256"] if name in local_files else prior_rows[name]["sha256"]
                ),
                "role": role,
                "provenance": source,
                "status": status,
            }
        )

    if CONTROLS_ROOT.exists():
        resolved = CONTROLS_ROOT.resolve()
        if TEMP_ROOT.resolve() not in resolved.parents:
            raise RuntimeError("Refusing to replace controls outside temp root")
        shutil.rmtree(CONTROLS_ROOT)
    CONTROLS_ROOT.mkdir(parents=True)

    readme = f"""# Current compact SGA release

This is a same-concept successor to Zenodo record {PREDECESSOR_RECORD},
reserved as record {SUCCESSOR_DRAFT}. It retains 62 public files byte-for-byte
and replaces only the all-SGA reader/source bundle, preferred SGA3 reader and
editable master, SGA3 source package, and release controls. One optional SGA3
reference/QA archive is added.

The first download is a single ZIP containing the current cumulative English
SGA1 through SGA6 PDFs and their complete buildable TeX closures. Direct
English reader PDFs remain individually accessible and precede direct TeX and
archive material. The default browser preview remains the SGA1 reader.

The preferred SGA3 R29 reader contains the Introduction, Exposes I-XXVI, the
Tome-I subject index, Tome-III mathematical guide, and terminal index in 1,470
A4 pages. Its 914-file buildable TeX closure and identical PDF are available in
one ZIP. The reader contains mathematics and source-era scholarly apparatus,
without project, workflow, production-status, source-locator, or tooling notes.

These are working English translations and TeX editions, not critical
editions, peer review, accessibility certification, or rights determinations.
They do not transfer rights in the underlying French works. Earlier Zenodo
versions remain immutable history.
"""
    manifest = csv_bytes(
        rows,
        ["filename", "bytes", "sha256", "role", "provenance", "status"],
    )
    validation = {
        "status": "PASS_READY_FOR_SINGLE_UI_PUBLICATION",
        "errors": [],
        "source_record": PREDECESSOR_RECORD,
        "reserved_successor_record": SUCCESSOR_DRAFT,
        "concept_doi": CONCEPT_DOI,
        "prospective_files": 68,
        "release_manifest_rows": 67,
        "retained_predecessor_files": 62,
        "replaced_predecessor_files": sorted(REPLACED, key=str.casefold),
        "new_noncontrol_files": sorted(local_files, key=str.casefold),
        "default_preview": DEFAULT_PREVIEW,
        "github": github,
        "sga3_reader": {
            "filename": SGA3_PDF,
            "bytes": local_files[SGA3_PDF]["bytes"],
            "sha256": local_files[SGA3_PDF]["sha256"],
            "pages": 1_470,
            "named_destinations": 13_119,
            "internal_goto_actions": 12_337,
            "broken_or_external_actions": 0,
            "image_xobjects": 0,
            "type3_fonts": 0,
            "reader_facing_project_or_workflow_notes": 0,
        },
        "zip_replays": zip_results,
        "privacy_hits": [],
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    control_files = {
        README_NAME: readme.encode("utf-8"),
        MANIFEST_NAME: manifest,
        VALIDATION_NAME: json_bytes(validation),
        PACKAGE_VALIDATION_NAME: (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_bytes(),
        PACKAGE_MANIFEST_NAME: (PACKAGE_ROOT / "SHA256SUMS.csv").read_bytes(),
        REPLAY_NAME: (
            REPLAY_ROOT / "INDEPENDENT_ARCHIVE_REPLAY.json"
        ).read_bytes(),
        BUNDLE_VALIDATION_NAME: (
            BUNDLE_ROOT / "BUNDLE_VALIDATION.json"
        ).read_bytes(),
        GITHUB_READBACK_NAME: json_bytes(github),
    }
    packed_rows = [
        {
            "filename": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(control_files.items(), key=lambda row: row[0].casefold())
    ]
    control_files[PACKED_MANIFEST_NAME] = csv_bytes(
        packed_rows, ["filename", "bytes", "sha256"]
    )
    for name, data in control_files.items():
        (CONTROLS_ROOT / name).write_bytes(data)

    control_zip = TEMP_ROOT / CONTROLS_ZIP
    if control_zip.exists():
        control_zip.unlink()
    with zipfile.ZipFile(
        control_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name in sorted(control_files, key=str.casefold):
            safe_zip_name(name)
            info = zipfile.ZipInfo(name, date_time=(2026, 7, 30, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, control_files[name])
    inspect_control_zip(control_zip, 9)

    qa_upload = TEMP_ROOT / SGA3_QA_ZIP
    shutil.copyfile(LOCAL_FILES[SGA3_QA_ZIP], qa_upload)
    if identity(qa_upload) != {
        key: local_files[SGA3_QA_ZIP][key] for key in ("bytes", "sha256", "md5")
    }:
        raise RuntimeError("Renamed QA upload copy mismatch")
    summary = {
        "status": "PASS_READY_FOR_SINGLE_UI_PUBLICATION",
        "draft_id": SUCCESSOR_DRAFT,
        "retained_files": 62,
        "final_files": 68,
        "uploads": {
            **local_files,
            CONTROLS_ZIP: {
                **identity(control_zip),
                "path": str(control_zip),
            },
        },
        "qa_upload_copy": str(qa_upload),
        "controls_zip": str(control_zip),
    }
    summary_path = TEMP_ROOT / "PREPARE_RESULT.json"
    summary_path.write_bytes(json_bytes(summary))
    return summary


def inspect_control_zip(path: Path, expected_members: int) -> dict[str, object]:
    with zipfile.ZipFile(path, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Release controls CRC failure")
        infos = [info for info in archive.infolist() if not info.is_dir()]
        if len(infos) != expected_members:
            raise RuntimeError("Release controls member boundary mismatch")
        rows = read_csv_bytes(archive.read(PACKED_MANIFEST_NAME))
        if len(rows) != expected_members - 1:
            raise RuntimeError("Release controls packed manifest mismatch")
        for row in rows:
            data = archive.read(row["filename"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(f"Release control mismatch: {row['filename']}")
        return {
            "member_count": len(infos),
            "manifest_rows": len(rows),
            "uncompressed_bytes": sum(info.file_size for info in infos),
            "identity_errors": 0,
        }


def exact_zip_member_receipt(
    path: Path, filename: str, content_url: str
) -> dict[str, object]:
    members: list[dict[str, object]] = []
    with zipfile.ZipFile(path, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError(f"Public ZIP CRC failure: {filename}")
        for info in archive.infolist():
            if info.is_dir():
                continue
            safe_zip_name(info.filename)
            data = archive.read(info.filename)
            members.append(
                {
                    "path": info.filename,
                    "bytes": len(data),
                    "sha256": sha256_bytes(data),
                }
            )
    return {
        "status": "PASS_PUBLIC_ZIP_MEMBER_READBACK",
        "record_id": SUCCESSOR_DRAFT,
        "filename": filename,
        "content_url": content_url,
        "outer_bytes": path.stat().st_size,
        "outer_sha256": sha256_file(path),
        "member_count": len(members),
        "uncompressed_bytes": sum(int(row["bytes"]) for row in members),
        "members": members,
    }


def public_readback(record_id: int) -> dict[str, object]:
    if record_id != SUCCESSOR_DRAFT:
        raise RuntimeError("Unexpected successor record id")
    record = fetch_json(f"https://zenodo.org/api/records/{record_id}")
    if (
        int(record["id"]) != record_id
        or record.get("doi") != f"10.5281/zenodo.{record_id}"
        or record.get("conceptdoi") != CONCEPT_DOI
        or len(record["files"]) != 68
    ):
        raise RuntimeError("Public successor boundary mismatch")
    files = {
        row["key"]: {
            "bytes": int(row["size"]),
            "md5": row["checksum"].split(":", 1)[1].lower(),
            "content_url": row["links"]["self"],
        }
        for row in record["files"]
    }
    _, predecessor_files, _ = predecessor_state()
    retained = {
        name: row for name, row in predecessor_files.items() if name not in REPLACED
    }
    if len(retained) != 62:
        raise RuntimeError("Retained set boundary mismatch during readback")
    for name, row in retained.items():
        current = files.get(name)
        if current is None or (
            current["bytes"], current["md5"]
        ) != (row["bytes"], row["md5"]):
            raise RuntimeError(f"Retained file identity changed: {name}")

    prepared = json.loads((TEMP_ROOT / "PREPARE_RESULT.json").read_text())
    expected_uploads = prepared["uploads"]
    downloaded: dict[str, dict[str, object]] = {}
    if READBACK_ROOT.exists():
        resolved = READBACK_ROOT.resolve()
        if TEMP_ROOT.resolve() not in resolved.parents:
            raise RuntimeError("Refusing to replace readback outside temp root")
        shutil.rmtree(READBACK_ROOT)
    READBACK_ROOT.mkdir(parents=True)
    for name, expected in expected_uploads.items():
        if name not in files:
            raise RuntimeError(f"Missing new public file: {name}")
        data = fetch_bytes(files[name]["content_url"])
        observed = {
            "bytes": len(data),
            "sha256": sha256_bytes(data),
            "md5": hashlib.md5(data, usedforsecurity=False).hexdigest(),
            "content_url": files[name]["content_url"],
        }
        if (observed["bytes"], observed["sha256"], observed["md5"]) != (
            int(expected["bytes"]),
            expected["sha256"],
            expected["md5"],
        ):
            raise RuntimeError(f"New public file readback mismatch: {name}")
        target = READBACK_ROOT / name
        target.write_bytes(data)
        downloaded[name] = observed

    zip_results = {
        name: inspect_zip(READBACK_ROOT / name, spec)
        for name, spec in ZIP_SPECS.items()
    }
    controls_result = inspect_control_zip(READBACK_ROOT / CONTROLS_ZIP, 9)
    with zipfile.ZipFile(READBACK_ROOT / CONTROLS_ZIP, "r") as archive:
        release_rows = read_csv_bytes(archive.read(MANIFEST_NAME))
    if len(release_rows) != 67:
        raise RuntimeError("Public release-manifest boundary mismatch")
    release_map = {row["filename"]: row for row in release_rows}
    if set(release_map) != set(files) - {CONTROLS_ZIP}:
        raise RuntimeError("Public release-manifest set mismatch")
    for name, row in release_map.items():
        if int(row["bytes"]) != files[name]["bytes"]:
            raise RuntimeError(f"Public release-manifest size mismatch: {name}")

    expected_order = sorted(files, key=str.casefold)
    result = {
        "status": "PASS_PUBLIC_READBACK",
        "record_id": record_id,
        "record_url": f"https://zenodo.org/records/{record_id}",
        "doi": f"10.5281/zenodo.{record_id}",
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "github_commit": GITHUB_COMMIT,
        "outer_files": len(files),
        "outer_bytes": sum(row["bytes"] for row in files.values()),
        "retained_predecessor_files": len(retained),
        "default_preview_expected": DEFAULT_PREVIEW,
        "expected_file_order": expected_order,
        "api_file_order": [row["key"] for row in record["files"]],
        "new_file_readback": downloaded,
        "retained_file_identities": retained,
        "zip_readback": zip_results,
        "controls_zip_readback": controls_result,
        "release_manifest_rows": len(release_rows),
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    RECEIPT_ROOT.mkdir(parents=True, exist_ok=True)
    receipt = (
        RECEIPT_ROOT
        / f"20260730_sga3_r29_record_{record_id}_public_readback.json"
    )
    receipt.write_bytes(json_bytes(result))
    zip_receipt_names = {
        LEADING_BUNDLE: (
            f"20260730_sga3_r29_record_{record_id}_bundle_member_readback.json"
        ),
        SGA3_ZIP: (
            f"20260730_sga3_r29_record_{record_id}_source_zip_member_readback.json"
        ),
        SGA3_QA_ZIP: (
            f"20260730_sga3_r29_record_{record_id}_qa_zip_member_readback.json"
        ),
        CONTROLS_ZIP: (
            f"20260730_sga3_r29_record_{record_id}_controls_zip_member_readback.json"
        ),
    }
    for name, receipt_name in zip_receipt_names.items():
        member_receipt = exact_zip_member_receipt(
            READBACK_ROOT / name,
            name,
            files[name]["content_url"],
        )
        (RECEIPT_ROOT / receipt_name).write_bytes(json_bytes(member_receipt))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("prepare", "readback"))
    parser.add_argument("--record", type=int, default=SUCCESSOR_DRAFT)
    args = parser.parse_args()
    if args.command == "prepare":
        result = build_controls()
    else:
        result = public_readback(args.record)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
