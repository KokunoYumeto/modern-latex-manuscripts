from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

from PIL import Image
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "Noether_Paper04_Section08_English_R823_SourceAudited.tex"
PDF = ROOT / "Noether_Paper04_Section08_English_R823_SourceAudited.pdf"
INVENTORY = ROOT / "SHA256SUMS.csv"
INVENTORY_RECEIPT = ROOT / "SHA256SUMS_SELF_RECEIPT.json"
MANIFEST = ROOT / "ZENODO_PAYLOAD_MANIFEST.csv"

CSV_FILES = {
    "ledgers/ADVERSE_WITNESS_COMPARISON_CURRENT.csv": "record_id",
    "ledgers/SOURCE_ALIGNMENT_CURRENT.csv": "record_id",
    "ledgers/SOURCE_CONTROL_HASHES_CURRENT.csv": "control_id",
    "ledgers/SOURCE_FORMULA_NOTE_COMPARISON_CURRENT.csv": "record_id",
    "ledgers/TERMINOLOGY_REJECTED_CHOICES_CURRENT.csv": "record_id",
}
JSONL_FILES = {
    "machine/DIFFICULTY_FAILURE_CURRENT.jsonl": "issue_id",
    "machine/EVIDENCE_GRAPH_CURRENT.jsonl": "record_id",
    "machine/STRUCTURAL_INDEX_CURRENT.jsonl": "record_id",
    "machine/VALIDATION_HISTORY_CURRENT.jsonl": "record_id",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def fail(errors: list[str], label: str, detail: object) -> None:
    errors.append(f"{label}: {detail}")


def read_csv(path: Path) -> list[dict[str, str]]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError("UTF-8 BOM is forbidden")
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None or len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError("missing or duplicate CSV header")
        rows = list(reader)
        if any(set(row) != set(reader.fieldnames) or None in row for row in rows):
            raise ValueError("non-rectangular CSV")
    for row in rows:
        for value in row.values():
            if value and value[0] in "=+-@":
                raise ValueError("spreadsheet-formula trigger")
    return rows


def read_jsonl(path: Path) -> list[dict]:
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError("UTF-8 BOM is forbidden")
    rows: list[dict] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        pairs = json.loads(line, object_pairs_hook=list)
        keys = [key for key, _ in pairs]
        if len(keys) != len(set(keys)):
            raise ValueError(f"duplicate JSON key on line {number}")
        rows.append(dict(pairs))
    return rows


def check_generic_path_and_identifier_surface(errors: list[str]) -> None:
    absolute_path = re.compile(r"(?i)(?:\b[A-Z]:[\\/]|/(?:home|Users)/)")
    uuid = re.compile(r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b")
    text_suffixes = {".md", ".txt", ".csv", ".json", ".jsonl", ".py", ".tex"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_suffixes:
            continue
        raw = path.read_bytes()
        variants: list[str] = [raw.decode("latin-1", errors="ignore")]
        for encoding in ("utf-8", "utf-16-le", "utf-16-be"):
            variants.append(raw.decode(encoding, errors="ignore"))
        for text in variants:
            normalized = text.replace("\\", "/")
            compact = re.sub(r"\s+", "", normalized)
            if absolute_path.search(normalized) or absolute_path.search(compact):
                fail(errors, "privacy", f"absolute path in {path.relative_to(ROOT).as_posix()}")
            if uuid.search(normalized) or uuid.search(compact):
                fail(errors, "privacy", f"UUID in {path.relative_to(ROOT).as_posix()}")


def check_exact_set(errors: list[str]) -> None:
    if not INVENTORY.is_file() or not INVENTORY_RECEIPT.is_file() or not MANIFEST.is_file():
        fail(errors, "exact set", "inventory controls are missing")
        return
    rows = read_csv(INVENTORY)
    if set(rows[0]) != {"relative_path", "bytes", "sha256"} if rows else True:
        fail(errors, "inventory", "unexpected header or empty inventory")
        return
    paths = [row["relative_path"] for row in rows]
    if len(paths) != len(set(paths)) or paths != sorted(paths):
        fail(errors, "inventory", "paths are duplicated or unsorted")
    actual = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and path.name not in {INVENTORY.name, INVENTORY_RECEIPT.name}
    }
    if set(paths) != actual:
        fail(errors, "inventory", f"exact-set delta missing={sorted(actual-set(paths))} extra={sorted(set(paths)-actual)}")
    for row in rows:
        path = ROOT / row["relative_path"]
        if not path.is_file():
            continue
        if int(row["bytes"]) != path.stat().st_size or row["sha256"] != sha256(path):
            fail(errors, "inventory", f"size/hash mismatch: {row['relative_path']}")
    receipt = json.loads(INVENTORY_RECEIPT.read_text(encoding="utf-8"))
    if receipt.get("sha256") != sha256(INVENTORY) or receipt.get("bytes") != INVENTORY.stat().st_size:
        fail(errors, "inventory receipt", "receipt does not authenticate SHA256SUMS.csv")
    if receipt.get("rows") != len(rows):
        fail(errors, "inventory receipt", "row count mismatch")

    manifest_rows = read_csv(MANIFEST)
    content_paths = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and path.name not in {MANIFEST.name, INVENTORY.name, INVENTORY_RECEIPT.name}
    }
    declared = {row["relative_path"] for row in manifest_rows}
    if declared != content_paths or len(declared) != len(manifest_rows):
        fail(errors, "manifest", "manifest is not the exact content-file set")
    for row in manifest_rows:
        path = ROOT / row["relative_path"]
        if not path.is_file() or int(row["bytes"]) != path.stat().st_size or row["sha256"] != sha256(path):
            fail(errors, "manifest", f"size/hash mismatch: {row['relative_path']}")


def check_file_surface(errors: list[str]) -> None:
    allowed = {".csv", ".json", ".jsonl", ".md", ".pdf", ".png", ".py", ".tex", ".txt"}
    archive_magic = (b"PK\x03\x04", b"7z\xbc\xaf'\x1c", b"Rar!", b"\x1f\x8b")
    for path in ROOT.rglob("*"):
        if path.is_symlink():
            fail(errors, "file surface", f"symbolic link: {path.relative_to(ROOT).as_posix()}")
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() not in allowed:
            fail(errors, "file surface", f"forbidden suffix: {rel}")
        if any(part in {"..", ""} for part in Path(rel).parts):
            fail(errors, "file surface", f"unsafe relative path: {rel}")
        head = path.read_bytes()[:8]
        if any(head.startswith(magic) for magic in archive_magic):
            fail(errors, "file surface", f"archive magic: {rel}")
    forbidden_names = [".aux", ".out", ".log", ".zip", ".7z", ".rar", ".gz", ".djvu"]
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in forbidden_names:
            fail(errors, "file surface", f"forbidden artifact: {path.relative_to(ROOT).as_posix()}")
    pngs = sorted(path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*.png"))
    expected_pngs = [f"evidence/rendered_pdf/page-{index}.png" for index in range(1, 5)] + [
        "evidence/rendered_pdf/contact_sheet.png"
    ]
    if sorted(expected_pngs) != pngs:
        fail(errors, "source exclusion", f"unexpected PNG set: {pngs}")
    for rel in expected_pngs:
        with Image.open(ROOT / rel) as image:
            if image.format != "PNG" or image.width < 1000 or image.height < 1000:
                fail(errors, "render", f"unexpected PNG geometry: {rel} {image.size}")


def check_machine_data(errors: list[str]) -> None:
    defined: set[str] = set()
    csv_rows: dict[str, list[dict[str, str]]] = {}
    json_rows: dict[str, list[dict]] = {}
    for rel, id_field in CSV_FILES.items():
        rows = read_csv(ROOT / rel)
        csv_rows[rel] = rows
        ids = [row[id_field] for row in rows]
        if len(ids) != len(set(ids)):
            fail(errors, "CSV IDs", f"duplicate current ID in {rel}")
        if any(int(row.get("revision") or 1) < 1 for row in rows):
            fail(errors, "CSV revisions", rel)
        overlap = defined.intersection(ids)
        if overlap:
            fail(errors, "global IDs", f"duplicate definitions {sorted(overlap)}")
        defined.update(ids)
    for rel, id_field in JSONL_FILES.items():
        rows = read_jsonl(ROOT / rel)
        json_rows[rel] = rows
        ids = [row[id_field] for row in rows]
        if len(ids) != len(set(ids)):
            fail(errors, "JSONL IDs", f"duplicate current ID in {rel}")
        if any(int(row.get("revision") or 1) < 1 for row in rows):
            fail(errors, "JSONL revisions", rel)
        overlap = defined.intersection(ids)
        if overlap:
            fail(errors, "global IDs", f"duplicate definitions {sorted(overlap)}")
        defined.update(ids)

    alignment = csv_rows["ledgers/SOURCE_ALIGNMENT_CURRENT.csv"]
    covered: list[int] = []
    for row in alignment:
        match = re.fullmatch(r"(\d+)-(\d+)", row["r823_lines"])
        if not match:
            fail(errors, "alignment", row["r823_lines"])
            continue
        start, end = map(int, match.groups())
        covered.extend(range(start, end + 1))
    if covered != list(range(4270, 4476)):
        fail(errors, "alignment", "does not partition lines 4270-4475 exactly once in order")

    adverse = csv_rows["ledgers/ADVERSE_WITNESS_COMPARISON_CURRENT.csv"]
    classes = Counter(row["record_class"] for row in adverse)
    formula_occurrences = sum(int(row["occurrence_count"]) for row in adverse if row["record_class"] == "formula_regression")
    ambiguity_occurrences = sum(int(row["occurrence_count"]) for row in adverse if row["record_class"] == "ambiguity_control")
    if classes != Counter({"formula_regression": 6, "ambiguity_control": 2}):
        fail(errors, "adverse accounting", dict(classes))
    if formula_occurrences != 8 or ambiguity_occurrences != 0:
        fail(errors, "adverse accounting", f"formula={formula_occurrences} ambiguity={ambiguity_occurrences}")

    graph = json_rows["machine/EVIDENCE_GRAPH_CURRENT.jsonl"]
    graph_ids = {row["record_id"] for row in graph}
    for row in graph:
        for ref in row.get("depends_on", []) + row.get("supports", []):
            if ref not in defined:
                fail(errors, "evidence reference", f"{row['record_id']} -> {ref}")
        artifact = str(row.get("artifact", ""))
        if ":" not in artifact:
            path = ROOT / artifact
            if not path.is_file():
                fail(errors, "evidence artifact", f"missing {artifact}")
            elif int(row["bytes"]) != path.stat().st_size or row["sha256"] != sha256(path):
                fail(errors, "evidence artifact", f"size/hash mismatch {artifact}")

    structural = json_rows["machine/STRUCTURAL_INDEX_CURRENT.jsonl"]
    structural_by_id = {row["record_id"]: row for row in structural}
    for row in structural:
        parent = row.get("parent_id")
        if parent is not None:
            if parent not in structural_by_id or row["record_id"] not in structural_by_id[parent].get("children", []):
                fail(errors, "structure", f"parent reciprocity {row['record_id']}")
        for child in row.get("children", []):
            if child not in structural_by_id or structural_by_id[child].get("parent_id") != row["record_id"]:
                fail(errors, "structure", f"child reciprocity {row['record_id']} -> {child}")
    if graph_ids != {f"N04-S08-EVID-{index:03d}" for index in range(1, 21)}:
        fail(errors, "evidence graph", "expected EVID-001 through EVID-020")


def check_tex_pdf(errors: list[str]) -> None:
    if sha256(TEX) != "5D579A47B0736102E0AB842A3CD0E1FF2232940226F608CBB33FCF88668CA22A":
        fail(errors, "TeX", "locked hash mismatch")
    if sha256(PDF) != "779B24EFD7B81006BC5A1994E49A7778422EAEE158320650FA50913F4A9858A3":
        fail(errors, "PDF", "locked hash mismatch")
    tex = TEX.read_text(encoding="utf-8")
    dependency_controls = ("\\input", "\\include", "\\includegraphics", "\\bibliography", "\\addbibresource")
    if any(control in tex for control in dependency_controls):
        fail(errors, "TeX", "external build dependency")
    for number in range(62, 71):
        if tex.count(f"\\tag{{{number}}}") != 1:
            fail(errors, "TeX", f"formula tag {number} count")
    for defect in range(1, 5):
        if tex.count(f"N04-S08-SRCDEF-{defect:03d}") != 1:
            fail(errors, "TeX", f"source-defect disclosure {defect}")
    if tex.count("\\footnote{") != 6:
        fail(errors, "TeX", "expected six footnotes")

    reader = PdfReader(str(PDF))
    if reader.is_encrypted or len(reader.pages) != 4:
        fail(errors, "PDF", "encryption or page count")
    if not reader.metadata or not reader.metadata.title or not reader.metadata.author or not reader.metadata.subject:
        fail(errors, "PDF", "metadata missing")
    unique_fonts: dict[tuple[int, int], object] = {}
    for page in reader.pages:
        resources = page.get("/Resources", {}).get_object()
        font_dictionary = (resources.get("/Font") or {}).get_object()
        for reference in font_dictionary.values():
            if not hasattr(reference, "idnum") or not hasattr(reference, "generation"):
                fail(errors, "PDF fonts", "direct font object")
                continue
            unique_fonts[(reference.idnum, reference.generation)] = reference.get_object()
    if len(unique_fonts) != 24:
        fail(errors, "PDF fonts", f"expected 24, found {len(unique_fonts)}")
    for key, font in unique_fonts.items():
        base_font = str(font.get("/BaseFont", ""))
        if not re.fullmatch(r"/[A-Z]{6}\+.+", base_font) or font.get("/ToUnicode") is None:
            fail(errors, "PDF fonts", f"subset/Unicode {key}")
        if str(font.get("/Subtype")) == "/Type0":
            descendants = font.get("/DescendantFonts") or []
            descriptor_ref = descendants[0].get_object().get("/FontDescriptor") if len(descendants) == 1 else None
        else:
            descriptor_ref = font.get("/FontDescriptor")
        descriptor = descriptor_ref.get_object() if descriptor_ref is not None else {}
        if not any(descriptor.get(name) is not None for name in ("/FontFile", "/FontFile2", "/FontFile3")):
            fail(errors, "PDF fonts", f"embedding {key}")

    catalog = reader.trailer["/Root"].get_object()
    if any(catalog.get(name) is not None for name in ("/AA", "/AcroForm", "/Collection")):
        fail(errors, "PDF actions", "catalog additional action/form/collection")
    open_action_ref = catalog.get("/OpenAction")
    open_action = open_action_ref.get_object() if open_action_ref is not None else {}
    destination = open_action.get("/D")
    first_page_ref = reader.pages[0].indirect_reference
    if not (
        str(open_action.get("/S")) == "/GoTo"
        and isinstance(destination, list)
        and len(destination) == 2
        and hasattr(destination[0], "idnum")
        and destination[0].idnum == first_page_ref.idnum
        and str(destination[1]) == "/Fit"
    ):
        fail(errors, "PDF actions", "unexpected OpenAction")
    names_ref = catalog.get("/Names")
    names = names_ref.get_object() if names_ref is not None else {}
    if set(names) != {"/Dests"}:
        fail(errors, "PDF actions", f"unexpected name tree {sorted(names)}")
    raw_pdf = PDF.read_bytes()
    for token in (b"/JavaScript", b"/JS", b"/URI", b"/Launch", b"/SubmitForm", b"/ImportData", b"/Rendition", b"/RichMedia", b"/EmbeddedFiles"):
        if token in raw_pdf:
            fail(errors, "PDF actions", f"forbidden token {token!r}")
    link_counts: list[int] = []
    for page_number, page in enumerate(reader.pages, 1):
        if page.get("/AA") is not None:
            fail(errors, "PDF actions", f"page {page_number} additional action")
        annotations = page.get("/Annots") or []
        link_counts.append(len(annotations))
        for annotation_ref in annotations:
            annotation = annotation_ref.get_object()
            action_ref = annotation.get("/A")
            action = action_ref.get_object() if hasattr(action_ref, "get_object") else action_ref
            if not (
                str(annotation.get("/Subtype")) == "/Link"
                and annotation.get("/AA") is None
                and annotation.get("/Dest") is None
                and isinstance(action, dict)
                and str(action.get("/S")) == "/GoTo"
                and str(action.get("/D", "")).startswith("Hfootnote.")
            ):
                fail(errors, "PDF actions", f"non-footnote link on page {page_number}")
    if link_counts != [0, 1, 1, 4]:
        fail(errors, "PDF actions", f"link distribution {link_counts}")


def main() -> int:
    errors: list[str] = []
    checks = [check_generic_path_and_identifier_surface, check_exact_set, check_file_surface, check_machine_data, check_tex_pdf]
    for check in checks:
        try:
            check(errors)
        except Exception as exc:
            fail(errors, check.__name__, exc)
    result = {
        "schema": "N04-S08-public-checkpoint-validation-v1",
        "status": "PASS" if not errors else "FAIL",
        "failure_count": len(errors),
        "failures": errors,
        "scope": "R823 lines 4270-4475; printed 146-152; physical 29-35; cursor 4477 Section 9",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
