# SGA5 R9 independent exhaustive-reference audit

Audit mode: fresh, read-only replay of the completed R9 successor. The auditor
did not edit the reader or evidence and did not send any archive or Claude
handoff.

Final disposition: **PASS**

No errors were found.

## Replayed controls

- Convention v2 exhaustive SHA-256:
  `F5BDC71164EDA34128E584E4F117993D31EE07698E329986CF5013519E5CA8CC`.
- 1,101 targets have unique stable IDs and LaTeX labels, occur exactly once in
  TeX and AUX, resolve to compiled PDF destinations, and have zero page
  mismatches.
- 1,578 edges have an exact TeX-wrapper multiset, zero missing or extra
  wrappers, zero target/stable-ID failures, and zero PDF-annotation deficits.
- 1,460 candidates have unique IDs and final dispositions. The three legacy R8
  records sharing source-line/text metadata were checked and correspond to
  three distinct `Exposé X` occurrences on that line.
- The complete prelink inventory replays as exactly 720 internal edges, 945
  declarations/tags, 268 external-work citations, 179 typography/layout/
  geometry values, and 6 unavailable source targets.
- The postlink replay contains exactly 1,398 ordered noninternal residuals at
  exact current-source coordinates, with zero unresolved, unadjudicated, or
  internally resolvable unwrapped occurrence.

## Compiled reader

- 309 pages, 2,343 named destinations, and 1,614 of 1,614 link annotations are
  valid internal `/GoTo` annotations.
- All 35 fonts are embedded, subset, and Unicode-mapped.
- Three-pass AUX SHA-256:
  `B01ED5F3F02DC8229FBDE4972C7F455BA15A6215E2D073412E306E4618E9BE4D`.
- Three-pass OUT SHA-256:
  `A6BD156ED6848286A0EFDF618146DDB9452E519E7238EAD4B4F7C2DA03118141`.
- Three-pass decoded page-content SHA-256:
  `39703C53954A1495A374DEA4E4BD61F8F6BB2ADA3CC8B028059C8C4D40B31B6B`.
- Fresh R8/R9 flow-text extraction is byte-exact at SHA-256
  `4D63AF274598A64338FFF2F60CD30C9D8108B55E438D17C238578E4F542A7EB9`.
- Fresh R8/R9 layout-text extraction is byte-exact at SHA-256
  `5A5CDF64D1DE92A18A2AB5086885F8E4F77A72143A222545AB0C88DF0D7662D8`.
- All 20 rendered page-pair metrics and five contact-sheet identities replay;
  visual inspection found no defect.

## Authoritative successor identities

- TeX SHA-256:
  `765067892F2F208015235BF548F2F8FA03E56DA63D4ED470CF5B67F08CA1CE2F`.
- PDF SHA-256:
  `EF93294085E06FFCF1F95DD8D2DEBB14DAD22FED44D967E09D3BAB24F5C78F6E`.

This PASS is limited to the exhaustive internal-reference retrofit and its
preservation/compiled-delivery gates. External citations and unavailable
same-work targets remain intentionally unlinked and fully ledgered; they are
not unresolved internal-reference backlog.
