# D006 work log

## 2026-08-02 — opening checkpoint

- Opened this no-overwrite D006 bilingual source-alignment root after exact local closure of D005.
- Bound the selected IAS vector-text authority, comparison PDF, prior scan witness, inherited French/English TeX, and existing GPU OCR locator identities in `controls/INPUT_IDENTITIES.csv`.
- Imported both inherited TeX files through bounded patches. Verified 1,307/1,307 French lines and 1,298/1,298 English lines, normalized content equality, and exact parent file SHA-256 identities.
- No OCR was generated or rerun. No D007 work was opened.
- Current replay cursor: authority page 1 of 20.

## 2026-08-02 — source-language and baseline correction

- Direct PDF-text and metadata inspection established that the selected 2004 IAS source has an English body under the historical French title. The opening assumption that it was a French authority is superseded; English is the source-alignment lane and French is the translation lane for this selected witness.
- The PDF is born-digital/vector text. Its text layer is used only for exact reading and location; formulas and diagrammatic arrays remain subject to direct rendered-source inspection at represented-detail resolution.
- Three-pass French and English baseline builds and a four-pass bilingual build converge with zero required diagnostics. Current provisional readers are 17, 16, and 33 pages respectively.

## 2026-08-02 — targeted weight and spectral-sequence adjudication

- Direct 5,000-dpi authority details confirm that the page-18 exponents are genuinely printed as `p^{k+1/2}` and `p^{i+j/2}`; these are source slips, not OCR artifacts.
- Corrected and visibly disclosed the theorem/lemma readings to eigenvalues of weights `k+1`, `i`, and `i+j`, hence absolute values `p^{(k+1)/2}`, `p^{i/2}`, and `p^{(i+j)/2}`.
- Corrected and visibly disclosed the printed assertion that the Leray differentials are nonzero: equivariance for `psi_m^*` between distinct `m^j`-eigenspaces forces them to be zero, which is the degeneration used immediately afterward.
- Restored genuine Corollary environments for 3.5 and 4.2, corrected both printed `fournishes` occurrences, and normalized the three printed `Peterson`/`Pertersson` variants to `Petersson`, with visible source notes.
- These targeted corrections do not advance the sequential page-by-page cursor, which remains authority page 1/20.
- Direct 5,000-dpi review of the Theorem 2.10 square found that both inherited vertical arrows had replaced printed inclusion symbols. Both editions now retain the two source-faithful vertical inclusions; compiled high-detail verification remains part of the page-6 gate.

## 2026-08-02 — English pages 1--5 closed and canonical French original bound

- Completed direct sequential replay of IAS English authority pages 1--5 at 1,200 dpi, escalating the matrix on page 4 to 5,000 dpi. Restored the missing qualifier “at infinity,” the finite-adele factor `Z_p`, equation tag (2.5), complex-modulus bars, and the source superscript in `\iota^k`; corrected and visibly disclosed the transposed action matrix required by the same-line Möbius formula.
- Rebuilt both standalone editions after these changes. The English reader is 16 pages, SHA-256 `44D3618ED81FC600ECC95F341CB2067ED388991944DC0F0EFF8EFB88FCD7182D`; the French reader is 17 pages, SHA-256 `91DF7712015D39ADFB64494CC8FB27257E477E646B5FA65D6AE01012ADAFB8A3`. Pages 1--6 of both outputs passed direct rendered layout review.
- Located and hash-bound the canonical published French Bourbaki original from NUMDAM: 35 physical pages, 1,975,508 bytes, SHA-256 `19509C19B0CB056F4A5EBA83A48A99F54BB6DF0C7A96AB7F4018B0765E1ED98C`. It is now the controlling French source; the IAS 2004 retype remains the controlling English source. No OCR was generated.
- Targeted direct comparison at French printed pp. 148--149 confirms the bar on the Néron model and confirms that the apparently tautological finite-adele notation is genuinely printed in both witnesses. The inherited normalization and omission were therefore undone source-faithfully rather than silently corrected.
- Sequential cursors are now IAS English page 6/20 and canonical French physical page 2/35 (printed p. 139). Targeted later-page adjudications do not advance either sequential cursor.

