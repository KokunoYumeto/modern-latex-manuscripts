# Download Guide

Use this page when you know what you want to do, but not which file type to choose.

None of the records should be treated as a certified critical edition unless a later release explicitly says the maintainer has certified that status. Current files are working drafts, translation drafts, source-witnessed tranches, OCR/witness layers, or provenance packets. Older filenames can contain words such as `Complete`, `Strict`, `Source-Checked`, or `Critical`; use the record status notes rather than the filename alone.

## I Want To Read Something

Download or preview the top-level PDF files first.

Good starting points:

| Interest | Start With |
|---|---|
| Noether | [Noether record](https://doi.org/10.5281/zenodo.20412587), latest public version [10.5281/zenodo.21426158](https://doi.org/10.5281/zenodo.21426158). Open the default 466-page German Paper 30 audited working reader for the newest source-control state; the 473-page Spanish or 494-page French PDFs for those language branches; the 529/552-page PDFs for Interslavic; the one-page Indonesian Paper 36 PDF; or the eight direct CJK PDFs for complete Papers 26/36. File `15` carries the Paper 30 corrected TeX, exact diff, direct source slice, enlarged witnesses, build evidence, and audit status; file `14` carries the exact French TeX/evidence closure. Existing translations are not silently represented as synchronized to the newest German patch. Treat compilation and audit packets as evidence, not universal synchronization, native/community certification, complete Paper 30 or whole-corpus certification, paper-by-paper mathematical certification, or critical-edition status. |
| Weber | [Weber record](https://doi.org/10.5281/zenodo.20412153), latest public version [10.5281/zenodo.21402223](https://doi.org/10.5281/zenodo.21402223). Open the current German Volume I p88 workpass first; its grouped ZIP carries TeX, ledgers, exact diff, source pages/crops, and render checks. The English Volume I PDF predates the latest German repairs. Volume II readers run through §176; Volume III remains available. |
| Strongest compact reader surfaces | [Frobenius](https://doi.org/10.5281/zenodo.20673444), [Kneser](https://doi.org/10.5281/zenodo.20836971), [Sylvester](https://doi.org/10.5281/zenodo.20520692), and [al-Battani](https://doi.org/10.5281/zenodo.20539593) are usually better first reads than the raw/mixed shelves. |
| SGA | [SGA record](https://doi.org/10.5281/zenodo.20410947), current version [10.5281/zenodo.21427899](https://doi.org/10.5281/zenodo.21427899). Open the 309-page SGA5 English working translation or the 296-page Spanish SGA5 source-reconciled working reader with 345 editable units through Exposé XV §2 no.1 and Proposition 1, then the corrected 381-page SGA6 full-range layered English reader. File `06` carries the SGA6 English editable TeX, authority/formula/terminology/page ledgers, build evidence, all-page renders, contact sheets, prefix-repair and correction evidence, hashes, and validation; file `07` carries the Spanish SGA5 TeX and evidence. The 374-page French SGA6 idx684 checkpoint and four-page Spanish SGA6 Exposé X idx532-537 tranche remain available. These are serious working translations and source-repair checkpoints, not critical editions, uniform whole-volume source certification, native-language certification, or whole-SGA completion. |
| Non-European mathematics | [Non-European consolidated record](https://doi.org/10.5281/zenodo.20410957), index/readers first, then work-level and source ZIPs |
| Bianchi | [Bianchi record](https://doi.org/10.5281/zenodo.20615814), English or Italian Vol. I reader first; for A2 use the public `Bianchi_A2_core_p0001_0135_IT_EN_20260613.zip` as the latest cataloged compact/core working package through p0135, with older scan-heavy p0105 and repair ZIPs retained as provenance/support layers. A smaller same-name Edge re-export exists locally under a disambiguated pending filename and should not be cited until a new Zenodo version publishes it. |
| Gordan / Clebsch-Gordan | [Gordan record](https://doi.org/10.5281/zenodo.20616260), use the 2026-06-24 files for theta fix06, Abelsche FinalAuditFix02, De linea p001-p047, and Vorlesungen Bd.1 p001-p028. Earlier Abel and AllPrior/auditfix packages cover earlier branches or provenance. PDFs, TeX, source witnesses, render checks, and audit ledgers are inside the ZIPs. |
| Frobenius | [Frobenius record](https://doi.org/10.5281/zenodo.20673444), open the latest RA05 cumulative German/English reader PDFs or RA05 ZIP for the selected group-character working draft, directly compilable TeX, source scans, and audit refresh. |
| Poincare | [Poincare record](https://doi.org/10.5281/zenodo.20673461), use `poincare_v1_*` packages individually; this is a non-continuous recovery stream, not a seamless Tome I edition. |
| Maxwell / old physics | [Maxwell record](https://doi.org/10.5281/zenodo.20653107), latest version [10.5281/zenodo.20821947](https://doi.org/10.5281/zenodo.20821947), with source-witnessed Volume I working-tranche ZIPs public through pp.001-079. Use the status/readme files inside the ZIPs; separate `Maxwell_WebPromo_MISSING_*` source/provenance supplements are still pending and are not reader coverage. |
| Kneser | [Dedicated Kneser record](https://doi.org/10.5281/zenodo.20836971), open the English working reader first, then the German source reader and HQ source witness. Current public surface runs through p0011-p0248 with p0234 lower-p0248 audit package; older mixed-shelf Kneser packets remain provenance/backstop. |
| Classical algebra/arithmetic | [Classical algebra and arithmetic record](https://doi.org/10.5281/zenodo.20414787), numbered reader PDFs by author; inherited Cayley `source_checked` filenames are de-promoted unless re-promoted by a later source audit |
| EGA / Cayley support lanes | [EGA](https://doi.org/10.5281/zenodo.20414353) and [Cayley](https://doi.org/10.5281/zenodo.20520749) should be opened as preservation, OCR, draft, or salvage records rather than as source-audited reader editions. |

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
