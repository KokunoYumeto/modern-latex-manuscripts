from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
CHECK_ROOT = HERE.parent
WORKSPACE = HERE.parents[5]

R3 = CHECK_ROOT / "cum_r3" / "reader.tex"
P10 = CHECK_ROOT / "paper10" / "rb1" / "p10.tex"
P44 = CHECK_ROOT / "paper44" / "rb1" / "p44.tex"
ED0007 = (
    WORKSPACE
    / "03_projects"
    / "noether"
    / "07_german_canon_control"
    / "candidates"
    / "ED0007"
    / "noether.tex"
)

OUT = HERE / "reader.tex"
RECORD = HERE / "diff.json"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def require_blob(label: str, data: bytes, size: int, digest: str) -> None:
    actual = sha256(data)
    if len(data) != size or actual != digest:
        raise RuntimeError(
            f"{label} identity failure: {len(data)} bytes / {actual}; "
            f"expected {size} / {digest}"
        )


def lf(data: bytes) -> bytes:
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def main() -> None:
    if OUT.exists() or RECORD.exists():
        raise RuntimeError("refusing to overwrite an existing r4 output or diff record")

    r3 = R3.read_bytes()
    require_blob(
        "accepted cumulative r3",
        r3,
        1_811_029,
        "50B212EA04061921607E13CB7B367DEBF4AAF2449CF5614F931E74AA1B5A5338",
    )

    p10_raw = P10.read_bytes()
    require_blob(
        "P10 checker candidate",
        p10_raw,
        24_543,
        "14FA3643EE1AD24D3ED5A5EF26547CB056CFF961F0AC2F16481F875009FCFBF9",
    )
    p10 = lf(p10_raw)
    require_blob(
        "P10 normalized checker candidate",
        p10,
        24_295,
        "4C90B30A4FD3913700B2F181FED52427E501C3EFC1F274989A9A2CA26DEC9DCE",
    )

    p10_start = 446_526
    p10_old_len = 24_277
    p10_old = r3[p10_start : p10_start + p10_old_len]
    require_blob(
        "exact P10 predecessor span",
        p10_old,
        p10_old_len,
        "A8827318DE029699F34CD6172B80BDD55F39E51831E684DE398F484688503252",
    )
    after_p10 = r3[:p10_start] + p10 + r3[p10_start + p10_old_len :]

    p38_old = "主理想基数".encode("utf-8")
    p38_new = "主理想生成元".encode("utf-8")
    p38_start = 1_460_956
    if after_p10[p38_start : p38_start + len(p38_old)] != p38_old:
        raise RuntimeError("P38 exact predecessor locus is not present at the pinned offset")
    if after_p10.count(p38_old) != 1:
        raise RuntimeError("P38 predecessor text is not globally unique")
    after_p38 = (
        after_p10[:p38_start]
        + p38_new
        + after_p10[p38_start + len(p38_old) :]
    )
    require_blob(
        "P10+P38 integration intermediate",
        after_p38,
        1_811_050,
        "8EB01C42DD77C3CF80B525261DE715DCDD5C4F0C5C65EC76CD41BB98E06B036C",
    )

    ed7_raw = ED0007.read_bytes()
    require_blob(
        "German authority ED0007",
        ed7_raw,
        2_153_563,
        "746FA01AC33CBC0BCCBF1E740413E5DC3E74CE30295B7A4794943F5198F73355",
    )
    ed7_lines = lf(ed7_raw).splitlines(keepends=True)
    post44_source = b"".join(ed7_lines[21_002:23_741])
    require_blob(
        "ED0007 normalized Post44 source span",
        post44_source,
        172_342,
        "7F2AE56326328DA8DD12453C889D767683AC96EB4677CBBEF00C8FEAAB4FE3F7",
    )

    p44 = P44.read_bytes()
    require_blob(
        "checked Post44 target",
        p44,
        156_522,
        "8B94ED0C54A9C7DA1C6A8E8E02F33F4FBA3ECAB4E783CDFF289F3172AE75A76F",
    )
    if not p44.endswith(b"\\clearpage\n"):
        raise RuntimeError("checked Post44 target does not end in exactly one clearpage line")

    old_p44_start = 1_681_232
    old_p44_len = 96_875
    old_p44 = after_p38[old_p44_start : old_p44_start + old_p44_len]
    require_blob(
        "obsolete cumulative Post44 block",
        old_p44,
        old_p44_len,
        "34428DAF02BDDDB88B882F4A2918E2BA302F29BF41FF0DFF51064EF7BA183253",
    )

    header = (
        "% BEGIN checked Post44 current-authority unit\n"
        "% Authority: NOETH-DE-AUTH-v043-20260806 / ED0007; "
        "Post44 lines 21003--23741 are byte-identical to ED0006 after LF normalization.\n"
        "% Source LF SHA-256: "
        "7F2AE56326328DA8DD12453C889D767683AC96EB4677CBBEF00C8FEAAB4FE3F7\n"
        "% Checker target SHA-256: "
        "8B94ED0C54A9C7DA1C6A8E8E02F33F4FBA3ECAB4E783CDFF289F3172AE75A76F\n"
        "\\providecommand{\\tightlist}{}\n"
        "\\providecommand{\\mathscr}[1]{\\mathcal{#1}}\n"
        "\\def\\srcfn#1#2{\\begingroup\\renewcommand{\\thefootnote}{#1}"
        "\\footnote{#2}\\addtocounter{footnote}{-1}\\endgroup}\n"
        "\\addcontentsline{toc}{section}{论文 44：超复量代数（讲义）}\n"
        "\\markboth{论文 44}{超复量代数}\n"
    ).encode("utf-8")
    footer = b"% END checked Post44 current-authority unit\n"
    replacement = header + p44 + footer
    r4 = (
        after_p38[:old_p44_start]
        + replacement
        + after_p38[old_p44_start + old_p44_len :]
    )

    metadata_old = b"pdftitle={Noether Simplified Chinese cumulative rebase r1}"
    metadata_new = b"pdftitle={Noether Simplified Chinese cumulative rebase r4}"
    if r4.count(metadata_old) != 1:
        raise RuntimeError("inherited PDF title metadata is not unique")
    r4 = r4.replace(metadata_old, metadata_new, 1)

    if r4.count(b"% BEGIN checked Post44 current-authority unit") != 1:
        raise RuntimeError("checked Post44 wrapper is not unique")
    if old_p44 in r4:
        raise RuntimeError("obsolete Post44 block survived integration")

    record = {
        "record_id": "ZHCHK-NOETHER-CUM-R4-DIFF-001",
        "state": "generated_unbuilt",
        "predecessor": {
            "path": str(R3),
            "bytes": len(r3),
            "sha256": sha256(r3),
        },
        "authority": {
            "pointer_id": "NOETH-DE-AUTH-v043-20260806",
            "pointer_sha256": "D625C79008B87863D452E35FE4A4DD36D1F961967D12A37560C77897DCD94FF1",
            "default_edition": "ED0007",
            "edition_sha256": sha256(ed7_raw),
            "post44_lines_1_based_inclusive": [21_003, 23_741],
            "post44_lf_bytes": len(post44_source),
            "post44_lf_sha256": sha256(post44_source),
            "ed0006_ed0007_post44_relation": "byte-identical after LF normalization",
        },
        "changes": [
            {
                "unit": "P10",
                "kind": "terminology_correction_block_replacement",
                "predecessor_offset_0_based": p10_start,
                "predecessor_bytes": len(p10_old),
                "predecessor_sha256": sha256(p10_old),
                "replacement_bytes": len(p10),
                "replacement_sha256": sha256(p10),
                "scope": "10 occurrences algebraische Basis; 6 occurrences Basiszahl",
            },
            {
                "unit": "P38",
                "kind": "single_exact_terminology_correction",
                "offset_after_p10_0_based": p38_start,
                "from": "主理想基数",
                "to": "主理想生成元",
            },
            {
                "unit": "P44",
                "kind": "obsolete_incomplete_block_replacement",
                "offset_after_p10_p38_0_based": old_p44_start,
                "predecessor_bytes": len(old_p44),
                "predecessor_sha256": sha256(old_p44),
                "target_body_bytes": len(p44),
                "target_body_sha256": sha256(p44),
                "wrapped_replacement_bytes": len(replacement),
                "wrapped_replacement_sha256": sha256(replacement),
                "checker_confirmed_source_repairs_realized_in_target": [
                    "ZHCHK-DE-P44-001",
                    "ZHCHK-DE-P44-002",
                    "ZHCHK-DE-P44-003",
                ],
            },
            {
                "unit": "cumulative_metadata",
                "kind": "version_metadata_correction",
                "from": "Noether Simplified Chinese cumulative rebase r1",
                "to": "Noether Simplified Chinese cumulative rebase r4",
                "rendered_page_content_change_expected": False,
            },
        ],
        "intermediate_after_p10_p38": {
            "bytes": len(after_p38),
            "sha256": sha256(after_p38),
        },
        "output": {
            "path": str(OUT),
            "bytes": len(r4),
            "sha256": sha256(r4),
        },
    }

    OUT.write_bytes(r4)
    RECORD.write_text(
        json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(record["output"], ensure_ascii=False))


if __name__ == "__main__":
    main()
