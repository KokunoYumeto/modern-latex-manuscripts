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
  `[PRIVATE_DOWNLOAD_ROOT]\EGA\ryankeleti_ega\fr\ega1\intro-fr.tex`,
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
  `03_projects/language_management/english_germanic/03_working_translations/EGA_English_Global_0_IV_french_recheck_source_successor_20260802_r1`.
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

## 2026-08-02 — EGA I printed p.94 diplomatic French and English recheck

- Reuse search found no existing p.94 authority witness. Exactly one
  1,100-dpi whole-page context image was generated, then personally inspected
  at original detail. It was sufficient for every formula, fraction,
  sheafification mark, reference, and every node/edge of the compatibility
  square; no detail crop was generated.
- The diplomatic French source now reaches 58,853 bytes / 1,336 lines /
  SHA-256
  `E0F4EA3D4AC371A160550ADE7BA8B04A3EC42D6E633DB53CBA834F3CBCDE35C6`.
  The p.94 addition closes paragraph 1.6.1, preserves Example 1.6.2 and
  Proposition 1.6.3 with proof, and stops exactly after the incomplete word
  group introducing the isomorphism continued on p.95. Its one diagram is
  native Xy-pic; active raster count is zero.
- Two inherited English decisions were wrong and were repaired individually:
  `Pour abréger` now uses the concise mathematical transition `For brevity`
  rather than the inherited nominal circumlocution, and `de façon précise`
  now becomes `More precisely`, with idiomatic `may be regarded as` for
  `peut être considéré comme`. Both changes preserve the same modules,
  homomorphism, restriction of scalars, and functoriality.
- Six retained English choices are separately justified: exact native-square
  structure; historical hash versus modern mathematical sharp glyph;
  lowercasing common mathematical nouns; semantic reader environments;
  visible-equivalent tilde/isomorphism macros; and punctuation plus clickable
  reference normalization. Ledger: eight rows / 6,931 bytes / SHA-256
  `DCCDA3F1B7B9DB60D19903ED0EE20E24B4E88A369FE2D63EA206E5B78EAF32C7`.
- English R23 is 78,882 bytes / SHA-256
  `3839AC1B392AA3B7629B06909D1DAC19AF652963B01D556D1889B1C9ECAB8414`.
  Two exact inverse substitutions reproduce R22 byte-for-byte. R23 covers
  127 files / 7,280,205 bytes / ordinal tree SHA-256
  `BB9926BFC40EB87CF106CDDACDDB834F99FF4B78CE99E0C3C3F8F32D638B5419`;
  manifest SHA-256
  `3D744079A8F05F4526BD2446B6636D487D2D258B93722F1861D810BF6408D06A`.
  Exact section/full validations have SHA-256 values
  `2E02BFF6F5B0725B629A7CA4E98B8C22CA49A1F4440627BCD62D2DC8DD906089`
  and
  `6D474E302F830412894BC3A394E631ED5A78BC220FFEBCD2DF45080A0BC7E2BC`,
  both PASS/errors empty.
- The first bounded wrapper was correctly rejected because it duplicated an
  inherited target stub. The no-overwrite r2 wrapper removes only that stub;
  two serial XeLaTeX passes produced 12 pages / 140,464 bytes / SHA-256
  `C70DC227F37A613D4667A67135F71DE49A8E3F72D4975988A8DAB1EB8A9793B5`
  with zero checked diagnostics. Pages 1--10 are content-stream-identical to
  the p.93 predecessor. Only pages 11--12 were rendered at 600 dpi for layout;
  both personally pass, including the native square and page seam.
- Four lead workflow/documentation errors are append-only and explicit:
  duplicate wrapper target; an invalid read-only PowerShell pipeline; an
  unescaped TeX backslash in draft JSONL; and stale draft English line
  locators. The latter two were found by parser/source replay before evidence
  admission. Ledger: four rows / 3,194 bytes / SHA-256
  `AAD7CED994CE3BA26B35A526C048596F974A659C0215F2F39E58AB195CC8A7FA`.
- No OCR, agent, parallel heavy job, bulk render, or unnecessary high-detail
  crop ran. Checkpoint R17: 9,196 bytes / SHA-256
  `87CAAA52DFC8971F4B0374D8040A7F5E67BE4A01974904A954F84F8D00610EB1`,
  PASS/errors empty.
- Next cursor: PDF one-based p.94 / printed p.95, continuing the canonical
  functorial isomorphism introduced by the final incomplete phrase on p.94.

## 2026-08-02 — EGA I printed p.95 diplomatic French and English recheck

- After reuse search, exactly one 1,100-dpi authority page was generated and
  personally inspected at original detail. The full page was sufficient to
  resolve every prime, subscript, tensor base, localization exponent,
  sheafification mark, arrow, reference, and equation; no crop or OCR was
  generated.
- Diplomatic French now reaches 63,197 bytes / 1,432 lines / SHA-256
  `B8C18DA8E3661EADD85EAE0FBC8A99779A1CD59285855FF2FCF5C54981265238`.
  The page closes the p.94 sentence, includes Corollary 1.6.4, Proposition
  1.6.5 and equation 1.6.5.1, the algebra/module consequence, Corollary 1.6.6,
  and opens paragraph 1.6.7 through its exact comma seam. The environment is
  deliberately left open because the sentence continues on p.96.
- The English audit repaired seven inherited decisions:
  - two literal French constructions in line 922 (`On en déduit` and `en
    vertu de`) now use grammatical mathematical English;
  - the inverted `Il correspond` sentence now has natural English word order;
  - two separate `respectivement` instances now use normal English placement;
  - the unsupported past perfect for `on a prouvé` is now simple past;
  - most importantly, `h_x(s_x' tensor t_x)` is corrected to the source-exact
    `h_x(s'_{x'} tensor t_x)`: the section on (X') is evaluated at (x'),
    not at (x). This is logged as a mathematical formula repair and as a
    prior lead error, not hidden as typography.
- A separate applied row changes three prime/subscript TeX orders to match the
  source base symbol before the index. The visible mathematics is unchanged,
  but the normalized source is less liable to machine or human misparsing.
  Six further retained choices are justified: stalk terminology for `fibre`;
  hash-to-sharp notation; English capitalization; semantic reader
  environments; visible-equivalent tilde/isomorphism macros; and the visible
  but not-yet-linked locator `0, 4.4.3.2`, explicitly queued for the stabilized
  cumulative reference/pre-Stacks pass.
- Decision ledger: fourteen rows / 11,105 bytes / SHA-256
  `905745E09BAC102CE4B799081490DB9647AE28D5BE0AE3707D6BECFB4C85BD8D`.
  Seven rows say `lead_was_wrong:true`; one is the mathematical stalk-index
  repair. Current English: 78,891 bytes / 1,266 lines / SHA-256
  `3C1A38B22A9A07315A8CFA2E8F3AC1B65232E0CFCE3F9F8E2E09A30464018617`.
- Eight exact inverse substitutions reproduce R23 byte-for-byte. R24 covers
  127 files / 7,280,214 bytes / ordinal tree SHA-256
  `099CD37D1BD2E8380DF875A90C61895F7B7BFF743573A4CF5452B22D3AEE5A56`;
  manifest SHA-256
  `EBA2F1067D485CCD4861EAFEC7F1239C55CA5858E1734714FA91667805E37E3E`.
  Section/full validation SHA-256 values are
  `865A67A3ADAAE8D2C380E5087200BE4E904E9F9699600DB16182BBA7485EAFF0`
  and
  `D53AED014E05339D9BB7106A60D15CC150C257325A6B9A6D93350D729980AA0A`,
  both PASS/errors empty.
- The first wrapper build correctly fail-closed because paragraph 1.6.7 was
  open at end of source. The no-overwrite r2 wrapper adds only the temporary
  closing delimiter and three bounded external targets. Two serialized passes
  produced 12 pages / 145,648 bytes / SHA-256
  `D6F9892A0FBFBFFD6EFC135A29191E0EFA4C69494A2670C5A4A961EFCEC3536C`
  with zero checked diagnostics. Pages 1--11 are content-stream-identical to
  the p.94 predecessor. Only page 12 was rendered at 600 dpi for layout and
  personally passes.
- The two-row workflow ledger preserves the omitted wrapper closure as a lead
  error and the nonfatal authority renderer font-lookup warnings as a verified
  warning; SHA-256
  `0E04DD82A9C4BB0DA0F4F1B60A0E0161102FC0627B37FEDE7CC0A9600702EBC0`.
  No agent, parallel heavy job, bulk render, redundant render, or OCR ran.
- Checkpoint R18: 9,167 bytes / SHA-256
  `7AC4DC5BDC566DF19569AF0EFCD14E1429C6A3A61A042B32895AD1A19AF3CC41`,
  PASS/errors empty. Next cursor: PDF one-based p.95 / printed p.96,
  continuing paragraph 1.6.7 after the terminal comma.

## 2026-08-02 — EGA I printed p.96 diplomatic French and English recheck

- Reused the already generated NUMDAM authority image
  `qa/authority_reuse/ega1_chapter1_opening/EGAI_pdfonebased095_printed096_context_1100dpi.png`
  (8144x11230, 5,353,679 bytes, SHA-256
  `D95EA237831E67C943B0A7F03E805D41E7CE6218D6D7F5250B03C261CBECA6BC`).
  I inspected that one image at original detail. No crop, OCR, agent, or
  alternative render was needed for source judgment.
- Transcribed the completion of 1.6.7, paragraphs 1.6.8--1.6.10, the §1.7
  heading, Definition 1.7.1, paragraph 1.7.2, and the complete statement of
  Theorem 1.7.3. The proof is not anticipated; it begins at printed p.97.
  Current French source: 68,010 bytes / 1,548 lines / SHA-256
  `9EAF6027F10D1EC54DC1779FC4C83785950447EE4E9DC8C5A1B3F2454EB672F2`.
- Source decisions are explicit in eight JSONL rows / 3,583 bytes / SHA-256
  `9B3F9948724B518DB513537ED3932E51B23475A85946DD01B4A24BC23280AD4D`.
  In particular: the ideal is fraktur J-prime while M is the plain A-module;
  the sheaf tildes are not promoted into the declaration; all four functor
  composition orders were read directly; and the source's convention-sensitive
  functor wording is retained rather than silently corrected. No source typo
  or mathematical defect was claimed on this page.
- English comparison found no mathematical mismatch or wrong earlier lead
  correction. Two inherited nonmathematical fidelity issues were repaired:
  the Chapter 0 citations 4.4.3 and 3.5.4.4 now share the source's one
  parenthesis and are both linked, and `when no confusion results` follows the
  French exactly. The translator note on Theorem 1.7.3 remains visibly marked
  and is justified as an errata-navigation aid. Ten decision rows / 4,144
  bytes / SHA-256
  `69FEE7A8EE3B705A6ABE2F53A66B72969CBFD7B110C4BF9DB89386A3B045842C`.
  Current English source: 78,908 bytes / SHA-256
  `758885F9505A72DF1A5A2EF8B116D998A41D0505571AD8E7028C438EE5795C6E`.
  Two inverse substitutions reproduce exact R24.
- R25 source manifest: 127 rows / 7,280,231 bytes / SHA-256
  `516696896ADBB097947CC00005B37C890C505AE9DB1D5B17EC688E0F8E7A475B`;
  ordinal tree SHA-256
  `8D3BF2A908E654E4B94AC1FFE2BEF606BF4EE92FDCEB400AAC02B737E1D51E4E`.
  Section/full validation SHA-256 values are
  `25124EBCA38FF5C5583ED1B85D1D3FD19DF40AD5EE4C740ED4D0804262FA091F`
  and
  `C748F5AD369E150BC8BFCFDE9E870AC2C7CFD914FE4A72032FE9DEE4F04BA945`,
  both PASS/errors empty.
- The first two-pass build command reused the known unsafe native-argument
  form `-output-directory=$out`; MiKTeX consequently wrote into the literal
  adverse `$out` subtree. No source changed. I preserved those artifacts and
  reran with the complete argument explicitly interpolated into a no-overwrite
  r2 directory. This is recorded as a workflow error rather than hidden.
- The dependency-runtime `pdftoppm.cmd` wrapper then failed twice with exit 3
  before producing any image. I used the installed `pdftocairo` once for the
  same single final output page. The admitted build is 13 pages / 152,080 bytes
  / SHA-256
  `013E31E9AC94D2153113C9EDC619DB8C8DBF2C33A35597F7F78FADAECB8BC159`,
  zero checked diagnostics. The only new output layout image is page 13 at
  600 dpi, 1,293,420 bytes / SHA-256
  `52B191A229C31CA6CAC2DEE3745EB7351B777F2141161A11AC7AAAA92A19A1D0`,
  personally PASS for clipping, overlap, spacing, and formula placement.
- Workflow ledger: two rows / 1,522 bytes / SHA-256
  `78F2BD3A94168E18E121212CC7DD2DF2C860D4E8E07D8E7C45FC216CD8A4FD61`.
  Checkpoint R19: 7,085 bytes / SHA-256
  `39B3AEC1B4BEF0DA99558F20D0CEF0AA030115F84C1AD024152F8A86122E4E72`,
  PASS/errors empty. Next cursor: PDF one-based p.96 / printed p.97, proof of
  Theorem 1.7.3.

## 2026-08-02 — EGA I printed p.97 diplomatic French and English recheck

- Reuse search found no existing p.97 authority image, so I generated exactly
  one direct NUMDAM page at 1,100 dpi:
  `qa/authority_reuse/ega1_chapter1_opening/EGAI_pdfonebased096_printed097_context_1100dpi.png`,
  8,296×11,107 / 5,490,961 bytes / SHA-256
  `F3033D317BF871AF491AE5E472DE64ECDF86D0ECDA79F9007800B7C977FB9AB0`.
  I inspected the complete page at original detail. The theorem-proof formulas,
  residue-field subscripts, four square nodes, four arrows and labels,
  corollaries, and section seam were all unambiguous. No crop or OCR was made.
- I transcribed the proof of Theorem 1.7.3, its native commutative square, the
  unnumbered definition of morphism of affine schemes, Corollaries 1.7.4 and
  1.7.5 with their consequences/proof, and the beginning of §2 through
  Definition 2.1.2. The page crosses a deliberate source boundary:
  `ega1-1-fr.tex` ends after 1.7.5 and `ega1-2-fr.tex` begins with §2. This
  preserves the printed source order while leaving the separately published
  errata-added §1.8 to be handled explicitly rather than silently interposed.
  Exact French identities are 71,381 bytes / SHA-256
  `D201398091BCC065BE7B5EFC610183E1E2071E01BC8E35C0CE1441DF3E579393`
  and 607 bytes / SHA-256
  `48DF1C2DA45FFC15BED36D50E53AE21B9819B64758A3ACE3D0A7B306FC4F282B`.
- The square is native `xymatrix`, not a raster, and is bound to stable target
  `I.1.7.3.diagram-fr`. Its exact topology and labels follow the authority;
  nothing was normalized beyond TeX encoding. Nine French decision rows /
  4,154 bytes / SHA-256
  `C26F809FDAB1E8AB820C76F874061C5777E6D0648F0FAA26EF9396B04ED6EB9C`
  justify each unit, the file seam, and the zero-correction disposition.
- English source comparison found no mathematical or diagram error and did not
  validate any new authorial defect. I made two local prose repairs only:
  `The hypotheses ... mean` became grammatically exact singular `The
  hypothesis ... means`, and `and we now write` became `equivalently` because
  the French `c'est-à-dire` states equivalence. Neither changes mathematics.
  Ten decision rows / 3,871 bytes / SHA-256
  `0CA4E32D47D13CBABB1993F7B3F8498A1B9F6152F6EEF28EC7A280811740E06A`;
  applied mathematical repairs zero, lead errors zero, reversals zero. Two
  inverse substitutions reproduce exact R25 source.
- R26 manifest is 29,675 bytes / SHA-256
  `A28F89369E461D3B434C5F66F51299B462AB9CE4F457ACA952B94551CDBE4147`;
  its 127 rows / 7,280,229 bytes replay to ordinal tree SHA-256
  `F6706D38DCA72AE5A01C4999F52056424809462990F8136C8042D6DE4108210E`.
  Exact section/full validation SHA-256 values are
  `B5AA88938FE6ADB0D44B3A0C41DAEA8EFFAD407B28FE783C3C6EA2BF9A5E54EE`
  and
  `64E386E2F1EA05F1D41B7E8AA4EA42B786CF7B5DB9BA9F10127B744588874976`,
  both PASS/errors empty.
- Two serialized XeLaTeX passes produced 14 pages / 157,916 bytes / SHA-256
  `8564A2C082E637A33B5FEE69D8C18FD54585EDF32832AE51948182EAD2AB4DE6`
  with zero checked diagnostics. I rendered only compiled page 13 at 600 dpi
  for layout—not source adjudication—and personally passed the dense proof,
  diagram, page marker, and Corollary 1.7.4. Page 14 was text-extracted only.
- The dependency `pdfinfo` wrapper and first console text print failed; the
  latter was rerun read-only with ASCII escaping. Nonfatal `pdftocairo` legacy
  font warnings were accepted only after the page image was complete. These
  are preserved in two workflow rows / 1,091 bytes / SHA-256
  `D319BE5C1632E2F9AC9B34241ED14366661B865F9BE7A5B9C7D62FEECAEC5227`.
  No source or mathematical effect occurred, and no redundant render followed.
- Checkpoint R20 is 7,273 bytes / SHA-256
  `BF4FD925BA25D4F5572F6B5186BF608A834A0B036BA95717DE74BDD63A275B78`,
  PASS/errors empty. No agent or parallel heavy process ran. Next cursor is
  printed p.98, Proposition 2.1.3.

## 2026-08-02 — EGA I printed p.98 diplomatic French and English recheck

- Reuse search found no p.98 evidence, so I created one and only one direct
  NUMDAM page at 1,100 dpi: 8,144×11,230 / 5,258,418 bytes / SHA-256
  `0B21F79E1BD1E8CDBDB62B647C7B5F01A787AA0D8CD5A7A362AC069E68CD98D4`.
  I inspected it at original detail. This page has no diagram; every formula,
  closure bar, subscript, sharp sign, and locator was legible without a crop.
- Transcribed Propositions 2.1.3--2.1.5 and their unlabeled explanatory
  paragraphs, 2.1.6, Proposition 2.1.7 and its unlabeled paragraph, 2.1.8,
  and the §2.2 heading through complete Definition 2.2.1. Current French is
  4,664 bytes / 114 lines / SHA-256
  `9C52B942A2B935B4201B021491D30EAD82748622FD4696D8909A6D5BEC16CC2B`.
- NUMDAM prints `L'unicité du point générique de X` in the proof of 2.1.5.
  The proposition and preceding sentence concern the closed irreducible set
  $Y$, so this is an apparent authorial typo. I preserved $X$ in diplomatic
  French. The English already reads $Y$ and carries an immediate translator
  note quoting the French; direct recheck confirms that correction rather than
  inventing a new one.
- The first bounded compile caught my own structural mistake: I had wrapped
  four source paragraphs in `proof` environments. NUMDAM prints no proof
  headings there, so even defining the environment would have altered the
  authorial presentation. I removed all four wrappers, leaving the words and
  mathematics unchanged, and preserved the r1 build/log as adverse history.
  This is explicitly counted as one lead error repaired before admission.
- The no-overwrite r2 wrapper/build passed two serialized XeLaTeX passes with
  zero checked diagnostics. PDF: 14 pages / 162,529 bytes / SHA-256
  `6908050489FFA9A1200F421B3DF0A4165489A0DD05D9B933C6891383EFEE201D`;
  log SHA-256
  `DC9599E5E68E8DCF153A6F4DDFE1B4F02DFBF966C69E41BFD7126099F14FB583`.
  Pages 1--13 are content-stream-identical to the admitted p.97 build. Only
  page 14 changed and was rendered once at 600 dpi for compiled layout;
  SHA-256
  `27191483F30CACDA90F3384C5F9C6046D303E88FFDFF232F4E97545A0F2F772D`,
  personally PASS with no overlap, clipping, crowding, or added proof heading.
- French ledger: nine rows / 4,545 bytes / SHA-256
  `2CFE6171523633BD8730600BD3B513C4D81D7AD1F524B126F47A8934C66086F2`.
  Workflow ledger: four rows / 2,435 bytes / SHA-256
  `277D15AD1B8EB5C8BE181B18110B441F71BA75A28AA1F6774D435995213F5BDF`.
  Besides the wrapper error, it preserves nonfatal authority-font warnings,
  the broken `pdfinfo` wrapper, and a false PowerShell culture-sort manifest
  mismatch corrected by an exact ordinal replay. None changed mathematics.
- English comparison applied two prose-only repairs on line 27: remove
  unsupported `some` from the existential and replace colloquial `contained
  inside` with mathematical `contained in`. All other p.98 content is retained
  source-faithfully, including the disclosed $X\to Y$ source-typo correction.
  English decision ledger: nine rows / 4,042 bytes / SHA-256
  `B1F157AC5909DD65497B34C67BA44A17E2362869C92402548E99A8E3F579C323`.
  Current English: 25,214 bytes / SHA-256
  `9239F37777A793E4A03AFEDCD0479AD55C7D90EC6A92886B20E20F80A031BA18`.
  Two inverse substitutions reproduce exact R26; no new mathematical repair,
  English lead error, or reversal occurred.
- R27 manifest: 127 rows / 7,280,220 bytes / SHA-256
  `1EBEC66D050557D5F20B1EF42B1CF8F3A7717D59ACD2CFDB3384604E0DDD5419`;
  ordinal tree SHA-256
  `07D146DDD043D20E0D30F09612E645F86A14000E974FE9C44703B6B0D35E239A`.
  Section/full validation SHA-256 values are
  `848CB0B5D0C789952E7E7B74D76C69C033BF6158A889ED33237323C8D8C9ADBA`
  and
  `804FF9CD84297A0C20B4AA027BED4EF42F54371CEA69E0B18FB18DE5D64D663F`,
  both PASS/errors empty. Checkpoint R21 SHA-256 is
  `F8E4DEBF91B6A76F697893324F32EA5E1A1678623B3845E34061F10D88C78D34`.
  Zero agents or parallel heavy jobs ran. Next cursor is printed p.99,
  paragraph 2.2.2.

## 2026-08-02 — EGA I printed p.99 / exact diplomatic and English decisions

- Reused the existing direct-authority image
  `qa/authority_reuse/ega1_chapter1_opening/EGAI_pdfonebased098_printed099_context_1100dpi.png`
  (8,220×11,077 / 5,721,373 bytes / SHA-256
  `446A4BFC0958E1210B5BD21E0F3753A15944D73AF676C1E621AD1522ED784BE1`).
  The lead inspected it at original detail. No additional image, crop, OCR,
  agent, or parallel job was needed. This implements the standing reuse-first,
  sequential, RAM-light rule rather than regenerating page imagery.
- Added the complete French page: the consequence about residue fields,
  paragraph 2.2.2, Example 2.2.3, Proposition 2.2.4 with proof and equation
  2.2.4.1, and the first line of Proposition 2.2.5. The exact page seam is
  after `Il existe alors une`; leaving the proposition environment open is
  intentional and source-faithful. The bounded QA wrapper closes it only after
  the input so the partial reader can compile.
- Preserved the authority's punctuation exactly at equation 2.2.4.1: there is
  no period inside or immediately after the display. No French source typo or
  source-backed correction was found. No diagram or raster occurs.
- French source is 9,213 bytes / 206 lines / SHA-256
  `80084D747F88429A8770AC0918B7B07ED8631D1FACCC6619661BCD95EA157A33`.
  The nine-row decision ledger is 3,925 bytes / SHA-256
  `99A0E92FA8B8B4A2CF917CFBB0DD287D1785E360DD827CD33D52CFF99E119DD7`.
- Rechecked the corresponding English source against the page and made four
  individually reversible prose/register repairs. `gives us a monomorphism`
  became `therefore gives a monomorphism` because the French marks the logical
  consequence (`donc`); `since it is given by the formula` became `as follows
  from the formula` because the formula supplies the inference, not the
  antecedent; `contained inside` became the standard mathematical `contained
  in`; and `so, with the equation` became `hence, by the relations` because
  the cited displayed equalities are the reason for the conclusion. None
  changes a symbol, hypothesis, conclusion, or source claim.
- English source is 25,214 bytes / SHA-256
  `C2C52F7F7543ABEC2A082C294123434E07FFA64E57181A879C033850C8E7DCBC`.
  The nine-row English ledger is 4,121 bytes / SHA-256
  `2198C5F835E8539CA737193AD32E41F58E4F47E1CF66AD20A9EAC1842DDD8251`.
  Four inverse substitutions reproduce R27 exactly. New mathematical/source
  repairs zero; lead errors zero; reversals zero.
- R28 binds 127 files / 7,280,220 bytes; manifest SHA-256
  `6E3AE6380AA300004627DEF42A1ECFEFEC6326C8887C525A9930A50623CF5B3C`,
  ordinal tree SHA-256
  `4C32D118D81AC1B2E89A5AEC33FD0C355B98DD2D509235A64C7A01D274280D01`.
  Section/full validation SHA-256 values are
  `063C3EFAA094A4A9C31494D2815F750CD1BED12BB8043C045BD330C0E78F13CF`
  and
  `B2FDF41EE8C27785E81EAAE0EA8050FA5049FDD9B0B7B1B3175F97FEC46B13FF`,
  both PASS/errors empty.
- The two-pass bounded build is 15 pages / 168,076 bytes / SHA-256
  `2DAE67334A752773F5DA94D0F838B67BF764E8B3BF9A9D6DAD9196D3C7CEB34D`.
  One 6.31696-point overfull box belongs to the deliberately temporary seam
  closure. Compiled pages 14 and 15 were inspected at 600 dpi and show no
  clipping or overlap; changing canonical source merely to silence that
  wrapper warning would be less faithful, so no source edit was made. Workflow
  ledger: two rows / 1,208 bytes / SHA-256
  `65D002B3FF98378B9E329BD75391BB575728D4295AA8B5F1CA590670130937DF`.
- Checkpoint R22 is 7,709 bytes / SHA-256
  `7BA41019FEE8362A644B856E7389E89087AE86911C7528F04D86104A6C8F5532`,
  PASS/errors empty. Next cursor is printed p.100, continuing Proposition
  2.2.5 after `Il existe alors une`.
- The first read-only R24 binding command did not execute because a PowerShell
  interpolated variable immediately preceded a colon. No file, source, image,
  or build was touched. The command was corrected by delimiting the variable;
  the complete second replay then returned declared errors zero and binding
  errors zero. This is a lead tooling-syntax mistake, not a source decision.

## 2026-08-02 — EGA I printed p.100 / exact diplomatic and English decisions

- Searched both active EGA trees for existing p.100 evidence and found none.
  Generated exactly one direct-authority image at 1,100 dpi, 8,220×11,077 /
  6,427,556 bytes / SHA-256
  `33F148CC42DCFD369BBE82C64EFA714084E8950CE8A1C31036CF583A493798BB`.
  Original-detail inspection resolved every formula and small mark; no crop,
  OCR, second authority render, agent, or parallel job was used.
- Completed Proposition 2.2.5 with the exact $f$-morphism/$A$-homomorphism
  bijection and bracketed $[\varphi]$ twist. Kept its proof as an unheaded
  roman paragraph, because NUMDAM prints no `Démonstration` heading.
- Transcribed 2.2.6 with the correct underlying continuous-map conditions;
  2.2.7 with the exact $X\to Y\to Z$ direction, $g\circ f$ order, three
  assertions, inverse images, and prime/double-prime equalities; and 2.2.8
  with both induced structure-sheaf restrictions and all four local
  properties.
- Transcribed 2.2.9 with finite component indexing, $\xi_i/\eta_i$, the
  singleton inverse image, and the sharp stalk map
  $\mathscr O_{\eta_i}\to\mathscr O_{\xi_i}$. Transcribed 2.2.10 as an
  authorial `Convention de notations`, not a modern correction. The localized
  semantic environment preserves that visible heading in the bounded reader.
- French source: 13,093 bytes / 296 lines / SHA-256
  `847E41008F84D6C74DAD4BEE3CA0C6DB2D9155BFE1947B7529D14EFF894C09E4`.
  Ten-row ledger: 4,528 bytes / SHA-256
  `282926E7B47BFC07FB6A87F39B4651AB6DE49C3A37CCF50E84F523D02DB92215`.
  Source corrections, source typos, unresolved readings, and diagrams: zero.
- English comparison found two inherited deviations. In Proposition 2.2.7(ii)
  `g\circ f closed` omitted the finite verb printed in French (`est fermé`),
  so it became `g\circ f is closed`. `Claims (i) and (iii)` became direct
  source-register `Assertions (i) and (iii)`. Both are reversible and have no
  mathematical effect. English source: 25,221 bytes / SHA-256
  `33AF57E584C85A17B7E0A18D22E0C504793BD0C71A30DC864EE0775DC349F5F2`;
  ledger ten rows / 4,145 bytes / SHA-256
  `81A07441311D728DA84936E0AE8C9C7708753527DE7D80CDF8F366CBFC63864C`.
  Two inverse substitutions reproduce exact R28. Mathematical/source repairs,
  English lead errors, and reversals: zero.
- R29 manifest: 127 rows / 7,280,227 bytes / SHA-256
  `3FC26BF7E9F628BF33AF9834C304C89071A21644DE923E6BCAC42FED6CE6AEE1`;
  ordinal tree SHA-256
  `7B25527C49B34E8EBB847D5887FAE707DBAB1DD9649A4508D0912407BAEAA96A`.
  Section/full validation SHA-256 values are
  `9AE6449765D5C1F8478EEC1E4A7E622D583BAE33CADC75CC22B4ACE6F8FCF73D`
  and
  `A391D6647EF46501FB39B3E3D313385B97FD15CDC17566A53D0133AE964797BD`,
  both PASS/errors empty.
