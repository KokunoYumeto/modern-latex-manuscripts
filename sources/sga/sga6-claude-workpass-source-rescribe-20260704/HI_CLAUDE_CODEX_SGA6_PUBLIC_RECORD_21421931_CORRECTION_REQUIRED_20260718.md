# Hi Claude — public SGA 6 record 21421931 needs a corrective version

**Resolved 2026-07-18:** corrective version
[`10.5281/zenodo.21422245`](https://doi.org/10.5281/zenodo.21422245) is live
under the same concept DOI. Its reader SHA-256 is
`F8B1E15754BEB5C83CF2A47B261D6F9F907DE5B7E8A6ED4DF311C624E38C7B8E` and
its corrected TeX/ledger/render-QA ZIP SHA-256 is
`42B9371BE6A031E459A2F77ED27C56F34A11C1E9BBC7B015DFB6DF2E4236F7E8`.
Both files were downloaded from the public record and re-hashed exactly.
Record 21421931 remains only as the historical defective predecessor.

Zenodo version DOI `10.5281/zenodo.21421931` was published concurrently while final English QA was still resolving Lemma 5.8.2's restored footnote.

The public reader SHA-256 `29CEEA7CE5ECBA9A8C36D34E170D19AAC8C014D64836FEAA77D723CB0F361939` is stale: on physical PDF page 81 it shows formula marker 14 but omits footnote 14 entirely. The public support ZIP SHA-256 `ED9CEC2D320041B626D5DDE424D651834C8961FE541C8253631FF5622AF8A2AC` contains the failed inline-display `\footnote` method that loses the insertion.

The corrected internal endpoint is:

- prefix SHA-256 `3FE03C89BA0662A61607CDE80DDB24BC4683FA37C30C1DA580908CFAD186F68C`;
- complete PDF SHA-256 `F8B1E15754BEB5C83CF2A47B261D6F9F907DE5B7E8A6ED4DF311C624E38C7B8E`;
- page 81 visibly has marker 14, footnote 14, and the full note;
- 381-page visual QA and independent integration review both PASS.

Full evidence:

`C:\Users\Floris\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\sga6_complete_layered_sync_sourcePDF001_702_en_20260718\controls\PUBLIC_RECORD_21421931_CORRECTION_REQUIRED.md`

Please do not treat 21421931 as the final corrected English endpoint. Do not mint a duplicate concept record. The parent manager should issue a corrective new version under concept DOI `10.5281/zenodo.20410947`, explicitly noting the restored Lemma 5.8.2 footnote. This note does not modify `sga6_fr_workpass.tex`.
