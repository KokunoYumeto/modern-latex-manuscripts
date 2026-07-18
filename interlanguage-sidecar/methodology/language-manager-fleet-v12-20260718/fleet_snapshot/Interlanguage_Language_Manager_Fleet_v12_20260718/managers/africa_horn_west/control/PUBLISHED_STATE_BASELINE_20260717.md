# Africa/Horn/West achieved-state baseline — 2026-07-17

## Bottom line

The lane achieved substantial source discovery, preservation, provenance, and
coordination. It did **not** achieve a completed translation in any routed
language.

No target-language TeX/PDF pair was found for Somali, Oromo, Tigrinya,
Amharic, Afar, Hausa, Fulfulde, Mandinka, Akan/Twi, Wolof, Yoruba, or Igbo.
No term was promoted, no translation completion was claimed in the final R9
active-row ledger, and no accepted external/community review return was found.

This baseline separates three states that the inherited paperwork often mixed:

1. public source/provenance infrastructure;
2. locally recovered but unpublished source shelves and candidate ledgers;
3. translation and review outputs that do not yet exist.

## Audit coordinates

- GitHub repository: <https://github.com/KokunoYumeto/modern-latex-manuscripts>
- GitHub `main` audited at `4051c2c9698c9ceedc90b66e9d02cdd8f22949e9`
  (2026-07-17T18:40:56Z).
- Other-PC source branch audited at
  `cfa67d676fab033acddaad2f0add10a14905466b`:
  <https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/codex/noether-pc-20260629>
- Zenodo concept DOI: <https://doi.org/10.5281/zenodo.21124403>
- Latest audited Zenodo version: `10.5281/zenodo.21300808`, published
  2026-07-10:
  <https://zenodo.org/records/21300808>
- Local recovery root:
  `C:\Users\Floris\Downloads\codex backup dump 7-4`

The local control repository has no remote and is not the publication
authority. GitHub and Zenodo were therefore inspected directly.

## What is actually public on GitHub

### 1. A real R9 source-body payload

The other-PC branch contains
`language-source-bodies/r9-africa-horn-west-20260705`. It was introduced by:

- `7b3ed05b899b3df9bf3d8d4d8a71b0ee5e5ec8b2` — “Add R9 Hausa Tigrinya
  source-body payload”;
- `ebd7a580a677259689af73a4a352b62a47ed7923` — subsequent package update.

The complete root has 16 blobs totalling 8,549,953 bytes. Eleven are
manifest-tracked source/body/support files totalling 8,529,598 bytes; the other
five are package metadata and a log excerpt.

Its language-bearing contents are narrowly scoped:

| Target | Public material | What it is |
| --- | --- | --- |
| Hausa | `hawiki-Lissafi-20200722.pdf`; `FazamMV23_HausaMath_4c35f0abeb88.zip` | Upstream Hausa mathematical prose/source witnesses. |
| Tigrinya | arXiv source tar, GitHub source ZIP, extracted `main.tex`, `.bbl`, `.bst`, `.sty`, two fonts | Upstream work on Tigrinya number verbalization and its build assets. |

The package README explicitly classifies this as source-canon/provenance
support only—not native review, accepted terminology, translation completion,
source-fidelity certification, publication readiness, or blanket license
clearance.

Public branch root:
<https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/codex/noether-pc-20260629/language-source-bodies/r9-africa-horn-west-20260705>

### 2. A curated copy on `main`

Commit `ccaca5ac79caf29e9681b6564fd5b6c4fe42b20f` imported the public-safe
source-body payload to `main` as “Import other-PC R9 source-body payload”:

<https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/ccaca5ac79caf29e9681b6564fd5b6c4fe42b20f>

Curated path:
<https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/main/interlanguage-sidecar/20260705/other_pc_r9_africa_horn_west_source_body_payload_20260705/language-source-bodies/r9-africa-horn-west-20260705>

### 3. A large coordination trail

At the audited `main` head, path matching for the R9/Africa-Horn-West lane
found 256 paths, of which 204 were blobs. Most are repeated rolling package
indexes, manifests, checksum refreshes, run logs, recovery ledgers, and route
observations.

Only three matching `.tex` or `.pdf` blobs exist:

1. an upstream arXiv Tigrinya-number-verbalization PDF;
2. the upstream Hausa `hawiki-Lissafi` PDF;
3. the upstream Tigrinya-number-verbalization `main.tex`.

None is a translation of a project work. A second search using the target
language names and exact ISO-like path segments found no other target-language
TeX/PDF candidate on `main`.

### 4. The final active-row state is uniformly non-promoted

The latest R9 active-row table on `main` has 49 rows across the inherited
targets. Every row says:

- `source_text_saved=false`;
- `translation_completion_claimed=false`;
- `approval_or_promotion_claimed=false`;
- `promotion_allowed=false`.

Source table:
<https://github.com/KokunoYumeto/modern-latex-manuscripts/blob/main/noether-slavic-handoff/20260629/cross-session-coordination/20260704/NOETHER_SESSION_OUTPUT_PACKAGE634_20260705T171259_ROLLING_DELTA_AFTER_PACKAGE633/lane_outputs/noether-r9-africa-horn-west/R9_ACTIVE_ROW_SOURCE_CANON_BUCKETS_AND_DRAFT_ACTIONS_20260705.csv>

