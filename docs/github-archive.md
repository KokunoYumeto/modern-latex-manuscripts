# GitHub Archive History

This page is the GitHub-only audit trail for the task-maintained catalogs. It
does not describe, query, or certify any external record. Use it to see which
catalog generation was committed, which receipt proved commit-pinned raw
readback, and where to start browsing without replaying old task transcripts.

## Start Here

| Need | Human landing | Exact machine evidence |
|---|---|---|
| Adopt or independently mirror a bounded work | [Adoption board](adopt.md) | [`manifests/adopt.json`](../manifests/adopt.json) |
| Find an author, work, or corpus | [Coverage-map index](github-maps.md) | [`maps-r6.json`](../manifests/github-custody/maps-r6.json) |
| Open a direct reader | [Reader-shelf index](../reader-pdfs/README.md) | [`20260808_readers_r5.json`](../manifests/github-custody/20260808_readers_r5.json) |
| Locate an exact tracked source | [Source-shelf index](../sources/README.md) | [`20260807_sources_r5.csv`](../manifests/github-custody/20260807_sources_r5.csv) and [summary](../manifests/github-custody/20260807_sources_r5.json) |
| Verify reader/source inventories against the current Git tree | [Reader shelf](../reader-pdfs/README.md) and [source shelf](../sources/README.md) | [`20260808_shelves_r9.json`](../manifests/github-custody/20260808_shelves_r9.json) |
| Understand the mixed classical shelf | [Classical shelf map](classical-map.md) | [`20260806_classical.json`](../manifests/github-custody/20260806_classical.json) |
| Audit the GitHub maintenance chain | This page | Current [frontier receipt](../manifests/published-github/frontier-r1.json) and [closure](../manifests/published-github/frontier-r1-close.json); [twenty-eight-cycle predecessor](../manifests/published-github/20260809_queue_scope_close.json) |
| Interpret manifests and readback receipts | [Custody evidence](../manifests/github-custody/README.md) | [Raw-readback receipts](../manifests/published-github/README.md) |

## Published GitHub Cycles

