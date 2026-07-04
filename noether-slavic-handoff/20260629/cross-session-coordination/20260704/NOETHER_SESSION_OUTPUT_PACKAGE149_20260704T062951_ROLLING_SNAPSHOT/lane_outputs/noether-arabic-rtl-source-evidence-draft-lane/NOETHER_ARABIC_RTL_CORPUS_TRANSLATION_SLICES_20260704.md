# Noether Arabic RTL Corpus Translation Slices

Draft / non-canonical / not native reviewed / not approved. Created 2026-07-04 for the whole Arabic RTL lane.

This artifact uses the six-row Arabic glossary/source sidecar as support and translates corpus slices from the current German baseline. It is not a reviewer packet, gate ledger, or canonical Arabic edition. It preserves unresolved term flags where a native Arabic mathematical reviewer or RTL TeX/PDF reviewer must decide.

German baseline used:

`C:\Users\memo_\Documents\Codex\2026-06-09\could-you-look-online-for-me\work\noether-slavic-canonical\tmp\zenodo_20836874_inspect\localcodex\Noether_R124plus_LocalCodex_PostR124_Consolidated_WebDrop_20260624\tex\cum_de_R124plus_localcodex_current_candidate_20260624.tex`

Glossary/source sidecar used:

`C:\Users\memo_\Documents\Codex\2026-07-04\noether-arabic-rtl-source-evidence-draft-lane\outputs\NOETHER_ARABIC_RTL_DRAFT_CORPUS_SIDECAR_20260704.md`

## Completion Scope

All six active Arabic rows are represented in actual draft corpus translation slices:

- `term-ar-0001` algebra: slices `AR-SLICE-005`, plus algebra references in `AR-SLICE-001`, `AR-SLICE-002`, and `AR-SLICE-007`.
- `term-ar-0002` field: slices `AR-SLICE-001`, `AR-SLICE-002`, and `AR-SLICE-007`.
- `term-ar-0003` Artinian / chain condition: slice `AR-SLICE-004`.
- `term-ar-0004` homomorphism: slices `AR-SLICE-006` and `AR-SLICE-008`.
- `term-ar-0005` isomorphism: slices `AR-SLICE-007` and `AR-SLICE-008`.
- `term-ar-0006` ring: slices `AR-SLICE-003`, `AR-SLICE-004`, `AR-SLICE-005`, `AR-SLICE-006`, and `AR-SLICE-008`.

## AR-SLICE-001: Rational Function Fields

Source anchor: German baseline lines 4510-4527, `Rationale Funktionenkörper`.

Queue rows touched: `field`, `ring` by contrast through coefficient domain, `algebra` through Steinitz algebraic-field reference.

Draft Arabic translation:

```text
٥. حقول الدوال الكسرية.

ترجع المسائل الآتية في الأصل إلى محادثات مع إ. فيشر. وقد طرح إ. شتاينتز بعض هذه المسائل، وأنجزها أيضاً، في الحالة الخاصة لمتغيّر واحد، وذلك في ظل فروض أعم على نطاق المعاملات.

أفهم من «حقل دوال كسرية» حقلاً تكون عناصره دوالاً كسرية في \(n\) من المتغيرات، بمعاملات من حقل عددي معطى، يمكنه بوجه خاص أن يضم جميع الأعداد المركبة. ومن أمثلة هذه الحقول: حقل الدوال المتماثلة في \(n\) من المقادير، أو على نحو أعم مجموع الدوال الكسرية في \(n\) من المتغيرات التي تقبل تبديلات زمرة معينة، وهي نطاقات لاغرانج النوعية؛ وكذلك حقل الثوابت.

وبين الحقلين المذكورين أولاً والحقل الأخير فرق مميز: فالأولان يحتويان \(n\) دوال مستقلة جبرياً، هي الدوال المتماثلة الأولية، أما عدد الثوابت المستقلة جبرياً فهو دائماً أصغر من عدد المتغيرات. لذلك من المهم أن نستطيع، على وجه عام، أن نقرن حقول النوع الثاني اقتراناً تقابلياً بحقول النوع الأول، وذلك بأن نستبدل بعض المتغيرات بأعداد. ولهذا سأقتصر فيما يأتي على حقول النوع الأول، أي على الحقول التي تحتوي \(n\) دوال مستقلة جبرياً؛ وبفضل هذا الاقتران تصح النتائج عندئذ على وجه عام.

تتجمع المسائل حول ثلاثة مفاهيم للأساس: الأساس الكسري، والأساس الأدنى، وأساس التكاملية.

١. أفهم من «أساس كسري» عدداً منتهياً من دوال الحقل، بحيث يمكن تمثيل كل دالة من دوال الحقل تركيباً كسرياً من ذلك العدد المنتهي، بمعاملات من نطاق المعاملات المعطى. وتبيّن اعتبارات بسيطة وجود الأساس الكسري لكل حقل دوال كسرية.
```

