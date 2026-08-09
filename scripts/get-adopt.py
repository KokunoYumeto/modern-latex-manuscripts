#!/usr/bin/env python3
"""Fetch and validate one human-approved adoption-board snapshot."""

from __future__ import annotations

import argparse
from collections.abc import Callable
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

try:
    from jsonschema import Draft202012Validator
except ModuleNotFoundError as error:  # pragma: no cover - environment diagnostic
    raise SystemExit(
        "ERROR: jsonschema is required; install it with "
        "`python -m pip install jsonschema`."
    ) from error


BOARD_PATH = "manifests/adopt.json"
SCHEMA_PATH = "manifests/adopt.schema.json"
CHECK_PATH = "manifests/adopt.check.json"
DEFAULT_REPOSITORY = "KokunoYumeto/modern-latex-manuscripts"
COMMIT_RE = re.compile(r"^[0-9a-fA-F]{40}$")
REPOSITORY_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def raw_url(repository: str, commit: str, path: str) -> str:
    encoded = "/".join(urllib.parse.quote(part, safe="") for part in path.split("/"))
    return f"https://raw.githubusercontent.com/{repository}/{commit}/{encoded}"


def fetch(repository: str, commit: str, path: str) -> bytes:
    request = urllib.request.Request(
        raw_url(repository, commit, path),
        headers={"User-Agent": "modern-latex-manuscripts-adopt/1.0"},
    )
    last_error: Exception | None = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                return response.read()
        except (urllib.error.URLError, TimeoutError) as error:
            last_error = error
            if attempt != 4:
                time.sleep(2**attempt)
    raise RuntimeError(f"could not fetch {path}: {last_error}")


class GitObjectSource:
    """Read exact blobs from one commit in a local Git object database."""

    def __init__(self, repository_path: str, commit: str) -> None:
        resolved_path = Path(repository_path).resolve(strict=True)
        if not resolved_path.is_dir():
            raise RuntimeError(
                "--git must name a checkout or bare-repository root directory"
            )
        self.repository_path = str(resolved_path)
        result = self._run("rev-parse", "--verify", f"{commit}^{{commit}}")
        resolved = result.stdout.decode("ascii", errors="strict").strip().lower()
        if resolved != commit.lower():
            raise RuntimeError("local Git repository did not resolve the approved commit exactly")
        self.commit = resolved

    def _run(self, *arguments: str) -> subprocess.CompletedProcess[bytes]:
        environment = os.environ.copy()
        environment["GIT_NO_LAZY_FETCH"] = "1"
        result = subprocess.run(
            ["git", "-C", self.repository_path, *arguments],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=environment,
            check=False,
        )
        if result.returncode != 0:
            diagnostic = result.stderr.decode("utf-8", errors="replace").strip()
            if len(diagnostic) > 240:
                diagnostic = diagnostic[:237] + "..."
            raise RuntimeError(f"local Git object read failed: {diagnostic or 'unknown error'}")
        return result

    def fetch(self, _repository: str, commit: str, path: str) -> bytes:
        if commit.lower() != self.commit:
            raise RuntimeError("local Git source commit changed during validation")
        return self._run("cat-file", "blob", f"{self.commit}:{path}").stdout


def parse_json(path: str, data: bytes) -> object:
    if data.startswith(b"\xef\xbb\xbf"):
        raise RuntimeError(f"{path} contains a UTF-8 BOM")
    if b"\r" in data:
        raise RuntimeError(f"{path} does not use LF-only line endings")
    try:
        return json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RuntimeError(f"{path} is not valid UTF-8 JSON: {error}") from error


def require_identity(label: str, row: object, path: str, data: bytes) -> None:
    if not isinstance(row, dict):
        raise RuntimeError(f"validation {label} identity is not an object")
    expected = {"path": path, "bytes": len(data), "sha256": sha256(data)}
    for field, value in expected.items():
        if row.get(field) != value:
            raise RuntimeError(
                f"validation {label}.{field} mismatch: "
                f"expected {value!r}, got {row.get(field)!r}"
            )


def require_relative_json_path(path: object) -> str:
    if not isinstance(path, str) or not path or "\\" in path:
        raise RuntimeError("board map_manifest is not a forward-slash relative path")
    parts = path.split("/")
    if path.startswith("/") or ".." in parts or any(not part for part in parts):
        raise RuntimeError("board map_manifest escapes or is not repository-relative")
    return path


FetchFunction = Callable[[str, str, str], bytes]


