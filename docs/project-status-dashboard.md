# Project Status Dashboard

Generated from the current public Zenodo catalog and local mirror manifests. For the latest local staging and caveats, use the [current status manifest](../manifests/current-status.md).

## Reader Priority And Quality

Open the records in this order if the goal is to find useful mathematics quickly. This is intentionally not ordered by file count, local package count, or the age of the record.

| Priority | Records | Reader Surface | Source-Audit / Caveat |
|---|---|---|---|
| 1. Coherent reader/translation surfaces | Noether, Weber, Frobenius, Kneser, Sylvester, al-Battani | Top-level PDFs or declared work-level readers exist for a named scope. | Still working scholarly drafts; Noether/Weber remain active source-reconciliation lanes rather than critical editions. |
| 2. Serious source-aware work, caveat-heavy | Bianchi, Gordan, Steinitz, Gibbs, Maxwell, SGA, Deligne, Ukrainian applied mathematics, non-European/Chinese/Indian/Islamic records | Real reader, translation, data/table, or source-audit surfaces exist. | Range quality varies; diagrams, tables, page-local source closure, and language synchronization must be checked. |
| 3. Partial author records and non-continuous streams | Dedekind, Dirichlet, Gauss, Riemann, Poincare, mixed classical shelves | Useful packages exist. | Read package-by-package; do not treat these as seamless author-complete editions. |
| 4. Source-intake/OCR/support/provenance or unsafe draft lanes | EGA, Cayley, Galois source staging, raw landing material | Preservation, OCR, salvage, source intake, or future continuation support. | EGA is mostly French-original/OCR/partial draft support. Cayley is de-promoted until exact page ranges are re-audited and re-promoted. Galois has source masters and locator witnesses only, not a reader release. |

The SGA/EGA distinction matters. SGA has substantial real SGA5 repair and SGA6/SGA7 working-translation material under caveat. EGA is currently a support/stub lane: useful French originals plus partial OCR/English draft material, but not a comparable source-audited working edition.

## Archive Surface

These counts describe the public file surface. They are useful for release hygiene, but they are not progress bars and do not measure mathematical correctness.

| Metric | Current Count |
|---|---:|
| Public records tracked here | 30 |
| Public files indexed | 1108 |
| Top-level PDFs | 555 |
| Artifact/source ZIPs | 459 |
| Manifest/status files | 86 |
| Total public file surface | 39.01 GB |

The top-level PDFs are the reading surface. ZIPs preserve TeX, source scans or references, provenance, audits, OCR, component files, and other material needed to continue the work.

Quality rule: the dashboard counts public files and working coverage, not critical-edition status. No record here is a certified critical edition unless a future release explicitly says so. Filename terms such as `Complete`, `Strict`, `Source-Checked`, or `Critical` can be legacy labels or scoped working labels; record caveats and source witnesses govern reliability.

Latest Noether local queue hygiene: R527 is the current clean packaged local TeX-changing German source-control candidate after the R523-R527 Paper 24 repair chain. WebB R497 is separately registered as a TeX-changing tail/Kapferer source-control provenance artifact, distinct from the local R497 no-patch Paper 22 survival guardrail; R285 is registered as P08/P10/P13/P15/P19 source-merge provenance and workflow evidence, not as a base replacement. The second-web intake fronts R527 as a source/state handoff, not as a reader release. Older R/RA/source-support packets remain anti-regression and source-evidence layers and should be folded into compact rollups rather than treated as standalone paper certification.

Latest Noether source-support hygiene: the current public-facing rule is reader PDFs and compact current source-control packages first; micro-ZIPs, support witnesses, OCR, and no-patch survival packets stay behind those as evidence. Noether remains a high-value working corpus with active German/source reconciliation, not whole-corpus closure, page-by-page certification, multilingual synchronization, or a critical edition.

## How To Read Coverage

Do not read file counts, upload size, or a local page percentage as a simple progress bar. The public question is: what can a reader responsibly use today?

