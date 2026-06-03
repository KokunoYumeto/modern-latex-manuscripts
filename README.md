# Modern LaTeX Editions of Public-Domain Mathematics Manuscripts

This repository is the forkable working mirror for an ongoing project to produce modern, inspectable LaTeX editions and translations of older mathematics and physics manuscripts.

Zenodo is the archival source of record. GitHub keeps editable TeX, public metadata, manifests, and reasonably sized reader PDFs together so people can fork, inspect, correct, and contribute without downloading multi-gigabyte preservation archives. The already-linked main Zenodo record is also the preservation backstop for the current working inputs, stored there as ten chunked ZIP parts plus a manifest and README; there is no separate public raw-source DOI.

## Current Public Records

- Main landing, bulk preservation, and full repository preservation backstop: https://zenodo.org/records/20393488
- Workflow and replication packet: https://zenodo.org/records/20461174
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
- Arthur Cayley author record: https://doi.org/10.5281/zenodo.20520749
- Richard Dedekind author record: https://doi.org/10.5281/zenodo.20520669
- P. G. Lejeune Dirichlet author record: https://doi.org/10.5281/zenodo.20520679
- James Joseph Sylvester author record: https://doi.org/10.5281/zenodo.20520692
- Deligne working record: https://zenodo.org/records/20410853
- Ukrainian applied mathematics working record: https://zenodo.org/records/20490906
- Cayley, Dedekind, and Dirichlet classical algebra/arithmetic shelf: https://zenodo.org/records/20414787
- Author cluster shelf: https://zenodo.org/records/20411006

The first dedicated author split has created separate Cayley, Dedekind, Dirichlet, and Sylvester records. Steinitz remains staged under `zenodo-metadata/` until the current local bilingual packet is mirrored and checked. The existing shelf records remain useful umbrellas and preservation backstops, not the preferred reader-facing entry points for mature author lanes.

## What Is Here

- `reader-pdfs/ega/`: EGA English working readers plus the eight NUMDAM French original PDFs.
- `sources/ega/`: editable EGA TeX tree, including the current local continuation work.
- `reader-pdfs/sga/`: SGA 1-2 snapshots, a cleaned SGA 3 rebuild, complete current SGA 4 working reader, SGA 5 and SGA 7-I partial assemblies, a source-checked SGA 5 French/English edition complete through printed page 484, a complete strict SGA 6 French/English source-checked rebuild through the indexes, SGA 7-I source-checked English/French readers through source page 184, and French reference scans.
- `sources/sga/`: extracted TeX/source/review material from the current SGA artifact packets.
- `reader-pdfs/non-european/`: current work-level public readers for Chinese, Indian/Sanskrit, Islamic/Arabic, and historical-reference material. The current Zenodo reader surface has 68 front-facing PDFs and about 7996 reader pages, including corrected combined readers and an al-Battani v083 trilingual text/reference reader; the al-Battani numerical tables remain an active reconstruction stream rather than a completed table edition.
- `sources/non-european/`: extracted TeX source bundles from the non-European corpus. Large page-image, OCR, raw-provenance, and source-scan zips stay on Zenodo.
- `reader-pdfs/weber/` and `sources/weber/`: Weber original-language readers and current English translation drafts, including the Volume I source-checked rebuild complete, Volume II source-checked cumulative readers through section 91, and the current repaired cumulative Volume III readers.
- `reader-pdfs/noether/` and `sources/noether/`: Noether selected-paper reader, newer source-checkable paper-level German/English files, and multilingual Spanish/Japanese cumulative readers through Paper 18 complete.
- `reader-pdfs/deligne/` and `sources/deligne/`: Deligne paper-level working translations, including cumulative English/French working readers for touched papers, individual English paper PDFs, source-checked paper packets for papers 001, 005, and 006, separate Deligne correspondence items, and TeX/source artifacts for papers 1, 5, 6, 32, 42, 45, 56, 57, 58, 69, 70, 71, 83, 84, 85, 87, and 88.
- `reader-pdfs/classical/`: current Cayley volume-level source-checked readers, including a complete Volume I source-label coverage reader, a complete German/English Dedekind edition of *Was sind und was sollen die Zahlen?*, Dedekind/Dirichlet paratext items LII-LIX, Dirichlet source-checked segments, and classical algebra/arithmetic shelf readers.
- `reader-pdfs/gauss/` and `sources/gauss/`: Gauss Werke reader drafts for Bands I, I alternate, II, III, VI, VII, XI Part I, individual papers, and the current Band II source-checked cumulative readers through Articles 30-76, notices, and the first Latin Nachlass section through printed page 211, plus TeX sources and audit reports.
- `reader-pdfs/dirichlet/` and `sources/dirichlet/`: Dirichlet Werke Band II source-checked cumulative original-language and English readers through Papers I-XII.
- `reader-pdfs/riemann/` and `sources/riemann/`: Riemann selected/complete-draft readers and source packets.
- `reader-pdfs/sylvester/` and `sources/sylvester/`: Sylvester Volume I source-checked working TeX/PDF through book page 347, with source scan slices and continuation notes preserved on Zenodo.
- `reader-pdfs/ukrainian-applied-math/` and `sources/ukrainian-applied-math/`: Ukrainian applied mathematics translation readers and TeX/source packets for signal processing, software-defined radio, sensor fusion, robotics, state estimation, Lie-theoretic navigation, VIO/SLAM residuals, and Kalman filtering.
- `workflow/`: a public workflow note, sanitized replication packet, audits, OCR/tooling notes, release-process guidance, and source-intake manifests. The Persian/Iranian mathematics intake manifest currently lists al-Biruni, al-Kashi, al-Tusi, Khayyam, and related source candidates for the next non-European completion pass.
- `zenodo-metadata/`: public metadata JSON used for the current records.
- `manifests/`: public summaries, coverage/status notes, and a GitHub file inventory.

