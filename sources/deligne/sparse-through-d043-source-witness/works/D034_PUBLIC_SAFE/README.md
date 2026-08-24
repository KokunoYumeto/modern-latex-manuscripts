# D034 canonical normalization

This directory contains independently normalized French and English mathematical editions of Pierre Deligne's *Cycles de Hodge absolus et périodes des intégrales des variétés abéliennes*, together with a restrained apparatus and deterministic audit evidence.

The controlling authority is the 12-page NUMDAM/SMF PDF at SHA-256 `c8b618a1da8b060e946c2fbcf6a1d36db73e4f3841330f8822043c593b7f4ece`. Physical page 1 is cover/copy matter and is recorded only in the apparatus. Physical pages 2-12 are article pages, printed 23-33, and map one-to-one to the 11 pages of each reader. Pierre Deligne is the author; the exact source role is `rédigé par J. L. Brylinski` (`written up by` in English).

All bytes from the returned S02 packet are preserved unchanged under `../inherited_zero_accepted/` and remain `ZERO_ACCEPTED`. The comparator, candidate ZIP, and diagram-selection ZIP are locator-only witnesses. No inherited PDF, TeX, candidate member, or diagram member is promoted into the canonical corpus merely by agreement. Canonical source files include deterministic PDF primitives and the authority-proved restoration of the accents in `SOCIÉTÉ MATHÉMATIQUE DE FRANCE`; the malformed inherited apparatus rendering of `Mémoire n° 2` is also corrected.

No production image fallback is needed: every formula, exact sequence, determinant, and the printed-page-29 two-column table is rendered as native TeX. The `audit/renders/` images are QA evidence only.

Final corpus status is controlled by `FINAL_GATE_RECEIPT.json`, not by inherited receipts.
