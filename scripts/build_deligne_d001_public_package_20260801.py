#!/usr/bin/env python3
"""Build the privacy-clean Deligne D001 reader and source-evidence package."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import struct
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / "sources/deligne/d001-bilingual-source-aligned-20260801"
ZIP_ROOT = "Deligne_D001_Bilingual_SourceAligned_20260801"

AUTHORITY_NAME = "Congruence_sous_groupes_pk_IAS_scan.pdf"
AUTHORITY_BYTES = 1_116_696
AUTHORITY_SHA256 = "4078B5827B016B7F0FA3F3ECB3A7D710AC7D63E7A1EDD889F86FCAA847078C2C"

PUBLIC_FILES = {
    "05_Deligne_D001_Bilingual_SourceAligned_Reader_20260801.pdf": (
        "build/bilingual_source_aligned_eof_r1/D001_Congruences_Bilingual_Reader.pdf",
        141_068,
        "54F6BF7B9C98BEF76B2F6DD54DAB763C9A25CBC7796963CD0704473D664A04B5",
        8,
        "bilingual_reader",
    ),
    "06_Deligne_D001_English_SourceAligned_20260801.pdf": (
        "build/en_source_aligned_through_eof_r1/D001_Congruences_EN_source_aligned.pdf",
        73_198,
        "04F6882A0BF898701424C05AC8866ED4F3350BC5AC910E7C45C93BCA73EC1FF5",
        4,
        "english_reader",
    ),
    "07_Deligne_D001_French_SourceAligned_20260801.pdf": (
        "build/fr_source_aligned_through_eof_r1/D001_Congruences_FR_source_aligned.pdf",
        65_284,
        "28B3E4D7688E705E2F875C31B62D8146BAB8C88712268F1524EA6F320D8D4B0D",
        4,
        "french_reader",
    ),
}

SOURCE_INPUTS = {
    "tex/D001_Congruences_Bilingual_Reader.tex": (
        774,
        "2C3A24C823097449F9790F86A19A3DE2C389228481B1A91FC69992DABF801C61",
    ),
    "tex/D001_Congruences_EN_source_aligned.tex": (
        8_881,
        "860E6C265A032E23A37FD35C015CDBD23E1FB15CF40495584C4DFD1DDA812706",
    ),
    "tex/D001_Congruences_FR_source_aligned.tex": (
        9_720,
        "F9CE5E20DC2E1553B3D8D0AEA8BFEDD74541E67375E2B6C92730F9DE86742309",
    ),
    "controls/SOURCE_DEFECT_REGISTER.csv": (
        1_204,
        "30973066BB9987E099998AF09DCC59ADF92DF9C4A6DF173D26D73AA19992EAF9",
    ),
    "controls/D001_SOURCE_MATH_CHECKS.json": (
        4_091,
        "71563EF2317DD77EC5129A491B06F9BE5898A3746FEC7C345544AB63D55B8DCF",
    ),
}

CROP_MANIFEST_IDENTITY = (
    14_069,
    "749C84E5BF78B2AD3B0BA5F4E636A84CED89EE2BA7C8CEFDBC3DB9F837C250E5",
)

TEXT_EXTENSIONS = {".csv", ".json", ".jsonl", ".md", ".tex", ".txt"}
PRIVATE_PATTERNS = (
    re.compile(r"(?i)c:[\\/]users[\\/]"),
    re.compile(r"(?i)c:[\\/]il_github"),
    re.compile(r"(?i)appdata[\\/]local"),
    re.compile(r"(?i)\\." + "co" + "dex" + r"[\\/]"),
    re.compile(r"(?i)" + "chat" + "notes"),
    re.compile(r"(?i)(?:clau" + "de|co" + "dex|chat" + "gpt)"),
    re.compile(r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b"),
)


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def identity(path: Path) -> tuple[int, str]:
    return path.stat().st_size, sha256_path(path)


def require_identity(path: Path, expected: tuple[int, str]) -> None:
    observed = identity(path)
    if observed != expected:
        raise RuntimeError(f"Identity mismatch for {path}: {observed!r}")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def write_json(path: Path, value: object) -> None:
    write_text(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def copy_exact(source: Path, target: Path, expected: tuple[int, str]) -> None:
    require_identity(source, expected)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    require_identity(target, expected)


def png_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        raise RuntimeError(f"Not a PNG: {path}")
    return struct.unpack(">II", header[16:24])


def issue_ids_for_crop(name: str) -> str:
    if name.startswith("p129_"):
        return "R1"
    if name.startswith("p130_"):
        return "R2"
    if name.startswith("p131_") or name.startswith("p132_additional_G_"):
        return "A1"
    if name.startswith("p132_referral3_"):
        return "R3"
    raise RuntimeError(f"Unclassified crop: {name}")


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


def scan_privacy(root: Path) -> list[dict[str, object]]:
    hits: list[dict[str, object]] = []
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        for pattern in PRIVATE_PATTERNS:
            for match in pattern.finditer(text):
                hits.append(
                    {
                        "path": path.relative_to(root).as_posix(),
                        "pattern": pattern.pattern,
                        "offset": match.start(),
                    }
                )
    return hits


def pdf_report(path: Path) -> dict[str, object]:
    reader = PdfReader(path)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    metadata = {str(key): str(value) for key, value in (reader.metadata or {}).items()}
    privacy_hits = []
    joined = json.dumps(metadata, ensure_ascii=False) + "\n" + text
    for pattern in PRIVATE_PATTERNS:
        if pattern.search(joined):
            privacy_hits.append(pattern.pattern)
    return {
        "pages": len(reader.pages),
        "encrypted": bool(reader.is_encrypted),
        "metadata": metadata,
        "extracted_text_characters": len(text),
        "privacy_hits": privacy_hits,
    }


def csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\r\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def inner_readme() -> str:
    return """# Deligne D001 bilingual source-aligned checkpoint

