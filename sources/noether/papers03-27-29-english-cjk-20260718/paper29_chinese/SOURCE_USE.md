# Source use and source check

## Controlling German authority

Sealed P31 cumulative TeX:

`private-local://Documents/Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP\1\01_current\cum_de_Local_20260718_P31.tex`

SHA-256: `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`.

The exact raw Paper 29 byte interval is stored at `source/Noether_Paper29_German_P31_Sealed_exact_slice.tex`, SHA-256 `904488A1630B36E12352A3313B16CC9283B345E28E5363E48B7E4757B388128F`. At final freeze it occurred exactly once in the sealed P31 head at byte offset 1,239,963.

The later unsealed candidate, cumulative SHA-256 `C243961810AD2EE10E866007620BBCDAFE2EF5305A1CAD040B5EA7E6ADDC2C39`, contains the same exact Paper 29 byte slice at the same offset. Its change is outside this unit, in Paper 30; it was checked but not promoted over the sealed head.

## Prohibited shared pointer

`private-local://Documents/interlanguage\03_projects\noether\00_current_german_authority` was re-inspected and still contains R821-labelled authority files. It is stale and was not used. The owner-level pointer-update debt remains open.

## Translation witness

The inherited cumulative Simplified Chinese source has SHA-256 `C2936EFAC3C22FBEBD3E5F418902A0A4CA3CFFD953DC3ADC827432D7529DF3F9`. Its declared Paper 29 block is frozen at `witness/Noether_Paper29_SimplifiedChinese_Inherited_exact_slice.tex`, SHA-256 `9C13B87F9E50D8B0519986E734F128190EAD93BEF32EFB65636B09E3A044067D`.

Because its mixed R122/R124/R823-era ancestry is not synchronized to P31, it served only as a translation witness. The structural extractor's boundary defect is preserved separately as adverse evidence; it was not allowed to set the source boundary.

## Independent Chinese evidence

The native evidence ledger records exact anchors in:

- ECNU commutative algebra material, PDF SHA-256 `C84AC610F21076DF2EC3AB6737D0713D1C84D3A84B38D2FAC42EAFEB3760C862`.
- HFUT algebraic number theory material, PDF SHA-256 `07E693EFBCCEBFE8AFD868C764D140F624DACD0028409B1D232F9BA068563B8D`.
- HFUT representation-theory material, PDF SHA-256 `01C390945C8795BF481E6B429B20579751075C6C712736669FCFE5854AB53C49`.

The ledger separates support, competitor, adverse, and absence evidence. In particular, native `整基` in the number-field integral-basis sense is adverse evidence against using bare `整基` for Noether's finite algebra-generating-system sense.

No OCR or VLM output was promoted as authority. No Chinese source is used to authorize Japanese or Korean, and PRC Simplified evidence is not used to authorize Singapore or regional Traditional standards.

## Source-structure result

Final checks pass for the author block, 22 emphasis loci, 15 unique footnotes plus the repeated Artin marker, the semicolon-separated field presentation, Hilbert and Artin note loci, the unindexed resolvent product, all 15 `\overline P` occurrences including the three in §2.3, and the displayed mathematical relations. Details are in `qa/source_alignment_checks.json`.
