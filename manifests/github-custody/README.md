# GitHub custody controls

This directory holds generation-specific machine evidence for the GitHub
archive: exact scope manifests, path/byte/SHA-256 inventories, link audits,
decision-log controls, and custody receipts that must remain outside frozen
producer payloads.

## Current repository indexes

- Current public-interface cleanup
  [source receipt](../published-github/ui-clean-r1.json), binding the active
  navigation, adoption board, Stacks claim form, contributor contract, tests,
  CI, and reader-facing repository and namespace language on the named surfaces
- Predecessor executable Stacks-preflight
  [closure](../published-github/stacks-pre-r1-close.json) and
  [source receipt](../published-github/stacks-pre-r1.json), binding the exact
  upstream pin, zero-entry registry, composition contract, checker, and
  regression identities; expected result `BLOCKED_EMPTY_OVERLAY_REGISTRY`
- Predecessor empty Stacks-overlay infrastructure
  [closure](../published-github/stacks-infra-r1-close.json) and
  [source receipt](../published-github/stacks-infra-r1.json), with a zero-entry
  overlay registry and a blocked deterministic-composition preflight; no overlay
  content, composed build, or modified edition is bound
- Predecessor Stacks-pin and Commons-handback
  [closure](../published-github/stacks-pin-r1-close.json) and
  [source receipt](../published-github/stacks-pin-r1.json), with the exact
  upstream reference in [stacks-pin.json](../stacks-pin.json), 78 reconciled
  coverage rows, and hardened exact-evidence handbacks; predecessor adoption v3
  [closure](../published-github/adopt-v3-close.json) and
  [source receipt](../published-github/adopt-v3.json), with 78 reconciled
  coverage rows and the hardened exact-commit claim trust boundary; predecessor
  adoption v2 [closure](../published-github/adopt-v2-close.json) and
  [source receipt](../published-github/adopt-v2.json)
- Predecessor [Commons Stacks intake closure](../published-github/stacks-intake-close.json)
  and [source receipt](../published-github/stacks-intake.json),
  with earlier [architecture closure](../published-github/stacks-r1-close.json)
  and [architecture source receipt](../published-github/stacks-r1.json)
- [Steinitz frontier predecessor closure](../published-github/stein-r1-close.json)
  and [source-and-correction receipt](../published-github/stein-r1.json)
- [Thirty-cycle frontier predecessor closure](../published-github/frontier-r1-close.json)
  and [source receipt](../published-github/frontier-r1.json)
