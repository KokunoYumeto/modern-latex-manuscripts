# Ring Review Packet — v0.1 (no verdict)
2026-07-04. For Interslavic-authority review. This packet presents evidence and questions; it makes no decision and changes no text. Framing per program policy: *the audit found that the status-quo `kolco` family has high internal corpus pressure and high East-Slavic continuity, while the West/South shelf supplies competitor-only evidence; the row is therefore the highest-leverage authority-review item in the corpus.*
Changelog v0.1 (same day): TeX-feed patch applied — corpus is NOT perfectly uniform on `kolco`; Paper-25 `prsten` exception added (§3a, question 7); weighted-intelligibility scores added to enclosures. Patch source: ChatGPT web grind (SLAVIC_LATEX_RING_OCCURRENCE_AUDIT); occurrence verified locally (paper25 interslavic v001, L68).

## 1. One-page memo

The corpus is a complete Interslavic rendering of Emmy Noether's collected papers (Latin 579pp + Cyrillic 603pp, render-validated). Its term for *ring* (German *Ring*) is `kolco`, chosen early via the Ukrainian/Russian evidence path (uk кільце, ru кольцо) and used consistently; 41 term rows are compounds of it (noetherian ring, group ring, quotient ring, …), so one review question governs the whole family. A 20-source West/South Slavic reference shelf (Czech 6, Polish 6, Slovak 1, Slovenian 2, Serbian 1, Croatian 2, Bulgarian 2 — university/institute texts, hash-pinned) was searched for branch forms: `kolco` has **zero** attestations there, while each branch attests its own lexeme. The project's own logbook states the term "is not derivable mechanically from a majority vote" and marks it reviewer-sensitive. The question for review is which surface (or variant policy) best serves family-central passive recognizability for mathematical prose, given the evidence below.

## 2. Candidate table (attested forms only; no invented candidates)

| Candidate | Where attested (shelf + corpora) | Lexeme notes |
| --- | --- | --- |
| `kolco` (status quo) | East only: uk кільце, ru кольцо (canonical corpora) | 'small wheel/ring' metaphor; East technical standard |
| `okruh` | Czech, Slovak sources | technical standard cs/sk; **adverse relation: collides with uk/ru округ 'district' (false-friend risk East)** |
| `pierścień` | Polish sources | same lexeme family as prsten (PSl *pьrstenь* 'finger-ring') |
| `prsten` | Croatian/Serbian sources; bg пръстен same family | everyday 'finger-ring' + technical use; largest single-lexeme coalition (pl+hr+sr+bg); East cognates перстень exist with jewellery register |
| `kolobar` | Slovenian sources | sl technical standard; 'ring/annulus' |

## 3. Current corpus pressure (status quo facts)

- 41 machine-readable rows in the `kolco` family (enumerated: F10 audit, flag F10-3).
- 1,182 rendered pages carry the term; revision = mechanical rebuild via the established pipeline (term migration is a known, tested operation in this corpus; open-revision policy is a standing principle of the lane).
- Consistency pressure: earlier papers define, later papers inherit; any change is corpus-wide or doublet-based, not piecemeal.

## 2a. Community-dictionary evidence (checked 2026-07-04; closes pre-ship requirement 1)

The community word list (medzuslovjansky/database sheet, 2026-07-04 snapshot, in enclosures) carries BOTH lexemes as general-language entries, with no mathematical sense marked for either:
- **`koljce` — "ring"**: ru кольцо, uk кільце, **pl pierścień, cs prsten, sk prsteň, sl prstan, hr prsten, sr прстен, bg пръстен**. Note (i): the community citation form is *koljce*, not the corpus's *kolco* — even if the lexeme stays, the surface may need normalization; a question for the reviewer. Note (ii): the community's own translation row maps the koljce entry onto the prsten-family in every West/South language — the decoding asymmetry the shelf evidence shows is built into the community's own lexicon.
- **`pŕstėnj` — "ring"**: ru кольцо/перстень, uk перстень/каблучка, same W/S row as above. So the prsten-family is community-sanctioned ISV vocabulary, not an import.
- `obrųčka` — "wedding ring" (separate lexeme, not relevant to algebra).

**Register verification (closes pre-ship requirement 2):** перстень/перстн- occurs 0 times in the corpus's own Ukrainian and Russian mathematical translations (vs кільце/кольцо ≈1,025/1,029 occurrences) — in East Slavic the prsten-family is exclusively jewellery-register. The register-shift concern for East readers (question 6) is therefore real but bounded: the cognate is recognizable, its register cue is non-mathematical, exactly as German *Ring*/English *ring* read to lay ears.

## 3a. Internal non-uniformity (TeX-feed finding, locally verified)

The corpus overwhelmingly uses `kolco`/`колцо` and its compounds for algebraic ring terminology (TeX-feed counts: kolc* 1059 occurrences in 125 Latin files; колц* 983 in 111 Cyrillic files), with strong internal corpus pressure. However, the feed contains a localized Paper 25 exception: `prsten`/`прстен` occurs twice, in a passage where residue classes modulo a prime ideal are said to form a ring without zero divisors and are then extended to a residue-class field (verified: `translations/paper25/interslavic/v001`, L68; Cyrillic sibling likewise). This exception is not a verdict against `kolco`; it is evidence that the review question should explicitly include variant policy. The reviewer should decide whether the `prsten` trace is accidental inconsistency, an acceptable local doublet, or a sign that the ring-family surface should be reconsidered.

## 4. West/South competitor evidence (file-pinned, now with definitional contexts)

