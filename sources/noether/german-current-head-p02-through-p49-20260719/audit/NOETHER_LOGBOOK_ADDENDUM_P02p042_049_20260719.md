# Noether publication logbook addendum: P02 pp. 42-49
+## 2026-07-19: P02 printed pp. 42-49 current-head complete-page audit

### Authority and method

The pass began from `Noether_LocalCodex_20260719_P02p035_041_CurrentHeadAudit_COMPLETE`, TeX SHA-256 `DBCB6CDFA5BCE6ED4DDDF76A4EBC406BDE31164B5EA7E0BF435D75D829CC7BCF`. Revision labels were not treated as authority. The controlling witness was the complete original Paper 2 publication scan. Every printed page from 42 through 49 was opened at native 600 ppi and in three overlapping 2x enlarged strips. Printed p44 also received a focused enlargement of the auxiliary-variable hat.

OCR and inherited audit text were used only for navigation. Every promoted reading was taken from the visible source page.

### Page dispositions and repairs

- p42: restored the pair-wide hat over `ub^2` and source underlines on principal expressions 1)-2).
- p43: restored the corresponding pair-wide hat and source underlines on principal expressions 3)-9).
- p44: complete-page no-patch. Focused source inspection confirms `w=x\widehat{u}b`; a wider `\widehat{xub}` reading is rejected.
- p45: restored the Section 7 source hierarchy: upright bold section number and italic title. The previously repaired source-local `*)` note survives.
- p46: complete-page no-patch.
- p47: removed a non-source comma in formula (6.); `s_\nu^3u_\nu s_x` is one product, not a stray expression followed by a separate equation.
- p48: restored source hierarchy for Sections 8 and 9; formulae (7.)-(9.) and matrix geometry otherwise survive.
- p49: restored source hierarchy for Section 10; the dense reduction and formula (9.) otherwise survive.

All six grouped repairs were found and adjudicated by LocalCodex from the original source. The user supplied the source-first, complete-page, durable-logbook requirements but did not supply any of these symbol readings.

### Build, render, and containment

XeLaTeX passed twice. The cumulative remains 466 pages. The final compile scan reports zero fatal errors, emergency stops, undefined references, rerun warnings, overfull boxes, or underfull boxes; only pre-existing font substitution warnings remain.

Whole-document PDF text comparison against the predecessor identifies exactly output pp. 13-17 as changed. Same-renderer image hashes identify pp. 13-17 as changed and pp. 11-12 plus 18-22 as pixel-identical. Final changed pages were regenerated from the sealed PDF with a second renderer and opened visually at original detail. No clipping, overlap, broken glyph, or page-boundary defect was found.

### Web-package disposition

`Web_P04_p118_143_CurrentHeadAudit_20260719_COMPLETE.zip` is a content duplicate of the eighteen P04 repair groups already present under `CO-W04-P04-001` through `CO-W04-P04-018`. Its cumulative was not imported. This is corroborating evidence, not a new authority head.

### Failures and recovery

1. The first mechanical ledger-merge attempt used a null synthetic key for append-only files and stopped before producing a merged ledger set. Recovery: recopy the sealed predecessor ledgers, use keyed idempotent merges only where stable IDs exist, append the QC/hard-math rows explicitly, then validate all counts and duplicates.
2. The first final-QA wrapper completed both XeLaTeX passes but failed while invoking the bundled `pdfinfo.cmd` wrapper. No TeX repair was lost. Recovery: take page count from the XeLaTeX log, use MiKTeX `pdftotext.exe` for whole-document containment, and use `mutool.exe` for final render regeneration.
3. Cross-rasterizer image hashes differed on every page despite identical content. Recovery: preserve cross-rasterizer hashes only as regeneration provenance and make pixel-reconvergence claims exclusively from the same-renderer before/after set.

### Repeatable lessons

- Underlining can encode which expression a long reduction develops; it belongs in the source audit even when formula strings are otherwise complete.
- Hat extent must be checked at the exact glyph boundary. A visually plausible wider hat can be mathematically false.
- A comma inside dense displayed algebra can change one product identity into two disconnected statements.
- Pixel equality is meaningful only when renderer, resolution, and settings are held constant.
- Generated ledgers must be rebuilt from a sealed baseline after any failed merge attempt; partial script state is not a valid continuation base.
- Web work is merged by source-backed content survival, never by filename or revision label.

### Cursor

This pass closes P02 pp. 42-49. The complete edition stands at 745/753 closed body-page keys (98.94%). The sole remaining body band is P02 printed pp. 50-57, assigned to Web. The author remains incomplete until that return is source-adjudicated on the live head and the 753-key validation reaches zero open rows.

