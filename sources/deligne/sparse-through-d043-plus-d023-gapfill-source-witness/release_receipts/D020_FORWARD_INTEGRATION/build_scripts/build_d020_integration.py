"""D020-specific local cumulative preparation/build/QA; no publication code.

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

import d020_contract as c
from tex_worker import Mutex, MUTEX_NAME, tex_pass, scan_log_anomalies, job_memory_policy

BUILD = c.TASK / "build/cumulative"
SOURCE = BUILD / "source_tree"
AUDIT = BUILD / "audit"
PROVENANCE = BUILD / "provenance_tree"
PRIVATE = BUILD / "private_preservation"
RECEIPTS = SOURCE / "release_receipts/D020_FORWARD_INTEGRATION"


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def output(path):
    path = Path(path)
    c.require(path.is_absolute(), "output must be absolute")
    try:
        relative = path.relative_to(BUILD).as_posix()
    except ValueError as exc:
        raise c.Failure("write outside D020 build child") from exc
    return c.confined(BUILD, relative)


def write_bytes(path, data):
    path = output(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    c.reject_reparse(path.parent)
    temporary = path.with_name(f".{path.name}.d020-{os.getpid()}.tmp")
    c.require(not temporary.exists(), "stale D020 temporary file")
    try:
        temporary.write_bytes(data)
        c.check(temporary, c.identity_bytes(data))
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)
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
        temporary = dest.with_name(f".{dest.name}.d020-copy-{os.getpid()}.tmp")
        c.require(not temporary.exists(), "stale D020 copy temporary file")
        try:
            with Path(src).open("rb") as reader, temporary.open("xb") as writer:
                shutil.copyfileobj(reader, writer, 1024 * 1024)
            c.check(temporary, expected)
            os.replace(temporary, dest)
        finally:
            temporary.unlink(missing_ok=True)
        c.check(dest, expected)
    return expected


def replace_exact(src, dest, expected=None):
    expected = expected or c.identity(src)
    c.check(src, expected)
    dest = output(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    c.reject_reparse(dest.parent)
    temporary = dest.with_name(f".{dest.name}.d020-replace-{os.getpid()}.tmp")
    c.require(not temporary.exists(), "stale D020 replacement temporary file")
    try:
        with Path(src).open("rb") as reader, temporary.open("xb") as writer:
            shutil.copyfileobj(reader, writer, 1024 * 1024)
        c.check(temporary, expected)
        os.replace(temporary, dest)
    finally:
        temporary.unlink(missing_ok=True)
    c.check(dest, expected)
    return expected


def link_exact(src, dest, expected):
    """Hardlink immutable predecessor bytes; changed roots are atomically replaced."""
    c.check(src, expected)
    dest = output(dest)
    c.require(not dest.exists(), "predecessor clone destination already exists")
    dest.parent.mkdir(parents=True, exist_ok=True)
    c.reject_reparse(dest.parent)
    os.link(src, dest)
    c.check(dest, expected)
    return expected


def refresh_source_manifest():
    """Write and immediately replay the actual source tree, excluding itself."""
    manifest = SOURCE / c.SOURCE_MANIFEST_NAME
    manifest_identity = write_bytes(manifest, c.source_manifest_bytes(SOURCE))
    rows = c.verify_source_manifest(SOURCE, manifest)
    return {"status": "PASS", "members": len(rows), "manifest": manifest_identity}


def patch_readme(text):
    replacements = {
        "Included complete works, in numerical order: D001-D019, D021, D022, D023,": "Included complete works, in numerical order: D001-D023,",
        "Explicit gaps through the current sparse sequence: D020, D024,": "Explicit gaps through the current sparse sequence: D024,",
        "This release contains 1100 English and 1113 French pages.": "This release contains __D020_EN_TOTAL__ English and __D020_FR_TOTAL__ French pages.",
        "under `release_receipts/D033_FORWARD_INTEGRATION/`.": "under `release_receipts/D020_FORWARD_INTEGRATION/`.",
        "D020 remains 30/36 with P06 next; ": "D020 is complete at 36/36 physical authority pages and 35/35 scholarly reader pages; ",
    }
    for old, new in replacements.items():
        c.require(text.count(old) == 1, "README update anchor mismatch")
        text = text.replace(old, new, 1)
    text += "\n## D020 gap insertion\n\nD020, *La conjecture de Weil. I* / *The Weil Conjecture. I*, is inserted after D019 and before D021. French is the source-language edition and English is the standalone translation. Each scholarly reader contains 35 pages aligned to printed 273-307; the 36-page authority cover is excluded from the scholarly body and retained in provenance. D020 occupies English cumulative pages __D020_EN_FIRST__-__D020_EN_LAST__ and French cumulative pages __D020_FR_FIRST__-__D020_FR_LAST__. The 36-page restrained apparatus is preserved separately and is not appended to either cumulative reader.\n\nThe immutable V6 state, editable TeX, offline MathML HTML, source-aligned records, assets, comparators, authority, ZERO_ACCEPTED salvage, and fresh memory-bounded nonpatching cold-audit PASS are preserved under `works/D020_PUBLIC_SAFE`; the full cold-audit tree is also carried in the consolidated provenance archive. Included coverage is D001-D023; D025-D031; D033-D036; D038-D040; D043. Explicit public gaps are D024; D032; D037; D041-D042.\n"
    return text


def d020_public_readme(cfg):
    return f"""# D020 — La conjecture de Weil. I / The Weil Conjecture. I

