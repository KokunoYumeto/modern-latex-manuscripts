#!/usr/bin/env python3
"""Build the first sealed-P31-reconciled Paper 37 Hans candidate from the frozen witness."""
from __future__ import annotations

from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
WITNESS = ROOT / "witness/Noether_Paper37_SimplifiedChinese_Inherited_logical_article_LF.tex"
SOURCE = ROOT / "source/Noether_Paper37_German_P31_logical_article_LF.tex"
OUT = ROOT / "zh-Hans-CN/Noether_Paper37_Chinese_P31Reconciled_zh-Hans-CN_v001.tex"
RECORD = ROOT / "qa/HANS_REBASE_TRANSFORM.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


body = WITNESS.read_text(encoding="utf-8")
changes: list[dict] = []


def restore_latex_control_escapes(value: str) -> str:
    """Undo Python control escapes in bounded replacement literals.

    The production text contains TeX commands such as ``\\frakp`` and
    ``\\bar``. This guard makes an accidentally non-raw replacement literal
    fail-safe while the occurrence assertions still bind every edit.
    """
    for control, latex in (
        ("\a", r"\a"),
        ("\b", r"\b"),
        ("\f", r"\f"),
        ("\r", r"\r"),
        ("\t", r"\t"),
        ("\v", r"\v"),
    ):
        value = value.replace(control, latex)
    return value


def replace_once(old: str, new: str, change_id: str, reason: str) -> None:
    global body
    old = restore_latex_control_escapes(old)
    new = restore_latex_control_escapes(new)
    count = body.count(old)
    if count != 1:
        raise SystemExit(f"{change_id}: expected exactly one witness occurrence, found {count}")
    body = body.replace(old, new, 1)
    changes.append({"id": change_id, "occurrences": 1, "reason": reason})


def replace_count(old: str, new: str, expected: int, change_id: str, reason: str) -> None:
    """Replace an exact number of occurrences and record the bounded transformation."""
    global body
    old = restore_latex_control_escapes(old)
    new = restore_latex_control_escapes(new)
    count = body.count(old)
    if count != expected:
        raise SystemExit(f"{change_id}: expected {expected} witness occurrences, found {count}")
    body = body.replace(old, new)
    changes.append({"id": change_id, "occurrences": expected, "reason": reason})


replace_once(
    "\\begin{center}\n\\emph{Journal f. d. reine u. angew. Math. 167 (1932), S. 147--152}\n\\end{center}\n\n",
    "\\begin{center}\n\\emph{Journal f. d. reine u. angew. Math. 167 (1932), S. 147--152}\n\\end{center}\n\n"
    "\\begin{center}\n作者：\\emph{Emmy Noether}，哥廷根。\n\\end{center}\n\n",
    "P37-HANS-AUTHOR-RESTORE",
    "Restore the omitted centered source author/affiliation and its emphasis scope.",
)

replace_once(
    "因此“导子”除了 \\(1\\) 以外成为\n"
    "\\[\n"
    "2\\sqrt[5]{2}/\\sqrt[5]{2^4},\\quad\n"
    "\\sqrt[5]{2^2}/\\sqrt[5]{2^3},\\quad\n"
    "\\sqrt[5]{2^3}/\\sqrt[5]{2^2},\\quad\n"
    "\\sqrt[5]{2^4}/(2\\sqrt[5]{2}),\n"
    "\\]\n"
    "也就是 \\(4,2,2,4\\)；",
    "因此“导子”除了 \\(1\\) 以外成为："
    "\\(2\\sqrt[5]{2}\\cdot\\sqrt[5]{2^4};\\;"
    "\\sqrt[5]{2^2}\\cdot\\sqrt[5]{2^3};\\;"
    "\\sqrt[5]{2^3}\\cdot\\sqrt[5]{2^2};\\;"
    "\\sqrt[5]{2^4}\\cdot 2\\sqrt[5]{2}\\)，"
    "也就是 \\(4,2,2,4\\)；",
    "P37-HANS-DEURING-PRODUCTS",
    "Restore four source multiplications in place of inherited quotients and restore the source inline topology.",
)

