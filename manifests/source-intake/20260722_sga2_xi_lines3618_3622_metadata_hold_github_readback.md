# SGA2 Expose XI lines 3618-3622 metadata hold GitHub readback

Date: 2026-07-22

Pull request [#66](https://github.com/KokunoYumeto/modern-latex-manuscripts/pull/66)
merged source commit `5c63cb73d82e2d1c86f4437b19c2e1a864b0633e` at public
`main` commit `392aafc225c2aabc20fdce827f179288d6813ea2`.

A fresh shallow sparse clone resolved exactly to the merge commit with a clean
worktree. The merge changes only the seven intended metadata paths. For every
path, the source-commit Git blob, merge-commit Git blob, and an independent
raw GitHub download have the same Git object identity.

| Path | Bytes | Raw SHA-256 |
|---|---:|---|
| `docs/pending-zenodo-uploads.md` | 1,315,315 | `4A38902E9FA7F21196670575000F038E5FD486312BAE4869E59C5422216D5E23` |
| `docs/project-status-dashboard.md` | 27,172 | `2858969506199E2501AC3208CBF942823E7B15D05C9DE61B5224ADE5A0AFAC00` |
| `manifests/archive-maintenance-logbook.jsonl` | 296,130 | `2A6E4BBAD2638DE424B6184638F29918C473D003EDD338CC725AE22B10A975A6` |
| `manifests/archive-maintenance-logbook.md` | 117,231 | `86B2B4708FA8F76B6919E153EC7C6D9355AC67CA087F8AA5A5DAA754C2298A64` |
| `manifests/current-status.md` | 698,413 | `1537BAA98022383D4AACEA4CAF976096680F165C2CD32184EAEFE7353E0B7025` |
| `manifests/source-intake/20260722_sga2_xi_lines3618_3622_reviewed_handoff_hold.json` | 5,649 | `6850F48E83553144D706D38916D1B58316AFB30D3DA8C36EE981337EF9244B47` |
| `manifests/source-intake/20260722_sga2_xi_lines3618_3622_reviewed_handoff_hold.md` | 5,175 | `ED5A5BDA1AC87F1EEBC9C46F64778799065615AC478E4439D17042977AD55E03` |

The raw public JSONL parses as 99 records with 99 unique decision IDs through
`AML-20260722-SGA-081`. The merge contains no TeX, PDF, source slice, machine
evidence body, image, workbook, ZIP, or other source-bearing artifact. Public
coverage therefore remains through corrected French line 3574.

The SGA Zenodo concept remains unchanged at published record 21435547,
version DOI `10.5281/zenodo.21435547`, 33 files / 73,450,481 bytes. No draft,
mutation, deposition, or duplicate was created. This closes GitHub metadata
custody and readback only.
