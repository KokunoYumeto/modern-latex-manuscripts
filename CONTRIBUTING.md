# Contributing

Thanks for helping make old mathematics and physics manuscripts easier to read, check, and translate.

## Good Contributions

- TeX corrections with source page references.
- Reports of unreadable, corrupt, malformed, or misleading PDFs.
- Better source witnesses or provenance links.
- Small scripts that improve audit/rebuild reliability.
- Translation batches with clear source alignment notes.

## Large Files

Please do not commit large PDFs, scans, or ZIP files directly to git. Put large artifacts in a Zenodo release, a GitHub release asset, Internet Archive item, or another stable location, then link them in an issue.

## Pull Requests

For TeX fixes, include:

- the affected work/file,
- page or section reference,
- what changed,
- how you checked it.

For script changes, include:

- the command used,
- expected output,
- any dependencies.

## PDF Quality Rule

A top-level reader PDF should open with `pdfinfo`, yield text with `pdftotext`, and be visually readable on sampled pages. If it fails, preserve the material in an artifact ZIP and open an issue to demote, repair, or replace it.
