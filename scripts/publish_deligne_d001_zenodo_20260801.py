#!/usr/bin/env python3
"""Publish Deligne D001 through one exact existing-concept successor."""

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
CONCEPT_DOI = "10.5281/zenodo.20410853"
PREDECESSOR_RECORD = 21_212_608
PREDECESSOR_DOI = "10.5281/zenodo.21212608"
PREDECESSOR_FILES = 6
PREDECESSOR_BYTES = 469_308_421
FINAL_FILES = 10
FINAL_BYTES = 486_525_402
PUBLICATION_DATE = "2026-08-01"
VERSION = "2026-08-01 D001 bilingual source-aligned checkpoint"
GITHUB_COMMIT = "de780b00c652e317b900b37d21a1f9bdbc0f387d"

REPO_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_REL = Path("sources/deligne/d001-bilingual-source-aligned-20260801")
PACKAGE_ROOT = REPO_ROOT / PACKAGE_REL
PUBLIC_ROOT = PACKAGE_ROOT / "public_files"
UPLOAD_MANIFEST = PACKAGE_ROOT / "ZENODO_UPLOAD_MANIFEST.csv"
TEMP_ROOT = REPO_ROOT / "tmp/zenodo/deligne-d001-20260801"
STATE_PATH = TEMP_ROOT / "draft_state.json"
PREPARE_PATH = TEMP_ROOT / "prepare_result.json"
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"

