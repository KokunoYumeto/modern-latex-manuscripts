from __future__ import annotations

import copy
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
WORDWEB = ROOT / "wordweb"
ACCESS = ROOT / "access"
CURATION = ROOT / "curation"
QA = ROOT / "qa"

WORDWEB_V9 = WORDWEB / "PAN_ROMANCE_WORDWEB_v9.json"
ACCESS_V9_JSON = ACCESS / "PAN_ROMANCE_ACCESS_LEDGER_v9.json"
ACCESS_V9_CSV = ACCESS / "PAN_ROMANCE_ACCESS_LEDGER_v9.csv"
GATE_V9 = QA / "ROMANCE_ACCEPTANCE_GATE_v9.json"
MANIFEST_V9 = QA / "SHA256SUMS_v9.csv"

WORDWEB_V10 = WORDWEB / "PAN_ROMANCE_WORDWEB_v10.json"
ACCESS_V10_JSON = ACCESS / "PAN_ROMANCE_ACCESS_LEDGER_v10.json"
ACCESS_V10_CSV = ACCESS / "PAN_ROMANCE_ACCESS_LEDGER_v10.csv"
MII_V10 = ACCESS / "MII_METHOD_v10.md"
EFFECTIVE_LINKS_CSV = CURATION / "CONTROLLED_ROMANCE_TERMINOLOGY_WORDWEB_LINKS_v10.csv"
EFFECTIVE_LINKS_JSON = CURATION / "CONTROLLED_ROMANCE_TERMINOLOGY_WORDWEB_LINKS_v10.json"
CROSSWALK_CSV = CURATION / "NOETHER_ES_FR_WORDWEB_CROSSWALK_v10.csv"
CROSSWALK_JSON = CURATION / "NOETHER_ES_FR_WORDWEB_CROSSWALK_v10.json"
CROSSWALK_MD = CURATION / "NOETHER_ES_FR_WORDWEB_CROSSWALK_v10.md"
ALIGNMENT_AUDIT = QA / "ROMANCE_SEMANTIC_ALIGNMENT_v10.json"
BUILD_LOG = QA / "ROMANCE_SEMANTIC_ALIGNMENT_BUILD_v10.log"

ES_LEDGER = (
    ROOT.parents[2]
    / "noether"
    / "03_translation_workspaces"
    / "romance_rebase_20260717"
    / "work"
    / "spanish"
    / "GERMAN_SPANISH_TERMINOLOGY_LEDGER.csv"
)
FR_LEDGER = (
    ROOT.parents[2]
    / "noether"
    / "03_translation_workspaces"
    / "fr_r823_20260717"
    / "evidence"
    / "GERMAN_FRENCH_TERMINOLOGY_LEDGER.csv"
)

TRANCHES = [f"R823_HG_T{i:03d}" for i in range(1, 7)]
TERM_LEDGERS = {
    tranche: ROOT / tranche / "terminology" / f"{tranche}_TERMINOLOGY_v1.csv"
    for tranche in TRANCHES
}
T006_SEED_V1 = ROOT / "R823_HG_T006" / "semantic" / "R823_HG_T006_clause_map_seed.csv"
T006_MAP_V1 = ROOT / "R823_HG_T006" / "semantic" / "R823_HG_T006_clause_map.csv"
T006_VISUAL_V1 = ROOT / "R823_HG_T006" / "qa" / "R823_HG_T006_VISUAL_QA.md"
T006_SEED_V2 = ROOT / "R823_HG_T006" / "semantic" / "R823_HG_T006_clause_map_seed_v2.csv"
T006_MAP_V2 = ROOT / "R823_HG_T006" / "semantic" / "R823_HG_T006_clause_map_v2.csv"
T006_VISUAL_V2 = ROOT / "R823_HG_T006" / "qa" / "R823_HG_T006_VISUAL_QA_v2.md"
T006_REPAIR = ROOT / "R823_HG_T006" / "qa" / "R823_HG_T006_SEMANTIC_METADATA_REPAIR_v2.json"


