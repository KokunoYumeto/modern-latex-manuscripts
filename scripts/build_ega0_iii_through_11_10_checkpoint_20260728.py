#!/usr/bin/env python3
"""Build the EGA 0 reader with bounded source-first work through section 11.10."""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parent.parent
EGA_ROOT = REPO_ROOT / "sources" / "ega"
PACKAGE_ROOT = (
    EGA_ROOT
    / "checkpoints"
    / "ega0-iii-source-first-through-11-10-working-20260728"
)

PDF_NAME = (
    "00a_EGA0_English_Working_Reader_"
    "SourceFirst_11_5_1_to_11_10_3_20260728.pdf"
)
TEX_NAME = (
    "02a_EGA0_III_Section11_English_"
    "SourceFirst_11_5_1_to_11_10_3_20260728.tex"
)
ZIP_NAME = (
    "10a_EGA0_English_Working_Source_"
    "with_Section11_SourceFirst_20260728.zip"
)

EXPECTED_PDF_SHA256 = (
    "DD5D2923561FD15302630869828AC549FCC370E84524F29E88A6BAEBA074D0BD"
)
EXPECTED_PDF_BYTES = 991_284
EXPECTED_PDF_PAGES = 93
EXPECTED_TEX_SHA256 = (
    "1311E0EECB318C6F3D5525D9846874B42151B8B49903E89E99BC89F4E56B54E7"
)
EXPECTED_TEX_BYTES = 107_199
EXPECTED_BASE_EGA0_12_SHA256 = (
    "E03370D2CB3A0B02568EA664A92529CFB3AA810C3FBA20E79FA3CC6C15BC53DB"
)
EXPECTED_INHERITED_UNDEFINED_HYPERREFS = [
    ".",
    "0.11.4.4",
    "I.2.5.1",
    "I.5.5.6",
    "II.7.1.7",
    "IV.5.4.3",
]

AUTHORITY_NAME = "EGA III Part 1, NUMDAM PMIHES 11 (1961)"
AUTHORITY_BYTES = 19_942_549
AUTHORITY_PAGES = 164
AUTHORITY_SHA256 = (
    "3ED59FE81DA07F1AB685DDC54A93128A364419D4DDAFBC7AFFCD8ABC8B401605"
)

