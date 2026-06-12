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
| Workflow / replication packet | Small AI-run workflow and tooling packet; latest addendum documents reader-first public records, source-image authority, derivative-PDF traps, OCR as locator rather than judge, page maps, aid-package design, reliability labels, and SGA OCR/page-map lessons. | <https://zenodo.org/records/20670272> |
| Emmy Noether | Curated reader-facing surface: cumulative readers, 43 standalone English paper PDFs, compact German/source, Spanish, Japanese, French, and Simplified Chinese packages, plus RA23 display-layout corrections and RA25-RA31 Paper 02 source-critical symbol/body audit packages; RA29 closes the Paper 02 body through printed pp.84-90 at the current page-level standard; RA30 adds the Paper 02 final-summary/table-plate audit package; RA31 source-checks Tabelle I on printed/source p.91, with Tabelle II p.92 and multilingual propagation still open. Not a certified critical edition; the RA25-RA31 source corrections still need cross-language propagation. | <https://zenodo.org/records/20672553> |
| Heinrich Weber | `Lehrbuch der Algebra` Volume I represented as repaired/source-scan-audited working edition; Volume II current German/English readers through §176 with localized recursive repairs through Batch129. Latest Batch129 repairs Volume II §§33-34 from source scans pp.134-140, with p.141 / §35 as the handoff boundary, replacing compressed/simple-group material and adding Frobenius proof material, footnotes, and explicit permutation arrays; larger compression clusters remain explicitly open. Volume III remains the earlier repaired cumulative. | <https://zenodo.org/records/20672355> |
| Arthur Cayley | Suspect draft/provenance readers; current PDFs and TeX are not accuracy-certified. The current promoted narrow tranche is `Cayley_V1_critical_p001_045_v2_20260609.zip` for Volume I pp.1-45 / Papers 1-9 as a source-inspected repair packet, not as a critical edition; older Cayley material remains de-promoted until page-by-page source audit. | <https://zenodo.org/records/20617845> |
| SGA working English translation | SGA 5/6 and further SGA working translations; repair025 carries forward cumulative SGA5/SGA6 French TeX/PDF and covers SGA5 French source pp.160, 171, 174-177, and 180, with a 484-page source-indexed SGA5 audit PDF and page map. SGA6 French is unchanged, SGA5 English remains unsynchronized, and SGA6/SGA7 keep explicit compression/provisional caveats; older `Complete`/`Source-Checked` filenames are legacy labels, not global certification. | <https://zenodo.org/records/20672608> |
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
| James Clerk Maxwell | `A Treatise on Electricity and Magnetism`, Volume I source-witnessed working tranches. Coverage now includes IA 1873 first-edition pp.001-059, with math/token registers currently refreshed through pp.001-058 and p.059 queued for the next register refresh, plus earlier ledger-backed book pages 95-101, 103, 105, 109, and continuous pp.111-267. The record is a working-tranche package, not a complete Maxwell Treatise or final critical edition; printed p.060 is the next continuation point. | <https://zenodo.org/records/20672724> |
| J. Willard Gibbs / old physics | Dedicated source-scan-backed working edition for `The Scientific Papers`, Vol. I, pp.001-124: three reader-facing PDF/TeX surfaces plus compact source-scan ZIP packets. Not a complete Gibbs corpus. | <https://zenodo.org/records/20649836> |
| Luigi Bianchi | `Lezioni di geometria differenziale` Vol. I Italian/English working draft represented through source pdfpages 001-543. A2 now has `Bianchi_A2_sumfix_p0001_0090_IT_EN_20260612.zip` as the latest summation-limit repair layer through p0090: it repairs summation-limit rendering through Chapter II / §§17-22; no new pages are added; next continuation p0091. | <https://zenodo.org/records/20669390> |
| Paul Gordan and Clebsch-Gordan | Dedicated working-edition packets: The revised Abel23 package extends `Theorie der Abelschen Functionen` through source pp.300-308 / printed pp.278-286 and cumulative German/English TeX/PDF through source p308. It continues and closes §79 and covers visible §80 through the final formula for the integral sums v_h; next continuation is after source p308 / printed p286. Earlier Abel tranches and AllPrior AuditFix01 remain provenance/support layers. | <https://zenodo.org/records/20671984> |
| Ernst Steinitz | Dedicated package-audited German/English working packets: 1910 fields sections 1-24, 1913 Bedingt I complete, strict 1894/1897/1906 early works, 1914 Bedingt II complete, and 1916 Bedingt III started through pp.1-13. | <https://zenodo.org/records/20617915> |
| Additional author cluster | Mixed author shelf for routed Poincare/Frobenius/Kneser/Mikami/Kronecker/etc. packets. Latest routed sweep includes `poincare_v1_24.zip` for Poincare Tome I source witnesses v1_0329-v1_0345 / Chapters XVII-XVIII, explicitly non-continuous because intervening v1_22/v1_23 artifacts are missing locally, `Frobenius_all_GE_EN_cum_scans_QA03_20260611.zip`, and `Kneser_LVR_p0206_0219_DE_EN_20260612.zip` for Kneser p0206 lower-p0219 upper / §§46-48 with Fig. 24 as a source-derived crop; lower p0219 / section 49 remains the next handoff. Treat the shelf package by package, not as blanket certification. | <https://zenodo.org/records/20672178> |

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
