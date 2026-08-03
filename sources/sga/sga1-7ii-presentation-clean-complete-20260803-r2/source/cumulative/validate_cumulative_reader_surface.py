from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

from pypdf import PdfReader


FORBIDDEN_METADATA_TERMS = (
    "workpass",
    "working edition",
    "source status",
    "source-synchron",
    "machine-assisted",
    "PRIVATE_OPERATOR",
    "audit",
    "certif",
    "codex",
    "claude",
)
PRIVATE_BYTE_PATTERNS = (
    rb"PRIVATE_HOME",
    rb"private-home",
    rb"PRIVATE_HOME",
    rb"Documents" + rb"/interlanguage",
    rb"Documents" + rb"\\interlanguage",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def indirect_key(value: Any) -> tuple[int, int] | None:
    reference = getattr(value, "indirect_reference", None)
    if reference is None and hasattr(value, "idnum"):
        reference = value
    if reference is None:
        return None
    return int(reference.idnum), int(reference.generation)


def image_objects(reader: PdfReader) -> int:
    seen: set[tuple[int, int]] = set()
    images: set[tuple[int, int] | tuple[str, int]] = set()

    def walk_resources(resources_ref: Any, page_number: int) -> None:
        if resources_ref is None:
            return
        resources = resources_ref.get_object() if hasattr(resources_ref, "get_object") else resources_ref
        xobjects_ref = resources.get("/XObject") if resources else None
        if not xobjects_ref:
            return
        xobjects = xobjects_ref.get_object() if hasattr(xobjects_ref, "get_object") else xobjects_ref
        for name, object_ref in xobjects.items():
            key = indirect_key(object_ref)
            if key is not None and key in seen:
                continue
            if key is not None:
                seen.add(key)
            obj = object_ref.get_object()
            subtype = obj.get("/Subtype")
            if subtype == "/Image":
                images.add(key if key is not None else (str(name), page_number))
            elif subtype == "/Form":
                walk_resources(obj.get("/Resources"), page_number)

    for page_number, page in enumerate(reader.pages, 1):
        walk_resources(page.get("/Resources"), page_number)
    return len(images)


def parse_fonts(path: Path) -> dict[str, Any]:
    rows: list[list[str]] = []
    for line in path.read_text(encoding="utf-8-sig").splitlines()[2:]:
        if not line.strip():
            continue
        # `pdffonts` uses fixed-width columns, but the three yes/no columns
        # and the two object-id integers are separated by only one space.
        # Splitting solely on runs of two spaces therefore collapses those
        # five terminal fields and can silently report an empty inventory.
        match = re.match(
            r"^(.*?)\s{2,}(.*?)\s{2,}(\S+)\s+"
            r"(yes|no)\s+(yes|no)\s+(yes|no)\s+(\d+)\s+(\d+)$",
            line.strip(),
        )
        if match:
            rows.append(list(match.groups()))
    return {
        "path": str(path),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
        "rows": len(rows),
        "type3_rows": sum(1 for fields in rows if fields[1] == "Type 3"),
        "unembedded_rows": sum(1 for fields in rows if fields[3] != "yes"),
    }


def main() -> int:
    if len(sys.argv) != 7:
        print(
            "usage: validate_cumulative_reader_surface.py "
            "PDF FONTS.txt ROUTE.json CONTENT.json SURFACE.json OUTPUT.json",
            file=sys.stderr,
        )
        return 2
    pdf, font_path, route_path, content_path, surface_path, output = map(Path, sys.argv[1:])
    route = json.loads(route_path.read_text(encoding="utf-8-sig"))
    content = json.loads(content_path.read_text(encoding="utf-8-sig"))
    surface = json.loads(surface_path.read_text(encoding="utf-8-sig"))
    reader = PdfReader(str(pdf))
    metadata = {str(key): str(value) for key, value in (reader.metadata or {}).items()}
    metadata_text = " ".join(metadata.values()).lower()
    metadata_hits = {
        term: metadata_text.count(term) for term in FORBIDDEN_METADATA_TERMS
    }
    fonts = parse_fonts(font_path)
    images = image_objects(reader)
    raw = pdf.read_bytes()
    privacy_hits = {
        pattern.decode("ascii", errors="replace"): raw.count(pattern)
        for pattern in PRIVATE_BYTE_PATTERNS
    }
    checks = {
        "page_count_4177": len(reader.pages) == 4177,
        "route_validation_pass": route.get("status") == "PASS" and route.get("errors") == [],
        "content_validation_pass": content.get("status") == "PASS" and content.get("errors") == [],
        "surface_adjudication_pass": surface.get("status") == "PASS" and surface.get("errors") == [],
        "neutral_metadata": not any(metadata_hits.values()),
        "nonempty_font_inventory": fonts["rows"] > 0,
        "zero_type3_fonts": fonts["type3_rows"] == 0,
        "all_fonts_embedded": fonts["unembedded_rows"] == 0,
        "zero_image_objects": images == 0,
        "zero_private_path_bytes": not any(privacy_hits.values()),
    }
    errors = [name for name, passed in checks.items() if not passed]
    result = {
        "schema": "sga-global-reader-surface-validation-v1",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "checks": checks,
        "pdf": {
            "path": str(pdf),
            "bytes": pdf.stat().st_size,
            "sha256": sha256(pdf),
            "pages": len(reader.pages),
            "metadata": metadata,
            "forbidden_metadata_hits": metadata_hits,
            "image_objects": images,
            "private_path_byte_hits": privacy_hits,
        },
        "fonts": fonts,
        "bound_validations": {
            "route_sha256": sha256(route_path),
            "content_sha256": sha256(content_path),
            "surface_adjudication_sha256": sha256(surface_path),
        },
    }
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "errors": errors, "checks": checks}))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
