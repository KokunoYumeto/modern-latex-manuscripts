#!/usr/bin/env python3
"""Build the compact SGA1 reference-v2 and refreshed SGA1-6 ZIPs."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import zipfile
from pathlib import Path, PurePosixPath, PureWindowsPath


ROOT = "SGA_Current_English_Readers_and_TeX_20260730"
SOURCE_ZIP_ROOT = "SGA1_English_Complete_ReferenceV2_R2_Public_20260730"
FIXED_ZIP_TIME = (2026, 7, 30, 12, 0, 0)
EXCLUDED_FROM_PACKAGE_MANIFEST = {
    "PACKAGE_VALIDATION.json",
    "ZENODO_PAYLOAD_MANIFEST.csv",
}
SGA1_READER = f"{ROOT}/SGA1/reader/SGA1_English_Reader.pdf"
SGA1_MASTER = (
    f"{ROOT}/SGA1/source/SGA1_English_source_sync_workpass.tex"
)
ROOT_MANIFEST = f"{ROOT}/SHA256SUMS.csv"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) >= 2 and name[1] == ":")
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    info.create_system = 3
    return info


def write_member(archive: zipfile.ZipFile, name: str, data: bytes) -> None:
    if not safe_member(name):
        raise RuntimeError(f"unsafe ZIP member path: {name}")
    archive.writestr(zip_info(name), data, compresslevel=9)


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def validate_candidate(candidate: Path) -> dict:
    manifest_path = candidate / "ZENODO_PAYLOAD_MANIFEST.csv"
    validation_path = candidate / "PACKAGE_VALIDATION.json"
    rows = read_manifest(manifest_path)
    actual = {
        path.relative_to(candidate).as_posix(): path
        for path in candidate.rglob("*")
        if path.is_file()
        and path.relative_to(candidate).as_posix()
        not in EXCLUDED_FROM_PACKAGE_MANIFEST
    }
    by_path = {row["relative_path"]: row for row in rows}
    if len(rows) != 178 or len(by_path) != 178 or set(by_path) != set(actual):
        raise RuntimeError("candidate manifest exact-set closure failed")
    for name, path in actual.items():
        row = by_path[name]
        observed = (path.stat().st_size, sha256_path(path))
        expected = (int(row["bytes"]), row["sha256"].upper())
        if observed != expected:
            raise RuntimeError(f"candidate manifest mismatch: {name}")
    validation = json.loads(validation_path.read_text(encoding="utf-8-sig"))
    if validation.get("status") != "PASS" or validation.get("errors"):
        raise RuntimeError("candidate packaged validation is not PASS")
    files = sorted(
        (path for path in candidate.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(candidate).as_posix(),
    )
    canonical = hashlib.sha256()
    identities = {}
    for path in files:
        relative = path.relative_to(candidate).as_posix()
        identity = {
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
        }
        identities[relative] = identity
        canonical.update(
            (
                f"{relative}\t{identity['bytes']}\t{identity['sha256']}\n"
            ).encode("utf-8")
        )
    return {
        "files": len(files),
        "bytes": sum(item["bytes"] for item in identities.values()),
        "canonical_identity_sha256": canonical.hexdigest().upper(),
        "manifest_rows": len(rows),
        "manifest_sha256": sha256_path(manifest_path),
        "package_validation_sha256": sha256_path(validation_path),
        "identities": identities,
    }


def write_payload_manifest(
    projection: Path,
    source_rows: dict[str, dict[str, str]],
) -> None:
    files = sorted(
        (
            path
            for path in projection.rglob("*")
            if path.is_file()
            and path.relative_to(projection).as_posix()
            not in EXCLUDED_FROM_PACKAGE_MANIFEST
        ),
        key=lambda path: path.relative_to(projection).as_posix().casefold(),
    )
    rows = []
    for path in files:
        relative = path.relative_to(projection).as_posix()
        source = source_rows[relative]
        digest = sha256_path(path)
        rows.append(
            {
                "manifest_id": f"sga1.public.sha256.{digest.lower()}",
                "relative_path": relative,
                "bytes": str(path.stat().st_size),
                "sha256": digest,
                "role": source["role"],
                "status": source["status"],
            }
        )
    manifest = projection / "ZENODO_PAYLOAD_MANIFEST.csv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "manifest_id",
                "relative_path",
                "bytes",
                "sha256",
                "role",
                "status",
            ],
            lineterminator="\r\n",
            quoting=csv.QUOTE_ALL,
        )
        writer.writeheader()
        writer.writerows(rows)


def sanitize_reproducibility_json(path: Path) -> None:
    value = json.loads(path.read_text(encoding="utf-8-sig"))

    def scrub(item: object) -> object:
        if isinstance(item, dict):
            return {
                key: (
                    PureWindowsPath(child).name
                    if key == "path" and isinstance(child, str)
                    else scrub(child)
                )
                for key, child in item.items()
            }
        if isinstance(item, list):
            return [scrub(child) for child in item]
        return item

    path.write_text(
        json.dumps(scrub(value), indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def sanitize_build_log(path: Path) -> None:
    text = path.read_text(encoding="utf-8", errors="strict")
    text = re.sub(
        r"C:/User\r?\ns/Floris",
        "<USER_HOME>",
        text,
        flags=re.IGNORECASE,
    )
    for token in (
        r"C:\\Users\\Floris",
        r"C:\Users\Floris",
        "C:/Users/Floris",
        "/Users/Floris",
    ):
        text = text.replace(token, "<USER_HOME>")
    text = text.replace("Floris", "<USER>")
    path.write_text(text, encoding="utf-8", newline="")


def build_public_projection(candidate: Path, projection: Path) -> dict:
    candidate = candidate.resolve()
    projection = projection.resolve()
    if projection == candidate or candidate in projection.parents:
        raise RuntimeError("public projection path overlaps the frozen candidate")
    if projection.exists():
        shutil.rmtree(projection)
    projection.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(candidate, projection)

    for name in (
        "REPRODUCIBILITY_BUILD_A_VS_BUILD_B.json",
        "REPRODUCIBILITY_FINAL_VS_BUILD_A.json",
    ):
        sanitize_reproducibility_json(projection / "build_evidence" / name)
    for name in (
        "final_tex_log_sanitized.txt",
        "pass3_console_sanitized.txt",
        "pass4_console_sanitized.txt",
    ):
        sanitize_build_log(projection / "build_evidence" / name)

    status_path = projection / "STATUS.md"
    status = status_path.read_text(encoding="utf-8")
    status = status.split("## Coordination", 1)[0].rstrip()
    status += """

