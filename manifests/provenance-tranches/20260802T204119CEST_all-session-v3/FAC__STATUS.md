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

- Continuous English coverage: `FAC-EN-U0001`--`FAC-EN-U0060`, French `fac_body.tex` lines 1--2267, printed pages 197--256, through Chapter III, §3, no. 62.
- Exact next cursor: French `fac_body.tex` line 2270 / printed page 256 / no. 63, `Propriétés générales des H^q(M)`.
- English master: `english_source_first_workpass/source/Serre_FAC_English_source_aligned_workpass.tex`, 5,172 B, SHA-256 `580F34C508E518CF0C74A68A2A60E342BE9146CA16FFF113E6932D10297280B5`.
- English checkpoint: `build_checkpoint_III_3_62_r1`, 58 A4 pages / 706,035 B / SHA-256 `C7540A182880F5259D0F249744FE9B8F9BD16EBC55F7230C203F6A709771981D`; three-pass convergence, affected pages 56--58 personal visual/formula PASS.
- Diplomatic French T0035 checkpoint: 63 pages / 633,725 B / SHA-256 `0CC2BF32C38AA8D7C908EF58AE980079D14E7EE501CB4656C42FC11E43534FB4`.
- Corrected French C0036/T0035 checkpoint: 63 pages / 634,029 B / SHA-256 `1C4EC94C2B45B96FFADF88E5F98E68FC1E68C713F817A265775D02C4BDD7FB4C`.
- Decision accounting: 36 printed-source corrections, 35 transcription-repair groups, 117 append-only self-correction events (135 affected textual/ledger/build/normalization occurrences), 2,607 occurrence-level English normalization rows, 163 semantic entities, and 288 semantic relations. Known post-admission mathematical/translation reversals: 1 (`FAC-SELF-0065`, now repaired).
- This snapshot controls over the chronological checkpoint history below. FAC remains active production, not complete or publication-ready.

## Chronological English coverage history

- Unit `FAC-EN-U0060`: French `fac_body.tex` lines 2195--2267; authority physical pages 59--61 / printed pages 254--256; no. 62 complete.
- `FAC-FR-T0035` repairs four inherited epsilon commands to the four authority-visible membership signs in the definitions of $\alpha^k$, $(P_0,\ldots,P_h)M$, and $N:P$. The repair is common to both working French layers; the immutable inherited tree remains untouched. No printed-source correction was found in no. 62, so the corrected layer retains C0036 as its latest authorial correction.
- English `build_checkpoint_III_3_62_r1`: 58 pages / 706,035 B / SHA `C7540A182880F5259D0F249744FE9B8F9BD16EBC55F7230C203F6A709771981D`; log SHA `6760CB5F41CE54E2FEFBE44A645AC3E13B5AB48C59716316E00F9C66D9B6BC63`; byte-identical pass-2/pass-3 console SHA `5F36B0A307127614E43518C915E9EE5FEF8B8A244DB7A0087A94EEBB554C0110`; hard/undefined/overfull 0 and two harmless underfull notices. Pages 56--58 personal PASS.
- Diplomatic T0035: 63 pages / SHA `0CC2BF32C38AA8D7C908EF58AE980079D14E7EE501CB4656C42FC11E43534FB4`; corrected C0036/T0035: 63 pages / SHA `1C4EC94C2B45B96FFADF88E5F98E68FC1E68C713F817A265775D02C4BDD7FB4C`. Each converges in three passes with hard0 and the inherited overfull1/underfull3. Pages 44--46 were personally reviewed from bounded 300-dpi output after the direct 600-dpi authority review.
- Seventeen new semantic entities and thirty-four relations expose the two submodule definitions, both propositions and their items, the top-cohomology quotient, beta reparametrization, and all three corollaries. Every new same-unit prose reference resolves to its exact target; no cross-unit approximation was invented.
- `FAC-SELF-0110`--`0117` preserve two corrected validation hashes, a rejected false validation query, two prebuild source/comment corrections, three zero-change Windows-tool/parser failures, and three immediately repaired documentation delimiters. Their successor checks are the only admitted evidence; no hidden mathematical or French-layer mutation resulted.

