# Noether Paper 35 Chinese producer build report — revision 3

Revision 3 is a Hant-only producer correction under `ZHCHK-P35-F015`. Exact `zh-Hans-CN` v002 is independently accepted and was neither edited nor rebuilt.

## Controlled-generic Hant v003

- Input Hans TeX: 31,328 bytes, SHA-256 `DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C`.
- Output Hant TeX: 31,515 bytes, SHA-256 `54DE9B43850376FD19306A11FC682166D8F34A4CA6D73E0940695357CE74A005`.
- Sealed checker-candidate whole-file equality: true.
- Math spans: 487/487 equal; TeX controls: 790/790 equal; legacy false display spans: zero.
- XeLaTeX: MiKTeX-XeTeX 4.18 / MiKTeX 26.5, two serial passes, exit codes `0/0`, six pages each.
- Final PDF: 284,874 bytes, SHA-256 `65A449AA0E9C727BEA548C1A8190568636F8C05AB63593666065F956B40774FA`.
- Final log: 23,191 bytes, SHA-256 `F8729C786730A84A83FB94FC6335768356BE3328DF74C72CB9670B07F7FA6573`.
- Per pass: two font-warning lines, one underfull hbox at TeX lines 112--114, zero overfull boxes/vboxes, zero error-pattern matches.
- Pass-1 PDF hash was recorded as `1A0A1B74CAD61C1618F9003E4E8D97BF19FE860A9A84519D74D80C14F8D1F5BE`; pass-1 PDF bytes were replaced by pass 2 and are not a separately retained artifact. Both pass engine logs are retained.

## Exact records

- Transport record: `controls/OPENCC_PRODUCER_RECORD_v003.json`, SHA-256 `D7087C586E78887CD5DB4339DDA6C5E9E535F5D8CF1EF6C15F07DBBF71549BFE`.
- Build record: `controls/HANT_MECHANICAL_BUILD_RECORD_v003.json`, SHA-256 `2DB562C01A72D30171EEC4082A5D7B1746752C1FB6CBB3DB79788C9B25D43BA1`.
- Warning annex: `controls/P35_HANT_V003_WARNING_ANNEX.json`, SHA-256 `F9E1E38ED456DB2ECF4F9F4FB83100522D906FE58DC8190DEEFA7F84A42D1AEE`.
- Realization record: `controls/P35_F015_PRODUCER_REALIZATION_RECORD.json`, SHA-256 `2B6E82F1C53573CBA67AB377C794FBC64683A3BFDA374AC460710FB47288FB66`.

## Claim limit

The producer performed mechanical generation, exact candidate equality checks, compilation, hashing, and custody recording only. The producer did not open/render the PDF or perform source, semantic, formula, terminology, translation-quality, visual, native, or regional review. Compilation is not acceptance. Independent checker task `019fca9c-f549-7e71-a314-66f7265343ca` must recheck the frozen package.

