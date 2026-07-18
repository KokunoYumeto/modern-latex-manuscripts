# French R823 final source-reconciliation audit

Date: 18 July 2026

## Frozen authority and target

- German authority: `Noether_R823_cum_de.tex`
- Authority SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`
- Expanded French target SHA-256: `C6D82EDA47B6B199D750B93FBF9A67AE2D94E20C2A7615A07FAE5D06980D2C05`
- Final French PDF: `output/pdf/cum_fr_R823_COMPLETE.pdf`
- Final PDF SHA-256: `6D6B23B3E196F0A76D179AFC359675EF97784D3091C391AFAA56FD6211F2FC9E`
- Final log SHA-256: `6F14ADE2B3D15E2F0E09EFEAEFC09A1D6599E5BE90B99B0CF73D5E69CF85E5FB`
- Final recorder SHA-256: `999A4820559C4E5913E9FAEFEABE30A84F86C088256AD9F75592DE5915295250`
- Final build: LuaLaTeX through `latexmk`, 494 A4 pages and 3,721,837 bytes, with zero TeX errors, package warnings, font warnings, missing glyphs, overfull boxes, or underfull boxes. The publish-directory PDF, log, and recorder are byte-identical copies of the reviewed bound build. Two independent Poppler renders of that frozen PDF match on all 494 page hashes.

The final source and target manifests contain exactly 81 units. Their SHA-256 values are `ED482400D9EC0C14EEEC8546249C719F26A85D3061D2DC79A19182246952D205` and `F7687CD44A873E75A7CE32705C8301916DA51B0D0498923ECAC9C6FF9C0B025F`. The exact pending parity seed, before evidence promotion, is `E86158187F2D8552DB7AD0724CECD3A78450A57CF1DA172EF3D4C5138702EEF4`.

## Audit method

Every unit was checked against the frozen R823 German slice, not merely against an older French witness. Review covered ordered headings and paragraphs, displayed mathematics and tags, inline symbols and dummy indices where R823 distinguishes them, theorem/definition/lemma topology, source notes and footnotes, terminal bibliographic records, and canonical French terminology. Repairs were made in the active 130-file include graph, then re-read from the live files. Independent audit passes were divided into disjoint tranches and followed by final expanded structural slicing.

The paper structure audit passes 43/43 (`PAPERS_01_43_STRUCTURE_FINAL.csv`, SHA-256 `18E7B72E80A24019B26991831AC0AD21B0888BF70CA8BFA23385B78727F45310`). The book audit passes 31/31 (`BOOK_STRUCTURE_FINAL.csv`, SHA-256 `16FA5991638721C94E3A7DD2D18D58A8618FA5C9ED6777666C3C75B1A1311071`). No paper is marked gross structural risk; no book section is missing or a parser failure.

## Papers P01--P21

Final status: PASS for `P01`, `P02`, `P03`, `P04`, `P05`, `P06`, `P07`, `P08`, `P09`, `P10`, `P11`, `P12`, `P13`, `P14`, `P15`, `P16`, `P17`, `P18`, `P19`, `P20`, and `P21`.

The final pass restored, among other source-visible details, the P09 fraktur-H family and Omega field symbols; P13 varkappa indices, suppressed summation indices, fraktur transformation symbols, explicit products, and the conserved first integral; P15 arbitrary exponent symbols; P17 varkappa families, finite-basis indices, congruences modulo the module, and Schmeidler indices; P19 divisor-direction semantics, families, formulas, notes, and canonical `étranger` terminology; and P20 the barred specialization, tag (12), and explicit Delta product. P06 `H^*`, P12 `\varkappa^\rho`, and P13 `\mathfrak T_r` are documented source emendations rather than silent deviations. P21 preserves the unresolved R823 reader-text `II,3` versus terminal-bibliography `III,3` conflict without guessing.

Paper 19 received a separate exhaustive second pass: all 12 sections, 51 footnotes, Definitions I--VIII, Theorems I--XV, Lemmas I--VI, and numbered formulas (1)--(5) pass. Its isolated strict build is 26 pages with no warnings, errors, missing glyphs, or layout defects; PDF SHA-256 `7AA28E32B908A20AF98447A253E425D9485CA2FEA307B50085746FA83A1F436C`.

## Papers P22--P43

Final status: PASS for `P22`, `P23`, `P24`, `P25`, `P26`, `P27`, `P28`, `P29`, `P30`, `P31`, `P32`, `P33`, `P34`, `P35`, `P36`, `P37`, `P38`, `P39`, `P40`, `P41`, `P42`, and `P43`.

This 22-unit tranche was re-read after the late repairs and frozen with zero residual blockers. The audit covered exact theorem/formula streams, note order, Galois-closure and exponent notation, source-assigned footnote resets, Russian-summary metadata, and the complete R823 reconstruction of P43. The final P40 replay specifically verifies the reverse-centralizer direction at R823 line 19476 and the exact `e^{(i)}A` / centre / coefficient-extension chain at lines 19737, 19739, and 19745. Isolated tranche builds and the integrated cumulative build pass.

## Book and post-P43 units

Final status: PASS for `BOOK_TITLE_INTRO`, `BOOK_S01`, `BOOK_S02`, `BOOK_S03`, `BOOK_S04`, `BOOK_S05`, `BOOK_S06`, `BOOK_S07`, `BOOK_S08`, `BOOK_S09`, `BOOK_S10`, `BOOK_S11`, `BOOK_S12`, `BOOK_S13`, `BOOK_S14`, `BOOK_S15`, `BOOK_S16`, `BOOK_S17`, `BOOK_S18`, `BOOK_S19`, `BOOK_S20`, `BOOK_S21`, `BOOK_S22`, `BOOK_S23`, `BOOK_S24`, `BOOK_S25`, `BOOK_S26`, `BOOK_S27`, `BOOK_S28`, `BOOK_S29`, `BOOK_S30`, `BOOK_S31`, `POST45_MAIN`, `POST45_NOETHER_SUPPLEMENT`, `BIBLIOGRAPHY`, `SHORT_NOTICES`, `BOOK_REVIEWS`, and `BOOKS_WITH_NOETHER`.

The 38-unit post-P43 audit found zero exact blockers. The book has all 31 sections; POST45 notes 1--16 and the split mark/text note are complete; bibliography is 43/43 plus the separate Kapferer citation; short notices are 12/12; book reviews are 5/5; books-with-Noether records are 2/2. Fresh isolated builds pass for the 44-page book, six-page Kapferer/Noether material, and four-page terminal matter.

## Final disposition

All 81 logical units are source-reconciled against the exact frozen R823 authority. Remaining differences are translated prose, harmless layout reflow, documented source emendations, or mathematically immaterial dummy renamings that do not collapse a distinction maintained by R823. The current 494-page PDF also passes the separately bound visual review: full render manifest SHA-256 `304FDFF689635779C33978E5CC63D0F3BF1D8818F3E0148E3B93751B34271218`, terminal manifest SHA-256 `5C43FD5BC2DE5A61FC48243AC9D8B82B9E6C965118EC90B7E63A298AC9CFA4BC`, and normalized all-page pixel binding SHA-256 `B693A0158DDC8C8E2DA3FEF970819C5E44F09C046E253C806C80730A1E25DFFC`. This audit is the common supporting review record for the final per-unit evidence corpus.
