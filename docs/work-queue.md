# Work Queue

This page turns the current archive gaps into concrete contribution targets. It is intentionally practical: pick a row, open the linked record, compare against source witnesses, and submit a narrow correction or continuation.

## Highest-Value Translation Work

| Area | Task | Start From |
|---|---|---|
| EGA | Translate and integrate EGA 0_III sections 12 and 13, which remain placeholder-level in the current preliminaries file. | [EGA record](https://zenodo.org/records/20454552) |
| EGA | Continue EGA III and EGA IV English translation beyond the current EGA IV section 4 partial working file. | [EGA record](https://zenodo.org/records/20454552) |
| SGA | Continue SGA and keep reader/source/audit packets synchronized with the current caveats. | [SGA record](https://zenodo.org/records/20661245) |
| SGA | Continue SGA5/SGA6 repair after repair017: synchronize English to the latest French repairs, then attack open diagram microgeometry, exact-symbol inventory, underlined-operator typography, and the remaining SGA6 v3 worklist rows. | [SGA record](https://zenodo.org/records/20661245) |
| SGA | Repair the SGA6 nuclear-audit gaps and continue SGA 7-I/II from French reference PDFs only with explicit source-check caveats. | [SGA record](https://zenodo.org/records/20661245) |
| Weber | Continue the English translation of Lehrbuch der Algebra beyond the current Volume II draft surface, while continuing recursive gap repairs after Batch122's Vol. II §81 table/boundary correction. | [Weber record](https://zenodo.org/records/20660948) |
| Noether | Continue source checking and multilingual translation branches from the curated numbered-paper corpus; propagate the RA20 Paper 02 German display correction and FR/ZH Paper 19 section 6 tau correction into EN/ES/JA, and resolve RA10 Papers 40-43 inline body resynchronization. | [Noether record](https://zenodo.org/records/20651590) |

## Highest-Value Typesetting And Source-Check Work

| Area | Task | Start From |
|---|---|---|
| Non-European mathematics | Check the combined English translations against original-language drafts and source/reference material, especially diagrams, tables, terminology, and page order. | [Non-European consolidated record](https://zenodo.org/records/20410957) |
| Chinese classics | Check work-level English, modern Chinese, and original-language PDFs against each other for omissions and alignment. | [Chinese record](https://zenodo.org/records/20415752) |
| Indian/Sanskrit classics | Check source fidelity for Aryabhata, Bhaskara II, and Brahmagupta materials, especially formulas and tabular content. | [Indian/Sanskrit record](https://zenodo.org/records/20415755) |
| Islamic/Arabic texts | Check algebraic terminology, diagrams, and source alignment for al-Khwarizmi, al-Kashi, al-Tusi, and Omar Khayyam materials. | [Islamic/Arabic record](https://zenodo.org/records/20415770) |
| Bianchi | Verify Vol. I formulas, references, terminology, and index entries against the source witness. For A2, use `Bianchi_A2_cont_p0001_0077_IT_EN_20260612.zip` as the latest continuation layer through p0077, then continue from p0078 inside section 17; keep older witness/intake layers as provenance, not authority. | [Bianchi record](https://zenodo.org/records/20664430) |
| Gordan / Clebsch-Gordan | Continue Abelsche Functionen after source p.270 / printed p.248. Use Abel19 and `Gordan_AllPrior_AuditFix01_20260610.zip` as the current correction layers. | [Gordan record](https://zenodo.org/records/20664425) |
| Gibbs / old physics | Continue `The Scientific Papers of J. Willard Gibbs`, Volume I after printed page 124. Keep source-scan slices, editable TeX, and explicit figure/table/formula inventories together; treat OCR as witness only. | [Gibbs record](https://zenodo.org/records/20649836) |
| Gauss | Repair the lower-quality staged Gauss OCR/TeX sections that were not promoted as clean reader material. | [Classical algebra and arithmetic record](https://zenodo.org/records/20583048) |
| Maxwell / old physics | Continue `A Treatise on Electricity and Magnetism`, Volume I after the current public source-witnessed tranches: IA 1873 first-edition pp.001-046 plus earlier book pages 95-101, 103, 105, 109, and continuous pp.111-267. The next local continuation is printed p.047; keep future public updates compact and ledger-governed, and do not merge broad OCR-derived Maxwell material into promoted range claims. | [Maxwell record](https://zenodo.org/records/20660332) |
| Additional authors | Check the selected drafts for wrapper removal, title accuracy, and source alignment before splitting into more complete author records. Bianchi, Gordan, Steinitz, Sylvester, Gibbs, and Maxwell now have standalone records; the mixed shelf still needs Poincare, Frobenius, Kneser, Mikami, Kronecker/Kron, Picard, Klein-Fricke, and related tranches triaged by package-level caveats. Current routed tranches include `poincare_v1_21.zip` through Chapter XIV, `Frobenius_all_GE_EN_cum_scans_QA03_20260611.zip` for the selected Frobenius sequence, and `Kneser_LVR_p0177_0192_DE_EN_20260612.zip` for Kneser p0177-p0192 / §§40-42. | [Additional author cluster](https://zenodo.org/records/20664437) |

## Archive And Metadata Work

| Area | Task | Start From |
|---|---|---|
| Naming clarity | Separate OCR/math-extraction witness packages from genuine mathematical working drafts in filenames and Zenodo descriptions. Use `OCR_candidate` or `formula_witness` for unpromoted extraction; use `working_draft`, `source_checked`, `reader`, or `cumulative` only after compilation and declared source-check level. | [Workflow notes](workflow.md) and [quality rubric](quality-rubric.md) |
| Public catalog | Keep `manifests/public-file-catalog.csv`, `docs/public-file-catalog.md`, and `docs/records/` synchronized after each Zenodo change. | `python scripts/build_public_catalog.py`; `python scripts/build_record_pages.py` |
| Status pages | Update the dashboard, known gaps, and work queue whenever a record is replaced or a major section is completed. | [Project status dashboard](project-status-dashboard.md) |
| Release hygiene | Run the release checklist before publishing new versions or splitting a corpus into a new author/topic record. | [Release checklist](release-checklist.md) |
| GitHub mirror | Push the local mirror once GitHub accepts the configured SSH key; until then, keep the portable snapshot ZIP current. | Local mirror and snapshot ZIP |

## Good First Corrections

- Fix a single bad formula, theorem reference, or page break in a TeX source.
- Compare one PDF page against its source scan and report exact differences.
- Replace a vague issue report with a precise record/file/page/source-witness report.
- Identify a better public scan for a work already present in draft form.
- Confirm whether a suspected duplicate is genuinely redundant or a different edition/version.
