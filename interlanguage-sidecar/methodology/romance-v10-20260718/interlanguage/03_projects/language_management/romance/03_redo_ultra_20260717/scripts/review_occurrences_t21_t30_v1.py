from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v1.csv"
WORDWEB = ROOT / "wordweb" / "PAN_ROMANCE_WORDWEB_v6.json"
OUT = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1.csv"
SUMMARY = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1.json"
LOG = ROOT / "qa" / "OCCURRENCE_REVIEW_T21_T30_v1.log"
REPORTS = ROOT.parent / "_agent_reports"


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


ACCEPTED: dict[str, tuple[str, str]] = {}


def accept(sense_id: str, reason: str, occurrence_ids: str) -> None:
    for occurrence_id in occurrence_ids.replace(",", " ").split():
        assert occurrence_id not in ACCEPTED
        ACCEPTED[occurrence_id] = (sense_id, reason)


accept("T21-S1", "invariant_object_under_action_or_class", "OCC-EF7497F66DAD5A8E OCC-AE63A1F83183BC7C OCC-EF7D92B9CE0F9869")
accept("T21-S2", "invariant_theory_form", "OCC-344E5A4568C7A286")
accept("T22-S1", "linear_or_free_module_basis", "OCC-29043AFDCC8D2288 OCC-F1B7B80E0A9674C2 OCC-86B38FE76D068CCD OCC-EC69DDB13A370D6F OCC-BAF4B149C822FB8B OCC-9414F0167831A397")
accept("T23-S1", "matrix_rank", "OCC-0142541E093802D4")
accept("T23-S2", "free_module_rank", "OCC-13F47FD20DFD504F OCC-3697B5C4B986706F OCC-C41FA996075D5CCB OCC-BBAEC24D3E0B310B")
accept("T23-S3", "generic_module_rank", "OCC-DFC1021A4322A1C0")
accept("T24-S1", "ring_or_enveloping_algebra_center", "OCC-126BD7712C451B3A OCC-A0A0F3DB1D2C5356 OCC-6386FE7C67BC4B53")
accept("T25-S1", "ring_or_field_structure_extension", "OCC-FCBFEE325B7A3D6F OCC-C15981A19E4EA15B OCC-5FA0ACEE9D28FC78 OCC-BFAC6A7ED7F7335B OCC-4B9C35E9F26ECC7D OCC-17B08DBF84F80999 OCC-06D859CA13430936")
accept("T25-S3", "linear_extension_of_map", "OCC-9E96884D41998AFD")
accept("T26-S2", "Galois_group_of_polynomial", "OCC-3A19D2A33EDDFEF3 OCC-BD1B95E04B302A6F")
accept("T26-S3", "Galois_theory_running_prose", "OCC-DF16928988C1AAA3")
accept("T27-S1", "Noetherian_adjective_ACC_or_finite_generation", "OCC-4B05E84AABB9DFE1 OCC-2EC597EEA18CB68A OCC-BC405B967CE43829 OCC-FF0299968A9430FC OCC-8C06B9EB11A84E12 OCC-CCA5CDE6A03A9C30")
accept("T28-S1", "Artinian_module_DCC_definition", "OCC-1CF0679243E78BDE")
accept("T29-S1", "finite_cardinality_or_finite_number", "OCC-5714A4B96C145ABE OCC-7FE81D62F411A8F4 OCC-B8544C8BB4CB0EED OCC-2986372BE5EE0B74 OCC-9637D6E5501F7E26 OCC-E30D8BD2D11F1EB4 OCC-FA39E156E77401BE OCC-BDD530058D2419A5 OCC-C3EEA5E660B36D73 OCC-90FD9B572E3091E9 OCC-88863A0FAD1186C7")
accept("T29-S2", "finite_generation", "OCC-C9D392444B7909D1")
accept("T29-S3", "finite_dimension_degree_or_rank", "OCC-08538B1B5404B653 OCC-91DAFA96FC0CACB2 OCC-743C61E0B4678C40")
accept("T30-S1", "explicit_mathematical_uniqueness", "OCC-D06C1FDE05C87EB4 OCC-82F61810A32723B2 OCC-13BD95F97195A52B OCC-0D79CF1D878A89A5 OCC-BECBF15B7F1A762A OCC-E03B6AE921C7126E OCC-A14E3064491800E2 OCC-531F3B2AC4188E00 OCC-CA0F4A63003FBCB5 OCC-3AF0C968CAA177E6 OCC-6531468290B481CA OCC-5E15ECFC3C22E263")

