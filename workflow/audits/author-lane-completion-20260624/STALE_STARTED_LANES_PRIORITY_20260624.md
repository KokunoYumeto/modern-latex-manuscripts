# Stale / Started Translation Lanes Priority, 2026-06-24

This is a quick local-machine triage, not a full line audit. It uses visible folders, source packages, and recent handoff state.

## Steinitz vs Gordan Source Quality

Steinitz now has genuinely good source for most staged remaining work. The high-resolution page-image packages sampled at 600dpi:

- `Steinitz_HighRes_PageImages_B1_1916_BedingtIII_20260624.zip`: sample 3888 x 5767, 600dpi.
- `Steinitz_HighRes_PageImages_B2_1916_1922_Polyeder_Raumeinteilungen_20260624.zip`: sample 3448 x 5436, 600dpi.

The weak point remains `Steinitz_1908_Beitraege_zur_Analysis_Situs_Ranick_offprint.pdf`, which is usable but only about 300ppi and should still be replaced if a better host-volume scan appears. The older completed Steinitz batches are not independently line-certified.

Gordan has the stronger explicit source setup for the next big production work:

- `Gordan_Vorlesungen_Bd1_Determinanten_GDZ_600ppi_Source_20260613.zip`: sampled TIFF 3120 x 5183, 600ppi.
- `Gordan_Vorlesungen_Bd2_Binaere_Formen_GDZ_600ppi_Source_20260613.zip`: sampled TIFF 3336 x 5264, 600ppi.
- `Gordan_IA_theoriederabelsc00clebuoft_RAW_JP2_400ppi.zip`: raw IA JP2 witness for `Theorie der Abelschen Functionen`; ImageMagick reports dimensions but not useful embedded DPI.

Verdict: for currently staged work, both are good enough. Gordan has the cleanest explicit 600ppi source authority for the next major lane. Steinitz is more finishable and now has 600dpi page images for most remaining staged work, but has the 1908 caveat and older-batch audit risk.

## Closest To Finish

1. Steinitz: closest bounded author lane. About 478/713 handoff-produced pages, but not line-certified. Remaining work is known and source-staged except 1908 quality caveat.
2. SGA5: very active and probably close in the limited sense of "repair/certify one SGA volume," but still not globally certified page-by-page. Needs targeted source/TeX anchor audits, not broad transcription.
3. Noether German source-critical lane: active, with high-resolution IA/source backfills now present. Large but already deep into audit/repair mode. It can finish, but only if the latest cumulative is used and fixes are integrated, not just ledgers.
4. Takagi 1920: likely quick if scoped to the one foundational paper, but current local production appears much less mature than Steinitz/Noether/SGA5.
5. Gordan scoped book lane: high value and good sources, but not close. Finish `Vorlesungen` Bd. 1 and Bd. 2 before saying "Gordan" in an author-wide sense.
6. Weber Lehrbuch / beyond-Lehrbuch: substantial started work and aid packages, but corpus is large and status has been easy to misread. Needs a clean continuation audit before priority.
7. Sylvester Vol. I: started and useful, but not close to whole author. Vol. IV rescue exists; Vols. II/III need OCR/visual verification later.
8. Deligne: active diagram-witness/repair lane, but broad corpus and lots of subtle diagram risk. Not close in author-wide terms.
9. Poincare: source work improved, but production only early in Tome I. Not close.
10. Bianchi: high-resolution sources exist, but production appears near the beginning. Not close.
11. Seki / Mikami: important, but OCR is poor and diagrams/classical layout make it handwork-heavy. Not close.
12. Lie / Gordan full corpus / Cayley / Frobenius / Kronecker / Picard / Klein-Fricke / Kneser: useful started or staged lanes, but mostly source/audit-package level rather than near-finish author editions.

## Practical Priority If Rate-Limited

Finish/certify in this order:

1. Steinitz, because the remaining staged work is finite and source quality is mostly good.
2. SGA5, because the remaining work is mostly certification/repair rather than raw acquisition.
3. Noether, because it is already in source-critical repair mode and has downstream multilingual value.
4. Takagi 1920, if a compact high-value win is desired.
5. Gordan, scoped to `Vorlesungen` Bd. 1, then Bd. 2.

Do not treat old "accepted" labels as canonical. For all stale lanes, use "handoff-produced" until a fresh source-page visual audit has happened.
