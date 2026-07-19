# Machine-readable evidence schema

Unit namespace: SGA2-VIII-IV-II-N1.

CSV primary IDs are the first column in each ledger. Every CSV must be
RFC-4180-readable, rectangular, primary-ID unique, and spreadsheet
formula-trigger safe. Corrected French lines, printed pages, physical PDF
pages, running pages, the internal printed-page marker, the excluded blank
line, and the substantive continuation cursor occupy separate fields.

JSONL uses schema_version, record_id, stable_id, record_revision, supersedes,
and superseded_by. Parent, child, unit, cross-reference, and outbound edges
must close or carry an explicit OUTBOUND: or COMPARISON: prefix. Stable IDs
persist across revisions; any later review state must be a new reciprocal
revision record rather than an overwrite.

This production self-gate does not claim independent review, a complete
Exposé VIII, or a complete SGA2 volume.
