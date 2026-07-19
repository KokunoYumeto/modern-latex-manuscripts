# Public-freeze revision history - SGA 1 Exposé I §I.8

The first public-freeze attempt, r1, stopped before manifests, exact-set
verification, or publication because a command-wrapper path prevented the
PDF metadata gate from executing. The compiler output itself was not used to
declare success.

- Preserved rejected r1 staging surface: 58 files / 1490687 bytes.
- Rejected r1 inventory digest: `AA035D6CC3D2D0029B9AEDF387C243B731C9E436719B1D58F4486420C18B506F`.
- Preserved private r1 build surface: 6 files /
  123197 bytes.
- Private r1 inventory digest: `DAB804FF54F7EC8B5EAFA915E0A6E552E83F90B3AE3A4D442C115CD5D08B8A52`.
- Status: rejected before public exact-set freeze; never publish or refill.

The second attempt, r2, selected the explicit executable and completed the
source/build/render/CSV preparation, but the package-wide privacy gate found
TeX's raw root `.log`, `.aux`, and `.toc` files still present. R2 therefore
stopped before manifests, exact-set verification, or publication.

- Preserved rejected r2 staging surface: 96 files / 7579759 bytes.
- Rejected r2 inventory digest: `777D281629F279E1F12D9989732284A028A556DEDE633EC585CFAE82E56C9954`.
- Preserved private r2 build surface: 7 files /
  123984 bytes.
- Private r2 inventory digest: `E377A9B5EBEBAC58C8A475AAFCC60567BF7328386727EB0AEF115E25E2C3F163`.
- Status: rejected at the privacy gate; never publish or refill.

The third attempt, r3, started again from the immutable predecessor and passed
the source, build, metadata, security, font, render, visual, CSV/JSONL, privacy,
and exact-set preparation gates. Its portable verifier nevertheless stopped
before freeze because one literal semantic check required a source sentence on
one physical line while the correct TeX wrapped it across a newline. The
translation reading itself was present and independently source-audited.

- Preserved rejected r3 staging surface: 96 files / 7647109 bytes.
- Rejected r3 inventory digest: `4D6125D3376904C388AC15D71569F4CF3EBB346A4D42AEC4C00C1A9AAA741E10`.
- Preserved private r3 build surface: 8 files /
  133996 bytes.
- Private r3 inventory digest: `56267A4C403E3BEB6193A500F01D6D6DCA5F261DBF75AA62678B7366564F8A02`.
- Status: rejected at the portable semantic verifier; never publish or refill.

Revision r4 starts again from the immutable predecessor, repeats all source,
build, metadata, security, font, render, visual, CSV/JSONL, privacy, and
exact-set gates, and replaces that brittle literal check with a
whitespace-tolerant semantic pattern. The verifier runs before and after the
atomic freeze. R4 supersedes only the three rejected freeze attempts; it does
not rewrite the independently audited translation fragment.