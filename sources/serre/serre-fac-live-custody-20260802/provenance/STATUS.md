# Serre FAC English/French source-aligned successor — status

Status: ACTIVE PRODUCTION; not complete and not publication-ready.

## Objective

Produce a complete source-aligned English TeX/PDF of Jean-Pierre Serre's *Faisceaux algébriques cohérents* through printed page 278, while preserving an immutable diplomatic French layer and propagating every source-established repair into a separate corrected French layer.

## Controlling authority

- 1955 *Annals of Mathematics* scan, 83 physical PDF pages / 82 printed article pages (197--278).
- SHA-256: `B8C6508249308F5D8BC886B9E6360F1EC4FDC8F0F18EFAA03EE0E36B591551CA`.
- The complete French TeX is a transcription/drafting layer, not authority.
- No standalone English FAC translation was found in the searched local corpora; the English workpass is a new translation.

## Controlling current snapshot

- Continuous English coverage: `FAC-EN-U0001`--`FAC-EN-U0041`, French `fac_body.tex` lines 1--1486, printed pages 197--236, through Chapter II, §3, no. 43.
- Exact next cursor: French `fac_body.tex` line 1489 / printed page 236 / no. 44, `Nullité de certains groupes de cohomologie`.
- English master: `english_source_first_workpass/source/Serre_FAC_English_source_aligned_workpass.tex`, 4,040 B, SHA-256 `2D8D07E0BCD653456820779AE3B9C7D47FBE1629946C82E52E61D16BF610675D`.
- English checkpoint: `build_checkpoint_II_3_43_r2`, 37 A4 pages / 566,556 B / SHA-256 `D95A762FCA5CC0327CA024C475B883D9B63BBFB47EEEAEFDC78CE6CCA6680580`; three-pass convergence, affected pages 36--37 personal visual PASS.
- Diplomatic French T0024 checkpoint: 63 pages / 634,126 B / SHA-256 `BABAE9A9A1E49ECAF66196B827C2633868E5607816873348C236A1A52A781065`.
- Corrected French C0027/T0024 checkpoint: 63 pages / 634,414 B / SHA-256 `6B962F5B36E4EDF148C0E8FE27613AC9F483D962C758041863ED8826B93A0A29`.
- Decision accounting: 27 printed-source corrections, 24 transcription-repair groups, 31 append-only self-correction events (23 affected textual/ledger occurrences), and 1,666 occurrence-level English normalization rows. Known post-admission mathematical/translation reversals: 0.
- This snapshot controls over the chronological checkpoint history below. FAC remains active production, not complete or publication-ready.

## Chronological English coverage history

- Unit `FAC-EN-U0001`: French `fac_body.tex` lines 1--115.
- Authority physical PDF pages 2--5; printed pages 197--200 through the end of no. 2, “Sections of a sheaf.”
- Target: `english_source_first_workpass/source/components/001_opening_introduction_contents_and_I_1_1_2.tex`.
- Gate: three-pass build and 3/3 rendered-page visual check PASS.
- Checkpoint PDF SHA-256: `75574FF08920D72B136A38326F70B6DB18C8673340FC34F172519805448AC935`.

- Unit `FAC-EN-U0002`: French `fac_body.tex` lines 116--162.
- Authority physical PDF pages 5--6; printed pages 200--201; no. 3, “Construction of sheaves,” complete.
- Target: `english_source_first_workpass/source/components/002_I_1_3_construction_of_sheaves.tex`.
- Gate: cumulative three-pass build and rendered-page visual check PASS.

- Unit `FAC-EN-U0003`: French `fac_body.tex` lines 163--179.
- Authority physical PDF pages 6--7; printed pages 201--202; no. 4, “Gluing of sheaves,” complete.
- The first source typo found during alignment is corrected transparently in the corrected French layer and English: printed `\Gamma(U_i,\mathfrak F_i)` to contextually required `\Gamma(U,\mathfrak F_i)`. The diplomatic French remains unchanged.
- Gate: cumulative English three-pass build and rendered-page visual check PASS; corrected French three-pass build and repaired-page visual check PASS.

Current English checkpoint: 4 A4 pages / 264,001 B / SHA-256 `C937E1113758CF4E65913D5B8EAC9009E923B3F30102F484CD63CE4FCBE144BF`.

Current corrected French checkpoint: 63 A4 pages / 634,039 B / SHA-256 `F7515D8657BCC986127E4D8D46041792752E55D8A06B8C6FCA32829F211FC56B`.

