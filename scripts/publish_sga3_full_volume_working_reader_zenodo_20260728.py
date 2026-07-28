#!/usr/bin/env python3
"""Publish the compact SGA3 1,434-page working-reader successor."""

from __future__ import annotations

import csv
import importlib.util
import io
import json
import os
import shutil
import sys
import zipfile
from pathlib import Path, PurePosixPath


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = SCRIPT_DIR / "publish_sga3_native_batch_xx_xxi_zenodo_20260728.py"
SPEC = importlib.util.spec_from_file_location("sga3_previous_release", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA successor workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)
base = previous.batch.base


PREDECESSOR_RECORD = 21642747
PREDECESSOR_DOI = "10.5281/zenodo.21642747"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-28"
VERSION = "2026-07-28 SGA3 1434-page current-progress cumulative reader"
GITHUB_COMMIT = "ed1448ccf4bc5b1e8ecf4ef4532d9b37eb0e9a0a"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-current-progress-full-volume-integration-20260728-r1"
)

PDF_NAME = "00c_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.pdf"
TEX_NAME = "02c_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.tex"
ZIP_NAME = "10c9_SGA3_CurrentProgress_FullVolume_Integration_Source_20260728.zip"
README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
REPLACED_NAMES = {
    PDF_NAME,
    TEX_NAME,
    README_NAME,
    MANIFEST_NAME,
    VALIDATION_NAME,
}

EXPECTED_PREDECESSOR_FILES = 88
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 86
EXPECTED_FINAL_FILES = 89
EXPECTED_RETAINED_PREDECESSOR_FILES = 83
EXPECTED_UNRELATED_RETAINED_FILES = 83
EXPECTED_MANIFEST_ROWS = 87
EXPECTED_ZIP_ARCHIVES = 56
EXPECTED_ZIP_FILE_MEMBERS = 5_478
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 5_484
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 427_047_861
EXPECTED_GITHUB_READBACK_FILES = 11
EXPECTED_NEW_ZIP_MEMBERS = 867
SESSION_C_RULE = {
    "existing_600_1200_evidence_invalidated": False,
    "reopen_300_only_approvals": True,
    "native_tex_required_for_future_diagram_final_delivery": True,
    "default_review_dpi": 5000,
    "ambiguity_review_dpi": 9000,
    "session_c_atomic_panels_closed": 28,
    "session_c_atomic_panels_open": 0,
    "current_cumulative_is_diagram_final": False,
}

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-current-progress-full-volume-integration-20260728-r1"
)
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21642747_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_full_volume_working_reader_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_full_volume_working_reader_zenodo_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_sga3_full_volume_working_reader_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    PDF_NAME: PACKAGE_ROOT / PDF_NAME,
    TEX_NAME: PACKAGE_ROOT / TEX_NAME,
    ZIP_NAME: PACKAGE_ROOT / ZIP_NAME,
}
PRIMARY_EXPECTED = {
    PDF_NAME: (
        8_650_355,
        "481EEDECAA8635AEAC5CCA91492797AF651D426A80B6A2F2510BDF05EB3DD36D",
    ),
    TEX_NAME: (
        27_421,
        "89214AC97C29A65FF2DE0BF08A2B1037D39112F091EA746EC80B5EC376702087",
    ),
    ZIP_NAME: (
        4_121_323,
        "E77667080D1C64C84CAB192255600BCAAAB9144E9507C9FB0C4085F98C6FA8CC",
    ),
}
PACKAGE_MANIFEST_SHA256 = (
    "9F27C2F810E30BDBE422B07AC56AF2966A04D7E44BF8C75AF2A3960B3BDF93DF"
)
SOURCE_MANIFEST_SHA256 = (
    "BF83605E60019A86CD6B4D68B172944F9C853EE5349816C368306BF087E98276"
)

