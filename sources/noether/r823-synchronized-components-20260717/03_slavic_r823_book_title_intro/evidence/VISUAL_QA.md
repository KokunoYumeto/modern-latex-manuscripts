# Visual QA record

All four final PDFs were rendered at 144 DPI into three page images and a three-page contact sheet. The contact sheets were inspected at original resolution.

| Target | Pages | Result |
|---|---:|---|
| Ukrainian | 3 | Pass: title, complete two-page contents, introduction, and Chapter I opening visible; no clipping or overlap. |
| Russian | 3 | Pass: title, complete two-page contents, introduction, and Chapter I opening visible; no clipping or overlap. |
| Interslavic Latin | 3 | Pass: title, complete two-page contents, introduction, and Chapter I opening visible; foreign-title islands and math preserved. |
| Interslavic Cyrillic | 3 | Pass after final deterministic regeneration/rebuild: no clipping or overlap; Latin foreign-title islands and math preserved. |

The machine audit separately verifies three pages per target, title extraction, embedded fonts, complete structural row counts, and zero build-log hits for overfull/underfull boxes, undefined references, missing characters, or TeX/package errors. See `BUILD_AND_STRUCTURE_AUDIT.json`.

This is internal visual QA only, not external or community certification.
