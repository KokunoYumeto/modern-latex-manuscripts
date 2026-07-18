# Controlled-Romance PDF output and visual QA v8

Date: 2026-07-17  
Scope: current T001–T004 build PDFs, final `output/pdf` delivery copies, and all nine pinned QA page renders.  
Result: **PASS** for current-artifact identity, required page counts, deterministic 150 dpi render reproduction, and visual layout.

This gate does not constitute native-speaker review, linguistic promotion, human comprehension evidence, marginal-intelligibility evidence, or a pilot result. Human/native observations recorded by this QA artifact: **0**.

## Executable verification

`scripts/verify_pdf_renders_v8.py` renders each build PDF afresh into its own automatically removed `TemporaryDirectory` under `tmp/pdfs`, using:

```text
C:\Users\Floris\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe -png -r 150 <build_pdf> <isolated_temporary_output_prefix>
```

Renderer identity:

- version: `pdftoppm version 26.05.0`;
- executable SHA-256: `742CBBD9A00931AD16C6618410BC40471375D639A45C61C1D86F3DCFC54B6388`.

Page counts are independently read from both the build and final-output PDFs with `pdfinfo version 26.05.0`, executable SHA-256 `BC2C0F980C9A2A29CD1E06AACD8D1C7B67A5304E9D1D6F75190BDEB9C81A4365`. The verifier requires exact pinned-page name sets, exact fresh-page name sets, matching SHA-256 values, and byte-for-byte equality of every fresh/pinned PNG pair.

The verifier was run twice. Both invocations passed, and the two resulting JSON files were byte-identical:

- pass 1 JSON SHA-256: `26E7AF22444EB8FD15A70E2EBB2366F0FE3910C0745EC6DA7EB3CFAA41947D09`;
- pass 2 JSON SHA-256: `26E7AF22444EB8FD15A70E2EBB2366F0FE3910C0745EC6DA7EB3CFAA41947D09`;
- explicit byte comparison: `true`.

## Build-to-delivery binding and page counts

Each final `output/pdf/R823_HG_T00N_controlled_romance.pdf` is byte-identical to the corresponding `R823_HG_T00N/build/R823_HG_T00N_romance.pdf`. Page counts agree across build PDF, output PDF, fresh render set, and pinned render set.

| Tranche | Required / observed pages | Build PDF SHA-256 | Final output PDF SHA-256 | Byte-identical |
|---|---:|---|---|---|
| T001 | 3 / 3 | `23DD4FD33C23419ED806431F7747A4EAF45BA32D87B301D47E83D899F7269B33` | `23DD4FD33C23419ED806431F7747A4EAF45BA32D87B301D47E83D899F7269B33` | yes |
| T002 | 2 / 2 | `1D8A7A28F05A0EEF665214BC458FF0CFF134B5AB300C41F041AED31D2A115E15` | `1D8A7A28F05A0EEF665214BC458FF0CFF134B5AB300C41F041AED31D2A115E15` | yes |
| T003 | 2 / 2 | `45399FC314B5337C3028EA473AE8D590FC303C41140DDC332AE6C7D822CC70A0` | `45399FC314B5337C3028EA473AE8D590FC303C41140DDC332AE6C7D822CC70A0` | yes |
| T004 | 2 / 2 | `3CAC96CD1305D55CBB11ED0AD8E079A62C634D64D08A585B2422AEC6BD3A9905` | `3CAC96CD1305D55CBB11ED0AD8E079A62C634D64D08A585B2422AEC6BD3A9905` | yes |

Total: four build PDFs, four bound final-output PDFs, and nine pages.

## Fresh-to-pinned render register

Every fresh PNG was 1241 × 1754 pixels in RGB mode and was byte-identical to its pinned QA PNG.

