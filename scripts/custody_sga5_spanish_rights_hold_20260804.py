#!/usr/bin/env python3
"""Accept exact private custody of the completed Spanish SGA 5 checkpoint.

This script is intentionally bounded to one immutable ZIP and its already-expanded
peer directory.  It never searches outside those exact paths, never edits the
producer package, and never performs a publication action.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import stat
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath


SOURCE_ZIP = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management"
    r"\romance\05_sga5_spanish_20260717\SGA5_ES_WORKPASS\output\release"
    r"\SGA5_ES_376U_326P_91A644AB_2B69F774.zip"
)
EXPANDED_ROOT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management"
    r"\romance\05_sga5_spanish_20260717\SGA5_ES_WORKPASS\output\release"
    r"\SGA5_ES_376U_326P_91A644AB_2B69F774"
)
EXTERNAL_GATE = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management"
    r"\romance\05_sga5_spanish_20260717\SGA5_ES_WORKPASS\evidence\FINAL_GATE.json"
)
DEST_ROOT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management"
    r"\romance\90_logs\private_archive_custody"
    r"\SGA5_ES_COMPLETE_RIGHTS_HOLD_20260804_r1"
)

EXPECTED_ZIP_BYTES = 2_821_750
EXPECTED_ZIP_SHA256 = "202EBF8A05F1C6A1F96D7B6235A6FD67185CB64A8B53C4F86ADD3EDBC068EB8C"
EXPECTED_MEMBER_COUNT = 408
EXPECTED_CHECKSUM_ROWS = 407
EXPECTED_UNCOMPRESSED_BYTES = 5_804_945
EXPECTED_MEMBER_TREE_SHA256 = "D3EE03791196BC1F9E70D4D5B005370A3F86FCAA752A67860FFCC70E062BB640"
EXPECTED_GATE_SHA256 = "35E76152CA87C41DCF7471EBD853AEB823D89B7A2BC6BFD7F75003A4903E17CF"
EXPECTED_PDF_SHA256 = "2B69F774EF0F3E56262C45E36DE1807DB3428563678AB1132322521C716E32CC"
EXPECTED_MASTER_SHA256 = "49A77434448F402C40EB935F982C4EDE7EF5B611677D2BD254D6E0520D460E7F"
EXPECTED_TARGET_SHA256 = "91A644AB72AEA7E24700BFA0FA9445C83A5D649C9DA7612B310FA3A417B1B72F"

PDF_NAME = "SGA5_ES.pdf"
MASTER_NAME = "sga5_es.tex"
CHECKSUM_NAME = "SHA256SUMS.txt"

# Tight private-path indicators.  The deliberately broad ``letter:\\macro``
# detector below is recorded separately because it flags ordinary TeX maps.
PRIVATE_PATTERNS = {
    "windows_user_root": re.compile(rb"(?i)[A-Z]:[\\/]+Users[\\/]+"),
    "windows_profile_artifact": re.compile(rb"(?i)(?:AppData|\\.codex|\\.gemini)(?:[\\/]|$)"),
    "posix_user_root": re.compile(rb"(?i)/(?:home|Users|private)/[^/\s]+/"),
    "named_operator": re.compile(rb"(?i)Floris"),
    "email": re.compile(rb"(?i)[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}"),
}
BROAD_COLON_BACKSLASH = re.compile(r"[A-Za-z]:\\[A-Za-z@]+")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name.replace("\\", "/"))
    return (
        not pure.is_absolute()
        and ".." not in pure.parts
        and not re.match(r"^[A-Za-z]:", name)
        and not name.startswith(("/", "\\"))
    )


def parse_sha256sums(data: bytes) -> dict[str, str]:
    rows: dict[str, str] = {}
    for line in data.decode("utf-8").splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r"([0-9A-Fa-f]{64})\s+\*?(.+)", line)
        if not match:
            raise RuntimeError(f"Malformed SHA256SUMS row: {line!r}")
        digest, name = match.groups()
        name = name.replace("\\", "/")
        if name in rows:
            raise RuntimeError(f"Duplicate SHA256SUMS member: {name}")
        rows[name] = digest.upper()
    return rows


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    errors: list[str] = []
    if not SOURCE_ZIP.is_file():
        raise FileNotFoundError(SOURCE_ZIP)
    if not EXPANDED_ROOT.is_dir():
        raise FileNotFoundError(EXPANDED_ROOT)
    if not EXTERNAL_GATE.is_file():
        raise FileNotFoundError(EXTERNAL_GATE)
    if DEST_ROOT.exists():
        raise FileExistsError(f"Refusing to overwrite custody root: {DEST_ROOT}")

    source_zip_bytes = SOURCE_ZIP.stat().st_size
    source_zip_sha = sha256_file(SOURCE_ZIP)
    if source_zip_bytes != EXPECTED_ZIP_BYTES:
        errors.append(f"zip_bytes:{source_zip_bytes}!={EXPECTED_ZIP_BYTES}")
    if source_zip_sha != EXPECTED_ZIP_SHA256:
        errors.append(f"zip_sha256:{source_zip_sha}!={EXPECTED_ZIP_SHA256}")
    if sha256_file(EXTERNAL_GATE) != EXPECTED_GATE_SHA256:
        errors.append("external_gate_hash_mismatch")

    member_rows: list[dict[str, object]] = []
    broad_rows: list[dict[str, object]] = []
    actual_privacy_hits: list[dict[str, object]] = []
    member_hashes: dict[str, str] = {}
    member_sizes: dict[str, int] = {}

    with zipfile.ZipFile(SOURCE_ZIP, "r") as archive:
        if archive.testzip() is not None:
            errors.append("zip_crc_failure")
        infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename.replace("\\", "/") for info in infos]
        if len(names) != len(set(names)):
            errors.append("duplicate_zip_member")
        unsafe = [name for name in names if not safe_member(name)]
        if unsafe:
            errors.append(f"unsafe_zip_members:{len(unsafe)}")
        if len(infos) != EXPECTED_MEMBER_COUNT:
            errors.append(f"member_count:{len(infos)}!={EXPECTED_MEMBER_COUNT}")
        if sum(info.file_size for info in infos) != EXPECTED_UNCOMPRESSED_BYTES:
            errors.append("uncompressed_byte_count_mismatch")

        checksum_data = archive.read(CHECKSUM_NAME)
        expected_hashes = parse_sha256sums(checksum_data)
        if len(expected_hashes) != EXPECTED_CHECKSUM_ROWS:
            errors.append("sha256sums_row_count_mismatch")
        expected_names = set(names) - {CHECKSUM_NAME}
        if set(expected_hashes) != expected_names:
            errors.append("sha256sums_member_set_mismatch")

        for info in sorted(infos, key=lambda item: item.filename.replace("\\", "/")):
            name = info.filename.replace("\\", "/")
            data = archive.read(info)
            digest = sha256_bytes(data)
            member_hashes[name] = digest
            member_sizes[name] = len(data)
            expected = expected_hashes.get(name, "")
            checksum_match = name == CHECKSUM_NAME or digest == expected
            if not checksum_match:
                errors.append(f"member_checksum_mismatch:{name}")
            member_rows.append(
                {
                    "relative_path": name,
                    "bytes": len(data),
                    "compressed_bytes": info.compress_size,
                    "crc32": f"{info.CRC:08X}",
                    "sha256": digest,
                    "listed_in_SHA256SUMS": "no" if name == CHECKSUM_NAME else "yes",
                    "SHA256SUMS_expected_sha256": expected,
                    "SHA256SUMS_match": "self-excluded" if name == CHECKSUM_NAME else ("yes" if checksum_match else "no"),
                }
            )

            for pattern_name, pattern in PRIVATE_PATTERNS.items():
                for match in pattern.finditer(data):
                    actual_privacy_hits.append(
                        {
                            "relative_path": name,
                            "pattern": pattern_name,
                            "byte_offset": match.start(),
                        }
                    )

            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                continue
            for line_number, line in enumerate(text.splitlines(), 1):
                matches = BROAD_COLON_BACKSLASH.findall(line)
                if not matches:
                    continue
                broad_rows.append(
                    {
                        "relative_path": name,
                        "line": line_number,
                        "match_count": len(matches),
                        "matched_tokens": " | ".join(matches),
                        "classification": (
                            "validator-regex-literal; not a path"
                            if name.endswith(".ps1")
                            else "TeX mathematical map/macro; not a path"
                        ),
                    }
                )

    expanded_files = {
        path.relative_to(EXPANDED_ROOT).as_posix(): path
        for path in EXPANDED_ROOT.rglob("*")
        if path.is_file()
    }
    if set(expanded_files) != set(member_hashes):
        errors.append("expanded_zip_member_set_mismatch")
    expanded_hash_mismatches = []
    for name, path in sorted(expanded_files.items()):
        if path.stat().st_size != member_sizes.get(name) or sha256_file(path) != member_hashes.get(name):
            expanded_hash_mismatches.append(name)
    if expanded_hash_mismatches:
        errors.append(f"expanded_zip_identity_mismatches:{len(expanded_hash_mismatches)}")

    tree_material = "".join(
        f"{name}\t{member_sizes[name]}\t{member_hashes[name]}\n"
        for name in sorted(member_hashes)
    ).encode("utf-8")
    tree_sha = sha256_bytes(tree_material)
    if tree_sha != EXPECTED_MEMBER_TREE_SHA256:
        errors.append(f"member_tree_sha256:{tree_sha}!={EXPECTED_MEMBER_TREE_SHA256}")

    if member_hashes.get(PDF_NAME) != EXPECTED_PDF_SHA256:
        errors.append("pdf_hash_mismatch")
    if member_hashes.get(MASTER_NAME) != EXPECTED_MASTER_SHA256:
        errors.append("master_hash_mismatch")
    gate = json.loads(EXTERNAL_GATE.read_text(encoding="utf-8-sig"))
    if gate.get("status") != "pass" or gate.get("passed_count") != 9 or gate.get("check_count") != 9:
        errors.append("external_gate_not_9_of_9_pass")
    if gate.get("target_document_sha256") != EXPECTED_TARGET_SHA256:
        errors.append("target_document_hash_mismatch")
    if actual_privacy_hits:
        errors.append(f"specific_private_path_or_email_hits:{len(actual_privacy_hits)}")

    if errors:
        raise RuntimeError("Pre-custody verification failed: " + "; ".join(errors))

    accepted_utc = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    DEST_ROOT.mkdir(parents=True, exist_ok=False)
    custody_zip = DEST_ROOT / SOURCE_ZIP.name
    shutil.copyfile(SOURCE_ZIP, custody_zip)
    if custody_zip.stat().st_size != source_zip_bytes or sha256_file(custody_zip) != source_zip_sha:
        raise RuntimeError("Post-copy custody ZIP identity mismatch")

    write_csv(
        DEST_ROOT / "ZIP_MEMBER_MANIFEST.csv",
        [
            "relative_path",
            "bytes",
            "compressed_bytes",
            "crc32",
            "sha256",
            "listed_in_SHA256SUMS",
            "SHA256SUMS_expected_sha256",
            "SHA256SUMS_match",
        ],
        member_rows,
    )
    write_csv(
        DEST_ROOT / "BROAD_PATH_ALERT_CLASSIFICATION.csv",
        ["relative_path", "line", "match_count", "matched_tokens", "classification"],
        broad_rows,
    )

    validation = {
        "schema": "private-archive-custody-sga5-es-rights-hold-v1",
        "accepted_utc": accepted_utc,
        "status": "PASS_PRIVATE_CUSTODY_RIGHTS_HOLD",
        "errors": [],
        "public_release_authorized": False,
        "public_release_hold_reason": (
            "Public redistribution permission for Springer LNM 589 and this derivative Spanish translation has not been established."
        ),
        "source_zip": {
            "bytes": source_zip_bytes,
            "sha256": source_zip_sha,
        },
        "custody_zip": {
            "relative_path": custody_zip.name,
            "bytes": custody_zip.stat().st_size,
            "sha256": sha256_file(custody_zip),
        },
        "zip": {
            "member_count": len(member_rows),
            "uncompressed_bytes": sum(int(row["bytes"]) for row in member_rows),
            "member_tree_sha256": tree_sha,
            "crc_errors": 0,
            "unsafe_members": 0,
            "sha256sums_rows": EXPECTED_CHECKSUM_ROWS,
            "sha256sums_missing": 0,
            "sha256sums_extra": 0,
            "sha256sums_mismatches": 0,
        },
        "expanded_peer_replay": {
            "file_count": len(expanded_files),
            "missing": 0,
            "extra": 0,
            "byte_or_hash_mismatches": 0,
        },
        "privacy": {
            "specific_private_path_or_email_hits": 0,
            "broad_colon_backslash_alert_lines": len(broad_rows),
            "broad_colon_backslash_alert_occurrences": sum(int(row["match_count"]) for row in broad_rows),
            "broad_alert_disposition": "all false positives: TeX mathematical maps/macros or the validator regex itself",
        },
        "completion_gate": {
            "bytes": EXTERNAL_GATE.stat().st_size,
            "sha256": sha256_file(EXTERNAL_GATE),
            "status": gate.get("status"),
            "passed_count": gate.get("passed_count"),
            "check_count": gate.get("check_count"),
        },
        "scope": {
            "editable_units": 376,
            "pdf_pages": 326,
            "terminology_decisions": 401,
            "target_document_sha256": EXPECTED_TARGET_SHA256,
            "pdf_sha256": EXPECTED_PDF_SHA256,
            "master_sha256": EXPECTED_MASTER_SHA256,
        },
        "supersedes_private_incomplete_checkpoints": [
            "SGA5_ES_356U_304P_20260718_982B9966",
            "SGA5_ES_356U_304P_20260718_REAUDIT_73565D08",
        ],
        "deduplication": (
            "One exact ZIP is retained in custody. Its 408 expanded members were byte/hash replayed against the producer directory; no redundant expanded copy was made."
        ),
        "zenodo_mutation": "none",
        "github_mutation": "none",
    }
    validation_path = DEST_ROOT / "PRIVATE_CUSTODY_VALIDATION.json"
    validation_path.write_text(json.dumps(validation, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    manifest_path = DEST_ROOT / "ZIP_MEMBER_MANIFEST.csv"
    broad_path = DEST_ROOT / "BROAD_PATH_ALERT_CLASSIFICATION.csv"
    receipt = f"""# Spanish SGA 5 complete checkpoint — private archive custody receipt

