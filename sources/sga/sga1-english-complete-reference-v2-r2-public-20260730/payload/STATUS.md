# SGA 1 complete English reader — stable reference-v2 successor

Status: **TECHNICAL PACKAGE PASS; independent exact-package replay PASS; archive handoff pending**  
Date: 2026-07-30

## Scope

This no-overwrite successor contains the complete cumulative English SGA 1
LaTeX source and a 262-page cumulative PDF.  The reference pass preserves the
English mathematical text and pagination while giving every delivered internal
GoTo action a stable named target.

## Current reader

- PDF: `SGA1_English_complete_reference_reader.pdf`
- bytes: 2,763,471
- SHA-256: `46406925C8EBBF4309A67CF4D84B493952EF99C067E1971F885F0F3AF326BA1E`
- pages: 262
- active source closure: 139 files / 1,046,685 bytes
- metadata: title, author/source basis, subject, creator, and keywords present

## Reference closure

- 933 stable semantic targets;
- 1,600/1,600 internal GoTo edges resolve and use stable IDs;
- 31 newly reviewed internal source applications;
- 189 reviewed positive residuals;
- exact candidate partition: 220 = 31 applications + 189 residuals;
- 2,151 total named destinations after retaining the original 1,218 names and
  adding 933 stable aliases;
- external EGA/other-SGA citations, the absent Exposé VII, inactive source
  branches, and one genuinely ambiguous duplicate printed number remain
  explicit nonedges rather than guessed links.

The two inherited table-of-contents footnote links that pdfTeX formerly sent to
its page-one fallback are now resolved at source level.  `Hfootnote.2` is
defined inside the VIII.3 body footnote on PDF page 133 and `Hfootnote.3` inside
the VIII.6 body footnote on PDF page 140.  The earlier r5 postbuild overrides
remain recorded as superseded adverse history.

## Build and PDF QA

- four-pass source build; pass 3 and pass 4 console logs byte-identical;
- final TeX log has zero undefined-reference, missing-destination,
  multiply-defined, duplicate-destination, missing-character, fatal, or
  emergency-stop diagnostics;
- 46/46 font objects embedded; Type 3 fonts 0;
- raster image XObjects 0;
- external/active PDF actions 0;
- active delivery-surface privacy hits 0 across 147 files;
- 262/262 rendered pages accepted at 180 dpi: 261 pixel-exact and page 102
  text/geometry-equivalent with a maximum `0.010925293 pt` subpixel shift;
- two independent clean wrapper builds reproduce all 262 decoded page streams,
  page text, 1,600 action targets/rectangles, 2,151 destination names, and every
  destination coordinate exactly.  Container hashes differ only because the
  TeX/PDF writers emit run-specific identifiers; byte identity is not the
  reproducibility contract.
- a separate read-only package replay revalidated the exact 178-row payload
  manifest, all CSV/JSON controls, privacy, fonts, PDF actions, and source
  closure; its isolated four-pass build reproduced all decoded page streams,
  text, link geometry, destination names, and destination coordinates.  The
  final independent receipt has SHA-256
  `218A18FAD327FCEBDBE273D5D9175CD8EA5D4CC803E373E54B7B5E008C0D3DF5`.

Machine evidence is in `controls/REFERENCE_*.csv`,
`controls/REFERENCE_GRAPH_VALIDATION.json`,
`controls/FINAL_PDF_QA_VALIDATION.json`, and the two
`controls/REPRODUCIBILITY_*.json` files.  Manual visual evidence is recorded in
`controls/MANUAL_VISUAL_QA_PASS.md`.

## Public release status

This public projection contains the complete cumulative reader, its buildable
TeX closure, and privacy-clean technical evidence. Internal task coordination
and machine-local paths are deliberately omitted. Earlier bounded checkpoints
remain available as immutable release history.
