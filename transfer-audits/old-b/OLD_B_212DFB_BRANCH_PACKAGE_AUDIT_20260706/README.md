# OLD B 212DFB Branch Package Audit

Audit time (UTC): 2026-07-06T07:50:40.2226638Z

## Scope

Old-B branch steward support lane only. B3 is the active package steward. This artifact is read-only audit/visibility output and does not commit, stage, push, edit PR metadata, use GitHub Issues, translate, alter language-lane artifacts, expose credentials, or make native-review/license-clearance/gate-promotion/source-certification/final-status/translation-completion claims.

## PR / Branch State

- Repository: KokunoYumeto/modern-latex-manuscripts
- PR: #1, open draft by GitHub connector check
- Branch: codex/noether-pc-20260629
- Live head: $(@{audit_time_utc=07/06/2026 07:46:34; repository=KokunoYumeto/modern-latex-manuscripts; pr_number=1; pr_state=open draft; branch=codex/noether-pc-20260629; live_head=212dfb1c7728f7c23274714434aa35d590e1aab7; pr_body_stale=yes; body still describes a40a32/package-148-era state; file_count=17285; total_bytes=8246010808; tex_family_count=3553; pdf_count=2401; archive_count=184; zip_count=167; manifest_sha_hash_like_count=4068; source_body_witness_like_count=4601; body_root_file_count=4819; body_root_bytes=4302103841}.live_head)
- PR body state: stale; still describes 40a32 / package 148 / 927-file era.

## Committed Tree Counts at 212dfb

- Files: 17285
- Bytes: 8246010808
- TeX-family bodies: 3553
- PDFs: 2401
- Archives: 184, including zips: 167
- Manifest/SHA/hash-like paths: 4068
- Source-body/source-witness-like paths: 4601
- Body-bearing roots: 4819 files / 4302103841 bytes

Body-root rollup:
- interlanguage-sidecar: 1963 files, 1085927522 bytes, TeX-family 397, PDFs 152, archives 60, manifest/hash-like 109
- language-source-bodies: 1934 files, 2952554057 bytes, TeX-family 287, PDFs 295, archives 41, manifest/hash-like 185
- noether-source-corpus-provenance: 552 files, 140655886 bytes, TeX-family 523, PDFs 0, archives 5, manifest/hash-like 15
- handoff-bodies: 207 files, 26718197 bytes, TeX-family 14, PDFs 1, archives 1, manifest/hash-like 14
- transfer-audits: 105 files, 95681585 bytes, TeX-family 0, PDFs 0, archives 2, manifest/hash-like 33
- formalization: 42 files, 126382 bytes, TeX-family 0, PDFs 0, archives 0, manifest/hash-like 4
- other-pc-coordination: 16 files, 440212 bytes, TeX-family 0, PDFs 0, archives 0, manifest/hash-like 4

## Package Frontier Compared to Old B Scope

- Old-B original package frontier: 148
- Stale PR body claims frontier: 148 (stale)
- Branch-visible max NOETHER_SESSION_OUTPUT_PACKAGE root: 637
- Branch-visible max package reference below 1000: 637
- Date-like package matches ignored: 1

Interpretation: Old-B package-148 scope is superseded; B3 owns any packaging/push. Package references below 1000 extend well beyond 148; date-like matches such as 2026 are separately ignored.

## Drift / Blockers

- PR body stale: GitHub connector live head 212df but body still describes a40a32/package 148/927 files -> B3/steward can update only if explicitly authorized
- Old-B no-push boundary: User explicitly assigned audit-only follow-up; B3 active steward -> Old-B produces outputs only
- B3 payload checkout dirty/detached: HEAD c55f07877c021a370c803a493aa84e011b13ed36, origin 212dfb1c7728f7c23274714434aa35d590e1aab7, status 241 -> B3 must reconcile before any package/push
- Old nocone checkout stale: HEAD 4ad9b266e47c2981979d46d2856bd5e3c3da861c, origin 212dfb1c7728f7c23274714434aa35d590e1aab7, status 0 -> Do not use as push base
- Local output drift after B3 snapshot: 200 files / 3448667 bytes after 2026-07-06T07:35:09.2262422Z -> B3 package review if still current

## Safety Scan

- Branch filename/path security-review hits: 8, recorded without secret values.
- Local drift credential-pattern hits: 0.
- Local drift files >= 50 MB: 0.

## Local Drift Snapshot

After the latest visible B3 output snapshot, old-B observed 200 non-B3/non-old-B local output files totaling 3448667 bytes. These are audit rows for B3 review, not old-B packaging authority.

## Key Ledgers

- BRANCH_TREE_MANIFEST_212DFB.csv: committed tree path/object/byte evidence.
- BRANCH_TREE_COUNTS_212DFB.json: aggregate branch counts.
- BODY_ROOT_COUNTS_212DFB.csv: body-bearing root rollup.
- PACKAGE_FRONTIER_SUMMARY_212DFB.json: old-B package-148 comparison.
- PACKAGE_REFERENCE_PATHS_212DFB.csv: package-number reference paths below 1000.
- NOETHER_SESSION_OUTPUT_PACKAGE_ROOTS_212DFB.csv: branch-visible NOETHER_SESSION_OUTPUT_PACKAGE* roots.
- DRIFT_AND_BLOCKER_ROWS.csv: no-push blockers and local drift rows.
- CHECKOUT_SAFETY_BLOCKERS.csv: B3/old-nocone safety state.
- LOCAL_OUTPUT_DRIFT_AFTER_B3_MANIFEST.csv: current local drift after B3 output baseline.
- MANIFEST.csv and SHA256SUMS.txt: audit-package self-manifest and checksums.
