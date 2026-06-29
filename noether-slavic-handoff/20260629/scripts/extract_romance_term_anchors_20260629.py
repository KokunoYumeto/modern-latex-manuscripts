import datetime
import hashlib
import json
import pathlib
import re
import subprocess


CACHE_ROOT = pathlib.Path("work/source-cache/romance_fr_es_20260629")
OUT_DIR = pathlib.Path("work/github-api-payloads/noether-slavic-handoff/20260629")
SEED_JSON = OUT_DIR / "NON_SLAVIC_SOURCE_EVIDENCE_SEED_20260629.json"
OUT_JSON = OUT_DIR / "ROMANCE_FRENCH_SPANISH_TERM_ANCHOR_SEED_20260629.json"


TERMS = {
    "French": [
        {"term": "anneau", "english": "ring", "category": "ring_theory", "patterns": [r"\banneaux?\b"]},
        {"term": "anneau noethérien", "english": "Noetherian ring", "category": "noetherian", "patterns": [r"\banneaux?\s+noeth[ée]rien(?:ne)?s?\b"]},
        {"term": "noethérien", "english": "Noetherian", "category": "noetherian", "patterns": [r"\bnoeth[ée]rien(?:ne)?s?\b"]},
        {"term": "idéal", "english": "ideal", "category": "ring_theory", "patterns": [r"\bid[ée]aux?\b"]},
        {"term": "idéal maximal", "english": "maximal ideal", "category": "ring_theory", "patterns": [r"\bid[ée]aux?\s+maxim(?:al|aux|ale|ales)\b"]},
        {"term": "idéal premier", "english": "prime ideal", "category": "ring_theory", "patterns": [r"\bid[ée]aux?\s+premier(?:s)?\b"]},
        {"term": "corps", "english": "field", "category": "field_theory", "patterns": [r"\bcorps\b"]},
        {"term": "module", "english": "module", "category": "module_theory", "patterns": [r"\bmodules?\b"]},
        {"term": "sous-module", "english": "submodule", "category": "module_theory", "patterns": [r"\bsous[- ]modules?\b"]},
        {"term": "module quotient", "english": "quotient module", "category": "module_theory", "patterns": [r"\bmodules?\s+quotients?\b"]},
        {"term": "algèbre", "english": "algebra", "category": "algebra_core", "patterns": [r"\balg[èe]bres?\b"]},
        {"term": "algèbre commutative", "english": "commutative algebra", "category": "commutative_algebra", "patterns": [r"\balg[èe]bre\s+commutative\b"]},
        {"term": "produit tensoriel", "english": "tensor product", "category": "module_theory", "patterns": [r"\bproduits?\s+tensoriels?\b"]},
        {"term": "localisation", "english": "localization", "category": "commutative_algebra", "patterns": [r"\blocalisations?\b"]},
        {"term": "représentation", "english": "representation", "category": "representation_theory", "patterns": [r"\brepr[ée]sentations?\b"]},
        {"term": "représentation irréductible", "english": "irreducible representation", "category": "representation_theory", "patterns": [r"\brepr[ée]sentations?\s+irr[ée]ductibles?\b"]},
        {"term": "irréductible", "english": "irreducible", "category": "representation_theory", "patterns": [r"\birr[ée]ductibles?\b"]},
        {"term": "semi-simple", "english": "semisimple", "category": "representation_theory", "patterns": [r"\bsemi[- ]simples?\b", r"\bsemisimples?\b"]},
        {"term": "homomorphisme", "english": "homomorphism", "category": "morphism", "patterns": [r"\bhomomorphismes?\b"]},
        {"term": "isomorphisme", "english": "isomorphism", "category": "morphism", "patterns": [r"\bisomorphismes?\b"]},
        {"term": "endomorphisme", "english": "endomorphism", "category": "morphism", "patterns": [r"\bendomorphismes?\b"]},
        {"term": "automorphisme", "english": "automorphism", "category": "morphism", "patterns": [r"\bautomorphismes?\b"]},
        {"term": "théorème de la base de Hilbert", "english": "Hilbert basis theorem", "category": "commutative_algebra", "patterns": [r"\bth[ée]or[èe]me\s+de\s+la\s+base\s+de\s+hilbert\b"]},
        {"term": "base de Hilbert", "english": "Hilbert basis", "category": "commutative_algebra", "patterns": [r"\bbase\s+de\s+hilbert\b"]},
        {"term": "finiment engendré", "english": "finitely generated", "category": "finiteness", "patterns": [r"\bfiniment\s+engendr[ée]s?\b"]},
    ],
    "Spanish": [
        {"term": "anillo", "english": "ring", "category": "ring_theory", "patterns": [r"\banillos?\b"]},
        {"term": "anillo noetheriano", "english": "Noetherian ring", "category": "noetherian", "patterns": [r"\banillos?\s+noetherian[ao]s?\b"]},
        {"term": "noetheriano", "english": "Noetherian", "category": "noetherian", "patterns": [r"\bnoetherian[ao]s?\b"]},
        {"term": "ideal", "english": "ideal", "category": "ring_theory", "patterns": [r"\bideales?\b"]},
        {"term": "ideal maximal", "english": "maximal ideal", "category": "ring_theory", "patterns": [r"\bideales?\s+maximales?\b"]},
        {"term": "ideal primo", "english": "prime ideal", "category": "ring_theory", "patterns": [r"\bideales?\s+primos?\b"]},
        {"term": "cuerpo", "english": "field", "category": "field_theory", "patterns": [r"\bcuerpos?\b"]},
        {"term": "módulo", "english": "module", "category": "module_theory", "patterns": [r"\bm[óo]dulos?\b"]},
        {"term": "submódulo", "english": "submodule", "category": "module_theory", "patterns": [r"\bsubm[óo]dulos?\b"]},
        {"term": "módulo cociente", "english": "quotient module", "category": "module_theory", "patterns": [r"\bm[óo]dulos?\s+cocientes?\b"]},
        {"term": "álgebra", "english": "algebra", "category": "algebra_core", "patterns": [r"\b[áa]lgebras?\b"]},
        {"term": "álgebra conmutativa", "english": "commutative algebra", "category": "commutative_algebra", "patterns": [r"\b[áa]lgebra\s+conmutativa\b"]},
        {"term": "producto tensorial", "english": "tensor product", "category": "module_theory", "patterns": [r"\bproductos?\s+tensoriales?\b"]},
        {"term": "localización", "english": "localization", "category": "commutative_algebra", "patterns": [r"\blocalizaci[oó]n(?:es)?\b"]},
        {"term": "representación", "english": "representation", "category": "representation_theory", "patterns": [r"\brepresentaci[oó]n(?:es)?\b"]},
        {"term": "representación irreducible", "english": "irreducible representation", "category": "representation_theory", "patterns": [r"\brepresentaci[oó]n(?:es)?\s+irreducibles?\b"]},
        {"term": "irreducible", "english": "irreducible", "category": "representation_theory", "patterns": [r"\birreducibles?\b"]},
        {"term": "semisimple", "english": "semisimple", "category": "representation_theory", "patterns": [r"\bsemi[- ]simples?\b", r"\bsemisimples?\b"]},
        {"term": "homomorfismo", "english": "homomorphism", "category": "morphism", "patterns": [r"\bhomomorfismos?\b"]},
        {"term": "isomorfismo", "english": "isomorphism", "category": "morphism", "patterns": [r"\bisomorfismos?\b"]},
        {"term": "endomorfismo", "english": "endomorphism", "category": "morphism", "patterns": [r"\bendomorfismos?\b"]},
        {"term": "automorfismo", "english": "automorphism", "category": "morphism", "patterns": [r"\bautomorfismos?\b"]},
        {"term": "teorema de la base de Hilbert", "english": "Hilbert basis theorem", "category": "commutative_algebra", "patterns": [r"\bteorema\s+de\s+la\s+base\s+de\s+hilbert\b"]},
        {"term": "base de Hilbert", "english": "Hilbert basis", "category": "commutative_algebra", "patterns": [r"\bbase\s+de\s+hilbert\b"]},
        {"term": "finitamente generado", "english": "finitely generated", "category": "finiteness", "patterns": [r"\bfinitamente\s+generad[ao]s?\b"]},
    ],
}


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