- Unit `FAC-EN-U0004`: French `fac_body.tex` lines 180--201.
- Authority physical PDF page 7; printed page 202; no. 5, “Extension and restriction of a sheaf,” complete.
- The second source typo is corrected in corrected French and English: the printed restriction-map direction $\mathfrak F_U\to\mathfrak F_V$ is replaced by $\mathfrak F_V\to\mathfrak F_U$. Diplomatic French remains unchanged.
- Current gate: translation and French repair written; cumulative rebuild pending.

- Unit `FAC-EN-U0005`: French `fac_body.tex` lines 202--218.
- Authority physical PDF pages 7--8; printed pages 202--203; no. 6, “Sheaves of rings and sheaves of modules,” complete.
- Three inherited `\epsilon` membership signs were verified against the authority as `\in` and repaired in both French working layers; these are transcription repairs, not printed-source defects.
- Current gate: translation and three French transcription repairs written; cumulative rebuild pending.

- Gate: cumulative English three-pass build and rendered pages 4--5 visual check PASS; diplomatic/corrected French three-pass builds and affected-page visual check PASS.
- Current English checkpoint: 5 A4 pages / 279,818 B / SHA-256 `54F013B97AE6A6AA89A2D215995E6BD6621B2C28CA0074B9B6A35E99E1D841BB`.

- Unit `FAC-EN-U0006`: French `fac_body.tex` lines 219--242.
- Authority physical PDF pages 8--9; printed pages 203--204; no. 7, “Subsheaf and quotient sheaf,” complete.
- Four further inherited `\epsilon` membership readings were verified against the authority as `\in` and repaired in both French working layers.
- Gate: cumulative English three-pass build and rendered pages 5--6 visual check PASS; both French layers rebuilt and the affected page visually checked.
- Current English checkpoint: 6 A4 pages / 293,517 B / SHA-256 `0F506997F04B60DA44D553374FB961CB3541D8EA21B6482CDDF1D899DB201F3F`.

- Unit `FAC-EN-U0007`: French `fac_body.tex` lines 245--266.
- Authority physical PDF pages 9--10; printed pages 204--205; no. 8, “Homomorphisms,” complete.
- Three further inherited membership-sign groups were repaired in both French layers. A printed-source type error omitting the stalk subscripts from `\mathcal{F}_x` and `\mathcal{G}_x` is preserved diplomatically and corrected/disclosed in corrected French and English.
- Gate: cumulative English three-pass rebuild and rendered page 7 visual check PASS after replacing LaTeX's misleading built-in imaginary-part `\Im` glyph with roman `\operatorname{Im}`.
- Current English checkpoint: 7 A4 pages / 306,105 B / SHA-256 `BC40A96BF77D4ECE0A5D61055B5079D6A2822F9ECDB0EEB2AEA251CE253D2B99`.

- Units `FAC-EN-U0008` and `FAC-EN-U0009`: French `fac_body.tex` lines 269--310.
- Authority physical PDF pages 10--11; printed pages 205--206; nos. 9, “Direct sum of two sheaves,” and 10, “Tensor product of two sheaves,” complete.
- Corrected French repairs the printed grammatical mismatch `partie ... formés` to `partie ... formée`; diplomatic French preserves the print.
- Gate: cumulative English three-pass build and rendered pages 7--8 visual/formula check PASS; corrected French three-pass build and repaired-page visual check PASS.
- Current English checkpoint: 8 A4 pages / 317,086 B / SHA-256 `E62FE5F954D71FF1F39D4084CEA8FEB032F352EAC4B5F08E2AB79382B27AC131`.
- Current diplomatic French checkpoint: 63 A4 pages / 634,045 B / SHA-256 `BA63F34D13505E28A4738A368BBB9BC9D7863D5D8C06C74BAB73B9A2D29E7503`.
- Current corrected French checkpoint: 63 A4 pages / 634,061 B / SHA-256 `6836950A1B1FC0DEBEDDBEC0F4B9A664F5B770B7532BFB7C8175786D02B44263`.

