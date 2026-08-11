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
import tempfile
import urllib.parse
import urllib.request


DEFAULT_REPOSITORY = "KokunoYumeto/modern-latex-manuscripts"
COMMIT_RE = re.compile(r"^[0-9a-fA-F]{40}$")
BOARD_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SECTION_RE = re.compile(r"(?m)^### (?P<label>[^\r\n]+)\s*$")
STACKS_BOARD_ID = "stacks-commons-layer"
STACKS_TITLE_PREFIX = "[Adopt] Stacks Commons layer — "
STACKS_REPOSITORY_RE = re.compile(r"^https://github\.com/[^/\s?#]+/[^/\s?#]+/?$")
STACKS_NAMESPACE_RE = re.compile(
    r"^[a-z0-9](?:[a-z0-9._-]*[a-z0-9_-])?(?:/[a-z0-9](?:[a-z0-9._-]*[a-z0-9_-])?)*$"
)
CLAIM_REQUIRED = (
    "Board ID",
    "Intent",
    "Workflow token",
    "Exact scope",
    "Starting evidence",
    "Traceability",
)
STACKS_CLAIM_REQUIRED = (
    "Commons writer identity",
    "Exact upstream repository URL",
    "Applicable upstream license identity",
    "Exact upstream commit",
    "Commons overlay namespace",
    "Deterministic composition",
    "Tests and review plan",
    "Starting synchronization cursor",
)
STACKS_TRACEABILITY_REQUIRED = (
    "I will write only to the declared Commons-owned namespace and will not edit upstream or another task's files.",
    "I will preserve exact upstream and predecessor identities, conflicts, failures, corrections, and reversals.",
    "I will not imply upstream acceptance, approval, endorsement, or a motive for prior contribution outcomes.",
    "Any public modified edition will be distinctly titled and will preserve applicable attribution, license, and history notices.",
    "I understand that opening this issue does not reserve the scope exclusively.",
)
GENERIC_TRACEABILITY_REQUIRED = (
    "I will preserve predecessors and declare overlap rather than silently overwriting existing work.",
    "I understand that opening this issue does not reserve the scope exclusively.",
)
STACKS_INTENT_WORKFLOW = {
    "Bind the first exact upstream pin and Commons overlay": "upstream_overlay_sync",
    "Independently mirror or check an existing Commons overlay": "independent_review",
    "Propose a deterministic composition and test fixture": "assembly_review",
    "Return source or license evidence only": "source_intake",
}
HANDBACK_REQUIRED = (
    "Board ID",
    "Adoption issue URL",
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
HANDBACK_PRESERVATION_REQUIRED = (
    "I preserved the starting generation and did not silently overwrite contradictory or superseded evidence.",
    "I kept quality/review state explicit and made no unsupported completion or certification claim.",
    "I understand that archive maps change only after the returned bytes or exact external identity are inspectable.",
)
APPROVED_EXECUTABLES = (
    "scripts/get-adopt.py",
    "scripts/check-claims.py",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def load_approved_board(
    repository: str,
    commit: str,
    approve: str,
    helper_bytes: bytes,
    git_repository: str | None = None,
) -> tuple[dict, dict]:
    with tempfile.TemporaryDirectory(prefix="approved-adopt-helper-") as directory:
        helper = pathlib.Path(directory) / "get-adopt.py"
        helper.write_bytes(helper_bytes)
        command = [
            sys.executable,
            str(helper),
            "--repository",
            repository,
            "--commit",
            commit,
            "--approve",
            approve,
        ]
        if git_repository is not None:
            command.extend(["--git", git_repository])
        result = subprocess.run(
            command,
            check=False,
            capture_output=True,
        )
    if result.returncode != 0:
        message = result.stderr.decode("utf-8", "replace").strip()
        raise RuntimeError(f"exact-commit board consumer failed: {message}")
    board = json.loads(result.stdout.decode("utf-8"))
    summary = json.loads(result.stderr.decode("utf-8"))
    return board, summary


def approved_blob(repository: str, commit: str, path: str, git_repository: str | None) -> bytes:
    if git_repository is None:
        encoded = "/".join(urllib.parse.quote(part, safe="") for part in path.split("/"))
        request = urllib.request.Request(
            f"https://raw.githubusercontent.com/{repository}/{commit}/{encoded}",
            headers={"User-Agent": "modern-latex-adoption-audit"},
        )
        with urllib.request.urlopen(request, timeout=120) as response:
            return response.read()
    environment = os.environ.copy()
    environment["GIT_NO_LAZY_FETCH"] = "1"
    result = subprocess.run(
        ["git", "-C", str(pathlib.Path(git_repository).resolve(strict=True)), "cat-file", "blob", f"{commit}:{path}"],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment,
    )
    if result.returncode != 0:
        diagnostic = result.stderr.decode("utf-8", "replace").strip()
        raise RuntimeError(f"approved auditor blob read failed for {path}: {diagnostic}")
    return result.stdout


def verify_approved_executables(
    repository: str, commit: str, git_repository: str | None
) -> tuple[dict[str, dict[str, object]], dict[str, bytes]]:
    script_directory = pathlib.Path(__file__).resolve().parent
    identities: dict[str, dict[str, object]] = {}
    blobs: dict[str, bytes] = {}
    for path in APPROVED_EXECUTABLES:
        local = (script_directory / pathlib.PurePosixPath(path).name).read_bytes()
        approved = approved_blob(repository, commit, path, git_repository)
        if local != approved:
            raise RuntimeError(f"executed {path} does not match the human-approved commit")
        identities[path] = {"bytes": len(local), "sha256": sha256(local)}
        blobs[path] = approved
    return identities, blobs


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


def checked_statements(value: str) -> tuple[str, ...] | None:
    """Return one exact checklist, or None when prose can masquerade as checks."""
    lines = tuple(line for line in value.replace("\r\n", "\n").split("\n") if line.strip())
    statements: list[str] = []
    for line in lines:
        match = re.fullmatch(r"- \[[xX]\] (?P<statement>[^\r\n]+)", line)
        if match is None:
            return None
        statements.append(match.group("statement"))
    return tuple(statements)


def require_exact_checklist(
    value: str,
    expected: tuple[str, ...],
    label: str,
    errors: list[str],
) -> None:
    statements = checked_statements(value)
    if statements != expected:
        errors.append(f"{label} checklist must contain exactly the required checked statements in order")


def namespaces_overlap(left: str, right: str) -> bool:
    return left == right or left.startswith(f"{right}/") or right.startswith(f"{left}/")


def issue_kind(title: str) -> str | None:
    if title.startswith("[Adopt] "):
        return "claim"
    if title.startswith("[Handback] "):
        return "handback"
    return None


def audit_issues(repository: str, board: dict, issues: list[dict]) -> tuple[list[dict], list[str], list[str]]:
    board_rows = {str(item["id"]): item for item in board.get("items", [])}
    board_ids = set(board_rows)
    workflow_ids = {str(flow["id"]) for flow in board.get("workflows", [])}
    rows: list[dict] = []
    claims: dict[int, dict] = {}
    global_errors: list[str] = []
    global_warnings: list[str] = []
    issue_url_re = re.compile(
        rf"https://github\.com/{re.escape(repository)}/issues/(?P<number>[1-9][0-9]*)/?$"
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

        board_id = sections.get("Board ID", "").strip()
        proposed = board_id.startswith("new:") and bool(BOARD_ID_RE.fullmatch(board_id[4:]))
        if board_id and board_id not in board_ids and not proposed:
            errors.append(f"unknown Board ID: {board_id}")

        workflow = sections.get("Workflow token", "").strip()
        if kind == "claim" and workflow:
            if workflow not in workflow_ids:
                errors.append(f"unknown Workflow token: {workflow}")
            elif board_id in board_rows and workflow not in {
                str(value) for value in board_rows[board_id].get("workflow", [])
            }:
                errors.append(f"Workflow token is not allowed for Board ID {board_id}: {workflow}")

        stacks_route = kind == "claim" and (
            title.startswith(STACKS_TITLE_PREFIX)
            or any(label in sections for label in STACKS_CLAIM_REQUIRED)
        )
        if stacks_route and board_id != STACKS_BOARD_ID:
            errors.append(f"dedicated Stacks route requires Board ID {STACKS_BOARD_ID}")
        if kind == "claim" and board_id == STACKS_BOARD_ID and not title.startswith(STACKS_TITLE_PREFIX):
            errors.append("Stacks Board ID requires the dedicated Stacks issue form and title prefix")

        if kind == "claim" and (board_id == STACKS_BOARD_ID or stacks_route):
            for label in STACKS_CLAIM_REQUIRED:
                if not sections.get(label, "").strip():
                    errors.append(f"missing required Stacks section: {label}")
            upstream_repository = sections.get("Exact upstream repository URL", "").strip()
            if upstream_repository and not STACKS_REPOSITORY_RE.fullmatch(upstream_repository):
                errors.append("Stacks upstream repository must be one exact GitHub repository URL")
            upstream_commit = sections.get("Exact upstream commit", "").strip()
            if upstream_commit and not COMMIT_RE.fullmatch(upstream_commit):
                errors.append("Stacks upstream commit must be exactly 40 hexadecimal characters")
            intent = sections.get("Intent", "").strip()
            expected_workflow = STACKS_INTENT_WORKFLOW.get(intent)
            if expected_workflow is None:
                errors.append(f"unknown Stacks Intent: {intent}")
            elif workflow != expected_workflow:
                errors.append(
                    f"Stacks Intent requires Workflow token {expected_workflow}: {intent}"
                )
            require_exact_checklist(
                sections.get("Traceability", ""),
                STACKS_TRACEABILITY_REQUIRED,
                "Stacks traceability",
                errors,
            )
            namespace = sections.get("Commons overlay namespace", "").strip()
            if namespace and not STACKS_NAMESPACE_RE.fullmatch(namespace):
                errors.append(
                    "Commons overlay namespace must be one canonical lowercase slash-delimited path"
                )
        elif kind == "claim":
            require_exact_checklist(
                sections.get("Traceability", ""),
                GENERIC_TRACEABILITY_REQUIRED,
                "Traceability",
                errors,
            )

        claim_number: int | None = None
        if kind == "handback":
            claim_value = sections.get("Adoption issue URL", "")
            match = issue_url_re.fullmatch(claim_value.strip())
            if match:
                claim_number = int(match.group("number"))
            else:
                errors.append("handback does not contain an exact repository adoption-issue URL")
            state = sections.get("Handback state", "").strip()
            if state and state not in HANDBACK_STATES:
                errors.append(f"unknown handback state: {state}")
            require_exact_checklist(
                sections.get("Preservation and status", ""),
                HANDBACK_PRESERVATION_REQUIRED,
                "Handback preservation",
                errors,
            )

        row = {
            "number": number,
            "url": str(issue.get("html_url") or issue.get("url") or ""),
            "state": str(issue.get("state") or ""),
            "title": title,
            "type": kind or "unknown",
            "board_id": board_id,
            "board_id_kind": "existing" if board_id in board_ids else ("proposed" if proposed else "invalid"),
            "workflow": workflow,
            "stacks_route": stacks_route,
            "commons_writer": sections.get("Commons writer identity", "").strip(),
            "overlay_namespace": sections.get("Commons overlay namespace", "").strip(),
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

    open_stacks = [
        row
        for row in rows
        if row["type"] == "claim"
        and row["board_id"] == STACKS_BOARD_ID
        and row["state"] == "open"
        and not row["errors"]
        and row["overlay_namespace"]
    ]
    conflicts: dict[int, set[str]] = {}
    for index, left in enumerate(open_stacks):
        for right in open_stacks[index + 1 :]:
            if left["commons_writer"] == right["commons_writer"]:
                continue
            if namespaces_overlap(left["overlay_namespace"], right["overlay_namespace"]):
                detail = f"{left['overlay_namespace']} <> {right['overlay_namespace']}"
                conflicts.setdefault(left["number"], set()).add(detail)
                conflicts.setdefault(right["number"], set()).add(detail)
    for row in open_stacks:
        for detail in sorted(conflicts.get(row["number"], set())):
            row["errors"].append(
                f"multiple Commons writers claim overlapping overlay namespaces: {detail}"
            )

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
    parser.add_argument(
        "--git",
        metavar="PATH",
        help=(
            "Read the approved board from exact Git objects in this checkout or "
            "bare repository; combine with --issues-file for a no-network audit"
        ),
    )
    parser.add_argument("--issues-file", help="Read a GitHub-API-style JSON array; use - for stdin")
    args = parser.parse_args()
    if not COMMIT_RE.fullmatch(args.commit) or not COMMIT_RE.fullmatch(args.approve):
        parser.error("--commit and --approve must each be exact 40-hex commits")
    if args.commit.lower() != args.approve.lower():
        parser.error("--approve does not match --commit")

    try:
        approved_executables, approved_blobs = verify_approved_executables(
            args.repository, args.commit.lower(), args.git
        )
        board, board_summary = load_approved_board(
            args.repository,
            args.commit.lower(),
            args.approve.lower(),
            approved_blobs["scripts/get-adopt.py"],
            args.git,
        )
        expected_repository = f"https://github.com/{args.repository}"
        if board.get("repository") != expected_repository:
            raise RuntimeError(
                f"approved board repository mismatch: expected {expected_repository}"
            )
        if args.issues_file:
            issues = load_fixture(args.issues_file)
            pages = 0
            authenticated = False
            issue_source = "json_fixture"
        else:
            issues, pages, authenticated = fetch_issues(args.repository)
            issue_source = "public_github_api"
        auditor_modes = board.get("claim_auditor_modes")
        if not isinstance(auditor_modes, dict):
            raise RuntimeError("board claim_auditor_modes is not an object")
        if board_summary.get("transport") not in auditor_modes.get("board", []):
            raise RuntimeError("board transport is not declared by claim_auditor_modes")
        if issue_source not in auditor_modes.get("issues", []):
            raise RuntimeError("issue transport is not declared by claim_auditor_modes")
        execution = board.get("claim_execution")
        if not isinstance(execution, dict):
            raise RuntimeError("board claim_execution is not an object")
        if execution.get("executable_paths") != list(APPROVED_EXECUTABLES):
            raise RuntimeError("claim_execution does not bind the exact approved executables")
        if (
            execution.get("ingestion_snapshot_files") != 4
            or execution.get("same_commit_required") is not True
            or execution.get("human_approved_checker_required") is not True
            or execution.get("helper_materialization") != "private_exact_commit_blob"
            or execution.get("local_script_comparison_role")
            != "drift_detection_not_trust_root"
            or execution.get("offline_git_requirement")
            != "fully_materialized_objects_with_lazy_fetch_disabled_or_network_isolation"
        ):
            raise RuntimeError("claim_execution trust boundary differs from the approved contract")
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
            "transport": board_summary["transport"],
            "approved_executables": approved_executables,
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
            "claim_workflows_valid": not any("Workflow token" in error for error in errors),
            "handbacks_linked": not any("handback" in error for error in errors),
            "parallel_claims_allowed": True,
            "stacks_namespace_single_writer": not any(
                "multiple Commons writers claim overlapping overlay namespaces" in error for error in errors
            ),
            "approved_executable_drift_check": (
                set(approved_executables) == set(APPROVED_EXECUTABLES)
                and all(
                    approved_executables[path]["bytes"] > 0
                    and re.fullmatch(
                        r"[0-9A-F]{64}", str(approved_executables[path]["sha256"])
                    )
                    is not None
                    for path in APPROVED_EXECUTABLES
                )
            ),
            "declared_auditor_modes": True,
            "external_network_queried": (
                board_summary["transport"] == "raw_github"
                or issue_source == "public_github_api"
            ),
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
