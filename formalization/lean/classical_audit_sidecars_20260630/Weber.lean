/-
ClassicalAudit — Heinrich Weber, *Lehrbuch der Algebra* (modular / class-field volume).
T9: the Weber cubic with roots f^8, -f_1^8, -f_2^8 as an abstract polynomial identity.
(Stated in a, b, c with a^8 = b^8 + c^8 and abc = √2, sidestepping the undefined f-functions.)
Build: `lake env lean Weber.lean` from helix_frobenius-master.
-/
import Mathlib

open Polynomial

namespace ClassicalAudit.Weber

/-- **Weber** (the cubic of the Weber modular functions, abstract form).  For reals `a,b,c` with
`a^8 = b^8 + c^8` and `a*b*c = √2` (so `a^8 b^8 c^8 = 16`), the cubic
`x^3 - (a^8 b^8 + a^8 c^8 - b^8 c^8) x - 16` factors as `(x - a^8)(x + b^8)(x + c^8)`.
SOURCE: H. Weber, *Lehrbuch der Algebra*, Bd. III (Weber functions f, f_1, f_2; f^8 = f_1^8 + f_2^8). -/
theorem weber_cubic_roots (a b c : ℝ)
    (h1 : a ^ 8 = b ^ 8 + c ^ 8) (h2 : a * b * c = Real.sqrt 2) :
    (X ^ 3 - C (a ^ 8 * b ^ 8 + a ^ 8 * c ^ 8 - b ^ 8 * c ^ 8) * X - C 16 : ℝ[X])
      = (X - C (a ^ 8)) * (X + C (b ^ 8)) * (X + C (c ^ 8)) := by
  have h16 : a ^ 8 * b ^ 8 * c ^ 8 = 16 := by
    have h : a ^ 8 * b ^ 8 * c ^ 8 = ((a * b * c) ^ 2) ^ 4 := by ring
    rw [h, h2, Real.sq_sqrt (by norm_num : (2 : ℝ) ≥ 0)]; norm_num
  rw [show (16 : ℝ) = a ^ 8 * b ^ 8 * c ^ 8 from h16.symm, h1]
  simp only [map_add, map_sub, map_mul]
  ring

#print axioms weber_cubic_roots

end ClassicalAudit.Weber
