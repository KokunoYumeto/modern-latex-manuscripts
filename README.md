# Modern LaTeX Editions of Public-Domain Mathematics Manuscripts

This repository is the forkable working mirror for an ongoing project to produce modern, inspectable LaTeX editions and translations of older mathematics and physics manuscripts.

Zenodo is the archival source of record. GitHub keeps editable TeX, public metadata, manifests, and reasonably sized reader PDFs together so people can fork, inspect, correct, and contribute without downloading multi-gigabyte preservation archives. The already-linked main Zenodo record is also the preservation backstop for the current working inputs, stored there as ten chunked ZIP parts plus a manifest and README; there is no separate public raw-source DOI.

## Current Public Records

- Main landing, bulk preservation, and full repository preservation backstop: https://doi.org/10.5281/zenodo.20393488
- Workflow and replication packet: https://doi.org/10.5281/zenodo.20461174
- EGA working English translation and French originals: https://doi.org/10.5281/zenodo.20414353
- SGA working English translation and French references: https://doi.org/10.5281/zenodo.20410947
- Non-European and multilingual mathematical manuscripts: https://doi.org/10.5281/zenodo.20410957
- al-Battani fixed-star catalogue work record: https://doi.org/10.5281/zenodo.20539593
- Chinese mathematical classics: https://doi.org/10.5281/zenodo.20415751
- Indian and Sanskrit mathematical classics: https://doi.org/10.5281/zenodo.20415754
- Islamic and Arabic mathematical texts: https://doi.org/10.5281/zenodo.20415769
- Historical reference texts for non-European mathematics: https://doi.org/10.5281/zenodo.20415776
- Heinrich Weber author record: https://doi.org/10.5281/zenodo.20412153
- Emmy Noether author record: https://doi.org/10.5281/zenodo.20412587
- Carl Friedrich Gauss author record: https://doi.org/10.5281/zenodo.20410934
- Bernhard Riemann author record: https://doi.org/10.5281/zenodo.20429778
- Arthur Cayley author record: https://doi.org/10.5281/zenodo.20520749
- Richard Dedekind author record: https://doi.org/10.5281/zenodo.20520669
- P. G. Lejeune Dirichlet author record: https://doi.org/10.5281/zenodo.20520679
- James Joseph Sylvester author record: https://doi.org/10.5281/zenodo.20520692
- Ernst Steinitz author record: https://doi.org/10.5281/zenodo.20530952
- Deligne working record: https://doi.org/10.5281/zenodo.20410853
- Ukrainian applied mathematics working record: https://doi.org/10.5281/zenodo.20490906
- Cayley, Dedekind, and Dirichlet classical algebra/arithmetic shelf: https://doi.org/10.5281/zenodo.20414787
- Author cluster shelf: https://doi.org/10.5281/zenodo.20411006

These are Zenodo concept DOI links, so they resolve to the record family rather than a single frozen version. The current latest-version identifiers are tracked in `zenodo-metadata/` and in `manifests/public_link_snippet_reddit_20260604.md`.

The first dedicated author split has created separate Cayley, Dedekind, Dirichlet, Sylvester, and Steinitz records. The existing shelf records remain useful umbrellas and preservation backstops, not the preferred reader-facing entry points for mature author lanes.

## What Is Here

