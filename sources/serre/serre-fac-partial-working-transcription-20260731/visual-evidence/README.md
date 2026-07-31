# FAC source-image evidence

This directory contains the four scan-derived crops that were actually opened
during the current FAC source work. They are retained as pixels because the
crop work itself is useful verification evidence.

The filenames encode the zero-based source index, requested rasterization
scale, and normalized vertical crop interval. Each crop spans the full rendered
page width. `VISUAL_EVIDENCE_INDEX.csv` records the corresponding PDF page,
printed page, full rendered-page dimensions, exact integer pixel box, crop
dimensions, file identity, and linked TeX page marker.

The PNG files carry 96 dpi in their embedded metadata. That metadata value is
not the source-generation scale. The separate `render_dpi` field records the
actual rasterization request: 300, 600, or 900 dpi.

The complete source PDF is not included.

