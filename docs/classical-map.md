# Classical GitHub Shelf Map

Observed 2026-08-06. This page maps the two mixed GitHub roots
[`reader-pdfs/classical`](../reader-pdfs/classical/) and
[`sources/classical`](../sources/classical/) without treating their filenames as
quality certification.

The current roots contain exactly three authors: Arthur Cayley, Richard
Dedekind, and P. G. Lejeune Dirichlet. Gauss, Weber, Noether, and Riemann have
separate GitHub shelves and maps; they are not present in these two mixed roots.

## Exact Custody

| Selection | Files | Bytes | Canonical tree SHA-256 |
|---|---:|---:|---|
| Complete mixed shelf | 832 | 216,679,649 | `1577003522C65FA647E7F52880C5BCD5975E5017E29B1D4017DCE00305BFDAF4` |
| Direct readers | 21 | 79,792,322 | `474B6469809F984D2777A0D5FFC235D6C91F7DE4465CCFFF2EC987B8772249AB` |
| Source/history tree | 811 | 136,887,327 | `32A21952C6B8A2F60860A70DC45279175D20A2C739788EB14A58A5093608BECF` |

The canonical stream is UTF-8 without BOM, ordered by ordinal repository-relative
path, with one `relative_path<TAB>bytes<TAB>SHA256<LF>` row per file. The complete
stream is 188,422 bytes. The machine-readable audit is
[`20260806_classical.json`](../manifests/github-custody/20260806_classical.json).

The shelf has 791 unique byte identities. Thirty-six SHA-256 groups contain 77
paths, so 41 paths are byte-redundant copies. No duplicate group crosses an
author boundary. These copies remain preserved because some are direct readers
and others are source-generation or build-history members.

## Author Routing

| Author | Readers | Reader pages | Source/history files | Total files | Total bytes | Exact status map |
|---|---:|---:|---:|---:|---:|---|
| Arthur Cayley | 13 | 5,713 | 781 | 794 | 201,021,770 | [Cayley map](cayley-map.md) |
| Richard Dedekind | 5 | 985 | 13 | 18 | 12,300,716 | [Dedekind map](dedekind-map.md) |
| P. G. Lejeune Dirichlet | 3 | 247 | 17 | 20 | 3,357,163 | [Dirichlet map](dirichlet-map.md) |

The partitions are mutually exclusive and account for all 832 files. Use the
author maps for continuation state and quality caveats; use this page to avoid
double-counting the shared shelf as another edition.

## Direct Readers

All 21 PDFs are direct files in
[`reader-pdfs/classical`](../reader-pdfs/classical/). Page counts are structural
PDF page slots, not proof of source fidelity or work completeness.

### Cayley

| Volume | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| I | 488 | 7,764,737 | `7B44F77BA13BFA88D7681A1647A08A917605870A908BBAF03CAB4A31B59FEC49` |
| II | 421 | 3,977,622 | `ABA67C1092418BEE639F331127A3C743257C051DF42029C324167A256FA70C6F` |
| III | 322 | 3,774,202 | `00545308A22E91EFEF1628BE76E040D3C4F49D9787D16D65CA4BB7B5C79A4D5F` |
| IV | 496 | 4,193,529 | `8F0BBB6B96FC98ED9F93608EBFBA55D281E3ED3FD0D488444F12293D92836218` |
| V | 443 | 6,186,480 | `40E22DE5077320635DB3403459AA10CE6BDC5624BD288107AAEF0DA59C20B68F` |
| VI | 407 | 4,159,529 | `996989A0E3A2A15AF0E44B1BC1EEA163C0961F9A3B5D05829C810BFA92ED6D2B` |
| VII | 336 | 4,852,925 | `DE5D4C4803C5671C278F2B1920FBE70FFB45852D9C09FCDBE1E29480F8C3C7A5` |
| VIII | 536 | 6,015,885 | `3E47A099A58930B7EC28E0A591B6A76AC4DE3729E90F7D657BDDC6D0B7C545CC` |
| IX | 348 | 5,211,862 | `40A1AAE1577D480833B12BD661DF2BAF1E06A184674C798ECB398006708D5151` |
| X | 576 | 6,833,979 | `808FEACEAAE71F5C9046EADF480427D2772AFE7C148567AFE6C7F94D4E1F962A` |
| XI | 415 | 4,779,372 | `D5EC6DAD41FF489C5ECD002C26CEB29D59C6FA1A63F6CA2B55A4D2C1D67A056A` |
| XII | 437 | 6,001,148 | `F018C62296595F43871CA153FBA52030F937B8F9EAFE5136FE3AF58131C1624B` |
| XIII | 488 | 6,130,483 | `480F9F0E45AC427F08F9C2C993E49092BAA419A942AA327917E9915683A2B679` |

