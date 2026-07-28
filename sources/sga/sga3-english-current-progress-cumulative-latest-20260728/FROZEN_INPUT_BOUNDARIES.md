# Frozen additive input boundaries

This cumulative integration copied only declared stable producer surfaces.
It did not read later mutable files into the reader merely because they
existed in an active working directory.

## Expose XVII

- Included authority scope: complete local pages 1-49 through Appendix III.
- Local page 50 / combined page 1012 is blank; Expose XVIII is excluded from
  the XVII source tree.
- Producer status SHA-256:
  `50D0DB2574DC0A4C25FABA40243927A367758FC02AD1101AF663B86FBBA8D81B`.
- Producer standalone master SHA-256:
  `6167501EAD3A9E447BE7CE0B3C4075B232969ADC1D81EDB269AAEE4B761A20A8`.
- Producer standalone reader SHA-256:
  `85448B0830DE96823C5C22B9C82B415DB4323EB8A761115EC160E4678B34210D`.
- Integration-corrected standalone reader SHA-256:
  `C055C608BBBA962BD8CF7E2B4FBFD1B1C6C2795F5B6BD902E0AAF7C0BC9CEC5E`.

The producer files contained three U+2019 apostrophes in editor-note text
that the selected T1 Latin Modern font omitted. The cumulative integration
changed only those three characters to ASCII apostrophes. The original two
source files and producer PDF remain preserved under
`predecessor/expose-xvii-complete-producer-original/`.

## Expose XX

- Included authority scope: complete local pages 1-35.
- Producer status SHA-256:
  `D877FCA304E80DCC10BB67C23A61AD70A0325EAF6F6843F3E2E2D6FC3C7B211D`.
- Master SHA-256:
  `9DF5337BDDADAC34B59626159D543660FAE6AA9F84A85F2FAB2516EBB4535D6C`.
- Standalone reader SHA-256:
  `D7B45AE2106E5913043C9A2073312127BC9D2D8925992522F319519CBE28785D`.

## Expose XXI

- Included authority scope: local pages 1-5 through Application 2.1.2.
- Next cursor: Definition 2.1.3 on local page 6 / combined page 1100.
- Producer status SHA-256:
  `5DE1E846420A18685D37D1AF6ADF8C174C88EBFB5C1C7435A0382055A17980E3`.
- Status-bound master SHA-256:
  `06372782FF4C9616A73A439A0F818F1FF6220045F5CB3367C26C4B022F756022`.

Only components 00 and 01 were admitted. Components written after the status
boundary were excluded. The packaged standalone PDF is a fresh three-pass
rebuild from this exact frozen closure; it is not a claim about later active
XXI work.

## Expose XXII

The immediately preceding cumulative snapshot's frozen local-pages-1-10
body was retained byte-for-byte. A producer working tree had advanced beyond
its status-bound source, so no later XXII bytes were admitted in this release.