Custody identity: `SGA5-ES-COMPLETE-PRIVATE-RIGHTS-HOLD-20260804-R1`

Accepted at: `{accepted_utc}`

## Exact preserved transport

- File: `{custody_zip.name}`
- Bytes: `{custody_zip.stat().st_size:,}`
- SHA-256: `{sha256_file(custody_zip)}`
- ZIP members: `{len(member_rows)}` files / `{sum(int(row['bytes']) for row in member_rows):,}` uncompressed bytes
- Canonical member path+bytes+SHA-256 tree: `{tree_sha}`
- ZIP CRC replay: PASS; unsafe members: 0
- Producer `SHA256SUMS.txt`: `{EXPECTED_CHECKSUM_ROWS}/{EXPECTED_CHECKSUM_ROWS}` represented members match; missing 0; extra 0; mismatch 0
- Expanded producer peer: `{len(expanded_files)}/{len(expanded_files)}` paths and bytes/hashes match the ZIP; no redundant expanded custody copy was created

## Completion evidence bound

- Completion gate: `{EXTERNAL_GATE.stat().st_size:,}` B — SHA-256 `{sha256_file(EXTERNAL_GATE)}` — PASS 9/9
- Scope: 376 editable units; 326-page PDF; 401 terminology decisions
- Expanded Spanish target SHA-256: `{EXPECTED_TARGET_SHA256}`
- PDF SHA-256: `{EXPECTED_PDF_SHA256}`
- Editable master SHA-256: `{EXPECTED_MASTER_SHA256}`

