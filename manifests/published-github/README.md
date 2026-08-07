# GitHub raw-readback receipts

Each file in this directory is a generation-specific receipt for bytes already
pushed to GitHub. A receipt binds its source commit and remote ref to exact
paths, byte counts, hashes, and mismatch results. It proves the recorded GitHub
transport; it does not invent mathematical review, source fidelity, rights, or
completion beyond the underlying checkpoint.

Start with the current [archive-history receipt](20260807_archive_r3_rb.json),
the [human archive history](../../docs/github-archive.md), and the
[custody-index landing](../github-custody/README.md).

The current [navigation-link closure receipt](20260807_links_r2_rb.json) binds
the twenty-cycle archive navigation and its 34-document, 987-local-link
committed-blob audit: six paths / 164,939 bytes, all matched exactly.

The [live-main receipt](20260807_main_rb.json) independently replays the
Simplified-Chinese Noether R3 reader/source seal, current catalogs, archive
controls, locked log, and receipts from `main`: 28 paths / 9,759,875 bytes,
all matched exactly.

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
The [R4 ED0008 compatibility receipt](20260807_zh_a4_rb.json) binds its four
sealed evidence files / 7,012 bytes, all matched exactly. It records no Chinese
byte change and no later-day certification credit.

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

The [twenty-cycle archive receipt](20260807_archive_r3_rb.json) replays all
seven paths in the current archive-history successor: 1,064,837 bytes, all
matched exactly. The [nineteen-cycle predecessor receipt](20260807_archive_r2_rb.json)
remains immutable: three paths / 25,735 bytes, all matched exactly.

Its [receipt-publication closure](20260807_archive_r3_close.json) replays four
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
