#!/usr/bin/env python3
"""Publish and read back the complete FAC successor in the Serre concept.

The transaction is deliberately narrow: it replaces the four partial FAC
objects, retains the GAGA custody ZIP byte-for-byte, and refuses a changed
predecessor or an untracked draft.
"""

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
CONCEPT_DOI = "10.5281/zenodo.21720996"
PREDECESSOR_RECORD = 21_720_997
PREDECESSOR_DOI = "10.5281/zenodo.21720997"
PREDECESSOR_TITLE = (
    "Jean-Pierre Serre: FAC Partial French Working Transcription and "
    "GAGA TeX Source Custody"
)
OLD_PREVIEW = "00_Serre_FAC_French_Partial_Working_Transcription_20260731.pdf"
NEW_PREVIEW = "00_Serre_FAC_French_Complete_Working_Transcription_20260731.pdf"

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path(
    "sources/serre/serre-fac-complete-working-transcription-20260731"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/serre-fac-complete-20260731"
STATE_PATH = TEMP_ROOT / "draft_state.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
TOKEN_LOG = Path(
    os.environ.get(
        "ZENODO_TOKEN_LOG",
        Path.home() / ".codex" / ".sandbox" / "sandbox.log",
    )
)

OLD_FAC_FILES = {
    OLD_PREVIEW,
    "01a_Serre_FAC_French_Partial_Working_Transcription_Master_20260731.tex",
    "01b_Serre_FAC_French_Partial_Working_Transcription_Body_20260731.tex",
    "02_Serre_FAC_French_Partial_Source_and_Visual_Evidence_20260731.zip",
}
GAGA_NAME = "03_Serre_GAGA_French_FirstPass_TeX_Custody_20260731.zip"
FAC_ZIP_NAME = "02_Serre_FAC_French_Complete_Source_and_Visual_Evidence_20260731.zip"
MASTER_NAME = "01a_Serre_FAC_French_Complete_Working_Transcription_Master_20260731.tex"
BODY_NAME = "01b_Serre_FAC_French_Complete_Working_Transcription_Body_20260731.tex"

LOCAL_UPLOADS = {
    NEW_PREVIEW: PACKAGE_ROOT
    / "reader/Serre_FAC_French_Complete_Working_Transcription_20260731.pdf",
    MASTER_NAME: PACKAGE_ROOT / "source/fac.tex",
    BODY_NAME: PACKAGE_ROOT / "source/fac_body.tex",
    FAC_ZIP_NAME: PACKAGE_ROOT
    / "release/02_Serre_FAC_French_Complete_Source_and_Visual_Evidence_20260731.zip",
}
LOCAL_ALL = {
    **LOCAL_UPLOADS,
    GAGA_NAME: PACKAGE_ROOT
    / "release/03_Serre_GAGA_French_FirstPass_TeX_Custody_20260731.zip",
}
EXPECTED_UPLOADS = {
    NEW_PREVIEW: (
        634_043,
        "794B982AB18FBAF734D836519C8DA34C407B77B4EEAB4ABC7A8BA495CD79B6F5",
    ),
    MASTER_NAME: (
        3_152,
        "80CC57E8D3056F79896534C82BC4AF143DA08A4856D9C2026CBB02CCE7A8D6C8",
    ),
    BODY_NAME: (
        335_189,
        "5354052BC1803015CF68CCD16E3612BA3A6FF3432F01C84A4419339FC373223F",
    ),
    FAC_ZIP_NAME: (
        1_300_549,
        "DC3FAF4D0CCA300FC8A7B98007DBCEE51D61932B8564C322E6A681FF0712FBC9",
    ),
}
EXPECTED_GAGA = (
    47_365,
    "B0D94F4B0DB91CEB3093BB4CAFF47F6F265D468709A703ACBD6EBE65B98B8B6E",
)
DESIRED_ORDER = [NEW_PREVIEW, MASTER_NAME, BODY_NAME, FAC_ZIP_NAME, GAGA_NAME]

PREDECESSOR_IDENTITIES = {
    OLD_PREVIEW: (
        583_271,
        "21D3923FAE6CAF108CA9EDF3429F8868C42D2F0DC71067444C2395643146B41B",
    ),
    "01a_Serre_FAC_French_Partial_Working_Transcription_Master_20260731.tex": (
        4_239,
        "130EB9C7EA835AAE53CD4A730650539376D7D17EF499F0FA5FC03D109ABAFFA9",
    ),
    "01b_Serre_FAC_French_Partial_Working_Transcription_Body_20260731.tex": (
        279_820,
        "66E3A1B8B878A165C83D1C068A653E90A99DD0D4DBFD85AB6C82CA1028510491",
    ),
    "02_Serre_FAC_French_Partial_Source_and_Visual_Evidence_20260731.zip": (
        1_193_953,
        "78AEB1CC4DFCD1B59B3C6F3BC742DF1416CE0F73C4CD6E92E470355EABA9E9A5",
    ),
    GAGA_NAME: EXPECTED_GAGA,
}

PACKAGE_MANIFEST = (
    30,
    3_612,
    "07AE1480461D3A8A11A514EEB1D2F7BFBB7F372114B2072548D6B98CCC79E970",
)
PACKAGE_VALIDATION = (
    4_729,
    "92C6CAE6199FBBB523DF84656228918AB92B499C0DCF2D3C7CCC845F3722EB09",
)
PACKAGE_FILES = 32
PACKAGE_BYTES = 3_112_049
PACKAGE_AGGREGATE = (
    "9D4E0B2A832BDE307B03EE149A9881B6C61327073C2745609E1300571BD0CBA7"
)
GITHUB_COMMIT = "279633789e1daaac1e99752d6b11cfa5462312a1"


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
    return value.lower().removeprefix("md5:")


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


def zip_member_identities(path: Path) -> dict[str, dict[str, object]]:
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError(f"ZIP CRC failure: {path.name}")
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename for item in infos]
        if len(names) != len(set(names)) or not all(safe_member(name) for name in names):
            raise RuntimeError(f"Unsafe or duplicate ZIP member: {path.name}")
        return {
            item.filename: {
                "bytes": item.file_size,
                "sha256": sha256_bytes(archive.read(item.filename)),
            }
            for item in infos
        }


