# GitHub custody controls

This directory holds generation-specific machine evidence for the GitHub
archive: exact scope manifests, path/byte/SHA-256 inventories, link audits,
decision-log controls, and custody receipts that must remain outside frozen
producer payloads.

## Current task-owned indexes

- [Fifteen-cycle archive history](20260806_archive_r4.json)
- [Coverage-map inventory](20260806_maps_r2.json)
- [Current reader/source shelf closure](20260806_shelves.json)
- [Direct-reader inventory](20260806_readers.json)
- [Tracked-source summary](20260806_sources.json) and
  [path inventory](20260806_sources.csv)
- [Bounded local-link audit](20260806_links.json)
- [Maintenance-log index](20260806_log.json) and
  [append-only log](log.jsonl)

The [human archive history](../../docs/github-archive.md) explains the bounded
cycles. Exact public-byte receipts have their own
[landing page](../published-github/README.md).

The [first coverage-map index](20260806_maps.json) remains the immutable
predecessor to the current additive r2 index. The
[twelve-cycle archive r3](20260806_archive_r3.json),
[eight-cycle archive r2](20260806_archive_r2.json), and
[four-cycle predecessor](20260806_archive.json) remain immutable historical
generations; the current r4 index adds later cycles without rewriting them.

These indexes do not silently promote a producer checkpoint, turn an unchecked
draft into a reviewed edition, or erase a superseded generation. Read the
linked scope and caveat fields before interpreting `complete`, `current`, or
similar inherited names.

## Detached legacy controls

Archive-generated custody receipts and mirror checksum indexes also live here
when placing them inside a producer payload would change that payload's frozen
file set.

- `20260719_noether-paper04-section08/` applies to
  `sources/noether/paper04-english-section08-20260719/`.
- `20260719_sga2-expose-vii/` applies to
  `sources/sga/sga2-english-expose-vii-20260719/`.

Within each `GITHUB_MIRROR_SHA256.csv`, the custody receipt resolves in the
control directory and producer-relative paths resolve against the associated
payload root above. Moving these controls did not change their bytes or the
producer files.
