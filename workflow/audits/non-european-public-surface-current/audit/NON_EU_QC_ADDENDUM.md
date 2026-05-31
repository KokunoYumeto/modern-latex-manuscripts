# Non-European QC Addendum - 2026-05-31 23:21 local

This addendum distinguishes hard rendering blockers from typography/process cleanup.

- Strict rendered-page QC was rerun from short Windows paths to avoid false failures from external PDF tools hitting MAX_PATH-length issues.
- Result: 60/60 current public PDFs rendered as clean candidates; no sampled-page blank/dark/text-dump blocker remained in that test.
- Typography audit still flags 28 readers, mostly inconsistent page/body font sizing.
- The prioritized TODO list remains the repair guide: it flags visible process/source-page wording, raw markup risk, blankish pages, bounding overruns, and typography issues.
- Highest-priority visible repair remains al-Battani, where source-page labels and rough Arabic/OCR-looking text remain visible in many pages.
