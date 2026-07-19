# Machine-readable evidence schema - SGA2-VIII-L24P

Unit stable ID: SGA2-VIII-L24P.

- Included inbound raw TeX state: French line 2723, equation-counter reset.
- Covered substantive prose: French lines 2725-2731.
- Raw TeX continuation cursor: French line 2733.
- Substantive prose continuation cursor: French line 2733 after blank 2732.

The compact continuation_cursor field in every CSV and JSONL record carries
the outbound cursor. Structural and difficulty JSONL records additionally
carry separate raw_tex_cursor and substantive_prose_cursor keys.

The five substantive CSV ledgers are UTF-8 rectangular tables. Each row has a
stable unique primary ID, unit ID, authority role, source and target locators,
status, confidence, revision, cursor, and revisit trigger. Parsed cell values
must not begin with an Excel formula sigil: equals, plus, minus, or at sign.

STRUCTURAL_INDEX.jsonl uses record_id equal to stable_id at record_revision.
Internal parent, child, cross-reference, revision, supersession, and closure
links must resolve. External links are explicitly prefixed INBOUND, OUTBOUND,
or COMPARISON.

DIFFICULTY_REVISION_LEDGER.jsonl uses unique event IDs and stable object IDs
shared with the structural ledger. A revision names the exact prior event in
supersedes; the prior event reciprocally names its closer in closed_by.

SOURCE_DEFECT_AND_EMENDATION_LEDGER.csv records both corrected French readings,
the exact contextual controls, target dispositions, comparison-candidate
deltas, confidence, and the hash of the durable coordination alert. It does
not authorize mutation of the French authority.

Validation requires exact authority hashes, rectangular and formula-safe CSV,
unique primary IDs, JSONL parse and reference closure, exact printed/physical/
running page separation, clean two-pass build, source and target 300 and 600
dpi review, extraction, font and destination checks, privacy scan, Artifact
Tool import/render inspection, and an exact self-excluding SHA-256 manifest.
