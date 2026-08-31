#!/usr/bin/env python3
"""Independent, packet-only integrity audit for the D038 S10 return.

This verifier deliberately ignores every inherited audit conclusion.  It
authenticates the named ZIP, its immutable extraction, the packet manifest,
the page/control topology, all canonical records, and all 58 authority-page
evidence chains directly from bytes.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import pathlib
import stat
import zipfile
from collections import Counter

from PIL import Image, ImageChops


PACKET_NAME = "DELIGNE_D038_CRISTAUX_CANONIQUES_S10_CUMULATIVE_FULL_STATE.zip"
PACKET_BYTES = 105_436_323
PACKET_SHA256 = "E4AD47A2F0A0BB17B1613167BB45F99819B8A0FD63845B3A58C7A7A05E6E7696"
PACKET_MEMBERS = 741
AUTHORITY_SHA256 = "07B0FEA2D9A674C6DD4894E1A97A617C5DDBB6BDC2CB190DDBBC8F7A77856FD0"
COMPARATOR_SHA256 = "23CC548768092A07BCC0EAAB1B876856FA52559D91A5F3FC2844A7C84F9C4502"
EXPECTED_PAGES = 58


def sha256_file(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_stream(stream) -> str:
    digest = hashlib.sha256()
    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
        digest.update(chunk)
    return digest.hexdigest().upper()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def canonical_record_hash(record: dict) -> str:
    payload = dict(record)
    payload.pop("record_sha256", None)
    encoded = json.dumps(
        payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return sha256_bytes(encoded)


def read_tsv(path: pathlib.Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def read_ndjson(path: pathlib.Path) -> list[dict]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def audit_zip(source_zip: pathlib.Path, copied_zip: pathlib.Path, packet_root: pathlib.Path) -> dict:
    for label, path in (("source", source_zip), ("copy", copied_zip)):
        require(path.is_file(), f"missing {label} packet: {path}")
        require(path.stat().st_size == PACKET_BYTES, f"{label} packet byte mismatch")
        require(sha256_file(path) == PACKET_SHA256, f"{label} packet SHA-256 mismatch")
    require(source_zip.read_bytes() == copied_zip.read_bytes(), "source/copy packet bytes differ")

    extracted_files = {
        path.relative_to(packet_root).as_posix(): path
        for path in packet_root.rglob("*")
        if path.is_file()
    }
    with zipfile.ZipFile(source_zip) as archive:
        infos = archive.infolist()
        require(len(infos) == PACKET_MEMBERS, "ZIP member-count mismatch")
        require(archive.testzip() is None, "ZIP CRC failure")
        names = [item.filename for item in infos]
        require(len(names) == len(set(names)), "duplicate exact ZIP member name")
        require(len(names) == len({name.casefold() for name in names}), "case-folded ZIP name collision")
        file_infos = []
        for item in infos:
            name = item.filename
            pure = pathlib.PurePosixPath(name)
            require(name and "\x00" not in name, f"invalid ZIP name: {name!r}")
            require(not pure.is_absolute(), f"absolute ZIP path: {name!r}")
            require(".." not in pure.parts, f"traversal ZIP path: {name!r}")
            require("\\" not in name and ":" not in pure.parts[0], f"nonportable ZIP path: {name!r}")
            require(not (item.flag_bits & 0x1), f"encrypted ZIP member: {name!r}")
            unix_mode = (item.external_attr >> 16) & 0xFFFF
            require(not stat.S_ISLNK(unix_mode), f"symlink ZIP member: {name!r}")
            if not item.is_dir():
                file_infos.append(item)
        archive_names = {item.filename for item in file_infos}
        require(archive_names == set(extracted_files), "ZIP/extraction path inventory mismatch")
        for item in file_infos:
            extracted = extracted_files[item.filename]
            require(extracted.stat().st_size == item.file_size, f"extracted size mismatch: {item.filename}")
            with archive.open(item) as stream:
                member_hash = sha256_stream(stream)
            require(member_hash == sha256_file(extracted), f"extracted byte mismatch: {item.filename}")

    manifest_rows = read_tsv(packet_root / "session_manifest.tsv")
    require(len(manifest_rows) == len(extracted_files) - 1, "packet manifest row count mismatch")
    manifest_paths = [row["path"] for row in manifest_rows]
    require(len(manifest_paths) == len(set(manifest_paths)), "duplicate packet manifest path")
    require(set(manifest_paths) == set(extracted_files) - {"session_manifest.tsv"}, "manifest inventory mismatch")
    for row in manifest_rows:
        path = extracted_files[row["path"]]
        require(int(row["bytes"]) == path.stat().st_size, f"manifest size mismatch: {row['path']}")
        require(row["sha256"] == sha256_file(path), f"manifest SHA-256 mismatch: {row['path']}")

    return {
        "source_path": str(source_zip),
        "copied_path": str(copied_zip),
        "bytes": PACKET_BYTES,
        "sha256": PACKET_SHA256,
        "zip_members": PACKET_MEMBERS,
        "zip_file_members": len(extracted_files),
        "safe_member_paths": True,
        "duplicate_member_names": 0,
        "casefold_name_collisions": 0,
        "encrypted_members": 0,
        "symlink_members": 0,
        "crc_status": "PASS",
        "source_copy_byte_identity": True,
        "extraction_byte_identity": True,
        "manifest_rows_verified": len(manifest_rows),
    }


def audit_primary_state(packet_root: pathlib.Path) -> dict:
    control = json.loads((packet_root / "controls/authority_contract.json").read_text(encoding="utf-8"))
    require(control["authority_sha256"] == AUTHORITY_SHA256, "authority identity mismatch")
    require(control["authority_pages"] == EXPECTED_PAGES, "authority page-count mismatch")
    require(control["comparator_sha256"] == COMPARATOR_SHA256, "comparator identity mismatch")
    require(control["comparator_pages"] == EXPECTED_PAGES, "comparator page-count mismatch")
    require(control["comparator_role"] == "COMPARISON_ONLY", "comparator role mismatch")
    require(control["prior_acceptance"] == "ZERO_ACCEPTED", "inherited acceptance boundary mismatch")

    page_map = read_tsv(packet_root / "controls/page_map.tsv")
    coverage = read_tsv(packet_root / "state/coverage.tsv")
    require(len(page_map) == EXPECTED_PAGES, "page-map row count mismatch")
    require(len(coverage) == EXPECTED_PAGES, "coverage row count mismatch")

    source = read_ndjson(packet_root / "edition/source_language.ndjson")
    english = read_ndjson(packet_root / "edition/english_standalone.ndjson")
    apparatus = read_ndjson(packet_root / "edition/apparatus.ndjson")
    require(len(source) == len(english) == len(apparatus) == EXPECTED_PAGES, "edition row count mismatch")
    by_layer = {"source": source, "english": english, "apparatus": apparatus}
    for layer, rows in by_layer.items():
        require([int(row["physical_page"]) for row in rows] == list(range(1, 59)), f"{layer} topology mismatch")
        for page, row in enumerate(rows, 1):
            require(row["status"] == "COMPLETE", f"incomplete {layer} page {page}")
            require(int(row["printed_page"]) == page + 79, f"printed-page mismatch: {layer} {page}")
            require(canonical_record_hash(row) == row["record_sha256"], f"record hash mismatch: {layer} {page}")

    image_modes: Counter[str] = Counter()
    copy_exclusions: Counter[str] = Counter()
    authority_evidence_hashes: list[str] = []
    pixel_hashes: list[str] = []
    for page in range(1, EXPECTED_PAGES + 1):
        map_row = page_map[page - 1]
        cov_row = coverage[page - 1]
        src = source[page - 1]
        eng = english[page - 1]
        app = apparatus[page - 1]
        expected_printed = page + 79
        expected_language = "FRENCH" if page <= 48 else "ENGLISH"
        expected_operation = "TRANSLATION_FROM_FRENCH" if page <= 48 else "SOURCE_ALREADY_ENGLISH_REPLAY"
        require(int(map_row["physical_page"]) == page, f"page-map physical mismatch: {page}")
        require(int(map_row["authority_pdf_page"]) == page, f"authority map mismatch: {page}")
        require(int(map_row["source_container_page"]) == page, f"source map mismatch: {page}")
        require(int(map_row["comparator_pdf_page"]) == page, f"comparator map mismatch: {page}")
        require(int(map_row["printed_page"]) == expected_printed, f"page-map printed mismatch: {page}")
        require(map_row["source_language_zone"].split("_")[0] == expected_language, f"language zone mismatch: {page}")
        require(int(cov_row["physical_page"]) == page and int(cov_row["printed_page"]) == expected_printed, f"coverage topology mismatch: {page}")
        require(src["source_language"] == expected_language, f"source language mismatch: {page}")
        require(eng["english_operation"] == expected_operation, f"English operation mismatch: {page}")
        require(cov_row["source_sha256"] == src["record_sha256"], f"coverage/source mismatch: {page}")
        require(cov_row["english_sha256"] == eng["record_sha256"], f"coverage/English mismatch: {page}")
        require(cov_row["apparatus_sha256"] == app["record_sha256"], f"coverage/apparatus mismatch: {page}")
        require(eng["source_record_sha256"] == src["record_sha256"], f"source-English link mismatch: {page}")
        require(app["source_record_sha256"] == src["record_sha256"], f"source-apparatus link mismatch: {page}")
        require(app["english_record_sha256"] == eng["record_sha256"], f"English-apparatus link mismatch: {page}")
        require(app["apparatus_scope"].startswith("RESTRAINED_PAGE_LOCAL"), f"apparatus scope mismatch: {page}")
        if page >= 49:
            require(src["text"] == eng["text"], f"already-English replay changed: {page}")

        evidence_path = packet_root / src["authority_evidence_path"]
        require(sha256_file(evidence_path) == src["authority_evidence_sha256"], f"authority evidence record mismatch: {page}")
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        require(evidence["physical_page"] == page and evidence["printed_page"] == expected_printed, f"authority evidence topology mismatch: {page}")
        require(evidence["authority_sha256"] == AUTHORITY_SHA256, f"authority chain mismatch: {page}")
        for path_key, hash_key in (
            ("content_stream_path", "content_stream_sha256"),
            ("decoded_tiff_path", "decoded_tiff_sha256"),
            ("presentation_png_path", "presentation_png_sha256"),
            ("raw_ccitt_path", "raw_ccitt_sha256"),
            ("raw_params_path", "raw_params_sha256"),
        ):
            item_path = packet_root / evidence[path_key]
            require(item_path.is_file(), f"missing authority evidence member: {page} {path_key}")
            require(sha256_file(item_path) == evidence[hash_key], f"authority evidence hash mismatch: {page} {path_key}")
        png_path = packet_root / evidence["presentation_png_path"]
        tif_path = packet_root / evidence["decoded_tiff_path"]
        require(src["facsimile_path"] == evidence["presentation_png_path"], f"source/evidence image path mismatch: {page}")
        require(src["facsimile_sha256"] == evidence["presentation_png_sha256"], f"source/evidence image hash mismatch: {page}")
        with Image.open(png_path) as png, Image.open(tif_path) as tif:
            png.load()
            tif.load()
            require(png.size == tif.size == (1920, 2850), f"authority image dimensions mismatch: {page}")
            png_one = png.convert("1")
            tif_one = tif.convert("1")
            require(ImageChops.difference(png_one, tif_one).getbbox() is None, f"authority PNG/TIFF pixel mismatch: {page}")
            pixel_hash = sha256_bytes(png_one.tobytes())
            require(pixel_hash == evidence["pixel_sha256"], f"authority pixel hash mismatch: {page}")
            image_modes[png.mode] += 1
            pixel_hashes.append(pixel_hash)
        reader_asset = packet_root / f"rendered_readers/assets/p{page:03d}.png"
        require(sha256_file(reader_asset) == evidence["presentation_png_sha256"], f"reader asset changed: {page}")
        authority_evidence_hashes.append(src["authority_evidence_sha256"])

        excluded = src.get("copy_matter_excluded_from_text", [])
        copy_exclusions.update(excluded)
        if page not in (1, 49):
            require(excluded == ["PRINTED_FOLIO"], f"copy-matter disposition mismatch: {page}")
            standalone_lines = {line.strip() for line in src["text"].splitlines()}
            require(str(expected_printed) not in standalone_lines, f"printed folio entered source prose: {page}")
            standalone_english = {line.strip() for line in eng["text"].splitlines()}
            require(str(expected_printed) not in standalone_english, f"printed folio entered English prose: {page}")
        else:
            require(excluded == [], f"unexpected page-one/boundary exclusion: {page}")

    literals = {
        "source_p001_title": (source[0]["text"], "CRISTAUX ORDINAIRES ET COORDONNÉES CANONIQUES"),
        "source_p001_byline": (source[0]["text"], "par P. DELIGNE"),
        "source_p001_credit": (source[0]["text"], "avec la collaboration de L. ILLUSIE (*)"),
        "english_p001_title": (english[0]["text"], "ORDINARY CRYSTALS AND CANONICAL COORDINATES"),
        "boundary_p049_title": (source[48]["text"], "APPENDIX TO EXPOSE V"),
        "boundary_p049_author": (source[48]["text"], "Nicholas M. Katz"),
        "p055_missing_pullback_star": (source[54]["text"], "Φ_can(q_{ij}^(σ)) = (q_{ij})ᵖ"),
        "p057_repeated_fil2_left_operand": (source[56]["text"], "F(Φ_can)Φ_can*((Fil²)^(σ)) ⊂ Fil¹"),
        "p058_pullback_star": (source[57]["text"], "Φ_can*(q_i^(σ)) = (q_i)ᵖ"),
        "p058_qed": (source[57]["text"], "Q.E.D."),
        "p048_deligne_address": (source[47]["text"], "P. DELIGNE"),
        "p048_illusie_address": (source[47]["text"], "L. ILLUSIE"),
    }
    for label, (haystack, needle) in literals.items():
        require(needle in haystack, f"missing high-risk literal: {label}")

    combined_text = "\n".join(row["text"] for row in source + english)
    forbidden_copy_needles = (
        "NUMDAM",
        "Downloaded from",
        "digitized by",
        "Bibliothèque nationale de France",
    )
    for needle in forbidden_copy_needles:
        require(needle.casefold() not in combined_text.casefold(), f"scanner/library copy matter entered prose: {needle}")

    return {
        "authority": {
            "sha256": AUTHORITY_SHA256,
            "role": "CONTROLLING_AUTHORITY",
            "pages": EXPECTED_PAGES,
            "page_evidence_records_verified": len(authority_evidence_hashes),
            "png_tiff_pixel_identical_pages": len(pixel_hashes),
            "pixel_dimensions": [1920, 2850],
            "pixel_modes": dict(sorted(image_modes.items())),
            "aggregate_evidence_sha256": sha256_bytes("\n".join(authority_evidence_hashes).encode("ascii")),
            "aggregate_pixel_sha256": sha256_bytes("\n".join(pixel_hashes).encode("ascii")),
        },
        "comparator": {
            "sha256": COMPARATOR_SHA256,
            "role": "COMPARISON_ONLY",
            "accepted_bytes": 0,
        },
        "inherited_exact_work": "ZERO_ACCEPTED",
        "page_topology": {"physical": [1, 58], "printed": [80, 137], "count": 58},
        "source_language": {"FRENCH": 48, "ENGLISH_KATZ_SOURCE_REPLAY": 10},
        "edition_records_verified": {"source": 58, "english": 58, "apparatus": 58},
        "exact_english_replay_pages": 10,
        "apparatus_scope": "RESTRAINED_PAGE_LOCAL",
        "copy_matter": {
            "excluded_printed_folios": copy_exclusions["PRINTED_FOLIO"],
            "page_1_no_visible_folio": True,
            "page_49_no_visible_folio": True,
            "scanner_library_needles_found": 0,
        },
        "high_risk_literals_verified": sorted(literals),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=pathlib.Path)
    parser.add_argument("--source-zip", required=True, type=pathlib.Path)
    args = parser.parse_args()
    root = args.root.resolve()
    copied_zip = root / "input" / PACKET_NAME
    packet_root = root / "input/packet"
    result = {
        "schema": "d038-independent-packet-audit-v1",
        "status": "PASS",
        "method": "FRESH_BYTE_RECOMPUTATION_NO_INHERITED_AUDIT_CONCLUSIONS",
        "packet": audit_zip(args.source_zip.resolve(), copied_zip, packet_root),
        "primary_state": audit_primary_state(packet_root),
    }
    output = root / "state/PACKET_INTEGRITY.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print("PASS_PACKET_INTEGRITY")


if __name__ == "__main__":
    main()
