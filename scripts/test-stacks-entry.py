#!/usr/bin/env python3
"""Exercise the offline Stacks overlay-candidate validator with synthetic fixtures."""

from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from typing import Any, Callable


VERSION = "1.0.0"
NAMESPACE = "commons/stacks/test-entry"
ENTRY_ID = "commons-stacks-test-entry-v1"
WRITER = "synthetic-regression-writer"
OVERLAY_REPOSITORY = "https://github.com/example/commons-stacks-overlay"
OVERLAY_COMMIT = "1" * 40
OVERLAY_TREE = "2" * 40
VALID_OUTCOME = "VALID_CANDIDATE_UNREGISTERED"
KINDS = (
    "original_additions",
    "historical_source_mappings",
    "provenance",
    "corrections",
    "multilingual_semantic_links",
    "stable_commons_ids",
    "tests",
    "review_receipts",
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def identity(path: str, data: bytes) -> dict[str, Any]:
    return {"path": path, "bytes": len(data), "sha256": sha256(data)}


def member(
    path: str,
    data: bytes,
    kind: str,
    *,
    stable_ids: list[str] | None = None,
    languages: list[str] | None = None,
    upstream_locators: list[str] | None = None,
    historical_source_locators: list[str] | None = None,
    provenance_receipts: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "path": path,
        "bytes": len(data),
        "sha256": sha256(data),
        "kind": kind,
        "media_type": "application/json" if path.endswith(".json") else "text/x-tex",
        "stable_ids": stable_ids or [],
        "languages": languages or [],
        "upstream_locators": upstream_locators or [],
        "historical_source_locators": historical_source_locators or [],
        "provenance_receipts": provenance_receipts or [],
        "supersedes": [],
        "rights_notice": "synthetic regression fixture; no mathematical or upstream payload",
    }


def content_tree(rows: list[dict[str, Any]]) -> str:
    stream = bytearray()
    for row in rows:
        stream.extend(row["path"].encode("utf-8"))
        stream.extend(b"\0")
        stream.extend(str(row["bytes"]).encode("ascii"))
        stream.extend(b"\0")
        stream.extend(row["sha256"].encode("ascii"))
        stream.extend(b"\n")
    return sha256(bytes(stream))


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    counts = {kind: 0 for kind in KINDS}
    stable_ids: list[str] = []
    for row in rows:
        counts[row["kind"]] += 1
        stable_ids.extend(row["stable_ids"])
    return {
        "files": len(rows),
        "bytes": sum(row["bytes"] for row in rows),
        "content_tree_sha256": content_tree(rows),
        "stable_ids": len(stable_ids),
        "mathematical_entries": len(stable_ids),
        "content_counts": counts,
    }


class Fixture:
    def __init__(self, case_root: Path, repo_root: Path) -> None:
        self.case_root = case_root
        self.repo_root = repo_root
        self.package = case_root / "package"
        self.entry_path = case_root / "entry.json"
        self.control_root = case_root / "control"
        for relative in (
            "manifests/stacks-overlay.json",
            "manifests/stacks-pin.json",
            "manifests/stacks-entry.schema.json",
            "scripts/check-stacks-entry.py",
        ):
            source = repo_root / Path(*relative.split("/"))
            target = self.control_root / Path(*relative.split("/"))
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        self.registry_path = self.control_root / "manifests" / "stacks-overlay.json"
        self.pin_path = self.control_root / "manifests" / "stacks-pin.json"
        self.schema_path = self.control_root / "manifests" / "stacks-entry.schema.json"
        self.validator_path = self.control_root / "scripts" / "check-stacks-entry.py"
        self.manifest_path = f"{NAMESPACE}/files.json"
        self.scope_path = f"{NAMESPACE}/scope.json"
        self.review_path = f"{NAMESPACE}/review.json"
        self.test_path = f"{NAMESPACE}/test.json"
        self.math_path = f"{NAMESPACE}/math.tex"

        pin_data = self.pin_path.read_bytes()
        pin = json.loads(pin_data.decode("utf-8"))
        scope_data = json_bytes(
            {
                "schema": "synthetic-scope/v1",
                "status": "PASS",
                "errors": [],
                "entry_id": ENTRY_ID,
                "namespace": NAMESPACE,
                "writer": WRITER,
                "overlay_repository": OVERLAY_REPOSITORY,
                "overlay_commit": OVERLAY_COMMIT,
                "overlay_tree": OVERLAY_TREE,
                "scope": "writer_scope_and_namespace_attestation_not_mathematical_certification",
            }
        )
        math_data = b"% synthetic validator fixture; not mathematical content\n\\def\\Fixture{1}\n"
        math_row = member(
            self.math_path,
            math_data,
            "original_additions",
            stable_ids=["MC-STX-TEST-0001"],
            languages=["en"],
            upstream_locators=["stacks-pin:a04446e57ec1fbc252a871afcec7752fb2807b14"],
            provenance_receipts=[self.scope_path],
        )
        scope_row = member(self.scope_path, scope_data, "provenance")
        subject_rows = sorted(
            [math_row, scope_row], key=lambda row: row["path"].encode("utf-8")
        )
        subject = {
            "entry_id": ENTRY_ID,
            "namespace": NAMESPACE,
            "upstream_commit": pin["pin"]["commit"],
            "overlay_commit": OVERLAY_COMMIT,
            "overlay_tree": OVERLAY_TREE,
            "subject_tree_sha256": content_tree(subject_rows),
        }
        review_data = json_bytes(
            {
                "schema": "synthetic-review/v1",
                "status": "PASS",
                "errors": [],
                **subject,
                "scope": "bounded_candidate_entry_review_not_mathematical_certification",
            }
        )
        test_data = json_bytes({"schema": "synthetic-test/v1", "status": "PASS", "errors": [], **subject})
        for path, data in (
            (self.scope_path, scope_data),
            (self.review_path, review_data),
            (self.test_path, test_data),
            (self.math_path, math_data),
        ):
            write_bytes(self.package / Path(*path.split("/")), data)

        self.rows = [
            math_row,
            member(self.review_path, review_data, "review_receipts"),
            scope_row,
            member(self.test_path, test_data, "tests"),
        ]
        self.rows.sort(key=lambda row: row["path"].encode("utf-8"))
        self.manifest = {
            "schema": "stacks-overlay-files/v1",
            "entry_id": ENTRY_ID,
            "namespace": NAMESPACE,
            "path_order": "ordinal_utf8_bytes",
            "canonical_stream": "path NUL bytes NUL sha256 LF",
            "self_excluding": True,
            "members": self.rows,
            "aggregate": aggregate(self.rows),
        }
        self.write_manifest()

        manifest_data = (self.package / Path(*self.manifest_path.split("/"))).read_bytes()
        counts = self.manifest["aggregate"]["content_counts"]
        self.entry = {
            "schema": "stacks-overlay-entry/v1",
            "state": "candidate_unregistered",
            "id": ENTRY_ID,
            "namespace": NAMESPACE,
            "writer": {
                "identity": WRITER,
                "repository": OVERLAY_REPOSITORY,
                "scope_receipt": identity(self.scope_path, scope_data),
            },
            "upstream_pin": {
                "receipt": identity("manifests/stacks-pin.json", pin_data),
                "repository": pin["repository"]["url"],
                "commit": pin["pin"]["commit"],
                "tree": pin["pin"]["tree"],
                "license_sha256": pin["license"]["sha256"],
            },
            "overlay": {
                "repository": OVERLAY_REPOSITORY,
                "commit": OVERLAY_COMMIT,
                "tree": OVERLAY_TREE,
                "root": NAMESPACE,
                "git_identity_verified": False,
            },
            "manifest": {
                **identity(self.manifest_path, manifest_data),
                "content_tree_sha256": self.manifest["aggregate"]["content_tree_sha256"],
                "members": len(self.rows),
            },
            "mathematical_entries": 1,
            "content_counts": counts,
            "review_receipt": {
                **identity(self.review_path, review_data),
                "status": "PASS",
                "errors": [],
                "scope": "bounded_candidate_entry_review_not_mathematical_certification",
            },
            "tests": [
                {
                    "id": "synthetic-validator-pass",
                    **identity(self.test_path, test_data),
                    "status": "PASS",
                    "errors": [],
                }
            ],
            "revision": {"predecessors": [], "supersedes": [], "reversals": []},
            "boundaries": {
                "registered": False,
                "composition_ready": False,
                "composition_executed": False,
                "modified_edition": False,
                "mathematical_certification_claimed": False,
                "upstream_approval_claimed": False,
                "upstream_endorsement_implied": False,
            },
        }
        self.write_entry()

    def write_manifest(self, *, rebind: bool = True) -> None:
        data = json_bytes(self.manifest)
        write_bytes(self.package / Path(*self.manifest_path.split("/")), data)
        if rebind and hasattr(self, "entry"):
            self.entry["manifest"]["bytes"] = len(data)
            self.entry["manifest"]["sha256"] = sha256(data)
            self.write_entry()

    def write_entry(self, data: bytes | None = None) -> None:
        write_bytes(self.entry_path, data if data is not None else json_bytes(self.entry))

    def refresh_manifest(self) -> None:
        self.manifest["aggregate"] = aggregate(self.manifest["members"])
        self.entry["content_counts"] = deepcopy(self.manifest["aggregate"]["content_counts"])
        self.entry["mathematical_entries"] = self.manifest["aggregate"]["mathematical_entries"]
        self.entry["manifest"]["content_tree_sha256"] = self.manifest["aggregate"]["content_tree_sha256"]
        self.entry["manifest"]["members"] = len(self.manifest["members"])
        self.write_manifest()

    def rebind_member(self, path: str, data: bytes) -> None:
        write_bytes(self.package / Path(*path.split("/")), data)
        member_row = row(self, path)
        member_row["bytes"] = len(data)
        member_row["sha256"] = sha256(data)
        if path == self.scope_path:
            self.entry["writer"]["scope_receipt"].update(identity(path, data))
        elif path == self.review_path:
            for key, value in identity(path, data).items():
                self.entry["review_receipt"][key] = value
        elif path == self.test_path:
            for key, value in identity(path, data).items():
                self.entry["tests"][0][key] = value
        self.refresh_manifest()

    def run(self) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(self.validator_path),
                "--entry",
                str(self.entry_path),
                "--package",
                str(self.package),
                "--schema",
                str(self.schema_path),
                "--pin",
                str(self.pin_path),
                "--registry",
                str(self.registry_path),
            ],
            cwd=self.control_root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
        )


