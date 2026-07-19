# Public revision history - SGA 1 through duplicate-numbered I.9.2

Local-build and public-checkpoint revisions are separate series.

- local r1: rejected stale-root-auxiliary read; 10 files / 704,238 bytes;
  pass-three log 29,475 bytes, SHA-256
  94986DDA6759B92005A1DAC98073515E7AE2E61647F36DED88D82C87E446F189.
- local r2: rejected malformed copy destination that omitted every fragment;
  5 files / 57,000 bytes; pass-one console 7,836 bytes, SHA-256
  295CEB7DBDBD382C33827C3D6D8446A2A192DF93803AF1C78354D375ECED14D3.
- local r3: rejected despite clean visible pages because passes two and three
  reported duplicate PDF destination proposition.1.9.2; PDF 545,835 bytes,
  SHA-256 658F8E130164B11676C45FFEA21B33D22AF712114B310FB0F542B01B9B58373B;
  pass-three log 28,857 bytes, SHA-256
  53A5FDDE5A52F9FBC26605F41DB81E6BAE9C85890FEE9A3F23CA68B4826E8B66.
- local r4: clean successor with distinct destinations proposition.1.9.2 and
  proposition.1.9.2.second; reviewed PDF 545,957 bytes, SHA-256
  A5C59DB6149BA82A443F919DFCF5952277D994FFF07B2B614A34BB150525C904.
- public r1: locally frozen as 137 files / 8,015,605 bytes with ordered
  inventory digest
  2F4347737B09AAA2E0456CCC607DE2C905E65CD2FC23176CCAEACADB6870D5BA.
  It is now rejected under explicit nonpublication HOLD. It lacked the corrected
  r2 release controls: final exact repins for all seven editable files, initial
  and final full 19-input-CSV identity gates, deterministic public-projection
  identity, current Zenodo concept/version routing, and an explicit cumulative
  audited-unit count. Its immutable directory is preserved and never refilled.
- public r2 attempt1: rejected before rename/handoff when the staged verifier
  failed verbatim: "Publication-readiness DOI/recheck text missing: never mint
  a duplicate record." The warning existed across a case-sensitive line wrap.
  Preserved surfaces are publication sibling
  SGA1_English_Expose_I_opening_through_I_9_2_source_audited_checkpoint_20260719_r2.__rejected_attempt1_prefreeze_verifier_phrase_wrap__
  (138 files / 8,104,240 bytes; inventory digest
  3F1484AB7FFFE303619EFDAB5841F43BA368AB1B209796504E7AFA231686FCA6),
  build/I9_2_PUBLIC_R2_REJECTED_ATTEMPT1_PREFREEZE_VERIFIER_PHRASE_WRAP_BUILD_20260719
  (17 files / 763,460 bytes;
  digest 7BCDB1CCCC393374C576E38C4F4786402479328A72A86C4CB954E3FA671ED80B),
  and both 16-file / 6,346,588-byte render directories with digest
  1B65B5CE7DC5F3A4B40FF9DB5694824F5D0BFF1F1183E3D5D864C2A834185793.
  Its verifier was 23,047 bytes / SHA-256
  0C7AB407B826EE6DD2FF22348F9B5C25505FFFB7C274EB3BA02171830231B8D0.
  Attempt1 remains rejected and unclosed; attempt2 does not refill or erase it.
- public r2 attempt2: fresh corrected successor with new staging/build/render
  paths. It becomes the sole local dispatch candidate only after every source,
  CSV, build, render, anchor, machine, privacy, DOI, manifest, pre-freeze
  verifier, final rename, and post-freeze verifier gate passes. At that point
  it supersedes r1 before the custody handoff is emitted.

The local rejected r1/r2/r3 build surfaces and rejected public r1 checkpoint are
preserved and non-promotable. No archive acceptance, upload, DOI update,
publication, or remote readback is claimed. The source boundary remains corrected
French lines 556-1721; line 1722 is excluded.