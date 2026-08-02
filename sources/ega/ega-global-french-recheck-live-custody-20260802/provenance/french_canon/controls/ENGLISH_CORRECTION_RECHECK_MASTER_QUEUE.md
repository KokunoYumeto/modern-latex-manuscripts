# English correction recheck master queue

This is a mechanical persistence of correction, source-defect, and adjudication
claims already recorded in the English/Germanic EGA working and publication
trees. It makes **no correctness judgment**. Every substantive row remains
`PENDING_DIRECT_NUMDAM_RECHECK`; every structural or already-no-edit row remains
`STRUCTURAL_NO_EDIT_REPLAY`.

The exact machine-readable ledger is
`controls/ENGLISH_CORRECTION_RECHECK_MASTER_QUEUE.csv`. Its 60 data rows map
one-to-one to the checklist IDs below and carry the complete absolute English
source locator, authority locator and SHA-256, evidence locator and SHA-256,
stable ID where available, and status.

## Scope and row invariants

| Class | Rows | Required status |
|---|---:|---|
| Substantive source-reading claims | 54 | `PENDING_DIRECT_NUMDAM_RECHECK` |
| Structural/no-edit adjudications | 6 | `STRUCTURAL_NO_EDIT_REPLAY` |
| Main queue total | 60 | — |

Official errata projections are deliberately excluded from those 60 rows and
are listed in a separate section at the end of this document.
`EGA-STRUCT-003` records only the no-edit duplicate-placement adjudication for
item 53; the projected erratum content remains in the separate section.

## English source roots

- `G` = `<REDACTED_USER_HOME>/Documents/interlanguage/03_projects/language_management/english_germanic/<REDACTED_INTERNAL_PUBLICATION_STAGING>/EGA_English_Global_0_IV_complete_linked_reader_20260801_r1/source`
- `R4` = `<REDACTED_USER_HOME>/Documents/interlanguage/03_projects/language_management/english_germanic/<REDACTED_INTERNAL_PUBLICATION_STAGING>/EGA4_English_complete_source_aligned_reference_v2_reader_20260801_r4/source`
- `W1` = `<REDACTED_USER_HOME>/Documents/interlanguage/03_projects/language_management/english_germanic/<REDACTED_INTERNAL_WORKSPACE>/ega1_english_source_aligned_successor_20260730_r1`
- `W2` = `<REDACTED_USER_HOME>/Documents/interlanguage/03_projects/language_management/english_germanic/<REDACTED_INTERNAL_WORKSPACE>/ega2_english_source_aligned_successor_20260729_r1`
- `W411` = `<REDACTED_USER_HOME>/Documents/interlanguage/03_projects/language_management/english_germanic/<REDACTED_INTERNAL_WORKSPACE>/ega4_sections11_21_source_aligned_successor_r1_20260730`
- `W416` = `<REDACTED_USER_HOME>/Documents/interlanguage/03_projects/language_management/english_germanic/<REDACTED_INTERNAL_WORKSPACE>/ega4_sections16_18_source_aligned_successor_r1_20260730`
- `W419` = `<REDACTED_USER_HOME>/Documents/interlanguage/03_projects/language_management/english_germanic/<REDACTED_INTERNAL_WORKSPACE>/ega4_sections19_21_source_aligned_successor_r1_20260730`
- `WC` = `<REDACTED_USER_HOME>/Documents/interlanguage/03_projects/language_management/english_germanic/<REDACTED_INTERNAL_WORKSPACE>/ega4_english_complete_cumulative_source_aligned_successor_r1_20260731`

## Authority SHA-256 anchors

| Authority | SHA-256 |
|---|---|
| EGA I | `9ABA23020217535977E279BDD06A0413F48DA703086865BA4C00766C85DF4AE6` |
| EGA II | `111834EFFFE9E90D068389D418F08925A82B4A54AE2957F080712D4180E032EB` |
| EGA III-1 | `3ED59FE81DA07F1AB685DDC54A93128A364419D4DDAFBC7AFFCD8ABC8B401605` |
| EGA III-2 | `3AD9D3710BCEEBB44B4FBAA976DCD05A719DB6FA2DCF2523C5A6669CE72C59CC` |
| EGA IV-1 | `DF11AFC6B6318FC491032B1239CD4AF9CBC2A7C73219DCC49BF65E5EE6C13140` |
| EGA IV-2 | `C3E960AA1C5C37046E8892D8A3CAC098E2738164136B5CDAA5D5D893F89931DA` |
| EGA IV-3 | `F365212B38F20608BA34C21AE3EE40BBAE1B42D9D3DFF01A85356F9CC819C23E` |
| EGA IV-4 | `B4277FB99C6EDF8FEEC5B01F54368E4B8521BCD52871316C0EDF6FF4AE69389E` |

