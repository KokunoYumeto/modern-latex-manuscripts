from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Regenerate an exact ordinal source-input manifest from a prior row set."
    )
    parser.add_argument("--source-root", required=True, type=Path)
    parser.add_argument("--previous", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--schema", required=True)
    parser.add_argument("--generation-disposition", required=True)
    args = parser.parse_args()

    previous = json.loads(args.previous.read_text(encoding="utf-8"))
    relative_paths = sorted(
        (row["relative_path"] for row in previous["files"]),
        key=lambda value: value,
    )

    rows = []
    errors = []
    for relative_path in relative_paths:
        source_path = args.source_root / Path(relative_path)
        if not source_path.is_file():
            errors.append(f"missing source input: {relative_path}")
            continue
        rows.append(
            {
                "relative_path": relative_path,
                "bytes": source_path.stat().st_size,
                "sha256": sha256(source_path),
            }
        )

    if errors:
        raise SystemExit("\n".join(errors))

    canonical = "".join(
        f"{row['relative_path']}\t{row['bytes']}\t{row['sha256']}\n"
        for row in rows
    ).encode("utf-8")

    predecessor_entry = {
        "relative_path": f"controls/{args.previous.name}",
        "bytes": args.previous.stat().st_size,
        "sha256": sha256(args.previous),
        "disposition": args.generation_disposition,
    }
    preserved = [predecessor_entry]
    preserved.extend(previous.get("preserved_predecessor_manifests", []))

    output = {
        "schema": args.schema,
        "canonicalization": (
            "UTF-8 lines relative_path TAB bytes TAB uppercase_sha256 LF, "
            "Python Unicode code-point order matching .NET ordinal for this "
            "ASCII path set, including final LF"
        ),
        "file_count": len(rows),
        "total_bytes": sum(row["bytes"] for row in rows),
        "canonical_tree_sha256": hashlib.sha256(canonical).hexdigest().upper(),
        "preserved_predecessor_manifests": preserved,
        "files": rows,
    }
    args.output.write_text(
        json.dumps(output, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


if __name__ == "__main__":
    main()
