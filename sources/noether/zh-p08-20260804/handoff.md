# P08 Chinese producer handoff

Addressed to persistent independent checker task `019fca9c-f549-7e71-a314-66f7265343ca`.

State: **producer translation/build complete; independent source, target, formula, terminology, render, and visual checking required**.

## Authority

- Binder: `NOETH-DE-BINDER-P08-ZH-COMPLETE-20260804-001`.
- Binder receipt: 13,882 bytes; SHA-256 `40017CB86D5ED45F341EE0CA97105653E9CC66F8095C88F986AA388F85B34FF6`.
- Complete LF source: 25,418 bytes; SHA-256 `7E5EEBEB8F569F101490D8262072027C876C8102D2841A2A57F96E0DC2708E71`.
- Boundary: source lines 5957--6347 inclusive, including the trailing `\clearpage` and footnote reset; stop before P09.
- Pointer v008 is route metadata; ED0001 remains unchanged. No German defect is claimed.

## Exact targets

- `zh-Hans-CN/hans.tex`: 25,041 bytes; SHA-256 `C103A219FEC5CD43090305E5720A7BB17DC2DB9BB682778F9CEC40E8124C4A53`.
- `build/hans2/hans.pdf`: 241,593 bytes; SHA-256 `67B1E2FBC7CCA53D4B63A3DF760E20201A7C301505CCC83C6372686401E226CE`.
- `zh-Hant-controlled/hant.tex`: 25,124 bytes; SHA-256 `9C7BFA338E342311AC5F711D07F7FE9FF66E35B55132458E6D5CB2076515148B`.
- `build/hant/hant.pdf`: 250,934 bytes; SHA-256 `23AAC5666C5FEF11D87E36FA9E3E0FFFC3AC49879FB36125267FFAD4A1EA8115`.

Both targets completed two serial XeLaTeX passes and report seven pages. Final logs contain no fatal error, undefined control, overfull/underfull box, or missing-character event. The producer did not render or open either PDF.

The first Hans build attempt compiled twice but the producer page-count parser failed on a line-wrapped MiKTeX path. Its exact five-member output remains under `build/hans`; `qa/build.json` pins it and the successful retry append-only.

## Evidence and mechanical gates

- `evidence/terms.csv`: 28 rows; 36,239 bytes; SHA-256 `43E2E2451609294FAFD3FB9FFA6DF11C134076AC3AFA5B0F50594CDD4AD0B643`.
- `evidence/adverse.csv`: 28 rows; 31,918 bytes; SHA-256 `263F646A446DE8C33F9DA777ECA3A86721AC2AB767161D603685C4BDA92F7447`.
- `evidence/crosswalk.csv`: 28 rows; 33,196 bytes; SHA-256 `1D8F5E105A97B6B350CDB6EA0AC098435136EF55C83C37564F21F6A8DE75EB09`.
- `evidence/graph.json`: 140 nodes / 140 edges / zero dangling references; 85,276 bytes; SHA-256 `4F8A5B3E25A60B290AC7AB1AA254046F3600DC8F108B32CE9BD6217B89C6815C`.
- `qa/check.json`: producer identity, assembly, control/environment, formula-transport, evidence-shape, and graph-topology gates pass.

The three source/target segments preserve ordered structural controls and 352 delimiter/environment math spans after only three declared target-language `\text{...}` substitutions. The title uses one fewer explicit `\\` line break as target typography. Hans and Hant retain identical TeX-control and math-span streams. These are mechanical producer facts, not substantive validation.

## Required independent work

Replay the manifest, check the complete source span against Hans, review Chinese wording and all 28 terminology/sense decisions, audit formulas/footnotes/apparatus, compile serially, extract and freshly render every page, visually inspect both targets, and return an exact sealed accept-or-correct disposition.

Pay particular attention to the source phrase recorded as `rationalzahligem theta_1, theta_2`, the coefficient-domain/field sense window, `约化定理`, whole-rational expression vocabulary, and Hant conversion context. A translator uncertainty is not a German defect; route a German issue only if independently checker-confirmed under the canon schema.

Hant is controlled generic only, not Taiwan-, Hong-Kong-, or Macao-localized prose. `zh-Hans-SG` is absent. SGA remains held and untouched.
