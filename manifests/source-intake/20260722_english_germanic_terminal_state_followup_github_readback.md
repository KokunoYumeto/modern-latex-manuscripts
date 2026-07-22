# English/Germanic terminal-state follow-up GitHub readback

Status: `GITHUB_METADATA_PUBLICATION_AND_RAW_BYTE_READBACK_COMPLETE`

Pull request [#64](https://github.com/KokunoYumeto/modern-latex-manuscripts/pull/64)
merged source commit
`a6bc2bc41dfba2d7a2ce317ec97c3d6444f347a5` at public `main` commit
`98050583b004b665bfcc081fd6cdcc964a1d8503`.

## Readback method

A fresh shallow sparse clone resolved exactly to the merge commit with a clean
worktree and materialized only the seven changed metadata paths. Source and
merge Git blob IDs match for all seven paths. Independent raw GitHub fetches
then matched all seven merge blobs byte-for-byte:

| Path | Bytes | SHA-256 |
|---|---:|---|
| `docs/pending-zenodo-uploads.md` | 1,313,404 | `4EA06C9B14EF696388737D0B469EE450BFCF572333584D313229FD4F8B1FB39B` |
| `docs/project-status-dashboard.md` | 26,827 | `B8FA99BCA9E4CD787AA7E1B67101E7C06C27DEDBA786FA74A8C77E182C36B168` |
| `manifests/archive-maintenance-logbook.jsonl` | 288,622 | `A6A8CE5F79F43DAFF7A7049C8F03D10BD7A0F51D96F92F29AB62B8DCA5B30DCA` |
| `manifests/archive-maintenance-logbook.md` | 114,533 | `FDE093F9DB0F8C80AD4CB832FBAE183BEA01CEBD207A0F7DE6550F427E7A479A` |
| `manifests/current-status.md` | 696,550 | `B22B5BF1F0552CAE4E9FF381E8F6B40E9BB9006881DE47BE5C7D3FA1645D7160` |
| `manifests/source-intake/20260722_english_germanic_terminal_state_followup_0658.json` | 4,494 | `BAB02C958FED1925A9AFCEF008E534BA7F2EDD1C4F604A14E75CB3CE1F9C6417` |
| `manifests/source-intake/20260722_english_germanic_terminal_state_followup_0658.md` | 5,226 | `7B17FFF6849293DD466C52584B36C6251558C4593CB2433E3820F586127855CC` |

The sparse checkout applied local CRLF conversion to the JSONL worktree copy,
so that transformed checkout byte stream was excluded from the byte-identity
claim. The raw Git blob and independent raw GitHub response match exactly at
288,622 bytes and the SHA-256 above. The raw JSONL parses as 97 records / 97
unique decision IDs through `AML-20260722-EG-085`.

## Public boundary

The server diff contains seven metadata paths, 249 additions, zero deletions,
and zero private-path or thread-ID hits. The merge tree contains no Noether
tranche-039 target, SGA2 lines3618-3622 target, SGA1 I.10.5 target, workbook,
preview, evidence tree, source slice, or source-page raster path. Public
source-bearing coverage is unchanged.

A live API check at `2026-07-22T07:05:01+02:00` returned SGA record
`21435547` at 33 files / 73,450,481 bytes and Noether record `21434690` at
100 files / 2,362,920,800 bytes. No Zenodo draft, mutation, deposition, or
duplicate was created.

This closes GitHub publication and readback for metadata only. The Noether
body remains internal and path-bearing, SGA2 still lacks a manager seal and
handoff, and SGA1 I.10.5 remains pre-seal.
