# Render/Script Validation Preflight - 2026-06-30

This local preflight records render and script obligations before future TeX/PDF or sidecar claims. It is not a render log, review result, or completion claim.

## Summary

- Render/script rows: 15
- CJK rows: 2
- RTL rows: 3
- Latin rows: 2
- Cyrillic or sidecar rows: 4
- Mixed/TBD script rows: 6
- Render jobs started: 0
- PDFs created: 0
- Visual inspections completed: 0
- Script-sidecar validations completed: 0
- Network actions performed: 0

## Rows

| Lane/cohort | Profile | Direction | Render status | Required visual/script roles |
| --- | --- | --- | --- | --- |
| Slavic Latin/Cyrillic Sidecar Reference | `latin_cyrillic_dual_script_sidecar` | ltr | not_started_preflight_only | latin_cyrillic_sidecar_validator |
| African Deep-Gap Cohort | `african_local_script_scope_tbd` | mixed_or_tbd | not_started_preflight_only | none routed yet |
| Arabic | `rtl_arabic` | rtl | not_started_preflight_only | rtl_tex_pdf_reviewer |
| East/Southeast Asia and Pacific Cohort | `east_southeast_asia_pacific_script_scope_tbd` | mixed_or_tbd | not_started_preflight_only | none routed yet |
| Persian/Farsi (Iran) | `rtl_persian_farsi` | rtl | not_started_preflight_only | rtl_or_script_reviewer |
| French | `latin_roman_french` | ltr | not_started_preflight_only | french_tex_pdf_visual_reviewer |
| Japanese | `cjk_japanese` | ltr | not_started_preflight_only | japanese_cjk_tex_pdf_visual_reviewer |
| Methodology / Interlanguage Access Cohort | `interlanguage_or_constructed_script_governance` | ltr_or_tbd | not_started_preflight_only | none routed yet |
| Pan-Turkic Adjacent Cohort | `pan_turkic_multi_script_scope_tbd` | mixed_or_tbd | not_started_preflight_only | script_standardization_reviewer |
| Dari/Persian (Afghanistan) | `rtl_dari_persian` | rtl | not_started_preflight_only | rtl_or_script_reviewer |
| Simplified Chinese | `cjk_han_simplified` | ltr | not_started_preflight_only | chinese_tex_pdf_visual_reviewer |
| Source-First Reference Textbook Cohort | `source_reference_mixed_scripts` | source_dependent | not_started_preflight_only | none routed yet |
| South Asian / Hindustani / Indic / Dravidian Cohort | `south_asia_multi_script_scope_tbd` | mixed_or_tbd | not_started_preflight_only | none routed yet |
| Spanish | `latin_roman_spanish` | ltr | not_started_preflight_only | none routed yet |
| Tajik Cyrillic | `cyrillic_tajik_source_discovery` | ltr | not_started_preflight_only | none routed yet |

## Boundaries

- This matrix does not create or inspect rendered PDFs.
- Render/script checks must be performed after upstream source-note or manual-review gates clear.
- Local mechanical preflight does not replace native, visual, script, educator, or community review.
- No source text, source-language term strings, credentials, reviewer returns, or accepted corrections are copied here.
- No network action was performed.
