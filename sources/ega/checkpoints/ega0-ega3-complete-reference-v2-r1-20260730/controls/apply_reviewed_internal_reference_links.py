#!/usr/bin/env python3
"""Apply the manually adjudicated same-reader EGA 0/EGA III links.

This is intentionally a closed action list.  It does not infer links and it
does not touch external-work or cross-volume references.  Every action was
reviewed in source context before this script was frozen.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path


LABELS = {
    "ega0/ega0-3.tex": {
        "3.3.2.1": "0.3.3.2.1",
        "3.5.4.2": "0.3.5.4.2",
        "3.5.4.3": "0.3.5.4.3",
    },
    "ega0/ega0-4.tex": {"4.2.2.2": "0.4.2.2.2"},
    "ega0/ega0-5.tex": {
        "5.4.4.1": "0.5.4.4.1",
        "5.4.8.1": "0.5.4.8.1",
    },
    "ega0/ega0-8.tex": {"8.1.3.1": "0.8.1.3.1"},
    "ega3/ega3-1.tex": {
        "1.1.3.3": "III.1.1.3.3",
        "1.2.2.3": "III.1.2.2.3",
        "1.2.3.1": "III.1.2.3.1",
        "1.2.3.2": "III.1.2.3.2",
        "1.4.5.1": "III.1.4.5.1",
        "1.4.10.1": "III.1.4.10.1",
        "1.4.10.2": "III.1.4.10.2",
        "1.4.10.3": "III.1.4.10.3",
        "1.4.11.1": "III.1.4.11.1",
        "1.4.15.2": "III.1.4.15.2",
        "1.4.15.3": "III.1.4.15.3",
    },
}


# relpath -> line -> (visible token, target label, expected occurrences)
LINKS = {
    "ega0/ega0-3.tex": {
        401: [("3.3.2.1", "0.3.3.2.1", 1)],
        535: [("3.5.1.1", "0.3.5.1.1", 1)],
        544: [("3.5.1.1", "0.3.5.1.1", 1)],
        638: [("3.5.3.3", "0.3.5.3.3", 1)],
        644: [
            ("3.5.3.3", "0.3.5.3.3", 1),
            ("3.5.4.2", "0.3.5.4.2", 1),
        ],
        669: [("3.5.4.3", "0.3.5.4.3", 1)],
    },
    "ega0/ega0-4.tex": {
        344: [("4.2.2.2", "0.4.2.2.2", 1)],
        499: [("4.3.3.1", "0.4.3.3.1", 1)],
    },
    "ega0/ega0-5.tex": {
        31: [("4.4.3.3", "0.4.4.3.3", 1)],
        314: [("5.4.4.1", "0.5.4.4.1", 1)],
        323: [("5.4.4.1", "0.5.4.4.1", 1)],
        328: [
            ("4.4.3.2", "0.4.4.3.2", 2),
            ("5.4.4.1", "0.5.4.4.1", 1),
        ],
        332: [("4.3.3.1", "0.4.3.3.1", 1)],
        381: [("5.4.8.1", "0.5.4.8.1", 1)],
        382: [("5.4.8.1", "0.5.4.8.1", 1)],
        409: [
            ("4.4.3.2", "0.4.4.3.2", 1),
            ("4.2.2.1", "0.4.2.2.1", 1),
        ],
    },
    "ega0/ega0-6.tex": {
        394: [("6.1", "subsection:0.6.1", 1)],
        430: [("6.7.6.1", "0.6.7.6.1", 1)],
    },
    "ega0/ega0-8.tex": {
        78: [("8.1.3.1", "0.8.1.3.1", 1)],
        98: [("8.1.3.1", "0.8.1.3.1", 1)],
    },
    "ega0/ega0-11.tex": {
        133: [
            ("11.1.1.2", "0.11.1.1.2", 1),
            ("11.1.1.3", "0.11.1.1.3", 1),
        ],
    },
    "ega0/ega0-12.tex": {
        800: [("3.3.2", "0.3.3.2", 1)],
    },
    "ega0/ega0-13.tex": {
        672: [("3.2.6", "0.3.2.6", 1)],
        714: [("3.2.6", "0.3.2.6", 1)],
    },
    "ega3.tex": {
        43: [("3.4", "subsection:III.3.4", 1)],
    },
    "ega3/ega3-1.tex": {
        71: [("1.1.2.3", "III.1.1.2.3", 1)],
        72: [("1.1.2.3", "III.1.1.2.3", 1)],
        87: [("1.1.3.3", "III.1.1.3.3", 1)],
        89: [
            ("1.1.3.3", "III.1.1.3.3", 1),
            ("1.1.3.5", "III.1.1.3.5", 1),
        ],
        258: [
            ("1.1.2.3", "III.1.1.2.3", 1),
            ("1.2.2.3", "III.1.2.2.3", 1),
        ],
        278: [("1.2.3.1", "III.1.2.3.1", 1)],
        279: [("1.2.3.2", "III.1.2.3.2", 1)],
        285: [("1.2.3.2", "III.1.2.3.2", 1)],
        290: [
            ("1.2.3.1", "III.1.2.3.1", 1),
            ("1.2.3.2", "III.1.2.3.2", 1),
        ],
        464: [("1.4.5.1", "III.1.4.5.1", 1)],
        549: [("1.4.10.1", "III.1.4.10.1", 1)],
        558: [
            ("1.4.10.3", "III.1.4.10.3", 1),
            ("1.4.10.2", "III.1.4.10.2", 1),
            ("1.4.10.1", "III.1.4.10.1", 1),
        ],
        639: [
            ("1.4.15.3", "III.1.4.15.3", 1),
            ("1.4.15.2", "III.1.4.15.2", 1),
        ],
        659: [
            ("1.4.11.1", "III.1.4.11.1", 1),
            ("1.4.15.3", "III.1.4.15.3", 1),
        ],
        713: [("1.4.16.1", "III.1.4.16.1", 1)],
    },
    "ega3/ega3-2.tex": {
        31: [
            ("2.1.1.2", "III.2.1.1.2", 1),
            ("2.1.1.3", "III.2.1.1.3", 1),
        ],
        35: [("2.1.1.3", "III.2.1.1.3", 1)],
        54: [("1.2.2", "III.1.2.2", 1)],
        56: [("1.2.2", "III.1.2.2", 1)],
        57: [("1.2.2", "III.1.2.2", 2)],
        64: [("1.2.2", "III.1.2.2", 1)],
        72: [("1.2.2", "III.1.2.2", 1)],
        91: [("2.1.1.1", "III.2.1.1.1", 1)],
        153: [("1.2.5", "III.1.2.5", 1)],
        197: [("1.1.3.5", "III.1.1.3.5", 1)],
        202: [("2.1.8.1", "III.2.1.8.1", 1)],
        211: [("2.1.2", "III.2.1.2", 1)],
        244: [("1.1.3.5", "III.1.1.3.5", 1)],
        251: [("2.1.11.1", "III.2.1.11.1", 1)],
        273: [("2.1.5.2", "III.2.1.5.2", 1)],
        274: [("2.1.5.2", "III.2.1.5.2", 1)],
    },
    "ega3/ega3-3.tex": {
        154: [("3.3.1.1", "III.3.3.1.1", 1)],
        237: [("3.4.2.2", "III.3.4.2.2", 1)],
        308: [("3.4.2.2", "III.3.4.2.2", 1)],
        326: [("3.4.5.1", "III.3.4.5.1", 1)],
        328: [("3.4.2.2", "III.3.4.2.2", 1)],
    },
    "ega3/ega3-4.tex": {
        328: [("3.4.2.2", "III.3.4.2.2", 1)],
    },
    "ega3/ega3-6.tex": {
        50: [
            ("6.3", "subsection:III.6.3", 1),
            ("6.7", "subsection:III.6.7", 1),
        ],
        52: [("6.7", "subsection:III.6.7", 1)],
    },
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: apply_reviewed_internal_reference_links.py WORK_ROOT")
    root = Path(sys.argv[1]).resolve()
    source = root / "source"
    report = {
        "schema": "ega3-reviewed-internal-reference-application-1.0",
        "status": "PASS",
        "errors": [],
        "label_insertions": [],
        "link_insertions": [],
        "files": [],
    }
    relpaths = sorted(set(LABELS) | set(LINKS))
    staged: dict[str, str] = {}
    before: dict[str, bytes] = {}
    try:
        for relpath in relpaths:
            path = source / relpath
            data = path.read_bytes()
            before[relpath] = data
            staged[relpath] = data.decode("utf-8")

        for relpath, declarations in LABELS.items():
            text = staged[relpath]
            for tag, label in declarations.items():
                old = rf"\tag{{{tag}}}"
                new = old + rf"\label{{{label}}}"
                if new in text:
                    raise RuntimeError(f"label action already applied: {relpath} {label}")
                count = text.count(old)
                if count != 1:
                    raise RuntimeError(
                        f"tag declaration count mismatch: {relpath} {tag}: {count}"
                    )
                text = text.replace(old, new, 1)
                report["label_insertions"].append(
                    {"source_relpath": relpath, "tag": tag, "label": label}
                )
            staged[relpath] = text

        for relpath, line_actions in LINKS.items():
            lines = staged[relpath].splitlines(keepends=True)
            for line_number, actions in line_actions.items():
                if line_number < 1 or line_number > len(lines):
                    raise RuntimeError(f"line out of range: {relpath}:{line_number}")
                line = lines[line_number - 1]
                for visible, target, expected in actions:
                    wrapper = rf"\hyperref[{target}]{{{visible}}}"
                    if wrapper in line:
                        raise RuntimeError(
                            f"link action already applied: {relpath}:{line_number} {visible}"
                        )
                    pattern = re.compile(
                        rf"(?<![A-Za-z0-9.]){re.escape(visible)}(?![A-Za-z0-9])"
                    )
                    matches = list(pattern.finditer(line))
                    if len(matches) != expected:
                        raise RuntimeError(
                            f"visible occurrence mismatch: {relpath}:{line_number} "
                            f"{visible}: {len(matches)} != {expected}"
                        )
                    line = pattern.sub(lambda _match: wrapper, line)
                    report["link_insertions"].append(
                        {
                            "source_relpath": relpath,
                            "source_line": line_number,
                            "visible_text": visible,
                            "target_label": target,
                            "occurrences": expected,
                        }
                    )
                lines[line_number - 1] = line
            staged[relpath] = "".join(lines)

        for relpath in relpaths:
            path = source / relpath
            after = staged[relpath].encode("utf-8")
            path.write_bytes(after)
            report["files"].append(
                {
                    "source_relpath": relpath,
                    "before_bytes": len(before[relpath]),
                    "before_sha256": sha256(before[relpath]),
                    "after_bytes": len(after),
                    "after_sha256": sha256(after),
                }
            )
    except Exception as exc:
        report["status"] = "FAIL"
        report["errors"].append(str(exc))
        print(json.dumps(report, indent=2))
        return 1

    report["counts"] = {
        "files_mutated": len(relpaths),
        "labels_inserted": len(report["label_insertions"]),
        "link_action_rows": len(report["link_insertions"]),
        "visible_link_occurrences": sum(
            row["occurrences"] for row in report["link_insertions"]
        ),
    }
    out = root / "controls" / "REFERENCE_ONLY_LINK_APPLICATION.json"
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", **report["counts"], "report": str(out)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