- Unit `FAC-EN-U0059`: French `fac_body.tex` lines 2133--2193; authority physical pages 58--59 / printed pages 253--254; Chapter III §3 opening and no. 61 complete.
- `FAC-FR-T0034` repairs three inherited epsilon commands to the authority-visible membership sign. A direct 5000-dpi same-formula comparison proves that print itself has $m\langle i_0\cdots i_i\rangle$ while the summation bound and terminal differential are indexed by $i_q$; `FAC-FR-C0036` preserves printed $i_i$ diplomatically and restores $i_q$ in corrected French and English.
- English `build_checkpoint_III_3_61_r1`: 56 pages / 694,872 B / SHA `4ED657560FD52B343CF06828D6A635B9CC019495330A5F371B7C38BF3329CDA5`; log SHA `5F7209AF2D3997D50F7F30D74F030B929E6DF7D124F3F505A8D58411C2E361FF`; byte-identical pass-2/pass-3 console SHA `4E02575DE3681B23FB6F6A29FFED90378DD1CCD16B51EADD6C756E75702942C2`; hard/undefined/overfull 0 and two harmless underfull notices. Pages 55--56 personal PASS.
- Fifteen new semantic entities and thirty relations expose the section, alternating cochains, differential, complex, differential-form interpretation, transition maps, direct limits, functorial maps, long exact sequence, and no. 69 forecast. `FAC-SELF-0106` restores source paragraph/display structure before the first build; `0107` rejects a false log diagnostic; `0108` generalizes the direct-limit-symbol rationale and append-only `0109` corrects its first undercount from two to six affected rows.

- Unit `FAC-EN-U0058`: French `fac_body.tex` lines 2079--2130; authority physical pages 57--58 / printed pages 252--253; no. 60 complete.
- The direct 600-dpi page review and bounded 1800-dpi diagram crop establish that the printed top row uses italic `L^1,L^0`, while the preceding exact sequence, lower row, and vertical beta maps require the sheaves `\mathcal L^1,\mathcal L^0`. `FAC-FR-C0035` therefore preserves print in diplomatic French and repairs only corrected French and English. No inherited-transcription repair was needed.
- English `build_checkpoint_III_2_60_r4`: 55 pages / 684,566 B / SHA `30660EC406B057DD2FE3DE55723505DC09962BCD5663B82E35E4198E59966127`; log SHA `403FB7EC25E604F44C75534C612034DED9006F055A2C2E13DC2820C8B0ADFA56`; byte-identical pass-2/pass-3 console SHA `50C2B7B9081B84298A6A795A1CB04F73F17F900947E30184F7A48DA6D2547D6F`; hard/undefined/overfull 0 and two harmless underfull notices. Pages 54--55 personal PASS.
- Eight new semantic entities and twenty-two relations expose Proposition 9, Theorem 2, four proof sequences/maps, and the commutative diagram. `FAC-SELF-0101` records and repairs the r1 proposition-layout drift; `FAC-SELF-0102`--`0104` disclose three zero-change command/query failures; `FAC-SELF-0105` restores twenty-two previously uncounted TeX-delimited `graded $S$-module` occurrences under N0071 without changing the translated body.

