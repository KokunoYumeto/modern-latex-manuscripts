# Persian-family and Arabic glossary/rationale seed - 2026-06-29

This is a terminology seed for Iranian Persian/Farsi (`fa_IR`), Dari/Afghanistan Persian (`prs_AF`), and Arabic (`ar`). It is derived from `PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json`, which records only term counts and page anchors from local PDF text extraction. No source passages or PDFs are redistributed here.

## Authority Boundary

- `fa_IR`, `prs_AF`, `tg_Cyrl_TJ`, and `ar` must remain separate evidence lanes.
- This file is evidence for glossary work, not canonical approval.
- RTL PDF extraction required Unicode normalization and still may miss OCR/scanned pages.
- Arabic module terminology is especially variable and needs native mathematical review before any canonical choice.
- Tajik Cyrillic remains unresolved; this file does not cover it.

## Extraction Coverage

| Source | Sublane | Pages | Nonempty Text Pages | Term Hits | Notes |
| --- | --- | ---: | ---: | ---: | --- |
| IUT advanced algebra | fa_IR | 186 | 186 | 19 | ok |
| PNU ring/module preview | fa_IR | 21 | 20 | 13 | license/provenance review needed before reuse beyond metadata |
| Shahrood thesis | fa_IR | 100 | 100 | 21 | ok |
| Afghanistan algebra text | prs_AF | 265 | 260 | 4 | Dari/Afghanistan witness; broad anchors only so far |
| Mustansiriyah abstract algebra | ar | 436 | 433 | 4 | ok |
| Mosul rings theory | ar | 34 | 6 | 2 | few extractable pages; visual/OCR follow-up needed |
| Archive rings/fields PDF | ar | 416 | 0 | 0 | no extractable text; likely OCR/manual inspection needed |
| Milne Arabic group theory | ar | 164 | 164 | 6 | ok |
| Majmaah rings/fields spec | ar | 5 | 5 | 3 | ok |
| Mustansiriyah ring theory handout | ar | 3 | 3 | 2 | ok |

## Iranian Persian/Farsi Term Anchors

| Term | Working English Gloss | Evidence Category | Total Count | Source/Page Anchors | Rationale Status |
| --- | --- | --- | ---: | --- | --- |
| `جبر` | algebra | algebra_core | 46 | IUT advanced algebra pp. 1,3,14,20,32,36; PNU ring/module preview pp. 7,17,18; Shahrood thesis pp. 5,25,26,54,90 | candidate; inspect pages before promotion |
| `میدان` | field | field_theory | 58 | IUT advanced algebra pp. 6,7,9,11,28,36; PNU ring/module preview pp. 4,9,10,17; Shahrood thesis pp. 34,37,38,40,42,53 | candidate; inspect pages before promotion |
| `آرتینی` | Artinian | finiteness | 24 | PNU ring/module preview pp. 5; Shahrood thesis pp. 13,36,37,39,43,67 | candidate; inspect pages before promotion |
| `مدول` | module | module_theory | 1922 | IUT advanced algebra pp. 4,6,7,8,9,10; PNU ring/module preview pp. 1,4,5,7,8,10; Shahrood thesis pp. 5,6,8,9,12,13 | module-register candidate; Arabic variants require extra review |
| `زیرمدول` | submodule | module_theory | 355 | IUT advanced algebra pp. 4,10,11,12,13,14; PNU ring/module preview pp. 4,5; Shahrood thesis pp. 12,13,14,15,17,21 | module-register candidate; Arabic variants require extra review |
| `مدول چپ` | left module | module_theory | 354 | IUT advanced algebra pp. 6,7,8,9,10,11; Shahrood thesis pp. 21,23 | module-register candidate; Arabic variants require extra review |
| `مدول آزاد` | free module | module_theory | 65 | IUT advanced algebra pp. 62,63,64,65,67,68; Shahrood thesis pp. 15,34,84 | module-register candidate; Arabic variants require extra review |
| `مدول راست` | right module | module_theory | 62 | IUT advanced algebra pp. 6,7,8,37,70,71; Shahrood thesis pp. 5,9,12,15,21,22 | module-register candidate; Arabic variants require extra review |
| `ضرب تانسوری` | tensor product | module_theory | 37 | IUT advanced algebra pp. 4,70,71,72,74,77 | module-register candidate; Arabic variants require extra review |
| `همریختی` | homomorphism | morphism | 353 | IUT advanced algebra pp. 4,9,17,18,19,20; PNU ring/module preview pp. 3,4; Shahrood thesis pp. 8,15,24,34,39,85 | candidate; inspect pages before promotion |
| `یکریختی` | isomorphism | morphism | 34 | PNU ring/module preview pp. 3,4; Shahrood thesis pp. 24,47,55,66,67,73 | candidate; inspect pages before promotion |
| `خودریختی` | automorphism | morphism | 14 | Shahrood thesis pp. 5,50,51,54,56,83 | candidate; inspect pages before promotion |
| `نوتری` | Noetherian | noetherian | 303 | IUT advanced algebra pp. 4,143,148,149,150,151; PNU ring/module preview pp. 5; Shahrood thesis pp. 13,18,25,29,30,32 | Noetherian register candidate; page-inspect before promotion |
| `ساده` | simple | representation_theory | 233 | IUT advanced algebra pp. 4,14,15,16,24,25; PNU ring/module preview pp. 10,11,12,13; Shahrood thesis pp. 14,15,16,22,23,24 | representation/simple/semisimple candidate; check context carefully |
| `نمایش` | representation | representation_theory | 108 | IUT advanced algebra pp. 11,36,55,57,62,65; PNU ring/module preview pp. 11,14,17; Shahrood thesis pp. 5,6,9,12,13,14 | representation/simple/semisimple candidate; check context carefully |
| `نیم‌ساده` | semisimple | representation_theory | 94 | IUT advanced algebra pp. 4,94,95,97,98,104; Shahrood thesis pp. 14,15,22,23,64,67 | representation/simple/semisimple candidate; check context carefully |
| `حلقه` | ring | ring_theory | 614 | IUT advanced algebra pp. 4,6,7,8,9,10; PNU ring/module preview pp. 1,3,4,7,8,9; Shahrood thesis pp. 2,5,6,8,9,11 | candidate; inspect pages before promotion |
| `ایده‌آل` | ideal | ring_theory | 377 | IUT advanced algebra pp. 4,7,8,10,15,16; PNU ring/module preview pp. 3; Shahrood thesis pp. 2,5,6,9,11,12 | candidate; inspect pages before promotion |
| `ایده‌آل اول` | prime ideal | ring_theory | 104 | IUT advanced algebra pp. 56,61,165; Shahrood thesis pp. 2,5,6,9,11,16 | candidate; inspect pages before promotion |
| `حلقه جابجایی` | commutative ring | ring_theory | 70 | IUT advanced algebra pp. 8,26,36,41,43,48; PNU ring/module preview pp. 16,20,21; Shahrood thesis pp. 9,15,16,17,18,19 | candidate; inspect pages before promotion |
| `ایده‌آل ماکسیمال` | maximal ideal | ring_theory | 28 | IUT advanced algebra pp. 56,58,92,93,129,135; Shahrood thesis pp. 9,12,15,34,54,55 | candidate; inspect pages before promotion |
| `حلقه ناجابجایی` | noncommutative ring | ring_theory | 7 | IUT advanced algebra pp. 36,61,67; Shahrood thesis pp. 9,72 | candidate; inspect pages before promotion |

