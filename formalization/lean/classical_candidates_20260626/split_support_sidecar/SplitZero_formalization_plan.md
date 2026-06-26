Here is the formalization plan.

---

# Lean 4 / Mathlib formalization of `G(R)` — the split-zero core

Scope: the **CORE algebra** only (Intro-Result-1 fragments plus the foundational definitions/theorems labeled (a)–(g) at the end of the ledger). Everything past the fixed-locus / division-trichotomy / idempotent-probe layer (projective stratification, denominator points, Frobenius helix, surcomplex, arithmetic site) is explicitly **out of scope** for this first formalization and is noted as downstream in the roadmap.

---

## 1. Recommended Lean 4 representation of `G(R)`

### 1.1 The two candidate carriers

There are two mathematically equivalent models in the ledger:

- **Disjoint-union model**: `G(R) := R ⊔ {τ}`, carrier `Option R` with `none = τ`, `some r = r`.
- **Subtype-of-product model**: `D_R := {(0,0)} ∪ (R × {1}) ⊆ R × Bool`, i.e. a subtype `{p : R × Bool // p.2 = false → p.1 = 0}`.

`prop:pair-normal-form` says these are canonically isomorphic semirings. We must pick **one** as the *definitional* carrier and prove the other is an iso.

### 1.2 Recommendation: `Option R` as the primary carrier

**Use `Option R` with `none := τ`, and a dedicated `structure`/`def`-wrapper type, not a bare type alias.**

Concretely, define a one-field structure (or `def` with `Option R`) so we can hang instances on it without polluting `Option R`'s own (nonexistent / conflicting) algebraic instances:

```lean
structure SplitZero (R : Type*) where
  toOption : Option R
```

with notation `G R := SplitZero R`, `τ := ⟨none⟩`, and `e := ⟨some 0⟩`.

**Why `Option R` over the subtype:**

1. **`τ` is genuinely a fresh point not in `R`.** `Option R` makes `none` definitionally distinct from every `some r`, including `some 0`. This is exactly the `e ≠ τ` requirement, and it holds *by `injection`/`Option.noConfusion`* with zero proof obligation. In the subtype model `τ = ⟨(0,false)⟩` and `e = ⟨(0,true)⟩`; distinctness is true but you must reason about the `Bool` tag every time.
2. **Pattern matching gives clean `add`/`mul` definitions.** The multiplication `τ ⊗ x = τ` (absorbing) and addition `τ ⊕ x = x` (identity) are literally the `Option` "match on `none`" cases. With `Option`, `mul`/`add` are total functions defined by `match` with no side conditions. The subtype forces you to *re-establish the invariant* `p.2 = false → p.1 = 0` after every operation (a proof obligation per field of the resulting pair), which is pure friction.
3. **`0 = τ`, not `0 = e`.** The semiring zero of `G(R)` is `τ` (the additive identity / absorber), and the multiplicative one is `some 1`. `e = some 0` is an *interior, non-distinguished* element. `Option`'s `none` is the natural home for the structural zero/absorber; aligning `0 := none` makes the `MulZeroClass`/`zero_mul` proofs definitional.
4. **The subtype carrier is still wanted — as the iso target.** Keep `D_R` for `prop:pair-normal-form`; it is the bridge to the "concrete model inside `R × Bool`" and to the support character `χ = π₂`. But it is a *theorem*, not the carrier.

**Caveat / the one place `Option` bites:** Mathlib's `Option` already carries `Option.instAdd`-style instances in some files and `WithZero`/`WithTop`/`WithBot` are themselves `def Option`. To avoid instance clashes and accidental defeq with `WithZero R` (whose multiplication is the *wrong* one — `WithZero` makes `none` the absorbing zero for `*` but there is no separate `e`, and its `+` is not ours), **wrap in the `structure` above** rather than using `Option R` or `WithZero R` raw. This is the decisive reason for the wrapper.

