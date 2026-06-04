# Modern LaTeX Editions of Public-Domain Mathematics Manuscripts

This repository is the forkable working mirror for an ongoing project to produce modern, inspectable LaTeX editions and translations of older mathematics and physics manuscripts.

Zenodo is the archival source of record. GitHub keeps editable TeX, public metadata, manifests, and reasonably sized reader PDFs together so people can fork, inspect, correct, and contribute without downloading multi-gigabyte preservation archives. The already-linked main Zenodo record is also the preservation backstop for the current working inputs, stored there as ten chunked ZIP parts plus a manifest and README; there is no separate public raw-source DOI.

## Current Public Records

- Main landing, bulk preservation, and full repository preservation backstop: https://doi.org/10.5281/zenodo.20393488
- Workflow and replication packet: https://doi.org/10.5281/zenodo.20461174
- EGA working English translation and French originals: https://doi.org/10.5281/zenodo.20414353
- SGA working English translation and French references: https://doi.org/10.5281/zenodo.20410947
- Non-European and multilingual mathematical manuscripts: https://doi.org/10.5281/zenodo.20410957
- al-Battani Opus Astronomicum work record: https://doi.org/10.5281/zenodo.20539593
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
- Deligne working record: https://doi.org/10.5281/zenodo.20410853 (latest version: https://doi.org/10.5281/zenodo.20544911)
- Ukrainian applied mathematics working record: https://doi.org/10.5281/zenodo.20490906
- Cayley, Dedekind, and Dirichlet classical algebra/arithmetic shelf: https://doi.org/10.5281/zenodo.20414787
- Author cluster shelf: https://doi.org/10.5281/zenodo.20411006

These are Zenodo concept DOI links, so they resolve to the record family rather than a single frozen version. The current latest-version identifiers are tracked in `zenodo-metadata/` and in `manifests/public_link_snippet_reddit_20260604.md`.

The first dedicated author split has created separate Cayley, Dedekind, Dirichlet, Sylvester, and Steinitz records. The existing shelf records remain useful umbrellas and preservation backstops, not the preferred reader-facing entry points for mature author lanes.

## What Is Here

