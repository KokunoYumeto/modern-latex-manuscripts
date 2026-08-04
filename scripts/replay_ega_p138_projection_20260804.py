#!/usr/bin/env python3
"""Independently replay the sealed EGA I p.138 custody/public projection.

This validator does not import the builder.  It re-hashes both trees, checks
manifest closure, replays every ZIP member, verifies the direct-upload table,
and repeats the bounded privacy/rights-routing gates.  It is read-only except
for the explicitly requested JSON receipt path.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import zipfile
from pathlib import Path, PurePosixPath


REPO = Path(__file__).resolve().parents[1]
PRIVATE_ROOT = Path(
    r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management"
    r"\english_germanic\90_logs\private_archive_custody"
    r"\EGA_I_P138_R61_R82_PRIVATE_RAW_CUSTODY_20260804_r1"
)
PUBLIC_ROOT = (
    REPO / "sources/ega/checkpoints/ega1-p138-diplomatic-prestacks-r1-20260804"
)

PRIVATE_MANIFEST = "PRIVATE_CUSTODY_MANIFEST.csv"
PRIVATE_VALIDATION = "PRIVATE_CUSTODY_VALIDATION.json"
PAYLOAD_MANIFEST = "13_PACKAGE_PAYLOAD_MANIFEST.csv"
UPLOAD_MANIFEST = "14_ZENODO_UPLOAD_MANIFEST.csv"
PACKAGE_VALIDATION = "15_PACKAGE_VALIDATION.json"
ZIP_NAME = "00_EGA_I_P138_Diplomatic_French_Paired_English_PreStacks_Source.zip"

EXPECTED_PRIVATE = {
    "files_total": 170,
    "bytes_total": 10_259_154,
    "manifest_rows": 168,
    "tree_sha256": "38ED77EABA204E580BD58550BAB2CBF95051A6F60FA77C0C64E7A475E4236C97",
}
EXPECTED_PUBLIC = {
    "files_total": 175,
    "bytes_total": 13_720_244,
    "payload_rows": 171,
    "tree_sha256": "DF373A02B067560A4EE73E2FE51B82404F3A9AE484C2DAB450C13BBF7D932428",
    "zip_members": 172,
    "zip_bytes": 3_258_568,
    "zip_sha256": "88483F26DCB88420718C2DCEC114998F84B23ED9A0F4A1A1ABF12BE28F3700D7",
    "upload_rows": 17,
}
EXPECTED_CONCEPTS = {
    "ega_concept": "10.5281/zenodo.20414353",
    "methodology_concept": "10.5281/zenodo.21124403",
    "replication_concept": "10.5281/zenodo.20461174",
}
EXPECTED_PRIVATE_IDENTITIES = {
    PRIVATE_MANIFEST: (19_580, "C4E69B82A235C4248B7FC9F508BD58BAB9296F9B4D90631D357EA9A8A3CB8F3A"),
    PRIVATE_VALIDATION: (1_011, "497D48AEB6A3569631F869D8A540A834D6C98411D27ABCD27A267B6C7F4C3181"),
}
EXPECTED_PUBLIC_IDENTITIES = {
    PAYLOAD_MANIFEST: (19_934, "83E97F153B0A6505B83E7E765EA39DCB6D6034F92B2A46DA9CA00FF3E3160595"),
    UPLOAD_MANIFEST: (3_410, "199CCA91B32544C9E3F33C74AA08681A45409EF99C380048E437DA3286CEE5E2"),
    PACKAGE_VALIDATION: (79_354, "E010E33952912E300DC24293BB807B3DE1B5A2ED4602A8435A132C8F27AC10E6"),
    ZIP_NAME: (3_258_568, "88483F26DCB88420718C2DCEC114998F84B23ED9A0F4A1A1ABF12BE28F3700D7"),
}

TEXT_SUFFIXES = {
    ".aux", ".bib", ".cfg", ".cls", ".csv", ".json", ".jsonl",
    ".log", ".md", ".out", ".ps1", ".py", ".sty", ".tex", ".txt",
    ".yaml", ".yml",
}
USER_HOME = re.compile(
    r"(?i)(?:[A-Za-z]:[\\/]Users[\\/][^\\/\s\"']+|/(?:Users|home)/[^/\s\"']+)"
)
TASK_ID = re.compile(
    r"(?i)019[0-9a-f]{5}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
)
EMAIL = re.compile(r"(?i)(?<!@)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
SECRET = re.compile(
    r"(?i)(?:access[_-]?token|api[_-]?key|github[_-]?token)\s*[:=]\s*[\"'][A-Za-z0-9_\-]{16,}"
)
PUBLIC_TOOLCHAIN_EMAIL = "krisrose@tug.org"
MANDATED_CONTROL = "controls/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
PUBLIC_OPERATOR_NAME_COUNTS = {
    # These are explicit human-readable governance/provenance attributions,
    # not leaked paths or account identifiers.  The first file is also the
    # mandated byte-exact BFA1E3A3... control and cannot be rewritten.
    MANDATED_CONTROL: 1,
    "controls/SUCCESSOR_SESSION_BOOTSTRAP_AND_LOGBOOK_PROTOCOL_20260803.md": 2,
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, sha256_path(path)


def list_files(root: Path) -> list[Path]:
    return sorted(
        (path for path in root.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(root).as_posix(),
    )


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def canonical_tree(rows: list[dict[str, object]]) -> str:
    payload = "".join(
        f"{row['relative_path']}\t{row['bytes']}\t{row['sha256']}\n"
        for row in sorted(rows, key=lambda item: str(item["relative_path"]))
    ).encode("utf-8")
    return sha256_bytes(payload)


def replay_manifest(
    root: Path,
    rows: list[dict[str, str]],
    excluded_names: set[str],
) -> dict[str, object]:
    errors: list[dict[str, object]] = []
    names = [row["relative_path"] for row in rows]
    if len(names) != len(set(names)):
        errors.append({"error": "duplicate_manifest_paths"})
    represented = set(names)
    actual = {
        path.relative_to(root).as_posix()
        for path in list_files(root)
        if path.relative_to(root).as_posix() not in excluded_names
    }
    missing = sorted(represented - actual)
    extra = sorted(actual - represented)
    if missing:
        errors.append({"error": "missing_files", "paths": missing})
    if extra:
        errors.append({"error": "extra_files", "paths": extra})
    observed_rows: list[dict[str, object]] = []
    for row in rows:
        path = root / PurePosixPath(row["relative_path"])
        if not path.is_file():
            continue
        observed = identity(path)
        wanted = int(row["bytes"]), row["sha256"].upper()
        if observed != wanted:
            errors.append(
                {
                    "error": "identity_mismatch",
                    "relative_path": row["relative_path"],
                    "wanted_bytes": wanted[0],
                    "wanted_sha256": wanted[1],
                    "observed_bytes": observed[0],
                    "observed_sha256": observed[1],
                }
            )
        observed_rows.append(
            {
                "relative_path": row["relative_path"],
                "bytes": observed[0],
                "sha256": observed[1],
            }
        )
    return {
        "rows": len(rows),
        "represented_bytes": sum(int(row["bytes"]) for row in rows),
        "canonical_tree_sha256": canonical_tree(observed_rows),
        "missing": len(missing),
        "extra": len(extra),
        "identity_mismatches": sum(
            1 for item in errors if item.get("error") == "identity_mismatch"
        ),
        "errors": errors,
    }


def safe_zip_name(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        bool(name)
        and "\\" not in name
        and not name.startswith("/")
        and not re.match(r"^[A-Za-z]:", name)
        and not pure.is_absolute()
        and all(part not in {"", ".", ".."} for part in pure.parts)
    )


def replay_zip(root: Path, payload_rows: list[dict[str, str]]) -> dict[str, object]:
    zip_path = root / ZIP_NAME
    errors: list[dict[str, object]] = []
    expected_names = sorted(
        [row["relative_path"] for row in payload_rows] + [PAYLOAD_MANIFEST]
    )
    member_bytes = 0
    with zipfile.ZipFile(zip_path, "r") as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        if names != expected_names:
            errors.append({"error": "zip_member_order_or_set_mismatch"})
        if len(names) != len(set(names)):
            errors.append({"error": "duplicate_zip_member"})
        unsafe = sorted(name for name in names if not safe_zip_name(name))
        if unsafe:
            errors.append({"error": "unsafe_zip_member", "paths": unsafe})
        bad_crc = archive.testzip()
        if bad_crc is not None:
            errors.append({"error": "zip_crc_failure", "path": bad_crc})
        for info in infos:
            data = archive.read(info)
            member_bytes += len(data)
            local = root / PurePosixPath(info.filename)
            if not local.is_file():
                errors.append({"error": "zip_member_without_local_peer", "path": info.filename})
                continue
            wanted = identity(local)
            observed = len(data), sha256_bytes(data)
            if observed != wanted:
                errors.append(
                    {
                        "error": "zip_member_identity_mismatch",
                        "path": info.filename,
                    }
                )
    return {
        "zip_bytes": zip_path.stat().st_size,
        "zip_sha256": sha256_path(zip_path),
        "members": len(expected_names),
        "uncompressed_member_bytes": member_bytes,
        "unsafe_members": sum(
            1 for item in errors if item.get("error") == "unsafe_zip_member"
        ),
        "identity_mismatches": sum(
            1 for item in errors if item.get("error") == "zip_member_identity_mismatch"
        ),
        "errors": errors,
    }


def replay_uploads(root: Path) -> dict[str, object]:
    rows = read_manifest(root / UPLOAD_MANIFEST)
    errors: list[dict[str, object]] = []
    names = [row["relative_path"] for row in rows]
    if len(names) != len(set(names)):
        errors.append({"error": "duplicate_upload_name"})
    for row in rows:
        path = root / PurePosixPath(row["relative_path"])
        if not path.is_file():
            errors.append({"error": "missing_upload_object", "path": row["relative_path"]})
            continue
        observed = identity(path)
        wanted = int(row["bytes"]), row["sha256"].upper()
        if observed != wanted:
            errors.append({"error": "upload_identity_mismatch", "path": row["relative_path"]})
        for key, value in EXPECTED_CONCEPTS.items():
            if row.get(key) != value:
                errors.append({"error": "upload_routing_mismatch", "path": row["relative_path"], "field": key})
        if row.get("direct_public", "").lower() != "true":
            errors.append({"error": "upload_not_direct_public", "path": row["relative_path"]})
    return {
        "rows": len(rows),
        "objects_bytes": sum(int(row["bytes"]) for row in rows),
        "names": names,
        "errors": errors,
    }


def privacy_replay(root: Path) -> dict[str, object]:
    errors: list[dict[str, object]] = []
    task_occurrences = 0
    toolchain_occurrences = 0
    public_operator_name_occurrences = 0
    text_files = 0
    binary_files = 0
    binary_needles = (
        b"C:\\Users\\",
        b"C:/Users/",
        b"Floris",
        b".codex",
        b"memo_lepthy@live.nl",
    )
    for path in list_files(root):
        rel = path.relative_to(root).as_posix()
        if rel == ZIP_NAME:
            continue
        data = path.read_bytes()
        if path.suffix.lower() in TEXT_SUFFIXES:
            text_files += 1
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                errors.append({"error": "non_utf8_text_surface", "path": rel})
                continue
            if USER_HOME.search(text):
                errors.append({"error": "private_user_home", "path": rel})
            if re.search(r"(?i)(?:^|[\\/])\.codex(?:[\\/]|$)", text):
                errors.append({"error": "private_codex_state", "path": rel})
            operator_name_count = len(re.findall(r"(?i)\bFloris\b", text))
            if operator_name_count:
                wanted_name_count = PUBLIC_OPERATOR_NAME_COUNTS.get(rel)
                if operator_name_count == wanted_name_count:
                    public_operator_name_occurrences += operator_name_count
                else:
                    errors.append(
                        {
                            "error": "unapproved_operator_name",
                            "path": rel,
                            "observed": operator_name_count,
                            "expected_public_provenance_count": wanted_name_count or 0,
                        }
                    )
            if SECRET.search(text):
                errors.append({"error": "hardcoded_secret_pattern", "path": rel})
            hits = TASK_ID.findall(text)
            if hits:
                if rel == MANDATED_CONTROL:
                    task_occurrences += len(hits)
                else:
                    errors.append({"error": "internal_task_id", "path": rel, "count": len(hits)})
            for address in EMAIL.findall(text):
                if address.lower() == PUBLIC_TOOLCHAIN_EMAIL:
                    toolchain_occurrences += 1
                else:
                    errors.append(
                        {
                            "error": "unapproved_email",
                            "path": rel,
                            "email_sha256": sha256_bytes(address.lower().encode("utf-8")),
                        }
                    )
        else:
            binary_files += 1
            lowered = data.lower()
            for needle in binary_needles:
                if needle.lower() in lowered:
                    errors.append(
                        {
                            "error": "binary_private_needle",
                            "path": rel,
                            "needle_sha256": sha256_bytes(needle.lower()),
                        }
                    )
                utf16 = needle.decode("ascii").encode("utf-16le").lower()
                if utf16 in lowered:
                    errors.append(
                        {
                            "error": "binary_private_needle_utf16le",
                            "path": rel,
                            "needle_sha256": sha256_bytes(needle.lower()),
                        }
                    )
    if task_occurrences != 3:
        errors.append({"error": "mandated_control_task_id_count", "observed": task_occurrences, "expected": 3})
    if toolchain_occurrences != 2:
        errors.append({"error": "public_toolchain_email_count", "observed": toolchain_occurrences, "expected": 2})
    expected_public_name_count = sum(PUBLIC_OPERATOR_NAME_COUNTS.values())
    if public_operator_name_occurrences != expected_public_name_count:
        errors.append(
            {
                "error": "public_operator_provenance_name_count",
                "observed": public_operator_name_occurrences,
                "expected": expected_public_name_count,
            }
        )
    forbidden_name_fragments = ("fac", "gaga")
    forbidden_names = [
        path.relative_to(root).as_posix()
        for path in list_files(root)
        if any(fragment in path.name.lower() for fragment in forbidden_name_fragments)
    ]
    if forbidden_names:
        errors.append({"error": "cross_corpus_filename", "paths": forbidden_names})
    return {
        "text_files_scanned": text_files,
        "binary_files_scanned": binary_files,
        "zip_scanned_by_member_replay": True,
        "mandated_control_task_id_occurrences": task_occurrences,
        "public_toolchain_email_occurrences": toolchain_occurrences,
        "authorized_public_operator_provenance_name_occurrences": public_operator_name_occurrences,
        "authority_pdf_files": sum(
            1 for path in list_files(root) if "numdam" in path.name.lower() and path.suffix.lower() == ".pdf"
        ),
        "cross_corpus_filenames": len(forbidden_names),
        "errors": errors,
    }


def validate_known_identities(root: Path, expected: dict[str, tuple[int, str]]) -> list[dict[str, object]]:
    errors: list[dict[str, object]] = []
    for name, wanted in expected.items():
        path = root / name
        if not path.is_file():
            errors.append({"error": "missing_control", "path": name})
        elif identity(path) != wanted:
            errors.append({"error": "control_identity_mismatch", "path": name})
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    errors: list[dict[str, object]] = []
    private_files = list_files(PRIVATE_ROOT)
    public_files = list_files(PUBLIC_ROOT)
    private_rows = read_manifest(PRIVATE_ROOT / PRIVATE_MANIFEST)
    payload_rows = read_manifest(PUBLIC_ROOT / PAYLOAD_MANIFEST)

    private_replay = replay_manifest(
        PRIVATE_ROOT,
        private_rows,
        {PRIVATE_MANIFEST, PRIVATE_VALIDATION},
    )
    public_payload_replay = replay_manifest(
        PUBLIC_ROOT,
        payload_rows,
        {ZIP_NAME, PAYLOAD_MANIFEST, UPLOAD_MANIFEST, PACKAGE_VALIDATION},
    )
    zip_replay = replay_zip(PUBLIC_ROOT, payload_rows)
    upload_replay = replay_uploads(PUBLIC_ROOT)
    privacy = privacy_replay(PUBLIC_ROOT)

    private_validation = json.loads((PRIVATE_ROOT / PRIVATE_VALIDATION).read_text(encoding="utf-8"))
    package_validation = json.loads((PUBLIC_ROOT / PACKAGE_VALIDATION).read_text(encoding="utf-8"))
    public_tree_rows = []
    for path in public_files:
        rel = path.relative_to(PUBLIC_ROOT).as_posix()
        if rel == PACKAGE_VALIDATION:
            continue
        observed = identity(path)
        public_tree_rows.append({"relative_path": rel, "bytes": observed[0], "sha256": observed[1]})
    public_tree_sha = canonical_tree(public_tree_rows)

    errors.extend(validate_known_identities(PRIVATE_ROOT, EXPECTED_PRIVATE_IDENTITIES))
    errors.extend(validate_known_identities(PUBLIC_ROOT, EXPECTED_PUBLIC_IDENTITIES))
    errors.extend(private_replay["errors"])
    errors.extend(public_payload_replay["errors"])
    errors.extend(zip_replay["errors"])
    errors.extend(upload_replay["errors"])
    errors.extend(privacy["errors"])

    observed_private_total = (len(private_files), sum(path.stat().st_size for path in private_files))
    wanted_private_total = (EXPECTED_PRIVATE["files_total"], EXPECTED_PRIVATE["bytes_total"])
    if observed_private_total != wanted_private_total:
        errors.append({"error": "private_total_mismatch", "observed": observed_private_total, "wanted": wanted_private_total})
    observed_public_total = (len(public_files), sum(path.stat().st_size for path in public_files))
    wanted_public_total = (EXPECTED_PUBLIC["files_total"], EXPECTED_PUBLIC["bytes_total"])
    if observed_public_total != wanted_public_total:
        errors.append({"error": "public_total_mismatch", "observed": observed_public_total, "wanted": wanted_public_total})
    if private_replay["rows"] != EXPECTED_PRIVATE["manifest_rows"]:
        errors.append({"error": "private_manifest_row_count"})
    if private_replay["canonical_tree_sha256"] != EXPECTED_PRIVATE["tree_sha256"]:
        errors.append({"error": "private_tree_digest"})
    if private_validation.get("canonical_tree_sha256") != EXPECTED_PRIVATE["tree_sha256"]:
        errors.append({"error": "private_declared_tree_digest"})
    if public_payload_replay["rows"] != EXPECTED_PUBLIC["payload_rows"]:
        errors.append({"error": "payload_manifest_row_count"})
    if public_tree_sha != EXPECTED_PUBLIC["tree_sha256"]:
        errors.append({"error": "public_tree_digest"})
    if package_validation.get("public_projection", {}).get("canonical_tree_sha256") != EXPECTED_PUBLIC["tree_sha256"]:
        errors.append({"error": "public_declared_tree_digest"})
    if zip_replay["members"] != EXPECTED_PUBLIC["zip_members"]:
        errors.append({"error": "zip_member_count"})
    if (zip_replay["zip_bytes"], zip_replay["zip_sha256"]) != (EXPECTED_PUBLIC["zip_bytes"], EXPECTED_PUBLIC["zip_sha256"]):
        errors.append({"error": "zip_identity"})
    if upload_replay["rows"] != EXPECTED_PUBLIC["upload_rows"]:
        errors.append({"error": "upload_row_count"})
    if package_validation.get("status") != "PASS_READY_FOR_EXACT_ARCHIVE_CUSTODY_AND_THREE_CONCEPT_PUBLICATION" or package_validation.get("errors") != []:
        errors.append({"error": "package_validation_not_pass"})

    receipt = {
        "status": "PASS_INDEPENDENT_EXACT_PACKAGE_REPLAY" if not errors else "FAIL",
        "errors": errors,
        "private": {
            "root": str(PRIVATE_ROOT),
            "files": observed_private_total[0],
            "bytes": observed_private_total[1],
            **{key: value for key, value in private_replay.items() if key != "errors"},
        },
        "public": {
            "root": str(PUBLIC_ROOT),
            "files": observed_public_total[0],
            "bytes": observed_public_total[1],
            "canonical_tree_sha256": public_tree_sha,
            "payload_manifest": {key: value for key, value in public_payload_replay.items() if key != "errors"},
            "zip": {key: value for key, value in zip_replay.items() if key != "errors"},
            "direct_uploads": {key: value for key, value in upload_replay.items() if key != "errors"},
            "privacy": {key: value for key, value in privacy.items() if key != "errors"},
        },
    }
    rendered = json.dumps(receipt, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8", newline="\n")
    print(rendered, end="")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
