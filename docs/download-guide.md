# Download Guide

Use this page when you know what you want to do, but not which file type to choose.

## I Want To Read Something

Download or preview the top-level PDF files first.

Good starting points:

| Interest | Start With |
|---|---|
| EGA | [EGA record](https://zenodo.org/records/20414353), current English working build and French/source artifacts |
| SGA | [SGA record](https://zenodo.org/records/20410947), the current reader PDFs first, then the audit/source ZIPs |
| Non-European mathematics | [Non-European consolidated record](https://zenodo.org/records/20410957), index/readers first, then work-level and source ZIPs |
| Weber | [Weber record](https://zenodo.org/records/20412153), Volume I first; later volumes are in progress |
| Noether | [Noether record](https://zenodo.org/records/20412587), cumulative German/English and multilingual reader PDFs first |
| Bianchi | [Bianchi record](https://zenodo.org/records/20615949), English or Italian Vol. I reader first; use the ZIP for TeX/source witnesses and audit ledgers |
| Gordan / Clebsch-Gordan | [Gordan record](https://zenodo.org/records/20617548), open the relevant package ZIP; PDFs, TeX, source witnesses, and audit ledgers are inside |
| Classical algebra/arithmetic | [Classical algebra and arithmetic record](https://zenodo.org/records/20418609), numbered reader PDFs by author |

If you want usable mathematical text rather than repair evidence, prefer top-level PDFs and files named `reader`, `working_draft`, `source_checked`, or `cumulative`. Treat files named `OCR_candidate`, `formula_witness`, `crop_witness`, or `locator_aid` as checking aids.

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
- `working_draft`, `source_checked`, `reader`, or `cumulative` means compiled TeX/PDF promoted to a declared draft layer.

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
