# P08 Chinese evidence-generator return

- Return ID: `P08-ZH-EVIDENCE-GENERATOR-RETURN-001`
- Recorded at: `2026-08-04T16:00:55+02:00` (wall-clock precision: one second)
- Work unit: Noether Paper 8 producer evidence packaging only
- State: generator complete; final evidence generation intentionally deferred until final Hans/Hant TeX paths exist

## Created artifact

- `qa/evidence.py`
  - 52,444 bytes
  - SHA-256 `34FC29081C10A08E9ECFF00B9160DC29E0714610785C1EB506F47DBEF972E2CD`

The generator preserves the established schemas exactly: 15 fields in `evidence/terms.csv`, 13 in `evidence/adverse.csv`, 16 in `evidence/crosswalk.csv`, and the established eight-key typed graph in `evidence/graph.json`. It packages 28 trap-prone decisions, with one source-locus node, one concept node, two script-scoped form nodes, one producer-choice node, and five typed edges per decision (140 nodes and 140 edges). Every decision carries a sense window, excluded senses, alternatives, a permitted provisional lexical-attractor basin, qualitative Mandarin-Simplified dominance debt, controlled-generic/nonregional Hant status, and independent-check-pending state. JA/KO fields remain blank and explicitly non-authorizing for Chinese.

## Pinned inputs

- sealed source: `source/P08_complete_lines5957_6347_LF_terminal.tex` — 25,418 bytes — SHA-256 `7E5EEBEB8F569F101490D8262072027C876C8102D2841A2A57F96E0DC2708E71`
- inherited Hans witness: `witness/P08_inherited_Hans_lines6395_6842_LF_terminal.tex` — 24,009 bytes — SHA-256 `F1DC44C7E4FC9D55EDC7636660CC741959A06613EABA43014353B663DE7A36D3`
- translation notes: `TRANSLATION_NOTES.md` — 1,703 bytes — SHA-256 `CE0559CA059C07EC41EDEFC2B9F4BF170F25F774CFC2DB9950A8F9677058EDF9`
- S01 producer return: `worker_returns/P08_S01_WORKER_RETURN.md` — 4,079 bytes — SHA-256 `85CD91322EF04611136D891C7D05A25233331FD2207CCF81F2CE0854B1CCE4F2`
- S03 producer return: `worker_returns/P08_S03_WORKER_RETURN.md` — 7,297 bytes — SHA-256 `E9E14FF5BA74B5411C8A204F4B2A7774DB510E3A134A769F132B8241FF8F97D2`

The sealed source and inherited witness were read completely for bounded terminology packaging, not German adjudication or translation checking. The P07/P10/P12/P39 15/13/16-field ledgers and typed node/edge shapes were inspected and retained without adding new node fields.

## Validation and deferred cursor

- `python qa/evidence.py --validate-only`: PASS; 28 decisions; 15/13/16 fields; 140/140 nodes/edges; unique IDs; zero dangling references; no files written.
- in-memory final-binding/schema exercise: PASS; 28 bound decisions and exact field counts.
- At return time, `evidence/terms.csv`, `evidence/adverse.csv`, `evidence/crosswalk.csv`, and `evidence/graph.json` were all absent, as required while the final targets were absent.

Generation cursor:

```powershell
python qa/evidence.py --hans "zh-Hans-CN/<final-Hans>.tex" --hant "zh-Hant-controlled/<final-controlled-Hant>.tex"
```

The run hash-binds both final TeX files and refuses to freeze evidence unless each of the two current assembly splits resolves to one corresponding Hans/Hant pair: `归约定理` versus `约化定理`, and `有理域` versus `有理性域`. This is an occurrence-consistency gate, not independent terminology validation.

No translation segment, final target, shared control, German file, PDF, build, render, manifest, SGA artifact, or pre-existing evidence file was edited. No German defect is asserted. Ownership of `qa/evidence.py` is released to the parent producer.
