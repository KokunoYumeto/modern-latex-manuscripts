# Source use and custody — Noether Paper 37 Chinese rebase

This record governs source use for Noether Paper 37, `Normalbasis bei Körpern ohne höhere Verzweigung`, in this tranche. It distinguishes original print, later German transcription, secondary reprint/OCR, and inherited Chinese evidence. It is an internal custody record, not external, publisher, source-owner, or community certification.

## Controlling German authority and exact boundary

The controlling editable German authority for this tranche is the sealed P31 cumulative TeX:

`evidence://local-workspace/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP/1/01_current/cum_de_Local_20260718_P31.tex`

SHA-256: `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F`.

The exact ordinary section-to-section interval is zero-based half-open bytes `[1649789,1672136)`, 22,347 bytes, from `\section*{37.` to immediately before `\section*{38.`. Its exact-CRLF SHA-256 is `AF2993A83530352893CABA50D196BDE9A17965C0E531297CA1A9E5AEB2D1B00A`, preserved as:

`source/Noether_Paper37_German_P31_section_interval_exact_CRLF.tex`

That interval carries 68 bytes of Paper-38 setup at its end: `\clearpage` and two footnote resets. The logical Paper-37 article therefore stops at byte `1672068` and is zero-based half-open bytes `[1649789,1672068)`, 22,279 bytes. Its exact-CRLF SHA-256 is `AF3B34ACF4FF8D91850AC56C4F86447ABC61E6641FF9795BEFBFDA004788585D`, preserved as:

`source/Noether_Paper37_German_P31_logical_article_exact_CRLF.tex`

The LF-normalized logical article is 22,092 bytes, SHA-256 `68C72173E0C060BC68CB3651AF078ACE82B4D5806C8A41584632AA2BB4A9B27B`, preserved as:

`source/Noether_Paper37_German_P31_logical_article_LF.tex`

Translation, formula parity, and standalone builds must use the logical article, with the standalone wrapper supplying the preceding Paper-37 footnote reset. The wider interval remains immutable boundary evidence and must not cause Paper-38 setup to enter the translation.

The machine-readable custody record is `SOURCE_CUSTODY.json`, SHA-256 `D692352468525BEDFD31FEA87BF0A5CEDA3C3ECB089D1B549CC9D89B2D578EE8`; its sealed whole-file, interval, logical-article, and LF-normalized assertions all pass.

## Live-head survival and pointer debt

A fresh source-use recheck found the same exact 22,347-byte Paper-37 interval, SHA-256 `AF2993A83530352893CABA50D196BDE9A17965C0E531297CA1A9E5AEB2D1B00A`, in all of the following:

| role | exact TeX path | whole-file SHA-256 | interval start byte |
|---|---|---|---:|
| sealed tranche authority | `evidence://local-workspace/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP/1/01_current/cum_de_Local_20260718_P31.tex` | `A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F` | 1,649,789 |
| manifested P30-reconciled comparison head | `evidence://local-workspace/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_LocalCodex_20260718_P30EvidenceReconciled_P31Closed_COMPLETE/Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP/1/01_current/cum_de_CURRENT_P30EvidenceReconciled_after_P31.tex` | `C243961810AD2EE10E866007620BBCDAFE2EF5305A1CAD040B5EA7E6ADDC2C39` | 1,649,796 |
| current coordination-pointer/Paper-4 head | `evidence://local-workspace/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_LocalCodex_20260718_P04p133_Eq28_SourceFix/1/01_current/cum_de_Local_20260718_P04p133_Eq28_SourceFix.tex` | `5D159B7457F2ACBAD583C82D391476659101F9519E7A4B45C97D4BD8A48C7AFD` | 1,650,254 |

The current coordination pointer is:

`evidence://local-workspace/Codex/2026-06-01/we-are-currently-doing-a-massive/Noether_Coordination_Current_20260718/CURRENT_HEAD_POINTER.md`

