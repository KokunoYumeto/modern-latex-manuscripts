# Rendered visual QA — SGA 2 Exposé VI cumulative checkpoint

Status: **PASS** after a fresh final build and complete original-resolution review.

## Target reader

All four final PDF pages were rendered with Poppler at 300 dpi and viewed at original resolution.

| Page | Bytes | SHA-256 | Review |
|---:|---:|---|---|
| 1 | 538746 | 1F32E469BC6301BE37AA48074D1AA8B672369EF469F73C0AB51F47322E2447E1 | title, exact scope table, evidence boundary, definitions, Lemma 1.2, Theorem 1.3 |
| 2 | 569132 | 7422EABF1DAC15EDB2F5A7CA7D16B2F71E9DA05683FD591430F846CBED82F058 | 1.4–1.7; all displayed isomorphisms, spectral terms, equation tags, primes, and page header |
| 3 | 607528 | 69837A67AD8A55688C51F3195F836B67EC540938926E42C6C84458A2EC3052AF | Theorem 1.8, Corollary 1.9, Proposition 2.1, formal-neighborhood maps, all three phi maps, Theorem 2.3 |
| 4 | 336520 | 2D793FB07EFFE97CE34231F30734EF4D615CCA31290340176B9FBE88D9219742 | proof, equation (2.3.1), plain/sheaf H distinction, vanishings, bibliography, page header |

No clipping, overlap, collision, blank output, missing glyph, black square, broken equation tag, or unreadable text was found. Text extraction independently confirms the running header on all four pages; the image viewer visually crops some outer white margin on even pages.

## Direct source controls

Physical source-PDF pages 65–68 were freshly rendered at 300 dpi and viewed at original resolution. They map to printed pages 72–76 and recomposed running pages 57–60. Their hashes match the source renders independently used by the six sealed component reviews.

| Physical page | Bytes | SHA-256 | Key checks |
|---:|---:|---|---|
| 65 | 442826 | 518490B4B58E4CCE31DA1165D5A7EE0EAF381B2A1BE35F934E572EAA76601248 | title, 1.1–1.4, literal X/V supports, theta direction |
| 66 | 590129 | 669D3DF992A8B4FD9509B2C502405BAB58F9407E8C5DC56741178C9D011A994D | 1.5–1.9, comma in (1.6.2), exact-sequence primes and degree shifts |
| 67 | 567481 | 071A1845328F417800B9503B32B772E1AF260ED455CE03D254A55E3765452620 | Proposition 2.1, 2.2 map directions, phi composition, Theorem 2.3 and proof opening |
| 68 | 277157 | 3BF0A0218C253B99FFBD7D6EA8B6BBFC0C46A2AF257BABF597021CB3402EA152 | (2.3.1), universal partial-functor, sheaf H versus plain H, final vanishings, bibliography |

Poppler reported unavailable display-font aliases while rasterizing the legacy French PDF, but every required glyph and formula was visible. The source PNGs remain local evidence only and are excluded from the proposed public payload.