## Status

This is a working scholarly archive, not a finished critical edition. Current strengths are availability, inspectability, and TeX continuity.

EGA currently includes the inherited community EGA I-II material plus project additions for EGA 0_IV sections 15-23 and EGA IV sections 1-21 as working translations. SGA currently includes a 484-page SGA 4 working reader, broad partial assemblies for SGA 5 and SGA 7-I, a source-checkable SGA 5 edition complete through printed page 484, a complete strict SGA 6 source-checked French/English rebuild through the terminological and notation indexes at source page 702, and SGA 7-I source-checked English/French cumulative readers through source page 184. The non-European corpus currently promotes a reconstructed work-level public surface of 68 reader PDFs plus guide, including corrected combined readers, refreshed Qin Jiushao and other Chinese/Sanskrit/Arabic reader surfaces, and al-Battani v083 text/reference material; the al-Battani numerical astronomical tables remain explicitly in progress. A new Persian/Iranian source-intake lane has public manifests for al-Biruni's `Qanun al-Masudi`, al-Kashi's `Miftah al-Hisab`, al-Tusi's Euclid recension, and related checking sources. Weber includes broad older English translation drafts plus current paired high-fidelity German/English readers for Volume I complete, Volume II source-checked cumulative readers through section 91, and the current repaired cumulative Volume III readers; Noether includes audited German/English numbered-paper readers through Papers 1-43 complete plus multilingual Spanish/Japanese cumulative readers through Paper 18; Deligne includes cumulative English/French working readers for the touched paper set, individual English paper PDFs, source-checked paper packets for papers 001, 005, and 006, separate Deligne correspondence items, and source artifacts; Gauss and Riemann have current author pages with reader PDFs and source artifacts.

Recent additions include the complete source-checked German and English TeX/PDF edition of Dedekind's *Was sind und was sollen die Zahlen?* under `sources/classical/dedekind-was-sind-zahlen-complete-2026-06-02/`, Dedekind/Dirichlet paratext items LII-LIX under `sources/classical/dedekind-dirichlet-prefaces-and-notices-lii-lix-2026-06-02/`, a complete Arthur Cayley Volume I source-checked reader assembled from validated slices plus six gap fills under `sources/classical/cayley-volume-i-complete-source-checked-reader-2026-06-02/`, a Sylvester Volume I working lane through book page 347 under `sources/sylvester/volume-i-through-book-page-347-2026-06-03/`, Dirichlet Werke Band II Papers I-XII under `sources/dirichlet/band-ii-papers-i-xii-2026-06-02/`, Gauss Band II Articles 30-76, notices, and Nachlass through printed page 211 under `sources/gauss/band-ii-articles30-76-notices-and-nachlass-through-printed-page-211-2026-06-02/`, Noether Spanish/Japanese cumulative translations through Paper 18 complete under `sources/noether/multilingual-spanish-japanese-through-paper18-complete-2026-06-03/`, the complete SGA 6 strict source-checked French/English readers through source page 702 under `sources/sga/sga6-complete-source-checked-through-page-702-2026-06-02/`, SGA 7-I source-checked cumulative readers through source page 184 under `sources/sga/sga7-i-source-checked-through-page-184-2026-06-03/`, Weber three-volume source-checked German/English readers with Volume I complete, Volume II through section 91, and the current repaired Volume III under `sources/weber/source-checked-three-volumes-current-through-volume-ii-section-91-2026-06-03/`, source-checked Deligne paper 001 and paper 006 packets under `sources/deligne/`, a complete source-checked Deligne-Mumford paper 005 rebuild under `sources/deligne/paper-005-irreducibility-curves-source-checked-complete-2026-06-02/`, and a Ukrainian high-density state-estimation/Lie/VIO/Kalman translation packet under `sources/ukrainian-applied-math/high-density-state-estimation-lie-vio-kalman-2026-06-02/`.

Remaining work includes source comparison, layout repair, theorem/reference checking, mathematical proofreading, translation completion, and replacing imperfect machine-generated passages with verified text. The latest public typography audit is in `manifests/public_pdf_typography_audit_current.md`; it is a conservative repair queue rather than a pass/fail judgement. The linked main-page reader surface review is in `manifests/main_landing_reader_surface_review_20260529.md`.

## Contributing

Useful contributions include focused pull requests correcting TeX, typography, theorem numbering, cross-references, translations, or metadata; issues pointing to better public scans or existing TeX; and review notes comparing a reader PDF against source/reference text.

Please keep corrections narrowly scoped and cite the source page or file when possible. Large raw scans and preservation ZIPs live on Zenodo; GitHub is meant to stay forkable and reviewable.

## License and Citation

Unless a file or upstream source says otherwise, project-created material in this repository is dedicated under CC0 1.0 Universal, to the extent possible under law. Upstream projects, source scans, source texts, and historical authors retain their own provenance, credit, public-domain status, and license context.

For citation, use the relevant Zenodo record for the corpus you consulted. The main project record is https://zenodo.org/records/20393488.










