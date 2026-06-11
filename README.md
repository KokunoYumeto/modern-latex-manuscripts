# Modern LaTeX Editions of Mathematics Manuscripts

This repository is the GitHub working front door for an open project to produce modern, inspectable LaTeX editions and translation drafts of older mathematics and physics manuscripts.

The durable release files live on Zenodo. GitHub is for coordination: manifests, issue tracking, contribution notes, scripts, and lightweight source snapshots where practical. Large PDFs, raw scan archives, and full provenance packages should be downloaded from the linked Zenodo records.

## How To Read The Status

The archive is not one uniform pile of OCR. Files sit at different quality layers, and the filename or record description should make that clear.

| Label | What It Means | How To Use It |
|---|---|---|
| `OCR_candidate`, `formula_witness`, `crop_witness`, `locator_aid` | Machine extraction, formula OCR, crops, or detector output kept as evidence. | Useful for repairing or checking; not a mathematical edition. |
| `working_draft`, `reader`, `cumulative` | Compiled TeX/PDF that is meant to be read as a draft edition or translation. | Usable for reading and continuation, but not automatically proofread. |
| `source_checked` | A named page/range has been compared against a source scan or reference witness. | Stronger than a generic draft; still check important equations, tables, and diagrams before relying on them. |
| Multilingual working translation | A real translated reader draft, often with TeX structure and mathematical layout preserved. | Useful where no good translation exists, but technical claims should be checked against the source for serious use. |

In short: OCR converted to TeX is a witness layer. The main scholarly value is in compiled, organized, source-aware working drafts and translations that can be read, checked, corrected, and extended.

Known weak points should be treated seriously. Some large working drafts show localized compression or omissions where generated text compressed the source instead of fully transcribing it; this is documented for parts of SGA 5, SGA 6, likely SGA 7 material, and some Weber continuation/audit ranges. Diagram-heavy Deligne papers sometimes need commutative diagrams rebuilt from source rather than accepted from flattened or OCR-derived displays. Deligne material is mixed: some early sequential papers and later descending/letters packets are useful working drafts or geometry-witness packages, while some papers remain rough-draft or OCR/source-witness level. Check important equations, tables, diagrams, theorem statements, and unusual notation against the source before serious use.

## Current Zenodo Records