## Substantive source-reading claims

The arrow in this checklist means only “recorded authority reading → current
English claim.” It does not endorse either side. Exact evidence paths and
hashes are in the CSV row with the same ID.

### EGA 0 — 5 rows

- [ ] `EGA0-SR-001` — `0_IV-1` p.67; `G/ega0/ega0-18.tex:773`; `(18.3.9)` → `(18.3.8)`.
- [ ] `EGA0-SR-002` — `0_IV-1` p.146; `G/ega0/ega0-20.tex:1680`; `(18.3.4.2)` → `(18.3.6.4)` and `(18.3.6.2)`.
- [ ] `EGA0-SR-003` — `0_IV-1` p.171; `G/ega0/ega0-21.tex:918`; `(20.6.3.2)` → `(20.6.5.2)`.
- [ ] `EGA0-SR-004` — `0_IV-1` p.177; `G/ega0/ega0-21.tex:1181`; `(20.14.4)` → `(20.7.14.4)`.
- [ ] `EGA0-SR-005` — `0_IV-1` p.217; `G/ega0/ega0-23.tex:185`; `(23.1.8.1)` → `(23.2.3.1)`.

### EGA I — 16 rows

- [ ] `EGA1-SR-001` — EGA I printed p.93/physical 92; `G/ega1/ega1-1.tex:804`; visible corollary number recorded as `1.5.3` → English Corollary `1.5.2` in the coherent-sheaf-of-rings passage.
- [ ] `EGA1-SR-002` — p.96/physical 95; `ega1-1.tex:982`; heading `(2.6.9)` → `1.6.9`.
- [ ] `EGA1-SR-003` — p.96/physical 95; `ega1-1.tex:992`; heading `(s.6.10)` → `1.6.10`.
- [ ] `EGA1-SR-004` — EGA-I claim with EGA-II witness p.219/physical 216; `ega1-1.tex:1154`; `X→Spec(A)` → `Y→Spec(A)`.
- [ ] `EGA1-SR-005` — EGA-I claim with EGA-II witness p.221; `ega1-1.tex:1256`; `1.8.8.1` → `1.8.9.1`.
- [ ] `EGA1-SR-006` — EGA-I claim with EGA-II witness p.221; `ega1-1.tex:1265`; “Proposition 1.8.7” → “Corollary 1.8.7”.
- [ ] `EGA1-SR-007` — EGA I p.98/physical 97; `G/ega1/ega1-2.tex:48`; generic point of `X` → generic point of `Y`.
- [ ] `EGA1-SR-008` — p.109/physical 108; `G/ega1/ega1-3.tex:398-400`; product pair `f` → `(g,ψ)`.
- [ ] `EGA1-SR-009` — p.114/physical 113; `ega1-3.tex:751`; “monomorphism” → “homomorphism”.
- [ ] `EGA1-SR-010` — p.122/physical 121; `G/ega1/ega1-4.tex:152`; reversed `θ#` direction → `ψ*(O_X)→O_Y`.
- [ ] `EGA1-SR-011` — p.153; `G/ega1/ega1-6.tex:745`; `W_1` a neighbourhood of `x` → `y=f(x)`.
- [ ] `EGA1-SR-012` — p.166; `G/ega1/ega1-8.tex:133`; `x∈V(a)=W∩F` → `F=W∩V(a)`.
- [ ] `EGA1-SR-013` — p.178; `G/ega1/ega1-9.tex:768`; injection `j` → `i`.
- [ ] `EGA1-SR-014` — p.180; `ega1-9.tex:837`; reversed exponents → `B^n→B^m`.
- [ ] `EGA1-SR-015` — p.210; `G/ega1/ega1-10.tex:1457`; `f=g∘j` → `f=j∘g`.
- [ ] `EGA1-SR-016` — printed p.223/physical 222; `G/ega1/ega1-backmatter-index-terminology.tex:268`; index target `I.3.6.1` → `I.3.1.1` with source disclosure.

### EGA II — 4 rows

