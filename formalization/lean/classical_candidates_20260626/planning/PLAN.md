I have enough grounding. The corpus exists under `Papors/OS/<author>`, the build env is `helix_frobenius-master` with Mathlib v4.31.0, `SplitZero.lean` is already GREEN there, and there's a `classical_lean_audit/STATUS.md` driving exactly this. The per-author map and verify verdicts in the prompt are the authoritative signal for what to build. Here is the launch plan.

---

# Classical-Mathematics Lean 4 Formalization — LAUNCH PLAN

Build env (confirmed on disk): `C:\Users\Floris\Downloads\helix_extract\helix_frobenius-master`, Mathlib v4.31.0 prebuilt oleans. Build with `lake env lean <file>` from that dir. Project STATUS already staged at `C:\Users\Floris\Documents\classical_lean_audit\STATUS.md`. New library lives there as `ClassicalAudit/`.

The gold standard from the verify pass is **genuine-gap-cheap**. There are exactly **8** of those. They are the entire near-term backlog. Everything else (genuine-gap-hard, already-in-mathlib) is deferred or skipped, with reasons in §4.

The 8 genuine-gap-cheap verdicts:
1. SL2-invariance of binary-quadratic discriminant `ac − b²` + it generates the invariant ring (Gordan)
2. Christoffel symbols of an explicit 2D fundamental form + symmetry (Bianchi)
3. Weber cubic with roots `f⁸, −f₁⁸, −f₂⁸` as an abstract polynomial identity (Weber)
4. `ConjClasses (Equiv.Perm (Fin n)) ≃ Nat.Partition n` packaged bijection (Frobenius)
5. Perfect-field criterion char p ⟺ Frobenius surjective (Steinitz)
6. Gauss/Sylvester generalization of Wilson's theorem (Sylvester)
7. Sylvester law of nullity `rank A + rank B − n ≤ rank(AB)` (Sylvester)
8. Sylvester catalecticant forward implication (Sylvester)
9. Number of primitive roots mod p `= φ(p−1)` (Jordan)
10. Order of affine line group `x ↦ ax+b` over 𝔽_p `= p(p−1)` (Jordan)

