# Parent-manager handoff — SGA 6 English complete layered working edition

Finalized working-edition handoff: 2026-07-18  
Owner: English/Germanic language-management parent  
Disposition: **CORRECTED INTERNAL ENDPOINT; PARENT CORRECTIVE ZENODO VERSION REQUIRED**

## Outcome handed upward

The SGA 6 English production lane now has a complete layered reader architecture covering the declared 702-page source scan, including the physical terminal back matter. The work is no longer only an inventory or a partial tail. Its current release limitation is authority, not physical completeness:

- source-PDF 001--525 uses the strongest audited repair108 English prefix, honestly labelled inherited and only partially source-synchronized;
- idx532--662 is source-checked English under French control certified for the same scope;
- idx663--702 and unindexed source-PDF 693--702 are scan-checked English drafts pending Claude/French certification;
- the complete volume terminates at source-PDF 702 / printed page 700 / notation entry `Z(x)`.

Production workspace:

`C:\Users\Floris\Documents\interlanguage\03_projects\language_management\english_germanic\03_working_translations\sga6_complete_layered_sync_sourcePDF001_702_en_20260718`

This handoff is finalized in that workspace and mirrored to:

`C:\Users\Floris\Documents\interlanguage\03_projects\language_management\english_germanic\00_lane_control\SGA6_COMPLETE_LAYERED_HANDOFF_20260718.md`

with the final build/QA hashes below.

## Final principal artifacts to seal

| Artifact | Final receipt required |
|---|---|
| `SGA6_English_Complete_Layered_WorkingEdition.tex` | SHA-256 `7E731468367BBC27A37BC224BBBEE3FAB37A3852FC76BB541A1AF36EF76D50F3`; bytes `3917` |
| `SGA6_English_Complete_Layered_WorkingEdition.pdf` | SHA-256 `F8B1E15754BEB5C83CF2A47B261D6F9F907DE5B7E8A6ED4DF311C624E38C7B8E`; bytes `2565870`; pages `381` |
| final build pass 1 | `logs/COMPLETE_BUILD_PASS1.log`; SHA-256 `25C87149FC9F3DDCF37235AD55A42B369FA993D14BCA2F1BF621208496AA2632` |
| final stabilized build pass 2 | `logs/COMPLETE_BUILD_PASS2.log`; SHA-256 `A9B1182E2E266B8A4A8A883D17B1E5F7812F83F7951EF67269C15A01D9FC6E1C` |
| complete-reader visual QA | `render_check/complete_working_edition/VISUAL_QA_COMPLETE.md`; SHA-256 `C3AD4FF832E2CD18BC2072A40397C930730E911F77F2A5158D379490FB90D2FA` |
| package-wide checksum manifest | `SHA256SUMS.csv`; exact self hash, bytes, and entry count are in `MANIFEST_SELF_SHA256.txt`, generated last |

Do not replace these placeholders with a receipt from an earlier compile. The final PDF receipt must postdate the final macro-state, title/status, TeX, and metadata decisions and must be the PDF actually rendered for QA.

## Stable component receipts

### Prefix and seam

- Selected source: repair108 whole file SHA-256 `FFCE609E3F38124C801304F109767C60A94B9319637B0F926B9D797CCCDC74D8`.
- Exact extraction: lines 71--13575, before the inherited Exposé X continuation.
- Initial repair108 extraction-control SHA-256: `EEEDD95BB9C042CCB1E4D9F5685248609E870DB3F0C270598FCE28B5B007DE2B`.
- Final corrected production-prefix receipt: SHA-256 `3FE03C89BA0662A61607CDE80DDB24BC4683FA37C30C1DA580908CFAD186F68C`; bytes `812912`.
- Structural seam witness SHA-256: `C3EB27CB9C162C2CDAFBD03DCEBCBF450CDA8F281C061B2C7A86A4A338E919B1`.
- Seam: Exposé IX Corollary 4.4 immediately followed by Exposé X / idx532 / source-PDF 526.

The initial extraction hash is a lineage receipt, not a post-repair production receipt. All documented targeted gates are now closed, but that is not a whole-prefix page-by-page certification. The prefix therefore remains **inherited, partially source-synchronized**, not globally source-checked.

### Synchronized tail

- Tail body SHA-256: `613006848EC8968D991FE2556AEC1B49AF29EB268FCA8C9C559DD61EF238C1A4`.
- Reviewed tail master TeX SHA-256: `86B04194E6B2C4EE165B8812167ECEE300DBB331F34A9A84B795AE139E66D75A`.
- Reviewed 109-page tail PDF SHA-256: `7B1280140ADE4BC7FBA152F3BA9006EA6AA1E288FBADB9740D2980085098164E`.
- Final repaired-tail pass-1 log SHA-256: `AB452450F81ABF8BE083E97872DD4BE74ACEAFE95DD461FF3951ECDD7EB4616A`.
- Final repaired-tail pass-2 log SHA-256: `E527A66B9C7DE85987D211EB1A4E272C0257B9A8D55BB8DBADAE311D86C294E3`.
- Independent review confirms exactly 171 consecutive markers idx532--702, ten unindexed markers, clean joins, clean build, complete rendered pages, and physical terminal `Z(x)`.

### Normalized ledgers

