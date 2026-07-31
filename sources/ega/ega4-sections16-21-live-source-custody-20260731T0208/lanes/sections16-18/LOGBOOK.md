# EGA IV §§16–18 logbook

## 2026-07-30 — opening freeze

- Bound the durable three-session allocation control `EGA_IV_SECTIONS11_21_THREE_SESSION_SPLIT_20260730.md`, 2,390 B, SHA-256 `D3BD7DAD97DC09973A624EC24772A19F4691BF7ED9BCF796AB5953C1D9C0283F`; this lane owns only §§16–18 and hard-stops before §19.
- Created the no-overwrite successor root.
- Copied `ega4-16.tex`, `ega4-17.tex`, and `ega4-18.tex` twice: immutable inherited inputs and active source-aligned working copies.
- Rehashed all three inherited files exactly against the predecessor source-aligned tree.
- Verified the authority PDF identity and 360-page extent.
- Located printed page 5 at physical PDF page 4.
- Compared printed page 5 against three direct-authority views: one 600-dpi whole page and overlapping 1800-dpi bands.
- Corrected the opening register, the mistranslation of *s’écrivent*, a dropped closing parenthesis, and several definition-level fidelity/grammar defects.
- Compared printed page 6 against one 600-dpi whole page and three overlapping 1800-dpi bands.
- Inspected the visually ambiguous transition-ideal formula at additional magnification and preserved the exact printed expression rather than normalizing it mathematically.
- Corrected the missing verb in the graded-module sentence, two variable/article defects in Example 16.1.3(ii), and the missing article in 16.1.4.
- Built the active §§16–18 harness in three XeLaTeX passes: 121 pages, 826,723 B, SHA-256 `B54952273B1643F65EB6943153B203D27C2EB6EE5B8B5D0063BAB46C45017008`; fatal errors 0, missing glyphs 0. Cross-volume references remain unresolved in this deliberately partial harness.
- Visually checked English output pages 2–3 at 600 dpi.
- Aligned printed page 7 from three direct 1800-dpi bands. Corrected a substantive lost exponent in the augmentation ideal (`I/I^n` → `I/I^{n+1}`), several broken proof clauses, a transition-homomorphism number disagreement, and proposition grammar.
- Aligned printed page 8 from three direct 1800-dpi bands. Corrected the inherited `I^n=I^m` to the authority's `I^n=I^{n+1}` and reversed “contained in Y” to the authority's “containing Y.”
- Examined the printed transition map in 16.1.9(b) at additional magnification: the authority visibly prints `φ_{n,n-1}` although its displayed domain/codomain and 16.1.2 convention require `φ_{n-1,n}`. Retained the mathematically coherent indices and added an explicit TeX source comment documenting the printed typo.
- Rebuilt in three passes: 121 pages, 826,692 B, SHA-256 `B2B4F394DC8AEC2CCAE11A2F7B49912AB62F1AF024B48F6098C21EBE1FF6B605`; fatal errors 0, missing glyphs 0.
- Visually checked English output pages 3–4 at 600 dpi.
- Current cursor: printed page 9 / authority physical page 8 / Remark 16.1.11(ii) continuation, active `ega4-16.tex` line 175.

## 2026-07-30 — printed pages 9–10

- Aligned printed page 9 / authority physical page 8 from one 600-dpi full page and three direct 1800-dpi bands. Corrected the page-opening continuation, several broken clauses in 16.2.1, and the grammar around its two commutative diagrams; the diagram nodes, arrows, directions, and labels matched the authority.
- Aligned printed page 10 / authority physical page 9 from one 600-dpi full page and three direct 1800-dpi bands.
- Corrected a substantive coefficient-ring error in diagram (16.2.1.4): the lower symmetric algebra is over `O_{Y'}`, not `O_Y`.
- Corrected a substantive character/meaning error in Proposition 16.2.2(iii): the homomorphism is `Gr(u)=gr(u)\otimes 1`, not `gr(u)\otimes I`.
- Repaired the composition paragraph, the canonical-projection clause, and surrounding English without altering formulas or diagram geometry.
- Built checkpoint r4, then rejected it on rendered inspection because the printed-page seam read “taking into Taking into account.” Preserved r4 as adverse history and corrected the continuation in source.
- Built checkpoint r5 in three XeLaTeX passes: 121 pages, 826,688 B, SHA-256 `EE8147A87CC2AF28B45BF9720D77AA1922E95CDD8CC38DB40E71E7C758AFBABC`; fatal errors 0, missing glyphs 0. One pre-existing overfull box in a later inherited section and the expected partial-harness undefined-reference summary remain.
- Rendered English pages 5–6 at 600 dpi. The corrected page seam, both page-10 diagrams, the `O_{Y'}` coefficient, the tensor factor `1`, and the transition into the proof of 16.2.2 are visually sound.
- Active `ega4-16.tex`: 176,540 B, SHA-256 `A2E0227D52CBA9B108F1B6D3AF96E10B6DF1EE38A40703057A1B3E61A67C510C`.
- Current cursor: printed page 11 / authority physical page 10 / Proposition 16.2.2 proof continuation, active `ega4-16.tex` line 278.

