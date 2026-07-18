from pathlib import Path
import csv
import hashlib
import json
import re


HERE = Path(__file__).resolve().parent
T = HERE.parent
REPOSITORY_ROOT = T.parents[4]
tex = T / "tex" / "R823_HG_T005_romance.tex"
source = T / "source" / "R823_HG_T005_de_exact.tex"
source_numbered = T / "source" / "R823_HG_T005_de_numbered.txt"
source_manifest = T / "source" / "R823_HG_T005_SOURCE_MANIFEST.json"
clause_seed = T / "semantic" / "R823_HG_T005_clause_map_seed.csv"
clause = T / "semantic" / "R823_HG_T005_clause_map.csv"
terms = T / "terminology" / "R823_HG_T005_TERMINOLOGY_v1.csv"
grammar = T / "grammar" / "CONTROLLED_ROMANCE_GRAMMAR_T005_DELTA_v1.csv"
pdf = T / "build" / "R823_HG_T005_romance.pdf"
output_pdf = REPOSITORY_ROOT / "output" / "pdf" / "R823_HG_T005_controlled_romance.pdf"
extracted = T / "qa" / "R823_HG_T005_extracted.txt"
pdfinfo = T / "qa" / "R823_HG_T005_pdfinfo.txt"
texlog = T / "build" / "R823_HG_T005_romance.log"
console_log = T / "build" / "R823_HG_T005_lualatex_console.log"
passone_log = T / "build" / "R823_HG_T005_lualatex_pass1.log"
render_dir = T / "qa" / "rendered"
visual_qa = T / "qa" / "R823_HG_T005_VISUAL_QA.md"
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

ids = []
for row in clauses:
    ids.extend(value.strip() for value in row["target_sentence_ids"].split(";"))
target_markers = set(re.findall(r"\bT-(?:\d{3}[A-Z]?|[A-Z]\d+)\b", text))
assert not [value for value in ids if value not in target_markers]
assert len(ids) == len(set(ids)) == 15
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
assert all(not source_lines[number].strip() for number in mapped_source_lines - nonblank_source_lines)
all_source_segments_accounted = True

assert len(termrows) == 15 and len(grammarrows) == 6
assert all(
    all(row.get(field, "").strip() for field in ("source_term", "target_term", "sense", "status", "source_evidence", "alternatives_or_crosswalk", "adverse_evidence", "rationale"))
    for row in termrows
)
assert all(
    all(row.get(field, "").strip() for field in ("feature", "decision", "alternatives_considered", "supporting_rationale", "adverse_evidence", "status"))
    for row in grammarrows
)
term_by_id = {row["term_id"]: row for row in termrows}
grammar_by_feature = {row["feature"]: row for row in grammarrows}
assert set(term_by_id) == {f"HG{i}" for i in range(72, 87)}
assert set(grammar_by_feature) == {
    "row_vector_side",
    "symbol_case_pairing",
    "homomorphism_order",
    "basis_change_direction",
    "class_quantifier_scope",
    "negative_scope_note",
}
assert {row["status"] for row in grammarrows} == {"test_only"}
assert not any("promoted" == row["status"].strip().lower() for row in termrows)


def target_block(sentence_id: str) -> str:
    match = re.search(
        rf"(?ms)^% {re.escape(sentence_id)}\s*$\n(.*?)(?=^% T-|^\\clearpage|\Z)",
        text,
    )
    assert match, sentence_id
    return match.group(1)


required = [
    r"c(x_1,\ldots,x_n)=(x_1,\ldots,x_n)C",
    r"d(x_1,\ldots,x_n)=(x_1,\ldots,x_n)D",
    r"(c+d)(x_1,\ldots,x_n)",
    r"&=(x_1,\ldots,x_n)(C+D)",
    r"cd(x_1,\ldots,x_n)",
    r"&=(cx_1,\ldots,cx_n)D=(x_1,\ldots,x_n)CD",
    r"(y_1,\ldots,y_n)=(x_1,\ldots,x_n)P",
    r"&=(y_1,\ldots,y_n)P^{-1}CP",
]
assert all(value in text for value in required)
assert src.count(r"\[") == text.count(r"\[") == 7
assert not re.search(r"\b(TODO|FIXME|UNTRANSLATED|PLACEHOLDER|TO_BE_FILLED)\b", text, re.I)
lexical_slash_bundles = re.findall(
    r"(?iu)\b[^\W\d_]+(?:-[^\W\d_]+)*\s*/\s*[^\W\d_]+(?:-[^\W\d_]+)*\b",
    text,
)
assert not lexical_slash_bundles
assert source.read_bytes().endswith(b"\n")
assert sha(source) == manifest["exact_slice_sha256"] == "90FBAF614F9DDF01AD4C80227E73A0685D7B5454B87F3D0A667654DF4F74DE8A"
assert manifest["authority_sha256"] == "EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21"
assert manifest["clause_map_sha256"] == sha(clause)
assert manifest["line_start"] == 21148 and manifest["line_end"] == 21202
assert manifest["next_line"] == 21209
assert manifest["intervening_scaffolding"]["line_start"] == 21204
assert manifest["intervening_scaffolding"]["line_end"] == 21208
assert pdf.exists() and pdf.stat().st_size > 20000
assert output_pdf.exists() and sha(output_pdf) == sha(pdf) and output_pdf.read_bytes() == pdf.read_bytes()
assert "R823-HG-T005" in ext and "Isomorfia e cambio de base" in ext
page_match = re.search(r"(?m)^Pages:\s+(\d+)$", pdfinfo_text)
assert page_match and int(page_match.group(1)) == 3
assert "Page size:       595.276 x 841.89 pts (A4)" in pdfinfo_text

