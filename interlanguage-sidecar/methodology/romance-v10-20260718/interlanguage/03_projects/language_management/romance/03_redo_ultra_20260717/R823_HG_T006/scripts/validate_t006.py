from pathlib import Path
import csv
import hashlib
import json
import re


HERE = Path(__file__).resolve().parent
T = HERE.parent
REPOSITORY_ROOT = T.parents[4]

tex = T / "tex" / "R823_HG_T006_romance.tex"
source = T / "source" / "R823_HG_T006_de_exact.tex"
source_numbered = T / "source" / "R823_HG_T006_de_numbered.txt"
source_manifest = T / "source" / "R823_HG_T006_SOURCE_MANIFEST.json"
clause_seed = T / "semantic" / "R823_HG_T006_clause_map_seed.csv"
clause = T / "semantic" / "R823_HG_T006_clause_map.csv"
terms = T / "terminology" / "R823_HG_T006_TERMINOLOGY_v1.csv"
grammar = T / "grammar" / "CONTROLLED_ROMANCE_GRAMMAR_T006_DELTA_v1.csv"
pdf = T / "build" / "R823_HG_T006_romance.pdf"
output_pdf = REPOSITORY_ROOT / "output" / "pdf" / "R823_HG_T006_controlled_romance.pdf"
extracted = T / "qa" / "R823_HG_T006_extracted.txt"
pdfinfo = T / "qa" / "R823_HG_T006_pdfinfo.txt"
texlog = T / "build" / "R823_HG_T006_romance.log"
console_log = T / "build" / "R823_HG_T006_lualatex_console.log"
passone_log = T / "build" / "R823_HG_T006_lualatex_pass1.log"
render_dir = T / "qa" / "rendered"
visual_qa = T / "qa" / "R823_HG_T006_VISUAL_QA.md"
cursor = T / "CONTINUATION_CURSOR.md"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


text = tex.read_text(encoding="utf-8")
src = source.read_text(encoding="utf-8")
ext = extracted.read_text(encoding="utf-8", errors="replace")
pdfinfo_text = pdfinfo.read_text(encoding="utf-8-sig", errors="replace")
log_text = texlog.read_text(encoding="utf-8", errors="replace")
manifest = json.loads(source_manifest.read_text(encoding="utf-8"))
clauses = read_csv(clause)
termrows = read_csv(terms)
grammarrows = read_csv(grammar)

# Validate exact source binding and full nonblank-line coverage.
assert source.read_bytes().endswith(b"\n")
assert sha(source) == manifest["exact_slice_sha256"] == "2F90BDA5829FDABF1D40797C2C529DB1AA95A9207F3A2040DB9F3612F526B171"
assert manifest["authority_sha256"] == "EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21"
assert manifest["line_start"] == 21209 and manifest["line_end"] == 21254
assert manifest["next_line"] == 21256
assert manifest["intervening_scaffolding"] == {
    "line_start": 21255,
    "line_end": 21255,
    "role": "blank separator only",
}
assert manifest["clause_map_sha256"] == sha(clause)
assert len(clauses) == 8 and all(row["review_status"] == "accounted" for row in clauses)
assert all(
    hashlib.sha256((row["source_text"].replace(" ⏎ ", "\n") + "\n").encode("utf-8"))
    .hexdigest()
    .upper()
    == row["source_text_sha256"]
    for row in clauses
)
source_lines = {
    manifest["line_start"] + offset: line for offset, line in enumerate(src.splitlines())
}
nonblank_source_lines = {number for number, line in source_lines.items() if line.strip()}
mapped_source_lines = {
    number
    for row in clauses
    for number in range(int(row["source_line_start"]), int(row["source_line_end"]) + 1)
}
assert nonblank_source_lines <= mapped_source_lines
assert mapped_source_lines <= set(source_lines)
all_source_segments_accounted = True

# Validate the target map and both decision ledgers, not merely their hashes.
ids = []
for row in clauses:
    ids.extend(value.strip() for value in row["target_sentence_ids"].split(";"))
