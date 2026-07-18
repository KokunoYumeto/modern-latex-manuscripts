#!/usr/bin/env python3
"""Semantic source-parity gate for the bounded Paper 37 zh-Hans tranche.

This gate deliberately does not compare the ordered stream of inline mathematics.
It checks the article's source topology, the 15 displayed formulae by named semantic
signatures, and the source-sensitive repairs recorded for this reconciliation.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TRANCHE = Path(__file__).resolve().parents[1]
SOURCE = TRANCHE / "source" / "Noether_Paper37_German_P31_logical_article_LF.tex"
SOURCE_EXACT = (
    TRANCHE / "source" / "Noether_Paper37_German_P31_logical_article_exact_CRLF.tex"
)
TARGET = (
    TRANCHE
    / "zh-Hans-CN"
    / "Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.tex"
)
OUTPUT = TRANCHE / "qa" / "P37_SOURCE_PARITY.json"

SEALED_P31_AUTHORITY_SHA256 = (
    "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F"
)
EXPECTED_SOURCE_LF_SHA256 = (
    "68C72173E0C060BC68CB3651AF078ACE82B4D5806C8A41584632AA2BB4A9B27B"
)
EXPECTED_SOURCE_EXACT_SHA256 = (
    "AF3B34ACF4FF8D91850AC56C4F86447ABC61E6641FF9795BEFBFDA004788585D"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def read_tex(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")


def target_article(text: str) -> str:
    start = text.find(r"\section*{37.")
    end = text.find(r"\end{document}", start)
    if start < 0 or end < 0:
        raise ValueError("Could not isolate the Paper 37 article in the target TeX")
    return text[start:end]


def braced_arguments(text: str, command: str) -> list[str]:
    """Return brace-balanced arguments immediately following ``command``."""
    needle = command + "{"
    values: list[str] = []
    cursor = 0
    while True:
        start = text.find(needle, cursor)
        if start < 0:
            return values
        index = start + len(needle)
        depth = 1
        while index < len(text) and depth:
            if text[index] == "{" and (index == 0 or text[index - 1] != "\\"):
                depth += 1
            elif text[index] == "}" and (index == 0 or text[index - 1] != "\\"):
                depth -= 1
            index += 1
        if depth:
            raise ValueError(f"Unbalanced argument for {command!r} at offset {start}")
        values.append(text[start + len(needle) : index - 1])
        cursor = index


def compact(text: str) -> str:
    return re.sub(r"\s+", "", text)


def canonical_tex(text: str) -> str:
    """Canonicalize harmless aliases and language-only boxes, not semantic case/indexes."""
    value = text.replace(r"\srcemph", r"\emph")
    value = re.sub(r"\\mathfrak\s*\{?C\}?", r"\\mathfrak{C}", value)
    value = value.replace(r"\frakC", r"\mathfrak{C}")
    value = re.sub(r"\\mathfrak\s*\{?P\}?", r"\\mathfrak{P}", value)
    value = value.replace(r"\frakP", r"\mathfrak{P}")
    value = re.sub(r"\\hbox\{[^{}]*\}", r"\\hbox{LANG}", value)
    return compact(value)


def display_matches(text: str) -> list[re.Match[str]]:
    return list(re.finditer(r"\\\[(.*?)\\\]", text, flags=re.DOTALL))


def paragraph_topology(label: str) -> str:
    plain = compact(label)
    match = re.search(r"(?:Satz|定理)([1-7])", plain)
    if match:
        if "Zusätzliche" in label or "补充" in label:
            return "supplement_theorem_3"
        return f"theorem_{match.group(1)}"
    if "Definition" in label or "定义" in label:
        return "definition"
    return "unresolved:" + plain


def subsection_topology(label: str) -> str:
    match = re.search(r"§\s*([1-3])", label)
    return f"section_{match.group(1)}" if match else "unresolved:" + compact(label)


def check_record(
    checks: list[dict[str, Any]],
    check_id: str,
    passed: bool,
    observed: Any,
    expected: Any,
    evidence_class: str = "computation",
) -> None:
    checks.append(
        {
            "id": check_id,
            "pass": bool(passed),
            "observed": observed,
            "expected": expected,
            "evidence_class": evidence_class,
        }
    )


def main() -> int:
    source = read_tex(SOURCE)
    target_full = read_tex(TARGET)
    target = target_article(target_full)
    source_displays = display_matches(source)
    target_displays = display_matches(target)
    checks: list[dict[str, Any]] = []

    hashes = {
        "sealed_p31_canonical_german_authority_declared_sha256": SEALED_P31_AUTHORITY_SHA256,
        "source_logical_lf": {
            "path": str(SOURCE),
            "sha256": sha256(SOURCE),
            "expected_sha256": EXPECTED_SOURCE_LF_SHA256,
        },
        "source_logical_exact_crlf": {
            "path": str(SOURCE_EXACT),
            "sha256": sha256(SOURCE_EXACT),
            "expected_sha256": EXPECTED_SOURCE_EXACT_SHA256,
        },
        "target": {"path": str(TARGET), "sha256": sha256(TARGET)},
        "checker": {"path": str(Path(__file__).resolve()), "sha256": sha256(Path(__file__))},
    }
    check_record(
        checks,
        "custody.source_lf_hash",
        hashes["source_logical_lf"]["sha256"] == EXPECTED_SOURCE_LF_SHA256,
        hashes["source_logical_lf"]["sha256"],
        EXPECTED_SOURCE_LF_SHA256,
        "source_fact+computation",
    )
    check_record(
        checks,
        "custody.source_exact_hash",
        hashes["source_logical_exact_crlf"]["sha256"] == EXPECTED_SOURCE_EXACT_SHA256,
        hashes["source_logical_exact_crlf"]["sha256"],
        EXPECTED_SOURCE_EXACT_SHA256,
        "source_fact+computation",
    )

    source_paragraphs = braced_arguments(source, r"\paragraph")
    target_paragraphs = braced_arguments(target, r"\paragraph")
    source_subsections = braced_arguments(source, r"\subsection*")
    target_subsections = braced_arguments(target, r"\subsection*")
    source_structure = {
        "section": source.count(r"\section*{"),
        "subsection": len(source_subsections),
        "paragraph_heading": len(source_paragraphs),
        "footnote": source.count(r"\footnote{"),
        "semantic_emphasis": source.count(r"\emph{"),
        "display": len(source_displays),
        "center": source.count(r"\begin{center}"),
    }
    target_structure = {
        "section": target.count(r"\section*{"),
        "subsection": len(target_subsections),
        "paragraph_heading": len(target_paragraphs),
        "footnote": target.count(r"\footnote{"),
        "semantic_emphasis": target.count(r"\emph{") + target.count(r"\srcemph{"),
        "display": len(target_displays),
        "center": target.count(r"\begin{center}"),
    }
    expected_structure = {
        "section": 1,
        "subsection": 3,
        "paragraph_heading": 9,
        "footnote": 12,
        "semantic_emphasis": 15,
        "display": 15,
        "center": 3,
    }
    for key, expected in expected_structure.items():
        check_record(
            checks,
            f"structure.{key}",
            source_structure[key] == target_structure[key] == expected,
            {"source": source_structure[key], "target": target_structure[key]},
            {"source": expected, "target": expected},
            "source_fact+computation",
        )

    source_paragraph_topology = [paragraph_topology(item) for item in source_paragraphs]
    target_paragraph_topology = [paragraph_topology(item) for item in target_paragraphs]
    expected_paragraph_topology = [
        "theorem_1",
        "theorem_2",
        "definition",
        "theorem_3",
        "theorem_4",
        "theorem_5",
        "supplement_theorem_3",
        "theorem_6",
        "theorem_7",
    ]
    check_record(
        checks,
        "topology.paragraph_headings",
        source_paragraph_topology == target_paragraph_topology == expected_paragraph_topology,
        {"source": source_paragraph_topology, "target": target_paragraph_topology},
        expected_paragraph_topology,
        "source_fact+editorial_inference+computation",
    )
    source_subsection_topology = [subsection_topology(item) for item in source_subsections]
    target_subsection_topology = [subsection_topology(item) for item in target_subsections]
    expected_subsection_topology = ["section_1", "section_2", "section_3"]
    check_record(
        checks,
        "topology.subsections",
        source_subsection_topology == target_subsection_topology == expected_subsection_topology,
        {"source": source_subsection_topology, "target": target_subsection_topology},
        expected_subsection_topology,
        "source_fact+editorial_inference+computation",
    )

    # Each display has a named algebraic signature. Language-only \hbox content and
    # harmless C/P fraktur aliases are canonicalized; indices and frako/frakO case are not.
    display_signatures: list[tuple[str, tuple[str, ...]]] = [
        ("group_ring_extension", (r"\mathfrak C=E^{(1)}", r"[\Gg]_{\frako_\frakp}", r"\frac1n\sum S")),
        ("galois_module_action", (r"z\Bigl(\sum_i S_i c_i\Bigr)", r"\sum_i z^{S_i}c_i")),
        ("operator_isomorphism", (r"S\longmapsto z^S", r"ST\longmapsto z^{ST}")),
        ("representation_matrix", (r"v_i^S", r"\bar S", r"v_i")),
        ("group_determinant", (r"D=\bigl|w^{ST^{-1}}\bigr|", r"S,T\in\Gg")),
        ("determinant_matrix_decomposition", (r"D=D_1^{f_1}\cdots D_t^{f_t}", r"M=f_1M_1+\cdots+f_tM_t")),
        ("lambda_matrix_transform", (r"M_\lambda=\sum_S w^S\bar S", r"M_\lambda^{T^{-1}}", r"M_\lambda\bar T")),
        ("lambda_determinant_transform", (r"D_\lambda^{T^{-1}}=D_\lambda|\bar T|", r"D_\lambda\varepsilon_T")),
        ("adjoint_determinant_pair", (r"D_\lambda^{T^{-1}}=D_\lambda\varepsilon_T", r"D_{\bar\lambda}^{T^{-1}}", r"\varepsilon_T^{-1}")),
        ("delta_invariance", (r"\Delta_\lambda^T=\Delta_\lambda", r"T", r"\Gg")),
        ("coefficient_direct_sum", (r"(K_\frakp)_P", r"e^{S_1}", r"e^{S_r}")),
        ("delta_factorization", (r"\Delta=\Delta_1^{f_1}\cdots\Delta_t^{f_t}",)),
        ("ramified_prime_factorization", (r"(p)=\frakp_1\cdots\frakp_{l-1}", r"\frakp_i=\mathfrak P_i^{\,l}")),
        ("root_number_factorization", (r"(\Omega_\lambda)=\mathfrak P_1^{r_1}\cdots\mathfrak P_{l-1}^{r_{l-1}}", r"(\Omega_{\bar\lambda})", r"\mathfrak P_1^{l-r_1}")),
        ("delta_ideal_chain", (r"(\Delta_\lambda)=(D_\lambda D_{\bar\lambda})", r"(\Omega_\lambda\Omega_{\bar\lambda})", r"=(p)")),
    ]
    display_results: list[dict[str, Any]] = []
    if len(source_displays) == len(target_displays) == len(display_signatures):
        for index, (signature_id, tokens) in enumerate(display_signatures):
            source_formula = canonical_tex(source_displays[index].group(1))
            target_formula = canonical_tex(target_displays[index].group(1))
            canonical_tokens = [canonical_tex(token) for token in tokens]
            missing_source = [token for token in canonical_tokens if token not in source_formula]
            missing_target = [token for token in canonical_tokens if token not in target_formula]
            display_results.append(
                {
                    "ordinal": index + 1,
                    "id": signature_id,
                    "pass": not missing_source and not missing_target,
                    "missing_source_tokens": missing_source,
                    "missing_target_tokens": missing_target,
                }
            )
    check_record(
        checks,
        "displays.semantic_signatures",
        len(display_results) == 15 and all(item["pass"] for item in display_results),
        display_results,
        "15 named source/target display signatures",
        "source_fact+editorial_inference+computation",
    )

    target_compact = compact(target)
    source_compact = compact(source)
    check_record(
        checks,
        "repair.author_line",
        target.count(r"作者：\emph{Emmy Noether}，哥廷根。") == 1,
        target.count(r"作者：\emph{Emmy Noether}，哥廷根。"),
        1,
        "source_fact+editorial_inference+computation",
    )
    check_record(
        checks,
        "repair.cross_reference_2a",
        "vgl.2a" in source_compact and "参见2a" in target_compact,
        {"source_vgl_2a": "vgl.2a" in source_compact, "target_参见_2a": "参见2a" in target_compact},
        {"source_vgl_2a": True, "target_参见_2a": True},
        "source_fact+editorial_inference+computation",
    )

    deuring_products = [
        r"2\sqrt[5]{2}\cdot\sqrt[5]{2^4}",
        r"\sqrt[5]{2^2}\cdot\sqrt[5]{2^3}",
        r"\sqrt[5]{2^3}\cdot\sqrt[5]{2^2}",
        r"\sqrt[5]{2^4}\cdot2\sqrt[5]{2}",
    ]
    product_counts = {item: target_compact.count(compact(item)) for item in deuring_products}
    corrupt_divisions = [
        r"2\sqrt[5]{2}/\sqrt[5]{2^4}",
        r"\sqrt[5]{2^2}/\sqrt[5]{2^3}",
        r"\sqrt[5]{2^3}/\sqrt[5]{2^2}",
        r"\sqrt[5]{2^4}/(2\sqrt[5]{2})",
    ]
    division_counts = {item: target_compact.count(compact(item)) for item in corrupt_divisions}
    check_record(
        checks,
        "repair.deuring_four_products",
        sum(product_counts.values()) == 4 and all(value == 1 for value in product_counts.values()),
        product_counts,
        "each of four source products occurs exactly once",
        "source_fact+computation",
    )
    check_record(
        checks,
        "repair.deuring_zero_corrupt_divisions",
        sum(division_counts.values()) == 0,
        division_counts,
        "all zero",
        "adverse_evidence+computation",
    )

    check_record(
        checks,
        "repair.lowercase_frako_opening",
        target_compact.count(compact(r"令 \(\frako\) 以及 \(\frako_\frakp\)")) == 1
        and target_compact.count(compact(r"令 \(\frakO\) 以及 \(\frako_\frakp\)")) == 0,
        {
            "lowercase_opening": target_compact.count(compact(r"令 \(\frako\) 以及 \(\frako_\frakp\)")),
            "corrupt_uppercase_opening": target_compact.count(compact(r"令 \(\frakO\) 以及 \(\frako_\frakp\)")),
        },
        {"lowercase_opening": 1, "corrupt_uppercase_opening": 0},
        "source_fact+adverse_evidence+computation",
    )
    check_record(
        checks,
        "repair.v_t_not_v_l",
        target_compact.count(compact(r"v_1,\ldots,v_t")) == 1
        and target_compact.count(compact(r"v_1,\ldots,v_l")) == 0,
        {
            "v_t": target_compact.count(compact(r"v_1,\ldots,v_t")),
            "v_l": target_compact.count(compact(r"v_1,\ldots,v_l")),
        },
        {"v_t": 1, "v_l": 0},
        "source_fact+adverse_evidence+computation",
    )

    kp_source_count = source_compact.count(compact(r"(K_\frakp)_P"))
    kp_target_count = target_compact.count(compact(r"(K_\frakp)_P"))
    kp_drift_patterns = [
        r"(K_\frakp)_\mathfrakP",
        r"(K_\frakp)_{\mathfrakP}",
        r"(K_\frakp)_\frakP",
        r"(K_\frakp)_{\frakP}",
    ]
    kp_drift_counts = {
        item: target_compact.count(compact(item)) for item in kp_drift_patterns
    }
    check_record(
        checks,
        "repair.Kp_subscript_P_source_occurrences",
        kp_source_count == kp_target_count == 4,
        {"source": kp_source_count, "target": kp_target_count},
        {"source": 4, "target": 4},
        "source_fact+computation",
    )
    check_record(
        checks,
        "repair.Kp_no_fraktur_P_drift",
        sum(kp_drift_counts.values()) == 0,
        kp_drift_counts,
        "all zero",
        "adverse_evidence+computation",
    )

    unindexed_sum = compact(r"E^{(1)}=\frac1n\sum S")
    indexed_sum_patterns = [
        compact(r"E^{(1)}=\frac1n\sum_{S\in\Gg}S"),
        compact(r"E^{(1)}=\frac1n\sum_{S\in G}S"),
    ]
    source_sum_count = source_compact.count(unindexed_sum)
    target_sum_count = target_compact.count(unindexed_sum)
    indexed_sum_counts = {item: target_compact.count(item) for item in indexed_sum_patterns}
    check_record(
        checks,
        "repair.unindexed_source_sum",
        source_sum_count == target_sum_count == 2 and sum(indexed_sum_counts.values()) == 0,
        {
            "unindexed_source": source_sum_count,
            "unindexed_target": target_sum_count,
            "indexed_target_drift": indexed_sum_counts,
        },
        {"unindexed_source": 2, "unindexed_target": 2, "indexed_target_drift_total": 0},
        "source_fact+adverse_evidence+computation",
    )

    generic_prime_observed: dict[str, Any]
    if len(source_displays) >= 14 and len(target_displays) >= 14:
        source_prime_prose = source[source_displays[12].end() : source_displays[13].start()]
        target_prime_prose = target[target_displays[12].end() : target_displays[13].start()]
        canonical_source_prime_prose = canonical_tex(source_prime_prose)
        canonical_target_prime_prose = canonical_tex(target_prime_prose)
        generic_prime_observed = {
            "source_generic_lowercase_p": canonical_source_prime_prose.count(compact(r"\(\frakp\)")),
            "source_generic_capital_P": canonical_source_prime_prose.count(canonical_tex(r"\(\mathfrak P\)")),
            "target_generic_lowercase_p": canonical_target_prime_prose.count(compact(r"\(\frakp\)")),
            "target_generic_capital_P": canonical_target_prime_prose.count(canonical_tex(r"\(\mathfrak P\)")),
            "target_indexed_lowercase_p_i": target_prime_prose.count(r"\(\frakp_i\)"),
            "target_indexed_capital_P_i": target_prime_prose.count(r"\(\frakP_i\)"),
        }
        generic_prime_pass = generic_prime_observed == {
            "source_generic_lowercase_p": 1,
            "source_generic_capital_P": 1,
            "target_generic_lowercase_p": 1,
            "target_generic_capital_P": 1,
            "target_indexed_lowercase_p_i": 0,
            "target_indexed_capital_P_i": 0,
        }
    else:
        generic_prime_observed = {"error": "display interval unavailable"}
        generic_prime_pass = False
    check_record(
        checks,
        "repair.generic_prime_notation_in_theorem_7_prose",
        generic_prime_pass,
        generic_prime_observed,
        {
            "source_generic_lowercase_p": 1,
            "source_generic_capital_P": 1,
            "target_generic_lowercase_p": 1,
            "target_generic_capital_P": 1,
            "target_indexed_lowercase_p_i": 0,
            "target_indexed_capital_P_i": 0,
        },
        "source_fact+adverse_evidence+computation",
    )

    failures = [item["id"] for item in checks if not item["pass"]]
    report = {
        "schema": "interlanguage.cjk.noether.p37.source_parity.v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "scope": "Noether Paper 37, sealed-P31-keyed logical article vs zh-Hans-CN target",
        "comparison_method": {
            "kind": "semantic topology and named formula signatures",
            "explicitly_not_used": "naive ordered inline-math equality",
            "canonicalizations": [
                r"target \srcemph treated as source-semantic \emph for the emphasis count",
                r"\frakC and \mathfrak C treated as \mathfrak{C}",
                r"\frakP and \mathfrak P treated as \mathfrak{P}",
                r"language-only \hbox text ignored within display signatures",
                "whitespace normalized",
            ],
            "not_canonicalized_because_semantic": [
                r"\frako versus \frakO case",
                "indices",
                "multiplication versus division",
                "roman P versus fraktur P",
            ],
        },
        "hashes": hashes,
        "structure": {"source": source_structure, "target": target_structure},
        "checks": checks,
        "status": "PASS" if not failures else "FAIL",
        "unresolved_parity_issues": failures,
        "validation_boundary": (
            "Automated source-parity computation; not external, community, or human certification."
        ),
    }
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{report['status']}: {OUTPUT}")
    if failures:
        print("Failed checks: " + ", ".join(failures))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