- `reader-pdfs/ega/`: EGA English working readers plus the eight NUMDAM French original PDFs.
- `sources/ega/`: editable EGA TeX tree, including the current local continuation work.
- `reader-pdfs/sga/`: SGA 1-2 snapshots, a cleaned SGA 3 rebuild, complete current SGA 4 working reader, SGA 5 and SGA 7-I partial assemblies, a source-checked SGA 5 French/English edition complete through printed page 484, a complete strict SGA 6 French/English source-checked rebuild through the indexes, SGA 7-I source-checked English/French readers through source page 469, and French reference scans.
- `sources/sga/`: extracted TeX/source/review material from the current SGA artifact packets.
- `reader-pdfs/non-european/`: current work-level public readers for Chinese, Indian/Sanskrit, Islamic/Arabic, Persian, Japanese, and historical-reference material. The current Zenodo reader surface includes a 2026-06-04 broad work-level release package with 78 PDF files and 19,599 manifest pages, including full al-Kashi *Miftah al-Hisab*, al-Tusi's Euclid recension, al-Biruni's *Qanun al-Masudi* vols. 1-3, Abu Kamil, al-Karaji, Seki Takakazu, and Zhu Shijie's *Jade Mirror*. It also has a dedicated al-Battani *Opus Astronomicum* work record with the Nallino source witness, a v083 working trilingual text-reader draft, a complete 485-star working catalogue with authoritative ecliptic coordinates, magnitudes, north/south signs, modern identifications, and Arabic/English descriptions, a complete al-Battani geography gazetteer with 269 locality rows, and a partial chronology/Canon-of-Kings working edition. The professional integrated reader, chronology collation, zodiac, and auxiliary numerical tables remain active reconstruction streams.
- `reader-pdfs/non-european/` Chinese-Arabic completion: combined Arabic working-translation readers are now present for *Jiuzhang Suanshu*, Li Ye's *Ceyuan Haijing*, Qin Jiushao's *Shuxue Jiuzhang*, *Sunzi Suanjing*, and Yang Hui's *Xiangjie Jiuzhang*.
- `sources/non-european/`: extracted TeX source bundles from the non-European corpus. Large page-image, OCR, raw-provenance, and source-scan zips stay on Zenodo.
- `reader-pdfs/weber/` and `sources/weber/`: Weber English translation readers and paired German source readers, including the Volume I source-checked rebuild complete, Volume II source-checked cumulative readers through section 131, and the current repaired cumulative Volume III readers. The top-level Weber reader PDFs are ordered English first, then German source.
- `reader-pdfs/noether/` and `sources/noether/`: Noether complete numbered-paper German/English readers, newer source-checkable paper-level files, and multilingual Spanish/Japanese cumulative readers through Paper 43 complete.
- `reader-pdfs/deligne/` and `sources/deligne/`: Deligne paper-level working translations, with English reader PDFs fronted before paired French working/source PDFs. The public surface has three active lanes: a diagram-audited forward source-checked stream covering papers 001-013 complete, paper 014 through page 30, paper 015 complete, and paper 016 through page 30 in the sequential cumulative reader; a reverse source-checked stream covering papers 090 down through 079 complete; and a prominent correspondence lane with twelve English letter readers paired with French working PDFs. Additional TeX/source artifacts exist for papers 32, 42, 45, 56, 57, 58, 69, 70, and 71.
- `reader-pdfs/classical/`: current Cayley volume-level source-checked readers, including a complete Volume I source-label coverage reader, a complete German/English Dedekind edition of *Was sind und was sollen die Zahlen?*, Dedekind/Dirichlet paratext items LII-LIX, Dirichlet source-checked segments, and classical algebra/arithmetic shelf readers.
- `reader-pdfs/dedekind/` and `sources/dedekind/`: dedicated Dedekind author lane, including the earlier Dedekind readers copied out of the mixed classical shelf and the current GMW Volume I Item I Eulerian-integrals source-checked edition complete.
- `reader-pdfs/gauss/` and `sources/gauss/`: Gauss Werke reader drafts for Bands I, I alternate, II, III, VI, VII, XI Part I, individual papers, and the current Band II source-checked cumulative readers from the actual beginning through printed page 303, including the start of `Theoria residuorum biquadraticorum. Commentatio secunda`, Articles 24-29, the accepted forward cumulative material, the first Latin Nachlass section, De nexu [IX]-[X], and Dedekind remarks to `De nexu`, plus TeX sources and audit reports.
- `reader-pdfs/dirichlet/` and `sources/dirichlet/`: Dirichlet Werke Band II source-checked cumulative original-language and English readers through Papers I-XXXV.
- `reader-pdfs/riemann/` and `sources/riemann/`: Riemann selected/complete-draft readers and source packets.
- `reader-pdfs/sylvester/` and `sources/sylvester/`: Sylvester Volume I source-checked working TeX/PDF through book page 457, with source scan slices and continuation notes preserved on Zenodo.
- `reader-pdfs/steinitz/` and `sources/steinitz/`: Steinitz German/English working readers for selected 1894, 1897, 1899, 1901, 1905, 1910, and 1911 material, with the 1894 dissertation and 1905 one-sided polyhedron paper now complete, plus a 1912 source-only slice and follow-up notes.
- `reader-pdfs/ukrainian-applied-math/` and `sources/ukrainian-applied-math/`: Ukrainian applied mathematics translation readers and TeX/source packets for signal processing, software-defined radio, sensor fusion, robotics, state estimation, Lie-theoretic navigation, VIO/SLAM residuals, and Kalman filtering.
- `workflow/`: a public workflow note, sanitized replication packet, audits, OCR/tooling notes, release-process guidance, and source-intake manifests. The reusable OCR/helper scripts and lessons are under `scripts/ocr/`. The Persian/Iranian mathematics intake manifest currently lists al-Biruni, al-Kashi, al-Tusi, Khayyam, and related source candidates for the next non-European completion pass.
- `zenodo-metadata/`: public metadata JSON used for the current records.
- `manifests/`: public summaries, coverage/status notes, and a GitHub file inventory.

## Status

This is a working scholarly archive, not a finished critical edition. Current strengths are availability, inspectability, and TeX continuity.

Chinese mathematical classics now have five combined Arabic working-translation readers on the focused Chinese Zenodo record, plus 17 lower-level TeX/PDF files in `sources/non-european/chinese-arabic-completion-2026-06-04/`. Older partial Chinese-Arabic surface files were removed from the current reader folder and remain recoverable through prior Zenodo versions.

EGA currently includes the inherited community EGA I-II material plus project additions for EGA 0_IV sections 15-23 and EGA IV sections 1-21 as working translations. SGA currently includes a 484-page SGA 4 working reader, broad partial assemblies for SGA 5 and SGA 7-I, a source-checkable SGA 5 edition complete through printed page 484, a complete strict SGA 6 source-checked French/English rebuild through the terminological and notation indexes at source page 702, and SGA 7-I source-checked English/French cumulative readers through source page 469. The non-European corpus currently promotes a 78-PDF / 19,599-manifest-page work-level reader release covering Chinese, Indian/Sanskrit, Islamic/Arabic, Persian, Japanese, and reference surfaces; a dedicated al-Battani *Opus Astronomicum* work record with source witnesses, a working trilingual text-reader draft, complete 485-star working catalogue, complete 269-locality geography gazetteer, and partial chronology/Canon-of-Kings layer; and explicit notes that the integrated professional reader, zodiac, and auxiliary numerical tables remain in progress. A new Persian/Iranian source-intake lane has public manifests for al-Biruni's `Qanun al-Masudi`, al-Kashi's `Miftah al-Hisab`, al-Tusi's Euclid recension, and related checking sources. Weber includes broad older English translation drafts plus current paired high-fidelity English/German readers for Volume I complete, Volume II source-checked cumulative readers through section 131, and the current repaired cumulative Volume III readers; Noether includes audited German/English numbered-paper readers through Papers 1-43 complete plus multilingual Spanish/Japanese cumulative readers through Paper 43 complete, with English/German controls and source witnesses in the current artifact packet; Steinitz now has a dedicated German/English author lane for selected 1894-1912 material, with the 1894 dissertation and 1905 one-sided polyhedron paper complete and 1912 source-only follow-up material included; Deligne includes English-first cumulative and individual paper readers, a forward source-checked stream through paper 016 page 30, a reverse source-checked stream for papers 090 down through 079 complete, a prominent twelve-item correspondence lane with paired English/French readers, and source artifacts; Gauss and Riemann have current author pages with reader PDFs and source artifacts.

