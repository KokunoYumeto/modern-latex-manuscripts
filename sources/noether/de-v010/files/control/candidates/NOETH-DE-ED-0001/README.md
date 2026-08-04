# NOETH-DE-ED-0001

Status: accepted local editorial successor; not published and not a critical edition.

This candidate starts from the exact later public GitHub preferred German
working head:

- publication commit: `b2262d074c01eabbacbfc0658575e1e589060327`
- Git blob: `0b07990f40d03ff47e815af516f83c95cc720513`
- parent bytes: `2,153,560`
- parent SHA-256: `6FCBF5DB4E4378032B7074442C181E3FCFE975275319E49B284CE3B868EE0D5D`

It applies exactly one independently source-confirmed later-transcription
repair, `NOETH-DEF-P22-0001`: at source line 12840, `\Bmod_i` is corrected to
`\Bmod_\lambda`. The printed Paper 22 witness visibly reads lambda and the
neighboring construction consistently indexes the displayed module by
lambda. No other semantic source line changed. The patch tool also changed
that line terminator from CRLF to LF; this tooling-only byte delta is recorded
explicitly rather than hidden.

Candidate identity:

- file: `Noether_German_NOETH-DE-ED-0001.tex`
- bytes: `2,153,565`
- SHA-256: `D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB`
- parent CRLF count: `23,129`; candidate CRLF count: `23,128`
- LF-normalized candidate bytes: `2,130,437`
- LF-normalized candidate SHA-256: `8E89A6BF94C8C5BF0BC2D125602BF1D349D9266D199C22DF7BE8DBD036A9B05B`

Evidence:

- printed witness: `../../evidence/NOETH-DEF-P22-0001/GDZ_P22_printed_p57_PPN235181684_0088_leaf61.jpg`
- witness bytes: `1,277,724`
- witness SHA-256: `32C0D0626784C504CD3AC0602720E2F4502A42A7A7ABF4DCB860FEF0AA024150`

Validation:

- two serial XeLaTeX passes completed with exit code 0;
- pass 2 produced 466 pages and no selected fatal, undefined-control,
  unresolved-reference, rerun, box, or missing-character diagnostic;
- output page 228 was rendered at 180 dpi and visually reopened; the corrected
  `B_lambda` sequence is present and the page layout is intact.

This candidate must not be confused with `NOETH-DE-RCV-0002`, which applied
the same repair to the surviving unpublished P09 file before the publication
surfaces had been checked. RCV-0002 is retained as historical evidence but is
superseded as an authority proposal.
