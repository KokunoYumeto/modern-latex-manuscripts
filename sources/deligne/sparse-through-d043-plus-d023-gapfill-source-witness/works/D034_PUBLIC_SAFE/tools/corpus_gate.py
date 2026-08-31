#!/usr/bin/env python3
"""Read-only D034 corpus gate.

The candidate tree is never written. The optional JSON receipt must live outside
the candidate tree; this is enforced before the audit begins.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image
from pypdf import PdfReader


AUTHORITY_SHA256 = "c8b618a1da8b060e946c2fbcf6a1d36db73e4f3841330f8822043c593b7f4ece"
RETURNED_PACKET_SHA256 = "31f047419084ce5f18e0974b1daab98c3dafc19f0bc6c2772aaed9b059c0b725"

PDF_NAMES = {
    "french": "D034_french_diplomatic.pdf",
    "english": "D034_english_translation.pdf",
    "apparatus": "D034_restrained_apparatus.pdf",
}

SOURCE_NAMES = {
    "french_tex": "D034_french_diplomatic.tex",
    "english_tex": "D034_english_translation.tex",
    "apparatus_tex": "D034_restrained_apparatus.tex",
    "french_md": "D034_french_diplomatic.md",
    "english_md": "D034_english_translation.md",
    "apparatus_md": "D034_restrained_apparatus.md",
    "apparatus_tsv": "D034_restrained_apparatus.tsv",
}

INHERITED_SOURCE_MAP = {
    "french_tex": "editions/french_diplomatic.tex",
    "english_tex": "editions/english_translation.tex",
    "apparatus_tex": "apparatus/apparatus.tex",
    "french_md": "editions/french_diplomatic.md",
    "english_md": "editions/english_translation.md",
    "apparatus_md": "apparatus/apparatus.md",
    "apparatus_tsv": "apparatus/apparatus.tsv",
}

INHERITED_PDF_MAP = {
    "french": "editions/french_diplomatic.pdf",
    "english": "editions/english_translation.pdf",
    "apparatus": "apparatus/apparatus.pdf",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def tsv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def assert_contains(text: str, tokens: list[str], label: str) -> None:
    missing = [token for token in tokens if token not in text]
    assert not missing, f"{label} missing required tokens: {missing}"


def assert_absent(text: str, tokens: list[str], label: str) -> None:
    found = [token for token in tokens if token in text]
    assert not found, f"{label} contains forbidden tokens: {found}"


def page_markers(tex: str) -> list[tuple[int, int]]:
    return [
        (int(physical), int(printed))
        for printed, physical in re.findall(
            r"% BEGIN_SOURCE_PAGE printed=(\d+) physical=(\d+)", tex
        )
    ]


def md_page_markers(markdown: str) -> list[tuple[int, int]]:
    return [
        (int(physical), int(printed))
        for physical, printed in re.findall(
            r"<!-- BEGIN_PAGE_RECORD physical=(\d+) article=\d+ printed=(\d+) -->",
            markdown,
        )
    ]


def pdf_text(reader: PdfReader) -> str:
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def pdf_javascript_absent(reader: PdfReader) -> bool:
    root = reader.trailer["/Root"]
    names = root.get("/Names")
    if names is not None and "/JavaScript" in names:
        return False
    return "/OpenAction" not in root and "/AA" not in root


def embedded_font_count(pdf_path: Path) -> int:
    output = subprocess.check_output(
        ["pdffonts", str(pdf_path)], text=True, errors="replace"
    )
    rows = [line for line in output.splitlines()[2:] if line.strip()]
    assert rows, f"no font rows reported for {pdf_path.name}"
    nonembedded = [line for line in rows if not re.search(r"\byes\s+yes\s+(yes|no)\s+\d+\s+\d+\s*$", line)]
    assert not nonembedded, f"nonembedded or malformed font rows in {pdf_path.name}: {nonembedded}"
    return len(rows)


def page_ink_ratio(image_path: Path) -> float:
    with Image.open(image_path) as image:
        gray = image.convert("L")
        histogram = gray.histogram()
        ink = sum(histogram[:245])
        total = image.width * image.height
        assert image.width >= 900 and image.height >= 1300, (
            f"undersized render {image_path}: {image.width}x{image.height}"
        )
        return ink / total


def audit(candidate: Path, inherited: Path | None) -> dict:
    expected_mapping = [(physical, physical + 21) for physical in range(2, 13)]

    authority = candidate / "authority" / "20_AUTHORITY_DELIGNE_D034_CYCLES_HODGE_ABSOLUS_NUMDAM_12PP.pdf"
    assert authority.is_file(), authority
    assert sha256(authority) == AUTHORITY_SHA256
    authority_reader = PdfReader(str(authority))
    assert len(authority_reader.pages) == 12

    source = candidate / "source"
    texts = {key: read_text(source / name) for key, name in SOURCE_NAMES.items()}
    french_tex = texts["french_tex"]
    english_tex = texts["english_tex"]
    french_md = texts["french_md"]
    english_md = texts["english_md"]
    apparatus_tex = texts["apparatus_tex"]

    assert page_markers(french_tex) == expected_mapping
    assert page_markers(english_tex) == expected_mapping
    assert md_page_markers(french_md) == expected_mapping
    assert md_page_markers(english_md) == expected_mapping
    assert french_tex.count("% END_SOURCE_PAGE") == 11
    assert english_tex.count("% END_SOURCE_PAGE") == 11

    deterministic_tokens = [
        r"\pdfinfoomitdate=1",
        r"\pdftrailerid{}",
        r"\pdfsuppressptexinfo=15",
    ]
    for key in ("french_tex", "english_tex", "apparatus_tex"):
        assert_contains(texts[key], deterministic_tokens, key)

    common_math = [
        r"F^p=\bigoplus_{p'>p}H^{p',q}",
        r"\omega_1\cdot\eta_2",
        r"n\times2n",
        r"{}^tN\cdot\Omega",
        r"\sigma^{-1}(x)",
        r"p_K(\sigma,\varphi)",
        r"H^{2d}(X,\Q_\ell)(d)",
        r"\mu(\Gm)",
        r"\dim(G)<g+1",
        r"\dim(G)>2+\log_2(g)",
        r"\bigwedge_E^d M_\varphi",
        r"\operatorname{Inf}",
        r"\operatorname{Res}",
        r"\begin{tabularx}",
    ]
    assert_contains(french_tex, common_math, "French TeX")
    assert_contains(english_tex, common_math, "English TeX")

    assert_contains(
        french_tex,
        [
            "SOCIÉTÉ MATHÉMATIQUE DE FRANCE",
            "rédigé par J. L. BRYLINSKI",
            "l'ensemble de ces plongements complexes",
            "Corollaire}} (Borovoï)",
            "C.Q.F.D.",
            "RÉFÉRENCES",
            "J.-L. Brylinski",
        ],
        "French TeX",
    )
    assert_contains(
        english_tex,
        [
            "SOCIÉTÉ MATHÉMATIQUE DE FRANCE",
            "written up by J. L. BRYLINSKI",
            "the set of these complex embeddings",
            "Corollary}} (Borovoï)",
            "Q.E.D.",
            "REFERENCES",
            "J.-L. Brylinski",
        ],
        "English TeX",
    )
    assert french_tex.count("C.Q.F.D.") == 1
    assert english_tex.count("Q.E.D.") == 1

    reader_forbidden = [
        "Astérisque",
        r"\qed",
        r"X_{\bar",
        r"\leq g+1",
        r"\geq2",
        "Corollaire 1",
        "Corollary 1",
        "numdam.org",
        "tous droits réservés",
        "Numérisation de documents anciens",
    ]
    assert_absent(french_tex, reader_forbidden, "French TeX")
    assert_absent(english_tex, reader_forbidden, "English TeX")

    assert "SOCIÉTÉ MATHÉMATIQUE DE FRANCE" in apparatus_tex
    assert r"Mémoire n\textsuperscript{o} 2" in apparatus_tex
    assert "Mémoire n no." not in apparatus_tex
    assert r"ZERO\_ACCEPTED" in apparatus_tex

    apparatus_rows = tsv_rows(source / SOURCE_NAMES["apparatus_tsv"])
    expected_apparatus_ids = {
        "A001", "A002", "A002A", "A003", "A004", "A005", "A006", "A006A",
        "A007", "A008", "A008A", "A009", "A010", "A011", "A012", "A013",
        "A014", "A015", "A016", "A017", "A018",
    }
    assert {row["entry_id"] for row in apparatus_rows} == expected_apparatus_ids
    assert all(row["authority_sha256"].lower() == AUTHORITY_SHA256 for row in apparatus_rows)
    assert all(row["status"] == "COMPLETE" for row in apparatus_rows)

    pdf_results = {}
    expected_pages = {"french": 11, "english": 11, "apparatus": 2}
    for key, name in PDF_NAMES.items():
        final_pdf = candidate / "pdf" / name
        build_a = candidate / "build" / "A" / name
        build_b = candidate / "build" / "B" / name
        final_hash = sha256(final_pdf)
        assert sha256(build_a) == final_hash
        assert sha256(build_b) == final_hash
        reader = PdfReader(str(final_pdf))
        assert len(reader.pages) == expected_pages[key]
        assert not reader.is_encrypted
        assert pdf_javascript_absent(reader)
        metadata = reader.metadata or {}
        assert "/CreationDate" not in metadata and "/ModDate" not in metadata
        for page in reader.pages:
            width = float(page.mediabox.width)
            height = float(page.mediabox.height)
            assert abs(width - 595.276) < 0.05 and abs(height - 841.89) < 0.05
        text = pdf_text(reader)
        assert len(text.strip()) > 1000
        pdf_results[key] = {
            "filename": name,
            "sha256": final_hash,
            "bytes": final_pdf.stat().st_size,
            "pages": len(reader.pages),
            "embedded_font_rows": embedded_font_count(final_pdf),
        }

    french_pdf_text = pdf_text(PdfReader(str(candidate / "pdf" / PDF_NAMES["french"])))
    english_pdf_text = pdf_text(PdfReader(str(candidate / "pdf" / PDF_NAMES["english"])))
    assert_contains(french_pdf_text, ["SOCIÉTÉ MATHÉMATIQUE DE FRANCE", "rédigé par", "RÉFÉRENCES"], "French PDF text")
    assert_contains(english_pdf_text, ["written up by", "THE LANGUAGE OF MOTIVES", "REFERENCES"], "English PDF text")
    for forbidden in ["NUMDAM", "tous droits réservés", "numdam.org"]:
        assert forbidden not in french_pdf_text and forbidden not in english_pdf_text

    log_warnings = []
    for variant in ("A", "B"):
        for log in sorted((candidate / "build" / variant).glob("*.log")):
            content = read_text(log)
            hits = re.findall(
                r"^(?:Overfull|Underfull|LaTeX Warning:|Package .+ Warning:|! LaTeX Error:|! Emergency stop\.)[^\n]*",
                content,
                flags=re.MULTILINE,
            )
            log_warnings.extend(f"{variant}/{log.name}: {hit}" for hit in hits)
    assert not log_warnings, f"build warnings/errors: {log_warnings}"

    visual_rows = tsv_rows(candidate / "audit" / "pagewise_visual_qa.tsv")
    assert len(visual_rows) == 36
    assert all(row["inspection_result"] == "PASS" for row in visual_rows)
    render_results = []
    for row in visual_rows:
        render = candidate / row["render_path"]
        assert render.is_file(), render
        ratio = page_ink_ratio(render)
        assert ratio > 0.0005, f"apparently blank render: {render} ({ratio})"
        render_results.append(
            {
                "layer": row["layer"],
                "page": row["page"],
                "path": row["render_path"],
                "sha256": sha256(render),
                "ink_ratio": round(ratio, 8),
            }
        )

    math_rows = tsv_rows(candidate / "audit" / "mathematical_literality_checks.tsv")
    assert len(math_rows) == 28
    assert all(row["verdict"] == "PASS" for row in math_rows)

    inherited_comparison = None
    if inherited is not None:
        comparisons = []
        for key, inherited_rel in INHERITED_SOURCE_MAP.items():
            canonical_path = source / SOURCE_NAMES[key]
            inherited_path = inherited / inherited_rel
            canonical_hash = sha256(canonical_path)
            inherited_hash = sha256(inherited_path)
            assert canonical_hash != inherited_hash, f"canonical byte copy detected: {key}"
            comparisons.append(
                {
                    "canonical": f"source/{SOURCE_NAMES[key]}",
                    "canonical_sha256": canonical_hash,
                    "inherited": inherited_rel,
                    "inherited_sha256": inherited_hash,
                    "byte_identical": False,
                }
            )
        for key, inherited_rel in INHERITED_PDF_MAP.items():
            canonical_path = candidate / "pdf" / PDF_NAMES[key]
            inherited_path = inherited / inherited_rel
            assert sha256(canonical_path) != sha256(inherited_path), f"canonical inherited PDF detected: {key}"
        inherited_comparison = comparisons

    return {
        "schema": "deligne-d034-canonical-cold-audit-v1",
        "work_id": "DELIGNE_D034_CYCLES_HODGE_ABSOLUS",
        "mode": "FRESH_READ_ONLY_NONPATCHING",
        "authority_sha256": AUTHORITY_SHA256,
        "returned_packet_sha256": RETURNED_PACKET_SHA256,
        "authority_physical_pages": 12,
        "article_pages": 11,
        "copy_matter_excluded": True,
        "accepted_inherited_members": 0,
        "reader_page_mapping": [
            {"reader_page": i, "authority_physical": i + 1, "printed": i + 22}
            for i in range(1, 12)
        ],
        "pdfs": pdf_results,
        "ab_builds_byte_identical": True,
        "build_warning_count": 0,
        "visual_rows_checked": len(visual_rows),
        "render_hashes_checked": render_results,
        "mathematical_literality_checks": len(math_rows),
        "apparatus_entries": len(apparatus_rows),
        "image_fallback_required": False,
        "inherited_byte_comparisons": inherited_comparison,
        "result": "PASS",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate_root", type=Path)
    parser.add_argument("--inherited-root", type=Path)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()

    candidate = args.candidate_root.resolve()
    inherited = args.inherited_root.resolve() if args.inherited_root else None
    if args.json_out:
        json_out = args.json_out.resolve()
        try:
            json_out.relative_to(candidate)
        except ValueError:
            pass
        else:
            raise SystemExit("receipt must be outside the read-only candidate tree")
    result = audit(candidate, inherited)
    encoded = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(encoded, encoding="utf-8", newline="\n")
    sys.stdout.write(encoded)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
