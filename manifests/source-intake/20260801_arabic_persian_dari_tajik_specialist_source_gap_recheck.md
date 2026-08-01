# Arabic, Persian, Dari, and Tajik Specialist-Source Gap Recheck

Status: `PASS_SEARCH_COMPLETE__SPECIALIST_SOURCE_GAPS_REMAIN_OPEN`.

This receipt revisits the unresolved source pointers in the historical
packages 458-459 intake after the two SireJeff rows were closed separately.
It tests the current public source-body archive rather than assuming that a
July pointer remains open merely because the original packet lacked bytes.

## Public Surface Replayed

The current Interlanguage head is
[`10.5281/zenodo.21739451`](https://doi.org/10.5281/zenodo.21739451), under
concept DOI [`10.5281/zenodo.21124403`](https://doi.org/10.5281/zenodo.21124403).
The inspected object was
`06_Interlanguage_OtherPC_SourceBodies_RTL_Persianate_Arabic_20260707.zip`:

- 884,720,731 bytes;
- MD5 `916409ae7791ae5dd917d64524a36bf3`;
- 1,047 outer ZIP entries;
- 212,128-byte central directory.

Anonymous HTTP byte ranges read the central directory and the selected
members directly. No full 884 MB download or persistent local copy was made.

## Exact Source-Object Replay

Eleven unique source objects totaling 92,657,225 bytes were decompressed,
CRC-checked, SHA-256 hashed, and searched. Nested ZIP text members were read
in memory.

| Object | Bytes | SHA-256 | Nested entries / text scanned |
| --- | ---: | --- | ---: |
| ArabicMath source ZIP | 86,828,566 | `A803C69A82D5F9AC4C884B278761CE5C9BAB821DD3119BE92FB9CAD8D7CD00F4` | 165 / 2 |
| Omarittwahi Arabic MathJax ZIP | 89,854 | `EBFC433392C879D1283CCDF122024DA625990347E4AA39AE0BEFD7F4FC7E87C2` | 42 / 12 |
| Babel Arabic sample TeX | 17,264 | `DBB194BF186C76242EBCD9082E592107F5DC326CA45AB4DCCDF06BF6C78228DE` | direct / 1 |
| xepersian source ZIP | 203,058 | `21F4EC54F3AB18B299CB650F6D2CDE099656B3F2BF25C17047DF6D4892F3AD0E` | 34 / 7 |
| Babel Farsi sample TeX | 2,105 | `636B8FDD3D592CA88369B90B606F5923E175E58189AFCFC96410E1B069DE3F1D` | direct / 1 |
| SireJeff Persian main TeX | 6,280 | `AA4207AE05BA1804FFB3BBE8265954571BE276E75A8CB7A1656A72ED92417427` | direct / 1 |
| SireJeff Persian source ZIP | 2,007,400 | `EEEE28E88CA465F0A125AFE056F6203B84C138EB44114867D8E49F3C3344252C` | 44 / 32 |
| Arabic forensic-linguistics false-positive TeX | 56,547 | `F3AA052D1300715AD637B337FEBC2DB99C695073F55864C2B35413D372FA3CA6` | direct / 1 |
| Arabic LaTeX manual TeX | 29,369 | `7024EF38569832AFF7555EE8D5E430C6A598318D14F283E02B9B714CACD44E77` | direct / 1 |
| Persian 3Blue1Brown linear-algebra source ZIP | 2,006,520 | `4D93CE90754B28ECC743CE5BB1ED62F0325F99A38D52E90DECC10DD1C3FFF59C` | 44 / 32 |
| Persian Gilbert Strang source ZIP | 1,410,262 | `1956A3821B88F2AFDA31A0DA184988DDDED44751A44E48068E6A06FCA091437B` | 42 / 21 |

The exact search vocabulary covered English `invariant` and `noether`, Arabic
forms for constants/invariants and Noether, Persian `ناورد`, `پایا`, `همورد`,
and `نوتر`, and Cyrillic `инвариант`, `ноэтер`, `нётер`, and `нотер`.

There were 78 lexical matches. Context review rejected all 78 as specialist
source hits:

- xepersian matches are command-name, macro-documentation, or substring hits;
- SireJeff and 3Blue1Brown matches use ordinary senses such as fixed,
  constant, prove, end, or stable;
- Gilbert Strang matches likewise concern elementary linear-algebra constants,
  fixed vectors, proofs, or substring overlap;
- the explicitly false-positive Arabic TeX concerns forensic linguistics and
  stylistic constants.

The ArabicMath, MathJax, Babel samples, direct SireJeff master, and Arabic
LaTeX manual produced no lexical hit at all. No inspected object is an Arabic
or Persian invariant-theory/Noether source.

## Dari and Tajik Extension Check

The same 1,047-entry central directory contains 204 Tajik-shaped paths and 49
Dari-shaped paths.

- Tajik-shaped paths contain 186 files: 61 TXT, 53 PDF, 36 HTML, 19 Markdown,
  6 JSON, 6 ZIP, and 5 CSV. The six ZIP paths are duplicate placements of two
  Persian linear-algebra source archives, not Tajik editable source.
- Dari-shaped paths contain 44 files: 16 PDF, 13 HTML, 13 TXT, and 2 Markdown.
  There is no TeX or source-archive entry.

These witness and reader files remain useful. They do not close a request for
direct Dari or Tajik mathematical TeX/source packages.

## Disposition

The following exact gaps remain open:

- Arabic invariant-theory TeX/arXiv source;
- Persian invariant-theory or Noether-topic TeX/arXiv source;
- Dari TeX/arXiv/invariant-theory source package;
- Tajik abstract-algebra or native TeX source package.

This is a bounded negative source-custody result, not evidence that no such
source exists on the web or in a later handoff. Existing Arabic, Persian,
Dari, and Tajik PDFs and source bodies remain valid at their documented
scope. No GitHub payload duplication or Zenodo mutation is warranted merely
to record the open gaps.

The mandatory locked helper appended decision
`EG-ARCHIVE-ARABIC-PERSIAN-DARI-TAJIK-SOURCE-GAP-RECHECK-20260801-0001`.
The controlling shared log now has 429 unique records / 2,701,956 bytes /
SHA-256 `5F671F9C209E1F21995743E71F13680BACF1CAE3B6FB47ABC9DFEB374A9DB656`,
with `errors=[]`. The standalone record is 6,498 bytes / SHA-256
`55AA7C626C6F4B769F9C040F32A1AE861FBB9C334737900C6AF513F013117AEE`.

GitHub PR [#212](https://github.com/KokunoYumeto/modern-latex-manuscripts/pull/212)
merged the seven-file receipt update as
`1cef0c253f69619054a5ee814866742c1101f936` from source commit
`f796c81f77f0a84119acd7de8ddee7d4d7159fa0`. Anonymous commit-pinned
readback matched 7/7 committed blobs at both commits. The canonical
path/bytes/SHA-256 aggregate is
`5AC234D51CC3453775A31526F33682EB14279690D985E29366EC3BC529D6EC61`.
