#!/usr/bin/env python3
"""Prepare and anonymously verify the partial SGA7 I Zenodo successor.

The authenticated new-version, upload, metadata, and publish steps are carried
out in the signed-in Zenodo UI. This helper fixes the intended mutation and
performs complete public readback without retaining downloaded payload copies.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import shutil
import sys
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PREDECESSOR_RECORD = 21_704_696
CONCEPT_DOI = "10.5281/zenodo.20410947"
GITHUB_COMMIT = "958c6c31a1b7b603cf150bfa58fbb846c4ab24b2"
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"

PACKAGE_REL = Path(
    "sources/sga/"
    "sga7i-fresh-transcription-exposes-i-ii-vi-vii-working-20260730"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
TEMP_ROOT = Path(r"C:\tmp\sga7i-zenodo-20260730")
CONTROLS_ROOT = TEMP_ROOT / "release-controls"
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260730_sga3_r29_record_21704696_public_readback.json"
)

PDF_NAME = "00g_SGA7I_Fresh_Source_Transcription_I_II_VI_VII_Working.pdf"
TEX_NAME = "02g_SGA7I_Fresh_Source_Transcription_I_II_VI_VII_Working.tex"
ZIP_NAME = (
    "10g_SGA7I_Fresh_Source_Transcription_I_II_VI_VII_"
    "Reader_and_Source_20260730.zip"
)
CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260730.zip"

README_NAME = "09_README_CURRENT_RELEASE.md"
RELEASE_MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
RELEASE_VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
SGA7_VALIDATION_NAME = "09h_SGA7I_PACKAGE_VALIDATION.json"
SGA7_MANIFEST_NAME = "09i_SGA7I_PACKAGE_SHA256SUMS.csv"
SGA7_GITHUB_NAME = "09j_SGA7I_GITHUB_PUBLIC_READBACK.json"
PACKED_MANIFEST_NAME = "PACKED_CONTROL_SHA256.csv"

OLD_CONTROLS = (
    19_107,
    "D3150D21A6CB652ACE1131F2DAD8E17125BF82B2846FE4A0B379A13A1031BF92",
)
PREDECESSOR_BOUNDARY = (68, 478_075_538)

LOCAL_FILES = {
    PDF_NAME: PACKAGE_ROOT
    / "reader/SGA7I_Fresh_Transcription_Exposes_I_II_VI_VII_Working.pdf",
    TEX_NAME: PACKAGE_ROOT
    / "source/SGA7I_Fresh_Transcription_Exposes_I_II_VI_VII_Working.tex",
    ZIP_NAME: PACKAGE_ROOT
    / "SGA7I_Fresh_Transcription_Exposes_I_II_VI_VII_"
    "Reader_and_Source_20260730.zip",
}
EXPECTED_LOCAL = {
    PDF_NAME: (
        1_006_870,
        "ED1E581C6858C219A99F1107A28C30B62BEEE7AD6DE2C009562335FC5A94B177",
    ),
    TEX_NAME: (
        2_535,
        "E8DE1C41FD213197B0ECED039AE2F7F7C1B0887C659B5EA116E1EA28BB16D57B",
    ),
    ZIP_NAME: (
        1_233_562,
        "0A9DDA79E9F48075A1191B094D23D1788B494D47A69F4E111311E77B1E97B07C",
    ),
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


def verify_zip_against_directory(zip_path: Path, root: Path) -> dict[str, object]:
    errors: list[str] = []
    with zipfile.ZipFile(zip_path, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError(f"CRC failure: {zip_path.name}")
        infos = [row for row in archive.infolist() if not row.is_dir()]
        for info in infos:
            safe_zip_name(info.filename)
            source = root / Path(info.filename)
            if not source.is_file():
                errors.append(f"missing:{info.filename}")
                continue
            data = archive.read(info.filename)
            if (len(data), sha256_bytes(data)) != (
                source.stat().st_size,
                sha256_file(source),
            ):
                errors.append(f"identity:{info.filename}")
        return {
            "member_count": len(infos),
            "uncompressed_bytes": sum(row.file_size for row in infos),
            "errors": errors,
        }


def extract_old_controls(data: bytes) -> list[dict[str, str]]:
    with zipfile.ZipFile(io.BytesIO(data), "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Current controls ZIP has a CRC failure")
        infos = [row for row in archive.infolist() if not row.is_dir()]
        if len(infos) != 9:
            raise RuntimeError("Current controls ZIP member boundary changed")
        for info in infos:
            safe_zip_name(info.filename)
            (CONTROLS_ROOT / info.filename).write_bytes(archive.read(info.filename))

    packed = read_csv_bytes((CONTROLS_ROOT / PACKED_MANIFEST_NAME).read_bytes())
    if len(packed) != 8:
        raise RuntimeError("Current packed-control boundary changed")
    for row in packed:
        path = CONTROLS_ROOT / row["filename"]
        if (path.stat().st_size, sha256_file(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Current packed-control mismatch: {path.name}")
    return read_csv_bytes(
        (CONTROLS_ROOT / RELEASE_MANIFEST_NAME).read_bytes()
    )


def github_readback() -> dict[str, object]:
    base = (
        "https://raw.githubusercontent.com/KokunoYumeto/"
        f"modern-latex-manuscripts/{GITHUB_COMMIT}/{PACKAGE_REL.as_posix()}"
    )
    manifest_data = fetch_bytes(f"{base}/SHA256SUMS.csv")
    if sha256_bytes(manifest_data) != (
        "E702090A181B858656BDC0191BF53029A53DD55468D1373517F9DCF4E4E1D082"
    ):
        raise RuntimeError("GitHub SGA7 manifest identity mismatch")
    rows = read_csv_bytes(manifest_data)
    if len(rows) != 16:
        raise RuntimeError("GitHub SGA7 manifest boundary mismatch")
    errors: list[str] = []
    for row in rows:
        quoted = urllib.parse.quote(row["relative_path"], safe="/")
        data = fetch_bytes(f"{base}/{quoted}")
        if (len(data), sha256_bytes(data)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            errors.append(row["relative_path"])
    return {
        "status": "PASS_GITHUB_PUBLIC_READBACK" if not errors else "FAIL",
        "commit": GITHUB_COMMIT,
        "package_path": PACKAGE_REL.as_posix(),
        "manifest_rows": len(rows),
        "manifest_sha256": sha256_bytes(manifest_data),
        "files_read_back": len(rows) + 1,
        "errors": errors,
    }


def current_record() -> tuple[dict, dict[str, dict[str, object]]]:
    record = fetch_json(f"https://zenodo.org/api/records/{PREDECESSOR_RECORD}")
    files = {
        row["key"]: {
            "bytes": int(row["size"]),
            "md5": row["checksum"].split(":", 1)[1].lower(),
            "content_url": row["links"].get("content", row["links"]["self"]),
        }
        for row in record["files"]
    }
    if (
        int(record["id"]) != PREDECESSOR_RECORD
        or record.get("doi") != f"10.5281/zenodo.{PREDECESSOR_RECORD}"
        or record.get("conceptdoi") != CONCEPT_DOI
        or (len(files), sum(int(row["bytes"]) for row in files.values()))
        != PREDECESSOR_BOUNDARY
    ):
        raise RuntimeError("Live SGA predecessor boundary changed")
    return record, files


def prepare() -> dict[str, object]:
    if TEMP_ROOT.exists():
        shutil.rmtree(TEMP_ROOT)
    CONTROLS_ROOT.mkdir(parents=True)

    record, api_files = current_record()
    prior = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    if prior.get("status") != "PASS_PUBLIC_READBACK":
        raise RuntimeError("Prior SGA readback receipt is not PASS")
    if set(prior["expected_file_order"]) != set(api_files):
        raise RuntimeError("Prior receipt and live predecessor differ")

    control_api = api_files[CONTROLS_NAME]
    control_data = fetch_bytes(str(control_api["content_url"]))
    if (len(control_data), sha256_bytes(control_data)) != OLD_CONTROLS:
        raise RuntimeError("Live release-controls ZIP identity changed")
    old_rows = extract_old_controls(control_data)
    if len(old_rows) != 67:
        raise RuntimeError("Live release manifest row boundary changed")
    if {row["filename"] for row in old_rows} != set(api_files) - {
        CONTROLS_NAME
    }:
        raise RuntimeError("Live release manifest filename closure failed")
    for row in old_rows:
        if int(row["bytes"]) != int(api_files[row["filename"]]["bytes"]):
            raise RuntimeError(f"Live release file size changed: {row['filename']}")

    uploads: dict[str, dict[str, object]] = {}
    for name, source in LOCAL_FILES.items():
        expected = EXPECTED_LOCAL[name]
        if (source.stat().st_size, sha256_file(source)) != expected:
            raise RuntimeError(f"Local SGA7 upload identity mismatch: {name}")
        target = TEMP_ROOT / name
        shutil.copyfile(source, target)
        uploads[name] = {**identity(target), "path": str(target)}

    zip_result = verify_zip_against_directory(TEMP_ROOT / ZIP_NAME, PACKAGE_ROOT)
    if zip_result != {
        "member_count": 13,
        "uncompressed_bytes": 2_143_291,
        "errors": [],
    }:
        raise RuntimeError("Local SGA7 ZIP replay failed")

    github = github_readback()
    if github["status"] != "PASS_GITHUB_PUBLIC_READBACK":
        raise RuntimeError("GitHub SGA7 readback failed")

    (CONTROLS_ROOT / SGA7_VALIDATION_NAME).write_bytes(
        (PACKAGE_ROOT / "PUBLIC_PROJECTION_VALIDATION.json").read_bytes()
    )
    (CONTROLS_ROOT / SGA7_MANIFEST_NAME).write_bytes(
        (PACKAGE_ROOT / "SHA256SUMS.csv").read_bytes()
    )
    (CONTROLS_ROOT / SGA7_GITHUB_NAME).write_bytes(json_bytes(github))

    readme = """# Current SGA release

