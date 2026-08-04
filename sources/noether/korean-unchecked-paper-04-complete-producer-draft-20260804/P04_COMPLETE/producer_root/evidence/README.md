# Noether Paper 4 Korean T01--T03 reproducibility evidence

This evidence freeze covers only T01-U01 through U04, T02-U05 through U09, and T03-U10 through U16. T04--T06 are out of scope even if later target files exist.

- structural_index/ contains the authoritative hierarchical JSONL, its CSV projection, a field-documented schema, and a deterministic PASS report.
- difficulty_ledger/ contains the append-only hash chain for the observed metadata/tooling events supplied for preservation, plus its CSV projection, schema, and PASS report.
- visual_evidence/ contains a documented zero-record JSONL/CSV inventory because no visual was used or created.
- csv_artifact_validation/ contains the no-render @oai/artifact-tool CSV import/inspection validator and its report.

Primary structural records partition every physical line in each scoped source slice and target file exactly once. Annotation records may overlap their parent lines for footnotes, bibliography cues, authors, or tagged equations. Cross-language links use only explicit tags or same-type occurrence parity and remain unchecked.

Boundary: no source/Korean/formula review, compilation, rendering, assembly, packaging, certification, approval, German patch, scan work, or SGA work is performed or implied.
