#!/usr/bin/env python3
"""Freeze and project the recovered EGA I printed-p.142 checkpoint.

The producer roots reached coherent p.142 source, ledger, manifest, wrapper, and
pre-Stacks bytes but stopped before their terminal p.142 validation files and
bounded builds were closed.  This archive-only recovery accepts the exact
stable producer bytes, preserves them unchanged in private custody, binds the
superseded French R1 build, and adds only separately identified archive QA and
continuation surfaces.  It never writes into either producer root.
"""

from __future__ import annotations

import csv
import importlib.util
import json
import re
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    "ega_p138_builder", SCRIPT_DIR / "build_ega_p138_custody_projection_20260804.py"
)
if _spec is None or _spec.loader is None:
    raise RuntimeError("cannot load the bounded predecessor builder")
prev = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(prev)
base = prev.base
base.TEXT_SUFFIXES.update({".aux", ".log", ".out"})

WORKTREE = SCRIPT_DIR.parent
PROJECT_ROOT = Path(r"C:\Users\Floris\Documents\interlanguage")
LANE_ROOT = PROJECT_ROOT / r"03_projects\language_management\english_germanic"
FRENCH_ROOT = (
    PROJECT_ROOT
    / r"Transcription\03_working_transcriptions\EGA_French_NUMDAM_canonical_TeX_20260801_r1"
)
ENGLISH_ROOT = (
    LANE_ROOT
    / r"03_working_translations\EGA_English_Global_0_IV_french_recheck_source_successor_20260802_r1"
)
LANE_CONTROL = LANE_ROOT / "00_lane_control"
RECOVERY_BUILD_ROOT = Path(r"C:\tmp\ega-p142-bounded-audit-20260804-r1")
PRIVATE_FINAL = (
    LANE_ROOT
    / r"90_logs\private_archive_custody\EGA_I_P142_R90_ARCHIVE_RECOVERY_PRIVATE_RAW_CUSTODY_20260804_r1"
)
PUBLIC_FINAL = (
    WORKTREE
    / r"sources\ega\checkpoints\ega1-p142-diplomatic-prestacks-archive-recovery-r1-20260804"
)

R89_MANIFEST = ENGLISH_ROOT / r"controls\SOURCE_INPUT_SHA256_R89.json"
R90_MANIFEST = ENGLISH_ROOT / r"controls\SOURCE_INPUT_SHA256_R90.json"
R88_VALIDATION = ENGLISH_ROOT / r"controls\SOURCE_DIFF_VALIDATION_R88.json"
R64_FRENCH_VALIDATION = FRENCH_ROOT / r"controls\EGA1_CHAPTER1_P141_VALIDATION_R64.json"
ENGLISH_PROJECTION = ENGLISH_ROOT / r"controls\EGA1_P142_ENGLISH_SECTION6_PREFIX_R1.tex"
ENGLISH_WRAPPER = ENGLISH_ROOT / r"controls\EGA1_P142_ENGLISH_BOUNDED_CHECK_R1.tex"
FRENCH_WRAPPER_R1 = FRENCH_ROOT / r"qa\ega1_chapter1_build\chapter1-p79-142-check-r1.tex"
FRENCH_WRAPPER_R2 = FRENCH_ROOT / r"qa\ega1_chapter1_build\chapter1-p79-142-check-r2.tex"
FRENCH_ADVERSE_R1 = FRENCH_ROOT / r"qa\ega1_chapter1_build\chapter1-p79-142-build-r1-xelatex"
ENGLISH_RECOVERY_BUILD = RECOVERY_BUILD_ROOT / "english"
FRENCH_RECOVERY_BUILD = RECOVERY_BUILD_ROOT / "french"
SCAFFOLD = LANE_CONTROL / "EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_20260802.md"
DUAL_DOI_CONTROL = LANE_CONTROL / "PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md"
SUCCESSOR_PROTOCOL = LANE_CONTROL / "SUCCESSOR_SESSION_BOOTSTRAP_AND_LOGBOOK_PROTOCOL_20260803.md"

EXPECTED = {
    R89_MANIFEST: (54491, "5B84232F8611E5C4B9D5AAFA775C60E92A85E4F611B0AE26BC37BF3B33ECF4D4"),
    R90_MANIFEST: (54931, "9C7A39B176AADF819DC164BDAEA8C23EEB6E7B5851D2F2C318952B1C837D3E7D"),
    R88_VALIDATION: (15431, "288BC03CD1D8E9DB2B291B9CA7369DD8670A9D912C0C70EBE2FCE126F4C8F529"),
    R64_FRENCH_VALIDATION: (16534, "027E1BB4FC646376CAC767DCFA08933C86AE657719BAAA99A8DBF68A6DF6CAF7"),
    ENGLISH_PROJECTION: (8280, "52F50CF40BFD1F3340A14E3B7F203DD5E02AAC9D90C87DEC0EF6A4A30F4DC40D"),
    ENGLISH_WRAPPER: (836, "B1A9359A7B02D17D8B22DD49C972E4E34744C4284C9C2D37D95730F10BE5251A"),
    FRENCH_WRAPPER_R1: (3816, "AD281ECE5F5CDBF5B80E5DCB3E57E74FC4D05BF4933F99FCE9C97298F86542F1"),
    FRENCH_WRAPPER_R2: (3850, "A59F9624D8215450E82453D4416B2ACAF551CE9ED00150CD300E2B27DD932F67"),
    SCAFFOLD: (120947, "B630C72A3BEE2CC67D76A087265639F2A54DF3AC866D367C7CE97A62CB914D09"),
    DUAL_DOI_CONTROL: (2296, "BFA1E3A3EDA94E8C3425BAE50C842610A47D508FB260BF761BA3206883012679"),
    SUCCESSOR_PROTOCOL: (4603, "2799FE59BDE0FA93334FE45EB2B0AC9C63F250B006C1DE0D5FF946160EE65ECC"),
    FRENCH_ROOT / "LOGBOOK.md": (400878, "E81FD6884BC4F81D938E73FBC7D1CEC3CFF076300AC992BFB14C2E02DAC40D67"),
    FRENCH_ROOT / "STATUS.md": (253367, "638E49B111EFB1589C0995F0A8A997CEF39F9D280AB61EE3E6C99EC9072701F7"),
    FRENCH_ROOT / "CONTINUATION_HANDOFF.md": (131980, "33DCF681AC3773C3250FBADF5AC59CD5F3081011E84C9EFC850B0B8F13D70C58"),
    FRENCH_ROOT / "README.md": (858, "70D6B44C93313E4FF153544EAB7260991C5F57FE66C96E0B193E9A2392713D59"),
    ENGLISH_ROOT / "LOGBOOK.md": (177464, "AD9439369B901452FBB1F66817C15821F02096DF01F94D3E228622DC14298540"),
    ENGLISH_ROOT / "STATUS.md": (108025, "B1BB430125C76EFA5F0B4FDABD47912C65DF0F945AFD4D40090526E21D36DB3E"),
}

