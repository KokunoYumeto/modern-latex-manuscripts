from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path


HERE = Path(__file__).resolve().parent
TRANCHE = HERE.parents[1]
LEDGER = HERE / "DIFFICULTY_LEDGER.jsonl"
AUTHORITY_CURSOR = r"sealed P31 A48CB5CD...CF814F; U02 normalized full-P29 lines 25-39, SHA B7EF8853...29DCAC; line 40 blank; next substantive cursor line 41, 2. \srcspaced{Beweis des Endlichkeitskriteriums.}"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def canonical_hash(record: dict) -> str:
    body = {k: v for k, v in record.items() if k != "record_sha256"}
    return digest(json.dumps(body, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def shown(path: Path) -> str:
    try:
        return path.relative_to(TRANCHE).as_posix()
    except ValueError:
        return str(path)


def current(path: Path, role: str) -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return {"path_or_reference": shown(path), "hash_or_test": f"SHA-256:{digest(path.read_bytes())};bytes={path.stat().st_size}", "role": role, "evidence_kind": "current_file"}


def historical(reference: str, sha: str, role: str, bytes_count: int | None = None) -> dict:
    suffix = f";bytes={bytes_count}" if bytes_count is not None else ""
    return {"path_or_reference": reference, "hash_or_test": f"SHA-256:{sha}{suffix}", "role": role, "evidence_kind": "historical_hash"}


def unavailable(reference: str, reason: str, role: str) -> dict:
    return {"path_or_reference": reference, "hash_or_test": f"UNAVAILABLE:{reason}", "role": role, "evidence_kind": "unavailable_historical_state"}


def computation(reference: str, result: str, role: str) -> dict:
    return {"path_or_reference": reference, "hash_or_test": result, "role": role, "evidence_kind": "computation"}


def main() -> int:
    if LEDGER.exists():
        raise SystemExit(f"REFUSING TO OVERWRITE append-only ledger: {LEDGER}")
    now = datetime.now().astimezone().replace(microsecond=0).isoformat()
    common = {"schema_version": "1.0.0", "recorded_at": now, "occurrence_time": {"value": "2026-07-18", "precision": "date_only"}, "authority_cursor": AUTHORITY_CURSOR, "related_decision_ids": ["CJK-KO-P29-001"], "supersedes": [], "supersession_state": "not_applicable"}

    full = TRANCHE / "source/Noether_Paper29_German_P31_Sealed_exact_slice.tex"
    source = TRANCHE / "source/Noether_Paper29_German_P31_U02_Rationalbasis_exact_lf.tex"
    gtex = TRANCHE / "source/Noether_Paper29_German_P31_U02_control.tex"
    gpdf = TRANCHE / "source/Noether_Paper29_German_P31_U02_control.pdf"
    glog = TRANCHE / "source/Noether_Paper29_German_P31_U02_control.log"
    gpng = TRANCHE / "visual_inspection/Noether_Paper29_German_U02_control_compact.png"
    old_g1 = TRANCHE / "visual_inspection/Noether_Paper29_German_U02_control-1.png"
    old_g2 = TRANCHE / "visual_inspection/Noether_Paper29_German_U02_control-2.png"
    ktex = TRANCHE / "ko/Noether_Paper29_Korean_U02_v001.tex"
    kpdf = TRANCHE / "ko/Noether_Paper29_Korean_U02_v001.pdf"
    klog = TRANCHE / "ko/Noether_Paper29_Korean_U02_v001.log"
    kpng = TRANCHE / "visual_inspection/Noether_Paper29_Korean_U02_v001.png"
    kextract = TRANCHE / "qa/Noether_Paper29_Korean_U02_extracted.txt"
    shelf = TRANCHE / "evidence/KOREAN_NATIVE_EXAMPLE_CORPUS_U01.csv"
    terms = TRANCHE / "evidence/TERMINOLOGY_LEDGER_U01.csv"
    adverse = TRANCHE / "evidence/ADVERSE_EVIDENCE_LEDGER_U01.csv"
    crosswalk = TRANCHE / "evidence/CJKV_CROSSWALK_P29_KO_U01.csv"

    records = [
        {
            **common,
            "issue_id": "CJK-KO-P29-U02-HARD-001",
            "work_unit": "P29-KO-U02 exact source boundary and continuation",
            "structural_ids": ["NOE-P29-KO-U02-ROOT-001", "NOE-P29-KO-U02-SEC-001", "NOE-P29-KO-U02-COR-001"],
            "source_locator": "exact full-P29 normalized lines 25-39; line 40 blank; line 41 starts subsection item 2",
            "target_locator": "U02 source lines 1-15 and Korean substantive lines 12-40",
            "difficulty_class": "blank_separator_and_next_substantive_cursor",
            "symptom": "Stopping at the corollary leaves a blank full-source line before the next substantive unit, so a naive next-line cursor would point to line 40 rather than line 41.",
            "severity": "high",
            "discovery_channel": "normalized full-slice boundary comparison",
            "cause": {"evidence": "U02 equals full-source lines 25-39 exactly; full line 40 is empty and line 41 begins item 2, Beweis des Endlichkeitskriteriums.", "inference": "The continuation must distinguish the first excluded byte/line from the next substantive translation cursor."},
            "attempted_approaches": [
                {"approach": "Record line 40 alone as the next production cursor.", "outcome": "rejected", "evidence": "It is only a paragraph separator and does not identify the next unit."},
                {"approach": "Pin U02 to lines 25-39 and separately assert blank line 40 plus substantive line 41.", "outcome": "resolved", "evidence": "Both structural and difficulty validators reproduce the exact boundary."}
            ],
            "resolution_state": "resolved",
            "resolution_or_workaround": "Preserve raw hashes and normalized line equality, then name line 41 explicitly as U03 while retaining line 40 as an excluded blank separator.",
            "evidence_artifacts": [current(full, "exact full-P29 slice"), current(source, "normalized U02 source"), computation("U02 boundary validator", "PASS:full_lines_25_39_equal;PASS:line_40_blank;PASS:line_41_item_2", "reproducible cursor computation")],
            "residual_risk": "A future source refresh may shift line numbers despite unchanged text.",
            "recurrence_cues": ["unit ends immediately before a blank line", "cursor records only first excluded line", "authority head changes"],
            "transferable_lesson": "Record both the excluded separator and the next substantive line; line-number cursors require pinned authority hashes.",
            "future_check": "Revisit and rerun before U03 or any sealed-authority refresh.",
            "changed_artifacts": ["source/Noether_Paper29_German_P31_U02_Rationalbasis_exact_lf.tex", "evidence/structural_index_u02/STRUCTURAL_INDEX.jsonl"],
            "validation_state": {"internal": "Exact normalized line comparison and authority hashes pass.", "external_human": "No external human source-boundary review claimed."},
            "continuation_or_revisit": "Revisit before U03 and after every German authority change."
        },
        {
            **common,
            "issue_id": "CJK-KO-P29-U02-HARD-002",
            "work_unit": "U02 proof footnote-marker placement",
            "structural_ids": ["NOE-P29-KO-U02-STEP-003", "NOE-P29-KO-U02-NOTE-002", "NOE-P29-KO-U02-DSP-002"],
            "source_locator": "source line 13, note attached to inline P<K relation before the overline-P chain",
            "target_locator": "final Korean line 30, balanced footnote inline before display lines 31-33",
            "difficulty_class": "footnote_marker_stranded_after_display",
            "symptom": "An early Korean layout conversion placed the proof's field-inclusion footnote marker after a display, visually stranding it from the P<K relation it explains.",
            "severity": "high",
            "discovery_channel": "rendered-page structural fidelity inspection",
            "cause": {"evidence": "The German source keeps P<K and its note inline; Korean introduced display blocks for nearby relations. The first affected proof marker was initially left after a display.", "inference": "Moving inline mathematics into displays without moving note anchors atomically can detach a note from its semantic host."},
            "attempted_approaches": [
                {"approach": "Leave the marker after the display because the note text still appeared on the page.", "outcome": "rejected", "evidence": "Visual presence does not preserve structural attachment."},
                {"approach": "Attach the footnote command to the inline P<K premise before the overline-P display and rebuild.", "outcome": "resolved", "evidence": "Final line 30 contains one balanced footnote; display line 31 follows it; extraction and render pass."}
            ],
            "resolution_state": "resolved",
            "resolution_or_workaround": "Keep P<K inline with its balanced footnote command, then start the display; index note and display separately with exact locators.",
            "evidence_artifacts": [
                unavailable("overwritten pre-hash Korean U02 state with stranded marker", "not hashed before in-place repair; no digest invented", "honest historical failure state"),
                historical("post-placement-repair/pre-independent-review Korean TeX", "757942045B900ED62288C9B94986D4156114887A6C4A6E9C79FF79F57CBAD26D", "first hashed repaired TeX", 5942),
                historical("post-placement-repair/pre-independent-review Korean PDF", "D396477CDA351685D4885692CAF518E7A99DCCCADF71B7F9CE321D69CFB9481D", "first hashed repaired PDF", 66372),
                historical("post-placement-repair/pre-independent-review Korean render", "3745EE1BFA0551F4BE6F2681A966872AD0C65A2CD87057F3AB80915CB4DA3935", "first hashed repaired render", 561221),
                current(ktex, "final Korean TeX with inline note anchor"), current(kpdf, "final rebuilt Korean PDF"), current(kpng, "final inspected Korean render")
            ],
            "residual_risk": "Later reformatting could again move a footnote command across a display boundary.",
            "recurrence_cues": ["inline source relation converted to display", "footnote command appears after display terminator", "note marker survives but lacks adjacent host"],
            "transferable_lesson": "Treat a note anchor and the exact phrase/relation it annotates as one structural unit during display transformations.",
            "future_check": "Revisit after any proof/display/footnote edit; retry the structural validator and render inspection.",
            "changed_artifacts": ["ko/Noether_Paper29_Korean_U02_v001.tex", "ko/Noether_Paper29_Korean_U02_v001.pdf", "visual_inspection/Noether_Paper29_Korean_U02_v001.png"],
            "validation_state": {"internal": "Balanced locator, extracted text, build, and visual layout pass in final files.", "external_human": "No external human typography review claimed."},
            "continuation_or_revisit": "Revisit after any U02 layout change; do not invent a hash for the overwritten stranded state."
        },
        {
            **common,
            "issue_id": "CJK-KO-P29-U02-HARD-003",
            "work_unit": "U02 standalone German control pagination",
            "structural_ids": ["NOE-P29-KO-U02-ROOT-001", "NOE-P29-KO-U02-COR-001"],
            "source_locator": "German U02 control wrapping exact source lines 1-15",
            "target_locator": "superseded 11pt two-page control versus current compact one-page control",
            "difficulty_class": "nearly_blank_second_control_page",
            "symptom": "The first 11pt German control broke onto two pages with only a small tail on page 2, weakening visual comparison and contact-sheet utility.",
            "severity": "medium",
            "discovery_channel": "PDF page-count check and two-page render inspection",
            "cause": {"evidence": "Historical PDF was 37,980 bytes; retained page renders show a substantive first page and nearly blank 29,229-byte second-page image. Compact 10pt/2.15cm control is one A4 page.", "inference": "Standalone wrapper typography, not source length or missing content, caused the orphaned tail."},
            "attempted_approaches": [
                {"approach": "Accept the two-page control because compilation succeeded.", "outcome": "rejected", "evidence": "Successful compilation did not make the near-empty second page useful for visual parity."},
                {"approach": "Compact only the disposable German wrapper to 10pt, 2.15cm margins, and 0.35em paragraph spacing without editing the exact source unit.", "outcome": "resolved", "evidence": "Current PDF is one A4 page and its complete compact render is retained."}
            ],
            "resolution_state": "resolved",
            "resolution_or_workaround": "Change only standalone wrapper layout parameters, rebuild, extract, and render; keep old PDF/render hashes and both page images.",
            "evidence_artifacts": [
                unavailable("superseded 11pt German U02 control TeX", "wrapper overwritten before hashing", "unavailable historical wrapper source"),
                historical("superseded 11pt German U02 control PDF", "9487BDA552D89D5CFF995DB79B96DDFD7B8D72F30837933ADC612EFE6FAABAA2", "historical two-page PDF", 37980),
                current(old_g1, "surviving superseded page-1 render"), current(old_g2, "surviving nearly blank page-2 render"),
                current(gtex, "current compact wrapper"), current(gpdf, "current one-page control PDF"), current(glog, "current compact build log"), current(gpng, "current one-page control render")
            ],
            "residual_risk": "A font/runtime change may reintroduce pagination drift; compact control typography is not publication typography.",
            "recurrence_cues": ["standalone control adds a nearly empty final page", "source and control page counts diverge unexpectedly", "wrapper parameter change"],
            "transferable_lesson": "Source-control wrappers may be compacted for visual QA only when the included authority text remains byte-identical and both old and new render evidence survives.",
            "future_check": "Revisit after font, TeX runtime, wrapper, or source changes and require one-page visual completeness again.",
            "changed_artifacts": ["source/Noether_Paper29_German_P31_U02_control.tex", "source/Noether_Paper29_German_P31_U02_control.pdf", "visual_inspection/Noether_Paper29_German_U02_control_compact.png"],
            "validation_state": {"internal": "Historical hashes, surviving page renders, current hashes, clean build, and one-page count are recorded.", "external_human": "No external human layout review claimed."},
            "continuation_or_revisit": "Revisit after any wrapper/runtime change; preserve the two superseded page renders."
        },
        {
            **common,
            "issue_id": "CJK-KO-P29-U02-HARD-004",
            "work_unit": "U02 independent fidelity review refinements",
            "structural_ids": ["NOE-P29-KO-U02-FORM-001", "NOE-P29-KO-U02-STEP-002", "NOE-P29-KO-U02-NOTE-002"],
            "source_locator": "source lines 3, 11, and 13",
            "target_locator": "intermediate target lines 14, 22, 30 versus final target at the same structural locations",
            "difficulty_class": "post_build_idiom_premise_and_note_structure_refinement",
            "symptom": "A separately run review found no substantive mathematical error but identified a more natural first-formulation idiom, an implicit algebraicity premise worth making explicit in the t<n step, and a tighter note-host structure.",
            "severity": "medium",
            "discovery_channel": "independent internal/model source review after compiled/rendered checkpoint",
            "cause": {"evidence": "The hashed intermediate TeX/PDF/render passed build and visual QA; final changes revised line 14 wording, exposed the premise in line 22, and integrated P<K plus note on line 30.", "inference": "Build and visual gates cannot detect all idiomatic or inferential-explicitness improvements; an independent pass has complementary value."},
            "attempted_approaches": [
                {"approach": "Freeze the first source-checked rendered target without an independent pass.", "outcome": "rejected", "evidence": "The review found nonfatal but material clarity refinements."},
                {"approach": "Treat the review suggestions as proof that the intermediate translation was substantively wrong.", "outcome": "rejected", "evidence": "The reviewer explicitly found no substantive error."},
                {"approach": "Apply bounded idiom/premise/note refinements, then rebuild, re-extract, rerender, and reindex all locators/hashes.", "outcome": "resolved", "evidence": "Final TeX/PDF/PNG hashes and zero-warning log are pinned; structural validator passes."}
            ],
            "resolution_state": "resolved",
            "resolution_or_workaround": "Preserve the intermediate hash triplet, adopt only source-supported refinements, and rerun every downstream integrity gate.",
            "evidence_artifacts": [
                historical("pre-independent-review Korean U02 TeX", "757942045B900ED62288C9B94986D4156114887A6C4A6E9C79FF79F57CBAD26D", "superseded reviewed intermediate", 5942),
                historical("pre-independent-review Korean U02 PDF", "D396477CDA351685D4885692CAF518E7A99DCCCADF71B7F9CE321D69CFB9481D", "superseded reviewed intermediate PDF", 66372),
                historical("pre-independent-review Korean U02 render", "3745EE1BFA0551F4BE6F2681A966872AD0C65A2CD87057F3AB80915CB4DA3935", "superseded reviewed intermediate render", 561221),
                current(ktex, "final reviewed Korean TeX"), current(kpdf, "final reviewed Korean PDF"), current(klog, "final zero-warning-pattern build log"), current(kpng, "final reviewed render"), current(kextract, "final Korean text extraction")
            ],
            "residual_risk": "Review remains internal/model-based rather than external Korean mathematical validation; exact historical terminology is still held.",
            "recurrence_cues": ["first compiled translation treated as editorially final", "implicit proof premise omitted in target", "review suggestion applied without downstream hash refresh"],
            "transferable_lesson": "Run an independent source pass after build/render, classify findings by severity, and preserve the pre-review artifact hashes even when no substantive error exists.",
            "future_check": "Revisit upon external Korean mathematical review or any target edit; rerun all hashes and structural validation.",
            "changed_artifacts": ["ko/Noether_Paper29_Korean_U02_v001.tex", "ko/Noether_Paper29_Korean_U02_v001.pdf", "ko/Noether_Paper29_Korean_U02_v001.log", "qa/Noether_Paper29_Korean_U02_extracted.txt", "visual_inspection/Noether_Paper29_Korean_U02_v001.png"],
            "validation_state": {"internal": "Independent internal/model review plus rebuild/extraction/render/index validation passed.", "external_human": "No external human Korean or mathematical validation is claimed."},
            "continuation_or_revisit": "Revisit on external review or any U02 target change."
        },
        {
            **common,
            "issue_id": "CJK-KO-P29-U02-HARD-005",
            "work_unit": "U02 Korean historical terminology evidence",
            "structural_ids": ["NOE-P29-KO-U02-FORM-001", "NOE-P29-KO-U02-FORM-002", "NOE-P29-KO-U02-NOTE-001", "NOE-P29-KO-U02-STEP-003"],
            "source_locator": "Rationalbasis, irreduzibles System, Transzendenzgrad, Vereinigungskörper in source lines 3, 5, 7, 11, 13, 15",
            "target_locator": "유리 기저, 기약계, 초월 차수, 합성체 in target lines 14-40",
            "difficulty_class": "historical_korean_term_and_local_evidence_debt",
            "symptom": "The local Korean shelf supports core field/module/algebra vocabulary and finite-generation semantics but does not independently attest every exact Noether/Steinitz-era compound used in U02.",
            "severity": "high",
            "discovery_channel": "Korean-only evidence and adverse-evidence carry-forward audit",
            "cause": {"evidence": "Existing Korean records support 체, 중간체-related register, 가군, 유한생성, and 정수확장, while the U01 terminology/adverse ledgers explicitly hold Rationalbasis and historical compounds; no DPRK source is present.", "inference": "U02 renderings are coherent working ko-KR choices but not externally certified historical terminology."},
            "attempted_approaches": [
                {"approach": "Use the frozen Chinese P29 vocabulary as authority for Korean compounds.", "outcome": "rejected", "evidence": "CJK governance prohibits cross-language authorization and treats Mandarin dominance risk qualitatively."},
                {"approach": "Promote every compositional Korean term because the theorem is internally consistent.", "outcome": "rejected", "evidence": "Internal consistency does not supply local historical usage evidence."},
                {"approach": "Retain source labels where needed, use coherent provisional ko-KR renderings, and keep exact-term/DPRK review debt explicit.", "outcome": "held", "evidence": "Source and target remain traceable while unsupported promotion is prevented."}
            ],
            "resolution_state": "held",
            "resolution_or_workaround": "Use the current source-labelled or context-controlled ko-KR terminology only as an internal working decision; make no ko-KP, community, or specialist-certification claim.",
            "evidence_artifacts": [current(shelf, "local Korean evidence shelf"), current(terms, "existing P29 Korean term decisions and sense windows"), current(adverse, "historical-term and DPRK adverse evidence"), current(crosswalk, "qualitative dominance-debt and lexical-attractor controls"), current(ktex, "current U02 contextual usage")],
            "residual_risk": "기약계, 유리 기저, and 합성체 may require different historical-specialist wording; North-Korean standards are unverified.",
            "recurrence_cues": ["exact U02 compound lacks Korean evidence ID", "modern textbook sense substituted for historical sense", "ko-KR choice generalized to ko-KP", "Mandarin cognate used as readiness evidence"],
            "transferable_lesson": "Carry evidence debts forward by exact term and sense; later-source consistency can constrain a choice but cannot replace local-language attestation or review.",
            "future_check": "Retry Korean invariant/field-theory sources and revisit on qualified Korean or DPRK review.",
            "changed_artifacts": ["ko/Noether_Paper29_Korean_U02_v001.tex", "evidence/difficulty_ledger_u02/DIFFICULTY_LEDGER.jsonl"],
            "validation_state": {"internal": "Source labels, contextual senses, and inherited evidence limitations were checked.", "external_human": "No external Korean specialist or DPRK review exists."},
            "continuation_or_revisit": "Revisit on independent Korean historical-algebra evidence or human review; retry during later P29 units."
        },
        {
            **common,
            "issue_id": "CJK-KO-P29-U02-HARD-006",
            "work_unit": "U02 source-target structural parity",
            "structural_ids": ["NOE-P29-KO-U02-STEP-002", "NOE-P29-KO-U02-DSP-001", "NOE-P29-KO-U02-STEP-003", "NOE-P29-KO-U02-DSP-002", "NOE-P29-KO-U02-DSP-003", "NOE-P29-KO-U02-NOTE-002"],
            "source_locator": "source lines 11 and 13 contain all relations inline inside two long proof paragraphs",
            "target_locator": "target proof lines 22-38 split prose around three display blocks and retain note inline at line 30",
            "difficulty_class": "non_isomorphic_inline_to_display_parity",
            "symptom": "A flat line- or paragraph-ordinal alignment would either lose three target displays, duplicate whole source paragraphs, or attach the second note to the wrong structural host.",
            "severity": "high",
            "discovery_channel": "manual source-target structure audit after display and footnote repair",
            "cause": {"evidence": "German source uses inline relations in lines 11/13; Korean uses exact display blocks 23-27, 31-33, and 35-37 and splits surrounding prose.", "inference": "Source-target parity is relational and many-to-one/one-to-many, not line-isomorphic."},
            "attempted_approaches": [
                {"approach": "Align same-type units by ordinal position only.", "outcome": "failed", "evidence": "It cannot represent source inline spans becoming three target displays or preserve the note host."},
                {"approach": "Index each target display against its entire source paragraph.", "outcome": "rejected", "evidence": "That obscures exact mathematical provenance and creates false duplicate coverage."},
                {"approach": "Use hierarchical proof steps plus exact source character spans and target line ranges for all three displays; index notes separately.", "outcome": "workaround", "evidence": "Sixteen-record structural index validates hierarchy, hashes, display delimiters, and note balance with zero errors."}
            ],
            "resolution_state": "workaround",
            "resolution_or_workaround": "Represent proof paragraphs as parent steps and each display/note as a child linked to an exact source substring; retain the non-isomorphic mapping as explicit evidence.",
            "evidence_artifacts": [current(source, "inline German structural authority"), current(ktex, "three-display Korean target"), current(HERE.parent / "structural_index_u02/STRUCTURAL_INDEX.jsonl", "canonical relational parity index"), computation("U02 structural validator", "PASS:records=16;displays=3;notes=2;errors=0", "structure/parity validation")],
            "residual_risk": "The mapping is internally reviewed; a future prose reflow can shift target locators even with unchanged semantics.",
            "recurrence_cues": ["source inline formula becomes target display", "one source paragraph maps to several target blocks", "footnote crosses display boundary", "flat CSV treated as hierarchy authority"],
            "transferable_lesson": "When translation changes mathematical layout, index exact spans and parent relations rather than forcing paragraph or line identity.",
            "future_check": "Revisit and regenerate after any U02 TeX change; validate JSONL before trusting the CSV projection.",
            "changed_artifacts": ["evidence/structural_index_u02/STRUCTURAL_INDEX.jsonl", "evidence/structural_index_u02/STRUCTURAL_INDEX.csv", "evidence/structural_index_u02/STRUCTURAL_INDEX_METADATA.json"],
            "validation_state": {"internal": "Schema, hierarchy, hash, delimiter, note, cursor, and CSV checks pass.", "external_human": "No external human structural-parity review claimed."},
            "continuation_or_revisit": "Revisit after any source/target structural edit or before an archive handoff."
        }
    ]

    chained, previous = [], None
    for sequence, record in enumerate(records, 1):
        ordered = {"schema_version": record.pop("schema_version"), "ledger_sequence": sequence, "issue_id": record.pop("issue_id"), "record_sha256": "", "previous_record_sha256": previous, **record}
        ordered["record_sha256"] = canonical_hash(ordered)
        previous = ordered["record_sha256"]
        chained.append(ordered)
    with LEDGER.open("x", encoding="utf-8", newline="\n") as handle:
        for record in chained:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(f"initialized={len(chained)} recorded_at={now} head={chained[-1]['record_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
