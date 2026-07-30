#!/usr/bin/env python3
"""Add clean cumulative-reader bundles to the live SGA and EGA concepts."""

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
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


API = "https://zenodo.org/api"
PUBLICATION_DATE = "2026-07-30"
REPO_ROOT = Path(__file__).resolve().parent.parent
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
TEMP_ROOT = Path(os.environ["LOCALAPPDATA"]) / "Temp" / "current_reader_bundles_20260730"
TOKEN_LOG = Path(
    os.environ.get(
        "ZENODO_TOKEN_LOG",
        Path.home() / ".codex" / ".sandbox" / "sandbox.log",
    )
)


@dataclass(frozen=True)
class Surface:
    key: str
    predecessor_record: int
    predecessor_doi: str
    concept_doi: str
    predecessor_files: int
    predecessor_bytes: int
    bundle_name: str
    stale_bundle_names: tuple[str, ...]
    bundle_path: Path
    bundle_bytes: int
    bundle_sha256: str
    bundle_members: int
    bundle_uncompressed_bytes: int
    bundle_readers: tuple[str, ...]
    default_preview: str
    current_readers: tuple[str, ...]
    current_tex: tuple[str, ...]
    version: str
    description_paragraph: str


SURFACES = {
    "sga": Surface(
        key="sga",
        predecessor_record=21_700_836,
        predecessor_doi="10.5281/zenodo.21700836",
        concept_doi="10.5281/zenodo.20410947",
        predecessor_files=66,
        predecessor_bytes=420_985_368,
        bundle_name=(
            "00_Current_SGA1-6_English_Readers_and_Buildable_TeX_"
            "20260730.zip"
        ),
        stale_bundle_names=(),
        bundle_path=(
            REPO_ROOT
            / "sources/sga/sga1-6-current-readers-and-buildable-tex-bundle-20260730"
            / "00_Current_SGA1-6_English_Readers_and_Buildable_TeX_20260730.zip"
        ),
        bundle_bytes=23_619_688,
        bundle_sha256=(
            "33224AE03185DFF9F7C5FAF79D3B80D25504EAF1BCF338791B4DBD8A44AFD999"
        ),
        bundle_members=1_394,
        bundle_uncompressed_bytes=39_337_105,
        bundle_readers=tuple(
            f"SGA_Current_English_Readers_and_TeX_20260730/SGA{i}/reader/"
            f"SGA{i}_English_Reader.pdf"
            for i in range(1, 7)
        ),
        default_preview="00a_SGA1_English_Reader.pdf",
        current_readers=tuple(
            f"00{chr(96 + i)}_SGA{i}_English_Reader.pdf" for i in range(1, 7)
        ),
        current_tex=tuple(
            f"02{chr(96 + i)}_SGA{i}_English_Master.tex" for i in range(1, 7)
        ),
        version="2026-07-30 clean cumulative SGA1-6 reader and TeX bundle",
        description_paragraph=(
            "<p><strong>Start here:</strong> the first file is one clean ZIP "
            "containing the current cumulative English reader PDF for each of "
            "SGA 1 through SGA 6 together with its complete buildable TeX "
            "closure. The same six reader PDFs and master TeX files remain "
            "directly accessible immediately afterward.</p>"
        ),
    ),
    "ega": Surface(
        key="ega",
        predecessor_record=21_697_218,
        predecessor_doi="10.5281/zenodo.21697218",
        concept_doi="10.5281/zenodo.20414353",
        predecessor_files=28,
        predecessor_bytes=502_837_433,
        bundle_name=(
            "00 Current_EGA_English_Readers_and_Buildable_TeX_20260730.zip"
        ),
        stale_bundle_names=(
            "00_Current_EGA_English_Readers_and_Buildable_TeX_20260730.zip",
        ),
        bundle_path=(
            REPO_ROOT
            / "sources/ega/ega-current-readers-and-buildable-tex-bundle-20260730"
            / "00 Current_EGA_English_Readers_and_Buildable_TeX_20260730.zip"
        ),
        bundle_bytes=5_802_085,
        bundle_sha256=(
            "2CB037322063DF459EFC55CFCC9424E6F9EF4A6D59329C65FCE6F25715DAABA1"
        ),
        bundle_members=99,
        bundle_uncompressed_bytes=9_560_632,
        bundle_readers=(
            "EGA_Current_English_Readers_and_TeX_20260730/EGA0/reader/"
            "EGA0_English_Working_Reader.pdf",
            "EGA_Current_English_Readers_and_TeX_20260730/EGA2/reader/"
            "EGA2_English_Reader.pdf",
            "EGA_Current_English_Readers_and_TeX_20260730/EGA3/reader/"
            "EGA3_English_Working_Reader_Sections1_7.pdf",
            "EGA_Current_English_Readers_and_TeX_20260730/EGA4/reader/"
            "EGA4_English_Working_Reader_Sections1_10.pdf",
        ),
        default_preview=(
            "00a_EGA0_English_Working_Reader_Assigned_SourceFirst_"
            "Sections8_13_20260729.pdf"
        ),
        current_readers=(
            "00a_EGA0_English_Working_Reader_Assigned_SourceFirst_"
            "Sections8_13_20260729.pdf",
            "00b_EGA2_English_Reader.pdf",
            "00c_EGA3_English_Working_Reader_Assigned_SourceFirst_"
            "Sections1_7_20260729.pdf",
            "00d_EGA4_English_Sections1_10_Reader.pdf",
        ),
        current_tex=(
            "02a_EGA0_English_Working_Master_Assigned_SourceFirst_"
            "Sections8_13_20260729.tex",
            "02b_EGA2_English_Master.tex",
            "02c_EGA3_English_Working_Master_Assigned_SourceFirst_"
            "Sections1_7_20260729.tex",
            "02d_EGA4_English_Sections1_10_Master.tex",
        ),
        version="2026-07-30 clean cumulative EGA reader and TeX bundle",
        description_paragraph=(
            "<p><strong>Start here:</strong> the first file is one clean ZIP "
            "containing one cumulative English reader PDF for every current "
            "EGA scope in this record together with its complete buildable "
            "TeX closure. The same current readers and master TeX files remain "
            "directly accessible immediately afterward.</p>"
        ),
    ),
}


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
            f"{response.request.method} {response.url}: "
            f"{response.text[:2000]}"
        )
    return response


