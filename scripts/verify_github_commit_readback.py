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
    parser.add_argument(
        "--paths-from-commit",
        help=(
            "Optional commit whose added/modified path list should be read back "
            "from --commit. This supports merge commits whose tree contains an "
            "already-verified source commit but whose default diff is empty."
        ),
    )
    parser.add_argument(
        "--start-index",
        type=int,
        default=0,
        help="Zero-based first path to verify after Git path ordering.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help=(
            "Maximum paths to verify in this run. Commits with more than 25 "
            "paths require an explicit limit so large readbacks are chunked."
        ),
    )
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    commit = git("rev-parse", args.commit).decode("ascii").strip()
    paths_from_commit = git(
        "rev-parse", args.paths_from_commit or commit
    ).decode("ascii").strip()
    changed = git(
        "diff-tree",
        "--no-commit-id",
        "--name-only",
        "--diff-filter=AM",
        "-r",
        paths_from_commit,
    ).decode("utf-8")
    all_paths = [line for line in changed.splitlines() if line]
    if not all_paths:
        raise RuntimeError(f"Commit {commit} has no added or modified files")
    if args.start_index < 0:
        raise RuntimeError("--start-index must be non-negative")
    if args.limit is not None and args.limit <= 0:
        raise RuntimeError("--limit must be positive")
    if len(all_paths) > 25 and args.limit is None:
        raise RuntimeError(
            f"Refusing an unchunked {len(all_paths)}-path readback; "
            "provide --start-index and --limit (25 or fewer recommended)"
        )
    stop_index = (
        len(all_paths)
        if args.limit is None
        else min(len(all_paths), args.start_index + args.limit)
    )
    paths = all_paths[args.start_index:stop_index]
    if not paths:
        raise RuntimeError(
            f"Selected path range starts at {args.start_index}, but the commit "
            f"has only {len(all_paths)} added or modified paths"
        )

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
        "paths_from_commit": paths_from_commit,
        "total_changed_file_count": len(all_paths),
        "path_start_index": args.start_index,
        "path_end_index_exclusive": stop_index,
        "all_paths_covered": args.start_index == 0 and stop_index == len(all_paths),
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
