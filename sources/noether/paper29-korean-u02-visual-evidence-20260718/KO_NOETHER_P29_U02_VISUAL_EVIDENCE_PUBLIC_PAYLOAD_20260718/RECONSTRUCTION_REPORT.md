# U02 Korean pre-review render reconstruction

The historical pre-independent-review Korean TeX was not preserved as a separate file, but its exact three-change successor patch survived in the saved production session. Reversing those three changes in an isolated copy of the final TeX produced a 5,942-byte source with SHA-256 `757942045B900ED62288C9B94986D4156114887A6C4A6E9C79FF79F57CBAD26D`, exactly matching the hash and byte count recorded before supersession.

The recovered source was compiled twice with XeLaTeX under the original job name and rendered with Poppler at 180 DPI. The reconstructed one-page PNG is 561,221 bytes with SHA-256 `3745EE1BFA0551F4BE6F2681A966872AD0C65A2CD87057F3AB80915CB4DA3935`, exactly matching the recorded historical render. This is a byte-for-byte recovery of the TeX and pixel-identical recovery of the rendered PNG.

The regenerated PDF is 66,373 bytes with SHA-256 `09A06792AFD75AA5E8AE668E0038EC956156F03FD744A7C60402FA462E3F6822`. It does not match the recorded unavailable historical PDF SHA-256 `D396477CDA351685D4885692CAF518E7A99DCCCADF71B7F9CE321D69CFB9481D`, as build metadata differs. The archive therefore calls the TeX and PNG exact recoveries, but calls the PDF a regenerated reconstruction rather than an original recovered binary.

The reconstruction log is 15,518 bytes with SHA-256 `0F5DFA897D2869E0E8EC8B17D534885DA9FB95A24EC53C88C5FA19ABBBD11E53`. It contains zero LaTeX errors, undefined-control-sequence reports, missing-character reports, fatal errors, overfull boxes, or underfull boxes. Original-resolution inspection found no visual defect. The superseded prose and proof-premise choices remain editorially rejected even though the historical pixels were reproduced exactly.

The earlier stranded-footnote render is a different lost state. It was overwritten before hashing, no patch boundary uniquely reconstructs it, and no digest is asserted for it.
