# Independent visual QA - 19 July 2026

The reviewer inspected the complete direct-source PDF physical pages 77 and
78 and the complete final target page at both 300 and 600 dpi. The original
printed page is 88 and the recomposed running pages are 69--70.

Verified against the source renders:

- the simple-complex statement for `P` and `Q`;
- the first abutment `H^*(underlined upright F P^bullet)`;
- both projective-of-finite-type hypotheses;
- the `L^bullet` Hom-complex isomorphism and maps `a`, `b`, and `c`;
- equation number `(1.5)` and arrow direction;
- the injective-resolution and Proposition 1.4 homotopy statements;
- the reference to `(1.1)` and the final `R^* underlined upright F(M)`;
- line 2617 as blank and line 2618 as the excluded continuation boundary.

The final target has no clipping, overlap, missing glyph, formula drift,
broken underline, or equation-number loss. The underlined `F` is upright as
required by `sga2-smf.sty` line 323; the earlier italic target form is rejected.

Render hashes:

- source p. 77, 300 dpi: `CC43BF59ABC2DBA1660B592CF7F463E6F5712B9B5FF95EC342F8BF681E71BBFA`;
- source p. 77, 600 dpi: `A946483BEA1B502E2873359385B0C9EFAE451500B407D0FC9F34FA475C63DD58`;
- source p. 78, 300 dpi: `D050BC08EBE75D720327351B0EBCA65ADE6258659CAC10EA6863EF527CE970A1`;
- source p. 78, 600 dpi: `6EB40AF7E88C873687F18F1F18655F5823C429482E611676FCE1BC387BE1572B`;
- final target p. 1, 300 dpi: `F5D5F9744F707AE480220B222C817ED15B61CF22251DCDFF5DA816E1942A784C`;
- final target p. 1, 600 dpi: `D6A81324532643B8358296F8E782D606498E6F827895611E8129ACA3D2E5E23F`.

Status: independent visual gate passed for the bounded unit only.
