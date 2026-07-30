# Download Guide

Use this page when you know what you want to do, but not which file type to choose.

None of the records should be treated as a certified critical edition unless a later release explicitly says the maintainer has certified that status. Current files are working drafts, translation drafts, source-witnessed tranches, OCR/witness layers, or provenance packets. Older filenames can contain words such as `Complete`, `Strict`, `Source-Checked`, or `Critical`; use the record status notes rather than the filename alone.

## I Want To Read Something

Download or preview the top-level PDF files first.

Good starting points:

| Interest | Start With |
|---|---|
| Noether | [Noether record](https://doi.org/10.5281/zenodo.20412587), current compact version [10.5281/zenodo.21499660](https://doi.org/10.5281/zenodo.21499660). Open the default 459-page full cumulative English working reader or its directly exposed master TeX first. German, Spanish, French, and paired Interslavic readers also remain direct downloads. Nine coherent ZIPs group bounded CJK and other-language work, current source-control material, repair evidence, visual evidence, and predecessor maps. All 20 public files and all 3,979 ZIP members passed anonymous byte-for-byte readback. Treat the corpus and evidence as working translation/source-control material, not universal synchronization, native/community certification, whole-corpus source certification, accessibility certification, rights clearance, or a critical edition. |
| Weber | [Weber record](https://doi.org/10.5281/zenodo.20412153), latest public version [10.5281/zenodo.21513712](https://doi.org/10.5281/zenodo.21513712). Open the current German Volume I p88 workpass first as readable modernized/summarized working material. Two high-detail audit-crop ZIPs preserve 248 page-mapped tight crops and 846 recovered formula/glyph/detail images; their manifests record exact hashes and honest locator status. The English Volume I PDF predates the latest German repairs. Volume II reaches §176; Volume III is an incomplete repaired cumulative, not a finished v3. All three volumes are incomplete, and neither the readers nor crop evidence are source-critical certification; SGA's bounded source-audit work is substantially closer to source. |
| Strongest compact reader surfaces | [Frobenius](https://doi.org/10.5281/zenodo.20673444), [Kneser](https://doi.org/10.5281/zenodo.20836971), [Sylvester](https://doi.org/10.5281/zenodo.20520692), and [al-Battani](https://doi.org/10.5281/zenodo.20539593) are usually better first reads than the raw/mixed shelves. |
| SGA | [SGA record](https://doi.org/10.5281/zenodo.20410947), current version [10.5281/zenodo.21702669](https://doi.org/10.5281/zenodo.21702669). Download the leading `00_Current_SGA1-6_English_Readers_and_Buildable_TeX_20260730.zip` once for all six cumulative reader PDFs and their complete TeX closures, or open direct PDFs `00a` through `00f`. SGA1 remains the default preview. The new 1,394-member ZIP and all 66 retained predecessor files passed anonymous readback. SGA3 remains a heterogeneous working integration rather than final diagram-fidelity closure; SGA4half remains rights-held; SGA6 remains layered. |
| Non-European mathematics | [Non-European consolidated record](https://doi.org/10.5281/zenodo.20410957), index/readers first, then work-level and source ZIPs |
| Bianchi | [Bianchi record](https://doi.org/10.5281/zenodo.20615814), English or Italian Vol. I reader first; for A2 use the public `Bianchi_A2_core_p0001_0135_IT_EN_20260613.zip` as the latest cataloged compact/core working package through p0135, with older scan-heavy p0105 and repair ZIPs retained as provenance/support layers. A smaller same-name Edge re-export exists locally under a disambiguated pending filename and should not be cited until a new Zenodo version publishes it. |
| Gordan / Clebsch-Gordan | [Gordan record](https://doi.org/10.5281/zenodo.20616260), use the 2026-06-24 files for theta fix06, Abelsche FinalAuditFix02, De linea p001-p047, and Vorlesungen Bd.1 p001-p028. Earlier Abel and AllPrior/auditfix packages cover earlier branches or provenance. PDFs, TeX, source witnesses, render checks, and audit ledgers are inside the ZIPs. |
| Frobenius | [Frobenius record](https://doi.org/10.5281/zenodo.20673444), open the latest RA05 cumulative German/English reader PDFs or RA05 ZIP for the selected group-character working draft, directly compilable TeX, source scans, and audit refresh. |
| Poincare | [Poincare record](https://doi.org/10.5281/zenodo.20673461), use `poincare_v1_*` packages individually; this is a non-continuous recovery stream, not a seamless Tome I edition. |
| Maxwell / old physics | [Maxwell record](https://doi.org/10.5281/zenodo.20653107), latest version [10.5281/zenodo.20821947](https://doi.org/10.5281/zenodo.20821947), with source-witnessed Volume I working-tranche ZIPs public through pp.001-079. Use the status/readme files inside the ZIPs; separate `Maxwell_WebPromo_MISSING_*` source/provenance supplements are still pending and are not reader coverage. |
| Kneser | [Dedicated Kneser record](https://doi.org/10.5281/zenodo.20836971), open the English working reader first, then the German source reader and HQ source witness. Current public surface runs through p0011-p0248 with p0234 lower-p0248 audit package; older mixed-shelf Kneser packets remain provenance/backstop. |
| Classical algebra/arithmetic | [Classical algebra and arithmetic record](https://doi.org/10.5281/zenodo.20414787), numbered reader PDFs by author; inherited Cayley `source_checked` filenames are de-promoted unless re-promoted by a later source audit |
| EGA working and support lanes | [EGA current version](https://doi.org/10.5281/zenodo.21702700) begins with one 99-member clean ZIP containing one cumulative reader PDF and complete TeX closure for every current EGA scope. EGA0 remains the record preview; EGA II is complete for its stated source-aligned scope, while EGA0, EGA III, EGA IV, and the wider corpus remain partial or non-uniform. |
| Cayley support lane | [Cayley](https://doi.org/10.5281/zenodo.20520749) should be opened as preservation, OCR, draft, or salvage material rather than as a source-audited reader edition. |

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
