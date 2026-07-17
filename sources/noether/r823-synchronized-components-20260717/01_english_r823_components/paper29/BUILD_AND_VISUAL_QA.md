# Build and visual-QA record: Noether Paper 29

Date: 2026-07-17

## Build

Source: `Noether_Paper29_English_R823_SourceChecked.tex`

Command used twice:

```text
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=<output/pdf> <source.tex>
```

Result:

- exit code 0 on both final passes;
- output: 4 A4 pages, 595.276 x 841.89 points;
- producer: MiKTeX pdfTeX 1.40.29;
- final log scan: zero `Overfull`, `Underfull`, LaTeX warning, package
  warning, or fatal-error matches.

## Render and visual inspection

The final PDF was rendered with Poppler at 144 dpi to:

- `render_check/paper29-1.png`
- `render_check/paper29-2.png`
- `render_check/paper29-3.png`
- `render_check/paper29-4.png`

All four latest images were inspected. The review covered title and byline,
paragraph and display flow, page numbers, footnote numbering and the repeated
source marker, fraktur and barred-field glyphs, the Galois resolvent, margins,
and the closing definitions.

Final result: pass. No clipped text, overlaps, missing glyphs, broken formulas,
or detached footnote markers remain.

Final TeX SHA-256:
`3556B19D32AAF4A12621CB3CAB482624E66F66DB5BC5F6021DBE69B4CEF4F174`

Final PDF SHA-256:
`D1AFBBB8D3B9BE7468737797902DD2B9BEE3265DB542E3728C77B9587C754BE1`
