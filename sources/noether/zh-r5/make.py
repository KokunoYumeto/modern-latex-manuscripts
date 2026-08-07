from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parents[5]
BASE = HERE / "base.tex"
OUT = HERE / "reader.tex"
RECORD = HERE / "diff.json"
ED8 = (
    WORKSPACE
    / "03_projects"
    / "noether"
    / "07_german_canon_control"
    / "candidates"
    / "ED0008"
    / "noether.tex"
)
POINTER = (
    WORKSPACE
    / "03_projects"
    / "noether"
    / "07_german_canon_control"
    / "CURRENT_GERMAN_AUTHORITY_POINTER.json"
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def require(label: str, data: bytes, size: int, digest: str) -> None:
    actual = sha256(data)
    if len(data) != size or actual != digest:
        raise RuntimeError(
            f"{label}: got {len(data)} / {actual}; expected {size} / {digest}"
        )


def lf(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def lines(text: str) -> list[bytes]:
    if not text.endswith("\n"):
        raise RuntimeError("replacement must end with LF")
    return [part.encode("utf-8") for part in text.splitlines(keepends=True)]


def main() -> None:
    if OUT.exists() or RECORD.exists():
        raise RuntimeError("refusing to overwrite existing r5 output or diff record")

    base = BASE.read_bytes()
    require(
        "rejected but exact r4 inherited base",
        base,
        1_871_385,
        "910399C8CB6A8A3CC0BE40638C23AFD496C642ACC63127E3AE812CACEF599E33",
    )
    base_lines = base.splitlines(keepends=True)
    if len(base_lines) != 24_991 or not all(x.endswith(b"\n") for x in base_lines):
        raise RuntimeError("unexpected r4 line structure")

    ed8_raw = ED8.read_bytes()
    require(
        "German authority ED0008",
        ed8_raw,
        2_153_575,
        "C83A94D25DE8FD27C66E2C6C50BAB04AA875E6C0A6A87BDFCA202E69A8EA660D",
    )
    pointer = POINTER.read_bytes()
    require(
        "authority pointer v044",
        pointer,
        74_915,
        "FF98F436CF8D38AA1D13CF1D969857CE277D02851CC79EFE521DFE1D0B45B98D",
    )
    ed8_lines = lf(ed8_raw).splitlines(keepends=True)
    p45_source = b"".join(ed8_lines[23_778:23_844])
    bib_source = b"".join(ed8_lines[24_097:24_128])
    post44_source = b"".join(ed8_lines[21_002:23_741])

    p45 = r"""其中有
\[
(g_1)+(g_2)+\cdots+(g_t)=\mu,
\]
这里 \(\mu\) 表示与 \(\mathfrak q\) 相应并由结式定义的交点重数。
\end{satz}

证明时，不妨假定 \(x=0,\ y=0\) 是多项式对 \((\varphi,\psi)\) 中与
\(\mathfrak q\) 相应的零点。进一步，一般约定：若 \(A(x,y)\) 是
\(x,y\) 中任一多项式\textsuperscript{7)}，则符号 \((A)\) 表示
\(y\) 作为因子在 \(A(0,y)\) 中出现的次数；若 \(A(0,y)\) 恒等为零，
则令 \((A)=\infty\)。与 \(\mathfrak q\) 相配的数
\((g_1),(g_2),\ldots,(g_t)\) 由下列方程组定义；这个方程组构成该方法的基础：

\begin{equation}\tag{1}\label{eq:kap-1}
\begin{aligned}
f_1\cdot g_1(0,y):y^{(g_1)}
 - g_1\cdot f_1(0,y):y^{(g_1)} &= x\cdot h_1,\\
f_2\cdot g_2(0,y):y^{(g_2)}
 - g_2\cdot f_2(0,y):y^{(g_2)} &= x\cdot h_2,\\
&\vdots \qquad\qquad\vdots\qquad\qquad\vdots\\
f_r\cdot g_r(0,y):y^{(g_r)}
 - g_r\cdot f_r(0,y):y^{(g_r)} &= x\cdot h_r.
\end{aligned}
\end{equation}

这个方程组完全建立在给定的多项式对 \(\varphi,\psi\) 之上；
也就是说，多项式 \(f_1,g_1\) 分别被定义为同 \(\varphi,\psi\) 恒等，
但必要时可交换两者的次序；次序须取为 \((f_1)\geq(g_1)\)。
由于这一规定，并且只有在这一规定下，\(h_1\) 才是整有理的。

多项式 \(f_2,g_2\) 分别被定义为同 \(h_1,g_1\) 恒等，并附加条件
\((f_2)\geq(g_2)\)。一般地，多项式对 \(f_r,g_r\) 分别被定义为同
\(h_{r-1},g_{r-1}\) 恒等，并附加条件 \((f_r)\geq(g_r)\)。

方程组 \eqref{eq:kap-1} 固然可以按所说明的方式无限继续下去；
但是主定理只要求形成该系统的前 \(t\) 个方程，其中 \(t\) 由以下事实确定：

\smallskip
\textbf{辅助定理 I.} 存在一个自然数 \(t\) [并且 \(t\leqq\mu\)，
这里 \(\mu\) 表示点 \(x=0,\ y=0\) 在 \(\varphi=0,\ \psi=0\)
中出现的交点重数]，使得由 \eqref{eq:kap-1} 定义的前 \(t\) 个数，
即 \((g_1),(g_2),\ldots,(g_t)\)，全都大于零，而同时
\((g_{t+1})\) 以及其后所有数都等于零。

事实上，考虑结式的乘积定理，点 \(x=0,\ y=0\) 作为
\(f_r=0,\ g_r=0\) 的交点，其重数等于
\[
\mu-(g_1)-(g_2)-\cdots-(g_r),
\]
由此推出至多经过 \(\mu\) 步即会中止。同时得到事实：
\begin{equation}\tag{2}\label{eq:kap-2}
\mu=(g_1)+(g_2)+\cdots+(g_t),
\end{equation}
这个公式之所以值得注意，是因为只要有关零点已知，它就在完全一般的情形下
给出一种有理且实践上易于执行的确定交点重数的方法。

既知数 \((g_i)\) 之后，数 \((K_i)\) 由下列与
\eqref{eq:kap-1} 相对应的方程组确定：
\begin{equation}\tag{3}\label{eq:kap-3}
\begin{aligned}
K_1\cdot g_1(0,y):y^{(g_1)}
 - g_1\cdot K_1(0,y):y^{(g_1)} &= x\cdot K_1,\\
K_2\cdot g_2(0,y):y^{(g_2)}
 - g_2\cdot K_2(0,y):y^{(g_2)} &= x\cdot K_2,\\
&\vdots \qquad\qquad\vdots\qquad\qquad\vdots\\
K_r\cdot g_r(0,y):y^{(g_r)}
 - g_r\cdot K_r(0,y):y^{(g_r)} &= x\cdot K_{r+1}.
\end{aligned}
\end{equation}

\(K_1\) 被定义为同 \(K\) 恒等。显然，\(K_2\) 当且仅当
\((K_1)\geq(g_1)\) 时才是整有理的。若后一条件成立，则进一步有：
\(K_3\) 当且仅当 \((K_2)\geq(g_2)\) 时才是整有理的。
一般地，若 \(K_r\) 已经是整有理的，则 \(K_{r+1}\) 当且仅当
\((K_r)\geq(g_r)\) 时才是整有理的。

主定理（定理 II）的证明现在依赖于下面的另一个辅助定理：

\smallskip
\textbf{辅助定理 II.} 若令
\((f_i,g_i,\mathfrak p^e)=\mathfrak q^{(i)}\)，
则对于整数列 \(1,2,\ldots\) 中的每个 \(i\)，
\textit{in inf.} 有下述命题：

同余式
\[
K_i\equiv0(\mathfrak q^{(i)})
\]
成立的必要且充分条件，是同时满足下列两个条件：
\[
(K_i)\geq(g_i)
\qquad \text{以及} \qquad
K_{i+1}\equiv0(\mathfrak q^{(i+1)}).
\]

辅助定理的证明\textsuperscript{8)}由组合方程组
\eqref{eq:kap-1} 与 \eqref{eq:kap-3} 得到。注意到按辅助定理 I，
\(g_{t+1}\) 在零点处不再消失，也就是说，模
\(\mathfrak q^{(t+1)}\) 由全体多项式组成（即为单位理想），
因而 \(K_{t+1}\equiv0(\mathfrak q^{(t+1)})\) 成为平凡命题；
于是把辅助定理 II 应用 \(t\) 次，便得到主定理的证明。
"""

    edits = [
        {
            "id": "ZH-R26-PROV-001/header",
            "start": 1,
            "end": 1,
            "text": r"""\documentclass[11pt]{article}
% Static successor: ZH-CUM-R5; producer state FROZEN_PENDING_INDEPENDENT_REVIEW.
% Inherited base: cum_r4/reader.tex, 1871385 bytes, SHA-256 910399C8CB6A8A3CC0BE40638C23AFD496C642ACC63127E3AE812CACEF599E33.
% Authority: NOETH-DE-AUTH-v044-20260807 / ED0008, pointer SHA-256 FF98F436CF8D38AA1D13CF1D969857CE277D02851CC79EFE521DFE1D0B45B98D, edition SHA-256 C83A94D25DE8FD27C66E2C6C50BAB04AA875E6C0A6A87BDFCA202E69A8EA660D.
% Rejected predecessor: ZHCHK-NOETHER-CUM-R4-RETURN-001; its prior acceptance claim is not inherited. Clean-day count: 0; publishable: false.
% Applied findings: ZH-R26-P45-001, ZH-R26-BIB-001, ZH-R26-P06-FN-001, ZH-R26-P13-FN-001, ZH-R26-P13-FN-002, ZH-R26-P38-FN-001, ZH-R26-PROV-001.
""",
        },
        {
            "id": "ZH-R26-PROV-001/pdf-title",
            "start": 20,
            "end": 20,
            "text": "\\hypersetup{unicode=true,hidelinks,pdfauthor={Emmy Noether},pdftitle={Noether Simplified Chinese cumulative rebase r5}}\n",
        },
        {
            "id": "ZH-R26-P06-FN-001",
            "start": 6066,
            "end": 6069,
            "text": r"""\begin{equation}
  R_0=a_0\ne0\footnotemark.
\tag{3}
\end{equation}
\footnotetext{Mertens，前引处，\S\ 5。}
""",
        },
        {
            "id": "ZH-R26-P13-FN-001",
            "start": 8809,
            "end": 8809,
            "text": "的不变性；因而得到 \\(\\sum_i\\psi_i\\delta u_i\\) 的相对不变性\\footnote{即 \\(\\sum_i\\psi_i\\delta u_i\\) 在变换下获得一个因子；在代数不变量论中，这一情形一向称为相对不变性。}，其中 \\(\\delta\\) 表示任意变分。确实，一方面\n",
        },
        {
            "id": "ZH-R26-P13-FN-002",
            "start": 8998,
            "end": 9000,
            "text": r"""\D u_i=p'(x)\footnotemark,\qquad
\bd u_i=p'(x)-u_i'p(x).
\]
\footnotetext{由这些无穷小变换，按照 \S{} 4 末尾所述的方法反向求出有限变换。}
""",
        },
        {
            "id": "ZH-R26-P38-FN-001",
            "start": 19448,
            "end": 19448,
            "text": "最后还要说明，主定理对 I. Schur\\footnote{I. Schur, \\emph{Arithmetische Untersuchungen über endliche Gruppen linearer Substitutionen}, Berl. Akad.-Ber. 1906。} 所研究的问题有实质推进；该问题是：一个有限群的绝对不可约表示可在哪些数域中实现。\n",
        },
        {
            "id": "ZH-R26-PROV-001/post44",
            "start": 21636,
            "end": 21638,
            "text": r"""% Authority: NOETH-DE-AUTH-v044-20260807 / NOETH-DE-ED-0008; immutable pointer 74915 bytes, SHA-256 FF98F436CF8D38AA1D13CF1D969857CE277D02851CC79EFE521DFE1D0B45B98D; edition 2153575 bytes, SHA-256 C83A94D25DE8FD27C66E2C6C50BAB04AA875E6C0A6A87BDFCA202E69A8EA660D.
% ED0008 Post44 LF-normalized source lines 21003--23741 inclusive: 172354 bytes, SHA-256 74F9A1A060E69E1CA845DFE6A5E487150DE0916D29422BB04116FA02DAF0EDB8.
% Inherited r4 Post44 target body: 156522 bytes, SHA-256 8B94ED0C54A9C7DA1C6A8E8E02F33F4FBA3ECAB4E783CDFF289F3172AE75A76F; ED0008 loci 21425, 21454, 21639--21640 were already realized at r4 target loci 22069, 22098, 22283--22284; ED0007->ED0008 adds no target-wording delta.
""",
        },
        {
            "id": "ZH-R26-PROV-001/post45",
            "start": 24377,
            "end": 24380,
            "text": r"""% Source-fidelity r5 repair: inherited Post45 unit with the independently required central-span replacement.
% Authority: NOETH-DE-AUTH-v044-20260807 / ED0008; exact repaired source lines 23779--23844.
% Primary witness: Math. Ann. 97 (1927), printed pp. 561--563; equation (3) preserved diplomatically.
% Boundary: PRC-oriented Chinese mathematical register; no interlanguage substitution and no whole-article recertification claim.
""",
        },
        {
            "id": "ZH-R26-P45-001",
            "start": 24466,
            "end": 24536,
            "text": p45,
        },
        {
            "id": "ZH-R26-BIB-001/1",
            "start": 24926,
            "end": 24926,
            "text": "\\item 不变变分问题，27, Teil II, (1918), S.~47\n",
        },
        {
            "id": "ZH-R26-BIB-001/2",
            "start": 24927,
            "end": 24927,
            "text": "\\item 整系数二元不变式的有限性，28, Teil II, (1919), S.~29\n",
        },
        {
            "id": "ZH-R26-BIB-001/3",
            "start": 24932,
            "end": 24932,
            "text": "\\item 一般理想论中 Hilbert 定理的一个类似物，32, Teil II, (1923), S.~20--21\n",
        },
        {
            "id": "ZH-R26-BIB-001/4",
            "start": 24933,
            "end": 24933,
            "text": "\\item 关于公理化问题的群论备注，33, Teil II, (1925), S.~21\n",
        },
        {
            "id": "ZH-R26-BIB-001/5",
            "start": 24936,
            "end": 24936,
            "text": "\\item 理想的微分商与分歧理论，38, Teil II, (1929), S.~81\n",
        },
        {
            "id": "ZH-R26-BIB-001/6",
            "start": 24949,
            "end": 24949,
            "text": "40, Teil II, (1931), S.~11--12\n",
        },
        {
            "id": "ZH-R26-BIB-001/7",
            "start": 24953,
            "end": 24953,
            "text": "41, Teil II, (1932), S.~17\n",
        },
        {
            "id": "ZH-R26-BIB-001/8",
            "start": 24957,
            "end": 24957,
            "text": "42, Teil II, (1933), S.~38--39\n",
        },
    ]

    edits.sort(key=lambda item: (item["start"], item["end"]))
    cursor = 1
    output_lines: list[bytes] = []
    change_records = []
    for edit in edits:
        start = edit["start"]
        end = edit["end"]
        if start < cursor or end < start or end > len(base_lines):
            raise RuntimeError(f"overlapping or unsafe edit: {edit}")
        output_lines.extend(base_lines[cursor - 1 : start - 1])
        before = b"".join(base_lines[start - 1 : end])
        replacement_lines = lines(edit["text"])
        replacement = b"".join(replacement_lines)
        final_start = len(output_lines) + 1
        output_lines.extend(replacement_lines)
        final_end = len(output_lines)
        change_records.append(
            {
                "id": edit["id"],
                "base_lines_1_based_inclusive": [start, end],
                "final_lines_1_based_inclusive": [final_start, final_end],
                "before_bytes": len(before),
                "before_sha256": sha256(before),
                "after_bytes": len(replacement),
                "after_sha256": sha256(replacement),
            }
        )
        cursor = end + 1
    output_lines.extend(base_lines[cursor - 1 :])
    output = b"".join(output_lines)

    forbidden = [
        "t \\leq \\mu,\n\\]".encode("utf-8"),
        b"f_{t-1} &= g_{t}",
        b"L_{1}",
        b"K_0",
        b"\\mathfrak p^{2^i}",
        b"K \\cdot f_{\\nu}",
        "应用 \\(\\mu\\) 次".encode("utf-8"),
    ]
    p45_blob = p45.encode("utf-8")
    surviving = [item.decode("utf-8") for item in forbidden if item in p45_blob]
    if surviving:
        raise RuntimeError(f"rejected P45 residue survived: {surviving}")

    required = [
        b"(g_1)+(g_2)+\\cdots+(g_t)=\\mu",
        b"f_1\\cdot g_1(0,y):y^{(g_1)}",
        b"\\mu-(g_1)-(g_2)-\\cdots-(g_r)",
        b"K_1\\cdot g_1(0,y):y^{(g_1)}",
        b"(f_i,g_i,\\mathfrak p^e)=\\mathfrak q^{(i)}",
        b"K_i\\equiv0(\\mathfrak q^{(i)})",
        "应用 \\(t\\) 次".encode("utf-8"),
    ]
    missing = [item.decode("utf-8") for item in required if item not in p45_blob]
    if missing:
        raise RuntimeError(f"required P45 reading absent: {missing}")

    record = {
        "id": "ZHCHK-NOETHER-CUM-R5-DIFF-001",
        "state": "generated_unbuilt_pending_independent_review",
        "authority": {
            "pointer_id": "NOETH-DE-AUTH-v044-20260807",
            "pointer_bytes": len(pointer),
            "pointer_sha256": sha256(pointer),
            "edition_id": "ED0008",
            "edition_bytes": len(ed8_raw),
            "edition_sha256": sha256(ed8_raw),
            "p45_source_lines": [23_779, 23_844],
            "p45_source_bytes": len(p45_source),
            "p45_source_sha256": sha256(p45_source),
            "p45_primary_pages": [561, 562, 563],
            "p45_equation_3_original_print_suspicion": "first two RHS subscripts print and ED0008 read K_1,K_2; following prose suggests K_2,K_3; target preserves authority diplomatically",
            "bibliography_source_lines": [24_098, 24_128],
            "bibliography_source_bytes": len(bib_source),
            "bibliography_source_sha256": sha256(bib_source),
            "post44_source_lines": [21_003, 23_741],
            "post44_source_bytes": len(post44_source),
            "post44_source_sha256": sha256(post44_source),
        },
        "inherited_base": {
            "path": str(BASE),
            "bytes": len(base),
            "sha256": sha256(base),
            "lines": len(base_lines),
            "return_id": "ZHCHK-NOETHER-CUM-R4-RETURN-001",
            "return_disposition_superseded_by": "RETURN_REQUIRED",
            "old_acceptance_claim_inherited": False,
        },
        "independent_return": {
            "csv_sha256": "706ABC522E9CF2A209B9C783937A8569397636718F575CE3BF988CF1A64B9D5D",
            "report_sha256": "7301C588500794C222EBFF0ACEADBF4BF7FD0E701A02CBDC7C518C9679236501",
            "clean_day_count": 0,
        },
        "changes": change_records,
        "output": {
            "path": str(OUT),
            "bytes": len(output),
            "sha256": sha256(output),
            "lines": len(output_lines),
        },
        "acceptance_claim": False,
        "producer_state": "FROZEN_PENDING_INDEPENDENT_REVIEW_AFTER_BUILD_AND_SEAL",
        "sga": "held and untouched",
    }
    OUT.write_bytes(output)
    RECORD.write_text(
        json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(record["output"], ensure_ascii=False))


if __name__ == "__main__":
    main()
