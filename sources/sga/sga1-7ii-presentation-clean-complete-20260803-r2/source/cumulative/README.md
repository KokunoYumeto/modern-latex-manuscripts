# Reproducing the cumulative reader

The global reader is a deterministic PDF-level assembly of the nine clean
standalone readers.  This is necessary because the standalone TeX trees have
independent macro and package environments.  The assembly does not rasterize or
re-typeset pages.

Install Python and `pypdf`, then run `source/cumulative/build_prefixed_pdf.py`
with an output path followed by the triples below:

```text
SGA1  "SGA 1"   00a_SGA1_English_Reader.pdf
SGA2  "SGA 2"   00b_SGA2_English_Reader.pdf
SGA3  "SGA 3"   00c_SGA3_English_Reader.pdf
SGA4  "SGA 4"   00d_SGA4_English_Reader.pdf
SGA4H "SGA 4½"  00d5_SGA4half_English_Reader.pdf
SGA5  "SGA 5"   00e_SGA5_English_Reader.pdf
SGA6  "SGA 6"   00f_SGA6_English_Reader.pdf
SGA7I "SGA 7 I" 00i_SGA7I_English_Reader.pdf
SGA7II "SGA 7 II" 00j_SGA7II_English_Reader.pdf
```

The exact input hashes and page counts are in
`source/cumulative/INPUT_READERS.csv`.  A valid rebuild must reproduce the
content/geometry partition and destination/action routing recorded in the
enclosed build and validation JSON files.  The precise whole-file PDF hash may
depend on the installed `pypdf` version; page contents and graph semantics are
the controlling reproducibility conditions.

