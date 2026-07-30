# EGA I complete English reference reader

This package contains the complete source-aligned English EGA I reader, its
editable LaTeX, and the machine-readable reference graph used by the PDF.
Coverage runs through Sections 1-10.15, the bibliography, the index of
notation, and the terminological index; the semantic cursor is EOF.

The main reader is `EGA1_English_complete_reference_reader.pdf` (113 letter
pages). Every delivered PDF action uses a stable local target. References to
EGA 0, EGA II, and external works remain visible but are deliberately not
misrouted to local EGA I content. This reader-clean R2 removes two redundant
contents registrations present in the held R1 package.

Rebuild from a fresh output directory with:

```powershell
./controls/build_complete_reference_reader.ps1 -OutputDirectory ./fresh_build
```

Verify the exact package set with:

```powershell
python ./verify_package.py
```

The French NUMDAM authority and scan witnesses are not redistributed. See
`RIGHTS_AND_PROVENANCE.md` and `PUBLICATION_READINESS.md` for the claim and
rights boundaries.