- The two-pass bounded build is 16 pages / 173,098 bytes / SHA-256
  `2F2D5983DA0C539D607641859E6F6575BC6986B34261E8C5909427F7509F9F5B`.
  Hard diagnostics are zero. Only affected pages 14, 15, and 16 were rendered,
  sequentially at 600 dpi for layout; all three personally pass. A pypdf
  replay proves predecessor/current pages 1--13 have identical 47,216-character
  extracted text, SHA-256
  `1F99AE6A5D640FBC909E13561266B5DF1A4F3A7F81A4E0F2FC611714C81AFC57`.
- Three workflow mistakes are append-only logged: the first render command
  used an unavailable PATH name and created nothing; one metadata command
  unnecessarily read the 6.4-MB PNG through `Get-Content`; and a guessed
  nonexistent `pdftotext` path produced empty strings whose apparent equality
  was rejected. Each was source-neutral and closed; the last was replaced by
  the valid pypdf replay above. Workflow ledger: three rows / 1,686 bytes /
  SHA-256
  `ED6C9885455F572438E9A1EEB838656F7B13D6C17D97023B21FEF0B4E0B4A316`.
- Checkpoint R23 is 6,479 bytes / SHA-256
  `BB8583C50950D3831D2CC2E5E35380E52AD56A4AC60710A15F883A10C2C1D9E1`,
  PASS/errors empty. Next cursor is printed p.101, opening §2.3.

## 2026-08-02 — EGA I printed p.101 / sections 2.3--2.4.1

- Reuse-first search found no authority image for this page. Exactly one
  1,100-dpi page was generated and personally inspected at original detail:
  6,407,754 bytes / SHA-256
  `3DE6FB3D2EB090764E6B7404BFBE7BF024DBB82D1ED93972119B84A654333341`.
  The small commutative triangle was already unambiguous at that represented
  detail, so making a 5,000- or 9,000-dpi crop would have added memory cost
  without resolving anything. No OCR ran.
- Added diplomatic French 2.3.1 and Example 2.3.2 with the exact `K`,
  `B=K[s]`, `C=K[t]`, `U_12`, `U_21`, localization fractions, reciprocal
  substitution, and nonaffineness argument. Preserved the future II.2.4.3
  locator and the source's statement that the construction will be encountered
  again later; it does not promise a later proof of the same assertion.
- Added 2.4.1 with `A` local, the unique closed point, the specialization
  direction, `O_y=B_y`, the maps `B -> B_y` and `Spec(O_y) -> V -> Y`, and
  independence from the chosen affine neighborhood. Reconstructed the source
  triangle natively as `B' -> B` with two arrows down to `O_y`; source image
  shows exactly those nodes and directions and no labels. Stable target:
  `I.2.4.1.diagram-fr`. No raster is active or delivered.
- No French source typo, mathematical defect, or ambiguous reading was found.
  Current French source: 16,814 bytes / 373 lines / SHA-256
  `73968E89E47D9DB989CAAD204BB32699BDE5EBE500387BB4C166FE44CB167FF4`.
  Nine-row decision ledger: 4,235 bytes / SHA-256
  `F7329A53C494396C09C8C6DED894FB40E40254977C66E25172CF50B19A3C297A`.
- English R30 admits five reversible source-fidelity repairs. `although` became
  causal `since` for `puisque`; the gluing sentence now has two polynomial
  rings and two isomorphic affine schemes in grammatical parallel; `We later
  show` became `We shall encounter again later`; the local-scheme definition
  now says its ring `A` is local; and plural `For all preschemes ... and
  points` became `For every prescheme ... and every point`. These restore
  logic, grammar, temporal register, definition wording, and quantifier
  register; none changes formulas or mathematical content.
- Current English source: 25,205 bytes / SHA-256
  `39D017669DCEFD7B859A5851D112CD2605720CB68F2C7A695C8BEE3FAA6D3535`.
  Ten-row English ledger: 4,870 bytes / SHA-256
  `A487312FE9ECD0087CFC885B6E20D307CB98659A1B3216DDFD1C151FCD4316B2`.
  Five inverse substitutions reproduce R29 exactly. Mathematical/source
  repairs, lead errors, and reversals: zero.
- R30 manifest: 127 rows / 7,280,211 bytes / SHA-256
  `0643CFD16D04791CC6865EA67D4C8FC19E0C77D38A073DB7BB0C4EE694AFAC4D`;
  ordinal tree SHA-256
  `E6C94B0401070FA4EA758DA90A03829EE7ED40D97A611A3EA86F751D13E64245`.
  Section/full validation SHA-256 values are
  `0297DA8CFFFE2870F360923A79CFCF8C8D4FD462538CC65A35F7037D7BA45B8F`
  and `0F533AF99A7BA7A2381ABA387ABCCF01841934A72B772AD2A49C555E0B442F62`,
  both PASS/errors empty.
- Lead review found a bounded-wrapper structural defect inherited from older
  checks: semantic examples displayed `(number) Exemple`, unlike NUMDAM's
  `Exemple (number)`. The French source environment was not wrong. A new
  no-overwrite p.79--101 wrapper localizes the heading correctly; earlier
  wrappers remain historical. Only compiled pages 11 and 15 changed for this
  reason before page 16's new source. All three were personally reviewed at
  the already-generated 600-dpi layout scale and pass.
- The two-pass bounded PDF is 16 pages / 178,349 bytes / SHA-256
  `238F7406BB562042BAEA00C1520169FDAB3F42FD8F64AFA82DA93F4DAA63A3C4`.
  Hard diagnostics are zero; the single 6.31696-point temporary-wrapper
  overfull is pre-existing and visibly benign. Page 16 has correct headings,
  formula attachment, native diagram geometry, and no clipping or overlap.
- Six source-neutral workflow events are append-only logged: the temporary
  example-heading defect; one validation lookup made from the wrong root and
  rejected; one PowerShell metadata command that failed to parse before
  execution; and two apply-patch context mismatches rejected atomically before
  changing their target files. The first restart harness then concatenated
  expected triples and produced a wholly false missing-file result, which was
  rejected. No source or mathematics changed. Ledger: six rows / 3,541 bytes /
  SHA-256
  `AA6E37F48D368D8F89CCF598369328AFA3F8EEB2808583B86B1647F4E113E137`.
- Checkpoint R24 is 7,918 bytes / SHA-256
  `2B8A9A673EC9DE56E26E13566CF11568F8DD5F3474A602B95F6F7EDE6410781B`,
  PASS/errors empty. Next cursor is printed p.102, Proposition 2.4.2.

## 2026-08-02 — EGA I printed p.102 / sections 2.4.2--2.4.5

- The scoped interlanguage reuse search found no p.102 witness. Exactly one
  direct 1,100-dpi authority page was created: 7,241,110 bytes / SHA-256
  `370CD729724B078B34089C58DA7D8FEB4A5F9CB31460EC6664239EEE493A5F21`.
  The page has no diagram, and every small mathematical feature is unambiguous
  at original detail, so no high-resolution crop or OCR was justified.
- Transcribed 2.4.2 exactly: the canonical morphism, homeomorphism onto the
  generalization subspace `S_y`, the condition `y in closure{z}`, and
  `theta_z-sharp:O_z -> (O_y)_p`. Preserved both causal proof clauses, the
  affine reduction, and the italic correspondence with irreducible closed
  subsets containing `y`.
- Transcribed Corollary 2.4.3 without normalization: `y` is the generic point
  of an irreducible component exactly when the sole prime of `O_y` is its
  maximal ideal, equivalently `O_y` has dimension zero.
- Transcribed 2.4.4 with the unique factorization
  `X -> Spec(O_{psi(a)}) -> Y` and the bijection with local homomorphisms.
  The proof retains `a in closure{x}`, `phi^{-1}(j_a)=j_{psi(a)}`, invertibility
  of `phi(B-j_{psi(a)})`, the fraction-ring universal property, and the exact
  converse map directions.
- Transcribed 2.4.5 through the authority page's terminal colon: field spectra
  as one point, factorization `A -> A/m -> K`, field monomorphisms, and the
  canonical `Spec(O_y/a_y) -> Y` construction. The p.103 consequence was not
  anticipated. No French source typo, correction, ambiguity, or diagram was
  found. Current French source: 21,434 bytes / 461 lines / SHA-256
  `81031D76811A088C7A4B777D60F15FB1EBBCA837B5CB4CD24ABBD688B65B4C1F`.
  Nine-row ledger: 4,159 bytes / SHA-256
  `7325833EC8890A9A8A0A627E14902F5DD3160A7CD019F880A41ABAB31EA3BD7E`.
- English R31 applies nine individually reversible fidelity edits:
  `for every y`; `onto ... consisting of those z` and `in other words`; `we
  can reduce ... in that case`; restoration of `therefore` after 2.4.2;
  `with ring A`; `for every x`; `the factorization asserted in the statement
  therefore`; `completes the proof`; and `that is ... Proposition therefore
  gives`. Each matches a precise French quantifier, connective, referent, or
  register choice; none changes a map, ideal, theorem, or proof step.
- Four mathematical units were explicitly retained: 2.4.2 topology/stalks,
  2.4.3 dimension zero, 2.4.4 factorization/localization, and 2.4.5 fields/
  residues. Current English source: 25,259 bytes / SHA-256
  `C9C8D501845AC6FDAF6E6172D308C90C5D34B22AED6C3059DF132F48F8B6E04B`.
  Fifteen-row English ledger: 5,278 bytes / SHA-256
  `C54DDBC3E12EB17048F5346E33FC8830A8BD341874BDEA1E187C454A997AE69D`.
  Nine inverse substitutions reproduce R30 byte-for-byte. Mathematical/source
  corrections, lead errors, and reversals: zero.
- R31 manifest: 127 rows / 7,280,265 bytes / SHA-256
  `AACB1E16646D6DAAEDF384728D9106CF1D752DDC6223B0F405C2BCC8551562ED`;
  ordinal tree SHA-256
  `D90DDDD991E64D1C022D4BD1CABCD597D46B4FF6ECD23DFAA12B06DB07FEA72E`.
  Section/full validation SHA-256 values are
  `DFFFA52C8E8CDAD313C2FF3E0722141CB1346503D625CE43295BD6F7E75A964A`
  and `6C30C88EAF95271CC613320EFF2CCBB50282EB71E6801619872F2D1011F94563`,
  both PASS/errors empty.
- The first bounded build used pdfLaTeX by mistake. Its 38 repeated automatic
  `equation.0.1` destinations disappeared when the admitted XeLaTeX engine was
  restored. The pdfLaTeX build and one diagnostic are retained unchanged as
  non-adjudicative history; they do not imply a source defect. This mistake,
  one overly broad filename reuse search, and one rejected Windows wildcard
  path are logged in the three-row workflow ledger, 2,066 bytes / SHA-256
  `5589AE6D1F0425794F948201B4EFB08BE2CAD99B2B79AAE042934C09125B31AB`.
- The controlling two-pass XeLaTeX PDF is 17 pages / 184,393 bytes / SHA-256
  `2601FE3650929E0E0F11E23DC98A7A05DFE620C1EF59B9618C30D73563675845`.
  Hard/undefined/duplicate diagnostics are zero. Pages 1--15 have exact
  predecessor text; affected pages 16--17 were the only pages rendered and
  personally pass. The short final page is intentional.
- Checkpoint R25 is 8,036 bytes / SHA-256
  `8DDC1F5216FE7D1E210C6F6AE57393F677BCDBAE965D948E5890846C59C66CF4`,
  PASS/errors empty. Next cursor is printed p.103, continuation of 2.4.5.

## 2026-08-02 — EGA I printed p.103 / diplomatic French and paired English R32

- Searched the exact EGA-I authority-evidence root before rendering. No
  printed-p.103 witness existed, so generated exactly one direct-authority
  full-page image at 1100 dpi:
  `qa/authority_reuse/ega1_chapter1_opening/EGAI_pdfonebased102_printed103_context_1100dpi.png`,
  8113x11138 / 6,908,140 bytes / SHA-256
  `68B9B43166B66DE85232A58E9084482CCC1AF3EDB11CFD7973FD5827B53453F3`.
  Personal original-detail inspection resolved every formula, subscript,
  ideal, arrow, label, and punctuation mark, including the simple triangle;
  no crop or OCR was justified.
- Transcribed Corollary 2.4.6 exactly: the unique factorization through
  `Spec(k(psi(xi)))` and the bijection with monomorphisms `k(y) -> K` retain
  their variables, fields, map order, and direction.
- Transcribed Corollary 2.4.7 and its source-prose proof exactly. The canonical
  `Spec(O_y/a_y) -> Y` map remains a monomorphism of ringed spaces; the
  `a_y=0` case and I.1.7.5 citation are unchanged. I did not manufacture a
  proof environment around the separate source sentence.
- Transcribed Remark 2.4.8 without normalization: every invertible
  `O_X`-module on a local scheme is free, or trivial; the contrast with
  arbitrary affine normal/factorial rings and Chapter V pointer remain exact.
- Opened §2.5 and transcribed 2.5.1 exactly: prescheme over `S`, `S`-prescheme,
  base prescheme, structure morphism, `A`-prescheme, the equivalent
  `A`-algebra-sheaf structure, unique `Z`-prescheme structure, points over a
  base point, and domination by a dominant structure morphism.
- Transcribed 2.5.2 through the exact p.103 end: `S`-morphisms, closure under
  composition, the category, `Hom_S(X,Y)`, identity, and `A`-morphism. The
  source triangle was reconstructed natively under target
  `I.2.5.2.diagram-fr`: `X -> Y` is labelled `u`, and both structural arrows
  descend to `S`. No raster entered the reader.
- French source after the page: 25,350 bytes / 549 lines / SHA-256
  `E1A20C84C2BB1914106EF14B280F5C3B41B5AFA975E5761828167C50206CAA01`.
  Nine-row decision ledger: 4,215 bytes / SHA-256
  `B520493D1CA931E46505DACB158597147EAC7DC84B9F53EF5AFAB21771AF13A7`.
  Source corrections, source typos, unresolved readings, and lead errors: zero.
- Personally compared the paired English from 2.4.6 through 2.5.2. Made only
  three fidelity edits. `For every y` restores singular `Pour tout y`.
  `(or, as one also says, is trivial)` supplies grammatical English for the
  source predicate `ou, comme on dit encore, est trivial`. `This entails
  that, for every s and every x, u(x) must also be over s` restores
  `cela entraîne`, both singular quantifiers, and `doit`. None changes a
  mathematical claim.
- Retained all residue-field, quotient-spectrum, invertible-module,
  base-prescheme, structural-map, categorical, Hom, and diagram mathematics.
  No formula, source correction, target, edge, diagram, citation, lead error,
  or reversal changed. Current English source: 25,275 bytes / SHA-256
  `5CFC1E90B2C64C7E2E71FC9EA27DC56E0B03F6ECC48E4C440D613097AB82E191`.
  Eleven-row ledger: 3,899 bytes / SHA-256
  `F889E3A1981064D8F9629E844A4C2996EB480BD55240322365453EDA90898A47`.
  Three inverse substitutions reproduce R31 byte-for-byte.
- R32 manifest contains 127 files / 7,280,281 bytes, SHA-256
  `9E77BB96A68A09C711439AF2D22FFC4166B844288E6E85F82B69D515B4CD7680`;
  independent ordinal replay matches tree SHA-256
  `5220A1B928990312262D72AC84A3BABAA67B2AED3189AFFD25333911B16B3D22`.
  Section/full validation SHA-256 values are
  `EB30391344D138D692FDC95AFD80C95C4831BCEE8545E97A08B27AEF38ACB811`
  and `EB5C64209251AC0EAB23185C2992E2741F3FE2C7D4A6D3F79D9AD462B4D01683`,
  both PASS/errors empty.
- Built sequentially with XeLaTeX only after the source edit. The admitted
  two-pass PDF is 18 pages / 190,068 bytes / SHA-256
  `E0FA8D1C9A7D31496940AC72F7C7331966C19AB219B0825EC3D13D2B11F86D86`;
  hard/undefined/missing/duplicate/rerun diagnostics are zero. Pages 1--16
  retain exact predecessor text. Only changed/new pages 17--18 were rendered
  at 600 dpi for compiled-layout review; both personally pass, including the
  native triangle, line attachments, and intentional short last page.
- Preserved nine source-neutral workflow mistakes append-only: two failed
  wrapper invocations before the sole successful authority render; one
  literal `$out` partial build caused by a native-argument quoting error; the
  bounded wrapper's initially missing `remark` environment; a guessed
  `pdftotext` path; accidental text-reading of an executable; an `H` helper
  collision; one unparenthesized `Join-Path` array call; and one restart-
  harness interpolation parser error; and one culture-sensitive manifest
  sort that produced a verifier-only false negative before the ordinal rerun.
  Each failed closed or was corrected before admission. Workflow ledger:
  5,592 bytes /
  SHA-256
  `0D55851828D617A65EB63D8952244FC1E0B37098E4D02B6D4AB6FD9B380E22F7`.
- Checkpoint `controls/EGA1_CHAPTER1_P103_VALIDATION_R26.json`: 8,157 bytes /
  SHA-256
  `E12D1BAFBF55F86BA7DC24349E7439E518A82397C649E51CA3186B13383BB78A`,
  PASS/errors empty. Next cursor is printed p.104, I.2.5.3. Agents used: zero;
  OCR: none; rendering/building: sequential and bounded.

## 2026-08-02 — EGA I printed p.104 / diplomatic French and paired English R33

- Reuse-first search found no p.104 witness. Generated exactly one direct
  authority page at 1100 dpi, 7914x10695 / 7,176,786 bytes / SHA-256
  `B6EF43C83B262486BDCF22618765C16F692428CF2EBA02C007694183909ABF0A`.
  It resolved all general prose and formulas. A substantive type-word question
  in 2.5.5 justified exactly one tight crop at 2500 dpi, 14500x2100 /
  146,163 bytes / SHA-256
  `4800122869C732889E83BF080FAC3923451157B73CAD92D2ABC043825933296B`.
  The crop unambiguously reads `Si X est un S-morphisme`; no 5000/9000-dpi
  escalation or OCR was needed.
- Transcribed 2.5.3 exactly: induced `S`-structure along `X' -> X -> S`,
  restriction to open subpreschemes, unique gluing of compatible
  `u_\alpha`, and factorization through an open `V` retain every map,
  intersection, quantifier, and uniqueness clause.
- Transcribed 2.5.4 without supplying the name omitted by the source after
  `pour tout S'-préschéma`. The following formula itself introduces `X` in
  `X -> S' -> S`. Both directions of the open-base restriction statement are
  exact.
- I initially inserted an explicit `X` after `S'-préschéma`, following the
  clearer English rather than the printed French. Direct rereading caught the
  mistake before build/admission; I removed it globally from the French source
  and logged stable ID
  `EG-EGA-I-P104-WORKFLOW-FR254-EXPLICIT-X-001`. This is one lead
  transcription error caught and repaired; it had no mathematical effect.
- Preserved the exact 2.5.5 phrase `Si X est un S-morphisme` in diplomatic
  French and catalogued it as a source typo rather than silently changing the
  author. The appositive structure morphism `X -> S` and the definition of an
  `S`-section require `S-préschéma`. The paired English already makes that
  type correction; the direct crop proves it was justified, and a visible
  English footnote now documents the divergence.
- Began `ega1-3-fr.tex` at the source section boundary. Transcribed §3.1:
  the topological sum, pairwise disjoint open components, homeomorphisms,
  transported structure sheaves, `Hom` product bijection, unique structural
  map, binary sum, and `Spec(A\times B)` identification. Opened 3.2 and
  transcribed only Definition 3.2.1 through the p.104 words `est un produit
  des`; the current temporary environment close keeps the bounded file
  compilable and will move after the p.105 continuation is admitted.
- Current French sources: `ega1-2-fr.tex`, 27,463 bytes / 592 lines / SHA-256
  `AE6B128092ACBB8C1AFB4899EEA003FB966B6FF6669A264B59FD5F095AF4F029`;
  `ega1-3-fr.tex`, 1,706 bytes / 34 lines / SHA-256
  `76F6B21FA566B11FA80E6538875E2A122B67616B37331EFE6E39794B697F6B93`.
  French ledger: nine rows / 4,498 bytes / SHA-256
  `C997C1D70DD5C6F32E67538657AB7DDE820ADF495BEF7EA8AF9BD3309F74769F`.
  Applied French source corrections: zero; catalogued source typos: one;
  unresolved readings: zero; repaired lead transcription errors: one.
- Personally compared English 2.5.3--2.5.5, §3.1, and the p.104 3.2.1 seam.
  Restored logical `therefore` for `donc` and singular `every pair` for
  `tout couple`. Retained the English explicit `X` in 2.5.4 as necessary
  grammatical clarification and retained the plural topic headings as normal
  English heading register. Added the 2.5.5 source footnote; made no new
  mathematical correction.
- Current English `ega1-2.tex`: 25,429 bytes / SHA-256
  `5785621211C98B1A4452864F3D408325ECED8F84C6CB16DE0875E052A6E7984F`.
  Audited unchanged `ega1-3.tex`: 56,496 bytes / SHA-256
  `ED1559A08A41EC54E35C4A1E5E192552EF0B1EC52B4CE5FAF1F6E6BB3E5707FB`.
  Nine-row English ledger: 3,834 bytes / SHA-256
  `B9BEC0096EDDEE9AEDD842F8F9197C31B5C770AA687840BB281944C32E915CF7`.
  Three inverse operations reproduce R32 byte-for-byte.
- R33 manifest: 127 files / 7,280,435 bytes / SHA-256
  `9FE51AAA429E7749F926D04B52B05891820F4FE6CC3BCCA49FF318AE3402C213`;
  ordinal tree SHA-256
  `85C3EE351B174E4C8C4CE49E782EA151C72D91E6A35A96674E633E10BA0E6956`.
  Only `ega1/ega1-2.tex` differs from R32. Section/full validations have
  SHA-256
  `0697B5A637FBE0835EDAC71560C2F7825BD2700A0C39441E107AEE9C0CF23259`
  and `835E4222FC24AE496D907DE67B42A61F39EF0D097B41650E89C34C7023490B7D`,
  both PASS/errors empty.
- The two-pass XeLaTeX reader is 18 pages / 194,458 bytes / SHA-256
  `E6B26C091A3B982E3E8677E890A50775BEB32CA9D49F9CA269A02F20F6DA5DCD`;
  hard/undefined/missing/duplicate/rerun diagnostics are zero. Pages 1--17
  retain exact predecessor text. Only page 18 changed; its 600-dpi layout
  witness is 1,375,914 bytes / SHA-256
  `A73CA8AFBB6185EDB4CF26439232F8B45854C24BFCBBDDEA9EC9D61460AB7CAB`
  and personally passes all headings, formulas, sums, products, indices, and
  the deliberate definition seam.
- Besides the repaired French word insertion, two read-only harness mistakes
  were caught: a PowerShell quoting rule initially prevented exact inverse
  removal of the new footnote, and a missing `in` space caused one manifest
  harness parse failure. Both were rejected and rerun correctly. Three-row
  workflow ledger: 1,691 bytes / SHA-256
  `BF163D055DE9F9AD04CA705051E61A615B146AD3BAB75FFB20A9D9DBF14EC82A`.
- Checkpoint `controls/EGA1_CHAPTER1_P104_VALIDATION_R27.json`: 8,883 bytes /
  SHA-256
  `D21A97F27507F42FC20848B422599877D5F04F4653E8A799DD1A5266B5FD49EF`,
  PASS/errors empty. Next cursor is printed p.105, continuation of 3.2.1.
  Agents used: zero; OCR: none; rendering/building: sequential and bounded.

## 2026-08-02 — EGA I printed p.105

- Reuse-first check found no exact p.105 authority image. Generated exactly
  one 1100-dpi page, 9,091x11,428 / 6,192,099 bytes / SHA-256
  `303FC3F3301AFC83E03CC8692C126A5D2777A1A000A4132C3DB32483EA642D5A`.
  Personally inspected at original detail. No crop or OCR was required.
- Completed Definition 3.2.1 at the page seam and transcribed the full p.105
  span through Corollary 3.2.5. The categorical product, projections,
  `(g,h)_S`, `u\times_S v`, affine tensor product, Hom bijections,
  rho/sigma/tau formula, monomorphic-base argument, and open-subset statement
  all agree with authority. Printed symbols are represented by reversible TeX
  notation only; no French wording or mathematics was corrected.
- New stable French targets: `I.3.2.2-fr`, `I.3.2.3-fr`, `I.3.2.4-fr`, and
  `I.3.2.5-fr`. These add product universal property, product functoriality,
  affine fiber product, and base-restriction concepts to the later pre-Stacks
  scaffold.
- Current `ega1-3-fr.tex`: 6,117 bytes / 121 lines / SHA-256
  `66E0EF2BBE7234C578E07E7465C0EEA8A86E8CB39310ACABD2AFA31A05716C22`.
  Nine-row French decision ledger: 4,143 bytes / SHA-256
  `4F85769E94A2E8EF7C3B4A6C7A8400D062313CC218BD5C97596C0109C947D8DB`.
- English audit repaired two source-facing defects. First, the old text began
  an `If` clause, inserted `and let`, ended the sentence, then started `We then
  write`; source French has one conditional. It is now one grammatical
  conditional. Second, source singular `l'hypothèse sur f entraîne` is now
  singular English `the hypothesis on f implies`, not plural
  `hypotheses/imply`. Neither repair changes mathematics. Retained and logged:
  `affine scheme given by some ring` for `schéma affine d'anneau`, explicit
  English Proof environments, and the textual `(T, I, 1.1)` locator.
- Current English `ega1-3.tex`: 56,482 bytes / SHA-256
  `180110F77A0665B749B1F29AB7DE6808E4E9BDEB8A857407572C3D6CF29B693B`.
  Two exact inverse operations reproduce the preceding 56,496-byte source at
  SHA-256
  `ED1559A08A41EC54E35C4A1E5E192552EF0B1EC52B4CE5FAF1F6E6BB3E5707FB`.
  Eight-row English ledger: 3,438 bytes / SHA-256
  `197F46B25506E94021E7987D7BB54DAC98FE4B649CD232E881DFB87E76004B55`.
- R34 manifest: 127 files / 7,280,421 bytes / SHA-256
  `7E5002ACDB744AE24EE49272325ADE110DAA406E813E3A80F357DB2B91AE472B`;
  ordinal tree SHA-256
  `E02F5175C3DEFA9A2EE35E2844ED39ABE01F7EC998331411E405AA7D87E8C241`.
  Section/full validations: SHA-256
  `50039F4AF08B24AA3A50DFFEA37168CBBDD110EAC16B587BDB441769A8E9F2E6`
  and `CAA4B234B7BAB495C977F94484A6B50B6104D6529A056825DB85E1EADD2EFFEC`,
  PASS/errors empty.
- The first French build made the footnote marker a separate line. This was a
  TeX placement error, not a source reading: moved the marker into the Hom
  display, preserved the footnote text, and rebuilt in no-overwrite r2. Final
  19-page PDF: 202,390 bytes / SHA-256
  `B182ED823AB1F6ED7778AF30B96D11095B3284997CBA642234490D896472B206`.
  Pages 1--17 are predecessor-text exact; changed pages 18--19 both personally
  pass at 600 dpi. English bounded 12-page PDF SHA-256
  `1C41C73B871FBD4ECC630BF6B904B18356E68B9782157C753342CEE65C1EE2D4`;
  changed page 1 personally passes.
- Self-audit record: restored one omitted source comma before the first build;
  repaired the detached footnote marker after the first build. Closed harness
  errors include Poppler wrapper failures, one invalid Windows rg wildcard,
  an atomic source-patch context rejection, long-path postprocessing failures,
  a pypdf console-encoding failure, one LF/CRLF inverse-harness mismatch, and
  one later atomic five-file logbook patch rejection caused by a stale English
  STATUS anchor. The latter changed no file; the bounded log additions were
  then applied separately against current tails.
  One improper broad executable search was terminated after about 22 seconds
  and will not be repeated. Twelve-row workflow ledger: 5,695 bytes / SHA-256
  `3C472FDEC297A20F9A13F0E694A0347435AB84A9143BF96FA05A202BF77147C2`.
  No remaining source or mathematical effect.
- Checkpoint R28: 9,118 bytes / SHA-256
  `E09FD9270B63CA943059DDEDCA557FB420C4C65D60DCF2D46FC68AA51ECCE022`,
  PASS/errors empty. Next cursor printed p.106. Agents used: zero.

## 2026-08-02 — EGA I printed p.106

- Reuse search found no existing p.106 authority image. Exactly one direct
  NUMDAM context page was rendered at 1,100 dpi:
  `EGAI_pdfonebased105_printed106_context_1100dpi.png`, 9,091x11,428 /
  4,965,020 bytes / SHA-256
  `8ECB4E558B1E60B0C989B2000844C2806C77765669CDFFBAF73C0D7678E4B7FF`.
  Personal original-detail inspection resolved every inverse image, Greek
  index, intersection, composition, and punctuation mark. No higher crop and
  no OCR were justified.
- Diplomatically transcribed the one-line proof of 3.2.5, Theorem 3.2.6, the
  proof transition, Lemma 3.2.6.1 and its proof, and Lemma 3.2.6.2 with both
  halves of its proof. Preserved the source-unheaded proof prose, abbreviated
  `déf.`, literal `c.q.f.d.`, and exact mathematical order. The long
  inverse-image identity is line-broken with `aligned` only for TeX
  readability; no symbol or equality order changes. New stable targets:
  `I.3.2.6-fr`, `I.3.2.6.1-fr`, `I.3.2.6.2-fr`.
- Self-caught integration error: the initial patch used a nonunique
  `\end{corollary}` anchor and inserted p.106 after 3.2.3, before 3.2.4 and
  3.2.5. The text itself remained intact, but its order was wrong. I detected
  this by personally inspecting changed compiled pages 19--20, moved the
  unchanged 3.2.4--3.2.5 block before the p.106 marker, replayed locator order
  as 3.2.3 / 3.2.4 / 3.2.5 / p.106 / 3.2.6, and rebuilt no-overwrite. This is
  a lead error, not an author/source defect, and is not hidden.
