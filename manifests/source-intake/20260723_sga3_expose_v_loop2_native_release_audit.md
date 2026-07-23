# SGA3 Expose V Loop 2 native release audit

Status: **PASS**

This receipt covers the compact, rights-curated package at
`sources/sga/sga3-english-expose-v-loop2-native-r2-freeze2-20260723`.

## Reader

- PDF: 51 pages / 361,493 bytes / SHA-256
  `E4682CBED71922AF8C1C2851D8B69F2CF6A1E089CC4CC52EDF0318708F65F6F2`.
- Editable master: 7,202 bytes / SHA-256
  `92AB24AB2E104618AB4E97AC4A2F23554BECB741258F7E9739EC463E6B99C37E`.
- PDF replay: 350 named destinations, 411 internal GoTo actions, zero
  external actions, zero invalid rectangles, and zero image XObjects.
- Reference and diagram closure: 273/273 targets, 333/333 semantic edges
  backed by actions, and 66/66 native diagrams.

## Compact package

- Outer surface: 8 files, with 7 exact self-excluding checksum rows.
- Source/evidence ZIP: 14,089,511 bytes / SHA-256
  `0B72613DAF10E95429FC3056A7739216978C7E3779AA9E7721E8D9C2A0375726`.
- ZIP replay: 229/229 safe unique members and 227/227 represented-member
  identities exact.
- Machine replay: 17 CSVs / 19,153 rows, 8 JSON files, and 6 JSONL files /
  4,753 records. Parsing, rectangularity, whitespace-normalized formula
  safety, and privacy checks pass.

## Rights boundary

The archive contains zero source-PDF pixel witnesses. Public CSV and JSONL
ledgers retain 66 parent-PDF identities, source locators, dimensions, crop
hashes, linked TeX positions, native replacements, and QA dispositions. The
actual pixels are classified `rights_blocked_not_public`.

## Clean rebuild

The exact ZIP was extracted without access to the withheld source-PNG tree.
Three XeLaTeX passes completed with zero selected diagnostics. The rebuilt
PDF differs only in generated PDF identity bytes:

- rebuilt PDF: 361,497 bytes / SHA-256
  `4C174E7825154F6FC7E35E867E4D027CA1317EE2F5579E1BDF3F1194A90A6CD2`;
- pages, destinations, links, image-object count, and extracted text are
  identical;
- 51/51 independent 120-dpi page renders are byte-identical.

Pages 1, 24, 49, and 51 were directly inspected after the compact-package
rebuild and passed.

## Claim limits

This is complete only for SGA3 Expose V. It is a bounded machine-assisted
working translation and native-diagram reconstruction, not complete SGA3,
a critical edition, mathematical certification, independent human peer
review, blanket rights determination, or accessibility certification.
