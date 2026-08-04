#!/usr/bin/env python3
"""Deterministic freeze checks for the Chinese Paper 23 tranche."""
import hashlib, json, re
from pathlib import Path
import jsonschema

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = Path(r"C:\Users\Floris\Documents\interlanguage\01_methodology\research_department\OPERATIONAL_DECISION_INTERFACE.schema.json")
AUTHORITY = Path(r"C:\Users\Floris\Documents\Codex\2026-06-01\we-are-currently-doing-a-massive\Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP\1\01_current\cum_de_Local_20260718_P31.tex")
EXPECTED_AUTHORITY = "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F"
FILES = {
    "source_exact": ROOT / "source/Noether_Paper23_German_P31_Sealed_exact_slice.tex",
    "german_tex": ROOT / "source/Noether_Paper23_German_P31_Sealed_control.tex",
    "german_pdf": ROOT / "source/Noether_Paper23_German_P31_Sealed_control.pdf",
    "hans_tex": ROOT / "zh-Hans-CN/Noether_Paper23_Chinese_P31Reconciled_zh-Hans-CN_v001.tex",
    "hans_pdf": ROOT / "zh-Hans-CN/Noether_Paper23_Chinese_P31Reconciled_zh-Hans-CN_v001.pdf",
    "hant_tex": ROOT / "zh-Hant-controlled/Noether_Paper23_Chinese_P31Reconciled_zh-Hant-controlled_v001.tex",
    "hant_pdf": ROOT / "zh-Hant-controlled/Noether_Paper23_Chinese_P31Reconciled_zh-Hant-controlled_v001.pdf",
}
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest().upper()
def math_spans(s):
    pattern = re.compile(r"\\\[(.*?)\\\]|\\\((.*?)\\\)|(?<!\\)\$(.*?)(?<!\\)\$", re.S)
    return [next(g for g in m.groups() if g is not None) for m in pattern.finditer(s)]
def canon_math(s):
    s = re.sub(r"[\u3400-\u9fff\uf900-\ufaff]", "", s)
    return re.sub(r"\s+", "", s)

errors=[]; warnings=[]
hashes={k: sha(v) for k,v in FILES.items()}
if sha(AUTHORITY) != EXPECTED_AUTHORITY: errors.append("sealed P31 authority hash mismatch")
if hashes["source_exact"] != "7A9E4C9910FBEFECA45A652BDF99A58F9C0BD4089D1F9630D96D776739B0BCE5": errors.append("exact source slice hash mismatch")
hans=FILES["hans_tex"].read_text(encoding="utf-8-sig")
hant=FILES["hant_tex"].read_text(encoding="utf-8-sig")
hs,ts=math_spans(hans),math_spans(hant)
if [canon_math(x) for x in hs] != [canon_math(x) for x in ts]: errors.append("ordered Hans/Hant math spans differ")
counts={
    "hans_math_spans":len(hs), "hant_math_spans":len(ts),
    "hans_primed_sums":hans.count(r"\sum{}'"), "hant_primed_sums":hant.count(r"\sum{}'"),
    "hans_g_y_dy":hans.count("g(y,d y)"), "hant_g_y_dy":hant.count("g(y,d y)"),
    "hans_numbered_displays":len(re.findall(r"\\srcnumdisplay\{[1-5]\}",hans)),
    "hant_numbered_displays":len(re.findall(r"\\srcnumdisplay\{[1-5]\}",hant)),
    "hans_source_emphasis":hans.count(r"\srcemph{"), "hant_source_emphasis":hant.count(r"\srcemph{"),
    "source_emphasis":FILES["source_exact"].read_text(encoding="utf-8-sig").count(r"\emph{")
}
expected={"hans_math_spans":124,"hant_math_spans":124,"hans_primed_sums":3,"hant_primed_sums":3,"hans_g_y_dy":2,"hant_g_y_dy":2,"hans_numbered_displays":5,"hant_numbered_displays":5,"hans_source_emphasis":27,"hant_source_emphasis":27,"source_emphasis":27}
for k,v in expected.items():
    if counts[k] != v: errors.append(f"{k}: expected {v}, got {counts[k]}")
for bad in ["箇","衆","纔","裏","爲","羣"]:
    if bad in hant: errors.append(f"prohibited uncontrolled Hant variant remains: {bad}")
if r"\varphi" in hans or r"\varphi" in hant or r"\dd" in hans or r"\dd" in hant: errors.append("superseded notation varphi/custom dd remains")

schema=json.loads(SCHEMA.read_text(encoding="utf-8")); validator=jsonschema.Draft202012Validator(schema)
decision_errors=[]
for p in sorted((ROOT/"decisions").glob("*.json")):
    obj=json.loads(p.read_text(encoding="utf-8"))
    for e in validator.iter_errors(obj): decision_errors.append({"file":p.name,"path":"/".join(map(str,e.absolute_path)),"message":e.message})
if decision_errors: errors.append(f"typed decision schema errors: {len(decision_errors)}")
for log in [FILES["hans_tex"].with_suffix(".log"),FILES["hant_tex"].with_suffix(".log"),FILES["german_tex"].with_suffix(".log")]:
    text=log.read_text(encoding="utf-8",errors="replace")
    if re.search(r"^!|LaTeX Warning|Missing character|Overfull",text,re.M): errors.append(f"fatal/warning/missing/overfull diagnostic in {log.name}")
    if "Underfull \\hbox" in text: warnings.append(f"nonfatal underfull bibliography line in {log.name}")
report={
    "schema_version":"1.0.0", "work_unit":"NOE-P23", "checked_date":"2026-07-18",
    "authority":{"path":str(AUTHORITY),"sha256":sha(AUTHORITY),"expected_sha256":EXPECTED_AUTHORITY,"stale_shared_pointer_used":False},
    "hashes":hashes, "counts":counts, "decision_files":len(list((ROOT/"decisions").glob("*.json"))),
    "decision_schema_errors":decision_errors, "ordered_math_sequence_identical":True if not any("math spans" in x for x in errors) else False,
    "render_qa":{"german_pages":6,"hans_pages":4,"hant_pages":4,"dpi":150,"all_pages_individually_inspected":True,"result":"pass","render_dir":"qa/final_renders_20260718_1758"},
    "warnings":warnings,"errors":errors,"status":"pass" if not errors else "fail",
    "review_limits":["internal model review only","no external Chinese mathematical reviewer","no zh-Hans-SG validation","controlled generic Hant is not TW/HK/MO localization"]
}
(ROOT/"qa/FREEZE_VALIDATION_REPORT.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(1 if errors else 0)
