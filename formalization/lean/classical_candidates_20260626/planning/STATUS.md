# Classical-Mathematics Lean Formalization — project STATUS

**Goal.** Recover the *explicit / computational* layer of 19th-century classical mathematics —
the part 20th-century abstraction buried — and formalize it in Lean 4, in **standard
Mathlib-aligned terms** (PR-able upstream, eventually Zenodo-published). Target results that are
**true + missing-from-Mathlib + cheap**. Emphasis on the coordinate-level constructions (exact
invariants, covariants, explicit forms), not the existence theorems Mathlib already has.

**Why it's feasible.** Floris is already transcribing these German scans to LaTeX. Pipeline:
*German scan → his LaTeX transcription → AI extracts an explicit computation with the source in
hand → Lean checks the normalized formal statement.* This is not certification of the archive,
the scan transcription, or the translation. The value is positive and independent: small useful
Lean/mathlib-style library candidates can be produced from historically important explicit
mathematics. Classical algebra needs no exotic Mathlib infrastructure, so it's the tractable
regime; and explicit computation is where Lean's `decide`/`norm_num`/reflection shine.

**Corpus (authors being mapped).** Gordan (invariant theory), Noether, Bianchi, Weber (Lehrbuch
der Algebra), Frobenius, Steinitz, Sylvester, Camille Jordan, Gauss (Disquisitiones), Lie/Klein
(transformation groups, Möbius/O(3,1) — the Apollonian lane). Sources under
`Papors\OS\<author>` and the transcription project `Papors\Chatnotes\CHat translates and clean`.

## Status
- **Scoping workflow `wqgkouo39` RUNNING** — one agent per author maps his transcription × Mathlib,
  extracts explicit results, classifies covered/gap/feasible, proposes Lean targets; then a
  skeptical verify pass; then a synthesized plan (beachhead + first 6–10 targets + module layout).
- **Lean build env:** `C:\Users\Floris\Downloads\helix_extract\helix_frobenius-master` (Mathlib
  v4.31.0 prebuilt, ~1.7GB oleans). Build a file with `lake env lean <file>` from that dir.
  `SplitZero.lean` already GREEN there (the split-zero core).

## Next (on workflow return)
1. Stand up `ClassicalAudit/` modules (per area), Mathlib-import, standard names.
2. Formalize the **beachhead** first; build-test to de-risk the Mathlib-coverage guesses
   (agents' Mathlib knowledge is training-dated — the Lean build is the real check).
3. Work targets continuously; track progress HERE, not chat. `#print axioms` each green module.
4. When a cluster is solid + tested + standard-aligned → package for Zenodo / propose upstream.

## Honest risks
- "What's in Mathlib" from agent knowledge is approximate; first action on any target is to try
  the import/lemma in Lean and see if it already exists.
- Explicit computations can be large to formalize; prefer the bounded ones first.

## Progress log
- 2026-06-25 — full scoping done (workflow wqgkouo39): 10 authors, 104 results, 10 verified
  genuine-cheap-gaps. Plan + targets in `PLAN.md`, cheap targets in `TARGETS_cheap.tsv`.
  Big-prize gap identified: **Gauss binary quadratic forms / composition / form class group is
  entirely absent from Mathlib** (phase-2 multi-module subproject).
- 2026-06-25 — **CORRECTION (Floris caught a false claim).** The scoping workflow searched only the
  `OS\` scan folders and I wrongly reported "Gordan invariant theory not transcribed." FALSE.
  AUTHORITATIVE INVENTORY = the published repo catalog, NOT filesystem search:
  `Papors\modern-latex-manuscripts-github\manifests\public-file-catalog.csv` (337KB) +
  `docs\browse-index.md` + `docs\by-author-and-work.md`. Real transcription is rich:
  Gordan *Vorlesungen über Invariantentheorie* Bd.1 p001-028 + Abelsche + geodesic (zenodo 20616260);
  Noether 43 papers (20412587); Weber Lehrbuch I+II thru §176 (20412153); Steinitz field theory
  1910 §1-24 + Bedingt I/II (20616988); Bianchi diff-geo Vol I (20615814); Frobenius characters
  (20673444); Gauss/Dedekind/Dirichlet/Cayley on classical shelf (20414787). RULE: source every Lean
  target from the actual transcribed `.tex` (repo `sources/` + source ZIPs) so it's a recovery of HIS
  text, and consult the catalog before claiming anything is/ isn't present.
- 2026-06-25 — **T1 GREEN + axiom-clean**: `ClassicalAudit.Jordan.card_aff` (Jordan Traité §420,
  affine line group over 𝔽_p has order p(p−1)). File: `helix_frobenius-master\AffineGroup.lean`.
  Axioms: [propext, Classical.choice, Quot.sound]. Toolchain de-risked end-to-end.
- IN PROGRESS: T2 (Jordan primitive-roots = φ(p−1)) + T4 (Steinitz perfect ⟺ Frobenius surjective).
  Then T8 (Sylvester nullity), T3/T5/T9/T7, and T6 (Gordan discriminant — needs the SL2-action layer).
