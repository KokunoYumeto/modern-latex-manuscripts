#!/usr/bin/env python3
"""Freeze and public-project the complete Korean Noether P04 producer draft.

The exact producer handoff covers the T08-T09 delta, scoped reproducibility
evidence, and the current methodology retrospective.  Archive custody also
freezes the bounded coherent 83-file Paper 4 root so the public successor can
preserve all fifty producer-draft TeX units rather than falsely presenting a
delta as the whole paper.  Every source byte remains immutable in private
custody; the public tree is a separately manifested privacy projection.
"""

from __future__ import annotations

import json
import re
import zipfile
from pathlib import Path

import build_korean_noether_unchecked_public_snapshots_20260804 as archive


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = archive.SOURCE_BASE / "noether_paper04_ko_translation_001_20260804"
PRIVATE_ROOT = (
    archive.CJK_CONTROL.parent
    / "90_logs"
    / "private_archive_custody"
    / "KOREAN_NOETHER_P04_COMPLETE_PRODUCER_DRAFT_20260804_r1"
)
PUBLIC_ROOT = (
    REPO_ROOT
    / "sources"
    / "noether"
    / "korean-unchecked-paper-04-complete-producer-draft-20260804"
)
PUBLIC_PACKAGE = PUBLIC_ROOT / "P04_COMPLETE"
METHOD_SOURCE = archive.METHODOLOGY_SOURCE
POINTER_V004 = archive.POINTER_SOURCE.parent / "NOETH_DE_AUTHORITY_POINTER_v004_20260804.json"
POLICY = archive.ARCHIVE_WIDE_POLICY
DECISION_LOG = archive.CJK_CONTROL / "CJK_DECISION_LOGBOOK_20260718.md"

HANDOFF_LOG_BYTES = 672_667
HANDOFF_LOG_SHA256 = "70E8ABAE634913B38DE0FDEAD5F9376647FDBC9CD4A7B48127C22062BE6F407C"
METHOD_BYTES = 157_357
METHOD_SHA256 = "DEEEBF4DD2B583DDAC97225965408A8A5DB06C50FE96E394BFA65D8CDC674006"
POINTER_BYTES = 16_536
POINTER_SHA256 = "A1C62FDACAA34DFC1B806DC18258F2E732539F7AE9D85AA4BD9E1067B8749D9F"

