from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEED = ROOT / "curation" / "ROMANCE_BRANCH_ROUTE_SEED_v1.csv"
CORPUS = ROOT / "corpus" / "ROMANCE_CONSOLIDATED_CORPUS_v2.csv"
OUT = ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v1.csv"
SUMMARY = ROOT / "corpus" / "ROMANCE_BRANCH_ROUTING_LEDGER_v1.json"
LOG = ROOT / "qa" / "BRANCH_ROUTING_BUILD_v1.log"


def read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


seed = read_csv(SEED)
corpus = read_csv(CORPUS)
rows = []
for route in seed:
    key = route["corpus_language_key"]
    active = [r for r in corpus if key and r["language"] == key and r["counting_eligible"] == "true"]
    licenses = sorted({r["license_status"] for r in active})
    if active:
        evidence_status = "active_substantive_body_present"
        gap_reason = ""
    elif route["scope_status"] == "historical_diachronic":
        evidence_status = "explicit_zero_historical_source_gap"
        gap_reason = route["gap_reason"]
    elif route["scope_status"] == "contact_comparator":
        evidence_status = "explicit_zero_contact_comparator_gap"
        gap_reason = route["gap_reason"]
    else:
        evidence_status = "explicit_zero_body_gap"
        gap_reason = route["gap_reason"]
    row = dict(route)
    row.update(
        current_active_body_count=str(len(active)),
        current_active_bytes=str(sum(int(r["bytes"]) for r in active)),
        current_domains=";".join(sorted({tag for r in active for tag in r["domain_tags"].split(";") if tag})),
        current_license_status=";".join(licenses) if licenses else "no_active_source",
        evidence_status=evidence_status,
        gap_reason=gap_reason,
        corpus_manifest_sha256=sha(CORPUS),
        review_status="route_implemented_20260717_needs_source_acquisition" if not active else "route_implemented_active_corpus",
    )
    rows.append(row)

fields = list(rows[0])
with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

summary = {
    "artifact": "ROMANCE_BRANCH_ROUTING_LEDGER_v1",
    "route_count": len(rows),
    "active_routes": sum(r["current_active_body_count"] != "0" for r in rows),
    "explicit_zero_routes": sum(r["current_active_body_count"] == "0" for r in rows),
    "macrobranches": sorted({r["macrobranch"] for r in rows}),
    "gallo_italic_routes": [r["variety_name"] for r in rows if r["subbranch"] == "Gallo-Italic"],
    "istriot_route_present": any(r["variety_code"] == "ist" for r in rows),
    "romansh_active_body_count": next(r["current_active_body_count"] for r in rows if r["variety_code"] == "rm-rg"),
    "dominant_standard_proxy_violations": sum(r["dominant_standard_not_proxy"] != "true" for r in rows),
    "corpus_manifest_sha256": sha(CORPUS),
    "ledger_sha256": sha(OUT),
}
SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

assert len({r["route_id"] for r in rows}) == len(rows)
assert len({r["variety_code"] for r in rows}) == len(rows)
assert summary["istriot_route_present"]
assert set(summary["gallo_italic_routes"]) >= {"Piedmontese", "Lombard", "Ligurian", "Emilian-Romagnol"}
assert summary["romansh_active_body_count"] == "1"
assert summary["dominant_standard_proxy_violations"] == 0

lines = [
    f"PASS routes={len(rows)}",
    f"active_routes={summary['active_routes']}",
    f"explicit_zero_routes={summary['explicit_zero_routes']}",
    "romansh_active_bodies=1",
    "romansh_specialist_algebra_bodies=0",
    f"ledger_sha256={summary['ledger_sha256']}",
]
LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
