# Download Guide

Use this page when you know what you want to do, but not which file type to choose.

None of the records should be treated as a certified critical edition unless a later release explicitly says the maintainer has certified that status. Current files are working drafts, translation drafts, source-witnessed tranches, OCR/witness layers, or provenance packets. Older filenames can contain words such as `Complete`, `Strict`, `Source-Checked`, or `Critical`; use the record status notes rather than the filename alone.

## I Want To Read Something

Download or preview the top-level PDF files first.

Good starting points:

| Interest | Start With |
|---|---|
| EGA | [EGA record](https://zenodo.org/records/20454552), current English working build and French/source artifacts |
| SGA | [SGA record](https://zenodo.org/records/20661245), the current reader PDFs first, then the audit/source ZIPs |
| Non-European mathematics | [Non-European consolidated record](https://zenodo.org/records/20410957), index/readers first, then work-level and source ZIPs |
| Weber | [Weber record](https://zenodo.org/records/20660948), Volume I first; later volumes are in progress |
| Noether | [Noether record](https://zenodo.org/records/20651590), cumulative reader PDFs and standalone English paper PDFs first; ZIPs contain TeX/source packages |
| Bianchi | [Bianchi record](https://zenodo.org/records/20651036), English or Italian Vol. I reader first; for A2 use `Bianchi_A2_reaudit_p0001_0066_IT_EN_20260611.zip` as the preferred correction layer through p0066, with older continuation/HQ/audit ZIPs retained as provenance/support layers. |
| Gordan / Clebsch-Gordan | [Gordan record](https://zenodo.org/records/20660721), open Abel17 for the current Abelsche continuation through source p243 / printed p221; Abel13 includes the p190 continuation of equation (4), while Abel14-16 continue p194-p227. AllPrior/auditfix packages cover earlier branches; PDFs, TeX, source witnesses, and audit ledgers are inside |
| Classical algebra/arithmetic | [Classical algebra and arithmetic record](https://zenodo.org/records/20583048), numbered reader PDFs by author; inherited Cayley `source_checked` filenames are de-promoted unless re-promoted by a later source audit |

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

Use the [main project landing record](https://zenodo.org/records/20415117) for the broad preservation surface. It is intentionally larger and more redundant than the focused records.

Use the topic/author records when you want a cleaner browsing experience.

## I Want To Contribute

Start with:

- [browse index](browse-index.md);
- [by author and work](by-author-and-work.md);
- [record landing pages](records/README.md);
- [known gaps](known-gaps.md);
- [contributing guide](../CONTRIBUTING.md).

For release work, use the [release checklist](release-checklist.md).
