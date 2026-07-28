#!/usr/bin/env python3
"""Verify every added or modified file in a commit by anonymous GitHub readback."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args])


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()


def raw_url(repository: str, commit: str, path: str) -> str:
    encoded_path = "/".join(
        urllib.parse.quote(part, safe="") for part in path.split("/")
    )
    return (
        f"https://raw.githubusercontent.com/{repository}/{commit}/"
        f"{encoded_path}"
    )


def download(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "modern-latex-manuscripts-readback/1.0"},
    )
    last_error: Exception | None = None
    for attempt in range(6):
        try:
            with urllib.request.urlopen(request, timeout=300) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError) as error:
            last_error = error
            if attempt == 5:
                break
            time.sleep(2**attempt)
    raise RuntimeError(f"Readback failed for {url}: {last_error}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    commit = git("rev-parse", args.commit).decode("ascii").strip()
    changed = git(
        "diff-tree",
        "--no-commit-id",
        "--name-only",
        "--diff-filter=AM",
        "-r",
        commit,
    ).decode("utf-8")
    paths = [line for line in changed.splitlines() if line]
    if not paths:
        raise RuntimeError(f"Commit {commit} has no added or modified files")

    files: dict[str, dict[str, object]] = {}
    errors: list[str] = []
    for index, path in enumerate(paths, start=1):
        local = git("show", f"{commit}:{path}")
        url = raw_url(args.repository, commit, path)
        print(f"READBACK {index}/{len(paths)} {path}", flush=True)
        remote = download(url)
        match = remote == local
        if not match:
            errors.append(f"identity mismatch: {path}")
        files[path] = {
            "bytes": len(remote),
            "sha256": sha256(remote),
            "url": url,
            "match": match,
        }

    receipt = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "repository": args.repository,
        "commit": commit,
        "changed_file_count": len(paths),
        "changed_file_bytes": sum(
            int(row["bytes"]) for row in files.values()
        ),
        "files": files,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(receipt, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "status": receipt["status"],
                "commit": commit,
                "changed_files": len(paths),
                "output": str(args.output),
            },
            indent=2,
        ),
        flush=True,
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
