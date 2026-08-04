# Paper 36 producer worker returns

These returns record bounded producer assistance only. None of the workers performed or claimed source, semantic, formula, terminology, translation-quality, rendered-visual, native-reader, regional, approval, publication, archive, or certification checking.

## `/root/p36_docs_draft`

Drafted `TRANSLATION_NOTES.md` and `STATUS.md` while build results were still intentionally unclaimed. Initial returned SHA-256 values were `CD971D6ED257D5E4514FDB09B1AFEBBA7B39D17193357EFFDA66AC0190DE6A90` and `EE3C86A3406FF84EAD01A783350D23B5F84F74A21729DC6B94B61C5ADAA1A188`. The root producer later appended final build metadata, producing final hashes recorded in the checker handoff.

## `/root/p36_hant_build`

Generated controlled-generic Hant from Hans SHA-256 `928C90ED8A02FA9F5BAA5E891CE780CCFF76878BB86515D84F7064E8998E6416`, replayed the deterministic conversion, and performed two mechanical XeLaTeX passes. Returned Hant TeX/PDF/log SHA-256 values: `88892EB73FEE50DBAF53C5ABA656A985479439CE41C53D88EB4A82CDCED15CBF` / `CCBD4BF5D30F2702E96A809EAFE1260890F1F6E6362E4E9A4FBF7AA4071F4CB3` / `6EB305F2AEF3E8E91AB2B7FB3863B1AACD182FFEF6F8E985A61D4228FE235B2B`. The worker explicitly reported no PDF viewing or visual inspection and no regional localization.

## `/root/p36_evidence`

Produced the exact-schema seven-row terminology, adverse-evidence, and CJKV CSV ledgers plus a 35-node/35-edge typed graph. Returned SHA-256 values: `4327A23339144081C4F3B613217BBC46247EEE643E158E2CCB5F4A88BE75031C`, `75CDA29505E33812A8673E898CD226290B2768D1407821FC9A2B3242B52D1423`, `C9AD2A7CA306FBD2936B6CF9BE953EB3F642D7A5BEA638751B6C3BD084FF86A9`, and `A878E604086C24AF41E6958F4C3B212DBC20FA4BC7B4A58B3EF93428A694453B`. Japanese and Korean fields remain explicitly unconsulted.

## Root producer disposition

The root producer mechanically parsed all three CSVs as seven rectangular rows with headers matching the adjacent Paper 38 schemas; parsed the graph as 35 nodes and 35 edges with unique node IDs and zero missing `from`/`to` references; and bound returned hashes in the final handoff. These are file/schema computations, not content checking.
