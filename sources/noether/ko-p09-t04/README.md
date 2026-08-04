# Korean Noether Paper 9 — T01–T04 producer freeze

This immutable checkpoint preserves the complete 49-file producer root captured after T04 closed mechanically. It covers the title, introduction, and §§1–3 through German authority line 6725. Paper 9 remains incomplete; the next cursor is §4, line 6726.

Start with the current machine controls: [manifest.json](files/root/manifest.json), [route.json](files/root/route.json), [validate.json](files/root/evidence/validate.json), and the 29 editable files in [`targets/`](files/root/targets/). The retained complete Paper 9 German source is [source.tex](files/root/source.tex): 77,798 bytes, SHA-256 `7C9C4970145A374552E0D68C5A5C8B5614447086737D808E2235805E38217FA7`.

The cumulative T01–T04 scope is lines 6348–6725: 21,268 bytes, SHA-256 `F5C79FADDE6A8CFEBC74CB6A2EFBCF80B2D85DFC52A57E37A16B0BB567DEDC6C`. Its 29 Korean targets total 32,462 bytes and have tree SHA-256 `EA945A541FFE5461B297BA9B1979250047F6F8DD468D3A077E17F26EB738AB99`.

Independent archive replay matched 29/29 targets, 9/9 manifest-listed evidence files, all 33 routed source slices, eight JSON documents, and 158 JSONL records. The supplied validator reports `PASS` for its stated mechanical scope only. No build, render, visual QA, source check, formula check, Korean review, assembly, approval, or certification is inferred.

State: **T01–T04 complete producer draft; Paper 9 incomplete; UNCHECKED, source-unchecked, formula-unchecked, Korean-unreviewed, uncompiled, unrendered, visually uninspected, unassembled, unapproved, and uncertified**.

Two inherited human surfaces lag the current machine controls: `CLAIM.md` still records the initial T01 cursor, and `META.md` ends with the T03 continuation. They are preserved byte-for-byte as provenance and are not presented as the current T04 cursor. `ROUTE.md`, `route.json`, `manifest.json`, `build.json`, and `validate.json` agree on T04 and line 6726.

This checkpoint supersedes `ko-p09-t02` only in cumulative text scope. The T01 and T02 generations remain immutable public history. No producer byte was edited or deleted.
