"""Finalize the D033 source/nonregression and provenance trees before packaging.

This is a bounded, offline reseal.  It does not run TeX, create archives, use
Git, access a network, publish anything, or inspect the contents of inherited
archive carriers.  The later packager remains the sole archive producer.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

import d033_contract as c


SOURCE_MANIFEST = c.SOURCE_MANIFEST_NAME
PROVENANCE_MANIFEST = "PROVENANCE_MANIFEST.tsv"
PRIVACY_RECEIPT = "PUBLIC_PROVENANCE_PRIVACY.json"
NONREGRESSION_RECEIPT = "SOURCE_NONREGRESSION.json"
INHERITED_MEMBER = "inherited/DELIGNE_PROVENANCE_AUDIT_D019_GAPFILL.zip"
D033_GATE_MEMBER = "D033/D033_PAPER_COMPLETE_CORPUS_GATE_V1.zip"
RECEIPT_DIRECTORY = "release_receipts/D033_FORWARD_INTEGRATION"
INTEGRATION_AUDITS = "integration_audits"
EXPECTED_REPAIRED_SOURCE_ROWS = 2913
EXPECTED_PREDECESSOR_SOURCE_ROWS = 2882
TOP_LEVEL_CURRENT = (
    "Deligne_EN.pdf",
    "Deligne_FR.pdf",
    "Deligne_EN.tex",
    "Deligne_FR.tex",
    "README.md",
)
EXPECTED_CHANGED_PREDECESSOR_PATHS = frozenset(TOP_LEVEL_CURRENT)
EXPECTED_EXISTING_TRACKED_RECEIPTS = frozenset(
    {"D019_PREDECESSOR_BUILD_RELEASE_RECEIPT.json"}
)

# These are the four decisive, successful receipts.  Failed attempts and
# historical worker noise deliberately remain outside both public trees.
PRODUCTION_RECEIPTS = (
    ("COLD_REPRODUCIBILITY_RECEIPT.json", "COLD_REPRODUCIBILITY_RECEIPT.json"),
    ("CUMULATIVE_PAGE_QA.json", "CUMULATIVE_PAGE_QA.json"),
    (
        "AGENT_VISUAL_REPORT_RECONCILIATION_20260904T210121Z.json",
        "VISUAL_INSPECTION.json",
    ),
    (
        "D033_SOURCE_MANIFEST_REPAIR_20260904T213406Z.json",
        "D033_SOURCE_MANIFEST_REPAIR.json",
    ),
)

# Minimal code closure needed to repeat staging, guarded build/QA, resealing,
# and the separate later packaging transaction.  Unit tests are validation
# inputs, not production payload members, matching the D019 layout precedent.
PRODUCTION_SCRIPTS = (
    "build_d033_integration.py",
    "build_tree_runner.py",
    "d033_contract.py",
    "finalize_manifest_nonregression.py",
    "package_d033_release.py",
    "tex_worker.py",
)


class FinalizationFailure(RuntimeError):
    """A bounded finalization contract failed."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise FinalizationFailure(message)


def identity_bytes(data: bytes) -> dict[str, object]:
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest().upper()}


def identity(path: Path) -> dict[str, object]:
    try:
        return c.identity(path)
    except (OSError, c.Failure) as exc:
        raise FinalizationFailure("file identity verification failed") from exc


def same_identity(left: dict[str, object], right: dict[str, object]) -> bool:
    return int(left["bytes"]) == int(right["bytes"]) and str(left["sha256"]).upper() == str(
        right["sha256"]
    ).upper()


def check(path: Path, expected: dict[str, object]) -> dict[str, object]:
    actual = identity(path)
    require(same_identity(actual, expected), "file identity mismatch")
    return actual


def read_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise FinalizationFailure("required JSON receipt is unreadable") from exc


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )


