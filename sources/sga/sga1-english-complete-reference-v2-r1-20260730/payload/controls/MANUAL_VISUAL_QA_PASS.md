# SGA 1 complete-reference reader — manual visual QA

Date: 2026-07-30  
Result: **PASS**

Controlling reader:

- `build_stable_alias_overlay_r6_source_complete/SGA1_English_complete_reference_reader.pdf`
- 262 pages
- SHA-256 `46406925C8EBBF4309A67CF4D84B493952EF99C067E1971F885F0F3AF326BA1E`

The exhaustive automated layout comparison rendered all 262 pages at 180 dpi.
This resolution is used only for delivered-reader layout QA, not as a source or
transcription witness.  Of the 262 pages, 261 are pixel-exact against the
pre-reference reader.  PDF page 102 has the same 607 words in the same order;
only nine word boxes differ, by at most `0.010925293 pt`, after the two new
bibliography links were inserted.  This is a bounded subpixel typesetting
difference, not a text, line-break, or layout change.  There are no material
render mismatches.

I personally inspected the following full-page 180-dpi renders from the final
reader:

- PDF page 2: source/status note and the newly linked Exposé VI/VIII sentence;
- PDF page 4: table of contents, including the VIII.3 and VIII.6 footnote marks;
- PDF page 102: both newly linked `VI.1` bibliography references and the sole
  subpixel-difference line;
- PDF page 133: VIII.3 heading and its body footnote target;
- PDF page 140: VIII.6 heading and its body footnote target;
- PDF page 262: terminal notation-index page and hard reader end.

The pages are legible and correctly composed; no text is clipped or displaced,
no link styling is visibly exposed, the two footnote bodies remain attached to
their headings, and the terminal page is intact.  Render evidence is under
`controls/manual_visual_qa_r6/`; the exhaustive per-page hashes are in
`controls/RENDER_QA_180DPI.csv`.

This visual receipt does not claim source-image or transcription review.  It
validates only the appearance of the completed English reader after reference
work.
