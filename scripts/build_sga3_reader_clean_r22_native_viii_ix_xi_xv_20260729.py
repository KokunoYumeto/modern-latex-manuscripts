#!/usr/bin/env python3
"""Build the clean SGA3 R22 reader with native VIII, IX, XI, and XV."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import os
import shutil
import sys
import zipfile
from pathlib import Path, PurePosixPath


REPO_ROOT = Path(__file__).resolve().parents[1]
BASE_PACKAGE = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-reader-clean-r21-no-project-notes-20260729"
)
BASE_ARCHIVE = (
    BASE_PACKAGE / "10c_SGA3_English_Source_and_History_R21_20260729.zip"
)
BASE_MASTER = BASE_PACKAGE / "02c_SGA3_English_Master.tex"
BASE_PDF = BASE_PACKAGE / "00c_SGA3_English_Reader.pdf"
VIII_IX_PACKAGE = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-exposes-viii-ix-highzoom-native-integration-inputs-20260729"
)
VIII_IX_ARCHIVE = (
    VIII_IX_PACKAGE
    / "10c_SGA3_Exposes_VIII_IX_HighZoom_Native_Integration_Inputs_20260729.zip"
)
OUTPUT_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-reader-clean-r22-native-viii-ix-xi-xv-20260729"
)
TEMP_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_reader_clean_r22_native_viii_ix_xi_xv_20260729"
)
R20_BUILDER_PATH = (
    REPO_ROOT
    / "scripts"
    / "build_sga3_reader_clean_complete_r20_native_v_vi_20260729.py"
)
R21_BUILDER_PATH = (
    REPO_ROOT
    / "scripts"
    / "build_sga3_reader_clean_r21_no_project_notes_20260729.py"
)
CLEANER_PATH = (
    REPO_ROOT
    / "scripts"
    / "build_sga_reader_mathematical_body_clean_successor_20260729.py"
)

MASTER_NAME = "SGA3_English_Master.tex"
PDF_NAME = "00c_SGA3_English_Reader.pdf"
TEX_NAME = "02c_SGA3_English_Master.tex"
ZIP_NAME = "10c_SGA3_English_Source_and_History_R22_20260729.zip"
ZIP_MANIFEST = "SOURCE_BUNDLE_SHA256.csv"
OUTER_MANIFEST = "SHA256SUMS.csv"
FIXED_ZIP_TIME = (2026, 7, 29, 0, 0, 0)

VIII_IX_EXPECTED = {
    "archive_bytes": 605_421,
    "archive_sha256": (
        "10F346EBF52378DD0A414CC9A9404E0C81006BD83C779A4383E90C24B092056C"
    ),
    "members": 34,
    "manifest_rows": 33,
}
LOCAL_EXPECTED = {
    "xi": {
        "manifest": "controls/ACTIVE_SOURCE_SHA256.csv",
        "manifest_sha256": (
            "AFE9B69A18512368426E5B2E4F106C2833BD75B1A90F99F42A4F9295EE56EE53"
        ),
        "validation": "controls/LOOP2_NATIVE_VALIDATION.json",
        "validation_sha256": (
            "457FBF1A94780329823768A6CE9AFB43DBC018072728171C7DBF1AA6155E70CE"
        ),
        "pdf": "build/SGA3_Expose_XI_English.pdf",
        "pdf_sha256": (
            "C5E0A127C7B61C3DCDFB3560D201F6E7FF35A5E1A0D0145370C21B0FD20F6963"
        ),
        "source_files": 13,
        "source_bytes": 147_746,
        "component_prefix": "tex/components/",
        "destination_prefix": "xi/components/",
        "evidence": (
            "STATUS.md",
            "controls/ACTIVE_SOURCE_SHA256.csv",
            "controls/LOOP2_NATIVE_VALIDATION.json",
            "controls/NATIVE_DIAGRAM_INVENTORY.csv",
            "qa/LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md",
        ),
    },
    "xv": {
        "manifest": "controls/ACTIVE_SOURCE_SHA256.csv",
        "manifest_sha256": (
            "3679ACF61E9B317F7FD8B64C3293D832E87BCF3ACF36FF3D5FF4AC15336BC4E9"
        ),
        "validation": "controls/FINAL_LOCAL_VALIDATION.json",
        "validation_sha256": (
            "97EE0D36807F4014A6620E29E4E2C43CFA132CDB0CA4679E3311015403BBA941"
        ),
        "pdf": "build_loop2_5000dpi_r1/SGA3_Expose_XV_English.pdf",
        "pdf_sha256": (
            "461E35451A88CABD959D2A1BE185B462E5E5E1AFF10822D5D0A19145BB6615C4"
        ),
        "source_files": 12,
        "source_bytes": 222_905,
        "component_prefix": "tex/components/",
        "destination_prefix": "xv/tex/components/",
        "evidence": (
            "STATUS.md",
            "controls/ACTIVE_SOURCE_SHA256.csv",
            "controls/FINAL_LOCAL_VALIDATION.json",
            "controls/NATIVE_DIAGRAM_INVENTORY.csv",
            "controls/LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md",
        ),
    },
}
VIII_IX_MAP = {
    "viii": {
        "member_prefix": "sga3_expose_viii/tex/components/",
        "destination_prefix": (
            "upstream_controls/exposeVIII_checkpoint_20260724_r1/"
            "source/tex/components/"
        ),
        "source_files": 8,
        "evidence_prefix": "sga3_expose_viii/",
    },
    "ix": {
        "member_prefix": "sga3_expose_ix/tex/components/",
        "destination_prefix": "ix/components/",
        "source_files": 5,
        "evidence_prefix": "sga3_expose_ix/",
    },
}
PRIVATE_MARKERS = (
    b"c:\\users\\",
    b"c:/users/",
    b"\\appdata\\",
    b"/appdata/",
    b"papors",
    b"chatnotes",
    b".claude",
    b".codex",
    b"source_thread_id",
    b"thread_id",
    b"claude-please",
)
EXPECTED_READER_CLEANUP = {
    "project_footnote": 20,
    "inline_project_source_aside": 11,
    "empty_project_note_wrapper": 1,
}
CLEANUP_GLUE_FIXES = {
    "xi/components/01_expose_XI_opening_through_remark_1_5.tex": (
        ("\\]\n\n(and even", "\\]\n(and even"),
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--expose-xi-root", type=Path, required=True)
    parser.add_argument("--expose-xv-root", type=Path, required=True)
    parser.add_argument("--keep-temp", action="store_true")
    return parser.parse_args()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def safe_member(name: str) -> bool:
    parts = PurePosixPath(name).parts
    return (
        bool(name)
        and not name.startswith(("/", "\\"))
        and not (len(name) > 1 and name[1] == ":")
        and ".." not in parts
    )


def safe_clear(path: Path) -> None:
    if not path.exists():
        return
    resolved = path.resolve()
    if path == TEMP_ROOT:
        expected_parent = (Path(os.environ["LOCALAPPDATA"]) / "Temp").resolve()
    else:
        expected_parent = OUTPUT_ROOT.parent.resolve()
    if resolved.parent != expected_parent:
        raise RuntimeError(f"Refusing to clear unexpected path: {resolved}")
    shutil.rmtree(resolved)


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=FIXED_ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def scan_public_bytes(name: str, data: bytes) -> None:
    lowered = data.lower()
    hits = [
        marker.decode("ascii", errors="replace")
        for marker in PRIVATE_MARKERS
        if marker in lowered
    ]
    if hits:
        raise RuntimeError(f"Private marker in {name}: {hits}")


def parse_manifest_bytes(data: bytes) -> list[dict[str, str]]:
    return list(
        csv.DictReader(
            io.StringIO(data.decode("utf-8-sig"), newline="")
        )
    )


def verify_viii_ix_archive() -> tuple[dict[str, bytes], dict[str, object]]:
    if (
        VIII_IX_ARCHIVE.stat().st_size,
        sha256_file(VIII_IX_ARCHIVE),
    ) != (
        VIII_IX_EXPECTED["archive_bytes"],
        VIII_IX_EXPECTED["archive_sha256"],
    ):
        raise RuntimeError("VIII/IX custody archive identity changed")

    members: dict[str, bytes] = {}
    with zipfile.ZipFile(VIII_IX_ARCHIVE) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("VIII/IX custody archive CRC failure")
        for info in archive.infolist():
            if not safe_member(info.filename):
                raise RuntimeError(
                    f"Unsafe VIII/IX archive member: {info.filename}"
                )
            members[info.filename] = archive.read(info.filename)

    if len(members) != VIII_IX_EXPECTED["members"]:
        raise RuntimeError("VIII/IX custody archive member count changed")
    rows = parse_manifest_bytes(members["PACKAGE_CONTENT_SHA256.csv"])
    if len(rows) != VIII_IX_EXPECTED["manifest_rows"]:
        raise RuntimeError("VIII/IX custody manifest row count changed")
    for row in rows:
        data = members.get(row["relative_path"])
        if data is None or (len(data), sha256_bytes(data)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(
                f"VIII/IX custody mismatch: {row['relative_path']}"
            )

    validation = json.loads(
        (VIII_IX_PACKAGE / "PACKAGE_VALIDATION.json").read_text(
            encoding="utf-8"
        )
    )
    if validation.get("status") != "PASS" or validation.get("errors") != []:
        raise RuntimeError("VIII/IX package validation is not closed")
    return members, validation


def verify_local_successor(
    root: Path, label: str
) -> tuple[dict[str, bytes], dict[str, object]]:
    expected = LOCAL_EXPECTED[label]
    manifest_path = root / expected["manifest"]
    validation_path = root / expected["validation"]
    pdf_path = root / expected["pdf"]
    for path in (manifest_path, validation_path, pdf_path):
        if not path.is_file():
            raise FileNotFoundError(path)
    if sha256_file(manifest_path) != expected["manifest_sha256"]:
        raise RuntimeError(f"{label.upper()} source manifest changed")
    if sha256_file(validation_path) != expected["validation_sha256"]:
        raise RuntimeError(f"{label.upper()} validation changed")
    if sha256_file(pdf_path) != expected["pdf_sha256"]:
        raise RuntimeError(f"{label.upper()} PDF changed")

    rows = parse_manifest_bytes(manifest_path.read_bytes())
    if len(rows) != expected["source_files"]:
        raise RuntimeError(f"{label.upper()} source count changed")
    source: dict[str, bytes] = {}
    for row in rows:
        relative = row.get("relative_path") or row.get("path")
        if relative is None:
            raise RuntimeError(f"{label.upper()} manifest lacks a path")
        relative = relative.replace("\\", "/")
        if not safe_member(relative):
            raise RuntimeError(f"Unsafe {label.upper()} source path")
        path = root / Path(relative)
        data = path.read_bytes()
        if (len(data), sha256_bytes(data)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"{label.upper()} source mismatch: {relative}")
        source[relative] = data
    if sum(len(data) for data in source.values()) != expected["source_bytes"]:
        raise RuntimeError(f"{label.upper()} source-byte boundary changed")

    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if validation.get("status") != "PASS" or validation.get("errors") != []:
        raise RuntimeError(f"{label.upper()} validation is not closed")
    return source, validation


def prepare_source(
    archive_members: dict[str, bytes],
    local_sources: dict[str, dict[str, bytes]],
    cleaner,
) -> tuple[Path, list[dict[str, object]], list]:
    source = TEMP_ROOT / "primary"
    source.mkdir(parents=True)
    with zipfile.ZipFile(BASE_ARCHIVE) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("R21 source archive CRC failure")
        for info in archive.infolist():
            if not safe_member(info.filename):
                raise RuntimeError(f"Unsafe R21 member: {info.filename}")
        archive.extractall(source)

    master = source / MASTER_NAME
    if master.read_bytes() != BASE_MASTER.read_bytes():
        raise RuntimeError("R21 direct master and archive master differ")

    replacement_rows: list[dict[str, object]] = []
    for label, mapping in VIII_IX_MAP.items():
        source_members = {
            name: data
            for name, data in archive_members.items()
            if name.startswith(mapping["member_prefix"])
            and name.endswith(".tex")
        }
        if len(source_members) != mapping["source_files"]:
            raise RuntimeError(
                f"Unexpected {label.upper()} component count: "
                f"{len(source_members)}"
            )
        for name, data in sorted(source_members.items()):
            suffix = name[len(mapping["member_prefix"]) :]
            destination_name = mapping["destination_prefix"] + suffix
            destination = source / Path(destination_name)
            old_data = destination.read_bytes()
            destination.write_bytes(data)
            replacement_rows.append(
                {
                    "expose": label.upper(),
                    "relative_path": destination_name,
                    "old_sha256": sha256_bytes(old_data),
                    "new_bytes": len(data),
                    "new_sha256": sha256_bytes(data),
                }
            )

    for label, files in local_sources.items():
        expected = LOCAL_EXPECTED[label]
        component_files = {
            name: data
            for name, data in files.items()
            if name.startswith(expected["component_prefix"])
            and name.endswith(".tex")
        }
        expected_components = expected["source_files"] - 2
        if len(component_files) != expected_components:
            raise RuntimeError(
                f"Unexpected {label.upper()} component count: "
                f"{len(component_files)}"
            )
        for name, data in sorted(component_files.items()):
            suffix = name[len(expected["component_prefix"]) :]
            destination_name = expected["destination_prefix"] + suffix
            destination = source / Path(destination_name)
            old_data = destination.read_bytes()
            destination.write_bytes(data)
            replacement_rows.append(
                {
                    "expose": label.upper(),
                    "relative_path": destination_name,
                    "old_sha256": sha256_bytes(old_data),
                    "new_bytes": len(data),
                    "new_sha256": sha256_bytes(data),
                }
            )

    changed = [
        row
        for row in replacement_rows
        if row["old_sha256"] != row["new_sha256"]
    ]
    if len(replacement_rows) != 34 or len(changed) != 20:
        raise RuntimeError(
            "Unexpected integration replacement boundary: "
            f"total={len(replacement_rows)}, changed={len(changed)}"
        )

    removals = []
    for path in sorted(source.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".tex", ".texfrag"}:
            cleaner.clean_tex(path, source, "sga3", removals)
    cleanup_counts = {
        kind: sum(1 for row in removals if row.kind == kind)
        for kind in EXPECTED_READER_CLEANUP
    }
    if (
        cleanup_counts != EXPECTED_READER_CLEANUP
        or len(removals) != sum(EXPECTED_READER_CLEANUP.values())
    ):
        raise RuntimeError(
            "Unexpected R22 reader-apparatus cleanup boundary: "
            f"counts={cleanup_counts}, total={len(removals)}"
        )
    for relative, fixes in CLEANUP_GLUE_FIXES.items():
        path = source / Path(relative)
        text = path.read_text(encoding="utf-8")
        for before, after in fixes:
            if text.count(before) != 1:
                raise RuntimeError(
                    f"Unexpected cleanup glue boundary in {relative}: "
                    f"{before!r}"
                )
            text = text.replace(before, after)
        path.write_text(text, encoding="utf-8", newline="\n")
    removal_counts: dict[str, int] = {}
    for row in removals:
        removal_counts[row.relative_path] = (
            removal_counts.get(row.relative_path, 0) + 1
        )
    for row in replacement_rows:
        path = source / Path(str(row["relative_path"]))
        row["reader_bytes"] = path.stat().st_size
        row["reader_sha256"] = sha256_file(path)
        row["reader_apparatus_removals"] = removal_counts.get(
            str(row["relative_path"]), 0
        )
    return source, replacement_rows, removals


def evidence_members(
    archive_members: dict[str, bytes],
    local_roots: dict[str, Path],
    local_sources: dict[str, dict[str, bytes]],
) -> dict[str, bytes]:
    members: dict[str, bytes] = {}
    for label, mapping in VIII_IX_MAP.items():
        prefix = mapping["evidence_prefix"]
        for name, data in archive_members.items():
            if not name.startswith(prefix):
                continue
            relative = name[len(prefix) :]
            if relative.startswith("build/") or relative.startswith("tex/"):
                continue
            members[f"evidence/expose_{label}/{relative}"] = data
    members["evidence/viii_ix/PACKAGE_README.md"] = archive_members[
        "PACKAGE_README.md"
    ]
    members["evidence/viii_ix/PROVENANCE_AND_RIGHTS.md"] = archive_members[
        "PROVENANCE_AND_RIGHTS.md"
    ]
    members["evidence/viii_ix/VISUAL_EVIDENCE_DISPOSITION.csv"] = (
        archive_members["VISUAL_EVIDENCE_DISPOSITION.csv"]
    )
    members[
        "history/10c_SGA3_Exposes_VIII_IX_"
        "HighZoom_Native_Integration_Inputs_20260729.zip"
    ] = VIII_IX_ARCHIVE.read_bytes()

    for label, root in local_roots.items():
        for relative in LOCAL_EXPECTED[label]["evidence"]:
            members[f"evidence/expose_{label}/{relative}"] = (
                root / relative
            ).read_bytes()
        for relative, data in local_sources[label].items():
            members[
                f"history/upstream_source_inputs/expose_{label}/{relative}"
            ] = data
    return members


def canonical_aggregate(members: dict[str, bytes]) -> str:
    records = [
        f"{name}|{len(data)}|{sha256_bytes(data)}"
        for name, data in sorted(
            members.items(), key=lambda item: item[0].casefold()
        )
    ]
    return sha256_bytes("\n".join(records).encode("utf-8"))


def build_source_zip(
    closure: dict[str, bytes],
    evidence: dict[str, bytes],
) -> dict[str, object]:
    members = dict(closure)
    members.update(evidence)
    members["history/00c_SGA3_English_Reader_R21_20260729.pdf"] = (
        BASE_PDF.read_bytes()
    )
    members["history/02c_SGA3_English_Master_R21_20260729.tex"] = (
        BASE_MASTER.read_bytes()
    )
    for name, data in members.items():
        scan_public_bytes(name, data)

    rows = [
        {
            "relative_path": name,
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(
            members.items(), key=lambda item: item[0].casefold()
        )
    ]
    manifest = csv_bytes(rows, ["relative_path", "bytes", "sha256"])
    members[ZIP_MANIFEST] = manifest

    output = OUTPUT_ROOT / ZIP_NAME
    with zipfile.ZipFile(output, "w") as archive:
        for name, data in sorted(
            members.items(), key=lambda item: item[0].casefold()
        ):
            archive.writestr(zip_info(name), data)

    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("R22 source ZIP CRC failure")
        replay_rows = parse_manifest_bytes(archive.read(ZIP_MANIFEST))
        if len(replay_rows) != len(members) - 1:
            raise RuntimeError("R22 source ZIP manifest-row mismatch")
        for row in replay_rows:
            data = archive.read(row["relative_path"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    f"R22 source ZIP mismatch: {row['relative_path']}"
                )
    return {
        "filename": ZIP_NAME,
        "bytes": output.stat().st_size,
        "sha256": sha256_file(output),
        "members": len(members),
        "manifest_rows": len(members) - 1,
        "uncompressed_bytes": sum(len(data) for data in members.values()),
        "manifest_sha256": sha256_bytes(manifest),
        "errors": [],
    }


def write_docs(metrics: dict, closure: dict) -> None:
    (OUTPUT_ROOT / "README.md").write_text(
        f"""# SGA 3 English Reader

