# Project Status Dashboard

Generated from the current public Zenodo catalog and local mirror manifests. For the latest local staging and caveats, use the [current status manifest](../manifests/current-status.md).

## Archive Surface

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

Latest Noether local queue hygiene: R128 P09/P10 Batch25 survival packages now record that current Paper 09 and Paper 10 spans are byte-identical to earlier rebuilt/source-backed spans, with no TeX patches. They are anti-regression/stale-queue controls only and should be folded into a compact Noether rollup rather than treated as standalone paper certification.

## Reader Priority And Quality

Open the records in this order if the goal is to find useful mathematics quickly. This is intentionally not ordered by file count, local package count, or the age of the record.

| Priority | Records | Reader Surface | Source-Audit / Caveat |
|---|---|---|---|
| 1. Coherent reader/translation surfaces | Noether, Weber, Frobenius, Kneser, Sylvester, al-Battani | Top-level PDFs or declared work-level readers exist for a named scope. | Still working scholarly drafts; Noether/Weber remain active source-reconciliation lanes rather than critical editions. |
| 2. Serious source-aware work, caveat-heavy | SGA, Deligne, Bianchi, Gordan, Steinitz, Gibbs, Maxwell, Ukrainian applied mathematics, non-European/Chinese/Indian/Islamic records | Real reader, translation, data/table, or source-audit surfaces exist. | Range quality varies; diagrams, tables, page-local source closure, and language synchronization must be checked. |
| 3. Partial author records and non-continuous streams | Dedekind, Dirichlet, Gauss, Riemann, Poincare, mixed classical shelves | Useful packages exist. | Read package-by-package; do not treat these as seamless author-complete editions. |
| 4. OCR/support/provenance or unsafe draft lanes | EGA, Cayley, raw landing material | Preservation, OCR, salvage, or future continuation support. | EGA is mostly French-original/OCR/partial draft support. Cayley is de-promoted until exact page ranges are re-audited and re-promoted. |

The SGA/EGA distinction matters. SGA has substantial real SGA5 repair and SGA6/SGA7 working-translation material under caveat. EGA is currently a support/stub lane: useful French originals plus partial OCR/English draft material, but not a comparable source-audited working edition.

## Current Records

The two project-level records are listed first for orientation and preservation. After that, records are grouped by public usefulness and source-confidence, not by creation date, file count, or upload size. A high file count is not a progress bar and does not imply a high source-accuracy tier.

