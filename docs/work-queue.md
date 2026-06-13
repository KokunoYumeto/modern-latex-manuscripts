# Work Queue

This page turns the current archive gaps into concrete contribution targets. It is intentionally practical: pick a row, open the linked record, compare against source witnesses, and submit a narrow correction or continuation.

## Highest-Value Translation Work

| Area | Task | Start From |
|---|---|---|
| EGA | Translate and integrate EGA 0_III sections 12 and 13, which remain placeholder-level in the current preliminaries file. | [EGA record](https://doi.org/10.5281/zenodo.20414353) |
| EGA | Continue EGA III and EGA IV English translation beyond the current EGA IV section 4 partial working file. | [EGA record](https://doi.org/10.5281/zenodo.20414353) |
| SGA | Continue SGA and keep reader/source/audit packets synchronized with the current caveats. | [SGA record](https://doi.org/10.5281/zenodo.20410947) |
| SGA | Continue SGA5/SGA6 repair after repair027: use repair027 as the compact cumulative French-output branch, keep repair025 as the prior source-indexed audit/page-map provenance, synchronize English to the latest French repairs, continue SGA5 diagram disposition after source p181, then attack open diagram microgeometry, exact-symbol inventory, underlined-operator typography, SGA6 dense worklist rows, and SGA7 compression/source-check lanes. | [SGA record](https://doi.org/10.5281/zenodo.20410947) |
| SGA | Repair the SGA6 nuclear-audit gaps and continue SGA 7-I/II from French reference PDFs only with explicit source-check caveats. | [SGA record](https://doi.org/10.5281/zenodo.20410947) |
| Weber | Continue the English translation and repair of `Lehrbuch der Algebra` beyond the current Volume II draft surface, while continuing recursive gap repairs after the locally staged Batch134. Current ledger remains open for larger compression clusters; Batch134 reports no-change source-reviewed closures for Volume I §§12, 14, 16, 20, and 22, bringing the working ledger estimate to 82/112 rows closed and 30 open. Batch134 is queued for Zenodo upload and is not yet in the public file catalog. | [Weber record](https://doi.org/10.5281/zenodo.20412153) |
| Noether | Continue source checking and multilingual translation branches from the curated numbered-paper corpus; carry RA23 display-layout fixes and RA25-RA37 source-critical corrections forward, run final Paper 02 tag/layout inventory, propagate source corrections across EN/ES/JA/FR/ZH where applicable, and run a full symbol audit beyond Paper 01. RA37 is locally staged for Paper 04 pp.122-127 and reports restoration of an omitted determinant-product display in formula (8); it is queued for Zenodo upload and is not yet in the public file catalog. | [Noether record](https://doi.org/10.5281/zenodo.20412587) |

## Highest-Value Typesetting And Source-Check Work

| Area | Task | Start From |
|---|---|---|
| Non-European mathematics | Check the combined English translations against original-language drafts and source/reference material, especially diagrams, tables, terminology, and page order. | [Non-European consolidated record](https://doi.org/10.5281/zenodo.20410957) |
| Chinese classics | Check work-level English, modern Chinese, and original-language PDFs against each other for omissions and alignment. | [Chinese record](https://doi.org/10.5281/zenodo.20415751) |
| Indian/Sanskrit classics | Check source fidelity for Aryabhata, Bhaskara II, and Brahmagupta materials, especially formulas and tabular content. | [Indian/Sanskrit record](https://doi.org/10.5281/zenodo.20415754) |
| Islamic/Arabic texts | Check algebraic terminology, diagrams, and source alignment for al-Khwarizmi, al-Kashi, al-Tusi, and Omar Khayyam materials. | [Islamic/Arabic record](https://doi.org/10.5281/zenodo.20415769) |
| Bianchi | Verify Vol. I formulas, references, terminology, and index entries against the source witness. For A2, use `Bianchi_A2_core_p0001_0135_IT_EN_20260613.zip` as the latest compact/core package through p0135; keep older scan-heavy witness/intake layers as provenance, not authority, and continue glyph-level checks for matrix dots, prime marks, summation superscripts, and handwritten symbols. | [Bianchi record](https://doi.org/10.5281/zenodo.20615814) |
| Gordan / Clebsch-Gordan | `Theorie der Abelschen Functionen` is now carried through the authorial ending in `Gordan_Abel27_p343_355_DE_EN_20260612.zip`; source pp.356-362 are blank/end/cover scan witnesses. Next work is audit cleanup, reader-facing extraction, or non-Abelsche Gordan branches rather than a further Abelsche continuation. | [Gordan record](https://doi.org/10.5281/zenodo.20616260) |
| Gibbs / old physics | Continue `The Scientific Papers of J. Willard Gibbs`, Volume I after printed page 124. Keep source-scan slices, editable TeX, and explicit figure/table/formula inventories together; treat OCR as witness only. | [Gibbs record](https://doi.org/10.5281/zenodo.20649835) |
| Gauss | Repair the lower-quality staged Gauss OCR/TeX sections that were not promoted as clean reader material. | [Classical algebra and arithmetic record](https://doi.org/10.5281/zenodo.20414787) |
| Maxwell / old physics | Continue `A Treatise on Electricity and Magnetism`, Volume I after the current public source-witnessed tranches: IA 1873 first-edition pp.001-059, with math/token registers currently refreshed through pp.001-058 and p.059 queued for the next register refresh, plus earlier book pages 95-101, 103, 105, 109, and continuous pp.111-267. The current record includes the IA master-image source-index helper. The next local continuation is printed p.060; keep future public updates compact and ledger-governed, and do not merge broad OCR-derived Maxwell material into promoted range claims. | [Maxwell record](https://doi.org/10.5281/zenodo.20653107) |
| Additional authors | Check the selected drafts for wrapper removal, title accuracy, and source alignment before splitting into more complete author records. Bianchi, Gordan, Steinitz, Sylvester, Gibbs, Maxwell, Poincare, and Frobenius now have standalone records; the mixed shelf still needs Kneser, Mikami, Kronecker/Kron, Picard, Klein-Fricke, and related tranches triaged by package-level caveats. Current routed Kneser tranche is `Kneser_LVR_p0206_0219_DE_EN_20260612.zip`. | [Additional author cluster](https://doi.org/10.5281/zenodo.20411006) |

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

