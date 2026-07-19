# Rejected SGA 1 I.9.1 public checkpoint r1

Status: rejected before freeze; never a final-named checkpoint and never eligible
for archive handoff.

The 2026-07-19 11:09+02 run stopped at the secondary public-CSV artifact
gate. The source, English TeX, PDF build, render, cumulative controls, and
primary machine validator had passed to that point. The secondary checker used
`$row.PSObject.Properties[0].Value`; in PowerShell 7 this attempted to obtain a
property named `0`, yielded a blank value for every row, and collapsed each
ledger's primary-ID set to one blank entry. The gate therefore rejected
`ledgers/SOURCE_COMPARISON_I_4.csv` even though the ledger itself was already
rectangular, unique-ID, and formula-safe under the primary validator.

This is a validator implementation failure, not a source or translation
failure. The correction is to enumerate the property collection explicitly as
`@($row.PSObject.Properties)[0].Value`, reject blank IDs explicitly, and rerun
on a separately named r2 surface. The same r2 sanitizer must also replace a
line-wrapped literal user-name fragment found by the post-failure privacy
audit; no r1 file may be filled or renamed as a successful payload.

Preserved failed surfaces:

- freeze script: 66,334 bytes, SHA-256
  `A2287F814F03DE56F0E85E3F015F456BC6A69B3E6B21CBB37D17B44D188D71D6`;
- isolated build: 16 files / 760,125 bytes, inventory digest
  `0FE467C827D0C47B261A45D530207A089D85D752608FDA228C0357FEBF07EBA7`;
- render A: 16 files / 6,262,810 bytes, inventory digest
  `77876BEB3A2A431FFA40A0D466690E470387C38B6AEECC0B97F6AA5CAF7100C6`;
- render B: the same 16-file / 6,262,810-byte digest;
- incomplete staging tree: 97 files / 7,566,589 bytes, inventory digest
  `CB6FB2FC9972731B384F7C9240161816E5D106E51265136E3CD65D04E8559A68`;
- final r1 target: absent;
- rejected-postfreeze r1 target: absent;
- custody CSV and handoff Markdown: absent.

The inventory digests are SHA-256 over ordered
`relative_path|bytes|sha256` lines joined with LF and no terminal LF. Archive
acceptance, publication, and remote readback are inapplicable and unclaimed.
