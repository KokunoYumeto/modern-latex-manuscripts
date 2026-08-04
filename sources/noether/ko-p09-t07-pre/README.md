# Korean Noether Paper 9 — T07 pre-control checkpoint

This immutable checkpoint preserves nine new T07 Korean targets before the producer regenerated its cumulative T07 controls. The exact T07 route defines nine units, `T07_U56.tex` through `T07_U64.tex`, and all nine corresponding target files are present and byte-stable.

T07 covers German authority lines 7023–7133: 7,436 bytes, SHA-256 `91EEBF6181823DFBF3C992C3B99EB6457320B08766EBC52D19F215A88C7161F6`. The nine Korean targets total 11,069 bytes with archive-bound tree SHA-256 `3D4CA466E1437774E83821A1E4B0878BDACC15A34FC9CF15328B7487BBA08C06`.

Important limitation: [manifest.json](files/root/manifest.json), [build.json](files/root/evidence/build.json), and [validate.json](files/root/evidence/validate.json) still describe T01–T06 and 55 targets. They are preserved unchanged and must not be cited as T07 validation. Archive maintenance independently established the exact nine-file T07 set from [route.json](files/root/route.json), replayed all 64 routed German source slices, and bound every file by path, bytes, and SHA-256 in [manifest.csv](manifest.csv).

The complete captured root contains 64 Korean targets totaling 71,372 bytes. The cumulative archive-bound target tree SHA-256 is `D800CAC6202E16709DCD4D397F23AF6CCA8DD2757A577FE5A34F98A306A47B7C`. No compilation, rendering, Korean review, source review, formula review, assembly, approval, certification, or new producer-side validation is claimed.

State: **T01–T06 complete producer draft; T07 nine-target pre-control checkpoint; Paper 9 incomplete; UNCHECKED, source-unchecked, formula-unchecked, Korean-unreviewed, uncompiled, unrendered, visually uninspected, unassembled, unapproved, and uncertified**.

Relative to `ko-p09-t06-r2`, 74 files are byte-identical, `evidence/build.mjs` changed, nine T07 targets were added, and no file was removed. This checkpoint preserves new target bytes without pretending the lagging producer controls have certified them. Every predecessor remains public, and no producer byte was edited or deleted by archive maintenance.
