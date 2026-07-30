# SGA 1 — complete English reader with stable references

This package is the complete cumulative English SGA 1 reader and its editable
LaTeX source.  The mathematical text covers the whole translated volume,
including all published exposés, appendices, bibliographies, and the notation
index.  The delivered PDF has 262 pages.

The reference-v2 pass adds stable semantic destination names and closes the
complete delivered internal-link graph:

- 933 stable targets;
- 1,600 resolved internal GoTo edges;
- 31 newly reviewed source-visible internal links;
- 189 reviewed positive residuals for locators that must not become internal
  links;
- 0 broken, external, launch, URI, or active PDF actions.

The main files are:

- `SGA1_English_source_sync_workpass.tex` — cumulative editable master;
- `drafts/` — the 138 included editable components;
- `SGA1_English_complete_reference_reader.pdf` — final cumulative reader;
- `controls/REFERENCE_TARGETS.csv`, `REFERENCE_EDGES.csv`,
  `REFERENCE_CANDIDATES.csv`, `REFERENCE_APPLICATIONS.csv`, and
  `REFERENCE_RESIDUALS.csv` — the complete machine graph and candidate
  partition;
- `controls/build_complete_reference_reader.ps1` — four-pass build plus stable
  alias application;
- `verify_package.py` — read-only package verifier.

Run a clean build from PowerShell with:

```powershell
.\controls\build_complete_reference_reader.ps1 -OutputDirectory .\rebuild
```

PDF container bytes may differ between runs because TeX/PDF writers emit
run-specific identifiers.  The checked reproducibility contract is exact
decoded page content, extracted text, link targets and rectangles, named
destination set, and destination coordinates.

See `STATUS.md`, `RIGHTS_AND_PROVENANCE.md`, and
`PUBLICATION_READINESS.md` before reuse or public distribution.
