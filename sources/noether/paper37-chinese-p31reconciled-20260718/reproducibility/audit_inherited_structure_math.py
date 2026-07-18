#!/usr/bin/env python3
"""Inventory sealed-P31 structure and inherited Chinese Paper 37 math divergences."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/Noether_Paper37_German_P31_logical_article_LF.tex"
WITNESS = ROOT / "witness/Noether_Paper37_SimplifiedChinese_Inherited_logical_article_LF.tex"
JSON_OUT = ROOT / "qa/INHERITED_STRUCTURE_AND_MATH_AUDIT.json"
MD_OUT = ROOT / "qa/INHERITED_STRUCTURE_AND_MATH_AUDIT.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def line_of(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


MATH_RE = re.compile(r"\\\[(.*?)\\\]|\\\((.*?)\\\)", re.S)


def math_spans(text: str) -> list[dict]:
    out = []
    for i, match in enumerate(MATH_RE.finditer(text), 1):
        body = match.group(1) if match.group(1) is not None else match.group(2)
        out.append(
            {
                "index": i,
                "kind": "display" if match.group(1) is not None else "inline",
                "line": line_of(text, match.start()),
                "raw": body,
                "compact": re.sub(r"\s+", "", body),
            }
        )
    return out


def structure(text: str) -> dict:
    return {
        "section": len(re.findall(r"\\section\*\{", text)),
        "subsection": len(re.findall(r"\\subsection\*\{", text)),
        "paragraph": len(re.findall(r"\\paragraph\{", text)),
        "footnote": text.count(r"\footnote{"),
        "emph": text.count(r"\emph{"),
        "center_environments": text.count(r"\begin{center}"),
        "display_math": len(re.findall(r"\\\[", text)),
        "inline_math": len(re.findall(r"\\\(", text)),
        "begin_environment_counts": dict(Counter(re.findall(r"\\begin\{([^}]+)\}", text))),
        "end_environment_counts": dict(Counter(re.findall(r"\\end\{([^}]+)\}", text))),
    }


source_text = SOURCE.read_text(encoding="utf-8")
witness_text = WITNESS.read_text(encoding="utf-8")
source_math = math_spans(source_text)
witness_math = math_spans(witness_text)

paired = []
for i in range(max(len(source_math), len(witness_math))):
    s = source_math[i] if i < len(source_math) else None
    w = witness_math[i] if i < len(witness_math) else None
    paired.append(
        {
            "index": i + 1,
            "source": s,
            "witness": w,
            "compact_equal": bool(s and w and s["compact"] == w["compact"]),
        }
    )

source_structure = structure(source_text)
witness_structure = structure(witness_text)
known_adverse = [
    {
        "id": "P37-W-AUTHOR-OMISSION",
        "class": "source_hierarchy_omission",
        "source_fact": r"Von \emph{Emmy Noether} in Göttingen.",
        "witness_state": "The author center line is absent.",
        "consequence": "Restore the source author hierarchy in the target.",
    },
    {
        "id": "P37-W-DEURING-PRODUCTS",
        "class": "mathematical_operator_error",
        "source_fact": r"The four conductor factors use multiplication \cdot and evaluate to 4,2,2,4.",
        "witness_state": "The inherited display uses division slashes while retaining 4,2,2,4.",
        "consequence": "Replace all four divisions with source multiplication and preserve the inherited form as adverse evidence.",
    },
    {
        "id": "P37-W-ORDER-CASE",
        "class": "symbol_case_error",
        "source_fact": r"§1 begins with \frako respectively \frako_\frakp, both lower-case orders.",
        "witness_state": r"The inherited first symbol is \frakO, the capital order of K used elsewhere.",
        "consequence": r"Restore \frako.",
    },
    {
        "id": "P37-W-BASIS-INDEX",
        "class": "symbol_index_error",
        "source_fact": r"v_1,\ldots,v_t is the basis of the Galois module.",
        "witness_state": r"The inherited text has v_1,\ldots,v_l.",
        "consequence": "Restore the source index t.",
    },
    {
        "id": "P37-W-COEFFICIENT-FIELD",
        "class": "symbol_object_error",
        "source_fact": r"The coefficient extension in the long footnote is (K_\frakp)_P and Pe^{S_i}.",
        "witness_state": r"Two inherited occurrences change subscript P to \mathfrak P while retaining Pe^{S_i} later.",
        "consequence": "Restore the ordinary capital P consistently.",
    },
    {
        "id": "P37-W-GROUP-SUM-EXPANSION",
        "class": "editorial_formula_expansion",
        "source_fact": r"E^{(1)}=\frac1n\sum S is intentionally unindexed in both source occurrences.",
        "witness_state": r"The first occurrence is expanded to \sum_{S\in\Gg} S while the next remains \sum S.",
        "consequence": "Use the exact source form unless an explicit editorial gloss is separately recorded.",
    },
]

errors = []
if len(source_math) != len(witness_math):
    errors.append(f"ordered math span count differs: source={len(source_math)}, witness={len(witness_math)}")
if source_structure["footnote"] != witness_structure["footnote"]:
    errors.append(
        f"footnote count differs: source={source_structure['footnote']}, witness={witness_structure['footnote']}"
    )
if source_structure["emph"] != witness_structure["emph"]:
    errors.append(f"emphasis count differs: source={source_structure['emph']}, witness={witness_structure['emph']}")

report = {
    "schema_version": "1.0.0",
    "work_id": "NOETHER-P37",
    "authority": {"path": str(SOURCE), "sha256": sha(SOURCE)},
    "inherited_witness": {"path": str(WITNESS), "sha256": sha(WITNESS)},
    "source_structure": source_structure,
    "witness_structure": witness_structure,
    "math_span_counts": {"source": len(source_math), "witness": len(witness_math)},
    "math_pairs": paired,
    "compact_unequal_indices": [x["index"] for x in paired if not x["compact_equal"]],
    "known_adverse_findings": known_adverse,
    "errors": errors,
    "status": "adverse_witness_inventory_complete",
    "validation_scope": "Internal structural computation and editorial identification only; not external or human validation.",
}
JSON_OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

rows = []
for item in paired:
    if item["compact_equal"]:
        continue
    s = item["source"] or {}
    w = item["witness"] or {}
    sraw = (s.get("raw") or "").replace("\n", " ").replace("|", r"\|")
    wraw = (w.get("raw") or "").replace("\n", " ").replace("|", r"\|")
    rows.append(
        f"| {item['index']} | {s.get('line', '')} | {w.get('line', '')} | `{sraw}` | `{wraw}` |"
    )

md = [
    "# Paper 37 inherited structure and mathematics audit",
    "",
    f"- Sealed logical source: `{SOURCE}`, SHA-256 `{sha(SOURCE)}`.",
    f"- Inherited logical witness: `{WITNESS}`, SHA-256 `{sha(WITNESS)}`.",
    f"- Ordered math spans: source `{len(source_math)}`, witness `{len(witness_math)}`.",
    f"- Source/witness footnotes: `{source_structure['footnote']}` / `{witness_structure['footnote']}`; source/witness emphasis scopes: `{source_structure['emph']}` / `{witness_structure['emph']}`.",
    "- This is an adverse-witness audit. Unequal strings require adjudication; equal counts do not establish semantic correctness.",
    "",
    "## Known adverse findings",
    "",
]
for finding in known_adverse:
    md.append(
        f"- `{finding['id']}` ({finding['class']}): {finding['witness_state']} {finding['consequence']}"
    )
md.extend(
    [
        "",
        "## Ordered compact-math differences",
        "",
        "| span | source line | witness line | sealed source | inherited witness |",
        "|---:|---:|---:|---|---|",
        *rows,
        "",
        "No external, native-review, or source-owner validation is claimed.",
        "",
    ]
)
MD_OUT.write_text("\n".join(md), encoding="utf-8")
print(json.dumps({"json": str(JSON_OUT), "markdown": str(MD_OUT), "unequal": report["compact_unequal_indices"], "errors": errors}, ensure_ascii=False, indent=2))
