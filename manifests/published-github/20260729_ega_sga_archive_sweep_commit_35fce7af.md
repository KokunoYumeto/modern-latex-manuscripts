# EGA and SGA archive sweep public readback

Date: 2026-07-29

Repository: `KokunoYumeto/modern-latex-manuscripts`

- Pull request: https://github.com/KokunoYumeto/modern-latex-manuscripts/pull/96
- Source commit: `b49ad2de667248a99e160ca791eea84b5d8bd437`
- Merge commit: `35fce7afa8c495130947ecf1f9ad6535c3582c0e`
- Machine readback: `20260729_ega_sga_archive_sweep_commit_35fce7af_public_readback.json`
- Machine readback SHA-256: `D41C2E1A20FE723F5F4D0C87207215AF791421B63C4DF45F92816BB03A3E1718`

## EGA assigned source-first lane

Public path:
`sources/ega/checkpoints/ega0-iii-and-ega3-source-first-assigned-lane-complete-20260729`

Anonymous readback reproduced all 11 outer files and all 44 source-ZIP
members exactly.

- EGA 0, III sections 8-13 working reader: 1,190,098 B,
  SHA-256 `D0454AA8BB79653D9CC97C7973EB54B2038BF8038525022038A29E9628C978F4`
- EGA III sections 1-7 working reader: 1,284,316 B,
  SHA-256 `1C2A3F286A02EBBB521D0D4939B0604A7D8000023288F4599322EFC0FA21B886`
- Grouped editable-source ZIP: 468,919 B,
  SHA-256 `B645E2F59F79F7F4DCD6A78922E0566C1DBF02590C0629358795EF49CA640BDF`

This is a working checkpoint, not complete EGA. EGA remains assigned to its
separate existing Zenodo concept `10.5281/zenodo.20414353`. No new EGA
deposition or duplicate concept was created in this sweep.

## SGA3 native-diagram integration inputs

Public path:
`sources/sga/sga3-native-diagram-integration-inputs-x-xvi-xviii-20260729`

Anonymous readback reproduced all 8 outer files and all 46 grouped-ZIP
members exactly.

- Grouped integration ZIP: 767,403 B,
  SHA-256 `7064F69F2CAE719DAE61601FC7A7D98122CACB5067739A24830DD149F586A070`
- Expose X bounded reader in ZIP: 44 pages,
  SHA-256 `116065B39DC227EA72863ED7C71BC925CC15E0C62AAAE88601B46C648CAF64A7`
- Expose XVI bounded reader in ZIP: 25 pages,
  SHA-256 `C2126756DF0A22A26D37DC5097C6DC723F63C65C21636E1BE9A7886016CBC84A`
- Expose XVIII bounded reader in ZIP: 22 pages,
  SHA-256 `83E955BD25A92A65507A38F8E697DFC1DA6E46D8BF154C56BE33C9940B57EF6A`

These are bounded native-diagram integration inputs, not a cumulative-reader
replacement. The clean 1,473-page SGA3 R15 reader remains the front reader
until cumulative source/reference regeneration is complete.

## Zenodo disposition

The SGA concept remains `10.5281/zenodo.20410947`. Public record `21650398`
remains the live head. Existing same-concept draft `21662699` remains
unsubmitted with exactly 92 inherited files. A fresh exact upload probe again
failed server-side with HTTP 400, `The file upload transfer failed, please try
again`; the probe left no residue. No second draft, record, or concept was
created.