row_vector_convention_locked = (
    r"c(x_1,\ldots,x_n)=(x_1,\ldots,x_n)C" in target_block("T-E9")
    and r"d(x_1,\ldots,x_n)=(x_1,\ldots,x_n)D" in target_block("T-E10")
    and "vector-riga" in text
    and term_by_id["HG74"]["status"] == "notation_carried_order_locked"
    and "place C D and P on its right" in grammar_by_feature["row_vector_side"]["decision"]
)
symbol_pairing_present = (
    "al transformation linear generate per $c" in target_block("T-051")
    and "corresponde le matrice $C$" in target_block("T-051")
    and "al elemento $d" in target_block("T-052")
    and "corresponde le matrice $D" in target_block("T-052")
    and r"$c\mapsto C$ e $d\mapsto D$" in text
)
addition_product_order_present = (
    r"&=(x_1,\ldots,x_n)(C+D)." in target_block("T-E11")
    and r"&=(cx_1,\ldots,cx_n)D=(x_1,\ldots,x_n)CD." in target_block("T-E12")
    and r"$cd\mapsto CD$" in text
    and term_by_id["HG77"]["status"] == "construction_candidate_order_locked"
    and "cd to CD" in grammar_by_feature["homomorphism_order"]["decision"]
)
basis_change_conjugation_present = (
    r"(y_1,\ldots,y_n)=(x_1,\ldots,x_n)P." in target_block("T-E13")
    and r"$P^{-1}CP$" in target_block("T-057")
    and r"&=(y_1,\ldots,y_n)P^{-1}CP." in target_block("T-E14")
    and term_by_id["HG84"]["status"] == "construction_candidate_order_locked"
    and "new matrix is P^{-1}CP" in grammar_by_feature["basis_change_direction"]["decision"]
)
representation_class_scope_locked = (
    "tote le representationes de un classe de representation" in target_block("T-059")
    and "si tote le bases de $\\mathfrak M$ es usate" in target_block("T-059")
    and "Isto non affirma que tote le matrices de $\\mathsf T_n$ es obtenite" in text
    and "ni que $\\mathfrak M$ produce tote le classes de representation" in text
    and term_by_id["HG85"]["status"] == "construction_candidate_scope_locked"
)
assert row_vector_convention_locked
assert symbol_pairing_present
assert addition_product_order_present
assert basis_change_conjugation_present
assert representation_class_scope_locked

warning_pattern = re.compile(
    r"Overfull|Underfull|Missing character|LaTeX Warning|Package .* Warning|Undefined control sequence|Emergency stop|Fatal error",
    re.I,
)
warning_hits = warning_pattern.findall(log_text)
assert not warning_hits

rendered = sorted(render_dir.glob("R823_HG_T005_page-*.png"))
assert len(rendered) == int(page_match.group(1)) == 3
render_hashes = {path.name: sha(path) for path in rendered}

log = {
    "artifact": "R823_HG_T005_VALIDATION",
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
    "build_script_sha256": sha(HERE / "build_t005.ps1"),
    "validator_sha256": sha(HERE / "validate_t005.py"),
    "visual_qa_sha256": sha(visual_qa),
    "continuation_cursor_sha256": sha(cursor),
    "clause_rows": len(clauses),
    "target_ids": len(ids),
    "terminology_rows": len(termrows),
    "grammar_delta_rows": len(grammarrows),
    "pdf_pages": int(page_match.group(1)),
    "rendered_page_sha256": render_hashes,
    "all_source_segments_accounted": all_source_segments_accounted,
    "row_vector_convention_locked": row_vector_convention_locked,
    "c_C_d_D_pairing_present": symbol_pairing_present,
    "addition_C_plus_D_and_product_CD_order_present": addition_product_order_present,
    "basis_change_y_equals_xP_and_P_inverse_CP_present": basis_change_conjugation_present,
    "representation_class_scope_locked": representation_class_scope_locked,
    "no_all_matrices_claim": representation_class_scope_locked,
    "final_warning_scan_hits": len(warning_hits),
    "lexical_alternative_bundles_in_running_prose": len(lexical_slash_bundles),
    "placeholders": 0,
    "human_validation_rows": 0,
    "native_validation": False,
    "pilot_claim": False,
    "next_source_line": 21209,
}
(T / "qa" / "R823_HG_T005_validation.json").write_text(
    json.dumps(log, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(log, indent=2))