(That's 10 cheap items across the verdict list — Sylvester and Jordan each contribute multiple.)

---

## 1. RECOMMENDED BEACHHEAD

**Module: `ClassicalAudit/Jordan/AffineGroup.lean` — order of the affine group `x ↦ ax+b` over 𝔽_p is `p(p−1)`, and the companion primitive-roots count `φ(p−1)`.**

WHY this one first, over the others:
- **Cheapest of the cheap.** It is pure finite cardinality. `|{(a,b) : a ∈ (ZMod p)ˣ, b ∈ ZMod p}| = (p−1)·p`. No new structures, no covariant glue, no surface theory, no discriminant action to set up. It is `Fintype.card` of a product and `ZMod.card_units_eq_totient`. You can land it in well under a day and it forces you to wire the lake target, the import surface, and the naming convention end-to-end before anything mathematically load-bearing is at stake.
- **It de-risks the toolchain, not the math.** The single largest unknown in this project is not "is the theorem true" (the source has it explicitly) — it's "does my `import Mathlib` + `lake env lean` pipeline actually produce a green file in this Mathlib v4.31.0 tree, and do the lemma names I'm guessing exist." Jordan affine is the minimal test that exercises real Mathlib API (`ZMod`, units, `Fintype.card`, `totient`) without any risk that the *math* blocks you.
- **Well-transcribed and exact.** Traité §420/§50, structured digest present in corpus. The statement is unambiguous; there is no transcription-fidelity question to resolve mid-formalization.
- **It immediately produces a second free win.** Primitive-roots `= φ(p−1)` shares the same imports (`(ZMod p)ˣ` cyclic, count of generators of a cyclic group). Two named results, one module, one build cycle.

The Gordan discriminant target is the more *intellectually* satisfying beachhead (it's the flagship "explicit invariant theory" lane), but it requires standing up an SL2 action on binary forms first — that is the right *second* module, not the first. Do not open the project on infrastructure you have to invent. Open it on a cardinality count that proves the pipeline.

---

## 2. FIRST 10 CONCRETE TARGETS, RANKED

Ranked by `(cheapness × pipeline-value)` then by clustering (do same-author/same-API items adjacently). Each statement is a sketch — exact Mathlib lemma names are training-dated and the build is the real check (see §5).

### T1 — Jordan: order of the affine line group `= p(p−1)`  ⟨beachhead⟩
```lean
-- ClassicalAudit/Jordan/AffineGroup.lean
open scoped BigOperators
/-- The affine group of the line over 𝔽_p, as pairs (a,b) with a a unit. -/
abbrev Aff (p : ℕ) [Fact p.Prime] := (ZMod p)ˣ × ZMod p

theorem card_aff (p : ℕ) [Fact p.Prime] :
    Fintype.card (Aff p) = (p - 1) * p := by
  rw [Fintype.card_prod, ZMod.card_units_eq_totient, Nat.totient_prime, ZMod.card]
```
Builds on: `Fintype.card_prod`, `ZMod.card_units_eq_totient` (or `ZMod.card_units`), `Nat.totient_prime`, `ZMod.card`. **Risk: API-name only.**

### T2 — Jordan: number of primitive roots mod p `= φ(p−1)`
```lean
theorem card_primitiveRoots_mod (p : ℕ) [Fact p.Prime] :
    Fintype.card {g : (ZMod p)ˣ // ∀ x, x ∈ Subgroup.zpowers g} = Nat.totient (p - 1)
```
Cleaner phrasing: the number of generators of the cyclic group `(ZMod p)ˣ` is `φ(card)`, and `card = p−1`. Builds on: `instIsCyclic`/`ZMod.instIsCyclicUnits`, the count-of-generators lemma for cyclic groups (`IsCyclic.card_orderOf_eq_totient` family), `Nat.totient`. **Risk: whether Mathlib already states "number of generators = φ(n)" directly — check first; if present this is one rewrite.**

### T3 — Sylvester: Gauss/Sylvester generalization of Wilson
```lean
-- ClassicalAudit/Sylvester/WilsonGauss.lean
/-- Product of all units of ZMod N equals -1 if N has a primitive root, else +1. -/
theorem prod_units_zmod (N : ℕ) [NeZero N] :
    (∏ x : (ZMod N)ˣ, x) = if IsCyclic (ZMod N)ˣ then -1 else 1
```
Builds on: `Finset.prod_univ` over a finite abelian group, the involution `x ↦ x⁻¹` pairing argument, `ZMod.wilsons_lemma` as the prime base case to cross-check. **Risk: the if-then-else form may need the abelian-group "product = product of order-2 elements" lemma; the prime case is already in Mathlib so the skeleton is safe.**

### T4 — Steinitz: perfect field ⟺ Frobenius surjective (char p)
```lean
-- ClassicalAudit/Steinitz/PerfectField.lean
theorem perfect_iff_frobenius_surjective
    (K : Type*) [Field K] (p : ℕ) [Fact p.Prime] [CharP K p] :
    PerfectRing K p ↔ Function.Surjective (frobenius K p) := by
  exact ⟨fun _ => (frobenius K p).surjective_of_perfectRing ..., fun h => ...⟩
```
Builds on: `PerfectRing`, `frobenius`, `PerfectField`, `frobenius_surjective`/`PerfectRing.surjective` API. **Risk: this may already be the *definition* in Mathlib (`PerfectRing` is defined via bijectivity of frobenius). If so, the value is repackaging it as Steinitz's stated char-p criterion + the `iff` against the older `PerfectField` predicate — still a worthwhile named bridge, but confirm it isn't `Iff.rfl`.**

### T5 — Frobenius: `ConjClasses (Equiv.Perm (Fin n)) ≃ Nat.Partition n`
```lean
-- ClassicalAudit/Frobenius/ConjClassesPartition.lean
def conjClassesEquivPartition (n : ℕ) :
    ConjClasses (Equiv.Perm (Fin n)) ≃ Nat.Partition n
```
Builds on: `Equiv.Perm.isConj_iff_cycleType_eq`, `Equiv.Perm.cycleType` (a `Multiset ℕ` summing to n), `Nat.Partition`. Assembly: `cycleType` is the forward map; it lands in partitions of n because cycle lengths sum to n; injectivity/surjectivity from `isConj_iff_cycleType_eq` + the fact every partition is realized by some permutation. **Risk: the "every partition is realized" surjectivity direction needs a constructor (build a permutation with prescribed cycle type) — Mathlib may have `Equiv.Perm.cycleType_eq` existence; if not, this is the one bit of real work. Still cheap.**

### T6 — Gordan: SL2-invariance of binary-quadratic discriminant + ring generation
```lean
-- ClassicalAudit/Gordan/SL2Action.lean   (sets up the action — reused by future Gordan targets)
-- ClassicalAudit/Gordan/QuadraticDiscriminant.lean
/-- The discriminant of a binary quadratic a x² + 2b xy + c y² is SL2-invariant. -/
theorem disc_SL2_invariant (g : SL(2, ℚ)) (a b c : ℚ) :
    disc (g • (a,b,c)) = disc (a,b,c)   -- disc = a*c - b^2
```
Plus the generation statement: every `SL(2,ℚ)`-invariant polynomial in `a,b,c` is a polynomial in `ac − b²`. Builds on: `Matrix.SpecialLinearGroup`, an explicit `MvPolynomial (Fin 3) ℚ` substitution for the action, `ring`/`decide` to discharge the invariance identity. **Risk: the invariance identity itself is `ring`-checkable once the action substitution is written out. This is the highest-VALUE cheap target (flagship invariant-theory content) but requires building the action layer — hence ranked after the zero-infrastructure counts. The verdict pinned it cheap; trust that, but build T1–T5 first so the action layer is the only new thing here.**

### T7 — Bianchi: Christoffel symbols of an explicit 2D form + symmetry
```lean
-- ClassicalAudit/Bianchi/Christoffel2D.lean
variable (E F G : ℝ → ℝ → ℝ)   -- first fundamental form coefficients, as functions of (u,v)
/-- Christoffel symbols of the 2nd kind, purely algebraic in E,F,G and their partials. -/
noncomputable def christoffel (k i j : Fin 2) : (ℝ → ℝ → ℝ) := ...
theorem christoffel_symm (k i j : Fin 2) :
    christoffel E F G k i j = christoffel E F G k j i
```
Builds on: `fderiv`/`deriv` for the partials, `Matrix` 2×2 inverse for the `[E F; F G]⁻¹` factor, explicit `Fin 2` case-split. The symmetry `Γᵏᵢⱼ = Γᵏⱼᵢ` is immediate from symmetry of the defining bracket in i,j. **Risk: the definition is the work; symmetry is a `fin_cases` + `ring`. No surface-embedding theory needed (verdict: cheap). This is the building block the later Bianchi-identity target needs — but that follow-on is genuine-gap-HARD, so stop here for now.**

### T8 — Sylvester: law of nullity `rank A + rank B − n ≤ rank(AB)`
```lean
-- ClassicalAudit/Sylvester/Nullity.lean
theorem rank_mul_ge {m n p : ℕ} {K : Type*} [Field K]
    (A : Matrix (Fin m) (Fin n) K) (B : Matrix (Fin n) (Fin p) K) :
    A.rank + B.rank - n ≤ (A * B).rank
```
Builds on: `Matrix.rank`, `Matrix.rank_mul_le` (the existing *upper* bound), rank-nullity (`Matrix.rank_add_rank_le` / `LinearMap.rank` machinery). The lower bound is the Frobenius/Sylvester inequality; Mathlib has the upper bound but the additive lower bound appears to be the gap. **Risk: needs `(A*B).rank ≥ ...` via dimension of intersection of kernel/image — moderate among the cheaps. Possibly Mathlib has `LinearMap.rank_comp` bounds to lift. Build-test early to see how much kernel-dimension API exists.**

### T9 — Weber: cubic with roots `f⁸, −f₁⁸, −f₂⁸` as an abstract polynomial identity
```lean
-- ClassicalAudit/Weber/CubicIdentity.lean
/-- For a,b,c with a^8 = b^8 + c^8 and a*b*c = √2:
    x³ − (a⁸b⁸ + a⁸c⁸ − b⁸c⁸)x − 16 has roots a⁸, −b⁸, −c⁸. -/
theorem weber_cubic_roots (a b c : ℝ)
    (h1 : a^8 = b^8 + c^8) (h2 : a*b*c = Real.sqrt 2) :
    (X^3 - C (a^8*b^8 + a^8*c^8 - b^8*c^8) * X - C 16 : ℝ[X])
      = (X - C (a^8)) * (X + C (b^8)) * (X + C (c^8))
```
Builds on: `Polynomial`, Vieta via direct `ring`/`ring_nf` expansion using `h1`, `h2` (note `(abc)² = 2` ⇒ `a⁸b⁸c⁸ = 16`). Pure algebra; the Weber f-functions themselves are *not* defined — but the verdict's trick is to state it as an abstract identity in `a,b,c`, sidestepping the missing f-functions entirely. **Risk: lowest math risk of all (it's `ring` after substituting the two hypotheses) — ranked lower only because Weber is a single isolated win with no cluster around it (the real f-function syzygy is genuine-gap-hard).**

### T10 — Sylvester: catalecticant forward implication
```lean
-- ClassicalAudit/Sylvester/Catalecticant.lean
/-- If a binary form of degree 2n is a sum of n powers of linear forms,
    its Hankel catalecticant det (a_{i+j}) vanishes. -/
theorem catalecticant_eq_zero_of_sum_of_powers {n : ℕ}
    (coeffs : Fin (2*n+1) → ℚ)
    (h : IsSumOfNPowers n coeffs) :
    (Matrix.of fun i j : Fin (n+1) => coeffs ⟨i+j, ...⟩).det = 0
```
Builds on: `Matrix.det`, Hankel matrix construction, the rank argument (a sum of n powers makes the `(n+1)×(n+1)` Hankel matrix rank ≤ n ⇒ det 0). **Risk: defining `IsSumOfNPowers` precisely and the rank-drop argument is the moderate part; the full apolarity iff is hard (skip), but the forward determinant-vanishing is self-contained. Ranked last among cheaps because it carries the most definitional setup.**

---

## 3. PROJECT STRUCTURE (Mathlib-PR-aligned)

Stand it up as a proper lake project (the current `SplitZero.lean` just does `import Mathlib` loose — fix that). Mirror Mathlib's directory-as-namespace convention so individual files can be lifted into a PR with minimal churn.

```
classical_lean_audit/
├─ lakefile.lean                  -- require mathlib @ v4.31.0 (match helix_frobenius tree)
├─ lean-toolchain                 -- copy from helix_frobenius-master exactly
├─ STATUS.md                      -- already exists; keep progress here, not chat
├─ ClassicalAudit.lean            -- root: imports every module (the `import`-aggregator)
└─ ClassicalAudit/
   ├─ Jordan/
   │   ├─ AffineGroup.lean        -- T1, T2  ⟨beachhead⟩
   ├─ Sylvester/
   │   ├─ WilsonGauss.lean        -- T3
   │   ├─ Nullity.lean            -- T8
   │   └─ Catalecticant.lean      -- T10
   ├─ Steinitz/
   │   └─ PerfectField.lean       -- T4
   ├─ Frobenius/
   │   └─ ConjClassesPartition.lean -- T5
   ├─ Gordan/
   │   ├─ SL2Action.lean          -- shared action layer (binary forms, SL2 substitution)
   │   └─ QuadraticDiscriminant.lean -- T6
   ├─ Bianchi/
   │   └─ Christoffel2D.lean       -- T7
   └─ Weber/
       └─ CubicIdentity.lean       -- T9
```

Conventions, enforced from file 1:
- **Standard Mathlib naming.** `card_aff`, `rank_mul_ge`, `conjClassesEquivPartition` — lowerCamel for defs, snake-ish theorem names matching Mathlib's `noun_verb_noun` style. No project-specific prefixes on the *names*; the namespace carries provenance.
- **One namespace per author** (`namespace ClassicalAudit.Jordan`), so upstreaming a result means moving the lemma to its true Mathlib home (`Mathlib/GroupTheory/...`) and deleting the namespace wrapper — nothing else changes.
- **Each green module ends with `#print axioms <mainThm>`** and must show only `propext, Classical.choice, Quot.sound`. Anything else (a stray `sorryAx`, an unexpected axiom) is a red flag. STATUS records the axiom line per module.
- **A `-- SOURCE:` docstring on every main theorem** citing the exact transcription (`Jordan, Traité §420`, file path). This is what makes it Zenodo-publishable as a *recovery* of the classical text, not just a Lean exercise.
- **Don't `import Mathlib` wholesale in leaf files** once you know the real imports — narrow imports make PR review tractable. (Keep `import Mathlib` only during initial exploration, then trim.)

---

## 4. WHAT TO SKIP, AND WHY

**Skip — already in Mathlib (no formalization value, the verdict confirmed it exists):**
- Noether: primary ideal ⟹ unique radical prime — `Ideal.IsPrimary.radical_isPrime` exists. Verdict: already-in-mathlib.
- Noether: Lasker–Noether existence of primary decomposition — Mathlib has it. Verdict: already-in-mathlib.
- Weber: quadratic reciprocity in Kronecker-symbol form — `legendreSym`/`jacobiSym.quadratic_reciprocity`. Verdict: already-in-mathlib. *(At most a 5-line notation-bridge lemma if you want Weber's exact packaging; not a target.)*
- Steinitz: exchange property for algebraic dependence — `AlgebraicIndependent` infra already gives it. Verdict: already-in-mathlib.
- Steinitz: additivity of transcendence degree in towers — Mathlib coverage present. Verdict: already-in-mathlib.
- Jordan: order of `GL(n,p)` — already packaged. Verdict: already-in-mathlib.

**Skip for now — genuine gap but HARD (needs infrastructure you don't want to build at launch):**
- Gordan: Hessian covariant, Jacobian/first transvectant — both verdict genuine-gap-**hard**. They need the full covariant/transvectant packaging, not just the 2×2 determinant. The *discriminant* target (T6) is the cheap entry to the same SL2 lane; do that first, and the Hessian/Jacobian become reachable once `SL2Action.lean` is mature. Revisit after T6.
- Gordan/Noether: finite generation of the invariant ring (`Algebra.FiniteType`) — genuine-gap-hard. High value (it's a real Mathlib gap) but the Noether symmetric-function proof is a substantial build. Defer to phase 2.
- Bianchi: Euler normal-curvature formula and the **second Bianchi identity** — both genuine-gap-hard. The Bianchi identity is the project's headline "buried by abstraction" prize, but it sits on top of the curvature tensor built from Christoffel symbols. Land T7 (Christoffel block) first; the identity is the phase-2 reward once that's solid.
- Weber: f-function syzygy `f⁸ = f₁⁸ + f₂⁸`, `j = γ₂³` — genuine-gap-hard, needs Dedekind-eta quotients defined first. The abstract cubic T9 is the cheap shadow of this; take T9 now, defer the real syzygy.
- Frobenius: degree formula (Vandermonde/factorial) and character-degree-divides-order — both genuine-gap-hard. The degree formula needs the hook-length/representation scaffolding; divides-order needs central-character algebraic-integrality. Both are phase-2.
- Gauss: composition of forms, cyclotomic period polynomial, genus character — all require a binary-quadratic-form structure that **does not exist in Mathlib at all**. This is the biggest gap and the biggest prize, but it's a multi-module subproject, not a launch target. Build the BQF structure deliberately in phase 2; the Gordan discriminant work (T6) is the natural warm-up for "SL2 acting on forms" before tackling Gauss composition.
- Lie: cross-ratio/3-transitivity, inversion-conformality, non-commuting vector fields — not in the verify verdict list (no gold-cheap verdict issued), and they pull in `crossRatio`/`IsConformalMap`/`VectorField.lieBracket` glue. Reasonable later, but unranked here because they weren't through the skeptical pass.

**Skip — not-yet-precise:** anything where the transcription is "SCANS + OCR ONLY" rather than clean LaTeX. Per the author map, **Gordan's actual target text ("Vorlesungen…") is scans+OCR only** — so when you build T6, state it from the *mathematical content* (the discriminant identity is standard and unambiguous) rather than trying to track a specific OCR'd page. Don't formalize against un-cleaned OCR.

---

## 5. THE HONEST RISK + DE-RISK ORDER

The single material risk: **"what's in Mathlib" was assessed from training-dated knowledge.** The verdicts above are educated guesses, not build results. v4.31.0 may already contain a target (collapsing it to `exact`/`Iff.rfl`), or may *lack* a lemma I assumed exists (turning a "cheap" into real work). The only real check is `lake env lean` in the helix tree.

**De-risk in this exact order — these three first, before any deep work:**

1. **T1 (Jordan affine count) — build it first, today.** It is the toolchain smoke test. If T1 doesn't go green, the problem is the build env / import surface / lemma names, *not* the math — fix that before touching anything else. This is why it's the beachhead.

2. **T4 (Steinitz perfect-field) — build second, as the "is it already trivial" probe.** `PerfectRing` in modern Mathlib is *defined* via frobenius bijectivity, so T4 may be `Iff.rfl` or a one-liner. Building it second tells you immediately how aggressively current Mathlib has already absorbed these criteria — which recalibrates your estimate of every other target. If T4 is trivial, expect T2 and parts of T5 to also be lighter than budgeted.

3. **T8 (Sylvester nullity) — build third, as the "is the cheap actually moderate" probe.** This is the cheap target most likely to be harder than the verdict says, because the rank *lower* bound needs kernel-dimension API that may or may not be ergonomic in v4.31.0. Hitting this early tells you whether the rank/linear-algebra cheaps (T8, T10) are truly cheap or are secretly phase-1.5.

After those three green, proceed T2 → T3 → T5 → T9 → T7 → T6 → T10 in that order. Run continuously, track in `STATUS.md`, `#print axioms` each green module. Re-classify any target the build contradicts (mark it already-in-mathlib or bump it to hard) and move on — do not fight a target that the real Mathlib has already solved or that needs infrastructure.

---

**Key paths (all absolute):**
- Library root to create: `C:\Users\Floris\Documents\classical_lean_audit\` (STATUS.md already there)
- Build env: `C:\Users\Floris\Downloads\helix_extract\helix_frobenius-master` (Mathlib v4.31.0 oleans; copy its `lean-toolchain`)
- Reference green file / import-pattern model: `C:\Users\Floris\Documents\arxiv_latex\_lean\SplitZero.lean`
- Source corpus: `C:\Users\Floris\Documents\Papors\OS\<author>\` (Sylvester, Steinitz, Frobenius, Gauss confirmed present)
