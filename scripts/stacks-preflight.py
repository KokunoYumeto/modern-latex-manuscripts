#!/usr/bin/env python3
"""Validate the exact empty Stacks overlay composition preflight offline."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys
from typing import Any


TOOL_PATH = "scripts/stacks-preflight.py"
REGRESSION_PATH = "scripts/test-stacks-preflight.py"
PIN_PATH = "manifests/stacks-pin.json"
REGISTRY_PATH = "manifests/stacks-overlay.json"
CONTRACT_PATH = "manifests/stacks-compose.json"
RESULT_PATH = "manifests/stacks-preflight.json"
VERSION = "1.0.0"
OUTCOME = "BLOCKED_EMPTY_OVERLAY_REGISTRY"


class ContractError(RuntimeError):
    def __init__(self, message: str, code: int = 12) -> None:
        super().__init__(message)
        self.code = code


def require(condition: bool, message: str, code: int = 12) -> None:
    if not condition:
        raise ContractError(message, code)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def safe_file(root: Path, relative: str) -> Path:
    require("\\" not in relative, f"non-canonical path: {relative}", 10)
    pure = PurePosixPath(relative)
    require(not pure.is_absolute(), f"absolute path rejected: {relative}", 10)
    require(all(part not in ("", ".", "..") for part in pure.parts), f"unsafe path: {relative}", 10)
    current = root
    for part in pure.parts:
        current = current / part
        require(not current.is_symlink(), f"symlink rejected: {relative}", 10)
    try:
        resolved = current.resolve(strict=True)
        resolved.relative_to(root)
    except (FileNotFoundError, ValueError) as error:
        raise ContractError(f"missing or escaping path: {relative}", 10) from error
    require(resolved.is_file(), f"not a file: {relative}", 10)
    return resolved


def strict_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ContractError(f"duplicate JSON key: {key}", 10)
        result[key] = value
    return result


def strict_json(path: Path, label: str) -> tuple[bytes, dict[str, Any]]:
    data = path.read_bytes()
    require(not data.startswith(b"\xef\xbb\xbf"), f"{label} contains a UTF-8 BOM", 10)
    require(b"\r" not in data, f"{label} must use LF line endings", 10)
    try:
        text = data.decode("utf-8", errors="strict")
        value = json.loads(
            text,
            object_pairs_hook=strict_pairs,
            parse_constant=lambda token: (_ for _ in ()).throw(ContractError(f"non-finite JSON value: {token}", 10)),
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ContractError(f"{label} is not strict UTF-8 JSON", 10) from error
    require(type(value) is dict, f"{label} root must be an object", 10)
    return data, value


def exact_keys(value: Any, expected: tuple[str, ...], label: str) -> None:
    require(type(value) is dict, f"{label} must be an object")
    require(tuple(value.keys()) == expected, f"{label} fields or order differ")


def exact_int(value: Any, expected: int, label: str) -> None:
    require(type(value) is int and value == expected, f"{label} must be integer {expected}")


def exact_bool(value: Any, expected: bool, label: str) -> None:
    require(type(value) is bool and value is expected, f"{label} must be boolean {str(expected).lower()}")


def exact_empty_list(value: Any, label: str) -> None:
    require(type(value) is list and not value, f"{label} must be an empty array")


def validate(root: Path) -> dict[str, Any]:
    tool_path = safe_file(root, TOOL_PATH)
    require(tool_path == Path(__file__).resolve(strict=True), "running tool is not the bound repository path")
    regression_path = safe_file(root, REGRESSION_PATH)
    pin_path = safe_file(root, PIN_PATH)
    registry_path = safe_file(root, REGISTRY_PATH)
    contract_path = safe_file(root, CONTRACT_PATH)

    tool_bytes = tool_path.read_bytes()
    regression_bytes = regression_path.read_bytes()
    pin_bytes, pin = strict_json(pin_path, "upstream pin")
    registry_bytes, registry = strict_json(registry_path, "overlay registry")
    contract_bytes, contract = strict_json(contract_path, "composition contract")

    exact_keys(
        registry,
        (
            "schema", "state", "role", "governance", "control_file_rights",
            "upstream_license_scope", "upstream_pin", "namespace_policy",
            "entry_contract", "namespace_claims", "entries", "aggregate",
            "boundaries", "next_cursor",
        ),
        "overlay registry",
    )
    require(registry["schema"] == "stacks-overlay-registry/v1", "registry schema differs")
    require(registry["state"] == "initialized_empty", "registry state is not initialized_empty")
    exact_keys(registry["upstream_pin"], ("receipt", "repository", "commit", "tree"), "registry upstream pin")
    exact_keys(registry["upstream_pin"]["receipt"], ("path", "bytes", "sha256"), "registry upstream pin receipt")
    receipt = registry["upstream_pin"]["receipt"]
    require(receipt["path"] == PIN_PATH, "upstream pin receipt path differs", 11)
    require(type(receipt["bytes"]) is int and receipt["bytes"] == len(pin_bytes), "upstream pin receipt bytes differ", 11)
    require(receipt["sha256"] == sha256(pin_bytes), "upstream pin receipt SHA-256 differs", 11)
    require(pin["schema"] == "stacks-upstream-pin/v1", "upstream pin schema differs", 11)
    require(pin["status"] == "PASS" and type(pin["errors"]) is list and not pin["errors"], "upstream pin is not PASS/errors[]", 11)
    require(pin["repository"]["url"] == registry["upstream_pin"]["repository"], "upstream repository differs across pin and registry", 11)
    require(pin["pin"]["commit"] == registry["upstream_pin"]["commit"], "upstream commit differs across pin and registry", 11)
    require(pin["pin"]["tree"] == registry["upstream_pin"]["tree"], "upstream tree differs across pin and registry", 11)
    exact_bool(pin["boundaries"]["upstream_tree_copied_into_commons"], False, "upstream pin copied-tree boundary")
    exact_bool(pin["boundaries"]["commons_overlay_bound"], False, "upstream pin overlay boundary")
    exact_bool(pin["boundaries"]["composed_build_bound"], False, "upstream pin build boundary")
    exact_bool(pin["boundaries"]["modified_edition_bound"], False, "upstream pin modified-edition boundary")
    exact_bool(registry["entry_contract"]["v1_nonempty_entries_allowed"], False, "nonempty-entry gate")
    exact_empty_list(registry["namespace_claims"], "namespace claims")
    exact_empty_list(registry["entries"], "registry entries")
    for field in (
        "registry_entries", "registered_namespaces", "registered_mathematical_entries",
        "registered_overlay_files", "registered_overlay_bytes", "historical_source_mappings",
        "corrections", "multilingual_semantic_links", "commons_assertion_ids_allocated",
        "tests", "review_receipts",
    ):
        exact_int(registry["aggregate"][field], 0, f"registry aggregate.{field}")
    exact_bool(registry["boundaries"]["content_bearing_commons_overlay_bound"], False, "content overlay boundary")
    require(registry["boundaries"]["overlay_content_commit"] is None, "overlay content commit must remain null")
    require(registry["boundaries"]["overlay_content_tree"] is None, "overlay content tree must remain null")
    exact_bool(registry["boundaries"]["upstream_tree_copied_into_commons"], False, "registry copied-tree boundary")
    exact_int(registry["boundaries"]["upstream_payload_files_added"], 0, "registry upstream payload file count")
    exact_int(registry["boundaries"]["upstream_payload_bytes_added"], 0, "registry upstream payload byte count")
    exact_int(registry["boundaries"]["archives_or_binary_payloads_added"], 0, "registry archive/binary count")
    exact_bool(registry["boundaries"]["composed_build_bound"], False, "composed-build boundary")
    exact_bool(registry["boundaries"]["modified_edition_bound"], False, "modified-edition boundary")
    exact_int(registry["boundaries"]["reader_or_edition_files_added"], 0, "registry reader/edition count")
    exact_bool(registry["boundaries"]["mathematical_review_claimed"], False, "registry review boundary")
    exact_bool(registry["boundaries"]["upstream_acceptance_dependency"], False, "registry acceptance boundary")
    exact_bool(registry["boundaries"]["upstream_endorsement_implied"], False, "registry endorsement boundary")

    exact_keys(
        contract,
        (
            "schema", "state", "role", "control_file_rights", "inputs",
            "determinism", "preflight_tool", "regression", "tool", "preconditions", "fixture",
            "output", "aggregate", "boundaries", "next_cursor",
        ),
        "composition contract",
    )
    require(contract["schema"] == "stacks-composition-contract/v1", "composition schema differs")
    require(contract["state"] == "executable_preflight_bound_empty_registry", "composition state differs")
    upstream = contract["inputs"]["upstream"]
    exact_keys(upstream, ("repository", "commit", "tree", "tree_replayed_into_commons"), "composition upstream input")
    require(upstream["repository"] == pin["repository"]["url"], "composition repository differs from pin", 11)
    require(upstream["commit"] == pin["pin"]["commit"], "composition commit differs from pin", 11)
    require(upstream["tree"] == pin["pin"]["tree"], "composition tree differs from pin", 11)
    exact_bool(upstream["tree_replayed_into_commons"], False, "composition copied-tree input")
    overlay = contract["inputs"]["overlay_registry"]
    require(overlay["path"] == REGISTRY_PATH, "registry path binding differs", 11)
    require(type(overlay["bytes"]) is int and overlay["bytes"] == len(registry_bytes), "registry byte binding differs", 11)
    require(overlay["sha256"] == sha256(registry_bytes), "registry SHA-256 binding differs", 11)
    exact_int(overlay["entries"], 0, "registry entry binding")
    require(contract["inputs"]["selected_overlay_id"] is None, "overlay selection must remain null")
    require(contract["inputs"]["selected_overlay_commit"] is None, "overlay commit must remain null")
    require(contract["inputs"]["selected_overlay_tree"] is None, "overlay tree must remain null")

    preflight_tool = contract["preflight_tool"]
    exact_keys(
        preflight_tool,
        ("state", "capability", "path", "version", "runtime", "invocation", "bytes", "sha256", "network", "git", "writes"),
        "preflight tool identity",
    )
    require(preflight_tool["state"] == "bound", "preflight tool state differs", 11)
    require(preflight_tool["capability"] == "validation_only_no_composition", "preflight tool capability differs", 11)
    require(preflight_tool["path"] == TOOL_PATH and preflight_tool["version"] == VERSION, "preflight tool path or version differs", 11)
    require(preflight_tool["runtime"] == "python_stdlib_3_11_plus", "preflight runtime differs", 11)
    require(preflight_tool["invocation"] == "python scripts/stacks-preflight.py --root . --expect BLOCKED_EMPTY_OVERLAY_REGISTRY", "preflight invocation differs", 11)
    require(type(preflight_tool["bytes"]) is int and preflight_tool["bytes"] == len(tool_bytes), "preflight tool byte binding differs", 11)
    require(preflight_tool["sha256"] == sha256(tool_bytes), "preflight tool SHA-256 binding differs", 11)
    exact_bool(preflight_tool["network"], False, "preflight network boundary")
    exact_bool(preflight_tool["git"], False, "preflight Git boundary")
    require(preflight_tool["writes"] == "stdout_only", "preflight write boundary differs", 11)

    regression = contract["regression"]
    exact_keys(regression, ("path", "version", "bytes", "sha256", "cases"), "regression identity")
    require(regression["path"] == REGRESSION_PATH and regression["version"] == VERSION, "regression path or version differs", 11)
    require(type(regression["bytes"]) is int and regression["bytes"] == len(regression_bytes), "regression byte binding differs", 11)
    require(regression["sha256"] == sha256(regression_bytes), "regression SHA-256 binding differs", 11)
    exact_int(regression["cases"], 11, "regression case count")

    tool = contract["tool"]
    exact_keys(tool, ("state", "path", "version", "sha256"), "composition tool identity")
    require(tool["state"] == "not_bound", "composition tool must remain unbound")
    require(tool["path"] is None and tool["version"] is None and tool["sha256"] is None, "composition tool identity must remain null")

    pre = contract["preconditions"]
    exact_bool(pre["upstream_pin_bound"], True, "upstream pin precondition")
    exact_bool(pre["upstream_tree_replayed"], False, "upstream replay precondition")
    exact_bool(pre["approved_overlay_selected"], False, "overlay selection precondition")
    exact_bool(pre["overlay_identity_verified"], False, "overlay identity precondition")
    exact_bool(pre["preflight_tool_bound"], True, "preflight tool precondition")
    exact_bool(pre["tool_identity_bound"], False, "composition tool precondition")
    exact_bool(pre["output_root_declared"], False, "output-root precondition")
    exact_bool(pre["ready"], False, "composition readiness")

    fixture = contract["fixture"]
    require(fixture["id"] == "empty-overlay-preflight", "fixture ID differs")
    require(fixture["receipt"] == RESULT_PATH, "fixture receipt path differs")
    require(fixture["expected_outcome"] == OUTCOME and fixture["observed_outcome"] == OUTCOME, "fixture outcome differs")
    exact_bool(fixture["outcome_matches"], True, "fixture outcome match")
    exact_bool(fixture["composition_executed"], False, "fixture execution state")
    exact_empty_list(contract["output"]["members"], "output members")
    for field in ("manifest", "tree", "bytes", "sha256"):
        require(contract["output"][field] is None, f"output.{field} must remain null")
    exact_int(contract["aggregate"]["static_contract_checks"], 1, "static contract check count")
    exact_int(contract["aggregate"]["executable_preflight_runs"], 1, "executable preflight run count")
    for field in ("composition_runs", "generated_members", "builds"):
        exact_int(contract["aggregate"][field], 0, f"composition aggregate.{field}")
    for field in (
        "overlay_content_bound", "composed_edition_bound", "composed_build_bound",
        "modified_edition_bound", "upstream_endorsement_implied", "mathematical_review_claimed",
    ):
        exact_bool(contract["boundaries"][field], False, f"composition boundary.{field}")
    exact_bool(contract["boundaries"]["contract_fixture_only"], True, "composition fixture-only boundary")
    for field in (
        "upstream_payload_files_added", "upstream_payload_bytes_added",
        "archives_or_binary_payloads_added", "reader_or_edition_files_added",
    ):
        exact_int(contract["boundaries"][field], 0, f"composition boundary.{field}")

    return {
        "schema": "stacks-composition-preflight/v1",
        "status": "PASS",
        "errors": [],
        "outcome": OUTCOME,
        "preflight_tool": {
            "path": TOOL_PATH,
            "version": VERSION,
            "bytes": len(tool_bytes),
            "sha256": sha256(tool_bytes),
            "capability": "validation_only_no_composition",
        },
        "inputs": {
            "upstream_pin": {
                "path": PIN_PATH,
                "bytes": len(pin_bytes),
                "sha256": sha256(pin_bytes),
                "repository": pin["repository"]["url"],
                "commit": pin["pin"]["commit"],
                "tree": pin["pin"]["tree"],
            },
            "overlay_registry": {
                "path": REGISTRY_PATH,
                "bytes": len(registry_bytes),
                "sha256": sha256(registry_bytes),
                "entries": 0,
            },
            "composition_contract": {
                "path": CONTRACT_PATH,
                "bytes": len(contract_bytes),
                "sha256": sha256(contract_bytes),
            },
        },
        "regression": {
            "path": REGRESSION_PATH,
            "version": VERSION,
            "bytes": len(regression_bytes),
            "sha256": sha256(regression_bytes),
            "cases": 11,
        },
        "preconditions": {
            "upstream_pin_bound": True,
            "empty_registry_verified": True,
            "preflight_tool_bound": True,
            "composition_tool_bound": False,
            "composition_ready": False,
        },
        "output": {
            "composition_executed": False,
            "manifest": None,
            "tree": None,
            "members": [],
            "bytes": None,
            "sha256": None,
        },
        "checks": {
            "strict_json": True,
            "duplicate_keys_rejected": True,
            "utf8_lf_no_bom": True,
            "fixed_paths_and_symlinks_rejected": True,
            "pin_identity_matches_registry_and_contract": True,
            "registry_identity_matches_contract": True,
            "tool_identity_matches_contract": True,
            "regression_identity_matches_contract": True,
            "empty_registry": True,
            "network_queried": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--expect", choices=[OUTCOME])
    args = parser.parse_args()
    try:
        root = Path(args.root).resolve(strict=True)
        require(root.is_dir(), "--root must be a directory")
        result = validate(root)
    except ContractError as error:
        sys.stderr.buffer.write((json.dumps({"status": "ERROR", "code": error.code, "error": str(error)}, separators=(",", ":")) + "\n").encode("utf-8"))
        return error.code
    except OSError as error:
        sys.stderr.buffer.write((json.dumps({"status": "ERROR", "code": 10, "error": str(error)}, separators=(",", ":")) + "\n").encode("utf-8"))
        return 10
    except Exception as error:
        sys.stderr.buffer.write((json.dumps({"status": "ERROR", "code": 14, "error": type(error).__name__}, separators=(",", ":")) + "\n").encode("utf-8"))
        return 14
    sys.stdout.buffer.write((json.dumps(result, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
    return 0 if args.expect == OUTCOME else 20


if __name__ == "__main__":
    raise SystemExit(main())