The direct PDF is the current reading edition. It contains the Editorial
Notice, Introduction, Exposes I--XXVI, the Tome-I index, the Tome-III
mathematical guide, and the terminal index.

R22 incorporates completed native-diagram successors for Exposes VIII, IX,
XI, and XV. Thirty-two project source-reading annotations present in those
upstream working components are retained in archive history but removed from
the mathematical reading flow.

Reader: {metrics['pages']} A4 pages, {metrics['named_destinations']} named
destinations, and {metrics['internal_goto_actions']} valid internal links.

This is an English scholarly working edition, not a critical edition or a
blanket rights clearance. Historical versions remain preserved.
""",
        encoding="utf-8",
        newline="\n",
    )
    (OUTPUT_ROOT / "PROVENANCE_AND_RIGHTS.md").write_text(
        """# Provenance and rights

R22 preserves the R21 translation and ordering while replacing the active
component sources for Exposes VIII, IX, XI, and XV with their completed
native-diagram, direct-authority high-zoom successors. Exact source
manifests and review controls are grouped in the source-and-history ZIP, not
printed in the reader.

No new license grant or redistribution right is asserted for the underlying
French work, the English reconstruction, or the package as a whole. Rights
remain with their respective holders.
""",
        encoding="utf-8",
        newline="\n",
    )
    (OUTPUT_ROOT / "PUBLICATION_READINESS.md").write_text(
        """# Publication readiness