Rendering notes:

- `حقل دوال كسرية` is the draft rendering of `rationaler Funktionenkörper`; unresolved flag `AR-FLAG-001` covers `الدوال الكسرية` versus `الدوال الناطقة`.
- Keep \(n\) separated from Arabic words. TeX draft should use `\(n\)` inside Arabic direction context.
- `N نطاقات لاغرانج النوعية` is a draft for `Lagrangesche Gattungsbereiche`; this is outside the six-row glossary and should be reviewed if promoted.

## AR-SLICE-002: Fields And Systems Of Rational Functions

Source anchor: German baseline lines 4551-4604, `Körper und Systeme rationaler Funktionen`.

Queue rows touched: `field`, `ring`, `algebra`.

Draft Arabic translation:

```text
٦. الحقول وأنظمة الدوال الكسرية.

تتناول هذه المقالة مسائل الأساس في أنظمة اعتباطية من الدوال الكسرية والدوال كثيرة الحدود؛ وتُظهر المناهج المستعملة من نظرية الحقول أن معالجة هذه المسائل في حقول مؤلفة من دوال كسرية، أي في حقول الدوال الكسرية، هي المسألة الجوهرية، بينما تظهر تعميمات النتائج على الأنظمة الاعتباطية كنتائج تابعة.

أما في الأنظمة العامة فلم يكن معروفاً إلى الآن، من مسائل الأساس، إلا وجود أساس الموديول الذي تكفله مبرهنة هيلبرت. وفيما يأتي ستُجاب مسألة قابلية التمثيل الكسري إجابة تامة بواسطة وجود الأساس الكسري لكل نظام اعتباطي؛ أما الأساس الكسري للحقول فيظهر منذ الفقرة ٤. ويتيح وجود هذا الأساس الكسري أن ننطلق على الدوام من الحقل أو النظام المعرّف تعريفاً مجرداً، وأن نتجنب بذلك الصعوبات التي ترجع إلى اختيار خاص للأساس الكسري، لا إلى النظام في ذاته، مثل ظهور مقامات خاصة أو نقاط أساسية لدوال الأساس.

وفي الحقول تعالج كذلك مسألة الأساس الأدنى، أي الأساس الكسري المؤلف من دوال مستقلة جبرياً. وتقود مناهج نظرية الحقول أيضاً إلى أساس كسري ممتاز، هو أساس الالتفاف، وهو يصبح جوهرياً على الخصوص في النطاقات التكاملية من كثيرات الحدود. فهو يعطي هنا تمثيلاً ذا مقام ثابت، كما هو معروف مثلاً في الحالة الخاصة للتمثيل النمطي للثوابت.

المسألة في ما يلي هي دراسة أنظمة من دوال كسرية في \(n\) من المتغيرات، وبخاصة حقول الدوال الكسرية.

وعليه فـ \(f(x_1\cdots x_n)\)، و \(g(x_1\cdots x_n)\)، ...، أو اختصاراً \(f(x)\)، و \(g(x)\)، ...، تعني دائماً دوالاً كسرية في \(x_1\cdots x_n\)، مفترضة في صورة مختزلة، أي إن البسط والمقام أوليان فيما بينهما. أما الدوال الكسرية الصحيحة، أي كثيرات الحدود، فسترمز إليها حروف كبيرة مثل \(F(x)\)، و \(G(x)\)، ... . ويفترض أن نطاق المعاملات \(\Omega\) حقل عددي ما، يمكنه بوجه خاص أن يضم جميع الأعداد المركبة؛ كما يمكن أن يحتوي \(\Omega\) عدداً منتهياً من الوسائط.

بعد هذه التحديدات يمكن تعريف حقل الدوال الكسرية تعريفاً مجرداً.

التعريف I: يسمى نظام من الدوال الكسرية حقلاً إذا حقق الشرطين الآتيين:

١. إذا احتوى \(f(x)\)، فإنه يحتوي أيضاً \(c\cdot f(x)\) لكل مقدار \(c\) من \(\Omega\).

٢. إذا احتوى \(f(x)\) و \(g(x)\)، فإنه يحتوي دائماً \(f(x)+g(x)\)، و \(f(x)\cdot g(x)\)، وكذلك، عندما \(g(x)\ne0\)، خارج القسمة \(f(x):g(x)\).
```

