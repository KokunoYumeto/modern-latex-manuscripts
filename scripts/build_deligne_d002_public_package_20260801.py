#!/usr/bin/env python3
"""Build the privacy-clean Deligne D002 reader and source-evidence package."""

from __future__ import annotations

import argparse
import json
import shutil
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

import build_deligne_d001_public_package_20260801 as base


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / "sources/deligne/d002-bilingual-source-aligned-20260801"
ZIP_ROOT = "Deligne_D002_Bilingual_SourceAligned_20260801"

AUTHORITY_NAME = "Cohomologie_support_propre_foncteur_f_shriek_IAS_scan.pdf"
AUTHORITY_BYTES = 745_800
AUTHORITY_PAGES = 18
AUTHORITY_SHA256 = "613CB973E466DD5ED414335B6C86B5E04E3E6138DCC607C638F235B2AE6A44A9"

PUBLIC_FILES = {
    "09_Deligne_D002_Bilingual_SourceAligned_Reader_20260801.pdf": (
        "build/bilingual_source_aligned_eof_r1/D002_ProperSupport_Bilingual_Reader.pdf",
        222_429,
        "F272A0CAEF2853469A4AAEE29C6FF6F066818772364CD1BE0D635B73DAAE5F37",
        24,
        "bilingual_reader",
    ),
    "10_Deligne_D002_English_SourceAligned_20260801.pdf": (
        "build/en_final/D002_ProperSupport_EN_source_aligned.pdf",
        106_630,
        "BDE6B832859555994F889C0CFDA7642B8D6848A1D4907503B6A52B3A0C3E2C71",
        12,
        "english_reader",
    ),
    "11_Deligne_D002_French_SourceAligned_20260801.pdf": (
        "build/fr_final/D002_ProperSupport_FR_source_aligned.pdf",
        106_349,
        "6DE66CDAD91E61756EA228D48AAD413C8287A8AC2A6B825D7E3B33B90325F345",
        12,
        "french_reader",
    ),
}

SOURCE_INPUTS = {
    "tex/D002_ProperSupport_Bilingual_Reader.tex": (
        731,
        "A97C0F4AC69EEEC61D0A4D5D81577C1C6DDB7A88F94181F6BE99668C11A2F8EE",
    ),
    "tex/D002_ProperSupport_EN_source_aligned.tex": (
        28_099,
        "B78354B3ED9637008A8687312EF61EB5095BA6651A1A0BC385738E202EC6F1C6",
    ),
    "tex/D002_ProperSupport_FR_source_aligned.tex": (
        29_971,
        "2EB15D430385807CBAC58CB9F67AF28C047FA63E4CB00A9DF45074672C115889",
    ),
    "controls/D002_SOURCE_ALIGNMENT_CORRECTIONS.csv": (
        4_034,
        "51BA053BDC5B6B9E1ABA096DA5B10B9572EED9BFDD0F26126A7A9FEC24B0741A",
    ),
    "controls/D002_SOURCE_ALIGNMENT_REPORT.md": (
        3_364,
        "C955EF8B4D33671A164738F43FDE690D6B48D533553A35247E835DBA0D60BC6C",
    ),
    "controls/FINAL_LOCAL_VALIDATION.json": (
        1_763,
        "7303B6DA7FF7FBDFD5671112754FD01C10DE3A721DC79517621A3F8E4B9F3CC7",
    ),
    "qa/D002_BILINGUAL_EOF_BUILD_RENDER_PASS.md": (
        1_238,
        "A971282AF3E01F46DDAA8B5E4E2A1CF3CE3DCD325F372BA9BEE452D289FF8824",
    ),
}

