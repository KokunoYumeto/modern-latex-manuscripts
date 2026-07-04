# Noether Arabic RTL Draft Corpus Sidecar

Draft / non-canonical / not native reviewed. Prepared for the Arabic RTL lane on 2026-07-04.

This sidecar covers the six active Arabic rows from the Session C non-Slavic queue: algebra, field, Artinian, homomorphism, isomorphism, and ring. It records source-evidence status, draft Arabic renderings, context/manual-review notes, and RTL/TeX risks. It does not approve terms, promote gates, populate reviewer packets, overwrite ledgers, or claim native review.

## Inputs Inspected

- Recovery report: `C:\Users\memo_\Documents\Codex\2026-07-04\i-want-information-on-the-any-2\outputs\NOETHER_TRANSLATION_INTERLANGUAGE_RECOVERY_REPORT_20260704.md`
- Queue root: `C:\Users\memo_\Documents\Codex\2026-06-29\updatede-goal-text-maintain-the-noether-2\work\github-checkouts\modern-latex-manuscripts-noether-pc-nocone-20260702\noether-slavic-handoff\20260629`
- Canonical local tree: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical`
- Current best on-disk German source: `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\tmp\zenodo_20836874_inspect\localcodex\Noether_R124plus_LocalCodex_PostR124_Consolidated_WebDrop_20260624\tex\cum_de_R124plus_localcodex_current_candidate_20260624.tex`
- Main queue files: `PAGE_CONTEXT_NOTE_WORKLIST_20260629.json`, `MANUAL_SOURCE_REVIEW_RESOLUTION_DECISION_QUEUE_20260630.json`, `LOCAL_SOURCE_WITNESS_SHORTLIST_20260630.json`
- Historical/source-evidence support inspected as branch evidence only, including `PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json` and older batch inspection payloads.

## Source Evidence Boundary

Direct Arabic mathematical sources were preferred. Controlled Arabic sources were absorbed only where they directly supported one of the six Arabic rows. Persianate and broader Arabic-script neighbor material was not used to authorize Arabic terms; it remains comparator/interlanguage material and should be routed separately to Session D if a novel bridge is needed.

Local Arabic witness shelves used:

- `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\sources\non_slavic_reference_corpus\20260628T210209Z_persian_arabic_native_math\arabic`
- `C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\sources\non_slavic_reference_corpus\20260628T232000Z_controlled_arabic_math_register`

Supplemental web evidence used only where local/manual extraction was insufficient:

- AIU / Damascus University journal page for Prufer and arithmetical rings, with Arabic use of the Artinian ring form: `https://www.aiu.edu.sy/ar/publication/prufer-ring-and-arithmetical-ring`
- Fezzan University PDF article using Arabic Artinian-ring terminology and descending-chain characterization: `https://fezzanu.edu.ly/fusj/index.php/FUAJ/article/download/343/189`
- Internet Archive full-text mathematics dictionary used as lexicon support, not as primary mathematical corpus evidence: `https://archive.org/stream/7_20240106_20240106_1905/%D9%82%D8%A7%D9%85%D9%88%D8%B3%20%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6%D9%8A%D8%A7%D8%AA%20%D8%A7%D8%B7%D9%84%D8%B3%20%D8%A7%D9%86%D9%83%D9%84%D9%8A%D8%B2%D9%8A%20%D8%B9%D8%B1%D8%A8%D9%8A_djvu.txt`

## Draft Row Outcomes

| Row | Queue class | Draft Arabic rendering | Evidence status | Packet decision |
| --- | --- | --- | --- | --- |
| `term-ar-0001` algebra | ready context-note | `الجبر`; in object contexts `جبر` | High. Exact local extraction support and multiple direct Arabic witnesses. | Draft sidecar context note only; no packet population. |
| `term-ar-0002` field | ready context-note | `حقل`; with article `الحقل` | High. Direct Arabic course/spec evidence supports algebraic register. | Draft sidecar context note only; no packet population. |
| `term-ar-0003` Artinian | manual/source-review | `آرتيني`; phrase `حلقة آرتينية` | Medium. Local extraction conflict plus direct seed/web support; needs native/domain review. | Manual note drafted; remains blocked from packet population. |
| `term-ar-0004` homomorphism | manual/source-review | `تشاكل`; context-specific `تشاكل حلقي` | Medium-high. Strong source support for `تشاكل`, but variants require review. | Manual note drafted; remains blocked from packet population. |
| `term-ar-0005` isomorphism | manual/source-review | `تماثل`; adjective `متماثل` | Medium-high. Strong source support, but register variants require review. | Manual note drafted; remains blocked from packet population. |
| `term-ar-0006` ring | ready context-note | `حلقة`; plural `حلقات` | High. Exact local extraction support and multiple direct Arabic witnesses. | Draft sidecar context note only; no packet population. |

