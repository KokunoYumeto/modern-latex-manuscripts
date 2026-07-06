# Zenodo Cleanup Log, 2026-07-06

This records reader-facing archive maintenance decisions. It is not a mathematical certification ledger.

## Rule Reinforced

Zenodo records should front the files a human reader is most likely to open first. Put cumulative reader PDFs first when available. Put standalone papers, TeX trees, source-witness files, repair packets, and audit ledgers into coherent ZIPs by language, author, work, or source-control function. Do not publish dozens of loose audit bundles or micro-packets at top level when a coherent ZIP is more readable.

Old versions preserve granular provenance. New versions should be usable.

## SGA

- Concept DOI: <https://doi.org/10.5281/zenodo.20410947>
- New cleaned version: <https://doi.org/10.5281/zenodo.21212365>
- Change: replaced inherited 100-file surface with 6 files.
- Front files: SGA5 French workpass PDF, SGA6 French source-rescribe workpass PDF, SGA6 English unsynchronized draft PDF.
- Grouped files: SGA5 TeX/audit/source-support ZIP and SGA6 TeX/source-rescribe/audit ZIP.
- Status language: SGA5 is not complete, not English-synchronized, not globally source-faithful, not index-audited, and not a critical edition. SGA6 remains source-rescribe/workpass material with compression/scaffold caveats.

## Emmy Noether

- Concept DOI: <https://doi.org/10.5281/zenodo.20412587>
- New cleaned version: <https://doi.org/10.5281/zenodo.21212395>
- Change: replaced inherited 100-file surface with 7 files.
- Front files: German cumulative source-control reader PDF and English cumulative reader PDF.
- Grouped files: 43 standalone English paper PDFs in one ZIP; current German/source-control TeX and reader material in one ZIP; R781-R796 source-repair/audit provenance in one ZIP; multilingual public checkpoint readers/TeX in one ZIP.
- Status language: high-value working corpus, not a critical edition, not whole-corpus certification, and not guaranteed source-faithful in dense formulas/tables without source checking.

## Workflow Lesson

Public-surface cleanup is part of the workflow, not clerical afterthought. The reader-facing record should distinguish:

- reader/cumulative PDFs,
- editable TeX/source-control packages,
- source-witness/audit/provenance packages,
- OCR/crop/formula locator aids,
- known caveats and non-certification claims.

This same rule should be applied to workflow, interlanguage, Weber, Deligne, non-European, and author-level records during subsequent sweeps.
