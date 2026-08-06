from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

from PIL import Image, ImageChops
from pypdf import PdfReader


HERE = Path(__file__).resolve().parent
NC = HERE.parent
P09 = NC / "paper09" / "rb1"
OLD = NC / "cum_r2"
WS = Path(r"C:\Users\Floris\Documents\interlanguage")
MANIFEST = HERE / "manifest.csv"
VERIFY = HERE / "verify.json"
VIZ_INDEX = HERE / "viz.csv"
EXPECTED_VIZ_SHA = "2513493FD755015C4CD4A794BE9A9DA2FD38C391EB19BD7FC827F0E956C35AC8"
EXPECTED_CHANGED = [
    92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106,
    108, 109, 110, 111, 112, 113, 114, 116, 118, 119, 120, 121, 123, 124,
    125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138,
    139, 140, 141, 142, 144, 146, 147, 149, 151, 152, 153, 155, 156, 157,
    158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 171, 172, 173,
    175, 176, 177, 178, 179, 181, 182, 183, 184, 185, 186,
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def pin(path: Path) -> dict[str, object]:
    return {"bytes": path.stat().st_size, "sha256": sha(path)}


if MANIFEST.exists() or VERIFY.exists() or VIZ_INDEX.exists():
    raise SystemExit("seal outputs already exist; refusing to overwrite")
if sorted(path.name for path in HERE.iterdir() if path.is_dir()) != ["fonts", "viz"]:
    raise SystemExit("unexpected top-level directory")
if any(path.name == "__pycache__" for path in HERE.rglob("__pycache__")):
    raise SystemExit("__pycache__ is not permitted")

expected_local = {
    "reader.tex": (1811029, "50B212EA04061921607E13CB7B367DEBF4AAF2449CF5614F931E74AA1B5A5338"),
    "reader.pdf": (2489062, "86031C4790433915D3882A9DEFFFD481F2743F897E0FFE49B5AAD300D27F9B62"),
    "reader.txt": (1351667, "5335AE4078DA6674DFF6009C2CCE8FA3E93EBFD408770154F672FD7EC4E080BD"),
    "intake.json": (3059, "3951E442ECC7A453AFE91E0FA18545480942E3F982F6E25467CF99D8836FB829"),
    "auth.json": (904, "7650B48129E5605D5F9B405F395DF549CF90C253919E821C62DFECAD8D1AEE98"),
    "build.json": (1573, "C1E1A218B23B868FD6F3329D1A23680E8994F8FCA1DD20CEA0BC3E743C3498D8"),
    "visual.json": (1305, "D3FD1631B58521ECA510B54C1D38153B3F448CD9C7808AE7E36A593EA3BE4125"),
    "text.json": (677, "A3E382BDDDE62AF23563E50B2B21A5F8F3B18FEFC081B0820A6C5086AA9CEDC6"),
    "hans.json": (455, "84A00FED2E88AA60293A84DC5D917A3BAF1C7149A4A4FFEB38B0D83F8B0603C8"),
    "qa.json": (12078, "B3CEBF3B86EDBCDE7A204B26E48EDA90A013AA3793DE2A05E068A43F8E7515B4"),
    "return.json": (4046, "8439B838B5109B8FF7AB10AAC470D88968DE6C4D160DBAC53DD1EC0B918EF0AB"),
}
for name, (size, digest) in expected_local.items():
    if pin(HERE / name) != {"bytes": size, "sha256": digest}:
        raise SystemExit(f"local pin mismatch: {name}")

external_paths = {
    "r2_return": OLD / "return.json",
    "r2_manifest": OLD / "manifest.csv",
    "r2_verify": OLD / "verify.json",
    "p09_return": P09 / "return" / "receipt.json",
    "p09_manifest": P09 / "return" / "manifest.csv",
    "p09_verify": P09 / "return" / "verify.json",
    "p09_intake": P09 / "intake.json",
    "p09_findings": P09 / "find.jsonl",
    "p09_german_packet": P09 / "de.json",
    "p09_candidate": P09 / "p09.tex",
    "p09_language": P09 / "lang.json",
    "p09_math": P09 / "math.json",
    "p09_diff": P09 / "diff.json",
    "pointer_v042": WS / "03_projects" / "noether" / "07_german_canon_control" / "pointers" / "v042.json",
    "ed0006": WS / "03_projects" / "noether" / "07_german_canon_control" / "candidates" / "ED0006" / "noether.tex",
    "method": WS / "01_methodology" / "research_department" / "REBASE_NOT_REWRITE.md",
    "german_handoff": WS / ".coordination_messages" / "DE_P09.md",
}
expected_external = {
    "r2_return": {"bytes": 2754, "sha256": "0A55D87FC0C49906655496745EC8348A6D3AD3766BC41BAE090ABB5C89E504BC"},
    "r2_manifest": {"bytes": 38087, "sha256": "19EB7902F1BBEEB1E0CF1E1099F65161E3AE37D7DFB4694AA2DEE3B169BDBD7E"},
    "r2_verify": {"bytes": 2135, "sha256": "4513A5F9A02C9DB853EC7B296A2B1297BBD87C580C7504AB5DFBA033EE4D6F60"},
    "p09_return": {"bytes": 5465, "sha256": "7EE2329B1846D6B54CD41582CF41E69A68C04D88C873B54CB691048DF95182A5"},
    "p09_manifest": {"bytes": 181, "sha256": "ADD0B951AAF0D8719E4379FFE28CCB877BE88825E81AB4F966C6598A55569700"},
    "p09_verify": {"bytes": 4042, "sha256": "EB7447828021731CF38C1EA15614607FFCE7C8DF5CD63283605B4CA06652DABF"},
    "p09_intake": {"bytes": 3975, "sha256": "96DED0C8EB69568EC8C82F9A73424AA9325BEBFCE18250C43F37AC06E9FE2552"},
    "p09_findings": {"bytes": 12914, "sha256": "9E9033AF200E001496BDAC35D7A37994BB311D693F1C1362DE13F7F25E89F4A9"},
    "p09_german_packet": {"bytes": 5435, "sha256": "C438A3DED9B51E472021C2933FD4935C9D5B82E792B7F46D1EDA2C8F1E8C46FD"},
    "p09_candidate": {"bytes": 66861, "sha256": "1199FC266E910F61AFE6A7BAFB9E390595B8DD7DE848EAE3BC939D8626CEEE94"},
    "p09_language": {"bytes": 1434, "sha256": "2E8585E8D4B8C40190664CE8A7CAE130D080FC727C5A1262772919F59CC687DA"},
    "p09_math": {"bytes": 1457, "sha256": "30897C077710544FABC6B91DD990C2D59EBE7F847F4088F3BD9C63FB2EC3CA76"},
    "p09_diff": {"bytes": 1364, "sha256": "B3B08EA9065D2B1C8D70FF6DF8A8B40F7EB2784FEE8B63A550E4AE64AFA05B36"},
    "pointer_v042": {"bytes": 67496, "sha256": "4D98113DBBFBE45C135FFCEFEFB695AF9AC1D09A2F488E56C32630F7E17591C7"},
    "ed0006": {"bytes": 2153563, "sha256": "BFCFAA1C0BBF5FCDEE3BCDF5C84F78CC4FD12C436141BE8FBD3835247CB341A1"},
    "method": {"bytes": 5389, "sha256": "5742DE5D67CE946A0A9179E9399645C63525FF199232EDD4BFA7FB134CEB319D"},
    "german_handoff": {"bytes": 927, "sha256": "690793102A1937B905C3601FCB04B61E699513F17C7CF21FE5ED7D33165E827D"},
}
external_actual = {name: pin(path) for name, path in external_paths.items()}
if external_actual != expected_external:
    raise SystemExit(f"external pin mismatch: {external_actual}")

for name in ("intake.json", "auth.json", "build.json", "visual.json", "text.json", "hans.json", "qa.json", "return.json"):
    json.loads((HERE / name).read_text(encoding="utf-8"))
if not json.loads((HERE / "build.json").read_text(encoding="utf-8"))["all_pass"]:
    raise SystemExit("build record not PASS")
if not json.loads((HERE / "text.json").read_text(encoding="utf-8"))["all_pass"]:
    raise SystemExit("text record not PASS")
if not json.loads((HERE / "hans.json").read_text(encoding="utf-8"))["all_pass"]:
    raise SystemExit("Hans record not PASS")
if not json.loads((HERE / "qa.json").read_text(encoding="utf-8"))["all_mechanical_gates_pass"]:
    raise SystemExit("QA record not PASS")
if json.loads((HERE / "visual.json").read_text(encoding="utf-8"))["verdict"] != "PASS":
    raise SystemExit("visual record not PASS")
if json.loads((HERE / "auth.json").read_text(encoding="utf-8"))["verdict"] != "COMPATIBLE":
    raise SystemExit("authority record not compatible")

old = (OLD / "reader.tex").read_bytes()
witness = (WS / "03_projects" / "language_management" / "cjk" / "03_working_translations" / "P09_zh_v2" / "src" / "zh_wit.tex").read_bytes()
candidate = (P09 / "p09.tex").read_bytes()
new = (HERE / "reader.tex").read_bytes()
offset = 379451
if old[offset : offset + len(witness)] != witness:
    raise SystemExit("P09 predecessor locus mismatch")
if old[:offset] + candidate + old[offset + len(witness) :] != new:
    raise SystemExit("successor has change outside exact P09 splice")

pdf = PdfReader(str(HERE / "reader.pdf"))
if len(pdf.pages) != 413:
    raise SystemExit("PDF page count mismatch")
old_viz = sorted((OLD / "viz").glob("p-*.png"))
new_viz = sorted((HERE / "viz").glob("p-*.png"))
names = [f"p-{number:03d}.png" for number in range(1, 414)]
if [path.name for path in old_viz] != names or [path.name for path in new_viz] != names:
    raise SystemExit("render inventory names mismatch")
changed: list[int] = []
blank: list[int] = []
edge: list[int] = []
for number, (old_path, new_path) in enumerate(zip(old_viz, new_viz), 1):
    with Image.open(old_path) as old_image, Image.open(new_path) as new_image:
        old_rgb = old_image.convert("RGB")
        new_rgb = new_image.convert("RGB")
        if old_rgb.size != new_rgb.size:
            raise SystemExit(f"render dimension mismatch page {number}")
        if ImageChops.difference(old_rgb, new_rgb).getbbox() is not None:
            changed.append(number)
        gray = new_rgb.convert("L")
        width, height = gray.size
        if gray.getextrema()[0] >= 245:
            blank.append(number)
        bands = (
            gray.crop((0, 0, width, 2)), gray.crop((0, height - 2, width, height)),
            gray.crop((0, 0, 2, height)), gray.crop((width - 2, 0, width, height)),
        )
        if any(band.getextrema()[0] < 245 for band in bands):
            edge.append(number)
if changed != EXPECTED_CHANGED or blank or edge:
    raise SystemExit(f"render QA mismatch changed={changed} blank={blank} edge={edge}")

viz_lines = [f"{path.name},{path.stat().st_size},{sha(path)}\n" for path in new_viz]
viz_payload = "".join(viz_lines).encode("utf-8")
if len(viz_payload) != 33861 or hashlib.sha256(viz_payload).hexdigest().upper() != EXPECTED_VIZ_SHA:
    raise SystemExit("render inventory aggregate mismatch")
VIZ_INDEX.write_bytes(viz_payload)

members = sorted(
    path for path in HERE.rglob("*")
    if path.is_file() and path.name not in {MANIFEST.name, VERIFY.name}
)
rows: list[tuple[str, int, str]] = []
for path in members:
    rel = path.relative_to(HERE).as_posix()
    pure = PurePosixPath(rel)
    if pure.is_absolute() or ".." in pure.parts:
        raise SystemExit(f"unsafe manifest path: {rel}")
    rows.append((rel, path.stat().st_size, sha(path)))
if len({row[0] for row in rows}) != len(rows):
    raise SystemExit("duplicate manifest path")
with MANIFEST.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.writer(handle, lineterminator="\n")
    writer.writerow(["path", "bytes", "sha256"])
    writer.writerows(rows)
with MANIFEST.open("r", encoding="utf-8", newline="") as handle:
    replay = list(csv.DictReader(handle))
failures: list[str] = []
for row in replay:
    pure = PurePosixPath(row["path"])
    path = HERE / Path(*pure.parts)
    if pure.is_absolute() or ".." in pure.parts:
        failures.append(f"unsafe:{row['path']}")
    elif not path.is_file():
        failures.append(f"missing:{row['path']}")
    elif pin(path) != {"bytes": int(row["bytes"]), "sha256": row["sha256"]}:
        failures.append(f"pin:{row['path']}")
nonexcluded = sorted(path.relative_to(HERE).as_posix() for path in HERE.rglob("*") if path.is_file() and path.name not in {MANIFEST.name, VERIFY.name})
if failures or sorted(row["path"] for row in replay) != nonexcluded:
    raise SystemExit(f"manifest replay failed: {failures}")

verify = {
    "verify_id": "ZHCHK-CUM-R3-VERIFY-001",
    "generated_at": datetime.now(timezone.utc).isoformat(),
    "return_id": "ZHCHK-NOETHER-ZH-CUM-R3-RETURN-001",
    "manifest": {**pin(MANIFEST), "entries": len(rows), "member_bytes": sum(row[1] for row in rows), "exclusions": ["manifest.csv", "verify.json"]},
    "replay": {"members_checked": len(replay), "duplicate_paths": 0, "unsafe_paths": 0, "missing": 0, "byte_failures": 0, "hash_failures": 0, "extra_or_missing_nonexcluded": 0},
    "external_pins": external_actual,
    "gates": {
        "exact_p09_splice_only": True,
        "p09_return": "PASS",
        "complete_hans_scan": "PASS",
        "two_serial_build_passes": "PASS",
        "final_build_diagnostics": "PASS",
        "pdf_pages": 413,
        "fresh_render_pages": 413,
        "changed_raster_pages": len(changed),
        "unchanged_raster_pages": 413 - len(changed),
        "original_detail_visual_pages": 95,
        "visual_review": "PASS",
        "authority_v042": "COMPATIBLE",
        "german_mutated": False,
        "sga": "held and untouched",
    },
    "expected_final_census": {"files": len(rows) + 2, "directories": 2},
    "all_pass": True,
}
VERIFY.write_text(json.dumps(verify, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
final_files = [path for path in HERE.rglob("*") if path.is_file()]
final_dirs = [path for path in HERE.rglob("*") if path.is_dir()]
if len(final_files) != len(rows) + 2 or len(final_dirs) != 2:
    raise SystemExit("final census mismatch")
print(json.dumps({"all_pass": True, "entries": len(rows), "member_bytes": sum(row[1] for row in rows), "manifest": pin(MANIFEST), "verify": pin(VERIFY), "final_files": len(final_files), "final_directories": len(final_dirs)}, indent=2))