- [ ] `EGA2-SR-001` — p.7/physical 4; `G/ega2/ega2-1.tex:118-120`; `λ∈S` → `λ∈A`.
- [ ] `EGA2-SR-002` — p.9/physical 6; `ega2-1.tex:220-222`; `Γ(U,B̃)=B` → `Γ(S,B̃)=B`.
- [ ] `EGA2-SR-003` — p.10/physical 7; `ega2-1.tex:281-282`; printed finite-type clause and citation I.9.6.2 → English omission of that clause.
- [ ] `EGA2-SR-004` — p.37/physical 34; `G/ega2/ega2-2.tex:1094-1097`; `α_d(f^n), α_d(f^k)` → `α_nd, α_kd`.

### EGA III — 1 row

- [ ] `EGA3-SR-001` — EGA III-2 p.210; `G/ega3/ega3-7-9.tex:298-301`; recorded omission of `(-1)^{i_0}` → English inclusion of that sign.

### EGA IV — 28 rows

- [ ] `EGA4-SR-001` — IV-1 p.233; `R4/ega4-1.source_aligned_r1.tex:553`; `v∘u` → `u∘v`.
- [ ] `EGA4-SR-002` — IV-2 p.91; `R4/components/02_section42_associated_prime_cycles.tex:240-242`; `X=Spec(A)` → `Spec(B)`.
- [ ] `EGA4-SR-003` — IV-2 p.95; `R4/components/05_section55_dimension_formula_finite_type.tex:97-99`; `(5.5.1.2)` → `(5.5.1.1)`; stable ID `ega4.reference.candidate.sha256.62b6932f0b0fd6ee72684a32f69d5a4df785723c5e7c90a515346dfbea1f7c3e`.
- [ ] `EGA4-SR-004` — IV-2 p.101; `R4/components/06_section56_dimension_formula_universally_catenary.tex:504-506`; “fraction field of A” → “residue field of A”.
- [ ] `EGA4-SR-005` — IV-2 p.194, target pp.140-141; `R4/source_aligned/ega4-7.tex:582`; `(6.3.9)` → Corollary `(6.3.5)(i)`; stable ID `ega4.reference.candidate.sha256.bfb14ddf99355cc9b8372768a0d85461582798431431286ac6d3c57f71ccb3f0`.
- [ ] `EGA4-SR-006` — IV-2 p.216; `ega4-7.tex:1542`; final-clause `A` → `B`.
- [ ] `EGA4-SR-007` — IV-3 p.180, target IV-2 p.80; `R4/source_aligned/ega4-12.tex:284`; `(4.7.14)` → `(4.7.13)`; stable ID `ega4.reference.candidate.sha256.a8825603c4a3c5e312837ddaf3b74e4a5dcf10724d6f0d5fad5c5b78e66b3cee`.
- [ ] `EGA4-SR-008` — IV-3 p.182; `ega4-12.tex:378`; `A/At^4` → `B/Bt^4`.
- [ ] `EGA4-SR-009` — IV-3 p.189; `R4/source_aligned/ega4-13.tex:48`; `f_0^{-1}(y)` → `f_0^{-1}(y_0)`.
- [ ] `EGA4-SR-010` — IV-3 p.203; `R4/source_aligned/ega4-14.tex:172-174`; source drops primes after defining `X'_{ij}` → English retains `X'_{ij}`.
- [ ] `EGA4-SR-011` — IV-3 p.228; `R4/source_aligned/ega4-15.tex:195`; `(11.6.4)` → `(11.6.2)`; stable ID `ega4.reference.candidate.sha256.496748db9bef1716d9930ac33e70abecb917c225b2c7ff5aa0edf9a4092794a6`.
- [ ] `EGA4-SR-012` — IV-3 p.233; `ega4-15.tex:411`; `X_i∩f^{-1}(y)` → use of `y′`.
- [ ] `EGA4-SR-013` — IV-3 p.233; `ega4-15.tex:425`; `f′:X→Y` → target `Y′`.
- [ ] `EGA4-SR-014` — IV-3 p.238; `ega4-15.tex:628`; openness at `f′^{-1}(z)` → points over `X_y^0`.
- [ ] `EGA4-SR-015` — IV-3 p.238; `ega4-15.tex:630`; `v(y),v(y′)` → `v(z),v(z′)`.
- [ ] `EGA4-SR-016` — IV-3 p.242; `ega4-15.tex:770`; `X^y` → `X^0 / X_{y_0}^0`.
- [ ] `EGA4-SR-017` — IV-4 p.8/physical 7; `R4/source_aligned/ega4-16.tex:135-136`; `φ_{n,n-1}` → `φ_{n-1,n}`.
- [ ] `EGA4-SR-018` — IV-4 p.12, target IV-3 p.222; `ega4-16.tex:348`; `(14.5.12.1)` → `(14.5.11.1)`; stable ID `ega4.reference.candidate.sha256.bc114b6b56912727646cfdc9eb3e115ea8abf69eef76db357ef539d3e25b57e6`.
- [ ] `EGA4-SR-019` — IV-4 p.78/physical 77; `R4/source_aligned/ega4-17.tex:1124`; `(17.12.5.1)` → semantic Proposition `17.12.5(a,c)`; candidate `ega4.reference.candidate.sha256.53c142cd28fd5ff2759d3a7875c52d42f105c3cde2bd7e4921f9f1c0bc5a75eb`; action `ega4.reference-action.sha256.ce12a09f2b6b4026a72da59f4a6f88fd6a5d9c9c1dc07803bcb024dd41f69b0b`; source-span SHA `8B8B1B9A22CCDC86A7FE4060D464F3F19B5A0628DA854072EA457A0C070C4EF3`.
- [ ] `EGA4-SR-020` — IV-4 p.89/physical 88; `ega4-17.tex:1854`; `(17.5.9)` → `(17.5.1)`; stable ID `ega4.reference.candidate.sha256.6c4e1afc8e49fef32f557160480df68f9e30a76d37c1c39eabd6444f5e1c610c`.
- [ ] `EGA4-SR-021` — IV-4 p.93/physical 92; `ega4-17.tex:1972`; `(16.5.12.5)` → `(16.5.13.5)`; stable ID `ega4.reference.candidate.sha256.13ddd36c81618134a7f3a9ddfc92018921a27a9b3af43520788896b115db53c4`.
- [ ] `EGA4-SR-022` — IV-4 p.189; `R4/source_aligned/ega4-19.tex:187`; `(19.1.4),(i)-(iv)` → Proposition `19.1.5`.
- [ ] `EGA4-SR-023` — IV-4 p.192; `ega4-19.tex:290`; `x` → `y`.
- [ ] `EGA4-SR-024` — IV-4 p.196; `ega4-19.tex:494`; `Y-f(X-U)` → `S-f(X-U)`.
- [ ] `EGA4-SR-025` — IV-4 p.237; `R4/source_aligned/ega4-20.tex:540`; `f|U′` → `f|V′`.
- [ ] `EGA4-SR-026` — IV-4 p.240; `ega4-20.tex:692`; introduced `V_α,V_λ,V` but subsequent `U_α,U_λ,U` → English consistently uses `U` notation.
- [ ] `EGA4-SR-027` — IV-4 p.313; `R4/source_aligned/ega4-21.tex:2866`; direct French `15.1.1.6`, exceptional fibre `P^1_k`, and `Y_s-{z}` → current English restores the complete sentence after inherited collapse.
- [ ] `EGA4-SR-028` — IV-4 p.333; `R4/source_aligned/ega4-backmatter-bibliography.tex:56-58`; `G. S. Seshadri` → `C. S. Seshadri`.

