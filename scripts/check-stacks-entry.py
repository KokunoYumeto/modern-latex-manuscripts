#!/usr/bin/env python3
"""Validate one unregistered Mathematics Commons Stacks overlay candidate offline."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import sys
import unicodedata
from typing import Any, Iterable

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError, ValidationError


VERSION = "1.0.0"
OUTCOME = "VALID_CANDIDATE_UNREGISTERED"
ENTRY_SCHEMA = "stacks-overlay-entry/v1"
MANIFEST_SCHEMA = "stacks-overlay-files/v1"
PIN_SCHEMA = "stacks-upstream-pin/v1"
REGISTRY_SCHEMA = "stacks-overlay-registry/v1"
NAMESPACE_ROOT = "commons/stacks"
NAMESPACE_PATTERN = r"^commons/stacks/[a-z0-9](?:[a-z0-9._-]*[a-z0-9_-])?(?:/[a-z0-9](?:[a-z0-9._-]*[a-z0-9_-])?)*$"
PIN_REPOSITORY = "https://github.com/stacks/stacks-project"
PIN_PATH = "manifests/stacks-pin.json"
REGISTRY_PATH = "manifests/stacks-overlay.json"
SCHEMA_PATH = "manifests/stacks-entry.schema.json"
VALIDATOR_PATH = "scripts/check-stacks-entry.py"
STABLE_ID_PATTERN = re.compile(r"^MC-STX-[A-Z0-9](?:[A-Z0-9._-]{0,94}[A-Z0-9_-])?$")
FORBIDDEN_PATH_CHARACTERS = frozenset('<>:"|?*')
MAX_PATH_BYTES = 500
MAX_SEGMENT_BYTES = 200
MAX_PATH_DEPTH = 32
CONTENT_KINDS = (
    "original_additions",
    "historical_source_mappings",
    "provenance",
    "corrections",
    "multilingual_semantic_links",
    "stable_commons_ids",
    "tests",
    "review_receipts",
)
CONTROL_KINDS = frozenset(("provenance", "tests", "review_receipts"))
ENTRY_KEYS = (
    "schema",
    "state",
    "id",
    "namespace",
    "writer",
    "upstream_pin",
    "overlay",
    "manifest",
    "mathematical_entries",
    "content_counts",
    "review_receipt",
    "tests",
    "revision",
    "boundaries",
)
MANIFEST_KEYS = (
    "schema",
    "entry_id",
    "namespace",
    "path_order",
    "canonical_stream",
    "self_excluding",
    "members",
    "aggregate",
)
MEMBER_KEYS = (
    "path",
    "bytes",
    "sha256",
    "kind",
    "media_type",
    "stable_ids",
    "languages",
    "upstream_locators",
    "historical_source_locators",
    "provenance_receipts",
    "supersedes",
    "rights_notice",
)
AGGREGATE_KEYS = (
    "files",
    "bytes",
    "content_tree_sha256",
    "stable_ids",
    "mathematical_entries",
    "content_counts",
)
WINDOWS_RESERVED = frozenset(
    ("CON", "PRN", "AUX", "NUL")
    + tuple(f"COM{number}" for number in range(1, 10))
    + tuple(f"LPT{number}" for number in range(1, 10))
)


class ContractError(RuntimeError):
    """A deterministic candidate-contract failure."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def strict_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ContractError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def is_reparse(stat_result: os.stat_result) -> bool:
    attribute = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    return bool(getattr(stat_result, "st_file_attributes", 0) & attribute)


def ordinary_file(path: Path, label: str) -> Path:
    require(path.exists(), f"missing {label}")
    result = path.lstat()
    require(not stat.S_ISLNK(result.st_mode), f"symlink rejected for {label}")
    require(not is_reparse(result), f"reparse point rejected for {label}")
    require(stat.S_ISREG(result.st_mode), f"not a regular file for {label}")
    return path.resolve(strict=True)


def ordinary_directory(path: Path, label: str) -> Path:
    require(path.exists(), f"missing {label}")
    result = path.lstat()
    require(not stat.S_ISLNK(result.st_mode), f"symlink rejected for {label}")
    require(not is_reparse(result), f"reparse point rejected for {label}")
    require(stat.S_ISDIR(result.st_mode), f"not a directory for {label}")
    return path.resolve(strict=True)


