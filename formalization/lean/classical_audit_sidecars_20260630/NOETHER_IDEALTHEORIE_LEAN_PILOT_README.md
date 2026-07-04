# Noether Idealtheorie Lean Pilot

Date: 2026-06-30

This is a small Lean sidecar for Emmy Noether, "Idealtheorie in Ringbereichen" (1921).

It is not a replacement for the German source-critical transcription. Its role is to anchor source-visible mathematical claims against Mathlib where the modern statement already exists.

## Built File

- `NoetherIdealtheorie.lean`

Build command from this directory:

```powershell
lake env lean NoetherIdealtheorie.lean
```

## Compiled Anchors

1. `noetherianRing_iff_every_ideal_finitely_generated`
   - Source role: Noether's finite-chain / finite-ideal-basis equivalence.
   - Mathlib anchor: `isNoetherianRing_iff_ideal_fg`.

2. `primaryIdeal_iff_factor_or_power_condition`
   - Source role: primary ideal condition: if a product lies in the ideal, then one factor lies in it or a power of the other factor does.
   - Mathlib anchor: `Ideal.isPrimary_iff`.

## Scope Rule

Use this only for formalizable claims that can be checked cleanly. It should help catch transcription drift in definitions and theorem statements, but it cannot certify prose, historical exposition, table layout, formula typography, or source-page completeness.
