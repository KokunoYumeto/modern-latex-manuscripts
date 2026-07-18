# Turkish probability/statistics build conflict

The canonical source package contains the native Turkish TeX tree at:

`bodies/tr/tex-source/kadirhanpolat_probability-statistics/source/probability-statistics-master/`

Its inherited status documents disagree:

- `CLAUDE.md` claims `main-ogrenci.pdf` at 310 pages and `main-egitmen.pdf` at 344 pages, both with zero errors.
- `tasarim_belgeleri/00_PROJE_OZETI.md` claims 168 and 192 pages, also with zero errors.
- the preserved `bolumler/compile_egitmen.txt` contains extensive unresolved-reference and unresolved-citation warnings and reports an older build state.
- neither claimed PDF is present in the packaged source tree.

Manager disposition: preserve the TeX as a valuable native Turkish source and terminology witness, but treat all inherited build/page claims as unverified. Before any derived use is represented as buildable, compile both entry points from a clean copy, capture tool versions and logs, verify references and bibliography, render every page, and record the resulting PDFs and hashes. This is not a translation-completion issue because the work is already authored in Turkish.
