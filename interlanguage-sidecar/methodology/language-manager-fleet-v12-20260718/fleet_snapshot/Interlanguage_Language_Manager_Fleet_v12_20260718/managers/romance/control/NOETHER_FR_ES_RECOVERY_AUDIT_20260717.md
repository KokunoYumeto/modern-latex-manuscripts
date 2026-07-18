# Noether French/Spanish recovery audit — 2026-07-17

## Finding

The other computer's work survived, but neither translation is complete. Both recovered cumulative editions contain draft material labelled Papers 1–43 and both happen to compile; that establishes nominal range coverage only. It does not establish that every paper is fully or correctly translated.

The newest German authority, R823, also proves that Papers 1–43 are not the whole volume. After Paper 43 it contains the full 31-section course/book `Algebra der hyperkomplexen Größen`, the Kapferer--Noether paper and supplement, the bibliography, and the terminal lists. Spanish has no recovered translation of that terminal scope. French has unintegrated terminal drafts, but its `post44` material was made from an older composite witness and is not a complete R823 translation.

The remaining job therefore includes both source rebase and scope completion: identify omissions or mistranslations in Papers 1–43, repair mathematical and linguistic defects, translate/rebuild all material after Paper 43 against R823, compile the complete cumulative books, and visually verify them.

This file records recovered draft evidence. Both books remain explicitly incomplete and unfit for publication in their recovered state.

## Current source authority

- Authority package: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717_COMPLETE.zip`
- Package SHA-256: `7AFC1B865EC710F6BECE507260605CBA7C950E5CC089C7464F63CBC20A8BD738` (matches the supplied sidecar)
- Package timestamp/size: 2026-07-17 18:37:48 / 24,613,194 bytes
- German TeX inside package: `1\01_cumulative\Noether_R823_cum_de.tex`
- German TeX SHA-256/size: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21` / 2,125,031 bytes
- German PDF inside package: `1\01_cumulative\Noether_R823_cum_de.pdf`
- German PDF SHA-256/pages: `B00486BAF227EE866DBBC2A9B6AA021D818B0373223E2000C60ED6AFA31B416F` / 466 pages
- R823 directly reopens Paper 20 printed pp. 27--31 against the article witness and records six source-style/layout corrections. No OCR was used for that audit.
- Earlier R821 files remain provenance only and are no longer the controlling authority.

## Recovered Spanish working edition

- TeX: `C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\sources\non_slavic_existing_translation_artifacts\zenodo_20836874_20260628\extracted\12_Noether_-_Spanish_Current_RA10_20260612\cumulative\cum_es.tex`
- TeX SHA-256: `2614DBF232F7DBB5914C1BFC8302019DFA914DEB305960BB46F20F2AD1D31F0C`
- TeX timestamp: 2026-07-03 18:49:14
- Nominal draft range: Papers 1–43, in one cumulative source. This is not a completion claim.
- Newest recovered PDF: `C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\renders\non_slavic_existing_translation_artifacts\spanish_ra10_p01_source_markup_patch_20260703\cum_es.pdf`
- PDF SHA-256: `D2E7BFA74D7974A00C0F0CC16EC3C39F8257BE77D59D6775617020BE8C71B5F5`
- PDF size/pages: 2,114,365 bytes / 409 pages.
- Build result: successful; recovered log contains only the harmless Xe/LuaLaTeX warning that `inputenc` is ignored.
- Latest visible patch chain: P10, P9, P6, P5, P3, P2 layout, and P1 source markup on 2026-07-03. Earlier 2026-06-29/30 packages contain source-native/source-resynchronization work across much of P11–P43.
- Terminal scope: no Spanish `post44`, `post45`, or post-bibliography translation was found in the recovered end-matter tree.
- Status: incomplete recovered draft. Coverage, accuracy, source synchronization, and native-language quality remain to be proved paper by paper, and the R823 terminal scope remains untranslated.

## Recovered French working edition

