from __future__ import annotations

import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WORDWEB = ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v8.json"
CORPUS = ROOT / "corpus" / "ROMANCE_CONSOLIDATED_CORPUS_v3.csv"
PREDECESSOR = ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v1.csv"
OUT = ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v2.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def fold(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value or "")
    return "".join(char for char in normalized if not unicodedata.combining(char)).lower()


def key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", fold(value)).strip()


def sha_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest().upper()


def context(line: str, form: str) -> str:
    words = re.findall(r"\S+", line.strip())
    head = (key(form).split() or [""])[0]
    index = 0
    for candidate_index, word in enumerate(words):
        if head and head in key(word).replace(" ", ""):
            index = candidate_index
            break
    start = max(0, index - 8)
    end = min(len(words), index + 13)
    excerpt = " ".join(words[start:end])
    return excerpt + (" …" if end < len(words) else "")


wordweb = json.loads(WORDWEB.read_text(encoding="utf-8-sig"))
corpus = [
    row
    for row in read_csv(CORPUS)
    if row["counting_eligible"].lower() == "true"
    and row["language"] in {"es", "fr", "pt", "gl", "ca", "it", "ro", "rm"}
]
by_language: dict[str, list[dict[str, str]]] = defaultdict(list)
for row in corpus:
    by_language[row["language"]].append(row)

expected_domain = {
    "T01": "ring_theory", "T02": "field_theory", "T03": "ring_theory",
    "T04": "abstract_algebra", "T05": "module_theory", "T06": "ring_theory",
    "T07": "ring_theory", "T08": "ring_theory", "T09": "ring_theory",
    "T10": "ring_theory", "T17": "abstract_algebra", "T18": "abstract_algebra",
    "T19": "abstract_algebra", "T20": "abstract_algebra", "T39": "group_theory",
    "T40": "group_theory", "T41": "proof_register", "T42": "proof_register",
    "T43": "proof_register", "T44": "proof_register", "T45": "proof_register",
    "T46": "proof_register", "T47": "proof_register", "T48": "proof_register",
    "T49": "proof_register", "T50": "proof_register",
}

occurrences: list[dict[str, object]] = []
seen: set[tuple[str, int, str, str]] = set()
for node in wordweb["core_concepts"]:
    term_id = node["term_id"]
    forms_by_language: dict[str, list[str]] = defaultdict(list)
    for form in node.get("forms", []):
        language = form["language"]
        known_keys = {key(item) for item in forms_by_language[language]}
        for value in (form.get("surface_as_inherited"), form.get("lemma_candidate")):
            if value and key(value) and key(value) not in known_keys:
                forms_by_language[language].append(value)
                known_keys.add(key(value))
    for language, forms in forms_by_language.items():
        selected_sources = 0
        for source in by_language.get(language, []):
            if selected_sources >= 3:
                break
            path = Path(source.get("search_text_path") or source["absolute_path"])
            if not path.exists() or path.suffix.lower() not in {".txt", ".tex", ".wikitext"}:
                continue
            lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
            found_in_source = False
            for line_number, line in enumerate(lines, 1):
                normalized_line = " " + key(line) + " "
                for form in forms:
                    normalized_form = key(form)
                    if not normalized_form:
                        continue
                    if not re.search(r"(?<![a-z0-9])" + re.escape(normalized_form) + r"(?![a-z0-9])", normalized_line):
                        continue
                    quote = context(line, form)
                    normalization_group = f"{term_id}:{language}:{normalized_form}"
                    occurrence_id = "OCC-" + sha_text(
                        f"{term_id}|{language}|{source['logical_source_id']}|{line_number}|{normalized_form}|{quote}"
                    )[:16]
                    dedupe = (source["logical_source_id"], line_number, normalized_form, sha_text(quote))
                    if dedupe in seen:
                        continue
                    seen.add(dedupe)
                    tier = (
                        "topic_shelf_context_candidate"
                        if source["domain"] == expected_domain.get(term_id)
                        else "mechanical_context_candidate"
                    )
                    occurrences.append(
                        {
                            "occurrence_id": occurrence_id,
                            "term_id": term_id,
                            "sense_ids": " | ".join(node["sense_ids"]),
                            "concept": node["concept"],
                            "language": language,
                            "surface_query": form,
                            "normalization_group": normalization_group,
                            "logical_source_id": source["logical_source_id"],
                            "record_id": source["record_id"],
                            "source_sha256": source["sha256"],
                            "license_status": source["license_status"],
                            "locator_path": str(path.resolve()),
                            "line_number": line_number,
                            "quote": quote,
                            "quote_sha256": sha_text(quote),
                            "source_domain": source["domain"],
                            "evidence_tier": tier,
                            "sense_review_status": "unreviewed_context_window",
                            "acceptance": "candidate_not_promoted",
                            "source_corpus_version": "ROMANCE_CONSOLIDATED_CORPUS_v3",
                            "human_observation_count": 0,
                            "pilot_claim": False,
                        }
                    )
                    selected_sources += 1
                    found_in_source = True
                    break
                if found_in_source:
                    break

