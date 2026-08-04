# Korean Noether Paper 9 — T01–T06 producer freeze

This immutable checkpoint preserves the complete producer root after T06. It covers German authority lines 6348–7022. Paper 9 remains incomplete; the next cursor is line 7023.

Start with [META.md](files/root/META.md), [manifest.json](files/root/manifest.json), [ROUTE.md](files/root/ROUTE.md), and [validate.json](files/root/evidence/validate.json). The 55 editable Korean targets are in [`targets/`](files/root/targets/). The retained complete Paper 9 German source is [source.tex](files/root/source.tex): 77,798 bytes, SHA-256 `7C9C4970145A374552E0D68C5A5C8B5614447086737D808E2235805E38217FA7`.

T06 adds ten target units, `T06_U46.tex` through `T06_U55.tex`, totaling 9,658 bytes with tree SHA-256 `ABD822EE0FCD8987DC40F0C381FE7ED2F5A3266A8842FC6E8BF81C58CCECF8A9`. Its German source is lines 6914–7022: 5,770 bytes, SHA-256 `4AFA31E0E7FB890A3381CED10461AB4F913A9ED47A555DB08EBF11B8EDA2F256`. The cumulative T01–T06 scope is 38,529 bytes, SHA-256 `0EED07A51F8CDACB3C01E7513CD0465F6EB0EEDE086A721C26ABD91B15367358`.

Independent archive replay matched 55/55 targets, 9/9 manifest-listed evidence files, all 55 routed German source slices, eight JSON documents, and 263 JSONL records. The supplied validator reports `PASS` for its stated mechanical scope only.

State: **T01–T06 complete producer draft; Paper 9 incomplete; UNCHECKED, source-unchecked, formula-unchecked, Korean-unreviewed, uncompiled, unrendered, visually uninspected, unassembled, unapproved, and uncertified**. The inherited `CLAIM.md` still records the initial T01 cursor and remains visible as exact provenance rather than being rewritten.

Relative to T05, 54 files are byte-identical, eleven controls/evidence files changed, ten T06 targets were added, and no file was removed. This checkpoint supersedes `ko-p09-t05` only in cumulative translated scope and current controls. Every earlier generation remains immutable public history. No producer byte was edited or deleted by archive maintenance.