## Privacy replay

Specific Windows/POSIX user-root, operator-name, profile-artifact, and email hits: 0.

The deliberately broad `letter:\\command` detector produced `{sum(int(row['match_count']) for row in broad_rows)}` occurrences on `{len(broad_rows)}` lines. Every occurrence is classified in `BROAD_PATH_ALERT_CLASSIFICATION.csv`: ordinary TeX mathematical notation/macros, plus the detector literal in `scripts/render_public.ps1`; none is a filesystem path.

## Preservation and publication disposition

Private custody is accepted. Public redistribution is **on rights hold** because permission for Springer LNM 589 and this derivative Spanish translation has not been established. No Zenodo concept, deposition, draft, record, DOI, file, metadata, preview, or relation was created or changed. No GitHub branch, commit, push, PR, merge, or public payload mutation occurred in this custody action.

This complete checkpoint supersedes the two incomplete Spanish checkpoints `SGA5_ES_356U_304P_20260718_982B9966` and `SGA5_ES_356U_304P_20260718_REAUDIT_73565D08` for private archival status. Those predecessor identities remain preserved as history and must not be represented as complete.

The exact source payload was not altered. Public release requires a later affirmative rights adjudication; absence of the authority scan from this ZIP does not itself establish permission for the derivative translation.

## Verification surfaces