PACKAGE_URL = (
    "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
    f"{GITHUB_COMMIT}/{GITHUB_PACKAGE}"
)
NEW_MANIFEST_ROWS = {
    PDF_NAME: {
        "role": "english_reader",
        "provenance": (
            "preferred SGA3 current-progress Loop-1 cumulative reader; "
            f"GitHub {PACKAGE_URL}"
        ),
        "status": (
            "working_reader_1434_pages_explicit_tomeiii_guide_and_"
            "expose_xxiv_gaps_not_complete_sga3_not_diagram_final"
        ),
    },
    TEX_NAME: {
        "role": "english_master_tex",
        "provenance": (
            "direct editable integration master for the preferred SGA3 "
            f"current-progress reader; GitHub {PACKAGE_URL}"
        ),
        "status": (
            "working_integration_master_loop1_raster_debt_disclosed_"
            "not_diagram_final"
        ),
    },
    ZIP_NAME: {
        "role": "grouped_source_and_machine_controls",
        "provenance": (
            "recorder-derived build closure for the 1434-page reader; "
            f"GitHub {PACKAGE_URL}"
        ),
        "status": (
            "buildable_source_closure_723_tex_142_provisional_loop1_png_"
            "not_rights_or_diagram_certification"
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
        "This same-concept compact successor preserves 83 files from version "
        "10.5281/zenodo.21642747 byte-identically, replaces the preferred "
        "SGA3 cumulative PDF and direct integration TeX, adds one grouped "
        "buildable source ZIP, and refreshes the three release controls. "
        "SGA1 remains the default preview."
    ),
    (
        "The preferred SGA3 reader now has 1,434 A4 pages and integrates the "
        "Editorial Notice, Introduction, Exposes I-XXIII and XXV-XXVI, the "
        "terminal bibliography, and the Tome III index. The four-page Tome "
        "III mathematical guide and Expose XXIV are explicit in-reader gaps. "
        "The object is current progress, not complete SGA3."
    ),
    (
        "The PDF has 9,246 named destinations, 4,541 valid internal GoTo "
        "actions, zero invalid or external actions, 64 font resources, zero "
        "Type3 fonts, and 142 raster image XObjects. Thirty-eight assembly "
        "and boundary pages passed direct visual review."
    ),
    (
        "The grouped source ZIP contains 867 safe members: an exact "
        "recorder-derived closure of 723 TeX files and 142 PNG assets plus "
        "manifest and validation controls. An independent four-pass rebuild "
        "matched all 1,434 extracted-text pages, decoded page streams, "
        "geometry, destinations, links, normalized fonts, and decoded image "
        "objects. Raw build logs, authority PDFs, OCR, and private paths are "
        "excluded."
    ),
    (
        "The 142 PNG assets are disclosed Loop-1 diagram witnesses needed for "
        "the current readable integration. They are not presented as final "
        "diagram-fidelity closure. Existing 600- and 1200-dpi evidence remains "
        "valid history and context; only 300-dpi-only approvals or identified "
        "defects reopen. Future diagram-final successors require native TeX "
        "and top-level lead authority comparison near 5000 dpi, escalating to "
        "9000 dpi for ambiguity."
    ),
    (
        "The component-specific Polo-Gille authority PDFs are identity and "
        "page controls only and are not redistributed. Floris's pre-existing "
        "GPU OCR may be consulted read-only as locator or drafting evidence "
        "and was not regenerated. Jacob C. Reinhold's jcreinhold/sga English "
        "lineage at revision e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e "
        "is credited comparison material, not source authority; its stated "
        "CC BY 4.0 applies only to that contribution."
    ),
    (
        "This is a scholarly working reader, not a critical edition, blanket "
        "rights clearance, exhaustive final reference or diagram "
        "certification, mathematical certification, peer review, or "
        "tagged-PDF accessibility remediation. No blanket license or transfer "
        "of underlying rights is asserted. Machine-assisted contributors "
        "include OpenAI Codex / ChatGPT and Anthropic Claude under human "
        "direction."
    ),
]
DESCRIPTION_HTML = "\n".join(
    f"<p>{paragraph}</p>" for paragraph in DESCRIPTION_PARAGRAPHS
)
NOTES_HTML = (
    "<p>Compact reader-first SGA surface with 89 public files. The newest "
    "1,434-page SGA3 cumulative reader and master TeX are direct; its exact "
    "build closure is grouped in one ZIP. Older cumulative/source states "
    "remain in the existing history ZIPs. GitHub custody commit: "
    f"{GITHUB_COMMIT}.</p>"
)


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
    if base.sha256_file(outer_manifest) != PACKAGE_MANIFEST_SHA256:
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
    if len(rows) != 10 or {row["filename"] for row in rows} != expected_outer:
        raise RuntimeError("Outer package manifest exact-set mismatch")
    for row in rows:
        path = PACKAGE_ROOT / row["filename"]
        if (path.stat().st_size, base.sha256_file(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Outer package mismatch: {row['filename']}")

    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    reader = validation.get("reader", {})
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or validation.get("privacy", {}).get("hits") != []
        or reader.get("pages") != 1434
        or reader.get("named_destinations") != 9246
        or reader.get("internal_goto_actions") != 4541
        or reader.get("invalid_actions") != 0
        or reader.get("uri_actions") != 0
        or reader.get("raster_xobjects") != 142
    ):
        raise RuntimeError("Package validation is not controlling PASS")

    with zipfile.ZipFile(PRIMARY_LOCAL_PATHS[ZIP_NAME], "r") as archive:
        bad = archive.testzip()
        names = archive.namelist()
        if (
            bad is not None
            or len(names) != 867
            or len(names) != len(set(names))
            or sum(info.file_size for info in archive.infolist()) != 7_593_707
        ):
            raise RuntimeError("Source ZIP boundary or CRC mismatch")
        for name in names:
            base.safe_zip_name(name)
        source_manifest = archive.read("SOURCE_BUNDLE_SHA256.csv")
        if base.hashlib.sha256(source_manifest).hexdigest().upper() != (
            SOURCE_MANIFEST_SHA256
        ):
            raise RuntimeError("Source ZIP manifest identity mismatch")
        source_rows = list(
            csv.DictReader(
                io.StringIO(source_manifest.decode("utf-8-sig"))
            )
        )
        expected_source = set(names) - {"SOURCE_BUNDLE_SHA256.csv"}
        if (
            len(source_rows) != 866
            or {row["relative_path"] for row in source_rows} != expected_source
        ):
            raise RuntimeError("Source ZIP manifest exact-set mismatch")
        for row in source_rows:
            data = archive.read(row["relative_path"])
            if (
                len(data),
                base.hashlib.sha256(data).hexdigest().upper(),
            ) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    f"Source ZIP member mismatch: {row['relative_path']}"
                )
        embedded = json.loads(
            archive.read("SOURCE_BUNDLE_VALIDATION.json").decode("utf-8")
        )
        if embedded.get("status") != "PASS" or embedded.get("errors") != []:
            raise RuntimeError("Embedded source validation is not PASS")
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
        csv.DictReader(
            io.StringIO(content.decode("utf-8-sig"), newline="")
        )
    )
    if len(rows) != EXPECTED_PREDECESSOR_MANIFEST_ROWS:
        raise RuntimeError("Unexpected predecessor release-manifest row count")
    return rows


