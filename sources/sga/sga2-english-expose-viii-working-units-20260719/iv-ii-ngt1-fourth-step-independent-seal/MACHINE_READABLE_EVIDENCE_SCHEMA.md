# Machine-readable evidence schema

Unit namespace: `SGA2-VIII-IV-II-NGT1`.

CSV primary IDs are the first column in each ledger. Every CSV is required to
be UTF-8, RFC-4180-readable, rectangular, primary-ID unique, and spreadsheet
formula-trigger safe. Corrected French lines, printed pages, physical PDF
pages, running pages, the physical page break, the internal `pageoriginale`
token, the excluded blank, and the substantive cursor remain separate fields.

`STRUCTURAL_INDEX.jsonl` and `DIFFICULTY_REVISION_LEDGER.jsonl` use
`schema_version`, `record_id`, `stable_id`, `record_revision`, `supersedes`,
and `superseded_by`. Parent, child, unit, cross-reference, and revision edges
must close locally or carry an explicit `OUTBOUND:` prefix. The two JSONL
files are validated together because the structural record for the unresolved
line-2865 ambiguity points to the typed difficulty record that preserves its
accepted and rejected choices.

The source-alignment, formula, terminology, source-defect, and authority CSVs
contain 64 substantive rows. Their current `status` cells carry the common
terminal seal state; separate coverage, result, verification, decision, and
issue-state fields preserve the substantive disposition. The structural JSONL
contains 31 records over 15 stable IDs; the append-only difficulty JSONL
contains 12 records over 5 stable IDs. Superseded draft, pre-seal, extraction-
failure, and unresolved-issue states remain visible through revision links.

The current terminal machine state is
`independently_sealed_pending_archive_custody`. This does not claim public
archive custody, publication, a complete Expose VIII, or a complete SGA2
volume.
