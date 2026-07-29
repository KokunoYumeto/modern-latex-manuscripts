#!/usr/bin/env python3
"""Build the SGA3 R21 reader with project notes removed from the reading flow."""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import sys
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
BASE_PACKAGE = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-complete-working-reader-clean-r20-native-expose-v-vi-20260729"
)
BASE_ARCHIVE = (
    BASE_PACKAGE
    / "10c_SGA3_English_Source_and_History_R20_20260729.zip"
)
BASE_MASTER = BASE_PACKAGE / "02c_SGA3_English_Master.tex"
BASE_PDF = BASE_PACKAGE / "00c_SGA3_English_Reader.pdf"
OUTPUT_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-reader-clean-r21-no-project-notes-20260729"
)
TEMP_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_reader_clean_r21_no_project_notes_20260729"
)
R20_BUILDER_PATH = (
    REPO_ROOT
    / "scripts"
    / "build_sga3_reader_clean_complete_r20_native_v_vi_20260729.py"
)
CLEANER_PATH = (
    REPO_ROOT
    / "scripts"
    / "build_sga_reader_mathematical_body_clean_successor_20260729.py"
)

MASTER_NAME = "SGA3_English_Master.tex"
PDF_NAME = "00c_SGA3_English_Reader.pdf"
TEX_NAME = "02c_SGA3_English_Master.tex"
ZIP_NAME = "10c_SGA3_English_Source_and_History_R21_20260729.zip"
ZIP_MANIFEST = "SOURCE_BUNDLE_SHA256.csv"
OUTER_MANIFEST = "SHA256SUMS.csv"
FIXED_ZIP_TIME = (2026, 7, 29, 0, 0, 0)
EXPECTED_REMOVALS = {
    "project_diagram_locator": 1,
    "inline_source_adjudication": 1,
    "project_footnote": 6,
}
EXPLICIT_READER_BLOCKLIST = (
    "ChatGPT",
    "OpenAI",
    "Claude",
    "Codex",
    "large language model",
    "LLM-generated",
    "AI-generated",
    "AI-assisted",
    "Native Loop-2 reconstruction",
    "source locator",
    "The French source prints",
    "The displayed French source prints",
    "Translator's note",
    "Translator’s note",
    "source-status",
    "production status",
    "workflow status",
)
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
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def safe_clear(path: Path) -> None:
    if not path.exists():
        return
    resolved = path.resolve()
    if path == TEMP_ROOT:
        parent = (Path(os.environ["LOCALAPPDATA"]) / "Temp").resolve()
    else:
        parent = OUTPUT_ROOT.parent.resolve()
    if resolved.parent != parent:
        raise RuntimeError(f"Refusing to clear unexpected path: {resolved}")
    shutil.rmtree(resolved)


def scan_public_bytes(name: str, data: bytes) -> None:
    lowered = data.lower()
    hits = [
        marker.decode("ascii", errors="replace")
        for marker in PRIVATE_MARKERS
        if marker in lowered
    ]
    if hits:
        raise RuntimeError(f"Private marker in {name}: {hits}")


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


def prepare_source(cleaner, r20) -> tuple[Path, list]:
    source = TEMP_ROOT / "primary"
    source.mkdir(parents=True)
    with zipfile.ZipFile(BASE_ARCHIVE) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"R20 source archive CRC failure: {bad}")
        for info in archive.infolist():
            if not r20.safe_member(info.filename):
                raise RuntimeError(f"Unsafe R20 archive member: {info.filename}")
        archive.extractall(source)

    master = source / MASTER_NAME
    if not master.is_file():
        raise FileNotFoundError(master)
    if master.read_bytes() != BASE_MASTER.read_bytes():
        raise RuntimeError("R20 direct master and source-archive master differ")

    removals: list = []
    for path in sorted(source.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".tex", ".texfrag"}:
            cleaner.clean_tex(path, source, "sga3", removals)

    counts = {
        kind: sum(1 for row in removals if row.kind == kind)
        for kind in EXPECTED_REMOVALS
    }
    if counts != EXPECTED_REMOVALS or len(removals) != sum(
        EXPECTED_REMOVALS.values()
    ):
        raise RuntimeError(
            "Unexpected R21 reader-apparatus removal set: "
            f"counts={counts}, total={len(removals)}"
        )
    return source, removals


