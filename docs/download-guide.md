# Download Guide

Use this page when you know what you want to do, but not which file type to choose.

None of the records should be treated as a certified critical edition unless a later release explicitly says the maintainer has certified that status. Current files are working drafts, translation drafts, source-witnessed tranches, OCR/witness layers, or provenance packets. Older filenames can contain words such as `Complete`, `Strict`, `Source-Checked`, or `Critical`; use the record status notes rather than the filename alone.

## I Want To Read Something

Download or preview the top-level PDF files first.

Good starting points:

| Interest | Start With |
|---|---|
| EGA | [EGA record](https://doi.org/10.5281/zenodo.20414353), current English working build and French/source artifacts |
| SGA | [SGA record](https://doi.org/10.5281/zenodo.20410947), the current reader PDFs first, then the audit/source ZIPs |
| Non-European mathematics | [Non-European consolidated record](https://doi.org/10.5281/zenodo.20410957), index/readers first, then work-level and source ZIPs |
| Weber | [Weber record](https://doi.org/10.5281/zenodo.20412153), Volume I first; Volume II readers plus recursive repair packets through public Batch132. Local staging has Batch136 queued as the newest recursive no-change closure packet, but it is not a public Zenodo file until upload succeeds. |
| Noether | [Noether record](https://doi.org/10.5281/zenodo.20412587), cumulative reader PDFs and standalone English paper PDFs first; ZIPs contain TeX/source packages and active Paper 02/Paper 04 source-audit correction packets. Locally staged German source-audit support ZIPs plus Paper 05, Paper 06, Paper 07, Paper 08, Paper 15, Paper 16, Paper 17, Paper 18, Paper 19, Paper 20, and RA43 Paper 06 web drops add RA/source ledgers, high-DPI witnesses, OCR/Markdown locator material, Paper 08/Paper 15/Paper 16/Paper 17/Paper 18/Paper 19/Paper 20 math/source corrections, and Paper 06-08 source-style footnote-marker issues, but are not public Zenodo files until the next upload succeeds. |
| Bianchi | [Bianchi record](https://doi.org/10.5281/zenodo.20615814), English or Italian Vol. I reader first; for A2 use the public `Bianchi_A2_core_p0001_0135_IT_EN_20260613.zip` as the latest cataloged compact/core working package through p0135, with older scan-heavy p0105 and repair ZIPs retained as provenance/support layers. A smaller same-name Edge re-export exists locally under a disambiguated pending filename and should not be cited until a new Zenodo version publishes it. |
| Gordan / Clebsch-Gordan | [Gordan record](https://doi.org/10.5281/zenodo.20616260), open `Gordan_Abel27_p343_355_DE_EN_20260612.zip` for the current published Abelsche continuation through source pp.343-355 / printed pp.321-333 and cumulative stream through source p355. Local staging has `Gordan_Abelsche_FinalAuditFix02_DE_EN_20260613.zip`, `Gordan_de_linea_p025_047_final_LA_EN_scans_20260613.zip`, `Gordan_VB1_01_p001_009_DE_EN_20260613.zip`, and `Gordan_VB1_02_p010_028_DE_EN_20260613.zip` queued, but they are not public Zenodo files until upload succeeds. Earlier Abel and AllPrior/auditfix packages cover earlier branches; PDFs, TeX, source witnesses, and audit ledgers are inside. |
| Frobenius | [Frobenius record](https://doi.org/10.5281/zenodo.20673444), open the published QA03 package for the selected group-character German/English cumulative working draft and source scans; RA05 is locally staged for upload as the next recursive auditfix. |
| Poincare | [Poincare record](https://doi.org/10.5281/zenodo.20673461), use `poincare_v1_*` packages individually; this is a non-continuous recovery stream, not a seamless Tome I edition. |
| Kneser | [Additional author cluster](https://doi.org/10.5281/zenodo.20411006), current published mixed-shelf Kneser continuation is p0206-p0219. A local p0234-p0248 German/English continuation is routed/extracted and queued for upload, but is not a public Zenodo file until a new version publishes it. |
| Classical algebra/arithmetic | [Classical algebra and arithmetic record](https://doi.org/10.5281/zenodo.20414787), numbered reader PDFs by author; inherited Cayley `source_checked` filenames are de-promoted unless re-promoted by a later source audit |

If you want usable mathematical text rather than repair evidence, prefer top-level PDFs and files named `reader`, `working_draft`, `source_checked`, or `cumulative`. Treat files named `OCR_candidate`, `formula_witness`, `crop_witness`, or `locator_aid` as checking aids. Even for reader PDFs and source-checked ranges, verify serious formulas, diagrams, tables, theorem statements, and unusual notation against source witnesses.

## I Want The TeX Or Build Artifacts

Download the artifact/source ZIP for the relevant record.

ZIPs usually contain some combination of:

- TeX sources;
- component PDFs;
- source scans or source-reference PDFs;
- OCR text;
- page images;
- render checks and logs;
- provenance notes and manifests.

The ZIPs are intentionally less polished than the reader PDFs. They exist so the public PDF can be checked, rebuilt, corrected, and extended.

Filename language matters:

- `OCR_candidate`, `formula_witness`, `crop_witness`, or `locator_aid` means machine-extracted or checking material, not a reader edition.
- `working_draft`, `source_checked`, `reader`, or `cumulative` means compiled TeX/PDF promoted to a declared draft layer. It does not mean a final critical edition unless the record says so explicitly.

That distinction is deliberate. OCR-derived TeX is useful because it can point to omissions or hard formulas; the reader-facing value comes from compiled drafts and translations whose structure has been organized and checked to the stated level.

## I Want To Check A Translation

Use both layers:

1. Open the translated reader PDF.
2. Open the original-language PDF or source/reference scan from the same record.
3. Check page order, theorem numbering, formulas, diagrams, tables, and cross-references.
4. Report corrections with the exact record, filename, page/section, and source witness.

## I Want Everything

Use the [main project landing record](https://doi.org/10.5281/zenodo.20393488) for the broad preservation surface. It is intentionally larger and more redundant than the focused records.

Use the topic/author records when you want a cleaner browsing experience.

## I Want To Contribute

Start with:

- [browse index](browse-index.md);
- [by author and work](by-author-and-work.md);
- [record landing pages](records/README.md);
- [known gaps](known-gaps.md);
- [contributing guide](../CONTRIBUTING.md).

For release work, use the [release checklist](release-checklist.md).

