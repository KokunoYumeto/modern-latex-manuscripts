# Publication readiness: Noether Paper 20 English R823 tranche

Status: `COMPONENT_READY / ZENODO_HOLD`

The standalone Paper 20 TeX/PDF component is source-synchronized, builds
cleanly, and has passed visual QA. It may be included in the next Noether
English source/standalone bundle.

It must not yet be presented as a replacement for the complete English
cumulative reader. The existing Zenodo English reader is RA10, while the
German authority is R823 and the remaining 42 papers have not all received a
current-delta disposition. Publishing this single paper as though it closed
the corpus-wide gap would be misleading.

## Required before the next Noether English Zenodo version

1. disposition every paper in the RA10-to-current German drift ledger;
2. promote all changed English paper TeX sources and rebuild the cumulative
   reader;
3. compile and visually inspect the cumulative PDF and every separately
   promoted standalone PDF;
4. produce a corpus-level hash manifest and Zenodo payload manifest;
5. retain an explicit working-draft caveat and identify the exact German
   source-control revision;
6. create the new version under concept DOI `10.5281/zenodo.20412587`, not a
   new concept DOI;
7. archive the returned record JSON and exact uploaded-file hashes.
