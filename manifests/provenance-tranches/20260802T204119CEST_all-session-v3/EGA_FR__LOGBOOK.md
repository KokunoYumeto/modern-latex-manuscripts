# Logbook

## 2026-08-01

- Opened one no-overwrite canonical French EGA source root.
- Bound the eight NUMDAM authorities (1,800 PDF pages total).
- Adopted the explicit diplomatic-source rule: reproduce the French source as
  printed; do not silently correct it.
- Added the English-correction triple-check rule: every English source
  intervention must be rechecked against the NUMDAM image while its French
  locus is transcribed.
- Reused the only discovered French TeX seed,
  `<REDACTED_USER_HOME>\Downloads\EGA\ryankeleti_ega\fr\ega1\intro-fr.tex`,
  6,179 bytes, SHA-256
  `CDE115CD02E26B6C065BABA88353A1A95A0FD029029242D7CA5A4BBEF6FE6D0A`,
  as provisional witness material. It currently ends partway through EGA I
  printed page 7 and is not yet admitted as source-exact.
- Personally checked that seed against direct 1400-dpi NUMDAM page images for
  physical pages 4–6 / printed pages 5–7. Restored the source's unaccented
  capital `A` in `A Oscar Zariski` and `A titre informatif`.
- Transcribed the remainder of the Introduction through printed page 9 from
  direct 1400-dpi authority images. The admitted file is
  `source/ega1/intro-fr.tex`, 16,433 bytes, SHA-256
  `CE78400CD9DBC36A4D11CC933B7BE18BEAC0C69AE6A04FBA3ECFA86053572980`.
- Built the isolated Introduction successfully as a four-page PDF and
  inspected all four rendered pages. The QA PDF is 131,176 bytes, SHA-256
  `67364F7711B67747CF2558E154B4CABBA32E439305FE243F394EBA1BCA9C7B81`.
- Personally checked original physical pages 2–3 at 1400 dpi and added
  `source/ega1/frontmatter-fr.tex`. The original title/imprint text is
  transcribed diplomatically; the publisher's graphic device is not inserted
  as a raster.
- Confirmed one prior English error during the same source pass: EGA I printed
  page 8 says `chap. IX`, not the English `Chapter XI`. This will be corrected
  only in a no-overwrite English successor; the French source remains exact.
- Advanced the exact French cursor to printed page 11 / physical PDF page 10;
  printed page 10 is blank.
- Compiled the admitted title/imprint and Introduction together. The six-page
  QA PDF is 170,918 bytes, SHA-256
  `99778A474DFAA7393209330447AC92D968412FF39A8FA8C0CA440966FF96C5EA`;
  all six pages were personally inspected at 600 dpi without clipping or
  overlap. The title/imprint source is 1,120 bytes, SHA-256
  `D506B87684E2136E3F87495190EECDF40B79DB8887ED71093C4CD56648E282A9`.
- Transcribed EGA I printed pages 11–12 / physical PDF pages 10–11 as
  `source/ega1/ega0-1-fr.tex`. Full-page authority renders were inspected at
  1400 dpi; the page-11 formulas in 1.0.2–1.0.3 were separately inspected in
  five direct 5000-dpi crops, confirming the $M_{[\varphi]}$ notation,
  $u(a.x)=\varphi(a).u(x)$, and both tensor-product maps.
- The admitted pages-11–12 source is 7,585 bytes, SHA-256
  `A36B1566B19094BD52B1BEEF0775806F7E6A336F148C45E558BB9321658F8C39`.
  Its two-page bounded QA PDF is 140,000 bytes, SHA-256
  `EEE676432A99BD65F8999E7DEF103A4C30A25CDC12CFBD31844B9AEAAEE3E4E3`;
  two pdfLaTeX passes completed without TeX
  warnings or layout diagnostics, and both rendered pages were personally
  inspected.
- Advanced the exact French cursor to printed page 13 / physical PDF page 12,
  the opening of §1.2.
- Transcribed EGA I printed pages 13–15 through the end of 1.3.5. The current
  `source/ega1/ega0-1-fr.tex` is 16,717 bytes, SHA-256
  `82223E0DC81FCF4A79DB75DC184E8BBFAF01EEFAE2BA0B4B80E28313A94206DD`.
- Personally inspected 13 direct-authority 5000-dpi formula crops covering the
  equivalence relation and addition law in 1.2.2, both universal
  factorizations, the tensor and prime-localization formulas, both exact
  sequences, the sum/intersection identities, and the direct-limit,
  tensor-product, and Hom morphisms on printed pages 13–15. Every checked
  symbol, arrow, subscript, superscript, and empty-intersection sign agrees
  with the French TeX; no correction was required. Exact crop identities are
  in `controls/EGA1_PRINTED13_15_DIRECT_AUTHORITY_5000DPI_CROPS.csv`, 2,514
  bytes, SHA-256
  `B56B08ED9958A1CF4FD3C417953C5E2B6CB1EDA502A4F1E0F0C919F00C4E2D49`.
- Rebuilt the bounded Chapter-0 reader through 1.3.5. The five-page PDF is
  `qa/ega1_chapter0_build/ega0-pages11-15-check.pdf`, 200,376 bytes, SHA-256
  `61F087C769E27D25452F32B7DAA10EB33AB149F739901B60CB714BE03409C42F`.
  Two pdfLaTeX passes completed without TeX or layout diagnostics; all five
  rendered output pages were personally checked without clipping or overlap.
- Advanced the exact French cursor to printed page 15 / physical PDF page 14,
  immediately before §1.4, `Changement de partie multiplicative`.
- Transcribed the rest of printed page 15 and all of printed page 16 through
  1.4.5 from the direct NUMDAM image. The current Chapter-0 source is 21,874
  bytes, SHA-256
  `32162026A0D9D8FBEEE291CD5029905AEC82F219153778DE88BF2FE073D2BFF0`.
- Personally checked the 1.4.1 maps and naturality square, both 1.4.2 squares,
  the 1.4.4 composition law, and the full 1.4.5 filtered-family notation,
  triangular diagram, injectivity argument, and limit isomorphisms against
  direct 5000-dpi authority crops. The four diagram blocks are reconstructed
  natively in TeX/TikZ; no source raster is delivered. Exact image identities
  are bound in `controls/EGA1_PRINTED15_16_DIRECT_AUTHORITY_IMAGES.csv`, 2,483
  bytes, SHA-256
  `7DA744A8488A80EB98C4E2FF6A285DE428E73779C330F4029C46176C904F8AE4`.
- Rebuilt after the actual source edits. The six-page bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-16-check.pdf`, 225,980 bytes, SHA-256
  `7FC9F7C08EB3B0FD02A8D4149ADD1B05F0F6E3DA8B275E359C16004AE0001537`.
  Three pdfLaTeX passes completed without warnings or layout diagnostics; all
  six output pages were personally inspected, including every reconstructed
  diagram and both printed-page seams.
- Advanced the exact French cursor to printed page 17 / physical PDF page 16,
  immediately after 1.4.5.
- Transcribed EGA I printed pages 17–18 through 1.5.6. The current Chapter-0
  source is 27,966 bytes, SHA-256
  `875EE5687438B3D516CB0F563CFBE02F1C47EF0C8C29374928F1513A8A3282BB`.
- Personally checked the iterated-localization map, change-of-ring
  factorizations, sigma, tensor and Hom base-change maps, tau and its inverse,
  both 1.5.5 isomorphisms, and all three 1.5.6 squares against direct
  5000-dpi NUMDAM crops. The three squares are reconstructed as native
  TikZ-cd diagrams; no raster is delivered. Fourteen exact source images are
  bound in `controls/EGA1_PRINTED17_18_DIRECT_AUTHORITY_IMAGES.csv`, 2,683
  bytes, SHA-256
  `FB4FA838AB77DD9504B2D3F0143D6628AFB0B40E0BA6A503DF3650635028DF27`.
- Rebuilt after the source edits. The eight-page bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-18-check.pdf`, 240,401 bytes, SHA-256
  `053A06999DD9AF67F0155E2271BCDBC084D6FCA2030C82F87A83BEECBC9B5116`.
  Three pdfLaTeX passes completed without warnings or layout diagnostics; all
  eight output pages were personally inspected, including the printed-page
  seam and the seven native diagram blocks.
- Advanced the exact French cursor to printed page 19 / physical PDF page 18,
  immediately after 1.5.6.
- Transcribed EGA I printed pages 19–20 through 1.7.5. The admitted Chapter-0
  source is now 35,851 bytes, SHA-256
  `4532B9AEF6885F7B75D717E5A2A62AAD89B5918914D7272CDFC5D5926620A525`.
- Personally checked the 1.5.7 composition formulas, 1.5.8 minimal-prime
  argument, 1.6.1 direct system, 1.6.2 naturality square, and the complete
  1.7.1–1.7.5 support argument against direct 5000-dpi vector-crop authority
  renders. The 1.6.2 square is reconstructed as native TikZ-cd; no source
  raster is delivered. Exact whole-page and detail-image identities are bound
  in `controls/EGA1_PRINTED19_20_DIRECT_AUTHORITY_IMAGES.csv`, 11 rows / 2,426
  bytes, SHA-256
  `A02A0271C21E1A037F942B018C57306D3719068164E5714B105CEFE508087FDF`;
  disk replay is 11/11 with errors 0.
- A first page-locator attempt exposed the offset between physical PDF page and
  printed page: the image initially named for printed page 19 was visibly page
  20. It was renamed before use; true printed page 19 was then rendered from
  physical PDF page 18. No mislabelled image entered the evidence manifest or
  the transcription decision surface.
- Direct 5000-dpi Poppler crops exceeded its allocation path and rendered
  blank. Those failed images were excluded. The admitted detail evidence uses
  vector-cropped one-page PDFs rendered by MuPDF at 5000 dpi; every admitted
  crop was personally inspected at original detail.
- Rebuilt after the source edits. The ten-page bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-20-check.pdf`, 272,504 bytes, SHA-256
  `B630BB835DC57227F4109A95BC713A5BCCDCD7E96EAEDD2A07A9D52F34D42CE5`.
  Three pdfLaTeX passes converged; pass 2 and pass 3 console logs are
  byte-identical. There are no build errors, undefined references, overfull or
  underfull boxes, missing characters, or duplicate destinations. The sole
  warning is the expected hyperref PDF-string warning for the mathematical
  subsection title. Output pages 8–10, covering the prior seam and both newly
  admitted pages, were personally inspected at 600 dpi and pass layout and
  native-diagram review.
- Froze the mechanical English-correction recheck queue as 60 unique rows in
  `controls/ENGLISH_CORRECTION_RECHECK_MASTER_QUEUE.csv`, 57,785 bytes,
  SHA-256
  `BF17F5ADEC2CD3E26B3AE30C463EEB4803ED55B5279AED5812852FBF34DD9CDA`.
  This is locator material only; no queued claim becomes a source correction
  without personal direct-NUMDAM image adjudication.
- Advanced the exact French cursor to printed page 21 / physical PDF page 20,
  immediately after 1.7.5.
- Transcribed printed page 21 through 2.1.4 from the direct authority. The
  closures $\overline{\{x\}}$, the relation
  $\overline{\{y\}}\subset\overline{\{x\}}$, the $(T_0)$ axiom, the
  $\supset$ order, and all $U_\alpha$ intersections were personally resolved
  in four direct 5000-dpi vector crops. Exact evidence is bound in
  `controls/EGA1_PRINTED21_DIRECT_AUTHORITY_IMAGES.csv`, 5 rows / 1,163 bytes,
  SHA-256
  `F921AF92129D1B1CEADD8FA5CEFAC3EF18AC1F97879CFD042C76F34242139295`;
  disk replay is 5/5 with errors 0.
- Transcribed printed page 22 through 2.1.8. The complement in
  $U_i=Z_i\cap\complement(\bigcup_{j\ne i}Z_j)$, all closure bars, and every
  occurrence of the fiber $f^{-1}(y)$ were personally checked in four direct
  5000-dpi vector crops. Exact evidence is bound in
  `controls/EGA1_PRINTED22_DIRECT_AUTHORITY_IMAGES.csv`, 5 rows / 1,164 bytes,
  SHA-256
  `7A8D101AB8AD123818D4B4C2771C758505A219B071D5B5BAA646DB64A88BB645`;
  disk replay is 5/5 with errors 0. Neither printed page contains a diagram.
- Rebuilt after both page edits. The twelve-page bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-22-check.pdf`, 297,949 bytes, SHA-256
  `116B55F4955640358431DDF335A55F65C5948A5747AB0930888428BF653E440A`.
  Three pdfLaTeX passes converged and pass 2/pass 3 console logs are
  byte-identical. There are no errors, undefined references, box diagnostics,
  missing characters, or duplicate destinations; only the already-recorded
  mathematical-bookmark warning remains. The p.21 and p.22 output pages and
  both prior seams were personally inspected at 600 dpi and pass layout review.
- The admitted EGA I Chapter-0 source through 2.1.8 is now 43,421 bytes,
  SHA-256
  `04D2E173C9E48819B8D4BD24B772E96FF79CC53CC3B160CFEDBFFD744CE3F725`.
- Advanced the exact French cursor to printed page 23 / physical PDF page 22,
  immediately after 2.1.8.
- Transcribed printed pages 23–24 through 3.1.4 directly from the NUMDAM
  authority. Printed page 23 closes the Noetherian-space subsection and opens
  the supplement on sheaves; printed page 24 completes axiom (F), condition
  (E), and the discussion of sheaves of topological rings. The category letter
  K, all alpha-beta orders, the Hom product, both compatibility composites,
  the restriction maps, the three printed footnotes, and the source wording
  `représentations continues` were personally resolved in ten direct
  5000-dpi vector crops. Neither page contains a diagram.
- Bound both whole-page authority renders and the ten 5000-dpi detail images
  in `controls/EGA1_PRINTED23_24_DIRECT_AUTHORITY_IMAGES.csv`, 12 rows /
  2,780 bytes, SHA-256
  `274E7BD39765061551AF521987A1CD96AA3EF254F8448AEC198E1FEB70964E8A`.
  The first crop-rendering command reached its outer time limit only after all
  five printed-page-23 image files had completed; the combined manifest later
  replayed 12/12 paths with size and SHA errors 0. There are no English
  correction-queue rows at printed pages 23–24.
- Rebuilt after the source edit. The fourteen-page bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-24-check.pdf`, 370,590 bytes, SHA-256
  `6BB07D4C554F0B882ED67BC55D03494FDF2646C326F17387BEBC4AF89A035F11`.
  Three pdfLaTeX passes converged; pass 2 and pass 3 console logs are
  byte-identical at SHA-256
  `D543AB1C546F11B999AF66382987410A9BF95836C0819D40E1925D18D05064DB`.
  There are no errors, undefined references, box diagnostics, missing
  characters, or duplicate destinations; only the already-recorded
  mathematical-bookmark warning remains. Output pages 12–14, covering the
  preceding seam and all newly admitted text, were personally inspected at
  600 dpi and pass layout review.
- The admitted EGA I Chapter-0 source through 3.1.4 is now 51,640 bytes,
  SHA-256
  `65F448FFF0B242E77C5709B231F27580CB7B3035B3A00352D7227455AA943496`.
- Advanced the exact French cursor to printed page 25 / physical PDF page 24,
  immediately after 3.1.4.
- Transcribed printed page 25 through 3.1.6 directly from the NUMDAM authority.
  The induced-presheaf notation, stalk as a filtered inductive limit, germ and
  support conventions, and the explicit rejection of the étalé-space viewpoint
  were personally resolved in four direct 5000-dpi vector crops. Neither 3.1.5
  nor 3.1.6 contains a diagram.
- Direct image review found the printed mismatch now recorded as
  `EG-EGA-I-P25-GAMMA-U-V-SRC-TYPO-001`: the source writes `u_V(s)` but then
  quantifies `s\in\Gamma(U,\mathcal F)`. The English erratum to
  `\Gamma(V,\mathcal F)` is justified. In accordance with the diplomatic
  transcription rule, the French TeX preserves the printed `U` and the source
  typo is catalogued separately.
- Bound the whole-page context and four direct 5000-dpi detail images in
  `controls/EGA1_PRINTED25_DIRECT_AUTHORITY_IMAGES.csv`, 5 rows / 1,228 bytes,
  SHA-256
  `ED36A97EB8CB526EDC8CB5443B5DF63E626FD9CEA8615904039216462C6CE774`;
  disk replay is 5/5 with errors 0.
- Rebuilt after the source edit. The fourteen-page bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-25-check.pdf`, 374,853 bytes, SHA-256
  `F57C8A70216AC3972551D1811CB82B7446277253C85E72EDEEDE0A09477E6B95`.
  Three pdfLaTeX passes converged; pass 2 and pass 3 console logs are
  byte-identical at SHA-256
  `EAE425FCC4B24B3A58A01CFAC7BC2764022165E7D12154E3A91B540F44C280A5`.
  There are no errors, undefined references, box diagnostics, missing
  characters, or duplicate destinations. Output pages 13–14, including the
  printed-page-24/25 seam and all newly admitted text, were personally
  inspected at 600 dpi and pass layout review.
- The admitted EGA I Chapter-0 source through 3.1.6 is now 55,116 bytes,
  SHA-256
  `824C0F7833DBEE04C90DE5799E5C013B13A84C112CBF06F85B69A772B69CC356`.
- Advanced the exact French cursor to printed page 25 / physical PDF page 24,
  at the opening of subsection 3.2 immediately after 3.1.6.
- Transcribed the complete subsection 3.2, printed pages 25–28, through 3.2.6.
  The restriction identities, all projective- and inductive-limit formulas,
  condition (F\textsubscript{0}), both printed footnotes, and the constructions
  of 3.2.3–3.2.6 were personally checked against ten direct 5000-dpi vector
  crops plus four whole-page authority images. No diagram occurs in this
  subsection.
- Confirmed source typo `EG-EGA-I-P27-BASE-X-VS-U-SRC-TYPO-001`: the printed
  French calls the restricted subfamily a basis of the topology of `X`, even
  though it consists of basis opens lying in a cover of $U$. The current
  English correction to `U` is justified; the diplomatic French retains `X`.
- Bound the complete subsection-3.2 image surface in
  `controls/EGA1_SECTION32_PRINTED25_28_DIRECT_AUTHORITY_IMAGES.csv`, 14 rows /
  3,091 bytes, SHA-256
  `49B5F664F971CBBA66EFB4C4BCC0E36F1EF5789C6BBA4E86C293DBFC9E78F847`;
  disk replay is 14/14 with errors 0.
- Adjusted only the bounded QA wrapper's `\oldpage` macro so page-local source
  footnote numbering is reproduced. The source body remains unchanged by this
  presentation repair. Rebuilt through 3.2.6 in three converged pdfLaTeX
  passes. The controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-28-check-r2.pdf`, 16 pages / 435,387
  bytes / SHA-256
  `F489EB80890F76E5D0AA93B89455574D8A51CAF69BBC45B7F6067B6B84B1A849`.
  Pass 2 and pass 3 console logs are byte-identical at SHA-256
  `B0C5236A47C5297122AB114CF967AC62B891A1B1017510996D1D0B9EE4138249`;
  errors, unresolved references, box diagnostics, missing characters, and
  duplicate destinations are all zero. Output pages 15–16 were personally
  inspected at 600 dpi and pass formula, footnote, seam, and layout review.
- The admitted EGA I Chapter-0 source through 3.2.6 is 66,133 bytes, SHA-256
  `EF843B088237A471B4DE2CD892858E9B7FA49AE9472711713EA3BA563F5D6C90`.
- Advanced the exact French cursor to printed page 28 / physical PDF page 27,
  immediately after 3.2.6 and before subsection 3.3.

## 2026-08-02

- Verified the admitted p. 28 checkpoint before resuming: source
  `source/ega1/ega0-1-fr.tex` remained 66,133 bytes at SHA-256
  `EF843B088237A471B4DE2CD892858E9B7FA49AE9472711713EA3BA563F5D6C90`;
  STATUS, LOGBOOK, and the three-row English adjudication ledger were intact.
- Generated whole-page 1400-dpi context for printed pages 29–31 and direct
  5000-dpi crops for subsection 3.3. A first crop invocation used the PDF
  page number as though it were the printed page number; the mismatch was
  caught before transcription, the files were segregated under
  `qa/ega1_chapter0_authority_5000dpi_details/superseded_wrong_page_mapping_20260802`,
  and no mislabeled image was admitted or used.
- Personally inspected the corrected direct-authority crops from physical PDF
  pages 27–28 / printed pages 28–29. Transcribed the complete subsection 3.3
  through 3.3.3, including the cocycle identity, both gluing constructions,
  equation (3.3.2.1), and two native TikZ commutative squares. No raster is
  delivered.
- Confirmed English mathematical transcription error
  `EG-EGA-I-P28-THETA-CODOMAIN-MISSING-LAMBDA-EN-001`: NUMDAM prints
  $\mathcal F_\lambda$ as the codomain of $\theta_{\lambda\mu}$, while the
  current English source omits the subscript and prints $\mathcal F$. The
  French TeX follows NUMDAM exactly; the English defect is recorded for a
  no-overwrite successor.
- Bound the subsection-3.3 authority evidence in
  `controls/EGA1_SECTION33_PRINTED28_29_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
  1,633 bytes / SHA-256
  `81BB8A99773638880D0B8E92E1FB192EF76FA8C56E9ACEAA41D0432D140F4DD4`;
  replay is 7/7 with errors 0.
- A preliminary PowerShell invocation passed the job-name variable literally
  and produced non-adjudicative `$job.*` scratch artifacts. They are excluded.
  The corrected literal-jobname build completed three converged pdfLaTeX
  passes. The controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-29-check-r3.pdf`, 18 pages / 446,138
  bytes / SHA-256
  `8AAE4F3E1BDDC0359B82F2F1DFC8168EB16EB3B6FC17E3AD86D9AACC0DABF430`.
  Pass 2 and pass 3 console logs are byte-identical at SHA-256
  `B8CF2AB2DCAD1BFD10ECC333252155D4BF93478AEF79A87FD5A818F77B2E9216`;
  errors, unresolved references, box diagnostics, missing characters, and
  duplicate destinations are all zero. Output pages 15–18 were personally
  inspected at 600 dpi for layout; both native squares, page seam, formulas,
  and surrounding prose pass.
- The admitted EGA I Chapter-0 source through 3.3.3 is 71,425 bytes, SHA-256
  `3E9195749E9B222763442D5B416D3EFA3A6C22702172484B4D4E6343F2A68629`.
- Advanced the exact French cursor to printed page 29 / physical PDF page 28,
  immediately after 3.3.3 and before subsection 3.4.
- Personally inspected printed pages 29–30 from whole-page 1400-dpi context and
  five direct 5000-dpi vector crops. Transcribed the complete subsection 3.4
  through 3.4.6, including the direct-image functor identities, the stalk
  morphism, the composition identity, and the source's exact support
  statements. The stalk square is native TikZ-cd; no raster is delivered.
- Bound the subsection-3.4 authority surface in
  `controls/EGA1_SECTION34_PRINTED29_30_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
  1,535 bytes / SHA-256
  `4C6ECB7292E0220849F27DF58398E24F3717C74C62CBE38327E22A46496546AA`;
  replay is 7/7 with errors 0.
- Rebuilt after the source edit in three converged pdfLaTeX passes. The
  controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-30-check-r4.pdf`, 19 pages / 454,885
  bytes / SHA-256
  `1206665EC07FA287E46A07D17A29E9278FC887F46CF2603AB9955EE58E623F65`.
  Pass 2 and pass 3 console logs are byte-identical at SHA-256
  `1EB101CE795E95D6A0FD348720416962DD2B0BEB2E1D06CEB11F3DDDF1C95443`;
  errors, unresolved references, box diagnostics, missing characters, and
  duplicate destinations are all zero. Output pages 17–19 were personally
  inspected at 600 dpi for layout; the p. 29 seam, all formulas, the native
  stalk square, surrounding prose, and the p. 30 ending pass.
- The admitted EGA I Chapter-0 source through 3.4.6 is 76,669 bytes, SHA-256
  `A35E2CA30ED99B0B77879597E0E2B2A6D664D3D4260AB872AC8CF55A683FF054`.
- Advanced the exact French cursor to printed page 30 / physical PDF page 29,
  immediately after 3.4.6 and before subsection 3.5.
- Personally inspected printed pages 30–33 from four whole-page 1400-dpi
  context images and direct 5000-dpi authority images. Transcribed the complete
  subsection 3.5 through 3.5.6 and 3.6.1–3.6.2, including the compatibility
  square, all manually tagged formulas, the printed footnote, and the exact
  page seams. The compatibility square is native TikZ-cd; no raster is
  delivered.
- Direct Poppler 5000-dpi full-page attempts for printed page 31 failed with
  memory-allocation errors and yielded blank artifacts. They were preserved
  but segregated under
  `qa/ega1_chapter0_authority_5000dpi_details/superseded_failed_poppler_memory_20260802`
  and were not admitted or used. A direct MuPDF 5000-dpi full-page rendering
  and five overlapping bands supplied the controlling authority evidence.
- Bound the complete printed-pages-30–33 authority surface in
  `controls/EGA1_SECTION35_36_PRINTED30_33_DIRECT_AUTHORITY_IMAGES.csv`, 25
  rows / 5,221 bytes / SHA-256
  `24DA0E86025CACB1043F1EF1E4C1DE10B8978DB24B00EEA3CCA0BAE47D7A1971`;
  replay is 25/25 with errors 0.
- Confirmed French source typo
  `EG-EGA-I-P33-SECOND-RESTRICTION-U-V-SRC-TYPO-001`: printed page 33 repeats
  $\mathcal F(X)\to\mathcal F(U)$ as the second restriction map where the
  argument requires $\mathcal F(X)\to\mathcal F(V)$. The diplomatic French
  retains the printed `U`. The current English also repeats `U`, so a
  transparent correction to `V` is pending in an append-only English
  successor. The five-row adjudication ledger is 4,242 bytes, SHA-256
  `B261BCD3FC68F9100E1245D52A4EE82816677D0701C1290841EE7D9755808A8F`.
- A first source insertion matched an earlier `\end{env}` instead of the active
  tail; the placement check caught it before compilation, and the unchanged
  block was moved to the correct no-overwrite tail. Initial equation-tagging
  attempts also exposed duplicate destinations and one mismatched environment;
  both were fail-closed and corrected before the controlling build.
- Rebuilt after the final source edit in three converged pdfLaTeX passes. The
  controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-33-check-r7.pdf`, 22 pages / 477,744
  bytes / SHA-256
  `023F30696AB3B400209A5B2D3A7425C783A262550162BA6FF2A15023C6D90126`.
  Pass 2 and pass 3 console logs are byte-identical at SHA-256
  `EE75565CA58B99F9DB90E2DADCC917408073C08CC060F711D9E2B604848B6210`;
  errors, unresolved references, box diagnostics, missing characters, and
  duplicate destinations are all zero. Output pages 20–22 were personally
  inspected at 600 dpi for output layout; formulas, native square, footnote,
  seams, and surrounding prose pass.
- The admitted EGA I Chapter-0 source through 3.6.2 is 90,363 bytes, SHA-256
  `A969C34AC1467670A63E77D5A413CFA469FA109FE5EE1928F91D0F91BEB73174`.
- Advanced the exact French cursor to printed page 33 / physical PDF page 32,
  immediately after 3.6.2 and before the next source unit on printed page 34.
