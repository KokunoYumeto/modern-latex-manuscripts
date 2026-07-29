#!/usr/bin/env python3
"""Publish the canonical SGA1-6 reader surface with the SGA3 R20 reader."""

from __future__ import annotations

import copy
import csv
import hashlib
import importlib.util
import io
import json
import os
import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = (
    SCRIPT_DIR
    / "publish_sga_reader_clean_complete_r19_native_iii_zenodo_20260729.py"
)
SPEC = importlib.util.spec_from_file_location("sga_r19_20260729", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA publication workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)
base = previous.base


PREDECESSOR_RECORD = 21682020
PREDECESSOR_DOI = "10.5281/zenodo.21682020"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-29"
VERSION = "2026-07-29 canonical SGA1-6 reader surface with SGA3 R20"
TITLE = "SGA 1-6: English Readers, French Texts, and TeX Archives"
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
GITHUB_COMMIT = "f0ba7012b60b42ffe702f08192377858cc4c697b"
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-complete-working-reader-clean-r20-native-expose-v-vi-"
    "20260729"
)

README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"

CANONICAL_RENAMES = {
    "00a_SGA1_English_Reader.pdf": (
        "00a_SGA1_English_CompleteVolume_"
        "Working_NoExhaustiveCertification_20260722.pdf",
        2_490_530,
        "D424E4A3E98E8C80C642BE5E5B8AAD813FF3F12D946BF53E237F6508387AC53B",
    ),
    "00b_SGA2_English_Reader.pdf": (
        "00b_SGA2_English_Complete_ReferenceLinked_R8_20260723.pdf",
        2_001_862,
        "AA8663D393CAE37D0D917E16E911F12D64AD90B90829CFCE601557AD759DEDFA",
    ),
    "00d_SGA4_English_Reader.pdf": (
        (
            "00d_SGA4_English_Proper_Exposes_I_XIX_including_Vbis_"
            "ReferenceV2_R7_20260723.pdf"
        ),
        4_420_366,
        "982DB88559FE4239CF3381D664792C2262658D511FA0A8A06FE99A1A68512BA5",
    ),
    "00e_SGA5_English_Reader.pdf": (
        "00e_SGA5_English_ReferenceLinked_R9_20260723.pdf",
        2_431_050,
        "9BB41B09624BFEB566503EAADD3276B709F9E1AC03E2F71188E0CE7E80A00A38",
    ),
    "00f_SGA6_English_Reader.pdf": (
        "00f_SGA6_English_Complete_ReferenceLinked_20260723.pdf",
        3_189_902,
        "E14FF6F4F2AD65BBCAA8410B9DF7DBD480D193A6CA97AF5F4428E7AB6B60B2FE",
    ),
    "01e_SGA5_French_Reader.pdf": (
        "01e_SGA5_French_Workpass_NotCertified_20260706.pdf",
        2_015_658,
        "977E3180CF5404DC7F0057C87551E41A7C0B87AE89BAFA5D8D40425DCD08B68A",
    ),
    "01f_SGA6_French_Reader.pdf": (
        (
            "01f_SGA6_French_SourceRescribe_"
            "Workpass_NotCertified_idx684_20260718.pdf"
        ),
        2_870_039,
        "5B42E4FA9607F9102791B744C96BF0A149B8B1404F9823AB6F1C7CC38145BAD9",
    ),
    "02a_SGA1_English_Master.tex": (
        "02a_SGA1_English_CompleteVolume_Working_Master_20260722.tex",
        27_322,
        "0E9B39EEF40BEDECB6CA61F5F5B2E7A7C277330BDC9E8AC7B93882B2920AA77C",
    ),
    "02b_SGA2_English_Master.tex": (
        "02b_SGA2_English_Complete_ReferenceLinked_R8_Master_20260723.tex",
        4_745,
        "33645D4A8481F6ADAE8CD9F17AE156D21A76C6BF9427E1AF348C28CAC23B0382",
    ),
    "02d_SGA4_English_Master.tex": (
        "02d_SGA4_English_Proper_Master_ReferenceV2_R7_20260723.tex",
        3_024,
        "CD3923F791412525A04004F7EADA9F8A088751BC6E82F254900BFFE957413658",
    ),
    "02e_SGA5_English_Master.tex": (
        "02e_SGA5_English_ReferenceLinked_R9_Master_20260723.tex",
        895_768,
        "6D3CA0C9B4050C200D875011E2B4D611EC67CD80B3C88011650E272D29DCFF48",
    ),
    "02f_SGA6_English_Master.tex": (
        "02f_SGA6_English_Complete_ReferenceLinked_Master_20260723.tex",
        3_348,
        "6CBD2794D46CB233AB9336C4C57AB7FCBEBDCE828B062FBE794EB7DE3E868ABD",
    ),
    "03e_SGA5_French_Master.tex": (
        "03e_SGA5_French_Workpass_NotCertified_20260706.tex",
        832_750,
        "29A8135906CA525F9623AA8165E57FE4C2750470461DE31910BE0BC64CF16D37",
    ),
    "03f_SGA6_French_Master.tex": (
        (
            "03f_SGA6_French_SourceRescribe_"
            "Workpass_NotCertified_idx684_20260718.tex"
        ),
        1_319_443,
        "7F32C2080A78A2746CBE52DCC1EC43A8505269F25518FA7B9A86E4E89AF858AC",
    ),
}

