# Source comparison: SGA 6 English prefix gates

## Authority and coordinates

The low-resolution 702-page scan is the ultimate source witness. The current French workpass is the transcription/translation control, not the origin of the inherited English. The 720-page high-resolution scan corroborates difficult glyphs and orientation. Current-rescribe indices do not exist for these inherited prefix pages and were not invented.

| Source-PDF page | Printed volume page | High-resolution page | English TeX lines | Source finding | Disposition |
|---:|---:|---:|---:|---|---|
| 277 | 270 | not needed | 6917--6928 | The inherited proof compressed the exact truncation hypotheses and stalk/cycle identifications; Corollary 5.6 lost the minus in `D^{-}(X)`. | Restored from the scan and French control (French lines 6036, 6038). |
| 286 | 279 | not needed | 7185--7195 | The displayed definitions are clean. A footnote governing omission of the index `A` and of “naive” was absent. | Footnote restored from the scan and French control line 6237. |
| 347 | 340 | not needed | 9152--9180 | The final identities (5.4.1), (5.4.2) were algebraically correct, but their finite-rank hypotheses, expansion, and cancellations had been compressed away. | Full source derivations restored; the final identities are unchanged in substance. French control lines 7689--7709 corroborate. |
| 350 | 343 | not needed | 9213--9226 | The inherited relation used `lambda^k(N'_0)=0`; the scan clearly uses `gamma^k(N'_0)=0`. The weight-filtration citations and homomorphism argument were compressed. | Corrected to `gamma`; restored (4.12), (4.15), (5.5.4), 4.7, augmentation and filtration compatibility. French control line 7775 corroborates. |
| 377 | 370 | 384 | 10073--10147; 10386 | The low scan leaf is physically upside down. After reorientation it shows the proof of Corollary 1.4 and complete Lemma 1.5.1, both omitted in the inherited English. Subsequent labels were therefore shifted. | Restored the omitted proof and lemma; synchronized Lemma 1.5.2, Propositions 1.6/1.7, §§1.8/1.9 and downstream references. French control lines 8625--8675 and high-resolution page 384 corroborate. |
| 431 | 424 | not needed | 11014--11113 | The audit required confirmation that repair105's expanded Proposition 1.8 survived extraction. | Retained exactly. Normalized LF extraction of lines 11014--11113 plus terminal LF is 7,148 characters and SHA-256 `6641F4AF065BF59773756A251002BCC115DAD0243E4E23CE26D882F129564F7F`, identical to repair105. |

## Source files

- Low scan: `C:\Users\Floris\Documents\Papors\OS\sga6.pdf`, 54,325,694 bytes, SHA-256 `5194436E290B8FCA54BACD5FF672588335408F1AAD3AE07D62BBA68DF35E3D76`.
- High-resolution supplement: `C:\Users\Floris\Documents\Papors\OS\Théorie des Intersections et Théorème de Riemann-Roch.pdf`, 26,833,956 bytes, SHA-256 `73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA`.
- French control: `C:\IL_GitHub\00_main_current\sources\sga\sga6-claude-workpass-source-rescribe-20260704\sga6_fr_workpass.tex`, 1,318,579 bytes, SHA-256 `77703F2D7E8FF9000C2C1E7320A903A48ADE00BF62C8F5F240FF88C42ED82703`.
- Inherited baseline: `repair108_unsynced/sga6_en_unsynced_baseline_repair108.tex`, preserved and unedited.

## Rejected evidence mapping

`source_renders/highresPDF_395_sourcePDF_377.png` is preserved as a mapping trial. It is printed page 381 and does not correspond to low-scan source-PDF 377. It was not used as authority. The correct high-resolution corroborating leaf is page 384, printed page 370.

## Scope caveat

“Resolved” here means these six audit gates are source-adjudicated. The prefix as a whole remains accurately labeled “inherited, partially source-synchronized through source page 525” until all other prefix gates are independently closed.