EXPECTED_HASHES = {
    WORDWEB_V9: "142785197B744029F7E07BF1D87003167DA6EBD1FAA81502AB4D99D121AA7BAF",
    ACCESS_V9_JSON: "32550AB52D083850D28F6425C02581DB6CA44E6FD3A0BDB5CEFB1E5FE0B37339",
    ACCESS_V9_CSV: "4360CAF4563382B69A70533D6FF14BA06786D8C6E9215F67CAB2F0E907BBC781",
    GATE_V9: "5A2E7269582499E20BAE91B5E205734A757FEB65A3C99D85B9BCD8A25CA5FBE8",
    MANIFEST_V9: "BE97BB77EFCF2EDD8F0B0711099E5CEF03AD54123CDBD5984374F4F87164B870",
    ES_LEDGER: "395C18C21D53C3E439DF95891DE197866548F4EBD0D550453ED83D8CE7B5B9EA",
    FR_LEDGER: "0A7B1704481609CF5C4A8B3B7B5CC03EC59ADC4E511FF39D4A0D6AF910448B77",
    TERM_LEDGERS["R823_HG_T001"]: "5B2DA488BBEE420B966F0E1EF4B1DF14127518D7B724E71B021DFCEB5D51DDB0",
    TERM_LEDGERS["R823_HG_T002"]: "29F5465F1D4088A303EFB56870989ED83F810CA9C273D83F63FE6B33ACB9BB55",
    TERM_LEDGERS["R823_HG_T003"]: "798D56C07C5BFDA7BA4996A89FA64B2A57C2194EC17592E11C44FA370F042F97",
    TERM_LEDGERS["R823_HG_T004"]: "FAF728886168DDC7713346E7E1B1EA37EA7EE2B57FF7F0E204DD1AD7C48FB00E",
    TERM_LEDGERS["R823_HG_T005"]: "0D48DCAB897FC91216376EEC00C3C2FEE5B8C0FF55B37450293EDA7B1C2DDC56",
    TERM_LEDGERS["R823_HG_T006"]: "B958960829A9AFDC6116F2CFCD83217CFF67ACA101BBAB495D32B9B3A1C3ACDF",
    T006_SEED_V1: "FF4DF05B89AFC720E32E2307F320F88E35894425B0E53F7EE47C94E86EDC7DBF",
    T006_MAP_V1: "4A59963DC06E634C2E4C860E1C7F3535C63D1377BC10F29D7B46054523165018",
    T006_VISUAL_V1: "CD2B7B3667466474B886D4CCF89F4C65CFBE8CF6D2ED13389C9857C447ADCB33",
}


CORRECTIONS = {
    "HG13": {
        "effective": "none_not_in_60_concept_spine",
        "class": "false_nearest_match_removed",
        "rationale": "Editorial supplement to another text is not the T33-S1 direct-complement sense.",
    },
    "HG22": {
        "effective": "C2-element",
        "class": "corrected_exact_extension_node",
        "rationale": "Algebraic element has an explicit C2 element node and is not the T06-S1 ideal sense.",
    },
    "HG26": {
        "effective": "none_not_in_60_concept_spine",
        "class": "false_nearest_match_removed",
        "rationale": "Additive sum is not the T14-S1 multiplicative-product sense; no exact core node exists.",
    },
    "HG64": {
        "effective": "none_not_in_60_concept_spine",
        "class": "false_nearest_match_removed",
        "rationale": "Pointwise sum of transformations is not the T16-S1 decomposition sense.",
    },
    "HG72": {
        "effective": "T19-S1",
        "class": "corrected_exact_core_sense",
        "rationale": "The row states an isomorphism, which is T19-S1; T23-S1 is matrix rank.",
    },
    "HG76": {
        "effective": "T18-S1",
        "class": "corrected_exact_core_sense",
        "rationale": "The c+d to C+D equation is additive operation preservation by the homomorphism.",
    },
}


