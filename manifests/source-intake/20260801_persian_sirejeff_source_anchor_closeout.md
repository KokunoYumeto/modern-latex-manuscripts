# Persian SireJeff Source-Anchor Closeout

Status: `PASS_ALREADY_PUBLIC_NO_DUPLICATE_UPLOAD`.

The 2026-07-05 packages 458-459 intake correctly reported that those two
rolling-delta packages contained only source-canon pointers, not the actual
objects named `fa_github_sirejeff_persian_main_tex` and
`fa_github_sirejeff_source_zip`. A later source-body payload closed those two
specific gaps. This receipt does not reinterpret packages 458-459 as
source-bearing and does not close their unrelated Arabic, Farsi, Dari, or
Tajik source-collection gaps.

## GitHub Readback

Current public main commit:
`6afa79b9d0b39624ffbec3d186599680f20ff57e`.

The exact public files are:

- `interlanguage-sidecar/20260705/other_pc_r10_rtl_persianate_arabic_source_body_payload_20260705/language-source-bodies/rtl-persianate-arabic-20260705-r3-witness-layer/source_files/fa/fa_github_sirejeff_persian_main_tex.tex`
  - 6,280 bytes
  - SHA-256
    `AA4207AE05BA1804FFB3BBE8265954571BE276E75A8CB7A1656A72ED92417427`
  - Git blob `0d6edd72d66906978a2060b4053b1e39bc5bb59e`
- `interlanguage-sidecar/20260705/other_pc_r10_rtl_persianate_arabic_source_body_payload_20260705/language-source-bodies/rtl-persianate-arabic-20260705-r3-witness-layer/source_archives/fa/fa_github_sirejeff_source_zip.zip`
  - 2,007,400 bytes
  - SHA-256
    `EEEE28E88CA465F0A125AFE056F6203B84C138EB44114867D8E49F3C3344252C`
  - Git blob `823a92fc287cb23191ccf4d464c1c7f48ef77bf1`

Fresh commit-pinned anonymous raw downloads matched both identities. The ZIP
has 44 readable members and 2,506,939 uncompressed bytes. Its embedded
`SireJeff-linear-algebra-3blue1brown-notes-faa29cc/persian_notes/main.tex`
is byte-identical to the direct TeX file.

## Zenodo Readback

The current Interlanguage concept head is
[`10.5281/zenodo.21739451`](https://doi.org/10.5281/zenodo.21739451), under
concept DOI [`10.5281/zenodo.21124403`](https://doi.org/10.5281/zenodo.21124403).
It retains
`06_Interlanguage_OtherPC_SourceBodies_RTL_Persianate_Arabic_20260707.zip`,
884,720,731 bytes, MD5 `916409ae7791ae5dd917d64524a36bf3`.

An anonymous HTTP-range replay read the outer ZIP central directory without
downloading the 884 MB object. It found 1,047 members and read the four
SireJeff objects in the full-source and witness layers. Both direct TeX copies
match SHA-256 `AA4207...17427`; both source-ZIP copies match SHA-256
`EEEE28...252C`. Each nested ZIP has 44 readable members, and its embedded
Persian `main.tex` matches the direct file.

No GitHub package, Zenodo successor, duplicate concept, or local large-file
copy was needed. This is exact source custody and pointer closeout only, not
native review, accepted terminology, translation certification, or a blanket
license determination.

The mandatory locked shared-log append recorded decision
`EG-ARCHIVE-PERSIAN-SIREJEFF-SOURCE-ANCHOR-CLOSEOUT-20260801-0001` and
returned 428 unique records, 2,696,108 bytes, SHA-256
`D840AF5A60B6FB48D7A377529DFBB62048F4B70A06F42C44E9B85B17B1C1CBB8`,
with `errors=[]`.

GitHub PR [#210](https://github.com/KokunoYumeto/modern-latex-manuscripts/pull/210)
merged these closeout records as
`ca8f9842c438eda51f8eb6b5ecc798d111667f04`. Anonymous raw readback
matched all nine changed files at both the source and merge commits.
