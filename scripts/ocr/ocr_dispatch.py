#!/usr/bin/env python3
"""Modular OCR dispatcher — thin glue over existing open-source engines, each in its own env.

Route (image, content_type) -> the right tool. Reusable across every work and script:
math, Chinese/Japanese/Devanagari/Cyrillic/Latin text, historical/abjad print, tables/layout.
Each engine runs in an ISOLATED environment (so their torch/deps never clobber each other or ours).

  from ocr_dispatch import dispatch
  dispatch("page.png", "math")          # -> Markdown with LaTeX
  dispatch("eq.png",   "math_equation") # -> LaTeX for one cropped equation
  dispatch("page.png", "multilingual")  # -> text (CJK/Arabic/Devanagari/...)
  dispatch("leaf.png", "historical", model="albattani_abjad")  # trainable Kraken model
  dispatch("page.png", "layout")        # -> document structure / tables

Engines and why (see LESSONS_LEARNED.md):
  pix2text  integrated layout+tables+math(LaTeX)+multilingual text  -> Markdown (Mathpix alt)
  pix2tex   single cropped equation -> LaTeX (~88% exact match)
  surya     printed multilingual OCR, 90+ scripts, layout + reading order
  kraken    TRAINABLE OCR for historical/abjad/Sanskrit print (train per typeface on hand-read lines)
  docling   document structure / table extraction
General VLMs are deliberately NOT here for numerals: they read prose but hallucinate abjad numbers.
"""
import os, sys, json, subprocess, tempfile
from pathlib import Path

OCR_PY = os.environ.get("OCR_TOOL_PYTHON") or str(
    Path.home() / "ocr_env" / "Scripts" / "python.exe"
)   # isolated OCR-toolkit venv; override with OCR_TOOL_PYTHON

ENGINES = {
    "math":          {"tool": "pix2text", "env": OCR_PY},
    "multilingual":  {"tool": "surya",    "env": OCR_PY},
    "math_equation": {"tool": "pix2tex",  "env": OCR_PY},
    "historical":    {"tool": "kraken",   "env": OCR_PY},   # train per print; see train recipe in LESSONS
    "layout":        {"tool": "docling",  "env": OCR_PY},
}

def _run(env_py, code, img, extra=""):
    """Run a tiny inline script in the engine's env; return stdout text."""
    r = subprocess.run([env_py, "-c", code, img, extra], capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        raise RuntimeError(f"engine failed: {r.stderr[-800:]}")
    return r.stdout.strip()

_PIX2TEXT = (
    "import sys; from pix2text import Pix2Text; p=Pix2Text.from_config();"
    "r=p.recognize(sys.argv[1], return_text=True);"
    "print(r if isinstance(r,str) else str(r))"
)
_PIX2TEX = (
    "import sys; from PIL import Image; from pix2tex.cli import LatexOCR;"
    "print(LatexOCR()(Image.open(sys.argv[1])))"
)
_SURYA = (
    "import sys; from PIL import Image; from surya.recognition import RecognitionPredictor;"
    "from surya.detection import DetectionPredictor;"
    "img=Image.open(sys.argv[1]); det=DetectionPredictor(); rec=RecognitionPredictor();"
    "res=rec([img], det_predictor=det);"
    "print('\\n'.join(l.text for l in res[0].text_lines))"
)
_DOCLING = (
    "import sys; from docling.document_converter import DocumentConverter;"
    "print(DocumentConverter().convert(sys.argv[1]).document.export_to_markdown())"
)

def dispatch(image_path, content_type="math", model=None):
    if content_type not in ENGINES:
        raise ValueError(f"unknown content_type {content_type!r}; choose {list(ENGINES)}")
    eng = ENGINES[content_type]; py = eng["env"]
    if eng["tool"] == "pix2text":      return _run(py, _PIX2TEXT, image_path)
    if eng["tool"] == "pix2tex":       return _run(py, _PIX2TEX, image_path)
    if eng["tool"] == "surya":         return _run(py, _SURYA, image_path)
    if eng["tool"] == "docling":       return _run(py, _DOCLING, image_path)
    if eng["tool"] == "kraken":
        # trainable engine: needs a model fitted to the print. See LESSONS_LEARNED "Kraken" recipe.
        m = model or "<train a model per typeface first>"
        raise NotImplementedError(f"kraken model '{m}' not wired yet; train on hand-read lines then add `kraken ocr -m <model>` here")
    raise RuntimeError("unreachable")

if __name__ == "__main__":
    img = sys.argv[1]; ct = sys.argv[2] if len(sys.argv) > 2 else "math"
    print(dispatch(img, ct))
