#!/usr/bin/env python3
"""Publish the reader-pure SGA3 R26 and SGA6 R10 successor."""

from __future__ import annotations

import copy
import csv
import hashlib
import importlib.util
import io
import json
import shutil
import subprocess
import sys
import urllib.request
import zipfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = SCRIPT_DIR / "publish_sga2_reader_clean_r9_zenodo_20260729.py"
SPEC = importlib.util.spec_from_file_location("sga_reader_clean_r9", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA publication workflow")
previous = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = previous
SPEC.loader.exec_module(previous)
base = previous.base


PREDECESSOR_RECORD = 21695622
PREDECESSOR_DOI = "10.5281/zenodo.21695622"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PUBLICATION_DATE = "2026-07-30"
VERSION = (
    "2026-07-30 compact SGA1-6 reader surface "
    "(SGA3 R26 and SGA6 R10 reader-pure successors)"
)
TITLE = previous.TITLE
DEFAULT_PREVIEW = previous.DEFAULT_PREVIEW

DESCRIPTION_HTML = "\n".join(
    (
        "<p>English readers for SGA 1 through SGA 6 are listed first in "
        "numerical order. Available French texts and editable TeX masters "
        "follow; supplementary source and historical files are grouped in "
        "ZIP archives.</p>",
        "<p>The preferred SGA3 English reader has 1,470 A4 pages and contains "
        "the Introduction, Exposes I-XXVI, the Tome-I subject index, the "
        "Tome-III mathematical guide, and the terminal index. Its reader "
        "pages contain mathematics and genuine source-era scholarly "
        "apparatus, without project, AI, workflow, production-status, or "
        "project-written source-reading narration.</p>",
        "<p>The preferred SGA6 English reader has 376 A4 pages and covers the "
        "complete layered English corpus through the end of the available "
        "source. Its direct reader likewise omits project source-correction "
        "notes, internal defect identifiers, and production commentary while "
        "retaining genuine source-era authorial and editorial apparatus.</p>",
        "<p>Removed production notes remain available only inside the grouped "
        "editable-source archives. The SGA3 R26 archive contains 922 exact "
        "file members; the SGA6 R10 archive contains 22 exact file members. "
        "Earlier Zenodo versions remain immutable history.</p>",
        "<p>These are working English translations and TeX editions, not "
        "critical editions or rights determinations. They do not transfer "
        "rights in the underlying French works.</p>",
    )
)

GITHUB_COMMIT = subprocess.check_output(
    ["git", "rev-parse", "HEAD"], cwd=SCRIPT_DIR.parent
).decode("ascii").strip()
GITHUB_PACKAGE = (
    "sources/sga/"
    "sga3-english-reader-pure-r26-no-project-notes-20260730"
)
GITHUB_PACKAGE_SGA4 = (
    "sources/sga/"
    "sga6-english-reader-pure-r10-no-project-notes-20260730"
)
REPO_ROOT = SCRIPT_DIR.parent
PACKAGE_ROOT = REPO_ROOT / GITHUB_PACKAGE
PACKAGE_ROOT_SGA4 = REPO_ROOT / GITHUB_PACKAGE_SGA4

SGA3_PDF = "00c_SGA3_English_Reader.pdf"
SGA3_TEX = "02c_SGA3_English_Master.tex"
OLD_SGA3_ZIP = "10c_SGA3_English_Source_R25_20260730.zip"
SGA3_ZIP = "10c_SGA3_English_Source_R26_20260730.zip"
SGA4_PDF = "00f_SGA6_English_Reader.pdf"
SGA4_TEX = "02f_SGA6_English_Master.tex"
OLD_SGA4_ZIP = "10g_SGA6_English_Complete_ReferenceLinked_TeX_Ledgers_20260723.zip"
SGA4_ZIP = "10f_SGA6_English_Source_R10_20260730.zip"
OLD_CONTROLS_ZIP = "10z_SGA_Current_Release_Controls_20260730.zip"
CONTROLS_ZIP = "10z_SGA_Current_Release_Controls_20260730.zip"

README_NAME = "09_README_CURRENT_RELEASE.md"
MANIFEST_NAME = "09a_RELEASE_FILE_MANIFEST.csv"
VALIDATION_NAME = "09b_RELEASE_VALIDATION.json"
PACKAGE_VALIDATION_NAME = "09c_SGA3_PACKAGE_VALIDATION.json"
PACKAGE_MANIFEST_NAME = "09d_SGA3_PACKAGE_SHA256SUMS.csv"
SGA4_PACKAGE_VALIDATION_NAME = "09e_SGA6_PACKAGE_VALIDATION.json"
SGA4_PACKAGE_MANIFEST_NAME = "09f_SGA6_PACKAGE_SHA256SUMS.csv"
PACKED_MANIFEST_NAME = "PACKED_CONTROL_SHA256.csv"

REPLACED_NAMES = {
    SGA3_PDF,
    OLD_SGA3_ZIP,
    SGA4_PDF,
    SGA4_TEX,
    OLD_SGA4_ZIP,
    OLD_CONTROLS_ZIP,
}
PRIMARY_LOCAL_PATHS = {
    SGA3_PDF: PACKAGE_ROOT / SGA3_PDF,
    SGA3_ZIP: PACKAGE_ROOT / SGA3_ZIP,
    SGA4_PDF: PACKAGE_ROOT_SGA4 / SGA4_PDF,
    SGA4_TEX: PACKAGE_ROOT_SGA4 / SGA4_TEX,
    SGA4_ZIP: PACKAGE_ROOT_SGA4 / SGA4_ZIP,
}
PRIMARY_EXPECTED = {
    SGA3_PDF: (
        6_363_561,
        "00A6EEBD15993BE4A438FF3D986D4C7DC35ED5FC1CEBD0F2D8DC172FD74E3E23",
    ),
    SGA3_ZIP: (
        1_977_460,
        "4386142ACC744C0077F878EB3A5AED88EE9A7C4AA58673486A600CA8460E1800",
    ),
    SGA4_PDF: (
        3_189_979,
        "08848062CF081E39E7F57E60CB31C1BFECFD1225DAF6DE99458A660B2A53600A",
    ),
    SGA4_TEX: (
        3_377,
        "9958DA143FF9AC52FD8B2FD0A78721136D5FC66528DB08D8CC675C7F4E041E7C",
    ),
    SGA4_ZIP: (
        569_577,
        "2DDC0BEF54A2CDB1E67FD573AE291BCA5A55B209BF64E6425E59CC06AE734B29",
    ),
}

PACKAGE_MANIFEST_IDENTITIES = {
    GITHUB_PACKAGE: (
        936,
        "2DF73367ED2F603F29E5E3C9EC786BD76F7E982AB426AEDD0B2CCC6214CC641F",
    ),
    GITHUB_PACKAGE_SGA4: (
        750,
        "94E7782B594AF9F94B86C2826844103DE809996A999F89E4F8E2E350B4657796",
    ),
}
PACKAGE_VALIDATION_IDENTITIES = {
    GITHUB_PACKAGE: (
        1_486,
        "D0E79EA660BDB400B8AE373FAD60F0177E65ECB81DF3E3565B5DE80D54B0A69F",
    ),
    GITHUB_PACKAGE_SGA4: (
        1_420,
        "A8D9A21B71CD66D1B437A36F40CAA572B9FCF4D0AFC60D6462FB67A2682FCE44",
    ),
}
SOURCE_ZIPS = {
    SGA3_ZIP: {
        "path": PACKAGE_ROOT / SGA3_ZIP,
        "members": 922,
        "manifest_rows": 921,
        "uncompressed_bytes": 5_318_533,
        "manifest_sha256": (
            "7465751803229F0CBB5A380D047FCD158017D7C780AEF0C17BDC69D61C95B95C"
        ),
    },
    SGA4_ZIP: {
        "path": PACKAGE_ROOT_SGA4 / SGA4_ZIP,
        "members": 22,
        "manifest_rows": 21,
        "uncompressed_bytes": 2_179_554,
        "manifest_sha256": (
            "F89292E6B39B010E7B4B176B10774C495ED7AAC10AE3AEAC9780C98D7480BB81"
        ),
    },
}

EXPECTED_PREDECESSOR_FILES = 66
EXPECTED_FINAL_FILES = 66
EXPECTED_RETAINED_PREDECESSOR_FILES = 60
EXPECTED_UNRELATED_RETAINED_FILES = 60
EXPECTED_MANIFEST_ROWS = 65
EXPECTED_GITHUB_READBACK_FILES = 18

RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
PREDECESSOR_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21695622_public_readback.json"
)
PREDECESSOR_ZIP_RECEIPT = (
    RECEIPT_ROOT
    / "20260728_sga3_cumulative_with_x_record_21695622_zip_member_readback.json"
)
TEMP_ROOT = previous.TEMP_ROOT
CONTROLS_ROOT = TEMP_ROOT / "sga_reader_pure_r26_r10_zenodo_controls"
READBACK_ROOT = TEMP_ROOT / "sga_reader_pure_r26_r10_zenodo_readback"
DRAFT_STATE = (
    RECEIPT_ROOT / "20260730_sga_reader_pure_r26_r10_zenodo_draft_state.json"
)
NEW_MANIFEST_ROWS: dict[str, dict] = {}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, base.sha256_file(path)


