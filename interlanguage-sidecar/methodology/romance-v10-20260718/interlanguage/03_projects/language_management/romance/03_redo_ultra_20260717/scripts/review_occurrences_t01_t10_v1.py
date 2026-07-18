from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "wordweb" / "ROMANCE_TERM_OCCURRENCES_v1.csv"
OUT = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T01_T10_v1.csv"
SUMMARY = ROOT / "wordweb" / "ROMANCE_OCCURRENCE_REVIEW_T01_T10_v1.json"
LOG = ROOT / "qa" / "OCCURRENCE_REVIEW_T01_T10_v1.log"


def ids(text: str):
    return set(text.split())


ACCEPT = ids(
    """
OCC-B5688AB1238DAB3B OCC-C006CE655F317F2F OCC-A636D81B5B9DE8AF OCC-B428BAE734AF90A6 OCC-FA6771105A9F0FA2
OCC-57C51AB046F7BBE5 OCC-DED186FEB6B40FB9 OCC-5AF849B829629BBE OCC-B409ECFB86750DE5 OCC-46DBCEFBF04F87E2
OCC-DB78650B1CD3CAF9 OCC-3DC13D36F50EE1D6 OCC-A725C674398D4105 OCC-41579C946F3D094A OCC-00D006FDF2D9833F
OCC-12F818F42672282D OCC-C0667E8C3CFB94B4 OCC-5E95E9611185A9EF OCC-A2965EADA4DB7ED6 OCC-2082863F4AFDB5C8
OCC-1C1E4F3A2D296E56 OCC-F5CAC32FE5773C33 OCC-3BCA9E34A20E378C OCC-BC0BD88E41821B94 OCC-AE56D5FBA7387BA8
OCC-5317A36879B0D415 OCC-0BBC2397182D6D0C OCC-792F080AA9B8AAE9 OCC-45BB23C87F054216 OCC-8722ED6982A1894A
OCC-024CCC53239D926D OCC-10D7F6E158192A17 OCC-A90C5CB4B6FA426F OCC-171B08E04B42F7BD
OCC-5A2ACAB94341BA12 OCC-C683B9222603159A OCC-0103976EB0EC81B4
OCC-9D25FAA17BDD3CB3 OCC-3A08F8542DE4091F OCC-C13C7161CC0E1602 OCC-E70E89BE3AD26CC5 OCC-31DD5DA296F37B58
OCC-DA8FB4A0D9159CE2 OCC-3ED564109B5F0F26 OCC-2F4B555C6E934283 OCC-DAAC59CBC5C7FF7E OCC-4A421C2A5FCA2941
OCC-2146BF7D9F04228D OCC-BB9B75B205CDD941 OCC-5A179125E78D4F50 OCC-1F100985BB1F11E7 OCC-4346BB8138C15101
OCC-E254395E8CBFE160 OCC-D4B5710D0941AC84 OCC-35D914C9C3A12F4D OCC-3389DEC34268F1B0 OCC-2079CCD36C7CF84D
OCC-778EDE48A64C514A OCC-28B6EDC89995A73B OCC-65E8BFDE1EF377A2 OCC-D545F7E4DAC0FEE0 OCC-030ED39B9BF410AA
OCC-817316F8989F61D0 OCC-19D0306808410BDB OCC-1946CBA0BE3DD1AD OCC-58BD12A3366A8CAC OCC-8EB6A7C251EDB0AD
OCC-9B9878ABBB169D1D OCC-6ABA84A29191E8E6 OCC-717D5896F9DE0ACD OCC-12C4CD1385935A2B OCC-2F38D6E00DE0D094
OCC-492632E849A6228F OCC-6CE44A6C9F0ED261 OCC-3EE58D5E9497937F OCC-831629F6D3AA4A37 OCC-AB172E75FA1B328E
OCC-8CE4CA0D5D399F9C OCC-B53032DFC7BB8618
OCC-C2E450D0770C0B87 OCC-E5E561CF4443FC2D OCC-24B6891F656B9490 OCC-D35C1C5D7C8224FC OCC-92C0587E3DFE560E
"""
)

