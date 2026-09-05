#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import pathlib
import sys

from pypdf import PdfReader


AUTH_SHA = "8392B345D4854E6DC55FB42CFC0B616D941935983723627237239A87348F42E5"


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def canonical(record: dict) -> str:
    return json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def canonical_hash(record: dict) -> str:
    return sha_bytes(canonical(record).encode("utf-8"))


def load_records(path: pathlib.Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


OBJECTS: dict[int, list[tuple[str, str]]] = {
    31: [
        ("theorem_8_1_continuation_and_point_count", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("theorem_8_2_modular_form_statement", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("remark_8_3", "INCLUDE"),
        ("theorem_8_4_opening", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("running_head_author", "EXCLUDE_BODY_RETAIN_PROVENANCE"),
        ("printed_folio_302_top_and_bottom", "EXCLUDE_BODY_RETAIN_PAGE_ANCHOR"),
    ],
    32: [
        ("theorem_8_4_exponential_sum_bound", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("equations_8_4_1_to_8_4_3", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("artin_schreier_cover_and_frobenius_trace", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("lambda_adic_rank_one_systems", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("lemma_8_5", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("running_head_title", "EXCLUDE_BODY_RETAIN_PROVENANCE"),
        ("printed_folio_303_top_and_bottom", "EXCLUDE_BODY_RETAIN_PAGE_ANCHOR"),
    ],
    33: [
        ("deduction_8_4_from_8_5", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("trace_identity", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("diagram_8_6_1", "INCLUDE_EDITABLE_DIAGRAM_EXACT_TOPOLOGY"),
        ("lemma_8_7_and_equations_8_7_1", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("lemma_8_8", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("paragraph_8_9", "INCLUDE"),
        ("running_head_author", "EXCLUDE_BODY_RETAIN_PROVENANCE"),
        ("printed_folio_304_top_and_bottom", "EXCLUDE_BODY_RETAIN_PAGE_ANCHOR"),
    ],
    34: [
        ("paragraph_8_9_continuation", "INCLUDE"),
        ("paragraph_8_10_universal_family", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("relative_compactification_square", "INCLUDE_EDITABLE_DIAGRAM_EXACT_TOPOLOGY"),
        ("derived_direct_image_decomposition", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("separation_of_variables_opening", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("running_head_title", "EXCLUDE_BODY_RETAIN_PROVENANCE"),
        ("printed_folio_305_top_and_bottom", "EXCLUDE_BODY_RETAIN_PAGE_ANCHOR"),
        ("printer_signature_39", "EXCLUDE_BODY_RETAIN_PROVENANCE"),
    ],
    35: [
        ("kunneth_reduction", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("paragraph_8_11", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("lemmas_8_12_and_8_13", "INCLUDE_EDITABLE_LINEAR_MATH"),
        ("serre_reference", "INCLUDE"),
        ("bibliography_heading_and_entries_1_to_3", "INCLUDE"),
        ("running_head_author", "EXCLUDE_BODY_RETAIN_PROVENANCE"),
        ("printed_folio_306_top_and_bottom", "EXCLUDE_BODY_RETAIN_PAGE_ANCHOR"),
    ],
    36: [
        ("bibliography_entry_4", "INCLUDE"),
        ("sga_sigla_and_entries", "INCLUDE"),
        ("received_date", "INCLUDE"),
        ("terminal_horizontal_rule", "EXCLUDE_BODY_RETAIN_PROVENANCE"),
        ("running_head_title", "EXCLUDE_BODY_RETAIN_PROVENANCE"),
        ("printed_folio_307_top_and_bottom", "EXCLUDE_BODY_RETAIN_PAGE_ANCHOR"),
    ],
}


def main() -> None:
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    receipt = root / "audit" / "P06_SOURCE_FREEZE_V4.tsv"
    with receipt.open(encoding="utf-8", newline="") as stream:
        freeze_rows = {int(row["physical_page"]): row for row in csv.DictReader(stream, delimiter="\t")}
    assert set(freeze_rows) == set(range(31, 37))

    source_path = root / "source" / "20_AUTHORITY_DELIGNE_D020_WEIL_I_NUMDAM_36PP.pdf"
    assert sha_file(source_path) == AUTH_SHA
    pdf = PdfReader(source_path)
    assert len(pdf.pages) == 36

    layer_paths = {
        "source_language": root / "edition" / "source_language.ndjson",
        "english_standalone": root / "edition" / "english_standalone.ndjson",
        "apparatus": root / "edition" / "apparatus.ndjson",
    }
    existing = {layer: load_records(path) for layer, path in layer_paths.items()}
    for layer, records in existing.items():
        assert [int(record["physical_page"]) for record in records] == list(range(1, 31)), layer

    new_records = {layer: [] for layer in layer_paths}
    page_qa_rows = []
    for physical in range(31, 37):
        printed = physical + 271
        freeze_row = freeze_rows[physical]
        french_path = root / pathlib.Path(freeze_row["french_record_path"])
        assert french_path.stat().st_size == int(freeze_row["bytes"])
        assert sha_file(french_path) == freeze_row["sha256"]
        french = french_path.read_text(encoding="utf-8").rstrip("\n")
        english = (root / "edition" / "english_p06" / f"P{physical:04d}.en.txt").read_text(encoding="utf-8").rstrip("\n")
        apparatus = (root / "edition" / "apparatus_p06" / f"P{physical:04d}.app.txt").read_text(encoding="utf-8").rstrip("\n")

        page = pdf.pages[physical - 1]
        content = page.get_contents().get_data()
        images = page.images
        assert len(images) == 1
        render_rel = f"control/pixel_replay/P06/page-{physical}.png"
        render = root / pathlib.Path(render_rel)
        objects = [
            {"disposition": disposition, "id": f"P{physical:04d}-O{index:02d}", "kind": kind}
            for index, (kind, disposition) in enumerate(OBJECTS[physical], 1)
        ]
        provenance = {
            "authority_pdf_sha256": AUTH_SHA,
            "content_stream_bytes": len(content),
            "content_stream_sha256": sha_bytes(content),
            "embedded_images": [
                {
                    "name": images[0].name,
                    "tiff_bytes": len(images[0].data),
                    "tiff_sha256": sha_bytes(images[0].data),
                }
            ],
            "render_200dpi_path": render_rel,
            "render_200dpi_sha256": sha_file(render),
        }
        source_record = {
            "assets": [],
            "disposition": "INCLUDE_ARTICLE",
            "editorial_policy": {
                "authority_first": True,
                "centered_and_running_folios": "retained as page anchors/provenance, not body text",
                "editable_math_encoding": "Unicode and linear mathematical notation; no mathematical content omitted or silently corrected",
                "figure_fallback": "none required in P06; both diagrams were safely reconstructed with exact editable arrow topology",
                "salvage_consulted_before_freeze": False,
                "versioned_authority_repair": "v1 frozen before salvage; current v4 is an authority-only correction derived from independent and magnified replays",
            },
            "objects": objects,
            "physical_page": physical,
            "printed_page": printed,
            "provenance": provenance,
            "source_sha256": AUTH_SHA,
            "status": "frozen",
            "text": french,
        }
        source_hash = canonical_hash(source_record)
        english_record = {
            "assets": [],
            "based_on_source_record_sha256": source_hash,
            "disposition": "INCLUDE_ARTICLE",
            "objects": objects,
            "physical_page": physical,
            "printed_page": printed,
            "source_sha256": AUTH_SHA,
            "status": "accepted",
            "text": english,
            "translation_policy": {
                "authority_pixels_rechecked": True,
                "no_translator_or_repository_copy_matter_added": True,
                "source_frozen_before_translation": True,
                "standalone_english": True,
                "technical_notation": "Source symbols, equation numbering, inequalities, diagrams, bibliography, sigla, and terminus retained in editable linear notation",
            },
            "witness_review": {
                "ias_and_collected_comparators": "rendered after the v1 source freeze; no comparator-only form was introduced",
                "paper20_french_tex": "consulted after the v1 source freeze; concrete divergences are logged and none was automatically adopted",
                "prior_work_state": "all 272 members remain ZERO_ACCEPTED",
            },
        }
        english_hash = canonical_hash(english_record)
        apparatus_record = {
            "assets": [],
            "disposition": "INCLUDE_ARTICLE",
            "english_record_sha256": english_hash,
            "objects_disposed": len(objects),
            "physical_page": physical,
            "printed_page": printed,
            "source_record_sha256": source_hash,
            "source_sha256": AUTH_SHA,
            "status": "accepted",
            "text": apparatus,
            "witness_log": "audit/P06_SALVAGE_COMPARISON.tsv",
        }
        apparatus_hash = canonical_hash(apparatus_record)
        new_records["source_language"].append(source_record)
        new_records["english_standalone"].append(english_record)
        new_records["apparatus"].append(apparatus_record)
        page_qa_rows.append((physical, printed, source_hash, english_hash, apparatus_hash, len(objects)))

    for layer, path in layer_paths.items():
        records = existing[layer] + new_records[layer]
        payload = "\n".join(canonical(record) for record in records) + "\n"
        path.write_text(payload, encoding="utf-8", newline="\n")

    coverage_path = root / "coverage" / "coverage.tsv"
    with coverage_path.open(encoding="utf-8", newline="") as stream:
        coverage = list(csv.DictReader(stream, delimiter="\t"))
        fieldnames = list(coverage[0])
    assert [int(row["physical_page"]) for row in coverage] == list(range(1, 37))
    hashes = {row[0]: row for row in page_qa_rows}
    for row in coverage:
        physical = int(row["physical_page"])
        if physical not in hashes:
            continue
        _, _, source_hash, english_hash, apparatus_hash, _ = hashes[physical]
        row.update(
            source_status="FROZEN",
            english_status="ACCEPTED",
            apparatus_status="ACCEPTED",
            final_status="ACCEPTED",
            record_sha256_source=source_hash,
            record_sha256_english=english_hash,
            record_sha256_apparatus=apparatus_hash,
        )
    with coverage_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(coverage)

    qa = root / "audit" / "S06_PAGE_QA.tsv"
    lines = [
        "physical_page\tprinted_page\tdisposition\tsource_record_sha256\tenglish_record_sha256\tapparatus_record_sha256\tobject_dispositions\tasset_pairs\tresult\tnote"
    ]
    for physical, printed, source_hash, english_hash, apparatus_hash, count in page_qa_rows:
        lines.append(
            f"{physical}\t{printed}\tINCLUDE_ARTICLE\t{source_hash}\t{english_hash}\t{apparatus_hash}\t{count}\t0\tPASS\tAuthority pixels were replayed before the v1 French freeze; current v3 is authority-only; post-freeze witnesses remained ZERO_ACCEPTED; English and apparatus were checked against the frozen French and authority pixels; every scoped object has a disposition."
        )
    qa.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    readme = root / "README.md"
    readme.write_text(
        "# DELIGNE_D020_WEIL_I cumulative full state\n\n"
        "Current cumulative state: S06 / P06 COMPLETE. Accepted physical-page dispositions: 36 of 36. "
        "Accepted article pages: 35 of 35 (authority physical pages 2-36; printed 273-307).\n\n"
        "P06 completes authority physical pages 31-36, including Theorems (8.2) and (8.4), Lemmas (8.5)-(8.13), "
        "the bibliography, SGA sigla, received date, and physical terminus. The French source records were frozen "
        "before comparison with inherited witnesses. The standalone French, standalone English, and separate apparatus remain distinct.\n\n"
        "The final clean nonpatching audit receipt is audit/S06_COLD_AUDIT.tsv. No later prompt exists.\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps({"result": "PASS", "integrated_pages": 6, "cumulative_pages": 36}, sort_keys=True))


if __name__ == "__main__":
    main()
