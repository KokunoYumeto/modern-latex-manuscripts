import datetime
import hashlib
import json
import pathlib
import re
import subprocess
import unicodedata


CACHE_ROOT = pathlib.Path("work/source-cache/persian_arabic_20260629")
OUT_DIR = pathlib.Path("work/github-api-payloads/noether-slavic-handoff/20260629")
OUT_JSON = OUT_DIR / "PERSIAN_FAMILY_ARABIC_TERM_ANCHOR_SEED_20260629.json"

SOURCES = [
    {
        "id": "fa_iut_behboodi_advanced_algebra",
        "sublane": "fa_IR",
        "language": "Persian/Farsi",
        "title": "جبر پیشرفته",
        "url": "https://people.iut.ac.ir/sites/default/files/users/behboodi/course_files/advanced_algebra_dr._behboodi.pdf",
        "evidence_role": ["advanced_algebra", "terminology_seed"],
    },
    {
        "id": "fa_pnu_ring_module_book_preview",
        "sublane": "fa_IR",
        "language": "Persian/Farsi",
        "title": "مباحثی در نظریه حلقه و مدول",
        "url": "https://press.pnu.ac.ir/book_30094.pdf",
        "evidence_role": ["ring_module_register", "license_review_needed"],
    },
    {
        "id": "fa_shahrood_noncomm_prime_ideals",
        "sublane": "fa_IR",
        "language": "Persian/Farsi",
        "title": "ایده آل های اول الحاقی روی حلقه های ناجابجایی",
        "url": "https://shahroodut.ac.ir/fa/thesis/files/somefiles/sf_QA37.pdf",
        "evidence_role": ["research_register", "noncommutative_rings"],
    },
    {
        "id": "prs_afghan_algebra_momand",
        "sublane": "prs_AF",
        "language": "Dari/Afghanistan Persian",
        "title": "Algebra",
        "url": "https://ecampus-afghanistan.org/wp-content/uploads/2021/10/Algebra-Abdullah-Momand.pdf",
        "evidence_role": ["educational_algebra", "dari_register_seed"],
    },
    {
        "id": "ar_mustansiriyah_abstract_algebra",
        "sublane": "ar",
        "language": "Arabic",
        "title": "مبادئ الجبر المجرد",
        "url": "https://uomustansiriyah.edu.iq/media/attachments/192/192_2019_10_20%2108_53_36_PM.pdf",
        "evidence_role": ["abstract_algebra", "undergraduate_register"],
    },
    {
        "id": "ar_mosul_ring_theory_2025",
        "sublane": "ar",
        "language": "Arabic",
        "title": "جبر الحلقات / Rings Theory",
        "url": "https://uomosul.edu.iq/education/wp-content/uploads/sites/18/2025/05/%D8%AC%D8%A8%D8%B1-%D8%A7%D9%84%D8%AD%D9%84%D9%82%D8%A7%D8%AA-RINGS-THEORY_compressed.pdf",
        "evidence_role": ["ring_theory", "arabic_reinforcement"],
    },
    {
        "id": "ar_archive_ring_fields",
        "sublane": "ar",
        "language": "Arabic",
        "title": "الحلقات والحقول",
        "url": "https://archive.org/download/Ringieldhe/Ringieldhe.pdf",
        "evidence_role": ["rings_fields", "arabic_reinforcement", "license_review_needed"],
    },
    {
        "id": "ar_jmilne_group_theory",
        "sublane": "ar",
        "language": "Arabic",
        "title": "Group Theory Arabic notes",
        "url": "https://www.jmilne.org/math/CourseNotes/GTarabic.pdf",
        "evidence_role": ["group_theory", "translation_register"],
    },
    {
        "id": "ar_mu_rings_fields_course_spec",
        "sublane": "ar",
        "language": "Arabic",
        "title": "الحلقات والحقول",
        "url": "https://www.mu.edu.sa/sites/default/files/content/2017/06/%D8%A7%D9%84%D8%AD%D9%84%D9%82%D8%A7%D8%AA%20%D9%88%D8%A7%D9%84%D8%AD%D9%82%D9%88%D9%84.pdf",
        "evidence_role": ["course_scope", "rings_fields"],
    },
    {
        "id": "ar_mustansiriyah_ring_theory_course",
        "sublane": "ar",
        "language": "Arabic",
        "title": "Ring theory course PDF",
        "url": "https://uomustansiriyah.edu.iq/media/lectures/12/12_2019_05_29%2101_03_09_PM.pdf",
        "evidence_role": ["ring_theory", "course_register"],
    },
]

