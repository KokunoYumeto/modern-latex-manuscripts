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
| Main project landing and bulk archive | 100/100 current preservation surface | <https://zenodo.org/records/20415117> |
| Workflow / replication packet | Small AI-run workflow and tooling packet; latest addendum documents reader-first public records, source-image authority, derivative-PDF traps, OCR as locator rather than judge, page maps, aid-package design, and reliability labels. | <https://zenodo.org/records/20652117> |
| Emmy Noether | Curated reader-facing surface: cumulative readers, 43 standalone English paper PDFs, and compact German/source, Spanish, Japanese, French, and Simplified Chinese packages. Known correction streams remain explicit. | <https://zenodo.org/records/20665205> |
| Heinrich Weber | Lehrbuch Volume I complete; Volume II current German/English readers through §176 with localized recursive gap repairs through Batch125. Recent repairs close Vol. II §71 and Vol. I §§166, 171, and 157; Batch125 corrects the Vol. I §157 rho notation. Volume III remains in progress; 88 priority gap-audit rows still open. | <https://zenodo.org/records/20665199> |
| Arthur Cayley | Suspect draft/provenance readers; current PDFs and TeX are not accuracy-certified. The current promoted narrow tranche is `Cayley_V1_critical_p001_045_v2_20260609.zip` for Volume I pp.1-45 / Papers 1-9 as a source-inspected repair packet, not as a critical edition; older Cayley material remains de-promoted until page-by-page source audit. | <https://zenodo.org/records/20617845> |
| SGA working English translation | SGA 5/6 and further SGA working translations; SGA repair018 adds source-level SGA5 French diagram repairs for source pp.030, 031, and 084 using the 179-row diagram micropass aid. SGA6 French is carried forward from the earlier Expose VI repair lane/repair004, which restored Expose VI source pp.391-397. English remains unsynchronized, SGA6 still has open v3 worklist rows, and SGA6/SGA7 keep explicit compression/provisional caveats; older `Complete`/`Source-Checked` filenames are legacy labels, not global certification. | <https://zenodo.org/records/20665102> |
| Pierre Deligne papers | Paper and letter translation/source drafts; latest 2026-06-09 v3 bundle refresh keeps D001-D017 witness/repair and equation-dense math-audit material, keeps D074-D090 descending triage material, and adds D074-D090 math-audit repairpass1. Diagram-heavy material remains working/audit level. | <https://zenodo.org/records/20617786> |
| EGA working English translation | Partial EGA 0_IV / EGA IV working draft material | <https://zenodo.org/records/20454552> |
| Ukrainian applied mathematics | Applied mathematics and engineering translation drafts | <https://zenodo.org/records/20520721> |
| Gauss | Gauss Werke modern LaTeX drafts and repair/source packages | <https://zenodo.org/records/20410934> |
| al-Battani Opus Astronomicum | Work-level trilingual reader/source package, recovered segment tree, and table/data layers | <https://zenodo.org/records/20584850> |
| Non-European mathematics manuscripts, consolidated | Multilingual Chinese, Indian/Sanskrit, Islamic/Arabic, Persian/Japanese-adjacent material | <https://zenodo.org/records/20410957> |
| Chinese mathematical classics | 80/100 | <https://zenodo.org/records/20415752> |
| Indian and Sanskrit mathematical classics | 80/100 | <https://zenodo.org/records/20415755> |
| Islamic and Arabic mathematical texts | 80/100 | <https://zenodo.org/records/20415770> |
| Historical reference witnesses | 70/100 | <https://zenodo.org/records/20415777> |
| Classical algebra and arithmetic manuscripts | Mixed classical shelf; includes Dedekind/Dirichlet/Gauss material and de-promoted Cayley provenance that still needs source-faithfulness repair. | <https://zenodo.org/records/20583048> |
| James Joseph Sylvester | Dedicated Volume I source-witnessed working draft through book page 608; newest tranche covers Papers 59-60 and keeps OCR/math-OCR witnesses distinct from source authority. | <https://zenodo.org/records/20649689> |
| James Clerk Maxwell | `A Treatise on Electricity and Magnetism`, Volume I source-witnessed working tranches. Coverage now includes IA 1873 first-edition pp.001-046 plus earlier ledger-backed book pages 95-101, 103, 105, 109, and continuous pp.111-267. The record is a working-tranche package, not a complete Maxwell Treatise or final critical edition; printed p.047 is the next continuation point and is not part of this public boundary. | <https://zenodo.org/records/20660332> |
| J. Willard Gibbs / old physics | Dedicated source-scan-backed working edition for `The Scientific Papers`, Vol. I, pp.001-124: three reader-facing PDF/TeX surfaces plus compact source-scan ZIP packets. Not a complete Gibbs corpus. | <https://zenodo.org/records/20649836> |
| Luigi Bianchi | `Lezioni di geometria differenziale` Vol. I Italian/English working draft represented through source pdfpages 001-543. A2 now has `Bianchi_A2_reaudit_p0001_0066_IT_EN_20260611.zip` as the preferred correction layer through p0066; it supersedes the previous cumulative at two audited mathematical locations while §§10-12 are structurally represented and §13 is still deliberately deferred. | <https://zenodo.org/records/20651036> |
| Paul Gordan and Clebsch-Gordan | Dedicated working-edition packets: Abel17 extends Abelsche Functionen through source p243 / printed p221 with cumulative DE/EN TeX/PDF and source witnesses. Abel13-16 remain the preceding p182-p227 tranches; AllPrior AuditFix01 remains the consolidated support checkpoint for earlier branches. | <https://zenodo.org/records/20660721> |
| Ernst Steinitz | Dedicated package-audited German/English working packets: 1910 fields sections 1-24, 1913 Bedingt I complete, strict 1894/1897/1906 early works, 1914 Bedingt II complete, and 1916 Bedingt III started through pp.1-13. | <https://zenodo.org/records/20617915> |
| Additional author cluster | Mixed author shelf; latest routed sweep adds `poincare_v1_20.zip` through Poincare Tome I Chapters XII-XIII and `Frobenius_all_GE_EN_cum_scans_QA03_20260611.zip`, a selected Frobenius sequence cumulative/QA package. `Kneser_LVR_hqfig_p0158_0177_DE_EN_20260611.zip` remains the preferred Kneser p0158-p0177 figure/source-witness repair. Treat the shelf package by package, not as blanket certification. | <https://zenodo.org/records/20651148> |

## Start Here

| Need | Page |
|---|---|
| Find the right corpus | [Browse index](docs/browse-index.md) |
| Decide what to download | [Download guide](docs/download-guide.md) |
| Browse by author or work | [By author and work](docs/by-author-and-work.md) |
| Browse files record by record | [Record landing pages](docs/records/README.md) |
| Understand current public/staging status | [Current status manifest](manifests/current-status.md) |
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