## 2026-08-02 — English page 6 closed

- Direct 1,200-dpi replay, with 5,000-dpi formula inspection and a paired 1,800-dpi check of canonical French printed pp. 148--149, closed the entire IAS page 6.
- Restored the overline on the Néron model in all three occurrences; restored the source's quotation marks around “locally constant”; and restored the printed finite-adele formula exactly, including `Q_l=Z_l tensor Q_l` and its terminal `A_T^f=Z-hat tensor A_T^f` identity. The latter is odd but source-stable in both controlling witnesses and is therefore not silently normalized.
- Disclosed the page's obvious English-retype spelling slips collectively. The corrected standalone builds converge with only the engine's benign `inputenc` notice: English 17 pages / SHA-256 `2E81A2FC0CC742008C4EC55FE78782FC76965D5768F227FA6DF339B116276920`; French 17 pages / SHA-256 `1ECBE98F167016AFDB464C25D1FFF15DB6B63154E6AC4E51C5D60A40563560F0`.
- Manually inspected compiled pages 5--7 at 600 dpi for layout only; the Néron notation, finite-adele formula, disclosure notes, section seam, and Proposition 3.3 remain unclipped and legible.
- English sequential cursor advances to IAS page 7/20. French-original sequential cursor remains physical page 2/35 / printed p. 139.

## 2026-08-02 — English pages 7--11 closed

- Completed direct sequential replay of IAS English authority pages 7--11 at 1,200 dpi, escalating the damaged page-8 wording, formula (3.11), and diagrams (3.16)--(3.17) to 5,000-dpi source details. Targeted direct checks of the canonical French original at printed pp. 151--154 adjudicated the English retype where needed; they do not advance the French sequential cursor.
- Recorded source-alignment actions 028--039. Substantive restorations include exact page-8 wording from the French original, the type-correct adelic action, Definition 3.9's second equality and left superscript, the compactification bars in (3.11), and a complete native reconstruction of diagram (3.16).
- The inherited (3.16) array was genuinely topologically wrong: it attached `u` and `v` to `M_{n,p}` and collapsed two separate pullback-to-curve maps. Both editions now use the source's nine-arrow topology. Personal 5,000-dpi source/output comparison passed for arrow direction, attachment, labels, and object placement; no visual judgment was delegated.
- Three-pass standalone builds converge with only the benign XeTeX `inputenc` notice: English 17 pages / 154,975 bytes / SHA-256 `67A4394F4B0D6EABE1193E312908374F172288CACA718E54BA4B1D9D428C0AE2`; French 17 pages / 156,342 bytes / SHA-256 `DFF6D6186E65843B877B4A89F154D7AD4CED3B8564B94F5F4FCE269F1792D7B1`.
- Updated and rebuilt the bilingual reader from those exact standalone PDFs: 34 pages / 325,068 bytes / SHA-256 `6627758DC4B21B8082DF4CE829F58E9B68BECF0C906996B18B9A7511D20104B7`. English/French pages 7--11 and bilingual seam pages 17--18 passed personal 1,100-dpi layout inspection.
- Durable receipt: `qa/ENGLISH_PAGES7_11_SOURCE_BUILD_RENDER_PASS_20260802.md`. English sequential cursor advances to IAS page 12/20. French-original sequential cursor remains physical page 2/35 / printed p. 139.

## 2026-08-02 — English pages 12--15 closed

