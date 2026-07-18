from pathlib import Path
import csv, hashlib, json, re

HERE = Path(__file__).resolve().parent
T = HERE.parent
tex = T / "tex" / "R823_HG_T002_romance.tex"
source = T / "source" / "R823_HG_T002_de_exact.tex"
source_manifest = T / "source" / "R823_HG_T002_SOURCE_MANIFEST.json"
clause = T / "semantic" / "R823_HG_T002_clause_map.csv"
terms = T / "terminology" / "R823_HG_T002_TERMINOLOGY_v1.csv"
pdf = T / "build" / "R823_HG_T002_romance.pdf"
extracted = T / "qa" / "R823_HG_T002_extracted.txt"
pdfinfo = T / "qa" / "R823_HG_T002_pdfinfo.txt"

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

ids = []
for row in clauses:
    ids.extend(value.strip() for value in row["target_sentence_ids"].split(";"))
missing = [value for value in ids if f"% {value}" not in text]
assert not missing, missing
assert len(clauses) == 6
assert all(row["review_status"] == "accounted" for row in clauses)
assert all(
    hashlib.sha256(row["source_text"].encode("utf-8")).hexdigest().upper()
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
assert len(termrows) == 10
assert all(row["source_term"] and row["target_term"] and row["sense"] and row["status"] and row["source_evidence"] for row in termrows)

term_by_id = {row["term_id"]: row for row in termrows}
assert set(term_by_id) == {f"HG{i}" for i in range(36, 46)}


def target_block(sentence_id: str) -> str:
    match = re.search(
        rf"(?ms)^% {re.escape(sentence_id)}\s*$\n(.*?)(?=^% T-|^\\clearpage|\Z)",
        text,
    )
    assert match, sentence_id
    return match.group(1)

required = [
    r"C\subseteq\mathfrak D",
    r"P^{-1}CP\subseteq P^{-1}\mathfrak D P",
    "matrice regular",
    "representation isomorf",
    "classe de representation",
    "representationes reciproc",
]
assert all(value in text for value in required)
assert text.count(r"P^{-1}CP\subseteq P^{-1}\mathfrak D P") == 2
assert not re.search(r"\b(TODO|FIXME|UNTRANSLATED|PLACEHOLDER|TO_BE_FILLED)\b", text, re.I)
lexical_slash_bundles = re.findall(r"(?iu)\b[^\W\d_]+(?:-[^\W\d_]+)*\s*/\s*[^\W\d_]+(?:-[^\W\d_]+)*\b", text)
assert not lexical_slash_bundles, lexical_slash_bundles
assert "la elemento" not in text and "la matrice" not in text and "al elemento" in text
assert source.read_bytes().endswith(b"\n")
assert sha(source) == "5F58DDE60BB8C34421D81E7A418BF712C3F2860DBF8E4F0C16007A1A2689E235"
assert manifest["exact_slice_sha256"] == sha(source)
assert manifest["line_start"] == 21089 and manifest["line_end"] == 21097 and manifest["next_line"] == 21099
assert pdf.exists() and pdf.stat().st_size > 20000
assert "R823-HG-T002" in ext and "Classes de representation" in ext
assert "Pages:           2" in pdfinfo_text and "Page size:       595.276 x 841.89 pts (A4)" in pdfinfo_text

# Derive the semantic flags from the exact mapped target blocks and typed
# terminology rows. They are evidence checks, not manually asserted outcomes.
t025a = target_block("T-025A")
c_and_C_case_distinction_retained = (
    "al elemento $c$" in t025a
    and r"C\subseteq\mathfrak D" in t025a
    and r"P^{-1}CP\subseteq P^{-1}\mathfrak D P" in t025a
    and "c/C case distinction" in next(row for row in clauses if row["segment_id"] == "S026")["scope_constraints"]
)
exact_conjugation_formula_present = (
    t025a.count(r"P^{-1}CP\subseteq P^{-1}\mathfrak D P") == 1
    and r"P^{-1}CP\subseteq P^{-1}\mathfrak D P" in next(row for row in clauses if row["segment_id"] == "S026")["source_text"]
)
historical_regular_matrix_sense_noted = (
    term_by_id["HG40"]["source_term"] == "reguläre Matrix"
    and term_by_id["HG40"]["target_term"] == "matrice regular"
    and "invertible/nonsingular" in term_by_id["HG40"]["sense"]
    and term_by_id["HG40"]["status"] == "source_preserving_with_modern_note"
    and r"\emph{matrice regular} significa hic un matrice invertibile" in text
)
equivalent_isomorphic_distinction_noted = (
    term_by_id["HG38"]["target_term"] == "representation isomorf"
    and "equivalent is not automatically identical" in term_by_id["HG38"]["adverse_evidence"]
    and term_by_id["HG43"]["target_term"] == "equivalente"
    and "false collapse into isomorphic or equal" in term_by_id["HG43"]["adverse_evidence"]
    and r"\emph{Equivalente} non es fusionate con \emph{isomorf}" in text
)
assert c_and_C_case_distinction_retained
assert exact_conjugation_formula_present
assert historical_regular_matrix_sense_noted
assert equivalent_isomorphic_distinction_noted

log = {
    "artifact": "R823_HG_T002_VALIDATION",
    "status": "PASS",
    "authority_slice_sha256": sha(source),
    "source_manifest_sha256": sha(source_manifest),
    "target_tex_sha256": sha(tex),
    "pdf_sha256": sha(pdf),
    "clause_map_sha256": sha(clause),
    "terminology_sha256": sha(terms),
    "extracted_text_sha256": sha(extracted),
    "pdfinfo_sha256": sha(pdfinfo),
    "clause_rows": len(clauses),
    "target_ids": len(ids),
    "terminology_rows": len(termrows),
    "all_source_segments_accounted": all_source_segments_accounted,
    "c_and_C_case_distinction_retained": c_and_C_case_distinction_retained,
    "exact_conjugation_formula_present": exact_conjugation_formula_present,
    "historical_regular_matrix_sense_noted": historical_regular_matrix_sense_noted,
    "equivalent_isomorphic_distinction_noted": equivalent_isomorphic_distinction_noted,
    "lexical_alternative_bundles_in_running_prose": len(lexical_slash_bundles),
    "placeholders": 0,
    "validator_sha256": sha(HERE / "validate_t002.py"),
    "human_validation_rows": 0,
    "pilot_claim": False,
    "next_source_line": 21099,
}
(T / "qa" / "R823_HG_T002_validation.json").write_text(json.dumps(log, indent=2) + "\n", encoding="utf-8")
print(json.dumps(log, indent=2))
