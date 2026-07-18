from __future__ import annotations

import csv
import hashlib
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "16_Interlanguage_v12_public_manifest_20260718.csv"
CHECKSUMS = ROOT / "16_Interlanguage_v12_public_sha256_20260718.txt"
UPLOADS = [
    (
        "00_Interlanguage_Methodology_Current_v12_20260718.pdf",
        "default reader-facing methodology and fleet map",
    ),
    (
        "00_Interlanguage_Methodology_Current_v12_20260718.md",
        "editable reader-facing methodology and fleet map",
    ),
    (
        "16_Interlanguage_Language_Manager_Fleet_Snapshot_v12_20260718.zip",
        "eight-lane controls and bounded working outputs",
    ),
    (
        "99_Interlanguage_Public_Status_v12_20260718.md",
        "scope and non-certification statement",
    ),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def main() -> None:
    rows = []
    for name, role in UPLOADS:
        path = ROOT / name
        if not path.is_file():
            raise FileNotFoundError(path)
        rows.append(
            {
                "filename": name,
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "role": role,
            }
        )

    with MANIFEST.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    checksum_paths = [ROOT / name for name, _ in UPLOADS] + [MANIFEST]
    CHECKSUMS.write_text(
        "".join(f"{sha256(path)}  {path.name}\n" for path in checksum_paths),
        encoding="utf-8",
    )

    with zipfile.ZipFile(ROOT / UPLOADS[2][0]) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("ZIP integrity check failed")

    print(f"manifest_rows={len(rows)}")
    print(f"zip_sha256={rows[2]['sha256']}")
    print(f"pdf_sha256={rows[0]['sha256']}")


if __name__ == "__main__":
    main()
