#!/usr/bin/env python3
"""Read back the SGA7 II through Expose XXI 4 GitHub publication."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


SOURCE_COMMIT = "508c171649722b2ec52459847344009b40fc7b29"
MERGE_COMMIT = "b8eb3dcf25d48d43a9fca382ce8b850774f9ed19"
PULL_REQUEST = 247
REPOSITORY = "KokunoYumeto/modern-latex-manuscripts"
RECEIPT_STEM = (
    "20260802_sga7ii_english_expose_xxi_4_"
    "commit_b8eb3dcf2_public_readback"
)


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=root)


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def fetch(url: str) -> tuple[bytes, int]:
    last_error: Exception | None = None
    for attempt in range(6):
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "modern-latex-manuscripts-readback/1.0"},
            )
            with urllib.request.urlopen(request, timeout=120) as response:
                return response.read(), response.status
        except (urllib.error.URLError, TimeoutError) as error:
            last_error = error
            time.sleep(2**attempt)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def raw_url(commit: str, path: str) -> str:
    encoded_path = urllib.parse.quote(path, safe="/")
    return f"https://raw.githubusercontent.com/{REPOSITORY}/{commit}/{encoded_path}"


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    for expected in (SOURCE_COMMIT, MERGE_COMMIT):
        actual = git(root, "rev-parse", expected).decode("ascii").strip()
        if actual != expected:
            raise RuntimeError(f"Commit mismatch: expected {expected}, got {actual}")

    changed = sorted(
        line
        for line in git(
            root,
            "diff-tree",
            "--no-commit-id",
            "--name-only",
            "--diff-filter=AM",
            "-r",
            SOURCE_COMMIT,
        )
        .decode("utf-8")
        .splitlines()
        if line
    )
    results: dict[str, dict[str, object]] = {}
    errors: list[str] = []
    total_bytes = 0
    aggregate_rows: list[str] = []

    for path in changed:
        source_local = git(root, "show", f"{SOURCE_COMMIT}:{path}")
        merge_local = git(root, "show", f"{MERGE_COMMIT}:{path}")
        source_remote, source_status = fetch(raw_url(SOURCE_COMMIT, path))
        merge_remote, merge_status = fetch(raw_url(MERGE_COMMIT, path))

        source_sha256 = hashlib.sha256(source_remote).hexdigest().upper()
        merge_sha256 = hashlib.sha256(merge_remote).hexdigest().upper()
        source_blob = git(root, "rev-parse", f"{SOURCE_COMMIT}:{path}").decode("ascii").strip()
        merge_blob = git(root, "rev-parse", f"{MERGE_COMMIT}:{path}").decode("ascii").strip()
        source_remote_blob = git_blob_sha1(source_remote)
        merge_remote_blob = git_blob_sha1(merge_remote)
        match = (
            source_status == 200
            and merge_status == 200
            and source_local == source_remote
            and merge_local == merge_remote
            and source_local == merge_local
            and source_sha256 == merge_sha256
            and source_blob == source_remote_blob
            and merge_blob == merge_remote_blob
        )
        if not match:
            errors.append(path)
        total_bytes += len(source_remote)
        aggregate_rows.append(f"{path}\t{len(source_remote)}\t{source_sha256}\n")
        results[path] = {
            "bytes": len(source_remote),
            "sha256": source_sha256,
            "source_url": raw_url(SOURCE_COMMIT, path),
            "merge_url": raw_url(MERGE_COMMIT, path),
            "source_http_status": source_status,
            "merge_http_status": merge_status,
            "source_git_blob": source_remote_blob,
            "merge_git_blob": merge_remote_blob,
            "source_merge_and_public_match": match,
        }

    aggregate_sha256 = hashlib.sha256(
        "".join(aggregate_rows).encode("utf-8")
    ).hexdigest().upper()
    receipt = {
        "status": "PASS_PUBLIC_RAW_READBACK" if not errors else "FAIL",
        "errors": errors,
        "repository": REPOSITORY,
        "pull_request": PULL_REQUEST,
        "pull_request_url": f"https://github.com/{REPOSITORY}/pull/{PULL_REQUEST}",
        "source_commit": SOURCE_COMMIT,
        "source_commit_url": f"https://github.com/{REPOSITORY}/commit/{SOURCE_COMMIT}",
        "merge_commit": MERGE_COMMIT,
        "merge_commit_url": f"https://github.com/{REPOSITORY}/commit/{MERGE_COMMIT}",
        "changed_file_count": len(changed),
        "readback_file_count": len(results),
        "readback_bytes_per_commit": total_bytes,
        "canonical_path_bytes_sha256_row_aggregate": aggregate_sha256,
        "readback_mode": (
            "anonymous_source_and_merge_commit_pinned_raw_exact_bytes_"
            "sha256_git_blob"
        ),
        "files": results,
    }

    out_dir = root / "manifests" / "published-github"
    json_path = out_dir / f"{RECEIPT_STEM}.json"
    md_path = out_dir / f"{RECEIPT_STEM}.md"
    json_path.write_text(
        json.dumps(receipt, ensure_ascii=True, indent=2) + "\n", encoding="utf-8"
    )
    md_path.write_text(
        "\n".join(
            [
                "# SGA7 II through Expose XXI Section 4 GitHub readback",
                "",
                f"- Status: `{receipt['status']}`",
                f"- Pull request: [#{PULL_REQUEST}]({receipt['pull_request_url']})",
                f"- Source commit: [`{SOURCE_COMMIT}`]({receipt['source_commit_url']})",
                f"- Merge commit: [`{MERGE_COMMIT}`]({receipt['merge_commit_url']})",
                f"- Files: {len(results)} / {len(changed)} at both commits",
                f"- Bytes per commit: {total_bytes}",
                f"- Canonical path/byte/SHA-256 row aggregate: `{aggregate_sha256}`",
                "- Method: anonymous commit-pinned raw retrieval with exact byte, "
                "SHA-256, and Git-blob comparison at source and merge commits",
                "",
                "The readback covers the cumulative reader, buildable source, compact "
                "reader/source ZIP, source-audit image ZIP, controls, and builders.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print(
        json.dumps(
            {
                "status": receipt["status"],
                "files": len(results),
                "bytes_per_commit": total_bytes,
                "aggregate_sha256": aggregate_sha256,
                "json": str(json_path),
                "markdown": str(md_path),
            },
            indent=2,
        )
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
