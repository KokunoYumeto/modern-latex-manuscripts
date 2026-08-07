from __future__ import annotations

import csv
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parents[5]
MANIFEST = ROOT / "manifest.csv"
VERIFY = ROOT / "verify.json"
EXCLUDED = {"manifest.csv", "verify.json"}
REPARSE_POINT = 0x400


def digest(path: Path) -> tuple[int, str]:
    sha = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            sha.update(chunk)
    return path.stat().st_size, sha.hexdigest().upper()


def safe_relative(path: Path) -> str:
    relative = path.relative_to(ROOT).as_posix()
    pure = PurePosixPath(relative)
    if (
        not relative
        or "\\" in relative
        or pure.is_absolute()
        or any(part in ("", ".", "..") for part in pure.parts)
        or ":" in relative
    ):
        raise RuntimeError(f"unsafe manifest path: {relative!r}")
    return relative


def is_reparse(path: Path) -> bool:
    stat = path.lstat()
    return path.is_symlink() or bool(getattr(stat, "st_file_attributes", 0) & REPARSE_POINT)


def members() -> list[tuple[str, Path]]:
    result: list[tuple[str, Path]] = []
    for path in ROOT.rglob("*"):
        relative = safe_relative(path)
        if is_reparse(path):
            raise RuntimeError(f"reparse point forbidden in frozen package: {relative}")
        if not path.is_file() or relative in EXCLUDED:
            continue
        result.append((relative, path))
    result.sort(key=lambda item: item[0])
    names = [item[0] for item in result]
    if len(names) != len(set(names)) or len(names) != len({name.casefold() for name in names}):
        raise RuntimeError("manifest member paths are not exact- and casefold-unique")
    return result


def parse_records(rows: list[dict[str, str]]) -> tuple[int, int, list[dict[str, object]]]:
    json_files = 0
    jsonl_records = 0
    failures: list[dict[str, object]] = []
    for row in rows:
        relative = row["path"]
        path = ROOT / Path(relative)
        try:
            if relative.endswith(".json"):
                json.loads(path.read_text(encoding="utf-8"))
                json_files += 1
            elif relative.endswith(".jsonl"):
                for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                    json.loads(line)
                    jsonl_records += 1
        except Exception as error:
            failures.append({"path": relative, "failure": "parse", "detail": str(error)})
    return json_files, jsonl_records, failures


def create_manifest() -> tuple[int, int]:
    if MANIFEST.exists() or VERIFY.exists():
        raise RuntimeError("refusing to overwrite an existing manifest or verifier")
    files = members()
    total = 0
    with MANIFEST.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["path", "bytes", "sha256"])
        for relative, path in files:
            size, sha256 = digest(path)
            total += size
            writer.writerow([relative, size, sha256])
    return len(files), total


def external_identity(relative: str) -> dict[str, object]:
    path = WORKSPACE / Path(relative)
    size, sha256 = digest(path)
    return {"path": relative, "bytes": size, "sha256": sha256}