- Current French `ega1-3-fr.tex`: 10,254 bytes / 216 lines / SHA-256
  `D928E7E21AB6B3C97A5A4B8692A75033075A61A58BA44F2E10E17A6603E81E14`.
  Eleven-row decision ledger: 4,400 bytes / SHA-256
  `E6757586AB33B973673E229E307EE9914AF5836EEC815643968DBD8F1C2A8F5D`.
  Source corrections, source typos, unresolved readings, diagrams, and active
  rasters are all zero.
- English comparison found one omitted source feature. French closes the proof
  of Lemma 3.2.6.2 with `c.q.f.d.`; inherited English ended with a period.
  Added terminal `\qed` under
  `EG-EGA-I-P106-EN-QED-RESTORE-001`. Rationale: restore a visible source
  proof terminator; mathematical delta zero. One exact inverse operation
  removes those four bytes and reproduces the p.105 English source, 56,482
  bytes / SHA-256
  `180110F77A0665B749B1F29AB7DE6808E4E9BDEB8A857407572C3D6CF29B693B`.
- Retained and individually justified: “The proof proceeds in several steps”
  explicitly names the referent implicit in `Nous procéderons`; “a unique
  S-morphism” is the exact English compression of `un S-morphisme et un
  seul`; “similarly” preserves the repeated open-cover assertion; “Definition
  3.2.1” expands `la déf. (3.2.1)`; and “proof of Lemma 3.2.6.2” names the
  numbered source unit without changing its logical role. All remaining
  p.106 prose, formulas, and references were retained.
- Current English `ega1-3.tex`: 56,486 bytes / SHA-256
  `4EE566EFB51DDD19D81E0392070899C2A64A51AF6997D65BC1B4ED07386C317B`.
  Eight-row English ledger: 3,104 bytes / SHA-256
  `12BD1328BAD114D1B1CF117E03401E60391DA1C63FB078D28B62CC9C76B437F2`.
  R35 has 127 files / 7,280,425 bytes / manifest SHA-256
  `FBEF05B2BDCB707DC1DB7AC8E176981B66F234DA03E1399208F5AE134EA99929`
  / ordinal tree SHA-256
  `BBBCB2AAA9C5A946847B25B2F483024E637558955863F5A1E194CB4FDCD6C52A`.
  Section/full validations are PASS/errors empty at SHA-256
  `D7D0E55F9AC38AF76A9302D2A593CFAB0D5C41BBC0AFA6BA957C09BCDB8E752A`
  and `7DF09CABA52388F313CCA150D89C6309FA8A1E6EA685BBC87BF41D212E0CFE9F`.
- Build history is append-only. The first build was misrouted into literal
  `qa/ega1_chapter1_build/$out`; the correctly routed r2 still contained the
  source-order error. Both are adverse. Final r3 is 20 pages / 207,270 bytes /
  SHA-256
  `B35FD477AAAB362ABC38A6A957275635795E083F10AA2D3AA726D1D8A362EA6D`.
  Pages 1--18 are predecessor-text exact; pages 19--20 personally pass at 600
  dpi. The English 12-page bounded PDF is 113,629 bytes / SHA-256
  `C1907F6CD2FD0E12A678E231DAF85EE336688EC520646D271FB5DDD9181F8F3C`;
  personally inspected page 2 shows the source-backed terminal square and no
  layout defect.
- Nine workflow rows explicitly preserve one source-order error, one
  literal-output routing error, and seven closed patch/read-only/path/syntax
  failures. Ledger: 4,957 bytes / SHA-256
  `BD5C5881BBD39B639E4E7611D3514A2DEA177AA74AEF3AF5180A56A6A1B759C9`.
  Short temporary PDF/PNG copies used to work around Windows long paths were
  removed after the final evidence copy was hashed. No remaining source or
  mathematical effect exists.
- Checkpoint R29: 10,362 bytes / SHA-256
  `FA89227CD8E5CCBBA1EE733B93BE9C87782A39ADA29234C1F316646C942BBAD1`,
  PASS/errors empty. No agent, OCR, batch render, or parallel heavy job was
  used. Next cursor: printed p.107.

## 2026-08-02 — EGA I printed p.107

- Authority: NUMDAM PDF one-based p.106 / printed p.107, inspected personally
  from one 1,100-dpi image, 9,091 x 11,428 / 5,888,753 bytes / SHA-256
  `E28F0B56EA197B2A091AD9F2CD813EDB01A51CEFADCBC1CA260E4603D6568476`.
  Every represented glyph and formula was clear; no OCR or crop was needed.
- Diplomatic French adds Lemma 3.2.6.3 and its gluing proof, Lemma 3.2.6.4
  and its proof, and the exact first-page fragment of 3.2.6.5. Preserved:
  `h_{ij}`, `h_{ji}`, `f_{ij}`, the cocycle identity, all `W`, `Z`, `p`,
  `q`, `theta`, inverse-image and overlap formulae,
  `Z_{ij}=X_{ij}\times_S Y_{ij}`, and the printed seam. Stable targets:
  `I.3.2.6.3-fr`, `I.3.2.6.4-fr`, `I.3.2.6.5-fr`. No source
  correction, typo adjudication, or mathematical reinterpretation was made.
- Lead error `EG-EGA-I-P107-FR-EMPH-COMMAND-001`: the first TeX append
  omitted the backslash before the visibly emphasized source phrase `schéma
  affine`. Restored `\emph{schéma affine}` before admission. This was our
  transcription error, not an authorial error. The partial 3.2.6.5 `env` is
  temporarily closed only to compile; p.108 must remove that close and
  continue the same source unit.
- Current French source: 14,987 bytes / 307 lines / SHA-256
  `6D6DF12A04AEA3B2788983A70AB8A474A156C889369F0FD70CF560439E8F2D51`.
  Decision ledger: 9 rows / 4,017 bytes / SHA-256
  `0BBB806A5B6AE6AB72327A3BA47D222AFAD5DFA5C1FFCCFF711CA928660498AF`.
- French build: two sequential passes, 20 pages / 212,863 bytes / SHA-256
  `0FEA473F2FF2389C7AFB005930BEFA9A03004873BD1C4C9105D58BC3F7507D1B`.
  Pages 1--19 are predecessor-text exact. Only page 20 changed; personal
  600-dpi inspection passes with no clipping or overlap.
- English repair `EG-EGA-I-P107-EN-3263-CITATION-PLACEMENT-001`: inherited
  English made “by Lemma 3.2.6.1” justify the displayed equality. The French
  states the equality first and applies the lemma to the following product
  structure. Moved the citation to that sentence. Mathematical delta: none.
- Retained English choices: “It follows that we have” for `Il y a par suite`;
  “We immediately see ... and similarly” for `on constate aussitôt ... et de
  même`; “it suffices to prove” for `tout revient à prouver`; and `Theorem
  3.2.6` expanding `th. (3.2.6)`. Each preserves the exact logical content.
- The first inverse replay exposed seven lines carrying two post-R35 leading
  spaces each. Those fourteen bytes were visually inert but provenance-
  invalid. Removed them; preserved R36 and bounded build r1 as stale history;
  regenerated R37 and bounded build r2. Final English source: 56,478 bytes /
  SHA-256
  `E6EEAE7CEF181FBB81A6E671AEE221B87E59AB43AD18174CAE570C9161EE3CA7`.
  One inverse citation operation restores R35 exactly: 56,486 bytes /
  SHA-256
  `4EE566EFB51DDD19D81E0392070899C2A64A51AF6997D65BC1B4ED07386C317B`.
- R37: 127 files / 7,280,417 bytes / manifest SHA-256
  `F5E43F1622CD9BBE5829A18A91771824C0D3426C1D797149F9CB8861FA28861A`
  / ordinal tree SHA-256
  `D9237435250A25A398CFF70A89052955964AA4DFF7113F74DE77E5A26DA748FE`.
  Section/full validations are PASS/errors empty at SHA-256
  `346C47C220692A30C2D0D321B6449EB4786C47F70E0C9B6E6D2DBD753C95D737`
  and `6642BED78416D3DE1CB1F42ECFB91792B8F5C15BDAC338F0FC7304F5DFCC2FDF`.
- Final English bounded build r2: 12 pages / 113,641 bytes / SHA-256
  `2CEAC677F19FDA30ED24C911A04E9D43F75162CDAAC914918A54C457C58BD784`.
  All extracted page texts and the affected-page raster equal r1; the reviewed
  raster SHA-256 is
  `056807BFAFF42B8312F9DF9A8FCCC8787290F545AF5435C6C70C9A3BE8BEB390`.
- Workflow failures are explicit: two bundled `pdftoppm` shim failures, one
  invalid PowerShell here-string, and the fourteen-byte identity drift. The
  direct native renderer succeeded; all temporary page files were removed.
  Ledger: 4 rows / 2,255 bytes / SHA-256
  `9263FC48129B321445889E776AF4CC47083DF5F852898FFB0788CD69EAF5445C`.
- Checkpoint R30: 10,050 bytes / SHA-256
  `15657B56D2904F07954F47CC0414038EB9C5D1A24CA41E53EB214EBEBE6BC713`,
  PASS/errors empty. Next cursor is printed p.108, continuing 3.2.6.5.
- Incremental pre-Stacks scaffold: admitted the three p.107 semantic nodes,
  their explicit source-certain dependencies, the overlap/cocycle formula
  roles, and the p.108 incompleteness flag for 3.2.6.5. No speculative or
  exhaustive graph work was added. File: 5,566 bytes / SHA-256
  `188BD70453BAAF986CC5764E9B46B9C82EF8DFBD93A65DA9ACCC99AAEDBC9FFE`.

## 2026-08-02 -- EGA I printed p.108

- Reuse search found no existing p.108 authority render, so exactly one direct
  context image was made at 1,100 dpi: 5,140,185 bytes / SHA-256
  `7825A67A3EE20344DA76133CA2D8F09F1E735C7F61D11E6D603BBDE282762FFA`.
  Personal original-detail inspection found every glyph and the simple
  six-arrow diagram unambiguous; no extra crop and no OCR were used.
- Continued the same 3.2.6.5 environment across the p.107 seam, then
  transcribed 3.2.7, 3.2.8, the 3.3 heading, 3.3.1--3.3.4, and the exact p.108
  fragment of 3.3.5. The source heading's terminal period and both source
  emphases in 3.3.1 were preserved. The 3.3.2 diagram is native `xymatrix` with
  exact nodes, arrow directions, and labels; no raster entered the reader.
- French source is 18,863 bytes / 403 lines / SHA-256
  `C818114F3BAE8B049C945F9AEFE79F2D74AED1959EAB8DB3ED667D4DEA9F367F`.
  French decision ledger: 13 rows / 5,198 bytes / SHA-256
  `61815DBE2CE8BA37209E8FB59DDAF7C7B718E79061993C8277098D5E8420EC6F`.
- Two sequential XeLaTeX passes produced a 21-page bounded PDF, 218,138 bytes
  / SHA-256
  `4F013282A7F82AA7D6AAB44F7C41BB2CDEEFA904B7BA96622AB5F8A217B1B3D6`.
  Pages 1--19 remain text-exact to p.107; only pages 20--21 changed or were
  added. Personal 600-dpi inspection of both pages passed.
- English repair `EG-EGA-I-P108-EN-331-EMPHASIS-001` restores emphasis on
  `any category` and `exist`. This is typographic source fidelity, not a
  mathematical correction. The remaining English choices were separately
  justified: proof square and proof environment as modern structural markup;
  categorical restriction phrasing; terminal-punctuation normalization in an
  English heading; and the visibly bracketed 3.2.9 translator augmentation,
  which remains excluded from diplomatic French and still needs its own cited
  EGA II p.221 replay.
- Lead error/reversal: I initially removed the terminal proof square after
  3.2.6.5 solely because French prints no `c.q.f.d.`. Rechecking the English
  edition's explicit proof-structure policy showed that this was an
  overcorrection, so the exact R37 square was restored before manifest/build.
  This is logged both as a decision and as workflow error; final effect zero.
- Current English source: 56,492 bytes / SHA-256
  `0E9CE7FB4E26EE686D1549407FAB8ACF2B521C73C256EB86221524FD89D39D38`.
  Removing the two emphasis wrappers reproduces R37 exactly at 56,478 bytes /
  SHA-256
  `E6EEAE7CEF181FBB81A6E671AEE221B87E59AB43AD18174CAE570C9161EE3CA7`.
  English decision ledger: 8 rows / 4,420 bytes / SHA-256
  `522199B32536F9713525DC17D9ED21574C1DA8150432B49F293EA0CA2BA48447`.
- R38 manifest: 127 files / 7,280,431 bytes / SHA-256
  `15D8794F8BF6AA98FDE1D527EBD87DFED961A03FE59225D7F52D13C245027961`;
  exact ordinal tree SHA-256
  `85E5FBAAD2D054550D91F893853B51B2AE4DC085E4E831E4B8C4C63F1A62C987`.
  Section/full validations are PASS/errors empty at SHA-256
  `BB292CF24461D37BD69201E91D55C51BE78066D45FD15C26D41FB76C5B95687E`
  and `9D9D67D83E60190BA83561D324A72CDE646637162E85F71811A8597D62EE62BF`.
- The final English bounded build r2 is 12 pages / 113,673 bytes / SHA-256
  `F8D2691252BDFD726BFF1989F7246EC45A110EF0AFDB868724DB13E18642E912`.
  Only physical page 4 reflowed; whitespace-normalized extracted text remains
  equal on all pages, and personal 600-dpi inspection passed.
- Workflow history is explicit. The first seam patch was a harmless no-op.
  The proof-square overreach was reversed. An unquoted XeLaTeX output argument
  generated four artifacts under literal `source/$out`; the exact directory
  was verified and removed, the failed build console remains preserved, and
  the corrected build ran in a no-overwrite r2 directory. Workflow ledger:
  3 rows / 2,022 bytes / SHA-256
  `697722F29CB151A4487D6C66EA35C8EA0FBCD2B4DD13A188DBFBD9FE53197224`.
- Checkpoint R31: 10,181 bytes / SHA-256
  `C2990F06616057C1051F1CA6B4ED3A68BB04BA9B966E7D05B22738A657394282`,
  PASS/errors empty. Next cursor is printed p.109, continuing 3.3.5.

## 2026-08-02 -- EGA I printed p.109

- Exactly one direct authority page was rendered at 1,100 dpi, 4,873,516 bytes
  / SHA-256
  `77C148E48E4BBC61731DF844AEE8ECD88D46A2F65914451528DB294C2A1E69F2`.
  Personal original-detail inspection resolved every prime, subscript, arrow,
  label side, and formula. An attempted 3,000-dpi crop used a bad crop window,
  emitted a memory warning, and produced a blank file; the exact blank PNG was
  inspected and removed. Because the page image was already unambiguous, no
  retry or extra image was justified.
- Continued 3.3.5 across the seam, then transcribed 3.3.6, 3.3.7, 3.3.8,
  Proposition 3.3.9, and its proof through the terminal p.109 diagram. Both
  diagrams are native `xymatrix`; the second deliberately has no terminal
  punctuation because the source proof continues on p.110.
- Source typo `EG-EGA-I-P109-FR-338-F-VS-G-SRCTYPO-001`: French visibly
  prints that the product definition is applied to the pair `f` and `psi`.
  Context proves that the pair is `(g,psi)`: `g:T -> X` is the given map and
  `f:T -> X_(S')` is the unique map being constructed. Diplomatic French keeps
  `f`; the English reader's `g` plus immediate translator note is reconfirmed
  as a transparent source-backed correction.
- French source is 22,550 bytes / 484 lines / SHA-256
  `6C99E997042971815820CF5AF3145EB3E1EF37A8630538B61FB502F339FEBF09`.
  French ledger: 12 rows / 4,426 bytes / SHA-256
  `0936AEE282CBEF59C4C613DC3AB891BDEEE7BFDB086DAE6E16521D61DB0F19E1`.
- Two sequential XeLaTeX passes produced 22 pages / 223,448 bytes / SHA-256
  `3FEAD5020F46956CD02F67268B3E1B568B38666D42322997DCAAF0614D285587`.
  Pages 1--20 remain text-exact to p.108; only pages 21--22 changed or were
  added. Personal 600-dpi inspection of both pages passed.
- English repair `EG-EGA-I-P109-EN-339-DIAGRAM-PERIOD-001` removes the period
  attached to the `S''` node. The source diagram has no period and the sentence
  continues on the next page; the former punctuation falsely closed the proof
  at the page seam. No node, arrow, label, or mathematical statement changed.
- Retained English choices are individually justified: `base change` is the
  standard term for `extension du préschéma de base`; 3.3.7 repeats it as a
  synonym for `image réciproque`; and the proof environment is modern
  structural markup for the source's bare `En effet` paragraph.
- Current English source: 56,491 bytes / SHA-256
  `E5E4C011C43B959AD95657C6B3B79612A0DB6D97A3B926A24A6F853E88861B8C`.
  Restoring the one period reproduces R38 exactly at 56,492 bytes / SHA-256
  `0E9CE7FB4E26EE686D1549407FAB8ACF2B521C73C256EB86221524FD89D39D38`.
  English ledger: 7 rows / 3,499 bytes / SHA-256
  `A6FB32BFF8443ECEF62EC37435FF9ECF4006DA64E53780838D54273DA0CF0ACA`.
- R39 manifest: 127 files / 7,280,430 bytes / SHA-256
  `5582CBE296292FDAD0D5FF8B94C8E660466523DD6DEB9DDF28ACA6B3AEA443DC`;
  exact ordinal tree SHA-256
  `B94674F50196214AF56CD3A4E58BA323CC821B8A61DA7D36669CD1C4B5363BCB`.
  Section/full validations are PASS/errors empty at SHA-256
  `3B74BFEFE4AE0B234D56AD2BEBB980F225636B190FE93178CA7BA5A76489EDB2`
  and `5776ECE4968A63C70F9DB3BF93B97F0CA42AB456EC4A340EE3151AD85438EDC5`.
- Final English bounded build: 12 pages / 113,669 bytes / SHA-256
  `8E135AF1F53C653F5069EEDCC2C67775F54A6816F2205F5ACE1ADA2E02D95889`.
  Only physical page 5 changed; personal 600-dpi inspection confirms the clean
  unpunctuated diagram and continuing proof.
- Workflow ledger: 2 rows / 1,032 bytes / SHA-256
  `8ECD50DF0DB61519BB331C5C4BEA51591CC0FC0DDEDD375D9CD7D1388F8EA729`.
  It records the removed blank crop and a transient proposition trailing-space
  error caught before build. Final source/math effect is zero.
- Checkpoint R32: 10,719 bytes / SHA-256
  `188004628018FCA04FD5FE31A8A8E690908FA57195DE2B6A33042A81CAF1CFCD`,
  PASS/errors empty. Next cursor is printed p.110 after the diagram.

## 2026-08-02 -- EGA I printed p.110 and corrective p.109 diagram replay

- One direct NUMDAM p.110 authority image was generated at 1,100 dpi and
  inspected at original detail. It was sufficient for every formula and
  diagram feature; no detail crop and no OCR were used. Authority image:
  4,169,206 bytes / SHA-256
  `4C1037B02A54DD83833DAE25C9C2953478B49731C9311FCB8E500D7BDE2BF1DE`.
- Diplomatic French now covers the end of the 3.3.9 proof, formulas 3.3.9.1
  and 3.3.9.2, Corollary 3.3.10 and formula 3.3.10.1, Corollary 3.3.11 and its
  native diagram, and 3.3.12 through `u=v`. Seven stable targets were added.
  Source: 25,782 bytes / 567 lines / SHA-256
  `EBB451F8E44FF4382A351AD5F19A9D3C657E8F7AAEB9B340073D42BB126989C6`.
  Removing the p.110 block and reversing the three p.109 label-side encodings
  reproduces the exact p.109 source at 22,550 bytes / SHA-256
  `6C99E997042971815820CF5AF3145EB3E1EF37A8630538B61FB502F339FEBF09`.
- Lead error `EG-EGA-I-P110-WORKFLOW-DIAGRAM-SIDE-QA-MISS-001` is not hidden:
  the earlier p.109 review passed two diagrams whose bottom-row labels were on
  the wrong page side. Xy-pic's `^` and `_` are relative to arrow direction;
  for left-pointing arrows, the source-below labels require `^`. Direct
  p.109--p.110 comparison caught the error. French and English 3.3.6, 3.3.9,
  and 3.3.11 now render top labels above and bottom labels below as printed.
- English repair `EG-EGA-I-P110-EN-3311-DIAGRAM-MISSING-PSI-LABEL-001`
  restores the omitted `psi_(S')` on `Y_(S')->S'`. This is one actual
  mathematical-diagram fidelity repair. `...DIAGRAM-PERIOD-001` removes the
  source-invented period after the lower-right `X`. No author text was
  corrected on p.110.
- English source is 56,504 bytes / SHA-256
  `6196282B5900DB26B985B1E0E12385B7FA995F7807E8E43D833C0EB8CE8227F8`.
  Seven inverse operations reproduce R39 exactly at 56,491 bytes / SHA-256
  `E5E4C011C43B959AD95657C6B3B79612A0DB6D97A3B926A24A6F853E88861B8C`.
  Retained choices remain limited to justified modern terminology (`base
  change`) and explicit proof environments; neither changes mathematics.
- French decision ledger: 9 rows / 3,224 bytes / SHA-256
  `92EBEF4E44D3821B4D2F4320ADFB5A1C9890A63873BC6C7AEB9F74338CB62CEA`.
  English decision ledger: 7 rows / 2,844 bytes / SHA-256
  `2BCAF2978B4F893E66607AAD29ED95B0DB799E5E3A5350D26EC211EDAADE130D`.
  Workflow ledger: 4 rows / 1,810 bytes / SHA-256
  `04BF7B8B3B1D4889A544EB3D1C928406D701336ADB93762CAC1DF971A6AA24F0`.
  It also records a closed Poppler long-path failure and a harmless `pdfinfo`
  shim failure; neither changed source or evidence.
- R40 manifest: 127 files / 7,280,443 bytes / SHA-256
  `072C32119B3126F28C96BB6958FDDFA4A8E5F34B949E1E383F57C96D9D75FE00`;
  ordinal tree SHA-256
  `17CFEFE9E801D74857E235DD508E72F4C42AD0FB9EF123176E88EE499B26E215`.
  Section/full validation SHA-256 values are
  `6CFA4AF4D781237FEA638A7C75A5825D1598033EF2C4A2D3E2FF03472563844F`
  and `F5F37BBAACF6F350736B7E1E6C74BF8686931953FF8B331B501AD54393EDBEB1`.
- The final French bounded build is 22 pages / 227,511 bytes / SHA-256
  `04DAA9D0016A0D95C17CF68BF7468F9ACD2DD2B05EF0FBDB153A16B560B38D88`;
  changed pages 21--22 pass personal 600-dpi layout inspection. The final
  English bounded build is 12 pages / 113,708 bytes / SHA-256
  `5D4A01B13AB03D0B2D4203FB87C665CBB848B9B6AC05EAC5B1F89B1AC0C8F17A`;
  changed pages 4--5 pass personal 600-dpi layout inspection.
- Checkpoint R33: 11,587 bytes / SHA-256
  `66E00BE78EEB8B6B4E8E470C2DAFEC901274DC24B6E845FBE477BE2DB5034B76`,
  PASS/errors empty. The p.109 R32 diagram-layout claim is superseded, while
  its immutable source/text evidence remains historical. Next: remove the
  temporary 3.3.12 close and continue printed p.111.

## 2026-08-02 -- EGA I printed p.111 and paired English source-typo audit

- Direct authority: one 1,100-dpi whole-page image, 5,131,337 bytes / SHA-256
  `99A6F04973A211960FCD5C0E32724048708AF8743916AF632B8226FB721EE0D6`.
  The 3.3.12 codomain was the only genuinely ambiguous small feature. One
  successful tight 5,000-dpi direct crop, 354,780 bytes / SHA-256
  `B0D3F4A403E9F7BA470BABBFB57DB62D3538D1375333956A039695302D43B5D1`,
  proves that the printed letter is `Y`; no OCR was run.
- Diplomatic French adds the p.111 continuation of 3.3.12, all of
  3.3.13--3.3.15, the 3.4 heading, 3.4.1, and the opening of 3.4.2. Source:
  30,015 bytes / 654 lines / SHA-256
  `5C0481F52B66A1402C2B692B57F497B0CBEBE14763960CC43878CEEA7084F065`.
  Removing the p.111 continuation and restoring the p.110 temporary close
  reproduces 25,782-byte p.110 SHA-256
  `EBB451F8E44FF4382A351AD5F19A9D3C657E8F7AAEB9B340073D42BB126989C6`.
- Source-typo decision
  `EG-EGA-I-P111-FR-3312-BASECHANGE-TARGET-Y-VS-XPRIME-SRCTYPO-001`:
  preserve French `f_(S'):X_(S')->Y_(S')`. The same numbered statement begins
  `f:X->X'`, so its base change has codomain `X'_(S')`; no `Y` is introduced.
  English already used `X'_(S')`, so the only English source change there is
  an immediate visible disclosure note. This is one confirmed prior
  correction, not a new theorem or an unsupported normalization.
- Source-typo decision
  `EG-EGA-I-P111-FR-3315-MORPHISM-DIRECTION-SRCTYPO-001`: preserve French
  `Z[T]->X`. A section of `X tensor Z[T]` over `X` is a scheme morphism
  `X->X tensor Z[T]`; locally, contravariance gives precisely the printed ring
  maps `A_alpha[T]->A_alpha`. The English therefore uses `X->Z[T]` and gives
  an immediate visible source note. This is one newly applied mathematical
  source correction.
- Translation choices checked individually on this page: retain `prescheme`
  for historical `preschema`; render `morphisme graphe` as `graph morphism`;
  render `produit fibre` as `fibre product`; retain the reader's numbered
  environment structure. These choices change no object, arrow, hypothesis,
  or conclusion. Unsupported corrections reversed: zero. Lead false
  corrections caught: zero. Confirmed source corrections: two.
- French ledger: 10 rows / 3,694 bytes / SHA-256
  `1CEDDC361F0EC9409C888F6D3CF6442E8E671FD9465F06F96244FDF81D3CBA5E`.
  English ledger: 9 rows / 4,909 bytes / SHA-256
  `284BE03CE61DF450250344244E03E55E6B6EB6110AF5F593144C0F91EAE1636D`.
  Workflow ledger: 6 rows / 3,582 bytes / SHA-256
  `263C168F7D0655C61722E5607E019E038B7A51FA3E63FE7526ABA44F42A2ECF7`.
- Workflow mistakes are explicit, not hidden: two blank Poppler 5,000-dpi
  crop attempts were deleted before one tight PyMuPDF crop succeeded; two
  French builds failed because `\Hom` was absent from the diplomatic preamble
  before both sites were changed to `\operatorname{Hom}`; one direct long-path
  English Poppler call produced no PNG; and one ambiguously quoted XeLaTeX
  output-directory argument created only generated files under literal
  `source/$o`. That exact generated directory was verified and removed, its
  console was retained as adverse evidence, and no TeX source changed.
- One low-intensity helper read only the preceding control schemas. It made no
  source edit, build, render, OCR, hash pass, or source/math judgment. All
  transcription, correction, build, and visual decisions remained with the
  lead.
- R41 manifest: 127 files / 7,280,789 bytes / SHA-256
  `09EB142C493126469764AFEF70825EAF27FC1D7344BE5C422AA35D56AD953BCC`;
  exact ordinal tree SHA-256
  `4021B24BB11E6520EEC75F4748E75044FFDD2E14FB9733606DAD564650B26F33`.
  Section/full validation SHA-256 values:
  `68BFE818FA2F0F13F0E2438AEA6F639E4EA61379A0841C08C788942BD695BFBC`
  and `29A6313B09FED8E055CE6D3D5ED7E2928FDF2E4F31DE6C35862FF43D4D49DF30`.
- Final French bounded build: 23 pages / 234,431 bytes / SHA-256
  `13D29B451526DB13EE31A6DDCD2B904C8CDD759A2C56FEC8D6164F678751B538`;
  pages 21--23 personally pass sequential 600-dpi layout review. Final English
  bounded build: 13 pages / 115,301 bytes / SHA-256
  `5C2E0ACC6499CA45E330FB01C8A2F40C3C70DA3788B2C8DDC8311662EB22BB03`;
  reflowed pages 6--13 personally pass sequential 600-dpi layout review.
- Checkpoint R34: 12,101 bytes / SHA-256
  `7FBFDD83E08BC65055A19F18FEB29EED152777414894DBE6A4A6844668AA3AE3`,
  PASS/errors empty. Next: remove the temporary 3.4.2 close and continue
  printed p.112.

## 2026-08-03 -- EGA I printed p.112

- Direct authority remained NUMDAM EGA I, 31,680,717 bytes / 227 pages /
  SHA-256
  `9ABA23020217535977E279BDD06A0413F48DA703086865BA4C00766C85DF4AE6`.
  Reused one p.112 context image at 1,100 dpi, 2,428,045 bytes / SHA-256
  `57FDC1EFF2D7518381671863DA5C4EC7A0AE547CA51D852D8766B46FEFDBB3E8`,
  and generated one tight 1,800-dpi diagram crop, 63,797 bytes / SHA-256
  `8E18B69CEE5004BD71468F3A703A3C9C71E162B0555F5C2E01B761537841EFD3`.
  No OCR, image batch, agent, or parallel heavy job was used.
- Diplomatic French now completes 3.4.2, formula 3.4.2.1, 3.4.3 and formulas
  3.4.3.1--3.4.3.2, the native product diagram, 3.4.4, and 3.4.5 through the
  printed seam `la donnée de sa`. Current source: 33,565 bytes / 733 lines /
  SHA-256
  `F8C95EAD1820DC660F61AA52C163C23D5F60C2A0F234DC668029F2B35E9F9ACE`.
  Seven stable targets were added. French source corrections and unresolved
  readings are both zero.
