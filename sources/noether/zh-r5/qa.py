from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys


HERE = Path(__file__).resolve().parent
BASE = HERE / "base.tex"
TARGET = HERE / "reader.tex"
DIFF = HERE / "diff.json"
OUT = HERE / "qa.json"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def main() -> None:
    if OUT.exists():
        raise RuntimeError("refusing to overwrite qa.json")

    base = BASE.read_bytes()
    target = TARGET.read_bytes()
    diff = json.loads(DIFF.read_text(encoding="utf-8"))
    base_lines = base.splitlines(keepends=True)
    target_lines = target.splitlines(keepends=True)
    failures: list[str] = []

    def check(name: str, condition: bool) -> None:
        if not condition:
            failures.append(name)

    check(
        "base identity",
        len(base) == 1_871_385
        and sha256(base)
        == "910399C8CB6A8A3CC0BE40638C23AFD496C642ACC63127E3AE812CACEF599E33",
    )
    check(
        "target identity",
        len(target) == diff["output"]["bytes"]
        and sha256(target) == diff["output"]["sha256"],
    )

    reconstructed: list[bytes] = []
    cursor = 1
    change_checks = []
    for item in diff["changes"]:
        bs, be = item["base_lines_1_based_inclusive"]
        fs, fe = item["final_lines_1_based_inclusive"]
        reconstructed.extend(base_lines[cursor - 1 : bs - 1])
        before = b"".join(base_lines[bs - 1 : be])
        after_lines = target_lines[fs - 1 : fe]
        after = b"".join(after_lines)
        ok = (
            len(before) == item["before_bytes"]
            and sha256(before) == item["before_sha256"]
            and len(after) == item["after_bytes"]
            and sha256(after) == item["after_sha256"]
        )
        check(f"change identity {item['id']}", ok)
        change_checks.append({"id": item["id"], "identity_pass": ok})
        reconstructed.extend(after_lines)
        cursor = be + 1
    reconstructed.extend(base_lines[cursor - 1 :])
    check("authorized changes only", b"".join(reconstructed) == target)

    text = target.decode("utf-8")
    base_text = base.decode("utf-8")
    p45_item = next(item for item in diff["changes"] if item["id"] == "ZH-R26-P45-001")
    ps, pe = p45_item["final_lines_1_based_inclusive"]
    p45 = b"".join(target_lines[ps - 1 : pe]).decode("utf-8")

    p45_required = [
        r"(g_1)+(g_2)+\cdots+(g_t)=\mu",
        r"f_1\cdot g_1(0,y):y^{(g_1)}",
        r"\mu-(g_1)-(g_2)-\cdots-(g_r)",
        r"K_1\cdot g_1(0,y):y^{(g_1)}",
        r"(f_i,g_i,\mathfrak p^e)=\mathfrak q^{(i)}",
        r"K_i\equiv0(\mathfrak q^{(i)})",
        r"K_{i+1}\equiv0(\mathfrak q^{(i+1)})",
        "应用 \\(t\\) 次",
    ]
    p45_forbidden = [
        r"t \leq \mu,",
        r"f_{t-1} &= g_{t}",
        r"L_{1}",
        r"K_0",
        r"\mathfrak p^{2^i}",
        r"K \cdot f_{\nu}",
        "应用 \\(\\mu\\) 次",
    ]
    required_counts = {item: p45.count(item) for item in p45_required}
    forbidden_counts = {item: p45.count(item) for item in p45_forbidden}
    check("P45 required readings", all(count >= 1 for count in required_counts.values()))
    check("P45 rejected readings absent", all(count == 0 for count in forbidden_counts.values()))
    tag_counts = {str(n): p45.count(rf"\tag{{{n}}}") for n in (1, 2, 3)}
    check("P45 exact tags 1-3", tag_counts == {"1": 1, "2": 1, "3": 1})
    check("P45 three equation environments", p45.count(r"\begin{equation}") == 3 and p45.count(r"\end{equation}") == 3)
    check("P45 source note markers", p45.count(r"\textsuperscript{7)}") == 1 and p45.count(r"\textsuperscript{8)}") == 1)

    note_readings = [
        r"\footnotetext{Mertens，前引处，\S\ 5。}",
        "在代数不变量论中，这一情形一向称为相对不变性",
        r"\footnotetext{由这些无穷小变换，按照 \S{} 4 末尾所述的方法反向求出有限变换。}",
        r"Arithmetische Untersuchungen über endliche Gruppen linearer Substitutionen",
    ]
    note_counts = {item: text.count(item) for item in note_readings}
    check("four restored note readings", all(count == 1 for count in note_counts.values()))
    check("footnote body delta", text.count(r"\footnote{") == base_text.count(r"\footnote{") + 2)
    check("footnotemark delta", text.count(r"\footnotemark") == base_text.count(r"\footnotemark") + 2)
    check("footnotetext delta", text.count(r"\footnotetext") == base_text.count(r"\footnotetext") + 2)

    bib_lines = [
        r"\item 不变变分问题，27, Teil II, (1918), S.~47",
        r"\item 整系数二元不变式的有限性，28, Teil II, (1919), S.~29",
        r"\item 一般理想论中 Hilbert 定理的一个类似物，32, Teil II, (1923), S.~20--21",
        r"\item 关于公理化问题的群论备注，33, Teil II, (1925), S.~21",
        r"\item 理想的微分商与分歧理论，38, Teil II, (1929), S.~81",
        r"40, Teil II, (1931), S.~11--12",
        r"41, Teil II, (1932), S.~17",
        r"42, Teil II, (1933), S.~38--39",
    ]
    bib_counts = {item: text.count(item) for item in bib_lines}
    check("eight bibliography readings", all(count == 1 for count in bib_counts.values()))

    check("r5 title", text.count("pdftitle={Noether Simplified Chinese cumulative rebase r5}") == 1)
    check("v044 provenance", text.count("NOETH-DE-AUTH-v044-20260807") >= 3)
    check("ED0008 provenance", text.count("ED0008") >= 4)
    check("no accepted true claim", "accepted=true" not in text and diff.get("acceptance_claim") is False)

    begin = Counter(re.findall(r"\\begin\{([^}]+)\}", text))
    end = Counter(re.findall(r"\\end\{([^}]+)\}", text))
    base_begin = Counter(re.findall(r"\\begin\{([^}]+)\}", base_text))
    base_end = Counter(re.findall(r"\\end\{([^}]+)\}", base_text))
    check("environment balance", begin == end)
    check("environment multiset unchanged", begin == base_begin and end == base_end)
    check("brace balance preserved", text.count("{") - text.count("}") == base_text.count("{") - base_text.count("}"))
    check("display delimiter multiset preserved", text.count(r"\[") == base_text.count(r"\[") and text.count(r"\]") == base_text.count(r"\]"))
    check("inline delimiter multiset preserved", text.count(r"\(") == base_text.count(r"\(") and text.count(r"\)") == base_text.count(r"\)"))
    check("single dollar parity", len(re.findall(r"(?<!\\)\$", text)) % 2 == 0)
    labels = re.findall(r"\\label\{([^}]+)\}", text)
    check("labels unique", len(labels) == len(set(labels)))

    find_records = [json.loads(line) for line in (HERE / "find.jsonl").read_text(encoding="utf-8").splitlines() if line]
    check("seven finding records", len(find_records) == 7 and len({r["id"] for r in find_records}) == 7)
    check("intake parses", bool(json.loads((HERE / "intake.json").read_text(encoding="utf-8"))))

    result = {
        "id": "ZHCHK-NOETHER-CUM-R5-QA-001",
        "base": {"bytes": len(base), "sha256": sha256(base), "lines": len(base_lines)},
        "target": {"bytes": len(target), "sha256": sha256(target), "lines": len(target_lines)},
        "diff": {"bytes": DIFF.stat().st_size, "sha256": sha256(DIFF.read_bytes()), "changes": len(diff["changes"])},
        "change_checks": change_checks,
        "p45": {
            "base_lines": p45_item["base_lines_1_based_inclusive"],
            "final_lines": p45_item["final_lines_1_based_inclusive"],
            "bytes": len(p45.encode("utf-8")),
            "sha256": sha256(p45.encode("utf-8")),
            "required_counts": required_counts,
            "forbidden_counts": forbidden_counts,
            "tag_counts": tag_counts,
            "equation_3_diplomatic_suspicion_recorded": True,
        },
        "notes": {"counts": note_counts, "footnote_body_delta": 2, "footnotemark_delta": 2, "footnotetext_delta": 2},
        "bibliography": {"counts": bib_counts},
        "structure": {
            "environment_types": len(begin),
            "environment_count": sum(begin.values()),
            "labels": len(labels),
            "brace_open_close": [text.count("{"), text.count("}")],
            "display_open_close": [text.count(r"\["), text.count(r"\]")],
            "inline_open_close": [text.count(r"\("), text.count(r"\)")],
            "single_dollar_count": len(re.findall(r"(?<!\\)\$", text)),
        },
        "failure_count": len(failures),
        "failures": failures,
        "all_pass": not failures,
        "acceptance_claim": False,
        "producer_state": "candidate_pending_build_render_and_independent_review",
        "sga": "held and untouched",
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"all_pass": not failures, "failures": failures}, ensure_ascii=False))
    if failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