- A first attempt to render printed page 34 invoked PDF command page 34 and
  therefore produced printed page 35. The visible header exposed the mapping
  error before transcription. The full page and bands were moved unchanged to
  `qa/ega1_chapter0_authority_5000dpi_details/superseded_wrong_page_mapping_20260802_p34`
  and were neither admitted nor used. The corrected authority command page is
  physical PDF page 33.
- Personally inspected the corrected complete printed page 34 and five
  overlapping direct 5000-dpi bands. Transcribed subsection 3.7 through 3.7.2
  diplomatically, including the construction of the inverse-image sheaf, the
  adjoint morphisms, the canonical homomorphism, the functoriality formula,
  induced sheaves, the stalk isomorphism, support identity, and exactness
  statement. No diagram or raster delivery is introduced on this page.
- Bound the printed-page-34 authority surface in
  `controls/EGA1_PRINTED34_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows / 1,614 bytes /
  SHA-256
  `49652D8AB9280E8DF627FF952B4D8E0DE387AC0602C49E5808F8F07E93CEEBE0`;
  disk replay is 7/7 with errors 0.
- Direct comparison found three inherited-English deviations. In both local
  representative conditions the NUMDAM source prints
  $s'_z=s_{\psi(z)}$, but the English has $s'_z=s_{\psi(x)}$. The source also
  says that $w$ is a homomorphism of `préfaisceaux d'ensembles`, while the
  English says sheaves. These are recorded under stable IDs
  `EG-EGA-I-P34-GPRIME-LOCAL-SECTION-PSI-Z-EN-001`,
  `EG-EGA-I-P34-USHARP-LOCAL-SECTION-PSI-Z-EN-001`, and
  `EG-EGA-I-P34-W-PRESHEAVES-VS-SHEAVES-EN-001`. The eight-row adjudication
  ledger is 6,508 bytes, SHA-256
  `32DDE8CD0CE00A2D12813B7C9457E52C72E73627DA95A2584BCE6A5F61357F76`.
- Rebuilt after the source edit in three converged XeLaTeX passes. The
  controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-34-check-r8.pdf`, 23 pages / 194,252
  bytes / SHA-256
  `ADFB9B4620D82BC2FB0609A1A1B07000C5BD23225792DE8ECAD4F4ACA9F85DEC`.
  Pass 2 and pass 3 console logs are byte-identical at SHA-256
  `ED86782B960190C9071E8929EED4FC6CCAFD9CBF9A02123487C5A0E0B8405676`;
  errors, unresolved references, box diagnostics, missing characters, and
  duplicate destinations are zero. Output pages 22–23 were personally
  inspected at 600 dpi for output layout; the p. 33→34 seam, formulas, and
  complete p. 34 body pass.
- The admitted EGA I Chapter-0 source through 3.7.2 is 94,753 bytes, SHA-256
  `54238F3758E867D416A2D4D6860F232C47495EB19F71B3A473847DF0763877B3`.
- Advanced the exact French cursor to printed page 34 / physical PDF page 33,
  immediately after 3.7.2 and before subsection 3.8 on printed page 35.
- Generated a fresh printed-page-35 authority image from physical PDF page 34,
  plus a direct 5000-dpi full page and five overlapping 5000-dpi bands. The
  band process exceeded one shell timeout after producing four valid files;
  the fifth band was then generated separately from the same immutable direct
  page. This was an image-preparation timeout only; no source was changed by
  it.
- Personally inspected all five direct bands and transcribed the complete
  closed unit 3.8.1–3.8.3, including the finite-cover argument, the topology on
  sections over non-quasi-compact opens, the associated pseudo-discrete
  sheaves of spaces/groups/rings, functoriality, and the closed-subsheaf
  statement. The later p. 35 opening of 4.1.1 is held for the direct p. 36
  seam rather than reconstructed across the printed hyphenation.
- Bound the subsection-3.8 authority surface in
  `controls/EGA1_PRINTED35_SECTION38_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
  1,637 bytes / SHA-256
  `1B8B2AAA69FFAA459B0340AFADAD2D3B14A5C2AB00FBC74D4DB6D2F4255FA68F`;
  replay is 7/7 with errors 0.
- Rebuilt after the source edit in three converged XeLaTeX passes. The
  controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-35-section38-check-r9.pdf`, 24 pages /
  198,394 bytes / SHA-256
  `DD4F3AE0BA5E086C6A0B9DD38DE457BB243A65732FA87FF9202CE9D8098DFB70`.
  Pass 2 and pass 3 console logs are byte-identical at SHA-256
  `00CAFFF43490270D855556FC84ECF149A23BCCCC7C49229F6B6FB75F930CC2F0`;
  substantive diagnostics are zero. Output pages 23–24 were personally
  inspected at 600 dpi for output layout; the 3.7→3.8 seam and complete 3.8
  body pass.
- The admitted EGA I source through 3.8.3 is 98,452 bytes, SHA-256
  `612A6BB7114D2E73734C89A138BC9F6ACD3D64229B3A366756955008E2A116DB`.
- Advanced the exact French cursor to printed page 35 / physical PDF page 34,
  immediately after 3.8.3 and before section 4 / 4.1.1 later on that same page.
- Generated and personally inspected the direct printed-page-36 authority
  image plus four overlapping 5000-dpi bands. Resolved the p. 35 `topo-` / p.
  36 `logique` printed-word seam as the lexical word `topologique`, while
  retaining the old-page boundary in the TeX source.
- Transcribed the section-4 and 4.1 headings, complete 4.1.1, and complete
  4.1.2. This includes the structure-sheaf notation, category of ringed
  spaces, composition formulas, injective/surjective criterion, canonical
  induced ringed subspace, and restriction morphism.
- Confirmed source typo
  `EG-EGA-I-P36-THETA-GF-VS-BA-SRC-TYPO-001`: NUMDAM literally prints
  $\theta:\mathcal G\to\mathcal F$ after naming the two structure sheaves
  $\mathcal A$ and $\mathcal B$. The inherited English erratum to
  $\theta:\mathcal B\to\mathcal A$ is mathematically and source-contextually
  justified. The diplomatic French retains the printed $\mathcal G\to\mathcal
  F$. The nine-row adjudication ledger is 7,342 bytes, SHA-256
  `5E36C1A7BCAA2B005C45A20B4CF2DD6CF42B30547AAF4180F5EC2256AE4311B8`.
- Bound the printed-page-36 authority surface in
  `controls/EGA1_PRINTED36_SECTION411_412_DIRECT_AUTHORITY_IMAGES.csv`, 6 rows
  / 1,445 bytes / SHA-256
  `96C554F48528EB3DC102B96CA58A9BFEFB1D4D117EB4A6CECA1EB951E9FB6B4E`;
  replay is 6/6 with errors 0.
- Rebuilt after the source edit in three converged XeLaTeX passes. The
  controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-36-through-412-check-r10.pdf`, 25 pages
  / 203,432 bytes / SHA-256
  `B6D2E33D55067864398EB614BBE7A41A1539340B54CE330B29D3239CDFB48AF7`.
  Pass 2 and pass 3 console logs are byte-identical at SHA-256
  `8D980EE87A8EF9C9CBEF80CEE4467E6EEAC2BF630BD9B58621A04D54258BA725`;
  substantive diagnostics are zero. Output pages 24–25 were personally
  inspected at 600 dpi for output layout; the 3.8→4.1 seam, mid-sentence old
  page marker, formulas, and complete 4.1.1–4.1.2 body pass.
- The admitted EGA I source through 4.1.2 is 101,997 bytes, SHA-256
  `645290C8A4851355F888B9C7D6ED9871B5F8C067F7D5236DD1AAB94D785399AA`.
- Advanced the exact French cursor to printed page 36 / physical PDF page 35,
  immediately after 4.1.2 and before 4.1.3 later on that same page.
- Reopened the complete printed-page-37 source image and all five overlapping
  direct 5000-dpi bands before editing. Transcribed the completion of 4.1.3 and
  all of 4.1.4 diplomatically, stopping before 4.1.5 at the bottom of the same
  printed page.
- Reconstructed the two printed 4.1.3 algebra diagrams as native
  `tikzcd`: the associativity square with
  `\varphi\otimes1`, `1\otimes\varphi`, and `\varphi`, and the
  commutativity triangle with `\sigma` and two `\varphi` arrows. No
  raster diagram entered the deliverable. Direct comparison of the inherited
  English 4.1.3–4.1.4 body found no new substantive mathematical or
  source-correction adjudication.
- The first output inspection caught two XeLaTeX/T1 visual encodings that the
  compile log did not flag: literal guillemets rendered as unrelated accented
  glyphs, and literal ordinal degree signs rendered incorrectly. Only the TeX
  spellings were changed to babel guillemets and superscript ordinal letters;
  the French wording remains the printed wording. The rebuilt output displays
  both correctly.
- Bound the printed-page-37 authority surface in
  `controls/EGA1_PRINTED37_SECTION413_414_DIRECT_AUTHORITY_IMAGES.csv`, 7
  rows / 1,693 bytes / SHA-256
  `6F332655F35196B09BF03CA6A556E1BDEE425445A15F082A3F0A09D98A4BFF05`;
  disk replay is 7/7 with errors 0.
- Rebuilt after the substantive source edit and visual-encoding repair in three
  converged XeLaTeX passes. The controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-37-through-414-check-r11.pdf`, 26
  pages / 210,367 bytes / SHA-256
  `16984C95D3637A92C2E567C5133E4C46DC23B0883D85CC95561E51358482DF03`.
  Pass 2 and pass 3 console logs are byte-identical at SHA-256
  `C4F7B57F4CD17A21AFC5EF31D57995055128A0B65183B45D519CC697B38CF027`;
  substantive diagnostics are zero. Output pages 24–26 were personally
  inspected at 600 dpi; the p. 36→37 seam, both native diagrams, ordinals,
  guillemets, formulas, and text layout pass.
- The admitted EGA I source through 4.1.4 is 106,790 bytes, SHA-256
  `D7A49BE473B9CE200E368583A30D6BC092445BED34E17DEA70796F9CE38B4502`.
- Advanced the exact French cursor to printed page 37 / physical PDF page 36,
  immediately after 4.1.4 and before 4.1.5 later on the same printed page.
- Generated the next authority page and caught a one-page command/printed-page
  offset from the visible header before transcription: PDF command page 38 is
  printed page 39. The already generated bytes were preserved under corrected
  `p39` names, and the true printed page 38 was then generated from PDF page
  37. Both printed pages now have 1400-dpi full-page context, direct 5000-dpi
  full-page witnesses, and five overlapping direct 5000-dpi bands.
- Personally inspected all p. 38 bands and the p. 39 completion band, then
  transcribed complete 4.1.5–4.1.7 diplomatically. This includes the tensor
  and two Hom bifunctors, stalk map, two exactness sequences, the
  $\Gamma$–Hom identity, duals, exterior powers, ideal-module products, and
  the full ringed-space gluing datum and cocycle condition. The exact hard
  stop is immediately before section 4.2 on printed page 39.
- Direct NUMDAM comparison confirmed four substantive inherited English
  errors: sheaf-Hom$(\mathcal F,\mathcal F)$ must be
  sheaf-Hom$(\mathcal F,\mathcal G)$; finite direct limits must be finite
  direct sums; the $\Gamma$–Hom display is missing a closing parenthesis; and
  $\mathcal A_\mu$ in the domain of $\varphi_{\lambda\mu}$ must be restricted
  to $V_{\mu\lambda}$. The frozen English global reader was not mutated. The
  four exact pending-successor rows expand the adjudication ledger to 13 rows
  / 10,468 bytes / SHA-256
  `35F3FEF37814390487939A47A6B1ECEEFE5B2115FAE8CE2AAFA8003E0AAFBDC0`.
- Bound the printed-pages-38–39 authority surface in
  `controls/EGA1_PRINTED38_39_SECTION415_417_DIRECT_AUTHORITY_IMAGES.csv`, 14
  rows / 3,174 bytes / SHA-256
  `802227EA49F2DFC0D164F893B0F358E94B735FB3739DA4364E62EA78C2592DDE`;
  disk replay is 14/14 with errors 0.
- A first R12 command invocation used PowerShell's automatic `$args` variable
  and reached XeTeX with no input filename. It changed no source and remains a
  non-controlling console. The corrected R12b build completed three converged
  XeLaTeX passes. The controlling reader is
  `qa/ega1_chapter0_build/ega0-pages11-39-through-417-check-r12b.pdf`, 27 pages
  / 216,957 bytes / SHA-256
  `3224B0D61163545F536AD2031E02E4862792AEECF63097CD0C1B9F2FAF15A460`.
  Pass 2 and pass 3 consoles are byte-identical at SHA-256
  `139BD4EE34C9BF9DF71C1CFE7ED0A7616011D17E0CEC4EA00CDEAF9CAE005C2B`;
  substantive diagnostics are zero. Output pages 24–27 were personally
  inspected at 1200 dpi; formulas, the p. 37→38 and p. 38→39 seams, and the
  sparse final page all pass.
- The admitted EGA I source through 4.1.7 is 113,787 bytes, SHA-256
  `566963EA399BBAD140695EFD21562A58332684AE779057999EC0A10056111CCE`.
- Advanced the exact French cursor to printed page 39 / physical PDF page 38,
  immediately after 4.1.7 and before section 4.2 / 4.2.1 later on that page.
- Reopened the remaining printed-page-39 direct 5000-dpi bands and transcribed
  the section-4.2 heading and complete 4.2.1. The source now contains the full
  direct-image construction on $\psi_*(\mathcal F)$, its transported
  $\mathcal B$-module structure, functorial action $\Psi_*(u)$, left
  exactness, and the induced $\mathcal B$-algebra $\Psi_*(\mathcal A)$.
  Direct comparison with the inherited English 4.2.1 found no additional
  substantive mathematical or source-correction discrepancy.
- Rebuilt after the 4.2.1 edit in three converged XeLaTeX passes. The
  controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-39-through-421-check-r13.pdf`, 27 pages
  / 218,964 bytes / SHA-256
  `C58E3B49AE20A991AE455F894EF9B49E49711CD362B3EBCEA19337E0ABC06031`.
  Pass 2 and pass 3 console logs are byte-identical at SHA-256
  `CFB2C64FE8D6F3C8F8D4598AB0AADD5957E9496B37250C36624E840CB3F02D81`;
  substantive diagnostics are zero. Output pages 26–27 were personally
  inspected at 1200 dpi and the 4.1.7→4.2.1 transition, displayed section
  formula, paragraph flow, and bottom envelope pass.
- The admitted EGA I source through 4.2.1 is 116,049 bytes, SHA-256
  `D1B790622506072272CD59636D8521A7A4942981112D71FCE50732D7A905D5BC`.
- Advanced the exact French cursor to printed page 39 / physical PDF page 38,
  immediately after 4.2.1 and before 4.2.2 later on the same printed page.
- Reopened the direct 5000-dpi printed-page-39 completion bands and personally
  inspected the complete printed-page-40 authority surface: a 1400-dpi page,
  direct 5000-dpi full page, and five overlapping direct 5000-dpi bands.
  Transcribed 4.2.2–4.2.6 diplomatically, including the two canonical tensor
  maps, native commutative square (4.2.2.2), sheaf-Hom map (4.2.3.1), induced
  algebra/module structures, the closed-subspace identifications, and the
  composition law for direct image. The exact hard stop is before 4.3.1 at the
  foot of printed page 40.
- Compared the inherited English 4.2.2–4.2.6 directly with the NUMDAM image.
  No additional substantive mathematical or source-correction discrepancy was
  found in this block; the existing English correction ledger remains at 13
  rows.
- Bound the printed-page-40 authority surface in
  `controls/EGA1_PRINTED40_SECTION422_426_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
  1,580 bytes / SHA-256
  `0A5BF4FD58281BDA78E11B5413049016FD004DA2B4CDE8DAEE217AFE9786781F`;
  disk replay is 7/7 with errors 0.
- Rebuilt after the 4.2.2–4.2.6 edit in three converged XeLaTeX passes. The
  controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-40-through-426-check-r14.pdf`, 28 pages /
  223,852 bytes / SHA-256
  `25E79B5BFFED283FDDE4B590BD08DF191B774E67E9DDCEC245E6143EA45FCCC9`.
  Pass 2 and pass 3 console logs are byte-identical at SHA-256
  `DC8B362F0BF1B967AACF1D17E669C28052AC2165E6928D7668DF4FE1D2F77460`;
  substantive diagnostics are zero. Output pages 27–28 were personally
  inspected at 1200 dpi; the printed-page seam, formula tags, native square,
  paragraph flow, and bottom envelope pass.
- The admitted EGA I source through 4.2.6 is 120,663 bytes, SHA-256
  `9F9E4670EEBFCF980107534B140486D9275C1F158BDB9BCBF6A2ECAF033CE054`.
- Advanced the exact French cursor to printed page 40 / physical PDF page 39,
  immediately after 4.2.6 and before 4.3.1 later on that printed page.
- Personally inspected the complete printed-page-41 authority surface: one
  1400-dpi context page, one direct MuPDF 5000-dpi full page, and five
  overlapping direct 5000-dpi bands. Transcribed complete 4.3.1–4.3.3
  diplomatically: inverse image of a $\mathcal B$-Module, functorial action and
  right exactness, stalk/support formula, preservation of inductive limits and
  arbitrary direct sums, and the canonical tensor-product isomorphism. The
  next source unit 4.3.4 begins later on printed page 41 but crosses the page
  seam and was deliberately left for the next bounded edit.
- Direct comparison against the inherited English found two new English
  defects. Its subsection heading says inverse image of an $\mathcal A$-module
  where NUMDAM says $\mathcal B$-Module, and 4.3.1 says `with the a` rather than
  `with a`. They are recorded append-only as
  `EG-EGA-I-P41-INVERSE-IMAGE-HEADING-A-VS-B-EN-001` and
  `EG-EGA-I-P41-ENDOWS-WITH-THE-A-EN-001`. The English reader remains frozen;
  the adjudication ledger now has 15 unique rows / 11,935 bytes / SHA-256
  `A642E00ED08027F09F7511F8D329D6C63AB0EBD7992C89CA094446AF9C836CED`.
- Bound the printed-page-41 authority surface in
  `controls/EGA1_PRINTED41_SECTION431_433_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
  1,611 bytes / SHA-256
  `DF271BCBBACFD18FAE6765EBBD6FCE378627DC4F0BB67FA063DE864410C24587`;
  disk replay is 7/7 with errors 0.
- Rebuilt after the 4.3.1–4.3.3 edit in three converged XeLaTeX passes. The
  controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-41-through-433-check-r15.pdf`, 29 pages /
  228,751 bytes / SHA-256
  `5D704DB7199C5A407B1F1A66CB9352FECCB11A7789B6CAB873E018CAAA92B5C4`.
  Pass 2 and pass 3 console logs are byte-identical at SHA-256
  `D016466E3A07C47C01D775DF324549EF17C2F8C37999CB54FF0A25A2DA30E201`;
  substantive diagnostics are zero. Output pages 28–29 were personally
  inspected at 1200 dpi; the 4.2.6→4.3 seam, displayed formulas, long
  paragraphs, equation tags, and final envelope pass.
- The admitted EGA I source through 4.3.3 is 125,306 bytes, SHA-256
  `2666EB3EBFB288B43BE117BC933C6635C47E568F58901966EF979D9E7EE769D5`.
- Advanced the exact French cursor to printed page 41 / physical PDF page 40,
  immediately after 4.3.3 and before 4.3.4 later on the same printed page.
- Reopened the bottom of printed page 41 and personally inspected all five
  overlapping direct 5000-dpi bands for printed page 42. Transcribed complete
  4.3.4–4.3.6 and complete 4.4.1–4.4.2 diplomatically, including the transported
  algebra/module structures, extension of ideal sheaves, inverse-image
  composition law, local description of a $\Psi$-morphism, and composition of
  $\Psi$-morphisms. Section 4.4.3 begins at the bottom of printed page 42 and
  crosses the next page seam, so it was deliberately left for the next bounded
  edit.
- Direct comparison against the inherited English found one new clear grammar
  defect: `a Psi-morphisms` must be singular `a Psi-morphism`, as the NUMDAM
  source explicitly says `un Psi-morphisme`. It is recorded append-only as
  `EG-EGA-I-P42-PSI-MORPHISM-PLURAL-EN-001`. No other source-backed
  mathematical correction was admitted in this block. The English ledger is
  now 16 unique rows / 12,725 bytes / SHA-256
  `12D77A4B55B68819482EF79BD0DDDDF1940497B0263B9CD4676F8E87D1EAE013`.
- Bound the printed-page-42 authority surface in
  `controls/EGA1_PRINTED42_SECTION434_442_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
  1,447 bytes / SHA-256
  `E513C415CCC0CE2C80B77E966C4FCD9F4BEB41568655DA4B4D3061B9CC3E6B35`;
  disk replay is 7/7 with errors 0.
- Rebuilt after the 4.3.4–4.4.2 edit in three converged XeLaTeX passes. The
  controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-42-through-442-check-r16.pdf`, 30 pages /
  233,722 bytes / SHA-256
  `4090B2BDBDFB2A1E0079C8F90B29C86C2ED38779DCBA3523D0219A5D634CA02A`.
  Pass 2 and pass 3 console logs are byte-identical at SHA-256
  `F97FEF4E1B95B937CD30C42C236A8BC702DC9FA052B33083F9A9C5532E9068BC`;
  errors, undefined references, overfull boxes, and underfull boxes are zero.
  Output pages 28–30 were personally inspected at 1200 dpi and the source-page
  seam, formulas, section transition, paragraph flow, and final envelope pass.
  The first R16 invocation accidentally passed the literal job name `$job` and
  fail-closed against an older auxiliary file; it did not alter source and is
  non-controlling. The correctly named R16 above is the admitted build.
- The admitted EGA I source through 4.4.2 is 130,128 bytes, SHA-256
  `6569D936D9733FCAC7D159A81E4A893813999C485211AF16E91E64082CB17900`.
- Advanced the exact French cursor to printed page 42 / physical PDF page 41,
  immediately after 4.4.2 and before 4.4.3 later on the same printed page.
- Generated and personally inspected the complete printed-page-43 authority
  surface: one 1400-dpi navigation page, one direct MuPDF 5000-dpi full page,
  and five overlapping direct 5000-dpi bands. Transcribed complete 4.4.3–4.4.5
  diplomatically, including the adjunction isomorphism and its unit/counit,
  stalk description, tensor compatibility, and inductive-system compatibility.
  Section 4.4.6 opens at the foot of printed page 43 and crosses the page seam,
  so it remains the next bounded unit.
- Direct English comparison found four further exact defects: a missing `from`
  in the deduction from 3.7.1; $\Psi^*(\mathcal B)$ substituted for the required
  $\Psi^*(\mathcal G)$ in the identity used to define $\rho_\mathcal G$;
  `neither ... or` instead of `neither ... nor`; and `inductive limit` instead
  of the source's `inductive system`. They are recorded under stable IDs
  `EG-EGA-I-P42-ON-EN-DEDUIT-MISSING-FROM-EN-001`,
  `EG-EGA-I-P43-IDENTITY-PSISTAR-B-VS-G-EN-001`,
  `EG-EGA-I-P43-NEITHER-OR-VS-NOR-EN-001`, and
  `EG-EGA-I-P43-INDUCTIVE-SYSTEM-VS-LIMIT-EN-001`. The ledger is now 20 unique
  rows / 15,655 bytes / SHA-256
  `8D42AE60CFF262CAB86414F6C935FEB120AB8CC635903763D68881C917341BF2`.
- Bound the printed-page-43 authority surface in
  `controls/EGA1_PRINTED43_SECTION443_445_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
  1,447 bytes / SHA-256
  `040B9F12688AE6C01EB0CE4E6CF83F196C1B59332E54F4ABE5E8A3E5D4AA25D0`;
  disk replay is 7/7 with errors 0.
- Rebuilt after the 4.4.3–4.4.5 edit in three converged XeLaTeX passes. The
  controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-43-through-445-check-r17.pdf`, 31 pages /
  238,968 bytes / SHA-256
  `F8C696FB78850DD30AF492EED1363C983ACFF0771EC16A961BCE4D4005715DBC`.
  Pass 2 and pass 3 consoles are byte-identical at SHA-256
  `BC8DDE07A24BC01F1B9A1DEA1579D557BFC227B8F60B181EE70F63C78C9CC795`;
  errors, undefined references, overfull boxes, and underfull boxes are zero.
  Output pages 29–31 were rendered at 1200 dpi; the unchanged seam pages are
  byte-identical to R16 and the new final page was personally inspected at
  original detail. Formula tags, adjunction notation, paragraph flow, and the
  bottom envelope pass.
- The admitted EGA I source through 4.4.5 is 135,215 bytes, SHA-256
  `CEFA8F1C49D9BFADD8AAE6485CB16926F316D8B9ADCFFDB95B1945414DC3B8FD`.
- Advanced the exact French cursor to printed page 43 / physical PDF page 42,
  immediately after 4.4.5 and before 4.4.6 later on the same printed page.
- Generated and personally inspected printed page 44 as one 1400-dpi context
  page, one direct MuPDF 5000-dpi full page, and five overlapping direct
  5000-dpi bands. Transcribed complete 4.4.6–4.4.8 diplomatically, including
  the two sheaf-Hom comparison morphisms, the native algebra square, and
  compatibility of the adjunction with composition. The section-5 heading and
  5.1.1 begin later on printed page 44, but 5.1.1 crosses the next page seam and
  remains the next bounded unit.
- A targeted 5000-dpi crop settled the sole ambiguous variable in 4.4.8:
  NUMDAM visibly introduces $u'$, but the same sentence defines
  $v''=v\circ v'$ and the arrow and induced map both use $v'$. Canonical French
  retains printed $u'$; the English correction must use $v'$ consistently and
  disclose the source typo. Together with `normaly` and duplicated `the a` in
  English 4.4.6, the new dispositions are
  `EG-EGA-I-P43-NORMALLY-MISSPELLED-EN-001`,
  `EG-EGA-I-P43-WITH-THE-A-DUPLICATE-ARTICLE-EN-001`, and
  `EG-EGA-I-P44-UPRIME-VS-VPRIME-SRC-TYPO-001`. The English ledger is now 23
  unique rows / 17,935 bytes / SHA-256
  `277A10AC2F4992324FDD99ADF4BF4CFAE4DEC3632E7D614CF5C222DB886946FB`.
- Bound the printed-page-44 authority surface in
  `controls/EGA1_PRINTED44_SECTION446_448_DIRECT_AUTHORITY_IMAGES.csv`, 8 rows /
  1,703 bytes / SHA-256
  `546E619E921611A06771E1EF81CCDF66BBA8741E631818A26CC3A053F6342408`;
  disk replay is 8/8 with errors 0.
- The initial R18 build exposed one 15.99-pt overfull line in the long inline
  Hom parenthesis. An invisible line-breaking adjustment was made without
  changing source wording or mathematics. R18 and R18b remain non-controlling
  diagnostics; the clean controlling build is R18c.
- The controlling bounded reader
  `qa/ega1_chapter0_build/ega0-pages11-44-through-448-check-r18c.pdf` is 32
  pages / 242,699 bytes / SHA-256
  `5422464FB4524DA0AC2E3AEC5975A19902431A33CFE3DB0C71A34746ABCD6B2B`.
  Three XeLaTeX passes converged; pass 2 and pass 3 consoles are byte-identical
  at SHA-256
  `DB3791E9FE259A576457BB77A2AEAD82324206FE6E530F70F3E81695CF5B9A5F`;
  errors, undefined references, overfull boxes, and underfull boxes are zero.
  Output pages 30–32 were rendered at 1200 dpi and personally inspected. The
  source-page seam, long Hom formulas, native commutative square, composition
  arrows, labels, paragraph flow, and bottom envelope pass.
