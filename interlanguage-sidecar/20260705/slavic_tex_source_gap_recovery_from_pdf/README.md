# Slavic TeX Source Gap Recovery From Rendered PDFs 20260705

Status: source-body recovery candidate package / non-canonical.

Purpose: recover findable TeX source-body candidates for gap rows where rendered PDFs exist but the cumulative source-corrected unit is missing a matching translated TeX row.

Inputs:
- Gap queue: C:\Users\memo_\Documents\Codex\2026-07-04\noether-slavic-canonical-baseline\interlanguage-sidecar\20260705\slavic_gap_recovery_queue\gap_recovery_queue.csv
- Language output root: C:\Users\memo_\Documents\Codex\2026-07-04\noether-slavic-canonical-baseline\noether-language-output\slavic-ru-uk-isv

Outputs:
- tex_source_gap_recovery_queue.csv: one row per PDF-present TeX-source gap.
- staged_tex_source_candidates.csv/jsonl: copied adjacent TeX candidates with hashes and PDF evidence links.
- source-bodies/: staged TeX-family source candidates copied from noether-language-output/slavic-ru-uk-isv.
- remaining_tex_source_blockers.csv: rows that still need source search or non-canonical reconstruction.

Boundaries:
- Staged TeX bodies are adjacent candidates for source checking, not source certification.
- No canonical reader/glossary mutation was performed.
- No native review, accepted terminology, canonical approval, license clearance, gate promotion, source certification, final status, or translation completion is claimed.
- No Git push was made by this lane.
