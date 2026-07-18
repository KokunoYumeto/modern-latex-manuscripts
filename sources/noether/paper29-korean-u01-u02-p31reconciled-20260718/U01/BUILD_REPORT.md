# P29 Korean U01 build report

Both standalone documents completed two XeLaTeX passes with `-interaction=nonstopmode -halt-on-error`.

| Artifact | Result | Pages | Page size | Notes |
|---|---|---:|---|---|
| `source/Noether_Paper29_German_P31_U01_control.pdf` | pass | 1 | A4, 595.28 × 841.89 pt | no fatal warning |
| `ko/Noether_Paper29_Korean_U01_v001.pdf` | pass | 1 | A4, 595.28 × 841.89 pt | two nonfatal underfull hboxes; visually acceptable |

The Korean target is editable TeX and contains no rasterized text. Text extraction returned 2,307 characters including 875 Hangul syllables, the title, criterion heading, the disambiguating phrases `유한 생성되는 것은`, `유한 생성 부분환`, and `가군 생성계`, the final `형식적` paragraph, footnote text, and all mathematical symbols. The source contains four `\footnote` commands and the target preserves four.

Current acceptance hashes after the finite-generation/module-generating-system fidelity correction are: TeX `1781D71A7B4EE1643E402E72A0D9604D2DDA4CFC1A294FB594DE21299BCD338C`; PDF `509AFF874A21B2FA0D4098330A80FF4FCB9800D84837C9BAF86A439777D2C676`; build log `E3D126D92E06488E6A25039738158C60313DC45AB3A2E5FAFAC626AC3FDA86EC`; extracted text `39CAA1AD170F1F15556305EB71516A268ACAC1F1919CE1F59BC57D28003B3FB6`.

Build success is not treated as source or visual certification. The separate render check and source-version cursor govern those claims.
