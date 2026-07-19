# Review freeze

Frozen source boundary: corrected French lines 2828--2854 inclusive. Printed
pages are 94--95; physical source-PDF page is 83; recomposed running page is
75; printed marker 95 occurs at line 2847. Blank line 2855 is excluded and
French line 2856 is the continuation cursor.

Frozen repaired target identity:

- TeX: 3,329 bytes; SHA-256
  C3EE7A146335E9C685D5B0E1AB0264580E6BE61EDAC1A085065625CEE55811EB;
- PDF: 237,675 bytes; one A4 page; SHA-256
  74E7182A077EF8B8BE3B374BA9A02740818FED947665E40442E43D035B5A9543;
- extracted text: 3,152 bytes; SHA-256
  198C19CC484BFF826015E3182C6A7C45B6B4EEA39554C10389AED2D81C42525D;
- 300-dpi render: 413,329 bytes; SHA-256
  65C14CCD2B73E4021496A6B1256AC28893A14C86F1DDFF6DD83FE10377E2EEF9.

The first target identity is not frozen: it emitted four U+0001 extraction
bytes. Its documented source-matching delimiter repair is closed in the CSV
and JSONL revision history. Independent recheck of the repaired identity
passes with no further repair. Independent PDF SHA-256 is
CBABECF596CC17B2C6522A48BF72BAC5E5435059124F695E8573685026E7BE87;
its difference is timestamp-only and its extraction and render are
byte-identical to the frozen target.

Final substantive machine evidence is 58 CSV rows and 25 JSONL records / 21
stable IDs. Machine-validation SHA-256 is
A7505521779E92146598DA6F67374FDD9629BEF004AAE64C8B25AAB096C06236.
Any later target TeX, target PDF, substantive ledger, source boundary, or
review-state change invalidates this freeze and requires fresh build,
extraction, render, machine, privacy, and independent review.
