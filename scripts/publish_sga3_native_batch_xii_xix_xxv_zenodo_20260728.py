#!/usr/bin/env python3
"""Publish one same-concept SGA3 XII/XIX/XXV native-reader successor."""

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


PREDECESSOR_RECORD = 21639459
PREDECESSOR_DOI = "10.5281/zenodo.21639459"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-28"
VERSION = "2026-07-28 SGA3 Exposes XII, XIX, and XXV native working readers"
GITHUB_COMMIT = "e852c35299397f3b1476437a9da3b8ce4b0c2bd5"
GITHUB_PACKAGE = "sources/sga"

README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
REPLACED_NAMES = {README_NAME, MANIFEST_NAME, VALIDATION_NAME}

EXPECTED_PREDECESSOR_FILES = 73
EXPECTED_PREDECESSOR_MANIFEST_ROWS = 71
EXPECTED_FINAL_FILES = 82
EXPECTED_RETAINED_PREDECESSOR_FILES = 70
EXPECTED_UNRELATED_RETAINED_FILES = 70
EXPECTED_MANIFEST_ROWS = 80
EXPECTED_ZIP_ARCHIVES = 53
EXPECTED_ZIP_FILE_MEMBERS = 4_531
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_537
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 419_157_854

REPO_ROOT = SCRIPT_DIR.parent
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21639459_public_readback.json"
)
CONTROLS_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_native_batch_xii_xix_xxv_zenodo_controls"
)
READBACK_ROOT = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga3_native_batch_xii_xix_xxv_zenodo_public_readback"
)
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260728_sga3_native_batch_xii_xix_xxv_zenodo_draft_state.json"
)

