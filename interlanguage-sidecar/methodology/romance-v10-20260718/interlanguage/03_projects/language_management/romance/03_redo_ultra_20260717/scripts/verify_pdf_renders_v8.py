from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageChops


ROOT = Path(__file__).resolve().parent.parent
REPOSITORY_ROOT = ROOT.parents[3]
POPLER_BIN = Path(
    r"C:\Users\Floris\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin"
)
PDFTOPPM = POPLER_BIN / "pdftoppm.exe"
PDFINFO = POPLER_BIN / "pdfinfo.exe"
OUT = ROOT / "qa" / "PDF_RENDER_REPRODUCIBILITY_v8.json"
TEMP_PARENT = ROOT / "tmp" / "pdfs"
RENDER_DPI = 150
TRANCHES = (
    ("R823_HG_T001", 3),
    ("R823_HG_T002", 2),
    ("R823_HG_T003", 2),
    ("R823_HG_T004", 2),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def byte_identical(left: Path, right: Path) -> bool:
    if left.stat().st_size != right.stat().st_size:
        return False
    with left.open("rb") as left_handle, right.open("rb") as right_handle:
        while True:
            left_block = left_handle.read(1024 * 1024)
            right_block = right_handle.read(1024 * 1024)
            if left_block != right_block:
                return False
            if not left_block:
                return True


def repository_relative(path: Path) -> str:
    return path.resolve().relative_to(REPOSITORY_ROOT.resolve()).as_posix()


def tool_version(path: Path) -> str:
    result = subprocess.run(
        [str(path), "-v"],
        check=True,
        capture_output=True,
        text=True,
    )
    lines = (result.stdout + "\n" + result.stderr).splitlines()
    first_line = next((line.strip() for line in lines if line.strip()), "")
    assert first_line, f"No version string returned by {path}"
    return first_line


def pdf_page_count(path: Path) -> int:
    result = subprocess.run(
        [str(PDFINFO), str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, flags=re.MULTILINE)
    assert match, f"No Pages field returned by pdfinfo for {path}"
    return int(match.group(1))


def first_nonwhite_row(path: Path) -> int | None:
    with Image.open(path).convert("RGB") as image:
        white = Image.new("RGB", image.size, "white")
        bbox = ImageChops.difference(image, white).getbbox()
        return None if bbox is None else bbox[1]


def numbered_pngs(directory: Path, prefix: str) -> dict[int, Path]:
    result: dict[int, Path] = {}
    pattern = re.compile(rf"^{re.escape(prefix)}-(\d+)\.png$")
    for path in directory.glob(f"{prefix}-*.png"):
        match = pattern.match(path.name)
        assert match, f"Unexpected render name: {path}"
        page = int(match.group(1))
        assert page not in result, f"Duplicate rendered page {page}: {path}"
        result[page] = path
    return result


def verify_tranche(tranche: str, expected_page_count: int) -> dict:
    base = ROOT / tranche
    build_pdf = base / "build" / f"{tranche}_romance.pdf"
    final_pdf = REPOSITORY_ROOT / "output" / "pdf" / f"{tranche}_controlled_romance.pdf"
    pinned_dir = base / "qa" / "rendered"

    for required in (build_pdf, final_pdf, pinned_dir):
        assert required.exists(), required

    build_hash = sha256(build_pdf)
    final_hash = sha256(final_pdf)
    pdfs_byte_identical = byte_identical(build_pdf, final_pdf)
    assert build_hash == final_hash, (tranche, build_hash, final_hash)
    assert pdfs_byte_identical, f"Build/output PDF byte mismatch: {tranche}"

    build_page_count = pdf_page_count(build_pdf)
    final_page_count = pdf_page_count(final_pdf)
    assert build_page_count == expected_page_count, (
        tranche,
        "build_pdf",
        build_page_count,
        expected_page_count,
    )
    assert final_page_count == expected_page_count, (
        tranche,
        "final_output_pdf",
        final_page_count,
        expected_page_count,
    )

    pinned = numbered_pngs(pinned_dir, f"{tranche}_page")
    expected_pages = set(range(1, expected_page_count + 1))
    assert set(pinned) == expected_pages, (
        tranche,
        "pinned_pages",
        sorted(pinned),
        sorted(expected_pages),
    )

    with tempfile.TemporaryDirectory(prefix=f"v8_{tranche}_", dir=TEMP_PARENT) as temp_name:
        temp_dir = Path(temp_name)
        output_prefix = temp_dir / f"{tranche}_page"
        subprocess.run(
            [
                str(PDFTOPPM),
                "-png",
                "-r",
                str(RENDER_DPI),
                str(build_pdf),
                str(output_prefix),
            ],
            check=True,
            capture_output=True,
        )
        fresh = numbered_pngs(temp_dir, f"{tranche}_page")
        assert set(fresh) == expected_pages, (
            tranche,
            "fresh_pages",
            sorted(fresh),
            sorted(expected_pages),
        )

        pages = []
        for page in sorted(expected_pages):
            fresh_path = fresh[page]
            pinned_path = pinned[page]
            fresh_hash = sha256(fresh_path)
            pinned_hash = sha256(pinned_path)
            pages_byte_identical = byte_identical(fresh_path, pinned_path)
            assert fresh_hash == pinned_hash, (
                tranche,
                page,
                fresh_hash,
                pinned_hash,
            )
            assert pages_byte_identical, f"Fresh/pinned PNG byte mismatch: {tranche} page {page}"
            with Image.open(fresh_path) as image:
                pixel_size = list(image.size)
                image_mode = image.mode
            pages.append(
                {
                    "page": page,
                    "pinned_render": {
                        "path": repository_relative(pinned_path),
                        "sha256": pinned_hash,
                        "bytes": pinned_path.stat().st_size,
                    },
                    "fresh_render_sha256": fresh_hash,
                    "fresh_render_bytes": fresh_path.stat().st_size,
                    "hash_match": True,
                    "byte_identical": True,
                    "pixel_size": pixel_size,
                    "image_mode": image_mode,
                    "first_nonwhite_row": first_nonwhite_row(fresh_path),
                }
            )

    return {
        "tranche": tranche,
        "expected_page_count": expected_page_count,
        "build_pdf": {
            "path": repository_relative(build_pdf),
            "sha256": build_hash,
            "bytes": build_pdf.stat().st_size,
            "pdfinfo_page_count": build_page_count,
        },
        "final_output_pdf": {
            "path": repository_relative(final_pdf),
            "sha256": final_hash,
            "bytes": final_pdf.stat().st_size,
            "pdfinfo_page_count": final_page_count,
        },
        "build_output_binding": {
            "sha256_match": True,
            "byte_identical": True,
        },
        "rendered_pdf": "build_pdf",
        "output_render_assurance": "The final output PDF is byte-identical to the rendered build PDF.",
        "fresh_render_page_count": len(pages),
        "pinned_render_page_count": len(pinned),
        "page_count_match": True,
        "pages": pages,
    }


def main() -> None:
    TEMP_PARENT.mkdir(parents=True, exist_ok=True)
    assert PDFTOPPM.exists(), PDFTOPPM
    assert PDFINFO.exists(), PDFINFO

    tranches = [verify_tranche(tranche, page_count) for tranche, page_count in TRANCHES]
    report = {
        "artifact": "PDF_RENDER_REPRODUCIBILITY_v8",
        "audit_date": "2026-07-17",
        "status": "PASS",
        "verifier": {
            "path": repository_relative(Path(__file__)),
            "sha256": sha256(Path(__file__)),
        },
        "renderer": {
            "path": str(PDFTOPPM),
            "sha256": sha256(PDFTOPPM),
            "version": tool_version(PDFTOPPM),
            "render_dpi": RENDER_DPI,
            "command_template": [
                str(PDFTOPPM),
                "-png",
                "-r",
                str(RENDER_DPI),
                "<build_pdf>",
                "<isolated_temporary_output_prefix>",
            ],
            "temporary_directory_policy": "One isolated TemporaryDirectory per tranche under tmp/pdfs; automatically removed after comparison.",
        },
        "page_counter": {
            "path": str(PDFINFO),
            "sha256": sha256(PDFINFO),
            "version": tool_version(PDFINFO),
            "command_template": [str(PDFINFO), "<pdf>"],
        },
        "required_page_counts": {
            tranche: page_count for tranche, page_count in TRANCHES
        },
        "totals": {
            "tranches": len(tranches),
            "build_pdfs": len(tranches),
            "final_output_pdfs": len(tranches),
            "pinned_pages": sum(item["pinned_render_page_count"] for item in tranches),
            "fresh_pages": sum(item["fresh_render_page_count"] for item in tranches),
            "all_build_output_pdfs_byte_identical": True,
            "all_fresh_pinned_pngs_byte_identical": True,
        },
        "tranches": tranches,
        "timestamp_caveat": "This gate binds and renders the current pinned PDFs. A later LuaLaTeX rebuild can change PDF CreationDate/ModDate and therefore the PDF SHA-256 without changing extracted text or rendered pages; such a rebuild requires this gate to be rerun and its new artifact identities recorded.",
        "human_native_claim_boundary": {
            "human_observation_rows_recorded_by_this_artifact": 0,
            "native_speaker_observations_recorded_by_this_artifact": 0,
            "human_intelligibility_observations_recorded_by_this_artifact": 0,
            "native_validated": False,
            "human_validated": False,
            "pilot_claim": False,
            "scope": "PDF identity, page-count, deterministic Poppler render reproduction, and visual-layout assurance only.",
        },
    }
    serialized = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    with OUT.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(serialized)
    print(serialized, end="")


if __name__ == "__main__":
    main()
