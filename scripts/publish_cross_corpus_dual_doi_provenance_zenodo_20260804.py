#!/usr/bin/env python3
"""Publish FAC/Korean/Spanish-SGA provenance on two existing DOI concepts."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import time
import zipfile
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import publish_current_reader_bundles_zenodo_20260730 as base
import build_cross_corpus_dual_doi_provenance_20260804 as builder


API = base.API
MODERN = {"Accept": "application/vnd.inveniordm.v1+json"}
REPO_ROOT = Path(__file__).resolve().parents[1]
ROOT = (
    REPO_ROOT
    / "sources/provenance/fac-korean-sga5-dual-doi-provenance-20260804-r4"
)
STATE_PATH = (
    Path(os.environ.get("LOCALAPPDATA", os.environ.get("TEMP", ".")))
    / "Temp"
    / "cross_corpus_dual_doi_provenance_20260804"
    / "state.json"
)
RECEIPT_ROOT = REPO_ROOT / "manifests/published-zenodo"
PUBLICATION_DATE = "2026-08-04"
BUNDLE_NAME = "09_ARCHIVE_PROVENANCE__00_FAC_KOREAN_SGA5_COMPLETE_20260804.zip"
BUNDLE_IDENTITY = (
    5_580_107,
    "FBC3DE900E13F7699ADDAABC7318643C465A8F928CA53C167199E763D4DFC55D",
    478,
)
VALIDATION_IDENTITY = (
    7_097,
    "4CA446D0B2063D12EFEE0B1B311F435678D5B6D5D41440396B9C4E8B9ADF0426",
)

CARRYFORWARD_REMOVALS = {
    "01_ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_TRANSFORMATIONS_v3.csv",
    "03_ENGLISH_GERMANIC_DECISION_LOG_PRIVACY_README_v3.md",
    "07z_Retained_Machine_Companion_Metadata_20260804.zip",
    "08_EGA_P138__08a_EGA1_CHAPTER1_P138_VALIDATION_R61.json",
    "08_EGA_P138__08b_EGA_ENGLISH_SOURCE_DIFF_VALIDATION_R82.json",
    "08_EGA_P138__09a_FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P138_20260804.jsonl",
    "08_EGA_P138__09b_ENGLISH_CORRECTION_RECHECK_APPEND_P138_20260804.jsonl",
    "08_EGA_P138__09c_WORKFLOW_ERROR_APPEND_P138_20260804.jsonl",
    "08_EGA_P138__11_PRIVACY_TRANSFORMATIONS.csv",
    "08_EGA_P138__12_PRIVACY_VALIDATION.json",
    "08_EGA_P138__13_PACKAGE_PAYLOAD_MANIFEST.csv",
    "08_EGA_P138__15_PACKAGE_VALIDATION.json",
}

SURFACE_ORDER = [
    BUNDLE_NAME,
    "09_FAC_R4__01_PROJECT_LOGBOOK.md",
    "09_FAC_R4__02_EDITORIAL_DECISION_LOGBOOK.md",
    "09_FAC_R4__03_SELF_CORRECTION_LEDGER.csv",
    "09_KO__01_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN.md",
    "09_KO__02_CJK_PRODUCTION_METHODOLOGY_PRIVACY_CLEAN.md",
    "09_SGA5_ES__01_PUBLIC_RELEASE_AUTHORIZATION_AND_HOLD_SUPERSESSION.md",
    "09_SGA5_ES__02_PUBLIC_SOURCE_AND_RIGHTS.md",
    "09_SGA5_ES__03_CONTINUATION_CURSOR.md",
    "09_SGA5_ES__04_SUPERSESSION.md",
    "09_ARCHIVE_PROVENANCE__98_DIRECT_SURFACE_MANIFEST.csv",
    "09_ARCHIVE_PROVENANCE__99_PACKAGE_VALIDATION.json",
]


@dataclass(frozen=True)
class Target:
    key: str
    predecessor_id: int
    predecessor_doi: str
    concept_id: str
    concept_doi: str
    version_index: int
    files: int
    bytes: int
    preview: str
    title: str
    result_files: int
    result_bytes: int
    version: str


TARGETS = {
    "methodology": Target(
        key="methodology",
        predecessor_id=21783420,
        predecessor_doi="10.5281/zenodo.21783420",
        concept_id="21124403",
        concept_doi="10.5281/zenodo.21124403",
        version_index=30,
        files=100,
        bytes=5_002_522_379,
        preview="00_Interlanguage_Methodology_Current_v13_20260718.pdf",
        title="Interlanguage and Mathematical Translation Methodology Sidecar",
        result_files=100,
        result_bytes=5_008_546_352,
        version="2026-08-04 FAC R4, Korean Noether, and Spanish SGA5 provenance",
    ),
    "replication": Target(
        key="replication",
        predecessor_id=21783421,
        predecessor_doi="10.5281/zenodo.21783421",
        concept_id="20461174",
        concept_doi="10.5281/zenodo.20461174",
        version_index=37,
        files=86,
        bytes=24_573_732,
        preview="00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.pdf",
        title="AI-Run Modern LaTeX Manuscript Workflow and Replication Packet",
        result_files=98,
        result_bytes=31_553_930,
        version="2026-08-04 FAC R4, Korean Noether, and Spanish SGA5 replication provenance",
    ),
}


COMMON_DESCRIPTION = """<p><strong>Current corpus map:</strong> EGA is on <a href="https://doi.org/10.5281/zenodo.20414353">concept 10.5281/zenodo.20414353</a> (current version <a href="https://doi.org/10.5281/zenodo.21783419">21783419</a>); SGA is on <a href="https://doi.org/10.5281/zenodo.20410947">concept 10.5281/zenodo.20410947</a> (current version <a href="https://doi.org/10.5281/zenodo.21783548">21783548</a>); FAC is on <a href="https://doi.org/10.5281/zenodo.21720996">concept 10.5281/zenodo.21720996</a> (current version <a href="https://doi.org/10.5281/zenodo.21783868">21783868</a>); GAGA remains separate on <a href="https://doi.org/10.5281/zenodo.21781322">concept 10.5281/zenodo.21781322</a>; and the Noether multilingual corpus is on <a href="https://doi.org/10.5281/zenodo.20412587">concept 10.5281/zenodo.20412587</a> (current version <a href="https://doi.org/10.5281/zenodo.21785492">21785492</a>).</p>
<p><strong>FAC trust evidence:</strong> the FAC project logbook, editorial decision logbook, and 219-entry self-correction/reversal ledger are direct files here. The project coordinator did not know the Achinger-Krupa English translation existed when Codex translated and froze FAC nos. 1-79 from the French working transcription; the comparator was discovered afterward, and all 79 blind-scope units were adjudicated against Serre's French authority. Nos. 80-81 are outside the blind claim. The result is qualitative evidence, not a scalar score, ranking, certification, peer review, or general superiority claim.</p>
<p><strong>Korean Noether audit surface:</strong> the current CJK decision/error log and production-methodology retrospective are direct. The complete provenance bundle preserves the full privacy-clean public projections for Papers 1, 3, 4, 5, 7, 41, and 42, including source custody, checker handoffs, translation choices, structural/difficulty/error histories, rejected attempts, and continuation. Paper 4 has all fifty producer-draft TeX units for sections 1-9; its structural evidence is scoped to T01-T03 only. All Korean states remain UNCHECKED, uncompiled, unrendered, unassembled, unreviewed, and uncertified; publication is preservation, not approval.</p>
<p><strong>Spanish SGA 5:</strong> the Spanish checkpoint is preserved on the existing SGA concept, with authorization/hold-supersession, source-and-rights, continuation, and supersession records direct here. Its mathematical work is public; state and rights caveats are metadata rather than release holds.</p>
<p><strong>Complete provenance bundle:</strong> <code>09_ARCHIVE_PROVENANCE__00_FAC_KOREAN_SGA5_COMPLETE_20260804.zip</code> contains 478 outer members plus 17 recursively checked nested ZIPs / 622 nested members. Private user-root path hits are zero. Public attribution names are retained. Exact transformations, validations, manifests, old error/reversal histories, and twelve methodology-ceiling carry-forward files are bound inside; no distinct content is curated away.</p>
<p><strong>Limits:</strong> these working corpora and audit surfaces do not claim critical-edition status, native-language certification, mathematical peer review, proof checking, universal rights clearance, or whole-program completion.</p>"""

DESCRIPTIONS = {
    "methodology": """<h2>Interlanguage and mathematical translation methodology sidecar</h2>