- Two lead draft errors were caught before checkpoint admission. The first
  draft added punctuation after 3.4.2.1 although the source sentence continues
  in lower case; it also placed the lower `psi'` label above the lower product
  diagram arrow although the authority puts it below. Both were corrected
  before the final build. They remain explicit in the p.112 French ledger.
- Paired English recheck found the inherited lower `psi'` label-side mismatch
  in the same diagram. Repair
  `EG-EGA-I-P112-EN-343-PRODUCT-DIAGRAM-PSI-LABEL-SIDE-001` changes only label
  attachment/side; nodes, arrow direction, and mathematics are unchanged.
  Current English source: 56,850 bytes / SHA-256
  `EC3BB57090C0A12EF48CF9572B0EE933DE8E0759E1F51379A921528A6BB1142E`.
  New author-text corrections, unsupported reversals, and false author
  corrections are all zero.
- Retained English decisions are individually recorded: a grammatical comma
  after the continuing 3.4.2.1 display; established `fibre product`
  terminology; and literal `location` for `localité` with the existing visible
  modern clarification. None changes a mathematical object or dependency.
- French ledger: 10 rows / 3,185 bytes / SHA-256
  `6477D061CCA725F81914AB381BB62047E84DD016F693E2099B3C2A63DC416EB7`.
  English ledger: 7 rows / 2,356 bytes / SHA-256
  `37596E84ECD5F67543993B3CC9066ACC46B06B92FC4F27BB95B65A38C310A0FC`.
  Workflow ledger: 1 row / 1,382 bytes / SHA-256
  `062766517A7C9A59B75E0A66AB385042FCC053F22D8CB099993E49582E8F53FE`.
  The workflow record corrects the earlier crash description: a whole-page
  original-detail image load and an unbounded recursive Documents search both
  remain prohibited co-contributors; the search was not orderly cancelled.
- French bounded PDF: 24 pages / 239,546 bytes / SHA-256
  `D0D8A789017B3931C4B2255DA3700FEF47C167CD9DB3982EF1B010C8A0420160`.
  English bounded PDF: 13 pages / 115,253 bytes / SHA-256
  `A6742676640ADC895B1A24922B5119CDCFBBDE351F8EAEF35C9680BF27400D9E`.
  Changed pages pass personal serialized layout inspection.
- R35 validation: 5,090 bytes / SHA-256
  `2024E09325ECB75B7398699C954856DA99CC13DB130E242357CF870C31110B9F`,
  PASS/errors empty. The p.112 English file has not yet received a complete
  127-file R42 source manifest/diff replay; R41 remains the last fully sealed
  English tree checkpoint.
- Next cursor: remove the temporary final `\end{env}` from the French source
  and continue at NUMDAM PDF one-based p.112 / printed p.113, continuation of
  3.4.5.

## 2026-08-03 -- successor read-in and custody receipt

- Read completely and independently replayed handoff package
  `EGA_FRENCH_CANON_AND_ENGLISH_RECHECK_SESSION_HANDOFF_20260803_R1` and its
  self-excluding seven-row manifest `HANDOFF_SHA256SUMS.csv`, 715 bytes /
  SHA-256
  `444213EF6C150875FF2E3BC6224DD3C94DFBA869BF4D91E2417B6BE8D0631C25`.
  All seven package rows and all nineteen external bindings pass exact
  size/hash replay; `HANDOFF_BINDINGS.json` and `HANDOFF_VALIDATION.json`
  retain their bound identities and validation is PASS/errors empty.
- Verified French `source/ega1/ega1-3-fr.tex`: 33,565 bytes / SHA-256
  `F8C95EAD1820DC660F61AA52C163C23D5F60C2A0F234DC668029F2B35E9F9ACE`.
  Verified English `source/ega1/ega1-3.tex`: 56,850 bytes / SHA-256
  `EC3BB57090C0A12EF48CF9572B0EE933DE8E0759E1F51379A921528A6BB1142E`.
- Accepted cursor: NUMDAM EGA I PDF one-based p.112 / printed p.113,
  continuation of 3.4.5 after the exact French words `la donnée de sa`.
  Accepted sole-producer custody of the two live French and English EGA roots
  for canonical EGA 0--IV French/English completion and subsequent reader and
  semantic-index closure. Deligne, SGA, FAC, and GAGA are outside this scope.

## 2026-08-03 -- EGA I printed p.113 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.112 / printed p.113. The one
  new 1,100-dpi context image is 5,666,957 bytes / SHA-256
  `F59555950CB61D8BFF916078FCB4704728ECD0FAF3E37038B642CE53DCC10FC6`.
  It was inspected at resized high detail; no OCR, crop, batch render, or
  whole-page original-detail load was used.
- French 3.4.5 is complete, followed by Lemma 3.4.6, Proposition 3.4.7, its
  underlying-set consequence, and Corollary 3.4.8 through the displayed
  base-change equality. No source typo, unresolved reading, or diplomatic
  correction was found. Current `source/ega1/ega1-3-fr.tex`: 37,418 bytes /
  SHA-256
  `C457C0F47862A74CABBCEC04E9F5B91919DAE184C3DBBD61DF896FEF4D14EF15`.
  Removing the p.113 suffix reproduces the exact open p.112 source, and
  restoring its former temporary close reproduces the accepted handoff hash.
- Paired English repairs: `underlying subspace` became source-backed
  `underlying space`; additive `also` became inferential `thus` for French
  `ainsi`; and compiled cross-layer QA exposed an inherited p.112 citation to
  I.2.2.4. Direct p.112 visibly prints 2.4.4, and I.2.4.4 is the required
  local-scheme/local-homomorphism correspondence, so the English link is now
  I.2.4.4. This is a citation-target repair, not a correction to the authors.
  Current English source: 56,847 bytes / SHA-256
  `8D581435C0AC808A879B35C5805834A620BEF657898EAD308744C357B6E537F8`;
  three unique inverse operations reproduce R42 exactly.
- R42 first sealed the inherited p.112 tree: manifest 35,233 bytes / SHA-256
  `86A38A31C8FF069983DC42D61280666FF1045388162940C69CB05FAA57BC769A`;
  diff validation 4,227 bytes / SHA-256
  `9441A1FBCC35B84CE18AD2457673D8112F1EFFA663B87D705360FCB809FBA0B0`.
  R43 seals the final p.113 state: 127 files / 7,280,786 bytes, manifest
  SHA-256 `79DC085957FB058EB002014309BA1DB84FD8AC6E62690DA650FC43893699E62A`,
  canonical tree SHA-256
  `531CBD2815F995C97B1DEDFDE19B68CD93A045FD639D07DF103027969FA86A10`,
  and PASS diff validation SHA-256
  `1444F102061A03B68807713A8B119976D8A6E796204EE4D7216A74DE51820BDE`.
- Decision ledgers: French 8 rows / 2,816 bytes / SHA-256
  `0BD86C9C74EE8B91DF622C09722DCC5BE0C2063A12C283EFDB88A9C27C0C6EE9`;
  English 10 rows / 4,125 bytes / SHA-256
  `E24779EE120F21098A3D0FE81979B185554880DBF70784573050E64625B40681`;
  workflow 7 rows / 3,181 bytes / SHA-256
  `802D32C30B0F51198418A14FECCEA698E633534124DC320B31FF362D8AF9AC0F`.
- Final serialized French build r2: 24 pages / 244,482 bytes / SHA-256
  `ABD2CB513FAC8DEA62CF3E67227301F319EA4A935AA589292CA93AD984D0EFDE`.
  Physical page 24 passes 600-dpi inspection. The r1 wrong-working-directory
  failure is preserved as adverse evidence. Final English build r2: 13 pages /
  115,245 bytes / SHA-256
  `4FA5EF4EC8E04E6270E77731022D347B309CED67A74B73B5EBC4064C4AE58440`;
  physical pages 7--8 pass, with r2 page 8 pixel-identical to the inspected r1
  page. Both final logs have zero hard errors.
- R36 validation is 5,936 bytes / SHA-256
  `06D68E902E48B278C0AB683D1992FFE739104AE7B670D55FD316EDF22046FA30`,
  PASS/errors empty. The incremental p.112--p.113 semantic scaffold is 15,125
  bytes / SHA-256
  `5758D11A716CC6C79809B4812AA8378C7B570A1AC7AC986F70AB40270BBDD345`.
- Next cursor: NUMDAM PDF one-based p.113 / printed p.114, proof of Corollary
  3.4.8 beginning `En effet`. No temporary source close must be removed.

## 2026-08-03 -- EGA I printed p.114 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.113 / printed p.114. The one
  new 1,100-dpi context image is 4,817,920 bytes / SHA-256
  `D9D4AEC70FD58E62C26C28E9DD8712885CD76226211C4BECDC67C96F32FEDD51`.
  It was inspected at resized high detail; embedded PDF text was used only as
  a locator. No OCR, crop, batch render, whole-page original-detail load,
  unbounded search, or agent was used.
- French now completes the proof of Corollary 3.4.8 and its cartesian diagram,
  Proposition 3.4.9 and proof, opens subsection 3.5, and admits 3.5.1 clauses
  (i) and (ii). Current `source/ega1/ega1-3-fr.tex`: 41,097 bytes / 885 lines /
  SHA-256
  `9545DE0E3DB01EB04591FBD65F5CDB406530A28F906132E331531ADD0B0C76BE`.
  Removing the p.114 suffix reproduces the exact p.113 source. The final
  `\end{env}` is a temporary bounded page-seam close and is the only source
  text to remove before p.115 continuation.
- The printed proof of 3.4.9 calls the induced map
  `k(x) tensor_(k(s)) k(y) -> k(z)` a `monomorphisme`. Record
  `EG-EGA-I-P114-FR-349-TENSOR-MONOMORPHISM-SRCTYPO-001` preserves that wording
  in diplomatic French and catalogues it as a mathematical author-text error:
  the universal property supplies a homomorphism, while injectivity can fail
  (for example for the multiplication map `C tensor_R C -> C`). No source
  correction was applied to French; unresolved readings remain zero.
- Paired English recheck repaired only the side of the lower leftward `q`
  label in the 3.4.8 diagram, placing it below the arrow as printed. The
  inherited English `homomorphism` and its immediate visible translator note
  were retained as the confirmed correction of the author-text error; no new
  English mathematical wording changed. Current English source: 56,847 bytes /
  SHA-256
  `E6CAD01349ABDC5F3AEBA24356E9593C1D1BFC717038E9D35D99E267C9C5416B`.
  One unique inverse operation reproduces R43 exactly.
- R44 seals the final p.114 English tree: 127 files / 7,280,786 bytes,
  manifest 36,060 bytes / SHA-256
  `0574B3D851A04E1023F4D5BDE1D9D1717D9D644BD9EA93D542BF0CBE5950E10D`,
  canonical tree SHA-256
  `BBD421CCBEE4825695882D5C10BEBE12C3663B53D9D9A16F901490372168CB61`,
  and PASS diff validation 4,914 bytes / SHA-256
  `08201B423C2CFEA44F8649A4B2F0AF570B04B6E578717BA91905A0D679186778`.
  Independent replay found zero size/hash/order errors, one changed row
  (`ega1/ega1-3.tex`), and no added or removed rows.
- Decision ledgers: French 8 rows / 2,880 bytes / SHA-256
  `1FA7DC8F496486E7FEA2DDAE640FF05F11EC72D7725E01A164CC2AF9A95E386C`;
  English 8 rows / 2,981 bytes / SHA-256
  `199D5D35A057C7B4C3339CD0CFB61D24DBC38FBE59E6A68D1C5176A0DD605A05`;
  workflow/resource accounting 1 row / 380 bytes / SHA-256
  `98BFE2C2ADB515C194F8A753CA0D97CDF7424CD527DCE09148C200F5CA0CC2C2`.
- Final serialized French build: 25 pages / 250,775 bytes / SHA-256
  `B3BC332189B2A9A80D04603178136E6B41EEC71B2DA5B2E8C7818AB4C321E134`;
  physical pages 24--25 pass 600-dpi inspection and the p.113 forward
  reference to 3.4.9 is resolved. Final English build: 13 pages / 115,257
  bytes / SHA-256
  `2A131D38698F5BDEA731D22CA28FD157C4DD6C4C9164BE578757D1D8A387259D`;
  physical pages 8--9 pass 600-dpi inspection, including the corrected label
  geometry and visible source note. Both logs have zero hard errors.
- R37 validation is 7,090 bytes / SHA-256
  `C0575FC4F2215613939BC4657407D123370967A385B83E11229333D005CCFAE1`,
  PASS/errors empty. The incremental semantic scaffold is 16,933 bytes /
  SHA-256
  `8BC180ED04A848805C7D576FF424A0CFAB2E1472D3C44ADFCE0FA53117E75BF2`.
- Next cursor: remove only the temporary final `\end{env}`, then continue at
  NUMDAM PDF one-based p.114 / printed p.115, continuation of 3.5.1 after
  clause (ii).

## 2026-08-03 -- EGA I printed p.115 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.114 / printed p.115. The one
  new 1,100-dpi context image is 3,574,587 bytes / SHA-256
  `B83B678E23285A2181C3EAE1AFACFFE2A575CF2731B964FA927B6A3D0D521667`.
  Embedded PDF text was used only as a locator. No OCR, crop, batch render,
  whole-page original-detail load, unbounded search, or agent was used.
- French now completes 3.5.1, Proposition 3.5.2 and proof, Proposition 3.5.3
  and proof, Definition 3.5.4, and 3.5.5 through its displayed
  algebraic-closure diagram. Current `source/ega1/ega1-3-fr.tex`: 44,578 bytes /
  969 lines / SHA-256
  `FCDD412953CDC75797758BCF4FA29B42BF90B703D497D5AA70B83BE8DF8173ED`.
  Removing the p.115 suffix and restoring the p.114 close reproduces R37's
  French source exactly. The terminal `\end{env}` is a temporary bounded close
  for the p.115 seam; no source typo, correction, or unresolved reading was
  admitted.
- Paired English repair
  `EG-EGA-I-P115-EN-351-COMPOSITION-ANTECEDENT-001` restores the mathematical
  antecedent that both component morphisms possess property P before their
  composite is assumed to preserve P. Two prose repairs restore French
  `encore` as `further` and `aussitôt` as `immediately`; one diagram repair
  places `alpha-prime` below the lower rightward arrow. Current English source:
  56,894 bytes / SHA-256
  `AB5F2BBC7E3AD82C0DAF342BC0AD0B3012FCB219FC02F6AFDA7E0DB70C6B347B`.
  Four unique inverse operations reproduce R44 exactly. Confirmed
  author-text corrections and unsupported reversals are both zero.
- R45 seals the final p.115 English tree: 127 files / 7,280,833 bytes,
  manifest 36,487 bytes / SHA-256
  `DFD8BF3BD7A461608179190AAA5FF72AA5F345ECC46C3127D357BEC7B08088F8`,
  canonical tree SHA-256
  `45B3E3D362F2E4D5227E26BFE4CEAA5620176581466DBF9C83D6D26FC0EADE9C`,
  and PASS diff validation 5,100 bytes / SHA-256
  `903FF29D8B9EE60E69B9B523E6813C8F5F824BC6E63E7A7066F5A9DA4BE57198`.
  Independent replay found zero size/hash/order errors, one changed row, and
  no added or removed rows.
- Decision ledgers: French 9 rows / 2,970 bytes / SHA-256
  `A179EAE0861A2E5D8F44BC2C4E4C80EED196751D70D1B81AE72A21BB6FBB8173`;
  English 9 rows / 3,170 bytes / SHA-256
  `3B6BBFCAD53200981986716F6ECE945A9087ECFDA560643C33492B790A364E7D`;
  workflow 5 rows / 2,156 bytes / SHA-256
  `FA6FBD1248115669C08F103D8FF664A2D42AC3C11D6471CCEA4EE6F59CA52973`.
- Workflow failures remain explicit. The bundled `pdftoppm.cmd` could not find
  its path and produced no authority image; explicit MiKTeX `pdftocairo`
  succeeded with nonfatal legacy-font warnings. A variable-looking French
  XeLaTeX argument routed first-pass outputs into the pre-existing literal
  `qa/ega1_chapter1_build/$out` directory. Because it also contains earlier
  artifacts, it was left intact; two explicit-path passes produced the final
  build. Long English render paths failed twice without output, after which an
  unused temporary `Q:` mapping rendered pages singly and was removed.
- Final serialized French build: 26 pages / 255,527 bytes / SHA-256
  `0A610E2218F4AEC0F1529ADF7975E4927B54E30E8A215A7581308075A8C29AE1`;
  physical pages 25--26 pass 600-dpi inspection. Final English build: 13 pages /
  115,338 bytes / SHA-256
  `6798D38939861A320C7046601BA5DD2D6AE4F498CA914F4D84C191F86C3C5A1A`;
  physical pages 9--10 pass, including the repaired antecedent and
  `alpha-prime` label side. Both final logs have zero hard errors.
- R38 validation is 7,651 bytes / SHA-256
  `8D0C007424BBFAECD5F59CE33A25567EE6923C4A88D461BB87CE86ADA2496E1B`,
  PASS/errors empty. The incremental semantic scaffold is 19,149 bytes /
  SHA-256
  `1E1E6B1F6A0F224E687D9A9F759B9945D3AC5ADF51B633A44F862E0CFB6503D8`.
- Next cursor: remove only the temporary final `\end{env}`, then continue at
  NUMDAM PDF one-based p.115 / printed p.116 immediately after the 3.5.5
  diagram.

## 2026-08-03 -- EGA I printed p.116 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.115 / printed p.116. The one
  new 1,100-dpi context image is 4,186,083 bytes / SHA-256
  `2E1BF02C59C35317E12B8A2CDBD5265F0B135979F33D437CE186CCCD3647F62E`.
  Embedded PDF text was used only as a locator. No OCR, crop, batch render,
  whole-page original-detail load, unbounded search, or agent was used.
- The required first source action removed only the temporary p.115
  `\end{env}`. French now completes 3.5.5; admits Propositions 3.5.6--3.5.8,
  Corollary 3.5.9, and Corollary 3.5.10; and stops in the proof of 3.5.10 after
  the exact words `de la commutativité du diagramme`. Current
  `source/ega1/ega1-3-fr.tex`: 48,499 bytes / 1,059 lines / SHA-256
  `0B41FE7CCF850924D06C8F8BB2099555506985FCFF23A70CED2952C4AD7ED4EA`.
  Removing the p.116 suffix and restoring the former p.115 close reproduces
  R38's French source exactly. There is no temporary final environment close
  at the present seam; no source typo, correction, or unresolved reading was
  admitted.
- The paired English recheck found two omitted instances of French
  `aussitôt`. Repairs
  `EG-EGA-I-P116-EN-357-AUSSITOT-ADVERB-001` and
  `EG-EGA-I-P116-EN-3510-AUSSITOT-ADVERB-001` restore `immediately` in the
  conclusion of 3.5.7 and the first claim of 3.5.10. They change no
  mathematical claim, formula, dependency, or diagram. Current English
  source: 56,913 bytes / SHA-256
  `5A1EA6875D95D891D87381A288C33B7184B97A9343A982D82D353EB3DA03F2A6`.
  Two unique inverse operations reproduce R45 exactly. Confirmed author-text
  corrections, new English mathematical edits, and unsupported reversals are
  all zero.
- R46 seals the final p.116 English tree: 127 files / 7,280,852 bytes,
  manifest 36,969 bytes / SHA-256
  `37C59DE260A37EEB5D4542C3AF9FF71531CC01A6BE3450FAB280F0C1776BDC70`,
  canonical tree SHA-256
  `83506DB9F2EEE686B2E5A7DC2E72BEF4730A3CD42A2C04667F0955FA16779AAA`,
  and PASS diff validation 5,219 bytes / SHA-256
  `8FBD28F268EF1F8601F1F81A188B0D3FF674F5F64EA8F73881066EA9503B9083`.
  Independent .NET-ordinal replay found zero size/hash/order errors, one
  changed row (`ega1/ega1-3.tex`), a +19-byte delta, and no added or removed
  rows.
- Decision ledgers: French 9 rows / 2,898 bytes / SHA-256
  `32869B325C0FCF2B48CB3F3DB99D887B22A84BC741FF8E98C22D4F9C4F9D92D0`;
  English 7 rows / 2,091 bytes / SHA-256
  `357A58F459A72A72DD1198B188353D2A9EE2C306C2D2A2E264791E470797684C`;
  workflow 5 rows / 2,015 bytes / SHA-256
  `F2B86DBB70D6243F40D354F4C7635EECE2E578BC6BB88DC7FC3EF8C27E0AF96D`.
- Workflow receipts remain explicit. The direct-page render succeeded with
  nonfatal legacy-font warnings. The two long-path English QA pages were
  rendered singly through an unused temporary `Q:` mapping, removed in
  `finally` and independently confirmed absent. Two read-only metadata-query
  assumptions were corrected and had no source or artifact effect.
- Final serialized French build: 27 pages / 260,286 bytes / SHA-256
  `904FC054DFAF507D1D65ADCEC64338CF05F9C993D4856C231512CA0A9D2158D2`;
  physical pages 26--27 pass 600-dpi inspection, including the paired
  field-valued product formulas and the exact open proof seam. Final English
  build: 13 pages / 115,346 bytes / SHA-256
  `450AF97FBF4066D3DCB2A72447CA5CFAE11A3684BC9217F3EBF23AFDA8A1A20B`;
  physical pages 10--11 pass, with both `immediately` repairs visible in
  context. Both final logs have zero hard errors.
- R39 validation is 7,251 bytes / SHA-256
  `083D997689E74C8E7610C0894F978E643753D73DCCA4D8BB61B1FBA17A72339A`,
  PASS/errors empty. The incremental semantic scaffold is 21,422 bytes /
  SHA-256
  `9E7E9E3BC767EF53322683BE9775B25995F8C163293804ECE9A2EB5D9C82C3EE`.
- Next cursor: append directly at NUMDAM PDF one-based p.116 / printed p.117,
  beginning with the diagram that completes the proof of 3.5.10. There is no
  temporary source close to remove.

## 2026-08-03 -- EGA I printed p.117 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.116 / printed p.117. The one
  new 1,100-dpi context image is 4,087,846 bytes / SHA-256
  `5190145A707154F1BCFD1841A0933CB53FDE850BC7E8A01FAE7E7FCBE700E0FC`.
  Embedded PDF text was used only as a locator. No OCR, crop, batch render,
  whole-page original-detail load, unbounded search, or agent was used.
- French completes the proof diagram for 3.5.10, adds Remark 3.5.11, opens
  subsection 3.6, admits Proposition 3.6.1 and convention 3.6.2, and carries
  3.6.3 through its displayed fibre-composition identity. Current
  `source/ega1/ega1-3-fr.tex`: 52,851 bytes / 1,156 lines / SHA-256
  `DF4B43CE4A6D15D2C0295DFBF173A00ABC998A98C38AEE127E76AF9593D35153`.
  Removing the p.117 suffix reproduces the p.116 source byte-for-byte. The
  terminal `\end{env}` is a temporary bounded close for the p.117 seam; no
  source typo, correction, or unresolved reading was admitted.
- The paired English recheck restores one omitted sequencing cue in Remark
  3.5.11: `the condition first implies` now preserves French `d'abord`.
  Existing fibre-product notation, the explicit 3.6.1 proof boundary, and the
  terminal period after the page-seam display are individually retained as
  reader-facing normalizations. Current English source: 56,919 bytes /
  SHA-256
  `6CCAAE5D05343975ABD6E68B1265525DDCA2C3F7C4A8D25987649DE73DD6C2AC`.
  One unique inverse operation reproduces R46 exactly. Confirmed author-text
  corrections, new English mathematical edits, and unsupported reversals are
  zero.
- R47 seals the final p.117 English tree: 127 files / 7,280,858 bytes,
  manifest 37,432 bytes / SHA-256
  `E8C29077CDC78DFB6A7F8A5544F3199F9E5564F64163B10FFC0047B21FC14E8B`,
  canonical tree SHA-256
  `FA3CD639E1DC14145A9270C641F99F1D3FEF399EE96BFB40CC6B8ACD0F35E6E7`,
  and PASS diff validation 5,135 bytes / SHA-256
  `A4E877FFFF87ECE878AFDD93BA29D2C2B4A48527D344B533AF40AF992FF2F5F1`.
  Independent .NET-ordinal replay found zero size/hash/order errors, one
  changed row with a +6-byte delta, and no added or removed rows.
- Decision ledgers: French 9 rows / 2,859 bytes / SHA-256
  `470A9BB81B7C3A8328334DBBD3D4DB86AC685BA799CE7E17214BE8A93FC3CCB6`;
  English 7 rows / 2,235 bytes / SHA-256
  `F56EF628800F8D06BB6F667F6F84F113170845AB3FE779C52F220EE900C5A77C`;
  workflow 6 rows / 2,550 bytes / SHA-256
  `A3E5BC823F9F391B47CEAA82A1AFCCC1BE575E3B4BE68AF5EC96CB2960659AD4`.
- Workflow receipts include the nonfatal legacy-font warnings, one harmless
  read-only PowerShell parser correction, the successfully removed temporary
  `Q:` mapping, and a rejected malformed multi-file patch that changed no
  file. The pre-seal semantic audit then added the non-rendering
  `I.3.6.1.localization-fraction-fr` anchor and triggered the final French-only
  rebuild; diplomatic text and English R47 were unchanged.
- Final serialized French build: 27 pages / 265,378 bytes / SHA-256
  `A41C256BC56DA3705B8DCFC20DD8818010A78B496536C8547F62D9CD9D0581F2`;
  physical page 27 passes 600-dpi inspection and is pixel-identical before and
  after the semantic-anchor addition. Final English build: 13 pages / 115,351
  bytes / SHA-256
  `32D71EB8A3CC7E7406F68993AF868F9D250DD5A667065769A90AD2E46E56B00E`;
  physical page 11 passes with the `first` repair visible in context. Both
  final logs have zero hard errors.
- R40 validation is 7,122 bytes / SHA-256
  `F35A37B89CB1DEE40A79D0C4E7AA708A006B608C166B153E241E2FB662A6464E`,
  PASS/errors empty. The incremental semantic scaffold is 23,632 bytes /
  SHA-256
  `8CDC91D268F39F44BD76FE972F32A067556F0161003180537E7B788F00039FCA`.
- Next cursor: remove only the temporary final `\end{env}`, then continue the
  same 3.6.3 paragraph at NUMDAM PDF one-based p.117 / printed p.118
  immediately after the displayed fibre-composition identity.

## 2026-08-03 -- EGA I printed p.118 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.117 / printed p.118. The one
  new 1,100-dpi context image is 4,376,825 bytes / SHA-256
  `52AA3CF4FB2291B552721C56316EEE5B769BBFDBBA9A514FFF720575653D95B1`.
  Embedded PDF text was used only as a locator. No OCR, crop, batch render,
  whole-page original-detail load, unbounded search, or agent was used.
- The required first source action removed only the temporary p.117
  `\end{env}`. French now completes 3.6.3, admits titled Proposition 3.6.4 and
  Proposition 3.6.5, opens subsection 3.7 with its printed footnote, admits
  3.7.1, and carries 3.7.2 through the exact words `l'unique point`. Current
  `source/ega1/ega1-3-fr.tex`: 57,071 bytes / 1,241 lines / SHA-256
  `2EDB68A378FE6C959B048180148FF7E69E42916D261F92207A24DA793B120192`.
  Removing the p.118 suffix and restoring the former p.117 close reproduces
  R40's French source exactly. The final `\end{env}` is a temporary bounded
  close for 3.7.2; no source typo, correction, or unresolved reading was
  admitted.
- The paired English recheck repairs the scope of the subsection footnote:
  `from later in Chapter I and from Chapter II` now preserves French `de la
  suite du chap. Ier et du chap. II`. The change restores forward-reference
  scope but no mathematical claim, formula, object, or map. Current English
  source: 56,933 bytes / SHA-256
  `55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`.
  One unique inverse operation reproduces R47 exactly. Confirmed author-text
  corrections, new English mathematical edits, and unsupported reversals are
  zero.
- R48 seals the final p.118 English tree: 127 files / 7,280,872 bytes,
  manifest 37,933 bytes / SHA-256
  `309B5B0A48AC2F3AD8903891526D8722ECB2C64C5CF18F5293F398BF89B58668`,
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
  and PASS diff validation 5,402 bytes / SHA-256
  `FE9746CE8BB49D3DF2F96D9EBF9B49AE67B8EEBFD61FD79FAC972AEDA31D4373`.
  Independent .NET-ordinal replay found zero size/hash/order errors, one
  changed row with a +14-byte delta, and no added or removed rows.
- Decision ledgers: French 11 rows / 3,406 bytes / SHA-256
  `6C12A8E3CF22505B602B24191546455A9B6C493BFE9887646B4BF373400E6AB3`;
  English 8 rows / 2,686 bytes / SHA-256
  `3C330E230922DA8C1D40095CE823D7129F80A52DECD0742F8E18348B3C475976`;
  workflow 6 rows / 2,643 bytes / SHA-256
  `7E6D1E754282AD8E3AF955D19210901B09B0124567FA4FEF77C8D952B176C60D`.
- Workflow receipts include nonfatal legacy-font warnings, the first French
  build's repaired PDF-string warning, the removed temporary `Q:` mapping, a
  rejected malformed ledger patch that changed no file, and the corrected
  p.118 scaffold block order. The final French title uses a visual/bookmark
  split; the complete footnote is attached and readable. The bounded wrapper
  uses its standard Arabic marker rather than the printed parenthesized marker,
  a recorded cumulative-reader styling concern.
