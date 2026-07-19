# Build, render, and PDF QA

The exact proposed TeX was copied alone to a fresh isolated directory and
built three times with pdfLaTeX. It has no `input`, `include`, graphics,
bibliography, or other external build dependency.

- Passes 1-3 exited zero.
- Pass 1 contained only the expected fresh-tree rerunfilecheck request.
- Passes 2 and 3 contained zero warnings, box diagnostics, undefined controls,
  fatal errors, or rerun requests.
- The isolated PDF is 328,554 bytes, SHA-256
  `045A3D79ABE928F8D641FB83D23D7FD648B962131A16F069F768525EF39BB699`.
  The differing PDF hash is generated-time metadata only.
- Its layout-preserving text extraction is byte-identical to the locked
  extraction: 17,173 bytes, SHA-256
  `F69D75EEC9557591B1F535279AC8DF0A6F9E2200584BDBCF2D799C0BC7DFB885`.
- All four fresh 200-dpi renders are byte-identical to the packaged target
  renders. Each pixel comparison therefore has absolute error 0 and RMSE 0.

All four pages and the contact sheet were inspected at original resolution.
No clipping, overlap, broken glyph, black box, missing formula, displaced tag,
unreadable disclosure, or malformed transition was found.

Both the locked and isolated readers have four A4 pages, populated title,
author, and subject metadata, and are unencrypted. The locked reader has 24
unique font objects; every object is embedded, subset-named, and Unicode
mapped. Its action surface is exactly one benign internal opening `/GoTo` and
six internal footnote `/GoTo` links distributed 0/1/1/4 by page. It has no
JavaScript, external URI, launch or additional action, form, attachment,
embedded-file name tree, collection, or encryption. It is not accessibility
tagged.

