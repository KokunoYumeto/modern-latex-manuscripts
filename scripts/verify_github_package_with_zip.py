#!/usr/bin/env python3
"""Verify a GitHub package and one grouped ZIP by anonymous raw readback."""

from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def stream_remote(url: str, destination: Path | None = None) -> tuple[int, str]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "modern-latex-manuscripts-github-readback"},
    )
    digest = hashlib.sha256()
    byte_count = 0
    output = destination.open("wb") if destination is not None else None
    try:
        with urllib.request.urlopen(request, timeout=1200) as response:
            while chunk := response.read(1024 * 1024):
                byte_count += len(chunk)
                digest.update(chunk)
                if output is not None:
                    output.write(chunk)
    finally:
        if output is not None:
            output.close()
    return byte_count, digest.hexdigest().upper()


def zip_inventory(path: Path) -> dict[str, object]:
    members: list[dict[str, object]] = []
    with zipfile.ZipFile(path) as archive:
        bad_member = archive.testzip()
        for info in sorted(archive.infolist(), key=lambda item: item.filename):
            if info.is_dir():
                continue
            digest = hashlib.sha256(archive.read(info)).hexdigest().upper()
            members.append(
                {
                    "relative_path": info.filename.replace("\\", "/"),
                    "bytes": info.file_size,
                    "sha256": digest,
                }
            )
    return {
        "file_members": len(members),
        "uncompressed_bytes": sum(int(row["bytes"]) for row in members),
        "crc_error": bad_member,
        "members": members,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--package-path", required=True)
    parser.add_argument("--package-root", type=Path, required=True)
    parser.add_argument("--zip-name", required=True)
    parser.add_argument("--expected-outer-files", type=int, required=True)
    parser.add_argument("--expected-zip-members", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    root = args.package_root.resolve()
    files = sorted(path for path in root.iterdir() if path.is_file())
    errors: list[str] = []
    if len(files) != args.expected_outer_files:
        errors.append(
            f"outer file count: expected {args.expected_outer_files}, got {len(files)}"
        )
    zip_path = root / args.zip_name
    if not zip_path.is_file():
        errors.append(f"missing local ZIP: {args.zip_name}")
    if errors:
        raise SystemExit(json.dumps({"status": "FAIL", "errors": errors}, indent=2))

    local_zip = zip_inventory(zip_path)
    if local_zip["file_members"] != args.expected_zip_members:
        errors.append(
            "local ZIP member count: "
            f"expected {args.expected_zip_members}, got {local_zip['file_members']}"
        )

    outer: dict[str, dict[str, object]] = {}
    remote_zip: dict[str, object] | None = None
    with tempfile.TemporaryDirectory(prefix="github-package-readback-") as temp:
        temp_dir = Path(temp)
        for path in files:
            encoded_package_path = "/".join(
                urllib.parse.quote(part, safe="")
                for part in args.package_path.split("/")
            )
            encoded_name = urllib.parse.quote(path.name, safe="")
            url = (
                f"https://raw.githubusercontent.com/{args.repository}/"
                f"{args.commit}/{encoded_package_path}/{encoded_name}"
            )
            destination = temp_dir / "remote.zip" if path.name == args.zip_name else None
            remote_bytes, remote_sha256 = stream_remote(url, destination)
            local_identity = (path.stat().st_size, sha256_file(path))
            match = (remote_bytes, remote_sha256) == local_identity
            if not match:
                errors.append(f"outer identity mismatch: {path.name}")
            outer[path.name] = {
                "bytes": remote_bytes,
                "sha256": remote_sha256,
                "url": url,
                "match": match,
            }
            if destination is not None:
                remote_zip = zip_inventory(destination)
                destination.unlink(missing_ok=True)

    if remote_zip is None:
        errors.append("remote ZIP was not downloaded")
    elif remote_zip != local_zip:
        errors.append("remote ZIP member inventory mismatch")

    receipt = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "repository": args.repository,
        "commit": args.commit,
        "package_path": args.package_path,
        "outer_files": len(outer),
        "outer_readback": outer,
        "zip": remote_zip,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(receipt, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "status": receipt["status"],
                "errors": errors,
                "outer_files": len(outer),
                "zip_members": (
                    int(remote_zip["file_members"]) if remote_zip is not None else 0
                ),
                "zip_uncompressed_bytes": (
                    int(remote_zip["uncompressed_bytes"])
                    if remote_zip is not None
                    else 0
                ),
                "output": str(args.output),
            },
            indent=2,
        )
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