## 2026-07-30 — printed pages 11–12

- Corrected an initial Poppler page-selection offset before using the new views: the first render was printed p12, was relabeled from `physical010/printed011` to `physical011/printed012`, and printed p11 was then rendered from the correct physical page. No source decision was made from a mislabeled witness.
- Aligned printed page 11 from one 600-dpi page and three overlapping direct 1800-dpi bands.
- Restored the source equality `I'^n/I'^{n+1}=(I^n/I^{n+1})\otimes_A A'`, which the inherited English had omitted before the sheaf calculation.
- Restored the explicit citation to (0, 4.3.3), moved the `\supertilde` onto the module before pullback as printed, and corrected the primed global-sections term from `Gamma(Y, I'^n/I'^{n+1})` to `Gamma(Y', I'^n/I'^{n+1})`.
- Compared every node, arrow, direction, and label in the exact-sequence diagram directly with the authority; no diagram-geometry repair was needed.
- Aligned printed page 12 from its correctly labeled 600-dpi page and three overlapping 1800-dpi bands. Repaired plural subjects and the two successive fiber-product identifications in Corollary 16.2.3, while preserving its displayed maps and formulas.
- Built checkpoint r6 in three XeLaTeX passes: 121 pages, 826,971 B, SHA-256 `8F464F502C1C434F9D28C9729963465DDA94FD237D27134EF956268024A16D4C`; fatal errors 0, missing glyphs 0. One pre-existing overfull box in a later inherited section and the expected partial-harness undefined-reference summary remain.
- Rendered English pages 6–7 at 600 dpi and visually checked the restored affine-module equality, pullback/tensor formulas, exact-sequence diagram, Corollary 16.2.3 statement, and its base-change diagram.
- Active `ega4-16.tex`: 176,663 B, SHA-256 `982F19860664467DBDF43F18D32D60DD72384FAECB9CA82925CC229956C0B3DD`.
- Current cursor: printed page 13 / authority physical page 12 / Corollary 16.2.4 proof continuation, active `ega4-16.tex` line 386.

## 2026-07-30 — printed pages 13–14

- Aligned printed page 13 from one 600-dpi page and three overlapping direct 1800-dpi bands. Normalized the primed ideal notation in the exact diagram, restored the printed Erratum III locator in Remark 16.2.5(i), and repaired the description of the two canonical graded-algebra maps without changing their mathematical content.
- Compared the four-term conormal sequence in Proposition 16.2.7 directly against the authority; its nodes, three arrows, direction, terminal zero, and degree-one explanation agree.
- Aligned printed page 14 from one 600-dpi page and three overlapping direct 1800-dpi bands.
- Corrected the inherited `Gr_n(P^n_{X/S})` in 16.3.2 to the source's `Gr_n(P_{X/S})`; the extra superscript changed the object being discussed.
- Restored the Definition 16.3.1 reference to Erratum III, item 10, and corrected the augmentation-ideal wording.
- Replaced the inherited assertion that `delta^*(lambda#)` “fixes” the displayed sheaf and ideal with the source-faithful statement that it “leaves [them] invariant”; the source does not assert pointwise fixation.
- Built checkpoint r7 in three XeLaTeX passes: 121 pages, 827,040 B, SHA-256 `5774244064F3BFCF27AAE772C7195A9C4CABBE1EFD6D12004F40FA50556ED314`; fatal errors 0, missing glyphs 0. One pre-existing overfull box in a later inherited section and the expected partial-harness undefined-reference summary remain.
- Rendered English pages 8–9 at 600 dpi. Visually checked the page-13 exact diagram and conormal sequence, the page-14 section transition, principal-parts notation, symmetric-algebra map, two algebra structures, and canonical-symmetry formulas.
- Active `ega4-16.tex`: 176,699 B, SHA-256 `0709ABA3B463E86C5CCB0CE8778BC684F4DBB55D27CBAF21713F4BB141214B35`.
- Current cursor: printed page 15 / authority physical page 14 / Proposition 16.3.4 continuation, active `ega4-16.tex` line 500.

