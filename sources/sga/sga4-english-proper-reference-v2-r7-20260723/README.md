# SGA 4 proper — cumulative English reader

This no-overwrite release candidate contains the cumulative English LaTeX and
PDF for SGA 4 proper, Exposés I–XIX including Exposé V bis. SGA 4½ is excluded.

The controlling French source is the frozen Orgogozo TeX snapshot at commit
`71766d9`; its acquired archive has SHA-256
`DA2D939D3BD66B03E7BEFF4353550F7A27982847AE4F798D0872F1DB5D64C7DC`.
The package asserts no new license grant. See `RIGHTS_AND_PROVENANCE.md`.

Primary objects:

- `reader/SGA4_English_Exposes_I_XIX_including_Vbis_reference_v2.pdf`:
  the 864-page cumulative reader;
- `source/SGA4_English_translation_workpass.tex`: the cumulative master;
- `source/SGA4_English_Exposes_I_XIX_including_Vbis_reference_v2_source.zip`:
  the complete 300-file build source and public controls;
- `qa/SGA4_English_Exposes_I_XIX_including_Vbis_reference_v2_QA_evidence.zip`:
  the complete graph, set-relation proof, source/build closure, and visual QA;
- `SOURCE_FILE_MANIFEST.csv`: the 300-row source identity manifest;
- `ZENODO_PAYLOAD_MANIFEST.csv` and `SHA256SUMS.csv`: the proposed upload set
  and its exact file identities.

The reference graph contains 8,701 source-visible candidates, 3,388 targets,
6,114 edges, and 8,701 exhaustive disposition rows. The candidate and residual
tables are bijective. Of the candidates, 5,998 own one edge and 2,703 are
closed positive nonedges; 116 disjoint supplemental source records own the
remaining edges, so `5,998 + 116 = 6,114`.

The superseded r2 working release and rejected r4, r5, and pre-freeze r6
candidates are not part of this package. Archive maintenance must update the
existing SGA archive concept, never mint a duplicate, and perform exact public
readback before publication is claimed.
