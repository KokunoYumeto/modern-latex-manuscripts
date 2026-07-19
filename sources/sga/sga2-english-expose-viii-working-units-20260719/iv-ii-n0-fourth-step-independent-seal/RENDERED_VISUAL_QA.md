# Rendered visual QA

The one-page target was rendered at 300 dpi and visually inspected in full.
Title hierarchy, authority box, proof transition, condition `(ii)`, depth
inequality, induction sentence, and base case are legible, aligned, and
unclipped. The generous lower whitespace is intentional for this short
bounded checkpoint; no content is missing.

The directly compiled same-edition French physical page 82 was also inspected
at full resolution. The target agrees with the bottom-of-page source block:
printed marker 94 precedes the unit; the implication is `(iv) => (ii)`; the
condition has `x\in U`, `c(x)=1`, `prof F_x\geq n`; and the page ends after
the `n=0` vacuity sentence. The `n=1` case begins on physical page 83 and is
excluded.

- target PNG SHA-256:
  `B258602D805D21EE178BC73DE984742718013BC2E5DFFF8EDF512DC2E480E520`;
- source physical-page-82 PNG SHA-256:
  `2EE16940E4335F9F3A5CB564855AA1D648D8C5A4B624FB0BD1AC2E03CC5295B8`.

Independent review rendered both target and source controls again and obtained
the same byte identities. Status: target/source visual and independent render
gates pass.