Rendering notes:

- `Körper` is consistently `حقل`.
- `ganze rationale Funktionen` is rendered as `الدوال كثيرة الحدود` after a first explanatory phrase; direct literal `الدوال الكسرية الصحيحة` is awkward and should not be left unclarified.
- Formula-neighboring Arabic should be PDF-checked around `\(f(x)\)` and `\(g(x)\)`.

## AR-SLICE-003: Ideal Theory In Ring Domains

Source anchor: German baseline lines 11281-11306 and 11331-11362, `Idealtheorie in Ringbereichen`.

Queue rows touched: `ring`, `field`, `isomorphism` in component-isomorphism footnote context.

Draft Arabic translation:

```text
نظرية المثاليات في نطاقات حلقية.

مقدمة.

يتألف مضمون هذه المقالة من نقل مبرهنات التحليل الخاصة بالأعداد الصحيحة الكسرية، أو بالمثاليات في الحقول العددية الجبرية، إلى مثاليات في نطاقات تكاملية اعتباطية، وبصورة أعم في نطاقات حلقية. ولتوضيح هذا النقل نورد أولاً مبرهنات التحليل للأعداد الصحيحة الكسرية بصياغة تختلف شيئاً ما عن الصياغة المعتادة.

إن التحليلين ١ و٢ وحيدان؛ أما في تحليلين مختلفين من النوع ٣ أو ٤ فإن عدد المركبات والمثاليات الأولية التابعة لها يتفقان. والمثاليات المعزولة التي تظهر بين المركبات محددة تحديداً وحيداً.

ومن أجل برهان مبرهنات التحليل، يُستنتج من شرط الانتهاء «مبرهنة السلسلة المنتهية» التي صاغها ديدكيند أولاً للموديولات العددية المنتهية؛ ومنها تُشتق صيغة كل مثالي بوصفه المضاعف المشترك الأصغر لعدد منته من المثاليات غير القابلة للاختزال. وبإعادة صياغة مفهوم قابلية اختزال مركبة ما نحصل على مبرهنة الوحدانية الأساسية للتحليل ٤ إلى مثاليات غير قابلة للاختزال.

١. ليكن النطاق الأساس \(\Sigma\) حلقة تبديلية بالمعنى المجرد، أي إن \(\Sigma\) يتألف من نظام عناصر \(a,b,c,\ldots,f,g,h,\ldots\)، عرّفت فيه علاقة مساواة تحقق الشروط المعتادة، وتنتج فيه عمليتان، هما الجمع والضرب، من كل عنصرين حلقيين \(a\) و \(b\) عنصراً ثالثاً وحيداً هو المجموع \(a+b\) والجداء \(a\cdot b\). وعلى الحلقة والعمليات، التي هي فيما عدا ذلك اعتباطية تماماً، أن تحقق القوانين الآتية:

١. قانون التجميع للجمع: \((a+b)+c=a+(b+c)\).

٢. قانون التبديل للجمع: \(a+b=b+a\).

٣. قانون التجميع للضرب: \((a\cdot b)c=a(b\cdot c)\).

٤. قانون التبديل للضرب: \(a\cdot b=b\cdot a\).

٥. قانون التوزيع: \(a(b+c)=ab+ac\).

٦. قانون الطرح غير المقيّد والوحيد: يوجد في \(\Sigma\) عنصر وحيد \(x\) يحقق المعادلة \(a+x=b\). ويرمز إليه بـ \(x=b-a\).

ومن هذه الخواص ينتج وجود الصفر؛ غير أن الحلقة لا يلزم أن تمتلك عنصراً واحدياً، وقد ينعدم جداء عنصرين من غير أن ينعدم أحد العاملين. والحلقات التي ينتج فيها من انعدام جداء ما انعدام أحد العاملين دائماً، وتمتلك فوق ذلك عنصراً واحدياً، تسمى نطاقات تكاملية حقيقية.
```

