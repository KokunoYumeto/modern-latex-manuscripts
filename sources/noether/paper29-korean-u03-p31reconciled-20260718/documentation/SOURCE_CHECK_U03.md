# P29-KO-U03 source check

The exact LF source equals full-P29 lines 41–45 byte-for-byte. The authority validator reports exactly one normalized occurrence in the sealed P31 head and one in the latest compiled unsealed comparison candidate. Raw line-ending mismatch is handled explicitly, not mistaken for source disappearance.

Printed evidence inspected at original resolution:

- printed p.28, SHA-256 65AA3A4C4565D849044E55A721FF9F5811677A6F58617AE562E317D4E1A81C27: cited footnote 2 identifies Steinitz locations for Charakteristik, Wurzelkörper, and Quotientenkörper;
- printed p.31, SHA-256 024008210DE649E1A452FBB9614DA4CE8453BC2B004233C79C9A8581951728BA: all U03 substantive text;
- printed p.32, SHA-256 7244CB121A9199EB1388DBEC862D6894D09F80378EAB5F6FEE143F16BDC55AB0: line-47 continuation boundary.

Source/target logic checked:

- necessity: choose \(\mathfrak R=\mathfrak S\) when \(\mathfrak S\) is finitely generated;
- sufficiency hypothesis: if characteristic is \(p\), \(P^{1/p}/P\) is finite; characteristic zero needs no restriction;
- proof target: a finite module-generating system over some subring of \(\mathfrak R\);
- \(\mathfrak K=\operatorname{Frac}(\mathfrak R)\), \(\mathfrak L=\operatorname{Frac}(\mathfrak S)\), with the stated containment chain;
- prior corollary gives finite algebraic \(\mathfrak L/\mathfrak K\);
- \(\mathfrak S\subseteq\mathfrak S'\), the ring of \(\mathfrak R\)-integral elements in \(\mathfrak L\);
- lack of integral closedness blocks direct use of Teilerkettensatz and motivates passage to \(\mathfrak T\).

Held discrepancy: sealed TeX encodes two identical footnote calls; printed p.31 uses two anchors with one marker/body. The target follows sealed TeX and does not edit the German exact source. No source owner has adjudicated the mismatch.

Independent read-only model review found no remaining substantive or quantifier defect after refinements. No human source audit is claimed.
