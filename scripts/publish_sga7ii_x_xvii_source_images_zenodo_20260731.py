#!/usr/bin/env python3
"""Publish and read back the compact SGA7 II X-XVII successor."""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import time
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import publish_current_reader_bundles_zenodo_20260730 as base


API = base.API
PUBLICATION_DATE = "2026-07-31"
CONCEPT_DOI = "10.5281/zenodo.20410947"
PREDECESSOR_RECORD = 21_713_912
PREDECESSOR_DOI = "10.5281/zenodo.21713912"
PREDECESSOR_FILES = 77
PREDECESSOR_BYTES = 637_474_352
FINAL_FILES = 78
DEFAULT_PREVIEW = "00a_SGA1_English_Reader.pdf"
CONTROLS_NAME = "10z_SGA_Current_Release_Controls_20260730.zip"
VERSION = "2026-07-31 SGA7 II working source transcription X-XVII"

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path(
    "sources/sga/"
    "sga7ii-french-source-transcription-working-x-xvii-recovered-20260731"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/sga7ii-x-xvii-20260731"
CONTROLS_ROOT = TEMP_ROOT / "release-controls"
CONTROLS_ZIP = TEMP_ROOT / CONTROLS_NAME
READBACK_ROOT = TEMP_ROOT / "public-readback"
STATE_PATH = TEMP_ROOT / "draft_state.json"
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
RECEIPT_TAG = "20260731_sga7ii_x_xvii_recovered_source_images"
PREDECESSOR_RECEIPT = RECEIPT_ROOT / (
    "20260731_sga7ii_x_xiv_number12_source_images_record_21713912_public_readback.json"
)
GITHUB_PACKAGE_COMMIT = "d915e207ffbaabb7b49384772f75cbb42ef35ff6"
GITHUB_RECEIPT_REL = Path(
    "manifests/published-github/"
    "20260731_sga7ii_x_xvii_recovered_working_transcription_"
    "commit_d915e207_public_readback.json"
)

OLD_PDF_NAME = "00h_SGA7II_French_Source_Transcription_Working_X-XIV_20260731.pdf"
OLD_TEX_NAME = "02h_SGA7II_French_Source_Transcription_Working_X-XIV_20260731.tex"
OLD_SOURCE_ZIP_NAME = (
    "10g2_SGA7II_French_Source_Transcription_Working_X-XIV_"
    "Reader_Source_and_WIP_20260731.zip"
)
PDF_NAME = "00h_SGA7II_French_Source_Transcription_Working_X-XVII_20260731.pdf"
TEX_NAME = "02h_SGA7II_French_Source_Transcription_Working_X-XVII_20260731.tex"
SOURCE_ZIP_NAME = (
    "10g2_SGA7II_French_Source_Transcription_Working_X-XVII_"
    "Reader_Source_and_WIP_20260731.zip"
)
IMAGE_ZIP_NAME = (
    "10h2_SGA7II_Recovered_Pages_197_198_211_212_"
    "Source_Image_Evidence_20260731.zip"
)
RELEASE_ROOT = REPO_ROOT / "tmp/pdfs/sga7ii_x_xvii_release_20260731"
LOCAL_UPLOADS = {
    PDF_NAME: PACKAGE_ROOT
    / "reader/SGA7II_French_Source_Transcription_Working_X-XVII_20260731.pdf",
    TEX_NAME: PACKAGE_ROOT
    / "source/SGA7II_French_Source_Transcription_Working_X-XVII_20260731.tex",
    SOURCE_ZIP_NAME: RELEASE_ROOT / SOURCE_ZIP_NAME,
    IMAGE_ZIP_NAME: RELEASE_ROOT / IMAGE_ZIP_NAME,
}
EXPECTED_UPLOADS = {
    PDF_NAME: (
        982_690,
        "759DC8AD961BA908ABD84AD250461B648F767E9AE79D945A58B73EB91E8EAEE0",
    ),
    TEX_NAME: (
        4_123,
        "0698CA44A5832EAE6263E69EEE082A298F62E8988830215F56BE2586878E7981",
    ),
    SOURCE_ZIP_NAME: (
        1_095_811,
        "CE318401DDCB30BD6E405913B4D79A98B822223D428BA577377CFF8E68480AF9",
    ),
    IMAGE_ZIP_NAME: (
        2_304_522,
        "4A56E92484EBC7C5E652FBAB3D1EBCE104D516B470F38C3B2D5195362357779F",
    ),
}
REPLACED_NAMES = {OLD_PDF_NAME, OLD_TEX_NAME, OLD_SOURCE_ZIP_NAME, CONTROLS_NAME}

OLD_DESCRIPTION_ADDITION = (
    "<p><strong>SGA7 II working French source transcription:</strong> this "
    "successor adds a directly readable 87-page A4 transcription of Exposes "
    "X-XIV, covering 164 consecutive source pages (scan indices 8-171 / book "
    "folios 1-164), together with the editable master and a portable reader/"
    "source ZIP. The ZIP also preserves the next 32 source pages of Expose XV "
    "as an explicitly incomplete continuation that stops mid-sentence and is "
    "not included in the reader. This is not a complete SGA7 II volume or a "
    "critical edition.</p>\n"
    "<p><strong>Actual source-image evidence:</strong> a separate archive "
    "preserves 5,033 unique source-page renders and high-detail crops generated "
    "from the publicly available 446-page Number12 scan during current "
    "transcription work. These are source-scan pixels, not screenshots of the "
    "reconstructed reader. The archive includes indexed parallel evidence for "
    "later SGA7 II pages as well as X-XIV; later-page image presence does not "
    "claim later text completion. The parent scan identity, page inference, "
    "dimensions, generator, and exact SHA-256 are recorded where recoverable.</p>"
)
OLD_NOTES_ADDITION = (
    "<p>SGA7 II Exposes X-XIV are a working French source transcription with "
    "one documented compile-only TikZ matrix repair. The PDF has no internal "
    "link annotations and includes five embedded Type 3 font resources without "
    "Unicode mappings; no accessibility or diagram-fidelity certification is "
    "claimed. SGA1 remains the default browser preview.</p>"
)

DESCRIPTION_ADDITION = (
    "<p><strong>SGA7 II working French source transcription:</strong> this "
    "successor extends the direct reader from Exposes X-XIV through Expose "
    "XVII: 130 A4 pages covering scan indices 8-260 / book folios 1-253. It "
    "also preserves an explicitly incomplete Expose XVIII continuation outside "
    "the reader. This is not a complete SGA7 II volume or critical edition.</p>\n"
    "<p><strong>Actual recovered source-image evidence:</strong> a compact "
    "archive contains four full 600-dpi source pages and six labeled 600-dpi "
    "detail crops used to recover scan indices 197, 198, 211, and 212. These "
    "are pixels derived from the publicly available Number12 scan, not reader "
    "screenshots. Page, folio, dimensions, DPI, bounding box, parent-scan hash, "
    "and exact image hashes are recorded. The existing larger high-detail "
    "Number12 image archive remains available unchanged.</p>"
)
NOTES_ADDITION = (
    "<p>SGA7 II Exposes X-XVII are a working French source transcription. "
    "Recovered pages 197, 198, 211, and 212 were checked against 600-dpi "
    "source renders and labeled crops. The PDF has no internal "
    "link annotations and includes five embedded Type 3 font resources without "
    "Unicode mappings; no accessibility or diagram-fidelity certification is "
    "claimed. SGA1 remains the default browser preview.</p>"
)


def sha256_path(path: Path) -> str:
    return base.sha256_path(path)


def md5_path(path: Path) -> str:
    return base.md5_path(path)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
    )


