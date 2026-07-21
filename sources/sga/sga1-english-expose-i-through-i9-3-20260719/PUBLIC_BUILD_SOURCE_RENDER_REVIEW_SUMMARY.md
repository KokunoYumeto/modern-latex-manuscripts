# Public build/source/render review summary

- Exact sealed source driver: 18,781 bytes; SHA-256
  2D0C09EC8C415CA0DB6DDF355EB775A1BC492E7374F95FA43B6162F1E164A59D.
- Exact I.9.3 fragment: 2,272 bytes; SHA-256
  59F896BDD6FE54D0221D05891503626EEC4204A6A24B09E72833BD2F3EC46A34.
- Fresh public PDF: 548916 bytes; SHA-256 1DC6C5793BF15A898A0458907F9B6C00FB6965E0D609BA22486580D2DA75E7CA; 17 A4 pages.
- Passes 2 and 3 have zero selected diagnostics.
- AUX and PDF name tree contain exactly one proposition.1.9.3 destination.
- All 30 fonts are embedded, subset, and Unicode-mapped.
- Dual 17-page renders are byte-identical to each other and to the reviewed
  local render; digest 54976F68334AB14C9EC3C9590B14FB807644A28C6CC5EADF5B7CC16CDF3FEBD7.
- The rejected wrong-working-directory local r1 remains preserved and
  unclosed. The fresh public build does not reuse it.