## Row Notes

### `term-ar-0001` Algebra

Draft target rendering: `الجبر` for the mathematical field and title-level use; `جبر` without the article when used as a count/object noun in compounds.

German context anchors:

- `kommutativen Algebra` -> draft Arabic `الجبر التبديلي`
- Noether bibliography context `Hyperkomplexe Systeme in ihren Beziehungen zur kommutativen Algebra und zur Zahlentheorie` -> draft Arabic `النظم فوق المركبة في علاقاتها بالجبر التبديلي ونظرية الأعداد`

Evidence:

- Historical Arabic batch: 44 pages checked, 4 pages with exact occurrence, 5 exact hits.
- Direct Arabic witnesses include Mosul ring theory, Majmaah rings/fields course spec, Mustansiriyah ring theory course, Mustansiriyah mathematics program/course material, and local Syriamath algebraic-structures material.

Context note without source quote:

The Arabic evidence supports `الجبر` as the normal register for algebra in abstract algebra, ring theory, and program/course contexts. For Noether corpus contexts involving commutative algebra and hypercomplex systems, `الجبر التبديلي` is the best draft target. Definite article use should follow sentence grammar rather than be fixed in the glossary entry.

Reviewer question:

Confirm whether the target edition wants `الجبر التبديلي` consistently for `kommutative Algebra`, and whether title contexts should retain the article in all cases.

### `term-ar-0002` Field

Draft target rendering: `حقل`; with article `الحقل`. Avoid silently replacing it with `مجال` in algebraic-field contexts.

German context anchors:

- `Körper und Systeme rationaler Funktionen` -> draft Arabic `الحقول وأنظمة الدوال الكسرية`
- `Funktionenkörper` -> draft Arabic `حقل الدوال الكسرية`
- `Zahlkörper` -> draft Arabic `حقل عددي`

Evidence:

- Historical Arabic batch: 44 pages checked, 2 pages with exact occurrence, 4 exact hits.
- Direct Arabic witnesses include Majmaah rings/fields course spec, Mustansiriyah abstract algebra/program material, and local Syriamath algebraic-structures material.

Context note without source quote:

The direct Arabic algebra register supports `حقل` for German `Körper` in algebraic settings. `مجال` may appear in other Arabic mathematical or physical contexts, but it risks ambiguity here because Noether's `Körper` is the algebraic field concept.

Reviewer question:

Confirm whether `الدوال الكسرية` or `الدوال الناطقة` should be preferred for `rationale Funktionen` in this edition. The current draft uses `الدوال الكسرية`.

### `term-ar-0003` Artinian

Draft target rendering: `آرتيني`; phrase form `حلقة آرتينية`. Search/register variants to preserve in notes: `أرتيني`, `ارتيني`, `أرتينية`, `ارتينية`.

German context anchors:

- Noether baseline has relevant `Minimalbedingung` / descending-chain context for ideals, including right-ideal minimum-condition discussion. Draft Arabic: `شرط السلسلة التنازلية` or explanatory `الشرط الأدنى للمثاليات اليمنى`.
- For a ring satisfying the Artinian condition: draft Arabic `حلقة آرتينية`.

Evidence:

- Manual queue status: exact extraction row showed 4 pages checked and no exact occurrence; this remains an extraction/register mismatch.
- Arabic term-anchor seed evidence reports `آرتيني` occurrences in an Arabic Milne group-theory witness, despite the manual-row exact extraction miss.
- Supplemental Arabic web evidence supports the ring phrase forms `الحلقة الآرتينية`, `حلقة أرتينية`, and `حلقة ارتينية`; this supports the concept but does not remove the need for native/domain review.

