# Noether Romance Source-Canon French Batch 3 Local TeX Metadata Probe - 2026-07-05

Draft/non-canonical source-canon sidecar. Not native reviewed. Not approved. No license-clearance claim. No gate promotion. No Git push from this lane.

## Scope

This pass deepens the nine French batch 3 rows that could not be live-verified because arXiv returned HTTP `429`. It uses only the already-present local source packages, extracts them into a temporary probe directory, records TeX metadata and topic signals, then deletes the temporary extraction directory. No raw source bodies are copied into outputs.

## Files and Hashes

- Prior live-verification blocker table: `outputs/NOETHER_ROMANCE_SOURCE_CANON_FRENCH_BATCH3_LIVE_ARXIV_RATE_LIMIT_GAP_20260705.csv`; SHA-256 `666e93b73c14685dff8d21ab6e780c45d045cceb7f0bf9dde41fc3df8b301c82`.
- Local TeX metadata probe table: `outputs/NOETHER_ROMANCE_SOURCE_CANON_FRENCH_BATCH3_LOCAL_TEX_METADATA_PROBE_20260705.csv`; SHA-256 `f9d5eda1019a553a64793e3795656a5975a156de1bc3f74424875f3bb84a7c7a`.

## Method

- Verified that each local `.source` package still matches the previously recorded SHA-256 hash.
- Extracted packages only into `%TEMP%` for metadata probing, using tar where possible and gzip single-file extraction where needed.
- Parsed local TeX-like files for title, author, document class, babel language signal, and topic-term counts (`Noether`, `Hilbert`, `module`, `anneau`, `corps`, `ideal`, `invariant`).
- Deleted the temporary extraction directory after the probe.

## Results

| Local ID | Title candidate | Extraction | Language signal | Topic counts | Action |
| --- | --- | --- | --- | --- | --- |
| 1104.1507v4 | Sur l'homologie des groupes unitaires à coefficients polynomiaux | tar_archive_extracted | local_french_signal_present | Hilbert:3; module:26; anneau:42; corps:48; invariant:4 | local_tex_metadata_candidate_not_promoted |
| 1104.3350v3 | Cycles de codimension 2 et H 3 non ramifie pour les varietes sur les corps finis | tar_archive_extracted | local_french_signal_present | Hilbert:3; module:33; anneau:8; corps:159; invariant:8 | local_tex_metadata_candidate_not_promoted |
| 1509.07817v1 | Variétés abéliennes sur les corps de fonctions de courbes sur des corps locaux supérieurs | gzip_single_file_extracted | local_french_signal_present | Hilbert:3; module:20; corps:79; invariant:2 | local_tex_metadata_candidate_not_promoted |
| 1510.05382v1 | Sur le module de Bertrandias--Payan \\ dans une p -extension -- Noyau de capitulation | gzip_single_file_extracted | local_french_signal_present | Hilbert:3; module:21; corps:39; ideal:4; invariant:2 | local_tex_metadata_candidate_not_promoted |
| 1709.00597v2 | -0.3cm | tar_archive_extracted | local_french_signal_present | Hilbert:5; module:6; corps:19; invariant:1 | local_tex_metadata_candidate_title_parse_weak_not_promoted |
| 1905.13138v3 | Generators, spanning sets and existence of twisted modules for a grading-restricted vertex (super)algebra | gzip_single_file_extracted | local_english_signal_present_despite_french_shelf | module:308; ideal:1; invariant:6 | local_tex_metadata_english_shelf_mismatch_not_promoted |
| 2001.10515v4 | Sur la conjecture de Tate entiere pour le produit d'une courbe et d'une surface CH 0 | gzip_single_file_extracted | local_french_signal_present | Hilbert:5; module:52; anneau:1; corps:109; invariant:4 | local_tex_metadata_candidate_not_promoted |
| 2501.13300v2 | Arithmétique des schémas en groupes de Bruhat-Tits sur un anneau de Dedekind semi-local | tar_archive_extracted | local_french_signal_present | Hilbert:3; module:2; anneau:20; corps:45; ideal:6; invariant:2 | local_tex_metadata_candidate_not_promoted |
| 2505.05443v1 | Dualité étale à la Poitou-Tate pour les tores sur des variétés définies sur un corps fini | tar_archive_extracted | local_french_signal_present | Noether:4; Hilbert:3; module:13; anneau:13; corps:45; ideal:1; invariant:2 | local_tex_metadata_candidate_not_promoted |

## Summary Counts

- Rows probed locally: 9.
- Local hash matches: 9.
- Local French signal rows: 8.
- English shelf-mismatch rows: 1.
- Candidate-only rows, no promotions: 9.

## Explicit Gaps Retained

- Live arXiv API/e-print verification remains blocked by the prior HTTP `429` status for these nine rows.
- Local metadata is not a substitute for live title/license/access verification.
- `1905.13138v3` is an English-title source despite French-shelf placement and must not be promoted as a French target-language witness without deeper review.
- `1709.00597v2` has French/babel/topic signals, but the local title parser produced a weak title candidate; live metadata retry is needed.

## Non-Claim Boundary

No translation expansion, glossary expansion, term promotion, reviewer-packet population, native-review claim, canonical approval, license-clearance claim, gate promotion, Git staging, Git commit, or Git push occurred.