| Page | Pinned and fresh SHA-256 | First nonwhite row | Exact byte match |
|---|---|---:|---|
| T001 p1 | `FAA345E7D36A4BDC16419FAA54B5D92148AF014ADD810B9EAF1F7F3E80CBD66A` | 161 | yes |
| T001 p2 | `F924441F08E9B78C0487F765725DCC38259058CF3B6827D71E6A8E15520F7895` | 164 | yes |
| T001 p3 | `DC493909744FBE846F408CB193F6AAD2620EF502D704B62BE2A614F76A347BBF` | 161 | yes |
| T002 p1 | `C678D7910C4B9332DA6EA80C4A0965DA420D26BC6AA05B79D813E062F9341C86` | 161 | yes |
| T002 p2 | `81E74EB9D99D573173BF5E9034B5FDDBF57F98343A9133FF5A88386C335949CA` | 299 | yes |
| T003 p1 | `15B7DD9471FEB10819EE47D9C8A33AAD5E838A158F13AF44BF30D0E42B1F5053` | 161 | yes |
| T003 p2 | `0D3BEEEC4340AE63FC633ABEE90F23426E978EB8AF2B160E955601E8D1C004AA` | 299 | yes |
| T004 p1 | `7E6E9456D9AACA6877DBECAA24B5351F3BB01F8BF4D7626B66FDA924AB4CB383` | 161 | yes |
| T004 p2 | `05C9581D2325D4446C4FF7736F888EE41BBE65E27C53737C89B01FD86C6F86F3` | 299 | yes |

## Original-resolution visual inspection

All nine pinned pages—proven byte-identical to the fresh renders—were separately inspected at original resolution.

- **T001 pages 1–3: PASS.** Page 1's title hierarchy, status box, source-boundary block, prose, italic source titles, chapter transition, and footer are clear. Page 2's direct/reciprocal definitions, Fraktur symbols, stars, indices, containment signs, arrows, and displayed formulas are legible; its heading and footer are not clipped. Page 3's editorial note and tranche boundary are clear; the large remaining whitespace is intentional for the bounded unit. No overlap, missing glyph, margin escape, or clipped text was found.
- **T002 pages 1–2: PASS.** Page 1's title, status/source blocks, section heading, inverse/conjugation notation, italic terminology, and footer remain legible. The text finishes low on the page but does not collide with or obscure the page number. Page 2 begins at nonwhite row 299; heading cap height is fully visible and the editorial note, formulas, limit statement, and footer are clear. No clipping, overlap, missing glyph, or margin escape was found.
- **T003 pages 1–2: PASS.** Page 1's hierarchy, direct/reciprocal module definitions, Fraktur and starred symbols, action-order expressions, annihilator conditions, direct sums, and footer are legible. Page 2 begins at nonwhite row 299; its editorial distinctions and limit statement are clear. No clipping, overlap, missing glyph, or margin escape was found.
- **T004 pages 1–2: PASS.** The dense first page remains readable: title/status/source blocks, class-uniqueness statement, abbreviations, Fraktur symbols, primes, summations, transformation formulas, matrix indices, and footer all render cleanly. Page 2 begins at nonwhite row 299; the scope/order/image-map editorial note and tranche boundary are fully legible. No clipping, overlap, missing glyph, or margin escape was found.

## Version preservation

The v8 successor was added without modifying the v7 artifacts. Their preserved SHA-256 identities are:

- `scripts/verify_pdf_renders_v7.py`: `53DE89B50D08D483C2A463C8772AE78AE33CC0EAD40C434F78B4DFEA0389CA16`;
- `qa/PDF_RENDER_REPRODUCIBILITY_v7.json`: `7676C6FDD5962DA2D3F8753F300DB4EBD0210F1B82F3CBE323E27D0CD74B96D7`;
- `qa/PDF_VISUAL_QA_v7.md`: `F28538ACA4CCB2BAD6772A0E6AB86DC4BD19C6666EDDCFFC1D5218C4C75F8ECF`.

## Timestamp caveat and claim boundary

This gate binds and renders the current pinned PDFs. A later LuaLaTeX rebuild may change embedded `CreationDate`/`ModDate` values and therefore the PDF SHA-256 even when extracted text and rendered pages remain unchanged. Any such rebuild must be rebound to `output/pdf`, rerendered, and recorded through a new verifier run.

The PASS here is limited to file identity, page counts, deterministic Poppler rendering, and visible layout. Native validation, human intelligibility validation, and pilot status all remain explicitly false.
