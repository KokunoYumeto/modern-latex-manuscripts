# Independent review

Final disposition: PASS after machine-ledger, privacy, and hyperlink-anchor
repairs.

The first independent pass found that terminology row `TERM-008` had 16
fields under a 17-column header. After that repair, exact-set review found
reconstructable private paths wrapped across lines in both purportedly
sanitized logs. After those paths were removed, a further build review found
two duplicate equation-anchor warnings per pass that an earlier zero-warning
statement had missed. The TeX now sets `hypertexnames=false`; all three defects
are resolved in the reviewed identity.

The five evidence CSVs contain 35 records (4 authority, 10 source-alignment,
9 formula, 11 terminology, and 1 source-defect record). They are rectangular,
formula-trigger safe, and primary-ID unique. The two JSONL files contain 13
records / 13 stable IDs. They parse and pass schema, stable-ID, record-ID,
parent/unit/child/cross-reference, revision, and supersession closure.

The source audit passed French lines 2733--2750, printed pages 91--92,
physical source-PDF pages 80--81, running pages 72--73, the implication graph,
local-duality display, equations (2.2)--(2.4), editor's note (4) / page 54, all
`S_q`, `S'_q`, and `Z_q` operations, and the exact continuation cursor at line
2751. The recorded calligraphic `\mathcal F` and calligraphic sheaf-Ext
typography are accepted established SGA2 English typographic normalizations;
semantic objects, degrees, bases, arguments, stalks, support, prime, and
closure are unchanged.

Reviewed target identities:

- TeX: 2,809 bytes, SHA-256
  `FDC13B7A721E456F8AFA5E0B7DB3DE88A5DD4ABE1604513FE3BC47161A31C595`.
- PDF: 217,162 bytes, one A4 page, SHA-256
  `F1F2E78AB82A011D57ABC3EB2E03D3BFB031E4E269434E3F791C8C0B8CF3CE64`.
- Extracted text: 2,547 bytes, SHA-256
  `2B521B55B03C70B5B4FFA08A93B13C894C32F232E2F8CD7D796AFF555628C743`.
- 300-dpi render: 360,723 bytes, SHA-256
  `B556C1FF65BD96B3020B24F1A87A6321E0EEDA887A39C957D66C42E629BACB0B`.

An independent two-pass build exited zero on both passes. Its PDF is 217,162
bytes, SHA-256
`5C966BA019AFF03F117DB88045FAEE5664B588436F53FBF4ADEADA762981B336`.
The independent and target extracted text are byte-identical, and their
300-dpi rendered PNGs are byte-identical. PDF metadata is identical except for
the expected creation/modification timestamps. The fresh first pass contains
only the normal rerun request; the second pass has no real warning, error, or
box diagnostic. Independent pass-log SHA-256 values are
`6F4165C4F5170E1D3AEA4A310EBBB3554B729567001293E13CA52E0CDBF392E6`
and `9C0459DE8AE15E1F74A403ECF573CF5DC7F58A9DADAB61B3DD47EEF3E74C85C9`.

The 27 text candidates pass raw and whitespace/newline-elided scans for
reconstructable private paths and problematic internal project nomenclature.
Raw local TeX and independent-review logs retain local toolchain paths and
remain local-only. Lifecycle fields in the machine ledgers remain explicit
revision state, not private identity or path material.

Before this review edit, exact-set and hash closure passed for 34 files / 
744,293 bytes: the 32-row proposed-public manifest had SHA-256
`45C48CC5073E85B2F11C713C8ED528C7FD8E6CD0D2F8D4DD45D7787F73101A2D`,
and the 33-row self-excluding unit manifest had SHA-256
`131A66F1D9ECD74FD0210ABDCF69ED72EA739D453C93317B84FE2AA2CA1202D7`.
This review edit intentionally invalidates those two manifests. They must be
regenerated and subjected to a final no-write exact-set/hash/privacy audit
before archive handoff. This PASS seals the substantive unit; it does not
claim publication, remote archival acceptance, or public readback.
