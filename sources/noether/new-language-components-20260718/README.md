# Noether Arabic, Persian, and Indonesian working components

This package preserves two bounded multilingual translation outputs against the
current Noether R823 German authority.

## Contents

- `01_paper06_ar_fa_opening/`: Paper 06 opening segments `P06-S0002`,
  `P06-S0004`, and `P06-S0005`, translated independently into Arabic and
  Iranian Persian. Both TeX targets compile in two warning-free XeLaTeX passes.
  The package includes the PDFs, decision records, bidirectional-typesetting
  invariants, source-use statement, terminology notes, session log, manifests,
  and render review. These are working translations with no native or external
  mathematical certification. Next source segment: `P06-S0006`.
- `02_paper36_id_complete/`: all five source segments of Noether Paper 36,
  translated into Indonesian. The one-page PDF was rebuilt twice with XeLaTeX
  during archive packaging, with zero logged warnings, overfull/underfull
  boxes, missing glyphs, or fatal diagnostics; the rendered page is included.
  The terminology ledger deliberately retains the unresolved German technical
  term `Differente`. This is a complete-work working translation, not a
  native-reviewed or critical edition.

The package does not imply that Paper 06 is complete in either Arabic or
Persian, that the Indonesian language branch extends beyond Paper 36, or that
any target has received community certification. TeX is the editable
authority; the R823 source coordinates and evidence files are retained so that
later reviewers can reproduce or correct the work.