| File | Scope | SHA-256 |
|---|---|---|
| `ledgers/PAGE_INDEX_LEDGER.csv` | 171 indexed rows plus ten unindexed terminal rows | `214F7682A456193D9E64872FBB3594561CB76CF3321E81D409BA8CA70796B0C4` |
| `ledgers/SOURCE_FORMULA_SYMBOL_COMPARISON.csv` | 324 source/formula/symbol comparison rows | `1D11A7B92BFD1B3E5A9FAD9B67FE78717F7B90876CEF74C49C7CB17DEA3EFCDC` |
| `ledgers/TERMINOLOGY_AND_REJECTED_CHOICES.csv` | 213 terminology and rejected-choice rows | `210DF4FE7E7E76247457DBB1F7F554156171EDBB866D68BBDDA90D0131A4BC9A` |
| `ledgers/PENDING_CLAUDE_SOURCE_FIXES.md` | complete durable French/source-control and public-record notes | `03B927AD378BB8CF875D3963B933817B74E0397C37375C41494D2B42BD90DE55` |
| `ledgers/AUTHORITY_LAYER_LEDGER.csv` | source, French, English, inherited, and style authority layers | `746135071EBF05793F18C53935B2BBC2AE10E2095F68088478A520F0DD6EBFF7` |
| `ledgers/MERGE_REPORT.md` | coordinate and certification validation | `F5A99649757FC1111DECEBE799AE7A8CBC6F7EAE7108ABACF78515A16A6B57FD` |

## Source authority and exact frontier

Ultimate scan:

`C:\Users\Floris\Documents\Papors\OS\sga6.pdf`  
702 pages; SHA-256 `5194436E290B8FCA54BACD5FF672588335408F1AAD3AE07D62BBA68DF35E3D76`.

High-resolution supplement:

`C:\Users\Floris\Documents\Papors\OS\Théorie des Intersections et Théorème de Riemann-Roch.pdf`  
720 pages; SHA-256 `73FBBAD41340C12ECCDCFCF6C3A1656953FE3D712AA8E391678458CCD17B4BAA`.

Current French control:

`C:\IL_GitHub\00_main_current\sources\sga\sga6-claude-workpass-source-rescribe-20260704\sga6_fr_workpass.tex`

- commit `8ccdcf8eeef35cba9cc7ca09fe79e6b3f863becc`;
- SHA-256 `77703F2D7E8FF9000C2C1E7320A903A48ADE00BF62C8F5F240FF88C42ED82703`;
- certified through idx662 / printed 649 / source-PDF 656;
- next French certification work begins at idx663 / printed 650 / source-PDF 657.

## Required parent actions

### 1. Finish and seal the complete reader

- Complete the final two-pass build from clean auxiliary state after all macro and metadata changes.
- Confirm the complete reader preserves the reviewed tail's macro meanings and text, not merely that it compiles.
- Render every final page memory-safely; inspect contact sheets and full-resolution seam/join/terminal pages.
- Freeze exact TeX, PDF, log, QA, and package-manifest receipts.
- Keep publication metadata placeholder-free and regenerate all dependent hashes after any change.

### 2. Preserve the closed targeted prefix gates and the remaining limitation

The documented targeted checks at source page 14; pages 141--150; manual pages 277, 286, 347, 350, and 377; and retained repair105 page 431 are closed in `ledgers/PREFIX_TARGETED_GATE_DISPOSITIONS.csv` and the two prefix-repair evidence bundles. Keep the page-14 X/Y choice pending Claude. Do not turn those targeted closures into a whole-prefix line-by-line certification claim; the prefix authority remains inherited and partially source-synchronized.

### 3. Coordinate Claude's remaining source-rescribe

Claude notes already live beside the French workpass, and the English mirror is `ledgers/PENDING_CLAUDE_SOURCE_FIXES.md`. Do not silently edit French from this lane. After Claude commits certification through idx702 and the unindexed back matter, diff and adjudicate the English, update all ledgers, rebuild, rerender, and rehash.

### 4. Resolve license and credit

The complete inherited English names no translator/model. Repair108 is from a Codex-named tree. The new synchronization was produced in a user-directed Codex task. The parent must select the final editor/translator credit, inherited-layer attribution, Claude role, AI-assistance disclosure, and license/rights statement. Do not upload the scans or scan-derived evidence unless rights are affirmatively resolved.

### 5. Coordinate the existing Zenodo record

- Existing concept DOI: `10.5281/zenodo.20410947`.
- Current published version verified from the Zenodo API: `10.5281/zenodo.21421931`.
- Previous public version: `10.5281/zenodo.21420146`.
- idx662 predecessor: `10.5281/zenodo.21419947`.
- Superseded interim record: `10.5281/zenodo.21419703`.

Version 21421931 is a stale publication endpoint: its public PDF SHA-256 `29CEEA7CE5ECBA9A8C36D34E170D19AAC8C014D64836FEAA77D723CB0F361939` shows marker 14 on page 81 but omits footnote 14; its ZIP SHA-256 `ED9CEC2D320041B626D5DDE424D651834C8961FE541C8253631FF5622AF8A2AC` contains the failed inline-display footnote code. Use `controls/PUBLIC_RECORD_21421931_CORRECTION_REQUIRED.md`. Do not mint a duplicate record. Coordinate a corrective new version under the existing concept DOI using the corrected internal PDF SHA-256 `F8B1E15754BEB5C83CF2A47B261D6F9F907DE5B7E8A6ED4DF311C624E38C7B8E`, explicitly note the restored footnote, preserve historical files, and archive returned metadata/checksums.

## Publication state at handoff

Physical translation coverage: **complete through source-PDF 702**.  
Uniform source certification: **not complete**.  
Final complete-reader build/QA receipts: **PASS — clean two-pass build, independent integration review, 381/381 rendered pages, 20/20 contacts, and 31/31 targeted gate pages sealed**.  
Rights/license: **unresolved**.  
Attribution/disclosure: **unresolved**.  
Zenodo action: **PARENT-COORDINATED CORRECTIVE VERSION REQUIRED; NO DUPLICATE CONCEPT**.
