# Workflow Addendum 2026-06-12: Curated Public Surfaces

This addendum records a practical publication rule learned from the Noether, SGA, Weber, Deligne,
and old-physics lanes.

## Core Rule

The public archive should not mirror raw workbench folders. It should present a curated reader
surface, backed by enough source and audit material for checking.

Raw working-evidence bundles can contain useful material: source scans, cropped witnesses, OCR outputs,
render checks, failed attempts, correction logs, and intermediate TeX. Those are valuable for QA and
provenance, but they should not be promoted as top-level reader files merely because they exist.

## Preferred Public Shape

For an author or work record, prefer:

- reader-facing PDFs first;
- editable TeX/source packages near the corresponding PDFs;
- one compact package per language branch or source branch when a project is multilingual;
- concise status and correction ledgers;
- clear labels for `source_checked`, `working_draft`, `OCR_candidate`, `formula_witness`,
  `crop_witness`, and `provenance`.

Avoid making readers discover the actual translation by opening many audit bundles. If the useful
artifact is an English translation of a paper, publish that paper as a paper. If the useful artifact
is a cumulative Japanese or French branch, publish that branch as a branch. Keep the workbench layer
available only where it helps verification.

## Reliability Labels

Use reliability labels honestly:

- `source_checked` means the stated range has been compared with source witnesses to the declared
  level.
- `working_draft` means readable and compiled, but not globally proofread or every-symbol certified.
- `OCR_candidate` or `formula_witness` means machine-derived evidence for repair, not edition-grade
  text.
- `provenance` means useful for tracing process, not necessarily useful for reading.

Legacy filenames that say `complete`, `strict`, or `source-checked` should be overridden by the
current record description when later audits find compression, diagram, table, or synchronization
problems. Do not delete suspect material automatically; de-promote it and label the limitation.

## Method Lesson

The durable workflow is:

1. preserve raw provenance somewhere;
2. distill current reader artifacts from the raw bundle;
3. attach source witnesses and concise ledgers;
4. publish the clean reader surface;
5. route corrections through GitHub issues or pull requests.

This keeps the archive useful for readers while still allowing future auditors to reconstruct how a
draft was produced and why a given range is or is not trusted.
