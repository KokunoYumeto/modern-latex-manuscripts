#!/usr/bin/env python3
"""Build twice, validate twice, finalize, and zip the public v11 checkpoint."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest().upper()


def files(root: Path, excluded: set[str] | None = None) -> list[Path]:
    excluded = excluded or set()
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and path.relative_to(root).as_posix() not in excluded
    )


def digest_map(root: Path, excluded: set[str] | None = None) -> dict[str, str]:
    return {path.relative_to(root).as_posix(): sha256(path) for path in files(root, excluded)}


def run(command: list[str]) -> str:
    result = subprocess.run(command, check=True, text=True, encoding="utf-8", capture_output=True)
    return result.stdout.strip()


def deterministic_zip(source: Path, destination: Path) -> None:
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files(source):
            relative = Path(source.name) / path.relative_to(source)
            info = zipfile.ZipInfo(relative.as_posix(), date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def manifest_role(relative: str) -> str:
    if relative.startswith("data/"):
        return "public_data"
    if relative.startswith("method/"):
        return "public_method"
    if relative.startswith("qa/"):
        return "quality_assurance"
    if relative.startswith("scripts/"):
        return "reproduction_or_validation_script"
    if relative == "README.md":
        return "checkpoint_readme"
    if relative == "PROVENANCE_INPUT_HASHES.json":
        return "input_hash_binding"
    if relative == "BUILD_LOG.md":
        return "build_log"
    return "checkpoint_file"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--zip", type=Path, required=True)
    args = parser.parse_args()
    project_root = args.project_root.resolve()
    output = args.output.resolve()
    zip_path = args.zip.resolve()
    if output.exists() and any(output.iterdir()):
        raise SystemExit(f"refusing nonempty output directory: {output}")
    output.mkdir(parents=True, exist_ok=True)
    zip_path.parent.mkdir(parents=True, exist_ok=True)

    script_dir = Path(__file__).resolve().parent
    builder = script_dir / "build_public_wordweb_checkpoint_v11.py"
    validator = script_dir / "validate_public_wordweb_checkpoint_v11.py"

    with tempfile.TemporaryDirectory(prefix="romance_public_v11_a_") as a_name, tempfile.TemporaryDirectory(prefix="romance_public_v11_b_") as b_name:
        a = Path(a_name) / "checkpoint"
        b = Path(b_name) / "checkpoint"
        run([sys.executable, str(builder), "--project-root", str(project_root), "--output", str(a)])
        run([sys.executable, str(builder), "--project-root", str(project_root), "--output", str(b)])
        run([sys.executable, str(validator), "--output", str(a), "--project-root", str(project_root), "--report", str(a / "qa" / "PUBLIC_CHECKPOINT_VALIDATION_v11.json")])
        run([sys.executable, str(validator), "--output", str(b), "--project-root", str(project_root), "--report", str(b / "qa" / "PUBLIC_CHECKPOINT_VALIDATION_v11.json")])
        map_a = digest_map(a)
        map_b = digest_map(b)
        if map_a != map_b:
            differing = sorted(set(map_a) | set(map_b))
            differing = [name for name in differing if map_a.get(name) != map_b.get(name)]
            raise SystemExit(f"nondeterministic build: {differing}")

        run([sys.executable, str(builder), "--project-root", str(project_root), "--output", str(output)])
        validation_stdout = run([sys.executable, str(validator), "--output", str(output), "--project-root", str(project_root), "--report", str(output / "qa" / "PUBLIC_CHECKPOINT_VALIDATION_v11.json")])
        live_map = digest_map(output)
        if live_map != map_a:
            differing = sorted(set(live_map) | set(map_a))
            differing = [name for name in differing if live_map.get(name) != map_a.get(name)]
            raise SystemExit(f"live build differs from isolated builds: {differing}")

    validation = json.loads(validation_stdout)
    provenance = json.loads((output / "PROVENANCE_INPUT_HASHES.json").read_text(encoding="utf-8"))
    set_hash_material = "\n".join(f"{name},{value}" for name, value in sorted(live_map.items())).encode("utf-8")
    set_hash = hashlib.sha256(set_hash_material).hexdigest().upper()
    build_log = f"""# Deterministic build log — public Romance WordWeb/access v11

Status: **PASS**

- Two isolated builds were made from the same four SHA-bound internal v11 inputs.
- Both isolated builds ran the independent semantic/access/public-safety validator.
- The live build was rebuilt separately and matched both isolated builds byte-for-byte.
- Stable pre-finalization file count: {len(live_map)}.
- Stable pre-finalization set hash: `{set_hash}`.
- Validator checks: {validation['checks_passed']}/{validation['checks_total']} passed.
- Source-input binding was recomputed: `{str(validation['source_binding_checked']).lower()}`.
- Counts: 60 concepts; 106 senses; 39 extension nodes; 811 evidence-metadata records; 106 decisions; 406 relation records with 27 target-ID edges; 78 supported senses and 28 gaps; 954 access rows across nine cohorts.
- Human observations: 0. Pilot-eligible rows/decisions: 0. Form promotions: 0.
- Public-safety scan rejects quote/locator/source-path keys and absolute host-path values.
- A deterministic ZIP is written twice with fixed member timestamps and permissions; its final hash is intentionally recorded outside the archive to avoid self-reference.

Input hashes:

""" + "\n".join(f"- `{name}`: `{value}`" for name, value in provenance["input_hashes"].items()) + """

Claim boundary: this log establishes deterministic projection and validation only. It does not clear underlying source rights, supply human observations, certify intelligibility, or complete the Romance lane.
"""
    (output / "BUILD_LOG.md").write_text(build_log, encoding="utf-8", newline="\n")

    manifest_path = output / "CHECKPOINT_SHA256.csv"
    rows = []
    for path in files(output, {"CHECKPOINT_SHA256.csv"}):
        relative = path.relative_to(output).as_posix()
        rows.append(
            {
                "relative_path": relative,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "role": manifest_role(relative),
                "public_scope": "yes",
            }
        )
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    with manifest_path.open(encoding="utf-8", newline="") as handle:
        parsed = list(csv.DictReader(handle))
    for row in parsed:
        path = output / Path(row["relative_path"])
        if not path.is_file() or path.stat().st_size != int(row["bytes"]) or sha256(path) != row["sha256"]:
            raise SystemExit(f"manifest verification failed: {row['relative_path']}")

    with tempfile.TemporaryDirectory(prefix="romance_public_zip_") as temp_name:
        first = Path(temp_name) / "first.zip"
        second = Path(temp_name) / "second.zip"
        deterministic_zip(output, first)
        deterministic_zip(output, second)
        if sha256(first) != sha256(second):
            raise SystemExit("deterministic ZIP replay mismatch")
        zip_path.write_bytes(first.read_bytes())

    summary = {
        "status": "PASS",
        "output_file_count": len(files(output)),
        "manifest_rows": len(parsed),
        "manifest_sha256": sha256(manifest_path),
        "zip_sha256": sha256(zip_path),
        "zip_bytes": zip_path.stat().st_size,
        "validation_checks": f"{validation['checks_passed']}/{validation['checks_total']}",
        "source_input_hashes": provenance["input_hashes"],
    }
    print(json.dumps(summary, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
