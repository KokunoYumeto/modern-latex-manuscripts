#!/usr/bin/env python3
"""Bind the completed human review of all D027 EN/FR math-alignment deltas."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


PAGE_NOTES = {
    4: "French removes a repeated inline s after identifying both commuting Jordan factors; the preceding s and u assignments are intact.",
    5: "French verbalizes the implication by 'impliquent'; all three Borel-pair conditions and O(w) are intact.",
    9: "French combines adjacent inline g and G tokens as g\\in G; the mathematical assertion is unchanged.",
    11: "Display differs only in the translated set-description text; G^F, F-stability, maximal tori, the isomorphism arrow, and W_F are intact.",
    34: "French writes 'Frobenius acts' instead of repeating an isolated inline F; all fixed-point formulas are intact.",
    41: "The two displays differ only in translated text describing F-stable maximal tori; every non-text mathematical token is retained.",
    46: "French elides a repeated subject T and repositions P/U_P with French syntax; Theorem 8.3 and both induction displays are intact.",
    51: "T'^{F} and T'^F are TeX-equivalent notations for the same exponent.",
    53: "The cases display translates only its prose conditions; nu(g), the regular/semisimple conditions, Z-factors, q-power, and zero branch are intact.",
    54: "French verbalizes the direct product indexed by simple roots instead of isolating the product as inline math; every U_alpha factor and the later indexed product formulas are retained.",
    57: "French removes only redundant parentheses around T' subset S^*; the mathematical relation is unchanged.",
}

DEFAULT_NOTE = (
    "Paired page review confirms a French word-order, punctuation, math-span boundary, "
    "or repeated-symbol relocation only; no mathematical object, relation, hypothesis, "
    "formula, tag, or diagram is lost."
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    with args.input.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fields = list(reader.fieldnames or [])
        rows = list(reader)

    if len(rows) != 48:
        raise ValueError(f"expected 48 alignment findings, found {len(rows)}")
    expected_pages = {2, 3, 4, 5, 9, 10, 11, 12, 13, 15, 16, 17, 30, 34, 41, 45, 46, 51, 53, 54, 57, 59}
    actual_pages = {int(row["physical_page"]) for row in rows}
    if actual_pages != expected_pages:
        raise ValueError(f"unexpected review page set: {sorted(actual_pages)}")

    for row in rows:
        page = int(row["physical_page"])
        row["review_status"] = "ACCEPTED_EQUIVALENT_AFTER_PAIRED_PAGE_REVIEW"
        row["review_note"] = PAGE_NOTES.get(page, DEFAULT_NOTE)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"PASS\trows={len(rows)}\tpages={len(actual_pages)}")


if __name__ == "__main__":
    main()
