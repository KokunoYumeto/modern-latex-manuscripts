# Survival Bridges And Source-Search Packets

Date: 2026-06-26

This addendum records a maintenance pattern that became explicit during the Noether R132-R135 local handoff sequence.

## Purpose

Some useful packages do not patch the TeX body. They still matter because they prevent regressions, stale queue replay, and source-search confusion.

Two distinct package types should be labelled explicitly:

- **No-patch survival bridge:** checks that previously accepted spans still survive in a later cumulative branch, either byte-exactly or after a documented normalization/extraction step.
- **Source-search packet:** records which source witnesses were sought, acquired, rejected, or found inadequate, and why no stronger source baseline was promoted.

## Public Status

These packages are evidence and routing aids, not reader editions.

They should not be described as proof, certification, critical editions, full paper closure, or source-fidelity verification. Public notes should instead say exactly what they do:

- no TeX body patch;
- anti-regression or stale-queue-prevention evidence;
- source-routing or source-quality-blocked evidence;
- span hashes, source archive checksums, and current preferred branch pointers;
- explicit caveats about what remains uncertified.

## Raw Source Archives

Large raw source archives such as IA/GDZ/JP2 bundles should not be loose-uploaded just because a source-search package touched them. Keep their checksums and local/source-library pointers in the compact handoff. Upload the bulky source only as part of a deliberate source-support rollup or source-library refresh.

## Workflow Rule

Before a package reaches Zenodo, inspect whether it is:

1. a reader-facing edition or translation;
2. a patched cumulative branch;
3. a source witness/support rollup;
4. a no-patch survival bridge;
5. a source-search packet;
6. failed-run salvage or locator material.

Only the first three should normally be fronted as public reader/source artifacts. The latter three can be archived when useful, but they need conservative labels and should not crowd out the actual TeX/PDF deliverables.
