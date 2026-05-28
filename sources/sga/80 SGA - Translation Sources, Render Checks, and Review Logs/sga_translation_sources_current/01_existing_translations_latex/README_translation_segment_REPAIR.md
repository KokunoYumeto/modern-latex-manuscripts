# translation segment repair of SGA 1-3 rendered PDFs

The translation segment package accidentally exposed SGA 1-3 as raw Markdown/plain-text preview PDFs. Those were not usable mathematical renderings: dollar-delimited formulas, bold markers, HTML comments, and code fences appeared literally.

translation segment supersedes those previews with XeLaTeX-rendered PDFs generated from the existing jcreinhold English Markdown snapshot via the Pandoc LaTeX source already present in the package, patched only enough to compile and to use broad Unicode fonts.

Use these PDFs:

- `fixed_math_render_pdfs/SGA1_existing_english_from_jcreinhold_mathfixed.pdf`
- `fixed_math_render_pdfs/SGA2_existing_english_from_jcreinhold_mathfixed.pdf`
- `fixed_math_render_pdfs/SGA3_existing_english_from_jcreinhold_mathfixed.pdf`

The prior raw previews have been moved to `superseded_raw_text_previews/` and should not be used for reading.

Status: this is a rendering repair, not a mathematical proofreading of the existing translation snapshot. Some display formulas inherited from fenced text blocks in the Markdown source remain monospaced rather than fully normalized LaTeX. The main failure mode reported by the user--raw Markdown displayed as the PDF body--is fixed.
