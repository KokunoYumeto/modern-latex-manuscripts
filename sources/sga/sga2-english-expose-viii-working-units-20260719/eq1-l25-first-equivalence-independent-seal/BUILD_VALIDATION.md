# Build validation

The bounded target builds with two stabilized `pdflatex` passes, zero errors,
and no LaTeX warning, package-warning, overfull-box, or underfull-box hits. The
result is one A4 page, 309,360 bytes.

- TeX SHA-256: `ECAAC213067D97BE280748C63BB615AEAB343A9D6337D1AE90934105C3B22E0E`;
- PDF SHA-256: `382660FC2890FA311B7DB0C7373440EAD1EBE23BC2FA9BDC98875BA845A9728E`;
- each raw stabilized log SHA-256:
  `F99F93C320313CA71AD649B17DC28BF9CD61F1C618677224A697518C93062FFD`;
- each public sanitized log SHA-256:
  `DBE6119393ACB6AD0D04C598BB2760EDD366983A67913D42AF762F6BFB5D4731`;
- PDF metadata report SHA-256:
  `B584961E28EA552164C8284CA3726ED3CC200057E723916B9B1BBE9FB591C740`;
- PDF font report SHA-256:
  `97DAD021A6C111B4F3B7920C308925F47ECE2CB18E142A8107B19409F301576A`;
- extracted target text SHA-256:
  `2F8367B438F9070B6BFE394E82E5CF3D825163C266F8C540DC9BC6C2DC788CFA`.

All 18 reported font rows are embedded, subset, and Unicode-mapped. The final
3,338-byte text extraction contains zero forbidden non-layout control bytes;
its single form-feed byte is the ordinary one-page extraction delimiter.

Raw build logs expose the local TeX installation and remain `LOCAL_ONLY`.
The proposed public logs replace the user-home prefix even when TeX wrapped it
across lines. Raw and whitespace/newline-elided scans of the public logs find
zero user-name, user-home-prefix, or internal source-tree path hits.

Independent review found that the first build had rendered source editor note
(6) as automatic footnote 1. The target now uses the established Exposé VIII
marked-note macro; the callout and footnote both visibly carry `(6)`, with no
automatic `1`. The hashes above are the post-repair identities.

A fresh independent two-pass build from the live TeX also exits zero. Its
309,360-byte one-page PDF has SHA-256
`77447AC2B1970E06FB32598D90DEE77071F76FBF4883E890055F5F78EA3C2FDF`.
The independent pass-1 and pass-2 log hashes are respectively
`28AE8FFC6E006DDA9C6B6FAACD62D6845FF81F8B438A29494C64A40D79838591`
and `1EADCD628B09619EB11A6CFB6FAFD951A5477E5E82A31E5A4D28910673078669`;
pass 1 has only the normal rerun request and stabilized pass 2 has zero real
diagnostics. The independent default extraction is byte-identical to the same
extraction from the frozen target, and the 300-dpi renders are byte-identical.
The two PDF files differ only in volatile timestamps and the derived trailer ID.
