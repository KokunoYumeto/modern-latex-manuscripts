# Japanese glossary/rationale seed - 2026-06-29

This is a terminology seed for the Japanese Noether lane. It is derived from `JAPANESE_TERM_ANCHOR_SEED_20260629.json`, which records only term counts and page anchors from local PDF text extraction. No source passages or PDFs are redistributed here.

## Authority Boundary

- This file is evidence for glossary work, not canonical approval.
- Single-character terms such as ring/field anchors are useful but noisy; compound terms and page inspection should carry more weight.
- Ring/module, representation-theory, and algebraic-number-theory registers are separate evidence buckets.
- Roman `Noether` appears in the extracted witnesses; Japanese-form choices such as transliteration versus adjectival phrasing need manual inspection.
- Native/external review remains required before canonical release language.

## Extraction Coverage

| Source | Pages | Nonempty Text Pages | Term Hits | Notes |
| --- | ---: | ---: | ---: | --- |
| Hiroshima rings/modules | 43 | 43 | 32 | ok |
| UTokyo representation theory | 83 | 81 | 25 | representation-theory register; not a ring/module baseline by itself |
| TUS module theory | 56 | 56 | 19 | ok |
| Joetsu algebraic number theory | 60 | 60 | 19 | number-theory register; useful for ideals/rings of integers |

## Term Anchors