The inherited `Complete` and `Source-Checked` filename labels are not current
quality claims. The [Cayley map](cayley-map.md) records manifest conflicts,
visible omissions, and the current de-promotion: no range is presently promoted
as source-faithful.

### Dedekind

| Reader | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| *Continuity and Irrational Numbers*, preface and §§1–4, English | 7 | 251,399 | `6502E044126F32B6FD967B80E6B41C2C15C5C43AC4366C3D12FAD95BFA230E54` |
| *Gesammelte Mathematische Werke*, Band I | 312 | 2,475,123 | `36483A32E95867B7E51464D5372EEA43B79589B8374E6CF8DB62883CBA059727` |
| *Gesammelte Mathematische Werke*, Band II | 304 | 1,853,022 | `9BD5FC5D80945816278D827667C3F2CAFA1D2F970DF6DFBC0A1FAF03582A57CA` |
| *Gesammelte Mathematische Werke*, Band III | 354 | 2,790,002 | `FD7DCD78CF6AD4877D24737C2EAB4F3099A1361778CDB4FE663A93A1641DD4C7` |
| *Stetigkeit und irrationale Zahlen*, preface and §§1–4, German | 8 | 261,833 | `36D9D2E1E1231F8E4035F4FBF737471F20F3C4AFF09942F1E280D44B5FF868F2` |

The two short *Stetigkeit* readers are source-bearing bounded segments. The
three broad GMW readers have no matching source tree in this mixed shelf and
remain reader-only drafts.

### Dirichlet

| Reader | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| *On the Stability of Equilibrium*, English | 3 | 248,375 | `DEBD6EFABB40DC9BA6639A4771747DCB11E7DA9AC4532B28E6C1C7E17B7F3CE5` |
| *Selected Works* | 241 | 1,776,322 | `37363B4A878977A4916D40627872C9329721B73EDDC30E208F2173F81FA2EFCA` |
| *Ueber die Stabilitaet des Gleichgewichts*, German | 3 | 254,493 | `AE8E1813B3B15DD886422F7EA42DDF3A6833C28072E841ED08A4C2C0280163BD` |

The German/English stability pair is separately source checked. The 241-page
selected-works scaffold is not source authority and must not be used as a
completion baseline.

## Source And History Generations

| Author | Selection | Files | Bytes | Tree SHA-256 |
|---|---|---:|---:|---|
| Cayley | `cayley_clean_per_volume_public` | 300 | 38,304,093 | `6FE6D3776AEC5777C778618C36F21E193666A711545C0C7A617EE86B5EEE52D2` |
| Cayley | `cayley_repaired_slice_sources_2026-05-29` | 450 | 82,204,074 | `EF736D59E8B448E28AC7CDA295F0587876842D80A586078BB7A9609087D0AFFC` |
| Cayley | June Volume-I assembly | 30 | 10,627,136 | `BE93E1811C4BE7D44EA3A31C387DB2377D6B2671497F9F1526A52964CD0BB7DE` |
| Cayley | Volume-VIII triage note | 1 | 4,714 | `A62F4F99314C88D0D7DBACDC187BFEB7435FF27B1EB523B616FEB1FC7D42E80A` |
| Dedekind | `dedekind-stetigkeit-segment` | 13 | 4,669,337 | `03FD75B6520D19BAECF9F075E2A645C1C3ADDE1DFC477ED68C8229AD31D88967` |
| Dirichlet | `dirichlet-stability` | 17 | 1,077,973 | `AAB55623B15006801013F71C7B4F2C1094E1956B47942D02DBDCC89862335C0F` |

The tree digests in this table use paths relative to each named selection. The
aggregate and author-partition digests use repository-relative paths.

## Duplicate And Supersession Relations

Four direct-reader identities each occur three times: the direct PDF, a
`cumulative_source` copy, and a `new_work_source` copy. The exact identities are
the Dedekind German and English *Stetigkeit* PDFs and the Dirichlet German and
English stability PDFs. They are one byte identity in three custody roles, not
three independently produced editions.

Cayley has 25 internal duplicate groups, Dedekind has five, and Dirichlet has
six. There are no cross-author duplicate bytes. No mixed-shelf Dedekind or
Dirichlet reader is byte-identical to a current direct reader in the dedicated
`reader-pdfs/dedekind` or `reader-pdfs/dirichlet` roots.

Nothing was renamed, deleted, compiled, rendered, OCRed, or rewritten for this
map. The older source generations, placeholders, failures, and superseded
artifacts remain in place as audit history.

## File-Type Shape

The 832 files comprise 313 PDFs, 427 TeX files, 17 Markdown files, 16 text
files, eight PNGs, seven CSVs, one JSON file, two Python files, 33
`.predelim_bak` files, seven `.wave2_bak` files, and one `.paper445_bak` file.
This shape is descriptive custody evidence, not a claim that every TeX file is
buildable or every PDF is current.
