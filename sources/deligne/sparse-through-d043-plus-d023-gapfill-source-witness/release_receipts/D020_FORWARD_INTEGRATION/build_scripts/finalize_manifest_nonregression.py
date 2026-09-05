"""Seal the D020 source/provenance trees after build, QA, and visual PASS.

All file copying, hashing, and public-surface checks are streaming.  The script
does not run TeX, create archives, use Git, access a network, or publish.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
from pathlib import Path, PurePosixPath

import d020_contract as c


BUILD = c.TASK / "build/cumulative"
SOURCE = BUILD / "source_tree"
AUDIT = BUILD / "audit"
PROVENANCE = BUILD / "provenance_tree"
TRACKED = SOURCE / "release_receipts/D020_FORWARD_INTEGRATION"
INTEGRATION = PROVENANCE / "integration_audits"
SOURCE_MANIFEST = c.SOURCE_MANIFEST_NAME
PROVENANCE_MANIFEST = "PROVENANCE_MANIFEST.tsv"
INHERITED = "inherited/DELIGNE_PROVENANCE_AUDIT_D033_GAPFILL.zip"
CHANGED = frozenset({"Deligne_EN.pdf", "Deligne_FR.pdf", "Deligne_EN.tex", "Deligne_FR.tex", "README.md"})
RECEIPTS = (
    ("SOURCE_PREPARATION_RECEIPT.json", "SOURCE_PREPARATION_RECEIPT.json"),
    ("COLD_REPRODUCIBILITY_RECEIPT.json", "COLD_REPRODUCIBILITY_RECEIPT.json"),
    ("CUMULATIVE_PAGE_QA.json", "CUMULATIVE_PAGE_QA.json"),
    ("VISUAL_INSPECTION.json", "VISUAL_INSPECTION.json"),
    ("PUBLIC_RECEIPT_SANITIZATION.json", "PUBLIC_RECEIPT_SANITIZATION.json"),
    ("D020_OUTER_BUILD_JOB_RECEIPT.json", "D020_OUTER_BUILD_JOB_RECEIPT.json"),
    # The first two QA launches failed closed while the bounded validator was
    # repaired.  Only retry 03 is the decisive PASS, and it is normalized to
    # the stable public receipt name inside the release closure.
    ("D020_OUTER_QA_RETRY03_JOB_RECEIPT.json", "D020_OUTER_QA_JOB_RECEIPT.json"),
)
SCRIPTS = (
    "build_d020_integration.py",
    "build_tree_runner.py",
    "create_d020_inputs.py",
    "d020_contract.py",
    "finalize_manifest_nonregression.py",
    "package_d020_release.py",
    "sanitize_d020_public_receipts.py",
    "tex_worker.py",
)
CHUNK = 1024 * 1024
MAX_JSON_BYTES = 16 * 1024 * 1024


class Failure(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Failure(message)


def identity(path: Path) -> dict[str, object]:
    try:
        return c.identity(path)
    except (OSError, c.Failure) as exc:
        raise Failure("identity check failed") from exc


def read_json(path: Path) -> object:
    require(path.stat().st_size <= MAX_JSON_BYTES, "JSON receipt exceeds bounded size")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise Failure("JSON receipt is unreadable") from exc


def atomic_write(path: Path, data: bytes) -> dict[str, object]:
    root = SOURCE if path.is_relative_to(SOURCE) else PROVENANCE
    require(path.is_relative_to(root), "write outside public finalization roots")
    path.parent.mkdir(parents=True, exist_ok=True)
    c.reject_reparse(path.parent)
    temporary = path.with_name(f".{path.name}.d020-finalize-{os.getpid()}.tmp")
    require(not temporary.exists(), "stale finalization temporary file")
    try:
        temporary.write_bytes(data)
        expected = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest().upper()}
        c.check(temporary, expected)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)
    return identity(path)


def copy_streaming(source: Path, destination: Path) -> dict[str, object]:
    expected = identity(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(f".{destination.name}.d020-copy-{os.getpid()}.tmp")
    require(not temporary.exists(), "stale closure copy temporary exists")
    try:
        with source.open("rb") as reader, temporary.open("xb") as writer:
            shutil.copyfileobj(reader, writer, CHUNK)
        c.check(temporary, expected)
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)
    return identity(destination)


def write_scan_failure(surface: str, public_name: str, category: str) -> None:
    data = {
        "schema": "d020-finalization-scan-failure-v1",
        "status": "FAIL_CLOSED",
        "surface": surface,
        "public_relative_path": public_name,
        "category": category,
        "sensitive_value_recorded": False,
    }
    path = AUDIT / "FINALIZATION_SCAN_FAILURE.json"
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=True, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def scan_rows(surface: str, root: Path, values: list[dict[str, object]], token: str) -> list[dict[str, object]]:
    scanned = []
    for row in values:
        public_name = str(row["path"])
        try:
            scanned.append(scan_file(c.confined(root, public_name), public_name, token))
        except Failure as exc:
            write_scan_failure(surface, public_name, str(exc))
            raise
    return scanned


def rows(root: Path, exclude: frozenset[str] = frozenset()) -> list[dict[str, object]]:
    names = c.inventory_tree(root)
    require(len(names) <= 10_000, "tree member cap exceeded")
    return [{"path": name, **identity(c.confined(root, name))} for name in names if name not in exclude]


def manifest_bytes(values: list[dict[str, object]]) -> bytes:
    require(values == sorted(values, key=lambda row: row["path"]), "manifest rows not sorted")
    lines = ["path\tbytes\tsha256\n"]
    for row in values:
        name = str(c.safe_relative(str(row["path"])))
        require(re.fullmatch(r"[0-9A-F]{64}", str(row["sha256"])), "manifest hash malformed")
        lines.append(f"{name}\t{int(row['bytes'])}\t{row['sha256']}\n")
    return "".join(lines).encode("utf-8")


def write_manifest(root: Path, name: str) -> tuple[list[dict[str, object]], dict[str, object]]:
    values = rows(root, frozenset({name}))
    seal = atomic_write(root / name, manifest_bytes(values))
    with (root / name).open("r", encoding="utf-8", newline="") as stream:
        replay = [{"path": row["path"], "bytes": int(row["bytes"]), "sha256": row["sha256"]} for row in csv.DictReader(stream, delimiter="\t")]
    require(replay == values, "manifest replay differs")
    return values, seal


def credential_patterns() -> tuple[re.Pattern[bytes], ...]:
    return tuple(re.compile(pattern, re.IGNORECASE) for pattern in (
        b"-----BEGIN (?:[A-Z0-9 ]{0,24})PRIVATE KEY-----",
        b"gh[pousr]_[A-Za-z0-9]{20,}",
        b"github_pat_[A-Za-z0-9_]{20,}",
        rb"(?:access_token|api_key|client_secret|password)\s*[\"']?\s*[:=]\s*[\"']?[A-Za-z0-9_./+=-]{16,}",
        rb"authorization\s*:\s*bearer\s+[A-Za-z0-9_./+=-]{16,}",
    ))


def scan_file(path: Path, public_name: str, token: str) -> dict[str, object]:
    needle = token.encode("ascii").lower()
    require(needle not in public_name.encode("utf-8").lower(), "local-account first name in public path")
    folded_parts = [part.casefold() for part in PurePosixPath(public_name).parts]
    require(not any("credential" in part or part in {".env", "token", "tokens", "secret", "secrets"} for part in folded_parts), "credential-like public path")
    tail = b""
    overlap = max(512, len(needle) - 1)
    patterns = credential_patterns()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(CHUNK), b""):
            sample = tail + block
            require(needle not in sample.lower(), "local-account first name in public bytes")
            require(not any(pattern.search(sample) for pattern in patterns), "credential signature in public bytes")
            tail = sample[-overlap:]
    return identity(path)


def private_token() -> str:
    token = os.environ.get("USERNAME", "")
    require(token.isascii() and token.casefold() == c.TASK.parts[2].casefold(), "privacy token unavailable")
    return token


def main() -> None:
    (AUDIT / "FINALIZATION_SCAN_FAILURE.json").unlink(missing_ok=True)
    cfg = c.config()
    token = private_token()
    prep = read_json(AUDIT / "SOURCE_PREPARATION_RECEIPT.json")
    build = read_json(AUDIT / "COLD_REPRODUCIBILITY_RECEIPT.json")
    qa = read_json(AUDIT / "CUMULATIVE_PAGE_QA.json")
    visual = read_json(AUDIT / "VISUAL_INSPECTION.json")
    outer_build = read_json(AUDIT / "D020_OUTER_BUILD_JOB_RECEIPT.json")
    outer_qa = read_json(AUDIT / "D020_OUTER_QA_RETRY03_JOB_RECEIPT.json")
    require(prep["status"] == build["status"] == qa["status"] == "PASS", "production receipt is not PASS")
    require(visual.get("status") == "PASS" and visual.get("decision") == "PASS", "visual receipt is not PASS")
    require(outer_build.get("status") == "PASS" and outer_qa.get("status") == "PASS", "bounded outer job receipt is not PASS")
    require(not any(marker in (SOURCE / "README.md").read_text(encoding="utf-8") for marker in ("__D020_", "IN_PROGRESS")), "README remains provisional")
    c.verify_source_manifest(SOURCE, SOURCE / SOURCE_MANIFEST)

    pred = Path(cfg["predecessor"]["root"]) / "source_tree"
    predecessor_rows = c.verify_source_manifest(pred, cfg["predecessor"]["source_manifest"]["path"])
    before = {row["path"]: row for row in predecessor_rows}
    current_values = rows(SOURCE, frozenset({SOURCE_MANIFEST}))
    current = {row["path"]: row for row in current_values}
    require(not (set(before) - set(current)), "predecessor source path removed")
    changed = sorted(name for name in set(before) & set(current) if before[name] != current[name])
    added = sorted(set(current) - set(before))
    require(set(changed) == CHANGED, "unexpected predecessor path changed")
    require(all(name.startswith(("works/D020_PUBLIC_SAFE/", "release_receipts/D020_FORWARD_INTEGRATION/")) for name in added), "unexpected source path added")

    INTEGRATION.mkdir(parents=True, exist_ok=True)
    existing_tracked = {p.name for p in TRACKED.iterdir() if p.is_file()}
    allowed_tracked = {
        "D033_PREDECESSOR_BUILD_RELEASE_RECEIPT.json",
        "SOURCE_NONREGRESSION.json",
        "PUBLIC_PROVENANCE_PRIVACY.json",
        *(public_name for _, public_name in RECEIPTS),
    }
    require("D033_PREDECESSOR_BUILD_RELEASE_RECEIPT.json" in existing_tracked, "predecessor receipt missing")
    require(existing_tracked <= allowed_tracked, "tracked receipt prestate differs")
    copied = []
    for source_name, public_name in RECEIPTS:
        source = AUDIT / source_name
        for destination in (TRACKED / public_name, INTEGRATION / public_name):
            copied.append({"path": destination.relative_to(SOURCE if destination.is_relative_to(SOURCE) else PROVENANCE).as_posix(), **copy_streaming(source, destination)})
    for name in SCRIPTS:
        copied.append({"path": f"release_receipts/D020_FORWARD_INTEGRATION/build_scripts/{name}", **copy_streaming(c.TASK / "scripts" / name, TRACKED / "build_scripts" / name)})

    nonregression = {
        "schema": "d020-source-nonregression-v1",
        "status": "PASS",
        "predecessor_work": "D033_RELEASE_BASELINE",
        "predecessor_manifest": {key: cfg["predecessor"]["source_manifest"][key] for key in ("bytes", "sha256")},
        "predecessor_members_replayed": len(predecessor_rows),
        "all_predecessor_paths_retained": True,
        "changed_paths": [{"path": name, "before": before[name], "after": current[name]} for name in changed],
        "added_paths_before_receipt_closure": added,
        "removed_paths": [],
        "d020_inserted_after": "D019",
        "d020_inserted_before": "D021",
        "packaging_performed": False,
    }
    nonregression_data = (json.dumps(nonregression, ensure_ascii=True, indent=2, sort_keys=True) + "\n").encode("utf-8")
    for destination in (TRACKED / "SOURCE_NONREGRESSION.json", INTEGRATION / "SOURCE_NONREGRESSION.json"):
        atomic_write(destination, nonregression_data)

    privacy = {
        "schema": "d020-public-provenance-privacy-v1",
        "status": "PASS_PENDING_FINAL_SCAN",
        "literal_target": "configured local-account first name; value intentionally omitted",
        "policy": "straightforward case-insensitive path/raw-byte scan; no recursive archive privacy machinery",
        "recursive_archive_privacy_scan": False,
        "findings": [],
        "credential_findings": [],
        "inherited_d033_carrier": "already-public byte-identical carrier; raw carrier bytes scanned, members not recursively privacy-scanned",
        "packaging_performed": False,
    }
    privacy_path_source = TRACKED / "PUBLIC_PROVENANCE_PRIVACY.json"
    privacy_path_prov = PROVENANCE / "PUBLIC_PROVENANCE_PRIVACY.json"
    privacy_data = (json.dumps(privacy, ensure_ascii=True, indent=2, sort_keys=True) + "\n").encode("utf-8")
    atomic_write(privacy_path_source, privacy_data)
    atomic_write(privacy_path_prov, privacy_data)

    source_values, source_seal = write_manifest(SOURCE, SOURCE_MANIFEST)
    provenance_values, provenance_seal = write_manifest(PROVENANCE, PROVENANCE_MANIFEST)
    source_scanned = scan_rows("source", SOURCE, source_values, token)
    scan_file(SOURCE / SOURCE_MANIFEST, SOURCE_MANIFEST, token)
    provenance_scanned = scan_rows("provenance", PROVENANCE, provenance_values, token)
    scan_file(PROVENANCE / PROVENANCE_MANIFEST, PROVENANCE_MANIFEST, token)

    privacy["status"] = "PASS"
    privacy["source_files_scanned"] = len(source_scanned) + 1
    privacy["provenance_files_scanned"] = len(provenance_scanned) + 1
    final_privacy = (json.dumps(privacy, ensure_ascii=True, indent=2, sort_keys=True) + "\n").encode("utf-8")
    atomic_write(privacy_path_source, final_privacy)
    atomic_write(privacy_path_prov, final_privacy)
    source_values, source_seal = write_manifest(SOURCE, SOURCE_MANIFEST)
    provenance_values, provenance_seal = write_manifest(PROVENANCE, PROVENANCE_MANIFEST)
    scan_file(privacy_path_source, privacy_path_source.relative_to(SOURCE).as_posix(), token)
    scan_file(privacy_path_prov, privacy_path_prov.relative_to(PROVENANCE).as_posix(), token)
    scan_file(SOURCE / SOURCE_MANIFEST, SOURCE_MANIFEST, token)
    scan_file(PROVENANCE / PROVENANCE_MANIFEST, PROVENANCE_MANIFEST, token)

    result = {
        "schema": "d020-finalization-result-v1",
        "status": "PASS",
        "source_manifest": {"members": len(source_values), **source_seal},
        "provenance_manifest": {"members": len(provenance_values), **provenance_seal},
        "predecessor_members_replayed": len(predecessor_rows),
        "allowed_changed_paths": changed,
        "added_paths_before_receipt_closure": len(added),
        "tracked_closure_copies": len(copied),
        "privacy_status": "PASS",
        "inherited_provenance": identity(PROVENANCE / INHERITED),
        "tex_runs": 0,
        "archives_created": 0,
        "git_operations": 0,
        "network_operations": 0,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
