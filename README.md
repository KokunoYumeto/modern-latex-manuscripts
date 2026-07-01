# Modern LaTeX Editions of Public-Domain Mathematics Manuscripts

This repository is the forkable working mirror for an ongoing project to produce modern, inspectable LaTeX editions and translations of older mathematics and physics manuscripts.

Zenodo is the archival source of record. GitHub keeps editable TeX, public metadata, manifests, and reasonably sized reader PDFs together so people can fork, inspect, correct, and contribute without downloading multi-gigabyte preservation archives. The already-linked main Zenodo record is also the preservation backstop for the current working inputs, stored there as ten chunked ZIP parts plus a manifest and README; there is no separate public raw-source DOI.

## Current Public Records

The list below is ordered by current public usefulness and source confidence, not by DOI age, file count, storage size, or aspirational importance. OCR/source-intake/support lanes are deliberately below the records with coherent reader or translation surfaces.

No record here is a certified critical edition unless a future release explicitly says so. Older filenames can contain words such as `complete`, `strict`, `source-checked`, or `critical`; use the notes below and the record metadata, not those inherited filenames alone.

### Strongest Current Reader And Translation Surfaces

- Emmy Noether author record: https://doi.org/10.5281/zenodo.20412587
- Heinrich Weber author record: https://doi.org/10.5281/zenodo.20412153
- Ferdinand Georg Frobenius record: https://doi.org/10.5281/zenodo.20673444
- Adolf Kneser record: https://doi.org/10.5281/zenodo.20836971
- James Joseph Sylvester author record: https://doi.org/10.5281/zenodo.20520692
- al-Battani Opus Astronomicum work record: https://doi.org/10.5281/zenodo.20539593

### Serious Source-Aware Work, With Caveats

- SGA working translation and source-audit material: https://doi.org/10.5281/zenodo.20410947
- Deligne working record: https://doi.org/10.5281/zenodo.20410853
- Luigi Bianchi record: https://doi.org/10.5281/zenodo.20615814
- Paul Gordan and Clebsch-Gordan record: https://doi.org/10.5281/zenodo.20616260
- Ernst Steinitz record: https://doi.org/10.5281/zenodo.20616988
- James Clerk Maxwell record: https://doi.org/10.5281/zenodo.20653107
- J. Willard Gibbs / old physics record: https://doi.org/10.5281/zenodo.20649835
- Ukrainian applied mathematics working record: https://doi.org/10.5281/zenodo.20490906
- Non-European and multilingual mathematical manuscripts: https://doi.org/10.5281/zenodo.20410957
- Chinese mathematical classics: https://doi.org/10.5281/zenodo.20415751
- Indian and Sanskrit mathematical classics: https://doi.org/10.5281/zenodo.20415754
- Islamic and Arabic mathematical texts: https://doi.org/10.5281/zenodo.20415769
- Historical reference texts for non-European mathematics: https://doi.org/10.5281/zenodo.20415776

### Partial Or Non-Continuous Author Workstreams

- Richard Dedekind author record: https://doi.org/10.5281/zenodo.20520669
- P. G. Lejeune Dirichlet author record: https://doi.org/10.5281/zenodo.20520679
- Carl Friedrich Gauss author record: https://doi.org/10.5281/zenodo.20410934
- Bernhard Riemann author record: https://doi.org/10.5281/zenodo.20429778
- Henri Poincare record: https://doi.org/10.5281/zenodo.20673461
- Cayley, Dedekind, and Dirichlet classical algebra/arithmetic shelf: https://doi.org/10.5281/zenodo.20414787
- Author cluster shelf: https://doi.org/10.5281/zenodo.20411006

### Source-Intake, OCR/Support, Or Currently Unsafe Draft Lanes

- EGA French originals plus partial English/OCR support: https://doi.org/10.5281/zenodo.20414353
- Arthur Cayley author record: https://doi.org/10.5281/zenodo.20520749

### Project Infrastructure

- Main landing, bulk preservation, and full repository preservation backstop: https://doi.org/10.5281/zenodo.20393488
- Workflow and replication packet: https://doi.org/10.5281/zenodo.20461174

SGA and EGA are not equivalent records. SGA contains substantial active translation and page-local repair/workpass material, especially for SGA 5, but it remains incomplete and not globally source-faithful. EGA is currently lower-confidence preservation/support material: French originals, OCR/source support, and partial English draft material. Cayley is currently repair provenance and source-comparison scaffolding; inherited `Complete`, `Source-Checked`, or `critical` Cayley filenames should not be treated as current quality claims.

These are Zenodo concept DOI links, so they resolve to the record family rather than a single frozen version. The current latest-version identifiers are tracked in `zenodo-metadata/` and in `manifests/public_link_snippet_reddit_20260604.md`.

