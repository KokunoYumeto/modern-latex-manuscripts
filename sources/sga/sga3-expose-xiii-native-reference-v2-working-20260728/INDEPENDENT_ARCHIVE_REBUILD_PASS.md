# Independent archive rebuild

Result: **PASS**

Archive maintenance copied the 85-file candidate byte-for-byte and replayed
its self-excluding 83-row manifest. The copied tree remained exact before
and after validation.

Four fresh XeLaTeX passes completed. Passes three and four have identical
console logs. The rebuilt PDF is 32 pages / 245,984 bytes / SHA-256
`CCD709A6D832E7BBC314445D713996428F1BABFE2160A414D9A64E7CA0EA6E6D`.
The two-byte raw PDF difference is regenerated metadata only.

Candidate and rebuild match on:

- extracted text: 32/32 pages;
- decoded content streams: 32/32 pages;
- link sets and rectangles: 32/32 pages;
- named destination map and PDF object counts;
- rendered pixels: 32/32 pages at 150 dpi.

The archive validator is 2,931 bytes / SHA-256
`8F5F81220F40E23122669669E6FD7ED96A3588A62D9F45E4704C91DC1BBE72D9`,
with status `PASS` and `errors[]`.
