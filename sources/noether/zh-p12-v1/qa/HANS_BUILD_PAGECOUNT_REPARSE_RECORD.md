# Hans build page-count metadata repair

- Initial completed build-record SHA-256: `FCA11B143217F4059B3777AB8621F39B7DAE07E5CE76B77AE319044B6C315DE3`.
- The initial wrapper stored `pages_reported_by_log: null` because its regex began with `Output written on` and did not cross MiKTeX's wrapped log line.
- A narrower mechanical regex, `\((\d+) pages?`, reparses the already completed final engine log as 5 pages.
- No TeX, PDF, translation, or engine output is changed and XeLaTeX is not rerun for this metadata repair.
- No PDF is opened or rendered. This is build metadata only, not a visual or translation check.
