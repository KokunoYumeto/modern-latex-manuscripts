# Noether R823 cumulative English custody

Date: 2026-07-22

## Archive classification

Archive maintenance accepted the privacy-clean 52-file cumulative English
payload for Noether numbered Papers 1-43 through R823 line 20967. The appended
German lecture beginning at line 20968 is excluded. This is an inherited
English working corpus, not a new full source audit, native review, community
certification, rights determination, or critical edition.

GitHub path:
`sources/noether/noether-r823-cumulative-english-43-papers-20260722/`

## Exact payload

- 52 files / 5,539,858 bytes.
- Producer aggregate SHA-256:
  `3AE6E9C024D4666D5A041D232DBF5F2CAEE2D308EACE8E59319B52D79ECC65AE`.
- `SHA256SUMS.csv`: 51 self-excluding rows / 8,168 bytes / SHA-256
  `315F115D6E140F8C7B830815EFBF3F23D9E5F72D7AA4D27E26C16D015A6E8B62`.
- Manifest replay: 51/51 exact, with the manifest's own identity checked
  separately.
- Recursive TeX closure: one master plus all 48 fragment files, with no
  missing or extra fragment dependency.

Primary targets:

- TeX: 1,837,182 bytes / SHA-256
  `CF3EE17888FDD484F4FCB943FA395A3398290F5C753C9A3E7DBE983B655828B2`.
- PDF: 2,891,622 bytes / 407 A4 pages / SHA-256
  `F66EEBD3374A58D0456FB35F3D3C85CE52B77E6DD74A28EDC557BB81A882E072`.

## Archive validation

Two isolated pdfLaTeX passes completed with exit code 0. The fresh 407-page
reader differs from the frozen PDF only in generated identity metadata and
extracts byte-identical layout text. All 38 font rows are embedded, subset,
and Unicode-mapped. Archive maintenance directly inspected pages 1, 50, 100,
150, 200, 250, 300, 350, 387, and 404-407; no clipping, overlap, missing page,
or terminal-boundary defect was found. The PDF is A4, unencrypted, untagged,
and has no XMP stream. The editable TeX is the durable accessible surface.

The package contains no scan, build log, local continuation cursor, or private
absolute path. The German lecture at line 20968 is not imported by the master
or any recursive fragment.

## Remote routing

Immediately before GitHub admission, the official Zenodo API still resolved
concept `10.5281/zenodo.20412587` to version
`10.5281/zenodo.21434690`. Any archive update must be one successor on that
existing concept and must wait for an exact public GitHub clone readback.
No duplicate concept or competing draft is authorized.
