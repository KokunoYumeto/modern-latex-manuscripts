import copy
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STAMP = "20260702T014000Z"
PREVIOUS = ROOT / "logs" / "ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_20260701T200500Z.json"
REFRESH = ROOT / "logs" / "CONTROLLED_ARABIC_ALGEBRA_SOURCE_REFRESH_20260702T013000Z.json"
OUT_JSON = ROOT / "logs" / f"ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_{STAMP}.json"
OUT_MD = ROOT / "logs" / f"ARABIC_PERSIANATE_LANE_STATUS_MANIFEST_{STAMP}.md"


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def dir_stats(path: Path) -> dict:
    files = [p for p in path.rglob("*") if p.is_file()]
    suffix_counts = {}
    for p in files:
        suffix = p.suffix.lower() or "[no_suffix]"
        suffix_counts[suffix] = suffix_counts.get(suffix, 0) + 1
    return {
        "path": rel(path),
        "present": path.exists(),
        "file_count": len(files),
        "bytes": sum(p.stat().st_size for p in files),
        "pdf_count": suffix_counts.get(".pdf", 0),
        "tex_count": suffix_counts.get(".tex", 0),
        "json_count": suffix_counts.get(".json", 0),
        "txt_count": suffix_counts.get(".txt", 0),
        "html_count": suffix_counts.get(".html", 0),
        "suffix_counts": dict(sorted(suffix_counts.items())),
    }


def file_record(path: Path) -> dict:
    import hashlib

    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return {
        "path": rel(path),
        "present": path.exists(),
        "bytes": path.stat().st_size,
        "sha256": h.hexdigest().upper(),
    }


def write_markdown(payload: dict) -> None:
    refresh = payload["arabic"]["evidence"]["algebra_source_refresh"]
    summary = refresh["summary"]
    lines = [
        "# Arabic / Persianate Lane Status Manifest",
        "",
        f"Generated UTC: `{payload['generated_utc']}`",
        "",
        "## Status",
        "",
        f"- Overall status: `{payload['status']}`",
        f"- Current local baseline: {payload['edition_decision']['current_local_baseline']}",
        f"- Cumulative reader lane: `{payload['edition_decision']['is_cumulative_reader_lane']}`",
        f"- Final public edition lane: `{payload['edition_decision']['is_final_public_edition_lane']}`",
        "",
        "## New Arabic Algebra Refresh",
        "",
        f"- Source root: `{refresh['source_root']}`",
        f"- Candidates: `{summary['candidate_count']}`",
        f"- Downloaded: `{summary['downloaded_count']}`",
        f"- Text extracted: `{summary['text_extracted_count']}`",
        f"- Official/direct algebra-register witnesses: `{summary['official_or_direct_algebra_register_count']}`",
        f"- Direct ring/rings-fields witnesses: `{summary['direct_ring_or_rings_fields_count']}`",
        f"- Strong direct invariant-theory witnesses: `{summary['strong_direct_invariant_theory_source_count']}`",
        f"- Accepted algebra-register IDs: `{', '.join(refresh['accepted_algebra_register_source_ids'])}`",
        "",
        "## Boundary",
        "",
    ]
    for reason in payload["edition_decision"]["why_not_final"]:
        lines.append(f"- {reason}")
    lines.extend(["", "## Next Actions", ""])
    for action in payload["next_actions"]:
        lines.append(f"- {action}")
    lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    previous = load(PREVIOUS)
    refresh = load(REFRESH)
    payload = copy.deepcopy(previous)
    payload["artifact"] = "arabic_persianate_lane_status_manifest"
    payload["generated_utc"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    payload["status"] = "manifest_only_no_translation_or_term_promotion_arabic_algebra_register_strengthened"
    payload["previous_manifest"] = rel(PREVIOUS)
    source_root = ROOT / refresh["source_root"]
    payload["source_roots"]["arabic_algebra_source_refresh"] = dir_stats(source_root)
    payload["arabic"]["evidence"]["algebra_source_refresh"] = {
        "file": file_record(REFRESH),
        "artifact": refresh["artifact"],
        "status": refresh["status"],
        "source_root": refresh["source_root"],
        "summary": refresh["summary"],
        "accepted_algebra_register_source_ids": refresh["accepted_algebra_register_source_ids"],
        "strong_direct_invariant_theory_source_ids": refresh["strong_direct_invariant_theory_source_ids"],
        "policy": refresh["policy"],
    }
    payload["arabic"]["invariant_theory_boundary"] = {
        **payload["arabic"]["invariant_theory_boundary"],
        "strong_direct_arabic_specialist_source_count": 0,
        "decision": "invariant_theory_gap_remains_open_after_20260702_algebra_refresh",
        "latest_refresh": rel(REFRESH),
    }
    payload["edition_decision"] = {
        **payload["edition_decision"],
        "current_local_baseline": (
            "Arabic/Persianate lane has source-evidence shelves and split-policy ledgers; "
            "the July 2 refresh strengthens controlled Arabic algebra/ring-field register evidence, "
            "but no cumulative Noether reader or final terminology authority exists."
        ),
        "why_not_final": [
            "No Arabic, Farsi, Dari, or Tajik cumulative Noether TeX/PDF reader is established by this manifest.",
            "Arabic algebra/ring-field evidence is stronger after the July 2 refresh, but Arabic invariant-theory evidence remains weak/secondary for specialist promotion.",
            "The July 2 refresh is a source-evidence shelf only; it does not promote glossary rows, translations, or reviewer closure.",
            "Dari evidence is mostly PDF/pathway/non-PDF lead evidence and explicitly no-promotion.",
            "Tajik evidence is Cyrillic PDF/text evidence with ambiguity boundaries and no TeX/source-code lane.",
            "Native/external review and accepted-correction closure remain open for all sublanes.",
        ],
    }
    payload["next_actions"] = [
        "Use the July 2 controlled Arabic algebra refresh for Arabic ring/field/ideal/module reviewer prompts and term triangulation.",
        "Continue a specialist-only search for direct Arabic invariant-theory, covariant, binary-form, and ring-of-invariants sources before hard-term promotion.",
        "Use Persian TeX linear-algebra evidence for cautious Farsi register checks, not as Dari/Tajik authority.",
        "Keep Dari and Tajik review packets source-pathway focused until native authority or stronger term evidence is obtained.",
        "Only create cumulative readers after a separate source-fidelity translation pass with sidecars and render validation.",
    ]
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(payload)
    print(json.dumps({"json": rel(OUT_JSON), "markdown": rel(OUT_MD), "source_root": refresh["source_root"]}, indent=2))


if __name__ == "__main__":
    main()