REJECTED: dict[str, tuple[str, str, str]] = {}


def reject(adverse_senses: str, reason: str, note: str, occurrence_ids: str) -> None:
    for occurrence_id in occurrence_ids.replace(",", " ").split():
        assert occurrence_id not in REJECTED
        REJECTED[occurrence_id] = (adverse_senses, reason, note)


reject("", "invariant_basis_number_unmodeled", "Invariant-basis-number is a distinct compound/property, not either modeled invariant sense.", "OCC-CD8D29A71D8CCF87 OCC-0656FC5309458378")
reject("", "free_monoid_basis_unmodeled", "Basis of a free commutative monoid is not a linear or historical ideal basis.", "OCC-31A59543452E768B")
reject("", "base_space_compound_unmodeled", "Topological base-space compound is outside the modeled basis senses.", "OCC-7B8F73BF2BEF7D84")
reject("T22-S1", "ordinary_foundation_false_friend", "Ordinary foundation/premise wording is adverse to accepting the surface as a linear basis.", "OCC-5CFD61B9462BBABB OCC-0DDA66745C8B3089 OCC-6D923BEA1FBAA10D OCC-9785ABD072D803F5 OCC-1A47F57D2230F4E4 OCC-0069CA0483C13084 OCC-468CE1233B81ADC4 OCC-6E9A5EE2D89EE690")
reject("T22-S1", "Italian_in_base_al_adverbial", "Italian in base al means according to and is not the mathematical basis noun.", "OCC-577C8F25268C0B21")
reject("", "induction_base_case_unmodeled", "Logical induction base case is outside the modeled basis senses.", "OCC-8D109F7F1BC76B47")
reject("T22-S1", "Romanian_basic_terms_adjectival", "Romanian bază is adjectival in basic terms, not a linear basis.", "OCC-1616C5C1C91BBEE9")
reject("", "free_group_rank_unmodeled", "Free-group rank is outside the matrix/module/generic-rank senses currently modeled.", "OCC-C2161805E1BA58F2 OCC-1FE515EA705A7824 OCC-772BCF7D00AC8532 OCC-37EA3F1AEB88678D")
reject("", "cluster_rank_unmodeled", "Cluster cardinality rank is outside the current rank senses.", "OCC-6805F7E3EDF1C646")
reject("T24-S1", "institutional_center_false_friend", "Institutional center is adverse to ring-center surface matching.", "OCC-F48A770A0C3617EA")
reject("", "Lie_algebra_center_unmodeled", "Lie-algebra center is not the explicitly modeled ring-center sense.", "OCC-A77491067FA5A71E")
reject("T24-S1", "geometric_center_false_friend", "Molecular/spherical geometric center is adverse to ring-center surface matching.", "OCC-86B5899552CE69D4 OCC-126C55E4C4C5ED0A")
reject("T25-S1", "ordinary_or_theory_extension_false_friend", "Generalization/extension of a discipline, theory, or associativity is not a ring/field extension.", "OCC-704C010B1BB3EFB7 OCC-A25441B791D4C29F OCC-CB37413119DDA006 OCC-59E4EDC7A8EDEC4C")
reject("", "quiver_principal_extension_unmodeled", "Principal extension of a quiver is outside the modeled extension senses.", "OCC-83AF0FCC7D62D7C7")
reject("", "wrong_language_category_extension_blocks", "English category/Ext-block text inside a French source is wrong-language and unmodeled.", "OCC-4B4B206DAC50DDFC")
reject("", "Galois_wrong_language_or_person_name", "Code, bibliography, acknowledgment, or person-name Galois hit is not a modeled mathematical occurrence.", "OCC-A9B028BB11406F55 OCC-41841642240535EC OCC-E57E105753672989 OCC-5F051DE668516412 OCC-D3809D55C9006F7F OCC-0C577AD3948F88E4 OCC-A5E04F51D9FEFF57 OCC-DA01A6C1063FA0AB")
reject("", "Noether_person_or_eponym_not_adjective", "Person names and Noether-normalization theorem labels do not attest the Noetherian adjective.", "OCC-1E9571F2B091EDB6 OCC-73A2C8B58C088E92 OCC-46F19BC8D5EB35A1 OCC-F235C744F70E3341 OCC-4B1CA861894D4261 OCC-BBFEA57CF0C913D3 OCC-86D25DC51D575FB4 OCC-0E71052B2884F1C9")
reject("", "Artin_person_citation_or_eponym_not_adjective", "Person, author, and Artin-Wedderburn theorem hits do not attest the Artinian adjective.", "OCC-2FC9B53BC3F89C5D OCC-3AF8625664C123ED OCC-9A9155BAB78984C5 OCC-D022D4434C064634 OCC-56759CC0E75E4507 OCC-DB7A7F5D18312085 OCC-3B604EBBF448BA2B OCC-6E7017F042A1282E")
reject("T29-S1", "explicit_negated_noninstance", "The passage explicitly says the group need not be finite; preserve as adverse, not supporting-instance evidence.", "OCC-8C857A77EA75FBFE")
reject("T30-S1", "nonmathematical_or_single_or_unified_wrong_sense", "Personal wordplay, one selected object, or one combined argument is not a mathematical uniqueness claim.", "OCC-F28F17CB799CA8F0 OCC-08D27D44F9FEA019 OCC-0CF4778D8A778D34")

