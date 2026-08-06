# GitHub raw-readback receipts

Each file in this directory is a generation-specific receipt for bytes already
pushed to GitHub. A receipt binds its source commit and remote ref to exact
paths, byte counts, hashes, and mismatch results. It proves the recorded GitHub
transport; it does not invent mathematical review, source fidelity, rights, or
completion beyond the underlying checkpoint.

Start with the current [archive-history receipt](20260806_archive_r4_rb.json),
the [human archive history](../../docs/github-archive.md), and the
[custody-index landing](../github-custody/README.md).

The current [navigation-link closure receipt](20260806_nav_rb.json) binds the
root, browse, and site-map landings plus the 34-document committed-blob audit.

The [Noether Slavic v038 source receipt](20260807_slavic_rb.json) binds every
path changed by its source commit: 126 commit-pinned raw files / 73,170,246
bytes, all matched exactly.

The [v038 catalog receipt](20260807_slavic_cat_rb.json) binds the twelve
custody/index/log/landing paths added by the catalog commit: 2,426,184 bytes,
all matched exactly.

The [shelf-closure receipt](20260807_slavic_close_rb.json) binds seven paths /
96,574 bytes, and the [map/audit receipt](20260807_slavic_audit_rb.json) binds
five paths / 87,097 bytes. Both replays matched every byte.

Receipts are immutable evidence generations. A later receipt may bind a newer
version of the same path without deleting or reinterpreting the earlier one.
Do not add receipt totals together as unique-file totals unless the controlling
manifest explicitly proves that the scopes are disjoint.

This landing concerns GitHub publication evidence only. Producer QA and
separately owned publication surfaces remain outside its claims.