## Structural/no-edit adjudications

- [ ] `EGA-STRUCT-001` — EGA III-1 marker context; `G/ega0/ega0-10.tex:89`; sequence `18,10,20`, with ledger assertion that the middle marker is structurally `19`; current marker retained pending replay. Stable ID `EGA3-COV-CURRENT-MIRROR-EGA0-10`. Status `STRUCTURAL_NO_EDIT_REPLAY`.
- [ ] `EGA-STRUCT-002` — EGA IV-1 oldpage namespace switch; current `R4/ega4-1.source_aligned_r1.tex:421-1349`; inherited journal pages 225-229 then collected leaves 326-346, with NUMDAM header 230/leaf 326; current markers use journal 230-250. Stable ID `EGA4-S01-OLDPAGE-NAMESPACE-SWITCH-001`. Status `STRUCTURAL_NO_EDIT_REPLAY`.
- [ ] `EGA-STRUCT-003` — EGA IV-4 p.358/physical 357; official Errata List 3 item 53 intentionally appears once inline and once in the appendix. Status `STRUCTURAL_NO_EDIT_REPLAY`.
- [ ] `EGA-STRUCT-004` — EGA IV-3 p.184; `R4/source_aligned/ega4-12.tex:484-486`; current English already has `Tor_{n+1}^B(M,N)=Tor_1^B(R,N)` and the separate citation `(M,V,7)`. Status `STRUCTURAL_NO_EDIT_REPLAY`.
- [ ] `EGA-STRUCT-005` — EGA IV-3 p.185; `ega4-12.tex:564`; current English already represents “Or, comme...” and exact `ρ∘u=0`. Status `STRUCTURAL_NO_EDIT_REPLAY`.
- [ ] `EGA-STRUCT-006` — EGA IV-3 p.224; `R4/source_aligned/ega4-15.tex:32`; current English already says “and we have `z_i=z`”. Status `STRUCTURAL_NO_EDIT_REPLAY`.

