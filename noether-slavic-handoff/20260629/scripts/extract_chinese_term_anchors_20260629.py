import datetime
import hashlib
import json
import pathlib
import re
import subprocess


ROOT = pathlib.Path("work/source-cache/simplified_chinese_20260629")
OUT_DIR = pathlib.Path("work/github-api-payloads/noether-slavic-handoff/20260629")
SOURCE_JSON = OUT_DIR / "CHINESE_SOURCE_EVIDENCE_REINFORCEMENT_20260629.json"
OUT_JSON = OUT_DIR / "SIMPLIFIED_CHINESE_TERM_ANCHOR_SEED_20260629.json"

TERMS = [
    {"term": "抽象代数", "english": "abstract algebra", "category": "course_scope"},
    {"term": "近世代数", "english": "modern algebra", "category": "course_scope"},
    {"term": "群", "english": "group", "category": "algebra_core", "caution": "single-character term; counts can be noisy"},
    {"term": "环", "english": "ring", "category": "algebra_core", "caution": "single-character term; counts can be noisy"},
    {"term": "交换环", "english": "commutative ring", "category": "ring_theory"},
    {"term": "诺特", "english": "Noether/Noetherian", "category": "noetherian"},
    {"term": "Noether", "english": "Noether/Noetherian", "category": "noetherian"},
    {"term": "Noetherian", "english": "Noetherian", "category": "noetherian"},
    {"term": "诺特环", "english": "Noetherian ring", "category": "noetherian"},
    {"term": "诺特模", "english": "Noetherian module", "category": "noetherian"},
    {"term": "理想", "english": "ideal", "category": "ring_theory"},
    {"term": "主理想", "english": "principal ideal", "category": "ring_theory"},
    {"term": "极大理想", "english": "maximal ideal", "category": "ring_theory"},
    {"term": "素理想", "english": "prime ideal", "category": "ring_theory"},
    {"term": "商环", "english": "quotient ring", "category": "ring_theory"},
    {"term": "域", "english": "field", "category": "field_theory", "caution": "single-character term; counts can be noisy"},
    {"term": "除环", "english": "division ring", "category": "field_theory"},
    {"term": "模", "english": "module", "category": "module_theory", "caution": "single-character term; counts can be noisy"},
    {"term": "左模", "english": "left module", "category": "module_theory"},
    {"term": "右模", "english": "right module", "category": "module_theory"},
    {"term": "子模", "english": "submodule", "category": "module_theory"},
    {"term": "自由模", "english": "free module", "category": "module_theory"},
    {"term": "模同态", "english": "module homomorphism", "category": "module_theory"},
    {"term": "有限生成", "english": "finitely generated", "category": "finiteness"},
    {"term": "有限维", "english": "finite-dimensional", "category": "finiteness"},
    {"term": "表示论", "english": "representation theory", "category": "representation_theory"},
    {"term": "表示", "english": "representation", "category": "representation_theory", "caution": "common word; counts can be noisy"},
    {"term": "不可约表示", "english": "irreducible representation", "category": "representation_theory"},
    {"term": "完全可约", "english": "completely reducible", "category": "representation_theory"},
    {"term": "半单", "english": "semisimple", "category": "representation_theory"},
    {"term": "特征标", "english": "character", "category": "representation_theory"},
    {"term": "群代数", "english": "group algebra", "category": "representation_theory"},
    {"term": "同态", "english": "homomorphism", "category": "morphism"},
    {"term": "同构", "english": "isomorphism", "category": "morphism"},
    {"term": "自同构", "english": "automorphism", "category": "morphism"},
    {"term": "自同态", "english": "endomorphism", "category": "morphism"},
    {"term": "张量积", "english": "tensor product", "category": "module_theory"},
    {"term": "局部化", "english": "localization", "category": "commutative_algebra"},
    {"term": "希尔伯特基定理", "english": "Hilbert basis theorem", "category": "commutative_algebra"},
    {"term": "基定理", "english": "basis theorem", "category": "commutative_algebra"},
]


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def page_count(pdf: pathlib.Path) -> int | None:
    proc = subprocess.run(
        ["pdfinfo", str(pdf)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    match = re.search(r"^Pages:\s+(\d+)", proc.stdout, re.M)
    return int(match.group(1)) if match else None


def text_page(pdf: pathlib.Path, page: int) -> str:
    proc = subprocess.run(
        ["pdftotext", "-enc", "UTF-8", "-f", str(page), "-l", str(page), str(pdf), "-"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=60,
        check=False,
    )
    return proc.stdout or ""


def main() -> None:
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    entries = [entry for entry in source["entries"] if entry["id"] != "zh_icourse_comm_alg_mirror"]
    source_results = []

    for entry in entries:
        pdf = ROOT / f"{entry['id']}.pdf"
        pages = page_count(pdf)
        term_data = {term["term"]: {"count": 0, "pages": []} for term in TERMS}
        extraction_errors = []
        nonempty_pages = 0

        for page in range(1, (pages or 0) + 1):
            try:
                text = text_page(pdf, page)
            except Exception as exc:  # noqa: BLE001 - extraction ledger should preserve failures.
                extraction_errors.append({"page": page, "error": str(exc)})
                continue
            if text.strip():
                nonempty_pages += 1
            for term in TERMS:
                count = text.count(term["term"])
                if count:
                    item = term_data[term["term"]]
                    item["count"] += count
                    if len(item["pages"]) < 20:
                        item["pages"].append(page)

        hits = []
        for term in TERMS:
            data = term_data[term["term"]]
            if data["count"]:
                hit = {
                    "term": term["term"],
                    "english": term["english"],
                    "category": term["category"],
                    "count": data["count"],
                    "sample_pages": data["pages"],
                }
                if "caution" in term:
                    hit["caution"] = term["caution"]
                hits.append(hit)

        source_results.append(
            {
                "id": entry["id"],
                "title": entry.get("title"),
                "institution_or_host": entry.get("institution_or_host"),
                "url": entry.get("url"),
                "local_cache_sha256": sha256(pdf),
                "local_cache_bytes": pdf.stat().st_size,
                "pages": pages,
                "text_nonempty_pages": nonempty_pages,
                "extraction_errors": extraction_errors,
                "term_hits": sorted(hits, key=lambda item: (item["category"], item["term"])),
            }
        )

    aggregate = []
    for term in TERMS:
        sources = []
        total = 0
        for source_result in source_results:
            hit = next((item for item in source_result["term_hits"] if item["term"] == term["term"]), None)
            if hit:
                sources.append(
                    {
                        "id": source_result["id"],
                        "count": hit["count"],
                        "sample_pages": hit["sample_pages"],
                    }
                )
                total += hit["count"]
        if sources:
            item = {
                "term": term["term"],
                "english": term["english"],
                "category": term["category"],
                "total_count": total,
                "sources": sources,
            }
            if "caution" in term:
                item["caution"] = term["caution"]
            aggregate.append(item)

    output = {
        "artifact": "simplified_chinese_term_anchor_seed",
        "generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "branch": "codex/noether-pc-20260629",
        "status": "term_anchor_seed_from_local_pdf_text_extraction_no_source_text_redistributed",
        "source_reinforcement": "CHINESE_SOURCE_EVIDENCE_REINFORCEMENT_20260629.json",
        "method": {
            "cache_scope": "PDFs downloaded only to local work/source-cache for analysis; not committed.",
            "extraction": "pdftotext page-level extraction; only counts and page anchors are recorded.",
            "copyright_boundary": "No source passages or PDF contents are redistributed in this artifact.",
            "authority_boundary": "Term anchors are evidence for glossary work, not native/external review or canonical acceptance.",
        },
        "sources_analyzed": source_results,
        "aggregate_term_hits": sorted(aggregate, key=lambda item: (item["category"], item["term"])),
        "next_steps": [
            "Inspect high-value pages manually before promoting any term decision.",
            "Add Chinese glossary entries with rationale, rejected alternatives, and source page anchors.",
            "Keep single-character term counts as weak evidence unless supported by compound terms or context.",
            "Separate mathematics and physics-adjacent register decisions.",
            "Request native/external review before canonical release language.",
        ],
    }
    OUT_JSON.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(
        json.dumps(
            {
                "out": str(OUT_JSON),
                "sources": len(source_results),
                "aggregate_terms": len(aggregate),
                "source_pages": sum(result["pages"] or 0 for result in source_results),
                "sources_with_errors": [result["id"] for result in source_results if result["extraction_errors"]],
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
