from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

import validate_romance_tranche_v9 as v9


ROOT = Path(__file__).resolve().parent.parent
QA = ROOT / "qa"
WORDWEB = ROOT / "wordweb"
ACCESS = ROOT / "access"
CURATION = ROOT / "curation"

README = ROOT / "README.md"
CURSOR = ROOT / "CONTINUATION_CURSOR.md"
WORDWEB_V9 = WORDWEB / "PAN_ROMANCE_WORDWEB_v9.json"
ACCESS_V9_JSON = ACCESS / "PAN_ROMANCE_ACCESS_LEDGER_v9.json"
ACCESS_V9_CSV = ACCESS / "PAN_ROMANCE_ACCESS_LEDGER_v9.csv"
GATE_V9 = QA / "ROMANCE_ACCEPTANCE_GATE_v9.json"
MANIFEST_V9 = QA / "SHA256SUMS_v9.csv"

WORDWEB_V10 = WORDWEB / "PAN_ROMANCE_WORDWEB_v10.json"
ACCESS_V10_JSON = ACCESS / "PAN_ROMANCE_ACCESS_LEDGER_v10.json"
ACCESS_V10_CSV = ACCESS / "PAN_ROMANCE_ACCESS_LEDGER_v10.csv"
MII_V10 = ACCESS / "MII_METHOD_v10.md"
LINKS_CSV = CURATION / "CONTROLLED_ROMANCE_TERMINOLOGY_WORDWEB_LINKS_v10.csv"
LINKS_JSON = CURATION / "CONTROLLED_ROMANCE_TERMINOLOGY_WORDWEB_LINKS_v10.json"
CROSSWALK_CSV = CURATION / "NOETHER_ES_FR_WORDWEB_CROSSWALK_v10.csv"
CROSSWALK_JSON = CURATION / "NOETHER_ES_FR_WORDWEB_CROSSWALK_v10.json"
CROSSWALK_MD = CURATION / "NOETHER_ES_FR_WORDWEB_CROSSWALK_v10.md"
ALIGNMENT_AUDIT = QA / "ROMANCE_SEMANTIC_ALIGNMENT_v10.json"
BUILD_LOG = QA / "ROMANCE_SEMANTIC_ALIGNMENT_BUILD_v10.log"
BUILDER = ROOT / "scripts" / "build_semantic_alignment_v10.py"
MANIFEST_V10 = QA / "SHA256SUMS_v10.csv"
GATE_V10 = QA / "ROMANCE_ACCEPTANCE_GATE_v10.json"
GATE_LOG_V10 = QA / "ROMANCE_ACCEPTANCE_GATE_v10.log"