replace_once(
    r"令 \(\frakO\) 以及 \(\frako_\frakp\) 分别表示",
    r"令 \(\frako\) 以及 \(\frako_\frakp\) 分别表示",
    "P37-HANS-ORDER-CASE",
    "Restore the lower-case main order of k; capital O denotes the order of K.",
)

replace_once(
    r"E^{(1)}=\frac1n\sum_{S\in\Gg} S,",
    r"E^{(1)}=\frac1n\sum S,",
    "P37-HANS-GROUP-SUM",
    "Revert an undocumented formula expansion and retain the unindexed sealed-source sum.",
)

replace_once(
    "这个断言本身借助算子同构，归结为对 \\((\\Gg)_k\\) 或 \\((\\Gg)_Z\\) 的相应断言；在那里不可约理想产生表示。",
    "这个断言本身借助算子同构，归结为对 \\((\\Gg)_k\\) 或 \\((\\Gg)_Z\\) 的相应断言；在那里，相对于 \\((\\Gg)_k\\) 或 \\((\\Gg)_Z\\) 的不可约理想产生表示。",
    "P37-HANS-AMBIENT-RINGS",
    "Restore the source's repeated ambient-ring parenthetical rather than compressing it away.",
)

replace_once(
    r"如果 \(v_1,\ldots,v_l\) 是这样一个伽罗瓦模的基",
    r"如果 \(v_1,\ldots,v_t\) 是这样一个伽罗瓦模的基",
    "P37-HANS-BASIS-INDEX",
    "Restore the source basis-length symbol t; l is not in scope at this locus.",
)

count_field = body.count(r"(K_\frakp)_\mathfrak P")
if count_field != 3:
    raise SystemExit(f"P37-HANS-COEFFICIENT-FIELD: expected three corrupt field subscripts, found {count_field}")
body = body.replace(r"(K_\frakp)_\mathfrak P", r"(K_\frakp)_P")
changes.append(
    {
        "id": "P37-HANS-COEFFICIENT-FIELD",
        "occurrences": 3,
        "reason": "Restore ordinary P as the defined extension field; the inherited fraktur-P substitutions are ill-typed.",
    }
)

replace_once(
    "对于其余共轭特征标，一般不能直接作出结论。}",
    "对于其余共轭特征标，一般不能直接作出结论（参见 2a）。}",
    "P37-HANS-CROSSREF",
    "Restore the source cross-reference [vgl. 2a)] inside the emphasized conclusion.",
)

replace_once(
    r"其中 \(\frakp_i\) 在 \(k_\varepsilon\) 中，\(\frakP_i\) 在 \(K_\varepsilon\) 中。",
    r"其中 \(\frakp\) 表示 \(k_\varepsilon\) 中的素理想，\(\frakP\) 表示 \(K_\varepsilon\) 中的素理想。",
    "P37-HANS-GENERIC-PRIMES",
    "Restore the source's generic unindexed prime-ideal symbols after the indexed family display.",
)

# Evidence-led Chinese terminology pass. These changes are sense-bounded to this
# article; zero hits in the local shelf are adverse evidence, not claims about
# Chinese usage in general. See the terminology/adverse-evidence ledger.
replace_once(
    r"所谓一个伽罗瓦数域 \(K/k\) 的正规基，是指 \(K\) 的主阶 \(\frakO\) 关于 \(k\) 的主阶 \(\frako\) 的一个由共轭元素组成的基。",
    r"所谓伽罗瓦数域 \(K/k\) 的正规基，是指 \(K\) 的整数环（极大阶）\(\frakO\) 作为 \(k\) 的整数环 \(\frako\) 上的模，有一组由共轭元素组成的基。",
    "P37-HANS-TERM-HAUPTORDNUNG-INTRO",
    "Translate Hauptordnung by the locally supported ring-of-integers sense rather than the unattested literal calque 主阶.",
)

replace_once(
    r"即使只限制在一个素位上，也就是说，过渡到 \(k\) 的 \(\frakp\)-进扩张 \(k_\frakp\) 以及 \(K\) 的相应扩张 \(K_\frakp\)，这一点仍然成立。",
    r"即使只限制在一个素位上，也就是说，过渡到 \(k\) 的 \(\frakp\)-进完备化 \(k_\frakp\) 以及 \(K\) 的相应标量扩张 \(K_\frakp\)，这一点仍然成立。",
    "P37-HANS-TERM-PADIC-COMPLETION-INTRO",
    "Make explicit that k_p is the p-adic completion and that K_p is the associated scalar extension, which may split.",
)