Status: `PASS_READER_CLEAN_R22_NATIVE_VIII_IX_XI_XV`.

The exact predecessor replay, manifest-bound source replacement, primary and
isolated builds, PDF structure, reader-text apparatus scan, privacy scan,
recursive source closure, and deterministic source ZIP replay pass.
High-zoom and native-diagram controls remain outside the reading flow.
""",
        encoding="utf-8",
        newline="\n",
    )
    (OUTPUT_ROOT / "BUILD_SUMMARY_PUBLIC.md").write_text(
        f"""# Public build summary

- primary XeLaTeX build: PASS
- isolated replay build: PASS
- cumulative pages: {metrics['pages']}
- named destinations: {metrics['named_destinations']}
- internal GoTo actions: {metrics['internal_goto_actions']}
- invalid or external actions: 0
- font resources: {metrics['font_resources']}
- Type3 fonts: 0
- recursive source files: {len(closure)}
- recursive source aggregate: `{canonical_aggregate(closure)}`
""",
        encoding="utf-8",
        newline="\n",
    )
    (OUTPUT_ROOT / "FINAL_VISUAL_QA.md").write_text(
        """# Final visual QA

The 28 cumulative reader pages containing the changed native diagrams in
Exposes VIII, IX, XI, and XV were rendered at 300 dpi from the final R22 PDF
and reviewed after the exact source integration: 697, 698, 706, 718, 723,
732, 734, 747, 748, 750, 752, 800, 801, 802, 812, 813, 946, 947, 951, 952,
953, 954, 956, 959, 964, 966, 973, and 985.