assert occurrences
fields = list(occurrences[0])
with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(occurrences)

coverage = []
for node in wordweb["core_concepts"]:
    rows = [row for row in occurrences if row["term_id"] == node["term_id"]]
    coverage.append(
        {
            "term_id": node["term_id"],
            "concept": node["concept"],
            "occurrences": len(rows),
            "languages_with_context": len({row["language"] for row in rows}),
            "languages": " ".join(sorted({row["language"] for row in rows})),
            "sense_reviewed_occurrences": 0,
            "promotion_status": "blocked_pending_context_review",
        }
    )
coverage_path = ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCE_COVERAGE_v2.csv"
with coverage_path.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(coverage[0]))
    writer.writeheader()
    writer.writerows(coverage)

predecessor_rows = read_csv(PREDECESSOR)
predecessor_ids = {row["occurrence_id"] for row in predecessor_rows}
current_ids = {str(row["occurrence_id"]) for row in occurrences}
new_rows = [row for row in occurrences if row["occurrence_id"] not in predecessor_ids]
removed_ids = sorted(predecessor_ids - current_ids)
summary = {
    "artifact": "ROMANCE_TERM_OCCURRENCES_v2",
    "input_hashes": {
        "PAN_ROMANCE_WORDWEB_v8.json": sha(WORDWEB),
        "ROMANCE_CONSOLIDATED_CORPUS_v3.csv": sha(CORPUS),
        "ROMANCE_TERM_OCCURRENCES_v1.csv": sha(PREDECESSOR),
    },
    "occurrence_count": len(occurrences),
    "terms_with_context": sum(row["occurrences"] > 0 for row in coverage),
    "terms_without_context": sum(row["occurrences"] == 0 for row in coverage),
    "languages": dict(sorted(Counter(str(row["language"]) for row in occurrences).items())),
    "new_vs_v1_count": len(new_rows),
    "new_vs_v1_occurrence_ids": [row["occurrence_id"] for row in new_rows],
    "new_vs_v1_record_ids": sorted({str(row["record_id"]) for row in new_rows}),
    "removed_vs_v1_count": len(removed_ids),
    "removed_vs_v1_occurrence_ids": removed_ids,
    "sense_reviewed": 0,
    "promotion_eligible": 0,
    "human_observation_count": 0,
    "pilot_claim": False,
    "boundary": "Context windows are mechanical candidates. Diacritic-folded aliases share normalization groups and are not summed. New 2024 Rumantsch Grischun windows are not specialist-algebra or semantic attestation until row review. No hit is a bridge decision.",
    "manifest_sha256": sha(OUT),
    "coverage_sha256": sha(coverage_path),
}
summary_path = ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v2.json"
summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
log = ROOT / "qa" / "TERM_OCCURRENCE_EXTRACTION_v2.log"
log.write_text(
    "\n".join(
        [
            f"PASS occurrences={len(occurrences)}",
            f"terms_with_context={summary['terms_with_context']}",
            f"terms_without_context={summary['terms_without_context']}",
            f"languages={summary['languages']}",
            f"new_vs_v1={len(new_rows)} removed_vs_v1={len(removed_ids)}",
            "sense_reviewed=0 promotion_eligible=0 human_observation_count=0 pilot_claim=false",
        ]
    )
    + "\n",
    encoding="utf-8",
)
print(json.dumps(summary, ensure_ascii=False, indent=2))