SELECTED_ROOT = {
    "targets/Noether_P04_Korean_T08_U39_UNCHECKED.tex": (3_375, "D5F068657C9E22A823C55E865C63990E559102F90329F9F1717A8313B03F6BEE"),
    "targets/Noether_P04_Korean_T08_U40_UNCHECKED.tex": (3_201, "9CD0BF3111D5239DA9B4E60F8F8B1E877F551A962485628A9E23866A80718A98"),
    "targets/Noether_P04_Korean_T08_U41_UNCHECKED.tex": (2_953, "C943587E0D0AB85E9DE341529F005C12DA8E6AED8B123F222C3B62FFB5FD316E"),
    "targets/Noether_P04_Korean_T08_U42_UNCHECKED.tex": (2_265, "FC0E0CEF4FE64A66E0D928A11433602B51230FC91B88F6797681955F5E99BF5E"),
    "targets/Noether_P04_Korean_T08_U43_UNCHECKED.tex": (3_878, "A0E31D058D3FD8B86F05CED6278E14124714B1019CBAC6ACB99614DD45616CE6"),
    "targets/Noether_P04_Korean_T08_U44_UNCHECKED.tex": (3_091, "9463F17C69AF95C2182C19281714DAA7C0DFFEF0F25CCC303C783D06504982CA"),
    "targets/Noether_P04_Korean_T09_U45_UNCHECKED.tex": (967, "A3855C2333A2C49CCC450510237915A722E6C1325DE0EB1B590B823183449311"),
    "targets/Noether_P04_Korean_T09_U46_UNCHECKED.tex": (3_268, "46E36FAA42AFB76E8862B663F5F6C8FC95C37FB5EB37F7DD2CB02588E7C8D6EE"),
    "targets/Noether_P04_Korean_T09_U47_UNCHECKED.tex": (1_487, "9AAA9B2C6C361DE17EF42CC35DE661535482F1B4255EF916206BDE35FAAD4BBC"),
    "targets/Noether_P04_Korean_T09_U48_UNCHECKED.tex": (2_547, "8FE88B0477EEBCF7D038471D656F1AF0325060369FD7F5FDEFF8180AF8162F5F"),
    "targets/Noether_P04_Korean_T09_U49_UNCHECKED.tex": (967, "3B4AAACCAAE9E1FB3E3FB99D99ADA033E36EC068AA6E34632DB6A14950284F48"),
    "targets/Noether_P04_Korean_T09_U50_UNCHECKED.tex": (572, "218EF90531A8B0D9F2298E6BF340FC0D702848AD8BCF763E29D6A71C4DF0D036"),
    "SOURCE_CUSTODY_T08_T09.md": (3_820, "ED3E8CB66C2AEBADBD1FEC4DB667ECA31A68CB8BA3AF7717957A65B00DACE50A"),
    "STATUS_T08_T09.md": (1_759, "31E60DDC34ACE572737A120D923B23A1CE5CB7950B7032EDB7BCAF3A76237A3E"),
    "CHECKER_HANDOFF_T08_T09_U39_U50.md": (2_111, "041480091F0A76C78226B6228964EEB0364924ED2F1755068D6F66C935D2FFB9"),
    "TRANSLATION_CHOICES_T08_T09.md": (3_748, "73E67D6C72B59697B21BCDEE25AA564B972993F8FBE66CDD37A46125E0BE95CF"),
    "evidence/build_and_validate_evidence.mjs": (97_898, "FAE4F778335827E39A4C9A63F06E021C11CB7F01E141F627BC28DC221652B93B"),
    "evidence/README.md": (1_275, "86D70E333C3B378CDA884925CF032BD7FF61656102D829BD60E4C5E5EE6B9BE9"),
    "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.jsonl": (761_416, "0C02E60D776CBEB98138BA14D74BFC3958090E78B95A729CB84EE3D88AA0C916"),
    "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.csv": (660_699, "DF2F053163A67EF8A00D56EA1247B4C233039DB4F21295E47AE68D40D56CD0B5"),
    "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX.schema.json": (10_849, "3F660E3196A853DCD97C203B253666DA376B8438789014D6B24A6D69058D728E"),
    "evidence/structural_index/PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json": (6_231, "0694DBB43C144D6ED38DEF8CF252DFCAA49B5631752BE945184F374B0CD7D324"),
    "evidence/difficulty_ledger/DIFFICULTY_LEDGER.jsonl": (14_494, "2A417EF267947F289793FE6E2BDA90E80377236C0A000D6B78ADA8713FC61CEB"),
    "evidence/difficulty_ledger/DIFFICULTY_LEDGER.csv": (12_345, "2997996277DDA29F2C86345AE9878165C4F2AC24931E77E37107B1CF5394D183"),
    "evidence/difficulty_ledger/DIFFICULTY_LEDGER.schema.json": (7_612, "2C23D57A688C1769AC1892ACB1C1CD5673589D532A3D7994644E36BC3F52748C"),
    "evidence/difficulty_ledger/DIFFICULTY_LEDGER_VALIDATION_REPORT.json": (1_473, "7439585F6A4B9B4025AF707C4D0DC6BE369872789E84264CB72AC1BD7F6C3D8E"),
    "evidence/visual_evidence/VISUAL_EVIDENCE_INDEX.jsonl": (0, "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855"),
    "evidence/visual_evidence/VISUAL_EVIDENCE_INDEX.csv": (336, "21D69F53CDC3024AF4F62526C971257956ACAF138E30810EB20CEF8062F80C9E"),
    "evidence/visual_evidence/VISUAL_EVIDENCE_INDEX.schema.json": (6_031, "FDCBDEDDBFEB96168C18DD981303E63C59BE93132598D9AE43779287916BBF67"),
    "evidence/visual_evidence/VISUAL_EVIDENCE_INDEX_VALIDATION_REPORT.json": (1_088, "57582D5CE19AA4E260D15A1EB5933FEEDE49CBA2B55C40860648C7A6FA15048C"),
    "evidence/visual_evidence/STATUS.md": (460, "E8DCFAD042FF140F0ED12B741524718C31A2B56EBF66CED29DE510AC57318AA6"),
    "evidence/csv_artifact_validation/validate_csv_projections_artifact_tool.mjs": (6_656, "1A4D6941F73FC56F282276C389C4585E6F7461EC973E031046A46CF3387DD2D2"),
    "evidence/csv_artifact_validation/CSV_PROJECTIONS_ARTIFACT_TOOL_VALIDATION_REPORT.json": (5_062, "9E0F83820783F2A8E185D7EA8BAA41AD1EE279FD346B44B221ECC6B2EFE44C28"),
}