def _within(path: Path, root: Path) -> bool:
    try:
        path.absolute().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def _write_bytes(path: Path, data: bytes, allowed_roots: tuple[Path, ...], *, replace: bool = False) -> dict[str, object]:
    require(any(_within(path, root) for root in allowed_roots), "write outside finalization roots")
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        c.reject_reparse(path.parent)
        if path.exists() and not replace:
            require(path.read_bytes() == data, "existing public finalization member differs")
            return identity(path)
        temporary = path.with_name(f".{path.name}.d033-finalize-{os.getpid()}.tmp")
        require(not temporary.exists(), "stale finalization temporary file")
        try:
            temporary.write_bytes(data)
            require(same_identity(identity(temporary), identity_bytes(data)), "temporary write replay failed")
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)
        return check(path, identity_bytes(data))
    except (OSError, c.Failure) as exc:
        raise FinalizationFailure("confined finalization write failed") from exc


def manifest_bytes(rows: list[dict[str, object]]) -> bytes:
    lines = ["path\tbytes\tsha256\n"]
    names = [str(row["path"]) for row in rows]
    require(names == sorted(names), "manifest rows are not sorted")
    require(len(names) == len(set(names)) == len({name.casefold() for name in names}), "manifest path collision")
    for row in rows:
        name = str(c.safe_relative(str(row["path"])))
        require(name == row["path"], "non-canonical manifest path")
        require(re.fullmatch(r"[0-9A-F]{64}", str(row["sha256"])), "malformed manifest hash")
        lines.append(f'{name}\t{int(row["bytes"])}\t{row["sha256"]}\n')
    return "".join(lines).encode("utf-8")


def tree_rows(root: Path, *, exclude: frozenset[str] = frozenset()) -> list[dict[str, object]]:
    rows = []
    for name in c.inventory_tree(root):
        if name in exclude:
            continue
        rows.append({"path": name, **identity(c.confined(root, name))})
    return rows


def verify_manifest(
    root: Path,
    manifest_name: str,
    *,
    require_canonical_order: bool = True,
) -> list[dict[str, object]]:
    manifest = c.confined(root, manifest_name)
    raw = manifest.read_bytes()
    require(b"\r\n" not in raw and raw.startswith(b"path\tbytes\tsha256\n"), "manifest serialization is not canonical LF TSV")
    try:
        reader = csv.DictReader(io.StringIO(raw.decode("utf-8"), newline=""), delimiter="\t")
        require(reader.fieldnames == ["path", "bytes", "sha256"], "manifest columns differ")
        actual = [
            {"path": row["path"], "bytes": int(row["bytes"]), "sha256": row["sha256"]}
            for row in reader
        ]
    except (UnicodeError, ValueError, TypeError) as exc:
        raise FinalizationFailure("manifest parse failed") from exc
    expected = tree_rows(root, exclude=frozenset({manifest_name}))
    if require_canonical_order:
        require(actual == expected, "manifest replay differs from live tree")
    else:
        # The inherited D019 manifest uses its historical producer's
        # case-insensitive ordering.  Preserve and bind those bytes, while
        # replaying coverage and every identity without rewriting it.
        actual_by_name = {row["path"]: row for row in actual}
        expected_by_name = {row["path"]: row for row in expected}
        require(
            len(actual_by_name) == len(actual) == len({row["path"].casefold() for row in actual}),
            "inherited manifest path collision",
        )
        require(actual_by_name == expected_by_name, "inherited manifest replay differs from live tree")
    return actual


def _privacy_token_bytes(token: str) -> bytes:
    require(isinstance(token, str) and token and token.isascii() and token.isprintable(), "privacy token unavailable")
    require(not any(character in token for character in "/\\\r\n\t"), "privacy token invalid")
    return token.encode("ascii")


def _replace_literal(data: bytes, token: str) -> tuple[bytes, int]:
    needle = _privacy_token_bytes(token)
    return re.subn(re.escape(needle), b"LOCAL_ACCOUNT", data, flags=re.IGNORECASE)