## Public release status

This public projection contains the complete cumulative reader, its buildable
TeX closure, and privacy-clean technical evidence. Internal task coordination
and machine-local paths are deliberately omitted. Earlier bounded checkpoints
remain available as immutable release history.
"""
    status_path.write_text(status, encoding="utf-8", newline="\n")

    readiness_path = projection / "PUBLICATION_READINESS.md"
    readiness = readiness_path.read_text(encoding="utf-8")
    archive_start = readiness.index("Archive action:")
    manifest_start = readiness.index(
        "The manifest `ZENODO_PAYLOAD_MANIFEST.csv`", archive_start
    )
    readiness = (
        readiness[:archive_start]
        + """Public projection:

- Machine-local paths and internal task-coordination notes are omitted.
- The cumulative PDF, master, 138 components, reference graph, and mathematical
  text are byte-identical to the frozen R2 custody package.
- Publication must remain on the existing SGA concept; no duplicate concept is
  authorized.

"""
        + readiness[manifest_start:]
    )
    readiness_path.write_text(readiness, encoding="utf-8", newline="\n")

    source_rows = {
        row["relative_path"]: row
        for row in read_manifest(candidate / "ZENODO_PAYLOAD_MANIFEST.csv")
    }
    write_payload_manifest(projection, source_rows)
    validation_path = projection / "PACKAGE_VALIDATION.json"
    validation = json.loads(validation_path.read_text(encoding="utf-8-sig"))
    validation["schema"] = "sga1-complete-reference-public-projection-1.0"
    validation["package"]["manifest_sha256"] = sha256_path(
        projection / "ZENODO_PAYLOAD_MANIFEST.csv"
    )
    validation["privacy_hits"] = []
    validation["public_projection"] = {
        "source_package": candidate.name,
        "source_files": 180,
        "reader_and_tex_changed": False,
        "sanitized_build_evidence_files": 5,
        "internal_coordination_removed": True,
    }
    save_json(validation_path, validation)

    private_pattern = re.compile(
        r"(?i)(C:(?:[/\\]|\\\\)+Users(?:[/\\]|\\\\)+|"
        r"C:/User\s*s/|/Users/Floris|Floris|Papors|Chatnotes|"
        r"\.codex|019f[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-"
        r"[0-9a-f]{4}-[0-9a-f]{12})"
    )
    hits = []
    text_suffixes = {
        ".csv",
        ".json",
        ".jsonl",
        ".log",
        ".md",
        ".py",
        ".tex",
        ".texfrag",
        ".txt",
    }
    for path in projection.rglob("*"):
        if path.is_file() and path.suffix.lower() in text_suffixes:
            text = path.read_text(encoding="utf-8", errors="ignore")
            match = private_pattern.search(text)
            if match:
                hits.append(
                    {
                        "path": path.relative_to(projection).as_posix(),
                        "token": match.group(0),
                    }
                )
    if hits:
        raise RuntimeError(f"public projection privacy scan failed: {hits[:5]}")
    result = validate_candidate(projection)
    result["sanitized_build_evidence_files"] = 5
    result["privacy_hits"] = []
    return result


def build_source_zip(candidate: Path, output: Path) -> dict:
    temporary = output.with_suffix(output.suffix + ".tmp")
    temporary.parent.mkdir(parents=True, exist_ok=True)
    temporary.unlink(missing_ok=True)
    files = sorted(
        (path for path in candidate.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(candidate).as_posix(),
    )
    with zipfile.ZipFile(temporary, "w", allowZip64=True) as archive:
        for path in files:
            relative = path.relative_to(candidate).as_posix()
            write_member(
                archive,
                f"{SOURCE_ZIP_ROOT}/{relative}",
                path.read_bytes(),
            )
    with zipfile.ZipFile(temporary) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        if len(infos) != len(files):
            raise RuntimeError("SGA1 source ZIP member count changed")
        for path, info in zip(files, infos, strict=True):
            data = archive.read(info.filename)
            if (
                len(data),
                sha256_bytes(data),
            ) != (path.stat().st_size, sha256_path(path)):
                raise RuntimeError(f"SGA1 source ZIP replay failed: {info.filename}")
    temporary.replace(output)
    return {
        "name": output.name,
        "bytes": output.stat().st_size,
        "sha256": sha256_path(output),
        "members": len(files),
        "uncompressed_bytes": sum(path.stat().st_size for path in files),
    }


def manifest_bytes(members: dict[str, bytes]) -> bytes:
    lines = ["relative_path,bytes,sha256\r\n"]
    for name in sorted(members, key=str.casefold):
        relative = name.removeprefix(f"{ROOT}/")
        data = members[name]
        lines.append(f'"{relative}",{len(data)},{sha256_bytes(data)}\r\n')
    return "".join(lines).encode("utf-8")


def build_current_bundle(
    existing: Path,
    candidate: Path,
    output: Path,
) -> dict:
    with zipfile.ZipFile(existing) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename for info in infos]
        if (
            len(names) != 1394
            or len(set(names)) != len(names)
            or ROOT_MANIFEST not in names
            or not all(map(safe_member, names))
        ):
            raise RuntimeError("existing SGA bundle boundary changed")
        members = {
            name: archive.read(name)
            for name in names
            if name != ROOT_MANIFEST
        }

    candidate_drafts = {
        path.name: path.read_bytes()
        for path in sorted((candidate / "drafts").glob("*.texfrag"))
    }
    bundled_drafts = {
        name.rsplit("/", 1)[1]: data
        for name, data in members.items()
        if name.startswith(f"{ROOT}/SGA1/source/drafts/")
    }
    if set(candidate_drafts) != set(bundled_drafts):
        raise RuntimeError("candidate and bundled SGA1 component path sets differ")
    for filename, data in candidate_drafts.items():
        members[f"{ROOT}/SGA1/source/drafts/{filename}"] = data

    members[SGA1_READER] = (
        candidate / "SGA1_English_complete_reference_reader.pdf"
    ).read_bytes()
    members[SGA1_MASTER] = (
        candidate / "SGA1_English_source_sync_workpass.tex"
    ).read_bytes()
    manifest = manifest_bytes(members)

    temporary = output.with_suffix(output.suffix + ".tmp")
    temporary.unlink(missing_ok=True)
    with zipfile.ZipFile(temporary, "w", allowZip64=True) as archive:
        for name in sorted(members, key=str.casefold):
            write_member(archive, name, members[name])
        write_member(archive, ROOT_MANIFEST, manifest)

    with zipfile.ZipFile(temporary) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename for info in infos]
        if len(infos) != 1394 or len(set(names)) != 1394:
            raise RuntimeError("refreshed SGA bundle member count changed")
        rows = list(
            csv.DictReader(
                io.StringIO(archive.read(ROOT_MANIFEST).decode("utf-8-sig"))
            )
        )
        if len(rows) != 1393:
            raise RuntimeError("refreshed SGA bundle manifest row count changed")
        represented = {}
        for row in rows:
            name = f"{ROOT}/{row['relative_path']}"
            data = archive.read(name)
            observed = (len(data), sha256_bytes(data))
            expected = (int(row["bytes"]), row["sha256"].upper())
            if observed != expected:
                raise RuntimeError(f"refreshed SGA bundle mismatch: {name}")
            represented[name] = observed
        if set(represented) != set(names) - {ROOT_MANIFEST}:
            raise RuntimeError("refreshed SGA bundle manifest closure failed")
        if sha256_bytes(archive.read(SGA1_READER)) != (
            "46406925C8EBBF4309A67CF4D84B493952EF99C067E1971F885F0F3AF326BA1E"
        ):
            raise RuntimeError("refreshed SGA bundle has the wrong SGA1 reader")
    temporary.replace(output)
    return {
        "name": output.name,
        "bytes": output.stat().st_size,
        "sha256": sha256_path(output),
        "members": 1394,
        "manifest_rows": 1393,
        "uncompressed_bytes": sum(len(data) for data in members.values())
        + len(manifest),
        "sga1_reader_sha256": sha256_bytes(members[SGA1_READER]),
        "sga1_master_sha256": sha256_bytes(members[SGA1_MASTER]),
    }


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--projection-output", type=Path, required=True)
    parser.add_argument("--existing-bundle", type=Path, required=True)
    parser.add_argument("--bundle-output", type=Path, required=True)
    parser.add_argument("--source-zip-output", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    candidate = args.candidate.resolve()
    projection = args.projection_output.resolve()
    existing = args.existing_bundle.resolve()
    bundle_output = args.bundle_output.resolve()
    source_zip_output = args.source_zip_output.resolve()
    source_candidate = validate_candidate(candidate)
    public_projection = build_public_projection(candidate, projection)
    report = {
        "schema": "sga1-reference-v2-compact-release-build-1.0",
        "status": "PASS",
        "source_candidate": source_candidate,
        "public_projection": public_projection,
        "source_zip": build_source_zip(projection, source_zip_output),
        "current_sga1_6_bundle": build_current_bundle(
            existing,
            projection,
            bundle_output,
        ),
    }
    save_json(args.report.resolve(), report)
    print(json.dumps(report, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