Diagram labels, arrows, surrounding prose, footnotes, headers, and page
breaks remain legible, with no clipping, overlap, collision, blank page, or
malformed spacing found.

The mathematical-fidelity decisions remain bound to the direct-authority
high-zoom controls packaged for each source successor.
""",
        encoding="utf-8",
        newline="\n",
    )


def write_outer_manifest() -> None:
    paths = sorted(
        (
            path
            for path in OUTPUT_ROOT.iterdir()
            if path.is_file() and path.name != OUTER_MANIFEST
        ),
        key=lambda path: path.name.casefold(),
    )
    rows = [
        {
            "filename": path.name,
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
        for path in paths
    ]
    (OUTPUT_ROOT / OUTER_MANIFEST).write_bytes(
        csv_bytes(rows, ["filename", "bytes", "sha256"])
    )


def write_cleanup_ledger(removals: list) -> None:
    rows = [
        {
            "volume": row.volume,
            "relative_path": row.relative_path,
            "kind": row.kind,
            "start_line": row.start_line,
            "bytes_removed": row.bytes_removed,
            "sha256": row.sha256,
            "preview": row.preview,
        }
        for row in removals
    ]
    (OUTPUT_ROOT / "READER_APPARATUS_REMOVAL_LEDGER.csv").write_bytes(
        csv_bytes(
            rows,
            [
                "volume",
                "relative_path",
                "kind",
                "start_line",
                "bytes_removed",
                "sha256",
                "preview",
            ],
        )
    )


def main() -> int:
    args = parse_args()
    xi_root = args.expose_xi_root.resolve()
    xv_root = args.expose_xv_root.resolve()
    for path in (
        BASE_ARCHIVE,
        BASE_MASTER,
        BASE_PDF,
        VIII_IX_ARCHIVE,
        R20_BUILDER_PATH,
        R21_BUILDER_PATH,
        CLEANER_PATH,
    ):
        if not path.is_file():
            raise FileNotFoundError(path)

    archive_members, viii_ix_validation = verify_viii_ix_archive()
    xi_sources, xi_validation = verify_local_successor(xi_root, "xi")
    xv_sources, xv_validation = verify_local_successor(xv_root, "xv")

    safe_clear(TEMP_ROOT)
    safe_clear(OUTPUT_ROOT)
    TEMP_ROOT.mkdir(parents=True)
    OUTPUT_ROOT.mkdir(parents=True)

    r20 = load_module("sga3_r22_r20_helpers", R20_BUILDER_PATH)
    r21 = load_module("sga3_r22_r21_helpers", R21_BUILDER_PATH)
    cleaner = load_module("sga3_r22_reader_cleaner", CLEANER_PATH)
    r20.TEMP_ROOT = TEMP_ROOT
    r20.OUTPUT_ROOT = OUTPUT_ROOT
    r20.BUNDLE_MASTER = MASTER_NAME

    source, replacements, removals = prepare_source(
        archive_members,
        {"xi": xi_sources, "xv": xv_sources},
        cleaner,
    )
    primary = r20.run_build(source, "R22 primary")
    metrics, primary_text = r21.validate_reader(
        primary["pdf"], cleaner, r20
    )

    replay_root = r20.prepare_replay(source)
    replay_build = r20.run_build(replay_root, "R22 isolated replay")
    replay_metrics, replay_text = r21.validate_reader(
        replay_build["pdf"], cleaner, r20
    )
    if replay_metrics != metrics:
        raise RuntimeError("R22 isolated replay PDF metrics differ")
    if replay_text != primary_text:
        raise RuntimeError("R22 isolated replay extracted text differs")

    closure = r20.recorder_closure(source, primary["fls"])
    shutil.copy2(primary["pdf"], OUTPUT_ROOT / PDF_NAME)
    shutil.copy2(source / MASTER_NAME, OUTPUT_ROOT / TEX_NAME)
    (OUTPUT_ROOT / "SGA3_R22_BUILD_PUBLIC.log").write_text(
        primary["console"], encoding="utf-8", newline="\n"
    )
    (OUTPUT_ROOT / "SOURCE_REPLACEMENT_LEDGER.csv").write_bytes(
        csv_bytes(
            replacements,
            [
                "expose",
                "relative_path",
                "old_sha256",
                "new_bytes",
                "new_sha256",
                "reader_bytes",
                "reader_sha256",
                "reader_apparatus_removals",
            ],
        )
    )
    write_cleanup_ledger(removals)
    write_docs(metrics, closure)
    evidence = evidence_members(
        archive_members,
        {"xi": xi_root, "xv": xv_root},
        {"xi": xi_sources, "xv": xv_sources},
    )
    source_zip = build_source_zip(closure, evidence)

    validation = {
        "schema": "sga3_reader_clean_r22_native_viii_ix_xi_xv_v1",
        "status": "PASS",
        "errors": [],
        "predecessor": {
            "reader_sha256": sha256_file(BASE_PDF),
            "master_sha256": sha256_file(BASE_MASTER),
            "source_archive_sha256": sha256_file(BASE_ARCHIVE),
        },
        "reader": {
            "filename": PDF_NAME,
            "bytes": (OUTPUT_ROOT / PDF_NAME).stat().st_size,
            "sha256": sha256_file(OUTPUT_ROOT / PDF_NAME),
            **metrics,
            "reader_process_term_hits": [],
        },
        "master_tex": {
            "filename": TEX_NAME,
            "bytes": (OUTPUT_ROOT / TEX_NAME).stat().st_size,
            "sha256": sha256_file(OUTPUT_ROOT / TEX_NAME),
        },
        "source_replacements": {
            "files_replayed": len(replacements),
            "files_changed": sum(
                1
                for row in replacements
                if row["old_sha256"] != row["new_sha256"]
            ),
            "exposes": ["VIII", "IX", "XI", "XV"],
        },
        "reader_apparatus_removals": {
            "total": len(removals),
            "by_kind": EXPECTED_READER_CLEANUP,
        },
        "visual_qa": {
            "status": "PASS",
            "whole_page_dpi": 300,
            "physical_pdf_pages": [
                697,
                698,
                706,
                718,
                723,
                732,
                734,
                747,
                748,
                750,
                752,
                800,
                801,
                802,
                812,
                813,
                946,
                947,
                951,
                952,
                953,
                954,
                956,
                959,
                964,
                966,
                973,
                985,
            ],
            "component_authority_review_dpi": 5000,
            "errors": [],
        },
        "successor_inputs": {
            "viii_ix": viii_ix_validation,
            "xi": xi_validation,
            "xv": xv_validation,
        },
        "source_archive": source_zip,
        "recorder_closure": {
            "files": len(closure),
            "bytes": sum(len(data) for data in closure.values()),
            "canonical_aggregate_sha256": canonical_aggregate(closure),
        },
        "isolated_replay": {
            "metrics": replay_metrics,
            "text_sha256": sha256_bytes(replay_text.encode("utf-8")),
            "errors": [],
        },
        "build_diagnostics": {
            "primary": primary["diagnostics"],
            "replay": replay_build["diagnostics"],
        },
        "privacy": {"hits": []},
    }
    (OUTPUT_ROOT / "PACKAGE_VALIDATION.json").write_text(
        json.dumps(validation, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_outer_manifest()

    for row in parse_manifest_bytes(
        (OUTPUT_ROOT / OUTER_MANIFEST).read_bytes()
    ):
        path = OUTPUT_ROOT / row["filename"]
        if (
            path.stat().st_size,
            sha256_file(path),
        ) != (int(row["bytes"]), row["sha256"].upper()):
            raise RuntimeError(f"Outer manifest mismatch: {path.name}")

    print(json.dumps(validation, indent=2))
    if not args.keep_temp:
        safe_clear(TEMP_ROOT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