## 2026-07-30 — printed pages 15–16

- Aligned printed page 15 from one 600-dpi page and three overlapping direct 1800-dpi bands. Corrected the canonical-symmetry proposition to say that the automorphism interchanges both algebra structures, repaired a missing verb in the projection-morphism paragraph, restored the printed Erratum IV item 11 locator, and corrected a missing comma in `Gamma(U,O_X)`.
- Retained the inherited non-source explanatory footnote only as an explicitly marked translator's note and repaired its English; it is not presented as authority text.
- Checked the affine principal-parts quotient, associated graded module, both ring homomorphisms, and formula (16.3.7.1) directly against the authority.
- Aligned printed page 16 from one 600-dpi page and three overlapping direct 1800-dpi bands. Both commutative diagrams in 16.4.1 and the factorization defining `v` match the authority node-for-node and arrow-for-arrow.
- Corrected the inherited description of `nu_infinity`: the source calls it a homomorphism of augmented sheaves of rings, not a homomorphism of graded rings.
- Built checkpoint r8 in three XeLaTeX passes: 121 pages, 827,104 B, SHA-256 `BA45B870C546E5C224B2FA5B6E809BA05D120F830751D0D55CFB2A6A702AE395`; fatal errors 0, missing glyphs 0. One pre-existing overfull box in a later inherited section and the expected partial-harness undefined-reference summary remain.
- Rendered English pages 9–11 at 600 dpi and visually checked the p15 formulas and Erratum IV locator, p16 propositions, the section-16.4 transition, both diagrams, the factorization, `nu_n`, `nu_infinity`, and `gr(u)`.
- Active `ega4-16.tex`: 176,713 B, SHA-256 `08187E6A5B870795AFFD5EB09B54D189AA2860FFF3937C7D777C4600BEE6D3A2`.
- Current cursor: printed page 17 / authority physical page 16 / 16.4.2 composition and transitivity, active `ega4-16.tex` line 631.

## 2026-07-30 — printed pages 17–18

- Aligned printed page 17 / authority physical page 16 from one 600-dpi full page and three overlapping direct 1800-dpi bands. Checked the two three-column functorial diagrams, the transitivity composite, the algebra-structure squares, and every arrow label directly against the authority.
- Corrected the inherited transitivity sentence's source-variable error: the morphism `v''` is deduced from `u'', w'', f, f''`; the inherited English incorrectly repeated `v''` in place of `w''`.
- Repaired the morphism/homomorphism distinction and the English clauses describing composition, transitivity, and functorial dependence, without changing the source formulas.
- Aligned printed page 18 / authority physical page 17 from one 600-dpi full page and three overlapping direct 1800-dpi bands. Verified the symmetry identity, the principal-parts map, the associated-graded and differential maps, all three commutative diagrams, and the affine ring interpretation directly against the authority.
- Repaired loose connective prose on page 18; the formulas, nodes, arrow directions, arrow labels, and coefficient rings required no mathematical correction.
- Built checkpoint r9 in three XeLaTeX passes: 121 pages, 827,157 B, SHA-256 `3C90B846762303B16A98447EE9B543970764175DE8D7B3D21335BECF8782CAE6`; fatal errors 0, missing glyphs 0. One pre-existing overfull box in a later inherited section and the expected partial-harness undefined-reference summary remain.
- Rendered English pages 11–13 at both 300 and 600 dpi. Visually checked the page-17 composition/transitivity continuation, the page-18 algebra-structure diagrams and formulas, and the transition to Proposition 16.4.5; no clipping, collision, or malformed diagram was found.
- Active `ega4-16.tex`: 176,685 B, SHA-256 `88D983C556603FB3552BFCC2091EF5D4F270055A1B21A8D64EE39515E2F53E6C`.
- Current cursor: printed page 19 / authority physical page 18 / Proposition 16.4.5, active `ega4-16.tex` line 737.

## 2026-07-30 — printed pages 19–20

