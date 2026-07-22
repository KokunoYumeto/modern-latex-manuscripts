# SGA2 Expose XI line 3609 notation adjudication

Decision `EG-SGA2-XI-L3609-PIC-YN-VS-XN-SOURCE-NOTATION-ADJUDICATION-20260722-0001`
closes the notation policy for the held Proposition XI.1.1 unit. This is a
metadata-only archive receipt. It does not publish or authorize an English
target.

## Authority and finding

- Sole textual authority: corrected French arXiv `math/0511279v1` TeX,
  586,789 bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`.
  The authority remains unchanged.
- Locus: French line 3609, printed page 125, same-edition physical page 108,
  recomposed running page 100.
- Exact line identity: 141 Latin-1 bytes without EOL, SHA-256
  `A4A97EB590DB6B9B06BDC45B08D7B351B68E22774A346F2DE81306AAFF3F1051`;
  142 bytes with LF, SHA-256
  `E530C43CE483C38C47FC3CE600D167F9800975B2AF6889E93CD045697E1BDDB3`.
- The authority and same-edition reader manifest `Pic(Y_n)`. Expose XI,
  however, defines the local thickening as `X_n` and uses that notation in
  the immediately preceding context. The manager therefore classifies the
  switch as a local source-notation defect, not a mathematical type error.

Final stable source-defect ID:
`SGA2-XI-L3609-PIC-YN-VS-XN-SRCDEF-001`.

## Target policy

A future no-overwrite English successor must use `Pic(X_n)` and place an
immediate visible note naming the stable defect ID, stating that the French
prints `Pic(Y_n)` and that Expose X had used `Y_n` for the same thickening.
The dependent recurrences at lines 3642 and 3646 must also use `Pic(X_n)` and
bind respectively to:

- `SGA2-XI-BIND-L3642-PIC-XN-001`;
- `SGA2-XI-BIND-L3646-PIC-XN-001`.

The French authority must not be patched. Silently normalizing the target,
retaining `Y_n` without explanation, or treating the same-edition PDF and a
comparison-only LLM lineage as independent corroboration are all rejected.

## Evidence and visual disposition

- Durable manager adjudication: 5,110 bytes, SHA-256
  `081724F82B5591D39B1CA2322CF3266B0114F961C23C36482EBE82F0696A652C`.
- Decision record: 8,086 bytes, SHA-256
  `FA5ED23870087673CD32829CE6FA7CC55E7A86BE077E42970E2EBEC3A34C0EB9`.
- Producer preflight: 37 files, internal only. Its 34-row self-excluding
  manifest has SHA-256
  `0C2210820A42B8FF780544F8975B0C30499B3B76615CB22B1D6181FA5B6D86BC`;
  final validation passes at SHA-256
  `26F67005C49ECCDA910FA1B5B47D4D9AEB35671473D829DBA2F11E431C481896`.
- Preflight machine controls: 22x26 CSV SHA-256
  `59099793E94BCB853EC76A05198260B2CA0E8FCFB241BF745653B246B3605AD3`;
  22-record JSONL SHA-256
  `C57CF360EA2E77806F684086E85990A91497F8EE1412488989BBBC22A65BE74E`;
  privacy validation SHA-256
  `D63604700BB9F47B891D33C382E3E67F0B312B58EABBB7DEF4A5ED6A2E65AFC4`.
- Same-edition physical-page-108 raster: 1,700x2,200 RGB, 200 dpi,
  rotation 0, full-page bounding box `(0,0,1700,2200)`, 289,995 bytes,
  SHA-256
  `B4C32C8D1EE9455FFE5F911FCE30D214EEA7A1186AC9181C06A98D9FB2E159A0`.
  It visibly manifests the source reading but remains
  `rights_blocked_not_public`.
- Same-edition physical-page-107 context raster: 1,700x2,200 RGB, 200 dpi,
  rotation 0, full-page bounding box `(0,0,1700,2200)`, 271,366 bytes,
  SHA-256
  `E727E093E0327C28EEFFA0BD384E003E57E7D44B818F0D3A821A57422767FBF1`.
  It carries the local antecedent context and also remains
  `rights_blocked_not_public`.
- Parent same-edition reader: 216 pages / 1,576,954 bytes, SHA-256
  `41AD02C57321A8D2200FF32A929BC93ADBC3DE0D59DCD5A284D28D859FB87A90`.
  It is same-lineage layout evidence, not independent corroboration.
- Four internal machine-evidence panels remain nonpublic at SHA-256 values
  `2FC19615B408E8319C86CD540E75E7A1AFC54699AE8EB68A2B425E738E671712`,
  `DE72442901F5A86AA5C7DA5F0A8E18CE7DE3F89E77F3FDCA64D3DF74A5AF6161`,
  `1E8621C4CD5894623596F2D1FB572D9475CD86971662B4B456D239C69C335E27`,
  and `7DD75A272F2BD6CC2295D76614DCB5944242561BFCC7B1EC0A247A474AB80679`.

The earlier Section 1 handoff receipt remains an immutable record of its
freeze-time scope, when line 3609 was excluded and unadjudicated. This
successor changes current notation policy only. The proposition unit remains
held at the line-3607/3609 boundary pending a no-overwrite target, regenerated
machine evidence, and fresh independent PASS.

Public source-bearing coverage remains through corrected French line 3574.
The SGA Zenodo concept `10.5281/zenodo.20410947` still resolves to version
`10.5281/zenodo.21435547`, 33 files / 73,450,481 bytes. No draft, mutation, or
duplicate was created.
