/-
ClassicalAudit — Camille Jordan, *Traité des substitutions et des équations algébriques*.
Beachhead module: the order of the affine line group over a prime field.
Build: `lake env lean AffineGroup.lean` from helix_frobenius-master (Mathlib v4.31.0).
-/
import Mathlib

namespace ClassicalAudit.Jordan

/-- The affine group of the line over the prime field `𝔽_p`: pairs `(a, b)` with `a` a unit,
acting by `x ↦ a*x + b`.  (Camille Jordan, *Traité des substitutions*, §420.) -/
abbrev Aff (p : ℕ) [Fact p.Prime] := (ZMod p)ˣ × ZMod p

/-- **Jordan, Traité §420.**  The affine line group over `𝔽_p` has order `p(p-1)`.
SOURCE: Jordan, *Traité des substitutions et des équations algébriques*, §420. -/
theorem card_aff (p : ℕ) [Fact p.Prime] :
    Fintype.card (Aff p) = (p - 1) * p := by
  haveI : NeZero p := ⟨(Fact.out : p.Prime).pos.ne'⟩
  rw [Fintype.card_prod, ZMod.card_units_eq_totient, ZMod.card,
    Nat.totient_prime (Fact.out : p.Prime)]

#print axioms card_aff

end ClassicalAudit.Jordan