Rendering notes:

- `Ringbereich` is rendered provisionally as `نطاق حلقي`; unresolved flag `AR-FLAG-002`.
- `ganze rationale Zahlen` is rendered `الأعداد الصحيحة الكسرية` only because the German phrase is historically loaded; reviewer should decide whether plain `الأعداد الصحيحة` is better in the final Arabic.
- In an Arabic TeX target, keep the list numerals Arabic or project-standard, but do not let `\item` markers inherit wrong direction around formulas.

## AR-SLICE-004: Minimal Condition / Artinian-Adjacent Context

Source anchor: German baseline lines 16507-16521 and 16648-16652.

Queue rows touched: `Artinian`, `ring`, `homomorphism` through ring-homomorphism/representation context.

Draft Arabic translation:

```text
تظهر في البرهان الحسابي الآتي المقادير فوق المركبة ونظرية التمثيلات من جديد بوصفهما كلاً موحداً، أي حالة خاصة من نظرية عامة للحلقات غير التبديلية التي لا يفرض عليها إلا أن تحقق شروط انتهاء معينة. ويتعلق الأمر بنظرية أصناف الموديولات والمثاليات بالنسبة إلى هذه الحلقات، ونتيجتها الرئيسة أن أصناف الموديولات غير القابلة للاختزال تستنفدها أصناف المثاليات المقابلة؛ وبوجه خاص، فإن كل أصناف الموديولات في الحلقات الخالية من الجذر تتحلل إلى أصناف غير قابلة للاختزال، أي تصبح تامة الاختزال.

وتتبيّن أن «مبرهنة سلسلة المضاعفات» للمثاليات اليمنى، أو الشرط الأدنى المطابق لها، تكفي شرطاً للانتهاء؛ ومعنى ذلك أن في كل مجموعة من المثاليات اليمنى يوجد مثالي أدنى، داخل تلك المجموعة. وينتج من ذلك تطابق الحلقات الخالية من الجذر والمحققة للشرط الأدنى مع الحلقات التامة الاختزال يميناً، ذات العنصر الواحدي.

أما الشرط الأعظمي فيعني أن في كل مجموعة من الزمر الجزئية توجد زمرة جزئية أعظمية، أي زمرة لا تحتويها زمرة أخرى من المجموعة. ويكافئ ذلك أن كل سلسلة صاعدة من الزمر الجزئية
\[
\mA_1\subset\mA_2\subset\mA_3\cdots
\]
تنقطع بعد عدد منته من الحدود.

والشرط الأدنى يعني أن في كل مجموعة من الزمر الجزئية توجد زمرة جزئية أدنى، لا تحتوي زمرة أخرى من تلك المجموعة، أو أيضاً أن كل سلسلة نازلة
\[
\mA_1\supset\mA_2\supset\mA_3\cdots
\]
تنقطع بعد عدد منته من الحدود.
```

