# Noether Romance Source-Canon French Batch 2 Live arXiv Verification - 2026-07-05

Draft/non-canonical source-canon sidecar. Not native reviewed. Not approved. No license-clearance claim. No gate promotion. No Git push from this lane.

## Scope

This pass screens eight unrepresented French-shelf arXiv/e-print candidates with live arXiv metadata and source-archive downloads. It separates promising French mathematical candidates from English/off-topic invariant false positives.

## Files and Hashes

- Raw arXiv API response: `outputs/NOETHER_ROMANCE_SOURCE_CANON_FRENCH_BATCH2_LIVE_ARXIV_API_20260705.xml`; SHA-256 `c8fe4b107f4b3179654bb62edaadb91589a99b8effd974607d0d8bd7f8aca931`.
- Live e-print download summary: `outputs/NOETHER_ROMANCE_SOURCE_CANON_FRENCH_BATCH2_LIVE_ARXIV_EPRINT_DOWNLOADS_20260705.csv`; SHA-256 `6ae24ab41cec2edb303f923259f547024a6302288379e154fa004cdda5f47f26`.
- Combined French batch 2 verification table: `outputs/NOETHER_ROMANCE_SOURCE_CANON_FRENCH_BATCH2_LIVE_ARXIV_VERIFICATION_20260705.csv`; SHA-256 `43e29cba76201a213edb9807559fb02038df4c9db446bc9dbe736901c3f6dbdd`.
- Live e-print source archives were downloaded under `outputs/source_canon_witness_downloads/candidate_live_arxiv_french_batch2_20260705/` for hashing/provenance only.

## Results

| Local ID | Title | Category | Topic hits | Hash match | Action | Gap/Relevance note |
| --- | --- | --- | --- | --- | --- | --- |
| [1205.6530v1](http://arxiv.org/abs/1205.6530v1) | Shift-invariant spaces on SI/Z Lie groups | math.FA | invariant | `true` | english_shift_invariant_false_positive_not_promoted | English title/abstract; local hit is shift-invariant/functional-analysis language, not French target-language invariant-theory evidence. |
| [1305.1672v1](http://arxiv.org/abs/1305.1672v1) | Kervaire invariants and selfcoincidences | math.AT | invariant | `true` | english_topological_invariant_false_positive_not_promoted | English title/abstract; invariant term is topological Kervaire-invariant context, not French target-language Noether/invariant-theory source support. |
| [1405.2056v2](http://arxiv.org/abs/1405.2056v2) | Théorèmes de dualité pour les corps de fonctions sur des corps locaux supérieurs et applications arithmétiques | math.AG | Noether; Hilbert | `true` | adjacent_french_noether_hilbert_candidate_not_promoted | French title and local Noether/Hilbert context; adjacent higher-local-field duality source, not a direct invariant-theory witness. |
| [1605.01289v1](http://arxiv.org/abs/1605.01289v1) | Dualité et principe local-global sur des corps locaux de dimension 2 | math.AG | Noether; Hilbert; corps | `true` | adjacent_french_noether_field_candidate_not_promoted | French title and local Noether/Hilbert/corps context; strong field/Noetherian register but adjacent AG/NT domain. |
| [1801.01463v2](http://arxiv.org/abs/1801.01463v2) | L'espace adélique d'un tore sur un corps de fonctions | math.AG | Noether; Hilbert | `true` | adjacent_french_noether_hilbert_candidate_not_promoted | French title and local Brauer-Hasse-Noether/Hilbert context; adjacent torus/function-field source. |
| [2112.07476v2](http://arxiv.org/abs/2112.07476v2) | Invariant integrals on coideals and their Drinfeld doubles | math.QA | invariant | `true` | english_invariant_source_not_french_target_not_promoted | English title/abstract despite local French-shelf invariant hit; source may be math.QA relevant but is not a French target-language witness without deeper evidence. |
| [math_0107137v2](http://arxiv.org/abs/math/0107137v2) | Caracteres sur l'algebre de diagrammes trivalents Lambda | math.GT | invariant; module | `true` | french_invariant_module_candidate_not_promoted | French title and local invariant/module context; strong target-language candidate for invariant-module register, but still not main-table promoted without steward review. |
| [math_0303168v2](http://arxiv.org/abs/math/0303168v2) | Surfaces de del Pezzo sans point rationnel sur un corps de dimension cohomologique un | math.NT | Noether; Hilbert | `true` | adjacent_french_math_candidate_not_promoted | French title and local Noether/Hilbert context; algebraic-geometry/number-theory adjacent rather than direct Noether algebra source. |

## Summary Counts

- Rows screened: 8.
- Live e-print HTTP 200 rows: 8.
- Source-archive payloads from arXiv e-print: 8.
- Local/live SHA-256 matches: 8.
- Blank arXiv API license fields: 8.

## Explicit Non-Promotion Notes

- `math_0107137v2` is the strongest new French candidate in this batch for invariant/module register, but it remains candidate-only pending steward review.
- `1605.01289v1`, `1405.2056v2`, `1801.01463v2`, and `math_0303168v2` are French mathematical adjacent candidates with Noether/Hilbert/corps context, not direct main-table promotions.
- `1205.6530v1`, `1305.1672v1`, and `2112.07476v2` are English/off-topic or not French target-language support despite local invariant hits.
- The arXiv API license field was blank for every row in this batch; access/source availability is recorded, but no license clearance is claimed.

## Non-Claim Boundary

No translation expansion, glossary expansion, term promotion, reviewer-packet population, native-review claim, canonical approval, license-clearance claim, gate promotion, Git staging, Git commit, or Git push occurred.
