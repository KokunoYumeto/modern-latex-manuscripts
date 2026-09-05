#!/usr/bin/env python3
import csv
import hashlib
import json
import pathlib
import sys
from datetime import datetime, timezone


ROOT = pathlib.Path(sys.argv[1]).resolve()
assert ROOT.name == "S06_math_v4"


def canonical(record):
    return json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest().upper()


def load(layer):
    return [
        json.loads(line)
        for line in (ROOT / "edition" / f"{layer}.ndjson").read_text(encoding="utf-8").splitlines()
    ]


source = load("source_language")
english = load("english_standalone")
apparatus = load("apparatus")
page = 26
src = source[page - 1]
eng = english[page - 1]
app = apparatus[page - 1]

assert len(src["objects"]) == 8
assert len(eng["objects"]) == 8
assert src["objects"][-1] == eng["objects"][-1] == {
    "disposition": "EXCLUDE_BODY_RETAIN_PROVENANCE",
    "id": "P0026-O08",
    "kind": "printer_signature_38",
}
assert app["objects_disposed"] == 7
assert "printer signature 38" in app["text"] and "P0026-O08" in app["text"]
old_record = canonical(app)
old_sha = digest_text(old_record)

with (ROOT / "coverage" / "coverage.tsv").open(encoding="utf-8", newline="") as handle:
    coverage = list(csv.DictReader(handle, delimiter="\t"))
assert len(coverage) == 36
assert coverage[page - 1]["record_sha256_apparatus"] == old_sha

app["objects_disposed"] = 8
new_record = canonical(app)
new_sha = digest_text(new_record)
assert new_sha != old_sha
coverage[page - 1]["record_sha256_apparatus"] = new_sha

(ROOT / "edition" / "apparatus.ndjson").write_text(
    "\n".join(canonical(record) for record in apparatus) + "\n", encoding="utf-8"
)
with (ROOT / "coverage" / "coverage.tsv").open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(coverage[0]), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(coverage)

receipt = {
    "schema": "d020-apparatus-metadata-v8-repair-v1",
    "status": "REPAIRED_NOT_YET_COLD_AUDITED",
    "created_at_utc": datetime.now(timezone.utc).isoformat(),
    "authority_physical_page": page,
    "printed_page": 297,
    "finding": "V3 A10 apparatus objects_disposed remained 7 after P0026-O08 was added to source and English inventories.",
    "repair": "Set apparatus objects_disposed to 8; apparatus prose, source and English records were unchanged.",
    "source_object_count": len(src["objects"]),
    "english_object_count": len(eng["objects"]),
    "apparatus_objects_disposed_before": 7,
    "apparatus_objects_disposed_after": app["objects_disposed"],
    "apparatus_record_sha256_before": old_sha,
    "apparatus_record_sha256_after": new_sha,
    "coverage_apparatus_sha256_after": coverage[page - 1]["record_sha256_apparatus"],
    "scholarly_text_changed": False,
    "source_language_changed": False,
    "english_changed": False,
    "pdf_rebuild_required": False,
    "reason_pdf_rebuild_not_required": "The repair changes apparatus provenance metadata only; all three TeX sources and all three PDFs are byte-identical presentation products of unchanged record text.",
}
(ROOT / "audit" / "FINAL_APPARATUS_V8_REPAIR.json").write_text(
    json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
(ROOT / "audit" / "V4_REPAIR_LOG.md").write_text(
    "# D020 V4 repair log\n\n"
    "STATUS: REPAIRED_NOT_YET_COLD_AUDITED.\n\n"
    "V3 remains immutable and adverse under `audit_cold/S06_math_v3_01`; its finding A10 proves that physical page 26 had eight source/English objects while the apparatus declared seven dispositions. V4 changes only `apparatus.ndjson` page 26 from `objects_disposed: 7` to `objects_disposed: 8` and updates that one apparatus canonical hash in `coverage.tsv`. Scholarly text, source/English records, authority, images, TeX, HTML and PDFs are unchanged.\n\n"
    f"Old apparatus canonical SHA-256: `{old_sha}`. New apparatus canonical SHA-256: `{new_sha}`.\n\n"
    "Next action: validate V4, confirm byte identity of all unchanged presentation products, freeze a new immutable subject, and run a fresh nonpatching whole-paper cold audit.\n",
    encoding="utf-8",
)
print(json.dumps(receipt, ensure_ascii=False, indent=2))
