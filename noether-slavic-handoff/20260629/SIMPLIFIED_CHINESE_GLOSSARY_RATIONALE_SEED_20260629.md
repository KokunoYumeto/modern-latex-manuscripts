# Simplified Chinese glossary/rationale seed - 2026-06-29

This is a terminology seed for the Simplified Chinese Noether lane. It is derived from `SIMPLIFIED_CHINESE_TERM_ANCHOR_SEED_20260629.json`, which records only term counts and page anchors from local PDF text extraction. No source passages or PDFs are redistributed here.

## Authority Boundary

- This file is evidence for glossary work, not canonical approval.
- Single-character terms are useful but noisy; compound terms and page inspection should carry more weight.
- Mathematics-register and physics-register evidence are separate. PKU physics group-theory notes are Noether-adjacent but should not override algebra-course convention.
- The ECNU abstract-algebra PDF is a source witness, but current text extraction did not produce reliable term hits; manual page inspection is still needed.
- Native/external review is still required before canonical release language.

## Extraction Coverage

| Source | Pages | Nonempty Text Pages | Term Hits | Notes |
| --- | ---: | ---: | ---: | --- |
| SJTU syllabus | 8 | 8 | 20 | ok |
| ECNU abstract algebra | 127 | 127 | 0 | manual inspection needed; text extraction yielded no term hits |
| ECNU commutative algebra | 164 | 164 | 22 | ok |
| Representation notes | 75 | 75 | 20 | ok |
| PKU physics group theory | 402 | 400 | 19 | ok |
| Finite-group representation notes | 11 | 11 | 15 | ok |

## Term Anchors

