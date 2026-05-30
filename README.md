# Modern LaTeX Editions of Public-Domain Mathematics Manuscripts

This repository is the forkable working mirror for an ongoing project to produce modern, inspectable LaTeX editions and translations of older mathematics and physics manuscripts.

Zenodo is the archival source of record. GitHub keeps editable TeX, public metadata, manifests, and reasonably sized reader PDFs together so people can fork, inspect, correct, and contribute without downloading multi-gigabyte preservation archives. The already-linked main Zenodo record is also the preservation backstop for the current working inputs, stored there as ten chunked ZIP parts plus a manifest and README; there is no separate public raw-source DOI.

## Current Public Records

- Main landing, bulk preservation, and full repository preservation backstop: https://zenodo.org/records/20393488
- EGA working English translation and French originals: https://zenodo.org/records/20414353
- SGA working English translation and French references: https://zenodo.org/records/20410947
- Non-European and multilingual mathematical manuscripts: https://zenodo.org/records/20410957
- Chinese mathematical classics: https://zenodo.org/records/20410957
- Indian and Sanskrit mathematical classics: https://zenodo.org/records/20410957
- Islamic and Arabic mathematical texts: https://zenodo.org/records/20410957
- Historical reference texts for non-European mathematics: https://zenodo.org/records/20410957
- Heinrich Weber author record: https://zenodo.org/records/20412153
- Emmy Noether author record: https://zenodo.org/records/20412587
- Carl Friedrich Gauss author record: https://zenodo.org/records/20410934
- Bernhard Riemann author record: https://zenodo.org/records/20429778
- Deligne working record: https://zenodo.org/records/20410853
- Cayley, Dedekind, and Dirichlet classical algebra/arithmetic shelf: https://zenodo.org/records/20414787
- Author cluster shelf: https://zenodo.org/records/20411006

## What Is Here

- `reader-pdfs/ega/`: EGA English working readers plus the eight NUMDAM French original PDFs.
- `sources/ega/`: editable EGA TeX tree, including the current local continuation work.
- `reader-pdfs/sga/`: SGA 1-2 snapshots, a cleaned SGA 3 rebuild, complete current SGA 4 working reader, SGA 5 and SGA 6 partial assemblies, SGA 7-I partial assemblies, a strict SGA 5 restart source/translation supplement through Expose III B Proposition 4.2, and French reference scans.
- `sources/sga/`: extracted TeX/source/review material from the current SGA artifact packets.
- `reader-pdfs/non-european/`: current work-level public readers for Chinese, Indian/Sanskrit, Islamic/Arabic, and historical-reference material, with weaker combined readers preserved on Zenodo as artifacts rather than promoted as front-facing PDFs.
- `sources/non-european/`: extracted TeX source bundles from the non-European corpus. Large page-image, OCR, raw-provenance, and source-scan zips stay on Zenodo.
- `reader-pdfs/weber/` and `sources/weber/`: Weber original-language readers and current English translation drafts, with Volume II through supplementary matter.
- `reader-pdfs/noether/` and `sources/noether/`: Noether selected-paper reader, the older cumulative translation/summary draft, and newer source-checkable paper-level German/English restart files.
- `reader-pdfs/classical/`: current Cayley, Dedekind, and Dirichlet reader PDFs from the cleaned classical algebra/arithmetic shelf.
- `reader-pdfs/gauss/` and `sources/gauss/`: Gauss Werke reader drafts for Bands I, I alternate, II, III, VI, VII, XI Part I, and individual papers, plus TeX sources and audit reports.
- `reader-pdfs/riemann/` and `sources/riemann/`: Riemann selected/complete-draft readers and source packets.
- `zenodo-metadata/`: public metadata JSON used for the current records.
- `manifests/`: public summaries, coverage/status notes, and a GitHub file inventory.

## Status

This is a working scholarly archive, not a finished critical edition. Current strengths are availability, inspectability, and TeX continuity.

EGA currently includes the inherited community EGA I-II material plus project additions for EGA 0_IV sections 15-23 and EGA IV sections 1-21 as working translations. SGA currently includes a 484-page SGA 4 working reader, broad partial assemblies for SGA 5, SGA 6, and SGA 7-I, plus a source-checkable SGA 5 strict restart through Expose III B Proposition 4.2 as paired French-source and English high-fidelity readers. The non-European corpus currently promotes a stricter work-level public surface of 40 reader PDFs plus guide, while older combined readers and weaker drafts are retained in Zenodo ZIP artifacts for provenance and reconstruction. Weber includes broad older English translation drafts plus current paired high-fidelity German/English readers for the Volume II tail and Volume III sections 1-14; Noether includes the older cumulative translation/summary draft plus paper-level high-fidelity German/English readers through Paper 06 section 3; Gauss and Riemann have current author pages with reader PDFs and source artifacts.

Remaining work includes source comparison, layout repair, theorem/reference checking, mathematical proofreading, translation completion, and replacing imperfect machine-generated passages with verified text. The latest public typography audit is in `manifests/public_pdf_typography_audit_current.md`; it is a conservative repair queue rather than a pass/fail judgement. The linked main-page reader surface review is in `manifests/main_landing_reader_surface_review_20260529.md`.

## Contributing

Useful contributions include focused pull requests correcting TeX, typography, theorem numbering, cross-references, translations, or metadata; issues pointing to better public scans or existing TeX; and review notes comparing a reader PDF against source/reference text.

Please keep corrections narrowly scoped and cite the source page or file when possible. Large raw scans and preservation ZIPs live on Zenodo; GitHub is meant to stay forkable and reviewable.

## License and Citation

Unless a file or upstream source says otherwise, project-created material in this repository is dedicated under CC0 1.0 Universal, to the extent possible under law. Upstream projects, source scans, source texts, and historical authors retain their own provenance, credit, public-domain status, and license context.

For citation, use the relevant Zenodo record for the corpus you consulted. The main project record is https://zenodo.org/records/20393488.