def _replace_name(name: str, token: str) -> tuple[str, int]:
    _privacy_token_bytes(token)
    return re.subn(re.escape(token), "LOCAL_ACCOUNT", name, flags=re.IGNORECASE)


def _forbidden_path_component(name: str) -> bool:
    exact = {
        ".env",
        "credential",
        "credentials",
        ".credentials",
        "secret",
        "secrets",
        "token",
        "tokens",
        "new zenodo token.md",
    }
    for part in PurePosixPath(name).parts:
        folded = part.casefold()
        if folded in exact or "credential" in folded or folded.endswith((".pem", ".key", ".p12", ".pfx")):
            return True
    return False


def _credential_patterns() -> tuple[re.Pattern[bytes], ...]:
    # Split sensitive literals keep this public checker from diagnosing its own
    # source code as a credential merely because it implements these checks.
    private_key = b"-----BEGIN " + b"(?:[A-Z0-9 ]{0,24})PRIVATE KEY-----"
    github_short = b"gh" + b"[pousr]_[A-Za-z0-9]{20,}"
    github_fine = b"github_" + b"pat_[A-Za-z0-9_]{20,}"
    labels = b"(?:access_" + b"token|api_" + b"key|client_" + b"secret|password)"
    assigned = labels + rb"\s*[\"']?\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{16,}"
    bearer = b"authori" + rb"zation\s*:\s*bearer\s+[A-Za-z0-9_./+=-]{16,}"
    return tuple(
        re.compile(pattern, re.IGNORECASE)
        for pattern in (private_key, github_short, github_fine, assigned, bearer)
    )


def assert_no_credentials_bytes(data: bytes, public_name: str) -> None:
    require(not _forbidden_path_component(public_name), "credential-bearing public path is forbidden")
    require(not any(pattern.search(data) for pattern in _credential_patterns()), "credential signature detected")


def _stream_contains(path: Path, needle: bytes) -> bool:
    lowered = needle.lower()
    overlap = max(0, len(lowered) - 1)
    tail = b""
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            haystack = (tail + block).lower()
            if lowered in haystack:
                return True
            tail = haystack[-overlap:] if overlap else b""
    return False


def direct_check_file(path: Path, public_name: str, token: str) -> dict[str, object]:
    needle = _privacy_token_bytes(token)
    require(not _forbidden_path_component(public_name), "credential-bearing public path is forbidden")
    require(needle.lower() not in public_name.encode("utf-8").lower(), "local-account first name detected in public filename")
    require(not _stream_contains(path, needle), "local-account first name detected in public bytes")
    # Credential signatures are short enough for a bounded overlap replay.
    tail = b""
    patterns = _credential_patterns()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            sample = tail + block
            require(not any(pattern.search(sample) for pattern in patterns), "credential signature detected")
            tail = sample[-512:]
    return identity(path)


@dataclass(frozen=True)
class FinalizationLayout:
    task: Path
    source: Path
    predecessor_source: Path
    audit: Path
    provenance: Path
    scripts: Path
    receipt_sources: tuple[tuple[str, Path], ...]
    script_sources: tuple[tuple[str, Path], ...]
    source_preparation_receipt: Path
    gate_expected: dict[str, object]
    inherited_external: Path
    inherited_expected: dict[str, object]
    predecessor_manifest_expected: dict[str, object]
    baseline_rows: int = EXPECTED_REPAIRED_SOURCE_ROWS
    predecessor_rows: int = EXPECTED_PREDECESSOR_SOURCE_ROWS
    expected_existing_tracked_receipts: frozenset[str] = EXPECTED_EXISTING_TRACKED_RECEIPTS

    @property
    def tracked_receipts(self) -> Path:
        return self.source / RECEIPT_DIRECTORY

    @property
    def integration_audits(self) -> Path:
        return self.provenance / INTEGRATION_AUDITS


