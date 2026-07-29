#!/usr/bin/env python3
"""Pack the loose canonical SGA release controls into one deterministic ZIP."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import shutil
import urllib.request
import zipfile
from pathlib import Path, PurePosixPath


REPO = Path(__file__).resolve().parents[1]
OUTPUT = (
    REPO
    / "sources"
    / "sga"
    / "sga-canonical-release-controls-compact-20260729"
)
ZIP_NAME = "10z_SGA_Current_Release_Controls_20260729.zip"
ZIP_TIME = (2026, 7, 29, 0, 0, 0)
RECORD_ID = 21683140
RAW_ROOT = f"https://zenodo.org/api/records/{RECORD_ID}/files"
CONTROLS = {
    "09_README_CURRENT_RELEASE.md": (
        1_162,
        "F29777968A96534331357D67B4ACEF7F1B1A8BC24F1F306D650A9B2FA9C6E5CD",
    ),
    "09a_RELEASE_FILE_MANIFEST.csv": (
        14_208,
        "E552C0D7A05F2E4FADFEAF198772854220464509CEC685521BFBCC2167178C38",
    ),
    "09b_RELEASE_VALIDATION.json": (
        1_952,
        "33283DBA919B606A0C62EB556110000457B694DA2A881ECCD2F7D891867D0CE7",
    ),
}
PRIVATE_PATTERNS = {
    "private_home": re.compile(rb"C:\\Users\\Floris", re.IGNORECASE),
    "private_github": re.compile(rb"C:\\IL_GitHub", re.IGNORECASE),
    "papors": re.compile(rb"Papors", re.IGNORECASE),
    "chatnotes": re.compile(rb"Chatnotes", re.IGNORECASE),
    "codex_thread": re.compile(
        rb"\b019[0-9a-f]{5}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
        re.IGNORECASE,
    ),
}
AI_PATTERNS = {
    "openai": re.compile(rb"\bOpenAI\b", re.IGNORECASE),
    "chatgpt": re.compile(rb"\bChatGPT\b", re.IGNORECASE),
    "codex": re.compile(rb"\bCodex\b", re.IGNORECASE),
    "claude": re.compile(rb"\bClaude\b", re.IGNORECASE),
    "anthropic": re.compile(rb"\bAnthropic\b", re.IGNORECASE),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def csv_bytes(fieldnames: list[str], rows: list[dict[str, object]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode("utf-8")


def fetch_controls() -> dict[str, bytes]:
    result: dict[str, bytes] = {}
    errors: list[str] = []
    for name, (expected_bytes, expected_sha256) in CONTROLS.items():
        request = urllib.request.Request(
            f"{RAW_ROOT}/{name}/content",
            headers={"User-Agent": "modern-latex-manuscripts-readback"},
        )
        with urllib.request.urlopen(request, timeout=180) as response:
            data = response.read()
        actual = (len(data), sha256_bytes(data))
        if actual != (expected_bytes, expected_sha256):
            errors.append(
                f"{name}: expected {(expected_bytes, expected_sha256)}, got {actual}"
            )
        result[name] = data
    if errors:
        raise RuntimeError("\n".join(errors))
    return result


def scan_controls(controls: dict[str, bytes]) -> dict[str, object]:
    hits: list[dict[str, str]] = []
    for name, data in controls.items():
        for pattern_name, pattern in {**PRIVATE_PATTERNS, **AI_PATTERNS}.items():
            if pattern.search(data):
                hits.append({"member": name, "pattern": pattern_name})
    if hits:
        raise RuntimeError(f"control privacy/AI scan failed: {hits}")
    return {
        "text_members_scanned": len(controls),
        "hits": hits,
        "hit_count": len(hits),
    }


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    return info


def build_zip(controls: dict[str, bytes], destination: Path) -> dict[str, object]:
    rows = [
        {
            "relative_path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
            "source_record": RECORD_ID,
            "disposition": "packed_not_reader_facing",
        }
        for name, data in sorted(controls.items())
    ]
    members = dict(controls)
    members["PACKED_CONTROL_SHA256.csv"] = csv_bytes(
        [
            "relative_path",
            "bytes",
            "sha256",
            "source_record",
            "disposition",
        ],
        rows,
    )

    with zipfile.ZipFile(destination, "w", allowZip64=True) as archive:
        for name, data in sorted(members.items()):
            archive.writestr(
                zip_info(name),
                data,
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )

    errors: list[str] = []
    with zipfile.ZipFile(destination) as archive:
        bad = archive.testzip()
        if bad:
            errors.append(f"CRC failure: {bad}")
        names = archive.namelist()
        if len(names) != len(set(names)):
            errors.append("duplicate ZIP member names")
        if set(names) != set(members):
            errors.append("ZIP member set mismatch")
        for name in names:
            pure = PurePosixPath(name)
            if pure.is_absolute() or ".." in pure.parts or "\\" in name:
                errors.append(f"unsafe ZIP member name: {name}")
                continue
            if sha256_bytes(archive.read(name)) != sha256_bytes(members[name]):
                errors.append(f"ZIP member SHA-256 mismatch: {name}")
        uncompressed = sum(info.file_size for info in archive.infolist())
    if errors:
        raise RuntimeError("\n".join(errors))

    return {
        "filename": destination.name,
        "bytes": destination.stat().st_size,
        "sha256": sha256(destination),
        "members": len(members),
        "represented_controls": len(controls),
        "uncompressed_bytes": uncompressed,
        "crc_test": "PASS",
        "safe_member_names": True,
        "member_hash_readback": "PASS",
    }


def write_readme(zip_result: dict[str, object]) -> None:
    text = f"""# Compact SGA release controls

