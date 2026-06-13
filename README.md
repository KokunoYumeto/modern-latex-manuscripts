# Modern LaTeX Editions of Mathematics Manuscripts

This repository is the GitHub working front door for an open project to produce modern, inspectable LaTeX editions and translation drafts of older mathematics and physics manuscripts.

The durable release files live on Zenodo. GitHub is for coordination: manifests, issue tracking, contribution notes, scripts, and lightweight source snapshots where practical. Large PDFs, raw scan archives, and full provenance packages should be downloaded from the linked Zenodo records.

## How To Read The Status

The archive is not one uniform pile of OCR. Files sit at different quality layers, and the filename or record description should make that clear.

| Label | What It Means | How To Use It |
|---|---|---|
| `OCR_candidate`, `formula_witness`, `crop_witness`, `locator_aid` | Machine extraction, formula OCR, crops, or detector output kept as evidence. | Useful for repairing or checking; not a mathematical edition. |
| `working_draft`, `reader`, `cumulative` | Compiled TeX/PDF that is meant to be read as a draft edition or translation. | Usable for reading and continuation, but not automatically proofread. |
| `source_checked` | A named page/range has been compared against a source scan or reference witness. | Stronger than a generic draft, but still only a scoped working claim. Check important equations, tables, and diagrams before relying on them. |
| Multilingual working translation | A real translated reader draft, often with TeX structure and mathematical layout preserved. | Useful where no good translation exists, but technical claims should be checked against the source for serious use. |

In short: OCR converted to TeX is a witness layer. The main scholarly value is in compiled, organized, source-aware working drafts and translations that can be read, checked, corrected, and extended.

No public record in this project should be read as a critical edition, critically complete edition, or mathematically certified edition unless a future record explicitly says that such certification has been completed. Words such as `complete`, `source_checked`, `strict`, or `critical` in older filenames are often inherited package labels or structural coverage labels; they do not override the current status notes. At present the archive is a live working corpus with source witnesses, repair ledgers, and reader drafts. Verify citation-critical formulas, diagrams, tables, theorem statements, cross-references, and unusual notation against the source scans.

Known weak points should be treated seriously. Some large working drafts show localized compression or omissions where generated text compressed the source instead of fully transcribing it; this is documented for parts of SGA 5, SGA 6, likely SGA 7 material, and some Weber continuation/audit ranges. Diagram-heavy Deligne papers sometimes need commutative diagrams rebuilt from source rather than accepted from flattened or OCR-derived displays. Deligne material is mixed: some early sequential papers and later descending/letters packets are useful working drafts or geometry-witness packages, while some papers remain rough-draft or OCR/source-witness level. Check important equations, tables, diagrams, theorem statements, and unusual notation against the source before serious use.

## Current Zenodo Records