The first dedicated author split has created separate Cayley, Dedekind, Dirichlet, Sylvester, and Steinitz records. The existing shelf records remain useful umbrellas and preservation backstops, not the preferred reader-facing entry points for mature author lanes.

## What Is Here

- `reader-pdfs/ega/`: EGA English OCR/draft/support readers plus the eight NUMDAM French original PDFs. This is a preservation/continuation-support lane, not a source-audited working edition comparable to SGA.
- `sources/ega/`: editable EGA TeX tree, including the current local continuation work.
- `reader-pdfs/sga/`: SGA 1-2 snapshots, a cleaned SGA 3 rebuild, SGA 4 working reader, SGA 5 and SGA 7-I assemblies, SGA 6 working rebuild material, and French reference scans. SGA is serious active work, but labels such as `complete`, `strict`, and `source-checked` in older packets should be read cautiously: SGA 5 remains under page-local workpass audit, and SGA 6/7 carry compression/detail caveats unless a specific packet states a bounded source-checked range.
- `sources/sga/`: extracted TeX/source/review material from the current SGA artifact packets.
- `reader-pdfs/non-european/`: current work-level public readers for Chinese, Indian/Sanskrit, Islamic/Arabic, Persian, Japanese, and historical-reference material. The current Zenodo reader surface includes a 2026-06-04 broad work-level release package with 78 PDF files and 19,599 manifest pages, including full al-Kashi *Miftah al-Hisab*, al-Tusi's Euclid recension, al-Biruni's *Qanun al-Masudi* vols. 1-3, Abu Kamil, al-Karaji, Seki Takakazu, and Zhu Shijie's *Jade Mirror*. It also has a dedicated al-Battani *Opus Astronomicum* work record with a complete-text Arabic/English/Chinese working edition, the Nallino source witness, a complete 485-star working catalogue with authoritative ecliptic coordinates, magnitudes, north/south signs, modern identifications, and Arabic/English descriptions, a complete al-Battani geography gazetteer with 269 locality rows, and a partial chronology/Canon-of-Kings working edition. The final professional critical reader, chronology collation, zodiac, table placement, and auxiliary numerical tables remain active reconstruction streams.
- `reader-pdfs/non-european/` Chinese-Arabic completion: combined Arabic working-translation readers are now present for *Jiuzhang Suanshu*, Li Ye's *Ceyuan Haijing*, Qin Jiushao's *Shuxue Jiuzhang*, *Sunzi Suanjing*, and Yang Hui's *Xiangjie Jiuzhang*.
- `sources/non-european/`: extracted TeX source bundles from the non-European corpus. Large page-image, OCR, raw-provenance, and source-scan zips stay on Zenodo.
- `reader-pdfs/weber/` and `sources/weber/`: Weber English translation readers and paired German source readers, including the Volume I source-checked rebuild complete, Volume II source-checked cumulative readers through section 131, and the current repaired cumulative Volume III readers. The top-level Weber reader PDFs are ordered English first, then German source.
- `reader-pdfs/noether/` and `sources/noether/`: Noether complete numbered-paper German/English readers, newer source-checkable paper-level files, and multilingual Spanish/Japanese cumulative readers through Paper 43 complete.
- `reader-pdfs/deligne/` and `sources/deligne/`: Deligne paper-level working translations, with English reader PDFs fronted before paired French working/source PDFs. The public surface has three active lanes: a diagram-audited forward source-checked stream covering papers 001-013 complete, paper 014 through page 30, paper 015 complete, and paper 016 through page 30 in the sequential cumulative reader; a reverse source-checked stream covering papers 090 down through 079 complete; and a prominent correspondence lane with twelve English letter readers paired with French working PDFs. Additional TeX/source artifacts exist for papers 32, 42, 45, 56, 57, 58, 69, 70, and 71.
- `reader-pdfs/classical/`: classical algebra/arithmetic shelf readers and working drafts. Dedekind and Dirichlet contain useful source-witnessed work, but Cayley material in this shelf is currently de-promoted repair/provenance material; do not treat Cayley volume-level `source-checked` or `complete` filenames as source-faithful until exact ranges are re-audited and re-promoted.
- `reader-pdfs/dedekind/` and `sources/dedekind/`: dedicated Dedekind author lane, including the earlier Dedekind readers copied out of the mixed classical shelf and the current GMW Volume I Item I Eulerian-integrals source-checked edition complete.
- `reader-pdfs/gauss/` and `sources/gauss/`: Gauss Werke reader drafts for Bands I, I alternate, II, III, VI, VII, XI Part I, individual papers, and the current Band II source-checked cumulative readers from the actual beginning through printed page 303, including the start of `Theoria residuorum biquadraticorum. Commentatio secunda`, Articles 24-29, the accepted forward cumulative material, the first Latin Nachlass section, De nexu [IX]-[X], and Dedekind remarks to `De nexu`, plus TeX sources and audit reports.
- `reader-pdfs/dirichlet/` and `sources/dirichlet/`: Dirichlet Werke Band II source-checked cumulative original-language and English readers through Papers I-XXXVI.
- `reader-pdfs/riemann/` and `sources/riemann/`: Riemann selected/complete-draft readers and source packets.
- `reader-pdfs/sylvester/` and `sources/sylvester/`: Sylvester Volume I source-checked working TeX/PDF through book page 457, with source scan slices and continuation notes preserved on Zenodo.
- `reader-pdfs/steinitz/` and `sources/steinitz/`: Steinitz German/English working readers for selected 1894, 1897, 1899, 1901, 1905, 1910, 1911, and the opening of 1912 material, with the 1894 dissertation and 1905 one-sided polyhedron paper complete, the 1910 field-theory reader current through sections 1-24, and 1912 Rectangular Systems II started through printed pp. 297-315.
- `reader-pdfs/ukrainian-applied-math/` and `sources/ukrainian-applied-math/`: Ukrainian applied mathematics translation readers and TeX/source packets for signal processing, software-defined radio, sensor fusion, robotics, state estimation, Lie-theoretic navigation, VIO/SLAM residuals, and Kalman filtering.
- `workflow/`: a public workflow note, sanitized replication packet, audits, OCR/tooling notes, release-process guidance, and source-intake manifests. The reusable OCR/helper scripts and lessons are under `scripts/ocr/`. The Persian/Iranian mathematics intake manifest currently lists al-Biruni, al-Kashi, al-Tusi, Khayyam, and related source candidates for the next non-European completion pass.
- `zenodo-metadata/`: public metadata JSON used for the current records.
- `manifests/`: public summaries, coverage/status notes, and a GitHub file inventory.

