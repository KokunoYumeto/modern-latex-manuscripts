#!/usr/bin/env python3
"""Exercise the completion gate's previously demonstrated false-pass holes.

This is a parser/evidence-integrity self-test, not a translation-quality test.
It operates on an existing complete Spanish or French cumulative and writes only
inside a temporary directory.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from noether_r823_completion_gate import (
    EVIDENCE_MAP_FIELDS,
    PINNED_RENDER_PROFILE,
    REQUIRED_UNITS,
    UNIT_EVIDENCE_FIELDS,
    VISUAL_REVIEW_SCHEMA,
    bind_final_audit,
    bind_render_manifest,
    bind_unit_evidence,
    bind_visual_review_record,
    exact_page_spec,
    has_strong_source_locator,
    meaningful_review_text,
    page_pixel_binding_sha256,
    rerender_pdf_pixels,
    run_exact_promoter,
)
from noether_r823_target_unit_manifest import MARKERS, build, expand_tex, locate_any
from noether_sync_audit import slice_papers


def require(condition: bool, detail: str) -> None:
    if not condition:
        raise AssertionError(detail)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--language", choices=tuple(MARKERS), required=True)
    parser.add_argument("--target-tex", type=Path, required=True)
    parser.add_argument("--parity-promoter", type=Path)
    parser.add_argument("--pdftoppm", type=Path, required=True)
    args = parser.parse_args()

    promoter = args.parity_promoter.resolve() if args.parity_promoter is not None else None
    if promoter is None:
        promoter = (
            args.target_tex.resolve().parents[3]
            / "tools"
            / "promote_exact_parity_ledger.py"
        )
    require(promoter.is_file(), f"canonical promoter is missing: {promoter}")
    require(args.pdftoppm.is_file(), f"pdftoppm is missing: {args.pdftoppm}")

    text, dependencies, warnings = expand_tex(args.target_tex)
    require(not warnings, f"target expansion warnings: {warnings}")
    rows = build(args.target_tex, text, args.language)
    require(len(rows) == 81, f"expected 81 target units, found {len(rows)}")

    # Unit slices begin at Paper 1, so a preamble attack used to evade all 81
    # hashes.  It must now change the repeated whole-document hash while leaving
    # the unit hashes unchanged.
    attacked_preamble = "\\newcommand{\\GateAttack}{x}\n" + text
    attacked_rows = build(args.target_tex, attacked_preamble, args.language)
    require(
        [row.target_sha256 for row in rows]
        == [row.target_sha256 for row in attacked_rows],
        "preamble probe unexpectedly changed unit slices",
    )
    require(
        rows[0].target_document_sha256
        != attacked_rows[0].target_document_sha256,
        "whole-document hash did not detect a preamble mutation",
    )

    # A commented-out normal paper heading must not satisfy paper presence.
    p10 = slice_papers(text)[10].start
    p10_line_end = text.find("\n", p10)
    commented_p10 = text[:p10] + "% " + text[p10:p10_line_end] + text[p10_line_end:]
    try:
        slice_papers(commented_p10)
    except ValueError as exc:
        require("10" in str(exc), f"unexpected commented-heading failure: {exc}")
    else:
        raise AssertionError("commented Paper 10 heading still counted as live")

    papers = slice_papers(text)
    post45 = locate_any(
        text,
        MARKERS[args.language]["post45"],
        papers[43].start,
        "post45",
    )
    phrase = MARKERS[args.language]["post45"][0]
    injected = f"Prose mention: {phrase}.\n"
    prose_attack = text[:post45] + injected + text[post45:]
    require(
        locate_any(
            prose_attack,
            MARKERS[args.language]["post45"],
            papers[43].start,
            "post45",
        )
        == post45 + len(injected),
        "a prose mention was accepted as the post-45 heading",
    )

    supplement = locate_any(
        text,
        MARKERS[args.language]["supplement"],
        post45,
        "supplement",
    )
    bibliography = locate_any(
        text,
        MARKERS[args.language]["bibliography"],
        supplement,
        "bibliography",
    )
    bibliography_phrase = MARKERS[args.language]["bibliography"][0]
    styled_prose = f"Prose with \\emph{{{bibliography_phrase}}}, not a heading.\n"
    terminal_attack = text[:bibliography] + styled_prose + text[bibliography:]
    require(
        locate_any(
            terminal_attack,
            MARKERS[args.language]["bibliography"],
            supplement,
            "bibliography",
        )
        == bibliography + len(styled_prose),
        "styled prose was accepted as a terminal heading",
    )

    with tempfile.TemporaryDirectory() as temp_dir:
        temp = Path(temp_dir)
        (temp / "a.tex").write_text("A", encoding="utf-8")
        (temp / "b.tex").write_text("B", encoding="utf-8")
        (temp / "root.tex").write_text(
            "x \\input{a} y \\input b\n% \\input{missing}\nz",
            encoding="utf-8",
        )
        expanded, found, input_warnings = expand_tex(temp / "root.tex")
        require(not input_warnings, f"valid mixed inputs warned: {input_warnings}")
        require("x A y B" in expanded, "inline/braced or unbraced input was not expanded")
        require(
            {path.name for path in found} == {"root.tex", "a.tex", "b.tex"},
            f"wrong dependency set: {sorted(path.name for path in found)}",
        )

        (temp / "malformed.tex").write_text("\\input\n", encoding="utf-8")
        _, _, malformed_warnings = expand_tex(temp / "malformed.tex")
        require(
            any("unparsed input/include" in warning for warning in malformed_warnings),
            "malformed input command was silently ignored",
        )

        # Only live, in-range R823 authority lines count as strong terminology
        # provenance. Unresolved native-looking paths/pages remain weak.
        authority_fixture = temp / "Noether_R823_cum_de.tex"
        authority_fixture.write_text(
            "\n".join(f"authority line {number}" for number in range(1, 20001)),
            encoding="utf-8",
        )
        authority_kwargs = {
            "authority_path": authority_fixture,
            "authority_line_count": 20000,
            "authority_sha256": file_sha256(authority_fixture),
        }
        require(
            has_strong_source_locator(
                "R823 cum_de.tex lines 14536--14540", **authority_kwargs
            ),
            "exact R823 authority lines were rejected",
        )
        require(
            not has_strong_source_locator(
                "Numdam ASENS_1983_4_16_3_355_0.pdf, p. 358",
                **authority_kwargs,
            ),
            "unresolved native French PDF page locator was accepted",
        )
        require(
            not has_strong_source_locator(
                "native Spanish corpus:C:\\sources\\spanish\\uqc.tex:78; "
                f"sha256={'A' * 64}",
                **authority_kwargs,
            ),
            "unresolved hash-pinned native TeX line locator was accepted",
        )
        require(
            not has_strong_source_locator(
                "working/french_canon/validated_tex/Exp.1014.B.Keller.tex:1370-1406",
                **authority_kwargs,
            ),
            "unidentified native French TeX line locator was accepted",
        )
        require(
            not has_strong_source_locator(
                "N43_rebuild_fr.tex:487", **authority_kwargs
            ),
            "target-only locator was accepted as source provenance",
        )
        require(
            not has_strong_source_locator(
                "R823_ES:C:\\workspace\\work\\spanish\\cum_es.tex:14774; "
                f"sha256={'B' * 64}",
                **authority_kwargs,
            ),
            "hash-pinned Spanish target locator was accepted as source provenance",
        )
        require(
            not has_strong_source_locator(
                "R823 chapters on ideal theory", **authority_kwargs
            ),
            "vague R823 citation was accepted as source provenance",
        )
        require(
            not has_strong_source_locator(
                "working/r823_fr/post43/book_intro_ch01_fr.tex:17",
                **authority_kwargs,
            ),
            "target post43 path was accepted as source provenance",
        )
        require(
            not has_strong_source_locator(
                "Production directe R823 book_ch05_ch06_fr.tex:840",
                **authority_kwargs,
            ),
            "bare R823 plus target path was accepted as source provenance",
        )
        require(
            not has_strong_source_locator(
                "Noether_R823_cum_de.tex lines 999999--1000000",
                **authority_kwargs,
            ),
            "out-of-range authority lines were accepted",
        )
        require(
            not has_strong_source_locator(
                "fabricated_nonexistent.pdf, p. 999999", **authority_kwargs
            ),
            "nonexistent out-of-range PDF locator was accepted",
        )
        require(
            not has_strong_source_locator(
                "Noether_R823_cum_de.tex lines 100--110; "
                f"sha256={'F' * 64}",
                **authority_kwargs,
            ),
            "wrong authority SHA was accepted",
        )
        require(
            not meaningful_review_text("pass " * 20),
            "repeated filler was accepted as meaningful review text",
        )
        require(
            meaningful_review_text(
                "Direct visual review covered every rendered page and confirmed "
                "legible formulas, stable margins, intact notes, and no clipping."
            ),
            "substantive visual review text was rejected",
        )

        parsed_pages, page_error = exact_page_spec("1-3, 5", 5)
        require(
            page_error is None and parsed_pages == {1, 2, 3, 5},
            f"exact page parser failed: {page_error}",
        )
        _, bad_page_error = exact_page_spec("pages 1-5", 5)
        require(bad_page_error is not None, "free-form page prose was accepted")
        _, overflow_error = exact_page_spec("1-6", 5)
        require(overflow_error is not None, "out-of-range page coverage was accepted")

        # A manifest image must be a fresh-pixel match for the actual candidate
        # PDF, not merely a hashed arbitrary image that repeats the PDF hash.
        from PIL import Image, ImageDraw  # type: ignore

        fixture_pdf = temp / "render-fixture.pdf"
        fixture_image = Image.new("RGB", (700, 900), "white")
        fixture_draw = ImageDraw.Draw(fixture_image)
        fixture_draw.rectangle((70, 90, 630, 810), outline="black", width=8)
        fixture_draw.line((100, 180, 600, 720), fill="black", width=5)
        fixture_draw.line((600, 180, 100, 720), fill="black", width=5)
        fixture_image.save(fixture_pdf, "PDF", resolution=72)
        fixture_pdf_hash = file_sha256(fixture_pdf)
        fresh_pixels, poppler_version, fresh_errors = rerender_pdf_pixels(
            fixture_pdf,
            args.pdftoppm,
            1,
        )
        require(
            not fresh_errors and set(fresh_pixels) == {1},
            f"fresh one-page Poppler derivation failed: {fresh_errors}",
        )

        render_prefix = temp / "manifest-page"
        render_run = subprocess.run(
            [
                str(args.pdftoppm),
                "-f",
                "1",
                "-l",
                "1",
                "-r",
                "120",
                "-png",
                str(fixture_pdf),
                str(render_prefix),
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
            check=False,
        )
        render_candidates = list(temp.glob("manifest-page-*.png"))
        require(
            render_run.returncode == 0 and len(render_candidates) == 1,
            f"manifest fixture render failed: {render_run.stderr or render_run.stdout}",
        )
        render = render_candidates[0]
        original_render_bytes = render.read_bytes()
        render_manifest = temp / "render_manifest.csv"
        manifest_rows = [
            {
                "page": "1",
                "render_path": render.name,
                "sha256": file_sha256(render),
                "pdf_sha256": fixture_pdf_hash,
                "renderer": PINNED_RENDER_PROFILE,
            }
        ]
        manifest_fields = ["page", "render_path", "sha256", "pdf_sha256", "renderer"]
        write_csv(render_manifest, manifest_fields, manifest_rows)
        _, rendered_pages, render_errors = bind_render_manifest(
            manifest_path=render_manifest,
            expected_pdf_hash=fixture_pdf_hash,
            expected_pages={1},
            expected_pixel_hashes=fresh_pixels,
        )
        require(
            rendered_pages == {1} and not render_errors,
            f"valid PDF-derived render manifest failed: {render_errors}",
        )
        render.write_bytes(render.read_bytes() + b"tamper")
        _, _, tamper_errors = bind_render_manifest(
            manifest_path=render_manifest,
            expected_pdf_hash=fixture_pdf_hash,
            expected_pages={1},
            expected_pixel_hashes=fresh_pixels,
        )
        require(tamper_errors, "tampered render file retained a passing binding")

        render.write_bytes(original_render_bytes)
        with Image.open(render) as valid_render:
            attack_size = valid_render.size
        arbitrary_pixels = Image.effect_noise(attack_size, 90).convert("RGB")
        arbitrary_pixels.save(render)
        manifest_rows[0]["sha256"] = file_sha256(render)
        write_csv(render_manifest, manifest_fields, manifest_rows)
        _, _, arbitrary_errors = bind_render_manifest(
            manifest_path=render_manifest,
            expected_pdf_hash=fixture_pdf_hash,
            expected_pages={1},
            expected_pixel_hashes=fresh_pixels,
        )
        require(
            any("do not derive" in error for error in arbitrary_errors),
            "arbitrary rehashed pixels retained a candidate-PDF derivation binding",
        )

        render.write_bytes(original_render_bytes)
        manifest_rows[0]["sha256"] = file_sha256(render)
        write_csv(render_manifest, manifest_fields, manifest_rows)
        pixel_binding = page_pixel_binding_sha256(fresh_pixels)
        visual_review = temp / "visual_review.json"
        valid_review = {
            "schema": VISUAL_REVIEW_SCHEMA,
            "status": "pass",
            "language": args.language,
            "reviewer_provenance": "Independent adversarial self-test visual reviewer record",
            "reviewed_at": "2026-07-18T05:30:00+02:00",
            "pdf_sha256": fixture_pdf_hash,
            "target_document_sha256": "D" * 64,
            "page_count": 1,
            "render_profile": PINNED_RENDER_PROFILE,
            "pdftoppm_sha256": file_sha256(args.pdftoppm),
            "reviewed_pages": "1",
            "baseline_kind": "reviewed-current-render",
            "baseline_render_manifest": render_manifest.name,
            "baseline_render_manifest_sha256": file_sha256(render_manifest),
            "baseline_pixel_binding_sha256": pixel_binding,
            "review_method": (
                "The reviewer inspected the complete derived page at original resolution, "
                "checking geometry, text regions, borders, and all visible marks against the fixture."
            ),
            "findings": (
                "The single candidate page is legible, complete, unclipped, and free of collisions, "
                "missing regions, malformed marks, or unexpected raster differences."
            ),
        }
        visual_review.write_text(
            json.dumps(valid_review, indent=2) + "\n", encoding="utf-8"
        )
        _, review_errors = bind_visual_review_record(
            visual_review,
            language=args.language,
            pdf_sha256=fixture_pdf_hash,
            target_document_sha256="D" * 64,
            page_count=1,
            pdftoppm_sha256=file_sha256(args.pdftoppm),
            full_manifest_path=render_manifest,
            expected_pixel_binding_sha256=pixel_binding,
        )
        require(not review_errors, f"valid visual review record failed: {review_errors}")

        stale_review = dict(valid_review)
        stale_review["baseline_render_manifest_sha256"] = "0" * 64
        visual_review.write_text(
            json.dumps(stale_review, indent=2) + "\n", encoding="utf-8"
        )
        _, stale_review_errors = bind_visual_review_record(
            visual_review,
            language=args.language,
            pdf_sha256=fixture_pdf_hash,
            target_document_sha256="D" * 64,
            page_count=1,
            pdftoppm_sha256=file_sha256(args.pdftoppm),
            full_manifest_path=render_manifest,
            expected_pixel_binding_sha256=pixel_binding,
        )
        require(stale_review_errors, "stale baseline manifest hash passed visual review binding")

        blank_reviewer = dict(valid_review)
        blank_reviewer["reviewer_provenance"] = ""
        visual_review.write_text(
            json.dumps(blank_reviewer, indent=2) + "\n", encoding="utf-8"
        )
        _, blank_reviewer_errors = bind_visual_review_record(
            visual_review,
            language=args.language,
            pdf_sha256=fixture_pdf_hash,
            target_document_sha256="D" * 64,
            page_count=1,
            pdftoppm_sha256=file_sha256(args.pdftoppm),
            full_manifest_path=render_manifest,
            expected_pixel_binding_sha256=pixel_binding,
        )
        require(blank_reviewer_errors, "blank reviewer passed visual review binding")

        wrong_pdf_review = dict(valid_review)
        wrong_pdf_review["pdf_sha256"] = "E" * 64
        visual_review.write_text(
            json.dumps(wrong_pdf_review, indent=2) + "\n", encoding="utf-8"
        )
        _, wrong_pdf_errors = bind_visual_review_record(
            visual_review,
            language=args.language,
            pdf_sha256=fixture_pdf_hash,
            target_document_sha256="D" * 64,
            page_count=1,
            pdftoppm_sha256=file_sha256(args.pdftoppm),
            full_manifest_path=render_manifest,
            expected_pixel_binding_sha256=pixel_binding,
        )
        require(wrong_pdf_errors, "wrong candidate PDF hash passed visual review binding")

        # Every routed record must bind the same final audit. Rehashing the
        # audit file is necessary but insufficient: its labeled live hashes
        # must also be parsed and compared semantically.
        support = temp / "final_audit.md"
        valid_audit_text = (
            "# Synthetic final audit\n\n"
            f"- Authority SHA-256: `{'B' * 64}`\n"
            f"- Expanded {args.language.title()} target SHA-256: `{'D' * 64}`\n"
            f"- Final PDF SHA-256: `{fixture_pdf_hash}`\n"
        )
        support.write_text(valid_audit_text, encoding="utf-8")
        support_hash = file_sha256(support)
        evidence_csv = temp / "unit_evidence.csv"
        evidence_rows: list[dict[str, str]] = []
        for unit in REQUIRED_UNITS:
            row = {field: "reviewed source-keyed content" for field in UNIT_EVIDENCE_FIELDS}
            row.update(
                {
                    "unit_id": unit,
                    "source_sha256": "B" * 64,
                    "target_sha256": "C" * 64,
                    "target_document_sha256": "D" * 64,
                    "supporting_artifacts": support.name,
                    "supporting_artifact_sha256": support_hash,
                    "status": "source-reconciled",
                }
            )
            evidence_rows.append(row)
        write_csv(evidence_csv, list(UNIT_EVIDENCE_FIELDS), evidence_rows)
        evidence_map = temp / "evidence_map.csv"
        map_rows = [
            {
                "unit_id": unit,
                "evidence_path": evidence_csv.name,
                "evidence_record": unit,
                "review_scope": "exact unit review",
                "notes": "adversarial binding fixture",
            }
            for unit in REQUIRED_UNITS
        ]
        write_csv(evidence_map, list(EVIDENCE_MAP_FIELDS), map_rows)
        _, record_count, _, evidence_errors = bind_unit_evidence(
            evidence_map,
            required_support_path=support,
        )
        require(
            record_count == 81 and not evidence_errors,
            f"valid direct evidence binding failed: {evidence_errors[:3]}",
        )
        audit_errors = bind_final_audit(
            support,
            language=args.language,
            authority_sha256="B" * 64,
            target_document_sha256="D" * 64,
            pdf_sha256=fixture_pdf_hash,
        )
        require(not audit_errors, f"valid semantic audit binding failed: {audit_errors}")

        stale_audit_text = valid_audit_text.replace(fixture_pdf_hash, "E" * 64)
        support.write_text(stale_audit_text, encoding="utf-8")
        _, _, _, support_tamper_errors = bind_unit_evidence(
            evidence_map,
            required_support_path=support,
        )
        require(
            support_tamper_errors,
            "tampered supporting artifact retained a passing binding",
        )

        # Close the outer-hash hole deliberately: refresh every declared file
        # hash after inserting a stale embedded PDF hash. Byte binding now
        # passes, while semantic audit binding must still reject the artifact.
        stale_support_hash = file_sha256(support)
        for row in evidence_rows:
            row["supporting_artifact_sha256"] = stale_support_hash
        write_csv(evidence_csv, list(UNIT_EVIDENCE_FIELDS), evidence_rows)
        _, _, _, refreshed_outer_errors = bind_unit_evidence(
            evidence_map,
            required_support_path=support,
        )
        require(
            not refreshed_outer_errors,
            f"refreshed outer support hashes unexpectedly failed: {refreshed_outer_errors[:3]}",
        )
        stale_semantic_errors = bind_final_audit(
            support,
            language=args.language,
            authority_sha256="B" * 64,
            target_document_sha256="D" * 64,
            pdf_sha256=fixture_pdf_hash,
        )
        require(
            stale_semantic_errors,
            "stale embedded audit PDF hash passed after its outer file hash was refreshed",
        )

        alternate_support = temp / "alternate_audit.md"
        alternate_support.write_text(valid_audit_text, encoding="utf-8")
        evidence_rows[0]["supporting_artifacts"] = alternate_support.name
        evidence_rows[0]["supporting_artifact_sha256"] = file_sha256(alternate_support)
        write_csv(evidence_csv, list(UNIT_EVIDENCE_FIELDS), evidence_rows)
        _, _, _, common_support_errors = bind_unit_evidence(
            evidence_map,
            required_support_path=support,
        )
        require(
            common_support_errors,
            "one unit omitted the required common final audit without rejection",
        )

        support.write_text(valid_audit_text, encoding="utf-8")
        support_hash = file_sha256(support)
        for row in evidence_rows:
            row["supporting_artifacts"] = support.name
            row["supporting_artifact_sha256"] = support_hash
        write_csv(evidence_csv, list(UNIT_EVIDENCE_FIELDS), evidence_rows)

        # The published parity CSV must be the byte-exact output of the pinned
        # promoter.  Recreate a fully substantive synthetic evidence corpus,
        # promote it, then prove that even a one-byte ledger edit is rejected.
        support.write_text(valid_audit_text, encoding="utf-8")
        support_hash = file_sha256(support)
        synthetic_whole_hash = "D" * 64
        seed_rows: list[dict[str, str]] = []
        promoter_evidence_rows: list[dict[str, str]] = []
        for index, unit in enumerate(REQUIRED_UNITS, start=1):
            source_hash = hashlib.sha256(f"source:{unit}".encode()).hexdigest().upper()
            target_hash = hashlib.sha256(f"target:{unit}".encode()).hexdigest().upper()
            seed_rows.append(
                {
                    "unit_id": unit,
                    "source_sha256": source_hash,
                    "target_sha256": target_hash,
                    "target_document_sha256": synthetic_whole_hash,
                    "status": "pending-review",
                    "review_evidence": "",
                    "notes": "",
                }
            )
            evidence_row = {field: "" for field in UNIT_EVIDENCE_FIELDS}
            evidence_row.update(
                {
                    "unit_id": unit,
                    "source_sha256": source_hash,
                    "target_sha256": target_hash,
                    "target_document_sha256": synthetic_whole_hash,
                    "source_locator": f"R823 cum_de.tex lines {1000 + index}--{1001 + index}",
                    "target_locator": f"synthetic_target.tex lines {2000 + index}--{2001 + index}",
                    "method": f"{unit}: exact source-to-target alignment with independent formula and prose collation.",
                    "reviewed_structures": f"{unit}: headings, numbered statements, paragraph sequence, displays, and cross-references were checked.",
                    "reviewed_formulas": f"{unit}: every displayed expression and its surrounding inline symbols were compared with the authority.",
                    "reviewed_notes": f"{unit}: source notes, anchors, attribution, and numbering were checked in context.",
                    "findings": f"{unit}: the synthetic record demonstrates a distinct, current-hash-keyed reconciliation finding.",
                    "reviewer_provenance": f"Codex adversarial self-test reviewer for exact unit {unit}.",
                    "supporting_artifacts": support.name,
                    "supporting_artifact_sha256": support_hash,
                    "status": "source-reconciled",
                }
            )
            promoter_evidence_rows.append(evidence_row)

        seed_ledger = temp / "seed.csv"
        write_csv(seed_ledger, list(seed_rows[0]), seed_rows)
        write_csv(evidence_csv, list(UNIT_EVIDENCE_FIELDS), promoter_evidence_rows)
        promoted_ledger = temp / "promoted.csv"
        completed = subprocess.run(
            [
                sys.executable,
                str(promoter),
                "--seed-ledger",
                str(seed_ledger),
                "--evidence-map",
                str(evidence_map),
                "--output-csv",
                str(promoted_ledger),
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=180,
            check=False,
        )
        require(
            completed.returncode == 0 and promoted_ledger.is_file(),
            f"synthetic canonical promotion failed: {completed.stderr or completed.stdout}",
        )
        promoter_ok, promoter_detail = run_exact_promoter(
            promoter=promoter,
            seed_ledger=seed_ledger,
            evidence_map=evidence_map,
            parity_ledger=promoted_ledger,
        )
        require(promoter_ok, f"byte-exact promoted ledger was rejected: {promoter_detail}")
        promoted_ledger.write_bytes(promoted_ledger.read_bytes() + b"\n")
        tampered_promoter_ok, _ = run_exact_promoter(
            promoter=promoter,
            seed_ledger=seed_ledger,
            evidence_map=evidence_map,
            parity_ledger=promoted_ledger,
        )
        require(
            not tampered_promoter_ok,
            "hand-edited parity ledger still matched the canonical promoter output",
        )

    print(f"PASS language={args.language}")
    print(f"expanded_dependencies={len(dependencies)}")
    print(f"target_document_sha256={rows[0].target_document_sha256}")
    print(
        "probes=preamble_hash,comment_mask,heading_context,input_parser,"
        "strict_source_locator,page_coverage,render_hash,poppler_pdf_derivation,"
        "visual_review_binding,direct_evidence_support_hash,"
        "final_audit_semantic_hash,canonical_promoter_byte_exact"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
