# Noether Arabic RTL Active Row Bucket Workup

Created: 2026-07-05.

Status: draft/non-canonical source-canon and translation-support workup. Not native reviewed, not accepted terminology, not canonical approval, not license clearance, not gate promotion, not reviewer-packet population, not completion, not a package, and not a Git push.

## Instruction Basis

Read again for this workup:

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `NOETHER_OPEN_MACHINE_GITHUB_COORDINATION_RULE_20260704.md`
- `NOETHER_OPEN_MACHINE_GITHUB_COORDINATION_RULE_20260704.json`
- `NOETHER_SOURCE_CANON_SUFFICIENCY_TRANSLATION_TRANSITION_20260705.md`

The controlling rule is source canon first, then scoped draft work for rows whose target-language baseline is sufficient. Generated Arabic drafts are not source canon.

## Bucket Result

The active-row scope remains exactly the six Arabic Session C rows recorded in `NOETHER_ARABIC_RTL_ACTIVE_ROW_SCOPE_RECHECK_20260704.json`.

| Queue row | Term | Bucket |
| --- | --- | --- |
| `term-ar-0001` | algebra | source-canon sufficient for scoped draft work |
| `term-ar-0002` | field | source-canon sufficient for scoped draft work |
| `term-ar-0006` | ring | source-canon sufficient for scoped draft work |
| `term-ar-0003` | Artinian | source-canon sufficient for scoped draft work, manual-review flag |
| `term-ar-0004` | homomorphism | source-canon sufficient for scoped draft work, manual-review flag |
| `term-ar-0005` | isomorphism | source-canon sufficient for scoped draft work, manual-review flag |

No active Arabic row is currently bucketed as source-canon insufficient. Non-active specialist/source-package gaps are kept as acquisition rows below.

## Covered Row Workup

### `term-ar-0001` Algebra

Source witnesses:

- HIAST/Mustansiriyah `الجبر 1 مبادئ الجبر المجرد`, URL `https://uomustansiriyah.edu.iq/media/attachments/192/192_2019_10_20%2108_53_36_PM.pdf`, local path `sources/non_slavic_reference_corpus/20260705T051200Z_arabic_abstract_algebra_module_probe/downloads/mustansiriyah_abstract_algebra_principles.pdf`, SHA-256 `FAA47DEBCB0157EBB28B4A0D0FAECDC7C52950802CE51C66A4F92DA2446F97E0`.
- Supporting source rows: `AR-CURRENT-024`, `AR-CURRENT-025`, `AR-CURRENT-027`, plus MediaWiki/Wikibooks fallback rows.

Access/license signal: in-PDF CC-BY-ND 4.0 signal; no blanket license clearance.

Draft rendering: `الجبر`; object/compound form `جبر`; plural structures `جبور` flagged.

Register alternatives: `الجبر التجريدي`, `بنية جبرية`; `جبور` needs native/domain review.

Formula note: `جبر \(A\)` and `\(A\)-جبر` need bidi/hyphen PDF inspection.

Scaffold: `Algebra (discipline) -> الجبر`; `algebra (structure) -> جبر`; `commutative algebra -> الجبر التبديلي`.

### `term-ar-0002` Field

Source witnesses:

- Majmaah MATH444 rings/fields course specification, URL `https://www.mu.edu.sa/sites/default/files/MATH444.pdf`, local path `sources/non_slavic_reference_corpus/20260705T132600Z_arabic_ring_homomorphism_curriculum_probe/downloads/mu_math444_course_spec.pdf`, SHA-256 `A201A42940790C88E1D817D9A717955AF97EA4C9D2AE7A7FC684A350CE06880B`.
- ENS Ouargla general algebra R211, URL `https://www.ens-ouargla.dz/wp-content/uploads/2023/10/%D8%A8.%D8%AC%D8%A8%D8%B1.%D8%B9%D8%A7%D9%85-%D8%B1211-1.pdf`, local path `sources/non_slavic_reference_corpus/20260705T132600Z_arabic_ring_homomorphism_curriculum_probe/downloads/ens_ouargla_general_algebra_r211.pdf`, SHA-256 `07A990B0210722A42CB9F47982C2FE48284A4AAE76787A55D96C6A66D56158E0`.

Access/license signal: official/public PDF endpoints; no reuse/license clearance.

