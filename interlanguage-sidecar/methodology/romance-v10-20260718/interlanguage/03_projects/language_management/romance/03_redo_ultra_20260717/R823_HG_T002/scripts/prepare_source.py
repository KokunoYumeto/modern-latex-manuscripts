from __future__ import annotations

import hashlib
import json
from pathlib import Path

T = Path(__file__).resolve().parent.parent
AUTHORITY = Path(r"C:\Users\Floris\Documents\interlanguage\03_projects\language_management\romance\02_r823_romance_translation_20260717\authority_extract\pkg_r823\Noether_R823_WebB_R822_P20p27_31_RunInDashRefine_20260717\1\01_cumulative\Noether_R823_cum_de.tex")
AUTHORITY_SHA256 = "EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21"
START, END = 21089, 21097


def sha_bytes(data: bytes):
    return hashlib.sha256(data).hexdigest().upper()


raw = AUTHORITY.read_bytes()
assert sha_bytes(raw) == AUTHORITY_SHA256
text = raw.decode("utf-8")
lines = text.splitlines()
selected = lines[START - 1 : END]
assert selected[0].startswith(r"\subsection*{§ 2. Darstellungsklassen}")
assert "Klasse von reziproken Darstellungen" in selected[-1]

exact = ("\n".join(selected) + "\n").encode("utf-8")
exact_path = T / "source" / "R823_HG_T002_de_exact.tex"
numbered_path = T / "source" / "R823_HG_T002_de_numbered.txt"
exact_path.write_bytes(exact)
numbered_path.write_text("\n".join(f"{number}: {lines[number - 1]}" for number in range(START, END + 1)) + "\n", encoding="utf-8")

manifest = {
    "artifact": "R823_HG_T002_SOURCE_MANIFEST",
    "authority_path": str(AUTHORITY),
    "authority_sha256": AUTHORITY_SHA256,
    "line_start": START,
    "line_end": END,
    "exact_slice_sha256": sha_bytes(exact),
    "exact_slice_bytes": len(exact),
    "next_line": 21099,
    "next_heading": "§ 3. Darstellungsmoduln",
}
(T / "source" / "R823_HG_T002_SOURCE_MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(manifest, ensure_ascii=False, indent=2))
