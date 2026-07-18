from __future__ import annotations

import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
BASE_PATH = HERE / "verify_pdf_renders_v8.py"
SPEC = importlib.util.spec_from_file_location("romance_render_v8_base", BASE_PATH)
assert SPEC is not None and SPEC.loader is not None
base = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(base)

# Preserve every earlier verifier and extend the live assurance surface through
# the complete T006 theorem-two tranche.
base.__file__ = __file__
base.OUT = base.ROOT / "qa" / "PDF_RENDER_REPRODUCIBILITY_v10.json"
base.TRANCHES = (
    ("R823_HG_T001", 3),
    ("R823_HG_T002", 2),
    ("R823_HG_T003", 2),
    ("R823_HG_T004", 2),
    ("R823_HG_T005", 3),
    ("R823_HG_T006", 3),
)


def main() -> None:
    base.main()
    report = json.loads(base.OUT.read_text(encoding="utf-8"))
    report["artifact"] = "PDF_RENDER_REPRODUCIBILITY_v10"
    report["supersedes"] = "PDF_RENDER_REPRODUCIBILITY_v9"
    report["successor_scope"] = (
        "Adds the complete T006 three-page theorem-two tranche; "
        "T001–T005 identities remain unchanged."
    )
    report["renderer"]["temporary_directory_policy"] = (
        "One isolated TemporaryDirectory per tranche under tmp/pdfs; "
        "automatically removed after comparison. Internal prefixes retain the audited v8 base name."
    )
    serialized = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    base.OUT.write_text(serialized, encoding="utf-8", newline="\n")
    print(serialized, end="")


if __name__ == "__main__":
    main()