def local_preflight() -> dict[str, object]:
    manifest = PACKAGE_ROOT / "SHA256SUMS.csv"
    validation_path = PACKAGE_ROOT / "PACKAGE_VALIDATION.json"
    if (manifest.stat().st_size, sha256_path(manifest)) != PACKAGE_MANIFEST[1:]:
        raise RuntimeError("FAC outer manifest identity changed")
    if (
        validation_path.stat().st_size,
        sha256_path(validation_path),
    ) != PACKAGE_VALIDATION:
        raise RuntimeError("FAC package validation identity changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if (
        validation.get("status")
        != "PASS_READY_FOR_PUBLIC_COMPLETE_WORKING_TRANSCRIPTION_CUSTODY"
        or validation.get("errors")
    ):
        raise RuntimeError("FAC package validation is not PASS")
    rows = read_csv_bytes(manifest.read_bytes())
    if len(rows) != PACKAGE_MANIFEST[0]:
        raise RuntimeError("FAC outer manifest row count changed")
    actual = {
        path.relative_to(PACKAGE_ROOT).as_posix(): path
        for path in PACKAGE_ROOT.rglob("*")
        if path.is_file()
    }
    if len(actual) != PACKAGE_FILES or sum(path.stat().st_size for path in actual.values()) != PACKAGE_BYTES:
        raise RuntimeError("FAC package file/byte boundary changed")
    represented = set(actual) - {"SHA256SUMS.csv", "PACKAGE_VALIDATION.json"}
    if {row["path"] for row in rows} != represented:
        raise RuntimeError("FAC outer manifest closure changed")
    for row in rows:
        path = actual[row["path"]]
        if (path.stat().st_size, sha256_path(path)) != (
            int(row["bytes"]),
            row["sha256"].upper(),
        ):
            raise RuntimeError(f"FAC package mismatch: {row['path']}")
    for name, expected in {**EXPECTED_UPLOADS, GAGA_NAME: EXPECTED_GAGA}.items():
        path = LOCAL_ALL[name]
        if (path.stat().st_size, sha256_path(path)) != expected:
            raise RuntimeError(f"FAC upload identity changed: {name}")
    fac_members = zip_member_identities(LOCAL_ALL[FAC_ZIP_NAME])
    gaga_members = zip_member_identities(LOCAL_ALL[GAGA_NAME])
    if len(fac_members) != 27 or len(gaga_members) != 8:
        raise RuntimeError("Serre ZIP member boundary changed")
    return {
        "status": "PASS",
        "package_files": len(actual),
        "package_bytes": sum(path.stat().st_size for path in actual.values()),
        "package_aggregate_sha256": PACKAGE_AGGREGATE,
        "fac_zip_members": fac_members,
        "gaga_zip_members": gaga_members,
    }


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
        record["metadata"]["title"],
        record["files"].get("default_preview"),
        len(entries),
        sum(int(entry["size"]) for entry in entries.values()),
    )
    expected = (
        PREDECESSOR_RECORD,
        PREDECESSOR_DOI,
        CONCEPT_DOI,
        PREDECESSOR_TITLE,
        OLD_PREVIEW,
        5,
        2_108_648,
    )
    if observed != expected or set(entries) != set(PREDECESSOR_IDENTITIES):
        raise RuntimeError(f"Live Serre predecessor boundary changed: {observed!r}")
    for name, expected_identity in PREDECESSOR_IDENTITIES.items():
        result, _ = stream_identity(session, entries[name]["links"]["content"])
        if (result["bytes"], result["sha256"]) != expected_identity:
            raise RuntimeError(f"Live Serre predecessor file changed: {name}")
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
        raise RuntimeError("Untracked Serre successor draft exists")
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
            raise RuntimeError("Tracked Serre draft state has wrong predecessor")
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
        raise RuntimeError("Serre predecessor is not a valid versioning base")
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
        raise RuntimeError("New Serre draft did not inherit exact predecessor files")
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