| Corpus | Status | Zenodo |
|---|---:|---|
| Main project landing and bulk archive | 100/100 current preservation surface | <https://zenodo.org/records/20415117> |
| Workflow / replication packet | Small AI-run workflow and tooling packet | <https://zenodo.org/records/20641449> |
| Emmy Noether | Numbered-paper German/English corpus plus multilingual working translations; latest public version keeps raw audit/witness material out of the reader-facing surface while DE/EN remain the canonical source branch and multilingual branches continue as working translations. | <https://zenodo.org/records/20643913> |
| Heinrich Weber | Lehrbuch Volume I complete; Volume II current German/English readers through §176 with localized recursive gap repairs through Batch119; Volume III in progress; 95 priority gap-audit rows still open. | <https://zenodo.org/records/20650399> |
| Arthur Cayley | Suspect draft/provenance readers; current PDFs and TeX are not accuracy-certified. The current promoted narrow tranche is `Cayley_V1_critical_p001_045_v2_20260609.zip` for Volume I pp.1-45 / complete Papers 1-9; older Cayley material remains de-promoted until page-by-page source audit. | <https://zenodo.org/records/20617845> |
| SGA working English translation | SGA 5/6 and further SGA working translations; SGA5 repair016 carries the French repair stream forward; SGA6 repair003 restores Expose VI source pp.372-387 in French while dense-cluster, diagram, and English-sync lanes remain open. English remains unsynchronized and SGA6/SGA7 keep explicit compression/provisional caveats. | <https://zenodo.org/records/20650065> |
| Pierre Deligne papers | Paper and letter translation/source drafts; latest 2026-06-09 v3 bundle refresh keeps D001-D017 witness/repair and equation-dense math-audit material, keeps D074-D090 descending triage material, and adds D074-D090 math-audit repairpass1. Diagram-heavy material remains working/audit level. | <https://zenodo.org/records/20617786> |
| EGA working English translation | Partial EGA 0_IV / EGA IV working draft material | <https://zenodo.org/records/20414353> |
| Ukrainian applied mathematics | Applied mathematics and engineering translation drafts | <https://zenodo.org/records/20490906> |
| Gauss | Gauss Werke modern LaTeX drafts and repair/source packages | <https://zenodo.org/records/20410934> |
| al-Battani Opus Astronomicum | Work-level trilingual reader/source package, recovered segment tree, and table/data layers | <https://zenodo.org/records/20584850> |
| Non-European mathematics manuscripts, consolidated | Multilingual Chinese, Indian/Sanskrit, Islamic/Arabic, Persian/Japanese-adjacent material | <https://zenodo.org/records/20410957> |
| Chinese mathematical classics | 80/100 | <https://zenodo.org/records/20415752> |
| Indian and Sanskrit mathematical classics | 80/100 | <https://zenodo.org/records/20415755> |
| Islamic and Arabic mathematical texts | 80/100 | <https://zenodo.org/records/20415770> |
| Historical reference witnesses | 70/100 | <https://zenodo.org/records/20415777> |
| Classical algebra and arithmetic manuscripts | Mixed classical shelf; includes Dedekind/Dirichlet/Gauss material and de-promoted Cayley provenance that still needs source-faithfulness repair. | <https://zenodo.org/records/20583048> |
| James Joseph Sylvester | Dedicated Volume I source-checked working edition through book page 608; newest tranche completes Papers 59-60 and keeps OCR/math-OCR witnesses distinct from source authority. | <https://zenodo.org/records/20649689> |
| J. Willard Gibbs / old physics | Dedicated source-scan-backed working edition for `The Scientific Papers`, Vol. I, pp.001-124: three reader-facing PDF/TeX surfaces plus compact source-scan ZIP packets. Not a complete Gibbs corpus. | <https://zenodo.org/records/20649836> |
| Luigi Bianchi | `Lezioni di geometria differenziale` Vol. I Italian/English working edition complete through source pdfpages 001-543, plus A2 high-quality Italian/English working start through source p0001-p0066, plus a newer preferred audit-continuation layer through p0001-p0057. A2 is not complete; section 13 begins at the p0066/p0067 boundary. | <https://zenodo.org/records/20649956> |
| Paul Gordan and Clebsch-Gordan | Dedicated working-edition packets: Abel11-Abel15 extend Abelsche Functionen through source p217; Abel13 includes the p190 continuation of equation (4), while Abel14/15 continue p194-p217. AllPrior AuditFix01 remains the consolidated support checkpoint for the earlier branches. | <https://zenodo.org/records/20649946> |
| Ernst Steinitz | Dedicated package-audited German/English working packets: 1910 fields sections 1-24, 1913 Bedingt I complete, strict 1894/1897/1906 early works, 1914 Bedingt II complete, and 1916 Bedingt III started through pp.1-13. | <https://zenodo.org/records/20617915> |
| Additional author cluster | Mixed author shelf; latest routed sweep adds Poincare v1_19, with Tome I FR/EN working drafts through Chapter XI; the same surface includes Kneser LVR p0139-p0158 and Frobenius 070/071. Superseded duplicate packets are pruned where needed while older Zenodo versions retain provenance. | <https://zenodo.org/records/20650460> |

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

These are working scholarly drafts, not final critical editions. PDF checks verify that files open and extract text; they do not certify mathematical correctness. The [quality rubric](docs/quality-rubric.md) explains the difference between preserved files, readable drafts, source-check candidates, and proofread editions. The most useful contributions are source comparison, theorem numbering checks, LaTeX repair, missing diagram/table repair, and translation proofreading.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for correction workflow and [release checklist](docs/release-checklist.md) for publication hygiene. Issues and pull requests should be specific: name the work, page/section, current file, source witness, and proposed correction.

Readers can suggest source comparisons, LaTeX fixes, translation corrections, and reader-facing issue reports through GitHub issues or pull requests: <https://github.com/KokunoYumeto/modern-latex-manuscripts>.
