from pathlib import Path
import csv
import hashlib
import json

HERE = Path(__file__).resolve().parent
TRANCHE = HERE.parent
ROMANCE = TRANCHE.parents[1]
authority_candidates = list((ROMANCE / "02_r823_romance_translation_20260717" / "authority_extract").rglob("Noether_R823_cum_de.tex"))
if not authority_candidates:
    raise SystemExit("R823 authority extraction not found")
authority = authority_candidates[0]

def digest_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest().upper()

def digest_file(path: Path) -> str:
    return digest_bytes(path.read_bytes())

expected_authority = "EE8955BCF7A263917BE57DBC8F682601550CDCB5260D02CA6D486C6A6DFD4F21"
expected_slice = "73119810BF01CFD24D461C80A829C37326D814F217C3E4CBC2B358A1184B1D33"
if digest_file(authority) != expected_authority:
    raise SystemExit("Authority hash mismatch")

lines = authority.read_text(encoding="utf-8-sig").splitlines()
start, end = 21099, 21115
source_dir = TRANCHE / "source"
source_dir.mkdir(parents=True, exist_ok=True)
exact_path = source_dir / "R823_HG_T003_de_exact.tex"
exact_path.write_bytes(("\n".join(lines[start - 1:end]) + "\n").encode("utf-8"))
(source_dir / "R823_HG_T003_de_numbered.txt").write_text(
    "\n".join(f"{number}: {lines[number - 1]}" for number in range(start, end + 1)) + "\n",
    encoding="utf-8",
)
if digest_file(exact_path) != expected_slice:
    raise SystemExit(f"Slice hash mismatch {digest_file(exact_path)}")

seed = TRANCHE / "semantic" / "R823_HG_T003_clause_map_seed.csv"
rows = []
with seed.open(encoding="utf-8-sig", newline="") as handle:
    for row in csv.DictReader(handle):
        first, last = int(row["source_line_start"]), int(row["source_line_end"])
        source_text = "\n".join(lines[first - 1:last])
        row["source_text_sha256"] = digest_bytes((source_text + "\n").encode("utf-8"))
        row["source_text"] = source_text.replace("\n", " ⏎ ")
        rows.append(row)
clause_map = TRANCHE / "semantic" / "R823_HG_T003_clause_map.csv"
fields = list(rows[0])
with clause_map.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

manifest = {
    "artifact": "R823_HG_T003_SOURCE_MANIFEST",
    "authority_path": str(authority),
    "authority_sha256": expected_authority,
    "line_start": start,
    "line_end": end,
    "exact_slice_path": str(exact_path),
    "exact_slice_sha256": digest_file(exact_path),
    "exact_slice_bytes": exact_path.stat().st_size,
    "clause_map_sha256": digest_file(clause_map),
    "next_line": 21117,
    "next_heading": "§ 4. Der Zusammenhang zwischen Darstellungsmoduln und Darstellungen",
}
(source_dir / "R823_HG_T003_SOURCE_MANIFEST.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(manifest, ensure_ascii=False, indent=2))
