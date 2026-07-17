# SGA 5 English synchronization — final adversarial audit of Exposés I and VII

Audit closed 2026-07-17. This report covers only Exposés I and VII in the sole live cumulative:

SGA5_English_sync_workpass.tex

The audit compared the live English with the current source-checked French control and used the LNM 589 scan or its scan-backed certification record where topology, accents, source emendation, or diagram logic required it. English SGA 1–4 translations on this disk were treated as translation/style precedents, not as substitutes for the SGA 5 source.

## Authorities and pinned state

- Current French control: sga5_fr_workpass.tex, SHA-256 791F4EFFC5E02832D5D77ED03518C8156D6F07E4C8238B03545DB93D883FBB28.
- Original LNM 589 scan: C:\Users\Floris\Documents\Papors\OS\SGA5 (1).pdf, SHA-256 B256EBD072A8C68209518412A263C9289C6F1854A346733D86F885930D5FE6CA.
- Live English at audit close: SHA-256 5FD80166F9905B8A69E4E079795BB936CDDE58B84E32A717913DE9202BDF511E, 796,628 bytes.
- Stable Exposé-I slice, normalized UTF-8/LF, live lines 1–2129: SHA-256 738CB2715349C465546C0EB1DEB6C8626199E1E877398E338FD62B8D8B4C2F7A.
- Stable Exposé-VII slice, normalized UTF-8/LF, live lines 9315–11837: SHA-256 05317F90315E7287BFE435977EFE0D619ADBA744BA91DE852F3FCD6D2435DA87.
- Machine-readable new-repair ledger: EXPOSE_I_VII_ADVERSARIAL_REPAIR_MAP_20260717.csv.

Line numbers above pin the audit-close state only; the exact anchors and printed source pages in the CSV remain controlling if later cumulative edits move lines.

## Outcome

The adversarial pass found and repaired four previously unlisted Exposé-I diagram-topology defects and nineteen physical Exposé-VII correction sites. Each row in the machine ledger records the exposé, printed source page, anchor, old form, new form, authority, and final status.

Final anchor revalidation:

| Scope | Result |
|---|---:|
| Previously listed Exposé-I residual groups I-R001–I-R042 | 42/42 current |
| Previously propagated exact Exposé-I groups | 16/16 current |
| New Exposé-I adversarial repairs I-A001–I-A004 | 4/4 old forms absent and new forms present |
| Previously applied nonexact Exposé-VII receipts | 24/24 current |
| Previously propagated exact Exposé-VII groups | 49/49 current |
| New Exposé-VII adversarial repairs VII-A001–VII-A019 | 19/19 old forms absent and new forms present |

The four apparent failures encountered while rechecking I-R015, I-R039, I-R041, and I-R042 were search-shape false negatives; direct anchor inspection confirmed the required negative Tate twist and underlined Hom/Ext operators. The four apparent failures in Exposé-VII receipts 0206, 0219, 0250, and 0265 were likewise formatting-sensitive searches; their complete current anchors were inspected and passed.

## Exposé I: diagram and formula findings

All thirteen source diagrams were checked in order:

- Twelve tikzcd blocks have the same nodes, edges, operators, and arrow directions as the French control.
- The remaining tikzpicture block, containing the paired printed-page-48 triangles, is normalized-equal to the French control. The word “and” versus “et” is outside the mathematical topology.
- Printed page 38 now has U to X and U-prime to X-prime as the vertical arrows in the cartesian square.
- Both printed-page-48 distinguished triangles now have the source cycle and the +1 label on the source edge.
- Printed page 71 now has i-prime from U to Y-prime, not the reverse.

The 42 previously listed Exposé-I repairs remain present. No new unresolved source ambiguity was introduced. The already documented printed-page-43 subscript uncertainty remains an editorial-ledger item; this audit did not guess or silently alter it.

## Exposé VII: formula, prose, and diagram findings

The pass corrected source-significant symbols and omitted derivation steps, including:

- the negative shift in the projective-bundle arrow c;
- degree 2i in formula (3.8.1);
- the missing i-star in the j-star image of (4.1.1);
- the p_i and j_i flag-variety indices;
- R^n in Q(S/T,L);
- the checked cotangent bundle in both formulas of Corollary 7.4;
- the d/bar-xi and pushforward symbols in the proof of Lemma 9.7;
- all v-star, i_1-star, alpha-star, beta-star, and gamma-star corrections in 9.7–9.8;
- the omitted beta-star-delta-star display and the D_1 sentence leading to (9.8.5);
- the exponential-sequence injection t maps to 2 i pi t;
- the scan-confirmed three-row D153 implication topology;
- the omitted displayed map in Lemma 8.2(c);
- the omitted middle equality in the projection-formula calculation.

All fifteen Exposé-VII diagram blocks have source-identical nodes, edges, operators, and arrow directions. Diagram 11 differs only in the TikZ label-side marker for f: the English puts the same f label on the opposite side of the same downward arrow. This is a rendered-layout choice, not a mathematical or topological difference.

After the repairs, the ordered Exposé-VII display sequence has 409 English openings and 410 French openings. The sole remaining count delta is the French standalone caption display “(D_1) (D_2)”; English embeds those labels directly inside the two diagrams. No formula, tag, statement, item, or diagram is missing. The remaining non-equal sequence entries are the translated title block and the harmless diagram-label-side choice just described.

Structural parity at close:

| Feature | English | French | Verdict |
|---|---:|---:|---|
| Tags | 100 | 100 | ordered sequence equal |
| Numbered statements | 62 | 62 | ordered numbers equal after title-language normalization |
| Diagram blocks | 15 | 15 | topology equal |
| Items | 64 | 64 | equal |
| Footnotes | 0 | 0 | equal |
| Display openings | 409 | 410 | one caption-representation delta only |

## Build disposition

No compile was run for this bounded audit, by explicit parent-manager instruction while the cumulative was being frozen. These edits therefore require inclusion in the parent’s next complete two-pass build, log capture, PDF hash, and rendered visual-QA tranche. This report does not claim whole-volume publication readiness from source parity alone.

## Files

- EXPOSE_I_VII_ADVERSARIAL_AUDIT_20260717.md — this durable audit.
- EXPOSE_I_VII_ADVERSARIAL_REPAIR_MAP_20260717.csv — exact machine-readable repair rows.
- `audit_evidence/expose_i_residual.md` — earlier detailed I-R001–I-R042 source table, retained as tranche-time audit evidence.
- `audit_evidence/expose_vii_application_receipt_20260717.md` — earlier 24-receipt Exposé-VII application record.

Bounded verdict: Exposés I and VII are current at every audited correction, ordered formula/display, source-significant prose, and diagram-topology site. No unadjudicated new I/VII defect remains from this pass.
