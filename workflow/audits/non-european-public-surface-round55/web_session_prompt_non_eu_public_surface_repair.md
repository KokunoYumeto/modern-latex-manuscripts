# Non-European public-reader repair and completion task

You are repairing the public-facing non-European mathematics manuscript archive. Work by human-readable author/work/language, not by internal batch names.

Use `NON_EU_PUBLIC_SURFACE_AUDIT_FOR_WEB_SESSION.md` and the contact sheets.

Priorities:

1. Repair visible public-surface defects first:
   - Aryabhata English (`10-07`) has visible layout leakage/overflow.
   - Arabic Li Ye (`30-01`) has visible overlap/misalignment and is missing vols. 7-9.
   - Ruska / Oldest Arabic Algebra (`60-05` / `10-17`) needs title/typography inspection.

2. Verify Sanskrit/Indian-script render quality:
   - `10-08`, `10-09`, `50-01` through `50-04`.
   - Check that apparent empty vertical space is intended and not lost text.
   - Check that Devanagari/Sanskrit transliteration and formulas are not clipped.

3. Complete partial work-level translations where source exists:
   - Modern Chinese Qin (`20-04`) is fasc. 1 and 5-9 only.
   - Arabic Li Ye (`30-01`) is vols. 1-6 and 10-12 only.
   - Arabic Qin (`30-02`) is fasc. 1 and 4 only.
   - Arabic Yang Hui (`30-03`) is part 1 only.
   - Kashi `Miftah al-Hisab` should be treated as a major Persian/Iranian computational arithmetic target, not a tiny snippet.

4. Begin Persian/Iranian lane only after the public-surface fixes above:
   - al-Biruni `al-Qanun al-Masudi`;
   - Tusi `Tahrir Euclid`;
   - Khayyam algebra;
   - Kashi `Miftah al-Hisab`;
   - al-Biruni `Elements/Tafhim` terminology bridge.

Output expectations:

- public-reader PDF;
- TeX source;
- manifest with source pages, gaps, and uncertain readings;
- no internal labels, no model names, no handoff/batch language on title pages;
- preserve older drafts as artifacts, but present the cleanest current reader as the public-facing PDF.