@dataclass(frozen=True)
class CopyPlan:
    logical_name: str
    source: Path
    destinations: tuple[Path, ...]
    data: bytes
    original_identity: dict[str, object]
    public_identity: dict[str, object]
    raw_byte_replacements: int
    filename_replacements: int


def production_layout() -> FinalizationLayout:
    cfg = c.config()
    task = c.TASK.resolve()
    predecessor_build = (task.parent / "successor_D019_gapfill_from_D017" / "build/cumulative").resolve()
    require(Path(cfg["predecessor"]["root"]).resolve() == predecessor_build, "predecessor is not the exact D019 sibling")
    inherited = next(
        row
        for row in cfg["predecessor"]["release_files"]
        if Path(row["path"]).name == Path(INHERITED_MEMBER).name
    )
    audit = task / "build/cumulative/audit"
    receipt_sources = tuple(
        (public_name, audit / original_name)
        for original_name, public_name in PRODUCTION_RECEIPTS
    )
    script_sources = tuple((name, task / "scripts" / name) for name in PRODUCTION_SCRIPTS)
    return FinalizationLayout(
        task=task,
        source=task / "build/cumulative/source_tree",
        predecessor_source=predecessor_build / "source_tree",
        audit=audit,
        provenance=task / "build/cumulative/provenance_tree",
        scripts=task / "scripts",
        receipt_sources=receipt_sources,
        script_sources=script_sources,
        source_preparation_receipt=audit / "SOURCE_PREPARATION_RECEIPT.json",
        gate_expected={key: cfg["d033"]["flat_packet"][key] for key in ("bytes", "sha256")},
        inherited_external=predecessor_build / "release" / Path(INHERITED_MEMBER).name,
        inherited_expected={key: inherited[key] for key in ("bytes", "sha256")},
        predecessor_manifest_expected={key: cfg["predecessor"]["source_manifest"][key] for key in ("bytes", "sha256")},
    )


def _validate_layout(layout: FinalizationLayout) -> None:
    task = layout.task.resolve()
    require(layout.source.resolve().parent.parent == task / "build", "source root outside D033 task")
    require(layout.audit.resolve().parent == layout.source.resolve().parent, "audit root differs from source build")
    require(layout.provenance.resolve().parent == layout.source.resolve().parent, "provenance root differs from source build")
    require(layout.scripts.resolve() == task / "scripts", "script root outside D033 task")
    require(layout.predecessor_source.resolve().parent.name == "cumulative", "predecessor source layout mismatch")
    for _, path in (*layout.receipt_sources, *layout.script_sources):
        require(_within(path, task), "public-copy input outside D033 task")
    require(_within(layout.inherited_external, layout.predecessor_source.parents[2]), "inherited carrier outside D019 sibling")