- Completed direct sequential replay of IAS English authority pages 12--15, using 1,200-dpi page inspection and 2,400--5,000-dpi detail evidence for the diagram groups on pages 14--15. Targeted comparison with the canonical French original adjudicated terminology but did not advance the French sequential cursor.
- Recorded source-alignment actions 040--046. The substantive repairs rebuild the paired Frobenius/Verschiebung diagrams with source-faithful label placement, the full nine-arrow topology of (4.5), and all structural/cohomological/trace diagrams in Lemma 4.6. The evident prose/name slips and the translation of *modérément ramifié* were also resolved and disclosed.
- Personally compared compiled native diagrams against the authority at 2,400--5,000 dpi. Arrow direction, attachments, labels, primes, subscripts, superscripts, equalities, and trace labels pass; no mathematical or visual judgment was delegated.
- Three-pass builds converge with zero required diagnostics: English 18 pages / 159,474 B / SHA-256 `681053076681ED9D857FD941C5DBD59C91D7A7431D5C89B9886708DD8CD5AC5D`; French 18 pages / 161,029 B / SHA-256 `6A08FD272E470F7787FF76D5D1527599A4FC360BF9106CC77BF847E63E4E4C5C`; bilingual 36 pages / 335,060 B / SHA-256 `0ED25D297FFCD3EBD067B123BCA655F7B43E4654EE4433F2BE0CC53609B2AB14`.
- English/French affected pages and the bilingual French-to-English seam passed personal rendered inspection. Durable receipt: `qa/ENGLISH_PAGES12_15_SOURCE_BUILD_RENDER_PASS_20260802.md`.
- English sequential cursor advances to IAS page 16/20. French-original sequential cursor remains physical page 2/35 / printed p. 139.

## 2026-08-02 — English pages 16--20 / EOF closed

- Completed direct sequential replay of the IAS English authority through page 20 / EOF, including references and initials, at 1,200 dpi with 5,000-dpi escalation for formulas and diagrams.
- Recorded source-alignment actions 047--055. The paired page-16 correspondences had lost half their descending relations and converted equality relations into arrows; the page-17 `VF` array had collapsed five upper objects to three and omitted two Frobenius twists and both diagonal structure maps. Both groups were rebuilt natively and personally source/output-checked at 5,000 dpi.
- Reconfirmed the disclosed page-18 weight and spectral-sequence corrections in sequential context; restored printed quotation emphasis and regularized only evident nonmathematical slips.
- A final 1,100-dpi whole-page pass caught a proof-end square touching the following source note. Added a layout-only paragraph break in both editions, rebuilt in fresh directories, and personally rechecked English pages 15--18, French pages 14--18, and the bilingual seam pages 18--19.
- Final provisional builds: English 18 pages / 162,574 B / SHA-256 `5AFF9E2DF65511BDE75F8E152845726637FF3F1D3089F36847271305970A78F7`; French 18 pages / 164,020 B / SHA-256 `B7EAFFEFCAAE2CB6DCCC7F258C1E6BEB9A3DD4BF04A79C96DC66D23880975B35`; bilingual 36 pages / 341,221 B / SHA-256 `D8D8157E66C693E012EB59A49C4BEFBF7D5071B68913B1F1924A30A495D49C01`. Three-pass diagnostics are zero.
- Durable receipt: `qa/ENGLISH_PAGES16_20_SOURCE_BUILD_RENDER_PASS_20260802.md`. English sequential cursor is EOF. French-original sequential cursor remains physical page 2/35 / printed p. 139, and becomes the active production cursor.

## 2026-08-02 — French printed pages 139--143 closed

- Completed direct sequential replay of canonical French authority physical pp. 2--6 / printed pp. 139--143 at 1,200 dpi. No OCR was generated; the PDF text layer was used only for location.
- Recorded actions 056--060. Replaced inherited back-translation drift with the canonical French wording, restored `A^f`, `A_f^S`, the underlined constant sheaf, *isomorphisme permis*, and *espace principal homogène*, and aligned the Kuga--Shimura and De Rham wording exactly.
- Corrected and visibly disclosed the two source slips on printed p. 142: permitted isomorphisms induce `1`, not `-1`, and the `Hom^+` maps respect the displayed orientations. The plus sign, orientation conventions, Poincaré half-plane, and subsequent construction jointly force both readings.
- Built the French, English, and bilingual readers serially in fresh directories for three passes. Current PDFs are respectively 18p SHA `E8392DC54DCABBA5351CF9C74B4A5B59F287F2251E4AE8C592F62FEBAC3D3131`, 18p SHA `1DDC87122988CEDC1FA30616B959984ED4656F65703C769FAD7B2E200D5227D2`, and 36p SHA `2FC51C4B92A84D88273507342CAA6A721A202664F7D35D5CB8E73AEFEC74617D`.
- Personally inspected French output pages 1--3 at 1,100 dpi. Title, formulas, notes, corrected orientation passage, Proposition 2.2, De Rham passage, matrices, and seams are legible and unclipped.
- Durable receipt: `qa/FRENCH_PRINTED139_143_SOURCE_BUILD_RENDER_PASS_20260802.md`. French sequential cursor advances to physical p. 7/35 / printed p. 144.