- Aligned printed page 19 / authority physical page 18 from one 600-dpi full page and three overlapping direct 1800-dpi bands. Checked Proposition 16.4.5, Corollary 16.4.6, the vector-bundle construction, the augmentation maps, and every displayed formula directly against the authority.
- Corrected both inherited occurrences of `Gr_n(P^n)` in Corollary 16.4.6 to the source's degree-`n` component `Gr_n(P)`; the inherited form applied the associated graded construction to the wrong truncated object.
- Corrected Proposition 16.4.8 from an isomorphism of graded `O_S`-algebras to the source's graded `O_X`-algebras.
- Aligned printed page 20 / authority physical page 19 from one 600-dpi full page and three overlapping direct 1800-dpi bands. Checked the split exact sequence, the two symmetric-algebra identifications, the kernel filtration, Lemma 16.4.8.3, and formula 16.4.8.4 directly against the authority.
- Corrected the diagonal's induced map from an inherited `O_X`-algebra map to the source's `O_S`-algebra map; removed an inherited spurious grading on the symmetric algebra inside `gr_I`; and restored `F'` (rather than `F`) in the final formula for `I^n/I^{n+1}`.
- Built checkpoint r10 in three XeLaTeX passes: 121 pages, 827,167 B, SHA-256 `DDEDFCA8B4BD56B2DE445EE37F382F9FE71B652D2B80CBFB1A7D4E6EE3BE7BBD`; fatal errors 0, missing glyphs 0. One pre-existing overfull box in a later inherited section and the expected partial-harness undefined-reference summary remain.
- Rendered English pages 13–14 at 600 dpi and visually checked all corrected formulas, the page-19/20 seam, the split sequence, the lemma statement, and its proof. No clipping, collision, malformed symbol, or diagram fault was found.
- Active `ega4-16.tex`: 176,722 B, SHA-256 `66A38E6BB2F73A93F2F8244FFA76612387D7BF3852C48E9232AA8E1F22D11C4B`.
- Current cursor: printed page 21 / authority physical page 20 / completion of Proposition 16.4.8 and Corollary 16.4.9, active `ega4-16.tex` line 854.

## 2026-07-30 — printed pages 21–22

- Aligned printed page 21 / authority physical page 20 from one 600-dpi full page and three overlapping direct 1800-dpi bands. Checked the conclusion of Proposition 16.4.8, both corollaries, the polynomial principal-parts description, Proposition 16.4.11, and all three diagrams directly against the authority.
- Corrected the inherited description of `d^n`: the map sends a polynomial `F(T)` to the class of `F(T+U)` modulo `K^{n+1}`; it does not itself “correspond to a polynomial.”
- Aligned printed page 22 / authority physical page 21 from one 600-dpi full page and three overlapping direct 1800-dpi bands. Checked both universal-section diagrams, the local closed-immersion reduction, residue-field and fibre corollaries, and the opening localization formula directly against the authority.
- Restored the source symbol `varpi_n` where the inherited English had a different barred-omega symbol; corrected the commutativity citation from the first 16.4.11.4 diagram to diagram 16.4.11.2 and repaired the malformed `16.4.11.4` label; restored the omitted target in `U cap f^{-1}(W) -> W`.
- Corrected Corollary 16.4.12 from `(P^n_{X/S})_x` to the source's `(P^n_{X/k})_x`, and repaired the surrounding product/universal-section prose.
- Built checkpoint r11 in three XeLaTeX passes: 121 pages, 827,253 B, SHA-256 `F33C020A3625E402BF15E52CBFFCC3E1F84E9A33C4D980ADFFFDCAE8BB1583AB`; fatal errors 0, missing glyphs 0. One pre-existing overfull box in a later inherited section and the expected partial-harness undefined-reference summary remain.
- Rendered English pages 14–16 at 600 dpi and visually checked all formulas and diagrams spanning printed pages 21–22, including both repaired references and the `X/k` formula. No clipping, collision, malformed label, or diagram fault was found.
- Active `ega4-16.tex`: 176,792 B, SHA-256 `DA14707D681F29A09C0654EC0FACEFCA74B5F6D0E684954C5C6211C82FA3A1A0`.
- Current cursor: printed page 23 / authority physical page 22 / continuation of Proposition 16.4.14, active `ega4-16.tex` line 970.

## 2026-07-31 — printed pages 23–24

