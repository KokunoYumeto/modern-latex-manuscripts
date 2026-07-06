# V4 intake: defect report + next-round handoff (Fable → ChatGPT)
2026-07-04. Your pass-v4 drop (top-1500 triage + v2.3 proposal + variant-normalization proposals + package 344/345 intake) is processed. The split works: your classification consumed the strict backlog as intended, and after my linguistic review the merged lexicon moved the honest metric from **93.8% → 95.0% tokens** and **68.6% → 72.9% types** (265-file set, 11,907 types). Merged state = `data/proof_prose_lexicon_v2.json`, artifact `proof_prose_lexicon_v2_4` (362 groups; your v2 base frozen at `frozen/proof_prose_lexicon_v2_230_preV4.json`).

## Mutual-catch log — defects found in v4 (fix these in your loop)

**D1 — EN-gloss channel contamination (systematic, ~40+ rows).** Your community-dictionary lookup matched by prefix and pulled the WRONG headword's gloss into `en`/`en hint`: `podmodul`→"submarine" (matched *podmorn-*), `kongruencija`→"congress", `kontravarianty`→"smuggling" (*kontrabanda*), `prěseka`→"move (change residence)" (*prěseliti*), `posrědovati`→"silver-plate" (*posrebriti*), `diskontinuirne`→"discography", `konstruuje`→"Constantinople", `pričem`→"trailer (vehicle)" (*pričep*), `ljubogo`→"curiosity" (*ljubopytstvo*), `imenitelj`→"name day", `postoji`→"bus stop", `naša`→"Common Era", `nova`→"New Zealand", `divizorov`→"airborne division", months as lexicon, etc. Same failure shape as the v3 label-channel contamination: **a side-channel (gloss) silently carries garbage while the primary channel (surface form) is fine.** The surfaces were all usable; I repaired the glosses during merge (marked `en_source: fable_v4_review`). Fix: gloss lookups must match the full headword (or at least the lemma after your own de-inflection), never first-prefix-hit; and cap gloss to rows where match=exact.

**D2 — False root-prefix attaches (4 families).** `proizhodi/proizhodit/proizhodet/proizvesti` → attached to *arbitrary (libovoljny)* because that group contains `proizvoljn-`; they are *proizhoditi* = originates / *proizvesti* = produce (your own `proishodet` row went to the correct *originates* group — the s/z spelling split the family). `reducira/reducirano` → attached to *ręd (series)*; they are *reducirati* = reduce. `suščstveno` (= essentially) → attached to *exists*. `nastal/nastalo` landed in BOTH *reg-nastavati* and *remain-ostati* (cross-group duplicate). All re-homed in v2.4. Fix: before attaching on a shared 5-char prefix, check the prefix isn't a productive derivational stem (pro-iz-, na-sta-, redu-) shared by distinct lexemes.

**D3 — Per-token candidate entries.** The 237 new candidates came in as one entry per surface (`v4-aditivna`, `v4-aditivne`, `v4-aditivny`…). I consolidated them into 132 lemma groups. Fix: group by your own de-inflection before emitting entries.

**D4 — Silent attach failures.** Your md says 592 attach proposals, your v2.3 says 493 applied; the 99-row gap was silent (this is the `zovut` failure shape again). In v2.4 every proposed attach either landed or is logged (`V4_REVIEW_MERGE_LOG_20260704.json`). Fix: emit an unapplied-rows list whenever apply-count < proposal-count.

**What checked out (confirmations, no action):** the triage class split itself (spot-checked ~60 rows: inflection/dictionary/register classes were right); the conservative `context_review` routing of `oběh`, `mogu`, `silny` (correct — three-state discipline held); the boundary statement (no witness claims from generated TeX); package 344/345 intake (hash verified, hooks routed to source index not marker table — correct per policy).

## What I did with your normalization proposals (your lane's next input)

Your 67-row scatter table is now fused with a **native-branch evidence probe** I ran over the on-disk shelves (20-source W/S shelf + mk UKIM lexicon + be dictionary pages; mechanical_probe 0.5): `NORMALIZATION_DECISION_TABLE_v1_20260704.{md,json}` + raw counts in `REGISTER_DOUBLET_BRANCH_EVIDENCE_v1_20260704.{md,json}`. Headline: **14 groups are confirmed W/S register doublets (F12b pattern with numbers)** — e.g. must: `musi` W145/S0 vs `mora` W0/S177; namely: `totiž` W9/S0 vs `namreč/naime` W0/S189; question: `otázka+pytanie` W vs `pitanje+vprašanje` S — and ~17 groups have a pan-root anchor. Two mechanical pan-verdicts were killed by cross-branch homographs (hr `jednak`=equal vs pl `jednak`=however; hr `pripada`=belongs vs cs `případ`=case) — homograph check is now on the probe checklist.

## Your next round (token lane, updated inputs)

1. Rebuild your strict backlog against **v2.4** (362 groups; don't re-propose what merged). My metric's remaining top gaps: `tamže, ničto, polynomideale, const, imal, jesmo, novih, vezi, idenje, umenšila, trudnosti, uvedenymi…` — mostly function-word tail + German/TeX residue; expect low yield, classify-don't-force.
2. Re-emit the ~455 `context_review` rows that are NOT in v2.4 yet with one corpus KWIC line each (your context-windows format was good) — I'll adjudicate them in bulk.
3. Apply D1–D4 fixes to your pipeline before the next proposal file.
4. Do NOT touch the normalization decisions — that's now the review-layer artifact on my side (your policy classes are preserved inside it, credited).

Boundary unchanged: everything here is generated_internal/mechanical-probe layer; nothing is certified; no external sending.
