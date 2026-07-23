#!/usr/bin/env python3
"""Build and validate the bounded SGA3 Expose VI A working release.

The live producer tree continues into Expose VI B. This script snapshots only
the independently reviewed VI A boundary (components 00-25), pins every source
and diagram identity, and builds in isolated temporary directories.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

from PIL import Image, ImageDraw
from pypdf import PdfReader
from pypdf.generic import ArrayObject, DictionaryObject, IndirectObject


RELEASE_DATE = "2026-07-23"
SOURCE_DATE_EPOCH = "1784764800"
AUTHORITY_BYTES = 427_698
AUTHORITY_SHA256 = (
    "6C8795572D1FC3B21BD02D24B1BFB20A8FB447475702C2674C96939B1EB69582"
)
INDEPENDENT_AUDIT_BYTES = 9_337
INDEPENDENT_AUDIT_SHA256 = (
    "98CE743C70746150A78982926933903B902405F5F0DFA3FE4899643227130630"
)

COMPONENTS: dict[str, tuple[int, str]] = {
    "00_expose_VIA_title_through_corollary_0_5_2_en.tex": (
        15082,
        "BAB6CF783EA5EB49698334DCDF88730256722143DA85F022F69412FD9DD36DC0",
    ),
    "01_expose_VIA_section1_through_prop131_en.tex": (
        10455,
        "7B7F408BD0981BE1585F5BC1E74686B87EED928999697B6875499642BEB9FD25",
    ),
    "02_expose_VIA_examples132_through_cor241_en.tex": (
        18701,
        "9FB44440111847C43389A7A7272741C7B8AF4686DFDCE949E01DC034FF12D704",
    ),
    "03_expose_VIA_section25_lemma251_prop252_en.tex": (
        10302,
        "C8A53E69938B0F350B8C1E3AE641772CC72825794D2FBCF9CF8C4D4FF14287BC",
    ),
    "04_expose_VIA_lemma253_prop254_en.tex": (
        8609,
        "725EBD9FFC7130D32F0120D263EB9DE62BF928378619B0F192BF696761163C31",
    ),
    "05_expose_VIA_section26_through_prop264_en.tex": (
        11762,
        "04CE7778DD24B8B16693C4B9EEC503C3DD6B857CABE897071B3E9536FCEA6F7F",
    ),
    "06_expose_VIA_theorem265_through_remark267_en.tex": (
        8301,
        "26BC4CA502B6F0CA59DC1465C7789E389B9726F484E3B45EC0C28298E1CB4297",
    ),
    "07_expose_VIA_section31_theorem32_statement_en.tex": (
        6272,
        "6D9CAA0384232FA8F76F5399684BE86443C05DA09001C3CBF21CC963711CF301",
    ),
    "08_expose_VIA_section321_quasisection_descent_en.tex": (
        6573,
        "4B9BDD94A0D245781FF7FDCA9CC0CC69DCB22F795C0085055B5A14919E114550",
    ),
    "09_expose_VIA_section322_induction_en.tex": (
        1780,
        "779644E2C8D30376AE203D5AE48F0AE8033C751D00C5680C4C3A8B13D5CEDADA",
    ),
    "10_expose_VIA_section323_descent_en.tex": (
        3571,
        "6F3AD7544E8D7BA12F6F2EA029E326B6AE53C818AB7E233FB72496E0070FDC52",
    ),
    "11_expose_VIA_sections324_325_en.tex": (
        2363,
        "96C2FFA4D50B7B5EB72B433F51E2BACB459987C19B6926C84BEC8A7686F25872",
    ),
    "12_expose_VIA_section33_theorems_corollary_en.tex": (
        5435,
        "C05BFE2EB89C8487DBF95924949094AEBAB9583B203112AC37FFBD1E8AC91E3C",
    ),
    "13_expose_VIA_section4_opening_par41_en.tex": (
        2252,
        "8110C9C1A2945782C6F15D007195424DDC0D8058C963A57A59FF2B1EC21B4E7C",
    ),
    "14_expose_VIA_par42_saturation_identity_component_en.tex": (
        2261,
        "681D6A45AC548EAE0A124A87C1EAC5C0C73792B1A618ACF7F213EE40CB634282",
    ),
    "15_expose_VIA_par43_identity_saturation_quotient_en.tex": (
        5351,
        "9A705D76298A93C62278A75A11628D4FE1F2C3C606E02C0361FE02AFFA0BF198",
    ),
    "16_expose_VIA_par44_arbitrary_component_descent_en.tex": (
        1737,
        "A3A54E1FE3F3FBAD6ADFA54BEBA09AF0B3031C72F15B16EB02C2A0D4F7DA0494",
    ),
    "17_expose_VIA_par45_46_base_change_en.tex": (
        4291,
        "B30D9CE8EA3F97BC6CA2F8BB2372ADE41A2BE66AAAE23756EFE973D8B1CC962C",
    ),
    "18_expose_VIA_par47_flat_base_change_en.tex": (
        2173,
        "216CA347326C1022A3B3958D3E0EBCD93D84BB1142DC678BDE0A1480E1602FFA",
    ),
    "19_expose_VIA_section5_opening_par51_en.tex": (
        2651,
        "A77ED1473245BB6C6F85944AD4DD0B487C3F5BC4AD0A3BBF956E470D9E7DCEA9",
    ),
    "20_expose_VIA_par52_group_structure_en.tex": (
        1195,
        "A7F759623C142523FD88ABFC201848296666FE089CD0760B841B5503F3393B45",
    ),
    "21_expose_VIA_par53_correspondences_en.tex": (
        2948,
        "C17A1609C327822259A51414761C9247A05BFAF64C9B6B4990E210DFA64FC975",
    ),
    "22_expose_VIA_par54_abelian_categories_en.tex": (
        5576,
        "1388DDCD2DF10C2777ABFEE8EB47D8EB52828FEB4FD5247E0470D7F6567EB7E2",
    ),
    "23_expose_VIA_par55_56_en.tex": (
        6123,
        "60D58D3360258E6B8CB122DF5EF590422FB4AA570F8B1FFB25292E4E795A70CD",
    ),
    "24_expose_VIA_section6_through_prop64_en.tex": (
        6379,
        "229592284119DF13ADEC4AA559DF04D00C4F350D99B16A9E113A8575B9732542",
    ),
    "25_expose_VIA_theorem65_through_bibliography_en.tex": (
        8799,
        "5B5CE731C76B1EBB8F4785A8009CE7112D02116C9FC06D0C71EF38179FB14860",
    ),
}

FIGURES: dict[str, tuple[int, str]] = {
    "figures/Exp6A_localp003_cartesian_square.png": (
        5412,
        "87D10BB073F6481D936AA1D4CA9C5E6A2373A8B2E4CD6AA496CF415EE7C0986B",
    ),
    "figures/Exp6A_localp013_lemma253_basechange_cartesian_square.png": (
        2381,
        "7E40D1B122956B5A0F55D2B66A436B1B4E5B8C44017DA6D8F1A70877155CD846",
    ),
    "figures/Exp6A_localp014_lemma253_translation_localrings_square.png": (
        2999,
        "A3CD5BAB5AB4B6ED03FBE0CCFA5796CD77CC1FFA73B8A54FF63C1D1F31A92A09",
    ),
    "figures/Exp6A_localp015_prop254_stabilizer_cartesian_square.png": (
        2659,
        "9F440F03D2B1DE11BB9EE602C706812E47A99DB1748686EEA8A1073F6EE97812",
    ),
    "figures/Exp6A_localp020_prop266_cartesian_square.png": (
        6539,
        "68554105155531E8988528627A905CF356FF6C98EAABDC1D0CD3CA22C5959295",
    ),
    "figures/Exp6A_localp020_section31_lambda_composite.png": (
        5007,
        "4172DBDBCE8BFFB05FD624EF0F31DCFA6077E52D199A224524C2D6A762AC2193",
    ),
    "figures/Exp6A_localp020_section31_groupoid.png": (
        8039,
        "FF8CDF6C065DC8DD6878C01FB3E84C6FF7B9D986303A03AD34DF72A247ED956A",
    ),
    "figures/Exp6A_localp021_theorem32_exact_sequence.png": (
        5020,
        "5AB7152938AFB32F44172D969CDCA1551BAFD649532B434CEC33BA8E50B6122C",
    ),
    "figures/Exp6A_localp023_section321_descent_equivalence_relation.png": (
        6836,
        "AE70E648C7FD4D0E1204AC286A3CE8B4A96B99FB15D1A8870755B98B74513890",
    ),
    "figures/Exp6A_localp024_section323_exact_descent_diagram.png": (
        21194,
        "4C6B0FE9AF8E0B235B81536DD50186B63A85595D9DD3468740A1C63EE1BD8CB6",
    ),
    "figures/Exp6A_localp025_section325_cartesian_square.png": (
        6611,
        "187CE16E08B856EAC2E64E1BBC7C39F61E7724DBA3E8457F516993681CC311B5",
    ),
    "figures/Exp6A_localp025_theorem332_exact_sequence.png": (
        4020,
        "DC2D38AEB9E64897CD982A45CDEB61D1C53DB9F3EDA90DE78384BB805A7EB28E",
    ),
    "figures/Exp6A_localp027_par43_G0_groupoid.png": (
        6225,
        "93A1B44475587097A4EDC4B2FAD8123F29ECAE5E1B8659B562B1F6D70F57CB1E",
    ),
    "figures/Exp6A_localp028_par43_span.png": (
        5296,
        "6EE884335301222AFEE2BB0B8A7335E5942E66A331AEBDD860A061D7E0B0F3FB",
    ),
    "figures/Exp6A_localp028_par43_V_groupoid.png": (
        6868,
        "48642CAED95CFD0DD548B8913039B05C001FC2B496E9C887687728B6021EBC04",
    ),
    "figures/Exp6A_localp028_par43_composite.png": (
        8011,
        "2E3B0931C660D2F884DA4FE4F436ECAC0149E1A6D8D2B451EE7BF3ED90CA6D47",
    ),
    "figures/Exp6A_localp030_section51_action_diagram.png": (
        16294,
        "36A9019F501F7F9D666447D84DA0F6F0B4EEEC0D06D043B18A05F69C362C249A",
    ),
    "figures/Exp6A_localp032_prop541_factorization.png": (
        4891,
        "963D8C96DEDE10CFDA58B44B82CFA07C6282F2077434154C1AAD486ED277957E",
    ),
    "figures/Exp6A_localp034_prop562_quotient_square.png": (
        6190,
        "9C782D68206C74487086322DFD287EB6388309600A831F2E55C1C6EB61D9E96D",
    ),
    "figures/Exp6A_localp034_prop562_local_flatness_square.png": (
        8360,
        "C2AD3A77396FFD7540F2112023F7A5E3D3B0023574EBB34658473B4EEBFBB550",
    ),
    "figures/Exp6A_localp035_prop64_factorization.png": (
        2155,
        "9572615C76C9128254A449463E068189ECB07399E1D82A045E6F6CA3C78C4127",
    ),
    "figures/Exp6A_localp037_cor66_square.png": (
        2746,
        "753A04ACC1E4E8884C9EF0D86DE601248C82DE8678A289782AB22F5BA455C107",
    ),
    "figures/Exp6A_localp037_cor67_factorization.png": (
        2522,
        "3BB2D5AE77FD4DD20B2B9FA59B88A4BFB3E9C1B7AB4A3D87700F2FCC101EF68B",
    ),
}

MASTER_NAME = "SGA3_English_Expose_VIA_Loop1_Working_20260723.tex"
PDF_NAME = "SGA3_English_Expose_VIA_Loop1_Working_20260723.pdf"
ZIP_NAME = "SGA3_English_Expose_VIA_Loop1_Working_Source_Evidence_20260723.zip"

PRIVACY_PATTERNS = (
    re.compile(r"C:\\Users\\", re.I),
    re.compile(r"C:/Users/", re.I),
    re.compile(r"C:\\IL_GitHub", re.I),
    re.compile(r"AppData", re.I),
    re.compile(r"Papors", re.I),
    re.compile(r"Chatnotes", re.I),
    re.compile(r"CLAUDE PLEASE", re.I),
    re.compile(r"(?:source_)?thread_id", re.I),
    re.compile(r"\bBearer\s+[A-Za-z0-9._-]+", re.I),
    re.compile(r"\b(?:access_token|api[_-]?key)\b", re.I),
)


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def identity(path: Path) -> dict[str, Any]:
    return {"bytes": path.stat().st_size, "sha256": sha256_path(path)}


def assert_identity(path: Path, expected_bytes: int, expected_sha: str) -> None:
    actual = identity(path)
    if actual["bytes"] != expected_bytes or actual["sha256"] != expected_sha:
        raise RuntimeError(
            f"Identity mismatch for {path}: {actual}, "
            f"expected bytes={expected_bytes} sha256={expected_sha}"
        )


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def write_json(path: Path, value: Any) -> None:
    write_text(path, json.dumps(value, ensure_ascii=True, indent=2))


def csv_cell_safe(value: Any) -> str:
    text = str(value)
    if text.startswith(("=", "+", "-", "@")):
        return "'" + text
    return text


def write_csv(path: Path, fieldnames: list[str], rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=fieldnames,
            lineterminator="\r\n",
            quoting=csv.QUOTE_MINIMAL,
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({key: csv_cell_safe(row.get(key, "")) for key in fieldnames})


def collect_files(root: Path, exclude: set[str] | None = None) -> list[Path]:
    excluded = exclude or set()
    return sorted(
        (
            path
            for path in root.rglob("*")
            if path.is_file() and path.relative_to(root).as_posix() not in excluded
        ),
        key=lambda path: path.relative_to(root).as_posix(),
    )


def aggregate_identity(root: Path, files: Iterable[Path]) -> str:
    digest = hashlib.sha256()
    for path in files:
        rel = path.relative_to(root).as_posix()
        row = f"{rel}\t{path.stat().st_size}\t{sha256_path(path)}\n"
        digest.update(row.encode("utf-8"))
    return digest.hexdigest().upper()


def validate_source_inputs(source_root: Path, authority_pdf: Path) -> dict[str, Any]:
    assert_identity(authority_pdf, AUTHORITY_BYTES, AUTHORITY_SHA256)

    component_dir = source_root / "tex" / "components"
    selected = sorted(
        path for path in component_dir.glob("*.tex") if path.name[:2].isdigit()
        and int(path.name[:2]) <= 25
    )
    if [path.name for path in selected] != list(COMPONENTS):
        raise RuntimeError("The VI A component set is not exactly components 00-25.")
    for path in selected:
        assert_identity(path, *COMPONENTS[path.name])

    combined_text = "\n".join(path.read_text(encoding="utf-8") for path in selected)
    include_pattern = re.compile(
        r"\\includegraphics(?:\s*\[[^\]]*\])?(?:\s|%[^\n]*\n)*"
        r"\{\s*([^}]+?)\s*\}",
        re.S,
    )
    references = [
        re.sub(r"\s+", "", match.group(1))
        for match in include_pattern.finditer(combined_text)
    ]
    if len(references) != 23 or len(set(references)) != 23:
        raise RuntimeError(
            f"Expected 23 unique VI A figure references, found {len(references)} "
            f"references / {len(set(references))} unique."
        )
    if set(references) != set(FIGURES):
        missing = sorted(set(FIGURES) - set(references))
        extra = sorted(set(references) - set(FIGURES))
        raise RuntimeError(f"Figure reference mismatch: missing={missing}, extra={extra}")
    for relative in references:
        assert_identity(source_root / relative, *FIGURES[relative])

    audit = (
        source_root
        / "qa"
        / "component22_25_independent_review"
        / "INDEPENDENT_QA_PASS.md"
    )
    assert_identity(audit, INDEPENDENT_AUDIT_BYTES, INDEPENDENT_AUDIT_SHA256)

    pin_files = selected + [source_root / rel for rel in sorted(FIGURES)] + [audit]
    pin_rows = []
    for path in pin_files:
        pin_rows.append(
            {
                "path": path.relative_to(source_root).as_posix(),
                **identity(path),
            }
        )
    pin_digest = hashlib.sha256(
        "".join(
            f"{row['path']}\t{row['bytes']}\t{row['sha256']}\n"
            for row in pin_rows
        ).encode("utf-8")
    ).hexdigest().upper()
    return {
        "components": selected,
        "figures": references,
        "audit": audit,
        "pin_rows": pin_rows,
        "pin_digest": pin_digest,
    }


def master_tex() -> str:
    inputs = "\n".join(
        f"\\input{{tex/components/{Path(name).stem}}}" for name in COMPONENTS
    )
    inputs = textwrap.indent(inputs, "        ")
    return textwrap.dedent(
        rf"""
        \documentclass[11pt,a4paper,oneside]{{book}}

        \usepackage[T1]{{fontenc}}
        \usepackage[utf8]{{inputenc}}
        \usepackage[english]{{babel}}
        \usepackage[a4paper,inner=30mm,outer=27mm,top=28mm,bottom=30mm]{{geometry}}
        \usepackage{{amsmath,amssymb,amsthm,mathrsfs,mathtools}}
        \usepackage{{graphicx,float}}
        \usepackage{{unicode-math}}
        \setmathfont{{Latin Modern Math}}
        \usepackage[hidelinks,hypertexnames=false,pdfstartview={{}},linktoc=page]{{hyperref}}
        \ifdefined\pdfgentounicode
          \input{{glyphtounicode}}
          \pdfgentounicode=1
        \fi

        \hypersetup{{
          pdftitle={{SGA 3 Expose VI A - English Working Translation and PDF Reconstruction}},
          pdfauthor={{Interlanguage project; machine-assisted contributions from Anthropic Claude and OpenAI Codex / ChatGPT}},
          pdfsubject={{Bounded Loop-1 working checkpoint through the Expose VI A bibliography}},
          pdfkeywords={{SGA 3, algebraic geometry, algebraic groups, group schemes, English translation, working checkpoint}}
        }}

        \setlength{{\emergencystretch}}{{3em}}
        \raggedbottom

        \title{{Seminar on Algebraic Geometry 3\\
          \large Expos\'e VI A: Generalities on Algebraic Groups and Group Schemes\\[0.75em]
          \normalsize English Working Translation and PDF Reconstruction --- Loop 1}}
        \author{{Interlanguage project\\
          \small Machine-assisted contributions from Anthropic Claude and OpenAI Codex / ChatGPT}}
        \date{{2026}}

        \begin{{document}}
        \frontmatter
        \maketitle

        \chapter*{{Checkpoint and reconstruction note}}
        \addcontentsline{{toc}}{{chapter}}{{Checkpoint and reconstruction note}}
        This bounded reader contains complete Expos\'e VI A through its
        bibliography. Expos\'e VI B and all later expos\'es are outside this
        checkpoint and remain separate work.

        The Polo--Gille Expos\'e-VI-A PDF controls the French text, numbering,
        formulas, source notes, page locations, and diagram appearance. OCR was
        used only as a locator and drafting witness. The Loop-1 diagrams are
        tightly bounded source-derived images; native \LaTeX{{}} reconstruction
        remains later Loop-2 work.

        Jacob C. Reinhold's English Markdown from \texttt{{jcreinhold/sga}} at
        commit \texttt{{e7a259f3\allowbreak f8608ad3\allowbreak edf9bf6e\allowbreak
        ead3fd50\allowbreak 4dd2d23e}} is credited
        comparison and drafting lineage under his stated CC BY 4.0 terms for
        his translation contribution. It is not source authority or independent
        corroboration.

        This is a scholarly working checkpoint, not complete SGA 3, a critical
        edition, rights clearance, or exhaustive convention-v2 reference
        certification. Rights in the underlying French work, Polo--Gille
        re-edition, and source-derived diagram material remain with their
        holders.

        \tableofcontents
        \mainmatter