DEFAULT_PREVIEW = (
    "00_Deligne_Sequential_Cumulative_Papers_001_016p080_"
    "English_WorkingDraft.pdf"
)
PREDECESSOR_ORDER = [
    DEFAULT_PREVIEW,
    "01_Deligne_Sequential_Cumulative_Papers_001_016p080_French_WorkingDraft.pdf",
    "02_Deligne_English_Paper_and_Letter_PDFs_20260706.zip",
    "03_Deligne_French_Paper_and_Letter_PDFs_20260706.zip",
    "04_Deligne_TeX_Source_QA_and_Update_Packets_20260706.zip",
    "99_Deligne_Public_Status_NotCritical_20260706.md",
]
NEW_ORDER = [
    "05_Deligne_D001_Bilingual_SourceAligned_Reader_20260801.pdf",
    "06_Deligne_D001_English_SourceAligned_20260801.pdf",
    "07_Deligne_D001_French_SourceAligned_20260801.pdf",
    "08_Deligne_D001_TeX_and_Decisive_Source_Crops_20260801.zip",
]
FINAL_ORDER = PREDECESSOR_ORDER[:5] + NEW_ORDER + PREDECESSOR_ORDER[5:]
EXPECTED_UPLOADS = {
    "05_Deligne_D001_Bilingual_SourceAligned_Reader_20260801.pdf": (
        141_068,
        "54F6BF7B9C98BEF76B2F6DD54DAB763C9A25CBC7796963CD0704473D664A04B5",
    ),
    "06_Deligne_D001_English_SourceAligned_20260801.pdf": (
        73_198,
        "04F6882A0BF898701424C05AC8866ED4F3350BC5AC910E7C45C93BCA73EC1FF5",
    ),
    "07_Deligne_D001_French_SourceAligned_20260801.pdf": (
        65_284,
        "28B3E4D7688E705E2F875C31B62D8146BAB8C88712268F1524EA6F320D8D4B0D",
    ),
    "08_Deligne_D001_TeX_and_Decisive_Source_Crops_20260801.zip": (
        16_937_431,
        "B439BA7F761129A40063E08AE8A15FD0E9A336FCA18756004FBA4B68B1EC110F",
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
    wanted = EXPECTED_UPLOADS[NEW_ORDER[-1]]
    if (len(data), sha256_bytes(data)) != wanted:
        raise RuntimeError("D001 ZIP outer identity changed")
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        infos = [row for row in archive.infolist() if not row.is_dir()]
        names = [row.filename for row in infos]
        if (
            archive.testzip() is not None
            or len(infos) != 29
            or len(names) != len(set(names))
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError("D001 ZIP member boundary changed")
        manifest_name = (
            "Deligne_D001_Bilingual_SourceAligned_20260801/SHA256SUMS.csv"
        )
        rows = list(
            csv.DictReader(
                io.StringIO(archive.read(manifest_name).decode("utf-8-sig"))
            )
        )
        if len(rows) != 27:
            raise RuntimeError("D001 inner manifest row boundary changed")
        prefix = "Deligne_D001_Bilingual_SourceAligned_20260801/"
        identities = {}
        for row in rows:
            name = prefix + row["relative_path"]
            payload = archive.read(name)
            observed = (len(payload), sha256_bytes(payload))
            expected = (int(row["bytes"]), row["sha256"].upper())
            if observed != expected:
                raise RuntimeError(f"D001 ZIP member changed: {name}")
            identities[row["relative_path"]] = {
                "bytes": observed[0],
                "sha256": observed[1],
            }
        crops = [
            name
            for name in identities
            if name.startswith("visual_evidence/decisive_scan_crops/")
        ]
        if len(crops) != 14:
            raise RuntimeError("D001 decisive source-crop boundary changed")
        return {
            "status": "PASS",
            "members": len(infos),
            "uncompressed_bytes": sum(row.file_size for row in infos),
            "manifest_rows": len(rows),
            "decisive_source_crops": len(crops),
            "member_identities": identities,
        }


def local_uploads() -> dict[str, dict[str, object]]:
    rows = list(
        csv.DictReader(
            UPLOAD_MANIFEST.open("r", encoding="utf-8-sig", newline="")
        )
    )
    if len(rows) != 4 or {row["filename"] for row in rows} != set(NEW_ORDER):
        raise RuntimeError("D001 upload manifest boundary changed")
    uploads = {}
    for name in NEW_ORDER:
        path = PUBLIC_ROOT / name
        observed = (path.stat().st_size, base.sha256_path(path))
        if observed != EXPECTED_UPLOADS[name]:
            raise RuntimeError(f"Local D001 upload changed: {name}")
        uploads[name] = {
            "path": path,
            "bytes": observed[0],
            "sha256": observed[1],
            "md5": base.md5_path(path),
        }
    replay_zip(Path(uploads[NEW_ORDER[-1]]["path"]).read_bytes())
    return uploads


def github_readback(uploads: dict[str, dict[str, object]]) -> dict[str, object]:
    session = base.make_session()
    readback = {}
    for name, local in uploads.items():
        url = (
            "https://raw.githubusercontent.com/KokunoYumeto/"
            f"modern-latex-manuscripts/{GITHUB_COMMIT}/"
            f"{PACKAGE_REL.as_posix()}/public_files/{quote(name, safe='')}"
        )
        data = base.check(session.get(url, timeout=(30, 600)), {200}).content
        observed = (len(data), sha256_bytes(data))
        expected = (int(local["bytes"]), str(local["sha256"]))
        if observed != expected:
            raise RuntimeError(f"GitHub D001 mismatch: {name}")
        readback[name] = {"bytes": observed[0], "sha256": observed[1]}
    return {
        "status": "PASS_GITHUB_PUBLIC_READBACK",
        "commit": GITHUB_COMMIT,
        "package_path": PACKAGE_REL.as_posix(),
        "files": readback,
        "zip_replay": replay_zip(
            Path(uploads[NEW_ORDER[-1]]["path"]).read_bytes()
        ),
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
        sum(int(row["size"]) for row in entries.values()),
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
    if observed != expected or set(entries) != set(PREDECESSOR_ORDER):
        raise RuntimeError(f"Live Deligne predecessor changed: {observed!r}")
    if set(entries) & set(NEW_ORDER):
        raise RuntimeError("D001 uploads already exist on live Deligne head")
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
        raise RuntimeError("Untracked Deligne successor draft exists")
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
        raise RuntimeError("Deligne predecessor is not a versioning base")
    created = base.check(
        session.post(
            deposition["links"]["newversion"], headers=auth, timeout=(30, 300)
        ),
        {201},
    ).json()
    draft = base.check(
        session.get(
            created["links"]["latest_draft"], headers=auth, timeout=(30, 180)
        ),
        {200},
    ).json()
    old_entries = base.modern_entries(predecessor)
    new_entries = base.legacy_entries(draft)
    if set(new_entries) != set(old_entries):
        raise RuntimeError("New Deligne draft did not inherit the predecessor set")
    for name, old in old_entries.items():
        new = new_entries[name]
        if (int(new["filesize"]), base.normalized_md5(new["checksum"])) != (
            int(old["size"]),
            base.normalized_md5(old["checksum"]),
        ):
            raise RuntimeError(f"Inherited Deligne file changed: {name}")
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
    uploads: dict[str, dict[str, object]],
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
    expected = inherited | set(NEW_ORDER)
    if not inherited.issubset(files) or not set(files).issubset(expected):
        raise RuntimeError("Tracked Deligne draft has an unexpected file set")
    bucket = deposition["links"]["bucket"].rstrip("/")
    for name, local in uploads.items():
        existing = files.get(name)
        wanted = (int(local["bytes"]), str(local["md5"]))
        if existing is not None:
            observed = (
                int(existing["filesize"]),
                base.normalized_md5(existing["checksum"]),
            )
            if observed != wanted:
                raise RuntimeError(f"Staged Deligne file changed: {name}")
            continue
        with Path(local["path"]).open("rb") as handle:
            base.check(
                session.put(
                    f"{bucket}/{quote(name, safe='')}",
                    headers={**auth, "Content-Type": "application/octet-stream"},
                    data=handle,
                    timeout=(30, 900),
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
    if set(base.modern_entries(draft)) != expected or len(expected) != FINAL_FILES:
        raise RuntimeError("Staged Deligne file set is not exact")
    metadata = draft["metadata"]
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = VERSION
    paragraph = (
        "<p><strong>D001 source-aligned checkpoint:</strong> direct bilingual, "
        "English, and corrected-French readers are accompanied by one compact "
        "editable-source and decisive-source-evidence ZIP. The ZIP contains 14 "
        "tightly bounded 2400-9600 dpi crops used to adjudicate four disclosed "
        "source repairs; it excludes redundant output-reader renders. This is a "
        "complete working edition of D001 only, not a whole-corpus completion, "
        "critical edition, peer review, certification, or new license grant.</p>"
    )
    if paragraph not in metadata.get("description", ""):
        metadata["description"] = metadata.get("description", "") + paragraph
    payload = {
        "access": draft["access"],
        "files": {
            "enabled": True,
            "default_preview": DEFAULT_PREVIEW,
            "order": FINAL_ORDER,
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
        raise RuntimeError("Patched Deligne draft changed")
    published = base.check(
        session.post(
            patched["links"]["publish"], headers=vendor, timeout=(30, 300)
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
    uploads: dict[str, dict[str, object]],
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
        raise RuntimeError("Published Deligne successor is not readable")
    entries = base.modern_entries(record)
    observed_boundary = (
        len(entries),
        sum(int(row["size"]) for row in entries.values()),
        record["parent"]["pids"]["doi"]["identifier"],
        record["metadata"].get("version"),
        record["files"].get("default_preview"),
    )
    expected_boundary = (
        FINAL_FILES,
        FINAL_BYTES,
        CONCEPT_DOI,
        VERSION,
        DEFAULT_PREVIEW,
    )
    if observed_boundary != expected_boundary:
        raise RuntimeError(f"Published Deligne boundary changed: {observed_boundary!r}")
    api_order = record["files"].get("order") or []
    if api_order not in ([], FINAL_ORDER):
        raise RuntimeError(f"Published Deligne order changed: {api_order!r}")
    effective_order = sorted(entries, key=str.casefold)
    if effective_order != FINAL_ORDER:
        raise RuntimeError(f"Published Deligne filename order changed: {effective_order!r}")
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
        raise RuntimeError(f"Retained Deligne files changed: {retained_errors}")
    new_readback = {}
    zip_replay = None
    for name, local in uploads.items():
        data = base.check(
            session.get(entries[name]["links"]["content"], timeout=(30, 900)),
            {200},
        ).content
        observed = (len(data), sha256_bytes(data))
        expected = (int(local["bytes"]), str(local["sha256"]))
        if observed != expected:
            raise RuntimeError(f"Public Deligne file mismatch: {name}")
        new_readback[name] = {"bytes": observed[0], "sha256": observed[1]}
        if name == NEW_ORDER[-1]:
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
        raise RuntimeError("Published Deligne successor is not live head")
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
        "outer_bytes": sum(int(row["size"]) for row in entries.values()),
        "file_order": api_order,
        "effective_filename_order": effective_order,
        "file_order_basis": (
            "Zenodo returned an empty explicit order; zero-padded filenames "
            "produce the verified effective order"
        ),
        "default_preview": record["files"].get("default_preview"),
        "retained_predecessor_files": len(predecessor_entries),
        "retained_predecessor_identity_method": "Zenodo size and MD5 equality",
        "retained_predecessor_identity_errors": retained_errors,
        "new_file_readback": new_readback,
        "artifact_zip_readback": zip_replay,
        "github_readback": github,
        "live_head_verified": True,
        "active_draft_remaining": False,
        "duplicate_concept_created": False,
        "errors": [],
    }
    RECEIPT_ROOT.mkdir(parents=True, exist_ok=True)
    receipt = RECEIPT_ROOT / (
        f"20260801_deligne_d001_record_{record_id}_public_readback.json"
    )
    base.save_json(receipt, result)
    result["receipt_path"] = str(receipt)
    return result


def preflight() -> dict[str, object]:
    uploads = local_uploads()
    github = github_readback(uploads)
    session = base.make_session()
    predecessor = live_predecessor(session)
    result = {
        "status": "PASS_READY_FOR_SINGLE_SAME_CONCEPT_SUCCESSOR",
        "predecessor_record": int(predecessor["id"]),
        "predecessor_files": len(base.modern_entries(predecessor)),
        "predecessor_bytes": sum(
            int(row["size"]) for row in base.modern_entries(predecessor).values()
        ),
        "new_files": {
            name: {"bytes": row["bytes"], "sha256": row["sha256"]}
            for name, row in uploads.items()
        },
        "github_readback": github,
        "zip_replay": replay_zip(Path(uploads[NEW_ORDER[-1]]["path"]).read_bytes()),
        "final_files": FINAL_FILES,
        "final_bytes": FINAL_BYTES,
        "default_preview": DEFAULT_PREVIEW,
        "errors": [],
    }
    TEMP_ROOT.mkdir(parents=True, exist_ok=True)
    base.save_json(PREPARE_PATH, result)
    return result


def publish() -> dict[str, object]:
    uploads = local_uploads()
    github = github_readback(uploads)
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
                session,
                token,
                predecessor,
                int(state["record_id"]),
                uploads,
                github,
            )
    predecessor = live_predecessor(session)
    draft_id = create_or_resume_draft(session, token, predecessor)
    record_id = stage_and_publish(
        session, token, predecessor, draft_id, uploads
    )
    return public_readback(
        session, token, predecessor, record_id, uploads, github
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--preflight", action="store_true")
    args = parser.parse_args()
    result = preflight() if args.preflight else publish()
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
