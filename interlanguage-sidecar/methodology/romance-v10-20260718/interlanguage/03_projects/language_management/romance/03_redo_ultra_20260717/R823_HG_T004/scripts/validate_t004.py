from pathlib import Path
import csv
import hashlib
import json
import re


HERE = Path(__file__).resolve().parent
T = HERE.parent
tex = T / "tex" / "R823_HG_T004_romance.tex"
source = T / "source" / "R823_HG_T004_de_exact.tex"
source_manifest = T / "source" / "R823_HG_T004_SOURCE_MANIFEST.json"
clause_seed = T / "semantic" / "R823_HG_T004_clause_map_seed.csv"
clause = T / "semantic" / "R823_HG_T004_clause_map.csv"
terms = T / "terminology" / "R823_HG_T004_TERMINOLOGY_v1.csv"
grammar = T / "grammar" / "CONTROLLED_ROMANCE_GRAMMAR_T004_DELTA_v1.csv"
pdf = T / "build" / "R823_HG_T004_romance.pdf"
extracted = T / "qa" / "R823_HG_T004_extracted.txt"
pdfinfo = T / "qa" / "R823_HG_T004_pdfinfo.txt"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


text = tex.read_text(encoding="utf-8")
src = source.read_text(encoding="utf-8")
ext = extracted.read_text(encoding="utf-8", errors="replace")
pdfinfo_text = pdfinfo.read_text(encoding="utf-8-sig", errors="replace")
manifest = json.loads(source_manifest.read_text(encoding="utf-8"))
clauses = read_csv(clause)
termrows = read_csv(terms)
grammarrows = read_csv(grammar)

ids = []
for row in clauses:
    ids.extend(value.strip() for value in row["target_sentence_ids"].split(";"))
target_markers = set(re.findall(r"\bT-(?:\d{3}[A-Z]?|[A-Z]\d+)\b", text))
assert not [value for value in ids if value not in target_markers]
assert len(ids) == len(set(ids)) == 16
assert len(clauses) == 7 and all(row["review_status"] == "accounted" for row in clauses)
assert all(
    hashlib.sha256((row["source_text"].replace(" ⏎ ", "\n") + "\n").encode("utf-8")).hexdigest().upper()
    == row["source_text_sha256"]
    for row in clauses
)
source_lines = {manifest["line_start"] + offset: line for offset, line in enumerate(src.splitlines())}
nonblank_source_lines = {number for number, line in source_lines.items() if line.strip()}
mapped_source_lines = {
    number
    for row in clauses
    for number in range(int(row["source_line_start"]), int(row["source_line_end"]) + 1)
}
assert nonblank_source_lines <= mapped_source_lines
assert all(not source_lines[number].strip() for number in mapped_source_lines - nonblank_source_lines)
all_source_segments_accounted = True

assert len(termrows) == 14 and len(grammarrows) == 5
assert all(all(row.get(field, "").strip() for field in ("source_term", "target_term", "sense", "status", "source_evidence")) for row in termrows)
assert all(all(row.get(field, "").strip() for field in ("feature", "decision", "alternatives_considered", "supporting_rationale", "adverse_evidence", "status")) for row in grammarrows)
term_by_id = {row["term_id"]: row for row in termrows}
grammar_by_feature = {row["feature"]: row for row in grammarrows}
assert set(term_by_id) == {f"HG{i}" for i in range(58, 72)}
assert set(grammar_by_feature) == {"uniqueness_scope", "self_map_direction", "definition_voice", "composition_order", "reference_expansion"}
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
    r"\sum y_i\tau_i\mapsto \sum y_i'\tau_i\left(=c\sum y_i\tau_i\right)",
    r"m\mapsto m'+m''(=(c_1+c_2)m)",
    r"m\mapsto (m'')'=c_1c_2m",
    r"x'_j=cx_j=\sum x_i\gamma_{ij}",
    r"x'=\sum x'_j\tau_j",
]
assert all(value in text for value in required)
assert src.count(r"\[") == text.count(r"\[") == 3
assert not re.search(r"\b(TODO|FIXME|UNTRANSLATED|PLACEHOLDER|TO_BE_FILLED)\b", text, re.I)
lexical_slash_bundles = re.findall(r"(?iu)\b[^\W\d_]+(?:-[^\W\d_]+)*\s*/\s*[^\W\d_]+(?:-[^\W\d_]+)*\b", text)
assert not lexical_slash_bundles
assert source.read_bytes().endswith(b"\n")
assert sha(source) == manifest["exact_slice_sha256"] == "2D757BFD661CE638D41F593DF6636A939AA0042477B6169A38217CAD23FB71BF"
assert manifest["clause_map_sha256"] == sha(clause)
assert manifest["line_start"] == 21117 and manifest["line_end"] == 21146 and manifest["next_line"] == 21148
assert pdf.exists() and pdf.stat().st_size > 20000
assert "R823-HG-T004" in ext and "Le relation inter moduls" in ext
page_match = re.search(r"(?m)^Pages:\s+(\d+)$", pdfinfo_text)
assert page_match and int(page_match.group(1)) >= 2
assert "Page size:       595.276 x 841.89 pts (A4)" in pdfinfo_text