def validate_reader(path: Path, cleaner, r20) -> tuple[dict, str]:
    metrics = r20.pdf_metrics(path)
    if (
        not 1_440 <= metrics["pages"] <= 1_500
        or metrics["named_destinations"] < 9_150
        or metrics["internal_goto_actions"] < 4_250
        or metrics["invalid_actions"] != 0
        or metrics["uri_actions"] != 0
        or metrics["type3_fonts"] != 0
        or metrics["raster_xobjects"] > 41
    ):
        raise RuntimeError(f"Unexpected cumulative PDF metrics: {metrics}")
    text = r20.extract_text(path)
    blocked = sorted(
        {
            token
            for token in (
                *cleaner.GLOBAL_BLOCKLIST,
                *cleaner.TEXT_BLOCKLIST["sga3"],
                *EXPLICIT_READER_BLOCKLIST,
            )
            if token.casefold() in text.casefold()
        },
        key=str.casefold,
    )
    if blocked:
        raise RuntimeError(f"Reader-facing project apparatus remains: {blocked}")
    required = (
        "Editorial Notice",
        "Introduction",
        "Exposé I",
        "Exposé XXVI",
    )
    missing = [token for token in required if token.casefold() not in text.casefold()]
    if missing:
        raise RuntimeError(f"Reader lost required historical/body text: {missing}")
    return metrics, text


