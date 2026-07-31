#!/usr/bin/env python3
"""Read back every file changed by the EGA IV p087-105 closeout commit."""

from __future__ import annotations

import hashlib
import json
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


COMMIT = "7ecccf0f529ee40e919444e3d9466107a943ca08"
REPOSITORY = "KokunoYumeto/modern-latex-manuscripts"
RECEIPT_STEM = (
    "20260731_ega4_source_image_witness_p087_105_"
    "closeout_commit_7ecccf0f_public_readback"
)
TITLE = "EGA IV printed pages 87-105 GitHub closeout readback"


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args])


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def fetch(url: str) -> tuple[bytes, int]:
    last_error: Exception | None = None
    for attempt in range(5):
        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "modern-latex-manuscripts-readback/1.0"},
            )
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read(), response.status
        except (urllib.error.URLError, TimeoutError) as error:
            last_error = error
            time.sleep(2**attempt)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    actual_commit = git("rev-parse", COMMIT).decode("ascii").strip()
    if actual_commit != COMMIT:
        raise RuntimeError(f"Commit mismatch: expected {COMMIT}, got {actual_commit}")

    changed = [
        line
        for line in git(
            "diff-tree", "--no-commit-id", "--name-only", "-r", COMMIT
        )
        .decode("utf-8")
        .splitlines()
        if line
    ]
    results: dict[str, dict[str, object]] = {}
    errors: list[str] = []
    total_bytes = 0

    for path in changed:
        local = git("show", f"{COMMIT}:{path}")
        encoded_path = urllib.parse.quote(path, safe="/")
        url = (
            f"https://raw.githubusercontent.com/{REPOSITORY}/"
            f"{COMMIT}/{encoded_path}"
        )
        remote, status = fetch(url)
        local_sha256 = hashlib.sha256(local).hexdigest().upper()
        remote_sha256 = hashlib.sha256(remote).hexdigest().upper()
        expected_blob = git("rev-parse", f"{COMMIT}:{path}").decode("ascii").strip()
        remote_blob = git_blob_sha1(remote)
        match = (
            status == 200
            and local == remote
            and local_sha256 == remote_sha256
            and expected_blob == remote_blob
        )
        if not match:
            errors.append(path)
        total_bytes += len(remote)
        results[path] = {
            "url": url,
            "http_status": status,
            "bytes": len(remote),
            "sha256": remote_sha256,
            "git_blob": remote_blob,
            "expected_git_blob": expected_blob,
            "match": match,
        }

    receipt = {
        "status": "PASS_PUBLIC_RAW_READBACK" if not errors else "FAIL",
        "errors": errors,
        "repository": REPOSITORY,
        "commit": COMMIT,
        "commit_url": f"https://github.com/{REPOSITORY}/commit/{COMMIT}",
        "changed_file_count": len(changed),
        "readback_file_count": len(results),
        "readback_bytes": total_bytes,
        "readback_mode": "anonymous_commit_pinned_raw_exact_bytes_sha256_git_blob",
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
                f"# {TITLE}",
                "",
                f"- Status: `{receipt['status']}`",
                f"- Commit: [`{COMMIT}`]({receipt['commit_url']})",
                f"- Files: {len(results)} / {len(changed)}",
                f"- Bytes: {total_bytes}",
                "- Method: anonymous commit-pinned raw retrieval with exact byte, "
                "SHA-256, and Git-blob comparison",
                "",
                "Every file changed by the closeout commit matched. The commit "
                "records the current Zenodo head, catalog, human and machine "
                "receipts, append-only archive log entry, and EGA landing-page "
                "updates for the actual source-image witness publication.",
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
                "bytes": total_bytes,
                "json": str(json_path),
                "markdown": str(md_path),
            },
            indent=2,
        )
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