- The admitted EGA I source through 4.4.8 is 138,365 bytes, SHA-256
  `3809F1D1371983AE85F2B37CDDB2FFAD5AF9944CFA10A99C17FED4B945EEFA64`.
- Advanced the exact French cursor to printed page 44 / physical PDF page 43,
  immediately after 4.4.8 and before section 5 / 5.1.1 later on the page.
- Generated and personally inspected printed page 45 as one 1400-dpi context
  page, one direct MuPDF 5000-dpi full page, five overlapping direct 5000-dpi
  bands, and one targeted 5000-dpi crop of the finite-type sentence. Transcribed
  section 5 through complete 5.2.1 diplomatically. The opening of 5.2.2 remains
  out of scope for this checkpoint because it crosses onto printed page 46.
- Direct comparison confirmed a French source typo in 5.1.3: the source
  introduces an open neighbourhood $U$ and then uses undefined $V$ in all
  three restrictions. Canonical French retains the printed $V$ occurrences;
  the inherited English use of $U$ is justified and recorded under
  `EG-EGA-I-P45-QUASICOHERENT-U-V-SRC-TYPO-001`. English also contains an
  explicitly marked Erratum-II sentence absent from the NUMDAM body; it was
  not imported into diplomatic French and is held under
  `EG-EGA-I-P45-ERRATUM-II-EXTERNAL-ADDITION-001` pending a separately bound
  errata authority. The English ledger is now 25 unique rows / 19,637 bytes /
  SHA-256
  `9F0332653D1CA64063F48BAFAB79007C3AD702D54737551BD176FA6B8DC93CB2`.
- Bound the printed-page-45 authority surface in
  `controls/EGA1_PRINTED45_SECTION5_521_DIRECT_AUTHORITY_IMAGES.csv`, 8 rows /
  1,701 bytes / SHA-256
  `3FA07D46A97EFDEDE063129AB26D6CED9001610194B5A551801AEEA191B83133`;
  disk replay is 8/8 with errors 0.
- Rebuilt after the p.45 edit in three converged XeLaTeX passes. The controlling
  bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-45-through-521-check-r19.pdf`, 33 pages /
  250,380 bytes / SHA-256
  `81794A9091D79376B7A6ED960C93E9D48A40039C5BDB4F570A85BDAD8F1A4846`.
  Pass 2 and pass 3 consoles are byte-identical at SHA-256
  `E781C6726736028A8EBEA5C279F3A50A33B992EA89878A0905453A21514A6A44`;
  errors, undefined references, overfull boxes, underfull boxes, missing glyphs,
  and rerun requests are zero. Output pages 31–33 were rendered at 1200 dpi
  and personally inspected. The section transition, p.44/p.45 seam, formulas,
  long Hom lines, diplomatic U/V typo, paragraph flow, and page envelopes pass.
- The admitted EGA I source through 5.2.1 is 144,007 bytes, SHA-256
  `0133B833887BDF1B20C791057C4C0F99C9B58063DEE03B239BD0F8D83383FC8E`.
- Advanced the exact French cursor to printed page 45 / physical PDF page 44,
  immediately after complete 5.2.1 and before 5.2.2 later on the same page.
- A first page-selector invocation produced printed page 47 under provisional
  p.46 filenames. The mismatch was caught visually before transcription; all
  seven files were moved without overwrite to accurate p.47 filenames. The
  actual printed page 46 was then rendered from PDF selector 45. No p.47 text
  was admitted as p.46.
- Generated and personally inspected actual printed page 46 as one 1400-dpi
  context page, one direct MuPDF 5000-dpi full page, five overlapping direct
  Poppler 5000-dpi bands, and one targeted 5000-dpi crop. Completed 5.2.2
  across the p.45/p.46 seam and transcribed complete 5.2.3–5.2.6. Section
  5.2.7 begins at the foot of p.46 and crosses to p.47, so it is the next
  bounded unit.
- Direct comparison found three inherited English mathematical defects:
  $y\in Y$ for source $y\in V$ in 5.2.2, $V(s)$ for $V(x)$ in 5.2.3, and a
  `maximal index` where the directed system supplies only an index above the
  finitely many $\lambda(x_k)$. It also confirmed a French source typo in
  5.2.4: NUMDAM omits the star from $f_U^*$ in the right-exactness clause.
  Canonical French preserves the missing star; the explicitly marked English
  Erratum-II restoration is justified. The four stable IDs are
  `EG-EGA-I-P45-522-Y-IN-Y-VS-V-EN-001`,
  `EG-EGA-I-P46-523-V-S-VS-V-X-EN-001`,
  `EG-EGA-I-P46-523-MAXIMAL-VS-UPPER-INDEX-EN-001`, and
  `EG-EGA-I-P46-FU-MISSING-STAR-SRC-TYPO-001`. The ledger is now 29 rows /
  22,495 bytes / SHA-256
  `A444F30926F1A879586824094EB8F8B1E2BA1E9316DE0B544353E34B171BA192`.
- Bound the p.46 authority surface in
  `controls/EGA1_PRINTED46_SECTION522_526_DIRECT_AUTHORITY_IMAGES.csv`, 8 rows /
  1,720 bytes / SHA-256
  `ADE04AE72ED6BAB56B05F7E7DBD3BD8A7874AC872A94212BB2F6822B6F568EE0`;
  disk replay is 8/8 with errors 0.
- The first R20 invocation failed before producing pages because PowerShell
  passed literal `$job` as XeLaTeX's job name. The source was not altered; the
  invocation is non-controlling. The corrected explicit job-name invocation
  completed three converged passes. The controlling reader is
  `qa/ega1_chapter0_build/ega0-pages11-46-through-526-check-r20.pdf`, 34 pages /
  255,232 bytes / SHA-256
  `E4DFD29AD799FD3B7866E54BCEFBD78C9EA67A4538EAB91F0BE8AF2DCA3F2E3A`.
  Pass 2 and pass 3 consoles are byte-identical at SHA-256
  `F7F36A8D85B1E0DE4245088149CE19BA874D245BF43E0767406AE6A5BB10A2ED`;
  all checked diagnostics are zero. Output pages 32–34 were rendered at 1200
  dpi and personally inspected; formula placement, p.45/p.46 seam, old-page
  marker, paragraph flow, and page envelopes pass.
- The admitted EGA I source through 5.2.6 is 148,221 bytes, SHA-256
  `0DA9EFE311AFB229DF3182C22D456C66859E3A2CD2205C7E4163325EBDF5E414`.
- Advanced the exact French cursor to printed page 46 / physical PDF page 45,
  immediately after complete 5.2.6 and before 5.2.7 later on the same page.
- Personally inspected the already-corrected p.47 context page, direct MuPDF
  5000-dpi full page, and all five overlapping direct 5000-dpi bands.
  Completed 5.2.7 across the p.46/p.47 seam and transcribed complete
  5.3.1–5.3.7. No raster diagrams were introduced.
- Four English dispositions were recorded: the word order `the two following`
  requires `the following two`; `inverse` must be the logical `converse` in
  5.3.2; the explicitly marked Erratum-II exact-sequence sentence in 5.3.4 is
  absent from the NUMDAM body and therefore not imported into diplomatic
  French; and the duplicate `are` in 5.3.5 must be removed. The ledger is now
  33 rows / 25,414 bytes / SHA-256
  `D865284F9B7C07B80C8644E0FACE968B02FF783036CD53D2D6DCB2C0E6DEDCE1`.
- Bound the p.47 authority surface in
  `controls/EGA1_PRINTED47_SECTION527_537_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
  1,466 bytes / SHA-256
  `6ABD7E86F2F6DA7C2A46BE8B5481274CFF00FD62D59FF2844C7D29EBDF90033E`;
  disk replay is 7/7 with errors 0.
