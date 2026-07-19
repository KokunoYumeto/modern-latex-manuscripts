# Unit status - Expose VIII proof comment and notation

Status: independently source-reviewed and sealed bounded internal working
unit against the corrected French TeX and direct compiled PDF. Cumulative
Expose VIII integration and full-volume completion remain pending.

- Unit ID: SGA2-VIII-P14N.
- Authority scope: corrected French lines 2583-2595; original printed pages
  86-87; physical source-PDF page 77; recomposed running page 69.
- Continuation cursor: French source line 2597 after blank line 2596.
- Coverage: proof-left-to-reader comment; Cartan--Eilenberg footnote; recall of
  Expose V notation; complete definition and differential of the simple Hom
  complex.
- Excluded: blank line 2596 and the construction beginning at line 2597.
- Comparison control: jcreinhold e7a259f is comparison-only. Its ordinary prose
  is useful; its partial^n silently changes the source's partial_n and is
  rejected.
- Source correction: none required. A target-only extraction defect was already
  corrected by replacing problematic extensible outer delimiters with ordinary
  matched parentheses; mathematical grouping is unchanged and independent text
  extraction contains zero forbidden controls.
- Build: fresh independent two-pass `pdflatex` PASS with zero final
  diagnostics. The PDF is one unencrypted A4 page with 18 embedded, subsetted
  Unicode font rows; 285390 bytes; SHA-256
  `F9505784012F4DA28123C1F0B7BB6E6BAB0C0731D7D8CB294342A8E7742941DF`.
  Editable TeX is 1977 bytes; SHA-256
  `604193CF5E4DC1B4BE6DA2D0A6280EEF0FDBD464DF8C2F71AA784A2D7B9DB066`.
- Render: source physical page 77 and target page 1 were freshly rendered and
  independently inspected at both 300 and 600 dpi without clipping, overlap,
  missing glyphs, formula defect, or footnote defect.
- Machine evidence: 39 substantive CSV records plus a 26-row exact manifest;
  14 structural JSONL records / 12 stable IDs; 9 difficulty and revision events
  / 8 stable IDs. Rectangularity, formula safety, authority hashes, JSONL parse,
  schema and reference closure, privacy, and exact-manifest gates pass.
  Artifact Tool imported, inspected, and rendered all five CSV tables.
- Review state: independently sealed as this bounded internal unit only. No
  archive, public, cumulative, or full-volume completion claim is made.
