import hashlib
import json
import re
import subprocess
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html import unescape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "20260702T013000Z"
SOURCE_ROOT = ROOT / "sources" / "non_slavic_reference_corpus" / f"{STAMP}_controlled_arabic_algebra_source_refresh"
DOWNLOAD_DIR = SOURCE_ROOT / "downloads"
HTML_DIR = SOURCE_ROOT / "html"
TEXT_DIR = SOURCE_ROOT / "extracted_text"
NORMALIZED_DIR = SOURCE_ROOT / "normalized_text"
CONTEXT_DIR = SOURCE_ROOT / "contexts"
LOG_JSON = ROOT / "logs" / f"CONTROLLED_ARABIC_ALGEBRA_SOURCE_REFRESH_{STAMP}.json"
LOG_MD = ROOT / "logs" / f"CONTROLLED_ARABIC_ALGEBRA_SOURCE_REFRESH_{STAMP}.md"

CANDIDATES = [
    {
        "id": "AR-SOHAG-MATH-PROGRAM-2024",
        "title": "Sohag University mathematics program/course descriptions 2024",
        "url": "https://edu.sohag-univ.edu.eg/edu/wp-content/uploads/2025/02/%D8%AA%D9%88%D8%B5%D9%8A%D9%81-%D8%A8%D8%B1%D8%A7%D9%85%D8%AC-%D9%88%D9%85%D9%82%D8%B1%D8%B1%D8%A7%D8%AA-%D9%82%D8%B3%D9%85-%D8%A7%D9%84%D8%B1%D9%8A%D8%A7%D8%B6%D9%8A%D8%A7%D8%AA-2024.pdf",
        "kind": "official_university_course_program_pdf",
        "authority_rank": "official_arabic_course_register_source",
        "filename": "sohag_math_program_2024.pdf",
        "note": "Official Arabic course/program PDF; useful for abstract algebra, rings, fields, ideals, modules, and proof-register terminology.",
    },
    {
        "id": "AR-MUST-RING-THEORY-2019",
        "title": "Mustansiriyah University ring theory lecture PDF",
        "url": "https://uomustansiriyah.edu.iq/media/lectures/12/12_2019_05_29%2101_03_09_PM.pdf",
        "kind": "university_ring_theory_lecture_pdf",
        "authority_rank": "direct_arabic_ring_theory_source",
        "filename": "mustansiriyah_ring_theory_2019.pdf",
        "note": "Direct Arabic university lecture source for ring-theory register; not invariant-theory authority by itself.",
    },
    {
        "id": "AR-MAJMAAH-RINGS-FIELDS",
        "title": "Majmaah University rings and fields course specification",
        "url": "https://www.mu.edu.sa/sites/default/files/MATH444.pdf",
        "kind": "official_course_specification_pdf",
        "authority_rank": "official_arabic_rings_fields_course_register_source",
        "filename": "majmaah_math444_rings_fields_course_spec.pdf",
        "note": "Official Arabic rings/fields course specification; course-register authority, not full textbook authority.",
    },
    {
        "id": "AR-MAJMAAH-RINGS-FIELDS-2017",
        "title": "Majmaah University rings and fields course description 2017",
        "url": "https://www.mu.edu.sa/sites/default/files/content/2017/06/%D8%A7%D9%84%D8%AD%D9%84%D9%82%D8%A7%D8%AA%20%D9%88%D8%A7%D9%84%D8%AD%D9%82%D9%88%D9%84.pdf",
        "kind": "official_course_specification_pdf",
        "authority_rank": "official_arabic_rings_fields_course_register_source",
        "filename": "majmaah_rings_fields_2017_course_spec.pdf",
        "note": "Official Arabic rings/fields course PDF with topics around rings, ideals, quotient fields, homomorphisms, and polynomial rings.",
    },
    {
        "id": "AR-MAJMAAH-RINGS-FIELDS-PROGRAM-SPEC",
        "title": "Majmaah University mathematics program specification with rings and fields row",
        "url": "https://www.mu.edu.sa/sites/default/files/content/2016/04/21.pdf",
        "kind": "official_university_program_pdf",
        "authority_rank": "official_arabic_rings_fields_course_register_source",
        "filename": "majmaah_program_spec_rings_fields_2016.pdf",
        "note": "Official Arabic program specification that names rings and fields and cites ring/field learning resources.",
    },
    {
        "id": "AR-MAJMAAH-COURSE-DESCRIPTION-HTML",
        "title": "Majmaah University Arabic course-description page",
        "url": "https://www.mu.edu.sa/ar/node/2064",
        "kind": "official_university_course_description_html",
        "authority_rank": "official_arabic_course_register_source",
        "filename": "majmaah_course_description_node2064.html",
        "note": "Official Arabic course-description HTML mentioning rings/fields and a King Saud University ring-theory reference.",
    },
    {
        "id": "AR-KSU-DOCTORAL-MATH-PROGRAM",
        "title": "King Saud University doctoral mathematics program plan",
        "url": "https://arts.ksu.edu.sa/sites/arts.ksu.edu.sa/files/imce_images/dkh09kht_lktwrh_fy_lrydyt_1.pdf",
        "kind": "official_doctoral_program_pdf",
        "authority_rank": "official_arabic_advanced_algebra_geometry_course_register_source",
        "filename": "ksu_doctoral_mathematics_program.pdf",
        "note": "Official graduate program register; useful for advanced algebra, algebraic geometry, and algebraic number theory terms.",
    },
    {
        "id": "AR-UQU-MATH-PLAN-2023",
        "title": "Umm Al-Qura mathematics bachelor plan 2023",
        "url": "https://uqu.edu.sa/juc_maths/89496",
        "kind": "official_university_plan_html",
        "authority_rank": "official_arabic_math_course_register_source",
        "filename": "uqu_bachelor_math_plan_2023.html",
        "note": "Official Arabic math plan; useful for undergraduate register and linear/algebra course names.",
    },
    {
        "id": "AR-ANBAR-MATH-PROGRAM",
        "title": "University of Anbar mathematics program PDF",
        "url": "https://www.uoanbar.edu.iq/BasicEducationCollege/catalog/program/4/1/4.pdf",
        "kind": "official_university_program_pdf",
        "authority_rank": "official_arabic_math_course_register_source",
        "filename": "anbar_math_program.pdf",
        "note": "Official Arabic program PDF; useful for course-register triangulation.",
    },
    {
        "id": "ARABICSCHOLAR-INVARIANT-THEORY-KEYWORD",
        "title": "ArabicScholar keyword index for نظرية الثوابت",
        "url": "https://www.arabicscholar.com/keyword/%D9%86%D8%B8%D8%B1%D9%8A%D8%A9-%D8%A7%D9%84%D8%AB%D9%88%D8%A7%D8%A8%D8%AA/",
        "kind": "arabic_academic_index_page",
        "authority_rank": "weak_index_phrase_witness_only",
        "filename": "arabicscholar_invariant_theory_keyword.html",
        "note": "Index/keyword page only. Useful as a search lead and phrase witness; not direct specialist authority or glossary authority.",
    },
]