## What is actually public on Zenodo

The concept DOI resolves to the July 10 v0.4 methodology record. The record's
own status language says it is methodology, source-body routing, provenance,
and corpus infrastructure—not native approval, accepted terminology, a
finished interlanguage, mathematical source-fidelity certification, reader
completion, or proof that a language branch is complete.

The R9 source-body root is genuinely present inside the published top-level
archive:

`07_Interlanguage_OtherPC_SourceBodies_Turkic_Indigenous_SEA_OLP_20260707.zip`

Despite that archive's incomplete label, its central directory contains the
full `language-source-bodies/r9-africa-horn-west-20260705/` tree, including all
16 blobs described above. The Zenodo side-branch inventory independently lists
the R9 corpus root as a source-body package of about 8.55 MB.

Archive:
<https://zenodo.org/api/records/21300808/files/07_Interlanguage_OtherPC_SourceBodies_Turkic_Indigenous_SEA_OLP_20260707.zip/content>

Inventory:
<https://zenodo.org/api/records/21300808/files/09_Interlanguage_SourceBody_SideBranch_Inventory_20260707.csv/content>

A separate GitHub manifest still labels
`OtherPC_R9_Africa_Horn_West_SourceBodyPayload_20260705.zip` as a pending Zenodo
upload. That exact standalone filename is not a top-level file in the audited
Zenodo version, and the corresponding `publish_staging` path is not on `main`.
The content was nevertheless published inside the grouped archive above.

Pending manifest:
<https://github.com/KokunoYumeto/modern-latex-manuscripts/blob/main/manifests/pending-zenodo-uploads/20260705_other_pc_r9_africa_horn_west_source_body_payload.json>

## What was recovered locally but is not a public translation

The backup contains much larger July 3 source returns than the small public R9
payload:

| Target | Recovered source return | Extraction state | Translation consequence |
| --- | ---: | --- | --- |
| Somali | 74 downloaded PDFs, 3,446 pages | 62 rows with extractable Latin text; 12 weak/empty; 10 failed/non-download rows | Foundational candidate ledger exists; no accepted terms and no translation. |
| Oromo | 83 downloaded PDFs, 3,444 pages | 70 rows with extractable Latin text; 13 weak/empty; one failed row | Foundational candidate ledger exists; no accepted terms and no translation. |
| Tigrinya | 82 downloaded PDFs, 3,420 pages | 53 extractable Ethiopic-text rows; 29 weak/empty; two failed rows | School-math evidence plus narrow public source body; no accepted higher-algebra register and no translation. |
| Amharic | 48 downloaded PDFs, 588 pages | 44 font-garbled/non-Unicode, 3 extractable Ethiopic, 1 empty | Script/OCR repair remains a hard intake task; no accepted terms and no translation. |
| Afar/Qafar | 5 captured context PDFs plus web/media routes | No admitted cacheable mathematical-text witness | Context only; no term ledger and no translation. |

The Somali ledger has 17 rows and the Oromo ledger 18 rows. All have
`promotion_allowed=false`. They are source-extracted candidate forms, not
canonical terminology. Somali theorem/proof remained an explicit gap; Oromo
has a textbook theorem marker but not a reviewed higher-algebra/proof register.

The later Hausa pass strengthened routes to a secondary-mathematics app/book,
public-register pages, and context material, but explicitly accepted no Hausa
terms and translated no Noether prose. Igbo had no admitted mathematical
witness. Fulfulde, Mandinka, Akan/Twi, Wolof, and Yoruba remained at glossary,
dictionary, or reviewer-scaffold level.

## What has not been achieved

- No completed Somali translation tranche.
- No completed Oromo translation tranche.
- No completed Tigrinya translation tranche.
- No completed Amharic translation tranche.
- No completed Afar/Qafar translation tranche.
- No completed Hausa translation tranche.
- No completed Fulfulde/Fulani translation tranche.
- No completed Mandinka/Manding translation tranche.
- No completed Akan/Twi translation tranche.
- No completed Wolof translation tranche.
- No completed Yoruba translation tranche.
- No completed Igbo translation tranche.
- No target-language compiled PDF for any work in this lane.
- No accepted terminology ledger.
- No accepted external/community review return.
- No valid pan-African, pan-West-African, or pan-Horn language object.
- No evidence for unified v6.2 readiness.

## Corrected interpretation

The work to date is not “nothing”: it is a real source and provenance layer,
with especially substantial locally recovered school-mathematics shelves for
Somali, Oromo, Tigrinya, and Amharic. But it is also not translation
production. The prior system produced many more coordination artifacts than
reader artifacts and repeatedly described future drafting without crossing the
mandatory TeX-plus-compiled-PDF gate.

From this baseline onward:

- provenance and routing live in a typed evidence graph;
- dependence and breadth live in a declared family/cohort tree;
- gaps, adverse evidence, competitors, candidates, and vetoes stay in separate
  channels;
- Horn and West remain separate research subprograms under one manager;
- translation may be drafted only for a named target/standard/script/audience
  whose source floor supports the actual work domain;
- draft status never becomes review or community acceptance by wording alone.