> Do **not** reuse `WithZero R`. `WithZero R = Option R` with `none` as `0`, and its `MulZeroClass` matches our `τ`-absorbing `⊗`. But `WithZero` provides **no addition** matching `⊕` (it's built for groups-with-zero / `MulZeroClass`, where `none` is the `*`-absorber and there is no additive structure identifying `none` as `+`-identity with a *second* interior zero `e`). Forcing our `+` onto `WithZero` would mean fighting its intended API. A fresh structure is cleaner.

### 1.3 Definitional choices fixed up front

| Concept | Lean definition |
|---|---|
| carrier | `structure SplitZero (R) where toOption : Option R` |
| `τ` (absent / `0`) | `⟨none⟩`; this is `(0 : G R)` |
| `e` (supported zero) | `⟨some 0⟩` |
| `1` | `⟨some 1⟩` |
| `r : R ↪ G R` | `⟨some r⟩` (a ring-hom-like coercion, `RingHom`-shaped but into a semiring) |
| `⊕` (add) | `none ⊕ y = y`, `x ⊕ none = x`, `some a ⊕ some b = some (a+b)` |
| `⊗` (mul) | `none ⊗ _ = none`, `_ ⊗ none = none`, `some a ⊗ some b = some (a*b)` |
| `χ : G R → Bool` | `none ↦ false`, `some _ ↦ true` (the support character) |
| `p : G R → R` (reflection) | `none ↦ 0`, `some r ↦ r` |

Target algebraic class: **`CommSemiring (G R)`** (requires `R : CommRing`, actually only `R : CommSemiring` is needed for most of it, but the ledger fixes `R : CommRing` nonzero; keep `CommRing R` to match the paper and to get `Nontrivial`/`e ≠ τ` cleanly — though `e ≠ τ` is free from `Option`).

> Note on `Bool` as the Boolean semiring `B`: Mathlib has `Bool` with `||` (or) and `&&` (and). The Boolean **semiring** structure we need is `(Bool, ||, &&, false, true)` — `false = 0`, `true = 1`, `||` = `+`, `&&` = `*`. Mathlib provides `Bool.instCommSemiring`? **Check this** (see §4); if absent, we provide it. This is `B`. The support character lands in this semiring.

---

## 2. Ordered formalization roadmap

Each step is sized to be a self-contained PR. `⇒` marks a dependency.

**Phase 0 — carrier & elements**
0. Define `SplitZero R`, notation `G R`, the constructors `τ`, `e`, the coercion `R → G R`, and `χ`/`p` as bare functions. Prove `e ≠ τ`, `coe` injective, basic `match` simp lemmas (`τ` defeq `none`, etc.).

**Phase 1 — semiring (theorem (a))**
1. Define `Add`, `Mul`, `Zero (= τ)`, `One (= some 1)`. ⇒ 0
2. Prove `AddCommMonoid (G R)` (`τ` is `0`, commutativity/assoc by `Option` case-split + `R`'s `AddCommMonoid`). ⇒ 1
3. Prove `CommMonoidWithZero`-style multiplicative structure: `CommMonoid` on `⊗` with `1 = some 1`, plus `τ ⊗ x = τ` (`MulZeroClass` with `0 = τ`). ⇒ 1
4. Prove distributivity `x ⊗ (y ⊕ z) = x⊗y ⊕ x⊗z` and `zero_mul`/`mul_zero` (= `τ` absorbing). Assemble **`CommSemiring (G R)`**. ⇒ 2,3
   - This is **theorem (a)**.

**Phase 2 — universal maps (theorems (b),(c))**
5. `χ_R : G R →+* Bool` as a `RingHom`-into-semiring (`G R →+*₀` / bundled `*` and `+` monoid hom; in Mathlib semiring homs are `RingHom` between `Semiring`s — usable since both are `CommSemiring`). Prove it's a semiring hom. ⇒ 4
6. **Uniqueness of `χ`** (`thm:universal-maps` (b)): any semiring hom `f : G R → Bool` equals `χ`. Key: `f 1 = 1`, `f τ = 0`, and `f (some r) = 1` because `some r` ... — see proof note §3. ⇒ 5
7. `p_R : G R → R` the reflection (a `MulHom`+`AddHom`? — note **`p` is NOT additive in general**: `p(e ⊕ e) = p(some 0) = 0` ok, but `p` collapses `τ` to `0` and is additive *because* `τ` is the additive identity mapping to `0`; actually `p` **is** a semiring hom `G R → R` when `R` is a semiring — check: `p(x ⊕ y)`: if `x=τ`, `p(y) = 0 + p(y)` ✓; `some a ⊕ some b ↦ a+b` ✓. And `p(τ) = 0`, `p(x⊗y)` with `τ` absorbing ↦ `0` ✓. So `p` is a genuine `RingHom`-into-semiring). Define `p_R : G R →+* R`. ⇒ 4
8. **Universal property (`thm:universal-maps` (a))**: `(· ∘ p_R) : (R →+* A) ≃ (G R →+* A)` for `A : CommRing` — bijection `Hom_Ring(R,A) ≅ Hom_SemiRing(G R, A)`. Construct the inverse (precompose with `coe : R → G R`) and prove round-trips. ⇒ 7
   - Steps 6 + 8 are **theorems (b) and (c)** / `thm:universal-maps`.

**Phase 3 — fibre product (theorem (d), Intro-Result-1 part 1)**
9. Define the fibre product `G A ×_Bool G B` as `{ p : G A × G B // χ_A p.1 = χ_B p.2 }` (subtype of the product, equalizer of the two support chars). Give it its `CommSemiring` (pullback / subsemiring of `(G A) × (G B)`). ⇒ 5
10. Define `Φ : G (A × B) → G A ×_Bool G B`, `Φ τ = (τ,τ)`, `Φ (some (a,b)) = (some a, some b)` (lands in the fibre product since both supports are `true`). ⇒ 9
11. Prove `Φ` is a semiring hom and a bijection ⇒ **`G (A × B) ≃+* G A ×_Bool G B`** (`thm:boolean-fibre-product`, theorem (d)). ⇒ 10
12. `cor:mixed-support-source`: the four support faces and image-of-`Φ` characterization. (Mostly a `decide`/case description; formalize as the statement that image of `Φ` = `{(τ,τ)} ∪ A×B` faces.) ⇒ 11

**Phase 4 — fixed locus (theorem (e), Intro-Result-1 part 2)**
13. Define the multiplicative action of `u : Rˣ` (or `u : R`) on `G R` by `x ↦ (coe u) ⊗ x`, and `Fix u := {x | (coe u) ⊗ x = x}`. ⇒ 4
14. Prove `Fix u = {τ} ∪ (coe '' Ann_R(u-1))` where `Ann_R(u-1) = {a : R | (u-1)*a = 0}` (`thm:fixed-locus-unit`, theorem (e)). For `u : Rˣ`. ⇒ 13
15. Corollaries: field case `Fix u = G K` if `u=1` else `{τ,e} ≃ B`; `cor:boolean-involution-locus` for `u=-1` in a domain of char ≠ 2. ⇒ 14

**Phase 5 — idempotent localization & division trichotomy (theorem (f))**
16. `thm:idempotent-localization`: for a `CommSemiring A` and idempotent `a` (`a*a=a`), `A[a⁻¹] ≃ a•A` (the principal localization at `a` is iso to the ideal/sub-semiring `aA` with unit `a`). This needs the semiring localization `Localization` / `Localization.awayₛ` — **check Mathlib has semiring localization** (§4). If not, this is the heaviest step (may need to build `OreLocalization`/away-localization for `CommMonoid`-with-the-right-structure, or state the universal property directly). ⇒ 4
17. `cor:two-zero-localizations` / theorem (f): `G(R)[e⁻¹] ≃ Bool` (with localization map = `χ`) and `G(R)[τ⁻¹] ≃ 0` (zero semiring). Apply 16 with `a = e` (idempotent: `e⊗e = some(0*0)=some 0 = e` ✓) and `a = τ` (`τ⊗τ=τ` ✓). ⇒ 16
18. `thm:division-trichotomy`: assemble the three division operations (invert `R\{0} ⇒ G K`; invert `e ⇒ B`; invert `τ ⇒ 0`). The `G K` part needs `cor:fraction-comparison` `G(R)[(R\{0})⁻¹] ≃ G K`. ⇒ 17

**Phase 6 — idempotent probe (theorem (g))**
19. `thm:idempotent-probe`: `A[q]/(q²−q) ≃ A × A` for `A : CommRing`, via `eval` at `q=0,1`. This is `AdjoinRoot (X^2 - X) ≃+* A × A` or via `R[X] ⧸ (X^2 - X)`. Pure Mathlib commutative-algebra; **independent of `G`**. Also `Ω¹_{C/A} = 0`. ⇒ (independent, can be done anytime)
20. Finite-difference identity `f(x+qh) = f(x) + q(f(x+h)−f(x))` in `C = A[q]/(q²−q)`, and the `idempotence vs nilpotence` corollary (`q²=q ∧ q²=0 ⇒ q=0` in nonzero ring). ⇒ 19

**Phase 7 — spectral/ideal core (optional, Intro-Result-1 adjacent)**
21. `thm:prime-classification`, `thm:generic-suspension`, `cor:split-stalks` — ideal/prime structure of `G R`. Heavier (needs `PrimeSpectrum` for semirings, which Mathlib has only for *rings*; would need `Spec` of a `CommSemiring`). **Flag as out-of-scope for v1**, list as a research extension.

Everything from Intro-Result-(3) division-trichotomy details onward beyond the above, and all of Intro-Result (4),(5),(9),(13) (projective stratification, denominator points, helix, etc.), is **downstream** and not part of this core formalization. The roadmap above covers exactly the lettered core (a)–(g) plus Intro-Result-1.

---

## 3. Draft Lean 4 source (best-effort, Mathlib-style; not guaranteed to compile)

> These are drafts to anchor the design. Names and exact Mathlib lemma calls (`simp` sets, `aesop`) will need adjustment against the live Mathlib version. Proofs marked `by sorry`-adjacent or `decide`/`aesop` are sketches.

```lean
import Mathlib.Algebra.Ring.Basic
import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Ring.Hom.Defs
import Mathlib.RingTheory.Ideal.Basic
import Mathlib.Data.Option.Basic
import Mathlib.Order.Bool        -- Bool order/lattice; semiring may be local

namespace SplitZero

universe u
variable (R : Type u)

/-- The split-zero globalization `G(R) = R ⊔ {τ}`.
`none` is the absent point `τ` (the additive identity & multiplicative absorber);
`some 0` is the *supported* zero `e`, which is distinct from `τ`. -/
structure G (R : Type u) where
  toOption : Option R
  deriving DecidableEq

variable {R}

/-- The absent point / structural zero `τ`. -/
def tau : G R := ⟨none⟩

/-- Coercion of a ring element into its supported avatar. -/
@[coe] def ofR (r : R) : G R := ⟨some r⟩

instance : CoeTail R (G R) := ⟨ofR⟩

/-- The supported zero `e := 0_R`, distinct from `τ`. -/
def e [Zero R] : G R := ofR 0

@[simp] theorem ofR_inj {a b : R} : ofR a = ofR b ↔ a = b := by
  constructor
  · intro h; simpa [ofR] using congrArg G.toOption h
  · rintro rfl; rfl

@[simp] theorem ofR_ne_tau (r : R) : ofR r ≠ tau := by
  simp [ofR, tau, G.ext_iff]

theorem e_ne_tau [Zero R] : (e : G R) ≠ tau := ofR_ne_tau 0

end SplitZero
```

### 3.1 The `CommSemiring` instance (theorem (a))

```lean
namespace SplitZero
variable {R : Type u}

section Semiring
variable [CommSemiring R]   -- CommRing R also fine; CommSemiring suffices

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

-- defeq unfolding lemmas
@[simp] theorem tau_eq_zero : (tau : G R) = 0 := rfl
@[simp] theorem zero_add' (x : G R) : (0 : G R) + x = x := by
  cases x with | mk o => cases o <;> rfl
@[simp] theorem add_zero' (x : G R) : x + (0 : G R) = x := by
  cases x with | mk o => cases o <;> rfl
@[simp] theorem zero_mul' (x : G R) : (0 : G R) * x = 0 := rfl
@[simp] theorem mul_zero' (x : G R) : x * (0 : G R) = 0 := by
  cases x with | mk o => cases o <;> rfl

@[simp] theorem some_add_some (a b : R) :
    (ofR a) + (ofR b) = ofR (a + b) := rfl
@[simp] theorem some_mul_some (a b : R) :
    (ofR a) * (ofR b) = ofR (a * b) := rfl

instance : AddCommMonoid (G R) where
  add := (· + ·)
  add_assoc x y z := by
    cases x with | mk ox => cases y with | mk oy => cases z with | mk oz =>
      cases ox <;> cases oy <;> cases oz <;>
        simp_all [SplitZero.add, ofR, add_assoc]
  zero := 0
  zero_add := zero_add'
  add_zero := add_zero'
  add_comm x y := by
    cases x with | mk ox => cases y with | mk oy =>
      cases ox <;> cases oy <;> simp_all [SplitZero.add, ofR, add_comm]
  nsmul := nsmulRec   -- default

instance : CommMonoid (G R) where
  mul := (· * ·)
  mul_assoc x y z := by
    cases x with | mk ox => cases y with | mk oy => cases z with | mk oz =>
      cases ox <;> cases oy <;> cases oz <;>
        simp_all [SplitZero.mul, ofR, mul_assoc]
  one := 1
  one_mul x := by cases x with | mk o => cases o <;> simp_all [SplitZero.mul, ofR, one_mul]
  mul_one x := by cases x with | mk o => cases o <;> simp_all [SplitZero.mul, ofR, mul_one]
  mul_comm x y := by
    cases x with | mk ox => cases y with | mk oy =>
      cases ox <;> cases oy <;> simp_all [SplitZero.mul, ofR, mul_comm]

instance : CommSemiring (G R) where
  __ := (inferInstance : AddCommMonoid (G R))
  __ := (inferInstance : CommMonoid (G R))
  left_distrib x y z := by
    cases x with | mk ox => cases y with | mk oy => cases z with | mk oz =>
      cases ox <;> cases oy <;> cases oz <;>
        simp_all [SplitZero.add, SplitZero.mul, ofR, mul_add]
  right_distrib x y z := by
    cases x with | mk ox => cases y with | mk oy => cases z with | mk oz =>
      cases ox <;> cases oy <;> cases oz <;>
        simp_all [SplitZero.add, SplitZero.mul, ofR, add_mul]
  zero_mul := zero_mul'
  mul_zero := mul_zero'

end Semiring
end SplitZero
```

> **Subtlety to watch:** the distributivity case-split has a genuine mathematical content point, not just bookkeeping. Consider `x = some a`, `y = some b`, `z = none (= τ)`. Then `y ⊕ z = some b`, so `x ⊗ (y⊕z) = some (a*b)`. And `x⊗y ⊕ x⊗z = some(a*b) ⊕ τ = some(a*b)` ✓. Now `x = none`: both sides `none`. The one to verify by hand is **`x = some a, y = some b, z = some c`** reducing to `mul_add` in `R`, and every case with a `none` reducing to identity/absorber laws. The `cases … <;> simp_all` covers all 8 (`add`) / relevant combinations; if `simp_all` doesn't close a stray case, split it out manually. This is where most compile-time iteration will go.

### 3.2 Support character `χ` and its uniqueness (theorems (b))

First we need `Bool` as the Boolean semiring `B`. Provide it locally if Mathlib lacks it:

```lean
namespace BooleanSemiring
/-- The Boolean semiring `B = ({false,true}, ∨, ∧)` with `0=false, 1=true`. -/
instance : CommSemiring Bool where
  add := (· || ·)
  mul := (· && ·)
  zero := false
  one := true
  add_assoc := by decide
  zero_add := by decide
  add_zero := by decide
  add_comm := by decide
  mul_assoc := by decide
  one_mul := by decide
  mul_one := by decide
  mul_comm := by decide
  left_distrib := by decide
  right_distrib := by decide
  zero_mul := by decide
  mul_zero := by decide
  nsmul := nsmulRec
end BooleanSemiring
```

> If Mathlib already provides a `CommSemiring Bool` (it might, via `BooleanAlgebra`/`order`), **do not** redeclare — reuse it. Confirm whether its `+` is `xor` or `or`: we need **`or`** (so that `1 + 1 = 1`, the idempotent/absorbing Boolean addition), not `xor` (which would make `Bool` a *ring* `𝔽₂`). This distinction is critical — a `xor`-based `Bool` semiring is the wrong `B`. If Mathlib's instance is `xor`-based, define `B` as a fresh one-field `structure` wrapper to force `or`.

```lean
namespace SplitZero
variable {R : Type u} [CommSemiring R]
open scoped BooleanSemiring   -- the (· || ·) semiring

/-- Support character `χ_R : G R → B`, `τ ↦ false`, supported ↦ `true`. -/
def chi : G R → Bool
  | ⟨none⟩   => false
  | ⟨some _⟩ => true

@[simp] theorem chi_tau : chi (tau : G R) = false := rfl
@[simp] theorem chi_zero : chi (0 : G R) = false := rfl
@[simp] theorem chi_ofR (r : R) : chi (ofR r) = true := rfl
@[simp] theorem chi_one : chi (1 : G R) = true := rfl

/-- `χ` packaged as a semiring homomorphism `G R →+* B`. -/
def chiHom : G R →+* Bool where
  toFun := chi
  map_one' := rfl
  map_mul' x y := by
    cases x with | mk ox => cases y with | mk oy =>
      cases ox <;> cases oy <;> rfl
  map_zero' := rfl
  map_add' x y := by
    cases x with | mk ox => cases y with | mk oy =>
      cases ox <;> cases oy <;> rfl

/-- `thm:universal-maps` (b): `χ` is the *unique* semiring hom `G R → B`. -/
theorem chiHom_unique (f : G R →+* Bool) : f = chiHom := by
  ext x
  cases x with
  | mk o =>
    cases o with
    | none =>
        -- f τ = f 0 = 0 = false = chi τ
        simpa using (map_zero f)
    | some r =>
        -- key step: `some r` has a supported additive structure forcing f = true.
        -- ofR r = ofR r * 1 and χ(ofR r)=true; more robustly:
        -- 1 = ofR 1, and ofR r is "supported": ofR r + ofR 0 = ofR r, but
        -- the clean argument: every supported element x satisfies x + e = x and
        -- f respects 1.  Use: f (ofR 1) = 1 (map_one).  Then for any r,
        -- ofR r * ofR 1 = ofR r, no help directly.
        -- The real lemma: in B, the only way f(ofR r) ≠ true is f(ofR r)=false=0;
        -- but ofR r is NOT a zero divisor witness... use idempotent e:
        -- f e is idempotent in Bool (e*e=e), and ofR r * e = e for r·0=0 ⇒ f(ofR r)*f e = f e.
        -- Cleanest: show f(ofR r) = true by contradiction via support.
        sorry
```

> **Proof note on `chiHom_unique` — the genuinely load-bearing argument.**
> The hard case is showing `f (ofR r) = true` for a semiring hom `f : G R → B`. The conceptual reason: every `some r` is a *unit-supported* element under `χ`, and `B = {0,1}` has only the idempotents `0,1`. A robust Lean argument:
> 1. `f 1 = 1` (`map_one`), and `1 = ofR 1` in `G R`. So `f (ofR 1) = true`.
> 2. For arbitrary `r`: in `B`, `f(ofR r)` is either `false` or `true`. Suppose `f (ofR r) = false`. Note `ofR r ⊕ ofR 1` — careful, `ofR r + ofR 1 = ofR (r+1)`, supported, no immediate contradiction.
> 3. The clean invariant is: **`χ` is determined by what `f` does to `e`**. Since `ofR r ⊗ e = ofR (r*0) = ofR 0 = e`, we get `f(ofR r) * f(e) = f(e)` in `B`. If `f(e)=1` then `f(ofR r) = 1` for all `r`, done (and then `f τ = 0`). If `f(e)=0`, then we additionally have `e + e = e` so `f(e)` idempotent (consistent), and `ofR 1 = ofR 1`, `f(ofR 1)=1`. But `e = ofR 0` and `ofR 1 + (something) = ...`. The watertight finish: `f(e) = f(ofR 0)`, and `ofR 0 + ofR 0 = ofR 0`; in `B`, additive-idempotent is automatic. Use instead that `ofR 1 ⊗ ofR 1 = ofR 1` and the **additive** relation `e + x` for `x = ofR r` gives `ofR r` (since `0 + r = r`), so `f(e) + f(ofR r) = f(ofR r)`, i.e. `f(e) ≤ f(ofR r)` in the `or`-order. Combined with `f(ofR 1) = 1`: take `r=1`, `f(e) ≤ 1` trivial. The decisive identity is `ofR r ⊗ e = e` ⇒ `f(ofR r) ∧ f(e) = f(e)`, **and** `e ⊕ ofR r = ofR r` ⇒ `f(e) ∨ f(ofR r) = f(ofR r)`. The only `B`-solutions with `f(ofR 1)=1` force `f(ofR r)=1` whenever … — finish by `decide` over the finite `Bool` cases once these two equations on `f e, f (ofR r)` are in hand.
> The cleanest fully-formal version: prove the helper `∀ r, f (ofR r) = true` by establishing `f e = false → f (ofR r) = true` is impossible to need separately, because `ofR r + e = ofR r` and `ofR r * e = e` pin `(f (ofR r), f e)` to one of `{(true,true),(true,false)}`, both giving `f (ofR r) = true`. Then `f τ = map_zero = false`. Hence `f = chiHom`. Replace the `sorry` with this two-equation + `decide` argument.

### 3.3 Ring reflection `p` and universal property (theorem (c))

```lean
namespace SplitZero
variable {R : Type u} [CommSemiring R]

/-- Ring reflection `p_R : G R →+* R`, `τ ↦ 0`, `some r ↦ r`. -/
def reflect : G R →+* R where
  toFun
    | ⟨none⟩   => 0
    | ⟨some r⟩ => r
  map_one' := rfl
  map_mul' x y := by
    cases x with | mk ox => cases y with | mk oy =>
      cases ox <;> cases oy <;> simp_all [SplitZero.mul, mul_comm, mul_zero, zero_mul]
  map_zero' := rfl
  map_add' x y := by
    cases x with | mk ox => cases y with | mk oy =>
      cases ox <;> cases oy <;> simp_all [SplitZero.add, add_zero, zero_add]

@[simp] theorem reflect_ofR (r : R) : reflect (ofR r) = r := rfl
@[simp] theorem reflect_tau : reflect (tau : G R) = 0 := rfl

/-- `thm:universal-maps` (a): precomposition with `reflect` is a bijection
`(R →+* A) ≃ (G R →+* A)` for any commutative (semi)ring `A`.
Inverse: precompose a `G R →+* A` with the coercion `ofR`. -/
def reflectEquiv (A : Type*) [CommSemiring A] :
    (R →+* A) ≃ (G R →+* A) where
  toFun g := g.comp reflect
  invFun h := h.comp (ofRHom)        -- ofRHom : R →ₙ* / →+* G R, see below
  left_inv g := by ext r; simp [ofRHom]
  right_inv h := by
    ext x
    cases x with
    | mk o => cases o with
      | none => simp [reflect]; exact (map_zero h).symm ▸ rfl
      | some r => simp [reflect, ofRHom]
```

> `ofRHom : R →+* G R` needs care: `ofR` is **not** a ring hom in the naive sense because `ofR 0 = e ≠ τ = 0_{G R}` — i.e. `ofR` does **not** send `0_R` to `0_{G R}`! So `ofR` is a *multiplicative-monoid* hom and an *additive* hom that preserves `+` and `*` and `1` but sends `0_R ↦ e ≠ 0_{G R}`. This is the whole point of the split zero. Therefore `ofRHom` is **not** a `RingHom`. The correct statement of `thm:universal-maps` (a) uses, on the inverse direction, the composite `h ∘ ofR` where `ofR` is treated as a non-unital-respecting map; but the round-trip still works because for `h = g ∘ reflect`, `h (ofR r) = g (reflect (ofR r)) = g r`, and `reflect ∘ ofR = id_R` is a genuine ring fact. The clean formalization: define the inverse directly as `h ↦ (h ∘ ofR)` as a *function*, prove it is a `RingHom R → A` (the `map_zero` for it: `h (ofR 0) = h e`; need `h e = 0`! — this holds because `e` is **absolute-ring-null** (`cor:scalar-absolute-halo`): any semiring hom to a ring kills `e`). So the inverse map's `map_zero'` is exactly the lemma `h e = 0` for `h : G R →+* A`, `A` a ring. **This is the crux**: the bijection works *because* `e ∈ I_abs`. Formalize `h_kills_e : (A : CommRing) → (h : G R →+* A) → h e = 0` first; it is `prop:absolute-characterization` specialized. Then `reflectEquiv` goes through. Note `A` must be a `CommRing` (not just semiring) for `h e = 0` — a semiring `A` need not kill `e`. Adjust the typeclass on `A` in `reflectEquiv` to `[CommRing A]`.

Helper to formalize first:

```lean
/-- `cor:scalar-absolute-halo` (the half we need):
any semiring hom from `G R` to a *ring* `A` kills the supported zero `e`. -/
theorem hom_kills_e {A : Type*} [CommRing A] (h : G R →+* A) : h (e : G R) = 0 := by
  -- e = ofR 0, and e + e = e (since 0+0=0 in R), so h e + h e = h e in A,
  -- a ring; cancel to get h e = 0.
  have hidem : (e : G R) + e = e := by
    simp [e, ofR]   -- ofR 0 + ofR 0 = ofR (0+0) = ofR 0
  have : h e + h e = h e := by simpa [map_add] using congrArg h hidem
  -- in a ring, x + x = x ↔ x = 0
  linarith?  -- or: have := add_right_cancel ...; simpa using this
  -- concretely:  (by linear_combination this) ; or
  --   have := sub_eq_zero.mpr this ... ; simp at this
```

> `e + e = e` in `G R` (because `0+0=0` in `R`) is the key idempotency. In a **ring** `A`, `h e + h e = h e ⇒ h e = 0` (subtract). In a general semiring this fails (e.g. `B` itself: `χ e = true`, `true+true=true`, no cancellation), which is exactly why the universal property targets **rings**, and why `G(R)[e⁻¹] = B` rather than `0`.

### 3.4 Fixed locus (theorem (e)) — statement-level draft

```lean
namespace SplitZero
variable {R : Type u} [CommRing R]

/-- The annihilator-style fixed set of `u` acting by `⊗`. -/
def Fix (u : R) : Set (G R) := {x : G R | (ofR u) * x = x}

/-- `thm:fixed-locus-unit`: for a unit `u`, `Fix(u) = {τ} ∪ ofR '' Ann(u-1)`. -/
theorem fix_eq (u : Rˣ) :
    Fix (u : R) = insert tau (ofR '' {a : R | (u - 1) * a = 0}) := by
  ext x
  cases x with
  | mk o => cases o with
    | none =>
        simp [Fix, tau, SplitZero.mul]   -- τ is fixed (absorbing)
    | some a =>
        -- (ofR u)*(ofR a) = ofR a  ↔  u*a = a  ↔  (u-1)*a = 0
        simp only [Fix, Set.mem_setOf_eq, some_mul_some, ofR_inj, Set.mem_insert_iff,
                   ofR_ne_tau, false_or, Set.mem_image, Set.mem_setOf_eq]
        constructor
        · intro h; exact ⟨a, by ring_nf; linear_combination h, rfl⟩
        · rintro ⟨b, hb, hbx⟩
          have : b = a := by simpa [ofR_inj] using hbx
          subst this; linear_combination hb
```

> Uses `u : Rˣ` only to match the paper's hypothesis; the proof of the `some` case is pure `R`-algebra: `u*a = a ↔ (u-1)*a = 0`, which holds for any `u` and does not actually need invertibility. (Invertibility matters for the *field* corollary where `Ann(u-1) = 0` unless `u=1`.) The field corollary `Fix u = {τ,e} ≃ B` for `u≠1` follows because in a field `(u-1)*a=0 ∧ u≠1 ⇒ a=0`, so `Ann(u-1) = {0}` and `ofR '' {0} = {e}`.

### 3.5 Idempotent probe (theorem (g)) — independent of `G`

```lean
import Mathlib.RingTheory.AdjoinRoot
import Mathlib.Algebra.Polynomial.Basic

variable (A : Type*) [CommRing A]

/-- `thm:idempotent-probe`: `A[q]/(q²−q) ≃ A × A` via evaluation at `q = 0, 1`. -/
noncomputable def idempotentProbeEquiv :
    AdjoinRoot (Polynomial.X ^ 2 - Polynomial.X : Polynomial A) ≃+* A × A := by
  -- X^2 - X = X*(X-1); CRT / Chinese remainder along coprime (X) and (X-1)
  -- since the ideals (X) and (X-1) are comaximal in A[X].
  sorry  -- assemble from AdjoinRoot + Ideal.quotientInfRingEquivPiQuotient / CRT
```

> `X² − X = X(X−1)`, and `(X)`, `(X−1)` are comaximal in `A[X]` (`X - (X-1) = 1`). Mathlib CRT (`Ideal.quotientMulEquivQuotientProd` / `Ideal.quotientInfRingEquivPiQuotient`) plus `A[X]/(X) ≃ A` and `A[X]/(X-1) ≃ A` (evaluation) gives the iso. `Ω¹_{C/A} = 0` is a separate Kähler-differentials statement (`KaehlerDifferential`), defer.

---

## 4. Mathlib API / lemmas needed, per step

> Where I write **(verify)**, the existence/name should be confirmed against the pinned Mathlib before relying on it; these are the ones most likely to have moved or to be absent.

**Phase 0–1 (carrier, `CommSemiring`):**
- `structure ... deriving DecidableEq`; `G.ext`, `G.ext_iff` (auto from structure).
- `Option` basics: `Option.noConfusion`, `Option.some.injEq` — for `e ≠ τ`, `ofR_inj`.
- `CommSemiring`, `AddCommMonoid`, `CommMonoid`, `MulZeroClass`, `Distrib` classes and their fields.
- `nsmulRec` (default `nsmul`), `npowRec` (default `npow`) to fill structure fields.
- `R`'s lemmas: `add_assoc`, `add_comm`, `mul_assoc`, `mul_comm`, `mul_add`, `add_mul`, `zero_add`, `mul_zero`, `one_mul` — all standard.
- Tactics: `cases … with | mk`, `<;>`, `simp_all`, `aesop`, `decide`.

**Phase 2 (`Bool` semiring, `χ`, uniqueness, `p`):**
- **`CommSemiring Bool` (verify)** — does Mathlib provide an `or/and` semiring on `Bool`? Mathlib has `Bool` as `BooleanAlgebra`, and `instCommMonoid`/lattice instances, but a `Semiring` with `+ = ||` may need to be supplied locally. The competing instance is `ZMod 2 ≃ Bool` with `xor` (a *ring*). **Must ensure we use the `or`-semiring, not `xor`-ring.** Safest: local `structure B` wrapper, or `Prop`-based / `Bool` with a `letI`.
- `RingHom` between semirings: `RingHom`, `RingHom.comp`, `RingHom.ext`, `map_zero`, `map_one`, `map_add`, `map_mul`. (In Mathlib `RingHom` is defined for `NonAssocSemiring`, so semiring homs are `→+*`. ✓)
- `decide` for finite `Bool` equational reasoning in `chiHom_unique`.

**Phase 2 universal property (theorem (c)):**
- `RingEquiv` / `Equiv` for the `Hom ≃ Hom` bijection; `Equiv.ext`, `RingHom.ext`.
- The crux lemma `hom_kills_e` needs: in a `CommRing A`, `x + x = x → x = 0` — via `add_right_cancel`/`self_eq_add_left` or `linarith`/`linear_combination`/`sub_eq_zero`. Relevant: `add_right_cancel`, `add_left_cancel`, `self_eq_add_right`.
- `map_add`, `congrArg`.

**Phase 3 (fibre product, theorem (d)):**
- `Subsemiring` of a product `Prod`: `Subsemiring`, `Subsemiring.prod` / building a `CommSemiring` on the equalizer subtype. May use `RingHom.eqLocus` (**verify** name; there is `RingHom.eqLocus` for monoid/ring homs) — the fibre product `G A ×_B G B` is the equalizer of `χ_A ∘ fst` and `χ_B ∘ snd` on `(G A) × (G B)`, i.e. `RingHom.eqLocus (χ_A.comp fst) (χ_B.comp snd)` as a `Subsemiring`.
- `Prod.instCommSemiring`, `RingHom.fst`, `RingHom.snd`, `RingHom.prod`.
- `RingEquiv.ofBijective`, `Function.Bijective`, `RingHom` constructed by cases; `RingEquiv`.

**Phase 4 (fixed locus, theorem (e)):**
- `Set`, `Set.mem_setOf_eq`, `Set.mem_insert_iff`, `Set.mem_image`, `Set.insert`.
- `Units` (`Rˣ`), `Units.val`, coercion.
- `ring`, `ring_nf`, `linear_combination` for `u*a=a ↔ (u-1)*a=0`.
- For the field corollary: `Field`, `mul_eq_zero`, `sub_eq_zero`, `IsDomain`; `Ann_R` as `Ideal.annihilator`? or bare `{a | (u-1)*a=0}`. Mathlib: `Ideal.annihilator` / `Submodule.annihilator` (**verify** for ideal-of-element form; bare set-builder is simplest).

**Phase 5 (idempotent localization, division trichotomy, theorem (f)):**
- **Semiring localization (verify — likely the biggest gap).** Mathlib's `Localization` / `IsLocalization` / `OreLocalization` machinery is built for `CommMonoid`/`CommRing`. For **`CommSemiring`** away-localization at an element, check `Localization.Away` / `IsLocalization.Away` — these are stated for `CommSemiring`? `IsLocalization` is defined for `CommSemiring M` actually (Mathlib's `IsLocalization` takes a `Submonoid` of a `CommSemiring`). **Verify `IsLocalization.Away (e) (G R)`** is expressible. If yes, `thm:idempotent-localization` can use `IsLocalization.atUnits` / the universal property. If the away-localization API is ring-only, fall back to: define `A[a⁻¹] := a • A` (sub-semiring) directly and *prove the universal property by hand* (any hom inverting `a` factors through `a•A`), stating the iso as `RingEquiv` to the principal sub-semiring. This is the recommended robust path — avoid depending on heavy localization API for semirings.
- `IsIdempotentElem` (`a*a=a`) — Mathlib has `IsIdempotentElem`.
- `cor:two-zero-localizations`: with `a=e`, `a•(G R) = {τ, e}`-ish; `a=τ` gives the zero semiring `Subsingleton`. Need `Subsingleton`/`Unique` instance for the zero semiring.
- `cor:fraction-comparison` `G(R)[(R∖0)⁻¹] ≃ G K`: needs `FractionField`, `IsFractionRing`, `IsDomain`, `Field K`. Heavier; can be stated and deferred.

**Phase 6 (idempotent probe, theorem (g)):**
- `AdjoinRoot`, `Polynomial.X`, `Polynomial.eval`, `AdjoinRoot.lift`.
- **CRT**: `Ideal.quotientInfRingEquivPiQuotient`, `Ideal.quotientMulEquivQuotientProd`, `Ideal.isCoprime_iff_...`; comaximality of `(X)` and `(X-1)` via `IsCoprime` (witness `(X) - (X-1) = 1`).
- `Polynomial.quotientSpanXSubCAlgEquiv` / evaluation iso `A[X]/(X - c) ≃ A` (**verify** exact name; there is `AdjoinRoot.quotMapOfEquiv`-style or `Ideal.quotientSpanSingleton`).
- `KaehlerDifferential` for `Ω¹_{C/A}=0` (defer).
- Finite-difference identity: `Polynomial.eval`, `Polynomial.taylor`, or direct induction on `Polynomial` via `Polynomial.induction_on`; the `f(x+qh)` identity uses `q²=q` reduction.

**Cross-cutting tactics/automation:**
- `decide` (finite `Bool`), `aesop`, `simp_all`, `cases … <;> …`, `ring`, `linear_combination`, `omega` (not needed here), `ext`.
- `RingHom.ext`, `RingEquiv.ext`, `Equiv.ext`, `Subsingleton.elim`.

---

## Key correctness pitfalls to flag for whoever implements this

1. **`0_{G R} = τ`, not `e`.** Wire `Zero (G R) := ⟨τ⟩`. `e = some 0` is a non-zero (in the semiring sense) interior element. Every `simp` lemma must respect this.
2. **`ofR` is not a `RingHom`** — it preserves `+`, `*`, `1` but sends `0_R ↦ e ≠ 0_{G R}`. Do not declare it `R →+* G R`. The universal-property inverse routes through `reflect ∘ ofR = id` and `hom_kills_e`.
3. **`B` must be the `or`-semiring, not the `xor`-ring `𝔽₂`.** `1 + 1 = 1` in `B`. This is what makes `χ` a hom and `G(R)[e⁻¹] = B` instead of collapsing.
4. **The universal property (theorem (c)) targets `CommRing A`, not `CommSemiring A`** — because `hom_kills_e` needs additive cancellation. State the typeclass accordingly. (Theorem (b), uniqueness of `χ` into `B`, is the *semiring* universal property and lives separately.)
5. **`e` is additively idempotent (`e+e=e`)** — this single fact drives `hom_kills_e`, `G(R)[e⁻¹]=B`, the derivation-kills-`e` result, and the absolute-halo characterization. Prove it as an early reusable lemma.
6. **Semiring localization API may be ring-only** — do not assume `Localization.Away` works out of the box for `CommSemiring`; the robust path for theorem (f) is the hand-rolled `a•A` sub-semiring + universal property.

No files were written and nothing was executed, per instructions. The above is the complete deliverable: representation choice (`Option R` wrapped in a `structure`, with the `R×Bool` subtype kept as the iso target), ordered roadmap (Phases 0–6 covering core results (a)–(g) and Intro-Result-1, with spectral structure flagged out-of-scope), draft Lean source for the carrier, `CommSemiring` instance, `χ`/uniqueness, `reflect`/universal property, fixed locus, and idempotent probe, plus the per-step Mathlib API list with the verify-flags on the three riskiest dependencies (`Bool` `or`-semiring, semiring away-localization, CRT names).
