from pathlib import Path
import csv
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
T = HERE.parent
tex = T / "tex" / "R823_HG_T003_romance.tex"
source = T / "source" / "R823_HG_T003_de_exact.tex"
source_manifest = T / "source" / "R823_HG_T003_SOURCE_MANIFEST.json"
clause = T / "semantic" / "R823_HG_T003_clause_map.csv"
terms = T / "terminology" / "R823_HG_T003_TERMINOLOGY_v1.csv"
grammar = T / "grammar" / "CONTROLLED_ROMANCE_GRAMMAR_T003_DELTA_v1.csv"
pdf = T / "build" / "R823_HG_T003_romance.pdf"
extracted = T / "qa" / "R823_HG_T003_extracted.txt"
pdfinfo = T / "qa" / "R823_HG_T003_pdfinfo.txt"

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()

text = tex.read_text(encoding="utf-8")
src = source.read_text(encoding="utf-8")
ext = extracted.read_text(encoding="utf-8", errors="replace")
pdfinfo_text = pdfinfo.read_text(encoding="utf-8-sig", errors="replace")
manifest = json.loads(source_manifest.read_text(encoding="utf-8"))
with clause.open(encoding="utf-8-sig", newline="") as handle:
    clauses = list(csv.DictReader(handle))
with terms.open(encoding="utf-8-sig", newline="") as handle:
    termrows = list(csv.DictReader(handle))
with grammar.open(encoding="utf-8-sig", newline="") as handle:
    grammarrows = list(csv.DictReader(handle))

ids = []
for row in clauses:
    ids.extend(value.strip() for value in row["target_sentence_ids"].split(";"))
target_markers = set(re.findall(r"\bT-(?:\d{3}[A-Z]?|[A-Z]\d+)\b", text))
assert not [value for value in ids if value not in target_markers]
assert len(clauses) == 10 and all(row["review_status"] == "accounted" for row in clauses)
assert all(
    hashlib.sha256((row["source_text"].replace(" ⏎ ", "\n") + "\n").encode("utf-8")).hexdigest().upper()
    == row["source_text_sha256"]
    for row in clauses
)
nonblank_source_lines = {
    manifest["line_start"] + offset
    for offset, line in enumerate(src.splitlines())
    if line.strip()
}
mapped_source_lines = {
    line
    for row in clauses
    for line in range(int(row["source_line_start"]), int(row["source_line_end"]) + 1)
}
all_source_segments_accounted = nonblank_source_lines == mapped_source_lines
assert all_source_segments_accounted, (nonblank_source_lines, mapped_source_lines)
assert len(termrows) == 12 and len(grammarrows) == 4
assert all(all(row.get(field, "").strip() for field in ("source_term", "target_term", "sense", "status", "source_evidence")) for row in termrows)
assert all(all(row.get(field, "").strip() for field in ("feature", "decision", "alternatives_considered", "supporting_rationale", "adverse_evidence", "status")) for row in grammarrows)
term_by_id = {row["term_id"]: row for row in termrows}
grammar_by_feature = {row["feature"]: row for row in grammarrows}
assert set(term_by_id) == {f"HG{i}" for i in range(46, 58)}
assert set(grammar_by_feature) == {"side_actions", "implication", "paired_actions", "source_ambiguous_term"}
assert {row["status"] for row in grammarrows} == {"test_only"}


def target_block(sentence_id: str) -> str:
    match = re.search(
        rf"(?ms)^% {re.escape(sentence_id)}\s*$\n(.*?)(?=^% T-|^\\clearpage|\Z)",
        text,
    )
    assert match, sentence_id
    return match.group(1)

