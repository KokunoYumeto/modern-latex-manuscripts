#!/usr/bin/env python3
"""Create the initial immutable, hash-chained P29-KO-U03 difficulty prefix."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
LEDGER = HERE / "DIFFICULTY_LEDGER.jsonl"
ZERO = "0" * 64
RECORDED = "2026-07-18T21:39:21+02:00"
AUTHORITY = (
    "sealed P31 A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F; "
    "exact U03 1CD2F142F472BE2A590EC8AACA45CEB49966A09FE803CC410D138B3F7BDE7458"
)


def payload_hash(record: dict) -> str:
    payload = {key: value for key, value in record.items() if key != "record_hash"}
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest().upper()


base = [
    {
        "difficulty_id": "CJK-KO-P29-U03-HARD-001",
        "source_locator": "lane active claim and work registry before U03 synchronization",
        "target_locator": "00_lane_control current-state fields",
        "symptom": "The active claim and registry still said U01/line 25 after U02 had already closed and been delivered.",
        "cause_evidence": "CJK-KO-P29-008 and -009 fixed the next cursor at line 41, while the two control files retained their original U01 wording.",
        "attempted_approaches": ["Read-only audit compared current controls against the append-only decision cursor.", "Preserved the stale state in an explicit correction-history section before advancing current fields."],
        "rejected_approaches": ["Trust the stale registry as current authority.", "Erase the old cursor without documenting the correction."],
        "state": "resolved",
        "resolution_or_hold": "Active claim and registry now state U01/U02 closed, U03 lines 41-45 active, and next substantive line 47.",
        "evidence_hashes_and_tests": ["updated claim 823995061E3845E9E77EDB4A5FDD83C457C5FBA87646A5BB20CA78B0F086DABE", "updated registry 4567C33A4C668A5F0CC4BF7AE41328C586861C97912747CCDA03E56257729389", "pre-update file hashes unavailable; exact old text survives in decision context and correction history"],
        "residual_risk": "Other projections outside these two files may still carry historical cursors.",
        "recurrence_cues": ["Registry next_action names an already sealed unit.", "Claim continuation disagrees with latest decision/handoff."],
        "related_structural_ids": ["NOE-P29-KO-U03-ROOT-001"],
        "transferable_lesson": "Replay append-only decisions against mutable cursor controls before claiming the next source unit.",
        "revisit_condition": "Any control scan that reports a cursor earlier than line 47."
    },
    {
        "difficulty_id": "CJK-KO-P29-U03-HARD-002",
        "source_locator": "full-P29 lines 41-59",
        "target_locator": "U03 boundary selection",
        "symptom": "Two plausible U03 boundaries existed: the first proof-reduction stage at lines 41-45 or the complete remaining proof at lines 41-57.",
        "cause_evidence": "Line 45 closes the quotient-field/integral-closedness reduction; lines 47-57 form a much longer construction with a display, module argument, finite-field reduction, and citations.",
        "attempted_approaches": ["Compared semantic closure, control surface, and continuation locators for both candidate slices.", "Inspected printed pp.31-32 to confirm the line 45/47 transition."],
        "rejected_approaches": ["Stop at line 43 before the quotient-field reduction.", "Absorb lines 47-57 merely to maximize word count."],
        "state": "resolved",
        "resolution_or_hold": "Bounded U03 is lines 41-45; proof incompleteness and line 47 continuation are explicit everywhere.",
        "evidence_hashes_and_tests": ["exact U03 1CD2F142F472BE2A590EC8AACA45CEB49966A09FE803CC410D138B3F7BDE7458", "authority validator proves exact lines 41-45 and next line 47"],
        "residual_risk": "Readers may mistake a closed tranche for a complete proof if status language is imprecise.",
        "recurrence_cues": ["A proposed unit ends inside a sentence.", "A status file says proof complete before §2."],
        "related_structural_ids": ["NOE-P29-KO-U03-PROOF-001", "NOE-P29-KO-U03-STEP-007"],
        "transferable_lesson": "Use mathematically closed proof stages as bounded units and encode the incomplete higher-level proof state separately.",
        "revisit_condition": "Qualified review finds that line 45 cannot be understood without co-packaging line 47."
    },
    {
        "difficulty_id": "CJK-KO-P29-U03-HARD-003",
        "source_locator": "full-P29 lines 41, 43, and 45",
        "target_locator": "target TeX lines 12, 14, and 16",
        "symptom": "The German adjective endlich changes meaning among finite generation, finite extension degree, and finite module generation.",
        "cause_evidence": "Ring nouns Integritätsbereich/Unterring, field Erweiterungskörper, and Modulbasis select different mathematical senses in the same short unit.",
        "attempted_approaches": ["Applied Korean-local finite-generation and field-extension register.", "Used 유한 생성 for rings, 유한 확대 for fields, and 유한 가군 생성계 for the module claim."],
        "rejected_approaches": ["Translate every occurrence mechanically as bare 유한.", "Read endlicher Integritätsbereich as a finite-cardinality domain.", "Read Modulbasis as an independent/free basis."],
        "state": "resolved",
        "resolution_or_hold": "All three senses are explicit in the accepted target and terminology ledger.",
        "evidence_hashes_and_tests": ["accepted target TeX 0DFEE79E2DF3A81005BDAF8488E108D9E324703133D0B9548F5A54933975CC60", "independent terminology audit found the three-way distinction correct"],
        "residual_risk": "Later editors may shorten 유한 생성 back to ambiguous 유한.",
        "recurrence_cues": ["German endlich modifies a ring or algebra.", "Korean target lacks 생성 near ring-theoretic finiteness."],
        "related_structural_ids": ["NOE-P29-KO-U03-STEP-001", "NOE-P29-KO-U03-STEP-002", "NOE-P29-KO-U03-STEP-004", "NOE-P29-KO-U03-STEP-007"],
        "transferable_lesson": "Treat high-frequency adjectives as sense-disambiguation problems, not glossary substitutions.",
        "revisit_condition": "Korean specialist review proposes a more historical finite-generation register."
    },
    {
        "difficulty_id": "CJK-KO-P29-U03-HARD-004",
        "source_locator": "sealed U03 lines 43 and 45; printed p.31",
        "target_locator": "target TeX lines 14 and 16; rendered footnotes 1 and 2",
        "symptom": "The sealed TeX has two identical footnote calls, while the printed page shows two anchors sharing marker 1 and one note body.",
        "cause_evidence": "Exact TeX markup and original 1926 p.31 typography diverge despite identical semantic note text.",
        "attempted_approaches": ["Initial target draft shared one translated note across two anchors, matching print; draft TeX hash 379C3A064823F94FDACD2419F5BCF9DAA54002FC7AA99F99A231DA0DE5FBE877.", "After independent review, target was changed to two numbered translated notes to follow the sealed TeX authority."],
        "rejected_approaches": ["Silently choose one state and omit the discrepancy.", "Edit the sealed German exact source.", "Claim the printed or TeX state was externally adjudicated."],
        "state": "held",
        "resolution_or_hold": "Target follows sealed TeX with two bodies; structural and authority reports retain the printed mismatch as source-owner review debt.",
        "evidence_hashes_and_tests": ["sealed exact U03 1CD2F142F472BE2A590EC8AACA45CEB49966A09FE803CC410D138B3F7BDE7458", "printed p31 024008210DE649E1A452FBB9614DA4CE8453BC2B004233C79C9A8581951728BA", "accepted target 0DFEE79E2DF3A81005BDAF8488E108D9E324703133D0B9548F5A54933975CC60"],
        "residual_risk": "A future canonical German correction may restore the shared printed marker and require a target note merge.",
        "recurrence_cues": ["Repeated identical footnote text on one printed page.", "Canonical note numbering disagrees with scan."],
        "related_structural_ids": ["NOE-P29-KO-U03-NOTE-001", "NOE-P29-KO-U03-NOTE-002"],
        "transferable_lesson": "When source layers disagree, preserve both states, choose the declared authority for the target, and open a source-owner revisit condition.",
        "revisit_condition": "Noether owner seals a footnote correction or a source auditor adjudicates the printed/TeX mismatch."
    },
    {
        "difficulty_id": "CJK-KO-P29-U03-HARD-005",
        "source_locator": "project-generated U03 PDFs",
        "target_locator": "visual_inspection U03 PNGs",
        "symptom": "The bundled pdftoppm command wrapper failed with 'The system cannot find the path specified.'",
        "cause_evidence": "The wrapper points to native/poppler/bin/pdftoppm.cmd, while the installed executable is under native/poppler/Library/bin/pdftoppm.exe.",
        "attempted_approaches": ["Tried the advertised wrapper with relative paths.", "Loaded workspace dependency paths and located the actual Poppler executable.", "Rendered directly with the executable at 180 DPI."],
        "rejected_approaches": ["Skip visual QA because compilation succeeded.", "Install a competing Poppler copy without need."],
        "state": "resolved",
        "resolution_or_hold": "Both final German and Korean page PNGs were rendered with the located Poppler executable and visually inspected.",
        "evidence_hashes_and_tests": ["German render 4331831B0FBF2F0E4354605897598F6A8EDDDEB8C8DFD416E15B5230550A1BFD", "Korean render 42E78806891372C91FDB089A5374103B8BD8E4E7BECFC14D1C94C719F7911579", "failed wrapper-state file hash unavailable because failure emitted no artifact"],
        "residual_risk": "The wrapper remains broken for later units unless runtime packaging changes.",
        "recurrence_cues": ["pdftoppm.cmd exits immediately with path-not-found.", "Poppler wrapper directory lacks its delegated cmd."],
        "related_structural_ids": ["NOE-P29-KO-U03-ROOT-001"],
        "transferable_lesson": "Record wrapper failure, locate the bundled binary, and preserve visual acceptance rather than downgrading QA.",
        "revisit_condition": "Runtime wrapper is repaired or the direct executable path changes."
    },
    {
        "difficulty_id": "CJK-KO-P29-U03-HARD-006",
        "source_locator": "full-P29 line 45 quotient-field sentence",
        "target_locator": "target TeX line 16",
        "symptom": "The first Korean draft said 'these rings' immediately after naming fraction fields, creating a potentially circular antecedent.",
        "cause_evidence": "German grammar points back to R and S as rings without zero divisors; Korean nearest-noun resolution could instead select K and L.",
        "attempted_approaches": ["Independent read-only terminology review flagged the antecedent.", "Reworded explicitly: R and S are rings without zero divisors, hence the two fraction fields exist."],
        "rejected_approaches": ["Retain the ambiguous demonstrative.", "Add a new mathematical premise not present in the source."],
        "state": "resolved",
        "resolution_or_hold": "The final target states the intended antecedent explicitly and preserves the source implication.",
        "evidence_hashes_and_tests": ["pre-review target 379C3A064823F94FDACD2419F5BCF9DAA54002FC7AA99F99A231DA0DE5FBE877", "accepted target 0DFEE79E2DF3A81005BDAF8488E108D9E324703133D0B9548F5A54933975CC60", "independent fidelity review found no remaining mathematical error"],
        "residual_risk": "No external Korean algebra specialist has reviewed the phrasing.",
        "recurrence_cues": ["Korean demonstrative follows a change from rings to fields.", "Existence reasoning appears circular after translation."],
        "related_structural_ids": ["NOE-P29-KO-U03-STEP-003"],
        "transferable_lesson": "Resolve German pronoun antecedents explicitly when Korean noun proximity would change the mathematical argument.",
        "revisit_condition": "Qualified review identifies a different historically faithful phrasing."
    },
    {
        "difficulty_id": "CJK-KO-P29-U03-HARD-007",
        "source_locator": "full-P29 line 45 inline containment chain",
        "target_locator": "target TeX line 16 inline containment chain",
        "symptom": "The initial Korean draft promoted an inline containment chain to a display, creating avoidable structural drift.",
        "cause_evidence": "A readability choice changed the equation/display inventory even though the short chain fits inline.",
        "attempted_approaches": ["Initial draft used a display.", "Independent structural review compared the scan and exact TeX.", "Final target restored inline math."],
        "rejected_approaches": ["Keep the display without recording a target-only structural relation.", "Remove the containment chain."],
        "state": "resolved",
        "resolution_or_hold": "The accepted target preserves the chain inline; the structural index classifies it as an inline equation.",
        "evidence_hashes_and_tests": ["pre-review target 379C3A064823F94FDACD2419F5BCF9DAA54002FC7AA99F99A231DA0DE5FBE877", "accepted target 0DFEE79E2DF3A81005BDAF8488E108D9E324703133D0B9548F5A54933975CC60", "structural ID NOE-P29-KO-U03-EQ-001"],
        "residual_risk": "Full-reader layout may later require a line-break intervention.",
        "recurrence_cues": ["Source inline equation becomes target display solely for wrapping.", "Display count changes without source justification."],
        "related_structural_ids": ["NOE-P29-KO-U03-EQ-001"],
        "transferable_lesson": "Do not turn inline mathematics into a display unless layout or semantics require it; if unavoidable, index the divergence.",
        "revisit_condition": "Merged reader render shows overflow or unreadable inline wrapping."
    }
]

records: list[dict] = []
previous = ZERO
for item in base:
    record = {
        "schema_version": "1.0.0",
        "recorded_at": RECORDED,
        "time_precision": "second precision for durable recording; underlying events occurred during the preceding bounded U03 production interval",
        "work_unit": "P29-KO-U03",
        "authority": AUTHORITY,
        "target_locator": item["target_locator"],
        "related_decision_ids": ["CJK-KO-P29-010"],
        "previous_hash": previous,
        **item,
    }
    record["record_hash"] = payload_hash(record)
    previous = record["record_hash"]
    records.append(record)

serialized = "".join(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n" for record in records)
if LEDGER.exists():
    existing = LEDGER.read_text(encoding="utf-8")
    if existing != serialized:
        raise SystemExit("Refusing to overwrite a non-identical append-only ledger")
else:
    LEDGER.write_text(serialized, encoding="utf-8", newline="\n")
print(json.dumps({"records": len(records), "chain_head": previous}, ensure_ascii=False))