- Rebuilt after the p.47 edit in three converged XeLaTeX passes. The controlling
  bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-47-through-537-check-r21.pdf`, 35 pages /
  260,113 bytes / SHA-256
  `4AAD617D6331BD69A3B4F73C1E81E47016953C190F7DF7F8BAFB253E8B600192`.
  Pass 2 and pass 3 consoles are byte-identical at SHA-256
  `5D9F83D8803D89E3D94E6B3F6F9C9D8EAC929D032CC26F0D3E9148566C5A603E`;
  checked diagnostics are zero. Output pages 33–35 were rendered at 1200 dpi
  and personally inspected. The p.46/p.47 seam, enumerate continuation,
  long formulas, subsection transition, paragraph flow, and page envelopes
  pass.
- The admitted EGA I source through 5.3.7 is 153,059 bytes, SHA-256
  `F0DCEA46C6D128E41DE1AD93E3376CB1658DEFC8CC7B1CA8AABB4F36FA1A8DEF`.
- Advanced the exact French cursor to printed page 47 / physical PDF page 46,
  immediately after complete 5.3.7 and before 5.3.8 on printed page 48.
- Generated and personally inspected printed page 48 as one 1400-dpi context
  page, one direct 5000-dpi full page, five overlapping 5000-dpi bands, and a
  targeted 5000-dpi crop. The initial failed targeted crops were newly
  generated scratch and were removed; the exact successful source witness is
  retained. Transcribed complete 5.3.8–5.3.12 without importing a correction
  into the French body.
- Bound the p.48 authority surface in
  `controls/EGA1_PRINTED48_SECTION538_5312_DIRECT_AUTHORITY_IMAGES.csv`, 8
  rows / 1,695 bytes / SHA-256
  `520DA1A67477B1DD2D4A210DDA22F141914081B32E2B94FC09CB2DE0F223357F`;
  disk replay is 8/8 with errors 0.
- Confirmed the inherited English grammar defect `This result ... impose`
  and the printed French source typo `un voisinage ouvert U de X` in 5.3.9,
  where the mathematical point is lowercase $x$. Diplomatic French retains
  uppercase $X$; the later English successor must use $x$ with a visible
  note. Stable IDs are `EG-EGA-I-P48-538-IMPOSE-VS-IMPOSES-EN-001` and
  `EG-EGA-I-P48-539-NEIGHBOURHOOD-OF-X-VS-XPOINT-SRC-TYPO-001`. The ledger is
  now 35 rows / 27,214 bytes / SHA-256
  `64B77FD1BE05F01601C594D41678800A39CC82DEE9672C3EBFB37A951567FD26`.
- Rebuilt after the p.48 edit in three converged XeLaTeX passes. The
  controlling bounded reader is
  `qa/ega1_chapter0_build/ega0-pages11-48-through-5312-check-r22.pdf`, 36 A4
  pages / 263,182 bytes / SHA-256
  `50C3C0FD0308BB6A53F46FAA2167ADC055E633798F7F11D37BB250728AAEC618`.
  Passes 2 and 3 have identical console SHA-256
  `4FB0EBE20EAA6E7FDA4F63835C47D6A8FC53D2B2650BD93EA837CA498FBBFA88`;
  checked diagnostics are zero. Output pages 34–36 were rendered at 1200 dpi
  and personally inspected; the seam, formulas, paragraph flow, clipping,
  and page envelopes pass.
- The admitted EGA I source through 5.3.12 is 155,985 bytes, SHA-256
  `062A2C2E54DD0741953584E8444812FDE32CF41294947CC47D160830BCB3C988`.
- Advanced the exact French cursor to printed page 48 / physical PDF page 47,
  after complete 5.3.12 and before the section 5.4 heading / 5.4.1 crossing
  the printed-page-48/49 seam.
- Generated and personally inspected printed page 49 as one 1400-dpi context
  page, one direct 5000-dpi full page, five overlapping 5000-dpi bands, and a
  targeted 5000-dpi arrow crop. Transcribed the section 5.4 heading, complete
  5.4.1 across the p.48/p.49 seam, and complete 5.4.2–5.4.3. Section 5.4.4
  crosses to p.50 and remains the next bounded unit.
- Bound the p.49 authority surface in
  `controls/EGA1_PRINTED49_SECTION541_543_DIRECT_AUTHORITY_IMAGES.csv`, 8
  rows / 1,735 bytes / SHA-256
  `A4B1602FED878CD1118C5D88F7E92BFC4C3D9CC72F89EA1EBA31ED1221FF1F57`;
  disk replay is 8/8 with errors 0.
- Recorded five stable dispositions: a spurious English comma in 5.4.1; an
  Erratum-II sentence absent from the bounded body; the English 5.3.2/5.4.2
  xref error; the omitted conditional `if`; and the printed 5.4.3
  isomorphism arrow on the general endomorphism map, which the following
  sentence itself proves to be a source typo. Diplomatic French retains that
  arrow; English must use an ordinary arrow with a visible note. The ledger
  is now 40 unique rows / 31,582 bytes / SHA-256
  `7B7CAD6B168DCC6F6A31EA90BEC43F0A7EF0FB26C89E4E46498E0B9D1DD14D2A`.
- The preliminary R23 render exposed wrong output glyphs for literal Unicode
  guillemets. Re-encoded the same printed quotation using the established
  `\og ... \fg{}` form and rebuilt without overwriting R23. The controlling
  reader is
  `qa/ega1_chapter0_build/ega0-pages11-49-through-543-check-r24.pdf`, 37 A4
  pages / 269,084 bytes / SHA-256
  `DE653E85A7F3A4C6EAA7A2015AA5201D00EC3C9B2640D62991173CEEB03A6790`.
  Passes 2 and 3 have identical console SHA-256
  `D9A0FF5973C1AA8BBFD6DC9D3EFBA6DEEFC61A7A9DB5A9934C8C9C9D5C8E3025`;
  checked diagnostics are zero. Output pages 36–37 were rendered at 1200 dpi
  and personally inspected; source seam, formulas/arrows, corrected
  guillemets, paragraph flow, clipping, and page envelopes pass.
- The admitted EGA I source through 5.4.3 is 161,804 bytes, SHA-256
  `A6F08C833F94C736E4F0C266C99EDADA972422CB5DFA2A71FE621BE7E8F1996B`.
- Advanced the exact French cursor to printed page 49 / physical PDF page 48,
  after complete 5.4.3 and before 5.4.4 crossing the printed-page-49/50 seam.
- Generated and personally inspected printed page 50 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping 5000-dpi bands.
  Transcribed complete 5.4.4 across the p.49/p.50 seam and complete 5.4.5.
  Section 5.4.6 crosses to p.51 and remains the next bounded unit.
- Bound the p.50 authority surface in
  `controls/EGA1_PRINTED50_SECTION544_545_DIRECT_AUTHORITY_IMAGES.csv`, 7
  rows / 1,446 bytes / SHA-256
  `3CD12BCAE16C58351D220A8D2E6308FE050DDF15FE5203342DEC49BA9EBCEF79`;
  disk replay is 7/7 with errors 0.
- Recorded three stable dispositions: English `With these notation` requires
  plural `notations`; English `follows immediately from that` requires `from
  the fact that`; and NUMDAM's isolated plain italic $L$ in 5.4.5 is a
  source-notation inconsistency with surrounding script $\mathcal L$.
  Diplomatic French retains plain $L$ while the English normalization is
  justified. The ledger is now 43 unique rows / 34,111 bytes / SHA-256
  `6ECC9DB41A80F464648EE560FB32514C684E6C1A9C7B49CC7C88B82619DE546C`.
- Rebuilt in three converged XeLaTeX passes as
  `qa/ega1_chapter0_build/ega0-pages11-50-through-545-check-r25.pdf`, 37 A4
  pages / 271,048 bytes / SHA-256
  `3CBD0696455326294FE4075CB8871891E5B5D7929497166F5C8F44244534D4AD`.
  Passes 2 and 3 have identical console SHA-256
  `C829F63C39A00B58126D033A02D1CA91991C45F5F226BFAE6A412E2F8050D56E`;
  checked diagnostics are zero. Output page 36 is byte-identical to its
  already-inspected R24 render; output page 37 was rendered at 1200 dpi and
  personally inspected. The seam, tensor-power formula, dual map, notation,
  paragraph flow, clipping, and page envelope pass.
- The admitted EGA I source through 5.4.5 is 163,898 bytes, SHA-256
  `7654EF35DB83CA45584C2747F4FC71DAD809D8E1EDB9974092312995460BE17D`.
- Advanced the exact French cursor to printed page 50 / physical PDF page 49,
  after complete 5.4.5 and before 5.4.6 crossing the printed-page-50/51 seam.
- Generated and personally inspected printed page 51 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping 5000-dpi bands.
  Transcribed complete 5.4.6 across the p.50/p.51 seam and stopped before
  5.4.7, which crosses to p.52.
- Bound the p.51 authority surface in
  `controls/EGA1_PRINTED51_SECTION546_DIRECT_AUTHORITY_IMAGES.csv`, 7 rows /
  1,446 bytes / SHA-256
  `651B83BD450FE474F23B34AE77DA817A033FA3C6CA8C0BF4CAAA96E75A0B587B`;
  disk replay is 7/7 with errors 0.
- Recorded four exact English defects in 5.4.6: `by corresponding to a pair`,
  singular-subject `are immediate`, one unmatched closing parenthesis in the
  pullback identity, and singular `these homomorphism`. Rejected the proposed
  $m/n$ candidate because the current English already has the correct
  $s_m\in\Gamma(X,\mathcal L^{\otimes m})$. The ledger is now 47 unique rows /
  36,998 bytes / SHA-256
  `0F33C1828BD84F71BC0EA7CA52D4384D6DB7B727C7A5C402454F0CEF4F7CEC49`.
- Rebuilt in three converged XeLaTeX passes as
  `qa/ega1_chapter0_build/ega0-pages11-51-through-546-check-r26.pdf`, 38 A4
  pages / 274,341 bytes / SHA-256
  `501A3CB4BD16B9525686FFDCB7AAD52B94EB4EEE6FCDB2FF593386F3EB5D821D`.
  Passes 2 and 3 have identical console SHA-256
  `B23964557AB54464617BCC91EB3EF639280141B44CA762A21D763FB288F02381`;
  checked diagnostics are zero. Output pages 37–38 were rendered at 1200 dpi
  and personally inspected; their SHA-256 identities are
  `C04FF07E9266E76BB10337D626FBD9333023751F3E8E66CC8AEB6BDDCB21EFED`
  and `677016CD39C249C3E41FF12405DAF8E3D948464E4643184A16E4A8824A8AD7A4`.
- The admitted EGA I source through 5.4.6 is 167,228 bytes, SHA-256
  `05648F5BFFBE435DEAAF138F301EA58F7E4674E29C1DA3517317856967F39653`.
- Advanced the exact French cursor to printed page 51 / physical PDF page 50,
  after complete 5.4.6 and before 5.4.7 crossing the printed-page-51/52 seam.
- Generated and personally inspected printed page 52 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping 5000-dpi bands.
  A targeted crop from the already-bound p.51 5000-dpi source resolved an
  ambiguous coefficient: NUMDAM visibly prints $H^1(\mathfrak U,\mathcal
  O_X)$ without the mathematically required star.
- Transcribed complete 5.4.7 across the p.51/p.52 seam and complete
  5.4.8–5.4.9. An initial generic environment anchor placed the new block at
  the first environment boundary; before any build, the exact unchanged block
  was mechanically relocated to the true end-of-5.4.6 cursor and its unique
  labels/order were replayed.
- Bound the p.52 authority surface in
  `controls/EGA1_PRINTED52_SECTION547_549_DIRECT_AUTHORITY_IMAGES.csv`, 8 rows /
  1,689 bytes / SHA-256
  `3E21A336A425ED1C39670F1800201CD6B6F8E6F0B967077C3A919C4113DD73D2`;
  disk replay is 8/8 with errors 0.
- Recorded seven source-backed dispositions. French source defects retained
  diplomatically are $x\in X$ where the stalk formula is only defined for
  $x\in U$, the omitted star in $H^1(\mathfrak U,\mathcal O_X)$, and the
  malformed inverse-image-functor sentence in 5.4.8. English-only defects are
  `and say ... meaning`, `coycles`, the comma-separated pair substituted for
  the product transition cocycle, and `automorphisms corresponds`. The ledger
  is now 54 unique rows / 42,917 bytes / SHA-256
  `F7B79B66644531A84E8D60FD2024400A4208FD2902D5DDEF39504A95F3DC9E9A`.
- R27 was preserved as non-controlling after it exposed a missing glyph for
  literal Unicode `Č`. Encoded the same printed word as `\v{C}ech` and rebuilt
  in three converged passes as
  `qa/ega1_chapter0_build/ega0-pages11-52-through-549-check-r28.pdf`, 39 A4
  pages / 285,696 bytes / SHA-256
  `25ED34E2ADA1014A20C2170BC800B28F8D5D05AF72A51EDE05DA8E889FB9B872`.
  Passes 2 and 3 have identical console SHA-256
  `E4F21AF445B532C71DBA9E5DD9D1381C4DDD68DFC0E9C8B552627435F4AA40D0`;
  checked diagnostics are zero. Output pages 38–39 were rendered at 1200 dpi
  and personally inspected; diagram, formulas, footnotes, seam, clipping, and
  page envelopes pass.
- The admitted EGA I source through 5.4.9 is 175,807 bytes, SHA-256
  `54E686F5ED3FC619A1CE60EF8F61222E4C448C630646DC3FB54E6F5C98FBCADB`.
- Advanced the exact French cursor to printed page 52 / physical PDF page 51,
  after complete 5.4.9 and before 5.4.10 crossing the printed-page-52/53 seam.
- Generated and personally inspected printed page 53 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping 5000-dpi bands.
  Transcribed complete 5.4.10 across the p.52/p.53 seam and complete
  5.5.1--5.5.3.
- Bound the p.53 authority surface in
  `controls/EGA1_PRINTED53_SECTION5410_553_DIRECT_AUTHORITY_IMAGES.csv`, seven
  rows / 1,447 bytes / SHA-256
  `D80E416FE9A1CD9B92ED629735D7DC929D043B61BB4EBFF7BDA9D7FC047B5087`;
  disk replay is 7/7 with errors 0.
- Recorded five exact English-only defects: `$\mathcal L=\mathcal O_X^n$`
  instead of the source- and type-correct `$\mathcal O_Y^n$`, three singular
  `question` constructions mistranslated with plural `questions`, and
  singular-subject `equivalence ... are`. The ledger is now 59 unique rows /
  46,176 bytes / SHA-256
  `EC6373F1966E1CD4F25E42B9A65DAC07A5C177E31EE9BA8D687B3A0F6AFD5415`.
- R29 compiled without TeX diagnostics but was preserved as non-controlling
  because the artificial book wrapper displayed subsection `0.5.5`. The
  source was untouched; the wrapper alone was corrected to the canonical EGA
  0 display scheme (`1`, `1.0`, ..., `5.5`) and is 833 bytes / SHA-256
  `5631F8ACC3089B0C3FFF3C33602C930A874225FE6E67AB0DCFE2881660B9D4AE`.
- Rebuilt in three converged passes as
  `qa/ega1_chapter0_build/ega0-pages11-53-through-553-check-r30.pdf`, 40 A4
  pages / 291,332 bytes / SHA-256
  `E4A85294D94BAA64062247A0528C0AB885ACB214F739BC7D784A3AF777FC16E5`.
  Passes 2 and 3 have identical console SHA-256
  `B7942978F819DDBBF4559DD9B6B2374130DD015588D9DAB382809A3C2543D4D1`;
  checked diagnostics are zero. Output pages 1, 36--37, and 39--40 were
  rendered at 1200 dpi and personally inspected; the canonical heading
  numbers, seam, formulas, lists, clipping, and page envelopes pass.
- The admitted EGA I source through 5.5.3 is 180,145 bytes, SHA-256
  `5338C7BFD794F17665FE476E453E3AB7EC3448FB9F8789766FEF263DB69D24B6`.
- Advanced the exact French cursor to printed page 53 / physical PDF page 52,
  after complete 5.5.3 and before 5.5.4 on printed page 54.
- Generated and personally inspected printed page 54 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping 5000-dpi bands.
  Transcribed complete 5.5.4--5.5.5 and stopped before the section-6 heading
  and 6.0 paragraph crossing to p.55.
- Bound the p.54 authority surface in
  `controls/EGA1_PRINTED54_SECTION554_555_DIRECT_AUTHORITY_IMAGES.csv`, seven
  rows / 1,447 bytes / SHA-256
  `CF1F04FDAFF0AC28DFF4FE0926E541AE53143BE3ED105272838797EB35607305`;
  disk replay is 7/7 with errors 0.
- Recorded six exact dispositions: printed plain $F$ amid calligraphic
  $\mathcal F$, lowercase neighbourhood $u$ versus $U$, and $y\in V$ versus
  the mathematically required $y\in U$ are retained French source defects;
  English independently omits `module`, breaks `saying ... means`, and
  changes the source's $y\in X$ to nonexistent $y\in Y$. The ledger is now
  65 unique rows / 51,003 bytes / SHA-256
  `AECC7EA7C57868B78CCD088EF45C103405459FE79A82B2705923A49129FF30EE`.
- Preserved R31 as non-controlling after its layout replay exposed one
  11.02023-pt overfull exterior-power line. Moved the unchanged expression to
  display math and rebuilt in three converged passes as
  `qa/ega1_chapter0_build/ega0-pages11-54-through-555-check-r32.pdf`, 41 A4
  pages / 296,746 bytes / SHA-256
  `19AC8BDE910E284B4FF6061342AFBB1A33CDD6865BB3C5F91CB9A168E2EC28FE`.
  Passes 2 and 3 have identical console SHA-256
  `0BA30D989A6FD0F6280DD3175C02DA2EE0F82DCB04205B7098CDD8B86962CA92`;
  checked diagnostics are zero. Output pages 40--41 were rendered at 1200
  dpi and personally inspected; seam, formulas, source-defect forms,
  clipping, and page envelopes pass.
- The admitted EGA I source through 5.5.5 is 184,246 bytes, SHA-256
  `775C63BB9CECD6ACA331C1FFF5DFCCF862E223A5CF42A2936E3FAD47F7C017B3`.
- Advanced the exact French cursor to the section-6 heading and opening 6.0
  text on printed page 54; 6.0 crosses to printed page 55 and remains wholly
  unadmitted.
- Generated and personally inspected printed page 55 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping 5000-dpi bands.
  Transcribed the section-6 heading, complete 6.0 across the p.54/p.55 seam,
  complete 6.1.1--6.1.4, and the 6.2 introductory paragraph; stopped before
  6.2.1 crossing to p.56.
- Bound the p.55 authority surface in
  `controls/EGA1_PRINTED55_SECTION60_614_62INTRO_DIRECT_AUTHORITY_IMAGES.csv`,
  seven rows / 1,447 bytes / SHA-256
  `1965466651C6FBF81973A4DB75309F50E6A7FE5DC1663337208E1A6A2718152D`;
  disk replay is 7/7 with errors 0.
- Recorded one retained French grammar typo (`Soient M un ...`) and six
  English defects: a mangled source footnote, `a flat A-modules`, declarative
  `is it necessary`, omitted separator between $N'$ and $N''$, missing
  $\operatorname{Im}$ in the 6.1.4 identity, and `multiple modules
  structures`. The ledger is now 72 unique rows / 56,274 bytes / SHA-256
  `9C7DE2AE913B4FDF4621D81561A8F7749414F27D1C2FA1B9996A279040F284F8`.
- Rebuilt in three converged passes as
  `qa/ega1_chapter0_build/ega0-pages11-55-through-614-62intro-check-r33.pdf`,
  42 A4 pages / 301,875 bytes / SHA-256
  `9102756F4A26615E6FAEC3AB3F07BF78D16364FDF0858AB0439EDEA77CC3B71C`.
  Passes 2 and 3 have identical console SHA-256
  `C1A61AAA9AE4E9423CC762361EA47DB3F6D418512D4EBF66AE715004371148F3`;
  checked diagnostics are zero. Output pages 40--42 were rendered at 1200
  dpi and personally inspected; seam, heading numbers, footnote, sequences,
  tensor/image formulas, clipping, and page envelopes pass.
- The admitted EGA I source through the 6.2 introductory paragraph is
  187,861 bytes, SHA-256
  `98C2C9B574C7BD688E16CDA31702A29C2A367B7400FE55B290E5B131587BD123`.
- Advanced the exact French cursor to 6.2.1 on printed page 55; it crosses to
  printed page 56 and remains wholly unadmitted.
- Recorded the SGA7 coordination boundary: this task has no SGA7 French
  correction-layer ownership and is not mutating SGA7. Its active scope
  remains canonical diplomatic French EGA 0--IV, followed by the disjoint
  Deligne D046--D090 and L007--L011/L013 lane.
- Generated and personally inspected printed page 56 as one 1400-dpi
  context page, one direct 5000-dpi full page, and five overlapping direct
  5000-dpi bands. Transcribed complete 6.2.1--6.2.3 and 6.3.1--6.3.2,
  retaining the printed-page break inside 6.2.1; stopped before 6.3.3,
  which crosses to p.57.
- Bound the p.56 authority surface in
  `controls/EGA1_PRINTED56_SECTION621_623_631_632_DIRECT_AUTHORITY_IMAGES.csv`,
  seven rows / 1,447 bytes / SHA-256
  `728AF04240DE5039760D40E4ADDC3A2D2F3017BFD0DE958795010745F2DB0C8C`;
  disk replay is 7/7 with errors 0.
- Rechecked the corresponding English through 6.3.2 and found no new
  substantive source-correction conflict or mathematical translation
  defect. The ledger remains 72 unique rows / 56,274 bytes / SHA-256
  `9C7DE2AE913B4FDF4621D81561A8F7749414F27D1C2FA1B9996A279040F284F8`.
- Rebuilt in three converged passes as
  `qa/ega1_chapter0_build/ega0-pages11-56-through-632-check-r34.pdf`, 43 A4
  pages / 306,535 bytes / SHA-256
  `66BDF8635CFD51F1193FF4079D527B116BDDDE5CB89246B9B5097664378AE802`.
  Passes 2 and 3 have identical console SHA-256
  `7058A2C73E485145F307BA3DEFE6D233AA1E27F0219157EA2C2B4B562A342A55`;
  checked diagnostics are zero. Output pages 41--43 were rendered at 1200
  dpi and personally inspected; seam, formulas, headings, clipping, and page
  envelopes pass.
- The admitted EGA I source through complete 6.3.2 is 191,592 bytes,
  SHA-256
  `746A77E2CA711DF2084051EBB08C7583C4F656A3ABC672750A131C2016C53A61`.
- Advanced the exact French cursor to 6.3.3 on printed page 56; it crosses to
  printed page 57 and remains wholly unadmitted.
- Generated and personally inspected printed page 57 as one 1400-dpi
  context page, one direct 5000-dpi full page, and five overlapping direct
  5000-dpi bands. Transcribed complete 6.3.3 across the p.56/p.57 seam,
  complete 6.3.4, and complete 6.4.1; stopped before 6.4.2 on p.58.
- Bound the p.57 authority surface in
  `controls/EGA1_PRINTED57_SECTION633_634_641_DIRECT_AUTHORITY_IMAGES.csv`,
  seven rows / 1,447 bytes / SHA-256
  `225AAD25B7CD588994C8246F6590A04F3FADD61B52E8194F686BFFF034C15E87`;
  disk replay is 7/7 with errors 0.
- Recorded one retained French source omission (`et != {0}` lacks subject
  $B$) and seven independent English defects: misspelled `homomorphism`,
  `none other that`, wrong zero-divisor terminology, `from that`, two
  missing logical conjunctions, and the omitted $v=0$ conclusion in 6.4.1
  item $c)$. The ledger is now 80 unique rows / 61,977 bytes / SHA-256
  `67A07EFE5792C6CC69A11312DC724285FE32E2EE4D97000FFC8DF4EE846673B1`.
- Rebuilt in three converged passes as
  `qa/ega1_chapter0_build/ega0-pages11-57-through-641-check-r35.pdf`, 44 A4
  pages / 311,283 bytes / SHA-256
  `F554E94F990D817146A58077545C2746F7F761041B65B0352D3082BED2DE753D`.
  Passes 2 and 3 have identical console SHA-256
  `48023EF3871B8605CB7CA0EFF29B209032CABCD67713F7416B57FF5666D8714C`;
  checked diagnostics are zero. Output pages 42--44 were rendered at 1200
  dpi and personally inspected; seams, displays, source omission, list,
  clipping, and page envelopes pass.
- The admitted EGA I source through complete 6.4.1 is 195,972 bytes,
  SHA-256
  `DFDA4F3C4A60EC3E4613EDE672E133C7F5E5DE51E05445D4A8857CEDD0E9FD90`.
- Advanced the exact French cursor to 6.4.2 on printed page 58; no 6.4.2 text
  has been admitted.
- Generated and personally inspected printed page 58 as one 1400-dpi
  context page, one direct 5000-dpi full page, and five overlapping direct
  5000-dpi bands. Transcribed complete 6.4.2--6.4.5 and 6.5.1--6.5.2;
  stopped before the 6.6 heading and 6.6.1 crossing to p.59.
- Bound the p.58 authority surface in
  `controls/EGA1_PRINTED58_SECTION642_645_651_652_DIRECT_AUTHORITY_IMAGES.csv`,
  seven rows / 1,447 bytes / SHA-256
  `78BC0A6854B3B1705A9C72240EB75AFB2E4F01CA169A1B342BF8FEBE4ADE1A1D`;
  disk replay is 7/7 with errors 0.
- Recorded two English defects: 6.4.2 reverses `only if` to `if`, and 6.4.5
  writes plural `a faithfully flat A-modules`. The ledger is now 82 unique
  rows / 63,427 bytes / SHA-256
  `B0ED90E7BE413555FA0FF3B30E30A823F0B2869854AA1254F6FFC862921F7BD5`.
- Rebuilt in three converged passes as
  `qa/ega1_chapter0_build/ega0-pages11-58-through-652-check-r36.pdf`, 45 A4
  pages / 315,041 bytes / SHA-256
  `95917CC03E3FABCBF3669BE4DC035D5F49BE5ACDA96FDB8FAC950B8664A47958`.
  Passes 2 and 3 have identical console SHA-256
  `E9C79F315FD9F4ED909AF28BEB9060B2B75442A5845E7CE3004BCB27D321E70E`;
  checked diagnostics are zero. Output pages 43--45 were rendered at 1200
  dpi and personally inspected; seam, formulas, headings, clipping, and page
  envelopes pass.
- The admitted EGA I source through complete 6.5.2 is 199,269 bytes,
  SHA-256
  `006DFC0A52E7EB879648591B4FC87670B105A88786E091A03C46F5B4D558F00E`.
- Advanced the exact French cursor to the 6.6 heading and 6.6.1 on printed
  page 58; the numbered unit crosses to p.59 and remains wholly unadmitted.
- Generated and personally inspected printed p.59 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping direct 5000-dpi
  bands. Transcribed the complete 6.6 heading, complete 6.6.1 across the
  p.58/p.59 seam, 6.6.2--6.6.4, the 6.7 heading, and 6.7.1--6.7.2; stopped
  before the p.59/p.60 6.7.3 unit.
- Bound the p.59 authority surface in
  `controls/EGA1_PRINTED59_SECTION661_664_671_672_DIRECT_AUTHORITY_IMAGES.csv`,
  seven rows / 1,447 bytes / SHA-256
  `46682F34F101948F853CC8BACA93EA5E3160DF016784E015D17ECB5FD50309AA`;
  replay is 7/7 with errors 0.
- Rechecked the inherited English 6.6.2 replacement and 6.7.1 insertion
  against the direct EGA II official errata/addenda image at physical p.214 /
  printed p.217. The 5000-dpi witness is 5,918,370 bytes / SHA-256
  `33244FCCC124FDCE60F914E761D0200ADBCF5B93C949DA4585F802ECD62FD61A`;
  its one-row manifest SHA-256 is
  `2480045D4ABDFB477D44EFF5116B84DDD6ED2FA2A4BB20CE913C2AB67EF5F6EE`.
  Both changes are official and exact, not hallucinated corrections. The
  diplomatic French body retains the original EGA I printing.
- Recorded one new independent English punctuation error in 6.6.1 and two
  explicit official-correction confirmations. The ledger is now 85 unique
  rows / 65,928 bytes / SHA-256
  `EE1E740681900BDF79B611E79D86BB129AD526177E1A18476248D98D44DA9641`.
- Rebuilt in three converged passes as
  `qa/ega1_chapter0_build/ega0-pages11-59-through-672-check-r37.pdf`, 46 A4
  pages / 319,537 bytes / SHA-256
  `AE962AB263ACD96D95177F4AD9890ADD8B8EFAF289C40226F540F381D0012B32`.
  Passes 2 and 3 have identical console SHA-256
  `6718B4DA395258F085E9406504E1A5B3FED3DC40AF8E9FCA6681089616128D3E`;
  checked diagnostics are zero. Output pages 44--46 were rendered at 1200
  dpi and personally inspected; seam, list, original proof, stalk formulas,
  headings, clipping, and page envelopes pass.
- The admitted EGA I source through complete 6.7.2 is 203,404 bytes,
  SHA-256
  `E7B1880BCA2ECCDF5C59B998C53254221F21EA15C08D7CDC744BC6472C5CA3FF`.
- Advanced the exact French cursor to 6.7.3 on printed p.59; it crosses to
  printed p.60 and remains wholly unadmitted.
- Generated and personally inspected printed p.60 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping direct 5000-dpi
  bands. Transcribed complete 6.7.3 across the seam, 6.7.4--6.7.6, 6.7.8,
  the section-7/7.1 headings, and complete 7.1.1; stopped before Definition
  7.1.2 crossing to p.61. The printed 6.7.6-to-6.7.8 jump is retained.
- Bound the p.60 authority surface in
  `controls/EGA1_PRINTED60_SECTION673_678_711_DIRECT_AUTHORITY_IMAGES.csv`,
  seven rows / 1,447 bytes / SHA-256
  `634F47AD20AA8FF26EF1872D7286D868A389408C33DA08B1E9B40C44C6108221`;
  replay is 7/7 with errors 0.
- Recorded six English defects, including the mathematical reversal from
  French `left exact` to English `right exact` in 6.7.6 and the missing
  $Y$-flat predicate in 6.7.8. The ledger is now 91 unique rows / 70,001
  bytes / SHA-256
  `C90F445519FB3A88797D521797663A4B1A899A0068897A1C3C9934DEC9D5BBFA`.
- Rebuilt in three converged passes as
  `qa/ega1_chapter0_build/ega0-pages11-60-through-711-check-r38.pdf`, 47 A4
  pages / 323,586 bytes / SHA-256
  `35DADAF587129C410F1DF581449B0DD213027F25334C338828A1D672D3280DDB`.
  Passes 2 and 3 have identical console SHA-256
  `A00E0BC7BBCD49B7734B78A52E725693E5E52C36BBC28BC05EF30BB38B5FF714`;
  checked diagnostics are zero. Output pages 45--47 were rendered at 1200
  dpi and personally inspected; seam, exact sequence, Hom display, retained
  numbering, section transition, clipping, and page envelopes pass.
- The admitted EGA I source through complete 7.1.1 is 207,550 bytes,
  SHA-256
  `56983D016FAE9271CF8C306C7D3F60F7F89D0AFB641F4E2CBCB7D187ABAC8DD2`.
- Advanced the exact French cursor to Definition 7.1.2 on printed p.60; it
  crosses to printed p.61 and remains wholly unadmitted.
- Generated and personally inspected printed p.61 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping direct 5000-dpi
  bands. Transcribed Definition 7.1.2 across the p.60/p.61 seam, Lemma 7.1.3,
  Proposition 7.1.4, and Corollaries 7.1.5--7.1.6; stopped before 7.1.7 on
  p.62.
- Bound the p.61 authority surface in
  `controls/EGA1_PRINTED61_SECTION712_716_DIRECT_AUTHORITY_IMAGES.csv`, seven
  rows / 1,447 bytes / SHA-256
  `03F54754548026D57E6445BEEBFC8ACE730F96BE00D4CC7C996848DC12ECC3C3`;
  replay is 7/7 with errors 0.
- Recorded five source-backed English grammar defects in 7.1.2, 7.1.4, and
  7.1.6. The ledger is now 96 unique rows / 73,652 bytes / SHA-256
  `807B29B2E2E309A05A36851B0BD568DBFC86729A881C771D2848A0066A678ABE`.
- Rebuilt in three converged passes as
  `qa/ega1_chapter0_build/ega0-pages11-61-through-716-check-r39.pdf`, 48 A4
  pages / 329,654 bytes / SHA-256
  `88278F266E4FD5A3D217C4D5A287CD512859657AA0E641193F32BB0DC04236B1`.
  Passes 2 and 3 have identical console SHA-256
  `16BF8B4B7F5F494D63864578C081A4959FBF3C35BA1F4845F590DB16B5A67F76`;
  checked diagnostics are zero. Output pages 46--48 were rendered at 1200
  dpi and personally inspected; theorem typography, seam, formulas, lists,
  clipping, and page envelopes pass.
- Confirmed to the disjoint FAC/GAGA task that this task has no FAC or GAGA
  source, translation, or reference mutation; that task may proceed without
  overlapping this task's EGA/Deligne scopes.
- The admitted EGA I source through complete 7.1.6 is 211,874 bytes,
  SHA-256
  `69222FB71F35905E5EC4744AC2DBCE06ADE2C3BABFF5BDF477D93E67446EB910`.
- Advanced the exact French cursor to Corollary 7.1.7 on printed p.62; it
  remains wholly unadmitted.
- Generated and personally inspected printed p.62 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping direct 5000-dpi
  bands. The first band-crop invocation lost the original image from the
  active stack after its initial crop; its unused `r1` band outputs are
  excluded. Regenerated `r2` bands all derive from the exact full-page image.
- Transcribed Corollaries 7.1.7--7.1.8, Definition 7.1.9 and its notation
  paragraph, Proposition 7.1.10, Corollaries 7.1.11--7.1.14, their proof,
  and the 7.2 heading; stopped before the p.62/p.63 unit 7.2.1.
- Bound the accepted p.62 surface in
  `controls/EGA1_PRINTED62_SECTION717_7114_72INTRO_DIRECT_AUTHORITY_IMAGES.csv`,
  seven rows / 1,447 bytes / SHA-256
  `877A516F22E787D3CEC096C92E482DE4F5910F2E3162B6B93EC90791F59D34B2`;
  replay is 7/7 with errors 0.
- Recorded the missing surjectivity predicate in English 7.1.14 and the
  duplicated 7.1.10 reference in its proof. The ledger is now 98 unique rows
  / 75,120 bytes / SHA-256
  `8831FBB0D1B556DC9CC8F1DF9C8D64F6E3ED343C4E2808943AEF30640B5AFB2B`.
- Rebuilt in three converged passes as
  `qa/ega1_chapter0_build/ega0-pages11-62-through-72intro-check-r40.pdf`, 48
  A4 pages / 334,188 bytes / SHA-256
  `92CF6A6C128A0849F6EAA1EB661D761F6E6663C49903E4335327BDE2BD3B026E`.
  Passes 2 and 3 have identical console SHA-256
  `BF7A7EEACE5965C15044CB4063B45CD833DCC4947FD2CC4B833A0636BB5455AD`;
  checked diagnostics are zero. Output pages 47--48 were rendered at 1200
  dpi and personally inspected; statement/proof layout, formulas, citations,
  transition, clipping, and page envelopes pass.
- The admitted EGA I source through complete 7.1 and the 7.2 heading is
  215,508 bytes, SHA-256
  `52CFC6A0EF8956A0E65B3D8E3A692AA64BA6E329624BF5BE0EDC14D1119CEB33`.
- Advanced the exact French cursor to 7.2.1 on printed p.62; it crosses to
  printed p.63 and remains wholly unadmitted.
- Generated and personally inspected printed p.63 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping direct 5000-dpi
  bands. Transcribed complete 7.2.1 across the p.62/p.63 seam, Lemma 7.2.2,
  7.2.3, and Proposition 7.2.4 with their proofs; stopped before Corollary
  7.2.5 crossing to p.64.
- Bound the p.63 authority surface in
  `controls/EGA1_PRINTED63_SECTION721_724_DIRECT_AUTHORITY_IMAGES.csv`, seven
  rows / 1,447 bytes / SHA-256
  `8CA2E17263D239A2B5133947B1FAB092AE3A08A737D1A2C035F8A8CF8A9CBDD4`;
  replay is 7/7 with errors 0.
- Recorded six English defects, including `compact` for source `complete` in
  7.2.1 and the union-for-intersection reversal in 7.2.3. The ledger is now
  104 unique rows / 79,486 bytes / SHA-256
  `7A53979127C12062692F55E601AF68F6C66D958EE51C0E344AA84A72A244C26B`.
- Rebuilt in three converged passes as
  `qa/ega1_chapter0_build/ega0-pages11-63-through-724-check-r41.pdf`, 49 A4
  pages / 338,837 bytes / SHA-256
  `EFF056875D4C4258897846C8D759B3B11025BF5E708A0EE502B2DD94D88871C9`.
  Passes 2 and 3 have identical console SHA-256
  `A26572AD94E35C68C000437BF963784AAC00E80B6597C20501691DE4B8FA957C`;
  checked diagnostics are zero. Output pages 48--49 were rendered at 1200
  dpi and personally inspected; inverse-limit notation, seam, maps,
  typography, clipping, and page envelopes pass.
- The admitted EGA I source through complete 7.2.4 is 219,631 bytes,
  SHA-256
  `B4E394E896495784839CFD45036349C06FA1E28E92C3E0D93FC18AD652B40E1C`.
- Advanced the exact French cursor to Corollary 7.2.5 on printed p.63; it
  crosses to printed p.64 and remains wholly unadmitted.
- Generated and personally inspected printed p.64 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping direct 5000-dpi
  bands. Transcribed Corollary 7.2.5 across the p.63/p.64 seam and complete
  Corollary 7.2.6 with its proof; stopped before Proposition 7.2.7, which
  crosses from p.64 to p.65.
- Bound the p.64 authority surface in
  `controls/EGA1_PRINTED64_SECTION725_726_DIRECT_AUTHORITY_IMAGES.csv`, seven
  rows / 1,447 bytes / SHA-256
  `F5F0A65DA113928401C5969130E93709F70694799AB8BCCDA5755D43A9B0F3E4`;
  replay is 7/7 with errors 0.
- Recorded four source-backed English defects in 7.2.5--7.2.6: one spelling
  error, one duplicated symbol, one omitted Noetherian predicate, and one
  article error. The ledger is now 108 unique rows / 82,187 bytes / SHA-256
  `4811A80272E7B6B2B6BD02FF9C336F22A68D175E32BB4549BA6B58CCB5903598`.
- Rebuilt in three converged passes as
  `qa/ega1_chapter0_build/ega0-pages11-64-through-726-check-r42.pdf`, 50 A4
  pages / 341,080 bytes / SHA-256
  `9FC0CBB681C799BDE99E9F38B6DB02095C6F88B25E2857FB5062C869E38C1FF1`.
  Passes 2 and 3 have identical console SHA-256
  `B6DE06A3F857E1686415B08D7CDB8D5AB739E19ADAD0EBB99929E0B6018AE905`;
  checked diagnostics are zero. Output pages 49--50 were rendered at 1200
  dpi and personally inspected; seam, list, quotient powers, graded-ring and
  polynomial notation, citation, clipping, and page envelopes pass.
- The admitted EGA I source through complete 7.2.6 is 221,260 bytes,
  SHA-256
  `164886484D2F354B8DAF7652DAC6702F38968E41887E4085E906121B3D536C14`.
- Advanced the exact French cursor to Proposition 7.2.7 on printed p.64; it
  crosses to printed p.65 and remains wholly unadmitted.
- Generated and personally inspected printed p.65 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping direct 5000-dpi
  bands. Transcribed Proposition 7.2.7 across the p.64/p.65 seam and complete
  Corollary 7.2.8, Proposition 7.2.9, and Corollary 7.2.10 with their proofs;
  stopped before Remark 7.2.11, which crosses to p.66.
- Bound the p.65 authority surface in
  controls/EGA1_PRINTED65_SECTION727_7210_DIRECT_AUTHORITY_IMAGES.csv, seven
  rows / 1,447 bytes / SHA-256
  E17C62749CA61C6B2F2DAF9CC8BB7F99C1DA1A3D58AC5657FCE59A10479BAF31;
  replay is 7/7 with errors 0.
- Recorded six source-backed English dispositions. Four are direct English
  defects: “and” for “in”, duplicated “to”, an omitted module factor M,
  and a number-agreement error. Two are retained French source defects:
  M^(0) must be M^(1) in the degree-zero generator sentence, and M→M_n must
  be M→M_(n-1) in the kernel sentence. The latter independently confirms
  the existing English erratum. The ledger is now 114 unique rows / 86,824
  bytes / SHA-256
  51FAE3C1233B7FDCA0B0C758C4F13BB5C749A737A86302ABF2DE06A106C2842C.
- Rebuilt in three converged passes as
  qa/ega1_chapter0_build/ega0-pages11-65-through-7210-check-r43.pdf, 51 A4
  pages / 349,890 bytes / SHA-256
  DA44BCB63605AF4B422816D9C3AF83C4043F93EA2F7BCA81A12875E34545775C.
  Passes 2 and 3 have identical console SHA-256
  D839C2544F7EB2ADB3CACDB3C5921036E8917109725A6839E3F23C0D9A5BA8A7;
  checked diagnostics are zero. Output pages 50--51 were rendered at 1200
  dpi and personally inspected; seam, inverse limits, filtration powers,
  quotient/tensor formulas, projective-system notation, clipping, and page
  envelopes pass.
- The admitted EGA I source through complete 7.2.10 is 228,325 bytes /
  4,845 lines / SHA-256
  5DF72B3392DBADB9C3328F2CB7540E38312563092D1C59AAE4DD03EC2E41B3ED.
- Advanced the exact French cursor to Remark 7.2.11 on printed p.65; it
  crosses to printed p.66 and remains wholly unadmitted.
- Generated and personally inspected printed p.66 as one 1400-dpi context
  page, one direct 5000-dpi full page, five overlapping direct 5000-dpi
  bands, and a targeted direct 5000-dpi inverse-limit crop. Transcribed
  Remark 7.2.11 across the p.65/p.66 seam, Example 7.2.12, 7.3.1, Krull's
  Theorem 7.3.2, and the Artin--Rees Lemma 7.3.2.1.
- Bound the p.66 authority surface in
  controls/EGA1_PRINTED66_SECTION7211_7321_DIRECT_AUTHORITY_IMAGES.csv,
  eight rows / 1,684 bytes / SHA-256
  B5669D92399E248E6BCDAF4F43DA21254CDBBCCEF331C0D2A4FE9DF9E7B12A6C;
  replay is 8/8 with errors 0.
- Confirmed the printed 7.3.1 source typo directly: the second inverse-limit
  subscript is u although the quotient system is indexed by n. Canonical
  French retains u, and English n is a justified source correction. Also
  recorded two English prose defects. The ledger is now 117 unique rows /
  89,159 bytes / SHA-256
  3F56E5F7F24E321BB7AECECFC26174937139527744AD834A7CF509ED3CFD3652.
- Rebuilt in three converged passes as
  qa/ega1_chapter0_build/ega0-pages11-66-through-7321-check-r44.pdf, 52 A4
  pages / 355,473 bytes / SHA-256
  BD1AD40130731C8E75C4D6FFB1D930E0D994FF1E0097733967DD475EE132A85A.
  Passes 2 and 3 have identical console SHA-256
  BF131B661A21612535CD1C90A46C44B8E9AADBD951BBBFFD1468546D03884A37;
  checked diagnostics are zero. Output pages 51--52 were rendered at 1200
  dpi and personally inspected; seam, closures, inverse limits, exact
  sequences, completion hats, named statements, clipping, and page envelopes
  pass.
- The admitted EGA I source through complete 7.3.2.1 is 232,399 bytes /
  4,943 lines / SHA-256
  00F9756104A5EC737A024AF23F9A63D649BE321A7F172B4AC774175B1FA574F3.
- Advanced the exact French cursor to Corollary 7.3.3 on printed p.67; it
  remains wholly unadmitted.
- Generated and personally inspected printed p.67 as one 1400-dpi context
  page, one direct 5000-dpi full page, and five overlapping direct 5000-dpi
  bands. Transcribed complete Corollaries 7.3.3--7.3.4 and reconstructed the
  7.3.3 completion diagram as native TikZ-cd; stopped before Corollary 7.3.5,
  which crosses to p.68.
- Bound the p.67 authority surface in
  controls/EGA1_PRINTED67_SECTION733_734_DIRECT_AUTHORITY_IMAGES.csv, seven
  rows / 1,481 bytes / SHA-256
  5DBA53780E8CEC0EC459F39F1E189B8A988525F9C8DDAC4F8C4999B3FAE22594;
  replay is 7/7 with errors 0. No new English defect was found.
- Rebuilt in three converged passes as
  qa/ega1_chapter0_build/ega0-pages11-67-through-734-check-r45.pdf, 52 A4
  pages / 359,144 bytes / SHA-256
  8542F9A492F245FBC2CA656D23E3CF027076A50F9CAF7D3EF702C992DFE0FA1F.
  Passes 2 and 3 have identical console SHA-256
  B9F7FAE777D48400536463D1BD61565947AFA9934E691348EA0DA2EF3863332E;
  checked diagnostics are zero. Output page 51 is unchanged from R44, and
  output page 52 was rendered at 1200 dpi and personally inspected. Its SHA
  is BF1EA4FE16215514A693EDF0FF129304388659E65AB18DC0048AD18E9CB35DCE;
  seam, completion maps, exact rows, native diagram arrows, formulas,
  clipping, and page envelope pass.
- The admitted EGA I source through complete 7.3.4 is 234,944 bytes /
  5,010 lines / SHA-256
  C56C46877E10DCC2D3E8050E752C0FC56C5A9C7DBC930F5C277FEBD6BCA45188.
- Advanced the exact French cursor to Corollary 7.3.5 on printed p.67; it
  crosses to p.68 and remains wholly unadmitted.
- Established from the Windows boot record that the machine rebooted at
  2026-08-02 11:37:54 +02:00. No EGA file had been modified after that boot
  before the present recheck; the intervening task activity was read-only
  status/diagnostic work, so there was no low-effort source mutation to undo.
- Re-read the complete provisional p.68 addition personally against the
  direct NUMDAM authority: one 1400-dpi page for navigation, one direct
  5000-dpi full page, and five overlapping direct 5000-dpi bands. Admitted
  complete Corollaries 7.3.5--7.3.7, the section-7.4 heading, Definition
  7.4.1, and its two following explanatory paragraphs. The exact printed
  clause `$x\in\mathfrak Jx$` in 7.3.7 is retained rather than normalized.
- Bound the accepted p.68 surface in
  `controls/EGA1_PRINTED68_SECTION735_741_DIRECT_AUTHORITY_IMAGES.csv`, seven
  data rows / 1,474 bytes / SHA-256
  `A0C0FD4A8A58224F9C93A3A19C23337051079154EF999C8ECCF0DE936D1F8420`;
  replay is 7/7 with errors 0.
- Compared the corresponding English 7.3.5--7.4.1 passage with the established
  French authority. No unsupported mathematical correction and no new
  normalization requiring ledger admission was found. The correction ledger
  therefore remains 117 data rows / 89,159 bytes / SHA-256
  `3F56E5F7F24E321BB7AECECFC26174937139527744AD834A7CF509ED3CFD3652`.
- Rebuilt in three serialized converged XeLaTeX passes as
  `qa/ega1_chapter0_build/ega0-pages11-68-through-741-check-r46.pdf`, 53 A4
  pages / 363,893 bytes / SHA-256
  `625D17308AEDC519272E92C6447E9FD22D4829AA34DE1AC6C01E9C386022FC37`.
  Passes 2 and 3 have identical console SHA-256
  `19ED29D2C03DF1D52FB93A82FD357651198785DD56B4A8B19FAB3A441A11FF61`;
  fatal, undefined, duplicate-destination, missing-character, rerun, and
  overfull diagnostics are zero. Output pages 52--53 were rendered singly at
  600 dpi and personally inspected; this output render is a layout check, not
  source-reading evidence. Page seam, theorem typography, equations, section
  transition, clipping, and page envelopes pass.
- The admitted EGA I source through complete 7.4.1 is 239,076 bytes / 5,100
  lines / SHA-256
  `B67D532198A8C7E4DFCAD5E39246D162960AAC351DBB2F805F321AABA363AAAB`.
- Advanced the exact French cursor to Proposition 7.4.2 on printed p.68; it
  crosses to p.69 and remains wholly unadmitted.
- Recorded the corpus-scale restart state in `CONTINUATION_HANDOFF.md`. The
  current task remains bounded to EGA production. After EGA completion, the
  distinct Deligne scope is to be handed to one smaller existing Deligne task
  rather than accumulated in this already large task.

## 2026-08-02 — normalization rationale and reversal accounting made controlling

- Adopted the user's controlling rule that every intentional English
  departure from the printed French must be individually justified and that
  every later reversal must be append-only, blame-aware, and repaired across
  every active English source copy rather than only locally.
- Wrote the exact policy and checkpoint accounting in
  `controls/ENGLISH_NORMALIZATION_DECISION_AND_REVISION_POLICY_20260802.md`.
  The existing 117-row `controls/ENGLISH_CORRECTION_RECHECK.csv` remains the
  per-instance rationale annex through printed p.68; its historical bytes are
  preserved.
- Replayed all 117 rows with an exact final-field status rule. The current
  split is 91 confirmed English errors, 21 French-source issues, two official
  EGA II erratum/addendum decisions, and three external additions absent from
  the bounded NUMDAM EGA I body. Ten decisions are formally marked
  source-justified; thirteen further French-source correction/normalization
  dispositions remain pending successor and/or visible-note closure.
- Recorded that the separate master queue has 54 substantive readings still
  awaiting direct NUMDAM recheck plus six structural no-edit rows. It is not
  arithmetically added to the 117-row ledger because overlap has not yet been
  reconciled.
- Caught a machine-readability defect in the historical rationale annex: five
  rows contain an unquoted comma in the rationale and therefore parse as 15
  fields rather than the 14-field schema. No mathematical record is lost and
  the final status field remains exact. The historical file was not edited;
  any corrected machine successor must be no-overwrite, preserve all 117
  stable IDs, and record reciprocal supersession.
- Honest current decision-error count: zero admitted English source-correction
  decisions have yet been reversed; one proposed mathematical correction
  (the 5.4.6 `m/n` exponent candidate) was rejected before admission; two
  inherited non-diplomatic French accent normalizations were reversed against
  NUMDAM. Older workflow errors were recorded narratively but not under a
  countable taxonomy, so no fabricated historical total is claimed. From this
  checkpoint onward, each judgment reversal and each source-affecting workflow
  error receives its own classified append-only entry.
- Stable baseline IDs are
  `EG-EGA-FR-INTRO-A-OSCAR-INHERITED-NORMALIZATION-REV-001`,
  `EG-EGA-FR-INTRO-A-TITRE-INHERITED-NORMALIZATION-REV-001`,
  `EG-EGA-I-P51-546-M-N-CANDIDATE-REJECTED-001`, and
  `EG-EGA-CONTROL-CSV-UNQUOTED-COMMA-001`; their individual rationales and
  error ownership are recorded in the controlling policy file.
- Adopted the global archive-provenance rule that privacy-clean logbooks,
  decision rationales, reversal history, and continuation records must be
  deposited in both the methodology DOI and the replication DOI. The durable
  cross-project control is
  `03_projects/language_management/english_germanic/00_lane_control/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md`.
  The rule was relayed to the replacement archive task and the two other active
  production tasks. No mutable EGA logbook was handed off or uploaded.

## 2026-08-02 — EGA I printed p.69 / 7.4.2--7.4.5

- Read the p.69 authority directly from one 1,400-dpi navigation render, one
  direct 5,000-dpi full page, and five overlapping direct 5,000-dpi bands. The
  exact seven-file surface is bound by
  `controls/EGA1_PRINTED69_SECTION742_745_DIRECT_AUTHORITY_IMAGES.json`, 3,115
  bytes / SHA-256
  `2CCF0BDFEDC221B1B6C9298EBCF1442E20B79BA72AF4D50411A309E8C959B9E1`.
  OCR/extracted text remained locator material only. A Poppler 5,000-dpi band
  attempt produced a blank, non-adjudicative raster after a memory-allocation
  failure; it is excluded from authority evidence and preserved under
  `superseded_failed_poppler_memory_20260802_p69`.
- Transcribed Proposition 7.4.2 across the p.68/p.69 seam, Corollary 7.4.3 and
  its proof, numbered paragraph 7.4.4, and Corollary 7.4.5 and its proof.
  French wording, notation, punctuation, and numbering are diplomatic. The
  `\oldpage[0\textsubscript{I}]{69}` marker is placed at the exact source seam.
  The admitted file is `source/ega1/ega0-1-fr.tex`, 242,901 bytes / 5,180
  lines / SHA-256
  `9A072E70A9652DA484529BC2F136FF2D682C4244C7C9F6B0E0445E4CDDA729AC`.
- Compared the complete parallel English passage against the direct authority
  and admitted exactly three new decisions in
  `controls/ENGLISH_CORRECTION_RECHECK_APPEND_20260802.jsonl`, three records /
  4,790 bytes / SHA-256
  `0AC3732031D359DA8F547BDCFA1B9850A353BF5ADF1604B4BBABA9C487480560`:
  - `EG-EGA-I-P69-742-NHK-MISSING-M-EN-001`: French visibly prints
    `\mathfrak n^{hk}M`. English omitted `M`, turning a submodule inclusion
    into a type-invalid ideal-power/module inclusion. Required repair: restore
    the module factor.
  - `EG-EGA-I-P69-743-742-VS-724-XREF-EN-001`: French explicitly says
    “Sous les hypothèses de (7.4.2)”. English linked 7.2.4, which is unrelated
    to the local hypotheses. Required repair: link Proposition 7.4.2.
  - `EG-EGA-I-P69-744-PRECEDING-JUSTIFICATION-OMISSION-EN-001`: English
    omitted “en vertu de ce qui précède” and obscured that precisely two
    jointly required conditions follow. Required repair: restore the
    preceding-argument justification and “the conjunction of the following
    two conditions”.
- These are inherited English-reader defects, not corrections of the French
  author and not reversals of an admitted lead judgment. The complete 127-file
  editable English source tree was copied without overwrite to
  `03_projects/language_management/english_germanic/<REDACTED_INTERNAL_WORKSPACE>/EGA_English_Global_0_IV_french_recheck_source_successor_20260802_r1`.
  Exactly one file changes: `source/ega0/ega0-7.tex`, predecessor SHA-256
  `DA01D1C953C721896DFBD2FCA241D25EE61625963AEAFCC9F14F69280E99F77C`,
  successor SHA-256
  `BF941F818AC3F174FD4C9DD3013761BB19A9811898D970FCBB686C8EDEE3BCB7`.
  Repair-state transitions are append-only in
  `controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_20260802.jsonl`, three
  records / 2,760 bytes / SHA-256
  `3F12C0504D7A24802A18DBA525F7395FB63F6E87F8C632B8230825713FEE459A`.
  The successor is not yet a rebuilt/public replacement.
- The first English diff validator was wrong: it expected one generic
  `0.7.4.2` target occurrence, but the file correctly contains two. The false
  FAIL is preserved at 849 bytes / SHA-256
  `CC93AAC01C58349764783D1E298C5E43EC2D3F8772F9F73AA46BD466C951392C`.
  The corrected no-overwrite R2 validator binds the complete Corollary
  sentence and exact formula: 1,588 bytes / SHA-256
  `CCD7E96E872A65E36CEF6F7CF6F8B2436CE4332DD1865DA81CE0AA17809FEA9F`,
  `PASS_SOURCE_SUCCESSOR_DIFF`, errors empty. This was a lead-authored
  validation mistake caught immediately; no source byte depended on it.
- Built the French bounded reader in three correctly quoted, serialized
  XeLaTeX passes as
  `qa/ega1_chapter0_build/ega0-pages11-69-through-745-check-r47.pdf`, 54 A4
  pages / 367,924 bytes / SHA-256
  `1F0C8B44B9C8026014D5521736896A2510F1706D7EF9A78487DC0A35A51EF72F`.
  Passes 2 and 3 have identical console SHA-256
  `A9806224D1203C928B92EC965824A9CFD0D320B21DF040AC5A093D464211467B`;
  fatal, undefined, duplicate-destination, missing-character, rerun, overfull,
  and underfull diagnostics are zero.
- Personally inspected changed output pages 52--54 at 1,200 dpi. Their exact
  SHA-256 identities are respectively
  `C7CD7444DB916D12B919FC6553B34F2D832C3390EDF7DA025116BB177B1BBD9A`,
  `FDB87891CB13BA9DCF7459522CCF93B4432DB468107CE08D8160563F3847E3D0`,
  and
  `F235D106504741E967ED86B4C14098CAFFCC18A9925F7286D3551606A88339A7`.
  The p.68/p.69 seam, the 7.4.2 inclusion formula, Corollary 7.4.3, the 7.4.4
  two-condition list, Corollary 7.4.5, typography, clipping, and page envelopes
  pass. These output renders establish layout only; the direct authority
  images establish source reading.
- The first R47 command was also wrong: literal PowerShell variable names were
  passed as output/job paths and wrote a non-controlling log under
  `qa/ega1_chapter0_build/$dir/$job.log`; it did not alter source. Together
  with the blank Poppler crop and false-negative English validator, this is
  recorded in `controls/WORKFLOW_ERROR_APPEND_20260802.jsonl`, three records /
  2,222 bytes / SHA-256
  `08611645794C98E11A5356D5C200FFE6C42662C18158A9BCF84CD6A4D30FFD68`.
  Two of the three are explicitly marked `lead_was_wrong: true`.
- Archive custody acknowledged the dual-logbook-DOI requirement under
  `EG-ARCHIVE-DUAL-DOI-LOGBOOK-CUSTODY-CONTROL-20260802-0001`, binding
  methodology concept `10.5281/zenodo.21124403` and replication concept
  `10.5281/zenodo.20461174`. Mutable EGA is excluded and no upload occurred.
- Exact next cursor: section 7.5 / numbered paragraph 7.5.1 on printed p.69,
  crossing to p.70. None of section 7.5 is admitted.

## 2026-08-02 — EGA I printed pp.69--70 / 7.5.1--7.5.3

- Read the new source range personally from the direct NUMDAM authority. The
  exact surface is bound by
  `controls/EGA1_PRINTED69_70_SECTION751_753_DIRECT_AUTHORITY_IMAGES.json`,
  ten files / 3,841 bytes / SHA-256
  `5B7BC847AF9B6765D6C8C62C14A439B97B74DCBEFB186C2421E0B9F260DE90D7`.
  It includes a 1,400-dpi context page, a direct 5,000-dpi full page, five
  overlapping direct 5,000-dpi bands, and a tight direct 9,000-dpi crop for
  the ambiguous second display in 7.5.2. OCR/extracted text was used only to
  locate the passage.
- Transcribed the section-7.5 heading, complete numbered paragraph 7.5.1
  across the printed-p.69/p.70 seam, and complete 7.5.2 and 7.5.3. Wording,
  notation, punctuation, and source oddities are diplomatic. The admitted
  file is `source/ega1/ega0-1-fr.tex`, 248,060 bytes / 5,282 lines / SHA-256
  `7F7758B1F6891D1B58E40C240C74C3FD359D04614410948B8D3CAAA037A23F5E`.
- The targeted 9,000-dpi crop is
  `qa/ega1_chapter0_authority_5000dpi_details/p70-752-second-display-direct-pymupdf-9000dpi-r1.png`,
  3,152,583 bytes / SHA-256
  `1DCFF8264E9A437610F9CE234638ABBD0238B75366AFFF94E01A1D2EED93F399`.
  It proves that the printed French really contains one unmatched opening
  square bracket before the iterated restricted-series expression. The
  French TeX therefore preserves `\Bigl[`; it is not silently repaired.
- Compared the complete parallel English passage and admitted six individual
  decisions in
  `controls/ENGLISH_CORRECTION_RECHECK_APPEND_P70_20260802.jsonl`, six
  records / 8,437 bytes / SHA-256
  `A49C199D52DB2623B86B880FC22951014A8C60558C4B1DD0DE58419A2D920494`:
  - `EG-EGA-I-P69-751-COMPLIMENTS-VS-COMPLEMENTS-EN-001`: French
    `complémentaires` is set-theoretic; inherited English `compliments` is an
    unrelated word. Repair to `complements`.
  - `EG-EGA-I-P70-751-JLAMBDA-MISSING-SUBSCRIPT-EN-001`: the authority has
    the quotient by `J_\lambda`; inherited English made lambda an adjacent
    token. Restore the subscript.
  - `EG-EGA-I-P70-751-COEFFICIENT-ARTICLE-OMISSION-EN-001`: restore `the` in
    the unique `T^\alpha` coefficient phrase.
  - `EG-EGA-I-P70-751-IS-VS-IT-REMAINS-EN-001`: inherited `is remains` has no
    source basis; repair to `it remains`.
  - `EG-EGA-I-P70-752-STRAY-OPEN-BRACKET-SRC-001`: preserve the unmatched
    bracket diplomatically in French, but confirm the existing English
    omission as a nonmathematical source-typography normalization.
  - `EG-EGA-I-P70-753-CHARACTERIZE-SVA-EN-001`: the singular subject
    `this property` requires `characterizes`, matching French
    `cette propriété ... caractérise`.
- Applied the five actual English edits in the complete copied no-overwrite
  source successor. The five repair events are
  `controls/ENGLISH_CORRECTION_REPAIR_APPLICATION_P70_20260802.jsonl`, 4,362
  bytes / SHA-256
  `739A28F3C6E989BCA2E999BABA73CC019E05BFDA6F3D97DBC0598D5FA271F421`.
  Together with the three p.69 repairs, the current English source is 75,196
  bytes / SHA-256
  `1E33F146B32D3EDEEF978DE63A9FB06F856E027D02F0C8BDD7F49B4482C96CE5`.
  No admitted lead source-correction decision was reversed.
- Built the French bounded reader in three serialized converged XeLaTeX
  passes as
  `qa/ega1_chapter0_build/ega0-pages11-70-through-753-check-r48.pdf`, 55 A4
  pages / 374,459 bytes / SHA-256
  `D2F0393B08389251626806CE801EE73D319EADB8F4D6A89D6240DB88930B6631`.
  Passes 2 and 3 have identical console SHA-256
  `9686CB238B8CD6A3ED5A9B3975E291D9E6866844F45FEA5D3C85384EDAE294CA`;
  fatal, undefined, duplicate-destination, missing-character, rerun,
  overfull, and underfull diagnostics are zero.
- Personally inspected output pages 53--55 at 1,200 dpi. Their identities are
  3,643,207 bytes / SHA-256
  `86AB8FA32B089BBF48ED017C954F9737909320CF00C63B99ADBA68322E1FCD5F`,
  3,626,156 bytes / SHA-256
  `41A41D1A0F7EE130391BDEDB9CA3D34E6B29531DD21D72517319E6424B7637E4`,
  and 2,625,027 bytes / SHA-256
  `3051DA3529ED3C4C9A32E3A050A0672AB9B23ADFC71A9495D306DC1DE763CEC5`.
  The predecessor seam, p.69/p.70 seam, restricted-series limits, projective
  system formulas, the deliberately unmatched source bracket, clipping, and
  page envelopes pass. These renders establish layout only; direct authority
  images establish source fidelity.

## 2026-08-02 — English successor manifest R2/R3 failures and R4 closure

- Preserved two lead-authored manifest-generation mistakes rather than
  rewriting them. R2 had a null total and did not implement its declared sort;
  R3 repaired every row and total but hashed list order while claiming ordinal
  path order. Archive maintenance independently caught the R3 mismatch: its
  rows were 127/127 exact, but the declared `A6BBB177...` aggregate did not
  replay. These are control-plane errors with no source effect.
- The mistakes are classified append-only in
  `controls/WORKFLOW_ERROR_APPEND_P70_20260802.jsonl`, 986 bytes / SHA-256
  `3BE1A68CB0336FFDCBCD50095824E57022D5B948F7CED05BEB92FCAA3E01E835`,
  and `controls/WORKFLOW_ERROR_APPEND_P70_R2_20260802.jsonl`, 1,233 bytes /
  SHA-256
  `6EAAAD8369F585709DD90F0A315F6BF39B048D9EA5565B63EB1B2EE52166E8A1`.
- The current English-source manifest is
  `controls/SOURCE_INPUT_SHA256_R4.json` in the English successor: 23,160
  bytes / SHA-256
  `E2D57DA04123015CA761E081142152EB4DF60029A914C94B3E4C89C180F81FD0`.
  Independent replay confirms 127/127 paths, 7,279,784 bytes, ordinal order,
  and exact aggregate
  `0E7BBF54FB4C5EC7C6EE5660909351A8788D7581F0DA8AAFB6C991D2CE490CAD`,
  errors empty.
- The append-only current source-diff validation is
  `controls/SOURCE_DIFF_VALIDATION_R4.json`, 3,893 bytes / SHA-256
  `C20119C23B354AE4EB56E0EB22F9C9DECF5F356235FA433EFCC7F21514BEEEC4`;
  its independent replay is 1,824 bytes / SHA-256
  `2DA2C5DBDBE07C8FD923DFA27BE882F83A3F0A53210B0271B75FF679C47CB6FA`.
  Exact comparison against the frozen predecessor proves one changed file and
  all eight repaired readings present once with obsolete readings absent.
- The repair-validation rebind is separately append-only in
  `controls/ENGLISH_REPAIR_VALIDATION_SUPERSESSION_P70_20260802.jsonl`, 1,588
  bytes / SHA-256
  `C57BB7E0C71ED5ECCDF3FC0B5B3D779E17E374611CFA38147FDC188D0E3E41EC`.
  R3 remains valid evidence for its source assertions but is superseded as
  the current gate because of its manifest dependency.
- Archive maintenance made no GitHub or Zenodo mutation. Global build,
  reference-coordinate replay, privacy-clean projection, rights/caveat and
  package closure, explicit handoff, public readback, and dual-DOI logbook
  deposit remain held.
- Exact next French cursor: Proposition 7.5.4 at the bottom of printed p.70,
  continuing on printed p.71. No Proposition 7.5.4 text is admitted.

## 2026-08-02 — EGA I printed pp.70--71 / Proposition 7.5.4

- Read Proposition 7.5.4 personally from the direct NUMDAM scan. The exact
  five-image surface is bound by
  `controls/EGA1_PRINTED70_71_PROP754_DIRECT_AUTHORITY_IMAGES.json`, 2,663
  bytes / SHA-256
  `D4AC485571C2BA8DC4E2DE59664728D5488A29217B6E723825E198A399489C58`.
  The proposition opening uses the already-bound direct p.70 5,000-dpi
  terminal band; the statement continuation and full proof use three
  overlapping direct p.71 5,000-dpi bands. A 1,400-dpi page gives navigation
  context only.
- Transcribed the complete two-part statement and proof diplomatically,
  including the exact printed p.70/p.71 seam, primes on $u'_{ij}$, ideal
  indices, powers, inequalities, and the final reference (7.2.8). The current
  French source is 251,121 bytes / 5,341 lines / SHA-256
  `52B886E42D7B2C904074DEC2725475D43519D95EC5D7A6C9BF94291B4B505561`.
  Proposition 7.5.5 remains wholly unadmitted.
- Compared the parallel English passage and recorded four independent
  inherited defects in
  `controls/ENGLISH_CORRECTION_RECHECK_APPEND_P71_20260802.jsonl`, four
  records / 5,116 bytes / SHA-256
  `99CF1649C8AB3128F57192C7D759907D6398DDEB071BDF8F232571A5C986518C`:
  - `EG-EGA-I-P71-754-U0I-MISSING-PRIME-EN-001`: the source says the kernel of
    the induced polynomial-ring map $u'_{0i}$; English named unprimed
    $u_{0i}$, a different map.
  - `EG-EGA-I-P71-754-UIJ-MISSING-PRIME-EN-001`: the later kernel claim also
    requires $u'_{ij}$, not unprimed $u_{ij}$.
  - `EG-EGA-I-P71-754-JI-VS-JJ-EN-001`: the monomial lies in the stage-$j$
    polynomial ring, and the direct source explicitly says a product of
    elements of $\mathfrak J'_j$; inherited English printed
    $\mathfrak J'_i$.
  - `EG-EGA-I-P71-754-NOTHERIAN-TYPO-EN-001`: inherited English misspelled
    `Noetherian` as `Notherian` in the conclusion.
- Applied all four repairs in the complete copied no-overwrite English source
  successor. The source is now 75,199 bytes / SHA-256
  `8DD6840E73ADBE9D529AE39979B495BB7BC2D4CAFC8DE72C2F2EA870E46D1528`.
  Repair events are four records / 3,424 bytes / SHA-256
  `E174622ECF18029DF74D0B2022D9DDD79B1C2C96A6BF33B6F7972A000FE3FDB0`;
  the R4-to-R5 validation transition is one record / 1,293 bytes / SHA-256
  `EA68A38E2E9DE87E0045CF4D4E5BD34628D9DAA00032B46C091F54028ABCDC5A`.
- Generated the English R5 source manifest with the corrected ordinal
  algorithm. Independent Python replay confirms 127/127 files, 7,279,787
  bytes, and exact tree SHA-256
  `30E8197C89FCE61EEB9ACAC82EE40985CB7C1B8F277FE627181B9C4195A8DCDA`,
  errors empty. Manifest: 24,084 bytes / SHA-256
  `38E8BD3642A7CBDE07428D9D13447A75DBFD6AAEE0A8B2B682B9F989DEEDB61C`.
  Current diff validation: 4,489 bytes / SHA-256
  `F0987DB31A57930111FD97A551DC379E6D68AA5701FC93673E0C229FC5B3956E`;
  replay: 2,138 bytes / SHA-256
  `F8E9B03EE5FE51A51C3EEB4BD2105692A599E383681F4F7A5CDB915388BB4108`.
- The first direct p.71 crop invocation was wrong: Cairo cannot create the
  requested 35,764-pixel-wide surface. It emitted a zero-byte file, caught by
  immediate exit-code/size inspection. The zero-byte artifact is preserved as
  excluded non-evidence; three serial direct PyMuPDF 5,000-dpi crops replaced
  it. The first build invocation then repeated a known PowerShell equals-form
  quoting error and wrote to literal `$build/$jobName`. Its noncontrolling PDF
  is preserved at 378,291 bytes / SHA-256
  `62A66482E4D74945AA7086647C9C24025C7A03C3449220E124E20E05909292C4`.
  Both lead-authored errors, their source-effect `none`, and their recovery are
  in `controls/WORKFLOW_ERROR_APPEND_P71_20260802.jsonl`, two records / 1,426
  bytes / SHA-256
  `34A0C65B16136EE976CC18FEC12294B50FDBC991528A4341F900FF3B7A5A0042`.
- Reran without overwrite as R50 using explicit native-command argument
  strings. Three serialized passes exit 0; passes 2 and 3 are byte-identical,
  14,898 bytes / SHA-256
  `10BBD2479D4BCF451FB56E9E715653B145FDDBABF4704F607D72349E79E7C90B`;
  final fatal, undefined, citation, duplicate-destination, missing-character,
  rerun, overfull, and underfull diagnostics are zero. Controlling PDF:
  `qa/ega1_chapter0_build/ega0-pages11-71-through-754-check-r50.pdf`, 56 A4
  pages / 378,288 bytes / SHA-256
  `BA4E1BAA58FD8DE9DED8C48E6C6A7AE92898083CA770FC7590FE8655A84C3598`.
- Personally inspected output pages 54--56 at 1,200 dpi. Their exact
  identities are 2,553,404 bytes / SHA-256
  `D6F6016CB439611906074ED996AE71461C660BD95650F28190DB05358033A9D3`,
  2,377,354 bytes / SHA-256
  `20C0956CAF24B7DDDE7743155806BEE3038BF3E07F07FBBD67F33DB043042F1D`,
  and 937,967 bytes / SHA-256
  `43D1CCF4F45E924BA6E46C950E0F9019AC620234103D65E6FA0DEC24DE7D58E4`.
  The predecessor seam, p.70/p.71 seam, all transition-map primes and ideal
  indices, line breaking, clipping, and page envelopes pass. These renders
  establish layout only; the 5,000-dpi direct authority crops establish source
  fidelity.
- Exact next cursor: Proposition 7.5.5 on printed p.71, continuing on p.72.
  No 7.5.5 text is admitted. No admitted English source-correction judgment
  was reversed.

- Personally read Proposition 7.5.5 and §7.6 through Corollary 7.6.3 from
  seven overlapping direct-authority 5,000-dpi bands spanning printed
  pp.71--72. The 1,400-dpi whole p.72 image was navigation context only.
  Exact witness manifest:
  controls/EGA1_PRINTED71_72_PROP755_763_DIRECT_AUTHORITY_IMAGES.json,
  3,483 bytes / SHA-256
  668DF770147CA68EC7EEA4D8A06D7B06BFBB9E684AAEFF85AA4427FBC4B4CA24.
- Transcribed diplomatically the complete 7.5.5 statement and proof, §7.6
  heading and 7.6.1, Proposition 7.6.2 with its proof, Corollary 7.6.3, and
  the cautionary paragraph ending printed p.72. The French source now has
  5,463 lines / 257,449 bytes / SHA-256
  2F511A63F9F13EDC8DB12A365731B392F2931ADE690290A09151A5DC4DD0A2A1.
  The next exact cursor is Corollary 7.6.4 on printed p.73; no p.73 text is
  admitted.
- Confirmed five inherited English errors and repaired each in the
  no-overwrite English source successor: Notherian→Noetherian, and→an in
  A-algebra, the malformed quotient parenthesis/clause, this→thus, and the
  mathematically substantive omission of ker(v_lambda)=S^{-1}J_lambda in
  7.6.2. The last inherited sentence had incorrectly said that the kernel
  itself was surjective.
- Recorded three no-edit decisions as well: the printed
  B_n=B_m/J^{n+1}B_m transition formula is preserved exactly; French dans A
  is idiomatically rendered on A in the restriction statement; and séparé
  complété is rendered by the standard English term separated completion.
  The complete eight-row decision surface is 10,398 bytes / SHA-256
  502D5089998CE3BE4D69237730C99FE89F803FE3FED70CAEE521041DBA01F700.
  Five append-only repair events are 4,314 bytes / SHA-256
  55655CBB9E63D509534923F04A35E9171B2F0DEFB79557515973A32FB8EDE513.
- Generated the exact R6 English source manifest after these repairs:
  127/127 rows / 7,279,848 source bytes / ordinal tree SHA-256
  0B11488A0F866FBF0AF5575AF6E6F77B322C08969BD9034821210EF2F47A00A7.
  Both Python and PowerShell ordinal implementations replay the same tree.
  Manifest identity: 23,692 bytes / SHA-256
  C47C6AAD610A7FF3A15A54C5E3931C2E1E28A2D237D3D4D26FD845947C523B35.
  Current diff validation is 4,058 bytes / SHA-256
  9C210905CE159FED2B4CA6745CD5AAF3CC5F039502DC04FAD6805A44B7D34311;
  replay is 1,356 bytes / SHA-256
  23BB830C291DC10C349DC825A49FE41F2F78F271D746E528F0FD6863C3C64D11.
  Both pass with errors empty. The sole changed source remains ega0-7.tex,
  now 75,260 bytes / SHA-256
  C576296A78A1303323C7296A7CCF9B989FCA8FF7C2C8A981140F66651B17A747.
- Lead-error record: the first insertion used a nonunique end-enumerate patch
  anchor and temporarily placed 7.5.5 after 3.6.2. Immediate line-order replay
  caught it before any build; the misplaced block was deleted and reinserted
  after 7.5.4. A first nonforcing line-break hint also failed to clear the
  14.43265pt overfull line in 7.5.5(c); a forced layout break fixed it without
  changing text or mathematics. Both mistakes are append-only in
  controls/WORKFLOW_ERROR_APPEND_P72_20260802.jsonl, two records / 1,825
  bytes / SHA-256
  C98159F5C93A3FB73E589E8191A56B898EC60CCBF2A7F7AE4A431DE9229A517C.
- The controlling R54 French build used three serialized XeLaTeX passes.
  Passes 2 and 3 are byte-identical, 15,194 bytes / SHA-256
  E5A74E816A209D8A140E714F197F0AFDF9DDDF2D37B51CA350A479CF2B4FCED2;
  all checked diagnostics are zero. PDF:
  qa/ega1_chapter0_build/ega0-pages11-72-through-763-check-r54.pdf, 57 A4
  pages / 385,147 bytes / SHA-256
  FAC9F2A96AFAB501D852E27FC3CB2873B0BC5504718E2ABFAB3EE576708B21F8.
  Output page 56 is identical to its already-inspected R53 counterpart.
  Output page 57 was personally inspected at 1,200 dpi, 2,732,387 bytes /
  SHA-256
  B3B959464FB0AA9EFCB1A44E95A85C47E73A5BECD0B8F45B9B6D39B57BF0235B;
  the section transition, formulas, theorem typography, clipping, and page
  envelope pass. Direct 5,000-dpi authority bands, not this output render,
  establish source fidelity.

## 2026-08-02 — EGA I printed p.73 and Proposition 7.6.10 seam

- Personally read five overlapping direct 5,000-dpi bands covering printed
  p.73 and one direct 5,000-dpi p.74 seam band. The 1,400-dpi whole page was
  navigation context only. Exact witness manifest:
  controls/EGA1_PRINTED73_PROP764_7610_DIRECT_AUTHORITY_IMAGES.json, 3,354
  bytes / SHA-256
  8DCD975AEC1239EC200674C02ABB201C39377A0FE3848B56BBD8CDBB7B6F9849.
- Transcribed Corollary 7.6.4, 7.6.5--7.6.9, and Proposition 7.6.10 with its
  exact p.73/p.74 seam. The printed glyphs o/i and the empty-set glyph are
  encoded by their mathematical values 0/1 and varnothing under the standing
  diplomatic typeface-normalization policy; wording, formulas, numbering,
  punctuation, and order remain exact.
- Four inherited English errors were caught and repaired individually:
  both occurrences of topological adhérence had been reduced to ordinary
  membership; the singular couple had a plural verb; and u(S) had been made
  equal to the full set of units rather than a set of invertible elements.
  Decision ledger: four rows / 5,321 bytes / SHA-256
  E1438205B716BF612974FDDCB0E996DB69F08084FB30B0AE951839BF4F6D6E48.
  Repair events: four rows / 3,506 bytes / SHA-256
  BAFB5569FED2135065F3807BF0FCE094886F14723A3B18C9536E13BDC125680B.
- R55 provided the intermediate bounded page-73 check: 58 pages / 390,736
  bytes / SHA-256
  83E56E6E9AD3DC07DAB3F0E3235A7A72FA6296ED911D74670F76BC90C26A4FD4.
  Passes 2 and 3 were identical, SHA-256
  695266B866B48E006BF2B85D4DE0E6832944A417D3F856EF95873A89186B0877.
  Output pages 57--58 were personally inspected at 1,200 dpi and passed.
- R7 English source manifest and diff validation independently replayed
  127/127 rows and all 21 cumulative exact assertions. R7 source tree:
  7,279,843 bytes / SHA-256
  DAABF2C09264F8F9AD72F99131B71F65EC5810281F958ED1C62A23BCC547119F.
  Manifest SHA-256
  0B140962BB07769A3D6E1387D4A48D0E26907434F21C6A14E7527890FFCC1F3D;
  diff validation SHA-256
  BAC0585F97194BCDFC00FE3C935B7B2B9B3D1D8E07A7416B76007085FD7C1CC1;
  replay SHA-256
  C03A0F9015CFCF7D0AB1A85BDBFA1F0131ECD2732780189F2B295614FE0F45E7.

## 2026-08-02 — EGA I printed p.74 through Corollary 7.6.14

- Personally read all five overlapping direct 5,000-dpi p.74 bands. Exact
  witness manifest:
  controls/EGA1_PRINTED74_PROP7611_7614_DIRECT_AUTHORITY_IMAGES.json, 2,650
  bytes / SHA-256
  0C4CEC360787E787DB968EB8CAF6DB919BC9BAFF572790DF8843EC35B9EAC7B4.
- Transcribed Proposition 7.6.11 and proof, Corollary 7.6.12, Proposition
  7.6.13 and proof, and Corollary 7.6.14 and proof. Section 7.6.15 remains
  wholly unadmitted even though its opening was visible in the terminal band.
- The direct source prints “ce qui achève de démontrer la proposition
  (7.2.8)” inside the proof of Proposition 7.6.11. This cannot identify the
  proposition being proved because 7.2.8 is an earlier corollary. The French
  diplomatic source preserves 7.2.8 exactly. English now gives the forced
  7.6.11 locator and immediately states what French prints. The other repair
  restores the missing inverse exponent in S^{-1}J-preadic. Decision ledger:
  two rows / 2,939 bytes / SHA-256
  3F6280B1A1ED8E663597081ABC0F23FBEEDA199D348369CFC1E22F39F746F41B.
  Repair events: two rows / 1,964 bytes / SHA-256
  F3A407E38723F125B98DB9DD147BA04757C07E756F82ABE2E60ACC603C4E2CD0.
- Lead-error/reversal record: I initially wrapped the enumerated proof in an
  undefined proof environment. R56 failed on its first serialized pass; no
  output from it was admitted. I removed only that wrapper and retained every
  source word, formula, and item. The closed record is
  controls/WORKFLOW_ERROR_APPEND_P74_20260802.jsonl, one row / 1,027 bytes /
  SHA-256
  D34D6F0B0246D12038C7EBB403AEF62DA9A1A37119F6E24F093ECDAC7AD00DC9.
- The corrected R57 bounded reader converges in three serialized passes:
  59 A4 pages / 394,596 bytes / SHA-256
  BE505741832275CA07930B1C931F23094C74F8A2EAD8003628D95E4927A3837D.
  Passes 2 and 3 are identical, SHA-256
  A179DD91DFD948C44E01AA60199EA05F20AF7CE8293E10C9BB196DCB7745C458.
  All hard/reference/destination/missing/overfull diagnostics are zero; one
  pre-existing underfull remains. Output pages 58 and 59 were personally
  inspected at 1,200 dpi and pass.
- Current French source is 266,060 bytes / 5,641 lines / SHA-256
  C5D6E1F1367641E914C184892DEBDABF3B0EDDF2E2F2BD167835CD7430343A7D.
  Current English ega0-7.tex is 75,427 bytes / SHA-256
  3A7611B105182E45AA33C945C85E34A48A2C46369568A686F7E6F73810D54AA7.
- R8 replays 127/127 source rows / 7,280,015 bytes / ordinal tree SHA-256
  7A0E4D9FB6A352C04009029A692E3E9D133015ECBFBBF52005BEF95F0A6B5F1A
  in both Python and PowerShell. Manifest SHA-256
  6087C82E314965389977E80D4E964EBB47AA2A205D699B1160B5455FB21AE851;
  diff validation SHA-256
  33F169EA742114018CA857D6391CEE89ECD9ABDB92B77AE79952EBC6D1731C32;
  replay SHA-256
  0B6D72131B9918330D525A4932841A4D6244A709D4DFE4A88F9DB782E05D843C.
  All 26 cumulative exact assertions pass. The global reader and release gates
  remain deliberately held.

## 2026-08-02 — EGA I printed pp.74--75 through Corollary 7.6.18

- Personally reread the direct 5,000-dpi p.74 continuation band and four
  overlapping direct 5,000-dpi p.75 bands. The image, not extracted text,
  decided every exponent, localization subscript, barred class, inverse,
  ideal, and reference. Exact witness manifest:
  controls/EGA1_PRINTED74_75_SECTION7615_7618_DIRECT_AUTHORITY_IMAGES.json,
  2,993 bytes / SHA-256
  A5623387606C16D2DC3360971781F36E8D5BDF65FA70CD8C41D55636C8F39675.
- Transcribed paragraph 7.6.15 with its p.74/p.75 seam, Proposition 7.6.16
  and proof, Proposition 7.6.17 and proof, and Corollary 7.6.18 and proof.
  The exact next cursor is the section 7.7 heading and paragraph 7.7.1 on
  printed p.75; section 7.7 remains unadmitted.
- The inverse calculation in the proof of 7.6.17 was checked directly:
  after g=xf, the image y_0=x^{k+1}/g^k of x/f^k has inverse
  x^{k-1}f^{2k}/g^k. No source correction was imposed. The diplomatic French
  also preserves the exact combined reference “(7.6.9 et 7.1.12)” and the
  occurrence of p_{f} in the later maximal-ideal argument.
- Three inherited-English changes were made, each with a separate rationale:
  - French “plat sur chacun des anneaux” uses the standard English technical
    relation “flat over each of the rings,” not inherited “flat for.”
  - French explicitly says A_{S} “est un anneau local”; inherited English
    omitted “is” and was repaired.
  - French “On sait déjà” is idiomatically “We already know.” Replacing “We
    know from before” is a nonsemantic register normalization, and is logged
    precisely because it changes inherited English wording.
  Decision ledger: three rows / 4,464 bytes / SHA-256
  8FEEADF8588E430401C865293AE55DE34B9A73CC61894140FE475674183F2D52.
  Repair-event ledger: three rows / 3,047 bytes / SHA-256
  A2623653DFAB44EAB81F4657A05328BF283B1E77F8F35EB6D77E294FDD206CAC.
- Lead error and reversal: the first patch serialization lost the backslash
  of an unnecessary thin-space command and produced overline{f}^{,k}. The
  immediate post-patch source-line replay caught the comma before any build
  or checkpoint admitted it. I replaced it with the exact printed
  overline{f}^k and logged the error append-only in
  controls/WORKFLOW_ERROR_APPEND_P75_20260802.jsonl, one row / 1,003 bytes /
  SHA-256
  A95844DDAA237547B777E1EE745AD24AE5F39347D84BFF9DBEB3CBCB0005F51B.
  The lead was wrong in the initial encoding; the active source is globally
  repaired and no erroneous PDF exists.
- The R58 bounded French reader converges in three serialized passes. PDF:
  59 A4 pages / 399,323 bytes / SHA-256
  4C9F136C4A8C5DBDF939F4B0A0B4A68530BA52C9BAD8BD15669C968EC863ABF8.
  Passes 2 and 3 are byte-identical, SHA-256
  80DD0813E039BF798BB7C400D0D042F752E5D214E05DF4FD70D9E6D9F9E1A16F.
  All hard/reference/destination/missing/rerun/overfull diagnostics are zero;
  the sole underfull line predates this batch. Output pages 58 and 59 were
  personally inspected at 1,200 dpi and pass the seam, line-flow, formula,
  theorem-style, clipping, and page-envelope checks.
- Current French source: 270,458 bytes / 5,726 lines / SHA-256
  CBE2C566A9DE9366F3F5859AD2563C7EFCB36FA9DAC9A17C7DE73186692ADBB8.
  Current English ega0-7.tex: 75,432 bytes / SHA-256
  81196521B4A963CFD614452C63C1669482B4C58A6A2E250DD593B1B11159F036.
- R9 replays 127/127 source rows / 7,280,020 bytes / ordinal tree SHA-256
  B20246760E9A19F7050C457EC91697105B6CB255FBBDDEFF15DD0718716698AE
  in both Python and PowerShell. Manifest SHA-256
  203A7E34F3BC5683E4612DA4300358B4A5DD295EA2781454811EB2C15A38B05D;
  diff validation SHA-256
  40AC5CDB5B686B5468DCD67B26BD9C5BFCA329D080D0FC696181AAE6DF6E9C90;
  replay SHA-256
  0C984F40AA06735D214D7E3264FD7C5DC3C5AF1FFE5EEFACF2E0CE4C9A84A8AA.
  Exact inverse reconstruction reproduces the R8 source hash; all 32
  cumulative assertions pass. The global reader and release gates remain
  deliberately held.

## 2026-08-02 — EGA I printed pp.75--77 / complete §7.7

- Personally read nine direct NUMDAM 5,000-dpi bands covering the §7.7
  heading, 7.7.1--7.7.6, Proposition 7.7.7 and proof, and Proposition 7.7.8
  and proof. Exact authority manifest:
  `controls/EGA1_PRINTED75_77_SECTION77_DIRECT_AUTHORITY_IMAGES.json`, 4,998
  bytes / SHA-256
  `6E728F658C5D14E9E36E7D4C069E1AA2F77E6B888CEB3C78C31F12CD2FD3C0E8`.
  OCR/PDF text extraction was locator material only. The direct image decided
  every completion mark, tensor-product subscript, ideal, exponent, inclusion,
  cross-reference, and page seam.
- Diplomatic transcription now stops after the proof of Proposition 7.7.8.
  Current French source: 277,633 bytes / 5,878 lines / SHA-256
  `1D94EA4889F450CB70BAA4EFD2BB78779F843235064B6350C8941BF1261F5809`.
  Exact next cursor is the §7.8 heading and paragraph 7.8.1 on printed p.77,
  continuing onto p.78; no §7.8 text is admitted.
- Source finding `EG-EGA-I-P76-776-DUPLICATE-ET-UN-SEUL-SRC-001`: printed
  7.7.6 says that there exists an `A`-homomorphism `et un seul w ... et un
  seul tel que`, repeating the same uniqueness phrase. The French source
  retains both printed occurrences. The following proof and the universal
  property establish one unique map; English therefore states uniqueness once
  and exposes the normalization in an immediate visible stable-ID footnote.
- Six English decisions were made and justified separately:
  1. `Si l'on remarque que` is rendered “If we note that,” replacing inherited
     nonidiomatic “If we have that”; no mathematical content changes.
  2. `dans la catégorie` is “in the category,” not inherited “on the
     category”; this is a grammatical repair only.
  3. French `J idéal ouvert ... il en existe toujours` is existential.
     Inherited “the open ideal ... it always exists” falsely suggested a
     distinguished unique ideal; it is now “an open ideal ... such an ideal
     always exists.”
  4. The duplicated French uniqueness phrase is normalized once in English
     with the visible note described above.
  5. French `sur B\otimes_A M` names the module carrying a topology; standard
     English is “on,” not inherited “over.”
  6. French has singular `le produit tensoriel`; inherited plural “the tensor
     products ... is” is now singular, matching both the construction and verb.
  The 7.7.8 citation to 7.3.6 was also checked: 7.3.6 is indeed a corollary, so
  no correction was made there.
- Decision ledger: six rows / 9,404 bytes / SHA-256
  `41BF40298FAF27C1B5825A97E18FE2447890C18E682D5188EE7AF699F432413D`.
  Repair-event ledger: six rows / 6,517 bytes / SHA-256
  `C0B96FC24F1238951C1872FFE98D24E8CEDED30BB5DB1DC6197199D89000DC91`.
  No admitted English judgment was reversed in this batch, and no new
  mathematical/source-fidelity lead error was found.
- Typesetting process record: the first R59 build exposed one 9.62384 pt
  overfull line in the long inline 7.7.2 quotient. Two provisional
  discretionary-break attempts (R60 and R61) did not remove it and were not
  admitted. The final source instead uses a local `sloppypar`, which changes no
  visible wording or mathematics and clears the overflow. R59--R61 remain
  diagnostic history; R62 is controlling.
- R62 converges in three serialized XeLaTeX passes. PDF: 61 A4 pages / 407,900
  bytes / SHA-256
  `9CB826D387B962B2B3F8305F0E2253AB41CBD1F410B5F2070D43E737AB434875`.
  Passes 2 and 3 are byte-identical, SHA-256
  `80E1AB98AE356AA89684A8B863AF0C93BF8FFDBF20735B7FC56455A8C2CD5007`;
  all checked hard/reference/destination/missing/rerun/overfull diagnostics are
  zero. Physical pages 60 and 61 were personally inspected at 1,200 dpi:
  SHA-256 `3367079D25873972E813FC4178CF6A3681730B4A5B01410D64227339F74F9E5D`
  and `66DEA621C15058DE66C2CE6B5F16A0A5934AB17AE372F505609C1B2D21E43ECD`.
  Line flow, formulas, seam, clipping, and page envelope pass.
- Current English `ega0-7.tex`: 75,620 bytes / 1,397 lines / SHA-256
  `29008BF15E3674F9B84BACDC8168B38E3C2B4B25497B153B2F96C744629749D8`.
  R10 manifest: 127/127 exact rows / 7,280,208 bytes / ordinal tree SHA-256
  `07BA24509DBA3162F680445DD535574044B3BB0E6E2BE03604EAFCA170CB71E7`;
  manifest SHA-256
  `D564A77B667290642B5206B29EC32FD667552D543642CE30F6ADF5D08DF325AE`.
  Python and .NET-ordinal PowerShell replays agree. Diff validation SHA-256
  `C4EF8A240F3CEC321AA4437F4D810343E2F06B953F7A8736C99C39775FFD7444`;
  independent replay SHA-256
  `B43869F4F6BC4B04D86E98AC5CE530BF8602360DC3EE70865033D420DFA52A61`.
  Six exact inverse substitutions reproduce the R9 source byte-for-byte.
- No global English reader build, coordinate replay, privacy projection, or
  archive action was triggered for this pagewise batch. R2/R3 manifest errors
  and all predecessor controls remain append-only history. Release and
  dual-DOI logbook gates remain held.

## 2026-08-02 — EGA I printed pp.77--78 / complete §7.8 text checkpoint

- Diplomatic French §7.8 was transcribed through `(A suivre.)`, including
  7.8.1, Propositions 7.8.2--7.8.3, and both proofs. Current French source:
  282,088 bytes / SHA-256
  `359E04723FCCB70D8BB758184B85C4A6A467ACC549A7B5F7D40A0AE92FF053AC`.
  This is a text checkpoint only: no compilation or layout claim has yet been
  made for the newly appended range.
- Four inherited-English defects were repaired individually:
  1. restored the omitted noun `topology` in the 7.8.2 proof;
  2. corrected `following proof` to source-exact `preceding proof`;
  3. corrected `injective` to `surjective` at the opening of the 7.8.3 proof;
  4. restored the direction of the final induction argument: the induction
     implies membership in every power, rather than that conclusion serving
     as its premise.
  Current English source: 75,637 bytes / SHA-256
  `96983D270206173230D51B70885CB846FD03BB1692D5DFAC03667EE7F4156252`.
  The four-row decision ledger is 6,181 bytes / SHA-256
  `FA9F3D79F64EB856EF919934E44F581D24641719B8ED0662FDB73D472AB23811`;
  the four-row application ledger is 3,570 bytes / SHA-256
  `BE5F779257515C1705A26FDBF623FE89714E7F0B747A0A6C70A384EBCE96739C`.
  Exact inverse replay uses each substitution once and reproduces the prior
  75,620-byte English source SHA-256
  `29008BF15E3674F9B84BACDC8168B38E3C2B4B25497B153B2F96C744629749D8`.
  Validation is `controls/SOURCE_DIFF_VALIDATION_R11_SECTION78.json`, 1,373
  bytes / SHA-256
  `FEF06E5F4EBBF4A9F5FB4BB2B161471BAC4F127BB9699B397757C8F32605DDE5`,
  status `PASS_EXACT_FOUR_EDIT_INVERSE_REPLAY__HOLD_SOURCE_MANIFEST_AND_BUILD`.
- Process failure and permanent operating correction: one command generated
  twenty grayscale 5,000-dpi bands, generally 33,057 by 3,056 pixels, and the
  task then loaded all twenty at original detail. Although the files were
  compressed on disk, their decoded/context footprint was roughly two
  gigabytes and destabilized the PC during task compactification. This was a
  lead workflow error, not an authority or mathematical error. It must never
  recur. Future image work is strictly sequential and RAM-light: generate and
  inspect at most one tightly relevant crop when actually needed; use roughly
  1,100--1,400 dpi for ordinary context and escalate only for a genuinely
  ambiguous small feature. Never batch-render or bulk-load authority images.
  No agent, renderer, OCR process, compiler, or other background job remains.
- EGA indexing is henceforth not merely clickable-reference plumbing. The
  controlling pre-Stacks scaffold is
  `03_projects/language_management/english_germanic/00_lane_control/EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_20260802.md`,
  4,062 bytes / SHA-256
  `803F9DD750F521B52C02DD02A99A20D904D1E47C4204DD73350B419F2CA5BE4D`.
  Stable semantic nodes, typed dependency edges, hypotheses/conclusions,
  formula/diagram identities, terminology bindings, and correction/reversal
  provenance are captured when source-certain and cheap; deeper proof
  decomposition remains a later pass so it does not stall transcription.
- Evidence-reuse and agent rule added after the incident: search existing
  Codex/Claude authority images first and reuse an exact existing page/crop
  whenever sufficient. A new image is allowed only for a missing or ambiguous
  detail, one crop at a time. At most two or three agents may perform genuinely
  disjoint, low-intensity grunt work; no swarms, duplicate ranges, agent OCR,
  bulk rendering, parallel builds, release-scale audits, or delegated final
  source/mathematical judgments.

### §7.8 build and exact-source closure

- R63 failed on the first new occurrence of undefined `\Hom`. This was a
  typesetting-portability mistake imported from the English source, not a
  French reading or mathematical decision. R63 remains failed history under
  console SHA-256
  `3838620C4C4577277E3C31B9B834AE10E9EDBF91DB06FF289C3D18F070E41C9D`
  and log SHA-256
  `4239324A551A2CC5720337E0C987A082C6A8D284D160C230C21546C09566052C`.
  All thirty §7.8 occurrences were changed mechanically to portable
  `\operatorname{Hom}`; visible wording and mathematics are unchanged.
- Current French source: 282,508 bytes / 5,978 lines / SHA-256
  `5B6E27ADF94611E5B135E2316C1EEAB4B1EE5A067146E7C22DC7DE67C6138005`.
  R64 converges in three serialized XeLaTeX passes. Passes 2 and 3 are
  byte-identical, 14,919 bytes / SHA-256
  `6230FBB475D6CF03F9A964DEED356BE28FCF7710ED1CF3E794C72551F5801247`.
  The 62-page A4 PDF is 413,424 bytes / SHA-256
  `C13330C0BE44ED2750AD936DAE29E7B932818C9272FFAE96D6609C0A66E6DB36`;
  checked hard/reference/destination/missing/rerun/overfull diagnostics are
  zero.
- Only the two newly affected terminal output pages were rendered, strictly
  sequentially and one at a time, at 1,100 dpi. They were loaded only in the
  resized high-detail viewer. Physical p.61 SHA-256
  `7175724C8CB55267B7B8AEA38D0436E21BE0BE8E99D4231B5D4E92ECC0FB830A`;
  physical p.62 SHA-256
  `B7FC8C0C7FEE70149C317B4E67F3E83C3130E875E87944972CE47324E1CF0215`.
  Both pass for the §7.8 opening, p.77/p.78 seam, Hom/inverse-limit formulas,
  proposition flow, terminal induction, `(A suivre.)`, clipping, margins, and
  page envelope. No other page or image was generated.
- Build validation:
  `controls/EGA1_SECTION78_BUILD_VALIDATION_R64.json`, 3,637 bytes /
  SHA-256
  `90C7FDBCA641A9712050C2D811FC7EA8528AB46F6B84E12EDF606B1B8AE156C8`,
  status `PASS_BOUNDED_FRENCH_TEXT_BUILD_AND_TERMINAL_LAYOUT`, errors empty.
- English R11 manifest generation initially used the project root instead of
  `source/` and exited before writing output. A first replay harness then used
  culture sorting and false-failed row zero; `.NET StringComparer.Ordinal`
  corrected the harness. The final manifest replays 127/127 rows, 7,280,225
  bytes, tree SHA-256
  `D3FCAFB187DF2A812ABEB019BBE4AD50E7EB6D143CADF2C51EB357D256E95B13`.
  Manifest SHA-256
  `BFF25F76B2DD8C58A895D7722F97EF711262757CCD42257AE59807A38F4C6F61`;
  final source/diff validation SHA-256
  `F29FF0F856DFCDD9E0491398D0292769250F7C4CD312D555BE9E884A2CF2A12E`,
  errors empty. Neither failed harness mutated source or final evidence.

## 2026-08-02 — EGA I Chapter I opening, printed p.79

- The prior cursor wording “next bounded NUMDAM EGA I publication” was too
  loose. The authority remains the same 227-page NUMDAM EGA-I PDF, 31,680,717
  bytes / SHA-256
  `9ABA23020217535977E279BDD06A0413F48DA703086865BA4C00766C85DF4AE6`.
  Physical PDF p.78 is printed p.79: the Chapter I title, ten-entry Sommaire,
  and orientation paragraph. Physical p.79 is printed p.80 and begins §1,
  §1.1, paragraph 1.1.1. Cursor control:
  `controls/EGA1_CHAPTER1_OPENING_AUTHORITY_CURSOR_20260802.json`, 2,033 bytes /
  SHA-256
  `4F4D0F994859EB7FAC0268190A721D36CA37178826F01D59E7FE64F0F6440A04`.
- A filename-first evidence search found no existing p.79 authority raster.
  Exactly one grayscale whole-page authority image was therefore rendered,
  sequentially, at 1,100 dpi and viewed only in the resized viewer:
  `qa/authority_reuse/ega1_chapter1_opening/EGAI_physical078_printed079_context_1100dpi.png`,
  1,363,560 bytes / SHA-256
  `C4CFD1479D83E858F171625D2806B673CFDB4285321D726E7FE81FA14928917C`.
  It passes for the complete page. The renderer emitted display-font warnings,
  but the direct scan itself is visibly intact; those warnings were not used as
  textual evidence.
- Diplomatic source written only through the printed-p.79 boundary:
  `source/ega1/chapter1-frontmatter-fr.tex`, 2,045 bytes / SHA-256
  `DE7D2CC5ED4918280120E35DB2BF3C90CB53F08D22D5E9241E63B1C06D387EE5`.
  The only editorial operations are TeX representation: a stable chapter
  label, source page marker, ordinary French guillemet spacing, and bibliography
  keys for the printed references [1] and [9]. No French wording, claim, or
  mathematical content was corrected or normalized.
- The current English chapter front matter, `source/global_volume_ega1.tex`,
  2,709 bytes / SHA-256
  `895A6D9D4E4977802CF88EF0E108A7E5921D9EF2ECF7DCB16E99645C40B592BE`,
  was compared against the page. No unsupported source correction was found and
  no English file was changed. Exact no-op decision record: 1,356 bytes /
  SHA-256
  `5D9E76F96C0008486BD0DD83A9D963885B09431C6C64595158F5C704BD4DEE59`.
- The one-page component compiled twice, serially, with zero checked hard,
  undefined, duplicate-destination, citation, or overfull diagnostics. PDF:
  1 page / 15,400 bytes / SHA-256
  `62072018461E2FB12F20D83980A7D1F033AE4F1A08664176C747F9336D194088`.
  Exactly one output page was rendered at 1,100 dpi, 1,009,970 bytes /
  SHA-256
  `D279C067085C5FAC419853871384C597F50580FEDAE396E00FB7B15E9B00CAB8`,
  and passes for layout, visibility, and page envelope. Validation:
  `controls/EGA1_CHAPTER1_FRONTMATTER_P79_VALIDATION_R1.json`, 1,996 bytes /
  SHA-256
  `E404FE4223BC22890DC5F005A70330490535EA433E35CBFE2B6C7C6A9C498C42`,
  errors empty.
- Exact next cursor: physical PDF p.79 / printed p.80, §1 “Schémas
  affines”, §1.1 “Le spectre premier d'un anneau”, paragraph 1.1.1.
- Resource rule remains binding: zero agents are currently active; at most two
  or three agents may handle genuinely disjoint low-intensity grunt work. No
  agent rendering, OCR, build, audit, or final source/mathematical/visual
  judgment; no batch images or parallel heavy jobs.

## 2026-08-02 — EGA I Chapter I, printed p.80 / §§1.1.1--1.1.2

- The exact authority remains `EGA_I_PMIHES_1960_4.pdf`, SHA-256
  `9ABA23020217535977E279BDD06A0413F48DA703086865BA4C00766C85DF4AE6`.
  One whole-page context image was generated, sequentially, for physical PDF
  p.79 / printed p.80:
  `qa/authority_reuse/ega1_chapter1_opening/EGAI_physical079_printed080_context_1400dpi.png`,
  2,091,337 bytes / SHA-256
  `E8CD108C3EA394B7A78A88411D41255D4D2A9E385A1D582A30875E671ED35B92`.
  A single tight high-detail crop was then genuinely necessary to distinguish
  the small Fraktur prime-ideal symbol:
  `EGAI_physical079_printed080_prime_ideal_notation_5000dpi.png`,
  17,000 by 9,500 pixels / 244,563 bytes / SHA-256
  `2A3A14E01DCE2CADB22BF6797BB2184610D81BE4338D41BB49191194F43DB3BB`.
  It proves that the source prints `\mathfrak j_x`, not `\mathfrak p_x`.
- Diplomatic French through the p.80 seam is now in
  `source/ega1/ega1-1-fr.tex`, 3,639 bytes / 106 lines / SHA-256
  `1CECBFC4D2CD0D595D46B7588721C334D06050DC97B40BAAE96FFD05E4218A23`.
  It contains §1, §1.1, all of 1.1.1 and Proposition 1.1.2 with proof and the
  Zariski footnote. `chapter1-frontmatter-fr.tex` gained only a terminal
  `\clearpage` to preserve the p.79/p.80 seam and is now 2,057 bytes / SHA-256
  `7B2D0F8F812EBA3121202F0AE6415FFC6C281B8428DA8F0F72D89DF1CEC01708`.
  No printed French wording or mathematics was corrected or modernized.
- The bounded two-page reader compiled in two serialized passes with zero
  checked diagnostics. PDF:
  `qa/ega1_chapter1_build/chapter1-p79-80-check-r2.pdf`, 46,494 bytes / SHA-256
  `6F238B0D3F015C1F8791435494FEED7FC17CC0571D7401D5973C36FBC09EDF37`.
  Only output p.2 was rendered, at 1,100 dpi, and personally passed for text,
  formulas, Fraktur glyphs, footnote, margins, clipping, and seam; image
  SHA-256
  `3F20206E81D4B32625D87BB9764F3A559B95996EE8869C35B8EFAB961BAFC3DE`.
- The English comparison produced two separately justified edits in
  `source/ega1/ega1-1.tex`:
  - `EG-EGA-I-P80-111-INTEGRAL-DOMAIN-TERMINOLOGY-EN-001`: “the field of
    fractions of the integral ring” became “the fraction field of the
    integral domain.” This is the standard precise English rendering of
    `corps des fractions de l'anneau intègre`; it changes terminology, not the
    mathematical assertion.
  - `EG-EGA-I-P80-111-RELATIONS-VS-EQUATIONS-EN-001`: “the equations
    $f(x)=0$ and $f\in\mathfrak j_x$” became “the relations ...”. French
    explicitly says `les relations`, and membership is not itself an
    equation. This is a source-faithfulness and mathematical-register repair.
  The source is now 78,900 bytes / SHA-256
  `7F3A34C3E03F3497A4BD406E9E7A48ED6EDC72CCDA99768DD516EEF948202C64`.
- A third candidate is deliberately logged as a lead error caught before
  mutation: at 1,400 dpi I suspected that inherited English `\mathfrak j_x`
  should be `\mathfrak p_x`; the tight 5,000-dpi crop proved the printed glyph
  is `j`. Stable ID
  `EG-EGA-I-P80-111-JX-VS-PX-CANDIDATE-REJECTED-001`; source mutation false.
  This is one self-caught wrong source-reading suspicion in this batch and zero
  wrong edits admitted.
- The first in-memory inverse-replay harness omitted the closing math delimiter
  from its second search string and therefore reported count zero. It wrote no
  file and changed no source. The corrected two-edit inverse replay exactly
  reconstructs the 78,902-byte predecessor SHA-256
  `263C48F2E102980DB1700F57B7CAB6235CFE940656A7873F637EE3C37F8A2D02`.
  Decision ledger SHA-256
  `363742C913D367889348FD4D554B6F53B22AC1ECE859BD9FDD8F83F4F9747A3E`;
  inverse validation SHA-256
  `01CC60CDDA76790566C19EFE18399426CA9CF883765745CDA0DE89161A659D0F`.
- Complete English R12 source closure is 127 files / 7,280,223 bytes / ordinal
  tree SHA-256
  `5410571C0C44F559B1474FFFACE408BE3137F71D418FD09F22B70B798A601191`.
  Manifest SHA-256
  `491EC4E6FD5410C54986400B0CE1B975E502481537E846521CC24B7A20AA15ED`;
  complete source/diff validation SHA-256
  `3102F963D936C1A15641FF49F9CEF4D61810B8CEE1FFD259A170816A8703447D`.
  The final p.80 checkpoint validation is
  `controls/EGA1_CHAPTER1_P80_VALIDATION_R3.json`, 3,167 bytes / SHA-256
  `919E4AA8D21E17CDA058D20468F20E688696CAC1B3915AA2F59BD61D702E9A61`,
  PASS with errors empty.
- No agent, OCR, parallel job, bulk render, or global build was used. Exact next
  cursor: physical PDF p.80 / printed p.81, paragraph 1.1.3.

## 2026-08-02 — EGA I Chapter I, printed p.81 / §§1.1.3--1.1.9

- No reusable p.81 authority image existed. The first renderer call had a
  one-page selector error: it produced printed p.82 while its requested
  filename said p.81. The page was recognized before transcription and caused
  no source mutation. It was preserved without overwrite as
  `EGAI_physical081_printed082_context_1400dpi.png`, 5,254,085 bytes /
  SHA-256
  `212A6AC00972E745CF7F7C4C33D6302B050BCFAA2B0D920B738AA982E104C1DA`,
  for exact reuse at the next cursor. The corrected single p.81 render is
  8,327,112 bytes / SHA-256
  `0820B8B9E0E7AFCE9F9D6A947B379F03C39834F4FF758EE9D44A3B6B0EEB73E2`.
  No high-detail crop was needed.
- Diplomatic French p.81 adds 1.1.3--1.1.9 to
  `source/ega1/ega1-1-fr.tex`; current file is 7,710 bytes / 206 lines /
  SHA-256
  `1A3C8979F95B51594029DE4D2C3EDB3C18B3331DF38F0DEAB2F65D9ED6F101C6`.
  The page was transcribed as printed, including `fonctions continues
  numériques`, `topologie initiale`, and `Kolmogoroff`; no French correction
  or modernization was introduced.
- Three English changes were admitted and individually logged:
  `intersection` became plural `intersections`; the inherited generalized
  “any non-Noetherian integral ring” became the source-exact “the example of a
  non-Noetherian integral domain having exactly one prime ideal distinct from
  (0)”; and the missing article in “example of a ring” was restored. Two
  nonliteral but justified choices were explicitly retained: `fonctions
  continues numériques` as “continuous real functions,” and `topologie
  initiale` as “original topology” in this noncategorical context. Five-row
  decision ledger SHA-256
  `51830FA1B2D263DDBDE91380EA04B6C6028D2A6711344A6E8038AAF8A05360D6`.
  Three-edit inverse replay SHA-256
  `6C46D53DB24F27BA8BEA6474EF39D13A40196E407728F2573DA9FE87D7407E9C`,
  errors empty. No lead decision was later reversed in this page batch.
- The bounded reader compiled twice with zero checked diagnostics. PDF:
  3 pages / 54,293 bytes / SHA-256
  `5C9C3AE13B9A7B14E95D04848FCB0826B50E083865E98E0B98D5BD45B8849BEC`.
  Only affected output pp.2--3 were rendered, one at a time, at 1,100 dpi.
  They pass for the p.80/p.81 seam, carried footnote, equations, proposition
  split, all corollaries, final 1.1.9, margins, clipping, and page envelope.
- Complete English R13 is 127 files / 7,280,251 bytes / ordinal tree SHA-256
  `C73A0D59938FB18E3B9DEC6BB9E1C4BC8033360DA5C1B4F0BD948A9FCED76430`.
  Manifest SHA-256
  `CC593E9C9D01D8053CF7757DAB745197E9481FF9308DA0C3D2623F25AD7406DF`;
  complete diff validation SHA-256
  `DA38B1A6554799334D70C5C9EEFB7CF4C9615BC8041CBDBEFAEE289E8FA13030`.
  French checkpoint validation R4 is 5,558 bytes / SHA-256
  `D71C9D2A525AE7DD280BF28559573D727DE3E21FBA5C86D2A7DE0B2313B6FD92`,
  PASS/errors empty.
- Exact next cursor: physical PDF p.81 / printed p.82, Proposition 1.1.10.
  Reuse the already-rendered p.82 authority page; generate nothing new for
  context. Zero agents are active.

## 2026-08-02 — EGA I Chapter I, printed p.82 / §§1.1.10--1.1.14 seam

- The exact p.82 authority page produced by the preceding selector mistake was
  reused at SHA-256
  `212A6AC00972E745CF7F7C4C33D6302B050BCFAA2B0D920B738AA982E104C1DA`.
  No authority page or detail crop was generated for this unit.
- Diplomatic French now reaches the p.82 seam inside the proof of Corollary
  1.1.14. `source/ega1/ega1-1-fr.tex` is 11,938 bytes / 297 lines / SHA-256
  `8CFF1ED1AF6AD16875A0EB87E1C9C4DA453799BC2FD29A1AE80BEFEEE90AB4F2`.
  The printed `n\geq0`, topological-space `isomorphes`, and all uses of
  `intègre` are preserved diplomatically.
- Three English decisions were applied: inherited `n>0` was restored to the
  valid printed `n\geq0` rather than treated as a source defect; both noun
  phrases translating `anneau intègre` now use standard “integral domain.”
  “Canonically homeomorphic” and “proper closed subsets” were audited and
  retained as exact standard equivalents. Decision ledger SHA-256
  `71711DFF7E0D5C21C8F32EF5A159585B22F61D574C20BBAAA91B4CB634719421`;
  inverse validation SHA-256
  `9096728741F07D4C9DA96C703E7381E53E16FC3B5D56140B029B1AFD2B787887`.
- The first new bounded wrapper compiled the source but was held on two
  undefined Chapter 0 targets. A no-overwrite wrapper successor added only
  nonvisible bounded targets. Final PDF: 4 pages / 61,661 bytes / SHA-256
  `CBD2C0707C64BA7D38EC3EBC00422A64955B8D4013DDD96D566D48A0EE0D1E3D`,
  two passes, checked diagnostics zero. Only affected output pp.3--4 were
  rendered sequentially at 1,100 dpi and personally pass.
- The first unsealed p.82 JSONL had incorrect JSON escaping for TeX
  backslashes; one row failed and another decoded `\n` silently. It was fixed
  before admission, all five rows now parse, and no TeX source changed. A
  read-only PowerShell display harness also initially used ambiguous `$n:` and
  failed to parse; its braced rerun passed. Both tooling errors are explicit in
  validation R5 rather than hidden.
- Complete English R14: 127 files / 7,280,275 bytes / tree SHA-256
  `01613437EE956CADF50FE90C8C18CE8E73F2F731E3D1C94398C1410D12175A3D`;
  manifest SHA-256
  `27038C5278D96F411B98E72780432BC2663B4923587FECED104ADC9AEE88CE59`;
  diff validation SHA-256
  `2E42656AE40BE12F5EEA3DB21A41602A6B1C4D1C5DE798DA83B990D1AB0BE509`.
  French checkpoint validation R5 is 6,137 bytes / SHA-256
  `066BA00C2B441021C925BF8A580E73CA5E1852D41EA7CF5EBA2588275A762C53`,
  errors empty.
- Exact next cursor: physical PDF p.82 / printed p.83, continuing the proof of
  Corollary 1.1.14 after `un point générique`. Zero agents active.

## 2026-08-02 — EGA I Chapter I, printed p.83 / §§1.1.14--1.2.3

- The sole whole-page authority image is the direct NUMDAM p.83 render at
  1,400 dpi, 11,025×14,389 / 6,914,227 bytes / SHA-256
  `A4926C407030704D562AFCDDDBC60FAEF8EBFAF9F908F6AC43F93B60A3ADE4B3`.
  The existing 1,400-dpi targeted crop proves the printed reference is
  Proposition 1.1.4(ii). A second bounded 1,800-dpi crop proves the exact
  historical composition-order formula. No 5,000-dpi or bulk page set was
  generated because neither reading remained ambiguous at that scale.
- Diplomatic French now closes p.83 through the functoriality remark.
  `source/ega1/ega1-1-fr.tex` is 16,053 bytes / 403 lines / SHA-256
  `5EF98CFE63E6F1A87283D59EA419FC069D475F896510409FB99EEE8129384CD7`.
  It preserves without correction (a) the source's omitted `a≠A` in the
  Proposition 1.1.15 proof sentence and (b) its historical composition order
  `a(φ'∘φ)=aφ∘aφ'`.
- English decisions, each justified in the five-row ledger:
  - retained “at most one generic point,” because existence was proved in the
    immediately preceding clause and the Kolmogoroff step proves uniqueness;
  - retained the explicit standard name “Jacobson radical” for the printed
    radical `R(A)` used as the intersection of maximal ideals;
  - retained the necessary source-backed insertion `a≠A`: the printed
    universal assertion is false for the unit ideal, while the proof requires
    exactly the proper-ideal case;
  - repaired “it is integral” to “it is an integral domain” for `est intègre`;
  - retained the English corpus's modern right-to-left composition order,
    documenting that it expresses the same maps as EGA's historical order.
  Ledger: 5,615 bytes / SHA-256
  `D2CE7E4C7FAC883AB1F68902655472B0559C4B40ED7A9C7EC95471A8DF36E9A7`;
  inverse validation: 1,692 bytes / SHA-256
  `E6810C527CF47F6A6B8C9BFDFF047D1FDE82D97FA4BB1E4DF12395CDBD2FFFF2`.
- The bounded wrapper compiled twice with zero checked diagnostics. PDF: 4
  pages / 68,147 bytes / SHA-256
  `747BD13DB1201010DB9E89BCB40E7412C915B4ED78491287E84C2B0BFD9BFE8E`.
  Only terminal output p.4 was rendered, at 600 dpi strictly for layout rather
  than source fidelity; it personally passes seams, displays, margins,
  clipping, and page envelope.
- Complete English R15: 127 files / 7,280,285 bytes / tree SHA-256
  `B62B297758730E9DB6D10818DFD815A6BD9F7CE2BD418DECE13D6DA662D4CF0B`;
  manifest SHA-256
  `E9A16CF44BB22B03540A64BDA62F21013D7030DA0B170EC7B66A335A15588108`;
  complete diff validation SHA-256
  `05B18115426FBB140190E05B1AB7833852F3EAEBF3EDDC5A4A88909EC970DEEE`.
- Five workflow mistakes are not hidden: nonexistent pdftotext path, one-page
  locator offset, an overbroad read-only rg stopped after about 12.8 seconds,
  one crop bounding-box miss, and a repeated PowerShell `$n:` parse error.
  None changed source. Exact error ledger: 5 rows / 3,216 bytes / SHA-256
  `E22F6D1D982B447B2B17C4DFBC61F825C54BE72DD036A54B8DFFC6F1FDBBFE7F`.
- Exact next cursor: physical PDF p.83 / printed p.84, Corollary 1.2.4. Zero
  agents active; reuse existing evidence before creating any new image.

## 2026-08-02 — EGA I Chapter I, printed p.84 / §§1.2.4--1.3.3

- One grayscale 1,400-dpi whole authority page was generated because no p.84
  image existed: 10,870×14,409 / 7,821,531 bytes / SHA-256
  `B9004FDF54FBDD6BABB78C76EF3B5AB5B17332FCA12CD4EA7C412952635A5F28`.
  Two serial 1,800-dpi crops were made only for actual small ambiguities: the
  1.2.5 cross-reference and the primes in the 1.2.7 ambient objects.
- Diplomatic French now closes p.84 at Equation 1.3.3.1. Current source is
  20,132 bytes / 508 lines / SHA-256
  `02C040DC7CB2DA53E4E6F2EE710BCAF37E99CA70AFC6960A1BAEF5FADC775E5B`.
- Three English normalization/correction decisions were individually closed:
  - the source prints 1.1.12 in 1.2.5, but the arbitrary quotient-spectrum
    result is Proposition 1.1.11; English 1.1.11 is retained;
  - source notation `{}^S i_A` is systematically written `i_A^S` in English;
  - the source prints X/A/A in the proof of 1.2.7, but `Ker φ` is an ideal of
    A' and its vanishing set lies in X'=Spec(A'); English X'/A'/A' is retained.
  Ledger: 3 rows / 4,064 bytes / SHA-256
  `67464F6931246807CB6478BBA49E9384E53ECC2399F0100241B14F49D605D20F`.
  No English source byte changed, so R15 remains current; exact no-mutation
  validation: 1,978 bytes / SHA-256
  `615D7EAABBF75650F9EAFF26D8DD64475CD1615450D31ECCBD6DCC668A6B0C9F`.
- I initially primed X/A/A in the unsealed French draft because that is the
  mathematically correct reading. This was wrong for a diplomatic source
  layer. The direct 1,800-dpi crop proved the printed symbols are unprimed; all
  three were restored before compilation or checkpoint admission. The exact
  self-error record is 1,188 bytes / SHA-256
  `8DABD3C2E707C95552C5EDBA3B7B34102833E6A8F5D8CEF1D1273A8E1E83463A`.
- The bounded wrapper compiled twice with zero checked diagnostics. PDF: 5
  pages / 75,818 bytes / SHA-256
  `527FDC5FDFDF86463F8F27384F183FD697926C086984F0EC9240015C90AE7F01`.
  Only affected output pp.4--5 were rendered serially at 600 dpi for layout;
  both personally pass. Source-fidelity decisions rely on the 1,400/1,800-dpi
  authority evidence, not these layout pages.
- Checkpoint R7: 6,320 bytes / SHA-256
  `FBFA113F4CED15ABB0694A7329A6EFB0A8795E42A971D1F94BFBA42C6783572B`,
  errors empty. Exact next cursor: physical PDF p.84 / printed p.85,
  continuation of 1.3.3 after Equation 1.3.3.1. Zero agents active.

## 2026-08-02 — EGA I Chapter I, printed p.85 / §§1.3.3--1.3.5

- One 1,400-dpi whole authority page was generated because no exact p.85 image
  existed: 11,025×14,389 / 7,380,300 bytes / SHA-256
  `8DCC1C72C7A521B5D42AB803E43A48630928FC8428559634F4EFA05AE9EB952F`.
  One 2,200-dpi crop was made solely to decide the four label sides in the
  1.3.5 diagram: 6,600×4,600 / 1,225,903 bytes / SHA-256
  `FE109A8D9AC8FBC393E13A43F6D91B631422EA06E87EC4A265EC3EA79ADD06A2`.
- Diplomatic French now closes p.85 after Proposition 1.3.5 and its proof.
  Current source is 23,758 bytes / 589 lines / SHA-256
  `D48927FDFB91B3A898965E5259B2C72B8BFB317FC60D716266104A7BD465BAA0`.
- Three English decisions were individually recorded:
  - applied: moved `u_g` below the lower arrow, exactly as printed; this is a
    strict layout-fidelity repair with no mathematical effect;
  - retained: `\setmin` for the printed set-minus notation because it renders
    the same set operation with corpus-consistent spacing;
  - retained: “structure sheaf” for *faisceau structural*, with “prime
    spectrum” preserving the historical qualifier.
  Ledger: 3 rows / 3,111 bytes / SHA-256
  `5A6AEAE4C1E6445364608FB234174915345D2B54E20E7C62A7BCA66860E8537D`.
  Exact one-character inverse replay reproduces the prior English SHA-256;
  validation SHA-256
  `0E9EB76A5A19EA2F6F3A43F395F8C009D420CF15F2D804095F9CBABDEF67FF2E`.
- Two lead workflow errors are explicit rather than hidden. First, a
  nonunique patch anchor briefly placed the p.85 block after 1.1.1; the marker
  check caught it before any compile or checkpoint, and the exact block was
  moved to the true terminal cursor. Second, the first XeLaTeX command let
  MiKTeX interpret `$out` literally; that generated scratch is adverse and
  excluded. Error ledger: 2 rows / 1,821 bytes / SHA-256
  `70742BEC151219B8DC317828B53DBA3893CC79DE8E9EF22FE494F4797641604B`.
- The corrected no-overwrite build ran twice serially with zero checked
  diagnostics. PDF: 6 pages / 86,036 bytes / SHA-256
  `7BE67411894028C10EE670652D8EC183866F51F9EC98C9FC31D3B2121829BD39`.
  Only output pp.5--6 were rendered at 600 dpi for layout, and both personally
  pass. Source fidelity rests on the authority page/crop, not these renders.
- Complete English R16: 127 files / 7,280,285 bytes / tree SHA-256
  `64C5266D3BB6553B6D3B1BBC42DF136042F6A5F83AFF0262CE22DF9500E35C30`;
  manifest SHA-256
  `39D7F529579466028B44E6E6BED9CDB547B4BDC2E4EDCD85783FCF1F8D9B7A34`;
  full diff validation SHA-256
  `DEA89BB808D3E6EF8221DE87C5DCA2007A868FD66847F992F1B109008926D28C`.
- The durable resource rule now requires sequential/RAM-light execution,
  image reuse before generation, one relevant crop only when needed, and at
  most two or three disjoint low-intensity agents. Exact rule SHA-256:
  `99526B90F942BC00325F2A72E4C597CE886D433E4491D0FBC7950BCDBDA38B5E`.
  Zero agents are active. Next cursor: physical PDF p.85 / printed p.86.
- During post-validation restart-file hashing, one read-only PowerShell command
  used an invalid direct `foreach | ConvertTo-Json` form and failed at parse
  time. It changed no file. Exact append-only error record: 718 bytes /
  SHA-256
  `F101CFBBAA3A07E0FE335D1F21B2181CC3011D65E4B33C003AEFDA56E6654D73`.

## 2026-08-02 — EGA I Chapter I, printed p.86 / §§1.3.6--1.3.7

- The first authority render exposed a lead locator mistake before source work:
  I passed PDF page 86 to a one-based renderer while treating the established
  physical-page number as zero-based. The resulting image visibly has printed
  folio 87. I preserved it as adverse/mislabeled history, then rendered the
  actual PDF one-based p.85 / printed p.86 once under a no-overwrite `_r2`
  filename. The correct authority image is 10,870×14,409 / 7,630,440 bytes /
  SHA-256
  `B7BEC3BAC68ACB643C558229D88E4B17F8AB3F2AF3A9DC0BF76B145516DE8B42`.
  No detail crop was required: the 1,400-dpi page resolved every current
  formula, index, emphasis mark, and reference. The adverse printed-p.87 image
  is 7,489,613 bytes / SHA-256
  `3E861071076111EEBB9572225C6EEDBEBB3664DE47E2FEB09C605071793E9AC3`
  and is eligible for p.87 reuse only under the corrected locator.
- Diplomatic French now includes Proposition 1.3.6 and proof, Theorem 1.3.7,
  and the proof through Equation 1.3.7.2 and `On en conclut`. Current
  `source/ega1/ega1-1-fr.tex` is 27,527 bytes / 664 lines / SHA-256
  `9189ABAEC2E1599F3F03D34D8687312EA1F59A9B994A81CBCDDEB43546CDEB20`.
  The page break is intentionally retained at the source continuation point.
- A second lead mistake was caught by visual build review: the first append
  omitted the backslash before `emph` in exactly two places, visibly yielding
  `emphinjectif` and `emphsurjectif`. That build is adverse and unsealed. I
  restored both exact backslashes, verified that no bare formatting-command
  token remains, and rebuilt in `chapter1-p79-86-build-r2`. Exact workflow
  error ledger: two valid JSONL rows / 1,982 bytes / SHA-256
  `99F09937F514AE72995E15D2F82734DBE55468DA67BC6E73379874A714A7FAF3`.
- The corrected bounded build ran twice serially with zero checked hard,
  undefined-reference/citation, duplicate-destination, missing-character,
  overfull, or rerun diagnostics. PDF: seven pages / 93,397 bytes / SHA-256
  `F2800A0E48B79217DE13500AD95E6D31FF0673DF66FA35B3F9EC86BA353E1BD9`.
  Only affected output pp.6--7 were rendered at 600 dpi for layout; both were
  personally inspected and pass. These output renders do not adjudicate
  source fidelity.
- Three previously accepted English phrasings were source-inaccurate enough
  to require explicit repairs rather than silent copyediting:
  1. `homomorphism of structure rings` became `ring homomorphism`. French
     says `homomorphisme de structure d'anneau`; the inherited plural implied
     an unrelated technical object. This is terminological precision only.
  2. `the m_{ij} are equal to the one single m` became `all the m_{ij} are
     equal to the same integer m`. This restores `tous`, `entier`, and the
     common-value force of `un même`; the bound itself is unchanged.
  3. `it remains to prove the case where m=0` became `we are reduced to the
     case where m=0`. French says `on est ramené`; rescaling reduces the data,
     rather than introducing a new proposition to prove.
  All three are logged with `lead_was_wrong:true`; none changes the theorem or
  proof mathematics. Ledger: three rows / 3,316 bytes / SHA-256
  `47ADE114A1A2161E71166C2BAD84C0E2EAEB06469B1703440524A06A46B456E7`.
  Exact inverse replay uses three unique substitutions and reconstructs the
  prior 78,962-byte English SHA-256
  `87F31A92CE21021768DB10B4C1F39A51992CF9949C61205E599CBD03E2E276AC`.
- Current English `ega1-1.tex` is 78,953 bytes / SHA-256
  `26747DCB22FCB736BBD1D025015C81E268F08CE42EB14D98518E4F21EA70DD99`.
  R17 contains 127 files / 7,280,276 bytes / exact ordinal tree SHA-256
  `CE854184377B48F388C46D5D4808E0A23A2E168F23909714C7E6F9C10B880DF8`;
  manifest SHA-256
  `63BA95B4C3C9B2E7C50C5878A523D7C5D032ABBB84C5D2B09AB967E904E78674`.
  Section diff validation SHA-256 is
  `A438CD78B18CAADC9EA051A06CA04D065C74034A27A500B3A6F80384B31A697E`;
  full R17 validation SHA-256 is
  `394F541895BE2619FE30D5562F28EA01FD28AF23B923C89B79BFFB9DC89D5D70`.
- Checkpoint R9 is 8,297 bytes / SHA-256
  `3B5598B9D9CB608D84DB54E9F70E6D1572157E62E46B66F2694E2DAF0E7A20AA`,
  PASS/errors empty. Execution remained sequential and RAM-light. The hard
  cap is two or three low-intensity, disjoint grunt-work agents; zero were
  active for this page. No OCR, bulk render, or parallel build was run.
- Exact next cursor: PDF one-based p.86 / printed p.87, continuing the proof
  of Theorem 1.3.7 after `On en conclut`. Reuse the already-generated
  printed-p.87 image before considering any new render.

## 2026-08-02 — EGA I Chapter I, printed p.87 / §§1.3.7--1.3.9

- Reused the already-generated page image rather than rendering again. Its
  filename still says printed086 because it arose from the p.86 page-base
  mistake, but direct folio inspection fixes its true locator as PDF one-based
  p.86 / printed p.87. Exact image: 10,423×14,137 / 7,489,613 bytes / SHA-256
  `3E861071076111EEBB9572225C6EEDBEBB3664DE47E2FEB09C605071793E9AC3`.
- Only two source-detail crops were made, both from that existing image and
  both tied to genuine decisions. The exact-sequence crop is 392,364 bytes /
  SHA-256
  `F21EC0435F9C6AF7E38D5B867DC76CA920828981237E2155E9A3A33FD56E6DEB`;
  it proves that neither sequence has terminal punctuation. The 1.3.8 diagram
  crop is 397,587 bytes / SHA-256
  `B16C7CBE18ECFC564B58298294029CEA3837386FC4B4886255A5F89723B7822C`;
  it proves that `u` is above the upper arrow and `w` below the lower arrow,
  with the two rho labels on the outward sides of the vertical arrows.
- Diplomatic French now includes the end of Theorem 1.3.7, Corollary 1.3.8
  and proof, and Corollary 1.3.9 and proof through the last line of printed
  p.87. Current source: 31,549 bytes / 755 lines / SHA-256
  `389A015AA2E5D3C595939B9B8396320810F6A25C73128C4E6EC47F8A7F86E9D8`.
- Lead transcription mistake: the first uncompiled p.87 draft added a period
  after the second exact-sequence display. The targeted crop showed that the
  source prints neither display with terminal punctuation. I removed the mark
  before any compile, validation, or handoff. Exact one-row error ledger:
  1,247 bytes / SHA-256
  `D6710706DBB44318760D45D321459255D8375AD18C58D56E529881457AD07230`.
- The bounded wrapper adds only the two required Chapter-0 target stubs. It is
  1,927 bytes / SHA-256
  `94AD116BE06E2389B3B3AC14CE3AC6C057F0AEB0162D606BEFAB8758AD482090`.
  Two serialized XeLaTeX passes exit zero, with no checked hard, undefined,
  duplicate-destination, missing-character, overfull, or rerun diagnostics.
  PDF: seven pages / 100,645 bytes / SHA-256
  `140C8F9DC7F6A28409918FB10E0E8AD43F35C8BB57811535A6211D9BDA598FBC`.
  Only output p.7 was rendered at 600 dpi for layout; it personally passes
  content flow, diagram placement, displays, margins, clipping, and terminal
  page envelope. It is not source-fidelity evidence.
- English repair `EG-EGA-I-P87-138-DIAGRAM-W-LABEL-BELOW-EN-001`: changed
  `M_f\\ar[r]^w & N_f` to `M_f\\ar[r]_w & N_f`. The direct crop shows the
  printed `w` below the arrow. This changes only label placement, not the
  diagram's mathematical content. The prior above-arrow placement had been
  accepted by this lineage, so the row explicitly says `lead_was_wrong:true`.
  Ledger: one row / 1,277 bytes / SHA-256
  `B4BC74E1FADA4448F35488502A81EFFA0C883572581F25A3BDEFDA0483E4AB32`.
- Current English source: 78,953 bytes / SHA-256
  `8C3145A4A41947759A191809C582163EF9FB590FBE9DC92211D719F205877D49`.
  One exact inverse substitution reconstructs R17 SHA-256
  `26747DCB22FCB736BBD1D025015C81E268F08CE42EB14D98518E4F21EA70DD99`.
  Section validation: 2,722 bytes / SHA-256
  `C5F2A10806376B6DC2D528213D2D3F03221FEA1865E60AE53E8F73244FEAAC82`.
  R18 manifest: 127 files / 7,280,276 bytes / tree SHA-256
  `D2A7BC6831E8F15D10CCE2C52C0D6907937D32DFA2EC5C4BC3779B7936AAC465`;
  file SHA-256
  `2355C8043243D22BFA826AE8664D8A3563DA28C60CCB81BD35DD28ABF1D64BCE`;
  full validation SHA-256
  `0FDA5725A45AAF1C21EBA5FCF51684B5FA5E4E1ED2129F7C69AFACFF943192F5`.
- Execution remained sequential and RAM-light. No OCR or new authority-page
  render was run. Zero agents were active; the hard maximum remains two or
  three bounded low-intensity grunt workers. Next cursor: PDF one-based p.87 /
  printed p.88, continuing 1.3.9(ii) with `Enfin, si M est la somme directe...`.

## 2026-08-02 — EGA I Chapter I, printed p.88 / §§1.3.9--1.3.12

- A filename-only reuse search found no p.88 authority image. Exactly one
  grayscale 1,400-dpi page was therefore rendered: 10,462×14,273 / 7,919,506
  bytes / SHA-256
  `A0269AB9268BF48B6C3B10923F9C31737F56EA9376C6A64567E988C07DA6E67F`.
  The whole page resolved all present notation and punctuation, so no detail
  crop was made.
- Diplomatic French now covers the completion of 1.3.9(ii), the two following
  notes, 1.3.10, Corollary 1.3.11 and proof, and Corollary 1.3.12(i) through
  its terminal display on p.88. Current source: 35,477 bytes / 844 lines /
  SHA-256
  `BF5E28152E1AEE70E34819CF64A9A2CC95A2B88DAC536D8B58421D5859C91A03`.
- Two serial XeLaTeX passes exit zero with no checked hard, undefined,
  duplicate-destination, missing-character, overfull, or rerun diagnostics.
  PDF: eight pages / 106,742 bytes / SHA-256
  `10A333E18BB2466D7CCEE6C815EDC2423E4FF682DC647F0820DA5DD043571946`.
  Output pp.7--8 were rendered one at a time at 600 dpi and personally pass
  the page seam, formula placement, corollary transitions, margins, clipping,
  and terminal envelope. These renders are layout evidence only.
- English source remained unchanged. Three potentially invisible editorial
  normalizations were nevertheless logged separately: `\supertilde` is the
  established TeX spelling of the same tilde over composite module
  expressions; `\shHom` denotes the same internal sheaf-Hom printed with a
  script H; and naming Theorem 1.3.7 and Proposition 1.3.6 before the same
  targets improves linked-reader navigation without changing the citation.
  Ledger: three retained rows / 3,276 bytes / SHA-256
  `39E247CAA4BA6F67384FB4EB535D49D2B0ADB6DAC73A3975642F310D8678DE76`.
  No lead error or source mutation occurred on this page.
- English R18 remains 78,953 bytes / SHA-256
  `8C3145A4A41947759A191809C582163EF9FB590FBE9DC92211D719F205877D49`.
  No-mutation validation: 2,729 bytes / SHA-256
  `C6FF77518A41AD662643CD1F39EF4880FB311B9C88B9FD310A7A93EC76F9960D`.
  Manifest/tree remain
  `2355C8043243D22BFA826AE8664D8A3563DA28C60CCB81BD35DD28ABF1D64BCE`
  / `D2A7BC6831E8F15D10CCE2C52C0D6907937D32DFA2EC5C4BC3779B7936AAC465`.
- Checkpoint R11: 6,384 bytes / SHA-256
  `3C9CC554D618C44E72EE0FEEBBAB828DEB0245F24B0C2BF83A87CBE69940C132`,
  PASS/errors empty. No OCR or parallel heavy job ran. Zero agents were active;
  the maximum remains two or three bounded low-intensity grunt workers.
- Next cursor: PDF one-based p.88 / printed p.89, continuing the proof of
  Corollary 1.3.12(i) after the displayed canonical isomorphism.

## 2026-08-02 — EGA I Chapter I, printed p.89 / §§1.3.12--1.3.13

- A filename-only reuse search across the French and English working trees
  found no p.89 authority image. Exactly one grayscale 1,400-dpi context page
  was generated: 10,423×14,137 / 2,878,227 bytes / SHA-256
  `9F357BAF256A9D27FE9E0B1647AEB08DF134D84F990F1195D57FE21669A96179`.
  It resolved every word, formula, condition number, arrow, and label side;
  no detail crop or second source render was made.
- Diplomatic French now completes Corollary 1.3.12 and reaches the finite-type
  statement at the foot of 1.3.13. All three diagrams are native Xy-pic, with
  the lower `\varphi` and `\psi` labels below their arrows exactly as printed.
  Current source: 39,112 bytes / 930 lines / SHA-256
  `F670F2FD67371DF61A7E41A994AC94376B835158DC6EF50B7A6765D8C346F688`.
- Three inherited English deviations were repaired and individually justified:
  the invented `(a)/(b)` condition lettering was restored to the printed
  `1^\circ/2^\circ`, and the two lower horizontal map labels were moved from
  above to below their arrows. Ledger: three rows / 3,633 bytes / SHA-256
  `38712B6F457B308FD650DDD19537321207EF7D256BDCD2622535EF1BC90D99C9`.
  All three rows say `lead_was_wrong:true`; none changes mathematics.
- English R19 source is 78,948 bytes / SHA-256
  `755474860ACB423698A25393EB56CE06396F321131B7EACBBF2624478089BDC5`.
  Four exact inverse substitutions reconstruct R18 SHA-256
  `8C3145A4A41947759A191809C582163EF9FB590FBE9DC92211D719F205877D49`.
  R19 manifest: 127 files / 7,280,271 bytes / tree SHA-256
  `FD8D86B665DACA629F4FE1ED320D15EF2BFA25A751B8527905C85457C78998C7`;
  manifest SHA-256
  `8A2618EE6EB0A895A6DE54B83A30F165D901504410CCB89177047325DAA59F80`.
- Two serialized XeLaTeX passes produce a clean nine-page bounded reader:
  113,444 bytes / SHA-256
  `36CC5F5FAAFF6AD88B55DEEF9C74293A74402440AAF9793FE2B006C53440D4EC`,
  with zero checked hard, undefined, duplicate, missing, overfull, or rerun
  diagnostics. Output pp.8--9 were rendered one at a time at 600 dpi solely
  for layout and personally pass the diagrams, seam, margins, and clipping.
- Four workflow mistakes are explicit rather than hidden: two inherited label
  sides were copied into the first uncompiled French draft; the first shell
  command wrote non-adjudicative artifacts to a literal `$build` directory;
  the first wrapper lacked target stub `0.1.3.5-fr`; and a culture-aware sort
  produced a false manifest mismatch before exact ordinal replay corrected it.
  Ledger: four rows / 3,784 bytes / SHA-256
  `E31E92A826C8570A1946B064C3D046A4FB784C7E9439FB5C74B234C66DF7C030`.
  The literal `$build` subtree is preserved and excluded.
- Checkpoint R12: 7,365 bytes / SHA-256
  `C674208138DB0C5528C4B842D006FDF141C6C553E04F220859F7FAC68F9D180A`,
  PASS/errors empty. Work remained sequential and RAM-light; no OCR or
  parallel heavy job ran, and zero agents were active.
- Next cursor: PDF one-based p.89 / printed p.90, continuing 1.3.13 with
  `Si M, N sont des B-modules...`.

## 2026-08-02 — EGA I Chapter I, printed p.90 / §§1.3.13--1.4.1

- No reusable p.90 page existed, so exactly one grayscale 1,400-dpi authority
  page was generated: 10,462×14,273 / 3,276,990 bytes / SHA-256
  `5B3D64B713A7E01460F1FC4637E85FC34284C656153033BF856F0A33DAA67AFC`.
  One genuine ambiguity was resolved with one 9,000×2,200 crop derived from
  those existing pixels, not a PDF rerender: 586,622 bytes / SHA-256
  `C1D0FC9811194B519FBDFF385CD637AAAD3FE2FC33545A6978C5E671CED4C33D`.
- The crop proves the printed oddity `au faisceau associé au module
  \widetilde N, conoyau...`. Diplomatic French preserves it. The English
  retains the mathematically forced reading “the sheaf \widetilde N associated
  to the module N,” with an explicit source-typo rationale rather than a silent
  correction.
- French now completes 1.3.13 and 1.3.14 and reaches the proof that condition
  c) implies b) in Theorem 1.4.1. Exact source: 43,364 bytes / 1,010 lines /
  SHA-256
  `209E5EF26239495DC1B1540FF7EB06E9E57122770D66EC37401FCA413DFE56E9`.
  The printed `a)`, `b)`, `c)`, `d)`, `d 1)`, and `d 2)` markers and the
  section-title period are explicit in the diplomatic TeX.
