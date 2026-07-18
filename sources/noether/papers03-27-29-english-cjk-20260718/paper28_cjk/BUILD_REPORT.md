# Build report

Build date: 2026-07-18  
Engine: XeLaTeX (MiKTeX 26.5)  
Current unit authority: sealed 2026-07-18 Paper 28 complete-page audit, carried unchanged in the later sealed P31 head

Each TeX file was compiled with:

```text
xelatex -interaction=nonstopmode -halt-on-error <file.tex>
```

## Results

| Document | Pages | Bytes | Extracted text characters | Replacement/box characters | Fatal | Undefined control | Missing glyph | Overfull | Underfull | Font-shape warnings |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| German current control | 1 | 20,337 | 1,345 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Simplified Chinese | 1 | 53,321 | 426 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Traditional Chinese | 1 | 78,453 | 426 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Japanese | 1 | 74,078 | 478 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Korean | 1 | 50,175 | 597 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

All five PDFs are one-page A4 files. Final logs contain no fatal, undefined-control, missing-character, overfull, underfull, or font-shape diagnostics.

## Text-extraction checks

PDF text was extracted with Poppler-compatible `pdftotext` using UTF-8 output.

- Every output preserves the source citation `S. 144`; none retains the inherited `p. 144` mismatch.
- Every output preserves the numbered `3. E. Noether` entry and its complete title/location content.
- The German output contains `Gruppencharaktere`, `vollständig reduzibeln Ringes`, `Gruppenringes`, `unzerlegbare Idealklassen`, and `Rang`.
- Chinese outputs retain distinct Simplified/Traditional script forms and the historical/modern semisimple-ring control.
- Japanese preserves `群指標`, `完全可約環`, `半単純環`, `直既約`, and `階数`.
- Korean spaces survive extraction, including `군 지표`, `아이디얼 이론`, `반단순환`, `양쪽 아이디얼`, and `기약 표현`.
- No U+FFFD replacement character or U+25A1 box character occurs.

## Source check

The exact current Paper 28 span is:

```text
private-local://Documents/Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_LocalCodex_20260718_P28_FullPaperAudit_from_P27Head\1\03_audit\P28\P28_current_span_20260718.tex
SHA-256 DC27CAF7EA5ACA2B61F90C366001432073AFB9FEF79492A4061AB2C465A70933
```

That complete-page audit restored bold to the whole numbered author/location/title entry. The same Paper 28 span is present in the later sealed P31 head:

```text
private-local://Documents/Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP\1\01_current\cum_de_Local_20260718_P31.tex
SHA-256 A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F
```

The standalone German control has SHA-256:

```text
212F6C8B80337CA6BD56CAE052A7B81F5AC502E48F0A96336C41B01850C9DEFD
```

## Decision-record validation

Both files under `decisions/` were validated using JSON Schema draft 2020-12 plus format checking against:

```text
01_methodology/research_department/OPERATIONAL_DECISION_INTERFACE.schema.json
```

Both passed. The Korean `Rang` choice remains held. No scalar readiness, pan-CJK authority, external certification, or automatic promotion is asserted.