target_markers = set(re.findall(r"\bT-(?:\d{3}[A-Z]?|E\d+)\b", text))
assert len(ids) == len(set(ids)) == 17
assert not [value for value in ids if value not in target_markers]
assert len(termrows) == 18 and len(grammarrows) == 8
required_term_fields = (
    "source_term",
    "target_term",
    "sense",
    "status",
    "source_evidence",
    "alternatives_or_crosswalk",
    "adverse_evidence",
    "rationale",
)
assert all(all(row.get(field, "").strip() for field in required_term_fields) for row in termrows)
required_grammar_fields = (
    "feature",
    "decision",
    "alternatives_considered",
    "supporting_rationale",
    "adverse_evidence",
    "status",
)
assert all(all(row.get(field, "").strip() for field in required_grammar_fields) for row in grammarrows)
term_by_id = {row["term_id"]: row for row in termrows}
grammar_by_feature = {row["feature"]: row for row in grammarrows}
assert set(term_by_id) == {f"HG{i}" for i in range(87, 105)}
assert set(grammar_by_feature) == {
    "theorem_scope",
    "proof_heading",
    "module_side",
    "coefficient_uniqueness",
    "mixed_associativity",
    "direct_reciprocal_orientation",
    "class_remainder_scope",
    "zero_human_boundary",
}
assert {row["status"] for row in grammarrows} == {"test_only"}
assert not any(row["status"].strip().lower() == "promoted" for row in termrows)
expected_wordweb_links = {
    "HG87": "T17-S1",
    "HG88": "none_not_in_60_concept_spine",
    "HG89": "T17-S1",
    "HG90": "T18-S1",
    "HG91": "none_not_in_60_concept_spine",
    "HG92": "T05-S1",
    "HG93": "none_not_in_60_concept_spine",
    "HG94": "T47-S1",
    "HG95": "T05-S1",
    "HG96": "T43-S1",
    "HG97": "T05-S1",
    "HG98": "T18-S1",
    "HG99": "T05-S1",
    "HG100": "T05-S1",
    "HG101": "T17-S1",
    "HG102": "T17-S2",
    "HG103": "T05-S1",
    "HG104": "T38-S1",
}
assert {key: row["wordweb_link"] for key, row in term_by_id.items()} == expected_wordweb_links


def target_block(sentence_id: str) -> str:
    match = re.search(
        rf"(?ms)^% {re.escape(sentence_id)}\s*$\n(.*?)(?=^% T-|^\\clearpage|\Z)",
        text,
    )
    assert match, sentence_id
    return match.group(1)


# Source-critical semantic invariants.
theorem_scope_locked = (
    "Cata classe de representation es generate" in target_block("T-060")
    and "maniera indicate sub 1" in target_block("T-060")
    and "limitate al representationes direct" in target_block("T-060")
    and "retain cata classe" in grammar_by_feature["theorem_scope"]["decision"]
    and term_by_id["HG87"]["status"].endswith("scope_locked")
)
free_module_and_coordinate_rules_locked = (
    r"\mathfrak M=x_1\mathsf T+\dots+x_n\mathsf T" in target_block("T-E15")
    and r"\sum x_i\tau_i+\sum x_i\overline{\tau}_i" in target_block("T-E16")
    and r"\quad\Longleftrightarrow\quad" in target_block("T-E16")
    and r"\left(\sum x_i\tau_i\right)\varrho=\sum x_i\tau_i\varrho" in target_block("T-E16")
    and "si e solmente si" in target_block("T-E16")
    and "si e solmente si" in grammar_by_feature["coefficient_uniqueness"]["decision"]
)
action_sides_locked = (
    "modul de $\\mathsf T$ con scalars al dextra" in target_block("T-061")
    and "action de $\\mathfrak{o}$ scripte al sinistra" in target_block("T-062A")
    and r"c\sum x_i\tau_i=\sum x_i'\tau_i" in target_block("T-062A")
    and "encode action side first by operand order" in grammar_by_feature["module_side"]["decision"]
    and term_by_id["HG92"]["status"] == "equation_first_hold_side_word"
    and term_by_id["HG95"]["status"] == "equation_first_hold_side_word"
)
homomorphism_and_mixed_associativity_locked = (
    r"c+d\mapsto C+D" in target_block("T-E17")
    and r"cd\mapsto CD" in target_block("T-E17")
    and r"cd\cdot x_i=c\cdot dx_i" in target_block("T-E19")
    and r"c\left(\sum x_i\tau_i\varrho\right)" in target_block("T-E20")
    and r"\left(c\sum x_i\tau_i\right)\!\cdot\varrho" in target_block("T-E20")
    and "lege associativ mixed" in target_block("T-E20")
    and term_by_id["HG100"]["target_term"] == "lege associativ mixed"
)
direct_reciprocal_orientation_locked = (
    r"(x_1',\ldots,x_n')=(x_1,\ldots,x_n)C" in target_block("T-062A")
    and r"\mathfrak M^*=\mathsf T^*x_1^*+\dots+\mathsf T^*x_n^*" in target_block("T-E21")
    and r"=C\begin{pmatrix}x_1\\ \vdots\\ x_n\end{pmatrix}" in target_block("T-E22")
    and "displayed unstarred column" in term_by_id["HG104"]["sense"]
    and "without inventing stars" in term_by_id["HG104"]["rationale"]
    and "keep the direct row with matrices on the right" in grammar_by_feature["direct_reciprocal_orientation"]["decision"]
    and term_by_id["HG104"]["status"].endswith("order_locked")
)
one_class_basis_scope_locked = (
    "restante representationes del classe" in target_block("T-065")
    and "representationes differente de un classe" in target_block("T-E22")
    and "non affirma que le modul es unic" in text
    and "fixed equivalence class" in grammar_by_feature["class_remainder_scope"]["supporting_rationale"]
)
assert theorem_scope_locked
assert free_module_and_coordinate_rules_locked
assert action_sides_locked
assert homomorphism_and_mixed_associativity_locked
assert direct_reciprocal_orientation_locked
assert one_class_basis_scope_locked

