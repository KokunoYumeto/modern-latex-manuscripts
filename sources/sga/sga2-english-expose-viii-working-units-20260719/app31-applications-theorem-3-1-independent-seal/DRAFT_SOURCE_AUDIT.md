# Production source audit — SGA2-VIII-APP31

This bounded production unit covers corrected French lines 2874–2886. It
contains §3's heading and bridge, the full statement of Theorem 3.1, and its
full proof. Blank 2887 and Proposition 3.2 beginning at line 2888 are excluded.

The corrected arXiv TeX is authority. The same-edition 216-page compiled French
reader checks physical p. 84, running p. 76, original printed pp. 96–97,
emphasis, formula layout, and the p. 97 marker. It is not independent
corroboration. The jcreinhold e7a259f Markdown is comparison-only and was
rejected where it substitutes a bullet abutment, fenced text, closure
shorthand, raw depth notation, `\geqslant`, or page/citation apparatus that is
not source-audited.

The corrected second `\sisi` branch at line 2886 restores the words “of page
`\pageref{condition}`.” Label `condition` is attached to source line 2811 and
resolves to recomposed running p. 74; that statement is on original printed p.
93 and physical source-PDF p. 82. The target therefore reads “condition (iv)
on p. 74” and explicitly prevents p. 74 from being mistaken for a printed-page
locator.

The corrected source style renders `\Fa`/`\Ga` as upright operators `F`/`G`.
Decision `EG-SGA2-FG-NOTATION-ADJUDICATION-20260719-0001` has now closed
Option A: the unchanged target's established calligraphic `F/G` are an explicit
English normalization from those upright French glyphs, never literal source
preservation. The controlling addendum is
`SGA2_VIII_NGT1_FG_POLICY_POSTSEAL_ADDENDUM_20260719.md`, 3,093 bytes, SHA-256
`B6870E65A6A36DD6B4A6291CF38A36AC95BF4903541BF65147C0CB60D6E7858D`.
Canonical MD/CSV/JSONL/validation controls retain SHA-256 identities
`C6573262CC02336CB7A215D2C0D91FA7C1F222A361DEBD74D02DDD6CBA7EEA75`,
`7C960386CF48CB359D81BCEB28767A15010EA375D587660DB3B668DDCF35CB84`,
`CC896683B5D43B00F8458E4AF49EFBEEE65C5CF8496C28F5B4467E4BB9C6ACBB`,
and `C3ED69FAF9F4B75D20309C41288FBC4EA04A16C0844AC22A3E826B658BA91A46`;
manager-adjudication prose is
`8ED4C58A288E22002BF88A098D52661D392D663436E63C63CD011B7AC099F0ED`.

Three further target-glyph deltas remain explicit. The source `\ZZ` macro is
upright bold `\mathbf Z`, whereas the unchanged target uses blackboard-bold
`\mathbb Z`; the source `\R` and `\E` macros are upright operators, whereas
the unchanged target uses ordinary math-italic `R` and `E`. Those Z and R/E
choices remain separately provisional. The Theorem 3.1 conclusion at French
line 2879 contains a plain italic `F` amid surrounding corrected upright
`\Fa` occurrences; closed Option A regularizes both source forms to the one
established calligraphic English sheaf glyph. The exact mixed-source delta is
retained, the target is unchanged, and no literal-glyph-preservation claim is
made.

No QED or proof square was added because none occurs before the source boundary.
This is a production self-review, not an independent seal.

The first target build was visually correct but its enlarged parentheses in
the codimension and Leray displays generated two U+0001 bytes in text
extraction. Their exact pre-repair TeX/PDF/extraction/render identities remain
append-only in `DIFFICULTY_REVISION_LEDGER.jsonl`. Only those delimiters were
changed to ordinary source-matching parentheses; the final extraction has no
forbidden control bytes.

An independent evidence audit also found that the first public-log sanitizer
missed wrapped private font-resource path fragments. Raw logs remain internal.
The repaired public logs replace the entire wrapped resource block with one
safe summary and pass a stronger scan for user/profile fragments,
drive-qualified paths, and reconstructed split-line continuations. Both failed
and repaired log identities remain append-only. The target TeX/PDF did not
change.
