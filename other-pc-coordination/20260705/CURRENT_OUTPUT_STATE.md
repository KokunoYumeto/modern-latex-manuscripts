# Current Output State - 2026-07-05

- Timestamp: 2026-07-05T18:48:41+02:00
- Active side branch target: `codex/noether-pc-20260629`
- Current payload: language-source-bodies/romance-germanic-baselines-20260705-spanish-san-salvador
- Per-session pursued-goal directory: session-pursued-goals/20260705
- Payload type: literal Spanish TeX-family source bodies plus per-session pursued-goal files
- Body files tracked in package manifest: 50
- Manifest-tracked bytes: 1957249
- Claims avoided: no native review, no accepted terminology, no translation completion, no source-fidelity certification, no publication readiness, no critical-edition claim, no blanket license clearance.

## Body Counts

| Extension | Count | Total bytes | Role |
|---|---:|---:|---|
| .bib | 2 | 45897 | Spanish TeX-family source body (bib) |
| .tex | 48 | 1911352 | Spanish TeX-family source body (tex) |

## Current Transfer Pass - 2026-07-05T19:17:23+02:00

- Active side branch target: `codex/noether-pc-20260629`; `main` not touched.
- Session 12 pursued goal: Directive P / Transfer-GitHub-Uploader block is recorded verbatim at the top of `SESSION_LOGBOOK_20260705.md` and `other-pc-coordination/20260705/SESSION_LOGBOOK_20260705.md`.
- Package roots prepared for side-branch transfer: 14.
- Package files prepared for transfer: 1289.
- Package bytes prepared for transfer: 1343302877.
- Transfer audit manifest rows: 1289 package-root committed-tree files, 1343302877 bytes.
- Package SHA256SUMS rows verified: 14 files, 1246 entries, 0 missing, 0 mismatched, 0 unparsed.
- Transfer audit checksums verified: 6 entries, 0 mismatched.
- Archives list-tested: 29 total, 29 OK, 0 failed.
- Files >= 100 MB: 0.
- Files >= 50 MB: 1, `language-source-bodies/rtl-persianate-arabic-20260705-r3-full-source-bodies/native-source-bodies/fa_IR/0005_ar_github_mohamed1984_arabicmath_zip.zip` at 86828566 bytes.
- Local credential scan: no GitHub/OpenAI/AWS/Slack/private-key token pattern matches in package roots.
- Claim scan: guarded/caveat/need-review terms remain in package metadata; no new native-review, accepted-terminology, license-clearance, gate-promotion, source-fidelity certification, publication-ready, critical-edition, or translation-completion claim is added by this transfer pass.
- Omission safety: three key-shaped public HTML files are omitted from the transfer tree and replaced by package-local omission ledgers.
- Transfer audit path: `transfer-audits/session12-20260705`.

## Transfer Package Roots

| Package root | Files | Bytes |
|---|---:|---:|
| `language-source-bodies/arabic-rtl-source-bodies-20260705` | 148 | 146815910 |
| `language-source-bodies/cjk-draft-source-evidence-20260705` | 29 | 17360032 |
| `language-source-bodies/cjk-native-source-bodies-20260705` | 82 | 2264176 |
| `language-source-bodies/persianate-tajik-source-bodies-20260705` | 60 | 92549940 |
| `language-source-bodies/r6-indigenous-creole-sign-20260705` | 195 | 364134758 |
| `language-source-bodies/r7-malay-sea-pacific-20260705` | 58 | 117316880 |
| `language-source-bodies/r9-africa-horn-west-20260705` | 16 | 8549953 |
| `language-source-bodies/romance-germanic-baselines-20260705-spanish-san-salvador` | 55 | 2050271 |
| `language-source-bodies/rtl-persianate-arabic-20260705-r3-full-source-bodies` | 197 | 341694950 |
| `language-source-bodies/rtl-persianate-arabic-20260705-r3-witness-layer` | 15 | 18559223 |
| `language-source-bodies/slavic-non-ru-uk-20260705` | 205 | 206273534 |
| `interlanguage-sidecar/fable-ledger-block-20260705` | 14 | 29662 |
| `handoff-bodies/olp-relation-function-support-20260705` | 207 | 26718913 |
| `other-pc-coordination/non-slavic-core-20260705` | 8 | 18316 |

## Post-Split Upload State - 2026-07-05T21:55:00+02:00

- Latest observed side-branch head before this audit note was staged: `739e63a1790fc119f9aa8c56b0b21677d20d2265`.
- R7 Malay/SEA/Pacific source bodies are pushed at `201ebbdbf55b854f72eb4fbf1057fcfbe070db3a`.
- R6 Indigenous/Creole/Sign source bodies were split after an oversized all-in-one push failed; the split series runs through `a0cb73ba8b0ca715c30af0d84e6802ad872b223d`.
- R3 Arabic/Persianate full source bodies are pushed across split commits; Arabic `0001-0099`, Persian, Tajik, OCR, manifests, hash sidecars, and the populated CSV manifest are present by head `739e63a1790fc119f9aa8c56b0b21677d20d2265`.
- Concurrent Slavic uploader commits were preserved by repeated fetch/reset/replay; this session did not overwrite those branch advances.
- Supplemental progress note: `transfer-audits/session12-20260705/UPLOAD_PROGRESS_AFTER_SPLIT_PUSHES_20260705.md`.