Mutation = Callable[[Fixture], None]


def row(fixture: Fixture, path: str) -> dict[str, Any]:
    return next(item for item in fixture.manifest["members"] if item["path"] == path)


def mutate_duplicate_key(fixture: Fixture) -> None:
    data = fixture.entry_path.read_bytes()
    fixture.write_entry(data.replace(b'  "state": "candidate_unregistered",\n', b'  "state": "candidate_unregistered",\n  "state": "candidate_unregistered",\n', 1))


def mutate_crlf(fixture: Fixture) -> None:
    fixture.write_entry(fixture.entry_path.read_bytes().replace(b"\n", b"\r\n"))


def mutate_bom(fixture: Fixture) -> None:
    fixture.write_entry(b"\xef\xbb\xbf" + fixture.entry_path.read_bytes())


def mutate_traversal(fixture: Fixture) -> None:
    fixture.manifest["members"][0]["path"] = f"{NAMESPACE}/../escape.tex"
    fixture.write_manifest()


def mutate_trailing_dot(fixture: Fixture) -> None:
    fixture.manifest["members"][0]["path"] = f"{NAMESPACE}/bad./math.tex"
    fixture.write_manifest()


def mutate_case_collision(fixture: Fixture) -> None:
    duplicate = deepcopy(row(fixture, fixture.math_path))
    duplicate["path"] = f"{NAMESPACE}/Math.tex"
    write_bytes(
        fixture.package / Path(*duplicate["path"].split("/")),
        (fixture.package / Path(*fixture.math_path.split("/"))).read_bytes(),
    )
    fixture.manifest["members"].append(duplicate)
    fixture.manifest["members"].sort(key=lambda item: item["path"].encode("utf-8"))
    fixture.write_manifest()


