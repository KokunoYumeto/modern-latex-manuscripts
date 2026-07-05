# Noether relation/function packages 101-119 GitHub staging exception

Date: 2026-07-03

Scope: Noether PC branch `codex/noether-pc-20260629`, cross-session coordination shelf `noether-slavic-handoff/20260629/cross-session-coordination/20260702`.

The local upload queue `NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702` was refreshed through package 119 and reports 449 queued files / 876,318,180 bytes with zero source-text or excerpt files. The queue policy remains: substantive artifacts should be staged/uploaded when a valid checkout path exists and should not be suppressed merely because of mobile-plan or bandwidth wording.

During GitHub staging, 135 queue files differed from the pushed branch. Of those:

- 133 files / 394,054,985 bytes were copied into the Git checkout for normal Git staging.
- 2 JSON files / 461,833,337 bytes were left local-only because each exceeds GitHub's 100 MB hard file limit for normal Git blobs.

Local-only over-limit files:

| package | local filename | bytes | sha256 | intended destination |
| --- | --- | ---: | --- | --- |
| 109 | `SEMI_CONSTRUCTED_RELATION_FUNCTION_P109_RESOLUTION_RETURN_EVIDENCE_CRITERIA_RUBRIC_20260702T124500Z.json` | 230,397,724 | `7C4FF1EEEA14EA0926EFF2FBDDF417430565D180393DB142B2B0390C31AF3E7E` | `noether-slavic-handoff/20260629/cross-session-coordination/20260702/SEMI_CONSTRUCTED_RELATION_FUNCTION_P109_RESOLUTION_RETURN_EVIDENCE_CRITERIA_RUBRIC_20260702T124500Z.json` |
| 110 | `SEMI_CONSTRUCTED_RELATION_FUNCTION_P110_RESOLUTION_RETURN_EVIDENCE_INTAKE_LEDGER_TEMPLATE_20260702T130000Z.json` | 231,435,613 | `D6EC61B3DD832EB12708F2C8DC2CC7CE7574604C4BEB4B570513554C9E25B3A3` | `noether-slavic-handoff/20260629/cross-session-coordination/20260702/SEMI_CONSTRUCTED_RELATION_FUNCTION_P110_RESOLUTION_RETURN_EVIDENCE_INTAKE_LEDGER_TEMPLATE_20260702T130000Z.json` |

The package 109/110 CSV, Markdown, checksum sidecars, coordination notes, and later package 111-119 artifacts remain eligible for normal Git staging where under the hard per-file limit. This exception does not claim a Zenodo upload, Git LFS configuration, dispatch, reviewer return, source-text ingestion, translation, canonical-row resolution, or readiness promotion.
