import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "20260702T003500Z"
OUT_JSON = ROOT / "logs" / f"CROSS_LANE_PROMOTION_READINESS_AUDIT_{STAMP}.json"
OUT_MD = ROOT / "logs" / f"CROSS_LANE_PROMOTION_READINESS_AUDIT_{STAMP}.md"


MANIFESTS = {
    "slavic": "logs/SLAVIC_MAINTENANCE_STATUS_MANIFEST_20260701T204500Z.json",
    "french_spanish": "logs/FRENCH_SPANISH_LANE_STATUS_AUDIT_20260701T153500Z.json",
    "spanish": "logs/SPANISH_CUMULATIVE_STATUS_MANIFEST_20260701T160000Z.json",
    "french": "logs/FRENCH_CUMULATIVE_STATUS_MANIFEST_20260701T161500Z.json",
    "chinese_japanese": "logs/CHINESE_JAPANESE_CUMULATIVE_STATUS_MANIFEST_20260701T170500Z.json",
    "arabic_persianate": "logs/ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_20260701T200500Z.json",
    "research_publication": "logs/RESEARCH_PUBLICATION_LANE_STATUS_MANIFEST_20260701T213000Z.json",
    "handoff": "logs/POST_CHECKPOINT_GITHUB_HANDOFF_20260701T223800Z.json",
    "zenodo": "logs/ZENODO_NOETHER_LATEST_LIVE_CHECK_20260701T222409Z.json",
}


def read_json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8-sig"))


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def count_files(root: str, suffixes: tuple[str, ...] | None = None) -> dict:
    base = ROOT / root
    if not base.exists():
        return {"root": root, "exists": False, "file_count": 0, "bytes": 0}
    total = 0
    size = 0
    suffix_counts: dict[str, int] = {}
    for path in base.rglob("*"):
        if not path.is_file():
            continue
        if suffixes and path.suffix.lower() not in suffixes:
            continue
        total += 1
        size += path.stat().st_size
        suffix_counts[path.suffix.lower() or "[none]"] = suffix_counts.get(path.suffix.lower() or "[none]", 0) + 1
    return {"root": root, "exists": True, "file_count": total, "bytes": size, "suffix_counts": suffix_counts}


def latest_package_state(handoff: dict) -> dict:
    checkpoint = handoff["current_checkpoint"]
    zip_path = ROOT / checkpoint["zip"]
    return {
        "zip": checkpoint["zip"],
        "exists": zip_path.is_file(),
        "bytes": zip_path.stat().st_size if zip_path.is_file() else None,
        "sha256": checkpoint["sha256"],
        "builder_overall_pass": checkpoint["builder_overall_pass"],
        "independent_overall_pass": checkpoint["independent_overall_pass"],
        "independent_sha256_matches": checkpoint["independent_sha256_matches"],
        "credential_scan_hits": checkpoint["builder_credential_scan_hits"],
    }


def lane_entry(
    *,
    lane: str,
    status: str,
    evidence: list[str],
    local_claim: str,
    forbidden_claims: list[str],
    gates: list[dict],
    next_actions: list[str],
) -> dict:
    return {
        "lane": lane,
        "status": status,
        "evidence": evidence,
        "local_claim": local_claim,
        "forbidden_claims": forbidden_claims,
        "promotion_gates": gates,
        "next_actions": next_actions,
    }


def record_present(record: dict) -> bool:
    if record.get("exists") is not None:
        return record.get("exists") is True
    if record.get("present") is not None:
        return record.get("present") is True
    path = record.get("path")
    return bool(path) and (ROOT / path).is_file()