## 2026-08-02 — retroactive bilingual-layout specification correction

- Floris clarified that a bilingual deliverable means a genuinely parallel, side-by-side French--English reader. The prior `D006_LAD_Bilingual.tex` concatenated the complete French PDF and complete English PDF sequentially. Its content bytes were valid as two monolingual editions, but its layout claim was wrong; all earlier sequential-bilingual PDF identities remain adverse/provisional history and cannot satisfy the final bilingual gate.
- Replaced the composition master with a reproducible A3-landscape parallel layout: French page `n` is placed on the left and English page `n` on the right. The standalone French and English TeX files remain the content authorities, while the third TeX file is explicitly the synchronized composition layer.
- This was recognized as a corpus-wide specification defect, not a D006-only cosmetic issue. D001--D005 were inspected immediately and all five inherited bilingual masters were also found to concatenate the languages sequentially. Their closed monolingual sources remain preserved; no-overwrite parallel-layout successors and item-level adverse-history log entries are required before those items can be called bilingual-complete.
- Page-ordinal pairing is only accepted after personal rendered comparison confirms that corresponding content remains aligned. If language-specific reflow causes a pairing drift, the correction must be an explicit synchronized break/blank-page decision recorded in that item's logbook; silently pairing mismatched pages is prohibited.

## 2026-08-02 — dual-DOI provenance release control adopted

- Adopted the global logbook/provenance requirement at workspace-relative `03_projects/language_management/english_germanic/00_lane_control/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md`, 2,296 B, SHA-256 `BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679`.
- Wrote the Deligne-lane adoption record `Transcription\00_lane_control\DELIGNE_DUAL_DOI_PROVENANCE_ADOPTION_20260802.md`. Every final item handoff must identify the privacy-clean logbook, decision ledger, append-only reversal history, continuation record, and governing controls by relative path, bytes, and SHA-256.
- The same frozen provenance set must be deposited and read back in both the methodology DOI (`10.5281/zenodo.21124403`) and replication DOI (`10.5281/zenodo.20461174`); presence in an item source bundle alone is insufficient.
- The replacement archive task acknowledged the rule under decision `EG-ARCHIVE-DUAL-DOI-LOGBOOK-CUSTODY-CONTROL-20260802-0001`. No mutable D006 or Deligne work was uploaded.

## 2026-08-02 — French printed pages 144--148 closed; stale cursor corrected

- The working TeX and action ledger already contained completed direct source replay through canonical French physical page 11 / printed page 148, but `STATUS.md` still named printed page 144. This was a control-layer lag, not missing source work. I fail-closed the stale cursor, bound the completed actions and evidence, and advanced the exact next cursor only after replaying the affected output.
- Actions 061--066 record the complete printed pp. 144--148 decisions. They restore Deligne's French syntax, constant-sheaf markings, compactification/domain notation, *formes automorphes paraboliques*, De Rham and cohomology terminology, Néron-model wording, period `l.c.c.` terminology, and printed tensor notation.
- The matrix on printed p. 144 is printed as `(a c; b d)^{-1}` in both the French original and English retype, but the same-line fractional-linear formula and following determinant computation require `(a b; c d)^{-1}`. The corrected reading is retained with an expanded visible note naming both witnesses; it is not silently normalized.
- The two disk inequalities on printed p. 145 omit modulus bars around the complex coordinate in the English retype. The geometric description of a punctured disk requires `|q|`; the repaired inequalities and rationale remain visibly disclosed.
- Direct authority evidence comprises physical pp. 7--11 rendered at 1,200 dpi. Formula and notation readings were enlarged as necessary during the source pass; no OCR output was treated as authority and no new OCR was generated.
- Rebuilt French, English, and genuine side-by-side A3 bilingual outputs all converge in three passes with zero required diagnostics. The exact reader hashes are bound in the new bounded receipt.
- I rendered French output pages 3--6 separately at 1,100 dpi and inspected them personally. The orientation note, action matrix, compactification bars, Section 2 seam, Shimura diagram, Néron notation, constant sheaves, Section 3 seam, and l.c.c./adelic formulas are legible and unclipped. No mathematical or visual judgment was delegated.
- Exact next French cursor: canonical authority physical page 12 / printed page 149. No later sequential page is claimed by this checkpoint.

