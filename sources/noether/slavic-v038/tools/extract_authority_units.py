#!/usr/bin/env python3
"""Extract the post-P43 units from the exact live Noether German authority.

The extractor is deliberately byte-oriented.  It preserves inherited mixed line
endings in each extracted unit and records both raw and LF-normalized identities.
It does not edit the German authority.
"""

from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[2] / "noether"
POINTER = PROJECT / "07_german_canon_control" / "CURRENT_GERMAN_AUTHORITY_POINTER.json"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def lf_normalize(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def find_exact(lines: list[str], text: str) -> int:
    matches = [index for index, line in enumerate(lines) if line.rstrip("\r\n") == text]
    if len(matches) != 1:
        raise RuntimeError(f"expected one exact marker {text!r}, found {len(matches)}")
    return matches[0]


def find_contains(lines: list[str], text: str) -> int:
    matches = [index for index, line in enumerate(lines) if text in line]
    if len(matches) != 1:
        raise RuntimeError(f"expected one containing marker {text!r}, found {len(matches)}")
    return matches[0]


def main() -> int:
    pointer_bytes = POINTER.read_bytes()
    pointer = json.loads(pointer_bytes.decode("utf-8-sig"))
    authority_info = pointer["default_translation_authority"]
    authority = Path(authority_info["path"])
    authority_bytes = authority.read_bytes()
    authority_hash = sha256(authority_bytes)
    if authority_hash != authority_info["raw_sha256"]:
        raise RuntimeError(
            f"live authority hash mismatch: {authority_hash} != {authority_info['raw_sha256']}"
        )

    raw_lines = authority_bytes.splitlines(keepends=True)
    text_lines = [line.decode("utf-8") for line in raw_lines]

    title_line = find_exact(text_lines, r"{\LARGE\bfseries Algebra der hyperkomplexen Größen\par}")
    book_start_candidates = [
        index
        for index in range(max(0, title_line - 30), title_line)
        if text_lines[index].rstrip("\r\n") == r"\begingroup"
    ]
    if not book_start_candidates:
        raise RuntimeError("could not locate book-opening begingroup")
    book_start = book_start_candidates[-1]

    section_markers = {
        1: "§ 1. Definition der direkten Darstellung",
        2: "§ 2. Darstellungsklassen",
        3: r"\(\S\) 3. Darstellungsmoduln",
        4: "§ 4. Der Zusammenhang zwischen Darstellungsmoduln und Darstellungen",
        5: "§ 5. Koeffizientenerweiterung hyperkomplexer Systeme",
        6: "§ 6. Die irreduziblen Darstellungen kommutativer Systeme",
        7: "§ 7. Die Isomorphismen eines Körpers",
        8: "§ 8. Der Zerfällungskörper",
        9: r"§ 9. Die Isomorphismen von \(Z_1\) auf die \(Z_i\)",
        10: "§ 10. Die Galoissche Gruppe",
        11: "§ 11. Der Hauptsatz der Galoisschen Theorie",
        12: r"§ 12. Die formale Bedeutung der Komponenten \(e_i\)",
        13: "§ 13. Der allgemeine Fortsetzungssatz",
        14: "§ 14. Der Gruppenring",
        15: "§ 15. Die Gruppenringe Abelscher Gruppen",
        16: "§ 16. Die Charakterenrelationen",
        17: "§ 17. Die Galoissche Theorie Abelscher Gruppen",
        18: "§ 18. Ein Hilfssatz",
        19: "§ 19. Darstellungen zweiseitig einfacher hyperkomplexer Systeme",
        20: "§ 20. Nichtkommutative Körper",
        21: "§ 21. Die Galoissche Theorie der nichtkommutativen Körper",
        22: "§ 22. Die Gruppe der Körper mit gegebenem Zentrum",
        23: "§ 23. Faktorensysteme",
        24: "§ 24. Multiplikation von Faktorensystemen",
        25: r"§ 25. Normaldarstellung von \(\mathfrak K_r\)",
        26: "§ 26. Multiplikation der verschränkten Darstellungen",
        27: r"§ 27. Darstellung der \(\mathfrak K_r\) als verschränkte Produkte",
        28: "§ 28. Produktsatz für Faktorensysteme",
        29: "§ 29. Hauptgeschlechtssatz im Minimalen",
        30: "§ 30. Spezialisierung auf zyklische Zerfällungskörper",
        31: "§ 31. Anwendungen des zyklischen Spezialfalles",
    }
    starts: dict[int, int] = {}
    for number, marker in section_markers.items():
        matches = [index for index, line in enumerate(text_lines) if marker in line]
        if len(matches) != 1:
            raise RuntimeError(f"section {number}: expected one marker, found {len(matches)}")
        starts[number] = matches[0]

    post45_matches = [
        index
        for index, line in enumerate(text_lines)
        if line.startswith(
            r"\subsection*{Notwendige und hinreichende Multiplizitätsbedingungen zum Noetherschen Fundamentalsatz"
        )
    ]
    if len(post45_matches) != 1:
        raise RuntimeError(f"expected one Post45 heading, found {len(post45_matches)}")
    post45_start = post45_matches[0]
    bibliography_title = find_exact(text_lines, r"{\Large\bfseries Bibliographie}")
    if text_lines[bibliography_title - 1].rstrip("\r\n") != r"\begin{center}":
        raise RuntimeError("bibliography start no longer preceded by begin{center}")
    postbib_start = bibliography_title - 1
    document_end = find_exact(text_lines, r"\end{document}")
    if text_lines[document_end - 1].rstrip("\r\n") != r"\endgroup":
        raise RuntimeError("book-closing endgroup not found immediately before end{document}")
    book_end = document_end - 1

    boundaries: list[tuple[str, int, int, str]] = []
    boundaries.append(("BOOK_TITLE_INTRO", book_start, starts[1], "book_title_intro"))
    for number in range(1, 32):
        start = starts[number]
        end = starts[number + 1] if number < 31 else post45_start
        boundaries.append((f"BOOK_S{number:02d}", start, end, "lecture_section"))
    boundaries.append(("POST45", post45_start, postbib_start, "kapferer_noether_item"))
    boundaries.append(("POSTBIB", postbib_start, book_end + 1, "bibliography_and_terminal_matter"))

    out_dir = ROOT / "authority_units"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, object]] = []
    for order, (unit_id, start, end, kind) in enumerate(boundaries, start=1):
        payload = b"".join(raw_lines[start:end])
        normalized = lf_normalize(payload)
        output = out_dir / f"{unit_id}.texfrag"
        output.write_bytes(payload)
        rows.append(
            {
                "unit_id": unit_id,
                "order": order,
                "kind": kind,
                "start_line": start + 1,
                "end_line": end,
                "raw_bytes": len(payload),
                "raw_sha256": sha256(payload),
                "lf_bytes": len(normalized),
                "lf_sha256": sha256(normalized),
                "output_path": output.as_posix(),
            }
        )

    if len(rows) != 34:
        raise RuntimeError(f"expected 34 extracted units, got {len(rows)}")
    if rows[0]["start_line"] != book_start + 1 or rows[-1]["end_line"] != book_end + 1:
        raise RuntimeError("coverage assertion failed")
    for previous, current in zip(rows, rows[1:]):
        if previous["end_line"] + 1 != current["start_line"]:
            raise RuntimeError(f"gap or overlap between {previous['unit_id']} and {current['unit_id']}")

    manifest = {
        "schema": "noether-slavic-v038-authority-unit-manifest/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "pointer": {
            "path": POINTER.as_posix(),
            "pointer_id": pointer["pointer_id"],
            "bytes": len(pointer_bytes),
            "sha256": sha256(pointer_bytes),
        },
        "authority": {
            "authority_id": authority_info["authority_id"],
            "path": authority.as_posix(),
            "bytes": len(authority_bytes),
            "sha256": authority_hash,
        },
        "scope": {
            "first_line": book_start + 1,
            "last_line": book_end + 1,
            "unit_count": len(rows),
            "coverage": "contiguous post-P43 book, Kapferer/Noether item, bibliography, and terminal matter; end{document} excluded",
        },
        "units": rows,
    }
    json_path = ROOT / "evidence" / "authority_units.json"
    json_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    csv_path = ROOT / "evidence" / "authority_units.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print(f"pointer={pointer['pointer_id']} {sha256(pointer_bytes)}")
    print(f"authority={authority_hash}")
    print(f"units={len(rows)} lines={book_start + 1}-{book_end + 1}")
    print(f"manifest={json_path} {sha256(json_path.read_bytes())}")
    print(f"csv={csv_path} {sha256(csv_path.read_bytes())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
