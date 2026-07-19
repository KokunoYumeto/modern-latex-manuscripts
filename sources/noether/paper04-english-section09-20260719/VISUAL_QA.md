# Visual QA

The two packaged page images are fresh 200-dpi renders of the locked reader.
They are also byte-identical to independently rendered pages from the
isolated three-pass rebuild. The contact sheet is a navigation aid. Each page
was reviewed at original resolution after the final source repair.

| Page | PNG bytes | SHA-256 | Isolated-render comparison | Visual result |
|---:|---:|---|---|---|
| 1 | 620,828 | `6DC8E111C22AC15F5233983F3A29F724B66E982BFCE043C7C893A46BAE8935D4` | byte-identical; AE 0; RMSE 0 | PASS |
| 2 | 465,252 | `7F49F29DA0853E54E19EF521D1C43A3EE83A8F3381E970152763BF4DDFB8A635` | byte-identical; AE 0; RMSE 0 | PASS |

Both pages are 1654 by 2339 pixels. The 3308 by 2339 contact sheet is 548,973
bytes with SHA-256
`7B5C8A84DCB77F2ED8F6CF3FC8CD6DD3A88ED075747D3986F3DA95997F09BBDD`.

No clipping, overlap, broken glyph, black box, missing symbol, malformed
matrix pair, displaced note call, unreadable note, or broken transition was
found. The labels `1)`, `2)`, and `3)` and both print-matched note-call
positions are visible.
