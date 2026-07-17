# Exposé III B stable-live revalidation

- Current-live cumulative TeX snapshot at final package revalidation: `313435A40E17DF53DC9C86D271548EFCE1C27520662D609D05C4FB373211E4F2`.
- Current live Exposé III B UTF-8 slice: 127,511 bytes; SHA-256 `0405187228682396D5D78830868277F35B37B3036BDF6435C139145E84246CC5`.
- Earlier coordination snapshots `94FD91FD0EF018E95D0C9EE04A34B8DDABCF3F7D5DB224B9D5320FE479B3EC25` and `237ACFB99BBD51A83495662F9D56260768DB7CFB4F22AE132583B2A3D71EF978` have the identical III B slice. The cumulative hash changed only through later non-overlapping edits outside III B.
- Desired semantic anchors: 32/32 occur exactly once in the stable III B slice; see `ANCHOR_VALIDATION.csv`.
- Distinctive legacy variants rechecked absent: the superscript-`b` category, Proposition 6.23 equality, Langlands `b/\Phi`, generic square reference, `B_\natural` reading, omitted repeated `\varphi`, inserted `p_1^*` in (6.2.3), unhyphenated `G`-equivariant wording, superscript-minus footnote category, and the old generic square prose.
- Definition (6.5.3) at lines 5970–5975 has the corrected domain `\delta^*\RHom_A(...)`, without `c_*`. A later, source-valid correspondence-level trace at line 6012 does contain `\delta^*c_*\RHom_A(c_1^*L,c_2^!L)` and is not the rejected definition anchor.
- Structural parity regenerated against the current live cumulative: III B is exact for 40/40 `tikzcd`, 1/1 `tikzpicture`, 41/41 total diagram blocks, 7/7 footnotes, 145/145 equation environments, 240/240 display openings, 9/9 items, 151/151 tags, and 28/28 statements, with no III B tag/statement multiset difference.

No current-live III B regression or unresolved source ambiguity was found.