- English R19 remains byte-identical at 78,948 bytes / SHA-256
  `755474860ACB423698A25393EB56CE06396F321131B7EACBBF2624478089BDC5`.
  Five individually justified retained choices cover the tilde source typo,
  idiomatic “over,” list-marker house style, reference-kind words, and TeX
  tilde/script macros. Ledger: five rows / 4,613 bytes / SHA-256
  `A5C0174B7820E383F6FA9B55FFC3D0E2C066C0B4C20CC5FBCE2D29E4DABE66C6`;
  no-mutation validation SHA-256
  `95E3671D4EB366F23D6C403B4E9D89D145D4EDBC9904CD3A218C111E142AE1F9`.
- After the final title-period edit, two serialized XeLaTeX passes produce a
  nine-page bounded PDF, 119,551 bytes / SHA-256
  `44FDD1A2620174F0A8A39FACB34F37355C09F5EB47151CD529DBB19C6015CA50`,
  with zero checked diagnostics. Only output p.9 was regenerated at 600 dpi
  for layout and personally passes.
- Three workflow issues are explicit: the first append context failed
  atomically; the first unsealed build omitted the heading period; and the
  bundled `pdfinfo.cmd` wrapper was broken, so native `pdfinfo.exe` was used
  to confirm nine pages. Ledger: three rows / 2,343 bytes / SHA-256
  `6FADE97B807D8730CF9BCEB74B374D1D9421153C1F157107FCD7CD70A020AC75`.