- [Twenty-eight-cycle queue-and-scope predecessor](../published-github/20260809_queue_scope_close.json)
- [Twenty-six-cycle predecessor archive history](20260808_archive_r9.json)
- [Current coverage-map inventory](maps-r6.json) and [R5 predecessor](20260807_maps_r5.json)
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
- Current sparse-adoption-CI link audit: `20260809_links_r28.json`
- Offline-claim-auditor predecessor link audit: `20260809_links_r27.json`
- Offline-consumer predecessor link audit: `20260809_links_r26.json`
- Queue-synchronization predecessor link audit: `20260809_links_r25.json`
- Complete adoption-dimension predecessor link audit: `20260809_links_r24.json`
- Ownership-semantics predecessor link audit: `20260809_links_r23.json`
- Reusable-workflow predecessor link audit: `20260809_links_r22.json`
- Claim-auditor predecessor link audit: `20260809_links_r21.json`
- Workflow-label predecessor link audit: `20260809_links_r20.json`
- Handback-interface predecessor link audit: `20260809_links_r19.json`
- Non-mutating adoption-audit predecessor link audit: `20260809_links_r18.json`
- Exact-commit consumer predecessor link audit: `20260809_links_r17.json`
- Human Board-ID predecessor link audit: `20260809_links_r16.json`
- Adoption work/snapshot predecessor link audit: `20260809_links_r15.json`
- Adoption-map synchronization predecessor link audit: `20260809_links_r14.json`
- Adoption-contract predecessor link audit: `20260809_links_r13.json`
- Stable operational adoption feed: [`../adopt.json`](../adopt.json)
- Adoption feed [schema](../adopt.schema.json) and [validation](../adopt.check.json)
- Adoption map-synchronization [raw readback](../published-github/20260809_adopt_maps_rb.json)
- Work-level adoption and snapshot-policy [raw readback](../published-github/20260809_adopt_work_rb.json)
- Human Board-ID [raw readback](../published-github/20260809_adopt_ids_rb.json)
- Exact-commit consumer [raw readback](../published-github/20260809_adopt_get_rb.json)
- Non-mutating adoption-audit [raw readback](../published-github/20260809_adopt_audit_rb.json)
- Handback-interface [raw readback](../published-github/20260809_handback_rb.json)
- Workflow-label source/API [raw readback](../published-github/20260809_labels_rb.json)
- Exact-commit claim-auditor [raw readback](../published-github/20260809_claims_rb.json)
- Reusable-workflow registry [raw readback](../published-github/20260809_flows_rb.json)
- Ownership-semantics [raw readback](../published-github/20260809_owners_rb.json)
- Complete adoption-dimension index [raw readback](../published-github/20260809_index_rb.json)
- Queue-source synchronization and interface-closure [raw readback](../published-github/20260809_queue_rb.json)
- Offline Git-object consumer [raw readback](../published-github/20260809_offline_rb.json)
- Offline claim-auditor and no-lazy-fetch [raw readback](../published-github/20260809_claims_offline_rb.json)
- Sparse continuous-validation [workflow/readback](../published-github/20260809_adopt_ci_rb.json)
- Human workflow guide: [`../../docs/adopt-flows.md`](../../docs/adopt-flows.md)
- Fail-closed consumer helper: [`../../scripts/get-adopt.py`](../../scripts/get-adopt.py)
- Promisor/no-lazy-fetch regression: [`../../scripts/test-adopt-offline.py`](../../scripts/test-adopt-offline.py)
- Read-only claim auditor: [`../../scripts/check-claims.py`](../../scripts/check-claims.py)
- Offline claim lifecycle regression: [`../../scripts/test-claims.py`](../../scripts/test-claims.py)
- Sparse continuous-validation workflow: [`../../.github/workflows/adopt.yml`](../../.github/workflows/adopt.yml)
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
remains unchanged. The twenty-six-cycle predecessor index binds the complete
five-commit publication and main closure of [archive r8](20260808_archive_r8.json).
The current public-interface cleanup
[source receipt](../published-github/ui-clean-r1.json) binds accepted source
commit `efb16617`: source readback matched 14/14 paths / 1,221,750 bytes, and
Actions run `31538054419` passed. Historical evidence files remain unchanged;
the active public interface now uses repository and independently maintained
namespace terms. The additive evidence aggregate through the source is 50
cycles, 3,266 commit-pinned observations, and 1,225,243,201 bytes with zero
mismatches. The predecessor executable Stacks-preflight
[closure](../published-github/stacks-pre-r1-close.json) binds accepted source
commit `23721648` and receipt commit `6a444fad`: source readback matched 15/15
paths / 1,157,128 bytes, receipt readback matched 5/5 paths / 641,474 bytes, and
both Actions runs passed. It binds zero registry entries, overlay files,
mathematical entries, composition runs, generated members, builds, and modified
editions. The additive evidence aggregate is 48 cycles, 3,245 commit-pinned
observations, and 1,223,353,877 bytes with zero mismatches.
The predecessor empty Stacks-overlay infrastructure
[closure](../published-github/stacks-infra-r1-close.json) binds accepted source
commit `15c5c63b` and receipt commit `86f7bafb`: source readback matched 13/13
paths / 581,482 bytes, receipt readback matched 7/7 paths / 655,965 bytes, and
both Actions runs passed. It binds zero registry entries, overlay files,
mathematical entries, composition runs, generated members, builds, and modified
editions. The additive evidence aggregate is 46 cycles, 3,225 commit-pinned
observations, and 1,221,555,275 bytes with zero mismatches.
The predecessor Stacks-pin and Commons-handback
[closure](../published-github/stacks-pin-r1-close.json) binds source commit
`eb82a809` and receipt commit `5f66d4d1`: source readback matched 19/19 paths /
690,910 bytes, receipt readback matched 5/5 paths / 585,847 bytes, and both
Actions runs passed. The additive evidence aggregate is 44 cycles, 3,205
commit-pinned observations, and 1,220,317,828 bytes with zero mismatches. The
adoption v3 [closure](../published-github/adopt-v3-close.json) remains immutable
predecessor evidence.
The [38-cycle Commons Stacks intake closure](../published-github/stacks-intake-close.json)
remains the immutable predecessor at 3,132 observations / 1,215,546,817 bytes;
it preserves Steinitz and all earlier generations without rewriting them.

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
