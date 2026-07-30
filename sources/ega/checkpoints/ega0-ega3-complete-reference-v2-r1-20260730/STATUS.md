# EGA 0 / EGA III complete-reader reference-v2 successor

Status: `PASS_INTERNAL_PUBLIC_PROJECTION__HOLD_EXACT_EXTERNAL_REPLAY`

Translation coverage is complete for the assigned two-reader scope. The exact
next source cursor is EOF for EGA 0 section 13 and EOF after EGA III 7.9.14,
“(To be continued.)”. No EGA IV source was edited.

Reference-only work added 18 source-proven invisible equation targets, 79
exact-text numeric reference links, and 11 exact-text section/chapter links.
Against the immediately preceding source-repaired readers, all 270 extracted-
text pages are byte-for-byte equal at the page-text level.

Current final readers:

- EGA 0: 120 pages, 1,200,518 bytes,
  SHA-256 `99C3D89B432231EC04F5932BA1404FE0B17A05500EA41459B9AE046599BBAD4E`;
- EGA III: 150 pages, 1,299,169 bytes,
  SHA-256 `25F4A2A857F36B536B9925C013BAA575B01E7C2CED438752CEE4384CBE1C1E70`.

Machine closure PASS:

- 35 active source files;
- 911 delivered targets and 1,416 source-label aliases;
- 2,800 candidates = 1,781 applications + 1,019 positive residuals;
- 1,993 complete delivered-PDF edges;
- 90 newly added reference-only PDF actions;
- zero broken GoTo actions and zero CSV formula-unsafe cells.

Controlling graph validation:
`controls/REFERENCE_GRAPH_VALIDATION.json`, SHA-256
`F3E9CA6BC39445F9F943032A46AA4F23A76E4F031657A6ACCBF41936ECFE8C1A`.

The privacy-clean projection rebuilds both readers from only its packaged source.
All 270 page-text streams, all 270 decoded page-content streams, all 911 named
destinations, and all 1,993 GoTo annotations match the packaged readers exactly.
CSV/JSON parsing, graph replay, source closure, and privacy scanning pass with
zero errors and zero private/task-metadata hits. Controlling projection
validation: `controls/PUBLIC_PROJECTION_VALIDATION.json`.

Remaining before custody transport: freeze the self-excluding payload manifest
and obtain one external copied-package replay. No archive action has yet been
taken.
