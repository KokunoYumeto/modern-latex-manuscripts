# EGA II — complete English reference reader

This package contains the complete source-aligned English EGA II reader:
Chapter II opening and summary, §§1–8, bibliography, notation and terminology
indexes, the chapter table of contents, and the terminal Errata/Addenda (List
1).  The 165-page PDF has stable named destinations and clickable internal
references throughout.

## Principal files

- `EGA2_English_complete_reference_reader.pdf` — the reader;
- `source/ega2.tex` plus its 13 active dependencies — editable English TeX;
- `controls/REFERENCE_TARGETS.csv` — 1,028 stable semantic targets;
- `controls/REFERENCE_EDGES.csv` — 2,078 resolved PDF link edges;
- `controls/REFERENCE_CANDIDATES.csv` — the 921 reviewed candidate universe;
- `controls/REFERENCE_APPLICATIONS.csv` and
  `controls/REFERENCE_RESIDUALS.csv` — the exact 264/657 candidate partition;
- `controls/build_complete_reference_reader.ps1` — isolated four-pass XeLaTeX
  build plus stable-destination overlay;
- `verify_package.py` — exact-set, source, ledger, PDF, and privacy verifier.

## Build

From PowerShell, with XeLaTeX and Python packages `pypdf` available:

```powershell
.\controls\build_complete_reference_reader.ps1 `
  -OutputDirectory C:\tmp\ega2_reference_build
```

The output directory must not already exist.  The script runs four XeLaTeX
passes, requires passes 3 and 4 to converge, rejects release-blocking log
diagnostics, then adds the stable aliases without editing page content streams.

Run the static package verifier with:

```powershell
python .\verify_package.py
```

## Scope and claim limits

The French authority, scans, and OCR are not included.  This is a complete
English working reader and reference-engineering successor, not a critical
edition, peer review, mathematical certification, accessibility certification,
or rights-clearance determination.  See `RIGHTS_AND_PROVENANCE.md`.
