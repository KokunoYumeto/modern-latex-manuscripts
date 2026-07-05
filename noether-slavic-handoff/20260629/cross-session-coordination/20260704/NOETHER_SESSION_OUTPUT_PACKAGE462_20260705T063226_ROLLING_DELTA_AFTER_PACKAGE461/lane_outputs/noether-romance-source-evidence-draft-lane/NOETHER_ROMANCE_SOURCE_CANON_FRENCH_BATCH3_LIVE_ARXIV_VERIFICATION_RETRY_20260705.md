# Noether Romance Source-Canon French Batch 3 Live arXiv Verification Retry - 2026-07-05

Draft/non-canonical source-canon sidecar. Not native reviewed. Not approved. No license-clearance claim. No gate promotion. No Git push from this lane.

## Scope

This pass retries the nine French batch 3 rows previously blocked by arXiv HTTP `429`. The retry succeeded for live arXiv API metadata and live e-print source downloads. Rows remain candidate-only/not promoted.

## Files and Hashes

- Retry arXiv API response: `outputs/NOETHER_ROMANCE_SOURCE_CANON_FRENCH_BATCH3_LIVE_ARXIV_API_RETRY_20260705.xml`; SHA-256 `c42021723bdbba3f6ce6bdb68d77a36eabb554b2977f9e6cbac9ff8cd0a97ad4`.
- Retry e-print download summary: `outputs/NOETHER_ROMANCE_SOURCE_CANON_FRENCH_BATCH3_LIVE_ARXIV_EPRINT_DOWNLOADS_RETRY_20260705.csv`; SHA-256 `c36735382ca4f842fb32408cb94955e1f1282210572f13b599197456e2b659d3`.
- Combined retry verification table: `outputs/NOETHER_ROMANCE_SOURCE_CANON_FRENCH_BATCH3_LIVE_ARXIV_VERIFICATION_RETRY_20260705.csv`; SHA-256 `3a434ab734069743b957cd973f1785f4e2a76475b692dcf9e4d3eaa08b791330`.
- Live retry e-print source archives were downloaded under `outputs/source_canon_witness_downloads/candidate_live_arxiv_french_batch3_retry_20260705/` for hashing/provenance only.

## Results

| Local ID | Live title | Category | Hash match | Action | Note |
| --- | --- | --- | --- | --- | --- |
| [1104.1507v4](http://arxiv.org/abs/1104.1507v4) | Sur l'homologie des groupes unitaires à coefficients polynomiaux | math.KT | `true` | live_arxiv_verified_adjacent_french_candidate_not_promoted | Live arXiv metadata/e-print verified and local source hash matches; adjacent French mathematical candidate remains not promoted. |
| [1104.3350v3](http://arxiv.org/abs/1104.3350v3) | Cycles de codimension 2 et H^3 non ramifié pour les variétés sur les corps finis | math.AG | `true` | live_arxiv_verified_adjacent_french_candidate_not_promoted | Live arXiv metadata/e-print verified and local source hash matches; adjacent French mathematical candidate remains not promoted. |
| [1509.07817v1](http://arxiv.org/abs/1509.07817v1) | Variétés abéliennes sur les corps de fonctions de courbes sur des corps locaux supérieurs | math.AG | `true` | live_arxiv_verified_adjacent_french_candidate_not_promoted | Live arXiv metadata/e-print verified and local source hash matches; adjacent French mathematical candidate remains not promoted. |
| [1510.05382v1](http://arxiv.org/abs/1510.05382v1) | On the Bertrandias-Payan module in a p-extension -- capitulation kernel | math.NT | `true` | live_arxiv_verified_adjacent_french_candidate_not_promoted | Live arXiv metadata/e-print verified and local source hash matches; adjacent French mathematical candidate remains not promoted. |
| [1709.00597v2](http://arxiv.org/abs/1709.00597v2) | Troisième groupe de cohomologie non ramifiée d'un solide cubique sur un corps de fonctions d'une variable | math.AG | `true` | live_arxiv_verified_adjacent_french_candidate_not_promoted | Live arXiv metadata resolves prior weak local title parse; French mathematical source remains adjacent/candidate-only, not main-table promoted. |
| [1905.13138v3](http://arxiv.org/abs/1905.13138v3) | Generators, spanning sets and existence of twisted modules for a grading-restricted vertex (super)algebra | math.QA | `true` | live_arxiv_verified_english_shelf_mismatch_not_promoted | Live arXiv title/metadata confirm English source despite French-shelf placement; keep as shelf-mismatch, not a French target-language witness. |
| [2001.10515v4](http://arxiv.org/abs/2001.10515v4) | Sur la conjecture de Tate entière pour le produit d'une courbe et d'une surface $CH_{0}$-triviale sur un corps fini | math.AG | `true` | live_arxiv_verified_adjacent_french_candidate_not_promoted | Live arXiv metadata/e-print verified and local source hash matches; adjacent French mathematical candidate remains not promoted. |
| [2501.13300v2](http://arxiv.org/abs/2501.13300v2) | Arithmétique des schémas en groupes de Bruhat-Tits sur un anneau de Dedekind semi-local | math.AG | `true` | live_arxiv_verified_adjacent_french_candidate_not_promoted | Live arXiv metadata/e-print verified and local source hash matches; adjacent French mathematical candidate remains not promoted. |
| [2505.05443v1](http://arxiv.org/abs/2505.05443v1) | Dualité étale à la Poitou-Tate pour les tores sur des variétés définies sur un corps fini | math.NT | `true` | live_arxiv_verified_adjacent_french_noether_candidate_not_promoted | Live arXiv metadata plus local Noether/corps/anneau hits support adjacent French mathematical provenance; still not promoted without steward review. |

## Summary Counts

- Rows verified after retry: 9.
- Live e-print HTTP 200 rows: 9.
- Source-archive payload rows: 9.
- Local/live SHA-256 matches: 9.
- Blank arXiv API license fields: 9.
- Promotion-like actions: 0.

## Explicit Boundaries

- The prior HTTP `429` blocker is superseded for live metadata/source availability by this retry, but retained as history.
- `1905.13138v3` is confirmed as an English-title shelf mismatch and remains excluded as a French target-language witness.
- arXiv API license fields were blank for all nine retry rows, so no license clearance is claimed.
- No row is promoted into the main witness table by this retry.

## Non-Claim Boundary

No translation expansion, glossary expansion, term promotion, reviewer-packet population, native-review claim, canonical approval, license-clearance claim, gate promotion, Git staging, Git commit, or Git push occurred.
