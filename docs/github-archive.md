# GitHub Archive History

This page is the GitHub-only audit trail for the task-maintained catalogs. It
does not describe, query, or certify any external record. Use it to see which
catalog generation was committed, which receipt proved commit-pinned raw
readback, and where to start browsing without replaying old task transcripts.

## Start Here

| Need | Human landing | Exact machine evidence |
|---|---|---|
| Find an author, work, or corpus | [Coverage-map index](github-maps.md) | [`20260807_maps.json`](../manifests/github-custody/20260807_maps.json) |
| Open a direct reader | [Reader-shelf index](../reader-pdfs/README.md) | [`20260807_readers.json`](../manifests/github-custody/20260807_readers.json) |
| Locate an exact tracked source | [Source-shelf index](../sources/README.md) | [`20260807_sources.csv`](../manifests/github-custody/20260807_sources.csv) and [summary](../manifests/github-custody/20260807_sources.json) |
| Verify reader/source inventories against the current Git tree | [Reader shelf](../reader-pdfs/README.md) and [source shelf](../sources/README.md) | [`20260807_shelves.json`](../manifests/github-custody/20260807_shelves.json) |
| Understand the mixed classical shelf | [Classical shelf map](classical-map.md) | [`20260806_classical.json`](../manifests/github-custody/20260806_classical.json) |
| Audit the GitHub maintenance chain | This page | [`20260807_archive.json`](../manifests/github-custody/20260807_archive.json) |
| Interpret manifests and readback receipts | [Custody evidence](../manifests/github-custody/README.md) | [Raw-readback receipts](../manifests/published-github/README.md) |

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
| Archive r2 publication | Eight-cycle archive successor and refreshed committed-blob link audit | [`9b040b86`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/9b040b864e8c277ea33c1a24292bd8ddf3bfed98), [`6f03f245`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/6f03f245017a05dbdadc289e3c0119017cbd3bdd) | [`870ee9a9`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/870ee9a96eb8edf3baff00e1f6f58bc8d58fc35b), [receipt](../manifests/published-github/20260806_archive_r2_readback.json) |
| Evidence landings | Human custody-manifest and raw-readback receipt landings plus their exact link audit | [`cbf3ec2f`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/cbf3ec2f2bf793318056d70d85683af812470704), [`7de0c19e`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/7de0c19e8fbfb38b7865340bf85263e298278ea4) | [`d36937ab`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/d36937ab53d3c65b218e73e3e9f01257073b4f87), [receipt](../manifests/published-github/20260806_evidence_readback.json) |
| Noether route closure | 121/121 tracked child trees routed; six previously detached support/history trees exposed; no source mutation; [manifest](../manifests/github-custody/20260806_noether_routes.json) | [`93b2239d`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/93b2239d40db244d19465c17b2ac2626935c4282), [`0e509253`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/0e509253aef5711a9450848561a3acd8ecee79d7), [`ffc5886c`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/ffc5886ccc76ea15be7d12e96310cc5ce79437c0) | [`fe9eafbf`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/fe9eafbfa4b8365590408a3d4e8345602724d8a8), [receipt](../manifests/published-github/20260806_noether_routes_readback.json) |
| Non-European source-only routes | All eight source-only translation files and the shared preamble directly linked; correction and live-main propagation history preserved; [manifest](../manifests/github-custody/20260806_non_european_map.json) | [`85466c47`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/85466c4761cdc306379441f5c62a05a8f6072f36), [`c11efa84`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/c11efa84e5ef975eb34f46647e46c1bcee1fe8ab), [`8be44498`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/8be444980cc212ca7223aaf78034e4ad1943509e), [`7edc3ae7`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/7edc3ae7bfff120e8834d00dbe1ac7b869ef9bbe), [`9fe96dde`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/9fe96dde25422f4ad631d90850170b16ac6150df) | [`70e84eb4`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/70e84eb498e6c520c1fc3b9fb36060d58e5a1cfb), [`72b413c2`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/72b413c2b55f3fc96416cb459de9a7aa271c4648), [`4660e0d7`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/4660e0d71f9785cc5cdb501e8907d3ae5a4a5199), [`6ccc2e52`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/6ccc2e527f0eb9258b3139ee59389b1f4572b872); [route](../manifests/published-github/20260806_non_euro_routes_rb.json), [closeout](../manifests/published-github/20260806_non_euro_close_rb.json), [audit](../manifests/published-github/20260806_non_euro_audit_rb.json), [live-main](../manifests/published-github/20260806_non_euro_live_rb.json) receipts |
| Archive r3 publication | Twelve-cycle archive successor, refreshed link audit, receipt landing, and closure | [`fa05368`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/fa05368a4bb4f101a9e122ef700d4ed33a979e7c), [`4554aea8`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/4554aea8b412104dad503e25fb0941da3cfcf5b6), [`dbf92d16`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/dbf92d164d37eedebbabe3275dc5036a0bb7163a) | [`764daadb`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/764daadb9b8da6ca341f314dcb06fa5de61aac3c), [`b20182b2`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/b20182b2ea93d0aaeac5202f21c3a8bcaa546702); [primary](../manifests/published-github/20260806_archive_r3_rb.json), [closure](../manifests/published-github/20260806_archive_r3_close.json) receipts |
| Coverage maps r2 | 19 current maps / 191,042 bytes, 619 resolved map links, 21 exact custody manifests | [`790c1dbb`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/790c1dbbf3976e642214e6e920f4fe662c108570), [`2b2f287b`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/2b2f287b1b4e8359011739616466064bd04c8260) | [`506f8e2d`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/506f8e2df6593b9a01c2275ea94feea08183163e), [receipt](../manifests/published-github/20260806_maps_r2_rb.json) |
| Reader/source shelf closure | 14/14 reader trees, 19/19 source trees, and 12,407/12,407 source metadata rows current | [`fafa41aa`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/fafa41aa6c29becb048aacc7cecf5f739f6dde86), [`938a1a75`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/938a1a7532808326cc582fbc7cf361649a1a8992) | [`ff5ab5d7`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/ff5ab5d73260439fb69065419e1465b10d6648c3), [receipt](../manifests/published-github/20260806_shelves_rb.json) |
| Noether Slavic v038 | Exact 116-file producer release plus handoff, four direct-reader mirrors, 399-reader and 12,524-source successor inventories, current-tree closure, and map audit | [`4af9d720`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/4af9d72039ac8d16697ff01971b651f968a73e32) | [`c23f5d33`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/c23f5d33bc6c005edd167732c8a7015fcb08b6b3), [`601e97e4`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/601e97e430352cf12545178aa45aea88a98d9ce5), [`34aa4159`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/34aa4159d50f6c9124e22afc9b6685ee6977de50); [source](../manifests/published-github/20260807_slavic_rb.json), [catalog](../manifests/published-github/20260807_slavic_cat_rb.json), [shelf](../manifests/published-github/20260807_slavic_close_rb.json), and [audit](../manifests/published-github/20260807_slavic_audit_rb.json) receipts |

