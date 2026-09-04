"""Read-only contracts and pure planning for the bounded D033 successor.

No subprocess, write, archive creation or network operation is performed here.
The input manifest is a frozen local locator, not a public-release receipt.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import stat
import zipfile
from pathlib import Path, PurePosixPath

TASK = Path(__file__).resolve().parents[1]
INPUT = TASK / "NEXT_INTEGRATION_INPUTS.json"
INPUT_SHA256 = "B75612ABE7BBEF0FD82CC12CF4A56D5D6B79574055FCA0A42A037E99A41B53F7"
MUTABLE = frozenset({"Deligne_EN.tex", "Deligne_FR.tex", "Deligne_EN.pdf", "Deligne_FR.pdf", "README.md", "PUBLIC_SOURCE_MANIFEST.tsv"})
LANGUAGES = ("EN", "FR")
SOURCE_MANIFEST_NAME = "PUBLIC_SOURCE_MANIFEST.tsv"


class Failure(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise Failure(message)


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def safe_relative(name):
    require(isinstance(name, str) and bool(name), "empty relative path")
    require("\\" not in name and ":" not in name and "\x00" not in name, "nonportable relative path")
    path = PurePosixPath(name)
    require(not path.is_absolute() and all(x not in ("", ".", "..") for x in name.split("/")), "unsafe relative path")
    for part in path.parts:
        require(not re.search(r'[<>"|?*\x00-\x1f]', part) and part == part.rstrip(" ."), "ambiguous Windows path component")
        require(not re.fullmatch(r"CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9]", part.split(".")[0], re.IGNORECASE), "reserved Windows path component")
    return path


def reject_reparse(path):
    path = Path(path).absolute()
    for item in (path, *path.parents):
        if item.exists() or item.is_symlink():
            info = item.lstat()
            require(not stat.S_ISLNK(info.st_mode) and not (getattr(info, "st_file_attributes", 0) & 0x400), "symlink/reparse path forbidden")
    return path


def confined(root, relative):
    root = reject_reparse(root).resolve()
    target = reject_reparse(root.joinpath(*safe_relative(relative).parts)).resolve()
    require(target != root and target.is_relative_to(root), "path escapes intended tree")
    return target


def identity_bytes(data):
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest().upper()}


def identity(path):
    path = reject_reparse(path)
    require(path.is_file(), "not a plain file: " + path.name)
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            size += len(block)
            h.update(block)
    return {"bytes": size, "sha256": h.hexdigest().upper()}


def check(path, expected):
    actual = identity(path)
    require(actual["sha256"] == expected["sha256"] and ("bytes" not in expected or actual["bytes"] == int(expected["bytes"])), "input identity mismatch: " + Path(path).name)
    return actual


def config():
    raw = reject_reparse(INPUT).read_bytes()
    require(identity_bytes(raw)["sha256"] == INPUT_SHA256, "input manifest snapshot hash mismatch")
    result = json.loads(raw)
    require(result["schema"] == "d033-next-integration-inputs-v1" and result["work_id"] == "D033", "input schema/work mismatch")
    require(Path(result["write_boundary"]).resolve() == TASK, "manifest write boundary differs from child")
    require(result["d033"]["source_language"] == "English" and result["d033"]["translation_language"] == "French", "source/translation roles reversed")
    return result


def absolute_identities(value):
    if isinstance(value, dict):
        if {"path", "sha256"} <= value.keys() and Path(value["path"]).is_absolute():
            yield value
        for child in value.values():
            yield from absolute_identities(child)
    elif isinstance(value, list):
        for child in value:
            yield from absolute_identities(child)


def inventory_tree(root):
    root = reject_reparse(root)
    result = []
    for directory, dirs, files in os.walk(root, followlinks=False):
        for name in dirs + files:
            reject_reparse(Path(directory) / name)
        result.extend((Path(directory) / name).relative_to(root).as_posix() for name in files)
    return sorted(result)


def manifest_rows(path):
    with Path(path).open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    names = [str(safe_relative(row["path"])) for row in rows]
    require(len(names) == len(set(names)) == len({x.casefold() for x in names}), "duplicate/case-colliding source paths")
    for row in rows:
        require(re.fullmatch(r"[0-9A-F]{64}", row["sha256"]) and int(row["bytes"]) >= 0, "malformed source identity")
    return rows


def source_manifest_rows(root):
    """Return the canonical non-self-referential source-tree inventory."""
    root = reject_reparse(root)
    rows = []
    for name in inventory_tree(root):
        if name == SOURCE_MANIFEST_NAME:
            continue
        safe_relative(name)
        rows.append({"path": name, **identity(confined(root, name))})
    return rows


def source_manifest_bytes(root):
    """Serialize the D019-compatible path/bytes/SHA-256 TSV with LF endings."""
    lines = ["path\tbytes\tsha256\n"]
    for row in source_manifest_rows(root):
        lines.append(f'{row["path"]}\t{row["bytes"]}\t{row["sha256"]}\n')
    return "".join(lines).encode("utf-8")


def verify_source_manifest(root, manifest=None):
    """Replay a manifest against every file except the manifest itself."""
    root = reject_reparse(root)
    manifest = Path(manifest) if manifest is not None else root / SOURCE_MANIFEST_NAME
    expected = source_manifest_rows(root)
    actual = [
        {"path": row["path"], "bytes": int(row["bytes"]), "sha256": row["sha256"]}
        for row in manifest_rows(manifest)
    ]
    require(actual == expected, "source manifest differs from canonical non-self-referential inventory")
    return actual


def replay_source(root, manifest):
    return verify_source_manifest(root, manifest)


def zip_inventory(archive, expected=None):
    """Read every member to EOF, checking CRC, size, hash and safe names."""
    with zipfile.ZipFile(archive) as z:
        infos = z.infolist()
        names = [i.filename for i in infos]
        require(len(names) == len(set(names)) == len({n.casefold() for n in names}), "duplicate/case-colliding ZIP entries")
        for info in infos:
            safe_relative(info.filename)
            require(not info.is_dir() and not stat.S_ISLNK(info.external_attr >> 16) and not (info.flag_bits & 1), "unsupported ZIP entry")
        if expected is None:
            expected = json.loads(z.read("MANIFEST.json"))
            expected = expected + [{"path": "MANIFEST.json", **identity_bytes(z.read("MANIFEST.json"))}]
        required = {r["path"]: r for r in expected}
        require(len(required) == len(expected) and set(names) == set(required), "ZIP manifest coverage")
        for info in infos:
            h = hashlib.sha256()
            count = 0
            with z.open(info) as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b""):
                    count += len(block)
                    h.update(block)
            row = required[info.filename]
            require(count == info.file_size == int(row["bytes"]) and h.hexdigest().upper() == row["sha256"], "ZIP member mismatch: " + info.filename)
    return {"status": "PASS", "members": len(names)}


INCLUDE_RE = re.compile(r"^\\includepdf\[.*?\]\{([^}]+)\}$", re.MULTILINE)


def include_names(text):
    names = INCLUDE_RE.findall(text)
    for name in names:
        safe_relative(name)
    works = []
    for name in names:
        match = re.search(r"\bD\d{3}(?=[_/.])", name)
        require(match is not None, "unidentified included work")
        works.append(match.group())
    require(works == sorted(set(works)), "nonunique or nonnumerical reader order")
    return names, works


def patch_master(text, lang, cfg):
    require(lang in LANGUAGES, "unsupported language")
    old_names, old_works = include_names(text)
    require("D033" not in old_works and "D033_PUBLIC_SAFE" not in text, "D033 already inserted")
    for replacement in cfg["insertion"]["master_exact_replacements"]:
        require(text.count(replacement["old"]) == replacement["occurrences_per_language"], "coverage replacement anchor mismatch")
        text = text.replace(replacement["old"], replacement["new"], 1)
    if lang == "EN":
        old_contents = r"\begingroup\small\sloppy\hyphenpenalty=10000\exhyphenpenalty=10000\tableofcontents\endgroup"
        compact_contents = r"\begingroup\footnotesize\sloppy\hyphenpenalty=10000\exhyphenpenalty=10000\tableofcontents\endgroup"
        require(text.count(old_contents) == 1, "English contents-size anchor mismatch")
        text = text.replace(old_contents, compact_contents, 1)
    lines = text.splitlines()
    anchor = [i for i, line in enumerate(lines) if "d034}" in line]
    require(len(anchor) == 1 and anchor[0] > 0 and "d031}" in lines[anchor[0] - 1], "D031/D034 insertion adjacency")
    lines.insert(anchor[0], cfg["insertion"]["master_insertions"][lang])
    result = "\n".join(lines) + "\n"
    new_names, new_works = include_names(result)
    require(set(new_works) - set(old_works) == {"D033"}, "unexpected work inventory delta")
    index = new_works.index("D033")
    require(new_works[index-1:index+2] == ["D031", "D033", "D034"], "wrong insertion order")
    require(new_names[index] == cfg["insertion"]["source_reader_mapping"][lang], "canonical language mapping mismatch")
    require([x for x in new_names if x != new_names[index]] == old_names, "predecessor reader path changed")
    require("APPARATUS" not in " ".join(new_names), "apparatus leaked into readers")
    return result


def measure_parts(root, lang, pdf=None, text=None):
    import fitz
    root = Path(root)
    if text is None:
        text = (root / f"Deligne_{lang}.tex").read_text(encoding="utf-8")
    names, works = include_names(text)
    first = None
    if pdf is not None:
        with fitz.open(pdf) as doc:
            marks = [x for x in doc.get_toc() if re.match(r"^D001\b", x[1])]
            require(len(marks) == 1, "D001 bookmark topology")
            first = marks[0][2]
    require(first is not None and first >= 2, "measure actual frontmatter; do not assume page3")
    parts = []
    for name, work in zip(names, works):
        with fitz.open(confined(root, name)) as doc:
            pages = len(doc)
        parts.append({"work": work, "path": name, "first": first, "last": first+pages-1, "pages": pages})
        first += pages
    return parts


def converged(passes, minimum=3):
    """Settled TOC and PDF bytes are both required, within bounded passes."""
    return len(passes) >= minimum and passes[-1]["toc"] == passes[-2]["toc"] and passes[-1]["pdf"] == passes[-2]["pdf"]


def validate_gate(cfg):
    packet = {Path(x["path"]).name: x for x in cfg["d033"]["canonical_files"]}
    gate = read_json(packet["D033_CORPUS_GATE.json"]["path"])
    require(gate["result"] == "PASS" and gate["paper_state"] == "PAPER_COMPLETE", "D033 gate not complete PASS")
    require(gate["source_language"] == "English" and gate["translation"] == "French", "live gate language roles")
    audit_row = next(x for x in cfg["d033"]["required_evidence"] if x["path"].endswith("/D033_FINAL_COLD_AUDIT.json"))
    audit = read_json(audit_row["path"])
    require(audit["status"] == "PASS" and audit["remaining_findings"] == [], "independent final audit not PASS")
    require(gate["independent_cold_audit_original_sha256"] == audit_row["sha256"], "gate/audit hash binding")
    for row in audit["artifacts"]:
        require(row["name"] in packet and row["sha256"] == packet[row["name"]]["sha256"] and row["bytes"] == packet[row["name"]]["bytes"], "independent audit canonical artifact binding")
    return packet


def evidence_closure(cfg):
    """Minimal exact receipt/log/math-snapshot closure, never a broad history scan."""
    gate_root = Path(cfg["d033"]["public_manifest"]["path"]).parents[1]
    rows = []
    for item in cfg["d033"]["required_evidence"]:
        relative = Path(item["path"]).relative_to(gate_root).as_posix()
        rows.append({"relative_path": relative, "path": item["path"], "bytes": item["bytes"], "sha256": item["sha256"], "role": "required_receipt_or_bound_visual"})
    for lane in ("normalized_v1", "reproduction_check"):
        receipt = read_json(confined(gate_root, lane + "/D033_COMPILE_RECEIPT.json"))
        require({x["name"] for x in receipt["artifacts"]} == {"D033_EN", "D033_FR", "D033_APPARATUS"}, "compile receipt artifact set")
        for item in receipt["artifacts"]:
            relative = lane + "/pdf/" + item["name"] + ".log"
            path = confined(gate_root, relative)
            actual = check(path, {"sha256": item["log_sha256"]})
            rows.append({"relative_path": relative, "path": str(path), **actual, "role": "historical_compile_log"})
    historical = read_json(confined(gate_root, "independent_fidelity/D033_MATH_ROUTE_CLOSURE_CBFD11AB_04AB9722.json"))
    require(historical["captured_directory"] == "math_revision_69BA9745_F94E4EE0", "historical math snapshot path mismatch")
    require(set(historical["sha256"]) == {"D033_EN.tex", "D033_FR.tex", "D033_FORMULA_ROUTES.json"}, "historical math snapshot inventory")
    for name, sha256 in historical["sha256"].items():
        relative = "independent_fidelity/" + historical["captured_directory"] + "/" + name
        path = confined(gate_root, relative)
        actual = check(path, {"sha256": sha256})
        rows.append({"relative_path": relative, "path": str(path), **actual, "role": "historical_snapshot_NOT_CANONICAL"})
    for row in rows:
        check(row["path"], row)
    require(len({r["relative_path"].casefold() for r in rows}) == len(rows), "evidence closure collision")
    return rows


def preflight():
    import fitz
    cfg = config()
    checked = list(absolute_identities(cfg))
    for row in checked:
        check(row["path"], row)
    packet = validate_gate(cfg)
    evidence = evidence_closure(cfg)
    pred = Path(cfg["predecessor"]["root"])
    receipt = read_json(cfg["predecessor"]["receipt"]["path"])
    require(receipt["status"] == "PASS" and receipt["concept_doi"] == cfg["publication_context"]["concept_doi"], "predecessor build receipt contract")
    require(receipt["source_manifest"]["sha256"] == cfg["predecessor"]["source_manifest"]["sha256"], "predecessor manifest receipt binding")
    for row in cfg["predecessor"]["release_files"]:
        require(receipt["release_files"][Path(row["path"]).name]["sha256"] == row["sha256"], "predecessor release identity binding")
    rows = replay_source(pred / "source_tree", cfg["predecessor"]["source_manifest"]["path"])
    require(len(rows) == cfg["predecessor"]["inherited_source_manifest_members"], "predecessor manifest member count")
    public_manifest = read_json(cfg["d033"]["public_manifest"]["path"])
    require({r["path"] for r in public_manifest} == set(packet), "public packet manifest coverage")
    for row in public_manifest:
        require({k: row[k] for k in ("bytes", "sha256")} == {k: packet[row["path"]][k] for k in ("bytes", "sha256")}, "public packet manifest binding")
    flat_expected = public_manifest + [{"path": "MANIFEST.json", **identity(cfg["d033"]["public_manifest"]["path"])}]
    flat = zip_inventory(cfg["d033"]["flat_packet"]["path"], flat_expected)
    source = zip_inventory(packet["D033_Source.zip"]["path"])
    language_checks = {}
    for lang in LANGUAGES:
        original = pred / "source_tree" / f"Deligne_{lang}.tex"
        release = pred / "release" / original.name
        require(original.read_bytes() == release.read_bytes(), "source/release master mismatch")
        draft = patch_master(original.read_text(encoding="utf-8"), lang, cfg)
        with fitz.open(packet[f"D033_{lang}.pdf"]["path"]) as doc:
            require(len(doc) == 60, "D033 canonical reader count")
        parts = measure_parts(pred / "source_tree", lang, pred / "release" / f"Deligne_{lang}.pdf")
        require(parts[-1]["last"] == cfg["predecessor"]["pages"][lang], "predecessor topology total")
        language_checks[lang] = {"source_role": "original English" if lang == "EN" else "French translation", "inserted_body_pages": 60, "predecessor_body_pages": sum(x["pages"] for x in parts), "predecessor_frontmatter_pages": parts[0]["first"]-1, "draft_master": identity_bytes(draft.encode("utf-8"))}
    with fitz.open(packet["D033_APPARATUS.pdf"]["path"]) as doc:
        require(len(doc) == 3, "apparatus count")
    check(INPUT, {"sha256": INPUT_SHA256})
    return {"schema": "d033-builder-preflight-v1", "status": "PASS", "manifest": identity(INPUT), "absolute_input_identities": len(checked), "minimal_raw_evidence_closure_members_replayed": len(evidence), "predecessor_source_manifest_members_replayed": len(rows), "flat_packet": flat, "source_packet": source, "languages": language_checks, "publication_identity": "UNVERIFIED_TARGET_ONLY", "tex_launches": 0, "pdf_or_archive_generation": False, "network_operations": 0, "source_writes": False}