- Checkpoint R13: 7,030 bytes / SHA-256
  `0DCD4476C7F3170509395EAD0A9B983810A19725AC185A3D188A248FE316DF39`,
  PASS/errors empty. No OCR or parallel heavy work ran; zero agents were active.
- Next cursor: PDF one-based p.90 / printed p.91, continuing the proof of
  Theorem 1.4.1 with `Pour démontrer que b) entraîne d 1) et d 2)...`.

## 2026-08-02 — EGA I Chapter I, printed p.91 / Theorem 1.4.1

- A reuse search found no existing p.91 authority image. Exactly one grayscale
  1,400-dpi context page was generated: 10,423×13,962 / 3,431,666 bytes /
  SHA-256
  `B9AA4889898ED3D09E542ED7C34D59BFBA7F4611B4F419FC5AA4E7BD02C4D83F`.
  It resolved every word, formula, index, restriction domain, marker, and
  punctuation point. The page contains no diagram and required no crop.
- Diplomatic French now includes the one-basic-open proof of b)⇒d 1),d 2),
  Lemma 1.4.1.1 and its proof, and the start of d 1),d 2)⇒a), ending exactly
  at the printed p.92 seam `g^m t se`. The source preserves the printed
  unparenthesized markers and incomplete seam. Current source: 47,381 bytes /
  1,080 lines / SHA-256
  `9F7FE068AB53F83ADF9CF58C3692D0CACCF2A3571A26C07F3AB9C164656E2ABE`.
