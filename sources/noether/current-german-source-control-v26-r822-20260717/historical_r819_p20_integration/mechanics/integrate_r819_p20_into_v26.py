from __future__ import annotations

import argparse
import difflib
import hashlib
import json
from pathlib import Path


START = r"\section*{20. Ein algebraisches Kriterium für absolute Irreduzibilität.}"
END = r"\section*{21. Formale Variationsrechnung und Differentialinvarianten}"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def split_paper(text: str) -> tuple[str, str, str]:
    if text.count(START) != 1 or text.count(END) != 1:
        raise RuntimeError("Paper 20/21 boundary markers are not unique")
    start = text.index(START)
    end = text.index(END, start)
    return text[:start], text[start:end], text[end:]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("base", type=Path)
    parser.add_argument("incoming", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("diff", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()

    base_bytes = args.base.read_bytes()
    incoming_bytes = args.incoming.read_bytes()
    base_text = base_bytes.decode("utf-8")
    incoming_text = incoming_bytes.decode("utf-8")
    base_prefix, base_p20, base_suffix = split_paper(base_text)
    incoming_prefix, incoming_p20, incoming_suffix = split_paper(incoming_text)

    required = (
        r"S(Z,u)=\sum \Phi_\lambda(Z)U_\lambda",
        r"\emph{mindestens eine Zerlegung zuläßt.}",
        r"\emph{Reduzibilitätsform von $E(x)$}",
        r"\srcnumdisplay{(14)}",
    )
    for needle in required:
        if needle not in incoming_p20:
            raise RuntimeError(f"Incoming Paper 20 is missing required R818/R819 locus: {needle}")
    if r"S(Z,u)=\sum \Phi_\lambda(Z)U_i" not in base_p20:
        raise RuntimeError("Base Paper 20 no longer has the expected pre-R818 U_i locus")

    integrated = base_prefix + incoming_p20 + base_suffix
    check_prefix, check_p20, check_suffix = split_paper(integrated)
    if check_prefix != base_prefix or check_suffix != base_suffix:
        raise RuntimeError("Material outside Paper 20 changed during integration")
    if check_p20 != incoming_p20:
        raise RuntimeError("Integrated Paper 20 differs from the sealed R819 input")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(integrated, encoding="utf-8", newline="\n")
    diff = difflib.unified_diff(
        base_p20.splitlines(keepends=True),
        incoming_p20.splitlines(keepends=True),
        fromfile=args.base.name + ":Paper20",
        tofile=args.incoming.name + ":Paper20",
        n=4,
    )
    args.diff.write_text("".join(diff), encoding="utf-8", newline="\n")

    output_bytes = args.output.read_bytes()
    report = {
        "base": str(args.base.resolve()),
        "base_sha256": sha256(base_bytes),
        "incoming": str(args.incoming.resolve()),
        "incoming_sha256": sha256(incoming_bytes),
        "output": str(args.output.resolve()),
        "output_sha256": sha256(output_bytes),
        "base_paper20_lines": len(base_p20.splitlines()),
        "incoming_paper20_lines": len(incoming_p20.splitlines()),
        "outside_paper20_byte_preservation": True,
        "paper20_exactly_matches_r819": True,
    }
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