- Unit `FAC-EN-U0057`: French `fac_body.tex` lines 2043--2076; authority physical pages 56--57 / printed pages 251--252; no. 59 complete.
- Direct bounded 600-dpi review found no printed-source defect or inherited French-transcription deviation. The diplomatic T0033 and corrected C0034/T0033 source layers and PDFs are therefore unchanged. The English preserves the graded module of twisted global sections, the global and local $S$-actions, the canonical maps $\alpha$ and $\beta$, their stalk formula, both identity composites, and the exact forward claim to no. 65.
- English `build_checkpoint_III_2_59_r1`: 54 pages / 678,659 B / SHA `B8AAAF1AC1CCF8CC2FE35CEBD7BE01997354E80BDEBCE35A58DA09F3BE02EA25`; log SHA `51C2074A9ED9692C936F6D2D17ADC982099E6E8A58127BC44BD6215AAC0DD346`; byte-identical pass-2/pass-3 console SHA `FE90EDFDB23FF70984AB6FA26D5CDC3CB6A8446C840B5A4A853C5D17C0B034ED`; hard/undefined/overfull 0 and two harmless underfull notices. Pages 53--54 personal PASS.
- Thirteen new semantic entities and twenty-nine relations expose the module action, $\alpha$, $\beta$, both composites, and the forward theorem dependency. The no. 65 edge remains explicitly `pending_entity_backfill`; no nonexistent local destination was invented. `FAC-SELF-0095`--`0100` preserve three zero-change read-only path/control/policy lookup corrections, one two-delimiter Markdown repair, one rejected CSV-count query, and correction of the stale internal privacy count to five files / 415 occurrences.

- Unit `FAC-EN-U0056`: French `fac_body.tex` lines 1999--2040; authority physical pages 55--56 / printed pages 250--251; no. 58 complete.
- `FAC-FR-T0032` repairs eighteen inherited epsilon commands to the authority-visible membership sign. `FAC-FR-T0033` removes a nonauthorial JSTOR footer while preserving the 3,447-line source geometry. `FAC-FR-C0034` preserves printed `vide où réduite à \{0\}` diplomatically while corrected French and English use the logically required `vide ou réduite` / “empty or reduced.”
- The English preserves exactness of $M\mapsto\mathcal A(M)$, compatibility with shifts, the $\eta_{i,x}$ and transition formulas, $\mathcal A(S(n))\simeq\mathcal O(n)$, the coherence/class-$\mathcal C$ criterion, Hilbert's Nullstellensatz argument, and the class-relative morphism criterion. Fourteen new semantic entities and twenty-five relations expose the proof formulas as well as the proposition targets.
- English `build_checkpoint_III_2_58_r2`: 53 pages / 671,525 B / SHA `6CBFA00A9EFA8119B4E276DB61B8365EBDF626A380C4986D100669DE5C337C7B`; log SHA `A639097C9A9F753324FCB384034C03A246B63BE7659A6718C9F60241F8DBA192`; byte-identical pass-2/pass-3 console SHA `4C8A4159289F44D4FD2735B2D3FBD4CB2E08B74A12F52D2388AEC48833C68CB2`; hard/undefined/overfull 0 and two harmless underfull notices. Pages 52--53 personal PASS.
- Diplomatic T0033 and corrected C0034/T0033 both converge in three passes with only the inherited one-overfull/three-underfull notices. French page 41 is pixel-identical between layers; page 42 visibly preserves `où` only in the diplomatic layer and shows `ou` in the corrected layer. `FAC-SELF-0089`--`0094` preserve the live-path lookup, build-directory, normalization-coverage, provisional-ledger-schema, privacy-query, and final-replay command corrections before admission.