- Cumulative TeX: `C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\sources\non_slavic_existing_translation_artifacts\zenodo_20836874_20260628\extracted\14_Noether_-_French_and_Simplified_Chinese_Checkpoint_P19s06_20260612\tex\cum_fr_P43.tex`
- TeX SHA-256: `72366D7715E24F8B34E249685C746668487F42EF5862FADA7D579E6204C8DA3A`
- TeX timestamp: 2026-07-02 05:56:23
- Nominal draft range: Papers 1–6 inline, including Papers 3–5; Papers 6–43 through local body inputs. This is not a completion claim. The old package name ending in `P19s06` is misleading and is not its actual range boundary.
- Newest recovered PDF: `C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\renders\non_slavic_existing_translation_artifacts\french_p43_20260702\cum_fr_P43.pdf`
- PDF SHA-256: `38503338864AB7995DDCB19DDF7E049AACE166A2869280260B1402620B61BD76`
- PDF size/pages: 2,065,961 bytes / 418 pages.
- Build result: successful; recovered log contains only the harmless Xe/LuaLaTeX warning that `inputenc` is ignored.
- Independent P1–5 witness: `C:\Users\Floris\Documents\Papors\Chatnotes\CHat translates and clean\Noether Multilingual\N_ZHFR_P05_20260605\08_fr\FR_01_05_scanfix.tex`, with a 70-page compiled PDF.
- Recovered terminal drafts:
  - `post44`: fifteen French working chunks exist, but they cite the older `Noether_Post44_Algebra_der_hyperkomplexen_Groessen_German_TeX_witness_body.tex`. That witness is a composite: a short/alternate §§1--29 component followed by a fuller continuation concentrated on §§22--31. Its chapter/section scheme differs from the integrated R823 book (including omission/misplacement of §17), so it cannot be promoted as a complete translation.
  - `post45`: one standalone French v001 exists against an older local German witness.
  - post-bibliography: one standalone French v001 exists against an older local German witness.
  - None of those units is integrated into `cum_fr_P43.tex`, and all require R823 reconciliation.
- Status: incomplete recovered draft. Obvious mojibake/orthographic defects remain in later prose (examples include `dàpend`, `diffàrentielle`, `tète`, and `remplacant`; large P38/P40 passages also omit normal French diacritics), and omissions/mistranslations have not yet been ruled out.

## Translation canon actually used

There was no single canon.

- Spanish is a layered RA10 scan-first branch: an older cumulative translation plus direct scan-visible apparatus restoration, local source-repaired witnesses, R124plus/original-scan checks for selected papers, and later per-paper source-native patches. It is better documented than French, but it was not translated from R823 and its own README disclaims final scholarly closure.
- French is a layered checkpoint lineage: older French witnesses for early papers, sequential direct translation from then-current German source slices, and later scan/source-fidelity repairs for selected papers. Paper 40 explicitly used a best-available repaired witness rather than strict final source certification. Papers 41--43 were appended later. It was not translated from R823.
- The target-language control corpus contains real French and Spanish mathematical TeX, but no evidence shows that a single approved French or Spanish terminology canon governed every paper. The Romance term artifacts are source evidence and generated draft rows, not a native-reviewed canonical glossary.

## What the prior “Romance lane” did

The latest recovered lane log is:

`C:\IL_GitHub\01_other_pc_full\noether-slavic-handoff\20260629\cross-session-coordination\20260704\NOETHER_SESSION_OUTPUT_PACKAGE634_20260705T171259_ROLLING_DELTA_AFTER_PACKAGE633\lane_outputs\noether-romance-source-evidence-draft-lane\NOETHER_ROMANCE_CORPUS_TRANSLATION_RUN_LOG_20260704.md`

That work built French/Spanish terminology and source-evidence infrastructure against an old June 24 German baseline. It reports 46 term rows, 44 with draft/source-note coverage and two tensor-product source-anchor blockers. It explicitly labels itself draft/noncanonical/not native reviewed. It did not rebase or finish the 43-paper French and Spanish editions.

## Romance reference corpus

- Main French/Spanish corpus: `C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut\sources\non_slavic_reference_corpus\20260628_french_spanish_native_math_register`
- Recorded extent: 52 accepted sources and 182 TeX files; French 41 sources/100 TeX, Spanish 11 sources/82 TeX.
- Transfer-ready source-body package: `C:\IL_GitHub\01_other_pc_full\language-source-bodies\romance-b3-transfer-ready-20260706`
- Recorded extent: 78 bodies — 54 Spanish, 16 French, four generated French/Spanish drafts, three Italian, and one Portuguese.

French and Spanish have a usable mathematical-register corpus for repair work; that corpus does not make the recovered drafts complete. Italian and Portuguese have useful seeds but not enough breadth for a responsible full Noether translation lane yet. No comparable Catalan or other Romance corpus was recovered. Expansion beyond French/Spanish should wait for corpus deepening and license review.

## Romance interlanguage infrastructure status

The intended Romance side is a zonal-access layer, not a substitute for standard French or Spanish translations. Its production ladder is `source shelf -> term spine -> proof grammar -> script sidecar -> review packet -> pilot gate`. Its job is to record cross-Romance senses, equivalents, false friends, branch-sensitive recognizability, and evidence-backed bridge choices without allowing French or Spanish to become a hidden pivot.

