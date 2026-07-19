# Build-log sanitization

Three concise public build receipts summarize the exact private full-log hash, each sanitized-log hash, the diagnostic count, all three TeX fragment dependencies, and the successful 13-page output terminus. They are synthetic receipts, not console transcripts. The other three files are path-scrubbed full compiler logs: every line containing an absolute local compiler path, plus wrapped continuation segments, is replaced by a fixed redaction marker, while non-path lines retain their order.

The sanitizer requires each 28,753-byte raw full log to have SHA-256 `CA53886EB5328A8633F4A871CECD9AD551D5B59B6876E1586168B1E389CCCE7F`, rejects local user paths and internal workflow tokens, requires the successful 13-page / 503,370-byte output terminus, and requires zero LaTeX warning, box, undefined-control, fatal, emergency, or rerun diagnostics. Raw private-path logs remain local and are not distributed.

The sanitized full-log hashes for passes 1--3 are respectively `16672771340FDDCC7F54496DC2CC038A03A92CB97E4A2BC57B72BC2F9962CADA`, `CFB99DC3ABFB4A6B1DDB44826C594BAA5BA3F2D0462439697B22D6765FC4391B`, and `10385ADA820CB1D93E43B716BD84C2AF6A1EBAFFE201032A4D1DAAE889BBC237`.