- Unit `FAC-EN-U0055`: French `fac_body.tex` lines 1955--1996; authority physical pages 54--55 / printed pages 249--250; no. 57 complete.
- `FAC-FR-T0030` repairs six inherited epsilon commands to the authority-visible membership sign. `FAC-FR-T0031` removes a nonauthorial JSTOR download footer while preserving the source line count and later locators. `FAC-FR-C0033` preserves the printed `U=X` and `U=x` singleton slips diplomatically while corrected French and English write the mathematically required `U=\{x\}`.
- The English retains the fraction-module equivalence relation, both module operations, canonical transition maps, the associated-sheaf construction, stalk direct limit, additivity/composition identities, and Serre's warning that $S_U$ is only the degree-zero homogeneous component. N0076--N0078 bind “multiplicatively closed,” “additive covariant functor,” and modern direct-limit notation without altering the indexing system.
- English `build_checkpoint_III_2_57_r3`: 52 pages / 662,306 B / SHA `445E9A369AF49261231567C355BC9C45B0B70F54699AA53ABFE8B298226B862E`; log SHA `5F7627E2A7687C6F7B883B431EB29AAB912C54FC316331571CA4966BF01BA9C7`; byte-identical pass-2/pass-3 console SHA `62FA4BDC001B48640084F443BC5CCA13F12467A32110B118DA49E31B78983DC4`; hard/undefined/overfull 0 and one inherited harmless underfull notice. Pages 51--52 personal PASS; the §4 link is an internal GoTo to an existing destination.
- Diplomatic T0031 and corrected C0033/T0031 both converge in three passes with only the inherited one-overfull/three-underfull notices. French pages 40--41 and the direct authority pages were personally inspected. `FAC-SELF-0085`--`0088` preserve the path lookup, locator-preservation, missing-anchor, and normalization-binding corrections rather than rewriting the work history.

- Unit `FAC-EN-U0054`: French `fac_body.tex` lines 1927--1952; authority physical pages 53--54 / printed pages 248--249; no. 56 complete.
- `FAC-FR-T0029` repairs five inherited epsilon commands to the authority-visible membership sign in the statements `A,C,B\in\mathcal C`, `\operatorname{Ker}(\varphi)\in\mathcal C`, and `\operatorname{Coker}(\varphi)\in\mathcal C`. Both French layers receive the repair; this is not a correction to the printed article.
- No. 56 preserves Serre's grading, homogeneous morphism degree, shift convention $M(n)_p=M_{n+p}$, class $\mathcal C$, class-relative morphism terminology, condition (TF), and free graded modules. Nine entities and thirteen relations make each definition separately addressable.
- English `build_checkpoint_III_2_56_r2`: 51 pages / 656,535 B / SHA `F5C4E82DDB95AFA79D7E72D92890B18C3E50E542854D8B54965323CE70DA619D`; log SHA `DCAEB767CBC2E468F17951C8B1A53FA1622EC3576B6BA4973C4870615BC0FD17`; byte-identical pass-2/pass-3 console SHA `A853309E6514C03F8C8A8456BE7069E14F6508B890430115F65DB710FC8F1DD8`; hard/undefined/overfull 0 and one inherited harmless underfull notice. Pages 50--51 personal PASS.
- Diplomatic T0029 and corrected C0032/T0029 both converge in three passes. Their affected reader page 40 renders are pixel-identical SHA `BE1210C377C42D888A27F44992F557BA2C036D3CF489FED7109003542DE17F29` and personal PASS. `FAC-SELF-0081`--`0083` preserve three normalization-metadata/coverage repairs made before admission.

- Unit `FAC-EN-U0053`: French `fac_body.tex` lines 1889--1924; authority physical pages 52--53 / printed pages 247--248; no. 55 complete.
- No. 55 preserves both extension lemmas, the global-generation theorem, every exponent and transition identity, and the quotient-sheaf corollary. Direct 600-dpi comparison found no printed-source defect or inherited French-transcription deviation, so the French layers remain unchanged at T0028 and C0032/T0028.
- Seven stable semantic entities and thirteen relations bind the numbered unit, both lemmas, Theorem 1, the two decisive compatibility formulas, and the corollary. Three certain same-unit prose references are clickable; references to nos. 42--45 remain explicit locator-backed relations pending their later local-entity backfill.
- English `build_checkpoint_III_2_55_r3`: 50 pages / 643,104 B / SHA `51D675C78B1FA9C3BA75B57823C69B0F85E65C1FBA0FC8257AC17C1B03FAF5ED`; log SHA `D32CC7AFB3A9AB047E056268417A85CBFB295C446D40C8649A356903E6AB8B5F`; byte-identical pass-2/pass-3 console SHA `DB383D6DBC96B5724FC80DFCC618974B21FCF7ADC222B9A80BE5EF88BBB1D0A4`; hard/undefined/overfull 0 and one inherited harmless underfull notice. Pages 49--50 personal PASS.
- `FAC-SELF-0072`--`0074` and `0076`--`0080` disclose eight zero-change validation/query-command or metadata-patch corrections; `FAC-SELF-0075` repairs two awkward English constructions before admission. Exact next cursor is line 1927 / printed p. 248 / no. 56.

