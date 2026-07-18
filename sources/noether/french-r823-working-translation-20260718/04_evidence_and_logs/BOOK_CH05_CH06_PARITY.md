# R823 French Chapters V--VI parity evidence

Date: 2026-07-17  
Scope status: complete for the assigned post-43 book scope, Chapters V--VI and true sections 22--31. This is not a claim that the full French cumulative is integrated or visually approved.

## Deliverable and exact authority

- French TeX: working/r823_fr/post43/book_ch05_ch06_fr.tex
- French TeX SHA-256: 64110FF7F7A29C2ADEC1CF7E65C1A361AD72F3ECBC792BFD80BD0B10BF417B13
- Authoritative German TeX: authority/R823/pkg_r823/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717/1/01_cumulative/Noether_R823_cum_de.tex
- Authoritative German TeX SHA-256: EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21
- Reconciled authority range: one-based lines 22343--23717 inclusive.
- Range SHA-256: 9D0073E273927525A4870CF7BD9895ECE36D7FF2A1058F50AF6269238960D033, computed from UTF-8 text for lines 22343--23717 joined with LF and without a terminal LF.
- Start boundary: line 22343, “Kapitel V. Faktorensysteme”.
- End boundary: line 23717, \clearpage.
- Excluded boundary: line 23718, the Kapferer paper heading. No Kapferer text is duplicated here.

The true R823 section topology retained in the French file is:

| R823 line | Unit |
|---:|---|
| 22343 | Chapter V |
| 22345 | section 22 |
| 22441 | section 23 |
| 22566 | section 24 |
| 22971 | section 25 |
| 23265 | section 26 |
| 23320 | Chapter VI |
| 23322 | section 27 |
| 23451 | section 28 |
| 23582 | section 29 |
| 23602 | section 30 |
| 23679 | section 31 |
| 23717 | terminal \clearpage |

## Translation-memory inputs

The recovered post44 files were used only as non-authoritative phrasing memory. Their altered symbols, obsolete summary topology, and formula drift were not imported mechanically.

| Translation-memory file | SHA-256 |
|---|---|
| part03_chapter_V_section22.tex | B8B73C3FB8010AD712FA93ECA589BC9087410AFABCD5D6B26D06A06DB66AD999 |
| part04_chapter_V_section23.tex | E98AE99AA5633942C44CCB5D299C8F4BB7E3EAEF5E1DDFA352BA7477AE45BE2A |
| part05_chapter_V_section24_opening_hilfssatz.tex | DF852D03F3FD09784DC414F0FEF5169F05A1756B2E1BFFF449C82951D7422A26 |
| part06_chapter_V_section24_remainder.tex | 20F1924A10E517D2E6B24B8FC8CE3965721C29DDB0285305F978EED303E4B4FC |
| part07_chapter_V_section25_normal_representation.tex | 23CCDA9330540EA8D5866ECFE4A70E48BF8D5DBC412CFBB6CE35A0A6E8DF9D44 |
| part08_chapter_V_section26_multiplication_crossed_representations.tex | D2D486DC4C0D7CAEA8AF5234F0C2EEB9DD90200FD9A5E4C35A45611B2E35C505 |
| part09_chapter_VI_section27_crossed_products_definition.tex | B99563DA892E50A8D3BA41ABC1D4F80E71B79C11C8822E1909A1F0DAA53A8813 |
| part10_chapter_VI_section27_simplicity_lemmas.tex | E231DA0368517F3AB382C27C198D7E83F4FC0D7B30C400AB5F23537DB823C819 |
| part11_chapter_VI_section28_product_theorem_setup.tex | 9CB01090B6F2DFB062C7249910B23CD4BC236B54E143029BDA40E90377DF0456 |
| part12_chapter_VI_section28_product_theorem_proof.tex | E4F2B86CB8058AA9E2247D86DCEB0720E1F1BEF56A3AED8E683D8CE0793BCA17 |
| part13_chapter_VI_section29_hauptgeschlecht_minimal.tex | 89576F153C9EC4DE05764C5431887EBE0A1BCB958FF28C66E54CFF678017DC99 |
| part14_chapter_VI_section30_cyclic_splitting_fields.tex | 1C6305051662ADBC743C38CB1D251FC869EE58C1907965A80D4BFFC8C77EFAE7 |
| part15_chapter_VI_section31_applications_cyclic_case.tex | F256E931C0C53A36DCEF4516FA7BB9AA8109412F7F9BF80DEA498CFE512ABBDA |

## Structural and mathematical parity audit

The audit compared the German authority slice with the finished French file.

| Check | R823 | French | Result |
|---|---:|---:|---|
| chapter headings | 2 | 2 | pass |
| true numbered subsections | 10 | 10 | pass |
| display-math blocks | 189 | 189 | pass |
| begin / end environments | 13 / 13 | 13 / 13 | pass |
| equation tags | 4 | 4 | pass |
| source-note macros | 4 | 4 | pass |
| footnote mark / text | 1 / 1 | 1 / 1 | pass |
| theorem labels, including the reciprocal theorem | 13 | 13 | pass |
| lemma labels | 15 | 15 | pass |
| assertion labels | 2 | 2 | pass |
| definition labels | 4 | 4 | pass |
| terminal clearpage | 1 | 1 | pass |

