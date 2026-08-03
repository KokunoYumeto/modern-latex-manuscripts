# Quality assessment of an accidentally independent AI translation of FAC

## Question

Can a source-first AI translation of a mathematically demanding paper be useful without hiding behind a generic claim that a model is "good"? This record answers only for one bounded case: FAC nos. 1--79, translated before an existing English translation was discovered and then compared unit by unit.

## Experimental boundary

The blind boundary is exact:

- no. 79 component: 4,111 bytes, SHA-256 `C685DE10A5F0CB32B55845212661C4E73FEBFBC30DBB1842D68F8874C1B09DBF`;
- cumulative TeX master at that boundary: 6,112 bytes, SHA-256 `038B973E31839A78D91F527467675AEABBCD978A6B69E49B355D306705489DFB`;
- 74-page compiled reader: 464,779 bytes, SHA-256 `0598183A783A2F8DCDB2EF021920EB1EB302FD423268A0BBC3866DE1058B4F98`.

Only after those bytes existed did the orchestrator locate the public Achinger--Krupa translation PDF and then its source archive. The public comparator identities are:

- PDF: `https://achinger.impan.pl/fac/fac.pdf`, frozen project copy 928,401 bytes, 105 pages, SHA-256 `3B3EBE76E335144D16201D3B2474311FD5A60F909A992B0D057FC5B33F39E1B5`;
- source: `https://achinger.impan.pl/fac/fac.tar.gz`, frozen project copy 73,666 bytes, SHA-256 `E38121AE17DC87469C60C9B1C2E901926DC43F425D27BB6A3AC9B6F96E3A3B57`.

The external files are not included in this deposit.

## Adjudication method

Mechanical similarity was used only to route attention. It never decided correctness. Each blind unit was reviewed with four distinct roles kept separate:

1. the French journal image as authority;
2. the corrected French TeX as a project working layer;
3. the Codex English as the blind target;
4. the Achinger--Krupa English as a target-language comparator.

Each material finding records the French, Codex, and external locators; the alternatives; the selected form; whether the difference was harmless or substantive; whether Codex English or corrected French required a change; and why. Categories distinguish independent agreement, harmless variation, beneficial external convention, external regression, Codex regression, inherited transcription deviation, and printed-source defect.

## Results

- 79/79 blind units reviewed.
- 20 units with substantive agreement and no material finding.
- 59 units with at least one material finding.
- 138 exact finding rows.
- 95/95 frozen input identities replayed with zero byte or hash mismatch.
- 0 changes to admitted Codex English required by the comparator review.
- 0 changes to corrected French required by the comparator review.

The external-lineage findings include omitted hypotheses, symbol substitutions, lost indices or superscripts, ill-typed maps, malformed TeX, broken locators, preservation of source defects without disclosure, and one weakening of "biregularly" to "birationally." Other rows record harmless or useful alternate English conventions. The ledgers, not this summary, are the evidence.

The zero-change result does not mean that the broader project never made mistakes. The self-correction ledger contains 219 append-only rows, including failed commands, stale validators, locator mistakes, source-transcription repairs, normalization-rationale repairs, and one known post-admission mathematical/translation reversal (`FAC-SELF-0065`) that was repaired and globally closed. Showing this adverse history is part of the assessment.

## Interpretation

For this one blind cohort, the independently generated Codex translation survived a complete comparison against a named external translation when disagreements were rechecked against French. This is positive evidence for the source-first workflow and for using the resulting reader as a working mathematical aid.

It is deliberately weaker than certification. The comparison is not independent peer review of every theorem and formula; the source-alignment work and the comparison were performed inside the same project; and both translations may share ordinary mathematical conventions. The result therefore supports practical confidence, not canonicity.

For readers of the related SGA and EGA corpus, the appropriate heuristic is: the work is documented enough to merit inspection and use, not permission to discard the source. Keep the original scan beside any passage on which a proof, citation, or publication depends.

## Reproducibility and audit path

The deposit includes:

- the exact blind and complete Codex readers;
- the complete source layers in a ZIP;
- the 79-row review universe and 138-row findings ledger;
- source and comparator identities;
- the full project and editorial logbook snapshots;
- the 219-row self-correction ledger;
- the complete comparison inventory, input-identity replay, and validation directly;
- a self-excluding payload manifest and package validation.

No scalar grade or model-ranking claim is encoded. A reviewer can select any unit, resolve its source and target locators, inspect the competing readings, and test the stated rationale directly against the French authority.