| Term | Working English Gloss | Evidence Category | Total Count | Source/Page Anchors | Rationale Status |
| --- | --- | --- | ---: | --- | --- |
| `群` | group | algebra_core | 3280 | SJTU syllabus pp. 1,2,3,4,5,6; ECNU commutative algebra pp. 6,78,79,148,150,151; Representation notes pp. 1,2,3,4,5,6; PKU physics group theory pp. 1,2,3,4,5,6 | weak/noisy count; require compound/context support |
| `环` | ring | algebra_core | 375 | SJTU syllabus pp. 1,2,3,4,5,7; ECNU commutative algebra pp. 3,4,5,8,9,10; Representation notes pp. 24,26,29,33,38,49; PKU physics group theory pp. 4,10,31,32,33,40 | weak/noisy count; require compound/context support |
| `基定理` | basis theorem | commutative_algebra | 6 | ECNU commutative algebra pp. 3,7,9,163 | candidate; inspect pages before promotion |
| `局部化` | localization | commutative_algebra | 4 | ECNU commutative algebra pp. 4,46,61,62 | candidate; inspect pages before promotion |
| `近世代数` | modern algebra | course_scope | 12 | SJTU syllabus pp. 1,8; ECNU commutative algebra pp. 9,16; PKU physics group theory pp. 4,10 | candidate; inspect pages before promotion |
| `抽象代数` | abstract algebra | course_scope | 11 | SJTU syllabus pp. 1; Representation notes pp. 2,4; PKU physics group theory pp. 11; Finite-group representation notes pp. 1 | candidate; inspect pages before promotion |
| `域` | field | field_theory | 199 | SJTU syllabus pp. 1,3,4,5,6,7; ECNU commutative algebra pp. 3,4,5,8,9,11; Representation notes pp. 2,5,8,9,11,13; PKU physics group theory pp. 4,14,17,19,63,64 | weak/noisy count; require compound/context support |
| `除环` | division ring | field_theory | 2 | SJTU syllabus pp. 4 | candidate; inspect pages before promotion |
| `有限维` | finite-dimensional | finiteness | 48 | ECNU commutative algebra pp. 33,110; Representation notes pp. 3,9,10,11,18,34; PKU physics group theory pp. 83,92,94; Finite-group representation notes pp. 2 | candidate; inspect pages before promotion |
| `有限生成` | finitely generated | finiteness | 45 | SJTU syllabus pp. 1,3,4,7; ECNU commutative algebra pp. 4,9,10,11,30,33 | candidate; inspect pages before promotion |
| `模` | module | module_theory | 82 | SJTU syllabus pp. 1; ECNU commutative algebra pp. 4,40,41,42,45,46; Representation notes pp. 3,9,18,38,66,68; PKU physics group theory pp. 10,18,196,198,212,234 | weak/noisy count; require compound/context support |
| `张量积` | tensor product | module_theory | 29 | Representation notes pp. 10,11,35,36,45,59; Finite-group representation notes pp. 6 | candidate; inspect pages before promotion |
| `模同态` | module homomorphism | module_theory | 5 | ECNU commutative algebra pp. 46,47,49 | candidate; inspect pages before promotion |
| `子模` | submodule | module_theory | 2 | ECNU commutative algebra pp. 45 | candidate; inspect pages before promotion |
| `右模` | right module | module_theory | 1 | Representation notes pp. 38 | candidate; inspect pages before promotion |
| `同构` | isomorphism | morphism | 257 | SJTU syllabus pp. 3,4,5; ECNU commutative algebra pp. 39,48,61,66,68,79; Representation notes pp. 9,10,18,22,23,28; PKU physics group theory pp. 23,40,41,43,44,45 | candidate; inspect pages before promotion |
| `同态` | homomorphism | morphism | 206 | SJTU syllabus pp. 3,4; ECNU commutative algebra pp. 4,5,10,36,37,42; Representation notes pp. 9,10,14,17,18,23; PKU physics group theory pp. 23,40,42,43,44,45 | candidate; inspect pages before promotion |
| `自同构` | automorphism | morphism | 79 | SJTU syllabus pp. 3; ECNU commutative algebra pp. 79,164; Representation notes pp. 35,36,37,59; PKU physics group theory pp. 46,47,48,56,57,58 | candidate; inspect pages before promotion |
| `自同态` | endomorphism | morphism | 4 | SJTU syllabus pp. 4; Representation notes pp. 50,58 | candidate; inspect pages before promotion |
| `Noether` | Noether/Noetherian | noetherian | 91 | ECNU commutative algebra pp. 3,4,5,6,9,10; PKU physics group theory pp. 4,236,356 | Noetherian register unresolved; compare transliteration and functional phrasing before promotion |
| `诺特` | Noether/Noetherian | noetherian | 4 | PKU physics group theory pp. 4,16,17 | Noetherian register unresolved; compare transliteration and functional phrasing before promotion |
| `表示` | representation | representation_theory | 1780 | SJTU syllabus pp. 1,8; ECNU commutative algebra pp. 5,8,27,35,36,43; Representation notes pp. 1,2,3,4,5,6; PKU physics group theory pp. 2,6,7,8,9,23 | representation-register candidate; separate algebra vs physics context |
| `不可约表示` | irreducible representation | representation_theory | 398 | Representation notes pp. 3,10,11,12,13,14; PKU physics group theory pp. 8,23,24,25,69,73; Finite-group representation notes pp. 2,3,4 | representation-register candidate; separate algebra vs physics context |
| `特征标` | character | representation_theory | 282 | Representation notes pp. 3,8,12,13,14,16; PKU physics group theory pp. 23,25,74,84,91,109; Finite-group representation notes pp. 1,4,5,6,7,8 | representation-register candidate; separate algebra vs physics context |
| `群代数` | group algebra | representation_theory | 73 | Representation notes pp. 3,19,34,37; PKU physics group theory pp. 23,84,85,86,88,90; Finite-group representation notes pp. 3,4 | representation-register candidate; separate algebra vs physics context |
| `表示论` | representation theory | representation_theory | 56 | SJTU syllabus pp. 1,8; Representation notes pp. 1,2,5,6,9,10; PKU physics group theory pp. 2,63,80,84; Finite-group representation notes pp. 1,2,3,8,9 | representation-register candidate; separate algebra vs physics context |
| `完全可约` | completely reducible | representation_theory | 24 | Representation notes pp. 9,44; PKU physics group theory pp. 79,80,82,83,97,106; Finite-group representation notes pp. 2,5 | representation-register candidate; separate algebra vs physics context |
| `半单` | semisimple | representation_theory | 12 | Representation notes pp. 2,3,6,11,26,57 | representation-register candidate; separate algebra vs physics context |
| `理想` | ideal | ring_theory | 303 | SJTU syllabus pp. 4,5,7; ECNU commutative algebra pp. 3,4,8,9,10,12; Representation notes pp. 19; PKU physics group theory pp. 8,268 | candidate; inspect pages before promotion |
| `素理想` | prime ideal | ring_theory | 127 | SJTU syllabus pp. 4,5,7; ECNU commutative algebra pp. 4,21,22,23,24,25 | candidate; inspect pages before promotion |
| `极大理想` | maximal ideal | ring_theory | 61 | SJTU syllabus pp. 4,5; ECNU commutative algebra pp. 3,14,20,24,25,37 | candidate; inspect pages before promotion |
| `交换环` | commutative ring | ring_theory | 16 | SJTU syllabus pp. 4; ECNU commutative algebra pp. 9,10,16,17,29,37 | candidate; inspect pages before promotion |
| `主理想` | principal ideal | ring_theory | 13 | SJTU syllabus pp. 4,5; ECNU commutative algebra pp. 9,55,63,74,75,76 | candidate; inspect pages before promotion |
| `商环` | quotient ring | ring_theory | 10 | SJTU syllabus pp. 4; ECNU commutative algebra pp. 37,39,52,61,83,84 | candidate; inspect pages before promotion |

## Immediate Rationale Notes

- Noetherian terminology appears in the ECNU commutative-algebra witness, but the preferred Chinese form is not promoted by this automated pass. It needs page inspection and comparison against existing Chinese algebra convention.
- Representation terms are well anchored across representation-theory notes and physics group-theory notes; they should still be checked against pure algebra usage before entering the Paper 34 glossary.
- The module term family needs careful treatment because short forms can be noisy; stronger evidence should prefer compound/context anchors.
- The Chinese lane now has enough reachable evidence to begin a real glossary/rationale sidecar, but not enough for final canonical terminology without manual inspection and review.

Generated UTC: 2026-06-29T12:54:40.924028+00:00
