# GitHub raw-readback receipts

Each file in this directory is a generation-specific receipt for bytes already
pushed to GitHub. A receipt binds its source commit and remote ref to exact
paths, byte counts, hashes, and mismatch results. It proves the recorded GitHub
transport; it does not invent mathematical review, source fidelity, rights, or
completion beyond the underlying checkpoint.

Start with the current [archive-history receipt](20260808_archive_r9_rb.json),
the [twenty-six-cycle manifest](../github-custody/20260808_archive_r9.json),
the [human archive history](../../docs/github-archive.md), and the
[custody-index landing](../github-custody/README.md).

The [Mathematics Commons adoption-layer receipt](20260809_adopt_rb.json)
replays all nine files in source commit `5e3d60bdcef9678edea6a046ecd46765c00b8e3b`:
257,262 bytes, all matched exactly. The corresponding JSON board is an
operational coordination layer; the coverage maps and source/reader manifests
remain the authoritative archive layer.

The [adoption-contract receipt](20260809_adopt_contract_rb.json) replays all
eight files in source commit `cb816b568e97734b8c27f086f0cf9beebdd602de`:
359,729 bytes, all matched exactly. It binds the Draft 2020-12 schema, bounded
validator, post-push validation, explicit mirror-row contract, navigation, and
locked maintenance history.

The [adoption map-synchronization receipt](20260809_adopt_maps_rb.json)
replays all eight files in source commit
`09cf5f7b4043985d03fccce0a4efcf87a4a2df47`: 385,658 bytes, all matched
exactly. The operational feed now has 30 rows (3 current, 23 adoption-ready,
4 future), represents all 19 authoritative coverage maps, and retains zero
integrated mirror claims until an inspectable mirror is actually returned.

The [work-level adoption and snapshot-policy receipt](20260809_adopt_work_rb.json)
replays all nine files in source commit
`511a78f8d008f044466a3dc041e3c6330d442f71`: 546,693 bytes, all matched
exactly. The successor exposes 46 rows (3 current, 38 adoption-ready, 5
future), binds both operational queue sources and all 19 maps, and requires a
human-approved exact commit for ingestion. Floating `main` is only a locator;
board, schema, validation, and map manifest must come from one revision.

The [human Board-ID receipt](20260809_adopt_ids_rb.json) replays all eight
files in source commit `ce8dc207e732530ec8fccc6d1d012ec415ef8ec4`:
487,621 bytes, all matched exactly. All 46 JSON item IDs now appear exactly
once in the human board, and the bounded validator rejects missing, unknown,
or duplicate human rows.

The current [catalog/map/link maintenance receipt](20260808_maps_rb.json)
binds eight additive path observations across three commits / 456,987 bytes,
all matched exactly. Its final link control records 34 documents, 1,027/1,027
local links, and 758 targets. The predecessor
[navigation-link closure receipt](20260808_links_rb.json) binds the
34-document, 1,024-local-link committed-blob audit: five paths / 223,303
bytes, all matched exactly. The
[R5 archive-navigation receipt](20260807_links_r4_rb.json) remains immutable
predecessor evidence: seven paths / 223,835 bytes, all matched exactly.
The [R5 receipt-publication closure](20260807_r5_close_rb.json) then replays
the four navigation-receipt publication paths / 193,908 bytes, all matched
exactly.

The current [live-main receipt](20260807_main_r5_rb.json) independently replays
the Simplified-Chinese Noether R5 pending reader/source seal, current catalogs,
archive controls, locked log, and receipts from `main`: 33 paths / 8,771,204
bytes, all matched exactly. The [R3 live-main receipt](20260807_main_rb.json)
remains immutable predecessor evidence.

The current [reader/source shelf-closure receipt](20260808_shelves_r7_rb.json)
replays all five paths in the metadata-only successor commit: 289,863 bytes,
all matched exactly. It proves 14/14 allowed reader-root and 19/19 allowed
source-root Git tree equality while binding the current direct-reader inventory
and five task-owned navigation identities; reader/source blob content was not
read or changed. The [r6 receipt](20260808_shelves_r6_rb.json) remains immutable
predecessor evidence.

