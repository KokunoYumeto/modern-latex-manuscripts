#!/usr/bin/env python3
"""Create the curated Paper 23 archive manifest and hash list."""
import hashlib, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
top=["README.md","STATUS.md","SOURCE_USE.md","SOURCE_CHECK.md","SOURCE_UNIT_MAP.csv","TERMINOLOGY.md","LOCALIZATION_STATUS.csv","BUILD_REPORT.md","RENDER_CHECK.md","CHINESE_WORKER_RETURN.md","ARCHIVE_HANDOFF.md"]
files=[ROOT/x for x in top]
for folder in ["source","witness","zh-Hans-CN","zh-Hant-controlled","evidence","decisions","qa/final_renders_20260718_1758"]:
    for p in (ROOT/folder).rglob("*"):
        if p.is_file() and p.suffix.lower() not in {".aux",".out"}: files.append(p)
for name in ["qa/FREEZE_VALIDATION_REPORT.json","qa/OPENCC_CONVERSION_RECORD.json","qa/HANS_HANT_SCRIPT_DIFF_REPORT.json","qa/source_version_cursor.json","qa/build_typed_decisions.py","qa/run_freeze_checks.py","qa/build_manifest.py"]: files.append(ROOT/name)
files=sorted(set(p for p in files if p.exists()),key=lambda p:p.relative_to(ROOT).as_posix())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest().upper()
records=[{"path":p.relative_to(ROOT).as_posix(),"bytes":p.stat().st_size,"sha256":sha(p)} for p in files]
manifest={"schema_version":"1.0.0","work_unit":"NOE-P23","created_date":"2026-07-18","authority_sha256":"A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F","artifact_count":len(records),"artifacts":records,"review_state":"internal_source_schema_build_render_freeze","publication_state":"archive_handoff_ready_not_received","limits":["no external certification","no zh-Hans-SG validation","controlled Hant is not TW/HK/MO localization","SGA held and untouched"]}
(ROOT/"MANIFEST.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
lines=[f"{r['sha256']}  {r['path']}" for r in records]
lines.append(f"{sha(ROOT/'MANIFEST.json')}  MANIFEST.json")
(ROOT/"SHA256SUMS.txt").write_text("\n".join(lines)+"\n",encoding="utf-8")
print(json.dumps({"artifact_count":len(records),"manifest_sha256":sha(ROOT/'MANIFEST.json'),"sha256sums_sha256":sha(ROOT/'SHA256SUMS.txt')},indent=2))
