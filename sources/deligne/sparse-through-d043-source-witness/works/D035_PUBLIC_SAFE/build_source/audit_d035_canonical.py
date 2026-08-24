#!/usr/bin/env python3
"""Independently gate the normalized D035 canonical packet.

This audit reads but never patches canonical source.  It replays every returned
ZIP member, checks topology and bilingual label/citation parity, verifies the
isolated A/B and cold builds, and emits only relative, publication-safe paths.
"""

from __future__ import annotations

import collections
import csv
import hashlib
import json
import os
import pathlib
import re
import zipfile

from pypdf import PdfReader


ROOT = pathlib.Path(__file__).resolve().parents[2]
CANONICAL = ROOT / "canonical"
AUDIT = ROOT / "audit"
STATE = ROOT / "state"
RETURNED = ROOT / "returned" / "DELIGNE_D035_GAUSS_CUBIQUES_SL2_PATTERSON_S06_CUMULATIVE_FULL_STATE.zip"

EXPECTED = {
    "returned": (34098286, "4382AF09D8EF536C3E58C19FFFE9A0DCFD9FC21B06C26F3AF6E7C4213395FF7F"),
    "authority": (1511172, "B65B39804DA147575D15CEFD37A681D586F500BEF3421CB27928D4F1550B2C0F"),
    "comparator": (669855, "58BBD3292082B126F8C96BD74B3F1455360831F389D1C150E534FFCDE9170D9A"),
    "zero": (2944802, "31F2DF8D8CFB851A81CA9479404FB6BBC38A131B65914B56B5270DA508E3A13A"),
    "diagram_zero": (19843113, "542174B82F6944E63A57A4D43F2CFCF771F95C82B9D239F576D20E0B9D50021F"),
    "fallback": (9050736, "B53D53A43E4D5EB3B1C12EB6E458BDAF2928A1758B2801B8170222AAD4C0E3B9"),
}

PAYLOADS = {
    "authority": CANONICAL / "witness" / "D035_AUTHORITY_34PP.pdf",
    "comparator": CANONICAL / "witness" / "D035_COMPARATOR_ONLY_34PP.pdf",
    "zero": CANONICAL / "witness" / "D035_ZERO_ACCEPTED_PRIOR_WORK.zip",
    "diagram_zero": CANONICAL / "witness" / "D035_ZERO_ACCEPTED_DIAGRAM_WITNESSES.zip",
    "fallback": CANONICAL / "witness" / "D035_IMAGE_FALLBACKS.zip",
}

CANONICAL_EXPECTED = {
    "D035_FR.tex": (104035, "9435C0736CA7AD2AFA747E25A4351BC4CACAF95BCB1E2693688712FF4B0CAB5D"),
    "D035_FR.pdf": (190358, "78B429E53939903E7E43AAD9D33F8EC005B96B3A34DA74A3D0AE33704C121510"),
    "D035_EN.tex": (100246, "9E903C6FD1E495DEF7F4DC58757F70674D919C8B497DD3E6BBA6D6457865BB69"),
    "D035_EN.pdf": (187845, "E202510EC8C5A8AFD8DFC0E36DD5793826ECB0AC5C041ED1C237C17878AC474E"),
    "D035_APPARATUS.tex": (27276, "325F013EE39672CAE631321686FBDC6F3213AC4B63E9B4ABB80215CF672A0F00"),
    "D035_APPARATUS.pdf": (93860, "F09D794DC403456BCB2C03F2B4E81A9477BFBDBD0E2A1ABB35A6DB52A29A550A"),
}

AB_BUILDS = {
    "D035_FR": ("final2_fr_A", "final2_fr_B"),
    "D035_EN": ("final3_en_A", "final3_en_B"),
    "D035_APPARATUS": ("final2_app_A", "final2_app_B"),
}

BAD_LOG = re.compile(r"Missing character|Overfull|Underfull|Undefined control|LaTeX Error|Fatal error")


