# Noether Paper 12 Chinese producer mechanical build report

## Claim limit

This report records translation packaging and compile-driven mechanics only. The controlling user boundary is:

> you do not check - you translate - other sessions CHEWCK

No source/witness comparison, source check, semantic or formula-content check, terminology or translation-quality review, PDF opening or rendering, Hant regional localization, approval, archive/publication action, external validation, or certification was performed.

Artifact hashes were read from the files at 2026-07-22 12:16:30 +02:00 and the current target/build-record hashes were re-confirmed at 2026-07-22 12:17:07 +02:00.

## Hans assembly inputs and output

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| segments\P12_STANDALONE_PREAMBLE.tex | 1,579 | 40AF841CA662EF08A0B7E98425529CEBCCE0AE6E01210D4F945611C12D29EA18 |
| segments\zh-Hans-CN\P12_A_zh-Hans-CN.tex | 4,263 | 65CB2373945FCC6973010CD29729E354DF892A4C4CDFC4E215D2E44755CDAF01 |
| segments\zh-Hans-CN\P12_B_zh-Hans-CN.tex | 5,209 | D8FEB6D63E9D837228503846D8B653954A36BFDC43443DC3CA4B379493502563 |
| segments\zh-Hans-CN\P12_C_zh-Hans-CN.tex | 6,377 | 23A21B0C662BA365ACC0373A5950C38C98577D06FD1059779B4F74B5AFA1DE64 |
| segments\P12_STANDALONE_POSTAMBLE.tex | 16 | D23C000D5CB7805066714CA6DB35A997F641E5209A2F60B139D1B48A482EBA44 |
| assembled zh-Hans-CN TeX | 17,444 | E98FC0F0B6B33D0E63C07DFBAC47A55CF9BCB601842013B22F72A2B78460BA77 |

Hans assembly record SHA-256: 13177604B67E038CCD50CEBBB614A345D28B9C757086AEFE15FD8EF27A43B727.

## Append-only Hans compile and syntax-repair chronology

1. Segment C first returned as SHA-256 7D2F1043466CCD6CA303D3CC257C02821F418CED70928C0F727C3F49C02D14DF.
2. A first Hans pass-1 invocation exited 1 on a missing inline-math delimiter and left an incomplete 2-page PDF. That incomplete file was not opened or rendered and is not a final artifact.
3. The parent mechanically restored only two missing math delimiters. Segment C then had SHA-256 2022CF8A46B94849908793733D7629E9867972DEBC4CB7B197C734C550AEF591. No prose wording was changed.
4. A second Hans pass-1 invocation exited 1 on remaining missing inline-math delimiters and left an incomplete 3-page PDF. That incomplete file was not opened or rendered and is not a final artifact.
5. The segment translator mechanically restored the remaining intended inline delimiters without changing prose. Final segment C SHA-256: 23A21B0C662BA365ACC0373A5950C38C98577D06FD1059779B4F74B5AFA1DE64.
6. The final unchanged-prose Hans assembly was written with SHA-256 E98FC0F0B6B33D0E63C07DFBAC47A55CF9BCB601842013B22F72A2B78460BA77.
7. The final assembly completed two XeLaTeX passes with exit code 0 on each pass. The final log reports 5 pages.

The failed invocations were compile triggers for TeX delimiter restoration. They were not formula checks, semantic checks, or translation review.

## Final Hans build artifacts

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| zh-Hans-CN TeX | 17,444 | E98FC0F0B6B33D0E63C07DFBAC47A55CF9BCB601842013B22F72A2B78460BA77 |
| zh-Hans-CN PDF | 226,917 | 5D7BF4C532933491F28E0ECC80A9AA4D5D23AA621A4C5B9A006390BD2AA2BB12 |
| final engine log | 20,713 | E7FC3618C70EEC2E1D4F24B758F77E20678F86B4C71757947E2E8F6024BE6D7E |
| final pass-1 stdout | 3,697 | 270B7E45BCFB1A8A35D0B2B811A0314F9902B4D40FCAD0E83947AA6565C1FA2B |
| final pass-2 stdout | 3,697 | 270B7E45BCFB1A8A35D0B2B811A0314F9902B4D40FCAD0E83947AA6565C1FA2B |

