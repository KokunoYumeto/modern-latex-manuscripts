# Modern LaTeX Editions of Public-Domain Mathematics Manuscripts

This repository is a lightweight, forkable working mirror for the public manuscript typesetting and translation project archived on Zenodo.

The archival source of record is Zenodo; this GitHub mirror keeps the editable TeX, public metadata, manifests, and small reader PDFs together so people can fork, inspect, correct, and contribute without downloading multi-gigabyte raw archives.

## Current Public Records

- Main landing page: https://zenodo.org/records/20415117
- EGA working translation: https://zenodo.org/records/20421561
- SGA working translation: https://zenodo.org/records/20421261
- Heinrich Weber author record: https://zenodo.org/records/20421148
- Emmy Noether author record: https://zenodo.org/records/20421149
- Non-European mathematics consolidated corpus: https://zenodo.org/records/20421441
- Chinese mathematical classics: https://zenodo.org/records/20420974
- Indian and Sanskrit mathematical classics: https://zenodo.org/records/20420975
- Islamic and Arabic mathematical texts: https://zenodo.org/records/20420983
- Historical reference witnesses: https://zenodo.org/records/20420986

## Repository Layout

- `sources/ega/`: current editable EGA TeX tree, including local continuation work.
- `sources/sga/`: extracted SGA TeX/source material from current public source packets.
- `sources/weber-noether/`: current Weber and Noether translation TeX.
- `sources/non-european/`: extracted TeX material from the current non-European corpus source bundle, including combined language/corpus TeX and work-level source bundles.
- `reader-pdfs/`: small current reader PDFs for quick inspection. Large scans and raw archives live on Zenodo.
- `reader-pdfs/non-european/`: current work-level and combined reader PDFs for the non-European corpus, with human-readable file names matching the public archive.
- `zenodo-metadata/`: public-facing metadata JSON used for the current records.
- `manifests/`: upload manifests and public summaries.

## Status

This is a working scholarly archive, not a finished critical edition. Current strengths are availability, inspectability, and TeX continuity. The EGA working reader currently includes EGA 0_IV sections 15 through 23 and EGA IV sections 1 through 9 as local continuation work, alongside the inherited community translation base. Remaining work includes source comparison, layout repair, theorem/reference checking, mathematical proofreading, and translation completion.

## Contributing

Useful contributions include:

- Pull requests correcting TeX, typography, theorem numbering, cross-references, translations, or metadata.
- Issues pointing to better public scans, existing TeX, existing translations, or obvious PDF rendering errors.
- Work-level review notes comparing a reader PDF against the source witness.

Please keep corrections narrowly scoped and cite the source page or file when possible. Large raw scans and preservation ZIPs live on Zenodo; GitHub is meant to stay forkable and reviewable.

Default dedication is CC0/public-domain dedication to the extent possible; upstream projects retain their own credit history and license context where applicable.