Manual source-review note without source quote:

The best draft rendering is `آرتيني` with feminine agreement in `حلقة آرتينية`. The row should be treated as manually resolved to a draft only: the local exact-occurrence inspection and seed evidence disagree, likely because of OCR/extraction or spelling/hamza variation. No canonical approval should follow from this sidecar. A reviewer should verify both the preferred hamza spelling and the explanatory relation between Noether's `Minimalbedingung` contexts and the later Artinian terminology.

Extraction mismatch resolution:

Record as `rtl_register_or_extraction_variant_manual_review`: variant spellings and OCR text extraction likely hid exact hits. Keep all spelling variants available for future search, but use `آرتيني/آرتينية` as the draft normalized form.

Reviewer question:

Should the Arabic edition normalize to `آرتيني/آرتينية`, or preserve the simpler source spellings `أرتيني` / `ارتيني` when matching specific source tradition?

### `term-ar-0004` Homomorphism

Draft target rendering: `تشاكل`; context-specific forms include `تشاكل حلقي`, `تشاكل زمري`, and `تشاكل جبور لي`.

German context anchors:

- `Homomorphie` -> draft Arabic `التشاكل`
- `homomorphes Bild` / group-homomorphic image contexts -> draft Arabic `صورة تشاكلية` or, when group-specific, `صورة تشاكلية زمريّة`

Evidence:

- Manual queue status: exact extraction row showed 12 pages checked and no exact occurrence; this remains a register mismatch.
- Historical Arabic seed evidence included `تجانس` in Mustansiriyah/J. Milne witnesses, which is a source variant.
- Local Syriamath algebraic-structures evidence directly supports `تشاكل حلقي`.
- Controlled Arabic Lie and group-theory materials support `تشاكل` and specialized compounds, while also showing transliterated `هومومورفيزم` in some papers.

Manual source-review note without source quote:

Use `تشاكل` as the draft Arabic mathematical register for homomorphism in algebraic contexts. Preserve `تجانس` and `هومومورفيزم` as observed evidence variants, not as the preferred draft form. For formula-neighboring ring contexts, prefer the explicit compound `تشاكل حلقي` so that the structural domain is visible.

Extraction mismatch resolution:

Record as `rtl_register_or_extraction_variant_manual_review`: exact matching likely missed source-supported synonyms and compounds. Do not promote until an Arabic mathematical reviewer confirms whether Noether corpus homomorphism contexts should use `تشاكل`, `تجانس`, or a compound form by structure.

Reviewer question:

For this edition, should `Homomorphie` be normalized as `تشاكل`, or should older/source-specific `تجانس` be retained in some contexts?

### `term-ar-0005` Isomorphism

Draft target rendering: `تماثل`; adjective `متماثل`. When the mathematical condition must be explicit, use `تشاكل تقابلي` or an explanatory phrase only with reviewer approval.

German context anchors:

- `isomorphe Abbildung` -> draft Arabic `التطبيق التماثلي`
- Bibliography context `Die Funktionalgleichungen der isomorphen Abbildung` -> draft Arabic `المعادلات الدالية للتطبيق التماثلي`
- `isomorphe Darstellung` -> draft Arabic `تمثيل متماثل`

Evidence:

- Manual queue status: exact extraction row showed 20 pages checked and no exact occurrence; this remains an extraction/register mismatch.
- Arabic seed evidence reports broad `تماثل` support in the Arabic Milne witness.
- Local Syriamath algebraic-structures evidence supports `تماثل حلقي` / isomorphism contexts.
- Controlled Arabic sources support `تماثل`, while one Lie-algebra source also shows transliterated `إيزومورفيزم`; the transliteration is evidence of use, not preferred in this draft.

Manual source-review note without source quote:

Use `تماثل` as the draft target for isomorphism and `متماثل` for isomorphic. This fits Arabic algebraic usage better than the transliteration `إيزومورفيزم` for a literary/mathematical edition. Where a sentence contrasts homomorphism and isomorphism, ensure the Arabic makes bijectivity/invertibility clear, either through context or an approved compound such as `تشاكل تقابلي`.

Extraction mismatch resolution:

Record as `rtl_register_or_extraction_variant_manual_review`: exact matching missed source-supported synonyms and compounds. Keep the row manual until native Arabic mathematical review verifies `تماثل` versus `تشاكل تقابلي` in each Noether context.

