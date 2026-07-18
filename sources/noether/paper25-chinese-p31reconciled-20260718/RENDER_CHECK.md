# Render check

The final PDFs were rendered at 180 dpi under `renders/final`: 3 German control pages, 2 Hans pages, and 2 controlled-Hant pages. Every one of the seven PNGs was individually inspected after the final corresponding build.

Result: pass. No clipping, overlap, missing glyph, blank or duplicate page, displaced formula, broken hierarchy, unreadable footnote, or page-number collision was observed. `qa/RENDER_VALIDATION_REPORT.json` binds each inspected PNG by path, byte length, and SHA-256.

This is internal model visual QA, not an external reader, regional-language, community, or human-expert review.

