# Build and visual QA — Japanese Noether Paper 23

## Accepted exact build

- Target TeX: `Noether_Paper23_Japanese_SourceReconciled_v001.tex`, 23,152 bytes, SHA-256 `758D36CA12EA463AD4DC23A04536E801FB9A6B190F8E79E87C668EDC15FEC6D9`.
- XeLaTeX pass 1 log: `build_logs/xelatex_pass1.log`, 21,039 bytes, SHA-256 `E211ECFFE560CD1BA4147D0846903CC04706C4A310F8CE8832A9772C666C833E`.
- XeLaTeX pass 2 log: `build_logs/xelatex_pass2.log`, 21,039 bytes, SHA-256 `E211ECFFE560CD1BA4147D0846903CC04706C4A310F8CE8832A9772C666C833E`.
- Final PDF: `output/pdf/Noether_Paper23_Japanese_SourceReconciled_v001.pdf`, 270,267 bytes, SHA-256 `2D39C6B9D9E81CC38E29A6FB9A354EC489BF13455CC5D96AAF67CAB9FCCEB748`.
- Layout-preserving extraction: `output/pdf/Noether_Paper23_Japanese_SourceReconciled_v001.txt`, 22,906 bytes, SHA-256 `974C77BB552A106BDB8AF97C09B13D11189D7FE9CAB7E5A144AC13B0B332444B`.

Both consecutive builds completed successfully and produced four pages. Each final log has zero LaTeX, package, and font warnings; zero missing-character notices; zero overfull and underfull boxes; zero undefined controls; and zero emergency, fatal, or ordinary TeX errors. The PDF is untagged PDF 1.5, four A4 pages at 595.28 × 841.89 points, rotation 0.

The installed Codex Poppler command shim pointed to a missing runtime path. Rendering and PDF metadata inspection therefore used the present MiKTeX native `pdftoppm.exe` and `pdfinfo.exe` directly. `pdftotext.exe` produced the extraction. This tooling substitution changes no project content.

## Accepted rendered pages

All pages were rendered at 200 ppi to 1654 × 2339 PNGs and inspected individually at original detail. No contact sheet was created or used.

| Page | PNG SHA-256 | Bytes | Result |
|---:|---|---:|---|
| 1 | `9782FCEB3189FE0842A581F82945079BF1DEC09659B4CC30CC06B694E8A3AA43` | 853,268 | accepted |
| 2 | `6787036453135017EED0993724233423126DA3CF76D66D82EBA2C1C14B95BF54` | 1,036,103 | accepted |
| 3 | `D409568ED44D5123F1B5AAB70EB2E9EA4450E276F8D1EE43D098C2FE0C26DCB5` | 922,979 | accepted |
| 4 | `0E4FE45381D1EE83D1FAC0670548983973541CFB381F00077CA6EB3D757F745E` | 559,099 | accepted |

Accepted-set total: 3,371,449 bytes. Canonical sorted image-set digest: SHA-256 `6118ED10FBA7E73C280E502F8862ACC2E0F8303E23727CEAA292CB8469E400D5`.

The owning lane and an independent read-only reviewer found no clipping, collision, missing glyph, margin overflow, prohibited line-start small kana, or visible typography defect. Labels `(1)`–`(5)` render exactly once. Page joins are clean:

- page 1 ends after `三つの問題圏、`; page 2 starts with complete `すなわち有限個`;
- page 2 ends after the complete section-3 sentence and notes; page 3 starts with complete `その方法`;
- page 3 ends after a complete question; page 4 starts with the complete sentence `これは実際に可能である。`.

On page 4 a minimal `\nolinebreak[4]` between `ジ` and small `ュ` prevents a kinsoku violation without boxing the full name. Ordinary spacing is retained; the wrapped line starts with regular `ジ`, followed by small `ュ`.

## Rejected build history

Rejected candidates are retained under `tmp/rejected/` and excluded from the publication manifest:

1. `70B647E1_page_split_candidate`: page 1→2 split `有限個`; page 2→3 also separated `その` from `方法`.
2. `FE689FD3_page_split_candidate`: the first nonbreaking attempt shifted the page 1→2 defect to `すなわ／ち`.
3. `4F47561C_double_equation_parentheses_candidate`: page boundaries were clean, but all numbered displays rendered as `((1))`–`((5))` because `\tag` re-parenthesized literal labels.
4. `5EFDF4A9_katakana_line_start_candidate`: `\tag*` fixed labels, but page 4 began a line with small `ュ` after `ラグランジ／ュ`.
5. `375DCEEB_overstretched_line_candidate`: boxing all of `ラグランジュ` removed the kinsoku defect but over-stretched the preceding justified line.

Each rejection is a Japanese target-layout issue. None is a German-source defect and none triggers routing to `4 -nterslav`.

## Claims boundary

This is internal source/build/render QA. It is not external/community certification, independent Japanese human-reader signoff, or publication certification.
