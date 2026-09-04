"""D033-specific local cumulative preparation/build/QA; no publication code.

Only `preflight` and pure offline tests are run during the code-preparation
assignment. `prepare`, `build`, and `qa` are explicit later production stages.
This bounded adapter deliberately contains no archive-generation implementation;
`release-plan` states the final packaging requirements without making archives.
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
from pathlib import Path

import d033_contract as c
from tex_worker import Mutex, MUTEX_NAME, tex_pass, log_anomalies, job_memory_policy

BUILD = c.TASK / "build/cumulative"
SOURCE = BUILD / "source_tree"
AUDIT = BUILD / "audit"
PROVENANCE = BUILD / "provenance_tree"
PRIVATE = BUILD / "private_preservation"
RECEIPTS = SOURCE / "release_receipts/D033_FORWARD_INTEGRATION"


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def output(path):
    path = Path(path)
    c.require(path.is_absolute(), "output must be absolute")
    try:
        relative = path.relative_to(BUILD).as_posix()
    except ValueError as exc:
        raise c.Failure("write outside D033 build child") from exc
    return c.confined(BUILD, relative)


def write_bytes(path, data):
    path = output(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    c.reject_reparse(path.parent)
    path.write_bytes(data)
    c.check(path, c.identity_bytes(data))
    return c.identity(path)


def write_json(path, value):
    return write_bytes(path, (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8"))


def copy_exact(src, dest, expected=None):
    expected = expected or c.identity(src)
    c.check(src, expected)
    dest = output(dest)
    if dest.exists():
        c.check(dest, expected)
    else:
        dest.parent.mkdir(parents=True, exist_ok=True)
        c.reject_reparse(dest.parent)
        shutil.copyfile(src, dest)
        c.check(dest, expected)
    return expected


def refresh_source_manifest():
    """Write and immediately replay the actual source tree, excluding itself."""
    manifest = SOURCE / c.SOURCE_MANIFEST_NAME
    manifest_identity = write_bytes(manifest, c.source_manifest_bytes(SOURCE))
    rows = c.verify_source_manifest(SOURCE, manifest)
    return {"status": "PASS", "members": len(rows), "manifest": manifest_identity}


def private_token():
    token = os.environ.get("USERNAME", "")
    c.require(token and token.isascii() and token.casefold() == c.TASK.parts[2].casefold(), "configured literal privacy token unavailable")
    return token


def public_derivative(data, token):
    """Only literal configured-name replacement; no hash-field rewriting."""
    c.require(token and token.isascii(), "invalid literal privacy token")
    revised, count = re.subn(re.escape(token.encode("ascii")), b"LOCAL_ACCOUNT", data, flags=re.IGNORECASE)
    return revised, count


def patch_readme(text):
    replacements = {
        "D025-D031, D034-D036,": "D025-D031, D033-D036,",
        "D032-D033,": "D032,",
        "This release contains 1040 English and 1053 French pages.": "This release contains 1100 English and 1113 French pages.",
        "under `release_receipts/D019_FORWARD_INTEGRATION/`.": "under `release_receipts/D033_FORWARD_INTEGRATION/`.",
        "## D019 gap insertion\n": "## D019 gap insertion (historical release narrative)\n",
    }
    for old, new in replacements.items():
        c.require(text.count(old) == 1, "README update anchor mismatch")
        text = text.replace(old, new, 1)
    text += "\n## D033 gap insertion\n\nD033 is inserted after D031 and before D034. English is the original source-language edition; French is its translation. Each reader contains 60 pages aligned to printed 227-286. D033 occupies English cumulative pages 892-951 and French cumulative pages 905-964. The three-page apparatus is preserved separately and is not appended to either cumulative reader. Canonical reader PDFs and editable TeX remain exact under `works/D033_PUBLIC_SAFE`; the complete source ZIP remains unchanged. Its archived returned convenience-reader PDFs are not cumulative inputs.\n\nIncluded coverage: D001-D019; D021-D023; D025-D031; D033-D036; D038-D040; D043. Explicit public gaps: D020; D024; D032; D037; D041-D042. These public gaps identify works outside this cumulative release; they are not missing downloads.\n\nThe local orchestrator uses three to five bounded XeLaTeX passes per clean replica and requires settled TOC and PDF hashes, with three independent clean replicas. All passes and immediate log checks share the single machine-wide TeX mutex and captured-process-tree contract stated above. New local raw evidence stays outside public packaging roots; separately hash-mapped literal-name derivatives preserve public provenance without changing historical original-hash claims.\n"
    return text


def prepare():
    cfg = c.config()
    report = c.preflight()
    c.require(not SOURCE.exists() and not PROVENANCE.exists() and not PRIVATE.exists(), "staging already exists: inspect retained cursor; do not restart/duplicate")
    pred = Path(cfg["predecessor"]["root"])
    rows = c.manifest_rows(cfg["predecessor"]["source_manifest"]["path"])
    stage = {"schema": "d033-source-preparation-v1", "status": "RUNNING", "started_utc": now(), "preflight": report, "publication_identity": "UNVERIFIED_TARGET_ONLY"}
    write_json(AUDIT / "SOURCE_PREPARATION_RECEIPT.json", stage)
    try:
        for row in rows:
            copy_exact(c.confined(pred / "source_tree", row["path"]), SOURCE / row["path"], row)
        for item in cfg["d033"]["canonical_files"]:
            copy_exact(item["path"], SOURCE / item["staged_relative_path"], item)
        item = cfg["d033"]["public_manifest"]
        copy_exact(item["path"], SOURCE / "works/D033_PUBLIC_SAFE/MANIFEST.json", item)
        flat = cfg["d033"]["flat_packet"]
        copy_exact(flat["path"], PROVENANCE / "D033/D033_PAPER_COMPLETE_CORPUS_GATE_V1.zip", flat)
        inherited = next(x for x in cfg["predecessor"]["release_files"] if Path(x["path"]).name == "DELIGNE_PROVENANCE_AUDIT_D019_GAPFILL.zip")
        copy_exact(inherited["path"], PROVENANCE / "inherited" / Path(inherited["path"]).name, inherited)
        token = private_token()
        mapping = []
        for item in c.evidence_closure(cfg):
            relative = str(c.safe_relative(item["relative_path"]))
            raw_path = PRIVATE / "D033_raw" / relative
            copy_exact(item["path"], raw_path, item)
            raw = raw_path.read_bytes()
            revised, count = public_derivative(raw, token)
            destination = "works/D033_PUBLIC_SAFE/evidence/" + relative
            public_id = write_bytes(SOURCE / destination, revised)
            write_bytes(PROVENANCE / "D033/evidence" / relative, revised)
            mapping.append({"relative_original_identity": relative, "original_bytes": item["bytes"], "original_sha256": item["sha256"], "public_bytes": public_id["bytes"], "public_sha256": public_id["sha256"], "replacement_count": count, "transform": "EXACT_CASE_INSENSITIVE_LOCAL_ACCOUNT_LITERAL_ONLY_v1", "public_source_destination": destination, "public_provenance_destination": "D033/evidence/" + relative, "role": item["role"], "historical_hash_fields_refer_to": "ORIGINAL_BYTES"})
        privacy = {"schema": "d033-public-evidence-derivative-map-v1", "status": "PASS", "original_bytes_preserved_local_only": True, "canonical_packet_witnesses_gate_unchanged": True, "minimal_closure_not_full_historical_genealogy": True, "files": mapping}
        write_json(SOURCE / "works/D033_PUBLIC_SAFE/D033_PUBLIC_EVIDENCE_MAP.json", privacy)
        write_json(PROVENANCE / "D033/D033_PUBLIC_EVIDENCE_MAP.json", privacy)
        for lang in c.LANGUAGES:
            original = (pred / "source_tree" / f"Deligne_{lang}.tex").read_text(encoding="utf-8")
            write_bytes(SOURCE / f"Deligne_{lang}.tex", c.patch_master(original, lang, cfg).encode("utf-8"))
        write_bytes(SOURCE / "README.md", patch_readme((pred / "source_tree/README.md").read_text(encoding="utf-8")).encode("utf-8"))
        copy_exact(cfg["predecessor"]["receipt"]["path"], RECEIPTS / "D019_PREDECESSOR_BUILD_RELEASE_RECEIPT.json", cfg["predecessor"]["receipt"])
        source_manifest = refresh_source_manifest()
        frozen = [{"path": name, **c.identity(SOURCE / name)} for name in c.inventory_tree(SOURCE) if name not in {"Deligne_EN.pdf", "Deligne_FR.pdf", "README.md", "PUBLIC_SOURCE_MANIFEST.tsv"}]
        stage.update(status="PASS", finished_utc=now(), immutable_stage_files=frozen, mutable_roots=sorted(c.MUTABLE), source_manifest=source_manifest, raw_evidence_local_only_members=len(mapping), canonical_reader_mapping=cfg["insertion"]["source_reader_mapping"], source_inputs_modified=False, next_action="Explicit build stage; no TeX has run.")
        write_json(AUDIT / "SOURCE_PREPARATION_RECEIPT.json", stage)
        return stage
    except Exception as exc:
        stage.update(status="FAIL", failure=str(exc), next_action="Inspect retained partial staging and exact failure; do not launch duplicate production.")
        write_json(AUDIT / "SOURCE_PREPARATION_RECEIPT.json", stage)
        raise


def staged():
    receipt = c.read_json(AUDIT / "SOURCE_PREPARATION_RECEIPT.json")
    c.require(receipt["status"] == "PASS", "source staging incomplete")
    for row in receipt["immutable_stage_files"]:
        c.check(c.confined(SOURCE, row["path"]), row)
    c.verify_source_manifest(SOURCE, SOURCE / c.SOURCE_MANIFEST_NAME)
    return receipt


def regenerate_manifest():
    """Explicit bounded repair for retained staging after a governed file change."""
    receipt = c.read_json(AUDIT / "SOURCE_PREPARATION_RECEIPT.json")
    c.require(receipt["status"] == "PASS", "source staging incomplete")
    for row in receipt["immutable_stage_files"]:
        c.check(c.confined(SOURCE, row["path"]), row)
    return refresh_source_manifest()


def check_tex_logs(process, engine_log):
    process["engine_log_anomalies"] = log_anomalies(engine_log.decode("utf-8", "replace"))
    c.require(process["return_code"] == 0 and not any(process["anomalies"].values()) and not any(process["engine_log_anomalies"].values()), "TeX stdout/full-engine-log anomaly")


def build():
    import fitz
    cfg = c.config()
    staged()
    c.require(not (AUDIT / "COLD_REPRODUCIBILITY_RECEIPT.json").exists(), "build already has a receipt; inspect current state instead of duplicate launch")
    engine = Path(cfg["assembly_reuse"]["runtime"]["engine"])
    engine_id = c.identity(engine)
    memory_policy = job_memory_policy()
    result = {"schema": "d033-cumulative-reproducibility-v1", "status": "RUNNING", "started_utc": now(), "engine": engine_id, "languages": {}, "maximum_passes_per_replica": 5, "minimum_passes_per_replica": 3, "clean_replicas": 3, "tex_process_tree_memory_policy": memory_policy, "maximum_observed_tex_job_memory_bytes": 0}
    write_json(AUDIT / "COLD_REPRODUCIBILITY_RECEIPT.json", result)
    mutex_report = {"name": MUTEX_NAME, "status": "ACQUIRING", "bounded_timeout_ms": 600000, "passes": 0, "tex_process_tree_memory_policy": memory_policy, "maximum_observed_tex_job_memory_bytes": 0}
    write_json(AUDIT / "TEX_MUTEX_RECEIPT.json", mutex_report)
    try:
        with Mutex() as mutex:
            mutex_report.update(status="RUNNING", acquired_utc=now(), abandoned_recovery=mutex.abandoned, wait_ms=mutex.wait_ms)
            write_json(AUDIT / "TEX_MUTEX_RECEIPT.json", mutex_report)
            for lang in c.LANGUAGES:
                names, _ = c.include_names((SOURCE / f"Deligne_{lang}.tex").read_text(encoding="utf-8"))
                replicas = []
                for replica in ("compile_A", "compile_B", "cold_replay"):
                    slot = output(BUILD / "tex_replay" / replica / lang)
                    c.require(not slot.exists(), "existing captured build slot; never duplicate a live/retained attempt")
                    for name in [f"Deligne_{lang}.tex"] + names:
                        copy_exact(SOURCE / name, slot / name)
                    passes = []
                    for pass_number in range(1, 6):
                        process, raw = tex_pass(mutex, engine, slot, f"Deligne_{lang}.tex", cfg["assembly_reuse"]["tex_launch_contract"]["environment"])
                        result["maximum_observed_tex_job_memory_bytes"] = max(result["maximum_observed_tex_job_memory_bytes"], process["peak_job_memory_bytes"])
                        mutex_report["maximum_observed_tex_job_memory_bytes"] = result["maximum_observed_tex_job_memory_bytes"]
                        log = write_bytes(AUDIT / "tex_logs" / f"{replica}_{lang}_{pass_number}.txt", raw)
                        process["stdout"] = log
                        engine_log = c.reject_reparse(slot / f"Deligne_{lang}.log").read_bytes()
                        process["engine_log"] = write_bytes(AUDIT / "tex_logs" / f"{replica}_{lang}_{pass_number}.engine.log", engine_log)
                        check_tex_logs(process, engine_log)
                        passes.append({"pass": pass_number, "process": process, "toc": c.identity(slot / f"Deligne_{lang}.toc"), "pdf": c.identity(slot / f"Deligne_{lang}.pdf")})
                        mutex_report["passes"] += 1
                        write_json(AUDIT / "TEX_MUTEX_RECEIPT.json", mutex_report)
                        settled = c.converged(passes)
                        rerun_warning = re.search(r"Rerun to get cross-references right|Label\(s\) may have changed", (raw + engine_log).decode("utf-8", "replace"), re.IGNORECASE)
                        if settled and not rerun_warning:
                            break
                    else:
                        raise c.Failure("TOC/PDF did not converge within five passes")
                    pdf = slot / f"Deligne_{lang}.pdf"
                    parts = c.measure_parts(SOURCE, lang, pdf)
                    with fitz.open(pdf) as doc:
                        c.require(len(doc) == parts[-1]["last"], "compiled total differs from measured include topology")
                        pages = len(doc)
                    replicas.append({"replica": replica, "pdf": c.identity(pdf), "pages": pages, "frontmatter_pages": parts[0]["first"]-1, "passes": passes, "settled": True})
                c.require(len({x["pdf"]["sha256"] for x in replicas}) == 1, "three clean replica PDF hashes differ")
                selected = BUILD / "tex_replay/compile_A" / lang / f"Deligne_{lang}.pdf"
                write_bytes(SOURCE / f"Deligne_{lang}.pdf", selected.read_bytes())
                result["languages"][lang] = {"replicas": replicas, "byte_identical": True, "pages": replicas[0]["pages"], "frontmatter_pages": replicas[0]["frontmatter_pages"], "pdf": c.identity(SOURCE / f"Deligne_{lang}.pdf")}
            mutex_report.update(status="PASS", all_captured_trees_ended=True, completed_inside_mutex_utc=now())
            write_json(AUDIT / "TEX_MUTEX_RECEIPT.json", mutex_report)
        result.update(status="PASS", completed_utc=now(), tex_mutex=c.identity(AUDIT / "TEX_MUTEX_RECEIPT.json"), source_manifest=refresh_source_manifest(), source_inputs_modified=False)
        write_json(AUDIT / "COLD_REPRODUCIBILITY_RECEIPT.json", result)
        return result
    except Exception as exc:
        result.update(status="FAIL", failure=str(exc), next_action="Inspect retained worker/replica/log evidence; no automatic retry or replacement worker.")
        mutex_report.update(status="FAIL", failure=str(exc))
        write_json(AUDIT / "TEX_MUTEX_RECEIPT.json", mutex_report)
        write_json(AUDIT / "COLD_REPRODUCIBILITY_RECEIPT.json", result)
        raise


def signature(page):
    import fitz
    pix = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False, colorspace=fitz.csRGB)
    text = re.sub(r"\s+", " ", page.get_text()).strip()
    return {"raster_sha256": hashlib.sha256(pix.samples).hexdigest().upper(), "text_sha256": hashlib.sha256(text.encode()).hexdigest().upper(), "width": pix.width, "height": pix.height, "characters": len(text)}


def glyph_image_geometry(page, ref):
    def glyphs(p):
        return [(ch["c"], ch["bbox"]) for block in p.get_text("rawdict")["blocks"] if block["type"] == 0 for line in block["lines"] for span in line["spans"] for ch in span["chars"]]
    left, right = glyphs(page), glyphs(ref)
    c.require(len(left) == len(right), "inserted glyph count")
    maximum = 0.0
    for a, b in zip(left, right):
        c.require(a[0] == b[0], "inserted glyph sequence")
        maximum = max(maximum, *(abs(x-y) for x, y in zip(a[1], b[1])))
    left_images, right_images = page.get_image_info(hashes=True), ref.get_image_info(hashes=True)
    c.require(len(left_images) == len(right_images), "inserted native-image count")
    for a, b in zip(left_images, right_images):
        c.require(all(a[key] == b[key] for key in ("width", "height", "colorspace", "bpc", "digest")), "inserted native-image pixels/dictionary")
        maximum = max(maximum, *(abs(x-y) for x, y in zip(a["bbox"], b["bbox"])))
    c.require(maximum <= 0.1 and abs(page.rect.width-ref.rect.width) <= 0.1 and abs(page.rect.height-ref.rect.height) <= 0.1, "inserted geometry deviation")
    vector = vector_geometry(page.get_drawings(), ref.get_drawings())
    source_fonts = font_programs(ref)
    current_fonts = font_programs(page)
    c.require(source_fonts == current_fonts, "inserted used-font program mismatch")
    return {"glyphs": len(left), "native_images": len(left_images), "maximum_position_deviation_points": maximum, "vector_drawings": vector["drawings"], "maximum_vector_position_deviation_points": vector["maximum_coordinate_deviation_points"], "used_font_programs": source_fonts}


def vector_geometry(left, right):
    """Preserve native TikZ strokes/fills, not merely text and image boxes."""
    c.require(len(left) == len(right), "inserted vector drawing count")
    maximum = 0.0

    def compare(a, b):
        nonlocal maximum
        if isinstance(a, (int, float)) and not isinstance(a, bool):
            c.require(isinstance(b, (int, float)), "vector numeric type")
            maximum = max(maximum, abs(a-b))
        elif isinstance(a, str) or a is None or isinstance(a, bool):
            c.require(a == b, "vector operator/style")
        else:
            c.require(len(a) == len(b), "vector item arity")
            for x, y in zip(a, b):
                compare(x, y)

    for a, b in zip(left, right):
        for key in ("type", "stroke_opacity", "color", "lineCap", "lineJoin", "closePath", "dashes", "fill", "fill_opacity", "even_odd"):
            c.require(a.get(key) == b.get(key), "vector stroke/fill style")
        c.require(abs(a.get("width", 0)-b.get("width", 0)) <= 0.001, "vector stroke width")
        compare(a["items"], b["items"])
        compare(a["rect"], b["rect"])
    c.require(maximum <= 0.1, "vector coordinate deviation")
    return {"drawings": len(left), "maximum_coordinate_deviation_points": maximum}


def font_programs(page):
    used = {span["font"] for block in page.get_text("dict")["blocks"] if block["type"] == 0 for line in block["lines"] for span in line["spans"]}
    result = {name: set() for name in used}
    for font in page.get_fonts(full=True):
        base = re.sub(r"^[A-Z]{6}\+", "", font[3])
        if base in used:
            _, extension, kind, data = page.parent.extract_font(font[0])
            c.require(bool(data), "used embedded font program unavailable")
            result[base].add((extension, kind, hashlib.sha256(data).hexdigest().upper()))
    c.require(all(result.values()), "used font could not be bound to embedded bytes")
    return {name: sorted(programs) for name, programs in sorted(result.items())}


def contents_entry_links(doc, parts, front):
    """Bind link rectangles to their own printed work rows, including wraps."""
    positions = []
    for part in parts:
        found = [(page_number, word[1]) for page_number in range(1, front) for word in doc[page_number].get_text("words") if word[4] == part["work"]]
        c.require(len(found) == 1, "unique printed work-row anchor missing")
        positions.append(found[0])
    c.require(positions == sorted(positions), "printed row geometry order")
    checks = []
    for index, part in enumerate(parts):
        start_page, start_y = positions[index]
        end_page, end_y = positions[index+1] if index+1 < len(positions) else (front-1, float("inf"))
        targets = []
        for page_number in range(start_page, end_page+1):
            lower = start_y-0.5 if page_number == start_page else float("-inf")
            upper = end_y-0.5 if page_number == end_page else float("inf")
            for link in doc[page_number].get_links():
                rect = link.get("from")
                # Annotation ascent can overlap the neighboring text row;
                # its vertical center assigns each link to one printed entry.
                if rect is not None and isinstance(link.get("page"), int) and lower <= (rect.y0+rect.y1)/2 < upper:
                    targets.append(link["page"])
        c.require(targets and all(target == part["first"]-1 for target in targets), "work-entry contents link target mismatch")
        checks.append({"work": part["work"], "links_bound_to_row": len(targets), "target": part["first"]-1})
    return checks


def contents_entry_page(segment, next_ordinal=None):
    """Read one entry's destination page without consuming the next ordinal.

    Depending on line wrapping, PDF text extraction places the destination on
    either a numeric-only line or at the end of a dotted-leader line.  The
    next entry's ordinal is emitted immediately before its Dxxx anchor, so it
    is the final line of the current anchor-bounded segment and must not be
    treated as this entry's page.
    """
    lines = [line.strip() for line in segment if line.strip()]
    c.require(lines and re.match(r"^D\d{3}\s", lines[0]), "contents entry anchor missing")
    if next_ordinal is not None and lines[-1] == str(next_ordinal):
        lines = lines[:-1]
    candidates = []
    for line in lines:
        if re.fullmatch(r"[0-9]+", line):
            candidates.append(int(line))
            continue
        inline = re.search(r"(?:\.\s*){2,}([0-9]+)\s*$", line)
        if inline:
            candidates.append(int(inline.group(1)))
    c.require(len(candidates) == 1, "ambiguous or missing printed contents page")
    return candidates[0]


def verify_contents(doc, parts, lang):
    front = parts[0]["first"] - 1
    text = "\n".join(doc[i].get_text() for i in range(1, front))
    heading = "Contents\n" if lang == "EN" else "Sommaire\n"
    c.require(heading in text, "contents heading missing")
    lines = text.split(heading, 1)[1].splitlines()
    starts = [i for i, line in enumerate(lines) if re.match(r"^D\d{3}\s", line)]
    c.require(len(starts) == len(parts), "printed contents inventory")
    entry_links = contents_entry_links(doc, parts, front)
    checks = []
    for index, (start, part) in enumerate(zip(starts, parts)):
        end = starts[index+1] if index+1 < len(starts) else len(lines)
        segment = [line.strip() for line in lines[start:end] if line.strip()]
        c.require(re.match(r"^(D\d{3})", segment[0]).group(1) == part["work"], "printed work order")
        next_ordinal = index+2 if index+1 < len(parts) else None
        c.require(contents_entry_page(segment, next_ordinal) == part["first"], "printed contents page differs from physical page")
        marks = [x for x in doc.get_toc() if re.match(r"^" + part["work"] + r"\b", x[1])]
        c.require(len(marks) == 1 and marks[0][2] == part["first"], "bookmark page mismatch")
        c.require(doc[part["first"]-1].get_label() in ("", str(part["first"])), "nonphysical cumulative label")
        checks.append({"work": part["work"], "first": part["first"], "entry_links": entry_links[index], "status": "PASS"})
    return checks


def qa():
    import fitz
    cfg = c.config()
    staged()
    built = c.read_json(AUDIT / "COLD_REPRODUCIBILITY_RECEIPT.json")
    c.require(built["status"] == "PASS", "cumulative clean-build gate")
    pred = Path(cfg["predecessor"]["root"])
    result = {"schema": "d033-cumulative-page-qa-v1", "status": "RUNNING", "languages": {}}
    detail = []
    for lang in c.LANGUAGES:
        current = SOURCE / f"Deligne_{lang}.pdf"
        c.check(current, built["languages"][lang]["pdf"])
        before = pred / "release" / current.name
        new = c.measure_parts(SOURCE, lang, current)
        old = c.measure_parts(pred / "source_tree", lang, before)
        old_map = {x["work"]: x for x in old}
        addition = next(x for x in new if x["work"] == "D033")
        c.require(addition["pages"] == 60 and set(x["work"] for x in new) - set(old_map) == {"D033"}, "D033 inventory/page increment")
        retained = inserted = 0
        geometry = []
        with fitz.open(current) as doc, fitz.open(before) as baseline, fitz.open(SOURCE / addition["path"]) as canonical:
            c.require(signature(doc[0]) == signature(baseline[0]), "cover regression")
            contents = verify_contents(doc, new, lang)
            for index in range(new[0]["first"]-1):
                dest = output(AUDIT / "visual" / f"{lang}-front-{index+1:03}.png")
                dest.parent.mkdir(parents=True, exist_ok=True)
                doc[index].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False).save(dest)
            for part in new:
                for offset in range(part["pages"]):
                    page = doc[part["first"] + offset - 1]
                    sig = signature(page)
                    c.require(sig["characters"] > 0, "empty cumulative reader page")
                    if part["work"] == "D033":
                        reference = canonical[offset]
                        c.require(sig["text_sha256"] == signature(reference)["text_sha256"], "inserted extracted text differs")
                        geometry.append({"standalone_page": offset+1, "cumulative_page": part["first"]+offset, **glyph_image_geometry(page, reference)})
                        inserted += 1
                    else:
                        reference = baseline[old_map[part["work"]]["first"] + offset - 1]
                        c.require(sig == signature(reference), "predecessor page raster/text regression")
                        retained += 1
                    detail.append({"language": lang, "work": part["work"], "page": part["first"]+offset, "status": "PASS", **sig})
                render_offsets = [0, 6, 7, 11, 18, 27, 29, 30, 33, 35, 36, 42, 46, 54, 55, 56, 57, 58, 59] if part["work"] == "D033" else ([part["pages"]-1] if part["work"] == "D031" else ([0] if part["work"] == "D034" else []))
                for offset in render_offsets:
                    dest = output(AUDIT / "visual" / f"{lang}-{part['work']}-{offset+1:03}.png")
                    doc[part["first"]+offset-1].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False).save(dest)
            c.require(retained == sum(x["pages"] for x in old) and inserted == 60 and len(doc) == new[-1]["last"], "body/page accounting")
            result["languages"][lang] = {"pages": len(doc), "frontmatter_pages": new[0]["first"]-1, "predecessor_body_pages_exact": retained, "inserted_pages_exact_text_and_geometry": inserted, "d033": addition, "contents": contents, "include_topology": new, "inserted_geometry": geometry, "pdf": c.identity(current)}
    result.update(status="PASS", all_reader_pages_rasterized_at_72dpi=True, source_inputs_modified=False, visual_next_action="Agent inspects changed frontmatter/boundary/critical-page PNGs and records exact rendered/PDF identities; no human review prerequisite.")
    write_json(AUDIT / "PAGE_IDENTITY_MAP.json", detail)
    result["page_identity_map"] = c.identity(AUDIT / "PAGE_IDENTITY_MAP.json")
    write_json(AUDIT / "CUMULATIVE_PAGE_QA.json", result)
    return result


def release_plan():
    return {"schema": "d033-release-plan-v1", "status": "PLAN_ONLY_NO_ARCHIVES_CREATED", "packaging_implementation": "Separate bounded production step after measured build/QA; no archive writer is exposed by this preparation adapter.", "six_filenames": ["Deligne_EN.pdf", "Deligne_FR.pdf", "Deligne_EN.tex", "Deligne_FR.tex", "Deligne_Source.zip", "DELIGNE_PROVENANCE_AUDIT_D033_GAPFILL.zip"], "public_roots_only": ["build/cumulative/source_tree", "build/cumulative/provenance_tree"], "never_package": ["build/cumulative/private_preservation", "NEXT_INTEGRATION_INPUTS.json", "NEXT_INTEGRATION_LOG.md"], "remaining_deterministic_requirements": ["Agent visual receipt bound to final PDF and rendered-image hashes", "Finalize current README with measured totals/positions while preserving historical narratives", "Replay inherited paths; only six cumulative root names in MUTABLE may change", "Public name scan and original/public evidence-map replay, including nested archive bytes", "Write/replay final source manifest before sealing nonregression receipt", "Deterministic ZIP twins and every-member byte/hash/CRC replay", "Inherit D019 provenance carrier exactly; split only archives at or above2147483648bytes into at most90000000byte binary parts", "Root performs authorized existing-lineage publication and anonymous inventory/full-file byte verification"], "D019_record22307785_public_status": "NOT_ASSERTED_BY_THIS_LOCAL_ADAPTER"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("preflight", "prepare", "manifest", "build", "qa", "release-plan"), nargs="?", default="preflight")
    args = parser.parse_args()
    operation = {"preflight": c.preflight, "prepare": prepare, "manifest": regenerate_manifest, "build": build, "qa": qa, "release-plan": release_plan}[args.stage]
    print(json.dumps(operation(), ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
