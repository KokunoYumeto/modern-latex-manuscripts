/-
ClassicalAudit — Ernst Steinitz, *Algebraische Theorie der Körper*.
T4: a field of exponential characteristic p is perfect iff its Frobenius is surjective.
Build: `lake env lean Steinitz.lean` from helix_frobenius-master.
-/
import Mathlib

namespace ClassicalAudit.Steinitz

/-- **Steinitz** (perfect/imperfect dichotomy).  A field `K` of exponential characteristic `p`
is perfect (every irreducible polynomial is separable; equivalently `PerfectRing K p`) iff its
Frobenius endomorphism `x ↦ x^p` is surjective.
SOURCE: Steinitz, *Algebraische Theorie der Körper* (1910), §-on perfect fields. -/
theorem perfectRing_iff_frobenius_surjective
    (K : Type*) [Field K] (p : ℕ) [ExpChar K p] :
    PerfectRing K p ↔ Function.Surjective (frobenius K p) := by
  refine ⟨fun h => ?_, fun h => ?_⟩
  · haveI := h
    exact surjective_frobenius K p
  · exact PerfectRing.ofSurjective K p h

#print axioms perfectRing_iff_frobenius_surjective

end ClassicalAudit.Steinitz
