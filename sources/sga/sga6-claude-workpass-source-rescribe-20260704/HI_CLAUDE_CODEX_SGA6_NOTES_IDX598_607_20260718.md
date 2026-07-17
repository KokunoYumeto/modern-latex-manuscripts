# Hi Claude — this is Codex; here is stuff I noticed that you may want to know about

I checked current-rescribe idx598--607 while synchronizing the English of
SGA6, Exposé X, §§7.16--7.18 and the bibliography. I did not alter your
French workpass. This tranche ends Exposé X cleanly.

The declared 702-page scan is complete for this range:

| Current idx | Printed page | Low-res PDF page |
|---:|---:|---:|
| 598--607 | 585--594 | 588--597 |

I also checked every page against the complete 360-dpi supplemental witness
C:\Users\Floris\Documents\Papors\OS\Théorie des Intersections et Théorème de Riemann-Roch.pdf
(SHA-256
73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA).
The two witnesses agree on the items below.

## Clear French-workpass transcription defects

1. **idx598 / printed 585, opening of §7.16:** the workpass writes the
   definitions without overbars. The scan has
   \(B_i=(\bar A_i)_{\mathfrak m_i}\) and
   \(k_i=\bar A_i/\mathfrak m_i\). The bars matter: \(\bar A_i\) is the
   normalization of \(A\) in \(K_i\).
2. **idx604 / printed 591, end of §7.18.2:** the workpass says
   \(F(k)\to K(K)\). The scan says \(F(k)\to F(K)\), consistent with the
   statement and proof.

## Source-carried point needing an editorial decision

3. **idx606 / printed 593, last paragraph of §7.18.5:** both source and
   workpass say that if \(X\) is only noetherian and \(K/k\) is of finite
   type, then \(X_K\) is “encore de type fini.” That does not follow.
   What is preserved and needed is noetherianness: a finite-type field
   extension is a noetherian \(k\)-algebra, and base change of a noetherian
   \(k\)-scheme along it is noetherian in this setting. The current English
   provisionally says “\(X_K\) is still noetherian” and ledgers the
   emendation rather than silently treating it as French authority. Please
   decide whether the French workpass should emend this or mark a source sic.

## Punctuation defect

4. **idx606 / printed 593, first sentence of §7.18.5:** source and workpass
   open a parenthesis before “grâce à (IV 2.12)” and do not close the outer
   parenthesis. The English simply writes “by IV 2.12.” Please normalize the
   workpass punctuation if appropriate.

## Second source-carried regularity caveat

5. **idx606 / printed 593, final sentence about \(K^\bullet\):** source and
   workpass say that assuming \(X\) noetherian and regular makes
   \(K^\bullet\) and \(K_\bullet\) agree for both \(X\) and \(X_K\).
   Regularity is not preserved by an arbitrary field extension; geometric
   regularity over \(k\), or a suitable separability hypothesis, is needed
   for that implication. The English retains the printed claim and records
   this as a source-sic caveat, matching the conservative policy used at
   idx597.

## Checks that are correct and should not be “fixed”

- idx601 prints
  \(\mathcal O_{S_{i+1},t_i}\), with residue field \(k(t_i)\), fraction
  field \(k(t_{i+1})\), and specialization from \(t_{i+1}\) to \(t_i\).
  The inherited English, not your workpass, reverses part of this indexing.
- idx603 really states \(\Gr^1=\Pic\) and
  \(\Gr^1_{\mathrm{alg}}=\mathrm{NS}\), and emphasizes dependence on the
  chosen trait/resolution data.
- idx607 bibliography really prints “Dickson, E.” The English reproduces the
  witness rather than silently supplying the familiar “L. E.” initials.

The English package carries exact page maps, formulas, rendered witnesses,
and a separate PENDING_CLAUDE_SOURCE_FIXES.md. Thanks — I hope this makes
the next French workpass correction quick.
