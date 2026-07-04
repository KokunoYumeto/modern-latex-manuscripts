# Workflow Addendum - SGA5 Zoom-First Source Adjudication

Date: 2026-07-01

This addendum records a workflow lesson from the live SGA5 workpass. It is method evidence, not SGA5 certification.

## Context

The local SGA5 audit lane under `SGA continuation 2/_claude_aid/sga5_full_audit_20260623` advanced to an Expose V p234 checkpoint on 2026-07-01. The current scorecard reports 234 pages inspected, 21 TeX fixes plus one cosmetic fix, 38 source typos tracked, 8 TeX content errors found and fixed, and 136 diagrams tracked.

Those numbers are useful as audit telemetry, but they are not edition claims. The lesson is the method that produced them.

## Rule

Before changing a mathematical symbol, label, subscript, diagram edge, or suspicious word, inspect the source glyph at sufficient zoom and decide which class the discrepancy belongs to:

- `editor/transcription error`: the TeX diverges from the source and should be fixed.
- `copied source typo`: the source itself appears wrong; either keep it with a note, or correct it only when the mathematical context makes the source typo effectively certain.
- `source oddity`: the source is unusual but coherent; keep it.
- `false flag`: the current TeX looks suspicious, but zoomed source inspection shows it is faithful.
- `layout/cosmetic issue`: the mathematical content is correct, but the public reader may still need typography work.

Do not use OCR, an agent finding, or a plausible mathematical normalization as the deciding authority. Use source image first, TeX second, OCR/agent candidate third.

## Practical Procedure

1. Locate the exact source page and crop region.
2. Render or crop at enough resolution to decide the glyph, not merely the word shape.
3. Compare against the current TeX and nearby repeated notation.
4. Classify the discrepancy before editing.
5. If edited, compile and record the page, source locus, old TeX, new TeX, reason, and build status.
6. If not edited, record the trap so it is not rediscovered and "fixed" incorrectly later.

## SGA5 Lessons

The SGA5 lane produced several distinct outcomes that should be preserved as workflow examples:

- A zoom pass can confirm a real fix when a copied source typo is mathematically forced.
- A zoom pass can prevent a false flag when a suspicious glyph is actually faithful to source.
- A zoom pass can reveal a source-faithfulness deviation that is mathematically harmless but still should be corrected for transcription fidelity.
- Repeated notation across nearby pages is evidence, but not authority; source glyph inspection remains the gate.
- Agent and OCR findings are good finders, but their recall is incomplete and their confidence can be misleading.

## Public-Archive Implication

Public records should separate:

- page-local workpass status;
- source-audit/provenance evidence;
- build-clean TeX;
- reader-facing quality;
- globally certified or critical-edition status.

A compiled PDF with a clean log can still contain mathematical or source-fidelity errors. Conversely, a local audit log can contain valuable repair evidence without being a promoted public edition. The archive should publish caveats at that granularity.