def _verify_repaired_baseline(layout: FinalizationLayout) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows = verify_manifest(layout.source, SOURCE_MANIFEST)
    require(len(rows) == layout.baseline_rows, "repaired source-manifest row count differs")
    manifest_id = identity(layout.source / SOURCE_MANIFEST)
    repair_path = dict(layout.receipt_sources)["D033_SOURCE_MANIFEST_REPAIR.json"]
    repair = read_json(repair_path)
    require(isinstance(repair, dict) and repair.get("status") == "PASS", "source-manifest repair receipt is not PASS")
    require(int(repair["new_manifest"]["rows"]) == layout.baseline_rows, "repair receipt row count differs")
    require(same_identity(manifest_id, repair["new_manifest"]), "repair receipt does not bind current manifest")
    by_path = {str(row["path"]): row for row in rows}
    require(set(TOP_LEVEL_CURRENT) <= set(by_path), "current README/PDF/TeX files are missing")
    for name in TOP_LEVEL_CURRENT:
        check(layout.source / name, by_path[name])

    cold = read_json(dict(layout.receipt_sources)["COLD_REPRODUCIBILITY_RECEIPT.json"])
    qa = read_json(dict(layout.receipt_sources)["CUMULATIVE_PAGE_QA.json"])
    prep = read_json(layout.source_preparation_receipt)
    visual = read_json(dict(layout.receipt_sources)["VISUAL_INSPECTION.json"])
    require(isinstance(cold, dict) and cold.get("status") == "PASS", "build receipt is not PASS")
    require(isinstance(qa, dict) and qa.get("status") == "PASS", "QA receipt is not PASS")
    require(isinstance(prep, dict) and prep.get("status") == "PASS", "source-preparation receipt is not PASS")
    require(
        isinstance(visual, dict)
        and visual.get("decision") == "PASS"
        and visual.get("final_visual_gate", {}).get("status") == "PASS",
        "visual receipt is not final PASS",
    )
    for lang in ("EN", "FR"):
        pdf = by_path[f"Deligne_{lang}.pdf"]
        tex = by_path[f"Deligne_{lang}.tex"]
        require(same_identity(pdf, cold["languages"][lang]["pdf"]), "PDF/build receipt identity differs")
        require(same_identity(pdf, qa["languages"][lang]["pdf"]), "PDF/QA receipt identity differs")
        require(same_identity(tex, prep["preflight"]["languages"][lang]["draft_master"]), "TeX/preparation identity differs")
    require(same_identity(by_path["README.md"], repair["readme_preserved"]), "README/repair receipt identity differs")
    return rows, manifest_id


def _verify_predecessor(layout: FinalizationLayout) -> tuple[list[dict[str, object]], dict[str, object]]:
    manifest = layout.predecessor_source / SOURCE_MANIFEST
    check(manifest, layout.predecessor_manifest_expected)
    rows = verify_manifest(
        layout.predecessor_source,
        SOURCE_MANIFEST,
        require_canonical_order=False,
    )
    require(len(rows) == layout.predecessor_rows, "predecessor source-manifest row count differs")
    return rows, identity(manifest)


def _plan_copy(logical_name: str, source: Path, destinations: tuple[Path, ...], token: str) -> CopyPlan:
    raw = source.read_bytes()
    original = identity_bytes(raw)
    assert_no_credentials_bytes(raw, logical_name)
    revised, byte_count = _replace_literal(raw, token)
    revised_name, name_count = _replace_name(logical_name, token)
    require(revised_name == logical_name, "configured public destination itself contains the local-account first name")
    assert_no_credentials_bytes(revised, revised_name)
    return CopyPlan(
        logical_name=logical_name,
        source=source,
        destinations=destinations,
        data=revised,
        original_identity=original,
        public_identity=identity_bytes(revised),
        raw_byte_replacements=byte_count,
        filename_replacements=name_count,
    )


def _write_plan(plan: CopyPlan, layout: FinalizationLayout) -> dict[str, object]:
    for destination in plan.destinations:
        _write_bytes(destination, plan.data, (layout.source, layout.provenance))
    require(same_identity(identity(plan.source), plan.original_identity), "original receipt/script changed during derivative copy")
    return {
        "logical_name": plan.logical_name,
        "original": plan.original_identity,
        "public": plan.public_identity,
        "derivative_created": bool(plan.raw_byte_replacements or plan.filename_replacements),
        "raw_byte_replacements": plan.raw_byte_replacements,
        "filename_replacements": plan.filename_replacements,
        "destinations": [
            destination.relative_to(layout.source if _within(destination, layout.source) else layout.provenance).as_posix()
            for destination in plan.destinations
        ],
        "original_preserved_outside_public_destination": True,
        "transform": "EXACT_CASE_INSENSITIVE_LOCAL_ACCOUNT_FIRST_NAME_ONLY_v1",
    }