Rendering notes:

- This is the Artinian lane's corpus slice, but the German anchor says `Minimalbedingung`, not `Artinian`. The draft must not silently replace Noether's phrase with `آرتيني`.
- Use `الشرط الأدنى` where translating Noether's literal term, and reserve `حلقة آرتينية` for reviewer notes or modern explanatory apparatus.
- `يميناً` after `تامة الاختزال` should be reviewed for idiomatic placement in Arabic algebra prose.

## AR-SLICE-005: Algebra Of Hypercomplex Quantities

Source anchor: German baseline lines 21034-21102 and bibliography lines 23938-23943.

Queue rows touched: `algebra`, `ring`, `field`, `isomorphism`.

Draft Arabic translation:

```text
جبر المقادير فوق المركبة.

محاضرة للأستاذة إ. نويثر، الفصل الشتوي ١٩٢٩/١٩٣٠.
حررها الأستاذ م. دويرنغ.

تتناول هذه المحاضرة نظرية التمثيلات العامة للحلقات، التي نشأت من جهة من نظرية تمثيلات الزمر المنتهية، ومن جهة أخرى من النظرية الجبرية والحسابية لنظم الأعداد فوق المركبة. ولهذا التصور الأعم لنظرية التمثيلات مزايا على التصور السابق عند فروبينيوس وشور.

فبما أن النظر هنا لا يقع على الزمرة، بل على حلقة الزمرة، وبصورة أعم على نظام فوق مركب أو على حلقة اعتباطية، يمكن استعمال نظرية الحلقات والمثاليات. وهذا يحرر النظرية من كثير من الحسابات المتشعبة، ولا يبسّطها فحسب، بل يدفعها أيضاً إلى الأمام، مثلاً في مسألة علاقات الزمرة بزمرها الجزئية، ويفتح لها ميادين تطبيق جديدة. ويمكن، بمساعدة نظرية التمثيلات العامة، إعطاء تأسيس جديد أنيق جداً للنظرية الغالوية، بل، وهو الأهم ربما، إقامة نظرية غالوية للحقول غير التبديلية.

مداخل ببليوغرافية مقابلة:

برهان مبرهنة رئيسة في نظرية الجبور.

النظم فوق المركبة في علاقاتها بالجبر التبديلي ونظرية الأعداد.

جبور غير تبديلية.
```

Rendering notes:

- `Algebra` as a discipline is `الجبر`; `Algebren` as plural algebraic structures is drafted as `جبور`, but this needs native mathematical review (`AR-FLAG-006`).
- `hyperkomplexe Größen` is drafted as `المقادير فوق المركبة`; an edition may prefer `الكميات فوق المركبة`.
- `nichtkommutative Körper` remains `حقول غير تبديلية` in this draft because Noether's German uses `Körper`; a reviewer may decide whether division-ring terminology should be made explicit in Arabic.

## AR-SLICE-006: Reciprocal Representation And Homomorphism

Source anchor: German baseline lines 21117-21124.

Queue rows touched: `homomorphism`, `isomorphism`, `ring`, `field`.

Draft Arabic translation:

```text
تعريف التمثيل العكسي.

التمثيل العكسي من الدرجة \(n\) لـ \(\mathfrak v\) في \(\mathsf T^*\) هو حلقة جزئية \(\mathfrak D^*\) من حلقة المصفوفات \(\mathsf T_n^*\) ذات الدرجة \(n\) بعناصر من \(\mathsf T^*\)، تُصوَّر عليها \(\mathfrak v\) تصويراً حلقياً تشاكلياً عكسياً.

وبعبارة رمزية:
\[
\mathfrak{d} \nrightarrow \mathfrak{O}^* \subseteq T_n^*
\]

ولإعطاء مثال على مفهوم التشاكل العكسي: إذا قرنّا بالمصفوفات ذات \(n\) من الصفوف في حقل تبدلي مصفوفاتها المنقولة، فإن هذا الإقران تماثل حلقي عكسي.
```

