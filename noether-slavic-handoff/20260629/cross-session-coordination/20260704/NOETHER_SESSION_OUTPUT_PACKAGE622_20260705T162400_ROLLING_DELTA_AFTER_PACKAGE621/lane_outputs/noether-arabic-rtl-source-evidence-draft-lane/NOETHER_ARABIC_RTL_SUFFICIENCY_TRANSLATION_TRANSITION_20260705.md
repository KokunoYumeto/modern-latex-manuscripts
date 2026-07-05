# Noether Arabic RTL Sufficiency Translation Transition

Created: 2026-07-05.

Status: draft, non-canonical, not native reviewed, not approved, not accepted terminology, not license-cleared, not a reviewer packet, not a completion claim, and not a Git/package publication action.

## Instruction Basis

This addendum applies the GitHub-visible source-canon sufficiency transition rule pushed on branch `codex/noether-pc-20260629` at commit `b99286628344251e860fe889e44cc54c8ebd6f87`.

Files checked:

- `AGENTS.md`
- `.github/copilot-instructions.md`
- `noether-slavic-handoff/20260629/cross-session-coordination/20260704/NOETHER_SOURCE_CANON_SUFFICIENCY_TRANSLATION_TRANSITION_20260705.md`
- Parent ledger Loop Check 94 in `NOETHER_INTERLANGUAGE_TRANSLATION_CONSOLIDATION_LEDGER_20260704.md`
- Source-canon steering record and B3 steward log
- Current Arabic source-canon rollup through `AR-CURRENT-034`

Source canon remains first. The new rule says a lane must not stay source-only once it has sufficient baseline witnesses for the offered language/topic scope. For Arabic, the six active Session C rows now have adequate PDF/HTML/raw-text/official-course/community fallback witnesses for draft review work, while direct Arabic TeX/source-package and specialist invariant-theory gaps remain open.

## Covered Rows

| Queue row | Covered status | Draft rendering | Source-canon basis | Draft artifacts |
| --- | --- | --- | --- | --- |
| `term-ar-0001` algebra | covered for scoped draft | `الجبر`; compound/object `جبر`; plural `جبور` flagged | normalized table, abstract-algebra/module probe, HIAST algebra shelf, Hindawi/Safahat and wiki fallbacks | `AR-SLICE-001`, `AR-SLICE-002`, `AR-SLICE-005`, `AR-SLICE-008` |
| `term-ar-0002` field | covered for scoped draft | `حقل`; `الحقل`; `حقل الدوال الكسرية` | ring/field curriculum, broad algebra, wiki/raw text, HIAST evidence | `AR-SLICE-001`, `AR-SLICE-002`, `AR-SLICE-003`, `AR-SLICE-006`, `AR-SLICE-007`, `AR-SLICE-008` |
| `term-ar-0006` ring | covered for scoped draft | `حلقة`; `حلقات`; `نظرية الحلقات`; `نطاق حلقي` flagged | official PDF probe, abstract algebra, Damascus specialist ring, ring-homomorphism curriculum | `AR-SLICE-001` through `AR-SLICE-008` where touched |
| `term-ar-0003` Artinian | covered for draft/manual review | `آرتيني`; `حلقة آرتينية`; corpus literal `الشرط الأدنى` / `شرط السلسلة التنازلية` | Damascus specialist ring, Fezzan adjacent matrix/ring, SyriaMath Noetherian/Artinian modules, KSU metadata caveat | `AR-SLICE-004` |
| `term-ar-0004` homomorphism | covered for draft/manual review | `تشاكل`; `تشاكل حلقي`; `صورة تشاكلية زمريّة` | module/homomorphism probes, direct homomorphism/isomorphism probe, official curriculum textchecks | `AR-SLICE-004`, `AR-SLICE-006`, `AR-SLICE-008` |
| `term-ar-0005` isomorphism | covered for draft/manual review | `تماثل`; `متماثل`; `التطبيق التماثلي`; `تماثل حلقي` | direct homomorphism/isomorphism probe, ring-isomorphism curriculum, Milne/wiki fallbacks | `AR-SLICE-003`, `AR-SLICE-005`, `AR-SLICE-006`, `AR-SLICE-007`, `AR-SLICE-008` |

The existing draft corpus artifacts remain the current draft translation layer:

- `NOETHER_ARABIC_RTL_DRAFT_CORPUS_SIDECAR_20260704.md`
- `NOETHER_ARABIC_RTL_CORPUS_TRANSLATION_SLICES_20260704.md`

This addendum refreshes their source-canon basis under the 2026-07-05 rule. It does not canonicalize them.

## Row Notes

### Algebra

Draft target: `الجبر` for the discipline and title-level use; `جبر` in compounds when Arabic grammar calls for an indefinite/object form. `الجبر التبديلي` remains the draft for `kommutative Algebra`.

Alternatives and flags: `الجبر التجريدي` for abstract algebra contexts, `بنية جبرية` for algebraic structure, and `جبور` for plural `Algebren` remain review-sensitive.

