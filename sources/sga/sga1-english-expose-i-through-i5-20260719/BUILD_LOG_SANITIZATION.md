# Build-log sanitization

Three concise public build receipts summarize the exact private build-log
hashes, sanitized-log hashes, diagnostic count, and successful output
terminus. They are synthetic receipts, not console transcripts. The other
three files are path-scrubbed full compiler logs: every line containing an
absolute local compiler path, plus wrapped continuation segments, is replaced
by a fixed redaction marker, while non-path lines retain their order.

The sanitizer verifies the expected raw hashes, rejects local user paths and
non-public workflow tokens, requires the successful nine-page output terminus,
and requires zero LaTeX warning, box, undefined-control, fatal, or emergency
diagnostics. Raw private-path logs remain local and are not distributed.
