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
STACKS_BOARD_ID = "stacks-commons-layer"


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


def stacks_claim_body() -> str:
    return f"""### Board ID
{STACKS_BOARD_ID}

### Intent
Start one bounded Commons-owned Stacks reference-layer implementation.

### Exact scope
Bind one exact upstream pin and one new Commons-owned overlay namespace; do not modify upstream or another task's files.

### Starting evidence
Exact repository URL, applicable license identity, 40-hex commit, overlay namespace, composition plan, tests, and synchronization cursor.

### Commons writer identity
example-maintainer

### Exact upstream repository URL
https://github.com/example/stacks-upstream

### Applicable upstream license identity
COPYING at the exact upstream commit

### Exact upstream commit
0123456789abcdef0123456789abcdef01234567

### Commons overlay namespace
commons/stacks/pilot

### Deterministic composition
Pin upstream, apply the named overlay without rewriting either input, and hash the composed output.

### Tests and review plan
Run exact-input, namespace, attribution, conflict, and deterministic-rebuild checks; retain review receipts.

### Starting synchronization cursor
Initial exact upstream pin; no earlier Commons overlay generation is claimed.

### Traceability
- [x] I will write only to the declared Commons-owned namespace and will not edit upstream or another task's files.
- [x] I will preserve exact upstream and predecessor identities, conflicts, failures, corrections, and reversals.
- [x] I will not imply upstream acceptance, approval, endorsement, or a motive for prior contribution outcomes.
- [x] Any public modified edition will be distinctly titled and will preserve applicable attribution, license, and history notices.
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
    environment["PYTHONUTF8"] = "1"
    environment["PYTHONIOENCODING"] = "utf-8"
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
        issue(12, "[Adopt] Stacks Commons layer — bounded fixture", stacks_claim_body(), "open"),
    ]
    invalid_stacks = stacks_claim_body().replace(
        "### Exact upstream commit\n0123456789abcdef0123456789abcdef01234567",
        "### Exact upstream commit\n_No response_",
    )
    invalid_fixture = [
        issue(13, "[Adopt] unknown board row", claim_body("not-a-board-row"), "open"),
        issue(14, "[Adopt] Stacks Commons layer — invalid fixture", invalid_stacks, "open"),
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
        expected = {"issues": 3, "claims": 2, "handbacks": 1, "valid": 3, "invalid": 0}
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
        if invalid_aggregate.get("issues") != 2 or invalid_aggregate.get("invalid") != 2:
            raise RuntimeError(f"invalid fixture aggregate mismatch: {invalid_aggregate}")
        if not any("unknown Board ID: not-a-board-row" in error for error in invalid_report.get("errors", [])):
            raise RuntimeError("invalid fixture did not preserve the unknown Board-ID error")
        if not any("missing required Stacks section: Exact upstream commit" in error for error in invalid_report.get("errors", [])):
            raise RuntimeError("invalid fixture did not fail closed on a missing Stacks commit")

    print(
        json.dumps(
            {
                "status": "PASS",
                "commit": args.commit.lower(),
                "valid_fixture": {"issues": 3, "valid": 3, "errors": 0},
                "invalid_fixture": {"issues": 2, "invalid": 2, "exit": 1},
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