OLD_SGA3_FILES = {
    "00c00_SGA3_English_Complete_Reader_Native_Update_R19_20260729.pdf",
    "02c00_SGA3_English_Complete_Reader_Native_Update_R19_20260729.tex",
    "10c9_SGA3_English_Complete_Reader_Source_and_History_R19_20260729.zip",
}
SGA3_PDF = "00c_SGA3_English_Reader.pdf"
SGA3_TEX = "02c_SGA3_English_Master.tex"
SGA3_ZIP = "10c_SGA3_English_Source_and_History_R20_20260729.zip"

REPLACED_NAMES = (
    {old for old, _bytes, _sha256 in CANONICAL_RENAMES.values()}
    | OLD_SGA3_FILES
    | {README_NAME, MANIFEST_NAME, VALIDATION_NAME}
)

EXPECTED_PREDECESSOR_FILES = 68
EXPECTED_FINAL_FILES = 68
EXPECTED_RETAINED_PREDECESSOR_FILES = 48
EXPECTED_UNRELATED_RETAINED_FILES = 48
EXPECTED_MANIFEST_ROWS = 66
EXPECTED_ZIP_ARCHIVES = 49
EXPECTED_ZIP_FILE_MEMBERS = 4_250
EXPECTED_ZIP_DIRECTORY_ENTRIES = 6
EXPECTED_ZIP_ALL_ENTRIES = 4_256
EXPECTED_ZIP_UNCOMPRESSED_BYTES = 441_148_189
EXPECTED_GITHUB_READBACK_FILES = 12

REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21682020_public_readback.json"
)
PREDECESSOR_ZIP_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21682020_zip_member_readback.json"
)
TEMP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp"
STAGING_ROOT = TEMP_ROOT / "sga_canonical_reader_surface_r20_staging"
CONTROLS_ROOT = TEMP_ROOT / "sga_canonical_reader_surface_r20_controls"
READBACK_ROOT = TEMP_ROOT / "sga_canonical_reader_surface_r20_readback"
DRAFT_STATE = (
    RECEIPT_ROOT
    / "20260729_sga_canonical_reader_surface_r20_zenodo_draft_state.json"
)