Reviewer question:

Should `isomorphe Abbildung` be rendered as `التطبيق التماثلي`, `التطبيق المتماثل`, or a more explicit `التطبيق التشاكلي التقابلي` in formal theorem statements?

### `term-ar-0006` Ring

Draft target rendering: `حلقة`; plural `حلقات`. Ring theory: `نظرية الحلقات`.

German context anchors:

- `Ringbereiche` -> draft Arabic `نطاقات حلقية` with review flag
- `Idealtheorie in Ringbereichen` -> draft Arabic `نظرية المثاليات في نطاقات حلقية`
- `Ringe ... Rechtsideale` -> draft Arabic `حلقات ... مثاليات يمنى`

Evidence:

- Historical Arabic batch: 35 pages checked, 3 pages with exact occurrence, 10 exact hits.
- Direct Arabic witnesses include Majmaah rings/fields course spec, Mustansiriyah ring theory course, Mustansiriyah program/course material, Mosul ring theory, and local Syriamath algebraic-structures material.

Context note without source quote:

The Arabic evidence strongly supports `حلقة` for the algebraic ring concept and `نظرية الحلقات` for ring theory. For German `Ringbereich`, however, the draft `نطاق حلقي`/`نطاقات حلقية` should be reviewed because `Bereich` may signal a domain/ring-domain nuance in Noether's German rather than the generic ring word alone.

Reviewer question:

Confirm whether `Ringbereich` should be rendered as `نطاق حلقي`, `مجال حلقي`, `حلقة`, or a context-sensitive phrase.

## RTL And TeX Notes

- Typesetting should use XeLaTeX or LuaLaTeX with an Arabic-capable stack such as `polyglossia` plus `bidi`, or an equivalent project-approved RTL setup.
- Wrap Arabic prose in an Arabic direction context such as `\textarabic{...}` or `\begin{Arabic}...\end{Arabic}`. Keep mathematical formulae in normal math mode.
- Keep spaces around inline formulae: draft `لتكن \(R\) حلقة` rather than attaching Latin/math tokens to Arabic words.
- Use Arabic punctuation in Arabic prose: comma `،` and semicolon `؛`. Latin punctuation is acceptable beside TeX formulae when needed, but it should be visually checked in PDF.
- Formula-neighboring compounds such as `تشاكل \(R \to S\)` and `\(R\)-حلقة` need PDF inspection because bidirectional ordering can shift hyphens and arrows.
- Avoid carrying Persian-specific forms into Arabic output. Persianate/Arabic-script neighbor material is not canonical evidence for this lane.
- OCR/source extraction notes: Arabic witness text may contain bidi marks, reversed Latin fragments, OCR substitutions, and line-order artifacts. Evidence here is term/register support, not a clean diplomatic transcription of the source.

## Draft Corpus Fragments

These are non-canonical draft fragments for corpus integration and reviewer orientation:

| German source/context | Draft Arabic |
| --- | --- |
| `Körper und Systeme rationaler Funktionen` | `الحقول وأنظمة الدوال الكسرية` |
| `Funktionenkörper` | `حقل الدوال الكسرية` |
| `Zahlkörper` | `حقل عددي` |
| `kommutative Algebra` | `الجبر التبديلي` |
| `Idealtheorie in Ringbereichen` | `نظرية المثاليات في نطاقات حلقية` |
| `Minimalbedingung für Rechtsideale` | `شرط السلسلة التنازلية للمثاليات اليمنى` |
| `Homomorphie` | `التشاكل` |
| `isomorphe Abbildung` | `التطبيق التماثلي` |
| `isomorphe Darstellung` | `تمثيل متماثل` |

## Gate And Review Status

- Ready rows `term-ar-0001`, `term-ar-0002`, and `term-ar-0006` now have draft context notes in this sidecar only.
- Manual rows `term-ar-0003`, `term-ar-0004`, and `term-ar-0005` now have draft manual-resolution notes in this sidecar only.
- All six rows remain `native_review: not_reviewed` and `canonical: not_approved`.
- No reviewer packets were populated or sent.
- No gate ledgers were overwritten or promoted.
- No Git push was performed.