HELD: dict[str, tuple[str, str, str]] = {
    "OCC-A4959F10886D9D49": ("T23-S1;T23-S2", "navigation_rank_ambiguous", "Bare French rank navigation label does not distinguish matrix from family/module rank."),
    "OCC-F39703B2A1EB5324": ("T26-S3", "toc_label_only", "Galois-theory phrase occurs only as a contents label."),
    "OCC-71C72B67D4F4FA67": ("T26-S3", "toc_label_only", "Italian Galois-theory phrase occurs only in page contents."),
    "OCC-288196D154FAFF31": ("T26-S1", "template_label_only", "Galois-extension phrase is only a field-navigation label."),
    "OCC-9F80560BF6EABF06": ("T26-S1", "duplicate_template_label", "Duplicate Italian Galois-extension template label without body evidence."),
    "OCC-2AD1E8E07F29F526": ("T28-S1", "navigation_label_only", "Correct Artinian adjective appears only in a ring-class navigation list."),
    "OCC-B2058005A498EC35": ("T29-S1", "finite_geometry_navigation_label", "Finite occurs only in a finite-geometry navigation entry."),
    "OCC-2ADAA09F9919B0B8": ("T29-S1", "toc_label_only", "Finite-group theory occurs only in a contents block."),
    "OCC-120F88AE3E936109": ("T30-S1", "uniqueness_qualifier_omitted", "Decomposition is called unique without the local isomorphism/permutation equivalence qualifier."),
}

SPECIAL_ACCEPT_NOTES = {
    "OCC-6386FE7C67BC4B53": "Ring-page navigation label only; lexical evidence, not independent defining prose.",
    "OCC-5FA0ACEE9D28FC78": "Field-extension navigation label only; lexical evidence, not independent defining prose.",
    "OCC-17B08DBF84F80999": "Italian field-extension navigation family; lexical evidence, not independent defining prose.",
    "OCC-BECBF15B7F1A762A": "Uniqueness is explicitly only up to isomorphisms; the qualifier must remain attached.",
    "OCC-531F3B2AC4188E00": "Finite-field uniqueness is explicitly only up to isomorphism; the qualifier must remain attached.",
}

with SOURCE.open(encoding="utf-8-sig", newline="") as handle:
    all_rows = list(csv.DictReader(handle))
source_rows = [row for row in all_rows if 21 <= int(row["term_id"][1:]) <= 30]
source_ids = {row["occurrence_id"] for row in source_rows}
classified = set(ACCEPTED) | set(REJECTED) | set(HELD)
assert not (set(ACCEPTED) & set(REJECTED) or set(ACCEPTED) & set(HELD) or set(REJECTED) & set(HELD))
assert source_ids == classified, {
    "unclassified": sorted(source_ids - classified),
    "stale_review_ids": sorted(classified - source_ids),
}
assert len(source_rows) == 131

