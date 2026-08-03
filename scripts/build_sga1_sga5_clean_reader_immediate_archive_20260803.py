#!/usr/bin/env python3
"""Build the privacy-clean immediate SGA1/SGA5 reader replacement payload."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
SOURCE_ROOT_TEXT = os.environ.get("SGA_CLEAN_READER_SOURCE_ROOT", "")
PRIVATE_PERSON_NAME = os.environ.get("SGA_PRIVATE_PERSON_NAME", "")
PROJECT = Path(SOURCE_ROOT_TEXT or "__SGA_CLEAN_READER_SOURCE_ROOT_REQUIRED__")
SGA1 = PROJECT / "sga1_reader_clean_r3"
SGA5 = PROJECT / "sga5_reader_clean_r10"
OUTPUT = REPO / "sources/sga/sga1-sga5-clean-reader-surfaces-20260803-r1"

PDF_SOURCES = {
    "00a_SGA1_English_Reader.pdf": SGA1 / "build_r3/SGA1_English_Reader_Clean_r3.pdf",
    "00e_SGA5_English_Reader.pdf": SGA5 / "build_r10/SGA5_English_Reader_Clean_r10.pdf",
}
TEXT_SOURCES = {
    "90a_SGA1_Clean_Reader_Validation_20260803.json": SGA1 / "controls/FINAL_STANDALONE_VALIDATION.json",
    "90b_SGA1_Reader_Prose_Removals_20260803.csv": SGA1 / "controls/READER_PROSE_REMOVALS_R3.csv",
    "90c_SGA1_Removed_Reader_Prose_History_20260803.texfrag": SGA1 / "controls/REMOVED_READER_PROSE_SGA1_007_008.texfrag",
    "90d_SGA5_Clean_Reader_Validation_20260803.json": SGA5 / "controls/FINAL_STANDALONE_VALIDATION.json",
    "90e_SGA5_Reader_Prose_Removals_20260803.csv": SGA5 / "controls/READER_PROSE_REMOVALS_R10.csv",
    "90f_SGA5_Removed_Reader_Prose_History_20260803.texfrag": SGA5 / "controls/REMOVED_READER_PROSE_SGA5_001_002.texfrag",
}
EXPECTED_PDFS = {
    "00a_SGA1_English_Reader.pdf": (2_538_547, "9D2BA160136F26A805AD3C7A949D5F7D3BC3E0B5521259C451C1EE798CAC72BF"),
    "00e_SGA5_English_Reader.pdf": (2_430_864, "07FD779DD32DBBBCAA482C062D73222A9DFD8EF478344846CE6A000144CBDFE2"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def sanitize(value: object, changes: list[dict], private_name: str, json_path: str = "$") -> object:
    if isinstance(value, dict):
        cleaned: dict[str, object] = {}
        for key, item in value.items():
            new_key = key
            if key.casefold() == private_name.casefold():
                new_key = "private_name_pattern"
                changes.append({"json_path": f"{json_path}.{new_key}", "action": "replace_private_name_pattern_key"})
            elif key.casefold() == f"under {private_name}".casefold():
                new_key = "under private-name pattern"
                changes.append({"json_path": f"{json_path}.{new_key}", "action": "replace_private_name_pattern_key"})
            cleaned[new_key] = sanitize(item, changes, private_name, f"{json_path}.{new_key}")
        return cleaned
    if isinstance(value, list):
        return [sanitize(item, changes, private_name, f"{json_path}[{index}]") for index, item in enumerate(value)]
    if isinstance(value, str) and re.search(re.escape(private_name), value, flags=re.IGNORECASE):
        cleaned = re.sub(re.escape(private_name) + r"'s", "the archive owner's", value, flags=re.IGNORECASE)
        cleaned = re.sub(re.escape(private_name), "the archive owner", cleaned, flags=re.IGNORECASE)
        changes.append({"json_path": json_path, "action": "replace_private_person_name"})
        return cleaned
    return value


def privacy_hits(path: Path, private_name: str) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    return {
        "absolute_windows_path": len(re.findall(r"(?<![A-Za-z])[A-Z]:[\\/]", text)),
        "private_person_name": len(re.findall(re.escape(private_name), text, flags=re.IGNORECASE)),
        "email": len(re.findall(r"(?i)[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", text)),
        "bearer_token": len(re.findall(r"(?i)Bearer\s+[A-Za-z0-9._-]{20,}", text)),
    }


def main() -> None:
    if not SOURCE_ROOT_TEXT or not PRIVATE_PERSON_NAME:
        raise RuntimeError(
            "Set SGA_CLEAN_READER_SOURCE_ROOT and SGA_PRIVATE_PERSON_NAME to the exact private source controls."
        )
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / ".gitattributes").write_text("*.pdf -text\n*.csv -text\n*.json -text\n*.texfrag -text\n", encoding="utf-8", newline="\n")
    for name, source in PDF_SOURCES.items():
        if (source.stat().st_size, sha256(source)) != EXPECTED_PDFS[name]:
            raise RuntimeError(f"Clean PDF identity changed: {name}")
        shutil.copyfile(source, OUTPUT / name)

    transformations: list[dict[str, object]] = []
    for name, source in TEXT_SOURCES.items():
        target = OUTPUT / name
        if source.suffix == ".json":
            source_data = json.loads(source.read_text(encoding="utf-8"))
            changes: list[dict] = []
            cleaned = sanitize(source_data, changes, PRIVATE_PERSON_NAME)
            target.write_text(json.dumps(cleaned, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
            transformations.append(
                {
                    "public_path": name,
                    "source_bytes": source.stat().st_size,
                    "source_sha256": sha256(source),
                    "public_bytes": target.stat().st_size,
                    "public_sha256": sha256(target),
                    "actions": changes,
                }
            )
        else:
            shutil.copyfile(source, target)
            transformations.append(
                {
                    "public_path": name,
                    "source_bytes": source.stat().st_size,
                    "source_sha256": sha256(source),
                    "public_bytes": target.stat().st_size,
                    "public_sha256": sha256(target),
                    "actions": [],
                }
            )

    transform_path = OUTPUT / "90g_Clean_Reader_Privacy_Transformations_20260803.csv"
    with transform_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["public_path", "source_bytes", "source_sha256", "public_bytes", "public_sha256", "action_count", "actions"],
            lineterminator="\n",
        )
        writer.writeheader()
        for row in transformations:
            writer.writerow(
                {
                    "public_path": row["public_path"],
                    "source_bytes": row["source_bytes"],
                    "source_sha256": row["source_sha256"],
                    "public_bytes": row["public_bytes"],
                    "public_sha256": row["public_sha256"],
                    "action_count": len(row["actions"]),
                    "actions": json.dumps(row["actions"], ensure_ascii=False, separators=(",", ":")),
                }
            )

    manifest_path = OUTPUT / "90h_Clean_Reader_Public_Manifest_20260803.csv"
    manifest_members = sorted(
        (path for path in OUTPUT.iterdir() if path.is_file() and path.name not in {manifest_path.name, ".gitattributes"}),
        key=lambda path: path.name.casefold(),
    )
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["filename", "bytes", "sha256", "role"], lineterminator="\n")
        writer.writeheader()
        for path in manifest_members:
            role = "reader_pdf" if path.suffix.lower() == ".pdf" else "external_provenance_control"
            writer.writerow({"filename": path.name, "bytes": path.stat().st_size, "sha256": sha256(path), "role": role})

    text_files = [path for path in OUTPUT.iterdir() if path.is_file() and path.suffix.lower() != ".pdf"]
    residuals = {path.name: privacy_hits(path, PRIVATE_PERSON_NAME) for path in text_files}
    nonzero = {name: hits for name, hits in residuals.items() if any(hits.values())}
    if nonzero:
        raise RuntimeError(f"Privacy residuals: {nonzero}")
    files = sorted((path for path in OUTPUT.iterdir() if path.is_file() and path.name != ".gitattributes"), key=lambda path: path.name.casefold())
    if len(files) != 10:
        raise RuntimeError(f"Expected ten upload files, found {len(files)}")
    print(
        json.dumps(
            {
                "status": "PASS",
                "output": str(OUTPUT),
                "upload_files": len(files),
                "upload_bytes": sum(path.stat().st_size for path in files),
                "files": {path.name: {"bytes": path.stat().st_size, "sha256": sha256(path)} for path in files},
                "privacy_residuals": nonzero,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
