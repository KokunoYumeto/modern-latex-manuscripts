#!/usr/bin/env python3
"""Build the four-concept v4 FAC/EGA provenance replacement specification.

The frozen v4 tranche retains the exact 34-object dual-DOI transport surface.
Every transport name already exists on the methodology and replication
predecessors, so the guarded policy is explicit named replacement rather than
additional files.  FAC/GAGA and EGA likewise replace their existing provenance
objects.  Deligne and SGA7 are excluded because their bytes are unchanged.
This builder performs local and anonymous public reads only; it creates no
Zenodo draft.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import build_all_session_provenance_release_spec_20260802 as base


REPO_ROOT = Path(__file__).resolve().parents[1]
PUBLICATION_DATE = "2026-08-03"
RELEASE_ID = "all-session-mathematical-provenance-20260803-v4"
TRANCHE_RELATIVE = Path(
    "manifests/provenance-tranches/20260803T001725CEST_all-session-v4"
)
DEFAULT_OUTPUT = REPO_ROOT / (
    "manifests/zenodo-active-custody/all-session-provenance-20260803-v4"
)
TARGETS: dict[str, dict[str, Any]] = {
    "methodology": {
        "record_id": 21_762_751,
        "concept_id": 21_124_403,
        "concept_doi": "10.5281/zenodo.21124403",
        "version_doi": "10.5281/zenodo.21762751",
    },
    "replication": {
        "record_id": 21_762_799,
        "concept_id": 20_461_174,
        "concept_doi": "10.5281/zenodo.20461174",
        "version_doi": "10.5281/zenodo.21762799",
    },
    "fac_gaga": {
        "record_id": 21_762_806,
        "concept_id": 21_720_996,
        "concept_doi": "10.5281/zenodo.21720996",
        "version_doi": "10.5281/zenodo.21762806",
    },
    "ega": {
        "record_id": 21_762_807,
        "concept_id": 20_414_353,
        "concept_doi": "10.5281/zenodo.20414353",
        "version_doi": "10.5281/zenodo.21762807",
    },
}
SAFE_PUBLISH_ORDER = ("methodology", "replication", "fac_gaga", "ega")
CORPUS_NAMES = {
    "fac_gaga": base.CORPUS_NAMES["fac_gaga"],
    "ega": base.CORPUS_NAMES["ega"],
}


def metadata_append(key: str, github_commit: str) -> dict[str, Any]:
    descriptions = {
        "methodology": (
            "<p>Replaces the bounded 34-object all-session provenance surface "
            "with coherent v4 bytes captured at 2026-08-03 00:17 CEST. The "
            "complete privacy-clean projection now represents 407 exact files: "
            "17 FAC controls/logbooks, 321 EGA English/French controls/logbooks, "
            "52 unchanged Deligne files, 14 unchanged SGA7 files, and the updated "
            "append-only shared decision log. The identical 34-object surface is "
            "deposited on the replication DOI.</p>"
        ),
        "replication": (
            "<p>Replaces the bounded 34-object provenance surface with the exact "
            "same privacy-clean v4 payload deposited on the methodology DOI. It "
            "preserves 407 FAC, EGA, Deligne, SGA7, archive-control, error, "
            "reversal, decision, and continuation files without selecting only "
            "preferred outputs.</p>"
        ),
        "fac_gaga": (
            "<p>Replaces the five FAC provenance objects with a complete "
            "18-member ZIP/manifest surface representing 17 current files. The "
            "bounded checkpoint passes through printed p.268 / no.73 and preserves "
            "the chronological log, editorial rationale, correction/reversal "
            "ledgers, validation, status, and next cursor at no.74.</p>"
        ),
        "ega": (
            "<p>Replaces the seven EGA provenance objects with a complete "
            "322-member ZIP/manifest surface representing 321 current English "
            "correction and French diplomatic-canon files. The coherent checkpoint "
            "closes EGA I printed p.104 / English R33, preserves all validation and "
            "workflow-error ledgers, and records printed p.105 as the next cursor.</p>"
        ),
    }
    versions = {
        "methodology": "2026-08-03 v0.21 FAC/EGA provenance successor",
        "replication": "2026-08-03 FAC/EGA provenance successor",
        "fac_gaga": "2026-08-03 FAC provenance through no.73",
        "ega": "2026-08-03 EGA I provenance through printed p.104",
    }
    github_url = (
        "https://github.com/KokunoYumeto/modern-latex-manuscripts/tree/"
        f"{github_commit}/{TRANCHE_RELATIVE.as_posix()}"
    )
    return {
        "version_suffix": versions[key],
        "description_html": descriptions[key],
        "cross_links": [
            {
                "identifier": github_url,
                "scheme": "url",
                "relation_type": "issupplementedby",
            }
        ],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--github-commit", required=True)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    base.verify_github_commit(args.github_commit)
    output = args.output_dir.resolve()
    allowed = (REPO_ROOT / "manifests/zenodo-active-custody").resolve()
    if output == allowed or allowed not in output.parents:
        raise RuntimeError(f"Output escaped guarded manifest root: {output}")
    if output.exists():
        raise RuntimeError(f"Output already exists: {output}")
    output.mkdir(parents=True)

    tranche = (REPO_ROOT / TRANCHE_RELATIVE).resolve()
    rows = base.load_tranche(tranche)
    dual_rows = [base.release_row(row, output, dual=True) for row in rows]
    target_rows: dict[str, list[dict[str, Any]]] = {
        "methodology": dual_rows,
        "replication": dual_rows,
    }
    for key, names in CORPUS_NAMES.items():
        selected = [row for row in rows if row["name"] in names]
        if {row["name"] for row in selected} != names:
            raise RuntimeError(f"Incomplete {key} provenance selection")
        target_rows[key] = [
            base.release_row(row, output, dual=False) for row in selected
        ]

    manifest_paths: dict[str, Path] = {}
    manifest_guards: dict[str, dict[str, Any]] = {}
    for key in TARGETS:
        path = output / f"{key}_upload_manifest.json"
        manifest_paths[key] = path
        manifest_guards[key] = base.write_manifest(path, target_rows[key])

    with base.make_session() as session:
        guards = {
            key: base.predecessor_guard(session, key, registry)
            for key, registry in TARGETS.items()
        }

    replacement_names: dict[str, list[str]] = {}
    for key, guard in guards.items():
        new_names = {row["name"] for row in target_rows[key]}
        old_names = {row["name"] for row in guard["files"]}
        if not new_names or not new_names.issubset(old_names):
            raise RuntimeError(
                f"{key} v4 must replace existing names only: "
                f"new-only={sorted(new_names - old_names)}"
            )
        replacement_names[key] = sorted(new_names)
        if int(guard["file_count"]) > base.MAX_ZENODO_FILES:
            raise RuntimeError(f"{key} predecessor already exceeds the file limit")

    targets: dict[str, Any] = {}
    for key in TARGETS:
        targets[key] = {
            "predecessor_guard": guards[key],
            "manifest_path": manifest_paths[key].name,
            "manifest_guard": manifest_guards[key],
            "file_policy": {
                "mode": "add-or-replace-named",
                "replace_names": replacement_names[key],
            },
            "metadata_append": metadata_append(key, args.github_commit),
        }

    spec = {
        "schema": base.SCHEMA,
        "release_id": RELEASE_ID,
        "publication_date": PUBLICATION_DATE,
        "github_commit": args.github_commit,
        "safe_publish_order": list(SAFE_PUBLISH_ORDER),
        "control": {
            "path": base.path_for_manifest(base.CONTROL_PATH, output),
            "bytes": base.CONTROL_BYTES,
            "sha256": base.CONTROL_SHA256,
        },
        "targets": targets,
    }
    spec_path = output / "release_spec.json"
    spec_path.write_text(
        json.dumps(spec, ensure_ascii=True, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    summary = {
        "status": "PASS_READ_ONLY_4_CONCEPT_REPLACEMENT_SPEC",
        "release_id": RELEASE_ID,
        "github_commit": args.github_commit,
        "release_spec": {
            "path": spec_path.name,
            "bytes": spec_path.stat().st_size,
            "sha256": base.sha256_path(spec_path),
        },
        "targets": {
            key: {
                "concept_doi": TARGETS[key]["concept_doi"],
                "predecessor_record": TARGETS[key]["record_id"],
                "predecessor_files": guards[key]["file_count"],
                "replacement_files": len(target_rows[key]),
                "successor_files": guards[key]["file_count"],
                "replacement_bytes": sum(
                    int(row["bytes"]) for row in target_rows[key]
                ),
                "manifest_bytes": manifest_guards[key]["bytes"],
                "manifest_sha256": manifest_guards[key]["sha256"],
            }
            for key in TARGETS
        },
        "unchanged_concepts_not_versioned": {
            "deligne": "10.5281/zenodo.20410853",
            "sga7": "10.5281/zenodo.20410947",
        },
        "dual_payload_identical": (
            target_rows["methodology"] == target_rows["replication"]
        ),
        "draft_created": False,
        "zenodo_mutation_performed": False,
    }
    (output / "BUILD_VALIDATION.json").write_text(
        json.dumps(summary, ensure_ascii=True, sort_keys=True, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(summary, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