- The mathematical English was faithful. Two inherited prose defects were
  nevertheless real and were repaired: `To finish the proof, that...` became
  `To finish proving that...`, and `It is evident for (d1)` became `This is
  clear for (d1)`. Both rows record `lead_was_wrong:true`; formulae, targets,
  and mathematical content are unchanged.
- Four nonliteral but justified choices were retained individually: English
  parenthesizes and closes the spacing in condition markers; it supplies the
  verified words Proposition/Theorem before locators 1.3.6/1.3.7; it renders
  `il suffira` with conventional present-tense `it suffices`; and `\sh{F}` is
  the project TeX spelling of the same script sheaf symbol. The complete
  six-row ledger is 4,740 bytes / SHA-256
  `4ADAD1B6997F3B699E36BF7F95E33D6F0FA68D7483FB5D1406C73EB190612510`.
- English R20 is 78,945 bytes / SHA-256
  `776A8D8FB7B5ACA95CC45F939C8BF11E5CF45B00709BC281F9FFB007C58A86A9`.
  Two inverse substitutions reconstruct exact R19. R20 covers 127 files /
  7,280,268 bytes / ordinal tree SHA-256
  `1C39A53AA1AFE22E39606C93EADB7FBE6C0D0705AE43C35C9D6DBD345DDFE5AD`;
  manifest SHA-256
  `864B73E7553E086F64D7AD32B4DD8494823505E3956A28DBED39EFBB8EA990D5`.
