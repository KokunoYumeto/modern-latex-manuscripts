# SGA5 numbered-print coverage topology reconciliation

Status: `METADATA_ONLY_TOPOLOGY_RECONCILIATION`

Archive maintenance reviewed the append-only local control
`SGA5_FRENCH_AUTHORITY_APPEND_ONLY_COVERAGE_RECONCILIATION_20260722.md`
(11,161 bytes, SHA-256
`9FA595236A3FF82F433E1DC46540B275E6B79FB3D377144A59E21E73A798F671`).
The control resolves an old bookkeeping conflict between an early p.65/p.103
snapshot and the later page-keyed body ledger. It does not repeat the full
scholarly audit and does not authorize a new SGA5 reader release.

## Independent archive replay

Archive maintenance rehashed the controlling inputs and independently parsed
the current body ledger:

- French workpass: 848,165 bytes, SHA-256
  `791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28`.
- Original-print witness: 62,025,563 bytes, SHA-256
  `B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA`.
- `CERT_LOG.md`: 1,327,593 bytes, SHA-256
  `272F6ED7DAA2DFF5E35803DFD3D04493E8CB838AE5A7F1A1447CE916D263D4B3`.
- `ERRATA_LNM589.md`: 40,725 bytes, SHA-256
  `03F71A5AE22CA1F4A2CBB1B24E2C3E3181CB24ABA637B7608560DFA7A3B90C58`.
- Current English workpass: 798,096 bytes, SHA-256
  `5A79546320606564E0FEF609A13E7F71D42487281325C4CCF97DC20990B7F4C4`.

The page-table parse returned exactly 480 rows, 480 distinct integer keys,
minimum 1, maximum 480, with no missing or duplicate key. Those rows account
for the ten physical exposes in this print witness: I, III, III B, V, VI,
VII, VIII, X, XII, and XV. Nonconsecutive expose numbering is native to the
witness and is not evidence of omitted physical units.

The French TeX then contains exactly 56 terminological index entries and 52
notation-index entries. Their line spans are 15304-15359 and 15362-15413,
respectively. The last numbered-print item is `|X|` at French line 15413;
line 15415 is `\end{document}`.

## Private visual witness audit

Original-print PDF pages 493-496, corresponding to printed pages 481-484,
were freshly rendered at 160 dpi and inspected at original resolution. Each
render is 1,360 x 1,760 pixels, rotation 0, full-page bounding box. The four
private render identities are:

| Printed page | PDF page | SHA-256 |
|---:|---:|---|
| 481 | 493 | `2730E67954639C85E9042BA1F9720C56B9B708503510B2BA137F3EAD851D6912` |
| 482 | 494 | `F0FAF8FC67B8408494F7FA8F193904B470138576525EDDDFBB5B6BDE182BE0C2` |
| 483 | 495 | `F9F998EC4F9941A6B380D34ADF87182BAEDBCD833AF33B391422456662B048F1` |
| 484 | 496 | `6D2AD9CA942D5676AC6EFA00588FE647AD0BDC6D706CF682848FBF2B72EB7123` |

The ordered first/last anchors and page transitions agree with the TeX
spans. The source renders and parent PDF are rights-blocked and are not
copied into GitHub or Zenodo. This receipt records their parent hash, page,
dimensions, DPI, rotation, full-page scope, and derived crop hashes so the
visual check is not silently omitted.

## Correct public interpretation

Within the bounded numbered-print authority, printed pages 1-484 are
topologically accounted for: 480 page-keyed body pages plus four freshly
controlled index pages. The two indexes contain 108 represented entries.
There is no honest next numbered expose or numbered page in this witness.

This is not a second symbol-by-symbol audit of the 480 body pages. Confidence
in body content still depends on the preserved page-keyed ledger and its
disclosed errata. Matching English spans establish structural presence, not
semantic recertification of every translated line. The unnumbered front
matter on PDF pages 1-12, other editions, rights, accessibility, packaging,
and publication readiness remain outside this control.

No source, TeX body, PDF, image, status file, shared decision log, or Zenodo
record is copied or mutated by this intake. SGA remains an incomplete working
archive at the volume-program level, not a critical edition or whole-SGA
completion claim.