CORRECTION_SOURCES = {
    "70_KO_P01_P05_P07_P41_P42_SNAPSHOT_VALIDATION_20260804.json": (
        REPO_ROOT / "sources/noether/korean-unchecked-papers-01-05-07-41-42-20260804/SNAPSHOT_VALIDATION.json",
        8_649,
        "87DDD1BDA6ED67A9EFC151EF377BDE80A1BD560A5D4F2D728E8480D42F18E0C3",
        7,
    ),
    "70f_KO_P03__92_SNAPSHOT_VALIDATION.json": (
        REPO_ROOT / "sources/noether/korean-unchecked-paper-03-20260804/SNAPSHOT_VALIDATION.json",
        6_217,
        "063CCDA2804D1165538400C4F9229D79E95E1965394A439F240222452A7CEFA8",
        9,
    ),
    "70g_KO_P04_T04_T06__92_SNAPSHOT_VALIDATION.json": (
        REPO_ROOT / "sources/noether/korean-unchecked-paper-04-t04-t06-20260804/SNAPSHOT_VALIDATION.json",
        3_149,
        "0A7D64A02A2E2BE30B05A031AB0E7A7B1F8D07BFBDF96E4CA79A2B548461FBC2",
        1,
    ),
    "70h_KO_P04_T07__92_SNAPSHOT_VALIDATION.json": (
        REPO_ROOT / "sources/noether/korean-unchecked-paper-04-t07-20260804/SNAPSHOT_VALIDATION.json",
        3_071,
        "3B1A84ACA62011B58769679E33EA32F53CA4BD3060BFFBD73C00E7CDA4DE30C7",
        1,
    ),
}

def escaped_windows_path_bytes(path: Path) -> bytes:
    return str(path).replace("\\", "\\\\").encode("utf-8")


ESCAPED_USER_ROOT_BYTES = escaped_windows_path_bytes(archive.USER_PROFILE_ROOT)
ESCAPED_REPLACEMENTS = (
    (
        escaped_windows_path_bytes(archive.INTERLANGUAGE_ROOT),
        b"${PUBLIC_INTERLANGUAGE_ROOT}",
    ),
    (escaped_windows_path_bytes(archive.PAPERS_ROOT), b"${PUBLIC_PAPERS_ROOT}"),
    (
        escaped_windows_path_bytes(archive.DOCUMENTS_ROOT),
        b"${PUBLIC_DOCUMENTS_ROOT}",
    ),
    (ESCAPED_USER_ROOT_BYTES, b"${PRIVATE_USER_ROOT}"),
)

GENERIC_USER_PATH_REPLACEMENTS = (
    (
        "ESCAPED_GENERIC_INTERLANGUAGE_ROOT",
        re.compile(rb"(?i)[A-Z]:\\\\Users\\\\[^\\\\\"\r\n]+\\\\Documents\\\\interlanguage"),
        b"${PUBLIC_INTERLANGUAGE_ROOT}",
    ),
    (
        "ESCAPED_GENERIC_PAPERS_ROOT",
        re.compile(rb"(?i)[A-Z]:\\\\Users\\\\[^\\\\\"\r\n]+\\\\Documents\\\\Papors"),
        b"${PUBLIC_PAPERS_ROOT}",
    ),
    (
        "ESCAPED_GENERIC_DOCUMENTS_ROOT",
        re.compile(rb"(?i)[A-Z]:\\\\Users\\\\[^\\\\\"\r\n]+\\\\Documents"),
        b"${PUBLIC_DOCUMENTS_ROOT}",
    ),
    (
        "ESCAPED_GENERIC_USER_ROOT",
        re.compile(rb"(?i)[A-Z]:\\\\Users\\\\[^\\\\\"\r\n]+"),
        b"${PRIVATE_USER_ROOT}",
    ),
    (
        "GENERIC_INTERLANGUAGE_ROOT",
        re.compile(rb"(?i)[A-Z]:\\Users\\[^\\\"\r\n]+\\Documents\\interlanguage"),
        b"${PUBLIC_INTERLANGUAGE_ROOT}",
    ),
    (
        "GENERIC_PAPERS_ROOT",
        re.compile(rb"(?i)[A-Z]:\\Users\\[^\\\"\r\n]+\\Documents\\Papors"),
        b"${PUBLIC_PAPERS_ROOT}",
    ),
    (
        "GENERIC_DOCUMENTS_ROOT",
        re.compile(rb"(?i)[A-Z]:\\Users\\[^\\\"\r\n]+\\Documents"),
        b"${PUBLIC_DOCUMENTS_ROOT}",
    ),
    (
        "GENERIC_USER_ROOT",
        re.compile(rb"(?i)[A-Z]:\\Users\\[^\\\"\r\n]+"),
        b"${PRIVATE_USER_ROOT}",
    ),
)