This package preserves a complete corrected French edition, a complete English
translation, and an eight-page bilingual reader of Pierre Deligne's
*Congruences sur le nombre de sous-groupes d'ordre p^k dans un groupe fini*.
Coverage is the complete four-page paper, printed pages 129-132, through EOF.

The IAS scan identified in `RIGHTS_AND_PROVENANCE.md` is the controlling source.
The scan itself is not bundled. Four source defects are disclosed in both
language editions and in `controls/SOURCE_DEFECT_REGISTER.csv`; the source text
has not been silently normalized. Exact arithmetic checks are in
`controls/D001_SOURCE_MATH_CHECKS.json`.

The visual-evidence directory contains only the 14 decisive 2400-9600 dpi crops
used to adjudicate the disputed formulas and glyphs. The accompanying CSV and
JSONL ledgers bind each crop to the parent scan hash, PDF and printed page,
bounding box, dimensions, DPI, issue ID, and crop hash. These crops are source
evidence, not rendered copies of the reconstructed reader.

Start with
`build/bilingual_source_aligned_eof_r1/D001_Congruences_Bilingual_Reader.pdf`.
The three files in `tex` are the editable source closure. Their original
relative build topology is preserved byte-for-byte. This is a scholarly working
edition and translation, not a critical edition, peer review, mathematical
certification, accessibility certification, or new license grant.
"""


def rights_text() -> str:
    return f"""# Rights and provenance

## Controlling source

- Work: Pierre Deligne, *Congruences sur le nombre de sous-groupes d'ordre p^k
  dans un groupe fini*.
- Source witness: publicly accessible IAS scan, four PDF pages, printed pages
  129-132.
- Archive-neutral source name: `{AUTHORITY_NAME}`.
- Source bytes: {AUTHORITY_BYTES:,}.
- Source SHA-256: `{AUTHORITY_SHA256}`.
- Source role: sole page, formula, glyph, and layout authority for this package.
- OCR role: locator only; no OCR body is bundled or promoted as authority.

The source PDF is not redistributed here. Fourteen tightly bounded crops from
that public scan are included because they are the decisive source evidence for
the four disclosed repairs. Their exact page, bounding box, dimensions, DPI,
and identities are recorded in the visual-evidence ledgers.

## Claim boundary

The package provides public working access to reconstructed French and English
readers, editable TeX, exact source-defect disclosures, machine checks, and
decisive source crops. It does not assert a new license over Deligne's work or
the source scan, and it is not a critical edition, peer review, mathematical
certification, accessibility certification, or legal determination. Rights in
the underlying work and scan remain with their respective holders.
"""


def build_qa_text() -> str:
    return """# Build and QA summary

Date: 2026-08-01

Status: `PASS_SOURCE_ALIGNED_WORKING_RELEASE`

- Corrected French: four A4 pages; four XeLaTeX passes; required diagnostics 0.
- English translation: four A4 pages; four XeLaTeX passes; required diagnostics 0.
- Bilingual reader: eight A4 pages; four XeLaTeX passes; required diagnostics 0.
- Pass-3 and pass-4 console output was byte-identical for each reader.
- Bilingual PDF: unencrypted; two language outline entries; no page annotations
  or external actions.
- All eight bilingual pages were rendered at 600 dpi and inspected for compiled
  layout. No blank page, clipping, overlap, missing glyph, or language-seam
  defect was found. Those output renders are intentionally not bundled.
