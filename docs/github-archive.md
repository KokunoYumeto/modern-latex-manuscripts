# GitHub Archive History

This page is the GitHub-only audit trail for the task-maintained catalogs. It
does not describe, query, or certify any external record. Use it to see which
catalog generation was committed, which receipt proved commit-pinned raw
readback, and where to start browsing without replaying old task transcripts.

## Start Here

| Need | Human landing | Exact machine evidence |
|---|---|---|
| Find an author, work, or corpus | [Coverage-map index](github-maps.md) | [`20260806_maps.json`](../manifests/github-custody/20260806_maps.json) |
| Open a direct reader | [Reader-shelf index](../reader-pdfs/README.md) | [`20260806_readers.json`](../manifests/github-custody/20260806_readers.json) |
| Locate an exact tracked source | [Source-shelf index](../sources/README.md) | [`20260806_sources.csv`](../manifests/github-custody/20260806_sources.csv) and [summary](../manifests/github-custody/20260806_sources.json) |
| Understand the mixed classical shelf | [Classical shelf map](classical-map.md) | [`20260806_classical.json`](../manifests/github-custody/20260806_classical.json) |
| Audit the GitHub maintenance chain | This page | [`20260806_archive_r2.json`](../manifests/github-custody/20260806_archive_r2.json) |

## Published GitHub Cycles

| Cycle | Coverage | Source commit | Raw-readback receipt |
|---|---|---|---|
| Classical shelf | 832 files / 216,679,649 bytes; exactly Cayley, Dedekind, and Dirichlet | [`621f903e`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/621f903e79f47117ac6dc2e6bca3a61ee5aa225b) | [`cff2dca2`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/cff2dca2b6bbb628a1e403ced1f930bcad88f407), [receipt](../manifests/published-github/20260806_classical_readback.json) |
| Coverage maps | 19 allowed map documents, 601 resolved map links, and 20 explicitly bound manifests | [`ca54370b`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/ca54370b0b348932facfed2e431ea178b3348be7) | [`bc86c1d2`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/bc86c1d2962b918c0abeb678993aa0e20860b13f), [receipt](../manifests/published-github/20260806_maps_readback.json) |
| Reader shelves | 14 roots, 392 PDFs, three support files / 911,980,954 bytes | [`742a49b0`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/742a49b0eb1272471a9ee4a4c8245f69a5ec9fec) | [`0a7577e4`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/0a7577e4716d100113f2e7e0d9014e0d68041216), [receipt](../manifests/published-github/20260806_readers_readback.json) |
| Source shelves | 19 roots, 12,407 tracked paths / 2,546,045,982 committed bytes | [`59d3463e`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/59d3463eb62312607f6faa37886d54a71e72f4b5) | [`ca518f55`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/ca518f554e7070addb2e5d3be2de660c4d6d87f7), [receipt](../manifests/published-github/20260806_sources_readback.json) |
| Archive history | Four-cycle GitHub history, navigation, and exact manifest/receipt binding | [`a5365f6e`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/a5365f6e22f7a6440319dc3016629d07f44081ea) | [`eaecfc6b`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/eaecfc6b7fd7f7476df08e767c26eabf7f2ddcd2), [receipt](../manifests/published-github/20260806_archive_readback.json) |
| Maintenance log | Seven-record initial locked log, deterministic replay helper, and preserved error/correction history | [`21f797ba`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/21f797ba43e0171978dd366d7e120711e477e2d0) | [`b184bc9a`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/b184bc9a14b30b8a2c5d58170d489b986ed99828), [receipt](../manifests/published-github/20260806_log_readback.json) |
| Local-link audit | 23 bounded documents, 715 resolved links, 627 unique targets, external requests zero | [`1b8e16e2`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/1b8e16e28718eb6ab9da5b5c11827ed6d9b26070) | [`b435c7b2`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/b435c7b2519ad14c50f7f89c662a640d9387a452), [receipt](../manifests/published-github/20260806_links_readback.json) |
| Contributor intake | GitHub-first issue/PR routing, canonical path correction, committed-blob audit, 29 documents and 725 resolved links | [`f4bcc505`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/f4bcc505077eb0dd8512a94f9f4b6a5af51ea181), [`3d3ae0c4`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/3d3ae0c439a13f335a18ed95e2d8fac62b1fd4b3), [`0e9a4c7b`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/0e9a4c7bdf2e949f3d58d05098d6d4d267847077) | [`8505d05c`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/8505d05c9aa43c35835338ace573c4b9b25f1e6e), [receipt](../manifests/published-github/20260806_contrib_readback.json) |

These scopes overlap and must not be treated as unique-file totals: the
classical files are a deeply classified subset of the reader and source
shelves, while later maintenance cycles repeatedly read back evolving catalog,
log, and navigation paths. Across all eight cycles, the receipts preserve 54
additive raw-readback observations / 3,263,525 bytes with zero mismatches.

The eighteen source/correction/receipt commits form one direct-parent,
fast-forward-only chain from
`621f903e79f47117ac6dc2e6bca3a61ee5aa225b` through
`8505d05c9aa43c35835338ace573c4b9b25f1e6e`. No pull request or merge commit
was used for these eight cycles. The exact generation-specific file identities
and chain are in
[`20260806_archive_r2.json`](../manifests/github-custody/20260806_archive_r2.json).
The [four-cycle predecessor](../manifests/github-custody/20260806_archive.json)
remains unchanged as historical evidence.

## Link Integrity

The bounded [local-link audit](../manifests/github-custody/20260806_links.json)
covers the nineteen allowed maps and the GitHub-only map, archive, reader, and
source landings, plus the six contributor/issue entry points.
[`check-links.ps1`](../scripts/check-links.ps1) resolves local targets only; it
counts external URLs without requesting them and stops before touching a
prohibited local target.

## Maintenance Decisions And Errors

The append-only [maintenance log](../manifests/github-custody/log.jsonl)
preserves controls, decisions, stopped attempts, and their corrections. Every
record binds the previous record by SHA-256. The
[log manifest](../manifests/github-custody/20260806_log.json) records the exact
chain identity and supersession edges; [`add-log.ps1`](../scripts/add-log.ps1)
replays the complete chain under an exclusive lock before appending one record.
Corrections supersede failed methods without deleting their error history.

## Boundary

The index names only the eight exact GitHub-maintenance cycles above. It does not
enumerate unrelated receipt directories or separately owned, revoked, or
prohibited corpus surfaces. Cataloging preserves distinct paths and generations;
it does not silently deduplicate, rewrite, promote, or certify producer work.
