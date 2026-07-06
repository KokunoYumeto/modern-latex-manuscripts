# Master marker table v3.3: merge CJK (ja/zh_hans/ko) + sense-audited Arabic +
# Turkish Noether block into the whole interlanguage map as sourcebody_internal_candidate.
# Confirmed-only for CJK; adverse rows carried; boundaries preserved.
import csv
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
BASE = Path(r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704")
V8 = BASE / "user made flr with chat web stuff" / "otherpc_v8"
F81 = V8 / "OTHERPC_CJK_ARABIC_FILL_PASS_v8_1_20260705"
F82 = V8 / "CJK_ARABIC_SENSE_AUDIT_PASS_v8_2_20260705"

mt = json.loads((BASE / "INTERLINGUAL_MARKER_TABLE_v3_2_20260704.json").read_text(encoding="utf-8"))
cjk = list(csv.DictReader((F81 / "CJK_LANE_MARKER_TABLE_v1_CHATGPT_20260705.csv").open(encoding="utf-8-sig")))
cjk_audit = json.loads((F82 / "CJK_SOURCEBODY_SENSE_AUDIT_v1_20260705.json").read_text(encoding="utf-8-sig"))
ar_ctrl = json.loads((F82 / "CONTROLLED_ARABIC_C2_FILL_LEDGER_v2_1_SENSE_AUDITED_20260705.json").read_text(encoding="utf-8-sig"))
tr = list(csv.DictReader((F81 / "TURKISH_NOETHER_BLOCK_INTEGRATION_v1_20260705.csv").open(encoding="utf-8-sig")))

confirmed = {r["concept"].lower() for r in cjk_audit if r["sense_status"] == "confirmed_sourcebody_internal"}
review = {r["concept"].lower(): r["sense_status"] for r in cjk_audit if r["sense_status"] in ("sense_review_candidate", "low_count_candidate")}
cjk_by = {r["concept"].lower(): r for r in cjk}

ar_rows = ar_ctrl.get("rows") or ar_ctrl if isinstance(ar_ctrl, list) else ar_ctrl.get("rows", [])
ar_by = {}
for r in (ar_rows or []):
    c = str(r.get("concept", "")).lower()
    if c:
        ar_by[c] = r

by_concept = {row["concept"].lower(): row for row in mt["rows"]}
stats = {"cjk_confirmed": 0, "cjk_review": 0, "ar_updated": 0, "tr_rows": 0, "cjk_concepts_not_in_master": []}

for c, r in cjk_by.items():
    tgt = by_concept.get(c)
    if not tgt:
        if c in confirmed:
            stats["cjk_concepts_not_in_master"].append(c)
        continue
    if c in confirmed:
        tgt["ja"] = r.get("ja_form") or ""
        tgt["zh_hans"] = r.get("zh_hans_form") or ""
        tgt["ko"] = r.get("ko_form") or ""
        tgt["cjk_status"] = "sourcebody_internal_candidate (sense-audited v8.2)"
        tgt["cjk_evidence"] = f"ja:{r.get('ja_hit_count','0')}/{r.get('ja_file_count','0')}f zh:{r.get('zh_hans_hit_count','0')}/{r.get('zh_hans_file_count','0')}f ko:{r.get('ko_hit_count','0')}/{r.get('ko_file_count','0')}f"
        stats["cjk_confirmed"] += 1
    elif c in review:
        tgt["cjk_status"] = review[c]
        stats["cjk_review"] += 1

for c, r in ar_by.items():
    tgt = by_concept.get(c)
    if not tgt:
        continue
    st = str(r.get("status") or r.get("sense_status") or "")
    if st:
        tgt["ar_sourcebody_status"] = st
        stats["ar_updated"] += 1
    if "reject" in st or "collision" in str(r.get("note", "")):
        tgt["ar_adverse_note"] = str(r.get("note", ""))[:160]

# Turkish Noether block: side-channel column on matching concepts (draft/non-canonical)
for r in tr:
    c = str(r.get("concept", "")).lower()
    tgt = by_concept.get(c)
    if tgt:
        tgt["tr_noether_draft"] = str(r.get("form") or r.get("tr_form") or "")[:60]
        tgt["tr_status"] = "draft_noncanonical_turkish_block (no native review)"
        stats["tr_rows"] += 1

mt["artifact"] = "interlingual_marker_table_v3_3"
mt["v3_3_note"] = ("v3.3: CJK lane merged (confirmed-only, sense-audited v8.2 — ja/ko forms spot-validated by Fable "
                   "against standard terminology: 環/加群/イデアル/準同型/体; 환/가군/몫환/체); Arabic sense-audited statuses "
                   "merged (modulus مودول module-collision and ground-form شكل أساسي stay ADVERSE); Turkish Noether "
                   "draft block side-channel. All new cells = sourcebody_internal_candidate tier; nothing certified.")
(BASE / "INTERLINGUAL_MARKER_TABLE_v3_3_20260705.json").write_text(json.dumps(mt, ensure_ascii=False, indent=1), encoding="utf-8")

cols = []
for row in mt["rows"]:
    for k in row:
        if k not in cols:
            cols.append(k)
with (BASE / "INTERLINGUAL_MARKER_TABLE_v3_3_20260705.csv").open("w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols)
    w.writeheader()
    w.writerows(mt["rows"])

print("merge stats:", stats)
print("cols now:", len(cols))
