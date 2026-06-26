# Classical Lean Formalization Watch - 2026-06-25

This is a watch handoff for Lean formalization/library-candidate material, not a DOI-ready publication package and not an audit or certification layer for the scanned editions.

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

Do not make a public archive-certification claim from this material. Before publication as a Lean/library-candidate package, require: exact Lean/Mathlib toolchain metadata, clean build logs, `#print axioms` logs where relevant, no `sorry` in promoted modules, source or motivation anchors to the actual transcribed TeX/public catalog where applicable, and a human-readable statement distinguishing formal theorem, source/motivation statement, and any modern restatement.

## Workflow lesson

The useful role of this lane is not proof of archival source fidelity or certification of the archive. It can become a pool of useful Lean/mathlib-style formalization candidates for selected explicit algebra/arithmetic statements inspired by or extracted from the transcription corpus. The authoritative source inventory for motivation links remains the GitHub/public catalog and transcribed TeX, not loose local scan folders.