Final build record SHA-256: C2BB357A8D4581A4C2DF7CD26CF28F766874BBA59653A78CE25A5E7A2F002AEF.

The initial completed build-record file had SHA-256 FCA11B143217F4059B3777AB8621F39B7DAE07E5CE76B77AE319044B6C315DE3 and stored pages_reported_by_log as null because its wrapper regex did not cross MiKTeX’s wrapped log line. The metadata-only reparse used the narrower pattern \((\d+) pages? and stored 5. No TeX, PDF, engine output, or translation changed; XeLaTeX was not rerun and the PDF was not viewed. Reparse record SHA-256: D91721BAA42616BA86C9F6BBD56A9F176E50958D62BBA092E1E337ED0AF5BB60.

## Controlled-generic Hant transport chronology

1. The first Hant conversion wrapper attempted unprotected raw s2t conversion.
2. Its mechanical invariant detected that recognized math spans had changed.
3. The wrapper stopped before writing a Hant target or OpenCC record. Therefore no failed-target hash is asserted.
4. The final producer script was changed to exclude 130 recognized math spans from conversion.
5. The final script mechanically retained all 130 recognized math spans and an ordered stream of 901 TeX control sequences, then wrote the controlled-generic Hant target and record.
6. These pattern-based transport invariants establish only the script behavior that they record; they are not formula-content, source, semantic, linguistic, or terminology validation.
7. The final controlled-generic Hant target completed two XeLaTeX passes with exit code 0 and 5 pages reported for each pass. No PDF was opened or rendered.

## Final Hant artifacts

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| controlled-generic zh-Hant TeX | 17,786 | 413FB3EDCB5E3C789137353DE670137AC2AEF4135A428E5AB6C58358DCA49CE3 |
| controlled-generic zh-Hant PDF | 244,189 | A3E65D85FD1FB21E6404040A31FE711E5D25BCB53E56299302414E83544FA872 |
| final Hant engine log | 20,780 | 82065B469A6AF78341309FB44964C7F65CCDBCBE63173986EC32D5E2D1AB4428 |

- OpenCC producer record SHA-256: E02D19A85D86D8032461619D219D242B0140374F12DBBF724E2EF060129A1756
- Hant build record SHA-256: C746B22F073B1FB0D18C0D6D4E9250DBF8177F65826658B52DB5C1F0D5A79497
- OpenCC converter: opencc-python-reimplemented 0.1.7, configuration s2t
- Hant status: controlled generic Traditional script only; not zh-Hant-TW, zh-Hant-HK, or zh-Hant-MO prose

## Producer scripts

| Script | SHA-256 | Mechanical role |
|---|---|---|
| qa\extract_exact_slices.ps1 | 366F1225372DC1E85342DD4E61BB156730F30C3A7DFCC1F73B39153052A578DD | exact line/byte snapshot extraction |
| qa\assemble_hans_producer.ps1 | 05F8902E37A69980BE8DE89DB08AA31D193FCE60DF79F0C4512252E31C51E533 | deterministic Hans concatenation |
| qa\compile_hans_producer.ps1 | 9457BD87448B3DC639CE026F9C0B4DCFE9935ADD5239C23ACAD81EC078B840DA | two-pass Hans XeLaTeX wrapper |
| qa\reparse_hans_page_count.ps1 | 1ABA7EA45A377820CAF36808A503F1A9EE085D77CD847599346571DDD050DCF4 | completed-log page-count metadata repair |
| qa\build_hant_producer.py | 1D3248C27B938C7B0F744D875E0D87311E4C83CD5F984F291F405D2224CF8C0D | protected controlled-generic Hant script transport |
| qa\compile_hant_producer.py | 06B93CE6EDB5EB8E0D6A4D042DEAADF157228BB44425BAB9EA177628EB09F135 | two-pass Hant XeLaTeX wrapper |

Successful compilation proves only that these current TeX inputs completed the recorded engine process. It does not validate the translation or the formulas.

