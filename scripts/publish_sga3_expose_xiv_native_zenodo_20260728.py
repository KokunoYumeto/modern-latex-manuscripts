#!/usr/bin/env python3
"""Publish the bounded native-diagram SGA3 Expose XIV checkpoint."""

from __future__ import annotations

import csv
import importlib.util
import io
import json
import os
import re
import shutil
import zipfile
from pathlib import Path, PurePosixPath


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = SCRIPT_DIR / "publish_sga3_cumulative_with_x_zenodo_20260728.py"
SPEC = importlib.util.spec_from_file_location("sga_successor_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA successor workflow")
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)


PREDECESSOR_RECORD = 21639117
PREDECESSOR_DOI = "10.5281/zenodo.21639117"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-28"
VERSION = "2026-07-28 SGA3 Expose XIV native-diagram Loop1 checkpoint"
GITHUB_COMMIT = "5539787a3186d9fea5285061704603b96d726568"
GITHUB_PACKAGE = (
    "sources/sga/sga3-expose-xiv-native-loop1-working-20260728"
)

NEW_PDF = (
    "00c14_SGA3_Expose_XIV_English_NativeDiagram_"
    "Loop1_Working_20260728.pdf"
)
NEW_TEX = (
    "02c14_SGA3_Expose_XIV_English_NativeDiagram_"
    "Loop1_Working_20260728.tex"
)
NEW_SOURCE_ZIP = (
    "10c14_SGA3_Expose_XIV_NativeDiagram_Loop1_Source_20260728.zip"
)
README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
REPLACED_NAMES = {README_NAME, MANIFEST_NAME, VALIDATION_NAME}

EXPECTED_PREDECESSOR_FILES = 70
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 68
EXPECTED_FINAL_FILES = 73
EXPECTED_RETAINED_PREDECESSOR_FILES = 67
EXPECTED_UNRELATED_RETAINED_FILES = 67
EXPECTED_MANIFEST_ROWS = 71
EXPECTED_ZIP_ARCHIVES = 50
EXPECTED_ZIP_FILE_MEMBERS = 4_464
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_470
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 418_837_501

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-expose-xiv-native-loop1-working-20260728"
)
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21639117_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_expose_xiv_native_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_expose_xiv_native_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_sga3_expose_xiv_native_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    NEW_PDF: PACKAGE_ROOT / NEW_PDF,
    NEW_TEX: PACKAGE_ROOT / NEW_TEX,
    NEW_SOURCE_ZIP: PACKAGE_ROOT / NEW_SOURCE_ZIP,
}
PRIMARY_EXPECTED = {
    NEW_PDF: (
        240_676,
        "6CD0B985FE2F4D0C69A52ACCD0E766F3029B3E8E6A40AEB31B9E511C40E72EA0",
    ),
    NEW_TEX: (
        3_301,
        "59D9FDB32AA981891BD807EF419D201C74A941E75A1FBAFA21F09C4C874CC9C1",
    ),
    NEW_SOURCE_ZIP: (
        70_074,
        "6739C9F69E09EF6BDE0995F38859DB745EEC1FA61158720057DA81B677C5C38B",
    ),
}