For display mathematics, an ordered comparison normalized only whitespace, punctuation spacing, single-letter brace style, and localized contents of \text{...}. All 189 normalized display blocks match in the same order: 189/189, sequence ratio 1.0.

The source has 1,315 inline-math fields and the French has 1,313 because adjacent references are grouped differently in grammatical French. A containment audit over all inline and display math found every normalized source inline expression in the French mathematical fields: 0 uncovered expressions.

Additional lexical and syntax checks:

- no TODO, placeholder, untranslated German heading/register marker, replacement character, mojibake marker, or control character;
- no literal Unicode section sign or Unicode guillemet; headings and quotations use \S{}, \og, and \fg;
- all ten section numbers 22--31 are present exactly once as section headings;
- canonical terms occur consistently: système de facteurs, produit croisé, représentation croisée, corps de décomposition, and genre principal dans le cas minimal.

## Terminology decisions

| German R823 term | Canonical French used |
|---|---|
| Faktorensystem | système de facteurs |
| verschränktes Produkt | produit croisé |
| verschränkte Darstellung | représentation croisée |
| Zerfällungskörper | corps de décomposition |
| Hauptgeschlecht im Minimalen | genre principal dans le cas minimal |
| Hauptgeschlechtssatz im Minimalen | théorème du genre principal dans le cas minimal |
| reziprok isomorph | anti-isomorphe |
| Linksideal / Rechtsideal | idéal à gauche / idéal à droite |
| Pseudomatrizeneinheiten | pseudo-unités matricielles |
| kleines / großes Faktorensystem | petit / grand système de facteurs |

No Pan-Romance terminology was introduced.

## R823 readings preserved without silent emendation

The following apparent source-level anomalies remain exactly as printed in the R823 mathematics. They are not unresolved translation gaps:

1. Section 23 has S(\alpha_{ik}^{(j)})=\alpha_{\nu\mu}^{\tau} rather than a parenthesized superscript.
2. The Schur determinant line in section 24 prints \alpha_{ij}^{(k)n}=\delta_{ik}\delta_{kj}/\delta_{ik}.
3. The end of theorem 5 in section 24 first states \sigma_i\le\varrho_i and later displays \sigma_i\ge\varrho_i.
4. The section 24 conjugacy passage says that \lambda is \mathfrak q-invariant.
5. Section 25 prints H=\Theta_E^{-1}\Theta before the indexed form.
6. Section 28 retains the printed \mathfrak A_f, \mathfrak A_j, and P_n naming sequence.

These can be addressed only by a separate critical-emendation policy; changing them here would break R823 source parity.

## Isolated smoke build

Wrapper: C:\tmp\noether_fr_ch56_smoke_20260717\book_ch56_smoke.tex

The wrapper explicitly loads \usepackage{amsmath,amssymb,mathtools,mathrsfs}. The mathrsfs package is required because this chapter file contains 25 uses of \mathscr.

Command:

    lualatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=C:\tmp\noether_fr_ch56_smoke_20260717 C:\tmp\noether_fr_ch56_smoke_20260717\book_ch56_smoke.tex

Result:

- exit code 0;
- 21-page PDF, 432,631 bytes;
- no undefined control sequence, fatal error, overfull box, underfull box, or unresolved-reference warning;
- the sole log warning is the expected notice that inputenc is ignored by a UTF-8-native LuaTeX engine;
- pdftotext confirms both chapter headings and all ten section headings 22--31 in the built PDF.

Build artifacts and hashes:

| Artifact | SHA-256 |
|---|---|
| C:\tmp\noether_fr_ch56_smoke_20260717\book_ch56_smoke.tex | 04DFD92C8E4CA825F44E550B9DCC9FD135FD8290E07B1FED28F69FD4AAD5201D |
| C:\tmp\noether_fr_ch56_smoke_20260717\book_ch56_smoke.pdf | 4315646C9AF795576491EB71ECD80D8F8DEE570DC30926CA18490428878BA859 |
| C:\tmp\noether_fr_ch56_smoke_20260717\book_ch56_smoke.log | D91ED37E9EB0416423FF9EB452AA586BDBEBE40C3EE4105CC1C9C43FAF61C466 |

## Continuation cursor

1. Insert working/r823_fr/post43/book_ch05_ch06_fr.tex after the reconstructed Chapters III--IV file and before the Kapferer/Noether terminal-matter file.
2. Ensure the cumulative preamble loads mathrsfs; the standalone smoke test proves that this is an explicit dependency.
3. Do not add another Chapters V--VI summary or the obsolete post44 section topology.
4. The file already ends with the R823 line-23717 \clearpage; begin the next input at the Kapferer heading corresponding to R823 line 23718.
5. Rebuild the complete cumulative, then perform page-by-page visual QA on all pages occupied by sections 22--31 and representative transition spreads.

