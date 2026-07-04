/-
Split-zero globalization `G(R) = R ⊔ {τ}` — core algebra, formalized in standard terms.
This is the "adjoin an absorbing/absent zero" construction (a `WithZero`-adjacent functor):
τ = none = the structural zero (additive identity AND multiplicative absorber);
e = some 0 = the *supported* zero, a distinct interior element (e ≠ τ).
Covers: CommSemiring (thm a); e additively idempotent; ring reflection p (thm c carrier);
the crux `hom_kills_e`; fixed locus (thm e). Boolean-character uniqueness and the localization
trichotomy are staged for the next module.
-/
import Mathlib

set_option linter.unusedSectionVars false
set_option linter.unusedSimpArgs false

namespace SplitZero

universe u

/-- The split-zero globalization `G(R) = R ⊔ {τ}`. `none` is `τ`; `some r` the supported
avatar of `r`; `e := some 0` is a supported zero distinct from `τ`. -/
structure G (R : Type u) where
  toOption : Option R
  deriving DecidableEq

variable {R : Type u}

/-- The absent point / structural zero `τ`. -/
def tau : G R := ⟨none⟩
/-- Supported avatar of a ring element. -/
@[coe] def ofR (r : R) : G R := ⟨some r⟩
/-- The supported zero `e := 0_R`, distinct from `τ`. -/
def e [Zero R] : G R := ofR 0

@[simp] theorem tau_eq : (tau : G R) = ⟨none⟩ := rfl
@[simp] theorem ofR_eq (r : R) : (ofR r : G R) = ⟨some r⟩ := rfl
theorem e_eq [Zero R] : (e : G R) = ⟨some 0⟩ := rfl

@[simp] theorem ofR_inj {a b : R} : (ofR a : G R) = ofR b ↔ a = b := by
  simp [ofR, G.mk.injEq]
@[simp] theorem ofR_ne_tau (r : R) : (ofR r : G R) ≠ tau := by
  simp [ofR, tau, G.mk.injEq]
theorem e_ne_tau [Zero R] : (e : G R) ≠ tau := ofR_ne_tau 0

section CommSemiring
variable [CommSemiring R]

/-- Addition: `τ` is the additive identity; supported elements add in `R`. -/
protected def add : G R → G R → G R
  | ⟨none⟩,   y        => y
  | x,        ⟨none⟩   => x
  | ⟨some a⟩, ⟨some b⟩ => ⟨some (a + b)⟩

/-- Multiplication: `τ` absorbs; supported elements multiply in `R`. -/
protected def mul : G R → G R → G R
  | ⟨none⟩,   _        => ⟨none⟩
  | _,        ⟨none⟩   => ⟨none⟩
  | ⟨some a⟩, ⟨some b⟩ => ⟨some (a * b)⟩

instance : Add (G R) := ⟨SplitZero.add⟩
instance : Mul (G R) := ⟨SplitZero.mul⟩
instance : Zero (G R) := ⟨tau⟩          -- 0 = τ
instance : One (G R)  := ⟨ofR 1⟩        -- 1 = some 1

@[simp] theorem zero_eq : (0 : G R) = ⟨none⟩ := rfl
@[simp] theorem one_eq : (1 : G R) = ⟨some 1⟩ := rfl

-- constructor-form reduction lemmas (these keep `+`/`*` as notation so `ring` etc. still fire)
@[simp] theorem mk_none_add (y : G R) : (⟨none⟩ : G R) + y = y := rfl
@[simp] theorem mk_add_none (x : G R) : x + (⟨none⟩ : G R) = x := by
  obtain ⟨_ | a⟩ := x <;> rfl
@[simp] theorem mk_some_add (a b : R) : (⟨some a⟩ : G R) + ⟨some b⟩ = ⟨some (a + b)⟩ := rfl
@[simp] theorem mk_none_mul (y : G R) : (⟨none⟩ : G R) * y = ⟨none⟩ := rfl
@[simp] theorem mk_mul_none (x : G R) : x * (⟨none⟩ : G R) = ⟨none⟩ := by
  obtain ⟨_ | a⟩ := x <;> rfl
@[simp] theorem mk_some_mul (a b : R) : (⟨some a⟩ : G R) * ⟨some b⟩ = ⟨some (a * b)⟩ := rfl

instance instAddCommMonoid : AddCommMonoid (G R) where
  add := (· + ·)
  add_assoc a b c := by
    obtain ⟨_ | ra⟩ := a <;> obtain ⟨_ | rb⟩ := b <;> obtain ⟨_ | rc⟩ := c <;>
      (simp only [mk_none_add, mk_add_none, mk_some_add, G.mk.injEq, Option.some.injEq]; try ring)
  zero := 0
  zero_add a := by simp
  add_zero a := by simp
  add_comm a b := by
    obtain ⟨_ | ra⟩ := a <;> obtain ⟨_ | rb⟩ := b <;>
      (simp only [mk_none_add, mk_add_none, mk_some_add, G.mk.injEq, Option.some.injEq]; try ring)
  nsmul := nsmulRec

