/-
ClassicalAudit — Camille Jordan, *Traité des substitutions et des équations algébriques*.
Primitive roots over a prime field: the number of generators of `(ZMod p)ˣ` is `φ(p−1)`.
Build: `lake env lean JordanPrimitiveRoots.lean` from helix_frobenius-master (Mathlib v4.31.0).
-/
import Mathlib

namespace ClassicalAudit.Jordan

/-- **Jordan, Traité §50.** The number of primitive roots modulo a prime `p`, modeled as
generators of `(ZMod p)ˣ` or equivalently units of order `p-1`, is `φ(p-1)`.
SOURCE: Camille Jordan, *Traité des substitutions et des équations algébriques*, §50. -/
theorem card_primitiveRoots (p : ℕ) [Fact p.Prime] :
    (Finset.univ.filter (fun g : (ZMod p)ˣ => orderOf g = p - 1)).card
      = Nat.totient (p - 1) := by
  haveI : NeZero p := ⟨(Fact.out : p.Prime).pos.ne'⟩
  have hc : Fintype.card (ZMod p)ˣ = p - 1 := by
    rw [ZMod.card_units_eq_totient, Nat.totient_prime (Fact.out : p.Prime)]
  rw [← hc]
  exact IsCyclic.card_orderOf_eq_totient (dvd_refl _)

#print axioms card_primitiveRoots

end ClassicalAudit.Jordan
