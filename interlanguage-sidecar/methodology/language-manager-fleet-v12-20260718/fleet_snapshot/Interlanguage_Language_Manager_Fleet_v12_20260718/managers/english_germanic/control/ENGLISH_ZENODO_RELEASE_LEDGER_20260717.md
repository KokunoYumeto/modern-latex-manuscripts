# English / Germanic Zenodo release ledger

Live-record audit: 2026-07-17, using the public Zenodo Records API.

This ledger is controlled by the English/Germanic manager. It distinguishes
material that merely exists locally from material that is current, verified,
and actually present on Zenodo. New releases must be versions of the existing
concept records; they must not create competing concept DOIs.

## SGA

- Permanent concept DOI: `10.5281/zenodo.20410947`
- Live version audited at 2026-07-17 23:39 CEST:
  `10.5281/zenodo.21420146`.
- Live title: *SGA 5 and SGA 6: Modern LaTeX Working Editions, English
  Translations, Source Repair, and Audit Materials*.
- Live SGA 5 English reader: exact 309-page frozen PDF, SHA-256
  `176759209CD284F1DD6D3E26D0C7600EC146AB01FAA637BF6F6BB97BFAA396A4`.
- Live SGA 5 support ZIP: 149,702,010 bytes, SHA-256
  `3F2B97E1480919D88020DC8DC4FD22B944D82936C647ADEFC45108D7AC0FD03C`;
  contains the exact final TeX, but also the complete original LNM 589 scan,
  exact French authority, exact legacy English witness, and fifteen
  scan-derived PNGs.
- Rights state: the public API exposes no recorded rights/license field, while
  the local SGA 5 controls explicitly excluded the scan and required parent
  rights/attribution review. Parent remediation is required; do not create a
  reflexive new version or duplicate concept.
- SGA 6: the repair108 English reader remains unsynchronized; idx662 French
  source-rescribe files are also present. The separate SGA 6 English lane
  remains active.

### Assigned production

- SGA 5 synchronization task:
  `019f711e-cac3-7a10-a0e6-dc0131799c3a`
- SGA 6 synchronization task:
  `019f711e-e434-7af2-9a4d-0cd038cfe022`

### Provenance guardrail

- SGA 5 legacy English SHA-256
  `6CEAB9D43C519EE7C9585933CC314A4807DC7A95750D1C8E8FAB2752A8EBF8CD`
  is demonstrably from the old-laptop Codex/GitHub tree. It is present in the
  historical `modern-latex-manuscripts` tree and commit
  `c914d9ce274b6e5a579a60a6a23f158b160f20b2`.
- SGA 6 complete inherited English SHA-256
  `C7C1C4DBE67D89E2CB7921B18D94CE830B5788CDE019C7CD4D27B46F46CE9625`
  comes from `SGA restart/SGA6_Indexes_Complete`; that package does not name a
  translator or model.
- SGA 6 repair108 English SHA-256
  `FFCE609E3F38124C801304F109767C60A94B9319637B0F926B9D797CCCDC74D8`
  is from the explicitly Codex-named
  `SGA6_repair033_codex_display_labels_20260621` repair tree.
- The `sga6-claude-workpass-source-rescribe-20260704` tree is the current
  French source-control authority. It is not the provenance of the inherited
  English translation.

### SGA publication gate

A new SGA Zenodo version may replace/add English payloads only after each
promoted work has all of the following:

1. editable current English TeX;
2. compiled English PDF;
3. source/page synchronization ledger with exact cursor or complete coverage;
4. terminology and rejected-choice ledger;
5. build log and rendered visual-QA evidence;
6. SHA-256 manifest;
7. `PUBLICATION_READINESS.md` and `ZENODO_PAYLOAD_MANIFEST.csv`;
8. explicit caveats that do not convert local tranche completion into a claim
   of critical-edition or whole-volume certification.

## Emmy Noether

- Permanent concept DOI: `10.5281/zenodo.20412587`
- Live version audited: `10.5281/zenodo.21406056`
- Live title: *Emmy Noether: Modern LaTeX Working Corpus and Multilingual
  Translation Drafts (v26/R822 Paper 20 Source Integration)*