def read_csv_bytes(data: bytes) -> list[dict[str, str]]:
    return list(
        csv.DictReader(io.StringIO(data.decode("utf-8-sig"), newline=""))
    )


def git_blob_bytes(package: str, filename: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{GITHUB_COMMIT}:{package}/{filename}"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
    )
    return result.stdout


def verify_github_directory(
    package: str, package_root: Path, expected_files: int
) -> None:
    files = sorted(
        (path for path in package_root.iterdir() if path.is_file()),
        key=lambda path: path.name.casefold(),
    )
    if len(files) != expected_files:
        raise RuntimeError("GitHub package boundary mismatch")
    raw_root = (
        "https://raw.githubusercontent.com/"
        f"KokunoYumeto/modern-latex-manuscripts/{GITHUB_COMMIT}/"
        f"{package}/"
    )
    for path in files:
        committed = git_blob_bytes(package, path.name)
        request = urllib.request.Request(
            raw_root + path.name,
            headers={"User-Agent": "modern-latex-manuscripts-readback"},
        )
        with urllib.request.urlopen(request, timeout=600) as response:
            remote = response.read()
        if remote != committed:
            raise RuntimeError(f"GitHub readback mismatch: {path.name}")


def verify_primary_local_files() -> dict[str, dict]:
    package_specs = (
        (GITHUB_PACKAGE, PACKAGE_ROOT, 10, 9),
        (GITHUB_PACKAGE_SGA4, PACKAGE_ROOT_SGA4, 8, 7),
    )
    validations = {}
    for package, root, outer_files, manifest_rows in package_specs:
        verify_github_directory(package, root, outer_files)
        manifest_data = git_blob_bytes(package, "SHA256SUMS.csv")
        if (
            len(manifest_data),
            sha256_bytes(manifest_data),
        ) != PACKAGE_MANIFEST_IDENTITIES[package]:
            raise RuntimeError(f"Public package manifest mismatch: {package}")
        rows = read_csv_bytes(manifest_data)
        if len(rows) != manifest_rows:
            raise RuntimeError(f"Public package manifest rows: {package}")
        for row in rows:
            data = git_blob_bytes(package, row["path"])
            if (len(data), sha256_bytes(data)) != (
                int(row["bytes"]),
                row["sha256"].upper(),
            ):
                raise RuntimeError(
                    f"Public package member mismatch: {package}/{row['path']}"
                )

        validation_data = git_blob_bytes(package, "PACKAGE_VALIDATION.json")
        if (
            len(validation_data),
            sha256_bytes(validation_data),
        ) != PACKAGE_VALIDATION_IDENTITIES[package]:
            raise RuntimeError(f"Package validation mismatch: {package}")
        validations[package] = json.loads(validation_data.decode("utf-8"))

    sga3 = validations[GITHUB_PACKAGE]
    sga6 = validations[GITHUB_PACKAGE_SGA4]
    sga3_reader = sga3.get("reader", {})
    sga6_reader = sga6.get("reader", {})
    if (
        sga3.get("status") != "PASS_DIRECT_READER_PURE_R26"
        or sga3.get("errors") != []
        or sga3_reader.get("pages") != 1_470
        or sga3_reader.get("named_destinations") != 9_378
        or sga3_reader.get("internal_goto_actions") != 4_915
        or sga3_reader.get("invalid_or_other_actions") != 0
        or sga3_reader.get("uri_actions") != 0
        or sga3_reader.get("raster_image_pages") != []
        or any(sga3_reader.get("hygiene_hits", {}).values())
        or sga3.get("reader_hygiene", {}).get("new_wrappers") != 40
        or sga3.get("reader_hygiene", {}).get("total_wrappers") != 142
    ):
        raise RuntimeError("SGA3 R26 package validation content mismatch")
    if (
        sga6.get("status") != "PASS_DIRECT_READER_PURE_R10"
        or sga6.get("errors") != []
        or sga6_reader.get("pages") != 376
        or sga6_reader.get("named_destinations") != 3_424
        or sga6_reader.get("internal_goto_actions") != 2_300
        or sga6_reader.get("invalid_or_other_actions") != 0
        or sga6_reader.get("uri_actions") != 0
        or sga6_reader.get("raster_image_pages") != []
        or any(sga6_reader.get("hygiene_hits", {}).values())
        or sga6.get("reader_hygiene", {}).get("replacements") != 5
        or sga6.get("reader_hygiene", {}).get("history_files") != 1
    ):
        raise RuntimeError("SGA6 R10 package validation content mismatch")

    for name, spec in SOURCE_ZIPS.items():
        with zipfile.ZipFile(spec["path"], "r") as archive:
            if archive.testzip() is not None:
                raise RuntimeError(f"Source ZIP CRC failure: {name}")
            infos = archive.infolist()
            files = [info for info in infos if not info.is_dir()]
            directories = [info for info in infos if info.is_dir()]
            for info in infos:
                base.safe_zip_name(info.filename)
            if (
                len(files),
                len(directories),
                sum(info.file_size for info in files),
            ) != (
                spec["members"],
                0,
                spec["uncompressed_bytes"],
            ):
                raise RuntimeError(f"Source ZIP boundary mismatch: {name}")
            manifest = archive.read("SOURCE_SHA256SUMS.csv")
            source_rows = read_csv_bytes(manifest)
            if (
                len(source_rows) != spec["manifest_rows"]
                or sha256_bytes(manifest) != spec["manifest_sha256"]
            ):
                raise RuntimeError(f"Source ZIP manifest mismatch: {name}")
            for row in source_rows:
                data = archive.read(row["path"])
                if (len(data), sha256_bytes(data)) != (
                    int(row["bytes"]),
                    row["sha256"].upper(),
                ):
                    raise RuntimeError(
                        f"Source ZIP member mismatch: {name}/{row['path']}"
                    )

    result = {}
    for name, path in PRIMARY_LOCAL_PATHS.items():
        observed = identity(path)
        if observed != PRIMARY_EXPECTED[name]:
            raise RuntimeError(f"Primary local identity mismatch: {name}")
        result[name] = {
            "path": path,
            "bytes": observed[0],
            "sha256": observed[1],
            "md5": base.md5_file(path),
        }
    return result