TERM_GROUPS = {
    "abstract_algebra": ["الجبر المجرد", "جبر مجرد", "الجبر", "جبري"],
    "rings": ["نظرية الحلقات", "حلقة", "حلقات", "الحلقة", "الحلقات", "الحلقي"],
    "fields": ["حقل", "حقول", "الحقل", "الحقول"],
    "ideals": ["مثالي", "مثالية", "مثاليات", "المثالي", "المثاليات"],
    "modules": ["مقاس", "مقاسات", "المقاس", "المقاسات", "مودول", "موديول"],
    "groups": ["زمرة", "زمر", "الزمرة", "الزمر", "مجموعة", "مجموعات", "المجموعة", "المجموعات"],
    "representations": ["تمثيل", "تمثيلات", "التمثيل", "تمثيلي"],
    "polynomials": ["كثيرة حدود", "كثيرات الحدود", "كثير حدود", "متعددة الحدود"],
    "algebraic_geometry": ["الهندسة الجبرية", "هندسة جبرية"],
    "algebraic_number_theory": ["نظرية الأعداد الجبرية", "نظرية الاعداد الجبرية"],
    "galois": ["غالوا", "گالوا", "كالوا"],
    "invariant_theory": ["نظرية الثوابت", "نظرية الثابت", "نظرية اللامتغيرات", "نظرية اللاتغيرات"],
    "geometric_invariant_theory": ["نظرية الثوابت الهندسية", "نظرية الثوابت الهندسية الجبرية"],
    "ring_of_invariants": ["حلقة الثوابت", "حلقات الثوابت", "حلقة اللامتغيرات", "حلقات اللامتغيرات"],
    "binary_form": ["أشكال ثنائية", "شكل ثنائي", "صيغة ثنائية", "صورة ثنائية"],
    "covariant": ["مصاحب", "مصاحبات", "متغاير", "متغايرات", "مرافق", "مرافقات"],
    "proof_grammar": ["تعريف", "مبرهنة", "برهان", "نظرية", "تمرين", "مسألة"],
}


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def normalize_text(text: str) -> str:
    text = unescape(text)
    text = re.sub(r"<script\b.*?</script>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<style\b.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("\u200f", "").replace("\u200e", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def download(candidate: dict) -> dict:
    url = candidate["url"]
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Codex-Noether-Arabic-source-refresh/20260702",
            "Accept": "application/pdf,text/html,*/*",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
            content_type = resp.headers.get("Content-Type", "")
            final_url = resp.geturl()
        return {
            "status": "downloaded",
            "data": data,
            "content_type": content_type,
            "final_url": final_url,
            "error": None,
        }
    except urllib.error.HTTPError as exc:
        return {
            "status": "failed",
            "data": b"",
            "content_type": exc.headers.get("Content-Type", "") if exc.headers else "",
            "final_url": url,
            "error": f"http_{exc.code}",
        }
    except Exception as exc:
        return {
            "status": "failed",
            "data": b"",
            "content_type": "",
            "final_url": url,
            "error": type(exc).__name__ + ": " + str(exc),
        }


def extract_pdf_text(pdf_path: Path, out_path: Path) -> dict:
    proc = subprocess.run(
        ["pdftotext", "-layout", "-enc", "UTF-8", str(pdf_path), str(out_path)],
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    if proc.returncode == 0 and out_path.exists():
        text = out_path.read_text(encoding="utf-8", errors="replace")
        if len(text.strip()) > 50:
            return {
                "status": "extracted",
                "method": "pdftotext",
                "characters": len(text),
                "text_path": rel(out_path),
                "error": None,
            }
    try:
        import fitz

        pieces = []
        with fitz.open(pdf_path) as doc:
            for page in doc:
                pieces.append(page.get_text())
        text = "\n".join(pieces)
        out_path.write_text(text, encoding="utf-8", errors="replace")
        return {
            "status": "extracted" if text.strip() else "empty",
            "method": "pymupdf_fallback",
            "characters": len(text),
            "text_path": rel(out_path),
            "error": None if text.strip() else "empty_text",
        }
    except Exception as exc:
        return {
            "status": "failed",
            "method": "pdftotext_then_pymupdf",
            "characters": 0,
            "text_path": rel(out_path) if out_path.exists() else None,
            "error": (proc.stderr[-1000:] if proc.stderr else "") + " / " + type(exc).__name__ + ": " + str(exc),
        }


def term_counts(text: str) -> tuple[dict, dict]:
    grouped = {}
    values = {}
    for group, terms in TERM_GROUPS.items():
        group_values = {}
        total = 0
        for term in terms:
            count = text.count(term)
            if count:
                group_values[term] = count
                total += count
        if total:
            grouped[group] = total
            values[group] = group_values
    return grouped, values


def contexts(text: str, max_per_group: int = 4) -> dict:
    out = {}
    for group, terms in TERM_GROUPS.items():
        snippets = []
        for term in terms:
            start = 0
            while len(snippets) < max_per_group:
                idx = text.find(term, start)
                if idx < 0:
                    break
                left = max(0, idx - 120)
                right = min(len(text), idx + len(term) + 120)
                snippets.append(
                    {
                        "term": term,
                        "offset": idx,
                        "snippet": text[left:right],
                    }
                )
                start = idx + len(term)
            if len(snippets) >= max_per_group:
                break
        if snippets:
            out[group] = snippets
    return out


def compact_hits(counts: dict) -> list[str]:
    return [f"{key}:{counts[key]}" for key in sorted(counts)]


def classify(candidate: dict, counts: dict, text_chars: int) -> str:
    if candidate["id"] == "ARABICSCHOLAR-INVARIANT-THEORY-KEYWORD":
        return "weak_invariant_theory_index_phrase_witness_no_promotion"
    if counts.get("invariant_theory") or counts.get("ring_of_invariants"):
        return "possible_invariant_phrase_evidence_needs_manual_review_no_promotion"
    if counts.get("rings") or counts.get("fields") or counts.get("ideals") or counts.get("modules"):
        if "ring_theory" in candidate["kind"]:
            return "direct_arabic_ring_theory_source"
        if "course_specification" in candidate["kind"]:
            return "official_arabic_rings_fields_course_register_source"
        return "official_arabic_algebra_register_source"
    if text_chars:
        return "downloaded_text_extracted_low_target_term_yield"
    return "download_failed_or_no_text"


def write_markdown(payload: dict) -> None:
    lines = [
        "# Controlled Arabic Algebra Source Refresh",
        "",
        f"Generated UTC: `{payload['generated_at_utc']}`",
        "",
        "## Summary",
        "",
        f"- Candidate count: `{payload['summary']['candidate_count']}`",
        f"- Downloaded count: `{payload['summary']['downloaded_count']}`",
        f"- Text extracted count: `{payload['summary']['text_extracted_count']}`",
        f"- Official/university algebra-register witnesses: `{payload['summary']['official_or_direct_algebra_register_count']}`",
        f"- Direct ring/rings-fields witnesses: `{payload['summary']['direct_ring_or_rings_fields_count']}`",
        f"- Strong direct Arabic invariant-theory witnesses: `{payload['summary']['strong_direct_invariant_theory_source_count']}`",
        f"- Decision: `{payload['summary']['decision']}`",
        "",
        "## Sources",
        "",
        "| ID | Class | Status | Hits | Local file |",
        "| --- | --- | --- | --- | --- |",
    ]
    for source in payload["sources"]:
        local = source.get("local_path") or source.get("html_path") or ""
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{source['id']}`",
                    f"`{source['evidence_class']}`",
                    f"`{source['download_status']}`",
                    ", ".join(source["compact_hits"]) or "none",
                    f"`{local}`",
                ]
            )
            + " |"
        )
    lines.extend(
        [
            "",
            "## Policy",
            "",
        ]
    )
    for key, value in payload["policy"].items():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Next actions", ""])
    for action in payload["next_actions"]:
        lines.append(f"- {action}")
    lines.append("")
    LOG_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    for directory in [DOWNLOAD_DIR, HTML_DIR, TEXT_DIR, NORMALIZED_DIR, CONTEXT_DIR]:
        directory.mkdir(parents=True, exist_ok=True)

    sources = []
    term_totals = {}
    term_value_totals = {}
    for candidate in CANDIDATES:
        result = download(candidate)
        source = {
            **{k: v for k, v in candidate.items() if k != "filename"},
            "download_status": result["status"],
            "final_url": result["final_url"],
            "content_type": result["content_type"],
            "error": result["error"],
        }
        text = ""
        if result["status"] == "downloaded":
            data = result["data"]
            source["bytes"] = len(data)
            source["sha256"] = sha256_bytes(data)
            is_pdf = candidate["filename"].lower().endswith(".pdf") or data[:4] == b"%PDF"
            if is_pdf:
                local_path = DOWNLOAD_DIR / candidate["filename"]
                local_path.write_bytes(data)
                source["local_path"] = rel(local_path)
                source["file_sha256"] = sha256_file(local_path)
                text_path = TEXT_DIR / (Path(candidate["filename"]).stem + ".txt")
                extraction = extract_pdf_text(local_path, text_path)
                source["extraction"] = extraction
                if text_path.exists():
                    text = text_path.read_text(encoding="utf-8", errors="replace")
                    source["text_path"] = rel(text_path)
            else:
                html_path = HTML_DIR / candidate["filename"]
                html_path.write_bytes(data)
                source["html_path"] = rel(html_path)
                try:
                    text = data.decode("utf-8", errors="replace")
                except Exception:
                    text = ""
        else:
            source["bytes"] = 0

        normalized = normalize_text(text)
        if normalized:
            normalized_path = NORMALIZED_DIR / (Path(candidate["filename"]).stem + ".normalized.txt")
            normalized_path.write_text(normalized, encoding="utf-8")
            counts, values = term_counts(normalized)
            source["normalized_text_path"] = rel(normalized_path)
            source["analysis"] = {
                "characters": len(text),
                "normalized_characters": len(normalized),
                "arabic_letter_count": len(re.findall(r"[\u0600-\u06FF]", normalized)),
                "term_hits": counts,
                "term_values": values,
            }
            context_payload = contexts(normalized)
            context_path = CONTEXT_DIR / (Path(candidate["filename"]).stem + "_contexts.json")
            context_path.write_text(json.dumps(context_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            source["context_path"] = rel(context_path)
            for group, count in counts.items():
                term_totals[group] = term_totals.get(group, 0) + count
            for group, group_values in values.items():
                term_value_totals.setdefault(group, {})
                for term, count in group_values.items():
                    term_value_totals[group][term] = term_value_totals[group].get(term, 0) + count
        else:
            counts = {}
            values = {}
            source["analysis"] = {
                "characters": len(text),
                "normalized_characters": 0,
                "arabic_letter_count": 0,
                "term_hits": {},
                "term_values": {},
            }
        source["compact_hits"] = compact_hits(counts)
        source["evidence_class"] = classify(candidate, counts, len(normalized))
        sources.append(source)

    downloaded_count = sum(1 for source in sources if source["download_status"] == "downloaded")
    text_extracted_count = sum(1 for source in sources if source["analysis"]["normalized_characters"] > 0)
    direct_ring_count = sum(
        1 for source in sources
        if source["evidence_class"] in {
            "direct_arabic_ring_theory_source",
            "official_arabic_rings_fields_course_register_source",
        }
    )
    algebra_count = sum(
        1 for source in sources
        if source["evidence_class"] in {
            "direct_arabic_ring_theory_source",
            "official_arabic_rings_fields_course_register_source",
            "official_arabic_algebra_register_source",
        }
    )
    strong_invariant_ids = [
        source["id"] for source in sources
        if source["evidence_class"] == "direct_arabic_invariant_theory_source"
    ]
    payload = {
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "artifact": "controlled_arabic_algebra_source_refresh",
        "lane": "controlled_arabic",
        "source_root": rel(SOURCE_ROOT),
        "status": "controlled_arabic_algebra_register_strengthened_invariant_theory_gap_remains_open",
        "search_queries_represented": [
            '"نظرية الحلقات" "مثالي" PDF جامعة',
            '"الجبر المجرد" "الحلقات" "المثالية" filetype:pdf',
            '"نظرية الثوابت" "الجبر" "pdf" Arabic mathematics',
            '"نظرية الثوابت" "حلقات الثوابت" filetype:pdf',
        ],
        "summary": {
            "candidate_count": len(sources),
            "downloaded_count": downloaded_count,
            "text_extracted_count": text_extracted_count,
            "official_or_direct_algebra_register_count": algebra_count,
            "direct_ring_or_rings_fields_count": direct_ring_count,
            "strong_direct_invariant_theory_source_count": len(strong_invariant_ids),
            "term_totals": dict(sorted(term_totals.items())),
            "decision": "controlled_arabic_algebra_register_strengthened_no_translation_or_invariant_promotion",
        },
        "sources": sources,
        "accepted_algebra_register_source_ids": [
            source["id"] for source in sources
            if source["evidence_class"] in {
                "direct_arabic_ring_theory_source",
                "official_arabic_rings_fields_course_register_source",
                "official_arabic_algebra_register_source",
            }
        ],
        "strong_direct_invariant_theory_source_ids": strong_invariant_ids,
        "term_values": term_value_totals,
        "policy": {
            "authority_boundary": "Official/university PDFs strengthen Arabic algebra/ring/field course-register evidence but do not close native review.",
            "invariant_boundary": "No direct specialist Arabic invariant-theory, covariant, binary-form, or ring-of-invariants source is promoted by this refresh.",
            "translation_boundary": "This is a source-evidence shelf only; it does not alter translations, glossary rows, or cumulative readers.",
            "non_erasure": "Controlled Arabic remains separate from Farsi, Dari, Tajik, Urdu, Turkish, and other Arabic-script lanes.",
        },
        "next_actions": [
            "Integrate accepted algebra-register IDs into the Arabic/Persianate lane status manifest on the next manifest refresh.",
            "Continue a specialist-only search for direct Arabic invariant theory, covariant, binary-form, and ring-of-invariants sources.",
            "Use these sources for reviewer prompts and term triangulation only until native/domain review accepts specific glossary rows.",
        ],
    }
    LOG_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(payload)
    print(json.dumps({"json": rel(LOG_JSON), "markdown": rel(LOG_MD), "source_root": rel(SOURCE_ROOT), "summary": payload["summary"]}, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