| Cycle | Coverage | Source commit | Raw-readback receipt |
|---|---|---|---|
| Classical shelf | 832 files / 216,679,649 bytes; exactly Cayley, Dedekind, and Dirichlet | [`621f903e`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/621f903e79f47117ac6dc2e6bca3a61ee5aa225b) | [`cff2dca2`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/cff2dca2b6bbb628a1e403ced1f930bcad88f407), [receipt](../manifests/published-github/20260806_classical_readback.json) |
| Coverage maps | 19 allowed map documents, 601 resolved map links, and 20 explicitly bound manifests | [`ca54370b`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/ca54370b0b348932facfed2e431ea178b3348be7) | [`bc86c1d2`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/bc86c1d2962b918c0abeb678993aa0e20860b13f), [receipt](../manifests/published-github/20260806_maps_readback.json) |
| Reader shelves | 14 roots, 399 PDFs, three support files / 932,575,366 bytes | [`fe01135c`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/fe01135c0c5bdaf6805efc030c4146e8fe9d6f54) | [receipt](../manifests/published-github/20260808_readers_r5_rb.json) |
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
| Noether Simplified Chinese R3 | Exact sealed 444-file, 43-paper source checkpoint plus direct 413-page reader; current 400-file reader inventory, 12,968-file source inventory, shelf closure, and map audit | [`bbe8a929`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/bbe8a929bb70dd36f968ee654743cbf0b36794ec) | [`e396ebdb`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/e396ebdbdff24f3238481ba662e8c7d193aee97b), [receipt](../manifests/published-github/20260807_zh_rb.json) |
| Noether Simplified Chinese R4 | Exact sealed 1,433-file source checkpoint plus direct 424-page reader; current 401-file reader inventory, 14,401-file source inventory, 19-map audit, and current-tree shelf closure | [`997fca68`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/997fca686443ff742a65c360e7ab0438c90d562e) | [`fbc287c8`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/fbc287c86305dbef401f7682ed2bb7c8819e15f9), [five-commit receipt](../manifests/published-github/20260807_r4_rb.json) |
| Noether Simplified Chinese R4 ED0008 compatibility | Four sealed evidence files proving the existing R4 reader already realizes accepted ED0008 Post44 readings; no Chinese or reader byte changed, no later-day credit earned; current source inventory 14,405 files | [`27cbaef5`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/27cbaef5bc5601ec95ee0ec648ed7e2d5bdce04a) | [`6563e5fc`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/6563e5fc18e3d0eb32c50fa3fc4a4e0c2e52586d), [three-commit receipt](../manifests/published-github/20260807_a4_rb.json) |
| Noether Simplified Chinese R5 pending review | Exact frozen 496-file source checkpoint plus direct 424-page pending reader; current 402-file reader inventory, 14,901-file source inventory, 19-map audit, and current-tree shelf closure; R4 remains accepted/current | [`60895012`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/608950122c7d13595a43f9347fd2aa72f77684db) | [`bdf2a563`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/bdf2a56395006f483c6b0f2fd1dd3f2756be3ca9), [four-commit receipt](../manifests/published-github/20260807_r5_rb.json) |
| GitHub catalog, map, and link maintenance | Corrected current 14,901-file / 3,681,880,509-byte source totals; 19 maps / 195,453 bytes; 1,027/1,027 local links to 758 targets; producer bytes unchanged | [`57123827`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/57123827c0b4ee9c8a6f30788341a48915ad7473), [`94665b41`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/94665b4105d18922f69b4dbdf60e0c6e44c8d2ef), [`124b2b4d`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/124b2b4dd41ee9b5711e256f7118426d93131826), [`4d3a4f5a`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/4d3a4f5a7023f2b88a277e145bb04108c8e00dbc) | [`23c3f46a`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/23c3f46ab53be35bcdc8572f2e42b8dba38be6bf), [combined receipt](../manifests/published-github/20260808_maps_rb.json) |
| Current reader/source shelf closure | 14/14 reader-root and 19/19 source-root Git trees unchanged; 402 reader files / 932,575,366 bytes and 14,901 source files / 3,681,880,509 bytes preserved without blob reads; stable four-file shelf navigation binding | [`65619865`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/6561986595bddc74b4988bbf494ffa56900459b9) | [source receipt](../manifests/published-github/20260808_shelves_r7_rb.json), [publication closure](../manifests/published-github/20260808_shelves_r7_pub_rb.json) |
| Direct-reader navigation | Unchanged 14-root, 402-file reader inventory; current two-file navigation binding; 1,038/1,038 bounded local links to 762 targets | [`fe01135c`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/fe01135c0c5bdaf6805efc030c4146e8fe9d6f54) | [`85772e34`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/85772e342e56a2844aac5c9bf17a771d0ad42d8c), [receipt](../manifests/published-github/20260808_readers_r5_rb.json) |
| Mathematics Commons adoption layer | 66 exact rows: 8 current, 53 ready for adoption, and 5 future; the former Noether and Grothendieck-school umbrella IDs are retired as claim scopes and replaced by 22 map-backed language/work rows with explicit priority, readiness, coverage, cursor, and ownership; all 19 authoritative maps and both operational queues remain represented; exact-commit ingestion, no-lazy-fetch local reads, parallel mirrors, claims, and handbacks remain machine-contracted | [`5e3d60bd`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/5e3d60bdcef9678edea6a046ecd46765c00b8e3b), [`cb816b56`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/cb816b568e97734b8c27f086f0cf9beebdd602de), [`09cf5f7b`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/09cf5f7b4043985d03fccce0a4efcf87a4a2df47), [`511a78f8`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/511a78f8d008f044466a3dc041e3c6330d442f71), [`ce8dc207`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/ce8dc207e732530ec8fccc6d1d012ec415ef8ec4), [`0e12042d`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/0e12042dd211c4bde69b99707e99881c43b68d68), [`be322ec9`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/be322ec97455e18c87b6f73fd2028433bba3b9c9), [`2695dbfe`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/2695dbfe84726329267c71ba7a0af3486435f4c8), [`10d2df08`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/10d2df083bf0b47b758d5f094b6fcaeed9167011) | [board receipt](../manifests/published-github/20260809_adopt_rb.json), [contract receipt](../manifests/published-github/20260809_adopt_contract_rb.json), [map-synchronization receipt](../manifests/published-github/20260809_adopt_maps_rb.json), [work/snapshot receipt](../manifests/published-github/20260809_adopt_work_rb.json), [human-ID receipt](../manifests/published-github/20260809_adopt_ids_rb.json), [consumer receipt](../manifests/published-github/20260809_adopt_get_rb.json), [audit-output receipt](../manifests/published-github/20260809_adopt_audit_rb.json), [handback receipt](../manifests/published-github/20260809_handback_rb.json), [exact-scope receipt](../manifests/published-github/20260809_scope_rb.json) |
| Sparse adoption CI | Blobless metadata checkout; 135 tracked-path checks; exact four-file consumer; no-lazy-fetch promisor regression; valid and invalid claim lifecycle fixtures; no corpus build | [`ae59d85d`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/ae59d85d406d52448eacc0794916b34c8189a739) | [Actions run `31321920964`](https://github.com/KokunoYumeto/modern-latex-manuscripts/actions/runs/31321920964), [receipt](../manifests/published-github/20260809_adopt_ci_rb.json) |
| GitHub-only boundary and adoption certification default | External DOI links are discovery/provenance only; producer trees remain immutable; SGA/FAC/GAGA publication custody and Erdős projects remain outside scope; all 66 adoption rows inherit `no_certification_asserted` without changing the 22-field row contract | [`c97dd635`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/c97dd635325c50be69dd1695d8bd369ec68bbfa4) | [Actions run `31326362266`](https://github.com/KokunoYumeto/modern-latex-manuscripts/actions/runs/31326362266), [source receipt](../manifests/published-github/20260809_scope_cert_rb.json), [closure](../manifests/published-github/20260809_scope_cert_close.json) |
| Queue cursor and operational-scope synchronization | Replaces the obsolete EGA IV section-4 continuation with EGA I printed p.144 after sealed p.143; preserves independent named-range review of complete-as-represented EGA IV; makes the adoption board the operational queue and external publication language producer context only; all 66 item rows unchanged | [`66fabe75`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/66fabe75eec1114bf1d468f71cbbebb7321ee675) | [Actions run `31327925415`](https://github.com/KokunoYumeto/modern-latex-manuscripts/actions/runs/31327925415), [source receipt](../manifests/published-github/20260809_queue_scope_rb.json), [closure](../manifests/published-github/20260809_queue_scope_close.json) |
| Archive pointer and Weber frontier reconciliation | Fronts the current archive evidence; requires binding the snapshotted public Weber Volume II German/English bytes through §176 to the GitHub custody surface through §143 before continuation; explicitly forbids redoing §§144–176 and sets the later source cursor to p.643; no producer or corpus byte changed | [`b525560c`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/b525560c8881a3611b9c9b224de672eaf93631e1) | [Actions run `31329353277`](https://github.com/KokunoYumeto/modern-latex-manuscripts/actions/runs/31329353277), [10-path source receipt](../manifests/published-github/frontier-r1.json), [30-cycle closure](../manifests/published-github/frontier-r1-close.json) |

The current [frontier closure](../manifests/published-github/frontier-r1-close.json)
binds 30 commit-pinned readback cycles, 3,057 observations, and 1,209,798,692
bytes with zero mismatches. It also binds the clean exact-commit consumer,
missing-promisor regression, claim fixtures, and 39-document link audit.

The [twenty-six-cycle predecessor archive-history receipt](../manifests/published-github/20260808_archive_r9_rb.json)
replays all five files in its publication commit: 291,841 bytes, all matched.
The [adoption-layer receipt](../manifests/published-github/20260809_adopt_rb.json)
replays all nine files in its source commit: 257,262 bytes, all matched. It is
an operational supplement; it does not replace the archive manifests or maps.
The [adoption-contract receipt](../manifests/published-github/20260809_adopt_contract_rb.json)
then replays all eight schema, validator, validation, navigation, and locked-log
files in its source commit: 359,729 bytes, all matched.
The [adoption map-synchronization receipt](../manifests/published-github/20260809_adopt_maps_rb.json)
replays all eight files in its source commit: 385,658 bytes, all matched. Its
validation binds 30 operational rows, 19/19 authoritative maps, and 79/79
tracked repository paths.
The [work-level adoption and snapshot-policy receipt](../manifests/published-github/20260809_adopt_work_rb.json)
replays all nine files in its source commit: 546,693 bytes, all matched. Its
validation binds 46 operational rows, 19/19 authoritative maps, 2/2 queue
sources, and 119/119 tracked repository paths. Consumers must human-approve
one exact commit and fetch the board, schema, validation, and map manifest from
that same revision; floating `main` is not an immutable snapshot.
The [human Board-ID receipt](../manifests/published-github/20260809_adopt_ids_rb.json)
replays all eight source-commit files: 487,621 bytes, all matched. It binds
46/46 human IDs to the 46 JSON items with missing0, unknown0, and duplicates0.
The [exact-commit consumer receipt](../manifests/published-github/20260809_adopt_get_rb.json)
replays all ten source-commit files: 576,112 bytes, all matched. The public
helper fetched the board, schema, validation, and referenced map manifest from
that one approved commit: four files / 95,021 bytes, schema errors0,
validation errors0, and mixed revisions0. Floating `main` and a mismatched
approval hash both fail closed.
The [non-mutating audit receipt](../manifests/published-github/20260809_adopt_audit_rb.json)
replays all five source-commit files: 376,836 bytes, all matched. The validator
now keeps the canonical `ValidationPath` separate from a caller-selected
`OutputPath`; absolute temporary output passes without changing the tracked
validation, while a false canonical path still fails.
The [handback-interface receipt](../manifests/published-github/20260809_handback_rb.json)
replays all thirteen source-commit files: 599,475 bytes, all matched. Claims
declare a bounded start; handbacks separately require achieved scope, exact
result and manifest identities, checks/failures/reversals, continuation cursor,
and reusable method findings.
The [workflow-label receipt](../manifests/published-github/20260809_labels_rb.json)
replays all six files in source commit
[`075c38f2`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/075c38f2cf60b9d935469093b395623dd40f3ffa):
516,329 bytes, all matched. Its anonymous GitHub API replay confirms all four
tracked labels and all six issue-template bindings; no issue was created or
edited.
The [claim-auditor receipt](../manifests/published-github/20260809_claims_rb.json)
preserves rejected source snapshot `9516fc91`, then replays all nine corrected
paths in
[`b79d5f12`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/b79d5f12036f31438b385c7b8307c88e2195fe57):
611,875 bytes, all matched. The exact-commit consumer, anonymous live issue
audit, valid linked handback fixture, and malformed fail-closed fixture all
behave as declared without changing any issue.
The [reusable-workflow receipt](../manifests/published-github/20260809_flows_rb.json)
then approves
[`0fff8d0f`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/0fff8d0fc06af508536aad623cc5e8b513512624):
eleven changed paths / 658,277 public bytes all match, and the exact-commit
consumer passes four files / 116,120 bytes. The board embeds all fourteen
workflow definitions, every token is used, and `docs/adopt.md` plus the
14-heading workflow guide remain human guidance rather than additional
machine-ingestion identities.
The [ownership-semantics receipt](../manifests/published-github/20260809_owners_rb.json)
then approves
[`3b3880f3`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/3b3880f35467d813dc6f83c55c4ed09a48a3dcaa):
eight changed paths / 645,231 bytes all match and the four-file consumer passes
118,267 bytes. The existing board facts remain three named current rows and 43
deliberately unclaimed ready/future rows; null is now contractually unclaimed,
not unknown, and parallel claims remain nonexclusive.
The [complete adoption-index receipt](../manifests/published-github/20260809_index_rb.json)
then approves
[`36e41b52`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/36e41b5213719194ab43232979c20c82046770f0):
eleven changed paths / 679,826 bytes all match and the four-file consumer
passes 118,886 bytes. Its exact 46-row human projection exposes 38 authors, 46
works, 16 named series, 16 languages, and 21 corpora while remaining derived
presentation guidance rather than a separate archive or machine contract.
The [queue-synchronization receipt](../manifests/published-github/20260809_queue_rb.json)
then approves
[`3893682f`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/3893682f02342fe2a19f4913fcf5bebdb91327fb):
all eight changed paths / 664,933 bytes match, and the four-file consumer passes
120,188 bytes. The board now binds the exact 93,584-byte known-gaps/work-queue
snapshot, so either source advancing without board review is a validation
failure. The receipt also records the exact `af0918` -> `0e12042` interface
history, commit roles, helper limits, and why `docs/adopt.md` remains human
guidance rather than a fifth machine-contract identity.
The [offline-consumer receipt](../manifests/published-github/20260809_offline_rb.json)
then approves
[`86db3448`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/86db3448b3315c48542f02cddba279ba9c60c5f1):
all nine changed paths / 691,738 bytes match. Online raw GitHub and an offline
checkout-root object database return byte-identical four-file contracts /
120,622 bytes; unknown commits and linked-worktree `.git` indirection files
fail closed. Offline mode reads committed blobs and ignores dirty working-tree
bytes without creating a fifth contract identity.
The [offline-claim-auditor receipt](../manifests/published-github/20260809_claims_offline_rb.json)
then approves
[`24fe25af`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/24fe25af7e593dee03280c46cf941ec6d83a4f84):
all eleven changed paths / 732,365 public bytes match. The claim auditor now
combines raw-GitHub or exact local-Git board transport with public-API or JSON
fixture issue transport. A paired claim/handback fixture passes with dead
network proxies, while unknown Board IDs and commits fail closed. The consumer
sets `GIT_NO_LAZY_FETCH=1`; an unreachable-promisor regression proves a missing
blob causes no remote attempt and a fully materialized four-file contract /
122,057 bytes passes.
The [sparse continuous-validation receipt](../manifests/published-github/20260809_adopt_ci_rb.json)
then approves
[`ae59d85d`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/ae59d85d406d52448eacc0794916b34c8189a739):
all ten changed paths / 734,367 public bytes match, both refs resolve to the
source, and Actions run
[`31321920964`](https://github.com/KokunoYumeto/modern-latex-manuscripts/actions/runs/31321920964)
passes all eleven setup, validation, regression, and cleanup steps. The exact
tree's local sparse replay materialized 105 metadata files / 3,153,851 bytes,
validated 135/135 tracked paths, and read four contract files / 124,468 bytes;
missing promisor blobs and unknown Board IDs fail closed.
The no-lazy-fetch fix itself first shipped in corrective commit
[`24fe25af`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/24fe25af7e593dee03280c46cf941ec6d83a4f84),
after the `7f791dfb` snapshot: its [public correction receipt](../manifests/published-github/20260809_claims_offline_rb.json)
records 11/11 raw files matched, and the current workflow continuously replays
the missing-promisor case.
The [exact-scope receipt](../manifests/published-github/20260809_scope_rb.json)
then approves
[`10d2df08`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/10d2df083bf0b47b758d5f094b6fcaeed9167011):
all seven changed paths / 661,932 public bytes match, Actions run
[`31324190709`](https://github.com/KokunoYumeto/modern-latex-manuscripts/actions/runs/31324190709)
passes the exact-commit consumer, no-lazy-fetch, and claim-lifecycle gates,
and the board validates 66 rows against 214/214 tracked paths. The two retired
umbrella IDs are no longer claimable; sixteen Noether language/work rows and
six Grothendieck-school work rows expose exact state, ownership, coverage, and
cursor instead. The 66-row human index projects those operational fields in
ordinal order. No producer or corpus artifact changed.
The [GitHub-boundary and certification receipt](../manifests/published-github/20260809_scope_cert_rb.json)
then approves
[`c97dd635`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/c97dd635325c50be69dd1695d8bd369ec68bbfa4):
all thirteen changed paths / 872,154 public bytes match, both maintained refs
point to that commit, and Actions run
[`31326362266`](https://github.com/KokunoYumeto/modern-latex-manuscripts/actions/runs/31326362266)
passes. The board and schema require the top-level
`item_certification_default: no_certification_asserted`; the validator reports
all 66 rows inheriting it and rejects missing, different, or ad hoc row-level
values. Current navigation now binds 14,901 source paths, 399 reader PDFs plus
three support files, 643/643 map-local links, and the prior 26-cycle receipt
aggregate. External record history remains discoverable without assigning this
task Zenodo custody. No producer or corpus artifact changed.
The [scope-and-certification closure](../manifests/published-github/20260809_scope_cert_close.json)
then verifies the public receipt commit
[`01747f5a`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/01747f5ab281cf0070a8d35783a03ca743d17983):
all six changed paths / 511,647 bytes match commit-pinned raw GitHub bytes,
both maintained refs point to the commit, Actions run
[`31326852595`](https://github.com/KokunoYumeto/modern-latex-manuscripts/actions/runs/31326852595)
passes, and the promisor regression again proves a missing blob exits without
contacting the configured remote. A fully materialized four-file contract
replays 156,610 bytes with lazy fetching disabled. No producer or corpus
artifact changed.
The [queue-and-scope receipt](../manifests/published-github/20260809_queue_scope_rb.json)
approves
[`66fabe75`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/66fabe75eec1114bf1d468f71cbbebb7321ee675):
all eleven changed paths / 863,654 bytes match commit-pinned raw GitHub bytes,
both maintained refs point to the commit, and Actions run
[`31327925415`](https://github.com/KokunoYumeto/modern-latex-manuscripts/actions/runs/31327925415)
passes. The exact 66 adoption rows are unchanged; the two-source queue snapshot
now binds 94,063 bytes, and the live adoption issue audit finds zero claims or
handbacks. The controlled 39-document link audit resolves 1,225 local links to
806 targets with zero missing or prohibited targets. No producer or corpus
artifact changed.
The [queue-and-scope closure](../manifests/published-github/20260809_queue_scope_close.json)
then verifies the public receipt commit
[`19352e28`](https://github.com/KokunoYumeto/modern-latex-manuscripts/commit/19352e285ca86431898772c121d28cc53ec4a703):
all six changed paths / 524,243 bytes match commit-pinned raw GitHub bytes,
both maintained refs point to the commit, Actions run
[`31328203806`](https://github.com/KokunoYumeto/modern-latex-manuscripts/actions/runs/31328203806)
passes, and the four-file contract replays 156,610 bytes with lazy fetching
disabled. The 28-cycle aggregate through that receipt is 3,041 observations /
1,208,486,039 bytes with zero mismatches. No producer or corpus artifact
changed.
The [complete archive-r9 cycle receipt](../manifests/published-github/20260808_archive_r9_cycle_rb.json)
replays the final versions of all ten paths changed after `7e56161f`:
343,102 bytes, all matched.
The [archive-r8 predecessor receipt](../manifests/published-github/20260808_archive_r8_rb.json)
replays its five publication files / 297,201 bytes, all matched.
The [archive-r8 shelf-and-link closure](../manifests/published-github/20260808_archive_r8_close_rb.json)
replays all eight paths in its remote commit: 328,925 bytes, all matched.
The [twenty-five-cycle predecessor archive-history receipt](../manifests/published-github/20260808_archive_r7_rb.json)
replays all five files in its publication commit: 278,384 bytes, all matched.
The [twenty-three-cycle archive-history predecessor receipt](../manifests/published-github/20260808_archive_r6_rb.json)
replays all five files in its publication commit: 252,007 bytes, all matched.
The [current shelf-closure receipt](../manifests/published-github/20260808_shelves_r7_rb.json)
replays its five publication files / 289,863 bytes, all matched, while proving
14/14 reader-root and 19/19 source-root Git tree equality.
The [current direct-reader receipt](../manifests/published-github/20260808_readers_r5_rb.json)
replays its six publication files / 267,277 bytes, all matched, while preserving
the exact 402-file reader inventory under 14/14 root-tree equality.

These scopes overlap and must not be treated as unique-file totals: the
classical files are a deeply classified subset of the reader and source
shelves, while later maintenance cycles repeatedly read back evolving catalog,
log, and navigation paths. Across all twenty-eight cycles through the public
queue-and-scope receipt commit, the receipts preserve 3,041 additive
raw-readback observations / 1,208,486,039 bytes with zero mismatches.

The 151 source/correction/receipt commits form one direct-parent,
fast-forward-only chain from
`621f903e79f47117ac6dc2e6bca3a61ee5aa225b` through
`7e56161ffa25b8346e6ad42c4e689ca90033991b`. No pull request or merge commit
was used for these twenty-six cycles. The exact generation-specific file identities
and chain are in
[`20260808_archive_r9.json`](../manifests/github-custody/20260808_archive_r9.json).
The [archive-r8 predecessor](../manifests/github-custody/20260808_archive_r8.json),
[twenty-three-cycle predecessor](../manifests/github-custody/20260808_archive_r6.json),
[twenty-two-cycle predecessor](../manifests/github-custody/20260807_archive_r5.json),
[twenty-one-cycle predecessor](../manifests/github-custody/20260807_archive_r4.json),
[twenty-cycle predecessor](../manifests/github-custody/20260807_archive_r3.json),
[nineteen-cycle predecessor](../manifests/github-custody/20260807_archive_r2.json),
[eighteen-cycle predecessor](../manifests/github-custody/20260807_archive.json),
the [fifteen-cycle r4 predecessor](../manifests/github-custody/20260806_archive_r4.json),
the [twelve-cycle r3 predecessor](../manifests/github-custody/20260806_archive_r3.json),
[eight-cycle r2 predecessor](../manifests/github-custody/20260806_archive_r2.json),
and [four-cycle predecessor](../manifests/github-custody/20260806_archive.json)
remain unchanged as historical evidence.

## Link Integrity

The exact-scope source commit's bounded link audit is recorded in
`manifests/published-github/20260809_scope_rb.json`. It covers 39 committed
documents: the nineteen allowed maps; the GitHub-only map, archive, reader,
source, custody, and receipt landings; the human adoption board and workflow
guide; the complete dimension index; and seven contributor/issue entry points.
It resolves 1,213 local links to 802 unique targets with zero missing or
prohibited targets. The sparse-CI, offline-claim-auditor, offline-consumer,
queue-synchronization, complete-index,
ownership, reusable-workflow, and claim-auditor audits remain immutable
predecessors `20260809_links_r28.json`, `20260809_links_r27.json`, `20260809_links_r26.json`, `20260809_links_r25.json`, `20260809_links_r24.json`,
`20260809_links_r23.json`, `20260809_links_r22.json`, and
`20260809_links_r21.json`.
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

The index names only the twenty-eight exact GitHub-maintenance cycles above. It does not
enumerate unrelated receipt directories or separately owned, revoked, or
prohibited corpus surfaces. Cataloging preserves distinct paths and generations;
it does not silently deduplicate, rewrite, promote, or certify producer work.
