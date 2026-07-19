# Build-log sanitization

All three pass logs and consoles were copied from the isolated public rebuild,
then scrubbed of the private build root, working-tree root, and user-home path.
The package-wide verifier rejects any residual absolute Windows user path,
personal workspace token, source-task identifier, or raw source-scan file/body.

Six sanitized compiler files are included. Passes 2 and 3 have zero recorded
TeX, LaTeX, package, reference, box, rerun, or missing-character diagnostics.
The unsanitized compiler files remain outside the public payload.