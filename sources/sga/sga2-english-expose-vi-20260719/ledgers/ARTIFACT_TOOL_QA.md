# Artifact Tool QA — SGA 2 Exposé VI cumulative checkpoint

Status: **PASS**.

The seven CSV evidence ledgers were loaded as spreadsheet artifacts, inspected over their full populated ranges, and rendered as readable PNG previews. All seven previews were viewed at original resolution. Preview images are public-payload evidence; the tool's internal inspection objects are represented here by their content hashes.

| CSV | Records | Columns | Full range | Inspection SHA-256 | Preview bytes | Preview SHA-256 |
|---|---:|---:|---|---|---:|---|
| `COMPONENT_UNIT_INTEGRATION.csv` | 6 | 25 | A1:Y7 | C438FA8467C53E9E346DA9D930FCFA1DCC370EC6B19BEEC0A57EDC792F40BA38 | 204871 | 1237BE63564A6447D5528B1BEBA9432FD7FBDCF3715C734E96F8F8D195EAC949 |
| `AUTHORITY_ARTIFACT_HASHES.csv` | 3 | 14 | A1:N4 | A14461CE2100F0BA73F2A69D296056D056617F306DD6B4DD85B83B26E77375A1 | 66759 | D73A311503A15ED3CEAE5CCB4586A465D113DF5790982484FC829C5C79AC4EDC |
| `SOURCE_ALIGNMENT_COVERAGE.csv` | 16 | 23 | A1:W17 | 0F7DDF616852739279CAEC17507926B7C423FA3EA2F11140A918AD74534BF1E2 | 289125 | 925096D51ADDECB9D01BC2555D9FA19A512B040403C60FE05D1F650A3C4D6212 |
| `FORMULA_SYMBOL_NOTE_STRUCTURE_COMPARISON.csv` | 30 | 25 | A1:Y31 | D0FC092D50A1C9E50971B459B3DF561D0A7582D4F798B301CC6D0FCA4CBAF2E7 | 294295 | 27442E1E8744D98EA1FAE791044FFFE66A75D586ACF1238F41F39056919041A6 |
| `TERMINOLOGY_NORMALIZATION_ADVERSE_CHOICES.csv` | 20 | 27 | A1:AA21 | CEE3586E4E867ADD35416BB4CC56EE7F49019F44931DA67985BD096DD32DBA0E | 279124 | 4FD96334AC6E84BF239E76F64D1C8EA5FAE474223A9A7D721AAFF70605AF9405 |
| `BUILD_RENDER_EVIDENCE.csv` | 18 | 18 | A1:R19 | 75BD9BEF803E5069D0EAF4D9B9D5E8DD9FC7FD19CDD757521B5819FAB8A0CEF7 | 270069 | 7876D40FDBC87EF40EF0AB443D40DF7A693EEF436BB0882DCC9911E65BE96859 |
| `INDEPENDENT_PACKAGE_REVIEW.csv` | 17 | 18 | A1:R18 | 71B90A561445E293398BEF7863560E99AD4021623F2F54752A35A809E65C7CF8 | 247176 | CAACD0167648E85E6889420DE4A480F27EC61108B2B4F465669D8F4C8CD68F35 |

Total: 7 CSV files, 110 data records. The previews show complete headers and representative rows without clipped columns, unreadable type, or cell-render failures. The larger ledgers use a bounded 12-record preview after the header; exact full-range inspection covered every populated cell.

The independent preflight additionally confirmed UTF-8 without BOM, rectangularity, unique primary IDs, spreadsheet-formula safety, exact component and authority artifact hashes, JSONL parseability, schema-required fields, hierarchy/revision closure, and reference closure.

The proposed-public payload manifest was then inspected separately over `A1:O35`: 34 records, 15 columns, unique IDs, rectangularity, formula safety, and 34/34 path/byte/hash checks passed. Its representative `A1:O13` preview was viewed at original resolution; the local-only preview is 224121 bytes with SHA-256 `DB123BC079D120CA51B3609854739DED75A315FE2FBB1F3D01C04168548CBBDB`.