## 2026-08-02 — French printed pages 149--153 closed

- Completed direct sequential replay of canonical French authority physical pp. 12--16 / printed pp. 149--153 at 1,800 dpi. The higher-detail pass was used for the densely set definitions, level-transition formulas, represented functors, and local-system notation. No OCR was generated and no OCR output was treated as authority.
- Recorded actions 067--072. Canonical authorial phrasing and notation were restored throughout §§3.2--3.8, including the exact transition-map syntax, *champ déduit*, *pleinement fidèle*, *leur sorite*, and the printed local-system terminology.
- Retracted the earlier false attribution of “faithfully flat” to the French original. The French says *pleinement fidèle*; the bad reading occurs only in the inherited English retype. Both visible notes now state this exact provenance.
- Four material inherited errors were repaired globally in both editions and visibly disclosed: `\cO_X` to `\cO_S`, `(m/n)\alpha_m` to `(n/m)\alpha_m`, `T_\infty(E'_\infty)` to `T_\infty(E_\infty)`, and the second represented tuple's primed universal curve to the same unprimed `E_\infty` used in the first tuple. These changes are compelled respectively by the functor's base, restriction of level for `n\mid m`, and the French original's use of one universal curve.
- Preserved the clearly printed but unusual word *sorite* rather than silently modernizing it. Rendered the name Šafarevič with TeX accents after the first literal-Unicode build exposed a font-glyph failure; the failed build remains adverse history and the successor has no missing glyph.
- Built current French, English, and genuine side-by-side outputs with zero required diagnostics. The exact identities and adverse-build history are bound in `qa/FRENCH_PRINTED149_153_SOURCE_BUILD_RENDER_PASS_20260802.md`.
- Personally inspected French output pages 6--8 at 1,100 dpi. Also inspected parallel spreads 6--8 at 600 dpi strictly for output layout and seam placement; source decisions remain controlled by the 1,800-dpi authority evidence. Both languages are legible, unclipped, correctly ordered, and remain on the same page-ordinal band.
- Exact next French cursor: canonical authority physical page 17 / printed page 154. No later sequential page is claimed by this checkpoint.

## 2026-08-02 — French printed pages 154--159 closed

