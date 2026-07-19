# Prior-audit failure record: P02 pp. 28-34

The older `N_SYM_RA13_P02_p28_34_20260611` packet described this band as symbol-level audited. That claim was not sufficient for closure. Direct current-head review found defects it had missed, including the p. 28 continuation schema, the lost prime in `C'_{pr\varrho}`, and the p. 33 exponent error `a_\eta^4` for source `a_\eta^3`.

The failure mechanism was methodological: a package-level or symbol-locator pass was treated as if it implied complete page coverage. It did not establish that every schema row, continuation mark, note identity, exponent, prime, centered product separator, and source emphasis had been compared against the current TeX.

Future closure requires one controlling row per printed page, explicit source and current-head identities, direct complete-page inspection, targeted enlargement for dense loci, exact fix/no-fix disposition, compilation, and changed-page render review. Earlier audit labels remain useful provenance, but they do not override this page-level evidence.