replace_once(
    "对于最后这个断言还要补充说，与 E. Artin 的一个猜想相反，过渡到他的导子",
    "对于最后这个断言还要补充说，与 E. Artin 的一个猜想相反，过渡到阿廷导子",
    "P37-HANS-TERM-ARTIN-CONDUCTOR-FIRST",
    "Use the established number-theoretic name 阿廷导子 and avoid the anaphoric literal wording.",
)

replace_count(
    "Artin 的导子",
    "阿廷导子",
    2,
    "P37-HANS-TERM-ARTIN-CONDUCTOR-REST",
    "Normalize the remaining Artinsche Führer occurrences to 阿廷导子.",
)

replace_once(
    r"把 \(\frakO/\frako\) 看作伽罗瓦模，也就是看作一个以伽罗瓦群的代换为算子域的 \(\frako\)-模时，它与用 \(\frako\) 扩展的整系数群环的一个单侧理想算子同构。",
    r"把 \(\frakO/\frako\) 看作伽罗瓦模（即带伽罗瓦群作用的模），也就是看作一个由伽罗瓦群代换作用的 \(\frako\)-模时，它作为 \([\Gg]_{\frako}\)-模，与用 \(\frako\) 作标量扩张所得整系数群环中的一个单侧理想同构。",
    "P37-HANS-TERM-GALOIS-MODULE-ACTION",
    "Define Galois module at first use and replace collision-prone operator-domain/isomorphism calques by explicit module action and module isomorphism.",
)

replace_once(
    r"这个群环在所有普通分歧素位上给出一个极大阶；而 \(\frakp\)-进半单系统的极大阶中的理想都是主理想",
    r"这个群环在所有普通分歧素位上给出一个极大阶；而 \(\frakp\)-进半单代数的极大阶中的理想都是主理想",
    "P37-HANS-TERM-SEMISIMPLE-INTRO",
    "Use the modern algebraic sense 半单代数 for halbeinfaches System.",
)

replace_once(
    "所有普通分歧素位",
    "所有温分歧素位",
    "P37-HANS-TERM-TAME-RAMIFICATION",
    "Render gewöhnliche Verzweigungsstellen by the locally attested tame-ramification term 温分歧素位, in its source contrast with higher (wild) ramification.",
)

replace_once(
    r"例如以 \(a_i\) 为基。于是 \(a=\sum a_i\) 成为原理想的基。",
    r"例如由 \(a_i\) 生成。于是 \(a=\sum a_i\) 成为原理想的生成元。",
    "P37-HANS-TERM-PRINCIPAL-IDEAL-GENERATOR",
    "Resolve historical ideal Basis in the principal-ideal proof as a generator, not a vector-space basis.",
)

replace_once(
    r"在交换系统中，只需过渡到 \(k\) 中按 \(\frakp\) 的商环，就已经有主理想性质；因此当处理阿贝尔群和阿贝尔域时，可以把定义素位的这种较弱扩张作为基础。",
    r"在交换代数中，只需过渡到 \(k\) 在 \(\frakp\) 处的局部化环，就已经有主理想性质；因此当处理阿贝尔群和阿贝尔域时，可以用这种较弱的局部化来定义该素位。",
    "P37-HANS-TERM-QUOTIENTENRING-FOOTNOTE",
    "Render historical Quotientenring nach p as localization/local ring, not an algebraic quotient ring.",
)

replace_once(
    r"\subsection*{§1. \(\frakp\)-进扩展的整系数群环}",
    r"\subsection*{§1. 经 \(\frakp\)-进标量扩张的整系数群环}",
    "P37-HANS-TERM-PADIC-SECTION",
    "Translate p-adisch erweiterter as scalar extension in the group-ring heading.",
)