| Coverage Tier | Meaning | Examples |
|---|---|---|
| Coherent reader/translation surface | A named work, selected corpus, or large continuous tranche has reader PDFs and TeX that are meant to be opened first. | Noether, Weber, Frobenius, Kneser, Sylvester, al-Battani. |
| Serious source-aware working lane | Real repair/source-audit/translation work exists, but reliability changes by page range or object type. | SGA, Deligne, Bianchi, Gordan, Steinitz, Gibbs, Maxwell, non-European records. |
| Partial or non-continuous stream | Useful packages exist, but the record is not a seamless author edition. | Dedekind, Dirichlet, Gauss, Riemann, Poincare, mixed shelves. |
| Support, OCR, salvage, source intake, or provenance | Material is retained because it helps future work, not because it is a promoted reading edition. | EGA, Cayley, Galois source staging, raw landing/provenance bundles. |

When these tiers conflict with an older filename such as `complete`, `strict`, `source-checked`, or `critical`, the tier and the current caveat win. Cayley is currently de-promoted repair/provenance material. EGA is OCR/original/draft support. SGA is substantially more real than EGA, but still not complete or globally source-faithful.

## Current Records

Records are grouped by public usefulness and source-confidence, not by creation date, file count, upload size, or internal maintenance importance. A high file count is not a progress bar and does not imply a high source-accuracy tier. The best reader/translation surfaces come first; project-level preservation and workflow records follow after the reader-facing surfaces.

