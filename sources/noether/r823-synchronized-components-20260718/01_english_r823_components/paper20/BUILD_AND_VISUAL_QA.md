# Build and visual-QA record

Date: 2026-07-17

## Build

Source: `Noether_Paper20_English_R823_SourceChecked.tex`

Command used twice:

```text
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=<output/pdf> <source.tex>
```

Result:

- exit code: 0 on both passes;
- output pages: 5;
- page size: A4, 595.276 x 841.89 points;
- PDF producer: MiKTeX pdfTeX 1.40.29;
- log scan: zero `Overfull`, `Underfull`, LaTeX warning, package warning, or
  fatal-error matches.

The complete compiler transcript is retained as
`output/pdf/Noether_Paper20_English_R823_SourceChecked.log`.

## Render

The final PDF was rendered with Poppler at 144 dpi to:

- `render_check/paper20-1.png`
- `render_check/paper20-2.png`
- `render_check/paper20-3.png`
- `render_check/paper20-4.png`
- `render_check/paper20-5.png`

All five latest images were inspected. The review covered title/byline,
paragraph flow, display placement and numbering, footnote rules and numbering,
page numbers, fraktur and Greek glyphs, bars over mathematical symbols, and the
final section transition.

## Repair made after visual inspection

The first render exposed amsmath re-evaluation of an unnumbered
`\footnotemark`, which advanced the displayed Kronecker footnote from 8 to 11,
and left the equation (11) footnote marker on a separate line. The source was
repaired with explicit source numbers 8 and 9, recompiled twice, rerendered,
and rechecked. The final render shows footnotes 8, 9, and 10 in source order,
with markers attached to their respective displays.

## Final visual result

Pass. No clipped text, overlapping elements, missing glyphs, broken equations,
or detached footnote markers remain in the latest render.
