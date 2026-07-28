#!/usr/bin/env python3
"""Build compact SGA3 native-diagram working packages for XX and XXI."""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
BASE_PATH = SCRIPT_DIR / "build_sga3_native_batch_xii_xix_xxv_20260728.py"
SPEC = importlib.util.spec_from_file_location("sga3_native_builder", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load the established SGA3 package builder")
base = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = base
SPEC.loader.exec_module(base)


base.PUBLIC_DOCS = (
    "README.md",
    "PROVENANCE_AND_RIGHTS.md",
    "PUBLICATION_READINESS.md",
    "BUILD_SUMMARY_PUBLIC.md",
    "FINAL_VISUAL_QA.md",
    "INDEPENDENT_ARCHIVE_REBUILD_PASS.md",
    "NATIVE_DIAGRAM_INVENTORY.csv",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--working-root", type=Path, required=True)
    parser.add_argument("--rebuild-root", type=Path, required=True)
    parser.add_argument("--render-root", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--lane-control", type=Path, required=True)
    return parser.parse_args()


def units(rebuild_root: Path) -> tuple[base.Unit, ...]:
    return (
        base.Unit(
            key="xx",
            producer_dir="sga3_exposeXX_native_diagram_loop2_successor_r1_20260728",
            producer_pdf=str((rebuild_root / "xx" / "public.pdf").resolve()),
            rebuild_pdf=str((rebuild_root / "xx" / "rebuild.pdf").resolve()),
            master="tex/SGA3_Expose_XX_English.tex",
            output_dir="sources/sga/sga3-expose-xx-native-loop1-working-20260728",
            pdf_name=(
                "00c20_SGA3_Expose_XX_English_"
                "NativeDiagram_Loop1_Working_20260728.pdf"
            ),
            tex_name=(
                "02c20_SGA3_Expose_XX_English_"
                "NativeDiagram_Loop1_Working_20260728.tex"
            ),
            zip_name=(
                "10c20_SGA3_Expose_XX_"
                "NativeDiagram_Loop1_Source_20260728.zip"
            ),
            receipt_name="LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md",
            receipt_source=(
                "qa/native_redo_20260728/"
                "LEAD_NATIVE_DIAGRAM_5000DPI_REVIEW_PASS.md"
            ),
            expected_receipt=(
                7_285,
                "FFC53ED499F7D2A66109EBC2C0AEB1225FA034C01F06A190D4DAEC9278C374E4",
            ),
            expected_producer_pdf=(
                236_958,
                "0AFA79FC6140B72814EB0BA03191709C1CFC718F5CE0485AD8151E103FD1AB15",
            ),
            expected_rebuild_pdf=(
                236_959,
                "32DE912D94FA54DEE81119C5E60CEC260013D43FCE217CF59284285D3DDC5A72",
            ),
            expected_tex_count=19,
            expected_tex_aggregate=(
                2_415,
                "DE39053894B09CE285BD3CB5FEAC4DDD72A276F548BEBB7165F6878F26E69992",
            ),
            expected_metrics={
                "pages": 41,
                "named_destinations": 327,
                "internal_goto_actions": 46,
                "linked_pages": 28,
                "invalid_actions": 0,
                "uri_actions": 0,
                "font_resources": 30,
                "type3_fonts": 0,
                "raster_xobjects": 0,
            },
            expected_tikzcd=8,
            expected_tikzpicture=3,
            expected_atomic_panels=10,
            scope="complete SGA3 Expose XX only",
            authority_pages="local 1-35 / combined 1060-1094",
            next_cursor="Expose XXI local 1 / combined 1095",
            authority_file="Exp20-13oct24.pdf",
            authority_bytes=332_777,
            authority_sha256=(
                "9B8B790E1F07EA4B6E07DA98A2ABAE048A8D40648A8F7C5EC909EA73B92411FA"
            ),
            visual_pages=(1, 2, 8, 22, 28, 31, 35, 36, 41),
        ),
        base.Unit(
            key="xxi",
            producer_dir=(
                "sga3_exposeXXI_native_diagram_loop2_successor_r1_20260728"
            ),
            producer_pdf=str((rebuild_root / "xxi" / "public.pdf").resolve()),
            rebuild_pdf=str(
                (rebuild_root / "xxi" / "rebuild.pdf").resolve()
            ),
            master="tex/SGA3_Expose_XXI_English.tex",
            output_dir=(
                "sources/sga/sga3-expose-xxi-native-loop1-working-20260728"
            ),
            pdf_name=(
                "00c21_SGA3_Expose_XXI_English_"
                "NativeDiagram_Loop1_Working_20260728.pdf"
            ),
            tex_name=(
                "02c21_SGA3_Expose_XXI_English_"
                "NativeDiagram_Loop1_Working_20260728.tex"
            ),
            zip_name=(
                "10c21_SGA3_Expose_XXI_"
                "NativeDiagram_Loop1_Source_20260728.zip"
            ),
            receipt_name="LEAD_NATIVE_HIGHZOOM_BUILD_PASS_20260728.md",
            receipt_source=(
                "qa/native_redo_20260728/"
                "LEAD_NATIVE_HIGHZOOM_BUILD_PASS_20260728.md"
            ),
            expected_receipt=(
                4_858,
                "4C61009D50FBACFDCA2B486A25C1414F34DD17FF546CA6103DF230B9B0A63DA6",
            ),
            expected_producer_pdf=(
                295_397,
                "A1C58F35B3AA2D29C02A9953B569295ACB0574786728432DD3D726E9F143F0D0",
            ),
            expected_rebuild_pdf=(
                295_397,
                "3F7926662ADE0DA876772E45EC80484F956DF4249CD45428A2AB60D29CF27111",
            ),
            expected_tex_count=41,
            expected_tex_aggregate=(
                5_491,
                "9300E6BE2A9F8F2A788894CFDBF8E93B6F609CD08E554EBBE53ADC7E6E30E4DF",
            ),
            expected_metrics={
                "pages": 56,
                "named_destinations": 378,
                "internal_goto_actions": 240,
                "linked_pages": 53,
                "invalid_actions": 0,
                "uri_actions": 0,
                "font_resources": 32,
                "type3_fonts": 0,
                "raster_xobjects": 0,
            },
            expected_tikzcd=9,
            expected_tikzpicture=2,
            expected_atomic_panels=11,
            scope="complete SGA3 Expose XXI only",
            authority_pages="local 1-46 / combined 1095-1140",
            next_cursor="Expose XXII local 1 / combined 1141",
            authority_file="Exp21-13oct24.pdf",
            authority_bytes=392_935,
            authority_sha256=(
                "1FB0720FFD496E6076DBEC3702CBD3CBA828C2BAAE0340A840855DF86A496284"
            ),
            visual_pages=(1, 2, 31, 33, 40, 44, 54, 56),
        ),
    )


def write_inventory(
    unit: base.Unit,
    working_root: Path,
    lane_control: Path,
    repo_root: Path,
) -> None:
    output = repo_root / unit.output_dir / "NATIVE_DIAGRAM_INVENTORY.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    if unit.key == "xx":
        source = (
            lane_control / "SGA3_SESSION_C_NATIVE_DIAGRAM_REDO_INVENTORY_20260728.csv"
        )
        with source.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = [
                row
                for row in csv.DictReader(handle)
                if row.get("expose") == "XX"
            ]
        if len(rows) != 10:
            raise RuntimeError("Expected ten Expose-XX inventory rows")
        fields = list(rows[0])
    else:
        source = (
            working_root
            / unit.producer_dir
            / "controls"
            / "SGA3_EXPOSE_XXI_NATIVE_DIAGRAM_INVENTORY_20260728.csv"
        )
        with source.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            fields = list(reader.fieldnames or ())
        if len(rows) != 11:
            raise RuntimeError("Expected eleven Expose-XXI inventory rows")
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    args = parse_args()
    working_root = args.working_root.resolve()
    rebuild_root = args.rebuild_root.resolve()
    render_root = args.render_root.resolve()
    repo_root = args.repo_root.resolve()
    lane_control = args.lane_control.resolve()
    selected = units(rebuild_root)
    for unit in selected:
        write_inventory(
            unit,
            working_root,
            lane_control,
            repo_root,
        )
    results = [
        base.build_unit(
            unit,
            working_root,
            rebuild_root,
            render_root,
            repo_root,
        )
        for unit in selected
    ]
    status = (
        "PASS" if all(row["status"] == "PASS" for row in results) else "FAIL"
    )
    print(json.dumps({"status": status, "units": results}, indent=2))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