- `reader-pdfs/ega/`: EGA English working readers plus the eight NUMDAM French original PDFs.
- `sources/ega/`: editable EGA TeX tree, including the current local continuation work.
- `reader-pdfs/sga/`: SGA 1-2 snapshots, a cleaned SGA 3 rebuild, complete current SGA 4 working reader, SGA 5 and SGA 7-I partial assemblies, a source-checked SGA 5 French/English edition complete through printed page 484, a complete strict SGA 6 French/English source-checked rebuild through the indexes, SGA 7-I source-checked English/French readers through source page 358, and French reference scans.
- `sources/sga/`: extracted TeX/source/review material from the current SGA artifact packets.
- `reader-pdfs/non-european/`: current work-level public readers for Chinese, Indian/Sanskrit, Islamic/Arabic, and historical-reference material. The current Zenodo reader surface has corrected combined readers, an al-Battani v083 trilingual text/reference reader, a dedicated al-Battani fixed-star catalogue record with a complete 485-star coordinate table, authoritative ecliptic coordinates, magnitudes, north/south signs, modern identifications, and a substantial but partial description layer, a complete al-Battani geography gazetteer with 269 locality rows, and a partial chronology/Canon-of-Kings working edition. Chronology collation, zodiac, and auxiliary numerical tables remain active reconstruction streams.
- `sources/non-european/`: extracted TeX source bundles from the non-European corpus. Large page-image, OCR, raw-provenance, and source-scan zips stay on Zenodo.
- `reader-pdfs/weber/` and `sources/weber/`: Weber original-language readers and current English translation drafts, including the Volume I source-checked rebuild complete, Volume II source-checked cumulative readers through section 114, and the current repaired cumulative Volume III readers.
- `reader-pdfs/noether/` and `sources/noether/`: Noether selected-paper reader, newer source-checkable paper-level German/English files, and multilingual Spanish/Japanese cumulative readers through Paper 34 part 2 complete.
- `reader-pdfs/deligne/` and `sources/deligne/`: Deligne paper-level working translations, including cumulative English/French working readers for touched papers, individual English paper PDFs, a sequential source-checked packet for papers 001-013 complete plus paper 014 through page 20, standardized source packets for papers 081-090, separate Deligne correspondence items, and TeX/source artifacts for papers 1-14 (14 partial), 32, 42, 45, 56, 57, 58, 69, 70, 71, and 81-90.
- `reader-pdfs/classical/`: current Cayley volume-level source-checked readers, including a complete Volume I source-label coverage reader, a complete German/English Dedekind edition of *Was sind und was sollen die Zahlen?*, Dedekind/Dirichlet paratext items LII-LIX, Dirichlet source-checked segments, and classical algebra/arithmetic shelf readers.
- `reader-pdfs/dedekind/` and `sources/dedekind/`: dedicated Dedekind author lane, including the earlier Dedekind readers copied out of the mixed classical shelf and the current GMW Volume I Item I Eulerian-integrals start through Article 8.
- `reader-pdfs/gauss/` and `sources/gauss/`: Gauss Werke reader drafts for Bands I, I alternate, II, III, VI, VII, XI Part I, individual papers, and the current Band II source-checked cumulative readers from the actual beginning through printed page 291, including the start of `Theoria residuorum biquadraticorum. Commentatio secunda`, Articles 24-29, the accepted forward cumulative material, and the first Latin Nachlass section and De nexu [IX]-[X], plus TeX sources and audit reports.
- `reader-pdfs/dirichlet/` and `sources/dirichlet/`: Dirichlet Werke Band II source-checked cumulative original-language and English readers through Papers I-XXIX.
- `reader-pdfs/riemann/` and `sources/riemann/`: Riemann selected/complete-draft readers and source packets.
- `reader-pdfs/sylvester/` and `sources/sylvester/`: Sylvester Volume I source-checked working TeX/PDF through book page 410, with source scan slices and continuation notes preserved on Zenodo.
- `reader-pdfs/steinitz/` and `sources/steinitz/`: Steinitz German/English working readers for selected 1894, 1897, 1899, 1901, 1905, 1910, and 1911 material, with the 1894 dissertation and 1905 one-sided polyhedron paper now complete, plus a 1912 source-only slice and follow-up notes.
- `reader-pdfs/ukrainian-applied-math/` and `sources/ukrainian-applied-math/`: Ukrainian applied mathematics translation readers and TeX/source packets for signal processing, software-defined radio, sensor fusion, robotics, state estimation, Lie-theoretic navigation, VIO/SLAM residuals, and Kalman filtering.
- `workflow/`: a public workflow note, sanitized replication packet, audits, OCR/tooling notes, release-process guidance, and source-intake manifests. The reusable OCR/helper scripts and lessons are under `scripts/ocr/`. The Persian/Iranian mathematics intake manifest currently lists al-Biruni, al-Kashi, al-Tusi, Khayyam, and related source candidates for the next non-European completion pass.
- `zenodo-metadata/`: public metadata JSON used for the current records.
- `manifests/`: public summaries, coverage/status notes, and a GitHub file inventory.

## Status

This is a working scholarly archive, not a finished critical edition. Current strengths are availability, inspectability, and TeX continuity.

EGA currently includes the inherited community EGA I-II material plus project additions for EGA 0_IV sections 15-23 and EGA IV sections 1-21 as working translations. SGA currently includes a 484-page SGA 4 working reader, broad partial assemblies for SGA 5 and SGA 7-I, a source-checkable SGA 5 edition complete through printed page 484, a complete strict SGA 6 source-checked French/English rebuild through the terminological and notation indexes at source page 702, and SGA 7-I source-checked English/French cumulative readers through source page 358. The non-European corpus currently promotes a reconstructed work-level public surface with corrected combined readers, refreshed Qin Jiushao and other Chinese/Sanskrit/Arabic reader surfaces, al-Battani v083 text/reference material, a dedicated al-Battani fixed-star catalogue record with a complete 485-star coordinate dataset and partial description layer, a complete al-Battani geography gazetteer with 269 locality rows, and a partial chronology/Canon-of-Kings working edition; chronology collation, zodiac, and auxiliary numerical tables remain explicitly in progress. A new Persian/Iranian source-intake lane has public manifests for al-Biruni's `Qanun al-Masudi`, al-Kashi's `Miftah al-Hisab`, al-Tusi's Euclid recension, and related checking sources. Weber includes broad older English translation drafts plus current paired high-fidelity German/English readers for Volume I complete, Volume II source-checked cumulative readers through section 114, and the current repaired cumulative Volume III readers; Noether includes audited German/English numbered-paper readers through Papers 1-43 complete plus multilingual Spanish/Japanese cumulative readers through Paper 34 part 2; Steinitz now has a dedicated German/English author lane for selected 1894-1912 material, with the 1894 dissertation and 1905 one-sided polyhedron paper complete and 1912 source-only follow-up material included; Deligne includes cumulative English/French working readers for the touched paper set, individual English paper PDFs, source-checked paper packets for papers 001-013 complete, paper 014 through page 20, papers 081-090, separate Deligne correspondence items, and source artifacts; Gauss and Riemann have current author pages with reader PDFs and source artifacts.