REJECT_REASON = {
    "OCC-3994744337A6FEBD": "nonmathematical_homograph_or_named_community",
    "OCC-5F9CD60CA5C911E0": "ordinary_body_of_document_not_algebraic_field",
    "OCC-FA55162AF80A7EDB": "field_of_study_not_algebraic_field",
    "OCC-5BD027568D67BB57": "field_of_study_not_algebraic_field",
    "OCC-221C13607A25C964": "field_of_study_not_algebraic_field",
    "OCC-5CE717BCAEF42C9D": "field_of_study_not_algebraic_field",
    "OCC-97B02F084FF063EE": "english_bibliographic_string_not_spanish_usage",
    "OCC-DE18FC51A9B8C314": "english_keyword_not_spanish_usage",
    "OCC-7CBBA6CF0ED47FFC": "english_bibliographic_string_not_galician_usage",
    "OCC-A3EE19DE18732506": "english_bibliographic_string_not_galician_usage",
    "OCC-67AEBD9A16AA82EF": "german_bibliographic_string_not_galician_usage",
    "OCC-FF2AD6A466449F03": "english_bibliographic_string_not_romanian_usage",
    "OCC-46DBCADE9A1F91CE": "modulo_equivalence_not_algebraic_module",
    "OCC-0047B96F01FE03FD": "integers_modulo_n_not_algebraic_module",
    "OCC-836358315814E61C": "groups_modulo_isomorphism_not_algebraic_module",
    "OCC-344CC28784D4F6BE": "numbers_modulo_integer_not_algebraic_module",
    "OCC-0B1DADED3F80F0C6": "residue_classes_modulo_prime_not_algebraic_module",
    "OCC-8DA907608BE57AA7": "remainders_modulo_six_not_algebraic_module",
    "OCC-11BC8ADF4E088E73": "integers_modulo_n_not_algebraic_module",
    "OCC-09CA6D436210EA60": "residue_classes_modulo_prime_not_algebraic_module",
    "OCC-907EA50C464D9785": "ordinary_manner_modul_in_care_not_algebraic_module",
    "OCC-13009514086E731F": "monoid_ideal_not_target_ring_ideal_sense",
    "OCC-5CDFD99B0593FD5E": "monoid_prime_ideal_not_target_ring_prime_ideal_sense",
    "OCC-B2B294D757D2BD28": "monoid_primary_ideal_not_target_ring_primary_ideal_sense",
    "OCC-8255E80548CD8567": "irreducible_polynomial_not_irreducible_ideal",
    "OCC-1F97881CDCB92714": "irreducible_polynomial_not_irreducible_ideal",
    "OCC-77942D43B6FB0898": "irreducible_element_not_irreducible_ideal",
    "OCC-3910B485CA705A0E": "irreducible_polynomial_not_irreducible_ideal",
    "OCC-C72F816E7519A759": "irreducible_polynomial_not_irreducible_ideal",
    "OCC-511EFE54676B614C": "coprime_integers_not_coprime_ideals",
    "OCC-5647916A748EE419": "coprime_integers_not_coprime_ideals",
    "OCC-540659E4ABB7CE23": "coprime_integers_not_coprime_ideals",
    "OCC-B36B349ABE1018EB": "coprime_integers_not_coprime_ideals",
}

ACCEPT_REASON = {
    "T01": "algebraic_ring_sense_matches",
    "T02": "algebraic_field_sense_matches",
    "T03": "division_ring_sense_matches",
    "T04": "algebra_discipline_or_structure_sense_matches",
    "T05": "algebraic_module_sense_matches",
    "T06": "ring_ideal_sense_matches",
    "T07": "ring_prime_ideal_sense_matches",
    "T08": "ring_primary_ideal_source_gloss_matches",
}