- Live English cumulative:
  `01_Noether_English_Cumulative_Working_Reader_RA10_20260612.pdf`.
- Live standalone collection:
  `02_Noether_Standalone_English_Papers_01_43_WorkingDrafts_20260706.zip`.
- Both English payloads predate German v26/R822 repairs. The record itself
  states that retained English and multilingual readers are not synchronized
  to the current German source-control head.

### Noether publication gate

The next English payload must be a reviewed R822-or-later rebase, not a renamed
RA10 file. It must include current cumulative TeX/PDF, updated standalone-paper
sources/readers where promoted, a paper-by-paper German-delta disposition
ledger, build/visual-QA evidence, exact hashes, and a release manifest. The
English manager task `019f70c0-aa55-7723-b00a-1d95324af359` owns this rebase and
the final Zenodo coordination.

### Current R823 component evidence

Paper 20 is now synchronized against R823 and the primary GDZ scan in:

`03_projects/language_management/english_germanic/03_working_translations/noether_r823_paper20_english_sync_tranche001`

- final English TeX SHA-256:
  `DD84E3FCB4E13DB76D77E69BA31A82C1702BB4A9A01CDAF36A5B938FDE8BD0D2`;
- final English PDF SHA-256:
  `86540B805885B6266D112D8A393979F6E3C83C996E5EB993CBDB2432337EF492`;
- build: two successful `pdflatex` passes, zero warning/box-error matches;
- visual QA: all five final pages rendered and inspected;
- publication decision: component ready for the next standalone/source
  bundle, but the Zenodo replacement remains on hold until the remaining paper
  dispositions and the cumulative R823 English rebuild are complete.

Paper 26 is also closed against R823 in:

`03_projects/language_management/english_germanic/03_working_translations/noether_r823_paper26_english_sync_tranche002`

Its only source delta was title-final punctuation plus the cumulative page
boundary; the English title is synchronized, the one-page PDF compiled twice
without warnings and passed render review. Final TeX SHA-256:
`AE5CA88D887E8C2655636F502828EFCD01CA78F9E06D5F9C049824D476C5519E`;
final PDF SHA-256:
`E6514D0ECD57FA4E04CA5806F790513C98671596DC721A9686750D16C88405DA`.

Paper 29 is source-synchronized and closed in:

`03_projects/language_management/english_germanic/03_working_translations/noether_r823_paper29_english_sync_tranche003`

The tranche restores the source author/presentation block and footnote
placement, aligns the printed Galois-resolvent display, and corrects the
relative- and modular-invariant coefficient field from `P` to
`\overline P`. Four pages compiled twice with zero warning/box-error matches
and passed complete visual inspection. Final TeX SHA-256:
`3556B19D32AAF4A12621CB3CAB482624E66F66DB5BC5F6021DBE69B4CEF4F174`;
final PDF SHA-256:
`D1AFBBB8D3B9BE7468737797902DD2B9BEE3265DB542E3728C77B9587C754BE1`.

Paper 28 is also source-synchronized and closed in:

`03_projects/language_management/english_germanic/03_working_translations/noether_r823_paper28_english_sync_tranche004`

Its German body is unchanged; the English component propagates the title-final
period and source small-cap author styling. The one-page PDF compiled twice
with zero warning/box-error matches and passed visual inspection. Final TeX
SHA-256:
`19C7C9905D4309354D5C0752296E26C3D7993A835BCA11D85434915AE8412DED`;
final PDF SHA-256:
`F40FAFC477361D295F1B1EF02B5C6216FF82FFD6B20B4B289E3808D9191809AE`.

Paper 10 is source-synchronized and closed in:

`03_projects/language_management/english_germanic/03_working_translations/noether_r823_paper10_english_sync_tranche005`

