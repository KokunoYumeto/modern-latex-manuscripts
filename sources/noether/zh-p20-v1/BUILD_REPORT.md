# Noether Paper 20 Chinese producer mechanical build report

## Claim limit

> you do not check - you translate - other sessions CHEWCK

This report records translation packaging and compile-driven mechanics only. It records no source/witness comparison, source check, semantic or formula-content check, terminology or translation-quality review, PDF opening/rendering, Traditional-Chinese regional localization, approval, publication/archive action, external validation, or certification.

## Hans assembly

| Assembly input | Bytes | SHA-256 |
|---|---:|---|
| segments\P20_STANDALONE_PREAMBLE.tex | 1,575 | D129A0DEC1FBA1F7048705A33035136F82DE8A8E29918D39FF4BCCCA2FFD8BFB |
| segments\zh-Hans-CN\P20_A_zh-Hans-CN.tex | 7,057 | DC694B77A78B1D12E12BC5A3DA315147538847F23F0E46772D85A7BAE9181834 |
| segments\zh-Hans-CN\P20_B_zh-Hans-CN.tex | 6,332 | 143C7386FCB9DDA7159C2F7D9A2C9547530D9AED786648A85ACD488D14A8A491 |
| segments\zh-Hans-CN\P20_C_zh-Hans-CN.tex | 5,265 | 8972FC4AA515FF93047D0F686DFD9CCB4003287E2F815313F02BAC079ED9D734 |
| segments\P20_STANDALONE_POSTAMBLE.tex | 16 | D23C000D5CB7805066714CA6DB35A997F641E5209A2F60B139D1B48A482EBA44 |
| assembled zh-Hans-CN TeX | 20,245 | 262430D0A092818F859516F3FD5DE612D897D0BD8AAC49605BE047E389963065 |

Hans assembly record SHA-256: 39A4D15DEBEC4E45D3032B9554A6D83B552957031074264ECC5D3DB66A673B2D.

## Append-only Hans compile and delimiter-repair chronology

1. Segment A first returned at SHA-256 B637B38DBD55BCF8BA6862F000B48D9108FC77F8D42D083762A5AE97081559FC.
2. Pass 1 stopped at the first un-delimited (n\ge2) and produced no pages.
3. Only that delimiter was restored, producing SHA-256 51BDBA85125DC72494746B49540FD6EF5DE21D7DD2854F86558B726E06586B3F.
4. Pass 1 stopped at the second un-delimited (n\ge2) and produced no pages.
5. Only that delimiter was restored, producing SHA-256 F4317188496FE61F220343C1C941E7D6F7EF02707F463D3FA208203963BD1AC6.
6. Pass 1 stopped at the third un-delimited (n\ge2) and produced no pages.
7. Only that delimiter was restored, producing SHA-256 80AA4F63166554C74EB29806CF1DCE77A6C98F1DB31EC181FD1BF9A372CCC4DC.
8. Pass 1 then produced one page and stopped at malformed (F(x,y)\).
9. Only that delimiter was restored, producing current segment-A SHA-256 DC694B77A78B1D12E12BC5A3DA315147538847F23F0E46772D85A7BAE9181834.
10. The final assembled Hans TeX was written at SHA-256 262430D0A092818F859516F3FD5DE612D897D0BD8AAC49605BE047E389963065.
11. The final assembly completed two XeLaTeX passes with exit code 0; the final log reports 5 pages.

Every repair restored TeX delimiters only and changed no prose. Failed builds were not viewed. This chronology is not formula or content checking.

## Final Hans artifacts

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| zh-Hans-CN TeX | 20,245 | 262430D0A092818F859516F3FD5DE612D897D0BD8AAC49605BE047E389963065 |
| zh-Hans-CN PDF | 235,218 | DF04B292EB1DDC80B8B1637406B7416EBF4CA947E06018D865F98424B72EA54D |
| final engine log | 21,148 | D4599B1218F1BC885E6F7CA3322BE71B5F9CAAA94D97E6C8B311917BFE884D13 |
| pass-1 stdout | 4,014 | 98CDAC0F58707FC1605821E1B2A80D3B3C8BE68A59B56378C30804594BC0084D |
| pass-2 stdout | 4,014 | 98CDAC0F58707FC1605821E1B2A80D3B3C8BE68A59B56378C30804594BC0084D |

