# EGA IV complete English reference reader

This package contains a complete source-aligned English reader for EGA IV,
its 59-file editable LaTeX closure, and the complete machine-readable
reference graph used by the PDF. Coverage runs through Sections 1–21, the
bibliography, notation and terminology indexes, contents, and errata/addenda;
the semantic cursor is EOF.

The main reader is `EGA4_English_complete_reference_reader.pdf` (4,252,287
bytes, 651 A4 pages, SHA-256 `6087FD9475DBDE908EA2025326BC7A49AF33583C7047A7D9332648D2B6387C7A`). It contains 7,374 resolved
internal GoTo actions and no raster images. References to EGA 0/I/II/III and
external works remain visible but are deliberately not misrouted to local
EGA-IV content.

Rebuild from a fresh output directory with:

```powershell
./controls/build_complete_reference_reader.ps1 -OutputDirectory ./fresh_build
```

Verify the exact package set with:

```powershell
python ./verify_package.py
```

The four French NUMDAM authority PDFs are not redistributed. See
`RIGHTS_AND_PROVENANCE.md` and `PUBLICATION_READINESS.md` for the claim and
rights boundaries.
