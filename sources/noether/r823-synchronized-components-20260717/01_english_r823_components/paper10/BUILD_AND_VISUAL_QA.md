# Build and visual-QA record: Noether Paper 10

Date: 2026-07-17

Build:

- two pdflatex passes completed with exit code 0;
- output: 6 A4 pages;
- producer: MiKTeX pdfTeX 1.40.29;
- final log scan: zero Overfull, Underfull, LaTeX warning, package warning,
  or fatal-error matches.

Render:

- render_check/paper10-1.png
- render_check/paper10-2.png
- render_check/paper10-3.png
- render_check/paper10-4.png
- render_check/paper10-5.png
- render_check/paper10-6.png

All six 144 dpi pages were inspected. The review covered the title/byline,
source-star note markers and footnote bodies, fraktur J, tau/sigma indices,
theta_i factor, restored linear-basis note, dot leaders, multiplication dot,
round delimiter, paragraph/display flow, margins, and page numbers.

Final result: pass. No clipped text, overlaps, missing glyphs, detached note
markers, or broken formulas remain.

Final TeX SHA-256:
27003A6B93E6671686A32162696B73BFC22BA0769E9FE98717E32C7A0B3E1EF1

Final PDF SHA-256:
4DE2EDC7AC7FC008B342DAA586090DB790E15F1F8605837F393B18C28347A263