def mutate_pin_drift(fixture: Fixture) -> None:
    fixture.entry["upstream_pin"]["commit"] = "0" * 40
    fixture.write_entry()


def mutate_license_drift(fixture: Fixture) -> None:
    fixture.entry["upstream_pin"]["license_sha256"] = "0" * 64
    fixture.write_entry()


def mutate_missing_member(fixture: Fixture) -> None:
    (fixture.package / Path(*fixture.math_path.split("/"))).unlink()


def mutate_extra_member(fixture: Fixture) -> None:
    write_bytes(fixture.package / Path(*f"{NAMESPACE}/extra.txt".split("/")), b"extra\n")


def mutate_member_hash(fixture: Fixture) -> None:
    write_bytes(fixture.package / Path(*fixture.math_path.split("/")), b"changed\n")


def mutate_post_receipt_subject(fixture: Fixture) -> None:
    fixture.rebind_member(
        fixture.math_path,
        b"% changed after the bound PASS receipts\n\\def\\Fixture{2}\n",
    )


def mutate_tree(fixture: Fixture) -> None:
    fixture.manifest["aggregate"]["content_tree_sha256"] = "0" * 64
    fixture.entry["manifest"]["content_tree_sha256"] = "0" * 64
    fixture.write_manifest()


def mutate_count(fixture: Fixture) -> None:
    fixture.manifest["aggregate"]["files"] += 1
    fixture.write_manifest()