Rendering notes:

- The German/OCR line for the formal definition is visibly corrupted by repetition, so this draft translates the recoverable mathematical sense only. This is an exact blocker for canonical release, not for draft slicing.
- `Ringhomomorphie` is drafted with `تشاكل حلقي`; `reziprok` is `عكسي`.
- `gespiegelten` is drafted as `مصفوفاتها المنقولة`; if the edition wants a more literal matrix reflection term, review is needed.

## AR-SLICE-007: Isomorphic Mapping

Source anchor: German baseline lines 7667-7702, `Die Funktionalgleichungen der isomorphen Abbildung`.

Queue rows touched: `isomorphism`, `field`, `ring`.

Draft Arabic translation:

```text
١٠. المعادلات الدالية للتطبيق التماثلي.

يفهم ديدكيند من التطبيق التماثلي للحقل \(\Afield\) على نظام \(\Bfield\)، الذي يتبين لاحقاً أنه هو أيضاً حقل، إقراناً وحيداً من النوع الآتي: يقابل كل عنصر من \(\Afield\) عنصر واحد ولا غير من \(\Bfield\)، وتقابل مجموعَ أي عنصرين من \(\Afield\)، وفرقَهما، وجداءَهما، وخارجَ قسمتهما، على الترتيب، مجموعات العناصر المقابلة في \(\Bfield\)، وفروقها، وجداؤها، وخوارج قسمتها.

وليكن هذا التطبيق معطى بدالة، وحيدة بحسب ما سبق، هي \(f(z)\). فإذا دار \(z\) على جميع عناصر \(x,y,\ldots\) من الحقل \(\Afield\)، فإن \(f(z)\) تتميز بالمعادلات الدالية الآتية:
\[
\begin{array}{ll}
(1)\quad f(x+y)=f(x)+f(y); & (2)\quad f(x-y)=f(x)-f(y);\\[0.45em]
(3)\quad f(x\cdot y)=f(x)\cdot f(y); & (4)\quad f\!\left(\dfrac{x}{y}\right)=\dfrac{f(x)}{f(y)}.
\end{array}
\]

وفيما يأتي ستعطى أعم الحلول الوحيدة \(f(z)\) لهذه المعادلات الدالية عندما يجري \(x,y,\ldots\) على جميع الأعداد الحقيقية والمركبة؛ أي أعم دالة \(f(z)\) تنجز تطبيقاً تماثلياً لحقل جميع الأعداد المركبة. وبصورة مماثلة تماماً نحصل على الحل في الحقول الاعتباطية.

نستخلص أولاً بعض النتائج من المعادلات الدالية (١) إلى (٤)، وذلك مباشرة للحقول العامة \(\Afield\). فمن (١) ينتج من الوحدانية أن \(f(0)=0\). وإذا كان \(f(y)\) غير منعدم، فلا يمكن أن يكون \(y\) الأصلي منعدماً؛ وتبين المعادلات الدالية (١) إلى (٤) أن نظام الصورة \(\Bfield\)، أي نظام جميع القيم \(f(z)\)، يؤلف بدوره حقلاً.

ومن \(f(x)=f(y)\) ينتج إذن \(x=y\)، أي إن كل قيمة لـ \(f(z)\) يقابلها أيضاً مقدار واحد ولا غير من \(z\): فالدالة \(f(z)\) دالة تقابلية في \(z\). وتبين المعادلات الدالية أن التطبيق المعطى بالدالة العكسية هو أيضاً تطبيق تماثلي. ولما كانت كل عملية كسرية مركبة من عدد منته من عمليات الجمع والضرب وعكوسهما، يمكن القول أيضاً إن التطبيق التماثلي يقيم علاقة تقابلية بين عناصر \(\Afield\) وعناصر \(\Bfield\)، بحيث تحفظ جميع العلاقات الكسرية القائمة بين أي عدد منته من عناصر \(\Afield\)، والعكس بالعكس.

وإذا جعلنا، بدلاً من حقل، نطاقاً تكاملياً \(\Jdom\) أساساً، فقد لا ينتمي \(x/y\) إلى \(\Jdom\)، ولا يمكن أن نستنتج من (٣) التقابلية. وهنا تكفي الصيغة الأشهر: التطبيق التماثلي هو إقران تقابلي بين عناصر \(\Jdom\) و \(\Jdom'\)، بحيث يقابل المجموع والجداء دائماً المجموع والجداء.
```