## Status

This is a working scholarly archive, not a finished critical edition. Current strengths are availability, inspectability, and TeX continuity.

Chinese mathematical classics now have five combined Arabic working-translation readers on the focused Chinese Zenodo record, plus 17 lower-level TeX/PDF files in `sources/non-european/chinese-arabic-completion-2026-06-04/`. Older partial Chinese-Arabic surface files were removed from the current reader folder and remain recoverable through prior Zenodo versions.

Noether and Weber are the most substantial current reader/translation surfaces. Noether has large German/English and multilingual working readers plus an active source-repair control lane; Weber has a repaired/source-witnessed `Lehrbuch` stream. SGA is serious but caveat-heavy: real page-local repair work exists, especially for SGA 5, but SGA should not be described as complete or globally source-faithful. EGA is lower-confidence OCR/original/source-support material. Cayley remains a repair/provenance lane with known source-faithfulness failures. The non-European corpus promotes broad work-level readers and source/reference material across Chinese, Indian/Sanskrit, Islamic/Arabic, Persian, Japanese, and reference surfaces, including the dedicated al-Battani work record; table placement, zodiac, auxiliary numerical tables, script typesetting, and source-completeness remain explicit audit targets. Deligne, Steinitz, Bianchi, Gordan, Maxwell, Gibbs, Frobenius, Kneser, Sylvester, Dedekind, Dirichlet, Gauss, Riemann, and Poincare should be read by their current record notes and package-level ledgers rather than by broad filename claims.

Recent additions include source-witnessed and working-reader packets for Dedekind, Dirichlet, Gauss, Sylvester, Steinitz, Noether, SGA, Weber, Deligne, non-European mathematics, al-Battani, and Ukrainian applied mathematics. Some older paths and filenames still contain strong words such as `complete` or `source-checked`; those words describe the package label at creation time, not current certification. In particular, older Cayley and SGA package names should not be read as final source-faithfulness claims.

Remaining work includes source comparison, layout repair, theorem/reference checking, mathematical proofreading, translation completion, and replacing imperfect machine-generated passages with verified text. The latest public typography audit is in `manifests/public_pdf_typography_audit_current.md`; it is a conservative repair queue rather than a pass/fail judgement. The linked main-page reader surface review is in `manifests/main_landing_reader_surface_review_20260529.md`.

## Contributing

Useful contributions include focused pull requests correcting TeX, typography, theorem numbering, cross-references, translations, or metadata; issues pointing to better public scans or existing TeX; and review notes comparing a reader PDF against source/reference text.

Please keep corrections narrowly scoped and cite the source page or file when possible. Large raw scans and preservation ZIPs live on Zenodo; GitHub is meant to stay forkable and reviewable.

## License and Citation

Unless a file or upstream source says otherwise, project-created material in this repository is dedicated under CC0 1.0 Universal, to the extent possible under law. Upstream projects, source scans, source texts, and historical authors retain their own provenance, credit, public-domain status, and license context.

For citation, use the relevant Zenodo record for the corpus you consulted. The main project record is https://zenodo.org/records/20393488.




















