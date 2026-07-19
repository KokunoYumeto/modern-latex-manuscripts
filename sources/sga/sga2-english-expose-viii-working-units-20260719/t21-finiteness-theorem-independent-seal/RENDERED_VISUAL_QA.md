# Rendered visual QA - Expose VIII Theorem 2.1

Fresh renders were produced after the final clean two-pass build and inspected
at original detail.

| Artifact | 300-dpi SHA-256 | 600-dpi SHA-256 | Result |
|---|---|---|---|
| Source physical PDF p. 78 | `D050BC08EBE75D720327351B0EBCA65ADE6258659CAC10EA6863EF527CE970A1` | `6EB40AF7E88C873687F18F1F18655F5823C429482E611676FCE1BC387BE1572B` | Pass |
| Source physical PDF p. 79 | `413899C59819721F60C6C001CB14214BEABA84FC302835F69B14C66D72B65ED2` | `B1A0E57ED810AB3E7812AFE89CE50279D8EA74071F28B7E5B7041683E7DF79FD` | Pass |
| Target p. 1 | `DED7EA1CC39272CE4A03597012F73311453D673BE88249C3174677B1A069C466` | `1819EF2FC709F2B2CA6DE5C2B7ADD81B3860210D4A8AA4C27D99567E08C01971` | Pass |

The source renders visibly confirm printed page 89, the re-composed running-page
transition 70-71, theorem-number/note placement, condition a), equation (2.1),
condition b), and the physical 78-79 break. Poppler reported legacy source
display-font lookup fallbacks, but both resolutions render the relevant source
text, formulas, bars, note markers, and page markers completely.

The target is one clean A4 page. Its authority box, automatic Section 2 and
Theorem 2.1 headings, exact `(1).` marker order, three footnotes, condition
letters, local-cohomology formula, two closure bars, equation number, and
coherence conclusion are legible. There is no clipping, overlap, black square,
missing glyph, broken note rule, or content from Corollary 2.2.

The renderer could not open the target at its very long absolute path. The
final PDF was copied byte-for-byte to a short inspection path; the source and
copy SHA-256 values were equal. Renders were made from that exact copy and
returned here. This is a tooling-path workaround, not a content substitution.

The source-page PNGs reproduce copyrighted French pages and are QA evidence,
not a statement that underlying French rights are transferred with the English
translation.