Rendering notes:

- `isomorphe Abbildung` is drafted as `التطبيق التماثلي`. Review alternatives: `التطبيق المتماثل`, `التماثل`, or in theorem-heavy contexts `التطبيق التشاكلي التقابلي`.
- The phrase `rationale Relationen` is drafted as `العلاقات الكسرية`; reviewer should decide whether `العلاقات النسبية` or `العلاقات الجبرية الكسرية` is clearer.
- The math display is retained LTR inside Arabic prose.

## AR-SLICE-008: Later Homomorphism / Isomorphism In Crossed Products

Source anchor: German baseline lines 23201-23203 and 23331-23347.

Queue rows touched: `homomorphism`, `isomorphism`, `ring`, `field`, `algebra`.

Draft Arabic translation:

```text
البرهان والتعاريف. لنفترض أن \(\mathfrak{G}=\mathfrak{L}\{E,S,\ldots,T\}\) هي زمرة غالوا لـ \(\mathfrak{J}\). ومعنى أن \(\mathfrak{K}_r\) يساوي الجداء المتقاطع هو أن
\[
\mathfrak{K}_r=\mathfrak{J}u_{\mathfrak{E}}+\cdots+\mathfrak{J}u_r
\]
مع
\[
zu_S=u_Sz^S,\qquad u_Su_T=a_{S,T}u_{ST}.
\]

وتعرّف الزمرة المولدة \(\mathfrak{G}^*\) بأنها مجموع العناصر النظامية \(g\) من \(\Re_r\) التي تنقل \(\Im\) كلها إلى نفسها بالتحويل:
\[
g^{-1}\Im g=\Im,\qquad g^{-1}zg=z^S.
\]
وهكذا تصبح \(\Im\) صورة تشاكلية زمريّة لـ \(\Im^*\)، إذ إن كل تماثل ذاتي لـ \(\Im\) يولده عنصر \(g\).

دعوى. يكون
\[
\tilde{c}_{S,T}=\tilde{a}_{S,T}\tilde{b}_{S,T},
\]
حيث إن \(\tilde{a}\) و \(\tilde{b}\) هما العنصران المتماثلان مع \(a\) و \(b\) في \(\tilde{\mathfrak{J}}\).

يرتكز البرهان على أن حلقة التماثلات الذاتية لأحد المثاليات اليسرى من \(\mathfrak{A}_j\)، متى كانت له الطول المطلق \(n\)، تكون متماثلة مع
\[
\mathfrak{A}_f=\tilde{\mathfrak{Z}}\tilde{\mathfrak{G}},
\]
وعلى أن حلقة التماثلات الذاتية هذه يمكن تعيينها مباشرة لمثالي أيسر مناسب من \(\mathfrak{A}_f\).

المبرهنة ١. حلقة التماثلات الذاتية لمثالي أيسر \(\mathbb{I}\) ذي طول مطلق \(n\) في
\[
\Re_{rs}=\Re_r\times\mathsf{P}_s
\]
تكون متماثلة مع \(\Re_r\).

التمهيد ١. جميع المثاليات اليسرى ذات الطول المطلق \(n\) في \(\Re_{rs}\) متشاكلة مؤثرياً. ومن ثم فإن حلقات تماثلاتها الذاتية متماثلة حلقياً.

التمهيد ٢. إذا كان \(o\) حلقة ذات عنصر واحدي، وكان \(l=oe_1\) مثالياً أيسر ومجموعاً مباشراً، بحيث يكون \(e_1\) عنصراً متساوي القوة، فإن حلقة التماثلات الذاتية لـ \(l\) متماثلة مع \(e_1oe_1\).

البرهان. إن الضرب بعنصر \(e_1re_1\) يحدث تشاكلاً مؤثرياً من \(\mathfrak{l}\) إلى نفسه. والعناصر المختلفة \(e_1re_1\) تحدث تشاكلات مختلفة، لأن \(e_1\) يقابل عندئذ عناصر مختلفة، وكل تشاكل يتولد بهذه الطريقة.
```

