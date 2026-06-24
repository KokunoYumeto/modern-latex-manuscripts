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
| Weber | [Weber record](https://doi.org/10.5281/zenodo.20412153), Volume I first; Volume II readers plus recursive repair packets through public Batch132. Local staging has Batch137 queued as the newest active-ledger closure/bulk-audit packet, reporting the active 112-row ledger at 112/112 closed, plus Batch138 as a focused post-closure Volume II section 6 control-character footnote fix and B139 as a focused Volume II English section 49 merged-tag repair; none of these local packages are public Zenodo files until upload succeeds. |
| Noether | [Noether record](https://doi.org/10.5281/zenodo.20412587), cumulative reader PDFs and standalone English paper PDFs first; ZIPs contain TeX/source packages and active Paper 02/Paper 04 source-audit correction packets. Locally staged German source-audit support ZIPs plus Paper 03/Paper 11/Paper 12/Paper 13 GDZ source/provenance witnesses, Paper 10/Paper 11/Paper 12 compact GDZ source-audit webdrops, the P12/P13 RA48 targeted applied-fix candidate, the P18 RA51 targeted resultant-display candidate, the P20 RA49 targeted formula (13) candidate, the P19 RA50 targeted tail-correction candidate, Paper 05, Paper 06, Paper 07, Paper 08, Paper 14, Paper 15, Paper 16, Paper 17, Paper 18, Paper 19, Paper 20, RA69-RA75 source-apparatus/source-text repair candidates, Paper 33 IA source-witness provenance support, and RA43-RA48 Paper 06 web drops add RA/source ledgers, high-DPI witnesses, OCR/Markdown locator material, Paper 08/Paper 15/Paper 16/Paper 17/Paper 18/Paper 19/Paper 20 math/source corrections, Paper 10/Paper 11/Paper 12 patch targets/no-fix traps, targeted P12/P13/P18/P19/P20 source-backed German candidate repairs, Paper 14 unpatched source-audit results, and Paper 06-08 source-style footnote-marker issues, but are not public Zenodo files until the next upload succeeds. |
| Bianchi | [Bianchi record](https://doi.org/10.5281/zenodo.20615814), English or Italian Vol. I reader first; for A2 use the public `Bianchi_A2_core_p0001_0135_IT_EN_20260613.zip` as the latest cataloged compact/core working package through p0135, with older scan-heavy p0105 and repair ZIPs retained as provenance/support layers. A smaller same-name Edge re-export exists locally under a disambiguated pending filename and should not be cited until a new Zenodo version publishes it. |
| Gordan / Clebsch-Gordan | [Gordan record](https://doi.org/10.5281/zenodo.20616260), use the 2026-06-24 files for theta fix06, Abelsche FinalAuditFix02, De linea p001-p047, and Vorlesungen Bd.1 p001-p028. Earlier Abel and AllPrior/auditfix packages cover earlier branches or provenance. PDFs, TeX, source witnesses, render checks, and audit ledgers are inside the ZIPs. |
| Frobenius | [Frobenius record](https://doi.org/10.5281/zenodo.20673444), open the latest RA05 cumulative German/English reader PDFs or RA05 ZIP for the selected group-character working draft, directly compilable TeX, source scans, and audit refresh. |
| Poincare | [Poincare record](https://doi.org/10.5281/zenodo.20673461), use `poincare_v1_*` packages individually; this is a non-continuous recovery stream, not a seamless Tome I edition. |
| Maxwell / old physics | [Maxwell record](https://doi.org/10.5281/zenodo.20653107), use the source-witnessed Volume I working-tranche ZIPs and IA master-image source-index helper. Local staging has a pp.001-059 web/promo closeout ZIP and a pp.060-079 continuation ZIP queued, extending local cumulative staging to pp.001-079, plus separate IA 500ppi/raw JP2 and metadata/PDF/OCR source supplements. These are not public Zenodo files until upload succeeds; the source supplements are provenance/witness material, not new reader coverage. Gibbs old-physics now has the p125-134 continuation published on its own Gibbs record. |
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

