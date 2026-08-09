#!/usr/bin/env python3
"""Audit public adoption and handback issues against one approved board commit."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
import urllib.parse
import urllib.request


DEFAULT_REPOSITORY = "KokunoYumeto/modern-latex-manuscripts"
COMMIT_RE = re.compile(r"^[0-9a-fA-F]{40}$")
BOARD_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SECTION_RE = re.compile(r"(?m)^### (?P<label>[^\r\n]+)\s*$")
CLAIM_REQUIRED = (
    "Board ID",
    "Intent",
    "Exact scope",
    "Starting evidence",
    "Traceability",
)
HANDBACK_REQUIRED = (
    "Board ID",
    "Adoption issue or mirror URL",
    "Handback state",
    "Exact achieved scope",
    "Inspectable result",
    "Manifest and identities",
    "Checks, failures, and reversals",
    "Continuation cursor",
    "Reusable workflow findings",
    "Preservation and status",
)
HANDBACK_STATES = {
    "returned — bounded result",
    "returned — partial checkpoint",
    "paused — open for continuation",
    "withdrawn — no result",
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def load_approved_board(repository: str, commit: str, approve: str) -> tuple[dict, dict]:
    helper = pathlib.Path(__file__).with_name("get-adopt.py")
    result = subprocess.run(
        [
            sys.executable,
            str(helper),
            "--repository",
            repository,
            "--commit",
            commit,
            "--approve",
            approve,
        ],
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        message = result.stderr.decode("utf-8", "replace").strip()
        raise RuntimeError(f"exact-commit board consumer failed: {message}")
    board = json.loads(result.stdout.decode("utf-8"))
    summary = json.loads(result.stderr.decode("utf-8"))
    return board, summary


def api_request(url: str) -> urllib.request.Request:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "modern-latex-adoption-audit",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return urllib.request.Request(url, headers=headers)


def fetch_issues(repository: str) -> tuple[list[dict], int, bool]:
    query = urllib.parse.urlencode(
        {"state": "all", "labels": "adoption", "per_page": 100, "page": 1}
    )
    url: str | None = f"https://api.github.com/repos/{repository}/issues?{query}"
    issues: list[dict] = []
    pages = 0
    while url:
        with urllib.request.urlopen(api_request(url), timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8"))
            link = response.headers.get("Link", "")
        if not isinstance(payload, list):
            raise RuntimeError("GitHub issue API did not return an array")
        issues.extend(issue for issue in payload if "pull_request" not in issue)
        pages += 1
        url = None
        for part in link.split(","):
            if 'rel="next"' not in part:
                continue
            match = re.search(r"<([^>]+)>", part)
            if match:
                url = match.group(1)
                break
    return issues, pages, bool(os.environ.get("GITHUB_TOKEN"))


def load_fixture(path: str) -> list[dict]:
    text = sys.stdin.read() if path == "-" else pathlib.Path(path).read_text(encoding="utf-8")
    value = json.loads(text)
    if not isinstance(value, list):
        raise RuntimeError("issue fixture must be a JSON array")
    return value


def parse_sections(body: str) -> dict[str, str]:
    matches = list(SECTION_RE.finditer(body))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        value = body[match.end() : end].strip()
        sections[match.group("label").strip()] = "" if value == "_No response_" else value
    return sections


def issue_kind(title: str) -> str | None:
    if title.startswith("[Adopt] "):
        return "claim"
    if title.startswith("[Handback] "):
        return "handback"
    return None


def first_line(value: str) -> str:
    return value.splitlines()[0].strip() if value.strip() else ""


def audit_issues(repository: str, board: dict, issues: list[dict]) -> tuple[list[dict], list[str], list[str]]:
    board_ids = {str(item["id"]) for item in board.get("items", [])}
    rows: list[dict] = []
    claims: dict[int, dict] = {}
    global_errors: list[str] = []
    global_warnings: list[str] = []
    issue_url_re = re.compile(
        rf"https://github\.com/{re.escape(repository)}/issues/(?P<number>[0-9]+)"
    )

    for issue in sorted(issues, key=lambda value: int(value.get("number", 0))):
        number = int(issue.get("number", 0))
        title = str(issue.get("title") or "")
        body = str(issue.get("body") or "")
        sections = parse_sections(body)
        kind = issue_kind(title)
        errors: list[str] = []
        warnings: list[str] = []
        if kind is None:
            errors.append("adoption-labeled issue has an unknown title prefix")
            required: tuple[str, ...] = ()
        else:
            required = CLAIM_REQUIRED if kind == "claim" else HANDBACK_REQUIRED
        for label in required:
            if not sections.get(label, "").strip():
                errors.append(f"missing required section: {label}")

        board_id = first_line(sections.get("Board ID", ""))
        proposed = board_id.startswith("new:") and bool(BOARD_ID_RE.fullmatch(board_id[4:]))
        if board_id and board_id not in board_ids and not proposed:
            errors.append(f"unknown Board ID: {board_id}")

        claim_number: int | None = None
        if kind == "handback":
            claim_value = sections.get("Adoption issue or mirror URL", "")
            match = issue_url_re.search(claim_value)
            if match:
                claim_number = int(match.group("number"))
            else:
                errors.append("handback does not contain an exact repository adoption-issue URL")
            state = first_line(sections.get("Handback state", ""))
            if state and state not in HANDBACK_STATES:
                errors.append(f"unknown handback state: {state}")

        row = {
            "number": number,
            "url": str(issue.get("html_url") or issue.get("url") or ""),
            "state": str(issue.get("state") or ""),
            "title": title,
            "type": kind or "unknown",
            "board_id": board_id,
            "board_id_kind": "existing" if board_id in board_ids else ("proposed" if proposed else "invalid"),
            "claim_issue": claim_number,
            "body_bytes": len(body.encode("utf-8")),
            "body_sha256": sha256(body.encode("utf-8")),
            "updated_at": issue.get("updated_at"),
            "errors": errors,
            "warnings": warnings,
            "valid": False,
        }
        rows.append(row)
        if kind == "claim" and number > 0:
            claims[number] = row

    for row in rows:
        if row["type"] != "handback" or row["claim_issue"] is None:
            continue
        claim = claims.get(int(row["claim_issue"]))
        if claim is None:
            row["errors"].append("handback references an adoption issue absent from the audited issue set")
            continue
        if row["board_id"] != claim["board_id"]:
            row["errors"].append("handback Board ID differs from its adoption issue")

    handback_claims = {
        int(row["claim_issue"])
        for row in rows
        if row["type"] == "handback" and row["claim_issue"] is not None
    }
    for number, claim in claims.items():
        if claim["state"] == "closed" and number not in handback_claims:
            claim["warnings"].append("closed adoption issue has no audited handback")

    for row in rows:
        row["valid"] = not row["errors"]
        global_errors.extend(f"issue#{row['number']}: {message}" for message in row["errors"])
        global_warnings.extend(f"issue#{row['number']}: {message}" for message in row["warnings"])
    return rows, global_errors, global_warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit adoption and handback issues against one approved board commit."
    )
    parser.add_argument("--commit", required=True)
    parser.add_argument("--approve", required=True)
    parser.add_argument("--repository", default=DEFAULT_REPOSITORY)
    parser.add_argument("--issues-file", help="Read a GitHub-API-style JSON array; use - for stdin")
    args = parser.parse_args()
    if not COMMIT_RE.fullmatch(args.commit) or not COMMIT_RE.fullmatch(args.approve):
        parser.error("--commit and --approve must each be exact 40-hex commits")
    if args.commit.lower() != args.approve.lower():
        parser.error("--approve does not match --commit")

    try:
        board, board_summary = load_approved_board(
            args.repository, args.commit.lower(), args.approve.lower()
        )
        if args.issues_file:
            issues = load_fixture(args.issues_file)
            pages = 0
            authenticated = False
            issue_source = "fixture"
        else:
            issues, pages, authenticated = fetch_issues(args.repository)
            issue_source = "public_github_api"
        rows, errors, warnings = audit_issues(args.repository, board, issues)
    except Exception as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    claims = [row for row in rows if row["type"] == "claim"]
    handbacks = [row for row in rows if row["type"] == "handback"]
    grouped: dict[str, int] = {}
    for row in claims:
        grouped[row["board_id"]] = grouped.get(row["board_id"], 0) + 1
    report = {
        "schema": "github-adoption-issues-check-v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "warnings": warnings,
        "observed_at": dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
        "repository": args.repository,
        "approved_commit": args.commit.lower(),
        "board": {
            "path": "manifests/adopt.json",
            "bytes": board_summary["board_bytes"],
            "sha256": board_summary["board_sha256"],
            "items": board_summary["items"],
            "mirrors": board_summary["mirrors"],
            "exact_commit_consumer": board_summary["status"],
        },
        "issue_source": {
            "kind": issue_source,
            "pages": pages,
            "authenticated": authenticated,
            "label": "adoption",
        },
        "aggregate": {
            "issues": len(rows),
            "claims": len(claims),
            "handbacks": len(handbacks),
            "open": sum(row["state"] == "open" for row in rows),
            "closed": sum(row["state"] == "closed" for row in rows),
            "valid": sum(row["valid"] for row in rows),
            "invalid": sum(not row["valid"] for row in rows),
            "parallel_claim_groups": sum(count > 1 for count in grouped.values()),
            "warnings": len(warnings),
        },
        "checks": {
            "exact_commit_consumer_pass": board_summary["status"] == "PASS",
            "board_ids_valid": not any("Board ID" in error for error in errors),
            "handbacks_linked": not any("handback" in error for error in errors),
            "parallel_claims_allowed": True,
            "issues_mutated": False,
            "producer_files_mutated": False,
            "zenodo_network_queried": False,
        },
        "issues": rows,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print(
        json.dumps(
            {
                "status": report["status"],
                "issues": len(rows),
                "claims": len(claims),
                "handbacks": len(handbacks),
                "errors": len(errors),
                "warnings": len(warnings),
            },
            separators=(",", ":"),
        ),
        file=sys.stderr,
    )
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