## Evidence-ledger anchors

These hashes anchor the principal claim and adjudication ledgers. Row-specific
images, page manifests, paths, and hashes remain in the CSV.

| Ledger | SHA-256 |
|---|---|
| `W1/SOURCE_ALIGNMENT_LOG.md` | `8F52B76B68747ED10483BE0A9B30DDBEDEC7C7E21BEF30B7AAFB518A04C736B4` |
| EGA III coverage/defects ledger | `20152B4B9EC1D75B3CEEEA6C5B3A9A9BE1AE8879E05AF99E50E4B79E36DCF4C8` |
| EGA IV §1 marker defect | `DCDA3FBF40C6C2B6619426EEE3A5CBC6DA50213C54D933B60C945F43276227E0` |
| EGA IV §1 marker audit | `6FA7899D3FB0740F61BE6BEE07E43696A15D256B8FA9626A8D9661CF8A0BD376` |
| `W411/LOGBOOK.md` | `412D23600823D8146717982BB79B76B0B9760B8091B98A7D29281E43646F4920` |
| `W416/LOGBOOK.md` | `BACE9FB9C024EDFB017710062310B6272ED6AD100391493D76A88FDB52DC136B` |
| `W419/LOGBOOK.md` | `B1212500E0B51FB5B1B70C12942D6A5B8E4D997E64A1C8E26543B5E193E47D47` |
| Cross-reference adjudication | `40CD7E0FE80C94CAD069E623ED68E4E249442091F0CE3081C42F1E70AE8BC237` |
| Cross-reference evidence manifest | `A44555B168620A96B6474F9D49AEE26A45EBF5CA880F82B4856F21AC9D53D11B` |
| R4 source-corrections note | `A1195C905B02EF9DC6395013AB280AB89CBAC375A06D55D2977CF7C85BBB5AB2` |
| R4 reference-exception dispositions | `BEF47F48AAB24B53E97B6171B53C45805E0F782CF8C46DB3AE65AD625D6742A8` |
| R4 reference actions | `C5E019DB673CE8EFDE890F3AB0B97B40FD60702BF48A4033550AF9837790130C` |

## Separate official errata projections — excluded from main queue

The following are projections of published errata/addenda. They are **not
mixed with the 54 local correction/source-reading allegations** above.

### Projection files

| Projection file | SHA-256 |
|---|---|
| `G/ega2/ega2-errata-addenda.tex` | `95A26EFBACD66FD2C635E73BCDF3C3BA3DED2517EBC250B9DC3744B92EE40F22` |
| `R4/source_aligned/ega4-21-erratum53-insertion.tex` | `D5E9B663A516FFEEF50C4EBBED245D887B629FC511AE8D9E0DBEDE25B7C345A3` |
| `R4/source_aligned/ega4-errata-addenda-list3.tex` | `54DA3739811AF72128CDA534B43193A3FBEBDC6A94B7CD93E7DF3EB26CD42E3C` |

### Inline projection callsites

| Volume | Callsites |
|---|---|
| EGA 0 | `ega0-2.tex:58`; `ega0-3.tex:141`; `ega0-4.tex:29`; `ega0-5.tex:35,98,162,248`; `ega0-6.tex:330,365`; `ega0-7.tex:412`; `ega0-17.tex:659` |
| EGA I | `ega1-4.tex:345`; `ega1-6.tex:244`; `ega1-9.tex:650`; `ega1-10.tex:334,442,1423,1427` |

### Separately evidenced official items

| Item | Authority evidence |
|---|---|
| EGA I §7.3.8, `G/ega1/ega1-7.tex:377-380`, paragraph replaced by EGA II errata | EGA II p.218 crop SHA `A4B635F2F46237242845048E0AE260357DC794F181069E5ED714AE1C5BDF2D2B`; p.219 crop SHA `82D3AF3D2646BFD3AB5C01A8EF717F841E291344E16D5C2F694E4856BC4AC9AC` |
| EGA I §4.4.5, `G/ega1/ega1-4.tex:345`, “B is an A-algebra” → “A is a B-algebra” | EGA I p.125 crop SHA `19055BEC1A1046C9BCB4BDD2BAF0CA519E4C7B3D994BC29E9BCC6EB9EB14E823` |

Authority-page locators were not separately recorded in the located ledgers
for the other inline official-errata callsites. No new source audit was made to
fill those gaps.