Formula-neighboring usage: keep math tokens separated in forms such as `جبر \(A\)` and `\(A\)-جبر`; the hyphen and Latin-letter ordering need PDF inspection.

Semi-constructed scaffold: `Algebra (discipline) -> الجبر`; `algebra (structure) -> جبر`; `commutative algebra -> الجبر التبديلي`; `algebras -> جبور [review]`.

### Field

Draft target: `حقل`; with article `الحقل`. `Funktionenkörper` remains `حقل الدوال الكسرية` in the current draft, with `الدوال الناطقة` kept as a review alternative.

Alternatives and flags: `مجال` is not preferred for algebraic `Körper` in this Noether lane because it risks non-field readings.

Formula-neighboring usage: examples such as `\(\Omega\) حقل عددي`, `حقل \(K\)`, and `حقل الدوال في \(n\) من المتغيرات` require visual RTL/math QA.

Semi-constructed scaffold: `Körper -> حقل`; `Funktionenkörper -> حقل دوال / حقل الدوال الكسرية`; `Zahlkörper -> حقل عددي`.

### Ring

Draft target: `حلقة`; plural `حلقات`; ring theory `نظرية الحلقات`. `Ringbereich` remains `نطاق حلقي` only as a flagged draft.

Alternatives and flags: `مجال حلقي`, `حلقة`, and `نطاق تكاملي` remain context/reviewer alternatives for `Ringbereich`.

Formula-neighboring usage: `\(R\)-حلقة`, `لتكن \(R\) حلقة`, and `\(o\) حلقة ذات عنصر واحدي` need bidi and hyphen inspection in PDF.

Semi-constructed scaffold: `Ring -> حلقة`; `ring theory -> نظرية الحلقات`; `Ringbereich -> نطاق حلقي [draft flag]`.

### Artinian

Draft target: `آرتيني`; feminine phrase `حلقة آرتينية`. In corpus prose where the German anchor says `Minimalbedingung`, keep the literal/explanatory Arabic `الشرط الأدنى` or `شرط السلسلة التنازلية`; do not silently modernize Noether's wording to `آرتيني`.

Alternatives and flags: `أرتيني`, `ارتيني`, `شرط السلسلة النازلة`, and `الشرط الأدنى` are search/register variants. KSU remains metadata-only because body extraction failed; AlFreed remains rights-blocked metadata only.

Formula-neighboring usage: descending-chain displays such as `\(\mA_1\supset\mA_2\supset\mA_3\cdots\)` should remain math mode with Arabic explanatory prose outside.

Semi-constructed scaffold: `Artinian -> آرتيني [modern/reviewer apparatus]`; `Minimalbedingung -> الشرط الأدنى`; `descending-chain condition -> شرط السلسلة التنازلية / النازلة`.

### Homomorphism

Draft target: `تشاكل`; ring-specific `تشاكل حلقي`; group-homomorphic image `صورة تشاكلية زمريّة`.

Alternatives and flags: `تجانس`, `مورفيزم`, and `هومومورفيزم` are evidence variants, not preferred draft renderings.

Formula-neighboring usage: `تشاكل \(R\to S\)`, `الصورة التشاكلية لـ \(\Im^*\)`, and arrow displays require visual order checks.

Semi-constructed scaffold: `Homomorphism -> تشاكل`; `ring homomorphism -> تشاكل حلقي`; `homomorphic image -> صورة تشاكلية`.

### Isomorphism

Draft target: `تماثل`; adjective `متماثل`; `isomorphic mapping` as `التطبيق التماثلي`; ring isomorphism `تماثل حلقي`.

Alternatives and flags: `تشاكل تقابلي` may be needed where bijectivity/invertibility must be explicit; `إيزومورفيزم` remains an evidence variant only.

Formula-neighboring usage: `\(\Afield\simeq\Bfield\)`, `التطبيق \(f(z)\)`, and `حلقة التماثلات الذاتية` need math isolation and PDF QA.

Semi-constructed scaffold: `Isomorphism -> تماثل`; `isomorphic -> متماثل`; `automorphism ring -> حلقة التماثلات الذاتية`; `isomorphic mapping -> التطبيق التماثلي`.

## Still Acquisition-Only

These are not active Session C Arabic rows and are not translated here:

| Gap | Status |
| --- | --- |
| Direct Arabic TeX/LaTeX/arXiv/e-print/source package for the treated algebra topics | open; repeated bounded probes found zero admitted mathematical source packages |
| Direct Arabic specialist invariant-theory source body/source package | open; Shamra/Marefa/secondary/English anchors remain weak or non-authorizing |
| Arabic covariant / binary forms source | open; route novel bridge/interlanguage material to Session D when it does not match the six-row Arabic scope |
| License/reuse closure | open; access and page-level signals are recorded, but no blanket license clearance is claimed |
| RTL TeX/PDF visual QA | open; all formula-neighboring Arabic needs project-stack rendering inspection before reviewer-packet use |

## Boundary

This addendum enables scoped draft work for the six covered rows under the source-canon sufficiency rule. It does not approve terms, claim native review, claim canonical Arabic translation, clear licenses, populate reviewer packets, promote gates, package artifacts, or push Git.