## Dari/Afghanistan Persian Term Anchors

| Term | Working English Gloss | Evidence Category | Total Count | Source/Page Anchors | Rationale Status |
| --- | --- | --- | ---: | --- | --- |
| `جبر` | algebra | algebra_core | 63 | Afghanistan algebra text pp. 3,8,10,11,12,39 | broad Dari evidence only; not enough for canonical technical choice |
| `میدان` | field | field_theory | 50 | Afghanistan algebra text pp. 5,44,59,60,61,64 | broad Dari evidence only; not enough for canonical technical choice |
| `ساده` | simple | representation_theory | 3 | Afghanistan algebra text pp. 221,223 | representation/simple/semisimple candidate; check context carefully |
| `حلقه` | ring | ring_theory | 16 | Afghanistan algebra text pp. 8,10,154,155,156,163 | broad Dari evidence only; not enough for canonical technical choice |

## Arabic Term Anchors

| Term | Working English Gloss | Evidence Category | Total Count | Source/Page Anchors | Rationale Status |
| --- | --- | --- | ---: | --- | --- |
| `جبر` | algebra | algebra_core | 131 | Mustansiriyah abstract algebra pp. 1,2,4,5,10,11; Mosul rings theory pp. 1; Milne Arabic group theory pp. 1,4,14,68,83,120; Majmaah rings/fields spec pp. 2,3 | candidate; inspect pages before promotion |
| `حقل` | field | field_theory | 332 | Mustansiriyah abstract algebra pp. 1,10,11,12,17,46; Milne Arabic group theory pp. 2,4,6,10,11,12; Majmaah rings/fields spec pp. 1,2,3,4 | candidate; inspect pages before promotion |
| `آرتيني` | Artinian | finiteness | 6 | Milne Arabic group theory pp. 70,84,85,163 | candidate; inspect pages before promotion |
| `تماثل` | isomorphism | morphism | 187 | Milne Arabic group theory pp. 3,6,10,11,13,15 | candidate; inspect pages before promotion |
| `تجانس` | homomorphism | morphism | 13 | Mustansiriyah abstract algebra pp. 103,135,138,142,143,144; Milne Arabic group theory pp. 71 | candidate; inspect pages before promotion |
| `حلقة` | ring | ring_theory | 305 | Mustansiriyah abstract algebra pp. 1,10,11,12,17,46; Mosul rings theory pp. 1; Milne Arabic group theory pp. 6,14,30,53,120,128; Majmaah rings/fields spec pp. 1,2,3,4 | candidate; inspect pages before promotion |

## Immediate Rationale Notes

- Iranian Persian/Farsi has strong extracted evidence for rings, ideals, modules, submodules, left/right modules, Noetherian and Artinian terminology, and morphism language.
- Dari/Afghanistan Persian currently has only broad algebra/ring/field/simple anchors from one educational text; it is not ready for a detailed technical glossary without more sources.
- Arabic now has reinforced ring/field/group-theory sources, but module and representation terminology remains thin or variable in the extracted data.
- Several Arabic PDFs are useful as witnesses but need OCR, provenance, or license review before they become stronger evidence.
- Tajik Cyrillic remains a separate unresolved lane and should not be inferred from Persian-script evidence.

Generated UTC: 2026-06-29T13:15:55.534712+00:00
