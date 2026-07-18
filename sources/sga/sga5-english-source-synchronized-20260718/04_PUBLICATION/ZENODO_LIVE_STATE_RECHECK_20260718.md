# SGA 5 live Zenodo state recheck

Latest read-only query: 2026-07-18T14:59:03Z
(16:59:03 Europe/Berlin).

Official endpoint: `https://zenodo.org/api/records/21430393`.

## Current record

- DOI: `10.5281/zenodo.21430393`.
- Concept DOI: `10.5281/zenodo.20410947`.
- Created: `2026-07-18T16:38:16.767817+02:00`.
- Updated: `2026-07-18T16:38:17.930457+02:00`.
- Title: `SGA 1, SGA 5, and SGA 6: Modern LaTeX Working Editions,
  Source Workpasses, English/French/Spanish Translations, and Audit
  Materials`.
- Version label: `2026-07-18 SGA 6 support-archive privacy withdrawal; SGA
  1/5/6 readers retained`.
- Publication date: `2026-07-18`.
- Access-right field: `open`.
- Record metadata license identifier: `cc-zero`.
- File count: 17.

The latest-version endpoints for the earlier records `21429328` and
`21420146`, as well as concept record `20410947`, resolved to `21430393` at the
query time above. The immediately preceding same-day record `21429328` is no
longer current.

The API note says this is a reader-first SGA 1/5/6 record and that the SGA 6
path-leaking support ZIP was removed pending a privacy-clean replacement. It
also disclaims a critical-edition, proof-checking, or whole-SGA completion
claim.

The `cc-zero` value is record metadata. It does not establish permission to
redistribute the Springer scan, the underlying French text, inherited English,
or the derivative translation. Those rights caveats remain separate.

## Files reported by the official API

| File | Bytes | API checksum |
|---|---:|---|
| `98_SGA6_SupportArchive_Withdrawn_PublicPathHygiene_20260718.md` | 1,250 | `md5:4dde2177bc0a8beae9b6712fa22e3fcb` |
| `04_SGA6_idx684_public_manifest_20260718.csv` | 876 | `md5:b2169efd0f814afea5c1723f33148194` |
| `01_SGA6_French_SourceRescribe_Workpass_NotCertified_idx684_20260718.pdf` | 2,870,039 | `md5:8df8a940a0aaf696b872846e8d686968` |
| `04_SGA6_idx684_public_sha256_20260718.csv` | 599 | `md5:35cb592cf4ba2b7a970010a3a2de8bc2` |
| `03_SGA5_English_public_manifest_20260717.csv` | 516 | `md5:d37e6056452962382d25c93857267e45` |
| `03_SGA5_English_public_sha256_20260717.csv` | 444 | `md5:2b52964fa511f6be5faf647c53ccf193` |
| `03_SGA5_English_TeX_Audit_and_SourceSupport_NotCritical_20260717.zip` | 149,702,010 | `md5:1958afe3205dd7d5931d86199cf8b25f` |
| `00_SGA5_English_SourceChecked_WorkingTranslation_NotCritical_20260717.pdf` | 2,054,026 | `md5:6b6cea8fc32f4440a4dbbf99f7817dac` |
| `04_SGA6_TeX_SourceRescribe_Audit_NotCertified_idx684_20260718.zip` | 13,052,838 | `md5:4488d5d34412b591f746c927e5ac2d16` |
| `02_SGA6_English_FullRange_Layered_WorkingReader_CORRECTED_20260718.pdf` | 2,565,870 | `md5:eb031a5c8f4fa1ef1792f9c216e29532` |
| `00_SGA5_French_Workpass_NotCertified_20260706.pdf` | 2,015,658 | `md5:546da52a90bfb5e49a0cd2a0380de593` |
| `03_SGA5_TeX_Audit_Ledgers_and_SourceSupport_NotCertified_20260706.zip` | 739,144,631 | `md5:8f66c8c8fb66e786a580559f94f89f3b` |
| `02a_SGA6_ExposeX_Spanish_idx532_537_WorkingTranslation_20260718.pdf` | 219,996 | `md5:1ec671de9218fdb36418d1a954f47400` |
| `05_SGA6_ExposeX_Spanish_idx532_537_TeX_Evidence_20260718.zip` | 2,620,930 | `md5:1e794997d3a30d1e5556aacb25f06a05` |
| `07_SGA1_English_ExposeI_Opening_SectionI1_TeX_Evidence_20260718.zip` | 735,608 | `md5:66f6bbcf48b832508592f8467226fbcb` |
| `00a_SGA1_English_ExposeI_Opening_SectionI1_SourceAudited_WorkingCheckpoint_20260718.pdf` | 284,532 | `md5:eef3bca993416c8b5481649a889b5651` |
| `99_SGA_Public_Status_SGA1_5_6_NotCritical_20260718.md` | 1,959 | `md5:3afa4fc0a9927256e6d7ce87719e0ddf` |

## SGA 5 disposition

The six SGA 5 files carried forward from `21429328` retain their filenames,
byte sizes, and MD5 checksums. In particular, the live SGA 5 English PDF is the
pre-reopen 2,054,026-byte baseline, and the live 149,702,010-byte support ZIP is
the previously audited scan-bearing package. Neither is the repaired local
reader or scan-free support candidate.

The live SGA 5 support ZIP contains the complete 62,025,563-byte scan and
fifteen scan-derived PNGs without an internal rights/attribution file. It is
superseded for any future preservation handoff.

## Required disposition

- Use the existing concept DOI; do not mint a duplicate record.
- Replace only through archive maintenance after the repaired scan-free
  candidate passes an independent freeze audit.
- Requery the official API immediately before an actual publication action,
  because two newer concept versions appeared during this repair session.
- Do not infer redistribution rights from `cc-zero` record metadata.

Earlier live-state receipts are retained outside this lean bundle as historical
evidence. This dated recheck controls current-version references at the stated
query time.