NEW_MANIFEST_ROWS = {
    NEW_PDF: {
        "role": "english_reader",
        "provenance": (
            "complete bounded SGA3 Expose XIV Loop1 working reader with "
            "native diagrams; GitHub commit " + GITHUB_COMMIT
        ),
        "status": (
            "bounded_complete_expose_xiv_working_reader_"
            "not_complete_sga3_not_reference_v2_certified"
        ),
    },
    NEW_TEX: {
        "role": "english_master_tex",
        "provenance": (
            "direct editable master for the bounded SGA3 Expose XIV "
            "working reader; GitHub commit " + GITHUB_COMMIT
        ),
        "status": "bounded_working_source_native_diagrams_no_raster",
    },
    NEW_SOURCE_ZIP: {
        "role": "grouped_source_and_qa",
        "provenance": (
            "42-member privacy-clean editable source and QA closure; "
            "GitHub commit " + GITHUB_COMMIT
        ),
        "status": (
            "bounded_source_qa_no_authority_pixels_no_raster_diagram_"
            "not_rights_clearance"
        ),
    },
    README_NAME: {
        "role": "manifest_status",
        "provenance": (
            "current compact same-concept release note; GitHub commit "
            + GITHUB_COMMIT
        ),
        "status": "current_release_control",
    },
}

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept compact successor preserves 67 files from version "
        "10.5281/zenodo.21639117 byte-identically, refreshes the three release "
        "controls, and adds a bounded SGA3 Expose XIV working checkpoint as "
        "a direct reader, direct editable master TeX, and grouped source/QA ZIP. "
        "SGA1 remains the default preview."
    ),
    (
        "The new 37-page A4 reader covers complete Expose XIV only: "
        "Polo-Gille authority local pages 1-36 / combined-reader pages "
        "835-870, with a hard stop before Expose XV local page 1 / "
        "combined-reader page 871. It has 236 named destinations, 24 valid "
        "internal GoTo actions, zero invalid or external actions, 32 font "
        "resources, no Type3 fonts, and no raster XObjects."
    ),
    (
        "The complete editable closure has 33 TeX files. The four "
        "Dynkin-automorphism rows that were previously delivered as one raster "
        "block are now one native TikZ picture, with zero includegraphics calls. "
        "The top-level Session-C lead compared all four authority and delivered "
        "rows at 5000 dpi and signed the included review receipt. Existing 600- "
        "and 1200-dpi evidence remains legitimate context history. No authority "
        "pixels, high-resolution crops, or raster diagram are redistributed."
    ),
    (
        "Three producer and three independent archive XeLaTeX passes completed. "
        "The "
        "producer and independent outputs match on all 37 extracted-text pages, "
        "all 37 decoded page-content streams, page geometry, destinations, "
        "links, and normalized font resources. All 37 producer/rebuild 180-dpi "
        "render pairs are byte-identical and all pages were visually reviewed."
    ),
    (
        "The existing 1,182-page SGA3 current-progress cumulative reader remains "
        "directly available as readable history, but it is not reissued here: "
        "its older raster-bearing components do not satisfy the current native-"
        "diagram delivery rule. The new standalone XIV checkpoint preserves one "
        "reading gap without claiming that the cumulative file, SGA3 as a "
        "whole, or every earlier diagram is finally certified."
    ),
    (
        "The controlling witness is Polo-Gille Expo14.pdf, 36 pages, "
        "SHA-256 467F03717A06F85DB3C1CAFB1D35E8A1E07247372717B94CD6E19F1EB114FEA1. "
        "It is not redistributed. Floris's pre-existing GPU OCR was consulted "
        "read-only as locator or drafting evidence and was not regenerated. "
        "Jacob C. Reinhold's jcreinhold/sga English lineage at revision "
        "e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e is credited comparison "
        "material, not source authority; its stated CC BY 4.0 applies only to "
        "that contribution."
    ),
    (
        "This package is a bounded scholarly working reader, not complete SGA3, "
        "a critical edition, exhaustive reference-v2 certification, rights "
        "clearance, mathematical certification, peer review, or tagged-PDF "
        "accessibility remediation. No blanket license or transfer of "
        "underlying rights is asserted. Machine-assisted contributors include "
        "OpenAI Codex / ChatGPT and Anthropic Claude under human direction."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_HTML = (
    "<p>Compact reader-first SGA surface with 73 public files. The bounded "
    "Expose XIV PDF and master TeX are direct; its 42-member editable "
    "source/QA closure is grouped in one ZIP. The existing cumulative SGA3 "
    "working reader remains visible history and is not represented as native-"
    "diagram-final. GitHub custody commit: "
    f"{GITHUB_COMMIT}.</p>"
)


def safe_member(name: str) -> None:
    pure = PurePosixPath(name)
    if (
        pure.is_absolute()
        or ".." in pure.parts
        or "\\" in name
        or re.match(r"^[A-Za-z]:", name)
    ):
        raise RuntimeError(f"Unsafe ZIP member: {name}")


def verify_primary_local_files() -> dict[str, dict]:
    result: dict[str, dict] = {}
    for name, path in PRIMARY_LOCAL_PATHS.items():
        if not path.is_file():
            raise FileNotFoundError(path)
        identity = {
            "path": path,
            "bytes": path.stat().st_size,
            "sha256": base.sha256_file(path),
            "md5": base.md5_file(path),
        }
        if (identity["bytes"], identity["sha256"]) != PRIMARY_EXPECTED[name]:
            raise RuntimeError(f"Primary local identity mismatch: {name}")
        result[name] = identity

    outer_manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    if base.sha256_file(outer_manifest) != (
        "A263A28D4C98384756256C071BFE553C7969198F8BB75D494C4B5C2DB54113F1"
    ):
        raise RuntimeError("Outer package manifest identity mismatch")
    rows = list(
        csv.DictReader(
            io.StringIO(outer_manifest.read_text(encoding="utf-8-sig"))
        )
    )
    expected_outer = {
        path.name
        for path in PACKAGE_ROOT.iterdir()
        if path.is_file() and path.name != outer_manifest.name
    }
    if len(rows) != 12 or {row["filename"] for row in rows} != expected_outer:
        raise RuntimeError("Outer package manifest exact-set mismatch")
    for row in rows:
        path = PACKAGE_ROOT / row["filename"]
        if (path.stat().st_size, base.sha256_file(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(
                f"Outer package manifest identity mismatch: {row['filename']}"
            )

    package_validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    if (
        package_validation.get("status") != "PASS"
        or package_validation.get("errors") != []
        or package_validation.get("privacy", {}).get("hits") != []
        or package_validation.get("reader", {}).get("raster_xobjects") != 0
    ):
        raise RuntimeError("Local package validation is not controlling PASS")

    zip_path = PRIMARY_LOCAL_PATHS[NEW_SOURCE_ZIP]
    with zipfile.ZipFile(zip_path, "r") as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"Source ZIP CRC failure: {bad}")
        names = archive.namelist()
        if len(names) != 42 or len(names) != len(set(names)):
            raise RuntimeError("Source ZIP member boundary mismatch")
        for name in names:
            safe_member(name)
        if sum(info.file_size for info in archive.infolist()) != 149_081:
            raise RuntimeError("Source ZIP uncompressed-byte mismatch")
        forbidden = {
            ".png",
            ".jpg",
            ".jpeg",
            ".tif",
            ".tiff",
            ".bmp",
            ".gif",
            ".webp",
            ".pdf",
        }
        raster_members = [
            name
            for name in names
            if PurePosixPath(name).suffix.lower() in forbidden
        ]
        if raster_members:
            raise RuntimeError(
                f"Source ZIP contains raster or PDF witness: {raster_members}"
            )
        source_rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read("SOURCE_SHA256SUMS.csv").decode("utf-8-sig")
                )
            )
        )
        expected_source = set(names) - {
            "SOURCE_SHA256SUMS.csv",
            "SOURCE_PACKAGE_VALIDATION.json",
        }
        if (
            len(source_rows) != 40
            or {row["relative_path"] for row in source_rows}
            != expected_source
        ):
            raise RuntimeError("Source ZIP internal manifest exact-set mismatch")
        for row in source_rows:
            data = archive.read(row["relative_path"])
            if (len(data), base.hashlib.sha256(data).hexdigest().upper()) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    "Source ZIP internal manifest mismatch: "
                    f"{row['relative_path']}"
                )
        source_validation = json.loads(
            archive.read("SOURCE_PACKAGE_VALIDATION.json")
        )
        if (
            source_validation.get("status") != "PASS"
            or source_validation.get("errors") != []
        ):
            raise RuntimeError("Source ZIP validation is not PASS")
        tex = "\n".join(
            archive.read(name).decode("utf-8")
            for name in names
            if name.lower().endswith(".tex")
        )
        if (
            tex.count(r"\begin{tikzcd}") != 0
            or tex.count(r"\begin{tikzpicture}") != 1
            or r"\includegraphics" in tex
        ):
            raise RuntimeError("Native-diagram/raster source boundary mismatch")
    return result


