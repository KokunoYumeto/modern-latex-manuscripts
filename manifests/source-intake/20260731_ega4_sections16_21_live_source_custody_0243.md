# EGA IV Sections 16-21 live source and bounded-build custody

At `2026-07-31T02:43+02:00`, archive maintenance captured coherent producer
checkpoints from both active EGA IV Part 4 lanes in:

`sources/ega/ega4-sections16-21-live-source-custody-20260731T0243`

The package has 19 files / 2,804,750 bytes. Its 17-row self-excluding
`SHA256SUMS.csv` is 2,931 bytes with SHA-256
`F73EADA4A7EA1EF030E3BB6370A69356338C4A9C2A665404F8594B036C2EDF2C`
and replays exactly. `CUSTODY_VALIDATION.json` is 1,937 bytes with SHA-256
`E1F1400EDB50E494D0476C6E207B4A8B7417EB8CF8C291582A416938FCED464A`
and reports no errors.

The Sections 16-18 source is the exact closure used by producer checkpoint
`checkpoint_printed070_r21`, aligned through printed page 70. Its bounded
122-page PDF is 834,359 bytes with SHA-256
`CD9FE68D1DD28F092DAE15AD90DEBDB68396626A34C9316DBAAA6E7D84DD6A68`.

The Sections 19-21 source is the exact closure used by producer checkpoint
`build_p185_210_r9`, aligned from printed page 185 through page 210. Its
bounded 101-page PDF is 698,596 bytes with SHA-256
`BBE9DAC3C7DB977E622BB7F6CA17C8744EC5E36091E1A6D17F60CE05423A511A`.

The producer checkpoint logs report three-pass builds with zero hard TeX
diagnostics. Archive maintenance verified the file identities, parsed the
controls, and scanned PDF text for private paths and project/model/process
prefaces with zero hits. It did not perform a fresh independent visual render;
the producer's existing visual evidence remains the visual basis.

The 360-page NUMDAM EGA IV Part 4 authority PDF, authority pixels, OCR bodies,
raw logs, scripts, caches, and auxiliaries are excluded. The checkpoint PDFs
include inherited text beyond the newly aligned page ranges, so they are not
complete EGA IV or cumulative EGA I-IV readers. No rights-clearance,
critical-edition, exhaustive-reference, or accessibility claim is made.
Zenodo remains unchanged.

