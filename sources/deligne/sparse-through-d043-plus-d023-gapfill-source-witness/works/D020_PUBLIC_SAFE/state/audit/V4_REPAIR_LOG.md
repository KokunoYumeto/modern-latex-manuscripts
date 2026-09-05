# D020 V4 repair log

STATUS: REPAIRED_NOT_YET_COLD_AUDITED.

V3 remains immutable and adverse under `audit_cold/S06_math_v3_01`; its finding A10 proves that physical page 26 had eight source/English objects while the apparatus declared seven dispositions. V4 changes only `apparatus.ndjson` page 26 from `objects_disposed: 7` to `objects_disposed: 8` and updates that one apparatus canonical hash in `coverage.tsv`. Scholarly text, source/English records, authority, images, TeX, HTML and PDFs are unchanged.

Old apparatus canonical SHA-256: `1D448DB3E5E1F338FF5EA0624AA8789C9BBFB3AF9CD25F906D95F8DB9BB81028`. New apparatus canonical SHA-256: `FD7D23C89F329E689870840E72D7E14F66BE04F4E6AA42EBE0127172D1B9664A`.

Next action: validate V4, confirm byte identity of all unchanged presentation products, freeze a new immutable subject, and run a fresh nonpatching whole-paper cold audit.
