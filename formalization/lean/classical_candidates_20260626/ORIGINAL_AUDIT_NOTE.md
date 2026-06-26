# Classical Lean Audit Watch - 2026-06-25

This is a watch/audit handoff, not a DOI-ready publication package.

## Local roots

- C:\Users\Floris\Documents\classical_lean_audit
- C:\Users\Floris\Downloads\helix_extract\helix_frobenius-master
- C:\Users\Floris\Documents\arxiv_latex\_lean

## Sense check

- Active historical-formalization files rebuilt locally with `lake env lean` from `helix_frobenius-master`:
  - `AffineGroup.lean`: exit 0; `ClassicalAudit.Jordan.card_aff`; ordinary Mathlib axioms only.
  - `Steinitz.lean`: exit 0; `ClassicalAudit.Steinitz.perfectRing_iff_frobenius_surjective`; ordinary Mathlib axioms only.
  - `Weber.lean`: exit 0; `ClassicalAudit.Weber.weber_cubic_roots`; ordinary Mathlib axioms only.
- `ClassicalBatch2.lean` is retained as provenance only. Its log shows an older failed Steinitz API attempt and should be treated as superseded by `Steinitz.lean`.
- `SplitZero.lean` rebuilt exit 0, but it is a separate side-paper formalization, not a transcription/translation deliverable.

## 2026-06-25 recheck

- Re-ran `lake env lean` on `AffineGroup.lean`, `Steinitz.lean`, `Weber.lean`, `ClassicalBatch2.lean`, and `SplitZero.lean` in `C:\Users\Floris\Downloads\helix_extract\helix_frobenius-master`.
- `AffineGroup.lean`, `Steinitz.lean`, and `Weber.lean` still build exit 0 and print only ordinary Mathlib classical axioms.
- `ClassicalBatch2.lean` still fails and prints `sorryAx`; keep it as failed provenance only.
- `SplitZero.lean` builds exit 0 in the current recheck log, but it has no `#print axioms` audit in this packet and remains a separate side-paper lane.
- Fresh logs are stored under `03_build_logs\Recheck_20260625_*.buildlog.txt`.

## Public-status rule

Do not make a DOI or public proof claim yet. Before publication, require: exact Lean/Mathlib toolchain metadata, clean build logs, `#print axioms` logs, no `sorry`, source anchors to the actual transcribed TeX/public catalog, and a human-readable statement distinguishing formal theorem, source theorem, and any modern restatement.

## Workflow lesson

The useful archival role of this lane is not just proof checking. It can become a machine-verifiable target layer for selected explicit algebra/arithmetic statements extracted from the transcription corpus. But the authoritative source inventory must be the GitHub/public catalog and transcribed TeX, not loose local scan folders.
