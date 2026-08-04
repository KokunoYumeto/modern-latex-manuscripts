# Build report — Noether Paper 33 Chinese rebase

Final build status: pass.

All three standalone artifacts were compiled with MiKTeX-XeTeX 4.18 (MiKTeX 26.5). Each received two `-interaction=nonstopmode -halt-on-error` passes after its final source or layout change.

| Edition | TeX SHA-256 | PDF SHA-256 | Pages | Log scan |
|---|---|---|---:|---|
| sealed-P31 German control | `BC9AC1A28C0496840DB0EE1DF3DD40650B9E2CD40B91EA430056BC1EE0253ECC` | `DF6E46CDC7B448EF04A376C2DBC8A2A5C176C56AAB1145AD1DB4FBA2C72B6458` | 3 | clean |
| `zh-Hans-CN` | `0DCDF37EDA633DC5CFD9858BAE1D4D66C689D25CEA3EF7F745D0A721C9A06178` | `9294243E8EF11B2FA00CCEC66323D7670C50188A4F24560852D75670B690CF34` | 2 | clean |
| controlled `zh-Hant` | `3C17E3A250892BF2FB418F3796196E1A8DB8418CB1D73621B3F143BE74E14DB5` | `FEB784798AF1E2F1C73CE4A7290053068A5C30D2198459290FD1DDB4946AED50` | 2 | clean |

Every PDF reports A4 pages. The final log scan found zero fatal/error, undefined-control-sequence, missing-character, overfull, underfull, or warning matches in all three logs.

All three PDFs were text-extracted with Poppler-compatible `pdftotext -layout`. The Hans extraction contains the corrected title, `双链条件`, the Jacobson-root gloss, `自同态除环`, and `分裂域`; both matrices and all source footnotes are present in the PDF text/layout output.

The controlled-Hant target required two layout-only controls after visual QA: a forced page break before the complete direct-product paragraph, and a nonbreaking wrapper around `意義下。`. These controls remove a two-character page-top/line-start orphan and do not alter mathematical or lexical content. The Hant file was then built twice again and both pages rerendered.

Build success is an internal computation, not publication or external language certification.