- Unit `FAC-EN-U0052`: French `fac_body.tex` lines 1860--1886; authority physical pages 51--52 / printed pages 246--247; Chapter III, §2 opening and no. 54 complete.
- `FAC-FR-C0031` preserves printed `élement` diplomatically and restores standard `élément` only in corrected French. `FAC-FR-C0032` preserves the printed `f_j`/domain-`U_i` index conflict diplomatically while corrected French and English use the internally required `f_i`; the following definition `g_i=t_i^n f_i` confirms the repair.
- The operation is called “the operation F(n)” rather than silently renamed “twisting”; the transition maps, canonical identities, exact-sequence behavior, homogeneous-function description, rational fractions, and tensor-product identification are all retained. No new recurring normalization policy was needed.
- English pages 47--49 and corrected-French pages 38--39 pass personal review. `FAC-SELF-0069`--`0071` disclose three zero-change read-only query syntax failures; the builds and sources were not affected.

- Unit `FAC-EN-U0051`: French `fac_body.tex` lines 1830--1857; authority physical pages 50--51 / printed pages 245--246; no. 53 complete.
- No. 53 retains the finite coverings `B^F`, the arbitrary-refinement lemma, the simplex comparison, vanishing for every sheaf on an irreducible algebraic curve, and Serre's explicit statement that he does not know the higher-dimensional analogue. Existing N0052 supplies the standard phrase “arbitrarily fine.” No French-source or inherited-transcription discrepancy was found in this unit.
- Direct rereading of printed p. 245 exposed `FAC-SELF-0065`: the admitted no. 52 component had `C'^{,n}` instead of source `C^{\prime n}`. The comma was removed, the semantic formula entity advanced to r2, and `build_checkpoint_III_1_52_r1` is superseded by the no. 53 cumulative build. `FAC-SELF-0066`--`0068` record three zero-change lookup/summary/replay-query errors.
- The current build has no hard/undefined/overfull diagnostics and one inherited harmless underfull notice; pages 46--48 pass personal review.

- Units `FAC-EN-U0049`--`FAC-EN-U0050`: French `fac_body.tex` lines 1767--1828; authority physical pages 48--50 / printed pages 243--245; Chapter III, §1 opening and nos. 51--52 complete.
- `FAC-FR-T0028` repairs inherited `l'espacc projectif` to the clearly printed `l'espace projectif` in both French layers. `FAC-FR-C0030` preserves printed `coincide` diplomatically while corrected French restores `coïncide`; English is naturally grammatical.
- No. 51 establishes the scalar quotient, coordinate functions, standard affine cover, degree-zero invariant structure sheaf, algebraic-variety proposition, and definition of projective variety. No. 52 contains the covering comparison, both vanishing corollaries, support-dimension theorem, the two homogeneous-polynomial lemmas, Veronese map, and final alternating-cochain proof.
- `FAC-SELF-0061` corrects the globally too-narrow rationale of N0063 without changing any English occurrence. `FAC-SELF-0062` moves two newly added anchors before their paragraphs prior to build. `FAC-SELF-0063` and `FAC-SELF-0064` record and replace two zero-change validation-query/parser mistakes. The no. 52 reader has no active hard/undefined/overfull diagnostics.