| Record | Files | PDFs | ZIPs | Size | State |
|---|---:|---:|---:|---:|---|
| **Project-level orientation and preservation** |  |  |  |  |  |
| [Main project landing](https://doi.org/10.5281/zenodo.20393488) | 100 | 58 | 38 | 4.41 GB | Current bulk preservation and project map. |
| [Workflow / replication packet](https://doi.org/10.5281/zenodo.20461174) | 23 | 3 | 11 | 0.45 MB | Latest workflow refresh published as <https://doi.org/10.5281/zenodo.20836364>. Adds archive-scope guardrails, source-witness/public-surface labels, audit harnesses, source inventory/page-object manifest patterns, OCR-as-locator guidance, and local/web handoff lessons. New queued GitHub-side workflow artifacts add an SGA6 page-unit harness and a Weber live audit method snapshot through p527; these remain support evidence, not edition certification. |
| **Best current reader/translation surfaces** |  |  |  |  |  |
| [Noether](https://doi.org/10.5281/zenodo.20412587) | 100 | 50 | 37 | 2.06 GB | Latest public version <https://doi.org/10.5281/zenodo.20836874> adds file 119, `119 Noether - PostR124 Survival Rollup NoNewPatch Audit 2026-06-24.zip`, to the curated reader/source-audit surface. This is a compact survival/no-new-patch audit/status rollup, not a new canonical TeX body patch and not completion. The local pending surface now treats R127_REBUILT as the German/source-audit authority and adds targeted P01 repair, P02-P20 survival/no-new-patch guardrails, P09-P20 queue/status index, P21/P23 survival bridge with P22 source-restoration context, P22/P30/P37/P42 repair candidates, P24-P34 queue/survival reconciliation, Tail/Kapferer no-new-patch reconciliation, P35 MathNet600/P36 GDZ600 no-patch source-disposition updates, and P35/P36/P38/P41/P43 stale-patch guardrails; all remain below strict 650+ full-page certification unless a specific packet says otherwise. The record carries cumulative readers, standalone English paper PDFs, compact language/source packages, source-audit repair packets, and multilingual working branches. It is now at the Zenodo 100-file ceiling, so future Noether updates require replacement/pruning. |
| [Weber](https://doi.org/10.5281/zenodo.20412153) | 54 | 8 | 38 | 1486.86 MB | `Lehrbuch der Algebra` Volume I represented as repaired but still under source-audit correction; Volume II readers through §176 plus recursive repair packets; Volume III current repaired cumulative. Latest public version <https://doi.org/10.5281/zenodo.20837104> adds Batch137, Batch138, and B139. New local pending Weber material includes B140-B145, the p648 content-map closure status package, and a Phase 2 status package accepting coherent German re-transcriptions for §141 and §162. Remaining held ranges include §69, §138 numbering/layout, p466, §§148-156, §158, §163, §165, §§167-170, and §§173-188; not English synchronized and not a certified critical edition. |
| [Frobenius](https://doi.org/10.5281/zenodo.20673444) | 8 | 2 | 2 | 333.59 MB | Dedicated selected group-character German/English working package. Latest public record 20821858 adds RA05, top-level German/English cumulative PDF/TeX readers, English item 070 formula-punctuation fixes, directly compilable cumulative TeX/PDF, verified extraction, and zero reported post-fix structural/formula/build flags. |
| [Adolf Kneser](https://doi.org/10.5281/zenodo.20836971) | 8 | 3 | 1 | 116.74 MB | Dedicated `Lehrbuch der Variationsrechnung` German-source and English working-translation record through p0011-p0248, with HQ source witness through p0001-p0248 and the p0234 lower-p0248 slice/audit package. Worklist reports 248/336 source pages done (73.8%), latest slice §§53-55 completing the Sixth Section, next p0249 / Seventh Section / §56. Not a certified critical edition. |
| [Sylvester](https://doi.org/10.5281/zenodo.20520692) | 3 | 1 | 1 | 91 MB | Sylvester Volume I source-witnessed working draft through book page 608; Papers 59-60 are represented in the latest tranche, next continuation p.609. |
| [al-Battani](https://doi.org/10.5281/zenodo.20539593) | 19 | 7 | 4 | 318 MB | Opus Astronomicum working edition, trilingual/catalogue data, geography, chronology, manifests, and workflow material. Legacy `Complete Critical Edition` catalogue filename is not a certified critical-edition claim. |
| **Serious source-aware work, but caveat-heavy** |  |  |  |  |  |
| [SGA](https://doi.org/10.5281/zenodo.20410947) | 100 | 74 | 25 | 3.23 GB | SGA 5/6 and further SGA working translation material, plus source/reference and audit packets. Latest local SGA5 compact delta is `SGA5_FullAudit_WebDrop_p260_p265_workpass_delta_20260626.zip`, which advances the page-local French workpass/source-audit boundary from p259 to p265 and sets p266 as the next cursor. The earlier p001-p254 webdrop and p255-p259 compact delta remain provenance/source-witness material. p260-p265 cover Expose VI around Prop. 1.2.6, tensor products, Prop. 1.3.2, cHom, invertible sheaves/Tate twist, A-faisceaux, D143/A-action square, and the opening of Q_l-faisceaux. p266+ crops/cursor text are active/pending scratch only. Local ledger terms such as certified/clean/complete are page-local workpass status only. This is repair evidence for a curated SGA5 expose selection, not complete SGA5, not synchronized English, not a critical edition, and not global source-faithfulness. SGA6 and SGA7-I remain substantial working drafts with source-compression/detail caveats. Corrections are welcome via GitHub issues or pull requests. |
| [Deligne](https://doi.org/10.5281/zenodo.20410853) | 100 | 96 | 3 | 448 MB | Mixed Deligne papers/letters drafts plus the refreshed `2026-06-09 v3` repair/math-audit packet containing D001-D017 witness material, D001-D017 equation-dense audit material, D074-D090 descending triage, and D074-D090 math-audit repairpass1; diagram-heavy material remains uneven and source-crop sensitive. |
| [Luigi Bianchi](https://doi.org/10.5281/zenodo.20615814) | 22 | 5 | 12 | 1.92 GB | `Lezioni di geometria differenziale` Vol. I represented through source pdfpages 001-543; A2 latest public compact/core package `Bianchi_A2_core_p0001_0135_IT_EN_20260613.zip` extends working coverage through source p0135 while earlier large scan-heavy p0105 packages remain provenance/backstop. Loose p0135 Italian/English reader PDFs/TeX and the p0121-p0135 source witness are queued as reader-convenience/fronting files, not new content. |
| [Paul Gordan and Clebsch-Gordan](https://doi.org/10.5281/zenodo.20616260) | 45 | 0 | 39 | 1.83 GB | Dedicated package set now includes Abel27, Abelsche FinalAuditFix02, `De linea geodetica` p001-p047, theta fix06, and `Vorlesungen ueber Invariantentheorie` Bd. 1 p001-p028 on the latest 2026-06-24 version DOI `10.5281/zenodo.20822196`, which also adds the compact project-control/status update. Working/source-audit drafts only, not a certified critical edition. |
| [Ernst Steinitz](https://doi.org/10.5281/zenodo.20616988) | 7 | 0 | 6 | 439.58 MB | Dedicated package-audited German/English working packets for 1910 fields sections 1-24, 1913 Bedingt I complete, strict 1894/1897/1906 early works, 1914 Bedingt II complete, and 1916 Bedingt III started through pp.1-13. A queued 2026-06-23 audit updates gaps: continue Bedingt III from p14; 1908 Analysis Situs has a provisional 300 ppi witness; Takagi remains intake-only. |
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
| **OCR/support/provenance or currently unsafe draft lanes** |  |  |  |  |  |
| [EGA](https://doi.org/10.5281/zenodo.20414353) | 16 | 10 | 4 | 472 MB | French originals plus partial English/OCR/draft continuation support. Useful preservation and continuation material, not a source-audited working edition comparable to the active SGA lane. |
| [Cayley](https://doi.org/10.5281/zenodo.20520749) | 84 | 13 | 69 | 1.17 GB | Provenance/repair material. No Cayley range is presently promoted as source-faithful, including the v2/restart Vol. I packets, until a future page-by-page glyph/source audit explicitly re-promotes exact ranges; the current record should be read as salvage/repair/source-comparison evidence. |

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