Draft rendering: `حقل`; with article `الحقل`; function field `حقل الدوال الكسرية`.

Register alternatives: `مجال` is not preferred for algebraic field; `الدوال الناطقة` remains a review alternative to `الدوال الكسرية`.

Formula note: `\(\Omega\) حقل عددي`, `حقل \(K\)`, and `حقل الدوال في \(n\) من المتغيرات` need formula-neighboring RTL QA.

Scaffold: `Körper -> حقل`; `Funktionenkörper -> حقل الدوال الكسرية`; `Zahlkörper -> حقل عددي`.

### `term-ar-0006` Ring

Source witnesses:

- Majmaah MATH444 as above.
- University of Anbar Arabic mathematics program, local path `sources/non_slavic_reference_corpus/20260705T132600Z_arabic_ring_homomorphism_curriculum_probe/downloads/anbar_mathematics_arabic_program.pdf`, SHA-256 `7BF438273AB5D3A3AAC5A7C53F79DB0527D1AA7766A1EF0BF606E9733608EF55`.
- Damascus specialist ring/commutative-algebra probe `NOETHER_ARABIC_RTL_DAMASCUS_SPECIALIST_RING_MATRIX_SOURCE_PROBE_20260705.csv`, SHA-256 `8D871382B9DD9BE1C79BD5F307AC13321061DB2CB6BBA74881D499CCCB7C11DB`.

Access/license signal: official university/course/journal access signals; no blanket license clearance.

Draft rendering: `حلقة`; plural `حلقات`; ring theory `نظرية الحلقات`; `Ringbereich` draft `نطاق حلقي`.

Register alternatives: `مجال حلقي`, `حلقة`, `نطاق تكاملي`, depending on context and reviewer decision.

Formula note: `\(R\)-حلقة`, `لتكن \(R\) حلقة`, and `\(o\) حلقة ذات عنصر واحدي` need bidi/hyphen PDF inspection.

Scaffold: `Ring -> حلقة`; `ring theory -> نظرية الحلقات`; `Ringbereich -> نطاق حلقي [draft flag]`.

### `term-ar-0003` Artinian

Source witnesses:

- SyriaMath `المودولات النوثرية والآرتينية`, URL `https://www.syriamath.net/files/lectures/2017/11/1779942999.pdf`, local path `sources/non_slavic_reference_corpus/20260705T140400Z_arabic_artinian_noetherian_chain_probe/downloads/syriamath_structures3_noetherian_artinian_modules.pdf`, SHA-256 `D5800C180027034048F5B60FFE4BF2751CC042AC5883AE6616E77226E655F996`.
- KSU DSRS Artinian serial rings DOC metadata, URL `https://dsrs.ksu.edu.sa/sites/dsrs.ksu.edu.sa/files/imce_images/1430.doc`, local path `sources/non_slavic_reference_corpus/20260705T140400Z_arabic_artinian_noetherian_chain_probe/downloads/ksu_artinian_serial_rings_1430.doc`, SHA-256 `AE0F5E7C92E8CFFE44BB6AA8041AF96FA3DE0E35FC69A17DA97B803AEFB157DD`.
- Damascus duplicate/owner-lane specialist ring evidence, URL `https://journal.damascusuniversity.edu.sy/index.php/basj/ar/article/view/3694/1220`.

Access/license signal: SyriaMath public PDF access; KSU official DOC access but body extraction failed; no license clearance.

Draft rendering: `آرتيني`; `حلقة آرتينية`. In Noether corpus prose, keep `Minimalbedingung` as `الشرط الأدنى` or `شرط السلسلة التنازلية`.

Register alternatives: `أرتيني`, `ارتيني`, `شرط السلسلة النازلة`, `شرط السلسلة التنازلية`.

Formula note: descending chains such as `\(\mA_1\supset\mA_2\supset\mA_3\cdots\)` should remain math mode with Arabic explanation outside.

Scaffold: `Artinian -> آرتيني [modern apparatus]`; `Minimalbedingung -> الشرط الأدنى`; `descending-chain condition -> شرط السلسلة التنازلية / النازلة`.

### `term-ar-0004` Homomorphism

Source witnesses:

