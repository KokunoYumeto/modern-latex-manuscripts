from __future__ import annotations

import hashlib
import json
from pathlib import Path

from pypdf import PdfReader


HERE = Path(__file__).resolve().parent
PDF = HERE / "reader.pdf"
OUTPUT = HERE / "reader.txt"

reader = PdfReader(str(PDF))
pages = [(page.extract_text() or "") for page in reader.pages]
text = "\n\f\n".join(pages) + "\n"
raw = text.encode("utf-8")
OUTPUT.write_bytes(raw)
normalized = "".join(text.split())
p09 = "".join(pages[91:103])
p09_normalized = "".join(p09.split())

result = {
    "extract_id": "ZHCHK-CUM-R3-TEXT-001",
    "extractor": "pypdf",
    "pages": len(pages),
    "text": {
        "path": OUTPUT.name,
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest().upper(),
    },
    "whole_reader": {
        "mixed_wen_ti": text.count("问題"),
        "traditional_ti": text.count("題"),
    },
    "p09_pages": [92, 103],
    "p09_gates": {
        "title_present": "由整超越数构成的最一般领域" in p09_normalized,
        "zermelo_434_present": "Zermelo" in p09 and "434" in p09,
        "algebraic_basis_residual": p09_normalized.count("代数基"),
        "basis_number_residual": p09_normalized.count("基数"),
        "degree_error_residual": sum(
            p09_normalized.count(term) for term in ("最低维", "零维项")
        ),
        "correct_transcendence_basis": p09_normalized.count("超越基"),
        "correct_maximal_subring": p09_normalized.count("最大公子环"),
        "correct_proper_subdomain": p09_normalized.count("真子整环"),
    },
}
result["all_pass"] = (
    len(pages) == 413
    and result["whole_reader"]["mixed_wen_ti"] == 0
    and result["whole_reader"]["traditional_ti"] == 0
    and result["p09_gates"]["title_present"]
    and result["p09_gates"]["zermelo_434_present"]
    and result["p09_gates"]["algebraic_basis_residual"] == 0
    and result["p09_gates"]["basis_number_residual"] == 0
    and result["p09_gates"]["degree_error_residual"] == 0
    and result["p09_gates"]["correct_transcendence_basis"] >= 41
    and result["p09_gates"]["correct_maximal_subring"] == 3
    and result["p09_gates"]["correct_proper_subdomain"] == 4
)
if not result["all_pass"]:
    raise SystemExit(json.dumps(result, ensure_ascii=False, indent=2))
print(json.dumps(result, ensure_ascii=False, indent=2))
