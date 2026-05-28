# Modern LaTeX Editions of Public-Domain Mathematics Manuscripts

This repository is a lightweight, forkable working mirror for the public manuscript typesetting and translation project archived on Zenodo.

The archival source of record is Zenodo; this GitHub mirror keeps the editable TeX, public metadata, manifests, and small reader PDFs together so people can fork, inspect, correct, and contribute without downloading multi-gigabyte raw archives.

## Current Public Records

- Main landing page: https://zenodo.org/records/20415117
- EGA working translation: https://zenodo.org/records/20422312
- SGA working translation: https://zenodo.org/records/20421894
- Heinrich Weber author record: https://zenodo.org/records/20421148
- Emmy Noether author record: https://zenodo.org/records/20421149
- Non-European mathematics consolidated corpus: https://zenodo.org/records/20422507
- Chinese mathematical classics: https://zenodo.org/records/20421647
- Indian and Sanskrit mathematical classics: https://zenodo.org/records/20421650
- Islamic and Arabic mathematical texts: https://zenodo.org/records/20421656
- Historical reference witnesses: https://zenodo.org/records/20421657

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

This is a working scholarly archive, not a finished critical edition. Current strengths are availability, inspectability, and TeX continuity. The EGA working reader is currently 827 pages and includes EGA 0_IV sections 15 through 23, EGA IV sections 1 through 18 as substantive local continuation work, and substantial current material for EGA IV section 20; EGA IV sections 19 and 21 are still stubs. The SGA mirror includes cleaned reader snapshots for SGA 1-3, SGA 4 through Expose XVIII section 2, and the current SGA 5 opening material. Remaining work includes source comparison, layout repair, theorem/reference checking, mathematical proofreading, and translation completion.

## Contributing

Useful contributions include:

- Pull requests correcting TeX, typography, theorem numbering, cross-references, translations, or metadata.
- Issues pointing to better public scans, existing TeX, existing translations, or obvious PDF rendering errors.
- Work-level review notes comparing a reader PDF against the source witness.

Please keep corrections narrowly scoped and cite the source page or file when possible. Large raw scans and preservation ZIPs live on Zenodo; GitHub is meant to stay forkable and reviewable.

## License and Citation

Unless a file or upstream source says otherwise, project-created material in this repository is dedicated under CC0 1.0 Universal, to the extent possible under law. Upstream projects, source scans, source texts, and historical authors retain their own provenance, credit, public-domain status, and license context.

For citation, use the relevant Zenodo record for the corpus you consulted. The main project record is https://zenodo.org/records/20415117.