The tranche restores the source byline and local star-note apparatus, corrects
the 1916 bibliographic year and mathematical indices/domain symbols, restores
the source-complete linear-basis footnote from the RA10 English authority, and
records every disposition in a 13-row ledger. Six pages compiled twice with
zero warning/box-error matches and passed complete visual inspection. All 20
checksum entries and all 19 manifest rows verify. Final TeX SHA-256:
`27003A6B93E6671686A32162696B73BFC22BA0769E9FE98717E32C7A0B3E1EF1`;
final PDF SHA-256:
`4DE2EDC7AC7FC008B342DAA586090DB790E15F1F8605837F393B18C28347A263`.

Paper 37 is source-complete, source-synchronized, and closed in:

`03_projects/language_management/english_germanic/03_working_translations/noether_r823_paper37_english_sync_tranche006`

The complete RA10 cumulative span replaces the materially abridged
GitHub/Codex standalone as the English base. The tranche restores the byline,
four Deuring products, mathematical indices and coefficient-field notation,
and the omitted source cross-reference. Five pages compiled twice with zero
warning/box-error matches and passed complete visual inspection. All 18
checksum entries and all 17 manifest rows verify. Final TeX SHA-256:
`6B93932EDA4A26D9DADD4D5105C17E257044584DA714866529B82172E0C75005`;
final PDF SHA-256:
`9EF810774612DD94336804CBD7DC630F7036F61D2C3EC09AF59C63EF406B53E0`.

Paper 7 is source-synchronized and closed in:

`03_projects/language_management/english_germanic/03_working_translations/noether_r823_paper07_english_sync_tranche007`

The tranche restores the printed title punctuation, byline, and all six local
star-note markers and their source text. Direct review of the primary scan and
a 650 dpi crop confirms the resolvent notation is Latin `z`; the contrary
June 29 package claim of `xi` is rejected and retained as an adverse control.
Three pages compiled twice with zero warning/box-error matches and passed
complete visual inspection. All 16 checksum entries and all 15 manifest rows
verify. Final TeX SHA-256:
`0053BA24E307FF84770C4E5F6CB6F636CE4671DAC137BC49027B86FCFD6FFE6A`;
final PDF SHA-256:
`33B4A66308B9C295A5C01991ACFD065C0C10A6CD18855BB13E24EA3CF9D8641B`.

Paper 25 is source-synchronized and closed in:

`03_projects/language_management/english_germanic/03_working_translations/noether_r823_paper25_english_sync_tranche008`

The tranche restores the original journal title, lecture/byline apparatus,
source-style congruence, and the barred Galois closure. It also repairs stale
mathematical English for greatest primary factors, fundamental ideals,
coefficient-field role, zero tuples, and the union of associated-prime zero
sets. The later collected-edition facsimile is retained as adverse evidence
because it omits the opening apparatus and the overbar. Three pages compiled
twice with zero warning/box-error matches and passed complete visual
inspection. All 16 checksum entries and all 15 manifest rows verify. Final
TeX SHA-256:
`A6A82132029FA3E88A1319D56A70DAF95CC45AB9AC448A30D65F40C23AE92533`;
final PDF SHA-256:
`F4118520E9B1FE62A9074449DBA8855F74FE2928A08A42D3E1AA93B493BDA43F`.

Paper 36 is source-synchronized and closed in:

`03_projects/language_management/english_germanic/03_working_translations/noether_r823_paper36_english_sync_tranche009`

The tranche restores the source-visible item number `2.`, small-cap author
styling, emphasis on `differential quotient` and `ideal`, and the printed
`Math. Ann.` journal form. The technical noun `the different` is retained with
independent English target-domain support, while `difference` is recorded as a
rejected false friend. The one-page PDF compiled twice with zero meaningful
diagnostic matches; PDF text extraction and the complete render passed. The
best staged source page is a legible 600 ppi witness, below the project's 650
ppi preference, so no strict high-resolution certification is claimed. Final
TeX SHA-256:
`6606AD33AC9262305417BA2C6A2ABEE2B4DB3E8BEF9343B09FA5628713CDC8A0`;
final PDF SHA-256:
`02A488B5EC92C84A5FF7F0E82D4A4499F0694E56BDB56AD4A359A68E8637E94C`.

