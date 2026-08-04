# Noether Paper 11 Chinese producer mechanical build report

## Claim limit

Floris’s exact boundary:

> you do not check - you translate - other sessions CHEWCK

This report records deterministic packaging and mechanical compilation only. It records no source/witness audit, semantic or formula-content check, terminology or translation-quality review, cross-segment harmonization, PDF opening/rendering, regional localization, approval, publication, archive action, certification, or SGA work.

Hash snapshot: 2026-07-22 13:06:06 +02:00.

## Hans assembly

| Input/output | Bytes | SHA-256 |
|---|---:|---|
| standalone preamble | 1,574 | BB6A1ACA1A5354DE93014851E4438D03862F852D99B865FDF5CB69C774034394 |
| Hans segment A | 9,767 | 26DD08920E1008DA29A99BAE1D35F113F6F01FF0B766905CDC847D1BB059AFC2 |
| Hans segment B | 5,896 | 82FB18F5F3F28C768BEFF2027619286F853374A183A09D72A0581FA9D4FABB4C |
| Hans segment C | 5,941 | 52802111D99718BE89923B90464A5F893163ABBD5AE7BB0590D3A983932FB712 |
| standalone postamble | 15 | 7C0796754F02F5FEB9AADD6A37D7145D65BD53DDB0779DBA48832B3BBB06FCB2 |
| assembled Hans TeX | 23,193 | 0AC62833A6F4510620FB1995F05AB9479D98D89371DE731371D7665729C8B352 |

- Assembly script SHA-256: 148FBDF85F9339B25A1595FB22E7D3564ACA443FDC14ADBF7C65B9355B2D13D0.
- Assembly record SHA-256: 0B424944453B36954A2B56B71950A296BCB019AF534A01DAD626BE93F2876B4C.

## Hans build

- Compiler: XeLaTeX.
- Requested and successful passes: 2 of 2; both exit codes 0.
- Pages reported by final log: 5.
- Final PDF: 245,319 bytes; SHA-256 A7435DC3D22C49D22B310371C6335A730517081FB3CEA342C12D216823691BB4.
- Final engine log: 21,148 bytes; SHA-256 5DA4F7F38ACE0446B01ABA1952880220AF6ADA57D173BD5B574152739FAAC172.
- Build record reports 0 error-pattern matches, 2 warning-line matches, 0 overfull matches, and 0 underfull matches.
- Build script SHA-256: A94D8A26AC67689B641D6B1685AD797732A8A3BCFD25F9BC6745F543A5EB372B.
- Build-record SHA-256: 0498D49C5BAB2BC67CAF2855B6E25A143AB66C21DEFEDF7FFE92551C27D194B2.
- PDF opened or rendered: no.

## Controlled-generic Hant transport

- Input Hans TeX SHA-256: 0AC62833A6F4510620FB1995F05AB9479D98D89371DE731371D7665729C8B352.
- Converter: opencc-python-reimplemented 0.1.7, configuration s2t.
- Producer script SHA-256: 49A2BBDAF0EC7A25E3B6A2AE329328993A58A76BF5AE6D467996B7169951CBA2.
- Mechanically protected and compared math spans: 229.
- Mechanically compared TeX control sequences: 795.
- Output controlled-generic Hant TeX: 23,535 bytes; SHA-256 3012062C76A642D698E6B8ABB5E566C20DF5130C2BC1D6B7BF40F09224AC0075.
- OpenCC producer-record SHA-256: 6CAF04D2280A9CC0BD483E39E62E9B0698EADED3D37A0BE9A009FD05BE955265.

The math-span and control-sequence comparisons are script-transport invariants only. They are not formula-content or source checks.

The output is controlled generic Traditional script only, with the Hans producer wording as lexical base. It is explicitly not zh-Hant-TW, zh-Hant-HK, or zh-Hant-MO prose.

## Hant build

- Compiler: MiKTeX-XeTeX 4.18 (MiKTeX 26.5).
- Requested and successful passes: 2 of 2; both exit codes 0.
- Pages reported per pass: 5.
- Final PDF: 265,866 bytes; SHA-256 D0945DB43CA55D6F66549D83EC54DC4E2FA3D013356093ABBB736CC4E99A5C24.
- Final engine log: 21,222 bytes; SHA-256 EDEE75F930084FFB1DAF80AB710907ABEB832213529A74B6F93656E417934D4E.
- Final record reports 2 font-warning lines and no LaTeX/package/box-warning lines.
- Build script SHA-256: 56BEE6570F59C758D268D8A870C7D63A9EBB1094AEB97034761FFE6F337C277A.
- Build-record SHA-256: 7708F77275FF334C69401C04827B5BA07F5652A204E4C135D5B3556FF283A618.
- PDF opened or rendered: no.

Successful compilation only records completion of the engine process for the current TeX. It does not validate source fidelity, formulas, semantics, terminology, translation quality, or appearance.

## Source-defect rule

Any precise Noether source defect belongs to a separate checker. That checker must deduplicate it and ensure 4 -nterslav sees it; this producer does not adjudicate or independently route source-defect claims.