replace_once(
    r"令 \(\frako\) 以及 \(\frako_\frakp\) 分别表示一个代数数域 \(k\) 及其 \(\frakp\)-进扩张 \(k_\frakp\) 的主阶，其中 \(\frakp\) 是 \(k\) 中的一个素理想。",
    r"令 \(\frako\) 以及 \(\frako_\frakp\) 分别表示代数数域 \(k\) 及其 \(\frakp\)-进完备化 \(k_\frakp\) 的整数环，其中 \(\frakp\) 是 \(k\) 中的一个素理想。",
    "P37-HANS-TERM-ORDER-COMPLETION-SECTION1",
    "Use 整数环 for Hauptordnung and 完备化 for the p-adic field at the definitional locus.",
)

replace_once(
    r"于是 \((\Gg)_k\) 和 \((\Gg)_{k_\frakp}\) 是无根基系统（半单系统），而 \([\Gg]_\frako\) 以及 \([\Gg]_{\frako_\frakp}\) 分别是 \((\Gg)_k\) 和 \((\Gg)_{k_\frakp}\) 中的阶。",
    r"于是 \((\Gg)_k\) 和 \((\Gg)_{k_\frakp}\) 是根基为零的代数（即半单代数），而 \([\Gg]_\frako\) 以及 \([\Gg]_{\frako_\frakp}\) 分别是 \((\Gg)_k\) 和 \((\Gg)_{k_\frakp}\) 中的阶。",
    "P37-HANS-TERM-RADICAL-ZERO",
    "Resolve System ohne Radikal by its algebraic meaning and retain Noether's parenthetical equivalence.",
)

replace_once(
    r"而 \(\frako_\frakp\) 已经被假定为主阶，也就是在 \(k_\frakp\) 中极大。",
    r"而 \(\frako_\frakp\) 已经被假定为整数环，也就是 \(k_\frakp\) 中的极大阶。",
    "P37-HANS-TERM-HAUPTORDNUNG-MAXIMAL",
    "State the ring-of-integers/maximal-order equivalence explicitly.",
)

replace_once(
    "与单位表示相应的直和",
    "与平凡表示相应的直和",
    "P37-HANS-TERM-TRIVIAL-REPRESENTATION-SECTION1",
    "Use the native representation-theory term 平凡表示; 单位表示 is unsupported and collision-prone.",
)

replace_once(
    r"\([\Gg]_{\frako_\frakp}\) 是一个 \(\frakp\)-进半单系统的极大阶；因此其中的理想都是主理想。",
    r"\([\Gg]_{\frako_\frakp}\) 是一个 \(\frakp\)-进半单代数的极大阶；因此其中的理想都是主理想。",
    "P37-HANS-TERM-SEMISIMPLE-THEOREM2",
    "Use 半单代数 for the finite-dimensional algebra context.",
)

replace_once(
    "那里只对单系统证明了主理想性质；但由已知推理可从中推出半单情形。",
    "那里只对单代数证明了主理想性质；但由已知推理可从中推出半单情形。",
    "P37-HANS-TERM-SIMPLE-ALGEBRA",
    "Use 单代数 for einfaches System in the Hasse algebra context.",
)

replace_once(
    r"\subsection*{§2. 伽罗瓦模、算子同构、正规基}",
    r"\subsection*{§2. 伽罗瓦模、模同构与正规基}",
    "P37-HANS-TERM-MODULE-ISOMORPHISM-HEADING",
    "Use the module-theoretic sense of Operatorisomorphie.",
)

replace_once(
    r"把 \(K/k\) 看作 \(k\)-模，也就是看作以 \(k\) 为算子域的加法阿贝尔群时，\(\Gg\) 的代换在其上产生算子自同构。",
    r"把 \(K/k\) 看作 \(k\)-模，也就是看作以 \(k\) 为标量环的加法阿贝尔群时，\(\Gg\) 的代换在其上产生模自同构。",
    "P37-HANS-TERM-SCALAR-RING-AUTOMORPHISM",
    "Replace operator-domain language with explicit scalar-ring and module-automorphism language.",
)

