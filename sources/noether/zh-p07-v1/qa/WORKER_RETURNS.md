# Paper 7 producer worker returns

These are bounded translation/production returns only. None of the workers performed or claimed source checking, semantic/formula/terminology/translation-quality review, PDF rendering/visual inspection, native/regional validation, approval, publication, archive, or certification.

## Translation segments

- `/root/p07_hans_a` translated German segment A SHA-256 `171A565C8BFFCB0BF1AE63405BD0C68E43F7A6898B1544C8CCAC63A48CB2EBAD`; initial Hans return SHA-256 `56E8CB894EB8014282FF4C1CC730CC6045D02F7552643C4DDF18DF9948182B97`. It flagged `einförmig` as unresolved after using `单型`.
- `/root/p07_hans_b` translated German segment B SHA-256 `540329352DF80393946DB81EF6EFFA6CF3F282725AE6170AF2B02F584507209B`; returned Hans SHA-256 `7C8DF21A7D4AA0FFADE22784FEFF8838160B9D09423679FFE2446647F1EBA24A`. It used `单式` and flagged alternatives.
- `/root/p07_hans_c` translated German segment C SHA-256 `35E48B0249F3C25E7E90467B4682A029C21E4C5B4202DCD63BEE277D745F4BB6`; returned Hans SHA-256 `EDC85CFD45A3EB597DEEA836874396713E224C56D73E689121A5D6D13D86B2AE` with no lexical obstacle reported.

The root producer changed only segment A's `单型` to `单式` for internal producer convergence, yielding final A SHA-256 `FF6CBF848BEE518A5E7EF4AD51C34A75A3CB53C339C71C7D562A2BFC86CF5C71`. That is a model preference, not terminology validation; independent review remains pending.

## Controlled Hant and mechanical build

`/root/p07_hant_build` generated controlled-generic Hant from exact Hans SHA-256 `B121BC5D5649F63904444A25179FB4D882F55EF9435A5C81C1689414639BE8F4`, performed two mechanical XeLaTeX passes, and explicitly reported no PDF viewing or regional localization. Returned Hant TeX/PDF/log SHA-256: `36648843726340B02C9B7FF31EEC28008AC3CD66594F469F7769540E29DEFC79` / `A238D9E25FBC44D8D4506D63C66E0CE576F1157F753292B741A3BA9CFA401159` / `DE6DE61142697728DB6E40B421B975AB53FF82CF6E361E7A250CBE7478DCD1B0`.

## Evidence package

`/root/p07_evidence` authored the 18-term producer evidence pack and bound source/Hans/Hant hashes. The root first observed preliminary generator outputs with terminology/adverse/CJKV/graph SHA-256 `1E3713A2247E7EEC9735392273A0D13975D85ABB0ACD8C40D9AB486FFB5A83A6`, `D2E9A86F069A8B4D4B022F670586CA6DFAE1FD8A26895A844135F9A673E57355`, `68EEC04FA427CCF499B610BBF721DD326340F9ACA8B766C9A6905280F070444A`, and `877542FA13BA34514E912DAB72B2D1520154FC8E85A29E2E01FDCEEA096D56B5`; the worker then completed a final deterministic rerun. Final SHA-256 values are `7A6A4716E0913F8822ABAEB3F9BF5DF8C0ADE28190F809C868D3D1C772E2F839`, `C24B31DD65F5FA1857A1B99A7688F227263B69FA775DD10AC3BCB80F1F366D0B`, `E10E9D090BFED48879D70EDBAEC1BB4A9BB01A31E5C2158C036D17DEAEB9D940`, and `C7DAAD65A6B3009B5D3EDBFDE7FA3335102592374219D5A1102F5339A896EA35`. The root mechanically imported the final CSVs as 18 rows with adjacent-schema headers and parsed the final graph as 90 nodes / 90 edges, unique node IDs, and zero missing `from`/`to` references.

## Documentation draft

`/root/p07_docs` drafted `TRANSLATION_NOTES.md` and `STATUS.md` before Hant/evidence completion, with initial SHA-256 values `32136FA677B772037AEEEB19410A184B8E5500E22C3E7B9068CD2D0C88A2684` and `84913912E993C92A199B960E92581220C87B08BD256DA1EC72252BC083E32D8F`. The root later appended exact Hant/evidence outcomes; final hashes are recorded in the checker handoff.