PRIVACY_PATTERNS = (
    b"C:\\Users\\",
    b"C:/Users/",
    b"C:\\IL_GitHub",
    b"C:/IL_GitHub",
    b"AppData\\Local",
    b".codex\\",
    b"Chatnotes",
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def require_identity(
    path: Path, *, expected_bytes: int, expected_sha256: str
) -> None:
    if not path.is_file():
        raise RuntimeError(f"Missing required file: {path}")
    actual_bytes = path.stat().st_size
    actual_sha256 = sha256_path(path)
    if actual_bytes != expected_bytes or actual_sha256 != expected_sha256:
        raise RuntimeError(
            "Identity mismatch for "
            f"{path}: {actual_bytes} B {actual_sha256}; expected "
            f"{expected_bytes} B {expected_sha256}"
        )


def source_files() -> list[Path]:
    files = []
    for path in EGA_ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(EGA_ROOT)
        if rel.parts and rel.parts[0] == "checkpoints":
            continue
        files.append(path)
    return sorted(files, key=lambda path: path.relative_to(EGA_ROOT).as_posix())


def zip_info(name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    return info


def csv_bytes(rows: list[dict[str, object]], fieldnames: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\r\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def build_source_zip(path: Path, files: list[Path]) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    payload: list[tuple[str, bytes]] = []
    for source in files:
        rel = source.relative_to(EGA_ROOT).as_posix()
        data = source.read_bytes()
        role = (
            "source_first_checkpoint_component"
            if rel == "ega0/ega0-11.tex"
            else "supporting_editable_source"
        )
        rows.append(
            {
                "relative_path": rel,
                "bytes": len(data),
                "sha256": sha256_bytes(data),
                "role": role,
            }
        )
        payload.append((rel, data))

    manifest = csv_bytes(
        rows, ["relative_path", "bytes", "sha256", "role"]
    )
    with zipfile.ZipFile(path, "w", allowZip64=True) as archive:
        for rel, data in payload:
            archive.writestr(zip_info(rel), data)
        archive.writestr(zip_info("SOURCE_BUNDLE_SHA256.csv"), manifest)

    return {
        "source_files": len(files),
        "zip_members": len(files) + 1,
        "source_bytes": sum(item.stat().st_size for item in files),
        "zip_bytes": path.stat().st_size,
        "zip_sha256": sha256_path(path),
        "internal_manifest_rows": len(rows),
        "internal_manifest_bytes": len(manifest),
        "internal_manifest_sha256": sha256_bytes(manifest),
    }


def link_summary(reader: PdfReader) -> dict[str, int]:
    goto = 0
    uri = 0
    other = 0
    for page in reader.pages:
        for ref in page.get("/Annots", []) or []:
            annotation = ref.get_object()
            if annotation.get("/Subtype") != "/Link":
                continue
            action = annotation.get("/A")
            if action is not None:
                action = action.get_object()
                kind = action.get("/S")
                if kind == "/GoTo":
                    goto += 1
                elif kind == "/URI":
                    uri += 1
                else:
                    other += 1
            elif annotation.get("/Dest") is not None:
                goto += 1
            else:
                other += 1
    return {"goto": goto, "uri": uri, "other": other}


def run_command(command: list[str], cwd: Path) -> str:
    result = subprocess.run(
        command,
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
        errors="replace",
    )
    output = result.stdout + result.stderr
    if result.returncode != 0:
        raise RuntimeError(
            f"Command failed ({result.returncode}): {' '.join(command)}\n"
            + "\n".join(output.splitlines()[-80:])
        )
    return output


def isolated_rebuild(files: list[Path], candidate_pdf: Path) -> dict[str, object]:
    with tempfile.TemporaryDirectory(prefix="ega0_iii_11_10_rebuild_") as temp:
        root = Path(temp)
        for source in files:
            rel = source.relative_to(EGA_ROOT)
            destination = root / rel
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)

        outputs = []
        outputs.append(run_command(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "ega0.tex"], root))
        outputs.append(run_command(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "ega0.tex"], root))
        outputs.append(run_command(["bibtex", "ega0"], root))
        for _ in range(4):
            outputs.append(
                run_command(
                    ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "ega0.tex"],
                    root,
                )
            )

        rebuilt_pdf = root / "ega0.pdf"
        if not rebuilt_pdf.is_file():
            raise RuntimeError("Isolated rebuild did not produce ega0.pdf")

        candidate = PdfReader(str(candidate_pdf))
        rebuilt = PdfReader(str(rebuilt_pdf))
        if len(candidate.pages) != EXPECTED_PDF_PAGES:
            raise RuntimeError("Candidate PDF page count drift")
        if len(rebuilt.pages) != EXPECTED_PDF_PAGES:
            raise RuntimeError("Rebuilt PDF page count mismatch")

        text_equal = []
        geometry_equal = []
        for left, right in zip(candidate.pages, rebuilt.pages, strict=True):
            text_equal.append((left.extract_text() or "") == (right.extract_text() or ""))
            geometry_equal.append(
                (
                    float(left.mediabox.width),
                    float(left.mediabox.height),
                )
                == (
                    float(right.mediabox.width),
                    float(right.mediabox.height),
                )
            )
        candidate_links = link_summary(candidate)
        rebuilt_links = link_summary(rebuilt)
        if not all(text_equal):
            raise RuntimeError("Isolated rebuild text differs from candidate PDF")
        if not all(geometry_equal):
            raise RuntimeError("Isolated rebuild geometry differs from candidate PDF")
        if candidate_links != rebuilt_links:
            raise RuntimeError("Isolated rebuild link summary differs")
        if len(candidate.named_destinations) != len(rebuilt.named_destinations):
            raise RuntimeError("Isolated rebuild destination count differs")

        final_log = (root / "ega0.log").read_text(
            encoding="utf-8", errors="replace"
        )
        hard_patterns = (
            "! LaTeX Error",
            "Undefined control sequence",
            "Emergency stop",
            "Fatal error",
            "There were undefined citations",
            "multiply defined",
        )
        hard_hits = {
            pattern: final_log.count(pattern)
            for pattern in hard_patterns
            if pattern in final_log
        }
        if hard_hits:
            raise RuntimeError(f"Isolated rebuild diagnostic failures: {hard_hits}")
        undefined_hyperrefs = sorted(
            set(
                re.findall(
                    r"Hyper reference `([^']+)' .* undefined",
                    final_log,
                )
            )
        )
        if undefined_hyperrefs != EXPECTED_INHERITED_UNDEFINED_HYPERREFS:
            raise RuntimeError(
                "Unexpected inherited undefined-hyperref set: "
                f"{undefined_hyperrefs}"
            )

        return {
            "engine_passes": 6,
            "bibtex_passes": 1,
            "page_count": len(rebuilt.pages),
            "text_pages_equal": sum(text_equal),
            "geometry_pages_equal": sum(geometry_equal),
            "candidate_destinations": len(candidate.named_destinations),
            "rebuilt_destinations": len(rebuilt.named_destinations),
            "candidate_links": candidate_links,
            "rebuilt_links": rebuilt_links,
            "rebuilt_pdf_bytes": rebuilt_pdf.stat().st_size,
            "rebuilt_pdf_sha256": sha256_path(rebuilt_pdf),
            "hard_diagnostic_hits": hard_hits,
            "inherited_undefined_hyperrefs": undefined_hyperrefs,
            "inherited_undefined_hyperref_count": len(undefined_hyperrefs),
            "raw_logs_retained": False,
        }


