# Independent review

An independent source/formula review passed the stable
`SGA2-VIII-IV-II-NGT1` target after the extraction, authority-box, page-marker,
and evidence-ledger repairs. No further target repair was required.

Reviewed source boundary: corrected French lines 2856--2872, printed pages
95--96, physical same-edition PDF pages 83--84, running pages 75--76, blank
2873 excluded, cursor 2874. The reviewer separately confirmed that the
physical page break is between 2864 and 2865 while the source
`pageoriginale` token occurs inside line 2865 after `il existe`.

Frozen target identities reviewed:

- TeX: 3,579 bytes, SHA-256
  `67DD636D18534E5AB372C7D38E13D98036DC821DF5C3D52FAB5D912395026252`;
- PDF: 284,712 bytes, one A4 page, SHA-256
  `C85E8FA13F035E68FFE98507E8E556952CFFFACEEE9F6F58C45853356C6F3BD8`;
- layout extraction: 3,381 bytes, one formfeed, zero forbidden controls,
  SHA-256
  `ECDB67ECCB1BCC24B8CC41C85FA71C49A5CBFCF80E1617D5867BC0F58ADA849A`;
- 300-dpi target render: 487,279 bytes, SHA-256
  `990CD4090076C8296EC2607A4034FDB7497BA5F3F4A36F285352069288CFC9CF`;
- machine validation: 3,527 bytes, `errors: []`, SHA-256
  `DCE020547C9C076B108BD928EAA0B5269B6089486ADC891F6D9D3E343D25F73D`.

The independent pass checked the induction hypothesis, immediate
specialization wording, literal diagram-(2.7) dependency, EGA III 1.4.15,
both higher-direct-image isomorphisms, italic local reduction, plain `A/x`
source oddity, underlined sheaf Gamma, point-versus-ideal symbols, Expose III
2.1, `g'` arrow and explanation, tilde `N`, strict `p<n-1`, both weak depth
bounds, proof close, and Section-3 exclusion. It also confirmed all 20 PDF
fonts are embedded, subset, and Unicode-mapped; all five Artifact Tool
receipts pass; the 64 CSV rows and 43 JSONL records validate with reference
closure and no formula-injection cells.

Two caveats survive the seal rather than being silently normalized:

- corrected-source upright roman `F` to target calligraphic `F` follows the
  P2-SETUP precedent as a provisional SGA2 English convention pending manager
  consolidation, explicitly recorded as an
  adverse glyph delta and revisitable under SGA-wide notation adjudication;
- French line 2865's transition from the `Ass F''` argument to `F=tilde M`,
  `M=F(X)` remains a high-priority source ambiguity. The target faithfully
  preserves `F`; silent `F''` emendation is rejected. A source-owner alert is
  already recorded by filename and SHA-256 in the machine ledgers.

This review seals only the bounded unit. It does not claim a complete Expose
VIII, a complete SGA2 volume, archive custody, publication, or public readback.