- Aligned printed page 23 / authority physical page 22 from one 600-dpi full page and three overlapping direct 1800-dpi bands. Checked the localization projective system, stalk formulas, rational-function-field presentation, and both transitivity homomorphisms directly against the authority.
- Corrected the associated-graded wording, restored `r` variables in the quotient polynomial ring, corrected the homomorphism direction, pluralized the two canonical homomorphisms, and corrected the augmentation ideal from `f^*(P^n_{X/Z})` to `f^*(P^n_{Y/Z})`.
- Aligned printed page 24 / authority physical page 23 from one 600-dpi full page and three overlapping direct 1800-dpi bands. Checked diagram 16.4.18.3 node-for-node and arrow-for-arrow, the ideal-quotient proof, exact sequence 16.4.19.1, and Proposition 16.4.20's opening directly against the authority.
- Corrected the diagram label `f times_z f` to the source's `f times_Z f`; corrected the parenthetical target of `d^n_{Y/Z}(K)` from `P^n_{X/Z}` to `P^n_{Y/Z}`.
- Built checkpoint r12 in three XeLaTeX passes: 121 pages, 827,255 B, SHA-256 `70101E8879699776FAA82234E2AFB6EF22EEF9CDFFEB6FF8C2DD4F01BE847E34`; log 146,341 B, SHA-256 `ACCB1C6D61FFC143A6938EC6DA7EC8CEDCD7B477A9216120994DE4D9617AB94A`; fatal errors 0 and missing glyphs 0. One pre-existing overfull box in a later inherited section and the expected partial-harness undefined-reference summary remain.
- Rendered English pages 16–18 at 600 dpi and personally checked the page-23/24 formulas, the repaired transitivity diagram label, the conormal sequence, the closed-immersion proposition, and the transition into printed page 25. No clipping, collision, malformed symbol, or diagram fault was found.
- Active `ega4-16.tex`: 176,796 B, SHA-256 `2779422E8C88A3FD33F588010786FC88CC99FAF94A05D9904228CC3EA9820503`.
- Current cursor: printed page 25 / authority physical page 24 / continuation of Proposition 16.4.20, active `ega4-16.tex` line 1093.

## 2026-07-31 — printed pages 25–30

- Aligned printed pp.25–30 / authority physical pp.24–29 from one 600-dpi whole-page view and three overlapping direct 1800-dpi bands per page; a formula on p.26 received an additional focused 1800-dpi crop.
- Corrected a duplicated word and a broken proof clause on p.25.
- On p.26 corrected the symmetric-factorization target from `P^n_{Z/Y}` to `P^n_{Z/X}`, the map subscript from `q_{Z/X/S}` to `q_{Z/Y/S}`, and the reversed relation “kernel is a direct summand of the image” to the source-faithful complementary-image statement. Retained the mathematically coherent `q^*(P^n_{Y/S})` where the printed parenthesis visibly has the inconsistent `q^*(P^n_{Z/S})`.
- On p.27 restored the canonical inclusion `iota_{O_X}+D`, corrected the derivation-sheaf notation to `Der_S`, and repaired definition register.
- On p.28 corrected the glued local homomorphism's domain from `O_X` to `Omega^1_{X/S}`, a substantive mathematical error; restored the stalk language.
- On pp.29–30 repaired uniqueness/base-change prose and a missing conjunction between cited results.
- Built checkpoint r13 in three passes to 121 pages; PDF 827,397 B, SHA-256 `7E9A62ED5EE70CF444849C5CDE40D62C800C1857B47C075BD34D3193C82066A8`; build log SHA-256 `228D679B8699EAA7833A942E135B72C37BE5A67B92CCCA6ECFA91AFAD4101CC9`.
- Rendered and personally inspected English pages 17–24 at 600 dpi. Mathematical displays and diagrams were sound. This check exposed that the partial harness had not initialized the section counter, causing headings `1.5`/`1.6`; the harness correction was queued with the next substantive build.

## 2026-07-31 — printed pages 31–36

