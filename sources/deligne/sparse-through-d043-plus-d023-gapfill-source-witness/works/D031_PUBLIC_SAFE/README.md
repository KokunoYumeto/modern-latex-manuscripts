# D031 independent normalization and gate

This is a task-local staging area, not a master-corpus or publication mutation.

`input_state` preserves the exact 20 members of the supplied S08 full state. The controlling source is `input_state/seed/20_AUTHORITY_DELIGNE_D031_SHIMURA_CANONICAL_MODELS_IAS_43PP.pdf`; the collected edition is comparison only. Both have 43 leaves. Printed pages are 247-289. The source header's 247-290 citation discrepancy is documented; page 290 is never synthesized.

`normalized` contains three independently editable native-TeX products: the diplomatic French reader, standalone English reader, and editorial apparatus. Each reader uses native mathematical notation, 23 TikZ-CD diagrams and seven TikZ Dynkin diagrams. No raster image substitutes for article text, formulas or diagrams. Each reader preserves one physical source leaf per PDF page and prints folios 247-289. The apparatus is separate.

All source corrections and presentation changes are explicit in `build_editions.py` and the normalized apparatus. Immutable inputs and inherited provenance remain available; inherited salvage is ZERO_ACCEPTED. Provenance-only candidate comparison notes are not promoted into the reader-facing apparatus.

To compile a delivered reader TeX file independently, use pdfLaTeX twice in its directory with shell escape disabled. Dependencies are standard LaTeX packages: Latin Modern, AMS math, mathrsfs, TikZ-CD/TikZ, microtype, geometry, booktabs, longtable, tabularx, adjustbox, fancyhdr and hyperref (plus needspace for apparatus heading clearance). The TeX does not require any image assets or the Markdown/Pandoc build path. Set `SOURCE_DATE_EPOCH=946684800` and `FORCE_SOURCE_DATE=1` for deterministic PDF builds. PDF dates and trailer IDs are suppressed in the source.

For full staged regeneration, `prepare_input.py` verifies/extracts the exact input and `build_editions.py` generates all three editions with Pandoc and compiles them. `--output replay` writes an independent replay. `render_qa.py` renders and checks outputs. `cold_audit.py` is nonpatching with respect to `normalized`: it rehashes before/after and checks structural, mathematical-regression and deterministic replay evidence. Source-pixel and translation review are recorded separately in `qa_content`; structural assertions are not presented as a glyph-by-glyph mathematical certification.

The authoritative final gate decision, once assembled, is `gate_acceptance.json`, with `gate_acceptance.md` and `gate_outputs.tsv`. Intermediate build success, old hashes, and the inherited return's COMPLETE/PASS statements are not acceptance.