- Unit `FAC-EN-U0048`: French `fac_body.tex` lines 1736--1764; authority physical pages 47--48 / printed pages 242--243; no. 50 complete.
- The source-defined projective-module criterion, projective-dimension display, local-freeness/vector-fiber-space corollary, class correspondence, and historical polynomial-ring question are all present. “Fiber space with vector-space fiber” is retained instead of silently modernizing the article to “vector bundle.”
- Direct 600-dpi authority comparison was fully legible and found no new printed-source defect or inherited French-transcription deviation. Both French layers therefore remain unchanged at T0027 / C0029-T0027.
- The first render exposed two source-listed corollary items flowing inline. `FAC-SELF-0057` records the explicit paragraph repair. `FAC-SELF-0058` records that a provisional r1 build directory was mistakenly reused; r1 is excluded, and the clean no-overwrite r3 checkpoint is controlling. `FAC-SELF-0059`--`0060` record two zero-change verification-wrapper/parser corrections.
- Stable targets now cover no. 50, Proposition 4, its projective-dimension display, the corollary and each item, the class correspondence, and the historical question.

- Unit `FAC-EN-U0047`: French `fac_body.tex` lines 1682--1734; authority physical pages 46--47 / printed pages 241--242; no. 49 complete.
- `FAC-FR-T0027` restores the authority-visible sheaf symbol in the final coherence clause, where inherited TeX had plain `F`. Both French layers now use the same calligraphic sheaf symbol as the surrounding paragraph; no printed-source correction was found.
- The English native diagram has the authority's exact 2-by-4 node layout, 10 ordinary arrows, and four downward alpha labels on the left of their shafts. English pages 43--44 and French pages 34--35 passed personal review; the two French affected-page pairs are pixel-identical.
- The semantic graph now identifies the Gamma construction, Theorem 1 and parts (a)/(b), alpha and beta maps, the proof diagram, and both remarks. Historical no. 45/no. 65/Chapter III targets remain explicitly pending entity backfill.

- Unit `FAC-EN-U0046`: French `fac_body.tex` lines 1635--1680; authority physical pages 45--46 / printed pages 240--241; §4 opening and no. 48 complete.
- `FAC-FR-T0026` repairs the two inherited `x/f \epsilon V/A` membership tokens to the authority-visible `x/f\in V/A` in both French layers. No printed-source correction was found in no. 48.
- English r2, diplomatic T0026, and corrected C0029/T0026 each passed three sequential pdfLaTeX passes. English pages 42--43 and French pages 33--34 passed personal visual/formula review; diplomatic and corrected French renders are pixel-identical on both affected pages.
- Semantic coverage now includes the section, numbered unit, coordinate-ring definition, associated-sheaf construction, three propositions, localization lemma, and localization tensor map. All 28 relation targets close except historical relations explicitly marked `pending_entity_backfill`.