Status: PAPER_COMPLETE; independent fresh nonpatching V6 cold audit PASS.

French is the source-language edition; English is the standalone translation. Both canonical scholarly readers contain 35 pages aligned to printed 273–307. The 36-page controlling authority includes an excluded repository cover; the restrained apparatus retains all 36 physical-page records and is not included in either cumulative reader.

`state/` is the immutable 328-file V6 subject, copied byte-for-byte from its sealed subject manifest, including the exact ZERO_ACCEPTED prior-work carrier. `cold_audit/` contains the decisive subject manifest and final audit receipts. The complete frozen audit tree, render contacts, guard receipts, and all evidence are also preserved in the consolidated provenance carrier.

Canonical reader mapping:

- French cumulative reader: `state/readers/pdf/source_language.pdf`
- English cumulative reader: `state/readers/pdf/english_standalone.pdf`
- Separate apparatus: `state/readers/pdf/apparatus.pdf`

The source authority SHA-256 is `{cfg['d020']['authority']['sha256']}`. No transcript-style HTML or preformatted-TeX PDF is used as the canonical cumulative reader input.
"""


def prepare():
    cfg = c.config()
    report = c.preflight()
    c.require(not SOURCE.exists() and not PROVENANCE.exists() and not PRIVATE.exists(), "staging already exists: inspect retained cursor; do not restart/duplicate")
    pred = Path(cfg["predecessor"]["root"])
    rows = c.manifest_rows(cfg["predecessor"]["source_manifest"]["path"])
    stage = {"schema": "d020-source-preparation-v1", "status": "RUNNING", "started_utc": now(), "preflight": report, "publication_identity": "UNVERIFIED_TARGET_ONLY", "clone_policy": "NTFS_HARDLINK_IMMUTABLE_PREDECESSOR__ATOMIC_REPLACE_MUTABLE_ROOTS"}
    write_json(AUDIT / "SOURCE_PREPARATION_RECEIPT.json", stage)
    try:
        for row in rows:
            link_exact(c.confined(pred / "source_tree", row["path"]), SOURCE / row["path"], row)

        work_root = Path(cfg["d020"]["work_root"])
        subject = c.read_json(cfg["d020"]["subject_manifest"]["path"])
        for item in subject["files"]:
            copy_exact(c.confined(work_root, item["path"]), SOURCE / "works/D020_PUBLIC_SAFE/state" / item["path"], item)
        for item in c.evidence_closure(cfg):
            copy_exact(item["path"], SOURCE / "works/D020_PUBLIC_SAFE/cold_audit" / item["relative_path"], item)
        write_bytes(SOURCE / "works/D020_PUBLIC_SAFE/README.md", d020_public_readme(cfg).encode("utf-8"))

        cold_root = Path(cfg["d020"]["cold_audit_root"])
        cold_names = c.inventory_tree(cold_root)
        c.require(len(cold_names) == 585, "D020 cold-audit tree inventory differs")
        for relative in cold_names:
            copy_exact(c.confined(cold_root, relative), PROVENANCE / "D020/S06_math_v6_01" / relative)
        inherited = next(x for x in cfg["predecessor"]["release_files"] if Path(x["path"]).name == "DELIGNE_PROVENANCE_AUDIT_D033_GAPFILL.zip")
        copy_exact(inherited["path"], PROVENANCE / "inherited" / Path(inherited["path"]).name, inherited)
        binding = {
            "schema": "d020-public-cold-audit-binding-v1",
            "status": "PASS",
            "subject_manifest": {key: cfg["d020"]["subject_manifest"][key] for key in ("bytes", "sha256")},
            "final_audit": {key: cfg["d020"]["final_audit"][key] for key in ("bytes", "sha256")},
            "source_tree_state_prefix": "works/D020_PUBLIC_SAFE/state/",
            "provenance_tree_prefix": "D020/S06_math_v6_01/",
            "subject_members": cfg["d020"]["subject_members"],
            "subject_member_bytes": cfg["d020"]["subject_member_bytes"],
            "candidate_public_surface_status": "PASS",
        }
        write_json(SOURCE / "works/D020_PUBLIC_SAFE/D020_COLD_AUDIT_BINDING.json", binding)
        write_json(PROVENANCE / "D020/D020_COLD_AUDIT_BINDING.json", binding)
        for lang in c.LANGUAGES:
            original = (pred / "source_tree" / f"Deligne_{lang}.tex").read_text(encoding="utf-8")
            write_bytes(SOURCE / f"Deligne_{lang}.tex", c.patch_master(original, lang, cfg).encode("utf-8"))
        write_bytes(SOURCE / "README.md", patch_readme((pred / "source_tree/README.md").read_text(encoding="utf-8")).encode("utf-8"))
        copy_exact(cfg["predecessor"]["receipt"]["path"], RECEIPTS / "D033_PREDECESSOR_BUILD_RELEASE_RECEIPT.json", cfg["predecessor"]["receipt"])
        source_manifest = refresh_source_manifest()
        frozen = [{"path": name, **c.identity(SOURCE / name)} for name in c.inventory_tree(SOURCE) if name not in {"Deligne_EN.pdf", "Deligne_FR.pdf", "README.md", "PUBLIC_SOURCE_MANIFEST.tsv"}]
        stage.update(status="PASS", finished_utc=now(), immutable_stage_files=frozen, mutable_roots=sorted(c.MUTABLE), source_manifest=source_manifest, d020_subject_members_copied=len(subject["files"]), d020_cold_audit_members_copied=len(cold_names), canonical_reader_mapping=cfg["insertion"]["source_reader_mapping"], source_inputs_modified=False, next_action="Explicit serial memory-capped build stage; no TeX has run.")
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


def check_tex_logs(process, stdout_log, engine_log):
    process["stdout_log_anomalies"] = scan_log_anomalies(stdout_log)
    process["engine_log_anomalies"] = scan_log_anomalies(engine_log)
    c.require(process["return_code"] == 0 and not any(process["stdout_log_anomalies"].values()) and not any(process["engine_log_anomalies"].values()), "TeX stdout/full-engine-log anomaly")


def log_requests_rerun(*paths):
    pattern = re.compile(r"Rerun to get cross-references right|Label\(s\) may have changed", re.IGNORECASE)
    for path in paths:
        with Path(path).open("r", encoding="utf-8", errors="replace") as stream:
            if any(pattern.search(line) for line in stream):
                return True
    return False


def build():
    import fitz
    cfg = c.config()
    staged()
    c.require(not (AUDIT / "COLD_REPRODUCIBILITY_RECEIPT.json").exists(), "build already has a receipt; inspect current state instead of duplicate launch")
    engine = Path(cfg["runtime"]["engine"])
    engine_id = c.identity(engine)
    memory_policy = job_memory_policy()
    result = {"schema": "d020-cumulative-reproducibility-v1", "status": "RUNNING", "started_utc": now(), "engine": engine_id, "languages": {}, "maximum_passes_per_replica": 5, "minimum_passes_per_replica": 3, "clean_replicas": 3, "tex_process_tree_memory_policy": memory_policy, "maximum_observed_tex_job_memory_bytes": 0}
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
                        worker_stdout = output(AUDIT / "tex_logs" / f"{replica}_{lang}_{pass_number}.worker.txt")
                        worker_stdout.parent.mkdir(parents=True, exist_ok=True)
                        process = tex_pass(mutex, engine, slot, f"Deligne_{lang}.tex", cfg["runtime"]["environment"], worker_stdout)
                        result["maximum_observed_tex_job_memory_bytes"] = max(result["maximum_observed_tex_job_memory_bytes"], process["peak_job_memory_bytes"])
                        mutex_report["maximum_observed_tex_job_memory_bytes"] = result["maximum_observed_tex_job_memory_bytes"]
                        process["stdout"] = c.identity(worker_stdout)
                        engine_source = c.reject_reparse(slot / f"Deligne_{lang}.log")
                        engine_copy = AUDIT / "tex_logs" / f"{replica}_{lang}_{pass_number}.engine.log"
                        process["engine_log"] = copy_exact(engine_source, engine_copy)
                        check_tex_logs(process, worker_stdout, engine_copy)
                        passes.append({"pass": pass_number, "process": process, "toc": c.identity(slot / f"Deligne_{lang}.toc"), "pdf": c.identity(slot / f"Deligne_{lang}.pdf")})
                        mutex_report["passes"] += 1
                        write_json(AUDIT / "TEX_MUTEX_RECEIPT.json", mutex_report)
                        settled = c.converged(passes)
                        rerun_warning = log_requests_rerun(worker_stdout, engine_copy)
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
                replace_exact(selected, SOURCE / f"Deligne_{lang}.pdf")
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
        return [(ch["c"], ch["bbox"]) for block in p.get_text("rawdict")["blocks"] if block["type"] == 0 for line in block["lines"] for span in line["spans"] for ch in span["chars"] if not ch["c"].isspace()]
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
    return {"visible_nonwhitespace_glyphs": len(left), "native_images": len(left_images), "maximum_position_deviation_points": maximum, "vector_drawings": vector["drawings"], "maximum_vector_position_deviation_points": vector["maximum_coordinate_deviation_points"], "used_font_programs": source_fonts}


def extracted_text_equivalence(page, ref):
    current = re.sub(r"\s+", " ", page.get_text()).strip()
    canonical = re.sub(r"\s+", " ", ref.get_text()).strip()
    whitespace_free_equal = re.sub(r"\s+", "", current) == re.sub(r"\s+", "", canonical)
    c.require(whitespace_free_equal, "inserted nonwhitespace extracted text differs")
    return {"normalized_exact": current == canonical, "whitespace_free_equal": True}


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


def contents_entry_page(segment, expected_page, next_ordinal=None):
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
    numeric_only = []
    dotted = []
    for line in lines:
        if re.fullmatch(r"[0-9]+", line):
            numeric_only.append(int(line))
            continue
        inline = re.search(r"(?:\.\s*){2,}([0-9]+)\s*$", line)
        if inline:
            dotted.append(int(inline.group(1)))
    candidates = numeric_only or dotted
    if not candidates:
        # PyMuPDF can omit the dot glyphs after TOC reflow.  Accept only one
        # whitespace-delimited terminal integer and only when it equals the
        # independently measured physical destination.
        terminal = [int(match.group(1)) for line in lines if (match := re.search(r"\s([0-9]+)\s*$", line))]
        candidates = [value for value in terminal if value == expected_page]
    c.require(candidates == [expected_page], "ambiguous or missing printed contents page")
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
        c.require(contents_entry_page(segment, part["first"], next_ordinal) == part["first"], "printed contents page differs from physical page")
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
    result = {"schema": "d020-cumulative-page-qa-v1", "status": "RUNNING", "languages": {}}
    detail = []
    for lang in c.LANGUAGES:
        current = SOURCE / f"Deligne_{lang}.pdf"
        c.check(current, built["languages"][lang]["pdf"])
        before = pred / "release" / current.name
        new = c.measure_parts(SOURCE, lang, current)
        old = c.measure_parts(pred / "source_tree", lang, before)
        old_map = {x["work"]: x for x in old}
        addition = next(x for x in new if x["work"] == "D020")
        c.require(addition["pages"] == 35 and set(x["work"] for x in new) - set(old_map) == {"D020"}, "D020 inventory/page increment")
        addition_index = [x["work"] for x in new].index("D020")
        c.require([x["work"] for x in new][addition_index-1:addition_index+2] == ["D019", "D020", "D021"], "D020 boundary order")
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
                    if part["work"] == "D020":
                        reference = canonical[offset]
                        text_equivalence = extracted_text_equivalence(page, reference)
                        geometry.append({"standalone_page": offset+1, "cumulative_page": part["first"]+offset, "extracted_text_equivalence": text_equivalence, **glyph_image_geometry(page, reference)})
                        inserted += 1
                    else:
                        reference = baseline[old_map[part["work"]]["first"] + offset - 1]
                        c.require(sig == signature(reference), "predecessor page raster/text regression")
                        retained += 1
                    detail.append({"language": lang, "work": part["work"], "page": part["first"]+offset, "status": "PASS", **sig})
                render_offsets = [0, 1, 5, 11, 17, 18, 24, 30, 34] if part["work"] == "D020" else ([part["pages"]-1] if part["work"] == "D019" else ([0] if part["work"] == "D021" else []))
                for offset in render_offsets:
                    dest = output(AUDIT / "visual" / f"{lang}-{part['work']}-{offset+1:03}.png")
                    doc[part["first"]+offset-1].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False).save(dest)
            c.require(retained == sum(x["pages"] for x in old) and inserted == 35 and len(doc) == new[-1]["last"], "body/page accounting")
            expected = cfg["insertion"]["expected_if_frontmatter_unchanged"][lang]
            if new[0]["first"] - 1 == cfg["predecessor"]["frontmatter_pages"][lang]:
                c.require(len(doc) == expected["total_pages"] and [addition["first"], addition["last"]] == expected["D020"], "D020 expected unchanged-frontmatter position differs")
            result["languages"][lang] = {"pages": len(doc), "frontmatter_pages": new[0]["first"]-1, "predecessor_body_pages_exact": retained, "inserted_pages_exact_text_and_geometry": inserted, "d020": addition, "contents": contents, "include_topology": new, "inserted_geometry": geometry, "pdf": c.identity(current)}
    result.update(status="PASS", all_reader_pages_rasterized_at_72dpi=True, source_inputs_modified=False, visual_next_action="Agent inspects changed frontmatter/boundary/critical-page PNGs and records exact rendered/PDF identities; no human review prerequisite.")
    write_json(AUDIT / "PAGE_IDENTITY_MAP.json", detail)
    result["page_identity_map"] = c.identity(AUDIT / "PAGE_IDENTITY_MAP.json")
    readme = (SOURCE / "README.md").read_text(encoding="utf-8")
    replacements = {
        "__D020_EN_TOTAL__": str(result["languages"]["EN"]["pages"]),
        "__D020_FR_TOTAL__": str(result["languages"]["FR"]["pages"]),
        "__D020_EN_FIRST__": str(result["languages"]["EN"]["d020"]["first"]),
        "__D020_EN_LAST__": str(result["languages"]["EN"]["d020"]["last"]),
        "__D020_FR_FIRST__": str(result["languages"]["FR"]["d020"]["first"]),
        "__D020_FR_LAST__": str(result["languages"]["FR"]["d020"]["last"]),
    }
    for old, new_value in replacements.items():
        c.require(readme.count(old) == 1, "README measurement placeholder mismatch")
        readme = readme.replace(old, new_value)
    write_bytes(SOURCE / "README.md", readme.encode("utf-8"))
    result["source_manifest"] = refresh_source_manifest()
    write_json(AUDIT / "CUMULATIVE_PAGE_QA.json", result)
    return result


def release_plan():
    return {"schema": "d020-release-plan-v1", "status": "PLAN_ONLY_NO_ARCHIVES_CREATED", "six_filenames": ["Deligne_EN.pdf", "Deligne_FR.pdf", "Deligne_EN.tex", "Deligne_FR.tex", "Deligne_Source.zip", "DELIGNE_PROVENANCE_AUDIT_D020_GAPFILL.zip"], "public_roots_only": ["build/cumulative/source_tree", "build/cumulative/provenance_tree"], "never_package": ["build/cumulative/private_preservation", "NEXT_INTEGRATION_INPUTS.json"], "requirements": ["Visual receipt bound to final PDF and PNG hashes", "Predecessor D033 source nonregression", "Final public-name scan", "Deterministic ZIP twins and full member replay", "Inherit D033 provenance carrier byte-identically", "Publish existing GitHub and Zenodo lineages and anonymously read back every byte"], "figshare": "EXCLUDED"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("preflight", "prepare", "manifest", "build", "qa", "release-plan"), nargs="?", default="preflight")
    args = parser.parse_args()
    operation = {"preflight": c.preflight, "prepare": prepare, "manifest": regenerate_manifest, "build": build, "qa": qa, "release-plan": release_plan}[args.stage]
    try:
        print(json.dumps(operation(), ensure_ascii=True, indent=2))
    except Exception as exc:
        if args.stage in {"build", "qa"}:
            write_json(AUDIT / f"{args.stage.upper()}_FAILURE_DIAGNOSIS.json", {
                "schema": "d020-bounded-stage-failure-v1",
                "status": "FAIL",
                "stage": args.stage,
                "failure_type": type(exc).__name__,
                "failure": str(exc)[:1000],
                "automatic_retry": False,
            })
        raise


if __name__ == "__main__":
    main()
