# Paper 7 exact-slice extraction-script syntax repair

The first invocation of `qa/extract_exact_slices.ps1` stopped at PowerShell parse time with exit code `1` because the error-message interpolation used `$OutputPath:`. No output file was created or changed by that failed parse.

The producer changed only that interpolation token to `${OutputPath}:`. The next invocation exited `0`, produced the eight declared exact slices, and matched the two pinned complete-slice hashes. This repair affects only the local extraction script's error-message syntax; it changes no German, witness, Chinese translation, formula, or source cursor. It is an operational computation record, not validation.