CROPS = (
    {
        "source_kind": "checkpoint",
        "source_relative": "qa/authority_renders/D002_p411_diagram_5000dpi_equiv.png",
        "public_name": "D002_p411_cech_exactness_diagram.png",
        "bytes": 417_192,
        "sha256": "BA77793803C6E3AC23B1923E9B1FE067F7EECB67A96F97BE2C0A544222422EBC",
        "dimensions": [35_000, 12_500],
        "authority_pdf_page": 8,
        "printed_page": 411,
        "bbox": [600, 2800, 9000, 5800],
        "review_equivalent_dpi": 5000,
        "resampling": "1200-dpi crop enlarged 416.6667 percent and thresholded for inspection",
        "correction_ids": "D002-C004",
        "purpose": "Complete two-row Cech exactness diagram and all arrow/term readings",
    },
    {
        "source_kind": "checkpoint",
        "source_relative": "qa/authority_renders/D002_p413_compactification_diagrams_5000dpi_equiv.png",
        "public_name": "D002_p413_compactification_diagrams.png",
        "bytes": 325_767,
        "sha256": "502B10C7D0162E0147034BEAB815A463D0D5B7F86190C1D319EB8AC143E521B2",
        "dimensions": [36_667, 12_917],
        "authority_pdf_page": 10,
        "printed_page": 413,
        "bbox": [400, 500, 9200, 3600],
        "review_equivalent_dpi": 5000,
        "resampling": "1200-dpi crop enlarged 416.6667 percent and thresholded for inspection",
        "correction_ids": "D002-C005",
        "purpose": "Full two-stage and three-stage compactification towers",
    },
    {
        "source_kind": "legacy_crop",
        "source_relative": "D002_p415_compatibility_diagram_formulas.png",
        "public_name": "D002_p415_comparison_diagram_and_formulas.png",
        "bytes": 344_320,
        "sha256": "33E84B92958DC2C83A46AEE379BB31A33BF3195398A7BADB5DB88D424BEE945B",
        "dimensions": [8_600, 5_200],
        "authority_pdf_page": 12,
        "printed_page": 415,
        "bbox": [500, 2200, 9100, 7400],
        "review_equivalent_dpi": 1200,
        "resampling": "direct 1200-dpi source crop; no enlargement in the packaged pixels",
        "correction_ids": "D002-C007;D002-C008;D002-C009",
        "purpose": "Comparison-diagram topology and the complete compatibility-chain context",
    },
    {
        "source_kind": "checkpoint",
        "source_relative": "qa/authority_renders/D002_p415_formula_detail_full_9000dpi_equiv.png",
        "public_name": "D002_p415_compatibility_chain_detail.png",
        "bytes": 87_053,
        "sha256": "19743A949CBCA72F2F5A6F451E92C929A3F75AC42C680F9BBD49F47D4AD74810",
        "dimensions": [6_100, 2_000],
        "authority_pdf_page": 12,
        "printed_page": 415,
        "bbox": [2950, 2200, 9050, 4200],
        "review_equivalent_dpi": 9000,
        "resampling": "direct 1200-dpi source crop; 9000-dpi-equivalent display inspection only",
        "correction_ids": "D002-C008;D002-C009",
        "purpose": "First and terminal terms of the four-step compatibility chain",
    },
)


def normalized_bbox(box: list[int]) -> str:
    width, height = 9_600, 13_084
    values = [box[0] / width, box[1] / height, box[2] / width, box[3] / height]
    return json.dumps([round(value, 8) for value in values], separators=(",", ":"))


def safe_member(name: str) -> bool:
    pure = PurePosixPath(name)
    return (
        name == name.replace("\\", "/")
        and not pure.is_absolute()
        and ".." not in pure.parts
        and not (len(name) > 1 and name[1] == ":")
    )


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
            archive.writestr(
                info,
                path.read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )
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
            "sha256": base.sha256_path(output),
        }


def inner_readme() -> str:
    return """# Deligne D002 bilingual source-aligned checkpoint

Start with `build/bilingual_source_aligned_eof_r1/D002_ProperSupport_Bilingual_Reader.pdf`.
It contains the complete corrected-French and English readers of Pierre
Deligne's *Cohomologie a support propre et construction du foncteur f!*.
Coverage is the complete eighteen-page paper, printed pages 404-421, through
the terminal bibliography.

The three files in `tex` are the complete editable source closure. Twelve
source-alignment decisions are recorded in
`controls/D002_SOURCE_ALIGNMENT_CORRECTIONS.csv`; the source-surprising final
term on printed page 415 is retained and disclosed rather than silently
normalized.

The four images in `visual_evidence/source_crops` are the decisive source crops
used for the diagram and formula decisions on printed pages 411, 413, and 415.
They are not page renders of the reconstructed reader. Their ledger binds each
crop to the parent scan hash, PDF and printed page, 1200-dpi source-render
coordinates, dimensions, review presentation scale, correction IDs, and crop
hash. The source PDF, full-page renders, output screenshots, raw logs, and build
auxiliaries are not bundled.

This is a source-aligned scholarly working edition and translation, not a
critical edition, peer review, mathematical certification, accessibility
certification, or new license grant.
"""


