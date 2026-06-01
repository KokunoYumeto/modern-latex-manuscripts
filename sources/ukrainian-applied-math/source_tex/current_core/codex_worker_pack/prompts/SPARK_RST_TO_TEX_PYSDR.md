# Spark prompt: PySDR Ukrainian RST -> clean TeX module

You are converting an already-Ukrainian PySDR `.rst` chapter into a clean XeLaTeX chapter for an applied mathematics reference.

Do not retranslate the Ukrainian prose from scratch. Normalize terminology only where needed.

Rules:

- Convert headings to `\chapter`, `\section`, `\subsection`.
- Convert math blocks to `equation`, `align`, or display math.
- Convert code blocks to `lstlisting`.
- Convert notes/warnings to short paragraphs or boxed notes.
- Remove web-navigation clutter, raw HTML directives, and interactive-widget references that do not work in PDF.
- Preserve filenames, code, equations, and technical acronyms.
- Add one final `\section{QA-перевірки}` with 5-10 checks relevant to the chapter.
- Output one complete `.tex` file.
