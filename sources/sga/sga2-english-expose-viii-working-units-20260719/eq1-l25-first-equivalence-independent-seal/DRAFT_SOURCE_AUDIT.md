# Source audit

Scope: corrected French lines 2751--2794, original printed pages 92--93,
physical source-PDF pages 81--82, and recomposed running pages 73--74. The
printed-page-93 marker occurs inside line 2782 after `D'où`. Line 2795 is
blank; line 2796 begins the second step and is excluded.

The repaired target preserves conditions (a'), (c'), and (d); every quantifier and
inequality; the three implication directions; equations (2.5) and (2.6); both
unnumbered displays; editor's note (6), now using the explicit source marker
`(6)` rather than the initially rendered automatic marker `1`; Lemma 2.5, its application, and its
complete proof. The corrected authority branch at line 2792 is rendered as
`z in Spec(O_{overline{x},y})`; the original alternative branch is not silently
restored.

The historical phrase `x suit y` is rendered using the standard directional
statement `y is an immediate specialization of x`, followed by the source's
defining closure-and-dimension display. Literal `x follows y` is rejected as
opaque English. The jcreinhold `e7a259f` file is comparison-only; its page-74
comment uses the recomposed running number, not original printed page 93.

Independent source/formula/terminology review passed all mathematical content
and found the note-marker defect described above. The repaired target then
passed fresh independent build, extraction, and 300-dpi render comparison.
Machine/hash/privacy and exact-public-set evidence remain separate gates; this
audit does not claim a complete exposé or volume.
