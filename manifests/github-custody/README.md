# GitHub custody controls

This directory holds generation-specific machine evidence for the GitHub
archive: exact scope manifests, path/byte/SHA-256 inventories, link audits,
decision-log controls, and custody receipts that must remain outside frozen
producer payloads.

## Current task-owned indexes

- [Twenty-six-cycle archive history](20260808_archive_r9.json)
- [Coverage-map inventory](20260807_maps_r5.json)
- [Current reader/source shelf closure](20260808_shelves_r9.json)
- [Direct-reader inventory](20260808_readers_r5.json)
- [Tracked-source summary](20260807_sources_r5.json) and
  [path inventory](20260807_sources_r5.csv)
- [Noether Slavic v038 custody](20260807_slavic.json) and
  [exact path index](20260807_slavic.csv)
- [Noether Simplified-Chinese R4 custody](20260807_zh_r4.json) and
  [exact path index](20260807_zh_r4.csv)
- [Frozen Simplified-Chinese R5 pending-review custody](20260807_zh_r5.json),
  [498-row archive index](20260807_zh_r5.csv), and
  [external replay](20260807_zh_r5_ext.json)
- [R4 ED0008 compatibility custody](20260807_zh_a4.json) and
  [four-row index](20260807_zh_a4.csv)
- [Immutable Simplified-Chinese R3 predecessor custody](20260807_zh.json) and
  [exact path index](20260807_zh.csv)
- Current bounded local-link audit: `20260808_links_r11.json`
- [Maintenance-log index](20260806_log.json) and
  [append-only log](log.jsonl)

The [human archive history](../../docs/github-archive.md) explains the bounded
cycles. Exact public-byte receipts have their own
[landing page](../published-github/README.md).

The [twenty-three-cycle archive predecessor](20260808_archive_r6.json),
[twenty-two-cycle archive predecessor](20260807_archive_r5.json),
[twenty-one-cycle archive predecessor](20260807_archive_r4.json),
[twenty-cycle archive predecessor](20260807_archive_r3.json),
[nineteen-cycle archive predecessor](20260807_archive_r2.json),
[first coverage-map index](20260806_maps.json), and all earlier generations
remain immutable. The
[twelve-cycle archive r3](20260806_archive_r3.json),
[eight-cycle archive r2](20260806_archive_r2.json), and
[four-cycle predecessor](20260806_archive.json) remain immutable historical
generations. The [eighteen-cycle predecessor](20260807_archive.json) also
remains unchanged. The current twenty-six-cycle index binds the complete
five-commit publication and main closure of [archive r8](20260808_archive_r8.json).
That predecessor already binds the bounded current shelf and local-link cycle;
neither generation rewrites R5, R4, R3, or any earlier generation.

The frozen R5 successor is preserved additively and remains pending independent
review; it does not replace the accepted R4 reader. The 2026-08-07 r5 source,
map, reader, and shelf inventories add its exact 496-file source projection and
one pending reader mirror. The r4 inventories preserve the four-file ED0008
compatibility predecessor, and every earlier inventory remains immutable. The r2 inventories
retain the exact Noether Slavic v038 and Simplified-Chinese R3 projections;
every predecessor remains unchanged.

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
