# Noether Paper 35 Chinese producer return — Hant F015 revision 3

## Assignment and state

- Work: complete Noether Paper 35 Chinese producer package.
- Producer revision: `noether_paper35_zh_translation_003_20260804`.
- Controlling decision: `ZH-D135`; metadata update `ZH-D136`; freeze decision pending.
- Checker return: `ZHCHK-NOETHER-P35-V002-RETURN-001`.
- Finding realized: `ZHCHK-P35-F015` only.
- State: producer generator correction, mechanical Hant build, evidence, and handoff complete; the last-generated root manifest and external receipt define exact package custody; independent recheck pending.

This is a producer return, not independent checking, acceptance, archive intake, publication approval, or certification.

## Exact authority and custody

- Immutable P35 binder: `NOETH-DE-BINDER-P35-20260804-001`.
- Source-native P35: 34,355 bytes, SHA-256 `2E205B2C51B9093FC61C77A9A1DF1C3399FCF098706CEC69134400F1ECC8E491`.
- LF source: 34,091 bytes, SHA-256 `DAED6EF21C297425F018C0AE6B23BC5BDD05C0B86984B3FC25FB5937DCBEBD6A`.
- Pointer v005: 19,889 bytes, SHA-256 `42E6844BFCBFB2133E9AA323A823604351CF9C49550AFCF34ECAAF7887185660`; route metadata only, no P35 source or target effect.
- Sealed checker-return manifest: 39 selected members, SHA-256 `36FE5550D4AEDC4E59C06C6636E081E7D2F7283E1B4055B38F410247DE038D74`; imported replay has zero failures.
- v001/v002 remain immutable at manifest SHA-256 `44A91086C3736A94D042A2D0DAEC5B5DA88F179E8AF962AB06D202EC33F5888F` / `733454A89830405E9D793E2565296C528BA0A5CAB1CE57177FA29C6E6EC886BD`.

## Exact targets

Accepted Hans was carried forward without edit or rebuild:

- TeX: 31,328 bytes, SHA-256 `DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C`.
- PDF: 274,158 bytes, SHA-256 `F6626C3DC6FFB82E3CFD5C21FA3F74B99459D477E39093715802C49E91E2A18C`.
- A/B/C: `26A7615B9EFD825ADF20DABF9DE34673CB1F52807AC7E07A0F0118F79E8DD3EF` / `5A2EB988239E78102D18F22AC552978AD987CE299E5B6A0D738FFA87034B2424` / `5F62E3139C5528ABCD4ACB978EA6CC14AF1B052E6E3E78CBAFBB10161B5B01B3`.
- Concatenated body: 29,808 bytes, SHA-256 `54061274DFDE806F491EE424277886ED4C4CEEF3F7E0315DFD1039AACF69F18A`.

Rejected Hant v002 remains adverse evidence:

- TeX/PDF: SHA-256 `FD16882FAC33B7FD7D0FFB882345168E40FA7F1F22FDEE83AFA2420627D1C054` / `8E77A4C511462C8ECF5876CE7EED0E3A9C4CAD8820A492BD8E665FB47FA50CF1`.

New producer Hant v003:

- TeX: `build/zh-Hant-controlled-v003/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v003.tex`; 31,515 bytes; SHA-256 `54DE9B43850376FD19306A11FC682166D8F34A4CA6D73E0940695357CE74A005`.
- It is byte-identical to the sealed checker correction candidate.
- PDF: `build/zh-Hant-controlled-v003/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v003.pdf`; 284,874 bytes; SHA-256 `65A449AA0E9C727BEA548C1A8190568636F8C05AB63593666065F956B40774FA`.
- Final engine log: 23,191 bytes; SHA-256 `F8729C786730A84A83FB94FC6335768356BE3328DF74C72CB9670B07F7FA6573`.

## Mechanical realization

- Producer scanner: `controls/build_hant_producer_v003.py`; SHA-256 `6286FAA6325E47D36F8FD7886E9C22D99343CF015C60C15D123ACBF84C40982C`.
- The scanner ignores delimiter starts preceded by an odd run of backslashes, so the second slash of `\\[0.6em]` cannot begin `\[`.
- Math spans: 487 Hans / 487 Hant, exact stream equality.
- TeX controls: 790 Hans / 790 Hant, exact stream equality.
- Legacy false display spans: zero.
- Transport record: 7,018 bytes, SHA-256 `D7087C586E78887CD5DB4339DDA6C5E9E535F5D8CF1EF6C15F07DBBF71549BFE`.
- Build script/record: SHA-256 `3142C89C5A4E7A18B6347F9BA224E07281498042F5459BD03C2BADEE06A7386F` / `2DB562C01A72D30171EEC4082A5D7B1746752C1FB6CBB3DB79788C9B25D43BA1`.
- Two serial XeLaTeX passes exited `0/0` and each reported six pages.
- Each pass retained two font-warning lines and one underfull hbox; zero overfull boxes/vboxes and zero error-pattern matches.
- Exact warning annex: SHA-256 `F9E1E38ED456DB2ECF4F9F4FB83100522D906FE58DC8190DEEFA7F84A42D1AEE`.
- Pass-1 PDF bytes were hash-captured but not retained separately; the pass-1 engine log is retained. This is nonblocking mechanical evidence, not a visual claim.

## Evidence records

- Intake receipt: SHA-256 `73DD5DF67418298980EC3FBF247CDB9DE239DB894913FB65D617774F1D59E294`.
- F015 realization: SHA-256 `2B6E82F1C53573CBA67AB377C794FBC64683A3BFDA374AC460710FB47288FB66`.
- v005 metadata receipt: SHA-256 `65D5006944735F28305D743B67E638C9384B813449A60E14DE7DFE110070074C`.
- Finding disposition: SHA-256 `B9CD5DF7FA956422019E95F8860C977834E54298A62928F2629B4E0808F1357E`.
- Adverse evidence: SHA-256 `0FDFDDA9D45EE1B5C368135FE628A4132A24AF24AF1A8F085DB9B24065718DAD`.
- Localization/CJKV: SHA-256 `6C44A4D076399A335CDB0587791CFF8BB4615904FF22191C75E7B8287168F4EA`.
- Typed graph: SHA-256 `634FE1EDC064A1C44E52363EFE680DFF8F2DEF47637253AD806EBB2D343CA477`.

No new terminology or sense-window record was added because F015 is a tooling/transport correction and introduces no producer lexical choice.

## Claim boundary and next action

The producer did not inspect/adjudicate German; source-check; review semantics, formulas, terminology, translation quality, or native/regional prose; open/render/visually inspect a PDF; or approve, archive, publish, certify, or claim community validation.

`zh-Hans-SG` remains absent. Hant is controlled generic only and is not Taiwan-, Hong-Kong-, or Macao-localized prose. `F013` remains unresolved with no German packet. SGA remains held.

Next: use the final root-manifest identity pinned externally in decision `ZH-D137`, the freeze receipt, and route `CJK-ROUTE-ZH-P35-005`; persistent checker task `019fca9c-f549-7e71-a314-66f7265343ca` must perform the exact independent recheck.