- Completed direct sequential replay of canonical French authority physical pp. 17--22 / printed pp. 154--159 at 1,800 dpi. Direct English comparison covered IAS pp. 8--12. No OCR was generated and no OCR output was treated as authority.
- Recorded actions 073--075. Restored Deligne's printed wording throughout Definition 3.9, §§3.12--3.20, and the opening of §4, including the exact Hodge, automorphic-form, trace-morphism, scalar-product, and functor terminology. The native diagrams (3.14), (3.16), and (3.17) remained source-faithful and were retained.
- Corrected two material English-retype defects globally and visibly: the first Definition 3.9 formula now carries the fixed level index `n`, and the retype's assertion that `W` “doesn't depend” on the universal elliptic curve is restored to the French source's `ne dépend que de` / “depends only on.” These are compelled by the canonical French and the definition's immediately fixed level, not stylistic preferences.
- Normalized the printed `Peterson`/`Pertersson` variants to `Petersson` with visible disclosure. Rejected a suspected additional symbol on `_nW` after an enlarged direct check showed that it belonged to the adjacent `K_n`; no speculative change was made.
- Preserved the first English p. 159 build as adverse history because an English note called the French-only `frquote` helper and failed with an undefined control sequence. The successor uses ordinary English quotation marks without changing content.
- Personal 1,100-dpi output review found one orphaned colon after the `I_p` functor sentence. Added a nonbreaking space as a layout-only repair, rebuilt the French and genuine side-by-side readers in fresh directories, and personally rechecked corrected French page 11 plus parallel spreads 8--12. The content is legible, unclipped, correctly ordered, and page-paired.
- Current PDFs: French 18p / SHA-256 `E7D4BC803B2582ECD6B62FF16E9E7522B803BA50E40D64AAA5B8E6FC22805E2D`; English 18p / SHA-256 `20E3F608127E03065E361F458B082B288E3EE963345476BABC3D1075D1CDF544`; side-by-side bilingual 18 A3 spreads / SHA-256 `CE5F0A75C7B0B23BF634C655E724654B1C298E21E5DE085EB96C9E8F54EAD42B`. All final logs have zero required diagnostics.
- Durable receipt: `qa/FRENCH_PRINTED154_159_SOURCE_BUILD_RENDER_PASS_20260802.md`. Exact next French cursor: canonical authority physical page 23 / printed page 160.

## 2026-08-02 — French printed pages 160--164 closed; Lemma 4.6 topology repaired globally

- Completed direct sequential replay of canonical French authority physical pp. 23--27 / printed pp. 160--164 at 1,800 dpi. No OCR was generated and no OCR output was treated as authority.
- Recorded actions 076--078. Restored Deligne's wording from Theorem 4.1 through Lemma 4.6, including the exact curve-compactification, reduction, tame-ramification, normalized-cover, l.c.c.-sheaf, tensor, Hecke, and lemma-hypothesis terminology.
- Corrected the French original's printed Corollary `3.2` to `4.2` with a visible source note. Its placement after Theorem 4.1 inside §4 and the independent IAS English label jointly force the correction.
- A direct p. 164 authority check found a material defect in the earlier native repair: it had represented the Lemma 4.6 structural diagram as two disconnected copies of `Z_1 -> Z_2`. The source has one shared object pair carrying all four maps to `X` and `Y`. Rebuilt the diagram globally in both French and English, replaced the prior source notes with explicit supersession notes, and personally compared both compiled diagrams against the source at 1,800 dpi. Arrow direction, attachments, labels, crossings, and shared object identity pass.
- Preserved the first French and bilingual p. 164 builds as adverse history: literal guillemets and a literal section glyph in the new numbering note rendered incorrectly under the active encoding. Replaced them with `frquote` and `\S4`, rebuilt in fresh no-overwrite directories, and personally rechecked the corrected note.
- Final builds converge with zero required diagnostics: French 18p / SHA-256 `02C11AD85D9B07313D82564D7531CF22A6F71951E6830CD8E748A30D20DC6C04`; English 18p / SHA-256 `CC93C24BBBB492A247E42F1B6526F5DF6E99DBF21FB8B4E572108064A2F707DA`; genuine side-by-side bilingual 18 A3 spreads / SHA-256 `F1C627BF868E98CC80A177BF2C2DE89D886E3110B4F3099B61093CC7A62259E4`.
- Personal source/output review used 1,800-dpi evidence for the mathematical diagram and 1,100-dpi evidence for the corrected French note. Parallel spreads 12--14 passed a separate 600-dpi layout-only inspection. Normal language-specific reflow remains visible and is logged; no false line-level alignment is claimed.
- Durable receipt: `qa/FRENCH_PRINTED160_164_SOURCE_BUILD_RENDER_PASS_20260802.md`. Exact next French cursor: canonical authority physical page 28 / printed page 165.

## 2026-08-02 — French printed pages 165--169 closed

