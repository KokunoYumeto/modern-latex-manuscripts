# Reproducible build

Requirements used for the accepted build:

- XeTeX / XeLaTeX (MiKTeX-XeTeX 4.18 was used)
- `latexmk` 4.88
- the LaTeX packages required by the pinned Open Logic source
- no separately installed Devanagari font is required; the exact OFL font is
  bundled in the overlay

Obtain and freeze the upstream source:

```powershell
git clone https://github.com/OpenLogicProject/OpenLogic.git OpenLogic
Set-Location OpenLogic
git checkout --detach 9620cc73f9c8e0ad003c514a5d3748f29611c4c0
```

Copy the *contents* of this package's `overlay` directory into the root of that
checkout, retaining the `locale/hi/...` paths. Then build from the directory
containing the cumulative wrapper:

```powershell
Set-Location locale/hi/content/sets-functions-relations/sets
latexmk -xelatex -bibtex- -g `
  -jobname=open-logic-hindi-working-reader-through-0009 `
  -interaction=nonstopmode -halt-on-error -file-line-error `
  -outdir=build open-logic-hindi-working-reader-through-0009.tex
```

The accepted PDF has 14 pages, 184,823 bytes, and SHA-256
`80B48447897C49EFD28B9B15A6951EB1C78F2CEE7BFD8DB0C53938D71B4C7793`.
An independently reproduced build may carry a different byte hash because TeX
can embed timestamps or environment metadata; it must still compile without a
hard error and pass the text, font, and page checks described in
`qa/QA_REPORT.md`.

