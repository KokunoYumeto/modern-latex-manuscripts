# Accepted build log excerpt

Final command (path placeholder intentionally used):

```text
latexmk -xelatex -bibtex- -g
  -jobname=open-logic-hindi-working-reader-through-0009
  -interaction=nonstopmode -halt-on-error -file-line-error
  -outdir=<build-dir> open-logic-hindi-working-reader-through-0009.tex
```

Receipt:

```text
latexmk exit: 0
Output written: open-logic-hindi-working-reader-through-0009.pdf
Pages: 14
Bytes: 184823
PDF SHA-256: 80B48447897C49EFD28B9B15A6951EB1C78F2CEE7BFD8DB0C53938D71B4C7793
Log SHA-256: E58EC11F1CB8211134DDECCF8A2784F90AA4CB4F61067B41D5E5B68474F8CE00
Hard-error scan hits: 0
```

Retained non-fatal upstream warnings concerned repeated Hyperref options,
subfiles/document-class naming, and absent optional Git metadata. None was a
missing glyph, undefined reference, overflow, fatal error, or stopped build.