- The first bounded compile used the wrong working directory and failed before
  producing a page; its r1 log is preserved/excluded. The admitted r2 build
  then ran two serial passes and produced 10 pages / 124,336 bytes / SHA-256
  `5B8761E5AEDA30ECBE6E7475A9489A6AEBCD5F895BF0372971B66286E12FCA03`,
  with zero checked diagnostics. Only output pp.9 and 10 were rendered, one at
  a time, at 600 dpi for layout; both personally pass.
- Two further workflow errors are explicit: an assumed Poppler path was absent,
  then resolved with `Get-Command`; and my first R20 replay repeated the known
  culture-aware-sort mistake before explicit ordinal replay passed. All three
  rows are 2,468 bytes / SHA-256
  `546982E90BF81244EE22F6986CDA458065D2C37621666DBFDB1274DA1744E355`.
- Checkpoint R14: 7,885 bytes / SHA-256
  `E48DC2814D020CA3C9EA06719BE864354A2276D533C6505DC5BDD978A11266C1`,
  PASS/errors empty. Work stayed sequential/RAM-light; no OCR, render swarm,
  parallel heavy process, or agent ran.
- Next cursor: PDF one-based p.91 / printed p.92, continuing immediately after
  `g^m t se`.

## 2026-08-02 — EGA I Chapter I, printed p.92 / §§1.4.1--1.5.1

- No reusable p.92 image existed. One grayscale 1,100-dpi authority page was
  generated: 8,266×11,184 / 6,642,775 bytes / SHA-256
  `57FCD19DD19BCF8D20CC7AC5F64F7981D794DF3854DB4EAEE27B3538574DCD85`.
  It resolved the entire page, including emphasis and inline arrow placement;
  no detail crop or diagram review was needed.
- Diplomatic French completes Theorem 1.4.1 with its literal `C.Q.F.D.`, adds
  Corollaries 1.4.2 and 1.4.3 and the latter's proof, then records the 1.5 title
  and Theorem 1.5.1. `noethérien` retains the source's internal emphasis, and
  the $M\to M_f\xrightarrow{u_f}\Gamma$ factorization remains inline.
  Current source: 51,644 bytes / 1,164 lines / SHA-256
  `B5E58A9430A49E9A19C0B792A1B4F41549A5092AFB8000BA8CE023C1AC4D264B`.
- English line 767 now repeats `from` after `as well as`, matching French
  `ainsi que de`. Line 768 now attaches `in the same way` to the concluding
  step rather than incorrectly to the showing step. Both are source-alignment
  repairs with `lead_was_wrong:true`; formulas and targets are unchanged.
- Seven retained choices are individually justified: proof-environment marker
  for `C.Q.F.D.`, list-marker house style, verified reference-kind words,
  English heading idiom/punctuation, common-noun capitalization for module and
  algebra, logical-present proof tense, and English eponym capitalization in
  `Noetherian`. Complete ledger: nine rows / 6,778 bytes / SHA-256
  `A12D4F80F39AD47269CA79400EBE3B8CCF5DE8C11FE5D21BE85B665A45722A89`.
- English R21 is 78,943 bytes / SHA-256
  `E79237CB465C8F0EF7C3FE573F568C4FCD122DC5D618463C46B914DE218459F9`.
  Two inverse substitutions reproduce exact R20. R21 covers 127 files /
  7,280,266 bytes / tree SHA-256
  `870E97EB71F44AA795F47332B655738011DB772C226899E1FFDE66A3741A4B82`;
  manifest SHA-256
  `DA77D11422EEB0CD94709729824171B1D9B33A1C7B71E5BBE68C9CAF9679717A`.
- The r1 wrapper omitted external target `0.3.2.5-fr`; its two-pass PDF remains
  adverse/unsealed. The no-overwrite r2 wrapper adds exactly that target and
  produces 10 pages / 129,151 bytes / SHA-256
  `393E1FBD1AC8C7A93A7D23FEB7E0F283666A0041D2623C58C03C686EB0407E74`
  with zero checked diagnostics.
- Page 9's old/new PDF content streams are byte-identical under SHA-256
  `AAE4F927574B1AE392E185D2C25F28125B68758AB4BCA6E902FE71E4D2AD1A76`,
  so its existing render was reused. Only page 10 was rendered at 600 dpi;
  it personally passes the seam, proof close, corollaries, section transition,
  theorem statement, margins, and clipping.
- Four caught errors are explicit: unhandled no-match exit status; initially
  displayed rather than inline factorization; initially omitted internal
  emphasis on `noethérien`; and the r1 wrapper's missing target. Ledger:
  four rows / 2,689 bytes / SHA-256
  `ED85AD247BE5BFDC21A0BDF46B9465BE2A45CB82ED13DA4619EE5AD3891151CB`.
- Checkpoint R15: 8,540 bytes / SHA-256
  `051E8D04A57A6094FA52E94B1061E774331FB691A3FD62B95125C29A1E0EFD7C`,
  PASS/errors empty. No OCR, parallel heavy work, or agent ran.
- Next cursor: PDF one-based p.92 / printed p.93, proof of Theorem 1.5.1.

## 2026-08-02 — EGA I Chapter I, printed p.93 / §§1.5.1--1.6.1

- A reuse search found no existing p.93 authority image. Exactly one grayscale
  1,100-dpi context page was generated: 8,189×10,970 / 5,464,710 bytes /
  SHA-256
  `274B90A70A72E0812131425C82664C9F47D82F66C1E1A821B574AA67C183C8F0`.
  The complete page was personally inspected at original rendered detail. It
  contains no diagram, and all prose, formulas, indices, maps, emphasis,
  references, and punctuation were legible without a crop.
- Diplomatic French completes the proof of Theorem 1.5.1, records Corollaries
  1.5.2--1.5.4 and the proof of 1.5.4, opens §1.6, and transcribes paragraph
  1.6.1 through its terminal displayed ring homomorphism on p.93. Paragraph
  1.6.1 continues on p.94, so the source correctly leaves its semantic
  environment open; only the bounded QA wrapper temporarily closes it.
  Current French source: 55,165 bytes / 1,253 lines / SHA-256
  `94FAA233686C9C44B8B492C7F772DAB3CC70D2F8BC0B5DCB047ECB758B2BC4ED`.
- Three inherited English prose/register errors were repaired and are recorded
  individually with `lead_was_wrong:true`: `remarquons déjà` now reads `first
  note` rather than the unsupported `we have previously seen`; singular
  $M_\lambda$ now `ranges over` rather than `run over`; and the ordered ring
  identifications now place `respectively` naturally and remove a doubled
  space. Formulae, objects, and reference targets are unchanged.
- Six retained choices are also individually justified: parenthesized logical
  markers; English eponym capitalization; proof-environment closure;
  corollary/reference reader structure; English heading idiom and punctuation;
  and visible-equivalent project TeX macros. The nine-row decision ledger is
  7,782 bytes / SHA-256
  `211B3C3A460DB008F6E01ECE0D6444448053525A42A816B86069515D7F63D54E`.
- English R22 is 78,920 bytes / SHA-256
  `08B58F1484E0195D637512C27528BF77F665DCE03D1B3C4F29A7FC685A956E5E`.
  Three inverse substitutions reproduce exact R21. R22 covers 127 files /
  7,280,243 bytes / ordinal tree SHA-256
  `4B01E8D9D30053F942E2570915BB92365BC754DA5A95ABA6C0AB8BA2DF9329B3`;
  manifest SHA-256
  `4B2C325B73D8DCF3027A5A6BE0FEB651AD6477200E71E33916E91399CD9262F8`.
  Exact section/full validations have SHA-256 values
  `92DAB4E502B3D03E863F764B026301016E17CFDE769DD29C5E9E9C1E5D745B0F`
  and
  `24D47EAD70C2AC404F7F85D0C1DCA7D9962291579B58785897855ECE91A71276`,
  both PASS/errors empty.
- The bounded wrapper supplies only two new external target stubs and a
  wrapper-only closing delimiter. Two serial XeLaTeX passes produced 11 pages
  / 134,806 bytes / SHA-256
  `6060F18A680F8F34A33E298FB2573A8A842AA0171022114C9A5E23944487B84D`
  with zero checked diagnostics. Pages 1--9 are content-stream-identical to
  the prior build. Only changed pages 10 and 11 were rendered, sequentially,
  at 600 dpi for layout; both personally pass without clipping or overlap.
- No new drafting, wrapper, rendering, build, manifest, or replay mistake was
  found in this unit. No OCR, agent, parallel heavy job, bulk render, or
  unnecessary high-resolution crop ran.
- Checkpoint R16: 8,061 bytes / SHA-256
  `6637A091AE9F1BEFC60E1E0365E3422DF2DBFBD2ED901DC079322861F23A90F0`,
  PASS/errors empty.
- Next cursor: PDF one-based p.93 / printed p.94, continuing paragraph 1.6.1
  with `En outre, ces homomorphismes satisfont...`.
