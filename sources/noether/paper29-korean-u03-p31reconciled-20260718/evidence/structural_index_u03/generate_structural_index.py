#!/usr/bin/env python3
"""Generate the hierarchy-preserving P29-KO-U03 structural authority and CSV projection."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / "source" / "Noether_Paper29_German_P31_U03_FinitenessCriterionProofSetup_exact_lf.tex"
TARGET = ROOT / "ko" / "Noether_Paper29_Korean_U03_v001.tex"
SEALED = Path(
    "evidence://local-workspace/Codex/2026-06-01/we-are-currently-doing-a-massive/"
    "Noether_LocalCodex_20260718_P31_FullPaperCanonicalReaudit_WEB_DROP/1/01_current/"
    "cum_de_Local_20260718_P31.tex"
)
SEALED_SHA = "A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F"
UNIT_SHA = "1CD2F142F472BE2A590EC8AACA45CEB49966A09FE803CC410D138B3F7BDE7458"
DECISION = "CJK-KO-P29-010"


def digest_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest().upper()


def digest_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


source_text = SOURCE.read_text(encoding="utf-8")
target_text = TARGET.read_text(encoding="utf-8")


def record(
    structural_id: str,
    structure_type: str,
    parent_id: str | None,
    order: int,
    source_locator: str,
    target_locator: str,
    source_fragment: str,
    target_fragment: str,
    *,
    relations: list[dict[str, str]] | None = None,
    review_state: str = "internally_fidelity_checked",
    notes: str = "",
    source_occurrences: int = 1,
    target_occurrences: int = 1,
) -> dict:
    actual_source_occurrences = source_text.count(source_fragment)
    actual_target_occurrences = target_text.count(target_fragment)
    if actual_source_occurrences != source_occurrences:
        raise ValueError(
            f"{structural_id}: source fragment count {actual_source_occurrences} != {source_occurrences}"
        )
    if actual_target_occurrences != target_occurrences:
        raise ValueError(
            f"{structural_id}: target fragment count {actual_target_occurrences} != {target_occurrences}"
        )
    return {
        "schema_version": "1.0.0",
        "structural_id": structural_id,
        "work_id": "noether.paper29.ko",
        "unit_id": "P29-KO-U03",
        "structure_type": structure_type,
        "parent_id": parent_id,
        "order": order,
        "source_language": "de",
        "target_language": "ko-KR",
        "authority": {
            "sealed_path": str(SEALED),
            "sealed_sha256": SEALED_SHA,
            "unit_path": SOURCE.relative_to(ROOT).as_posix(),
            "unit_sha256": UNIT_SHA,
        },
        "source_locator": source_locator,
        "target_locator": target_locator,
        "source_fragment_sha256": digest_text(source_fragment),
        "target_fragment_sha256": digest_text(target_fragment),
        "relations": relations or [],
        "completion_state": "translated",
        "review_state": review_state,
        "publication_state": "internal_checkpoint_not_published",
        "decision_ids": [DECISION],
        "continuation_cursor": "Full-P29 line 46 is blank; next substantive cursor line 47.",
        "notes": notes,
    }


source_paragraphs = source_text.strip().split("\n\n")
target_body = target_text.split("\\begin{document}\n", 1)[1].split("\n\\end{document}", 1)[0].strip()
target_paragraphs = target_body.split("\n\n")

records = [
    record(
        "NOE-P29-KO-U03-ROOT-001", "work_unit", None, 1,
        "full-P29 lines 41-45", "target TeX lines 12-16",
        source_text, target_body,
        relations=[{"relation_type": "continues", "target_id": "NOE-P29-KO-U02-COR-001"}],
        notes="Bounded proof-stage unit; proof continues at line 47 and is not complete."
    ),
    record(
        "NOE-P29-KO-U03-ITEM-001", "item", "NOE-P29-KO-U03-ROOT-001", 2,
        "full-P29 line 41 heading", "target TeX line 12 heading",
        r"2. \srcspaced{Beweis des Endlichkeitskriteriums.}",
        r"2. \textbf{유한성 판정기준의 증명.}",
        relations=[{"relation_type": "opens", "target_id": "NOE-P29-KO-U03-PROOF-001"}],
        notes="Numbered item 2 heading."
    ),
    record(
        "NOE-P29-KO-U03-PROOF-001", "proof", "NOE-P29-KO-U03-ROOT-001", 3,
        "full-P29 lines 41-45", "target TeX lines 12-16",
        source_text, target_body,
        relations=[{"relation_type": "contains", "target_id": "NOE-P29-KO-U03-PARA-001"}],
        notes="Incomplete proof segment; no claim of proof completion."
    ),
    record(
        "NOE-P29-KO-U03-PARA-001", "paragraph", "NOE-P29-KO-U03-PROOF-001", 4,
        "full-P29 line 41", "target TeX line 12",
        source_paragraphs[0], target_paragraphs[0],
        relations=[{"relation_type": "contains", "target_id": "NOE-P29-KO-U03-STEP-001"}],
        notes="Necessity paragraph."
    ),
    record(
        "NOE-P29-KO-U03-STEP-001", "closed_prose_unit", "NOE-P29-KO-U03-PARA-001", 5,
        "full-P29 line 41 after heading", "target TeX line 12 after heading",
        r"Die Bedingung ist offenbar notwendig; denn wenn $\mathfrak S$ endlicher Integritätsbereich ist, so läßt sich $\mathfrak S$ selbst als der im Kriterium auftretende endliche Unterring $\mathfrak R$ auffassen.",
        r"이 조건이 필요함은 명백하다. 실제로 $\mathfrak S$가 유한 생성 정역이면, $\mathfrak S$ 자체를 판정기준에 나타나는 유한 생성 부분환 $\mathfrak R$로 잡을 수 있다.",
        relations=[{"relation_type": "source_one_sentence_to_target_two_sentences", "target_id": "NOE-P29-KO-U03-STEP-001"}],
        notes="Ring-theoretic endlich means finite generation, not finite cardinality."
    ),
    record(
        "NOE-P29-KO-U03-PARA-002", "paragraph", "NOE-P29-KO-U03-PROOF-001", 6,
        "full-P29 line 43", "target TeX line 14",
        source_paragraphs[1], target_paragraphs[1],
        relations=[
            {"relation_type": "contains", "target_id": "NOE-P29-KO-U03-NOTE-001"},
            {"relation_type": "contains", "target_id": "NOE-P29-KO-U03-STEP-002"}
        ],
        notes="Sufficiency hypothesis and module-finiteness goal."
    ),
    record(
        "NOE-P29-KO-U03-NOTE-001", "note", "NOE-P29-KO-U03-PARA-002", 7,
        "full-P29 line 43 first footnote call", "target TeX line 14 footnote 1",
        r"\footnote{Siehe S. 28, Fußnote 2.}",
        r"\footnote{원논문 28쪽 각주 2 참조.}",
        relations=[{"relation_type": "duplicate_text_with", "target_id": "NOE-P29-KO-U03-NOTE-002"}],
        review_state="held_source_discrepancy",
        notes="Sealed TeX has two calls; printed p.31 shares marker/body. Target follows sealed TeX.",
        source_occurrences=2, target_occurrences=2
    ),
    record(
        "NOE-P29-KO-U03-STEP-002", "closed_prose_unit", "NOE-P29-KO-U03-PARA-002", 8,
        "full-P29 line 43 final sentence", "target TeX line 14 final sentence",
        r"Zum Nachweis ist zu zeigen, daß $\mathfrak S$ eine \srcspaced{endliche} Modulbasis inbezug auf einen Unterring von $\mathfrak R$ besitzt.",
        r"이를 증명하려면 $\mathfrak S$가 $\mathfrak R$의 어떤 부분환에 관한 \textbf{유한 가군 생성계(Modulbasis)}를 가짐을 보이면 된다.",
        notes="Modulbasis is treated as a finite generating system, not an independent/free basis."
    ),
    record(
        "NOE-P29-KO-U03-PARA-003", "paragraph", "NOE-P29-KO-U03-PROOF-001", 9,
        "full-P29 line 45", "target TeX line 16",
        source_paragraphs[2], target_paragraphs[2],
        relations=[
            {"relation_type": "contains", "target_id": "NOE-P29-KO-U03-NOTE-002"},
            {"relation_type": "contains", "target_id": "NOE-P29-KO-U03-EQ-001"},
            {"relation_type": "contains", "target_id": "NOE-P29-KO-U03-STEP-007"}
        ],
        notes="Quotient-field passage, integral closure obstruction, and reduction to T."
    ),
    record(
        "NOE-P29-KO-U03-NOTE-002", "note", "NOE-P29-KO-U03-PARA-003", 10,
        "full-P29 line 45 second footnote call", "target TeX line 16 footnote 2",
        r"\footnote{Siehe S. 28, Fußnote 2.}",
        r"\footnote{원논문 28쪽 각주 2 참조.}",
        relations=[{"relation_type": "duplicate_text_with", "target_id": "NOE-P29-KO-U03-NOTE-001"}],
        review_state="held_source_discrepancy",
        notes="Second canonical call retained; both source and target fragment counts are two."
        , source_occurrences=2, target_occurrences=2
    ),
    record(
        "NOE-P29-KO-U03-STEP-003", "closed_prose_unit", "NOE-P29-KO-U03-PARA-003", 11,
        "full-P29 line 45 sentences 1-2", "target TeX line 16 sentences 1-2",
        r"Es bedeute $\mathfrak K$ den Quotientenkörper\footnote{Siehe S. 28, Fußnote 2.} von $\mathfrak R$ und $\mathfrak L$ den Quotientenkörper von $\mathfrak S$. Diese Quotientenkörper existieren, da es sich um Ringe ohne Nullteiler handelt; und es wird $P<\mathfrak K<\mathfrak L<P(x_1,\ldots,x_n)$.",
        r"$\mathfrak K$는 $\mathfrak R$의 분수체\footnote{원논문 28쪽 각주 2 참조.}를, $\mathfrak L$은 $\mathfrak S$의 분수체를 뜻한다고 하자. $\mathfrak R$과 $\mathfrak S$는 영인자가 없는 환이므로 이 두 분수체가 존재하며, $P<\mathfrak K<\mathfrak L<P(x_1,\ldots,x_n)$이다.",
        relations=[{"relation_type": "contains_inline_equation", "target_id": "NOE-P29-KO-U03-EQ-001"}],
        notes="Antecedent is made explicit in Korean without changing the source logic."
    ),
    record(
        "NOE-P29-KO-U03-EQ-001", "equation", "NOE-P29-KO-U03-STEP-003", 12,
        "full-P29 line 45 inline containment chain", "target TeX line 16 inline containment chain",
        r"$P<\mathfrak K<\mathfrak L<P(x_1,\ldots,x_n)$",
        r"$P<\mathfrak K<\mathfrak L<P(x_1,\ldots,x_n)$",
        notes="Less-than glyph denotes field containment in the established Paper 29 notation."
    ),
    record(
        "NOE-P29-KO-U03-STEP-004", "closed_prose_unit", "NOE-P29-KO-U03-PARA-003", 13,
        "full-P29 line 45 sentence 3 first clause", "target TeX line 16 sentence 3",
        r"Also wird $\mathfrak L$ nach der Folgerung unter 1. \srcspaced{endlicher algebraischer Erweiterungskörper} von $\mathfrak K$",
        r"따라서 1의 따름정리에 의해 $\mathfrak L$은 $\mathfrak K$의 \textbf{유한 대수적 확대체}다",
        notes="Field-theoretic endlich means finite extension degree."
    ),
    record(
        "NOE-P29-KO-U03-STEP-005", "closed_prose_unit", "NOE-P29-KO-U03-PARA-003", 14,
        "full-P29 line 45 sentence 3 second clause", "target TeX line 16 sentence 4",
        r"es ist weiter nach Voraussetzung jedes Element aus $\mathfrak S$ ganz inbezug auf $\mathfrak R$, und es wird somit $\mathfrak S$ Unterring des aus allen $\mathfrak R$-ganzen Elementen aus $\mathfrak L$ bestehenden Ringes $\mathfrak S'$",
        r"또한 가정에 의해 $\mathfrak S$의 모든 원소는 $\mathfrak R$에 대해 정수적이므로, $\mathfrak S$는 $\mathfrak L$에서 $\mathfrak R$에 대해 정수적인 모든 원소로 이루어진 환 $\mathfrak S'$의 부분환이다",
        notes="Integrality is over R; S prime is described rather than silently renamed integral closure."
    ),
    record(
        "NOE-P29-KO-U03-STEP-006", "closed_prose_unit", "NOE-P29-KO-U03-PARA-003", 15,
        "full-P29 line 45 penultimate sentence", "target TeX line 16 penultimate sentence",
        r"Da aber nichts über die ganze Abgeschlossenheit von $\mathfrak R$ in $\mathfrak K$ vorausgesetzt ist, kann die Tatsache, daß bei endlicher Erweiterung der Teilerkettensatz erhalten bleibt, nicht direkt herangezogen werden.",
        r"그러나 $\mathfrak R$이 $\mathfrak K$ 안에서 정수적으로 닫혀 있다고 가정하지 않았으므로, 유한 확대에서 약수사슬정리(Teilerkettensatz)가 보존된다는 사실을 직접 적용할 수는 없다.",
        notes="Integral closedness is not algebraic closure; historical theorem label is retained."
    ),
    record(
        "NOE-P29-KO-U03-STEP-007", "closed_prose_unit", "NOE-P29-KO-U03-PARA-003", 16,
        "full-P29 line 45 final sentence", "target TeX line 16 final sentence",
        r"Es muß vielmehr erst zu einem gleichfalls endlichen Unterring $\mathfrak T$ von $\mathfrak R$ übergegangen werden, für den diese ganze Abgeschlossenheit erfüllt ist.",
        r"그 대신 먼저, 역시 유한 생성인 $\mathfrak R$의 부분환 $\mathfrak T$로 넘어가야 하며, 이 $\mathfrak T$는 그러한 정수적 닫힘 조건을 만족해야 한다.",
        relations=[{"relation_type": "continues_to_full_p29_line", "target_id": "47"}],
        notes="The construction of T begins in the next unit."
    ),
]

jsonl = HERE / "STRUCTURAL_INDEX.jsonl"
csv_path = HERE / "STRUCTURAL_INDEX.csv"
metadata_path = HERE / "STRUCTURAL_INDEX_METADATA.json"
jsonl.write_text(
    "".join(json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n" for item in records),
    encoding="utf-8",
    newline="\n",
)

csv_fields = [
    "structural_id", "structure_type", "parent_id", "order", "source_locator", "target_locator",
    "source_fragment_sha256", "target_fragment_sha256", "completion_state", "review_state",
    "publication_state", "relation_count", "continuation_cursor", "notes"
]
with csv_path.open("w", encoding="utf-8", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=csv_fields)
    writer.writeheader()
    for item in records:
        row = {key: item[key] for key in csv_fields if key not in {"relation_count"}}
        row["relation_count"] = len(item["relations"])
        writer.writerow(row)

counts = Counter(item["structure_type"] for item in records)
metadata = {
    "schema_version": "1.0.0",
    "index_id": "NOE-P29-KO-U03-STRUCTURAL-INDEX-001",
    "work_unit": "P29-KO-U03",
    "record_count": len(records),
    "counts_by_type": dict(sorted(counts.items())),
    "root_id": records[0]["structural_id"],
    "latest_id": records[-1]["structural_id"],
    "source_sha256": digest_file(SOURCE),
    "target_sha256": digest_file(TARGET),
    "jsonl_sha256": digest_file(jsonl),
    "csv_sha256": digest_file(csv_path),
    "continuation_cursor": "Full-P29 line 46 blank; next substantive line 47.",
    "review_boundary": "Internal source/fidelity indexing only; no external human validation.",
}
metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps(metadata, ensure_ascii=False))