{inputs}

        \end{{document}}
        """
    ).strip() + "\n"


def prepare_build_source(source_root: Path, destination: Path, pins: dict[str, Any]) -> None:
    destination.mkdir(parents=True)
    write_text(destination / MASTER_NAME, master_tex())
    component_target = destination / "tex" / "components"
    component_target.mkdir(parents=True)
    for component in pins["components"]:
        shutil.copy2(component, component_target / component.name)
    for relative in pins["figures"]:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_root / relative, target)


def run_xelatex_build(
    input_source: Path,
    build_root: Path,
    xelatex: Path,
) -> dict[str, Any]:
    shutil.copytree(input_source, build_root)
    env = os.environ.copy()
    env["SOURCE_DATE_EPOCH"] = SOURCE_DATE_EPOCH
    env["FORCE_SOURCE_DATE"] = "1"
    env["TZ"] = "UTC"
    pass_records = []
    for pass_number in range(1, 4):
        completed = subprocess.run(
            [
                str(xelatex),
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                MASTER_NAME,
            ],
            cwd=build_root,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        output = completed.stdout.decode("utf-8", errors="replace")
        pass_records.append(
            {
                "pass": pass_number,
                "exit_code": completed.returncode,
                "console_bytes": len(completed.stdout),
                "console_sha256": hashlib.sha256(completed.stdout).hexdigest().upper(),
            }
        )
        if completed.returncode != 0:
            raise RuntimeError(
                f"XeLaTeX pass {pass_number} failed:\n{output[-8000:]}"
            )

    pdf = build_root / PDF_NAME
    generated_pdf = build_root / f"{Path(MASTER_NAME).stem}.pdf"
    if not generated_pdf.exists():
        raise RuntimeError("XeLaTeX did not produce the expected PDF.")
    if generated_pdf != pdf:
        generated_pdf.replace(pdf)

    log_path = build_root / f"{Path(MASTER_NAME).stem}.log"
    log = log_path.read_text(encoding="utf-8", errors="replace")
    diagnostic_patterns = {
        "fatal_errors": r"(?m)^!",
        "undefined_references": r"(?i)undefined references?",
        "multiply_defined_labels": r"(?i)multiply defined",
        "missing_characters": r"(?i)missing character",
        "overfull_boxes": r"(?i)overfull \\[hv]box",
        "underfull_boxes": r"(?i)underfull \\[hv]box",
        "rerun_warnings": r"(?i)(rerun to get|label\\(s\\) may have changed)",
    }
    diagnostics = {
        key: len(re.findall(pattern, log))
        for key, pattern in diagnostic_patterns.items()
    }
    if any(diagnostics.values()):
        log_lines = log.splitlines()
        context = []
        for index, line in enumerate(log_lines):
            if re.search(
                r"(?i)(^!|undefined references?|multiply defined|"
                r"missing character|overfull \\[hv]box|underfull \\[hv]box|"
                r"rerun to get|label\(s\) may have changed)",
                line,
            ):
                context.extend(log_lines[index : min(index + 5, len(log_lines))])
        raise RuntimeError(
            f"Build diagnostics are not clean: {diagnostics}\n"
            + "\n".join(context[:30])
        )
    return {
        "pdf": pdf,
        "log": log_path,
        "passes": pass_records,
        "diagnostics": diagnostics,
    }


def dereference(value: Any) -> Any:
    return value.get_object() if isinstance(value, IndirectObject) else value


def inspect_pdf(pdf: Path) -> dict[str, Any]:
    reader = PdfReader(str(pdf))
    if reader.is_encrypted:
        raise RuntimeError("Reader PDF is encrypted.")
    page_count = len(reader.pages)
    if page_count < 40 or page_count > 50:
        raise RuntimeError(f"Unexpected VI A page count: {page_count}")

    blank_pages = []
    replacement_pages = []
    nul_pages = []
    geometry_failures = []
    link_actions = Counter()
    link_rectangles = 0
    image_objects: set[tuple[int, int] | str] = set()
    font_objects: set[tuple[int, int] | str] = set()
    extracted_text = []

    for index, page in enumerate(reader.pages, start=1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        if abs(width - 595.28) > 0.2 or abs(height - 841.89) > 0.2:
            geometry_failures.append(
                {"page": index, "width": width, "height": height}
            )
        text = page.extract_text() or ""
        extracted_text.append(text)
        if not text.strip():
            blank_pages.append(index)
        if "\ufffd" in text:
            replacement_pages.append(index)
        if "\x00" in text:
            nul_pages.append(index)

        resources = dereference(page.get("/Resources", DictionaryObject()))
        fonts = dereference(resources.get("/Font", DictionaryObject()))
        for font in fonts.values():
            if isinstance(font, IndirectObject):
                font_objects.add((font.idnum, font.generation))
            else:
                font_objects.add(repr(font)[:80])
        xobjects = dereference(resources.get("/XObject", DictionaryObject()))
        for xobject in xobjects.values():
            resolved = dereference(xobject)
            if resolved.get("/Subtype") == "/Image":
                if isinstance(xobject, IndirectObject):
                    image_objects.add((xobject.idnum, xobject.generation))
                else:
                    image_objects.add(repr(xobject)[:80])

        annotations = dereference(page.get("/Annots", ArrayObject()))
        for annotation in annotations:
            resolved = dereference(annotation)
            if resolved.get("/Subtype") != "/Link":
                continue
            link_rectangles += 1
            action = dereference(resolved.get("/A", DictionaryObject()))
            if action:
                link_actions[str(action.get("/S", "unknown"))] += 1
            elif "/Dest" in resolved:
                link_actions["/Dest"] += 1
            else:
                link_actions["missing"] += 1

    if geometry_failures:
        raise RuntimeError(f"Non-A4 pages found: {geometry_failures}")
    if blank_pages:
        raise RuntimeError(f"Text-empty pages found: {blank_pages}")
    if link_actions.get("/URI", 0) or link_actions.get("missing", 0):
        raise RuntimeError(f"Unexpected PDF link actions: {dict(link_actions)}")

    root = dereference(reader.trailer["/Root"])
    names = dereference(root.get("/Names", DictionaryObject()))
    embedded_files = bool(names.get("/EmbeddedFiles"))
    javascript = bool(names.get("/JavaScript"))
    acroform = bool(root.get("/AcroForm"))
    additional_actions = bool(root.get("/AA"))
    open_action = bool(root.get("/OpenAction"))
    if any((embedded_files, javascript, acroform, additional_actions, open_action)):
        raise RuntimeError(
            "Unexpected active/attached PDF surface: "
            f"embedded={embedded_files}, javascript={javascript}, "
            f"acroform={acroform}, aa={additional_actions}, open={open_action}"
        )

    metadata = {str(key): str(value) for key, value in (reader.metadata or {}).items()}
    if "Expose VI A" not in metadata.get("/Title", ""):
        raise RuntimeError(f"Expected publication title is absent: {metadata}")
    joined_text = "\n".join(extracted_text)
    if "\ufffd" in joined_text:
        raise RuntimeError(
            "PyPDF extraction contains replacement characters: "
            f"replacement_pages={replacement_pages}, "
            f"replacement_count={joined_text.count(chr(0xfffd))}"
        )
    pdf_privacy_hits = []
    privacy_surface = joined_text + "\n" + json.dumps(metadata, ensure_ascii=True)
    for pattern in PRIVACY_PATTERNS:
        if pattern.search(privacy_surface):
            pdf_privacy_hits.append(pattern.pattern)
    if pdf_privacy_hits:
        raise RuntimeError(f"PDF privacy scan failed: {pdf_privacy_hits}")

    return {
        "pages": page_count,
        "a4_pages": page_count,
        "blank_pages": blank_pages,
        "named_destinations": len(reader.named_destinations),
        "link_rectangles": link_rectangles,
        "link_actions": dict(link_actions),
        "unique_font_resources": len(font_objects),
        "unique_image_objects": len(image_objects),
        "embedded_files": embedded_files,
        "javascript": javascript,
        "acroform": acroform,
        "additional_actions": additional_actions,
        "open_action": open_action,
        "metadata": metadata,
        "privacy_hits": pdf_privacy_hits,
        "pypdf_nul_pages": nul_pages,
        "pypdf_nul_count": joined_text.count("\x00"),
        "extracted_text_sha256": hashlib.sha256(
            joined_text.encode("utf-8")
        ).hexdigest().upper(),
    }


def inspect_text_extraction(pdf: Path, pdftotext: Path) -> dict[str, Any]:
    completed = subprocess.run(
        [str(pdftotext), "-layout", str(pdf), "-"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "pdftotext failed:\n"
            + completed.stderr.decode("utf-8", errors="replace")[-4000:]
        )
    text = completed.stdout.decode("utf-8", errors="strict")
    forbidden = Counter(
        ord(char)
        for char in text
        if ord(char) < 32 and char not in ("\t", "\n", "\r", "\f")
    )
    if "\ufffd" in text or "\x00" in text or forbidden:
        contexts = []
        for index, char in enumerate(text):
            if ord(char) >= 32 or char in ("\t", "\n", "\r", "\f"):
                continue
            page = text[:index].count("\f") + 1
            context = text[max(0, index - 45) : min(len(text), index + 46)]
            context = context.replace("\n", " ").replace("\r", " ")
            contexts.append(
                {
                    "page": page,
                    "codepoint": ord(char),
                    "context": repr(context),
                }
            )
        raise RuntimeError(
            "Canonical pdftotext extraction contains forbidden controls: "
            f"replacement={text.count(chr(0xfffd))}, nul={text.count(chr(0))}, "
            f"other={dict(forbidden)}, contexts={contexts}"
        )
    privacy_hits = []
    for pattern in PRIVACY_PATTERNS:
        if pattern.search(text):
            privacy_hits.append(pattern.pattern)
    if privacy_hits:
        raise RuntimeError(f"Canonical extracted-text privacy scan failed: {privacy_hits}")
    return {
        "bytes": len(completed.stdout),
        "sha256": hashlib.sha256(completed.stdout).hexdigest().upper(),
        "form_feeds": text.count("\f"),
        "replacement_characters": text.count("\ufffd"),
        "nul_characters": text.count("\x00"),
        "forbidden_controls": dict(forbidden),
        "privacy_hits": privacy_hits,
    }


def inspect_fonts(pdf: Path, pdffonts: Path) -> dict[str, Any]:
    completed = subprocess.run(
        [str(pdffonts), str(pdf)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "pdffonts failed:\n"
            + completed.stdout.decode("utf-8", errors="replace")[-4000:]
        )
    output = completed.stdout.decode("utf-8", errors="replace")
    rows = []
    row_pattern = re.compile(
        r"\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$",
        re.I,
    )
    for line in output.splitlines()[2:]:
        match = row_pattern.search(line)
        if not match:
            continue
        rows.append(
            {
                "embedded": match.group(1).lower() == "yes",
                "subset": match.group(2).lower() == "yes",
                "unicode": match.group(3).lower() == "yes",
            }
        )
    if not rows:
        raise RuntimeError("pdffonts returned no parseable font rows.")
    failures = [row for row in rows if not all(row.values())]
    if failures:
        raise RuntimeError(f"Font embedding/subset/Unicode failures: {failures}")
    return {
        "rows": len(rows),
        "embedded": sum(row["embedded"] for row in rows),
        "subset": sum(row["subset"] for row in rows),
        "unicode": sum(row["unicode"] for row in rows),
        "output_sha256": hashlib.sha256(completed.stdout).hexdigest().upper(),
    }


def scan_privacy(root: Path, pdf_text: str | None = None) -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    text_extensions = {".tex", ".md", ".csv", ".json", ".jsonl", ".txt", ".log"}
    for path in collect_files(root):
        if path.suffix.lower() not in text_extensions:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in PRIVACY_PATTERNS:
            if pattern.search(text):
                hits.append(
                    {
                        "path": path.relative_to(root).as_posix(),
                        "pattern": pattern.pattern,
                    }
                )
    if pdf_text is not None:
        for pattern in PRIVACY_PATTERNS:
            if pattern.search(pdf_text):
                hits.append({"path": PDF_NAME, "pattern": pattern.pattern})
    return hits


def render_pdf(
    pdf: Path,
    qa_root: Path,
    pdftoppm: Path,
    page_count: int,
) -> dict[str, Any]:
    render_root = qa_root / "rendered_pages"
    render_root.mkdir(parents=True)
    prefix = render_root / "page"
    completed = subprocess.run(
        [str(pdftoppm), "-png", "-r", "120", str(pdf), str(prefix)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "pdftoppm failed:\n"
            + completed.stdout.decode("utf-8", errors="replace")[-4000:]
        )
    pages = sorted(render_root.glob("page-*.png"))
    if len(pages) != page_count:
        raise RuntimeError(f"Expected {page_count} page renders, found {len(pages)}.")

    contacts = []
    group_size = 12
    thumb_width = 300
    margin = 18
    label_height = 28
    for group_index in range(0, len(pages), group_size):
        group = pages[group_index : group_index + group_size]
        sample = Image.open(group[0])
        ratio = thumb_width / sample.width
        thumb_height = round(sample.height * ratio)
        sample.close()
        columns = 3
        rows = (len(group) + columns - 1) // columns
        canvas = Image.new(
            "RGB",
            (
                margin + columns * (thumb_width + margin),
                margin + rows * (thumb_height + label_height + margin),
            ),
            "white",
        )
        draw = ImageDraw.Draw(canvas)
        for offset, page_path in enumerate(group):
            image = Image.open(page_path).convert("RGB")
            image.thumbnail((thumb_width, thumb_height), Image.Resampling.LANCZOS)
            column = offset % columns
            row = offset // columns
            x = margin + column * (thumb_width + margin)
            y = margin + row * (thumb_height + label_height + margin)
            canvas.paste(image, (x, y + label_height))
            page_number = group_index + offset + 1
            draw.text((x, y + 6), f"Page {page_number}", fill="black")
            image.close()
        contact_path = qa_root / f"contact-{group_index // group_size + 1:02d}.png"
        canvas.save(contact_path, format="PNG", optimize=True)
        canvas.close()
        contacts.append(contact_path)
    return {
        "page_renders": len(pages),
        "contacts": [
            {
                "path": path.name,
                **identity(path),
            }
            for path in contacts
        ],
        "render_bytes": sum(path.stat().st_size for path in pages),
    }


def write_source_controls(
    source_stage: Path,
    source_root: Path,
    pins: dict[str, Any],
    build: dict[str, Any],
    pdf_info: dict[str, Any],
    text_info: dict[str, Any],
    font_info: dict[str, Any],
) -> dict[str, Any]:
    evidence = source_stage / "evidence"
    evidence.mkdir(parents=True, exist_ok=True)
    shutil.copy2(
        pins["audit"],
        evidence / "INDEPENDENT_VIA_CLOSING_RANGE_QA_PASS.md",
    )

    component_rows = []
    for index, name in enumerate(COMPONENTS):
        path = source_stage / "tex" / "components" / name
        component_rows.append(
            {
                "component_index": index,
                "relative_path": path.relative_to(source_stage).as_posix(),
                **identity(path),
                "scope": "SGA3 Expose VI A",
                "status": "final_pinned_working_component",
            }
        )
    write_csv(
        source_stage / "controls" / "COMPONENT_MANIFEST.csv",
        [
            "component_index",
            "relative_path",
            "bytes",
            "sha256",
            "scope",
            "status",
        ],
        component_rows,
    )

    figure_rows = []
    for relative in pins["figures"]:
        path = source_stage / relative
        page_match = re.search(r"localp(\d{3})", relative)
        with Image.open(path) as image:
            width, height = image.size
            mode = image.mode
        figure_rows.append(
            {
                "relative_path": relative,
                **identity(path),
                "source_pdf_sha256": AUTHORITY_SHA256,
                "source_local_page": int(page_match.group(1)) if page_match else "",
                "width_px": width,
                "height_px": height,
                "image_mode": mode,
                "role": "required_loop1_source_derived_diagram",
                "rights_status": "underlying_rights_retained_no_blanket_grant",
                "qa_status": "producer_source_matched",
            }
        )
    write_csv(
        source_stage / "controls" / "FIGURE_MANIFEST.csv",
        [
            "relative_path",
            "bytes",
            "sha256",
            "source_pdf_sha256",
            "source_local_page",
            "width_px",
            "height_px",
            "image_mode",
            "role",
            "rights_status",
            "qa_status",
        ],
        figure_rows,
    )

    write_text(
        source_stage / "PROVENANCE_AND_SCOPE.md",
        f"""
        # Provenance and scope

        This package is the bounded SGA 3 Expose VI A English working
        checkpoint through the VI A bibliography. It covers Polo-Gille
        Expose VI A local pages 1-38, corresponding to combined-reader pages
        304-341. Expose VI B and all later exposes are excluded.

        The sole controlling French prose, formula, page, note, and diagram
        witness is `Exp6A-13oct24.pdf`, 38 pages, {AUTHORITY_BYTES:,} bytes,
        SHA-256 `{AUTHORITY_SHA256}`. The authority PDF is not redistributed
        here. OCR was locator and drafting witness only.

        Jacob C. Reinhold's English Markdown in `jcreinhold/sga` at commit
        `e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison and
        drafting lineage. Reinhold describes that contribution as LLM
        generated and licenses his translation contribution CC BY 4.0. It is
        neither authority nor independent corroboration.

        The 26 editable components are pinned in
        `controls/COMPONENT_MANIFEST.csv`. The 23 required Loop-1 diagram
        images are pinned and page-mapped in `controls/FIGURE_MANIFEST.csv`.
        """,
    )
    write_text(
        source_stage / "RIGHTS_AND_ATTRIBUTION.md",
        """
        # Rights and attribution

        This working package asserts no blanket license over the underlying
        French work, the Polo-Gille re-edition, or the source-derived diagram
        pixels. Rights in those materials remain with their respective
        holders.

        Credit the Interlanguage project for this English reconstruction and
        its source-audit workflow. Machine-assisted contributions include
        Anthropic Claude and OpenAI Codex / ChatGPT.

        Jacob C. Reinhold's `jcreinhold/sga` snapshot
        `e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison and
        drafting lineage under his stated CC BY 4.0 terms for his translation
        contribution. Do not present it as source authority or as this
        project's work.
        """,
    )
    write_text(
        source_stage / "PUBLICATION_READINESS.md",
        """
        # Publication readiness

        Status: READY_FOR_BOUNDED_WORKING_PUBLICATION_WITH_CAVEATS.

        This is complete Expose VI A only. It is not complete SGA 3, a
        critical edition, rights clearance, human peer review, or exhaustive
        convention-v2 internal-reference certification. Expose VI B and later
        are not included.

        All 23 diagrams are required Loop-1 source-derived images. Native
        diagram reconstruction remains open Loop-2 work. The PDF is an
        untagged working reader and is not claimed to satisfy archival PDF
        accessibility requirements.
        """,
    )
    write_text(
        source_stage / "BUILD_SUMMARY.md",
        f"""
        # Build summary

        Two fresh isolated builds were run from the exact pinned source
        closure. Each used three XeLaTeX passes and returned exit code zero.
        The resulting PDFs were byte-identical at SHA-256
        `{sha256_path(build['pdf'])}`.

        Final diagnostics: `{json.dumps(build['diagnostics'], sort_keys=True)}`.
        PDF: {pdf_info['pages']} A4 pages, {pdf_info['named_destinations']}
        named destinations, {pdf_info['link_rectangles']} link rectangles,
        {pdf_info['unique_image_objects']} unique image objects, and
        {pdf_info['unique_font_resources']} unique page font resources.
        Link actions: `{json.dumps(pdf_info['link_actions'], sort_keys=True)}`.

        `pdffonts` reports {font_info['rows']}/{font_info['rows']} font rows
        embedded, subset, and Unicode mapped. There are no attachments, forms,
        JavaScript, additional actions, or external URI links.

        Canonical `pdftotext -layout` extraction is {text_info['bytes']:,}
        bytes at SHA-256 `{text_info['sha256']}`, with
        {text_info['replacement_characters']} replacement characters,
        {text_info['nul_characters']} NUL bytes, and no forbidden controls.
        PyPDF independently parsed every page and link; its math-font extraction
        reports {pdf_info['pypdf_nul_count']} NUL placeholders on
        {len(pdf_info['pypdf_nul_pages'])} pages, which is retained as a
        parser-specific observation rather than used as the canonical text
        extraction.

        All pages were rendered at 120 dpi into temporary local QA files for
        archive-maintainer inspection. Those routine page renders are not
        duplicated in the public package.
        """,
    )
    write_text(
        source_stage / "README.md",
        """
        # SGA 3 Expose VI A English working checkpoint

        Build the reader by running XeLaTeX three times on
        `SGA3_English_Expose_VIA_Loop1_Working_20260723.tex` from this
        directory.

        The 26 component files are under `tex/components`; all 23 required
        Loop-1 diagram assets are under `figures`. Provenance, rights,
        readiness, build, machine manifests, and independent closing-range QA
        are included.
        """,
    )

    validation_path = source_stage / "SOURCE_EVIDENCE_VALIDATION.json"
    privacy_hits = scan_privacy(source_stage)
    validation = {
        "status": "PASS" if not privacy_hits else "FAIL",
        "errors": [] if not privacy_hits else ["privacy_hits"],
        "scope": "SGA3 Expose VI A through bibliography",
        "source_root_mutated": False,
        "component_files": len(COMPONENTS),
        "figure_files": len(FIGURES),
        "input_pin_digest": pins["pin_digest"],
        "authority_pdf_redistributed": False,
        "authority_pdf_sha256": AUTHORITY_SHA256,
        "independent_closing_audit_sha256": INDEPENDENT_AUDIT_SHA256,
        "reader_sha256": sha256_path(build["pdf"]),
        "reader_pages": pdf_info["pages"],
        "reader_named_destinations": pdf_info["named_destinations"],
        "reader_link_rectangles": pdf_info["link_rectangles"],
        "reader_link_actions": pdf_info["link_actions"],
        "reader_image_objects": pdf_info["unique_image_objects"],
        "canonical_text_extraction": text_info,
        "pypdf_nul_count": pdf_info["pypdf_nul_count"],
        "pypdf_nul_pages": pdf_info["pypdf_nul_pages"],
        "fonts": font_info,
        "privacy_hits": privacy_hits,
        "rights_clearance_claimed": False,
        "whole_sga3_completion_claimed": False,
        "exhaustive_reference_certification_claimed": False,
        "native_diagram_completion_claimed": False,
    }
    write_json(validation_path, validation)
    if validation["status"] != "PASS":
        raise RuntimeError(f"Source evidence validation failed: {validation}")

    manifest_path = source_stage / "SHA256SUMS.csv"
    manifest_rows = []
    for path in collect_files(source_stage, {"SHA256SUMS.csv"}):
        manifest_rows.append(
            {
                "relative_path": path.relative_to(source_stage).as_posix(),
                **identity(path),
            }
        )
    write_csv(
        manifest_path,
        ["relative_path", "bytes", "sha256"],
        manifest_rows,
    )
    return {
        "files": len(manifest_rows) + 1,
        "bytes": sum(path.stat().st_size for path in collect_files(source_stage)),
        "manifest_rows": len(manifest_rows),
        "manifest": identity(manifest_path),
        "aggregate": aggregate_identity(source_stage, collect_files(source_stage)),
        "privacy_hits": privacy_hits,
    }


def make_deterministic_zip(source: Path, destination: Path) -> dict[str, Any]:
    fixed_time = (2026, 7, 23, 0, 0, 0)
    files = collect_files(source)
    with zipfile.ZipFile(
        destination,
        "x",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
        strict_timestamps=True,
    ) as archive:
        for path in files:
            relative = path.relative_to(source).as_posix()
            info = zipfile.ZipInfo(relative, fixed_time)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())

    errors = []
    member_rows = []
    with zipfile.ZipFile(destination, "r") as archive:
        bad = archive.testzip()
        if bad:
            errors.append(f"crc_failure:{bad}")
        names = archive.namelist()
        if len(names) != len(files):
            errors.append("member_count")
        for name in names:
            pure = PurePosixPath(name)
            if pure.is_absolute() or ".." in pure.parts or "\\" in name:
                errors.append(f"unsafe_name:{name}")
            data = archive.read(name)
            source_path = source / Path(*pure.parts)
            if not source_path.is_file():
                errors.append(f"missing_source:{name}")
                continue
            if data != source_path.read_bytes():
                errors.append(f"member_mismatch:{name}")
            member_rows.append(
                {
                    "relative_path": name,
                    "bytes": len(data),
                    "sha256": hashlib.sha256(data).hexdigest().upper(),
                }
            )
    if errors:
        raise RuntimeError(f"ZIP validation failed: {errors}")
    return {
        **identity(destination),
        "members": len(member_rows),
        "uncompressed_bytes": sum(row["bytes"] for row in member_rows),
        "member_aggregate": hashlib.sha256(
            "".join(
                f"{row['relative_path']}\t{row['bytes']}\t{row['sha256']}\n"
                for row in member_rows
            ).encode("utf-8")
        ).hexdigest().upper(),
        "errors": errors,
    }


def build_outer_package(
    output_root: Path,
    source_stage: Path,
    build: dict[str, Any],
    source_controls: dict[str, Any],
    pdf_info: dict[str, Any],
    text_info: dict[str, Any],
    font_info: dict[str, Any],
    pins: dict[str, Any],
) -> dict[str, Any]:
    output_root.mkdir(parents=True)
    reader_target = output_root / PDF_NAME
    master_target = output_root / MASTER_NAME
    zip_target = output_root / ZIP_NAME
    shutil.copy2(build["pdf"], reader_target)
    shutil.copy2(source_stage / MASTER_NAME, master_target)
    zip_info = make_deterministic_zip(source_stage, zip_target)

    write_text(
        output_root / "README.md",
        f"""
        # SGA 3 English Expose VI A - Loop-1 working release

        This compact package publishes complete Expose VI A through its
        bibliography as a bounded English working reader.

        - Reader: {pdf_info['pages']} A4 pages.
        - Editable source: 26 pinned components plus this direct master.
        - Diagrams: 23 required source-derived Loop-1 assets in the source and
          evidence ZIP.
        - Scope ends after the Expose VI A bibliography.
        - Expose VI B and all later exposes are excluded.

        The reader is not complete SGA 3, a critical edition, rights clearance,
        exhaustive convention-v2 reference certification, or native-diagram
        Loop-2 completion. Rights in the underlying French work, Polo-Gille
        re-edition, and diagram pixels remain with their holders.

        Jacob C. Reinhold's `jcreinhold/sga` commit
        `e7a259f3f8608ad3edf9bf6eead3fd504dd2d23e` is credited comparison and
        drafting lineage under his stated CC BY 4.0 terms for his translation
        contribution, not authority.
        """,
    )
    package_validation = {
        "status": "PASS",
        "errors": [],
        "scope": "SGA3 Expose VI A through bibliography",
        "package_shape": "direct_reader_direct_master_grouped_source_evidence_zip",
        "reader": {**identity(reader_target), **pdf_info},
        "canonical_text_extraction": text_info,
        "master_tex": identity(master_target),
        "source_evidence_zip": zip_info,
        "source_evidence": source_controls,
        "input_pin_digest": pins["pin_digest"],
        "independent_build_byte_identical": True,
        "fonts": font_info,
        "visual_qa": {
            "status": "PASS_ARCHIVE_MAINTAINER_APPROVED",
            "routine_page_renders_published": False,
        },
        "rights_clearance_claimed": False,
        "whole_sga3_completion_claimed": False,
        "expose_vib_included": False,
        "native_diagram_completion_claimed": False,
        "exhaustive_reference_certification_claimed": False,
    }
    write_json(output_root / "PACKAGE_VALIDATION.json", package_validation)

    manifest_rows = []
    for path in collect_files(output_root, {"SHA256SUMS.csv"}):
        manifest_rows.append(
            {
                "relative_path": path.relative_to(output_root).as_posix(),
                **identity(path),
            }
        )
    write_csv(
        output_root / "SHA256SUMS.csv",
        ["relative_path", "bytes", "sha256"],
        manifest_rows,
    )

    privacy_hits = scan_privacy(output_root)
    if privacy_hits:
        raise RuntimeError(f"Outer package privacy scan failed: {privacy_hits}")
    package_files = collect_files(output_root)
    if len(package_files) != 6:
        raise RuntimeError(f"Expected six outer files, found {len(package_files)}.")
    return {
        "files": len(package_files),
        "bytes": sum(path.stat().st_size for path in package_files),
        "aggregate": aggregate_identity(output_root, package_files),
        "reader": identity(reader_target),
        "master_tex": identity(master_target),
        "zip": zip_info,
        "outer_manifest": identity(output_root / "SHA256SUMS.csv"),
        "validation": identity(output_root / "PACKAGE_VALIDATION.json"),
        "privacy_hits": privacy_hits,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--authority-pdf", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--mode", choices=("qa", "release"), required=True)
    parser.add_argument("--expected-pdf-sha256")
    parser.add_argument(
        "--visual-qa-approved",
        action="store_true",
        help="Required for release mode after the QA contacts were inspected.",
    )
    parser.add_argument(
        "--xelatex",
        type=Path,
        default=Path(
            r"C:\Users\Floris\AppData\Local\Programs\MiKTeX"
            r"\miktex\bin\x64\xelatex.exe"
        ),
    )
    parser.add_argument(
        "--pdffonts",
        type=Path,
        default=Path(
            r"C:\Users\Floris\AppData\Local\Programs\MiKTeX"
            r"\miktex\bin\x64\pdffonts.exe"
        ),
    )
    parser.add_argument(
        "--pdftoppm",
        type=Path,
        default=Path(
            r"C:\Users\Floris\AppData\Local\Programs\MiKTeX"
            r"\miktex\bin\x64\pdftoppm.exe"
        ),
    )
    parser.add_argument(
        "--pdftotext",
        type=Path,
        default=Path(
            r"C:\Users\Floris\AppData\Local\Programs\MiKTeX"
            r"\miktex\bin\x64\pdftotext.exe"
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_root = args.source_root.resolve(strict=True)
    authority_pdf = args.authority_pdf.resolve(strict=True)
    output_root = args.output_root.resolve()
    if output_root.exists():
        raise RuntimeError(f"Output root already exists: {output_root}")
    if args.mode == "release" and not args.visual_qa_approved:
        raise RuntimeError("Release mode requires --visual-qa-approved.")
    for executable in (
        args.xelatex,
        args.pdffonts,
        args.pdftoppm,
        args.pdftotext,
    ):
        if not executable.is_file():
            raise RuntimeError(f"Required executable not found: {executable}")

    pins = validate_source_inputs(source_root, authority_pdf)
    temporary_root = Path(tempfile.mkdtemp(prefix="sga3-via-release-"))
    try:
        build_source = temporary_root / "build_source"
        prepare_build_source(source_root, build_source, pins)
        first = run_xelatex_build(
            build_source,
            temporary_root / "build_one",
            args.xelatex,
        )
        second = run_xelatex_build(
            build_source,
            temporary_root / "build_two",
            args.xelatex,
        )
        first_identity = identity(first["pdf"])
        second_identity = identity(second["pdf"])
        if first_identity != second_identity:
            raise RuntimeError(
                "Independent builds are not byte-identical: "
                f"{first_identity} != {second_identity}"
            )
        if (
            args.expected_pdf_sha256
            and first_identity["sha256"] != args.expected_pdf_sha256.upper()
        ):
            raise RuntimeError(
                f"Reader SHA differs from approved QA build: {first_identity['sha256']}"
            )

        pdf_info = inspect_pdf(first["pdf"])
        text_info = inspect_text_extraction(first["pdf"], args.pdftotext)
        font_info = inspect_fonts(first["pdf"], args.pdffonts)
        if pdf_info["unique_image_objects"] != len(FIGURES):
            raise RuntimeError(
                f"Expected {len(FIGURES)} PDF image objects, "
                f"found {pdf_info['unique_image_objects']}."
            )

        # Re-pin the producer files after both builds to exclude a source race.
        after = validate_source_inputs(source_root, authority_pdf)
        if after["pin_digest"] != pins["pin_digest"]:
            raise RuntimeError("Producer inputs changed during the archive build.")

        if args.mode == "qa":
            output_root.mkdir(parents=True)
            shutil.copy2(first["pdf"], output_root / PDF_NAME)
            render_info = render_pdf(
                first["pdf"],
                output_root,
                args.pdftoppm,
                pdf_info["pages"],
            )
            result = {
                "status": "PASS_PENDING_MANUAL_VISUAL_QA",
                "errors": [],
                "pdf": first_identity,
                "pdf_info": pdf_info,
                "canonical_text_extraction": text_info,
                "fonts": font_info,
                "render": render_info,
                "input_pin_digest": pins["pin_digest"],
                "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            }
            write_json(output_root / "QA_RESULT.json", result)
        else:
            source_stage = temporary_root / "source_evidence"
            shutil.copytree(build_source, source_stage)
            source_controls = write_source_controls(
                source_stage,
                source_root,
                pins,
                first,
                pdf_info,
                text_info,
                font_info,
            )
            result = {
                "status": "PASS_ARCHIVE_RELEASE_READY",
                "errors": [],
                **build_outer_package(
                    output_root,
                    source_stage,
                    first,
                    source_controls,
                    pdf_info,
                    text_info,
                    font_info,
                    pins,
                ),
            }
            write_json(output_root / "ARCHIVE_BUILD_RECEIPT.json", result)
            # The receipt is outside the proposed six-file public package and is
            # intentionally removed after its values have been printed.
            receipt = output_root / "ARCHIVE_BUILD_RECEIPT.json"
            printed = receipt.read_text(encoding="utf-8")
            receipt.unlink()
            print(printed)
            return 0

        print(json.dumps(result, ensure_ascii=True, indent=2))
        return 0
    finally:
        shutil.rmtree(temporary_root, ignore_errors=True)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