def transform_public(data: bytes, label: str) -> tuple[bytes, list[tuple[str, int]]]:
    value = data
    applied: list[tuple[str, int]] = []
    for index, (old, new) in enumerate(ESCAPED_REPLACEMENTS, start=1):
        count = value.lower().count(old.lower())
        if count:
            value = re.sub(re.escape(old), lambda _: new, value, flags=re.IGNORECASE)
            applied.append((f"ESCAPED_JSON_PRIVATE_PATH_{index}", count))
    for rule_id, pattern, replacement in GENERIC_USER_PATH_REPLACEMENTS:
        value, count = pattern.subn(replacement, value)
        if count:
            applied.append((rule_id, count))
    value, standard = archive.transform_text(value)
    applied.extend(standard)
    archive.assert_privacy_clean(label, value)
    if re.search(rb"(?i)[A-Z]:\\\\Users\\\\", value):
        raise RuntimeError(f"Escaped Windows user path remains in {label}")
    return value, applied


def exact_prefix(path: Path, size: int, digest: str, label: str) -> bytes:
    data = path.read_bytes()[:size]
    if len(data) != size or archive.sha256_bytes(data) != digest:
        raise RuntimeError(f"Exact append-only prefix changed: {label}")
    return data


def write_projected(
    destination: Path,
    source_label: str,
    source_data: bytes,
    projection_rows: list[dict],
    privacy_rows: list[dict],
    disposition: str,
) -> bytes:
    public, applied = transform_public(source_data, source_label)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(public)
    projection_rows.append(
        {
            "relative_path": destination.relative_to(PUBLIC_PACKAGE).as_posix(),
            "source_label": source_label,
            "source_bytes": len(source_data),
            "source_sha256": archive.sha256_bytes(source_data),
            "public_bytes": len(public),
            "public_sha256": archive.sha256_bytes(public),
            "privacy_transformations": sum(count for _, count in applied),
            "disposition": disposition,
        }
    )
    for rule, count in applied:
        privacy_rows.append(
            {
                "relative_path": destination.relative_to(PUBLIC_PACKAGE).as_posix(),
                "rule_id": rule,
                "occurrences": count,
                "effect": "replace private local-path or operator token only; mathematical/source text otherwise unchanged",
            }
        )
    return public


def zip_replay(path: Path, expected_members: int) -> dict:
    rows = []
    with zipfile.ZipFile(path) as package:
        infos = [row for row in package.infolist() if not row.is_dir()]
        errors = []
        if len(infos) != expected_members or package.testzip() is not None:
            errors.append("member_count_or_crc")
        for info in infos:
            data = package.read(info)
            transform_public(data, f"zip:{info.filename}")
            rows.append(
                {
                    "relative_path": info.filename,
                    "bytes": len(data),
                    "sha256": archive.sha256_bytes(data),
                }
            )
    return {"status": "PASS" if not errors else "FAIL", "errors": errors, "members": len(rows), "member_identities": rows}


