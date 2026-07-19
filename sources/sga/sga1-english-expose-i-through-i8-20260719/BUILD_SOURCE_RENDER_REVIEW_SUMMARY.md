# Build, source, render, and review summary - SGA 1 through §I.8

- French §I.8 authority: lines 1493--1653 / 7,259 bytes / SHA-256
  `A8885501DFCE9760EA0EC20EB6894F8E45B53E71C131132238F24C7579D0A86D`.
- I.8 fragment: 7,567 bytes / SHA-256 `4C25DB6731B4AC26CBDB65E8F5EA2B289A95CA7ADACAC7DD0464451B81F5BCA8`.
- Public TeX: 18482 bytes / SHA-256 `55671B1DDC22770A056E23D3BB4052CAC9EDF642893B04747D7EF84376CD23C9`.
- Public PDF: 15 A4 pages / 539984 bytes / SHA-256 `76447BE947C25C89D882AD07BE8814109C7943EA31FB2401ED0D3C6D4A597EB9`.

An isolated clean build ran three times. Pass 1 is explicitly the bootstrap
pass and records 62 cross-reference/rerun diagnostic hits; it has no fatal
error. Passes 2 and 3 each have zero warning/error/undefined-reference/box/
rerun hits and produce the final PDF identity above. Full logs are retained
after absolute-path scrubbing, alongside concise receipts and private raw-log
hashes.

Two fresh 180-dpi Poppler render sets contain 15 pages each and match 15/15
byte-for-byte. The public render set totals 5932381 bytes. All pages
were visually reviewed; no clipping, overlap, blank page, missing glyph,
malformed formula, margin collision, broken header/footer, or rotation was
found. The PDF is A4, unencrypted, contains no JavaScript, has populated
metadata, and all 30 fonts are embedded, subset, and Unicode-enabled.

Public machine gates pass 23 CSVs / 400 rows and 10 JSONLs / 145 records with
zero failures. These facts establish only the bounded checkpoint gates, not
publication, rights clearance, peer review, a critical edition, or complete
SGA 1.