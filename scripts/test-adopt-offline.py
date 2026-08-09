#!/usr/bin/env python3
"""Prove that local adoption reads fail closed instead of lazy-fetching blobs."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile


BOARD_PATH = "manifests/adopt.json"
SCHEMA_PATH = "manifests/adopt.schema.json"
CHECK_PATH = "manifests/adopt.check.json"
DEFAULT_REPOSITORY = "KokunoYumeto/modern-latex-manuscripts"
COMMIT_RE = re.compile(r"^[0-9a-fA-F]{40}$")


def run(
    command: list[str],
    *,
    data: bytes | None = None,
    check: bool = True,
    timeout: int = 60,
) -> subprocess.CompletedProcess[bytes]:
    result = subprocess.run(
        command,
        input=data,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        timeout=timeout,
    )
    if check and result.returncode != 0:
        diagnostic = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"command failed ({result.returncode}): {diagnostic}")
    return result


def git(repository: Path, *arguments: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return run(["git", "-C", str(repository), *arguments], check=check)


def object_bytes(repository: Path, object_type: str, object_id: str) -> bytes:
    return git(repository, "cat-file", object_type, object_id).stdout


def copy_object(source: Path, target: Path, object_type: str, object_id: str) -> None:
    result = run(
        ["git", "-C", str(target), "hash-object", "-w", "-t", object_type, "--stdin"],
        data=object_bytes(source, object_type, object_id),
    )
    written = result.stdout.decode("ascii", errors="strict").strip().lower()
    if written != object_id.lower():
        raise RuntimeError(f"copied {object_type} identity changed: {object_id} -> {written}")


def resolve(source: Path, expression: str) -> str:
    return git(source, "rev-parse", "--verify", expression).stdout.decode("ascii").strip().lower()


def tree_ids(source: Path, commit: str, paths: list[str]) -> set[str]:
    root = resolve(source, f"{commit}^{{tree}}")
    identifiers = {root}
    for path in paths:
        current = root
        for component in Path(path).parts[:-1]:
            listing = git(source, "ls-tree", current, "--", component).stdout.strip()
            metadata, _separator, _path = listing.partition(b"\t")
            _mode, object_type, object_id = metadata.split(b" ", 2)
            if object_type != b"tree":
                raise RuntimeError(f"contract parent is not a tree: {path}")
            current = object_id.decode("ascii").lower()
            identifiers.add(current)
    return identifiers


def configure_promisor(repository: Path) -> None:
    git(repository, "config", "core.repositoryformatversion", "1")
    git(repository, "remote", "add", "origin", "http://127.0.0.1:9/unreachable")
    git(repository, "config", "remote.origin.promisor", "true")
    git(repository, "config", "remote.origin.partialclonefilter", "blob:none")
    git(repository, "config", "extensions.partialClone", "origin")


def helper_command(
    helper: Path,
    repository: str,
    commit: str,
    object_database: Path,
) -> list[str]:
    return [
        sys.executable,
        str(helper),
        "--repository",
        repository,
        "--commit",
        commit,
        "--approve",
        commit,
        "--git",
        str(object_database),
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--repository", default=DEFAULT_REPOSITORY)
    parser.add_argument("--git", default=".", help="Source checkout or bare repository root")
    args = parser.parse_args()
    if not COMMIT_RE.fullmatch(args.commit):
        parser.error("--commit must be exactly 40 hexadecimal characters")

    source = Path(args.git).resolve(strict=True)
    if not source.is_dir():
        parser.error("--git must name a checkout or bare-repository root directory")
    commit = resolve(source, f"{args.commit.lower()}^{{commit}}")
    helper = Path(__file__).with_name("get-adopt.py").resolve(strict=True)
    board_bytes = object_bytes(source, "blob", resolve(source, f"{commit}:{BOARD_PATH}"))
    board = json.loads(board_bytes.decode("utf-8"))
    map_path = str(board["map_manifest"])
    contract_paths = [BOARD_PATH, SCHEMA_PATH, CHECK_PATH, map_path]
    contract_blobs = {path: resolve(source, f"{commit}:{path}") for path in contract_paths}

    with tempfile.TemporaryDirectory(prefix="adopt-offline-") as temporary:
        promisor = Path(temporary) / "promisor.git"
        run(["git", "init", "--bare", str(promisor)])
        configure_promisor(promisor)
        copy_object(source, promisor, "commit", commit)
        for identifier in sorted(tree_ids(source, commit, contract_paths)):
            copy_object(source, promisor, "tree", identifier)

        environment = os.environ.copy()
        environment["GIT_TERMINAL_PROMPT"] = "0"
        missing = subprocess.run(
            helper_command(helper, args.repository, commit, promisor),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=30,
            env=environment,
        )
        missing_diagnostic = missing.stderr.decode("utf-8", errors="replace")
        if missing.returncode == 0:
            raise RuntimeError("helper accepted a promisor repository with missing contract blobs")
        network_markers = ("127.0.0.1", "unable to access", "fetch-pack", "git fetch")
        attempted_remote = any(marker in missing_diagnostic for marker in network_markers)
        if attempted_remote:
            raise RuntimeError(f"missing-blob read attempted the promisor remote: {missing_diagnostic}")

        for path in contract_paths:
            copy_object(source, promisor, "blob", contract_blobs[path])
        complete = subprocess.run(
            helper_command(helper, args.repository, commit, promisor),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=30,
            env=environment,
        )
        if complete.returncode != 0:
            diagnostic = complete.stderr.decode("utf-8", errors="replace").strip()
            raise RuntimeError(f"materialized promisor replay failed: {diagnostic}")
        if complete.stdout != board_bytes:
            raise RuntimeError("materialized promisor replay changed the board bytes")
        summary = json.loads(complete.stderr.decode("utf-8"))
        if summary.get("transport") != "local_git_object_database":
            raise RuntimeError("materialized replay did not report local Git transport")
        if summary.get("lazy_fetch_disabled") is not True:
            raise RuntimeError("materialized replay did not report lazy-fetch prevention")

    print(
        json.dumps(
            {
                "status": "PASS",
                "commit": commit,
                "missing_blob_exit": missing.returncode,
                "missing_blob_remote_attempt": False,
                "materialized_files": summary["files"],
                "materialized_bytes": summary["bytes"],
                "materialized_transport": summary["transport"],
                "lazy_fetch_disabled": summary["lazy_fetch_disabled"],
            },
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