def modern_entries(record: dict) -> dict[str, dict]:
    return record["files"]["entries"]


def legacy_entries(record: dict) -> dict[str, dict]:
    return {entry["filename"]: entry for entry in record["files"]}


def safe_member(name: str) -> bool:
    normalized = name.replace("\\", "/")
    pure = PurePosixPath(normalized)
    return (
        normalized == name
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", normalized)
    )


def replay_zip(path: Path, surface: Surface) -> dict:
    with zipfile.ZipFile(path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        if len(infos) != surface.bundle_members:
            raise RuntimeError(
                f"{surface.key} ZIP member count changed: {len(infos)}"
            )
        names = [info.filename for info in infos]
        if len(names) != len(set(names)) or not all(map(safe_member, names)):
            raise RuntimeError(f"{surface.key} ZIP paths are unsafe or duplicate")
        if sum(info.file_size for info in infos) != surface.bundle_uncompressed_bytes:
            raise RuntimeError(f"{surface.key} ZIP uncompressed byte count changed")
        if not set(surface.bundle_readers).issubset(names):
            raise RuntimeError(f"{surface.key} cumulative readers missing from ZIP")
        manifest_names = [name for name in names if name.endswith("/SHA256SUMS.csv")]
        if len(manifest_names) != 1:
            raise RuntimeError(f"{surface.key} ZIP manifest count is not one")
        manifest_name = manifest_names[0]
        root_prefix = manifest_name.rsplit("/", 1)[0] + "/"
        rows = list(
            csv.DictReader(
                io.StringIO(archive.read(manifest_name).decode("utf-8-sig"))
            )
        )
        if len(rows) != len(infos) - 1:
            raise RuntimeError(f"{surface.key} ZIP manifest row count changed")
        observed = {}
        for row in rows:
            relative_name = row["relative_path"]
            name = root_prefix + relative_name
            if name in observed or name == manifest_name:
                raise RuntimeError(f"{surface.key} ZIP manifest path error: {name}")
            data = archive.read(name)
            identity = (len(data), hashlib.sha256(data).hexdigest().upper())
            expected = (int(row["bytes"]), row["sha256"].upper())
            if identity != expected:
                raise RuntimeError(f"{surface.key} ZIP member mismatch: {name}")
            observed[name] = {
                "bytes": identity[0],
                "sha256": identity[1],
            }
        if set(observed) != set(names) - {manifest_name}:
            raise RuntimeError(f"{surface.key} ZIP manifest closure changed")
        manifest_data = archive.read(manifest_name)
        observed[manifest_name] = {
            "bytes": len(manifest_data),
            "sha256": hashlib.sha256(manifest_data).hexdigest().upper(),
        }
        return {
            "status": "PASS",
            "zip": path.name,
            "members": len(infos),
            "uncompressed_bytes": sum(info.file_size for info in infos),
            "manifest": manifest_name,
            "manifest_rows": len(rows),
            "required_cumulative_readers": list(surface.bundle_readers),
            "member_identities": observed,
        }


def preflight(
    session: requests.Session,
    token: str,
    surface: Surface,
) -> dict:
    path = surface.bundle_path
    identity = (path.stat().st_size, sha256_path(path))
    if identity != (surface.bundle_bytes, surface.bundle_sha256):
        raise RuntimeError(f"{surface.key} local bundle identity changed")
    replay_zip(path, surface)

    public_headers = {"Accept": "application/vnd.inveniordm.v1+json"}
    live = check(
        session.get(
            f"{API}/records/{surface.predecessor_record}/versions/latest",
            headers=public_headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = modern_entries(live)
    observed = (
        int(live["id"]),
        live["pids"]["doi"]["identifier"],
        live["parent"]["pids"]["doi"]["identifier"],
        len(entries),
        sum(int(entry["size"]) for entry in entries.values()),
        live["files"].get("default_preview"),
    )
    expected = (
        surface.predecessor_record,
        surface.predecessor_doi,
        surface.concept_doi,
        surface.predecessor_files,
        surface.predecessor_bytes,
        surface.default_preview,
    )
    if observed != expected:
        raise RuntimeError(
            f"{surface.key} live predecessor boundary changed: {observed!r}"
        )
    if surface.bundle_name in entries:
        raise RuntimeError(f"{surface.key} bundle is already present")
    auth_headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    state_path = TEMP_ROOT / f"{surface.key}_draft_state.json"
    if state_path.is_file():
        state = json.loads(state_path.read_text(encoding="utf-8"))
        if not state.get("published"):
            tracked = session.get(
                f"{API}/records/{int(state['draft_id'])}/draft",
                headers=auth_headers,
                timeout=(30, 60),
            )
            check(tracked, {200})
            if int(tracked.json()["id"]) != int(state["draft_id"]):
                raise RuntimeError(f"Tracked {surface.key} draft identity changed")
    else:
        active = session.get(
            f"{API}/records/{surface.predecessor_record}/draft",
            headers=auth_headers,
            timeout=(30, 60),
        )
        if active.status_code == 200:
            raise RuntimeError(f"Untracked {surface.key} successor draft exists")
        check(active, {404})
    return live


def create_or_resume_draft(
    session: requests.Session,
    token: str,
    surface: Surface,
    live: dict,
) -> int:
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {**auth, "Accept": "application/vnd.inveniordm.v1+json"}
    state_path = TEMP_ROOT / f"{surface.key}_draft_state.json"
    if state_path.is_file():
        state = json.loads(state_path.read_text(encoding="utf-8"))
        if state.get("published"):
            raise RuntimeError(f"Tracked {surface.key} successor is published")
        draft_id = int(state["draft_id"])
        tracked = session.get(
            f"{API}/records/{draft_id}/draft",
            headers=vendor,
            timeout=(30, 60),
        )
        check(tracked, {200})
        return draft_id
    active = session.get(
        f"{API}/records/{surface.predecessor_record}/draft",
        headers=vendor,
        timeout=(30, 60),
    )
    if active.status_code == 200:
        state = json.loads(state_path.read_text(encoding="utf-8"))
        draft_id = int(active.json()["id"])
        if draft_id != int(state["draft_id"]):
            raise RuntimeError(f"Tracked {surface.key} draft identity changed")
        return draft_id
    check(active, {404})

    predecessor = check(
        session.get(
            f"{API}/deposit/depositions/{surface.predecessor_record}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if (
        predecessor.get("state") != "done"
        or not predecessor.get("submitted")
        or not predecessor.get("links", {}).get("newversion")
    ):
        raise RuntimeError(f"{surface.key} predecessor is not a versioning base")
    created = check(
        session.post(
            predecessor["links"]["newversion"],
            headers=auth,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    deposition = check(
        session.get(
            created["links"]["latest_draft"],
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if set(legacy_entries(deposition)) != set(modern_entries(live)):
        raise RuntimeError(f"{surface.key} successor did not inherit predecessor")
    draft_id = int(deposition["id"])
    save_json(
        state_path,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "surface": surface.key,
            "predecessor_record": surface.predecessor_record,
            "draft_id": draft_id,
            "published": False,
        },
    )
    return draft_id


def ordered_names(surface: Surface, predecessor_names: set[str]) -> list[str]:
    current = set(surface.current_readers) | set(surface.current_tex)
    if not current.issubset(predecessor_names):
        raise RuntimeError(f"{surface.key} current direct objects are incomplete")
    remainder = predecessor_names - current
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
    return (
        [surface.bundle_name]
        + list(surface.current_readers)
        + list(surface.current_tex)
        + other_pdfs
        + other_tex
        + archival
    )


def stage_and_publish(
    session: requests.Session,
    token: str,
    surface: Surface,
    live: dict,
    draft_id: int,
) -> int:
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
    predecessor_names = set(modern_entries(live))
    expected_names = predecessor_names | {surface.bundle_name}
    files = legacy_entries(deposition)
    stale_names = set(surface.stale_bundle_names)
    allowed_stale = predecessor_names | stale_names
    if set(files) not in (predecessor_names, expected_names, allowed_stale):
        raise RuntimeError(f"{surface.key} draft has an unexpected file set")
    for stale_name in stale_names & set(files):
        check(
            session.delete(
                files[stale_name]["links"]["self"],
                headers=auth,
                timeout=(30, 300),
            ),
            {204},
        )
    if stale_names & set(files):
        deposition = check(
            session.get(
                f"{API}/deposit/depositions/{draft_id}",
                headers=auth,
                timeout=(30, 180),
            ),
            {200},
        ).json()
        files = legacy_entries(deposition)
    existing = files.get(surface.bundle_name)
    wanted_md5 = md5_path(surface.bundle_path)
    if existing is not None:
        observed = (
            int(existing["filesize"]),
            normalized_md5(existing["checksum"]),
        )
        if observed != (surface.bundle_bytes, wanted_md5):
            raise RuntimeError(f"{surface.key} staged bundle identity changed")
    else:
        bucket = deposition["links"]["bucket"].rstrip("/")
        with surface.bundle_path.open("rb") as handle:
            check(
                session.put(
                    f"{bucket}/{quote(surface.bundle_name, safe='')}",
                    headers={
                        **auth,
                        "Content-Type": "application/octet-stream",
                    },
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
    if set(entries) != expected_names:
        raise RuntimeError(f"{surface.key} staged file set is not exact")
    bundle_entry = entries[surface.bundle_name]
    if (
        int(bundle_entry["size"]),
        normalized_md5(bundle_entry["checksum"]),
    ) != (surface.bundle_bytes, wanted_md5):
        raise RuntimeError(f"{surface.key} staged bundle checksum changed")

    metadata = draft["metadata"]
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = surface.version
    description = metadata.get("description", "")
    if surface.description_paragraph not in description:
        metadata["description"] = surface.description_paragraph + "\n" + description
    order = ordered_names(surface, predecessor_names)
    if len(order) != len(expected_names) or set(order) != expected_names:
        raise RuntimeError(f"{surface.key} final order is not a permutation")
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": surface.default_preview,
            "order": order,
        },
        "metadata": metadata,
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
        or patched["files"].get("default_preview") != surface.default_preview
    ):
        raise RuntimeError(f"{surface.key} patched draft controls changed")
    api_order = patched["files"].get("order") or []
    if api_order and api_order != order:
        raise RuntimeError(f"{surface.key} API returned a conflicting file order")
    if sorted(expected_names, key=str.casefold)[0] != surface.bundle_name:
        raise RuntimeError(f"{surface.key} bundle does not sort first")
    published = check(
        session.post(
            patched["links"]["publish"],
            headers=vendor,
            timeout=(30, 300),
        ),
        {202},
    ).json()
    record_id = int(published["id"])
    state_path = TEMP_ROOT / f"{surface.key}_draft_state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    state.update(
        {
            "published": True,
            "record_id": record_id,
            "doi": published["pids"]["doi"]["identifier"],
        }
    )
    save_json(state_path, state)
    return record_id


def stream_download(session: requests.Session, url: str, path: Path) -> tuple[int, str]:
    path.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    total = 0
    with check(session.get(url, stream=True, timeout=(30, 1800)), {200}) as response:
        with path.open("wb") as handle:
            for block in response.iter_content(4 * 1024 * 1024):
                if block:
                    handle.write(block)
                    digest.update(block)
                    total += len(block)
    return total, digest.hexdigest().upper()


def public_readback(
    session: requests.Session,
    surface: Surface,
    predecessor: dict,
    record_id: int,
) -> dict:
    headers = {"Accept": "application/vnd.inveniordm.v1+json"}
    record = None
    for _ in range(30):
        response = session.get(
            f"{API}/records/{record_id}", headers=headers, timeout=(30, 180)
        )
        if response.status_code == 200:
            candidate = response.json()
            if candidate.get("is_published"):
                record = candidate
                break
        time.sleep(2)
    if record is None:
        raise RuntimeError(f"{surface.key} public record did not become readable")
    entries = modern_entries(record)
    predecessor_entries = modern_entries(predecessor)
    expected_names = set(predecessor_entries) | {surface.bundle_name}
    expected_order = ordered_names(surface, set(predecessor_entries))
    if (
        set(entries) != expected_names
        or len(entries) != surface.predecessor_files + 1
        or record["parent"]["pids"]["doi"]["identifier"] != surface.concept_doi
        or record["files"].get("default_preview") != surface.default_preview
    ):
        raise RuntimeError(f"{surface.key} public record boundary changed")
    api_order = record["files"].get("order") or []
    if api_order and api_order != expected_order:
        raise RuntimeError(f"{surface.key} public API file order conflicts")
    if sorted(entries, key=str.casefold)[0] != surface.bundle_name:
        raise RuntimeError(f"{surface.key} public bundle does not sort first")
    retained = 0
    retained_bytes = 0
    retained_entries = {}
    for name, old in predecessor_entries.items():
        new = entries[name]
        identity = (int(new["size"]), normalized_md5(new["checksum"]))
        expected = (int(old["size"]), normalized_md5(old["checksum"]))
        if identity != expected:
            raise RuntimeError(f"{surface.key} retained file changed: {name}")
        retained += 1
        retained_bytes += identity[0]
        retained_entries[name] = {
            "bytes": identity[0],
            "md5": identity[1],
        }
    bundle_url = entries[surface.bundle_name]["links"]["content"]
    destination = TEMP_ROOT / surface.key / surface.bundle_name
    observed_bundle = stream_download(session, bundle_url, destination)
    if observed_bundle != (surface.bundle_bytes, surface.bundle_sha256):
        raise RuntimeError(f"{surface.key} remote bundle SHA-256 changed")
    zip_receipt = replay_zip(destination, surface)
    outer = {
        name: {
            "bytes": int(entry["size"]),
            "md5": normalized_md5(entry["checksum"]),
        }
        for name, entry in entries.items()
    }
    result = {
        "status": "PASS_PUBLIC_READBACK",
        "surface": surface.key,
        "record_id": int(record["id"]),
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": record["parent"]["pids"]["doi"]["identifier"],
        "predecessor_record": surface.predecessor_record,
        "outer_files": len(entries),
        "outer_bytes": sum(int(entry["size"]) for entry in entries.values()),
        "retained_predecessor_files": retained,
        "retained_predecessor_bytes": retained_bytes,
        "bundle": {
            "name": surface.bundle_name,
            "bytes": observed_bundle[0],
            "sha256": observed_bundle[1],
            "content_url": bundle_url,
        },
        "default_preview": record["files"].get("default_preview"),
        "configured_file_order": expected_order,
        "api_file_order": api_order,
        "lexicographic_first_file": sorted(entries, key=str.casefold)[0],
        "outer_file_identities": outer,
        "retained_file_identities": retained_entries,
        "zip_readback": zip_receipt,
    }
    prefix = f"20260730_{surface.key}_current_reader_bundle_record_{record_id}"
    save_json(RECEIPT_ROOT / f"{prefix}_public_readback.json", result)
    save_json(RECEIPT_ROOT / f"{prefix}_zip_member_readback.json", zip_receipt)
    return result


def publish_surface(
    session: requests.Session,
    token: str,
    surface: Surface,
) -> dict:
    predecessor = preflight(session, token, surface)
    draft_id = create_or_resume_draft(session, token, surface, predecessor)
    record_id = stage_and_publish(
        session, token, surface, predecessor, draft_id
    )
    return public_readback(session, surface, predecessor, record_id)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--surface", choices=("sga", "ega", "all"), default="all"
    )
    args = parser.parse_args()
    token = find_token()
    session = make_session()
    selected = (
        tuple(SURFACES.values())
        if args.surface == "all"
        else (SURFACES[args.surface],)
    )
    results = []
    for surface in selected:
        results.append(publish_surface(session, token, surface))
        print(
            f"{surface.key.upper()} PASS: record "
            f"{results[-1]['record_id']} / {results[-1]['doi']}"
        )
    save_json(TEMP_ROOT / "publication_summary.json", results)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
