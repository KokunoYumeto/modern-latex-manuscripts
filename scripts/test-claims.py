#!/usr/bin/env python3
"""Replay valid and invalid adoption-issue lifecycle fixtures offline."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


DEFAULT_REPOSITORY = "KokunoYumeto/modern-latex-manuscripts"
COMMIT_RE = re.compile(r"^[0-9a-fA-F]{40}$")
BOARD_ID = "gauss-werke-ii"


def issue(number: int, title: str, body: str, state: str) -> dict:
    return {
        "number": number,
        "title": title,
        "body": body,
        "state": state,
        "html_url": f"https://github.com/{DEFAULT_REPOSITORY}/issues/{number}",
        "updated_at": "2026-08-09T00:00:00Z",
    }


def claim_body(board_id: str) -> str:
    return f"""### Board ID
{board_id}

### Intent
Independently mirror/check existing work

### Exact scope
Gauss, Werke II, one bounded page range from the declared cursor.

### Starting evidence
One exact approved Git commit, mapped source paths, byte lengths, and SHA-256 values.

### Traceability
- [x] I will preserve predecessors and declare overlap rather than silently overwriting existing work.
- [x] I understand that opening this issue does not reserve the scope exclusively.
"""


def handback_body(repository: str) -> str:
    return f"""### Board ID
{BOARD_ID}

### Adoption issue or mirror URL
https://github.com/{repository}/issues/10

### Handback state
returned — bounded result

### Exact achieved scope
One bounded page range; no broader completion claim.

### Inspectable result
https://github.com/example/mirror/commit/0123456789012345678901234567890123456789

### Manifest and identities
result.tex, 123 bytes, SHA-256 0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF.

### Checks, failures, and reversals
Exact inputs replayed; one retained unresolved source ambiguity.

### Continuation cursor
The next printed page after the bounded result.

### Reusable workflow findings
Keep the source ambiguity explicit in parallel mirrors.

### Preservation and status
- [x] I preserved the starting generation.
- [x] I kept quality state explicit.
- [x] I returned inspectable evidence.
"""


def run_auditor(
    checker: Path,
    repository: str,
    commit: str,
    git_root: Path,
    fixture: Path,
) -> subprocess.CompletedProcess[bytes]:
    environment = os.environ.copy()
    environment.pop("GITHUB_TOKEN", None)
    environment["HTTP_PROXY"] = "http://127.0.0.1:9"
    environment["HTTPS_PROXY"] = "http://127.0.0.1:9"
    environment["ALL_PROXY"] = "http://127.0.0.1:9"
    return subprocess.run(
        [
            sys.executable,
            str(checker),
            "--repository",
            repository,
            "--commit",
            commit,
            "--approve",
            commit,
            "--git",
            str(git_root),
            "--issues-file",
            str(fixture),
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=60,
        env=environment,
    )


def parse_report(result: subprocess.CompletedProcess[bytes], context: str) -> dict:
    try:
        return json.loads(result.stdout.decode("utf-8"))
    except Exception as error:
        diagnostic = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"{context} did not emit a JSON report: {diagnostic}") from error


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--repository", default=DEFAULT_REPOSITORY)
    parser.add_argument("--git", default=".", help="Checkout or bare Git repository root")
    args = parser.parse_args()
    if not COMMIT_RE.fullmatch(args.commit):
        parser.error("--commit must be exactly 40 hexadecimal characters")

    git_root = Path(args.git).resolve(strict=True)
    checker = Path(__file__).with_name("check-claims.py").resolve(strict=True)
    valid_fixture = [
        issue(10, "[Adopt] bounded Gauss mirror", claim_body(BOARD_ID), "open"),
        issue(11, "[Handback] bounded Gauss mirror", handback_body(args.repository), "closed"),
    ]
    invalid_fixture = [
        issue(12, "[Adopt] unknown board row", claim_body("not-a-board-row"), "open")
    ]

    with tempfile.TemporaryDirectory(prefix="adopt-claims-") as temporary:
        root = Path(temporary)
        valid_path = root / "valid.json"
        invalid_path = root / "invalid.json"
        valid_path.write_text(
            json.dumps(valid_fixture, ensure_ascii=True, separators=(",", ":")) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        invalid_path.write_text(
            json.dumps(invalid_fixture, ensure_ascii=True, separators=(",", ":")) + "\n",
            encoding="utf-8",
            newline="\n",
        )

        valid = run_auditor(checker, args.repository, args.commit.lower(), git_root, valid_path)
        valid_report = parse_report(valid, "valid claim/handback fixture")
        if valid.returncode != 0:
            raise RuntimeError("valid claim/handback fixture was rejected")
        if valid_report.get("status") != "PASS" or valid_report.get("errors") != []:
            raise RuntimeError("valid claim/handback fixture did not return PASS/errors[]")
        aggregate = valid_report.get("aggregate", {})
        expected = {"issues": 2, "claims": 1, "handbacks": 1, "valid": 2, "invalid": 0}
        if any(aggregate.get(key) != value for key, value in expected.items()):
            raise RuntimeError(f"valid fixture aggregate mismatch: {aggregate}")
        if valid_report.get("board", {}).get("transport") != "local_git_object_database":
            raise RuntimeError("valid fixture did not use the local Git board transport")
        if valid_report.get("issue_source", {}).get("kind") != "json_fixture":
            raise RuntimeError("valid fixture did not report the JSON issue transport")
        if valid_report.get("checks", {}).get("external_network_queried") is not False:
            raise RuntimeError("valid fixture did not remain fully offline")

        invalid = run_auditor(checker, args.repository, args.commit.lower(), git_root, invalid_path)
        invalid_report = parse_report(invalid, "invalid Board-ID fixture")
        if invalid.returncode != 1 or invalid_report.get("status") != "FAIL":
            raise RuntimeError("invalid Board-ID fixture did not fail closed with exit 1")
        invalid_aggregate = invalid_report.get("aggregate", {})
        if invalid_aggregate.get("issues") != 1 or invalid_aggregate.get("invalid") != 1:
            raise RuntimeError(f"invalid fixture aggregate mismatch: {invalid_aggregate}")
        if not any("unknown Board ID: not-a-board-row" in error for error in invalid_report.get("errors", [])):
            raise RuntimeError("invalid fixture did not preserve the unknown Board-ID error")

    print(
        json.dumps(
            {
                "status": "PASS",
                "commit": args.commit.lower(),
                "valid_fixture": {"issues": 2, "valid": 2, "errors": 0},
                "invalid_fixture": {"issues": 1, "invalid": 1, "exit": 1},
                "board_transport": "local_git_object_database",
                "issue_transport": "json_fixture",
                "external_network_queried": False,
            },
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