def write_text(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def validate_zip(path: Path) -> dict[str, object]:
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        names = [info.filename for info in infos]
        unsafe = []
        for name in names:
            pure = PurePosixPath(name)
            if (
                pure.is_absolute()
                or ".." in pure.parts
                or "\\" in name
                or (len(name) >= 2 and name[1] == ":")
            ):
                unsafe.append(name)
        manifest = archive.read("SOURCE_BUNDLE_SHA256.csv")
        rows = list(
            csv.DictReader(io.StringIO(manifest.decode("utf-8-sig")))
        )
        errors = []
        expected_names = set()
        for row in rows:
            name = row["relative_path"]
            expected_names.add(name)
            try:
                data = archive.read(name)
            except KeyError:
                errors.append({"path": name, "error": "missing"})
                continue
            if (
                len(data) != int(row["bytes"])
                or sha256_bytes(data) != row["sha256"].upper()
            ):
                errors.append({"path": name, "error": "identity"})
        unexpected = sorted(
            set(names) - expected_names - {"SOURCE_BUNDLE_SHA256.csv"}
        )
        return {
            "entries": len(infos),
            "files": sum(not info.is_dir() for info in infos),
            "directories": sum(info.is_dir() for info in infos),
            "uncompressed_bytes": sum(info.file_size for info in infos),
            "safe_path_errors": unsafe,
            "manifest_rows": len(rows),
            "manifest_sha256": sha256_bytes(manifest),
            "manifest_errors": errors,
            "unexpected_entries": unexpected,
            "crc_error": archive.testzip(),
        }


def privacy_scan(paths: list[Path]) -> list[dict[str, str]]:
    hits = []
    for path in paths:
        if path.suffix.lower() not in {
            ".md",
            ".tex",
            ".csv",
            ".json",
            ".txt",
            ".yml",
            ".yaml",
            ".py",
        }:
            continue
        data = path.read_bytes()
        for pattern in PRIVACY_PATTERNS:
            if pattern in data:
                hits.append(
                    {
                        "path": path.relative_to(REPO_ROOT).as_posix(),
                        "pattern": pattern.decode("ascii", errors="replace"),
                    }
                )
    return hits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate-pdf", type=Path, required=True)
    args = parser.parse_args()

    candidate_pdf = args.candidate_pdf.resolve()
    checkpoint_tex = EGA_ROOT / "ega0" / "ega0-11.tex"
    base_ega0_12 = EGA_ROOT / "ega0" / "ega0-12.tex"
    require_identity(
        candidate_pdf,
        expected_bytes=EXPECTED_PDF_BYTES,
        expected_sha256=EXPECTED_PDF_SHA256,
    )
    require_identity(
        checkpoint_tex,
        expected_bytes=EXPECTED_TEX_BYTES,
        expected_sha256=EXPECTED_TEX_SHA256,
    )
    if sha256_path(base_ega0_12) != EXPECTED_BASE_EGA0_12_SHA256:
        raise RuntimeError("ega0-12.tex is not the checkpoint baseline")

    files = source_files()
    if len(files) != 95:
        raise RuntimeError(f"Unexpected source-file count: {len(files)}")

    if PACKAGE_ROOT.exists():
        shutil.rmtree(PACKAGE_ROOT)
    PACKAGE_ROOT.mkdir(parents=True)

    public_pdf = PACKAGE_ROOT / PDF_NAME
    public_tex = PACKAGE_ROOT / TEX_NAME
    source_zip = PACKAGE_ROOT / ZIP_NAME
    shutil.copyfile(candidate_pdf, public_pdf)
    shutil.copyfile(checkpoint_tex, public_tex)

    rebuild = isolated_rebuild(files, public_pdf)
    source_bundle = build_source_zip(source_zip, files)

    reader = PdfReader(str(public_pdf))
    pdf_links = link_summary(reader)
    if len(reader.pages) != EXPECTED_PDF_PAGES:
        raise RuntimeError("Public PDF page count mismatch")
    if pdf_links["other"] or pdf_links["uri"]:
        raise RuntimeError(f"Unexpected PDF actions: {pdf_links}")

    write_text(
        PACKAGE_ROOT / "README.md",
        f"""
# EGA 0 English working reader with source-first section 11 successor

This checkpoint integrates source-first English work from section 11.5.1
through Corollary 11.10.3 into the existing EGA 0 working reader. That
verified successor range covers authority PDF pages 32-46 / printed pages
35-49. Its next source-first unit is section 12.1.1.

The 93-page reader is a cumulative working container, not a PDF ending at
11.10.3. It also retains inherited surrounding English material for sections
1.0-11.5 and 12.1-14.3.6. Those surrounding sections are useful reading
context but are not newly source-certified by this checkpoint.

Reader:

- `{PDF_NAME}`
- {EXPECTED_PDF_PAGES} US-letter pages
- {EXPECTED_PDF_BYTES:,} bytes
- SHA-256 `{EXPECTED_PDF_SHA256}`

Editable section-11 component:

- `{TEX_NAME}`
- {EXPECTED_TEX_BYTES:,} bytes
- SHA-256 `{EXPECTED_TEX_SHA256}`

The direct TeX contains the complete section-11 component. The source-first
successor span begins at 11.5.1 and continues through 11.10.3. The grouped
source ZIP contains {source_bundle['source_files']} editable and support files
plus a self-excluding internal manifest and rebuilds the full 93-page working
container.

This is a source-first bounded working checkpoint, not completion of EGA,
not a critical edition, and not independent human certification. Existing
user-supplied OCR and inherited English drafts were read-only locator and
drafting witnesses; neither is textual authority.
""",
    )
    write_text(
        PACKAGE_ROOT / "PROVENANCE_AND_RIGHTS.md",
        f"""
# Provenance and rights

The controlling authority is `{AUTHORITY_NAME}`, {AUTHORITY_PAGES} pages,
{AUTHORITY_BYTES:,} bytes, SHA-256 `{AUTHORITY_SHA256}`. The authority PDF is
not bundled in this checkpoint.

The source-first translated successor covers EGA 0_III sections
11.5.1-11.10.3 against authority pages 32-46 / printed pages 35-49. The
93-page working reader also includes inherited English context for sections
1.0-11.5 and 12.1-14.3.6; this checkpoint does not certify those surrounding
sections against the authority. Existing user-supplied OCR and comparison
translations were consulted read-only as locators or drafting witnesses. No
OCR was generated or rerun.

No license grant or redistribution right for the French authority, the
underlying mathematical work, or third-party material is asserted here.
Rights and attribution remain with their respective holders. This package is
a bounded machine-assisted working translation and source checkpoint, not a
critical edition or rights determination.
""",
    )
    write_text(
        PACKAGE_ROOT / "BUILD_SUMMARY_PUBLIC.md",
        f"""
# Public build summary

- Isolated rebuild: PASS
- pdfLaTeX passes: {rebuild['engine_passes']}
- BibTeX passes: {rebuild['bibtex_passes']}
- Candidate/rebuild pages: {rebuild['page_count']}/{rebuild['page_count']}
- Candidate/rebuild extracted-text pages equal:
  {rebuild['text_pages_equal']}/{rebuild['page_count']}
- Candidate/rebuild page geometry equal:
  {rebuild['geometry_pages_equal']}/{rebuild['page_count']}
- Named destinations: {rebuild['candidate_destinations']}
- Internal GoTo links: {pdf_links['goto']}
- URI/other actions: {pdf_links['uri']}/{pdf_links['other']}
- Hard build diagnostics: 0
- Inherited unresolved cross-volume/earlier-range hyperrefs:
  {rebuild['inherited_undefined_hyperref_count']}
- Unresolved identifiers:
  `{', '.join(rebuild['inherited_undefined_hyperrefs'])}`
- Raw build logs retained publicly: no

The producer separately rendered and inspected the newly completed section
11.8-11.10 pages at 400 dpi. Archive curation also inspected reader pages 1,
80, 87, and 93 at 180 dpi, including the section-11 ending and retained
surrounding context. This public package retains the mathematical reader,
editable source, and reproducible source closure without raw host-path-bearing
logs.
""",
    )
    write_text(
        PACKAGE_ROOT / "PUBLICATION_READINESS.md",
        """
# Publication readiness

Status: `READY_FOR_BOUNDED_WORKING_PUBLICATION`

The direct reader, direct editable checkpoint TeX, and grouped source closure
are privacy-clean and independently rebuildable. Publication must retain the
bounded scope, authority, rights, and machine-assisted-working-status caveats.

This checkpoint does not claim completion of EGA 0_III, EGA III, or EGA as a
whole. Its source-first verified range stops before section 12.1.1; the reader
container retains inherited surrounding material through section 14.3.6. It
does not claim critical-edition status, source certification beyond the stated
pages, peer review, tagged-PDF accessibility remediation, exhaustive reference
closure, or a new license grant. Six inherited cross-volume or earlier-range
hyperrefs remain unresolved and are disclosed in the public build summary.
""",
    )

    content_names = [
        PDF_NAME,
        TEX_NAME,
        ZIP_NAME,
        "BUILD_SUMMARY_PUBLIC.md",
        "PROVENANCE_AND_RIGHTS.md",
        "PUBLICATION_READINESS.md",
        "README.md",
    ]
    manifest_rows = []
    for name in content_names:
        path = PACKAGE_ROOT / name
        manifest_rows.append(
            {
                "filename": name,
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
            }
        )
    manifest = csv_bytes(manifest_rows, ["filename", "bytes", "sha256"])
    (PACKAGE_ROOT / "SHA256SUMS.csv").write_bytes(manifest)

    zip_check = validate_zip(source_zip)
    privacy_hits = privacy_scan(
        files
        + [
            PACKAGE_ROOT / name
            for name in content_names
            if (PACKAGE_ROOT / name).suffix.lower() != ".zip"
        ]
        + [PACKAGE_ROOT / "SHA256SUMS.csv"]
    )
    errors = []
    if zip_check["safe_path_errors"]:
        errors.append("unsafe_zip_paths")
    if zip_check["manifest_errors"] or zip_check["unexpected_entries"]:
        errors.append("zip_manifest_closure")
    if zip_check["crc_error"] is not None:
        errors.append("zip_crc")
    if privacy_hits:
        errors.append("privacy")

    validation = {
        "schema": "ega0_iii_11_10_public_checkpoint_validation.v2",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "scope": {
            "work": "EGA 0_III",
            "reader_container": {
                "start": "1.0",
                "end": "14.3.6",
                "status": "mixed inherited working English plus bounded source-first successor",
            },
            "source_first_verified_successor": {
                "start": "11.5.1",
                "end": "11.10.3",
                "next": "12.1.1",
                "authority_pdf_pages": "32-46",
                "printed_pages": "35-49",
            },
            "surrounding_context_source_certified_here": False,
            "whole_ega_complete": False,
        },
        "reader": {
            "filename": PDF_NAME,
            "bytes": public_pdf.stat().st_size,
            "sha256": sha256_path(public_pdf),
            "pages": len(reader.pages),
            "page_size_points": [
                float(reader.pages[0].mediabox.width),
                float(reader.pages[0].mediabox.height),
            ],
            "named_destinations": len(reader.named_destinations),
            "links": pdf_links,
        },
        "editable_tex": {
            "filename": TEX_NAME,
            "bytes": public_tex.stat().st_size,
            "sha256": sha256_path(public_tex),
        },
        "source_bundle": source_bundle,
        "zip_replay": zip_check,
        "isolated_rebuild": rebuild,
        "outer_manifest": {
            "rows": len(manifest_rows),
            "bytes": len(manifest),
            "sha256": sha256_bytes(manifest),
        },
        "privacy_hits": privacy_hits,
        "authority_redistributed": False,
        "ocr_generated_or_rerun": False,
    }
    validation_path = PACKAGE_ROOT / "PACKAGE_VALIDATION.json"
    validation_path.write_text(
        json.dumps(validation, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    if errors:
        raise RuntimeError(f"Package validation failed: {errors}")

    result = {
        "package": str(PACKAGE_ROOT),
        "files": len(list(PACKAGE_ROOT.iterdir())),
        "bytes": sum(path.stat().st_size for path in PACKAGE_ROOT.iterdir()),
        "reader_sha256": sha256_path(public_pdf),
        "tex_sha256": sha256_path(public_tex),
        "zip_sha256": sha256_path(source_zip),
        "manifest_sha256": sha256_path(PACKAGE_ROOT / "SHA256SUMS.csv"),
        "validation_sha256": sha256_path(validation_path),
        "status": "PASS",
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
