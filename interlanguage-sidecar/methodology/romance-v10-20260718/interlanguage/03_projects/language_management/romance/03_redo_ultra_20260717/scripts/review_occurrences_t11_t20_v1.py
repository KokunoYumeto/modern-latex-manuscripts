from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v1.csv"
OUT = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T11_T20_v1.csv"
SUMMARY = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T11_T20_v1.json"
LOG = ROOT / "qa" / "OCCURRENCE_REVIEW_T11_T20_v1.log"
REPORTS = ROOT.parent / "_agent_reports"


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


ACCEPTED: dict[str, tuple[str, str]] = {}


def accept(sense_id: str, reason: str, occurrence_ids: str) -> None:
    for occurrence_id in occurrence_ids.split():
        assert occurrence_id not in ACCEPTED
        ACCEPTED[occurrence_id] = (sense_id, reason)


accept("T12-S1", "least_common_multiple_in_UFD_statement", "OCC-D52C7C0632C0FD24")
accept("T13-S1", "greatest_common_divisor_math_context", "OCC-9E2CC75E86A70EB9 OCC-2EAA99526AECE0C7 OCC-6B588AE33943B89B OCC-513F9CB0A847D534")
accept("T14-S1", "multiplicative_product_context", """
OCC-131584C7675B48BF OCC-0E1702D0DFA7F04E OCC-8804B2F795FFC5CC OCC-9FA2FC27D8AFB147
OCC-B4AEC435302C4B75 OCC-67DA8C04582F72F3 OCC-1AE2087FD4C69969 OCC-58B7F85C42732507
OCC-866549268EF99357 OCC-964C6351AC8E7AE0 OCC-1E7337EA09D84541 OCC-5027536F60E1521B
OCC-3C37DC0098E5DFB9
""")
accept("T14-S3", "direct_or_cartesian_product_context", "OCC-3FA6FDA62AE7A321 OCC-7BE5570564DAFDAE OCC-536B5CF1BF2844F2")
accept("T15-S1", "multiplicative_factor_context", """
OCC-52402A5D8ADE6FFE OCC-BB4ABD5CB160116B OCC-6E78B1085F34FE13 OCC-6C85DC9B04FE051D
OCC-37D3CE8C2CFF05E9 OCC-3B3359BB4DC21315 OCC-4FE18012F439124D
""")
accept("T15-S2", "quotient_or_factor_object_context", "OCC-65A723BAEE193003 OCC-065EDE76429D42E2 OCC-644086A8BC130A48 OCC-CFDDAAAD942F1CA1 OCC-53A6AD487706E58E")
accept("T16-S1", "generic_mathematical_decomposition_context", "OCC-37D911D5F3BF3601 OCC-0C684E9EDDA30134 OCC-F413CAACE1649037 OCC-D035BFEC124B070F OCC-6EE39C25B2B8CA1F OCC-74C0C4E136747126")
accept("T16-S2", "direct_sum_decomposition_context", "OCC-5E4605EAF4059DFD OCC-4B0AF4AACA1CB8BD OCC-4CE594BED74B0DF0 OCC-8DBE218A385B7A80")
accept("T16-S3", "primary_decomposition_context", "OCC-4FD456B68365596E")
accept("T17-S1", "algebraic_representation_context", "OCC-855D9412D6D27E64 OCC-F1C5EFBC5CE14A4C OCC-4F5A1C4DE08BB9C0 OCC-C3A8C52163E15CC2 OCC-FF38F968E23A33AD OCC-6C9D18FB19B3793D OCC-69D0BAF2C491C257 OCC-00AB352B7A5311F3")
accept("T18-S1", "structure_preserving_homomorphism_context", """
OCC-0186A8073BD69F7A OCC-98FD9E53A9E4943C OCC-74AD623E3CAC4ECB OCC-126EB43FE523C2AE
OCC-0EA46714BAEC564B OCC-36606C586BE519AE OCC-F4F55129362EE71D OCC-F0893D305CBB55F6
OCC-3938B1FAFD350D08 OCC-5ABEAED9F770C54C OCC-E6CE985F452E2607 OCC-B2670A8388E430FA
OCC-F002893BE948EA9A OCC-00209D16575B5CE3
""")
accept("T19-S1", "structural_isomorphism_context", """
OCC-8787AED925CBE819 OCC-E217FF34500D3425 OCC-87AFBE7B36C87957 OCC-320847F8A031BF88
OCC-5EA8B2B9B26D2855 OCC-47BFDBF93BB7FCB1 OCC-AC96C2D81A417845 OCC-46032EF8074CE367
OCC-99A4BAD440782F01 OCC-E677297B9BAA3C38 OCC-EFC4AC63E3F2C411 OCC-CD5F6505DECDEF84
OCC-BC9C9D8513FB1722 OCC-F7A461FA2324B727 OCC-5581743365D1DC13 OCC-81EC860D331346B3
OCC-DC2BAE019EE5C968
""")
accept("T20-S1", "algebraic_structure_automorphism_context", "OCC-958D9B2A333E926B OCC-B3C9F669A34EBA1B OCC-21CA003B7FF8042B OCC-BBD5DAA638D0A0DC OCC-8C2B54D00C9E7DDE OCC-1BBBAF23EDE00F6F OCC-537655620D8C357B")