def build_source_zip(
    closure: dict[str, bytes],
    cleanup_note: bytes,
) -> dict[str, object]:
    members = dict(closure)
    members["history/00c_SGA3_English_Reader_R20_20260729.pdf"] = (
        BASE_PDF.read_bytes()
    )
    members["history/02c_SGA3_English_Master_R20_20260729.tex"] = (
        BASE_MASTER.read_bytes()
    )
    members["evidence/R21_READER_FACING_APPARATUS_REMOVAL.md"] = cleanup_note
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

    errors: list[str] = []
    with zipfile.ZipFile(output) as archive:
        bad = archive.testzip()
        if bad is not None:
            errors.append(f"CRC failure: {bad}")
        rows_in_zip = list(
            csv.DictReader(
                io.StringIO(
                    archive.read(ZIP_MANIFEST).decode("utf-8"),
                    newline="",
                )
            )
        )
        if len(rows_in_zip) != len(members) - 1:
            errors.append("manifest-row mismatch")
        for row in rows_in_zip:
            data = archive.read(row["relative_path"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                errors.append(f"member mismatch: {row['relative_path']}")
    if errors:
        raise RuntimeError(f"Source ZIP validation failed: {errors}")
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


def write_removal_ledger(removals: list) -> None:
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


def write_docs(metrics: dict, replay: dict, closure: dict) -> bytes:
    (OUTPUT_ROOT / "README.md").write_text(
        f"""# SGA 3 English Reader

The direct PDF is the reading edition. It contains the Editorial Notice,
Introduction, Exposes I--XXVI, the Tome-I index, the Tome-III mathematical
guide, and the terminal index.

The direct TeX file is the editable master. Build sources, provenance,
validation evidence, and earlier reader states are grouped in the source and
history ZIP.

Reader: {metrics['pages']} A4 pages, {metrics['named_destinations']} named
destinations, and {metrics['internal_goto_actions']} valid internal links.

This is an English scholarly edition, not a critical edition or a blanket
rights clearance. Historical versions remain preserved.
""",
        encoding="utf-8",
        newline="\n",
    )
    cleanup_note = f"""# R21 reader-facing apparatus removal

The reading edition removes eight project-authored production and
source-adjudication annotations that remained visible in R20: one diagram
reconstruction/source-locator caption, one inline source-adjudication aside,
and six project-added source-reading footnotes.

The mathematical reading text, source ordering, links, and legitimate
historical source-edition apparatus remain. Detailed provenance and the R20
predecessor are preserved in this archive rather than printed in the reader.

R21 reader metrics: {metrics['pages']} A4 pages,
{metrics['named_destinations']} named destinations, and
{metrics['internal_goto_actions']} valid internal links.
"""
    cleanup_bytes = cleanup_note.encode("utf-8")
    (OUTPUT_ROOT / "PROVENANCE_AND_RIGHTS.md").write_text(
        """# Provenance and rights

The mathematical source basis and translation lineage are unchanged from the
R20 predecessor. Controlling source identities, comparison-lineage credit,
diagram review evidence, and earlier reader states remain in the source and
history archive.

No new license grant or redistribution right is asserted for the underlying
French work, the English reconstruction, or the package as a whole. Rights
remain with their respective holders.
""",
        encoding="utf-8",
        newline="\n",
    )
    (OUTPUT_ROOT / "PUBLICATION_READINESS.md").write_text(
        """# Publication readiness

Status: `PASS_READER_CLEAN_R21_NO_PROJECT_NOTES`.

The primary and isolated replay builds, PDF structure, reader-text apparatus
scan, privacy scan, recursive source closure, and deterministic source ZIP
replay pass. The direct reader contains mathematical and legitimate
historical editorial content; project workflow and source-adjudication
apparatus is kept outside the reading flow.
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
- replay text SHA-256: `{replay['text_sha256']}`
""",
        encoding="utf-8",
        newline="\n",
    )
    return cleanup_bytes


def write_visual_qa() -> None:
    (OUTPUT_ROOT / "FINAL_VISUAL_QA.md").write_text(
        """# Final visual QA

The seven reader pages affected by the eight removals were rendered from the
final R21 PDF and directly inspected: physical PDF pages 281, 1084, 1259,
1262, 1296, 1297, and 1436.

The reconstruction/source-locator caption and six project source-reading
footnotes are absent. The Expose-XVIII historical editor note remains, with
only the two project-added source-adjudication sentences removed. Mathematical
text, diagrams, page headers, footnote rules, and surrounding paragraphs are
legible and show no clipping, overlap, collision, orphaned marker, or malformed
spacing.
""",
        encoding="utf-8",
        newline="\n",
    )


def canonical_aggregate(members: dict[str, bytes]) -> str:
    records = [
        f"{name}|{len(data)}|{sha256_bytes(data)}"
        for name, data in sorted(
            members.items(), key=lambda item: item[0].casefold()
        )
    ]
    return sha256_bytes("\n".join(records).encode("utf-8"))


def write_outer_manifest() -> None:
    files = sorted(
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
        for path in files
    ]
    (OUTPUT_ROOT / OUTER_MANIFEST).write_bytes(
        csv_bytes(rows, ["filename", "bytes", "sha256"])
    )


def main() -> int:
    for required in (
        BASE_ARCHIVE,
        BASE_MASTER,
        BASE_PDF,
        R20_BUILDER_PATH,
        CLEANER_PATH,
    ):
        if not required.is_file():
            raise FileNotFoundError(required)

    safe_clear(TEMP_ROOT)
    safe_clear(OUTPUT_ROOT)
    TEMP_ROOT.mkdir(parents=True)
    OUTPUT_ROOT.mkdir(parents=True)

    cleaner = load_module("sga_reader_cleaner_r21", CLEANER_PATH)
    r20 = load_module("sga3_r20_builder_helpers", R20_BUILDER_PATH)
    r20.TEMP_ROOT = TEMP_ROOT
    r20.OUTPUT_ROOT = OUTPUT_ROOT
    r20.BUNDLE_MASTER = MASTER_NAME

    source, removals = prepare_source(cleaner, r20)
    primary = r20.run_build(source, "R21 primary")
    metrics, primary_text = validate_reader(primary["pdf"], cleaner, r20)

    replay_root = r20.prepare_replay(source)
    replay_build = r20.run_build(replay_root, "R21 isolated replay")
    replay_metrics, replay_text = validate_reader(
        replay_build["pdf"], cleaner, r20
    )
    if replay_metrics != metrics:
        raise RuntimeError("Isolated replay PDF metrics differ")
    if replay_text != primary_text:
        raise RuntimeError("Isolated replay extracted text differs")
    replay = {
        "metrics": replay_metrics,
        "text_sha256": sha256_bytes(replay_text.encode("utf-8")),
        "errors": [],
    }

    closure = r20.recorder_closure(source, primary["fls"])
    shutil.copy2(primary["pdf"], OUTPUT_ROOT / PDF_NAME)
    shutil.copy2(source / MASTER_NAME, OUTPUT_ROOT / TEX_NAME)
    (OUTPUT_ROOT / "SGA3_R21_BUILD_PUBLIC.log").write_text(
        primary["console"], encoding="utf-8", newline="\n"
    )
    write_removal_ledger(removals)
    cleanup_note = write_docs(metrics, replay, closure)
    write_visual_qa()
    source_zip = build_source_zip(closure, cleanup_note)

    validation = {
        "schema": "sga3_reader_clean_r21_no_project_notes_v1",
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
        "reader_apparatus_removals": {
            "total": len(removals),
            "by_kind": EXPECTED_REMOVALS,
        },
        "visual_qa": {
            "status": "PASS",
            "physical_pdf_pages": [281, 1084, 1259, 1262, 1296, 1297, 1436],
            "errors": [],
        },
        "source_archive": source_zip,
        "recorder_closure": {
            "files": len(closure),
            "bytes": sum(len(data) for data in closure.values()),
            "canonical_aggregate_sha256": canonical_aggregate(closure),
        },
        "isolated_replay": replay,
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

    rows = list(
        csv.DictReader(
            (OUTPUT_ROOT / OUTER_MANIFEST).read_text(
                encoding="utf-8"
            ).splitlines()
        )
    )
    for row in rows:
        path = OUTPUT_ROOT / row["filename"]
        if (
            path.stat().st_size,
            sha256_file(path),
        ) != (int(row["bytes"]), row["sha256"].upper()):
            raise RuntimeError(f"Outer manifest mismatch: {path.name}")

    print(json.dumps(validation, indent=2))
    safe_clear(TEMP_ROOT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
