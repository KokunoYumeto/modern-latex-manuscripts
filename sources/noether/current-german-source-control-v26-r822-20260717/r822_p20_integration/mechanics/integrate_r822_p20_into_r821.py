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


def require_all(text: str, markers: tuple[str, ...], label: str) -> None:
    missing = [marker for marker in markers if marker not in text]
    if missing:
        raise RuntimeError(f"{label} is missing required markers: {missing}")


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
    _, incoming_p20, _ = split_paper(incoming_text)

    require_all(
        incoming_p20,
        (
            r"S(Z,u)=\sum \Phi_\lambda(Z)U_\lambda",
            r"\emph{mindestens eine Zerlegung zuläßt.}",
            r"\emph{Reduzibilitätsform von $E(x)$}",
            r"\srcnumdisplay{(14)}",
            "„Algebraischen Theorie der Körper“",
            r"sich \emph{algebraisch} fassen",
            r"} Mit anderen Worten: \emph{",
            r"\emph{speziell zugrunde gelegten Körper unabhängige Zahlkoeffizienten}",
            r"\emph{Unbestimmten $Z$}",
            r"\emph{Primideal $\mathfrak P$}",
            r"\emph{Nachweis der Umkehrung}",
            r"\emph{ein-eindeutig}",
            r"\emph{Wertsysteme, daß (12) erfüllt ist.}",
            r"\emph{Erweiterungskörper in zwei Faktoren zerfallen}",
            "„im allgemeinen“",
            r"(Hilfssatz S.~296). -- Für den Fall",
            r"d&=l+m+1;",
            r"=t_{p+q}\xi^{p+q}+t_{p+q-1}\xi^{p+q-1}\eta+\cdots+t_0\eta^{p+q};",
            "„Fundamentalsatz der Algebra“",
        ),
        "Sealed R822 Paper 20",
    )
    require_all(
        base_p20,
        (
            r"S(Z,u)=\sum \Phi_\lambda(Z)U_\lambda",
            r"\emph{mindestens eine Zerlegung zuläßt.}",
            r"\emph{Reduzibilitätsform von $E(x)$}",
            r"\srcnumdisplay{(14)}",
        ),
        "Published R821-integrated Paper 20",
    )

    integrated = base_prefix + incoming_p20 + base_suffix
    check_prefix, check_p20, check_suffix = split_paper(integrated)
    if check_prefix.encode("utf-8") != base_prefix.encode("utf-8"):
        raise RuntimeError("Material before Paper 20 changed during integration")
    if check_suffix.encode("utf-8") != base_suffix.encode("utf-8"):
        raise RuntimeError("Material after Paper 20 changed during integration")
    if check_p20.encode("utf-8") != incoming_p20.encode("utf-8"):
        raise RuntimeError("Integrated Paper 20 differs from sealed R822")

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
        "paper20_exactly_matches_sealed_r822": True,
    }
    args.report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
