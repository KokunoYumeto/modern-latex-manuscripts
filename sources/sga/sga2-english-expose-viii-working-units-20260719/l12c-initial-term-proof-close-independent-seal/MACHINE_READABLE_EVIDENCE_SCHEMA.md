# Machine-readable evidence schema

CSV files are strict UTF-8 comma-delimited tables with one header row, a unique
stable primary ID in the first column, rectangular row width, and no cell whose
first non-space character is a spreadsheet formula sigil. The four substantive
tables hold source coverage, formula/symbol/note comparison, terminology and
adverse choices, and exact authority/review-control hashes. `UNIT_HASHES.csv`
is a self-excluding exact manifest with safe relative paths.

JSONL files contain exactly one UTF-8 JSON object per nonblank line. Every
record has a stable ID, unique revision/event ID, revision number, status,
confidence, continuation cursor, and revisit condition. Parent/child and local
cross-references close; external links carry `INBOUND:` or `OUTBOUND:`;
supersession and closure links are reciprocal. Correction dispositions preserve
the distinction between source authority, compiled-page evidence, comparison
lineage, and workflow review evidence.

Validation covers CSV parsing and formula safety, JSON duplicate-key and schema
checks, hierarchy/reference/revision closure, exact authority bytes/hashes,
build diagnostics, PDF/font facts, render hashes, privacy patterns, and exact
manifest bytes/hashes.