ES_LEDGER = (
    ROOT.parents[2] / "noether" / "03_translation_workspaces" / "romance_rebase_20260717"
    / "work" / "spanish" / "GERMAN_SPANISH_TERMINOLOGY_LEDGER.csv"
)
FR_LEDGER = (
    ROOT.parents[2] / "noether" / "03_translation_workspaces" / "fr_r823_20260717"
    / "evidence" / "GERMAN_FRENCH_TERMINOLOGY_LEDGER.csv"
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
EXPECTED_LINK_CONTRACT = "0EEC70319DA18D5321C6B05FC9D27F270A9121BAD1E7901C9D8CFB5133B5B5B7"
CORRECTIONS = {
    "HG13": (
        "none_not_in_60_concept_spine", "false_nearest_match_removed",
        "Editorial supplement to another text is not the T33-S1 direct-complement sense.",
    ),
    "HG22": (
        "C2-element", "corrected_exact_extension_node",
        "Algebraic element has an explicit C2 element node and is not the T06-S1 ideal sense.",
    ),
    "HG26": (
        "none_not_in_60_concept_spine", "false_nearest_match_removed",
        "Additive sum is not the T14-S1 multiplicative-product sense; no exact core node exists.",
    ),
    "HG64": (
        "none_not_in_60_concept_spine", "false_nearest_match_removed",
        "Pointwise sum of transformations is not the T16-S1 decomposition sense.",
    ),
    "HG72": (
        "T19-S1", "corrected_exact_core_sense",
        "The row states an isomorphism, which is T19-S1; T23-S1 is matrix rank.",
    ),
    "HG76": (
        "T18-S1", "corrected_exact_core_sense",
        "The c+d to C+D equation is additive operation preservation by the homomorphism.",
    ),
}
FIXED_T006_FOCUS = (
    "the matrix C acts on the left of the displayed unstarred column; stars remain on the reciprocal module "
    "and its generators in the preceding display, and varying bases yields the different representations of one class"
)
HUMAN_FIELDS = [
    "human_n", "human_correct", "human_incorrect", "human_abstain",
    "human_latency_ms", "human_confidence", "effect_interval",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def text_sha(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest().upper()


def jread(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["relative_path", "bytes", "sha256"], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


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


def verify_v9_predecessor(core_only: bool) -> tuple[int, list[str]]:
    for path, expected in EXPECTED_HASHES.items():
        require(path.exists() and sha(path) == expected, f"pinned v9/input drift: {path}")
    rows = read_csv(MANIFEST_V9)
    require(len(rows) == len({row["relative_path"] for row in rows}) == 288, "v9 manifest shape changed")
    mismatches = []
    for row in rows:
        path = (ROOT / row["relative_path"]).resolve()
        if not path.exists() or path.stat().st_size != int(row["bytes"]) or sha(path) != row["sha256"]:
            mismatches.append(row["relative_path"])
    if core_only:
        require(not mismatches, f"v9 manifest mismatch before successor docs: {mismatches}")
    else:
        require(set(mismatches) <= {"README.md", "CONTINUATION_CURSOR.md"}, f"unexpected v9 drift: {mismatches}")
    return len(rows), mismatches


def expected_link_rows(wordweb_v9: dict) -> list[dict[str, str]]:
    sense_ids = {sense["sense_id"] for sense in wordweb_v9["senses"]}
    c2_ids = {node["concept_id"] for node in wordweb_v9["c2_extension_nodes"]}
    output = []
    term_ids = []
    for tranche in TRANCHES:
        source_path = TERM_LEDGERS[tranche]
        source_hash = sha(source_path)
        for row in read_csv(source_path):
            term_id = row["term_id"]
            term_ids.append(term_id)
            original = row.get("wordweb_link", "")
            if term_id in CORRECTIONS:
                effective, compatibility, rationale = CORRECTIONS[term_id]
                change = "corrected_v10"
            elif not original:
                effective = original
                compatibility = "explicit_unlinked_outside_reviewed_spine"
                rationale = "No v9 WordWeb link was asserted; v10 does not infer one."
                change = "retained_v9"
            elif original == "none_not_in_60_concept_spine":
                effective = original
                compatibility = "explicit_no_exact_spine_node"
                rationale = "The ledger explicitly records that no exact 60-concept spine sense exists."
                change = "retained_v9"
            else:
                effective = original
                compatibility = "approved_semantic_or_context_link"
                rationale = "Retained after v10 link audit; every target token resolves to a v9 core sense or C2 node."
                change = "retained_v9"
            if effective and effective != "none_not_in_60_concept_spine":
                require(
                    {part.strip() for part in effective.split("+") if part.strip()} <= sense_ids | c2_ids,
                    f"unresolved link {term_id}: {effective}",
                )
            output.append({
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
                "link_change_status": change,
                "semantic_compatibility_status": compatibility,
                "semantic_compatibility_rationale": rationale,
                "alternatives_or_crosswalk": row["alternatives_or_crosswalk"],
                "adverse_evidence": row["adverse_evidence"],
                "source_rationale": row["rationale"],
                "attestation_effect": "none_existing_evidence_only",
                "promotion_effect": "none",
            })
    require(len(output) == len(set(term_ids)) == 104, "controlled terminology topology changed")
    return output


def validate_links(wordweb_v9: dict) -> dict:
    expected = expected_link_rows(wordweb_v9)
    actual = read_csv(LINKS_CSV)
    require(actual == expected, "effective-link CSV differs from independent reconstruction")
    contract = {row["term_id"]: row["effective_wordweb_link"] for row in actual}
    contract_sha = text_sha(json.dumps(contract, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
    require(contract_sha == EXPECTED_LINK_CONTRACT, "approved semantic-link contract changed")
    data = jread(LINKS_JSON)
    require(data["rows"] == actual and data["row_count"] == 104 and data["correction_count"] == 6, "link JSON mismatch")
    require(data["corrected_term_ids"] == list(CORRECTIONS), "corrected term order/set changed")
    require(data["semantic_link_contract_sha256"] == contract_sha, "link contract hash mismatch")
    require(all(row["attestation_effect"].startswith("none") and row["promotion_effect"] == "none" for row in actual), "link claim leak")
    return {"rows": 104, "corrections": 6, "contract_sha256": contract_sha}


def validate_t006() -> dict:
    for old_path, new_path in ((T006_SEED_V1, T006_SEED_V2), (T006_MAP_V1, T006_MAP_V2)):
        old_rows = read_csv(old_path)
        new_rows = read_csv(new_path)
        require(len(old_rows) == len(new_rows) == 8, f"T006 map topology changed: {old_path.name}")
        expected = copy.deepcopy(old_rows)
        changed = 0
        for row in expected:
            if row["segment_id"] == "S063":
                require("starred column" in row["scope_constraints"], "historical T006 defect missing")
                row["scope_constraints"] = FIXED_T006_FOCUS
                changed += 1
        require(changed == 1 and new_rows == expected, f"T006 v2 is not an exact one-field repair: {new_path.name}")
    old_visual = T006_VISUAL_V1.read_text(encoding="utf-8")
    expected_visual = old_visual.replace(
        "reciprocal construction, starred column, and page number",
        "reciprocal construction, displayed column without star marks (with stars retained on the preceding reciprocal-module notation), and page number",
    )
    require(expected_visual != old_visual and T006_VISUAL_V2.read_text(encoding="utf-8") == expected_visual, "T006 visual successor mismatch")
    repair = jread(T006_REPAIR)
    require(repair["status"] == "PASS" and repair["source_or_target_tex_changes"] == 0, "T006 repair claim mismatch")
    require(repair["semantic_changes"] == repair["visual_qa_wording_changes"] == 1, "T006 repair counts changed")
    for label, digest in repair["historical_inputs_preserved"].items():
        require(sha(ROOT / label) == digest, f"T006 historical input hash mismatch: {label}")
    for label, digest in repair["successors"].items():
        require(sha(ROOT / label) == digest, f"T006 successor hash mismatch: {label}")
    return {"status": "PASS_UNSTARRED_COLUMN_SUCCESSORS", "source_or_target_tex_changes": 0}


def expected_crosswalk(wordweb_v9: dict) -> list[dict[str, str]]:
    es_rows = read_csv(ES_LEDGER)
    fr_rows = read_csv(FR_LEDGER)
    require((len(es_rows), len(fr_rows)) == (101, 93), "production ledger topology changed")
    senses_by_term = defaultdict(list)
    for sense in wordweb_v9["senses"]:
        senses_by_term[sense["term_id"]].append(sense["sense_id"])
    german_core_map = {}
    for index, core in enumerate(wordweb_v9["core_concepts"]):
        key = norm(es_rows[index]["source_term"])
        require(key and key not in german_core_map, f"duplicate German core identity: {key}")
        german_core_map[key] = core["term_id"]
    surface_index = {"es": defaultdict(set), "fr": defaultdict(set)}
    for core in wordweb_v9["core_concepts"]:
        for form in core["forms"]:
            language = form["language"]
            if language in surface_index:
                for field in ("surface_as_inherited", "lemma_candidate"):
                    for value in alternatives(form.get(field) or ""):
                        surface_index[language][value].add(core["term_id"])

    def one(language: str, index: int, row: dict[str, str]) -> dict[str, str]:
        source_candidates: set[str] = set()
        target_candidates: set[str] = set()
        if language == "es" and index < 60:
            mapped = f"T{index + 1:02d}"
            candidates = {mapped}
            method, status = "pinned_spanish_core_row_identity", "mapped"
        else:
            for value in alternatives(row["source_term"]):
                if value in german_core_map:
                    source_candidates.add(german_core_map[value])
            for value in alternatives(row["target_term"]):
                target_candidates.update(surface_index[language].get(value, set()))
            common = source_candidates & target_candidates
            if len(common) == 1:
                candidates, mapped = common, next(iter(common))
                method, status = "exact_normalized_source_and_target_identity", "mapped"
            elif not source_candidates and len(target_candidates) == 1:
                candidates, mapped = target_candidates, next(iter(target_candidates))
                method, status = "unique_exact_normalized_target_surface", "mapped"
            elif not target_candidates and len(source_candidates) == 1:
                candidates, mapped = source_candidates, next(iter(source_candidates))
                method, status = "unique_exact_normalized_german_core_source", "mapped"
            else:
                candidates, mapped = source_candidates | target_candidates, ""
                if source_candidates and target_candidates and not common:
                    method, status = "source_target_exact_match_conflict_no_mapping", "conflict_held"
                elif candidates:
                    method, status = "nonunique_exact_match_no_mapping", "ambiguous_held"
                else:
                    method, status = "no_exact_identity_no_inference", "unmapped_explicit"
        candidate_senses = sorted(sense for term in candidates for sense in senses_by_term[term])
        mapped_senses = sorted(senses_by_term[mapped]) if mapped else []
        precision = "term_and_single_sense_exact" if mapped and len(mapped_senses) == 1 else "term_exact_sense_disambiguation_open" if mapped else "no_mapping"
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
            "production_row_sha256": text_sha(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":"))),
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

    rows = [one("es", i, row) for i, row in enumerate(es_rows)]
    rows.extend(one("fr", i, row) for i, row in enumerate(fr_rows))
    return rows


def validate_crosswalk(wordweb_v9: dict) -> dict:
    expected = expected_crosswalk(wordweb_v9)
    actual = read_csv(CROSSWALK_CSV)
    require(actual == expected and len(actual) == 194, "production crosswalk differs from independent reconstruction")
    require([row["wordweb_term_id"] for row in actual[:60]] == [f"T{i:02d}" for i in range(1, 61)], "Spanish T01-T60 identity drift")
    counts = {
        language: dict(Counter(row["mapping_status"] for row in actual if row["language"] == language))
        for language in ("es", "fr")
    }
    require(counts == {"es": {"mapped": 61, "unmapped_explicit": 40}, "fr": {"unmapped_explicit": 84, "mapped": 9}}, "crosswalk mapping counts changed")
    require(all(row["attestation_effect"].startswith("none") and row["promotion_effect"] == "none" and row["human_or_MII_effect"] == "none" for row in actual), "crosswalk claim leak")
    data = jread(CROSSWALK_JSON)
    require(data["rows"] == actual and data["mapping_status_counts"] == counts, "crosswalk JSON mismatch")
    require(data["row_count"] == 194 and data["language_rows"] == {"es": 101, "fr": 93}, "crosswalk counts mismatch")
    method = CROSSWALK_MD.read_text(encoding="utf-8")
    for required in ("194", "101-row Spanish", "93-row French", "no attestation", "no semantic nearest-neighbor"):
        require(required.lower() in method.lower(), f"crosswalk method note missing: {required}")
    return {"rows": 194, "language_rows": {"es": 101, "fr": 93}, "mapping_status_counts": counts}


def restore_keys(new: dict, old: dict, keys: tuple[str, ...]) -> dict:
    clone = copy.deepcopy(new)
    for key in keys:
        if key in old:
            clone[key] = copy.deepcopy(old[key])
        else:
            clone.pop(key, None)
    return clone


def validate_successors(wordweb_v9: dict, links: dict, crosswalk: dict) -> dict:
    wordweb = jread(WORDWEB_V10)
    restored = restore_keys(
        wordweb, wordweb_v9,
        ("artifact", "supersedes_for_semantic_use", "v9_retained_as", "production_alignment_v10", "input_hashes_v10"),
    )
    require(restored == wordweb_v9, "WordWeb v10 changed predecessor semantic/evidence/form payload")
    require(wordweb["artifact"] == "PAN_ROMANCE_WORDWEB_v10", "wrong WordWeb v10 artifact")
    alignment = wordweb["production_alignment_v10"]
    require(alignment["effective_link_rows"] == 104 and alignment["corrected_link_rows"] == 6, "WordWeb alignment counts mismatch")
    require(alignment["semantic_link_contract_sha256"] == links["contract_sha256"], "WordWeb link contract mismatch")
    require(alignment["effective_links_csv_sha256"] == sha(LINKS_CSV) and alignment["crosswalk_csv_sha256"] == sha(CROSSWALK_CSV), "WordWeb alignment hashes mismatch")
    require(alignment["crosswalk_mapping_status_counts"] == crosswalk["mapping_status_counts"], "WordWeb crosswalk count mismatch")
    require(alignment["attestation_effect"] == "none" and alignment["core_form_promotions"] == alignment["human_observations"] == 0, "WordWeb v10 claim leak")

    access_v9 = jread(ACCESS_V9_JSON)
    access = jread(ACCESS_V10_JSON)
    restored_access = restore_keys(
        access, access_v9,
        ("artifact", "supersedes", "method", "status", "input_hashes_v10", "production_alignment_v10", "claim_boundary"),
    )
    for old_row, row in zip(access_v9["rows"], restored_access["rows"], strict=True):
        row["method_version"] = old_row["method_version"]
    require(restored_access == access_v9, "access v10 changed predecessor diagnostics/human payload")
    access_csv = read_csv(ACCESS_V10_CSV)
    require(len(access["rows"]) == len(access_csv) == 954, "access v10 row topology changed")
    for json_row, csv_row in zip(access["rows"], access_csv, strict=True):
        require({key: csv_scalar(value) for key, value in json_row.items()} == csv_row, "access v10 JSON/CSV mismatch")
        require(json_row["method_version"] == "MII_METHOD_v10", "access row method drift")
        require(all(json_row[field] is None for field in HUMAN_FIELDS) and json_row["pilot_eligible"] is False, "access human/pilot claim leak")
    require(access["human_observation_count"] == access["pilot_eligible_count"] == access["form_promotion_count"] == 0, "access aggregate claim leak")
    method = MII_V10.read_text(encoding="utf-8")
    for required in ("zero human observations", "954", "do not measure intelligibility", "33 senses", "53 zero-body routes", "no empirical-MII"):
        require(required.lower() in method.lower(), f"MII v10 missing boundary: {required}")
    return {
        "wordweb_sha256": sha(WORDWEB_V10),
        "access_json_sha256": sha(ACCESS_V10_JSON),
        "access_csv_sha256": sha(ACCESS_V10_CSV),
    }


def validate_audit(links: dict, crosswalk: dict, successors: dict) -> None:
    audit = jread(ALIGNMENT_AUDIT)
    require(audit["artifact"] == "ROMANCE_SEMANTIC_ALIGNMENT_v10" and audit["status"] == "PASS", "alignment audit not PASS")
    require(audit["controlled_terminology"]["semantic_link_contract_sha256"] == links["contract_sha256"], "audit link hash mismatch")
    require(audit["production_crosswalk"]["mapping_status_counts"] == crosswalk["mapping_status_counts"], "audit crosswalk mismatch")
    require(audit["wordweb_v10"]["sha256"] == successors["wordweb_sha256"], "audit WordWeb hash mismatch")
    require(audit["access_v10"]["json_sha256"] == successors["access_json_sha256"], "audit access hash mismatch")
    require(audit["wordweb_v10"]["supported_senses"] == 73 and audit["wordweb_v10"]["unsupported_senses"] == 33, "audit support boundary changed")
    require(audit["production_crosswalk"]["attestation_effect_rows_non_none"] == audit["production_crosswalk"]["promotion_effect_rows_non_none"] == 0, "audit claim leak")


def validate_docs() -> None:
    for text, label in ((README.read_text(encoding="utf-8"), "README"), (CURSOR.read_text(encoding="utf-8"), "cursor")):
        for required in ("v10", "104", "six", "194", "73/106", "954", "zero human", "T006", "21256", "ACTIVE_NOT_COMPLETE"):
            require(required.lower() in text.lower(), f"{label} missing v10 closure fact: {required}")
        require("empirical mii" in text.lower() and ("zero" in text.lower() or "0" in text), f"{label} blurs empirical MII boundary")


def build_manifest() -> list[dict[str, str | int]]:
    targets = {row["relative_path"]: (ROOT / row["relative_path"]).resolve() for row in read_csv(MANIFEST_V9)}
    targets.update({
        "README.md": README,
        "CONTINUATION_CURSOR.md": CURSOR,
        "qa/ROMANCE_ACCEPTANCE_GATE_v9.json": GATE_V9,
        "qa/SHA256SUMS_v9.csv": MANIFEST_V9,
        "scripts/build_semantic_alignment_v10.py": BUILDER,
        "scripts/validate_romance_tranche_v10.py": Path(__file__).resolve(),
        "curation/CONTROLLED_ROMANCE_TERMINOLOGY_WORDWEB_LINKS_v10.csv": LINKS_CSV,
        "curation/CONTROLLED_ROMANCE_TERMINOLOGY_WORDWEB_LINKS_v10.json": LINKS_JSON,
        "curation/NOETHER_ES_FR_WORDWEB_CROSSWALK_v10.csv": CROSSWALK_CSV,
        "curation/NOETHER_ES_FR_WORDWEB_CROSSWALK_v10.json": CROSSWALK_JSON,
        "curation/NOETHER_ES_FR_WORDWEB_CROSSWALK_v10.md": CROSSWALK_MD,
        "wordweb/PAN_ROMANCE_WORDWEB_v10.json": WORDWEB_V10,
        "access/PAN_ROMANCE_ACCESS_LEDGER_v10.json": ACCESS_V10_JSON,
        "access/PAN_ROMANCE_ACCESS_LEDGER_v10.csv": ACCESS_V10_CSV,
        "access/MII_METHOD_v10.md": MII_V10,
        "R823_HG_T006/semantic/R823_HG_T006_clause_map_seed_v2.csv": T006_SEED_V2,
        "R823_HG_T006/semantic/R823_HG_T006_clause_map_v2.csv": T006_MAP_V2,
        "R823_HG_T006/qa/R823_HG_T006_VISUAL_QA_v2.md": T006_VISUAL_V2,
        "R823_HG_T006/qa/R823_HG_T006_SEMANTIC_METADATA_REPAIR_v2.json": T006_REPAIR,
        "qa/ROMANCE_SEMANTIC_ALIGNMENT_v10.json": ALIGNMENT_AUDIT,
        "qa/ROMANCE_SEMANTIC_ALIGNMENT_BUILD_v10.log": BUILD_LOG,
    })
    rows = []
    for label, path in targets.items():
        require(path.exists(), f"manifest target missing: {label}")
        rows.append({"relative_path": label, "bytes": path.stat().st_size, "sha256": sha(path)})
    require(len(rows) == len({row["relative_path"] for row in rows}), "v10 manifest labels not unique")
    write_csv(MANIFEST_V10, rows)
    return rows


def validate_v10_manifest() -> tuple[int, list[str]]:
    rows = read_csv(MANIFEST_V10)
    mismatches = []
    for row in rows:
        path = (ROOT / row["relative_path"]).resolve()
        if not path.exists() or path.stat().st_size != int(row["bytes"]) or sha(path) != row["sha256"]:
            mismatches.append(row["relative_path"])
    return len(rows), mismatches


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core-only", action="store_true", help="validate v10 before advancing mutable documentation")
    args = parser.parse_args()

    predecessor_rows, predecessor_mismatches = verify_v9_predecessor(args.core_only)
    v9_core = v9.validate_core(False)
    wordweb_v9 = jread(WORDWEB_V9)
    links = validate_links(wordweb_v9)
    t006 = validate_t006()
    crosswalk = validate_crosswalk(wordweb_v9)
    successors = validate_successors(wordweb_v9, links, crosswalk)
    validate_audit(links, crosswalk, successors)
    if args.core_only:
        print("PASS ROMANCE_V10_CORE_GATE")
        print("effective_links=104 corrections=6 crosswalk=194 attestations_added=0 promotions=0")
        print("wordweb=60/106 evidence=802 support=73/106 access=954 human=0 empirical_MII=0")
        print("stage_D=T001_T006_PASS next_authority_line=21256")
        return

    validate_docs()
    manifest_rows = build_manifest()
    manifest_count, manifest_mismatches = validate_v10_manifest()
    require(not manifest_mismatches and manifest_count == len(manifest_rows), f"v10 manifest mismatch: {manifest_mismatches}")
    gate = {
        "artifact": "ROMANCE_ACCEPTANCE_GATE_v10",
        "machine_validation": "PASS",
        "romance_infrastructure_status": "PASS_MAINTAINED_EMPIRICAL_RESEARCH_INCOMPLETE",
        "goal_status": "ACTIVE_NOT_COMPLETE",
        "predecessor_v9": {
            "status": "PRESERVED_IMMUTABLE_VERSIONED_PREDECESSOR",
            "wordweb_sha256": sha(WORDWEB_V9),
            "access_json_sha256": sha(ACCESS_V9_JSON),
            "access_csv_sha256": sha(ACCESS_V9_CSV),
            "gate_sha256": sha(GATE_V9),
            "manifest_sha256": sha(MANIFEST_V9),
            "manifest_rows": predecessor_rows,
            "mutable_successor_pointer_paths": predecessor_mismatches,
        },
        "stage_A": {
            "status": "NOT_COMPLETE", "explicit_routes": 61, "active_routes": 8,
            "zero_body_routes": 53, "romansh_general_school_math_bodies": 3,
            "romansh_specialist_algebra_bodies": 0, "romansh_regional_idiom_bodies": 0,
        },
        "stage_B": {
            "status": "CURRENT_CORPUS_TRANCHE_PASS", "records": 148,
            "primary_unique": 142, "representation_aliases": 6,
            "counting_eligible": 66, "excluded": 5,
        },
        "stage_C": {
            "status": "STRUCTURAL_REVIEW_AND_PRODUCTION_ALIGNMENT_PASS_NOT_HUMAN_VALIDATED",
            "core_concepts": 60, "senses": 106, "c2_nodes": 39,
            "evidence_records": 802, "reviewed_occurrences": 682,
            "senses_with_accepted_support": 73, "senses_without_accepted_support": 33,
            "relation_records": 402, "human_observations": 0, "core_form_promotions": 0,
            "controlled_terminology_rows": links["rows"], "corrected_semantic_links": links["corrections"],
            "semantic_link_contract_sha256": links["contract_sha256"],
            "production_crosswalk_rows": crosswalk["rows"],
            "production_crosswalk_language_rows": crosswalk["language_rows"],
            "production_crosswalk_mapping_status_counts": crosswalk["mapping_status_counts"],
            "attestations_added_by_alignment": 0,
        },
        "T006_metadata": t006,
        "stage_D": v9_core["stage_d"],
        "access_and_MII": {
            "sense_count": 106, "cohort_count": 9, "rows": 954,
            "human_result_fields_nonnull": 0, "human_observations": 0,
            "pilot_eligible_rows": 0, "form_promotions": 0,
            "empirical_MII_status": "ZERO_OBSERVATIONS_NOT_IMPLEMENTED",
            "diagnostic_boundary": "Orthographic proxy values are design diagnostics and do not measure intelligibility.",
        },
        "documentation_status": "CURRENT_V10",
        "pilot_claim": False,
        "full_R823_romance_translation_claim": False,
        "hash_target_count": len(manifest_rows),
        "hash_manifest_sha256": sha(MANIFEST_V10),
        "key_hashes": {row["relative_path"]: row["sha256"] for row in manifest_rows},
    }
    GATE_V10.write_text(json.dumps(gate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "PASS machine_validation romance_infrastructure=PASS_MAINTAINED goal_status=ACTIVE_NOT_COMPLETE",
        "stage_A=NOT_COMPLETE routes=61 active=8 zero=53 rm_general_math=3 rm_specialist_algebra=0 rm_idioms=0",
        "stage_B=PASS records=148 primary_unique=142 counting_eligible=66 excluded=5",
        "stage_C=PASS_STRUCTURAL concepts=60 senses=106 c2=39 evidence=802 reviewed=682 supported_senses=73/106 human=0 promotions=0",
        "production_alignment=PASS effective_links=104 corrected=6 crosswalk=194 es=101 fr=93 attestations_added=0",
        "T006_metadata=PASS_UNSTARRED_COLUMN_SUCCESSORS source_or_target_tex_changes=0",
        "access=PASS rows=954 cohorts=9 human_observations=0 pilot_eligible=0 promotions=0 empirical_MII=ZERO_OBSERVATIONS",
        "stage_D=T001_T006_PASS outputs=6 render_pages=15/15 next=21256 human_validation=0",
        f"wordweb_v10_sha256={successors['wordweb_sha256']}",
        f"access_v10_json_sha256={successors['access_json_sha256']}",
        f"access_v10_csv_sha256={successors['access_csv_sha256']}",
        f"hash_targets={len(manifest_rows)} sha256_manifest={sha(MANIFEST_V10)}",
        f"gate_v10_sha256={sha(GATE_V10)}",
    ]
    GATE_LOG_V10.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
