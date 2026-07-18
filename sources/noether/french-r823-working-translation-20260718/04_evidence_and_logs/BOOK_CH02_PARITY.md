# R823 French Chapter II source-parity record

## Authority and product

- Authority: `authority/R823/pkg_r823/Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717/1/01_cumulative/Noether_R823_cum_de.tex`, lines 21256--21542 inclusive, from the Chapter II heading through the last paragraph of section 13 and immediately before the Chapter III heading.
- Authority TeX SHA-256: `EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21`.
- Enclosing verified R823 ZIP SHA-256: `7AFC1B865EC710F6BECE507260605CBA7C950E5CC089C7464F63CBC20A8BD738`.
- French product: `working/r823_fr/post43/book_ch02_fr.tex`.
- French product SHA-256: `D1AA8A59F080DE0D7B422606F29C73F656DB991AC561B1A7629FB28EA854FE06` (21,271 bytes).

## Parity checks

The French file contains the complete Chapter II introduction and all nine true numbered sections, 5--13. Source and target each contain 36 displayed-math blocks, 323 inline-math openings, 11 labels in the identical sequence, 9 emphasized passages, 1 numbered source footnote, 2 paragraph-level proof headings, 1 enumeration, 1 centered theorem caption, 1 array, 2 `pmatrix` environments, and 56 blank-separated structural blocks. A token comparison of all displays after removing only translated `\text{...}` prose found no mathematical-token differences. There are no literal Unicode section signs or guillemets; section references use `\S{}`.

Canonical choices applied here include `extension du corps des coefficients` for *Koeffizientenerweiterung*, `corps de décomposition` for *Zerfällungskörper*, `complètement réductible` for *vollreduzibel*, `de première espèce` / `de seconde espèce` for the historical field classification, `groupe d'invariance` / `corps des invariants`, and `prolongement` for *Fortsetzung*. Mathematical notation, numbering, emphasis, labels, and the source footnote were retained.

## Smoke build

A temporary standalone LuaLaTeX wrapper (MiKTeX 26.5) compiled the file successfully after two passes. Final result: both passes exit 0; 6 pages; 189,647-byte PDF; 0 undefined-control/LaTeX/fatal errors; 0 overfull boxes; 0 LaTeX warnings. Final temporary log SHA-256: `C1966FA07A1A874666E83F0EB38B4E545F4BB6BCD4AED60339C368BD78AA6BAF`; temporary PDF SHA-256: `EFC85BE6A6B661DC00120CBA993F9820E0A8E7CC9E1719E688D530FDB3798755`. The temporary wrapper and outputs were removed after recording these results.

## R823 source ambiguities retained

1. In section 5, the displayed product repeats `\sum c_i\omega_i` as both factors although the right-hand side sums over `i,j`. It is identical in the R823 TeX and rendered authority and was not silently changed to a `j`-indexed second factor.
2. In section 6, R823 says that the basis elements are already contained in `\mathsf P`; this is mathematically awkward in context but was translated without substituting a different source object.
3. In the second half of section 11, R823 says that the `S_i` are made automorphisms of `\mathfrak Z`, then stipulates that they fix its elements and immediately applies them to `\mathfrak Z_{\mathsf Z}`. The French wording retains the displayed notation and does not invent a missing subscript.
4. Also in section 11, the display `S_i e_1=e_i+\cdots` conflicts typographically with the surrounding discussion of the sum `E_1`. The same lower-case `e_1` occurs in both the R823 TeX and rendered authority; it was preserved exactly.