def git_head() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO_ROOT, text=True
    ).strip()


def github_main() -> str:
    value = subprocess.check_output(
        [
            "git",
            "ls-remote",
            "github-write",
            "refs/heads/main",
        ],
        cwd=REPO_ROOT,
        text=True,
    ).split()[0]
    return value


def zip_inventory(path: Path) -> dict[str, object]:
    members: dict[str, dict[str, object]] = {}
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError(f"ZIP CRC failure: {path.name}")
        infos = [row for row in archive.infolist() if not row.is_dir()]
        names = [row.filename for row in infos]
        if len(names) != len(set(names)) or not all(map(safe_member, names)):
            raise RuntimeError(f"Unsafe or duplicate ZIP member: {path.name}")
        for info in infos:
            digest = hashlib.sha256()
            size = 0
            with archive.open(info) as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
                    size += len(chunk)
            members[info.filename] = {
                "bytes": size,
                "sha256": digest.hexdigest().upper(),
                "crc32": f"{info.CRC:08X}",
            }
    return {
        "status": "PASS",
        "filename": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256_path(path),
        "members": len(members),
        "uncompressed_bytes": sum(int(row["bytes"]) for row in members.values()),
        "member_identities": members,
    }


def validate_source_zip(path: Path, inventory: dict[str, object]) -> None:
    members = inventory["member_identities"]
    manifest_names = [name for name in members if name.endswith("/SHA256SUMS.csv")]
    if len(manifest_names) != 1 or int(inventory["members"]) != 19:
        raise RuntimeError("Source ZIP member boundary changed")
    manifest_name = manifest_names[0]
    prefix = manifest_name.removesuffix("SHA256SUMS.csv")
    with zipfile.ZipFile(path) as archive:
        rows = list(
            csv.DictReader(
                io.StringIO(archive.read(manifest_name).decode("utf-8-sig"))
            )
        )
    expected_names = {name.removeprefix(prefix) for name in members} - {
        "SHA256SUMS.csv"
    }
    if len(rows) != 18 or {row["path"] for row in rows} != expected_names:
        raise RuntimeError("Source ZIP manifest closure changed")
    for row in rows:
        observed = members[prefix + row["path"]]
        if (int(observed["bytes"]), str(observed["sha256"])) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Source ZIP identity mismatch: {row['path']}")


