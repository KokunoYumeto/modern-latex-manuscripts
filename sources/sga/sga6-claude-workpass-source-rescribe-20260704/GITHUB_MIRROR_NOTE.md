# GitHub Mirror Integrity Note

This directory is the rolling GitHub mirror of the SGA6 French source-rescribe
workpass. The current public frontier is ledger entry #679 / scan idx662;
scan idx663 is next.

`PACKAGE_SHA256.csv` is the internal manifest of the preserved Zenodo ZIP
`04_SGA6_TeX_SourceRescribe_Audit_NotCertified_idx662_20260717.zip`. It records
the byte surface used to build that archive. Git can normalize line endings in
text files, so those archive hashes are not asserted as Git-blob hashes.

`SHA256SUMS.txt` is generated from the staged Git blobs and is the integrity
manifest for this GitHub mirror. Binary source witnesses, render checks, and
the reader PDF are byte-identical across both surfaces.

Neither manifest is a mathematical certification. Material after idx662 is
inherited unchecked scaffold, the retained English idx532-537 tranche is not a
synchronized whole-volume translation, and this is not a critical edition.
