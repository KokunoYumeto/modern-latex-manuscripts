# current public build PDF formatting QA sweep and continuation

This pass responds to the screenshot issue by treating formatting QA as a batch requirement, not a one-off fix. The current integrated wrapper was rebuilt with smaller chapter headings, ragged-right source/status notes, no boxed monospace source paths, suppressed running headers, and safer line-breaking.

## New content added

- Chapters 52-58 in the integrated reference: formatting QA, PySDR frequency/sampling/IQ, PySDR modulation/coding, Kalman/Labbe implementation bridge, Solà ESKF next source-preserved cut, micro Lie next source-preserved cut, and an updated queue.
- New standalone `pysdr_ukraine_rst_to_tex_core.pdf` module.

## Build status

- integrated current public build XeLaTeX build: pass 1 OK, pass 2 OK; final PDF has 143 pages.
- PySDR standalone XeLaTeX build: pass 1 OK, pass 2 OK.

## Render sweep

- `ukrainian_applied_math_core_current.pdf`: pages=143, open=ok, rendered=143, edge_flags=0
- `pysdr_ukraine_rst_to_tex_core.pdf`: pages=2, open=ok, rendered=2, edge_flags=0
- `ukrainian_applied_math_core_session07_format_checked_combined.pdf`: pages=158, open=ok, rendered=158, edge_flags=0
- `ukrainian_applied_math_core_session07_delta_format_checked.pdf`: pages=19, open=ok, rendered=19, edge_flags=0
- `arxiv_2402_17894_zuazua_wave_ch01_03_ua.pdf`: pages=60, open=ok, rendered=60, edge_flags=0
- `arxiv_2410_15480_event_sensor_fusion_ua_full.pdf`: pages=8, open=ok, rendered=8, edge_flags=0
- `arxiv_2506_19769_sensor_fusion_ua_full_session07.pdf`: pages=19, open=ok, rendered=19, edge_flags=0
- `peeterjoot_antenna_full_ua_session07.pdf`: pages=23, open=ok, rendered=23, edge_flags=0
- `autonomous_robots_correll_perception_navigation_ua_full_session07.pdf`: pages=72, open=ok, rendered=72, edge_flags=0
- `arxiv_1703_02428_roth_robust_filter_ua_full.pdf`: pages=9, open=ok, rendered=9, edge_flags=0
- `arxiv_1812_01537_spark_micro_lie_partial_ua.pdf`: pages=4, open=ok, rendered=4, edge_flags=0
- `blackman_ch04_dynamic_targets_spark_ua_working_ocr_gap_format_checked.pdf`: pages=10, open=ok, rendered=10, edge_flags=0
- `arxiv_1711_02508_sola_eskf_ua_core.pdf`: pages=4, open=ok, rendered=4, edge_flags=0
- `labbe_kalman_ua_practical_core.pdf`: pages=2, open=ok, rendered=2, edge_flags=0

Edge flags are heuristic: page numbers, horizontal rules, or legitimate full-width figures can trigger them. They are used to prioritize visual review, not as proof of defects.

## Log audit

- `src/main.log`: overfull hboxes=78, undefined control sequences=0, missing characters=3, undefined refs=0, undefined citations=0.

The remaining overfull warnings in older appendix tables are small table-width issues, not the gross clipping seen in the Roth screenshot. They are kept in the CSV for later table polishing.