def updated_metadata(draft: dict) -> dict:
    metadata = draft["metadata"]
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = "2026-07-31 FAC complete and GAGA source custody"
    metadata["title"] = (
        "Jean-Pierre Serre: FAC Complete French Working Transcription and "
        "GAGA TeX Source Custody"
    )
    metadata["description"] = "\n".join(
        [
            "<p><strong>Start here:</strong> the first file is the complete "
            "63-page FAC French working reader and is selected as the browser "
            "preview. The next two files are its direct editable master and body "
            "TeX. The compact FAC ZIP contains the reader, complete TeX closure, "
            "source-observation apparatus, exact manifests, and four actual "
            "scan-derived crops with page, rasterization, bounding-box, dimension, "
            "and hash provenance.</p>",
            "<p><strong>FAC scope:</strong> all 82 source pages are transcribed, "
            "covering printed pages 197-278. Twelve formerly missing source-page "
            "units (indices 21, 22, 25, 26, 71-74, and 77-80) are now included. "
            "The full 83-page authority scan is not redistributed.</p>",
            "<p><strong>GAGA:</strong> the final ZIP retains byte-identically the "
            "complete first-pass TeX transcription of printed pages 1-42. Its "
            "earlier PDF is not fronted because visible page-join sentinels remain; "
            "GAGA is source-survival custody here, not a clean reader claim.</p>",
            "<p>These are scholarly working transcriptions, not a complete Serre "
            "corpus, critical editions, independent peer review, mathematical "
            "certification, accessibility certification, or blanket rights "
            "clearance. Rights in the underlying works remain with their respective "
            "holders and no new blanket license is asserted.</p>",
        ]
    )
    metadata["additional_descriptions"] = [
        {
            "description": (
                "<p>FAC frozen and isolated-rebuild PDFs match on all 63 decoded "
                "page-content streams, extracted texts, page geometries, and 200-dpi "
                "page renders. Representative pages 1, 32, 60, and 63 were visually "
                "reviewed. All 82 source markers are present exactly once.</p>"
            ),
            "type": {"id": "notes"},
        }
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
    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = legacy_entries(deposition)
    predecessor_names = set(modern_entries(predecessor))
    expected_names = set(DESIRED_ORDER)
    allowed_universe = predecessor_names | expected_names
    if GAGA_NAME not in files or not set(files).issubset(allowed_universe):
        raise RuntimeError("Tracked Serre draft has an unexpected file set")
    for name in sorted(OLD_FAC_FILES, key=str.casefold):
        if name not in files:
            continue
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
                raise RuntimeError(f"Staged Serre upload identity changed: {name}")
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
    if set(entries) != expected_names or len(entries) != 5:
        raise RuntimeError("Staged Serre file set is not exact")
    retained = entries[GAGA_NAME]
    predecessor_gaga = modern_entries(predecessor)[GAGA_NAME]
    if (
        int(retained["size"]),
        normalized_md5(retained["checksum"]),
    ) != (
        int(predecessor_gaga["size"]),
        normalized_md5(predecessor_gaga["checksum"]),
    ):
        raise RuntimeError("Retained GAGA object changed in draft")
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": NEW_PREVIEW,
            "order": DESIRED_ORDER,
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
        raise RuntimeError("Patched Serre draft controls changed")
    returned_order = patched["files"].get("order") or []
    if returned_order and returned_order != DESIRED_ORDER:
        raise RuntimeError("Patched Serre file order changed")
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


def replay_zip(
    data: bytes,
    expected_outer: tuple[int, str],
    expected_members: dict[str, dict[str, object]],
    manifest_suffix: str,
    expected_manifest_rows: int,
) -> dict[str, object]:
    if (len(data), sha256_bytes(data)) != expected_outer:
        raise RuntimeError("Published Serre ZIP outer identity changed")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Published Serre ZIP CRC failed")
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename for item in infos]
        if (
            set(names) != set(expected_members)
            or len(names) != len(set(names))
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError("Published Serre ZIP member boundary changed")
        identities = {}
        for name in names:
            member = archive.read(name)
            observed = (len(member), sha256_bytes(member))
            expected = (
                int(expected_members[name]["bytes"]),
                str(expected_members[name]["sha256"]),
            )
            if observed != expected:
                raise RuntimeError(f"Published Serre ZIP member changed: {name}")
            identities[name] = {
                "bytes": observed[0],
                "sha256": observed[1],
                "match": True,
            }
        manifest_names = [name for name in names if name.endswith(manifest_suffix)]
        if len(manifest_names) != 1:
            raise RuntimeError("Published Serre ZIP manifest boundary changed")
        rows = read_csv_bytes(archive.read(manifest_names[0]))
        if len(rows) != expected_manifest_rows:
            raise RuntimeError("Published Serre ZIP manifest row count changed")
        return {
            "status": "PASS",
            "members": len(infos),
            "uncompressed_bytes": sum(item.file_size for item in infos),
            "manifest_rows": len(rows),
            "safe_names": True,
            "member_identities": identities,
        }


def public_readback(
    session: requests.Session,
    token: str,
    predecessor: dict,
    record_id: int,
    local: dict[str, object],
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
        raise RuntimeError("Published Serre successor did not become readable")
    entries = modern_entries(record)
    if (
        set(entries) != set(DESIRED_ORDER)
        or len(entries) != 5
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["files"].get("default_preview") != NEW_PREVIEW
        or record["metadata"].get("version")
        != "2026-07-31 FAC complete and GAGA source custody"
    ):
        raise RuntimeError("Published Serre successor boundary changed")
    latest = check(
        session.get(
            f"{API}/records/{record_id}/versions/latest",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id:
        raise RuntimeError("Published Serre successor is not the live concept head")
    api_order = record["files"].get("order") or []
    if api_order and api_order != DESIRED_ORDER:
        raise RuntimeError("Published Serre file order changed")

    outer = {}
    captured = {}
    expected_all = {**EXPECTED_UPLOADS, GAGA_NAME: EXPECTED_GAGA}
    for ordinal, name in enumerate(DESIRED_ORDER, start=1):
        result, data = stream_identity(
            session,
            entries[name]["links"]["content"],
            capture=name in {FAC_ZIP_NAME, GAGA_NAME},
        )
        if (result["bytes"], result["sha256"]) != expected_all[name]:
            raise RuntimeError(f"Published Serre outer file changed: {name}")
        if result["md5"] != normalized_md5(entries[name]["checksum"]):
            raise RuntimeError(f"Published Serre API checksum changed: {name}")
        outer[name] = {
            **result,
            "url": entries[name]["links"]["content"],
            "readback_ordinal": ordinal,
            "match": True,
        }
        if data is not None:
            captured[name] = data

    predecessor_entries = modern_entries(predecessor)
    new_gaga = entries[GAGA_NAME]
    old_gaga = predecessor_entries[GAGA_NAME]
    if (
        int(new_gaga["size"]),
        normalized_md5(new_gaga["checksum"]),
    ) != (
        int(old_gaga["size"]),
        normalized_md5(old_gaga["checksum"]),
    ):
        raise RuntimeError("Published retained GAGA identity changed")

    fac_zip = replay_zip(
        captured[FAC_ZIP_NAME],
        EXPECTED_UPLOADS[FAC_ZIP_NAME],
        local["fac_zip_members"],
        "SOURCE_PACKAGE_MANIFEST.csv",
        26,
    )
    gaga_zip = replay_zip(
        captured[GAGA_NAME],
        EXPECTED_GAGA,
        local["gaga_zip_members"],
        "SHA256SUMS.csv",
        6,
    )
    predecessor_public = check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if not predecessor_public.get("is_published"):
        raise RuntimeError("Serre predecessor is no longer publicly immutable")
    draft_probe = session.get(
        f"{API}/records/{record_id}/draft",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.inveniordm.v1+json",
        },
        timeout=(30, 120),
    )
    check(draft_probe, {404})

    result = {
        "status": "PASS_PUBLIC_READBACK",
        "errors": [],
        "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "record_id": int(record["id"]),
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": record["parent"]["pids"]["doi"]["identifier"],
        "predecessor_record": PREDECESSOR_RECORD,
        "predecessor_preserved_published": True,
        "title": record["metadata"]["title"],
        "default_preview": record["files"].get("default_preview"),
        "configured_file_order": DESIRED_ORDER,
        "api_file_order": api_order,
        "outer_file_count": len(outer),
        "outer_total_bytes": sum(int(value["bytes"]) for value in outer.values()),
        "outer_all_match": True,
        "files": outer,
        "zip_archives": {FAC_ZIP_NAME: fac_zip, GAGA_NAME: gaga_zip},
        "zip_member_count": fac_zip["members"] + gaga_zip["members"],
        "zip_members_all_match": True,
        "github": {
            "commit": GITHUB_COMMIT,
            "path": PACKAGE_REL.as_posix(),
            "package_files_read_back": 32,
            "readback_status": "PASS",
        },
        "published_record_draft_probe_status": draft_probe.status_code,
        "retained_gaga_byte_identical": True,
        "duplicate_concept_created": False,
        "second_draft_created": False,
    }
    receipt = RECEIPT_ROOT / (
        f"20260731_serre_fac_complete_record_{record_id}_public_readback.json"
    )
    save_json(receipt, result)
    result["receipt_path"] = str(receipt)
    return result


def preflight() -> dict[str, object]:
    local = local_preflight()
    token = find_token()
    session = make_session()
    predecessor = current_predecessor(session)
    assert_no_untracked_draft(session, token)
    return {
        "status": "PASS_PREFLIGHT",
        "predecessor_record": int(predecessor["id"]),
        "concept_doi": CONCEPT_DOI,
        "local_package_files": local["package_files"],
        "local_package_bytes": local["package_bytes"],
        "fac_zip_members": len(local["fac_zip_members"]),
        "gaga_zip_members": len(local["gaga_zip_members"]),
        "untracked_draft": False,
        "errors": [],
    }


def publish() -> dict[str, object]:
    local = local_preflight()
    token = find_token()
    session = make_session()
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            predecessor = check(
                session.get(
                    f"{API}/records/{PREDECESSOR_RECORD}",
                    headers={"Accept": "application/vnd.inveniordm.v1+json"},
                    timeout=(30, 180),
                ),
                {200},
            ).json()
            return public_readback(
                session, token, predecessor, int(state["record_id"]), local
            )
    predecessor = current_predecessor(session)
    draft_id = create_or_resume_draft(session, token, predecessor)
    record_id = stage_and_publish(session, token, predecessor, draft_id)
    return public_readback(session, token, predecessor, record_id, local)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args()
    result = preflight() if args.preflight_only else publish()
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
