# ClassicalAudit Lean Sidecars: Noether, Steinitz, Weber, Jordan

Date: 2026-06-30

This is a project-relevant extraction from the local Lean/Mathlib working tree. It keeps only the small classical-manuscript audit sidecars and minimal Lean project files needed to reproduce the checks.

Included Lean files:

- `NoetherIdealtheorie.lean`: two Mathlib anchors for Noether, "Idealtheorie in Ringbereichen".
- `Steinitz.lean`: perfect-field/Frobenius-surjectivity anchor for Steinitz, *Algebraische Theorie der Koerper*.
- `Weber.lean`: abstract Weber cubic identity sidecar.
- `AffineGroup.lean`: Jordan affine-line group cardinality sidecar.

Build logs are included exactly as found. These Lean files are not source certification and do not verify the historical editions. They are formalization-aided sanity anchors for claims that already have clean Mathlib counterparts or simple algebraic identities.

Excluded from this extraction: unrelated helix/phaser paper material, Python demos, `SplitZero`, and any non-manuscript side research files.
