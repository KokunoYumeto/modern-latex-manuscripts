# Independent build validation - SGA2-VIII-P11S

Result: PASS for this bounded internal unit.

- Fresh pdfTeX pass 1 exit: 0.
- Fresh pdfTeX pass 2 exit: 0.
- Final-pass diagnostics: 0 TeX errors, warnings, unresolved references,
  overfull boxes, underfull boxes, missing characters, or fatal errors.
- TeX: 2,253 bytes; SHA-256
  `C22C4815DF0CC9C54CBB1EE939982AE381CCE8F6F652962E1921972F5C6A0A56`.
- PDF: 238,642 bytes; one unencrypted A4 page; SHA-256
  `B8E3E888D3EA138B949929CE555DA76B7F6720EB30D2C45B6897440FFD8DA8B8`.
- Independent pass-1 local-only log SHA-256:
  `56CDF85466EAB445AE0AD0285F254E625C94C5C02DB583D2870319488A544849`.
- Independent pass-2 local-only log SHA-256:
  `56CDF85466EAB445AE0AD0285F254E625C94C5C02DB583D2870319488A544849`.
- Font report: 15/15 rows embedded, subsetted, and Unicode mapped; SHA-256
  `5BE3754B311FE5297F292D19D07AF8CA2B5BB3FC10823DACE6711AD73B0EB6FB`.
- PDF information receipt SHA-256:
  `B0F8DD26662822F5BFE923EEA0F8ADDDC83EB01D2D1A665E4C4397A9D2538ABA`.
- Independent target text extraction: 1,538 bytes; zero unexpected control
  characters; SHA-256
  `A122E1F9273641614952AF6DFFB1054D55BD07F906E56432855AF9BAE04661CB`.

The first independent extraction contained two U+0001 controls emitted after
the compact displays. Replacing only the extensible outer parentheses with
ordinary parentheses removed them without changing either visible formula or
its mathematics. The final extraction contains both complete displays and the
complete Section 1 footnote.

The PDF is an internal bounded reader, not a cumulative Expose VIII edition or
publication payload. It is untagged and has no XMP metadata stream; those are
release-level caveats rather than failures of this internal seal.