Recent additions include the complete source-checked German and English TeX/PDF edition of Dedekind's *Was sind und was sollen die Zahlen?* under `sources/classical/dedekind-was-sind-zahlen-complete-2026-06-02/`, Dedekind/Dirichlet paratext items LII-LIX under `sources/classical/dedekind-dirichlet-prefaces-and-notices-lii-lix-2026-06-02/`, Dedekind GMW Volume I Item I through Article 8 under `sources/dedekind/gmw-volume-i-item-i-eulerian-integrals-through-article-8-2026-06-03/`, a complete Arthur Cayley Volume I source-checked reader assembled from validated slices plus six gap fills under `sources/classical/cayley-volume-i-complete-source-checked-reader-2026-06-02/`, a Sylvester Volume I working lane through book page 410 under `sources/sylvester/volume-i-through-book-page-410-2026-06-04/`, a dedicated Steinitz German/English corpus lane with complete 1894 and 1905 readers under `sources/steinitz/corpus-current-2026-06-04/`, Dirichlet Werke Band II Papers I-XXIX in the current `reader-pdfs/dirichlet/` lane and Zenodo source packet, Gauss Band II cumulative source/translation readers from the actual beginning through printed page 291 under `sources/gauss/band-ii-actual-beginning-through-printed-page-291-2026-06-04/`, Noether Spanish/Japanese cumulative translations through Paper 34 part 2 under `sources/noether/multilingual-spanish-japanese-through-paper34-part2-2026-06-04/`, the complete SGA 6 strict source-checked French/English readers through source page 702 under `sources/sga/sga6-complete-source-checked-through-page-702-2026-06-02/`, SGA 7-I source-checked cumulative readers through source page 358 in the current `reader-pdfs/sga/` lane and Zenodo source packet, Weber three-volume source-checked German/English readers with Volume I complete, Volume II through section 114, and the current repaired Volume III under `sources/weber/source-checked-three-volumes-current-through-volume-ii-section-114-2026-06-04/`, a dedicated al-Battani fixed-star catalogue record and source folder under `sources/non-european/al-battani-star-catalogue-complete-description-layer-2026-06-04/`, a sequential source-checked Deligne packet for papers 001-013 complete and paper 014 through page 20 under `sources/deligne/papers-001-014-through-paper014-page020-source-checked-2026-06-04/`, standardized Deligne papers 081-090 under `sources/deligne/papers-081-090-standardized-source-checked-2026-06-04/`, a complete source-checked Deligne-Mumford paper 005 rebuild under `sources/deligne/paper-005-irreducibility-curves-source-checked-complete-2026-06-02/`, and a Ukrainian high-density state-estimation/Lie/VIO/Kalman translation packet under `sources/ukrainian-applied-math/high-density-state-estimation-lie-vio-kalman-2026-06-02/`.

Remaining work includes source comparison, layout repair, theorem/reference checking, mathematical proofreading, translation completion, and replacing imperfect machine-generated passages with verified text. The latest public typography audit is in `manifests/public_pdf_typography_audit_current.md`; it is a conservative repair queue rather than a pass/fail judgement. The linked main-page reader surface review is in `manifests/main_landing_reader_surface_review_20260529.md`.

## Contributing

Useful contributions include focused pull requests correcting TeX, typography, theorem numbering, cross-references, translations, or metadata; issues pointing to better public scans or existing TeX; and review notes comparing a reader PDF against source/reference text.

Please keep corrections narrowly scoped and cite the source page or file when possible. Large raw scans and preservation ZIPs live on Zenodo; GitHub is meant to stay forkable and reviewable.

## License and Citation

Unless a file or upstream source says otherwise, project-created material in this repository is dedicated under CC0 1.0 Universal, to the extent possible under law. Upstream projects, source scans, source texts, and historical authors retain their own provenance, credit, public-domain status, and license context.

For citation, use the relevant Zenodo record for the corpus you consulted. The main project record is https://zenodo.org/records/20393488.











