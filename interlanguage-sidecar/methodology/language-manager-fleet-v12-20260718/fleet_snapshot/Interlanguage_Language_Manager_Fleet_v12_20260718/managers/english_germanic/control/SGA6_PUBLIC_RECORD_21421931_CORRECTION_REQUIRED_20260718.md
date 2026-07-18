# Parent alert — SGA 6 Zenodo record 21421931 needs correction

Record `10.5281/zenodo.21421931` is real and current under concept DOI `10.5281/zenodo.20410947`, but its public SGA 6 English PDF and ZIP were frozen before final footnote repair.

- public PDF SHA-256 `29CEEA7CE5ECBA9A8C36D34E170D19AAC8C014D64836FEAA77D723CB0F361939`: page 81 has marker 14 but no footnote text;
- public ZIP SHA-256 `ED9CEC2D320041B626D5DDE424D651834C8961FE541C8253631FF5622AF8A2AC`: prefix TeX uses the failed amsmath-inline `\footnote` insertion;
- corrected internal PDF SHA-256 `F8B1E15754BEB5C83CF2A47B261D6F9F907DE5B7E8A6ED4DF311C624E38C7B8E`: page 81 has matching marker/footnote 14 and full text; complete visual QA and independent review PASS.

Do not mint a duplicate concept record. Coordinate a corrective new version under the existing concept DOI and state that it restores the missing Lemma 5.8.2 footnote from version 21421931. Full verification is in:

`03_projects\language_management\english_germanic\03_working_translations\sga6_complete_layered_sync_sourcePDF001_702_en_20260718\controls\PUBLIC_RECORD_21421931_CORRECTION_REQUIRED.md`