def fetch_predecessor_manifest(
    session, predecessor: dict, receipt: dict
) -> list[dict[str, str]]:
    entry = base.entries_map(predecessor)[MANIFEST_NAME]
    response = base.check(
        session.get(entry["links"]["content"], timeout=(30, 180)),
        {200},
    )
    content = response.content
    wanted = receipt["files"][MANIFEST_NAME]
    if (
        len(content),
        base.hashlib.sha256(content).hexdigest().upper(),
    ) != (
        int(wanted["bytes"]),
        wanted["sha256"].upper(),
    ):
        raise RuntimeError("Predecessor release-manifest readback mismatch")
    rows = list(
        csv.DictReader(io.StringIO(content.decode("utf-8-sig"), newline=""))
    )
    if len(rows) != EXPECTED_PREDECESSOR_MANIFEST_ROWS:
        raise RuntimeError("Unexpected predecessor release-manifest row count")
    return rows


def readme_text(draft_id: int) -> str:
    return f"""# Current compact SGA release

This is one same-concept successor to Zenodo record {PREDECESSOR_RECORD}. It
retains 67 predecessor files byte-identically, refreshes three release
controls, and adds the bounded SGA3 Expose XIV reader, master TeX, and
source/QA ZIP. The reserved successor record is {draft_id}. SGA1 remains the
default preview.

## New bounded SGA3 Expose XIV reader

`{NEW_PDF}` is a complete 37-page working reader for Expose XIV only:

- Polo-Gille authority local pages 1-36 / combined-reader pages 835-870;
- hard stop before Expose XV local page 1 / combined page 871;
- 33 editable TeX files;
- one native TikZ picture containing four replacement diagram rows;
- zero raster inclusions;
- 236 named destinations and 24 valid internal GoTo actions;
- zero invalid or URI actions; and
- 32 font resources with no Type3 fonts.

Three producer and three independent archive XeLaTeX passes completed. All 37
extracted-text pages, decoded page-content streams, page boxes, destinations,
links, fonts, and 180-dpi render pairs match.

The four Dynkin-automorphism rows previously delivered as a single raster
block were rebuilt in native TikZ. The top-level Session-C lead compared all
four authority and delivered rows at 5000 dpi and signed the included review
receipt. Existing 600/1200-dpi evidence remains valid context history. No
authority pixels, crops, or raster diagram are redistributed.

## Current-progress boundary

The existing 1,182-page SGA3 cumulative working reader remains directly
available as readable history. It is not reissued here because older
raster-bearing components do not satisfy the current native-diagram delivery
rule. The direct XIV checkpoint preserves useful completed work without claiming
complete SGA3 or final certification of every earlier component.

This release is not a critical edition, exhaustive reference-v2
certification, rights clearance, mathematical certification, peer review, or
tagged-PDF accessibility remediation.

## Authority, rights, and lineage

Polo-Gille `Expo14.pdf`, 36 pages, SHA-256
`467F03717A06F85DB3C1CAFB1D35E8A1E07247372717B94CD6E19F1EB114FEA1`,
controls. It is not redistributed. Floris's pre-existing GPU OCR was
consulted read-only as locator or drafting material and was not regenerated.
Jacob C. Reinhold's `jcreinhold/sga` English lineage at commit
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison
material, not authority; its stated CC BY 4.0 applies only to that
contribution. No blanket license or transfer of underlying rights is
asserted.

Machine-assisted contributors include OpenAI Codex / ChatGPT and Anthropic
Claude under human direction. GitHub custody:

`https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/{GITHUB_COMMIT}/{GITHUB_PACKAGE}`
"""