- Unit `FAC-EN-U0045`: French `fac_body.tex` lines 1604--1633; authority physical pages 44--45 / printed pages 239--240; no. 47 complete.
- `FAC-FR-T0025` repairs three inherited `i \epsilon I` tokens to the authority-visible membership notation `i\in I` in Proposition 8 and Theorems 4--5. Both French layers are repaired identically; no printed-source correction is asserted.
- English, diplomatic French, and corrected French each passed converged three-pass builds. English pages 41--42 and French reader pages 32--33 passed personal review from valid sequential 200-dpi renderings after four zero-filled `pdftoppm` intermediates were rejected by signature inspection.
- The first broader semantic scaffold records 8 no. 47/section/formula entities and 14 hierarchy/dependency/proof relations. All admitted local targets resolve; historical no. 29/no. 42/no. 46 dependencies remain explicitly `pending_entity_backfill`, not falsely certified.

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
- No new OCR is generated. Direct authority rendering is bounded to the current pages: ordinary prose/formula checks use the lowest detail that resolves the print, while small or ambiguous indices, arrows, and diagram geometry escalate within the user-authorized 1100--9000-dpi range. No whole-volume high-resolution rendering is permitted.
- Controlling provenance rule: `00_lane_control/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md`, 2,296 B, SHA-256 `BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679`. Every immutable handoff must bind privacy-clean logbook identities, and archive maintenance must deposit them in both the methodology and replication DOI records. Mutable FAC logs remain local until a bounded/final freeze.
- Archive task `<REDACTED_TASK_ID>` acknowledged that rule under decision `EG-ARCHIVE-DUAL-DOI-LOGBOOK-CUSTODY-CONTROL-20260802-0001`, naming methodology DOI `10.5281/zenodo.21124403` and replication DOI `10.5281/zenodo.20461174`. It accepted and uploaded no FAC artifact; FAC remains mutable production.
- Semantic indexing is broader than clickable references. Shared control `00_lane_control/SGA_FAC_GAGA_SEMANTIC_INDEXING_AND_FORMALIZATION_SCAFFOLD_20260802.md`, 6,190 B, SHA-256 `F5E54638B569157DC355FFD3C3A283111BD26ABA1834C8F618A40B8BBC2F1601`, requires stable mathematical entities, source/translation spans, terminology, hypotheses, dependency and correction edges, diagrams/formulae, multilingual attachments, and explicitly qualified Stacks/Lean mappings. FAC captures these incrementally without stalling sequential translation; exhaustive closure belongs to bounded/cumulative gates.
- Occurrence-level English normalization ledger through no. 61: `controls/ENGLISH_NORMALIZATION_OCCURRENCES.csv`, 2,581 unique rows / 949,829 B / SHA-256 `9BCDA06605E2180462511F6C2D863ED5C83C21F9C99B184F01623EA95435B57E`.

## 2026-08-02 — Chapter II §2 no. 39 through §3 no. 43

- `FAC-EN-U0037`--`FAC-EN-U0041` translate French lines 1353--1486 / authority physical pp. 36--41 / printed pp. 231--236: the closed-subvariety ideal sheaf, fractional-ideal sheaves, the sheaf of sections of a vector-space fiber space, affine varieties, and the preliminary irreducible-variety propositions.
- Nos. 39--42 required no new printed-source correction or inherited transcription repair. Direct 1100-dpi comparison on physical pp. 37--41 controls their prose, formulae, and source footnotes. The English terminology ledger records every recurring choice, including “sheaf of fractional ideals,” historical “algebraic fiber space,” standard “structure group,” “nonsingular” rather than importing modern relative smoothness, and the type-explicit `\Delta\cap(U\times V)` notation.
- `FAC-FR-T0024` repairs inherited upright `\mathrm A` to the authority's italic variable `A` in the first intersection formula of no. 43. Both French layers now match print; this is a transcription repair, not a source correction. French reader page 29 passed personal 600-dpi review after converged three-pass rebuilds.
- The first no. 43 English build supplied an `x` subscript on two sum signs that are unindexed in Serre. `FAC-SELF-0029` records the pre-admission reversal; r2 restores both unindexed sums while retaining the indexed factors. Pages 36--37 then passed personal formula/layout review. `FAC-SELF-0030` records a harmless wrong executable lookup; `FAC-SELF-0031` repairs the provisional N0048 occurrence regex and binds both actual parenthesized-intersection occurrences.
- English `build_checkpoint_II_3_43_r2`: 37 A4 pages / 566,556 B / SHA-256 `D95A762FCA5CC0327CA024C475B883D9B63BBFB47EEEAEFDC78CE6CCA6680580`; pass-2/pass-3 console SHA `CBF06A4144102689CB413C967D7C87DC033BA40357AC721B85EB1122DF9B6F6D`; log SHA `EC2AA055EAD8339F946421B8280C252D0793204F50B5BD99E2A7A5C6FD6DD4B3`; hard/undefined/overfull diagnostics 0, one inherited harmless underfull notice.
- Diplomatic T0024: 63 pages / 634,126 B / SHA-256 `BABAE9A9A1E49ECAF66196B827C2633868E5607816873348C236A1A52A781065`. Corrected C0027/T0024: 63 pages / 634,414 B / SHA-256 `6B962F5B36E4EDF148C0E8FE27613AC9F483D962C758041863ED8826B93A0A29`. Both have byte-identical pass-2/pass-3 consoles, zero hard diagnostics, and only the inherited one overfull/three underfull notices.
- Exact continuation cursor: `fac_body.tex` line 1489 / printed p. 236 / no. 44, “Vanishing of certain cohomology groups.”