No literal `WordWeb` artifact was found. What exists is a partial precursor:

- a 60-concept shared term spine with attestation counts: Spanish 60/60, French 60/60, Portuguese 52/60, Catalan 51/60, Italian 51/60, Galician 48/60, Romanian 42/60, Romansh 30/60;
- a 39-row C2 sense/hard-term audit with 27 internally witnessed rows, six specialist Noether gaps, three rejected false-sense rows, two sense-review rows, and one earlier low-confidence row;
- the latest French/Spanish head package carries 44 source-support rows, 184 term-evidence snippets, and two tensor-product blockers, all explicitly generated-draft/noncanonical/not-native-reviewed.

Those are node/evidence inventories, not a completed semantic graph or approved bridge lexicon. The relations, competing forms, sense boundaries, derivational links, false-friend edges, cohort effects, and final term promotions are not assembled into one operative WordWeb.

The marginal-intelligibility work is even less complete operationally. A general scoring concept and a field specification exist, but the required `PAN_ROMANCE_ACCESS_LEDGER_v1.{md,json}` does not. The generic marginal-intelligibility ledger contains no Romance term rows, no cohort-scored alternatives, and no human intelligibility results. The lane's own status is therefore `source_or_policy_partial_no_pilot` / `not_pilot_ready`. Method drafted; Romance implementation effectively absent; external validation zero.

## Confirmed source corrections and provisional local repair

The recovered R705 source audit confirms two mathematical corrections that postdate both final translation builds:

1. Paper 20, printed p. 32: `S(Z,u)=\sum \Phi_\lambda(Z)U_\lambda` must read `S(Z,u)=\sum \Phi_\lambda(Z)U_i`.
2. Paper 34, printed p. 648: three displayed `\simeq` relation signs must be `\sim`.

Both recovered French and Spanish editions contained the old Paper 20 formula and the three old Paper 34 relation signs. Those corrections have been applied only to isolated working copies under `03_projects/noether/03_translation_workspaces/romance_rebase_20260717` and compile successfully. They are provisional repair evidence, not completion. The working copies must now be reconciled to R823, including its six newer Paper 20 run-in/dash/punctuation fixes.

## Rebase map status

The closest contemporaneous German checkpoints appear to be R549 for the 2026-07-02 French build and R704 for the 2026-07-03 Spanish build. The earlier token comparison against R821 remains a rough triage clue only; it is now stale and must be regenerated against R823. Token similarity is never proof of translation equivalence.

- Highest confirmed repair: P20 and P34 in both languages.
- Largest remaining French source drift: P40, then P30/P34; notable P13/P15/P19/P20/P24.
- Largest remaining Spanish source drift: P30/P34, then P15/P19/P20; Spanish P40–P42 were already exact against R704 and show no later token drift in this comparison.
- Many papers compare exactly to the contemporaneous baseline; those still require build and visual QA before final acceptance.
- R823 changes within P20 include source run-in structure, spacing, em-dash pairs, and punctuation. They need deliberate target-language propagation rather than blind German-format copying.

See `NOETHER_FR_ES_PAPER_STATUS_20260717.csv` for the operational paper queue.

## Acceptance gate

A paper/tranche is complete only when all of the following exist:

1. rebased French and Spanish TeX against the current German authority;
2. recorded source/terminology decisions for non-mechanical changes;
3. successful compilation to PDF — plain text is not a completed deliverable;
4. clean build log apart from understood harmless warnings;
5. rendered-page visual QA for changed pages plus a spread across the cumulative volume;
6. hashes and a continuation cursor in the lane ledger.

## Immediate production order

1. Freeze R823 and the recovered French/Spanish artifacts by hash; never edit the backup dump.
2. Generate a fresh R823 structural/source-delta map for every Paper 1--43 unit in both languages.
3. Reconcile the source-confirmed P20/P34 working-copy repairs to R823, then process all content-bearing R823 deltas.
4. Run systematic language cleanup, with French encoding/diacritic defects as an explicit first pass and terminology choices checked against native mathematical corpora.
5. Rebuild the R823 `Algebra der hyperkomplexen Größen` book in French and Spanish. Treat the old French chunks only as salvageable translation memory, not as authority.
6. Reconcile/translate the Kapferer--Noether unit, bibliography, and terminal lists in both languages and integrate them into each cumulative source.
7. Compile complete French and Spanish cumulative PDFs, visually verify them, record hashes/continuation cursor, and only then hand a publication tranche to the Zenodo/upstream task.