def main() -> int:
    if PRIVATE_ROOT.exists() or PUBLIC_ROOT.exists():
        raise RuntimeError("P04 complete output exists; frozen revisions are never overwritten")
    before = archive.inventory(SOURCE_ROOT)
    source_map = {row["relative_path"]: row for row in before}
    if len(SELECTED_ROOT) != 33 or sum(row[0] for row in SELECTED_ROOT.values()) != 1_633_934:
        raise RuntimeError("P04 exact root handoff declaration changed")
    for relative, expected in SELECTED_ROOT.items():
        row = source_map.get(relative)
        if row is None or (int(row["bytes"]), row["sha256"]) != expected:
            raise RuntimeError(f"P04 exact selected identity changed: {relative}")
    methodology = exact_prefix(METHOD_SOURCE, METHOD_BYTES, METHOD_SHA256, "methodology")
    decision_log = exact_prefix(DECISION_LOG, HANDOFF_LOG_BYTES, HANDOFF_LOG_SHA256, "decision log")
    if (POINTER_V004.stat().st_size, archive.sha256_file(POINTER_V004)) != (POINTER_BYTES, POINTER_SHA256):
        raise RuntimeError("Noether pointer v004 changed")
    targets = sorted(
        relative for relative in source_map if relative.startswith("targets/") and relative.endswith(".tex")
    )
    if len(targets) != 50 or not targets[0].endswith("U01_UNCHECKED.tex") or not targets[-1].endswith("U50_UNCHECKED.tex"):
        raise RuntimeError("P04 coherent 50-unit target closure changed")
    evidence = [relative for relative in source_map if relative.startswith("evidence/")]
    if len(evidence) != 17:
        raise RuntimeError("P04 scoped evidence boundary changed")

    PRIVATE_ROOT.mkdir(parents=True)
    PUBLIC_PACKAGE.mkdir(parents=True)
    archive.deterministic_zip(
        PRIVATE_ROOT / "P04_COMPLETE_83_FILE_ROOT_EXACT_PRIVATE_SNAPSHOT_20260804.zip",
        [(row["relative_path"], Path(row["path"]).read_bytes()) for row in before],
    )
    archive.write_csv(
        PRIVATE_ROOT / "P04_COMPLETE_ROOT_EXACT_MANIFEST.csv",
        ["relative_path", "bytes", "sha256", "handoff_disposition"],
        [
            {
                "relative_path": row["relative_path"],
                "bytes": row["bytes"],
                "sha256": row["sha256"],
                "handoff_disposition": (
                    "EXACT_20260804_COMPLETE_SUCCESSOR_SELECTION"
                    if row["relative_path"] in SELECTED_ROOT
                    else "ARCHIVE_COHERENT_P04_COMPLETION_SUPPLEMENT"
                ),
            }
            for row in before
        ],
    )
    archive.deterministic_zip(
        PRIVATE_ROOT / "P04_COMPLETE_34_FILE_EXACT_PRODUCER_HANDOFF_20260804.zip",
        [
            *[(relative, (SOURCE_ROOT / relative).read_bytes()) for relative in sorted(SELECTED_ROOT)],
            ("methodology/CJK_KOREAN_PRODUCTION_LESSONS_20260718.md", methodology),
        ],
    )
    archive.deterministic_zip(
        PRIVATE_ROOT / "P04_COMPLETE_COMMON_CONTROLS_EXACT_PRIVATE_20260804.zip",
        [
            ("CJK_DECISION_LOGBOOK_20260718.md", decision_log),
            (POINTER_V004.name, POINTER_V004.read_bytes()),
            (POLICY.name, POLICY.read_bytes()),
        ],
    )

    projection_rows: list[dict] = []
    privacy_rows: list[dict] = []
    for row in before:
        relative = row["relative_path"]
        write_projected(
            PUBLIC_PACKAGE / "producer_root" / relative,
            f"producer_root/{relative}",
            Path(row["path"]).read_bytes(),
            projection_rows,
            privacy_rows,
            (
                "EXACT_34_FILE_HANDOFF_COMPONENT"
                if relative in SELECTED_ROOT
                else "ARCHIVE_COHERENT_COMPLETE_P04_SUPPLEMENT"
            ),
        )
    method_public = write_projected(
        PUBLIC_PACKAGE / "methodology" / "CJK_KOREAN_PRODUCTION_LESSONS_20260718.md",
        "current_methodology_retrospective",
        methodology,
        projection_rows,
        privacy_rows,
        "EXACT_34_FILE_HANDOFF_COMPONENT",
    )
    log_public = write_projected(
        PUBLIC_PACKAGE / "controls" / "CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md",
        "append_only_cjk_decision_log_generation",
        decision_log,
        projection_rows,
        privacy_rows,
        "CURRENT_DECISION_REVERSAL_ERROR_HISTORY",
    )
    pointer_public = write_projected(
        PUBLIC_PACKAGE / "controls" / "NOETH_DE_AUTHORITY_POINTER_v004_20260804.json",
        "noether_authority_pointer_v004",
        POINTER_V004.read_bytes(),
        projection_rows,
        privacy_rows,
        "CURRENT_AUTHORITY_BINDING",
    )
    write_projected(
        PUBLIC_PACKAGE / "controls" / POLICY.name,
        "archive_wide_immediate_publication_policy",
        POLICY.read_bytes(),
        projection_rows,
        privacy_rows,
        "CONTROLLING_ARCHIVE_POLICY",
    )

    corrected_rows = []
    for remote_name, (source, expected_bytes, expected_sha, expected_hits) in CORRECTION_SOURCES.items():
        raw = source.read_bytes()
        if (len(raw), archive.sha256_bytes(raw)) != (expected_bytes, expected_sha):
            raise RuntimeError(f"Published validation correction source changed: {remote_name}")
        observed_hits = raw.lower().count(ESCAPED_USER_ROOT_BYTES.lower())
        if observed_hits != expected_hits:
            raise RuntimeError(f"Published validation privacy-hit count changed: {remote_name}")
        public = write_projected(
            PUBLIC_PACKAGE / "predecessor_privacy_corrections" / remote_name,
            f"public_record_21784732/{remote_name}",
            raw,
            projection_rows,
            privacy_rows,
            "SAME_FILENAME_PRIVACY_CORRECTED_SUCCESSOR",
        )
        corrected_rows.append(
            {
                "remote_filename": remote_name,
                "predecessor_record": 21784732,
                "predecessor_bytes": len(raw),
                "predecessor_sha256": archive.sha256_bytes(raw),
                "absolute_private_path_occurrences": expected_hits,
                "successor_bytes": len(public),
                "successor_sha256": archive.sha256_bytes(public),
                "supersession": "replace_live_same_filename; immutable predecessor retained as adverse history",
            }
        )

    correction_text = """# Privacy correction and append-only supersession

Anonymous raw inspection of Noether record 21784732 found four direct outer validation JSON files containing serialized absolute local user paths. The mathematical TeX, evidence, ZIP payloads, logbooks, and reader bytes were not implicated. This archive-layer defect is recorded rather than concealed.

This successor replaces the same four live filenames with minimally transformed privacy-clean projections. Exact predecessor bytes, hashes, and occurrence counts are bound in `PREDECESSOR_PRIVACY_CORRECTION_MANIFEST.csv`; immutable record 21784732 remains the adverse-history witness. No mathematical, Korean, German, formula, evidence, or state claim is changed.
"""
    archive.write_text(PUBLIC_PACKAGE / "PRIVACY_CORRECTION_AND_SUPERSESSION.md", correction_text)
    archive.write_csv(
        PUBLIC_PACKAGE / "PREDECESSOR_PRIVACY_CORRECTION_MANIFEST.csv",
        [
            "remote_filename",
            "predecessor_record",
            "predecessor_bytes",
            "predecessor_sha256",
            "absolute_private_path_occurrences",
            "successor_bytes",
            "successor_sha256",
            "supersession",
        ],
        corrected_rows,
    )
    archive.write_csv(
        PUBLIC_PACKAGE / "ARCHIVE_PUBLIC_PROJECTION_MANIFEST.csv",
        [
            "relative_path",
            "source_label",
            "source_bytes",
            "source_sha256",
            "public_bytes",
            "public_sha256",
            "privacy_transformations",
            "disposition",
        ],
        projection_rows,
    )
    archive.write_csv(
        PUBLIC_PACKAGE / "ARCHIVE_PRIVACY_TRANSFORMATIONS.csv",
        ["relative_path", "rule_id", "occurrences", "effect"],
        privacy_rows,
    )
    package_before_validation = archive.inventory(PUBLIC_PACKAGE)
    package_validation = {
        "schema": "korean_noether_p04_complete_producer_draft_public_snapshot_v1",
        "status": "PASS_PUBLIC_UNCHECKED_COMPLETE_PRODUCER_DRAFT",
        "errors": [],
        "producer_root_files": len(before),
        "producer_root_bytes": sum(int(row["bytes"]) for row in before),
        "producer_root_tree_sha256": archive.tree_sha(before),
        "producer_handoff_files": 34,
        "producer_handoff_bytes": 1_791_291,
        "producer_handoff_root_files": 33,
        "producer_handoff_root_bytes": 1_633_934,
        "methodology_bytes": METHOD_BYTES,
        "methodology_sha256": METHOD_SHA256,
        "target_units": 50,
        "target_scope": "P04 sections 1-9 complete producer-draft text coverage",
        "evidence_structural_scope": "T01-T03 only; never whole-P04 structural evidence",
        "evidence_files": 17,
        "visual_assets": 0,
        "privacy_transformations": sum(int(row["occurrences"]) for row in privacy_rows),
        "corrected_predecessor_direct_files": 4,
        "corrected_predecessor_private_path_occurrences": sum(int(row["absolute_private_path_occurrences"]) for row in corrected_rows),
        "state_labels": [
            "UNCHECKED",
            "complete producer-draft text coverage",
            "uncompiled",
            "unrendered",
            "unassembled",
            "unreviewed",
            "uncertified",
        ],
        "publication_is_approval": False,
        "release_hold": False,
        "package_files_excluding_this_validation": len(package_before_validation),
        "package_bytes_excluding_this_validation": sum(int(row["bytes"]) for row in package_before_validation),
        "package_tree_sha256_excluding_this_validation": archive.tree_sha(package_before_validation),
    }
    archive.write_json(PUBLIC_PACKAGE / "ARCHIVE_SNAPSHOT_VALIDATION.json", package_validation)
    package_members = [
        (path.relative_to(PUBLIC_PACKAGE).as_posix(), path.read_bytes())
        for path in sorted(
            (item for item in PUBLIC_PACKAGE.rglob("*") if item.is_file()),
            key=lambda item: item.relative_to(PUBLIC_PACKAGE).as_posix().casefold(),
        )
    ]
    public_zip = PUBLIC_ROOT / "P04_Korean_Complete_Producer_Draft_UNCHECKED_20260804.zip"
    archive.deterministic_zip(public_zip, package_members)

    direct_copies = {
        "01_STATUS_T08_T09.md": PUBLIC_PACKAGE / "producer_root" / "STATUS_T08_T09.md",
        "02_CHECKER_HANDOFF_T08_T09_U39_U50.md": PUBLIC_PACKAGE / "producer_root" / "CHECKER_HANDOFF_T08_T09_U39_U50.md",
        "03_TRANSLATION_CHOICES_T08_T09.md": PUBLIC_PACKAGE / "producer_root" / "TRANSLATION_CHOICES_T08_T09.md",
        "04_SOURCE_CUSTODY_T08_T09.md": PUBLIC_PACKAGE / "producer_root" / "SOURCE_CUSTODY_T08_T09.md",
        "05_PRIVACY_CORRECTION_AND_SUPERSESSION.md": PUBLIC_PACKAGE / "PRIVACY_CORRECTION_AND_SUPERSESSION.md",
        "06_CJK_PRODUCTION_METHODOLOGY_PRIVACY_CLEAN.md": PUBLIC_PACKAGE / "methodology" / "CJK_KOREAN_PRODUCTION_LESSONS_20260718.md",
        "70_KO_CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md": PUBLIC_PACKAGE / "controls" / "CJK_DECISION_LOGBOOK_PRIVACY_CLEAN_20260804.md",
        "70_KO_NOETH_DE_AUTHORITY_POINTER_v004_20260804.json": PUBLIC_PACKAGE / "controls" / "NOETH_DE_AUTHORITY_POINTER_v004_20260804.json",
    }
    for name, source in direct_copies.items():
        (PUBLIC_ROOT / name).write_bytes(source.read_bytes())
    correction_dir = PUBLIC_ROOT / "corrected_predecessor_validations"
    correction_dir.mkdir()
    for remote_name in CORRECTION_SOURCES:
        source = PUBLIC_PACKAGE / "predecessor_privacy_corrections" / remote_name
        (correction_dir / remote_name).write_bytes(source.read_bytes())

    index_path = PUBLIC_ROOT / "70i_KO_P04_COMPLETE_SNAPSHOT_INDEX_20260804.csv"
    archive.write_csv(
        index_path,
        [
            "scope",
            "producer_root_files",
            "producer_root_bytes",
            "producer_root_tree_sha256",
            "handoff_files",
            "handoff_bytes",
            "target_units",
            "evidence_scope",
            "public_zip",
            "public_zip_bytes",
            "public_zip_sha256",
            "public_zip_members",
            "privacy_corrections",
            "state",
        ],
        [
            {
                "scope": "P04_T01_T09_COMPLETE_PRODUCER_DRAFT",
                "producer_root_files": len(before),
                "producer_root_bytes": sum(int(row["bytes"]) for row in before),
                "producer_root_tree_sha256": archive.tree_sha(before),
                "handoff_files": 34,
                "handoff_bytes": 1_791_291,
                "target_units": 50,
                "evidence_scope": "T01-T03_ONLY",
                "public_zip": public_zip.name,
                "public_zip_bytes": public_zip.stat().st_size,
                "public_zip_sha256": archive.sha256_file(public_zip),
                "public_zip_members": len(package_members),
                "privacy_corrections": 4,
                "state": "UNCHECKED;complete_producer_draft_text;uncompiled;unrendered;unassembled;unreviewed;uncertified",
            }
        ],
    )
    readme_path = PUBLIC_ROOT / "README.md"
    archive.write_text(
        readme_path,
        """# Korean Noether Paper 4 complete producer-draft archive snapshot

The complete ZIP preserves all fifty privacy-clean Korean TeX producer-draft units for Paper 4 sections 1-9, the exact T08-T09 handoff, scoped evidence, decision/error history, source custody, and methodology. The evidence structural index covers T01-T03 only.

State: UNCHECKED, uncompiled, unrendered, unassembled, unreviewed, and uncertified. Publication preserves work; it is not approval. Four predecessor outer validation files are replaced on the live DOI by documented privacy-clean successors while their immutable predecessor bytes remain adverse history.
""",
    )
    root_before_validation = archive.inventory(PUBLIC_ROOT)
    root_validation = {
        "schema": "korean_noether_p04_complete_archive_closeout_v1",
        "status": "PASS_READY_FOR_PRIVACY_CORRECTIVE_SAME_CONCEPT_PUBLICATION",
        "errors": [],
        "package_validation": package_validation,
        "public_zip": {
            "filename": public_zip.name,
            "bytes": public_zip.stat().st_size,
            "sha256": archive.sha256_file(public_zip),
            "members": len(package_members),
        },
        "decision_log_public": {
            "bytes": len(log_public),
            "sha256": archive.sha256_bytes(log_public),
        },
        "methodology_public": {
            "bytes": len(method_public),
            "sha256": archive.sha256_bytes(method_public),
        },
        "pointer_public": {
            "bytes": len(pointer_public),
            "sha256": archive.sha256_bytes(pointer_public),
        },
        "corrected_remote_validations": corrected_rows,
        "public_root_files_excluding_this_validation": len(root_before_validation),
        "public_root_bytes_excluding_this_validation": sum(int(row["bytes"]) for row in root_before_validation),
        "public_root_tree_sha256_excluding_this_validation": archive.tree_sha(root_before_validation),
        "private_custody": {
            "producer_root_zip_bytes": (PRIVATE_ROOT / "P04_COMPLETE_83_FILE_ROOT_EXACT_PRIVATE_SNAPSHOT_20260804.zip").stat().st_size,
            "producer_root_zip_sha256": archive.sha256_file(PRIVATE_ROOT / "P04_COMPLETE_83_FILE_ROOT_EXACT_PRIVATE_SNAPSHOT_20260804.zip"),
            "exact_handoff_zip_bytes": (PRIVATE_ROOT / "P04_COMPLETE_34_FILE_EXACT_PRODUCER_HANDOFF_20260804.zip").stat().st_size,
            "exact_handoff_zip_sha256": archive.sha256_file(PRIVATE_ROOT / "P04_COMPLETE_34_FILE_EXACT_PRODUCER_HANDOFF_20260804.zip"),
        },
        "release_hold": False,
    }
    validation_path = PUBLIC_ROOT / "SNAPSHOT_VALIDATION.json"
    archive.write_json(validation_path, root_validation)

    after = archive.inventory(SOURCE_ROOT)
    if [(row["relative_path"], row["bytes"], row["sha256"]) for row in after] != [
        (row["relative_path"], row["bytes"], row["sha256"]) for row in before
    ]:
        raise RuntimeError("P04 producer root changed during coherent snapshot")
    final = archive.inventory(PUBLIC_ROOT)
    for row in final:
        if Path(row["path"]).suffix.lower() != ".zip":
            transform_public(Path(row["path"]).read_bytes(), row["relative_path"])
    replay = zip_replay(public_zip, len(package_members))
    if replay["status"] != "PASS":
        raise RuntimeError("P04 complete public ZIP replay failed")
    result = {
        **root_validation,
        "public_root": str(PUBLIC_ROOT),
        "public_root_files": len(final),
        "public_root_bytes": sum(int(row["bytes"]) for row in final),
        "public_root_tree_sha256": archive.tree_sha(final),
        "public_zip_replay": {key: value for key, value in replay.items() if key != "member_identities"},
        "validation_bytes": validation_path.stat().st_size,
        "validation_sha256": archive.sha256_file(validation_path),
        "index_bytes": index_path.stat().st_size,
        "index_sha256": archive.sha256_file(index_path),
        "readme_bytes": readme_path.stat().st_size,
        "readme_sha256": archive.sha256_file(readme_path),
        "private_custody_root": str(PRIVATE_ROOT),
    }
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