reviewed = []
for row in source_rows:
    occurrence_id = row["occurrence_id"]
    item = dict(row)
    if occurrence_id in ACCEPTED:
        reviewed_sense_ids, reason = ACCEPTED[occurrence_id]
        status = "accepted_sense_match"
        adverse_to = held_for = ""
        note = SPECIAL_ACCEPT_NOTES.get(occurrence_id, "Full stored quote and adjacent source lines inspected; the explicit modeled sense is matched.")
        role = "sense_matching_source_context"
    elif occurrence_id in REJECTED:
        adverse_to, reason, note = REJECTED[occurrence_id]
        status = "rejected_adverse_or_wrong_sense"
        reviewed_sense_ids = held_for = ""
        role = "adverse_false_friend_source_defect_or_provenance_boundary"
    else:
        held_for, reason, note = HELD[occurrence_id]
        status = "held_insufficient_context_or_unmodeled_sense"
        reviewed_sense_ids = adverse_to = ""
        role = "held_not_support_not_adverse"
    item.update(
        semantic_review_status=status,
        reviewed_sense_ids=reviewed_sense_ids,
        adverse_to_sense_ids=adverse_to,
        held_for_sense_ids=held_for,
        review_reason_code=reason,
        review_note=note,
        evidence_role=role,
        review_tier="codex_internal_manual_context_review_20260717",
        reviewer_model_claim="semantic_curation_not_human_validation",
        bridge_form_promotion_eligible="false",
        human_observation="false",
    )
    reviewed.append(item)

fields = list(reviewed[0])
with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(reviewed)

by_term = defaultdict(Counter)
accepted_languages_by_sense = defaultdict(set)
for row in reviewed:
    by_term[row["term_id"]][row["semantic_review_status"]] += 1
    if row["semantic_review_status"] == "accepted_sense_match":
        accepted_languages_by_sense[row["reviewed_sense_ids"]].add(row["language"])

report_hashes = {
    "review_t21_t25": file_sha(REPORTS / "review_t21_t25.md"),
    "review_t26_t30": file_sha(REPORTS / "review_t26_t30.md"),
}
assert report_hashes == {
    "review_t21_t25": "E9C7F06BC00726FEB75721430A49C350E5D11CCBCFD0CE4090BEB20AB688F250",
    "review_t26_t30": "E653E5E4767CC27B162AD4E3F932038784BC7DB5F866C4B50A51A94A4D4C653E",
}
assert file_sha(WORDWEB) == "0D4B581A2CE3F6664B1A97A44AAD023ED1FDC6C023FED5ADE42677E445751AD4"

summary = {
    "artifact": "ROMANCE_OCCURRENCE_REVIEW_T21_T30_v1",
    "source_occurrence_manifest_sha256": file_sha(SOURCE),
    "reviewed_against_wordweb_sha256": file_sha(WORDWEB),
    "independent_review_report_hashes": report_hashes,
    "reviewed_terms": [f"T{i:02d}" for i in range(21, 31)],
    "reviewed_rows": len(reviewed),
    "accepted_sense_matches": sum(row["semantic_review_status"] == "accepted_sense_match" for row in reviewed),
    "rejected_adverse_or_wrong_sense": sum(row["semantic_review_status"] == "rejected_adverse_or_wrong_sense" for row in reviewed),
    "held_rows": sum(row["semantic_review_status"] == "held_insufficient_context_or_unmodeled_sense" for row in reviewed),
    "zero_accepted_sense_gaps": ["T22-S2", "T25-S2", "T26-S1"],
    "narrow_language_coverage": {
        "T27-S1": sorted(accepted_languages_by_sense["T27-S1"]),
        "T28-S1": sorted(accepted_languages_by_sense["T28-S1"]),
    },
    "bridge_form_promotions": 0,
    "human_observations": 0,
    "by_term": {term: dict(counts) for term, counts in sorted(by_term.items())},
    "review_manifest_sha256": file_sha(OUT),
    "boundary": "Internal semantic review only. Accepted rows do not promote forms; held rows are neither support nor adverse; template families are not independent attestations.",
}
SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

assert summary["accepted_sense_matches"] == 64
assert summary["rejected_adverse_or_wrong_sense"] == 58
assert summary["held_rows"] == 9
assert summary["narrow_language_coverage"] == {"T27-S1": ["es", "fr"], "T28-S1": ["es"]}
assert summary["bridge_form_promotions"] == summary["human_observations"] == 0
assert Counter(row["term_id"] for row in reviewed) == Counter({"T21": 6, "T22": 19, "T23": 12, "T24": 7, "T25": 14, "T26": 15, "T27": 14, "T28": 10, "T29": 18, "T30": 16})

lines = [
    "PASS reviewed_rows=131 T21_T30_complete=true",
    "accepted_sense_matches=64",
    "rejected_adverse_or_wrong_sense=58",
    "held_rows=9",
    "zero_accepted_sense_gaps=T22-S2,T25-S2,T26-S1",
    "bridge_form_promotions=0 human_observations=0",
    f"review_manifest_sha256={summary['review_manifest_sha256']}",
]
LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
