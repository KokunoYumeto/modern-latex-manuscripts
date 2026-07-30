#!/usr/bin/env python3
"""Build the compact current EGA reader/source release."""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import shutil
import zipfile
from pathlib import Path, PurePosixPath


REPO = Path(__file__).resolve().parents[1]
EGA = REPO / "sources" / "ega"
OUTPUT = EGA / "releases" / "ega-current-reference-v2-20260730-r2"
P0_3 = EGA / "checkpoints" / "ega0-ega3-complete-reference-v2-r1-20260730"
P1 = EGA / "checkpoints" / "ega1-complete-reference-v2-r2-reader-clean-20260730"
P2 = EGA / "checkpoints" / "ega2-complete-reference-v2-r1-20260730"
P4 = EGA / "checkpoints" / "ega4-sections1-10-source-aligned-working-20260730"
P2_ZIP = EGA / "ega2-complete-reference-v2-release-20260730" / (
    "10b_EGA2_English_Source_20260730.zip"
)

ZIP_TIME = (2026, 7, 30, 0, 0, 0)
BUNDLE_ROOT = "EGA_Current_English_Readers_and_TeX_20260730/"

BUNDLE = "00 Current_EGA_English_Readers_and_Buildable_TeX_20260730.zip"
PDFS = {
    "EGA0": "00a_EGA0_English_Complete_Through_Section13_Reference_v2_20260730.pdf",
    "EGA1": "00b_EGA1_English_Complete_Reference_v2_Reader_20260730.pdf",
    "EGA2": "00c_EGA2_English_Complete_Reference_v2_Reader_20260730.pdf",
    "EGAIII": "00d_EGAIII_English_Published_Text_Complete_Reference_v2_20260730.pdf",
    "EGAIV": "00e_EGAIV_English_Working_Reader_Sections1_10_20260730.pdf",
}
MASTERS = {
    "EGA0": "01a_EGA0_English_Master_20260730.tex",
    "EGA1": "01b_EGA1_English_Master_20260730.tex",
    "EGA2": "01c_EGA2_English_Master_20260730.tex",
    "EGAIII": "01d_EGAIII_English_Master_20260730.tex",
    "EGAIV": "01e_EGAIV_English_Master_Sections1_10_20260730.tex",
}
SOURCE_ZIPS = {
    "EGA0_EGAIII": "02a_EGA0_EGAIII_English_Reference_v2_TeX_PDF_QA_20260730.zip",
    "EGA1": "02b_EGA1_English_Reference_v2_TeX_PDF_QA_20260730.zip",
    "EGA2": "02c_EGA2_English_Reference_v2_TeX_PDF_QA_20260730.zip",
    "EGAIV": "02d_EGAIV_English_Sections1_10_TeX_PDF_QA_20260730.zip",
}
README_NAME = "90 EGA - README and Status.md"
SUMMARY_NAME = "91 EGA - Public Summary.json"
MANIFEST_NAME = "92 EGA - Current File SHA256SUMS.csv"

EXPECTED = {
    "EGA0_PDF": (1_200_518, "99C3D89B432231EC04F5932BA1404FE0B17A05500EA41459B9AE046599BBAD4E"),
    "EGA1_PDF": (1_356_401, "0DC301F1998AA4E6A97ABD92197BB94A3F7FBEE1847261CC7BB69E0F8E6D8C58"),
    "EGA2_PDF": (1_905_144, "16487005C6257BDA2FC8B2C872C153538DE73A8950CD9B26D772B6BE354FA78F"),
    "EGAIII_PDF": (1_299_169, "25F4A2A857F36B536B9925C013BAA575B01E7C2CED438752CEE4384CBE1C1E70"),
    "EGAIV_PDF": (2_632_563, "773EFC15C9B815504D06A59F624C7EFC9A76B55BD5EC2F4FD17DAAEFEEB5AA6A"),
    "EGA0_MASTER": (787, "35991ACEB8C7467344198E5B09E725DDD96E692BA1F14DECAE7A55C059FEFEAF"),
    "EGA1_MASTER": (3_193, "EEEEB19FF8D94B62ABFCB39A4B2A43E9F7EB701362027804654D8CCF818F0097"),
    "EGA2_MASTER": (2_205, "D42280B6ECD1E0ECCB4812A5F902510E9DBF1BBCFB6965EEA7CED06E0199A525"),
    "EGAIII_MASTER": (3_479, "2E8CD9D4E8528B52F67325DD14DB9A6F5F08A39BCC330AEC941A5E16C07C50A6"),
    "EGAIV_MASTER": (765, "2209635F42A66B61001271D9791E03DD7988BF1FDBDE0DECF7A80CD47951B9FF"),
    "EGA2_ZIP": (4_950_763, "415324691FFFD387F35862E29115184B14AE4A6D0C8703A0BB2B057211D8F2BD"),
    "EGAIV_ZIP": (365_786, "08EDEA8FEF8B3233E8FA69072E981F26A60860C68A234363F580B8BB3E2C9677"),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def check(path: Path, identity: tuple[int, str]) -> None:
    if not path.is_file():
        raise RuntimeError(f"missing input: {path}")
    if (path.stat().st_size, sha256(path)) != identity:
        raise RuntimeError(f"input identity changed: {path.name}")


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        bool(name)
        and name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and re.match(r"^[A-Za-z]:", name) is None
    )


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=ZIP_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.create_system = 3
    info.external_attr = 0o100644 << 16
    return info


