# Korean Noether Paper 9 — T01–T05 producer freeze

This immutable checkpoint preserves the complete producer root after T05. It covers the title, introduction, and §§1–4 through German authority line 6913. Paper 9 remains incomplete; the next cursor is line 6914.

Start with [META.md](files/root/META.md), [manifest.json](files/root/manifest.json), [ROUTE.md](files/root/ROUTE.md), and [validate.json](files/root/evidence/validate.json). The 45 editable Korean targets are in [`targets/`](files/root/targets/). The retained complete Paper 9 German source is [source.tex](files/root/source.tex): 77,798 bytes, SHA-256 `7C9C4970145A374552E0D68C5A5C8B5614447086737D808E2235805E38217FA7`.

T05 adds sixteen target units, `T05_U30.tex` through `T05_U45.tex`, totaling 18,182 bytes with tree SHA-256 `D3E9BDB8C96EF79EAD5AC509FE725FAF7D57147AC7ED8EB472AF97FE64DE9FF6`. The cumulative T01–T05 scope is lines 6348–6913: 32,759 bytes, SHA-256 `594E917087720E6E3115C0D42DDF5195B31662B4D2D891C95E2C111AF5CBFA24`.

Independent archive replay matched 45/45 targets, 9/9 manifest-listed evidence files, all 50 routed German source slices, eight JSON documents, and 222 JSONL records. The supplied validator reports `PASS` for its stated mechanical scope only.

State: **T01–T05 complete producer draft; Paper 9 incomplete; UNCHECKED, source-unchecked, formula-unchecked, Korean-unreviewed, uncompiled, unrendered, visually uninspected, unassembled, unapproved, and uncertified**. The inherited `CLAIM.md` still records the initial T01 cursor and remains visible as exact provenance rather than being rewritten.

This checkpoint supersedes `ko-p09-t04-r2` only in cumulative translated scope and current controls. All earlier T01, T02, T04, and T04-r2 bytes remain immutable public history. No producer byte was edited or deleted by archive maintenance.
