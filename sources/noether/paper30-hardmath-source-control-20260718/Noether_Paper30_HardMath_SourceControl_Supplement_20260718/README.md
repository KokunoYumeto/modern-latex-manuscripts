# Noether Paper 30 Hard-Math Source-Control Supplement

This supplement records a bounded direct-source audit of German Paper 30, source pages 37-61, against the R823 cumulative German working source.

## Use

- `tex/Noether_R823_P30_HardMath_CodexChecked.tex` is the corrected 466-page cumulative German working source.
- `diff/R823_to_P30_HardMath_CodexChecked.diff` is the exact patch against the public R823 authority.
- `source_scan/Noether_P30_source_pages_037_061.pdf` is the direct source witness for the audited range.
- `witness_stacks/` shows the principal symbol changes against the scan.
- `audit/` preserves the original web-session diff and the rejected false-positive witness.
- `build/` records the two-pass LuaLaTeX build and hashes.

## Result

The checked patch has six diff hunks. It restores source-visible Greek exponent variables, a sigma/varrho distinction, a Fraktur-variable distinction, source line flow, and German quotation typography. One web-session edit was rejected: it changed ordinary German `durch` to literal `dnrch` after misreading the Fraktur shape of `u`. The corrected source retains `durch`.

The corrected cumulative source rebuilt to 466 pages with LuaLaTeX and no overfull, underfull, missing-character, undefined-reference, or fatal diagnostics in the final log.

## Status

This is a bounded source-control supplement and working reader. It does not certify all of Paper 30, all 43 papers, the translations, mathematical correctness, or critical-edition status. Translation branches have not been silently promoted to include these German corrections.