Hans build record SHA-256: 78CE6579A83531D42FBD3007042AA69BF742DCEF35D68F558234DF91F685B779. The final log contains two font-warning lines concerning unavailable italic CJK font shapes and substitution. It contains no overfull or underfull line. The PDF was not opened or rendered.

## Controlled-generic Hant transport

- Input Hans TeX SHA-256: 262430D0A092818F859516F3FD5DE612D897D0BD8AAC49605BE047E389963065.
- Producer script SHA-256: 11E74A3830A8EB0A181328C94A2FCC1E97F7C38563C9D4A4AD29FC875E7031C2.
- Converter: opencc-python-reimplemented 0.1.7, configuration s2t.
- Raw protected conversion stream SHA-256: F700CCD33B82BA33F6C470653F023B9F2BA253C4EEF0248008B04833BFB575A4.
- Recognized math spans protected and mechanically retained: 220.
- Ordered TeX control sequences mechanically retained: 742.
- Controlled-generic Hant output SHA-256: 17EE7ECD25A298D8818144CE41273A31DEB85F3E49A02F08D5335B6815FF20C0.
- OpenCC producer record SHA-256: 80A7FC6B1D859A63CC4BC602CC289860098EA317BE158D32D3BEE048CD541B76.

These pattern-based invariants describe script behavior only. They are not formula-content, linguistic, source, semantic, terminology, or regional validation.

## Final Hant artifacts

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| controlled-generic zh-Hant TeX | 20,587 | 17EE7ECD25A298D8818144CE41273A31DEB85F3E49A02F08D5335B6815FF20C0 |
| controlled-generic zh-Hant PDF | 257,407 | 286400FD8AECE3D86AABC06855B53E9817A2C58AC1ED5952DF14086FAB7488EA |
| final Hant engine log | 21,222 | 12A88EA8BCD7FA0BB52AF870CF82DE475B1D65D5C054714203DEF0A8B6931999 |

- Hant pass 1 stdout SHA-256: D2EEC880AB2E635FB8B388E0C620F01AC224DFC89762C9B5F45239D2AF18E5F9.
- Hant pass 1 retained engine-log SHA-256: 2E951D75AAE4065728223F7D5051D22FC277AD88E6F3A80E30953E7D8CDBB8D3.
- Hant pass 2 stdout SHA-256: 0522D86533F59498FF490F3E12331797FADD30A925A1D7472DDA66D2F529EACC.
- Hant pass 2 retained engine-log SHA-256: 12A88EA8BCD7FA0BB52AF870CF82DE475B1D65D5C054714203DEF0A8B6931999.
- Hant build record SHA-256: D71DB684736DCE854A98C1FBF5548A8CC00D173F244F95D8C9CEB8F31BEB2FF9.
- Both passes exited 0 and reported 5 pages.
- Each retained engine log records two font-warning lines and no overfull/underfull lines.
- No PDF was opened or rendered.

The Hant output is controlled generic Traditional script only, not zh-Hant-TW, zh-Hant-HK, or zh-Hant-MO prose.

## Producer scripts

| Script | SHA-256 |
|---|---|
| qa\extract_exact_slices.ps1 | F0565D771C40D252B90FFB2E99A0B2B33ACB540A347F704BC08FFB8CFC1C1489 |
| qa\assemble_hans_producer.ps1 | DB928612D71EED2589EFDE9DE115BDCFD8BB010DE220D1469F7BA1A3416BD102 |
| qa\compile_hans_producer.ps1 | DF784B173F6D5D2B8CAC6918B49A0941476CBD11D8E4EF5BD1A6B67FEBA2B3A4 |
| qa\build_hant_producer.py | 11E74A3830A8EB0A181328C94A2FCC1E97F7C38563C9D4A4AD29FC875E7031C2 |
| qa\compile_hant_producer.py | 2FDD1925C403563AEB93C3F4B1EE8DE1031D2A9F05E85F95104BFD74967C9626 |

Successful compilation proves only completion of the recorded engine process.