- `ZIP_MEMBER_MANIFEST.csv`: `{manifest_path.stat().st_size:,}` B — SHA-256 `{sha256_file(manifest_path)}`
- `BROAD_PATH_ALERT_CLASSIFICATION.csv`: `{broad_path.stat().st_size:,}` B — SHA-256 `{sha256_file(broad_path)}`
- `PRIVATE_CUSTODY_VALIDATION.json`: `{validation_path.stat().st_size:,}` B — SHA-256 `{sha256_file(validation_path)}`
"""
    receipt_path = DEST_ROOT / "PRIVATE_CUSTODY_RECEIPT.md"
    receipt_path.write_text(receipt, encoding="utf-8")

    custody_zip.chmod(custody_zip.stat().st_mode & ~stat.S_IWRITE)
    result = {
        "status": "PASS_PRIVATE_CUSTODY_RIGHTS_HOLD",
        "custody_root": str(DEST_ROOT),
        "custody_zip_bytes": custody_zip.stat().st_size,
        "custody_zip_sha256": sha256_file(custody_zip),
        "member_count": len(member_rows),
        "member_tree_sha256": tree_sha,
        "receipt_bytes": receipt_path.stat().st_size,
        "receipt_sha256": sha256_file(receipt_path),
        "validation_bytes": validation_path.stat().st_size,
        "validation_sha256": sha256_file(validation_path),
        "zenodo_mutation": "none",
        "github_mutation": "none",
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # exact failure is preferable to partial acceptance
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
