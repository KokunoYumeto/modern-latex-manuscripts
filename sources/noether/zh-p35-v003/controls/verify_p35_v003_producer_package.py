#!/usr/bin/env python3
"""Mechanical producer-package verifier for Noether P35 Chinese revision 3.

This checks file identities, immutable predecessor custody, imported checker-return
custody, JSON/JSONL/Python syntax, graph integrity, target byte identities,
mechanical build-record fields, and optionally the root manifest. It never opens
or renders a PDF and performs no source, linguistic, semantic, formula,
terminology, native, regional, visual, approval, archive, publication, or
certification check.
"""

from __future__ import annotations

import argparse
import ast
from datetime import datetime
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "controls/P35_V003_PRODUCER_VERIFICATION.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def rel_path(root: Path, relative: str) -> Path:
    return root.joinpath(*relative.replace("\\", "/").split("/"))


def check(condition: bool, check_id: str, detail: str, checks: list[dict[str, object]]) -> None:
    checks.append({"id": check_id, "pass": bool(condition), "detail": detail})


def expected_file(
    checks: list[dict[str, object]], check_id: str, relative: str, size: int, digest: str
) -> None:
    path = rel_path(ROOT, relative)
    actual = "missing"
    ok = False
    if path.is_file():
        actual = f"{path.stat().st_size} bytes / {sha(path)}"
        ok = path.stat().st_size == size and sha(path) == digest
    check(ok, check_id, f"{relative}: expected {size} bytes / {digest}; actual {actual}", checks)


