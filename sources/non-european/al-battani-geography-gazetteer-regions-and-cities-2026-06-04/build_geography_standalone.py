#!/usr/bin/env python3
"""Build the local al-Battani geography gazetteer PDF and CSV.

This is a standalone variant of the push-queue build script. It reads the
`geo_cat_raw.tsv` file in this folder rather than Claude's scratch `grind/`
directory.
"""

from __future__ import annotations

import csv
import os
import subprocess


HERE = os.path.dirname(os.path.abspath(__file__))
TSV = os.path.join(HERE, "geo_cat_raw.tsv")


def esc(value: str) -> str:
    return (
        (value or "")
        .replace("&", r"\&")
        .replace("%", r"\%")
        .replace("_", r"\_")
        .replace("#", r"\#")
        .replace("[", r"{[}")
        .replace("]", r"{]}")
    )


def coord(degrees: str, minutes: str) -> str:
    degrees = (degrees or "").strip()
    minutes = (minutes or "").strip()
    if degrees in ("", "?") or minutes == "?":
        return r"\textcolor{gray}{--}"
    return f"{degrees}$^\\circ$\\,{minutes or '0'}$'$"


def load_rows():
    regions = []
    cities = []
    with open(TSV, encoding="utf-8", newline="") as handle:
        for row in csv.reader(handle, delimiter="\t"):
            if not row or row[0].startswith("#"):
                continue
            record = {
                "n": row[1],
                "name": row[2],
                "lod": row[3],
                "lom": row[4],
                "lad": row[5],
                "lam": row[6],
            }
            (regions if row[0] == "region" else cities).append(record)
    return regions, cities


PREAMBLE = r"""\documentclass[10pt,a4paper]{article}
\usepackage{fontspec}
\usepackage[margin=1.5cm]{geometry}
\usepackage{xcolor}
\usepackage{longtable,booktabs,array,textcomp}
\setmainfont{Cambria}[Ligatures=TeX]
\setlength{\tabcolsep}{5pt}
\renewcommand{\arraystretch}{1.18}
\begin{document}
\begin{center}
{\LARGE\bfseries al-Battani -- Geographical Gazetteer}\\[3pt]
{\large Regions and cities, with ecliptic-frame coordinates}
\end{center}
\small\noindent\textbf{Source.} al-Battani's coordinates as established in C.~A.~Nallino's critical edition
(\textit{Opus Astronomicum}, Pars~II, 1907): the table of \emph{regional mid-points}
(\textit{Tabula mediorum punctorum regionum}, after Ptolemy's \textit{Geography}) and the table of
\emph{city} longitudes/latitudes (\textit{Tabula latitudinum et longitudinum urbium}). Longitude is
reckoned from the Fortunate Isles; latitudes are northern unless noted. \textcolor{gray}{--} marks a
cell still to be collated.\\[6pt]
"""


def table(title: str, subtitle: str, rows) -> str:
    output = [
        rf"\noindent{{\large\bfseries {title}}}\quad{{\small\textit{{{subtitle}}}}}\\[2pt]",
        r"\begin{longtable}{r >{\raggedright\arraybackslash}p{8.5cm} c c}",
        r"\toprule \# & Name / identification & Long. & Lat.\\ \midrule\endhead",
    ]
    for row in rows:
        output.append(
            f"{row['n']} & {esc(row['name'])} & {coord(row['lod'], row['lom'])} & {coord(row['lad'], row['lam'])}\\\\"
        )
    output.append(r"\bottomrule\end{longtable}\vspace{4pt}")
    return "\n".join(output)


def main() -> int:
    regions, cities = load_rows()
    body = [PREAMBLE]
    body.append(
        table(
            "I. Regions (94 in the source; 93 transcribed)",
            "Tabula mediorum punctorum regionum",
            regions,
        )
    )
    body.append(
        table(
            f"II. Cities ({len(cities)} of about 340; transcription in progress)",
            "Tabula latitudinum et longitudinum urbium",
            cities,
        )
    )
    body.append(r"\end{document}")

    tex_path = os.path.join(HERE, "al_battani_geography_gazetteer.tex")
    with open(tex_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("\n".join(body))

    with open(os.path.join(HERE, "albattani_geography.csv"), "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["type", "n", "name", "lon_d", "lon_m", "lat_d", "lat_m"])
        for row_type, rows in (("region", regions), ("city", cities)):
            for row in rows:
                writer.writerow([row_type, row["n"], row["name"], row["lod"], row["lom"], row["lad"], row["lam"]])

    subprocess.run(
        ["xelatex", "-interaction=nonstopmode", "-halt-on-error", os.path.basename(tex_path)],
        cwd=HERE,
        check=True,
    )
    print(f"Built {len(regions)} regions and {len(cities)} city rows.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
