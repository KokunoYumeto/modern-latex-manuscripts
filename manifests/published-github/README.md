# GitHub raw-readback receipts

Each file in this directory is a generation-specific receipt for bytes already
pushed to GitHub. A receipt binds its source commit and remote ref to exact
paths, byte counts, hashes, and mismatch results. It proves the recorded GitHub
transport; it does not invent mathematical review, source fidelity, rights, or
completion beyond the underlying checkpoint.

Start with the current [archive-history receipt](20260806_archive_r3_rb.json),
the [human archive history](../../docs/github-archive.md), and the
[custody-index landing](../github-custody/README.md).

Receipts are immutable evidence generations. A later receipt may bind a newer
version of the same path without deleting or reinterpreting the earlier one.
Do not add receipt totals together as unique-file totals unless the controlling
manifest explicitly proves that the scopes are disjoint.

This landing concerns GitHub publication evidence only. Producer QA and
separately owned publication surfaces remain outside its claims.
