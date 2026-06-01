# prior build fixed PDF QA sweep

| PDF | Pages | Flagged pages | Flags |
|---|---:|---:|---|
| prior_format_qc | 144 | 0 |  |
| delta_format_checked | 19 | 0 |  |
| zuazua_ch01_03_format_checked | 34 | 1 | blank_or_low_content |
| sensor_fusion_2410_event | 8 | 0 |  |
| sensor_fusion_2506_full | 19 | 0 |  |
| antenna_peeterjoot_format_checked | 23 | 1 | blank_or_low_content |
| autonomous_robots_correll_format_checked | 45 | 0 |  |
| roth_robust_filter | 9 | 0 |  |
| spark_micro_lie_partial | 4 | 0 |  |
| blackman_working_ocr_gap_format_checked | 10 | 0 |  |

The fixed standalone builds replace the earlier Zuazua, Peeter-Joot antenna, and Correll robotics PDFs where visual render checks showed long running headers, wrapped code/image-argument debris, or unnecessary blank chapter pages. Conservative flags may still appear on intentionally sparse title/TOC pages; rendered pages are included in `renders/`.
