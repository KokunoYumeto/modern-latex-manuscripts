# Independent rendered visual QA - 2026-07-19

Direct source-PDF physical page 77 and the final target page were rendered and
inspected at both 300 dpi and 600 dpi.

The inspection confirmed the degree conditions on `A`, the direction of `a`,
the nested Hom order and minus sign in `L^{-q}`, source `CA` notation, the
underlined `F`, all bullets and primes, and visible labels (1.2)-(1.4). No
clipping, overlap, baseline collision, lost glyph, stray mark, or numbering
drift was observed in the target.

The page audit also confirmed that included French lines 2597-2609 are wholly
on original printed page 87. The marker for printed page 88 occurs only inside
excluded line 2611, after this unit's continuation cursor. This corrects the
earlier overbroad included-page envelope without changing the mathematical
body.

Render hashes:

- source 300 dpi: `CC43BF59ABC2DBA1660B592CF7F463E6F5712B9B5FF95EC342F8BF681E71BBFA`;
- source 600 dpi: `A946483BEA1B502E2873359385B0C9EFAE451500B407D0FC9F34FA475C63DD58`;
- target 300 dpi: `1D4B231CCCADFE34198B2FB728A3862F8E390E587E68FA4014C87AE22E51EB69`;
- target 600 dpi: `5EC562DE07D5FEFE3371FE2CAEE4B3DD53CDCB0674C2592619038398C4AB77F8`.