- Source reading used direct 1200-1800 dpi page renders and the bundled decisive
  2400/5600/9600 dpi crops. Every bundled crop is identity- and coordinate-bound.
- Four source defects R1, R2, R3, and A1 have exact machine checks and visible
  disclosure in both corrected language editions.
"""


def outer_readme() -> str:
    return """# Deligne D001 source-aligned bilingual release

This GitHub package mirrors the exact reader and artifact files proposed for
the existing Deligne Zenodo concept. It adds one complete source-aligned paper:

- a direct bilingual PDF;
- direct English and corrected-French PDFs;
- one compact TeX/source-evidence ZIP containing editable source, exact repair
  controls, and 14 decisive 2400-9600 dpi scan crops.

The source scan itself, raw build logs, auxiliaries, low-value output renders,
private paths, and workflow chatter are excluded. This release does not replace
the broader Deligne cumulative readers and makes no whole-corpus claim.
"""


def outer_provenance() -> str:
    return f"""# Scope and provenance

- Exact scope: Deligne D001, complete paper, printed pages 129-132, EOF.
- Authority: publicly accessible four-page IAS scan, {AUTHORITY_BYTES:,} bytes,
  SHA-256 `{AUTHORITY_SHA256}`; source PDF not bundled.
- Public evidence: 14 tightly bounded decisive source crops at 2400-9600 dpi.
- Public readers: corrected French, English translation, and bilingual reader.
- Source repairs: R1, R2, R3, and A1, visibly disclosed and machine-checked.
- Claim boundary: source-aligned scholarly working edition and translation; not
  a whole-corpus completion, critical edition, peer review, certification, or
  new license grant.