- Damascus module-representation PDF, URL `https://journal.damascusuniversity.edu.sy/index.php/basj/ar/article/view/4805/2152`, local path `sources/non_slavic_reference_corpus/20260705T113500Z_arabic_homomorphism_isomorphism_probe/downloads/damascus_module_representation_pdf.pdf`, SHA-256 `58C1254FC8F2F7D3C8C6018E2F889B444D631CE212DE371D9BB560DA9EC69B2D`.
- ENS Kouba `alg411.pdf`, URL `https://www.ens-kouba.dz/arabic/images/programs/math/4b%2B5/alg411.pdf`, local path `sources/non_slavic_reference_corpus/20260705T113500Z_arabic_homomorphism_isomorphism_probe/downloads/ens_kouba_alg411.pdf`, SHA-256 `97281366546BA5019A01B7212659AF3C0999BF55FB0629215076F9368768B29B`.
- SyriaMath ring-homomorphism lecture, URL `https://www.syriamath.net/files/lectures/2019/04/998822944.pdf`, SHA-256 `35519D9ABFBCF427125ECB8985F4832EDDB8F425A9F3022E78B26D9F7D9C9AB2`.

Access/license signal: official/institutional/weak-public PDF access signals; no blanket license clearance.

Draft rendering: `تشاكل`; `تشاكل حلقي`; `صورة تشاكلية زمريّة`.

Register alternatives: `تجانس`; `مورفيزم`; `هومومورفيزم`. These are evidence variants, not preferred draft forms.

Formula note: `تشاكل \(R\to S\)`, `الصورة التشاكلية لـ \(\Im^*\)`, and arrow displays need direction checks.

Scaffold: `Homomorphism -> تشاكل`; `ring homomorphism -> تشاكل حلقي`; `module homomorphism -> تشاكل مودولي`; `homomorphic image -> صورة تشاكلية`.

### `term-ar-0005` Isomorphism

Source witnesses:

- Damascus module-representation PDF as above.
- ENS Kouba `alg411.pdf` as above.
- University of Anbar Arabic mathematics program, URL `https://epscollege.uoanbar.edu.iq/catalog/%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6%D9%8A%D8%A7%D8%AA-%D8%B9%D8%B1%D8%A8%D9%8A%281%29.pdf`, local path `sources/non_slavic_reference_corpus/20260705T132600Z_arabic_ring_homomorphism_curriculum_probe/downloads/anbar_mathematics_arabic_program.pdf`, SHA-256 `7BF438273AB5D3A3AAC5A7C53F79DB0527D1AA7766A1EF0BF606E9733608EF55`.

Access/license signal: official/institutional PDF access signals; no blanket license clearance.

Draft rendering: `تماثل`; `متماثل`; `التطبيق التماثلي`; `تماثل حلقي`.

Register alternatives: `تشاكل تقابلي` may be needed where bijectivity/invertibility must be explicit; `إيزومورفيزم` remains a transliteration/evidence variant only.

Formula note: `\(\Afield\simeq\Bfield\)`, `التطبيق \(f(z)\)`, and `حلقة التماثلات الذاتية` need math isolation and PDF QA.

Scaffold: `Isomorphism -> تماثل`; `isomorphic -> متماثل`; `isomorphic mapping -> التطبيق التماثلي`; `automorphism ring -> حلقة التماثلات الذاتية`.

## Insufficient Active Rows

None under current evidence. If a new Arabic queue row appears, it must be classified before draft work begins.

## Non-Active Acquisition Gaps

These remain source-canon insufficient and are not active translation rows here:

- Direct Arabic TeX/LaTeX/arXiv/e-print/source packages for the treated algebra topics.
- Direct specialist Arabic invariant-theory source body/source package.
- Arabic covariant / binary-forms source evidence.
- License/reuse closure across the Arabic witness set.
- RTL TeX/PDF visual QA for formula-neighboring Arabic.

Do not translate or promote uncovered invariant/covariant/binary-form material from weak metadata, English anchors, neighboring-script sources, or interlanguage scaffolds.

## Existing Draft Support

The covered-row draft support lives in:

- `NOETHER_ARABIC_RTL_DRAFT_CORPUS_SIDECAR_20260704.md`
- `NOETHER_ARABIC_RTL_CORPUS_TRANSLATION_SLICES_20260704.md`
- `NOETHER_ARABIC_RTL_SUFFICIENCY_TRANSLATION_TRANSITION_20260705.md`

This workup adds an active-row bucket layer. It does not approve or canonicalize the drafts.