Rendering notes:

- The German/OCR around these later lecture notes contains symbol corruption; this draft keeps the recoverable algebraic structure and flags the rest for TeX source review.
- `gruppenhomomorphes Bild` is rendered `صورة تشاكلية زمريّة`.
- `operatorisomorph` is rendered `متشاكلة مؤثرياً`; reviewer should decide whether `تماثل مؤثري` is better to keep the isomorphism family separate from homomorphism.
- `Automorphismenring` is rendered `حلقة التماثلات الذاتية`.

## Blocker Ledger

These blockers prevent canonical release or reviewer-packet promotion, but they do not prevent draft corpus slicing for the Arabic lane.

| Flag | Scope | Status |
| --- | --- | --- |
| `AR-FLAG-001` | `rationale Funktionen`, `Funktionenkörper` | Draft uses `الدوال الكسرية`; review against `الدوال الناطقة`. |
| `AR-FLAG-002` | `Ringbereich` | Draft uses `نطاق حلقي`; review against `مجال حلقي`, `حلقة`, or context-specific domain phrasing. |
| `AR-FLAG-003` | `Minimalbedingung` / Artinian row | Draft translates Noether literally as `الشرط الأدنى` / `شرط السلسلة التنازلية`; do not insert `آرتيني` into the corpus unless reviewer approves explanatory modernization. |
| `AR-FLAG-004` | Homomorphism row | Draft uses `تشاكل`; older/source variants `تجانس` and transliterated forms remain evidence only. |
| `AR-FLAG-005` | Isomorphism row | Draft uses `تماثل`, `متماثل`, and `التطبيق التماثلي`; review against `تشاكل تقابلي` where bijectivity must be explicit. |
| `AR-FLAG-006` | `Algebra` / `Algebren` | Draft uses `الجبر` for discipline and `جبور` for plural algebra structures; native math review required. |
| `AR-FLAG-007` | RTL TeX / formula adjacency | All Arabic prose with inline formulas needs PDF review under the project RTL stack before any packet use. |
| `AR-FLAG-008` | OCR/TeX corruption in lecture notes | Lines around reciprocal homomorphism and crossed products contain corrupted symbols/repetition; draft translates recoverable meaning only. |

## RTL / TeX Implementation Notes

- Use an Arabic direction context around prose, e.g. `\textarabic{...}` or a project-approved Arabic environment.
- Keep displayed formulas outside forced RTL prose blocks when possible.
- Keep spaces around inline math: `ليكن \(o\) حلقة` not `ليكن \(o\)حلقة`.
- Arabic punctuation used in prose: `،` and `؛`. Do not leave German semicolons inside Arabic clauses unless they are part of a TeX display.
- Formula-neighboring strings requiring PDF inspection: `\(n\) من المتغيرات`, `\(\Omega\) حقل عددي`, `\(\Re_r\)-موديول`, `\(R\)-حلقة`, `\(g^{-1}\Im g=\Im\)`.
- Avoid Persianate terms such as `همریختی` or `یکریختی`; they are not Arabic lane authorization.

## Review And Gate Status

- Draft corpus translation slices exist for the whole six-row Arabic lane.
- All slices are non-canonical and not native reviewed.
- No reviewer packet was populated.
- No gate ledger was modified.
- No approval or promotion was claimed.
- No Git push was performed.

