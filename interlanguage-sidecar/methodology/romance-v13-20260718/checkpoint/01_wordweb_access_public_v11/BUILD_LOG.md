# Deterministic build log — public Romance WordWeb/access v11

Status: **PASS**

- Two isolated builds were made from the same four SHA-bound internal v11 inputs.
- Both isolated builds ran the independent semantic/access/public-safety validator.
- The live build was rebuilt separately and matched both isolated builds byte-for-byte.
- Stable pre-finalization file count: 12.
- Stable pre-finalization set hash: `BF542AD6DDE68F450A011BC306784256B0C2E26C51EDBA2D1F28A281E6A77AB0`.
- Validator checks: 33/33 passed.
- Source-input binding was recomputed: `true`.
- Counts: 60 concepts; 106 senses; 39 extension nodes; 811 evidence-metadata records; 106 decisions; 406 relation records with 27 target-ID edges; 78 supported senses and 28 gaps; 954 access rows across nine cohorts.
- Human observations: 0. Pilot-eligible rows/decisions: 0. Form promotions: 0.
- Public-safety scan rejects quote/locator/source-path keys and absolute host-path values.
- A deterministic ZIP is written twice with fixed member timestamps and permissions; its final hash is intentionally recorded outside the archive to avoid self-reference.

Input hashes:

- `PAN_ROMANCE_WORDWEB_v11`: `570822B02B2C713429C097CA526B87ACE39C2441A1DEB1B937E79FBA18303E26`
- `PAN_ROMANCE_ACCESS_LEDGER_v11_json`: `2EB865261D3A769164EEAD60133B71E7D812419716CA9F9DD244C5593E1D92E3`
- `PAN_ROMANCE_ACCESS_LEDGER_v11_csv`: `463E66246A8EF22599689C0E58B985BD928BCA8D39015280AC554600100EF137`
- `MII_METHOD_v11`: `6B9E527E966F34EB9A6DB61FD743D54FB3BE073D0F3A8E98DD27B11B3910E861`

Claim boundary: this log establishes deterministic projection and validation only. It does not clear underlying source rights, supply human observations, certify intelligibility, or complete the Romance lane.
