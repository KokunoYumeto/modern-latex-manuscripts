# SGA2 Expose X line 3588 hold: GitHub readback

Pull request [#47](https://github.com/KokunoYumeto/modern-latex-manuscripts/pull/47)
merged the metadata-only hold at public `main` commit
`c1994efc86b8bbf39824d9acb1b8078e0abd8974`.

A fresh sparse clone resolved exactly to that commit with a clean worktree.
Five ordinary changed files matched the custody worktree byte for byte. The
JSONL checkout differed only by the repository's Windows line-ending filter:
both copies have Git blob `ab9ab524a89981d887e599eec81c25b492f43702`,
normalize to SHA-256
`5CF3EC9EAFEF7BD66485C8212B3FE6C6CD833B94E07D79A6C4EEB2E47F32B6F4`,
and parse as 76 records with 76 unique decision IDs.

The public tree contains the two metadata receipts and linked status/logbook
updates. It does not contain the line-3588 TeX, PDF, source slice, target
render, source-page raster, machine-panel images, comparison excerpt, raw
logs, or preserved privacy-failure evidence. Public source-bearing coverage
therefore remains through corrected French line 3574.

The merged diff introduced no private path, thread ID, or body/pixel file.
The official API recheck at 2026-07-22T04:06:31+02:00 still resolved SGA
concept DOI `10.5281/zenodo.20410947` to version
`10.5281/zenodo.21435547`, 33 files / 73,450,481 bytes. No draft, mutation,
or duplicate was created.
