# D031 independent content audit

Date: 2026-08-31. Read-only input: sibling `input_state`. Only `qa_content` is writable by this reviewer. No inherited acceptance conclusion is used.

## Primary identities

- Authority PDF `seed/20_AUTHORITY_DELIGNE_D031_SHIMURA_CANONICAL_MODELS_IAS_43PP.pdf`: SHA256 `591EE837C4C87E5263B76427B393742E111D615C6E098C940F132519A0861922`, 2,735,096 bytes, Poppler reports 43 pages.
- French `editions/french_diplomatic.md`: SHA256 `C3048CC18E53C1D348BB2F754668974DDDB6BC11C61AFFE3F664758E584DBFE1`.
- English `editions/english_translation.md`: SHA256 `F01974977265893171BA6D58AACC2558ED8FDD4F47161242E43B4E6E7CC5D771`.
- Apparatus `apparatus/apparatus.tsv`: SHA256 `46CAE369A83B1053D178CBEFA9EA616244C89772F6C9BE8C94996199A177BF3A`.

The PDF skill was fully read. All 43 authority leaves were rendered with Poppler at 180 dpi, to `authority-01.png` through `authority-43.png`. Source crops are direct Poppler render regions, not retouched images.

## Confirmed defects in immutable input

### C01 - introductory diagram source geometry (both languages)

Physical 3 / printed 249. Source places C(F) above C(E), with the quotient at right halfway between them. Both arrows into the quotient are oblique; the vertical norm arrow is labelled N_{F/E}. Both Markdown files instead place the quotient bottom-right and have `C(E) \\arrow[r]`. The vertical norm arrow exists, but the explicit both-diagonal source gate is not met. Use a three-row native layout with quotient in the middle-right and arrows dr/ur. This is a source-geometry defect, not an abstract graph change.

### C02 - omitted complex-base subscripts (both languages)

Physical 41 / printed 287, 2.7.11(a)-(b). French lines 1763/1765, English 1785/1787. Exactly three source terms carry a C subscript that is absent in both Markdown files:

- In (a), `M^0_{\\mathbf C}(G_i,G'_i,X_i^+)`.
- In (a), `M^0_{\\mathbf C}(\\prod G_i,\\prod G'_i,\\prod X_i^+)`.
- At the end of (b), `M^0_{\\mathbf C}(G,G'',X^+)`.

Do not blanket-add subscripts: the initial M^0 term in (b), and the term in preceding (c), are printed without C. Original-size inspection of `authority-41.png` establishes these three omissions.

### C03 - silently supplied group symbol in source-anomalous set (both languages)

Physical 11 / printed 257, display in 1.2.3. The source literally prints `G^*(R)={g in (C) | g=int(h(i))sigma(g)}`: no group symbol before `(C)`. Both Markdown files supply `G_{\\mathbf C}`. For a diplomatic edition, the display must retain `g\\in(\\mathbf C)` and document the missing source term separately. This is not a recommendation to adopt the incomplete expression as mathematically correct.

Direct crop `source11_Gstar.png`: `pdftoppm -f 11 -l 11 -r 300 -x 850 -y 2070 -W 1250 -H 200 -png -singlefile AUTHORITY PREFIX`.

### C04 - silently unified source-local z/r variables (both languages)

Physical 15 / printed 261, opening paragraph. Source literally has pairing `<mu,z>` followed by `pour r une racine`; both Markdown files substitute gamma in both places. Preserve `\\langle\\mu,z\\rangle`, followed by `$r$ une racine` / `for a root $r$`, and document the source mismatch. French also prints singular `de racine` within the preceding parenthesis; Markdown pluralizes it to `de racines`.

Direct crop `source15_root.png`: `pdftoppm -f 15 -l 15 -r 300 -x 720 -y 265 -W 1500 -H 310 -png -singlefile AUTHORITY PREFIX`.

### C05 - subscript plus substituted for source superscript plus (both languages)

Physical 20 / printed 266, prose in 2.1.6, French line774 / English794. Replace only the prose `\Gamma\subset G_1(\mathbf Q)_+` by source-literal `\Gamma\subset G_1(\mathbf Q)^+`. Do not change the subscript-plus groups in equation (2.1.6.2): they really are subscripted. Direct source crop `source20_plus.png` is decisive.

### C06 - silently supplied finite-adele exponent (both languages)

Physical 20 / printed 266, the same prose paragraph as C05, French line774 / English794. Source literally defines `\Gamma=\rho\widetilde G_0(A)\cap G_1(\mathbf Q)`; the Markdown silently prints `A^f` in this definition. Replace only this occurrence by `A`, with a source-anomaly apparatus note. The adjacent closure notation and displayed formulas use `A^f` and must remain unchanged. Direct source crop `source20_plus.png` shows the difference at 300dpi.

### C07 - two injection hooks omitted (both languages)

Physical 31 / printed 277, diagram (2.4.8.1), French line1261 / English1281. Both vertical source arrows have hooks. Replace the two `\arrow[d]` commands on this one line by `\arrow[d,hook]`. Source crop `source31_hook.png` shows both hooks. The subsequent archimedean diagram has ordinary vertical arrows and must not be altered.

### C08 - arrow supplied across a source-literal gap (both languages)

