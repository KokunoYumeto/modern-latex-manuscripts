# QA report — HI-OLP-PUB-0001

Status: **accepted as a machine-assisted working-draft checkpoint**.

## Build and file identity

- Cumulative wrapper SHA-256:
  `B994D597F5C988685791566FC40343B3FD8F3536949951B27D08CCECF4D23E22`
- XeLaTeX/latexmk exit: 0
- Hard-error scan: 0 hits
- PDF: 14 pages; 184,823 bytes; SHA-256
  `80B48447897C49EFD28B9B15A6951EB1C78F2CEE7BFD8DB0C53938D71B4C7793`
- Build log: 85,408 bytes; SHA-256
  `E58EC11F1CB8211134DDECCF8A2784F90AA4CB4F61067B41D5E5B68474F8CE00`
- Console transcript: 73,982 bytes; SHA-256
  `3A22D3C293CA021DCC66F3ABB5294487D56E43D914D37715B2552239F0431CB1`

## Structural and linguistic checks

- All nine units passed their unit-level stable-ID, label, command,
  environment-event, inline-math, and OLP-token invariance checks before
  admission to the cumulative reader.
- All reader-facing text in the nine bounded target files is Hindi
  (`hi-Deva-IN`); formal syntax and identifiers remain source-bound.
- Poppler layout extraction produced 40,063 characters, zero Unicode
  replacement characters, and passed 11/11 positive Hindi probes.
- All nine English source-section titles were absent from the extracted target.
- Extraction SHA-256:
  `F18CBA85C45457E61A17869EEDFE0F2140ED42FA5ECB5168BCE64B824AAC5D21`.

## Fonts, language metadata, and visual review

- PDF catalogue language: `/Lang hi-IN`.
- `pdffonts`: 17/17 font instances embedded and subset; 17/17 have Unicode
  maps; all 5 Devanagari instances have Unicode maps.
- Every one of the 14 pages was rendered at 300 dpi and opened at original
  detail. Review found no clipping, overlap, missing glyphs, broken formulas,
  unintended blank pages, or footer/page-number defects.
- Each source unit also compiled independently and passed its own final-page
  visual check before inclusion.

## Honest limitations

- The PDF has no structure tree, marked-content declaration, or `ActualText`
  objects. It is untagged and is **not** certified as PDF/UA or fully
  accessible.
- Poppler extraction passed; pypdf's secondary extractor did not reproduce
  most exact Devanagari cluster probes reliably. This is retained as tool
  divergence, not hidden as a pass.
- No human linguistic review is claimed.
- This checkpoint contains nine sections, not the complete Open Logic corpus.

The individual 300 dpi render files and tool outputs are included here so the
reported QA can be independently audited.