HUMAN_FIELDS = [
    "human_n",
    "human_correct",
    "human_incorrect",
    "human_abstain",
    "human_latency_ms",
    "human_confidence",
    "effect_interval",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def text_sha(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest().upper()


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def csv_scalar(value) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.lower().replace("ß", "ss")
    return " ".join(re.findall(r"[a-z0-9]+", value))


def alternatives(value: str) -> set[str]:
    return {norm(part) for part in re.split(r"\s*(?:;|/)\s*", value or "") if norm(part)}


for path, expected in EXPECTED_HASHES.items():
    require(path.exists(), f"missing pinned input: {path}")
    require(sha(path) == expected, f"pinned input drift: {path}")

v9_manifest_rows = read_csv(MANIFEST_V9)
require(len(v9_manifest_rows) == len({row["relative_path"] for row in v9_manifest_rows}) == 288, "v9 manifest shape changed")
v9_manifest_mismatches = []
for row in v9_manifest_rows:
    path = (ROOT / row["relative_path"]).resolve()
    if not path.exists() or path.stat().st_size != int(row["bytes"]) or sha(path) != row["sha256"]:
        v9_manifest_mismatches.append(row["relative_path"])
require(set(v9_manifest_mismatches) <= {"README.md", "CONTINUATION_CURSOR.md"}, f"unexpected v9 predecessor drift: {v9_manifest_mismatches}")

wordweb_v9 = json.loads(WORDWEB_V9.read_text(encoding="utf-8"))
access_v9 = json.loads(ACCESS_V9_JSON.read_text(encoding="utf-8"))
sense_ids = {sense["sense_id"] for sense in wordweb_v9["senses"]}
c2_ids = {node["concept_id"] for node in wordweb_v9["c2_extension_nodes"]}
senses_by_term = defaultdict(list)
for sense in wordweb_v9["senses"]:
    senses_by_term[sense["term_id"]].append(sense["sense_id"])


# Effective controlled-Romance terminology/WordWeb link surface.
effective_rows = []
all_term_ids = []
for tranche in TRANCHES:
    source_path = TERM_LEDGERS[tranche]
    source_hash = sha(source_path)
    for row in read_csv(source_path):
        term_id = row["term_id"]
        all_term_ids.append(term_id)
        correction = CORRECTIONS.get(term_id)
        original = row.get("wordweb_link", "")
        effective = correction["effective"] if correction else original
        if correction:
            compatibility = correction["class"]
            compatibility_rationale = correction["rationale"]
            change_status = "corrected_v10"
        elif not effective:
            compatibility = "explicit_unlinked_outside_reviewed_spine"
            compatibility_rationale = "No v9 WordWeb link was asserted; v10 does not infer one."
            change_status = "retained_v9"
        elif effective == "none_not_in_60_concept_spine":
            compatibility = "explicit_no_exact_spine_node"
            compatibility_rationale = "The ledger explicitly records that no exact 60-concept spine sense exists."
            change_status = "retained_v9"
        else:
            compatibility = "approved_semantic_or_context_link"
            compatibility_rationale = "Retained after v10 link audit; every target token resolves to a v9 core sense or C2 node."
            change_status = "retained_v9"
        tokens = [part.strip() for part in effective.split("+") if part.strip()]
        if effective and effective != "none_not_in_60_concept_spine":
            require(tokens and set(tokens) <= sense_ids | c2_ids, f"unresolved effective WordWeb link {term_id}: {effective}")
        out = {
            "tranche": tranche,
            "source_ledger_path": source_path.relative_to(ROOT).as_posix(),
            "source_ledger_sha256": source_hash,
            "term_id": term_id,
            "source_term": row["source_term"],
            "target_term": row["target_term"],
            "sense": row["sense"],
            "status": row["status"],
            "source_evidence": row["source_evidence"],
            "original_wordweb_link": original,
            "effective_wordweb_link": effective,
            "link_change_status": change_status,
            "semantic_compatibility_status": compatibility,
            "semantic_compatibility_rationale": compatibility_rationale,
            "alternatives_or_crosswalk": row["alternatives_or_crosswalk"],
            "adverse_evidence": row["adverse_evidence"],
            "source_rationale": row["rationale"],
            "attestation_effect": "none_existing_evidence_only",
            "promotion_effect": "none",
        }
        effective_rows.append(out)

require(len(effective_rows) == len(set(all_term_ids)) == 104, "controlled terminology row topology changed")
require(set(CORRECTIONS) <= set(all_term_ids), "correction row missing")
require(sum(row["link_change_status"] == "corrected_v10" for row in effective_rows) == 6, "correction count mismatch")
effective_fields = list(effective_rows[0])
write_csv(EFFECTIVE_LINKS_CSV, effective_rows, effective_fields)
link_contract = {row["term_id"]: row["effective_wordweb_link"] for row in effective_rows}
link_contract_sha = text_sha(json.dumps(link_contract, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
effective_json = {
    "artifact": "CONTROLLED_ROMANCE_TERMINOLOGY_WORDWEB_LINKS_v10",
    "supersedes_effective_link_fields_in": [path.relative_to(ROOT).as_posix() for path in TERM_LEDGERS.values()],
    "preserves_v1_ledgers": True,
    "row_count": len(effective_rows),
    "correction_count": 6,
    "corrected_term_ids": list(CORRECTIONS),
    "semantic_link_contract_sha256": link_contract_sha,
    "input_hashes": {path.relative_to(ROOT).as_posix(): sha(path) for path in TERM_LEDGERS.values()},
    "claim_boundary": "Link correction and semantic routing only; no attestation, native-validation, form-promotion, or MII claim is added.",
    "rows": effective_rows,
}
write_json(EFFECTIVE_LINKS_JSON, effective_json)


# T006 successor metadata: keep the source/map bytes from v9 and correct only the false starred-column description.
fixed_focus = (
    "the matrix C acts on the left of the displayed unstarred column; stars remain on the reciprocal module "
    "and its generators in the preceding display, and varying bases yields the different representations of one class"
)
for source_path, output_path in ((T006_SEED_V1, T006_SEED_V2), (T006_MAP_V1, T006_MAP_V2)):
    rows = read_csv(source_path)
    require(len(rows) == 8, f"T006 clause-map row count changed: {source_path}")
    changed = 0
    for row in rows:
        if row["segment_id"] == "S063":
            require("starred column" in row["scope_constraints"], "expected historical S063 wording not found")
            row["scope_constraints"] = fixed_focus
            changed += 1
    require(changed == 1, f"T006 S063 repair count mismatch: {source_path}")
    write_csv(output_path, rows, list(rows[0]))

visual_v1_text = T006_VISUAL_V1.read_text(encoding="utf-8")
require(visual_v1_text.count("starred column") == 1, "historical visual-QA wording changed")
visual_v2_text = visual_v1_text.replace(
    "reciprocal construction, starred column, and page number",
    "reciprocal construction, displayed column without star marks (with stars retained on the preceding reciprocal-module notation), and page number",
)
require(
    "reciprocal construction, starred column, and page number" not in visual_v2_text
    and "displayed column without star marks" in visual_v2_text,
    "visual-QA repair failed",
)
T006_VISUAL_V2.write_text(visual_v2_text, encoding="utf-8")
write_json(
    T006_REPAIR,
    {
        "artifact": "R823_HG_T006_SEMANTIC_METADATA_REPAIR_v2",
        "status": "PASS",
        "historical_inputs_preserved": {
            T006_SEED_V1.relative_to(ROOT).as_posix(): sha(T006_SEED_V1),
            T006_MAP_V1.relative_to(ROOT).as_posix(): sha(T006_MAP_V1),
            T006_VISUAL_V1.relative_to(ROOT).as_posix(): sha(T006_VISUAL_V1),
        },
        "successors": {
            T006_SEED_V2.relative_to(ROOT).as_posix(): sha(T006_SEED_V2),
            T006_MAP_V2.relative_to(ROOT).as_posix(): sha(T006_MAP_V2),
            T006_VISUAL_V2.relative_to(ROOT).as_posix(): sha(T006_VISUAL_V2),
        },
        "source_notation": "The displayed column at R823 lines 21249-21251 is unstarred; stars belong to the reciprocal module and generators in the preceding display.",
        "semantic_changes": 1,
        "visual_qa_wording_changes": 1,
        "source_or_target_tex_changes": 0,
        "promotion_effect": "none",
    },
)


# Evidence-preserving crosswalk from the current production ledgers to the existing WordWeb.
es_rows = read_csv(ES_LEDGER)
fr_rows = read_csv(FR_LEDGER)
require(len(es_rows) == 101 and len(fr_rows) == 93, "production terminology ledger count changed")
require([core["term_id"] for core in wordweb_v9["core_concepts"]] == [f"T{i:02d}" for i in range(1, 61)], "WordWeb term order changed")

german_core_map = {}
for index, core in enumerate(wordweb_v9["core_concepts"]):
    source_key = norm(es_rows[index]["source_term"])
    require(source_key and source_key not in german_core_map, f"duplicate German core key: {source_key}")
    german_core_map[source_key] = core["term_id"]

surface_index = {"es": defaultdict(set), "fr": defaultdict(set)}
for core in wordweb_v9["core_concepts"]:
    term_id = core["term_id"]
    for form in core["forms"]:
        language = form["language"]
        if language not in surface_index:
            continue
        for field in ("surface_as_inherited", "lemma_candidate"):
            for candidate in alternatives(form.get(field) or ""):
                surface_index[language][candidate].add(term_id)


def crosswalk_row(language: str, index: int, row: dict[str, str]) -> dict[str, str]:
    source_candidates = set()
    target_candidates = set()
    if language == "es" and index < 60:
        mapped = f"T{index + 1:02d}"
        method = "pinned_spanish_core_row_identity"
        status = "mapped"
        candidates = {mapped}
    else:
        for item in alternatives(row["source_term"]):
            if item in german_core_map:
                source_candidates.add(german_core_map[item])
        for item in alternatives(row["target_term"]):
            target_candidates.update(surface_index[language].get(item, set()))
        common = source_candidates & target_candidates
        if len(common) == 1:
            candidates = common
            mapped = next(iter(common))
            method = "exact_normalized_source_and_target_identity"
            status = "mapped"
        elif not source_candidates and len(target_candidates) == 1:
            candidates = target_candidates
            mapped = next(iter(target_candidates))
            method = "unique_exact_normalized_target_surface"
            status = "mapped"
        elif not target_candidates and len(source_candidates) == 1:
            candidates = source_candidates
            mapped = next(iter(source_candidates))
            method = "unique_exact_normalized_german_core_source"
            status = "mapped"
        else:
            candidates = source_candidates | target_candidates
            mapped = ""
            if source_candidates and target_candidates and not common:
                method = "source_target_exact_match_conflict_no_mapping"
                status = "conflict_held"
            elif candidates:
                method = "nonunique_exact_match_no_mapping"
                status = "ambiguous_held"
            else:
                method = "no_exact_identity_no_inference"
                status = "unmapped_explicit"
    candidate_senses = sorted(sense for term in candidates for sense in senses_by_term[term])
    mapped_senses = sorted(senses_by_term[mapped]) if mapped else []
    if mapped and len(mapped_senses) == 1:
        precision = "term_and_single_sense_exact"
    elif mapped:
        precision = "term_exact_sense_disambiguation_open"
    else:
        precision = "no_mapping"
    row_json = json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return {
        "crosswalk_id": f"{language.upper()}-{index + 1:03d}",
        "language": language,
        "production_ledger_path": ES_LEDGER.as_posix() if language == "es" else FR_LEDGER.as_posix(),
        "production_ledger_sha256": sha(ES_LEDGER if language == "es" else FR_LEDGER),
        "production_data_row": str(index + 1),
        "source_term": row["source_term"],
        "target_term": row["target_term"],
        "sense": row["sense"],
        "status": row["status"],
        "source_evidence": row["source_evidence"],
        "source_excerpt": row.get("source_excerpt", ""),
        "german_source_evidence": row.get("german_source_evidence", ""),
        "decision_note": row.get("decision_note", ""),
        "production_row_sha256": text_sha(row_json),
        "mapping_status": status,
        "mapping_method": method,
        "mapping_precision": precision,
        "wordweb_term_id": mapped,
        "wordweb_candidate_term_ids": ";".join(sorted(candidates)),
        "wordweb_candidate_sense_ids": ";".join(candidate_senses),
        "wordweb_mapped_sense_ids": ";".join(mapped_senses),
        "attestation_effect": "none_existing_production_evidence_preserved",
        "promotion_effect": "none",
        "human_or_MII_effect": "none",
    }


crosswalk_rows = [crosswalk_row("es", index, row) for index, row in enumerate(es_rows)]
crosswalk_rows.extend(crosswalk_row("fr", index, row) for index, row in enumerate(fr_rows))
require(len(crosswalk_rows) == 194, "crosswalk row count mismatch")
require([row["wordweb_term_id"] for row in crosswalk_rows[:60]] == [f"T{i:02d}" for i in range(1, 61)], "Spanish core crosswalk drift")
crosswalk_fields = list(crosswalk_rows[0])
write_csv(CROSSWALK_CSV, crosswalk_rows, crosswalk_fields)

crosswalk_counts = {
    language: dict(Counter(row["mapping_status"] for row in crosswalk_rows if row["language"] == language))
    for language in ("es", "fr")
}
crosswalk_json = {
    "artifact": "NOETHER_ES_FR_WORDWEB_CROSSWALK_v10",
    "row_count": 194,
    "language_rows": {"es": 101, "fr": 93},
    "mapping_status_counts": crosswalk_counts,
    "spanish_core_identity_rows": 60,
    "input_hashes": {
        "wordweb_v9": sha(WORDWEB_V9),
        "spanish_production_ledger": sha(ES_LEDGER),
        "french_production_ledger": sha(FR_LEDGER),
    },
    "method_boundary": (
        "Only pinned Spanish T01-T60 row identity and unique normalized exact source/target identities map automatically. "
        "Ambiguous, conflicting, and absent identities remain explicit; no semantic nearest-neighbor inference is used."
    ),
    "claim_boundary": "This crosswalk preserves existing evidence and decisions. It creates no attestation, promotion, human result, or MII result.",
    "rows": crosswalk_rows,
}
write_json(CROSSWALK_JSON, crosswalk_json)

CROSSWALK_MD.write_text(
    "# Nöther Spanish/French production-ledger ↔ Romance WordWeb crosswalk v10\n\n"
    "This successor binds the current 101-row Spanish and 93-row French production terminology ledgers to the immutable v9 WordWeb without inventing attestations. "
    "The first 60 Spanish rows are the pinned T01–T60 production sequence. Other rows map only when an existing German core source identity or target surface matches uniquely after deterministic normalization. "
    "Ambiguous, conflicting, and absent exact identities remain held or unmapped.\n\n"
    "- Total production rows preserved: `194` (`101` Spanish + `93` French).\n"
    f"- Spanish mapping states: `{json.dumps(crosswalk_counts['es'], ensure_ascii=False, sort_keys=True)}`.\n"
    f"- French mapping states: `{json.dumps(crosswalk_counts['fr'], ensure_ascii=False, sort_keys=True)}`.\n"
    "- Every production row and evidence field is retained in the CSV/JSON; each source row has a canonical SHA-256.\n"
    "- The crosswalk creates no attestation and uses no semantic nearest-neighbor inference.\n"
    "- `attestation_effect`, `promotion_effect`, and `human_or_MII_effect` are uniformly `none`.\n"
    "- Unmapped rows are an integration cursor, not negative evidence about the language or term.\n",
    encoding="utf-8",
)


# WordWeb/access v10 bind the unchanged semantic and diagnostic payloads to the corrected alignment layer.
wordweb_v10 = copy.deepcopy(wordweb_v9)
wordweb_v10["artifact"] = "PAN_ROMANCE_WORDWEB_v10"
wordweb_v10["supersedes_for_semantic_use"] = "PAN_ROMANCE_WORDWEB_v9"
wordweb_v10["v9_retained_as"] = "immutable_predecessor_semantic_payload"
wordweb_v10["production_alignment_v10"] = {
    "status": "PASS_EFFECTIVE_LINKS_AND_ES_FR_CROSSWALK_NO_PROMOTION",
    "effective_link_rows": 104,
    "corrected_link_rows": 6,
    "corrected_term_ids": list(CORRECTIONS),
    "semantic_link_contract_sha256": link_contract_sha,
    "effective_links_csv_sha256": sha(EFFECTIVE_LINKS_CSV),
    "crosswalk_rows": 194,
    "crosswalk_csv_sha256": sha(CROSSWALK_CSV),
    "crosswalk_mapping_status_counts": crosswalk_counts,
    "T006_unstarred_column_metadata_successor": T006_REPAIR.relative_to(ROOT).as_posix(),
    "attestation_effect": "none",
    "core_form_promotions": 0,
    "human_observations": 0,
}
wordweb_v10["input_hashes_v10"] = {
    "wordweb_v9_preserved": sha(WORDWEB_V9),
    "effective_links_json": sha(EFFECTIVE_LINKS_JSON),
    "production_crosswalk_json": sha(CROSSWALK_JSON),
    "T006_metadata_repair": sha(T006_REPAIR),
    "builder_v10": sha(Path(__file__).resolve()),
}
write_json(WORDWEB_V10, wordweb_v10)

access_v10 = copy.deepcopy(access_v9)
access_v10["artifact"] = "PAN_ROMANCE_ACCESS_LEDGER_v10"
access_v10["supersedes"] = "PAN_ROMANCE_ACCESS_LEDGER_v9"
access_v10["method"] = "MII_METHOD_v10"
access_v10["status"] = "complete_106_by_9_design_grid_v10_alignment_bound_zero_human_data"
access_v10["input_hashes_v10"] = {
    "access_v9_preserved": sha(ACCESS_V9_JSON),
    "wordweb_v10": sha(WORDWEB_V10),
    "production_crosswalk_csv": sha(CROSSWALK_CSV),
    "effective_links_csv": sha(EFFECTIVE_LINKS_CSV),
    "builder_v10": sha(Path(__file__).resolve()),
}
access_v10["production_alignment_v10"] = copy.deepcopy(wordweb_v10["production_alignment_v10"])
access_v10["claim_boundary"] = (
    "Empirical MII remains zero observations. V10 repairs semantic routing and binds production ledgers without changing "
    "orthographic diagnostics, human fields, pilot eligibility, or form-promotion status."
)
for row in access_v10["rows"]:
    row["method_version"] = "MII_METHOD_v10"
require(len(access_v10["rows"]) == 954, "access row count changed")
require(all(all(row[field] is None for field in HUMAN_FIELDS) for row in access_v10["rows"]), "human data leak")
require(not any(row["pilot_eligible"] for row in access_v10["rows"]), "pilot eligibility leak")
require(access_v10["form_promotion_count"] == 0, "form promotion leak")
write_json(ACCESS_V10_JSON, access_v10)
access_fields = list(access_v10["rows"][0])
write_csv(
    ACCESS_V10_CSV,
    [{key: csv_scalar(value) for key, value in row.items()} for row in access_v10["rows"]],
    access_fields,
)

MII_V10.write_text(
    "# Marginal-access implementation v10\n\n"
    "`PAN_ROMANCE_WORDWEB_v10` and `PAN_ROMANCE_ACCESS_LEDGER_v10` preserve the v9 semantic and orthographic payloads while binding the corrected controlled-Romance terminology links and the Spanish/French production-ledger crosswalk. "
    "The access ledger remains exactly 106 senses × 9 declared cohorts = 954 rows.\n\n"
    "Empirical MII remains **zero human observations**. All seven human-result fields are null/empty on all 954 rows, every row is `pilot_eligible=false`, and there are zero form promotions. "
    "Orthographic proxy diagnostics do not measure intelligibility and do not feed vocabulary or grammar decisions.\n\n"
    "The v10 crosswalk preserves existing Spanish/French evidence and maps only pinned or unique exact identities. It creates no attestation or human result. "
    "The 33 senses without accepted corpus support remain explicit source gaps; the 53 zero-body routes remain acquisition gaps. Neither is relabelled as a negative intelligibility result.\n\n"
    "A future human protocol still requires participant-level language/variety, mathematical-literacy, cross-Romance exposure, randomized item order, responses/abstentions, latency, confidence, uncertainty, consent, and review metadata. "
    "Until such records exist, no empirical-MII, scalar-readiness, pilot, or controlled-form promotion claim is authorized.\n",
    encoding="utf-8",
)


alignment_audit = {
    "artifact": "ROMANCE_SEMANTIC_ALIGNMENT_v10",
    "status": "PASS",
    "predecessor_v9": {
        "wordweb_sha256": sha(WORDWEB_V9),
        "access_json_sha256": sha(ACCESS_V9_JSON),
        "access_csv_sha256": sha(ACCESS_V9_CSV),
        "gate_sha256": sha(GATE_V9),
        "manifest_sha256": sha(MANIFEST_V9),
        "manifest_rows": 288,
        "live_mismatches": v9_manifest_mismatches,
    },
    "controlled_terminology": {
        "source_rows": 104,
        "effective_rows": 104,
        "corrections": 6,
        "corrected_term_ids": list(CORRECTIONS),
        "resolved_link_tokens": sum(
            len([part for part in row["effective_wordweb_link"].split("+") if part.strip()])
            for row in effective_rows
            if row["effective_wordweb_link"] not in {"", "none_not_in_60_concept_spine"}
        ),
        "semantic_link_contract_sha256": link_contract_sha,
    },
    "T006_metadata": {
        "status": "PASS_UNSTARRED_COLUMN_SUCCESSORS",
        "source_or_target_tex_changes": 0,
        "repair_sha256": sha(T006_REPAIR),
    },
    "production_crosswalk": {
        "rows": 194,
        "language_rows": {"es": 101, "fr": 93},
        "mapping_status_counts": crosswalk_counts,
        "spanish_core_identity_rows": 60,
        "attestation_effect_rows_non_none": 0,
        "promotion_effect_rows_non_none": 0,
    },
    "wordweb_v10": {
        "sha256": sha(WORDWEB_V10),
        "concepts": 60,
        "senses": 106,
        "c2_nodes": 39,
        "evidence_records": 802,
        "supported_senses": 73,
        "unsupported_senses": 33,
        "core_form_promotions": 0,
    },
    "access_v10": {
        "json_sha256": sha(ACCESS_V10_JSON),
        "csv_sha256": sha(ACCESS_V10_CSV),
        "rows": 954,
        "human_observations": 0,
        "pilot_eligible_rows": 0,
        "form_promotions": 0,
    },
    "claim_boundary": "Infrastructure alignment PASS; empirical Romance research remains incomplete and no new linguistic claim is made.",
}
write_json(ALIGNMENT_AUDIT, alignment_audit)

log_lines = [
    "PASS ROMANCE_SEMANTIC_ALIGNMENT_v10",
    f"v9_predecessor_manifest=288 mismatches={','.join(v9_manifest_mismatches) or 'none'}",
    f"effective_links=104 corrections=6 corrected={','.join(CORRECTIONS)} contract_sha256={link_contract_sha}",
    f"T006_metadata=PASS seed_v2={sha(T006_SEED_V2)} map_v2={sha(T006_MAP_V2)} visual_v2={sha(T006_VISUAL_V2)}",
    f"crosswalk=194 es={crosswalk_counts['es']} fr={crosswalk_counts['fr']} attestations_added=0 promotions=0",
    f"wordweb_v10={sha(WORDWEB_V10)} concepts=60 senses=106 evidence=802 supported=73 unsupported=33",
    f"access_v10_json={sha(ACCESS_V10_JSON)} csv={sha(ACCESS_V10_CSV)} rows=954 human=0 pilot=0 promotions=0",
    "empirical_MII=0 diagnostics_do_not_measure_intelligibility",
]
BUILD_LOG.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
print("\n".join(log_lines))
