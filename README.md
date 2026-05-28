# Modern LaTeX Editions of Public-Domain Mathematics Manuscripts

This repository is the forkable working mirror for an ongoing project to produce modern, inspectable LaTeX editions and translations of older mathematics and physics manuscripts.

Zenodo is the archival source of record. GitHub keeps editable TeX, public metadata, manifests, and reasonably sized reader PDFs together so people can fork, inspect, correct, and contribute without downloading multi-gigabyte raw archives. The main Zenodo record is also the preservation backstop for the current raw working inputs, stored there as ten `99 Raw Source Drops` ZIP parts plus a manifest.

## Current Public Records

- Main landing, bulk preservation, and raw source backstop: https://zenodo.org/records/20430709
- EGA working English translation and French originals: https://zenodo.org/records/20432146
- SGA working English translation and French references: https://zenodo.org/records/20434295
- Non-European and multilingual mathematical manuscripts: https://zenodo.org/records/20434098
- Heinrich Weber author record: https://zenodo.org/records/20434469
- Emmy Noether author record: https://zenodo.org/records/20434473
- Carl Friedrich Gauss author record: https://zenodo.org/records/20433382
- Bernhard Riemann author record: https://zenodo.org/records/20434317
- Deligne working record: https://zenodo.org/records/20414959
- Classical algebra/arithmetic shelf: https://zenodo.org/records/20418609
- Author cluster shelf: https://zenodo.org/records/20416839

## What Is Here

- `reader-pdfs/ega/`: 971-page EGA English working reader plus the eight NUMDAM French original PDFs.
- `sources/ega/`: editable EGA TeX tree, including the current local continuation work.
- `reader-pdfs/sga/`: SGA 1-3 snapshots, complete current SGA 4 working reader, SGA 5 delivered segments, SGA 6 through Expose XIV end, SGA 7-I opening, and French reference scans.
- `sources/sga/`: extracted TeX/source/review material from the current SGA artifact packets.
- `reader-pdfs/non-european/`: current public readers for Chinese, Indian/Sanskrit, Islamic/Arabic, and historical-reference material, including combined language readers, work-level PDFs, and clearly labelled Rosen and Robert/Karpinski reference scans where the generated LaTeX originals are not yet good enough for the public surface.
- `sources/non-european/`: extracted TeX source bundles from the non-European corpus. Large page-image, OCR, raw-provenance, and source-scan zips stay on Zenodo.
- `reader-pdfs/weber/` and `sources/weber/`: Weber original-language readers and current English translation drafts, with Volume II through section 124.
- `reader-pdfs/noether/` and `sources/noether/`: Noether selected-paper reader and current English translation drafts.
- `reader-pdfs/gauss/` and `sources/gauss/`: Gauss Werke reader drafts for Bands I, I alternate, II, III, VI, VII, XI Part I, and individual papers, plus TeX sources and audit reports.
- `reader-pdfs/riemann/` and `sources/riemann/`: Riemann selected/complete-draft readers and source packets.
- `zenodo-metadata/`: public metadata JSON used for the current records.
- `manifests/`: public summaries and a GitHub file inventory.

## Status

This is a working scholarly archive, not a finished critical edition. Current strengths are availability, inspectability, and TeX continuity.

EGA currently compiles to a 971-page English working reader. SGA currently includes complete current SGA 4, SGA 5 delivered segments pending audit against the 496-page French reference, SGA 6 through Expose XIV end pending audit against the 702-page French reference, and an SGA 7-I opening reader. The non-European corpus has 66 top-level public PDFs; the latest pass enlarges the index, removes visible translator-note labels from the Aryabhata reader surface, and labels Rosen and Robert/Karpinski as reference scans rather than generated originals. Weber now includes Volume II English translation through section 124 plus a Volume I English draft, and Noether now includes a 154-page English translation draft reader; Gauss and Riemann have current author pages with reader PDFs and source artifacts.

Remaining work includes source comparison, layout repair, theorem/reference checking, mathematical proofreading, translation completion, and replacing imperfect machine-generated passages with verified text.

## Contributing

Useful contributions include focused pull requests correcting TeX, typography, theorem numbering, cross-references, translations, or metadata; issues pointing to better public scans or existing TeX; and review notes comparing a reader PDF against a source witness.

Please keep corrections narrowly scoped and cite the source page or file when possible. Large raw scans and preservation ZIPs live on Zenodo; GitHub is meant to stay forkable and reviewable.

## License and Citation

Unless a file or upstream source says otherwise, project-created material in this repository is dedicated under CC0 1.0 Universal, to the extent possible under law. Upstream projects, source scans, source texts, and historical authors retain their own provenance, credit, public-domain status, and license context.

For citation, use the relevant Zenodo record for the corpus you consulted. The main project record is https://zenodo.org/records/20430709.