def mutate_duplicate_stable_id(fixture: Fixture) -> None:
    duplicate_path = f"{NAMESPACE}/math2.tex"
    duplicate_data = b"% second synthetic substantive fixture\n"
    write_bytes(fixture.package / Path(*duplicate_path.split("/")), duplicate_data)
    fixture.manifest["members"].append(
        member(
            duplicate_path,
            duplicate_data,
            "original_additions",
            stable_ids=["MC-STX-TEST-0001"],
            languages=["en"],
            upstream_locators=["stacks-pin:test"],
            provenance_receipts=[fixture.scope_path],
        )
    )
    fixture.manifest["members"].sort(key=lambda item: item["path"].encode("utf-8"))
    fixture.refresh_manifest()


def mutate_control_stable_id(fixture: Fixture) -> None:
    row(fixture, fixture.scope_path)["stable_ids"] = ["MC-STX-TEST-CONTROL"]
    fixture.refresh_manifest()


def mutate_stable_id_syntax(fixture: Fixture) -> None:
    row(fixture, fixture.math_path)["stable_ids"] = ["../../not-an-id"]
    fixture.refresh_manifest()


def mutate_review_internal_fail(fixture: Fixture) -> None:
    document = json.loads((fixture.package / Path(*fixture.review_path.split("/"))).read_text(encoding="utf-8"))
    document["status"] = "FAIL"
    document["errors"] = ["synthetic"]
    fixture.rebind_member(fixture.review_path, json_bytes(document))


def mutate_test_internal_fail(fixture: Fixture) -> None:
    document = json.loads((fixture.package / Path(*fixture.test_path.split("/"))).read_text(encoding="utf-8"))
    document["status"] = "FAIL"
    document["errors"] = ["synthetic"]
    fixture.rebind_member(fixture.test_path, json_bytes(document))


def mutate_scope_internal_fail(fixture: Fixture) -> None:
    document = json.loads((fixture.package / Path(*fixture.scope_path.split("/"))).read_text(encoding="utf-8"))
    document["status"] = "FAIL"
    document["errors"] = ["synthetic"]
    fixture.rebind_member(fixture.scope_path, json_bytes(document))


def mutate_review_scope(fixture: Fixture) -> None:
    document = json.loads((fixture.package / Path(*fixture.review_path.split("/"))).read_text(encoding="utf-8"))
    document["scope"] = "unrelated"
    fixture.rebind_member(fixture.review_path, json_bytes(document))


def mutate_review_subject(fixture: Fixture) -> None:
    document = json.loads((fixture.package / Path(*fixture.review_path.split("/"))).read_text(encoding="utf-8"))
    document["entry_id"] = "unrelated-entry"
    fixture.rebind_member(fixture.review_path, json_bytes(document))


