# Noether Paper 12 Chinese producer status

Snapshot: 2026-07-22 12:17:07 +02:00.

## Producer outcome

Paper 12 has a complete PRC-oriented Simplified Chinese producer translation, a deterministically assembled editable TeX target, a mechanically derived controlled-generic Traditional-script target, and two successful XeLaTeX passes for each target. This is producer completion only. Independent checking is pending, and no approval, publication, archive, or certification state is claimed.

Controlling user boundary:

> you do not check - you translate - other sessions CHEWCK

## Current target custody

| Target artifact | Bytes | SHA-256 | Mechanical state |
|---|---:|---|---|
| zh-Hans-CN TeX | 17,444 | E98FC0F0B6B33D0E63C07DFBAC47A55CF9BCB601842013B22F72A2B78460BA77 | assembled from current A/B/C segments |
| zh-Hans-CN PDF | 226,917 | 5D7BF4C532933491F28E0ECC80A9AA4D5D23AA621A4C5B9A006390BD2AA2BB12 | two successful XeLaTeX passes; 5 pages reported by final log |
| zh-Hans-CN final engine log | 20,713 | E7FC3618C70EEC2E1D4F24B758F77E20678F86B4C71757947E2E8F6024BE6D7E | final mechanical build log |
| controlled-generic zh-Hant TeX | 17,786 | 413FB3EDCB5E3C789137353DE670137AC2AEF4135A428E5AB6C58358DCA49CE3 | script transport from Hans; not regionalized |
| controlled-generic zh-Hant PDF | 244,189 | A3E65D85FD1FB21E6404040A31FE711E5D25BCB53E56299302414E83544FA872 | two successful XeLaTeX passes; 5 pages reported by logs |
| controlled-generic zh-Hant final engine log | 20,780 | 82065B469A6AF78341309FB44964C7F65CCDBCBE63173986EC32D5E2D1AB4428 | final mechanical build log |

The producer did not open, render, or visually inspect either PDF.

## Current records

- Source-custody record SHA-256: 09F5B7942159982E1BB00764DF8FB260DED12DB36524C88F053E644FD955546C
- Segmentation record SHA-256: E23F4956C9451324BFAABA6E37EAEE447BBF1B66A4F972C64F130B4FEFE8A2C8
- Hans assembly record SHA-256: 13177604B67E038CCD50CEBBB614A345D28B9C757086AEFE15FD8EF27A43B727
- Hans mechanical build record SHA-256: C2BB357A8D4581A4C2DF7CD26CF28F766874BBA59653A78CE25A5E7A2F002AEF
- Hans page-count reparse record SHA-256: D91721BAA42616BA86C9F6BBD56A9F176E50958D62BBA092E1E337ED0AF5BB60
- OpenCC producer record SHA-256: E02D19A85D86D8032461619D219D242B0140374F12DBBF724E2EF060129A1756
- Hant mechanical build record SHA-256: C746B22F073B1FB0D18C0D6D4E9250DBF8177F65826658B52DB5C1F0D5A79497

## Mechanical adverse history retained

- Two preliminary Hans pass-1 invocations exited 1 because intended inline-math delimiters were missing. They produced incomplete 2-page and then 3-page PDFs before the final unchanged-prose assembly was available.
- Segment C moved append-only through SHA-256 values 7D2F1043466CCD6CA303D3CC257C02821F418CED70928C0F727C3F49C02D14DF, then 2022CF8A46B94849908793733D7629E9867972DEBC4CB7B197C734C550AEF591, then current 23A21B0C662BA365ACC0373A5950C38C98577D06FD1059779B4F74B5AFA1DE64. Only math delimiters were restored; no prose was changed.
- The initial completed Hans build record stored a null page count; a metadata-only reparse read 5 pages from the already completed log. It did not rebuild or view the PDF.
- The first Hant conversion wrapper stopped before writing its target or record because unprotected raw s2t conversion changed recognized math spans. The final script excluded 130 recognized math spans from conversion and preserved those spans plus a stream of 901 TeX control sequences.

These are mechanical repair facts, not source, formula, content, or quality checks.

## Explicitly pending

No source/witness comparison, source check, semantic check, formula-content check, terminology adjudication, translation-quality review, PDF opening/rendering, visual QA, Traditional Chinese regional localization, human or external validation, approval, archive/publication action, or certification has been performed in this producer session. The next authorized state is separate-session checking.

