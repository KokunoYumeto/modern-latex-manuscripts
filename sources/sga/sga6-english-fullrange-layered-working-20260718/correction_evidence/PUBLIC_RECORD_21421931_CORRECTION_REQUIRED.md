# Zenodo record 21421931 — corrective version required

Verification date: 2026-07-18  
Concept DOI: `10.5281/zenodo.20410947`  
Published version DOI: `10.5281/zenodo.21421931`  
Disposition: **PUBLISHED PUBLIC FILE IS STALE; PARENT-COORDINATED CORRECTIVE VERSION REQUIRED**

## Verified public state

Zenodo's public Records API reports record 21421931 as published, current (`is_last: true`), and part of the existing concept record. The exact API response is preserved as `controls/ZENODO_RECORD_SNAPSHOT_20260718_RECORD21421931.json`, SHA-256 `D9D2579BA93B18EE4469041627B77B7A979C1607C4A0B4A542E079ECE750FB27`.

The public SGA 6 reader is:

- file: `02_SGA6_English_FullRange_Layered_WorkingReader_NotCritical_20260718.pdf`;
- bytes: 2,567,119;
- public-file SHA-256 independently downloaded and verified: `29CEEA7CE5ECBA9A8C36D34E170D19AAC8C014D64836FEAA77D723CB0F361939`;
- Zenodo MD5: `34ebae93739c25e02dc7693eeaf15b3a`;
- 381 A4 pages;
- PDF creation time: 2026-07-18 03:10:54 +02:00.

The public English support ZIP is:

- file: `06_SGA6_English_FullRange_TeX_Ledgers_and_RenderQA_20260718.zip`;
- bytes: 124,315,898;
- SHA-256 independently downloaded and verified: `ED9CEC2D320041B626D5DDE424D651834C8961FE541C8253631FF5622AF8A2AC`;
- Zenodo MD5: `526351284b909b413fa041d7b71ba957`.

## Material stale-state defect

The public PDF visibly prints Lemma 5.8.2 formula marker 14 on physical PDF page 81 but omits the corresponding source footnote entirely. The public ZIP proves the cause in its prefix TeX:

```tex
\longrightarrow G.\text{\begin{NoHyper}\footnote{...}\end{NoHyper}}
```

The footnote command is executed inside an amsmath display and its insertion is lost. `pdftotext -f 81 -l 81 -layout` on the public PDF contains marker 14 but no footnote-14 text, and a full-page render confirms there is no footnote at the bottom of the page.

This is the exact regression caught and repaired after the public package's 03:10 build. Therefore record 21421931 is not the final corrected endpoint described by the later internal QA.

## Corrected internal endpoint

- corrected prefix TeX: SHA-256 `3FE03C89BA0662A61607CDE80DDB24BC4683FA37C30C1DA580908CFAD186F68C`, 812,912 bytes;
- corrected complete PDF: SHA-256 `F8B1E15754BEB5C83CF2A47B261D6F9F907DE5B7E8A6ED4DF311C624E38C7B8E`, 2,565,870 bytes, 381 A4 pages;
- corrected page 81: marker 14, footnote number 14, and complete note text;
- complete visual QA: `render_check/complete_working_edition/VISUAL_QA_COMPLETE.md`, SHA-256 `C3AD4FF832E2CD18BC2072A40397C930730E911F77F2A5158D379490FB90D2FA`;
- independent integration review: `controls/final_independent_review/INDEPENDENT_REVIEW_COMPLETE.md`, SHA-256 `1CEF0C05B477ECB96F2FF61A4F0795AA6F808BD3BABA6EB4D554317465A5F1EC`.

## Required parent action

Do not mint a duplicate concept record and do not overwrite the historical fact of version 21421931. The parent English/Germanic manager should coordinate a corrective **new version under the same concept DOI**, using the corrected PDF/TeX/package only after confirming their exact receipts and retaining the layered-authority caveats. The new version metadata should state that it corrects the missing Lemma 5.8.2 footnote in the prior version.

This Codex task did not upload, modify, or withdraw any Zenodo record. Zenodo's CC0 record metadata also does not by itself resolve the source-scan, inherited-translation, derivative-license, or attribution questions documented elsewhere in this workspace.
