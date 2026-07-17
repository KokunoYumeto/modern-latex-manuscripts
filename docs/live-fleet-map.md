# Live Translation Fleet Map

Last evidence refresh: 2026-07-18 00:44 Europe/Berlin.

This page records concrete output, not task activity. A task title, branch name,
commit subject, or folder called `COMPLETE` is not enough. A row advances only
when the underlying TeX/PDF, scope statement, build or audit evidence, and
publication state agree.

## Status Key

- **Public:** present on the cited Zenodo concept record and mirrored on GitHub
  where practical.
- **Sealed local:** a bounded artifact has a coherent manifest, build, and QA
  state, but has not yet been published.
- **In review:** substantive text exists, but its current endpoint, build, or
  source-reconciliation gate is not frozen.
- **Witness/support:** useful corpus, OCR, terminology, or review material, not
  a promoted translation.

## Current Work

| Lane | Work and verified scope | Public state | Next gate |
|---|---|---|---|
| Archive / publication | GitHub is the inspectable working front; Zenodo carries reader-first releases. Noether concept DOI `10.5281/zenodo.20412587`, SGA `10.5281/zenodo.20410947`, and interlanguage methodology `10.5281/zenodo.21124403` are the active public homes. | **Public.** Noether version `10.5281/zenodo.21420665`; SGA version `10.5281/zenodo.21420146`; interlanguage version `10.5281/zenodo.21418942`. | Refresh this map and public metadata whenever a sealed artifact changes the reader-facing state. |
| English / Germanic - Noether | Older RA10 English coverage exists for all 43 papers. Twelve standalone English components are synchronized to German R823: Papers 5, 7, 10, 18, 20, 25, 26, 27, 28, 29, 36, and 37. Their July 18 grouped package has 304 files and a zero-failure 302-row manifest/hash check. | **Public** in Noether file `09` and mirrored under `sources/noether/r823-synchronized-components-20260718/`. The full RA10 reader remains an older unsynchronized working translation. | Dispose the remaining 31 paper deltas before calling the cumulative English branch R823-synchronized. |
| English / Germanic - SGA 5 | A 309-page English working edition covers the ten selected exposes through the printed-page-484 index. Its workpass records final dispositions for 432 scan-derived candidates, source-critical repairs, build evidence, and visual QA. | **Public** on SGA version `10.5281/zenodo.21420146`. Serious source-aware working translation, not a critical edition or independent certification of every locus. | Revisit only for a documented source correction or public-package metadata decision; do not restart synchronization from an older control. |
| English / Germanic - SGA 6 | The sealed English Expose X cumulative covers idx532-597, printed pp.519-584, through Appendix 7.15. New direct-source audit notes cover idx598-607 and idx608-615 and record concrete French-workpass defects, source-carried caveats, and translation emendations. They do not supply a frozen cumulative release whose TeX, PDF, status, source map, QA, manifest, and hashes all name one endpoint. The French source-rescribe public checkpoint reaches idx662. | **In review.** The audit findings through idx615 are public on GitHub; the older full English control remains public but unsynchronized. No idx615 English Zenodo release is claimed. | Freeze one endpoint by aligning TeX, status, source map, build, QA, manifest, and hashes; then publish that exact endpoint. |
| Romance - Noether Spanish | A 473-page R823 cumulative covers 81/81 source units, all 43 papers, all 31 book sections, post-book material, and terminal matter. The local v3 gate reports every check passed, 101 terminology decisions, clean build diagnostics, 473 rendered pages, and stable hashes. The archive pass independently matched 13/13 frozen artifact hashes and inspected sampled renders. | **Public** on Noether version `10.5281/zenodo.21420665`: directly readable PDF plus one coherent TeX/source-authority/evidence ZIP. This is a source-reconciled working translation, not native-language certification or a critical edition. | Accept corrections through GitHub; regenerate the complete gate and hashes after any source or translation edit. |
| Romance - Noether French | A broad R823 French corpus candidate exists, including a cumulative TeX and hundreds of component TeX files. The last cumulative PDF predates active Paper 02 and later syntax/math repairs. No final whole-corpus gate was found. | **In review.** Do not describe the French branch as sealed or current merely because a broad cumulative exists. | Finish the active source/math repairs, rebuild the exact current TeX, run parity/build/visual gates, and freeze hashes. |
| Romance - SGA 5 Spanish | Complete Expose I including appendix and bibliographies, plus Expose III through section 2.4, is translated and source-reconciled in the growing cumulative. | **In review.** The lane explicitly requires regenerated current build/hash/QA evidence after the latest integration. | Rebuild and freeze current evidence, then continue at Expose III Proposition 2.5. |
| Romance - SGA 6 Spanish | Expose X idx532-537 / printed pp.519-524 is a bounded internally checked working translation. | **Sealed local component**, not a complete expose or SGA volume. | Continue at idx538 and preserve the same source-coordinate and QA discipline. |
| CJK | Complete bounded Noether Paper 26 and Paper 36 notices exist in Simplified Chinese, Traditional Chinese, Japanese, and Korean, with current R823 source reconciliation, TeX/PDF builds, text extraction, and render checks. | **Public** inside Noether file `09`. No full CJK reader is current to R823. | Korean continues with Paper 28; Chinese/Japanese require paperwise R823 delta reconciliation. |
| Slavic / Interslavic | Noether Paper 06 has 16 units in Ukrainian, Russian, Interslavic Latin, and deterministic Interslavic Cyrillic. The approved orthographic tranche changed 9 files / 17 forms, preserved Ukrainian and Russian byte-for-byte, passed 32 Interslavic builds, and is idempotent. The lecture-book title/introduction is also available in all four branches, covering 1 of 32 core book units. | **Public bounded components** in Noether files `08` and `09`. Older broad Slavic readers remain working controls and are not current-source certification. | Reconcile Paper 06 semantically against R823, then continue the book at `BOOK_S01`; do not replay the closed orthography tranche. |
| Arabic / Persianate / RTL | Noether Paper 06 opening units `P06-S0002`, `P06-S0004`, and `P06-S0005` exist independently in Arabic and Iranian Persian. Both targets build warning-free; terminology and native mathematical review remain pending. | **Sealed local component / working translation.** Not publicly promoted at this refresh. | Continue at `P06-S0006`; treat Dari and Tajik as independent targets rather than automatic Persian conversions. |
| Malay / Southeast Asia / Pacific | The complete five-segment Noether Paper 36 notice exists as a one-page Indonesian TeX/PDF with clean build, text extraction, and visual QA. | **Sealed local component / working translation.** No native review or final-publication claim. | Translate the same complete work independently into Malaysian Malay; retain unresolved historical terminology explicitly. |
| Africa / Horn / West | A 113-word OpenStax Prealgebra 2e section 2.1 microtranche exists in Somali and Oromo, with TeX/PDF, terminology notes, source coordinate, and technical QA. | **Sealed local pilot / unreviewed working translations.** | Obtain language and mathematical review before promotion or scale-up. |
| Turkic | One manager now inventories a nine-language canonical corpus plus Chuvash candidates and 568 curated files. Kyrgyz, Uyghur, and Uzbek one-page Hefferon review microdrafts compile and render, but no translation satisfies the lane publication gate. | **Witness/support plus incomplete microdrafts.** No public translation candidate. | Reconcile one stable source unit completely and obtain the declared language, mathematics, adverse, external, and comprehension reviews. |

## Release Queue

1. Do not publish SGA6 English through idx615 until every release document names the
   same endpoint and the current build/hash/QA evidence is frozen.
2. Do not publish the active French Noether cumulative until the post-build
   repairs are compiled and its whole-corpus gate is explicit.
3. Refresh the interlanguage methodology record when the fleet map, source-use
   method, or reusable workflow changes materially; translation payloads remain
   on their author/work records.

## Refresh Rule

Every archive sweep should check the live lane status files, artifact hashes,
Git branches, and public Zenodo API. This page should be changed only for a
real scope, gate, or publication transition. Unchanged task chatter does not
create a map update.