| Corpus | Status | Zenodo |
|---|---:|---|
| Main project landing and bulk archive | 100/100 current preservation surface | <https://doi.org/10.5281/zenodo.20393488> |
| Workflow / replication packet | Small AI-run workflow and tooling packet; latest addenda document reader-first public records, source-image authority, derivative-PDF traps, OCR as locator rather than judge, page maps, aid-package design, reliability labels, object-level diagram/table audit rules, and SGA OCR/page-map lessons. | <https://doi.org/10.5281/zenodo.20461174> |
| Emmy Noether | Curated reader-facing surface: cumulative readers, 43 standalone English paper PDFs, compact German/source, Spanish, Japanese, French, and Simplified Chinese packages, plus RA23 display-layout corrections and RA25-RA34 Paper 02 source-critical symbol/body/table audit packages; RA29 closes the Paper 02 body through printed pp.84-90 at the current page-level standard; RA31 source-checks Tabelle I p.91; RA33/RA34 source-checks Tabelle II p.92 rows 0-23 at plate-row level, with final Paper 02 tag/layout inventory and multilingual propagation still open. Local staging note 2026-06-13: RA37, RA40, and RA41 for Paper 04 plus RA42 Paper 05, targeted Paper 06/Paper 07 source-audit web drops, Paper 19 tail source-audit fixes, and a Paper 20 Lean/source-audit formula-fix web drop are extracted and queued for the next Zenodo upload, but are not yet in the public file catalog; RA41 reports Paper 04 printed pp.118-154 closed at the current German source-symbol standard, RA42 flags a Paper 05 title-footnote integration defect in RA41 cumulative, Paper 06/07 flag source-style symbolic footnote markers versus numeric TeX footnotes, Paper 19 corrects tail element-divisor exponent indices/source order, and Paper 20 corrects formula (13) factor-sum indices to `\kappa,\lambda`. The whole corpus remains 3/43 German source-symbol closed papers. A separate German source-audit support set is also queued: core RA/source ledgers, high-DPI visual witnesses, and OCR/Markdown locator material. Those companions are audit/provenance aids only; source pages and high-DPI witnesses control readings. Not a certified critical edition. | <https://doi.org/10.5281/zenodo.20412587> |
| Heinrich Weber | `Lehrbuch der Algebra` Volume I represented as repaired/source-scan-audited working edition; Volume II current German/English readers plus localized recursive repairs. Latest public Batch132 repairs Volume II §§120 and 128, reporting the active 112-row repair ledger at 73 closed / 39 open and Tier-3 rows 11/11 closed. Local staging note 2026-06-13: Batch136 for Volume I §§56, 63, 64, 68, 70, 73, 78, 89, 100, 113 is extracted and queued for upload; it reports scan-reviewed no-change closures and 101/112 ledger rows closed, 11 open. Larger compression clusters remain explicitly open. | <https://doi.org/10.5281/zenodo.20412153> |
| Arthur Cayley | Suspect draft/provenance readers; current PDFs and TeX are not accuracy-certified. The current promoted narrow tranche is `Cayley_V1_critical_p001_045_v2_20260609.zip` for Volume I pp.1-45 / Papers 1-9 as a source-inspected repair packet, not as a critical edition; older Cayley material remains de-promoted until page-by-page source audit. | <https://doi.org/10.5281/zenodo.20520749> |
| SGA working English translation | SGA 5/6 and further SGA working translations; repair027 is the latest published compact cumulative French-output refresh, containing SGA5/SGA6 French TeX/PDF only. Local staging note 2026-06-13: repair030 is extracted and queued for upload as another compact SGA5/SGA6 French TeX/PDF refresh, but is not yet in the public file catalog. The source-indexed SGA5 audit PDF and page map from repair025 remain preserved in a previous Zenodo version. SGA5 English remains unsynchronized, and SGA6/SGA7 keep explicit compression/provisional caveats; older `Complete`/`Source-Checked` filenames are legacy labels, not global certification. | <https://doi.org/10.5281/zenodo.20410947> |
| Pierre Deligne papers | Paper and letter translation/source drafts; latest 2026-06-09 v3 bundle refresh keeps D001-D017 witness/repair and equation-dense math-audit material, keeps D074-D090 descending triage material, and adds D074-D090 math-audit repairpass1. Diagram-heavy material remains working/audit level. | <https://doi.org/10.5281/zenodo.20410853> |
| EGA working English translation | Partial EGA 0_IV / EGA IV working draft material | <https://doi.org/10.5281/zenodo.20414353> |
| Ukrainian applied mathematics | Applied mathematics and engineering translation drafts | <https://doi.org/10.5281/zenodo.20490906> |
| Gauss | Gauss Werke modern LaTeX drafts and repair/source packages | <https://doi.org/10.5281/zenodo.20410934> |
| Bernhard Riemann | Selected mathematical papers and broader Gesammelte Werke working-draft readers, with TeX/source/provenance artifacts. Not a certified critical edition. | <https://doi.org/10.5281/zenodo.20429778> |
| al-Battani Opus Astronomicum | Work-level trilingual reader/source package, recovered segment tree, and table/data layers | <https://doi.org/10.5281/zenodo.20539593> |
| Non-European mathematics manuscripts, consolidated | Multilingual Chinese, Indian/Sanskrit, Islamic/Arabic, Persian/Japanese-adjacent material | <https://doi.org/10.5281/zenodo.20410957> |
| Chinese mathematical classics | 80/100 | <https://doi.org/10.5281/zenodo.20415751> |
| Indian and Sanskrit mathematical classics | 80/100 | <https://doi.org/10.5281/zenodo.20415754> |
| Islamic and Arabic mathematical texts | 80/100 | <https://doi.org/10.5281/zenodo.20415769> |
| Historical reference witnesses | 70/100 | <https://doi.org/10.5281/zenodo.20415776> |
| Classical algebra and arithmetic manuscripts | Mixed classical shelf; includes Dedekind/Dirichlet/Gauss material and de-promoted Cayley provenance that still needs source-faithfulness repair. | <https://doi.org/10.5281/zenodo.20414787> |
| James Joseph Sylvester | Dedicated Volume I source-witnessed working draft through book page 608; newest tranche covers Papers 59-60 and keeps OCR/math-OCR witnesses distinct from source authority. | <https://doi.org/10.5281/zenodo.20520692> |
| James Clerk Maxwell | `A Treatise on Electricity and Magnetism`, Volume I source-witnessed working tranches. Coverage now includes IA 1873 first-edition pp.001-059, with math/token registers currently refreshed through pp.001-058 and p.059 queued for the next register refresh, plus earlier ledger-backed book pages 95-101, 103, 105, 109, and continuous pp.111-267. The record now also includes the IA master-image source index/source-intake helper. It is a working-tranche package, not a complete Maxwell Treatise or final critical edition; printed p.060 is the next continuation point. | <https://doi.org/10.5281/zenodo.20653107> |
| J. Willard Gibbs / old physics | Dedicated source-scan-backed working edition for `The Scientific Papers`, Vol. I, pp.001-124: three reader-facing PDF/TeX surfaces plus compact source-scan ZIP packets. Not a complete Gibbs corpus. | <https://doi.org/10.5281/zenodo.20649835> |
| Luigi Bianchi | `Lezioni di geometria differenziale` Vol. I Italian/English working draft represented through source pdfpages 001-543. A2 now has compact/core Italian-English working coverage through source p0135 via `Bianchi_A2_core_p0001_0135_IT_EN_20260613.zip`; earlier large scan-heavy p0105/repair packages remain provenance/backstop layers. Local staging note 2026-06-13: a smaller same-name Edge re-export of the p0135 core package was routed under a disambiguated filename and is pending review/upload; it is not yet a public catalog replacement. | <https://doi.org/10.5281/zenodo.20615814> |
| Paul Gordan and Clebsch-Gordan | Dedicated working-edition packets: current published Abelsche package `Gordan_Abel27_p343_355_DE_EN_20260612.zip` extends `Theorie der Abelschen Functionen` through source pp.343-355 / printed pp.321-333 and cumulative German/English TeX/PDF through source p355. Local staging note 2026-06-13: `Gordan_Abelsche_FinalAuditFix02_DE_EN_20260613.zip` is extracted and queued for upload with a §91 notation-family correction (`w_k^{(h)}` rather than `n_k^{(h)}`), `Gordan_de_linea_p025_047_final_LA_EN_scans_20260613.zip` is queued for `De linea geodetica` p001-p047, and `Gordan_VB1_01_p001_009_DE_EN_20260613.zip` starts `Vorlesungen ueber Invariantentheorie` Bd. 1 with the title, Hermite dedication, and full Vorwort. Not a certified critical edition. | <https://doi.org/10.5281/zenodo.20616260> |
| Ernst Steinitz | Dedicated package-audited German/English working packets: 1910 fields sections 1-24, 1913 Bedingt I complete, strict 1894/1897/1906 early works, 1914 Bedingt II complete, and 1916 Bedingt III started through pp.1-13. | <https://doi.org/10.5281/zenodo.20616988> |
| Ferdinand Georg Frobenius | Dedicated split for selected group-character papers: public QA03 reports 10/10 selected items and 221/221 tracked source-intake pages, with German/English cumulative working readers and 241 merged source-scan pages. Local staging note 2026-06-13: RA05 is extracted and queued for upload; it fixes English item 070 formula punctuation, replaces cumulative TeX archives with directly compilable cumulative TeX/PDF, verifies ZIP extraction, and reports zero post-fix structural/formula-skeleton/build flags. Not a certified critical edition. | <https://doi.org/10.5281/zenodo.20673444> |
| Henri Poincare | Dedicated `Oeuvres`, Tome I working package stream through `poincare_v1_26.zip`; non-continuous recovery sequence with local artifacts v1_01, v1_02, v1_08-v1_21, and v1_24-v1_26, while v1_03-v1_07 and v1_22-v1_23 are not present as local package artifacts. | <https://doi.org/10.5281/zenodo.20673461> |
| Additional author cluster | Mixed author shelf for routed Kneser/Mikami/Kronecker/etc. packets and older provenance/backstop copies. Poincare and Frobenius now have preferred standalone records. Local staging note 2026-06-13: Kneser `Lehrbuch der Variationsrechnung` p0234-p0248 is routed/extracted and queued for upload, reporting 248/336 source pages done, 73.8%, with next start p0249 / Seventh Section / §56. Treat this shelf package by package, not as blanket certification. | <https://doi.org/10.5281/zenodo.20411006> |

