# Noether Paper 6 Korean producer source custody — T03 / §2

Custody state: translation-producer metadata only. No source/scan audit, Korean review, formula review, or authority adjudication was performed.

## Authority and pointer binding

- Frozen unit binding: `NOETH-DE-AUTH-v007-20260804`, retained pointer `C:\Users\Floris\Documents\interlanguage\03_projects\noether\07_german_canon_control\pointers\NOETH_DE_AUTHORITY_POINTER_v007_20260804.json`; 21,580 bytes / SHA-256 `A6A8FC8E5AC24ACAF49DFD55B4B58FA3DA882EF8C3FDD4D136220C8751045156`.
- German authority: `NOETH-DE-ED-0001`, `C:\Users\Floris\Documents\interlanguage\03_projects\noether\07_german_canon_control\candidates\NOETH-DE-ED-0001\Noether_German_NOETH-DE-ED-0001.tex`; 2,153,565 raw bytes / SHA-256 `D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB`.
- Complete Paper 6 §2 interval: whole-authority lines 4692--4798; 5,856 LF-normalized UTF-8 bytes / SHA-256 `27A1D4E81287A3F2D4C4276CB3A1909611EDE4B1BB5A47F52F9F86E6DB27B681`.
- Section boundary: line 4799 begins §3 and is excluded.
- Route record: `ROUTE_AND_CLAIM_T03_SECTION2.md`; 1,800 bytes / SHA-256 `FBF2FBB53AD5F273ED70B699F348618B31536200C94A63BE640D86EA4ED0F806`.

## Frozen unit identities

| Unit | Whole lines | Source bytes | Source SHA-256 | Target file | Target bytes | Target SHA-256 |
|---|---:|---:|---|---|---:|---|
| T03-U15 | 4692--4694 | 550 | `28BA46CF37AFEC296C87B4B72B4D5DA6BEF784F733C0F4789B1DCBF16009F641` | `targets/Noether_P06_Korean_T03_U15_UNCHECKED.tex` | 1,246 | `B691FF293FE889DDA5A06493F5B5500D518F1A1EF9A25CB904E77170316FD638` |
| T03-U16 | 4696--4710 | 630 | `7A07524CBCD60B7A7DC366FEC1BD95EADE93C6DDF27D82B1F8B8767E7571E2D8` | `targets/Noether_P06_Korean_T03_U16_UNCHECKED.tex` | 1,563 | `002E6F493C0632F10614AC624292F808AD29089D42164E8FA42AEABAC4008A53` |
| T03-U17 | 4712--4718 | 534 | `6458FEFFCAEEB0BB5541CB2F3762B6BEDEEF88A014C3FE2FF0822023E78BFE2F` | `targets/Noether_P06_Korean_T03_U17_UNCHECKED.tex` | 1,367 | `A8B395E696DA0FBCFC168F9C9C6071AF9F46F9631347FEE8539E6377CD42DF4C` |
| T03-U18 | 4720--4744 | 1,140 | `77796138EF22C497918FD7B80138B0EC90751AAB480459B6ED52131DB5967160` | `targets/Noether_P06_Korean_T03_U18_UNCHECKED.tex` | 2,032 | `96158DD395A0A99BE3166E8039A0B0F379238ECBD3E8FFC59884EE8F04A55429` |
| T03-U19 | 4746--4760 | 1,342 | `65F1723FBCA1B51A908EBB4EF14696165A4CB1BD8ED51514621DF9F0EFE5ED7F` | `targets/Noether_P06_Korean_T03_U19_UNCHECKED.tex` | 2,267 | `AC1C363178B097953C016BFD85BD384F63B9518DBA4804DDEB075A9D88ECFB9B` |
| T03-U20 | 4762--4776 | 556 | `FD9C8EAC41BA33956BDDE0F83A430AF6073F056475841EFBA1B6E5D647ACEA76` | `targets/Noether_P06_Korean_T03_U20_UNCHECKED.tex` | 1,425 | `2C923333710848C0BDE4B4F538C33BB21F8DFBFAAF7272A0E5CED4A4195E0DCE` |
| T03-U21 | 4777--4793 | 938 | `F7F81CBB7440996B2B0390DA7388EEB590BB619D4B24498AB6DFD293BB48E214` | `targets/Noether_P06_Korean_T03_U21_UNCHECKED.tex` | 1,904 | `24DCDF0C062D39CC32256CBD1D398990A32AA590DE845E6104F5D0A84EF4C65C` |
| T03-U22 | 4794--4797 | 160 | `29C47D6D86AF55DE39FABE69F5E37CAC69FE0EFDD57A52CC3CF6FA9113682AC3` | `targets/Noether_P06_Korean_T03_U22_UNCHECKED.tex` | 894 | `F09F8FC5A78E6FBB070706014F9FF4B31567BB758B68388D8F97D9FD94814619` |

The eight source slices total 5,850 bytes. The excluded blank separator lines 4695, 4711, 4719, 4745, 4761, and 4798 contribute exactly one LF byte each: `5,850 + 6 = 5,856` bytes, reconstructing the complete §2 interval. The eight target files total 12,698 bytes; at freeze they are UTF-8, LF-only, without BOM or CR.

U21 opens a `\srcfn{**)}{...` footnote that U22 continues and closes. U21 and U22 are therefore individually editable custody units but not individually closed TeX fragments; any checker or later build task must concatenate U21 immediately followed by U22, without inserted prose.

All eight targets remain `UNCHECKED`. Hash and byte reproduction establishes identity and coverage only; it is not linguistic, mathematical, source, formula, TeX, or visual approval.