At this recheck its SHA-256 is `B86609853235EBB786C3CCBBE5AC5FB7DFB6A913404260E5A19F32107CB80B8F` and it names the `5D159...C7AFD` head. The claim-time pointer previously named whole-file hash `BDDEE79A2B47F7D0329671AA8FC7241B2B2167B099AF4CED581F0B2505895A8F`; that prior state also carried the identical Paper-37 interval. Whole-file head changes outside Paper 37 do not promote a different Paper-37 authority inside this tranche: sealed P31 remains the citation, and newer heads are unit-survival witnesses unless the lane is explicitly rerouted.

The separate shared directory

`evidence://local-workspace/interlanguage/03_projects/noether/00_current_german_authority`

still exposes R821-labelled artifacts. Its visible cumulative TeX `Noether_German_Cumulative_v26_R821integrated_20260716.tex` has SHA-256 `84FF0149472DB59D34BFFFD8FF6A4D4D227A6A3D83139E7F9F9067C2D33E643C`. This directory is stale and prohibited as current authority. Pointer-update debt remains with the Noether owner: refresh the shared pointer and supersession record. Until that happens, every bounded unit must cite the exact sealed P31 path/hash and recheck the live head separately.

## Primary printed authority: six original GDZ leaves

The primary authority for what the 1932 JRAM printing visibly contains is the six full-resolution GDZ IIIF leaf set in:

`evidence://local-workspace/Papors/Chatnotes/CHat translates and clean/Noether Multilingual/Noether_LocalCodex_after_WebR272_P37_p147_152_GDZ600_SourceAudit_20260629/02_source_pages_p147_152_GDZ600`

The enclosing audit ZIP is `Noether_LocalCodex_after_WebR272_P37_p147_152_GDZ600_SourceAudit_20260629.zip`, SHA-256 `F9ECF6C68E9C02DD0B0FB659BC03C8CC920C4C9B3EC088F26C8ABD78FEAFEE01`.

| printed JRAM page | GDZ canvas | original leaf file | dimensions | SHA-256 |
|---:|---:|---|---:|---|
| 147 | `00000152` | `P37_GDZ_JRAM167_canvas00000152_printed_p147_fullres.jpg` | 3800×5789 | `37E0B6700603821D39F106769F8CE9AC29E3C4B6F1F664505B05B46B4ECDAE85` |
| 148 | `00000153` | `P37_GDZ_JRAM167_canvas00000153_printed_p148_fullres.jpg` | 3792×5790 | `7C4CB39719CF8F9625ED5DC3DFF6BE908D10E89893FEAA142EBB62ED3B8F9DBE` |
| 149 | `00000154` | `P37_GDZ_JRAM167_canvas00000154_printed_p149_fullres.jpg` | 3800×5789 | `3E37D78ED96F3588D997FC471F921F724946A1959CBFAE9C8EDD62B879FB06C1` |
| 150 | `00000155` | `P37_GDZ_JRAM167_canvas00000155_printed_p150_fullres.jpg` | 3792×5790 | `85FC3BA0A9B964F6E5EF8CADF4D407A53488902E3558EC453D385E5447BA3A91` |
| 151 | `00000156` | `P37_GDZ_JRAM167_canvas00000156_printed_p151_fullres.jpg` | 3800×5789 | `6CE8C3C2B7C6043695AC613BE134A3DB00C968163BA4EF7599FBCD4AEC82E256` |
| 152 | `00000157` | `P37_GDZ_JRAM167_canvas00000157_printed_p152_fullres.jpg` | 3792×5790 | `B07BC32E4ED9E63668860EBDA7954C708EDBDD506894A6A475680532B028D528` |

Durable audit controls in that package are:

- `04_provenance/P37_GDZ_JRAM167_canvas_image_map.csv`, SHA-256 `AD5DA771B491333E2894949E140BB8EA0A14724C11D4A47BAD0F1908FF9D70FD`;
- `03_audit_ledgers/P37_page_dispositions_p147_152_20260629.csv`, SHA-256 `F8CDF58AA2FEBD576C02C286777A51888AEDF1221A1E1F6F2B840A79B9DD231F`;
- `03_audit_ledgers/P37_confirmed_source_fixes_20260629.csv`, SHA-256 `5DC076D13DCB963429DB5ABE609BBFE50D9DE56F05EFD4466A1FB0C570F4877C`.

The later p.150 index correction is recorded in Web R276 at:

`evidence://local-workspace/Papors/Chatnotes/CHat translates and clean/Noether Multilingual/Noether_WEB_DOWNLOADS_LAST_14_DAYS_FULL_AUDIT_20260703/01_extracted_unique_zips/0138_R276_F850FDA55C63_Noether_R276_Complete_P13P37P38_SourceFix_20260630/Noether_R276_complete/1/03_audit/confirmed_fixes_R276.csv`

SHA-256 `496879689F46487824EE0D7911850541E43EF6C77DE232E072473826DFB9CFAE`, row `R276-F007`. The decisive p.150 crop has SHA-256 `8FEBDDE386B784861C91E26522E5233059BC363E880E395CCC43DB813DBD6A64`.

All six original leaves were individually inspected. They are complete, upright, sharp, and legible, with negligible skew and only minor scan specks. This bounded internal visual check found no additional defect in Noether's original printed mathematical text; that negative finding is not proof of global absence and is not external validation.

## Secondary collected-volume/reprint witness

The following six-page PDF is a secondary collected-volume/reprint witness, not the exact original JRAM leaf set:

`evidence://local-workspace/Papors/modern-latex-manuscripts-github/sources/noether/final-numbered-papers-audit-with-table-restoration/source_paper_slices/Noether_Paper37_SOURCE_SCAN_pages638-643_Normalbasis_bei_K_rpern_ohne_h_here_Verzweigung.pdf`

SHA-256 `3824959FA3FFA8D325F44A9EE9EE66C2DA383B9CD28649A752A38AF4F532EEE2`; 401,260 bytes; six PDF pages. Its map is:

- PDF page 1 / source-master page 638 / reprint footer 624 / original printed page 147;
- PDF pages 2–6 continue one-to-one through source-master page 643 / reprint footer 629 / original printed page 152.

Page 1 adds the collected-volume number `37.` and journal citation and omits the original printed author line. The PDF embeds approximately 360-ppi bilevel text/masks over a 120-ppi background; its OCR text layer contains unsafe German, mathematical, Greek, and Fraktur recognitions. It may be used as a locator, secondary image witness, and ancestry control, but never to override the six GDZ originals or sealed P31. The source-master coverage row is in `SOURCE_PAGE_COVERAGE_NUMBERED_PAPERS.csv`, SHA-256 `3A15AC585222D65C922B6A02E7F08DE39344FB251264A2778E1FAB5141CFD8D9`.

## Defect classes and cross-language routing

### Original print

No defect in Noether's original 1932 print was confirmed in this bounded six-leaf inspection. In particular, the original visibly prints the centered author line on p.147, `v_1,\ldots,v_t` on p.150, and `[vgl. 2a)]` on p.151.

### Later German transcriptions

Older German transcriptions omitted the p.147 author line and p.151 cross-reference and misread p.150 `v_t` as `v_l`. The older R124+ source-fidelity witness, SHA-256 `BADEC053CB8BA5361437CCED8269333F213097CDD58322034C73A07450EFD7F2`, retains those three stale defects. An earlier German cumulative was also an abridged recasting; the broader restoration of its opening, notes, Deuring example, sections, displays, and receipt line is recorded in `AUDIT_RA08.md`, SHA-256 `3EE257DDC97B204F084BBD7DE1FF3F82D5F48825AA2290211E11368FC6CBCD88`. Sealed P31 carries the three directly checked printed forms, so this tranche does not edit German authority.