def _build_nonregression(
    layout: FinalizationLayout,
    predecessor_rows: list[dict[str, object]],
    predecessor_manifest_id: dict[str, object],
    repaired_manifest_id: dict[str, object],
) -> tuple[dict[str, object], int]:
    self_paths = frozenset(
        {
            f"{RECEIPT_DIRECTORY}/{NONREGRESSION_RECEIPT}",
            f"{RECEIPT_DIRECTORY}/{PRIVACY_RECEIPT}",
        }
    )
    current_rows = tree_rows(layout.source, exclude=frozenset({SOURCE_MANIFEST}) | self_paths)
    predecessor = {str(row["path"]): row for row in predecessor_rows}
    current = {str(row["path"]): row for row in current_rows}
    removed = sorted(set(predecessor) - set(current))
    changed = sorted(
        name for name in set(predecessor) & set(current) if not same_identity(predecessor[name], current[name])
    )
    identical = sorted(
        name for name in set(predecessor) & set(current) if same_identity(predecessor[name], current[name])
    )
    added = sorted(set(current) - set(predecessor))
    require(not removed, "predecessor source path was removed")
    require(set(changed) == EXPECTED_CHANGED_PREDECESSOR_PATHS, "unexpected predecessor identity delta")
    allowed_prefixes = ("works/D033_PUBLIC_SAFE/", RECEIPT_DIRECTORY + "/")
    require(all(name.startswith(allowed_prefixes) for name in added), "unexpected successor-added source path")
    expected_final_members = len(current_rows) + len(self_paths)
    receipt = {
        "schema": "d033-source-nonregression-v1",
        "status": "PASS",
        "scope": "Final non-manifest D033 source tree after tracked closure; receipt/self and privacy/self are bound by the subsequently rewritten canonical source manifest to avoid a self-hash cycle.",
        "predecessor": {
            "work": "D019",
            "source_manifest": predecessor_manifest_id,
            "members_replayed": len(predecessor_rows),
        },
        "repaired_source_manifest_baseline": {
            **repaired_manifest_id,
            "members_replayed_before_tracked_closure": layout.baseline_rows,
        },
        "final_source_manifest_contract": {
            "members_expected": expected_final_members,
            "sorted_lf_tsv": True,
            "excludes_itself": True,
            "written_and_replayed_after_receipt_copy": True,
        },
        "identity_comparison_exclusions": sorted(self_paths | {SOURCE_MANIFEST}),
        "all_predecessor_paths_retained": True,
        "byte_identical_predecessor_files": len(identical),
        "allowed_changed_files": [
            {"path": name, "predecessor": predecessor[name], "current": current[name]}
            for name in changed
        ],
        "allowed_added_files": [{"path": name, **current[name]} for name in added],
        "removed_files": [],
        "source_master_writes_by_finalizer": False,
        "packaging_performed": False,
    }
    return receipt, expected_final_members


def _scan_tree_direct(
    root: Path,
    token: str,
    *,
    exclude: frozenset[str] = frozenset(),
) -> list[dict[str, object]]:
    checked = []
    for name in c.inventory_tree(root):
        if name in exclude:
            continue
        checked.append({"path": name, **direct_check_file(c.confined(root, name), name, token)})
    return checked


def _privacy_receipt(
    copy_records: list[dict[str, object]],
    source_checks: list[dict[str, object]],
    provenance_checks: list[dict[str, object]],
) -> dict[str, object]:
    derivatives = [record for record in copy_records if record["derivative_created"]]
    return {
        "schema": "d033-public-provenance-privacy-v1",
        "status": "PASS",
        "literal_target": "configured local-account first name; value intentionally omitted",
        "policy": {
            "candidate_names": "DIRECT_CASE_INSENSITIVE_CHECK",
            "candidate_regular_file_bytes": "DIRECT_CASE_INSENSITIVE_RAW_BYTE_CHECK",
            "recursive_archive_privacy_scan": False,
            "d033_gate_archive_privacy_scope": "CARRIER_NAME_AND_RAW_BYTES_ONLY_NO_MEMBER_TRAVERSAL",
            "inherited_d019_carrier": "OPAQUE_ALREADY_PUBLIC_BYTE_IDENTICAL_NO_PRIVACY_RESCAN_OR_UNPACK",
            "credential_validation": "DIRECT_PATH_AND_RAW_BYTE_SIGNATURE_CHECK",
        },
        "source_tracked_closure_files_checked": len(source_checks),
        "provenance_files_checked_excluding_opaque_inherited_and_receipt_self": len(provenance_checks),
        "findings": [],
        "credential_findings": [],
        "derivative_count": len(derivatives),
        "derivatives": derivatives,
        "originals_preserved_outside_public_tree": True,
        "packaging_performed": False,
    }


