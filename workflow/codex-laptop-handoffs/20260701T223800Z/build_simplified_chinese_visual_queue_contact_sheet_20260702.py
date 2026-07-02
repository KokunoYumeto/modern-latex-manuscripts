import json
from datetime import datetime, timezone
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
STAMP = "20260702T013500Z"
QUEUE_LEDGER = ROOT / "logs" / "VISUAL_INSPECTION_COVERAGE_LEDGER_20260702T011500Z.json"
OUT_DIR = ROOT / "visual_inspection" / "simplified_chinese_visual_queue_20260702T013500Z"
OUT_JSON = ROOT / "logs" / f"SIMPLIFIED_CHINESE_VISUAL_QUEUE_CONTACT_SHEET_{STAMP}.json"
OUT_MD = ROOT / "logs" / f"SIMPLIFIED_CHINESE_VISUAL_QUEUE_CONTACT_SHEET_{STAMP}.md"


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def render_first_page(pdf_path: Path, out_path: Path, zoom: float = 1.5) -> dict:
    doc = fitz.open(pdf_path)
    page = doc[0]
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    pix.save(out_path)
    return {
        "page_count": doc.page_count,
        "page_width_pt": page.rect.width,
        "page_height_pt": page.rect.height,
        "render_png": rel(out_path),
        "render_png_bytes": out_path.stat().st_size,
    }


def make_contact_sheet(items: list[dict], out_path: Path) -> None:
    if not items:
        raise ValueError("No rendered items supplied for contact sheet")
    thumb_w = 420
    label_h = 78
    margin = 18
    cols = 2
    rows = (len(items) + cols - 1) // cols
    cell_w = thumb_w + margin * 2
    cell_h = 620
    sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), "white")
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("arial.ttf", 16)
        small = ImageFont.truetype("arial.ttf", 13)
    except OSError:
        font = ImageFont.load_default()
        small = ImageFont.load_default()

    for idx, item in enumerate(items):
        row, col = divmod(idx, cols)
        x = col * cell_w + margin
        y = row * cell_h + margin
        img = Image.open(ROOT / item["render_png"]).convert("RGB")
        scale = min(thumb_w / img.width, (cell_h - label_h - margin) / img.height)
        resized = img.resize((int(img.width * scale), int(img.height * scale)))
        sheet.paste(resized, (x + (thumb_w - resized.width) // 2, y + label_h))
        label = f"{idx + 1}. {Path(item['pdf']).name}"
        draw.text((x, y), label[:58], fill="black", font=font)
        draw.text((x, y + 22), f"pages={item['page_count']}  bytes={item['pdf_bytes']}", fill="black", font=small)
        draw.text((x, y + 42), item["pdf"][-68:], fill="black", font=small)
        draw.rectangle((x, y + label_h, x + thumb_w, y + cell_h - margin), outline=(180, 180, 180), width=1)
    sheet.save(out_path)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ledger = json.loads(QUEUE_LEDGER.read_text(encoding="utf-8-sig"))
    queued = [
        rec for rec in ledger["priority_visual_inspection_queue"]
        if rec["lane"] == "simplified_chinese"
    ]
    if not queued and OUT_JSON.exists():
        existing = json.loads(OUT_JSON.read_text(encoding="utf-8-sig"))
        existing["generated_utc"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
        existing["source_ledger"] = rel(QUEUE_LEDGER)
        existing["replay_status"] = {
            "current_queue_count": 0,
            "action": "preserved_existing_contact_sheet",
            "reason": (
                "The coverage ledger now references the prior contact-sheet evidence, so the "
                "Simplified Chinese priority queue is empty on replay."
            ),
        }
        OUT_JSON.write_text(json.dumps(existing, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        lines = [
            "# Simplified Chinese Visual Queue Contact Sheet",
            "",
            f"- Generated UTC: `{existing['generated_utc']}`",
            "- Replay status: `preserved_existing_contact_sheet`",
            "- Current queue count: `0`",
            f"- Existing contact sheet: `{existing['contact_sheet']}`",
            f"- Previously rendered items: `{len(existing.get('rendered_items', []))}`",
            "",
            "## Boundary",
            "",
        ]
        for note in existing["boundary"]:
            lines.append(f"- {note}")
        lines.append("- Replay note: the queue is empty because the contact-sheet evidence now exists; this is not a promotion-grade clearance.")
        OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(json.dumps({"json": rel(OUT_JSON), "markdown": rel(OUT_MD), "contact_sheet": existing["contact_sheet"], "replay_status": "preserved_existing_contact_sheet"}, ensure_ascii=True, indent=2))
        return

    rendered = []
    for idx, rec in enumerate(queued, start=1):
        pdf_path = ROOT / rec["path"]
        png_path = OUT_DIR / f"{idx:02d}_{pdf_path.stem}_page001.png"
        details = render_first_page(pdf_path, png_path)
        item = {
            "pdf": rec["path"],
            "pdf_bytes": pdf_path.stat().st_size,
            **details,
            "inspection_scope": "first page only; working/font-test PDFs are not promoted cumulative readers",
            "initial_machine_note": "Rendered successfully for visual contact-sheet inspection.",
        }
        rendered.append(item)
    sheet_path = OUT_DIR / "simplified_chinese_visual_queue_contact_sheet_page001.png"
    make_contact_sheet(rendered, sheet_path)
    result = {
        "artifact": "simplified_chinese_visual_queue_contact_sheet",
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "source_ledger": rel(QUEUE_LEDGER),
        "scope": "First-page contact sheet for the 10 Simplified Chinese working/font-test PDFs queued by the visual coverage ledger.",
        "completion_claim": False,
        "contact_sheet": rel(sheet_path),
        "contact_sheet_bytes": sheet_path.stat().st_size,
        "queued_pdf_count": len(queued),
        "rendered_items": rendered,
        "boundary": [
            "This contact sheet is a visual triage artifact, not a full front/middle/back inspection.",
            "These PDFs are working/font-test outputs and should not be used as public promotion evidence unless separately promoted.",
            "The canonical Simplified Chinese cumulative proof remains governed by the cumulative status manifest and visual ledger.",
        ],
    }
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Simplified Chinese Visual Queue Contact Sheet",
        "",
        f"- Generated UTC: `{result['generated_utc']}`",
        f"- Queued PDFs rendered: `{len(queued)}`",
        f"- Contact sheet: `{result['contact_sheet']}`",
        f"- Scope: {result['scope']}",
        "",
        "## Items",
        "",
    ]
    for idx, item in enumerate(rendered, start=1):
        lines.append(f"- {idx}. `{item['pdf']}` pages `{item['page_count']}` render `{item['render_png']}`")
    lines.extend(["", "## Boundary", ""])
    for note in result["boundary"]:
        lines.append(f"- {note}")
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"json": rel(OUT_JSON), "markdown": rel(OUT_MD), "contact_sheet": rel(sheet_path)}, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
