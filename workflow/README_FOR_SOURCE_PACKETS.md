# How to Read the GitHub Source Packets

This repository is the forkable working mirror for the Modern LaTeX Editions of Mathematics Manuscripts project.
Zenodo is the archival DOI surface; GitHub is the editable surface for TeX, compact reader PDFs, manifests, and current public metadata.

## What the folders mean

- `reader-pdfs/` contains front-facing reader PDFs.
  These are the files meant for direct browsing and citation as the current public reading surface.
- `sources/` contains editable TeX, source-check packets, scan cutouts when useful, manifests, audits, and build notes.
  These are meant for reviewers, continuation threads, and people who want to fork or repair the work.
- `manifests/` contains public status summaries, coverage notes, inventories, and quality-audit queues.
- `zenodo-metadata/` contains the metadata JSON used for the Zenodo author/corpus records.
- `workflow/` contains public process notes, replication notes, tooling notes, OCR/math-extraction notes, and release-process guidance.

## Reader files versus source packets

A reader PDF is the human-facing artifact.
A source packet is the continuation and verification artifact.

For public records, prefer the clean reader PDFs as the direct files.
Use source packets as ZIP attachments when they contain useful TeX, source scans, render checks, manifests, or audit material.
Do not treat every internal packet as a new public title.
If a packet is a continuation aid, label it as source material or a source-check packet rather than as a finished edition.

## Naming rule

Use author/work/scope names in public.
Avoid internal process names such as batch nicknames, model names, handoff notes, repair-pass labels, or thread names in titles.
Internal process names may remain inside manifests when they are necessary for provenance, but they should not be the public-facing title.

## Quality rule

Do not promote screenshots or page images as substitutes for transcribed TeX.
Scans, crops, and page images are useful witnesses inside source packets, but the reader surface should be editable text and math wherever possible.

When replacing an older reader, keep the older material preserved through Zenodo versions or source/provenance packets, but make the cleanest current reader the front-facing file.

## Recommended continuation workflow

1. Start from the newest source packet for the author or work.
2. Read `README_START_HERE.md`, `BUILD_SUMMARY`, `MANIFEST`, and audit files if present.
3. Compare TeX/PDF against the included source scan slice for the current range.
4. Repair prose, formulas, diagrams, labels, and tables in TeX.
5. Compile the PDF and render-check representative pages.
6. Return both individual new-work files and cumulative files, with source scans and a compact manifest.
7. Keep process notes out of public reader PDFs.

## Bulk provenance

Large raw archives and broad provenance are kept on the main Zenodo preservation record, not re-uploaded to every author record.
Author and corpus records should stay readable and comparatively lean, linking back to the main record for raw preservation when needed.
