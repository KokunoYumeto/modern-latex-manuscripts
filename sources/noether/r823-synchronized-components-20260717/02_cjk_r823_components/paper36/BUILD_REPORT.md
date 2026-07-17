# Build report

Build date: 2026-07-17  
Engine: XeLaTeX (MiKTeX 26.5)  
Source authority: Noether R823

Each TeX file was compiled with:

```text
xelatex -interaction=nonstopmode -halt-on-error <file.tex>
```

## Results

| Document | Pages | Bytes | Extracted text characters | Replacement characters | Fatal | Undefined control | Missing glyph | Overfull | Underfull | Font-shape warnings |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| German R823 control | 1 | 25,175 | 538 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Simplified Chinese | 1 | 35,451 | 203 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| Traditional Chinese | 1 | 58,424 | 203 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Japanese | 1 | 61,643 | 237 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Korean | 1 | 33,378 | 285 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |

The CJK warnings are non-fatal font-shape substitutions for bold or italic CJK glyphs; the affected fonts lack those distinct faces. They do not represent missing characters. The German control has no warning.

## Text-extraction checks

PDF text was extracted with Poppler `pdftotext` using UTF-8 output.

- German title anchor present: `Idealdifferentiation und Differente`.
- Simplified Chinese title anchor present: `理想微分与不同`.
- Traditional Chinese title anchor present: `理想微分與不同`.
- Japanese title anchor present: `イデアル微分と共役差積`.
- Korean title anchor present: `아이디얼 미분과 디퍼런트`.
- All five extracts contain the citation, item number `2.`, author line, body, and closing publication sentence.
- The Simplified Chinese font was changed from FandolSong to SimSun after the first visually correct PDF produced unusable extracted text. The final PDF has proper Unicode extraction.
- The Korean document uses `fontspec` without `xeCJK`; this preserves normal Hangul word spaces in both the rendered page and extracted text.

## Source check

The exact R823 Paper 36 block is byte-for-byte identical to R822 and normalized-identical to R570. Exact cumulative block SHA-256:

```text
9474842663DE42505D0239DA2ABA1FBF22048ECC89A8D042C3403F69F549C7A6
```

The standalone German control adds a document wrapper and therefore has a different file hash, recorded in `SHA256SUMS.txt`.

## Decision-record validation

The three `decisions/*.json` records were validated with JSON Schema draft 2020-12 and format checking against:

```text
01_methodology/research_department/OPERATIONAL_DECISION_INTERFACE.schema.json
```

All three passed. No scalar readiness field or auto-promotion decision is present.
