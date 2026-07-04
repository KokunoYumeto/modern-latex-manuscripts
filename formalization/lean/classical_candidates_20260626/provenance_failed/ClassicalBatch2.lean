/-
ClassicalAudit batch 2 — de-risk probes:
  T2 (Jordan): number of primitive roots mod p = φ(p−1)
  T4 (Steinitz): char-p field perfect ⟺ Frobenius surjective
Build: `lake env lean ClassicalBatch2.lean` from helix_frobenius-master.
-/
import Mathlib

namespace ClassicalAudit.Jordan

/-- **Jordan, Traité §50.**  The number of primitive roots mod `p` (generators of `(ZMod p)ˣ`,
i.e. units of order `p−1`) equals `φ(p−1)`. -/
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

namespace ClassicalAudit.Steinitz

/-- **Steinitz, *Algebraische Theorie der Körper*.**  A field of characteristic `p` is perfect
iff its Frobenius endomorphism is surjective. -/
theorem perfectRing_iff_frobenius_surjective
    (K : Type*) [Field K] (p : ℕ) [Fact p.Prime] [CharP K p] :
    PerfectRing K p ↔ Function.Surjective (frobenius K p) :=
  ⟨fun _ => (PerfectRing.bijective_frobenius K p).surjective,
   fun h => PerfectRing.ofSurjective K p h⟩

#print axioms perfectRing_iff_frobenius_surjective

end ClassicalAudit.Steinitz