Paper 27 is source-synchronized and closed in:

`03_projects/language_management/english_germanic/03_working_translations/noether_r823_paper27_english_sync_tranche010`

The tranche restores the source title punctuation, opening dash, and small-cap
author styling and replaces all inherited fraktur `q,p` forms with the printed
plain italic notation. It preserves the exact composition-series direction
from `q/p^i` to `q/p^{i-1}` and excludes the trailing `18 November` material
belonging to a different proceedings item. The prose was re-edited against the
German, and the historical target term `Hilbert numbers` was retained with
independent support from Macaulay's original 1913 English article title while
`Hilbert function` was rejected as a distinct concept at this locus. The
one-page PDF compiled twice with zero meaningful diagnostic matches; PDF text,
the complete render, and all three spreadsheet previews passed. The best
staged primary page is a native 600 ppi GDZ witness, below the project's 650
ppi preference. Final TeX SHA-256:
`84CD25B4BC35BC471DA6B094F626880D5AE9B7A69928EC08F45D614B0709166E`;
final PDF SHA-256:
`F8C54DD8AEB3991607225B2EF955A73E5B7CDB3FD89E23E4B9A4C980B9B81299`.

Paper 18 is source-synchronized and closed in:

`03_projects/language_management/english_germanic/03_working_translations/noether_r823_paper18_english_sync_tranche011`

The tranche restores the complete source-visible session and centered talk
headings, the full emphasized elimination-theory phrase, and the inline
primary decomposition. It corrects the inherited resultant endpoint from
`R^(m)(x_n)=0(M)` to the printed `R^(n)(x_n)` with a congruence relation and
removes several stale English calques. The one-page PDF compiled twice with
zero meaningful diagnostic matches; PDF text, the complete render, and all
three spreadsheet previews passed. The best staged primary page is a native
600 ppi GDZ witness, below the project's 650 ppi preference. All 13 manifest
rows and all 14 checksum rows verify. Final TeX SHA-256:
`DE48D9D10E742D57A58FF4917DEA8C3A533CF210CDCC3986A05B721727A6D939`;
final PDF SHA-256:
`38ECF3F7E33E08AE7CD296EBFB0099CB5887D34C7FE987D237627510714BE285`.

Paper 5 is source-synchronized and closed in:

`03_projects/language_management/english_germanic/03_working_translations/noether_r823_paper05_english_sync_tranche012`

The tranche restores the printed title punctuation and lecture note, the
small-cap author byline, and all five source-local note markers as
page-qualified labels. It distinguishes `Koeffizientenbereich` as
`coefficient domain` from `Zahlkörper` as `field of scalars`, rejecting the
modern finite-extension sense of `number field` at this locus. It also repairs
the polynomial-expression definition, the highest-degree homogeneous terms,
the attachment of the irreducible equation's coefficients to all `u`
variables, and the closing arbitrary-`n` quantifier. The contribution stops
above the printed-page-319 rule and excludes the following Haentzschel
article. The two-page PDF compiled twice with zero meaningful diagnostic
matches; complete PDF text, both page renders, and all three spreadsheet
previews passed. The four best staged original pages are native 600 ppi GDZ
witnesses, below the project's 650 ppi preference. All 14 manifest rows and
all 15 checksum rows verify. Final TeX SHA-256:
`9479CBF826CEAEEF88DE48A65BBA2D20B0D2FF7CDF71AA7D0581DD30FA8E5011`;
final PDF SHA-256:
`7D100558AF04C43617B7BF758BB99C3C01CE1AAB5AC82830F23BC933FAF96F89`.

Twelve of 43 paper dispositions are now component-ready. Thirty-one remain;
the complete English cumulative replacement therefore stays on Zenodo hold.

## Publication rule

Do not remove historical files from published versions. Publish a new version
under the existing concept DOI, give replacement files unambiguous current
names, retain status caveats, and archive the returned Zenodo record JSON plus
the exact uploaded-file SHA-256 manifest in the repository.
