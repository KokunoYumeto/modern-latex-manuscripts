# Web P04 pp. 118-143 integration adjudication

Web returned a 26-page source audit with 18 grouped source-backed repairs. Its validation cumulative was deliberately not used as an authority because its input hash was `6AC8F355BF3BABD9610F52240D48BDE359284DB7D775E47C489ECADAC8B940D5`, not the requested live hash. The compact return ZIP itself hashes to `8ACB934E9E793AC16542765FE9C6806FF90B4DF0CD84EE86E73E43D57DB8A7DC`.

LocalCodex applied only the bounded content diff to the live P05+P02 successor. A line-level survival check found all 26 added TeX lines present and all 26 superseded lines absent. The most consequential repair, printed p. 142 formula (48), was independently reopened against the source comparison: the source has `f\equiv`, a second equality rather than a multiplication join, and the full non-strict chain in (49). The p. 132 partition/source-glyph evidence was also reopened.

The merged cumulative compiled twice to 466 pages. All changed output pages 49-55 and 57-59 were rendered at 400 dpi and reopened visually. No clipping, overlap, broken glyph, equation-number displacement, or page-boundary failure was found. The exact Web ledgers, bounded diff, input-hash warning, contacts, and source manifest are preserved in `03_audit/Web_P04_p118_143/`; the complete original Paper 4 PDF is preserved under `02_source/P04_original/`.

Disposition: all 18 grouped repairs are integrated on the live current head. P04 printed pp. 118-143 now has a controlling independent complete-page pass, and with the already closed pp. 144-154, Paper 4 is closed subject only to a concrete future source contradiction.