LEDGER_EXPECTED = {
    "FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P142_20260804.jsonl": (
        7388,
        "2309825CB20EC7BD9C9F6ADC6EB6288CFA2164972EE8F99C2FD03A737CA928D5",
        14,
    ),
    "ENGLISH_CORRECTION_RECHECK_APPEND_P142_20260804.jsonl": (
        6541,
        "EBF102402D50CA3867B46DC1607760A52BFA186F174C6EFAFAB5E3612462A25E",
        14,
    ),
    "WORKFLOW_ERROR_APPEND_P142_20260804.jsonl": (
        6991,
        "03C0499CED4426F6D6926F1875BB973613D9B5E8AD588F460E283B29B6BDDAE2",
        8,
    ),
}

FRENCH_SOURCE_EXPECTED = {
    "ega1/chapter1-frontmatter-fr.tex": (2057, "7B2D0F8F812EBA3121202F0AE6415FFC6C281B8428DA8F0F72D89DF1CEC01708"),
    "ega1/ega0-1-fr.tex": (282508, "5B6E27ADF94611E5B135E2316C1EEAB4B1EE5A067146E7C22DC7DE67C6138005"),
    "ega1/ega1-1-fr.tex": (71381, "D201398091BCC065BE7B5EFC610183E1E2071E01BC8E35C0CE1441DF3E579393"),
    "ega1/ega1-2-fr.tex": (27463, "AE6B128092ACBB8C1AFB4899EEA003FB966B6FF6669A264B59FD5F095AF4F029"),
    "ega1/ega1-3-fr.tex": (59766, "DB4F986C9FDC1B66FF2D627C5E9121BCE0490563B7C14415320B5DDD7424B851"),
    "ega1/ega1-4-fr.tex": (34793, "9775A6A8EA2AC2415CCE4DC64EEA356382ECED4F06C59FB67C602C6C7ED6F0C1"),
    "ega1/ega1-5-fr.tex": (50232, "4610C5F9E732D99948AA809ED64C85D236423990C2750A06F0DC7A805D317701"),
    "ega1/ega1-6-fr.tex": (8918, "00E79CA7426EA6320FF63BF0ED4207272B5210C94CF8F4E6840358A9D5A9A622"),
    "ega1/frontmatter-fr.tex": (1120, "D506B87684E2136E3F87495190EECDF40B79DB8887ED71093C4CD56648E282A9"),
    "ega1/intro-fr.tex": (16433, "CE78400CD9DBC36A4D11CC933B7BE18BEAC0C69AE6A04FBA3ECFA86053572980"),
}

ENGLISH_BUILD_EXPECTED = {
    "EGA1_P142_ENGLISH_BOUNDED_CHECK_R1.aux": (16123, "F693C579D459499059EF6B66D3671883975EE45DF3038731F7E4C19D24C1C503"),
    "EGA1_P142_ENGLISH_BOUNDED_CHECK_R1.log": (52985, "EB75A63C4A9B29041DFB48BE85DEA92E4F5C34ABBD75DC7272D4546D4849C9A5"),
    "EGA1_P142_ENGLISH_BOUNDED_CHECK_R1.out": (5077, "81A7FF2E6CB5BD290DB153922B9C41B57B2164C1B16233E86859CD54F6BBF816"),
    "EGA1_P142_ENGLISH_BOUNDED_CHECK_R1.pdf": (236138, "9D47EF0B835D96BC58A038D88999A851C7A3618B6972A1FD8EEBA52286717837"),
    "EGA1_P142_ENGLISH_BOUNDED_CHECK_R1-terminal-pages-31-32-layout.txt": (4845, "08F94CD3E57FEC7E38DA6FED09F2BADAFDDA19B5912B56B0B3F5C0F730DE7882"),
}

FRENCH_BUILD_EXPECTED = {
    "chapter1-p79-142-check-r2.aux": (38471, "ADA0E4C725A7EF0141A96DCA1B5F734E1E06F3C3B24E8F8D94FB1868C21AE658"),
    "chapter1-p79-142-check-r2.log": (24813, "F7D9772BF1259962DD3D2779DD7F5F3EAB7ECF62804D3AF241B31F6FE232626A"),
    "chapter1-p79-142-check-r2.out": (8960, "F544BBB7B3E513CD3F73746F95BDA64ECAA54CA94278E60AA424BE82598597C4"),
    "chapter1-p79-142-check-r2.pdf": (390212, "4A0B1A2918BF560E3AE8228DA3FB9EA5A000B338F785B251B22A2012EFA073BB"),
    "chapter1-p79-142-check-r2-terminal-pages-43-44-layout.txt": (7239, "16E63BBAB9B009EF1DA1B6D3E827743767ED0069A9DAEA2515B4E2ECABA6B4FA"),
}

FRENCH_ADVERSE_EXPECTED = {
    "chapter1-p79-142-check-r1.aux": (38422, "1F79E1C75268A2682C1B2F6A8A6E5B75A00766B219CAAFE6BCE3E6E3B188E7C4"),
    "chapter1-p79-142-check-r1.log": (25653, "C29E9778215FC4DD2D97F9CAF1F4CB703409DE307A1B183BD8E89C5B53C62411"),
    "chapter1-p79-142-check-r1.out": (8960, "F544BBB7B3E513CD3F73746F95BDA64ECAA54CA94278E60AA424BE82598597C4"),
    "chapter1-p79-142-check-r1.pdf": (390049, "7EF5D014AC143F974C9900D620656DFC2E42F21B340923EB9C8C5905E5937354"),
}

DIRECT_NAMES = [
    "00_EGA_I_P142_Diplomatic_French_Paired_English_PreStacks_Source.zip",
    "01_READ_ME_FIRST.md",
    "02_EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P142.md",
    "03_EGA_FRENCH_PROJECT_LOGBOOK_THROUGH_P141_PUBLIC_PRIVACY_CLEAN.md",
    "04_EGA_ENGLISH_RECHECK_LOGBOOK_THROUGH_P141_PUBLIC_PRIVACY_CLEAN.md",
    "05_EGA_P142_ARCHIVE_RECOVERY_CONTINUATION_HANDOFF.md",
    "06_EGA_FRENCH_STATUS_THROUGH_P141_PUBLIC_PRIVACY_CLEAN.md",
    "07_EGA_ENGLISH_STATUS_THROUGH_P141_PUBLIC_PRIVACY_CLEAN.md",
    "08a_EGA1_CHAPTER1_P142_ARCHIVE_RECOVERY_VALIDATION.json",
    "08b_EGA_ENGLISH_R90_ARCHIVE_RECOVERY_VALIDATION.json",
    "09a_FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P142_20260804.jsonl",
    "09b_ENGLISH_CORRECTION_RECHECK_APPEND_P142_20260804.jsonl",
    "09c_WORKFLOW_ERROR_APPEND_P142_20260804.jsonl",
    "09d_EGA_P142_ARCHIVE_RECOVERY_DECISION_LOG.jsonl",
    "09e_EGA_P142_ARCHIVE_PUBLIC_PROJECTION_ATTEMPT_LOG.jsonl",
    "10_RIGHTS_AND_PROVENANCE.md",
    "11_PRIVACY_TRANSFORMATIONS.csv",
    "12_PRIVACY_VALIDATION.json",
    "13_PACKAGE_PAYLOAD_MANIFEST.csv",
]


def copy_exact(target_root: Path, relative: str, source: Path, expected=None) -> bytes:
    data = base.require_identity(source, expected) if expected else base.stable_copy_bytes(source)
    base.write_bytes(target_root, relative, data)
    return data