def validate_image_zip(path: Path, inventory: dict[str, object]) -> None:
    members = inventory["member_identities"]
    manifest_names = [name for name in members if name.endswith("/SHA256SUMS.csv")]
    if len(manifest_names) != 1 or int(inventory["members"]) != 13:
        raise RuntimeError("Image ZIP member boundary changed")
    manifest_name = manifest_names[0]
    prefix = manifest_name.removesuffix("SHA256SUMS.csv")
    image_names = {name for name in members if name.lower().endswith(".png")}
    if len(image_names) != 10:
        raise RuntimeError("Image ZIP pixel-member count changed")
    with zipfile.ZipFile(path) as archive:
        rows = list(
            csv.DictReader(io.StringIO(archive.read(manifest_name).decode("utf-8-sig")))
        )
    expected_names = {name.removeprefix(prefix) for name in members} - {
        "SHA256SUMS.csv"
    }
    if len(rows) != 12 or {row["path"] for row in rows} != expected_names:
        raise RuntimeError("Image ZIP index closure changed")
    for row in rows:
        observed = members[prefix + row["path"]]
        if (int(observed["bytes"]), str(observed["sha256"])) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Image ZIP identity mismatch: {row['path']}")


def verify_github() -> dict[str, object]:
    head = git_head()
    if github_main() != head or head != GITHUB_PACKAGE_COMMIT:
        raise RuntimeError("Local HEAD is not public GitHub main")
    session = base.make_session()
    rows = []
    for path in sorted(PACKAGE_ROOT.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(REPO_ROOT).as_posix()
        response = base.check(
            session.get(
                "https://raw.githubusercontent.com/KokunoYumeto/"
                f"modern-latex-manuscripts/{GITHUB_PACKAGE_COMMIT}/{relative}",
                timeout=(30, 300),
            ),
            {200},
        )
        data = response.content
        observed = (len(data), sha256_bytes(data))
        wanted = (path.stat().st_size, sha256_path(path))
        if observed != wanted:
            raise RuntimeError(f"GitHub raw readback mismatch: {relative}")
        rows.append(
            {
                "path": relative,
                "bytes": observed[0],
                "sha256": observed[1],
                "match": True,
            }
        )
    if len(rows) != 32:
        raise RuntimeError("GitHub package file boundary changed")
    result = {
        "status": "PASS_GITHUB_PUBLIC_READBACK",
        "errors": [],
        "commit": GITHUB_PACKAGE_COMMIT,
        "package_path": PACKAGE_REL.as_posix(),
        "files_read_back": len(rows),
        "readback_mode": "anonymous_commit_pinned_raw_exact_sha256",
        "file_readback": rows,
    }
    base.save_json(REPO_ROOT / GITHUB_RECEIPT_REL, result)
    return result


def verify_package_controls() -> None:
    rows = list(
        csv.DictReader(
            (PACKAGE_ROOT / "SHA256SUMS.csv").read_text(encoding="utf-8-sig").splitlines()
        )
    )
    files = [path for path in PACKAGE_ROOT.rglob("*") if path.is_file()]
    if len(files) != 32 or len(rows) != 31:
        raise RuntimeError("Package control boundary changed")
    expected_paths = {
        path.relative_to(PACKAGE_ROOT).as_posix()
        for path in files
        if path.name != "SHA256SUMS.csv"
    }
    if {row["path"] for row in rows} != expected_paths:
        raise RuntimeError("Package manifest closure changed")
    for row in rows:
        path = PACKAGE_ROOT / Path(row["path"])
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Package control changed: {row['path']}")
    manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    if (manifest.stat().st_size, sha256_path(manifest)) != (
        4_589,
        "D78D80865A25CB5D571FEFCC71EC4CFABC8675048D975C311D78552962D74048",
    ):
        raise RuntimeError("Package manifest identity changed")
    validation = json.loads(
        (PACKAGE_ROOT / "PACKAGE_VALIDATION.json").read_text(encoding="utf-8")
    )
    if validation.get("status") != "PASS_READY_FOR_WORKING_PUBLICATION" or validation.get("errors"):
        raise RuntimeError("Package validation is not PASS")


def verify_local_uploads() -> dict[str, dict[str, object]]:
    verify_package_controls()
    local: dict[str, dict[str, object]] = {}
    for name, expected in EXPECTED_UPLOADS.items():
        path = LOCAL_UPLOADS[name]
        if (path.stat().st_size, sha256_path(path)) != expected:
            raise RuntimeError(f"Local upload changed: {name}")
        row: dict[str, object] = {
            "path": path,
            "bytes": expected[0],
            "sha256": expected[1],
            "md5": md5_path(path),
        }
        if name.endswith(".zip"):
            row["inventory"] = zip_inventory(path)
        local[name] = row
    validate_source_zip(
        LOCAL_UPLOADS[SOURCE_ZIP_NAME], local[SOURCE_ZIP_NAME]["inventory"]
    )
    validate_image_zip(
        LOCAL_UPLOADS[IMAGE_ZIP_NAME], local[IMAGE_ZIP_NAME]["inventory"]
    )
    return local


def load_predecessor_receipt() -> dict[str, object]:
    receipt = json.loads(PREDECESSOR_RECEIPT.read_text(encoding="utf-8"))
    files = receipt.get("outer_file_readback", {})
    if (
        receipt.get("status") != "PASS_PUBLIC_READBACK"
        or int(receipt.get("record_id", -1)) != PREDECESSOR_RECORD
        or receipt.get("doi") != PREDECESSOR_DOI
        or receipt.get("concept_doi") != CONCEPT_DOI
        or int(receipt.get("outer_files", -1)) != PREDECESSOR_FILES
        or int(receipt.get("outer_bytes", -1)) != PREDECESSOR_BYTES
        or len(files) != PREDECESSOR_FILES
    ):
        raise RuntimeError("Controlling SGA predecessor receipt changed")
    return receipt


def public_headers() -> dict[str, str]:
    return {"Accept": "application/vnd.inveniordm.v1+json"}


def auth_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }


def fetch_live(session, predecessor: dict[str, object]) -> dict[str, object]:
    live = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = base.modern_entries(live)
    expected = predecessor["outer_file_readback"]
    if (
        int(live["id"]) != PREDECESSOR_RECORD
        or live["pids"]["doi"]["identifier"] != PREDECESSOR_DOI
        or live["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or len(entries) != PREDECESSOR_FILES
        or sum(int(row["size"]) for row in entries.values()) != PREDECESSOR_BYTES
        or set(entries) != set(expected)
        or live["files"].get("default_preview") != DEFAULT_PREVIEW
    ):
        raise RuntimeError("Live SGA predecessor boundary changed")
    for name, row in expected.items():
        observed = (
            int(entries[name]["size"]),
            base.normalized_md5(entries[name]["checksum"]),
        )
        wanted = (int(row["bytes"]), str(row["md5"]).lower())
        if observed != wanted:
            raise RuntimeError(f"Live SGA predecessor drift: {name}")
    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != PREDECESSOR_RECORD:
        raise RuntimeError("SGA concept head moved; refusing parallel successor")
    return live


def expected_retained(predecessor: dict[str, object]) -> dict[str, dict[str, object]]:
    files = predecessor["outer_file_readback"]
    return {name: row for name, row in files.items() if name not in REPLACED_NAMES}


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_controls(
    local: dict[str, dict[str, object]],
    predecessor: dict[str, object],
    github: dict[str, object],
) -> dict[str, object]:
    shutil.rmtree(CONTROLS_ROOT, ignore_errors=True)
    CONTROLS_ROOT.mkdir(parents=True, exist_ok=True)
    retained = expected_retained(predecessor)
    readme = "\n".join(
        [
            "# Current SGA release controls",
            "",
            "The current surface keeps the cumulative English readers first and SGA1 as",
            "the browser preview. This successor extends the working French SGA7 II",
            "reader through Expose XVII, preserves an explicitly partial XVIII",
            "continuation outside the reader, and adds actual Number12-derived source",
            "pages and detail crops for recovered scan indices 197, 198, 211, and 212.",
            "",
            "The existing large Number12 high-detail source-image archive is retained",
            "unchanged. The new compact image archive contains ten actual scan-derived",
            "PNGs with page, folio, dimensions, DPI, bounding box, and parent-scan hash.",
            "",
            "The SGA7 II reader is not a critical edition, diagram-fidelity certification,",
            "accessibility-remediated PDF, or complete SGA7 II volume.",
            "",
        ]
    ).encode("utf-8")
    (CONTROLS_ROOT / "09_README_CURRENT_RELEASE.md").write_bytes(readme)

    rows: list[dict[str, object]] = []
    for name, row in sorted(retained.items(), key=lambda item: item[0].casefold()):
        rows.append(
            {
                "filename": name,
                "bytes": int(row["bytes"]),
                "sha256": str(row["sha256"]).upper(),
                "release_role": "retained_predecessor_file",
                "source": f"zenodo_record_{PREDECESSOR_RECORD}",
            }
        )
    roles = {
        PDF_NAME: "direct_working_reader",
        TEX_NAME: "direct_editable_master",
        SOURCE_ZIP_NAME: "portable_reader_source_and_wip",
        IMAGE_ZIP_NAME: "actual_source_image_witnesses",
    }
    for name, row in local.items():
        rows.append(
            {
                "filename": name,
                "bytes": int(row["bytes"]),
                "sha256": str(row["sha256"]).upper(),
                "release_role": roles[name],
                "source": PACKAGE_REL.as_posix(),
            }
        )
    rows.sort(key=lambda row: str(row["filename"]).casefold())
    write_csv(
        CONTROLS_ROOT / "09a_RELEASE_FILE_MANIFEST.csv",
        rows,
        ["filename", "bytes", "sha256", "release_role", "source"],
    )
    validation = {
        "status": "PASS_PREPARED_RELEASE_CONTROLS",
        "errors": [],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "retained_predecessor_files": len(retained),
        "added_files": len(local),
        "replaced_files": sorted(REPLACED_NAMES),
        "expected_outer_files_including_controls": FINAL_FILES,
        "release_manifest_rows_excluding_controls": len(rows),
        "default_preview": DEFAULT_PREVIEW,
        "github": github,
        "reader_pages": 130,
        "reader_source_page_markers": 253,
        "source_zip_members": 19,
        "image_zip_members": 13,
        "image_members": 10,
        "complete_sga7ii_claim": False,
        "later_text_completion_claim_from_images": False,
        "source_images_are_actual_scan_derived_pixels": True,
    }
    base.save_json(CONTROLS_ROOT / "09b_RELEASE_VALIDATION.json", validation)

    copies = {
        "09c_SGA7II_PACKAGE_VALIDATION.json": PACKAGE_ROOT
        / "PACKAGE_VALIDATION.json",
        "09d_SGA7II_PACKAGE_SHA256SUMS.csv": PACKAGE_ROOT / "SHA256SUMS.csv",
        "09e_SGA7II_ZENODO_UPLOAD_MANIFEST.csv": PACKAGE_ROOT
        / "ZENODO_UPLOAD_MANIFEST.csv",
        "09f_SGA7II_VISUAL_EVIDENCE_INDEX.csv": PACKAGE_ROOT
        / "visual-evidence/VISUAL_EVIDENCE_INDEX.csv",
        "09g_SGA7II_GITHUB_PUBLIC_READBACK.json": REPO_ROOT / GITHUB_RECEIPT_REL,
    }
    for name, source in copies.items():
        shutil.copyfile(source, CONTROLS_ROOT / name)

    packed_rows: list[dict[str, object]] = []
    for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda row: row.name.casefold()):
        packed_rows.append(
            {
                "filename": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
            }
        )
    write_csv(
        CONTROLS_ROOT / "PACKED_CONTROL_SHA256.csv",
        packed_rows,
        ["filename", "bytes", "sha256"],
    )
    CONTROLS_ZIP.parent.mkdir(parents=True, exist_ok=True)
    CONTROLS_ZIP.unlink(missing_ok=True)
    with zipfile.ZipFile(
        CONTROLS_ZIP,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        allowZip64=True,
    ) as archive:
        for path in sorted(CONTROLS_ROOT.iterdir(), key=lambda row: row.name.casefold()):
            data = path.read_bytes()
            info = zipfile.ZipInfo(path.name, date_time=(2026, 7, 31, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, data, compresslevel=9)
    inventory = zip_inventory(CONTROLS_ZIP)
    if int(inventory["members"]) != len(packed_rows) + 1:
        raise RuntimeError("Release-control ZIP boundary changed")
    return {
        "path": CONTROLS_ZIP,
        "bytes": CONTROLS_ZIP.stat().st_size,
        "sha256": sha256_path(CONTROLS_ZIP),
        "md5": md5_path(CONTROLS_ZIP),
        "inventory": inventory,
    }


def assert_no_untracked_draft(session, token: str) -> None:
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            return
        base.check(
            session.get(
                f"{API}/records/{int(state['draft_id'])}/draft",
                headers=auth_headers(token),
                timeout=(30, 120),
            ),
            {200},
        )
        return
    response = session.get(
        f"{API}/records/{PREDECESSOR_RECORD}/draft",
        headers=auth_headers(token),
        timeout=(30, 120),
    )
    if response.status_code == 200:
        raise RuntimeError("Untracked active SGA successor draft exists")
    base.check(response, {404})


def create_or_resume_draft(session, token: str, live: dict[str, object]) -> int:
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            return int(state["record_id"])
        return int(state["draft_id"])
    headers = {"Authorization": f"Bearer {token}"}
    predecessor = base.check(
        session.get(
            f"{API}/deposit/depositions/{PREDECESSOR_RECORD}",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        predecessor.get("state") != "done"
        or not predecessor.get("submitted")
        or not predecessor.get("links", {}).get("newversion")
    ):
        raise RuntimeError("Live SGA predecessor is not a versioning base")
    created = base.check(
        session.post(
            predecessor["links"]["newversion"],
            headers=headers,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    deposition = base.check(
        session.get(created["links"]["latest_draft"], headers=headers, timeout=(30, 180)),
        {200},
    ).json()
    if set(base.legacy_entries(deposition)) != set(base.modern_entries(live)):
        raise RuntimeError("SGA successor did not inherit predecessor exactly")
    draft_id = int(deposition["id"])
    base.save_json(
        STATE_PATH,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "predecessor_record": PREDECESSOR_RECORD,
            "draft_id": draft_id,
            "concept_doi": CONCEPT_DOI,
            "published": False,
        },
    )
    return draft_id


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
    with path.open("rb") as handle:
        base.check(
            session.put(
                f"{bucket.rstrip('/')}/{quote(name, safe='')}",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Content-Type": "application/octet-stream",
                },
                data=handle,
                timeout=(30, 3600),
            ),
            {200, 201},
        )


def ordered_names(names: set[str]) -> list[str]:
    bundle = "00_Current_SGA1-6_English_Readers_and_Buildable_TeX_20260730.zip"
    direct_readers = [
        f"00{chr(96 + index)}_SGA{index}_English_Reader.pdf"
        for index in range(1, 7)
    ] + [
        "00g_SGA7I_Fresh_Source_Transcription_Complete_Working.pdf",
        PDF_NAME,
    ]
    direct_tex = [
        f"02{chr(96 + index)}_SGA{index}_English_Master.tex"
        for index in range(1, 7)
    ] + [
        "02g_SGA7I_Fresh_Source_Transcription_Complete_Working.tex",
        TEX_NAME,
    ]
    direct = {bundle, *direct_readers, *direct_tex}
    if not direct.issubset(names):
        raise RuntimeError("Direct SGA reader/source surface changed")
    remainder = names - direct
    other_pdfs = sorted(
        (name for name in remainder if name.lower().endswith(".pdf")),
        key=str.casefold,
    )
    other_tex = sorted(
        (name for name in remainder if name.lower().endswith(".tex")),
        key=str.casefold,
    )
    archival = sorted(
        remainder - set(other_pdfs) - set(other_tex), key=str.casefold
    )
    return [bundle, *direct_readers, *direct_tex, *other_pdfs, *other_tex, *archival]


def stage_and_publish(
    session,
    token: str,
    live: dict[str, object],
    draft_id: int,
    local: dict[str, dict[str, object]],
    controls: dict[str, object],
    predecessor: dict[str, object],
) -> dict[str, object]:
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            return base.check(
                session.get(
                    f"{API}/records/{int(state['record_id'])}?expand=true",
                    headers=public_headers(),
                    timeout=(30, 180),
                ),
                {200},
            ).json()
    legacy_headers = {"Authorization": f"Bearer {token}"}
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=legacy_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = base.legacy_entries(deposition)
    predecessor_names = set(predecessor["outer_file_readback"])
    allowed = predecessor_names | set(local)
    if not set(files).issubset(allowed) or not predecessor_names.issubset(files):
        raise RuntimeError("Tracked SGA draft file set changed")
    for name in sorted(REPLACED_NAMES):
        if name in files:
            base.check(
                session.delete(
                    files[name]["links"]["self"],
                    headers=legacy_headers,
                    timeout=(30, 300),
                ),
                {204},
            )
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=legacy_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = base.legacy_entries(deposition)
    uploads = {**local, CONTROLS_NAME: controls}
    bucket = deposition["links"]["bucket"]
    for index, (name, row) in enumerate(uploads.items(), start=1):
        existing = files.get(name)
        wanted = (int(row["bytes"]), str(row["md5"]).lower())
        if existing is not None:
            observed = (
                int(existing["filesize"]),
                base.normalized_md5(existing["checksum"]),
            )
            if observed != wanted:
                raise RuntimeError(f"Staged SGA identity changed: {name}")
            continue
        print(f"UPLOAD {index}/{len(uploads)} {name}", flush=True)
        upload_file(session, token, bucket, name, row["path"])

    headers = auth_headers(token)
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft?expand=true",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = base.modern_entries(draft)
    retained = expected_retained(predecessor)
    expected_names = set(retained) | set(local) | {CONTROLS_NAME}
    if set(entries) != expected_names or len(entries) != FINAL_FILES:
        raise RuntimeError("Staged SGA successor file boundary changed")
    expected = {**retained, **local, CONTROLS_NAME: controls}
    for name, entry in entries.items():
        observed = (
            int(entry["size"]),
            base.normalized_md5(entry["checksum"]),
        )
        wanted = (int(expected[name]["bytes"]), str(expected[name]["md5"]).lower())
        if observed != wanted:
            raise RuntimeError(f"Staged SGA successor identity changed: {name}")

    metadata = copy.deepcopy(draft["metadata"])
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = VERSION
    metadata["title"] = (
        "SGA 1-7: English Readers, French Texts, TeX Archives, and SGA7 "
        "Source Transcriptions"
    )
    description = metadata.get("description", "").replace(OLD_DESCRIPTION_ADDITION, "")
    if DESCRIPTION_ADDITION not in description:
        metadata["description"] = description + "\n" + DESCRIPTION_ADDITION
    subjects = metadata.setdefault("subjects", [])
    existing_subjects = {row.get("subject") for row in subjects}
    for subject in (
        "SGA7 II French source transcription",
        "high-detail mathematical source images",
    ):
        if subject not in existing_subjects:
            subjects.append({"subject": subject})
    additions = metadata.get("additional_descriptions", [])
    note_rows = [row for row in additions if row.get("type", {}).get("id") != "notes"]
    previous_notes = " ".join(
        row.get("description", "")
        for row in additions
        if row.get("type", {}).get("id") == "notes"
    ).replace(OLD_NOTES_ADDITION, "")
    note_rows.append(
        {
            "description": previous_notes + NOTES_ADDITION,
            "type": {"id": "notes", "title": {"en": "Notes"}},
        }
    )
    metadata["additional_descriptions"] = note_rows
    order = ordered_names(expected_names)
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": order,
        },
        "metadata": metadata,
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    patched = base.check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers={**headers, "Content-Type": "application/json"},
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    if (
        set(base.modern_entries(patched)) != expected_names
        or patched["files"].get("default_preview") != DEFAULT_PREVIEW
        or patched["metadata"].get("version") != VERSION
    ):
        raise RuntimeError("Patched SGA successor controls changed")
    base.save_json(
        RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{draft_id}_draft_files.json",
        {
            "status": "PASS_STAGED",
            "errors": [],
            "predecessor_record": PREDECESSOR_RECORD,
            "draft_id": draft_id,
            "concept_doi": CONCEPT_DOI,
            "files": len(entries),
            "retained_files": len(retained),
            "added_files": len(local),
            "replaced_files": sorted(REPLACED_NAMES),
            "default_preview": DEFAULT_PREVIEW,
            "duplicate_concept_created": False,
        },
    )
    published = base.check(
        session.post(patched["links"]["publish"], headers=headers, timeout=(30, 900)),
        {200, 202},
    ).json()
    if (
        int(published["id"]) != draft_id
        or published["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
    ):
        raise RuntimeError("Published SGA successor escaped the concept")
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    state.update(
        {
            "status": "PUBLISHED_TRACKED_SUCCESSOR",
            "published": True,
            "record_id": draft_id,
            "doi": published["pids"]["doi"]["identifier"],
        }
    )
    base.save_json(STATE_PATH, state)
    base.save_json(
        RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{draft_id}_publish_response.json",
        {
            "status": "PUBLISH_ACCEPTED",
            "errors": [],
            "record_id": draft_id,
            "doi": published["pids"]["doi"]["identifier"],
            "concept_doi": CONCEPT_DOI,
        },
    )
    return published


def stream_download(session, url: str, destination: Path | None) -> tuple[int, str, str]:
    sha = hashlib.sha256()
    md5 = hashlib.md5(usedforsecurity=False)
    size = 0
    output = destination.open("wb") if destination is not None else None
    try:
        with base.check(session.get(url, stream=True, timeout=(30, 3600)), {200}) as response:
            for block in response.iter_content(4 * 1024 * 1024):
                if not block:
                    continue
                sha.update(block)
                md5.update(block)
                size += len(block)
                if output is not None:
                    output.write(block)
    finally:
        if output is not None:
            output.close()
    return size, sha.hexdigest().upper(), md5.hexdigest().lower()


def assert_no_open_draft(session, token: str, record_id: int) -> None:
    response = session.get(
        f"{API}/records/{record_id}/draft",
        headers=auth_headers(token),
        timeout=(30, 120),
    )
    if response.status_code == 200:
        raise RuntimeError("Published SGA successor still has an active draft")
    base.check(response, {404})


def public_readback(
    session,
    token: str,
    record_id: int,
    local: dict[str, dict[str, object]],
    controls: dict[str, object],
    predecessor: dict[str, object],
    github: dict[str, object],
) -> dict[str, object]:
    record = None
    for _ in range(120):
        response = session.get(
            f"{API}/records/{record_id}?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        )
        if response.status_code == 200 and response.json().get("is_published"):
            candidate = response.json()
            if len(base.modern_entries(candidate)) == FINAL_FILES:
                record = candidate
                break
        time.sleep(2)
    if record is None:
        raise RuntimeError("Published SGA successor did not become public")
    retained = expected_retained(predecessor)
    expected = {**retained, **local, CONTROLS_NAME: controls}
    entries = base.modern_entries(record)
    if (
        set(entries) != set(expected)
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["files"].get("default_preview") != DEFAULT_PREVIEW
        or record["metadata"].get("version") != VERSION
    ):
        raise RuntimeError("Public SGA successor boundary changed")
    latest = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest?expand=true",
            headers=public_headers(),
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id:
        raise RuntimeError("Published SGA successor is not concept head")

    shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    READBACK_ROOT.mkdir(parents=True)
    files: dict[str, dict[str, object]] = {}
    archives: dict[str, dict[str, object]] = {}
    archive_names = {SOURCE_ZIP_NAME, IMAGE_ZIP_NAME, CONTROLS_NAME}
    try:
        for index, name in enumerate(sorted(entries, key=str.casefold), start=1):
            print(f"PUBLIC READBACK {index}/{len(entries)} {name}", flush=True)
            destination = READBACK_ROOT / f"archive-{index:03d}.zip" if name in archive_names else None
            observed = stream_download(session, entries[name]["links"]["content"], destination)
            row = expected[name]
            wanted = (
                int(row["bytes"]),
                str(row["sha256"]).upper(),
                str(row["md5"]).lower(),
            )
            if observed != wanted:
                raise RuntimeError(f"Public SGA successor mismatch: {name}")
            files[name] = {
                "bytes": observed[0],
                "sha256": observed[1],
                "md5": observed[2],
                "content_url": entries[name]["links"]["content"],
                "match": True,
                "readback_mode": "anonymous_full_download_exact_sha256",
            }
            if destination is not None:
                inventory = zip_inventory(destination)
                local_inventory = row["inventory"]
                if inventory["member_identities"] != local_inventory["member_identities"]:
                    raise RuntimeError(f"Public ZIP member drift: {name}")
                inventory["match"] = True
                archives[name] = inventory
                destination.unlink()
    finally:
        shutil.rmtree(READBACK_ROOT, ignore_errors=True)
    final_bytes = sum(int(row["bytes"]) for row in files.values())
    retained_errors = [
        name
        for name in retained
        if files[name]["sha256"] != str(retained[name]["sha256"]).upper()
    ]
    if (
        len(files) != FINAL_FILES
        or retained_errors
        or len(archives) != 3
        or int(archives[SOURCE_ZIP_NAME]["members"]) != 19
        or int(archives[IMAGE_ZIP_NAME]["members"]) != 13
    ):
        raise RuntimeError("SGA successor public readback did not close")
    assert_no_open_draft(session, token, record_id)

    result = {
        "status": "PASS_PUBLIC_READBACK",
        "errors": [],
        "record_id": record_id,
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "version": VERSION,
        "outer_files": len(files),
        "outer_bytes": final_bytes,
        "outer_file_readback": files,
        "retained_predecessor_files": len(retained),
        "retained_predecessor_identity_errors": retained_errors,
        "added_files": list(local),
        "replaced_files": sorted(REPLACED_NAMES),
        "default_preview": record["files"].get("default_preview"),
        "configured_file_order": ordered_names(set(expected)),
        "api_file_order": record["files"].get("order"),
        "latest_record": int(latest["id"]),
        "github": github,
        "source_zip_members": 19,
        "source_image_zip_members": 13,
        "source_image_members": 10,
        "duplicate_concept_created": False,
        "active_draft_remaining": False,
    }
    zipped = {
        "status": "PASS",
        "errors": [],
        "record_id": record_id,
        "doi": record["pids"]["doi"]["identifier"],
        "zip_archive_count": len(archives),
        "zip_member_count": sum(int(row["members"]) for row in archives.values()),
        "archives": archives,
    }
    base.save_json(
        RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}_public_readback.json",
        result,
    )
    base.save_json(
        RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}_zip_member_readback.json",
        zipped,
    )
    markdown = "\n".join(
        [
            "# SGA7 II X-XVII and recovered source-image publication receipt",
            "",
            f"- Record: <https://zenodo.org/records/{record_id}>",
            f"- DOI: `{record['pids']['doi']['identifier']}`",
            f"- Concept DOI: `{CONCEPT_DOI}`",
            f"- GitHub package commit: `{GITHUB_PACKAGE_COMMIT}`",
            f"- Public files: {len(files)} / {final_bytes:,} bytes",
            f"- Retained predecessor files: {len(retained)} / identity errors 0",
            f"- Working reader: 130 pages / `{EXPECTED_UPLOADS[PDF_NAME][1]}`",
            f"- Source ZIP: 19 members / `{EXPECTED_UPLOADS[SOURCE_ZIP_NAME][1]}`",
            f"- Recovered source-image ZIP: 13 members, including 10 PNGs / `{EXPECTED_UPLOADS[IMAGE_ZIP_NAME][1]}`",
            f"- Default preview: `{DEFAULT_PREVIEW}`",
            "- Duplicate concept created: no",
            "- Active draft remaining: no",
            "",
            "The reader covers SGA7 II Exposes X-XVII. Expose XVIII remains an",
            "explicit partial source continuation and is not part of the reader.",
            "The compact image archive contains actual Number12-derived source pixels",
            "for the four recovered pages; the earlier large image archive is retained.",
            "",
        ]
    )
    (RECEIPT_ROOT / f"{RECEIPT_TAG}_record_{record_id}.md").write_text(
        markdown, encoding="utf-8", newline="\n"
    )
    return result


def preflight() -> dict[str, object]:
    local = verify_local_uploads()
    predecessor = load_predecessor_receipt()
    github = verify_github()
    controls = build_controls(local, predecessor, github)
    token = base.find_token()
    session = base.make_session()
    fetch_live(session, predecessor)
    assert_no_untracked_draft(session, token)
    return {
        "status": "PASS_PREFLIGHT",
        "predecessor_record": PREDECESSOR_RECORD,
        "concept_doi": CONCEPT_DOI,
        "retained_files": PREDECESSOR_FILES - len(REPLACED_NAMES),
        "added_files": len(local),
        "replaced_files": sorted(REPLACED_NAMES),
        "final_files": FINAL_FILES,
        "default_preview": DEFAULT_PREVIEW,
        "github": github,
        "controls_zip": {
            "bytes": controls["bytes"],
            "sha256": controls["sha256"],
            "members": controls["inventory"]["members"],
        },
        "duplicate_concept_created": False,
    }


def publish() -> dict[str, object]:
    local = verify_local_uploads()
    predecessor = load_predecessor_receipt()
    github = verify_github()
    controls = build_controls(local, predecessor, github)
    token = base.find_token()
    session = base.make_session()
    live = fetch_live(session, predecessor)
    assert_no_untracked_draft(session, token)
    draft_id = create_or_resume_draft(session, token, live)
    published = stage_and_publish(
        session, token, live, draft_id, local, controls, predecessor
    )
    return public_readback(
        session,
        token,
        int(published["id"]),
        local,
        controls,
        predecessor,
        github,
    )


def readback_only() -> dict[str, object]:
    local = verify_local_uploads()
    predecessor = load_predecessor_receipt()
    github = verify_github()
    controls = build_controls(local, predecessor, github)
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if not state.get("published"):
        raise RuntimeError("Tracked SGA successor is not published")
    token = base.find_token()
    return public_readback(
        base.make_session(),
        token,
        int(state["record_id"]),
        local,
        controls,
        predecessor,
        github,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--readback-only", action="store_true")
    args = parser.parse_args()
    if args.preflight:
        result = preflight()
    elif args.readback_only:
        result = readback_only()
    else:
        result = publish()
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