Two independent probes of the same 20-source shelf (stem-level backfill: WS_WITNESS_BACKFILL_v1_20260704.json; page-level context windows: NON_RU_UK_SLAVIC_CONTEXT_WINDOWS_20260704.md). The context windows show each branch *defining* the ring concept with its native lexeme — definitional attestation, the strongest competitor evidence class:

- **cs** `okruh` — definitional: "Definice. Okruhem R rozumíme pětici (R, +, −, ·, 0)…" (Charles Univ. algebra 2021, p.2); ~425 occurrences across 6 Czech sources incl. a group-rings thesis (182) and Karlin lectures (54).
- **sk** `okruh` — chapter-level: "5 Okruhy … Homomorfizmy okruhov, podielové telesá" (Slovak abstract algebra text, 114 occ).
- **pl** `pierścień` — definitional: "Definicja pierścienia … nazywamy pierścieniem wtedy i tylko wtedy gdy (R,+,0) jest grupą abelową…" (IMPAN lecture 3, p.2); ~350 occ across 5 Polish sources (UJ algebra alone 250).
- **sr** `prsten` — definitional: "Definicija 1: Komutativan prsten sa jedinicom je struktura (A, +, ·)…" (Belgrade Algebra I lecture 9, 81 occ).
- **hr** `prsten` — PMF Split rings text (title-level: "prsteni"); math.hr structures overview.
- **sl** `kolobar` — massive: 939 occurrences in the Ljubljana algebra introduction + 24 in the commutative-algebra sheets ("noetherski kolobar").
- **bg** `пръстен` — Sofia lectures (rings lecture 7).
- **`kolco`: zero occurrences in all 20 sources, both probes.**
- **be** `кольца` — NEW (2026-07-04, underrepresented-branch shelf): the 1993 Minsk Russian–Belarusian mathematical dictionary carries a full ring-compound family (51 entries on the ring page: фактарыяльнае кольца, цэлазамкнутае кольца, кольца эндамарфізмаў…). Third East-Slavic standard, also kolco-family — East-branch coherence for the lexeme is now three-for-three, while W/S remains competitor-only. Dictionary-grade native source; OCR caveat noted in manifest.
- **mk** `прстен` — NEW (same shelf): the UKIM mathematical lexicon (trilingual mk/en/ru) uses prsten definitionally, 172 occurrences ("Vo prsten (R; +, ·)… a.g. na prstenot"; legacy font transliteration handled). **The prsten coalition is now five standards: pl + hr + sr + bg + mk.**
- **hsb**: the shelf's "Domowina math terminology 2008" PDF is in fact a publisher's catalog (source mislabeled — flagged in shelf audit); Upper Sorbian mathematical witnesses remain an open gap (soblex/Institute term databases are the live leads).

## 5. Known adverse relations (typed; vetoes are not scores)

- `okruh` → East false-friend risk: uk/ru округ 'district/okrug' (same surface, unrelated concept). Recorded as do-not-use candidate for family-central surface unless review overrides.
- `prsten` → East register shift: uk/ru перстень = 'ring (jewellery)'; recognizable cognate, wrong register cue for algebra. (Same metaphor as German *Ring*/English *ring*; whether this is a defect or a feature is a review question, not a data question.)
- `kolco` → West/South opacity: no technical attestation; everyday cognates (pl kółko 'little wheel/circle', etc.) may cue 'circle', adjacent-concept risk vs *krąg/kružnica* families. [flagged for reviewer; not shelf-verified]

## 6. Questions for the reviewer

1. For a pan-Slavic mathematical register, which surface do you judge most passively recognizable as *algebraic ring* across cs/sk/pl/hr/sr/bg/sl/uk/ru readers: kolco, prsten, okruh, kolobar — or none without a doublet?
2. Does the Interslavic community's existing lexicon fix the algebra sense (and if so, to which lexeme family)? The project defers to community usage where it exists.
3. If continuity with 1,182 rendered pages argues for keeping `kolco` as running surface, is a mandatory first-use doublet + glossary crosswalk (kolco = prsten = okruh = kolobar) sufficient for W/S readers?
4. If a migration is preferred, which target and which doublet policy?
5. Should compounds follow the head term automatically, or do any compounds (e.g. group ring, quotient ring) warrant separate treatment?
6. Is the East register-shift concern for `prsten` (перстень jewellery reading) material in mathematical context, in your judgment?
7. The corpus already contains a localized `prsten` occurrence in Paper 25 (§3a). Should this be normalized back to `kolco`, preserved as a contextual doublet, or treated as evidence for a broader `kolco`/`prsten` variant policy?

## 7. Enclosures
- WS_WITNESS_BACKFILL_v1_20260704.json (hit evidence, file-pinned)
- F10_EAST_SLAVIC_SKEW_AUDIT_20260704.md (flag context: 41-row family)
- WEIGHTED_INTELLIGIBILITY_SCORES_v2_20260704.md (four-weighting sensitivity analysis; ring is weight-sensitive: prsten-coalition ahead under equal-branch and dependence-corrected weights, kolco ahead under population weighting — the choice depends on declared cohort weights, which is itself a review input)
- SLAVIC_LATEX_RING_OCCURRENCE_AUDIT_20260704.{md,json} (internal-consistency counts; Paper-25 exception)
- RING_TERM_DECISION_MEMO_20260704.md (option analysis — labelled review proposal, superseded in tone by this packet's no-verdict framing)
- SLAVIC_TRIANGULATION_REFERENCE_LOG.md excerpt (the lane's own 2026-06-24 assessment)
- SOURCE_USE_POLICY.md + honest-limits page (what this evidence is and is not; the TeX feed is internal-consistency evidence, not witness material)