def generate_controls(
    draft_id: int,
    predecessor_rows: list[dict[str, str]],
    predecessor_identities: dict[str, dict],
    primary_local: dict[str, dict],
) -> dict[str, dict]:
    if CONTROLS_ROOT.exists():
        resolved = CONTROLS_ROOT.resolve()
        temp_root = Path(os.environ["LOCALAPPDATA"]).resolve() / "Temp"
        if temp_root not in resolved.parents:
            raise RuntimeError("Refusing to replace controls outside local temp")
        shutil.rmtree(CONTROLS_ROOT)
    CONTROLS_ROOT.mkdir(parents=True)

    readme_path = CONTROLS_ROOT / README_NAME
    base.write_text(readme_path, readme_text(draft_id))
    readme_identity = {
        "path": readme_path,
        "bytes": readme_path.stat().st_size,
        "sha256": base.sha256_file(readme_path),
        "md5": base.md5_file(readme_path),
    }

    release_rows: list[dict[str, str]] = []
    for row in predecessor_rows:
        name = row["filename"]
        if name == README_NAME:
            continue
        if name in REPLACED_NAMES:
            raise RuntimeError(f"Unexpected replaced control row: {name}")
        identity = predecessor_identities[name]
        if (int(row["bytes"]), row["sha256"].upper()) != (
            identity["bytes"],
            identity["sha256"],
        ):
            raise RuntimeError(f"Retained manifest identity mismatch: {name}")
        release_rows.append(dict(row))

    new_local = dict(primary_local)
    new_local[README_NAME] = readme_identity
    for name in sorted(new_local, key=str.casefold):
        metadata = NEW_MANIFEST_ROWS[name]
        identity = new_local[name]
        release_rows.append(
            {
                "filename": name,
                "bytes": str(identity["bytes"]),
                "sha256": identity["sha256"],
                "role": metadata["role"],
                "provenance": metadata["provenance"],
                "status": metadata["status"],
            }
        )
    release_rows.sort(key=lambda row: row["filename"].casefold())
    if len(release_rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError(
            f"Expected {EXPECTED_MANIFEST_ROWS} rows, got {len(release_rows)}"
        )
    if len({row["filename"] for row in release_rows}) != len(release_rows):
        raise RuntimeError("Generated release manifest has duplicate filenames")

    manifest_path = CONTROLS_ROOT / MANIFEST_NAME
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=(
                "filename",
                "bytes",
                "sha256",
                "role",
                "provenance",
                "status",
            ),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(release_rows)
    manifest_identity = {
        "path": manifest_path,
        "bytes": manifest_path.stat().st_size,
        "sha256": base.sha256_file(manifest_path),
        "md5": base.md5_file(manifest_path),
    }

    validation = {
        "status": "PASS_READY_FOR_ONE_SAME_CONCEPT_SUCCESSOR",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "reserved_successor_record": draft_id,
        "release_policy": (
            "one same-concept compact successor; no duplicate concept or draft"
        ),
        "retained_predecessor_files": EXPECTED_RETAINED_PREDECESSOR_FILES,
        "replaced_files": sorted(REPLACED_NAMES, key=str.casefold),
        "new_files": sorted(
            {
                NEW_PDF,
                NEW_TEX,
                NEW_SOURCE_ZIP,
                README_NAME,
                MANIFEST_NAME,
                VALIDATION_NAME,
            },
            key=str.casefold,
        ),
        "final_public_file_count": EXPECTED_FINAL_FILES,
        "release_manifest": {
            "rows": EXPECTED_MANIFEST_ROWS,
            "bytes": manifest_identity["bytes"],
            "sha256": manifest_identity["sha256"],
        },
        "default_preview": base.DEFAULT_PREVIEW,
        "github": {
            "commit": GITHUB_COMMIT,
            "package_path": GITHUB_PACKAGE,
            "anonymous_readback_files": 13,
            "source_zip_members_read_back": 42,
            "status": "PASS",
        },
        "sga3_expose_xiv": {
            "scope": "complete Expose XIV only",
            "authority_local_pages": "1-36",
            "combined_reader_pages": "835-870",
            "next_excluded": "Expose XV local page 1 / combined page 871",
            "pages": 37,
            "bytes": primary_local[NEW_PDF]["bytes"],
            "sha256": primary_local[NEW_PDF]["sha256"],
            "named_destinations": 236,
            "valid_internal_goto": 24,
            "broken_or_external_actions": 0,
            "font_resources": 32,
            "type3_fonts": 0,
            "raster_xobjects": 0,
            "editable_tex_files": 33,
            "native_diagram_blocks": 1,
            "replacement_diagram_rows": 4,
            "includegraphics_calls": 0,
            "lead_5000dpi_review": "PASS",
            "complete_sga3_claimed": False,
            "exhaustive_reference_v2_claimed": False,
        },
        "source_zip": {
            "filename": NEW_SOURCE_ZIP,
            "members": 42,
            "uncompressed_bytes": 149_081,
            "sha256": primary_local[NEW_SOURCE_ZIP]["sha256"],
            "raster_or_pdf_members": 0,
            "privacy_hits": 0,
        },
        "zip_surface_expected": {
            "archives": EXPECTED_ZIP_ARCHIVES,
            "file_members": EXPECTED_ZIP_FILE_MEMBERS,
            "directory_entries": EXPECTED_ZIP_DIRECTORY_ENTRIES,
            "all_entries": EXPECTED_ZIP_ALL_ENTRIES,
            "uncompressed_bytes": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
        },
        "privacy_hits": [],
        "new_license_grant": False,
    }
    validation_path = CONTROLS_ROOT / VALIDATION_NAME
    base.save_json(validation_path, validation)
    validation_identity = {
        "path": validation_path,
        "bytes": validation_path.stat().st_size,
        "sha256": base.sha256_file(validation_path),
        "md5": base.md5_file(validation_path),
    }

    result = dict(new_local)
    result[MANIFEST_NAME] = manifest_identity
    result[VALIDATION_NAME] = validation_identity
    return result


for name, value in {
    "CONCEPT_DOI": CONCEPT_DOI,
    "PREDECESSOR_RECORD": PREDECESSOR_RECORD,
    "PREDECESSOR_DOI": PREDECESSOR_DOI,
    "PUBLICATION_DATE": PUBLICATION_DATE,
    "VERSION": VERSION,
    "GITHUB_COMMIT": GITHUB_COMMIT,
    "GITHUB_PACKAGE": GITHUB_PACKAGE,
    "NEW_PDF": NEW_PDF,
    "NEW_TEX": NEW_TEX,
    "NEW_SOURCE_ZIP": NEW_SOURCE_ZIP,
    "README_NAME": README_NAME,
    "MANIFEST_NAME": MANIFEST_NAME,
    "VALIDATION_NAME": VALIDATION_NAME,
    "REPLACED_NAMES": REPLACED_NAMES,
    "EXPECTED_PREDECESSOR_FILES": EXPECTED_PREDECESSOR_FILES,
    "EXPECTED_FINAL_FILES": EXPECTED_FINAL_FILES,
    "EXPECTED_RETAINED_PREDECESSOR_FILES": (
        EXPECTED_RETAINED_PREDECESSOR_FILES
    ),
    "EXPECTED_UNRELATED_RETAINED_FILES": EXPECTED_UNRELATED_RETAINED_FILES,
    "EXPECTED_MANIFEST_ROWS": EXPECTED_MANIFEST_ROWS,
    "EXPECTED_ZIP_ARCHIVES": EXPECTED_ZIP_ARCHIVES,
    "EXPECTED_ZIP_FILE_MEMBERS": EXPECTED_ZIP_FILE_MEMBERS,
    "EXPECTED_ZIP_DIRECTORY_ENTRIES": EXPECTED_ZIP_DIRECTORY_ENTRIES,
    "EXPECTED_ZIP_ALL_ENTRIES": EXPECTED_ZIP_ALL_ENTRIES,
    "EXPECTED_ZIP_UNCOMPRESSED_BYTES": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
    "RECEIPT_ROOT": RECEIPT_ROOT,
    "PREDECESSOR_RECEIPT": PREDECESSOR_RECEIPT,
    "CONTROLS_ROOT": CONTROLS_ROOT,
    "READBACK_ROOT": READBACK_ROOT,
    "DRAFT_STATE": DRAFT_STATE,
    "PRIMARY_LOCAL_PATHS": PRIMARY_LOCAL_PATHS,
    "NEW_MANIFEST_ROWS": NEW_MANIFEST_ROWS,
    "DESCRIPTION_HTML": DESCRIPTION_HTML,
    "NOTES_HTML": NOTES_HTML,
}.items():
    setattr(base, name, value)

base.verify_primary_local_files = verify_primary_local_files
base.fetch_predecessor_manifest = fetch_predecessor_manifest
base.readme_text = readme_text
base.generate_controls = generate_controls


if __name__ == "__main__":
    base.main()