REJECTED: dict[str, tuple[str, str, str]] = {
    "OCC-3A624F791BE8AE0E": ("", "tensor_product_unmodeled", "The occurrence is the distinct compound tensor product, not any modeled T14 sense."),
    "OCC-575DEDACE17E4844": ("T14-S1", "ordinary_causal_result", "Product describes a historical causal result, not multiplication."),
    "OCC-A59BA5D3C0F196B5": ("T14-S1", "ordinary_causal_result", "Product describes a result of human thought, not multiplication."),
    "OCC-152D76C3FA7BE9F4": ("", "direct_factor_unmodeled_navigation", "Direct factor is a navigation label for an unmodeled module sense."),
    "OCC-FD919D2A654E8276": ("", "wrong_language_code_label", "English theorem-environment text inside a French source is not French lexical evidence."),
    "OCC-F4D3BF6D23492F3A": ("", "wrong_language_bibliography", "English bibliography title inside a French body is not French lexical evidence."),
    "OCC-BE1E7350CD214AB5": ("", "wrong_language_english_abstract", "English abstract inside a French source is not French lexical evidence."),
    "OCC-47D17A78D3D65925": ("", "coordinate_representation_wrong_sense", "A coordinate matrix representing a linear map is outside T17-S1 through T17-S3 as currently defined."),
    "OCC-8FC255BA87A54893": ("T18-S1", "explicit_nonexample_crossed_homomorphism", "The source explicitly says the cocycle is not a group homomorphism; retain as adverse evidence."),
    "OCC-A8FEE5299CCE3A40": ("T19-S1", "source_defect_hom_implies_isomorphism", "The Catalan sentence materially and falsely says any ring homomorphism makes rings isomorphic; unsafe as support."),
}

HELD: dict[str, tuple[str, str, str]] = {
    "OCC-6A20983E3E964DEB": ("", "exterior_product_compound_needs_sense", "Mathematical exterior-product compound requires a separate sense or compound edge before assignment."),
    "OCC-F5CFB29B5618B836": ("T16-S3", "navigation_label_only", "Exact primary-decomposition label, but no local proposition or definition."),
    "OCC-9D0B733A9E4C7DB9": ("T16-S3", "navigation_label_only", "Duplicate exact primary-decomposition navigation label without a local body."),
    "OCC-18B9CAECB08871DC": ("T17-S1", "toc_label_only", "Group-representation phrase occurs only as a contents label."),
    "OCC-310338F60B3D09A1": ("T17-S1", "toc_label_only", "Group-representation phrase occurs only as a contents label."),
    "OCC-A794F6C6D498085E": ("T17-S1", "toc_label_only", "Group-representation phrase occurs only as a contents label."),
    "OCC-5E917BB01D56606D": ("T19-S1", "navigation_label_only", "Isomorphism occurs only in a template list."),
    "OCC-76090F5CCE2C9E01": ("T19-S1", "vocabulary_list_only", "Romanian form occurs only in a coined-terms list without a structural proposition."),
    "OCC-EC9D87555536A150": ("", "category_autoequivalence_unmodeled", "Derived-category autoequivalence use is broader than the current T20-S1 definition."),
    "OCC-E3AD4842AA3687A3": ("T20-S1", "navigation_label_only", "Internal-automorphism phrase occurs only in a template list."),
    "OCC-D5BA86CC0588DC2F": ("T20-S1", "navigation_label_only", "Duplicate internal-automorphism navigation label without local body evidence."),
}

SPECIAL_ACCEPT_NOTES = {
    "OCC-9E2CC75E86A70EB9": "Semantically valid MCD navigation label; belongs to one repeated Italian template evidence family.",
    "OCC-2EAA99526AECE0C7": "Semantically valid MCD navigation label; belongs to one repeated Italian template evidence family.",
    "OCC-6B588AE33943B89B": "Semantically valid MCD navigation label; belongs to one repeated Italian template evidence family.",
    "OCC-513F9CB0A847D534": "Romanian running text explicitly identifies the greatest common divisor of two polynomials.",
    "OCC-4FD456B68365596E": "Spanish running text explicitly discusses ideals admitting a primary decomposition.",
    "OCC-6C9D18FB19B3793D": "Adjacent Galician lines define the ring homomorphism into an endomorphism ring and call it a representation.",
    "OCC-5ABEAED9F770C54C": "Catalan running text gives ring-homomorphism equations and unit preservation.",
    "OCC-5581743365D1DC13": "Italian section and adjacent definition identify an isomorphism as an invertible linear transformation.",
    "OCC-537655620D8C357B": "Adjacent Italian body defines an automorphism as an isomorphism with equal domain and codomain.",
}