- Zenodo route: existing Deligne concept DOI `10.5281/zenodo.20410853` only.
"""


def build_inner_package(
    checkpoint_root: Path,
    evidence_root: Path,
    results_root: Path,
    staging: Path,
) -> dict[str, object]:
    for relative, wanted in SOURCE_INPUTS.items():
        source = checkpoint_root / relative
        target = staging / relative
        copy_exact(source, target, wanted)

    for public_name, (relative, size, digest, pages, _role) in PUBLIC_FILES.items():
        source = checkpoint_root / relative
        require_identity(source, (size, digest))
        reader_name = Path(relative).name
        target = staging / relative
        copy_exact(source, target, (size, digest))
        report = pdf_report(target)
        if report["pages"] != pages or report["encrypted"] or report["privacy_hits"]:
            raise RuntimeError(f"PDF gate failed for {reader_name}: {report!r}")

    manifest_path = results_root / "decisive_scan_crops_manifest.json"
    require_identity(manifest_path, CROP_MANIFEST_IDENTITY)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if (
        manifest.get("source_sha256") != AUTHORITY_SHA256
        or len(manifest.get("crops", [])) != 14
    ):
        raise RuntimeError("Decisive-crop manifest boundary changed")

    visual_rows: list[dict[str, object]] = []
    for crop in manifest["crops"]:
        source = evidence_root / "decisive_scan_crops" / Path(crop["output"]).name
        wanted_sha = str(crop["sha256"]).upper()
        if sha256_path(source) != wanted_sha:
            raise RuntimeError(f"Crop changed: {source.name}")
        width, height = png_dimensions(source)
        if [width, height] != crop["pixel_dimensions"]:
            raise RuntimeError(f"Crop dimensions changed: {source.name}")
        target_relative = f"visual_evidence/decisive_scan_crops/{source.name}"
        target = staging / target_relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        if sha256_path(target) != wanted_sha:
            raise RuntimeError(f"Copied crop changed: {source.name}")
        issue_ids = issue_ids_for_crop(str(crop["name"]))
        visual_rows.append(
            {
                "witness_id": f"D001-{crop['name'].upper().replace('-', '_')}",
                "relative_path": target_relative,
                "parent_source_filename": AUTHORITY_NAME,
                "parent_source_bytes": AUTHORITY_BYTES,
                "parent_source_sha256": AUTHORITY_SHA256,
                "authority_pdf_page": crop["page"],
                "printed_page": crop["printed"],
                "bbox_points_top_left": json.dumps(crop["box"], separators=(",", ":")),
                "page_rect_points": json.dumps(crop["page_rect_points"], separators=(",", ":")),
                "normalized_bbox": json.dumps(crop["normalized_box"], separators=(",", ":")),
                "dpi": crop["dpi"],
                "width_pixels": width,
                "height_pixels": height,
                "rotation_degrees": 0,
                "crop_bytes": source.stat().st_size,
                "crop_sha256": wanted_sha,
                "linked_issue_ids": issue_ids,
                "linked_tex_files": "tex/D001_Congruences_FR_source_aligned.tex;tex/D001_Congruences_EN_source_aligned.tex",
                "qa_disposition": "USED_IN_SOURCE_ALIGNMENT_AND_SOURCE_DEFECT_ADJUDICATION",
                "public_disposition": "PUBLIC_SCAN_DERIVED_DECISIVE_CROP",
                "purpose": crop["purpose"],
            }
        )

    visual_fields = list(visual_rows[0])
    write_csv(staging / "visual_evidence/VISUAL_EVIDENCE_INDEX.csv", visual_fields, visual_rows)
    write_text(
        staging / "visual_evidence/VISUAL_EVIDENCE_INDEX.jsonl",
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in visual_rows),
    )
    write_text(staging / "README.md", inner_readme())
    write_text(staging / "RIGHTS_AND_PROVENANCE.md", rights_text())
    write_text(staging / "BUILD_AND_QA.md", build_qa_text())

    content_files = sorted(
        path
        for path in staging.rglob("*")
        if path.is_file() and path.name not in {"SHA256SUMS.csv", "PACKAGE_VALIDATION.json"}
    )
    checksum_rows = [
        {
            "relative_path": path.relative_to(staging).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
        }
        for path in content_files
    ]
    write_csv(
        staging / "SHA256SUMS.csv",
        ["relative_path", "bytes", "sha256"],
        checksum_rows,
    )
    privacy_hits = scan_privacy(staging)
    if privacy_hits:
        raise RuntimeError(f"Privacy scan failed: {privacy_hits[:3]}")
    json_errors = []
    for path in sorted(staging.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8-sig"))
        except Exception as exc:  # pragma: no cover - explicit release gate
            json_errors.append({"path": path.name, "error": str(exc)})
    if json_errors:
        raise RuntimeError(f"JSON parse failed: {json_errors}")
    validation = {
        "status": "PASS_READY_FOR_ARCHIVE_PUBLICATION",
        "scope": "Deligne D001 complete bilingual source-aligned working edition through EOF",
        "authority": {
            "filename": AUTHORITY_NAME,
            "bytes": AUTHORITY_BYTES,
            "sha256": AUTHORITY_SHA256,
            "included": False,
        },
        "content_manifest": {
            "rows": len(checksum_rows),
            "bytes": (staging / "SHA256SUMS.csv").stat().st_size,
            "sha256": sha256_path(staging / "SHA256SUMS.csv"),
        },
        "decisive_visual_evidence": {
            "rows": len(visual_rows),
            "files": len(visual_rows),
            "dpi_min": min(int(row["dpi"]) for row in visual_rows),
            "dpi_max": max(int(row["dpi"]) for row in visual_rows),
            "source_render_copies": 0,
        },
        "source_defect_rows": len(csv_rows(staging / "controls/SOURCE_DEFECT_REGISTER.csv")),
        "reader_pdfs": {
            path.name: pdf_report(path)
            for path in sorted((staging / "build").rglob("*.pdf"))
        },
        "privacy_hits": privacy_hits,
        "json_errors": json_errors,
        "errors": [],
    }
    write_json(staging / "PACKAGE_VALIDATION.json", validation)
    if scan_privacy(staging):
        raise RuntimeError("Privacy scan changed after validation write")
    return validation


def deterministic_zip(source_root: Path, output: Path) -> dict[str, object]:
    output.parent.mkdir(parents=True, exist_ok=True)
    files = sorted(path for path in source_root.rglob("*") if path.is_file())
    with zipfile.ZipFile(
        output,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        strict_timestamps=True,
    ) as archive:
        for path in files:
            member = f"{ZIP_ROOT}/{path.relative_to(source_root).as_posix()}"
            if not safe_member(member):
                raise RuntimeError(f"Unsafe ZIP member: {member}")
            info = zipfile.ZipInfo(member, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    with zipfile.ZipFile(output) as archive:
        infos = [item for item in archive.infolist() if not item.is_dir()]
        names = [item.filename for item in infos]
        if (
            archive.testzip() is not None
            or len(names) != len(set(names))
            or not all(safe_member(name) for name in names)
        ):
            raise RuntimeError("ZIP replay failed")
        return {
            "members": len(infos),
            "uncompressed_bytes": sum(item.file_size for item in infos),
            "bytes": output.stat().st_size,
            "sha256": sha256_path(output),
        }


def build(args: argparse.Namespace) -> dict[str, object]:
    checkpoint_root = args.checkpoint_root.resolve()
    evidence_root = args.evidence_root.resolve()
    results_root = args.results_root.resolve()
    output_root = args.output_root.resolve()
    if output_root.exists():
        raise RuntimeError(f"Output already exists: {output_root}")
    output_root.mkdir(parents=True)
    public_root = output_root / "public_files"
    public_root.mkdir()

    for public_name, (relative, size, digest, pages, _role) in PUBLIC_FILES.items():
        source = checkpoint_root / relative
        target = public_root / public_name
        copy_exact(source, target, (size, digest))
        report = pdf_report(target)
        if report["pages"] != pages or report["encrypted"] or report["privacy_hits"]:
            raise RuntimeError(f"Public PDF gate failed: {public_name}")

    with tempfile.TemporaryDirectory(prefix="deligne-d001-public-") as temp:
        staging = Path(temp) / ZIP_ROOT
        staging.mkdir(parents=True)
        inner_validation = build_inner_package(
            checkpoint_root, evidence_root, results_root, staging
        )
        zip_name = "08_Deligne_D001_TeX_and_Decisive_Source_Crops_20260801.zip"
        zip_report = deterministic_zip(staging, public_root / zip_name)

    write_text(output_root / "README.md", outer_readme())
    write_text(output_root / "PROVENANCE_AND_SCOPE.md", outer_provenance())
    upload_rows: list[dict[str, object]] = []
    for public_name, (_relative, _size, _digest, pages, role) in PUBLIC_FILES.items():
        path = public_root / public_name
        upload_rows.append(
            {
                "filename": public_name,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
                "role": role,
                "scope": "Deligne D001 complete through EOF",
                "pages": pages,
                "zenodo_action": "additive_same_concept_upload",
            }
        )
    zip_path = public_root / "08_Deligne_D001_TeX_and_Decisive_Source_Crops_20260801.zip"
    upload_rows.append(
        {
            "filename": zip_path.name,
            "bytes": zip_path.stat().st_size,
            "sha256": sha256_path(zip_path),
            "role": "tex_source_math_checks_and_decisive_source_crops",
            "scope": "Deligne D001 complete through EOF",
            "pages": "",
            "zenodo_action": "additive_same_concept_upload",
        }
    )
    write_csv(
        output_root / "ZENODO_UPLOAD_MANIFEST.csv",
        ["filename", "bytes", "sha256", "role", "scope", "pages", "zenodo_action"],
        upload_rows,
    )
    checksum_targets = sorted(
        path
        for path in output_root.rglob("*")
        if path.is_file() and path.name not in {"SHA256SUMS.csv", "PACKAGE_VALIDATION.json"}
    )
    checksum_rows = [
        {
            "relative_path": path.relative_to(output_root).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256_path(path),
        }
        for path in checksum_targets
    ]
    write_csv(
        output_root / "SHA256SUMS.csv",
        ["relative_path", "bytes", "sha256"],
        checksum_rows,
    )
    privacy_hits = scan_privacy(output_root)
    if privacy_hits:
        raise RuntimeError(f"Outer privacy scan failed: {privacy_hits[:3]}")
    validation = {
        "status": "PASS_READY_FOR_GITHUB_AND_SINGLE_EXISTING_CONCEPT_SUCCESSOR",
        "concept_doi": "10.5281/zenodo.20410853",
        "proposed_upload_files": len(upload_rows),
        "proposed_upload_bytes": sum(int(row["bytes"]) for row in upload_rows),
        "upload_manifest": {
            "rows": len(upload_rows),
            "bytes": (output_root / "ZENODO_UPLOAD_MANIFEST.csv").stat().st_size,
            "sha256": sha256_path(output_root / "ZENODO_UPLOAD_MANIFEST.csv"),
        },
        "repository_manifest": {
            "rows": len(checksum_rows),
            "bytes": (output_root / "SHA256SUMS.csv").stat().st_size,
            "sha256": sha256_path(output_root / "SHA256SUMS.csv"),
        },
        "artifact_zip": zip_report,
        "inner_validation": inner_validation,
        "privacy_hits": privacy_hits,
        "duplicate_concept_authorized": False,
        "errors": [],
    }
    write_json(output_root / "PACKAGE_VALIDATION.json", validation)
    if scan_privacy(output_root):
        raise RuntimeError("Outer privacy scan changed after validation write")
    validation["package_tree"] = {
        "files": sum(1 for path in output_root.rglob("*") if path.is_file()),
        "bytes": sum(path.stat().st_size for path in output_root.rglob("*") if path.is_file()),
    }
    return validation


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint-root", type=Path, required=True)
    parser.add_argument("--evidence-root", type=Path, required=True)
    parser.add_argument("--results-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    print(json.dumps(build(args), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
