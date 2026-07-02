# Noether source-core upload policy - 2026-06-29

This policy records the PC-branch rule for GitHub handoff of reusable source-core material.

## Include

- TeX/BibTeX/style/class files
- Markdown, text notes, CSV/TSV, JSON/YAML manifests
- small workbooks (`.xlsx`, `.ods`)
- local scripts used to rebuild or audit source-core artifacts

## Exclude By Default

- PDFs, images, scans, and existing archive blobs
- LaTeX build logs and transient build products
- source-cache PDFs and OCR/PDF text extraction dumps
- vendor caches and dependency directories
- files larger than 5 MiB in this GitHub snapshot lane

## Boundary

This source-core snapshot is not a native review result, not a replacement for Zenodo releases, and not a license clearance decision. It is a compact GitHub handoff layer for rebuildable text/TeX/workbook sources.
