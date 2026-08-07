from __future__ import annotations

import hashlib
import json
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
P2 = ROOT / "p2.pdf"
P3 = ROOT / "reader.pdf"
T2 = ROOT / "p2.txt"
T3 = ROOT / "reader.txt"


def ident(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {
        "path": path.name,
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest().upper(),
    }


def trailer_ids(reader: PdfReader) -> list[str]:
    values = reader.trailer.get("/ID") or []
    out: list[str] = []
    for value in values:
        raw = getattr(value, "original_bytes", None)
        out.append(raw.hex().upper() if raw is not None else str(value))
    return out


def page_signature(page: object) -> dict[str, object]:
    media = tuple(float(value) for value in page.mediabox)
    crop = tuple(float(value) for value in page.cropbox)
    annots = page.get("/Annots")
    if annots is None:
        annot_count = 0
    else:
        annots = annots.get_object()
        annot_count = len(annots)
    return {
        "media_box": media,
        "crop_box": crop,
        "rotate": int(page.get("/Rotate", 0)),
        "annotation_count": annot_count,
    }


def main() -> None:
    before = P2.read_bytes()
    after = P3.read_bytes()
    if len(before) != len(after):
        differing = []
    else:
        differing = [index for index, pair in enumerate(zip(before, after)) if pair[0] != pair[1]]

    regions: list[list[int]] = []
    if differing:
        start = previous = differing[0]
        for index in differing[1:]:
            if index != previous + 1:
                regions.append([start, previous])
                start = index
            previous = index
        regions.append([start, previous])

    readers = [PdfReader(str(P2)), PdfReader(str(P3))]
    content_hashes: list[list[str]] = []
    page_signatures: list[list[dict[str, object]]] = []
    for reader in readers:
        hashes: list[str] = []
        signatures: list[dict[str, object]] = []
        for page in reader.pages:
            contents = page.get_contents()
            payload = b"" if contents is None else contents.get_data()
            hashes.append(hashlib.sha256(payload).hexdigest().upper())
            signatures.append(page_signature(page))
        content_hashes.append(hashes)
        page_signatures.append(signatures)

    metadata = [dict(reader.metadata or {}) for reader in readers]
    common_metadata = {
        key: metadata[0][key]
        for key in metadata[0]
        if key in metadata[1] and metadata[0][key] == metadata[1][key]
    }
    metadata_differences = {
        key: [metadata[0].get(key), metadata[1].get(key)]
        for key in sorted(set(metadata[0]) | set(metadata[1]))
        if metadata[0].get(key) != metadata[1].get(key)
    }

    result = {
        "record_id": "ZHCHK-NOETHER-CUM-R5-PDFDIAG-001",
        "method": "serial byte comparison plus pypdf logical page-stream, geometry, annotation, metadata, trailer-ID, and pdftotext comparison",
        "pass2_pdf": ident(P2),
        "pass3_pdf": ident(P3),
        "same_file_size": len(before) == len(after),
        "raw_differing_byte_count": len(differing),
        "raw_differing_regions_zero_based_inclusive": regions,
        "page_counts": [len(readers[0].pages), len(readers[1].pages)],
        "page_content_stream_mismatches_one_based": [
            index
            for index, pair in enumerate(zip(content_hashes[0], content_hashes[1]), 1)
            if pair[0] != pair[1]
        ],
        "page_content_hash_list_sha256": [
            hashlib.sha256(("\n".join(values) + "\n").encode("ascii")).hexdigest().upper()
            for values in content_hashes
        ],
        "page_geometry_annotation_mismatches_one_based": [
            index
            for index, pair in enumerate(zip(page_signatures[0], page_signatures[1]), 1)
            if pair[0] != pair[1]
        ],
        "common_metadata": common_metadata,
        "metadata_differences": metadata_differences,
        "trailer_ids": [trailer_ids(readers[0]), trailer_ids(readers[1])],
        "pass2_text": ident(T2),
        "pass3_text": ident(T3),
        "extracted_text_byte_identical": T2.read_bytes() == T3.read_bytes(),
        "disposition": "TOOLING_ONLY_PDF_ID_AND_CREATIONDATE_VARIANCE",
        "deterministic_pdf_bytes_claimed": False,
        "content_equivalence_pass": (
            len(readers[0].pages) == len(readers[1].pages) == 424
            and content_hashes[0] == content_hashes[1]
            and page_signatures[0] == page_signatures[1]
            and T2.read_bytes() == T3.read_bytes()
            and set(metadata_differences) == {"/CreationDate"}
        ),
    }
    (ROOT / "pdfdiag.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    if not result["content_equivalence_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
