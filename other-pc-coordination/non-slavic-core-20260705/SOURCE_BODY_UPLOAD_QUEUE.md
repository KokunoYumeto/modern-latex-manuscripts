# Non-Slavic Core Source Body Upload Queue

Generated: `2026-07-05T18:52:00+02:00`

Status: concrete body/path queue. Body paths may be local workspace paths or upstream Git paths. Upstream-only paths are real committed paths but may not be present in the local checkout until B3 reconciles upstream.

## Body Packages And Concrete Paths

| Queue | Lane | Location | Commit/local basis | Body status | Notes |
| --- | --- | --- | --- | --- | --- |
| BODY-R9-001 | R9 Africa/Horn/West | `language-source-bodies/r9-africa-horn-west-20260705/` | upstream commit `7b3ed05b899b3df9bf3d8d4d8a71b0ee5e5ec8b2` | real upstream source-body package | Contains manifests, SHA256SUMS, Hausa zip/PDF, Tigrinya arXiv/GitHub archives, extracted Tigrinya TeX/support files. |
| BODY-RTL-001 | Arabic RTL / Persianate / R3 | `language-source-bodies/rtl-persianate-arabic-20260705-r3-witness-layer/` | upstream commit `18bbadaa` | real upstream source-body package | Contains Arabic MathJax zip, Persian TeX/source zips, Arabic/Persian TeX/PDF witnesses, manifests and SHA256SUMS. |
| BODY-CORE-001 | Non-Slavic coordinator | `C:/Users/memo_/Documents/Codex/2026-06-29/updatede-goal-text-maintain-the-noether-2/work/github-checkouts/modern-latex-manuscripts-noether-pc-nocone-20260702/noether-slavic-handoff/20260629/cross-session-coordination/20260704/NOETHER_SESSION_OUTPUT_PACKAGE637_20260705T180014_ROLLING_DELTA_AFTER_PACKAGE636/` | local package directory, pushed at `3ce9d38e` plus README fix `4ad9b266` | coordinator handoff package, not source-body corpus | Contains active-row scaffold MD/CSV/JSON primaries and ledger copy. |
| BODY-LATEX-001 | Broad source-corpus support | `noether-source-corpus-provenance/20260704/NOETHER_DIRECT_GATED_LATEX_SOURCE_CANON_UPLOAD_20260704T232634Z/` | local safe checkout path if present; prior pushed shelf | gated TeX source-canon shelf | 524 TeX-family payload files were previously recorded; use as support, not blanket license clearance. |
| GAP-CJK-001 | CJK | `noether-cjk-native-source-evidence/outputs/` and `noether-cjk-source-evidence-draft-lane/outputs/` | local workspace | output artifacts present, no dedicated source-body package observed | B3/package lane should request or package CJK source bodies only if gated source witnesses are available. |
| GAP-ROM-001 | Romance | `noether-romance-source-evidence-draft-lane/outputs/` | local workspace | output artifacts present, no dedicated source-body package observed | Romance lane should emit body paths or explicit missing-body blockers. |
| GAP-R2-001 | R2 Pan-Turkic | `noether-r2-pan-turkic-hard-blockers/outputs/` | local workspace | output artifacts present, source-level package rows still gap-governed | Preserve hard-blocker status unless body/provenance exists. |
| GAP-R6-001 | R6 Indigenous/Creole/Sign | `noether-r6-indigenous-creole-sign/outputs/` | local workspace | output artifacts present, no dedicated source-body package observed | Per-language/community source-body acquisition required before draft. |
| GAP-R7-001 | R7 Malay/SEA/Pacific | `noether-r7-malay-sea-pacific/outputs/` | local workspace | Malay/Indonesian draft support exists; body package not observed | Queue non-covered SEA/Pacific rows for source bodies. |
| OLP-001 | OLP support | `noether-olp-relation-function-support/outputs/SESSION_K_FULL_SUPPORT_LANE_PAYLOAD_20260704.*` | local workspace | support payload manifest, not raw source-body package | Keep relation/function scaffolds tied to source anchors. |

## Upload Rules

- Do not upload credentials, OCR/runtime caches, `.traineddata`, or zip primaries through rolling packages unless the dedicated source-body package owns them.
- Upstream R9 and RTL packages are already source-body commits; B3 should reconcile them through Git/package state rather than re-copying blindly.
- All body rows remain source-canon/provenance support only.