def parse_manifest(path: Path) -> list[tuple[str, int, str]]:
    entries: list[tuple[str, int, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        digest, size_text, relative = line.split("  ", 2)
        entries.append((digest.upper(), int(size_text), relative))
    return entries


def replay_manifest(
    root: Path,
    manifest: Path,
    *,
    expected_entries: int,
    compare_actual: bool,
    excluded_relative_paths: set[str] | None = None,
) -> tuple[bool, str]:
    if excluded_relative_paths is None:
        excluded_relative_paths = {manifest.relative_to(root).as_posix()}
    entries = parse_manifest(manifest)
    failures: list[str] = []
    paths = [relative for _, _, relative in entries]
    for digest, size, relative in entries:
        path = rel_path(root, relative)
        if not path.is_file():
            failures.append(f"missing:{relative}")
        elif path.stat().st_size != size:
            failures.append(f"bytes:{relative}")
        elif sha(path) != digest:
            failures.append(f"sha256:{relative}")
    extras: list[str] = []
    missing: list[str] = []
    if compare_actual:
        actual = sorted(
            path.relative_to(root).as_posix()
            for path in root.rglob("*")
            if path.is_file() and path.relative_to(root).as_posix() not in excluded_relative_paths
        )
        extras = sorted(set(actual) - set(paths))
        missing = sorted(set(paths) - set(actual))
    ok = (
        len(entries) == expected_entries
        and len(paths) == len(set(paths))
        and not failures
        and not extras
        and not missing
    )
    detail = (
        f"entries={len(entries)}; unique={len(set(paths))}; failures={failures}; "
        f"extras={extras}; missing={missing}"
    )
    return ok, detail


def verify_expected_identities(checks: list[dict[str, object]]) -> None:
    expected = [
        ("BINDER", "source/current/CHINESE_P35_BINDER_20260804.json", 6520, "CFE2D81FB1E5C74EC1F73A1076F6D002A895D01056A5CEE26F844F882AF70CF3"),
        ("SOURCE_NATIVE", "source/current/Noether_P35_Zenodo21699405_source_native_CRLF.tex", 34355, "2E205B2C51B9093FC61C77A9A1DF1C3399FCF098706CEC69134400F1ECC8E491"),
        ("SOURCE_LF", "source/current/Noether_P35_crosshead_LF.tex", 34091, "DAED6EF21C297425F018C0AE6B23BC5BDD05C0B86984B3FC25FB5937DCBEBD6A"),
        ("POINTER_CURRENT", "controls/canon_pointer_v005/CURRENT_GERMAN_AUTHORITY_POINTER.json", 19889, "42E6844BFCBFB2133E9AA323A823604351CF9C49550AFCF34ECAAF7887185660"),
        ("POINTER_IMMUTABLE", "controls/canon_pointer_v005/NOETH_DE_AUTHORITY_POINTER_v005_20260804.json", 19889, "42E6844BFCBFB2133E9AA323A823604351CF9C49550AFCF34ECAAF7887185660"),
        ("CHECKER_RECEIPT", "controls/checker_return_v002/sealed_return/P35_V002_CHECKER_RETURN_RECEIPT.json", 13785, "B850E0A3320D91787F72CD09A766F681672DF588D846C4307625AEA1B8C5DB69"),
        ("CHECKER_SUMMARY", "controls/checker_return_v002/sealed_return/P35_V002_CHECKER_RETURN_SUMMARY.md", 2855, "AF3611C4B01710444447B66EF5D1ED74DB90316DEAA4DD046556B18AA7E5DAFF"),
        ("CHECKER_MANIFEST", "controls/checker_return_v002/sealed_return/SHA256SUMS.txt", 5674, "36FE5550D4AEDC4E59C06C6636E081E7D2F7283E1B4055B38F410247DE038D74"),
        ("CHECKER_VERIFIER", "controls/checker_return_v002/sealed_return/P35_V002_RETURN_VERIFICATION.json", 16499, "BA6E7BFA29252839DF16D5CDF857E1652BE33184D4F949E448E5A4AF98854381"),
        ("CHECKER_SEAL", "controls/checker_return_v002/sealed_return/P35_V002_RETURN_SEAL.json", 2414, "AA7C524ED3CCCC48574F3763E541854FD6D43E6F53B47FB870365571E9B2B83A"),
        ("V002_SEED_MANIFEST", "controls/producer_seed_v002/SHA256SUMS_v002.txt", 16656, "733454A89830405E9D793E2565296C528BA0A5CAB1CE57177FA29C6E6EC886BD"),
        ("V002_SEED_HANDOFF", "controls/producer_seed_v002/CHINESE_PRODUCER_CORRECTED_RETURN_AND_CHECKER_REHANDOFF_v002.md", 6123, "547BAB055789AE141F83AC288C47AC4F75C7EA53D01E5002D2538EF673BE58AE"),
        ("HANS_SEG_A", "translation/corrected_segments_v002/P35_A_zh-Hans-CN_v002.tex", 11737, "26A7615B9EFD825ADF20DABF9DE34673CB1F52807AC7E07A0F0118F79E8DD3EF"),
        ("HANS_SEG_B", "translation/corrected_segments_v002/P35_B_zh-Hans-CN_v002.tex", 7451, "5A2EB988239E78102D18F22AC552978AD987CE299E5B6A0D738FFA87034B2424"),
        ("HANS_SEG_C", "translation/corrected_segments_v002/P35_C_zh-Hans-CN_v002.tex", 10620, "5F62E3139C5528ABCD4ACB978EA6CC14AF1B052E6E3E78CBAFBB10161B5B01B3"),
        ("HANS_TEX", "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex", 31328, "DDF7E898E706552028C2BCEAC4BBDE3D45487C6A339F7FA0A43968FF7E1F465C"),
        ("HANS_PDF", "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf", 274158, "F6626C3DC6FFB82E3CFD5C21FA3F74B99459D477E39093715802C49E91E2A18C"),
        ("REJECTED_HANT_V002_TEX", "build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.tex", 31515, "FD16882FAC33B7FD7D0FFB882345168E40FA7F1F22FDEE83AFA2420627D1C054"),
        ("REJECTED_HANT_V002_PDF", "build/zh-Hant-controlled-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v002.pdf", 306051, "8E77A4C511462C8ECF5876CE7EED0E3A9C4CAD8820A492BD8E665FB47FA50CF1"),
        ("HANT_V003_TEX", "build/zh-Hant-controlled-v003/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v003.tex", 31515, "54DE9B43850376FD19306A11FC682166D8F34A4CA6D73E0940695357CE74A005"),
        ("HANT_V003_PDF", "build/zh-Hant-controlled-v003/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v003.pdf", 284874, "65A449AA0E9C727BEA548C1A8190568636F8C05AB63593666065F956B40774FA"),
        ("HANT_V003_LOG", "build/zh-Hant-controlled-v003/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v003.log", 23191, "F8729C786730A84A83FB94FC6335768356BE3328DF74C72CB9670B07F7FA6573"),
        ("HANT_V003_AUX", "build/zh-Hant-controlled-v003/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v003.aux", 32, "BDE1D0FC7F1717473BB9238DC27CA9984E0220C9AEDA9654E16D5E91BB025EED"),
        ("HANT_SCANNER", "controls/build_hant_producer_v003.py", 14101, "6286FAA6325E47D36F8FD7886E9C22D99343CF015C60C15D123ACBF84C40982C"),
        ("HANT_BUILD_SCRIPT", "controls/compile_hant_producer_v003.py", 7532, "3142C89C5A4E7A18B6347F9BA224E07281498042F5459BD03C2BADEE06A7386F"),
        ("HANT_TRANSPORT_RECORD", "controls/OPENCC_PRODUCER_RECORD_v003.json", 7018, "D7087C586E78887CD5DB4339DDA6C5E9E535F5D8CF1EF6C15F07DBBF71549BFE"),
        ("HANT_BUILD_RECORD", "controls/HANT_MECHANICAL_BUILD_RECORD_v003.json", 7379, "2DB562C01A72D30171EEC4082A5D7B1746752C1FB6CBB3DB79788C9B25D43BA1"),
        ("HANT_WARNING_ANNEX", "controls/P35_HANT_V003_WARNING_ANNEX.json", 4606, "F9E1E38ED456DB2ECF4F9F4FB83100522D906FE58DC8190DEEFA7F84A42D1AEE"),
        ("F015_REALIZATION", "controls/P35_F015_PRODUCER_REALIZATION_RECORD.json", 8503, "2B6E82F1C53573CBA67AB377C794FBC64683A3BFDA374AC460710FB47288FB66"),
        ("RETURN_INTAKE", "controls/P35_V002_CHECKER_RETURN_INTAKE_RECEIPT.json", 5025, "73DD5DF67418298980EC3FBF247CDB9DE239DB894913FB65D617774F1D59E294"),
        ("POINTER_V005_RECEIPT", "controls/P35_CANON_CONTROL_UPDATE_V005_20260804.json", 5055, "65D5006944735F28305D743B67E638C9384B813449A60E14DE7DFE110070074C"),
        ("R3_FINDINGS", "evidence/revision3/P35_FINDING_DISPOSITION_R3.jsonl", 11888, "B9CD5DF7FA956422019E95F8860C977834E54298A62928F2629B4E0808F1357E"),
        ("R3_ADVERSE", "evidence/revision3/P35_ADVERSE_EVIDENCE_LEDGER_R3.jsonl", 5680, "0FDFDDA9D45EE1B5C368135FE628A4132A24AF24AF1A8F085DB9B24065718DAD"),
        ("R3_LOCALIZATION", "evidence/revision3/P35_LOCALIZATION_AND_CJKV_CROSSWALK_R3.jsonl", 5367, "6C44A4D076399A335CDB0587791CFF8BB4615904FF22191C75E7B8287168F4EA"),
        ("R3_GRAPH", "evidence/revision3/P35_CORRECTION_CONCEPT_EVIDENCE_GRAPH_R3.json", 12270, "634FE1EDC064A1C44E52363EFE680DFF8F2DEF47637253AD806EBB2D343CA477"),
        ("V003_RETURN", "worker_returns/P35_V003_PRODUCER_F015_RETURN.md", 5710, "FA0B18002CBDB2BC5874DE94B94CCA0557BEE33EED8BAC8FD5B3906F9C65677B"),
        ("V003_BUILD_REPORT", "BUILD_REPORT_V003.md", 2296, "23A262DDFACC8190E4A017FC3A1B4E4E6B5142325479F3F8A2B2B04BDEB36D40"),
        ("V003_STATUS", "STATUS_V003.md", 1240, "577C0B75350155F0B41D17DFCDD6CA2A565F07954A0842BB71F67966042669D8"),
        ("INTERRUPTED_FREEZE", "controls/P35_V003_INTERRUPTED_FREEZE_PROBE.md", 1955, "2FA7049AAF119C423ED510D21859CB8C0E4BEA08D59C25D8FCB9D6AB8FBB8629"),
        ("VERIFIER_FIRST_FAILURE_JSON", "controls/P35_V003_VERIFIER_FIRST_RUN_FAILURE.json", 18310, "D5DA71C9D126E244692BDFADBC3CFF433754079AB9F619D759C80EE0A90C4A2F"),
        ("VERIFIER_FIRST_FAILURE_MD", "controls/P35_V003_VERIFIER_FIRST_RUN_FAILURE.md", 1374, "6ACBA90864C342B4A788833F2923AB2353E4F0C5B9C6FB0642B22A207F7861E4"),
        ("VERIFIER_SECOND_FAILURE_JSON", "controls/P35_V003_VERIFIER_SECOND_RUN_FAILURE.json", 18310, "3688EFE8A07D430CBC77FA36E1D855327E379EF032FDF7C309A333550EF1E080"),
        ("VERIFIER_SECOND_FAILURE_MD", "controls/P35_V003_VERIFIER_SECOND_RUN_FAILURE.md", 1328, "BED8EA30ECE270363B7071A17C7B98DA7B0929E5625172E455CA323E253577D8"),
        ("FIRST_MANIFEST_ATTEMPT", "controls/P35_V003_FIRST_MANIFEST_ATTEMPT.txt", 29304, "952364985F93C5159563D27C847D6893AD36D6EB84D437017D5510D3D4B60196"),
        ("FIRST_MANIFEST_ATTEMPT_NOTE", "controls/P35_V003_FIRST_MANIFEST_ATTEMPT_FAILURE.md", 1322, "AB71F94B510E64965F6E07D68748BF1B53D06B9AE1EE480FC218C8C7C1B5A30C"),
        ("V003_MANIFEST_GENERATOR", "controls/generate_sha256_manifest_v003.py", 963, "D5FFD7875E00CF1ADB3C2BB5468ADD4653E2B62254F9361FC0134C045E8834FF"),
        ("V003_FREEZE_METADATA", "controls/P35_FREEZE_METADATA_V003.md", 5581, "68123DC6770F379E82DB171F7FCBF8D26FD49C528665777E30E35ED442401009"),
        ("V003_HANDOFF", "CHINESE_PRODUCER_V003_RETURN_AND_CHECKER_REHANDOFF.md", 7746, "5CF97EDDE0B832CAF17E084595F6C81D8C5A09DDF1D4F3D9FFF9F099F4EE419C"),
    ]
    for item in expected:
        expected_file(checks, *item)


def verify_syntax(checks: list[dict[str, object]]) -> None:
    json_count = 0
    jsonl_records = 0
    python_count = 0
    failures: list[str] = []
    for path in sorted(ROOT.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
            json_count += 1
        except Exception as exc:
            failures.append(f"json:{path.relative_to(ROOT)}:{exc}")
    for path in sorted(ROOT.rglob("*.jsonl")):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                json.loads(line)
                jsonl_records += 1
            except Exception as exc:
                failures.append(f"jsonl:{path.relative_to(ROOT)}:{lineno}:{exc}")
    for path in sorted(ROOT.rglob("*.py")):
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            python_count += 1
        except Exception as exc:
            failures.append(f"python:{path.relative_to(ROOT)}:{exc}")
    check(
        not failures,
        "SYNTAX_PARSE",
        f"json_files={json_count}; jsonl_records={jsonl_records}; python_files={python_count}; failures={failures}",
        checks,
    )


def verify_graph(checks: list[dict[str, object]]) -> None:
    path = ROOT / "evidence/revision3/P35_CORRECTION_CONCEPT_EVIDENCE_GRAPH_R3.json"
    graph = json.loads(path.read_text(encoding="utf-8"))
    node_ids = [node["id"] for node in graph["nodes"]]
    edge_ids = [edge["id"] for edge in graph["edges"]]
    node_types = set(graph["node_type_definitions"])
    edge_types = set(graph["edge_type_definitions"])
    bad_nodes = [node["id"] for node in graph["nodes"] if node["type"] not in node_types]
    bad_edges = [
        edge["id"]
        for edge in graph["edges"]
        if edge["type"] not in edge_types or edge["from"] not in node_ids or edge["to"] not in node_ids
    ]
    ok = (
        len(node_ids) == len(set(node_ids))
        and len(edge_ids) == len(set(edge_ids))
        and not bad_nodes
        and not bad_edges
    )
    check(ok, "TYPED_GRAPH", f"nodes={len(node_ids)}; edges={len(edge_ids)}; bad_nodes={bad_nodes}; bad_edges={bad_edges}", checks)


def verify_lineage(checks: list[dict[str, object]]) -> None:
    parent = ROOT.parent
    for revision, entries, digest in (
        ("001", 70, "44A91086C3736A94D042A2D0DAEC5B5DA88F179E8AF962AB06D202EC33F5888F"),
        ("002", 130, "733454A89830405E9D793E2565296C528BA0A5CAB1CE57177FA29C6E6EC886BD"),
    ):
        sibling = parent / f"noether_paper35_zh_translation_{revision}_20260804"
        manifest = sibling / "SHA256SUMS.txt"
        ok, detail = replay_manifest(sibling, manifest, expected_entries=entries, compare_actual=True)
        ok = ok and sha(manifest) == digest
        check(ok, f"V{revision}_SIBLING_REPLAY", f"manifest_sha256={sha(manifest)}; {detail}", checks)

    selected_root = ROOT / "controls/checker_return_v002/selected_members"
    selected_manifest = ROOT / "controls/checker_return_v002/sealed_return/SHA256SUMS.txt"
    ok, detail = replay_manifest(
        selected_root,
        selected_manifest,
        expected_entries=39,
        compare_actual=True,
        excluded_relative_paths=set(),
    )
    check(ok, "CHECKER_SELECTED_IMPORT_REPLAY", detail, checks)


def verify_targets(checks: list[dict[str, object]]) -> None:
    parts = [
        ROOT / "translation/corrected_segments_v002/P35_A_zh-Hans-CN_v002.tex",
        ROOT / "translation/corrected_segments_v002/P35_B_zh-Hans-CN_v002.tex",
        ROOT / "translation/corrected_segments_v002/P35_C_zh-Hans-CN_v002.tex",
    ]
    body = b"".join(path.read_bytes() for path in parts)
    hans = (ROOT / "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex").read_bytes()
    ok = (
        len(body) == 29808
        and hashlib.sha256(body).hexdigest().upper() == "54061274DFDE806F491EE424277886ED4C4CEEF3F7E0315DFD1039AACF69F18A"
        and hans.count(body) == 1
    )
    check(ok, "HANS_BODY_IDENTITY", f"bytes={len(body)}; sha256={hashlib.sha256(body).hexdigest().upper()}; occurrences={hans.count(body)}", checks)

    v2 = ROOT.parent / "noether_paper35_zh_translation_002_20260804"
    unchanged = []
    for relative in (
        "translation/corrected_segments_v002/P35_A_zh-Hans-CN_v002.tex",
        "translation/corrected_segments_v002/P35_B_zh-Hans-CN_v002.tex",
        "translation/corrected_segments_v002/P35_C_zh-Hans-CN_v002.tex",
        "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.tex",
        "build/zh-Hans-CN-v002/Noether_Paper35_Chinese_CurrentAuthority_zh-Hans-CN_v002.pdf",
    ):
        unchanged.append(rel_path(ROOT, relative).read_bytes() == rel_path(v2, relative).read_bytes())
    check(all(unchanged), "ACCEPTED_HANS_V002_UNCHANGED", f"members={len(unchanged)}; all_equal={all(unchanged)}", checks)

    producer = ROOT / "build/zh-Hant-controlled-v003/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_v003.tex"
    candidate = ROOT / "controls/checker_return_v002/selected_members/candidate/zh-Hant-controlled/Noether_Paper35_Chinese_CurrentAuthority_zh-Hant-controlled_checker_candidate_v003.tex"
    check(
        producer.read_bytes() == candidate.read_bytes(),
        "HANT_V003_CANDIDATE_EQUALITY",
        f"producer={producer.stat().st_size}/{sha(producer)}; candidate={candidate.stat().st_size}/{sha(candidate)}; equal={producer.read_bytes() == candidate.read_bytes()}",
        checks,
    )


def verify_records(checks: list[dict[str, object]]) -> None:
    transport = json.loads((ROOT / "controls/OPENCC_PRODUCER_RECORD_v003.json").read_text(encoding="utf-8"))
    scanner = transport["scanner"]
    boundary = transport["epistemic_boundary"]
    transport_ok = (
        transport["finding_applied"] == "ZHCHK-P35-F015"
        and transport["exact_checker_candidate_equality"] is True
        and scanner["math_span_count_hans"] == scanner["math_span_count_hant"] == 487
        and scanner["math_stream_equal"] is True
        and scanner["tex_control_count_hans"] == scanner["tex_control_count_hant"] == 790
        and scanner["tex_control_stream_equal"] is True
        and scanner["legacy_false_display_span_count"] == 0
        and all(value is False for value in boundary.values())
    )
    check(transport_ok, "HANT_TRANSPORT_RECORD_FIELDS", f"scanner={scanner}; boundary={boundary}", checks)

    build = json.loads((ROOT / "controls/HANT_MECHANICAL_BUILD_RECORD_v003.json").read_text(encoding="utf-8"))
    pass_ok = all(
        item["exit_code"] == 0
        and item["pages_reported_by_log"] == 6
        and item["warning_counts"]["font_warning_lines"] == 2
        and item["warning_counts"]["underfull_hbox_lines"] == 1
        and item["warning_counts"]["overfull_hbox_lines"] == 0
        and item["warning_counts"]["overfull_vbox_lines"] == 0
        and item["warning_counts"]["error_pattern_matches"] == 0
        for item in build["passes"]
    )
    build_ok = (
        build["finding_applied"] == "ZHCHK-P35-F015"
        and build["requested_passes"] == build["successful_passes"] == 2
        and pass_ok
        and build["final_pdf"]["pages_reported_by_log"] == 6
        and build["final_pdf"]["opened_or_rendered_by_producer"] is False
        and build["epistemic_boundary"]["visual_check_performed"] is False
        and build["epistemic_boundary"]["source_check_performed"] is False
    )
    check(build_ok, "HANT_BUILD_RECORD_FIELDS", f"passes={len(build['passes'])}; pass_ok={pass_ok}; final_pdf={build['final_pdf']}", checks)

    pointer = json.loads((ROOT / "controls/P35_CANON_CONTROL_UPDATE_V005_20260804.json").read_text(encoding="utf-8"))
    pointer_ok = (
        pointer["pointer"]["pointer_id"] == "NOETH-DE-AUTH-v005-20260804"
        and pointer["pointer"]["sha256"] == "42E6844BFCBFB2133E9AA323A823604351CF9C49550AFCF34ECAAF7887185660"
        and pointer["metadata_delta"]["p35_content_delta"] is False
        and pointer["metadata_delta"]["chinese_language_evidence"] is False
        and pointer["p35_binder"]["remains_valid"] is True
        and pointer["p35_binder"]["reopened"] is False
    )
    check(pointer_ok, "POINTER_V005_METADATA_ONLY", f"pointer={pointer['pointer']['pointer_id']}; delta={pointer['metadata_delta']}; p35={pointer['p35_binder']}", checks)

    checker_verifier = json.loads((ROOT / "controls/checker_return_v002/sealed_return/P35_V002_RETURN_VERIFICATION.json").read_text(encoding="utf-8"))
    check(checker_verifier.get("all_pass") is True, "SEALED_CHECKER_VERIFIER_STATE", f"all_pass={checker_verifier.get('all_pass')}", checks)


def verify_no_producer_render(checks: list[dict[str, object]]) -> None:
    raster_suffixes = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp"}
    disallowed = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in raster_suffixes:
            continue
        relative = path.relative_to(ROOT).as_posix()
        if not relative.startswith("controls/checker_return_001/") and not relative.startswith("controls/checker_return_v002/"):
            disallowed.append(relative)
    check(not disallowed, "NO_PRODUCER_RENDER_ARTIFACTS", f"disallowed={disallowed}", checks)


def verify_root_manifest(checks: list[dict[str, object]]) -> None:
    manifest = ROOT / "SHA256SUMS.txt"
    entries = parse_manifest(manifest)
    ok, detail = replay_manifest(ROOT, manifest, expected_entries=len(entries), compare_actual=True)
    check(ok, "ROOT_MANIFEST", detail, checks)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-manifest", action="store_true")
    parser.add_argument("--stdout-only", action="store_true")
    args = parser.parse_args()

    checks: list[dict[str, object]] = []
    verify_expected_identities(checks)
    verify_syntax(checks)
    verify_graph(checks)
    verify_lineage(checks)
    verify_targets(checks)
    verify_records(checks)
    verify_no_producer_render(checks)
    if args.check_manifest:
        verify_root_manifest(checks)

    report = {
        "schema_version": "1.0.0",
        "record_type": "producer_mechanical_package_verification",
        "recorded_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "work_id": "NOETHER-P35-ZH",
        "revision": "v003",
        "decision_id": "ZH-D137",
        "checker_return_id": "ZHCHK-NOETHER-P35-V002-RETURN-001",
        "checks": checks,
        "check_count": len(checks),
        "all_pass": all(item["pass"] for item in checks),
        "manifest_checked": args.check_manifest,
        "producer_render_or_visual_check": False,
        "claim_limit": "Mechanical syntax, custody, hash, exact-byte, build-record, graph, and optional manifest checks only; no substantive or visual validation.",
    }
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if not args.stdout_only:
        REPORT.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")
    return 0 if report["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