PERSIAN_TERMS = [
    {"term": "جبر", "english": "algebra", "category": "algebra_core", "patterns": [r"جبر"]},
    {"term": "حلقه", "english": "ring", "category": "ring_theory", "patterns": [r"حلقه"]},
    {"term": "حلقه جابجایی", "english": "commutative ring", "category": "ring_theory", "patterns": [r"حلقه\s+جابجایی", r"حلقه\s+جابجايی"]},
    {"term": "حلقه ناجابجایی", "english": "noncommutative ring", "category": "ring_theory", "patterns": [r"حلقه\s+ناجابجایی", r"حلقه\s+ناجابجايی"]},
    {"term": "میدان", "english": "field", "category": "field_theory", "patterns": [r"میدان", r"ميدان"]},
    {"term": "ایده‌آل", "english": "ideal", "category": "ring_theory", "patterns": [r"ایده.?آل", r"ايده.?آل", r"ایده\s+ال", r"ايده\s+ال"]},
    {"term": "ایده‌آل اول", "english": "prime ideal", "category": "ring_theory", "patterns": [r"ایده.?آل(?:\s+های)?\s+اول", r"ايده.?آل(?:\s+های)?\s+اول"]},
    {"term": "ایده‌آل ماکسیمال", "english": "maximal ideal", "category": "ring_theory", "patterns": [r"ایده.?آل(?:\s+های)?\s+ماکسیمال", r"ايده.?آل(?:\s+های)?\s+ماکسیمال"]},
    {"term": "مدول", "english": "module", "category": "module_theory", "patterns": [r"مدول"]},
    {"term": "زیرمدول", "english": "submodule", "category": "module_theory", "patterns": [r"زیر\s?مدول", r"زير\s?مدول"]},
    {"term": "مدول آزاد", "english": "free module", "category": "module_theory", "patterns": [r"مدول\s+آزاد"]},
    {"term": "مدول چپ", "english": "left module", "category": "module_theory", "patterns": [r"مدول\s+چپ"]},
    {"term": "مدول راست", "english": "right module", "category": "module_theory", "patterns": [r"مدول\s+راست"]},
    {"term": "نوتری", "english": "Noetherian", "category": "noetherian", "patterns": [r"نوتری", r"نوتر"]},
    {"term": "آرتینی", "english": "Artinian", "category": "finiteness", "patterns": [r"آرتینی", r"آرتينی"]},
    {"term": "نیم‌ساده", "english": "semisimple", "category": "representation_theory", "patterns": [r"نیم.?ساده", r"نيم.?ساده"]},
    {"term": "ساده", "english": "simple", "category": "representation_theory", "patterns": [r"ساده"]},
    {"term": "نمایش", "english": "representation", "category": "representation_theory", "patterns": [r"نمایش", r"نمايش"]},
    {"term": "همریختی", "english": "homomorphism", "category": "morphism", "patterns": [r"همریختی", r"همريختی", r"همریخت", r"همريخت"]},
    {"term": "یکریختی", "english": "isomorphism", "category": "morphism", "patterns": [r"یکریختی", r"يكريختی", r"یکریخت", r"يكريخت"]},
    {"term": "خودریختی", "english": "automorphism", "category": "morphism", "patterns": [r"خودریختی", r"خودريختی", r"خودریخت", r"خودريخت"]},
    {"term": "ضرب تانسوری", "english": "tensor product", "category": "module_theory", "patterns": [r"ضرب\s+تانسوری", r"ضرب\s+تنسوری"]},
]

