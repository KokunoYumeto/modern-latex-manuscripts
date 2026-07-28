# Independent Archive Rebuild Pass

Date: 2026-07-28

The archive-maintenance lane independently replayed the exact 14-file
TeX closure without modifying the producer root.

Results:

- three XeLaTeX passes exited successfully;
- the final log contains no fatal, undefined-reference, duplicate-label,
  missing-glyph, overfull-box, or rerun diagnostics;
- the rebuild has 37 A4 pages;
- all 37 extracted-text pages match the producer;
- all 37 decoded page-content streams match the producer;
- all page boxes, 227 named destinations, 58 internal GoTo actions,
  linked-page count, and 36 font resources match;
- invalid and external actions are zero;
- all 37 producer/rebuild 200-dpi raster pairs are byte-identical;
- all 37 pages were visually reviewed;
- the complete source has one native `tikz-cd` and no
  `\includegraphics` call;
- the producer tree remained byte-identical before and after replay.

The lead's 5000-dpi native-diagram comparison was also inspected. The
documented four label-side repairs are present in the delivered TeX.

This is a bounded technical PASS for custody of Exposé XXIII. It is not
whole-SGA3 completion, exhaustive reference-v2 certification, rights
clearance, peer review, or a critical-edition claim.