- Final serialized French build: 28 pages / 272,098 bytes / SHA-256
  `9AA2E9A7A387F1881BC861C0AED7CCBD9BDADA9F2F558F6A3E45005375536DD0`;
  physical pages 27--28 pass 600-dpi inspection, including the pre-dash 3.6.4
  title, complete footnote, and exact p.118 seam. Final English build: 13 pages
  / 115,362 bytes / SHA-256
  `28A75B6834B4151C5CA9CF4FD2C475CA4F809CA8E267CE7EF58113B1E9643689`;
  physical page 12 passes with the repaired forward scope visible. Both final
  logs have zero hard errors; the clean French log has zero PDF-string
  warnings.
- R41 validation is 7,161 bytes / SHA-256
  `40CE9BF9A4180940D00ACA2E0A69BA3D3F51CF059F9BFD037D26B4A7D83AEF7A`,
  PASS/errors empty. The incremental semantic scaffold is 26,214 bytes /
  SHA-256
  `9D9639133E63266DE00366015BE03AA840F05C998B07D12DBE9A87AB7EC481D5`.
- Next cursor: remove only the temporary final `\end{env}`, then continue
  3.7.2 at NUMDAM PDF one-based p.118 / printed p.119 after the exact words
  `l'unique point`, beginning `fermé y=\mathfrak{J}`.

## 2026-08-03 -- EGA I printed p.119 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.118 / printed p.119. The one
  new 1,100-dpi context image is 4,453,245 bytes / SHA-256
  `98313EF45F7C1C17800DB643DB2652715FD3B80FEF59F6239E25C67B0BB0B31D`.
  Embedded PDF text was used only as a locator. No OCR, crop, batch render,
  whole-page original-detail load, unbounded search, or agent was used.
- The required first source action removed only the temporary p.118
  `\end{env}`. French now completes 3.7.2 and 3.7.3 in
  `source/ega1/ega1-3-fr.tex`, 59,766 bytes / 1,282 lines / SHA-256
  `DB4F986C9FDC1B66FF2D627C5E9121BCE0490563B7C14415320B5DDD7424B851`.
  The canonical section boundary then creates `source/ega1/ega1-4-fr.tex`,
  1,292 bytes / 29 lines / SHA-256
  `BEDC1B141252E20EE298389D39C3B9C38D9403E08AF57F5ED53CD25BB115916F`,
  containing section 4, subsection 4.1, 4.1.1, and the complete statement of
  Proposition 4.1.2. No temporary environment close is present. Two inverse
  operations reproduce the sealed p.118 French source and its SHA-256
  `2EDB68A378FE6C959B048180148FF7E69E42916D261F92207A24DA793B120192`.
  Source corrections, catalogued p.119 typos, and unresolved readings are
  zero.
- The paired English recheck confirms the remainder of 3.7.2, all of 3.7.3,
  and section 4 through Proposition 4.1.2 without changing a source byte.
  `ega1-3.tex` remains 56,933 bytes / SHA-256
  `55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`;
  `ega1-4.tex` remains 33,365 bytes / SHA-256
  `55FCE2B2C9A51F7FC86DCEB1A8E0BD4EC6E06818C28E302FFE045B4CA323B275`.
  The explicit `Theorem` and `Corollary` reference types in 4.1.1 and the
  p.120 proof environment remain documented reader-facing normalizations.
- R49 seals the unchanged English tree: 127 files / 7,280,872 bytes,
  manifest 38,368 bytes / SHA-256
  `0BB20AFE664720F711F04AEC55D88E96DA918C27C26DF26FE6D60A7AE8838E8C`,
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
  and PASS diff validation 5,564 bytes / SHA-256
  `519B2CBC2EA3FCB9FCCCD3F4FB85907776DAD1D260F48BE86E6ED3D888B82031`.
  Independent ordinal replay found zero size/hash/order errors and zero
  changed, added, or removed rows from R48; inverse-operation count is zero.
- Decision ledgers: French 12 rows / 4,175 bytes / SHA-256
  `FBCADAE7530EEB787FEC60A6A8421E181DF72ADF4DF1B3F04460D0DD2CF2CBFC`;
  English 10 rows / 2,808 bytes / SHA-256
  `9F4E34AF1CF73A748A760C67F8BD30C6B5B63E36053B9DA770F9F7477EAA4FDB`;
  workflow 14 rows / 5,720 bytes / SHA-256
  `77B4C54E3939752892E24135D39139599A467A23CFD7F157CB1C80E89EAEC607`.
- Workflow receipts preserve the Windows-glob and guessed-name read-only
  corrections, the new French wrapper boundary, inherited build warnings,
  native long-path render fallback, guarded and removed temporary `Q:`
  mapping, the English bounded-wrapper section-counter repair, the corrected
  p.119 scaffold order, and two harmless PowerShell metadata corrections.
  None changed diplomatic wording or the English source tree.
- Final serialized French build: 29 pages / 276,883 bytes / SHA-256
  `CB39695477CB9CE1791569D358BE74EBAC2B733F317E92C33DDE497D4225E0AF`;
  physical pages 28--29 pass 600-dpi inspection and the final log has zero
  hard errors and zero PDF-string warnings. Final English build: 13 pages /
  117,660 bytes / SHA-256
  `985FC4F4B0A5BD7E6FA236CDC9AC17720A7FAF34D6859C28DF504E2C1F2F82DA`;
  physical page 13 passes after the wrapper-only counter repair. Its two
  PDF-string warnings are inherited from the section 3.7 title and do not
  affect the printed p.119 content.
- R42 validation is 8,838 bytes / SHA-256
  `B82C5D63AF34111BBE4D94700582770A36CFF1A005E76C8C088E960421DE83CC`,
  PASS/errors empty. The incremental semantic scaffold is 28,571 bytes /
  SHA-256
  `0AE321FFE5B0BAC6450650738F8E088EDF6EB282BF70ACE313D50DCEFEFD220D`,
  with exactly one p.119 block after p.118.
- Next cursor: append directly to `source/ega1/ega1-4-fr.tex` at NUMDAM PDF
  one-based p.119 / printed p.120, beginning the proof of Proposition 4.1.2
  with `Il suffit évidemment`. There is no temporary close to remove.

## 2026-08-03 -- EGA I printed p.120 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.119 / printed p.120. The one
  new 1,100-dpi context image is 4,526,764 bytes / SHA-256
  `6A978EC28596239DDFEDD191E02DEB3A0149A5C62B34DD69205F7AA6408C8DA7`.
  Embedded PDF text remained locator-only. No OCR, crop, batch render,
  whole-page original-detail load, unbounded search, or agent was used.
- French now completes the proof of 4.1.2, the subprescheme terminology,
  Definition 4.1.3, the canonical closed-subprescheme/ideal-sheaf bijection,
  4.1.4, Proposition 4.1.5 with proof, and the open induced-prescheme
  consequence. Proposition 4.1.6 opens and stops at the exact printed seam
  `d'un sous-`. `source/ega1/ega1-4-fr.tex` is 5,966 bytes / 118 lines /
  SHA-256
  `90C1D93784F8A1817702732BE9E69B513F9D538A4F878688894D131F24F20B71`;
  `ega1-3-fr.tex` remains 59,766 bytes / SHA-256
  `DB4F986C9FDC1B66FF2D627C5E9121BCE0490563B7C14415320B5DDD7424B851`.
  One temporary final `\end{proposition}` balances the p.120 checkpoint.
  Truncation from the extra LF before the unique p.120 marker through EOF
  reproduces the sealed p.119 section-4 source exactly at 1,292 bytes /
  SHA-256
  `BEDC1B141252E20EE298389D39C3B9C38D9403E08AF57F5ED53CD25BB115916F`.
  Source corrections, catalogued typos, and unresolved readings are zero.
- The paired English recheck retains every source byte. `ega1-3.tex` remains
  56,933 bytes / SHA-256
  `55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`;
  `ega1-4.tex` remains 33,365 bytes / SHA-256
  `55FCE2B2C9A51F7FC86DCEB1A8E0BD4EC6E06818C28E302FFE045B4CA323B275`.
  Explicit proof environments, proof-reference type words, and the English
  whole-word p.121 marker remain documented reader-facing normalizations.
- R50 seals the unchanged English tree: 127 files / 7,280,872 bytes,
  manifest 38,864 bytes / SHA-256
  `D6F7AFA347FD3B0B3D63E310394D0D3CE9D77AF57F26C44A9C3FE189C98D43A8`,
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
  and PASS/errors-empty diff validation 6,347 bytes / SHA-256
  `988292B9754053803D7AEDDD1817D95A7543D6A1361F806F91BC2C29E1DD4FC0`.
  Independent ordinal replay found zero size/hash/order errors and zero
  changed, added, or removed rows from R49.
- Decision ledgers: French 12 rows / 4,107 bytes / SHA-256
  `8850E167FAD0DCCC4FD868AC93E0F996CF28C7B7E491FDA7BD47CCF8D43B834E`;
  English 13 rows / 3,669 bytes / SHA-256
  `48EA6332507CFC53013C67985A89E876E773448D8753E490352E34A4F749B7E6`;
  workflow 11 rows / 4,253 bytes / SHA-256
  `4CFA1980B9D7A926667D08D631524DFB28BB4F0BC92FB9B81A370429EA687215`.
  All recorded command corrections were read-only and changed no source.
- Final serialized French build: 29 pages / 281,746 bytes / SHA-256
  `2ADC022DE0787263913EBEC8BD06BDDDE5706B480AC059C2354C126E5519B871`;
  physical page 29 passes 600-dpi inspection and the log has zero hard errors
  and zero PDF-string warnings. Final English build: 14 pages / 122,887 bytes
  / SHA-256
  `172F4C958CEFE1BAA310557229E6F73D0FEB58A3462A6BA8634A1296BA2546F8`;
  physical page 14 passes inspection. Its two PDF-string warnings are
  inherited from the section 3.7 title. Temporary `Q:` is absent.
- R43 validation is 9,149 bytes / SHA-256
  `4721AB517C81B0770246C1F1CC1A4FF1C579FB50A0392A767E83DD9B51F5EF20`,
  PASS/errors empty. The incremental semantic scaffold is 31,358 bytes /
  SHA-256
  `10A3797A83CEB208428817E4D9F3EED3B27B54F72EF6CAA727EC3C8FB887BEB6`,
  with exactly one p.120 block at true EOF after p.119.
- Next cursor: first remove only the temporary final `\end{proposition}`
  from `source/ega1/ega1-4-fr.tex`, then continue Proposition 4.1.6 from
  direct NUMDAM PDF one-based p.120 / printed p.121 authority after the exact
  p.120 hyphenation `d'un sous-`.

## 2026-08-03 -- EGA I printed p.121 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.120 / printed p.121. The one
  new 1,100-dpi context image is 4,515,600 bytes / SHA-256
  `466CF45909A29FEAA5AAD19DB13F1BEE4C898C1D82A4AB1A89CA7FA4525EEFD7`.
  Embedded PDF text remained locator-only. No OCR, crop, batch render,
  whole-page original-detail load, unbounded search, or agent was used.
- The required first source action removed only the temporary p.120
  `\end{proposition}`. French now completes 4.1.6 and its proof, records the
  standing identification convention, completes 4.1.7 and 4.1.8, states
  Proposition 4.1.9, and admits its proof through the exact words
  `est un morphisme Z\to Y`. `source/ega1/ega1-4-fr.tex` is 10,356 bytes /
  203 lines / SHA-256
  `52A11F6F8AFE416C5D1999C463FE328060F3E1009BB14E0781A636C6761C6169`;
  `ega1-3-fr.tex` remains 59,766 bytes / SHA-256
  `DB4F986C9FDC1B66FF2D627C5E9121BCE0490563B7C14415320B5DDD7424B851`.
  No temporary environment close is present. One inverse replacement restores
  the sealed p.120 section-4 source exactly at 5,966 bytes / SHA-256
  `90C1D93784F8A1817702732BE9E69B513F9D538A4F878688894D131F24F20B71`.
  Source corrections, catalogued typos, and unresolved readings are zero.
- The paired English recheck retains every source byte. `ega1-3.tex` remains
  56,933 bytes / SHA-256
  `55C1E1129E40F1E2F8DB7B46867B3E49AE2556F04C1CFE1FBF5EE3C149B63BD9`;
  `ega1-4.tex` remains 33,365 bytes / SHA-256
  `55FCE2B2C9A51F7FC86DCEB1A8E0BD4EC6E06818C28E302FFE045B4CA323B275`.
  Whole-word page placement, explicit proof environments, the retained
  translator note on `majoré`, and English `g` for French `g'` remain fully
  documented reader-facing normalizations.
- R51 seals the unchanged English tree: 127 files / 7,280,872 bytes,
  manifest 39,418 bytes / SHA-256
  `F6736445D6C310C85A5FA44E5B718C71EC6B6574DCC28CFF1BD8AD673EBF46A8`,
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
  and PASS/errors-empty diff validation 6,385 bytes / SHA-256
  `8E0A9E1AD4122E6320D288A3CDE75D7262C4608FEB2D7983ADBD2101FAE6C6BC`.
  Independent ordinal replay found zero size/hash/order errors and zero
  changed, added, or removed rows from R50.
- Decision ledgers: French 13 rows / 4,503 bytes / SHA-256
  `E2F5CDB0D21E6AEA0E52CB184868FDCE1EDD6249AE87D88E1F2583CC88A75CB0`;
  English 11 rows / 3,332 bytes / SHA-256
  `DBF5BDEE551BE26F11A15F8456BC5AEDAAC089EE09A443A223A25AEEAA15A93D`;
  workflow 12 rows / 4,982 bytes / SHA-256
  `2431D227B193C56F583A0637A87EF1AC28B7AE9F7A88ABBD90E0B8323715F23A`.
- The first French build passed a PowerShell variable literally and retained
  a superseded 25-file / 1,466,519-byte diagnostic under
  `qa/ega1_chapter1_build/$out`. It also exposed the now-obsolete forward
  placeholder for `I.4.1.7-fr`. The final p.121 wrapper equals the p.119
  wrapper minus only that placeholder; source bytes were never affected.
- Final serialized French build: 30 pages / 287,123 bytes / SHA-256
  `220A7280A4420D338E9A910B4A971E2357DEB62390F4E61DE018738AFDDEC732`;
  physical pages 29--30 pass 600-dpi inspection and the log has zero hard
  errors, zero PDF-string warnings, and zero duplicate-label warnings. Final
  English build: 14 pages / 128,025 bytes / SHA-256
  `148D326B436272E09B8C644CD29F1F05064517B4B02EC6006220935D04A43472`;
  physical page 14 passes inspection. Its two PDF-string warnings are
  inherited from the section 3.7 title. Temporary `Q:` is absent.
- R44 validation is 9,607 bytes / SHA-256
  `16F74B50E79D3AFF7373FB8104C9507FC028D7E151523550C8165ACC3D668EF8`,
  PASS/errors empty. The semantic scaffold is 33,979 bytes / SHA-256
  `45E213E7BB074993A9D405333A9E9D88A7E96C0A35CB4A60271B3EA373E4D8FC`,
  with exactly one p.121 block at true EOF after p.120.
- Next cursor: append directly to `source/ega1/ega1-4-fr.tex` from direct
  NUMDAM PDF one-based p.121 / printed p.122 authority, continuing the proof
  of Proposition 4.1.9 after the morphism `g':Z\to Y`. There is no temporary
  close to remove.

## 2026-08-03 -- EGA I printed p.122 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.121 / printed p.122. The one
  new 1,100-dpi context image is 4,084,576 bytes / SHA-256
  `AA56A3CA45D405ACC6699DC7E139A72643B204715E5FA3E1FEEEB799383AB4D4`.
  Embedded PDF text remained locator-only. No OCR, crop, batch render,
  whole-page original-detail load, unbounded search, or agent was used.
- French completes the proof of 4.1.9, Corollary 4.1.10 and the order
  notation, Definition 4.2.1, Proposition 4.2.2, and its proof through the
  exact terminal words `restriction à $U$ de l'image`.
  `source/ega1/ega1-4-fr.tex` is 14,467 bytes / 285 lines / SHA-256
  `984EFEEB45E09398B9B1E0E7DAB3602D89119F2AC2A860A19872CFEC0494992E`;
  `ega1-3-fr.tex` remains 59,766 bytes / SHA-256
  `DB4F986C9FDC1B66FF2D627C5E9121BCE0490563B7C14415320B5DDD7424B851`.
  The final `\end{enumerate}` is temporary. One inverse truncation at byte
  10,356 restores the sealed p.121 source and SHA-256
  `52A11F6F8AFE416C5D1999C463FE328060F3E1009BB14E0781A636C6761C6169`.
- Printed proof 4.2.2(a) reverses the source and target of
  `\theta^\sharp`, saying it is an isomorphism from `\mathscr O_Y` onto
  `\psi^*(\mathscr O_X)`. Canonical French preserves and catalogues this
  single printed mathematical error; no French correction is silently
  applied. The inherited English gives the typed direction from
  `\psi^*(\mathscr O_X)` to `\mathscr O_Y` and displays an explicit
  translator footnote. No English source byte changed.
- R52 seals the unchanged English tree: 127 files / 7,280,872 bytes,
  manifest 40,084 bytes / SHA-256
  `B2BCA961EEE011D9E5F03147CD696F9888D96E6A58F944DD1A2ED6FB292EE614`,
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
  and PASS/errors-empty diff validation 6,974 bytes / SHA-256
  `75B3BC2A7E09CDDBCBAEA5D558E9F37095FA4052C908330323F43F2D50A2AF4D`.
  Independent ordinal replay found zero size/hash/order errors and zero
  changed, added, or removed rows from R51.
- Decision ledgers: French 15 rows / 5,366 bytes / SHA-256
  `A8D9FC8079316E875620EBF5FCEB842A68B0F14CD38B0C5F117090DBAE24E0EF`;
  English 11 rows / 3,731 bytes / SHA-256
  `DF71BFA7B1FBF4F72D40E469AF4916C5DE9743944C1EBCB096A938F563B35AC5`;
  workflow 11 rows / 4,231 bytes / SHA-256
  `0E7D40B3BB0A586606DE20CF181043610C8EA8062FA7CEB8F1E7B8606C7F132B`.
- Final serialized French build: 31 pages / 291,778 bytes / SHA-256
  `3B5CF6685A40A87632D6B6A269669504A62EB540D6205E022173EE3239BBD5E4`;
  physical pages 30--31 pass 600-dpi inspection and the log has zero hard
  errors, zero PDF-string warnings, and zero duplicate-label warnings. Final
  English build: 15 pages / 133,594 bytes / SHA-256
  `D4EF20AEA2BC89EF7924C5B42870B64DE05F5E6F6AE39B8D2D66E67C566E676C`;
  physical pages 14--15 pass inspection. Its two PDF-string warnings and two
  overfull boxes are inherited diagnostics. Temporary `Q:` is absent.
- R45 validation is 10,598 bytes / SHA-256
  `B188DC15970531829D52CDC27BEC574A7DC056E05C5BCB9814F326657C680B14`,
  PASS/errors empty. The semantic scaffold is 36,912 bytes / SHA-256
  `520C8428973418FB38435D536B621B48918E14168F4FEC6D86C1E9A0D351812B`,
  with exactly one p.122 block at true EOF after p.121.
- Next cursor: first remove only the temporary final `\end{enumerate}` from
  `source/ega1/ega1-4-fr.tex`, then continue from direct NUMDAM PDF one-based
  p.122 / printed p.123 authority after `restriction à $U$ de l'image`.

## 2026-08-03 -- EGA I printed p.123 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.122 / printed p.123. The one
  new 1,100-dpi context image is 4,233,219 bytes / SHA-256
  `91F7D24B15E1C76360049B11212C7284F87F3DAEC9366C4CEAD3B91C3DA721DF`.
  Embedded PDF text remained locator-only. No OCR, crop, batch render,
  whole-page original-detail load, unbounded search, or agent was used.
- French completes Proposition 4.2.2(b), including the stalk diagram,
  quotient-sheaf factorization, and affine-open gluing; states Corollary
  4.2.3; and admits Corollary 4.2.4(a) through the exact words `il faut et il
  suffit`. `source/ega1/ega1-4-fr.tex` is 18,980 bytes / 365 lines / SHA-256
  `B75325670BDB54B9B6F17AF3945110A86E2506F3EF41A699FE3032B5B5EEFACC`;
  `ega1-3-fr.tex` remains 59,766 bytes / SHA-256
  `DB4F986C9FDC1B66FF2D627C5E9121BCE0490563B7C14415320B5DDD7424B851`.
  The final `\end{enumerate}` and `\end{corollary}` are temporary. One
  inverse suffix replacement restores the sealed p.122 source at 14,467
  bytes / SHA-256
  `984EFEEB45E09398B9B1E0E7DAB3602D89119F2AC2A860A19872CFEC0494992E`.
- An initially context-free close removal matched the earlier 4.1.3
  delimiter. The immediate hash/environment check caught it before
  continuation; the delimiter was restored, the exact p.122 hash was
  reconfirmed, and the EOF close was then removed with unique context. The
  erroneous intermediate SHA was
  `4D98F5500D825DA4CEBDBC5F3E7AF635BC7EEAC14ED825993346106C48EF7656`;
  it has no remaining effect. No French source correction, new printed-source
  error, or unresolved reading was introduced on p.123.
- The paired English recheck retains every source byte. R53 seals 127 files /
  7,280,872 bytes, manifest 40,442 bytes / SHA-256
  `A66887EBE9AA70959C970051C08550FD8A4DE525CD78D23A21662B4C75F18ED5`,
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
  and PASS/errors-empty diff validation 7,465 bytes / SHA-256
  `465F8FE2D3DC7B10BA4CC74792B81A8BD65B51FD29C03B37B0AD2495F5979DD9`.
  Independent replay found zero size/hash/order errors and zero changed,
  added, or removed rows from R52. The p.122 theta correction is carried, not
  counted as a new p.123 correction.
- Decision ledgers: French 11 rows / 4,572 bytes / SHA-256
  `F38B6C8452650F4879CACD9B14C92EDB3C93A589F90F5FC475C84EE3AF1B4233`;
  English 9 rows / 2,991 bytes / SHA-256
  `F948EE8915F1F1CE7A1C1A6352A13D4F218B6A084F36678DA3E9A20C12822321`;
  workflow 15 rows / 6,495 bytes / SHA-256
  `E2DC27D9F1A1EEC4E569AE7099334370BA2FA931E43FFDAEAC9E93F0BA5FCC8A`.
- Final serialized French build: 31 pages / 297,263 bytes / SHA-256
  `E52987A1F74065FE13BE9177DE04E7DBFD0B00D456D1212397DE9AA4A59AC6E7`;
  physical page 31 passes inspection, and page 30 exactly replays its sealed
  p.122 render hash. The log has zero hard errors, zero PDF-string warnings,
  and zero duplicate-label warnings.
- The first English live-marker wrapper did not terminate within the bounded
  runtime; the sole surviving XeLaTeX PID was identity-checked and stopped.
  Its four incomplete files / 105,879 bytes remain as superseded evidence.
  The replacement 189-line projection has 187 lines exactly equal to live
  `ega1-4.tex` lines 18--204 and two balancing closes. Final English build:
  16 pages / 139,048 bytes / SHA-256
  `892949ADB0BED5773CC14933B0CCD79860D21FBA1501CC9639A61DC835B6C24E`;
  physical pages 15--16 pass inspection. No XeLaTeX process or `Q:` mapping
  remains.
- R46 validation is 10,743 bytes / SHA-256
  `859AE56FAFA479F12F68B1080E61100CD9B0F2C750DFA9041774516BC3CDF20C`,
  PASS/errors empty. The semantic scaffold is 39,471 bytes / SHA-256
  `FEA8C2EF710D19870D963162F269DBF3AEE10059C94C26B595B4C812659940BA`,
  with exactly one p.123 block at true EOF after p.122.
- Next cursor: first remove only the temporary final `\end{enumerate}` and
  `\end{corollary}` from `source/ega1/ega1-4-fr.tex`, then continue from
  direct NUMDAM PDF one-based p.123 / printed p.124 authority after `il faut
  et il suffit`.

## 2026-08-03 -- EGA I printed p.124 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.123 / printed p.124. The one
  new 1,100-dpi context image is 4,297,349 bytes / SHA-256
  `DBA58C282E3CF63EA81EF4C57669371DC063F9BCD34A54BB9F60D08E01F1EA31`.
  Embedded PDF text remained locator-only. No OCR, crop, batch render,
  whole-page original-detail load, unbounded search, or agent was used.
- French completes Corollary 4.2.4 and its proof, states Proposition 4.2.5,
  opens subsection 4.3 and Proposition 4.3.1, and admits its proof through
  the exact terminal phrase `la restriction de $\alpha\times_S\beta$`.
  `source/ega1/ega1-4-fr.tex` is 23,239 bytes / 440 lines / SHA-256
  `E9061031DB90102A99851D0397A879CCF422F50A820F8C2A30AF30E222CC9185`;
  `ega1-3-fr.tex` remains 59,766 bytes / SHA-256
  `DB4F986C9FDC1B66FF2D627C5E9121BCE0490563B7C14415320B5DDD7424B851`.
  No temporary final environment close is present. One inverse suffix
  replacement restores the sealed p.123 source at 18,980 bytes / SHA-256
  `B75325670BDB54B9B6F17AF3945110A86E2506F3EF41A699FE3032B5B5EEFACC`.
  No French source correction, new printed-source error, or unresolved
  reading was introduced on p.124.
- The paired English recheck retains every source byte. R54 seals 127 files /
  7,280,872 bytes, manifest 40,800 bytes / SHA-256
  `9A53F6C16D4DD5D366696988C95321DCE2062E1010CF981526C7233296F541A4`,
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
  and PASS/errors-empty diff validation 7,092 bytes / SHA-256
  `BA53F085977613E2ABA88B3CF943837204E3BBB9A9C2D1EFF80D59891EA8B43C`.
  Independent replay found zero size/hash/order errors and zero changed,
  added, or removed rows from R53. The p.122 theta correction is carried, not
  counted as a new p.124 correction.
- Decision ledgers: French 10 rows / 3,623 bytes / SHA-256
  `8C1E0029C8EC3D8BC8494999CEE99A63F55236D72B9B906BD236E4A2D589DCDF`;
  English 10 rows / 2,954 bytes / SHA-256
  `979851360743216CD781D3F08CC0174EFA8E3B0A6498DB5C8515FFD6A4AFB988`;
  workflow 16 rows / 6,560 bytes / SHA-256
  `B4765811FDBA57F5747F249A1249DDAA0290F20E20E5E54757063B11BE7D9493`.
- Final serialized French build: 32 pages / 302,104 bytes / SHA-256
  `E9524E042DFC8936359BE9C6AECF3BA24943CB25E8EB0F3BBF7F147C326CE25B`;
  physical pages 31--32 pass inspection, and the log has zero hard errors,
  zero PDF-string warnings, and zero duplicate-label warnings. Final English
  build: 17 pages / 144,319 bytes / SHA-256
  `5BF1482C1EB63A89EAADB179DEB06C10B4F88D49116C462AB46C919AECAC17E1`;
  physical pages 16--17 pass inspection. Its two PDF-string warnings and two
  overfull boxes are inherited diagnostics.
- Pre-build verification corrected an over-escaped balancer in the English
  QA projection without touching live source. Immediate ordering checks also
  moved the single p.124 semantic block from two intercepted broad-anchor
  placements to true EOF after p.123. Read-only metadata/parser corrections
  and long-path retries are fully logged; no XeLaTeX process or `Q:` mapping
  remains.
- R47 validation is 10,336 bytes / SHA-256
  `49BAFE90DBC08F35258F8C1AB4C3B476971B3B9B5359667B8C9D0564CC4E6A54`,
  PASS/errors empty. The semantic scaffold is 41,558 bytes / SHA-256
  `DC976E9D55C245D37001098D466B3AA3AC1DD594C8BB3051EE49F75C28DA52BF`,
  with exactly one p.124 block at true EOF after p.123.
- Next cursor: append directly from NUMDAM PDF one-based p.124 / printed
  p.125 authority, continuing Proposition 4.3.1 after `la restriction de
  $\alpha\times_S\beta$`. Do not remove any environment delimiter first.

## 2026-08-03 -- EGA I printed p.125 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.124 / printed p.125. The one
  new 1,100-dpi context image is 4,462,107 bytes / SHA-256
  `B1C2D6C0BD2C5538DC3E65EF64304E7CBFD6B6D936ADEB6319826F2D833B8616`.
  Embedded PDF text remained locator-only. No OCR, crop, batch render,
  whole-page original-detail load, unbounded search, or agent was used.
- French completes the proof of Proposition 4.3.1, states Corollary 4.3.2,
  opens subsection 4.4, states and proves Proposition 4.4.1, and admits the
  inverse-image terminology through the exact terminal phrase `qui s'accorde
  avec celle introduite`. `source/ega1/ega1-4-fr.tex` is 27,679 bytes /
  522 lines / SHA-256
  `E26B5510C2DF88911C36C57755D6D5AAF6EF23174C9B30DA70BB95FC6A955FA2`;
  `ega1-3-fr.tex` remains 59,766 bytes / SHA-256
  `DB4F986C9FDC1B66FF2D627C5E9121BCE0490563B7C14415320B5DDD7424B851`.
  No temporary final environment close is present. One inverse suffix
  truncation restores the sealed p.124 source at 23,239 bytes / SHA-256
  `E9061031DB90102A99851D0397A879CCF422F50A820F8C2A30AF30E222CC9185`.
  No French source correction, new printed-source error, or unresolved
  reading was introduced on p.125.
- The paired English recheck retains every source byte. R55 seals 127 files /
  7,280,872 bytes, manifest 41,158 bytes / SHA-256
  `2C76ACD405EDA12EF0D89A89FFF7388410B770F4940C9F55EC8476859218E165`,
  canonical tree SHA-256
  `E8331E55DEABD57007298B17012BE1E50C20370837535F413F3679EBE3FB646B`,
  and PASS/errors-empty diff validation 7,453 bytes / SHA-256
  `38C475CFA262D891E3747AFF0FF517E3E81602ADBFA733131602F30B6F412A31`.
  Independent replay found zero size/hash/order errors and zero changed,
  added, or removed rows from R54. The p.122 theta correction is carried, not
  counted as a new p.125 correction.
