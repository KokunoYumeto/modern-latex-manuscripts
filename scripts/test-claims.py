#!/usr/bin/env python3
"""Replay valid and invalid adoption-issue lifecycle fixtures offline."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
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

### Workflow token
bounded_continuation

### Exact scope
Gauss, Werke II, one bounded page range from the declared cursor.

### Starting evidence
One exact approved Git commit, mapped source paths, byte lengths, and SHA-256 values.

### Traceability
- [X] I will preserve predecessors and declare overlap rather than silently overwriting existing work.
- [X] I understand that opening this issue does not reserve the scope exclusively.
"""


def stacks_claim_body(
    *,
    board_id: str = STACKS_BOARD_ID,
    intent: str = "Bind the first exact upstream pin and Commons overlay",
    workflow: str = "upstream_overlay_sync",
    writer: str = "example-maintainer",
    namespace: str = "commons/stacks/pilot",
) -> str:
    return f"""### Board ID
{board_id}

### Intent
{intent}

### Workflow token
{workflow}

### Exact scope
Bind one exact upstream pin and one new Commons-owned overlay namespace; do not modify upstream or another task's files.

### Starting evidence
Exact repository URL, applicable license identity, 40-hex commit, overlay namespace, composition plan, tests, and synchronization cursor.

### Commons writer identity
{writer}

### Exact upstream repository URL
https://github.com/example/stacks-upstream

### Applicable upstream license identity
COPYING at the exact upstream commit

### Exact upstream commit
0123456789abcdef0123456789abcdef01234567

### Commons overlay namespace
{namespace}

### Deterministic composition
Pin upstream, apply the named overlay without rewriting either input, and hash the composed output.

### Tests and review plan
Run exact-input, namespace, attribution, conflict, and deterministic-rebuild checks; retain review receipts.

### Starting synchronization cursor
Initial exact upstream pin; no earlier Commons overlay generation is claimed.

### Traceability
- [X] I will write only to the declared Commons-owned namespace and will not edit upstream or another task's files.
- [X] I will preserve exact upstream and predecessor identities, conflicts, failures, corrections, and reversals.
- [X] I will not imply upstream acceptance, approval, endorsement, or a motive for prior contribution outcomes.
- [X] Any public modified edition will be distinctly titled and will preserve applicable attribution, license, and history notices.
- [X] I understand that opening this issue does not reserve the scope exclusively.
"""