def count_patterns(text: str, patterns: list[str]) -> int:
    folded = text.casefold()
    return sum(len(re.findall(pattern, folded, flags=re.IGNORECASE)) for pattern in patterns)


def main() -> None:
    seed = json.loads(SEED_JSON.read_text(encoding="utf-8"))
    entries = [entry for entry in seed["entries"] if entry["language"] in {"French", "Spanish"}]
    source_results = []

    for entry in entries:
        pdf = CACHE_ROOT / f"{entry['id']}.pdf"
        pages = page_count(pdf)
        term_data = {term["term"]: {"count": 0, "pages": []} for term in TERMS[entry["language"]]}
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
            for term in TERMS[entry["language"]]:
                count = count_patterns(text, term["patterns"])
                if count:
                    item = term_data[term["term"]]
                    item["count"] += count
                    if len(item["pages"]) < 20:
                        item["pages"].append(page)

        hits = []
        for term in TERMS[entry["language"]]:
            data = term_data[term["term"]]
            if data["count"]:
                hits.append(
                    {
                        "term": term["term"],
                        "english": term["english"],
                        "category": term["category"],
                        "count": data["count"],
                        "sample_pages": data["pages"],
                    }
                )

        source_results.append(
            {
                "id": entry["id"],
                "language": entry["language"],
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
    for language in ["French", "Spanish"]:
        for term in TERMS[language]:
            sources = []
            total = 0
            for source_result in source_results:
                if source_result["language"] != language:
                    continue
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
                aggregate.append(
                    {
                        "language": language,
                        "term": term["term"],
                        "english": term["english"],
                        "category": term["category"],
                        "total_count": total,
                        "sources": sources,
                    }
                )

    output = {
        "artifact": "romance_french_spanish_term_anchor_seed",
        "generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "branch": "codex/noether-pc-20260629",
        "status": "term_anchor_seed_from_local_pdf_text_extraction_no_source_text_redistributed",
        "source_seed": "NON_SLAVIC_SOURCE_EVIDENCE_SEED_20260629.json",
        "method": {
            "cache_scope": "PDFs downloaded only to local work/source-cache for analysis; not committed.",
            "extraction": "pdftotext page-level extraction; regex term patterns record counts and page anchors only.",
            "copyright_boundary": "No source passages or PDF contents are redistributed in this artifact.",
            "authority_boundary": "Term anchors are evidence for glossary work, not native/external review or canonical acceptance.",
        },
        "sources_analyzed": source_results,
        "aggregate_term_hits": sorted(aggregate, key=lambda item: (item["language"], item["category"], item["term"])),
        "next_steps": [
            "Inspect high-value pages manually before promoting any French or Spanish term decision.",
            "Separate French and Spanish glossary decisions even when Romance cognates are obvious.",
            "Use compound expressions and page context over high-frequency generic words.",
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