def fetch_predecessor_manifest(
    session, predecessor: dict, receipt: dict
) -> list[dict[str, str]]:
    entry = base.entries_map(predecessor)[OLD_CONTROLS_ZIP]
    response = base.check(
        session.get(entry["links"]["content"], timeout=(30, 180)),
        {200},
    )
    data = response.content
    wanted = receipt["files"][OLD_CONTROLS_ZIP]
    if (len(data), sha256_bytes(data)) != (
        int(wanted["bytes"]),
        wanted["sha256"].upper(),
    ):
        raise RuntimeError("Predecessor controls ZIP readback mismatch")
    with zipfile.ZipFile(io.BytesIO(data), "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Predecessor controls ZIP CRC mismatch")
        rows = read_csv_bytes(archive.read(MANIFEST_NAME))
    if len(rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Predecessor packed manifest boundary mismatch")
    return rows


def csv_bytes(rows: list[dict[str, object]], fields: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=True, indent=2) + "\n").encode("utf-8")


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def build_controls_zip(files: dict[str, bytes], target: Path) -> None:
    if target.exists():
        target.unlink()
    with zipfile.ZipFile(
        target, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for name in sorted(files, key=str.casefold):
            base.safe_zip_name(name)
            info = zipfile.ZipInfo(name, date_time=(2026, 7, 30, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, files[name])


def generate_controls(
    draft_id: int,
    predecessor_rows: list[dict[str, str]],
    predecessor_identities: dict[str, dict],
    primary_local: dict[str, dict],
) -> dict[str, dict]:
    if draft_id <= PREDECESSOR_RECORD:
        raise RuntimeError("Reserved successor record is not newer")
    if len(predecessor_rows) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Predecessor packed manifest rows changed")
    if len(predecessor_identities) != EXPECTED_PREDECESSOR_FILES:
        raise RuntimeError("Predecessor identity boundary changed")
    if set(primary_local) != set(PRIMARY_LOCAL_PATHS):
        raise RuntimeError("R26/R10 primary local set changed")

    retained = {
        name: row
        for name, row in predecessor_identities.items()
        if name not in REPLACED_NAMES
    }
    prospective = {**retained, **primary_local}
    if len(prospective) != EXPECTED_MANIFEST_ROWS:
        raise RuntimeError("Prospective release-manifest boundary mismatch")

    previous_rows = {row["filename"]: row for row in predecessor_rows}
    if len(previous_rows) != len(predecessor_rows):
        raise RuntimeError("Duplicate predecessor release-manifest filename")
    rows = []
    for name in sorted(prospective, key=str.casefold):
        item = prospective[name]
        if name == SGA3_PDF:
            role = "english_reader"
            provenance = (
                "reader-pure R26 1470-page cumulative SGA3 English reader; "
                f"GitHub commit {GITHUB_COMMIT}"
            )
        elif name == SGA3_ZIP:
            role = "source_archive"
            provenance = (
                "compact exact 922-file-member SGA3 R26 editable source and "
                f"public QA archive; GitHub commit {GITHUB_COMMIT}"
            )
        elif name == SGA4_PDF:
            role = "english_reader"
            provenance = (
                "reader-pure R10 376-page complete layered SGA6 English reader; "
                f"GitHub commit {GITHUB_COMMIT}"
            )
        elif name == SGA4_TEX:
            role = "english_tex"
            provenance = (
                "reader-pure R10 SGA6 editable master; "
                f"GitHub commit {GITHUB_COMMIT}"
            )
        elif name == SGA4_ZIP:
            role = "source_archive"
            provenance = (
                "compact exact 22-file-member SGA6 R10 editable source and "
                f"public QA archive; GitHub commit {GITHUB_COMMIT}"
            )
        else:
            prior = previous_rows.get(name)
            if prior is None:
                raise RuntimeError(f"Missing retained manifest row: {name}")
            role = prior["role"]
            provenance = prior["provenance"]
        rows.append(
            {
                "filename": name,
                "bytes": item["bytes"],
                "sha256": item["sha256"],
                "role": role,
                "provenance": provenance,
                "status": "current",
            }
        )

    if CONTROLS_ROOT.exists():
        resolved = CONTROLS_ROOT.resolve()
        temp_root = Path(base.os.environ["LOCALAPPDATA"]).resolve() / "Temp"
        if temp_root not in resolved.parents:
            raise RuntimeError("Refusing to replace controls outside local temp")
        shutil.rmtree(CONTROLS_ROOT)
    CONTROLS_ROOT.mkdir(parents=True)

    readme = f"""# Current compact SGA release

This is a same-concept successor to Zenodo record {PREDECESSOR_RECORD}. It
retains 60 files byte-for-byte and replaces only the preferred SGA3 and SGA6
readers, the SGA6 editable master, their current source ZIPs, and the release
controls ZIP. The SGA3 direct editable master is retained byte-for-byte. The
reserved successor record is {draft_id}.

The preferred SGA3 reader contains the Introduction, Exposes I-XXVI, the
Tome-I subject index, the Tome-III mathematical guide, and terminal index in
1,470 A4 pages. The preferred SGA6 reader contains the complete layered English
corpus through the end of the available source in 376 A4 pages. Their direct
reader pages contain mathematics and genuine source-era scholarly apparatus
without project, AI, workflow, production-status, internal-defect, or
project-written source-reading narration.

The removed production notes remain in archive-only source blocks. The exact
922-member SGA3 R26 source archive and 22-member SGA6 R10 source archive carry
the editable sources and concise QA records. Older versions remain immutable
history. These are working translations and TeX editions, not critical
editions, peer review, accessibility certification, or rights determinations.
"""
    manifest_data = csv_bytes(
        rows,
        ["filename", "bytes", "sha256", "role", "provenance", "status"],
    )
    package_validation = git_blob_bytes(
        GITHUB_PACKAGE, "PACKAGE_VALIDATION.json"
    )
    package_manifest = git_blob_bytes(GITHUB_PACKAGE, "SHA256SUMS.csv")
    sga4_package_validation = git_blob_bytes(
        GITHUB_PACKAGE_SGA4, "PACKAGE_VALIDATION.json"
    )
    sga4_package_manifest = git_blob_bytes(
        GITHUB_PACKAGE_SGA4, "SHA256SUMS.csv"
    )
    validation = {
        "status": "PASS",
        "errors": [],
        "source_record": PREDECESSOR_RECORD,
        "reserved_successor_record": draft_id,
        "concept_doi": CONCEPT_DOI,
        "prospective_files": EXPECTED_FINAL_FILES,
        "release_manifest_rows": EXPECTED_MANIFEST_ROWS,
        "retained_files": EXPECTED_RETAINED_PREDECESSOR_FILES,
        "replaced_files": sorted(REPLACED_NAMES, key=str.casefold),
        "new_files": sorted(
            [
                SGA3_PDF,
                SGA3_ZIP,
                SGA4_PDF,
                SGA4_TEX,
                SGA4_ZIP,
                CONTROLS_ZIP,
            ],
            key=str.casefold,
        ),
        "default_preview": DEFAULT_PREVIEW,
        "readers": {
            "sga3": {
                "filename": SGA3_PDF,
                "bytes": PRIMARY_EXPECTED[SGA3_PDF][0],
                "sha256": PRIMARY_EXPECTED[SGA3_PDF][1],
                "pages": 1_470,
                "named_destinations": 9_378,
                "internal_goto_actions": 4_915,
                "invalid_or_other_actions": 0,
                "uri_actions": 0,
                "raster_image_pages": 0,
                "visible_project_ai_workflow_source_status_hits": 0,
                "new_archive_only_wrappers": 40,
                "total_archive_only_wrappers": 142,
            },
            "sga6": {
                "filename": SGA4_PDF,
                "bytes": PRIMARY_EXPECTED[SGA4_PDF][0],
                "sha256": PRIMARY_EXPECTED[SGA4_PDF][1],
                "pages": 376,
                "named_destinations": 3_424,
                "internal_goto_actions": 2_300,
                "invalid_or_other_actions": 0,
                "uri_actions": 0,
                "raster_image_pages": 0,
                "visible_project_ai_workflow_source_status_hits": 0,
                "reader_facing_replacements": 5,
                "history_files": 1,
            },
        },
        "source_zips": {
            "sga3": {
                "filename": SGA3_ZIP,
                "bytes": PRIMARY_EXPECTED[SGA3_ZIP][0],
                "sha256": PRIMARY_EXPECTED[SGA3_ZIP][1],
                "members": SOURCE_ZIPS[SGA3_ZIP]["members"],
                "manifest_rows": SOURCE_ZIPS[SGA3_ZIP]["manifest_rows"],
                "uncompressed_bytes": (
                    SOURCE_ZIPS[SGA3_ZIP]["uncompressed_bytes"]
                ),
                "identity_errors": 0,
            },
            "sga6": {
                "filename": SGA4_ZIP,
                "bytes": PRIMARY_EXPECTED[SGA4_ZIP][0],
                "sha256": PRIMARY_EXPECTED[SGA4_ZIP][1],
                "members": SOURCE_ZIPS[SGA4_ZIP]["members"],
                "manifest_rows": SOURCE_ZIPS[SGA4_ZIP]["manifest_rows"],
                "uncompressed_bytes": (
                    SOURCE_ZIPS[SGA4_ZIP]["uncompressed_bytes"]
                ),
                "identity_errors": 0,
            },
        },
        "privacy_hits": [],
        "new_license_grant": False,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    control_files = {
        README_NAME: readme.encode("utf-8"),
        MANIFEST_NAME: manifest_data,
        VALIDATION_NAME: json_bytes(validation),
        PACKAGE_VALIDATION_NAME: package_validation,
        PACKAGE_MANIFEST_NAME: package_manifest,
        SGA4_PACKAGE_VALIDATION_NAME: sga4_package_validation,
        SGA4_PACKAGE_MANIFEST_NAME: sga4_package_manifest,
    }
    packed_rows = []
    for name in sorted(control_files, key=str.casefold):
        data = control_files[name]
        packed_rows.append(
            {"filename": name, "bytes": len(data), "sha256": sha256_bytes(data)}
        )
    control_files[PACKED_MANIFEST_NAME] = csv_bytes(
        packed_rows, ["filename", "bytes", "sha256"]
    )
    for name, data in control_files.items():
        write_bytes(CONTROLS_ROOT / name, data)

    control_zip = CONTROLS_ROOT / CONTROLS_ZIP
    build_controls_zip(control_files, control_zip)
    with zipfile.ZipFile(control_zip, "r") as archive:
        if archive.testzip() is not None:
            raise RuntimeError("R26/R10 controls ZIP failed CRC validation")
        infos = archive.infolist()
        if len(infos) != len(control_files) or any(info.is_dir() for info in infos):
            raise RuntimeError("R26/R10 controls ZIP boundary mismatch")
        for name, data in control_files.items():
            if archive.read(name) != data:
                raise RuntimeError(
                    f"R26/R10 controls ZIP member mismatch: {name}"
                )

    control_identity = {
        "path": control_zip,
        "bytes": control_zip.stat().st_size,
        "sha256": base.sha256_file(control_zip),
        "md5": base.md5_file(control_zip),
    }
    result = {**primary_local, CONTROLS_ZIP: control_identity}

    zip_receipt = json.loads(
        PREDECESSOR_ZIP_RECEIPT.read_text(encoding="utf-8-sig")
    )
    archives = {row["filename"]: row for row in zip_receipt["archives"]}
    removed = [
        archives[OLD_SGA3_ZIP],
        archives[OLD_SGA4_ZIP],
        archives[OLD_CONTROLS_ZIP],
    ]
    new_controls_uncompressed = sum(len(data) for data in control_files.values())
    new_source_members = sum(
        int(spec["members"]) for spec in SOURCE_ZIPS.values()
    )
    new_source_uncompressed = sum(
        int(spec["uncompressed_bytes"]) for spec in SOURCE_ZIPS.values()
    )
    expected_zip = {
        "EXPECTED_ZIP_ARCHIVES": int(zip_receipt["zip_archive_count"]),
        "EXPECTED_ZIP_FILE_MEMBERS": (
            int(zip_receipt["zip_file_member_count"])
            - sum(int(row["member_count"]) for row in removed)
            + new_source_members
            + len(control_files)
        ),
        "EXPECTED_ZIP_DIRECTORY_ENTRIES": int(
            zip_receipt["zip_directory_entry_count"]
        )
        - sum(int(row["directory_entry_count"]) for row in removed),
        "EXPECTED_ZIP_ALL_ENTRIES": (
            int(zip_receipt["zip_all_entry_count"])
            - sum(int(row["all_entry_count"]) for row in removed)
            + new_source_members
            + len(control_files)
        ),
        "EXPECTED_ZIP_UNCOMPRESSED_BYTES": (
            int(zip_receipt["zip_uncompressed_bytes"])
            - sum(int(row["uncompressed_bytes"]) for row in removed)
            + new_source_uncompressed
            + new_controls_uncompressed
        ),
    }
    for name, value in expected_zip.items():
        setattr(base, name, value)
        setattr(previous, name, value)
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
    if metadata.get("contributors"):
        raise RuntimeError("Reader-facing contributor badges are forbidden")
    if any(
        row.get("type", {}).get("id") == "notes"
        for row in (metadata.get("additional_descriptions") or [])
    ):
        raise RuntimeError("Reader-facing release notes are forbidden")


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
    metadata["contributors"] = []
    metadata["additional_descriptions"] = [
        row
        for row in (metadata.get("additional_descriptions") or [])
        if row.get("type", {}).get("id") != "notes"
    ]
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
        "contributors": [],
        "notes_present": False,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    base.save_json(
        RECEIPT_ROOT
        / (
            "20260730_sga_reader_pure_r26_r10_record_"
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
    "TITLE": TITLE,
    "GITHUB_COMMIT": GITHUB_COMMIT,
    "GITHUB_PACKAGE": GITHUB_PACKAGE,
    "README_NAME": README_NAME,
    "MANIFEST_NAME": MANIFEST_NAME,
    "VALIDATION_NAME": VALIDATION_NAME,
    "REPLACED_NAMES": REPLACED_NAMES,
    "EXPECTED_PREDECESSOR_FILES": EXPECTED_PREDECESSOR_FILES,
    "EXPECTED_FINAL_FILES": EXPECTED_FINAL_FILES,
    "EXPECTED_RETAINED_PREDECESSOR_FILES": EXPECTED_RETAINED_PREDECESSOR_FILES,
    "EXPECTED_UNRELATED_RETAINED_FILES": EXPECTED_UNRELATED_RETAINED_FILES,
    "EXPECTED_MANIFEST_ROWS": EXPECTED_MANIFEST_ROWS,
    "EXPECTED_GITHUB_READBACK_FILES": EXPECTED_GITHUB_READBACK_FILES,
    "RECEIPT_ROOT": RECEIPT_ROOT,
    "PREDECESSOR_RECEIPT": PREDECESSOR_RECEIPT,
    "PREDECESSOR_ZIP_RECEIPT": PREDECESSOR_ZIP_RECEIPT,
    "CONTROLS_ROOT": CONTROLS_ROOT,
    "READBACK_ROOT": READBACK_ROOT,
    "DRAFT_STATE": DRAFT_STATE,
    "PRIMARY_LOCAL_PATHS": PRIMARY_LOCAL_PATHS,
    "NEW_MANIFEST_ROWS": NEW_MANIFEST_ROWS,
    "DESCRIPTION_HTML": DESCRIPTION_HTML,
    "DEFAULT_PREVIEW": DEFAULT_PREVIEW,
}.items():
    setattr(previous, name, value)
    setattr(base, name, value)

base.verify_primary_local_files = verify_primary_local_files
base.fetch_predecessor_manifest = fetch_predecessor_manifest
base.create_or_resume_draft = previous.create_or_resume_draft
base.generate_controls = generate_controls
base.assert_metadata = assert_metadata
base.publish_draft = publish_draft


if __name__ == "__main__":
    base.main()