## Start Here

| Need | Page |
|---|---|
| Find the right corpus | [Browse index](docs/browse-index.md) |
| Decide what to download | [Download guide](docs/download-guide.md) |
| Browse by author or work | [By author and work](docs/by-author-and-work.md) |
| Browse files record by record | [Record landing pages](docs/records/README.md) |
| Understand current public/staging status | [Current status manifest](manifests/current-status.md) |
| See extracted packages queued for Zenodo upload | [Pending Zenodo uploads](docs/pending-zenodo-uploads.md) |
| Understand current Zenodo file surface | [Project status dashboard](docs/project-status-dashboard.md) |
| Understand draft quality | [Quality rubric](docs/quality-rubric.md) |
| Pick a concrete task | [Work queue](docs/work-queue.md) |
| See all docs | [Site map](docs/site-map.md) |

## Workflow

The detailed provenance and review workflow is in [workflow notes](docs/workflow.md).

1. Public scans and candidate works are identified and downloaded.
2. Automated transcription systems produce initial TeX drafts.
3. ChatGPT/Codex and other agents audit, compile, repair, organize, and translate.
4. Reader PDFs stay front-facing; TeX, source scans, provenance, audits, and raw source packets are kept in artifact ZIPs.
5. Clean releases are organized by author, work, or coherent corpus and published to Zenodo under CC0 where possible.

## Quality Status

These are working scholarly drafts, not final critical editions. PDF checks verify that files open and extract text; they do not certify mathematical correctness. The [quality rubric](docs/quality-rubric.md) explains the difference between preserved files, readable drafts, source-check candidates, and proofread editions. No public record is currently certified as a critical edition by default. The most useful contributions are source comparison, theorem numbering checks, LaTeX repair, missing diagram/table repair, and translation proofreading.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for correction workflow and [release checklist](docs/release-checklist.md) for publication hygiene. Issues and pull requests should be specific: name the work, page/section, current file, source witness, and proposed correction.

Readers can suggest source comparisons, LaTeX fixes, translation corrections, and reader-facing issue reports through GitHub issues or pull requests: <https://github.com/KokunoYumeto/modern-latex-manuscripts>.