SPECIAL_NOTE = {
    "OCC-57C51AB046F7BBE5": "Adjacent lines 230–234 list algebraic structures: anéis, campos.",
    "OCC-5AF849B829629BBE": "Adjacent lines 204–210 list grupos, anéis, corpos.",
    "OCC-DB78650B1CD3CAF9": "Adjacent lines 139–143 state módulo sobre un anel R.",
    "OCC-A2965EADA4DB7ED6": "Adjacent lines 163–169 list grupuri, inele, corpuri.",
    "OCC-2082863F4AFDB5C8": "Adjacent lines 435–441 explicitly say abstract algebra studies rings and fields.",
    "OCC-F5CAC32FE5773C33": "Adjacent lines 185–189 identify cuerpo (a veces llamado campo) among algebraic structures.",
    "OCC-5317A36879B0D415": "Adjacent lines 388–392 state a group over a field K.",
    "OCC-10D7F6E158192A17": "Adjacent lines 222–225 define a ring with multiplicative inverses as a field.",
    "OCC-A90C5CB4B6FA426F": "Adjacent lines 420–424 state peste un corp K.",
    "OCC-D545F7E4DAC0FEE0": "Reviewed as a mathematical navigation/source-gloss label between Artin–Wedderburn and Dedekind-domain entries; not running proof prose.",
    "OCC-836358315814E61C": "Adjacent lines 551–556 show modulo-isomorphism category wording, not module theory.",
    "OCC-B2B294D757D2BD28": "Source lines 1021–1024 explicitly set M to a Noetherian monoid.",
}


def file_sha(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


with SOURCE.open(encoding="utf-8-sig", newline="") as handle:
    all_rows = list(csv.DictReader(handle))
source_rows = [r for r in all_rows if 1 <= int(r["term_id"][1:]) <= 10]
source_ids = {r["occurrence_id"] for r in source_rows}
reject = set(REJECT_REASON)

assert not ACCEPT & reject
assert ACCEPT | reject == source_ids, {
    "unclassified": sorted(source_ids - ACCEPT - reject),
    "stale_review_ids": sorted((ACCEPT | reject) - source_ids),
}

reviewed = []
for row in source_rows:
    item = dict(row)
    accepted = row["occurrence_id"] in ACCEPT
    item.update(
        semantic_review_status="accepted_sense_match" if accepted else "rejected_adverse_or_wrong_sense",
        review_reason_code=ACCEPT_REASON[row["term_id"]] if accepted else REJECT_REASON[row["occurrence_id"]],
        review_note=SPECIAL_NOTE.get(row["occurrence_id"], "Full extracted context window inspected."),
        evidence_role="sense_matching_source_context" if accepted else "adverse_false_friend_or_semantic_boundary",
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
by_language = defaultdict(Counter)
for row in reviewed:
    status = row["semantic_review_status"]
    by_term[row["term_id"]][status] += 1
    by_language[row["language"]][status] += 1

summary = {
    "artifact": "ROMANCE_OCCURRENCE_REVIEW_T01_T10_v1",
    "source_occurrence_manifest_sha256": file_sha(SOURCE),
    "reviewed_terms": [f"T{i:02d}" for i in range(1, 11)],
    "reviewed_rows": len(reviewed),
    "accepted_sense_matches": sum(r["semantic_review_status"] == "accepted_sense_match" for r in reviewed),
    "rejected_adverse_or_wrong_sense": sum(r["semantic_review_status"] != "accepted_sense_match" for r in reviewed),
    "held_rows": 0,
    "bridge_form_promotions": 0,
    "human_observations": 0,
    "by_term": {key: dict(value) for key, value in sorted(by_term.items())},
    "by_language": {key: dict(value) for key, value in sorted(by_language.items())},
    "review_manifest_sha256": file_sha(OUT),
    "boundary": "Internal semantic context review only. Accepted occurrence evidence does not promote a native form or supply human intelligibility data.",
}
SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

assert len(reviewed) == 117
assert summary["accepted_sense_matches"] == 84
assert summary["rejected_adverse_or_wrong_sense"] == 33
assert summary["bridge_form_promotions"] == summary["human_observations"] == 0

lines = [
    "PASS reviewed_rows=117",
    "accepted_sense_matches=84",
    "rejected_adverse_or_wrong_sense=33",
    "bridge_form_promotions=0",
    "human_observations=0",
    f"review_manifest_sha256={summary['review_manifest_sha256']}",
]
LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
