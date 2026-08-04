# Paper 12 controlled-Hant math-protection wrapper repair record

## Boundary

Controlling user instruction:

> you do not check - you translate - other sessions CHEWCK

This record covers a mechanical script-transport guard. It is not source comparison, formula-content checking, semantic review, terminology review, translation-quality review, Traditional Chinese regional localization, visual QA, approval, publication, archive work, or certification.

## Append-only wrapper history

1. The initial Hant conversion wrapper applied raw s2t conversion without first excluding recognized math spans.
2. Its mechanical postcondition detected that recognized math spans had changed.
3. The wrapper stopped before writing a Hant target or OpenCC record. No failed-target or failed-record hash is asserted because those files were not written.
4. The final script was changed to exclude recognized math spans from OpenCC conversion.
5. On the final Hans input it recognized and excluded 130 math spans, converted the remaining text, restored the protected spans, and mechanically confirmed that all 130 recognized spans were retained.
6. The same final run mechanically confirmed that the ordered stream of 901 TeX control sequences was retained.
7. It then applied the recorded controlled generic character normalizations and wrote the current Hant TeX and producer record.
8. The Hant target subsequently completed two XeLaTeX passes with exit code 0 and 5 pages reported on each pass. The PDF was not opened or rendered.

Recognition by a wrapper pattern and equality of the recorded streams do not constitute a formula-content check. They establish only the mechanical transport invariants described here.

## Current input, script, and output custody

- Hans input TeX: zh-Hans-CN\Noether_Paper12_Chinese_CurrentAuthority_zh-Hans-CN_v001.tex
- Hans input bytes: 17,444
- Hans input SHA-256: E98FC0F0B6B33D0E63C07DFBAC47A55CF9BCB601842013B22F72A2B78460BA77
- Final Hant producer script: qa\build_hant_producer.py
- Final Hant producer-script bytes: 6,431
- Final Hant producer-script SHA-256: 1D3248C27B938C7B0F744D875E0D87311E4C83CD5F984F291F405D2224CF8C0D
- Converter: opencc-python-reimplemented 0.1.7
- Configuration: s2t
- Recognized math spans protected and mechanically retained: 130
- TeX control sequences mechanically retained in order: 901
- Current controlled-generic Hant TeX bytes: 17,786
- Current controlled-generic Hant TeX SHA-256: 413FB3EDCB5E3C789137353DE670137AC2AEF4135A428E5AB6C58358DCA49CE3
- OpenCC producer-record SHA-256: E02D19A85D86D8032461619D219D242B0140374F12DBBF724E2EF060129A1756

The final OpenCC record’s raw_opencc_output_utf8_sha256 value, 201772E00BB43887D65E1F9DF78D0383E15958F3C485A4FBB197ED991AFC93A2, describes the final protected conversion stream before controlled normalizations. It is not a hash of the aborted unprotected attempt.

## Runtime custody recorded by the final wrapper

| Runtime component | SHA-256 |
|---|---|
| opencc-python-reimplemented 0.1.7 METADATA | 0DA812FD9236BE4F841553350A64DCF76F84DD580DE99320B6E3030C1B9C7A4B |
| s2t.json | 246F559AAF3756B280157F4EB2AB1DD22F31EBAC2A9E0AAFA2B4A99C1CB676CE |
| STPhrases.txt | A4DE4D2471F73CDB7E5B1B22920139AA4E4BBB1EBEEA8F1FC341F988AA75C586 |
| STCharacters.txt | 9207708DA9F2E2A248F39C457B2FCCAD26EC42E7EFAF47A860E6900464F4CAC5 |

## Final mechanical build custody

- Hant compile script SHA-256: 06B93CE6EDB5EB8E0D6A4D042DEAADF157228BB44425BAB9EA177628EB09F135
- Final Hant PDF bytes: 244,189
- Final Hant PDF SHA-256: A3E65D85FD1FB21E6404040A31FE711E5D25BCB53E56299302414E83544FA872
- Final Hant engine-log SHA-256: 82065B469A6AF78341309FB44964C7F65CCDBCBE63173986EC32D5E2D1AB4428
- Hant build-record SHA-256: C746B22F073B1FB0D18C0D6D4E9250DBF8177F65826658B52DB5C1F0D5A79497
- Successful passes: 2 of 2
- Pages reported: 5 per pass
- PDF opened or rendered: no

## Localization status

The output is controlled generic Traditional script only. The Hans producer wording remains its lexical base. It is not zh-Hant-TW, zh-Hant-HK, or zh-Hant-MO prose, and no regional-language claim is made.