- Aligned printed pp.31–36 / authority physical pp.30–35 from one 600-dpi whole-page view and three overlapping direct 1800-dpi bands per page.
- On p.31 corrected the inherited base-change direction `S -> S'` to the authority's `S' -> S`; normalized “square-zero”; restored “same underlying topological space.”
- On p.32 corrected the square-zero ideal throughout from the stray `I` back to the defined `J`, including `Hom(u_0^*Omega,J)`, and repaired the morphism/torsor prose. Diagram 16.5.14.3 agrees with the authority.
- On pp.33–34 corrected “torsor over” to “torsor under,” corrected the corollary's semantically intended cross-reference from 16.5.16 to 16.5.17, and repaired the affine-triviality proof and exterior-power register.
- On p.35 corrected four substantive inherited defects in the exterior-differential construction: `B` (not `M`) is the `A`-algebra; the kernel is taken in `B tensor_A B`, not a fibre product; the formula quantifies `f,g` in `B`, not `A`; and the annihilated submodule is `B tensor_A I^2`. Also repaired the antiderivation prose and a finite-linear-combination typo.
- On p.36 corrected the generator check's variable mismatch and restored strict inequalities `i_1 < ... < i_p` in the wedge basis; repaired the range of the complementary index `k`.
- Added `setcounter{section}{15}` to the harness so the standalone reader displays the source's section numbers.
- Built checkpoint r14 in three XeLaTeX passes to 121 letter pages. Active source: 176,722 B, SHA-256 `427F3F3FBF5029AA1647DC18580F6D45BD2D42673BC119E388A2AC92F6384DD9`. PDF: 827,297 B, SHA-256 `46DE219B3DF9B5925D37763EA5B41DDDD037AD41B12B2D27759F62E7C12A52C6`. Log: 146,301 B, SHA-256 `8595DC2BCD1F94064F67C90DB1D706D4A03CB7385C98323B80DD432D7A09BAB8`. Fatal errors, undefined control sequences, missing glyphs, and duplicate destinations: 0.
- Rendered English pages 23–30 at 600 dpi and personally checked the corrected torsor diagrams, source-page transitions, exterior-differential proof, wedge basis, and 16.7 opening. No clipping, collision, malformed symbol, or diagram fault was found; headings now display 16.5–16.7 correctly.
- Current cursor: printed page 37 / authority physical page 36 / continuation of 16.7.1, active `ega4-16.tex` line 1734.

## 2026-07-31 — printed pages 37–46

- Aligned printed pp.37–46 / authority physical pp.36–45 from one 600-dpi whole-page view and three overlapping direct 1800-dpi bands per page. Corrected an off-by-one in the temporary render commands before using pp.43–46; the authority-image filenames now match the printed leaves they contain.
- On pp.37–42 repaired several substantive inherited defects: a right/left module mismatch; a differential-label exponent; the object carrying the principal-parts algebra structure; the definition of order as an infimum rather than a supremum; the affine principal-parts quotient and its $B$-action; a wrong internal reference/equation tag; the description of the left vertical map; and the target of the continuous-homomorphism interpretation, which is the discrete group `Gamma(U,G)`.
- On p.43 corrected the proof from the false “equivalence of (a) and (b)” to the source's (a) and (c), restored the induction index set $I_n$, and corrected the representation of $D'$ from order $n$ to order $n'$.
- On pp.44–45 checked all three composition diagrams directly and repaired malformed nested principal-parts expressions, the lemma-proof heading/reference, tensor-factor prose, and several proof clauses without changing the formulas.
- On pp.45–46 corrected the direct-sum argument's functor from the nonsensical `U maps to Gamma(U,F)` to the source's `F maps to Gamma(U,F)`; restored the missing open neighbourhood $U$ in Definition 16.9.1; repaired the locally free differential-operator remark, immersion prose, a nonzero-element typo, and the malformed quasi-regular-sequence reference.
- Built checkpoint r15 in three XeLaTeX passes to 121 letter pages. Active source: 176,755 B, SHA-256 `CE9A3A21F0D8BE10065D24B9BACBBCD5A82E958A55FF31E9D9BDA445BC8D8A6A`. PDF: 827,826 B, SHA-256 `83137ED5636D9F18D4992B73FDB1AE7FDE7AB5E1B930F4DEDD8EE451FD176DB9`. Log: 146,293 B, SHA-256 `6835B1BC17EB88461B0922FA9530A502C6175C05BBAA373FB09BEFEED7F9FCF6`. Fatal errors, undefined control sequences, missing glyphs, and duplicate destinations: 0; the one overfull box is the pre-existing later-section line 2188 diagnostic.
- A native-command quoting mistake initially directed build output into a literal `$out` directory under `build_harness`; its generated files were moved into the intended r15 checkpoint, the empty accidental directory was removed, and no source file was affected.
- Rendered English reader pages 29–34 at 600 dpi and personally checked the corrected formulas and diagrams, pp.43–46 seams, proof endings, and the 16.8→16.9 transition. No clipping, collision, malformed symbol, or broken diagram was found.
- Current cursor: printed page 47 / authority physical page 46 / proof of Proposition 16.9.3, active `ega4-16.tex` line 2282.