def readme_text(draft_id: int) -> str:
    return f"""# Current compact SGA release

This is one same-concept successor to Zenodo record {PREDECESSOR_RECORD}. It
retains 83 predecessor files byte-identically, replaces the preferred SGA3
cumulative PDF and direct integration TeX, adds one grouped buildable source
ZIP, and refreshes the three release controls. The reserved successor record
is {draft_id}. SGA1 remains the default preview.

## Preferred SGA3 reading surface

`{PDF_NAME}` is the preferred 1,434-page current-progress reader. It contains
the Editorial Notice, Introduction, Exposes I-XXIII and XXV-XXVI, terminal
bibliography, and the Tome III index. The four-page Tome III guide and Expose
XXIV are explicit gaps.

The reader has 9,246 named destinations and 4,541 valid internal GoTo actions.
It is a working Loop-1 integration, not complete SGA3, a critical edition, or
final reference/diagram/accessibility certification.

## Compact source shape

The PDF and its master TeX remain direct reader-facing files. `{ZIP_NAME}`
contains the exact recorder-derived build closure: 723 TeX files and 142 PNG
assets, plus manifest and validation controls. Older cumulative/source states
remain in existing history ZIPs rather than being promoted as loose files.

The ZIP was independently extracted and rebuilt in four XeLaTeX passes. All
1,434 text pages, decoded content streams, geometry, destinations, links,
normalized fonts, and 142 decoded image objects match the public candidate.

## Diagram state

The 142 PNG assets are disclosed provisional Loop-1 diagram witnesses needed
for the current readable integration. They are not final diagram-fidelity
closure. Existing 600/1200-dpi evidence remains valid history; 300-dpi-only
approval is insufficient. Future diagram-final successors require native TeX
and top-level lead authority comparison near 5000 dpi, escalating to 9000 dpi
for ambiguity.

## Authority, rights, and lineage

The component-specific Polo-Gille authority PDFs are controls only and are not
redistributed. Floris's pre-existing GPU OCR may be consulted read-only as
locator/drafting evidence and was not regenerated. Jacob C. Reinhold's
`jcreinhold/sga` English lineage at commit
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison material,
not authority; its stated CC BY 4.0 applies only to that contribution.

No blanket license or transfer of underlying rights is asserted.
Machine-assisted contributors include OpenAI Codex / ChatGPT and Anthropic
Claude under human direction.

GitHub package:

`{PACKAGE_URL}`
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
        if name in REPLACED_NAMES:
            continue
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
            set(PRIMARY_LOCAL_PATHS)
            | {README_NAME, MANIFEST_NAME, VALIDATION_NAME},
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
            "package_root": GITHUB_PACKAGE,
            "anonymous_readback_files": EXPECTED_GITHUB_READBACK_FILES,
            "source_zip_members_read_back": EXPECTED_NEW_ZIP_MEMBERS,
            "status": "PASS",
        },
        "reader": {
            "filename": PDF_NAME,
            "pages": 1434,
            "bytes": primary_local[PDF_NAME]["bytes"],
            "sha256": primary_local[PDF_NAME]["sha256"],
            "included": (
                "Editorial Notice, Introduction, Exposes I-XXIII and "
                "XXV-XXVI, bibliography and Tome III index"
            ),
            "explicit_gaps": "four-page Tome III guide and Expose XXIV",
            "named_destinations": 9246,
            "valid_internal_goto": 4541,
            "broken_or_external_actions": 0,
            "font_resources": 64,
            "type3_fonts": 0,
            "raster_xobjects": 142,
            "complete_sga3_claimed": False,
            "diagram_final_claimed": False,
        },
        "source_zip": {
            "filename": ZIP_NAME,
            "members": 867,
            "uncompressed_bytes": 7_593_707,
            "sha256": primary_local[ZIP_NAME]["sha256"],
            "tex_files": 723,
            "png_files": 142,
            "privacy_hits": 0,
        },
        "independent_rebuild": {
            "passes": 4,
            "pages_exact": 1434,
            "text_exact": True,
            "decoded_content_exact": True,
            "geometry_exact": True,
            "destination_names_exact": True,
            "link_actions_exact": True,
            "normalized_fonts_exact": True,
            "decoded_image_objects_exact": True,
        },
        "zip_surface_expected": {
            "archives": EXPECTED_ZIP_ARCHIVES,
            "file_members": EXPECTED_ZIP_FILE_MEMBERS,
            "directory_entries": EXPECTED_ZIP_DIRECTORY_ENTRIES,
            "all_entries": EXPECTED_ZIP_ALL_ENTRIES,
            "uncompressed_bytes": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
        },
        "session_c_rule": SESSION_C_RULE,
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
    "EXPECTED_GITHUB_READBACK_FILES": EXPECTED_GITHUB_READBACK_FILES,
    "EXPECTED_NEW_ZIP_MEMBERS": EXPECTED_NEW_ZIP_MEMBERS,
    "SESSION_C_RULE": SESSION_C_RULE,
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
