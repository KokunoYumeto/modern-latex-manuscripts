#!/usr/bin/env python3
"""Non-TeX regression checks for the D020 V5 lacets insertion repair."""

import importlib.util
import json
import pathlib
import sys

sys.dont_write_bytecode = True
ROOT = pathlib.Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location(
    "d020_build_math_readers", ROOT / "tools" / "build_math_readers.py"
)
builder = importlib.util.module_from_spec(spec)
saved_argv = sys.argv
try:
    sys.argv = [str(ROOT / "tools" / "build_math_readers.py"), str(ROOT)]
    spec.loader.exec_module(builder)
finally:
    sys.argv = saved_argv


def record(layer: str, page: int) -> dict:
    path = ROOT / "edition" / f"{layer}.ndjson"
    records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
    return next(item for item in records if item["physical_page"] == page)


def check_reader_layer(layer: str) -> None:
    item = record(layer, 19)
    asset = item["assets"][0]
    marker = asset["placement_after"]
    paragraph = next(part for part in item["text"].split("\n\n") if marker in part)

    builder.LAYER = layer
    builder.PAGE = 19
    assert builder.labelled_prose(paragraph) is not None

    rendered = builder.record_text(item)
    filename = pathlib.PurePosixPath(asset["presentation_path"]).name
    command = rf"\includegraphics[width=.73\linewidth]{{{filename}}}"
    assert rendered.count(command) == 1
    assert rendered.index(command) > rendered.index(r"\textbf{(5.2)}")


for reader_layer in ("source_language", "english_standalone"):
    check_reader_layer(reader_layer)

builder.LAYER = "apparatus"
builder.PAGE = 19
assert r"\includegraphics" not in builder.record_text(record("apparatus", 19))

print(
    json.dumps(
        {
            "result": "PASS",
            "layers": ["source_language", "english_standalone"],
            "asset": "P0019-A01",
            "branch": "labelled_prose",
            "apparatus_insertion_count": 0,
        },
        sort_keys=True,
    )
)