<p><strong>Open first:</strong> <code>00_Interlanguage_Methodology_Current_v13_20260718.pdf</code> is the default overview. This concept is the public methodology, provenance, decision-rationale, correction/reversal, corpus-control, and continuation shelf for the archive; mathematical readers remain on their dedicated concepts.</p>
""" + COMMON_DESCRIPTION,
    "replication": """<h2>AI-run manuscript workflow and replication packet</h2>
<p><strong>Open first:</strong> <code>00_AI_Run_Modern_LaTeX_Manuscript_Workflow_Current_20260728.pdf</code> is the default workflow overview. This concept preserves reproducible source-control, validation, decision/error history, and public-safe replication surfaces used across the archive.</p>
""" + COMMON_DESCRIPTION,
}

ADDITIONAL_NOTE = """<p><strong>2026-08-04 cross-corpus provenance successor.</strong> Twelve direct files are identical across methodology and replication: one 478-member complete bundle, three FAC trust logs, two Korean decision/methodology logs, four Spanish SGA5 provenance surfaces, a direct manifest, and validation. Recursive bundle privacy replay covers 17 nested ZIPs / 622 members with private-path hits0. The methodology record remains at the 100-file ceiling by moving twelve exact machine/carry-forward files into the manifested bundle; predecessor21783420 retains them direct.</p>"""


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def md5(path: Path) -> str:
    digest = hashlib.md5(usedforsecurity=False)
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().lower()


def normalized_md5(value: str) -> str:
    return str(value).lower().removeprefix("md5:")


def modern_entries(record: dict) -> dict[str, dict]:
    entries = record.get("files", {}).get("entries", [])
    return entries if isinstance(entries, dict) else {row["key"]: row for row in entries}


def legacy_entries(record: dict) -> dict[str, dict]:
    return {row["filename"]: row for row in record.get("files", [])}


def identity(row: dict) -> tuple[int, str]:
    return int(row["size"]), normalized_md5(row["checksum"])


def legacy_identity(row: dict) -> tuple[int, str]:
    return int(row["filesize"]), normalized_md5(row["checksum"])


def auth(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}


def auth_modern(token: str) -> dict[str, str]:
    return {**auth(token), **MODERN}


def save_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def load_state() -> dict:
    if not STATE_PATH.is_file():
        return {"schema": "cross-corpus-dual-doi-state-v1", "targets": {}}
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def target_state(state: dict, key: str) -> dict:
    return state.setdefault("targets", {}).setdefault(key, {})


def local_surface() -> tuple[dict[str, dict], dict]:
    validation_path = ROOT / "09_ARCHIVE_PROVENANCE__99_PACKAGE_VALIDATION.json"
    if (validation_path.stat().st_size, sha256(validation_path)) != VALIDATION_IDENTITY:
        raise RuntimeError("Cross-corpus provenance validation identity changed")
    validation = json.loads(validation_path.read_text(encoding="utf-8"))
    if (
        validation.get("status") != "PASS_READY_FOR_DUAL_DOI_PUBLICATION"
        or validation.get("errors") != []
        or validation.get("schema") != "cross_corpus_dual_doi_provenance_package_v5"
        or validation.get("bundle_recursive_privacy_validation", {}).get("status") != "PASS"
        or int(validation.get("bundle_recursive_privacy_validation", {}).get("private_path_hits", -1)) != 0
        or validation.get("noether_record") != "10.5281/zenodo.21785492"
    ):
        raise RuntimeError("Cross-corpus provenance validation boundary changed")
    bundle = ROOT / BUNDLE_NAME
    if (bundle.stat().st_size, sha256(bundle)) != BUNDLE_IDENTITY[:2]:
        raise RuntimeError("Cross-corpus provenance bundle identity changed")
    with zipfile.ZipFile(bundle) as package:
        members = [row for row in package.infolist() if not row.is_dir()]
        if len(members) != BUNDLE_IDENTITY[2] or package.testzip() is not None:
            raise RuntimeError("Cross-corpus provenance bundle replay changed")
    if set(SURFACE_ORDER) != {path.name for path in ROOT.iterdir() if path.is_file()}:
        raise RuntimeError("Cross-corpus direct surface filename closure changed")
    surface = {
        name: {
            "path": str(ROOT / name),
            "bytes": (ROOT / name).stat().st_size,
            "sha256": sha256(ROOT / name),
            "md5": md5(ROOT / name),
        }
        for name in SURFACE_ORDER
    }
    if len(surface) != 12 or sum(int(row["bytes"]) for row in surface.values()) != 6_980_198:
        raise RuntimeError("Cross-corpus direct surface count/bytes changed")
    return surface, validation


def fetch_predecessor(session, target: Target, require_latest: bool = True) -> dict:
    record = base.check(
        session.get(f"{API}/records/{target.predecessor_id}", headers=MODERN, timeout=(30, 300)),
        {200},
    ).json()
    entries = modern_entries(record)
    observed = (
        int(record["id"]),
        record["pids"]["doi"]["identifier"],
        str(record.get("parent", {}).get("id")),
        record.get("parent", {}).get("pids", {}).get("doi", {}).get("identifier"),
        int(record.get("versions", {}).get("index", 0)),
        record.get("status"),
        len(entries),
        sum(int(row["size"]) for row in entries.values()),
        record.get("files", {}).get("default_preview"),
        record.get("metadata", {}).get("title"),
    )
    expected = (
        target.predecessor_id,
        target.predecessor_doi,
        target.concept_id,
        target.concept_doi,
        target.version_index,
        "published",
        target.files,
        target.bytes,
        target.preview,
        target.title,
    )
    if observed != expected:
        raise RuntimeError(f"{target.key} predecessor boundary changed: {observed!r}")
    if require_latest:
        latest = base.check(session.get(record["links"]["latest"], headers=MODERN, timeout=(30, 300)), {200}).json()
        if int(latest["id"]) != target.predecessor_id:
            raise RuntimeError(f"{target.key} live head changed")
    return record


def compaction_proof(session, methodology: dict, validation: dict) -> list[dict]:
    rows = {row["filename"]: row for row in validation["methodology_carryforward"]}
    if set(rows) != CARRYFORWARD_REMOVALS:
        raise RuntimeError("Methodology carry-forward validation boundary changed")
    entries = modern_entries(methodology)
    bundle = ROOT / BUNDLE_NAME
    proofs = []
    anonymous = base.make_session()
    with zipfile.ZipFile(bundle) as package:
        for name in sorted(CARRYFORWARD_REMOVALS, key=str.casefold):
            member = f"METHODOLOGY_CARRYFORWARD/{name}"
            data = package.read(member)
            expected = rows[name]
            remote = base.check(anonymous.get(entries[name]["links"]["content"], timeout=(30, 300)), {200}).content
            observed_sha = hashlib.sha256(remote).hexdigest().upper()
            if (
                len(data) != int(expected["bytes"])
                or hashlib.sha256(data).hexdigest().upper() != expected["sha256"]
                or len(remote) != int(expected["bytes"])
                or observed_sha != expected["sha256"]
            ):
                raise RuntimeError(f"Methodology carry-forward proof changed: {name}")
            proofs.append(
                {
                    "removed_direct_filename": name,
                    "bytes": len(data),
                    "sha256": observed_sha,
                    "retained_bundle": BUNDLE_NAME,
                    "retained_member": member,
                    "immutable_predecessor": TARGETS["methodology"].predecessor_doi,
                }
            )
    return proofs


def check_draft(session, token: str, target: Target, state: dict) -> None:
    tracked = target_state(state, target.key)
    probe = session.get(f"{API}/records/{target.predecessor_id}/draft", headers=auth_modern(token), timeout=(30, 180))
    if tracked.get("published_record"):
        if probe.status_code not in {404, 410}:
            raise RuntimeError(f"{target.key} published state conflicts with active draft")
        return
    if not tracked.get("draft_id"):
        if probe.status_code == 200:
            raise RuntimeError(f"Untracked {target.key} draft exists: {probe.json().get('id')}")
        base.check(probe, {404, 410})
        return
    draft_id = int(tracked["draft_id"])
    draft = base.check(session.get(f"{API}/records/{draft_id}/draft", headers=auth_modern(token), timeout=(30, 180)), {200}).json()
    if int(draft["id"]) != draft_id or str(draft.get("parent", {}).get("id")) != target.concept_id:
        raise RuntimeError(f"Tracked {target.key} draft boundary changed")


def create_or_resume(session, token: str, target: Target, predecessor: dict, state: dict) -> tuple[int, bool]:
    tracked = target_state(state, target.key)
    if tracked.get("draft_id"):
        return int(tracked["draft_id"]), False
    deposition = base.check(session.get(f"{API}/deposit/depositions/{target.predecessor_id}", headers=auth(token), timeout=(30, 300)), {200}).json()
    if deposition.get("state") != "done" or not deposition.get("submitted") or str(deposition.get("conceptrecid")) != target.concept_id:
        raise RuntimeError(f"{target.key} is not a safe same-concept versioning base")
    created = base.check(session.post(deposition["links"]["newversion"], headers=auth(token), timeout=(30, 600)), {201}).json()
    draft_dep = base.check(session.get(created["links"]["latest_draft"], headers=auth(token), timeout=(30, 300)), {200}).json()
    draft_id = int(draft_dep["id"])
    if set(legacy_entries(draft_dep)) != set(modern_entries(predecessor)):
        raise RuntimeError(f"{target.key} successor inheritance changed")
    tracked.update({"status": "OPEN_TRACKED_DRAFT", "draft_id": draft_id, "predecessor_id": target.predecessor_id, "concept_id": target.concept_id})
    save_json(STATE_PATH, state)
    return draft_id, True


def desired_order(predecessor: dict, target: Target) -> list[str]:
    entries = modern_entries(predecessor)
    removals = CARRYFORWARD_REMOVALS if target.key == "methodology" else set()
    remaining = [name for name in entries if name != target.preview and name not in removals]
    order = [target.preview, *SURFACE_ORDER, *sorted(remaining, key=str.casefold)]
    if len(order) != target.result_files or len(order) != len(set(order)):
        raise RuntimeError(f"{target.key} resulting order changed: {len(order)}")
    return order


def desired_metadata(predecessor: dict, target: Target) -> dict:
    metadata = copy.deepcopy(predecessor["metadata"])
    metadata["title"] = target.title
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["version"] = target.version
    metadata["description"] = DESCRIPTIONS[target.key]
    metadata["additional_descriptions"] = [{"description": ADDITIONAL_NOTE, "type": {"id": "notes"}}]
    return metadata


def verify_staged(draft: dict, predecessor: dict, target: Target, surface: dict, order: list[str]) -> None:
    entries = modern_entries(draft)
    inherited = modern_entries(predecessor)
    removals = CARRYFORWARD_REMOVALS if target.key == "methodology" else set()
    expected = (set(inherited) - removals) | set(surface)
    if set(entries) != expected or len(entries) != target.result_files:
        raise RuntimeError(f"{target.key} staged filename closure changed")
    errors = []
    for name in expected - set(surface):
        if identity(entries[name]) != identity(inherited[name]):
            errors.append(name)
    for name, row in surface.items():
        if identity(entries[name]) != (int(row["bytes"]), str(row["md5"])):
            errors.append(name)
    if errors:
        raise RuntimeError(f"{target.key} staged identity errors: {errors}")
    metadata = draft["metadata"]
    additional = metadata.get("additional_descriptions") or []
    additional_exact = (
        len(additional) == 1
        and additional[0].get("description") == ADDITIONAL_NOTE
        and (additional[0].get("type") or {}).get("id") == "notes"
    )
    if (
        metadata.get("title") != target.title
        or metadata.get("publication_date") != PUBLICATION_DATE
        or metadata.get("version") != target.version
        or metadata.get("description") != DESCRIPTIONS[target.key]
        # Zenodo expands the controlled-vocabulary type with localized titles.
        # Verify the submitted semantic identity while accepting that response-only
        # enrichment instead of mistaking it for a metadata mutation.
        or not additional_exact
        or draft.get("files", {}).get("default_preview") != target.preview
    ):
        raise RuntimeError(f"{target.key} staged metadata/default preview changed")
    observed_order = draft.get("files", {}).get("order") or []
    if observed_order not in (order, []):
        raise RuntimeError(f"{target.key} staged order changed")


def upload_file(session, token: str, bucket: str, name: str, path: Path) -> None:
    print(f"UPLOAD {name} ({path.stat().st_size} bytes)", flush=True)
    with path.open("rb") as handle:
        base.check(
            session.put(
                f"{bucket.rstrip('/')}/{quote(name, safe='')}",
                headers={**auth(token), "Content-Type": "application/octet-stream"},
                data=handle,
                timeout=(30, 3600),
            ),
            {200, 201},
        )


def stage_one(session, token: str, target: Target, predecessor: dict, surface: dict, state: dict) -> dict:
    draft_id, created = create_or_resume(session, token, target, predecessor, state)
    deposition = base.check(session.get(f"{API}/deposit/depositions/{draft_id}", headers=auth(token), timeout=(30, 300)), {200}).json()
    remote = legacy_entries(deposition)
    removals = CARRYFORWARD_REMOVALS if target.key == "methodology" else set()
    deleted = []
    for name in sorted(removals & set(remote), key=str.casefold):
        base.check(session.delete(remote[name]["links"]["self"], headers=auth(token), timeout=(30, 300)), {204})
        deleted.append(name)
    deposition = base.check(session.get(f"{API}/deposit/depositions/{draft_id}", headers=auth(token), timeout=(30, 300)), {200}).json()
    remote = legacy_entries(deposition)
    uploaded = []
    for name in SURFACE_ORDER:
        row = surface[name]
        if name in remote:
            if legacy_identity(remote[name]) != (int(row["bytes"]), str(row["md5"])):
                raise RuntimeError(f"{target.key} tracked upload changed: {name}")
            continue
        upload_file(session, token, deposition["links"]["bucket"], name, Path(row["path"]))
        uploaded.append(name)
    draft = base.check(session.get(f"{API}/records/{draft_id}/draft", headers=auth_modern(token), timeout=(30, 600)), {200}).json()
    order = desired_order(predecessor, target)
    payload = {
        "access": predecessor["access"],
        "files": {"enabled": True, "default_preview": target.preview, "order": order},
        "metadata": desired_metadata(predecessor, target),
        "custom_fields": predecessor.get("custom_fields", {}),
    }
    if draft.get("pids"):
        payload["pids"] = draft["pids"]
    patched = base.check(
        session.put(f"{API}/records/{draft_id}/draft", headers={**auth_modern(token), "Content-Type": "application/json"}, json=payload, timeout=(30, 600)),
        {200},
    ).json()
    verify_staged(patched, predecessor, target, surface, order)
    if len(modern_entries(patched)) != target.result_files or sum(int(row["size"]) for row in modern_entries(patched).values()) != target.result_bytes:
        raise RuntimeError(f"{target.key} staged count/bytes changed")
    tracked = target_state(state, target.key)
    tracked.update({"status": "STAGED_EXACT_READY_FOR_EXPLICIT_PUBLISH", "staged": True, "files": target.result_files, "bytes": target.result_bytes})
    save_json(STATE_PATH, state)
    return {"target": target.key, "draft_id": draft_id, "draft_url": patched.get("links", {}).get("self_html"), "created": created, "deleted": deleted, "uploaded": uploaded, "files": target.result_files, "bytes": target.result_bytes, "preview": target.preview}


def preflight(session, token: str) -> dict:
    surface, validation = local_surface()
    state = load_state()
    records = {key: fetch_predecessor(session, target) for key, target in TARGETS.items()}
    for target in TARGETS.values():
        check_draft(session, token, target, state)
    proof = compaction_proof(session, records["methodology"], validation)
    return {
        "status": "PASS_READY_FOR_TWO_EXISTING_CONCEPT_SUCCESSORS",
        "surface_files": len(surface),
        "surface_bytes": sum(int(row["bytes"]) for row in surface.values()),
        "bundle": {"filename": BUNDLE_NAME, "bytes": BUNDLE_IDENTITY[0], "sha256": BUNDLE_IDENTITY[1], "members": BUNDLE_IDENTITY[2]},
        "methodology_compaction_files": len(proof),
        "methodology_compaction_bytes": sum(int(row["bytes"]) for row in proof),
        "targets": {
            key: {
                "concept_doi": target.concept_doi,
                "predecessor": target.predecessor_id,
                "predecessor_doi": target.predecessor_doi,
                "active_draft": bool(target_state(state, key).get("draft_id")),
                "result_files": target.result_files,
                "result_bytes": target.result_bytes,
                "default_preview": target.preview,
            }
            for key, target in TARGETS.items()
        },
        "duplicate_concept_created": False,
        "release_hold": False,
    }


def stage(session, token: str) -> dict:
    surface, validation = local_surface()
    state = load_state()
    records = {key: fetch_predecessor(session, target) for key, target in TARGETS.items()}
    for target in TARGETS.values():
        check_draft(session, token, target, state)
    compaction_proof(session, records["methodology"], validation)
    results = [stage_one(session, token, TARGETS[key], records[key], surface, state) for key in ("methodology", "replication")]
    return {"status": "STAGED_BOTH_EXACT_READY_FOR_EXPLICIT_PUBLISH", "targets": results, "duplicate_concept_created": False, "release_hold": False}


def stream_identity(session, url: str, destination: Path | None = None) -> tuple[int, str]:
    digest = hashlib.sha256()
    total = 0
    response = base.check(session.get(url, stream=True, timeout=(30, 3600)), {200})
    try:
        handle = None if destination is None else destination.open("wb")
        try:
            for block in response.iter_content(4 * 1024 * 1024):
                if not block:
                    continue
                if handle is not None:
                    handle.write(block)
                digest.update(block)
                total += len(block)
        finally:
            if handle is not None:
                handle.close()
    finally:
        response.close()
    return total, digest.hexdigest().upper()


def replay_bundle(path: Path) -> dict:
    local = ROOT / BUNDLE_NAME
    expected = {}
    with zipfile.ZipFile(local) as package:
        for info in package.infolist():
            if info.is_dir():
                continue
            data = package.read(info)
            expected[info.filename] = (len(data), hashlib.sha256(data).hexdigest().upper())
    rows = []
    errors = []
    payloads = {}
    with zipfile.ZipFile(path) as package:
        infos = [row for row in package.infolist() if not row.is_dir()]
        if len(infos) != BUNDLE_IDENTITY[2] or package.testzip() is not None or set(info.filename for info in infos) != set(expected):
            errors.append("member_boundary_or_crc")
        for info in infos:
            data = package.read(info)
            observed = (len(data), hashlib.sha256(data).hexdigest().upper())
            match = observed == expected.get(info.filename)
            if not match:
                errors.append(info.filename)
            payloads[info.filename] = data
            rows.append({"member_path": info.filename, "bytes": observed[0], "sha256": observed[1], "match": match})
    privacy = builder.validate_bundle_privacy(payloads)
    if privacy["status"] != "PASS":
        errors.append("recursive_privacy")
    return {"status": "PASS" if not errors else "FAIL", "errors": errors, "members": len(rows), "matches": sum(1 for row in rows if row["match"]), "mismatches": sum(1 for row in rows if not row["match"]), "recursive_privacy": privacy, "member_identities": rows}


def publish_one(session, token: str, target: Target, predecessor: dict, surface: dict, state: dict, confirm: str) -> dict:
    tracked = target_state(state, target.key)
    if tracked.get("published_record"):
        record_id = int(tracked["published_record"])
    else:
        if not tracked.get("staged"):
            raise RuntimeError(f"{target.key} has no exact staged draft")
        draft_id = int(tracked["draft_id"])
        if confirm != str(draft_id):
            raise RuntimeError(f"Publishing {target.key} requires --confirm {draft_id}")
        draft = base.check(session.get(f"{API}/records/{draft_id}/draft", headers=auth_modern(token), timeout=(30, 600)), {200}).json()
        order = desired_order(predecessor, target)
        verify_staged(draft, predecessor, target, surface, order)
        response = base.check(session.post(draft["links"]["publish"], headers=auth_modern(token), timeout=(30, 1200)), {200, 202})
        try:
            record_id = int(response.json().get("id", draft_id))
        except Exception:
            record_id = draft_id
        tracked.update({"status": "PUBLISHED_READBACK_PENDING", "published_record": record_id})
        save_json(STATE_PATH, state)
    anonymous = base.make_session()
    record = None
    for _ in range(60):
        probe = anonymous.get(f"{API}/records/{record_id}", headers=MODERN, timeout=(30, 300))
        if probe.status_code == 200 and probe.json().get("status") == "published":
            record = probe.json()
            break
        time.sleep(2)
    if record is None:
        raise RuntimeError(f"{target.key} successor did not become public")
    order = desired_order(predecessor, target)
    verify_staged(record, predecessor, target, surface, order)
    entries = modern_entries(record)
    if (
        str(record.get("parent", {}).get("id")) != target.concept_id
        or record.get("versions", {}).get("is_latest") is not True
        or int(record.get("versions", {}).get("index", 0)) != target.version_index + 1
        or len(entries) != target.result_files
        or sum(int(row["size"]) for row in entries.values()) != target.result_bytes
    ):
        raise RuntimeError(f"{target.key} published boundary changed")
    download_root = STATE_PATH.parent / "readback"
    download_root.mkdir(parents=True, exist_ok=True)
    bundle_path = download_root / f"{target.key}_{BUNDLE_NAME}"
    readback = []
    errors = []
    for index, name in enumerate(SURFACE_ORDER, start=1):
        print(f"READBACK {target.key} {index}/12 {name}", flush=True)
        destination = bundle_path if name == BUNDLE_NAME else None
        observed = stream_identity(anonymous, entries[name]["links"]["content"], destination)
        expected = (int(surface[name]["bytes"]), str(surface[name]["sha256"]))
        match = observed == expected
        if not match:
            errors.append(name)
        readback.append({"filename": name, "bytes": observed[0], "sha256": observed[1], "match": match, "content_url": entries[name]["links"]["content"]})
    bundle_replay = replay_bundle(bundle_path)
    bundle_path.unlink()
    if bundle_replay["status"] != "PASS":
        errors.append("bundle_member_replay")
    inherited = modern_entries(predecessor)
    removals = CARRYFORWARD_REMOVALS if target.key == "methodology" else set()
    desired_retained = set(inherited) - removals
    retained_errors = [name for name in desired_retained if identity(entries[name]) != identity(inherited[name])]
    errors.extend(retained_errors)
    if errors:
        raise RuntimeError(f"{target.key} publication/readback errors: {errors}")
    draft_probe = session.get(f"{API}/records/{record_id}/draft", headers=auth_modern(token), timeout=(30, 180))
    if draft_probe.status_code not in {404, 410}:
        raise RuntimeError(f"{target.key} active draft remains after publication")
    result = {
        "status": "PASS_PUBLISHED_AND_ANONYMOUS_RAW_READBACK",
        "target": target.key,
        "record_id": record_id,
        "record_url": record["links"]["self_html"],
        "doi": record["pids"]["doi"]["identifier"],
        "concept_id": target.concept_id,
        "concept_doi": target.concept_doi,
        "predecessor_record": target.predecessor_id,
        "predecessor_doi": target.predecessor_doi,
        "version_index": int(record["versions"]["index"]),
        "files": len(entries),
        "bytes": sum(int(row["size"]) for row in entries.values()),
        "default_preview": record["files"]["default_preview"],
        "new_direct_files": len(readback),
        "new_direct_raw_readback_matches": len(readback),
        "new_direct_raw_readback_mismatches": 0,
        "retained_predecessor_files": len(desired_retained),
        "retained_predecessor_identity_mismatches": 0,
        "methodology_compacted_direct_files": sorted(removals),
        "bundle_replay": bundle_replay,
        "raw_public_readback": readback,
        "active_draft": False,
        "duplicate_concept_created": False,
        "release_hold": False,
    }
    tracked.update({"status": "PASS_PUBLISHED_AND_ANONYMOUS_READBACK", "doi": result["doi"], "readback": True})
    save_json(STATE_PATH, state)
    receipt = RECEIPT_ROOT / f"20260804_cross_corpus_{target.key}_record_{record_id}_public_readback.json"
    save_json(receipt, result)
    result["receipt_path"] = str(receipt)
    result["receipt_bytes"] = receipt.stat().st_size
    result["receipt_sha256"] = sha256(receipt)
    return result


def publish(session, token: str, methodology_confirm: str, replication_confirm: str) -> dict:
    surface, validation = local_surface()
    state = load_state()
    records = {
        key: fetch_predecessor(session, target, require_latest=not bool(target_state(state, key).get("published_record")))
        for key, target in TARGETS.items()
    }
    proof = compaction_proof(session, records["methodology"], validation)
    confirms = {"methodology": methodology_confirm, "replication": replication_confirm}
    results = [publish_one(session, token, TARGETS[key], records[key], surface, state, confirms[key]) for key in ("methodology", "replication")]
    identities = [{row["filename"]: (row["bytes"], row["sha256"]) for row in result["raw_public_readback"]} for result in results]
    if identities[0] != identities[1]:
        raise RuntimeError("Methodology and replication direct provenance bytes diverged")
    combined = {
        "status": "PASS_CROSS_CORPUS_DUAL_DOI_PUBLICATION_AND_READBACK",
        "errors": [],
        "surfaces": results,
        "identical_new_direct_files": True,
        "identical_new_direct_file_names": SURFACE_ORDER,
        "methodology_compaction_proof": proof,
        "bundle": {"filename": BUNDLE_NAME, "bytes": BUNDLE_IDENTITY[0], "sha256": BUNDLE_IDENTITY[1], "members": BUNDLE_IDENTITY[2]},
        "fac_record": "10.5281/zenodo.21783868",
        "noether_record": "10.5281/zenodo.21785492",
        "sga_record": "10.5281/zenodo.21783548",
        "gaga_concept": "10.5281/zenodo.21781322",
        "duplicate_concept_created": False,
        "release_hold": False,
    }
    receipt = RECEIPT_ROOT / "20260804_cross_corpus_dual_doi_provenance_publication_receipt.json"
    save_json(receipt, combined)
    combined["receipt_path"] = str(receipt)
    combined["receipt_bytes"] = receipt.stat().st_size
    combined["receipt_sha256"] = sha256(receipt)
    return combined


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("preflight", "stage", "publish"))
    parser.add_argument("--confirm-methodology")
    parser.add_argument("--confirm-replication")
    args = parser.parse_args()
    session = base.make_session()
    token = base.find_token()
    if args.action == "preflight":
        result = preflight(session, token)
    elif args.action == "stage":
        result = stage(session, token)
    else:
        if not args.confirm_methodology or not args.confirm_replication:
            raise RuntimeError("Publishing requires both exact draft ids")
        result = publish(session, token, args.confirm_methodology, args.confirm_replication)
    summary = copy.deepcopy(result)
    for surface in summary.get("surfaces", []):
        surface.pop("raw_public_readback", None)
        surface.pop("bundle_replay", None)
    if "methodology_compaction_proof" in summary:
        summary["methodology_compaction_files"] = len(summary.pop("methodology_compaction_proof"))
    print(json.dumps(summary, ensure_ascii=False, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
