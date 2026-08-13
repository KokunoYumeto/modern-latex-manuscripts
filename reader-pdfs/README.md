# GitHub Reader Shelves

This is the direct landing for the reader-facing roots that this
GitHub-maintenance task is allowed to catalog. Open the linked coverage map
before treating a filename as current, complete, source-faithful, independently
reviewed, or an invitation to start a new translation.

Observed 2026-08-07: fourteen allowed roots contain 402 tracked files /
932,575,366 bytes. There are 399 PDFs and three small support files. The set has
401 unique SHA-256 identities, one internal duplicate pair, and no cross-root
duplicate bytes.

Post-audit addition, 2026-08-13: [Open Logic Hindi](open-logic/hindi/)
adds one 14-page working-reader PDF, 184,823 bytes, SHA-256
`80B48447897C49EFD28B9B15A6951EB1C78F2CEE7BFD8DB0C53938D71B4C7793`.
It is mapped separately in the [Open Logic Hindi coverage map](../docs/open-logic-map.md)
and is not folded retroactively into the frozen 2026-08-07 totals below.

## Exact Root Index

Per-root tree digests use ordinal paths relative to that root. The full-set
digest below uses repository-relative paths.

| Reader root | PDFs | Support | Bytes | Tree SHA-256 | Coverage map |
|---|---:|---:|---:|---|---|
| [Additional authors](author-cluster/) | 10 | 0 | 15,291,684 | `6834119ECAB949FD966ACC4E6390ACEBA93DC33127D4BADB749CBC7391863013` | [Map](../docs/cluster-map.md) |
| [Classical](classical/) | 21 | 0 | 79,792,322 | `3CCB01C0470ADCECA8C30381F01E42CDB1542790D34282F1E8A85DE684B03ABA` | [Map](../docs/classical-map.md) |
| [Dedekind](dedekind/) | 2 | 0 | 571,836 | `08867846489C83A29A62F3B0AEFFEBFDBC1E71FB4175770D5AB8188558437627` | [Map](../docs/dedekind-map.md) |
| [Deligne](deligne/) | 96 | 0 | 42,412,442 | `CE8AE55F8E809775FF0F46DD950A8C652249685D2F96313AB0BF650D3283059A` | [Map](../docs/deligne-map.md) |
| [Dirichlet](dirichlet/) | 2 | 0 | 20,990,879 | `D43DABDB4AEB21AACCD3641362746F6C538FE732ADBD9ED7AC9E2552A69F4736` | [Map](../docs/dirichlet-map.md) |
| [EGA](ega/) | 10 | 0 | 250,754,356 | `0142D300645188929023C253BA649795EE3425FC2C546FD697D7EF000D519AD4` | [Map](../docs/ega-map.md) |
| [Gauss](gauss/) | 14 | 0 | 115,264,723 | `9CC990DAF36F41CE2A91602BCA99E1527FAD91603DF53BD363CFCF30F0FD9686` | [Map](../docs/gauss-map.md) |
| [Noether](noether/) | 129 | 3 | 72,229,799 | `2C3EB4E0ABB80F62689AFA7333CE156AD1EE1A7F69EBB533EB30204E270673E2` | [Map](../docs/noether-map.md) |
| [Non-European mathematics](non-european/) | 72 | 0 | 244,889,001 | `742D16670E2EFED507B7509B632B17519418374D9BBBAFC1F82AD95552724B84` | [Map](../docs/non-european-map.md) |
| [Riemann](riemann/) | 2 | 0 | 4,372,317 | `9D8CB090D50B4789E8CF476E40DA4EEA7A07F6417F91242C75768E5F2E0B625D` | [Map](../docs/riemann-map.md) |
| [Steinitz](steinitz/) | 21 | 0 | 70,809,375 | `9CEDCE699E75ACDA36DDEF55D6FB2EA00C36F1F77E2F2289E88EACD901D2308A` | [Map](../docs/steinitz-map.md) |
| [Sylvester](sylvester/) | 1 | 0 | 2,058,797 | `F42B91C2B356D8D10698E291892C97DD9FE27BFA95A254032A123CBFF73F53A6` | [Map](../docs/sylvester-map.md) |
| [Ukrainian applied mathematics](ukrainian-applied-math/) | 13 | 0 | 4,710,882 | `6F00C45BAECB33F9BA43848157071A9973EF3BDAD2EFB1DC6C729929B453EC56` | [Map](../docs/ukrainian-map.md) |
| [Weber](weber/) | 6 | 0 | 8,426,953 | `0A570B6AB6DAD18478D9D0815D8B76C12BDE3E749EABCD74839312014F47F3D9` | [Map](../docs/weber-map.md) |

The complete 402-row canonical stream is 68,056 bytes with tree SHA-256
`620DF4B8EC4982C3CAF6190166ADF2DAE369D8D099073DD5511B30675BB61F6F`.
Exact machine evidence is in
[`20260808_readers_r5.json`](../manifests/github-custody/20260808_readers_r5.json).

## Duplicate And Support State

Only one SHA-256 identity occurs twice. These two non-European paths are
byte-identical (125,405 bytes; SHA-256
`28DF2CBC08FDE1734EB7D1CACCB5A9F7766AA8E1F7BB334394BF8976C7DF8990`):

- `10-15 English Translation - Omar Khayyam - Treatise on Algebra.pdf`
- `60-04 Islamic Original - Omar Khayyam - Treatise on Algebra.pdf`

They are one byte identity under two labels, not two independently established
language editions. The [non-European map](../docs/non-european-map.md) preserves
the work/language caveat.

The three non-PDF support files are all under the Noether root: one exact CJK
SHA-256 CSV and two small README files. Their full paths, bytes, and hashes are
in the machine manifest. They are navigation/provenance support, not reader
editions.

The four additional Noether PDFs are the complete v038 Russian, Ukrainian,
Latin-script Interslavic, and Cyrillic-script Interslavic cumulative readers.
They are exact mirrors of the corresponding frozen source-release PDFs; their
scope and language-review caveats are recorded in the
[Noether map](../docs/noether-map.md) and the
[Slavic custody manifest](../manifests/github-custody/20260807_slavic.json).

The current [424-page Simplified-Chinese R4 reader](noether/zh-r4.pdf) is an
exact mirror of the sealed source-release PDF. It covers Papers 1–43, complete
Post44, Post45, and post-bibliographic matter. Two later distinct-calendar-day
certification checks remain pending; its scope is PRC-oriented `zh-Hans-CN`,
not `zh-Hans-SG`, generic Hant, or TW/HK/MO localization. The [413-page R3
reader](noether/zh-r3.pdf) remains unchanged as its immediate predecessor; see
the [Noether map](../docs/noether-map.md) and [R4 custody
manifest](../manifests/github-custody/20260807_zh_r4.json).

The separate [424-page R5 pending reader](noether/zh-r5-pending.pdf) preserves
the frozen successor that realizes seven returned repairs, including the
complete Paper 45 span. It is not the current reader: independent acceptance is
absent, `publishable=false`, clean-day count is zero, and two later distinct-day
checks remain. Its exact state and source relation are in the [R5 custody
manifest](../manifests/github-custody/20260807_zh_r5.json).

## Reading Rule

The directory name `reader-pdfs` describes repository placement, not quality.
Some files are current readers; others are bounded checkpoints, broad drafts,
containers, rejected bilingual history, or superseded generations. The linked
map decides which role applies and records the continuation cursor, source
binding, errors, reversals, and duplicate relations.

Separately owned, revoked, or prohibited reader surfaces are intentionally
absent and were not inspected. Their absence from this page is a task boundary,
not evidence that their work does not exist.