## 2026-08-02 — Chapter II §3, no. 44

- Translated `FAC-EN-U0042`, French lines 1489--1546 / authority physical pp. 41--42 / printed pp. 236--237, completing no. 44, “Vanishing of certain cohomology groups,” Proposition 7 and its three corollaries.
- Direct 1100-dpi authority inspection admitted `FAC-FR-C0028`: the print has `coincident` and `coincideront`; diplomatic French preserves both, corrected French restores `coïncident` and `coïncideront`, and English is naturally grammatical. It also admitted mathematical repair `FAC-FR-C0029`: the displayed coboundary summand prints `(-1)^q`, but the omitted-index summation is over `j` and the following cocycle reduction requires `(-1)^j`. Diplomatic French preserves the printed exponent; corrected French and English restore and disclose the alternating sign.
- Authority evidence: `qa/authority/opening_1100dpi/fac-41.png`, SHA-256 `2802D9DD12CED2300DBDD503AF51C21D11E3820758A419E8CA8E60731E9896AA`; `fac-42.png`, SHA-256 `31E177F46116262F97D84D9ED2265DD092510CF6C892992E950DE8C3E70A9A3B`. High-detail crops were used for the printed verb and sign, not OCR.
- English r1 was rejected before admission after rendered review exposed two literal `ldots` tokens introduced by patch escaping. `FAC-SELF-0033` records both occurrences; r2 restores `\ldots`, a full-component bare-command search is clean, and pages 37--39 visually PASS. `FAC-SELF-0032`, `0034`, and `0035` record zero-occurrence diagnostic/documentation failures that changed no artifact.
- Admitted English `build_checkpoint_II_3_44_r2`: 39 A4 pages / 574,891 B / SHA-256 `45C8AD4F101916A4B4BA476C19137419B211326FE1EC9AB6E063D96F85143DDA`; pass-2/pass-3 console SHA `6B94391807E46200D1615B7F51C886F222A079ABE51018645C5F2BA0D10BFFDD`; log SHA `CC5C3AB0A35C25F0498A8BDFAE4C9E4FBA435A534336B0E000634D78717EA062`; zero hard/undefined/overfull diagnostics and one harmless underfull notice.
- Diplomatic T0024 remains byte-identical at 63 pages / SHA-256 `BABAE9A9A1E49ECAF66196B827C2633868E5607816873348C236A1A52A781065`. Corrected French `build_checkpoint_C0029_T0024_r1`: 63 pages / 634,440 B / SHA-256 `5A364CCBBC6B180A0877E05338BD7DAF6223A5B27B91BA78CA7FB27EBA2E4C1B`; pass-2/pass-3 console SHA `72348E22D4D188F879680182589D8CF0E840094CB2C70E971176BFE5F3137782`; log SHA `ABE47D32019DB47710D928030B941EFBE6B54811C3EE7C36917385C26FD60B38`. Corrected pages 30--31 personally reviewed at 600 dpi: PASS.
- Normalization policies N0051--N0052 document “have no common zero” and “arbitrarily fine.” Replay now has 1,702 unique rows / 617,362 B / SHA `94D6B27D6FEAB298A1306E244B91961AB3B0CC992CA0B968184131455FDC4BD4`.
- Exact next cursor: `fac_body.tex` line 1549 / printed p. 237 / no. 45, “Sections of a coherent algebraic sheaf on an affine variety.”