- Decision ledgers: French 11 rows / 3,818 bytes / SHA-256
  `77247C08974DD7B0C34B75E16B9FFCB08B509BCB23127A47BA6E7C8521227814`;
  English 10 rows / 2,897 bytes / SHA-256
  `5BF77F44C13123E01245F52C2F44C6046120FFC6B8973B6BB7E3D1709F40E068`;
  workflow 13 rows / 5,113 bytes / SHA-256
  `6C43336E861955435F203EAA89EA40E4F53B9B7FC9274748380E35115B93612E`.
- Final serialized French build: 32 pages / 307,609 bytes / SHA-256
  `859CFDB406BE148825CE270EC587A01C90490B2434A371BF8F36E1C45A2CBF9E`;
  physical page 32 passes inspection, and the log has zero hard errors, zero
  PDF-string warnings, and zero duplicate-label warnings. Final English
  build: 18 pages / 150,482 bytes / SHA-256
  `27703818224457A02D4AB5C0C69B919FAE515324520F7A40293FEEB08130996E`;
  physical pages 17--18 pass inspection. Its two PDF-string warnings and two
  overfull boxes are inherited diagnostics.
- Two rejected or misplaced semantic-scaffold anchors, one flawed read-only
  EOF expression, and one wrong manifest-replay base were caught by immediate
  controls, fully logged, and corrected before sealing. They changed no live
  source byte. No XeLaTeX process or `Q:` mapping remains.
- R48 validation is 10,341 bytes / SHA-256
  `0B5B2C235F4E2166F5A15F084A4B8FC9592EA7426D2CB663EB916DBDAD9CA1F0`,
  PASS/errors empty. The semantic scaffold is 43,753 bytes / SHA-256
  `405FE80C84B9DABB9CB0B7994B1C3E564D2C16FACAFB55FD653FD813425F1CB8`,
  with exactly one p.125 block at true EOF after p.124.
- Next cursor: append directly from NUMDAM PDF one-based p.125 / printed
  p.126 authority, continuing the inverse-image terminology after `qui
  s'accorde avec celle introduite`. Do not remove any environment delimiter
  first.

## 2026-08-03 -- EGA I printed p.126 diplomatic and paired-English checkpoint

- Direct authority: NUMDAM EGA I PDF one-based p.125 / printed p.126. The one
  new 1,100-dpi context image is 5,448,546 bytes / SHA-256
  `7ADA8D9A25FCFAC30112DBD4744EB192F32BA63F7FD80500DEA9B063173C1DDA`.
  Embedded PDF text was used only as a locator. No OCR, crop, batch render,
  whole-page original-detail load, unbounded search, or agent was used.
- French completes the inverse-image terminology, its identity-factorization
  and closed-point-fibre consequences, Corollaries 4.4.2--4.4.4,
  Proposition 4.4.5, Corollary 4.4.6, subsection 4.5, Definition 4.5.1, and
  Definition 4.5.2 through the exact terminal phrase `un isomorphisme local
  en`. `source/ega1/ega1-4-fr.tex` is 31,712 bytes / 619 lines / SHA-256
  `96BA0D70ADCFA3758DEBB25113B8AE0CA71CCC8D4CE12C1FBBFA8CECBF75D1A7`.
  Its final `\end{definition}` is temporary. One inverse suffix truncation
  restores p.125 exactly at 27,679 bytes / SHA-256
  `E26B5510C2DF88911C36C57755D6D5AAF6EF23174C9B30DA70BB95FC6A955FA2`.
- The diplomatic source preserves and catalogues one new officially
  evidenced printed mathematical error in 4.4.5: French says `B est une
  A-algèbre` but then forms `A\otimes_B(B/\mathfrak K)`; the typed
  statement requires (A) to be a (B)-algebra. English retains its visible
  `Err` list-II correction. The prior p.122 theta-direction error remains
  carried. No French correction was silently applied.
- Direct comparison caught and fixed two lead transcription deviations before
  build: plural `isomorphes` was restored to printed singular
  `isomorphée`, and the second `quasi cohérent` in 4.4.5 was restored
  without a hyphen. No unresolved reading remains.
- The paired recheck also found one inherited English formula omission in
  Corollary 4.4.6. The live criterion now reads
  `f^*(\sh{K})\sh{O}_X\subset\sh{J}`. English `ega1-4.tex` is 33,373
  bytes / SHA-256
  `CE8036FF9EF584DD794C7D4925EA62FE7937229E57212873B1C25DE68F8715A5`;
  one unique inverse restores the R56 file at 33,365 bytes / SHA-256
  `55FCE2B2C9A51F7FC86DCEB1A8E0BD4EC6E06818C28E302FFE045B4CA323B275`.
- R57 seals the repaired English tree: 127 files / 7,280,880 bytes, manifest
  41,920 bytes / SHA-256
  `A8C6D3E4AA6E478CBFCD1A144C6460D9DF03195C09758C713C9CC4C0048739A1`,
  canonical tree SHA-256
  `C22FBDE03D3833584E83A448F5BB74B51399798C4B1E1C82769659211DCAE1E2`,
  and PASS/errors-empty diff validation 8,647 bytes / SHA-256
  `421DC3016B112F2CD3E1CA92A3E7C76E4FA438B44C83B05C98CD280048C251B5`.
  Independent replay found exactly one changed row from R56,
  `ega1/ega1-4.tex`, and zero added or removed rows.
- Decision ledgers: French 17 rows / 6,054 bytes / SHA-256
  `1458690D9E8040A6D7AF74482CDBED91C16503DF5AE8273F2C4E168F5BEA57A5`;
  English 15 rows / 5,172 bytes / SHA-256
  `A4F7CB99DD848E81EB82EC772FF65DDD9F8F5CE8DA6039EA95A43C03E3FF780C`;
  workflow 21 rows / 10,805 bytes / SHA-256
  `4F508B34BE1E897DE19669F85C7783AA25A463DBCCAB66C275BB1605D2DD2153`.
- Final serialized French build: 33 pages / 313,109 bytes / SHA-256
  `E9E0486B63CAD646E6C961B6435919FFA00C47A2022C30A5668757FA4F1EBB8A`;
  physical pages 32--33 pass inspection, with zero hard errors, PDF-string
  warnings, or duplicate labels. Final repaired English build: 19 pages /
  156,047 bytes / SHA-256
  `D3B4CA5FC24BE58C62C3E602953E6FE78AF20B7AA7B39834364228DD6AD5E534`;
  physical pages 18--19 pass inspection and visibly contain both `Err₂`
  and the restored (\mathscr O_X). Its two PDF-string warnings and two
  overfull boxes are inherited.
- Renderer-wrapper, argument-tokenization, metadata long-path, and display
  retries are fully logged. The pre-repair English build is retained only as
  detection evidence and excluded from final claims. No XeLaTeX process or
  `Q:` mapping remains.
- R49 validation is 12,000 bytes / SHA-256
  `98501091AB4641EEAFB20F2FFC7E25225189C2A2784E3EDE0AEA7773F1E19DE9`,
  PASS/errors empty. The semantic scaffold is 47,731 bytes / SHA-256
  `4DB40D004F016D16BB620A61C11F2F963EA4629B647618769C74AFE4EEE025CA`,
  with exactly one p.126 block at true EOF after p.125.
- Next cursor: remove only the temporary final `\end{definition}`, then
  continue Definition 4.5.2 from NUMDAM PDF one-based p.126 / printed p.127
  authority after `un isomorphisme local en`.

## 2026-08-03 -- full source-thread reread, scope correction, and production hold

### Audit receipt and reason for the hold

- The complete source-task conversation `[PRIVATE_TASK_376B7BA66C40]`
  was reread back to its origin, including the initial task attachment and all
  later instructions, corrections, reversals, handoffs, resource incidents,
  release discussions, and user objections. The initial attachment
  `pasted-text.txt` is 7,946 bytes / 132 lines / SHA-256
  `356EE7288EB4C60CF8732E67D1DF9E22AAA7748F28834AFD9CD847427E8F8E7D`.
  It explicitly requires bilingual source work plus preparatory
  machine-readable indexing: stable identities for mathematical units,
  formulas, diagrams, terminology, and dependencies are first-class corpus
  records, not optional hyperlink polish.
- The successor handoff package
  `EGA_FRENCH_CANON_AND_ENGLISH_RECHECK_SESSION_HANDOFF_20260803_R1` was read
  again in its mandatory order through the current EOF of every live file, not
  merely through the package's historical p.112 tails. Its self-excluding
  `HANDOFF_SHA256SUMS.csv` independently replays 7/7 rows with zero errors,
  715 bytes / SHA-256
  `444213EF6C150875FF2E3BC6224DD3C94DFBA869BF4D91E2417B6BE8D0631C25`.
  `HANDOFF_BINDINGS.json` remains 10,242 bytes / SHA-256
  `72E871E74D3AFF94FBD263B5E3FB6C4D1D024079339FF9F820E3FCC849B856C9`;
  `HANDOFF_VALIDATION.json` remains 1,247 bytes / SHA-256
  `12D1D7CA5D3FC86E9A24121E9724CA02B6ADEBA7085C9C4B2653EAD00C2C67FF`.
  The validation is an immutable PASS for the acceptance-time p.112 state, not
  a claim about today's advanced live bytes. Of its 19 external paths, all 19
  still exist, 11 immutable/historical paths still match exactly, and eight
  mutable source/status/log/scaffold paths have advanced under the accepted
  successor. The earlier acceptance receipt at the p.112 boundary records the
  successful 19/19 creation-time replay. The current mismatch is expected
  succession, not handoff corruption.
- The prior durable goal was deleted because it omitted the explicit
  pre-Stacks/Stacks scaffold. That omission materially narrowed the requested
  deliverable and was wrong. `get_goal` confirms that no durable goal is active
  during this audit. Production is held until the corrected objective is
  recorded below in the project logbooks and installed as the active goal.
- Pre-append identity of this logbook: 328,459 bytes / 5,260 lines / SHA-256
  `01DE43C345E6F0341218423B4005981859CCAA7F6F0064FE3C1B0119F46F43F1`.
  Removing only this appended audit block must reproduce that predecessor.

### Corrected corpus scope and terminal deliverables

- “EGA 0--IV” in this project means the complete canonical diplomatic French
  corpus for the eight bounded NUMDAM publications EGA I, EGA II, EGA III-1,
  EGA III-2, and EGA IV-1 through IV-4. Chapter 0 is carried inside the EGA I
  publication and is not a ninth publication. The terminal condition is the
  complete corpus, not a sample, pilot, chapter fragment, or link-only layer.
- For every remaining source unit, direct NUMDAM page imagery is the textual
  authority. Canonical French remains diplomatic: preserve printed wording,
  notation, punctuation, order, and authorial errors, with only reversible TeX
  representation. Catalogue source defects; never silently repair them in the
  French layer. Existing OCR, extraction, inherited English, and earlier
  transcriptions are locator/comparison witnesses only.
- Recheck the paired English against the same direct authority after the
  French reading is established. Keep ordinary idiomatic translation within
  the declared English editorial role, but give every functional departure,
  retained correction, notation normalization, source-error correction,
  rejected candidate, and later reversal its own stable, source-bound,
  concise rationale. Mathematical corrections require immediate visible
  disclosure. Repair every active standalone and cumulative/global source copy
  carrying a reversed decision; record exact inverses and successor IDs rather
  than overwriting history.
- Keep the standalone readers for their bounded publications and the
  cumulative/global English reader co-current with the final French/English
  source generations. After sources stabilize, regenerate the applicable
  readers, compile serially, validate references and layout in proportion to
  the actual change, and close exact source/manifests for the final generation.
- Maintain and complete the bilingual machine-readable pre-Stacks scaffold as
  a named deliverable throughout production. Required semantic records include
  volumes, chapters, sections, numbered and unnumbered units; definitions,
  conventions, remarks, examples, propositions, lemmas, corollaries, theorems,
  and proofs; formulas, exact sequences, diagrams, tables, and notes; named
  objects and constructions; explicit hypotheses and conclusions; parent and
  scope relationships; terminology and notation bindings; and source-error,
  normalization, official-erratum, reversal, and repair provenance.
- Give dependencies typed edges, including proof-use, definition-use,
  comparison, forward pointer, range, cross-volume, and external citation.
  Stable IDs must survive line and byte movement and must anchor French slices,
  English targets, formula/diagram identities, ambiguity state, provenance,
  review method, and confidence. During source work, add the cheap,
  source-certain nodes and explicit edges. At meaningful cumulative checkpoints
  and after the canonical source freeze, regenerate the complete target/edge/
  residual graph, exhaustive reference audit, subject/formula/terminology
  indices, final coordinates, and implication/dependency closure. Then deepen
  the existing graph into the requested Stacks-style reconstruction; do not
  misrepresent the preparatory scaffold as already-completed Stacks exposition
  or formalization.
- The controlling scaffold is currently
  `EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_20260802.md`, 47,731 bytes /
  SHA-256
  `4DB40D004F016D16BB620A61C11F2F963EA4629B647618769C74AFE4EEE025CA`.
  The handoff's 12,419-byte / SHA-256
  `00782C23C1DE78EBCC58A4C75BF424BA926CB99A4CB25BE6083B2383FE8D40E4`
  scaffold binding is its historical p.112 generation; the live file has
  advanced append-only through p.126.
- Final closure includes privacy-clean chronological logbooks, per-decision
  ledgers, reversal/error history, authority/cursor records, exact manifests,
  rights and caveat statements, package/handoff identities, and public
  readback when an archive action is separately authorized. Bind frozen
  privacy-clean logbook surfaces into both methodology concept DOI
  `10.5281/zenodo.21124403` and replication concept DOI
  `10.5281/zenodo.20461174`. Do not upload mutable work or perform any archive,
  GitHub, or Zenodo mutation without explicit authority. Do not duplicate the
  already-completed standalone EGA IV archive handoff.
- Deligne, SGA, FAC, and GAGA are explicitly outside this goal. Their history
  supplied operating lessons during the transcript reread, but no source,
  reader, index, package, or archive work for them belongs in this objective.

### Transcript lessons adopted as controlling operating rules

- Preserve completed, validated work. Do not blanket-recheck an already closed
  range without a concrete discrepancy, stale binding, unresolved witness, or
  required final cumulative replay. Do not quarantine or replace a sound
  generation merely to redo work; when provenance or task/model identity is
  genuinely wrong, quarantine it explicitly and never merge it silently.
- Keep adverse history and blame precise. Distinguish authorial error,
  inherited translation error, lead source/translation judgment, rejected
  pre-admission candidate, tooling error, and workflow/resource error. A
  reversal is append-only and closed only after every active copy and derived
  gate has been repaired and replayed. Never invent totals by adding
  overlapping queues or malformed historical CSV rows.
- Use ordinal path order for manifests and state the implemented algorithm.
  Culture sorting, JSON/list-order hashing mislabeled as ordinal, stale
  validators, and approximate inverse substitutions are prohibited. Preserve
  wrong controls as superseded evidence and issue no-overwrite successors.
- Exact per-instance decisions and page cursors remain continuous, but do not
  turn every small page unit into a release-scale audit. Capture page-local
  rationales, reversible edits, cursor state, and cheap semantic anchors;
  reserve exhaustive global builds, coordinate replay, privacy projection,
  package closure, and complete graph regeneration for meaningful cumulative
  or final checkpoints. Report candidly when a layer is only drafted,
  unsealed, bounded, or pending; never use “complete”, “canonical”, “sealed”,
  “source-certified”, or “released” beyond the exact layer proven.
- Work sequentially and RAM-light. Reuse exact witnesses before generating
  anything. No new OCR; no unbounded recursive filesystem search; no batch
  authority rendering or bulk image loading; no whole-page original-detail
  load. Ordinary context is approximately 1,100--1,400 dpi only when a reusable
  witness is absent; create at most one tight higher-resolution crop for a
  genuine small ambiguity. Serialize builds and compile only after real source
  edits. Agents, if any, are limited to two or three bounded, disjoint,
  low-intensity mechanical tasks and may not decide source, mathematics,
  translation, or visual fidelity or launch render/OCR/build/audit swarms.
- Put inter-task notes, controls, and continuation records in the actual
  counterpart work root, not merely in an origin task's private directory.
  Privacy checks must detect dewrapped private paths as well as visibly wrapped
  ones. Do not duplicate frozen candidates, handoffs, transports, or archive
  records.

### Exact live hold state after the reread

- P.126 is the last sealed checkpoint. P.127 work exists but is deliberately
  unsealed: French `source/ega1/ega1-4-fr.tex` is 34,793 bytes / 682 lines /
  SHA-256
  `9775A6A8EA2AC2415CCE4DC64EEA356382ECED4F06C59FB67C602C6C7ED6F0C1`;
  new `source/ega1/ega1-5-fr.tex` is 681 bytes / 17 lines / SHA-256
  `E4893706A6EFAEB40D74BECC0FFA3C7E32A1FB3FCA64374CC4B6F9EDCD17163C`;
  English `source/ega1/ega1-4.tex` is 33,644 bytes / 413 lines / SHA-256
  `C933CDFEB1C7F64B0BFFB8D510A732349B196E3E53B8044A70098D999CAB1BF8`.
  The three p.127 decision/workflow ledgers exist, but no p.127 checkpoint
  validation, STATUS closure, or LOGBOOK production entry exists. Do not
  promote this draft or infer a sealed next cursor until its existing work is
  audited and closed under the corrected goal.
- Current English manifest R59 is 42,723 bytes / SHA-256
  `3D874D60FA7AB1CE4C0A0496BD20C3B096481E0A35463D851ACD295CCBD08569`.
  An independent .NET-ordinal replay returns 127/127 rows, 7,281,151 source
  bytes, zero row errors, and exact canonical tree SHA-256
  `BF73FCED73F50B5A18F310A4206EC14955E1DC8512BD50DC6847BCE60A19005D`.
  This proves the current source manifest only; it does not seal p.127 or
  replace the missing decision/build/status/logbook closure.
- No source, reader, scaffold, build, render, OCR, or archive mutation was made
  during this corrective reread. Work performed was limited to complete file/
  transcript reading, exact hashes, bounded current-state inspection, and
  read-only control replay. The next mutation after this receipt is the
  replacement durable goal itself; production remains held for explicit
  handoff after the goal and logbook receipts are reported.

## 2026-08-03 -- paired French/English closure, EGA I printed p.127

- The previously unsealed draft was audited against the retained direct
  NUMDAM context image, 5,482,731 bytes / SHA-256
  `06AC22100F50F42481383B13DF8763E6635EDC024D580B49ECD9CC10DE0EFA3C`.
  No OCR, new authority render, agent, or whole-page original-detail load was
  used. The draft French and inherited English content required no source-text
  rewrite during this audit.
- French completes Definition 4.5.2, 4.5.3, Proposition 4.5.4 and proof,
  Proposition 4.5.5 and proof, opens section 5 and subsection 5.1, and admits
  the complete Proposition 5.1.1 statement through `de B.`. Current
  `ega1-4-fr.tex` is 34,793 bytes / SHA-256
  `9775A6A8EA2AC2415CCE4DC64EEA356382ECED4F06C59FB67C602C6C7ED6F0C1`;
  new `ega1-5-fr.tex` is 681 bytes / SHA-256
  `E4893706A6EFAEB40D74BECC0FFA3C7E32A1FB3FCA64374CC4B6F9EDCD17163C`.
  Truncating at the unique p.127 marker, restoring the predecessor's temporary
  `end-definition`, and removing the new file reproduces p.126 exactly.
- Direct authority confirms two printed defects in proof 4.5.5. The cited
  transitivity target is printed as `(4.2.4)` although the typed proposition
  is `(4.2.5)`; the product proof also uses `z,z'` without introducing them.
  Diplomatic French preserves both. English retains the typed citation and
  necessary point introduction, each with an immediate translator footnote.
  Removing the unique 119-byte and 152-byte notes reproduces the exact R58
  English source at 33,373 bytes / SHA-256
  `CE8036FF9EF584DD794C7D4925EA62FE7937229E57212873B1C25DE68F8715A5`.
- R59 independently replays 127/127 source files / 7,281,151 bytes with zero
  row, membership, size, hash, or ordinal-order error and canonical tree
  SHA-256
  `BF73FCED73F50B5A18F310A4206EC14955E1DC8512BD50DC6847BCE60A19005D`.
  The one-row R58--R59 validator is PASS/errors empty at 7,763 bytes / SHA-256
  `C68E010B34CF050695FCDC5AC8A1AC5F405A4AC05661A0558979214547426C73`.
- The p.127 pre-Stacks block adds durable nodes for 4.5.2--4.5.5, both source
  errors, section 5, subsection 5.1, and 5.1.1; it records bilingual slice
  hashes and typed proof/definition/error edges. The scaffold is 51,566 bytes
  / 887 lines / SHA-256
  `5DD244CCB3A223D0EEDB67E233027A1A338ACD24232C7639023723F8B98BACBC`.
- The retained source-current French build is 34 pages / 317,866 bytes /
  SHA-256
  `CF636F3492F8B81E34BD5E4417393071F3910EDE1AEEA0CDAFB627179606F25E`;
  physical pages 33--34 pass review. The settled English build is 19 pages /
  161,909 bytes / SHA-256
  `E344A519B0DDC19DF372296FA1829FBBCAE0BEC68EDDE4FD0A60BCB60A938BD6`;
  physical page 19 passes review with both notes visible. Hard errors are zero.
  Inherited diagnostics are one French overfull box plus bounded undefined
  references, and two English PDF-string warnings, two overfull boxes, plus
  the bounded undefined-reference summary.
- The first English compile placed only temporary products under literal
  `source/$out`; their hashes are retained in the workflow ledger and that
  verified directory was removed. Long-path text/render retries likewise had
  no source effect. The successful one-page render used a temporary `Q:`
  mapping, removed immediately. No XeLaTeX process remains. All nine workflow
  entries are preserved at SHA-256
  `690C10C16475C0EF16DB8DB0FDAD2046FB7BB7657798BD557E61ACD0258FAB61`.
- R50 combined validation is PASS/errors empty at 11,010 bytes / SHA-256
  `D631DC20C4EF98C822AA61FF29A02176382A23E40077C1D36338FE359E80EA25`.
  Next paired cursor: NUMDAM PDF one-based p.127 / printed p.128, proof of
  Proposition 5.1.1. No temporary French close must be removed.

## 2026-08-03 -- paired French/English closure, EGA I printed p.128

- Direct authority was NUMDAM PDF one-based p.127 / printed p.128. The single
  retained 1100-dpi context image is 5,716,880 bytes / SHA-256
  `904A5A63F91442AF11B11CE2F8E6F1B68523D92D9C254813BA6197BA1A045EA2`.
  It was reviewed directly without OCR or an original-detail whole-page load.
- French completes the proof of 5.1.1, establishes nilradical terminology,
  admits Corollary 5.1.2 and proof, Definition 5.1.3, Proposition 5.1.4 and
  proof, the locally integral consequence/converse, and begins 5.1.5 through
  exact `l'homomor-`. `ega1-5-fr.tex` is 5,091 bytes / 103 lines / SHA-256
  `EB37539C7AAD273C7A780E087FDB8863CD86A0C284D0BA532B72D395FC5860A0`.
  The p.128 marker slice is 4,409 bytes / SHA-256
  `EF33E8767B2A9209D26CBF9C98CF24D563F0A3C333C53299FC92273C94C1989D`;
  truncation to 681 bytes restores p.127 exactly. The final `end-env` is a
  temporary page-seam close and must be removed before p.129.
- French diplomatically preserves the printed 5.1.2 word-order error placing
  `Y` after `défini`. English retains its inherited grammatical resolution.
  The paired recheck makes exactly two source changes: remove the erroneous
  stalk subscript from the ideal in `I subset j_x`, and replace the defining
  `thus implies` with `thus means`. Current English `ega1-5.tex` is 46,829
  bytes / SHA-256
  `D3BB566847A24BD268157D7171BD9F5B282FA2C9B8F4D1A1ABD9B84F656FEFF3`;
  two unique inverse substitutions reproduce exact R60 at 46,833 bytes /
  SHA-256
  `1585EC164F57E55BA86264F86F428523D7659442AAE5046D43D9E5FA49B5F777`.
- R61 independently replays 127/127 source files / 7,281,147 bytes with zero
  row, membership, size, hash, or ordinal-order error and canonical tree
  SHA-256
  `658ACB58DBE08F3641410EF071EBA6D80DB628C0560940DF6BEFE8AFBAF091AD`.
  Its manifest is 43,455 bytes / SHA-256
  `D7EFC8554A3B01C0FD5D715131B553EC95701D718FE7683315EFBA5FA0F219EE`;
  the one-row R60--R61 validation is PASS/errors empty at 9,672 bytes /
  SHA-256
  `BD43E7FD61B33CC687B09F1EF7F51FF8E6CB5CEC2B5090B78A291A85A5761C0D`.
- The p.128 pre-Stacks block adds durable proof, terminology, definition,
  equivalence, consequence, error, correction, and continuation nodes with
  typed dependencies and bilingual slice hashes. The scaffold is 55,476
  bytes / 953 lines / SHA-256
  `387C86432463544C2DB0B5146A1164F07A4AF49D3876FFA1C50655E7333DFF09`.
- The settled French bounded build is 34 pages / 322,571 bytes / SHA-256
  `260B266739260B10E9BF2291DBC23A07B323C82018E2AB04EFB8F33705BCCC25`;
  its terminal page carries all admitted p.128 text and the exact seam. The
  settled English build is 20 pages / 166,762 bytes / SHA-256
  `B033E23E0E5FDD50DBAC6404E752636BDB7BC99E8B62383AB70816A6E6C45614`;
  physical page 20 passes direct visual inspection with both repairs visible.
  Hard errors are zero. Inherited diagnostics are one French overfull box and
  bounded references, plus two English PDF-string warnings, two overfull
  boxes, and the bounded undefined-reference summary.
- Fourteen workflow rows preserve every closed helper-name, projection-size,
  output-routing, environment-balance, metadata, PDF-tool, and control-name
  retry at 10,113 bytes / SHA-256
  `F2B03BFD6A91BE884EBCA88A40F57965A14A486862BB18EECEC76192407D546E`.
  The verified four-product English `source/$out` directory was removed; the
  pre-existing shared French `$out` directory was left intact because it also
  contains earlier retained artifacts. Temporary `Q:` mappings were removed,
  and no XeLaTeX process remains. No global build, publication, upload, or
  archive action occurred.
- R51 combined validation is PASS/errors empty at 10,926 bytes / SHA-256
  `94F833E316F3726489EEF9254871BB55B12EBA691B7BFEAF918F76C285A7DE41`.
  Next paired cursor: remove only the temporary final `end-env`, then continue
  5.1.5 from NUMDAM PDF one-based p.128 / printed p.129 after `l'homomor-`.

## 2026-08-03 -- paired French/English closure, EGA I printed p.129

- Direct authority was NUMDAM PDF one-based p.128 / printed p.129. The single
  retained 1100-dpi context image is 4,936,370 bytes / SHA-256
  `DF9166BCA72BE762005A6B530925E11888A5267D977EC0F82EB7D09A01FF3301`.
  It was reviewed directly without OCR or a whole-page original-detail load.
- French completes the reduced-morphism construction and functoriality square
  in 5.1.5, proves preservation properties in 5.1.6, proves the product
  comparison in 5.1.7, admits Corollary 5.1.8, and records the nilpotent tensor-
  product warning. `ega1-5-fr.tex` is 9,060 bytes / 190 lines / SHA-256
  `D3DEC590DD38DE0A1CB5F756F7970AC4434CF1E5521379855BCC0592B4E7941C`.
  The p.129 marker slice is 3,979 bytes / SHA-256
  `B0D630DDBDC8D4A6597F12105E6314F0AD0415D40E65B8F192F207C71B696966`;
  the one-operation inverse reproduces p.128 exactly. No temporary close or
  unresolved reading remains, and no printed source defect was catalogued.
- Direct comparison requires no English mutation. The p.129 slice is exactly
  live `ega1-5.tex` lines 69--125, 3,457 bytes / SHA-256
  `1613516E5198693420370041667CE6EC2B8B2C67209B6501722684839729D779`.
  Together with the p.128 prefix it reproduces live lines 1--125 at 8,142
  bytes / SHA-256
  `9BEF395F1E37CFFC7819B25487C4A9F54B8505FE547E2131752EAB830A565B78`
  with no balancing addition.
- R63 independently replays 127/127 source files / 7,281,147 bytes with zero
  row, membership, size, hash, or ordinal-order error and the unchanged tree
  SHA-256
  `658ACB58DBE08F3641410EF071EBA6D80DB628C0560940DF6BEFE8AFBAF091AD`.
  Its manifest is 44,173 bytes / SHA-256
  `13659CCA1A6298345AC1EF029422A1BD4ADCFCDD75763B9D0331B7846ED58605`;
  the R62--R63 validation is PASS/errors empty and zero-delta at 8,581 bytes /
  SHA-256
  `0AC289389C15769AC85CEF5AD442CCDAE0B9BF77226EF48666BC0DB8AF5F250E`.
- The p.129 pre-Stacks block adds the reduced-functor, naturality-diagram,
  preservation, product, corollary, warning, and English-confirmation nodes
  with typed proof edges. The scaffold is 58,492 bytes / 1,004 lines /
  SHA-256
  `88D8A1AF0020C8F0561F837B9C01DB7494FBD7CE4193B215A44645E9DCE9BA19`.
- The settled French bounded build is 35 pages / 327,377 bytes / SHA-256
  `22C33565863E3F71CDD975F17A4C26902D22E24C287113D1C113D4649ECC9483`;
  physical pages 34--35 carry the complete p.129 unit. The settled English
  build is 21 pages / 171,271 bytes / SHA-256
  `2B568041BF9DF9E7EADA134DF4986696BA4472B6B50A982E8E38B62696B2686D`;
  physical page 21 passes visual inspection. Hard errors are zero; inherited
  diagnostics remain one French overfull box and bounded references plus two
  English PDF-string warnings, two overfull boxes, and the bounded reference
  summary.