| Term | Working English Gloss | Evidence Category | Total Count | Source/Page Anchors | Rationale Status |
| --- | --- | --- | ---: | --- | --- |
| `代数` | algebra | algebra_core | 107 | Hiroshima rings/modules pp. 1,3,4,7,9,10; UTokyo representation theory pp. 3,5,19,22,23,24; TUS module theory pp. 1,3,7,10,13,15; Joetsu algebraic number theory pp. 1,2,11,13,14,15 | candidate; inspect pages before promotion |
| `局所化` | localization | commutative_algebra | 4 | UTokyo representation theory pp. 25,27 | candidate; inspect pages before promotion |
| `基底定理` | basis theorem | commutative_algebra | 1 | Hiroshima rings/modules pp. 34 | candidate; inspect pages before promotion |
| `体` | field | field_theory | 226 | Hiroshima rings/modules pp. 3,4,6,7,8,10; UTokyo representation theory pp. 3,5,7,11,12,18; TUS module theory pp. 3,5,8,11,12,13; Joetsu algebraic number theory pp. 2,3,4,5,7,8 | weak/noisy count; require compound/context support |
| `有限生成` | finitely generated | finiteness | 76 | Hiroshima rings/modules pp. 2,5,7,8,12,13; UTokyo representation theory pp. 23,25,27,28,29,44; TUS module theory pp. 3,6,23,24,25,27; Joetsu algebraic number theory pp. 2,25 | candidate; inspect pages before promotion |
| `有限次元` | finite-dimensional | finiteness | 19 | Hiroshima rings/modules pp. 7,38,39,43; UTokyo representation theory pp. 18,22,23,28,39,55; TUS module theory pp. 3,30; Joetsu algebraic number theory pp. 14 | candidate; inspect pages before promotion |
| `Artin` | Artin/Artinian | finiteness | 16 | Hiroshima rings/modules pp. 2,38,39,40,43 | candidate; inspect pages before promotion |
| `アルティン` | Artinian/Artin | finiteness | 5 | Hiroshima rings/modules pp. 2,36,38,40,42 | candidate; inspect pages before promotion |
| `加群` | module | module_theory | 887 | Hiroshima rings/modules pp. 1,2,3,4,5,6; UTokyo representation theory pp. 3,5,12,13,15,16; TUS module theory pp. 1,2,3,4,5,6; Joetsu algebraic number theory pp. 2,25,26,27,28,29 | strong technical-register candidate; still page-inspect before promotion |
| `部分加群` | submodule | module_theory | 91 | Hiroshima rings/modules pp. 5,6,14,15,24,25; UTokyo representation theory pp. 13,15,16,17,26,29; TUS module theory pp. 6,7,12,23,24,25; Joetsu algebraic number theory pp. 26,27,28,29 | strong technical-register candidate; still page-inspect before promotion |
| `テンソル積` | tensor product | module_theory | 36 | Hiroshima rings/modules pp. 2,18,19,20,21,22; UTokyo representation theory pp. 37; TUS module theory pp. 2,3,40,41,42 | strong technical-register candidate; still page-inspect before promotion |
| `自由加群` | free module | module_theory | 36 | Hiroshima rings/modules pp. 2,6,7,13,20,26; TUS module theory pp. 2,8,10,11,12,15 | strong technical-register candidate; still page-inspect before promotion |
| `単純加群` | simple module | module_theory | 1 | Hiroshima rings/modules pp. 43 | strong technical-register candidate; still page-inspect before promotion |
| `同型` | isomorphism | morphism | 212 | Hiroshima rings/modules pp. 3,4,6,8,9,14; UTokyo representation theory pp. 9,13,15,19,21,22; TUS module theory pp. 3,5,7,12,15,16; Joetsu algebraic number theory pp. 15,17,19,23,25,27 | candidate; inspect pages before promotion |
| `準同型` | homomorphism | morphism | 135 | Hiroshima rings/modules pp. 3,4,6,8,15,16; UTokyo representation theory pp. 21,22,48,49,52,54; TUS module theory pp. 5,7,12,15,16,17; Joetsu algebraic number theory pp. 15,17,19,23,25,27 | candidate; inspect pages before promotion |
| `自己準同型` | endomorphism | morphism | 2 | Hiroshima rings/modules pp. 15,23 | candidate; inspect pages before promotion |
| `自己同型` | automorphism | morphism | 1 | UTokyo representation theory pp. 19 | candidate; inspect pages before promotion |
| `Noether` | Noether/Noetherian | noetherian | 70 | Hiroshima rings/modules pp. 2,32,33,34,35,38; UTokyo representation theory pp. 27 | Noetherian register unresolved; inspect source phrasing before promotion |
| `ネーター` | Noetherian/Noether | noetherian | 6 | Hiroshima rings/modules pp. 11; TUS module theory pp. 48; Joetsu algebraic number theory pp. 35 | Noetherian register unresolved; inspect source phrasing before promotion |
| `Noetherian` | Noetherian | noetherian | 3 | Hiroshima rings/modules pp. 33 | Noetherian register unresolved; inspect source phrasing before promotion |
| `ノルム` | norm | number_theory | 17 | UTokyo representation theory pp. 22; Joetsu algebraic number theory pp. 2,15,22,23,31,37 | number-theory candidate; use only where Paper 34 context needs this register |
| `整数環` | ring of integers | number_theory | 17 | TUS module theory pp. 17; Joetsu algebraic number theory pp. 2,7,13,15,24,29 | number-theory candidate; use only where Paper 34 context needs this register |
| `類数` | class number | number_theory | 6 | Joetsu algebraic number theory pp. 2,34,37 | number-theory candidate; use only where Paper 34 context needs this register |
| `素数の分解` | decomposition of primes | number_theory | 2 | Joetsu algebraic number theory pp. 2,51 | number-theory candidate; use only where Paper 34 context needs this register |
| `表現` | representation | representation_theory | 179 | Hiroshima rings/modules pp. 16,17,19,32,36,37; UTokyo representation theory pp. 1,3,5,7,8,9; TUS module theory pp. 15,16,17,25,29,30 | weak/noisy count; require compound/context support |
| `半単純` | semisimple | representation_theory | 35 | Hiroshima rings/modules pp. 2,32,36,37,38,40; UTokyo representation theory pp. 21,24,28,51 | representation-register candidate; separate from ring/module baseline |
| `既約表現` | irreducible representation | representation_theory | 14 | Hiroshima rings/modules pp. 38; UTokyo representation theory pp. 3,8,12,15,17,18 | representation-register candidate; separate from ring/module baseline |
| `完全可約` | completely reducible | representation_theory | 10 | Hiroshima rings/modules pp. 2,32,36,37,42 | representation-register candidate; separate from ring/module baseline |
| `表現論` | representation theory | representation_theory | 9 | Hiroshima rings/modules pp. 32,36; UTokyo representation theory pp. 3,51,52,82 | representation-register candidate; separate from ring/module baseline |
| `リー群` | Lie group | representation_theory | 7 | UTokyo representation theory pp. 1,3,82 | representation-register candidate; separate from ring/module baseline |
| `群環` | group ring/group algebra | representation_theory | 7 | Hiroshima rings/modules pp. 2,36; TUS module theory pp. 52 | representation-register candidate; separate from ring/module baseline |
| `Harish-Chandra` | Harish-Chandra | representation_theory | 6 | UTokyo representation theory pp. 3,12,13,56,82 | representation-register candidate; separate from ring/module baseline |
| `指標` | character | representation_theory | 3 | UTokyo representation theory pp. 30,52,56 | representation-register candidate; separate from ring/module baseline |
| `環` | ring | ring_theory | 364 | Hiroshima rings/modules pp. 1,2,3,4,5,6; UTokyo representation theory pp. 3,13,15,16,19,21; TUS module theory pp. 1,2,3,4,5,8; Joetsu algebraic number theory pp. 2,3,5,6,7,8 | weak/noisy count; require compound/context support |
| `イデアル` | ideal | ring_theory | 222 | Hiroshima rings/modules pp. 7,9,11,13,14,21; UTokyo representation theory pp. 21,22,23,24,25,26; TUS module theory pp. 5,6,8,11,12,17; Joetsu algebraic number theory pp. 2,3,4,5,6,8 | strong technical-register candidate; still page-inspect before promotion |
| `可換環` | commutative ring | ring_theory | 61 | Hiroshima rings/modules pp. 2,3,7,9,19,20; UTokyo representation theory pp. 3; TUS module theory pp. 4,5,10,11,12,13; Joetsu algebraic number theory pp. 7 | strong technical-register candidate; still page-inspect before promotion |
| `素イデアル` | prime ideal | ring_theory | 29 | Hiroshima rings/modules pp. 37; UTokyo representation theory pp. 25,26,28,29,46; Joetsu algebraic number theory pp. 9,34,35,39,40,41 | strong technical-register candidate; still page-inspect before promotion |
| `極大イデアル` | maximal ideal | ring_theory | 25 | Hiroshima rings/modules pp. 7,14,37,40,41,42; UTokyo representation theory pp. 27,29,30,46,58,70; TUS module theory pp. 11,12; Joetsu algebraic number theory pp. 40 | strong technical-register candidate; still page-inspect before promotion |
| `単項イデアル` | principal ideal | ring_theory | 13 | Hiroshima rings/modules pp. 9; TUS module theory pp. 17,18,56; Joetsu algebraic number theory pp. 8,9,34,37,38,48 | strong technical-register candidate; still page-inspect before promotion |
| `半単純環` | semisimple ring | ring_theory | 11 | Hiroshima rings/modules pp. 2,36,38,40,41,42 | strong technical-register candidate; still page-inspect before promotion |
| `商環` | quotient ring | ring_theory | 3 | Hiroshima rings/modules pp. 27,30 | strong technical-register candidate; still page-inspect before promotion |

## Immediate Rationale Notes

- Japanese has unusually strong direct evidence for module/ring terminology because two sources focus on rings and modules.
- `Noether` is strongly anchored in the Hiroshima ring/module source, but Japanese canonical treatment still needs page inspection and external review.
- Representation terms are supported by the Tokyo representation-theory source and also cross-appear in the rings/modules source, but these should remain a distinct register bucket.
- Number-theory terminology from the Joetsu source is valuable for ideals and rings of integers, but should not be overextended into representation-theory prose.
- The next useful step is a page-inspected glossary for high-value Japanese terms with accepted forms, alternatives, and review status fields.

Generated UTC: 2026-06-29T13:05:53.418222+00:00
