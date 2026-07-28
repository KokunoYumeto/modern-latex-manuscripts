#!/usr/bin/env python3
"""Publish one same-concept SGA3 XX/XXI native-reader successor."""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = (
    SCRIPT_DIR
    / "publish_sga3_native_batch_xii_xix_xxv_zenodo_20260728.py"
)
SPEC = importlib.util.spec_from_file_location("sga3_native_batch_base", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established native-batch workflow")
batch = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = batch
SPEC.loader.exec_module(batch)


PREDECESSOR_RECORD = 21639977
PREDECESSOR_DOI = "10.5281/zenodo.21639977"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-28"
VERSION = "2026-07-28 SGA3 Exposes XX and XXI native working readers"
GITHUB_COMMIT = "9fc59e75e0bcaa4a0998aa14d397a843a4eaf15f"
GITHUB_PACKAGE = "sources/sga"

README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
REPLACED_NAMES = {README_NAME, MANIFEST_NAME, VALIDATION_NAME}

EXPECTED_PREDECESSOR_FILES = 82
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 80
EXPECTED_FINAL_FILES = 88
EXPECTED_RETAINED_PREDECESSOR_FILES = 79
EXPECTED_UNRELATED_RETAINED_FILES = 79
EXPECTED_MANIFEST_ROWS = 86
EXPECTED_ZIP_ARCHIVES = 55
EXPECTED_ZIP_FILE_MEMBERS = 4_611
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_617
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 419_454_154
EXPECTED_GITHUB_READBACK_FILES = 26
EXPECTED_NEW_ZIP_MEMBERS = 80
SESSION_C_RULE = {
    "existing_600_1200_evidence_invalidated": False,
    "reopen_300_only_approvals": True,
    "native_tex_required_for_new_delivery": True,
    "default_review_dpi": 5000,
    "ambiguity_review_dpi": 9000,
    "session_c_atomic_panels_closed": 28,
    "session_c_atomic_panels_open": 0,
    "xx_closed": True,
    "xxi_closed": True,
}

REPO_ROOT = SCRIPT_DIR.parent
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21639977_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_native_batch_xx_xxi_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_native_batch_xx_xxi_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_sga3_native_batch_xx_xxi_zenodo_draft_state.json"
)

UNITS = [
    {
        "roman": "XX",
        "package": "sga3-expose-xx-native-loop1-working-20260728",
        "pdf": (
            "00c20_SGA3_Expose_XX_English_NativeDiagram_"
            "Loop1_Working_20260728.pdf"
        ),
        "tex": (
            "02c20_SGA3_Expose_XX_English_NativeDiagram_"
            "Loop1_Working_20260728.tex"
        ),
        "zip": (
            "10c20_SGA3_Expose_XX_NativeDiagram_"
            "Loop1_Source_20260728.zip"
        ),
        "pdf_identity": (
            236_958,
            "0AFA79FC6140B72814EB0BA03191709C1CFC718F5CE0485AD8151E103FD1AB15",
        ),
        "tex_identity": (
            2_163,
            "9DF5337BDDADAC34B59626159D543660FAE6AA9F84A85F2FAB2516EBB4535D6C",
        ),
        "zip_identity": (
            53_447,
            "BE514E26716741720F7D880874F39C88FCAE58BB9A4E0EF4A3B7EBF8DC09F202",
        ),
        "outer_manifest_sha256": (
            "84AB016547A5C19BAEF3725B4D1109EBC869FF23D54E71D197BF6882032D49AC"
        ),
        "outer_manifest_rows": 12,
        "zip_members": 29,
        "zip_uncompressed": 129_379,
        "pages": 41,
        "destinations": 327,
        "goto": 46,
        "fonts": 30,
        "tex_files": 19,
        "diagrams": 10,
        "diagram_review": "top-level lead 5000-dpi review",
    },
    {
        "roman": "XXI",
        "package": "sga3-expose-xxi-native-loop1-working-20260728",
        "pdf": (
            "00c21_SGA3_Expose_XXI_English_NativeDiagram_"
            "Loop1_Working_20260728.pdf"
        ),
        "tex": (
            "02c21_SGA3_Expose_XXI_English_NativeDiagram_"
            "Loop1_Working_20260728.tex"
        ),
        "zip": (
            "10c21_SGA3_Expose_XXI_NativeDiagram_"
            "Loop1_Source_20260728.zip"
        ),
        "pdf_identity": (
            295_397,
            "A1C58F35B3AA2D29C02A9953B569295ACB0574786728432DD3D726E9F143F0D0",
        ),
        "tex_identity": (
            3_597,
            "A0C8E0173AE0C6D620AE56F496FE58B067E29C8142B26614DED40BFA71C45F10",
        ),
        "zip_identity": (
            73_756,
            "E961C79C1E4342A37260A89DC063AC26D1323C0F684F62CE1546DCD2DEEC6FB2",
        ),
        "outer_manifest_sha256": (
            "4B17107932697DF0596101F958B550493E9289DF6827B2F9EAFB5ECBCA0EA53C"
        ),
        "outer_manifest_rows": 12,
        "zip_members": 51,
        "zip_uncompressed": 166_921,
        "pages": 56,
        "destinations": 378,
        "goto": 240,
        "fonts": 32,
        "tex_files": 41,
        "diagrams": 11,
        "diagram_review": "top-level lead 5000-dpi review",
    },
]