# General production and PDF assurance.
assert not re.search(r"\b(TODO|FIXME|UNTRANSLATED|PLACEHOLDER|TO_BE_FILLED)\b", text, re.I)
lexical_slash_bundles = re.findall(
    r"(?iu)\b[^\W\d_]+(?:-[^\W\d_]+)*\s*/\s*[^\W\d_]+(?:-[^\W\d_]+)*\b",
    text,
)
assert not lexical_slash_bundles
assert pdf.exists() and pdf.stat().st_size > 20000
assert output_pdf.exists() and output_pdf.read_bytes() == pdf.read_bytes()
assert "R823-HG-T006" in ext and "Del classe al modul" in ext
page_match = re.search(r"(?m)^Pages:\s+(\d+)$", pdfinfo_text)
assert page_match and int(page_match.group(1)) == 3
assert "Page size:       595.276 x 841.89 pts (A4)" in pdfinfo_text
warning_pattern = re.compile(
    r"Overfull|Underfull|Missing character|LaTeX Warning|Package .* Warning|Undefined control sequence|Emergency stop|Fatal error",
    re.I,
)
warning_hits = warning_pattern.findall(log_text)
assert not warning_hits
rendered = sorted(render_dir.glob("R823_HG_T006_page-*.png"))
assert len(rendered) == int(page_match.group(1)) == 3
render_hashes = {path.name: sha(path) for path in rendered}

log = {
    "artifact": "R823_HG_T006_VALIDATION",
    "status": "PASS",
    "authority_slice_sha256": sha(source),
    "numbered_source_sha256": sha(source_numbered),
    "source_manifest_sha256": sha(source_manifest),
    "target_tex_sha256": sha(tex),
    "pdf_sha256": sha(pdf),
    "output_pdf_sha256": sha(output_pdf),
    "output_pdf_byte_identical_to_build": True,
    "clause_seed_sha256": sha(clause_seed),
    "clause_map_sha256": sha(clause),
    "terminology_sha256": sha(terms),
    "grammar_delta_sha256": sha(grammar),
    "extracted_text_sha256": sha(extracted),
    "pdfinfo_sha256": sha(pdfinfo),
    "final_lualatex_log_sha256": sha(texlog),
    "lualatex_console_sha256": sha(console_log),
    "lualatex_pass1_sha256": sha(passone_log),
    "prepare_script_sha256": sha(HERE / "prepare_source.py"),
    "build_script_sha256": sha(HERE / "build_t006.ps1"),
    "validator_sha256": sha(HERE / "validate_t006.py"),
    "visual_qa_sha256": sha(visual_qa),
    "continuation_cursor_sha256": sha(cursor),
    "clause_rows": len(clauses),
    "target_ids": len(ids),
    "terminology_rows": len(termrows),
    "grammar_delta_rows": len(grammarrows),
    "pdf_pages": int(page_match.group(1)),
    "rendered_page_sha256": render_hashes,
    "all_source_segments_accounted": all_source_segments_accounted,
    "theorem_every_class_direct_scope_locked": theorem_scope_locked,
    "free_module_and_all_coordinate_rules_locked": free_module_and_coordinate_rules_locked,
    "left_right_action_order_locked": action_sides_locked,
    "homomorphism_and_mixed_associativity_locked": homomorphism_and_mixed_associativity_locked,
    "direct_row_reciprocal_column_orientation_locked": direct_reciprocal_orientation_locked,
    "one_class_basis_scope_locked": one_class_basis_scope_locked,
    "final_warning_scan_hits": len(warning_hits),
    "lexical_alternative_bundles_in_running_prose": len(lexical_slash_bundles),
    "placeholders": 0,
    "human_validation_rows": 0,
    "native_validation": False,
    "pilot_claim": False,
    "next_source_line": 21256,
}
(T / "qa" / "R823_HG_T006_validation.json").write_text(
    json.dumps(log, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(log, indent=2))
