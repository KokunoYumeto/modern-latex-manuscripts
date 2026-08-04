# Paper 35 Chinese producer freeze metadata — revision 3

Prepared for decision `ZH-D137` after the checker-frozen Hant-only F015 correction and mechanical build. This is producer custody metadata, not checker acceptance.

## Immutable authority and lineage

- P35 binder: `NOETH-DE-BINDER-P35-20260804-001`.
- Source-native complete P35: 34,355 bytes, SHA-256 `2E205B2C51B9093FC61C77A9A1DF1C3399FCF098706CEC69134400F1ECC8E491`.
- LF-only translation source: 34,091 bytes, SHA-256 `DAED6EF21C297425F018C0AE6B23BC5BDD05C0B86984B3FC25FB5937DCBEBD6A`.
- Global pointer v005: 19,889 bytes, SHA-256 `42E6844BFCBFB2133E9AA323A823604351CF9C49550AFCF34ECAAF7887185660`; route metadata only, with no P35 rebase, source reopening, or target-byte effect.
- Historical v001 manifest: 70 entries, SHA-256 `44A91086C3736A94D042A2D0DAEC5B5DA88F179E8AF962AB06D202EC33F5888F`.
- Frozen v002 manifest: 130 entries, SHA-256 `733454A89830405E9D793E2565296C528BA0A5CAB1CE57177FA29C6E6EC886BD`.
- Sealed independent return `ZHCHK-NOETHER-P35-V002-RETURN-001`: receipt `B850E0A3320D91787F72CD09A766F681672DF588D846C4307625AEA1B8C5DB69`; 39-member selected manifest `36FE5550D4AEDC4E59C06C6636E081E7D2F7283E1B4055B38F410247DE038D74`; all-pass verifier `BA6E7BFA29252839DF16D5CDF857E1652BE33184D4F949E448E5A4AF98854381`; seal `AA7C524ED3CCCC48574F3763E541854FD6D43E6F53B47FB870365571E9B2B83A`.
- Exact copies of all 39 selected return members are retained under `controls/checker_return_v002/selected_members/`; producer replay found zero missing, size, or hash failures.

## Artifact-specific disposition

- Accepted PRC-oriented Hans v002 was neither edited nor rebuilt. TeX: 31,328 bytes, SHA-256 `DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C`. PDF: 274,158 bytes, SHA-256 `F6626C3DC6FFB82E3CFD5C21FA3F74B99459D477E39093715802C49E91E2A18C`. Concatenated A/B/C body: 29,808 bytes, SHA-256 `54061274DFDE806F491EE424277886ED4C4CEEF3F7E0315DFD1039AACF69F18A`.
- Rejected controlled-generic Hant v002 remains adverse evidence. TeX/PDF SHA-256: `FD16882FAC33B7FD7D0FFB882345168E40FA7F1F22FDEE83AFA2420627D1C054` / `8E77A4C511462C8ECF5876CE7EED0E3A9C4CAD8820A492BD8E665FB47FA50CF1`.
- New controlled-generic Hant v003 TeX: 31,515 bytes, SHA-256 `54DE9B43850376FD19306A11FC682166D8F34A4CA6D73E0940695357CE74A005`; byte-identical to the sealed checker correction candidate.
- New controlled-generic Hant v003 PDF: 284,874 bytes, SHA-256 `65A449AA0E9C727BEA548C1A8190568636F8C05AB63593666065F956B40774FA`.
- New final Hant engine log: 23,191 bytes, SHA-256 `F8729C786730A84A83FB94FC6335768356BE3328DF74C72CB9670B07F7FA6573`.

## F015 realization and build custody

- Applied only: `ZHCHK-P35-F015`.
- Escaped-delimiter generator: `controls/build_hant_producer_v003.py`, SHA-256 `6286FAA6325E47D36F8FD7886E9C22D99343CF015C60C15D123ACBF84C40982C`.
- Exact checker correction diff: 7,840 bytes, SHA-256 `A87F91E27B5BA0CD25BB3983A55140F4C0C7F1AE32CE6A6FE7AFF0EAB96DD8D4`.
- Mechanical transport record: 7,018 bytes, SHA-256 `D7087C586E78887CD5DB4339DDA6C5E9E535F5D8CF1EF6C15F07DBBF71549BFE`.
- Build script/record: SHA-256 `3142C89C5A4E7A18B6347F9BA224E07281498042F5459BD03C2BADEE06A7386F` / `2DB562C01A72D30171EEC4082A5D7B1746752C1FB6CBB3DB79788C9B25D43BA1`.
- Warning annex: SHA-256 `F9E1E38ED456DB2ECF4F9F4FB83100522D906FE58DC8190DEEFA7F84A42D1AEE`.
- Mechanical invariants: 487/487 recognized math spans with equal stream; 790/790 TeX controls with equal stream; zero legacy false-display spans.
- Two serial XeLaTeX passes exited `0/0` and each reported six pages. Each retained two font-warning lines and one underfull-hbox line; no overfull boxes/vboxes or mechanically matched error patterns were recorded.
- Pass-1 PDF hash was captured but its bytes were overwritten by pass 2; the pass-1 engine log remains. This is a documented custody limitation, not acceptance evidence.

## Findings and localization state

- F001--F011: resolved and accepted in the exact Hans target by the independent checker.
- F012/F014: exact earlier loci resolved; Hant v002 rejection was the separate F015 tooling defect.
- F013: unresolved advisory; no action, German packet, or German mutation.
- `zh-Hans-CN`: present and independently accepted at the exact v002 bytes above.
- `zh-Hans-SG`: absent and unlocalized.
- `zh-Hant-controlled`: present as controlled generic script only.
- `zh-Hant-TW`, `zh-Hant-HK`, and `zh-Hant-MO`: absent; no regional prose claim.
- Japanese and Korean evidence: unconsulted and non-authorizing for Chinese.

## Interrupted probe and claim ceiling

`controls/P35_V003_INTERRUPTED_FREEZE_PROBE.md` preserves the first incomplete freeze probe, which found the inherited v002 manifest and missing v003 controls. It is superseded only after the new deterministic manifest is generated last and replayed.

The producer performed translation realization, exact candidate reproduction, mechanical generation, compilation, hashing, parsing, and custody checks only. The producer did not inspect or adjudicate German; source-check; review semantics, formulas, terminology, translation quality, native or regional prose; open, render, or visually inspect a PDF; or approve, archive, publish, certify, or claim community validation.

The deterministic v003 `SHA256SUMS.txt` is generated after this metadata, verifier report, and handoff exist. It excludes itself to avoid recursion. Its final entry count, bytes, and SHA-256 belong in the external freeze-verification receipt, decision `ZH-D137`, route `CJK-ROUTE-ZH-P35-005`, and transport message, not recursively in this file.