- Units `FAC-EN-U0010` through `FAC-EN-U0012`: French `fac_body.tex` lines 313--458.
- Authority physical PDF pages 11--15; printed pages 206--210; nos. 11--14 complete, including the transition into Chapter I, \S2 and the main coherence theorems.
- Five additional inherited `\epsilon` membership groups were verified directly against the authority as printed `\in` and repaired in both French working layers (repairs `FAC-FR-T0011`--`FAC-FR-T0015`). No new printed-source defect was admitted in this tranche.
- The first no. 14 render exposed a missing TeX backslash that printed `qquad`; the defective r1 build remains historical and was superseded by a corrected r2 rebuild.
- Gate: cumulative English three-pass build and rendered pages 8--12 visual/formula check PASS; both French layers rebuilt and the affected corrected-French pages passed 600-dpi visual inspection.
- Current English checkpoint: 12 A4 pages / 343,184 B / SHA-256 `8BFB8D8B04F915CD9C9A89AE47598AEBADB623A0C2ED93428DA37672FBE7E462`.
- Current diplomatic French checkpoint: 63 A4 pages / 634,048 B / SHA-256 `3391817CFACFF28AC3DCFB1C981F20D3F3B21381753953739A791348001BC4FD`.
- Current corrected French checkpoint: 63 A4 pages / 634,064 B / SHA-256 `C14FD56264A1A8C7FE956BB016B760BFF9751F392454194887F04C0D6C6D1007`.

- Units `FAC-EN-U0013` through `FAC-EN-U0015`: French `fac_body.tex` lines 461--514.
- Authority physical PDF pages 15--17; printed pages 210--212; nos. 15--17 complete, including coherent sheaves of rings, change of rings, and extension by zero.
- Printed-source repair `FAC-FR-C0005` changes the impossible reference `condition (b) de la Proposition 2` to `condition (b) de la Définition 2` in corrected French and English, with an explicit English editorial footnote; diplomatic French preserves the printed wording.
- Gate: cumulative English three-pass build PASS with identical pass-2/pass-3 console logs, zero diagnostics, and rendered pages 12--13 visual/formula PASS. Corrected French three-pass build PASS with the four inherited layout diagnostics only; corrected reader page 11 visual PASS.
- Current English checkpoint: 13 A4 pages / 352,543 B / SHA-256 `6047943E980DADD5323574F0ED2AA7D41C5A873A57DFDC23B7E070F330A203E4`.
- Current corrected French checkpoint: 63 A4 pages / 634,065 B / SHA-256 `A27F8AC6ABE1745CA41E24D97B8A62EAE64F25711D4679971CF2170EFE9FC41B`.

- Units `FAC-EN-U0016` through `FAC-EN-U0018`: French `fac_body.tex` lines 517--629.
- Authority physical PDF pages 17--19; printed pages 212--214; Chapter I, \S3 opening and nos. 18--20 complete.
- Authority comparison repaired `FAC-FR-T0016` (`\rho^{s'}` to `\rho_s^{s'}`) and `FAC-FR-T0017` (two `i\epsilon I` membership signs to `i\in I`) in both French working layers.
- The first English no. 20 build printed two literal `qquad` strings because TeX spacing backslashes were lost. The r1 build is rejected/history; r2 restores both `\qquad` commands.
- Gate: admitted r2 English three-pass build PASS, pass-2/pass-3 console byte equality, zero diagnostics, and rendered pages 14--15 visual/formula PASS. Both French layers three-pass PASS; corrected French pages 12--13 visually confirm the repaired restriction-map subscript and membership signs.
- Current English checkpoint: 15 A4 pages / 380,179 B / SHA-256 `AD99D9E384873A9BDFC798FE5881F0E771D7F5B6F55B0370BD114F0F63CBCA8F`.
- Current diplomatic French checkpoint: 63 A4 pages / 634,057 B / SHA-256 `708EA4F41DB259C9A7564E1EA06D06583407115AF3E402B5BD4BD7E17CA67AA9`.
- Current corrected French checkpoint: 63 A4 pages / 634,074 B / SHA-256 `A035907C1DAF3CC2D0708AE27EABC20A4843E2D22837471DE825BC0B0C4ABA21`.

