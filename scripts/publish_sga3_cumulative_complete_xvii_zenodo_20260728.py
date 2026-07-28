#!/usr/bin/env python3
"""Publish the SGA3 cumulative reader with complete Expose XVII."""

from __future__ import annotations

import csv
import importlib.util
import io
import json
import os
import shutil
import zipfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = SCRIPT_DIR / "publish_sga3_cumulative_with_x_zenodo_20260728.py"
SPEC = importlib.util.spec_from_file_location("sga_successor_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA successor workflow")
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)


PREDECESSOR_RECORD = 21636902
PREDECESSOR_DOI = "10.5281/zenodo.21636902"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-28"
VERSION = (
    "2026-07-28 SGA3 current-progress cumulative: "
    "complete I-XVIII and XX; partial XXI and XXII"
)
GITHUB_COMMIT = "5fee121b33874eb994ed0e5456c1256bf735fd4b"
GITHUB_PACKAGE = (
    "sources/sga/sga3-english-current-progress-cumulative-latest-20260728"
)

OLD_PDF = (
    "00c_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.pdf"
)
OLD_TEX = (
    "02c_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.tex"
)
OLD_SOURCE_ZIP = (
    "10c8_SGA3_CurrentProgress_Source_History_Latest_20260728.zip"
)
NEW_PDF = "00c_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.pdf"
NEW_TEX = "02c_SGA3_English_CurrentProgress_Cumulative_Latest_20260728.tex"
NEW_SOURCE_ZIP = (
    "10c8_SGA3_CurrentProgress_Source_History_Latest_20260728.zip"
)
README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
REPLACED_NAMES = {
    OLD_PDF,
    OLD_TEX,
    OLD_SOURCE_ZIP,
    README_NAME,
    MANIFEST_NAME,
    VALIDATION_NAME,
}

EXPECTED_PREDECESSOR_FILES = 67
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 65
EXPECTED_FINAL_FILES = 67
EXPECTED_RETAINED_PREDECESSOR_FILES = 61
EXPECTED_UNRELATED_RETAINED_FILES = 61
EXPECTED_MANIFEST_ROWS = 65
EXPECTED_ZIP_ARCHIVES = 48
EXPECTED_ZIP_FILE_MEMBERS = 4_399
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_405
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 418_574_682

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = (
    REPO_ROOT
    / "sources"
    / "sga"
    / "sga3-english-current-progress-cumulative-latest-20260728"
)
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21636902_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_cumulative_complete_xvii_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_cumulative_complete_xvii_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_complete_xvii_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    NEW_PDF: PACKAGE_ROOT / NEW_PDF,
    NEW_TEX: PACKAGE_ROOT / NEW_TEX,
    NEW_SOURCE_ZIP: PACKAGE_ROOT / NEW_SOURCE_ZIP,
}
PRIMARY_EXPECTED = {
    NEW_PDF: (
        7_427_202,
        "970CDB20FBFCADEBACDE8AD4C69D89E38AFF278F067B1998B809411538B43660",
    ),
    NEW_TEX: (
        30_096,
        "5AA580989A66EFCAAA464257D05F72699A1DA1C82E8C90C2FCA9B93C21778E60",
    ),
    NEW_SOURCE_ZIP: (
        23_920_541,
        "DEE96050EC1D0A2E071CB873E7750338CE39A0F1839B0794797B3DBF296023FF",
    ),
}