PACKAGE_ROOTS = {
    unit["roman"]: REPO_ROOT / "sources" / "sga" / unit["package"]
    for unit in UNITS
}
PRIMARY_LOCAL_PATHS = {}
PRIMARY_EXPECTED = {}
for unit in UNITS:
    root = PACKAGE_ROOTS[unit["roman"]]
    for kind in ("pdf", "tex", "zip"):
        name = unit[kind]
        PRIMARY_LOCAL_PATHS[name] = root / name
        PRIMARY_EXPECTED[name] = unit[f"{kind}_identity"]

NEW_MANIFEST_ROWS = {}
for unit in UNITS:
    package_url = (
        "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
        f"{GITHUB_COMMIT}/sources/sga/{unit['package']}"
    )
    NEW_MANIFEST_ROWS[unit["pdf"]] = {
        "role": "english_reader",
        "provenance": (
            f"complete bounded SGA3 Expose {unit['roman']} native-diagram "
            f"working reader; GitHub {package_url}"
        ),
        "status": (
            f"bounded_complete_expose_{unit['roman'].lower()}_working_reader_"
            "not_complete_sga3"
        ),
    }
    NEW_MANIFEST_ROWS[unit["tex"]] = {
        "role": "english_master_tex",
        "provenance": (
            f"direct editable master for SGA3 Expose {unit['roman']}; "
            f"GitHub {package_url}"
        ),
        "status": "bounded_working_source_native_diagrams_no_raster",
    }
    NEW_MANIFEST_ROWS[unit["zip"]] = {
        "role": "grouped_source_and_qa",
        "provenance": (
            f"privacy-clean editable source and QA closure for SGA3 Expose "
            f"{unit['roman']}; GitHub {package_url}"
        ),
        "status": (
            "bounded_source_qa_no_authority_pixels_no_raster_diagram_"
            "not_rights_clearance"
        ),
    }
NEW_MANIFEST_ROWS[README_NAME] = {
    "role": "manifest_status",
    "provenance": (
        "current compact same-concept release note; GitHub commit "
        + GITHUB_COMMIT
    ),
    "status": "current_release_control",
}