- Eight workflow rows preserve the two read-only PowerShell parser retries and
  all build/resource receipts at 5,454 bytes / SHA-256
  `3BA6C0B6D2EEB7F7FDF79D715C11486B61D61BEBBDFA35B3E4D26CA7E24AB674`.
  Temporary `Q:` mappings were removed; no XeLaTeX process remains. No global
  build, publication, upload, or archive action occurred.
- R52 combined validation is PASS/errors empty at 10,074 bytes / SHA-256
  `2A69BDB7C8D978A1BC2864A66A738A5C7450A3DE567EB7A67A937817EB1E2902`.
  Next paired cursor: NUMDAM PDF one-based p.129 / printed p.130,
  Proposition 5.1.9. No temporary French close must be removed.

## 2026-08-03 -- paired French/English closure, EGA I printed p.130

- Direct authority was NUMDAM PDF one-based p.129 / printed p.130. The single
  retained 1100-dpi context image is 4,351,421 bytes / SHA-256
  `DA0FD61616ABA3417AC23D410675A020EDC288A4E4B444548039354E8D9152B1`.
  It was reviewed directly without OCR or a whole-page original-detail load.
- French admits Proposition 5.1.9 through the nilpotent-to-square-zero
  reduction, exact sequence (5.1.9.1), the global square-zero ideal, canonical
  affine comparison morphism, two diagrams, and the five-lemma argument. It
  stops exactly at `ce qui résultera de`. `ega1-5-fr.tex` is 12,517 bytes /
  267 lines / SHA-256
  `4F6DDD36624D115FF3571344674D5B3D49E101F4851D2E634ED094359F3DC7A2`.
  The p.130 suffix is 3,457 bytes / SHA-256
  `C27E7F6F0D0C4ACE819B4C536D7010DABFD498ABC0900BF1FE350D9DA3924E45`;
  its one-operation truncation reproduces p.129 exactly. No temporary close,
  unresolved reading, or newly catalogued printed defect remains.
- Direct comparison requires no English mutation. The exact build
  continuation is live `ega1-5.tex` lines 126--177, 3,172 bytes / SHA-256
  `AB1B318C93CEB0F2CA17E6DF96C5C438F27AD5E4390D296E67BB0F6A4B2EEC56`.
  Together with prior projections it reproduces live lines 1--177 at 11,314
  bytes / SHA-256
  `C48CBD81D34FB48E0B8756F6B9C23960B3E207A466FD68C54FF69787F2E51D08`
  with no balancing addition. The inherited `I`, `K`, and `vphi` notation and
  the English placement of `H^1(X,I)=0` across the French physical-page seam
  are retained and reversibly logged.
- R65 independently replays 127/127 source files / 7,281,147 bytes with zero
  row, membership, size, hash, or ordinal-order error and the unchanged tree
  SHA-256
  `658ACB58DBE08F3641410EF071EBA6D80DB628C0560940DF6BEFE8AFBAF091AD`.
  Its manifest is 44,891 bytes / SHA-256
  `76207E6D99DA99033EB431B51886630B4A917FDEEDEE29308FD97FBE2DCDE7F0`;
  the R64--R65 validation is PASS/errors empty and zero-delta at 9,004 bytes /
  SHA-256
  `498854BC46966003417E66D90A21777E3B62DEB7729244C45E064AF467D7A287`.
- The p.130 pre-Stacks block adds the nilpotent-thickening, square-zero
  reduction, exact-sequence, ideal, canonical-map, diagram, five-lemma,
  continuation, and English-confirmation nodes. The scaffold is 61,902 bytes
  / 1,062 lines / SHA-256
  `2D2E022FCF22DC3C47278D7273F4B6B4BB79DDD0BFE73D87E65628D520E1E66A`.
- The settled French bounded build is 36 pages / 331,996 bytes / SHA-256
  `C3938C2B94C3CCCBA74225F94A444C3289873FE4D58365D2DEC82B4CD2C10B49`;
  physical pages 35--36 carry the complete p.130 unit. The settled English
  build is 22 pages / 176,102 bytes / SHA-256
  `5989A16F1CB50EF183F849C55E64C0DBB79468CDDF385E70583C0C470F349BD2`;
  physical pages 21--22 pass targeted visual inspection. The new 11.2554 pt
  English box warning is visible but neither clipped nor overlapping; page 21
  was rendered only because that warning fell there. Hard errors are zero.
- Nine workflow rows preserve the R64/R65 gates, authority receipt, the
  read-only marker and checkpoint-order verifier retries, corrected handoff
  placement, both build receipts, the targeted second reader page, and
  resource closure at 6,362 bytes / SHA-256
  `2DD72D9B2ED6839E63DB8556CCF479D1741CF8FD6D0F62E3EF050FF0962823A6`.
  Temporary `Q:` mappings were removed; no XeLaTeX process or literal English
  `source/$out` remains. No global build, publication, upload, or archive
  action occurred.
- R53 combined validation is PASS/errors empty at 10,676 bytes / SHA-256
  `BDD7227EE137F2B61A57438AB84D3B564131AD214C9A1F8AFD918CE7A2472F8F`.
  Next paired cursor: NUMDAM PDF one-based p.130 / printed p.131, continuation
  of Proposition 5.1.9 after `ce qui résultera de`. No temporary French close
  must be removed.

## 2026-08-03 -- EGA I printed p.131 sealed

- Direct NUMDAM authority at PDF one-based p.130 was reviewed without OCR.
  French completes Proposition 5.1.9, Lemma 5.1.9.2, Corollary 5.1.10,
  Propositions 5.2.1--5.2.2, and the statement of Corollary 5.2.3. It stops
  exactly at `un sous-préschéma induit sur un ouvert de Z.`
  `ega1-5-fr.tex` is 16,480 bytes / 350 lines / SHA-256
  `C6F64E7AD05183672B3F709BE452A0EA0EA3D5013030AE0A03792D3D0B85B6EA`.
  The p.131 suffix is 3,963 bytes / SHA-256
  `35023EDB16116F0E9B7818692F2E393671D0DEC682274B353C44210747E0D9C3`;
  one-operation truncation reproduces p.130 exactly. No temporary close or
  unresolved reading remains.
- The source prints `F|Y` in the local splitting formula of Lemma 5.1.9.2.
  This is preserved diplomatically and catalogued: the extension is over the
  neighbourhood `V`, so the type-correct restriction is `F|V`. English keeps
  `F|V` and adds one immediately visible translator footnote naming `F|Y`.
  The live English file is 46,962 bytes / SHA-256
  `89CB70021FE8386126FAAEBFE2C823A07A71F177BEEB8AD0862209391111E543`;
  deleting the unique note restores exact R66 bytes
  `D3BB566847A24BD268157D7171BD9F5B282FA2C9B8F4D1A1ABD9B84F656FEFF3`.
- R66 independently sealed the pre-edit 127-file tree. R67 replays all 127
  files / 7,281,280 bytes with zero row, membership, size, hash, or ordinal
  error and exactly one changed row, `ega1/ega1-5.tex`. R67 manifest SHA-256 is
  `F9DF2387D0B08F4269B8307DCD7268DD93AA47706F5B024967ED6D8149571EE1`;
  tree SHA-256 is
  `B12D07B194C59E154BE7F7DB383C9B52E0AC6E4ADCAEEF9E0E567522090558A7`;
  PASS validation is 9,356 bytes / SHA-256
  `3AC5F994DC237FDDBCCF5A839D5B5212502B5560F1D92AAD366AB6971B106EAE`.
- The p.131 pre-Stacks block binds the cohomological vanishing, trivial
  extension, printed `F|Y`/type-correct `F|V` decision, reduction corollary,
  locally closed reduced subscheme, factorization, and 5.2.3 continuation
  nodes. The scaffold is 65,174 bytes / 1,117 lines / SHA-256
  `57EC4614738F849349AC91BC57EDC92E85D17B92CCC33F9AE6A57C6A80BBBCB8`.
- The final French bounded build uses r2, which removes only the obsolete
  build-only `I.5.1.4-fr` forward placeholder from the retained p.127 wrapper;
  no source byte changes. Its PDF is 36 pages / 337,663 bytes / SHA-256
  `0521507AD983275AD6152D5B65E011DEEFD4CF727022B5D58983BE29FC14C220`,
  with zero hard errors, duplicate labels, or rerun request. Page 36 passes
  text-layout review. The English PDF is 23 pages / 181,229 bytes / SHA-256
  `7B5CB44FE6196E36B3475D879A59F6013EF38C52C054E5B0FE071602C2237057`;
  pages 22--23 pass targeted review and the note is visible without clipping.
- French, English, and workflow ledgers are respectively 2,558 bytes / SHA-256
  `C22B1C247490E56610CB584D9F4B104CF79F060C21FD21158A75B9CE5E598547`,
  2,308 bytes / SHA-256
  `DF223382341C820F9DA7D5AA71DCE8982B564C5DA4AD29D86EE65B31D9770E15`,
  and 11,870 bytes / SHA-256
  `6286274C0B1502E61D26F9D34C85A937FE2BED30903225D030BB6A769BC0D63F`.
  All renderer, path, parser, projection, placement, wrapper, and metadata
  retries are explicit. No OCR, global build/render, publication, upload, or
  archive action occurred; no XeLaTeX process or `Q:` mapping remains.
- R54 combined validation is PASS/errors empty at 11,936 bytes / SHA-256
  `4B51F8C9B847D1D4A3C8C759CAEE6E09DD1F5EA00D5291E9623A44AF69990AA4`.
  Next paired cursor: NUMDAM PDF one-based p.131 / printed p.132, proof of
  Corollary 5.2.3. No temporary French close must be removed.

## 2026-08-03 -- EGA I printed p.132 sealed

- Direct NUMDAM authority at PDF one-based p.131 was reviewed without OCR.
  French completes 5.2.3 and 5.2.4, opens subsection 5.3, admits 5.3.1,
  5.3.2, and 5.3.4, and stops after diagram (5.3.5.1) in Proposition 5.3.5.
  `ega1-5-fr.tex` is 19,923 bytes / 442 lines / SHA-256
  `EE969AFC8501A89A9D5A079E7A9503FD2D355E89C557F97D50825C806D2A0FAC`.
  The p.132 suffix is 3,443 bytes / SHA-256
  `E1DD07F18D2B412BDB99DCF905FC14A6199C182E4F48B955F4F61F3A35510DB9`;
  truncation reproduces p.131 exactly. The unique terminal
  `\end{proposition}` is temporary and must be removed before p.133.
- Proposition 5.3.5 prints `f:X→S, Y→S`, omitting `g` before the second
  structural map, although `π=f∘p=g∘q` and the diagram identify it. French
  preserves the omission. English retains `g:Y→S` with one visible translator
  footnote. The live English file is 47,147 bytes / SHA-256
  `F28E52859F1D3CF5393BEED2D882180197D6B27DF81976E343864863B9DF821F`.
- Initial English reader layout exposed the inherited empty 5.3.3 environment
  as a visible stray period absent from French authority. R2 replaces it with
  `\phantomsection` while keeping label `I.5.3.3`; no visible 5.3.3 text is
  invented. Removing the new footnote and restoring the former empty
  environment reproduces exact R68 bytes and hash.
- R68 sealed the unchanged pre-edit 127-file tree; R69 recorded the note;
  R70 records the reader repair. R70 replays all 127 files / 7,281,465 bytes
  with zero row, membership, size, hash, or ordinal error. Manifest SHA-256 is
  `18F2EF15DF53015AE384D8CD148FBF4D8B378A82C5CE0A90F6FA398D0DF2B952`;
  tree SHA-256 is
  `49B83F1B0ED89440DCC3759038AC626EED7C2C869766D1D6D1E55B07E448F210`;
  PASS validation is 11,413 bytes / SHA-256
  `9218CF601B450135DB63656B3E6A66E638FF33368792BA6C0F5A7B50FF71D740`.
- The p.132 pre-Stacks block binds the reduced-closure proof, ideal pullback,
  diagonal identities, categorical portability, product/base-change
  compatibility, printed 5.3.3 gap, missing-`g` omission, diagram, and p.133
  continuation. It is 69,454 bytes / 1,188 lines / SHA-256
  `EB95123847A5B6B08D50C20ECF0857D31E0D3E3599D15153FECEF8EEC3E58E82`.
- The French bounded PDF is 37 pages / 342,931 bytes / SHA-256
  `ADFF8CAEA181CE14DC5F774EF41E095E15C69E024624E0ED7CE65CC6006671A4`;
  pages 36--37 pass text-layout review. Final English r2 is 23 pages / 186,413
  bytes / SHA-256
  `D34DD7AE50939B003451C06CBA06BD7E8788F533197D846415A92EE1002E5A1E`;
  page 23 passes visual review with the note visible, stray period absent,
  diagram complete, and no clipping or overlap.
- French, English, and workflow ledgers are respectively 3,069 bytes / SHA-256
  `D3EF82B165D8F351F62F098C6511B13F5D2B39581348C3CFD3482A7D4E62EA20`,
  2,805 bytes / SHA-256
  `6F433E72C6281D4237D31E9336093BE8595201186E5CCC7362EC0DD782E79040`,
  and 11,957 bytes / SHA-256
  `8A129466B462CF28A5D1B9EE5CAD71BD58218026192C12C3B94AC660917F0BE4`.
  All path, parser, marker, patch-context, placement, projection, diagnostic
  build, and reader-repair events are explicit. No OCR, global build/render,
  publication, upload, or archive action occurred; no XeLaTeX process or
  `Q:` mapping remains.
- R55 combined validation is PASS/errors empty at 12,290 bytes / SHA-256
  `C97366E68C0A41EF8D55E74D17F01A661A274F7850BB9EE24C897D1F67996C7A`.
  Next paired cursor: remove only the temporary final `\end{proposition}`,
  then continue NUMDAM PDF one-based p.132 / printed p.133 with
  `est commutatif` in Proposition 5.3.5.

## 2026-08-03 -- EGA I printed p.133 sealed

- Direct NUMDAM authority at PDF one-based p.132 was reviewed without OCR.
  The one bounded authority image is 4,819,964 bytes / SHA-256
  `30490AFD70E4515B84CA69B3008EC5EDAA33221971B0DE8EC84031CA9EDAAE05`;
  its existing text-layer extraction is 3,047 bytes / SHA-256
  `20DAAD645CB6D8199359FC662F899410C443B6E1D5AA5C70DCBB96271702A126`.
  French completes Proposition 5.3.5, Corollaries 5.3.6--5.3.7,
  Propositions 5.3.8--5.3.9, and Corollaries 5.3.10--5.3.11. It stops exactly
  at `C'est le cas particulier du cor. (5.3.10) où l'on remplace S par Y et T
  par S (cf. (5.3.7)).`
- `ega1-5-fr.tex` is 23,519 bytes / 538 lines / SHA-256
  `DC5D2863A197CE33C9AAC314696ABDD36E840183D8DA735ACE6E99613A60FB91`.
  The p.133 marker starts at byte offset 19,905; marker-to-EOF is 3,614 bytes /
  SHA-256
  `9D8475E0BB535C2061A1A1A6F860A339C911E31E7C530987C66ED99AD1AB78FD`.
  Replacing that suffix with the exact 18-byte `\end{proposition}\n` restores
  sealed p.132 at 19,923 bytes / SHA-256
  `EE969AFC8501A89A9D5A079E7A9503FD2D355E89C557F97D50825C806D2A0FAC`.
  This records the required seam reversal; no temporary close remains.
- Proposition 5.3.8 prints that `X(Z)_Y` is likewise reduced to one element
  after injecting it into the singleton `Y(Z)_Y`. Injection proves only “at
  most one element,” since `X(Z)_Y` may be empty. French preserves the
  author-text wording; English retains “at most one element” and adds one
  immediately visible translator note. Current `ega1-5.tex` is 47,337 bytes /
  827 lines / SHA-256
  `520D28FBEE094AFC930E09D6A27ED8257D4E4F802FAAE0E2C5135F8F8641D798`.
  Removing only that 190-byte note restores R71 at 47,147 bytes / SHA-256
  `F28E52859F1D3CF5393BEED2D882180197D6B27DF81976E343864863B9DF821F`.
- R71 independently seals and replays the unchanged pre-edit 127-file tree:
  manifest 47,259 bytes / SHA-256
  `5C2864AB0D734217A601220A5702D3C1077AA1C2ACF6522B882979981FBDB65A`,
  7,281,465 source bytes, and tree SHA-256
  `49B83F1B0ED89440DCC3759038AC626EED7C2C869766D1D6D1E55B07E448F210`.
  R72 replays 127 files / 7,281,655 bytes with zero row, membership, size,
  hash, or ordinal error and exactly one changed row, `ega1/ega1-5.tex`.
  R72 manifest is 47,710 bytes / SHA-256
  `1942000C1077F279EC63EE894E15F0830C925753E3ADC0A5E18370B3DF948C2A`;
  tree SHA-256 is
  `29EB38A85D6F0DEC1644A9B2C4AA2A52D7185A83875E115B6AD0C44C627F9D37`;
  PASS validation is 9,300 bytes / SHA-256
  `4B637E88F650B3479D9F6545361D7895A4B0145BEE9B81425826C64387595C21`.
- The exact English p.132--p.133 seam projection is live lines 239--401,
  7,292 bytes / SHA-256
  `509C0BCCBE4B7FA86F642D2032B36BD63C662DBF70881E85E1C47A04F91B543F`,
  with no balancing addition. Its p.133 marker slice is 3,713 bytes /
  SHA-256
  `0F8884F778BD6E84AE70F4812688FB99511FB1D4ADE1E9F6BE7868CAD3A946CF`;
  cumulative live lines 1--401 are 22,462 bytes / SHA-256
  `20C09CBE4E058340D3E23C26C6377233C358FFA49CB706EDF5F2E62341DA9187`.
- The p.133 pre-Stacks block binds the completed fibre-product universal
  property, diagonal base-change consequences, monomorphism criteria,
  separatedness criteria, the printed one-element defect, and the graph
  continuation. The scaffold is 72,982 bytes / 1,246 lines / SHA-256
  `B95A07D25C9773FE9AC06725E4B9833A9E8851EFA9328F76ED8739EF0994EA44`.
- The French bounded PDF is 38 pages / 347,584 bytes / SHA-256
  `15B36FFA1B62269026EC7ED1A5BF7980203B0163DB137DACFDABE5297979B06B`,
  with zero hard errors, duplicate labels, or rerun request; pages 37--38 pass
  text-layout review. The English PDF is 24 pages / 191,842 bytes / SHA-256
  `5EF5926DA9FFC164E1E60D3228F0F46132F42259D3F66EB8188C0CDC5B73AB7D`;
  pages 23--24 pass targeted text/visual QA, the note is visible, and no
  clipping or overlap is present.
- French, English, and workflow ledgers are respectively 3,109 bytes /
  SHA-256
  `AA2FB8063F3093212BEFD7888972AAFB4B924E3CB5191B7FA2192D4247EB1F6B`,
  2,285 bytes / SHA-256
  `7A2DBEC3A4474C0FB4FB3ED92D52C9B58D2D47DE038674BD0A080B57200D7EE6`,
  and 7,402 bytes / SHA-256
  `E05C22AC16A379B4E2CF21FCE496EC6DDCE5AF827BB4A080308F0B7F7BCB05A4`.
  The workflow ledger includes the late receipt-tail command-composition
  failure and successful bounded retry. No OCR, global build/render,
  publication, upload, or archive action occurred; no XeLaTeX process,
  temporary English `source/$out`, or `Q:` mapping remains.
- R56 combined validation is PASS/errors empty at 11,033 bytes / SHA-256
  `025D9BB49D0B2305199EBE54D56822E6CE7E4E38E4AAA93819EC67A560CCB091`.
  Next paired cursor: NUMDAM PDF one-based p.133 / printed p.134, graph
  terminology after Corollary 5.3.11. No temporary French close must be
  removed.

## 2026-08-04 -- EGA I printed p.134 sealed

- Direct NUMDAM PDF one-based p.133 / printed p.134 was read from the bounded
  4,681,976-byte authority image, SHA-256
  6D57CB50CF18A51FF996D8F71D10516D12E499365B62F2EA8F3B6DAF25F40F8A.
  The existing 46-line text layer is 2,860 bytes / SHA-256
  0C92D2FD88D9CD2D20856DC272C78A46A53853504F48EC418878269666980992;
  no OCR was run.
- Appended graph terminology, Corollaries 5.3.12--5.3.14, Proposition 5.3.15,
  and Corollary 5.3.16 through the terminal words “z in Delta_Y(Y) intersect
  p_1^{-1}(X), on a z=Delta_Y(y)”. source/ega1/ega1-5-fr.tex is 27,093
  bytes / 629 lines / SHA-256
  2BF15FE97B29DE032BB338E83897243673A7CC9C5956049AB1A29E195281DC2F.
  Truncation to 23,519 bytes restores exact p.133 SHA-256
  DC5D2863A197CE33C9AAC314696ABDD36E840183D8DA735ACE6E99613A60FB91;
  no temporary close was added.
- The inherited English printed-p.134 slice was source-grounded and required
  zero source mutations. R73 and R74 both replay 127 files / 7,281,655 bytes
  to tree SHA-256
  29EB38A85D6F0DEC1644A9B2C4AA2A52D7185A83875E115B6AD0C44C627F9D37.
  R74 is 48,428 bytes / SHA-256
  E4A8F263163EE68710CC572F81E63E7A0DBAFC72B728985D2E6519CF27F86D9D;
  its PASS validation is 10,891 bytes / SHA-256
  E153071E1444563D15BDF45A440C05A9441CF325D534E04654DDBCB0F2867B34.
- The French bounded build passes in two serialized XeLaTeX passes: 38 pages /
  352,013 bytes / SHA-256
  1DD0BA9C886D8C3BAFDC8AC3504848B5F180EAAFEC63FF9C2ECD820F1585A052.
  Pages 37--38 pass text-layout review. The English bounded build passes in
  three serialized passes: 25 pages / 196,609 bytes / SHA-256
  629DF4EF410D01F22290444C82BDD350AB8399D2BD108772E973F5469C968F73.
  Pages 24--25 pass text-layout/visual QA, including the diagram, with no
  clipping or overlap. Its terminal proof close is build-only projection
  balancing and is absent from live English source.
- The p.134 semantic block occurs once, follows p.133, and is at true EOF of
  the pre-Stacks scaffold: 77,945 bytes / 1,329 lines / SHA-256
  C2697E538722F21711C2833A524D689CD084E6F283E058AB37FB1AD40BAB5EA3.
  French, English, and workflow ledgers parse at respectively 9 rows / 3,289
  bytes / SHA-256
  342FF6BAF4F870B459C209966437144A008C8AB365BE44C2BBF4C9EE10970AE9,
  8 rows / 2,130 bytes / SHA-256
  F4266810E5D1C1D56C373ECEA8349B8751D9E8905D62AE431C546A11CC443B55,
  and 23 rows / 17,614 bytes / SHA-256
  546920CB0A701EF12C3E8B1FB2CD7405EB5247943D85A7E35C26D21A9D2B332A.
  The workflow preserves both receipt-patch syntax failures and their bounded
  retries; neither failed command mutated a source, validation, or receipt.
- R57 combined validation is PASS/errors empty at 11,389 bytes / SHA-256
  26FAB757B306D0046E7169404721530AF65A9308A23A95CA37A138DB4931E3CC.
  No OCR, global build/render, publication, upload, archive, XeLaTeX process,
  temporary English source/$out, or Q: mapping remains. The user-moved
  unrelated tree is authoritative at
  [PRIVATE_DOCUMENTS_ROOT]\CHat translates and clean; its former
  Papors\Chatnotes location was not recursed.
- Next paired cursor: first create/replay R75, then NUMDAM PDF one-based p.134
  / printed p.135, continuing Corollary 5.3.16 after z=Delta_Y(y). No
  temporary French close must be removed.

## 2026-08-04 -- EGA I printed p.137 sealed

- Direct NUMDAM PDF one-based p.136 / printed p.137 was read from one bounded
  authority image, 5,057,783 bytes / SHA-256
  85D4DC363A051C5EA7D369D41B0756B13FB29BBC286EF1F77505E32A2B3A109E.
  The existing text layer is 3,592 bytes / 53 lines / SHA-256
  58F824549A3718171C76DFF77DAFE5CC6DDFE3033A48ED601BC200C5EE713350;
  no OCR was run and the image was not loaded at original detail.
- Appended the completion of Proposition 5.5.1, its unnumbered reduction
  diagram, Corollaries 5.5.2--5.5.3, Proposition 5.5.4 and its proof, and the
  terminal irreducible-component reduction. source/ega1/ega1-5-fr.tex is
  38,044 bytes / 889 lines / SHA-256
  9F316E9901A7DC8F069853E0DC3A9061FA49779CB59CE2016CFF95B2D11FD4BE.
  Its 3,823-byte append has SHA-256
  804E027A1BCA48480DE29FC8B4B45436BA00B2A588C0042A93B21E64EC50EF91
  and is exactly reversible by truncation to sealed p.136 at 34,221 bytes /
  SHA-256
  E025EFA76D8F9C9BBDA04042337FA59D653F93E403AAB5FD3BC287F2712FDE67.
  There is no temporary close, source correction, new printed-source defect,
  or unresolved reading.
- Direct paired recheck made three source-fidelity repairs in the inherited
  English: visible (3.3.9.1) now targets the exact existing I.3.3.9.1 label;
  the lower Delta_X label is on the source's lower arrow side; and the weak
  “leads to the idea of separation” wording now states the actual reduction
  asserted by French ramène. Each intervention has exact old/new fragment
  hashes and an exact inverse. Current source/ega1/ega1-5.tex is 47,345 bytes
  / 827 lines / SHA-256
  BE2123101A28F8BEB6BBB5B32FC09CCA17F1B01BA491C9799229D9810B89BE2E;
  in-memory replay of the three inverses restores exact R79 bytes, 47,337 /
  SHA-256
  520D28FBEE094AFC930E09D6A27ED8257D4E4F802FAAE0E2C5135F8F8641D798.
- Complete R80 is a one-row successor of pre-edit R79: 127 files / 7,281,663
  bytes, manifest 50,731 bytes / 1,114 lines / SHA-256
  1ECABBC856950C7EDB083D9FA502DBF86F68B56D74C2AB84F6AE460704D93F7B,
  canonical tree SHA-256
  E179D8E2393A34B50CA89B4C26616FE685F0A96FE74F5F91B20A921689CA3FFB.
  Independent .NET-ordinal replay found zero membership, order, size, row-hash,
  aggregate-byte, or tree-hash error; exactly ega1/ega1-5.tex changes by +8
  bytes.
- The two-pass French bounded reader is 40 pages / 366,748 bytes / SHA-256
  480AA13E0D0694556D4AA2FA5025754F421513D62B8581D44C08276CD68B87F4.
  Page 40 passes text-layout and visual QA, including both diagrams and the
  lower Delta_X label. The three-pass English bounded reader is 28 pages /
  211,829 bytes / SHA-256
  2A041B3BAD2EB9F64BE88FE8A4E9F5B3A881FADC84FD53AA4ED894B360B37B62;
  pages 27--28 pass text-layout QA with the diagram and strengthened reduction
  visible and no clipping or overlap indication.
- The unique p.137 semantic block follows p.136 at true EOF: 92,172 bytes /
  1,571 lines / SHA-256
  248460C70D5B42F30E254761EC31C30F9F3AD6EFAFDFC41C768AEC50581D10C6.
  French, English, and workflow ledgers parse at 9, 10, and 20 rows, with
  SHA-256 values
  5E258575FACC7B0AF94C1B48F7F61C093F4609DE2EAD944F4C675D28D29A7310,
  D5751EC1C3C1FF5552878D5BA435BDE73B4E20C899C7DCECA74F6DAB4F2C96B2,
  and
  C07847BA8242D286A7303249DAF56E85DFC3070623A633AFB56330819CD9663C.
  All stable IDs are present and unique. The workflow ledger retains the
  authority-wrapper, view path, scaffold-placement, XeLaTeX invocation,
  projection, parser, self-hash expectation, and accidental broad-search
  failures with their exact no-mutation or bounded-retry resolutions; the
  accidental broad search crossed unrelated SGA/Noether text but changed no
  file and was not repeated.
- English R80 validation is PASS/errors empty at 10,978 bytes / 249 lines /
  SHA-256
  4034C5B336955026E9210E7D2FD3EFC5EBF4A8FA4C93C68BF45FFD4B119AA93C;
  French R60 is PASS/errors empty at 12,962 bytes / 277 lines / SHA-256
  A91D65AB7FCA43D68A6AF62301105872ED5A61EDC938B98BDFE2C50DE694B999.
  All external identities, exact source inverses, source balances, target
  labels, projection coordinates, and resource closures replay. No OCR,
  global build/render, publication, upload, archive, remaining XeLaTeX
  process, temporary English source/$out, or Q: mapping remains.
- Next paired cursor: create and independently replay R81, then direct NUMDAM
  PDF one-based p.137 / printed p.138, beginning Proposition 5.5.5. No
  temporary French close must be removed. Use only named EGA roots; do not
  recurse [PRIVATE_DOCUMENTS_ROOT]\CHat translates and clean or its former
  Papors\Chatnotes location.

### 2026-08-04 -- p.134 retained-raster metadata correction

- A bounded p.134 build-directory listing during p.135 setup found the
  retained English p.25 raster at
  controls/ega1_p134_english_bounded_build_r1/EGA1_P134_ENGLISH_BOUNDED_CHECK_R1-page25-150dpi.png,
  259,908 bytes / SHA-256
  390A1151EB9A661083D57C67CD880C7A98326BD95912165C6006E5E8871324DD.
