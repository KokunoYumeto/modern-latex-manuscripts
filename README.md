# Modern LaTeX Editions of Mathematics Manuscripts

This repository is the GitHub working front door for an open project to produce modern, inspectable LaTeX editions and translation drafts of older mathematics and physics manuscripts.

The durable release files live on Zenodo. GitHub is for coordination: manifests, issue tracking, contribution notes, scripts, and lightweight source snapshots where practical. Large PDFs, raw scan archives, and full provenance packages should be downloaded from the linked Zenodo records.

## Current Zenodo Records

| Corpus | Status | Zenodo |
|---|---:|---|
| Main project landing and bulk archive | 100/100 current preservation surface | <https://zenodo.org/records/20415117> |
| EGA working English translation | 40/100, 560-page current build | <https://zenodo.org/records/20416974> |
| SGA working English translation | 50/100 | <https://zenodo.org/records/20417172> |
| Non-European mathematics manuscripts, consolidated | 80/100 | <https://zenodo.org/records/20415659> |
| Chinese mathematical classics | 80/100 | <https://zenodo.org/records/20415752> |
| Indian and Sanskrit mathematical classics | 80/100 | <https://zenodo.org/records/20415755> |
| Islamic and Arabic mathematical texts | 80/100 | <https://zenodo.org/records/20415770> |
| Historical reference witnesses | 70/100 | <https://zenodo.org/records/20415777> |
| Heinrich Weber | 35/100 | <https://zenodo.org/records/20416135> |
| Emmy Noether | 35/100 | <https://zenodo.org/records/20416137> |
| Pierre Deligne papers | 60/100 | <https://zenodo.org/records/20414959> |
| Classical algebra and arithmetic manuscripts | 60/100 | <https://zenodo.org/records/20418609> |
| Additional author cluster | 60/100 | <https://zenodo.org/records/20416839> |

## Start Here

| Need | Page |
|---|---|
| Find the right corpus | [Browse index](docs/browse-index.md) |
| Decide what to download | [Download guide](docs/download-guide.md) |
| Browse by author or work | [By author and work](docs/by-author-and-work.md) |
| Browse files record by record | [Record landing pages](docs/records/README.md) |
| Understand current status | [Project status dashboard](docs/project-status-dashboard.md) |
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
