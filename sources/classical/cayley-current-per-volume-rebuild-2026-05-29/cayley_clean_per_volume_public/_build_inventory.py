import os, re, json
from pathlib import Path

SRC = Path(r"local workspace\Documents\Papors\Chatnotes\CHat translates and clean\source system\source system 7\source system 7\latex_typesetting_CONTINUED_WORK\cayley")
ALT = Path(r"local workspace\Documents\Papors\Chatnotes\CHat translates and clean\source system\more source system 5\more source system 5\latex_typesetting_CONTINUED_WORK\cayley")

chunk_re = re.compile(r"cayley_(vol\d{2})_pages_(\d{3})_(\d{3})\.tex$")

def inventory(root):
    out = {}
    if not root.exists():
        return out
    for vol_dir in sorted(root.iterdir()):
        if not vol_dir.is_dir() or not vol_dir.name.startswith("vol"):
            continue
        chunks = []
        for fp in sorted(vol_dir.iterdir()):
            m = chunk_re.match(fp.name)
            if not m:
                continue
            start, end = int(m.group(2)), int(m.group(3))
            pdf = fp.with_suffix(".pdf")
            chunks.append({
                "name": fp.name,
                "tex_path": str(fp),
                "pdf_path": str(pdf) if pdf.exists() else None,
                "start": start, "end": end, "span": end - start + 1,
                "tex_bytes": fp.stat().st_size,
                "pdf_bytes": pdf.stat().st_size if pdf.exists() else 0,
            })
        out[vol_dir.name] = chunks
    return out

inv_main = inventory(SRC)
inv_alt  = inventory(ALT)

def pick_canonical(chunks):
    """Pick non-overlapping coverage. Tolerate internal gaps."""
    if not chunks:
        return [], []
    by_start = {}
    for c in chunks:
        by_start.setdefault(c["start"], []).append(c)
    span_counts = {}
    for c in chunks:
        span_counts[c["span"]] = span_counts.get(c["span"], 0) + 1
    dominant_span = max(span_counts, key=lambda s: span_counts[s])
    chosen = []
    starts_sorted = sorted(by_start.keys())
    last_end = 0
    missing = []
    for s in starts_sorted:
        if s <= last_end:
            continue
        if last_end and s > last_end + 1:
            missing.append(f"{last_end+1:03d}_{s-1:03d}")
        candidates = by_start[s]
        pick = None
        for c in candidates:
            if c["span"] == dominant_span:
                pick = c; break
        if pick is None:
            pick = max(candidates, key=lambda x: x["span"])
        chosen.append(pick)
        last_end = pick["end"]
    return chosen, missing

result = {}
for vol in sorted(set(list(inv_main.keys()) + list(inv_alt.keys()))):
    main_chunks = inv_main.get(vol, [])
    alt_chunks  = inv_alt.get(vol, [])
    # Merge into superset keyed by start; prefer main when both have same start
    merged = {}
    for c in main_chunks:
        merged.setdefault(c["start"], []).append(("main", c))
    for c in alt_chunks:
        merged.setdefault(c["start"], []).append(("alt", c))
    flat = []
    for start, items in merged.items():
        # Prefer main if multiple share same start
        main_items = [c for src,c in items if src=="main"]
        alt_items  = [c for src,c in items if src=="alt"]
        flat.extend(main_items if main_items else alt_items)
    chosen, missing = pick_canonical(flat)
    result[vol] = {
        "main_count": len(main_chunks),
        "alt_count": len(alt_chunks),
        "chosen_count": len(chosen),
        "chunks": chosen,
        "missing_ranges": missing,
        "last_page": chosen[-1]["end"] if chosen else 0,
    }

out_dir = Path(r"local workspace\Documents\local repair pass PLEASE DONT DELETE WINDOWS 32\local repair pass_OUTPUTS\cayley_clean_per_volume")
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "_inventory.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print("Summary per volume:")
for vol, info in sorted(result.items()):
    print(f"  {vol}: {info['chosen_count']} chunks, last page {info['last_page']}, "
          f"missing={info['missing_ranges'] or 'none'}")