UNITS = [
    {
        "roman": "XII",
        "package": "sga3-expose-xii-native-loop1-working-20260728",
        "pdf": (
            "00c12_SGA3_Expose_XII_English_NativeDiagram_"
            "Loop1_Working_20260728.pdf"
        ),
        "tex": (
            "02c12_SGA3_Expose_XII_English_NativeDiagram_"
            "Loop1_Working_20260728.tex"
        ),
        "zip": (
            "10c12_SGA3_Expose_XII_NativeDiagram_"
            "Loop1_Source_20260728.zip"
        ),
        "pdf_identity": (
            282_869,
            "17D3646EF85FB1C1D7831B646755C199C862E912935EC4B01DAA0DF0BF48ADDC",
        ),
        "tex_identity": (
            1_296,
            "2B6F6207CFDA0ADAF046727BC62A533B090FF5A35D66C297306BFE8234335C57",
        ),
        "zip_identity": (
            54_087,
            "1574DB2BBFF469ADAEC1FB26D01D172CBB306753B01761C605DE5A39E3BC9388",
        ),
        "outer_manifest_sha256": (
            "EB7C68CA87CD43663B813CFC592163007567371C2AF2200253F43DE64F136CFA"
        ),
        "zip_members": 14,
        "zip_uncompressed": 171_299,
        "pages": 51,
        "destinations": 287,
        "goto": 28,
        "fonts": 27,
        "tex_files": 5,
        "diagrams": 2,
        "diagram_review": "lead 5000 dpi, with 9000-dpi ambiguity escalation",
    },
    {
        "roman": "XIX",
        "package": "sga3-expose-xix-native-loop1-working-20260728",
        "pdf": (
            "00c19_SGA3_Expose_XIX_English_NativeDiagram_"
            "Loop1_Working_20260728.pdf"
        ),
        "tex": (
            "02c19_SGA3_Expose_XIX_English_NativeDiagram_"
            "Loop1_Working_20260728.tex"
        ),
        "zip": (
            "10c19_SGA3_Expose_XIX_NativeDiagram_"
            "Loop1_Source_20260728.zip"
        ),
        "pdf_identity": (
            659_293,
            "6C57558E58C3D27BF453C094121495F4EC66CF7CEC66E8790D783317BDD1DE39",
        ),
        "tex_identity": (
            3_040,
            "F8FD7CAA87173108419142DB8D5E48752841ECCB801D1D83CA97745E284A5D9E",
        ),
        "zip_identity": (
            50_922,
            "0DCBC8FD12DA00BA4C5BCDB46AFDF0C0233D6A89227D0A6727CF664535930CA5",
        ),
        "outer_manifest_sha256": (
            "5175517B357B316ADE66F559D0D67C2A2BA0A413D37346FA2B428A76CF5C5299"
        ),
        "zip_members": 37,
        "zip_uncompressed": 104_793,
        "pages": 27,
        "destinations": 174,
        "goto": 55,
        "fonts": 35,
        "tex_files": 28,
        "diagrams": 1,
        "diagram_review": "archive 5000-dpi authority replay",
    },
    {
        "roman": "XXV",
        "package": "sga3-expose-xxv-native-loop1-working-20260728",
        "pdf": (
            "00c25_SGA3_Expose_XXV_English_NativeDiagram_"
            "Loop1_Working_20260728.pdf"
        ),
        "tex": (
            "02c25_SGA3_Expose_XXV_English_NativeDiagram_"
            "Loop1_Working_20260728.tex"
        ),
        "zip": (
            "10c25_SGA3_Expose_XXV_NativeDiagram_"
            "Loop1_Source_20260728.zip"
        ),
        "pdf_identity": (
            498_082,
            "8F2FC8434D352354F1AA16A8A36913988768F2261F74072A5F7CF4D796BE04D9",
        ),
        "tex_identity": (
            1_266,
            "C37671D8C1DA7A9DB1EEB8A1FB7F94CAFCD81CB1EE800A6E1C9E1AFDFB0382A7",
        ),
        "zip_identity": (
            21_415,
            "469D61BDEBB99684B5CC3F9BB990BF4287B7C9F585B1494360AF089DE6C7A015",
        ),
        "outer_manifest_sha256": (
            "66D868C2AE02BC268DE3234CD87A19707977E1E098681A9D7B7B631F9C69E88C"
        ),
        "zip_members": 16,
        "zip_uncompressed": 44_261,
        "pages": 14,
        "destinations": 85,
        "goto": 29,
        "fonts": 29,
        "tex_files": 7,
        "diagrams": 2,
        "diagram_review": "lead 5000-dpi review",
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
        "This same-concept compact successor preserves 70 files from version "
        "10.5281/zenodo.21639459 byte-identically, refreshes the three release "
        "controls, and adds complete bounded SGA3 Exposes XII, XIX, and XXV as "
        "three direct working readers, three direct editable master TeX files, "
        "and three grouped source/QA ZIPs. SGA1 remains the default preview."
    ),
    (
        "The three new A4 readers comprise 92 pages. Expose XII has 51 pages, "
        "287 named destinations, and 28 valid internal GoTo actions; Expose "
        "XIX has 27 pages, 174 destinations, and 55 actions; Expose XXV has "
        "14 pages, 85 destinations, and 29 actions. All have zero invalid or "
        "external actions, zero Type3 fonts, and zero raster XObjects."
    ),
    (
        "Their 40 editable TeX files contain five native diagram blocks and "
        "no raster diagram inclusions. Expose XII's two diagrams passed direct "
        "top-level lead comparison at 5000 dpi, with a 9000-dpi escalation and "
        "one corrected label-side placement. Expose XIX's diagram passed a "
        "fresh archive 5000-dpi authority replay. Expose XXV's two diagrams "
        "passed top-level lead 5000-dpi review. Existing 600- and 1200-dpi "
        "evidence remains valid append-only history and context."
    ),
    (
        "Each reader passed three producer and three independent archive build "
        "passes. All 92 producer/rebuild pages match in extracted text, decoded "
        "page-content streams, geometry, and 150-dpi raster output. Every page "
        "was visually reviewed. The three source ZIPs contain 67 safe file "
        "members and exclude authority pixels, high-resolution crops, raster "
        "diagrams, raw private logs, and private paths."
    ),
    (
        "The existing 1,182-page SGA3 current-progress cumulative reader remains "
        "available as readable history and is not represented as native-diagram "
        "final. These standalone readers preserve completed work without "
        "claiming that SGA3 is complete. Exposes XX and XXI remain open under "
        "the Session-C native-diagram control, and Expose XXVI remains active."
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
    "<p>Compact reader-first SGA surface with 82 public files. Three bounded "
    "native SGA3 readers and their master TeX files are direct; each editable "
    "source/QA closure is grouped in one ZIP. The existing cumulative SGA3 "
    "working reader remains visible history. GitHub custody commit: "
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

    for unit in UNITS:
        root = PACKAGE_ROOTS[unit["roman"]]
        outer_manifest = root / "SHA256SUMS.csv"
        if base.sha256_file(outer_manifest) != unit["outer_manifest_sha256"]:
            raise RuntimeError(
                f"Outer manifest identity mismatch: Expose {unit['roman']}"
            )
        rows = list(
            csv.DictReader(
                io.StringIO(outer_manifest.read_text(encoding="utf-8-sig"))
            )
        )
        expected_outer = {
            path.name
            for path in root.iterdir()
            if path.is_file() and path.name != outer_manifest.name
        }
        if len(rows) != 11 or {row["filename"] for row in rows} != expected_outer:
            raise RuntimeError(
                f"Outer manifest exact-set mismatch: Expose {unit['roman']}"
            )
        for row in rows:
            path = root / row["filename"]
            if (path.stat().st_size, base.sha256_file(path)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    f"Outer manifest mismatch: {unit['roman']} "
                    f"{row['filename']}"
                )

        validation = json.loads(
            (root / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
        )
        if (
            validation.get("status") != "PASS"
            or validation.get("errors") != []
            or validation.get("privacy", {}).get("hits") != []
            or validation.get("reader", {}).get("raster_xobjects") != 0
        ):
            raise RuntimeError(
                f"Package validation is not controlling PASS: {unit['roman']}"
            )

        zip_path = root / unit["zip"]
        with zipfile.ZipFile(zip_path, "r") as archive:
            bad = archive.testzip()
            if bad is not None:
                raise RuntimeError(f"Source ZIP CRC failure: {bad}")
            names = archive.namelist()
            if (
                len(names) != unit["zip_members"]
                or len(names) != len(set(names))
                or sum(info.file_size for info in archive.infolist())
                != unit["zip_uncompressed"]
            ):
                raise RuntimeError(
                    f"Source ZIP boundary mismatch: Expose {unit['roman']}"
                )
            for name in names:
                safe_member(name)
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
            if any(PurePosixPath(name).suffix.lower() in forbidden for name in names):
                raise RuntimeError(
                    f"Source ZIP contains raster/PDF: Expose {unit['roman']}"
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
            if {row["relative_path"] for row in source_rows} != expected_source:
                raise RuntimeError(
                    f"Source ZIP manifest set mismatch: Expose {unit['roman']}"
                )
            for row in source_rows:
                data = archive.read(row["relative_path"])
                if (len(data), base.hashlib.sha256(data).hexdigest().upper()) != (
                    int(row["bytes"]),
                    row["sha256"].upper(),
                ):
                    raise RuntimeError(
                        f"Source ZIP member mismatch: {unit['roman']} "
                        f"{row['relative_path']}"
                    )
            source_validation = json.loads(
                archive.read("SOURCE_PACKAGE_VALIDATION.json")
            )
            if (
                source_validation.get("status") != "PASS"
                or source_validation.get("errors") != []
            ):
                raise RuntimeError(
                    f"Source ZIP validation failed: Expose {unit['roman']}"
                )
            tex = "\n".join(
                archive.read(name).decode("utf-8")
                for name in names
                if name.lower().endswith(".tex")
            )
            if r"\includegraphics" in tex:
                raise RuntimeError(
                    f"Source ZIP contains raster inclusion: Expose {unit['roman']}"
                )
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
    unit_lines = "\n".join(
        (
            f"- Expose {unit['roman']}: {unit['pages']} pages, "
            f"{unit['tex_files']} editable TeX files, "
            f"{unit['diagrams']} native diagram(s), "
            f"{unit['destinations']} destinations, {unit['goto']} valid "
            f"internal GoTo actions, {unit['fonts']} font resources, and "
            f"{unit['diagram_review']}."
        )
        for unit in UNITS
    )
    package_lines = "\n".join(
        (
            "  - `https://github.com/KokunoYumeto/modern-latex-manuscripts/"
            f"tree/{GITHUB_COMMIT}/sources/sga/{unit['package']}`"
        )
        for unit in UNITS
    )
    return f"""# Current compact SGA release

This is one same-concept successor to Zenodo record {PREDECESSOR_RECORD}. It
retains 70 predecessor files byte-identically, refreshes three release
controls, and adds complete bounded SGA3 Exposes XII, XIX, and XXV as direct
working readers, direct editable master TeX files, and grouped source/QA ZIPs.
The reserved successor record is {draft_id}. SGA1 remains the default preview.

## New bounded native SGA3 readers

{unit_lines}

All three readers have zero invalid or external actions, zero Type3 fonts,
and zero raster XObjects. Their source packages contain 40 editable TeX files
and five native diagram blocks. They passed three producer and three
independent archive build passes. All 92 producer/rebuild pages match in
extracted text, decoded page-content streams, geometry, and 150-dpi renders.

Existing 600- and 1200-dpi evidence remains legitimate append-only history
and context. A 300-dpi image alone does not carry diagram-fidelity approval.
The current top-level review rule uses about 5000 dpi by default and 9000 dpi
where ambiguity remains.

## Current-progress boundary

The existing 1,182-page SGA3 cumulative working reader remains directly
available as readable history. It is not represented as native-diagram-final.
These standalone readers do not claim complete SGA3. Exposes XX and XXI remain
open under the Session-C native-diagram control; Expose XXVI remains active.

These releases are not critical editions, exhaustive reference-v2
certifications, rights clearance, mathematical certification, peer review, or
tagged-PDF accessibility remediation.

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
            "anonymous_readback_files": 37,
            "source_zip_members_read_back": 67,
            "status": "PASS",
        },
        "units": [
            {
                "expose": unit["roman"],
                "scope": f"complete Expose {unit['roman']} only",
                "pages": unit["pages"],
                "pdf": unit["pdf"],
                "bytes": primary_local[unit["pdf"]]["bytes"],
                "sha256": primary_local[unit["pdf"]]["sha256"],
                "named_destinations": unit["destinations"],
                "valid_internal_goto": unit["goto"],
                "broken_or_external_actions": 0,
                "font_resources": unit["fonts"],
                "type3_fonts": 0,
                "raster_xobjects": 0,
                "editable_tex_files": unit["tex_files"],
                "native_diagram_blocks": unit["diagrams"],
                "includegraphics_calls": 0,
                "diagram_review": unit["diagram_review"],
                "complete_sga3_claimed": False,
            }
            for unit in UNITS
        ],
        "source_zips": [
            {
                "filename": unit["zip"],
                "members": unit["zip_members"],
                "uncompressed_bytes": unit["zip_uncompressed"],
                "sha256": primary_local[unit["zip"]]["sha256"],
                "raster_or_pdf_members": 0,
                "privacy_hits": 0,
            }
            for unit in UNITS
        ],
        "zip_surface_expected": {
            "archives": EXPECTED_ZIP_ARCHIVES,
            "file_members": EXPECTED_ZIP_FILE_MEMBERS,
            "directory_entries": EXPECTED_ZIP_DIRECTORY_ENTRIES,
            "all_entries": EXPECTED_ZIP_ALL_ENTRIES,
            "uncompressed_bytes": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
        },
        "session_c_rule": {
            "existing_600_1200_evidence_invalidated": False,
            "reopen_300_only_approvals": True,
            "native_tex_required_for_new_delivery": True,
            "default_review_dpi": 5000,
            "ambiguity_review_dpi": 9000,
            "xii_closed": True,
            "xx_xxi_open": True,
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