instance instCommMonoid : CommMonoid (G R) where
  mul := (· * ·)
  mul_assoc a b c := by
    obtain ⟨_ | ra⟩ := a <;> obtain ⟨_ | rb⟩ := b <;> obtain ⟨_ | rc⟩ := c <;>
      (simp only [mk_none_mul, mk_mul_none, mk_some_mul, G.mk.injEq, Option.some.injEq]; try ring)
  one := 1
  one_mul a := by obtain ⟨_ | ra⟩ := a <;> simp
  mul_one a := by obtain ⟨_ | ra⟩ := a <;> simp
  mul_comm a b := by
    obtain ⟨_ | ra⟩ := a <;> obtain ⟨_ | rb⟩ := b <;>
      (simp only [mk_none_mul, mk_mul_none, mk_some_mul, G.mk.injEq, Option.some.injEq]; try ring)
  npow := npowRec

/-- Theorem (a): `G(R)` is a commutative semiring, with `0 = τ` (and `1 = some 1`). -/
instance instCommSemiring : CommSemiring (G R) :=
  { instAddCommMonoid, instCommMonoid with
    left_distrib := by
      intro a b c
      obtain ⟨_ | ra⟩ := a <;> obtain ⟨_ | rb⟩ := b <;> obtain ⟨_ | rc⟩ := c <;>
        (simp only [mk_none_add, mk_add_none, mk_some_add, mk_none_mul, mk_mul_none, mk_some_mul,
          G.mk.injEq, Option.some.injEq]; try ring)
    right_distrib := by
      intro a b c
      obtain ⟨_ | ra⟩ := a <;> obtain ⟨_ | rb⟩ := b <;> obtain ⟨_ | rc⟩ := c <;>
        (simp only [mk_none_add, mk_add_none, mk_some_add, mk_none_mul, mk_mul_none, mk_some_mul,
          G.mk.injEq, Option.some.injEq]; try ring)
    zero_mul := by intro a; simp
    mul_zero := by intro a; simp }

/-- `e` is additively idempotent — the single fact that drives `hom_kills_e`,
`G(R)[e⁻¹] = B`, and the absolute-halo characterization. -/
@[simp] theorem e_add_e : (e : G R) + e = e := by
  simp only [e_eq, mk_some_add, add_zero]

end CommSemiring

/-- Ring reflection `p_R : G R →+* R`, `τ ↦ 0`, `some r ↦ r`. The standard collapse
`WithZero R → R` adapted to the split carrier. -/
def reflect [CommSemiring R] : G R →+* R where
  toFun x := x.toOption.getD 0
  map_one' := rfl
  map_zero' := rfl
  map_add' x y := by
    obtain ⟨_ | a⟩ := x <;> obtain ⟨_ | b⟩ := y <;> simp
  map_mul' x y := by
    obtain ⟨_ | a⟩ := x <;> obtain ⟨_ | b⟩ := y <;> simp

@[simp] theorem reflect_ofR [CommSemiring R] (r : R) : reflect (ofR r) = r := rfl
@[simp] theorem reflect_tau [CommSemiring R] : reflect (tau : G R) = 0 := rfl

/-- Crux lemma (`cor:scalar-absolute-halo`): any semiring hom from `G R` to a *ring* kills the
supported zero `e`. This is why the universal ring reflection targets rings, and why
`G(R)[e⁻¹] = B` rather than `0`. -/
theorem hom_kills_e [CommSemiring R] {A : Type*} [CommRing A] (h : G R →+* A) :
    h (e : G R) = 0 := by
  have hi : h e + h e = h e := by rw [← map_add]; rw [e_add_e]
  have h2 : h e + h e = 0 + h e := by rw [hi, zero_add]
  exact add_right_cancel h2

section CommRing
variable [CommRing R]

/-- The set of `⊗`-fixed points of a ring element `u` acting on `G R`. -/
def Fix (u : R) : Set (G R) := {x : G R | (ofR u) * x = x}

/-- Theorem (e): `Fix(u) = {τ} ∪ ofR '' Ann_R(u-1)`. Stated for any `u`; the paper's unit
hypothesis is only needed for the field corollary (`Ann(u-1) = {0}` for `u ≠ 1`). -/
theorem fix_eq (u : R) :
    Fix u = insert tau (ofR '' {a : R | (u - 1) * a = 0}) := by
  ext x
  obtain ⟨_ | a⟩ := x
  · simp [Fix]
  · simp only [Fix, Set.mem_setOf_eq, ofR_eq, mk_some_mul, G.mk.injEq, Option.some.injEq,
      Set.mem_insert_iff, tau_eq, reduceCtorEq, Set.mem_image, false_or]
    constructor
    · intro h
      exact ⟨a, by linear_combination h, rfl⟩
    · rintro ⟨b, hb, hbx⟩
      obtain rfl : b = a := by simpa using hbx
      linear_combination hb

end CommRing

end SplitZero
