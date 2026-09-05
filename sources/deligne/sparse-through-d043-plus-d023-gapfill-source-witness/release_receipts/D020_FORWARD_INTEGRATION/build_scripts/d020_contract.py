"""Read-only contracts and pure planning for the bounded D020 successor.

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
INPUT_SHA256 = "86B0AC5C7DE90157A346C1EE32B1900343CFC8FB9AA0B50D1D5F21E75378A988"
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
    require(result["schema"] == "d020-next-integration-inputs-v1" and result["work_id"] == "D020", "input schema/work mismatch")
    require(Path(result["write_boundary"]).resolve() == TASK, "manifest write boundary differs from child")
    require(result["d020"]["source_language"] == "French" and result["d020"]["translation_language"] == "English", "source/translation roles reversed")
    require(result["publication_context"]["figshare"] == "EXCLUDED", "Figshare exclusion missing")
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
    require("D020" not in old_works and "D020_PUBLIC_SAFE" not in text, "D020 already inserted")
    for old, new in cfg["insertion"]["coverage_replacements"][lang]:
        require(text.count(old) == 1, "coverage replacement anchor mismatch")
        text = text.replace(old, new, 1)
    lines = text.splitlines()
    anchor = [i for i, line in enumerate(lines) if "d021}" in line]
    require(len(anchor) == 1 and anchor[0] > 0 and "d019}" in lines[anchor[0] - 1], "D019/D021 insertion adjacency")
    lines.insert(anchor[0], cfg["insertion"]["master_insertions"][lang])
    result = "\n".join(lines) + "\n"
    new_names, new_works = include_names(result)
    require(set(new_works) - set(old_works) == {"D020"}, "unexpected work inventory delta")
    index = new_works.index("D020")
    require(new_works[index-1:index+2] == ["D019", "D020", "D021"], "wrong insertion order")
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
    d020 = cfg["d020"]
    audit = read_json(d020["final_audit"]["path"])
    require(audit["terminal_status"] == "PASS_PAPER_COMPLETE", "D020 final audit did not establish PAPER_COMPLETE")
    require(audit["paper_complete_established"] is True and audit["publication_ready"] is True, "D020 is not publication ready")
    require(audit["candidate_public_surface_status"] == "PASS", "D020 public-surface audit failed")
    require(audit["constraints"]["candidate_modified"] is False and audit["constraints"]["tex_launched"] is False, "D020 cold-audit mode differs")
    subject = read_json(d020["subject_manifest"]["path"])
    require(subject["schema"] == "d020-immutable-cold-subject-v4" and len(subject["files"]) == 328, "D020 subject manifest differs")
    require(sum(int(row["bytes"]) for row in subject["files"]) == 106_554_318, "D020 subject byte total differs")
    require(audit["immutable_inputs"]["v6_subject"]["expected_members"] == 328, "audit/subject member binding differs")
    require(audit["immutable_inputs"]["v6_subject"]["manifest"]["sha256"] == d020["subject_manifest"]["sha256"], "audit/subject manifest hash binding differs")
    require(audit["immutable_inputs"]["authority"]["sha256"] == d020["authority"]["sha256"], "audit/authority binding differs")
    return subject


def evidence_closure(cfg):
    """Small exact final-audit closure; the full cold tree is copied separately."""
    rows = []
    for item in cfg["d020"]["selected_audit"]:
        rows.append({**item, "relative_path": item["relative"], "role": "D020_FRESH_COLD_AUDIT"})
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
    subject = validate_gate(cfg)
    evidence = evidence_closure(cfg)
    pred = Path(cfg["predecessor"]["root"])
    receipt = read_json(cfg["predecessor"]["receipt"]["path"])
    require(receipt["status"] == "PASS", "predecessor build receipt contract")
    for row in cfg["predecessor"]["release_files"]:
        bound = next(x for x in receipt["files"] if x["name"] == Path(row["path"]).name)
        require(bound["sha256"].casefold() == row["sha256"].casefold() and int(bound["bytes"]) == int(row["bytes"]), "predecessor release identity binding")
    rows = replay_source(pred / "source_tree", cfg["predecessor"]["source_manifest"]["path"])
    require(len(rows) == cfg["predecessor"]["source_manifest_members"], "predecessor manifest member count")
    work_root = Path(cfg["d020"]["work_root"])
    for item in subject["files"]:
        check(confined(work_root, item["path"]), item)
    language_checks = {}
    for lang in LANGUAGES:
        original = pred / "source_tree" / f"Deligne_{lang}.tex"
        release = pred / "release" / original.name
        require(original.read_bytes() == release.read_bytes(), "source/release master mismatch")
        draft = patch_master(original.read_text(encoding="utf-8"), lang, cfg)
        with fitz.open(cfg["d020"]["canonical_readers"][lang]["path"]) as doc:
            require(len(doc) == 35, "D020 canonical reader count")
        parts = measure_parts(pred / "source_tree", lang, pred / "release" / f"Deligne_{lang}.pdf")
        require(parts[-1]["last"] == cfg["predecessor"]["pages"][lang], "predecessor topology total")
        language_checks[lang] = {"source_role": "English translation" if lang == "EN" else "original French", "inserted_body_pages": 35, "predecessor_body_pages": sum(x["pages"] for x in parts), "predecessor_frontmatter_pages": parts[0]["first"]-1, "draft_master": identity_bytes(draft.encode("utf-8"))}
    with fitz.open(cfg["d020"]["canonical_readers"]["APPARATUS"]["path"]) as doc:
        require(len(doc) == 36, "apparatus count")
    check(INPUT, {"sha256": INPUT_SHA256})
    return {"schema": "d020-builder-preflight-v1", "status": "PASS", "manifest": identity(INPUT), "absolute_input_identities": len(checked), "selected_cold_audit_members_replayed": len(evidence), "d020_subject_members_replayed": len(subject["files"]), "predecessor_source_manifest_members_replayed": len(rows), "languages": language_checks, "publication_identity": "UNVERIFIED_TARGET_ONLY", "tex_launches": 0, "pdf_or_archive_generation": False, "network_operations": 0, "source_writes": False}