def mutate_test_subject(fixture: Fixture) -> None:
    document = json.loads((fixture.package / Path(*fixture.test_path.split("/"))).read_text(encoding="utf-8"))
    document["overlay_tree"] = "3" * 40
    fixture.rebind_member(fixture.test_path, json_bytes(document))


def mutate_registry_pin(fixture: Fixture) -> None:
    registry = json.loads(fixture.registry_path.read_text(encoding="utf-8"))
    registry["upstream_pin"]["commit"] = "3" * 40
    write_bytes(fixture.registry_path, json_bytes(registry))


def mutate_registry_pattern(fixture: Fixture) -> None:
    registry = json.loads(fixture.registry_path.read_text(encoding="utf-8"))
    registry["namespace_policy"]["entry_pattern"] = "^nope$"
    write_bytes(fixture.registry_path, json_bytes(registry))


def mutate_registry_kinds(fixture: Fixture) -> None:
    registry = json.loads(fixture.registry_path.read_text(encoding="utf-8"))
    registry["entry_contract"]["allowed_content_kinds"] = []
    write_bytes(fixture.registry_path, json_bytes(registry))


def mutate_foreign_pin(fixture: Fixture) -> None:
    pin = json.loads(fixture.pin_path.read_text(encoding="utf-8"))
    pin["pin"]["commit"] = "3" * 40
    pin["pin"]["tree"] = "4" * 40
    pin["license"]["sha256"] = "5" * 64
    data = json_bytes(pin)
    write_bytes(fixture.pin_path, data)
    fixture.entry["upstream_pin"]["receipt"] = identity("manifests/stacks-pin.json", data)
    fixture.entry["upstream_pin"]["commit"] = pin["pin"]["commit"]
    fixture.entry["upstream_pin"]["tree"] = pin["pin"]["tree"]
    fixture.entry["upstream_pin"]["license_sha256"] = pin["license"]["sha256"]
    fixture.write_entry()


def mutate_foreign_schema(fixture: Fixture) -> None:
    schema = json.loads(fixture.schema_path.read_text(encoding="utf-8"))
    schema["title"] = "foreign candidate schema"
    write_bytes(fixture.schema_path, json_bytes(schema))


def mutate_absolute_pin_receipt(fixture: Fixture) -> None:
    fixture.entry["upstream_pin"]["receipt"]["path"] = fixture.pin_path.as_posix()
    fixture.write_entry()


def mutate_forbidden_path(fixture: Fixture) -> None:
    fixture.manifest["members"][0]["path"] = f"{NAMESPACE}/bad?.tex"
    fixture.write_manifest()


def mutate_long_path(fixture: Fixture) -> None:
    fixture.manifest["members"][0]["path"] = f"{NAMESPACE}/{'a' * 480}.tex"
    fixture.write_manifest()


def mutate_directory_case_collision(fixture: Fixture) -> None:
    for directory, name, stable_id in (("Dir", "a.tex", "MC-STX-TEST-A"), ("dir", "b.tex", "MC-STX-TEST-B")):
        path = f"{NAMESPACE}/{directory}/{name}"
        data = f"% {path}\n".encode("utf-8")
        write_bytes(fixture.package / Path(*path.split("/")), data)
        fixture.manifest["members"].append(
            member(
                path,
                data,
                "original_additions",
                stable_ids=[stable_id],
                languages=["en"],
                upstream_locators=["stacks-pin:test"],
                provenance_receipts=[fixture.scope_path],
            )
        )
    fixture.manifest["members"].sort(key=lambda item: item["path"].encode("utf-8"))
    fixture.refresh_manifest()


def mutate_aggregate_boolean(fixture: Fixture) -> None:
    fixture.manifest["aggregate"]["files"] = True
    fixture.write_manifest()


def mutate_content_count_boolean(fixture: Fixture) -> None:
    fixture.manifest["aggregate"]["content_counts"]["original_additions"] = True
    fixture.write_manifest()


def mutate_huge_integer(fixture: Fixture) -> None:
    data = fixture.entry_path.read_bytes()
    fixture.write_entry(data.replace(b'  "mathematical_entries": 1,', b'  "mathematical_entries": ' + b"9" * 5000 + b",", 1))


