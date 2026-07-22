# SGA2 Expose XI line 3607 R3 reviewed handoff hold

Date: 2026-07-22

## Current classification

Archive maintenance received and independently replayed the no-overwrite R3
handoff for corrected French line 3607. The source boundary, target identities,
three producer builds, three independent builds, extracted text, fonts, render,
machine ledgers, privacy checks, and R1/R2 failure history all close.

The handoff nevertheless authorizes zero public files. Every one of its 45
custody candidates is marked `proposed_public=false` and
`not_authorized_not_dispatched`; the controlling readiness is
`NOT_READY_FOR_PUBLICATION`. GitHub therefore records only this sanitized
custody metadata. The TeX, PDF, extracted text, machine evidence, build
evidence, target render, and source-page raster remain withheld.

## Scope and identities

- Scope: SGA2 Expose XI, corrected French line 3607 only.
- Locators: original printed pages 124-125, same-edition physical page 107,
  recomposed running page 99.
- Page transition: the embedded original-page marker occurs at zero-based byte
  201, immediately after `c(E)`.
- Cursor: raw cursor 3608, an excluded blank; line 3609 and Proposition XI.1.1
  are separate and excluded.
- French authority: 586,789 bytes, SHA-256
  `C2F899E92A904E312B550C6452A117FF23D30AF984B2254A0961D2DF0DACD042`;
  unchanged.
- Exact authority line: 354 bytes including LF, SHA-256
  `9CAC599D8F8831D3FBC0B75854F46C0C0E140CA1BA2BD31BBA30F3515758874F`;
  withheld.
- Withheld TeX: 2,283 bytes, SHA-256
  `9CC4C39BA32A0C98B1150BB9035EDDEAE0266F670118456BF147D2EF6A313619`.
- Withheld one-page A4 PDF: 278,894 bytes, SHA-256
  `B12C84829AC6535C5ECFCE490AA9594ACE7297DC02A56E6D15E696AA77863A6D`.

The frozen original handoff contains 16 files / 107,817 bytes. Its 13-row
self-excluding manifest replays 13/13 at SHA-256
`4632548E91C8C8BC4040208A07DD85AD839E9B438063716ED96B53933B97695F`;
`HANDOFF_VALIDATION.json` passes with errors `[]` at SHA-256
`1686E5A946EE9B310CD03F0577CB4ED3760983E9938A2C5A698D1B27BBF69DCA`.
Four append-only transport controls later expanded the local directory to 20
files / 115,511 bytes. Its 18-row post-dispatch manifest also replays 18/18,
and records message transport only, not archive acknowledgment or publication.
Those local controls remain internal.

Archive replay matched all 96 producer/review custody identities
(2,067,223 bytes), all 45 candidate identities (456,296 bytes), and all 28
stable CSV/JSONL identities. Independent privacy replay found zero private-path
or thread-ID hits in the candidate projection.

## Review and visual disposition

R1 failed closed on an incomplete page-marker assertion. R2 closed that
assertion but failed closed on one stale terminal manifest identity. R3 changes
no authority, target, locator, or boundary bytes and closes the manifest
failure. A first reviewer attempt ended before adjudication with a preserved
logic error; the corrected independent review then passed.

- Producer machine evidence: 29 CSV rows and 29 JSONL records, SHA-256
  `2701ED4D7888605D116FE9CC425827B6484A2F6C8EBFDDC4D3EC47FFC05C6F0D`
  and
  `1777CF6BAEA83FFCEF999ECA8881AE00E21CAF882C261006B24F3326B121F041`.
- Independent evidence: 41 CSV rows and 41 JSONL records, SHA-256
  `DB8673ED17D3FCAE5DB1B5E9212C33A1A9554F6257E107AA21B93C9DA50B7E9C`
  and
  `49B3A257845EE1E92B25CCDC93D784C7A898BECEB25EEC93B6294A935E4BC3D8`.
- Independent final validation: `PASS`, SHA-256
  `DD77A35BF60DE87A60BC62E1BAB5D95A7B3B3CB2F3FE5D3F1225BB8FA45CB826`.
- Fonts: 22/22 embedded, subset, and Unicode mapped.

The project-generated target render is 1,654 x 2,339 pixels at 200 dpi,
203,448 bytes, SHA-256
`4D60865ACED1C29617FE655D621EA64116CF7AB74AE50508EE23EB7D885AE30C`.
The independent rebuild render is byte-identical and the pixel comparison has
zero differences. Direct archive inspection found a clean page, but its
immutable authority box still says that fresh review and line-3609 manager
adjudication are pending. Both statements are now stale, so the render and
target remain held pending a publication-facing successor.

The same-edition physical-page-107 raster is 1,700 x 2,200 pixels at 200 dpi,
271,366 bytes, SHA-256
`E727E093E0327C28EEFFA0BD384E003E57E7D44B818F0D3A821A57422767FBF1`.
It is locator/layout evidence from the same lineage, not independent
corroboration, and remains `rights_blocked_not_public`.

## Release boundary

Underlying French rights/final attribution, an explicit English license,
publication-facing regeneration, and PDF accessibility remain unresolved.
Line 3609 has a separate manager-closed `Pic(Y_n)` to `Pic(X_n)` target
policy, but no proposition target is released here.

This receipt does not extend public source-bearing coverage beyond corrected
French line 3574. It is not a complete Expose XI or SGA2 claim, publication,
peer review, source certification, rights clearance, accessibility
certification, or critical edition.

The official Zenodo API was rechecked at
2026-07-22T05:40:19.7027887+02:00. Concept
`10.5281/zenodo.20410947` still resolves to published version
`10.5281/zenodo.21435547`, record 21435547, 33 files / 73,450,481 bytes,
updated 2026-07-19T02:40:42.287682+02:00. No draft, mutation, deposition, or
duplicate was created.
