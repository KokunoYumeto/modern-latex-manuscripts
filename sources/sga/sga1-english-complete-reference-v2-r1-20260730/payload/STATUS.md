# SGA 1 complete English reader — stable reference-v2 successor

Status: **LOCAL PASS; immutable checkpoint packaging and independent replay pending**  
Date: 2026-07-30

## Scope

This no-overwrite successor contains the complete cumulative English SGA 1
LaTeX source and a 262-page cumulative PDF.  The reference pass preserves the
English mathematical text and pagination while giving every delivered internal
GoTo action a stable named target.

## Current reader

- PDF: `build_stable_alias_overlay_r6_source_complete/SGA1_English_complete_reference_reader.pdf`
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

Machine evidence is in `controls/REFERENCE_*.csv`,
`controls/REFERENCE_GRAPH_VALIDATION.json`,
`controls/FINAL_PDF_QA_VALIDATION.json`, and the two
`controls/REPRODUCIBILITY_*.json` files.  Manual visual evidence is recorded in
`controls/MANUAL_VISUAL_QA_PASS.md`.

## Coordination

- EGA I remains exclusively owned by task
  `019f70c0-aa55-7723-b00a-1d95324af359`; latest reported cursor is
  Proposition 6.5.1 after continuous alignment through §6.4.13.
- EGA IV §§11–21 remain exclusively owned by task
  `019f711e-e434-7af2-9a4d-0cd038cfe022`; latest admitted coverage is through
  IV-3 printed page 148, with page 149 next.
- EGA II is complete through EOF, EGA III is locally complete, and EGA IV
  §§1–10 are a closed 270-page predecessor.  No numbered EGA I–IV reader gap is
  known to be ownerless.
- This task alone owns the SGA 1 reference successor.  No EGA root was entered.

No archive/publication/readback claim is made in this working status.  The next
step is a no-overwrite, privacy-clean exact checkpoint and independent replay.