def mutate_control_only(fixture: Fixture) -> None:
    (fixture.package / Path(*fixture.math_path.split("/"))).unlink()
    fixture.manifest["members"] = [item for item in fixture.manifest["members"] if item["path"] != fixture.math_path]
    fixture.refresh_manifest()


def mutate_missing_provenance(fixture: Fixture) -> None:
    row(fixture, fixture.math_path)["provenance_receipts"] = []
    fixture.refresh_manifest()


def mutate_missing_source_locator(fixture: Fixture) -> None:
    math = row(fixture, fixture.math_path)
    math["kind"] = "corrections"
    math["upstream_locators"] = []
    fixture.refresh_manifest()


def mutate_review_kind(fixture: Fixture) -> None:
    row(fixture, fixture.review_path)["kind"] = "provenance"
    fixture.refresh_manifest()


def mutate_test_kind(fixture: Fixture) -> None:
    row(fixture, fixture.test_path)["kind"] = "provenance"
    fixture.refresh_manifest()


def mutate_scope_kind(fixture: Fixture) -> None:
    row(fixture, fixture.scope_path)["kind"] = "review_receipts"
    fixture.refresh_manifest()


def mutate_bad_commit(fixture: Fixture) -> None:
    fixture.entry["overlay"]["commit"] = "not-a-commit"
    fixture.write_entry()


def mutate_numeric_boolean(fixture: Fixture) -> None:
    fixture.entry["boundaries"]["registered"] = 0
    fixture.write_entry()


def mutate_null_required(fixture: Fixture) -> None:
    fixture.entry["manifest"]["members"] = None
    fixture.write_entry()


def mutate_certification(fixture: Fixture) -> None:
    fixture.entry["boundaries"]["mathematical_certification_claimed"] = True
    fixture.write_entry()


def mutate_endorsement(fixture: Fixture) -> None:
    fixture.entry["boundaries"]["upstream_endorsement_implied"] = True
    fixture.write_entry()


def mutate_registered(fixture: Fixture) -> None:
    fixture.entry["boundaries"]["registered"] = True
    fixture.write_entry()


def mutate_git_verified(fixture: Fixture) -> None:
    fixture.entry["overlay"]["git_identity_verified"] = True
    fixture.write_entry()


def mutate_overlay_root(fixture: Fixture) -> None:
    fixture.entry["overlay"]["root"] = "commons/stacks/other"
    fixture.write_entry()


def mutate_manifest_self_include(fixture: Fixture) -> None:
    fixture.manifest["self_excluding"] = False
    fixture.write_manifest()


def mutate_member_order(fixture: Fixture) -> None:
    fixture.manifest["members"] = list(reversed(fixture.manifest["members"]))
    fixture.write_manifest()


def mutate_namespace_collision(fixture: Fixture) -> None:
    registry = json.loads(fixture.registry_path.read_text(encoding="utf-8"))
    registry["namespace_claims"] = [f"{NAMESPACE}/child"]
    write_bytes(fixture.registry_path, json_bytes(registry))