Recent additions include the complete source-checked German and English TeX/PDF edition of Dedekind's *Was sind und was sollen die Zahlen?* under `sources/classical/dedekind-was-sind-zahlen-complete-2026-06-02/`, Dedekind/Dirichlet paratext items LII-LIX under `sources/classical/dedekind-dirichlet-prefaces-and-notices-lii-lix-2026-06-02/`, Dedekind GMW Volume I Item I complete under `sources/dedekind/gmw-volume-i-item-i-eulerian-integrals-complete-2026-06-04/`, a complete Arthur Cayley Volume I source-checked reader assembled from validated slices plus six gap fills under `sources/classical/cayley-volume-i-complete-source-checked-reader-2026-06-02/`, a Sylvester Volume I working lane through book page 457 under `sources/sylvester/volume-i-through-book-page-457-2026-06-04/`, a dedicated Steinitz German/English corpus lane with complete 1894 and 1905 readers under `sources/steinitz/corpus-current-2026-06-04/`, Dirichlet Werke Band II Papers I-XXXV in the current `reader-pdfs/dirichlet/` lane and Zenodo source packet, Gauss Band II cumulative source/translation readers from the actual beginning through printed page 303 under `sources/gauss/band-ii-through-printed-page-303-dedekind-de-nexu-notes-2026-06-04/`, Noether Spanish/Japanese cumulative translations through Paper 43 complete under `sources/noether/multilingual-spanish-japanese-through-paper43-with-en-de-controls-2026-06-04/`, the complete SGA 6 strict source-checked French/English readers through source page 702 under `sources/sga/sga6-complete-source-checked-through-page-702-2026-06-02/`, SGA 7-I source-checked cumulative readers through source page 469 in the current `reader-pdfs/sga/` lane and Zenodo source packet, Weber three-volume source-checked English/German readers with Volume I complete, Volume II through section 131, and the current repaired Volume III under `sources/weber/source-checked-three-volumes-current-through-volume-ii-section-131-2026-06-04/`, a non-European 2026-06-04 work-level reader release on Zenodo with 78 PDFs and 19,599 manifest pages, a dedicated al-Battani *Opus Astronomicum* work record and source folder under `sources/non-european/al-battani-opus-astronomicum-work-level-2026-06-04/`, a forward source-checked Deligne packet for papers 001-016 through paper 016 page 30 under `sources/deligne/papers-001-016p030-source-checked-2026-06-04/`, a reverse source-checked Deligne packet for papers 079-090 complete under `sources/deligne/papers-079-090-standardized-source-checked-complete-2026-06-04/`, a complete source-checked Deligne-Mumford paper 005 rebuild under `sources/deligne/paper-005-irreducibility-curves-source-checked-complete-2026-06-02/`, a twelve-item Deligne correspondence reader lane, and a Ukrainian high-density state-estimation/Lie/VIO/Kalman translation packet under `sources/ukrainian-applied-math/high-density-state-estimation-lie-vio-kalman-2026-06-02/`.

Remaining work includes source comparison, layout repair, theorem/reference checking, mathematical proofreading, translation completion, and replacing imperfect machine-generated passages with verified text. The latest public typography audit is in `manifests/public_pdf_typography_audit_current.md`; it is a conservative repair queue rather than a pass/fail judgement. The linked main-page reader surface review is in `manifests/main_landing_reader_surface_review_20260529.md`.

## Contributing

Useful contributions include focused pull requests correcting TeX, typography, theorem numbering, cross-references, translations, or metadata; issues pointing to better public scans or existing TeX; and review notes comparing a reader PDF against source/reference text.

Please keep corrections narrowly scoped and cite the source page or file when possible. Large raw scans and preservation ZIPs live on Zenodo; GitHub is meant to stay forkable and reviewable.

## License and Citation

Unless a file or upstream source says otherwise, project-created material in this repository is dedicated under CC0 1.0 Universal, to the extent possible under law. Upstream projects, source scans, source texts, and historical authors retain their own provenance, credit, public-domain status, and license context.

For citation, use the relevant Zenodo record for the corpus you consulted. The main project record is https://zenodo.org/records/20393488.





















