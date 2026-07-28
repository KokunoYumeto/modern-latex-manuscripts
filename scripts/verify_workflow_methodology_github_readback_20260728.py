#!/usr/bin/env python3
"""Verify the corrected July 28 workflow package from anonymous GitHub."""

from __future__ import annotations

import hashlib
import io
import json
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


REPOSITORY = "KokunoYumeto/modern-latex-manuscripts"
COMMIT = "fb697af58c15d95f3c3dd7d5f7c7e05e463fe39b"
PACKAGE_PATH = "sources/workflow/ai-run-modern-latex-workflow-20260728"
EXPECTED_OUTER_FILES = 10
EXPECTED_ZIP_ARCHIVES = 2
EXPECTED_ZIP_FILE_MEMBERS = 28
EXPECTED_ZIP_DIRECTORY_ENTRIES = 0
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 836_257

REPO_ROOT = Path(__file__).resolve().parent.parent
PACKAGE_ROOT = REPO_ROOT / PACKAGE_PATH
OUTPUT = (
    REPO_ROOT
    / "manifests"
    / "published-github"
    / "20260728_workflow_methodology_commit_fb697af58_public_readback.json"
)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def safe_zip_name(name: str) -> None:
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts or "\\" in name:
        raise RuntimeError(f"Unsafe ZIP member: {name}")


def zip_members(value: bytes) -> tuple[list[dict], int, int]:
    rows = []
    directories = 0
    uncompressed = 0
    with zipfile.ZipFile(io.BytesIO(value), "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("ZIP CRC verification failed")
        for info in archive.infolist():
            safe_zip_name(info.filename)
            if info.is_dir():
                directories += 1
                continue
            content = archive.read(info.filename)
            rows.append(
                {
                    "relative_path": info.filename,
                    "bytes": len(content),
                    "sha256": sha256_bytes(content),
                }
            )
            uncompressed += len(content)
    return rows, directories, uncompressed


def session() -> requests.Session:
    value = requests.Session()
    retries = Retry(
        total=8,
        connect=8,
        read=8,
        status=8,
        backoff_factor=1.0,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
        raise_on_status=False,
    )
    value.mount("https://", HTTPAdapter(max_retries=retries))
    value.headers.update(
        {"User-Agent": "modern-latex-manuscripts-readback/1.0"}
    )
    return value


def main() -> None:
    paths = sorted(
        (path for path in PACKAGE_ROOT.iterdir() if path.is_file()),
        key=lambda path: path.name.casefold(),
    )
    if len(paths) != EXPECTED_OUTER_FILES:
        raise RuntimeError("Unexpected local workflow package file count")

    client = session()
    files = {}
    archives = []
    all_members = []
    zip_directories = 0
    zip_uncompressed = 0
    for index, path in enumerate(paths, start=1):
        local = path.read_bytes()
        url = (
            f"https://raw.githubusercontent.com/{REPOSITORY}/{COMMIT}/"
            f"{PACKAGE_PATH}/{quote(path.name)}"
        )
        print(f"READBACK {index}/{len(paths)} {path.name}", flush=True)
        response = client.get(url, timeout=(30, 600))
        response.raise_for_status()
        remote = response.content
        observed = {
            "bytes": len(remote),
            "sha256": sha256_bytes(remote),
            "url": url,
            "match": remote == local,
        }
        if not observed["match"]:
            raise RuntimeError(f"GitHub readback mismatch: {path.name}")
        files[path.name] = observed

        if path.suffix.lower() != ".zip":
            continue
        local_members, local_directories, local_uncompressed = zip_members(local)
        remote_members, remote_directories, remote_uncompressed = zip_members(
            remote
        )
        if (
            remote_members,
            remote_directories,
            remote_uncompressed,
        ) != (
            local_members,
            local_directories,
            local_uncompressed,
        ):
            raise RuntimeError(f"GitHub ZIP member mismatch: {path.name}")
        for row in remote_members:
            all_members.append({"archive": path.name, **row})
        archives.append(
            {
                "filename": path.name,
                "bytes": len(remote),
                "sha256": sha256_bytes(remote),
                "file_members": len(remote_members),
                "directory_entries": remote_directories,
                "uncompressed_bytes": remote_uncompressed,
                "errors": [],
            }
        )
        zip_directories += remote_directories
        zip_uncompressed += remote_uncompressed

    observed_zip = (
        len(archives),
        len(all_members),
        zip_directories,
        zip_uncompressed,
    )
    expected_zip = (
        EXPECTED_ZIP_ARCHIVES,
        EXPECTED_ZIP_FILE_MEMBERS,
        EXPECTED_ZIP_DIRECTORY_ENTRIES,
        EXPECTED_ZIP_UNCOMPRESSED_BYTES,
    )
    if observed_zip != expected_zip:
        raise RuntimeError(
            f"ZIP aggregate mismatch: {observed_zip} != {expected_zip}"
        )

    receipt = {
        "status": "PASS",
        "errors": [],
        "repository": REPOSITORY,
        "commit": COMMIT,
        "path": PACKAGE_PATH,
        "file_count": len(files),
        "bytes": sum(row["bytes"] for row in files.values()),
        "files": files,
        "zip_archive_count": len(archives),
        "zip_file_member_count": len(all_members),
        "zip_directory_entry_count": zip_directories,
        "zip_uncompressed_bytes": zip_uncompressed,
        "archives": archives,
        "members": all_members,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(receipt, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "status": receipt["status"],
                "commit": COMMIT,
                "files": len(files),
                "zip_archives": len(archives),
                "zip_members": len(all_members),
                "zip_uncompressed_bytes": zip_uncompressed,
                "output": str(OUTPUT),
            },
            indent=2,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
