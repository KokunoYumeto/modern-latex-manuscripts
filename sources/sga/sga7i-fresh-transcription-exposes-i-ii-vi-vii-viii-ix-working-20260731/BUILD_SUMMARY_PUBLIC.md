# Public build and validation summary

The reader was rebuilt from the seven packaged TeX files with three
`pdflatex` passes with a fixed archival build epoch. All three passes
completed successfully and produced the same 267-page, 2,002,517-byte PDF
with SHA-256
`45E4C2980260C8172AA3762BE0CDBF84FE1DCFC2FA23B724C64508A96F4D2E96`.

The final reader has 267 A4 pages, no text-empty pages, and no raster image
objects. Its decoded page-content streams, extracted page text, and page
geometry match the frozen producer gate reader on all 267 pages. The six TeX
bodies contain 528 unique page markers: scan indices 12-539 and source folios
1-528, each continuous with no gap or duplicate.

The build has no hard TeX errors, undefined-control-sequence errors, package
warnings, or LaTeX warnings. It reports seven overfull and thirteen underfull
horizontal boxes; the largest overfull box is 30.9277 pt in the terminal
publisher catalogue. Direct review of those pages found no clipping or overlap.
All 31 font resources are embedded; five are Type 3 resources inherited from
the source build. The PDF is untagged and is not claimed accessibility
remediated.

Representative visual review covered pages 1, 14, 18, 36, 47, 48, 50, 63,
76, 100, 117, 135, 150, 163, 220, 266, and 267. The review found no blank
render, clipping, overlap, malformed formula, or malformed diagram on those
pages.
