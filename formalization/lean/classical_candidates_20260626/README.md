# Classical Lean Formalization Candidates 2026-06-26

This package is a small Lean/Formalization lane, not a reader-facing transcription archive. Its purpose is to expose useful candidate Lean additions inspired by the historical mathematics transcription project and related side work. The motivation is simply that Lean/mathlib needs more formal mathematics; these are candidate additions to that library ecosystem.

## Main Buildable Candidates

The files in `lean_green/` are the primary usable Lean candidates:

- `AffineGroup.lean`: Camille Jordan, affine line group over `ZMod p`; `Fintype.card (Aff p) = (p - 1) * p`.
- `JordanPrimitiveRoots.lean`: Camille Jordan, primitive roots modulo a prime; generators of `(ZMod p)ˣ` counted by `Nat.totient (p - 1)`.
- `Steinitz.lean`: Ernst Steinitz/perfect fields; `PerfectRing K p ↔ Function.Surjective (frobenius K p)`.
- `Weber.lean`: Heinrich Weber modular-function cubic, formalized as a real polynomial identity.

These are useful as Lean/mathlib-adjacent formal mathematics candidates. Their value is as library material and reusable formal statements. They are not proof or certification of the scanned editions or translations, and they are not archive-audit or source-fidelity evidence; the promoted value is as Lean/mathlib-style library material.

The internal namespace prefix `ClassicalAudit` is a legacy code namespace from the first local experiment. It should not be read as a public audit or certification claim; the promoted public meaning of this package is formalization/library candidate material.

## Side Lane

`split_support_sidecar/` contains `SplitZero.lean` and its formalization plan for the separate split-support/projectification side paper. That belongs with the side-paper DOI or a formalization companion DOI, not silently inside a historical-author record.

## Provenance And Failed Work

`provenance_failed/ClassicalBatch2.lean` is retained because it led to the extracted Jordan primitive-roots module, but the batch file itself is not a green module: its Steinitz attempt uses a stale API and the recheck log exits nonzero with `sorryAx`.

## Build Environment

The recorded local build environment is:

- Workdir: `C:\Users\Floris\Downloads\helix_extract\helix_frobenius-master`
- Toolchain: copied in `build_logs/lean-toolchain`
- Lake metadata: copied in `build_logs/lakefile.toml` and `build_logs/lake-manifest.json`
- Command pattern: `lake env lean <file>.lean`

Recheck logs in `build_logs/` report successful builds for `AffineGroup.lean`, `JordanPrimitiveRoots.lean`, `Steinitz.lean`, `Weber.lean`, and `SplitZero.lean`.

## Publication Status

Recommended Zenodo label: **Lean formalization candidates / useful formal mathematics additions**.

Do not label this as proof or certification that any historical scanned edition is faithful. The value is independent and positive: these are small formalized mathematical results and a target list for expanding Lean coverage of classical algebra, arithmetic, invariant theory, and related historical mathematics.
