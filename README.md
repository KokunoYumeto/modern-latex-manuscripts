# Modern LaTeX Editions of Public-Domain Mathematics Manuscripts

This repository is the forkable working mirror for an ongoing project to produce modern, inspectable LaTeX editions and translations of older mathematics and physics manuscripts.

Zenodo is the archival source of record. GitHub keeps editable TeX, public metadata, manifests, and reasonably sized reader PDFs together so people can fork, inspect, correct, and contribute without downloading multi-gigabyte raw archives.

## Current Public Records

- Main landing and bulk preservation record: https://zenodo.org/records/20430709
- EGA working English translation and French originals: https://zenodo.org/records/20432146
- SGA working English translation and French references: https://zenodo.org/records/20432263
- Non-European and multilingual mathematical manuscripts: https://zenodo.org/records/20432922
- Heinrich Weber author record: https://zenodo.org/records/20431945
- Emmy Noether author record: https://zenodo.org/records/20431948
- Bernhard Riemann author record: https://zenodo.org/records/20431305
- Deligne working record: https://zenodo.org/records/20414959
- Classical algebra/arithmetic shelf: https://zenodo.org/records/20418609
- Author cluster shelf: https://zenodo.org/records/20416839

## What Is Here

- `reader-pdfs/ega/`: 971-page EGA English working reader plus the eight NUMDAM French original PDFs.
- `sources/ega/`: editable EGA TeX tree, including the current local continuation work.
- `reader-pdfs/sga/`: SGA 1-3 snapshots, complete current SGA 4 working reader, SGA 5 delivered segments, SGA 6 through Expose XIV end, SGA 7-I opening, and French reference scans.
- `sources/sga/`: extracted TeX/source/review material from the current SGA artifact packets.
- `reader-pdfs/non-european/`: repaired round3 public readers for Chinese, Indian/Sanskrit, Islamic/Arabic, and historical-reference material, including combined language readers, work-level PDFs, and complete scan replacements for the Rosen and Robert/Karpinski reference originals.
- `sources/non-european/`: extracted TeX source bundles from the non-European corpus. Large page-image, OCR, raw-provenance, and source-scan zips stay on Zenodo.
- `reader-pdfs/weber/` and `sources/weber/`: Weber original-language readers and current English translation drafts, with Volume II through section 124.
- `reader-pdfs/noether/` and `sources/noether/`: Noether selected-paper reader and current English translation drafts.
- `reader-pdfs/riemann/` and `sources/riemann/`: Riemann selected/complete-draft readers and source packets.
- `zenodo-metadata/`: public metadata JSON used for the current records.
- `manifests/`: public summaries and a GitHub file inventory.

## Status

This is a working scholarly archive, not a finished critical edition. Current strengths are availability, inspectability, and TeX continuity.

EGA currently compiles to a 971-page English working reader. SGA currently includes complete current SGA 4, SGA 5 delivered segments pending audit against the 496-page French reference, SGA 6 through Expose XIV end pending audit against the 702-page French reference, and an SGA 7-I opening reader. The non-European corpus has 66 repaired top-level reader PDFs; the latest pass also promoted complete public-domain scan PDFs for the Rosen and Robert/Karpinski reference originals where sparse derived readers were not useful as public-facing originals. Weber and Noether have current author pages with original-language readers, English readers, and source artifacts.

Remaining work includes source comparison, layout repair, theorem/reference checking, mathematical proofreading, translation completion, and replacing imperfect machine-generated passages with verified text.

## Contributing

Useful contributions include focused pull requests correcting TeX, typography, theorem numbering, cross-references, translations, or metadata; issues pointing to better public scans or existing TeX; and review notes comparing a reader PDF against a source witness.

Please keep corrections narrowly scoped and cite the source page or file when possible. Large raw scans and preservation ZIPs live on Zenodo; GitHub is meant to stay forkable and reviewable.

## License and Citation

Unless a file or upstream source says otherwise, project-created material in this repository is dedicated under CC0 1.0 Universal, to the extent possible under law. Upstream projects, source scans, source texts, and historical authors retain their own provenance, credit, public-domain status, and license context.

For citation, use the relevant Zenodo record for the corpus you consulted. The main project record is https://zenodo.org/records/20430709.



