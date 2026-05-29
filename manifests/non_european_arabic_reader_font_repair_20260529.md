# Non-European Arabic Reader Font Repair

Date: 2026-05-29

## Summary

The public-facing Arabic reader PDFs in `reader-pdfs/non-european/` were rechecked after a visual audit found boxed glyphs and platform-dependent font failures in several earlier Arabic drafts.

Promoted repaired readers:

- `30-01 Arabic Translation - Li Ye - Ceyuan Haijing, vols. 1-6 and 10-12.pdf`
- `30-02 Arabic Translation - Qin - Shuxue Jiuzhang, fasc. 1 and 4.pdf`
- `30-04 Arabic Translation - al-Kashi - Miftah al-Hisab.pdf`
- `30-05 Arabic Transliteration and Commentary - al-Khwarizmi - Algebra.pdf`
- `30-06 Arabic Translation - Omar Khayyam - Treatise on Algebra.pdf`

Held for later repair:

- `30-03 Arabic Translation - Yang Hui - Xiangjie, part 1.pdf`, because the currently available source is not yet a clean complete rebuild.

## What Changed

The repaired TeX sources now use locally available CJK/Arabic font configuration instead of Linux-only Noto file paths. The promoted PDFs were rebuilt, visually spot-checked, and the combined Arabic reader, index, summary JSON, upload manifest, and Zenodo metadata staging JSON were refreshed.

Superseded public PDFs are preserved in the local repair workspace and the current TeX/source bundles preserve the repaired builds for provenance and continuation.
