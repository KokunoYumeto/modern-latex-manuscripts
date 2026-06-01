# current public build final QA-checked package

Generated: 2026-06-01 12:41:40 UTC

This package responds to the formatting-defect issue as a batch QA problem, not a one-page fix. The deliverable set uses format-checked replacements where the earlier PDFs showed visible jank.

## What was continued

- Integrated reference continued to current public build, with chapters on PDF format QA, PySDR Ukrainian RST-to-TeX conversion, code/agent QA tasks, and the next practical queue.
- PySDR Ukrainian selected RST was converted into a larger TeX/PDF module for SDR, sampling, I/Q, frequency domain, filters, noise, modulation, pulse shaping, synchronization, channel coding, and SigMF/IQ file handling.
- SDR survey standalone was rebuilt with the acronym table as a full-width breakable table instead of a clipped two-column table.

## Formatting fixes included

- Zuazua chapters 1-3: replaced the earlier running-header layout that clipped long Ukrainian chapter titles.
- Peeter Joot antenna/RF module: fixed long code/argument spill and over-wide emphasized/underlined text.
- Autonomous Robots module: rebuilt with safer page-breaking and line-breaking.
- Blackman working OCR draft: kept the XeLaTeX/fontspec Cyrillic build, avoiding missing glyphs.
- SDR survey: rebuilt the acronym table to avoid the page-2 clipping seen in the old standalone.

## Deliverable PDFs

| File | Pages | Notes |
|---|---:|---|
| `ukrainian_applied_math_core_current_qachecked.pdf` | 143 | integrated reference, current working core |
| `pysdr_ukrainian_selected_tex_current_full.pdf` | 100 | full PySDR Ukrainian selected RST-to-TeX module |
| `arxiv_1804_06564_sdr_survey_ua_core_format_checked.pdf` | 6 | format-checked SDR survey core |
| `arxiv_2402_17894_zuazua_wave_ch01_03_ua_format_checked.pdf` | 40 | format-checked wave controllability chapters |
| `arxiv_2410_15480_event_sensor_fusion_ua_full.pdf` | 8 | event-based sensor fusion / odometry |
| `arxiv_2506_19769_sensor_fusion_ua_full_session07.pdf` | 19 | multi-sensor fusion survey |
| `peeterjoot_antenna_full_ua_session07_format_checked.pdf` | 23 | format-checked antenna/RF module |
| `autonomous_robots_correll_perception_navigation_ua_full_session07_format_checked.pdf` | 45 | format-checked robotics perception/navigation module |
| `arxiv_1703_02428_roth_robust_filter_ua_full.pdf` | 9 | robust Student-t filtering module |
| `arxiv_1812_01537_spark_micro_lie_partial_ua.pdf` | 4 | Spark micro-Lie partial module |
| `arxiv_1711_02508_sola_eskf_ua_core.pdf` | 4 | Solà ESKF core start |
| `labbe_kalman_ua_practical_core.pdf` | 2 | Kalman practical core bridge |
| `blackman_ch04_dynamic_targets_spark_ua_working_ocr_gap_format_checked_working.pdf` | 10 | working OCR gap draft; needs source-level review before being treated as complete |

## QA scope and limits

The package includes render contact sheets and CSV logs from the formatting sweeps. This is build/layout QA: it checks renderability, obvious clipping, missing Cyrillic glyph problems, unbreakable source-path boxes, and gross table overflow. It is not a mathematical proofread against the original papers.

The root directory may still contain older PDFs from previous turns. Use the PDFs inside `standalone_pdfs/` here as the current checked set.