NEW_MANIFEST_ROWS = {
    NEW_PDF: {
        "role": "english_reader",
        "provenance": (
            "preferred SGA3 current-progress cumulative working reader; "
            "GitHub commit " + GITHUB_COMMIT
        ),
        "status": (
            "preferred_working_reader_incomplete_not_final_diagram_"
            "fidelity_closure"
        ),
    },
    NEW_TEX: {
        "role": "english_master_tex",
        "provenance": (
            "direct editable master for the preferred current-progress "
            "cumulative reader; GitHub commit " + GITHUB_COMMIT
        ),
        "status": "current_progress_working_source_incomplete_sga3",
    },
    NEW_SOURCE_ZIP: {
        "role": "grouped_source_evidence_and_predecessor_history",
        "provenance": (
            "1080-member privacy-clean source/history closure with exact "
            "predecessor reader retained; GitHub commit " + GITHUB_COMMIT
        ),
        "status": "current_progress_source_history_not_final_certification",
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
        "This same-concept compact successor replaces only the preferred SGA3 "
        "current-progress PDF, its direct editable master, its grouped "
        "source/history ZIP, and three release controls. The other 61 files "
        "from version 10.5281/zenodo.21636902 are retained byte-identically. "
        "SGA1 remains the default preview."
    ),
    (
        "The preferred SGA3 working reader has 1,182 A4 pages. It contains "
        "complete current working bodies for the Editorial Notice, "
        "Introduction, Exposes I-XVIII, and XX; Expose XXI through local page "
        "5 / Application 2.1.2; and the frozen Expose XXII local pages 1-10. "
        "Expose XVII now closes through Appendix III on authority local page "
        "49. Expose XIX and Exposes XXIII-XXVI are explicit gaps."
    ),
    (
        "This is intentionally a readable preservation release while SGA3 "
        "remains unfinished. It is not a complete translation, critical "
        "edition, rights clearance, tagged accessibility edition, uniform "
        "component certification, or final diagram/reference-fidelity "
        "closure. A post-freeze high-zoom audit found five Expose-V diagram "
        "layout defects in figures007-011 involving bottom arrow-label side or "
        "placement; mathematical content was intact and corrected successors "
        "remain pending."
    ),
    (
        "The reader has 7,481 named destinations, 4,031 valid internal link "
        "annotations/actions, zero invalid or external URI actions, 63 font "
        "resources, and no Type3 fonts. Three XeLaTeX passes converged without "
        "fatal errors, undefined controls or references, duplicate "
        "destinations, missing inputs, missing characters, or rerun requests. "
        "An isolated source-archive rebuild matched all 1,182 decoded page "
        "streams, extracted text, geometry, destinations, links, and "
        "normalized font resources; 37 selected renders were pixel-exact."
    ),
    (
        "The grouped source/history ZIP has 1,080 exact safe members and "
        "includes the immediately preceding cumulative PDF, TeX, and README. "
        "Its CRC, exact-set, member hashes, privacy scan, extraction, and fresh "
        "three-pass rebuild all passed. Earlier Zenodo versions remain "
        "immutable history rather than loose duplicates on the current landing "
        "surface."
    ),
    (
        "Polo-Gille source PDFs control the French wording, formulas, "
        "numbering, notes, page order, and diagram appearance; they are not "
        "redistributed by this package. Floris's pre-existing GPU OCR was "
        "consulted read-only as a locator or drafting witness and was not "
        "regenerated. Jacob C. Reinhold's jcreinhold/sga English lineage at "
        "revision e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e is credited "
        "comparison and drafting material, not source authority; its stated "
        "CC BY 4.0 applies only to that contribution. Rights in the underlying "
        "French works and scans remain with their holders. Machine-assisted "
        "contributors include OpenAI Codex / ChatGPT and Anthropic Claude "
        "under human direction."
    ),
]
DESCRIPTION_HTML = "\n".join(f"<p>{text}</p>" for text in DESCRIPTION_PARAGRAPHS)
NOTES_HTML = (
    "<p>Compact reader-first surface with 67 public files. The expanded SGA3 "
    "reader is direct; source, evidence, and predecessor state are grouped in "
    "one ZIP. It is a working preservation reader and explicitly not final "
    "diagram-fidelity closure. GitHub custody commit: "
    f"{GITHUB_COMMIT}.</p>"
)


