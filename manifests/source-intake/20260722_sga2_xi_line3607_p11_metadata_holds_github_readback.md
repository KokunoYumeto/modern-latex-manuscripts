# SGA2 Expose XI line 3607 and Proposition 1.1 holds: GitHub readback

Pull request [#58](https://github.com/KokunoYumeto/modern-latex-manuscripts/pull/58)
merged the two metadata-only custody holds at public `main` commit
`93355464e84c8b1a37ce651fbbbe2475c53da6c8` from source commit
`b8586a5e8213088c16a9c5d9e086639801593e5e`.

A fresh sparse clone of the public repository resolved exactly to the merge
commit with a clean worktree. All nine changed Git blobs matched the source
commit exactly. The public archive logbook blob has SHA-256
`23E70786A4E6DF7864505B9CF29C83E307A31124E104FD9815630FE792DEFA23`
and parses as 90 records with 90 unique decision IDs, ending at
`AML-20260722-SGA-078`.

The merged diff contains four sanitized Markdown/JSON hold receipts and five
status/logbook paths. It contains no line-3607 or Proposition XI.1.1 TeX, PDF,
authority slice, CSV/JSONL evidence body, build log, ZIP, extracted text,
target render, source-page raster, or machine panel. Public source-bearing
coverage therefore remains through corrected French line 3574.

The 693 added lines contain zero private-path, thread-ID, or agent-name hits.
The official API recheck at `2026-07-22T05:52:51.2429914+02:00` still
resolved SGA concept DOI `10.5281/zenodo.20410947` to published version
`10.5281/zenodo.21435547`, 33 files / 73,450,481 bytes, updated
`2026-07-19T02:40:42.287682+02:00`. No draft, mutation, deposition, or
duplicate was created.