The [r7 receipt-publication closure](20260808_shelves_r7_pub_rb.json) replays
the five receipt and landing paths in the next remote commit: 283,335 bytes,
all matched exactly.

The [archive-r8 receipt-publication closure](20260808_archive_r8_pub_rb.json)
replays the five receipt and landing paths in the next remote commit: 295,142
bytes, all matched exactly.

The [archive-r8 shelf-and-link closure](20260808_archive_r8_close_rb.json)
replays all eight paths in its remote commit: 328,925 bytes, all matched
exactly. It binds the stable four-file shelf navigation, link audit r8, locked
log, receipt-publication evidence, and both human landings.

The current [direct-reader inventory receipt](20260808_readers_r5_rb.json)
replays all six paths in the navigation-only reader successor publication:
267,277 bytes, all matched exactly. It preserves the exact 402-file /
932,575,366-byte reader inventory under 14/14 root-tree equality and binds the
current two-file GitHub navigation surface without reading or changing reader
blob content.

The [Noether Slavic v038 source receipt](20260807_slavic_rb.json) binds every
path changed by its source commit: 126 commit-pinned raw files / 73,170,246
bytes, all matched exactly.

The current [Noether Simplified-Chinese R4 source receipt](20260807_zh_r4_rb.json)
binds all 1,435 paths changed by the exact source/reader publication commit:
563,347,319 bytes, all matched exactly. Its three disjoint read-only agent
partitions and their independently checked union are recorded in the receipt.
The separate [R4 custody/index receipt](20260807_zh_r4_cat_rb.json) binds all
11 paths changed by the catalog commit: 1,436,126 bytes, all matched exactly.
The [R4 whole-shelf index receipt](20260807_r4_idx_rb.json) binds all nine
reader/source/map catalog paths and 2,558,492 bytes, all matched exactly.
The combined [R4 cycle receipt](20260807_r4_rb.json) binds all 1,465 additive
commit-pinned observations across five commits and 567,609,781 bytes, all
matched exactly. Repeated evolving catalog paths remain separate observations.
The [final R4 closure receipt](20260807_r4_close_rb.json) binds its last four
navigation-receipt paths / 143,789 bytes, all matched exactly.
The [R4 ED0008 compatibility receipt](20260807_zh_a4_rb.json) binds its four
sealed evidence files / 7,012 bytes, all matched exactly. It records no Chinese
byte change and no later-day certification credit.
The [Simplified-Chinese R5 pending-review source receipt](20260807_zh_r5_rb.json)
binds all 501 paths changed by its exact source/reader publication commit:
252,904,542 bytes, all matched exactly. R5 remains
`FROZEN_PENDING_INDEPENDENT_REVIEW`; this receipt proves transport, not
acceptance, publication readiness, or clean-day credit.
The separate [R5 custody/catalog receipt](20260807_zh_r5_cat_rb.json) binds all
ten custody, discoverability, locked-log, and source-receipt paths / 700,811
bytes, all matched exactly.
The [R5 reader-inventory receipt](20260807_zh_r5_reader_rb.json) binds all seven
catalog-receipt, reader-index, reader-landing, and locked-log paths / 202,988
bytes, all matched exactly.
The [R5 global-index receipt](20260807_zh_r5_idx_rb.json) binds all nine source,
map, reader, shelf, landing, log, and prior-receipt paths / 2,669,549 bytes,
all matched exactly. The combined [four-commit R5 receipt](20260807_r5_rb.json)
preserves 527 additive commit-pinned observations / 256,477,890 bytes with zero
mismatches. These transport receipts do not change R5's pending-review state.
The [R5 source-shelf catalog correction receipt](20260808_src_cat_rb.json)
binds the three corrected catalog/log paths / 199,943 bytes at commit
`94665b4105d18922f69b4dbdf60e0c6e44c8d2ef`, all matched exactly. It changes
catalog facts and links only; no producer or source byte changed.
The [front-door source-total correction receipt](20260808_front_rb.json) binds
the three front-door/log paths / 317,002 bytes at commit
`124b2b4dd41ee9b5711e256f7118426d93131826`, all matched exactly. It refreshes
the current source-shelf totals without rewriting historical cycle entries.
The separate [A4 custody/index receipt](20260807_zh_a4_cat_rb.json) binds all
nine catalog, landing, log, and source-receipt paths / 202,313 bytes, all
matched exactly.
The [A4 source/map/shelf receipt](20260807_zh_a4_idx_rb.json) binds all eleven
index paths / 2,606,440 bytes, all matched exactly. The combined
[three-commit A4 receipt](20260807_a4_rb.json) preserves 24 additive
observations / 2,815,765 bytes with zero mismatches.

