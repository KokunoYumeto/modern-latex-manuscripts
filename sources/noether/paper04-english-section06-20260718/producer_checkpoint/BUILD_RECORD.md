# Isolated build record

- Engine: MiKTeX pdfTeX 1.40.29 through pdfLaTeX.
- Input set: one packaged TeX file only; no external TeX or image dependency.
- Passes: two, both exit code 0 with halt-on-error enabled.
- Pass 1: one expected rerunfilecheck warning; no fatal, undefined-command, or box diagnostic.
- Pass 2: zero warning, box, undefined-command, fatal, emergency-stop, or rerun diagnostics.
- Final TeX: 11,287 bytes; SHA-256 `68002AA81C7F1150E357D97741DFB57FB0FF23A6F8C705527B00569FA996EB68`.
- Final PDF: 289,603 bytes; SHA-256 `FC68D48F04C8CA95DE548987E7A1F8D4D5A8248AC6B8750CFEEB85C29DB0940C`.
- Extracted-text receipt: 11,991 bytes; SHA-256 `AE7EF7D03CA204FCF8532FE2905C53A93A96A5B8074DBE61A83DC96278765773`.

Raw logs are excluded because they contain machine-local paths. Their exact receipts are retained in the sanitized per-pass records.
