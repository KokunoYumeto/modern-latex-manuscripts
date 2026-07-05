# Noether Slavic Source-Canon Sorbian Catalog/Body-Route Recheck - 2026-07-04

Scope: source-canon-first Sorbian recheck for the Lower and Upper Sorbian mathematics terminology witness routes. This pass caches BVS/eOPAC/SorBib/soblex source-list pages and records exact official WITAJ/Domowina/Sorbian Institute catalog snippets.

Boundary: catalog/source-list/source-package evidence only. The actual mathematics terminology booklet bodies remain uninspected here. No native review, canonical approval, accepted correction, license clearance, source promotion, or translation completion is claimed.

## Summary

- Evidence rows: 9
- Compact snippet bundle: C:\Users\memo_\Documents\Codex\2026-07-04\noether-slavic-canonical-baseline\outputs\source_canon_witness_cache_20260704\hsb_dsb_math_terminology_catalog_snippets_20260705.csv
- Compact snippet SHA256: B2D952EEBD7453F8365728E4ADC72A33E1E680F11F92A6986D4F8DE11E6CF212
- Open blocker effect: Sorbian Lower and Upper blockers are sharpened, not closed.
- Rebuild trigger: none.

| language | row_id | body_status | local_sha256 | blocker_effect |
|---|---|---|---|---|
| Sorbian Lower | dsb_witaj_catalog_math_terminology_2016 | catalog_listing_only_not_booklet_body | 98881D3DB030E842C434B45D05D1C67F9BC7957154256C2F2C7656FBFA45B823 | pins official WITAJ 2016 Lower Sorbian math terminology listing, compilers, 260 pages, and textbook basis; does not inspect booklet entries |
| Sorbian Lower | dsb_bvs_eopac_math_terminology_item_records | catalog_item_only_not_booklet_body | 088A87FB1E3428B921A7CA88E09A99140A1B6EBFCBFA4E5DE5DD366B27BD0F39 ; 39CC34373E2216F7711B44A988DA0CF970A18F89075C37B3CC27690C1572A0A3 ; 80D624D7D8B3E7988AD0308DD6A18B7B097B4AC4C4A6B6FFBE1A6C293125083B | adds BVS/eOPAC title/item routes and shelf marker Ter F 22 for Lower Sorbian copies; does not expose booklet body |
| Sorbian Lower | dsb_spellchecker_math_terminology_route | lexicon_source_package_route_not_booklet_body | 20E1628FD66B1BC8AD5C5459277F2F14F0978A5E1E2D959767CC9B9A18BFCC25 | confirms public spellchecker route incorporated WITAJ 2016 mathematics terminology; lexicon package remains findability/body evidence only |
| Sorbian Upper | hsb_witaj_catalog_magerowa_2008 | catalog_listing_only_not_booklet_body | 5C8F75D6594839C3AAAAF9739293AEB1B6CEA7DC8A2861BC1D61995E7701D4DD | pins official WITAJ Magerowa 2008 listing, 106 pages, ISBN 978-3-7420-1359-0; does not inspect booklet entries |
| Sorbian Upper | hsb_domowina_catalog_magerowa_2008 | catalog_listing_only_not_booklet_body | 9DE13ADA16FB58D66A281372050269F9F03EDBF997AA2FDD5145F07A966D3E47 | adds Domowina literature-list corroboration for Magerowa 2008, 106 pages, ISBN; does not expose booklet body |
| Sorbian Upper | hsb_sorbian_institute_corpus_source_kuskec_1996 | corpus_source_list_only_not_booklet_body | 45497BEC619C14D04C8014E7E3C4EEA0046BFAD2DEAE17F8482A28312F531EB9 | pins Kuškec 1996 source-list identity in Sorbian Institute corpus sources; corpus/booklet body remains not inspected here |
| Sorbian Upper | hsb_soblex_about_magerowa_2008_source_list | source_list_only_not_booklet_body | A695117896049927A7537AF881DD876F1FB555EAF4BA081FDC84E17CBE368ED9 | adds soblex source-list corroboration for Magerowa/RCW 2008; not a mathematical publication body |
| Sorbian Upper | hsb_bvs_sorbib_math_terminology_item_records | catalog_item_only_not_booklet_body | 088A87FB1E3428B921A7CA88E09A99140A1B6EBFCBFA4E5DE5DD366B27BD0F39 ; 1832B814505149E43B59B784F97BC3757C7DFC1833886C0F902DE0EC6BEFE43D ; 2064C5EDEDF6433BB495C27090121C0685C7152C963245BD9F5BA07A6FF7C91B ; 00ED560157D4F8098101502B13967CE4EEDAC12E817E798D02179BE424633FB9 ; 9C88AB0AE5843C18B32A1B455A726F9E6B23A9F706DD47CC8070161FC0631CBA | adds BVS/SorBib item routes for Kuškec 1996 and Magerowa 2008; does not expose booklet body |
| Sorbian Upper | hsb_soblexx_negative_math_source_list_probe | negative_probe_no_math_source_list_hit | 96B92F62754B535F7C2F2C49DBA9867F54BF2EBB1B77AB417A8FF79F448AA23A | kept as a negative route check so stale readers do not assume soblexx provides the missing math booklet body |

## Decisions

- Lower Sorbian: official WITAJ catalog and BVS/eOPAC records identify the 2016 `Terminologija za pśedmjat matematika` route and shelf/copy records, and the Sorbian Institute Hunspell page links the spellchecker data to WITAJ 2016 mathematics terminology. This is still not the booklet body.
- Upper Sorbian: WITAJ/Domowina/BVS/SorBib/Sorbian Institute/soblex records identify Kuškec 1996 and Magerowa 2008 mathematics terminology routes, with Magerowa 2008 page count/ISBN and Kuškec 1996 page count. This is still not the booklet body.
- `soblexx.de` is retained as a negative route probe because it does not expose the missing math terminology body in this pass.

## Remaining Trigger

A rebuild or terminology mutation is justified only if the actual booklet/corpus body is acquired, a qualified Sorbian review return lands, hashes drift materially, or a concrete accepted source defect appears.
