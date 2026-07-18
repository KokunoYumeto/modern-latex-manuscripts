#!/usr/bin/env python3
"""Wrap the exact sealed-P31 Paper 37 logical article as a German control."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/Noether_Paper37_German_P31_logical_article_LF.tex"
OUTPUT = ROOT / "source_control/Noether_Paper37_German_P31_Standalone.tex"

EXPECTED_BODY_SHA256 = (
    "68C72173E0C060BC68CB3651AF078ACE82B4D5806C8A41584632AA2BB4A9B27B"
)

PREAMBLE = rb"""% Standalone control for the sealed P31 Paper 37 logical article.
% Cumulative authority SHA-256:
% A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F.
% Logical article LF SHA-256:
% 68C72173E0C060BC68CB3651AF078ACE82B4D5806C8A41584632AA2BB4A9B27B.
\documentclass[11pt]{article}
\usepackage{fontspec}
\setmainfont[Ligatures=TeX]{Latin Modern Roman}
\usepackage[ngerman]{babel}
\usepackage{amsmath,amssymb}
\usepackage[a4paper,margin=2.35cm]{geometry}
\setlength{\emergencystretch}{3em}
\providecommand{\frakO}{\mathfrak O}
\providecommand{\frako}{\mathfrak o}
\providecommand{\frakp}{\mathfrak p}
\providecommand{\Gg}{\mathfrak G}
\begin{document}
"""

POSTAMBLE = b"\\end{document}\n"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def main() -> None:
    body = SOURCE.read_bytes()
    actual_body_sha256 = sha256(body)
    if actual_body_sha256 != EXPECTED_BODY_SHA256:
        raise SystemExit(
            "Refusing to build: logical-article hash mismatch "
            f"({actual_body_sha256} != {EXPECTED_BODY_SHA256})."
        )
    if b"\r" in body:
        raise SystemExit("Refusing to build: sealed LF body contains a CR byte.")

    separator = b"" if body.endswith(b"\n") else b"\n"
    standalone = PREAMBLE + body + separator + POSTAMBLE
    body_start = len(PREAMBLE)
    body_end = body_start + len(body)
    if standalone[body_start:body_end] != body:
        raise SystemExit("Internal error: standalone wrapper changed the sealed body bytes.")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(standalone)

    print(f"output={OUTPUT}")
    print(f"body_bytes={len(body)}")
    print(f"body_sha256={actual_body_sha256}")
    print(f"body_offset=[{body_start},{body_end})")
    print(f"standalone_sha256={sha256(standalone)}")


if __name__ == "__main__":
    main()