def strict_json(path: Path, label: str) -> tuple[bytes, dict[str, Any]]:
    resolved = ordinary_file(path, label)
    data = resolved.read_bytes()
    require(not data.startswith(b"\xef\xbb\xbf"), f"{label} contains a UTF-8 BOM")
    require(b"\r" not in data, f"{label} must use LF-only line endings")
    try:
        text = data.decode("utf-8", errors="strict")
        value = json.loads(
            text,
            object_pairs_hook=strict_pairs,
            parse_int=lambda token: bounded_json_integer(token, label),
            parse_float=lambda token: (_ for _ in ()).throw(
                ContractError(f"floating-point JSON value rejected in {label}: {token}")
            ),
            parse_constant=lambda token: (_ for _ in ()).throw(
                ContractError(f"non-finite JSON value in {label}: {token}")
            ),
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        raise ContractError(f"{label} is not strict UTF-8 JSON") from error
    require(type(value) is dict, f"{label} root must be an object")
    return data, value


def bounded_json_integer(token: str, label: str) -> int:
    require(len(token.lstrip("-")) <= 100, f"integer token is too long in {label}")
    return int(token)


def exact_keys(value: Any, expected: Iterable[str], label: str) -> None:
    require(type(value) is dict, f"{label} must be an object")
    require(set(value.keys()) == set(expected), f"{label} fields differ")


def exact_int(value: Any, label: str, minimum: int = 0) -> int:
    require(type(value) is int and value >= minimum, f"{label} must be an integer >= {minimum}")
    return value


def string_list(value: Any, label: str, allow_empty: bool = True) -> list[str]:
    require(type(value) is list, f"{label} must be an array")
    if not allow_empty:
        require(bool(value), f"{label} must not be empty")
    require(all(type(item) is str and item for item in value), f"{label} must contain nonempty strings")
    require(len(value) == len(set(value)), f"{label} contains duplicates")
    return value


def canonical_path(relative: str, label: str) -> PurePosixPath:
    require(type(relative) is str and relative, f"{label} must be a nonempty string")
    require(relative == unicodedata.normalize("NFC", relative), f"{label} is not Unicode NFC")
    require(len(relative.encode("utf-8")) <= MAX_PATH_BYTES, f"{label} exceeds {MAX_PATH_BYTES} UTF-8 bytes")
    require("\\" not in relative, f"backslash rejected in {label}: {relative}")
    require(not relative.startswith("/"), f"absolute path rejected in {label}: {relative}")
    pure = PurePosixPath(relative)
    require(not pure.is_absolute(), f"absolute path rejected in {label}: {relative}")
    require(all(part not in ("", ".", "..") for part in pure.parts), f"unsafe segment in {label}: {relative}")
    require(len(pure.parts) <= MAX_PATH_DEPTH, f"{label} exceeds {MAX_PATH_DEPTH} segments")
    for part in pure.parts:
        require(len(part.encode("utf-8")) <= MAX_SEGMENT_BYTES, f"segment is too long in {label}: {relative}")
        require(not part.endswith((".", " ")), f"trailing dot or space rejected in {label}: {relative}")
        require(not any(character in FORBIDDEN_PATH_CHARACTERS for character in part), f"portable-path character rejected in {label}: {relative}")
        require(all(ord(character) >= 32 and ord(character) != 127 for character in part), f"control character rejected in {label}")
        base = part.split(".", 1)[0].upper()
        require(base not in WINDOWS_RESERVED, f"reserved path segment rejected in {label}: {relative}")
    require(pure.as_posix() == relative, f"non-canonical spelling in {label}: {relative}")
    return pure


def package_file(root: Path, relative: str, label: str) -> Path:
    pure = canonical_path(relative, label)
    current = root
    for part in pure.parts:
        current = current / part
        if current.exists():
            result = current.lstat()
            require(not stat.S_ISLNK(result.st_mode), f"symlink rejected in package path: {relative}")
            require(not is_reparse(result), f"reparse point rejected in package path: {relative}")
    resolved = ordinary_file(current, label)
    try:
        resolved.relative_to(root)
    except ValueError as error:
        raise ContractError(f"package path escapes root: {relative}") from error
    return resolved


def enumerate_package(root: Path) -> list[str]:
    files: list[str] = []

    def visit(directory: Path, prefix: tuple[str, ...]) -> None:
        with os.scandir(directory) as entries:
            for entry in entries:
                relative_parts = prefix + (entry.name,)
                relative = "/".join(relative_parts)
                canonical_path(relative, "package path")
                result = entry.stat(follow_symlinks=False)
                require(not entry.is_symlink(), f"symlink rejected in package: {relative}")
                require(not is_reparse(result), f"reparse point rejected in package: {relative}")
                if stat.S_ISDIR(result.st_mode):
                    visit(Path(entry.path), relative_parts)
                elif stat.S_ISREG(result.st_mode):
                    files.append(relative)
                else:
                    raise ContractError(f"non-regular package object rejected: {relative}")

    visit(root, ())
    return sorted(files, key=lambda value: value.encode("utf-8"))


def identity_matches(identity: dict[str, Any], data: bytes, path: str, label: str) -> None:
    require(identity["path"] == path, f"{label} path differs")
    require(type(identity["bytes"]) is int and identity["bytes"] == len(data), f"{label} byte count differs")
    require(identity["sha256"] == sha256(data), f"{label} SHA-256 differs")


def stable_commons_id(value: str, label: str) -> None:
    require(value == unicodedata.normalize("NFC", value), f"{label} is not Unicode NFC")
    require(value.isascii() and STABLE_ID_PATTERN.fullmatch(value) is not None, f"{label} is not a canonical MC-STX ID")


def namespace_overlap(left: str, right: str) -> bool:
    return left == right or left.startswith(right + "/") or right.startswith(left + "/")


def registry_namespaces(registry: dict[str, Any]) -> list[str]:
    namespaces: list[str] = []
    claims = registry.get("namespace_claims")
    entries = registry.get("entries")
    require(type(claims) is list and type(entries) is list, "registry claims and entries must be arrays")
    for claim in claims:
        if type(claim) is str:
            namespaces.append(claim)
        elif type(claim) is dict and type(claim.get("namespace")) is str:
            namespaces.append(claim["namespace"])
        else:
            raise ContractError("registry namespace claim has unsupported shape")
    for item in entries:
        require(type(item) is dict and type(item.get("namespace")) is str, "registry entry lacks a namespace")
        namespaces.append(item["namespace"])
    return namespaces


def validate_schema(schema: dict[str, Any], entry: dict[str, Any]) -> None:
    try:
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        errors = sorted(validator.iter_errors(entry), key=lambda error: tuple(str(part) for part in error.absolute_path))
    except SchemaError as error:
        raise ContractError(f"candidate schema is invalid: {error.message}") from error
    if errors:
        error = errors[0]
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        raise ContractError(f"candidate schema validation failed at {location}: {error.message}")


def validate_schema_fragment(schema: dict[str, Any], definition: str, value: Any, label: str) -> None:
    definitions = schema.get("$defs")
    require(type(definitions) is dict and definition in definitions, f"candidate schema lacks {definition}")
    try:
        validator = Draft202012Validator(
            {
                "$schema": "https://json-schema.org/draft/2020-12/schema",
                "$defs": definitions,
                "$ref": f"#/$defs/{definition}",
            }
        )
        errors = sorted(validator.iter_errors(value), key=lambda error: tuple(str(part) for part in error.absolute_path))
    except SchemaError as error:
        raise ContractError(f"{label} schema is invalid: {error.message}") from error
    if errors:
        error = errors[0]
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        raise ContractError(f"{label} schema validation failed at {location}: {error.message}")


def validate_manifest_shape(manifest: dict[str, Any]) -> None:
    exact_keys(manifest, MANIFEST_KEYS, "member manifest")
    require(manifest["schema"] == MANIFEST_SCHEMA, "member manifest schema differs")
    require(manifest["path_order"] == "ordinal_utf8_bytes", "member manifest path order differs")
    require(manifest["canonical_stream"] == "path NUL bytes NUL sha256 LF", "member manifest canonical stream differs")
    require(manifest["self_excluding"] is True, "member manifest must be self-excluding")
    require(type(manifest["members"]) is list and manifest["members"], "member manifest must contain members")
    exact_keys(manifest["aggregate"], AGGREGATE_KEYS, "member manifest aggregate")
    exact_keys(manifest["aggregate"]["content_counts"], CONTENT_KINDS, "member manifest content counts")


def validate(
    entry_path: Path,
    package_root: Path,
    schema_path: Path,
    pin_path: Path,
    registry_path: Path,
) -> dict[str, Any]:
    repository_root = Path(__file__).resolve(strict=True).parent.parent
    expected_schema = repository_root / SCHEMA_PATH
    expected_pin = repository_root / PIN_PATH
    expected_registry = repository_root / REGISTRY_PATH
    require(ordinary_file(schema_path, "candidate schema") == expected_schema.resolve(strict=True), f"candidate schema must be {SCHEMA_PATH}")
    require(ordinary_file(pin_path, "upstream pin") == expected_pin.resolve(strict=True), f"upstream pin must be {PIN_PATH}")
    require(ordinary_file(registry_path, "overlay registry") == expected_registry.resolve(strict=True), f"overlay registry must be {REGISTRY_PATH}")
    package = ordinary_directory(package_root, "package root")
    entry_bytes, entry = strict_json(entry_path, "candidate entry")
    schema_bytes, schema = strict_json(schema_path, "candidate schema")
    pin_bytes, pin = strict_json(pin_path, "upstream pin")
    registry_bytes, registry = strict_json(registry_path, "overlay registry")
    validate_schema(schema, entry)
    exact_keys(entry, ENTRY_KEYS, "candidate entry")
    require(entry["schema"] == ENTRY_SCHEMA, "candidate entry schema differs")

    require(pin.get("schema") == PIN_SCHEMA, "upstream pin schema differs")
    require(pin.get("status") == "PASS" and pin.get("errors") == [], "upstream pin is not PASS/errors[]")
    require(registry.get("schema") == REGISTRY_SCHEMA, "overlay registry schema differs")
    require(registry.get("namespace_policy", {}).get("root") == NAMESPACE_ROOT, "overlay registry namespace root differs")
    require(registry.get("namespace_policy", {}).get("entry_pattern") == NAMESPACE_PATTERN, "overlay registry entry pattern differs")
    require(registry.get("namespace_policy", {}).get("one_writer_per_ancestor_chain") is True, "registry ancestor-chain policy differs")
    require(registry.get("namespace_policy", {}).get("registry_control_does_not_claim_overlay_namespace") is True, "registry control claims an overlay namespace")
    require(registry.get("namespace_policy", {}).get("upstream_paths_writable") is False, "registry permits upstream writes")
    registry_pin = registry.get("upstream_pin", {})
    identity_matches(registry_pin.get("receipt", {}), pin_bytes, PIN_PATH, "registry upstream pin receipt")
    require(registry_pin.get("repository") == PIN_REPOSITORY == pin.get("repository", {}).get("url"), "registry upstream repository differs")
    require(registry_pin.get("commit") == pin.get("pin", {}).get("commit"), "registry upstream commit differs")
    require(registry_pin.get("tree") == pin.get("pin", {}).get("tree"), "registry upstream tree differs")
    entry_contract = registry.get("entry_contract", {})
    registry_schema = entry_contract.get("schema", {})
    identity_matches(registry_schema, schema_bytes, SCHEMA_PATH, "registry candidate schema")
    require(registry_schema.get("schema") == ENTRY_SCHEMA, "registry candidate schema name differs")
    validator_bytes = Path(__file__).resolve(strict=True).read_bytes()
    identity_matches(entry_contract.get("validator", {}), validator_bytes, VALIDATOR_PATH, "registry candidate validator")
    require(entry_contract.get("validator", {}).get("version") == VERSION, "registry candidate validator version differs")
    require(entry_contract.get("required_fields") == list(ENTRY_KEYS), "registry required candidate fields differ")
    require(entry_contract.get("allowed_content_kinds") == list(CONTENT_KINDS), "registry allowed content kinds differ")
    require(entry_contract.get("v1_nonempty_entries_allowed") is False, "registry permits nonempty v1 registration")
    require(entry_contract.get("candidate_manifests_accepted") == 0, "registry already reports accepted candidate manifests")
    require(entry_contract.get("registered_entries") == 0, "registry already reports registered entries")
    require(entry_contract.get("content_bound") is False, "registry already reports bound overlay content")

    namespace = entry["namespace"]
    canonical_path(namespace, "candidate namespace")
    require(re.fullmatch(NAMESPACE_PATTERN, namespace) is not None, "candidate namespace violates registry entry pattern")
    require(entry["overlay"]["root"] == namespace, "overlay root differs from candidate namespace")
    require(entry["overlay"]["git_identity_verified"] is False, "materialized replay cannot claim Git identity verification")
    for existing in registry_namespaces(registry):
        canonical_path(existing, "registered namespace")
        require(not namespace_overlap(namespace, existing), f"candidate namespace overlaps registered namespace: {existing}")
    registry_ids = [item.get("id") for item in registry.get("entries", []) if type(item) is dict]
    require(entry["id"] not in registry_ids, "candidate ID already exists in registry")

    pin_receipt = entry["upstream_pin"]["receipt"]
    identity_matches(pin_receipt, pin_bytes, PIN_PATH, "upstream pin receipt")
    require(entry["upstream_pin"]["repository"] == PIN_REPOSITORY == pin["repository"]["url"], "upstream repository differs")
    require(entry["upstream_pin"]["commit"] == pin["pin"]["commit"], "upstream commit differs")
    require(entry["upstream_pin"]["tree"] == pin["pin"]["tree"], "upstream tree differs")
    require(entry["upstream_pin"]["license_sha256"] == pin["license"]["sha256"], "upstream license identity differs")

    manifest_identity = entry["manifest"]
    manifest_relative = manifest_identity["path"]
    require(manifest_relative.startswith(namespace + "/"), "member manifest is outside candidate namespace")
    manifest_path = package_file(package, manifest_relative, "member manifest")
    manifest_bytes, manifest = strict_json(manifest_path, "member manifest")
    identity_matches(manifest_identity, manifest_bytes, manifest_relative, "member manifest identity")
    validate_manifest_shape(manifest)
    validate_schema_fragment(schema, "member_manifest", manifest, "member manifest")
    require(manifest["entry_id"] == entry["id"], "member manifest entry ID differs")
    require(manifest["namespace"] == namespace, "member manifest namespace differs")

    member_rows = manifest["members"]
    member_paths: list[str] = []
    member_by_path: dict[str, dict[str, Any]] = {}
    all_stable_ids: list[str] = []
    content_counts: Counter[str] = Counter()
    total_bytes = 0
    canonical = bytearray()
    casefold_paths: dict[str, str] = {}
    casefold_prefixes: dict[str, str] = {}
    substantive_members = 0
    for index, member in enumerate(member_rows):
        exact_keys(member, MEMBER_KEYS, f"member[{index}]")
        relative = member["path"]
        canonical_path(relative, f"member[{index}].path")
        require(relative.startswith(namespace + "/"), f"member lies outside candidate namespace: {relative}")
        require(relative != manifest_relative, "self-excluding manifest lists itself")
        require(relative not in member_by_path, f"duplicate member path: {relative}")
        folded = relative.casefold()
        require(folded not in casefold_paths, f"case-fold path collision: {relative} and {casefold_paths.get(folded)}")
        casefold_paths[folded] = relative
        prefix_parts: list[str] = []
        for part in PurePosixPath(relative).parts:
            prefix_parts.append(part)
            prefix = "/".join(prefix_parts)
            folded_prefix = prefix.casefold()
            previous_prefix = casefold_prefixes.get(folded_prefix)
            require(previous_prefix in (None, prefix), f"case-fold path-prefix collision: {prefix} and {previous_prefix}")
            casefold_prefixes[folded_prefix] = prefix
        require(member["kind"] in CONTENT_KINDS, f"unsupported content kind for {relative}")
        require(type(member["media_type"]) is str and member["media_type"], f"missing media type for {relative}")
        stable_ids = string_list(member["stable_ids"], f"stable IDs for {relative}")
        for stable_id in stable_ids:
            stable_commons_id(stable_id, f"stable ID for {relative}")
        languages = string_list(member["languages"], f"languages for {relative}")
        upstream_locators = string_list(member["upstream_locators"], f"upstream locators for {relative}")
        historical_locators = string_list(member["historical_source_locators"], f"historical locators for {relative}")
        provenance_receipts = string_list(member["provenance_receipts"], f"provenance receipts for {relative}")
        string_list(member["supersedes"], f"supersession list for {relative}")
        require(type(member["rights_notice"]) is str and member["rights_notice"], f"missing rights notice for {relative}")
        if member["kind"] in CONTROL_KINDS:
            require(not stable_ids, f"control member carries a mathematical stable ID: {relative}")
        else:
            require(bool(stable_ids), f"mathematical member lacks a stable ID: {relative}")
            require(bool(provenance_receipts), f"mathematical member lacks a provenance receipt: {relative}")
            substantive_members += 1
        if member["kind"] == "historical_source_mappings":
            require(bool(historical_locators), f"historical mapping lacks a source locator: {relative}")
        if member["kind"] in ("corrections", "multilingual_semantic_links"):
            require(bool(upstream_locators), f"{member['kind']} member lacks an upstream locator: {relative}")
        data = package_file(package, relative, f"member {relative}").read_bytes()
        exact_int(member["bytes"], f"bytes for {relative}")
        require(member["bytes"] == len(data), f"member byte count differs: {relative}")
        require(member["sha256"] == sha256(data), f"member SHA-256 differs: {relative}")
        member_paths.append(relative)
        member_by_path[relative] = member
        all_stable_ids.extend(stable_ids)
        content_counts[member["kind"]] += 1
        total_bytes += len(data)
        canonical.extend(relative.encode("utf-8"))
        canonical.extend(b"\0")
        canonical.extend(str(len(data)).encode("ascii"))
        canonical.extend(b"\0")
        canonical.extend(member["sha256"].encode("ascii"))
        canonical.extend(b"\n")

    expected_order = sorted(member_paths, key=lambda value: value.encode("utf-8"))
    require(member_paths == expected_order, "member rows are not in ordinal UTF-8 byte order")
    require(len(all_stable_ids) == len(set(all_stable_ids)), "stable Commons IDs are not globally unique")
    require(substantive_members > 0, "candidate package contains no substantive mathematical member")
    attestation_paths = {entry["review_receipt"]["path"]}
    attestation_paths.update(test["path"] for test in entry["tests"])
    subject_canonical = bytearray()
    for member in member_rows:
        if member["path"] in attestation_paths:
            continue
        subject_canonical.extend(member["path"].encode("utf-8"))
        subject_canonical.extend(b"\0")
        subject_canonical.extend(str(member["bytes"]).encode("ascii"))
        subject_canonical.extend(b"\0")
        subject_canonical.extend(member["sha256"].encode("ascii"))
        subject_canonical.extend(b"\n")
    calculated_subject_tree = sha256(bytes(subject_canonical))

    declared_files = [manifest_relative] + member_paths
    folded_manifest = manifest_relative.casefold()
    require(folded_manifest not in casefold_paths, "manifest path case-fold-collides with a member")
    observed_files = enumerate_package(package)
    require(observed_files == sorted(declared_files, key=lambda value: value.encode("utf-8")), "package has missing, extra, or differently named files")

    for member in member_rows:
        for receipt_path in member["provenance_receipts"]:
            require(receipt_path in member_by_path, f"unrepresented provenance receipt: {receipt_path}")
            require(member_by_path[receipt_path]["kind"] in ("provenance", "review_receipts"), f"misclassified provenance receipt: {receipt_path}")

    scope_path = entry["writer"]["scope_receipt"]["path"]
    require(scope_path in member_by_path, "writer scope receipt is not a package member")
    require(member_by_path[scope_path]["kind"] == "provenance", "writer scope receipt is not classified as provenance")
    scope_file = package_file(package, scope_path, "writer scope receipt")
    scope_data, scope_document = strict_json(scope_file, "writer scope receipt")
    identity_matches(entry["writer"]["scope_receipt"], scope_data, scope_path, "writer scope receipt")
    require(member_by_path[scope_path]["media_type"] == "application/json", "writer scope receipt media type must be application/json")
    validate_schema_fragment(schema, "scope_document", scope_document, "writer scope receipt")
    require(scope_document["status"] == "PASS" and scope_document["errors"] == [], "writer scope receipt content is not PASS/errors[]")
    require(scope_document["entry_id"] == entry["id"], "writer scope receipt entry ID differs")
    require(scope_document["namespace"] == namespace, "writer scope receipt namespace differs")
    require(scope_document["writer"] == entry["writer"]["identity"], "writer scope receipt writer differs")
    require(scope_document["overlay_repository"] == entry["overlay"]["repository"], "writer scope receipt repository differs")
    require(scope_document["overlay_commit"] == entry["overlay"]["commit"], "writer scope receipt commit differs")
    require(scope_document["overlay_tree"] == entry["overlay"]["tree"], "writer scope receipt tree differs")

    review_path = entry["review_receipt"]["path"]
    require(review_path in member_by_path, "review receipt is not a package member")
    require(member_by_path[review_path]["kind"] == "review_receipts", "review receipt is not classified as review_receipts")
    review_file = package_file(package, review_path, "review receipt")
    review_data, review_document = strict_json(review_file, "review receipt")
    identity_matches(entry["review_receipt"], review_data, review_path, "review receipt")
    require(member_by_path[review_path]["media_type"] == "application/json", "review receipt media type must be application/json")
    validate_schema_fragment(schema, "review_document", review_document, "review receipt")
    require(review_document["status"] == "PASS" and review_document["errors"] == [], "review receipt content is not PASS/errors[]")
    require(review_document["entry_id"] == entry["id"], "review receipt entry ID differs")
    require(review_document["namespace"] == namespace, "review receipt namespace differs")
    require(review_document["upstream_commit"] == entry["upstream_pin"]["commit"], "review receipt upstream commit differs")
    require(review_document["overlay_commit"] == entry["overlay"]["commit"], "review receipt overlay commit differs")
    require(review_document["overlay_tree"] == entry["overlay"]["tree"], "review receipt overlay tree differs")
    require(review_document["subject_tree_sha256"] == calculated_subject_tree, "review receipt subject tree differs")
    require(review_document["scope"] == entry["review_receipt"]["scope"], "review receipt scope differs")

    test_ids: set[str] = set()
    for test in entry["tests"]:
        require(test["id"] not in test_ids, f"duplicate test ID: {test['id']}")
        test_ids.add(test["id"])
        test_path = test["path"]
        require(test_path in member_by_path, f"test receipt is not a package member: {test_path}")
        require(member_by_path[test_path]["kind"] == "tests", f"test receipt is not classified as tests: {test_path}")
        test_file = package_file(package, test_path, f"test receipt {test_path}")
        test_data, test_document = strict_json(test_file, f"test receipt {test_path}")
        identity_matches(test, test_data, test_path, f"test receipt {test['id']}")
        require(member_by_path[test_path]["media_type"] == "application/json", f"test receipt media type must be application/json: {test_path}")
        validate_schema_fragment(schema, "test_document", test_document, f"test receipt {test_path}")
        require(test_document["status"] == "PASS" and test_document["errors"] == [], f"test receipt content is not PASS/errors[]: {test_path}")
        require(test_document["entry_id"] == entry["id"], f"test receipt entry ID differs: {test_path}")
        require(test_document["namespace"] == namespace, f"test receipt namespace differs: {test_path}")
        require(test_document["upstream_commit"] == entry["upstream_pin"]["commit"], f"test receipt upstream commit differs: {test_path}")
        require(test_document["overlay_commit"] == entry["overlay"]["commit"], f"test receipt overlay commit differs: {test_path}")
        require(test_document["overlay_tree"] == entry["overlay"]["tree"], f"test receipt overlay tree differs: {test_path}")
        require(test_document["subject_tree_sha256"] == calculated_subject_tree, f"test receipt subject tree differs: {test_path}")

    calculated_counts = {kind: content_counts[kind] for kind in CONTENT_KINDS}
    calculated_tree = sha256(bytes(canonical))
    aggregate = manifest["aggregate"]
    exact_int(aggregate["files"], "member manifest file aggregate", minimum=1)
    exact_int(aggregate["bytes"], "member manifest byte aggregate")
    exact_int(aggregate["stable_ids"], "member manifest stable-ID aggregate", minimum=1)
    exact_int(aggregate["mathematical_entries"], "member manifest mathematical-entry aggregate", minimum=1)
    for kind in CONTENT_KINDS:
        exact_int(aggregate["content_counts"][kind], f"member manifest {kind} count")
    require(aggregate["files"] == len(member_rows), "member manifest file aggregate differs")
    require(aggregate["bytes"] == total_bytes, "member manifest byte aggregate differs")
    require(aggregate["content_tree_sha256"] == calculated_tree, "member manifest content tree differs")
    require(aggregate["stable_ids"] == len(all_stable_ids), "member manifest stable-ID aggregate differs")
    require(aggregate["mathematical_entries"] == len(all_stable_ids), "member manifest mathematical-entry aggregate differs")
    require(aggregate["content_counts"] == calculated_counts, "member manifest content-kind counts differ")
    exact_int(manifest_identity["members"], "candidate member count", minimum=1)
    exact_int(entry["mathematical_entries"], "candidate mathematical-entry count", minimum=1)
    for kind in CONTENT_KINDS:
        exact_int(entry["content_counts"][kind], f"candidate {kind} count")
    require(manifest_identity["members"] == len(member_rows), "candidate member count differs")
    require(manifest_identity["content_tree_sha256"] == calculated_tree, "candidate content tree differs")
    require(entry["mathematical_entries"] == len(all_stable_ids), "candidate mathematical-entry count differs")
    require(entry["content_counts"] == calculated_counts, "candidate content-kind counts differ")

    return {
        "schema": "stacks-overlay-entry-check/v1",
        "status": "PASS",
        "errors": [],
        "outcome": OUTCOME,
        "validator": {
            "version": VERSION,
            "runtime": "python_3_11_plus_jsonschema_4_26_0",
            "network": False,
            "git": False,
            "writes": "stdout_only",
        },
        "entry": {
            "source": "candidate_entry_argument",
            "bytes": len(entry_bytes),
            "sha256": sha256(entry_bytes),
            "id": entry["id"],
            "namespace": namespace,
            "state": entry["state"],
        },
        "schema_file": {
            "path": SCHEMA_PATH,
            "bytes": len(schema_bytes),
            "sha256": sha256(schema_bytes),
        },
        "pin": {
            "path": PIN_PATH,
            "bytes": len(pin_bytes),
            "sha256": sha256(pin_bytes),
            "commit": pin["pin"]["commit"],
            "tree": pin["pin"]["tree"],
        },
        "registry": {
            "path": REGISTRY_PATH,
            "bytes": len(registry_bytes),
            "sha256": sha256(registry_bytes),
            "existing_entries": len(registry["entries"]),
        },
        "package": {
            "source": "materialized_candidate_package",
            "manifest": manifest_relative,
            "members": len(member_rows),
            "bytes": total_bytes,
            "content_tree_sha256": calculated_tree,
            "mathematical_entries": len(all_stable_ids),
            "content_counts": calculated_counts,
        },
        "checks": {
            "strict_json": True,
            "schema_valid": True,
            "same_upstream_pin": True,
            "namespace_disjoint": True,
            "paths_safe_and_case_distinct": True,
            "regular_files_only": True,
            "exact_file_set": True,
            "member_bytes_and_hashes": True,
            "content_tree_replayed": True,
            "stable_ids_unique": True,
            "provenance_review_tests_bound": True,
            "state_boundaries_false": True,
        },
        "boundaries": {
            "candidate_registered": False,
            "composition_ready": False,
            "composition_executed": False,
            "git_identity_verified": False,
            "mathematical_certification": False,
            "upstream_approval_or_endorsement": False,
        },
    }


def failure(error: Exception) -> dict[str, Any]:
    return {
        "schema": "stacks-overlay-entry-check/v1",
        "status": "FAIL",
        "errors": [str(error)],
        "outcome": "REJECTED_CANDIDATE",
        "validator": {
            "version": VERSION,
            "network": False,
            "git": False,
            "writes": "stdout_only",
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry", required=True, type=Path, help="candidate entry JSON")
    parser.add_argument("--package", required=True, type=Path, help="materialized candidate package root")
    parser.add_argument("--schema", required=True, type=Path, help="candidate entry JSON Schema")
    parser.add_argument("--pin", required=True, type=Path, help="exact upstream pin receipt")
    parser.add_argument("--registry", required=True, type=Path, help="current Commons overlay registry")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        report = validate(args.entry, args.package, args.schema, args.pin, args.registry)
        code = 0
    except OSError as error:
        report = failure(ContractError(f"filesystem operation failed: {error.__class__.__name__}"))
        code = 12
    except (ContractError, ValidationError, KeyError, TypeError) as error:
        report = failure(error)
        code = 12
    sys.stdout.write(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