replace_once(
    r"\emph{作为有理伽罗瓦模，\(K/k\) 与 \((\Gg)_k\) 算子同构。}",
    r"\emph{作为 \((\Gg)_k\)-模，\(K/k\) 与 \((\Gg)_k\) 同构。}",
    "P37-HANS-TERM-MODULE-ISOMORPHISM-THEOREM3",
    "State the coefficient ring and module isomorphism explicitly.",
)

replace_once(
    r"给出一个算子同态；由于它关于 \(k\) 的秩相同，因而成为同构。",
    r"给出一个 \((\Gg)_k\)-模同态；由于两边关于 \(k\) 的秩相同，因而成为同构。",
    "P37-HANS-TERM-MODULE-HOMOMORPHISM",
    "Replace the obsolete operator-homomorphism calque by the exact module homomorphism.",
)

replace_once(
    r"\emph{作为整伽罗瓦模，\(\frakO/\frako\) 与 \((\Gg)_k\) 中一个最高秩 \(n\) 的 \([\Gg]_\frako\)-模算子同构。同样，\(\frakO_\frakp/\frako_\frakp\) 与 \((\Gg)_{k_\frakp}\) 中一个秩为 \(n\) 的 \([\Gg]_{\frako_\frakp}\)-模算子同构。}",
    r"\emph{作为 \([\Gg]_\frako\)-模，\(\frakO/\frako\) 与 \((\Gg)_k\) 中一个最高秩 \(n\) 的 \([\Gg]_\frako\)-模同构。同样，\(\frakO_\frakp/\frako_\frakp\) 作为 \([\Gg]_{\frako_\frakp}\)-模，与 \((\Gg)_{k_\frakp}\) 中一个秩为 \(n\) 的 \([\Gg]_{\frako_\frakp}\)-模同构。}",
    "P37-HANS-TERM-MODULE-ISOMORPHISM-THEOREM4",
    "Make both module categories explicit in the theorem statement.",
)

replace_once(
    r"这里 \(K_\frakp/k_\frakp\) 要看作 \(k_\frakp\) 上的超复系统。\(K_\frakp/k_\frakp\) 由 \(K/k\) 扩张系数而得；一般说来它成为带零因子的系统，而且是同构域的和，因此是半单系统。",
    r"这里 \(K_\frakp/k_\frakp\) 要看作 \(k_\frakp\) 上的有限维代数（原文“超复系统”）。它由 \(K/k\) 作标量扩张而得；一般说来会有零因子，并且是若干同构域的直和，因而是半单代数。",
    "P37-HANS-TERM-HYPERCOMPLEX-SCALAR-EXTENSION-LOCAL",
    "Gloss the historical hypercomplex-system term by finite-dimensional algebra and use 标量扩张 for coefficient extension.",
)

replace_once(
    "在阿贝尔域的情形中，按注 3 和注 5，素位也可以通过商环来定义。",
    "在阿贝尔域的情形中，按注 3 和注 5，也可以用在该素位处的局部化环来定义素位。",
    "P37-HANS-TERM-QUOTIENTENRING-THEOREM5",
    "Translate the historical local quotient-ring usage as localization at the prime.",
)

replace_once(
    r"算子同构说明，如果 \(w\) 表示与 \(W\) 对应的 \(\frakO_\frakp/\frako_\frakp\) 中元素，",
    r"上述模同构说明，如果 \(w\) 表示与 \(W\) 对应的 \(\frakO_\frakp/\frako_\frakp\) 中元素，",
    "P37-HANS-TERM-MODULE-ISOMORPHISM-THEOREM5-PROOF",
    "Use module-isomorphism language in the proof.",
)

replace_once(
    r"由定理 3 所证明的 \((\Gg)_k\) 与 \(K/k\) 的算子同构",
    r"由定理 3 所证明的 \((\Gg)_k\) 与 \(K/k\) 的模同构",
    "P37-HANS-TERM-MODULE-ISOMORPHISM-REMARK",
    "Use the module-theoretic sense in the additional remark.",
)