def _write_source_manifest(layout: FinalizationLayout) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows = tree_rows(layout.source, exclude=frozenset({SOURCE_MANIFEST}))
    data = manifest_bytes(rows)
    manifest_id = _write_bytes(layout.source / SOURCE_MANIFEST, data, (layout.source,), replace=True)
    replayed = verify_manifest(layout.source, SOURCE_MANIFEST)
    require(replayed == rows, "final source manifest replay changed")
    return replayed, manifest_id


def _write_provenance_manifest(layout: FinalizationLayout) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows = tree_rows(layout.provenance, exclude=frozenset({PROVENANCE_MANIFEST}))
    data = manifest_bytes(rows)
    manifest_id = _write_bytes(layout.provenance / PROVENANCE_MANIFEST, data, (layout.provenance,), replace=True)
    replayed = verify_manifest(layout.provenance, PROVENANCE_MANIFEST)
    require(replayed == rows, "provenance manifest replay changed")
    return replayed, manifest_id


def finalize(layout: FinalizationLayout, token: str) -> dict[str, object]:
    _privacy_token_bytes(token)
    _validate_layout(layout)
    baseline_rows, repaired_manifest_id = _verify_repaired_baseline(layout)
    predecessor_rows, predecessor_manifest_id = _verify_predecessor(layout)

    gate = layout.provenance / D033_GATE_MEMBER
    inherited_copy = layout.provenance / INHERITED_MEMBER
    gate_id = check(gate, layout.gate_expected)
    inherited_external_id = check(layout.inherited_external, layout.inherited_expected)
    inherited_copy_id = check(inherited_copy, layout.inherited_expected)
    require(same_identity(inherited_external_id, inherited_copy_id), "inherited D019 carrier is not byte-identical")

    require(not (layout.provenance / PROVENANCE_MANIFEST).exists(), "provenance manifest already exists")
    require(not (layout.provenance / PRIVACY_RECEIPT).exists(), "provenance privacy receipt already exists")
    require(not layout.integration_audits.exists(), "integration-audit destination already exists")
    existing = {
        path.relative_to(layout.tracked_receipts).as_posix()
        for path in layout.tracked_receipts.rglob("*")
        if path.is_file()
    }
    require(existing == layout.expected_existing_tracked_receipts, "tracked receipt directory has unexpected pre-finalization members")

    # Validate and transform every candidate before the first write.
    plans = []
    for logical_name, source in layout.receipt_sources:
        destinations = (
            layout.tracked_receipts / logical_name,
            layout.integration_audits / logical_name,
        )
        plans.append(_plan_copy(logical_name, source, destinations, token))
    for logical_name, source in layout.script_sources:
        plans.append(
            _plan_copy(
                logical_name,
                source,
                (layout.tracked_receipts / "build_scripts" / logical_name,),
                token,
            )
        )

    # Existing public D033 provenance must already be safe; the inherited D019
    # carrier is deliberately not opened or byte-scanned for privacy.
    _scan_tree_direct(layout.provenance, token, exclude=frozenset({INHERITED_MEMBER}))
    copy_records = [_write_plan(plan, layout) for plan in plans]

    nonregression, expected_final_members = _build_nonregression(
        layout,
        predecessor_rows,
        predecessor_manifest_id,
        repaired_manifest_id,
    )
    nonregression_data = json_bytes(nonregression)
    assert_no_credentials_bytes(nonregression_data, NONREGRESSION_RECEIPT)
    nonregression_id = identity_bytes(nonregression_data)
    for destination in (
        layout.tracked_receipts / NONREGRESSION_RECEIPT,
        layout.integration_audits / NONREGRESSION_RECEIPT,
    ):
        _write_bytes(destination, nonregression_data, (layout.source, layout.provenance))

    source_checks = _scan_tree_direct(layout.tracked_receipts, token)
    provenance_checks = _scan_tree_direct(
        layout.provenance,
        token,
        exclude=frozenset({INHERITED_MEMBER, PRIVACY_RECEIPT, PROVENANCE_MANIFEST}),
    )
    privacy = _privacy_receipt(copy_records, source_checks, provenance_checks)
    privacy_data = json_bytes(privacy)
    _replace_literal(privacy_data, token)  # validates token without recording it
    require(_privacy_token_bytes(token).lower() not in privacy_data.lower(), "privacy receipt exposes configured literal")
    assert_no_credentials_bytes(privacy_data, PRIVACY_RECEIPT)
    privacy_id = identity_bytes(privacy_data)
    for destination in (
        layout.tracked_receipts / PRIVACY_RECEIPT,
        layout.provenance / PRIVACY_RECEIPT,
    ):
        _write_bytes(destination, privacy_data, (layout.source, layout.provenance))

    final_source_rows, final_source_manifest_id = _write_source_manifest(layout)
    require(len(final_source_rows) == expected_final_members, "final source-manifest row count differs from nonregression contract")
    provenance_rows, provenance_manifest_id = _write_provenance_manifest(layout)

    # Final direct checks include the generated receipt and manifests.  The
    # inherited carrier remains the sole opaque exception and was hash-bound.
    final_source_closure = _scan_tree_direct(layout.tracked_receipts, token)
    direct_check_file(layout.source / SOURCE_MANIFEST, SOURCE_MANIFEST, token)
    final_provenance = _scan_tree_direct(layout.provenance, token, exclude=frozenset({INHERITED_MEMBER}))
    require(
        (layout.tracked_receipts / NONREGRESSION_RECEIPT).read_bytes()
        == (layout.integration_audits / NONREGRESSION_RECEIPT).read_bytes(),
        "nonregression public copies differ",
    )
    require(
        (layout.tracked_receipts / PRIVACY_RECEIPT).read_bytes()
        == (layout.provenance / PRIVACY_RECEIPT).read_bytes(),
        "privacy public copies differ",
    )
    require(verify_manifest(layout.provenance, PROVENANCE_MANIFEST) == provenance_rows, "final provenance replay failed")

    top = {name: identity(layout.source / name) for name in TOP_LEVEL_CURRENT}
    return {
        "schema": "d033-provenance-nonregression-finalization-result-v1",
        "status": "PASS",
        "repaired_baseline": {"members": len(baseline_rows), "manifest": repaired_manifest_id},
        "final_source_manifest": {"members": len(final_source_rows), "manifest": final_source_manifest_id},
        "source_nonregression": nonregression_id,
        "public_provenance_privacy": privacy_id,
        "provenance_manifest": {"members": len(provenance_rows), "manifest": provenance_manifest_id},
        "top_level_current": top,
        "d033_gate_packet": gate_id,
        "inherited_d019_provenance": {**inherited_copy_id, "recursive_open_performed": False},
        "tracked_closure_files_direct_checked": len(final_source_closure),
        "provenance_files_direct_checked": len(final_provenance),
        "credential_findings": [],
        "tex_runs": 0,
        "archives_created": 0,
        "git_operations": 0,
        "network_operations": 0,
        "publication_operations": 0,
    }


def private_token() -> str:
    token = os.environ.get("USERNAME", "")
    require(token and token.isascii() and token.casefold() == c.TASK.parts[2].casefold(), "configured local-account first-name token unavailable")
    return token


def main() -> None:
    print(json.dumps(finalize(production_layout(), private_token()), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
