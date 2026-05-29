# Round 5 Arabic/font repair delta - not a final corpus

This is a targeted replacement delta. It is not a claim that the full corpus is clean or complete.

Included replacements:
- `10-11 English Translation - al-Kashi - Miftah al-Hisab.pdf`: 30 pages; missing-glyph warnings 0; compile errors 0; blank spacer pages removed [].
- `30-04 Arabic Translation - al-Kashi - Miftah al-Hisab.pdf`: 29 pages; missing-glyph warnings 0; compile errors 0; blank spacer pages removed [].
- `60-01 Islamic Original - al-Kashi - Miftah al-Hisab.pdf`: 27 pages; missing-glyph warnings 0; compile errors 0; blank spacer pages removed [].
- `10-12 English Translation - al-Khwarizmi - Algebra.pdf`: 30 pages; missing-glyph warnings 0; compile errors 0; blank spacer pages removed [4, 12, 27].
- `60-02 Islamic Original - al-Khwarizmi - Algebra.pdf`: 33 pages; missing-glyph warnings 0; compile errors 0; blank spacer pages removed [].

Held / not fixed in this delta:
- `30-05 Arabic Translation - al-Khwarizmi - Algebra.pdf` is not shipped: the available Arabic-enhanced source compiles only after font changes, but much of it is Latin transliteration rather than Arabic-script text.
- Omar Khayyam Arabic/bilingual files remain held because the source still has paracol/leftbar/preamble failures.
- Combined readers are not rebuilt in this delta; rebuilding them before all component repairs pass would reintroduce damaged pages.

Checks included: two-pass XeLaTeX logs, missing-glyph counts, final sample renders, text sweep, and SHA-256 checksums.