def line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def validate_jsonl(path: Path, expected_rows: int) -> list[dict[str, object]]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    if len(rows) != expected_rows:
        raise RuntimeError(f"JSONL row count mismatch for {path}: {len(rows)} != {expected_rows}")
    ids = [str(row.get("stable_id") or row.get("id") or "") for row in rows]
    if any(not item for item in ids) or len(ids) != len(set(ids)):
        raise RuntimeError(f"missing or duplicate stable JSONL IDs: {path}")
    return rows


def log_profile(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8", errors="strict")
    lines = text.splitlines()
    page_match = re.search(r"Output written on[\s\S]*?\((\d+)\s+page\s*s?\)\.", text)
    if not page_match:
        raise RuntimeError(f"cannot recover page count from TeX log: {path}")
    return {
        "bytes": path.stat().st_size,
        "lines": len(lines),
        "sha256": base.identity(path)[1],
        "pages": int(page_match.group(1)),
        "hard_errors": sum(bool(re.search(r"^!|Fatal error|Emergency stop", line)) for line in lines),
        "pdf_string_warnings": sum("Token not allowed in a PDF string" in line for line in lines),
        "overfull_boxes": sum(line.startswith("Overfull \\hbox") for line in lines),
        "underfull_boxes": sum(line.startswith("Underfull \\hbox") for line in lines),
        "undefined_hyperrefs": sum("Hyper reference" in line and "undefined" in line for line in lines),
        "undefined_reference_summaries": sum("There were undefined references" in line for line in lines),
        "multiply_defined_label_warnings": sum("multiply defined" in line for line in lines),
        "rerun_warnings": sum(
            "Rerun to get cross-references right" in line or "Label(s) may have changed" in line
            for line in lines
        ),
    }


def archive_recovery_rows() -> list[dict[str, object]]:
    return [
        {
            "stable_id": "EG-EGA-ARCHIVE-P142-INTAKE-001",
            "classification": "bounded_interrupted_checkpoint_recovery",
            "decision": "accept the stable p.142 source, ledgers, R89/R90 manifests, wrappers, and pre-Stacks scaffold without changing either producer root",
            "producer_terminal_validation_present": False,
            "archive_recovery_required": True,
        },
        {
            "stable_id": "EG-EGA-ARCHIVE-P142-STABILITY-001",
            "classification": "two_observation_exact_byte_stability",
            "english_source": {"bytes": 54751, "sha256": "EBFAFDE5100D7B2D956AF1B98ACF7948717C8384F2D4C45347E1278EE77D9EA9"},
            "french_source": {"bytes": 8918, "sha256": "00E79CA7426EA6320FF63BF0ED4207272B5210C94CF8F4E6840358A9D5A9A622"},
            "tex_processes_running_at_both_observations": 0,
            "pass": True,
        },
        {
            "stable_id": "EG-EGA-ARCHIVE-P142-R90-REPLAY-001",
            "classification": "complete_manifest_and_ordinal_tree_replay",
            "file_count": 127,
            "total_bytes": 7281925,
            "canonical_tree_sha256": "F25D638DCFAA5654BF5ED53481009D6E2B3D94C4B1AB99AF5AAFECC0C1F1335A",
            "missing": 0,
            "extra": 0,
            "size_errors": 0,
            "hash_errors": 0,
            "ordinal_order_errors": 0,
            "r89_to_r90_changed_paths": ["ega1/ega1-6.tex"],
            "pass": True,
        },
        {
            "stable_id": "EG-EGA-ARCHIVE-P142-FRENCH-R1-SUPERSESSION-001",
            "classification": "preserved_adverse_build_and_wrapper_successor",
            "adverse_event": "the existing French R1 build had the newly introduced undefined bounded hyper-reference 0.2.1.6-fr",
            "resolution": "preserve R1 unchanged; use the already-existing R2 wrapper that adds only a bounded phantom target; build R2 separately in scratch",
            "producer_source_mutated": False,
            "adverse_bytes_preserved": True,
        },
        {
            "stable_id": "EG-EGA-ARCHIVE-P142-BOUNDED-BUILDS-001",
            "classification": "sequential_ram_light_archive_build_recovery",
            "english_passes": 3,
            "french_passes": 3,
            "exit_codes": [0, 0, 0, 0, 0, 0],
            "english_pages": 32,
            "french_pages": 44,
            "new_rendered_pages": 0,
            "ocr_run": False,
            "global_build_run": False,
            "producer_roots_mutated": False,
            "pass": True,
        },
        {
            "stable_id": "EG-EGA-ARCHIVE-P142-PDFINFO-ROUTE-001",
            "classification": "read_only_tool_route_failure_and_successor",
            "adverse_event": "the configured pdfinfo command wrapper returned system-cannot-find-path for both scratch PDFs",
            "mutation_before_failure": False,
            "resolution": "take page counts from the terminal TeX log declarations and use the working pdftotext executable for two-page terminal layout extraction",
            "pass": True,
        },
        {
            "stable_id": "EG-EGA-ARCHIVE-P142-PRIVATE-BUILD-ATTEMPT-001",
            "classification": "immutable_projection_builder_failure_and_successor",
            "adverse_event": "the first private-custody build stopped because the adverse French R1 TeX log wraps the word pages across a physical log line and the strict page-count parser did not admit that representation",
            "mutation_before_failure": "partial private temp tree only",
            "producer_root_mutated": False,
            "public_root_created": False,
            "failed_temp_preserved": True,
            "resolution": "admit TeX whitespace inside the word pages, preserve the failed temp under an explicit private adverse-attempt name, and rerun into a fresh immutable target",
            "pass": True,
        },
        {
            "stable_id": "EG-EGA-ARCHIVE-P142-TERMINAL-TEXT-001",
            "classification": "bounded_terminal_text_replay",
            "english_layout": {"pages": [31, 32], "bytes": 4845, "sha256": "08F94CD3E57FEC7E38DA6FED09F2BADAFDDA19B5912B56B0B3F5C0F730DE7882"},
            "french_layout": {"pages": [43, 44], "bytes": 7239, "sha256": "16E63BBAB9B009EF1DA1B6D3E827743767ED0069A9DAEA2515B4E2ECABA6B4FA"},
            "corrected_meeting_components_visible": True,
            "english_p143_cursor_visible": True,
            "french_p143_cursor_visible": True,
            "visual_render_run": False,
            "pass": True,
        },
        {
            "stable_id": "EG-EGA-ARCHIVE-P142-BOUNDARY-001",
            "classification": "honest_checkpoint_boundary",
            "producer_logbook_status_continuation_terminal_page": 141,
            "p142_decision_ledgers_complete": True,
            "archive_recovery_surfaces_separate": True,
            "next_cursor": "PDF one-based p.142 / printed p.143, continuation of Proposition 6.1.10",
            "whole_project_complete": False,
        },
    ]


def build_recovery_validations(temp_root: Path, manifest: dict[str, object]) -> tuple[dict[str, object], dict[str, object]]:
    english_log = log_profile(ENGLISH_RECOVERY_BUILD / "EGA1_P142_ENGLISH_BOUNDED_CHECK_R1.log")
    french_log = log_profile(FRENCH_RECOVERY_BUILD / "chapter1-p79-142-check-r2.log")
    adverse_log = log_profile(FRENCH_ADVERSE_R1 / "chapter1-p79-142-check-r1.log")
    if english_log != {
        **english_log,
        "pages": 32,
        "hard_errors": 0,
        "pdf_string_warnings": 2,
        "overfull_boxes": 4,
        "underfull_boxes": 0,
        "undefined_hyperrefs": 1,
        "undefined_reference_summaries": 1,
        "multiply_defined_label_warnings": 0,
        "rerun_warnings": 0,
    }:
        raise RuntimeError(f"unexpected recovered English warning profile: {english_log}")
    if french_log != {
        **french_log,
        "pages": 44,
        "hard_errors": 0,
        "pdf_string_warnings": 0,
        "overfull_boxes": 2,
        "underfull_boxes": 0,
        "undefined_hyperrefs": 5,
        "undefined_reference_summaries": 1,
        "multiply_defined_label_warnings": 0,
        "rerun_warnings": 0,
    }:
        raise RuntimeError(f"unexpected recovered French warning profile: {french_log}")
    if adverse_log["undefined_hyperrefs"] != 7 or "0.2.1.6-fr" not in (
        FRENCH_ADVERSE_R1 / "chapter1-p79-142-check-r1.log"
    ).read_text(encoding="utf-8"):
        raise RuntimeError("preserved French R1 adverse build no longer has its exact seven-reference profile")

    english_layout = (ENGLISH_RECOVERY_BUILD / "EGA1_P142_ENGLISH_BOUNDED_CHECK_R1-terminal-pages-31-32-layout.txt").read_text(encoding="utf-8")
    french_layout = (FRENCH_RECOVERY_BUILD / "chapter1-p79-142-check-r2-terminal-pages-43-44-layout.txt").read_text(encoding="utf-8")
    if "components of U that meet W" not in english_layout or "a closed set F containing" not in english_layout:
        raise RuntimeError("English terminal layout does not expose the correction and p.143 cursor")
    if not re.search(r"ensemble ferm[ée] F contenant", french_layout, flags=re.IGNORECASE):
        raise RuntimeError("French terminal layout does not expose the p.143 cursor")

    live = (ENGLISH_ROOT / r"source\ega1\ega1-6.tex").read_bytes()
    projection = base.require_identity(ENGLISH_PROJECTION, EXPECTED[ENGLISH_PROJECTION])
    live_lines = live.splitlines(keepends=True)
    if b"".join(live_lines[:137]) != projection:
        raise RuntimeError("p.142 English bounded projection is not an exact live-source prefix")
    content = b"".join(live_lines[66:137])
    bounded = b"".join(live_lines[65:138])
    if (len(content), base.sha256(content)) != (
        3598,
        "FA92D3476F9D64F664607B90E4249F3473E719698E4B171447D4321AFA4497D8",
    ) or (len(bounded), base.sha256(bounded)) != (
        3632,
        "485A4C7865B016E208DC9AEE9ACD23BA9F4D23B6606D44CE6410EC7B3C12C87F",
    ):
        raise RuntimeError("p.142 English slice identities do not replay")

    ledger_info: dict[str, object] = {}
    for name, expected in LEDGER_EXPECTED.items():
        path = FRENCH_ROOT / "controls" / name
        rows = validate_jsonl(path, expected[2])
        ledger_info[name] = {
            "rows": len(rows),
            "bytes": expected[0],
            "sha256": expected[1],
            "parse_errors": 0,
            "duplicate_stable_ids": 0,
        }

    french_source_rows = [
        {"relative_path": rel, "bytes": expected[0], "sha256": expected[1]}
        for rel, expected in sorted(FRENCH_SOURCE_EXPECTED.items())
    ]
    english_validation = {
        "schema": "ega_english_archive_recovery_validation_v1",
        "status": "PASS_ARCHIVE_RECOVERY_PRINTED_P142_DIRECT_AUTHORITY_RECHECK_ONE_MATHEMATICAL_PRECISION_REPAIR_MANIFEST_AND_BOUNDED_BUILD__READY_PRINTED_P143",
        "errors": [],
        "source_manifest": {
            "relative_path": "controls/SOURCE_INPUT_SHA256_R90.json",
            "bytes": EXPECTED[R90_MANIFEST][0],
            "sha256": EXPECTED[R90_MANIFEST][1],
            "file_count": manifest["file_count"],
            "total_bytes": manifest["total_bytes"],
            "canonical_tree_sha256": manifest["canonical_tree_sha256"],
            "missing": 0,
            "extra": 0,
            "size_errors": 0,
            "hash_errors": 0,
            "ordinal_order_errors": 0,
        },
        "pre_recheck_manifest": {"generation": "R89", "bytes": EXPECTED[R89_MANIFEST][0], "sha256": EXPECTED[R89_MANIFEST][1]},
        "manifest_delta": {
            "changed_rows": 1,
            "changed_relative_paths": ["ega1/ega1-6.tex"],
            "added_rows": 0,
            "removed_rows": 0,
            "byte_delta": 14,
        },
        "source": {
            "relative_path": "source/ega1/ega1-6.tex",
            "bytes": 54751,
            "lines": 839,
            "sha256": "EBFAFDE5100D7B2D956AF1B98ACF7948717C8384F2D4C45347E1278EE77D9EA9",
            "inverse_replay_bytes": 54737,
            "inverse_replay_sha256": "BA45F1965B6085D84CA7E3723E4078039093ACFDDD916FD191AD43DE251CA980",
        },
        "authority": {
            "printed_page": 142,
            "pdf_one_based_page": 141,
            "authority_pdf_bytes": 31680717,
            "authority_pdf_sha256": "9ABA23020217535977E279BDD06A0413F48DA703086865BA4C00766C85DF4AE6",
            "authority_image_bytes": 1772673,
            "authority_image_sha256": "F7FCFB5BF65576AC2607AF7126910447C4F3C16971D53E76554C6DC6BC43F8AE",
            "authority_image_included": False,
            "ocr_run": False,
        },
        "decision_ledgers": ledger_info,
        "source_intervention": {
            "mathematical_precision_repairs": 1,
            "repair": "restore that only irreducible components of U which meet W contribute component traces on W",
            "old_fragment_sha256": "17479EC875747AF90126616F9EB57B7B570A59177AB3BABBEB6792145F3AA267",
            "new_fragment_sha256": "0E9A8A606A9A2E73405E169847FBFBA17DD6399EF5307C86FF0FB55D03EAE5F9",
            "unsupported_corrections": 0,
            "unresolved_readings": 0,
        },
        "paired_slice": {
            "content_lines": "67--137",
            "content_bytes": 3598,
            "content_sha256": "FA92D3476F9D64F664607B90E4249F3473E719698E4B171447D4321AFA4497D8",
            "bounded_lines_with_markers": "66--138",
            "bounded_bytes": 3632,
            "bounded_sha256": "485A4C7865B016E208DC9AEE9ACD23BA9F4D23B6606D44CE6410EC7B3C12C87F",
        },
        "bounded_projection": {"bytes": 8280, "lines": 137, "sha256": EXPECTED[ENGLISH_PROJECTION][1], "exact_live_prefix": True},
        "bounded_build": {
            **english_log,
            "passes": 3,
            "pdf_bytes": ENGLISH_BUILD_EXPECTED["EGA1_P142_ENGLISH_BOUNDED_CHECK_R1.pdf"][0],
            "pdf_sha256": ENGLISH_BUILD_EXPECTED["EGA1_P142_ENGLISH_BOUNDED_CHECK_R1.pdf"][1],
            "terminal_layout_bytes": ENGLISH_BUILD_EXPECTED["EGA1_P142_ENGLISH_BOUNDED_CHECK_R1-terminal-pages-31-32-layout.txt"][0],
            "terminal_layout_sha256": ENGLISH_BUILD_EXPECTED["EGA1_P142_ENGLISH_BOUNDED_CHECK_R1-terminal-pages-31-32-layout.txt"][1],
            "warning_profile_matches_p141": True,
            "terminal_text_pass": True,
        },
        "semantic_scaffold": {"bytes": EXPECTED[SCAFFOLD][0], "lines": 2049, "sha256": EXPECTED[SCAFFOLD][1], "p142_last_heading": True},
        "producer_terminal_validation_present": False,
        "archive_recovery_validation": True,
        "producer_roots_mutated_by_recovery": False,
        "global_build_run": False,
        "render_run": False,
        "ocr_run": False,
        "next_cursor": "PDF one-based p.142 / printed p.143, continuation of Proposition 6.1.10",
    }
    french_validation = {
        "schema": "ega_french_archive_recovery_validation_v1",
        "status": "PASS_ARCHIVE_RECOVERY_DIPLOMATIC_FRENCH_THROUGH_P142_AND_PAIRED_ENGLISH_ONE_MATHEMATICAL_PRECISION_REPAIR__READY_PRINTED_P143",
        "errors": [],
        "printed_page": 142,
        "pdf_one_based_page": 141,
        "admitted_through": "exact words un ensemble ferme F contenant in the open argument of Proposition 6.1.10",
        "next_cursor": "PDF one-based p.142 / printed p.143, continuation of Proposition 6.1.10",
        "french_sources": french_source_rows,
        "french_source_control": {
            "source_files": 10,
            "source_bytes": 554671,
            "source_lines": 11733,
            "chapter1_sections_3_through_6_bytes": 153709,
            "chapter1_sections_3_through_6_lines": 3305,
            "environment_begin_count": 170,
            "environment_end_count": 170,
            "enumerate_begin_count": 16,
            "enumerate_end_count": 16,
            "ega1_6_environment_begin_count": 15,
            "ega1_6_environment_end_count": 15,
            "p142_marker_count": 1,
            "p143_marker_count": 0,
            "intentional_open_source_environments": [],
            "unresolved_readings": 0,
            "source_corrections": 0,
            "p142_append_bytes": 3844,
            "p142_append_sha256": "3F80CD616F841F25010329244BD545AA03A652B5F18BAE50BA863CF3696BE95E",
            "inverse_replay_bytes": 5074,
            "inverse_replay_sha256": "75A77003BDC90E8F0809F0DBF324A1F45268BC7A39C557D5A78C62816168B95B",
        },
        "authority": english_validation["authority"],
        "decision_ledgers": ledger_info,
        "paired_english": {
            "source_bytes": 54751,
            "source_sha256": "EBFAFDE5100D7B2D956AF1B98ACF7948717C8384F2D4C45347E1278EE77D9EA9",
            "manifest_generation": "R90",
            "manifest_sha256": EXPECTED[R90_MANIFEST][1],
            "mathematical_precision_repairs": 1,
            "unsupported_corrections": 0,
        },
        "bounded_build": {
            **french_log,
            "passes": 3,
            "pdf_bytes": FRENCH_BUILD_EXPECTED["chapter1-p79-142-check-r2.pdf"][0],
            "pdf_sha256": FRENCH_BUILD_EXPECTED["chapter1-p79-142-check-r2.pdf"][1],
            "terminal_layout_bytes": FRENCH_BUILD_EXPECTED["chapter1-p79-142-check-r2-terminal-pages-43-44-layout.txt"][0],
            "terminal_layout_sha256": FRENCH_BUILD_EXPECTED["chapter1-p79-142-check-r2-terminal-pages-43-44-layout.txt"][1],
            "warning_profile_matches_p141": True,
            "terminal_text_pass": True,
            "adverse_r1_preserved": True,
            "adverse_r1_undefined_hyperrefs": adverse_log["undefined_hyperrefs"],
        },
        "semantic_scaffold": english_validation["semantic_scaffold"],
        "producer_terminal_validation_present": False,
        "archive_recovery_validation": True,
        "producer_roots_mutated_by_recovery": False,
        "global_build_run": False,
        "render_run": False,
        "ocr_run": False,
    }
    base.write_bytes(temp_root, "controls/EGA1_CHAPTER1_P142_ARCHIVE_RECOVERY_VALIDATION.json", base.json_bytes(french_validation))
    base.write_bytes(temp_root, "controls/EGA_ENGLISH_R90_ARCHIVE_RECOVERY_VALIDATION.json", base.json_bytes(english_validation))
    return french_validation, english_validation


def build_private(temp_root: Path) -> dict[str, object]:
    for path, expected in EXPECTED.items():
        base.require_identity(path, expected)
    for name, expected in LEDGER_EXPECTED.items():
        base.require_identity(FRENCH_ROOT / "controls" / name, expected[:2])
    for name, expected in ENGLISH_BUILD_EXPECTED.items():
        base.require_identity(ENGLISH_RECOVERY_BUILD / name, expected)
    for name, expected in FRENCH_BUILD_EXPECTED.items():
        base.require_identity(FRENCH_RECOVERY_BUILD / name, expected)
    for name, expected in FRENCH_ADVERSE_EXPECTED.items():
        base.require_identity(FRENCH_ADVERSE_R1 / name, expected)

    manifest = json.loads(R90_MANIFEST.read_text(encoding="utf-8"))
    predecessor = json.loads(R89_MANIFEST.read_text(encoding="utf-8"))
    if (
        manifest.get("file_count") != 127
        or manifest.get("total_bytes") != 7281925
        or manifest.get("canonical_tree_sha256") != "F25D638DCFAA5654BF5ED53481009D6E2B3D94C4B1AB99AF5AAFECC0C1F1335A"
    ):
        raise RuntimeError("R90 manifest is not the accepted p.142 generation")
    before = {str(row["relative_path"]): row for row in predecessor["files"]}
    after = {str(row["relative_path"]): row for row in manifest["files"]}
    changed = sorted(
        path for path in after if path in before and (after[path]["bytes"], after[path]["sha256"]) != (before[path]["bytes"], before[path]["sha256"])
    )
    if changed != ["ega1/ega1-6.tex"] or set(before) != set(after):
        raise RuntimeError(f"unexpected R89/R90 delta: changed={changed}")

    copied_english = 0
    for row in manifest["files"]:
        rel = str(row["relative_path"])
        copy_exact(temp_root, f"source/english/{rel}", ENGLISH_ROOT / "source" / Path(rel), (int(row["bytes"]), str(row["sha256"])))
        copied_english += 1

    actual_french = sorted(
        path.relative_to(FRENCH_ROOT / "source").as_posix()
        for path in (FRENCH_ROOT / "source").rglob("*")
        if path.is_file()
    )
    if actual_french != sorted(FRENCH_SOURCE_EXPECTED):
        raise RuntimeError(f"French source membership mismatch: {actual_french}")
    for rel, expected in sorted(FRENCH_SOURCE_EXPECTED.items()):
        copy_exact(temp_root, f"source/french/{rel}", FRENCH_ROOT / "source" / Path(rel), expected)

    controls = {
        "controls/SOURCE_INPUT_SHA256_R89.json": R89_MANIFEST,
        "controls/SOURCE_INPUT_SHA256_R90.json": R90_MANIFEST,
        "controls/SOURCE_DIFF_VALIDATION_R88_PREDECESSOR.json": R88_VALIDATION,
        "controls/EGA1_CHAPTER1_P141_VALIDATION_R64_PREDECESSOR.json": R64_FRENCH_VALIDATION,
        "controls/EGA1_P142_ENGLISH_SECTION6_PREFIX_R1.tex": ENGLISH_PROJECTION,
        "controls/EGA1_P142_ENGLISH_BOUNDED_CHECK_R1.tex": ENGLISH_WRAPPER,
        "controls/chapter1-p79-142-check-r1.tex": FRENCH_WRAPPER_R1,
        "controls/chapter1-p79-142-check-r2.tex": FRENCH_WRAPPER_R2,
        "controls/PROJECT_LOGBOOK_METHODOLOGY_REPLICATION_DOI_REQUIREMENT_20260802.md": DUAL_DOI_CONTROL,
        "controls/SUCCESSOR_SESSION_BOOTSTRAP_AND_LOGBOOK_PROTOCOL_20260803.md": SUCCESSOR_PROTOCOL,
    }
    for rel, source in controls.items():
        copy_exact(temp_root, rel, source, EXPECTED[source])
    for name, expected in LEDGER_EXPECTED.items():
        copy_exact(temp_root, f"controls/{name}", FRENCH_ROOT / "controls" / name, expected[:2])
        validate_jsonl(temp_root / "controls" / name, expected[2])

    for name, expected in ENGLISH_BUILD_EXPECTED.items():
        copy_exact(temp_root, f"qa/english/recovered-r1/{name}", ENGLISH_RECOVERY_BUILD / name, expected)
    for name, expected in FRENCH_BUILD_EXPECTED.items():
        copy_exact(temp_root, f"qa/french/recovered-r2/{name}", FRENCH_RECOVERY_BUILD / name, expected)
    for name, expected in FRENCH_ADVERSE_EXPECTED.items():
        copy_exact(temp_root, f"qa/french/adverse-r1/{name}", FRENCH_ADVERSE_R1 / name, expected)

    copy_exact(temp_root, "semantic/EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P142.md", SCAFFOLD, EXPECTED[SCAFFOLD])
    copy_exact(temp_root, "provenance/FRENCH_PROJECT_LOGBOOK_THROUGH_P141_RAW.md", FRENCH_ROOT / "LOGBOOK.md", EXPECTED[FRENCH_ROOT / "LOGBOOK.md"])
    copy_exact(temp_root, "provenance/FRENCH_STATUS_THROUGH_P141_RAW.md", FRENCH_ROOT / "STATUS.md", EXPECTED[FRENCH_ROOT / "STATUS.md"])
    copy_exact(temp_root, "provenance/CONTINUATION_HANDOFF_THROUGH_P141_RAW.md", FRENCH_ROOT / "CONTINUATION_HANDOFF.md", EXPECTED[FRENCH_ROOT / "CONTINUATION_HANDOFF.md"])
    copy_exact(temp_root, "provenance/FRENCH_README_RAW.md", FRENCH_ROOT / "README.md", EXPECTED[FRENCH_ROOT / "README.md"])
    copy_exact(temp_root, "provenance/ENGLISH_RECHECK_LOGBOOK_THROUGH_P141_RAW.md", ENGLISH_ROOT / "LOGBOOK.md", EXPECTED[ENGLISH_ROOT / "LOGBOOK.md"])
    copy_exact(temp_root, "provenance/ENGLISH_RECHECK_STATUS_THROUGH_P141_RAW.md", ENGLISH_ROOT / "STATUS.md", EXPECTED[ENGLISH_ROOT / "STATUS.md"])

    rows = archive_recovery_rows()
    base.write_text(
        temp_root,
        "provenance/ARCHIVE_RECOVERY_DECISION_LOG_P142.jsonl",
        "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows),
    )
    validate_jsonl(temp_root / "provenance/ARCHIVE_RECOVERY_DECISION_LOG_P142.jsonl", len(rows))
    base.write_text(
        temp_root,
        "provenance/ARCHIVE_RECOVERY_CONTINUATION_HANDOFF_P142.md",
        "# EGA I p.142 archive recovery continuation\n\n"
        "This archive generation closes an interrupted bookkeeping boundary without altering the producer roots. The exact diplomatic French source, paired English correction, three producer p.142 ledgers, R89/R90 manifests, wrappers, and pre-Stacks scaffold were stable and coherent. Producer LOGBOOK, STATUS, and CONTINUATION files stop at their sealed p.141 entry and are preserved with that scope in their public names.\n\n"
        "Archive recovery then ran only the two missing bounded checks, sequentially and outside the producer roots: three successful XeLaTeX passes for the 32-page English wrapper and three for the 44-page French R2 wrapper. No global build, render, OCR, source mutation, or image load occurred. The existing French R1 build is preserved as adverse history because it retained one newly introduced undefined bounded target; R2 adds only that wrapper target and restores the p.141 warning profile.\n\n"
        "Admitted source cursor: printed p.142 through the exact French words `un ensemble ferme F contenant` and English words `a closed set F containing` in the open argument of Proposition 6.1.10. Next cursor: NUMDAM PDF one-based p.142 / printed p.143, continuation of that argument. EGA I and the eight-publication EGA corpus remain incomplete.\n",
    )

    french_validation, english_validation = build_recovery_validations(temp_root, manifest)
    base.write_text(
        temp_root,
        "PRIVATE_CUSTODY_README.md",
        "# Private exact custody: EGA I printed p.142 archive recovery\n\n"
        "This immutable raw snapshot preserves the exact stable p.142 producer bytes and separately identified archive recovery QA. Producer LOGBOOK/STATUS/CONTINUATION surfaces are preserved exactly through their p.141 terminal entries; the complete p.142 rationale lives in the exact producer ledgers plus the separate archive recovery decision and continuation files. The NUMDAM authority PDF and authority-page image are not copied. Producer roots were not modified.\n",
    )
    private_rows = base.rows_for_tree(temp_root, {"PRIVATE_CUSTODY_MANIFEST.csv", "PRIVATE_CUSTODY_VALIDATION.json"})
    base.write_manifest(temp_root / "PRIVATE_CUSTODY_MANIFEST.csv", private_rows)
    validation = {
        "status": "PASS_PRIVATE_EXACT_CUSTODY_EGA_I_P142_R90_ARCHIVE_RECOVERY",
        "errors": [],
        "printed_page": 142,
        "next_cursor": "PDF one-based p.142 / printed p.143, continuation of Proposition 6.1.10",
        "english_source_files": copied_english,
        "english_source_bytes": int(manifest["total_bytes"]),
        "english_source_tree_sha256": manifest["canonical_tree_sha256"],
        "french_source_files": len(FRENCH_SOURCE_EXPECTED),
        "french_source_bytes": sum(item[0] for item in FRENCH_SOURCE_EXPECTED.values()),
        "represented_files": len(private_rows),
        "represented_bytes": sum(int(row["bytes"]) for row in private_rows),
        "canonical_tree_sha256": base.canonical_tree_sha(private_rows),
        "producer_terminal_validation_present": False,
        "archive_recovery_validations": {
            "french_status": french_validation["status"],
            "english_status": english_validation["status"],
        },
        "authority_pdfs_included": 0,
        "authority_page_images_included": 0,
        "producer_roots_mutated": False,
    }
    base.write_bytes(temp_root, "PRIVATE_CUSTODY_VALIDATION.json", base.json_bytes(validation))
    return validation


def scan_public(root: Path) -> dict[str, object]:
    return prev.scan_public(root)


def build_public(temp_root: Path, private_root: Path, private_validation: dict[str, object]) -> dict[str, object]:
    path_map = {
        "semantic/EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P142.md": "02_EGA_PRESTACKS_MACHINE_READABLE_INDEXING_SCAFFOLD_P142.md",
        "provenance/FRENCH_PROJECT_LOGBOOK_THROUGH_P141_RAW.md": "03_EGA_FRENCH_PROJECT_LOGBOOK_THROUGH_P141_PUBLIC_PRIVACY_CLEAN.md",
        "provenance/ENGLISH_RECHECK_LOGBOOK_THROUGH_P141_RAW.md": "04_EGA_ENGLISH_RECHECK_LOGBOOK_THROUGH_P141_PUBLIC_PRIVACY_CLEAN.md",
        "provenance/ARCHIVE_RECOVERY_CONTINUATION_HANDOFF_P142.md": "05_EGA_P142_ARCHIVE_RECOVERY_CONTINUATION_HANDOFF.md",
        "provenance/FRENCH_STATUS_THROUGH_P141_RAW.md": "06_EGA_FRENCH_STATUS_THROUGH_P141_PUBLIC_PRIVACY_CLEAN.md",
        "provenance/ENGLISH_RECHECK_STATUS_THROUGH_P141_RAW.md": "07_EGA_ENGLISH_STATUS_THROUGH_P141_PUBLIC_PRIVACY_CLEAN.md",
        "controls/EGA1_CHAPTER1_P142_ARCHIVE_RECOVERY_VALIDATION.json": "08a_EGA1_CHAPTER1_P142_ARCHIVE_RECOVERY_VALIDATION.json",
        "controls/EGA_ENGLISH_R90_ARCHIVE_RECOVERY_VALIDATION.json": "08b_EGA_ENGLISH_R90_ARCHIVE_RECOVERY_VALIDATION.json",
        "controls/FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P142_20260804.jsonl": "09a_FRENCH_DIPLOMATIC_TRANSCRIPTION_APPEND_P142_20260804.jsonl",
        "controls/ENGLISH_CORRECTION_RECHECK_APPEND_P142_20260804.jsonl": "09b_ENGLISH_CORRECTION_RECHECK_APPEND_P142_20260804.jsonl",
        "controls/WORKFLOW_ERROR_APPEND_P142_20260804.jsonl": "09c_WORKFLOW_ERROR_APPEND_P142_20260804.jsonl",
        "provenance/ARCHIVE_RECOVERY_DECISION_LOG_P142.jsonl": "09d_EGA_P142_ARCHIVE_RECOVERY_DECISION_LOG.jsonl",
    }
    excluded = {"PRIVATE_CUSTODY_MANIFEST.csv", "PRIVATE_CUSTODY_VALIDATION.json", "PRIVATE_CUSTODY_README.md"}
    events: list[dict[str, object]] = []
    bindings: list[dict[str, object]] = []
    for source in sorted((path for path in private_root.rglob("*") if path.is_file())):
        private_rel = source.relative_to(private_root).as_posix()
        if private_rel in excluded:
            continue
        public_rel = path_map.get(private_rel, private_rel)
        raw = source.read_bytes()
        public = base.privacy_transform(public_rel, raw, events)
        base.write_bytes(temp_root, public_rel, public)
        bindings.append(
            {
                "private_relative_path": private_rel,
                "public_relative_path": public_rel,
                "private_bytes": len(raw),
                "private_sha256": base.sha256(raw),
                "public_bytes": len(public),
                "public_sha256": base.sha256(public),
                "transformed": raw != public,
            }
        )

    base.write_text(
        temp_root,
        "01_READ_ME_FIRST.md",
        "# EGA I diplomatic French / paired-English / pre-Stacks checkpoint through printed p.142\n\n"
        "This coherent source-and-provenance successor advances the public EGA I checkpoint from printed p.138 to p.142. It is not completion of EGA I or of the eight-publication EGA corpus. The existing complete EGA 0–IV English reader remains the front-facing default reader.\n\n"
        "The package preserves the exact p.142 diplomatic French source, the matching 127-file R90 English source tree, one reversible English precision repair, all p.142 producer decision/reversal/error ledgers, the pre-Stacks scaffold, predecessor logbooks/status through their actual p.141 boundary, and the separately labeled archive recovery that supplied only the missing bounded build and continuation evidence. Start with the archive continuation and the two recovery validators to see the exact boundary. The next source cursor is printed p.143.\n\n"
        "The NUMDAM authority PDF and authority-page image are identified by hash but are not duplicated in this source package. Existing readers and predecessor record versions remain intact.\n",
    )
    base.write_text(
        temp_root,
        "10_RIGHTS_AND_PROVENANCE.md",
        "# Rights and provenance\n\n"
        "The authority is the NUMDAM EGA corpus identified in the validators. No authority PDF, publisher scan, source-page raster, or third-party comparison file is included in this compact source successor. Underlying-work and scan rights remain with their rightsholders; no package-wide license is invented.\n\n"
        "French TeX is a diplomatic project transcription. English TeX is a separately ledgered source-rechecked project layer. Generated bounded PDFs and their QA sidecars are reproducibility evidence, not a critical edition or mathematician-review certification. Raw private logs remain in separate custody; public surfaces are minimally transformed and every replacement is hash-ledgered.\n",
    )
    base.write_text(
        temp_root,
        "09e_EGA_P142_ARCHIVE_PUBLIC_PROJECTION_ATTEMPT_LOG.jsonl",
        json.dumps(
            {
                "stable_id": "EG-EGA-ARCHIVE-P142-PUBLIC-PROJECTION-ATTEMPT-001",
                "classification": "public_projection_allowlist_failure_and_successor",
                "adverse_event": "the first public projection stopped before finalization because its exact build-log set contains three occurrences of the public TeX-toolchain contact address while the predecessor allowlist expected two",
                "exact_occurrence_surfaces": [
                    "qa/english/recovered-r1/EGA1_P142_ENGLISH_BOUNDED_CHECK_R1.log",
                    "qa/french/adverse-r1/chapter1-p79-142-check-r1.log",
                    "qa/french/recovered-r2/chapter1-p79-142-check-r2.log",
                ],
                "private_path_hits": 0,
                "private_email_hits": 0,
                "binary_private_hits": 0,
                "public_root_finalized_before_failure": False,
                "failed_temp_preserved_privately": True,
                "resolution": "raise only the exact public-toolchain-email count from two to three and rebuild into a fresh immutable public target",
                "pass": True,
            },
            ensure_ascii=False,
            sort_keys=True,
        )
        + "\n",
    )

    event_fields = ("relative_path", "transform_class", "original_token_bytes", "original_token_sha256", "replacement")
    with (temp_root / "11_PRIVACY_TRANSFORMATIONS.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=event_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(events)
    privacy = {
        "status": "PASS",
        "errors": [],
        "files_bound": len(bindings),
        "transformed_files": sum(1 for row in bindings if row["transformed"]),
        "transformation_events": len(events),
        "raw_private_source_mutated": False,
        "file_bindings": bindings,
    }
    base.write_bytes(temp_root, "12_PRIVACY_VALIDATION.json", base.json_bytes(privacy))
    privacy.update(scan_public(temp_root))
    base.write_bytes(temp_root, "12_PRIVACY_VALIDATION.json", base.json_bytes(privacy))

    payload_excluded = {
        "00_EGA_I_P142_Diplomatic_French_Paired_English_PreStacks_Source.zip",
        "13_PACKAGE_PAYLOAD_MANIFEST.csv",
        "14_ZENODO_UPLOAD_MANIFEST.csv",
        "15_PACKAGE_VALIDATION.json",
    }
    payload_rows = base.rows_for_tree(temp_root, payload_excluded)
    base.write_manifest(temp_root / "13_PACKAGE_PAYLOAD_MANIFEST.csv", payload_rows)
    zip_members = [str(row["relative_path"]) for row in payload_rows] + ["13_PACKAGE_PAYLOAD_MANIFEST.csv"]
    zip_identity = base.make_zip(
        temp_root / "00_EGA_I_P142_Diplomatic_French_Paired_English_PreStacks_Source.zip",
        temp_root,
        zip_members,
    )

    upload_rows: list[dict[str, object]] = []
    for rel in DIRECT_NAMES:
        data = (temp_root / rel).read_bytes()
        upload_rows.append(
            {
                "relative_path": rel,
                "bytes": len(data),
                "sha256": base.sha256(data),
                "ega_concept": "10.5281/zenodo.20414353",
                "methodology_concept": "10.5281/zenodo.21124403",
                "replication_concept": "10.5281/zenodo.20461174",
                "direct_public": "true",
            }
        )
    base.write_manifest(
        temp_root / "14_ZENODO_UPLOAD_MANIFEST.csv",
        upload_rows,
        ("ega_concept", "methodology_concept", "replication_concept", "direct_public"),
    )
    final_rows = base.rows_for_tree(temp_root, {"15_PACKAGE_VALIDATION.json"})
    validation = {
        "status": "PASS_READY_FOR_EXACT_ARCHIVE_CUSTODY_AND_THREE_CONCEPT_PUBLICATION",
        "errors": [],
        "scope": "EGA I diplomatic French and paired English through printed p.142; complete EGA remains in progress",
        "printed_page": 142,
        "next_cursor": "PDF one-based p.142 / printed p.143, continuation of Proposition 6.1.10",
        "private_custody": private_validation,
        "public_projection": {
            "files_before_validation": len(final_rows),
            "bytes_before_validation": sum(int(row["bytes"]) for row in final_rows),
            "canonical_tree_sha256": base.canonical_tree_sha(final_rows),
            "payload_manifest_rows": len(payload_rows),
            "zip": zip_identity,
            "direct_upload_objects": len(upload_rows),
        },
        "privacy": privacy,
        "quality_boundary": {
            "producer_logbook_status_continuation_through": "printed p.141",
            "producer_p142_ledgers": "complete and directly public",
            "archive_recovery_validation": True,
            "global_build_run": False,
            "render_run": False,
            "ocr_run": False,
            "mathematician_review_claimed": False,
        },
        "rights": {
            "authority_pdfs_included": 0,
            "authority_page_images_included": 0,
            "third_party_comparison_files_included": 0,
            "package_wide_license_invented": False,
        },
        "routing": {
            "ega_existing_concept": "10.5281/zenodo.20414353",
            "methodology_existing_concept": "10.5281/zenodo.21124403",
            "replication_existing_concept": "10.5281/zenodo.20461174",
            "new_concept_authorized": False,
            "fac_payload_included": False,
            "gaga_payload_included": False,
        },
    }
    base.write_bytes(temp_root, "15_PACKAGE_VALIDATION.json", base.json_bytes(validation))
    final_privacy = scan_public(temp_root)
    if (
        final_privacy["residual_private_patterns"] != 0
        or final_privacy["remaining_email_addresses"] != 0
        or final_privacy["binary_private_hits"] != 0
        or final_privacy["mandated_task_id_exceptions"] != 3
        or final_privacy["public_toolchain_email_occurrences"] != 3
    ):
        raise RuntimeError(f"final privacy replay failed: {final_privacy}")
    return validation


def main() -> None:
    if PRIVATE_FINAL.exists():
        private = json.loads((PRIVATE_FINAL / "PRIVATE_CUSTODY_VALIDATION.json").read_text(encoding="utf-8"))
        if private.get("status") != "PASS_PRIVATE_EXACT_CUSTODY_EGA_I_P142_R90_ARCHIVE_RECOVERY" or private.get("errors") != []:
            raise RuntimeError("existing immutable private custody root is not the accepted p.142 generation")
        rows = list(csv.DictReader((PRIVATE_FINAL / "PRIVATE_CUSTODY_MANIFEST.csv").open(encoding="utf-8", newline="")))
        for row in rows:
            path = PRIVATE_FINAL / str(row["relative_path"])
            if base.identity(path) != (int(row["bytes"]), str(row["sha256"])):
                raise RuntimeError(f"existing private custody replay mismatch: {row['relative_path']}")
        if base.canonical_tree_sha(rows) != private.get("canonical_tree_sha256"):
            raise RuntimeError("existing private custody canonical tree replay mismatch")
    else:
        private = base.atomic_build(PRIVATE_FINAL, build_private)
    public = base.atomic_build(PUBLIC_FINAL, build_public, PRIVATE_FINAL, private)
    summary = {
        "status": "PASS",
        "private_root": str(PRIVATE_FINAL),
        "private_files": len([path for path in PRIVATE_FINAL.rglob("*") if path.is_file()]),
        "private_bytes": sum(path.stat().st_size for path in PRIVATE_FINAL.rglob("*") if path.is_file()),
        "private_tree_sha256": private["canonical_tree_sha256"],
        "public_root": str(PUBLIC_FINAL),
        "public_files": len([path for path in PUBLIC_FINAL.rglob("*") if path.is_file()]),
        "public_bytes": sum(path.stat().st_size for path in PUBLIC_FINAL.rglob("*") if path.is_file()),
        "public_tree_sha256": public["public_projection"]["canonical_tree_sha256"],
        "zip": public["public_projection"]["zip"],
        "direct_upload_objects": public["public_projection"]["direct_upload_objects"],
        "privacy_events": public["privacy"]["transformation_events"],
        "privacy_errors": public["privacy"]["errors"],
    }
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
