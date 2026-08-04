# Chinese Noether Paper 35 — producer revision 3 return and checker re-handoff

## Address and state

Receiving persistent Chinese checker task: `019fca9c-f549-7e71-a314-66f7265343ca`.

Producer state: `HANT-ONLY F015 PRODUCER CORRECTION COMPLETE; FINAL ROOT MANIFEST DEFINES THE IMMUTABLE FREEZE; EXACT INDEPENDENT RECHECK REQUIRED`.

This is not checker acceptance, final reader assembly, archive intake, publication handoff, or certification. It returns the smallest sibling correction required by sealed checker return `ZHCHK-NOETHER-P35-V002-RETURN-001`.

Exact package root:

`C:\Users\Floris\Documents\interlanguage\03_projects\language_management\cjk\03_working_translations\noether_paper35_zh_translation_003_20260804`

The deterministic root manifest is `SHA256SUMS.txt`. It is generated last and excludes only itself; the transport message, decision `ZH-D137`, route `CJK-ROUTE-ZH-P35-005`, and external freeze receipt pin its final entry count, bytes, and SHA-256. After that generation this root must remain byte-immutable during checking.

## Authority and sealed-return custody

- Immutable P35 binder: `NOETH-DE-BINDER-P35-20260804-001`.
- Source-native complete P35: 34,355 bytes, SHA-256 `2E205B2C51B9093FC61C77A9A1DF1C3399FCF098706CEC69134400F1ECC8E491`.
- LF translation source: 34,091 bytes, SHA-256 `DAED6EF21C297425F018C0AE6B23BC5BDD05C0B86984B3FC25FB5937DCBEBD6A`.
- Global pointer v005: 19,889 bytes, SHA-256 `42E6844BFCBFB2133E9AA323A823604351CF9C49550AFCF34ECAAF7887185660`; route metadata only, with no P35 source or target effect.
- Historical v001/v002 root manifests: `44A91086C3736A94D042A2D0DAEC5B5DA88F179E8AF962AB06D202EC33F5888F` / `733454A89830405E9D793E2565296C528BA0A5CAB1CE57177FA29C6E6EC886BD`; both predecessor roots remain unchanged.
- Sealed checker receipt: 13,785 bytes, SHA-256 `B850E0A3320D91787F72CD09A766F681672DF588D846C4307625AEA1B8C5DB69`.
- Sealed selected manifest: 39 entries, 5,674 bytes, SHA-256 `36FE5550D4AEDC4E59C06C6636E081E7D2F7283E1B4055B38F410247DE038D74`.
- Sealed checker verifier: 16,499 bytes, SHA-256 `BA6E7BFA29252839DF16D5CDF857E1652BE33184D4F949E448E5A4AF98854381`, 20/20 checks pass and second replay is byte-identical.
- Sealed return seal: 2,414 bytes, SHA-256 `AA7C524ED3CCCC48574F3763E541854FD6D43E6F53B47FB870365571E9B2B83A`.
- Exact copies of the 39 selected members are under `controls/checker_return_v002/selected_members/`; producer and read-only worker replays found zero missing, byte, or hash failures.

Do not reopen P35 because the route pointer advanced to v005. Do not use Korean binder additions as Chinese evidence.

## Exact artifact-specific disposition

| Target | Editable TeX | Compiled PDF | State |
|---|---|---|---|
| PRC-oriented `zh-Hans-CN` v002 | `build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex`; 31,328 bytes; `DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C` | 274,158 bytes; `F6626C3DC6FFB82E3CFD5C21FA3F74B99459D477E39093715802C49E91E2A18C` | Independently accepted exact artifact; carried forward without edit or rebuild |
| Rejected `zh-Hant-controlled` v002 | 31,515 bytes; `FD16882FAC33B7FD7D0FFB882345168E40FA7F1F22FDEE83AFA2420627D1C054` | 306,051 bytes; `8E77A4C511462C8ECF5876CE7EED0E3A9C4CAD8820A492BD8E665FB47FA50CF1` | Retained only as adverse evidence for F015 |
| New `zh-Hant-controlled` v003 | `build/zh-Hant-controlled-v003/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v003.tex`; 31,515 bytes; `54DE9B43850376FD19306A11FC682166D8F34A4CA6D73E0940695357CE74A005` | 284,874 bytes; `65A449AA0E9C727BEA548C1A8190568636F8C05AB63593666065F956B40774FA` | Producer-generated/compiled; exact independent recheck pending |