PRIMARY_LOCAL_PATHS = {
    name: STAGING_ROOT / name for name in CANONICAL_RENAMES
}
PRIMARY_LOCAL_PATHS.update(
    {
        SGA3_PDF: PACKAGE_ROOT / SGA3_PDF,
        SGA3_TEX: PACKAGE_ROOT / SGA3_TEX,
        SGA3_ZIP: PACKAGE_ROOT / SGA3_ZIP,
    }
)
PRIMARY_EXPECTED = {
    name: (size, sha256)
    for name, (_old, size, sha256) in CANONICAL_RENAMES.items()
}
PRIMARY_EXPECTED.update(
    {
        SGA3_PDF: (
            6_811_667,
            "22A61E1C018EB0722635CADDAD71981EFE7BA0B01AD06ACBD7F8D0A9366FF8DB",
        ),
        SGA3_TEX: (
            22_203,
            "7E4EE9653AEB052F820841DA58D6659DED35DF0DB7655839CD06CADF2088EA73",
        ),
        SGA3_ZIP: (
            9_146_080,
            "88839938439FCD7D9FD548B43AB14890919200A533070747C45B99AEF02840C9",
        ),
    }
)

READER_METRICS = {
    "SGA1": {
        "filename": "00a_SGA1_English_Reader.pdf",
        "pages": 259,
    },
    "SGA2": {
        "filename": "00b_SGA2_English_Reader.pdf",
        "pages": 178,
    },
    "SGA3": {
        "filename": SGA3_PDF,
        "pages": 1_459,
        "named_destinations": 9_351,
        "internal_goto_actions": 4_467,
    },
    "SGA4": {
        "filename": "00d_SGA4_English_Reader.pdf",
        "pages": 864,
    },
    "SGA5": {
        "filename": "00e_SGA5_English_Reader.pdf",
        "pages": 309,
    },
    "SGA6": {
        "filename": "00f_SGA6_English_Reader.pdf",
        "pages": 376,
    },
}

NEW_MANIFEST_ROWS: dict[str, dict[str, str]] = {}
for name in PRIMARY_LOCAL_PATHS:
    if name.startswith("00"):
        role = "english_reader"
    elif name.startswith("01"):
        role = "french_reader"
    elif name.startswith("02"):
        role = "english_master_tex"
    elif name.startswith("03"):
        role = "french_master_tex"
    else:
        role = "source_and_history_archive"
    NEW_MANIFEST_ROWS[name] = {
        "role": role,
        "provenance": (
            "canonical direct reading/source object"
            if not name.lower().endswith(".zip")
            else "grouped SGA3 source closure and prior reader history"
        ),
        "status": "current" if not name.lower().endswith(".zip") else "archive",
    }
NEW_MANIFEST_ROWS[README_NAME] = {
    "role": "reader_index",
    "provenance": "plain index to the direct readers and source archives",
    "status": "current",
}