replace_once(
    r"这里 \(Z\) 表示包含 \(k\) 的一个分裂域，它分裂群环的相应分量；\(K_Z/Z\) 要看作 \(Z\) 上的超复系统，由 \(K/k\) 扩张系数而得。特别地，如果能够把 \(Z\) 选得与 \(K\) 关于 \(k\) 互素，也就是使 \(K_Z/Z\) 成为附属扩张（Speiser 所处理的情形），则 \(K_Z\) 仍然是域。",
    r"这里 \(Z\) 表示包含 \(k\) 的一个分裂域，它分裂群环的相应分量；\(K_Z/Z\) 要看作 \(Z\) 上的有限维代数，由 \(K/k\) 作标量扩张而得。特别地，如果可以选择 \(Z\)，使它与 \(K\) 在 \(k\) 上线性无交，也就是使 \(K_Z/Z\) 成为辅助扩张（原文 akzessorische Erweiterung；Speiser 所处理的情形），则 \(K_Z\) 仍然是域。",
    "P37-HANS-TERM-LINEAR-DISJOINT-ACCESSORY",
    "Replace the misleading coprime wording by linear disjointness and retain the historical extension label with its German form.",
)

replace_once(
    r"这个断言本身借助算子同构，归结为对 \((\Gg)_k\) 或 \((\Gg)_Z\) 的相应断言；",
    r"这个断言本身借助模同构，归结为对 \((\Gg)_k\) 或 \((\Gg)_Z\) 的相应断言；",
    "P37-HANS-TERM-MODULE-ISOMORPHISM-SPEISER",
    "Use module-isomorphism language at the Speiser reduction.",
)

replace_once(
    r"一般说来，\(D_\lambda\) 位于由 \(K_\frakp/k_\frakp\) 通过把系数域 \(k_\frakp\) 用相应特征标扩张而得的超复系统中；并且它们是这个系统的\emph{整}量。",
    r"一般说来，\(D_\lambda\) 位于由 \(K_\frakp/k_\frakp\) 把系数域 \(k_\frakp\) 按相应特征标作标量扩张所得的有限维代数中；并且它们是这个代数中的\emph{整元素}。",
    "P37-HANS-TERM-INTEGRAL-ELEMENTS-HYPERCOMPLEX",
    "Use finite-dimensional algebra, scalar extension, and the supported integral-element term instead of literal historical calques.",
)

replace_once(
    "由于这里是一个域的超复系数扩张，通常伽罗瓦理论中的推理必须作修改。",
    "由于这里是在有限维代数意义下对一个域作标量扩张，通常伽罗瓦理论中的推理必须作修改。",
    "P37-HANS-TERM-HYPERCOMPLEX-FOOTNOTE",
    "Resolve hyperkomplexe Koeffizientenerweiterung as scalar extension in the finite-dimensional-algebra sense.",
)

replace_once(
    "子群的单位表示对应于相应子域的判别式。",
    "子群的平凡表示对应于相应子域的判别式。",
    "P37-HANS-TERM-TRIVIAL-REPRESENTATION-SUBGROUP",
    "Use 平凡表示 in the subgroup representation statement.",
)

replace_once(
    r"则对于非单位表示，由 \(\Delta_\lambda\) 生成的理想彼此相等",
    r"则对于非平凡表示，由 \(\Delta_\lambda\) 生成的理想彼此相等",
    "P37-HANS-TERM-NONTRIVIAL-REPRESENTATION",
    "Use 非平凡表示 for Nicht-Einsdarstellungen.",
)

replace_once(
    "而此处的素位可按注 7 简单地通过商环定义，所以不再需要引用《数论报告》中所用的事实，即绝对循环域是圆分域。",
    "而此处的素位可按注 7 直接用局部化环定义，所以不再需要引用《数论报告》中所用的事实，即绝对循环域是分圆域。",
    "P37-HANS-TERM-LOCALIZATION-CYCLOTOMIC",
    "Use 局部化环 for Quotientenring and the locally attested term 分圆域.",
)

replace_once(
    r"\(K_\varepsilon\) 仍然是域，因为 \(k_\varepsilon\) 与 \(K\) 互素，并且按注 7 这里不需要 \(\frakp\)-进扩张",
    r"\(K_\varepsilon\) 仍然是域，因为 \(k_\varepsilon\) 与 \(K\) 在 \(k\) 上线性无交，并且按注 7 这里不需要 \(\frakp\)-进完备化",
    "P37-HANS-TERM-LINEAR-DISJOINT-CYCLOTOMIC",
    "Use linear disjointness and p-adic completion in the final local argument.",
)