The exact German-transcription evidence and the broader restoration record were routed to the existing task `4 -nterslav`, thread `019ea764-a4a8-7ca1-bdfc-3d88b6085213`. Recipient-side decision `SLISV-20260718-008`, recorded at 2026-07-18T20:47:09+02:00, now provides file-backed incorporation into the four active Latin Interslavic, Cyrillic Interslavic, Russian, and Ukrainian Paper-37 bodies. Its confirmed-repair ledger, QA note, and negative-control ledger are respectively `PAPER37_CONFIRMED_REPAIRS_20260718.csv` SHA-256 `91D9FD0A7990450743C788AFDB08C1225F749B41A37CCCF77B2E9A556772BCC2`, `PAPER37_SOURCE_REPAIR_AND_QA_20260718.md` SHA-256 `78E7A13EE862AA9322043E6AD86061C271B781AEC476F0BF8FDC095E48B822CF`, and `PAPER37_NEGATIVE_CONTROLS_AND_DEDUP_20260718.csv` SHA-256 `DB19D7817D1A6C00DCF2D114CD32F5277CEDBCDB83B0BC17A3D00FBDBF346B78`, under `03_projects/language_management/slavic_interslavic/Noether_Paper37_Slavic_SourceRepair_20260718_COMPLETE/05_audit`. The recipient reports exact one-occurrence repairs, two builds per body, and inspection of twenty rendered pages. This closes message-only routing uncertainty at the downstream-artifact level; it is not publisher, German-source-owner, external, community, or human-language certification.

### Inherited Chinese witness

The inherited Chinese cumulative is:

`evidence://local-workspace/interlanguage/03_projects/language_management/cjk/01_recovered_witnesses/noether_cjk_chinese_japanese_cumulative_20260702/translations/non_slavic/simplified_chinese/cumulative/source_fidelity/v001/Noether_SimplifiedChinese_Cumulative_SourceFidelity_v001.tex`

Whole-file SHA-256 `C2936EFAC3C22FBEBD3E5F418902A0A4CA3CFFD953DC3ADC827432D7529DF3F9`. Its frozen Paper-37 records are:

- declared block: 19,515 bytes, SHA-256 `2B716D1B1D002998CD0FCBADAC3EECC90D5D3E8E1B1DFE2D90D6D3A7895B26B7`;
- historical BEGIN-to-before-END interval: bytes `[1421101,1440452)`, 19,351 bytes, SHA-256 `AD14E41B6B75829D20540A9C7654ABC2BEC157123555A08DB29158FF73EAF073`;
- logical article: 18,689 bytes, SHA-256 `1312DD725554A57A3A52FE780E924A5F7305C4E61E6418E393374B4D9EA1924B`;
- LF-normalized logical article: 18,499 bytes, SHA-256 `50094AA7F4A8153E613496E4F2F43B6E69B7B512FD689018459BAF366736C1D1`.

This Chinese material is translation and adverse-evidence witness only. It inherits the three older German defects and also introduces distinct Chinese/math transcription defects, including changing four Deuring products into quotients, changing lower-case base order `\frako` to capital `\frakO`, changing ordinary `_P` extension-field subscripts to prime-ideal forms, and adding or retaining source-divergent indices. It cannot establish German wording, printed mathematics, current source synchronization, native Chinese quality, Singapore usage, or any Hant localization.

## Use precedence

1. Use the six GDZ original leaves for claims about visible original-print glyphs, hierarchy, formulae, notes, and pagination.
2. Use sealed P31 as the controlling editable German transcription for this tranche, checked against those leaves.
3. Use later whole-file heads only to establish Paper-37 byte survival; do not silently promote them within this sealed-P31-keyed tranche.
4. Use the collected-volume PDF only as a secondary reprint/locator and treat its OCR as unaudited witness text.
5. Use inherited Chinese only as translation/adverse evidence to be reconciled, never as source authority.
6. Reopen custody, parity, build, and render checks if the sealed authority, live Paper-37 interval, logical boundary, printed-leaf hashes, or target-language source changes.
