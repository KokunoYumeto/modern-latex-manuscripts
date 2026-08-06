#!/usr/bin/env python3
"""Prove the bounded ED0004 -> ED0005 delta and Slavic target state.

This tool is deliberately read-only outside its two evidence reports.  It does
not mutate German custody, the public archive package, the v014 checkpoint, or
any translation unit.  The report distinguishes the complete numbered-paper
base from the still-active post-P43 continuation.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parents[3]
CANON = WORKSPACE / "03_projects" / "noether" / "07_german_canon_control"
POINTER = CANON / "CURRENT_GERMAN_AUTHORITY_POINTER.json"
ED0004 = CANON / "candidates" / "ED0004" / "noether.tex"
ED0005 = CANON / "candidates" / "ED0005" / "noether.tex"
R19 = WORKSPACE / "03_projects" / "noether" / "08_zenodo" / "r19"
V014 = ROOT.parent / "noether_ru_uk_v014"
SNAPSHOT = ROOT / "lineage" / "human_edited_ed0004_incomplete_20260804"
EVIDENCE = ROOT / "evidence"

POINTER_ID = "NOETH-DE-AUTH-v038-20260805"
POINTER_SHA256 = "666FCB863C8599778BB1B48DCD0D4E444D6486133B7FE703E6CDE073F15FFBAE"
AUTHORITY_ID = "NOETH-DE-ED-0005"
ED0004_SHA256 = "0CB422ECD397DD392A8625297A508DAEE3A5A934EA19EEEF49B47B319EA4F2BB"
ED0005_SHA256 = "1A44F967B29972E8F99E5C323A479162AD82A23FC457395915A4BB9DDF51AD41"

OLD_FORMULA = (
    r"\Psi(z,u)=x_1^2z^2-x_1^2u_1^2-2x_1^2x_2u_1u_2-x_1^2x_2^2u_2^2."
)
NEW_FORMULA = (
    r"\Psi(z,u)=x_1^2z^2-x_1^4u_1^2-2x_1^3x_2u_1u_2-x_1^2x_2^2u_2^2."
)

SURFACES = {
    "ru": ("20-ru.tex", "10-ru.pdf", "noether-ru-v014.pdf"),
    "uk": ("20-uk.tex", "10-uk.pdf", "noether-uk-v014.pdf"),
    "isv-latn": ("20-isv-latn.tex", "10-isv-latn.pdf", "noether-isv-v014.pdf"),
    "isv-cyrl": ("20-isv-cyrl.tex", "10-isv-cyrl.pdf", "noether-isv-cy-v014.pdf"),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def record(path: Path) -> dict:
    return {
        "path": path.resolve().as_posix(),
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def snapshot_manifest() -> dict:
    files = []
    for path in sorted(item for item in SNAPSHOT.rglob("*") if item.is_file()):
        files.append(
            {
                "relative_path": path.relative_to(SNAPSHOT).as_posix(),
                **record(path),
            }
        )
    return {
        "schema": "noether-slavic-incomplete-ed0004-snapshot/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "snapshot_root": SNAPSHOT.resolve().as_posix(),
        "classification": "immutable lineage witness; incomplete and not release-eligible",
        "file_count": len(files),
        "total_bytes": sum(item["bytes"] for item in files),
        "files": files,
    }


def main() -> int:
    pointer_bytes = POINTER.read_bytes()
    pointer = json.loads(pointer_bytes.decode("utf-8-sig"))
    authority = pointer["default_translation_authority"]
    if pointer["pointer_id"] != POINTER_ID:
        raise RuntimeError(f"unexpected live pointer: {pointer['pointer_id']}")
    if sha256_bytes(pointer_bytes) != POINTER_SHA256:
        raise RuntimeError("live pointer SHA-256 mismatch")
    if authority["authority_id"] != AUTHORITY_ID:
        raise RuntimeError(f"unexpected authority: {authority['authority_id']}")
    if sha256_file(ED0004) != ED0004_SHA256 or sha256_file(ED0005) != ED0005_SHA256:
        raise RuntimeError("German authority file SHA-256 mismatch")

    old_lines = ED0004.read_bytes().splitlines(keepends=True)
    new_lines = ED0005.read_bytes().splitlines(keepends=True)
    if len(old_lines) != len(new_lines):
        raise RuntimeError("ED0004/ED0005 line-count mismatch")
    deltas = []
    for line_number, (old, new) in enumerate(zip(old_lines, new_lines), start=1):
        if old != new:
            deltas.append(
                {
                    "line": line_number,
                    "before_utf8": old.decode("utf-8").rstrip("\r\n"),
                    "after_utf8": new.decode("utf-8").rstrip("\r\n"),
                    "before_sha256": sha256_bytes(old),
                    "after_sha256": sha256_bytes(new),
                }
            )
    if len(deltas) != 1 or deltas[0]["line"] != 5383:
        raise RuntimeError(f"unexpected ED0004/ED0005 deltas: {deltas}")
    if OLD_FORMULA not in deltas[0]["before_utf8"] or NEW_FORMULA not in deltas[0]["after_utf8"]:
        raise RuntimeError("the exact P06 exponent delta was not observed")

    # One-based authority lines 20988--24145 are the entire post-P43 scope.
    old_post = b"".join(old_lines[20987:24145])
    new_post = b"".join(new_lines[20987:24145])
    if old_post != new_post:
        raise RuntimeError("post-P43 authority bytes changed between ED0004 and ED0005")

    surface_records = []
    for surface, (tex_name, archive_pdf_name, v014_pdf_name) in SURFACES.items():
        tex = R19 / tex_name
        archive_pdf = R19 / archive_pdf_name
        v014_pdf = V014 / v014_pdf_name
        text = tex.read_text(encoding="utf-8-sig")
        item = {
            "surface": surface,
            "archive_normalized_tex": record(tex),
            "archive_pdf": {**record(archive_pdf), "pages": len(PdfReader(str(archive_pdf)).pages)},
            "producer_v014_pdf": {**record(v014_pdf), "pages": len(PdfReader(str(v014_pdf)).pages)},
            "archive_pdf_is_exact_v014_pdf": archive_pdf.read_bytes() == v014_pdf.read_bytes(),
            "p06": {
                "accepted_formula_count": text.count(NEW_FORMULA),
                "superseded_formula_count": text.count(OLD_FORMULA),
                "accepted_H_star_nonzero_count": text.count(r"H^*(\xi)\ne0"),
                "bare_H_nonzero_count": text.count(r"H(\xi)\ne0"),
            },
            "scope": "complete numbered Papers 1--43 only; post-numbered continuation excluded",
        }
        if not item["archive_pdf_is_exact_v014_pdf"]:
            raise RuntimeError(f"archive PDF is not byte-identical to v014 for {surface}")
        if item["p06"]["accepted_formula_count"] != 1 or item["p06"]["superseded_formula_count"]:
            raise RuntimeError(f"P06 exponent state failed for {surface}")
        if item["p06"]["accepted_H_star_nonzero_count"] < 2 or item["p06"]["bare_H_nonzero_count"]:
            raise RuntimeError(f"P06 H-star state failed for {surface}")
        surface_records.append(item)

    snapshot = snapshot_manifest()
    if snapshot["file_count"] != 76 or snapshot["total_bytes"] != 489591:
        raise RuntimeError(
            f"unexpected incomplete snapshot state: {snapshot['file_count']} files / {snapshot['total_bytes']} bytes"
        )
    EVIDENCE.mkdir(parents=True, exist_ok=True)
    snapshot_path = EVIDENCE / "human_edited_ed0004_incomplete_snapshot.json"
    snapshot_path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    report = {
        "schema": "noether-slavic-ed0005-reconciliation/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "status": "PASS_BOUNDED_AUTHORITY_AND_BASE_RECONCILIATION",
        "authority": {
            "pointer": record(POINTER),
            "pointer_id": POINTER_ID,
            "authority_id": AUTHORITY_ID,
            "ed0004": record(ED0004),
            "ed0005": record(ED0005),
            "exact_deltas": deltas,
            "accepted_delta_count": len(authority["accepted_editorial_deltas"]),
        },
        "post_p43_identity": {
            "lines_one_based_inclusive": [20988, 24145],
            "bytes": len(new_post),
            "sha256": sha256_bytes(new_post),
            "ed0004_equals_ed0005": True,
            "consequence": "The previously extracted 34 post-P43 units remain byte-current; their metadata must be rebound to ED0005.",
        },
        "numbered_paper_bases": surface_records,
        "lineage_snapshot_manifest": record(snapshot_path),
        "interpretation": {
            "source_fact": "ED0005 differs from ED0004 at exactly German line 5383, changing two P06 exponents.",
            "computation": "All four archive-normalized Slavic TeX bases already contain the accepted exponent and H-star readings; their archived PDFs are exact v014 producer PDFs.",
            "editorial_inference": "No target wording repair is required for this German delta, but every final reader must be rebuilt/reviewed with ED0005-bound evidence and the missing post-P43 continuation.",
            "validation_limit": "This proves exact source and formula state, not native-language correctness or original-print fidelity beyond the pointer's retained evidence.",
        },
        "continuation_cursor": "Complete BOOK_TITLE_INTRO, BOOK_S01--BOOK_S31, POST45, and POSTBIB; then build four ED0005-bound cumulative readers.",
    }
    output = EVIDENCE / "authority_reconciliation_v038.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": report["status"],
                "authority_delta_count": len(deltas),
                "post_p43_sha256": report["post_p43_identity"]["sha256"],
                "surfaces": len(surface_records),
                "snapshot_files": snapshot["file_count"],
                "report": record(output),
                "snapshot_manifest": record(snapshot_path),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