replace_once(
    "按不可约特征标分解群行列式，会得到广义根数；",
    "按不可约特征标分解群行列式，会得到广义拉格朗日预解因子（原文称 Wurzelzahlen）；",
    "P37-HANS-TERM-WURZELZAHLEN-FIRST",
    "Use a formula-led resolvent-factor gloss; local 根数 evidence means root count and is directly adverse here.",
)

replace_once(
    "借助根数的理想论分解，我能够把这些新因子与 阿廷导子等同起来。",
    "借助这些预解因子的理想论分解，我能够把这些新因子与阿廷导子等同起来。",
    "P37-HANS-TERM-WURZELZAHLEN-IDEAL-ARTIN",
    "Carry the resolvent-factor term through the ideal decomposition and remove a witness-derived spacing artifact before 阿廷导子.",
)

replace_once(
    "仍然总可以分裂为广义根数；",
    "仍然总可以分解为广义拉格朗日预解因子；",
    "P37-HANS-TERM-WURZELZAHLEN-COMPOSITION",
    "Use the formula-led resolvent-factor term in the composition-series claim.",
)

replace_once(
    "群行列式分解为广义根数；",
    "群行列式分解为广义拉格朗日预解因子；",
    "P37-HANS-TERM-WURZELZAHLEN-THEOREM6",
    "Replace the root-count collision in Theorem 6.",
)

replace_once(
    "分解为根数由 Speiser 前引文献中的推理得到。",
    "分解为预解因子由 Speiser 前引文献中的推理得到。",
    "P37-HANS-TERM-WURZELZAHLEN-DECOMPOSITION",
    "Use the bounded short form after the first Wurzelzahlen gloss.",
)

replace_once(
    r"这就把 \(D_\lambda\) 识别为广义根数；",
    r"这就把 \(D_\lambda\) 识别为广义拉格朗日预解因子；",
    "P37-HANS-TERM-WURZELZAHLEN-IDENTIFICATION",
    "The determinant formula identifies D_lambda as a generalized Lagrange resolvent factor, not a root count.",
)

replace_once(
    r"即 \(\Gg\) 模其换位子群的因子群的不可约表示",
    r"即 \(\Gg\) 模其导出子群所得的商群（交换化）的不可约表示",
    "P37-HANS-TERM-ABELIANIZATION",
    "Use locally supported derived-subgroup, quotient-group, and abelianization vocabulary.",
)

replace_once(
    r"\(D_\lambda\) 简化为 Lagrange 根数 \(\sum w^S\chi_\lambda(S)\)。",
    r"\(D_\lambda\) 简化为拉格朗日预解和 \(\sum w^S\chi_\lambda(S)\)。",
    "P37-HANS-TERM-LAGRANGE-RESOLVENT",
    "Name the displayed cyclic sum as a Lagrange resolvent sum.",
)

replace_once(
    r"为了从群行列式的分解过渡到判别式的分解，需要把每个表示同它的伴随表示合并。若 \(\lambda,\bar\lambda\) 表示伴随表示，则同时有",
    r"为了从群行列式的分解过渡到判别式的分解，需要把每个表示同其复共轭表示（在此等价于对偶表示）配对。若 \(\lambda,\bar\lambda\) 是这样一对表示，则同时有",
    "P37-HANS-TERM-CONJUGATE-CONTRAGREDIENT",
    "Avoid the adjoint-representation trap: the source pairs complex-conjugate/contragredient finite-group representations with determinant characters epsilon and epsilon inverse.",
)

replace_count(
    "共轭复特征标",
    "复共轭特征标",
    2,
    "P37-HANS-TERM-COMPLEX-CONJUGATE-CHARACTERS",
    "Use unambiguous modifier order for konjugiert-komplexe Charaktere.",
)

replace_once(
    "这由已知的根数分解推出。",
    "这由已知的拉格朗日预解因子分解推出。",
    "P37-HANS-TERM-WURZELZAHLEN-THEOREM7-PROOF",
    "Retain the formula-led resolvent-factor sense in the cyclic case.",
)

