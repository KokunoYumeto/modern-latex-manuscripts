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
