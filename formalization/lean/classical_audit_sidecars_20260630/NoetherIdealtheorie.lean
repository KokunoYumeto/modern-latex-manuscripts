/-
ClassicalAudit — Emmy Noether, "Idealtheorie in Ringbereichen" (1921).

Purpose:
  This is not a replacement for the German source-critical edition. It is a
  Lean sidecar for claims that already have exact Mathlib counterparts, so
  they can be used as a formalization-aided transcription sanity check.

Build:
  lake env lean NoetherIdealtheorie.lean
-/
import Mathlib

namespace ClassicalAudit.Noether.Idealtheorie1921

/-- Noether, "Idealtheorie in Ringbereichen", Satz I / finite-basis principle:
the ascending-chain/noetherian condition for ideals is equivalent in Mathlib to
every ideal being finitely generated.

Source-audit use: if the German transcription says the chain condition is
equivalent to every ideal having a finite ideal basis, this is the Mathlib
anchor for that formal claim. -/
theorem noetherianRing_iff_every_ideal_finitely_generated
    (R : Type*) [Semiring R] :
    IsNoetherianRing R ↔ ∀ I : Ideal R, I.FG := by
  exact isNoetherianRing_iff_ideal_fg R

/-- Noether's primary-ideal condition, expressed in Mathlib's radical form:
`I` is primary iff it is proper and whenever `x*y ∈ I`, either `x ∈ I` or
`y` lies in the radical of `I`, i.e. some power of `y` lies in `I`.

Source-audit use: this anchors the German condition "product in q implies one
factor in q or a power of the other factor in q" without forcing every old
divisibility phrase into modern notation at once. -/
theorem primaryIdeal_iff_factor_or_power_condition
    {R : Type*} [CommSemiring R] {I : Ideal R} :
    I.IsPrimary ↔ I ≠ ⊤ ∧ ∀ {x y : R}, x * y ∈ I → x ∈ I ∨ y ∈ I.radical := by
  exact Ideal.isPrimary_iff

#print axioms noetherianRing_iff_every_ideal_finitely_generated
#print axioms primaryIdeal_iff_factor_or_power_condition

end ClassicalAudit.Noether.Idealtheorie1921