INVALID_CASES: tuple[tuple[str, Mutation, str], ...] = (
    ("duplicate_key", mutate_duplicate_key, "duplicate JSON key"),
    ("crlf", mutate_crlf, "LF-only"),
    ("bom", mutate_bom, "UTF-8 BOM"),
    ("traversal", mutate_traversal, "unsafe segment"),
    ("trailing_dot", mutate_trailing_dot, "trailing dot or space"),
    ("forbidden_path", mutate_forbidden_path, "portable-path character"),
    ("long_path", mutate_long_path, "member manifest schema validation failed"),
    ("case_collision", mutate_case_collision, "case-fold path collision"),
    ("directory_case_collision", mutate_directory_case_collision, "case-fold path-prefix collision"),
    ("namespace_collision", mutate_namespace_collision, "overlaps registered namespace"),
    ("pin_drift", mutate_pin_drift, "upstream commit differs"),
    ("license_drift", mutate_license_drift, "upstream license identity differs"),
    ("registry_pin_drift", mutate_registry_pin, "registry upstream commit differs"),
    ("registry_pattern_drift", mutate_registry_pattern, "entry pattern differs"),
    ("registry_kinds_drift", mutate_registry_kinds, "allowed content kinds differ"),
    ("foreign_pin", mutate_foreign_pin, "registry upstream pin receipt"),
    ("foreign_schema", mutate_foreign_schema, "registry candidate schema"),
    ("absolute_pin_receipt", mutate_absolute_pin_receipt, "upstream pin receipt path differs"),
    ("missing_member", mutate_missing_member, "missing member"),
    ("extra_member", mutate_extra_member, "missing, extra, or differently named files"),
    ("member_hash", mutate_member_hash, "member byte count differs"),
    ("post_receipt_subject_change", mutate_post_receipt_subject, "review receipt subject tree differs"),
    ("content_tree", mutate_tree, "content tree differs"),
    ("aggregate_count", mutate_count, "file aggregate differs"),
    ("aggregate_boolean", mutate_aggregate_boolean, "member manifest schema validation failed"),
    ("content_count_boolean", mutate_content_count_boolean, "candidate schema validation failed"),
    ("duplicate_stable_id", mutate_duplicate_stable_id, "stable Commons IDs are not globally unique"),
    ("control_stable_id", mutate_control_stable_id, "control member carries a mathematical stable ID"),
    ("stable_id_syntax", mutate_stable_id_syntax, "member manifest schema validation failed"),
    ("control_only", mutate_control_only, "candidate schema validation failed"),
    ("missing_provenance", mutate_missing_provenance, "mathematical member lacks a provenance receipt"),
    ("missing_source_locator", mutate_missing_source_locator, "corrections member lacks an upstream locator"),
    ("review_kind", mutate_review_kind, "review receipt is not classified"),
    ("test_kind", mutate_test_kind, "test receipt is not classified"),
    ("scope_kind", mutate_scope_kind, "writer scope receipt is not classified"),
    ("review_internal_fail", mutate_review_internal_fail, "review receipt schema validation failed"),
    ("test_internal_fail", mutate_test_internal_fail, "test receipt"),
    ("scope_internal_fail", mutate_scope_internal_fail, "writer scope receipt schema validation failed"),
    ("review_scope", mutate_review_scope, "review receipt schema validation failed"),
    ("review_subject", mutate_review_subject, "review receipt entry ID differs"),
    ("test_subject", mutate_test_subject, "test receipt overlay tree differs"),
    ("malformed_commit", mutate_bad_commit, "candidate schema validation failed"),
    ("numeric_boolean", mutate_numeric_boolean, "candidate schema validation failed"),
    ("null_required", mutate_null_required, "candidate schema validation failed"),
    ("huge_integer", mutate_huge_integer, "integer token is too long"),
    ("certification_claim", mutate_certification, "candidate schema validation failed"),
    ("endorsement_claim", mutate_endorsement, "candidate schema validation failed"),
    ("registered_claim", mutate_registered, "candidate schema validation failed"),
    ("git_verified_claim", mutate_git_verified, "candidate schema validation failed"),
    ("overlay_root", mutate_overlay_root, "overlay root differs"),
    ("manifest_self_include", mutate_manifest_self_include, "member manifest must be self-excluding"),
    ("member_order", mutate_member_order, "member rows are not in ordinal"),
)