uniqueness_scope_locked = (
    "in maniera unic un classe de representation" in target_block("T-039")
    and "d. D. M. a d. D. K." in target_block("T-039")
    and "Le unicitate se refere al \\emph{classe de representation}, non a un sol representation." in text
    and term_by_id["HG59"]["status"] == "construction_candidate_scope_locked"
    and "multiple representatives" in grammar_by_feature["uniqueness_scope"]["decision"]
)
self_map_without_surjectivity_claim = (
    "de $\\mathfrak M$ a se mesme" in target_block("T-041")
    and "a se mesme" in target_block("T-042")
    and "surjectivitate" in text
    and term_by_id["HG61"]["status"] == "analytic_construction_candidate"
)
composition_order_present = (
    r"$m\mapsto (m'')'=c_1c_2m$" in target_block("T-045")
    and term_by_id["HG65"]["status"] == "construction_candidate_order_locked"
    and "terminal equality c1c2m" in grammar_by_feature["composition_order"]["decision"]
)
ring_image_map_distinction_present = (
    "imagine $\\overline{\\mathfrak D}$" in target_block("T-046")
    and "homomorfism de anels" in target_block("T-046")
    and r"\emph{Imagine} nomina le anel resultante" in text
)
basis_matrix_bijection_present = (
    "base arbitrari" in target_block("T-047")
    and r"matrice $(\gamma_{ij})=C$" in target_block("T-048")
    and r"x'_j=cx_j=\sum x_i\gamma_{ij}" in target_block("T-E8")
    and "le matrices e le transformationes determina un le altere" in target_block("T-050")
    and term_by_id["HG67"]["status"] == "construction_test_candidate_not_promoted"
)
assert uniqueness_scope_locked
assert self_map_without_surjectivity_claim
assert composition_order_present
assert ring_image_map_distinction_present
assert basis_matrix_bijection_present

log = {
    "artifact": "R823_HG_T004_VALIDATION",
    "status": "PASS",
    "authority_slice_sha256": sha(source),
    "source_manifest_sha256": sha(source_manifest),
    "target_tex_sha256": sha(tex),
    "pdf_sha256": sha(pdf),
    "clause_seed_sha256": sha(clause_seed),
    "clause_map_sha256": sha(clause),
    "terminology_sha256": sha(terms),
    "grammar_delta_sha256": sha(grammar),
    "extracted_text_sha256": sha(extracted),
    "pdfinfo_sha256": sha(pdfinfo),
    "clause_rows": len(clauses),
    "target_ids": len(ids),
    "terminology_rows": len(termrows),
    "grammar_delta_rows": len(grammarrows),
    "pdf_pages": int(page_match.group(1)),
    "all_source_segments_accounted": all_source_segments_accounted,
    "uniqueness_scope_locked_to_representation_class": uniqueness_scope_locked,
    "self_map_without_surjectivity_claim": self_map_without_surjectivity_claim,
    "composition_order_c1c2_present": composition_order_present,
    "ring_image_map_distinction_present": ring_image_map_distinction_present,
    "basis_matrix_bijection_present": basis_matrix_bijection_present,
    "lexical_alternative_bundles_in_running_prose": len(lexical_slash_bundles),
    "placeholders": 0,
    "validator_sha256": sha(HERE / "validate_t004.py"),
    "human_validation_rows": 0,
    "pilot_claim": False,
    "next_source_line": 21148,
}
(T / "qa" / "R823_HG_T004_validation.json").write_text(json.dumps(log, indent=2) + "\n", encoding="utf-8")
print(json.dumps(log, indent=2))