Accepted Hans A/B/C concatenation remains 29,808 bytes, SHA-256 `54061274DFDE806F491EE424277886ED4C4CEEF3F7E0315DFD1039AACF69F18A`. No accepted Hans byte changed.

No `zh-Hans-SG`, `zh-Hant-TW`, `zh-Hant-HK`, or `zh-Hant-MO` target exists. Hant is controlled generic only and is not Taiwan-, Hong-Kong-, or Macao-localized prose.

## Exact F015 producer realization

- Applied only: `ZHCHK-P35-F015`.
- Cause frozen by checker: the older regex read the second slash of `\\[0.6em]` as a display opener `\[`, protecting a 2,075-character ordinary-prose span.
- Producer correction: the versioned scanner recognizes a delimiter only when its leading backslash is not preceded by an odd run of backslashes.
- Exact correction diff: 7,840 bytes, SHA-256 `A87F91E27B5BA0CD25BB3983A55140F4C0C7F1AE32CE6A6FE7AFF0EAB96DD8D4`.
- Producer Hant v003 TeX is byte-identical to the sealed checker candidate TeX: 31,515 bytes, SHA-256 `54DE9B43850376FD19306A11FC682166D8F34A4CA6D73E0940695357CE74A005`.
- Recognized math streams: 487/487 equal.
- TeX-control streams: 790/790 equal.
- Legacy false-display spans: zero.
- Scanner/transport record SHA-256: `6286FAA6325E47D36F8FD7886E9C22D99343CF015C60C15D123ACBF84C40982C` / `D7087C586E78887CD5DB4339DDA6C5E9E535F5D8CF1EF6C15F07DBBF71549BFE`.
- Build script/record SHA-256: `3142C89C5A4E7A18B6347F9BA224E07281498042F5459BD03C2BADEE06A7386F` / `2DB562C01A72D30171EEC4082A5D7B1746752C1FB6CBB3DB79788C9B25D43BA1`.
- Final engine log: 23,191 bytes, SHA-256 `F8729C786730A84A83FB94FC6335768356BE3328DF74C72CB9670B07F7FA6573`.
- Two serial XeLaTeX passes exited `0/0` and each reported six pages. Each retained two font-warning lines and one underfull-hbox line; no overfull boxes/vboxes or mechanically matched error patterns were recorded.
- The pass-1 PDF hash was captured but its bytes were overwritten by pass 2; the pass-1 engine log is retained.

These are reproduction, process, and custody facts. They are not source, semantic, formula, terminology, translation-quality, script-completeness, visual, native, or regional validation.

## Finding state

- F001--F011: resolved and independently accepted in exact Hans v002.
- F012/F014: their exact earlier controlled-Hant loci are resolved; F015 was distinct.
- F013: unresolved advisory; no action, German packet, or German mutation.
- F015: realized in producer v003; acceptance pending this recheck.

The interrupted first freeze probe is retained at `controls/P35_V003_INTERRUPTED_FREEZE_PROBE.md`; it found the inherited v002 manifest and correctly halted dispatch. It is operational failure evidence, not a target defect.

## Required independent recheck

Please:

1. Replay the final v003 root manifest and verify the external producer freeze receipt.
2. Confirm that accepted Hans TeX/PDF and A/B/C body custody remain byte-identical; Hans need not be substantively reopened absent an independent checker reason.
3. Independently validate the exact Hant v003 F015 realization and the already controlled generic normalizations against the unchanged binder/source as needed.
4. Compile the exact producer Hant TeX or independently validate the retained build evidence.
5. Freshly render and inspect every Hant v003 page, including the previously failing page 5 and the recorded underfull locus.
6. Return a new sealed, hash-pinned accepted/rejected receipt addressed to the same producer lane.

If a possible German defect is independently confirmed, route a schema-complete finding packet only to canon task `019fca5c-0e73-7c72-92fb-5b507b710598`, keyed to pointer v005 and the exact source span. A translator guess is not defect intake. Do not ask this producer to inspect or adjudicate German.

## Producer boundary

The producer did not source-check, compare or adjudicate German, review semantics/formulas/terminology/translation quality, perform native or regional validation, open/render/visually inspect a PDF, or approve, archive, publish, certify, or claim human/community validation. German is unchanged. SGA remains held and untouched.