DESCRIPTION_HTML = "\n".join(
    (
        "<p>This edition presents the English SGA 1-6 readers first, in "
        "numerical order, followed by the available French texts and direct "
        "editable TeX masters. Supporting source, provenance, quality-control, "
        "and historical material is grouped in ZIP archives.</p>",
        "<p>The SGA3 reader has 1,459 A4 pages and covers the Editorial Notice, "
        "Introduction, Exposes I-XXVI, the Tome-I index, the Tome-III "
        "mathematical guide, and the terminal index. This revision integrates "
        "native-diagram replacements for Exposes V and VI.</p>",
        "<p>The direct PDFs are reading editions containing the mathematical "
        "text, diagrams, labels, links, and ordinary editorial apparatus. "
        "Detailed provenance and technical records remain available in the "
        "archives.</p>",
        "<p>These scholarly editions do not transfer rights in the underlying "
        "French works and are not presented as new critical editions. "
        "Historical Zenodo versions remain immutable.</p>",
    )
)
NOTES_HTML = (
    "<p>Canonical direct filenames are used for the SGA 1-6 readers and TeX "
    "masters. SGA1 is the default preview.</p>"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def guarded_remove(path: Path) -> None:
    if not path.exists():
        return
    resolved = path.resolve()
    if TEMP_ROOT.resolve() not in resolved.parents:
        raise RuntimeError(f"Refusing to remove a non-temporary path: {path}")
    shutil.rmtree(path)


def verify_github_readback() -> None:
    raw_root = (
        "https://raw.githubusercontent.com/"
        f"KokunoYumeto/modern-latex-manuscripts/{GITHUB_COMMIT}/"
        f"{GITHUB_PACKAGE}/"
    )
    local_files = sorted(
        (path for path in PACKAGE_ROOT.iterdir() if path.is_file()),
        key=lambda path: path.name.casefold(),
    )
    if len(local_files) != EXPECTED_GITHUB_READBACK_FILES:
        raise RuntimeError("R20 GitHub readback file boundary mismatch")
    remote_zip: bytes | None = None
    for path in local_files:
        request = urllib.request.Request(
            raw_root + path.name,
            headers={"User-Agent": "modern-latex-manuscripts-readback"},
        )
        with urllib.request.urlopen(request, timeout=300) as response:
            data = response.read()
        if (len(data), sha256_bytes(data)) != (
            path.stat().st_size,
            base.sha256_file(path),
        ):
            raise RuntimeError(f"R20 GitHub readback mismatch: {path.name}")
        if path.name == SGA3_ZIP:
            remote_zip = data
    if remote_zip is None:
        raise RuntimeError("R20 GitHub source archive readback is missing")
    with zipfile.ZipFile(io.BytesIO(remote_zip)) as archive:
        if archive.testzip() is not None or len(archive.infolist()) != 922:
            raise RuntimeError("R20 GitHub archive CRC/member mismatch")
        rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read("SOURCE_BUNDLE_SHA256.csv").decode("utf-8"),
                    newline="",
                )
            )
        )
        if len(rows) != 921:
            raise RuntimeError("R20 GitHub archive manifest boundary mismatch")
        for row in rows:
            data = archive.read(row["relative_path"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    f"R20 GitHub archive member mismatch: "
                    f"{row['relative_path']}"
                )


def download_canonical_predecessor_files() -> None:
    guarded_remove(STAGING_ROOT)
    STAGING_ROOT.mkdir(parents=True)
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8-sig"))
    for new_name, (old_name, expected_bytes, expected_sha256) in (
        CANONICAL_RENAMES.items()
    ):
        row = receipt["files"].get(old_name)
        if row is None or not row.get("match"):
            raise RuntimeError(f"Missing controlling predecessor row: {old_name}")
        if (int(row["bytes"]), row["sha256"].upper()) != (
            expected_bytes,
            expected_sha256,
        ):
            raise RuntimeError(f"Predecessor identity changed: {old_name}")
        target = STAGING_ROOT / new_name
        request = urllib.request.Request(
            row["url"],
            headers={"User-Agent": "modern-latex-manuscripts-readback"},
        )
        with urllib.request.urlopen(request, timeout=600) as response:
            with target.open("wb") as handle:
                shutil.copyfileobj(response, handle, 4 * 1024 * 1024)
        if (target.stat().st_size, base.sha256_file(target)) != (
            expected_bytes,
            expected_sha256,
        ):
            raise RuntimeError(f"Canonical rename readback mismatch: {new_name}")


def verify_primary_local_files() -> dict[str, dict]:
    download_canonical_predecessor_files()
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
            raise RuntimeError(f"Primary identity mismatch: {name}")
        result[name] = identity

    outer_manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    if (
        base.sha256_file(outer_manifest)
        != "BD089069CAB3E00D521C2577B61B8C475919BCA4B3A6FDECEA1573429605EA19"
    ):
        raise RuntimeError("R20 outer manifest mismatch")
    rows = list(
        csv.DictReader(
            io.StringIO(
                outer_manifest.read_text(encoding="utf-8-sig"),
                newline="",
            )
        )
    )
    if len(rows) != 11:
        raise RuntimeError("R20 outer manifest boundary mismatch")
    for row in rows:
        path = PACKAGE_ROOT / row["filename"]
        if (path.stat().st_size, base.sha256_file(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"R20 outer manifest mismatch: {row['filename']}")

    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    reader = validation.get("reader", {})
    archive = validation.get("source_archive", {})
    if (
        validation.get("status") != "PASS"
        or validation.get("errors") != []
        or reader.get("pages") != 1_459
        or reader.get("named_destinations") != 9_351
        or reader.get("internal_goto_actions") != 4_467
        or reader.get("invalid_actions") != 0
        or reader.get("uri_actions") != 0
        or reader.get("reader_process_term_hits") != []
        or archive.get("members") != 922
        or archive.get("manifest_rows") != 921
        or archive.get("errors") != []
    ):
        raise RuntimeError("R20 package validation mismatch")

    verify_github_readback()
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
    if (len(content), sha256_bytes(content)) != (
        int(wanted["bytes"]),
        wanted["sha256"].upper(),
    ):
        raise RuntimeError("Predecessor release-manifest mismatch")
    rows = list(
        csv.DictReader(
            io.StringIO(content.decode("utf-8-sig"), newline="")
        )
    )
    if len(rows) != 66:
        raise RuntimeError("Predecessor release-manifest boundary mismatch")
    return rows


def create_or_resume_draft(session, token: str, predecessor: dict) -> int:
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {
        **auth,
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    existing = session.get(
        f"{base.API}/records/{PREDECESSOR_RECORD}/draft",
        headers=vendor,
        timeout=(30, 180),
    )
    if existing.status_code == 200:
        if not DRAFT_STATE.is_file():
            raise RuntimeError(
                "An untracked successor draft already exists; refusing a "
                "second or blind mutation"
            )
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        draft = existing.json()
        draft_id = int(draft["id"])
        if (
            draft_id != int(state["draft_id"])
            or base.concept_doi(draft) != CONCEPT_DOI
            or int(state["predecessor_record"]) != PREDECESSOR_RECORD
        ):
            raise RuntimeError("Existing successor is not the tracked draft")
        return draft_id
    base.check(existing, {404})

    if DRAFT_STATE.is_file():
        state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError(
                "Tracked successor is already published; use readback recovery"
            )
        raise RuntimeError("Tracked draft state exists but Zenodo draft is absent")

    legacy = base.check(
        session.get(
            f"{base.API}/deposit/depositions/{PREDECESSOR_RECORD}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        legacy.get("state") != "done"
        or not legacy.get("submitted")
        or not legacy.get("links", {}).get("newversion")
    ):
        raise RuntimeError("Predecessor is not a submitted versioning base")
    created = base.check(
        session.post(
            legacy["links"]["newversion"],
            headers=auth,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    deposit = base.check(
        session.get(
            created["links"]["latest_draft"],
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    draft_id = int(deposit["id"])
    if set(base.legacy_file_map(deposit)) != set(
        base.entries_map(predecessor)
    ):
        raise RuntimeError("New-version draft did not inherit the predecessor")
    base.save_json(
        DRAFT_STATE,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "predecessor_record": PREDECESSOR_RECORD,
            "draft_id": draft_id,
            "concept_doi": CONCEPT_DOI,
            "published": False,
        },
    )
    return draft_id


def readme_text(draft_id: int) -> str:
    return f"""# SGA 1-6

## English readers

- `00a_SGA1_English_Reader.pdf`
- `00b_SGA2_English_Reader.pdf`
- `00c_SGA3_English_Reader.pdf`
- `00d_SGA4_English_Reader.pdf`
- `00e_SGA5_English_Reader.pdf`
- `00f_SGA6_English_Reader.pdf`

The SGA3 reader has 1,459 A4 pages and includes the Editorial Notice,
Introduction, Exposes I-XXVI, the Tome-I index, the Tome-III mathematical
guide, and the terminal index.

## French texts

Direct French reader and TeX files are present for SGA5 and SGA6.

## Editable sources and archives

The `02*` files are the direct English master TeX files. The `03*` files are
the available direct French master TeX files. Supporting source, provenance,
quality-control, and historical material is grouped in the `10*`, `11*`, and
`12*` ZIP archives.

The editions preserve their mathematical text, diagrams, links, and ordinary
editorial apparatus. Rights in the underlying works remain with their
respective holders. Historical versions remain available through Zenodo. The
corresponding source package is mirrored in the project's GitHub repository.

Zenodo successor reserved from record {PREDECESSOR_RECORD}: {draft_id}.
"""


def generate_controls(
    draft_id: int,
    predecessor_rows: list[dict[str, str]],
    predecessor_identities: dict[str, dict],
    primary_local: dict[str, dict],
) -> dict[str, dict]:
    guarded_remove(CONTROLS_ROOT)
    CONTROLS_ROOT.mkdir(parents=True)

    readme_path = CONTROLS_ROOT / README_NAME
    readme_path.write_text(readme_text(draft_id), encoding="utf-8")
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
            raise RuntimeError(f"Retained identity mismatch: {name}")
        release_rows.append(
            {
                "filename": name,
                "bytes": str(identity["bytes"]),
                "sha256": identity["sha256"],
                "role": "supporting_archive",
                "provenance": (
                    f"retained byte-identically from Zenodo record "
                    f"{PREDECESSOR_RECORD}"
                ),
                "status": "archive",
            }
        )

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
                **metadata,
            }
        )
    release_rows.sort(key=lambda row: row["filename"].casefold())
    if len(release_rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Generated release-manifest boundary mismatch")
    if len({row["filename"] for row in release_rows}) != len(release_rows):
        raise RuntimeError("Generated release manifest has duplicate names")

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
        "schema": "sga_canonical_reader_surface_r20_v1",
        "status": "PASS",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "reserved_successor_record": draft_id,
        "github": {
            "commit": GITHUB_COMMIT,
            "package": GITHUB_PACKAGE,
            "outer_files_verified": EXPECTED_GITHUB_READBACK_FILES,
            "source_archive_members_verified": 922,
            "source_archive_manifest_rows_verified": 921,
            "errors": [],
        },
        "predecessor_files": EXPECTED_PREDECESSOR_FILES,
        "retained_archive_files": EXPECTED_RETAINED_PREDECESSOR_FILES,
        "canonical_direct_files": 16,
        "sga3_source_archive": {
            "filename": SGA3_ZIP,
            "bytes": primary_local[SGA3_ZIP]["bytes"],
            "sha256": primary_local[SGA3_ZIP]["sha256"],
            "members": 922,
            "manifest_rows": 921,
        },
        "final_files": EXPECTED_FINAL_FILES,
        "manifest_rows": EXPECTED_MANIFEST_ROWS,
        "default_preview": DEFAULT_PREVIEW,
        "readers": {
            sga: {
                **metrics,
                "bytes": primary_local[metrics["filename"]]["bytes"],
                "sha256": primary_local[metrics["filename"]]["sha256"],
            }
            for sga, metrics in READER_METRICS.items()
        },
        "zip_surface_expected": {
            "archives": EXPECTED_ZIP_ARCHIVES,
            "file_members": EXPECTED_ZIP_FILE_MEMBERS,
            "directory_entries": EXPECTED_ZIP_DIRECTORY_ENTRIES,
            "all_entries": EXPECTED_ZIP_ALL_ENTRIES,
            "uncompressed_bytes": EXPECTED_ZIP_UNCOMPRESSED_BYTES,
        },
        "privacy_hits": [],
        "duplicate_concept_created": False,
        "second_draft_created": False,
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


def assert_metadata(metadata: dict) -> None:
    if metadata.get("title") != TITLE:
        raise RuntimeError("Title metadata mismatch")
    if metadata.get("version") != VERSION:
        raise RuntimeError("Version metadata mismatch")
    if metadata.get("publication_date") != PUBLICATION_DATE:
        raise RuntimeError("Publication-date metadata mismatch")
    if metadata.get("description") != DESCRIPTION_HTML:
        raise RuntimeError("Description metadata mismatch")
    if not any(
        row.get("description") == NOTES_HTML
        for row in metadata.get("additional_descriptions", [])
    ):
        raise RuntimeError("Release-notes metadata mismatch")


def publish_draft(
    session,
    token: str,
    draft_id: int,
    expected: dict[str, dict],
) -> dict:
    draft = base.modern_draft(session, token, draft_id)
    if set(draft["files"]["entries"]) != set(expected):
        raise RuntimeError("Cannot publish: modern draft set mismatch")

    metadata = copy.deepcopy(draft["metadata"])
    metadata["title"] = TITLE
    metadata["version"] = VERSION
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["description"] = DESCRIPTION_HTML
    base.patch_notes(metadata)
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": sorted(expected, key=str.casefold),
        },
        "metadata": metadata,
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
        "Content-Type": "application/json",
    }
    patched = base.check(
        session.put(
            f"{base.API}/records/{draft_id}/draft",
            headers=headers,
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    assert_metadata(patched["metadata"])
    reread = base.modern_draft(session, token, draft_id)
    assert_metadata(reread["metadata"])
    if reread["files"].get("default_preview") != DEFAULT_PREVIEW:
        raise RuntimeError("Draft default preview mismatch")
    if set(reread["files"]["entries"]) != set(expected):
        raise RuntimeError("Draft lost exact file set after metadata patch")

    published = base.check(
        session.post(
            reread["links"]["publish"],
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.inveniordm.v1+json",
            },
            timeout=(30, 600),
        ),
        {200, 202},
    ).json()
    if (
        int(published["id"]) != draft_id
        or base.concept_doi(published) != CONCEPT_DOI
    ):
        raise RuntimeError("Published response escaped the existing concept")
    doi = base.version_doi(published)
    state = json.loads(DRAFT_STATE.read_text(encoding="utf-8"))
    state.update({"published": True, "doi": doi})
    base.save_json(DRAFT_STATE, state)
    receipt = {
        "status": "PUBLISH_ACCEPTED",
        "errors": [],
        "record_id": draft_id,
        "doi": doi,
        "concept_doi": CONCEPT_DOI,
        "file_count": EXPECTED_FINAL_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    base.save_json(
        RECEIPT_ROOT
        / (
            "20260729_sga_canonical_reader_surface_r20_record_"
            f"{draft_id}_publish_response.json"
        ),
        receipt,
    )
    return receipt


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
    "RECEIPT_ROOT": RECEIPT_ROOT,
    "PREDECESSOR_RECEIPT": PREDECESSOR_RECEIPT,
    "CONTROLS_ROOT": CONTROLS_ROOT,
    "READBACK_ROOT": READBACK_ROOT,
    "DRAFT_STATE": DRAFT_STATE,
    "PRIMARY_LOCAL_PATHS": PRIMARY_LOCAL_PATHS,
    "NEW_MANIFEST_ROWS": NEW_MANIFEST_ROWS,
    "DESCRIPTION_HTML": DESCRIPTION_HTML,
    "NOTES_HTML": NOTES_HTML,
    "DEFAULT_PREVIEW": DEFAULT_PREVIEW,
}.items():
    setattr(base, name, value)

base.verify_primary_local_files = verify_primary_local_files
base.fetch_predecessor_manifest = fetch_predecessor_manifest
base.create_or_resume_draft = create_or_resume_draft
base.readme_text = readme_text
base.generate_controls = generate_controls
base.assert_metadata = assert_metadata
base.publish_draft = publish_draft


if __name__ == "__main__":
    try:
        base.main()
    finally:
        guarded_remove(STAGING_ROOT)
