# NOETHER_LOW_BANDWIDTH_GITHUB_STAGING_RUNBOOK_20260702

Status: local staging runbook, not a clone, fetch, commit, push, PR update, Zenodo action, or completion claim.

## Scope

This runbook turns the existing Noether offline commit plan into a reproducible low-bandwidth staging sequence for a future valid checkout of `KokunoYumeto/modern-latex-manuscripts`.

It does not store credentials. It does not copy raw GitHub tokens. It does not perform network actions. It does not claim that any remote branch, PR, or Zenodo deposition has been updated.

## Current Constraint

The current Noether workspace at `C:\Users\memo_\Documents\Codex\2026-06-29\updatede-goal-text-maintain-the-noether-2` is not a valid Git checkout. Its `.git` directory is present but lacks `HEAD`, config, refs, and packed refs.

The payload to stage later is:

`C:\Users\memo_\Documents\Codex\2026-06-29\updatede-goal-text-maintain-the-noether-2\work\github-api-payloads\noether-slavic-handoff\20260629`

The authoritative staging plan is:

`OFFLINE_GITHUB_COMMIT_BATCH_PLAN_20260630.json`

## Low-Bandwidth Checkout Shape

When network use is acceptable, use a fresh dedicated checkout. Prefer single-branch, no-tags, and partial-clone options:

```powershell
git clone --filter=blob:none --no-tags --single-branch --branch codex/noether-pc-20260629 https://github.com/KokunoYumeto/modern-latex-manuscripts.git C:\Users\memo_\Documents\Codex\github-checkouts\modern-latex-manuscripts-noether-pc-20260629
```

If the branch does not exist remotely, verify `codex/noether-slavic-handoff-20260628` first, then create the PC branch from that verified base. Do not claim this happened unless command output proves it.

## Small Text Staging Counts

The offline plan currently contains `214` commit-item rows. The default staging set is the `209` rows where `ready_for_small_text_commit` is true and `deferred_until_bandwidth_window` is false.

| Batch | Rows | Bytes |
| --- | ---: | ---: |
| `01_status_branch_orientation` | 5 | 24,131 |
| `02_source_core_packaging_and_lane_handoff` | 27 | 1,290,805 |
| `03_review_authority_packets` | 50 | 2,883,638 |
| `04_methodology_publication_and_terminology_governance` | 11 | 82,960 |
| `05_language_evidence_and_term_seeds` | 65 | 3,906,399 |
| `06_reproducibility_scripts` | 51 | 1,796,537 |

Total default staging set: `209` files, `9,984,470` bytes.

Deferred large metadata: `5` files, `22,103,134` bytes, split as:

- `large_json_metadata_ready_when_bandwidth_allows`: 2 files, 10,122,960 bytes
- `large_json_ready_when_bandwidth_allows`: 3 files, 11,980,174 bytes

The source-core zip remains outside the default small-text staging path.

## Helper Script

Use:

`stage_noether_payload_small_text_20260702.ps1`

Dry-run example:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs\stage_noether_payload_small_text_20260702.ps1 -CheckoutRoot C:\Users\memo_\Documents\Codex\github-checkouts\modern-latex-manuscripts-noether-pc-20260629
```

Apply example after reviewing dry-run output:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File C:\Users\memo_\Documents\Codex\2026-06-29\files-mentioned-by-the-user-worked\outputs\stage_noether_payload_small_text_20260702.ps1 -CheckoutRoot C:\Users\memo_\Documents\Codex\github-checkouts\modern-latex-manuscripts-noether-pc-20260629 -Apply
```

The helper refuses to run against a destination without `.git\HEAD`. It validates source file size and SHA-256 before copying. With `-Apply`, it creates needed directories and copies only the selected files. It does not stage with `git add`, commit, push, fetch, clone, authenticate, or call Zenodo.

## Dry-Run Validation

The helper was parsed by PowerShell and dry-run against a temporary local fake checkout containing only `.git\HEAD`. The temporary checkout was removed after path verification.

Observed dry-run result:

- `ok: true`
- `apply: false`
- Selected files: `209`
- Selected bytes: `9,984,470`
- Batch counts: `5`, `27`, `50`, `11`, `65`, `51`
- Network/auth/commit/push/Zenodo actions: `0`

## Commit Order After Staging

After a successful apply into a valid checkout, inspect the checkout with:

```powershell
git -C C:\Users\memo_\Documents\Codex\github-checkouts\modern-latex-manuscripts-noether-pc-20260629 status --short -- noether-slavic-handoff/20260629
```

Then commit in the six small-text batches first, following the `commit_batch_id` groups above. Large metadata and source-core archives should remain deferred until a bandwidth window or explicit upload strategy exists.

## Boundary

This runbook is coordination material. It does not resolve canonical rows, create translations, populate reviewer packets, ingest review returns, push GitHub, update PRs, or publish Zenodo records.