def rights_text() -> str:
    return f"""# Rights and provenance

- Work: Pierre Deligne, *Cohomologie a support propre et construction du
  foncteur f!*.
- Controlling witness: publicly accessible IAS scan, {AUTHORITY_PAGES} PDF
  pages, printed pages 404-421.
- Archive-neutral witness name: `{AUTHORITY_NAME}`.
- Witness bytes: {AUTHORITY_BYTES:,}.
- Witness SHA-256: `{AUTHORITY_SHA256}`.
- Source role: sole page, formula, glyph, and layout authority for this package.
- OCR role: locator only; no OCR body is bundled or promoted as authority.

The complete source PDF is not redistributed in this package. Four tightly
bounded source crops are included as the decisive evidence for reconstructed
diagrams and the page-415 compatibility chain. The visual-evidence ledgers
record source-render coordinates and distinguish the true 1200-dpi source
render from higher inspection-presentation scales.

This package does not assert a new license over Deligne's work or the IAS scan.
Rights in the underlying work and source witness remain with their respective
holders. The package is a scholarly working edition and translation, not a
critical edition, peer review, mathematical certification, accessibility
certification, or legal determination.
"""


def build_qa_text() -> str:
    return """# Build and QA summary

Date: 2026-08-01

Status: `PASS_SOURCE_ALIGNED_WORKING_RELEASE`

- Corrected French: twelve A4 pages; three stable XeLaTeX passes.
- English translation: twelve A4 pages; three stable XeLaTeX passes.
- Bilingual reader: twenty-four A4 pages; four stable XeLaTeX passes and two
  language outline entries.
- Blocking build diagnostics, duplicate destinations, and missing glyphs: 0.
- All component pages and all twenty-four bilingual pages were rendered at 600
  dpi and inspected. No blank page, clipping, overlap, broken vector diagram,
  seam error, or terminal-page cutoff was found. Output renders are not bundled.
- All diagrams are native vector TeX/Xy-pic. Raster image objects: 0. Type 3
  fonts: 0; all fonts embedded.
- Twelve source-alignment decisions close, including restored source notes,
  reconstructed compactification/comparison diagrams, corrected limit
  direction and subscripts, and one visibly retained source anomaly.
"""


def outer_readme() -> str:
    return """# Deligne D002 source-aligned bilingual release

This package mirrors four compact objects for the existing Deligne archive:

1. the complete bilingual reader;
2. the complete English reader;
3. the complete corrected-French reader;
4. one TeX/source-evidence ZIP with editable source, exact correction controls,
   build QA, and four decisive source crops.

The source scan, full-page source renders, output screenshots, raw logs,
auxiliaries, private paths, and workflow files are excluded. This release adds
one complete paper and does not replace or claim completion of the broader
Deligne corpus.
"""


def outer_provenance() -> str:
    return f"""# Scope and provenance

- Exact scope: Deligne D002, complete paper, printed pages 404-421, EOF.
- Authority: publicly accessible {AUTHORITY_PAGES}-page IAS scan,
  {AUTHORITY_BYTES:,} bytes, SHA-256 `{AUTHORITY_SHA256}`; source PDF excluded.
- Public readers: corrected French, English translation, and bilingual reader.
- Public visual evidence: four tightly bounded decisive source crops on printed
  pages 411, 413, and 415, with parent hash and coordinate ledgers.
- Source alignment: twelve explicit decisions; the source-surprising page-415
  terminal term is retained and disclosed.
- Claim boundary: source-aligned scholarly working edition and translation; not
  a whole-corpus completion, critical edition, peer review, certification, or
  new license grant.
- Zenodo route: existing Deligne concept DOI `10.5281/zenodo.20410853` only.
"""


