# Build-log sanitization

All three full compiler logs and all three full consoles were regenerated from
the fresh isolated public build, scrubbed of build/workspace/user paths, and
retained under evidence/build. Passes 2 and 3 have zero selected diagnostics.
The package-wide privacy gate and portable verifier inspect every public text
artifact after these files are written.

Sanitized files: 6.