DESCRIPTION_PARAGRAPHS = [
    (
        "This same-concept compact successor preserves 79 files from version "
        "10.5281/zenodo.21639977 byte-identically, refreshes the three release "
        "controls, and adds complete bounded SGA3 Exposes XX and XXI as two "
        "direct working readers, two direct editable master TeX files, and "
        "two grouped source/QA ZIPs. SGA1 remains the default preview."
    ),
    (
        "The two new A4 readers comprise 97 pages. Expose XX has 41 pages, "
        "327 named destinations, and 46 valid internal GoTo actions. Expose "
        "XXI has 56 pages, 378 destinations, and 240 actions. Both have zero "
        "invalid or external actions, zero Type3 fonts, and zero raster "
        "XObjects."
    ),
    (
        "Their 60 editable TeX files deliver 21 native atomic diagram panels "
        "and no raster diagram inclusions. Every panel passed direct top-level "
        "lead authority comparison at about 5000 dpi. Expose XX includes two "
        "copy-on-write repairs; Expose XXI includes two. No unresolved "
        "ambiguity required 9000-dpi escalation. Existing 600- and 1200-dpi "
        "evidence remains valid append-only history and context."
    ),
    (
        "Each source closure passed four archive XeLaTeX passes. Passes three "
        "and four agree in text, decoded content, geometry, links, fonts, and "
        "rendered output. The submitted Expose-XXI r6 PDF had stale contents "
        "page numbers; the public reader uses the corrected converged rebuild. "
        "Its other 55 pages remain pixel-identical to r6."
    ),
    (
        "The two source ZIPs contain 80 safe file members and exclude authority "
        "pixels, high-resolution crops, raster diagrams, raw private logs, and "
        "private paths. The existing 1,182-page SGA3 current-progress "
        "cumulative reader remains available as readable history and is not "
        "represented as native-diagram final."
    ),
    (
        "The controlling Polo-Gille authority PDFs are identity controls only "
        "and are not redistributed. Floris's pre-existing GPU OCR may be "
        "consulted read-only as locator or drafting evidence and was not "
        "regenerated. Jacob C. Reinhold's jcreinhold/sga English lineage at "
        "revision e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e is credited "
        "comparison material, not source authority; its stated CC BY 4.0 "
        "applies only to that contribution."
    ),
    (
        "These packages are bounded scholarly working readers, not complete "
        "SGA3, critical editions, exhaustive reference-v2 certification, "
        "rights clearance, mathematical certification, peer review, or "
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
    "<p>Compact reader-first SGA surface with 88 public files. Two bounded "
    "native SGA3 readers and their master TeX files are direct; each editable "
    "source/QA closure is grouped in one ZIP. GitHub custody commit: "
    f"{GITHUB_COMMIT}.</p>"
)


def readme_text(draft_id: int) -> str:
    package_lines = "\n".join(
        (
            "  - `https://github.com/KokunoYumeto/modern-latex-manuscripts/"
            f"tree/{GITHUB_COMMIT}/sources/sga/{unit['package']}`"
        )
        for unit in UNITS
    )
    return f"""# Current compact SGA release

This is one same-concept successor to Zenodo record {PREDECESSOR_RECORD}. It
retains 79 predecessor files byte-identically, refreshes three release
controls, and adds complete bounded SGA3 Exposes XX and XXI as direct working
readers, direct editable master TeX files, and grouped source/QA ZIPs. The
reserved successor record is {draft_id}. SGA1 remains the default preview.

## New bounded native SGA3 readers

- Expose XX: 41 pages, 19 editable TeX files, 10 native atomic panels,
  327 named destinations, and 46 valid internal GoTo actions.
- Expose XXI: 56 pages, 41 editable TeX files, 11 native atomic panels,
  378 named destinations, and 240 valid internal GoTo actions.

Both readers have zero invalid or external actions, zero Type3 fonts, zero
raster XObjects, and zero active raster diagram inclusions. All 21 panels
passed direct top-level lead review at about 5000 dpi.

The Expose-XXI public reader is a four-pass archive rebuild from the exact
submitted TeX. It corrects stale table-of-contents numbers in the local r6
PDF; the other 55 pages remain pixel-identical.

## Current-progress boundary

The existing 1,182-page SGA3 cumulative working reader remains directly
available as readable history. It is not represented as native-diagram-final.
These standalone readers do not claim complete SGA3 or exhaustive
reference-v2 closure.

## Authority, rights, and lineage

The controlling Polo-Gille authority PDFs are identity controls only and are
not redistributed. Floris's pre-existing GPU OCR may be consulted read-only
as locator or drafting material and was not regenerated. Jacob C. Reinhold's
`jcreinhold/sga` English lineage at commit
`e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison material,
not authority; its stated CC BY 4.0 applies only to that contribution. No
blanket license or transfer of underlying rights is asserted.

Machine-assisted contributors include OpenAI Codex / ChatGPT and Anthropic
Claude under human direction. GitHub custody commit:

`{GITHUB_COMMIT}`

Packages:

{package_lines}
"""


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
    "EXPECTED_PREDECESSOR_MANIFEST_ROWS": (
        EXPECTED_PREDECESSOR_MANIFEST_ROWS
    ),
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
    "UNITS": UNITS,
    "PACKAGE_ROOTS": PACKAGE_ROOTS,
    "PRIMARY_LOCAL_PATHS": PRIMARY_LOCAL_PATHS,
    "PRIMARY_EXPECTED": PRIMARY_EXPECTED,
    "NEW_MANIFEST_ROWS": NEW_MANIFEST_ROWS,
    "DESCRIPTION_HTML": DESCRIPTION_HTML,
    "NOTES_HTML": NOTES_HTML,
}.items():
    setattr(batch, name, value)
    setattr(batch.base, name, value)

batch.base.verify_primary_local_files = batch.verify_primary_local_files
batch.base.fetch_predecessor_manifest = batch.fetch_predecessor_manifest
batch.base.readme_text = readme_text
batch.base.generate_controls = batch.generate_controls


if __name__ == "__main__":
    batch.base.main()
