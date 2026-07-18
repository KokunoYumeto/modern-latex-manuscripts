from __future__ import annotations

import csv
import hashlib
import json
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path


STAGE = Path(__file__).resolve().parent.parent
SOURCE = Path(r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management")
ROOT_NAME = "Interlanguage_Language_Manager_Fleet_v12_20260718"
ROOT = STAGE / "fleet_snapshot" / ROOT_NAME
ZIP_PATH = STAGE / "16_Interlanguage_Language_Manager_Fleet_Snapshot_v12_20260718.zip"

CONTROL_MANAGERS = [
    "africa_horn_west",
    "arabic_persianate_rtl",
    "cjk",
    "english_germanic",
    "malay_sea_pacific",
    "romance",
    "turkic",
]

WORKING_SELECTIONS = [
    (
        "africa_horn_west",
        Path("03_working_translations/openstax_prealgebra_2e/section_2_1_tranche_001_20260717"),
    ),
    (
        "arabic_persianate_rtl",
        Path("03_working_translations/noether/paper06/tranche_001_opening"),
    ),
    (
        "malay_sea_pacific",
        Path("03_working_translations/noether/paper36/tranche_001_id_20260717"),
    ),
    (
        "turkic",
        Path("03_working_translations/hefferon_linear_algebra/compiled_review_tranches"),
    ),
]

SLAVIC_FILES = [
    Path("normalization_20260718/STATUS_AND_CONTINUATION_20260718.md"),
    Path("normalization_20260718/evidence/CORRESPONDENCE_FAMILY_SURFACE_INVENTORY.json"),
    Path("normalization_20260718/evidence/NORMALIZATION_COMPLETION_CURSOR.json"),
    Path("normalization_20260718/evidence/NORMALIZATION_STATUS_AUDIT.json"),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def copy_file(source: Path, destination: Path) -> None:
    if not source.is_file():
        raise FileNotFoundError(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def copy_tree(source: Path, destination: Path) -> None:
    if not source.is_dir():
        raise FileNotFoundError(source)
    for path in sorted(source.rglob("*")):
        if path.is_file():
            copy_file(path, destination / path.relative_to(source))


def classification(relative: Path) -> str:
    text = relative.as_posix()
    if "/working_outputs/" in f"/{text}":
        return "bounded_working_output_not_native_certified"
    if "slavic_interslavic" in text:
        return "normalization_status_and_evidence"
    if "/control/" in f"/{text}":
        return "manager_control_or_audit"
    return "reader_map_or_package_metadata"


def main() -> None:
    if ROOT.exists():
        shutil.rmtree(ROOT)
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    ROOT.mkdir(parents=True)

    copy_file(
        STAGE / "00_Interlanguage_Methodology_Current_v12_20260718.md",
        ROOT / "README.md",
    )
    copy_file(
        STAGE / "99_Interlanguage_Public_Status_v12_20260718.md",
        ROOT / "PUBLIC_STATUS.md",
    )

    for manager in CONTROL_MANAGERS:
        copy_tree(
            SOURCE / manager / "00_lane_control",
            ROOT / "managers" / manager / "control",
        )

    copy_file(
        SOURCE / "turkic" / "README.md",
        ROOT / "managers" / "turkic" / "README.md",
    )
    copy_file(
        SOURCE / "turkic" / "06_publication_candidates" / "README.md",
        ROOT / "managers" / "turkic" / "publication_candidates" / "README.md",
    )

    for manager, relative in WORKING_SELECTIONS:
        copy_tree(
            SOURCE / manager / relative,
            ROOT / "managers" / manager / "working_outputs" / relative.name,
        )

    for relative in SLAVIC_FILES:
        copy_file(
            SOURCE / "slavic_interslavic" / relative,
            ROOT / "managers" / "slavic_interslavic" / "control" / relative.name,
        )

    payload_rows = [
        [
            "Noether",
            "10.5281/zenodo.21423112",
            "German R823 source control; English, Spanish, French, Interslavic, and bounded CJK/RTL/Indonesian working outputs",
            "working corpus; not critical edition",
        ],
        [
            "SGA 5 and SGA 6",
            "10.5281/zenodo.21422245",
            "French workpasses; SGA5 English; corrected layered SGA6 English; bounded SGA6 Spanish",
            "working editions with declared authority layers",
        ],
        [
            "Interlanguage",
            "10.5281/zenodo.21124403",
            "source bodies, automata, terminology, methodology, normalization, completion gates, manager snapshot",
            "methodology and evidence sidecar",
        ],
        [
            "GitHub",
            "https://github.com/KokunoYumeto/modern-latex-manuscripts",
            "human-readable mirrors, editable evidence, manifests, and pull-request route",
            "public collaboration mirror",
        ],
    ]
    with (ROOT / "PUBLIC_PAYLOAD_MAP.csv").open(
        "w", encoding="utf-8", newline=""
    ) as handle:
        writer = csv.writer(handle)
        writer.writerow(["record", "identifier", "contents", "classification"])
        writer.writerows(payload_rows)

    manifest_rows = []
    for path in sorted(item for item in ROOT.rglob("*") if item.is_file()):
        relative = path.relative_to(ROOT)
        manifest_rows.append(
            {
                "path": relative.as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
                "classification": classification(relative),
            }
        )

    manifest_path = ROOT / "FILE_MANIFEST.csv"
    with manifest_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(manifest_rows[0]))
        writer.writeheader()
        writer.writerows(manifest_rows)

    summary = {
        "captured_utc": datetime.now(timezone.utc).isoformat(),
        "manager_count": 8,
        "copied_payload_file_count": len(manifest_rows),
        "classification": (
            "manager controls and bounded working outputs; not critical editions"
        ),
        "moving_work_excluded": [
            "romance/05_sga5_spanish_20260717/SGA5_ES_WORKPASS",
            (
                "SGA continuation 2/_claude_aid/sga6_full_audit_20260703/"
                "sga6_fr_workpass.*"
            ),
        ],
    }
    (ROOT / "BUILD_SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    checksum_files = sorted(item for item in ROOT.rglob("*") if item.is_file())
    checksum_path = ROOT / "SHA256SUMS.txt"
    checksum_path.write_text(
        "".join(
            f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}\n"
            for path in checksum_files
        ),
        encoding="utf-8",
    )

    with zipfile.ZipFile(
        ZIP_PATH, "w", zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for path in sorted(item for item in ROOT.rglob("*") if item.is_file()):
            archive.write(
                path,
                f"{ROOT_NAME}/{path.relative_to(ROOT).as_posix()}",
            )

    with zipfile.ZipFile(ZIP_PATH) as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"ZIP integrity failure: {bad}")
        members = archive.namelist()
        if not members or any(
            not name.startswith(ROOT_NAME + "/") for name in members
        ):
            raise RuntimeError("ZIP does not have exactly one package root")

    print(
        json.dumps(
            {
                **summary,
                "final_package_file_count": len(
                    [item for item in ROOT.rglob("*") if item.is_file()]
                ),
                "zip_bytes": ZIP_PATH.stat().st_size,
                "zip_sha256": sha256(ZIP_PATH),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
