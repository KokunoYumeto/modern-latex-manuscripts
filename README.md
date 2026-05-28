# Modern LaTeX Editions of Public-Domain Mathematics Manuscripts

This repository is a lightweight, forkable working mirror for the public manuscript typesetting and translation project archived on Zenodo.

The archival source of record is Zenodo; this GitHub mirror keeps the editable TeX, public metadata, manifests, and small reader PDFs together so people can fork, inspect, correct, and contribute without downloading multi-gigabyte raw archives.

## Start Here

- Browse `reader-pdfs/` when you want the current readable PDFs.
- Browse `sources/` when you want editable TeX or source packets to correct.
- Browse `manifests/` and `zenodo-metadata/` when you want record status, file inventories, and public archive metadata.
- Open a GitHub issue when a PDF renders badly, a source witness is missing, or a theorem/reference/translation error is visible.
- Open a pull request when you have a focused correction to TeX, translation, numbering, or metadata.

## Current Public Records

- Main landing page: https://zenodo.org/records/20415117
- EGA working translation: https://zenodo.org/records/20428073
- SGA working translation: https://zenodo.org/records/20427838
- Heinrich Weber author record: https://zenodo.org/records/20425697
- Emmy Noether author record: https://zenodo.org/records/20422936
- Non-European mathematics consolidated corpus: https://zenodo.org/records/20427329
- Chinese mathematical classics: https://zenodo.org/records/20421647
- Indian and Sanskrit mathematical classics: https://zenodo.org/records/20421650
- Islamic and Arabic mathematical texts: https://zenodo.org/records/20421656
- Historical reference texts for non-European mathematics: https://zenodo.org/records/20421657
- Cayley, Dedekind, Dirichlet, Gauss, Weber, and Noether shelf: https://zenodo.org/records/20418609
- Minkowski, Hecke, Landau, Steinitz, Hensel, Oka, Hausdorff, Grassmann, and Killing cluster: https://zenodo.org/records/20416839
- Deligne papers working record: https://zenodo.org/records/20414959

## Repository Layout

- `sources/ega/`: current editable EGA TeX tree, including local continuation work.
- `sources/sga/`: extracted SGA TeX/source material from current public source packets, normalized for public inspection and correction.
- `sources/weber-noether/`: current Weber and Noether TeX/source material, including Weber original-language chapter TeX and English translation drafts.
- `sources/non-european/`: extracted TeX material and repair notes from the current cleaned non-European corpus source bundle, including combined language/corpus TeX and work-level source bundles.
- `reader-pdfs/`: small current reader PDFs for quick inspection. Large scans and raw archives live on Zenodo.
- `reader-pdfs/ega/`: current EGA working English reader.
- `reader-pdfs/sga/`: SGA translation snapshots, SGA 4 current readers, the complete current SGA 5 working reader, the current SGA 6 working reader through Expose V section 2.3, and French reference PDFs.
- `reader-pdfs/weber/`: Weber modern LaTeX readers, the current Volume II English translation reader, and a separate Volume I English draft on inverse substitutions, transformed substitutions, transposed substitutions, permutation substitutions, invariants, and finite binary polyhedral groups.
- `reader-pdfs/noether/`: Noether modern LaTeX reader and current English translation reader.
- `reader-pdfs/non-european/`: current work-level and combined reader PDFs for the consolidated non-European/multilingual corpus, with human-readable file names matching the public archive. The Chinese, Indian/Sanskrit, Islamic/Arabic, and historical-reference Zenodo records are focused download slices of this corpus, not competing project pages.
- `zenodo-metadata/`: public-facing metadata JSON used for the current records.
- `manifests/`: upload manifests and public summaries.

## Status

This is a working scholarly archive, not a finished critical edition. Current strengths are availability, inspectability, and TeX continuity. The EGA working reader is currently 948 pages and includes EGA 0_IV sections 15 through 23 plus EGA IV sections 1 through 21 as substantive working translations; the current EGA update also replaces the earlier provisional EGA IV 7.9 placeholder material with a direct working translation of the French section on excellent rings and resolution of singularities. The SGA mirror includes cleaned reader snapshots for SGA 1-3, a complete current SGA 4 working reader through Exposes I-XIX, a complete current SGA 5 working reader assembled through the end of SGA 5, and a current SGA 6 working reader through Expose V section 2.3. The non-European mirror now tracks the cleaned multilingual release: 66 public reader PDFs, 214 editable TeX files, 40 regenerated component PDFs, repair notes, and text-sweep reports, including author/work-level TeX bundles for translations and original-language drafts. The Weber mirror now includes original-language TeX drafts for Volumes I and III, the current Volume II English translation reader, and a separate Volume I English draft on inverse substitutions, transformed substitutions, transposed substitutions, permutation substitutions, invariants, and finite binary polyhedral groups. Older cross-author shelves remain for preservation and broad browsing, while cleaner author/corpus pages are the recommended public entry points where they supersede duplicate material. Remaining work includes source comparison, layout repair, theorem/reference checking, mathematical proofreading, and translation completion.

## Contributing

Useful contributions include:

- Pull requests correcting TeX, typography, theorem numbering, cross-references, translations, or metadata.
- Issues pointing to better public scans, existing TeX, existing translations, or obvious PDF rendering errors.
- Work-level review notes comparing a reader PDF against the source witness.

Please keep corrections narrowly scoped and cite the source page or file when possible. Large raw scans and preservation ZIPs live on Zenodo; GitHub is meant to stay forkable and reviewable.

## License and Citation

Unless a file or upstream source says otherwise, project-created material in this repository is dedicated under CC0 1.0 Universal, to the extent possible under law. Upstream projects, source scans, source texts, and historical authors retain their own provenance, credit, public-domain status, and license context.

For citation, use the relevant Zenodo record for the corpus you consulted. The main project record is https://zenodo.org/records/20415117.




