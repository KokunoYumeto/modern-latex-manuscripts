# Build report

Build date: 2026-07-17  
Engine: XeLaTeX (MiKTeX 26.5)  
Source authority: Noether R823

Each TeX file was compiled with:

```text
xelatex -interaction=nonstopmode -halt-on-error <file.tex>
```

## Results

| Document | Pages | Bytes | Extracted text characters | Replacement/box characters | Fatal | Undefined control | Missing glyph | Overfull | Underfull | Font-shape warnings |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| German R823 control | 1 | 20,561 | 977 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Simplified Chinese | 1 | 55,082 | 397 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Traditional Chinese | 1 | 80,456 | 397 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Japanese | 1 | 75,649 | 476 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Korean | 1 | 47,665 | 537 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

All five PDFs are one-page A4 files. The final logs contain no fatal, undefined-control, missing-character, overfull, underfull, or font-shape diagnostics.

## Text-extraction checks

PDF text was extracted with Poppler `pdftotext` using UTF-8 output.

- All five outputs preserve `S. 102`; none retains the inherited `p. 102` mismatch.
- The German control contains `Doppelkettensatz`, `Teilerkette`, and `Vielfachenkette`.
- Each target preserves the source-defined double-chain concept and both chain clauses.
- Historically unsettled target terms retain visible German or English controls.
- Korean spaces survive extraction, including `대수적 수체`, `이중 사슬 조건`, and `유한 오더`.
- No U+FFFD replacement character or U+25A1 box character occurs.

## Source check

R570 and R823 differ in Paper 26 only in the author-name markup: R570 uses `\textsc{E. Noether}` and R823 uses plain `E. Noether`. The German prose and mathematical content are identical. The standalone R823 control TeX has SHA-256:

```text
97FA2651F8F2EF17E4E6D4DEB11295BBA7A8CA31D1AFD98C1BA6D04468533E17
```

## Decision-record validation

`decisions/NOE-P26-DOPPELKETTENSATZ.ko.json` was validated with JSON Schema draft 2020-12 plus format checking against:

```text
01_methodology/research_department/OPERATIONAL_DECISION_INTERFACE.schema.json
```

It passed. The Korean term remains held; no scalar readiness, pan-CJK authority, external certification, or automatic promotion is asserted.