with SOURCE.open(encoding="utf-8-sig", newline="") as handle:
    all_rows = list(csv.DictReader(handle))
source_rows = [row for row in all_rows if 11 <= int(row["term_id"][1:]) <= 20]
source_ids = {row["occurrence_id"] for row in source_rows}
classified_ids = set(ACCEPTED) | set(REJECTED) | set(HELD)
assert not (set(ACCEPTED) & set(REJECTED) or set(ACCEPTED) & set(HELD) or set(REJECTED) & set(HELD))
assert source_ids == classified_ids, {
    "unclassified": sorted(source_ids - classified_ids),
    "stale_review_ids": sorted(classified_ids - source_ids),
}
assert len(source_rows) == 111 and not any(row["term_id"] == "T11" for row in source_rows)

reviewed = []
for row in source_rows:
    occurrence_id = row["occurrence_id"]
    item = dict(row)
    if occurrence_id in ACCEPTED:
        reviewed_sense_ids, reason = ACCEPTED[occurrence_id]
        status = "accepted_sense_match"
        adverse_to = ""
        held_for = ""
        note = SPECIAL_ACCEPT_NOTES.get(occurrence_id, "Full stored quote and adjacent source lines inspected; the explicit modeled sense is matched.")
        role = "sense_matching_source_context"
    elif occurrence_id in REJECTED:
        adverse_to, reason, note = REJECTED[occurrence_id]
        status = "rejected_adverse_or_wrong_sense"
        reviewed_sense_ids = ""
        held_for = ""
        role = "adverse_false_friend_source_defect_or_provenance_boundary"
    else:
        held_for, reason, note = HELD[occurrence_id]
        status = "held_insufficient_context_or_unmodeled_sense"
        reviewed_sense_ids = ""
        adverse_to = ""
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
for row in reviewed:
    by_term[row["term_id"]][row["semantic_review_status"]] += 1

report_hashes = {
    "review_t11_t15": file_sha(REPORTS / "review_t11_t15.md"),
    "review_t16_t20": file_sha(REPORTS / "review_t16_t20.md"),
}
assert report_hashes == {
    "review_t11_t15": "602585111095436CBF8A9CF693E511456247C11931EF9B6665D531BF905BE3F2",
    "review_t16_t20": "05EAEA25207A6A785C6B4451CD7478317C25D2ED7879EF3A31B2C22D721E3F56",
}

summary = {
    "artifact": "ROMANCE_OCCURRENCE_REVIEW_T11_T20_v1",
    "source_occurrence_manifest_sha256": file_sha(SOURCE),
    "independent_review_report_hashes": report_hashes,
    "reviewed_terms": [f"T{i:02d}" for i in range(11, 21)],
    "explicit_zero_hit_terms": ["T11"],
    "reviewed_rows": len(reviewed),
    "accepted_sense_matches": sum(row["semantic_review_status"] == "accepted_sense_match" for row in reviewed),
    "rejected_adverse_or_wrong_sense": sum(row["semantic_review_status"] == "rejected_adverse_or_wrong_sense" for row in reviewed),
    "held_rows": sum(row["semantic_review_status"] == "held_insufficient_context_or_unmodeled_sense" for row in reviewed),
    "bridge_form_promotions": 0,
    "human_observations": 0,
    "by_term": {term: dict(counts) for term, counts in sorted(by_term.items())},
    "review_manifest_sha256": file_sha(OUT),
    "boundary": "Internal semantic context review only. Accepted rows do not promote forms or become inherited-core quotations; held rows are neither support nor adverse evidence.",
}
SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

assert summary["accepted_sense_matches"] == 90
assert summary["rejected_adverse_or_wrong_sense"] == 10
assert summary["held_rows"] == 11
assert summary["bridge_form_promotions"] == summary["human_observations"] == 0
assert Counter(row["term_id"] for row in reviewed) == Counter({"T12": 1, "T13": 4, "T14": 20, "T15": 13, "T16": 14, "T17": 14, "T18": 15, "T19": 20, "T20": 10})

lines = [
    "PASS reviewed_rows=111 explicit_zero_hit_T11=true",
    "accepted_sense_matches=90",
    "rejected_adverse_or_wrong_sense=10",
    "held_rows=11",
    "bridge_form_promotions=0 human_observations=0",
    f"review_manifest_sha256={summary['review_manifest_sha256']}",
]
LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