replace_once(
    "进一步，对于根数有",
    "进一步，对于预解因子有",
    "P37-HANS-TERM-WURZELZAHLEN-IDEALS",
    "Use the established short form at the Omega ideal factorization.",
)

replace_once(
    r"这里，根数 \(\Omega_\lambda\) 与群行列式的因子 \(D_\lambda\) 相同；",
    r"这里，预解因子 \(\Omega_\lambda\) 与群行列式的因子 \(D_\lambda\) 相同；",
    "P37-HANS-TERM-WURZELZAHLEN-OMEGA",
    "Identify Omega_lambda as a resolvent factor rather than a number of roots.",
)

replace_once(
    "它们就与 阿廷导子一致。",
    "它们就与阿廷导子一致。",
    "P37-HANS-TERM-ARTIN-CONDUCTOR-SPACING",
    "Remove the inherited pre-name spacing exposed by normalization.",
)

# Microsoft YaHei has no native italic face. Preserve every source-emphasis scope
# while mapping Chinese source emphasis to bold; keep the Latin citation/author italic.
emphasis_count = body.count(r"\emph{")
if emphasis_count != 15:
    raise SystemExit(f"P37-HANS-EMPHASIS-MAP: expected 15 source scopes after author restoration, found {emphasis_count}")
body = body.replace(r"\emph{", r"\srcemph{")
body = body.replace(r"\srcemph{Journal", r"\emph{Journal")
body = body.replace(r"\srcemph{Emmy Noether}", r"\emph{Emmy Noether}")
changes.append(
    {
        "id": "P37-HANS-EMPHASIS-MAP",
        "occurrences": 15,
        "reason": "Preserve all 15 source-emphasis scopes; render Chinese scopes in bold because the selected CJK font has no native italic face, while retaining Latin citation/author italics.",
    }
)

preamble = r"""% Complete zh-Hans-CN reconciliation candidate of Noether Paper 37.
% Controlling German authority: sealed P31 cumulative TeX SHA-256
% A48CB5CD1716974B686AC1CBA681CA4B17BC72F9043B78AD2528ACA41FCF814F.
% Exact Paper 37 logical article source SHA-256:
% AF3B34ACF4FF8D91850AC56C4F86447ABC61E6641FF9795BEFBFDA004788585D.
% The inherited Chinese text is translation/adverse witness material only.
\documentclass[11pt]{article}
\usepackage[a4paper,margin=2.15cm]{geometry}
\usepackage{fontspec}
\usepackage{xeCJK}
\usepackage{amsmath,amssymb}
\setmainfont{Noto Serif}
\setCJKmainfont{Microsoft YaHei}
\setCJKsansfont{Microsoft YaHei}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip=0pt plus 1pt
\setlength{\parindent}{2em}
\setlength{\parskip}{0.30em}
\setlength{\emergencystretch}{3em}
\newcommand{\frakO}{\mathfrak O}
\newcommand{\frako}{\mathfrak o}
\newcommand{\frakp}{\mathfrak p}
\newcommand{\frakC}{\mathfrak C}
\newcommand{\frakP}{\mathfrak P}
\newcommand{\Gg}{\mathfrak G}
\newcommand{\srcemph}[1]{\textbf{#1}}
\begin{document}
\setcounter{footnote}{0}
"""
postamble = "\n\\end{document}\n"
OUT.write_text(preamble + body.rstrip() + postamble, encoding="utf-8", newline="\n")

record = {
    "schema_version": "1.0.0",
    "work_id": "NOETHER-P37",
    "authority": {"path": str(SOURCE), "sha256": sha(SOURCE)},
    "witness": {"path": str(WITNESS), "sha256": sha(WITNESS)},
    "target": {"path": str(OUT), "sha256": sha(OUT)},
    "changes": changes,
    "epistemic_status": {
        "source_symbols_and_loci": "source facts",
        "hashes_and_occurrence_assertions": "computations",
        "Chinese apparatus wording": "internal editorial inference",
        "external_or_human_validation": False,
    },
    "status": "source_reconciled_evidence_led_hans_candidate; exact parity rebuild, final compile/render, and freeze still open",
}
RECORD.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(record, ensure_ascii=True, indent=2))
