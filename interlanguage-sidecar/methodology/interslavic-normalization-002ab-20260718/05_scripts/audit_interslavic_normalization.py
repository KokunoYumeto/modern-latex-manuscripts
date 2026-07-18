#!/usr/bin/env python3
"""Streaming, TeX-aware audit of the canonical Noether Interslavic corpus.

The audit reads one TeX file at a time and keeps only counters plus capped
before/after examples.  It deliberately excludes working/cumulative drafts and
targets only canonical ``interslavic/v001`` translation units.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from apply_fable_tranche001 import read_text, transform_tex


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = (
    ROOT
    / "03_projects"
    / "noether"
    / "02_slavic_working_corpus"
    / "translations"
)
DEFAULT_OUTPUT = (
    ROOT
    / "03_projects"
    / "language_management"
    / "slavic_interslavic"
    / "normalization_20260718"
    / "evidence"
    / "NORMALIZATION_STATUS_AUDIT.json"
)


@dataclass(frozen=True)
class Rule:
    rule_id: str
    classification: str
    description: str
    sources: tuple[str, ...]
    target_probe: tuple[str, ...]
    proposed_target: str


RULES = (
    Rule(
        "ortho_vzeti_nasal",
        "reviewed_orthography_rollout",
        "Normalize non-nasal vzet- to vzęt-.",
        ("vzet",),
        ("vzęt",),
        "vzęt-",
    ),
    Rule(
        "ortho_obci",
        "reviewed_orthography_rollout",
        "Normalize East-flavored obšč- to obć-.",
        ("obšč",),
        ("obć",),
        "obć-",
    ),
    Rule(
        "ortho_length",
        "reviewed_orthography_rollout",
        "Normalize dlugost- spelling to dolgost-.",
        ("dlugost",),
        ("dolgost",),
        "dolgost-",
    ),
    Rule(
        "ortho_general_adverb",
        "reviewed_orthography_rollout",
        "Normalize vobče/voobče to obće.",
        ("voobče", "vobče"),
        ("obće",),
        "obće",
    ),
    Rule(
        "lex_simultaneous",
        "accepted_lexical_switch_user_activated",
        "Replace East/hybrid/S variants with W+S-facing jednočasno.",
        ("odnovrěmenno", "odnovremenno", "odnovočasno", "istočasno"),
        ("jednočasno",),
        "jednočasno",
    ),
    Rule(
        "lex_simultaneous_sanctioned_doublet",
        "dictionary_sanctioned_policy_unresolved",
        "Retained jednovrěmenno-family: the community dictionary sanctions both this headword and jednočasno; root count may include adjectival inflections.",
        ("jednovrěmenno",),
        ("jednočasno",),
        "retain until an explicit two-headword corpus policy is reviewed",
    ),
    Rule(
        "lex_simultaneous_nearby_unreviewed",
        "form_or_register_review_required",
        "Nearby simultaneous forms not covered by the exact authorized switch.",
        ("jednovremenno", "istovrěmenno", "samočasno"),
        (),
        "review spelling, register, and context before changing",
    ),
    Rule(
        "lex_step",
        "accepted_lexical_switch_user_activated",
        "Replace korak-family with krok-family.",
        ("korak",),
        ("krok",),
        "krok-family",
    ),
    Rule(
        "lex_correspond",
        "accepted_but_requires_inflection_table",
        "Re-head sootvětstvovati-family to odpovědati-family.",
        ("sootvět", "sootvet", "sootvęt"),
        ("odpověd",),
        "odpovědati-family",
    ),
    Rule(
        "backlog_sastoji",
        "high_confidence_unexecuted",
        "Orthographic sastoji- to sostoji- candidate.",
        ("sastoji",),
        ("sostoji",),
        "sostoji-",
    ),
    Rule(
        "backlog_question",
        "high_confidence_but_alias_policy_needed",
        "vprašanj- to pytanj- candidate.",
        ("vprašanj",),
        ("pytanj",),
        "pytanj-",
    ),
    Rule(
        "backlog_solution_orthography",
        "high_confidence_unexecuted",
        "reseno to rěšeno orthography candidate.",
        ("reseno",),
        ("rěšeno",),
        "rěšeno",
    ),
    Rule(
        "backlog_follows",
        "high_confidence_but_context_review_needed",
        "slijedi/sledi to slěduje candidate.",
        ("slijedi", "sledi"),
        ("slěduje",),
        "slěduje",
    ),
    Rule(
        "backlog_type",
        "high_confidence_unexecuted",
        "typ spelling to tip in prose.",
        ("typ",),
        ("tip",),
        "tip",
    ),
    Rule(
        "backlog_case_orthography",
        "held_wording_orthography_only",
        "slućaj spelling to held corpus-primary slučaj.",
        ("slućaj",),
        ("slučaj",),
        "slučaj",
    ),
    Rule(
        "backlog_entirely",
        "high_confidence_alias_policy_needed",
        "sasvim to sovsěm candidate; sanctioned alternatives remain.",
        ("sasvim",),
        ("sovsěm", "vpolně", "popolno"),
        "sovsěm (aliases documented)",
    ),
    Rule(
        "backlog_connective_imenno",
        "high_confidence_form_but_intelligibility_warning",
        "namreč/naime/totiž to imenno proposal with mandatory W/S glosses.",
        ("namreč", "naime", "totiž"),
        ("imenno",),
        "imenno plus W/S register documentation",
    ),
    Rule(
        "held_series_order",
        "held_human_review",
        "Current ręd-family density; no automatic replacement authorized.",
        ("ręd",),
        (),
        "held: retain and add context glosses until reviewed",
    ),
    Rule(
        "held_however",
        "held_homograph_review",
        "Current jednako density; Croatian/Serbian equal(ly) homograph risk.",
        ("jednako",),
        (),
        "held: contextual review",
    ),
    Rule(
        "held_valid",
        "held_register_extension_review",
        "Current važi-/važe- density; dictionary sense-extension unresolved.",
        ("važi", "važe"),
        (),
        "held: contextual review",
    ),
    Rule(
        "held_case_wording",
        "held_wording_review",
        "Current slučaj-family density; spelling may normalize but wording stays held.",
        ("slučaj",),
        (),
        "held: no lexical replacement",
    ),
    Rule(
        "held_ring_family",
        "held_terminology_family",
        "Current kolc-family density; competitor surfaces remain evidence, not replacements.",
        ("kolc",),
        (),
        "held: kolco remains corpus-primary",
    ),
    Rule(
        "held_ring_competitors",
        "held_competitor_evidence",
        "Observed prsten/pŕstėnj/koljce competitors.",
        ("pŕstėnj", "prsten", "koljce"),
        (),
        "held: do not promote automatically",
    ),
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def canonical_latin_files(corpus: Path) -> list[Path]:
    # The path list is small (221 current units); file bodies are never retained.
    return sorted(
        path
        for path in corpus.rglob("*.tex")
        if "interslavic" in path.parts
        and "v001" in path.parts
        and "interslavic-cyrillic" not in path.parts
        and "working" not in path.parts
    )


def run_probe(text: str, sources: tuple[str, ...], marker: str) -> tuple[str, dict[str, int]]:
    mappings = tuple((source, marker) for source in sorted(sources, key=len, reverse=True))
    raw_counts: dict[tuple[str, str], int] = {}
    transformed = transform_tex(text, mappings, raw_counts)
    counts = {source: raw_counts.get((source, marker), 0) for source in sources}
    return transformed, counts


def changed_line_examples(
    relative: str,
    original: str,
    transformed: str,
    remaining: int,
) -> list[dict[str, object]]:
    if remaining <= 0 or original == transformed:
        return []
    before_lines = original.splitlines()
    after_lines = transformed.splitlines()
    examples: list[dict[str, object]] = []
    for line_number, (before, after) in enumerate(zip(before_lines, after_lines), start=1):
        if before == after:
            continue
        examples.append(
            {
                "path": relative,
                "line": line_number,
                "before": before.strip()[:500],
                "probe_after": after.strip()[:500],
            }
        )
        if len(examples) >= remaining:
            break
    return examples


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--examples-per-rule", type=int, default=5)
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    corpus = args.corpus.resolve()
    files = canonical_latin_files(corpus)
    if not files:
        raise SystemExit(f"No canonical Interslavic Latin TeX found under {corpus}")

    state: dict[str, dict[str, object]] = {
        rule.rule_id: {
            "classification": rule.classification,
            "description": rule.description,
            "sources": list(rule.sources),
            "proposed_target": rule.proposed_target,
            "source_occurrences": {source: 0 for source in rule.sources},
            "source_occurrence_total": 0,
            "affected_files": 0,
            "target_probe_occurrences": {target: 0 for target in rule.target_probe},
            "examples": [],
        }
        for rule in RULES
    }

    aggregate = hashlib.sha256()
    total_bytes = 0
    largest_file_bytes = 0
    for path in files:
        raw = path.read_bytes()
        total_bytes += len(raw)
        largest_file_bytes = max(largest_file_bytes, len(raw))
        text = raw.decode("utf-8-sig")
        relative = path.relative_to(corpus).as_posix()
        aggregate.update(relative.encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(bytes.fromhex(sha256_bytes(raw)))

        for rule in RULES:
            record = state[rule.rule_id]
            marker = f"NORMPROBE{rule.rule_id.upper().replace('_', '')}"
            transformed, counts = run_probe(text, rule.sources, marker)
            file_total = sum(counts.values())
            if file_total:
                record["affected_files"] = int(record["affected_files"]) + 1
                record["source_occurrence_total"] = int(record["source_occurrence_total"]) + file_total
                source_occurrences = record["source_occurrences"]
                assert isinstance(source_occurrences, dict)
                for source, count in counts.items():
                    source_occurrences[source] = int(source_occurrences[source]) + count
                examples = record["examples"]
                assert isinstance(examples, list)
                examples.extend(
                    changed_line_examples(
                        relative,
                        text,
                        transformed,
                        args.examples_per_rule - len(examples),
                    )
                )

            _, target_counts = run_probe(text, rule.target_probe, marker + "TARGET")
            target_record = record["target_probe_occurrences"]
            assert isinstance(target_record, dict)
            for target, count in target_counts.items():
                target_record[target] = int(target_record[target]) + count

    report = {
        "schema": "interslavic-normalization-status-audit-v2",
        "generated_at": datetime.now().astimezone().isoformat(),
        "scope": {
            "corpus": str(corpus),
            "selection": "canonical **/interslavic/v001/*.tex only; working/cumulative drafts excluded",
            "file_count": len(files),
            "total_utf8_file_bytes": total_bytes,
            "largest_single_file_bytes": largest_file_bytes,
            "aggregate_path_and_filehash_sha256": aggregate.hexdigest().upper(),
        },
        "memory_policy": {
            "file_bodies_loaded_concurrently": 1,
            "examples_capped_per_rule": args.examples_per_rule,
            "whole_corpus_body_materialized": False,
            "parallel_recursive_scans": False,
        },
        "dictionary_evidence": {
            "path": str(
                Path(
                    r"C:\Users\Floris\Documents\CLAUDE PLEASE DONT DELETE WINDOWS 32\_claude_aid\interlingua_program_20260704\data\isv_words_list.csv"
                )
            ),
            "sha256": "072DE8E512EB386780D199FBD6F0ACF2639D3096EA920F1AF2D0AFCC5535E842",
            "headwords": {
                "jednočasno": {
                    "csv_line": 5038,
                    "id": 3852,
                    "intelligibility_field": "bg+ hr~ pl+ ru- sk+ sr+ uk+",
                    "frequency_field": 6708,
                },
                "jednovrěmenno": {
                    "csv_line": 5068,
                    "id": 16948,
                    "intelligibility_field": "bg+ hr+ pl- ru+ sk- sr+ uk+",
                    "frequency_field": 6700,
                },
            },
            "interpretation": "Both surfaces are sanctioned headwords with complementary recorded branch profiles; dictionary presence does not choose a single corpus standard.",
        },
        "rules": state,
        "interpretation_limits": [
            "Counts are TeX-aware prose-node probes; comments, math, and protected identifier/URL/citation arguments are excluded by the tranche parser.",
            "Probes are case-insensitive root searches; a family count may include inflections or embedded strings and is a routing inventory, not an executable replacement count.",
            "Target probes measure surface presence, not comprehension or independent branch support.",
            "Family/cohort dependence and adverse evidence must be considered before any lexical switch.",
            "The correspond-family still requires a reviewed inflection table; this audit does not synthesize one.",
            "The community dictionary contains both jednočasno and jednovrěmenno; neither may be collapsed solely from a draft normalization claim.",
            "No result is community or external certification.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"wrote {args.output}")
    print(f"files={len(files)} total_bytes={total_bytes} largest_file={largest_file_bytes}")
    for rule in RULES:
        record = state[rule.rule_id]
        print(
            f"{rule.rule_id}: source={record['source_occurrence_total']} "
            f"files={record['affected_files']} targets={record['target_probe_occurrences']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
