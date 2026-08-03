# FAC blind-comparator transport: Git line-ending error and correction

## Failed first Git custody state

Transport-acceptance commit
`9ac9236320415e5c455b729a9ca9b93b3848ca74` was pushed before an
independent comparison of Git blob bytes against the controlling public
projection manifest. Git's configured text filter normalized CRLF to LF in
five files. The commit remains immutable adverse history and is not the
accepted public-payload identity.

The exact mismatches were:

| File | Expected bytes | Git bytes | Expected SHA-256 | Git SHA-256 |
|---|---:|---:|---|---|
| `BLIND_COMPARATOR_GENERATION_VALIDATION.json` | 1,386 | 1,352 | `7E2C3A6E69C471DF3A0A50DE3731B4D62290C8A2321684A555B4786D1061DF9E` | `59A91A16F1F7F9EFAA97AD9B302B3B3EAF72D7340442B33FA3914C2DF759E623` |
| `BLIND_COMPARATOR_INPUT_IDENTITIES.csv` | 15,492 | 15,396 | `76FB5CB89C484AD21BC8813C1DBFE9960C1AA209F678A7B1D1E129F7F19AB102` | `662ABD7B3FEECE595FE860888815C249D2D8CF974AE9301E5A235FB449DD4A91` |
| `FAC_BLIND_COMPARATOR_ALL_79_FINDINGS.csv` | 68,365 | 68,226 | `2291410CD5BE0C483E159769E45B9B79F378FBDA28857E1B5A1597C78403AE73` | `2266BF7512726D6CD1E7E361AC9A098B0357274208E30916CEE9C5669AA37E89` |
| `FAC_BLIND_COMPARATOR_ALL_79_UNIT_REVIEWS.csv` | 51,218 | 51,138 | `09F2D367C565D71F68ECC195E34BD2FB9DBEE72FD098EBB747CBEDF1A4E16E7E` | `EAE9C825F7E1AA5E3FB7074421EA97BE15955FB49CADC6421A3CB379A31C4B8E` |
| `FAC_BLIND_COMPARATOR_INVENTORY.csv` | 53,297 | 53,217 | `AD8D4A8A242BBE3A5FD6606928904151A067F303C1780BF072BE909CD7F744AB` | `88F47561075D1E807A314E063D02C1C2BDFF18593B7CB2ECD2987E480FF2C7D5` |

The other fourteen payload files matched the controlling public projection.
No producer source, private-custody file, or intended Zenodo upload byte was
changed by this Git-only transport defect.

## Corrected Git custody state

Commit `3c9489183c9dc46e5fc318b5fecd665b1dfdf4ea` adds the scoped rule
`payload/* -text` and recommits the five affected payload files without text
normalization. The rule applies only to this immutable payload directory.

Anonymous raw GitHub readback then passed:

- all 19 payload files / 734,806 bytes against
  `PUBLIC_PROJECTION_IDENTITY_MANIFEST.csv`;
- all six files changed by the correction commit; and
- the three required direct provenance surfaces remain directly readable.

Readback receipts:

- `manifests/published-github/20260803_fac_blind_comparator_payload_commit_3c9489183_19_file_public_readback.json`
  — 11,352 bytes — SHA-256
  `A5A5785638EE24CA5DC519780399FE7EA3DF1E488621445FB5776B6E3A0AE201`;
- `manifests/published-github/20260803_fac_blind_comparator_transport_commit_3c9489183_public_readback.json`
  — 3,134 bytes — SHA-256
  `D065577F41ACBF258332A36610C0A2E65AFD7D4BF395FD96EC6AEF8C897E2AF0`.

This correction establishes GitHub custody only. It does not claim Zenodo
publication or Zenodo public readback.
