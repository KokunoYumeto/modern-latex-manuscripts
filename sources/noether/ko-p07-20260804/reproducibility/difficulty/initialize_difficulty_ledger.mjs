import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
import { projectDifficultyCsv } from "./project_difficulty_csv.mjs";

const dir = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(dir, "..", "..");
const ledgerPath = path.join(dir, "DIFFICULTY_LEDGER.jsonl");
if (fs.existsSync(ledgerPath)) throw new Error("Append-only ledger already exists; initializer refuses to rewrite it");

const authorityPath = path.normalize("C:/Users/Floris/Documents/interlanguage/03_projects/noether/07_german_canon_control/candidates/NOETH-DE-ED-0001/Noether_German_NOETH-DE-ED-0001.tex");
const authoritySha = "D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB";
const intervalSha = "8C5D6E8DDF24B33C5AF719F59C4CEFA0B9CEABB61960E2AC30F888CB1206AFBC";
const pointerSha = "932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197";
const targetHashes = {
  U01: "96327E3C4C558450D56D62F2433EACFD8CD4ACFBBB8F648506BE939B01105507",
  U02: "813E2586E4FE975C51E21C74F8399CEEEA60139A9FDD833FF2C44888A6649177",
  U03: "7E12CEC2A1FB8A73AD5D9ADBD025B7B142B575FA064FC5671ED24E3C43F994A5",
  U04: "5387865AFD79A4C0B46930896944B0F8AD425715A177274EF51EA160CD2DC377",
  U05: "A1B345CAD00CD9FC8BCB8A443A0917FFCDFA9707E006A5417B136822820F24CA",
  U06: "896E625D41FEE52847CABFE77CE7426ADFE18CB8169EE8CB463D0765B5AA4AB3",
  U07: "B0AE4C26E0AE0C79111820868B09049AF18A894944CCD46EF098197A9E9BCA9C",
  U08: "DE8AD783FF83DC27A2568D4DD47A42DA55127A912F8FDEC57BF0F50DBDE38971"
};
const recordedAt = new Date().toISOString();
const common = {
  recorded_at: recordedAt,
  time_precision: "system clock recorded once for this initialization batch; millisecond field retained",
  authority_cursor: {
    pointer_id: "NOETH-DE-AUTH-v003-20260804",
    pointer_sha256: pointerSha,
    authority_path: authorityPath,
    authority_sha256: authoritySha,
    paper_interval: "whole lines 5842--5954 / local lines 1--113",
    paper_interval_sha256: intervalSha
  },
  review_state: "unchecked",
  supersession_state: "active initial record",
  related_decision_ids: [],
  test_render_review_evidence: {
    mechanical_tests: ["Frozen target byte counts and SHA-256 identities recorded", "Structural index mechanical validator available separately"],
    renders: ["None; rendering is outside the translation-producer role"],
    independent_review: ["None; no Korean checker receipt exists"]
  }
};

function rec(id, fields) {
  return {
    difficulty_id: "NOE-P07-KO-HARD-" + String(id).padStart(3, "0"),
    ...common,
    ...fields,
    previous_record_sha256: null,
    record_sha256: null
  };
}

