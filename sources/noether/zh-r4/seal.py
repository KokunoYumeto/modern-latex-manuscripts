from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "manifest.csv"
VERIFY = HERE / "verify.json"
EXCLUDED = {"manifest.csv", "verify.json"}


def digest(path: Path) -> tuple[int, str]:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return path.stat().st_size, h.hexdigest().upper()


def members() -> list[Path]:
    result = []
    for path in HERE.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(HERE).as_posix()
        if relative in EXCLUDED:
            continue
        result.append(path)
    return sorted(result, key=lambda path: path.relative_to(HERE).as_posix())


def create_manifest() -> tuple[int, int]:
    if MANIFEST.exists() or VERIFY.exists():
        raise RuntimeError("refusing to overwrite an existing manifest or verifier receipt")
    files = members()
    total = 0
    with MANIFEST.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["path", "bytes", "sha256"])
        for path in files:
            size, sha256 = digest(path)
            total += size
            writer.writerow([path.relative_to(HERE).as_posix(), size, sha256])
    return len(files), total


def verify_manifest(expected_entries: int, expected_total: int) -> dict[str, object]:
    manifest_size, manifest_sha256 = digest(MANIFEST)
    rows: list[dict[str, str]]
    with MANIFEST.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != expected_entries:
        raise RuntimeError("manifest entry count changed during replay")

    listed = [row["path"] for row in rows]
    if len(listed) != len(set(listed)) or listed != sorted(listed):
        raise RuntimeError("manifest paths are duplicate or unsorted")

    failures: list[dict[str, object]] = []
    replay_total = 0
    for row in rows:
        path = HERE / Path(row["path"])
        if not path.is_file():
            failures.append({"path": row["path"], "failure": "missing"})
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

    actual = [path.relative_to(HERE).as_posix() for path in members()]
    missing_from_manifest = sorted(set(actual) - set(listed))
    listed_but_absent = sorted(set(listed) - set(actual))
    all_pass = bool(
        not failures
        and not missing_from_manifest
        and not listed_but_absent
        and replay_total == expected_total
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
                }
            )
        )

    return {
        "record_id": "ZHCHK-NOETHER-CUM-R4-VERIFY-001",
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "manifest": {
            "path": str(MANIFEST),
            "bytes": manifest_size,
            "sha256": manifest_sha256,
            "entries": len(rows),
            "member_bytes": replay_total,
            "self_excluded": True,
            "verifier_receipt_excluded": True,
        },
        "replay": {
            "identity_failures": failures,
            "missing_from_manifest": missing_from_manifest,
            "listed_but_absent": listed_but_absent,
        },
        "critical": {
            "tex": dict(zip(("bytes", "sha256"), digest(HERE / "reader.tex"))),
            "pdf": dict(zip(("bytes", "sha256"), digest(HERE / "reader.pdf"))),
            "return": dict(zip(("bytes", "sha256"), digest(HERE / "return.json"))),
            "build": dict(zip(("bytes", "sha256"), digest(HERE / "build.json"))),
            "visual": dict(zip(("bytes", "sha256"), digest(HERE / "visual.json"))),
        },
        "all_pass": True,
    }


def main() -> None:
    entries, total = create_manifest()
    result = verify_manifest(entries, total)
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