- Completed direct sequential replay of canonical French authority physical pp. 28--32 / printed pp. 165--169 at 1,800 dpi. No OCR was generated and no OCR output was treated as authority.
- Recorded action 079. Restored Deligne's exact French from paragraph 4.7 through the opening proof of Lemma 5.4, including the l.c.c.-sheaf, trace/base-change, Frobenius, Weil-conjecture, representability, spectral-sequence, iterated-fibre-product, and non-smoothness terminology.
- Directly rechecked the already repaired p. 165 correspondence diagrams and p. 166 five-object `VF` diagram at 1,800 dpi. Their object identities, equalities, directions, diagonals, labels, and attachment points agree with the source; no new diagram mutation was justified.
- Reconfirmed in sequential context that the already disclosed Theorem 5.1/Lemmas 5.2--5.3 exponents and the printed “non-null” differentials are genuine source slips. Their visible mathematical corrections remain unchanged. No additional mathematical defect was found in this band.
- Built the French and side-by-side readers in fresh directories for three passes with zero required diagnostics. Current PDFs: French 18p / SHA-256 `8394A2451FA2D41D2C657F495C3DEE9022588116CBBDF56AA8A1AB19FE6120A9`; unchanged English 18p / SHA-256 `CC93C24BBBB492A247E42F1B6526F5DF6E99DBF21FB8B4E572108064A2F707DA`; genuine side-by-side bilingual 18 A3 spreads / SHA-256 `69810E5A4140EFA88BC84122010EC0D3096C5CDED01A4DA2E0936DC34024E49E`.
- Personally inspected French output pages 14--17 at 1,100 dpi and parallel spreads 15--17 at 600 dpi for layout only. No clipping, blank pages, diagram regression, or page-order defect is present. No false line-level synchronization is claimed.
- Durable receipt: `qa/FRENCH_PRINTED165_169_SOURCE_BUILD_RENDER_PASS_20260802.md`. Exact next French cursor: canonical authority physical page 33 / printed page 170.

## 2026-08-02 — French printed pages 170--172 / EOF closed; terminal bilingual synchronization repaired

- Completed direct sequential replay of canonical French authority physical pp. 33--35 / printed pp. 170--172 at 1,800 dpi, including the terminal proof, bibliography, and sigla. No OCR was generated and no OCR output was treated as authority.
- Recorded actions 080--081. Restored Deligne's exact proof transitions and terminal technical wording, retained the printed Lemma 5.5 monomial without silent normalization, and corrected bibliographic title/publication-status drift in both editions.
- The first EOF French reader occupied 19 pages while English occupied 18. The then-current 18-spread composition silently omitted the French sigla page. This is a real composition-layer failure; `build/bilingual_parallel_eof_r1` is preserved as rejected adverse history.
- A first layout-only remedy using `\enlargethispage` compressed the French sigla onto page 18, but personal 1,100-dpi output inspection found the text crossing the footer/page-number region. That attempt is also preserved and rejected; apparent page-count agreement is not accepted over visible clipping.
- The final repair removed the compression and inserted an explicit matched page break before the English initials. French bibliography and English references now end cleanly on page 18; French sigla and English initials occupy page 19. The A3 composition master pairs all 19 pages French-left / English-right, with no omission.
- Final three-pass builds have zero required diagnostics: French 19p SHA `80E69F2487F840C2B46A76D0FEF6D7E709363C5E7FD8A653A9DADAD0518B6267`; English 19p SHA `95A7962CDFD15136940763DE3490E4D96C0B8A0DE8A73BEE412F4189363085FC`; bilingual 19 A3 spreads SHA `F7CBC207ACFD540591D101CF7C9EDB330DC2EC1A2BD9313AE158F17862B1FDEC`.
- Personally inspected final monolingual pages 18--19 at 1,100 dpi and final parallel spreads 18--19 at 600 dpi strictly for composition/layout. Bibliographies, sigla/initials, margins, footers, page order, and language pairing pass. Source decisions remain controlled by the direct 1,800-dpi authority evidence.
- Durable bounded receipt: `qa/FRENCH_PRINTED170_172_EOF_SOURCE_BUILD_RENDER_PASS_20260802.md`. Both English and canonical-French sequential cursors are now EOF. Exact manifests and final whole-item local validation remain the next gate.