- Units `FAC-EN-U0019` through `FAC-EN-U0021`: French `fac_body.tex` lines 631--707.
- Authority physical PDF pages 19--21; printed pages 214--216; nos. 21--23 complete: refinement of coverings, the definition of $H^q(X,\mathcal F)$ as a direct limit, and functoriality under sheaf homomorphisms.
- `FAC-FR-T0018` repairs four inherited membership signs (`\epsilon` to printed `\in`) in both French layers.
- Direct authority comparison caught and reversed one unjustified English normalization before admission: Serre's upper summation limit `h=q-1` had initially been shortened to `q-1`. The r2 English source preserves the authorial notation; `FAC-SELF-0004` records the global search and repair.
- Gate: English r2 compiled in three passes to 17 A4 pages with byte-identical pass-2/pass-3 console logs and zero diagnostics; output pages 15--17 passed lead visual/formula comparison. Both French layers compiled in three passes with zero hard diagnostics and the same four inherited layout notices; corrected-French pages 14--15 passed 600-dpi visual comparison.
- Current English checkpoint: 17 A4 pages / 394,142 B / SHA-256 `B34B46164C064B230A035CF292FECDA28A4B03D2A402D58C26C5E352B7DB490C`.
- Current diplomatic French checkpoint: 63 A4 pages / 634,055 B / SHA-256 `4FC6AD4F8167284C738BB97E488B30DCBE77CC4B4C679BB42D9082F4E1E82B78`.
- Current corrected French checkpoint: 63 A4 pages / 634,072 B / SHA-256 `C8E25BFFF681A297A366A3233CEE7354C3242AD6B2E2F19DF4A21807FA207218`.
- Human-readable rationale is controlling in `EDITORIAL_DECISION_LOGBOOK.md`; exact self-correction history is in `controls/EDITORIAL_SELF_CORRECTION_LEDGER.csv` (five events, seven affected textual occurrences, no known post-admission mathematical/translation reversal).

- Unit `FAC-EN-U0022`: French `fac_body.tex` lines 710--815.
- Authority physical PDF pages 21--22; printed pages 216--217; no. 24, “Exact sequence of sheaves: the general case,” complete.
- Printed-source repair `FAC-FR-C0006` changes the impossible phrase “choice of the map $\tau^*$” to “choice of the map $\tau$” in corrected French and English; the diplomatic French retains the print and the English discloses the intervention.
- Printed-source repair `FAC-FR-C0007` restores the source's inkless missing term as $0$ after “cohomologous to,” since $\tau z=d(\tau f)$ in the subcomplex. Diplomatic French preserves the visible blank; corrected French and English restore and disclose $0$.
- The authority's $C'_0$ prime was checked directly at 1100 dpi and retained; it is the alternating subcomplex notation, not a numeral or an editorial normalization. A 5000-dpi Poppler attempt was abandoned after full-page allocation produced blank crops and a memory-allocation error; no reading depends on those failed crops.
- Gate: English three-pass build PASS with byte-identical pass-2/pass-3 consoles, zero diagnostics, and pages 16--18 visually/formula checked. The native diagram has exactly eight nodes and nine arrows, including three downward arrows labelled $\tau$ on the left. Corrected French three-pass build PASS with zero hard diagnostics and the four inherited layout notices; pages 15--17 visually checked at 600 dpi. Diplomatic French is byte-unchanged from the T0018 checkpoint.
- Current English checkpoint: 18 A4 pages / 406,362 B / SHA-256 `7036A0F36F6E63EE9CF5BE626519467D41DC0869A65035F7D8BA912AED8D21C9`.
- Current corrected French checkpoint: 63 A4 pages / 634,036 B / SHA-256 `EB55186403BE47AD343216A29407EDAC4BE7D1EBF3853384DA55E338793182C8`.
- Self-correction history now has seven events: four textual/typesetting events, two generated-output-path events, and one continuation-metadata event. The textual occurrence count remains seven; known post-admission mathematical/translation reversals remain zero.

