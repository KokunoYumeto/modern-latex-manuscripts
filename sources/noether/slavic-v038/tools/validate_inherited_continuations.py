#!/usr/bin/env python3
"""Validate inherited title, Post45, and PostBibliography custody against ED0005.

This audit deliberately separates three evidence classes:

* byte identity with previously reviewed Slavic artifacts;
* current-authority deltas that must be inherited by the release;
* source-backed target readings that disagree with the German cumulative TeX.

It does not treat archive metadata, model review, or cross-surface agreement as
native-speaker or original-source certification.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parents[3]
LINEAGE = ROOT / "lineage"
RELEASE_SOURCE = ROOT / "release" / "source"
OUTPUT = ROOT / "release" / "evidence" / "inherited_continuation_audit.json"
SLAVIC_ARCHIVE = WORKSPACE / "03_projects" / "noether" / "08_zenodo" / "r19" / "slavic.zip"
AUTHORITY_UNITS = ROOT / "authority_units"
SOURCE_ROOT = Path(
    r"C:\Users\Floris\Downloads\codex backup dump 7-4\$germanOut"
)
POST45_WITNESS = (
    SOURCE_ROOT
    / "sources"
    / "endmatter"
    / "post45"
    / "Noether_Post45_Kapferer_Noether_Multiplizitaetsbedingungen_German_TeX_witness_body.tex"
)
POSTBIB_WITNESS = (
    SOURCE_ROOT
    / "sources"
    / "endmatter"
    / "postbibliography"
    / "Noether_PostBibliography_Terminal_Material_German_TeX_witness_body.tex"
)
SOURCE_PDF = SOURCE_ROOT / "sources" / "endmatter" / "source_blocks" / "noether_pages_751_798.pdf"
SOURCE_TEXT = SOURCE_ROOT / "sources" / "endmatter" / "source_blocks" / "noether_pages_751_798.txt"

EXPECTED_SOURCE_HASHES = {
    POST45_WITNESS: "EE787705D719584295D6203BE1E1B4F751DE24127B403560A962792B1DA1572E",
    POSTBIB_WITNESS: "854CE0629CA14AFE6F6C71AE04D4347C8787783041C54D3E606843BBF4A65E37",
    SOURCE_PDF: "155803818E3AF5FD5CDF80A9D29E4AA1F9770446C956DDC745313C52B742D961",
    SOURCE_TEXT: "5DF9EFF2D4C9F89998BD51276D45DE705F8FD34D4608FFD9BB084325691D58E1",
}

TITLE_MEMBERS = {
    "ru": "files/book/translations/russian/Noether_R823_BOOK_TITLE_INTRO_Russian_v001.tex",
    "uk": "files/book/translations/ukrainian/Noether_R823_BOOK_TITLE_INTRO_Ukrainian_v001.tex",
    "isv": "files/book/translations/interslavic/Noether_R823_BOOK_TITLE_INTRO_Interslavic_v001.tex",
    "isv-cy": "files/book/translations/interslavic-cyrillic/Noether_R823_BOOK_TITLE_INTRO_Interslavic_Cyrillic_v001.tex",
}
POST45_MEMBERS = {
    "ru": "files/canon/endmatter/post45/source_fidelity/russian/v001/Noether_Post45_SourceFidelity_Russian_v001.tex",
    "uk": "files/canon/endmatter/post45/source_fidelity/ukrainian/v001/Noether_Post45_SourceFidelity_Ukrainian_v001.tex",
    "isv": "files/canon/endmatter/post45/source_fidelity/interslavic/v001/Noether_Post45_SourceFidelity_Interslavic_v001.tex",
    "isv-cy": "files/canon/endmatter/post45/source_fidelity/interslavic-cyrillic/v001/Noether_Post45_SourceFidelity_Interslavic_Cyrillic_v001.tex",
}
POSTBIB_MEMBERS = {
    "ru": "files/canon/endmatter/postbibliography/source_fidelity/russian/v001/Noether_PostBibliography_SourceFidelity_Russian_v001.tex",
    "uk": "files/canon/endmatter/postbibliography/source_fidelity/ukrainian/v001/Noether_PostBibliography_SourceFidelity_Ukrainian_v001.tex",
    "isv": "files/canon/endmatter/postbibliography/source_fidelity/interslavic/v001/Noether_PostBibliography_SourceFidelity_Interslavic_v001.tex",
    "isv-cy": "files/canon/endmatter/postbibliography/source_fidelity/interslavic-cyrillic/v001/Noether_PostBibliography_SourceFidelity_Interslavic_Cyrillic_v001.tex",
}
POST45_METADATA = (
    "files/canon/endmatter/post45/source_fidelity/"
    "noether_post45_source_fidelity_translation_unit_v001.json"
)
POSTBIB_METADATA = (
    "files/canon/endmatter/postbibliography/source_fidelity/"
    "noether_postbibliography_source_fidelity_translation_unit_v001.json"
)
TITLE_METADATA = "files/book/evidence/TRANSLATION_UNIT.json"

MATH_RE = re.compile(
    r"(?<!\\)\\\[.*?(?<!\\)\\\]|(?<!\\)\\\(.*?(?<!\\)\\\)|"
    r"(?<!\$)\$\$.*?\$\$(?!\$)|(?<![\\$])\$(?:\\.|[^$])*?(?<!\\)\$(?!\$)",
    re.DOTALL,
)


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def file_record(path: Path) -> dict:
    return {
        "path": path.resolve().as_posix(),
        "bytes": path.stat().st_size,
        "sha256": sha_file(path),
    }


def zip_record(archive: ZipFile, member: str) -> dict:
    data = archive.read(member)
    return {"member": member, "bytes": len(data), "sha256": sha_bytes(data)}


def normalized_tex(value: str) -> str:
    return re.sub(r"\s+", "", value).replace("−", "-")


def first_enumerate_item_count(text: str) -> int:
    match = re.search(r"\\begin\{enumerate\}(.*?)\\end\{enumerate\}", text, re.DOTALL)
    if not match:
        return 0
    return len(re.findall(r"(?m)^\\item(?:\[.*?\])?", match.group(1)))


def structural_signature(text: str) -> dict:
    return {
        "labels": sorted(re.findall(r"\\label\{([^}]+)\}", text)),
        "references": sorted(re.findall(r"\\(?:eqref|ref)\{([^}]+)\}", text)),
        "display_count": len(re.findall(r"(?<!\\)\\\[", text)),
        "math_span_count": len(MATH_RE.findall(text)),
    }


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    checks: list[dict] = []

    for path, expected in EXPECTED_SOURCE_HASHES.items():
        if not path.exists():
            errors.append(f"missing source custody file: {path}")
            continue
        actual = sha_file(path)
        passed = actual == expected
        checks.append(
            {
                "check": "source_custody_hash",
                "file": file_record(path),
                "expected_sha256": expected,
                "pass": passed,
            }
        )
        if not passed:
            errors.append(f"source custody hash mismatch: {path}")

    archive_records = []
    metadata_adverse = []
    with ZipFile(SLAVIC_ARCHIVE) as archive:
        title_metadata = json.loads(archive.read(TITLE_METADATA).decode("utf-8"))
        post45_metadata = json.loads(archive.read(POST45_METADATA).decode("utf-8"))
        postbib_metadata = json.loads(archive.read(POSTBIB_METADATA).decode("utf-8"))
        metadata_documents = {
            "title": {item["language"].lower(): item for item in title_metadata["targets"]},
            "post45": {item["language"]: item for item in post45_metadata["files"]},
            "postbib": {item["language"]: item for item in postbib_metadata["files"]},
        }
        metadata_names = {
            "ru": "russian",
            "uk": "ukrainian",
            "isv": "interslavic",
            "isv-cy": "interslavic_cyrillic",
        }
        title_names = {
            "ru": "russian",
            "uk": "ukrainian",
            "isv": "interslavic latin",
            "isv-cy": "interslavic cyrillic",
        }
        for group, members, directory in (
            ("title", TITLE_MEMBERS, LINEAGE / "title_r823"),
            ("post45", POST45_MEMBERS, LINEAGE / "post45"),
            ("postbib", POSTBIB_MEMBERS, LINEAGE / "postbib"),
        ):
            for target, member in members.items():
                archive_record = zip_record(archive, member)
                current = directory / f"{target}.tex"
                current_record = file_record(current)
                passed = current_record["sha256"] == archive_record["sha256"]
                if not passed:
                    errors.append(f"{group}/{target} is not byte-identical to archived reviewed artifact")
                metadata_key = title_names[target] if group == "title" else metadata_names[target]
                metadata_record = metadata_documents[group][metadata_key]
                metadata_hash = metadata_record["tex_sha256"]
                metadata_matches_member = metadata_hash == archive_record["sha256"]
                if not metadata_matches_member:
                    metadata_adverse.append(
                        {
                            "group": group,
                            "target": target,
                            "metadata_sha256": metadata_hash,
                            "actual_archived_member_sha256": archive_record["sha256"],
                            "classification": "stale archive metadata; actual archived member and current lineage are byte-identical",
                        }
                    )
                archive_records.append(
                    {
                        "group": group,
                        "target": target,
                        "archive": archive_record,
                        "current": current_record,
                        "byte_identity": passed,
                        "metadata_sha256": metadata_hash,
                        "metadata_matches_member": metadata_matches_member,
                    }
                )

    authority_post45 = (AUTHORITY_UNITS / "POST45.texfrag").read_text(encoding="utf-8-sig")
    authority_postbib = (AUTHORITY_UNITS / "POSTBIB.texfrag").read_text(encoding="utf-8-sig")
    source_witness = POST45_WITNESS.read_text(encoding="utf-8-sig")
    source_text = SOURCE_TEXT.read_text(encoding="utf-8-sig")
    authority_compact = normalized_tex(authority_post45)
    witness_compact = normalized_tex(source_witness)
    source_text_compact = normalized_tex(source_text)
    authority_wrong_example = "\\psi=x^2+y^3" in authority_compact
    witness_correct_example = "\\psi=x^{2}-y^{5}" in witness_compact
    extraction_correct_example = "ψ=x2-y5" in source_text_compact
    if not (authority_wrong_example and witness_correct_example and extraction_correct_example):
        errors.append("could not reproduce the bounded Post45 Bertini source discrepancy")

    target_correct_example = {}
    post45_signatures = {}
    postbib_counts = {}
    current_delta_checks = {}
    for target in ("ru", "uk", "isv"):
        post45_path = LINEAGE / "post45" / f"{target}.tex"
        post45 = post45_path.read_text(encoding="utf-8-sig")
        compact = normalized_tex(post45)
        target_correct_example[target] = (
            "\\psi=x^{2}-y^{5}" in compact and "\\psi=x^{2}+y^{3}" not in compact
        )
        if not target_correct_example[target]:
            errors.append(f"{target} Post45 does not preserve the source-backed Bertini example")
        first_45 = "\n".join(post45.splitlines()[:45])
        current_delta_checks[target] = {
            "header_location_removed": "Freiburg" not in first_45 and "Göttingen" not in first_45,
            "varrho_present": post45.count(r"\varrho") >= 2,
            "bare_rho_absent": re.search(r"(?<!var)\\rho\b", post45) is None,
            "source_backed_A_B_identity_present": (
                "A" in post45
                and "B" in post45
                and "K = A\\varphi + B\\psi" in post45
            ),
        }
        if not all(current_delta_checks[target].values()):
            errors.append(f"{target} Post45 current-delta/source-normalization check failed")
        post45_signatures[target] = structural_signature(post45)

        postbib = (LINEAGE / "postbib" / f"{target}.tex").read_text(encoding="utf-8-sig")
        postbib_counts[target] = {
            "main_bibliography_items": first_enumerate_item_count(postbib),
            "total_items": len(re.findall(r"(?m)^\\item(?:\[.*?\])?", postbib)),
            "old_item_34_colon_absent": r"\item[34:]" not in postbib,
        }
        if postbib_counts[target] != {
            "main_bibliography_items": 43,
            "total_items": 62,
            "old_item_34_colon_absent": True,
        }:
            errors.append(f"{target} PostBibliography item structure failed")

    common_labels = len({tuple(value["labels"]) for value in post45_signatures.values()}) == 1
    common_refs = len({tuple(value["references"]) for value in post45_signatures.values()}) == 1
    common_displays = {value["display_count"] for value in post45_signatures.values()} == {14}
    math_counts = {target: value["math_span_count"] for target, value in post45_signatures.items()}
    uk_inline_fusion_explains_count = math_counts == {"ru": 297, "uk": 296, "isv": 297}
    if not (common_labels and common_refs and common_displays and uk_inline_fusion_explains_count):
        errors.append("Post45 cross-surface structural signature failed")

    release_delta_checks = {}
    for target in ("ru", "uk", "isv", "isv-cy"):
        book = RELEASE_SOURCE / f"44-book-{target}.tex"
        if not book.exists():
            errors.append(f"missing assembled release book source: {book}")
            continue
        text = book.read_text(encoding="utf-8-sig")
        toc_25_match = re.search(r"(?m)^\\tocsec\{25\}.*$", text)
        toc_25_compact = normalized_tex(toc_25_match.group(0)) if toc_25_match else ""
        release_delta_checks[target] = {
            "toc_25_found": bool(toc_25_match),
            "toc_25_K_r": r"\mathfrakK_r" in toc_25_compact,
            "toc_25_R_r_absent": r"\mathfrakR_r" not in toc_25_compact,
        }
        if not all(release_delta_checks[target].values()):
            errors.append(f"{target} assembled title TOC §25 current-authority delta failed")

    authority_postbib_state = {
        "item_34_period_present": r"\item[34.]" in authority_postbib,
        "item_34_colon_absent": r"\item[34:]" not in authority_postbib,
    }
    if not all(authority_postbib_state.values()):
        errors.append("authority PostBibliography item 34 correction is not current")

    result = {
        "schema": "noether-slavic-v038-inherited-continuation-audit/1.0",
        "generated_at": datetime.now().astimezone().isoformat(),
        "pass": not errors,
        "evidence_classes": {
            "source_fact": (
                "hash-bound German witness, page-scan text extraction, and archived reviewed artifact bytes"
            ),
            "computation": (
                "SHA-256 identity, explicit delta probes, TeX structural counts, and deterministic assembly checks"
            ),
            "editorial_inference": (
                "the target x^2-y^5 reading is retained because both the direct TeX witness and scan extraction agree; "
                "it is not an automatic mutation of German authority"
            ),
            "external_or_human_validation": (
                "prior internal source/build/visual review recorded by the archived metadata; no native-speaker or new independent original-print certification"
            ),
        },
        "source_custody_checks": checks,
        "archive_identity_records": archive_records,
        "metadata_adverse_evidence": metadata_adverse,
        "current_authority_delta_checks": {
            "post45": current_delta_checks,
            "postbib": authority_postbib_state,
            "assembled_title": release_delta_checks,
        },
        "post45_cross_surface_structure": {
            "signatures": post45_signatures,
            "common_labels": common_labels,
            "common_references": common_refs,
            "common_display_count_14": common_displays,
            "math_span_counts": math_counts,
            "uk_count_difference_explanation": (
                "Ukrainian places q^(nu)=... inside one math island where Russian and Interslavic use two adjacent islands; "
                "the symbols are present and label/reference/display structure is unchanged"
            ),
            "count_difference_explained": uk_inline_fusion_explains_count,
        },
        "postbibliography_structure": postbib_counts,
        "source_backed_german_authority_discrepancy": {
            "work_unit": "POST45",
            "authority_locator": "POST45.texfrag lines 117-121",
            "authority_reading": r"\varphi=x^3+y^4; \psi=x^2+y^3",
            "direct_witness_locator": (
                "Noether_Post45_Kapferer_Noether_Multiplizitaetsbedingungen_German_TeX_witness_body.tex lines 287-292"
            ),
            "direct_witness_reading": r"\varphi=x^{3}+y^{4}, \psi=x^{2}-y^{5}",
            "scan_text_locator": "noether_pages_751_798.txt lines 2095-2098; source PDF page 46",
            "scan_reading": "φ=x³+y⁴, ψ=x²−y⁵",
            "target_state": target_correct_example,
            "disposition": (
                "preserve source-backed Slavic target reading; report exact correction to German/Noether owner; do not mutate German authority here"
            ),
        },
        "warnings": warnings,
        "errors": errors,
        "review_limit": (
            "PASS establishes inherited artifact identity and bounded current-authority/source reconciliation only; "
            "it is not native review or complete independent original-print reaudit"
        ),
        "continuation_cursor": (
            "next verified German authority delta affecting BOOK_TITLE_INTRO/POST45/POSTBIB, or native-language review"
        ),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "pass": result["pass"],
                "errors": errors,
                "output": file_record(OUTPUT),
            },
            ensure_ascii=False,
        )
    )
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