const records = [
  rec(1, {
    work_unit: "P07 U01--U08 authority cursor",
    category: "authority_cursor_control",
    stable_symptom: "A path-only citation can silently drift when the German canon pointer advances.",
    choice_or_control: "Freeze this producer tranche to pointer NOETH-DE-AUTH-v003-20260804 plus exact authority, interval, and unit hashes.",
    alternatives_considered: ["Use only the candidate path", "Reuse the older historical whole source", "Wait for a later pointer"],
    evidence_classes: ["source_fact", "computation"],
    evidence_and_hashes: { source_facts: ["Routed pointer v003 and exact Paper 7 interval"], authority_sha256: authoritySha, paper_interval_sha256: intervalSha, target_hashes: Object.values(targetHashes), validation_evidence: ["Authority and interval hashes mechanically verified by structural builder"] },
    motivation: "A checker must be able to reproduce the exact producer cursor without treating an evolving path as immutable authority.",
    uncertainty_adverse_evidence: ["The pointer may later be superseded", "No source or scan audit was performed by this producer"],
    attempted_approaches: ["Content-addressed cursor recorded in every target header and metadata file"],
    rejected_approaches: ["Path-only authority citation"],
    resolution_state: "active_control",
    resolution_or_hold: "Active for this tranche; revisit only on an explicit superseding authority receipt.",
    consequences: ["All checking must cite v003 and the exact hashes", "Later pointer changes do not silently mutate this tranche"],
    changed_artifacts: ["SOURCE_CUSTODY.md", "CHECKER_HANDOFF_U01_U08.md", "all eight target headers"],
    residual_risk: "A later canonical correction may require a new synchronized tranche rather than silent replacement.",
    recurrence_cues: ["Pointer ID changes", "Candidate file hash changes", "Checker cites a different authority"],
    related_structural_ids: ["NOE-P07-KO-STR-001"],
    transferable_lesson: "Bind every bounded translation to both a named pointer and content hashes.",
    next_cursor: "Independent Korean checker using the exact v003 cursor"
  }),
  rec(2, {
    work_unit: "P07 interval boundary",
    category: "scope_boundary",
    stable_symptom: "Layout controls immediately after substantive text can be mistaken for translatable content or used to widen the unit.",
    choice_or_control: "Cover local lines 1--113 only; exclude blank whole line 5955 and clearpage whole line 5956.",
    alternatives_considered: ["Include the clearpage in U08", "Treat trailing controls as a ninth unit"],
    evidence_classes: ["source_fact", "computation", "editorial_inference"],
    evidence_and_hashes: { source_facts: ["Substantive interval ends at the Erlangen date line", "Following lines are blank and clearpage controls"], authority_sha256: authoritySha, paper_interval_sha256: intervalSha, target_hashes: [targetHashes.U08], validation_evidence: ["Interval byte count 8,511 and SHA-256 mechanically matched"] },
    motivation: "Keep translation coverage exact without claiming editorial authority over layout controls.",
    uncertainty_adverse_evidence: ["No broader document assembly was performed"],
    attempted_approaches: ["Explicit exclusion recorded in custody and status"],
    rejected_approaches: ["Translate or reproduce out-of-scope control matter"],
    resolution_state: "scope_resolved",
    resolution_or_hold: "Boundary fixed for this producer tranche.",
    consequences: ["Eight substantive units only", "Assembly role may later restore controls independently"],
    changed_artifacts: ["SOURCE_CUSTODY.md", "STATUS.md"],
    residual_risk: "A future assembler could misread the omission as accidental unless custody accompanies the targets.",
    recurrence_cues: ["Trailing TeX controls at work boundaries"],
    related_structural_ids: ["NOE-P07-KO-STR-051"],
    transferable_lesson: "State excluded control lines explicitly at every bounded-work edge.",
    next_cursor: "Checker confirms substantive completeness only within local lines 1--113"
  }),
  rec(3, {
    work_unit: "P07 U02--U07 terminology",
    category: "historical_semantic_distinction",
    stable_symptom: "The historical phrase ganze rationale can be mistranslated as arbitrary rational rather than polynomial.",
    choice_or_control: "Render ganze rationale as 다항 while reserving 유리 for later rationale invariants and representations.",
    alternatives_considered: ["정유리", "정식", "유리"],
    evidence_classes: ["source_fact", "editorial_inference", "model_preference"],
    evidence_and_hashes: { source_facts: ["The source contrasts ganze rationale with rationale in subsection 3"], authority_sha256: authoritySha, paper_interval_sha256: intervalSha, target_hashes: [targetHashes.U02, targetHashes.U03, targetHashes.U07], validation_evidence: ["Sense window recorded; no Korean corpus validation"] },
    motivation: "Preserve the polynomial/rational distinction central to the argument.",
    uncertainty_adverse_evidence: ["다항 is a modernizing interpretation", "No Korean historical invariant-theory corpus was consulted"],
    attempted_approaches: ["Contextual split between 다항 and 유리"],
    rejected_approaches: ["Use 유리 indiscriminately for both German forms"],
    resolution_state: "held",
    resolution_or_hold: "Producer wording retained, but independent Korean adjudication is required.",
    consequences: ["Checker must examine every occurrence across U02--U08"],
    changed_artifacts: ["TRANSLATION_CHOICES_U01_U08.md", "targets U02--U08"],
    residual_risk: "A checker may prefer 정유리 to preserve historical register.",
    recurrence_cues: ["ganze rational in older German algebra", "contrast with rationale Funktion"],
    related_structural_ids: ["NOE-P07-KO-STR-010", "NOE-P07-KO-STR-037", "NOE-P07-KO-STR-045"],
    transferable_lesson: "Create an explicit historical sense window before translating older uses of rational.",
    next_cursor: "Korean checker adjudicates the polynomial/rational contrast"
  }),
  rec(4, {
    work_unit: "P07 U01, U03--U06, U08 terminology",
    category: "terminology_consistency",
    stable_symptom: "volles System names a finite polynomial generating family, while the Korean draft alternates 완전계 and 완전 불변식계.",
    choice_or_control: "Retain the producer variation visibly and require the checker to unify or justify it.",
    alternatives_considered: ["생성계", "완비계", "완전 불변식계 throughout"],
    evidence_classes: ["source_fact", "editorial_inference", "model_preference"],
    evidence_and_hashes: { source_facts: ["The source states that every invariant is polynomially expressible in finitely many named invariants"], authority_sha256: authoritySha, paper_interval_sha256: intervalSha, target_hashes: [targetHashes.U01, targetHashes.U03, targetHashes.U05, targetHashes.U06, targetHashes.U08], validation_evidence: ["Variation disclosed; no self-review or Korean checker"] },
    motivation: "Avoid silently pretending that a contested technical label has already been standardized.",
    uncertainty_adverse_evidence: ["완전계 may suggest completeness rather than generation", "생성계 may be mathematically clearer but less source-literal"],
    attempted_approaches: ["Short form in introductory prose and explicit form in theorem statements"],
    rejected_approaches: ["Silent post-production normalization without review"],
    resolution_state: "held",
    resolution_or_hold: "Independent checker must decide one consistent policy.",
    consequences: ["Terminology inconsistency remains deliberate reviewer-visible debt"],
    changed_artifacts: ["TRANSLATION_CHOICES_U01_U08.md", "CHECKER_HANDOFF_U01_U08.md"],
    residual_risk: "Unchecked publication could alternate terms for the same object.",
    recurrence_cues: ["volles System", "vollständiges System", "generating family"],
    related_structural_ids: ["NOE-P07-KO-STR-005", "NOE-P07-KO-STR-017", "NOE-P07-KO-STR-034", "NOE-P07-KO-STR-035", "NOE-P07-KO-STR-045"],
    transferable_lesson: "Expose terminology variation to the checker instead of silently normalizing it.",
    next_cursor: "Korean checker selects and documents the complete-system term"
  }),
  rec(5, {
    work_unit: "P07 U02--U03 terminology",
    category: "trap_prone_source_form",
    stable_symptom: "Größenreihe can attract the misleading literal reading magnitude sequence.",
    choice_or_control: "Use 변수열 for the ordered tuples of transformed variables.",
    alternatives_considered: ["변수행", "변수 묶음", "양의 열"],
    evidence_classes: ["source_fact", "editorial_inference", "model_preference"],
    evidence_and_hashes: { source_facts: ["The source explicitly lists x_1 through x_n as the elements of each Reihe"], authority_sha256: authoritySha, paper_interval_sha256: intervalSha, target_hashes: [targetHashes.U02, targetHashes.U03], validation_evidence: ["Sense window recorded; no Korean corpus evidence"] },
    motivation: "Keep the tuple/row meaning and avoid analytic-sequence connotations.",
    uncertainty_adverse_evidence: ["변수열 can still suggest a sequence", "변수행 may better fit multisymmetric terminology"],
    attempted_approaches: ["Use 열 with immediate element-level context"],
    rejected_approaches: ["Literal magnitude-based wording"],
    resolution_state: "held",
    resolution_or_hold: "Producer choice awaits Korean mathematical review.",
    consequences: ["Checker should compare terminology used for multisymmetric functions"],
    changed_artifacts: ["TRANSLATION_CHOICES_U01_U08.md"],
    residual_risk: "The chosen noun may obscure row-wise symmetry.",
    recurrence_cues: ["Größenreihe", "Reihe of transformed variables"],
    related_structural_ids: ["NOE-P07-KO-STR-008", "NOE-P07-KO-STR-013"],
    transferable_lesson: "Translate the mathematical referent, not the everyday cognate, for historical row terminology.",
    next_cursor: "Korean checker tests 변수열 against local invariant-theory usage"
  }),
  rec(6, {
    work_unit: "P07 U03--U04 terminology",
    category: "trap_prone_source_form",
    stable_symptom: "einförmig can be confused with homogeneous or uniform even though the source defines a one-row-per-summand condition.",
    choice_or_control: "Use 단일형 and retain the explicit source sense window.",
    alternatives_considered: ["일형", "단일행형", "동차", "균일형"],
    evidence_classes: ["source_fact", "editorial_inference", "model_preference"],
    evidence_and_hashes: { source_facts: ["The source says each summand contains only one row"], authority_sha256: authoritySha, paper_interval_sha256: intervalSha, target_hashes: [targetHashes.U03, targetHashes.U04], validation_evidence: ["Definition-level structural records NOE-P07-KO-STR-013 and 020"] },
    motivation: "Prevent collision with degree homogeneity.",
    uncertainty_adverse_evidence: ["단일형 is a producer coinage without Korean corpus confirmation"],
    attempted_approaches: ["Term immediately accompanied by the defining clause"],
    rejected_approaches: ["동차, because the source condition is not degree homogeneity"],
    resolution_state: "held",
    resolution_or_hold: "Term requires independent Korean adjudication.",
    consequences: ["Checker may replace it globally while preserving the sense window"],
    changed_artifacts: ["TRANSLATION_CHOICES_U01_U08.md"],
    residual_risk: "A reader may not recognize the historical multisymmetric term.",
    recurrence_cues: ["einförmig in symmetric functions of rows"],
    related_structural_ids: ["NOE-P07-KO-STR-013", "NOE-P07-KO-STR-019", "NOE-P07-KO-STR-020"],
    transferable_lesson: "When a source defines a technical adjective locally, index that definition alongside the lexical choice.",
    next_cursor: "Korean checker approves or replaces 단일형"
  }),
  rec(7, {
    work_unit: "P07 U03, U06--U07 terminology",
    category: "mixed_loan_choice",
    stable_symptom: "Resolvente has several competing Korean calques and can be confused with a splitting field.",
    choice_or_control: "Use 갈루아 레졸벤트 for the displayed product polynomial.",
    alternatives_considered: ["갈루아 해소식", "갈루아 분해식", "갈루아 결해식"],
    evidence_classes: ["source_fact", "editorial_inference", "model_preference"],
    evidence_and_hashes: { source_facts: ["The source defines Phi as a product and names its coefficients"], authority_sha256: authoritySha, paper_interval_sha256: intervalSha, target_hashes: [targetHashes.U03, targetHashes.U06, targetHashes.U07], validation_evidence: ["Displayed polynomial indexed at NOE-P07-KO-STR-015"] },
    motivation: "Avoid falsely equating the polynomial with its splitting field while keeping the historical technical object visible.",
    uncertainty_adverse_evidence: ["레졸벤트 is a global modern loan", "No Korean terminology source was consulted"],
    attempted_approaches: ["Loanword plus explicit displayed definition"],
    rejected_approaches: ["분해체, because the object here is a polynomial"],
    resolution_state: "held",
    resolution_or_hold: "Checker must choose a Korean standard based on local evidence.",
    consequences: ["All later cross-references must follow the checker choice"],
    changed_artifacts: ["TRANSLATION_CHOICES_U01_U08.md"],
    residual_risk: "Readers may expect a different established Korean resolvent term.",
    recurrence_cues: ["Resolvente", "resolvent polynomial"],
    related_structural_ids: ["NOE-P07-KO-STR-015", "NOE-P07-KO-STR-017", "NOE-P07-KO-STR-035", "NOE-P07-KO-STR-037"],
    transferable_lesson: "Name the object type in the sense window whenever a loanword has field/polynomial ambiguity.",
    next_cursor: "Korean checker supplies local-language evidence for resolvent terminology"
  }),
  rec(8, {
    work_unit: "P07 U01 terminology",
    category: "modernization_choice",
    stable_symptom: "Modulbasis can attract either the Korean module term 가군 or the global loan 모듈.",
    choice_or_control: "Use 가군 기저 정리 provisionally.",
    alternatives_considered: ["모듈 기저 정리", "가군의 기저 정리"],
    evidence_classes: ["source_fact", "model_preference"],
    evidence_and_hashes: { source_facts: ["The source explicitly cites Hilbert's Theorem von der Modulbasis"], authority_sha256: authoritySha, paper_interval_sha256: intervalSha, target_hashes: [targetHashes.U01], validation_evidence: ["No Korean terminology validation"] },
    motivation: "Prefer the conventional Korean mathematical noun while preserving the exact theorem reference.",
    uncertainty_adverse_evidence: ["Historical theorem naming may conventionally retain 모듈", "No Korean bibliography was consulted"],
    attempted_approaches: ["Hangul technical term with citation context"],
    rejected_approaches: ["Treat basis as a bare vector-space basis"],
    resolution_state: "held",
    resolution_or_hold: "Korean checker must verify theorem naming.",
    consequences: ["Title-level terminology may need global replacement"],
    changed_artifacts: ["TRANSLATION_CHOICES_U01_U08.md"],
    residual_risk: "The wording may not match Korean histories of Hilbert's basis theorem.",
    recurrence_cues: ["Modulbasis", "Hilbert basis theorem"],
    related_structural_ids: ["NOE-P07-KO-STR-005"],
    transferable_lesson: "Separate object terminology from conventional theorem naming.",
    next_cursor: "Korean checker checks local theorem-title convention"
  }),
  rec(9, {
    work_unit: "P07 U05--U06 terminology",
    category: "cross_locale_term",
    stable_symptom: "Potenzsumme and Ordnung invite South/North Korean lexical divergence and an order-versus-ordering ambiguity.",
    choice_or_control: "Use 거듭제곱합 and 군의 위수; keep 멱합, 누승합, and 차수 as explicitly held alternatives.",
    alternatives_considered: ["멱합", "누승합", "군의 차수", "군의 크기"],
    evidence_classes: ["source_fact", "editorial_inference", "model_preference"],
    evidence_and_hashes: { source_facts: ["S_mu is defined as a power sum", "h is explicitly the group order"], authority_sha256: authoritySha, paper_interval_sha256: intervalSha, target_hashes: [targetHashes.U05, targetHashes.U06], validation_evidence: ["No ko-KP evidence or reviewer"] },
    motivation: "Keep the displayed power-sum meaning and finite-group cardinality distinct.",
    uncertainty_adverse_evidence: ["North Korean standard is entirely unverified", "멱합 may be more concise in South Korean texts"],
    attempted_approaches: ["Use explanatory modern South-oriented wording"],
    rejected_approaches: ["Treat Ordnung as ordering", "Claim ko-KP equivalence"],
    resolution_state: "held",
    resolution_or_hold: "Both terminology and locale decisions await independent evidence.",
    consequences: ["No ko-KP publication claim is permitted"],
    changed_artifacts: ["TRANSLATION_CHOICES_U01_U08.md", "CHECKER_HANDOFF_U01_U08.md"],
    residual_risk: "Locale-specific mathematical vocabulary may differ materially.",
    recurrence_cues: ["Potenzsumme", "Ordnung of a finite group", "ko-KP routing"],
    related_structural_ids: ["NOE-P07-KO-STR-027", "NOE-P07-KO-STR-031", "NOE-P07-KO-STR-034", "NOE-P07-KO-STR-035"],
    transferable_lesson: "Do not infer North Korean terminology from South Korean or CJK cognates.",
    next_cursor: "Independent ko-KR checker; separate ko-KP evidence if later authorized"
  }),
  rec(10, {
    work_unit: "P07 U07--U08 terminology",
    category: "disciplinary_sense_collision",
    stable_symptom: "rationale Darstellung can be mistaken for representation theory rather than rational expression in generators.",
    choice_or_control: "Use 유리 표현 and state that the sense is rational expressibility, not representation theory.",
    alternatives_considered: ["유리적 표시", "유리적 표현", "유리 표현론"],
    evidence_classes: ["source_fact", "editorial_inference", "model_preference"],
    evidence_and_hashes: { source_facts: ["The paragraph discusses quotient and rational expression through coefficients"], authority_sha256: authoritySha, paper_interval_sha256: intervalSha, target_hashes: [targetHashes.U07, targetHashes.U08], validation_evidence: ["Argument structure indexed at NOE-P07-KO-STR-037 through 043"] },
    motivation: "Keep the algebraic-expression sense distinct from group representation.",
    uncertainty_adverse_evidence: ["유리 표현 remains potentially ambiguous without context"],
    attempted_approaches: ["Contextual wording around quotient and coefficients"],
    rejected_approaches: ["유리 표현론"],
    resolution_state: "held",
    resolution_or_hold: "Independent checker must decide whether 유리적 표시 is clearer.",
    consequences: ["Section 3 terminology must remain consistent with U08 theorem references"],
    changed_artifacts: ["TRANSLATION_CHOICES_U01_U08.md"],
    residual_risk: "A modern reader could still hear Darstellung as representation.",
    recurrence_cues: ["Darstellung paired with rational ausdrücken"],
    related_structural_ids: ["NOE-P07-KO-STR-037", "NOE-P07-KO-STR-043", "NOE-P07-KO-STR-045"],
    transferable_lesson: "Use neighboring verbs and mathematical operations to disambiguate Darstellung.",
    next_cursor: "Korean checker adjudicates rational-expression terminology"
  }),
  rec(11, {
    work_unit: "P07 U01--U08 language standard",
    category: "evidence_dominance_and_locale_control",
    stable_symptom: "Sino-xenic forms can look mutually validating across CJK languages even when no Korean evidence exists.",
    choice_or_control: "Record Mandarin-Simplified dominance debt qualitatively; use Hangul-first prose; hold all Hanja and ko-KP claims.",
    alternatives_considered: ["Infer Korean terms from Chinese cognates", "Insert unreviewed Hanja glosses", "Treat ko-KR as authorizing ko-KP"],
    evidence_classes: ["editorial_inference", "model_preference"],
    evidence_and_hashes: { source_facts: ["No Chinese target was inspected", "No Korean terminology corpus or checker was used"], authority_sha256: authoritySha, paper_interval_sha256: intervalSha, target_hashes: Object.values(targetHashes), validation_evidence: ["All terminology explicitly marked provisional"] },
    motivation: "Prevent false cross-language authority and false readiness.",
    uncertainty_adverse_evidence: ["Korean local-language evidence remains absent", "Candidate Hanja may be historically or institutionally variable"],
    attempted_approaches: ["Hangul-first body", "Candidate Hanja only in metadata", "Separate ko-KR and ko-KP holds"],
    rejected_approaches: ["Use Mandarin-Simplified prevalence as a scalar or vote"],
    resolution_state: "active_control",
    resolution_or_hold: "Control remains active until Korean evidence and separate locale review exist.",
    consequences: ["No Hanja standard or ko-KP equivalence is claimed", "Chinese evidence cannot close Korean review"],
    changed_artifacts: ["TRANSLATION_CHOICES_U01_U08.md", "CHECKER_HANDOFF_U01_U08.md", "STATUS.md"],
    residual_risk: "The draft still reflects model priors shaped by globally dominant CJK terminology shelves.",
    recurrence_cues: ["Sino-xenic cognates", "Simplified-Chinese search dominance", "cross-locale publication"],
    related_structural_ids: ["NOE-P07-KO-STR-001", "NOE-P07-KO-STR-051"],
    transferable_lesson: "Treat dominance debt as a hard qualitative control, never as evidence of Korean correctness.",
    next_cursor: "Independent Korean-language evidence review; separate ko-KP review only if authorized"
  }),
  rec(12, {
    work_unit: "P07 U07 embedded note",
    category: "nested_note_and_formula_boundary",
    stable_symptom: "A single NoetherSrcNote spans argumentative prose, two displays, and a closing conclusion, creating high risk of lost brace scope or main-text misclassification.",
    choice_or_control: "Keep the entire source note as one TeX note while indexing its internal prose and displays separately.",
    alternatives_considered: ["Flatten the note into main prose", "Split it into multiple notes", "Move formulas outside the note"],
    evidence_classes: ["source_fact", "computation", "editorial_inference"],
    evidence_and_hashes: { source_facts: ["Source local lines 94--108 form one note", "The note contains displays at local lines 95--98 and 100--107"], authority_sha256: authoritySha, paper_interval_sha256: intervalSha, target_hashes: [targetHashes.U07], validation_evidence: ["Structural parent/child records NOE-P07-KO-STR-039 through 043", "Target SHA-256 mechanically fixed"] },
    motivation: "Preserve the source note topology without claiming formula correctness.",
    uncertainty_adverse_evidence: ["No compilation or brace-scope render was performed", "No formula review was performed"],
    attempted_approaches: ["Direct TeX preservation with internal structural indexing"],
    rejected_approaches: ["Editorially restructure the note"],
    resolution_state: "held",
    resolution_or_hold: "TeX topology is producer-preserved but must be checked, compiled, and rendered by other roles.",
    consequences: ["Checker handoff explicitly calls out the note and both displays"],
    changed_artifacts: ["targets\\Noether_P07_Korean_U07_UNCHECKED.tex", "reproducibility\\structural\\STRUCTURAL_INDEX.jsonl"],
    residual_risk: "A latent brace or formula-token issue cannot be excluded without forbidden downstream checks.",
    recurrence_cues: ["NoetherSrcNote spanning displays", "closing brace after multiple paragraphs"],
    related_structural_ids: ["NOE-P07-KO-STR-039", "NOE-P07-KO-STR-040", "NOE-P07-KO-STR-041", "NOE-P07-KO-STR-042", "NOE-P07-KO-STR-043"],
    transferable_lesson: "Index nested note internals without flattening their source topology.",
    next_cursor: "Independent checker, then separately authorized compile/render role"
  }),
  rec(13, {
    work_unit: "P07 U07 source-authored criticism",
    category: "claim_provenance_control",
    stable_symptom: "The source author's statement that Weber's proof is not valid could be misreported as a producer-discovered German-canon defect.",
    choice_or_control: "Translate and classify it as source-authored mathematical criticism, not as a new canon finding.",
    alternatives_considered: ["Open a German defect", "Omit the criticism", "Present it as producer validation"],
    evidence_classes: ["source_fact", "editorial_inference"],
    evidence_and_hashes: { source_facts: ["The criticism occurs inside the source note at local line 94"], authority_sha256: authoritySha, paper_interval_sha256: intervalSha, target_hashes: [targetHashes.U07], validation_evidence: ["Provenance retained in structural note record NOE-P07-KO-STR-039"] },
    motivation: "Distinguish source fact from producer judgment and avoid polluting the German-canon defect route.",
    uncertainty_adverse_evidence: ["The mathematical criticism itself was not checked by this producer"],
    attempted_approaches: ["Source-attributed translation only"],
    rejected_approaches: ["Treat the source's claim as external or human validation by this session"],
    resolution_state: "scope_resolved",
    resolution_or_hold: "No canon packet is created unless an independent checker identifies a separate German defect.",
    consequences: ["Canon owner is not contacted for this source-authored passage"],
    changed_artifacts: ["CHECKER_HANDOFF_U01_U08.md", "reproducibility\\difficulty\\DIFFICULTY_LEDGER.jsonl"],
    residual_risk: "Later summaries could strip the attribution and overstate validation.",
    recurrence_cues: ["Source text criticizes another proof", "historical authorial correction or dispute"],
    related_structural_ids: ["NOE-P07-KO-STR-037", "NOE-P07-KO-STR-039"],
    transferable_lesson: "Log claim provenance explicitly: source-authored criticism is not a newly adjudicated defect.",
    next_cursor: "Independent Korean checker checks translation of the attribution and criticism"
  })
];

let previous = null;
const lines = [];
for (const r of records) {
  r.previous_record_sha256 = previous;
  const unhashed = JSON.stringify(r);
  const digest = crypto.createHash("sha256").update(unhashed, "utf8").digest("hex").toUpperCase();
  r.record_sha256 = digest;
  lines.push(JSON.stringify(r));
  previous = digest;
}
fs.writeFileSync(ledgerPath, lines.join("\n") + "\n", { encoding: "utf8", flag: "wx" });
const projected = projectDifficultyCsv();
const report = {
  initialized_at: recordedAt,
  operation: "append-only ledger initialization; no prior record rewritten",
  record_count: records.length,
  latest_difficulty_id: records[records.length - 1].difficulty_id,
  chain_head_sha256: previous,
  csv_projected_records: projected,
  actual_p07_write_or_tool_failure_records: 0,
  note: "No P07 write/tool failure occurred before initialization; none was invented."
};
fs.writeFileSync(path.join(dir, "INITIALIZATION_REPORT.json"), JSON.stringify(report, null, 2) + "\n", "utf8");
console.log(JSON.stringify(report));