def main() -> None:
    data = {name: read_json(path) for name, path in MANIFESTS.items()}
    slavic = data["slavic"]
    fs = data["french_spanish"]
    spanish = data["spanish"]
    french = data["french"]
    cj = data["chinese_japanese"]
    ap = data["arabic_persianate"]
    research = data["research_publication"]
    handoff = data["handoff"]
    zenodo = data["zenodo"]

    source_inventory = {
        "slavic_translation_tree": count_files("translations", (".tex", ".json", ".md")),
        "slavic_render_tree": count_files("renders", (".pdf", ".tex", ".json", ".md")),
        "non_slavic_reference_corpus": count_files("sources/non_slavic_reference_corpus"),
        "non_slavic_translations": count_files("translations/non_slavic", (".json", ".tex", ".md")),
        "non_slavic_renders": count_files("renders/non_slavic", (".pdf", ".tex", ".json", ".md", ".txt")),
    }

    lanes = [
        lane_entry(
            lane="Slavic: Ukrainian, Russian, Interslavic Latin+Cyrillic",
            status="review-ready maintenance lane; no rebuild required at latest check",
            evidence=[
                MANIFESTS["slavic"],
                slavic["prior_validated_artifacts"]["slavic_package"]["path"],
                slavic["prior_validated_artifacts"]["external_review_bundle"]["path"],
            ],
            local_claim=(
                "Local translation files cover Papers 01-43 in Ukrainian, Russian, Interslavic Latin, "
                "and Interslavic Cyrillic; prior package and review bundle validate; Zenodo unchanged."
            ),
            forbidden_claims=[
                "Do not claim external/native review closure until return files are ingested.",
                "Do not rebuild/reissue Slavic cumulative readers merely for churn while Zenodo/review state is unchanged.",
            ],
            gates=[
                {"gate": "Zenodo unchanged", "pass": slavic["zenodo_freshness"]["no_source_replacement_required"] is True},
                {"gate": "Latin and Cyrillic lanes both present", "pass": slavic["script_sidecar_status"]["latin_and_cyrillic_lanes_both_present"] is True},
                {"gate": "Review returns complete", "pass": slavic["review_status"]["complete_for_all_units"] is True},
            ],
            next_actions=slavic["next_actions"],
        ),
        lane_entry(
            lane="Spanish",
            status="cumulative local baseline exists; source-native audit still required before final edition promotion",
            evidence=[
                MANIFESTS["spanish"],
                spanish["spanish_branch_root"],
                fs["source_roots"]["native_register_shelf"],
                fs["source_roots"]["spanish_covariant_tex_broader_retry"],
            ],
            local_claim=spanish["edition_decision"]["current_local_baseline"],
            forbidden_claims=[
                "Do not claim final public edition.",
                "Do not promote patched terminology without source-native audit and visual proof closure.",
            ],
            gates=[
                {"gate": "Cumulative TeX present", "pass": record_present(spanish["current_branch_records"]["cum_es_tex"])},
                {"gate": "Cumulative PDF present", "pass": record_present(spanish["current_branch_records"]["cum_es_pdf"])},
                {"gate": "Final edition lane", "pass": spanish["edition_decision"]["is_final_edition_lane"] is True},
            ],
            next_actions=spanish["next_actions"],
        ),
        lane_entry(
            lane="French",
            status="cumulative local baseline exists; not final edition",
            evidence=[
                MANIFESTS["french"],
                fs["source_roots"]["native_register_shelf"],
                fs["source_roots"]["invariant_hardterm_evidence"],
            ],
            local_claim=french["edition_decision"]["current_local_baseline"],
            forbidden_claims=[
                "Do not claim final public edition.",
                "Do not skip source-native reread of hard algebra/invariant terminology.",
            ],
            gates=[
                {"gate": "Cumulative TeX present", "pass": record_present(french["current_branch_records"]["cum_fr_p40_s09_tex"])},
                {"gate": "Cumulative PDF present", "pass": record_present(french["current_branch_records"]["cum_fr_p40_s09_pdf"])},
                {"gate": "Final edition lane", "pass": french["edition_decision"]["is_final_edition_lane"] is True},
            ],
            next_actions=french["next_actions"],
        ),
        lane_entry(
            lane="Simplified Chinese",
            status=cj["simplified_chinese"]["status"],
            evidence=[
                MANIFESTS["chinese_japanese"],
                cj["source_register_evidence"]["native_math_shelf_root"],
                cj["simplified_chinese"]["current_records"]["source_tex"]["path"],
                cj["simplified_chinese"]["current_records"]["pdf"]["path"],
            ],
            local_claim="Source-fidelity cumulative proof artifact exists with retained visual evidence.",
            forbidden_claims=cj["simplified_chinese"]["open_boundaries"],
            gates=[
                {
                    "gate": "Cumulative TeX exists",
                    "pass": record_present(cj["simplified_chinese"]["current_records"]["source_tex"]),
                },
                {
                    "gate": "Cumulative PDF exists",
                    "pass": record_present(cj["simplified_chinese"]["current_records"]["pdf"]),
                },
                {"gate": "Final public edition", "pass": cj["edition_decision"]["is_final_public_edition_lane"] is True},
            ],
            next_actions=cj["next_actions"],
        ),
        lane_entry(
            lane="Japanese",
            status=cj["japanese"]["status"],
            evidence=[
                MANIFESTS["chinese_japanese"],
                cj["source_register_evidence"]["native_math_shelf_root"],
                cj["japanese"]["current_records"]["source_tex"]["path"],
                cj["japanese"]["current_records"]["pdf"]["path"],
            ],
            local_claim="Source-fidelity cumulative proof artifact exists with term-count and visual-check evidence.",
            forbidden_claims=cj["japanese"]["remaining_boundaries"],
            gates=[
                {
                    "gate": "Cumulative TeX exists",
                    "pass": record_present(cj["japanese"]["current_records"]["source_tex"]),
                },
                {
                    "gate": "Cumulative PDF exists",
                    "pass": record_present(cj["japanese"]["current_records"]["pdf"]),
                },
                {"gate": "Final public edition", "pass": cj["edition_decision"]["is_final_public_edition_lane"] is True},
            ],
            next_actions=cj["next_actions"],
        ),
        lane_entry(
            lane="Arabic / Persian-Farsi / Dari / Tajik",
            status=ap["status"],
            evidence=[
                MANIFESTS["arabic_persianate"],
                ap["source_roots"]["deep_tex_shelf"],
                ap["source_roots"]["arabic_invariant_sweep"],
                ap["source_roots"]["dari_pdf_shelf"],
                ap["source_roots"]["tajik_cyrillic"],
            ],
            local_claim=(
                "Evidence shelves exist and the split policy is explicit; Arabic remains controlled/evidence-limited, "
                "while Persian, Dari, and Tajik are separate register lanes."
            ),
            forbidden_claims=[
                "Do not collapse Iranian Persian, Afghan Dari, and Tajik Cyrillic into a single authority lane.",
                "Do not claim Arabic invariant-theory specialist authority from weak/secondary evidence.",
                "Do not claim cumulative reader construction yet.",
            ],
            gates=[
                {"gate": "Persianate deep TeX shelf has strong sources", "pass": ap["persian_farsi"]["deep_tex_summary"]["strong_exact_math_tex_sources"] > 0},
                {
                    "gate": "Dari algebra-register contexts exist",
                    "pass": ap["dari"]["pdf_shelf_summary"]["strong_algebra_register_context_count"] > 0,
                },
                {
                    "gate": "Arabic direct invariant-theory specialist sources exist",
                    "pass": ap["arabic"]["invariant_theory_boundary"]["strong_direct_arabic_specialist_source_count"] > 0,
                },
                {"gate": "Cumulative reader lane exists", "pass": ap["edition_decision"]["is_cumulative_reader_lane"] is True},
            ],
            next_actions=ap["next_actions"],
        ),
        lane_entry(
            lane="Research/publication and interlanguage methodology",
            status=research["status"],
            evidence=[
                MANIFESTS["research_publication"],
                research["primary_artifacts"]["ai_semiconstructed_agenda"],
                research["primary_artifacts"]["interlanguage_methodology_note"],
                research["primary_artifacts"]["world_family_coordination_index"],
            ],
            local_claim=(
                "A citable evidence map exists for AI-assisted technical-register construction, "
                "semi-constructed/interlanguage methodology, education lanes, and open-source ethics."
            ),
            forbidden_claims=[
                "Do not claim the publication article is finished.",
                "Do not claim language authority from local validation.",
                "Do not frame regional translation lanes as imposed standards.",
            ],
            gates=[
                {"gate": "Publication-ready article", "pass": research["publication_boundary"]["is_publication_ready_article"] is True},
                {"gate": "Language authority claim", "pass": research["publication_boundary"]["is_language_authority_claim"] is True},
                {"gate": "Translation completion claim", "pass": research["publication_boundary"]["is_translation_completion_claim"] is True},
            ],
            next_actions=research["next_actions"],
        ),
    ]

    result = {
        "artifact": "cross_lane_promotion_readiness_audit",
        "generated_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "completion_claim": False,
        "latest_checkpoint": latest_package_state(handoff),
        "github_handoff": {
            "branch": "codex/laptop-noether-language-planning-20260701",
            "metadata_root": "workflow/codex-laptop-handoffs/20260701T223800Z",
            "draft_release_tag": "codex-laptop-noether-language-planning-20260701T222757Z",
            "full_zip_asset_uploaded": True,
        },
        "zenodo_freshness": {
            "path": MANIFESTS["zenodo"],
            "checked_at_utc": zenodo.get("checked_at_utc"),
            "record_id": zenodo.get("record_id"),
            "revision": zenodo.get("revision"),
            "file_count": zenodo.get("file_count"),
            "no_source_replacement_required": zenodo.get("no_source_replacement_required"),
            "changed_files": {
                "added": zenodo.get("added_files"),
                "removed": zenodo.get("removed_files"),
                "size_changed": zenodo.get("size_changed_files"),
                "checksum_changed": zenodo.get("checksum_changed_files"),
            },
        },
        "source_inventory": source_inventory,
        "lanes": lanes,
        "global_decision": {
            "do_now": [
                "Use this audit as the cross-lane gate before translation/revision work.",
                "For any lane marked corpus-only or cumulative-local-baseline, perform source-native reread before public promotion.",
                "Keep Slavic in maintenance mode unless Zenodo or review-return state changes.",
            ],
            "do_not_do": [
                "Do not conflate local mechanical validation with native/external authority.",
                "Do not rebuild large packages solely to include this post-checkpoint audit; publish as branch metadata until the next substantive package checkpoint.",
            ],
        },
    }

    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Cross-Lane Promotion Readiness Audit",
        "",
        f"- Generated UTC: `{result['generated_utc']}`",
        f"- Completion claim: `{result['completion_claim']}`",
        f"- Latest checkpoint: `{result['latest_checkpoint']['zip']}`",
        f"- Checkpoint SHA256: `{result['latest_checkpoint']['sha256']}`",
        f"- Zenodo no source replacement required: `{result['zenodo_freshness']['no_source_replacement_required']}`",
        "",
        "## Lane Decisions",
        "",
    ]
    for lane in lanes:
        failed = [gate["gate"] for gate in lane["promotion_gates"] if gate["pass"] is not True]
        lines.extend(
            [
                f"### {lane['lane']}",
                "",
                f"- Status: {lane['status']}",
                f"- Local claim: {lane['local_claim']}",
                f"- Failed or still-open gates: {', '.join(failed) if failed else 'none'}",
                f"- Primary evidence: `{lane['evidence'][0]}`",
                "",
            ]
        )
    lines.extend(
        [
            "## Global Decision",
            "",
            "- Slavic remains maintenance/watch mode.",
            "- French, Spanish, Chinese, and Japanese have local cumulative baselines/proofs but still need source-native/public-edition promotion gates.",
            "- Arabic/Persianate remains evidence-split and corpus-first, with Arabic specialist invariant evidence still weak.",
            "- Research/publication lane is an evidence map and methods spine, not a finished article.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"json": rel(OUT_JSON), "markdown": rel(OUT_MD), "lane_count": len(lanes)}, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