Physical 37 / printed 283, first, unnumbered diagram in 2.5.8, French line1590 / English1612. The source has bottom objects `H(Q)`, dots, and `pi_0 pi(T)`, but no horizontal arrow from the dots to `pi_0 pi(T)`. The Markdown supplies one. Replace that diagram's `\cdots \arrow[r] \arrow[u]` by `\cdots \arrow[u]`, retaining the upward arrow and all other arrows. Record the source-literal missing arrow in the apparatus. Do not alter either numbered diagram on the same page: (2.5.8.1) has both dots and the bottom horizontal arrow, and (2.5.10.1) also has its bottom arrow. Direct source crop `source37_arrows.png` establishes the distinction.

### C09 - inaccurate copy-matter statements (apparatus only)

Physical 30 / printed276 and physical33 / printed279 are tightly cropped single-page scans. They contain the running head and folio, but no scanner border or neighboring-page sliver. Apparatus entries A088 and A097 incorrectly assert both. Remove the border/sliver claims from these two entries, retain the actual running head/folio exclusions, and describe their true single-page crop. This is an evidentiary-description defect, not missing body text. The rest of the source visual pass found no further categorical copy-matter mismatch.

## Initial-pass coverage and limits

All 43 authority pages, physical1-43 / printed247-289, have been visually inspected at legible 180dpi or original-size rendering. All page-local folios, first/last owned-text boundaries, section and result topology, numbered displays, and native-diagram incidence/labels were checked. The seven Dynkin diagrams on physical15 were compared for values, circles, underlines, and bond directions; no further definite fault was found there. This is a full-page topology and focused mathematical-symbol audit, not a character-by-character certification of every source glyph.

The four required fault sites were checked directly, without accepting inherited resolutions: page3 has its vertical norm arrow but C01 applies to oblique geometry; page16 2.0.1(a) has `r(\varphi(\gamma))` with no extra `g`; page38 uses `r_{G,X}(\sigma)` with no inverse in the sign convention (the inverse in Theorem2.6.3 is separate and legitimate); page43 bibliography item5 is Expose389. All13 bibliography entries, the SGA line and the terminal address are present. The exact authority has43 leaves and ends printed289; its publication header claims247-290, but no290 leaf exists and none may be invented.

Mechanical whole-edition comparison lives in `mechanical_alignment.json`: 43 matched BEGIN/END physical/printed page pairs; 23 native tikzcd environments and seven native tikzpicture environments per language; 36 `\tag{}` labels per language, plus the special `(1)_m` tag. The math tokenizer identifies3,201 French and3,192 English spans; all emitted cross-language differences were reviewed. No additional definite translation-only formula damage was found. Differences consist of translated prose inside math, word-order changes, omitted repeated symbols whose referents remain explicit, inline/display regrouping, or clarifying parentheses (notably physical17 and39). There are108 French and111 English `\[` displays; this is regrouping, not three missing source formulas. The separately tagged equation environment on16 is outside this simplistic display counter.

Translation wording is generally clear mathematical English. The English regularizes several openly documented source grammatical anomalies. One discretionary wording concern remains at physical14 / Englishline459: source's displaced phrase `essentiellement equivalent` is lost in the fluent rendering. A more conservative English final sentence would say `This problem is essentially equivalent to the one solved by Satake in [11].` Because the source itself is syntactically damaged and A039 discloses regularization, this is not promoted to an additional high-confidence formula defect or a new acceptance blocker.

The comparison-only PDF was separately hashed: SHA256 `5A8B592C4A1BF21CBA5403B4CE8584D772CD7E907DD8B6EC7FCF9FE8E03605AC`, 1,331,405 bytes,43 pages. Comparison leaves1,3,11,15,20,31,37,41,43 were rendered and inspected. They support the above anomaly readings, but did not replace controlling authority pixels. No evidence from inherited salvage conclusions was used as acceptance.

Initial decision: immutable input is NOT source-agreement clean, because C01-C08 and apparatus C09 are open there. Parent owns staged repairs and PDF QA. A separate nonpatching pass of frozen normalized editions, beginning at page1, is required before this reviewer can issue any revised acceptance statement. It must verify the exact frozen hashes and changes, not presume repairs from messages. No final rendered-output acceptance is asserted in this report.

## Direct crop identities

All crops are produced directly by Poppler from the authority identified above, at300dpi, and are unretouched:

- `source11_Gstar.png`: SHA256 `6CAC1A9608EC46A937F8246B6F087B8250872EC6D8BA2A97783C2C3630EE21FC`.
- `source15_root.png`: SHA256 `08B774FA5576F35BF43DD0EBA8AAF3A2F71F26AB1238F1C10E21CF0007080A64`.
- `source20_plus.png`: SHA256 `7F4DEBB2594B10788F8DC209FFFAC8770A5DC066688919A89D8DA2032ADBF8BE`; `-f20 -l20 -r300 -x320 -y2370 -W1580 -H550`.
- `source31_hook.png`: SHA256 `727AC063E49C84CA5747FE1781539A8036E24E900A001F646F0AD3DD34C21229`; `-f31 -l31 -r300 -x750 -y1300 -W1400 -H600`.
- `source37_arrows.png`: SHA256 `2F91725EB5BC5177994DF82B12E6FD7CFBA517FFEC13D96F576A410F89BA1BF9`; `-f37 -l37 -r300 -x900 -y620 -W1150 -H810`.

Next executable action: obtain exact frozen normalized edition and apparatus paths/hashes from the parent; read-only independent page1-through43 recheck, logging any remaining defect without patching.
