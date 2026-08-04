# Paper 35 Chinese independent-checker return — v002

Return ID: `ZHCHK-NOETHER-P35-V002-RETURN-001`

## Disposition

- **Overall frozen dual-target package: REJECTED.** A Hant-only producer correction, serial rebuild, new freeze, and new exact re-handoff are required.
- **PRC-oriented zh-Hans-CN v002: ACCEPTED.** Findings F001–F011 are resolved and the exact 29,808-byte body (`54061274DFDE806F491EE424277886ED4C4CEEF3F7E0315DFD1039AACF69F18A`) passed the independent semantic, terminology, formula, TeX, build, PDF-text, render, and six-page visual replay.
- **Frozen controlled-generic Hant v002: REJECTED for `ZHCHK-P35-F015`.** The exact F012 and F014 loci are corrected, but page 5 contains a large mixed-script block.
- **Checker controlled-generic Hant candidate v003: VALIDATED correction candidate.** This is generic script transport only—not Taiwan, Hong Kong, or Macao localization.

## F015 exact coordinates and cause

Target: `build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex`.

The producer regex treats the second backslash in line 244 `\\[0.6em]` as a `\[` display opener and protects through line 272. Visible unconverted Simplified prose is concentrated on lines 245–269. The corresponding 28 complete Hans/Hant lines are byte-identical: 3,901 bytes, SHA-256 `FB5301141DA8681A6551AC92E85BA8C1B96279781D4005C42FD9ED79D02C1098`; the false protected span is 2,075 characters.

## Exact correction and validation

- Candidate TeX: 31,515 bytes, SHA-256 `54DE9B43850376FD19306A11FC682166D8F34A4CA6D73E0940695357CE74A005`.
- Candidate PDF: 284,856 bytes, SHA-256 `5595AEBC8A59247D0E87BC94D9D350B031BCEF6C071BC34642EA9F6C0E695A15`.
- Exact correction diff: 7,840 bytes, SHA-256 `A87F91E27B5BA0CD25BB3983A55140F4C0C7F1AE32CE6A6FE7AFF0EAB96DD8D4`.
- Escaped-delimiter replay: all 487 math spans and all 790 TeX controls preserved; zero legacy false display spans.
- Formula/structure: 478 source formulas; zero missing symbolic source formulas; nine expected explicit target repeats; environment and structural signatures equal.
- Builds: Hans, frozen Hant, and candidate Hant each completed two serial XeLaTeX passes and produced six pages; no overfull boxes or missing characters.
- Visual QA: all pages were inspected directly or by exact raster identity. Hans passes; frozen Hant page 5 confirms F015; corrected Hant page 5 passes.

## Producer action

Integrate only the Hant F015 scanner/correction, regenerate from the accepted Hans body, reapply the already controlled generic normalizations, compile serially, freeze a new manifest/handoff, and return it here. The accepted Hans target need not change.

## Scope

F013 remains unresolved/no action. No German-source defect was confirmed, no German packet was created or sent, German was not mutated, and SGA was not touched.