def handback_body(repository: str) -> str:
    return f"""### Board ID
{BOARD_ID}

### Adoption issue URL
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
- [X] I preserved the starting generation and did not silently overwrite contradictory or superseded evidence.
- [X] I kept quality/review state explicit and made no unsupported completion or certification claim.
- [X] I understand that archive maps change only after the returned bytes or exact external identity are inspectable.
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


def git_blob(git_root: Path, commit: str, path: str) -> bytes:
    environment = os.environ.copy()
    environment["GIT_NO_LAZY_FETCH"] = "1"
    result = subprocess.run(
        ["git", "-C", str(git_root), "cat-file", "blob", f"{commit}:{path}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        env=environment,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"required approved blob is not locally materialized: {path}: "
            + result.stderr.decode("utf-8", errors="replace").strip()
        )
    return result.stdout


def git_command(
    repository: Path,
    *arguments: str,
    data: bytes | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[bytes]:
    result = subprocess.run(
        ["git", "-C", str(repository), *arguments],
        input=data,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace").strip())
    return result


def git_resolve(repository: Path, expression: str) -> str:
    return git_command(repository, "rev-parse", "--verify", expression).stdout.decode("ascii").strip()


def copy_git_object(source: Path, target: Path, object_type: str, object_id: str) -> None:
    payload = git_command(source, "cat-file", object_type, object_id).stdout
    written = git_command(
        target, "hash-object", "-w", "-t", object_type, "--stdin", data=payload
    ).stdout.decode("ascii").strip()
    if written.lower() != object_id.lower():
        raise RuntimeError(f"copied {object_type} identity changed: {object_id} -> {written}")


def required_tree_ids(source: Path, commit: str, paths: list[str]) -> set[str]:
    root = git_resolve(source, f"{commit}^{{tree}}")
    identifiers = {root}
    for path in paths:
        current = root
        for component in Path(path).parts[:-1]:
            listing = git_command(source, "ls-tree", current, "--", component).stdout.strip()
            metadata, _separator, _name = listing.partition(b"\t")
            _mode, object_type, object_id = metadata.split(b" ", 2)
            if object_type != b"tree":
                raise RuntimeError(f"execution-contract parent is not a tree: {path}")
            current = object_id.decode("ascii")
            identifiers.add(current)
    return identifiers


def configure_promisor(repository: Path) -> None:
    git_command(repository, "config", "core.repositoryformatversion", "1")
    git_command(repository, "remote", "add", "origin", "http://127.0.0.1:9/unreachable")
    git_command(repository, "config", "remote.origin.promisor", "true")
    git_command(repository, "config", "remote.origin.partialclonefilter", "blob:none")
    git_command(repository, "config", "extensions.partialClone", "origin")


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
        issue(
            17,
            "[Adopt] proposed workflow-contract fixture",
            claim_body("new:workflow-contract-fixture").replace(
                "### Workflow token\nbounded_continuation",
                "### Workflow token\nsource_intake",
            ),
            "open",
        ),
        issue(
            19,
            "[Adopt] Stacks Commons layer — source evidence",
            stacks_claim_body(
                intent="Return source or license evidence only",
                workflow="source_intake",
                writer="source-researcher",
                namespace="commons/stacks/source-evidence",
            ),
            "open",
        ),
        issue(
            20,
            "[Adopt] Stacks Commons layer — same writer mirror",
            stacks_claim_body(),
            "open",
        ),
        issue(
            30,
            "[Adopt] Stacks Commons layer — independent review",
            stacks_claim_body(
                intent="Independently mirror or check an existing Commons overlay",
                workflow="independent_review",
                writer="reviewer",
                namespace="commons/stacks/review",
            ),
            "open",
        ),
        issue(
            31,
            "[Adopt] Stacks Commons layer — deterministic composition",
            stacks_claim_body(
                intent="Propose a deterministic composition and test fixture",
                workflow="assembly_review",
                writer="assembler",
                namespace="commons/stacks/composition",
            ),
            "open",
        ),
    ]
    invalid_stacks = stacks_claim_body().replace(
        "### Exact upstream commit\n0123456789abcdef0123456789abcdef01234567",
        "### Exact upstream commit\n_No response_",
    )
    invalid_workflow = claim_body(BOARD_ID).replace(
        "### Workflow token\nbounded_continuation",
        "### Workflow token\ntable_audit",
    )
    unknown_workflow = claim_body(BOARD_ID).replace(
        "### Workflow token\nbounded_continuation",
        "### Workflow token\nnot_a_registered_workflow",
    )
    missing_workflow = claim_body(BOARD_ID).replace(
        "### Workflow token\nbounded_continuation",
        "### Workflow token\n_No response_",
    )
    wrong_stacks_board = stacks_claim_body(
        board_id="noether-de-auth",
        intent="Independently mirror or check an existing Commons overlay",
        workflow="independent_review",
    )
    wrong_stacks_intent_workflow = stacks_claim_body(
        intent="Return source or license evidence only",
        workflow="upstream_overlay_sync",
    )
    conflicting_stacks_repository = stacks_claim_body().replace(
        "https://github.com/example/stacks-upstream",
        "https://github.com/example/stacks-upstream\nhttps://github.com/example/conflict",
    )
    conflicting_stacks_commit = stacks_claim_body().replace(
        "0123456789abcdef0123456789abcdef01234567",
        "0123456789abcdef0123456789abcdef01234567\nabcdef0123456789abcdef0123456789abcdef01",
    )
    generic_checks = (
        "- [X] I will preserve predecessors and declare overlap rather than silently overwriting existing work.\n"
        "- [X] I understand that opening this issue does not reserve the scope exclusively."
    )
    arbitrary_traceability = claim_body(BOARD_ID).replace(
        generic_checks,
        "- [X] arbitrary assurance",
    )
    bad_handback = handback_body(args.repository).replace(
        f"https://github.com/{args.repository}/issues/10",
        f"prefix https://github.com/{args.repository}/issues/10evil suffix",
    ).replace(
        "- [X] I preserved the starting generation and did not silently overwrite contradictory or superseded evidence.\n- [X] I kept quality/review state explicit and made no unsupported completion or certification claim.\n- [X] I understand that archive maps change only after the returned bytes or exact external identity are inspectable.",
        "- [X] arbitrary preservation",
    )
    conflicting_board_id = claim_body(f"{BOARD_ID}\nnoether-de-auth")
    suffixed_checkbox = claim_body(BOARD_ID).replace(
        "- [X] I will preserve predecessors and declare overlap rather than silently overwriting existing work.",
        "- [X] I will preserve predecessors and declare overlap rather than silently overwriting existing work. NOT AGREED",
    )
    fenced_checkboxes = claim_body(BOARD_ID).replace(
        generic_checks,
        f"```text\n{generic_checks}\n```",
    )
    commented_checkboxes = claim_body(BOARD_ID).replace(
        generic_checks,
        f"<!--\n{generic_checks}\n-->",
    )
    extra_checkbox = claim_body(BOARD_ID).replace(
        generic_checks,
        f"{generic_checks}\n- [X] arbitrary extra assurance",
    )
    invalid_fixture = [
        issue(13, "[Adopt] unknown board row", claim_body("not-a-board-row"), "open"),
        issue(14, "[Adopt] Stacks Commons layer — invalid fixture", invalid_stacks, "open"),
        issue(15, "[Adopt] row-incompatible workflow", invalid_workflow, "open"),
        issue(16, "[Adopt] unknown workflow", unknown_workflow, "open"),
        issue(18, "[Adopt] missing workflow", missing_workflow, "open"),
        issue(21, "[Adopt] Stacks Commons layer — wrong Board ID", wrong_stacks_board, "open"),
        issue(22, "[Adopt] Stacks Commons layer — mismatched intent", wrong_stacks_intent_workflow, "open"),
        issue(23, "[Adopt] Stacks Commons layer — conflicting repository", conflicting_stacks_repository, "open"),
        issue(24, "[Adopt] Stacks Commons layer — conflicting commit", conflicting_stacks_commit, "open"),
        issue(25, "[Adopt] arbitrary traceability", arbitrary_traceability, "open"),
        issue(26, "[Handback] malformed link and preservation", bad_handback, "closed"),
        issue(
            27,
            "[Adopt] Stacks Commons layer — namespace writer A",
            stacks_claim_body(writer="writer-a", namespace="commons/stacks/collision"),
            "open",
        ),
        issue(
            28,
            "[Adopt] Stacks Commons layer — namespace writer B",
            stacks_claim_body(writer="writer-b", namespace="commons/stacks/collision"),
            "open",
        ),
        issue(29, "[Adopt] conflicting Board ID", conflicting_board_id, "open"),
        issue(
            32,
            "[Adopt] Stacks Commons layer — trailing-slash namespace",
            stacks_claim_body(writer="writer-c", namespace="commons/stacks/trailing/"),
            "open",
        ),
        issue(
            33,
            "[Adopt] Stacks Commons layer — dot namespace",
            stacks_claim_body(writer="writer-d", namespace="commons/stacks/../dot"),
            "open",
        ),
        issue(
            34,
            "[Adopt] Stacks Commons layer — multiline namespace",
            stacks_claim_body(writer="writer-e", namespace="commons/stacks/first\ncommons/stacks/second"),
            "open",
        ),
        issue(
            35,
            "[Adopt] Stacks Commons layer — parent-child namespace A",
            stacks_claim_body(writer="writer-f", namespace="commons/stacks/tree"),
            "open",
        ),
        issue(
            36,
            "[Adopt] Stacks Commons layer — parent-child namespace B",
            stacks_claim_body(writer="writer-g", namespace="commons/stacks/tree/child"),
            "open",
        ),
        issue(37, "[Adopt] suffixed checkbox", suffixed_checkbox, "open"),
        issue(38, "[Adopt] fenced checkboxes", fenced_checkboxes, "open"),
        issue(39, "[Adopt] commented checkboxes", commented_checkboxes, "open"),
        issue(40, "[Adopt] extra checkbox", extra_checkbox, "open"),
        issue(
            41,
            "[Adopt] Stacks Commons layer — terminal-dot namespace",
            stacks_claim_body(writer="writer-h", namespace="commons/stacks/terminal."),
            "open",
        ),
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
        expected = {"issues": 8, "claims": 7, "handbacks": 1, "valid": 8, "invalid": 0}
        if any(aggregate.get(key) != value for key, value in expected.items()):
            raise RuntimeError(f"valid fixture aggregate mismatch: {aggregate}")
        if valid_report.get("board", {}).get("transport") != "local_git_object_database":
            raise RuntimeError("valid fixture did not use the local Git board transport")
        if valid_report.get("issue_source", {}).get("kind") != "json_fixture":
            raise RuntimeError("valid fixture did not report the JSON issue transport")
        if valid_report.get("checks", {}).get("external_network_queried") is not False:
            raise RuntimeError("valid fixture did not remain fully offline")
        if valid_report.get("checks", {}).get("claim_workflows_valid") is not True:
            raise RuntimeError("valid fixture did not prove registered row-compatible workflows")
        if valid_report.get("checks", {}).get("stacks_namespace_single_writer") is not True:
            raise RuntimeError("valid fixture did not preserve one writer per Stacks namespace")
        if valid_report.get("checks", {}).get("approved_executable_drift_check") is not True:
            raise RuntimeError("valid fixture did not pass the approved-executable drift check")
        approved_executables = valid_report.get("board", {}).get("approved_executables", {})
        expected_executable_paths = ("scripts/get-adopt.py", "scripts/check-claims.py")
        if tuple(approved_executables) != expected_executable_paths:
            raise RuntimeError(f"approved executable path contract mismatch: {approved_executables}")
        for path in expected_executable_paths:
            blob = git_blob(git_root, args.commit.lower(), path)
            expected_identity = {
                "bytes": len(blob),
                "sha256": hashlib.sha256(blob).hexdigest().upper(),
            }
            if approved_executables.get(path) != expected_identity:
                raise RuntimeError(f"approved executable identity mismatch for {path}")

        invalid = run_auditor(checker, args.repository, args.commit.lower(), git_root, invalid_path)
        invalid_report = parse_report(invalid, "invalid Board-ID fixture")
        if invalid.returncode != 1 or invalid_report.get("status") != "FAIL":
            raise RuntimeError("invalid Board-ID fixture did not fail closed with exit 1")
        if invalid_report.get("checks", {}).get("claim_workflows_valid") is not False:
            raise RuntimeError("invalid workflow fixtures did not fail the workflow contract")
        invalid_aggregate = invalid_report.get("aggregate", {})
        if invalid_aggregate.get("issues") != 24 or invalid_aggregate.get("invalid") != 24:
            raise RuntimeError(f"invalid fixture aggregate mismatch: {invalid_aggregate}")
        invalid_rows = {row.get("number"): row for row in invalid_report.get("issues", [])}
        for number in (38, 39, 40):
            row_errors = invalid_rows.get(number, {}).get("errors", [])
            if not any("Traceability checklist must contain exactly" in error for error in row_errors):
                raise RuntimeError(f"checklist context fixture {number} did not fail exact validation")
        if not any(
            "Commons overlay namespace must be one canonical lowercase slash-delimited path" in error
            for error in invalid_rows.get(41, {}).get("errors", [])
        ):
            raise RuntimeError("terminal-dot namespace fixture did not fail canonical validation")
        if not any("unknown Board ID: not-a-board-row" in error for error in invalid_report.get("errors", [])):
            raise RuntimeError("invalid fixture did not preserve the unknown Board-ID error")
        if not any("missing required Stacks section: Exact upstream commit" in error for error in invalid_report.get("errors", [])):
            raise RuntimeError("invalid fixture did not fail closed on a missing Stacks commit")
        if not any("Workflow token is not allowed for Board ID gauss-werke-ii: table_audit" in error for error in invalid_report.get("errors", [])):
            raise RuntimeError("invalid fixture did not reject a row-incompatible workflow")
        if not any("unknown Workflow token: not_a_registered_workflow" in error for error in invalid_report.get("errors", [])):
            raise RuntimeError("invalid fixture did not reject an unknown workflow")
        if not any("missing required section: Workflow token" in error for error in invalid_report.get("errors", [])):
            raise RuntimeError("invalid fixture did not reject a missing workflow")
        required_error_fragments = (
            "dedicated Stacks route requires Board ID stacks-commons-layer",
            "Stacks Intent requires Workflow token source_intake",
            "Stacks upstream repository must be one exact GitHub repository URL",
            "Stacks upstream commit must be exactly 40 hexadecimal characters",
            "Traceability checklist must contain exactly the required checked statements in order",
            "handback does not contain an exact repository adoption-issue URL",
            "Handback preservation checklist must contain exactly the required checked statements in order",
            "multiple Commons writers claim overlapping overlay namespaces: commons/stacks/collision <> commons/stacks/collision",
            "Commons overlay namespace must be one canonical lowercase slash-delimited path",
            "commons/stacks/tree <> commons/stacks/tree/child",
            "Traceability checklist must contain exactly the required checked statements in order",
            "unknown Board ID: gauss-werke-ii\nnoether-de-auth",
        )
        for fragment in required_error_fragments:
            if not any(fragment in error for error in invalid_report.get("errors", [])):
                raise RuntimeError(f"invalid fixture did not preserve error: {fragment}")

        repository_mismatch = run_auditor(
            checker,
            "other-owner/other-repo",
            args.commit.lower(),
            git_root,
            valid_path,
        )
        if repository_mismatch.returncode != 2 or b"approved board repository mismatch" not in repository_mismatch.stderr:
            raise RuntimeError("repository-mismatch fixture did not fail closed with exit 2")

        altered_root = root / "altered"
        altered_root.mkdir()
        altered_checker = altered_root / "check-claims.py"
        shutil.copyfile(checker, altered_checker)
        shutil.copyfile(checker.with_name("get-adopt.py"), altered_root / "get-adopt.py")
        altered_checker.write_bytes(altered_checker.read_bytes() + b"\n# altered fixture\n")
        checker_mismatch = run_auditor(
            altered_checker,
            args.repository,
            args.commit.lower(),
            git_root,
            valid_path,
        )
        if checker_mismatch.returncode != 2 or b"does not match the human-approved commit" not in checker_mismatch.stderr:
            raise RuntimeError("altered-auditor fixture did not fail closed with exit 2")

        helper_root = root / "altered-helper"
        helper_root.mkdir()
        helper_checker = helper_root / "check-claims.py"
        helper = helper_root / "get-adopt.py"
        shutil.copyfile(checker, helper_checker)
        shutil.copyfile(checker.with_name("get-adopt.py"), helper)
        helper.write_bytes(helper.read_bytes() + b"\n# altered helper fixture\n")
        helper_mismatch = run_auditor(
            helper_checker,
            args.repository,
            args.commit.lower(),
            git_root,
            valid_path,
        )
        if helper_mismatch.returncode != 2 or b"does not match the human-approved commit" not in helper_mismatch.stderr:
            raise RuntimeError("altered-helper fixture did not fail closed with exit 2")

        board = json.loads(git_blob(git_root, args.commit.lower(), "manifests/adopt.json"))
        contract_paths = [
            "manifests/adopt.json",
            "manifests/adopt.schema.json",
            "manifests/adopt.check.json",
            str(board["map_manifest"]),
            "scripts/get-adopt.py",
            "scripts/check-claims.py",
        ]
        promisor = root / "execution-promisor.git"
        subprocess.run(
            ["git", "init", "--bare", str(promisor)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        configure_promisor(promisor)
        copy_git_object(git_root, promisor, "commit", args.commit.lower())
        for object_id in sorted(required_tree_ids(git_root, args.commit.lower(), contract_paths)):
            copy_git_object(git_root, promisor, "tree", object_id)
        helper_path = "scripts/get-adopt.py"
        checker_path = "scripts/check-claims.py"
        for path in contract_paths:
            if path in (helper_path, checker_path):
                continue
            copy_git_object(
                git_root,
                promisor,
                "blob",
                git_resolve(git_root, f"{args.commit.lower()}:{path}"),
            )
        missing_execution_blob = run_auditor(
            checker,
            args.repository,
            args.commit.lower(),
            promisor,
            valid_path,
        )
        missing_diagnostic = missing_execution_blob.stderr.decode("utf-8", errors="replace")
        if missing_execution_blob.returncode != 2:
            raise RuntimeError("missing execution blob did not fail closed with exit 2")
        if "approved auditor blob read failed for scripts/get-adopt.py" not in missing_diagnostic:
            raise RuntimeError("missing execution blob did not identify the absent helper")
        network_markers = ("127.0.0.1", "unable to access", "fetch-pack", "git fetch")
        if any(marker in missing_diagnostic for marker in network_markers):
            raise RuntimeError("missing execution blob attempted the promisor remote")
        copy_git_object(
            git_root,
            promisor,
            "blob",
            git_resolve(git_root, f"{args.commit.lower()}:{helper_path}"),
        )
        missing_checker_blob = run_auditor(
            checker,
            args.repository,
            args.commit.lower(),
            promisor,
            valid_path,
        )
        missing_checker_diagnostic = missing_checker_blob.stderr.decode("utf-8", errors="replace")
        if missing_checker_blob.returncode != 2:
            raise RuntimeError("missing checker blob did not fail closed with exit 2")
        if "approved auditor blob read failed for scripts/check-claims.py" not in missing_checker_diagnostic:
            raise RuntimeError("missing checker blob did not identify the absent checker")
        if any(marker in missing_checker_diagnostic for marker in network_markers):
            raise RuntimeError("missing checker blob attempted the promisor remote")
        copy_git_object(
            git_root,
            promisor,
            "blob",
            git_resolve(git_root, f"{args.commit.lower()}:{checker_path}"),
        )
        materialized_execution = run_auditor(
            checker,
            args.repository,
            args.commit.lower(),
            promisor,
            valid_path,
        )
        materialized_report = parse_report(materialized_execution, "materialized execution fixture")
        if materialized_execution.returncode != 0 or materialized_report.get("status") != "PASS":
            raise RuntimeError("fully materialized execution contract did not pass offline")

    print(
        json.dumps(
            {
                "status": "PASS",
                "commit": args.commit.lower(),
                "valid_fixture": {"issues": 8, "valid": 8, "errors": 0},
                "invalid_fixture": {"issues": 24, "invalid": 24, "exit": 1},
                "repository_mismatch_exit": 2,
                "checker_mismatch_exit": 2,
                "helper_mismatch_exit": 2,
                "missing_execution_blob_exit": 2,
                "missing_execution_blob_remote_attempt": False,
                "missing_checker_blob_exit": 2,
                "missing_checker_blob_remote_attempt": False,
                "materialized_execution_blobs": 2,
                "uppercase_checkbox": "accepted_exactly",
                "suffixed_checkbox": "rejected",
                "fenced_checkbox": "rejected",
                "commented_checkbox": "rejected",
                "extra_checkbox": "rejected",
                "parent-child namespace": "rejected",
                "terminal-dot namespace": "rejected",
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
