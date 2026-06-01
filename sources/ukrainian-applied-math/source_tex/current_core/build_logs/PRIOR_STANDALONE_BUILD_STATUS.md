# prior build standalone build status

All four staged auxiliary local run-output standalone targets compile under XeLaTeX in this package after small mechanical patches.

Primary copies are in `pdf/auxiliary_standalones/`; release-named copies are also in `paper_tracks_pdfs/session04/`.

| Target | Release-named PDF | Notes |
|---|---|---|
| sensor_fusion_2506_19769 | `paper_tracks_pdfs/session04/arxiv_2506_19769_sensor_fusion_ua_auxiliary local run.pdf` | Full IEEEtran project; patched `\IEEEPARstart` for XeLaTeX font compatibility. |
| sdr_survey_1804_06564 | `paper_tracks_pdfs/session04/arxiv_1804_06564_sdr_survey_core_ua_auxiliary local run.pdf` | Patched missing original figure with placeholder; citations remain partially unresolved because this batch did not include a matching bibliography bundle. |
| zuazua_ch01_wrapper | `paper_tracks_pdfs/session04/arxiv_2402_17894_zuazua_ch01_ua_auxiliary local run.pdf` | Chapter wrapper compiles; references/citations into later original chapters are unresolved, as expected. |
| antenna_maxwell_wrapper | `paper_tracks_pdfs/session04/peeterjoot_antenna_maxwell_ua_auxiliary local run.pdf` | Local macro shim used for Peeter Joot macros; original repo style files should be used for production. |

The raw auxiliary local run output is preserved under `incoming_auxiliary_output/ukrainian_output_20260601/`.