required = [
    r"(cm)\tau=c(m\tau)",
    r"x_i\tau=0$ implica $\tau=0",
    r"\mathfrak M=x_1\cdot\mathsf T+x_2\cdot\mathsf T+\cdots+x_n\cdot\mathsf T",
    r"c(\tau^*m^*)=\tau^*(cm)",
    r"\tau^*\!\cdot x_i^*=0$ implica $\tau^*=0",
    r"\mathfrak M^*=\mathsf T^*\!\cdot x_1+\cdots+\mathsf T^*\!\cdot x_n",
]
assert all(value in text for value in required)
assert "Algebra de quantitates hypercomplex" not in text
assert not re.search(r"\b(TODO|FIXME|UNTRANSLATED|PLACEHOLDER|TO_BE_FILLED)\b", text, re.I)
lexical_slash_bundles = re.findall(r"(?iu)\b[^\W\d_]+(?:-[^\W\d_]+)*\s*/\s*[^\W\d_]+(?:-[^\W\d_]+)*\b", text)
assert not lexical_slash_bundles
assert source.read_bytes().endswith(b"\n")
assert sha(source) == manifest["exact_slice_sha256"] == "73119810BF01CFD24D461C80A829C37326D814F217C3E4CBC2B358A1184B1D33"
assert manifest["clause_map_sha256"] == sha(clause)
assert manifest["line_start"] == 21099 and manifest["line_end"] == 21115 and manifest["next_line"] == 21117
assert src.count(r"\[") == text.count(r"\[") == 2
assert pdf.exists() and pdf.stat().st_size > 20000
assert "R823-HG-T003" in ext and "Moduls de representation" in ext
assert "Pages:           2" in pdfinfo_text and "Page size:       595.276 x 841.89 pts (A4)" in pdfinfo_text

direct_action_order_present = (
    all(token in target_block("T-032") for token in (r"$cm$", r"$m\tau$"))
    and r"$(cm)\tau=c(m\tau)$" in target_block("T-033")
    and "operand order" in grammar_by_feature["side_actions"]["decision"]
)
reciprocal_action_order_present = (
    all(token in target_block("T-036") for token in (r"$cm$", r"$\tau^*m^*$"))
    and r"$c(\tau^*m^*)=\tau^*(cm)$" in target_block("T-037")
)
zero_annihilator_conditions_present = (
    r"$x_i\tau=0$ implica $\tau=0$" in target_block("T-034")
    and r"$\tau^*\!\cdot x_i^*=0$ implica $\tau^*=0$" in target_block("T-038")
    and term_by_id["HG57"]["target_term"] == "condition de annulator zero"
    and term_by_id["HG57"]["status"] == "analytic_construction_candidate"
)
source_x_star_variation_preserved_and_noted = (
    r"$\tau^*\!\cdot x_i^*=0$" in target_block("T-038")
    and r"\mathfrak M^*=\mathsf T^*\!\cdot x_1+\cdots+\mathsf T^*\!\cdot x_n" in target_block("T-E5")
    and r"usa etiam $x_i^*$" in text
    and r"$x_1,\ldots,x_n$ sin asterisco" in text
)
source_einfach_sense_held = (
    term_by_id["HG56"]["status"] == "source_preserving_hold"
    and "historically ambiguous" in term_by_id["HG56"]["sense"]
    and r"\emph{einfach} es rendite fonte-a-fronte" in text
    and "ante revision historic" in text
    and "non-promotion" in grammar_by_feature["source_ambiguous_term"]["decision"]
)
assert direct_action_order_present
assert reciprocal_action_order_present
assert zero_annihilator_conditions_present
assert source_x_star_variation_preserved_and_noted
assert source_einfach_sense_held

log = {
    "artifact": "R823_HG_T003_VALIDATION",
    "status": "PASS",
    "authority_slice_sha256": sha(source),
    "source_manifest_sha256": sha(source_manifest),
    "target_tex_sha256": sha(tex),
    "pdf_sha256": sha(pdf),
    "clause_map_sha256": sha(clause),
    "terminology_sha256": sha(terms),
    "grammar_delta_sha256": sha(grammar),
    "extracted_text_sha256": sha(extracted),
    "pdfinfo_sha256": sha(pdfinfo),
    "clause_rows": len(clauses),
    "target_ids": len(ids),
    "terminology_rows": len(termrows),
    "grammar_delta_rows": len(grammarrows),
    "all_source_segments_accounted": all_source_segments_accounted,
    "direct_action_order_present": direct_action_order_present,
    "reciprocal_action_order_present": reciprocal_action_order_present,
    "zero_annihilator_conditions_present": zero_annihilator_conditions_present,
    "source_x_star_variation_preserved_and_noted": source_x_star_variation_preserved_and_noted,
    "source_einfach_sense_held": source_einfach_sense_held,
    "lexical_alternative_bundles_in_running_prose": 0,
    "placeholders": 0,
    "validator_sha256": sha(HERE / "validate_t003.py"),
    "human_validation_rows": 0,
    "pilot_claim": False,
    "next_source_line": 21117,
}
(T / "qa" / "R823_HG_T003_validation.json").write_text(json.dumps(log, indent=2) + "\n", encoding="utf-8")
print(json.dumps(log, indent=2))
