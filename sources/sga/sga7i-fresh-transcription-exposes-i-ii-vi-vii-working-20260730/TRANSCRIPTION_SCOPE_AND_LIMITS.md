# Transcription scope and limits

## Exact scope

The reader concatenates four separately frozen, complete exposé bodies in source order:

| Exposé | Source folios | Source pages | Output pages | Language printed in source | Native diagrams |
|---|---:|---:|---:|---|---:|
| I | 1-24 | 24 | 13 | French | 7 |
| II | 25-31 | 7 | 4 | French | 1 |
| VI | 32-132 | 101 | 59 | English | 87 |
| VII | 133-217 | 85 | 39 | French | 21 |
| **Total** | **1-217, with the volume's exposé numbering gap preserved** | **217** | **115** | **mixed** | **116** |

The production ledger's broader 249-page progress count also included 32 unfinished Exposé VIII
pages. They are not frozen and remain outside this checkpoint, as does all of Exposé IX.

## Completed checks

- the four frozen source bodies build together in two passes;
- all 115 output pages contain extractable text;
- all diagrams are native TeX (`tikzcd`), with zero `includegraphics` calls and zero PDF image
  XObjects;
- representative opening, ending, and exposé-transition pages were rendered and inspected;
- all extracted character boxes remain inside the A4 media box after seven explicit wide-display
  layout wrappers and breakable underlining;
- the reader text contains no private paths, internal task names, model names, or project-status
  pages.

## Open limits

- This is a working transcription rather than a critical edition.
- The source-side apparatus records numerous uncertain readings and source defects; those raw
  working ledgers are not part of this compact reader package.
- The four exact producer-frozen body files are retained under `source/frozen/`; the build-facing
  copies differ only by the reader-layout wrappers described above.
- Diagram fidelity is not claimed uniformly beyond the source checks already completed.
- The PDF has no internal GoTo links, tagging, or XMP metadata stream.
- No translation claim is made for the French exposés; Exposé VI is English because the source
  itself is English.