def build_inner_package(
    checkpoint_root: Path,
    legacy_crop_root: Path,
    staging: Path,
) -> dict[str, object]:
    for relative, wanted in SOURCE_INPUTS.items():
        base.copy_exact(checkpoint_root / relative, staging / relative, wanted)

    reader_reports: dict[str, object] = {}
    for _public_name, (relative, size, digest, pages, _role) in PUBLIC_FILES.items():
        target = staging / relative
        base.copy_exact(checkpoint_root / relative, target, (size, digest))
        report = base.pdf_report(target)
        if report["pages"] != pages or report["encrypted"] or report["privacy_hits"]:
            raise RuntimeError(f"PDF gate failed for {relative}: {report!r}")
        reader_reports[relative] = report

    visual_rows: list[dict[str, object]] = []
    for crop in CROPS:
        if crop["source_kind"] == "checkpoint":
            source = checkpoint_root / str(crop["source_relative"])
        else:
            source = legacy_crop_root / str(crop["source_relative"])
        wanted = (int(crop["bytes"]), str(crop["sha256"]))
        base.require_identity(source, wanted)
        if list(base.png_dimensions(source)) != list(crop["dimensions"]):
            raise RuntimeError(f"Crop dimensions changed: {source}")
        target_relative = f"visual_evidence/source_crops/{crop['public_name']}"
        target = staging / target_relative
        base.copy_exact(source, target, wanted)
        box = list(crop["bbox"])
        visual_rows.append(
            {
                "witness_id": f"D002-W{len(visual_rows) + 1:03d}",
                "relative_path": target_relative,
                "parent_source_filename": AUTHORITY_NAME,
                "parent_source_bytes": AUTHORITY_BYTES,
                "parent_source_sha256": AUTHORITY_SHA256,
                "authority_pdf_page": crop["authority_pdf_page"],
                "printed_page": crop["printed_page"],
                "embedded_source_page_dimensions": "2400x3270",
                "source_render_dimensions": "9600x13084",
                "source_render_dpi": 1200,
                "bbox_source_render_pixels": json.dumps(box, separators=(",", ":")),
                "normalized_bbox": normalized_bbox(box),
                "review_equivalent_dpi": crop["review_equivalent_dpi"],
                "resampling_disclosure": crop["resampling"],
                "width_pixels": crop["dimensions"][0],
                "height_pixels": crop["dimensions"][1],
                "rotation_degrees": 0,
                "crop_bytes": crop["bytes"],
                "crop_sha256": crop["sha256"],
                "linked_correction_ids": crop["correction_ids"],
                "linked_tex_files": "tex/D002_ProperSupport_FR_source_aligned.tex;tex/D002_ProperSupport_EN_source_aligned.tex",
                "qa_disposition": "USED_IN_SOURCE_ALIGNMENT_AND_DIAGRAM_FORMULA_ADJUDICATION",
                "public_disposition": "PUBLIC_SCAN_DERIVED_DECISIVE_CROP",
                "purpose": crop["purpose"],
            }
        )

    fields = list(visual_rows[0])
    base.write_csv(staging / "visual_evidence/VISUAL_EVIDENCE_INDEX.csv", fields, visual_rows)
    base.write_text(
        staging / "visual_evidence/VISUAL_EVIDENCE_INDEX.jsonl",
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in visual_rows),
    )
    base.write_text(staging / "README.md", inner_readme())
    base.write_text(staging / "RIGHTS_AND_PROVENANCE.md", rights_text())
    base.write_text(staging / "BUILD_AND_QA.md", build_qa_text())

    content_files = sorted(
        path
        for path in staging.rglob("*")
        if path.is_file() and path.name not in {"SHA256SUMS.csv", "PACKAGE_VALIDATION.json"}
    )
    checksum_rows = [
        {
            "relative_path": path.relative_to(staging).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": base.sha256_path(path),
        }
        for path in content_files
    ]
    base.write_csv(staging / "SHA256SUMS.csv", ["relative_path", "bytes", "sha256"], checksum_rows)
    privacy_hits = base.scan_privacy(staging)
    if privacy_hits:
        raise RuntimeError(f"Privacy scan failed: {privacy_hits[:3]}")
    validation = {
        "status": "PASS_READY_FOR_ARCHIVE_PUBLICATION",
        "scope": "Deligne D002 complete bilingual source-aligned working edition through EOF",
        "authority": {
            "filename": AUTHORITY_NAME,
            "bytes": AUTHORITY_BYTES,
            "pages": AUTHORITY_PAGES,
            "sha256": AUTHORITY_SHA256,
            "included": False,
        },
        "content_manifest": {
            "rows": len(checksum_rows),
            "bytes": (staging / "SHA256SUMS.csv").stat().st_size,
            "sha256": base.sha256_path(staging / "SHA256SUMS.csv"),
        },
        "decisive_visual_evidence": {
            "rows": len(visual_rows),
            "files": len(visual_rows),
            "source_render_dpi": 1200,
            "review_equivalent_dpi_min": min(int(row["review_equivalent_dpi"]) for row in visual_rows),
            "review_equivalent_dpi_max": max(int(row["review_equivalent_dpi"]) for row in visual_rows),
            "full_page_source_renders": 0,
            "output_reader_renders": 0,
        },
        "source_alignment_rows": len(base.csv_rows(staging / "controls/D002_SOURCE_ALIGNMENT_CORRECTIONS.csv")),
        "reader_pdfs": reader_reports,
        "privacy_hits": privacy_hits,
        "errors": [],
    }
    base.write_json(staging / "PACKAGE_VALIDATION.json", validation)
    if base.scan_privacy(staging):
        raise RuntimeError("Privacy scan changed after validation write")
    return validation