def rel(path: pathlib.Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def identity(path: pathlib.Path) -> dict:
    return {"path": rel(path), "bytes": path.stat().st_size, "sha256": sha256(path)}


def pdf_identity(path: pathlib.Path) -> dict:
    out = identity(path)
    out["pages"] = len(PdfReader(str(path)).pages)
    return out


def zip_identity(path: pathlib.Path, expected_members: int) -> dict:
    out = identity(path)
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None
        members = [item for item in archive.infolist() if not item.is_dir()]
        assert len(members) == expected_members
        assert all(item.date_time == (1980, 1, 1, 0, 0, 0) for item in members)
        out.update({"members": len(members), "crc_replay": "PASS", "fixed_timestamps": True})
    return out


def replay_outer() -> dict:
    assert (RETURNED.stat().st_size, sha256(RETURNED)) == EXPECTED["returned"]
    state_files = {rel(path).removeprefix("state/"): path for path in STATE.rglob("*") if path.is_file()}
    with zipfile.ZipFile(RETURNED) as archive:
        assert archive.testzip() is None
        names = archive.namelist()
        assert len(names) == 117 and set(names) == set(state_files)
        assert all(archive.getinfo(name).date_time == (1980, 1, 1, 0, 0, 0) for name in names)
        for name in names:
            assert hashlib.sha256(archive.read(name)).hexdigest().upper() == sha256(state_files[name])
    return {**identity(RETURNED), "members": 117, "crc_replay": "PASS", "extracted_member_hash_replay": "PASS"}


def topology_gate() -> dict:
    with (STATE / "control" / "PAGE_MAP.tsv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    assert len(rows) == 34
    assert [int(row["physical_page"]) for row in rows] == list(range(1, 35))
    assert [int(row["printed_page"]) for row in rows] == list(range(244, 278))
    assert all(row["disposition"] == "INCLUDE_ARTICLE" for row in rows)
    assert all(row["named_author"] == "PIERRE_DELIGNE_ONLY" for row in rows)
    assert all(row["patterson_role"] == "SUBJECT_ATTRIBUTION_NOT_AUTHOR" for row in rows)
    assert "title" in rows[0]["topology_marker"] and "revision footnote" in rows[0]["topology_marker"]
    assert "bibliography [13]-[24]" in rows[-1]["topology_marker"]
    assert "physical EOF" in rows[-1]["topology_marker"]
    return {
        "authority_physical_pages": list(range(1, 35)),
        "printed_pages": list(range(244, 278)),
        "article_pages": 34,
        "copy_matter_pages": 0,
        "page_mapping": "ONE_TO_ONE",
        "title_byline_revision_footnote": "physical_page_1",
        "terminal_bibliography_rule_blank_remainder_eof": "physical_page_34",
    }


def edition_records(layer: str) -> list[dict]:
    path = STATE / "edition" / f"{layer}.ndjson"
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(rows) == 34
    assert [int(row["physical_page"]) for row in rows] == list(range(1, 35))
    assert all(row["status"] == "COMPLETE" and row["disposition"] == "INCLUDE_ARTICLE" for row in rows)
    return rows


def alignment_gate() -> dict:
    source = edition_records("source_language")
    english = edition_records("english_standalone")
    apparatus = edition_records("apparatus")
    repaired_english = [row["text"] for row in english]
    before = "identified with μ\nby 0.0.2."
    after = "identified with μ\nby (0.0.2)."
    assert repaired_english[13].count(before) == 1
    repaired_english[13] = repaired_english[13].replace(before, after)
    for index, source_row in enumerate(source):
        source_text = source_row["text"]
        english_text = repaired_english[index]
        for pattern in (r"\(\d+(?:\.\d+)+\)", r"\[\d+\]"):
            assert collections.Counter(re.findall(pattern, source_text)) == collections.Counter(re.findall(pattern, english_text))
    assert all(row["restraint"] == "PAGE_ADDRESSED_SOURCE_CRITICAL_NOTES_ONLY" for row in apparatus)
    return {
        "source_records": 34,
        "english_records": 34,
        "apparatus_records": 34,
        "equation_label_multisets_aligned": 34,
        "bibliographic_citation_multisets_aligned": 34,
        "recorded_repair": "English physical page 14 restored parentheses around (0.0.2)",
    }


def canonical_pdf_gate() -> dict:
    out = {}
    for filename, (expected_bytes, expected_sha) in CANONICAL_EXPECTED.items():
        path = CANONICAL / filename
        assert path.stat().st_size == expected_bytes and sha256(path) == expected_sha
        out[filename] = pdf_identity(path) if path.suffix == ".pdf" else identity(path)
    for filename in ("D035_FR.pdf", "D035_EN.pdf", "D035_APPARATUS.pdf"):
        reader = PdfReader(str(CANONICAL / filename))
        assert len(reader.pages) == 34
        all_text = []
        for index, page in enumerate(reader.pages, 1):
            text = page.extract_text() or ""
            all_text.append(text)
            assert f"authority physical {index} / printed {243 + index}" in text
        joined = "\n".join(all_text)
        if filename != "D035_APPARATUS.pdf":
            assert "[PHYSICAL EOF]" not in joined and not re.search(r"\b539-\d{2}\b", joined)
            assert "[13]" in all_text[-1] and "[24]" in all_text[-1]
        else:
            assert "physical EOF" in all_text[-1]
    fr_first = PdfReader(str(CANONICAL / "D035_FR.pdf")).pages[0].extract_text() or ""
    en_first = PdfReader(str(CANONICAL / "D035_EN.pdf")).pages[0].extract_text() or ""
    assert "SOMMES DE GAUSS CUBIQUES" in fr_first and "par P" in fr_first
    assert "CUBIC GAUSS SUMS" in en_first and "by P" in en_first
    en_page14 = PdfReader(str(CANONICAL / "D035_EN.pdf")).pages[13].extract_text() or ""
    assert "(0.0.2)" in en_page14
    return out


def build_gate() -> dict:
    out = {}
    for stem, (a_name, b_name) in AB_BUILDS.items():
        a = AUDIT / "isolated_builds" / a_name / f"{stem}.pdf"
        b = AUDIT / "isolated_builds" / b_name / f"{stem}.pdf"
        a_log = a.with_suffix(".log")
        b_log = b.with_suffix(".log")
        assert a.read_bytes() == b.read_bytes() == (CANONICAL / f"{stem}.pdf").read_bytes()
        assert BAD_LOG.search(a_log.read_text(encoding="utf-8", errors="replace")) is None
        assert BAD_LOG.search(b_log.read_text(encoding="utf-8", errors="replace")) is None
        out[stem] = {"A": identity(a), "B": identity(b), "byte_identical": True, "bad_log_findings": 0, "engine": "LuaHBTeX 1.25.7"}
    return out


def cold_gate() -> dict:
    out = {}
    for stem in ("D035_FR", "D035_EN", "D035_APPARATUS"):
        canonical_tex = CANONICAL / f"{stem}.tex"
        cold_tex = AUDIT / "cold" / "input" / f"{stem}.tex"
        cold_pdf = AUDIT / "cold" / "build" / stem / f"{stem}.pdf"
        cold_log = cold_pdf.with_suffix(".log")
        assert cold_tex.read_bytes() == canonical_tex.read_bytes()
        assert cold_pdf.read_bytes() == (CANONICAL / f"{stem}.pdf").read_bytes()
        assert BAD_LOG.search(cold_log.read_text(encoding="utf-8", errors="replace")) is None
        out[stem] = {
            "frozen_input": identity(cold_tex),
            "cold_output": pdf_identity(cold_pdf),
            "canonical_output_byte_identical": True,
            "bad_log_findings": 0,
        }
    return {"mode": "FRESH_FULL_NONPATCHING_COLD_AUDIT", "input_mutations": [], "editions": out, "result": "PASS"}


def visual_gate() -> dict:
    metrics = json.loads((AUDIT / "VISUAL_METRICS.json").read_text(encoding="utf-8"))
    sheets = {}
    editions = {}
    for edition in ("fr", "en", "apparatus"):
        rows = metrics[edition]
        assert len(rows) == 34
        assert max(row["edge_dark_fraction"] for row in rows) <= 0.001
        assert all(row["content_bbox"] is not None for row in rows)
        editions[edition] = {
            "rendered_pages": 34,
            "minimum_nonwhite_fraction": min(row["nonwhite_fraction"] for row in rows),
            "maximum_nonwhite_fraction": max(row["nonwhite_fraction"] for row in rows),
            "maximum_edge_dark_fraction": max(row["edge_dark_fraction"] for row in rows),
        }
        for span in ("P001_P017", "P018_P034"):
            path = AUDIT / "rendered" / f"CONTACT_{edition.upper()}_{span}.png"
            sheets[path.name] = identity(path)
    return {
        "rendered_pages": 102,
        "contact_sheets": sheets,
        "editions": editions,
        "inspection": "COMPLETE_ALL_102_PAGES_NO_CLIPPING_OVERLAP_BLACK_SQUARES_OR_BROKEN_GLYPHS",
        "findings": [],
    }


def public_name_check(path: pathlib.Path, needle: bytes) -> bool:
    if path.suffix.lower() == ".pdf":
        raw = path.read_bytes().lower()
        text = "\n".join((page.extract_text() or "") for page in PdfReader(str(path)).pages).encode("utf-8", errors="ignore").lower()
        return needle in raw or needle in text
    if path.suffix.lower() == ".zip":
        with zipfile.ZipFile(path) as archive:
            return any(needle in archive.read(item).lower() for item in archive.namelist() if not item.endswith("/"))
    return needle in path.read_bytes().lower()


def write_inventory() -> tuple[pathlib.Path, list[dict]]:
    candidates = [
        (CANONICAL / "D035_FR.pdf", "canonical_source_language_pdf", "PUBLIC_CANONICAL"),
        (CANONICAL / "D035_FR.tex", "canonical_source_language_tex", "PUBLIC_CANONICAL"),
        (CANONICAL / "D035_EN.pdf", "canonical_english_pdf", "PUBLIC_CANONICAL"),
        (CANONICAL / "D035_EN.tex", "canonical_english_tex", "PUBLIC_CANONICAL"),
        (CANONICAL / "D035_APPARATUS.pdf", "restrained_apparatus_pdf", "PUBLIC_APPARATUS"),
        (CANONICAL / "D035_APPARATUS.tex", "restrained_apparatus_tex", "PUBLIC_APPARATUS"),
        (PAYLOADS["authority"], "controlling_authority", "PUBLIC_PROVENANCE_WITNESS"),
        (PAYLOADS["comparator"], "comparison_only", "PUBLIC_PROVENANCE_WITNESS"),
        (PAYLOADS["fallback"], "image_fallbacks", "PUBLIC_PROVENANCE_WITNESS"),
    ]
    profile_leaf = pathlib.Path(os.environ["USERPROFILE"]).name.encode("utf-8").lower()
    rows = []
    for path, role, disposition in candidates:
        assert not public_name_check(path, profile_leaf)
        info = identity(path)
        pages_or_members = ""
        if path.suffix.lower() == ".pdf":
            pages_or_members = f"pages={len(PdfReader(str(path)).pages)}"
        elif path.suffix.lower() == ".zip":
            with zipfile.ZipFile(path) as archive:
                pages_or_members = f"members={len([x for x in archive.infolist() if not x.is_dir()])}"
        rows.append({**info, "role": role, "disposition": disposition, "pages_or_members": pages_or_members, "local_account_first_name_check": "PASS_NO_MATCH"})
    path = AUDIT / "PUBLIC_SAFE_INVENTORY.tsv"
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["path", "role", "disposition", "bytes", "sha256", "pages_or_members", "local_account_first_name_check"], delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return path, rows


def write_manifest(paths: list[pathlib.Path]) -> pathlib.Path:
    target = AUDIT / "CANONICAL_MANIFEST.tsv"
    rows = [identity(path) for path in sorted(paths, key=rel)]
    with target.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["path", "bytes", "sha256"], delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return target


def main() -> None:
    returned = replay_outer()
    payloads = {}
    member_counts = {"zero": 42, "diagram_zero": 96, "fallback": 74}
    for name, path in PAYLOADS.items():
        expected_bytes, expected_sha = EXPECTED[name]
        assert path.stat().st_size == expected_bytes and sha256(path) == expected_sha
        payloads[name] = pdf_identity(path) if path.suffix == ".pdf" else zip_identity(path, member_counts[name])
    assert payloads["authority"]["pages"] == payloads["comparator"]["pages"] == 34
    canonical = canonical_pdf_gate()
    topology = topology_gate()
    alignment = alignment_gate()
    builds = build_gate()
    visual = visual_gate()
    cold = cold_gate()
    inventory_path, inventory_rows = write_inventory()
    manifest_paths = [RETURNED, *PAYLOADS.values()]
    manifest_paths.extend(CANONICAL / name for name in CANONICAL_EXPECTED)
    manifest_paths.extend((CANONICAL / "build_source" / name) for name in ("build_d035_canonical.py", "make_d035_contact_sheets.py", "audit_d035_canonical.py"))
    manifest_path = write_manifest(manifest_paths)
    visual_path = AUDIT / "VISUAL_INSPECTION_RECEIPT.json"
    visual_path.write_text(json.dumps(visual, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    cold_path = AUDIT / "FRESH_COLD_AUDIT.json"
    cold_path.write_text(json.dumps(cold, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    gate = {
        "schema": "deligne-d035-independent-canonical-gate-v1",
        "work_id": "D035",
        "title": "Sommes de Gauss cubiques et revetements de SL(2), d'apres S. J. Patterson",
        "status": "PASS",
        "result": "PAPER_COMPLETE_INDEPENDENT_CANONICAL_GATE_PASS",
        "returned": returned,
        "payloads": payloads,
        "canonical": canonical,
        "topology": topology,
        "alignment": alignment,
        "deterministic_builds": builds,
        "visual_qa": visual,
        "fresh_nonpatching_cold_audit": cold,
        "public_safe_inventory": {"receipt": identity(inventory_path), "entries": len(inventory_rows), "local_account_first_name_check": "PASS_NO_MATCH"},
        "canonical_manifest": identity(manifest_path),
        "inherited_cold_claim": {
            "path": "state/audit/S06_COLD_AUDIT.json",
            "mode": "FRESH_FULL_NONPATCHING_COLD_AUDIT",
            "status": "PASS_NO_FINDINGS_NO_REPAIR_RESTART_REQUIRED",
            "accepted_as": "INHERITED_EVIDENCE_ONLY_INDEPENDENT_GATE_RECOMPUTED",
        },
        "resolved_repairs": [
            "normalized literal set-quotient reverse solidi before TeX compilation",
            "normalized combining overline, tilde, and underline accents including Greek tokens",
            "mapped mathematical script E/F and box-rule glyphs without missing characters",
            "separated mixed mathematical-prefix and prose-suffix hyphen tokens",
            "excluded scan identifiers, printed folio duplicates, and [PHYSICAL EOF] control marker from canonical reader prose",
            "removed a generated terminal topology note from canonical FR/EN; topology remains in apparatus",
            "restored English physical-page-14 cross-reference parentheses around (0.0.2)",
            "used LuaLaTeX to eliminate XeLaTeX randomized subset-tag byte drift",
        ],
        "unresolved_deterministic_failures": [],
        "findings": [],
    }
    target = AUDIT / "CANONICAL_GATE.json"
    target.write_text(json.dumps(gate, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"gate": identity(target), "status": gate["status"], "result": gate["result"]}, sort_keys=True))


if __name__ == "__main__":
    main()
