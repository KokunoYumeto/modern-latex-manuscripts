# Rendered visual inspection — Noether Paper 33 Chinese rebase

Final visual status: pass.

Poppler rendered all final pages at 150 dpi. Every one of the 7 final PNG pages was opened and inspected individually at original detail:

- German control: pages 1--3;
- `zh-Hans-CN`: pages 1--2;
- controlled `zh-Hant`: pages 1--2.

Inspection criteria: clipping, overlap, blank or duplicate pages, missing or substituted glyphs, broken hierarchy, displaced footnote markers, unreadable footnotes, split or malformed matrices, page-number collisions, accidental carryover from Paper 34, and bad sentence fragments at page boundaries.

Results:

- German pages 1 and 2 carry the full article structure, both matrices, and both footnotes cleanly. German page 3 is intentionally sparse and contains the article's closing paragraph; it is not blank.
- Hans page 1 contains title/citation, both footnotes, the first matrix, and the complete first reduction discussion without collision. Hans page 2 opens at a valid paragraph transition, contains the second matrix and complete radical/Schur/Wedderburn discussion, and has no missing glyphs.
- The first controlled-Hant render placed the two-character tail `下。` alone at the top of page 2. An ineffective page-height attempt was discarded. The final file instead begins page 2 with the complete direct-product paragraph and keeps `意義下。` together. Both final Hant pages were rerendered and reinspected; they pass.

Final rendered-page SHA-256 values:

| Page | SHA-256 |
|---|---|
| German 1 | `03FD06E19969719D1C9674DC310F60D421965197FAAC6653BFFF816D831C6A79` |
| German 2 | `04C6710BC290831D41F4BAE0FA34B7BD1F479670A999ECB56BCF2347CBA86F82` |
| German 3 | `B2E350D8D64B8C01958C5175765F1FA9F8B63B4687B73A511FC13990D3977EB7` |
| Hans 1 | `DE949F0942DA44DA88F5284CAA5A0A15E159875A184A9E9B1CBBD312F4A8B0EA` |
| Hans 2 | `6B0CEF4A52EEAD6939B080C5DD6A3E0F523CDE118F645FC6277D32094304C23A` |
| Hant 1 | `9F309039B093538F6B58CA36C48A5E692E93741369B2BD2AA720437200218E6F` |
| Hant 2 | `FE06C37AF4A8BDF8C1F45F427C86F7D6DC1AF7A68EB10889D7B7EB1928DF6B74` |

The inspection is an internal editorial observation. No external or community visual acceptance is claimed.