def csv_bytes(rows: list[dict[str, object]]) -> bytes:
    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(
        buffer,
        fieldnames=["relative_path", "bytes", "sha256"],
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def tree_members(root: Path, prefix: str) -> dict[str, bytes]:
    members: dict[str, bytes] = {}
    for path in sorted(root.rglob("*"), key=lambda row: row.as_posix().casefold()):
        if path.is_file():
            name = prefix + path.relative_to(root).as_posix()
            if not safe_member(name):
                raise RuntimeError(f"unsafe tree member: {name}")
            members[name] = path.read_bytes()
    return members


def read_zip(path: Path) -> dict[str, bytes]:
    members: dict[str, bytes] = {}
    with zipfile.ZipFile(path) as archive:
        if archive.testzip() is not None:
            raise RuntimeError(f"ZIP CRC failure: {path.name}")
        for info in archive.infolist():
            if info.is_dir():
                continue
            if not safe_member(info.filename) or info.filename in members:
                raise RuntimeError(f"unsafe or duplicate ZIP member: {info.filename}")
            members[info.filename] = archive.read(info.filename)
    return members


def write_zip(path: Path, members: dict[str, bytes]) -> dict[str, object]:
    with zipfile.ZipFile(path, "w", allowZip64=True) as archive:
        for name, data in sorted(members.items(), key=lambda item: item[0].casefold()):
            if not safe_member(name):
                raise RuntimeError(f"unsafe output ZIP member: {name}")
            archive.writestr(
                zip_info(name),
                data,
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )
    replay = read_zip(path)
    if replay != members:
        raise RuntimeError(f"ZIP readback mismatch: {path.name}")
    return {
        "filename": path.name,
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "members": len(members),
        "uncompressed_bytes": sum(len(data) for data in members.values()),
        "member_identities": {
            name: {"bytes": len(data), "sha256": sha256_bytes(data)}
            for name, data in sorted(members.items(), key=lambda item: item[0].casefold())
        },
    }


def verify_manifest(package: Path) -> None:
    manifest = package / "ZENODO_PAYLOAD_MANIFEST.csv"
    rows = read_csv(manifest)
    manifest_paths = {row.get("relative_path", row.get("relpath", "")): row for row in rows}
    actual = {
        path.relative_to(package).as_posix()
        for path in package.rglob("*")
        if path.is_file()
        and path.name not in {"ZENODO_PAYLOAD_MANIFEST.csv", "PACKAGE_VALIDATION.json"}
    }
    # EGA 0/III excludes only the manifest; EGA I excludes manifest and validation.
    if package == P0_3:
        actual.add("controls/PUBLIC_PROJECTION_VALIDATION.json")
        expected = {
            path.relative_to(package).as_posix()
            for path in package.rglob("*")
            if path.is_file() and path.name != "ZENODO_PAYLOAD_MANIFEST.csv"
        }
    else:
        expected = actual
    if set(manifest_paths) != expected:
        raise RuntimeError(f"package manifest exact-set mismatch: {package.name}")
    for relative, row in manifest_paths.items():
        path = package / relative
        if path.stat().st_size != int(row["bytes"]) or sha256(path) != row["sha256"]:
            raise RuntimeError(f"package manifest replay mismatch: {relative}")


def source_rows(package: Path, member_column: str | None = None) -> list[str]:
    rows = read_csv(package / "controls" / "SOURCE_CLOSURE.csv")
    if member_column is not None:
        rows = [row for row in rows if row[member_column] == "yes"]
        key = "source_relpath"
    else:
        key = "relative_path"
    result = [row[key] for row in rows]
    for relative in result:
        if not (package / "source" / relative).is_file():
            raise RuntimeError(f"source closure member missing: {relative}")
    return result


def package_zip(package: Path, root_name: str, output: Path) -> dict[str, object]:
    members = tree_members(package, root_name.rstrip("/") + "/")
    return write_zip(output, members)


def release_readme() -> bytes:
    return b"""# Current EGA English readers

Start with the leading ZIP: it contains one cumulative English reader PDF and
the complete buildable TeX closure for every current reader on this surface.
The same five reader PDFs and master TeX files are directly available next.
Source and QA packages follow as four coherent ZIPs.

Current reader scopes:

- EGA 0: complete through Section 13; reference-v2 working reader.
- EGA I: complete through authority EOF; reader-clean reference-v2 successor.
- EGA II: complete through authority EOF; reference-v2 working reader.
- EGA III: complete published text through 7.9.14; reference-v2 working reader.
- EGA IV: current source-aligned working reader through Sections 1-10.

These are scholarly working translations, not critical editions, mathematical
or peer-review certifications, accessibility remediation, or rights-clearance
decisions. No blanket license or transfer of underlying rights is asserted.
Earlier Zenodo versions and GitHub checkpoint directories preserve prior
states immutably.
"""


def main() -> None:
    if OUTPUT.exists():
        raise RuntimeError(f"refusing to overwrite release directory: {OUTPUT}")
    verify_manifest(P0_3)
    verify_manifest(P1)

    pdf_inputs = {
        "EGA0": P0_3 / "readers" / "EGA0_English_Complete_Through_Section13_Reference_v2.pdf",
        "EGA1": P1 / "EGA1_English_complete_reference_reader.pdf",
        "EGA2": P2 / "EGA2_English_complete_reference_reader.pdf",
        "EGAIII": P0_3 / "readers" / "EGAIII_English_Complete_Sections1_Through7_Reference_v2.pdf",
        "EGAIV": P4 / "00d_EGA4_English_Sections1_10_Reader.pdf",
    }
    master_inputs = {
        "EGA0": P0_3 / "source" / "ega0.tex",
        "EGA1": P1 / "source" / "ega1.tex",
        "EGA2": P2 / "source" / "ega2.tex",
        "EGAIII": P0_3 / "source" / "ega3.tex",
        "EGAIV": P4 / "02d_EGA4_English_Sections1_10_Master.tex",
    }
    for key, path in pdf_inputs.items():
        check(path, EXPECTED[f"{key}_PDF"])
    for key, path in master_inputs.items():
        check(path, EXPECTED[f"{key}_MASTER"])
    check(P2_ZIP, EXPECTED["EGA2_ZIP"])
    p4_zip = P4 / "10g_EGA4_English_Sections1_10_Source_20260730.zip"
    check(p4_zip, EXPECTED["EGAIV_ZIP"])

    OUTPUT.mkdir(parents=True)
    for key, name in PDFS.items():
        shutil.copyfile(pdf_inputs[key], OUTPUT / name)
    for key, name in MASTERS.items():
        shutil.copyfile(master_inputs[key], OUTPUT / name)

    zip_reports = {
        "EGA0_EGAIII": package_zip(
            P0_3,
            "EGA0_EGAIII_English_Reference_v2_20260730",
            OUTPUT / SOURCE_ZIPS["EGA0_EGAIII"],
        ),
        "EGA1": package_zip(
            P1,
            "EGA1_English_Reference_v2_R2_20260730",
            OUTPUT / SOURCE_ZIPS["EGA1"],
        ),
    }
    shutil.copyfile(P2_ZIP, OUTPUT / SOURCE_ZIPS["EGA2"])
    shutil.copyfile(p4_zip, OUTPUT / SOURCE_ZIPS["EGAIV"])
    zip_reports["EGA2"] = {
        "filename": SOURCE_ZIPS["EGA2"],
        "bytes": (OUTPUT / SOURCE_ZIPS["EGA2"]).stat().st_size,
        "sha256": sha256(OUTPUT / SOURCE_ZIPS["EGA2"]),
        "members": len(read_zip(OUTPUT / SOURCE_ZIPS["EGA2"])),
    }
    zip_reports["EGAIV"] = {
        "filename": SOURCE_ZIPS["EGAIV"],
        "bytes": (OUTPUT / SOURCE_ZIPS["EGAIV"]).stat().st_size,
        "sha256": sha256(OUTPUT / SOURCE_ZIPS["EGAIV"]),
        "members": len(read_zip(OUTPUT / SOURCE_ZIPS["EGAIV"])),
    }

    bundle_members: dict[str, bytes] = {}
    for key, path in pdf_inputs.items():
        bundle_members[f"{BUNDLE_ROOT}{key}/reader/{PDFS[key]}"] = path.read_bytes()

    for relative in source_rows(P0_3, "ega0_member"):
        bundle_members[f"{BUNDLE_ROOT}EGA0/source/{relative}"] = (
            P0_3 / "source" / relative
        ).read_bytes()
    for relative in source_rows(P1):
        bundle_members[f"{BUNDLE_ROOT}EGA1/source/{relative}"] = (
            P1 / "source" / relative
        ).read_bytes()
    for relative in source_rows(P2):
        bundle_members[f"{BUNDLE_ROOT}EGA2/source/{relative}"] = (
            P2 / "source" / relative
        ).read_bytes()
    for relative in source_rows(P0_3, "ega3_member"):
        bundle_members[f"{BUNDLE_ROOT}EGAIII/source/{relative}"] = (
            P0_3 / "source" / relative
        ).read_bytes()

    p4_members = read_zip(p4_zip)
    p4_prefix = "EGA4_English_Sections1_10_Source_20260730/"
    for name, data in p4_members.items():
        if not name.startswith(p4_prefix):
            raise RuntimeError(f"unexpected EGA IV ZIP member: {name}")
        bundle_members[f"{BUNDLE_ROOT}EGAIV/{name[len(p4_prefix):]}"] = data

    bundle_members[BUNDLE_ROOT + "README.md"] = release_readme()
    bundle_rows = [
        {
            "relative_path": name[len(BUNDLE_ROOT):],
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        }
        for name, data in sorted(bundle_members.items(), key=lambda item: item[0].casefold())
    ]
    bundle_members[BUNDLE_ROOT + "SHA256SUMS.csv"] = csv_bytes(bundle_rows)
    bundle_report = write_zip(OUTPUT / BUNDLE, bundle_members)

    (OUTPUT / README_NAME).write_bytes(release_readme())
    summary = {
        "schema": "ega-current-compact-reference-v2-release-1.0",
        "status": "PASS",
        "publication_date": "2026-07-30",
        "concept_doi": "10.5281/zenodo.20414353",
        "predecessor_record": 21708453,
        "reader_order": [PDFS[key] for key in ("EGA0", "EGA1", "EGA2", "EGAIII", "EGAIV")],
        "scopes": {
            "EGA0": "complete through Section 13",
            "EGA1": "complete through authority EOF",
            "EGA2": "complete through authority EOF",
            "EGAIII": "complete published text through 7.9.14",
            "EGAIV": "current source-aligned working reader through Sections 1-10",
        },
        "bundle": bundle_report,
        "source_packages": zip_reports,
        "caveat": "Scholarly working readers; no critical-edition, mathematical-certification, accessibility, or rights-clearance claim.",
    }
    (OUTPUT / SUMMARY_NAME).write_text(
        json.dumps(summary, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    upload_names = [BUNDLE]
    upload_names.extend(PDFS.values())
    upload_names.extend(MASTERS.values())
    upload_names.extend(SOURCE_ZIPS.values())
    upload_names.extend([README_NAME, SUMMARY_NAME])
    rows = [
        {
            "relative_path": name,
            "bytes": (OUTPUT / name).stat().st_size,
            "sha256": sha256(OUTPUT / name),
        }
        for name in upload_names
    ]
    (OUTPUT / MANIFEST_NAME).write_bytes(csv_bytes(rows))
    upload_names.append(MANIFEST_NAME)

    privacy_patterns = [
        re.compile(rb"[A-Za-z]:[\\/]Users[\\/]", re.I),
        re.compile(rb"03_working_translations", re.I),
        re.compile(rb"06_publication_candidates", re.I),
    ]
    privacy_hits: list[str] = []
    for name in upload_names:
        data = (OUTPUT / name).read_bytes()
        if any(pattern.search(data) for pattern in privacy_patterns):
            privacy_hits.append(name)
    if privacy_hits:
        raise RuntimeError(f"privacy hits in release: {privacy_hits}")

    validation = {
        "schema": "ega-current-compact-reference-v2-release-validation-1.0",
        "status": "PASS",
        "errors": [],
        "upload_files": len(upload_names),
        "upload_bytes": sum((OUTPUT / name).stat().st_size for name in upload_names),
        "manifest_rows": len(rows),
        "privacy_hits": privacy_hits,
        "bundle": bundle_report,
        "source_packages": zip_reports,
        "files": {
            name: {
                "bytes": (OUTPUT / name).stat().st_size,
                "sha256": sha256(OUTPUT / name),
            }
            for name in upload_names
        },
    }
    (OUTPUT / "RELEASE_VALIDATION.json").write_text(
        json.dumps(validation, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(validation, indent=2))


if __name__ == "__main__":
    main()
