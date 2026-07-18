from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path


HERE = Path(__file__).resolve().parent
TRANCHE = HERE.parents[1]
LEDGER = HERE / "DIFFICULTY_LEDGER.jsonl"

SEALED_AUTHORITY_SHA256 = "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F"
AUTHORITY_CURSOR = (
    "sealed P31 cumulative authority SHA-256 "
    f"{SEALED_AUTHORITY_SHA256}; exact P29 slice 904488A1...128F; U01 lines 1-24; "
    r"next exact line 25 \subsection*{§ 1. Das Endlichkeitskriterium}"
)
SOURCE_SCAN_ROOT = Path(
    r"evidence://local-workspace/Papors\Chatnotes\CHat translates and clean\Noether Multilingual"
    r"\Noether_LocalCodex_after_WebR272_P29_p028_035_SourceAudit_20260629"
    r"\02_source_pages_p028_035_native400"
)
RUNTIME_ROOT = Path(
    r"evidence://local-user/.cache\codex-runtimes\codex-primary-runtime\dependencies"
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def canonical_record_hash(record: dict) -> str:
    without_hash = {key: value for key, value in record.items() if key != "record_sha256"}
    encoded = json.dumps(
        without_hash, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return digest(encoded)


def display_path(path: Path) -> str:
    try:
        return path.relative_to(TRANCHE).as_posix()
    except ValueError:
        return str(path)


def file_evidence(path: Path, role: str, evidence_kind: str = "current_file") -> dict:
    if not path.is_file():
        raise FileNotFoundError(path)
    return {
        "path_or_reference": display_path(path),
        "hash_or_test": f"SHA-256:{digest(path.read_bytes())};bytes={path.stat().st_size}",
        "role": role,
        "evidence_kind": evidence_kind,
    }


def historical_hash(reference: str, sha256: str, role: str) -> dict:
    return {
        "path_or_reference": reference,
        "hash_or_test": f"SHA-256:{sha256}",
        "role": role,
        "evidence_kind": "historical_hash",
    }


def computation(reference: str, result: str, role: str) -> dict:
    return {
        "path_or_reference": reference,
        "hash_or_test": result,
        "role": role,
        "evidence_kind": "computation",
    }


def main() -> int:
    if LEDGER.exists():
        raise SystemExit(
            f"REFUSING TO OVERWRITE append-only canonical ledger: {LEDGER}. "
            "Append a new chained line with a new issue ID instead."
        )

    recorded_at = datetime.now().astimezone().replace(microsecond=0).isoformat()
    common = {
        "schema_version": "1.0.0",
        "recorded_at": recorded_at,
        "occurrence_time": {"value": "2026-07-18", "precision": "date_only"},
        "authority_cursor": AUTHORITY_CURSOR,
        "related_decision_ids": ["CJK-KO-P29-001"],
        "supersedes": [],
        "supersession_state": "not_applicable",
    }

    full_source = TRANCHE / "source/Noether_Paper29_German_P31_Sealed_exact_slice.tex"
    u01_source = TRANCHE / "source/Noether_Paper29_German_P31_U01_Introduction_exact_lf.tex"
    target_tex = TRANCHE / "ko/Noether_Paper29_Korean_U01_v001.tex"
    target_pdf = TRANCHE / "ko/Noether_Paper29_Korean_U01_v001.pdf"
    target_png = TRANCHE / "visual_inspection/Noether_Paper29_Korean_U01_v001.png"
    german_pdf = TRANCHE / "source/Noether_Paper29_German_P31_U01_control.pdf"
    german_png = TRANCHE / "visual_inspection/Noether_Paper29_German_U01_control.png"
    target_log = TRANCHE / "ko/Noether_Paper29_Korean_U01_v001.log"
    source_cursor = TRANCHE / "SOURCE_VERSION_CURSOR.md"
    render_check = TRANCHE / "RENDER_CHECK.md"
    terminology = TRANCHE / "evidence/TERMINOLOGY_LEDGER_U01.csv"
    adverse = TRANCHE / "evidence/ADVERSE_EVIDENCE_LEDGER_U01.csv"
    crosswalk = TRANCHE / "evidence/CJKV_CROSSWALK_P29_KO_U01.csv"
    korean_corpus = TRANCHE / "evidence/KOREAN_NATIVE_EXAMPLE_CORPUS_U01.csv"

    records = [
        {
            **common,
            "issue_id": "CJK-KO-P29-HARD-001",
            "work_unit": "P29-KO-U01 exact German source extraction",
            "structural_ids": ["NOE-P29-KO-U01-ROOT-001"],
            "source_locator": "full P29 exact slice lines 1-24; raw slice has mixed CRLF/LF; line 25 is the section-one cursor",
            "target_locator": "source/Noether_Paper29_German_P31_U01_Introduction_exact_lf.tex lines 1-24; all Korean U01 structures depend on this frozen source",
            "difficulty_class": "line_ending_normalization_and_prefix_identity",
            "symptom": "A raw byte-prefix comparison could reject or mis-size the correct U01 because the sealed extracted P29 slice contains mixed CRLF and LF line endings while the bounded U01 is LF-normalized.",
            "severity": "high",
            "discovery_channel": "byte/hash audit plus normalized line comparison",
            "cause": {
                "evidence": "The full P29 slice contains 76 CRLF pairs and 101 LF bytes; after UTF-8-sig decoding and splitlines(), its first 24 lines exactly equal the 24-line U01 file.",
                "inference": "The discrepancy is transport/newline representation, not a source-text divergence; raw-byte prefix identity is the wrong comparison for this boundary.",
            },
            "attempted_approaches": [
                {
                    "approach": "Require the LF-normalized U01 to be a literal raw-byte prefix of the mixed-ending full slice.",
                    "outcome": "failed",
                    "evidence": "The line-ending encodings differ even though decoded lines match.",
                },
                {
                    "approach": "Normalize through UTF-8-sig decoding and splitlines(), compare exactly 24 lines, and separately assert the line-25 cursor.",
                    "outcome": "resolved",
                    "evidence": "Structural generator and validator both reproduce exact first-24-line equality and the section-one continuation.",
                },
            ],
            "resolution_state": "resolved",
            "resolution_or_workaround": "Preserve both raw file hashes, define LF-normalized line identity as the bounded extraction rule, and keep the exact next-line assertion.",
            "evidence_artifacts": [
                file_evidence(full_source, "raw full-P29 exact slice"),
                file_evidence(u01_source, "LF-normalized exact U01 prefix"),
                file_evidence(source_cursor, "durable authority and continuation cursor"),
                computation(
                    "normalized-prefix validation",
                    "PASS:first_24_lines_equal;PASS:line_25_section_cursor;raw_full_slice_CRLF_pairs=76;raw_full_slice_LF_bytes=101",
                    "reproducible boundary test",
                ),
            ],
            "residual_risk": "A later extractor may compare bytes without newline normalization or may include the trailing blank line as a substantive structural unit.",
            "recurrence_cues": [
                "raw slice and bounded unit have different byte counts despite equal decoded text",
                "mixed CRLF/LF source",
                "cursor expressed only as a remembered section name",
            ],
            "transferable_lesson": "Pin both raw hashes and a deterministic decoded-line boundary; verify the first excluded line independently.",
            "future_check": "Rerun normalized-prefix and line-25 assertions after any source-head or extraction change.",
            "changed_artifacts": [
                "source/Noether_Paper29_German_P31_U01_Introduction_exact_lf.tex",
                "SOURCE_VERSION_CURSOR.md",
                "evidence/structural_index/STRUCTURAL_INDEX.jsonl",
            ],
            "validation_state": {
                "internal": "Exact hashes and decoded-line assertions reproduced by executable validators.",
                "external_human": "No independent human source-boundary validation claimed.",
            },
            "continuation_or_revisit": "Revisit before U02 and after every German authority refresh.",
        },
        {
            **common,
            "issue_id": "CJK-KO-P29-HARD-002",
            "work_unit": "P29-KO-U01 criterion semantic fidelity repair",
            "structural_ids": ["NOE-P29-KO-U01-THM-001", "NOE-P29-KO-U01-NOTE-003"],
            "source_locator": "U01 source line 17; corroborating later full-P29 source lines 53-55",
            "target_locator": "Korean TeX line 28; superseded draft and current revision occupy the same locator",
            "difficulty_class": "finite_cardinality_and_false_free_basis_semantic_trap",
            "symptom": "The first compiled draft used 유한 정역 and 가군 기저, which could read as finite cardinality and a free/linearly independent module basis rather than finite algebra/module generation.",
            "severity": "high",
            "discovery_channel": "post-build source-fidelity review against later theorem proof language and Korean algebra evidence",
            "cause": {
                "evidence": "German line 17 uses endlich and Modulbasis historically; lines 53-55 exhibit a finite T-module generating representation with no freeness assertion. The SNU course description independently uses 유한생성 대수 and 정수확장 in Korean.",
                "inference": "The draft's compact nominal choices attracted modern cardinality/free-basis senses that Noether's argument does not license.",
            },
            "attempted_approaches": [
                {
                    "approach": "Retain draft 유한 정역 and 가군 기저 because the surrounding algebraic context might disambiguate them.",
                    "outcome": "rejected",
                    "evidence": "The terms leave two high-impact false readings available and do not expose finite generation explicitly.",
                },
                {
                    "approach": "Import wording from the frozen Mandarin-Simplified P29 translation.",
                    "outcome": "rejected",
                    "evidence": "CJK governance prohibits Chinese evidence from authorizing Korean wording.",
                },
                {
                    "approach": "Revise line 28 to 유한 생성, 유한 생성 부분환, and 가군 생성계 while retaining German source labels on first occurrence.",
                    "outcome": "resolved",
                    "evidence": "New TeX/PDF/PNG hashes, clean compilation, source comparison, Korean SNU evidence, and renewed visual inspection record the repair.",
                },
            ],
            "resolution_state": "resolved",
            "resolution_or_workaround": "Replace the ambiguous draft wording with explicit finite-generation and module-generating-system language; rebuild, re-extract, rerender, and preserve every rejected draft hash.",
            "evidence_artifacts": [
                historical_hash(
                    "superseded in-place Korean U01 TeX before fidelity repair",
                    "242B3DF47606609F3E2962753782028F5325BD84646FD145AFA30CA2A899CCAD",
                    "rejected draft TeX hash retained after overwrite",
                ),
                historical_hash(
                    "superseded in-place Korean U01 PDF before fidelity repair",
                    "AA390A2FBB8F3C79650127C4C725C58A6F0C66E01439DEE2DE13F34142E47B5C",
                    "rejected draft PDF hash retained after overwrite",
                ),
                historical_hash(
                    "superseded in-place Korean U01 180-DPI PNG before fidelity repair",
                    "7E0E5A0250BB9CC70EAFA79CDF22695254042D9CB20513B7226C6C1ED8B1919E",
                    "rejected draft render hash retained after overwrite",
                ),
                file_evidence(target_tex, "revised editable Korean TeX"),
                file_evidence(target_pdf, "recompiled revised Korean PDF"),
                file_evidence(target_png, "rerendered and visually inspected Korean page"),
                file_evidence(full_source, "later source lines 53-55 semantic control"),
                file_evidence(korean_corpus, "local Korean evidence shelf including SNU course evidence"),
            ],
            "residual_risk": "Integritätsbasis and the historical criterion label remain specialist-review debts even after the finite-generation and module-generation senses are explicit.",
            "recurrence_cues": [
                "endlich translated without a finite-generation sense window",
                "Modulbasis translated with 기저 despite no independence or freeness proof",
                "a compiled/rendered draft treated as semantically sealed before later-source review",
            ],
            "transferable_lesson": "For historical algebra, inspect later constructive formulas before translating basis-like and finiteness terms; successful rendering is not a semantic fidelity gate.",
            "future_check": "Revisit during U02/section-one consistency review and append a correction if a Korean invariant-theory specialist rejects 생성계.",
            "changed_artifacts": [
                "ko/Noether_Paper29_Korean_U01_v001.tex",
                "ko/Noether_Paper29_Korean_U01_v001.pdf",
                "ko/Noether_Paper29_Korean_U01_v001.log",
                "visual_inspection/Noether_Paper29_Korean_U01_v001.png",
                "evidence/KOREAN_NATIVE_EXAMPLE_CORPUS_U01.csv",
                "evidence/TERMINOLOGY_LEDGER_U01.csv",
                "evidence/ADVERSE_EVIDENCE_LEDGER_U01.csv",
                "evidence/CJKV_CROSSWALK_P29_KO_U01.csv",
            ],
            "validation_state": {
                "internal": "Source-fidelity review, two-pass rebuild, extraction, and original-resolution render inspection passed after revision.",
                "external_human": "SNU is external Korean usage evidence; no human reviewer validated this specific translation decision.",
            },
            "continuation_or_revisit": "Revisit at the section-one consistency audit or upon Korean specialist review; do not restore any superseded draft hash as current.",
        },
        {
            **common,
            "issue_id": "CJK-KO-P29-HARD-003",
            "work_unit": "P29-KO-U01 historical Korean terminology choices",
            "structural_ids": [
                "NOE-P29-KO-U01-THM-001",
                "NOE-P29-KO-U01-PARA-002",
                "NOE-P29-KO-U01-PARA-003",
            ],
            "source_locator": "German U01 lines 17, 19, and 21: Integritätsbasis, Rationalbasis, Teilerkettensatz, Wurzelring, Galois'sche Resolvente",
            "target_locator": "Korean TeX lines 28, 30, and 32; German labels retained at first occurrence where needed",
            "difficulty_class": "unsupported_historical_korean_compounds",
            "symptom": "Independent Korean evidence was unavailable for several historical invariant-theory compounds, and plausible calques have competing modern senses.",
            "severity": "high",
            "discovery_channel": "Korean-only terminology shelf and adverse-evidence audit",
            "cause": {
                "evidence": "The Korean corpus supports core terms such as 정역, 부분환, 가군, 유한생성 대수, and 정수확장 but not the exact historical compounds; adverse rows A002-A004 record the gaps.",
                "inference": "Compositional Korean renderings are necessary working choices but cannot be promoted as established specialist terminology.",
            },
            "attempted_approaches": [
                {
                    "approach": "Treat Chinese or Japanese cognate terminology as Korean authorization.",
                    "outcome": "rejected",
                    "evidence": "Language-lane governance explicitly forbids cross-language authorization.",
                },
                {
                    "approach": "Suppress every unsupported term and leave German-only prose.",
                    "outcome": "rejected",
                    "evidence": "That would not produce a Korean translation and would obscure sentence structure.",
                },
                {
                    "approach": "Use provisional Korean renderings with exact German source labels, sense windows, adverse evidence, and held review state.",
                    "outcome": "workaround",
                    "evidence": "Terminology, adverse-evidence, and CJKV crosswalk rows preserve uncertainty without importing unauthorized evidence.",
                },
            ],
            "resolution_state": "held",
            "resolution_or_workaround": "Keep the provisional source-labeled Korean compounds in the working translation and prohibit promotion beyond internal use until independent Korean specialist evidence or review exists.",
            "evidence_artifacts": [
                file_evidence(terminology, "term-by-term Korean decisions and sense windows"),
                file_evidence(adverse, "explicit unsupported-term and ambiguity risks"),
                file_evidence(crosswalk, "qualitative dominance debt and lexical-attractor basins"),
                file_evidence(korean_corpus, "independent Korean evidence shelf and scope limits"),
            ],
            "residual_risk": "정수성 기저, 유리 기저, 약수사슬정리, 근환, and 갈루아 분해식 may be nonstandard or historically misaligned.",
            "recurrence_cues": [
                "historical German compound has no Korean corpus hit",
                "same Korean form names a number-field or modern computational concept",
                "cross-CJK cognate looks convenient despite missing Korean evidence",
            ],
            "transferable_lesson": "A usable provisional translation can coexist with a held terminology decision only when the source label, excluded senses, evidence gap, and revisit trigger remain durable.",
            "future_check": "Revisit with a Korean invariant-theory source or qualified reviewer; append, never overwrite, any promoted or replaced term decision.",
            "changed_artifacts": [
                "ko/Noether_Paper29_Korean_U01_v001.tex",
                "evidence/TERMINOLOGY_LEDGER_U01.csv",
                "evidence/ADVERSE_EVIDENCE_LEDGER_U01.csv",
                "evidence/CJKV_CROSSWALK_P29_KO_U01.csv",
            ],
            "validation_state": {
                "internal": "Source labels, sense windows, adverse rows, and controlled basin values are present.",
                "external_human": "No external Korean invariant-theory or DPRK review exists.",
            },
            "continuation_or_revisit": "Revisit when independent Korean specialist evidence or review becomes available; retry exact-compound searches during later P29 units.",
        },
        {
            **common,
            "issue_id": "CJK-KO-P29-HARD-004",
            "work_unit": "P29-KO-U01 PDF inspection tool invocation",
            "structural_ids": ["NOE-P29-KO-U01-ROOT-001"],
            "source_locator": "German U01 control PDF page 1",
            "target_locator": "Korean U01 PDF page 1 and 180-DPI page render",
            "difficulty_class": "poppler_wrapper_invocation_failure",
            "symptom": "The bundled pdfinfo/pdftoppm command-wrapper layer did not provide a usable invocation during production, although the PDFs themselves were valid.",
            "severity": "medium",
            "discovery_channel": "PDF metadata/render command execution",
            "cause": {
                "evidence": "Direct execution of the bundled native Poppler Library/bin executables produced valid metadata and 1489x2105 PNGs for both PDFs.",
                "inference": "The failure was isolated to command resolution or the wrapper layer rather than PDF corruption; the exact wrapper fault was not proved.",
            },
            "attempted_approaches": [
                {
                    "approach": "Use the command wrappers resolved first on PATH.",
                    "outcome": "failed",
                    "evidence": "Production had to bypass the wrappers to obtain usable output.",
                },
                {
                    "approach": "Invoke the exact native Poppler Library/bin pdfinfo.exe and pdftoppm.exe paths.",
                    "outcome": "resolved",
                    "evidence": "Both one-page A4 PDFs were inspected and rendered at 180 DPI.",
                },
            ],
            "resolution_state": "resolved",
            "resolution_or_workaround": "Pin and invoke the native Poppler executables directly; retain wrapper and binary hashes so later runtime changes are distinguishable.",
            "evidence_artifacts": [
                file_evidence(
                    RUNTIME_ROOT / "bin/override/pdftoppm.cmd",
                    "failed-path wrapper retained for reproducibility",
                ),
                file_evidence(
                    RUNTIME_ROOT / "native/poppler/Library/bin/pdftoppm.exe",
                    "working direct renderer",
                ),
                file_evidence(
                    RUNTIME_ROOT / "native/poppler/Library/bin/pdfinfo.exe",
                    "working direct PDF metadata tool",
                ),
                file_evidence(german_pdf, "German control PDF rendered through direct binary"),
                file_evidence(german_png, "German 180-DPI output"),
                file_evidence(target_pdf, "Korean PDF rendered through direct binary"),
                file_evidence(target_png, "Korean 180-DPI output"),
                file_evidence(render_check, "visual inspection method and results"),
            ],
            "residual_risk": "A runtime update can move or replace the native executable, and the root wrapper cause remains unproved.",
            "recurrence_cues": [
                "PATH resolves to a .cmd wrapper before an executable",
                "pdfinfo or pdftoppm returns no usable output for a known-valid PDF",
                "bundled runtime version changes",
            ],
            "transferable_lesson": "When a document tool wrapper fails, pin the underlying binary and its hash before diagnosing the PDF as corrupt.",
            "future_check": "Revisit after runtime upgrades; retry the wrapper only as a diagnostic while retaining the direct-binary fallback.",
            "changed_artifacts": [
                "visual_inspection/Noether_Paper29_German_U01_control.png",
                "visual_inspection/Noether_Paper29_Korean_U01_v001.png",
                "RENDER_CHECK.md",
            ],
            "validation_state": {
                "internal": "Direct executable output, dimensions, hashes, and visual inspection are recorded.",
                "external_human": "No external toolchain audit or human typesetting review exists.",
            },
            "continuation_or_revisit": "Revisit if the Poppler runtime changes or direct rendering stops reproducing the recorded dimensions.",
        },
        {
            **common,
            "issue_id": "CJK-KO-P29-HARD-005",
            "work_unit": "P29-KO-U01 Korean typesetting diagnostics",
            "structural_ids": ["NOE-P29-KO-U01-THM-001", "NOE-P29-KO-U01-PARA-002"],
            "source_locator": "German U01 theorem line 17 and supporting paragraph line 19",
            "target_locator": "Korean TeX/log paragraphs at lines 28-29 and 30-31; rendered PDF page 1",
            "difficulty_class": "nonfatal_underfull_hbox_after_semantic_repair",
            "symptom": "Final XeLaTeX log retains Underfull hbox warnings with badness 1603 at lines 28-29 and 2050 at lines 30-31.",
            "severity": "low",
            "discovery_channel": "final XeLaTeX diagnostic scan and original-resolution render inspection",
            "cause": {
                "evidence": "The long Korean criterion/support paragraphs contain protected TeX/math/source-label spans; the final one-page render shows no clipping, collision, missing glyph, or visibly excessive gap.",
                "inference": "Line-breaking flexibility is limited, but the warnings do not evidence a visible or semantic defect in this layout.",
            },
            "attempted_approaches": [
                {
                    "approach": "Treat any underfull warning as automatic build failure.",
                    "outcome": "rejected",
                    "evidence": "Underfull boxes are nonfatal and require visual/contextual evaluation; both affected regions remain legible and within margins.",
                },
                {
                    "approach": "Accept only after inspecting the affected criterion and support paragraphs at original render resolution.",
                    "outcome": "workaround",
                    "evidence": "The 1489x2105 page passed the documented defect checklist after the fidelity revision.",
                },
            ],
            "resolution_state": "workaround",
            "resolution_or_workaround": "Retain the warnings as evidence, accept the current render after targeted visual QA, and force a rebuild/reinspection after any wording, font, or geometry change.",
            "evidence_artifacts": [
                file_evidence(target_log, "final XeLaTeX log containing both warnings"),
                file_evidence(target_png, "original-resolution visual inspection artifact"),
                file_evidence(render_check, "documented post-revision visual QA"),
            ],
            "residual_risk": "Small wording or font changes can make these paragraphs visibly loose or cause pagination drift.",
            "recurrence_cues": [
                "underfull badness increases",
                "criterion wording changes",
                "font, geometry, or emergency stretch changes",
            ],
            "transferable_lesson": "Preserve nonfatal layout warnings even after acceptance; tie the decision to exact log and render hashes rather than deleting the symptom.",
            "future_check": "Rebuild and visually revisit after any target TeX, font, geometry, or dependency change.",
            "changed_artifacts": [
                "ko/Noether_Paper29_Korean_U01_v001.log",
                "visual_inspection/Noether_Paper29_Korean_U01_v001.png",
                "RENDER_CHECK.md",
            ],
            "validation_state": {
                "internal": "Warnings reproduced; affected areas passed internal original-resolution inspection.",
                "external_human": "No independent human typographic review exists.",
            },
            "continuation_or_revisit": "Revisit after every target/layout change and retry line-break improvement only if it preserves fidelity and page integrity.",
        },
        {
            **common,
            "issue_id": "CJK-KO-P29-HARD-006",
            "work_unit": "P29-KO-U01 printed-source visual evidence disposition",
            "structural_ids": [
                "NOE-P29-KO-U01-ROOT-001",
                "NOE-P29-KO-U01-SEC-001",
                "NOE-P29-KO-U01-PARA-001",
                "NOE-P29-KO-U01-THM-001",
                "NOE-P29-KO-U01-PARA-002",
                "NOE-P29-KO-U01-PARA-003",
                "NOE-P29-KO-U01-PARA-004",
            ],
            "source_locator": "native 400-PPI source scans: printed p. 28/canvas 32 and printed p. 29/canvas 33, full-page bounds",
            "target_locator": "metadata/hash/coordinate handoff only for source scans; project-generated Korean render is separately distributable",
            "difficulty_class": "unresolved_source_image_redistribution_rights",
            "symptom": "The source-page JPEGs are necessary research evidence, but no documentary redistribution permission or rights basis was found.",
            "severity": "high",
            "discovery_channel": "visual-evidence rights audit",
            "cause": {
                "evidence": "The local files preserve printed pp. 28-29 and stable hashes, but neither the source directory nor lane controls contain a license or permission grant.",
                "inference": "Age, accessibility, or research use cannot be converted into a public redistribution right without documentary evidence.",
            },
            "attempted_approaches": [
                {
                    "approach": "Assume the historical page scans may be placed in the public payload.",
                    "outcome": "rejected",
                    "evidence": "No permission record supports that disposition.",
                },
                {
                    "approach": "Discard or silently omit the scans after source checking.",
                    "outcome": "rejected",
                    "evidence": "The archival directive requires preservation of every used visual witness.",
                },
                {
                    "approach": "Preserve binaries privately and expose only public-safe hashes, page/canvas identifiers, coordinates, dimensions, and rights-blocked status.",
                    "outcome": "held",
                    "evidence": "This preserves reproducibility without inventing permission.",
                },
            ],
            "resolution_state": "held",
            "resolution_or_workaround": "Keep both source JPEGs at the exact private root, exclude their pixels from public packages, and route only the public-safe metadata/hash/coordinate layer pending rights clearance.",
            "evidence_artifacts": [
                file_evidence(
                    SOURCE_SCAN_ROOT / "P29_source_printed_p28_canvas00000032_fullres.jpg",
                    "printed p. 28 source witness",
                    "source_scan",
                ),
                file_evidence(
                    SOURCE_SCAN_ROOT / "P29_source_printed_p29_canvas00000033_fullres.jpg",
                    "printed p. 29 source witness",
                    "source_scan",
                ),
                file_evidence(render_check, "source-scan visual inspection scope and noncertification caveat"),
            ],
            "residual_risk": "Public reproduction remains blocked; private paths may be unavailable to a future archive consumer even though hashes and coordinates survive.",
            "recurrence_cues": [
                "source scan used in QA without a license field",
                "historical age treated as permission",
                "public package builder copies an entire visual directory",
            ],
            "transferable_lesson": "Rights uncertainty must change publication disposition, not evidence preservation or the truth of the source-check record.",
            "future_check": "Revisit only on documentary rights clearance or repository-custody instruction; keep source pixels manifest-only meanwhile.",
            "changed_artifacts": [
                "RENDER_CHECK.md",
                "evidence/visual_evidence/RIGHTS_BLOCKED_SOURCE_ROOT_MANIFEST.csv",
            ],
            "validation_state": {
                "internal": "Files, hashes, dimensions, pages, and private preservation were checked internally.",
                "external_human": "No rights-holder permission, legal clearance, or archive-review disposition exists.",
            },
            "continuation_or_revisit": "Revisit on documentary rights clearance; otherwise retain the manifest-only rights-blocked disposition at every handoff.",
        },
        {
            **common,
            "issue_id": "CJK-KO-P29-HARD-007",
            "work_unit": "P29-KO-U01 Korean terminology evidence shelf",
            "structural_ids": [
                "NOE-P29-KO-U01-THM-001",
                "NOE-P29-KO-U01-PARA-002",
                "NOE-P29-KO-U01-PARA-003",
            ],
            "source_locator": "U01 terminology at German lines 17, 19, and 21; evidence shelf records KO-P29-E001 through E006",
            "target_locator": "Korean TeX lines 28, 30, and 32 plus terminology/adverse/crosswalk records",
            "difficulty_class": "sparse_secondary_local_language_evidence",
            "symptom": "The available Korean shelf is mostly institutional repositories, course catalogs, and publisher contents; it supports core algebra senses but not the exact Noether-era compounds or DPRK standards.",
            "severity": "medium",
            "discovery_channel": "bounded Korean-only web/evidence audit",
            "cause": {
                "evidence": "Six Korean records support 표수, 정역, 부분환, 가군, 유한생성 대수, 정수확장, and related core vocabulary while each record states its scope limit; no DPRK source was checked.",
                "inference": "The shelf is adequate to veto clear sense errors and support core ko-KR register, but inadequate for certification or historical-compound promotion.",
            },
            "attempted_approaches": [
                {
                    "approach": "Treat syllabus/catalog occurrence as sentence-level translation authority.",
                    "outcome": "rejected",
                    "evidence": "The evidence records explicitly limit these sources to headword and semantic-frame support.",
                },
                {
                    "approach": "Fill exact-compound gaps from Mandarin-Simplified or Japanese evidence.",
                    "outcome": "rejected",
                    "evidence": "Cross-language authorization is forbidden and dominance debt is qualitative, never a readiness score.",
                },
                {
                    "approach": "Use the shelf for core ko-KR senses, label exact compounds provisional/held, and make DPRK noncoverage explicit.",
                    "outcome": "workaround",
                    "evidence": "The terminology, adverse, and crosswalk ledgers separate supported core terms from unresolved historical choices.",
                },
            ],
            "resolution_state": "held",
            "resolution_or_workaround": "Continue ko-KR working production with explicit evidence scope limits; make no ko-KP, community, or specialist-certification claim and keep exact historical compounds held.",
            "evidence_artifacts": [
                file_evidence(korean_corpus, "six-record Korean native/example evidence shelf"),
                file_evidence(terminology, "evidence-linked Korean term decisions"),
                file_evidence(adverse, "DPRK absence and exact-compound adverse evidence"),
                file_evidence(crosswalk, "qualitative Mandarin-Simplified dominance risk/debt controls"),
            ],
            "residual_risk": "Institutional headword evidence may not reflect invariant-theory specialist usage; North-Korean standards remain completely unverified.",
            "recurrence_cues": [
                "exact compound lacks Korean evidence ID",
                "source class is only syllabus or catalog",
                "ko-KR choice is generalized to ko-KP",
                "dominant Mandarin evidence is treated as a readiness scalar",
            ],
            "transferable_lesson": "Record what a local-language source actually supports and its scope limit; weak but relevant evidence can constrain meaning without certifying a translation.",
            "future_check": "Retry Korean primary/specialist searches and revisit upon a documented DPRK corpus or qualified reviewer; append any promotion or correction.",
            "changed_artifacts": [
                "evidence/KOREAN_NATIVE_EXAMPLE_CORPUS_U01.csv",
                "evidence/TERMINOLOGY_LEDGER_U01.csv",
                "evidence/ADVERSE_EVIDENCE_LEDGER_U01.csv",
                "evidence/CJKV_CROSSWALK_P29_KO_U01.csv",
            ],
            "validation_state": {
                "internal": "Evidence IDs, URLs, source classes, observed terms, and scope limits are recorded and hashed.",
                "external_human": "The cited institutions are external sources; no human review of the P29 translation or DPRK terminology exists.",
            },
            "continuation_or_revisit": "Revisit on independent Korean invariant-theory evidence, DPRK documentation, or human review; retry at each later P29 terminology promotion.",
        },
    ]

    chained: list[dict] = []
    previous_hash: str | None = None
    for sequence, record in enumerate(records, 1):
        ordered = {
            "schema_version": record.pop("schema_version"),
            "ledger_sequence": sequence,
            "issue_id": record.pop("issue_id"),
            "record_sha256": "",
            "previous_record_sha256": previous_hash,
            **record,
        }
        ordered["record_sha256"] = canonical_record_hash(ordered)
        previous_hash = ordered["record_sha256"]
        chained.append(ordered)

    with LEDGER.open("x", encoding="utf-8", newline="\n") as handle:
        for record in chained:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")

    print(
        f"initialized={len(chained)} recorded_at={recorded_at} "
        f"head={chained[-1]['record_sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
