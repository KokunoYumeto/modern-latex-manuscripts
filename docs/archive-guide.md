# Archive Guide

This project publishes working modern LaTeX editions and translation drafts of older mathematics manuscripts. The Zenodo records are the durable archive; this repository is the coordination layer for contributors, manifests, and status notes.

## Where to Start

Use the topic or author records first. They are cleaner and easier to browse than the broad bulk-preservation record.

For the shortest path into the archive, use the [browse index](browse-index.md). For file-choice help, use the [download guide](download-guide.md). For a named-work view, use [by author and work](by-author-and-work.md). For a per-record file view, use the [record landing pages](records/README.md). For a one-page status view, use the [project status dashboard](project-status-dashboard.md). For quality/status vocabulary, use the [quality rubric](quality-rubric.md). For a searchable list of every current public file, use the [public file catalog](public-file-catalog.md). For known incompleteness, use the [known gaps](known-gaps.md) page.

| Need | Start Here |
|---|---|
| Overall project map and bulk preservation | <https://zenodo.org/records/20415117> |
| EGA French originals and English working translation | <https://zenodo.org/records/20416974> |
| SGA source and English translation drafts | <https://zenodo.org/records/20417172> |
| Chinese, Indian/Sanskrit, and Islamic/Arabic mathematical classics together | <https://zenodo.org/records/20415659> |
| Chinese mathematical classics only | <https://zenodo.org/records/20415752> |
| Indian and Sanskrit mathematical classics only | <https://zenodo.org/records/20415755> |
| Islamic and Arabic mathematical texts only | <https://zenodo.org/records/20415770> |
| Weber | <https://zenodo.org/records/20416135> |
| Noether | <https://zenodo.org/records/20416137> |
| Deligne | <https://zenodo.org/records/20414959> |
| Cayley, Dedekind, Dirichlet, Gauss, Weber, Noether, and nearby algebra/arithmetic material | <https://zenodo.org/records/20418609> |
| Minkowski, Hecke, Landau, Steinitz, Hensel, Oka, Hausdorff, Grassmann, and Killing | <https://zenodo.org/records/20416839> |

## File Types

Top-level PDFs are meant for direct reading and quick preview. They are the best files to open first.

Artifact ZIPs are for checking, rebuilding, or continuing work. They usually contain TeX sources, component PDFs, source witnesses, provenance notes, audit outputs, OCR text, and machine-generated intermediate material.

JSON, Markdown, and CSV files are manifests or status notes. They explain what is included, what passed basic checks, and what still needs review.

For the provenance and review model, see [workflow notes](workflow.md).

## Quality Levels

These are working scholarly drafts, not final critical editions. A PDF being public means it is useful enough to inspect, not that every theorem number, cross-reference, diagram, table, and translation choice has been proofread.

For review vocabulary, see the [quality rubric](quality-rubric.md).

The most useful corrections are:

- page-by-page source comparison against the original scan or reference PDF;
- theorem, proposition, equation, and cross-reference checks;
- LaTeX compile repairs and layout fixes;
- missing diagram or table reconstruction;
- translation proofreading against the original language.

## Current Shape

The archive is intentionally split into a main landing record plus topic/author records. The main record keeps broad preservation and a complete bulk ZIP; the topic and author records are the preferred public browsing surface.

The public metadata and filenames are periodically audited for stale internal labels, private paths, and confusing run names. The latest local audit found no configured public metadata or filename flags across the current 13-record map.