| Record | Files | PDFs | ZIPs | Size | State |
|---|---:|---:|---:|---:|---|
| **Best current reader/translation surfaces** |  |  |  |  |  |
| [Noether](https://doi.org/10.5281/zenodo.20412587) | 100 | 50 | 37 | 2.06 GB | Reader-facing first: cumulative German/English readers, 43 standalone English paper PDFs, compact German/source and multilingual packages, plus active German/source-audit control layers. Current clean packaged local TeX-changing source-control candidate is R527: the active chain includes R496 post-P43 tail/Schur fixes, WebB R497 tail/Kapferer hard-source provenance, R504 Paper 14 source-backed fixes, R507 a tail display-punctuation fix, R516/R518/R519/R520/R521/R522/R523/R524/R525/R526/R527 Paper 24 source-control repairs, and R285 P08/P10/P13/P15/P19 provenance/workflow evidence. R508-R515 and R517 are support/no-patch/source-quality/visual-audit packets, not new TeX heads. This remains a working corpus/source-control lane, not whole-corpus closure, page-by-page certification, multilingual synchronization, or a critical edition. |
| [Weber](https://doi.org/10.5281/zenodo.20412153) | 54 | 8 | 38 | 1486.86 MB | `Lehrbuch der Algebra` Volume I represented as repaired but still under source-audit correction; Volume II readers through §176 plus recursive repair packets; Volume III current repaired cumulative. Latest public version <https://doi.org/10.5281/zenodo.20837104> adds Batch137, Batch138, and B139. New local pending Weber material includes B140-B145, the p648 content-map closure status package, and a Phase 2 status package accepting coherent German re-transcriptions for §141 and §162. Remaining held ranges include §69, §138 numbering/layout, p466, §§148-156, §158, §163, §165, §§167-170, and §§173-188; not English synchronized and not a certified critical edition. |
| [Frobenius](https://doi.org/10.5281/zenodo.20673444) | 8 | 2 | 2 | 333.59 MB | Dedicated selected group-character German/English working package. Latest public record 20821858 adds RA05, top-level German/English cumulative PDF/TeX readers, English item 070 formula-punctuation fixes, directly compilable cumulative TeX/PDF, verified extraction, and zero reported post-fix structural/formula/build flags. |
| [Adolf Kneser](https://doi.org/10.5281/zenodo.20836971) | 8 | 3 | 1 | 116.74 MB | Dedicated `Lehrbuch der Variationsrechnung` German-source and English working-translation record through p0011-p0248, with HQ source witness through p0001-p0248 and the p0234 lower-p0248 slice/audit package. Worklist reports 248/336 source pages done (73.8%), latest slice §§53-55 completing the Sixth Section, next p0249 / Seventh Section / §56. Not a certified critical edition. |
| [Sylvester](https://doi.org/10.5281/zenodo.20520692) | 3 | 1 | 1 | 91 MB | Sylvester Volume I source-witnessed working draft through book page 608; Papers 59-60 are represented in the latest tranche, next continuation p.609. |
| [al-Battani](https://doi.org/10.5281/zenodo.20539593) | 19 | 7 | 4 | 318 MB | Opus Astronomicum working edition with complete trilingual text over 100 segments, complete fixed-star catalogue data (485 stars), complete geography gazetteer (269 localities), chronology framework/canon partial, and zodiac auxiliary tables documented as not cleanly present in Nallino's Latin table source. Legacy `Complete Critical Edition` catalogue filename is not a certified critical-edition claim. |
| **Serious source-aware work, but caveat-heavy** |  |  |  |  |  |
| [SGA](https://doi.org/10.5281/zenodo.20410947) | 100 | 74 | 25 | 3.23 GB | SGA 5/6 and further SGA working translation material, plus source/reference and audit packets. Latest compact promoted SGA5 delta remains p260-p265, but later live ledger/provenance now records the local SGA5 workpass through p360 in `AGENT_SCORECARD.md`. Exposé VIII has started; p352 records fix #33, p355 records fix #34 in the `K(F)` formula, and diagrams are tracked through D174. Treat p266-p360 as live workpass/provenance metadata only, not a compact promoted public delta, not SGA5 completion, not synchronized English, not a critical edition, and not global source-faithfulness. SGA6 is substantial but not complete: a June 11 audit found 127/524 sampled source prose windows, about 24%, missing from current TeX in late regions. SGA7-I is still partial starter work. Corrections are welcome via GitHub issues or pull requests. |
| [Deligne](https://doi.org/10.5281/zenodo.20410853) | 100 | 96 | 3 | 448 MB | Mixed Deligne papers/letters drafts plus the refreshed `2026-06-09 v3` repair/math-audit packet containing D001-D017 witness material, D001-D017 equation-dense audit material, D074-D090 descending triage, and D074-D090 math-audit repairpass1; diagram-heavy material remains uneven and source-crop sensitive. |
| [Luigi Bianchi](https://doi.org/10.5281/zenodo.20615814) | 22 | 5 | 12 | 1.92 GB | `Lezioni di geometria differenziale` Vol. I represented through source pdfpages 001-543; A2 latest public compact/core package `Bianchi_A2_core_p0001_0135_IT_EN_20260613.zip` extends working coverage through source p0135 while earlier large scan-heavy p0105 packages remain provenance/backstop. Loose p0135 Italian/English reader PDFs/TeX and the p0121-p0135 source witness are queued as reader-convenience/fronting files, not new content. |
| [Paul Gordan and Clebsch-Gordan](https://doi.org/10.5281/zenodo.20616260) | 45 | 0 | 39 | 1.83 GB | Dedicated package set now includes Abel27, Abelsche FinalAuditFix02, `De linea geodetica` p001-p047, theta fix06, and `Vorlesungen ueber Invariantentheorie` Bd. 1 p001-p028 on the latest 2026-06-24 version DOI `10.5281/zenodo.20822196`, which also adds the compact project-control/status update. Working/source-audit drafts only, not a certified critical edition. |
| [Ernst Steinitz](https://doi.org/10.5281/zenodo.20616988) | 7 | 0 | 6 | 439.58 MB | Dedicated package-audited German/English working packets for 1910 fields sections 1-24, 1913 Bedingt I complete, strict 1894/1897/1906 early works, 1914 Bedingt II complete, and 1916 Bedingt III started through pp.1-13. A 2026-06-28 exact-name follow-up resolves recent local misses as source-backfill/support or superseded lineage, not loose uploads; continue Bedingt III from p14, and keep 1908 Analysis Situs as the major source-gap/provisional-witness caveat. |
| [Gibbs / old physics](https://doi.org/10.5281/zenodo.20649835) | 10 | 3 | 3 | 18.6 MB | `The Scientific Papers of J. Willard Gibbs`, Volume I source-scan-backed public working tranche through printed pp.001-134. The current version includes `GibbsV1_P3_p125_134.zip` plus reader-facing cumulative Paper 3 PDF/TeX for pp.055-134, with clean compile QC and formula/table/scan-map ledgers. Local source-quality refresh adds IA raw JP2/scandata sources for future continuation. Not a complete Gibbs corpus or final critical edition. |
| [Maxwell](https://doi.org/10.5281/zenodo.20653107) | 9 | 0 | 7 | 700.61 MB | `A Treatise on Electricity and Magnetism`, Volume I source-witnessed working tranches. Latest public version <https://doi.org/10.5281/zenodo.20821947> adds the pp.001-059 web/promo index closeout and pp.060-079 continuation ZIPs, so the compact IA 1873 first-edition source-witnessed sequence is public through printed pp.001-079 (79/467 pages, 16.9%). Earlier ledger-backed book pages 95-101, 103, 105, 109, and continuous pp.111-267 remain in the record. Continue at printed p.080 / IA leaf 118. |
| [Ukrainian applied mathematics](https://doi.org/10.5281/zenodo.20490906) | 19 | 18 | 1 | 13 MB | Applied mathematics and engineering translation/readers. |
| [Non-European consolidated](https://doi.org/10.5281/zenodo.20410957) | 100 | 71 | 24 | 3.10 GB | Combined multilingual release, work-level readers, and raw provenance archive. |
| [Chinese classics](https://doi.org/10.5281/zenodo.20415751) | 30 | 28 | 1 | 99 MB | Current Chinese mathematical classics shelf. |
| [Indian and Sanskrit classics](https://doi.org/10.5281/zenodo.20415754) | 13 | 11 | 1 | 549 MB | Current Indian/Sanskrit mathematical classics shelf. |
| [Islamic and Arabic texts](https://doi.org/10.5281/zenodo.20415769) | 19 | 17 | 1 | 46 MB | Current Islamic/Arabic mathematical texts shelf. |
| **Partial author records, non-continuous streams, and mixed shelves** |  |  |  |  |  |
| [Dedekind](https://doi.org/10.5281/zenodo.20520669) | 18 | 14 | 3 | 25 MB | Dedekind source-witnessed working drafts and English translations. |
| [Dirichlet](https://doi.org/10.5281/zenodo.20520679) | 7 | 2 | 4 | 168 MB | Dirichlet source-witnessed working drafts and English translations. |
| [Gauss](https://doi.org/10.5281/zenodo.20410934) | 26 | 14 | 10 | 1.30 GB | Gauss Werke modern-LaTeX working drafts, source packets, and repair/transcription starts; latest R38 package continues Band II through printed p.312 with p.313 only as a preview/handoff scan. Local source-quality audit says future Gauss work should use the coherent GDZ Werke PDFs plus IIIF manifests for Bands I-XII, while older broad reader PDFs remain unsafe unless individually re-audited. |
| [Riemann](https://doi.org/10.5281/zenodo.20429778) | 4 | 2 | 2 | 52.3 MB | Selected-papers and broader Gesammelte Werke working-draft readers with matching TeX/source/provenance artifacts. Not a certified critical edition. |
| [Poincare](https://doi.org/10.5281/zenodo.20673461) | 20 | 0 | 19 | 2401.61 MB | Dedicated `Oeuvres`, Tome I working package stream through public `poincare_v1_26.zip`; explicitly non-continuous. Local Edge sweep recovered and queued a v1_03/v1_04/v1_05/v1_07 gap-fill rollup; v1_06 and v1_22-v1_23 remain absent by this sweep. |
| [Historical reference witnesses](https://doi.org/10.5281/zenodo.20415776) | 15 | 13 | 1 | 59 MB | Current reference-witness shelf. |
| [Classical algebra and arithmetic](https://doi.org/10.5281/zenodo.20414787) | 25 | 21 | 3 | 6.72 GB | Organized shelf for selected classical algebra/arithmetic drafts, including large provenance bundles. |
| [Additional author cluster](https://doi.org/10.5281/zenodo.20411006) | 100 | 10 | 88 | 5.60 GB | Mixed backstop/provenance shelf for routed authors not yet split into full records. Kneser, Poincare, and Frobenius now have preferred standalone records; older Kneser packets here remain provenance/backstop. |
| **Project-level orientation and preservation** |  |  |  |  |  |
| [Main project landing](https://doi.org/10.5281/zenodo.20393488) | 100 | 58 | 38 | 4.41 GB | Current bulk preservation and project map. Open this for raw provenance, not as the first reader surface. |
| [Workflow / replication packet](https://doi.org/10.5281/zenodo.20461174) | 23 | 3 | 11 | 0.45 MB | Latest workflow refresh published as <https://doi.org/10.5281/zenodo.20836364>. Adds archive-scope guardrails, source-witness/public-surface labels, audit harnesses, source inventory/page-object manifest patterns, OCR-as-locator guidance, and local/web handoff lessons. New queued GitHub-side workflow artifacts add an SGA6 page-unit harness and a Weber live audit method snapshot through p527; these remain support evidence, not edition certification. |
| **Source-intake-only, OCR/support/provenance, or currently unsafe draft lanes** |  |  |  |  |  |
| [EGA](https://doi.org/10.5281/zenodo.20414353) | 16 | 10 | 4 | 472 MB | French originals plus partial English/OCR/draft continuation support. The cleaner local EGA support package contains NUMDAM scan PDFs, NUMDAM OAI metadata, and upstream/community `ryankeleti/ega` TeX; NUMDAM OAI is metadata only, and the community TeX is real but incomplete, especially EGA III/IV and parts of EGA 0_IV. Useful preservation and continuation material, not a source-audited working edition comparable to the active SGA lane. |
| [Cayley](https://doi.org/10.5281/zenodo.20520749) | 84 | 13 | 69 | 1.17 GB | Provenance/repair material. A 2026-06-28 exact-name follow-up triages 308 local Cayley names as quarantine/source-intake evidence, including page micro-ZIPs, unitized indexes, suspect Vol. I chunks, Pro salvage extracts, and source scans. No Cayley range is presently promoted as source-faithful, including the v2/restart Vol. I packets, until a future page-by-page glyph/source audit explicitly re-promotes exact ranges. |

## Completion Read

The project is best read as a live corpus rather than a finished edition. The numbers below describe the current archive surface, not final scholarly proof status.

| Area | Current Status | Plain-English Meaning |
|---|---|---|
| Preservation and discoverability | Current preservation surface | Current public records are indexed, linked, and mirrored in local manifests. This says the archive is findable, not that the mathematics is proofread. |
| Zenodo presentation hygiene | Strong but caveat-sensitive | Current records have human titles and configured metadata/filename checks, but record descriptions still need periodic review as audit evidence changes. |
| PDF technical surface | Technically healthy in last audit | The latest local public PDF surface audit checked 356 PDFs with no configured defect flags; this is a file/render check, not a mathematical correctness check. |
| Source/provenance availability | Broad but uneven | Most records include artifact ZIPs with TeX, sources, or checking material; quality and usefulness vary by author lane. |
| Human browseability | Improved, still noisy | The dashboard, browse index, download guide, author/work index, record landing pages, and file catalog make the archive navigable; some older shelves remain provenance-heavy and need continued pruning/fronting. |
| Mathematical/source proofreading | Early and uneven | Many drafts still need page-by-page checking against source witnesses; no record is currently treated as critically certified by default. |
| Reader/translation coverage | Substantial but uneven | Several corpora have substantial reader or translation surfaces, but status differs sharply: Noether/Weber/SGA/al-Battani and several author records have real working editions, while EGA, Cayley, and mixed shelves are mostly partial, OCR/support, or repair-provenance lanes. |

## Most Useful Next Work

1. Continue source comparison for the best current top-level PDFs and repair obvious layout problems.
2. Expand author-level records when an author or corpus becomes coherent enough to stand alone.
3. Keep the main landing record as a complete preservation layer, while making topic and author records the preferred public browsing surface.
4. Use the artifact ZIPs for ongoing TeX and translation repair rather than editing from PDFs alone.
5. Re-run the public metadata and PDF-surface audits after each public refresh.

## Current Audit Notes

The latest record-map consistency checks on 2026-06-24 verify that the generated record pages, public file catalog, Zenodo record map, and machine-readable record manifest agree on 30 current public records.

The older local public PDF surface audit checked 356 public PDFs at 2026-05-28 00:09:01 and reported zero configured defect flags. SGA 5, SGA 6, SGA 7-I, and SGA 7-II French reference PDFs are intentionally image-based scans, so low embedded text extraction is expected for those files.
