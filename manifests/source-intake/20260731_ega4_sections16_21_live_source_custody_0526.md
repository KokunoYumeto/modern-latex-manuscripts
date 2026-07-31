# EGA IV Sections 16-21 live source custody at 05:26

At `2026-07-31T05:26:00+02:00`, archive maintenance copied the
current editable source closures from the two active EGA IV Part 4 lanes into:

`sources/ega/ega4-sections16-21-live-source-custody-20260731T0526/`

The public-safe snapshot contains 19 files / 2,917,563 bytes. Its 17-row
self-excluding `SHA256SUMS.csv` is 2,749 bytes with SHA-256
`8DE2589A977841BA505AD688C526D4454BA827F4A1FDE75FB3ECEAF5B00C8386`.
Together with the manifest's own identity and `CUSTODY_VALIDATION.json`
(2,195 bytes, SHA-256
`A313348A0E3E9E5BCCA88EF275114BD8407885E0E4B9924C10127C1D9E9D52D0`),
every file has an exact public identity. Validation reports
`PASS_GITHUB_LIVE_SOURCE_AND_FRESH_BUILD_CUSTODY`, `errors=[]`, zero source
copy mismatch, zero change during capture, and zero privacy/process hits.

## Conservative scope

- Sections 16-18: producer checkpoint `checkpoint_printed132_r34`, aligned
  from printed page 5 through page 132; conservative next page 133.
- Sections 19-21: producer checkpoint `build_p185_251_r13`, aligned from
  printed page 185 through page 251; conservative next page 252.

The six live source files were newer than one or both named producer
checkpoints. Their exact later bytes are preserved because they are valuable
work, and fresh builds prove coherent TeX closure. No alignment coverage beyond
the conservative checkpoint boundaries is promoted.

## Source and build identities

| File | Bytes | SHA-256 |
|---|---:|---|
| `ega4-16.tex` | 177,024 | `117AA3D848923C3FF849713BA124C5E106FA9A89EBF5557FA6055ACDC7631E2F` |
| `ega4-17.tex` | 194,286 | `5CFAAA5DF8AF305F49CD7475B67B97586F181854C5751C7454DECE865D994EC0` |
| `ega4-18.tex` | 323,041 | `425EB27404E40F0EA6F88FA9C06F2806F79AD3F34B461B28788B118A12901CC7` |
| `ega4-19.tex` | 175,857 | `803DD260ED0B988FC95084CE10203C05B1840F7B689919FE25E18C6704120496` |
| `ega4-20.tex` | 114,732 | `497B0302E808FF0D49D4CCBD1D03B61ACE3DC9A1B15FCB835752E9E7C6F478BC` |
| `ega4-21.tex` | 311,259 | `3E16523296BE71D59D61C56CC91F3C2D6871261E10F305964A3978875BDE3425` |
| Sections 16-18 fresh build | 889,360 | `F75E178F3EC3492C76F1E52DA7378A6E2861CA472F849C3B0A7F40E4F51C033F` |
| Sections 19-21 fresh build | 709,949 | `7ED437714B7D2AE367CC348955799F5619501332A62CC91726DD461DB171C281` |

Each copied closure built in three XeLaTeX passes with zero hard diagnostics.
The resulting PDFs have 132 and 103 pages. Their extracted text has zero
private-path, task-ID, model-name, or project-process hits; no AI or status
preface was added to the mathematical reader.

The NUMDAM authority PDF, source pixels, OCR bodies, raw logs, caches, and
build intermediates are excluded. High-detail source images are already
preserved separately on the established EGA Zenodo concept. This snapshot is
GitHub source survival, not a complete EGA IV reader, rights determination,
critical edition, peer review, accessibility certification, or Zenodo change.
