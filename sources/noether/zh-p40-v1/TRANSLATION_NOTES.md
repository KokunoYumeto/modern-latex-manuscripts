# Noether Paper 40 — Chinese producer translation notes

State: complete producer translation and mechanical builds; independent check not performed by this lane.

## Bound inputs

- Current German Paper 40 interval: `source/Noether_Paper40_CurrentGermanAuthority_interval.tex`, SHA-256 `7965805D3A75C3354C85BC7A3E4725F07BF869A8833FC19D74E32BE369427937`.
- Inherited Simplified-Chinese drafting witness: `witness/Noether_Paper40_InheritedSimplifiedChinese_interval.tex`, SHA-256 `3DAD18CAB878BDFA62ED4FCC634E21AF92AF22BC8E11DF8A36888088D0A608AB`.
- Full authority and witness custody: `SOURCE_CUSTODY.md`.

## Non-overlapping producer segmentation

| Segment | German interval-local lines | Source SHA-256 | Intended target |
|---|---:|---|---|
| A | 1–213 | `FF916923952C33A97995C6C7AD098AF4037766B7FC3A781F4D41263B20919BED` | `segments/segment_A_zh-Hans-CN.tex` |
| B | 214–446 | `1A057A1196950C6E3E4FC49C37A93F6966C2DDD1F344125ACFC4D899289B4F7E` | `segments/segment_B_zh-Hans-CN.tex` |
| C | 447–648 | `5D510253EA3A90C673204122BB447D164FA2A08682EB2A1D52C9D4EB99AC4B4B` | `segments/segment_C_zh-Hans-CN.tex` |

Segments are independent translation assignments, not mutual review assignments. Mechanical assembly order is preamble, A, B, C, postamble.

## Initial shared producer terminology

These are editorial proposals for consistency, not checked or approved terms:

- `Nichtkommutative Algebra` → `非交换代数`.
- `Rechtsmodul` / `Linksmodul` / `Doppelmodul` → `右模` / `左模` / `双模`.
- `Darstellungsmodul` → `表示模`.
- `reziproke Darstellung` → provisional `反向表示`; exact sense and alternatives must be exposed to the independent checker.
- `Erweiterungsring` / `Erweiterungsmodul` → `扩张环` / `扩张模`.
- `hyperkomplexes System` → `超复系统`.
- `ähnliche Algebren` / `Algebrenklasse` → `相似代数` / `代数类`.
- `Zerfällungskörper` / `Abspaltungskörper` → provisional `分裂域` / `析出域`.
- `Divisionsalgebra` → `除法代数`.
- `komplementäre Basis` → `互补基`.

`Körper` is trap-prone in this paper because it can denote a commutative field in some passages and a noncommutative division ring/skew field in others. A generic one-term replacement is not assumed.

## Segment producer returns and final normalization

- Segment A was returned as SHA-256 `C5E4551ACB2D011C5C5B06562AEB66FB251531A14FE0D091CFCA8FA94EAA525E`, 24,367 bytes. It proposed `反向表示`, `自同态环`, `除环`, and `分出域`.
- Segment B was returned as SHA-256 `929FB13B6B2DC412A78C2998863CAE8F34C4526EAD8BC8C127FAE2EFD5673615`, 23,559 bytes. It proposed `反向表示`, `自同态环`, `斜域`, `正规基`, `限制模`, and `容许子模`.
- Segment C was returned as SHA-256 `0EC9A765A3A285407CC2953040FF63622C35490D10F385EFD0D4DED7551A7B64`, 23,342 bytes. It proposed `分裂域`, `析出域`, `除环`, `除法代数`, `相似代数`, `代数类`, `互补基`, `可分`, and `完美`.

Before final assembly, two explicit translation-production normalizations made the paper internally consistent without claiming correctness:

- Segment A: `分出域` → `析出域`, exactly 2 replacements; final segment SHA-256 `177E586E500D9B2AC8FFDAD01D95261123DD40C595D062DA030E1F4936955D24`.
- Segment B: `斜域` → `除环`, exactly 42 replacements, while explicit commutative `域` wording remained untouched; final segment SHA-256 `D77B79E042DED043E2BE4517DA53E745148C36B86C254C5851656FFE00877739`.
- Segment C remained unchanged at SHA-256 `0EC9A765A3A285407CC2953040FF63622C35490D10F385EFD0D4DED7551A7B64`.
- Exact input/output hashes, counts, motivations, and claim limits are in `qa/TERMINOLOGY_NORMALIZATION_RECORD.json`, SHA-256 `CC1D6320628159A007A7D7B880133539F1A5240D647975AB0B2970267084EB87`.

Producer risks for the independent checker include the historical scope of `Automorphism` where the source admits noninvertible maps; `反向` versus inherited `互反`; `析出域` versus other Chinese renderings of `Abspaltungskörper`; `除环` versus `斜域`; source reuse of (Z) for isomorphic copies; and `Differente`, which must not be read as the everyday adjective “different.” These are adverse translation notes, not findings or validation.

## Final producer outputs

- Hans TeX SHA-256 `73E05D631EBA59BDCD69770275586833FA0546D8D7E4A262F9048D10D5B44147`.
- Controlled-generic Hant TeX SHA-256 `B2C71E1CFC48D232D45FF164FD60008837DDDFD3D9279E5CA3A168B221EAB8C6`.
- Hant is a controlled script derivative only, not Taiwan-, Hong Kong-, or Macao-localized prose.
- Both targets compiled mechanically in two successful XeLaTeX passes to 15-page PDFs. Build facts and adverse compiler messages are in `BUILD_REPORT.md`.
- No PDF page was rendered to an image or viewed by this lane.

## Required claim limit

Floris's controlling instruction is `you do not check - you translate - other sessions CHEWCK`. These notes record producer choices and uncertainties only. They are not source checking, semantic checking, formula checking, visual inspection, native-reader validation, regional Hant localization, approval, or certification.