- This expressly supersedes the earlier ephemeral/not-retained conclusion.
  The bad probe remains in the workflow ledger; a correction/reversal row
  records the exact path. No source, build, render, or visual result changed.
- Final p.134 workflow is 25 rows / 19,178 bytes / SHA-256
  280759893633110B6019F6D6E65E025BB44573CE099380B64B2E4DECF9C24C65.
  Corrected English R74 is 11,546 bytes / SHA-256
  70EE5C3DF4C68F4549EF55E7D6C572998706C32572288653D75932BA50042B7A;
  corrected French R57 is 12,367 bytes / SHA-256
  AA264ADF86D4AF5B1A1BE075DC5293920009B08E57C8218993865E958BF9EC18.

## 2026-08-04 -- EGA I printed p.135 sealed

- Direct NUMDAM PDF one-based p.134 / printed p.135 was read from one bounded
  authority image, 4,299,800 bytes / SHA-256
  AA876A55EC9FD2FE0B3140B0F00AB9031D7C0D1909146B1B2396CD508126BB0A.
  The existing text layer is 3,005 bytes / 51 lines / SHA-256
  F2957B8386662FC62E68EA0A528DC4A22B002E41E1FCCD61E5B6F8EB858E606C;
  no OCR was run.
- Appended the completion of 5.3.16, Corollary 5.3.17 with both diagrams,
  Definition 5.4.1, Proposition 5.4.2, and Corollaries 5.4.3--5.4.4.
  source/ega1/ega1-5-fr.tex is 30,547 bytes / 718 lines / SHA-256
  E1DBCD8A7DEF99161EE00A439D8BC4C1144D57B79DAB4853B0BDC80716B350F5.
  Its 3,454-byte append is exactly reversible by truncation to sealed p.134;
  no temporary close was added.
- Direct paired recheck found the inherited English p.135 slice
  source-grounded with zero source mutations. The visible historical
  prescheme/scheme footnote at 5.4.1 is retained as explicitly classified
  translator paratext. R75 and R76 replay the same 127-file tree; R76 is
  49,155 bytes / SHA-256
  67192F831823DB9C25E6951DF7CFB69A69C81422CF594EE33C84C3B3ACB386E3.
- The two-pass French bounded reader is 39 pages / 356,630 bytes / SHA-256
  EECC102968EB25B18C92A369BFCB5350FCB35B4E1651F00F2BA28BA14CF81BA2.
  Pages 38--39 pass text-layout QA and page 39 passes visual QA, including
  both diagrams. The sole new unresolved hyperlink is the source-intent
  forward reference I.5.5.7-fr. The three-pass English bounded reader is 26
  pages / 201,867 bytes / SHA-256
  AB575233DAD6613B4CBFD411C085443EDDDB10967D13D9E2A28996099A2293FE;
  pages 25--26 pass text-layout QA with diagrams and translator note visible.
- The unique p.135 semantic block follows p.134 at true EOF after the logged
  repeated-footer placement retry: 82,678 bytes / 1,408 lines / SHA-256
  9545858861D9E506F65069F7E65FCD0403D29C78A7DAC4D6A7A7AFE56348E183.
  French, English, and workflow ledgers parse at 9, 8, and 11 rows, with
  SHA-256 values
  F36809C9FA4BF10D80158835282CE6763A99ADBCD1E32B23529C597141C5C47A,
  489EE8FD76A1E5530143D085FB2A5E4D1BB162B72FE9763AB58B89F86CA5C4D7,
  and
  6968A314768BE84F01C685A4D9A25C6DE20F29D55C5198870758E2986EADB33E.
- English R76 validation is PASS/errors empty at 10,513 bytes / SHA-256
  A344A70C00EBEE10693A5B7CF9AE38CBF9A6E69B6F5914DD4CC69DF913D61398;
  French R58 is PASS/errors empty at 12,751 bytes / SHA-256
  A170A999DBA4BB832A693D406172FF83398FC61413A922C455CC84DC25321C10.
  The p.134 raster-custody correction is explicitly carried forward. No OCR,
  global build/render, publication, upload, archive, XeLaTeX process,
  temporary English source/$out, or Q: mapping remains.
- Next paired cursor: create/replay R77, then NUMDAM PDF one-based p.135 /
  printed p.136, beginning Corollary 5.4.5. No temporary French close must be
  removed.

## 2026-08-04 -- EGA I printed p.136 sealed

- Direct NUMDAM PDF one-based p.135 / printed p.136 was read from one bounded
  authority image, 4,742,222 bytes / SHA-256
  E0116F6D3509552A6308EBD99DABAFAD63D60ECCCB12EF1907415E734085921E.
  The existing text layer is 2,943 bytes / 52 lines / SHA-256
  BA752752DA446DD2EB32AD4805E51487FBA656F82664EE7D81F9AA6692529106;
  no OCR was run.
- Appended Corollaries 5.4.5--5.4.7, Remark 5.4.8, the 5.5 heading, all six
  clauses of Proposition 5.5.1, and its proof through the triangular diagonal
  diagram and exact terminal words ce qui. source/ega1/ega1-5-fr.tex is
  34,221 bytes / 810 lines / SHA-256
  E025EFA76D8F9C9BBDA04042337FA59D653F93E403AAB5FD3BC287F2712FDE67.
  Its 3,674-byte append is exactly reversible by truncation to sealed p.135;
  no temporary close was added and no printed-source defect was catalogued.
- Direct paired recheck found the inherited English p.136 slice
  source-grounded with zero source mutations. Exact live lines 552--621 are
  3,461 bytes / SHA-256
  FF6AE4299248F4ED0B7B10A1229B6687A93A87A5A5D538ACEDEACF0501DE2E10.
  R77 and R78 replay the same 127-file tree; R78 is 49,882 bytes / SHA-256
  803A294EC3F3CF1EFBC42ED8C3CDEE057FF2DA8142483676ED5B2E0B74F85F7B.
- The two-pass French bounded reader is 40 pages / 361,890 bytes / SHA-256
  2616D0F29294FF83B73C6BEF0B27728B8C8D5EF1633D3ED0B5DA84EEAEBB6C42.
  Pages 39--40 pass text-layout QA and page 40 passes visual QA, including the
  triangular diagram. The three-pass English bounded reader is 27 pages /
  206,911 bytes / SHA-256
  1E4A283AC89786A08A3DC0B5AB5C979D783490E0A4DA47DD2FDBA888F777E5B8;
  pages 26--27 pass text-layout QA with all six clauses and the diagram. Its
  sole proof close is build-only because the live proof continues on p.137.
- The unique p.136 semantic block follows p.135 at true EOF: 86,845 bytes /
  1,481 lines / SHA-256
  908D82E0E7063B91CFDE8C2765AD49F7DA2A9B60E5F8E782A4B1C0A697FE1DA2.
  French, English, and workflow ledgers parse at 8, 8, and 18 rows, with
  SHA-256 values
  0A6DC1307AC03D2997C33A59F584993DEEF1AE7362A157704D7956EC5B0BA915,
  0B24E6C39398AACDA9FE0631914F542ACB88B1A497EF37C7CC2DA5898CD59239,
  and
  C3B242A5B9B4130D3AF2A7FC27A459B0D551F30BD232EF53D5C98635919CFCDE.
  The workflow ledger retains every harmless inverse/parser/long-path/name
  retry and its exact no-mutation resolution rather than erasing failed
  attempts.
- English R78 validation is PASS/errors empty at 10,320 bytes / SHA-256
  2877803FF2CE1394874B34E53E7F5734EA3071E63E78CA26D81CB78720559127;
  French R59 is PASS/errors empty at 12,413 bytes / SHA-256
  0B7EFF6AC3741D1FB7B4CF326CCAC9872C6E4EC6FBFD5C83D6F0FA9A54651A9C.
  Twelve exact cross-bind checks pass. No OCR, global build/render,
  publication, upload, archive, remaining XeLaTeX process, temporary English
  source/$out, or Q: mapping remains.
- Next paired cursor: create/replay R79, then NUMDAM PDF one-based p.136 /
  printed p.137, continuing the proof of Proposition 5.5.1 after ce qui. No
  temporary French close must be removed.

## 2026-08-04 -- EGA I printed p.138 sealed

- This terminal entry supersedes the stale terminal p.135--p.136 cursor
  receipts that were previously appended after the valid p.137 entry. Their
  historical bytes remain intact; the chronology anomaly and non-destructive
  resolution are recorded in the p.138 workflow ledger.
- Direct NUMDAM PDF one-based p.137 / printed p.138 was read from one bounded
  600-dpi authority image, 1,956,101 bytes / SHA-256
  C5104A4DB04052A58074BF34EDD92726FE3C25FC1E5F68D59C46E286F50A240F.
  The existing text layer is 3,400 bytes / 47 lines / SHA-256
  F92EEB6316D10137CD3A34E1634478D7C48013E0E8A717162F0E868E7A30F889;
  no OCR was run.
- Appended Proposition 5.5.5 and proof, the affine-target reduction,
  Proposition 5.5.6 and proof, Corollaries 5.5.7--5.5.9 and proofs, the
  affine-morphism consequence, and Proposition 5.5.10 with its proof through
  the exact words “s'identifie à l'espace sous-jacent au”.
  source/ega1/ega1-5-fr.tex is 42,953 bytes / 1,003 lines / SHA-256
  2619437E655E33F819B8A965B48F8DA2D9B0F6890A0E9314EA285D8C99DF87CB.
  The 4,909-byte append is exactly reversible by truncation to sealed p.137;
  no temporary close, source correction, printed defect, or unresolved
  reading was admitted. The rejected `\mathbb{Z}` candidate and accepted
  corpus-standard `\mathbf{Z}` glyph encoding are individually recorded and are
  not treated as an authorial error.
- Direct paired recheck produced four English source-fidelity repairs: the
  omitted first 3.2.5 dependency, the logical reduction to affine targets,
  singular “criterion”, and the necessary-versus-sufficient polarity/scope
  of Corollary 5.5.9. The last is mathematically substantive: inherited
  English incorrectly made the broad condition biconditional. The retained
  mapsto glyph, proof environments, and structured clause display are
  separately catalogued normalizations, not silent claims about the printed
  author. Current source/ega1/ega1-5.tex is 47,354 bytes / SHA-256
  29761A8C85CC1608E3EC80A7397B0847306F8A5F8C61AEA4772E1C79A3E493E3.
  All four old and new fragment hashes replay, and the exact inverse restores
  R81 at 47,345 bytes / SHA-256
  BE2123101A28F8BEB6BBB5B32FC09CCA17F1B01BA491C9799229D9810B89BE2E.
- R82 is a complete 127-file / 7,281,672-byte manifest, 51,613 bytes / 1,126
  lines / SHA-256
  CE696DDADDBAD9D41D2086BC0B849F9D57531BA086B77826DC1FA0F0BFA771F9;
  its ordinal tree SHA-256 is
  863DC6BD6E3C752E94DDA9B58EEBD8AE9378CF64B525F663359EFDAE146E85CD.
  Exactly ega1/ega1-5.tex changes from R81 by +9 bytes; membership, row,
  order, aggregate, tree, and inverse gates all pass.
- The two-pass French bounded reader is 41 pages / 372,423 bytes / SHA-256
  96E1279700FDCBEFFC38E7E1E28A28D6CA9C4F08BB9B87A3D1BD7C91B8FD2687.
  Page 41 passes text-layout and visual QA, including the formulae and terminal
  cursor. The three-pass English bounded reader is 29 pages / 217,374 bytes /
  SHA-256
  1B4A7532D8DF1C832CBE61249EF6395CC36A3EEFEA1C1C886472ECA62D0297C4;
  pages 28--29 pass text-layout QA with all four repairs visible. Its sole
  end-proof token is wrapper-only because the live proof continues on p.139.
- The unique p.138 semantic block follows p.137 at true EOF: 98,950 bytes /
  1,682 lines / SHA-256
  1B024552FFE71D56EB1BB2BA50304961073B55B0CEE76D5F514EDDFB65D49BB4.
  French, English, and workflow ledgers parse at 9, 14, and 22 rows, with
  SHA-256 values
  81D5831F7E7C7A300DE9CC8CBB51BB367D677294907038B2D2D7DC370FC3FC20,
  1917D2EF35BC1AADB57074D45481DF3899F120402E915595608A3573D4E3226A,
  and
  A1FFA5B192BE640F4BE13E876823E1F255AF2CF1E0560DCB3B89DA76D8EEB7C4.
  Failed render, parser, long-path, line-ending, and search-scope attempts and
  the receipt chronology anomaly remain visible with no-source-mutation
  resolutions.
- English R82 validation is PASS/errors empty at 15,740 bytes / 335 lines /
  SHA-256
  9B73FA281982CBC243DDEA33272650265A40A64E1FF7FBB18D217D9C63F4E58A;
  French R61 is PASS/errors empty at 13,736 bytes / 295 lines / SHA-256
  61DEE7FD8760F32CF965CB8D10E85FC4572B766ADCDFC16978EA297FCFA22E73.
  Independent identity, ordinal-manifest, LF projection, source-slice,
  label-target, fragment-inverse, environment-balance, scaffold-placement,
  process, and mapping checks pass. No global build/render, publication,
  upload, archive, remaining XeLaTeX process, temporary English source/$out,
  or Q: mapping remains.
- Next paired cursor: create/replay complete R83 before any p.139 English
  source mutation, then use NUMDAM PDF one-based p.138 / printed p.139 to
  continue the proof of Proposition 5.5.10. No temporary French close must be
  removed.

## 2026-08-04 -- EGA I printed p.139 sealed

- This terminal entry supersedes every older cursor receipt while preserving
  its append-only bytes and the previously recorded receipt-order anomaly.
- Direct NUMDAM PDF one-based p.138 / printed p.139 was read from one bounded
  600-dpi authority image, 1,882,379 bytes / SHA-256
  DCA1F394B632C3CCA5BB86F9BD2FCDB1CD29BDE66A4051AAAE99DBBD53550DDC.
  The bounded text layer is 3,420 bytes / 46 lines / SHA-256
  E176F48224668AA482CEED21B783ACA6286D62508EEA7C337585EDF63E36531A.
  One temporary crop established both printed (0) tokens and was removed; no
  OCR was run.
- Appended the completion of Proposition 5.5.10, Examples 5.5.11, and Remark
  5.5.12 clauses (i)--(iii), ending exactly at “possède la propriété P.”
  source/ega1/ega1-5-fr.tex is 47,116 bytes / 1,076 lines / SHA-256
  D8168125192DF12B1765D4F81E8DD2A15D37378370454F4370E0A3F18C3BC055.
  The 4,163-byte append is exactly reversible by truncation to sealed p.138.
  Remark 5.5.12 and its enumerate remain intentionally open, with no
  temporary source close.
- The diplomatic source preserves and catalogues the authorial doubled-origin
  error: the print has (0) in both ideal conditions although the origin has
  prime ideal (s), while (0) is generic. The English correction is visible
  and noted, never silent. The direct-image comma after 4.2.1 also supersedes
  a recorded secondary text-layer digit-3 misdecode.
- Direct paired recheck produced three English repairs: two (0)-to-(s)
  replacements plus their visible translator note on one source line;
  singular agreement after neither; and exact negative-quantifier scope for
  the doubled affine plane. The latter prevents a weaker reading in which
  only the conjunction of the two conditions fails. Current
  source/ega1/ega1-5.tex is 47,538 bytes / SHA-256
  E4E6D19A7C19B69E61CBBE8792DB0EED1AD6DAA0DD559E61811057F11641651C.
  All three old and new fragment identities replay; their exact inverse
  restores R83 at 47,354 bytes / SHA-256
  29761A8C85CC1608E3EC80A7397B0847306F8A5F8C61AEA4772E1C79A3E493E3.
- R84 is a complete 127-file / 7,281,856-byte manifest, 52,489 bytes / 1,138
  lines / SHA-256
  4C4EF213763A4E9838AF2E8E23A89C8DB0FC45DEBEA0DA078908BED01EA6CFB8;
  its ordinal tree SHA-256 is
  3DD3F9B92DBC78C7334C1F194836E9F4181DF2FE87A8A3905D64947F51576F6C.
  Exactly ega1/ega1-5.tex changes from R83 by +184 bytes; membership, row,
  order, aggregate, tree, fragment, and inverse gates all pass.
- The two-pass French bounded reader is 42 pages / 378,267 bytes / SHA-256
  47E016E105621346051731757945D7110492D3D25F34C1DCE93CBC08896DAB07.
  Pages 41--42 pass text-layout QA and the single page-42 raster is clean.
  The three-pass English bounded reader is 29 pages / 223,477 bytes /
  SHA-256
  D9DCC6A8D435A42A762FCE1B60E465873540FBCE8487DDAAB1ACB7353FB505CC;
  pages 28--29 pass text-layout QA with all three repairs and the translator
  note visible. Each wrapper supplies exactly two build-only closures for
  the continuing remark/list scopes.
- The unique p.139 semantic block follows p.138 as the final heading:
  104,604 bytes / 1,773 lines / SHA-256
  BE3FB4F09303AAF6D12C972D38D1590E94201A6952223A35BD32A9CECADA282B.
  French, English, and workflow ledgers parse at 10, 10, and 24 rows, with
  SHA-256 values
  1829BF1EC9897BD171EA456CD46BF02E9A48314398F92059DD149B493F042B1C,
  F9BDD05D3B6FB6C102CCF139EB3CF681835AF602182E4F777E637A816A687431,
  and
  02D0EEEB094CDBB8DD974883E2A5D124FBB123A2EF8BF70B5C4A598425639327.
  All adverse build, parser, path-normalization, optional-dependency,
  long-path, and bounded-crop attempts remain recorded with explicit
  no-source-mutation or superseding resolutions.
- English R84 validation is PASS/errors empty at 16,128 bytes / 332 lines /
  SHA-256
  1BBFC3699FA46963B0818E655DC8A52D11BE53D8A81B2A0772E2ABB19EB551AE;
  French R62 is PASS/errors empty at 15,178 bytes / 310 lines / SHA-256
  6463BC1513088A20797B180C252BE4AFD7B609B260B525C958C237CD382B27CE.
  Identity, ordinal-manifest, LF projection, source-slice, label-target,
  fragment-inverse, intentional-open-scope, scaffold-placement, process, and
  mapping checks pass. No global build/render, publication, upload, archive,
  remaining XeLaTeX process, temporary crop, or drive mapping remains.
- Next paired cursor: create/replay complete R85 before any p.140 English
  source mutation, then use NUMDAM PDF one-based p.139 / printed p.140,
  beginning Remark 5.5.12 clause (iv). Do not place or remove a temporary
  French source close.

## 2026-08-04 -- paired French recheck, EGA I printed p.140 sealed

- This terminal entry supersedes every older cursor receipt while preserving
  all append-only decisions, failed diagnostics, superseded artifacts, and
  exact reversals.
- Direct NUMDAM PDF one-based p.139 / printed p.140 was read from one bounded
  600-dpi image, 1,611,884 bytes / SHA-256
  53C5CB09587812441B5A5ED0C6DB1451E3A63C106EBEDFB7FD33CF421536A93B.
  One genuinely needed punctuation crop was inspected at original detail and
  removed; no OCR was run.
- Appended Remark 5.5.12 clauses (iv)--(vi), both proof blocks, the reduction
  square and alternate clauses, 5.5.13, section 6, subsection 6.1, Definition
  6.1.1, and the following paragraph through the exact fragment
  `Tout sous-$\mathscr{O}_X$-`. source/ega1/ega1-5-fr.tex is 50,232 bytes /
  1,149 lines / SHA-256
  4610C5F9E732D99948AA809ED64C85D236423990C2750A06F0DC7A805D317701;
  its exact inverse truncates to sealed p.139 at 47,116 bytes / SHA-256
  D8168125192DF12B1765D4F81E8DD2A15D37378370454F4370E0A3F18C3BC055.
  New source/ega1/ega1-6-fr.tex is 694 bytes / SHA-256
  0292AFD987807F3045A61D94F56A2344684A539439013DE19091181E369F859F
  and reverses only by hash-guarded removal. No live environment is open.
- The first rendered French source carried a comma after the reduction
  square's bottom-right Y inherited from English. Direct authority has no
  comma. Only that French punctuation was removed; the old/new fragment
  hashes, comma-bearing source identity, first build, crop identity, and exact
  inverse all remain in the ledgers. This records a fidelity repair, not an
  unannounced claim that the author was wrong.
- The paired p.140 English slices total 3,214 bytes / SHA-256
  AECF8D9C3BD19AA2CDB86B074270F09921732D829417AFA04F67C41FB0E775A7
  and required zero source mutation. The ledger explicitly retains the
  reordered page-boundary position, Noetherian capitalization, and the
  English diagram comma as sentence punctuation. R86 is 53,233 bytes / 1,150
  lines / SHA-256
  1AACEE47C3D247A51FAC9790F44B8B4291AD670DB299986CEC6F056638063F8B;
  all 127 rows, 7,281,856 aggregate bytes, and ordinal tree SHA-256
  3DD3F9B92DBC78C7334C1F194836E9F4181DF2FE87A8A3905D64947F51576F6C
  exactly preserve R85.
- The final two-pass French bounded reader is 43 pages / 381,772 bytes /
  SHA-256
  3952A572810DD80868F84C80C4FDD3165C538F1F27576546D2C87AD9F0E887F6;
  pages 42--43 pass text-layout QA and page 42 passes visual QA with the
  direct-authority diagram punctuation. The three-pass English reader is 30
  pages / 227,500 bytes / SHA-256
  29AA995989C8EED0293505EEBF32CFDA4C40C4743C443B041C1566CA5ECBF267;
  pages 29--30 pass text-layout QA. Both builds preserve the inherited p.139
  warning profiles and add no hard errors or build-only closes.
- The unique p.140 scaffold block follows p.139 as the terminal heading:
  110,209 bytes / 1,867 lines / SHA-256
  42B41EE3099E81D8D32B59ED957F1790EFBF83BC1BC09F535B5D53D04CC0CD32.
  French, English, and workflow ledgers parse at 11, 13, and 26 rows / SHA-256
  0812FA43B5C655AD90F62249CD6C82DB651231344C5248CAAAE13C473DC9CD15,
  6C1741A51DF3E3371E0503C47CF5F25D40C336A7780D6FE3DEC649C7AAB9FABC,
  and
  738585AFF1AE7363E113DB039FC29859E1FDECE29EC51F24B73652E42E856CDD.
  Every recorded adverse event remains present, including the scaffold
  misplacement, superseded comma-bearing build, path/tool failures, repeated
  parser error, and alias collision, each with no-source-mutation or exact
  successor evidence.
- English R86 validation is PASS/errors empty at 14,728 bytes / 315 lines /
  SHA-256
  0CA69172635D18391445CD58E9186CD96F0428B505D4A1602C8E31C93B094DF9;
  French R63 is PASS/errors empty at 15,819 bytes / 329 lines / SHA-256
  947BF36318ABA08B46674E6C94D49078651B817BAFE1C53DB059CE9F1109FDD6.
  Identity, ordinal-manifest, source-slice, label-target, exact-inverse,
  environment-balance, scaffold-placement, warning-profile, process, and
  mapping gates pass. No global build/render, publication, upload, archive,
  remaining XeLaTeX process, temporary crop, drive mapping, or agent remains.
- Next paired cursor: create/replay complete R87 before any p.141 English
  source mutation, then use NUMDAM PDF one-based p.140 / printed p.141 and
  continue source/ega1/ega1-6-fr.tex after
  `Tout sous-$\mathscr{O}_X$-`. Place the p.141 marker at the true
  continuation; no French source close must be removed.

## 2026-08-04 -- printed p.140 receipt-order control successor

- The complete p.140 French STATUS receipt was appended before its existing
  p.139 successor because a repeated terminal anchor matched early. The
  adverse placement and its previously sealed validator identities remain
  visible. No historical receipt was deleted or moved; a terminal p.140
  STATUS successor now controls.
- The workflow ledger therefore gains exactly one no-source-mutation row and
  is final at 20,658 bytes / 27 parse-clean unique-ID rows / SHA-256
  E58DBC28BE8369CA3649CC4E106825206A8517970B3EC221134216B0B9CA5A0E.
  English R86 validation is rebound, PASS/errors empty, at 14,728 bytes / 315
  lines / SHA-256
  09041AA2A2E206C09256857D4A9A6447E0EF6322D8FD6CB9A4524FA2D4EB5F23;
  French R63 is rebound, PASS/errors empty, at 15,819 bytes / 329 lines /
  SHA-256
  730E1C8D71CF9F063349CE6797D0C4F3966615A45E2BF66F8D957F3E7E4E9FCD.
- No French or English source byte, manifest row, PDF, scaffold, authority
  artifact, or French/English decision row changed. Printed p.140 remains
  sealed through `Tout sous-$\mathscr{O}_X$-`; create/replay R87, then continue
  direct NUMDAM PDF one-based p.140 / printed p.141 with no close to remove.

## 2026-08-04 -- final printed p.140 receipt-control successor

- A second French STATUS successor and the first continuation identity block
  also matched repeated contexts. All misplaced blocks remain preserved. The
  final appends use independently counted unique terminal anchors; no source,
  manifest row, build, authority, scaffold, or substantive decision changed.
- Final workflow ledger is 23,071 bytes / 29 parse-clean unique-ID rows /
  SHA-256
  A736395707953F046D095A6A6F2EF4CB856F752F5045A1714260B32295C5E1D0.
  Final English R86 validation is PASS/errors empty at 14,728 bytes / 315
  lines / SHA-256
  17324EC59ECCC5E0E9B9C5905190B841435EE7C07F5C485665E765215FE6F4DC;
  final French R63 is PASS/errors empty at 15,819 bytes / 329 lines / SHA-256
  3D8088D1C25BD1925B80083CF44618FE2CDEACFF2C254E09FCCD792FD9C75235.
- Printed p.140 remains sealed through `Tout sous-$\mathscr{O}_X$-`. First
  create/replay complete R87; then continue direct NUMDAM PDF one-based p.140
  / printed p.141. No French source close must be removed.

## 2026-08-04 -- final printed p.141 control-identity successor

- Direct NUMDAM p.141 closes the cross-page coherent-module paragraph,
  supplies the local-cover observation, and gives Propositions 6.1.2--6.1.4
  through the exact finite-$D(f_i)$-cover semicolon. The p.140 half of the
  visibly italic cross-page phrase required one typographic fidelity
  successor. This is not an author correction; the ledger records both
  fragment hashes and the exact inverse.
- French source/ega1/ega1-6-fr.tex is 5,074 bytes / 105 lines / SHA-256
  75A77003BDC90E8F0809F0DBF324A1F45268BC7A39C557D5A78C62816168B95B.
  Seven environment starts and six ends encode only the intentionally open
  proof of Proposition 6.1.4. The exact two-step inverse reproduces p.140
  SHA-256
  0292AFD987807F3045A61D94F56A2344684A539439013DE19091181E369F859F.
- Reconstructing the French caught one real English mathematical
  imprecision: the inherited line made the corresponding ideal-sheaf
  sequence merely a sequence rather than an increasing sequence. The same
  reversible line restores omitted provenance 1.3.7 and the printed canonical
  equivalence instead of silently flattening it to equality. A separate
  17-byte repair restores oldpage 142. No claim is made that the author was
  wrong.
- English source/ega1/ega1-6.tex is 54,737 bytes / 839 lines / SHA-256
  BA45F1965B6085D84CA7E3723E4078039093ACFDDD916FD191AD43DE251CA980.
  Its exact inverse reproduces R87 at 54,682 bytes / SHA-256
  357725613444BBBD373C6F7983A958807EC2C94AF1A972BDF5B2519A5A74FE9D.
  Cross-page English placement, Noetherian capitalization, and parenthesized
  condition letters remain explicit retained normalizations.
- R88 is 54,107 bytes / 1,162 lines / SHA-256
  76E4ACFF554773770EBC1C53C87E02A3F4CC54D3EA8CE81898DA6D5B9BF9B0E6.
  All 127 files / 7,281,911 bytes replay to ordinal tree SHA-256
  5AAE163319428FB1DDB52411C7F5CAB6AFA90235FB32C7ADE2AFD6203E6D4C25;
  exactly ega1/ega1-6.tex changes from R87 by +55 bytes.
- The three-pass French bounded reader is 43 pages / SHA-256
  833844565C2D05E098455F36DF403B2438671716B32E30E0F48F52374C070C1D
  and page 43 passes visual QA. The three-pass English reader is 31 pages /
  SHA-256
  B0802C9A4F68EA07E9EA785330C8722956B91FD74F408274E8F772CA81DCED65;
  pages 30--31 pass text-layout QA. Warning profiles match p.140. The failed
  French R1 build remains preserved as adverse evidence.
- The p.141 scaffold is terminal at 115,599 bytes / 1,958 lines / SHA-256
  E5BCB61BB2C8CBF65B628253E62B2F5579D9821C15078BFF25A12880ADDDC689.
  It records statement, proof-use, sequence, object, identification,
  reference, repair, normalization, and open-range edges without claiming
  completed Stacks exposition or formalization.
- French and English decision ledgers remain parse-clean at 11 rows each.
  Final workflow is 20,189 bytes / 22 unique-ID rows / SHA-256
  8744745815106FA65635512D34E1EA9DC3C93090735583DF2247F200600DA90F.
  English R88 validation is PASS/errors empty at 15,431 bytes / 326 lines /
  SHA-256
  288BC03CD1D8E9DB2B291B9CA7369DD8670A9D912C0C70EBE2FCE126F4C8F529;
  French R64 is PASS/errors empty at 16,534 bytes / 353 lines / SHA-256
  027E1BB4FC646376CAC767DCFA08933C86AE657719BAAA99A8DBF68A6DF6CAF7.
- Next gate: create/replay R89, then continue direct NUMDAM PDF one-based
  p.141 / printed p.142 in the already-open proof of Proposition 6.1.4. Add
  oldpage 142 at the true French continuation; add or remove no temporary
  proof close.
