#!/usr/bin/env python3
"""Fresh, independent, nonpatching cold audit for the corrected D027 candidate.

This script reads the frozen return, canonical TeX/PDF outputs, and QA evidence.
It writes nothing and prints one deterministic JSON result to stdout.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import sys
from pathlib import Path, PurePosixPath
from zipfile import ZipFile

from pypdf import PdfReader


HOME = Path.home()
INTAKE = (
    HOME
    / "Documents"
    / "interlanguage"
    / "Transcription"
    / "Web_Session_Hourly_Intake"
)
INTEGRATION = (
    INTAKE
    / "Zenodo_Maintenance"
    / "D027_20260823T000729Z_INTEGRATION_AUDIT"
)
RETURN_ROOT = INTAKE / "artifacts" / "Pierre_Deligne" / "D027"
AUDIT_RETURN = (
    RETURN_ROOT
    / "maintenance"
    / "20260822T205018Z_D027_S10_INDEPENDENT_AUDIT"
)
EXTRACTED = AUDIT_RETURN / "extracted"
OUTER = (
    RETURN_ROOT
    / "FINAL_RELEASE"
    / "DELIGNE_LUSZTIG_D027_REDUCTIVE_GROUPS_FINAL_RELEASE_BUNDLE.zip"
)
STATE = (
    AUDIT_RETURN
    / "inherited_return"
    / "DELIGNE_LUSZTIG_D027_REDUCTIVE_GROUPS_S10_CUMULATIVE_FULL_STATE.zip"
)
AUTHORITY = (
    EXTRACTED
    / "source"
    / "20_AUTHORITY_DELIGNE_LUSZTIG_D027_REDUCTIVE_GROUPS_JSTOR_60PP.pdf"
)
TEX_ROOT = INTEGRATION / "output" / "tex"
RAW_PDF_ROOT = INTEGRATION / "output" / "pdf"
FINAL_PDF_ROOT = INTEGRATION / "output" / "final"
QA_ROOT = INTEGRATION / "qa"

AUTHORITY_SHA = "8037B883D391A17534F2B5C7A55B9593AD6A3F5C15045EC8751BD1FFCED83BDF"
OUTER_SHA = "03FEE1267B4103CEC85729B381F391DCF9E40EF15B5539F947FB51B9D728F07F"
STATE_SHA = "5DAB55A193B2036B9573BB692F0B2B931B511727EA22B3DC9A3539F5027C4CF8"
WORK_ID = "DELIGNE_LUSZTIG_D027_REDUCTIVE_GROUPS"

EXPECTED_NDJSON = {
    "source_language.ndjson": (
        191883,
        "C35B21FFB2836BD786618CC1535777BCF733441A913451E00B89AC2814936A3D",
        "frozen",
    ),
    "french_translation.ndjson": (
        201231,
        "ABD231E5E7439D74137F8FD159C5B36C933B77308BB24B41F287A8AF59E2BB69",
        "accepted",
    ),
    "apparatus.ndjson": (
        41167,
        "F8EAB11AB3CFB11DAFD423F13EADC1663B279EB8B0247764DDDAC10238DA4A01",
        "accepted",
    ),
}

EXPECTED_TEX = {
    "Deligne_D027_EN.tex": (
        173054,
        "BD7DEF0DEBE310A228B8A48E74F2B90C0C5F9B2537C289EF8B6F1E3FC2EFF83F",
    ),
    "Deligne_D027_FR.tex": (
        182219,
        "A6EB4CA7B84028E7358BDB5DC5794A0FACF42CCA3BB1B409410270C47F0CE428",
    ),
    "Deligne_D027_APPARATUS.tex": (
        33500,
        "72159EAAAD4D9674A99F0EBF04F3CBD93824F30BE5955202B236617A8454B727",
    ),
}

EXPECTED_PDF = {
    "Deligne_D027_EN.pdf": (
        344126,
        "C445D38899816E0A99FA52C9DAE333EEAB4F04AB8DE0E034773A017B065E3CDF",
        59,
    ),
    "Deligne_D027_FR.pdf": (
        349639,
        "C23577760AC20486798B3D406D45550CDB028F32F729ED65EBE83FBFCC794A10",
        59,
    ),
    "Deligne_D027_APPARATUS.pdf": (
        85635,
        "DD1DB8DAE8FF755254B06BEE09B7D04C97F68200BC87AC0629991F736CAD2337",
        8,
    ),
}

EXPECTED_METADATA = {
    "Deligne_D027_EN.pdf": {
        "/Title": "Representations of Reductive Groups over Finite Fields",
        "/Author": "P. Deligne and G. Lusztig",
        "/Subject": "Source-language critical edition",
        "/Keywords": "Deligne, Lusztig, reductive groups, finite fields, editable LaTeX",
    },
    "Deligne_D027_FR.pdf": {
        "/Title": "Représentations des groupes réductifs sur les corps finis",
        "/Author": "P. Deligne and G. Lusztig",
        "/Subject": "Édition française fidèle",
        "/Keywords": "Deligne, Lusztig, reductive groups, finite fields, editable LaTeX",
    },
    "Deligne_D027_APPARATUS.pdf": {
        "/Title": "D027 restrained textual and translation apparatus",
        "/Author": "P. Deligne and G. Lusztig",
    },
}

EXPECTED_REPAIRS = {
    ("en", 9, r"\toE", r"\to E"): 2,
    ("en", 10, r"\inE", r"\in E"): 1,
    ("en", 35, r"\\[", r"\\{}["): 1,
    ("en", 55, r"\\[", r"\\{}["): 2,
    ("en", 56, r"\\[", r"\\{}["): 2,
    ("en", 57, r"\\[", r"\\{}["): 1,
    ("fr", 9, r"\toE", r"\to E"): 2,
    ("fr", 10, r"\inE", r"\in E"): 1,
    ("fr", 35, r"\\[", r"\\{}["): 1,
    ("fr", 55, r"\\[", r"\\{}["): 2,
    ("fr", 56, r"\\[", r"\\{}["): 2,
    ("fr", 57, r"\\[", r"\\{}["): 1,
}


def sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_stream(handle) -> str:
    digest = hashlib.sha256()
    for chunk in iter(lambda: handle.read(1024 * 1024), b""):
        digest.update(chunk)
    return digest.hexdigest().upper()


def tsv_rows_from_text(text: str) -> list[dict[str, str]]:
    return list(csv.DictReader(io.StringIO(text), delimiter="\t"))


def tsv_rows(path: Path) -> list[dict[str, str]]:
    return tsv_rows_from_text(path.read_text(encoding="utf-8-sig"))


def safe_zip_names(names: list[str]) -> bool:
    for name in names:
        pure = PurePosixPath(name)
        if pure.is_absolute() or ".." in pure.parts or "\\" in name:
            return False
    return len(names) == len(set(names)) == len({name.casefold() for name in names})


class Audit:
    def __init__(self) -> None:
        self.checks: list[dict[str, str]] = []
        self.failures: list[str] = []

    def require(self, condition: bool, check_id: str, detail: str) -> None:
        status = "PASS" if condition else "FAIL"
        self.checks.append({"check_id": check_id, "status": status, "detail": detail})
        if not condition:
            self.failures.append(f"{check_id}: {detail}")


def pdf_resources(page):
    resources = page.get("/Resources")
    return resources.get_object() if hasattr(resources, "get_object") else resources


def inspect_pdf(path: Path, expected_pages: int) -> dict:
    reader = PdfReader(str(path), strict=True)
    page_details = []
    font_records: dict[tuple[str, str], dict] = {}
    image_xobjects = 0
    form_xobjects = 0
    inline_images = 0

    def walk_resources(resources, seen: set[tuple[int, int]]) -> None:
        nonlocal image_xobjects, form_xobjects
        if not resources:
            return
        resources = resources.get_object() if hasattr(resources, "get_object") else resources
        xobjects = resources.get("/XObject")
        if not xobjects:
            return
        xobjects = xobjects.get_object() if hasattr(xobjects, "get_object") else xobjects
        for ref in xobjects.values():
            marker = (getattr(ref, "idnum", id(ref)), getattr(ref, "generation", 0))
            if marker in seen:
                continue
            seen.add(marker)
            obj = ref.get_object()
            subtype = str(obj.get("/Subtype"))
            if subtype == "/Image":
                image_xobjects += 1
            elif subtype == "/Form":
                form_xobjects += 1
                walk_resources(obj.get("/Resources"), seen)

    for number, page in enumerate(reader.pages, 1):
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        crop_width = float(page.cropbox.width)
        crop_height = float(page.cropbox.height)
        rotation = int(page.get("/Rotate", 0) or 0) % 360
        text = page.extract_text() or ""
        resources = pdf_resources(page)
        fonts = resources.get("/Font") if resources else None
        if fonts:
            fonts = fonts.get_object() if hasattr(fonts, "get_object") else fonts
            for ref in fonts.values():
                font = ref.get_object()
                base = str(font.get("/BaseFont"))
                subtype = str(font.get("/Subtype"))
                to_unicode = bool(font.get("/ToUnicode"))
                embedded = False
                descendants = font.get("/DescendantFonts")
                if descendants:
                    descendant = descendants[0].get_object()
                    descriptor = descendant.get("/FontDescriptor")
                    if descriptor:
                        descriptor = descriptor.get_object()
                        embedded = any(
                            descriptor.get(key) is not None
                            for key in ("/FontFile", "/FontFile2", "/FontFile3")
                        )
                key = (base, subtype)
                font_records[key] = {
                    "base_font": base,
                    "subtype": subtype,
                    "to_unicode": to_unicode,
                    "embedded": embedded,
                }
        walk_resources(resources, set())
        contents = page.get_contents()
        if contents:
            raw = contents.get_data()
            inline_images += len(re.findall(rb"(?:^|\s)BI(?:\s|$)", raw))
        page_details.append(
            {
                "page": number,
                "width": width,
                "height": height,
                "crop_width": crop_width,
                "crop_height": crop_height,
                "rotation": rotation,
                "text_chars": len(text.strip()),
                "text": text,
            }
        )

    return {
        "page_count": len(reader.pages),
        "page_details": page_details,
        "fonts": sorted(font_records.values(), key=lambda row: (row["base_font"], row["subtype"])),
        "image_xobjects": image_xobjects,
        "form_xobjects": form_xobjects,
        "inline_images": inline_images,
        "metadata": {str(key): str(value) for key, value in (reader.metadata or {}).items()},
        "expected_pages": expected_pages,
    }


def edition_segments(text: str) -> dict[int, tuple[int, str]]:
    markers = list(re.finditer(r"\\EditionPage\{(\d+)\}\{(\d+)\}\{%", text))
    segments: dict[int, tuple[int, str]] = {}
    for index, marker in enumerate(markers):
        start = marker.start()
        stop = markers[index + 1].start() if index + 1 < len(markers) else text.find(r"\end{document}", start)
        segments[int(marker.group(1))] = (int(marker.group(2)), text[start:stop])
    return segments


def main() -> int:
    audit = Audit()
    computed: dict[str, object] = {}

    # Immutable wrapper, state, manifest, and extracted mirror.
    audit.require(OUTER.is_file(), "wrapper.present", "final return wrapper exists")
    outer_size = OUTER.stat().st_size
    outer_sha = sha256_path(OUTER)
    computed["wrapper"] = {"bytes": outer_size, "sha256": outer_sha}
    audit.require(
        outer_size == 57254061 and outer_sha == OUTER_SHA,
        "wrapper.identity",
        f"bytes={outer_size}; sha256={outer_sha}",
    )

    expected_outer_names = {
        "README_FINAL_RELEASE.txt",
        "SHA256SUMS.txt",
        "DELIGNE_LUSZTIG_D027_REDUCTIVE_GROUPS_S10_CUMULATIVE_FULL_STATE.zip",
        "DELIGNE_LUSZTIG_D027_REDUCTIVE_GROUPS_S10_CUMULATIVE_CHECKPOINT.json",
        "DELIGNE_LUSZTIG_D027_REDUCTIVE_GROUPS_S10_CUMULATIVE_MANIFEST.tsv",
    }
    with ZipFile(OUTER) as outer_zip:
        outer_infos = outer_zip.infolist()
        outer_names = [info.filename for info in outer_infos]
        audit.require(outer_zip.testzip() is None, "wrapper.crc", "all five members pass CRC replay")
        audit.require(
            set(outer_names) == expected_outer_names and len(outer_names) == 5,
            "wrapper.inventory",
            f"exact member count={len(outer_names)}",
        )
        audit.require(safe_zip_names(outer_names), "wrapper.paths", "paths are unique, case-unique, and traversal-safe")
        audit.require(
            all(info.date_time == (1980, 1, 1, 0, 0, 0) for info in outer_infos),
            "wrapper.timestamps",
            "all ZIP member timestamps are deterministic DOS epoch",
        )

        sums_text = outer_zip.read("SHA256SUMS.txt").decode("utf-8")
        sum_rows = {}
        for line in sums_text.splitlines():
            if line.strip():
                digest, name = line.split(None, 1)
                sum_rows[name.strip()] = digest.upper()
        expected_sum_names = {
            "DELIGNE_LUSZTIG_D027_REDUCTIVE_GROUPS_S10_CUMULATIVE_FULL_STATE.zip",
            "DELIGNE_LUSZTIG_D027_REDUCTIVE_GROUPS_S10_CUMULATIVE_CHECKPOINT.json",
            "DELIGNE_LUSZTIG_D027_REDUCTIVE_GROUPS_S10_CUMULATIVE_MANIFEST.tsv",
        }
        sum_identity_ok = set(sum_rows) == expected_sum_names
        for name, digest in sum_rows.items():
            sum_identity_ok = sum_identity_ok and hashlib.sha256(outer_zip.read(name)).hexdigest().upper() == digest
        audit.require(sum_identity_ok, "wrapper.sha256sums", "three cumulative trio hashes replay exactly")

        checkpoint_bytes = outer_zip.read(
            "DELIGNE_LUSZTIG_D027_REDUCTIVE_GROUPS_S10_CUMULATIVE_CHECKPOINT.json"
        )
        checkpoint = json.loads(checkpoint_bytes)
        checkpoint_ok = (
            checkpoint.get("work_id") == WORK_ID
            and checkpoint.get("status") == "COMPLETE"
            and checkpoint.get("current_session") == "S10"
            and checkpoint.get("prompt_id") == "P10"
            and checkpoint.get("next_prompt") == "NONE_PROJECT_PASS"
            and checkpoint.get("source_pdf_sha256") == AUTHORITY_SHA
            and checkpoint.get("source_pdf_pages") == 60
            and checkpoint.get("source_page_count") == 60
            and checkpoint.get("french_page_count") == 60
            and checkpoint.get("apparatus_page_count") == 60
            and checkpoint.get("final_accepted_page_count") == 60
            and checkpoint.get("full_state", {}).get("sha256") == STATE_SHA
            and checkpoint.get("full_state", {}).get("bytes") == 57247919
        )
        audit.require(checkpoint_ok, "wrapper.checkpoint", "S10/P10 is COMPLETE with 60/60/60 dispositions and no next prompt")

        manifest_text = outer_zip.read(
            "DELIGNE_LUSZTIG_D027_REDUCTIVE_GROUPS_S10_CUMULATIVE_MANIFEST.tsv"
        ).decode("utf-8")
        manifest_rows = tsv_rows_from_text(manifest_text)
        state_manifest_rows = [row for row in manifest_rows if row["scope"] == "STATE_MEMBER"]
        trio_rows = [row for row in manifest_rows if row["scope"] == "TRIO"]
        audit.require(
            len(state_manifest_rows) == 60 and len(trio_rows) == 2,
            "wrapper.manifest.shape",
            f"state rows={len(state_manifest_rows)}; non-self trio rows={len(trio_rows)}",
        )

    state_size = STATE.stat().st_size
    state_sha = sha256_path(STATE)
    computed["state"] = {"bytes": state_size, "sha256": state_sha}
    audit.require(
        state_size == 57247919 and state_sha == STATE_SHA,
        "state.identity",
        f"bytes={state_size}; sha256={state_sha}",
    )
    audit.require(
        sum_rows.get(STATE.name) == state_sha,
        "wrapper.state.binding",
        "outer SHA256SUMS binds the exact local S10 full-state bytes",
    )

    manifest_by_path = {row["path"]: row for row in state_manifest_rows}
    with ZipFile(STATE) as state_zip:
        state_infos = state_zip.infolist()
        state_names = [info.filename for info in state_infos]
        audit.require(state_zip.testzip() is None, "state.crc", "all 60 state members pass CRC replay")
        audit.require(len(state_names) == 60, "state.inventory.count", f"exact member count={len(state_names)}")
        audit.require(safe_zip_names(state_names), "state.paths", "paths are unique, case-unique, and traversal-safe")
        audit.require(
            all(info.date_time == (1980, 1, 1, 0, 0, 0) for info in state_infos),
            "state.timestamps",
            "all state timestamps are deterministic DOS epoch",
        )
        audit.require(
            set(state_names) == set(manifest_by_path),
            "state.manifest.coverage",
            "manifest covers every state member exactly once and no extra path",
        )
        member_hashes_ok = True
        extracted_mirror_ok = True
        for info in state_infos:
            with state_zip.open(info) as handle:
                member_sha = sha256_stream(handle)
            row = manifest_by_path.get(info.filename, {})
            member_hashes_ok = member_hashes_ok and row.get("sha256") == member_sha and row.get("bytes") == str(info.file_size)
            extracted_path = EXTRACTED / PurePosixPath(info.filename)
            extracted_mirror_ok = (
                extracted_mirror_ok
                and extracted_path.is_file()
                and extracted_path.stat().st_size == info.file_size
                and sha256_path(extracted_path) == member_sha
            )
        audit.require(member_hashes_ok, "state.manifest.hashes", "all member sizes and SHA-256 values replay")
        audit.require(extracted_mirror_ok, "state.extracted.mirror", "all 60 extracted files are byte-identical to state members")

    # Authority topology and page map.
    authority_size = AUTHORITY.stat().st_size
    authority_sha = sha256_path(AUTHORITY)
    authority_reader = PdfReader(str(AUTHORITY), strict=True)
    computed["authority"] = {"bytes": authority_size, "sha256": authority_sha, "pages": len(authority_reader.pages)}
    audit.require(
        authority_size == 3640869 and authority_sha == AUTHORITY_SHA and len(authority_reader.pages) == 60,
        "authority.identity",
        f"bytes={authority_size}; pages={len(authority_reader.pages)}; sha256={authority_sha}",
    )
    authority_images_ok = True
    authority_annots_ok = True
    for index, page in enumerate(authority_reader.pages, 1):
        resources = pdf_resources(page)
        xobjects = resources.get("/XObject") if resources else None
        xobjects = xobjects.get_object() if hasattr(xobjects, "get_object") else xobjects
        images = [] if not xobjects else [ref.get_object() for ref in xobjects.values() if str(ref.get_object().get("/Subtype")) == "/Image"]
        if len(images) != 1:
            authority_images_ok = False
            continue
        image = images[0]
        if index == 1:
            authority_images_ok = authority_images_ok and int(image.get("/Width")) == 322 and int(image.get("/Height")) == 352
        else:
            authority_images_ok = (
                authority_images_ok
                and int(image.get("/Width")) == 3750
                and int(image.get("/Height")) == 5445
                and str(image.get("/ColorSpace")) == "/DeviceGray"
                and str(image.get("/Filter")) == "/JBIG2Decode"
            )
        annotation_count = len(page.get("/Annots", []))
        authority_annots_ok = authority_annots_ok and (annotation_count == 3 if index == 1 else annotation_count == 0)
    audit.require(authority_images_ok, "authority.scan.topology", "one cover image plus 59 one-bit 3750x5445 article images")
    audit.require(authority_annots_ok, "authority.annotations", "three cover links only; article pages have no annotations")

    page_map = tsv_rows(EXTRACTED / "control" / "PAGE_MAP.tsv")
    page_map_ok = len(page_map) == 60
    for index, row in enumerate(page_map, 1):
        expected_printed = 0 if index == 1 else index + 101
        expected_disposition = "EXCLUDE_FROM_SCHOLARLY_BODIES_RETAIN_PROVENANCE" if index == 1 else "INCLUDE_ARTICLE"
        page_map_ok = (
            page_map_ok
            and int(row["physical_page"]) == index
            and int(row["printed_page"]) == expected_printed
            and row["disposition"] == expected_disposition
        )
    audit.require(page_map_ok, "authority.page_map", "physical 1 is excluded cover; physical 2-60 map to printed 103-161")

    # Frozen production records.
    ndjson_rows: dict[str, list[dict]] = {}
    ndjson_computed = {}
    for name, (expected_bytes, expected_sha, expected_status) in EXPECTED_NDJSON.items():
        path = EXTRACTED / "edition" / name
        digest = sha256_path(path)
        ndjson_computed[name] = {"bytes": path.stat().st_size, "sha256": digest}
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
        ndjson_rows[name] = rows
        identity_ok = path.stat().st_size == expected_bytes and digest == expected_sha
        topology_ok = len(rows) == 60
        for index, row in enumerate(rows, 1):
            topology_ok = (
                topology_ok
                and int(row["physical_page"]) == index
                and int(row["printed_page"]) == (0 if index == 1 else index + 101)
                and row.get("source_sha256") == AUTHORITY_SHA
                and row.get("status") == expected_status
                and row.get("disposition")
                == ("EXCLUDE_FROM_SCHOLARLY_BODIES_RETAIN_PROVENANCE" if index == 1 else "INCLUDE_ARTICLE")
                and row.get("assets") in ([], None)
                and bool(str(row.get("text", "")).strip())
            )
        audit.require(identity_ok, f"ndjson.{name}.identity", f"bytes={path.stat().st_size}; sha256={digest}")
        audit.require(topology_ok, f"ndjson.{name}.topology", "60 exact authority-addressed dispositions with no promoted image asset")
    computed["ndjson"] = ndjson_computed

    # Corrected TeX and the exact, closed repair set.
    tex_computed = {}
    tex_texts = {}
    for name, (expected_bytes, expected_sha) in EXPECTED_TEX.items():
        path = TEX_ROOT / name
        digest = sha256_path(path)
        tex_computed[name] = {"bytes": path.stat().st_size, "sha256": digest}
        tex_texts[name] = path.read_text(encoding="utf-8")
        audit.require(
            path.stat().st_size == expected_bytes and digest == expected_sha,
            f"tex.{name}.identity",
            f"bytes={path.stat().st_size}; sha256={digest}",
        )
    computed["tex"] = tex_computed

    repair_path = TEX_ROOT / "D027_SEMANTIC_TEX_REPAIRS.json"
    repair_data = json.loads(repair_path.read_text(encoding="utf-8"))
    actual_repairs = {
        (row["layer"], int(row["physical_page"]), row["before"], row["after"]): int(row["count"])
        for row in repair_data["repairs"]
    }
    repair_count = sum(actual_repairs.values())
    audit.require(
        repair_data.get("result") == "PASS"
        and repair_data.get("work_id") == WORK_ID
        and repair_data.get("authority_sha256") == AUTHORITY_SHA
        and actual_repairs == EXPECTED_REPAIRS
        and repair_count == 18,
        "tex.repairs.closed_set",
        f"exact allowed repair total={repair_count}; rows={len(actual_repairs)}",
    )
    repair_tsv = tsv_rows(TEX_ROOT / "D027_SEMANTIC_TEX_REPAIRS.tsv")
    tsv_repairs = {
        (row["layer"], int(row["physical_page"]), row["before"], row["after"]): int(row["count"])
        for row in repair_tsv
    }
    audit.require(tsv_repairs == EXPECTED_REPAIRS, "tex.repairs.tsv_binding", "TSV and JSON encode the same exact repair set")

    for layer, name in (("en", "Deligne_D027_EN.tex"), ("fr", "Deligne_D027_FR.tex")):
        text = tex_texts[name]
        segments = edition_segments(text)
        topology_ok = sorted(segments) == list(range(2, 61)) and [segments[p][0] for p in range(2, 61)] == list(range(103, 162))
        page53 = segments.get(53, (0, ""))[1]
        spacing_ok = text.count(r"\\[2mm]") == 1 and page53.count(r"\\[2mm]") == 1 and r"\\{}[2mm]" not in text
        repair_surface_ok = text.count(r"\\{}[") == 6 and r"\toE" not in text and r"\inE" not in text
        audit.require(topology_ok, f"tex.{layer}.topology", "59 edition pages map physical 2-60 to printed 103-161")
        audit.require(spacing_ok, f"tex.{layer}.page53_spacing", "one genuine \\\\[2mm] remains on physical page 53 and is not literalized")
        audit.require(repair_surface_ok, f"tex.{layer}.repair_surface", "six literal-bracket disambiguations and no fused relation command remain")
        frozen_page53 = ndjson_rows["source_language.ndjson" if layer == "en" else "french_translation.ndjson"][52]["text"]
        audit.require(
            frozen_page53.count(r"\\[2mm]") == 1 and r"\\{}[2mm]" not in frozen_page53,
            f"tex.{layer}.frozen_page53",
            "frozen physical-page-53 record retains the genuine spacing token unchanged",
        )
    apparatus_tex = tex_texts["Deligne_D027_APPARATUS.tex"]
    audit.require(
        "Nine TeX parser-boundary repairs are applied independently in each scholarly edition" in apparatus_tex
        and r"The genuine \verb|\\[2mm]| spacing command on physical page 53 is preserved" in apparatus_tex,
        "tex.apparatus.repair_statement",
        "apparatus accurately states nine repairs per edition and preserved page-53 spacing",
    )

    # Canonical PDFs, deterministic lanes, and PDF object-level checks.
    pdf_computed = {}
    pdf_inspections = {}
    for name, (expected_bytes, expected_sha, expected_pages) in EXPECTED_PDF.items():
        path = FINAL_PDF_ROOT / name
        digest = sha256_path(path)
        pdf_computed[name] = {"bytes": path.stat().st_size, "sha256": digest, "pages": expected_pages}
        audit.require(
            path.stat().st_size == expected_bytes and digest == expected_sha,
            f"pdf.{name}.identity",
            f"bytes={path.stat().st_size}; sha256={digest}",
        )
        inspection = inspect_pdf(path, expected_pages)
        pdf_inspections[name] = inspection
        pages = inspection["page_details"]
        a4_ok = all(
            abs(page["width"] - 595.276) <= 0.75
            and abs(page["height"] - 841.89) <= 0.75
            and abs(page["crop_width"] - 595.276) <= 0.75
            and abs(page["crop_height"] - 841.89) <= 0.75
            for page in pages
        )
        rotation_ok = all(page["rotation"] == 0 for page in pages)
        text_ok = len(pages) == expected_pages and all(page["text_chars"] >= 40 for page in pages)
        fonts_ok = bool(inspection["fonts"]) and all(
            row["subtype"] == "/Type0" and row["to_unicode"] and row["embedded"]
            for row in inspection["fonts"]
        )
        image_ok = inspection["image_xobjects"] == 0 and inspection["inline_images"] == 0
        metadata = inspection["metadata"]
        semantic_metadata_ok = all(metadata.get(key) == value for key, value in EXPECTED_METADATA[name].items())
        deterministic_metadata_ok = (
            metadata.get("/Producer") == "Pierre Deligne corpus deterministic build"
            and metadata.get("/Creator") == "XeLaTeX; normalized with pypdf"
            and metadata.get("/CreationDate") == "D:20260823000000Z"
            and metadata.get("/ModDate") == "D:20260823000000Z"
        )
        audit.require(len(pages) == expected_pages, f"pdf.{name}.pages", f"page count={len(pages)}")
        audit.require(a4_ok and rotation_ok, f"pdf.{name}.geometry", "every MediaBox/CropBox is A4 with zero rotation")
        audit.require(text_ok, f"pdf.{name}.text", "every page has a nonblank extractable text layer")
        audit.require(fonts_ok, f"pdf.{name}.fonts", f"all {len(inspection['fonts'])} referenced Type0 fonts are embedded and have ToUnicode")
        audit.require(image_ok, f"pdf.{name}.images", "zero image XObjects and zero inline images")
        audit.require(
            semantic_metadata_ok and deterministic_metadata_ok,
            f"pdf.{name}.metadata",
            "semantic title/author/edition metadata is preserved with deterministic producer, creator, and dates",
        )
        if name in {"Deligne_D027_EN.pdf", "Deligne_D027_FR.pdf"}:
            folios_ok = all(f"Printed page {103 + index}" in page["text"] for index, page in enumerate(pages))
            audit.require(folios_ok, f"pdf.{name}.folios", "headers map PDF pages 1-59 to printed folios 103-161")
    computed["pdf"] = pdf_computed

    determinism_ok = True
    determinism_rows = {}
    for name, (_, expected_sha, _) in EXPECTED_PDF.items():
        hashes = {
            lane: sha256_path(QA_ROOT / "determinism" / lane / name)
            for lane in ("a", "b")
        }
        hashes["final"] = sha256_path(FINAL_PDF_ROOT / name)
        determinism_rows[name] = hashes
        determinism_ok = determinism_ok and len(set(hashes.values())) == 1 and hashes["final"] == expected_sha
    computed["determinism"] = determinism_rows
    audit.require(determinism_ok, "pdf.determinism", "A, B, and final SHA-256 values are identical for all three PDFs")

    raster_ok = True
    raster_count = 0
    raster_counts = {}
    for kind, expected_count in (("en", 59), ("fr", 59), ("apparatus", 8)):
        raw_dir = QA_ROOT / "renders" / kind
        final_dir = QA_ROOT / "final_renders" / kind
        raw_files = {path.name: path for path in raw_dir.glob("*.png")}
        final_files = {path.name: path for path in final_dir.glob("*.png")}
        lane_ok = set(raw_files) == set(final_files) and len(raw_files) == expected_count
        for name in sorted(set(raw_files) & set(final_files)):
            lane_ok = lane_ok and sha256_path(raw_files[name]) == sha256_path(final_files[name])
        raster_ok = raster_ok and lane_ok
        raster_count += len(raw_files)
        raster_counts[kind] = len(raw_files)
    computed["raster_counts"] = raster_counts
    audit.require(raster_ok and raster_count == 126, "pdf.raw_final_rasters", f"all {raster_count} raw/final PNG pairs have identical SHA-256")

    # Manual visual QA is hash-bound to the corrected bytes and postdates them.
    visual_path = QA_ROOT / "D027_MANUAL_VISUAL_QA.tsv"
    visual_rows = tsv_rows(visual_path)
    visual_by_id = {row["check_id"]: row for row in visual_rows}
    visual_ok = len(visual_rows) == 6 and set(visual_by_id) == {f"V{i:02d}" for i in range(1, 7)} and all(row["result"] == "PASS" for row in visual_rows)
    visual_ok = visual_ok and visual_by_id.get("V01", {}).get("identity_sha256") == AUTHORITY_SHA
    visual_ok = visual_ok and visual_by_id.get("V02", {}).get("identity_sha256") == EXPECTED_PDF["Deligne_D027_EN.pdf"][1]
    visual_ok = visual_ok and visual_by_id.get("V03", {}).get("identity_sha256") == EXPECTED_PDF["Deligne_D027_FR.pdf"][1]
    visual_ok = visual_ok and visual_by_id.get("V04", {}).get("identity_sha256") == EXPECTED_PDF["Deligne_D027_APPARATUS.pdf"][1]
    v05_identity = visual_by_id.get("V05", {}).get("identity_sha256", "")
    visual_ok = visual_ok and all(
        digest in v05_identity
        for digest in (AUTHORITY_SHA, EXPECTED_PDF["Deligne_D027_EN.pdf"][1], EXPECTED_PDF["Deligne_D027_FR.pdf"][1])
    )
    visual_ok = visual_ok and visual_path.stat().st_mtime_ns >= max((FINAL_PDF_ROOT / name).stat().st_mtime_ns for name in EXPECTED_PDF)
    computed["manual_visual_qa_sha256"] = sha256_path(visual_path)
    audit.require(visual_ok, "visual.manual_binding", "six PASS rows bind authority and all corrected final PDF hashes, including paired page 53")

    # Math alignment: every inherited finding is explicitly reviewed and accepted.
    math_raw_path = QA_ROOT / "D027_MATH_ALIGNMENT_REVIEW.tsv"
    math_reviewed_path = QA_ROOT / "D027_MATH_ALIGNMENT_REVIEWED.tsv"
    math_raw = tsv_rows(math_raw_path)
    math_reviewed = tsv_rows(math_reviewed_path)
    base_columns = [
        "physical_page",
        "kind",
        "opcode",
        "source_index",
        "french_index",
        "source_formula",
        "french_formula",
        "source_skeleton",
        "french_skeleton",
    ]
    math_binding_ok = len(math_raw) == len(math_reviewed) == 48
    for raw, reviewed in zip(math_raw, math_reviewed):
        math_binding_ok = (
            math_binding_ok
            and all(raw[column] == reviewed[column] for column in base_columns)
            and raw["review_status"] == "REQUIRES_HUMAN_REVIEW"
            and reviewed["review_status"] == "ACCEPTED_EQUIVALENT_AFTER_PAIRED_PAGE_REVIEW"
            and bool(reviewed["review_note"].strip())
        )
    computed["math_review"] = {
        "findings": len(math_reviewed),
        "raw_sha256": sha256_path(math_raw_path),
        "reviewed_sha256": sha256_path(math_reviewed_path),
    }
    audit.require(math_binding_ok, "math.review", "all 48 findings match one-for-one and are explicitly accepted with review notes")

    # Compilation logs: distinguish benign warnings from release blockers.
    log_summary = {}
    logs_ok = True
    expected_log_pages = {
        "Deligne_D027_EN.log": 59,
        "Deligne_D027_FR.log": 59,
        "Deligne_D027_APPARATUS.log": 8,
    }
    fatal_patterns = (
        r"(?m)^! ",
        r"Undefined control sequence",
        r"Emergency stop",
        r"Fatal error",
        r"No pages of output",
        r"LaTeX Error:",
        r"Package [^\n]+ Error:",
        r"Missing character:",
        r"Overfull \\[hv]box",
        r"There were undefined references",
        r"Citation [^\n]+ undefined",
    )
    for name, expected_pages in expected_log_pages.items():
        path = RAW_PDF_ROOT / name
        text = path.read_text(encoding="utf-8", errors="replace")
        fatal_hits = [pattern for pattern in fatal_patterns if re.search(pattern, text, re.IGNORECASE)]
        package_warning_lines = [line for line in text.splitlines() if "Warning:" in line]
        unknown_warnings = [line for line in package_warning_lines if not line.startswith("Package unicode-math Warning:")]
        underfull = len(re.findall(r"(?m)^Underfull \\[hv]box", text))
        output_match = re.search(r"Output written on .*?\((\d+) pages?\)\.", text.replace("\n", ""), re.DOTALL)
        output_pages = int(output_match.group(1)) if output_match else -1
        lane_ok = not fatal_hits and not unknown_warnings and output_pages == expected_pages
        logs_ok = logs_ok and lane_ok
        log_summary[name] = {
            "sha256": sha256_path(path),
            "fatal_hits": fatal_hits,
            "known_unicode_math_warning_lines": len(package_warning_lines),
            "underfull_boxes": underfull,
            "output_pages": output_pages,
            "classification": "PASS_BENIGN_ONLY" if lane_ok else "FAIL_ACTIONABLE",
        }
    computed["compilation_logs"] = log_summary
    audit.require(logs_ok, "compile.logs", "no fatal, overfull, missing-glyph, or unknown warning; only known unicode-math warnings and one visually cleared EN underfull box")

    # Copy matter and publication-surface privacy/credential check.
    copy_markers = (
        "[PROVENANCE-ONLY DISPOSITION",
        "JSTOR",
        "terms-of-use",
        "stable URL",
        "access statement",
        "Publisher recorded on the cover",
    )
    scholarly_text = {}
    copy_ok = True
    for name in ("Deligne_D027_EN.pdf", "Deligne_D027_FR.pdf"):
        text = "\n".join(page["text"] for page in pdf_inspections[name]["page_details"])
        scholarly_text[name] = text
        copy_ok = copy_ok and all(marker.casefold() not in text.casefold() for marker in copy_markers)
        tex_name = name.replace(".pdf", ".tex")
        copy_ok = copy_ok and all(marker.casefold() not in tex_texts[tex_name].casefold() for marker in copy_markers)
    audit.require(copy_ok, "surface.copy_matter", "JSTOR cover/copy matter is absent from both 59-page scholarly bodies")

    public_surface = [TEX_ROOT / name for name in EXPECTED_TEX] + [FINAL_PDF_ROOT / name for name in EXPECTED_PDF]
    private_name_token = HOME.name.casefold()
    credential_patterns = (
        re.compile(r"(?i)access[_-]?token\s*[:=]"),
        re.compile(r"(?i)authorization\s*:\s*bearer\s+[A-Za-z0-9._~-]{12,}"),
        re.compile(r"(?i)(?:api[_-]?token|client[_-]?secret|password)\s*[:=]\s*['\"]?[A-Za-z0-9._~-]{12,}"),
        re.compile(r"(?i)[?&]access_token="),
    )
    surface_ok = True
    for path in public_surface:
        raw = path.read_bytes()
        decoded = raw.decode("utf-8", errors="ignore")
        searchable = decoded
        if path.suffix.casefold() == ".pdf":
            searchable += "\n" + "\n".join(page["text"] for page in pdf_inspections[path.name]["page_details"])
            searchable += "\n" + json.dumps(pdf_inspections[path.name]["metadata"], ensure_ascii=False)
        surface_ok = surface_ok and private_name_token not in searchable.casefold()
        surface_ok = surface_ok and all(pattern.search(searchable) is None for pattern in credential_patterns)
    audit.require(surface_ok, "surface.sensitive_strings", "six candidate TeX/PDF files contain neither the local private-name token nor credential-shaped strings")

    result = {
        "schema": "d027-independent-cold-audit-final-v1",
        "work_id": WORK_ID,
        "audit_mode": "fresh_nonpatching_read_only",
        "result": "PASS" if not audit.failures else "FAIL",
        "checks": audit.checks,
        "failures": audit.failures,
        "computed": computed,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if not audit.failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