- Unit `FAC-EN-U0023`: French `fac_body.tex` lines 817--871.
- Authority physical PDF pages 22--23; printed pages 217--218; no. 25, “Exact sequence of sheaves: the case where X is paracompact,” complete.
- `FAC-FR-T0019` restores the authority's overline in \(x\in\overline W_j\), which the inherited TeX omitted. Both French layers and English now agree with print.
- Printed-source repairs `FAC-FR-C0008` and `FAC-FR-C0009` respectively restore the typed covering \(\mathfrak U\) where print has an undefined plain \(U\), and remove the undefined subscript in \(\beta(b)_x\) where the proof asserts equality of sections over \(U_{x_0}\). Diplomatic French preserves both printed defects; corrected French and English repair and disclose them.
- Gate: English three-pass build PASS with byte-identical pass-2/pass-3 consoles, zero hard diagnostics, no overfull boxes, one harmless underfull notice, and pages 18--19 visually/formula checked. Both French layers three-pass PASS with zero hard diagnostics and the same four inherited layout notices; reader page 17 in each layer passed 600-dpi visual comparison.
- Current English checkpoint: 19 A4 pages / 423,823 B / SHA-256 `DF27EF14278C56A50E1CA91E7E709941F419FFF0EEE2C920928E1A3B40F53BE1`.
- Current diplomatic French checkpoint: 63 A4 pages / 634,075 B / SHA-256 `C2BAAE5FAB4DD28D45C834D8C07A158D9FFDE73224E13E9C4E179590C70C0E22`.
- Current corrected French checkpoint: 63 A4 pages / 634,030 B / SHA-256 `CE496B257A7E56FCC2D8F48F5EB939EA0C39074D798622DA686FB0403423CD3D` (`build_checkpoint_C0009_T0019_r3`).
- Current occurrence ledger: 1,059 unique rows / 385,384 B / SHA-256 `0BCD7F498E0CF1D71823A904CAA04952333ECE80D2D45887548ACBE1272B20BA`. `FAC-SELF-0008` supersedes the underinclusive calligraphic-letter regex; `FAC-SELF-0009` retroactively binds the seven existing “Hausdorff/non-Hausdorff” normalizations under policy `FAC-EN-N0013`. Neither changes English source bytes.
- Self-correction history now has ten events: four textual/typesetting events, two generated-output-path events, one continuation-metadata event, two provenance-ledger coverage events, and one pre-admission line-geometry repair. `FAC-SELF-0010` restores exact 3,447-line alignment between the French layers after an explanatory comment expansion shifted corrected-layer locators. Known post-admission mathematical/translation reversals remain zero.

