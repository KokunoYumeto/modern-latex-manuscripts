# Riemann GitHub Coverage Map

Observed 2026-08-06. This page records the Bernhard Riemann material whose
bytes are actually present in GitHub. It separates two direct working readers,
their editable source layers, and historical controls whose recorded identities
do not all match the current files.

These are machine-assisted working transcriptions, not critical editions,
mathematical certification, or proof of source completeness. The reader PDFs
and TeX files are independent custody surfaces unless an exact build relation is
explicitly proved below.

## Start Here

| Surface | Direct reader | Editable source | Exact represented state |
|---|---|---|---|
| *Gesammelte mathematische Werke* broader draft | [511-page reader](<../reader-pdfs/riemann/10 Reader PDF - Riemann - Gesammelte Werke Complete Draft.pdf>) | [current flattened TeX](<../sources/riemann/90 Artifacts - Riemann - Gesammelte Werke Complete Draft/riemann_gesammelte_werke_complete_transcription/canonical_tex/tex__riemann_gesammelte_werke_complete_transcription.tex>) | The current reader is 2,983,207 bytes, SHA-256 `F665607AAC5F396361C70DD69EF4C5A5737014B40393D7E3F9795271DDECD040`; the current TeX is 1,258,237 bytes, SHA-256 `BE6F672B5D9CDB33DBDCEE3199FA1D24221390844E61F4F13BFC15DBCAECE19F`. Neither matches the identities in the retained repair manifest, so they are not presented as a manifest-bound PDF/TeX pair. |
| Selected papers | [228-page reader](<../reader-pdfs/riemann/10 Reader PDF - Riemann - Selected Papers.pdf>) | [current flattened TeX](<../sources/riemann/90 Artifacts - Riemann - Selected Papers/riemann_papers/canonical_tex/tex__riemann_papers.tex>) | The reader is 1,389,110 bytes, SHA-256 `EC0D6498521A363BB6170AD2FA566CF6554B586052EFC527DEE76CE60DDFCB21`, and matches its retained PDF control. The two tracked canonical-TeX copies are byte-identical at 801,346 bytes, SHA-256 `0945992152B4D53A64D28D978C950D3A9E4B0A0D0D2E687A69F14B5635098FEA`, but do not match the TeX identity recorded by that control. |

## Broader *Gesammelte Werke* Draft

The [repair manifest](<../sources/riemann/90 Artifacts - Riemann - Gesammelte Werke Complete Draft/riemann_gesammelte_werke_complete_transcription/metadata/manifest.json>)
records a 512-page repaired display PDF at 2,929,141 bytes, SHA-256
`DEDDD2BC79109C789246370F7249D8BBAE678F5DE3601CCBF68BB728F7B010E8`,
and a canonical TeX SHA-256 of
`7BB4786EF01F30A23DA71E9619C142F9923A7B87FC8DCE359BF4A5545910DC73`.
Neither identity is present in the current 32-file Riemann selection.

Git history explains part of the divergence: commit
`41eccb69e1c0ee24dbbecf80d66dd8095630d4e3` replaced the direct reader in a
“Trim blank pages from generated readers” change, from 2,929,141 to 2,983,207
bytes. The current reader has 511 pages. The source and repair controls did not
change in that commit, so the old [33-page sample QC](<../sources/riemann/90 Artifacts - Riemann - Gesammelte Werke Complete Draft/riemann_gesammelte_werke_complete_transcription/qc/riemann_trimmed_strict_display_pdf_quality.csv>)
remains historical evidence for the manifest-bound 512-page object, not QA for
the current 511-page reader.

The current TeX contains fifteen chapter markers, including flattened source
segments and later cover material. Maintenance did not compile it and does not
claim that it reproduces the current reader. Recover or regenerate an exact
post-trim PDF/TeX/control package before treating this as a synchronized
complete edition.

## Selected Papers

The direct 228-page reader exactly matches the PDF bytes, size, and hash in the
[selected-papers control](<../sources/riemann/90 Artifacts - Riemann - Selected Papers/riemann_papers/metadata/manifest_final.json>).
A current read-only PDF structure pass enumerated all 228 pages but warned of a
broken cross-reference subsection. The older control records successful PDF
and text checks; neither fact is a source-level mathematical audit.

The control records a canonical TeX at 815,515 bytes, SHA-256
`37DFA1E2F1E1527F5C113CC5D61ABCBCD0DE51C490014B4C49D601D17AF851ED`.
That identity is absent. The current
[canonical copy](<../sources/riemann/90 Artifacts - Riemann - Selected Papers/riemann_papers/canonical_tex/tex__riemann_papers.tex>)
and [normalized copy](<../sources/riemann/90 Artifacts - Riemann - Selected Papers/riemann_papers/normalized_corpus/canonical/riemann_papers.tex>)
are byte-identical to each other but not to the control. The current flattened
TeX contains nine source-segment chapters for page-labelled chunks 001–450 and
ends with an incomplete `Ausf\` fragment immediately before
`\end{document}`.

The normalized control lists only six PDF inputs: chunks 051–100, 101–150,
151–200, 201–250, 301–350, and 351–400. Those chunk PDFs are not tracked here.
Do not infer that the 228-page reader covers the same nine segments as the
current TeX, or that the TeX is its exact build source.

## Preserved Prior-Bundle Layer

The [prior-bundle subtree](<../sources/riemann/90 Artifacts - Riemann - Selected Papers/riemann_papers/source_artifacts/prior_bundle/>)
contains 16 files / 1,312,979 bytes: nine TeX chunks, five extracted/raw text
files, one manifest, and one README. It contains no PDF chunks or scans.

Its manifest records a historical 73-file / 46,291,275-byte copy operation,
while the later selected-papers metadata records 75 files / 46,293,309 bytes.
Those larger historical sets and the named prior package are not present in
the current GitHub tree. Preserve both claims as provenance, but do not treat
either as current custody proof.

## Exact Content Inventory

The audited GitHub-native selection contains 32 files / 8,567,055 bytes.
Canonical tree SHA-256:
`470E1FBE651A1D74CF0863B48606002F5C1DFC983B638DA6808CB9DCCD20E97D`.

It includes all 30 files under `sources/riemann` and both direct readers. See
[`20260806_riemann_map.json`](../manifests/github-custody/20260806_riemann_map.json)
for selection-level counts, hashes, current-versus-recorded identities, and
the exact caveat state.

## Continue Without Duplicating Work

1. Preserve the current readers, TeX files, controls, and stale identities as distinct history; do not silently rewrite them into agreement.
2. Recover or produce an exact post-trim *Gesammelte Werke* source/control package before claiming a synchronized 511-page edition.
3. Repair and source-check the selected-papers TeX ending in its producer lane, and bind any corrected TeX to the exact reader it builds.
4. Recover the missing selected-papers chunk PDFs/scans before assigning duplicate transcription or asserting source closure.
5. Verify citation-critical mathematics against an authoritative printed source; the retained structural and sampled-display checks are not that verification.
