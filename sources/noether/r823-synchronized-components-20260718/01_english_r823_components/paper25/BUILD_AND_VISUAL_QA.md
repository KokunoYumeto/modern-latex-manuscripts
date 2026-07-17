# Build and visual-QA record: Noether Paper 25

Date: 2026-07-17

Build:

- two `pdflatex` passes completed with exit code 0;
- output: 3 A4 pages;
- producer: MiKTeX pdfTeX 1.40.29;
- final log scan: zero Overfull, Underfull, LaTeX warning, package warning,
  undefined-control, or fatal-error matches.

Render:

- `render_check/paper25-1.png`
- `render_check/paper25-2.png`
- `render_check/paper25-3.png`

All three pages were rendered at 144 dpi and inspected. Page 1 was checked for
the title period, lecture/byline block, `1)` marker, attached footnote body,
opening formula, typography, and lower margin. Page 2 was checked for the
source-style congruence, the visibly barred second Galois field, both norm
displays, line wrapping, and page boundary. Page 3 was checked for the
continued closing paragraph, received date, margins, and page number.

Final result: pass. No clipped text, overlaps, missing glyphs, broken formulas,
detached note bodies, or incorrect page boundaries remain.

Final TeX SHA-256:
`A6A82132029FA3E88A1319D56A70DAF95CC45AB9AC448A30D65F40C23AE92533`

Final PDF SHA-256:
`F4118520E9B1FE62A9074449DBA8855F74FE2928A08A42D3E1AA93B493BDA43F`

Final log SHA-256:
`1FF2CE7D0987F0AE5108AD009844BF190A6C8E6AD037CD1D6B504CCAACF4A271`