The [Simplified-Chinese R3 cycle receipt](20260807_zh_rb.json) remains the
immutable predecessor receipt: 465 commit-pinned raw files / 269,957,244
bytes, all matched exactly.

The [v038 catalog receipt](20260807_slavic_cat_rb.json) binds the twelve
custody/index/log/landing paths added by the catalog commit: 2,426,184 bytes,
all matched exactly.

The [shelf-closure receipt](20260807_slavic_close_rb.json) binds seven paths /
96,574 bytes, and the [map/audit receipt](20260807_slavic_audit_rb.json) binds
five paths / 87,097 bytes. Both replays matched every byte.

The [landing receipt](20260807_slavic_land_rb.json), [final-link receipt](20260807_slavic_link_rb.json),
and [link-receipt closure](20260807_slavic_link_close.json) preserve the final
landing and audit chain; all thirteen recorded paths matched.

The [current twenty-six-cycle archive receipt](20260808_archive_r9_rb.json)
replays all five paths in the archive-r9 publication commit: 291,841 bytes,
all matched exactly. The [archive-r8 predecessor receipt](20260808_archive_r8_rb.json)
replays its five paths / 297,201 bytes, all matched exactly.

The [archive-r9 complete-cycle receipt](20260808_archive_r9_cycle_rb.json)
replays the final versions of all ten unique paths changed from `7e56161f`
through `4a71e535`: 343,102 bytes, all matched exactly.
The [twenty-five-cycle archive predecessor receipt](20260808_archive_r7_rb.json)
replays all five paths / 278,384 bytes, all matched exactly. The
[twenty-three-cycle archive predecessor receipt](20260808_archive_r6_rb.json)
replays all five paths / 252,007 bytes, all matched exactly. The
[twenty-two-cycle archive receipt](20260807_archive_r5_rb.json) replays all
eight paths in the current archive-history successor: 546,389 bytes, all
matched exactly. The [twenty-one-cycle predecessor receipt](20260807_archive_r4_rb.json)
remains immutable: nine paths / 209,016 bytes, all matched exactly. The
[twenty-cycle predecessor receipt](20260807_archive_r3_rb.json)
remains immutable: seven paths / 1,064,837 bytes, all matched exactly. The
[nineteen-cycle predecessor receipt](20260807_archive_r2_rb.json) also remains
immutable: three paths / 25,735 bytes, all matched exactly.

The twenty-cycle predecessor's [receipt-publication closure](20260807_archive_r3_close.json) replays four
paths / 139,662 bytes, all matched exactly.

The nineteen-cycle predecessor's [receipt-publication closure](20260807_archive_r2_close.json) replays four
paths / 95,433 bytes, all matched exactly.

The [eighteen-cycle predecessor receipt](20260807_archive_rb.json) replays all
seven paths in its archive-history publication commit: 106,469 bytes, all
matched exactly.

Receipts are immutable evidence generations. A later receipt may bind a newer
version of the same path without deleting or reinterpreting the earlier one.
Do not add receipt totals together as unique-file totals unless the controlling
manifest explicitly proves that the scopes are disjoint.

This landing concerns GitHub publication evidence only. Producer QA and
separately owned publication surfaces remain outside its claims.
