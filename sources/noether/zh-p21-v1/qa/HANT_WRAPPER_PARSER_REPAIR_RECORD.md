# Paper 21 Hant build-wrapper parser repair

During the first Hant build-driver invocation, XeLaTeX pass 1 completed with engine exit code `0` and created a three-page PDF. The surrounding producer wrapper then stopped because its page-summary parser required a byte count that this MiKTeX output did not print.

Only the wrapper's page-summary parser was broadened. The Hant TeX was not changed. A second driver invocation compiled the same TeX as pass 2 with engine exit code `0` and three pages. Exact pass-engine/stdout hashes and the driver note are preserved in `HANT_BUILD_RECORD.json`.

This is an operational parser repair, not a source, formula, language, visual, regional, or publication check. Neither PDF was opened or rendered for inspection.
