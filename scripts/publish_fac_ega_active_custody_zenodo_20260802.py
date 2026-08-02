#!/usr/bin/env python3
"""Guarded four-concept Zenodo publisher for the 2026-08-02 custody release.

This script is intentionally specification-driven.  Package builders provide a
JSON release specification and exact upload manifests after the archive-owned
privacy projection is frozen.  With no mode flag the script performs a
read-only preflight.  Zenodo is mutated only when ``--publish`` is explicit.

The release specification has this shape (hashes are hexadecimal strings):

{
  "schema": "zenodo-active-custody-release-spec-v1",
  "release_id": "fac-ega-active-custody-20260802-r1",
  "publication_date": "2026-08-02",
  "control": {
    "path": "C:/.../PROJECT_LOGBOOK_..._20260802.md",
    "bytes": 2296,
    "sha256": "BFA1E3...12679"
  },
  "targets": {
    "fac_gaga": {
      "predecessor_guard": {
        "record_id": 21721854,
        "concept_id": 21720996,
        "concept_doi": "10.5281/zenodo.21720996",
        "version_doi": "10.5281/zenodo.21721854",
        "title": "exact existing title",
        "file_count": 1,
        "total_bytes": 123,
        "inventory_sha256": "...",
        "files": [{
           "name": "existing.zip", "bytes": 123, "md5": "...",
           "zenodo_file_id": "exact-inherited-object-uuid"
        }]
      },
      "manifest_path": "path/to/zenodo-upload-manifest.json",
      "manifest_guard": {"bytes": 1234, "sha256": "..."},
      "file_policy": {"mode": "add-only"},
      "metadata_append": {
        "version_suffix": "2026-08-02 bounded custody snapshot r1",
        "description_html": "<p>Exact, bounded scope and caveats.</p>",
        "cross_links": [{
          "identifier": "https://github.com/.../tree/COMMIT/path",
          "scheme": "url", "relation_type": "issupplementedby"
        }]
      }
    },
    "ega": {}, "methodology": {}, "replication": {}
  }
}

Each target manifest is JSON with a top-level ``files`` list, or CSV.  Every
row must contain ``name`` (or ``filename``), ``path`` (or ``source_path``),
``bytes``, ``sha256``, ``md5``, and ``role``.  Paths are resolved relative to
the manifest.  Rows sent identically to the methodology and replication DOI
   records must also set ``dual_doi_provenance=true``, ``privacy_clean=true``, and
   ``control_binding_sha256=BFA1...12679``.  That shared set must contain the
   privacy-clean public projection of the control plus
   ``ARCHIVE_CONTROL_IDENTITIES.json`` binding it to the exact 2,296-byte private
   source identity, at least one loose logbook/decision/revision/continuation
   provenance object, and a public provenance-manifest object.  The raw control
   contains internal task identifiers and must not be uploaded.  ZIP rows may
   additionally pin
``zip_member_count``, ``zip_uncompressed_bytes``, and
``zip_inventory_sha256``; the script calculates and checks these regardless.

The predecessor inventory digest is SHA-256 over canonical JSON for the full
sorted list of normalized Zenodo object rows (name, bytes, native MD5, and
inherited file UUID).  The complete predecessor row list is mandatory.  This
matches the established archive workflow: existing published bytes are retained
by exact Zenodo object identity plus size/MD5, while every newly uploaded object
receives anonymous whole-file SHA-256 readback and every new ZIP receives full
member-level SHA-256 replay.  Already-published multi-gigabyte predecessors are
not needlessly downloaded and decompressed again on every successor.

Safety properties:

* all four concepts and current heads are compiled into this program;
* an authenticated, account-wide deposition scan rejects parallel same-concept
  drafts, while a narrowly tracked creation intent permits crash recovery;
* a successor is created only through an existing head's ``newversion`` link;
* add-only is the default, and every inherited predecessor object is checked;
* all four drafts are staged and revalidated before the first is published;
* methodology and replication publish before corpus successors;
* title, access, rights/license metadata, and predecessor files are retained;
* exact anonymous whole-file and streaming ZIP-member SHA-256 readback closes
  each record, followed by latest-version and no-active-draft checks;
* receipts are written below ``manifests/published-zenodo``.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import os
import re
import tempfile
import time
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any, Iterable
from urllib.parse import quote

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


API = "https://zenodo.org/api"
SCHEMA = "zenodo-active-custody-release-spec-v1"
MANIFEST_SCHEMA = "zenodo-upload-manifest-v1"
PUBLICATION_DATE = "2026-08-02"
CONTROL_BYTES = 2_296
CONTROL_SHA256 = (
    "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679"
)
CONTROL_PUBLIC_BYTES = 2_242
CONTROL_PUBLIC_SHA256 = (
    "864DC6B0183161DFA289D6A25DDE268D09E5187C3C4102C854F05422B86DF2AA"
)
CONTROL_BINDING_MANIFEST_NAME = "ARCHIVE_CONTROL_IDENTITIES.json"
CONTROL_PATH = Path(
    "C:/Users/Floris/Documents/interlanguage/03_projects/language_management/"
    "english_germanic/00_lane_control/"
    "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
)

REPO_ROOT = Path(__file__).resolve().parents[1]
RECEIPT_ROOT = REPO_ROOT / "manifests" / "published-zenodo"
TOKEN_LOG = Path(
    os.environ.get(
        "ZENODO_TOKEN_LOG",
        Path.home() / ".codex" / ".sandbox" / "sandbox.log",
    )
)

# The registry is a hard boundary.  The program has no code path that creates a
# concept and refuses release specifications that omit or alter these targets.
TARGETS: dict[str, dict[str, Any]] = {
    "fac_gaga": {
        "predecessor_record": 21_721_854,
        "concept_id": 21_720_996,
        "concept_doi": "10.5281/zenodo.21720996",
    },
    "ega": {
        "predecessor_record": 21_744_406,
        "concept_id": 20_414_353,
        "concept_doi": "10.5281/zenodo.20414353",
    },
    "methodology": {
        "predecessor_record": 21_744_853,
        "concept_id": 21_124_403,
        "concept_doi": "10.5281/zenodo.21124403",
    },
    "replication": {
        "predecessor_record": 21_707_334,
        "concept_id": 20_461_174,
        "concept_doi": "10.5281/zenodo.20461174",
    },
}

# All drafts are staged before publication.  Public provenance is then closed
# on both DOI surfaces before the corpus records that rely on it.
SAFE_PUBLISH_ORDER = ("methodology", "replication", "fac_gaga", "ega")
OPEN_STATUSES = {"CREATE_INTENT", "DRAFT_CREATED", "STAGED"}
PUBLISHED_STATUSES = {"PUBLISHED_PENDING_READBACK", "CLOSED"}
PROVENANCE_ROLE_WORDS = (
    "logbook",
    "decision",
    "revision",
    "reversal",
    "continuation",
    "provenance",
)
NON_CERTIFYING_NOTICE = (
    "<p><strong>Archive scope:</strong> This is a bounded preservation "
    "snapshot. It does not certify production completion, mathematical or "
    "editorial correctness, publication readiness, or rights beyond the "
    "rights and caveats already recorded.</p>"
)


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=True,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


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


def normalized_sha256(value: Any) -> str:
    result = str(value or "").strip().upper()
    if not re.fullmatch(r"[0-9A-F]{64}", result):
        raise RuntimeError(f"Invalid SHA-256 value: {value!r}")
    return result


def normalized_md5(value: Any) -> str:
    result = str(value or "").strip().lower().removeprefix("md5:")
    if not re.fullmatch(r"[0-9a-f]{32}", result):
        raise RuntimeError(f"Invalid MD5 value: {value!r}")
    return result


def as_bool(value: Any, field: str) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, int) and value in {0, 1}:
        return bool(value)
    lowered = str(value).strip().lower()
    if lowered in {"true", "yes", "1"}:
        return True
    if lowered in {"false", "no", "0", ""}:
        return False
    raise RuntimeError(f"Invalid Boolean for {field}: {value!r}")


def check(response: requests.Response, expected: set[int]) -> requests.Response:
    if response.status_code not in expected:
        raise RuntimeError(
            f"Zenodo HTTP {response.status_code} for "
            f"{response.request.method} {response.url}: {response.text[:2000]}"
        )
    return response


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
            "User-Agent": "modern-latex-manuscripts-active-custody/1.0",
            "Connection": "close",
        }
    )
    return session


def find_token() -> str:
    direct = os.environ.get("ZENODO_TOKEN")
    if direct:
        return direct
    if not TOKEN_LOG.is_file():
        raise RuntimeError("ZENODO_TOKEN is unset and the retained token log is absent")
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


def auth_headers(token: str, *, json_content: bool = False) -> dict[str, str]:
    result = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.inveniordm.v1+json",
    }
    if json_content:
        result["Content-Type"] = "application/json"
    return result


def save_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=True, indent=2) + "\n"
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def safe_slug(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-.")
    if not slug or slug != value:
        raise RuntimeError(
            "release_id must already be a filesystem-safe ASCII slug"
        )
    return slug


def state_path_for(spec: dict[str, Any]) -> Path:
    release_id = safe_slug(str(spec["release_id"]))
    return REPO_ROOT / "tmp" / "zenodo" / release_id / "draft_state.json"


def safe_zip_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        bool(name)
        and name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
    )


def zip_inventory(path: Path, *, include_members: bool = True) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    with zipfile.ZipFile(path) as archive:
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename for info in infos]
        if len(names) != len(set(names)):
            raise RuntimeError(f"Duplicate ZIP member in {path}")
        if not all(safe_zip_member(name) for name in names):
            raise RuntimeError(f"Unsafe ZIP member in {path}")
        for info in infos:
            digest = hashlib.sha256()
            total = 0
            with archive.open(info, "r") as handle:
                for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
                    total += len(block)
                    digest.update(block)
            if total != info.file_size:
                raise RuntimeError(f"ZIP member length changed: {info.filename}")
            rows.append(
                {
                    "name": info.filename,
                    "bytes": total,
                    "sha256": digest.hexdigest().upper(),
                }
            )
    rows.sort(key=lambda row: row["name"])
    result: dict[str, Any] = {
        "member_count": len(rows),
        "uncompressed_bytes": sum(int(row["bytes"]) for row in rows),
        "inventory_sha256": sha256_bytes(canonical_bytes(rows)),
        "safe_member_names": True,
        "all_members_streamed": True,
    }
    if include_members:
        result["members"] = rows
    return result


def normalized_file_row(row: dict[str, Any], *, require_zip: bool) -> dict[str, Any]:
    name = str(row.get("name") or row.get("filename") or "")
    if (
        not name
        or Path(name).name != name
        or "/" in name
        or "\\" in name
        or any(ord(character) < 32 for character in name)
    ):
        raise RuntimeError(f"Unsafe Zenodo filename: {name!r}")
    result: dict[str, Any] = {
        "name": name,
        "bytes": int(row["bytes"]),
        "md5": normalized_md5(row["md5"]),
        "sha256": normalized_sha256(row["sha256"]),
    }
    if result["bytes"] < 0:
        raise RuntimeError(f"Negative byte count for {name}")
    if name.lower().endswith(".zip"):
        zip_fields = (
            "zip_member_count",
            "zip_uncompressed_bytes",
            "zip_inventory_sha256",
        )
        if require_zip and not all(field in row for field in zip_fields):
            raise RuntimeError(
                f"Predecessor ZIP row lacks exact member guard: {name}"
            )
        if all(field in row and str(row[field]).strip() for field in zip_fields):
            result.update(
                {
                    "zip_member_count": int(row["zip_member_count"]),
                    "zip_uncompressed_bytes": int(row["zip_uncompressed_bytes"]),
                    "zip_inventory_sha256": normalized_sha256(
                        row["zip_inventory_sha256"]
                    ),
                }
            )
    return result


def normalized_predecessor_row(row: dict[str, Any]) -> dict[str, Any]:
    name = str(row.get("name") or row.get("filename") or "")
    if (
        not name
        or Path(name).name != name
        or "/" in name
        or "\\" in name
        or any(ord(character) < 32 for character in name)
    ):
        raise RuntimeError(f"Unsafe Zenodo predecessor filename: {name!r}")
    file_id = str(row.get("zenodo_file_id") or "").strip()
    if not re.fullmatch(r"[0-9A-Fa-f-]{36}", file_id):
        raise RuntimeError(f"Invalid Zenodo predecessor file UUID: {name}")
    result = {
        "name": name,
        "bytes": int(row["bytes"]),
        "md5": normalized_md5(row["md5"]),
        "zenodo_file_id": file_id.lower(),
    }
    if result["bytes"] < 0:
        raise RuntimeError(f"Negative predecessor byte count for {name}")
    return result


def inventory_digest(rows: Iterable[dict[str, Any]]) -> str:
    normalized = [
        normalized_file_row(dict(row), require_zip=False) for row in rows
    ]
    normalized.sort(key=lambda row: row["name"])
    return sha256_bytes(canonical_bytes(normalized))


def predecessor_inventory_digest(rows: Iterable[dict[str, Any]]) -> str:
    normalized = [normalized_predecessor_row(dict(row)) for row in rows]
    normalized.sort(key=lambda row: row["name"])
    return sha256_bytes(canonical_bytes(normalized))


def resolve_local_path(value: Any, base: Path) -> Path:
    path = Path(str(value))
    if not path.is_absolute():
        path = base / path
    return path.resolve()


def parse_manifest_rows(path: Path) -> list[dict[str, Any]]:
    if path.suffix.lower() == ".json":
        document = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(document, list):
            rows = document
        else:
            if document.get("schema") not in {None, MANIFEST_SCHEMA}:
                raise RuntimeError(f"Unsupported manifest schema: {path}")
            rows = document.get("files")
        if not isinstance(rows, list):
            raise RuntimeError(f"Manifest files must be a list: {path}")
        return [dict(row) for row in rows]
    if path.suffix.lower() == ".csv":
        with path.open(encoding="utf-8-sig", newline="") as handle:
            return [dict(row) for row in csv.DictReader(handle)]
    raise RuntimeError(f"Upload manifest must be JSON or CSV: {path}")


def load_manifest(
    target_key: str,
    target: dict[str, Any],
    spec_path: Path,
) -> dict[str, Any]:
    manifest_path = resolve_local_path(target["manifest_path"], spec_path.parent)
    if not manifest_path.is_file():
        raise RuntimeError(f"Missing {target_key} manifest: {manifest_path}")
    manifest_bytes = manifest_path.stat().st_size
    manifest_sha = sha256_path(manifest_path)
    guard = target.get("manifest_guard") or {}
    if (manifest_bytes, manifest_sha) != (
        int(guard.get("bytes", -1)),
        normalized_sha256(guard.get("sha256")),
    ):
        raise RuntimeError(f"{target_key} manifest identity changed")

    rows = parse_manifest_rows(manifest_path)
    if not rows:
        raise RuntimeError(f"{target_key} manifest has no upload files")
    files: list[dict[str, Any]] = []
    for raw in rows:
        normalized = normalized_file_row(raw, require_zip=False)
        local_value = raw.get("path") or raw.get("source_path") or raw.get(
            "local_path"
        )
        if not local_value:
            raise RuntimeError(
                f"Manifest row has no local path: {normalized['name']}"
            )
        local_path = resolve_local_path(local_value, manifest_path.parent)
        if not local_path.is_file():
            raise RuntimeError(f"Missing upload file: {local_path}")
        observed = (
            local_path.stat().st_size,
            sha256_path(local_path),
            md5_path(local_path),
        )
        expected = (
            normalized["bytes"],
            normalized["sha256"],
            normalized["md5"],
        )
        if observed != expected:
            raise RuntimeError(
                f"Local upload identity changed for {target_key}: "
                f"{normalized['name']}"
            )
        normalized.update(
            {
                "path": local_path,
                "role": str(raw.get("role") or "").strip(),
                "dual_doi_provenance": as_bool(
                    raw.get("dual_doi_provenance", False),
                    "dual_doi_provenance",
                ),
                "privacy_clean": as_bool(
                    raw.get("privacy_clean", False), "privacy_clean"
                ),
                "control_binding_sha256": (
                    normalized_sha256(raw["control_binding_sha256"])
                    if str(raw.get("control_binding_sha256", "")).strip()
                    else None
                ),
            }
        )
        if not normalized["role"]:
            raise RuntimeError(f"Manifest role is empty: {normalized['name']}")
        if normalized["name"].lower().endswith(".zip"):
            local_zip = zip_inventory(local_path, include_members=False)
            supplied_zip = {
                "member_count": normalized.get("zip_member_count"),
                "uncompressed_bytes": normalized.get("zip_uncompressed_bytes"),
                "inventory_sha256": normalized.get("zip_inventory_sha256"),
            }
            if any(value is not None for value in supplied_zip.values()) and (
                supplied_zip != {
                    "member_count": local_zip["member_count"],
                    "uncompressed_bytes": local_zip["uncompressed_bytes"],
                    "inventory_sha256": local_zip["inventory_sha256"],
                }
            ):
                raise RuntimeError(
                    f"Local ZIP member guard changed: {normalized['name']}"
                )
            normalized.update(
                {
                    "zip_member_count": local_zip["member_count"],
                    "zip_uncompressed_bytes": local_zip["uncompressed_bytes"],
                    "zip_inventory_sha256": local_zip["inventory_sha256"],
                }
            )
        files.append(normalized)

    names = [row["name"] for row in files]
    if len(names) != len(set(names)) or len(names) != len(
        {name.casefold() for name in names}
    ):
        raise RuntimeError(f"Duplicate or case-colliding {target_key} filenames")
    return {
        "path": manifest_path,
        "bytes": manifest_bytes,
        "sha256": manifest_sha,
        "files": files,
        "by_name": {row["name"]: row for row in files},
    }


def validate_control(spec: dict[str, Any], spec_path: Path) -> dict[str, Any]:
    control = spec.get("control") or {}
    path = resolve_local_path(control.get("path", ""), spec_path.parent)
    try:
        same_path = path == CONTROL_PATH.resolve()
    except OSError:
        same_path = False
    observed = (
        path.stat().st_size if path.is_file() else -1,
        sha256_path(path) if path.is_file() else "",
    )
    expected = (
        int(control.get("bytes", -1)),
        normalized_sha256(control.get("sha256")),
    )
    if (
        not same_path
        or observed != (CONTROL_BYTES, CONTROL_SHA256)
        or expected != (CONTROL_BYTES, CONTROL_SHA256)
    ):
        raise RuntimeError("The exact dual-DOI logbook control is not bound")
    return {"path": path, "bytes": observed[0], "sha256": observed[1]}


def validate_predecessor_guard(
    target_key: str, target: dict[str, Any]
) -> dict[str, Any]:
    registry = TARGETS[target_key]
    guard = target.get("predecessor_guard") or {}
    fixed = (
        int(guard.get("record_id", -1)),
        int(guard.get("concept_id", -1)),
        str(guard.get("concept_doi", "")),
    )
    expected_fixed = (
        registry["predecessor_record"],
        registry["concept_id"],
        registry["concept_doi"],
    )
    if fixed != expected_fixed:
        raise RuntimeError(f"{target_key} predecessor/concept guard changed")
    if str(guard.get("version_doi", "")) != (
        f"10.5281/zenodo.{registry['predecessor_record']}"
    ):
        raise RuntimeError(f"{target_key} version DOI guard changed")
    if not str(guard.get("title", "")).strip():
        raise RuntimeError(f"{target_key} predecessor title guard is empty")
    rows = [normalized_predecessor_row(dict(row)) for row in guard.get("files", [])]
    names = [row["name"] for row in rows]
    if not rows or len(names) != len(set(names)):
        raise RuntimeError(f"{target_key} predecessor file guard is not exact")
    observed_aggregate = (
        len(rows),
        sum(int(row["bytes"]) for row in rows),
        predecessor_inventory_digest(rows),
    )
    expected_aggregate = (
        int(guard.get("file_count", -1)),
        int(guard.get("total_bytes", -1)),
        normalized_sha256(guard.get("inventory_sha256")),
    )
    if observed_aggregate != expected_aggregate:
        raise RuntimeError(f"{target_key} predecessor aggregate guard is invalid")
    guard = copy.deepcopy(guard)
    guard["record_id"] = fixed[0]
    guard["concept_id"] = fixed[1]
    guard["concept_doi"] = fixed[2]
    guard["file_count"] = observed_aggregate[0]
    guard["total_bytes"] = observed_aggregate[1]
    guard["inventory_sha256"] = observed_aggregate[2]
    guard["files"] = rows
    guard["by_name"] = {row["name"]: row for row in rows}
    return guard


def file_policy(target_key: str, target: dict[str, Any]) -> dict[str, Any]:
    policy = copy.deepcopy(target.get("file_policy") or {"mode": "add-only"})
    mode = str(policy.get("mode", "add-only"))
    if mode not in {"add-only", "add-or-replace-named"}:
        raise RuntimeError(f"Unsupported {target_key} file policy: {mode}")
    replace_names = [str(name) for name in policy.get("replace_names", [])]
    if mode == "add-only" and replace_names:
        raise RuntimeError(f"{target_key} add-only policy names replacements")
    if mode == "add-or-replace-named" and not replace_names:
        raise RuntimeError(f"{target_key} replacement policy is not explicit")
    if len(replace_names) != len(set(replace_names)):
        raise RuntimeError(f"{target_key} replacement names are duplicated")
    return {"mode": mode, "replace_names": replace_names}


def normalized_dual_rows(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for row in manifest["files"]:
        if not row["dual_doi_provenance"]:
            continue
        rows.append(
            {
                key: row[key]
                for key in (
                    "name",
                    "bytes",
                    "md5",
                    "sha256",
                    "role",
                    "privacy_clean",
                    "control_binding_sha256",
                    "zip_member_count",
                    "zip_uncompressed_bytes",
                    "zip_inventory_sha256",
                )
                if key in row
            }
        )
    return sorted(rows, key=lambda row: row["name"])


def validate_dual_doi(manifests: dict[str, dict[str, Any]]) -> dict[str, Any]:
    for target_key in ("methodology", "replication"):
        for row in manifests[target_key]["files"]:
            role_is_provenance = any(
                word in row["role"].casefold() for word in PROVENANCE_ROLE_WORDS
            )
            is_control = (row["bytes"], row["sha256"]) == (
                CONTROL_BYTES,
                CONTROL_SHA256,
            )
            if (role_is_provenance or is_control) and not row[
                "dual_doi_provenance"
            ]:
                raise RuntimeError(
                    f"{target_key} provenance was not marked for both DOI "
                    f"records: {row['name']}"
                )
    methodology = normalized_dual_rows(manifests["methodology"])
    replication = normalized_dual_rows(manifests["replication"])
    if not methodology or methodology != replication:
        raise RuntimeError(
            "Methodology and replication dual-DOI provenance payloads differ"
        )
    for row in methodology:
        if (
            row["privacy_clean"] is not True
            or row["control_binding_sha256"] != CONTROL_SHA256
        ):
            raise RuntimeError(
                f"Dual-DOI provenance is not privacy-clean/control-bound: "
                f"{row['name']}"
            )
    if any(
        (row["bytes"], row["sha256"]) == (CONTROL_BYTES, CONTROL_SHA256)
        for row in methodology
    ):
        raise RuntimeError(
            "The raw archive control contains internal task identifiers and "
            "must not be uploaded"
        )
    control_rows = [
        row
        for row in methodology
        if PurePosixPath(row["name"].replace("\\", "/")).name
        == CONTROL_PATH.name
    ]
    if len(control_rows) != 1 or (
        control_rows[0]["bytes"], control_rows[0]["sha256"]
    ) != (CONTROL_PUBLIC_BYTES, CONTROL_PUBLIC_SHA256):
        raise RuntimeError(
            "The privacy-clean archive-control projection is not in both DOI "
            "payloads"
        )
    binding_rows = [
        row
        for row in manifests["methodology"]["files"]
        if row["dual_doi_provenance"]
        and PurePosixPath(row["name"].replace("\\", "/")).name
        == CONTROL_BINDING_MANIFEST_NAME
    ]
    if len(binding_rows) != 1:
        raise RuntimeError(
            "The exact-private-to-public archive-control identity manifest is "
            "not in both DOI payloads"
        )
    try:
        binding_document = json.loads(
            binding_rows[0]["path"].read_text(encoding="utf-8")
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("Archive-control identity manifest is unreadable") from exc
    binding_matches = [
        row
        for row in binding_document
        if row.get("relative_path", "").replace("\\", "/").endswith(
            "/" + CONTROL_PATH.name
        )
        and (int(row.get("original_bytes", -1)), row.get("original_sha256"))
        == (CONTROL_BYTES, CONTROL_SHA256)
        and (int(row.get("public_bytes", -1)), row.get("public_sha256"))
        == (CONTROL_PUBLIC_BYTES, CONTROL_PUBLIC_SHA256)
        and row.get("status")
        == "BOUND_EXACT_ORIGINAL_IDENTITY_WITH_PRIVACY_CLEAN_PUBLIC_PROJECTION"
    ]
    if len(binding_matches) != 1:
        raise RuntimeError(
            "Archive-control identity manifest does not bind the exact private "
            "control to its privacy-clean public projection"
        )
    direct_history_words = (
        "logbook",
        "decision",
        "revision",
        "reversal",
        "continuation",
    )
    if not any(
        any(word in row["role"].casefold() for word in direct_history_words)
        and row not in control_rows
        and not row["name"].lower().endswith(".zip")
        for row in methodology
    ):
        raise RuntimeError(
            "Both DOI payloads require a privacy-clean logbook/decision/"
            "revision/continuation provenance object"
        )
    if not any(
        "manifest" in row["role"].casefold()
        and not row["name"].lower().endswith(".zip")
        for row in methodology
    ):
        raise RuntimeError(
            "Both DOI payloads require the identical public provenance manifest"
        )
    return {
        "file_count": len(methodology),
        "total_bytes": sum(int(row["bytes"]) for row in methodology),
        "inventory_sha256": inventory_digest(methodology),
        "control_included": True,
        "public_provenance_manifest_included": True,
        "exact_private_control_bound_without_public_disclosure": True,
        "direct_revision_history_included": True,
        "identical_on_methodology_and_replication": True,
    }


def validate_metadata_append(target_key: str, target: dict[str, Any]) -> None:
    append = target.get("metadata_append") or {}
    if not str(append.get("version_suffix", "")).strip():
        raise RuntimeError(f"{target_key} version suffix is empty")
    if not str(append.get("description_html", "")).strip():
        raise RuntimeError(f"{target_key} description append is empty")
    links = append.get("cross_links")
    if not isinstance(links, list) or not links:
        raise RuntimeError(f"{target_key} cross-links are empty")
    for link in links:
        if not str(link.get("identifier", "")).strip() or not str(
            link.get("scheme", "")
        ).strip():
            raise RuntimeError(f"{target_key} has an invalid cross-link")


def load_release_spec(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    spec = json.loads(raw.decode("utf-8"))
    if spec.get("schema") != SCHEMA:
        raise RuntimeError(f"Expected release schema {SCHEMA}")
    safe_slug(str(spec.get("release_id", "")))
    if spec.get("publication_date") != PUBLICATION_DATE:
        raise RuntimeError(f"publication_date must be {PUBLICATION_DATE}")
    if set(spec.get("targets", {})) != set(TARGETS):
        raise RuntimeError("Release specification must contain exactly four targets")
    if tuple(spec.get("safe_publish_order", SAFE_PUBLISH_ORDER)) != (
        SAFE_PUBLISH_ORDER
    ):
        raise RuntimeError("The release safe publish order may not be changed")

    control = validate_control(spec, path)
    manifests: dict[str, dict[str, Any]] = {}
    guards: dict[str, dict[str, Any]] = {}
    policies: dict[str, dict[str, Any]] = {}
    for target_key, target in spec["targets"].items():
        guards[target_key] = validate_predecessor_guard(target_key, target)
        manifests[target_key] = load_manifest(target_key, target, path)
        policies[target_key] = file_policy(target_key, target)
        validate_metadata_append(target_key, target)
        old_names = set(guards[target_key]["by_name"])
        new_names = set(manifests[target_key]["by_name"])
        replacements = set(policies[target_key]["replace_names"])
        collisions = old_names & new_names
        if policies[target_key]["mode"] == "add-only" and collisions:
            raise RuntimeError(
                f"{target_key} add-only names collide with predecessor: "
                f"{sorted(collisions)}"
            )
        if policies[target_key]["mode"] == "add-or-replace-named":
            if replacements != collisions:
                raise RuntimeError(
                    f"{target_key} explicit replacement set does not equal "
                    "the manifest/predecessor collisions"
                )

    dual = validate_dual_doi(manifests)
    spec["_path"] = path.resolve()
    spec["_bytes"] = len(raw)
    spec["_sha256"] = sha256_bytes(raw)
    spec["_control"] = control
    spec["_manifests"] = manifests
    spec["_guards"] = guards
    spec["_policies"] = policies
    spec["_dual_doi"] = dual
    return spec


def public_concept_doi(record: dict[str, Any]) -> str | None:
    return (
        record.get("parent", {})
        .get("pids", {})
        .get("doi", {})
        .get("identifier")
        or record.get("conceptdoi")
    )


def public_version_doi(record: dict[str, Any]) -> str | None:
    return (
        record.get("pids", {}).get("doi", {}).get("identifier")
        or record.get("doi")
    )


def modern_entries(record: dict[str, Any]) -> dict[str, dict[str, Any]]:
    entries = record.get("files", {}).get("entries")
    if not isinstance(entries, dict):
        raise RuntimeError(f"Modern Zenodo file entries absent for {record.get('id')}")
    return entries


def legacy_entries(record: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(row["filename"]): row for row in record.get("files", [])}


def stream_public_file(
    session: requests.Session,
    url: str,
    *,
    destination: Path | None = None,
) -> dict[str, Any]:
    digest = hashlib.sha256()
    md5 = hashlib.md5(usedforsecurity=False)
    total = 0
    handle = destination.open("wb") if destination is not None else None
    try:
        with check(session.get(url, stream=True, timeout=(30, 3600)), {200}) as response:
            if "access_token=" in response.url or "Authorization" in response.request.headers:
                raise RuntimeError("Anonymous public readback unexpectedly used credentials")
            for block in response.iter_content(4 * 1024 * 1024):
                if not block:
                    continue
                total += len(block)
                digest.update(block)
                md5.update(block)
                if handle is not None:
                    handle.write(block)
    finally:
        if handle is not None:
            handle.close()
    return {
        "bytes": total,
        "sha256": digest.hexdigest().upper(),
        "md5": md5.hexdigest().lower(),
        "readback_mode": "anonymous_whole_file_streaming_sha256_md5",
    }


def load_modern_record(
    session: requests.Session,
    record_id: int,
    *,
    token: str | None = None,
    draft: bool = False,
) -> dict[str, Any]:
    suffix = "/draft" if draft else ""
    headers = (
        auth_headers(token) if token else {"Accept": "application/vnd.inveniordm.v1+json"}
    )
    return check(
        session.get(
            f"{API}/records/{record_id}{suffix}?expand=true",
            headers=headers,
            timeout=(30, 300),
        ),
        {200},
    ).json()


def verify_predecessor(
    session: requests.Session,
    anonymous: requests.Session,
    target_key: str,
    spec: dict[str, Any],
    scratch: Path,
    *,
    require_latest: bool,
) -> dict[str, Any]:
    guard = spec["_guards"][target_key]
    registry = TARGETS[target_key]
    record_id = registry["predecessor_record"]
    record = load_modern_record(session, record_id)
    if require_latest:
        latest = check(
            session.get(
                f"{API}/records/{record_id}/versions/latest?expand=true",
                headers={"Accept": "application/vnd.inveniordm.v1+json"},
                timeout=(30, 300),
            ),
            {200},
        ).json()
        if int(latest["id"]) != record_id:
            raise RuntimeError(f"{target_key} concept head moved")
    observed_header = (
        int(record["id"]),
        public_version_doi(record),
        public_concept_doi(record),
        record.get("metadata", {}).get("title"),
        bool(record.get("is_published")),
    )
    expected_header = (
        record_id,
        guard["version_doi"],
        registry["concept_doi"],
        guard["title"],
        True,
    )
    if observed_header != expected_header:
        raise RuntimeError(
            f"{target_key} predecessor header changed: {observed_header!r}"
        )
    entries = modern_entries(record)
    if set(entries) != set(guard["by_name"]):
        raise RuntimeError(f"{target_key} predecessor file set changed")

    observed_rows: list[dict[str, Any]] = []
    for name in sorted(entries):
        api_row = entries[name]
        expected = guard["by_name"][name]
        api_identity = (
            int(api_row["size"]),
            normalized_md5(api_row["checksum"]),
            str(api_row.get("id") or "").lower(),
        )
        if api_identity != (
            expected["bytes"],
            expected["md5"],
            expected["zenodo_file_id"],
        ):
            raise RuntimeError(f"{target_key} predecessor API file changed: {name}")
        observed_rows.append(
            {
            "name": name,
                "bytes": api_identity[0],
                "md5": api_identity[1],
                "zenodo_file_id": api_identity[2],
            }
        )
    observed_aggregate = (
        len(observed_rows),
        sum(int(row["bytes"]) for row in observed_rows),
        predecessor_inventory_digest(observed_rows),
    )
    expected_aggregate = (
        guard["file_count"],
        guard["total_bytes"],
        guard["inventory_sha256"],
    )
    if observed_aggregate != expected_aggregate:
        raise RuntimeError(f"{target_key} predecessor byte aggregate changed")
    return record


def list_account_depositions(
    session: requests.Session, token: str
) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    page_size = 100
    for page in range(1, 101):
        batch = check(
            session.get(
                f"{API}/deposit/depositions",
                headers={"Authorization": f"Bearer {token}"},
                params={"size": page_size, "page": page},
                timeout=(30, 300),
            ),
            {200},
        ).json()
        if not isinstance(batch, list):
            raise RuntimeError("Account-wide deposition listing was not a list")
        results.extend(batch)
        if len(batch) < page_size:
            return results
    raise RuntimeError("Account-wide deposition scan exceeded 10,000 records")


def deposition_concept_id(
    session: requests.Session, token: str, deposition: dict[str, Any]
) -> int | None:
    for key in ("conceptrecid", "concept_id"):
        value = deposition.get(key)
        if value is not None and str(value).isdigit():
            return int(value)
    concept_doi = str(deposition.get("conceptdoi") or "")
    match = re.fullmatch(r"10\.5281/zenodo\.(\d+)", concept_doi)
    if match:
        return int(match.group(1))
    draft_id = int(deposition["id"])
    response = session.get(
        f"{API}/records/{draft_id}/draft?expand=true",
        headers=auth_headers(token),
        timeout=(30, 180),
    )
    if response.status_code == 404:
        return None
    draft = check(response, {200}).json()
    parent_doi = public_concept_doi(draft) or ""
    match = re.fullmatch(r"10\.5281/zenodo\.(\d+)", parent_doi)
    return int(match.group(1)) if match else None


def account_active_drafts(
    session: requests.Session, token: str
) -> dict[str, Any]:
    depositions = list_account_depositions(session, token)
    active = [
        row
        for row in depositions
        if row.get("state") != "done" or not bool(row.get("submitted"))
    ]
    concept_to_target = {
        int(value["concept_id"]): key for key, value in TARGETS.items()
    }
    target_drafts: dict[str, list[int]] = {key: [] for key in TARGETS}
    unrelated = 0
    for row in active:
        concept_id = deposition_concept_id(session, token, row)
        target_key = concept_to_target.get(concept_id)
        if target_key is None:
            unrelated += 1
            continue
        target_drafts[target_key].append(int(row["id"]))
    for draft_ids in target_drafts.values():
        draft_ids.sort()
    return {
        "account_deposition_count": len(depositions),
        "account_active_draft_count": len(active),
        "unrelated_active_draft_count": unrelated,
        "target_active_drafts": target_drafts,
    }


def load_state(spec: dict[str, Any]) -> dict[str, Any] | None:
    path = state_path_for(spec)
    if not path.is_file():
        return None
    state = json.loads(path.read_text(encoding="utf-8"))
    if (
        state.get("schema") != "zenodo-active-custody-state-v1"
        or state.get("release_id") != spec["release_id"]
        or state.get("release_spec_sha256") != spec["_sha256"]
        or set(state.get("targets", {})) != set(TARGETS)
    ):
        raise RuntimeError("Tracked draft state does not match the release spec")
    return state


def initial_state(spec: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "zenodo-active-custody-state-v1",
        "release_id": spec["release_id"],
        "release_spec_path": str(spec["_path"]),
        "release_spec_bytes": spec["_bytes"],
        "release_spec_sha256": spec["_sha256"],
        "control_sha256": CONTROL_SHA256,
        "safe_publish_order": list(SAFE_PUBLISH_ORDER),
        "targets": {
            key: {
                "status": "NOT_STARTED",
                "predecessor_record": value["predecessor_record"],
                "concept_id": value["concept_id"],
                "concept_doi": value["concept_doi"],
            }
            for key, value in TARGETS.items()
        },
    }


def save_state(spec: dict[str, Any], state: dict[str, Any]) -> None:
    state["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    save_json_atomic(state_path_for(spec), state)


def assert_account_drafts_tracked(
    scan: dict[str, Any],
    state: dict[str, Any] | None,
    *,
    allow_creation_recovery: bool,
) -> None:
    for target_key, observed_list in scan["target_active_drafts"].items():
        observed = set(observed_list)
        target_state = (state or {}).get("targets", {}).get(target_key, {})
        status = target_state.get("status", "NOT_STARTED")
        tracked_id = target_state.get("draft_id")
        expected = {int(tracked_id)} if tracked_id and status in OPEN_STATUSES else set()
        if observed == expected:
            continue
        if (
            allow_creation_recovery
            and status == "CREATE_INTENT"
            and tracked_id is None
            and len(observed) == 1
        ):
            continue
        raise RuntimeError(
            f"Untracked or parallel active draft for {target_key}: "
            f"observed={sorted(observed)}, tracked={sorted(expected)}"
        )


def final_file_rows(
    target_key: str, spec: dict[str, Any]
) -> dict[str, dict[str, Any]]:
    predecessor = copy.deepcopy(spec["_guards"][target_key]["by_name"])
    policy = spec["_policies"][target_key]
    for name in policy["replace_names"]:
        predecessor.pop(name)
    for name, row in spec["_manifests"][target_key]["by_name"].items():
        predecessor[name] = row
    return predecessor


def draft_matches_predecessor(
    draft: dict[str, Any], target_key: str, spec: dict[str, Any]
) -> None:
    entries = legacy_entries(draft) if isinstance(draft.get("files"), list) else modern_entries(draft)
    expected = spec["_guards"][target_key]["by_name"]
    if set(entries) != set(expected):
        raise RuntimeError(f"New {target_key} draft did not inherit every file")
    for name, row in expected.items():
        entry = entries[name]
        size = int(entry.get("filesize", entry.get("size", -1)))
        checksum = normalized_md5(entry["checksum"])
        if (size, checksum) != (row["bytes"], row["md5"]):
            raise RuntimeError(f"Inherited {target_key} draft file changed: {name}")


def create_or_resume_draft(
    session: requests.Session,
    token: str,
    target_key: str,
    spec: dict[str, Any],
    state: dict[str, Any],
    predecessor: dict[str, Any],
) -> int:
    target_state = state["targets"][target_key]
    status = target_state["status"]
    if status in {"DRAFT_CREATED", "STAGED"}:
        draft_id = int(target_state["draft_id"])
        draft = load_modern_record(session, draft_id, token=token, draft=True)
        if public_concept_doi(draft) != TARGETS[target_key]["concept_doi"]:
            raise RuntimeError(f"Tracked {target_key} draft escaped its concept")
        return draft_id
    if status in PUBLISHED_STATUSES:
        return int(target_state["record_id"])

    scan = account_active_drafts(session, token)
    observed = scan["target_active_drafts"][target_key]
    if status == "CREATE_INTENT" and target_state.get("draft_id") is None:
        if len(observed) == 1:
            draft_id = int(observed[0])
            draft = load_modern_record(session, draft_id, token=token, draft=True)
            if public_concept_doi(draft) != TARGETS[target_key]["concept_doi"]:
                raise RuntimeError(f"Recovered {target_key} draft has wrong concept")
            draft_matches_predecessor(draft, target_key, spec)
            target_state.update(
                {"status": "DRAFT_CREATED", "draft_id": draft_id, "recovered": True}
            )
            save_state(spec, state)
            return draft_id
        if observed:
            raise RuntimeError(f"Ambiguous {target_key} draft creation recovery")
    elif observed:
        raise RuntimeError(f"Untracked {target_key} draft exists before creation")

    target_state.update({"status": "CREATE_INTENT", "draft_id": None})
    save_state(spec, state)
    base = check(
        session.get(
            f"{API}/deposit/depositions/{TARGETS[target_key]['predecessor_record']}",
            headers={"Authorization": f"Bearer {token}"},
            timeout=(30, 300),
        ),
        {200},
    ).json()
    if base.get("state") != "done" or not base.get("submitted"):
        raise RuntimeError(f"{target_key} predecessor is not a versioning base")
    newversion = base.get("links", {}).get("newversion")
    if not newversion or "/deposit/depositions/" not in newversion:
        raise RuntimeError(f"{target_key} predecessor has no same-concept newversion")
    created = check(
        session.post(
            newversion,
            headers={"Authorization": f"Bearer {token}"},
            timeout=(30, 300),
        ),
        {201},
    ).json()
    latest_draft = created.get("links", {}).get("latest_draft")
    if not latest_draft:
        raise RuntimeError(f"{target_key} newversion response lacks latest_draft")
    legacy_draft = check(
        session.get(
            latest_draft,
            headers={"Authorization": f"Bearer {token}"},
            timeout=(30, 300),
        ),
        {200},
    ).json()
    draft_id = int(legacy_draft["id"])
    draft_matches_predecessor(legacy_draft, target_key, spec)
    modern = load_modern_record(session, draft_id, token=token, draft=True)
    if public_concept_doi(modern) != TARGETS[target_key]["concept_doi"]:
        raise RuntimeError(f"New {target_key} version escaped its existing concept")
    target_state.update(
        {
            "status": "DRAFT_CREATED",
            "draft_id": draft_id,
            "same_concept_newversion": True,
        }
    )
    save_state(spec, state)
    return draft_id


def relation_type(link: dict[str, Any]) -> dict[str, str]:
    value = link.get("relation_type", link.get("relation", "isrelatedto"))
    if isinstance(value, dict):
        value = value.get("id", "isrelatedto")
    return {"id": str(value).strip().lower()}


def merged_related_identifiers(
    existing: list[dict[str, Any]],
    target_key: str,
    target: dict[str, Any],
) -> list[dict[str, Any]]:
    def existing_relation_id(row: dict[str, Any]) -> str:
        value = row.get("relation_type", row.get("relation", ""))
        if isinstance(value, dict):
            value = value.get("id", "")
        return str(value)

    result = copy.deepcopy(existing)
    additions = list(target["metadata_append"]["cross_links"])
    for other_key, registry in TARGETS.items():
        if other_key == target_key:
            continue
        additions.append(
            {
                "identifier": registry["concept_doi"],
                "scheme": "doi",
                "relation_type": "isrelatedto",
            }
        )
    seen = {
        (
            str(row.get("identifier", "")),
            str(row.get("scheme", "")),
            existing_relation_id(row),
        )
        for row in result
    }
    for link in additions:
        normalized = {
            "identifier": str(link["identifier"]),
            "scheme": str(link["scheme"]),
            "relation_type": relation_type(link),
        }
        key = (
            normalized["identifier"],
            normalized["scheme"],
            normalized["relation_type"]["id"],
        )
        if key not in seen:
            result.append(normalized)
            seen.add(key)
    return result


def desired_metadata(
    target_key: str,
    target: dict[str, Any],
    predecessor: dict[str, Any],
) -> dict[str, Any]:
    metadata = copy.deepcopy(predecessor["metadata"])
    append = target["metadata_append"]
    old_version = str(metadata.get("version") or "").strip()
    suffix = str(append["version_suffix"]).strip()
    metadata["version"] = f"{old_version} | {suffix}" if old_version else suffix
    old_description = str(metadata.get("description") or "").rstrip()
    addition = str(append["description_html"]).strip()
    metadata["description"] = "\n".join(
        part
        for part in (
            old_description,
            f"<hr><p><strong>{PUBLICATION_DATE} active-custody update:</strong></p>",
            addition,
            NON_CERTIFYING_NOTICE,
        )
        if part
    )
    metadata["publication_date"] = PUBLICATION_DATE
    metadata["related_identifiers"] = merged_related_identifiers(
        metadata.get("related_identifiers", []), target_key, target
    )
    return metadata


def exact_api_file_check(
    entries: dict[str, dict[str, Any]], expected: dict[str, dict[str, Any]], label: str
) -> None:
    if set(entries) != set(expected):
        raise RuntimeError(f"{label} file set is not exact")
    for name, row in expected.items():
        entry = entries[name]
        size = int(entry.get("size", entry.get("filesize", -1)))
        if (size, normalized_md5(entry["checksum"])) != (
            row["bytes"],
            row["md5"],
        ):
            raise RuntimeError(f"{label} file identity changed: {name}")
        expected_file_id = row.get("zenodo_file_id")
        if expected_file_id and str(entry.get("id") or "").lower() != str(
            expected_file_id
        ).lower():
            raise RuntimeError(f"{label} inherited Zenodo object changed: {name}")


def stage_target(
    session: requests.Session,
    token: str,
    target_key: str,
    spec: dict[str, Any],
    state: dict[str, Any],
    predecessor: dict[str, Any],
    draft_id: int,
) -> None:
    target_state = state["targets"][target_key]
    target = spec["targets"][target_key]
    manifest = spec["_manifests"][target_key]
    policy = spec["_policies"][target_key]
    expected = final_file_rows(target_key, spec)
    auth = {"Authorization": f"Bearer {token}"}

    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    files = legacy_entries(deposition)
    allowed = set(spec["_guards"][target_key]["by_name"]) | set(
        manifest["by_name"]
    )
    if not set(files).issubset(allowed):
        raise RuntimeError(f"Tracked {target_key} draft contains unexpected files")

    for name in policy["replace_names"]:
        existing = files.get(name)
        wanted = manifest["by_name"][name]
        if existing is None:
            continue
        observed = (
            int(existing["filesize"]),
            normalized_md5(existing["checksum"]),
        )
        if observed == (wanted["bytes"], wanted["md5"]):
            continue
        check(
            session.delete(existing["links"]["self"], headers=auth, timeout=(30, 300)),
            {204},
        )

    deposition = check(
        session.get(
            f"{API}/deposit/depositions/{draft_id}",
            headers=auth,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    files = legacy_entries(deposition)
    bucket = deposition["links"]["bucket"].rstrip("/")
    for row in manifest["files"]:
        name = row["name"]
        existing = files.get(name)
        if existing is not None:
            observed = (
                int(existing["filesize"]),
                normalized_md5(existing["checksum"]),
            )
            if observed != (row["bytes"], row["md5"]):
                raise RuntimeError(f"Interrupted {target_key} upload differs: {name}")
            continue
        with row["path"].open("rb") as handle:
            uploaded = check(
                session.put(
                    f"{bucket}/{quote(name, safe='')}",
                    headers={**auth, "Content-Type": "application/octet-stream"},
                    data=handle,
                    timeout=(30, 3600),
                ),
                {200, 201},
            ).json()
        uploaded_size = int(uploaded.get("size", uploaded.get("filesize", -1)))
        uploaded_md5 = normalized_md5(uploaded["checksum"])
        if (uploaded_size, uploaded_md5) != (row["bytes"], row["md5"]):
            raise RuntimeError(f"Zenodo upload response changed: {target_key}/{name}")

    draft = load_modern_record(session, draft_id, token=token, draft=True)
    entries = modern_entries(draft)
    exact_api_file_check(entries, expected, f"Staged {target_key}")
    predecessor_entries = spec["_guards"][target_key]["by_name"]
    for name, row in predecessor_entries.items():
        if name in policy["replace_names"]:
            continue
        entry = entries[name]
        if (int(entry["size"]), normalized_md5(entry["checksum"])) != (
            row["bytes"],
            row["md5"],
        ):
            raise RuntimeError(f"Staged {target_key} inherited file changed: {name}")

    old_order = list(predecessor.get("files", {}).get("order") or [])
    ordered = [name for name in old_order if name in expected]
    for name in predecessor_entries:
        if name in expected and name not in ordered:
            ordered.append(name)
    for row in manifest["files"]:
        if row["name"] not in ordered:
            ordered.append(row["name"])
    payload: dict[str, Any] = {
        "access": copy.deepcopy(predecessor["access"]),
        "files": {
            "enabled": True,
            "default_preview": predecessor.get("files", {}).get("default_preview"),
            "order": ordered,
        },
        "metadata": desired_metadata(target_key, target, predecessor),
        "custom_fields": copy.deepcopy(predecessor.get("custom_fields", {})),
    }
    if draft.get("pids"):
        payload["pids"] = copy.deepcopy(draft["pids"])
    patched = check(
        session.put(
            f"{API}/records/{draft_id}/draft",
            headers=auth_headers(token, json_content=True),
            json=payload,
            timeout=(30, 300),
        ),
        {200},
    ).json()
    exact_api_file_check(modern_entries(patched), expected, f"Patched {target_key}")
    invariant_fields = ("title", "rights", "license")
    for field in invariant_fields:
        if patched["metadata"].get(field) != predecessor["metadata"].get(field):
            raise RuntimeError(f"Patched {target_key} changed metadata.{field}")
    if patched.get("access") != predecessor.get("access"):
        raise RuntimeError(f"Patched {target_key} changed access/license controls")
    if patched["metadata"] != payload["metadata"]:
        raise RuntimeError(f"Patched {target_key} metadata did not round-trip exactly")
    target_state.update(
        {
            "status": "STAGED",
            "draft_id": draft_id,
            "manifest_path": str(manifest["path"]),
            "manifest_bytes": manifest["bytes"],
            "manifest_sha256": manifest["sha256"],
            "staged_file_count": len(expected),
            "staged_total_bytes": sum(int(row["bytes"]) for row in expected.values()),
            "add_only": policy["mode"] == "add-only",
            "replacements": policy["replace_names"],
        }
    )
    save_state(spec, state)


def verify_staged_target(
    session: requests.Session,
    token: str,
    target_key: str,
    spec: dict[str, Any],
    predecessor: dict[str, Any],
    draft_id: int,
) -> dict[str, Any]:
    draft = load_modern_record(session, draft_id, token=token, draft=True)
    if public_concept_doi(draft) != TARGETS[target_key]["concept_doi"]:
        raise RuntimeError(f"Staged {target_key} draft escaped its concept")
    exact_api_file_check(
        modern_entries(draft), final_file_rows(target_key, spec), f"Staged {target_key}"
    )
    wanted_metadata = desired_metadata(
        target_key, spec["targets"][target_key], predecessor
    )
    if draft["metadata"] != wanted_metadata:
        raise RuntimeError(f"Staged {target_key} metadata changed before publish")
    for field in ("title", "rights", "license"):
        if draft["metadata"].get(field) != predecessor["metadata"].get(field):
            raise RuntimeError(f"Staged {target_key} changed metadata.{field}")
    if draft.get("access") != predecessor.get("access"):
        raise RuntimeError(f"Staged {target_key} changed access/license controls")
    return draft


def recover_uncertain_publish(
    session: requests.Session,
    target_key: str,
    spec: dict[str, Any],
    predecessor: dict[str, Any],
) -> dict[str, Any] | None:
    base_id = TARGETS[target_key]["predecessor_record"]
    latest = check(
        session.get(
            f"{API}/records/{base_id}/versions/latest?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 300),
        ),
        {200},
    ).json()
    if int(latest["id"]) == base_id:
        return None
    if public_concept_doi(latest) != TARGETS[target_key]["concept_doi"]:
        raise RuntimeError(f"Latest {target_key} record escaped its concept")
    exact_api_file_check(
        modern_entries(latest), final_file_rows(target_key, spec), f"Latest {target_key}"
    )
    if latest["metadata"] != desired_metadata(
        target_key, spec["targets"][target_key], predecessor
    ):
        raise RuntimeError(f"Latest {target_key} record is not this transaction")
    return latest


def publish_target(
    session: requests.Session,
    token: str,
    target_key: str,
    spec: dict[str, Any],
    state: dict[str, Any],
    predecessor: dict[str, Any],
) -> int:
    target_state = state["targets"][target_key]
    if target_state["status"] in PUBLISHED_STATUSES:
        return int(target_state["record_id"])
    draft_id = int(target_state["draft_id"])
    probe = session.get(
        f"{API}/records/{draft_id}/draft?expand=true",
        headers=auth_headers(token),
        timeout=(30, 300),
    )
    if probe.status_code == 404:
        recovered = recover_uncertain_publish(
            session, target_key, spec, predecessor
        )
        if recovered is None:
            raise RuntimeError(f"Tracked {target_key} draft disappeared")
        record_id = int(recovered["id"])
        target_state.update(
            {
                "status": "PUBLISHED_PENDING_READBACK",
                "record_id": record_id,
                "doi": public_version_doi(recovered),
                "publish_response_recovered": True,
            }
        )
        save_state(spec, state)
        return record_id
    draft = check(probe, {200}).json()
    verify_staged_target(
        session, token, target_key, spec, predecessor, draft_id
    )
    published = check(
        session.post(
            draft["links"]["publish"],
            headers=auth_headers(token),
            timeout=(30, 300),
        ),
        {202},
    ).json()
    record_id = int(published["id"])
    if public_concept_doi(published) != TARGETS[target_key]["concept_doi"]:
        raise RuntimeError(f"Published {target_key} escaped its concept")
    target_state.update(
        {
            "status": "PUBLISHED_PENDING_READBACK",
            "record_id": record_id,
            "doi": public_version_doi(published),
            "publish_response_recovered": False,
        }
    )
    save_state(spec, state)
    return record_id


def wait_public(session: requests.Session, record_id: int) -> dict[str, Any]:
    for _ in range(90):
        response = session.get(
            f"{API}/records/{record_id}?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 300),
        )
        if response.status_code == 200 and response.json().get("is_published"):
            return response.json()
        time.sleep(2)
    raise RuntimeError(f"Published record {record_id} did not become public")


def wait_latest(
    session: requests.Session, base_record_id: int, expected_record_id: int
) -> dict[str, Any]:
    last_id: int | None = None
    for _ in range(90):
        response = session.get(
            f"{API}/records/{base_record_id}/versions/latest?expand=true",
            headers={"Accept": "application/vnd.inveniordm.v1+json"},
            timeout=(30, 300),
        )
        if response.status_code == 200:
            latest = response.json()
            last_id = int(latest["id"])
            if last_id == expected_record_id:
                return latest
        time.sleep(2)
    raise RuntimeError(
        f"Concept head did not settle on {expected_record_id}; last={last_id}"
    )


def readback_target(
    authenticated: requests.Session,
    anonymous: requests.Session,
    token: str,
    target_key: str,
    record_id: int,
    spec: dict[str, Any],
    predecessor: dict[str, Any],
    scratch: Path,
) -> tuple[dict[str, Any], dict[str, Any]]:
    record = wait_public(anonymous, record_id)
    registry = TARGETS[target_key]
    expected = final_file_rows(target_key, spec)
    if (
        int(record["id"]) != record_id
        or public_concept_doi(record) != registry["concept_doi"]
        or not record.get("is_published")
    ):
        raise RuntimeError(f"Published {target_key} record boundary changed")
    latest = wait_latest(anonymous, registry["predecessor_record"], record_id)
    exact_api_file_check(modern_entries(record), expected, f"Public {target_key}")
    wanted_metadata = desired_metadata(
        target_key, spec["targets"][target_key], predecessor
    )
    if record["metadata"] != wanted_metadata:
        raise RuntimeError(f"Public {target_key} metadata changed")
    for field in ("title", "rights", "license"):
        if record["metadata"].get(field) != predecessor["metadata"].get(field):
            raise RuntimeError(f"Public {target_key} changed metadata.{field}")
    if record.get("access") != predecessor.get("access"):
        raise RuntimeError(f"Public {target_key} changed access/license controls")

    entries = modern_entries(record)
    outer: dict[str, dict[str, Any]] = {}
    archives: dict[str, dict[str, Any]] = {}
    new_payload = spec["_manifests"][target_key]["by_name"]
    for ordinal, name in enumerate(sorted(entries), start=1):
        row = expected[name]
        entry = entries[name]
        if name not in new_payload:
            retained_identity = (
                int(entry["size"]),
                normalized_md5(entry["checksum"]),
                str(entry.get("id") or "").lower(),
            )
            expected_retained = (
                row["bytes"],
                row["md5"],
                row["zenodo_file_id"],
            )
            if retained_identity != expected_retained:
                raise RuntimeError(
                    f"Public {target_key} retained predecessor changed: {name}"
                )
            outer[name] = {
                "bytes": retained_identity[0],
                "md5": retained_identity[1],
                "zenodo_file_id": retained_identity[2],
                "url": entry["links"]["content"],
                "readback_ordinal": ordinal,
                "match": True,
                "source": "retained_predecessor",
                "readback_mode": (
                    "zenodo_inherited_object_uuid_size_md5_no_redundant_download"
                ),
            }
            continue

        zip_path = scratch / f"{target_key}-readback-{ordinal:04d}.zip"
        identity = stream_public_file(
            anonymous,
            entry["links"]["content"],
            destination=zip_path if name.lower().endswith(".zip") else None,
        )
        if (
            identity["bytes"],
            identity["md5"],
            identity["sha256"],
        ) != (row["bytes"], row["md5"], row["sha256"]):
            raise RuntimeError(f"Public {target_key} bytes changed: {name}")
        if identity["md5"] != normalized_md5(entry["checksum"]):
            raise RuntimeError(f"Public {target_key} API checksum changed: {name}")
        outer[name] = {
            **identity,
            "url": entry["links"]["content"],
            "readback_ordinal": ordinal,
            "match": True,
            "source": "new_manifest_payload",
        }
        if name.lower().endswith(".zip"):
            zipped = zip_inventory(zip_path, include_members=True)
            zip_path.unlink()
            expected_zip = (
                row["zip_member_count"],
                row["zip_uncompressed_bytes"],
                row["zip_inventory_sha256"],
            )
            observed_zip = (
                zipped["member_count"],
                zipped["uncompressed_bytes"],
                zipped["inventory_sha256"],
            )
            if observed_zip != expected_zip:
                raise RuntimeError(f"Public {target_key} ZIP members changed: {name}")
            archives[name] = {
                **zipped,
                "readback_mode": "anonymous_zip_member_streaming_sha256",
                "match": True,
            }

    predecessor_public = load_modern_record(
        anonymous, registry["predecessor_record"]
    )
    if not predecessor_public.get("is_published"):
        raise RuntimeError(f"{target_key} predecessor is no longer public")
    draft_probe = authenticated.get(
        f"{API}/records/{record_id}/draft?expand=true",
        headers=auth_headers(token),
        timeout=(30, 180),
    )
    check(draft_probe, {404})
    policy = spec["_policies"][target_key]
    receipt = {
        "status": "PASS_PUBLIC_READBACK",
        "errors": [],
        "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "release_id": spec["release_id"],
        "release_spec_path": str(spec["_path"]),
        "release_spec_bytes": spec["_bytes"],
        "release_spec_sha256": spec["_sha256"],
        "target": target_key,
        "record_id": record_id,
        "record_url": record.get("links", {}).get("self_html"),
        "doi": public_version_doi(record),
        "concept_id": registry["concept_id"],
        "concept_doi": registry["concept_doi"],
        "predecessor_record": registry["predecessor_record"],
        "predecessor_guard": {
            "file_count": spec["_guards"][target_key]["file_count"],
            "total_bytes": spec["_guards"][target_key]["total_bytes"],
            "inventory_sha256": spec["_guards"][target_key][
                "inventory_sha256"
            ],
            "identity_method": "zenodo_inherited_object_uuid_size_md5",
        },
        "predecessor_preserved_published": True,
        "title_retained_exact": True,
        "rights_license_retained_exact": True,
        "access_retained_exact": True,
        "non_certifying_description_appended": True,
        "cross_links_appended": True,
        "upload_manifest": {
            "path": str(spec["_manifests"][target_key]["path"]),
            "bytes": spec["_manifests"][target_key]["bytes"],
            "sha256": spec["_manifests"][target_key]["sha256"],
            "file_count": len(spec["_manifests"][target_key]["files"]),
            "total_bytes": sum(
                int(row["bytes"])
                for row in spec["_manifests"][target_key]["files"]
            ),
            "inventory_sha256": inventory_digest(
                spec["_manifests"][target_key]["files"]
            ),
        },
        "file_policy": policy,
        "retained_predecessor_files_exact_zenodo_object_size_md5": (
            len(spec["_guards"][target_key]["files"])
            - len(policy["replace_names"])
        ),
        "outer_file_count": len(outer),
        "outer_total_bytes": sum(int(row["bytes"]) for row in outer.values()),
        "outer_file_readback": outer,
        "latest_record": int(latest["id"]),
        "active_draft_remaining": False,
        "published_record_draft_probe_status": draft_probe.status_code,
        "duplicate_concept_created": False,
        "parallel_draft_created": False,
    }
    zip_receipt = {
        "status": "PASS_ZIP_MEMBER_READBACK",
        "errors": [],
        "checked_at": receipt["checked_at"],
        "release_id": spec["release_id"],
        "release_spec_sha256": spec["_sha256"],
        "target": target_key,
        "record_id": record_id,
        "doi": public_version_doi(record),
        "concept_doi": registry["concept_doi"],
        "upload_manifest_sha256": spec["_manifests"][target_key]["sha256"],
        "zip_archive_count": len(archives),
        "zip_member_count": sum(int(row["member_count"]) for row in archives.values()),
        "zip_uncompressed_bytes": sum(
            int(row["uncompressed_bytes"]) for row in archives.values()
        ),
        "all_members_streamed_sha256": True,
        "archives": archives,
    }
    return receipt, zip_receipt


def write_target_receipts(
    spec: dict[str, Any],
    target_key: str,
    record_id: int,
    receipt: dict[str, Any],
    zip_receipt: dict[str, Any],
) -> tuple[Path, Path]:
    tag = safe_slug(str(spec["release_id"])).replace("-", "_")
    public_path = RECEIPT_ROOT / (
        f"20260802_{tag}_{target_key}_record_{record_id}_public_readback.json"
    )
    zip_path = RECEIPT_ROOT / (
        f"20260802_{tag}_{target_key}_record_{record_id}_zip_member_readback.json"
    )
    save_json_atomic(public_path, receipt)
    save_json_atomic(zip_path, zip_receipt)
    return public_path, zip_path


def predecessor_require_latest(
    state: dict[str, Any] | None, target_key: str
) -> bool:
    if state is None:
        return True
    return state["targets"][target_key]["status"] not in PUBLISHED_STATUSES


def run_preflight(spec: dict[str, Any]) -> dict[str, Any]:
    token = find_token()
    authenticated = make_session()
    anonymous = make_session()
    state = load_state(spec)
    scan = account_active_drafts(authenticated, token)
    assert_account_drafts_tracked(
        scan, state, allow_creation_recovery=True
    )
    predecessor_summary: dict[str, Any] = {}
    with tempfile.TemporaryDirectory(
        prefix=f"{safe_slug(spec['release_id'])}-preflight-"
    ) as temporary:
        scratch = Path(temporary)
        for target_key in TARGETS:
            record = verify_predecessor(
                authenticated,
                anonymous,
                target_key,
                spec,
                scratch,
                require_latest=predecessor_require_latest(state, target_key),
            )
            predecessor_summary[target_key] = {
                "record_id": int(record["id"]),
                "concept_doi": public_concept_doi(record),
                "file_count": spec["_guards"][target_key]["file_count"],
                "total_bytes": spec["_guards"][target_key]["total_bytes"],
                "inventory_sha256": spec["_guards"][target_key][
                    "inventory_sha256"
                ],
                "latest_guard_required": predecessor_require_latest(
                    state, target_key
                ),
            }
    return {
        "status": "PASS_PREFLIGHT_READ_ONLY",
        "errors": [],
        "release_id": spec["release_id"],
        "release_spec_path": str(spec["_path"]),
        "release_spec_bytes": spec["_bytes"],
        "release_spec_sha256": spec["_sha256"],
        "mode": "preflight",
        "remote_mutation": False,
        "state_path": str(state_path_for(spec)),
        "state_exists": state is not None,
        "control": {
            "path": str(spec["_control"]["path"]),
            "bytes": spec["_control"]["bytes"],
            "sha256": spec["_control"]["sha256"],
        },
        "dual_doi_provenance": spec["_dual_doi"],
        "account_wide_draft_scan": scan,
        "predecessors": predecessor_summary,
        "manifests": {
            key: {
                "path": str(value["path"]),
                "bytes": value["bytes"],
                "sha256": value["sha256"],
                "upload_file_count": len(value["files"]),
                "upload_total_bytes": sum(
                    int(row["bytes"]) for row in value["files"]
                ),
            }
            for key, value in spec["_manifests"].items()
        },
        "safe_publish_order": list(SAFE_PUBLISH_ORDER),
        "duplicate_concept_will_be_created": False,
    }


def load_all_predecessors(
    authenticated: requests.Session,
    anonymous: requests.Session,
    spec: dict[str, Any],
    state: dict[str, Any] | None,
    scratch: Path,
) -> dict[str, dict[str, Any]]:
    return {
        target_key: verify_predecessor(
            authenticated,
            anonymous,
            target_key,
            spec,
            scratch,
            require_latest=predecessor_require_latest(state, target_key),
        )
        for target_key in TARGETS
    }


def close_readback(
    authenticated: requests.Session,
    anonymous: requests.Session,
    token: str,
    spec: dict[str, Any],
    state: dict[str, Any],
    predecessors: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    results: dict[str, Any] = {}
    scratch_root = REPO_ROOT / "tmp" / "zenodo" / safe_slug(spec["release_id"])
    scratch_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=scratch_root) as temporary:
        scratch = Path(temporary)
        for target_key in SAFE_PUBLISH_ORDER:
            target_state = state["targets"][target_key]
            if target_state["status"] not in PUBLISHED_STATUSES:
                raise RuntimeError(
                    f"{target_key} has no published record for readback"
                )
            record_id = int(target_state["record_id"])
            receipt, zipped = readback_target(
                authenticated,
                anonymous,
                token,
                target_key,
                record_id,
                spec,
                predecessors[target_key],
                scratch,
            )
            public_path, zip_path = write_target_receipts(
                spec, target_key, record_id, receipt, zipped
            )
            target_state.update(
                {
                    "status": "CLOSED",
                    "public_readback_receipt": str(public_path),
                    "zip_member_readback_receipt": str(zip_path),
                    "readback_closed_at": receipt["checked_at"],
                }
            )
            save_state(spec, state)
            results[target_key] = {
                "record_id": record_id,
                "doi": receipt["doi"],
                "concept_doi": receipt["concept_doi"],
                "outer_file_count": receipt["outer_file_count"],
                "outer_total_bytes": receipt["outer_total_bytes"],
                "zip_archive_count": zipped["zip_archive_count"],
                "zip_member_count": zipped["zip_member_count"],
                "public_readback_receipt": str(public_path),
                "zip_member_readback_receipt": str(zip_path),
            }

    closure_scan = account_active_drafts(authenticated, token)
    for target_key, draft_ids in closure_scan["target_active_drafts"].items():
        if draft_ids:
            raise RuntimeError(
                f"Active {target_key} draft remains after publication: {draft_ids}"
            )
    tag = safe_slug(str(spec["release_id"])).replace("-", "_")
    summary_path = RECEIPT_ROOT / f"20260802_{tag}_four_concept_summary.json"
    summary = {
        "status": "PASS_FOUR_CONCEPT_PUBLICATION_AND_READBACK",
        "errors": [],
        "checked_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "release_id": spec["release_id"],
        "release_spec_path": str(spec["_path"]),
        "release_spec_bytes": spec["_bytes"],
        "release_spec_sha256": spec["_sha256"],
        "control_sha256": CONTROL_SHA256,
        "safe_publish_order": list(SAFE_PUBLISH_ORDER),
        "targets": results,
        "dual_doi_provenance": spec["_dual_doi"],
        "account_wide_draft_closure": closure_scan,
        "target_active_drafts_remaining": False,
        "duplicate_concept_created": False,
        "parallel_draft_created": False,
    }
    save_json_atomic(summary_path, summary)
    summary["summary_receipt"] = str(summary_path)
    return summary


def run_publish(spec: dict[str, Any]) -> dict[str, Any]:
    token = find_token()
    authenticated = make_session()
    anonymous = make_session()
    state = load_state(spec) or initial_state(spec)
    save_state(spec, state)
    initial_scan = account_active_drafts(authenticated, token)
    assert_account_drafts_tracked(
        initial_scan, state, allow_creation_recovery=True
    )
    scratch_root = REPO_ROOT / "tmp" / "zenodo" / safe_slug(spec["release_id"])
    scratch_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=scratch_root) as temporary:
        predecessors = load_all_predecessors(
            authenticated, anonymous, spec, state, Path(temporary)
        )

    # Transaction preparation: every target is staged and validated before the
    # first irreversible publish call.
    for target_key in SAFE_PUBLISH_ORDER:
        target_state = state["targets"][target_key]
        if target_state["status"] in PUBLISHED_STATUSES:
            continue
        draft_id = create_or_resume_draft(
            authenticated,
            token,
            target_key,
            spec,
            state,
            predecessors[target_key],
        )
        stage_target(
            authenticated,
            token,
            target_key,
            spec,
            state,
            predecessors[target_key],
            draft_id,
        )

    staged_scan = account_active_drafts(authenticated, token)
    assert_account_drafts_tracked(
        staged_scan, state, allow_creation_recovery=False
    )
    for target_key in SAFE_PUBLISH_ORDER:
        if state["targets"][target_key]["status"] in PUBLISHED_STATUSES:
            continue
        verify_staged_target(
            authenticated,
            token,
            target_key,
            spec,
            predecessors[target_key],
            int(state["targets"][target_key]["draft_id"]),
        )

    for target_key in SAFE_PUBLISH_ORDER:
        before_publish_scan = account_active_drafts(authenticated, token)
        assert_account_drafts_tracked(
            before_publish_scan, state, allow_creation_recovery=False
        )
        publish_target(
            authenticated,
            token,
            target_key,
            spec,
            state,
            predecessors[target_key],
        )
    return close_readback(
        authenticated, anonymous, token, spec, state, predecessors
    )


def run_readback_only(spec: dict[str, Any]) -> dict[str, Any]:
    token = find_token()
    authenticated = make_session()
    anonymous = make_session()
    state = load_state(spec)
    if state is None:
        raise RuntimeError("--readback-only requires tracked published state")
    for target_key in TARGETS:
        if state["targets"][target_key]["status"] not in PUBLISHED_STATUSES:
            raise RuntimeError(
                f"--readback-only has no published {target_key} record"
            )
    scan = account_active_drafts(authenticated, token)
    assert_account_drafts_tracked(scan, state, allow_creation_recovery=False)
    scratch_root = REPO_ROOT / "tmp" / "zenodo" / safe_slug(spec["release_id"])
    scratch_root.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=scratch_root) as temporary:
        predecessors = load_all_predecessors(
            authenticated, anonymous, spec, state, Path(temporary)
        )
    return close_readback(
        authenticated, anonymous, token, spec, state, predecessors
    )


def clean_for_output(value: Any) -> Any:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {
            key: clean_for_output(item)
            for key, item in value.items()
            if not str(key).startswith("_") and key not in {"by_name"}
        }
    if isinstance(value, list):
        return [clean_for_output(item) for item in value]
    return value


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Guarded add-first Zenodo successor publisher for FAC/GAGA, EGA, "
            "methodology, and replication concepts. Defaults to read-only preflight."
        )
    )
    parser.add_argument(
        "--release-spec",
        type=Path,
        required=True,
        help="immutable JSON release specification",
    )
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument(
        "--preflight",
        action="store_true",
        help="read-only local, predecessor, and account-wide draft verification (default)",
    )
    modes.add_argument(
        "--publish",
        action="store_true",
        help="stage and publish all four tracked same-concept successors",
    )
    modes.add_argument(
        "--readback-only",
        action="store_true",
        help="perform anonymous readback for already published tracked records",
    )
    args = parser.parse_args()
    spec_path = args.release_spec.resolve()
    if not spec_path.is_file():
        parser.error(f"release specification does not exist: {spec_path}")
    spec = load_release_spec(spec_path)
    if args.publish:
        result = run_publish(spec)
    elif args.readback_only:
        result = run_readback_only(spec)
    else:
        result = run_preflight(spec)
    print(json.dumps(clean_for_output(result), ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
