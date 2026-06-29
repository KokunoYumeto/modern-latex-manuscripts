import datetime
import hashlib
import json
import pathlib
import subprocess
import re


CACHE_ROOT = pathlib.Path("work/source-cache/japanese_20260629")
OUT_DIR = pathlib.Path("work/github-api-payloads/noether-slavic-handoff/20260629")
SEED_JSON = OUT_DIR / "NON_SLAVIC_SOURCE_EVIDENCE_SEED_20260629.json"
OUT_JSON = OUT_DIR / "JAPANESE_TERM_ANCHOR_SEED_20260629.json"

TERMS = [
    {"term": "代数", "english": "algebra", "category": "algebra_core"},
    {"term": "環", "english": "ring", "category": "ring_theory", "caution": "single-character term; counts can be noisy"},
    {"term": "可換環", "english": "commutative ring", "category": "ring_theory"},
    {"term": "半単純環", "english": "semisimple ring", "category": "ring_theory"},
    {"term": "群環", "english": "group ring/group algebra", "category": "representation_theory"},
    {"term": "商環", "english": "quotient ring", "category": "ring_theory"},
    {"term": "体", "english": "field", "category": "field_theory", "caution": "single-character term; counts can be noisy"},
    {"term": "イデアル", "english": "ideal", "category": "ring_theory"},
    {"term": "素イデアル", "english": "prime ideal", "category": "ring_theory"},
    {"term": "極大イデアル", "english": "maximal ideal", "category": "ring_theory"},
    {"term": "単項イデアル", "english": "principal ideal", "category": "ring_theory"},
    {"term": "加群", "english": "module", "category": "module_theory"},
    {"term": "部分加群", "english": "submodule", "category": "module_theory"},
    {"term": "自由加群", "english": "free module", "category": "module_theory"},
    {"term": "単純加群", "english": "simple module", "category": "module_theory"},
    {"term": "ネーター", "english": "Noetherian/Noether", "category": "noetherian"},
    {"term": "Noether", "english": "Noether/Noetherian", "category": "noetherian"},
    {"term": "Noetherian", "english": "Noetherian", "category": "noetherian"},
    {"term": "アルティン", "english": "Artinian/Artin", "category": "finiteness"},
    {"term": "Artin", "english": "Artin/Artinian", "category": "finiteness"},
    {"term": "有限生成", "english": "finitely generated", "category": "finiteness"},
    {"term": "有限次元", "english": "finite-dimensional", "category": "finiteness"},
    {"term": "表現論", "english": "representation theory", "category": "representation_theory"},
    {"term": "表現", "english": "representation", "category": "representation_theory", "caution": "common term; counts can be noisy"},
    {"term": "既約表現", "english": "irreducible representation", "category": "representation_theory"},
    {"term": "完全可約", "english": "completely reducible", "category": "representation_theory"},
    {"term": "半単純", "english": "semisimple", "category": "representation_theory"},
    {"term": "指標", "english": "character", "category": "representation_theory"},
    {"term": "準同型", "english": "homomorphism", "category": "morphism"},
    {"term": "同型", "english": "isomorphism", "category": "morphism"},
    {"term": "自己同型", "english": "automorphism", "category": "morphism"},
    {"term": "自己準同型", "english": "endomorphism", "category": "morphism"},
    {"term": "テンソル積", "english": "tensor product", "category": "module_theory"},
    {"term": "局所化", "english": "localization", "category": "commutative_algebra"},
    {"term": "ヒルベルトの基底定理", "english": "Hilbert basis theorem", "category": "commutative_algebra"},
    {"term": "基底定理", "english": "basis theorem", "category": "commutative_algebra"},
    {"term": "整数環", "english": "ring of integers", "category": "number_theory"},
    {"term": "類数", "english": "class number", "category": "number_theory"},
    {"term": "ノルム", "english": "norm", "category": "number_theory"},
    {"term": "素数の分解", "english": "decomposition of primes", "category": "number_theory"},
    {"term": "リー群", "english": "Lie group", "category": "representation_theory"},
    {"term": "Harish-Chandra", "english": "Harish-Chandra", "category": "representation_theory"},
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
    seed = json.loads(SEED_JSON.read_text(encoding="utf-8"))
    entries = [entry for entry in seed["entries"] if entry["language"] == "Japanese"]
    source_results = []

    for entry in entries:
        pdf = CACHE_ROOT / f"{entry['id']}.pdf"
        pages = page_count(pdf)
        term_data = {term["term"]: {"count": 0, "pages": []} for term in TERMS}
        extraction_errors = []
        nonempty_pages = 0

        for page in range(1, (pages or 0) + 1):
            try:
                text = text_page(pdf, page)
            except Exception as exc:  # noqa: BLE001
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
        "artifact": "japanese_term_anchor_seed",
        "generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "branch": "codex/noether-pc-20260629",
        "status": "term_anchor_seed_from_local_pdf_text_extraction_no_source_text_redistributed",
        "source_seed": "NON_SLAVIC_SOURCE_EVIDENCE_SEED_20260629.json",
        "method": {
            "cache_scope": "PDFs downloaded only to local work/source-cache for analysis; not committed.",
            "extraction": "pdftotext page-level extraction; only counts and page anchors are recorded.",
            "copyright_boundary": "No source passages or PDF contents are redistributed in this artifact.",
            "authority_boundary": "Term anchors are evidence for glossary work, not native/external review or canonical acceptance.",
        },
        "sources_analyzed": source_results,
        "aggregate_term_hits": sorted(aggregate, key=lambda item: (item["category"], item["term"])),
        "next_steps": [
            "Inspect high-value pages manually before promoting any Japanese term decision.",
            "Keep ring/module/number-theory and representation-theory registers separate.",
            "Treat single-character counts as weak evidence unless supported by compound terms.",
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