def verify_zip(path: Path) -> None:
    files = 0
    directories = 0
    uncompressed = 0
    with zipfile.ZipFile(path, "r") as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"ZIP CRC failure: {bad}")
        names = archive.namelist()
        if len(names) != len(set(names)):
            raise RuntimeError("Duplicate source ZIP member")
        for info in archive.infolist():
            base.safe_zip_name(info.filename)
            if info.is_dir():
                directories += 1
            else:
                files += 1
                uncompressed += info.file_size
    if (files, directories, uncompressed) != (1_080, 0, 29_392_857):
        raise RuntimeError(
            "Source ZIP boundary mismatch: "
            f"{(files, directories, uncompressed)}"
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

    package_validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    if (
        package_validation.get("status") != "PASS"
        or package_validation.get("errors") != []
        or package_validation.get(
            "independent_source_archive_rebuild_receipt_included"
        )
        is not True
    ):
        raise RuntimeError("Local package validation is not controlling PASS")
    verify_zip(PRIMARY_LOCAL_PATHS[NEW_SOURCE_ZIP])
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
replaces only the preferred SGA3 cumulative PDF, direct master TeX, grouped
source/history ZIP, and three release controls. All other 61 predecessor files
remain byte-identical. The reserved successor record is {draft_id}.

## Preferred SGA3 current-progress reader

`{NEW_PDF}` has 1,182 A4 pages and contains:

- complete current working bodies for the Editorial Notice, Introduction,
  Exposes I-XVIII, and XX;
- Expose XVII through Appendix III on authority local page 49;
- Expose XXI through local page 5 / Application 2.1.2;
- the frozen Expose XXII local-pages-1-10 snapshot; and
- explicit gaps for Expose XIX and Exposes XXIII-XXVI.

This is a readable working preservation release, not complete SGA3, a critical
edition, rights clearance, accessibility remediation, uniform component
certification, or final diagram/reference-fidelity closure.

A post-freeze high-zoom audit found five layout defects in Expose-V figures
007-011: bottom arrow-label side or placement. Mathematical content remained
intact. Later corrected no-overwrite components should replace them; this
version remains honest public history.

## Checks

- 7,481 named destinations;
- 4,031 valid internal link annotations/actions;
- zero invalid or URI actions;
- 63 font resources and zero Type3 fonts;
- three converged XeLaTeX passes with zero critical diagnostics;
- 1,182/1,182 decoded content, text, geometry, destination, link, and
  normalized-font comparisons exact against a fresh extracted-source rebuild;
- 37 selected page renders pixel-exact; and
- 1,080/1,080 source/history ZIP members exact with privacy hits 0.

## Authority, rights, and lineage

Polo-Gille PDFs control the French wording, formulas, numbering, notes, page
order, and diagram appearance. They are not redistributed here. Floris's
pre-existing GPU OCR was consulted read-only as locator or drafting material
and was not regenerated. Jacob C. Reinhold's `jcreinhold/sga` English Markdown
at commit `e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison and
drafting lineage, not authority; its stated CC BY 4.0 applies only to that
contribution. No blanket license or transfer of underlying rights is asserted.

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

    retained_rows: list[dict[str, str]] = []
    for row in predecessor_rows:
        name = row["filename"]
        if name in {OLD_PDF, OLD_TEX, OLD_SOURCE_ZIP, README_NAME}:
            continue
        if name in REPLACED_NAMES:
            raise RuntimeError(f"Unexpected replaced control row: {name}")
        identity = predecessor_identities[name]
        if (int(row["bytes"]), row["sha256"].upper()) != (
            identity["bytes"],
            identity["sha256"],
        ):
            raise RuntimeError(f"Retained manifest identity mismatch: {name}")
        retained_rows.append(dict(row))

    new_local = dict(primary_local)
    new_local[README_NAME] = readme_identity
    for name in sorted(new_local, key=str.casefold):
        metadata = NEW_MANIFEST_ROWS[name]
        identity = new_local[name]
        retained_rows.append(
            {
                "filename": name,
                "bytes": str(identity["bytes"]),
                "sha256": identity["sha256"],
                "role": metadata["role"],
                "provenance": metadata["provenance"],
                "status": metadata["status"],
            }
        )
    retained_rows.sort(key=lambda row: row["filename"].casefold())
    if len(retained_rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError(
            f"Expected {EXPECTED_MANIFEST_ROWS} rows, got {len(retained_rows)}"
        )
    if len({row["filename"] for row in retained_rows}) != len(retained_rows):
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
        writer.writerows(retained_rows)
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
            "anonymous_readback_files": 12,
            "source_zip_members_read_back": 1_080,
            "status": "PASS",
        },
        "sga3_reader": {
            "complete": (
                "Editorial Notice, Introduction, Exposes I-XVIII, XX"
            ),
            "partial": "Exposes XXI, XXII",
            "gaps": "Expose XIX and Exposes XXIII-XXVI",
            "pages": 1_182,
            "bytes": primary_local[NEW_PDF]["bytes"],
            "sha256": primary_local[NEW_PDF]["sha256"],
            "named_destinations": 7_481,
            "valid_internal_goto": 4_031,
            "broken_or_external_actions": 0,
            "font_resources": 63,
            "type3_fonts": 0,
            "independent_rebuild_all_pages_structurally_exact": True,
            "selected_renders_pixel_exact": 37,
        },
        "postfreeze_diagram_reaudit": {
            "expose": "V",
            "strict_pass": 25,
            "strict_layout_fail": 5,
            "affected": "figures007-011",
            "defect": "bottom arrow-label side or placement",
            "mathematical_content_intact": True,
            "final_diagram_fidelity_closure_claimed": False,
        },
        "source_zip": {
            "filename": NEW_SOURCE_ZIP,
            "members": 1_080,
            "uncompressed_bytes": 29_392_857,
            "sha256": primary_local[NEW_SOURCE_ZIP]["sha256"],
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
    "OLD_PDF": OLD_PDF,
    "OLD_TEX": OLD_TEX,
    "OLD_SOURCE_ZIP": OLD_SOURCE_ZIP,
    "NEW_PDF": NEW_PDF,
    "NEW_TEX": NEW_TEX,
    "NEW_SOURCE_ZIP": NEW_SOURCE_ZIP,
    "README_NAME": README_NAME,
    "MANIFEST_NAME": MANIFEST_NAME,
    "VALIDATION_NAME": VALIDATION_NAME,
    "REPLACED_NAMES": REPLACED_NAMES,
    "EXPECTED_PREDECESSOR_FILES": EXPECTED_PREDECESSOR_FILES,
    "EXPECTED_FINAL_FILES": EXPECTED_FINAL_FILES,
    "EXPECTED_RETAINED_PREDECESSOR_FILES": EXPECTED_RETAINED_PREDECESSOR_FILES,
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