def validate_snapshot(
    repository: str,
    commit: str,
    fetcher: FetchFunction = fetch,
) -> tuple[bytes, dict[str, object]]:
    board_bytes = fetcher(repository, commit, BOARD_PATH)
    schema_bytes = fetcher(repository, commit, SCHEMA_PATH)
    check_bytes = fetcher(repository, commit, CHECK_PATH)
    board = parse_json(BOARD_PATH, board_bytes)
    schema = parse_json(SCHEMA_PATH, schema_bytes)
    check = parse_json(CHECK_PATH, check_bytes)
    if not isinstance(board, dict) or not isinstance(schema, dict) or not isinstance(check, dict):
        raise RuntimeError("board, schema, and validation must each be JSON objects")

    if check.get("status") != "PASS" or check.get("errors") != []:
        raise RuntimeError("validation must have status PASS and errors []")

    map_path = require_relative_json_path(board.get("map_manifest"))
    map_bytes = fetcher(repository, commit, map_path)
    parse_json(map_path, map_bytes)

    same_commit_paths = [BOARD_PATH, SCHEMA_PATH, CHECK_PATH, map_path]
    policy = board.get("snapshot_policy")
    if not isinstance(policy, dict):
        raise RuntimeError("board snapshot_policy is not an object")
    if policy.get("stable_locator_ref") != "main":
        raise RuntimeError("snapshot_policy stable locator is not main")
    if policy.get("immutable_unit") != "human_approved_exact_commit":
        raise RuntimeError("snapshot_policy immutable unit is not a human-approved commit")
    if policy.get("same_commit_paths") != same_commit_paths:
        raise RuntimeError("snapshot_policy same_commit_paths does not match fetched paths")
    if policy.get("required_checks") != [
        "validation_status_pass",
        "validation_errors_empty",
        "declared_bytes_sha256_match",
        "schema_validation_pass",
    ]:
        raise RuntimeError("snapshot_policy required_checks does not match the v1 contract")
    if policy.get("mixed_revisions_forbidden") is not True:
        raise RuntimeError("snapshot_policy does not forbid mixed revisions")

    require_identity("board", check.get("board"), BOARD_PATH, board_bytes)
    require_identity("schema_file", check.get("schema_file"), SCHEMA_PATH, schema_bytes)
    require_identity("map_manifest", check.get("map_manifest"), map_path, map_bytes)
    if check["board"].get("schema") != board.get("schema"):
        raise RuntimeError("validation board schema identity does not match the board")

    Draft202012Validator.check_schema(schema)
    schema_errors = sorted(
        Draft202012Validator(schema).iter_errors(board),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    if schema_errors:
        first = schema_errors[0]
        location = "/".join(str(part) for part in first.absolute_path) or "<root>"
        raise RuntimeError(
            f"board fails schema validation at {location}: {first.message} "
            f"({len(schema_errors)} error(s))"
        )

    summary: dict[str, object] = {
        "status": "PASS",
        "repository": repository,
        "commit": commit,
        "files": 4,
        "bytes": len(board_bytes) + len(schema_bytes) + len(check_bytes) + len(map_bytes),
        "board_bytes": len(board_bytes),
        "board_sha256": sha256(board_bytes),
        "schema_bytes": len(schema_bytes),
        "schema_sha256": sha256(schema_bytes),
        "validation_bytes": len(check_bytes),
        "validation_sha256": sha256(check_bytes),
        "map_manifest_path": map_path,
        "map_manifest_bytes": len(map_bytes),
        "map_manifest_sha256": sha256(map_bytes),
        "items": len(board.get("items", [])),
        "mirrors": len(board.get("mirrors", [])),
        "item_certification_default": board.get("item_certification_default"),
        "schema_errors": 0,
        "validation_errors": 0,
        "mixed_revisions": 0,
    }
    return board_bytes, summary


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch the four adoption contract files from one exact commit, "
            "verify their identities and schema, and emit the validated board."
        )
    )
    parser.add_argument("--commit", required=True, help="Human-selected 40-hex commit")
    parser.add_argument(
        "--approve",
        required=True,
        help="Repeat the exact approved commit; floating refs are rejected",
    )
    parser.add_argument("--repository", default=DEFAULT_REPOSITORY)
    parser.add_argument(
        "--git",
        metavar="PATH",
        help=(
            "Read exact blobs from this local Git repository instead of the network; "
            "dirty working-tree bytes are ignored"
        ),
    )
    args = parser.parse_args()

    if not COMMIT_RE.fullmatch(args.commit):
        parser.error("--commit must be exactly 40 hexadecimal characters; refs are forbidden")
    if not COMMIT_RE.fullmatch(args.approve):
        parser.error("--approve must repeat the exact 40-hex commit")
    commit = args.commit.lower()
    if args.approve.lower() != commit:
        parser.error("--approve does not match --commit")
    if not REPOSITORY_RE.fullmatch(args.repository):
        parser.error("--repository must have the form owner/name")

    try:
        source = GitObjectSource(args.git, commit) if args.git else None
        board_bytes, summary = validate_snapshot(
            args.repository,
            commit,
            source.fetch if source is not None else fetch,
        )
        summary["transport"] = "local_git_object_database" if source else "raw_github"
        summary["lazy_fetch_disabled"] = source is not None
    except Exception as error:  # one concise fail-closed public interface
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(json.dumps(summary, separators=(",", ":")), file=sys.stderr)
    sys.stdout.buffer.write(board_bytes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
