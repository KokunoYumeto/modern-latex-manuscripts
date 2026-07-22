# SGA2 Expose X Theorem 3.10 hold: GitHub readback

Pull request [#43](https://github.com/KokunoYumeto/modern-latex-manuscripts/pull/43)
merged the metadata-only hold at public `main` commit
`a03cf1a5cefe42285261725ed57130d9c5818f33`.

A fresh sparse clone resolved exactly to that commit with a clean worktree.
Five changed files matched the custody worktree byte for byte. The JSONL
checkout differed only by the repository's Windows line-ending filter: both
copies have Git blob `9d4dd11812019bc6fb82e93e7d14e1ae3fa49f60`, normalize to SHA-256
`BF1B169453EBDCA42CEF2A2513FFCD73B14675C0C9F3AB8AD83FE2E9FC8F9303`,
and parse as 72 records with 72 unique decision IDs.

The public tree contains the two metadata receipts and the linked
status/logbook updates. It does not contain the Theorem 3.10 TeX, PDF, target
render, source slice, or source-page rasters. Public source-bearing coverage
therefore remains through corrected French line 3574.

No private path, thread ID, or agent-name occurrence was introduced by the
merged diff. Zenodo remains unchanged at the same SGA concept; no draft,
mutation, or duplicate was created.