def replay(expected_entries: int, expected_total: int) -> dict[str, object]:
    manifest_size, manifest_sha256 = digest(MANIFEST)
    with MANIFEST.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != ["path", "bytes", "sha256"]:
            raise RuntimeError("manifest header mismatch")
        rows = list(reader)
    if len(rows) != expected_entries:
        raise RuntimeError("manifest entry count changed during replay")

    listed = [row["path"] for row in rows]
    if listed != sorted(listed):
        raise RuntimeError("manifest paths are unsorted")
    if len(listed) != len(set(listed)) or len(listed) != len({path.casefold() for path in listed}):
        raise RuntimeError("manifest paths are not exact- and casefold-unique")

    failures: list[dict[str, object]] = []
    replay_total = 0
    for row in rows:
        pure = PurePosixPath(row["path"])
        if pure.is_absolute() or any(part in ("", ".", "..") for part in pure.parts):
            failures.append({"path": row["path"], "failure": "unsafe_path"})
            continue
        path = (ROOT / Path(*pure.parts)).resolve(strict=False)
        try:
            path.relative_to(ROOT.resolve())
        except ValueError:
            failures.append({"path": row["path"], "failure": "containment"})
            continue
        if not path.is_file() or is_reparse(path):
            failures.append({"path": row["path"], "failure": "missing_or_reparse"})
            continue
        size, sha256 = digest(path)
        replay_total += size
        if size != int(row["bytes"]) or sha256 != row["sha256"]:
            failures.append(
                {
                    "path": row["path"],
                    "failure": "identity",
                    "actual_bytes": size,
                    "actual_sha256": sha256,
                }
            )

    actual = [relative for relative, _ in members()]
    missing_from_manifest = sorted(set(actual) - set(listed))
    listed_but_absent = sorted(set(listed) - set(actual))
    json_files, jsonl_records, parse_failures = parse_records(rows)
    failures.extend(parse_failures)

    receipt = json.loads((ROOT / "return.json").read_text(encoding="utf-8"))
    disposition_pass = (
        "accepted" not in receipt
        and receipt["disposition"] == "FROZEN_PENDING_INDEPENDENT_REVIEW"
        and receipt["producer_state"] == "FROZEN_PENDING_INDEPENDENT_REVIEW"
        and receipt["publishable"] is False
        and receipt["clean_day_count"] == 0
        and receipt["required_independent_checks_remaining"] == 3
    )
    external = {
        "authority_pointer": external_identity(
            "03_projects/noether/07_german_canon_control/CURRENT_GERMAN_AUTHORITY_POINTER.json"
        ),
        "authority_edition": external_identity(
            "03_projects/noether/07_german_canon_control/candidates/ED0008/noether.tex"
        ),
        "independent_csv": external_identity(
            "03_projects/language_management/cjk/05_independent_checking/cjk_r1/zh_r26.csv"
        ),
        "independent_report": external_identity(
            "03_projects/language_management/cjk/05_independent_checking/cjk_r1/zh_r26.md"
        ),
        "agent_ledger": external_identity(
            "03_projects/language_management/cjk/05_independent_checking/noether_chinese/agent2.jsonl"
        ),
    }
    external_pass = (
        external["authority_pointer"]["sha256"]
        == "FF98F436CF8D38AA1D13CF1D969857CE277D02851CC79EFE521DFE1D0B45B98D"
        and external["authority_edition"]["sha256"]
        == "C83A94D25DE8FD27C66E2C6C50BAB04AA875E6C0A6A87BDFCA202E69A8EA660D"
        and external["independent_csv"]["sha256"]
        == "706ABC522E9CF2A209B9C783937A8569397636718F575CE3BF988CF1A64B9D5D"
        and external["independent_report"]["sha256"]
        == "7301C588500794C222EBFF0ACEADBF4BF7FD0E701A02CBDC7C518C9679236501"
    )
    pages = len(PdfReader(str(ROOT / "reader.pdf")).pages)
    all_pass = bool(
        not failures
        and not missing_from_manifest
        and not listed_but_absent
        and replay_total == expected_total
        and pages == 424
        and disposition_pass
        and external_pass
    )
    if not all_pass:
        raise RuntimeError(
            json.dumps(
                {
                    "failures": failures,
                    "missing_from_manifest": missing_from_manifest,
                    "listed_but_absent": listed_but_absent,
                    "replay_total": replay_total,
                    "expected_total": expected_total,
                    "pages": pages,
                    "disposition_pass": disposition_pass,
                    "external_pass": external_pass,
                }
            )
        )

    critical_names = [
        "reader.tex",
        "reader.pdf",
        "reader.txt",
        "return.json",
        "diff.json",
        "qa.json",
        "build.json",
        "visual.json",
        "find.jsonl",
        "fail.jsonl",
        "de/p45.json",
        "de/p45v.json",
    ]
    return {
        "record_id": "ZHCHK-NOETHER-CUM-R5-VERIFY-001",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "manifest": {
            "path": str(MANIFEST),
            "bytes": manifest_size,
            "sha256": manifest_sha256,
            "entries": len(rows),
            "member_bytes": replay_total,
            "self_excluded": True,
            "verifier_receipt_excluded": True,
            "exact_unique": True,
            "casefold_unique": True,
            "reparse_points": 0,
        },
        "replay": {
            "identity_failures": failures,
            "missing_from_manifest": missing_from_manifest,
            "listed_but_absent": listed_but_absent,
            "actual_regular_files": len(actual) + 1,
            "expected_excluded_after_write": ["manifest.csv", "verify.json"],
        },
        "parse": {
            "json_files": json_files,
            "jsonl_records": jsonl_records,
            "failures": parse_failures,
        },
        "critical": {
            name: dict(zip(("bytes", "sha256"), digest(ROOT / name))) for name in critical_names
        },
        "external_pins": external,
        "disposition_pass": disposition_pass,
        "pdf_pages": pages,
        "all_pass": True,
    }


def main() -> None:
    entries, total = create_manifest()
    result = replay(entries, total)
    VERIFY.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "manifest": result["manifest"],
                "verify": dict(zip(("bytes", "sha256"), digest(VERIFY))),
                "all_pass": True,
            }
        )
    )


if __name__ == "__main__":
    main()
