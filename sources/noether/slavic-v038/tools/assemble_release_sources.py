#!/usr/bin/env python3
"""Assemble source-current Slavic post-P43 components without touching lineage."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path

from transliterate_isv_cyrillic import transliterate_document


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parents[3]
ARCHIVE_R19 = WORKSPACE / "03_projects" / "noether" / "08_zenodo" / "r19"
TITLE_DIR = ROOT / "lineage" / "title_r823"
UNIT_DIR = ROOT / "translations" / "human_edited"
POST45_DIR = ROOT / "lineage" / "post45"
POSTBIB_DIR = ROOT / "lineage" / "postbib"
RELEASE_SOURCE = ROOT / "release" / "source"
EVIDENCE = ROOT / "release" / "evidence"

BASE_SOURCE_NAMES = {
    "ru": "20-ru.tex",
    "uk": "20-uk.tex",
    "isv": "20-isv-latn.tex",
    "isv-cy": "20-isv-cyrl.tex",
}

TITLE_PATCHES = {
    "ru": (
        r"\tocsec{25}{Нормальное представление $\mathfrak R_r$ с максимальным коммутативным подполем Галуа}{39}",
        r"\tocsec{25}{Нормальное представление $\mathfrak K_r$ с максимальными коммутативными подполями Галуа}{39}",
    ),
    "uk": (
        r"\tocsec{25}{Нормальне зображення $\mathfrak R_r$ з максимальним комутативним підполем Галуа}{39}",
        r"\tocsec{25}{Нормальне зображення $\mathfrak K_r$ з максимальними комутативними підполями Галуа}{39}",
    ),
    "isv": (
        r"\tocsec{25}{Normalno predstavjenje $\mathfrak R_r$ s Galoisovym maksimalnym komutativnym podpoljem}{39}",
        r"\tocsec{25}{Normalno predstavjenje $\mathfrak K_r$ s Galoisovymi maksimalnymi komutativnymi podpoljami}{39}",
    ),
}

PREAMBLE_ADDITION = r"""\usepackage{mathrsfs}
\newcommand{\srcfn}[2]{\footnote{#2}}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\allowdisplaybreaks
"""


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def file_record(path: Path, role: str, lineage: dict | None = None) -> dict:
    data = path.read_bytes()
    record = {
        "role": role,
        "path": path.resolve().as_posix(),
        "bytes": len(data),
        "sha256": sha256(data),
    }
    if lineage:
        record["lineage"] = lineage
    return record


def build_book(target: str) -> tuple[Path, list[dict]]:
    title = TITLE_DIR / f"{target}.tex"
    title_bytes = title.read_bytes()
    text = title_bytes.decode("utf-8-sig")
    old, new = TITLE_PATCHES[target]
    if text.count(old) != 1:
        raise RuntimeError(f"{title}: expected exactly one current-title patch locus")
    text = text.replace(old, new)
    if text.count(r"\end{document}") != 1:
        raise RuntimeError(f"{title}: expected one end document")
    text = text.replace(r"\usepackage{hyperref}", r"\usepackage{hyperref}" + "\n" + PREAMBLE_ADDITION, 1)
    text = text.rsplit(r"\end{document}", 1)[0].rstrip() + "\n\n"
    lineages = [
        {
            "role": "R823 translated title/introduction base",
            "path": title.resolve().as_posix(),
            "bytes": len(title_bytes),
            "sha256": sha256(title_bytes),
            "applied_delta": "current-authority TOC §25 R_r->K_r and singular->plural maximal commutative subfields",
        }
    ]
    for section in range(1, 32):
        unit_id = f"BOOK_S{section:02d}"
        source = UNIT_DIR / target / f"{unit_id}.texfrag"
        if not source.exists():
            raise FileNotFoundError(source)
        data = source.read_bytes()
        unit_text = data.decode("utf-8-sig").strip()
        text += f"% BEGIN {unit_id}\n" + unit_text + f"\n% END {unit_id}\n\n"
        lineages.append(
            {
                "role": "ED0005-aligned translated lecture unit",
                "unit_id": unit_id,
                "path": source.resolve().as_posix(),
                "bytes": len(data),
                "sha256": sha256(data),
            }
        )
    text += r"\end{document}" + "\n"
    output = RELEASE_SOURCE / f"44-book-{target}.tex"
    output.write_text(text, encoding="utf-8", newline="\n")
    return output, lineages


def main() -> int:
    RELEASE_SOURCE.mkdir(parents=True, exist_ok=True)
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    source_records: list[dict] = []
    base_lineage: list[dict] = []
    for target, archive_name in BASE_SOURCE_NAMES.items():
        source = ARCHIVE_R19 / archive_name
        output = RELEASE_SOURCE / f"base-papers1-43-{target}.tex"
        data = source.read_bytes()
        output.write_bytes(data)
        if output.read_bytes() != data:
            raise RuntimeError(f"numbered-paper base copy mismatch for {target}")
        source_records.append(
            file_record(output, f"exact archive-normalized editable Papers 1--43 base ({target})")
        )
        base_lineage.append(
            {
                "target": target,
                "source_path": source.resolve().as_posix(),
                "source_bytes": len(data),
                "source_sha256": sha256(data),
                "release_path": output.resolve().as_posix(),
                "release_sha256": sha256(output.read_bytes()),
                "copy_identity": output.read_bytes() == data,
                "scope": "219 exact numbered-paper units; no post-P43 continuation",
                "authority_reconciliation": "P06 already contains ED0005 exponents 4 and 3 plus inherited H-star repairs; see authority_reconciliation_v038.json",
            }
        )
    book_lineage: dict[str, list[dict]] = {}
    for target in ("ru", "uk", "isv"):
        book, lineage = build_book(target)
        source_records.append(file_record(book, f"complete Work 44 lecture reader source ({target})"))
        book_lineage[target] = lineage

    latin_book = RELEASE_SOURCE / "44-book-isv.tex"
    cyrillic_book = RELEASE_SOURCE / "44-book-isv-cy.tex"
    latin_text = latin_book.read_text(encoding="utf-8")
    cyrillic_text, validation = transliterate_document(latin_text)
    cyrillic_book.write_text(cyrillic_text, encoding="utf-8", newline="\n")
    if not validation["pass"]:
        raise RuntimeError(f"Cyrillic projection failed: {validation['errors']}")
    source_records.append(
        file_record(
            cyrillic_book,
            "complete Work 44 deterministic Cyrillic Interslavic reader source",
            {
                "source_path": latin_book.resolve().as_posix(),
                "source_sha256": sha256(latin_book.read_bytes()),
                "classification": "reader projection, not independent translation witness",
            },
        )
    )

    static_lineage: list[dict] = []
    cyrillic_static_validation: list[dict] = []
    for role, directory, stem in (
        ("Post45 Kapferer-Noether source", POST45_DIR, "45"),
        ("post-numbered bibliography source", POSTBIB_DIR, "bib"),
    ):
        for target in ("ru", "uk", "isv"):
            source = directory / f"{target}.tex"
            output = RELEASE_SOURCE / f"{stem}-{target}.tex"
            data = source.read_bytes()
            output.write_bytes(data)
            source_records.append(file_record(output, f"{role} ({target})"))
            static_lineage.append(
                {
                    "role": role,
                    "target": target,
                    "source_path": source.resolve().as_posix(),
                    "source_bytes": len(data),
                    "source_sha256": sha256(data),
                    "release_path": output.resolve().as_posix(),
                    "release_sha256": sha256(output.read_bytes()),
                    "copy_identity": data == output.read_bytes(),
                }
            )
        latin = RELEASE_SOURCE / f"{stem}-isv.tex"
        cyrillic = RELEASE_SOURCE / f"{stem}-isv-cy.tex"
        cyrillic_text, static_validation = transliterate_document(
            latin.read_text(encoding="utf-8-sig")
        )
        if not static_validation["pass"]:
            raise RuntimeError(
                f"Cyrillic projection failed for {stem}: {static_validation['errors']}"
            )
        cyrillic.write_text(cyrillic_text, encoding="utf-8", newline="\n")
        source_records.append(
            file_record(cyrillic, f"{role} (deterministic isv-cy projection)")
        )
        legacy_cyrillic = directory / "isv-cy.tex"
        static_lineage.append(
            {
                "role": role,
                "target": "isv-cy",
                "source_path": latin.resolve().as_posix(),
                "source_bytes": latin.stat().st_size,
                "source_sha256": sha256(latin.read_bytes()),
                "release_path": cyrillic.resolve().as_posix(),
                "release_sha256": sha256(cyrillic.read_bytes()),
                "classification": "deterministic reader projection, not independent translation witness",
                "preserved_legacy_cyrillic_path": legacy_cyrillic.resolve().as_posix(),
                "preserved_legacy_cyrillic_sha256": sha256(legacy_cyrillic.read_bytes()),
            }
        )
        cyrillic_static_validation.append(
            {"component": stem, "source": latin.resolve().as_posix(), **static_validation}
        )

    manifest = {
        "schema": "noether-slavic-v038-release-source-assembly/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "authority": {
            "pointer_id": "NOETH-DE-AUTH-v038-20260805",
            "pointer_sha256": "666FCB863C8599778BB1B48DCD0D4E444D6486133B7FE703E6CDE073F15FFBAE",
            "authority_id": "NOETH-DE-ED-0005",
            "authority_sha256": "1A44F967B29972E8F99E5C323A479162AD82A23FC457395915A4BB9DDF51AD41",
            "post_p43_identity_sha256": "662BBFC0926381E0D45A2356BF19959FCAEE6282F6F049E85B0BD5D553E80B58",
            "post_p43_scope": "BOOK_TITLE_INTRO, BOOK_S01--BOOK_S31, POST45, POSTBIB",
        },
        "source_records": source_records,
        "numbered_paper_base_lineage": base_lineage,
        "book_lineage": book_lineage,
        "cyrillic_projection_validation": validation,
        "cyrillic_static_projection_validation": cyrillic_static_validation,
        "static_lineage": static_lineage,
    }
    manifest_path = EVIDENCE / "source_assembly.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"PASS sources={len(source_records)} manifest={manifest_path} "
        f"sha256={sha256(manifest_path.read_bytes())}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