The canonical SGA Zenodo reader surface should expose only direct readers,
direct editable TeX masters, and grouped archives. This package moves the
three previously loose release-control files into one deterministic ZIP
without changing their bytes.

- ZIP: `{ZIP_NAME}`
- ZIP bytes: {zip_result["bytes"]}
- ZIP SHA-256: `{zip_result["sha256"]}`
- ZIP members: {zip_result["members"]}
- Represented predecessor controls: {zip_result["represented_controls"]}
- Uncompressed bytes: {zip_result["uncompressed_bytes"]}

The next same-concept Zenodo successor removes the three loose controls and
adds this ZIP. Every reader, direct TeX file, and unrelated archive is retained
byte-identically. Historical Zenodo versions remain immutable.
"""
    (OUTPUT / "README.md").write_text(text, encoding="utf-8", newline="\n")


def write_validation(
    scan: dict[str, object],
    zip_result: dict[str, object],
) -> None:
    validation = {
        "schema": "sga_compact_release_controls_v1",
        "status": "PASS",
        "errors": [],
        "concept_doi": "10.5281/zenodo.20410947",
        "source_record": RECORD_ID,
        "removed_loose_files": sorted(CONTROLS),
        "replacement_zip": zip_result,
        "privacy_and_ai": scan,
        "expected_successor": {
            "predecessor_files": 68,
            "retained_files": 65,
            "removed_files": 3,
            "added_files": 1,
            "final_files": 66,
            "readers_changed": 0,
            "direct_tex_changed": 0,
            "duplicate_concept_created": False,
        },
    }
    (OUTPUT / "PACKAGE_VALIDATION.json").write_text(
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def write_manifest() -> None:
    represented = [
        OUTPUT / ZIP_NAME,
        OUTPUT / "PACKAGE_VALIDATION.json",
        OUTPUT / "README.md",
    ]
    rows = [
        {
            "relative_path": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in represented
    ]
    with (OUTPUT / "SHA256SUMS.csv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["relative_path", "bytes", "sha256"],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    controls = fetch_controls()
    scan = scan_controls(controls)
    zip_result = build_zip(controls, OUTPUT / ZIP_NAME)
    write_readme(zip_result)
    write_validation(scan, zip_result)
    write_manifest()
    print(
        json.dumps(
            {
                "output": str(OUTPUT),
                "outer_files": 4,
                "outer_bytes": sum(
                    path.stat().st_size
                    for path in OUTPUT.iterdir()
                    if path.is_file()
                ),
                "zip": zip_result,
                "outer_manifest_sha256": sha256(OUTPUT / "SHA256SUMS.csv"),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
