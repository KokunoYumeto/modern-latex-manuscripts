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
