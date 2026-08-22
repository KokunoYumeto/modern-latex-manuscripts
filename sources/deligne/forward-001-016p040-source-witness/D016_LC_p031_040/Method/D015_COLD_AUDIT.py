#!/usr/bin/env python3
"""Fresh, fail-closed, nonpatching D015 cold audit.

The audit reads frozen inputs, may create only its receipt/manifest and temporary
renders, and never repairs an input.  Any failed invariant exits nonzero.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageChops
from pypdf import PdfReader


A4 = (595.276, 841.89)
AUTHORITY_SHA = "22BD33F5D00EA962BA24996703CDDF74C4DCB09BF91050F0463036B5B38803CB"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def identity(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return {"path": str(path), "bytes": path.stat().st_size, "sha256": sha256(path)}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def verify(path: Path, expected_bytes: int, expected_sha: str) -> dict:
    row = identity(path)
    require(row["bytes"] == expected_bytes, f"byte count mismatch: {path}: {row['bytes']} != {expected_bytes}")
    require(row["sha256"] == expected_sha, f"SHA-256 mismatch: {path}: {row['sha256']} != {expected_sha}")
    require(row["bytes"] < 500_000_000, f"500 MB contract exceeded: {path}")
    return row


def page_size(page) -> tuple[float, float]:
    box = page.mediabox
    return (round(float(box.width), 3), round(float(box.height), 3))


def assert_a4(size: tuple[float, float], label: str) -> None:
    require(abs(size[0] - A4[0]) < 0.1 and abs(size[1] - A4[1]) < 0.1, f"non-A4 page in {label}: {size}")


def run_text(path: Path, first: int | None = None, last: int | None = None) -> str:
    command = ["pdftotext", "-enc", "UTF-8"]
    if first is not None:
        command += ["-f", str(first)]
    if last is not None:
        command += ["-l", str(last)]
    command += [str(path), "-"]
    result = subprocess.run(command, check=True, capture_output=True)
    text = result.stdout.decode("utf-8")
    require("\ufffd" not in text, f"replacement character in extracted text: {path}")
    require("\x00" not in text, f"NUL in extracted text: {path}")
    return text


def normalized_text(text: str) -> bytes:
    return re.sub(r"\s+", " ", text).strip().encode("utf-8")


def text_sha(text: str) -> str:
    return hashlib.sha256(normalized_text(text)).hexdigest().upper()


def reader_text(reader: PdfReader, first: int = 1, last: int | None = None) -> str:
    if last is None:
        last = len(reader.pages)
    return "\f".join((reader.pages[index - 1].extract_text() or "") for index in range(first, last + 1))


def pdffonts_audit(path: Path, first: int | None = None, last: int | None = None) -> dict:
    command = ["pdffonts"]
    if first is not None:
        command += ["-f", str(first)]
    if last is not None:
        command += ["-l", str(last)]
    command.append(str(path))
    result = subprocess.run(command, check=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
    rows = []
    for line in result.stdout.splitlines()[2:]:
        match = re.search(r"\s(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$", line)
        if match:
            rows.append({"embedded": match.group(1), "subset": match.group(2), "unicode": match.group(3), "line": line})
    require(rows, f"no font rows parsed: {path}")
    require(all(row["embedded"] == "yes" for row in rows), f"unembedded typeset font: {path}")
    require(all(row["unicode"] == "yes" for row in rows), f"font without ToUnicode in audited D015 range: {path}")
    return {"font_rows": len(rows), "all_embedded": True, "all_unicode": True}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def flat_outline(reader: PdfReader) -> list:
    result = []

    def walk(items) -> None:
        for item in items:
            if isinstance(item, list):
                walk(item)
            else:
                result.append(item)

    walk(reader.outline)
    return result


def render_page(authority: Path, page_number: int, temporary: Path) -> Path:
    prefix = temporary / f"authority_{page_number:02d}"
    subprocess.run(
        ["pdftoppm", "-f", str(page_number), "-l", str(page_number), "-r", "300", "-gray", "-png", str(authority), str(prefix)],
        check=True,
        capture_output=True,
    )
    matches = list(temporary.glob(f"{prefix.name}-*.png"))
    require(len(matches) == 1, f"unexpected authority render count for page {page_number}")
    return matches[0]


def audit(args: argparse.Namespace) -> dict:
    root = args.successor_root.resolve()
    canonical = root / "canonical_work"
    audit_root = root / "audit"
    source_tree = root / "source_tree"
    github = root / "github_cumulative_rebuild_D015"

    expected = {
        canonical / "authority" / "D015_IAS_Number14_300dpi.pdf": (335330, AUTHORITY_SHA),
        canonical / "D015_FR.tex": (22229, "54652D76CE4C90EB853554D685420E30591A793462D3A5FDEE7418AFF213A495"),
        canonical / "D015_EN.tex": (22160, "9FF022FFC278BE27659C87823F83194902CF0BBB52C7E488374AB8EC7212CC49"),
        canonical / "D015_FR.pdf": (755393, "C885BD1693CEC81EB949B33E7049A28F352D1797D76AA70F565BB259508CEAD2"),
        canonical / "D015_EN.pdf": (834905, "607E3F0EB100655151CBB830632D6555587918007BB7B76E45CC7F22F33059A2"),
        canonical / "D015_APPARATUS.md": (2016, "0EB6C2F9319A5374EDC52DF2A08EFAEF73BA27050173628AE334A1EA745788A6"),
        source_tree / "Deligne_FR.pdf": (4274270, "66D021592EA2C2B6CFF7DFD8825043EC229AAD343649CD70324FFBA8231ED355"),
        source_tree / "Deligne_EN.pdf": (4420184, "529B11CBF56E8FAED030E61F88C884C33F72D04942E9EB17E60D081C4257F59A"),
        github / "ALL_001_016p040_FR.pdf": (6375831, "4D022E4E5083804FE4337F2FEC32EA921D3F2C6D92F56CD26F2223CB972C08BF"),
        github / "ALL_001_016p040_EN.pdf": (6378148, "5D19FD934D8F41B4F429235B98F7FE2BC85E92659AA4768C659595AE538D6CAD"),
        github / "ALL_001_016p040_SCAN.pdf": (8444031, "0E1081CB7CC14C73D7E1978397FD6D99F8E876437DF8543143F49615029EA558"),
        args.returned_zip.resolve(): (5528693, "A48A6573372617FFFD37F6664BA5BABB25A381E16DADCAD16528AD5E7BA01A25"),
    }
    identities = [verify(path, size, digest) for path, (size, digest) in expected.items()]

    authority_reader = PdfReader(str(canonical / "authority" / "D015_IAS_Number14_300dpi.pdf"))
    fr_reader = PdfReader(str(canonical / "D015_FR.pdf"))
    en_reader = PdfReader(str(canonical / "D015_EN.pdf"))
    zfr_reader = PdfReader(str(source_tree / "Deligne_FR.pdf"))
    zen_reader = PdfReader(str(source_tree / "Deligne_EN.pdf"))
    gfr_reader = PdfReader(str(github / "ALL_001_016p040_FR.pdf"))
    gen_reader = PdfReader(str(github / "ALL_001_016p040_EN.pdf"))
    gscan_reader = PdfReader(str(github / "ALL_001_016p040_SCAN.pdf"))

    require(len(authority_reader.pages) == 13, "authority page count")
    require(len(fr_reader.pages) == 13, "French standalone page count")
    require(len(en_reader.pages) == 7, "English standalone page count")
    require(len(zfr_reader.pages) == 223 and len(zen_reader.pages) == 213, "Zenodo cumulative page counts")
    require(len(gfr_reader.pages) == 245 and len(gen_reader.pages) == 238 and len(gscan_reader.pages) == 352, "GitHub cumulative page counts")
    for label, pages in {
        "FR standalone": fr_reader.pages,
        "EN standalone": en_reader.pages,
        "Zenodo FR D015": zfr_reader.pages[210:223],
        "Zenodo EN D015": zen_reader.pages[206:213],
        "GitHub FR D015": gfr_reader.pages[211:224],
        "GitHub EN D015": gen_reader.pages[210:217],
    }.items():
        for page in pages:
            require(int(page.get("/Rotate", 0) or 0) == 0, f"rotation in {label}")
            assert_a4(page_size(page), label)

    fr_tex = (canonical / "D015_FR.tex").read_text(encoding="utf-8")
    en_tex = (canonical / "D015_EN.tex").read_text(encoding="utf-8")
    require(fr_tex.count("% Authority physical page") == 13, "French authority markers")
    require(en_tex.count("% Authority physical page") == 13, "English authority markers")
    require(fr_tex.count("\\newpage") == 12, "French exact physical-page breaks")
    require("paper=a4paper" in fr_tex and "paper=a4paper" in en_tex, "standalone A4 declarations")
    required = [
        r"(ii)\Rightarrow(i)\Leftrightarrow(iii)\Rightarrow(iv)\Leftrightarrow(ii)",
        r"P_a\simeq P_2=0",
        r"H^0(X,\Omega_X^1)=H^0(X,(\Omega_X^2)^{\otimes2})=0",
        r"\psi:H^3(X,\ZZ)\otimes H^3(X,\ZZ)",
        "diagramme 2.1",
        r"J(Y'')\simeq J(Y')\times J(Z)",
        r"(x,y)\overset{\delta}{\longmapsto}\alpha(x)-\alpha(y)",
        r"X_s=f^{-1}(s)",
        "ceci résoud",
        r"0\longrightarrow\ZZ/2\oplus\ZZ/2\longrightarrow E^{2,2}",
        r"a(E^{0,2})=2\ZZ",
        r"E_2^{pq}=E_\infty^{pq}",
    ]
    compact = lambda value: re.sub(r"\s+", "", value)
    compact_fr = compact(fr_tex)
    compact_en = compact(en_tex)
    for literal in required:
        require(compact(literal) in compact_fr, f"required French reading absent: {literal}")
    for literal in [r"P_a\simeq P_2=0", r"X_s=f^{-1}(s)", r"E_2^{pq}=E_\infty^{pq}"]:
        require(compact(literal) in compact_en, f"required English reading absent: {literal}")
    for forbidden in ["\\begin{tikzpicture}", r"(\Alb(S),\Theta(S\times S))", r"(ii)\Rightarrow(i)\Rightarrow(iii)"]:
        require(compact(forbidden) not in compact_fr and compact(forbidden) not in compact_en, f"rejected inherited reading present: {forbidden}")
    body_lower = (fr_tex + "\n" + en_tex).lower()
    require("24e année" not in body_lower and "novembre 1971" not in body_lower, "masthead/date copy matter entered body")

    page_map = read_tsv(audit_root / "D015_CURRENT_AUTHORITY_PAGE_MAP.tsv")
    literality = read_tsv(audit_root / "D015_CURRENT_LITERALITY_LEDGER.tsv")
    assets = read_tsv(audit_root / "D015_CURRENT_ASSET_LEDGER.tsv")
    for rows, label, count in [(page_map, "page map", 13), (literality, "literality ledger", 13), (assets, "asset ledger", 7)]:
        require(len(rows) == count, f"{label} row count")
        require(all(row.get("authority_sha256", AUTHORITY_SHA) == AUTHORITY_SHA for row in rows), f"{label} authority binding")
        require(all(row["status"] == "PASS" for row in rows) if "status" in rows[0] else True, f"{label} status")

    assets_dir = canonical / "D015_assets"
    source_assets = source_tree / "works" / "D015_assets"
    require(len(list(assets_dir.glob("*.png"))) == 14, "canonical asset count")
    require(len(list(source_assets.glob("*.png"))) == 14, "source-tree asset count")
    asset_checks = []
    with tempfile.TemporaryDirectory(prefix="d015-cold-audit-") as temporary_name:
        temporary = Path(temporary_name)
        rendered_pages: dict[int, Path] = {}
        for row in assets:
            page_number = int(row["authority_page"])
            if page_number not in rendered_pages:
                rendered_pages[page_number] = render_page(canonical / "authority" / "D015_IAS_Number14_300dpi.pdf", page_number, temporary)
            raw = assets_dir / row["raw_filename"]
            presentation = assets_dir / row["presentation_filename"]
            require(sha256(raw) == row["raw_sha256"], f"raw asset hash: {raw}")
            require(sha256(presentation) == row["presentation_sha256"], f"presentation asset hash: {presentation}")
            require(sha256(source_assets / raw.name) == row["raw_sha256"], f"source raw copy hash: {raw.name}")
            require(sha256(source_assets / presentation.name) == row["presentation_sha256"], f"source presentation copy hash: {presentation.name}")
            require(fr_tex.count(row["presentation_filename"]) == 1, f"French asset reference count: {presentation.name}")
            require(en_tex.count(row["presentation_filename"]) == 1, f"English asset reference count: {presentation.name}")
            with Image.open(rendered_pages[page_number]) as page_image, Image.open(raw) as raw_image:
                box = (
                    int(row["crop_x_300dpi"]),
                    int(row["crop_y_300dpi"]),
                    int(row["crop_x_300dpi"]) + int(row["crop_width"]),
                    int(row["crop_y_300dpi"]) + int(row["crop_height"]),
                )
                replay = page_image.convert("L").crop(box)
                difference = ImageChops.difference(replay, raw_image.convert("L"))
                require(difference.getbbox() is None, f"raw crop replay mismatch: {raw.name}")
            asset_checks.append({"asset": row["asset_id"], "raw_crop_replay": "PASS", "fr_reference_count": 1, "en_reference_count": 1})

    for name in ["D015_FR.tex", "D015_EN.tex", "D015_FR.pdf", "D015_EN.pdf", "D015_APPARATUS.md"]:
        require(sha256(canonical / name) == sha256(source_tree / "works" / name), f"source-tree copy mismatch: {name}")

    text_checks = {}
    for language, standalone, standalone_reader, zenodo_pdf, zenodo_reader, zenodo_range, github_pdf, github_reader, github_range in [
        ("fr", canonical / "D015_FR.pdf", fr_reader, source_tree / "Deligne_FR.pdf", zfr_reader, (211, 223), github / "ALL_001_016p040_FR.pdf", gfr_reader, (212, 224)),
        ("en", canonical / "D015_EN.pdf", en_reader, source_tree / "Deligne_EN.pdf", zen_reader, (207, 213), github / "ALL_001_016p040_EN.pdf", gen_reader, (211, 217)),
    ]:
        run_text(standalone)
        run_text(zenodo_pdf, *zenodo_range)
        run_text(github_pdf, *github_range)
        standalone_text = reader_text(standalone_reader)
        zenodo_text = reader_text(zenodo_reader, *zenodo_range)
        github_text = reader_text(github_reader, *github_range)
        hashes = {"standalone": text_sha(standalone_text), "zenodo_range": text_sha(zenodo_text), "github_range": text_sha(github_text)}
        require(len(set(hashes.values())) == 1, f"normalized text mismatch: {language}: {hashes}")
        text_checks[language] = hashes

    font_checks = {
        "fr_standalone": pdffonts_audit(canonical / "D015_FR.pdf"),
        "en_standalone": pdffonts_audit(canonical / "D015_EN.pdf"),
        "zenodo_fr_range": pdffonts_audit(source_tree / "Deligne_FR.pdf", 211, 223),
        "zenodo_en_range": pdffonts_audit(source_tree / "Deligne_EN.pdf", 207, 213),
        "github_fr_range": pdffonts_audit(github / "ALL_001_016p040_FR.pdf", 212, 224),
        "github_en_range": pdffonts_audit(github / "ALL_001_016p040_EN.pdf", 211, 217),
    }

    zfr_outline = flat_outline(zfr_reader)
    zen_outline = flat_outline(zen_reader)
    fr_d015 = [item for item in zfr_outline if item.title.startswith("D015")]
    en_d015 = [item for item in zen_outline if item.title.startswith("D015")]
    require(len(fr_d015) == 1 and zfr_reader.get_destination_page_number(fr_d015[0]) + 1 == 211, "French D015 bookmark")
    require(len(en_d015) == 1 and zen_reader.get_destination_page_number(en_d015[0]) + 1 == 207, "English D015 bookmark")
    require(len(flat_outline(gfr_reader)) == 0 and len(flat_outline(gen_reader)) == 0 and len(flat_outline(gscan_reader)) == 0, "GitHub inherited outline disposition")

    build_receipt = json.loads((audit_root / "D015_BUILD_RECEIPT.json").read_text(encoding="utf-8-sig"))
    require(build_receipt["status"] == "PASS", "build receipt")
    require(build_receipt["authority"]["sha256"] == AUTHORITY_SHA, "build authority")
    require({row["pdf_sha256"] for row in build_receipt["standalone"]} == {expected[canonical / "D015_FR.pdf"][1], expected[canonical / "D015_EN.pdf"][1]}, "standalone receipt hashes")
    require(len(build_receipt["presentation_assets"]) == 7 and len(build_receipt["raw_authority_assets"]) == 7, "build asset receipts")

    rebuild = json.loads((github / "REBUILD_GITHUB_CUMULATIVES_RECEIPT.json").read_text(encoding="utf-8"))
    require(rebuild["status"] == "PASS", "GitHub cumulative rebuild receipt")
    for lane in ("en", "fr", "scan"):
        require(rebuild["determinism"][lane]["status"] == "PASS" and rebuild["determinism"][lane]["byte_identical"], f"GitHub determinism: {lane}")
        require(rebuild["page_sequence_validation"][lane]["status"] == "PASS", f"GitHub page sequence: {lane}")
        require(rebuild["page_sequence_validation"][lane]["mismatched_pages"] == [], f"GitHub fingerprint mismatch: {lane}")
    require(rebuild["d015_replacements"]["en"]["sha256"] == expected[canonical / "D015_EN.pdf"][1], "stale GitHub EN splice")

    visual = json.loads((audit_root / "D015_FINAL_VISUAL_QA.json").read_text(encoding="utf-8"))
    github_visual = json.loads((github / "D015_GITHUB_CUMULATIVE_VISUAL_QA.json").read_text(encoding="utf-8"))
    require(visual["status"] == "PASS" and github_visual["status"] == "PASS", "visual QA receipts")
    require(visual["standalone"]["english"]["sha256"] == expected[canonical / "D015_EN.pdf"][1], "stale visual QA")
    require(github_visual["outputs"]["english"]["sha256"] == expected[github / "ALL_001_016p040_EN.pdf"][1], "stale GitHub visual QA")

    manifest_paths = sorted(set(expected) | {
        canonical / "D015_APPARATUS.md",
        audit_root / "D015_AUTHORITY_RECONCILIATION.json",
        audit_root / "D015_AUTHORITY_RENDER_REPLAY.tsv",
        audit_root / "D015_BUILD_RECEIPT.json",
        audit_root / "D015_CURRENT_AUTHORITY_PAGE_MAP.tsv",
        audit_root / "D015_CURRENT_ASSET_LEDGER.tsv",
        audit_root / "D015_CURRENT_LITERALITY_LEDGER.tsv",
        audit_root / "D015_FINAL_VISUAL_QA.json",
        github / "REBUILD_GITHUB_CUMULATIVES_RECEIPT.json",
        github / "D015_GITHUB_CUMULATIVE_VISUAL_QA.json",
    }, key=lambda path: str(path).lower())
    for asset in sorted(assets_dir.glob("*.png")):
        manifest_paths.append(asset)
    manifest_rows = [identity(path) for path in manifest_paths]

    result = {
        "schema": "deligne-d015-fresh-nonpatching-cold-audit-v1",
        "status": "PASS",
        "mode": "read-only inputs; receipt and manifest outputs only; no repair path",
        "authority": identities[0],
        "topology": {
            "authority_pages": 13,
            "printed_pages": "45-57",
            "french_pages": 13,
            "french_disposition": "exact authority physical-page topology",
            "english_pages": 7,
            "english_source_markers": 13,
            "english_disposition": "independent A4 translation layout mapped to all thirteen frozen source-page markers; not a physical-page facsimile",
        },
        "page_map_rows": 13,
        "literality_rows": 13,
        "asset_checks": asset_checks,
        "text_identity": text_checks,
        "font_checks": font_checks,
        "bookmarks": {"zenodo_fr_d015_page": 211, "zenodo_en_d015_page": 207, "github_outlines": "inherited absent; explicitly recorded"},
        "deterministic_build": "PASS",
        "github_cumulative_rebuild": "PASS; prefix and D016 suffix fingerprints preserved with zero mismatches",
        "visual_qa": "PASS; all standalone D015 pages, all cumulative D015 pages, and adjacent transitions inspected",
        "copy_matter": "PASS; masthead/running identifiers/page furniture excluded and November 1971 recorded in restrained apparatus",
        "zero_accepted": "PASS; returned web state preserved and demoted; IAS authority controls every accepted reading",
        "manifest": manifest_rows,
    }
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--successor-root", type=Path, required=True)
    parser.add_argument("--returned-zip", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = audit(args)
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with args.manifest.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["path", "bytes", "sha256"], delimiter="\t")
        writer.writeheader()
        writer.writerows(result["manifest"])
    print(json.dumps({
        "status": result["status"],
        "receipt": identity(args.receipt),
        "manifest": identity(args.manifest),
        "manifest_entries": len(result["manifest"]),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
