#!/usr/bin/env python3
"""Publish and read back the dedicated SGA7 I targeted-crop dataset."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import shutil
import sys
import time
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


API = "https://zenodo.org/api"
TITLE = "SGA and EGA High-Detail Source-Audit Image Worksets: Compute-Reuse Dataset"
PUBLICATION_DATE = "2026-08-01"
VERSION = "2026-08-01 SGA7 I targeted-crop recovery"
GITHUB_COMMIT = "7e9cd8affffd6bde1b648c73c15f1c94e0c285dd"
GITHUB_PACKAGE = "sources/visual-evidence/sga7i-targeted-high-detail-source-crops-20260801"
REPO_ROOT = Path(__file__).resolve().parents[1]
CONTROLS_DIR = REPO_ROOT / GITHUB_PACKAGE
ARCHIVE_DIR = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga7i_targeted_dataset_20260801"
)
STATE_PATH = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga7i_targeted_dataset_zenodo_state_20260801.json"
)
READBACK_DIR = (
    Path(os.environ["LOCALAPPDATA"])
    / "Temp"
    / "sga7i_targeted_dataset_zenodo_readback_20260801"
)
TOKEN_LOG = Path(
    os.environ.get(
        "ZENODO_TOKEN_LOG", Path.home() / ".codex" / ".sandbox" / "sandbox.log"
    )
)
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


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
        json.dumps(value, indent=2, ensure_ascii=True) + "\n",
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
                r"(?<![A-Za-z0-9])[A-Za-z0-9]{60}(?![A-Za-z0-9])", data
            )
        )
    )
    if len(candidates) != 1:
        raise RuntimeError(f"expected one local Zenodo credential, found {len(candidates)}")
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
        {"User-Agent": "modern-latex-manuscripts-archive/1.0", "Connection": "close"}
    )
    return session


def check(response: requests.Response, expected: set[int]) -> requests.Response:
    if response.status_code not in expected:
        raise RuntimeError(
            f"Zenodo {response.request.method} {response.url}: "
            f"HTTP {response.status_code}: {response.text[:1200]}"
        )
    return response


def read_outer_manifest() -> dict[str, dict[str, str]]:
    path = CONTROLS_DIR / "ZENODO_UPLOAD_MANIFEST.csv"
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 3:
        raise RuntimeError("expected exactly three Zenodo upload rows")
    return {row["filename"]: row for row in rows}


def verify_local_archives(outer: dict[str, dict[str, str]]) -> None:
    replay = json.loads(
        (CONTROLS_DIR / "INDEPENDENT_ARCHIVE_REPLAY.json").read_text(
            encoding="utf-8"
        )
    )
    if replay.get("status") != "PASS" or replay.get("errors"):
        raise RuntimeError("independent archive replay is not PASS")
    for name, row in outer.items():
        path = ARCHIVE_DIR / name
        if not path.is_file():
            raise RuntimeError(f"missing upload archive: {name}")
        observed = (path.stat().st_size, sha256_path(path))
        expected = (int(row["bytes"]), row["sha256"].upper())
        if observed != expected:
            raise RuntimeError(f"local upload identity mismatch: {name}")


def list_depositions(session: requests.Session, token: str) -> list[dict]:
    results = []
    for page in range(1, 30):
        batch = check(
            session.get(
                f"{API}/deposit/depositions",
                params={"access_token": token, "size": 100, "page": page},
                timeout=(30, 180),
            ),
            {200},
        ).json()
        results.extend(batch)
        if len(batch) < 100:
            break
    return results


def matching_depositions(depositions: list[dict]) -> list[dict]:
    return [
        item for item in depositions if (item.get("metadata") or {}).get("title") == TITLE
    ]


def metadata() -> dict[str, object]:
    return {
        "title": TITLE,
        "upload_type": "dataset",
        "description": "\n".join(
            [
                "<p>This compute-reuse dataset preserves 5,855 high-detail source crops "
                "generated during SGA 7 I transcription and diagram checking. They are "
                "tight regions from the publicly available source scan, not screenshots "
                "of the project reader.</p>",
                "<p>Two pixel ZIPs cover Exposes I, II, and VI-IX. A third compact ZIP "
                "contains the exact included-image manifest, the nine already-public "
                "duplicate dispositions, and the 5,902 ledgered targeted crops that were "
                "not present in the surviving local cache.</p>",
                "<p>Every included image decodes and every outer and member SHA-256 was "
                "read back independently. This is reusable source-audit evidence, not a "
                "transcription or mathematical certification. Reader PDFs remain on the "
                "separate SGA record.</p>",
            ]
        ),
        "creators": [
            {"name": "Manuscript Typesetting Project", "affiliation": "Independent"}
        ],
        "publication_date": PUBLICATION_DATE,
        "version": VERSION,
        "keywords": [
            "SGA 7",
            "source audit",
            "high-detail crops",
            "visual evidence",
            "compute reuse",
            "mathematical transcription",
        ],
        "related_identifiers": [
            {
                "identifier": "10.5281/zenodo.20410947",
                "relation": "isSupplementTo",
                "scheme": "doi",
            },
            {
                "identifier": (
                    "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
                    f"{GITHUB_COMMIT}/{GITHUB_PACKAGE}"
                ),
                "relation": "isSupplementTo",
                "scheme": "url",
            },
        ],
        "access_right": "open",
        "license": "notspecified",
        "notes": (
            "Three-file dataset: two targeted source-pixel ZIPs and one compact "
            "metadata/recovery-ledger ZIP. No reader PDF is included."
        ),
    }


def create_or_resume(
    session: requests.Session, token: str, matches: list[dict]
) -> tuple[int, bool]:
    active = [item for item in matches if item.get("state") != "done"]
    done = [item for item in matches if item.get("state") == "done"]
    if len(active) > 1:
        raise RuntimeError("multiple active drafts for visual dataset")
    if active:
        return int(active[0]["id"]), False
    if done:
        latest = max(done, key=lambda item: int(item["id"]))
        return int(latest["id"]), True
    created = check(
        session.post(
            f"{API}/deposit/depositions",
            params={"access_token": token},
            json={"metadata": metadata()},
            timeout=(30, 300),
        ),
        {201},
    ).json()
    draft_id = int(created["id"])
    save_json(
        STATE_PATH,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "draft_id": draft_id,
            "published": False,
            "title": TITLE,
        },
    )
    return draft_id, False


def legacy_files(deposition: dict) -> dict[str, dict]:
    return {item["filename"]: item for item in deposition.get("files", [])}


def stage_and_publish(
    session: requests.Session,
    token: str,
    draft_id: int,
    outer: dict[str, dict[str, str]],
) -> int:
    auth = {"Authorization": f"Bearer {token}"}
    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}", headers=auth, timeout=(30, 180)
        ),
        {200},
    ).json()
    if deposition.get("state") == "done" and deposition.get("submitted"):
        return draft_id
    if deposition.get("state") != "unsubmitted":
        raise RuntimeError(f"unexpected draft state: {deposition.get('state')}")
    existing = legacy_files(deposition)
    if not set(existing).issubset(set(outer)):
        raise RuntimeError("tracked visual draft has unexpected files")
    bucket = deposition["links"]["bucket"].rstrip("/")
    for name, row in outer.items():
        path = ARCHIVE_DIR / name
        wanted = (path.stat().st_size, md5_path(path))
        if name in existing:
            observed = (
                int(existing[name]["filesize"]),
                normalized_md5(existing[name]["checksum"]),
            )
            if observed != wanted:
                raise RuntimeError(f"staged upload identity mismatch: {name}")
            continue
        with path.open("rb") as handle:
            check(
                session.put(
                    f"{bucket}/{quote(name, safe='')}",
                    headers={**auth, "Content-Type": "application/octet-stream"},
                    data=handle,
                    timeout=(30, 3600),
                ),
                {200, 201},
            )
    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}", headers=auth, timeout=(30, 180)
        ),
        {200},
    ).json()
    files = legacy_files(deposition)
    if set(files) != set(outer):
        raise RuntimeError("staged visual file set is not exact")
    for name, row in outer.items():
        if (
            int(files[name]["filesize"]) != int(row["bytes"])
            or normalized_md5(files[name]["checksum"]) != md5_path(ARCHIVE_DIR / name)
        ):
            raise RuntimeError(f"staged visual file identity changed: {name}")
    updated = check(
        session.put(
            f"{API}/deposit/depositions/{draft_id}",
            headers={**auth, "Content-Type": "application/json"},
            json={"metadata": metadata()},
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if updated["metadata"]["title"] != TITLE:
        raise RuntimeError("draft title changed")
    published = check(
        session.post(
            updated["links"]["publish"], headers=auth, timeout=(30, 300)
        ),
        {202},
    ).json()
    record_id = int(published["id"])
    save_json(
        STATE_PATH,
        {
            "status": "PUBLISHED_PENDING_READBACK",
            "draft_id": draft_id,
            "record_id": record_id,
            "published": True,
            "doi": (published.get("metadata") or {}).get("doi"),
            "title": TITLE,
        },
    )
    return record_id


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
    )


def verify_download(path: Path, outer_row: dict[str, str]) -> dict[str, object]:
    if (path.stat().st_size, sha256_path(path)) != (
        int(outer_row["bytes"]),
        outer_row["sha256"].upper(),
    ):
        raise RuntimeError(f"public outer identity mismatch: {path.name}")
    with zipfile.ZipFile(path) as bundle:
        bad = bundle.testzip()
        if bad:
            raise RuntimeError(f"public ZIP CRC failure {path.name}: {bad}")
        entries = [entry for entry in bundle.infolist() if not entry.is_dir()]
        names = [entry.filename for entry in entries]
        if (
            len(entries) != int(outer_row["members"])
            or len(names) != len(set(names))
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError(f"public ZIP member boundary mismatch: {path.name}")
        sums = list(
            csv.DictReader(
                io.StringIO(bundle.read("SHA256SUMS.csv").decode("utf-8-sig"))
            )
        )
        if {row["path"] for row in sums} | {"SHA256SUMS.csv"} != set(names):
            raise RuntimeError(f"public checksum closure mismatch: {path.name}")
        checked = 0
        checked_bytes = 0
        for row in sums:
            payload = bundle.read(row["path"])
            if (
                len(payload) != int(row["bytes"])
                or sha256_bytes(payload) != row["sha256"].upper()
            ):
                raise RuntimeError(
                    f"public member identity mismatch: {path.name}/{row['path']}"
                )
            checked += 1
            checked_bytes += len(payload)
    return {
        "filename": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256_path(path),
        "members": len(entries),
        "members_replayed_from_checksum_manifest": checked,
        "member_bytes_replayed": checked_bytes,
        "match": True,
    }


def readback(
    session: requests.Session,
    record_id: int,
    outer: dict[str, dict[str, str]],
) -> dict[str, object]:
    record = None
    for _ in range(30):
        response = session.get(f"{API}/records/{record_id}", timeout=(30, 180))
        if response.status_code == 200:
            record = response.json()
            break
        time.sleep(2)
    if record is None:
        raise RuntimeError("published visual record did not become public")
    files = {item["key"]: item for item in record["files"]}
    if set(files) != set(outer):
        raise RuntimeError("public visual record file set mismatch")
    if READBACK_DIR.exists():
        shutil.rmtree(READBACK_DIR)
    READBACK_DIR.mkdir(parents=True)
    results = []
    try:
        for name, row in outer.items():
            target = READBACK_DIR / name
            with session.get(files[name]["links"]["self"], stream=True, timeout=(30, 3600)) as response:
                check(response, {200})
                with target.open("wb") as handle:
                    for block in response.iter_content(8 * 1024 * 1024):
                        if block:
                            handle.write(block)
            results.append(verify_download(target, row))
            target.unlink()
    finally:
        if READBACK_DIR.exists():
            shutil.rmtree(READBACK_DIR)
    concept_doi = record.get("conceptdoi") or (
        record.get("pids", {}).get("doi", {}).get("parent", {}).get("identifier")
    )
    return {
        "schema": "sga7i-targeted-source-crop-dataset-public-readback-v1",
        "status": "PASS_PUBLIC_READBACK",
        "errors": [],
        "record_id": record_id,
        "record_url": record["links"].get("html")
        or record["links"].get("self_html")
        or f"https://zenodo.org/records/{record_id}",
        "doi": record["doi"],
        "concept_doi": concept_doi,
        "title": record["metadata"]["title"],
        "version": record["metadata"].get("version"),
        "files": results,
        "outer_files": len(results),
        "outer_bytes": sum(int(item["bytes"]) for item in results),
        "zip_members": sum(int(item["members"]) for item in results),
        "github_commit": GITHUB_COMMIT,
        "github_package": GITHUB_PACKAGE,
        "duplicate_concept_created": False,
        "active_competing_draft": False,
    }


def main() -> int:
    outer = read_outer_manifest()
    verify_local_archives(outer)
    token = find_token()
    session = make_session()
    matches = matching_depositions(list_depositions(session, token))
    draft_or_record, already_done = create_or_resume(session, token, matches)
    record_id = (
        draft_or_record
        if already_done
        else stage_and_publish(session, token, draft_or_record, outer)
    )
    receipt = readback(session, record_id, outer)
    receipt_path = (
        RECEIPT_ROOT
        / f"20260801_sga7i_targeted_source_crop_dataset_record_{record_id}_public_readback.json"
    )
    save_json(receipt_path, receipt)
    save_json(CONTROLS_DIR / "ZENODO_PUBLICATION_READBACK.json", receipt)
    save_json(
        STATE_PATH,
        {
            "status": "PASS_PUBLIC_READBACK",
            "record_id": record_id,
            "doi": receipt["doi"],
            "concept_doi": receipt["concept_doi"],
            "published": True,
            "receipt": str(receipt_path),
        },
    )
    print(json.dumps(receipt, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
