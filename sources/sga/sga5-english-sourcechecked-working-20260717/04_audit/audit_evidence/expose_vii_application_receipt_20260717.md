# Exposé VII production application receipt — 2026-07-17

Production file: `03_projects/language_management/english_germanic/03_working_translations/sga5_english_sync_workpass/SGA5_English_sync_workpass.tex`

- Before SHA-256: `8322E14DAEBE5EDFF35FCF5A71BFB863DE5C8AACEF5F1106D8394C5FB4496F07` (791,330 bytes).
- After SHA-256: `7185347ABAD933F4D99C8D8F68CED9F043A26C928F0867F3E41D5F903A4EDAE6` (792,758 bytes).
- Anchor conflicts: none.
- Scope edited: Exposé VII only.
- Compile deliberately deferred while concurrent III B/middle production work remains active.

## Applied receipt IDs

`SGA5-EXACT-0038`, `0042`, `0048`, `0052`, `0055`, `0056`, `0197`, `0200`, `0206`, `0219`, `0220`, `0223`, `0224`, `0226`, `0227`, `0237`, `0247`, `0248`, `0250`, `0252`, `0255`, `0256`, `0259`, and `0265`.

Receipt `0265` was subsumed by the complete printed pp.346–347 proof-tail replacement. All 24 old receipt forms are absent and all 24 new forms occur exactly once after application.

## Applied structural repairs

- Restored tag `(Q)` using the French authority's exact display representation `\[ ... \tag{Q} ... \]`.
- Corrected the left vertical arrow label in Proposition 8.6.3(a) from `\cup` to `(8.6.1)`; the right vertical arrow remains `\cup`.
- Replaced the entire proof tail after (9.8.8), restoring the Hironaka citation, both missing diagrams, the target `v''_*`, the reduction through `(D_2)`, and the final identity `(f_1)_*\circ v_*=u_*\circ f_*`.

The normalized inserted tail matches `tmp/sga5_audits/expose_vii_p346_replacement.tex` byte-for-byte after newline normalization and removal of its four package comments.

## Exposé VII structural parity after application

| Feature | English | French | Delta |
|---|---:|---:|---:|
| tag multiset | 100 | 100 | 0 |
| statement-number multiset | 62 | 62 | 0 |
| `tikzcd` | 15 | 15 | 0 |
| `tikzpicture` | 0 | 0 | 0 |
| diagram blocks | 15 | 15 | 0 |
| footnotes | 0 | 0 | 0 |
| `equation` environments | 0 | 0 | 0 |
| item entries | 64 | 64 | 0 |
| display openings | 407 | 410 | -3 |

The tag and statement multisets are exactly equal. The residual display-opening count difference is a pre-existing TeX representation/layout difference and is not caused by an omitted tag, statement, diagram, footnote, or item.