def parse_report(process: subprocess.CompletedProcess[str], case: str) -> dict[str, Any]:
    if process.stderr:
        raise RuntimeError(f"{case}: validator wrote stderr: {process.stderr.strip()}")
    try:
        report = json.loads(process.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError(f"{case}: validator did not emit JSON") from error
    return report


def run_case(base: Path, repo_root: Path, name: str, mutation: Mutation | None, expected_error: str | None = None) -> tuple[bool, str]:
    case_root = base / name
    case_root.mkdir(parents=True)
    fixture = Fixture(case_root, repo_root)
    if mutation is not None:
        mutation(fixture)
    process = fixture.run()
    report = parse_report(process, name)
    report_text = json.dumps(report, ensure_ascii=False)
    local_markers = (str(case_root), case_root.as_posix(), str(fixture.control_root), fixture.control_root.as_posix())
    local_path_clean = all(marker not in report_text for marker in local_markers)
    if mutation is None:
        passed = process.returncode == 0 and report.get("status") == "PASS" and report.get("errors") == [] and report.get("outcome") == VALID_OUTCOME and local_path_clean
    else:
        errors = report.get("errors", [])
        passed = (
            process.returncode != 0
            and report.get("status") == "FAIL"
            and bool(errors)
            and report.get("outcome") == "REJECTED_CANDIDATE"
            and expected_error is not None
            and any(expected_error in str(error) for error in errors)
            and local_path_clean
        )
    return passed, "" if passed else f"return={process.returncode}; report={json.dumps(report, ensure_ascii=False)}"


def run_symlink_case(base: Path, repo_root: Path) -> tuple[str, str]:
    case_root = base / "symlink"
    case_root.mkdir(parents=True)
    fixture = Fixture(case_root, repo_root)
    target = fixture.package / Path(*fixture.math_path.split("/"))
    external = case_root / "external.tex"
    external.write_bytes(target.read_bytes())
    target.unlink()
    try:
        os.symlink(external, target)
    except OSError as error:
        return "SKIP", f"platform denied symlink creation: {error.__class__.__name__}"
    process = fixture.run()
    report = parse_report(process, "symlink")
    passed = process.returncode != 0 and report.get("status") == "FAIL" and bool(report.get("errors"))
    return ("PASS", "") if passed else ("FAIL", f"return={process.returncode}; report={report}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."), help="repository root")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = args.root.resolve(strict=True)
    required = (
        repo_root / "manifests" / "stacks-entry.schema.json",
        repo_root / "manifests" / "stacks-pin.json",
        repo_root / "manifests" / "stacks-overlay.json",
        repo_root / "scripts" / "check-stacks-entry.py",
    )
    missing = [path.as_posix() for path in required if not path.is_file()]
    if missing:
        sys.stdout.write(json.dumps({"schema": "stacks-overlay-entry-regression/v1", "status": "FAIL", "errors": [f"missing: {path}" for path in missing]}, indent=2) + "\n")
        return 12

    failures: list[str] = []
    valid_passed = 0
    invalid_passed = 0
    conditional_passed = 0
    conditional_skipped = 0
    with tempfile.TemporaryDirectory(prefix="stacks-entry-") as temporary:
        base = Path(temporary)
        passed, detail = run_case(base, repo_root, "valid", None)
        if passed:
            valid_passed += 1
        else:
            failures.append(f"valid: {detail}")
        for name, mutation, expected_error in INVALID_CASES:
            passed, detail = run_case(base, repo_root, name, mutation, expected_error)
            if passed:
                invalid_passed += 1
            else:
                failures.append(f"{name}: {detail}")
        state, detail = run_symlink_case(base, repo_root)
        if state == "PASS":
            conditional_passed += 1
        elif state == "SKIP":
            conditional_skipped += 1
        else:
            failures.append(f"symlink: {detail}")

    status = "PASS" if not failures else "FAIL"
    report = {
        "schema": "stacks-overlay-entry-regression/v1",
        "status": status,
        "errors": failures,
        "version": VERSION,
        "valid_cases": {"expected": 1, "passed": valid_passed},
        "invalid_cases": {"expected": len(INVALID_CASES), "passed": invalid_passed},
        "platform_conditional": {
            "defined": 1,
            "passed": conditional_passed,
            "skipped": conditional_skipped,
            "rule": "symlink rejection executes when the platform permits fixture symlink creation",
        },
        "aggregate": {
            "defined_cases": 1 + len(INVALID_CASES) + 1,
            "required_cases": 1 + len(INVALID_CASES),
            "required_passed": valid_passed + invalid_passed,
        },
        "boundaries": {
            "fixtures_temporary": True,
            "registered_entries": 0,
            "mathematical_payloads": 0,
            "network_queried": False,
            "git_invoked": False,
        },
    }
    sys.stdout.write(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    return 0 if status == "PASS" else 12


if __name__ == "__main__":
    raise SystemExit(main())