ARABIC_TERMS = [
    {"term": "جبر", "english": "algebra", "category": "algebra_core", "patterns": [r"جبر"]},
    {"term": "حلقة", "english": "ring", "category": "ring_theory", "patterns": [r"حلق(?:ة|ات|ه)"]},
    {"term": "حلقة تبديلية", "english": "commutative ring", "category": "ring_theory", "patterns": [r"حلق(?:ة|ات)?\s+تبديلية", r"حلق(?:ة|ات)?\s+ابدالية"]},
    {"term": "حقل", "english": "field", "category": "field_theory", "patterns": [r"حق(?:ل|ول)"]},
    {"term": "جسم", "english": "field/division ring", "category": "field_theory", "patterns": [r"جسم", r"أجسام", r"اجسام"]},
    {"term": "مثالية", "english": "ideal", "category": "ring_theory", "patterns": [r"مثالي(?:ة|ات)?", r"المثالي(?:ة|ات)?"]},
    {"term": "مثالية أولية", "english": "prime ideal", "category": "ring_theory", "patterns": [r"مثالي(?:ة|ات)?\s+أولية", r"مثالي(?:ة|ات)?\s+اولية"]},
    {"term": "مثالية عظمى", "english": "maximal ideal", "category": "ring_theory", "patterns": [r"مثالي(?:ة|ات)?\s+عظمى"]},
    {"term": "مقاس", "english": "module", "category": "module_theory", "patterns": [r"مقاس(?:ات)?"]},
    {"term": "موديول", "english": "module", "category": "module_theory", "patterns": [r"موديول(?:ات)?"]},
    {"term": "نوتري", "english": "Noetherian", "category": "noetherian", "patterns": [r"نوتري", r"نوثري", r"Noetherian", r"Noether"]},
    {"term": "آرتيني", "english": "Artinian", "category": "finiteness", "patterns": [r"آرتيني", r"ارتيني", r"Artinian", r"Artin"]},
    {"term": "تمثيل", "english": "representation", "category": "representation_theory", "patterns": [r"تمثيل(?:ات)?"]},
    {"term": "غير قابل للاختزال", "english": "irreducible", "category": "representation_theory", "patterns": [r"غير\s+قابل(?:ة)?\s+للاختزال"]},
    {"term": "شبه بسيط", "english": "semisimple", "category": "representation_theory", "patterns": [r"شبه\s+بسيط", r"نصف\s+بسيط"]},
    {"term": "تشاكل", "english": "homomorphism", "category": "morphism", "patterns": [r"تشاكل(?:ات)?"]},
    {"term": "تماثل", "english": "isomorphism", "category": "morphism", "patterns": [r"تماثل(?:ات)?"]},
    {"term": "تجانس", "english": "homomorphism", "category": "morphism", "patterns": [r"تجانس(?:ات)?"]},
    {"term": "جداء تنسوري", "english": "tensor product", "category": "module_theory", "patterns": [r"جداء\s+تنسوري", r"ضرب\s+تنسوري"]},
]


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"[\u200e\u200f\u202a-\u202e]", "", text)
    text = text.replace("\u200c", " ")
    text = text.replace("ي", "ی").replace("ك", "ک")
    text = text.replace("أ", "ا").replace("إ", "ا").replace("آ", "آ")
    text = re.sub(r"[\u064b-\u065f\u0670]", "", text)
    return text


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
    text = normalize(text)
    return sum(len(re.findall(pattern, text, flags=re.IGNORECASE)) for pattern in patterns)


def terms_for_sublane(sublane: str) -> list[dict]:
    return ARABIC_TERMS if sublane == "ar" else PERSIAN_TERMS


def main() -> None:
    source_results = []
    for source in SOURCES:
        pdf = CACHE_ROOT / f"{source['id']}.pdf"
        pages = page_count(pdf)
        terms = terms_for_sublane(source["sublane"])
        term_data = {term["term"]: {"count": 0, "pages": []} for term in terms}
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
            for term in terms:
                count = count_patterns(text, term["patterns"])
                if count:
                    item = term_data[term["term"]]
                    item["count"] += count
                    if len(item["pages"]) < 20:
                        item["pages"].append(page)

        hits = []
        for term in terms:
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
                **source,
                "local_cache_sha256": sha256(pdf),
                "local_cache_bytes": pdf.stat().st_size,
                "pages": pages,
                "text_nonempty_pages": nonempty_pages,
                "extraction_errors": extraction_errors,
                "term_hits": sorted(hits, key=lambda item: (item["category"], item["term"])),
            }
        )

    aggregate = []
    for sublane in ["fa_IR", "prs_AF", "ar"]:
        terms = terms_for_sublane(sublane)
        for term in terms:
            sources = []
            total = 0
            for source_result in source_results:
                if source_result["sublane"] != sublane:
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
                item = {
                    "sublane": sublane,
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
        "artifact": "persian_family_arabic_term_anchor_seed",
        "generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "branch": "codex/noether-pc-20260629",
        "status": "term_anchor_seed_from_local_pdf_text_extraction_no_source_text_redistributed",
        "method": {
            "cache_scope": "PDFs downloaded only to local work/source-cache for analysis; not committed.",
            "extraction": "pdftotext page-level extraction; only counts and page anchors are recorded.",
            "normalization": "Arabic/Persian Yeh/Kaf normalization, ZWNJ spacing, and Arabic diacritic stripping are applied for counting.",
            "copyright_boundary": "No source passages or PDF contents are redistributed in this artifact.",
            "authority_boundary": "Term anchors are evidence for glossary work, not native/external review or canonical acceptance.",
        },
        "sources_analyzed": source_results,
        "aggregate_term_hits": sorted(aggregate, key=lambda item: (item["sublane"], item["category"], item["term"])),
        "known_gaps": [
            "Tajik Cyrillic remains a separate unresolved sublane; these Persian/Arabic-script anchors do not cover it.",
            "Arabic module terminology is especially variable and requires native mathematical review.",
            "Dari/Afghanistan Persian is represented by one educational algebra witness only.",
            "Several Arabic reinforcement PDFs need license/provenance review before any reuse beyond URL and term-anchor metadata.",
        ],
        "next_steps": [
            "Manually inspect high-value pages before promoting any term decision.",
            "Separate fa_IR, prs_AF, tg_Cyrl_TJ, and ar in manifests and glossaries.",
            "Add Tajik Cyrillic sources before any Persian-family cross-register table is promoted.",
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
