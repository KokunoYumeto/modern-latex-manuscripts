# Non-European Mathematics v3 PDF Audit and Repair TODO

Source root: `redacted source drop preserved in this record`

PDFs audited: 158. Recommended for public reader surface by structural/text checks: 146.

## Flag Counts

- `log_missing_characters`: 76
- `tofu_or_replacement_char`: 72
- `log_latex_errors`: 65
- `translator_or_process_note`: 9
- `test_pdf`: 9
- `many_overfull_boxes`: 7
- `html_error_page_text`: 7
- `low_text_extract`: 2

## Folder Coverage

- `chinese`: 23/23 recommended by audit
- `indian`: 20/20 recommended by audit
- `islamic`: 7/8 recommended by audit
- `master-index.pdf`: 1/1 recommended by audit
- `references`: 5/5 recommended by audit
- `translations`: 90/101 recommended by audit

## Priority Repair Queue

- `chinese/jiuzhang-suanshu-vols1-3.pdf`: log_missing_characters;log_latex_errors; pages=25; text chars=24328; missing chars=723; latex errors=11
- `chinese/jiuzhang-suanshu-vols4-6.pdf`: translator_or_process_note;tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=32; text chars=31634; missing chars=2; latex errors=2
- `chinese/li-ye-ceyuan-haijing-vols7-9.pdf`: tofu_or_replacement_char; pages=25; text chars=23562; missing chars=0; latex errors=0
- `chinese/sunzi-suanjing.pdf`: log_missing_characters;log_latex_errors; pages=33; text chars=10779; missing chars=18798; latex errors=5
- `chinese/yang-hui-xiangjie-jiuzhang-part1.pdf`: log_missing_characters;log_latex_errors; pages=20; text chars=17864; missing chars=1169; latex errors=15
- `chinese/yang-hui-xiangjie-jiuzhang-part3.pdf`: log_missing_characters;log_latex_errors; pages=32; text chars=18924; missing chars=1732; latex errors=8
- `indian/aryabhata-aryabhatiya.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=15; text chars=7124; missing chars=15968; latex errors=1
- `indian/bhaskara-ii-bijaganita-part1.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=39; text chars=11819; missing chars=15360; latex errors=3
- `indian/bhaskara-ii-bijaganita-part2.pdf`: tofu_or_replacement_char;log_missing_characters; pages=26; text chars=17026; missing chars=373; latex errors=0
- `indian/bhaskara-ii-bijaganita-part3.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=13; text chars=7257; missing chars=11707; latex errors=8
- `indian/bhaskara-ii-lilavati.pdf`: tofu_or_replacement_char;log_missing_characters; pages=14; text chars=5234; missing chars=19500; latex errors=0
- `indian/brahmagupta-brahmasphutasiddhanta-pt1-chunk1.pdf`: tofu_or_replacement_char;log_missing_characters; pages=32; text chars=35941; missing chars=54; latex errors=0
- `indian/brahmagupta-brahmasphutasiddhanta-pt1-chunk3.pdf`: log_latex_errors; pages=19; text chars=31527; missing chars=0; latex errors=1
- `indian/brahmagupta-brahmasphutasiddhanta-pt1-chunk4.pdf`: tofu_or_replacement_char; pages=23; text chars=13500; missing chars=0; latex errors=0
- `indian/brahmagupta-brahmasphutasiddhanta-pt1-chunk5.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=27; text chars=16472; missing chars=18264; latex errors=1
- `indian/brahmagupta-brahmasphutasiddhanta-pt1-chunk6.pdf`: tofu_or_replacement_char; pages=12; text chars=6406; missing chars=0; latex errors=0
- `indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk1.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=16; text chars=25424; missing chars=4189; latex errors=1
- `indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk2.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=23; text chars=31001; missing chars=5710; latex errors=3
- `indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk3.pdf`: tofu_or_replacement_char; pages=13; text chars=8462; missing chars=0; latex errors=0
- `indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk4.pdf`: log_latex_errors; pages=13; text chars=15265; missing chars=0; latex errors=1
- `indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk5.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=25; text chars=25256; missing chars=8217; latex errors=2
- `indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk6.pdf`: tofu_or_replacement_char;log_missing_characters; pages=16; text chars=12874; missing chars=8544; latex errors=0
- `indian/brahmagupta-brahmasphutasiddhanta-pt3-chunk1.pdf`: log_missing_characters;log_latex_errors; pages=13; text chars=13603; missing chars=2; latex errors=1
- `indian/brahmagupta-brahmasphutasiddhanta-pt3-chunk2.pdf`: tofu_or_replacement_char; pages=10; text chars=11693; missing chars=0; latex errors=0
- `indian/brahmagupta-brahmasphutasiddhanta-pt3-chunk3.pdf`: tofu_or_replacement_char;log_missing_characters; pages=19; text chars=20461; missing chars=4060; latex errors=0
- `islamic/al-kashi-miftah-al-hisab.pdf`: tofu_or_replacement_char;log_missing_characters; pages=26; text chars=27728; missing chars=4; latex errors=0
- `islamic/al-khwarizmi-al-jabr-wa-l-muqabala.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=47; text chars=38681; missing chars=188; latex errors=2
- `islamic/al-tusi-shakl-al-qatta.pdf`: log_latex_errors; pages=16; text chars=24452; missing chars=0; latex errors=1
- `islamic/karpinski-robert-of-chester-latin-translation-1915.pdf`: log_missing_characters; pages=42; text chars=16863; missing chars=30052; latex errors=0
- `islamic/omar-khayyam-sinaat-al-jabr.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=16; text chars=16485; missing chars=20; latex errors=5
- `islamic/rosen-algebra-of-mohammed-ben-musa-1831.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=20; text chars=4386; missing chars=114165; latex errors=1
- `islamic/ruska-zur-aeltesten-arabischen-algebra-1917.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors;many_overfull_boxes; pages=61; text chars=162781; missing chars=2; latex errors=37
- `master-index.pdf`: log_missing_characters;log_latex_errors; pages=10; text chars=3642; missing chars=12542; latex errors=1
- `references/al-muqaddasi-ahsan-al-taqasim.pdf`: log_missing_characters;log_latex_errors; pages=15; text chars=8889; missing chars=9727; latex errors=1
- `references/ibn-al-qifti-tarikh-al-hukama.pdf`: tofu_or_replacement_char;log_missing_characters; pages=10; text chars=15523; missing chars=24; latex errors=0
- `references/said-al-andalusi-tabaqat-al-umam.pdf`: tofu_or_replacement_char;log_missing_characters; pages=14; text chars=25324; missing chars=32; latex errors=0
- `translations/ar/chinese/jiuzhang-suanshu-vols1-3_arabic.pdf`: html_error_page_text;tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=26; text chars=85208; missing chars=1408; latex errors=1
- `translations/ar/chinese/li-ye-ceyuan-haijing-vols1-3_arabic.pdf`: tofu_or_replacement_char;log_missing_characters;many_overfull_boxes; pages=25; text chars=52677; missing chars=1173; latex errors=0
- `translations/ar/chinese/li-ye-ceyuan-haijing-vols10-12_arabic.pdf`: tofu_or_replacement_char;log_missing_characters;many_overfull_boxes; pages=29; text chars=52053; missing chars=8743; latex errors=0
- `translations/ar/chinese/li-ye-ceyuan-haijing-vols4-6_arabic.pdf`: tofu_or_replacement_char;log_missing_characters; pages=32; text chars=65408; missing chars=1465; latex errors=0
- `translations/ar/chinese/qin-jiushao-shuxue-jiuzhang-fascicle1_arabic.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=40; text chars=63708; missing chars=8959; latex errors=25
- `translations/ar/chinese/qin-jiushao-shuxue-jiuzhang-fascicle4_arabic.pdf`: tofu_or_replacement_char;log_missing_characters; pages=12; text chars=28445; missing chars=314; latex errors=0
- `translations/ar/chinese/sunzi-suanjing_arabic.pdf`: html_error_page_text;tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=14; text chars=13651; missing chars=6106; latex errors=3
- `translations/ar/chinese/test_tcolor.pdf`: html_error_page_text;test_pdf;log_latex_errors; pages=1; text chars=315; missing chars=0; latex errors=1
- `translations/ar/chinese/test_tcolor2.pdf`: html_error_page_text;test_pdf;log_latex_errors; pages=1; text chars=328; missing chars=0; latex errors=3
- `translations/ar/chinese/test_tcolor3.pdf`: html_error_page_text;test_pdf;log_latex_errors; pages=1; text chars=315; missing chars=0; latex errors=1
- `translations/ar/chinese/test_tcolor4.pdf`: html_error_page_text;test_pdf;log_latex_errors; pages=1; text chars=315; missing chars=0; latex errors=1
- `translations/ar/chinese/yang-hui-xiangjie-jiuzhang-part1_arabic.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors;many_overfull_boxes; pages=7; text chars=11801; missing chars=41048; latex errors=1014
- `translations/ar/islamic/al-kashi-miftah-al-hisab_arabic.pdf`: tofu_or_replacement_char;log_missing_characters; pages=38; text chars=24246; missing chars=3264; latex errors=0
- `translations/ar/islamic/al-khwarizmi-al-jabr_arabic-enhanced.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=60; text chars=50043; missing chars=45925; latex errors=2
- `translations/ar/islamic/omar-khayyam-sinaat-al-jabr_arabic.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=14; text chars=15642; missing chars=445; latex errors=3
- `translations/en/chinese/jiuzhang-suanshu-vols1-3_bilingual.pdf`: log_missing_characters; pages=14; text chars=9670; missing chars=34571; latex errors=0
- `translations/en/chinese/jiuzhang-suanshu-vols4-6_bilingual.pdf`: translator_or_process_note;log_latex_errors; pages=23; text chars=23808; missing chars=0; latex errors=10
- `translations/en/chinese/jiuzhang-suanshu-vols7-9_bilingual.pdf`: log_missing_characters;log_latex_errors; pages=33; text chars=16825; missing chars=52585; latex errors=81
- `translations/en/chinese/li-ye-ceyuan-haijing-vols7-9_bilingual.pdf`: tofu_or_replacement_char; pages=35; text chars=77881; missing chars=0; latex errors=0
- `translations/en/chinese/qin-jiushao-shuxue-jiuzhang-fascicle2_bilingual.pdf`: log_latex_errors; pages=15; text chars=20739; missing chars=0; latex errors=32
- `translations/en/chinese/qin-jiushao-shuxue-jiuzhang-fascicle6_bilingual.pdf`: log_missing_characters; pages=16; text chars=6902; missing chars=20431; latex errors=0
- `translations/en/chinese/qin-jiushao-shuxue-jiuzhang-fascicles7-9_bilingual.pdf`: log_latex_errors; pages=24; text chars=28890; missing chars=0; latex errors=2
- `translations/en/chinese/test_no_hyperref.pdf`: translator_or_process_note;test_pdf;log_latex_errors; pages=23; text chars=23986; missing chars=0; latex errors=12
- `translations/en/chinese/yang-hui-xiangjie-jiuzhang-part1_bilingual.pdf`: log_missing_characters; pages=25; text chars=38024; missing chars=2; latex errors=0
- `translations/en/chinese/yang-hui-xiangjie-jiuzhang-part3_bilingual.pdf`: log_missing_characters; pages=21; text chars=11717; missing chars=31773; latex errors=0
- `translations/en/indian/aryabhata-aryabhatiya_bilingual.pdf`: translator_or_process_note;tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=20; text chars=21468; missing chars=45; latex errors=15
- `translations/en/indian/bhaskara-ii-bijaganita-part1_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=32; text chars=23502; missing chars=4840; latex errors=1
- `translations/en/indian/bhaskara-ii-bijaganita-part2_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=18; text chars=14323; missing chars=4542; latex errors=1
- `translations/en/indian/bhaskara-ii-bijaganita-part3_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters; pages=12; text chars=17156; missing chars=645; latex errors=0
- `translations/en/indian/bhaskara-ii-lilavati_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters; pages=23; text chars=22908; missing chars=66; latex errors=0
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt1-chunk1_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=23; text chars=33831; missing chars=2; latex errors=464
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt1-chunk3_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=14; text chars=17031; missing chars=5; latex errors=2
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt1-chunk4_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters; pages=28; text chars=40943; missing chars=647; latex errors=0
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt1-chunk5_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=34; text chars=51095; missing chars=36794; latex errors=1
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt1-chunk5_bilingual_fixed.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=34; text chars=51095; missing chars=463; latex errors=1
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt1-chunk6_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=17; text chars=23452; missing chars=2609; latex errors=96
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt1-chunk6_bilingual_fixed.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=17; text chars=23452; missing chars=2725; latex errors=299
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk1_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=28; text chars=34238; missing chars=3218; latex errors=1
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk1_bilingual_fixed.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=28; text chars=34238; missing chars=3218; latex errors=1
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk2_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=17; text chars=21807; missing chars=36453; latex errors=7
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk3_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=21; text chars=31775; missing chars=3; latex errors=1
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk3_bilingual_fixed.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=21; text chars=31775; missing chars=9895; latex errors=87
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk4_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=9; text chars=13449; missing chars=203; latex errors=1
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk5_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters; pages=12; text chars=11435; missing chars=28943; latex errors=0
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt2-chunk6_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters; pages=18; text chars=37218; missing chars=10771; latex errors=0
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt3-chunk1_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=15; text chars=21431; missing chars=151; latex errors=59
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt3-chunk2_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=19; text chars=34490; missing chars=33; latex errors=50
- `translations/en/indian/brahmagupta-brahmasphutasiddhanta-pt3-chunk3_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=9; text chars=5471; missing chars=18323; latex errors=21
- `translations/en/islamic/al-kashi-miftah-al-hisab_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;many_overfull_boxes; pages=34; text chars=39972; missing chars=17763; latex errors=0
- `translations/en/islamic/al-khwarizmi-al-jabr-wa-l-muqabala_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=45; text chars=52753; missing chars=156; latex errors=2
- `translations/en/islamic/al-khwarizmi-al-jabr_bilingual.pdf`: translator_or_process_note;tofu_or_replacement_char; pages=47; text chars=44982; missing chars=0; latex errors=0
- `translations/en/islamic/al-tusi-shakl-al-qatta_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=22; text chars=34589; missing chars=25; latex errors=1
- `translations/en/islamic/karpinski-robert-of-chester-latin-translation-1915_bilingual.pdf`: log_latex_errors;many_overfull_boxes; pages=44; text chars=52401; missing chars=0; latex errors=5
- `translations/en/islamic/omar-khayyam-sinaat-al-jabr_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=18; text chars=17875; missing chars=22; latex errors=7
- `translations/en/islamic/rosen-algebra-of-mohammed-ben-musa-1831_enhanced.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=52; text chars=126304; missing chars=460; latex errors=6
- `translations/en/islamic/ruska-zur-aeltesten-arabischen-algebra_bilingual.pdf`: log_latex_errors;many_overfull_boxes; pages=65; text chars=250438; missing chars=0; latex errors=34
- `translations/en/references/al-muqaddasi-ahsan-al-taqasim_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=15; text chars=9138; missing chars=10792; latex errors=1
- `translations/en/references/ibn-al-nadim-kitab-al-fihrist_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=19; text chars=30759; missing chars=8; latex errors=2
- `translations/en/references/ibn-al-qifti-tarikh-al-hukama_bilingual.pdf`: html_error_page_text;tofu_or_replacement_char;log_missing_characters;log_latex_errors; pages=15; text chars=28871; missing chars=26; latex errors=3
- `translations/en/references/said-al-andalusi-tabaqat-al-umam_bilingual.pdf`: tofu_or_replacement_char;log_missing_characters; pages=12; text chars=23371; missing chars=23; latex errors=0
- `translations/en/references/smith-karpinski-hindu-arabic-numerals-1911_enhanced.pdf`: log_latex_errors; pages=17; text chars=28703; missing chars=0; latex errors=49
- `translations/zh/chinese/li-ye-ceyuan-haijing-vols7-9_classical-modern_bilingual.pdf`: tofu_or_replacement_char; pages=25; text chars=24551; missing chars=0; latex errors=0
- `translations/zh/chinese/zhu-shijie-suanxue-qimeng-part1_classical-modern_bilingual.pdf`: tofu_or_replacement_char; pages=25; text chars=31979; missing chars=0; latex errors=0
