#!/usr/bin/env python3
"""Publish and read back the Tajik algebra source anchor.

The transaction is additive and same-concept only. It inherits the exact live
Interlanguage record server-side, uploads one compact deterministic ZIP, and
refuses a changed predecessor boundary or an untracked draft.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import time
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import quote

import publish_sga7_visual_evidence_zenodo_20260730 as base


API = "https://zenodo.org/api"
PUBLICATION_DATE = "2026-08-01"
CONCEPT_DOI = "10.5281/zenodo.21124403"
PREDECESSOR_RECORD = 21_743_417
PREDECESSOR_DOI = "10.5281/zenodo.21743417"
PREDECESSOR_FILES = 65
PREDECESSOR_BYTES = 4_976_131_237
FINAL_FILES = 66
FINAL_BYTES = 4_982_736_704
VERSION = "2026-08-01 v0.19 Tajik algebra source anchor"

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path("interlanguage-sidecar/20260801/tajik-algebra-source-anchor")
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
PUBLIC_NAME = "23_Tajik_Algebra_Source_Anchor_20260801.zip"
ZIP_BYTES = 6_605_467
ZIP_SHA256 = "2331C3AB1D9B8EC3A18C6822CC22EF394E5D516723A3CAC82D7DE328DA14F26F"
GITHUB_COMMIT = "5cefaa7772e69ace2b44b499d9819a6218049307"
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/tajik-algebra-source-anchor-20260801"
STATE_PATH = TEMP_ROOT / "draft_state.json"
PREPARE_PATH = TEMP_ROOT / "prepare_result.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"

EXPECTED_MEMBERS = {
    "README.md": (
        3_327,
        "89B6075C91EADEFFE0B04B11FE8DD3E10064512D69340B12E53207394BE8FBC5",
    ),
    "SOURCE_MANIFEST.csv": (
        1_065,
        "E7974B2078FAD703D6A9BB61DE584AE88F1A266E4CBF3F2CC953B073B5B0D964",
    ),
    "SOURCE_SNAPSHOT_METADATA_20260801.json": (
        3_507,
        "551306A7D98B0354878699A519AF242B70C5792FE42C0B4F9141BE355DEB07ED",
    ),
    "TAJIK_ALGEBRA_SCOPE_LEDGER_20260801.csv": (
        1_677,
        "039A1FB56D44A67C37B2692D333F9680B94BC7B9A942A1D2B760952E502E3FB9",
    ),
    "source/choriev_algebra_number_theory_course_manual_tajik.pdf": (
        1_487_129,
        "5A4B150F67B79009F0FDD207F46297A21F18913C83BACE38B1909A8712AFADAC",
    ),
    "source/davlatov_choriev_algebra_number_theory_part1_tajik.pdf": (
        5_283_895,
        "4862488CA3B492C10CC1893D921A110F0B39C2CD84FFCEC50FD612B631666181",
    ),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def replay_zip(data: bytes) -> dict[str, object]:
    if (len(data), sha256_bytes(data)) != (ZIP_BYTES, ZIP_SHA256):
        raise RuntimeError("Tajik source-anchor ZIP outer identity changed")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename for item in infos]
        if (
            archive.testzip() is not None
            or len(infos) != 6
            or len(names) != len(set(names))
            or set(names) != set(EXPECTED_MEMBERS)
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError("Tajik source-anchor ZIP boundary changed")
        identities = {}
        for name, wanted in EXPECTED_MEMBERS.items():
            member = archive.read(name)
            observed = (len(member), sha256_bytes(member))
            if observed != wanted:
                raise RuntimeError(f"Tajik source-anchor member changed: {name}")
            identities[name] = {"bytes": observed[0], "sha256": observed[1]}
        rows = list(
            csv.DictReader(
                io.StringIO(
                    archive.read("SOURCE_MANIFEST.csv").decode("utf-8-sig")
                )
            )
        )
        if len(rows) != 2:
            raise RuntimeError("Tajik source manifest row boundary changed")
        return {
            "status": "PASS",
            "members": len(infos),
            "uncompressed_bytes": sum(item.file_size for item in infos),
            "source_manifest_rows": len(rows),
            "member_identities": identities,
        }


def local_upload() -> dict[str, object]:
    path = PACKAGE_ROOT / PUBLIC_NAME
    observed = (path.stat().st_size, base.sha256_path(path))
    if observed != (ZIP_BYTES, ZIP_SHA256):
        raise RuntimeError("Local Tajik source-anchor identity changed")
    replay_zip(path.read_bytes())
    return {
        "path": path,
        "bytes": ZIP_BYTES,
        "sha256": ZIP_SHA256,
        "md5": base.md5_path(path),
    }


def github_readback(local: dict[str, object]) -> dict[str, object]:
    url = (
        "https://raw.githubusercontent.com/KokunoYumeto/"
        f"modern-latex-manuscripts/{GITHUB_COMMIT}/{PACKAGE_REL.as_posix()}/"
        f"{quote(PUBLIC_NAME, safe='')}"
    )
    session = base.make_session()
    data = base.check(session.get(url, timeout=(30, 300)), {200}).content
    observed = (len(data), sha256_bytes(data))
    wanted = (int(local["bytes"]), str(local["sha256"]))
    if observed != wanted:
        raise RuntimeError("GitHub Tajik source-anchor mismatch")
    return {
        "status": "PASS_GITHUB_PUBLIC_READBACK",
        "commit": GITHUB_COMMIT,
        "package_path": PACKAGE_REL.as_posix(),
        "file": PUBLIC_NAME,
        "bytes": observed[0],
        "sha256": observed[1],
        "zip_replay": replay_zip(data),
        "errors": [],
    }


def live_predecessor(session) -> dict:
    headers = {"Accept": "application/vnd.inveniordm.v1+json"}
    record = base.check(
        session.get(
            f"{API}/records/{PREDECESSOR_RECORD}/versions/latest",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = base.modern_entries(record)
    observed = (
        int(record["id"]),
        record["pids"]["doi"]["identifier"],
        record["parent"]["pids"]["doi"]["identifier"],
        len(entries),
        sum(int(entry["size"]) for entry in entries.values()),
        bool(record.get("is_published")),
    )
    expected = (
        PREDECESSOR_RECORD,
        PREDECESSOR_DOI,
        CONCEPT_DOI,
        PREDECESSOR_FILES,
        PREDECESSOR_BYTES,
        True,
    )
    if observed != expected:
        raise RuntimeError(f"Live Interlanguage predecessor changed: {observed!r}")
    if PUBLIC_NAME in entries:
        raise RuntimeError("Tajik source-anchor ZIP already exists on live head")
    return record


def create_or_resume_draft(session, token: str, predecessor: dict) -> int:
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {**auth, "Accept": "application/vnd.inveniordm.v1+json"}
    TEMP_ROOT.mkdir(parents=True, exist_ok=True)
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            return int(state["record_id"])
        draft_id = int(state["draft_id"])
        base.check(
            session.get(
                f"{API}/records/{draft_id}/draft",
                headers=vendor,
                timeout=(30, 180),
            ),
            {200},
        )
        return draft_id
    active = session.get(
        f"{API}/records/{PREDECESSOR_RECORD}/draft",
        headers=vendor,
        timeout=(30, 180),
    )
    if active.status_code == 200:
        raise RuntimeError("Untracked Interlanguage successor draft exists")
    base.check(active, {404})
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{PREDECESSOR_RECORD}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if deposition.get("state") != "done" or not deposition.get("submitted"):
        raise RuntimeError("Interlanguage predecessor is not a versioning base")
    created = base.check(
        session.post(
            deposition["links"]["newversion"],
            headers=auth,
            timeout=(30, 300),
        ),
        {201},
    ).json()
    draft = base.check(
        session.get(
            created["links"]["latest_draft"],
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    old_entries = base.modern_entries(predecessor)
    new_entries = base.legacy_entries(draft)
    if set(new_entries) != set(old_entries):
        raise RuntimeError("New draft did not inherit the exact predecessor set")
    for name, old in old_entries.items():
        new = new_entries[name]
        if (int(new["filesize"]), base.normalized_md5(new["checksum"])) != (
            int(old["size"]),
            base.normalized_md5(old["checksum"]),
        ):
            raise RuntimeError(f"Inherited predecessor changed: {name}")
    draft_id = int(draft["id"])
    base.save_json(
        STATE_PATH,
        {
            "status": "OPEN_TRACKED_DRAFT",
            "predecessor_record": PREDECESSOR_RECORD,
            "draft_id": draft_id,
            "published": False,
        },
    )
    return draft_id


def stage_and_publish(
    session,
    token: str,
    predecessor: dict,
    draft_id: int,
    local: dict[str, object],
) -> int:
    state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
    if state.get("published"):
        return int(state["record_id"])
    auth = {"Authorization": f"Bearer {token}"}
    vendor = {**auth, "Accept": "application/vnd.inveniordm.v1+json"}
    json_headers = {**vendor, "Content-Type": "application/json"}
    deposition = base.check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    files = base.legacy_entries(deposition)
    inherited = set(base.modern_entries(predecessor))
    expected = inherited | {PUBLIC_NAME}
    if not inherited.issubset(files) or not set(files).issubset(expected):
        raise RuntimeError("Tracked draft has an unexpected file set")
    existing = files.get(PUBLIC_NAME)
    wanted = (int(local["bytes"]), str(local["md5"]))
    if existing is not None:
        observed = (
            int(existing["filesize"]),
            base.normalized_md5(existing["checksum"]),
        )
        if observed != wanted:
            raise RuntimeError("Staged Tajik source anchor changed")
    else:
        bucket = deposition["links"]["bucket"].rstrip("/")
        with Path(local["path"]).open("rb") as handle:
            base.check(
                session.put(
                    f"{bucket}/{quote(PUBLIC_NAME, safe='')}",
                    headers={**auth, "Content-Type": "application/octet-stream"},
                    data=handle,
                    timeout=(30, 600),
                ),
                {200, 201},
            )
    draft = base.check(
        session.get(
            f"{API}/records/{draft_id}/draft",
            headers=vendor,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    entries = base.modern_entries(draft)
    if set(entries) != expected or len(entries) != FINAL_FILES:
        raise RuntimeError("Staged Interlanguage file set is not exact")
    metadata = draft["metadata"]
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = VERSION
    paragraph = (
        "<p><strong>Tajik algebra source anchor:</strong> one compact "
        "deterministic ZIP preserves two exact public-library Tajik algebra "
        "PDFs with source URLs, page identities, and a bounded topic ledger. "
        "It closes the Tajik algebra-source row, not native TeX. The source "
        "site reserves rights; no open license or certification claim is "
        "made.</p>"
    )
    if paragraph not in metadata.get("description", ""):
        metadata["description"] = metadata.get("description", "") + paragraph
    previous_order = list(draft["files"].get("order") or [])
    order = [name for name in previous_order if name in inherited]
    order.extend(sorted(inherited - set(order), key=str.casefold))
    order.append(PUBLIC_NAME)
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": draft["files"].get("default_preview"),
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
            headers=json_headers,
            json=payload,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if set(base.modern_entries(patched)) != expected:
        raise RuntimeError("Patched Interlanguage draft changed")
    published = base.check(
        session.post(
            patched["links"]["publish"],
            headers=vendor,
            timeout=(30, 300),
        ),
        {202},
    ).json()
    record_id = int(published["id"])
    state.update(
        {
            "status": "PUBLISHED_PENDING_READBACK",
            "published": True,
            "record_id": record_id,
            "doi": published["pids"]["doi"]["identifier"],
        }
    )
    base.save_json(STATE_PATH, state)
    return record_id


def public_readback(
    session,
    token: str,
    predecessor: dict,
    record_id: int,
    local: dict[str, object],
    github: dict[str, object],
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
        raise RuntimeError("Published Interlanguage successor is not readable")
    entries = base.modern_entries(record)
    if (
        len(entries) != FINAL_FILES
        or sum(int(item["size"]) for item in entries.values()) != FINAL_BYTES
        or record["parent"]["pids"]["doi"]["identifier"] != CONCEPT_DOI
        or record["metadata"].get("version") != VERSION
    ):
        raise RuntimeError("Published Interlanguage successor boundary changed")
    predecessor_entries = base.modern_entries(predecessor)
    retained_errors = []
    for name, old in predecessor_entries.items():
        new = entries.get(name)
        if new is None or (
            int(new["size"]),
            base.normalized_md5(new["checksum"]),
        ) != (int(old["size"]), base.normalized_md5(old["checksum"])):
            retained_errors.append(name)
    if retained_errors:
        raise RuntimeError(f"Retained predecessor changed: {retained_errors[:3]}")
    data = base.check(
        session.get(entries[PUBLIC_NAME]["links"]["content"], timeout=(30, 600)),
        {200},
    ).content
    observed = (len(data), sha256_bytes(data))
    wanted = (int(local["bytes"]), str(local["sha256"]))
    if observed != wanted:
        raise RuntimeError("Public Tajik source-anchor mismatch")
    zip_replay = replay_zip(data)
    latest = base.check(
        session.get(
            f"{API}/records/{record_id}/versions/latest",
            headers=headers,
            timeout=(30, 180),
        ),
        {200},
    ).json()
    if int(latest["id"]) != record_id:
        raise RuntimeError("Published successor is not the live concept head")
    auth_vendor = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    draft = session.get(
        f"{API}/records/{record_id}/draft",
        headers=auth_vendor,
        timeout=(30, 180),
    )
    base.check(draft, {404})
    result = {
        "status": "PASS_PUBLIC_READBACK",
        "record_id": record_id,
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "concept_doi": record["parent"]["pids"]["doi"]["identifier"],
        "predecessor_record": PREDECESSOR_RECORD,
        "outer_files": len(entries),
        "outer_bytes": sum(int(item["size"]) for item in entries.values()),
        "retained_predecessor_files": len(predecessor_entries),
        "retained_predecessor_identity_method": "Zenodo size and MD5 equality",
        "retained_predecessor_identity_errors": retained_errors,
        "new_file_readback": {
            PUBLIC_NAME: {"bytes": observed[0], "sha256": observed[1]}
        },
        "source_anchor_zip_readback": zip_replay,
        "github_readback": github,
        "default_preview_preserved": (
            record["files"].get("default_preview")
            == predecessor["files"].get("default_preview")
        ),
        "live_head_verified": True,
        "active_draft_remaining": False,
        "duplicate_concept_created": False,
        "errors": [],
    }
    RECEIPT_ROOT.mkdir(parents=True, exist_ok=True)
    receipt = RECEIPT_ROOT / (
        f"20260801_tajik_algebra_source_anchor_record_{record_id}_"
        "public_readback.json"
    )
    base.save_json(receipt, result)
    result["receipt_path"] = str(receipt)
    return result


def preflight() -> dict[str, object]:
    local = local_upload()
    github = github_readback(local)
    session = base.make_session()
    predecessor = live_predecessor(session)
    result = {
        "status": "PASS_READY_FOR_SINGLE_SAME_CONCEPT_SUCCESSOR",
        "predecessor_record": int(predecessor["id"]),
        "predecessor_files": len(base.modern_entries(predecessor)),
        "predecessor_bytes": sum(
            int(item["size"])
            for item in base.modern_entries(predecessor).values()
        ),
        "new_file": {
            PUBLIC_NAME: {"bytes": local["bytes"], "sha256": local["sha256"]}
        },
        "github_readback": github,
        "zip_replay": replay_zip(Path(local["path"]).read_bytes()),
        "errors": [],
    }
    TEMP_ROOT.mkdir(parents=True, exist_ok=True)
    base.save_json(PREPARE_PATH, result)
    return result


def publish() -> dict[str, object]:
    local = local_upload()
    github = github_readback(local)
    token = base.find_token()
    session = base.make_session()
    if STATE_PATH.is_file():
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("published"):
            predecessor = base.check(
                session.get(
                    f"{API}/records/{PREDECESSOR_RECORD}",
                    headers={"Accept": "application/vnd.inveniordm.v1+json"},
                    timeout=(30, 180),
                ),
                {200},
            ).json()
            return public_readback(
                session, token, predecessor, int(state["record_id"]), local, github
            )
    predecessor = live_predecessor(session)
    draft_id = create_or_resume_draft(session, token, predecessor)
    record_id = stage_and_publish(session, token, predecessor, draft_id, local)
    return public_readback(session, token, predecessor, record_id, local, github)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    args = parser.parse_args()
    result = preflight() if args.preflight else publish()
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
