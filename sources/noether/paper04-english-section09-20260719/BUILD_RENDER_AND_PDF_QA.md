# Build, render, and PDF QA

The packaged TeX was copied alone into a fresh isolated directory and built
three times with pdfLaTeX. It has no input, include, graphics, bibliography,
or other external build dependency.

- Passes 1-3 exited zero.
- Pass 1 contained only the expected fresh-tree outline rerun request.
- Passes 2 and 3 contained zero warnings, box diagnostics, undefined
  controls, fatal errors, or rerun requests; their raw logs are byte-identical.
- Raw logs are excluded. Three concise receipts retain their byte counts,
  SHA-256 values, exit status, and diagnostic counts.
- The isolated PDF is 269,106 bytes, SHA-256
  `9548288D8F17EA4C4566C7AEBD40090094D018FA22680A8619048BDF1AB7349C`.
  Its difference from the locked reader is generated-time metadata only.
- The isolated layout extraction is byte-identical to the locked extraction:
  7,908 bytes, SHA-256
  `3A649C0A7CB4B822A5DCA364C8270F28B622DB6A2EB71A316B13F43A13B8A018`.
- Both isolated 200-dpi page renders are byte-identical to the packaged page
  renders.

The locked reader has two A4 pages, populated title, author, and subject
metadata, and no encryption. All 20 font objects are embedded, subset-named,
and Unicode mapped. Its action surface is one benign internal opening action
and six internal footnote links distributed 4/2 across the pages. It has no
JavaScript, external URI, launch action, form, attachment, embedded-file name
tree, collection, or encryption. It is not accessibility tagged.