def build(args: argparse.Namespace) -> dict[str, object]:
    checkpoint_root = args.checkpoint_root.resolve()
    legacy_crop_root = args.legacy_crop_root.resolve()
    authority_pdf = args.authority_pdf.resolve()
    output_root = args.output_root.resolve()
    base.require_identity(authority_pdf, (AUTHORITY_BYTES, AUTHORITY_SHA256))
    authority_report = base.pdf_report(authority_pdf)
    if authority_report["pages"] != AUTHORITY_PAGES:
        raise RuntimeError(f"Authority page count changed: {authority_report!r}")
    if output_root.exists():
        raise RuntimeError(f"Output already exists: {output_root}")
    public_root = output_root / "public_files"
    public_root.mkdir(parents=True)

    for public_name, (relative, size, digest, pages, _role) in PUBLIC_FILES.items():
        target = public_root / public_name
        base.copy_exact(checkpoint_root / relative, target, (size, digest))
        report = base.pdf_report(target)
        if report["pages"] != pages or report["encrypted"] or report["privacy_hits"]:
            raise RuntimeError(f"Public PDF gate failed: {public_name}")

    with tempfile.TemporaryDirectory(prefix="deligne-d002-public-") as temp:
        staging = Path(temp) / ZIP_ROOT
        staging.mkdir(parents=True)
        inner_validation = build_inner_package(checkpoint_root, legacy_crop_root, staging)
        zip_name = "12_Deligne_D002_TeX_and_Decisive_Source_Crops_20260801.zip"
        zip_report = deterministic_zip(staging, public_root / zip_name)

    base.write_text(output_root / "README.md", outer_readme())
    base.write_text(output_root / "PROVENANCE_AND_SCOPE.md", outer_provenance())
    upload_rows: list[dict[str, object]] = []
    for public_name, (_relative, _size, _digest, pages, role) in PUBLIC_FILES.items():
        path = public_root / public_name
        upload_rows.append(
            {
                "filename": public_name,
                "bytes": path.stat().st_size,
                "sha256": base.sha256_path(path),
                "role": role,
                "scope": "Deligne D002 complete through EOF",
                "pages": pages,
                "zenodo_action": "additive_same_concept_upload",
            }
        )
    zip_path = public_root / "12_Deligne_D002_TeX_and_Decisive_Source_Crops_20260801.zip"
    upload_rows.append(
        {
            "filename": zip_path.name,
            "bytes": zip_path.stat().st_size,
            "sha256": base.sha256_path(zip_path),
            "role": "tex_source_alignment_and_decisive_source_crops",
            "scope": "Deligne D002 complete through EOF",
            "pages": "",
            "zenodo_action": "additive_same_concept_upload",
        }
    )
    base.write_csv(
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
            "sha256": base.sha256_path(path),
        }
        for path in checksum_targets
    ]
    base.write_csv(output_root / "SHA256SUMS.csv", ["relative_path", "bytes", "sha256"], checksum_rows)
    privacy_hits = base.scan_privacy(output_root)
    if privacy_hits:
        raise RuntimeError(f"Outer privacy scan failed: {privacy_hits[:3]}")
    validation = {
        "status": "PASS_READY_FOR_GITHUB_AND_SINGLE_EXISTING_CONCEPT_SUCCESSOR",
        "concept_doi": "10.5281/zenodo.20410853",
        "authority_identity_verified": True,
        "proposed_upload_files": len(upload_rows),
        "proposed_upload_bytes": sum(int(row["bytes"]) for row in upload_rows),
        "upload_manifest": {
            "rows": len(upload_rows),
            "bytes": (output_root / "ZENODO_UPLOAD_MANIFEST.csv").stat().st_size,
            "sha256": base.sha256_path(output_root / "ZENODO_UPLOAD_MANIFEST.csv"),
        },
        "repository_manifest": {
            "rows": len(checksum_rows),
            "bytes": (output_root / "SHA256SUMS.csv").stat().st_size,
            "sha256": base.sha256_path(output_root / "SHA256SUMS.csv"),
        },
        "artifact_zip": zip_report,
        "inner_validation": inner_validation,
        "privacy_hits": privacy_hits,
        "duplicate_concept_authorized": False,
        "errors": [],
    }
    base.write_json(output_root / "PACKAGE_VALIDATION.json", validation)
    if base.scan_privacy(output_root):
        raise RuntimeError("Outer privacy scan changed after validation write")
    validation["package_tree"] = {
        "files": sum(1 for path in output_root.rglob("*") if path.is_file()),
        "bytes": sum(path.stat().st_size for path in output_root.rglob("*") if path.is_file()),
    }
    return validation


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint-root", type=Path, required=True)
    parser.add_argument("--legacy-crop-root", type=Path, required=True)
    parser.add_argument("--authority-pdf", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    print(json.dumps(build(args), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