## 2026-08-02 — final D006 whole-item local reader validation closed

- Replayed the complete 81-row source-alignment ledger: 81 unique stable action IDs, eight rectangular columns, no empty IDs, and zero spreadsheet-formula-risk cells. All 20 English-authority pages and all 35 canonical-French pages have direct sequential source decisions recorded through EOF.
- Audited the three final PDFs mechanically. French and English are each 19 nonblank letter pages; the side-by-side edition is 19 nonblank A3-landscape spreads. All fonts are embedded and non-Type-3 (French 23 rows, English 22, bilingual 45); all three PDFs have zero raster image rows. The side-by-side composition uses imported vector pages, not rasterized page images.
- Completed the final composition evidence without redundant visual judgment. Spreads 1--5 were rendered from the final PDF at 600 dpi and personally inspected. Final spreads 6--16 were rendered at 600 dpi and are pixel-hash-identical to their previously inspected bounded checkpoint renders. Final spread 17 and both monolingual page-17 outputs were personally inspected after the terminal proof changes; spreads/pages 18--19 had already passed the terminal synchronization check. Thus all 19 final spreads have exact, personally reviewed layout evidence.
- Scanned the editable/record surface for private home paths. The sole internal absolute-path occurrence in this logbook was replaced by a workspace-relative control path; the French/English/bilingual TeX, action ledger, status, and logbook now have zero private-home hits. `controls/INPUT_IDENTITIES.csv` intentionally remains an internal provenance ledger containing authority locations and is not itself a privacy-clean public artifact.
- D006 now passes the local source-aligned French, English, and true side-by-side bilingual EOF gate. This does not claim public-package/reference-v2 closure, DOI deposition, archive custody, D007 completion, letters, or whole-corpus completion.

## 2026-08-02 — semantic scaffold and control-file recovery

- Added `controls/SEMANTIC_UNITS.csv`, containing 56 stable `deligne.d006.*` unit identifiers for the delivered title, numbered sections, definitions, propositions, theorems, corollaries, lemmas, remarks, examples, displayed formulas, and diagrams. The IDs are language-neutral attachment points for the canonical French and English sources and for later multilingual/interlanguage or Stacks-style work; they do not claim formalization.
- Added `controls/SEMANTIC_DEPENDENCIES.csv`, containing 19 explicit relations supported by delivered source structure or cross-reference text. No dependency was inferred merely because it seemed mathematically plausible. Validation found 56/56 unique units, zero missing parents, 19 dependency rows, zero missing endpoints, and zero spreadsheet-formula-risk cells.
- Bound the corpus-wide semantic/interlanguage policy `Transcription/00_lane_control/DELIGNE_BILINGUAL_SEMANTIC_INDEX_AND_INTERLANGUAGE_SCAFFOLD_20260802.md`, 4,544 bytes, SHA-256 `C348283EBC3ED045AFBE2107D2C8B4A068E04C6D3E9639244E1F074423EC2009`. Current priority remains source-aligned French and English; later languages attach to the stable units rather than forking the mathematics.
- During this text-only update, `LOGBOOK.md` and `STATUS.md` were found entirely NUL-filled from the preceding PC-instability interval. No TeX, PDF, diagram, or semantic CSV was affected. Their complete immutable task file-change histories were replayed with zero errors, exact known pre-corruption byte counts and hashes were recovered, and the canonical paths were restored byte-for-byte only after no-overwrite recovery copies matched those identities.
- Durable adverse/recovery record: `controls/LOGBOOK_STATUS_NUL_CORRUPTION_AND_RECOVERY_20260802.md`. Exact recovery copies remain at `LOGBOOK_RECOVERED_FROM_THREAD_HISTORY_20260802.md` and `STATUS_RECOVERED_FROM_THREAD_HISTORY_20260802.md`; they are historical evidence and are not alternate live status records.
- No rendering, image loading, OCR, compilation, agent work, or source/PDF mutation was performed for this scaffold and recovery step.
