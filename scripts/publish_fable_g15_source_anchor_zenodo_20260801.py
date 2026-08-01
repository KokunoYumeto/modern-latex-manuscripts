#!/usr/bin/env python3
"""Publish and read back the direct Fable G15 source anchor.

The transaction is additive and same-concept only. It inherits the exact live
Interlanguage record server-side and uploads five small source/control files.
The already-public provenance archive remains byte-identical and is not
duplicated.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path
from urllib.parse import quote

import publish_sga7_visual_evidence_zenodo_20260730 as base


API = "https://zenodo.org/api"
PUBLICATION_DATE = "2026-08-01"
CONCEPT_DOI = "10.5281/zenodo.21124403"
PREDECESSOR_RECORD = 21_739_167
PREDECESSOR_DOI = "10.5281/zenodo.21739167"
PREDECESSOR_FILES = 59
PREDECESSOR_BYTES = 4_976_099_640
FINAL_FILES = 64
FINAL_BYTES = 4_976_113_470
VERSION = "2026-08-01 v0.17 Fable G15 invariant-ledger source anchor"

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path(
    "interlanguage-sidecar/20260801/"
    "fable-g15-invariant-ledger-source-anchor"
)
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
GITHUB_COMMIT = "9975e8bbc4e40327758ef4cad183e18d7ce75162"
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/fable-g15-source-anchor-20260801"
STATE_PATH = TEMP_ROOT / "draft_state.json"
PREPARE_PATH = TEMP_ROOT / "prepare_result.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"

UPLOADS = {
    "21_Fable_G15_Invariant_Ledger_Gate_Map_20260801.md": (
        "INTERSLAVIC_GATE_MAP.md",
        7_691,
        "E714C7A1EEED2DC5B3DD5C2F2AD9184521E14225B82DE1F9E563D1F93987A6F7",
    ),
    "21a_Fable_G15_Source_Anchor_Readme_20260801.md": (
        "README.md",
        2_490,
        "B6C4F4AAA64B7A2B95C0F08B0B321712664037FA7C4BBC0C2D65A8B857D03CE8",
    ),
    "21b_Fable_G15_Source_Anchor_Metadata_20260801.json": (
        "SOURCE_ANCHOR_METADATA_20260801.json",
        1_962,
        "864A8482432D610EF51157A209C24DD024D2A31763FDE4369AA01B1B479DAE59",
    ),
    "21c_Fable_G15_Source_Anchor_Validation_20260801.json": (
        "PACKAGE_VALIDATION.json",
        1_177,
        "CF900C545866060E511D9E1F7D57740278334C5A76F6D899772A9DC393F7A1E7",
    ),
    "21d_Fable_G15_Source_Anchor_SHA256SUMS_20260801.csv": (
        "SHA256SUMS.csv",
        510,
        "6D2B688782EB7F49D23BA4F59371A604B7C4BC6EE8AA6D5F648E95F960EA9737",
    ),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def local_uploads() -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for public_name, (source_name, wanted_bytes, wanted_sha) in UPLOADS.items():
        path = PACKAGE_ROOT / source_name
        observed = (path.stat().st_size, base.sha256_path(path))
        if observed != (wanted_bytes, wanted_sha):
            raise RuntimeError(f"Local G15 source anchor changed: {source_name}")
        result[public_name] = {
            "path": path,
            "source_name": source_name,
            "bytes": wanted_bytes,
            "sha256": wanted_sha,
            "md5": base.md5_path(path),
        }
    if sum(int(item["bytes"]) for item in result.values()) != 13_830:
        raise RuntimeError("Local G15 source-anchor byte boundary changed")
    return result


def github_readback(local: dict[str, dict[str, object]]) -> dict[str, object]:
    root = (
        "https://raw.githubusercontent.com/KokunoYumeto/"
        f"modern-latex-manuscripts/{GITHUB_COMMIT}/{PACKAGE_REL.as_posix()}"
    )
    session = base.make_session()
    files = {}
    for item in local.values():
        source_name = str(item["source_name"])
        response = base.check(
            session.get(
                f"{root}/{quote(source_name, safe='/')}", timeout=(30, 300)
            ),
            {200},
        )
        data = response.content
        observed = (len(data), sha256_bytes(data))
        wanted = (int(item["bytes"]), str(item["sha256"]))
        if observed != wanted:
            raise RuntimeError(f"GitHub G15 source-anchor mismatch: {source_name}")
        files[source_name] = {"bytes": observed[0], "sha256": observed[1]}
    return {
        "status": "PASS_GITHUB_PUBLIC_READBACK",
        "commit": GITHUB_COMMIT,
        "package_path": PACKAGE_REL.as_posix(),
        "files_read_back": len(files),
        "files": files,
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
    if set(UPLOADS) & set(entries):
        raise RuntimeError("G15 source-anchor files already exist on the live head")
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
            deposition["links"]["newversion"], headers=auth, timeout=(30, 300)
        ),
        {201},
    ).json()
    draft = base.check(
        session.get(created["links"]["latest_draft"], headers=auth, timeout=(30, 180)),
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
    local: dict[str, dict[str, object]],
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
    expected = inherited | set(local)
    if not inherited.issubset(files) or not set(files).issubset(expected):
        raise RuntimeError("Tracked draft has an unexpected file set")
    bucket = deposition["links"]["bucket"].rstrip("/")
    for name, item in local.items():
        existing = files.get(name)
        wanted = (int(item["bytes"]), str(item["md5"]))
        if existing is not None:
            observed = (
                int(existing["filesize"]),
                base.normalized_md5(existing["checksum"]),
            )
            if observed != wanted:
                raise RuntimeError(f"Staged G15 source anchor changed: {name}")
            continue
        with Path(item["path"]).open("rb") as handle:
            base.check(
                session.put(
                    f"{bucket}/{quote(name, safe='')}",
                    headers={**auth, "Content-Type": "application/octet-stream"},
                    data=handle,
                    timeout=(30, 600),
                ),
                {200, 201},
            )
        files[name] = {"filesize": wanted[0], "checksum": f"md5:{wanted[1]}"}
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
        "<p><strong>Fable G15 source anchor:</strong> Gate 15 is identified "
        "directly as the invariant-ledger gate in the preserved "
        "<code>INTERSLAVIC_GATE_MAP.md</code>; the exact existing artifact is "
        "now exposed without duplicating the large provenance archive.</p>"
    )
    if paragraph not in metadata.get("description", ""):
        metadata["description"] = metadata.get("description", "") + paragraph
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": draft["files"].get("default_preview"),
            "order": sorted(expected, key=str.casefold),
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
        session.post(patched["links"]["publish"], headers=vendor, timeout=(30, 300)),
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
    local: dict[str, dict[str, object]],
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
    outer = {}
    for name, item in local.items():
        data = base.check(
            session.get(entries[name]["links"]["content"], timeout=(30, 600)),
            {200},
        ).content
        observed = (len(data), sha256_bytes(data))
        wanted = (int(item["bytes"]), str(item["sha256"]))
        if observed != wanted:
            raise RuntimeError(f"Public G15 source-anchor mismatch: {name}")
        outer[name] = {"bytes": observed[0], "sha256": observed[1]}
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
        "new_files_streamed": len(outer),
        "new_file_readback": outer,
        "github_readback": github,
        "live_head_verified": True,
        "active_draft_remaining": False,
        "duplicate_concept_created": False,
        "errors": [],
    }
    RECEIPT_ROOT.mkdir(parents=True, exist_ok=True)
    receipt = RECEIPT_ROOT / (
        f"20260801_fable_g15_source_anchor_record_{record_id}_public_readback.json"
    )
    base.save_json(receipt, result)
    result["receipt_path"] = str(receipt)
    return result


def preflight() -> dict[str, object]:
    local = local_uploads()
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
        "new_files": {
            name: {"bytes": item["bytes"], "sha256": item["sha256"]}
            for name, item in local.items()
        },
        "github_readback": github,
        "errors": [],
    }
    TEMP_ROOT.mkdir(parents=True, exist_ok=True)
    base.save_json(PREPARE_PATH, result)
    return result


def publish() -> dict[str, object]:
    local = local_uploads()
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
