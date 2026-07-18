# Source check

Internal source reconciliation covers the 20 units in `SOURCE_UNIT_MAP.csv`, including the separately represented `\srcfn{marker}{text}` note `NOE-P25-N001`.

- Ordered displays: source/Hans 3/3, mathematically equal in order.
- Source emphasis: source/Hans 14/14.
- Source footnote: source/Hans 1/1 at the restored opening locus.
- Galois-field overline: source/Hans 1/1.
- Inherited failures repaired: omitted/moved apparatus, lost overline, `完备域` for perfect field, field/ring object confusion, bare `理想基`, quotient/fraction ambiguity, and lexicalized `原理想` collision.
- Hans/Hant computational integrity: 165/165 ordered math spans, 232/232 TeX controls, 8/8 environment tokens, balanced 92/92 braces, 324/324 dollar delimiters, and 3/3 display delimiter pairs.
- Typed decisions: 14 records, zero schema/join errors. Evidence graph: 205 nodes, 288 edges, zero errors, acyclic, with A012→A007, A013→A009, and A014→A010 supersession links; old evidence edges are retained but marked inactive for current decisions.
- Search evidence correction: the exact-search shelf is mixed CJK, not PRC-only—71 Chinese-oriented files and 24 Japanese files. `超越次数` has 2 Chinese and 4 Japanese hit lines; Japanese hits never authorize Chinese. `超越度` has 0/0. The lexical choice independently rests on exact Li Wenwei Chinese evidence.

Machine authorities are `qa/SOURCE_PARITY_REPORT.json`, `qa/DECISION_SCHEMA_VALIDATION_REPORT.json`, `qa/EVIDENCE_GRAPH_VALIDATION_REPORT.json`, and `qa/FREEZE_VALIDATION_REPORT.json`. These are internal checks, not external semantic certification.

