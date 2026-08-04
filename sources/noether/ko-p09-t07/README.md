# Korean Noether Paper 9 — controlled T01–T07 freeze

This immutable checkpoint preserves the producer-controlled T01–T07 generation. It supersedes the pre-control checkpoint by adding a current T07 manifest, build report, validator, evidence ledgers, and expanded rationale while retaining all nine T07 target bytes unchanged.

The translated scope is German authority lines 6348–7133: 45,965 bytes, SHA-256 `5580DC085A13755614796F2538D58404BD929C1FD8F0242DBD4ABF5E52D911B4`. Paper 9 remains incomplete; the next cursor is line 7134.

Start with [META.md](files/root/META.md), [manifest.json](files/root/manifest.json), [ROUTE.md](files/root/ROUTE.md), and [validate.json](files/root/evidence/validate.json). The 64 editable Korean targets total 71,372 bytes with tree SHA-256 `D800CAC6202E16709DCD4D397F23AF6CCA8DD2757A577FE5A34F98A306A47B7C`.

T07 comprises nine targets, `T07_U56.tex` through `T07_U64.tex`, totaling 11,069 bytes with tree SHA-256 `3D4CA466E1437774E83821A1E4B0878BDACC15A34FC9CF15328B7487BBA08C06`. Its German source is lines 7023–7133: 7,436 bytes, SHA-256 `91EEBF6181823DFBF3C992C3B99EB6457320B08766EBC52D19F215A88C7161F6`.

Independent archive replay matched 64/64 targets, 9/9 manifest-listed evidence files, and all 64 routed source slices. Eight JSON documents and 307 JSONL records parse. The supplied validator reports `PASS` for its T01–T07 mechanical scope.

State: **T01–T07 complete producer draft; Paper 9 incomplete; UNCHECKED, source-unchecked, formula-unchecked, Korean-unreviewed, uncompiled, unrendered, visually uninspected, unassembled, unapproved, and uncertified**.

Relative to `ko-p09-t07-pre`, 73 files are byte-identical, eleven controls/evidence/provenance files changed, and no file was added or removed. The pre-control checkpoint remains public as the exact chronology of the target bytes before control regeneration. No producer byte was edited or deleted by archive maintenance.