- Unit `FAC-EN-U0024`: French `fac_body.tex` lines 873--892.
- Authority physical PDF pages 23--24; printed pages 218--219; no. 26, “Cohomology of a closed subspace,” complete.
- Printed-source repair `FAC-FR-C0010` removes the authority-confirmed stray comma in the defining equality (U'_{i_0\ldots i_q}=Y\cap U_{i_0\ldots i_q}) from corrected French and English; diplomatic French preserves the print and English discloses the repair.
- Gate: cumulative English three-pass pdfLaTeX build PASS and pages 19--20 visual/formula check PASS; corrected French three-pass build PASS and reader page 17 visual check PASS.

- Unit `FAC-EN-U0025`: French `fac_body.tex` lines 895--935.
- Authority physical PDF pages 24--25; printed pages 219--220; Chapter I, \S4 opening and no. 27, “Double complexes,” complete.
- `FAC-FR-C0011` repairs the definition of (K_h): print sums only over (q\ge h), leaving (p) free; corrected French and English sum over (p\ge0,q\ge h). `FAC-FR-C0012` repairs the transposed row-cohomology term (H_I^{h,n-h}) to (H_I^{n-h,h}). The 1100-dpi authority confirms both defective forms are printed; diplomatic French preserves them; English footnotes disclose both interventions.
- Gate: admitted English `build_checkpoint_I_4_27_r4` compiled in three pdfLaTeX passes to 21 A4 pages / 455,746 B / SHA-256 `1D56249F9DC1DDC21AED4E5EF5B08725D7360879C514000DF3A7E1AA06FD73E4`; pass-2/pass-3 console SHA-256 `3D24FDC56D97652E649C51349806F39B259D2CE4D65DE5AB2B20B6AFD021681B`; zero hard/undefined/overfull diagnostics and one harmless underfull notice. Pages 20--21 passed personal visual/formula review.
- Corrected French `build_checkpoint_C0012_T0019_r2`: 63 A4 pages / 634,017 B / SHA-256 `0D6A4E90F42B3251AB113C2892410312D12D93A8427FAED6E232F39692D590BF`; pass-2/pass-3 console SHA-256 `913075B46D5961FA6EBA7539876CE48E8109A07D6A2F4092D13534DA5501B612`; zero hard diagnostics and the same one overfull/three underfull inherited notices. Reader page 18 passed personal 600-dpi review.
- `FAC-SELF-0011`--`FAC-SELF-0014` preserve four pre-admission process corrections: wrong TeX engine selection, a mathematically correct but pagination-disruptive two-line subscript, a PowerShell `$args` collision, and repair of two provisional non-rectangular self-correction rows. None changed an admitted translation or diplomatic source. Known post-admission mathematical/translation reversals remain zero.

- Unit `FAC-EN-U0026`: French `fac_body.tex` lines 938--1015; authority physical pages 25--26 / printed pages 220--221; no. 28, “Double complex defined by two coverings,” complete.
- `FAC-FR-C0013` restores the omitted `\hat{i}_k` in the target intersection of the restriction map. The cochain being restricted is indexed with `i_k` omitted, so the larger target intersection must omit it as well. The native 600-ppi authority image confirms that the hat is absent in print; diplomatic French preserves the source, while corrected French and English restore and disclose it.
- English no. 28 checkpoint: 23 A4 pages / 464,355 B / SHA-256 `E3D3D5A8B170AD7C210194D54F69BF8F0DC4E9D640FBA0AA76C98BB1B4D76226`; three converged pdfLaTeX passes and affected pages 21--23 visual PASS. Corrected French C0013/T0019: 63 A4 pages / 634,035 B / SHA-256 `84E745319DF6C667BEBDA678F548C0F61F7B2442B67C1ACCACC17F535EB178CE`; page 19 visual PASS.

- Unit `FAC-EN-U0027`: French `fac_body.tex` lines 1017--1102; authority physical pages 26--27 / printed pages 221--222; no. 29, “Applications,” and Chapter I complete.
- `FAC-FR-C0014` restores the diaeresis in `coïncide`. `FAC-FR-C0015` reverses the printed, ill-typed composite to `\iota''^{-1}\circ\iota'`; `FAC-FR-C0016` removes the undefined terminal index `j_{n-p}` in favor of `j_{n-p-1}`; and `FAC-FR-C0017` restores the domain of `\iota'` to `H^n(\mathfrak U,\mathfrak F)`. All four printed readings were confirmed directly at 1100 dpi. Diplomatic French preserves them; corrected French and English repair the mathematical readings, and the English discloses the three mathematical interventions.
- `FAC-SELF-0015` records and closes the lead's own transient `l'homomisme` typo in corrected French before any build existed. Global replay finds zero surviving occurrences; diplomatic French and admitted English were never affected.
- Admitted English checkpoint `build_checkpoint_I_4_29_r1`: 25 A4 pages / 476,617 B / SHA-256 `088BFC1EF031C057BC0BE584294DBD85D787E35796F889722C928F7481ACBF1A`; three pdfLaTeX passes; pass-2/pass-3 console SHA-256 `0F12C8E8B1238D5B9905756BE210F59E995AD8D97D8C4E6E275AF19655CEB62A`; zero hard/undefined/overfull diagnostics and one inherited harmless underfull notice. Pages 22--25 passed personal visual/formula review.
- Admitted corrected French checkpoint `build_checkpoint_C0017_T0019_r1`: 63 A4 pages / 634,358 B / SHA-256 `7669E342775FA565B46728AB030DB1839DE3F24869B41BBDA78E52F3F9A0D5A0`; pass-2/pass-3 console SHA-256 `67B1A783CE13AF4673B67E062D7D23D165B45267487ED94221B714D2799AA5C0`; zero hard diagnostics and the inherited one overfull/three underfull notices. Pages 19--20 passed personal 600-dpi review.

Historical cursor after `FAC-EN-U0027`: French `fac_body.tex` line 1104, printed page 222, Chapter II heading and §1, no. 30, `Espaces vérifiant la condition (A)`. This cursor is superseded by the controlling line-1353 cursor above.

- Units `FAC-EN-U0035`--`FAC-EN-U0036`: French `fac_body.tex` lines 1321--1351; authority physical pages 35--36 / printed pages 230--231; nos. 37--38 complete.
- `FAC-FR-C0027` balances the first printed quotation around the polynomial relation in no. 37; diplomatic French preserves the unmatched closing quote, while corrected French and English supply the opening mark. `FAC-FR-T0023` repairs inherited `\mathcal J_x(\mathrm V)` to the authority's `\mathcal J_x(V)` in both French layers.
- English `build_checkpoint_II_2_38_r1`: 34 A4 pages / 533,965 B / SHA-256 `0A2C1575E66454FA9BDD42BCBFD1D1AF863B795B52CB9D3E2A501CB596F2AD88`; pass-2/pass-3 consoles are byte-identical; no hard, undefined, or overfull diagnostics; pages 33--34 personal visual/formula PASS.
- Diplomatic T0023 and corrected C0027/T0023 both build in three passes to 63 pages. Their page 26 renderings passed personal comparison; corrected French changes only the admitted reading, while diplomatic French preserves print.

## Boundaries

- The frozen French source at `<REDACTED_LOCAL_ROOT>/w\e620\sources\serre\serre-fac-complete-working-transcription-20260731` is read-only input and remains untouched.
- FAC is disjoint from the live Deligne and EGA lanes. GAGA follows FAC; no GAGA source is mutated in this checkpoint.
- No new OCR is generated. Authority images are rendered directly from the controlling PDF at 1100 dpi for this opening tranche; higher detail is reserved for genuinely ambiguous small notation.
- Controlling provenance rule: `00_lane_control/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md`, 2,296 B, SHA-256 `BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679`. Every immutable handoff must bind privacy-clean logbook identities, and archive maintenance must deposit them in both the methodology and replication DOI records. Mutable FAC logs remain local until a bounded/final freeze.
- Archive task `<REDACTED_TASK_ID>` acknowledged that rule under decision `EG-ARCHIVE-DUAL-DOI-LOGBOOK-CUSTODY-CONTROL-20260802-0001`, naming methodology DOI `10.5281/zenodo.21124403` and replication DOI `10.5281/zenodo.20461174`. It accepted and uploaded no FAC artifact; FAC remains mutable production.
- Occurrence-level English normalization ledger through no. 43: `controls/ENGLISH_NORMALIZATION_OCCURRENCES.csv`, 1,666 unique rows / 604,282 B / SHA-256 `5F437256D0E6337B6365B18561CDF88742B6743C36176DA02F73B39716A163C8`.

## 2026-08-02 — Chapter II §2 no. 39 through §3 no. 43

- `FAC-EN-U0037`--`FAC-EN-U0041` translate French lines 1353--1486 / authority physical pp. 36--41 / printed pp. 231--236: the closed-subvariety ideal sheaf, fractional-ideal sheaves, the sheaf of sections of a vector-space fiber space, affine varieties, and the preliminary irreducible-variety propositions.
- Nos. 39--42 required no new printed-source correction or inherited transcription repair. Direct 1100-dpi comparison on physical pp. 37--41 controls their prose, formulae, and source footnotes. The English terminology ledger records every recurring choice, including “sheaf of fractional ideals,” historical “algebraic fiber space,” standard “structure group,” “nonsingular” rather than importing modern relative smoothness, and the type-explicit `\Delta\cap(U\times V)` notation.
- `FAC-FR-T0024` repairs inherited upright `\mathrm A` to the authority's italic variable `A` in the first intersection formula of no. 43. Both French layers now match print; this is a transcription repair, not a source correction. French reader page 29 passed personal 600-dpi review after converged three-pass rebuilds.
- The first no. 43 English build supplied an `x` subscript on two sum signs that are unindexed in Serre. `FAC-SELF-0029` records the pre-admission reversal; r2 restores both unindexed sums while retaining the indexed factors. Pages 36--37 then passed personal formula/layout review. `FAC-SELF-0030` records a harmless wrong executable lookup; `FAC-SELF-0031` repairs the provisional N0048 occurrence regex and binds both actual parenthesized-intersection occurrences.
- English `build_checkpoint_II_3_43_r2`: 37 A4 pages / 566,556 B / SHA-256 `D95A762FCA5CC0327CA024C475B883D9B63BBFB47EEEAEFDC78CE6CCA6680580`; pass-2/pass-3 console SHA `CBF06A4144102689CB413C967D7C87DC033BA40357AC721B85EB1122DF9B6F6D`; log SHA `EC2AA055EAD8339F946421B8280C252D0793204F50B5BD99E2A7A5C6FD6DD4B3`; hard/undefined/overfull diagnostics 0, one inherited harmless underfull notice.
- Diplomatic T0024: 63 pages / 634,126 B / SHA-256 `BABAE9A9A1E49ECAF66196B827C2633868E5607816873348C236A1A52A781065`. Corrected C0027/T0024: 63 pages / 634,414 B / SHA-256 `6B962F5B36E4EDF148C0E8FE27613AC9F483D962C758041863ED8826B93A0A29`. Both have byte-identical pass-2/pass-3 consoles, zero hard diagnostics, and only the inherited one overfull/three underfull notices.
- Exact continuation cursor: `fac_body.tex` line 1489 / printed p. 236 / no. 44, “Vanishing of certain cohomology groups.”
