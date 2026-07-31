#!/usr/bin/env python3
"""Publish and read back the complete Weber Volume I working-reader successor."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import time
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


API = "https://zenodo.org/api"
PUBLICATION_DATE = "2026-07-31"
CONCEPT_DOI = "10.5281/zenodo.20412153"
PREDECESSOR_RECORD = 21_513_712
PREDECESSOR_DOI = "10.5281/zenodo.21513712"
PREDECESSOR_FILES = 56
PREDECESSOR_BYTES = 1_848_308_444
OLD_PREVIEW = (
    "01_CURRENT_Weber_VolumeI_German_SourceRepair_Workpass_through_p088_20260716.pdf"
)
OLD_FILES = {
    OLD_PREVIEW,
    "Weber_B139_heuristic_fix.zip",
    "99_Weber_Public_Status_20260716.json",
    "99_Weber_VolumeI_p088_GapPass_Status_20260716.md",
}
NEW_PREVIEW = (
    "00_CURRENT_Weber_VolumeI_German_Complete_Working_SourceRepair_20260731.pdf"
)
NEW_TEX = "01a_Weber_VolumeI_German_Complete_Working_SourceRepair_20260731.tex"
NEW_ZIP = "80_Weber_VolumeI_German_Complete_Working_Reader_TeX_QA_20260731.zip"
NEW_NAMES = {NEW_PREVIEW, NEW_TEX, NEW_ZIP}
GITHUB_COMMIT = "162305bc3d1b490fa5706e3971ed8c5799c332ca"

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path(
    "sources/weber/weber-volume1-german-complete-working-source-repair-20260731"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/weber-volume1-complete-working-20260731"
STATE_PATH = TEMP_ROOT / "draft_state.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
TOKEN_LOG = Path(
    os.environ.get(
        "ZENODO_TOKEN_LOG",
        Path.home() / ".codex" / ".sandbox" / "sandbox.log",
    )
)

LOCAL_UPLOADS = {
    NEW_PREVIEW: PACKAGE_ROOT
    / "reader/Weber_VolumeI_German_Complete_Working_SourceRepair_20260731.pdf",
    NEW_TEX: PACKAGE_ROOT
    / "source/Weber_VolumeI_German_Complete_Working_SourceRepair_20260731.tex",
    NEW_ZIP: TEMP_ROOT
    / "80_Weber_VolumeI_German_Complete_Working_Reader_TeX_QA_20260731.zip",
}
EXPECTED_UPLOADS = {
    NEW_PREVIEW: (
        2_275_193,
        "11000F9FA3F65C7C40ADB859A6A89689805012B3DF5D5DC4547E483778E1791A",
    ),
    NEW_TEX: (
        1_319_161,
        "003F967DD7316716D3B234D6DB4294C9765FD717093F968E4C0A0BD29129856A",
    ),
    NEW_ZIP: (
        10_291_232,
        "F625E45B77B1C6CF6E94262338A56EA326F95FC74F379B363BAE2EAD53EB03BF",
    ),
}
PACKAGE_MANIFEST = (
    24,
    3_226,
    "6008B86DD5484492F6D51A8C84D23B2131F713C7B8EDA4A89601426FFDAF06F7",
)
PACKAGE_VALIDATION = (
    2_017,
    "0C7095AF5BECA7C05567B57280C92C2445208B00E069B7B650E871AFBAD73341",
)
PACKAGE_FILES = 26
PACKAGE_BYTES = 11_500_208

DIRECT_READER_NAMES = [
    NEW_PREVIEW,
    "00_Weber_VolumeI_English_Translation_WorkingDraft_Predates_p088_German_Repairs.pdf",
    "02 CURRENT Heinrich Weber - Lehrbuch der Algebra, Volume II Source-Checked through Section 176 - English Translation.pdf",
    "03 CURRENT Heinrich Weber - Lehrbuch der Algebra, Volume II Source-Checked through Section 176 - German Source.pdf",
    "04 Heinrich Weber - Lehrbuch der Algebra, Volume III Current Repaired Cumulative - English Translation.pdf",
    "05 Heinrich Weber - Lehrbuch der Algebra, Volume III Current Repaired Cumulative - German Source.pdf",
]

DESCRIPTION = """<p><strong>Start here:</strong> the first file is the current 420-page German working reader for Heinrich Weber's <em>Lehrbuch der Algebra</em>, Volume I. It is selected as the browser preview. The existing Volume I English and Volume II-III German/English readers follow, then the direct editable Volume I TeX and one compact reader/source/QA ZIP.</p>
<p><strong>Volume I scope:</strong> the reader covers the complete body through Section 188 and the printed errata. A full p.1-p.648 content map, targeted retranscription of damaged sections, four global consistency sweeps, and broad visual spot checks are complete. A later stricter page-by-page cold re-verification is complete through printed p.124; printed p.125 is next.</p>
<p><strong>Other volumes:</strong> Volume II remains current through Section 176. Volume III remains an incomplete repaired cumulative. The Volume I English reader predates the current German repairs and is not synchronized to them.</p>
<p>These are scholarly working readers, not critical editions, complete symbol-by-symbol recertification, synchronized translations, peer review, mathematical certification, rights determinations, or tagged-PDF accessibility remediation. Historical versions remain immutable.</p>"""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5_path(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def normalized_md5(value: str) -> str:
    return value.casefold().removeprefix("md5:")


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def read_csv_bytes(data: bytes) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(data.decode("utf-8-sig"))))


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
    )


def find_token() -> str:
    direct = os.environ.get("ZENODO_TOKEN")
    if direct:
        return direct
    data = TOKEN_LOG.read_text(encoding="utf-8", errors="ignore")
    candidates = sorted(
        set(
            re.findall(
                r"(?<![A-Za-z0-9])[A-Za-z0-9]{60}(?![A-Za-z0-9])",
                data,
            )
        )
    )
    if len(candidates) != 1:
        raise RuntimeError(
            "Expected exactly one locally retained Zenodo credential; "
            f"found {len(candidates)}"
        )
    return candidates[0]


def make_session() -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=8,
        connect=8,
        read=8,
        status=8,
        backoff_factor=1.5,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET", "HEAD", "PUT"}),
        raise_on_status=False,
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers.update(
        {
            "User-Agent": "modern-latex-manuscripts-archive/1.0",
            "Connection": "close",
        }
    )
    return session


def check(response: requests.Response, expected: set[int]) -> requests.Response:
    if response.status_code not in expected:
        raise RuntimeError(
            f"Zenodo HTTP {response.status_code} for "
            f"{response.request.method} {response.url}: {response.text[:2000]}"
        )
    return response


def modern_entries(record: dict) -> dict[str, dict]:
    return record["files"]["entries"]


def legacy_entries(record: dict) -> dict[str, dict]:
    return {entry["filename"]: entry for entry in record["files"]}


def local_preflight() -> dict[str, object]:
    manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    validation_path = PACKAGE_ROOT / "PACKAGE_VALIDATION.json"
    if (manifest.stat().st_size, sha256_path(manifest)) != PACKAGE_MANIFEST[1:]:
        raise RuntimeError("Weber package manifest identity changed")
    if (
        validation_path.stat().st_size,
        sha256_path(validation_path),
    ) != PACKAGE_VALIDATION:
        raise RuntimeError("Weber package validation identity changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if (
        validation.get("status")
        != "PASS_READY_FOR_GITHUB_AND_SAME_CONCEPT_ZENODO_SUCCESSOR"
        or validation.get("errors")
        or validation.get("privacy_or_agent_process_hits")
    ):
        raise RuntimeError("Weber package validation is not PASS")
    rows = read_csv_bytes(manifest.read_bytes())
    if len(rows) != PACKAGE_MANIFEST[0]:
        raise RuntimeError("Weber package manifest row count changed")
    actual = {
        path.relative_to(PACKAGE_ROOT).as_posix(): path
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file()
    }
    if (
        len(actual) != PACKAGE_FILES
        or sum(path.stat().st_size for path in actual.values()) != PACKAGE_BYTES
    ):
        raise RuntimeError("Weber package file/byte boundary changed")
    represented = set(actual) - {"SHA256SUMS.csv", "PACKAGE_VALIDATION.json"}
    if {row["path"] for row in rows} != represented:
        raise RuntimeError("Weber package manifest closure changed")
    for row in rows:
        path = actual[row["path"]]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"Weber package mismatch: {row['path']}")
    for name, expected in EXPECTED_UPLOADS.items():
        path = LOCAL_UPLOADS[name]
        if (path.stat().st_size, sha256_path(path)) != expected:
            raise RuntimeError(f"Weber upload identity changed: {name}")
    with zipfile.ZipFile(LOCAL_UPLOADS[NEW_ZIP]) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Weber ZIP CRC failure")
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename for item in infos]
        if (
            len(infos) != PACKAGE_FILES
            or len(names) != len(set(names))
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError("Weber ZIP member boundary changed")
    return {
        "status": "PASS",
        "package_files": len(actual),
        "package_bytes": sum(path.stat().st_size for path in actual.values()),
        "zip_members": PACKAGE_FILES,
    }


def current_predecessor(session: requests.Session) -> dict:
    headers = {"Accept": "application/vnd.inveniordm.v1+json"}
    record = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = modern_entries(record)
    observed = (
        int(record["id"]),
        record["pids"]["doi"]["identifier"],
        record["parent"]["pids"]["doi"]["identifier"],
        record["files"].get("default_preview"),
        len(entries),
        sum(int(entry["size"]) for entry in entries.values()),
    )
    expected = (
        PREDECESSOR_RECORD,
        PREDECESSOR_DOI,
        CONCEPT_DOI,
        OLD_PREVIEW,
        PREDECESSOR_FILES,
        PREDECESSOR_BYTES,
    )
    if observed != expected or not OLD_FILES.issubset(entries):
        raise RuntimeError(f"Live Weber predecessor boundary changed: {observed!r}")
    return record


def assert_no_untracked_draft(
    session: requests.Session, token: str, allow_state: bool = False
) -> None:
    if allow_state and STATE_PATH.is_file():
        return
    vendor = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    response = session.get(
        f"{API}/records/{PREDECESSOR_RECORD}/draft",
        headers=vendor,
        timeout=(30, 120),
    )
    if response.status_code == 200:
        raise RuntimeError("Untracked Weber successor draft exists")
    check(response, {404})


def create_or_resume_draft(
    session: requests.Session, token: str, predecessor: dict
) -> int:
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {**auth, "Accept": "application/vnd.inveniordm.v1+json"}
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            return int(state["record_id"])
        if int(state.get("predecessor_record", -1)) != PREDECESSOR_RECORD:
            raise RuntimeError("Tracked Weber draft state has wrong predecessor")
        draft_id = int(state["draft_id"])
        check(
            session.get(
                f"{API}/records/{draft_id}/draft",
                headers=vendor,
                timeout=(30, 120),
            ),
            {200},
        )
        return draft_id
    assert_no_untracked_draft(session, token)
    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{PREDECESSOR_RECORD}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if deposition.get("state") != "done" or not deposition.get("submitted"):
        raise RuntimeError("Weber predecessor is not a valid versioning base")
    created = check(
        session.post(
            deposition["links"]["newversion"],
            headers=auth,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    draft = check(
        session.get(
            created["links"]["latest_draft"], headers=auth, timeout=(30, 180)
        ),
        {200},
    ).json()
    if set(legacy_entries(draft)) != set(modern_entries(predecessor)):
        raise RuntimeError("New Weber draft did not inherit exact predecessor files")
    draft_id = int(draft["id"])
    save_json(
        STATE_PATH,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "predecessor_record": PREDECESSOR_RECORD,
            "draft_id": draft_id,
            "published": False,
        },
    )
    return draft_id


def desired_order(predecessor_names: set[str]) -> list[str]:
    retained = predecessor_names - OLD_FILES
    prefix = DIRECT_READER_NAMES + [NEW_TEX, NEW_ZIP]
    if not set(prefix).issubset(retained | NEW_NAMES):
        raise RuntimeError("Weber reader-first order references a missing file")
    remainder = sorted((retained | NEW_NAMES) - set(prefix), key=str.casefold)
    return prefix + remainder


def updated_metadata(draft: dict) -> dict:
    metadata = draft["metadata"]
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = "2026-07-31 Volume I complete working reader"
    metadata["title"] = (
        "Heinrich Weber, Lehrbuch der Algebra: Complete German Volume I "
        "Working Reader and English Translation Drafts"
    )
    metadata["description"] = DESCRIPTION
    metadata["additional_descriptions"] = []
    metadata["subjects"] = [
        item
        for item in metadata.get("subjects", [])
        if item.get("subject")
        not in {"high-resolution scan crops", "visual evidence"}
    ]
    related = []
    for item in metadata.get("related_identifiers", []):
        identifier = item.get("identifier", "")
        if (
            item.get("scheme") == "url"
            and "github.com/KokunoYumeto/modern-latex-manuscripts" in identifier
        ):
            continue
        related.append(item)
    related.append(
        {
            "identifier": (
                "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
                f"{GITHUB_COMMIT}/{PACKAGE_REL.as_posix()}"
            ),
            "scheme": "url",
            "relation_type": {"id": "issupplementedby"},
        }
    )
    metadata["related_identifiers"] = related
    return metadata


def stage_and_publish(
    session: requests.Session,
    token: str,
    predecessor: dict,
    draft_id: int,
) -> int:
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            return int(state["record_id"])
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {**auth, "Accept": "application/vnd.inveniordm.v1+json"}
    json_headers = {**vendor, "Content-Type": "application/json"}
    predecessor_entries = modern_entries(predecessor)
    predecessor_names = set(predecessor_entries)
    expected_names = (predecessor_names - OLD_FILES) | NEW_NAMES
    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = legacy_entries(deposition)
    if not set(files).issubset(predecessor_names | NEW_NAMES):
        raise RuntimeError("Tracked Weber draft has an unexpected file set")
    for name in sorted(OLD_FILES, key=str.casefold):
        if name in files:
            check(
                session.delete(
                    files[name]["links"]["self"], headers=auth, timeout=(30, 300)
                ),
                {204},
            )
    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = legacy_entries(deposition)
    bucket = deposition["links"]["bucket"].rstrip("/")
    for name, path in LOCAL_UPLOADS.items():
        existing = files.get(name)
        wanted = (path.stat().st_size, md5_path(path))
        if existing is not None:
            observed = (
                int(existing["filesize"]),
                normalized_md5(existing["checksum"]),
            )
            if observed != wanted:
                raise RuntimeError(f"Staged Weber upload identity changed: {name}")
            continue
        with path.open("rb") as handle:
            check(
                session.put(
                    f"{bucket}/{quote(name, safe='')}",
                    headers={**auth, "Content-Type": "application/octet-stream"},
                    data=handle,
                    timeout=(30, 1800),
                ),
                {200, 201},
            )
    draft = check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=vendor,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = modern_entries(draft)
    if set(entries) != expected_names or len(entries) != PREDECESSOR_FILES - 1:
        raise RuntimeError("Staged Weber file set is not exact")
    for name in predecessor_names - OLD_FILES:
        before = predecessor_entries[name]
        after = entries[name]
        if (
            int(before["size"]),
            normalized_md5(before["checksum"]),
        ) != (
            int(after["size"]),
            normalized_md5(after["checksum"]),
        ):
            raise RuntimeError(f"Retained Weber object changed in draft: {name}")
    order = desired_order(predecessor_names)
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": NEW_PREVIEW,
            "order": order,
        },
        "metadata": updated_metadata(draft),
        "custom_fields": draft.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    patched = check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers=json_headers,
            json=payload,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        set(modern_entries(patched)) != expected_names
        or patched["files"].get("default_preview") != NEW_PREVIEW
    ):
        raise RuntimeError("Patched Weber draft controls changed")
    returned_order = patched["files"].get("order") or []
    if returned_order and returned_order != order:
        raise RuntimeError("Patched Weber draft returned a different file order")
    published = check(
        session.post(patched["links"]["publish"], headers=vendor, timeout=(30, 300)),
        {202},
    ).json()
    record_id = int(published["id"])
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    state.update(
        {
            "status": "PUBLISHED_PENDING_READBACK",
            "published": True,
            "record_id": record_id,
            "doi": published["pids"]["doi"]["identifier"],
        }
    )
    save_json(STATE_PATH, state)
    return record_id


def stream_identity(
    session: requests.Session, url: str, capture: bool = False
) -> tuple[dict[str, object], bytes | None]:
    digest = hashlib.sha256()
    md5 = hashlib.md5(usedforsecurity=False)
    total = 0
    captured = io.BytesIO() if capture else None
    with check(session.get(url, stream=True, timeout=(30, 1800)), {200}) as response:
        for block in response.iter_content(4 * 1024 * 1024):
            if not block:
                continue
            total += len(block)
            digest.update(block)
            md5.update(block)
            if captured is not None:
                captured.write(block)
    return (
        {
            "bytes": total,
            "sha256": digest.hexdigest().upper(),
            "md5": md5.hexdigest().lower(),
        },
        captured.getvalue() if captured is not None else None,
    )


def replay_zip(data: bytes) -> dict[str, object]:
    if (len(data), sha256_bytes(data)) != EXPECTED_UPLOADS[NEW_ZIP]:
        raise RuntimeError("Published Weber ZIP outer identity changed")
    local_members = {}
    with zipfile.ZipFile(LOCAL_UPLOADS[NEW_ZIP]) as archive:
        for info in archive.infolist():
            if not info.is_dir():
                member = archive.read(info.filename)
                local_members[info.filename] = (len(member), sha256_bytes(member))
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Published Weber ZIP CRC failed")
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename for item in infos]
        if (
            set(names) != set(local_members)
            or len(names) != len(set(names))
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError("Published Weber ZIP member boundary changed")
        rows = []
        for name in names:
            member = archive.read(name)
            observed = (len(member), sha256_bytes(member))
            if observed != local_members[name]:
                raise RuntimeError(f"Published Weber ZIP member changed: {name}")
            rows.append(
                {"path": name, "bytes": observed[0], "sha256": observed[1]}
            )
        checksum_rows = read_csv_bytes(archive.read("SHA256SUMS.csv"))
        if len(checksum_rows) != PACKAGE_MANIFEST[0]:
            raise RuntimeError("Published Weber ZIP manifest row count changed")
        return {
            "status": "PASS",
            "members": len(rows),
            "uncompressed_bytes": sum(int(row["bytes"]) for row in rows),
            "safe_names": True,
            "manifest_rows": len(checksum_rows),
            "member_identities": rows,
        }


def public_readback(
    session: requests.Session,
    token: str,
    predecessor: dict,
    record_id: int,
) -> dict[str, object]:
    headers = {"Accept": "application/vnd.inveniordm.v1+json"}
    record = None
    for _ in range(60):
        response = session.get(
            f"{API}/records/{record_id}", headers=headers, timeout=(30, 180)
        )
        if response.status_code == 200 and response.json().get("is_published"):
            record = response.json()
            break
        time.sleep(2)
    if record is None:
        raise RuntimeError("Published Weber successor did not become readable")
    predecessor_entries = modern_entries(predecessor)
    predecessor_names = set(predecessor_entries)
    expected_names = (predecessor_names - OLD_FILES) | NEW_NAMES
    entries = modern_entries(record)
    order = desired_order(predecessor_names)
    if (
        set(entries) != expected_names
        or len(entries) != PREDECESSOR_FILES - 1
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["files"].get("default_preview") != NEW_PREVIEW
        or record["metadata"].get("description") != DESCRIPTION
        or record["metadata"].get("additional_descriptions")
    ):
        raise RuntimeError("Published Weber successor boundary changed")
    api_order = record["files"].get("order") or []
    if api_order and api_order != order:
        raise RuntimeError("Published Weber successor returned a different file order")
    lowered = DESCRIPTION.casefold()
    for forbidden in ("image", "crop", "raster", "dpi", "witness"):
        if forbidden in lowered:
            raise RuntimeError(f"Weber landing metadata contains {forbidden} prose")
    latest = check(
        session.get(
            f"{API}/records/{record_id}/versions/latest",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id:
        raise RuntimeError("Published Weber successor is not the live concept head")

    retained = {}
    for name in sorted(predecessor_names - OLD_FILES, key=str.casefold):
        before = predecessor_entries[name]
        after = entries[name]
        identity = {
            "bytes": int(after["size"]),
            "md5": normalized_md5(after["checksum"]),
        }
        if identity != {
            "bytes": int(before["size"]),
            "md5": normalized_md5(before["checksum"]),
        }:
            raise RuntimeError(f"Retained published Weber object changed: {name}")
        retained[name] = identity

    new_files = {}
    captured_zip = None
    for name in (NEW_PREVIEW, NEW_TEX, NEW_ZIP):
        identity, data = stream_identity(
            session, entries[name]["links"]["content"], capture=name == NEW_ZIP
        )
        if (identity["bytes"], identity["sha256"]) != EXPECTED_UPLOADS[name]:
            raise RuntimeError(f"Published Weber file changed: {name}")
        if identity["md5"] != normalized_md5(entries[name]["checksum"]):
            raise RuntimeError(f"Published Weber API checksum changed: {name}")
        new_files[name] = identity
        if name == NEW_ZIP:
            captured_zip = data
    if captured_zip is None:
        raise RuntimeError("Published Weber ZIP was not captured")
    zip_readback = replay_zip(captured_zip)

    predecessor_public = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}", headers=headers, timeout=(30, 180)
        ),
        {200},
    ).json()
    if not predecessor_public.get("is_published"):
        raise RuntimeError("Weber predecessor is no longer published")
    vendor = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    draft_probe = session.get(
        f"{API}/records/{record_id}/draft", headers=vendor, timeout=(30, 120)
    )
    check(draft_probe, {404})
    receipt = {
        "status": "PASS",
        "concept_doi": CONCEPT_DOI,
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_doi": PREDECESSOR_DOI,
        "record_id": record_id,
        "doi": record["pids"]["doi"]["identifier"],
        "record_url": record["links"]["self_html"],
        "github_commit": GITHUB_COMMIT,
        "github_package_path": PACKAGE_REL.as_posix(),
        "files": len(entries),
        "bytes": sum(int(entry["size"]) for entry in entries.values()),
        "default_preview": record["files"].get("default_preview"),
        "requested_order": order,
        "api_order": api_order,
        "description_sha256": sha256_bytes(DESCRIPTION.encode("utf-8")),
        "description_bytes": len(DESCRIPTION.encode("utf-8")),
        "new_files": new_files,
        "retained_files": retained,
        "retained_files_count": len(retained),
        "removed_stale_files": sorted(OLD_FILES),
        "zip_readback": zip_readback,
        "predecessor_preserved_published": True,
        "published_record_draft_probe_status": draft_probe.status_code,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    path = RECEIPT_ROOT / (
        f"20260731_weber_volume1_complete_working_record_{record_id}_public_readback.json"
    )
    save_json(path, receipt)
    return receipt


def preflight() -> dict[str, object]:
    local = local_preflight()
    token = find_token()
    session = make_session()
    predecessor = current_predecessor(session)
    assert_no_untracked_draft(session, token, allow_state=True)
    return {
        "status": "PASS",
        "predecessor_record": int(predecessor["id"]),
        "concept_doi": predecessor["parent"]["pids"]["doi"]["identifier"],
        "predecessor_files": len(modern_entries(predecessor)),
        "package_files": local["package_files"],
        "zip_members": local["zip_members"],
        "untracked_draft": False,
    }


def publish() -> dict[str, object]:
    local_preflight()
    token = find_token()
    session = make_session()
    predecessor = current_predecessor(session)
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            return public_readback(
                session, token, predecessor, int(state["record_id"])
            )
    draft_id = create_or_resume_draft(session, token, predecessor)
    record_id = stage_and_publish(session, token, predecessor, draft_id)
    return public_readback(session, token, predecessor, record_id)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args()
    result = preflight() if args.preflight_only else publish()
    compact = {
        key: value
        for key, value in result.items()
        if key
        not in {
            "retained_files",
            "new_files",
            "zip_readback",
            "requested_order",
            "api_order",
        }
    }
    print(json.dumps(compact, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
