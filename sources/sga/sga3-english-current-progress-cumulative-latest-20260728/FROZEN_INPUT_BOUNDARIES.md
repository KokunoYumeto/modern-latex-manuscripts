# Frozen additive input boundaries

This cumulative integration copied only declared stable producer surfaces.
It did not read later mutable files into the reader merely because they
existed in an active working directory.

## Expose XVII

- Included authority scope: local pages 1-34 through Section 5.9.
- Next cursor: local page 35 / combined page 997 / printed page 602.
- Producer status SHA-256:
  `5B55676333F4D8A8A8B1870CE473AB8C385A96E4F2734CF6526B427BFE753E57`.
- Frozen standalone master SHA-256:
  `CF0C606C399EB076B89EABD7AF787188CA578187017BD4A71E2F016D2859DD97`.
- Frozen standalone reader SHA-256:
  `C0CF34D838C6D78980B8AF7865B3BC28FBB4199DC8C1AE533BD2C5AE26916015`.

The working master had already acquired a later Section 6 input by the time
of archive integration. Removing that one input reproduced the status-bound
master byte-for-byte; the later component was not admitted.

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