These scopes overlap and must not be treated as unique-file totals: the
classical files are a deeply classified subset of the reader and source
shelves, while later maintenance cycles repeatedly read back evolving catalog,
log, and navigation paths. Across all eighteen cycles, the receipts preserve
304 additive raw-readback observations / 82,530,145 bytes with zero mismatches.

The sixty-six source/correction/receipt commits form one direct-parent,
fast-forward-only chain from
`621f903e79f47117ac6dc2e6bca3a61ee5aa225b` through
`dc30c7c1497642d6599d99b104e1f57fd2163270`. No pull request or merge commit
was used for these eighteen cycles. The exact generation-specific file identities
and chain are in
[`20260807_archive.json`](../manifests/github-custody/20260807_archive.json).
The [fifteen-cycle r4 predecessor](../manifests/github-custody/20260806_archive_r4.json),
The [twelve-cycle r3 predecessor](../manifests/github-custody/20260806_archive_r3.json),
[eight-cycle r2 predecessor](../manifests/github-custody/20260806_archive_r2.json),
and [four-cycle predecessor](../manifests/github-custody/20260806_archive.json)
remain unchanged as historical evidence.

## Link Integrity

The bounded [local-link audit](../manifests/github-custody/20260806_links.json)
covers the nineteen allowed maps and the GitHub-only map, archive, reader,
source, custody, and receipt landings, plus the six contributor/issue entry
points.
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

The index names only the eighteen exact GitHub-maintenance cycles above. It does not
enumerate unrelated receipt directories or separately owned, revoked, or
prohibited corpus surfaces. Cataloging preserves distinct paths and generations;
it does not silently deduplicate, rewrite, promote, or certify producer work.
