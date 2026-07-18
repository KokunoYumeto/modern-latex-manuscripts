# Build-log sanitization receipt

The two source build logs were retained privately at 49,352 bytes each with
SHA-256
`F440A9CFA0A4615AD3FAD34597962C9F768AC3B2ADF19F60144CB85417E877D0`.
They contain machine-specific MiKTeX paths.

For publication, both copies were transformed deterministically by replacing
the private Windows user-root prefix, in its backslash, forward-slash, and one
line-wrapped occurrence, with `<LOCAL_USER_ROOT>`. No other replacement was
made.

The resulting files are each 49,723 bytes and have identical SHA-256
`4842DC57268881939F5565FCB6CC473DEBF4B245C16C500058B4C9CD95192946`.
Each contains 185 placeholder occurrences and zero occurrences of the private
path prefix. The diagnostics, page count, and build result are
otherwise unchanged.