Start with `00_Current_SGA1-6_English_Readers_and_Buildable_TeX_20260730.zip` for the six cumulative English reader PDFs and their buildable TeX closures. The same reader PDFs and master TeX files remain direct in SGA1-6 order, and SGA1 remains the default browser preview.

The current SGA3 reader is the clean R29 cumulative: 1,470 A4 pages covering the Introduction, Exposes I-XXVI, the Tome-I subject index, the Tome-III mathematical guide, and the terminal index. Its source package and reference/QA controls remain grouped separately.

This successor adds a fresh scan-based SGA7 I source-transcription checkpoint for complete Exposes I, II, VI, and VII. The frozen bodies cover 217 of 529 known body pages and compile as a clean 115-page A4 reader with 116 native diagrams and no raster diagram inputs. It preserves the source language as printed, including English Expose VI. Expose VIII remains unfinished and excluded; Expose IX has not started. This is not a complete SGA7 transcription or a complete English translation. The older June SGA7 reconstruction remains immutable history but is not the controlling transcription.

All objects remain working scholarly editions or transcriptions, not critical editions, peer review, accessibility certification, rights determinations, or mathematical certification. No rights in the underlying works are transferred.
"""
    (CONTROLS_ROOT / README_NAME).write_text(readme, encoding="utf-8")

    new_rows = list(old_rows)
    provenance = {
        PDF_NAME: (
            "fresh scan-based SGA7 I source transcription for complete Exposes "
            "I, II, VI, VII; 115 pages; GitHub commit " + GITHUB_COMMIT
        ),
        TEX_NAME: (
            "editable master for the fresh partial SGA7 I source transcription; "
            "GitHub commit " + GITHUB_COMMIT
        ),
        ZIP_NAME: (
            "13-member reader and editable-source archive for the fresh partial "
            "SGA7 I source transcription; GitHub commit " + GITHUB_COMMIT
        ),
    }
    roles = {
        PDF_NAME: "partial_source_transcription_reader",
        TEX_NAME: "partial_source_transcription_master",
        ZIP_NAME: "partial_source_transcription_archive",
    }
    for name in (PDF_NAME, TEX_NAME, ZIP_NAME):
        new_rows.append(
            {
                "filename": name,
                "bytes": uploads[name]["bytes"],
                "sha256": uploads[name]["sha256"],
                "role": roles[name],
                "provenance": provenance[name],
                "status": "current_partial_source_transcription",
            }
        )
    new_rows.sort(key=lambda row: row["filename"].casefold())
    (CONTROLS_ROOT / RELEASE_MANIFEST_NAME).write_bytes(
        csv_bytes(
            new_rows,
            ["filename", "bytes", "sha256", "role", "provenance", "status"],
        )
    )

    validation = {
        "status": "PASS_READY_FOR_SINGLE_SAME_CONCEPT_SUCCESSOR",
        "prepared_at": "2026-07-30",
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_files": PREDECESSOR_BOUNDARY[0],
        "predecessor_bytes": PREDECESSOR_BOUNDARY[1],
        "expected_successor_files": 71,
        "retained_predecessor_files": 67,
        "replaced_files": [CONTROLS_NAME],
        "new_files": {
            name: {key: uploads[name][key] for key in ("bytes", "sha256", "md5")}
            for name in (PDF_NAME, TEX_NAME, ZIP_NAME)
        },
        "sga7_scope": {
            "included_exposes": ["I", "II", "VI", "VII"],
            "frozen_source_pages": 217,
            "known_body_pages": 529,
            "reader_pages": 115,
            "source_language_preserved": True,
            "complete_sga7_claim": False,
            "complete_english_translation_claim": False,
        },
        "github_commit": GITHUB_COMMIT,
        "github_readback": github,
        "source_zip_replay": zip_result,
        "default_preview_expected": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "second_draft_created": False,
        "errors": [],
    }
    (CONTROLS_ROOT / RELEASE_VALIDATION_NAME).write_bytes(
        json_bytes(validation)
    )

    packed_rows = []
    for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda row: row.name.casefold()):
        if path.name == PACKED_MANIFEST_NAME:
            continue
        packed_rows.append(
            {
                "filename": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    (CONTROLS_ROOT / PACKED_MANIFEST_NAME).write_bytes(
        csv_bytes(packed_rows, ["filename", "bytes", "sha256"])
    )

    controls_zip = TEMP_ROOT / CONTROLS_NAME
    with zipfile.ZipFile(
        controls_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda row: row.name.casefold()):
            info = zipfile.ZipInfo(path.name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    uploads[CONTROLS_NAME] = {**identity(controls_zip), "path": str(controls_zip)}

    expected_files = {
        row["filename"]: {
            "bytes": int(row["bytes"]),
            "sha256": row["sha256"].upper(),
        }
        for row in new_rows
    }
    expected_files[CONTROLS_NAME] = {
        "bytes": uploads[CONTROLS_NAME]["bytes"],
        "sha256": uploads[CONTROLS_NAME]["sha256"],
    }
    result = {
        "status": "PASS_PREPARED_FOR_BROWSER_UPLOAD",
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_title": record["metadata"]["title"],
        "expected_successor_files": len(expected_files),
        "expected_successor_bytes": sum(
            int(row["bytes"]) for row in expected_files.values()
        ),
        "uploads": uploads,
        "expected_files": expected_files,
        "release_manifest_rows": len(new_rows),
        "controls_members": len(packed_rows) + 1,
        "default_preview_expected": DEFAULT_PREVIEW,
        "metadata": {
            "title": "SGA 1-7: English Readers, French Texts, TeX Archives, and Partial SGA7 Source Transcription",
            "version": "2026-07-30 fresh partial SGA7 I source transcription",
        },
        "errors": [],
    }
    (TEMP_ROOT / "PREPARE_RESULT.json").write_bytes(json_bytes(result))
    return result


def stream_identity(url: str, capture: bool = False) -> tuple[dict[str, object], bytes | None]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "modern-latex-manuscripts-readback"},
    )
    sha = hashlib.sha256()
    md5 = hashlib.md5(usedforsecurity=False)
    size = 0
    captured = io.BytesIO() if capture else None
    with urllib.request.urlopen(request, timeout=1800) as response:
        while True:
            block = response.read(1024 * 1024)
            if not block:
                break
            size += len(block)
            sha.update(block)
            md5.update(block)
            if captured is not None:
                captured.write(block)
    return (
        {
            "bytes": size,
            "sha256": sha.hexdigest().upper(),
            "md5": md5.hexdigest().lower(),
            "content_url": url,
        },
        captured.getvalue() if captured is not None else None,
    )


def inspect_remote_zip(data: bytes, expected_local: Path) -> dict[str, object]:
    with zipfile.ZipFile(io.BytesIO(data), "r") as remote, zipfile.ZipFile(
        expected_local, "r"
    ) as local:
        remote_infos = [row for row in remote.infolist() if not row.is_dir()]
        local_infos = [row for row in local.infolist() if not row.is_dir()]
        remote_names = [row.filename for row in remote_infos]
        local_names = [row.filename for row in local_infos]
        if remote_names != local_names:
            raise RuntimeError(f"Remote ZIP member set mismatch: {expected_local.name}")
        for name in remote_names:
            safe_zip_name(name)
            if remote.read(name) != local.read(name):
                raise RuntimeError(f"Remote ZIP member mismatch: {name}")
        return {
            "member_count": len(remote_infos),
            "uncompressed_bytes": sum(row.file_size for row in remote_infos),
            "identity_errors": 0,
        }


def inspect_remote_controls(data: bytes) -> dict[str, object]:
    with zipfile.ZipFile(io.BytesIO(data), "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Remote controls ZIP CRC failure")
        infos = [row for row in archive.infolist() if not row.is_dir()]
        rows = read_csv_bytes(archive.read(PACKED_MANIFEST_NAME))
        if len(rows) + 1 != len(infos):
            raise RuntimeError("Remote controls manifest boundary mismatch")
        for row in rows:
            data_row = archive.read(row["filename"])
            if (len(data_row), sha256_bytes(data_row)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    f"Remote controls member mismatch: {row['filename']}"
                )
        return {
            "member_count": len(infos),
            "manifest_rows": len(rows),
            "uncompressed_bytes": sum(row.file_size for row in infos),
            "identity_errors": 0,
        }


def readback(record_id: int) -> dict[str, object]:
    prepared = json.loads((TEMP_ROOT / "PREPARE_RESULT.json").read_text())
    record = fetch_json(f"https://zenodo.org/api/records/{record_id}")
    if (
        int(record["id"]) != record_id
        or record.get("conceptdoi") != CONCEPT_DOI
        or record.get("doi") != f"10.5281/zenodo.{record_id}"
    ):
        raise RuntimeError("Published successor identity mismatch")
    if record["metadata"].get("version") != prepared["metadata"]["version"]:
        raise RuntimeError("Published successor version metadata mismatch")

    api_files = {row["key"]: row for row in record["files"]}
    expected = prepared["expected_files"]
    if set(api_files) != set(expected):
        raise RuntimeError("Published successor outer-file set mismatch")

    files: dict[str, dict[str, object]] = {}
    captured: dict[str, bytes] = {}
    for name in sorted(expected, key=str.casefold):
        url = api_files[name]["links"].get(
            "content", api_files[name]["links"]["self"]
        )
        result, data = stream_identity(
            url, capture=name in {ZIP_NAME, CONTROLS_NAME}
        )
        if (result["bytes"], result["sha256"]) != (
            int(expected[name]["bytes"]),
            expected[name]["sha256"].upper(),
        ):
            raise RuntimeError(f"Public readback mismatch: {name}")
        api_md5 = api_files[name]["checksum"].split(":", 1)[1].lower()
        if result["md5"] != api_md5:
            raise RuntimeError(f"Public API checksum mismatch: {name}")
        files[name] = result
        if data is not None:
            captured[name] = data

    source_zip = inspect_remote_zip(captured[ZIP_NAME], TEMP_ROOT / ZIP_NAME)
    controls_zip = inspect_remote_controls(captured[CONTROLS_NAME])
    predecessor = fetch_json(
        f"https://zenodo.org/api/records/{PREDECESSOR_RECORD}"
    )
    predecessor_names = {row["key"] for row in predecessor["files"]}
    retained = predecessor_names - {CONTROLS_NAME}
    if len(retained) != 67:
        raise RuntimeError("Retained predecessor boundary mismatch")

    result = {
        "status": "PASS_PUBLIC_READBACK",
        "record_id": record_id,
        "record_url": f"https://zenodo.org/records/{record_id}",
        "doi": f"10.5281/zenodo.{record_id}",
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "github_commit": GITHUB_COMMIT,
        "outer_files": len(files),
        "outer_bytes": sum(int(row["bytes"]) for row in files.values()),
        "retained_predecessor_files": len(retained),
        "new_files": [PDF_NAME, TEX_NAME, ZIP_NAME],
        "replaced_files": [CONTROLS_NAME],
        "default_preview_expected": DEFAULT_PREVIEW,
        "file_readback": files,
        "sga7_zip_readback": source_zip,
        "controls_zip_readback": controls_zip,
        "duplicate_concept_created": False,
        "second_draft_created": False,
        "errors": [],
    }
    RECEIPT_ROOT.mkdir(parents=True, exist_ok=True)
    receipt = (
        RECEIPT_ROOT
        / f"20260730_sga7i_partial_transcription_record_{record_id}_public_readback.json"
    )
    receipt.write_bytes(json_bytes(result))
    return {**result, "receipt_path": str(receipt)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("prepare", "readback"))
    parser.add_argument("--record", type=int)
    args = parser.parse_args()
    if args.command == "prepare":
        result = prepare()
    else:
        if args.record is None:
            parser.error("readback requires --record")
        result = readback(args.record)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
