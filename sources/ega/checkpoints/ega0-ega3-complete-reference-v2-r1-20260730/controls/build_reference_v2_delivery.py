#!/usr/bin/env python3
"""Build and validate the complete EGA 0/EGA III reference-v2 delivery.

The source-candidate universe consists of every explicit visible reference
command plus every remaining plain dotted/section/chapter locator outside
structural declarations.  It is partitioned exactly into compiled local
applications and reviewed positive residuals.  The PDF edge universe is the
complete delivered GoTo graph and is deliberately separate from that source
partition.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

from pypdf import PdfReader


UNSAFE_PREFIXES = ("=", "+", "-", "@")
STRUCTURAL_ENVS = (
    "env|proposition|theorem|lemma|corollary|remark|remarks|definition|"
    "notation|example|examples|proposition-definition|scholium"
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def file_sha(path: Path) -> str:
    return digest(path.read_bytes())


def safe(value: object) -> str:
    text = "" if value is None else str(value)
    return "'" + text if text.startswith(UNSAFE_PREFIXES) else text


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: safe(row.get(field, "")) for field in fields})


def active_closure(source: Path, master: str) -> list[str]:
    queue: deque[str] = deque([master])
    seen: list[str] = []
    while queue:
        relpath = queue.popleft().replace("\\", "/")
        path = source / relpath
        if not path.suffix:
            relpath += ".tex"
            path = source / relpath
        if relpath in seen:
            continue
        if not path.is_file():
            raise FileNotFoundError(path)
        seen.append(relpath)
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r"\\(?:input|include)\{([^}]+)\}", text):
            queue.append(match.group(1))
    if "the.bib" not in seen:
        seen.append("the.bib")
    return seen


def mask_comments(text: str) -> str:
    chars = list(text)
    i = 0
    while i < len(chars):
        if chars[i] == "%" and (i == 0 or chars[i - 1] != "\\"):
            j = i
            while j < len(chars) and chars[j] not in "\r\n":
                chars[j] = " "
                j += 1
            i = j
        else:
            i += 1
    return "".join(chars)


def balanced_end(text: str, start: int, opener: str, closer: str) -> int:
    if start >= len(text) or text[start] != opener:
        raise ValueError(f"expected {opener!r} at {start}")
    depth = 0
    i = start
    while i < len(text):
        if text[i] == "\\":
            i += 2
            continue
        if text[i] == opener:
            depth += 1
        elif text[i] == closer:
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError(f"unclosed {opener!r} group")


def group_content(text: str, start: int, opener: str = "{", closer: str = "}") -> tuple[str, int]:
    end = balanced_end(text, start, opener, closer)
    return text[start + 1 : end - 1], end


def line_col(text: str, offset: int) -> tuple[int, int]:
    line = text.count("\n", 0, offset) + 1
    last = text.rfind("\n", 0, offset)
    return line, offset - last


def line_context(text: str, offset: int) -> str:
    start = text.rfind("\n", 0, offset) + 1
    end = text.find("\n", offset)
    if end < 0:
        end = len(text)
    return " ".join(text[start:end].strip().split())


def parse_newlabels(aux_path: Path) -> dict[str, dict[str, str]]:
    labels: dict[str, dict[str, str]] = {}
    for line in aux_path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("\\newlabel{"):
            continue
        first = line.find("{")
        key, pos = group_content(line, first)
        while pos < len(line) and line[pos].isspace():
            pos += 1
        payload, _ = group_content(line, pos)
        fields: list[str] = []
        p = 0
        while p < len(payload):
            while p < len(payload) and payload[p].isspace():
                p += 1
            if p >= len(payload) or payload[p] != "{":
                break
            value, p = group_content(payload, p)
            fields.append(value)
        if len(fields) >= 4:
            labels[key] = {
                "printed_value": fields[0],
                "printed_page": fields[1],
                "title": fields[2],
                "pdf_destination": fields[3],
            }
    return labels


def source_label_positions(source: Path, closure: list[str]) -> tuple[dict[str, dict[str, object]], list[str]]:
    result: dict[str, dict[str, object]] = {}
    errors: list[str] = []
    for relpath in closure:
        if not relpath.endswith(".tex"):
            continue
        path = source / relpath
        original = path.read_text(encoding="utf-8")
        text = mask_comments(original)
        for match in re.finditer(r"\\label\{([^}]+)\}", text):
            label = match.group(1)
            line, column = line_col(original, match.start())
            row = {
                "source_relpath": relpath,
                "source_line": line,
                "source_column": column,
                "source_sha256": file_sha(path),
            }
            if label in result:
                errors.append(f"duplicate active source label {label}")
            else:
                result[label] = row
    return result, errors


def candidate_id(reader: str, relpath: str, line: int, column: int, form: str, raw: str, discriminator: str) -> str:
    material = "\0".join((reader, relpath, str(line), str(column), form, raw, discriminator))
    return f"ega3.{reader}.candidate.sha256." + hashlib.sha256(material.encode()).hexdigest()


def target_id(reader: str, destination: str) -> str:
    material = f"{reader}\0{destination}".encode()
    return f"ega3.{reader}.target.sha256." + hashlib.sha256(material).hexdigest()


def target_lookup(label: str, aliases: dict[str, str], named: dict[str, object]) -> tuple[str, str]:
    if label in aliases:
        destination = aliases[label]
        return destination, target_id("PLACEHOLDER", destination)
    if label in named:
        return label, target_id("PLACEHOLDER", label)
    return "", ""


def external_context(context: str) -> bool:
    return bool(
        re.search(
            r"(?:\bBourbaki\b|\bFAC\b|\\(?:emph|textnormal|textbf)\{?[GMT]\}?|"
            r"\(\s*[GMT]\s*,|\bG\s*,\s*(?:I|II)|\bT\s*,|\bM\s*,|"
            r"\\textbf\{(?:0|I|II|IV)\}|0\\textsubscript\{I\}|Alg\\?\.|"
            r"Chapter~?(?:I|II|III|IV)\b)",
            context,
        )
    )


def structural_context(context: str) -> bool:
    return bool(
        re.search(r"\\emph\{(?:Remark|Remarks|Scholium)", context)
        or re.search(r"^\\textsection\d+\.?\s*&", context)
    )


def extract_candidates(
    *, reader: str, prefix: str, source: Path, closure: list[str],
    aux_labels: dict[str, dict[str, str]], named: dict[str, object],
    target_by_destination: dict[str, str],
) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[str]]:
    candidates: list[dict[str, object]] = []
    applications: list[dict[str, object]] = []
    residuals: list[dict[str, object]] = []
    errors: list[str] = []
    seen: set[str] = set()

    candidate_fields = {
        "reader": reader,
        "status": "",
        "classification": "",
        "resolution_basis": "",
        "target_label": "",
        "target_id": "",
        "pdf_destination": "",
    }

    def add(
        *, relpath: str, original: str, offset: int, form: str, raw: str,
        visible: str, discriminator: str, target_label_value: str = "",
        classification: str, status: str, basis: str,
        pdf_destination: str = "",
    ) -> str:
        line, column = line_col(original, offset)
        cid = candidate_id(reader, relpath, line, column, form, raw, discriminator)
        if cid in seen:
            errors.append(f"duplicate candidate ID {cid}")
        seen.add(cid)
        tid = target_by_destination.get(pdf_destination, "")
        row = {
            **candidate_fields,
            "candidate_id": cid,
            "reference_form": form,
            "source_relpath": relpath,
            "source_line": line,
            "source_column": column,
            "visible_text": visible,
            "raw_tex": raw,
            "context": line_context(original, offset),
            "source_sha256": file_sha(source / relpath),
            "target_label": target_label_value,
            "pdf_destination": pdf_destination,
            "target_id": tid,
            "classification": classification,
            "status": status,
            "resolution_basis": basis,
        }
        candidates.append(row)
        if status == "applied_local_link":
            applications.append(
                {
                    "application_id": cid.replace(".candidate.", ".application.", 1),
                    **row,
                }
            )
        else:
            residuals.append(
                {
                    "residual_id": cid.replace(".candidate.", ".residual.", 1),
                    **row,
                }
            )
        return cid

    for relpath in closure:
        if not relpath.endswith(".tex") or relpath == "preamble.tex":
            continue
        path = source / relpath
        original = path.read_text(encoding="utf-8")
        text = mask_comments(original)
        spans: list[tuple[int, int]] = []

        # sref: optional volume, required target label, optional subitem.
        sref_start = re.compile(r"\\sref\s*(?:\[([^]]*)\])?\s*\{")
        for match in sref_start.finditer(text):
            brace = text.find("{", match.start(), match.end() + 1)
            label, end = group_content(original, brace)
            p = end
            while p < len(original) and original[p].isspace():
                p += 1
            item = ""
            if p < len(original) and original[p] == "[":
                item, end = group_content(original, p, "[", "]")
            raw = original[match.start() : end]
            destination = aux_labels.get(label, {}).get("pdf_destination", "")
            visible = label + (f" ({item})" if item else "")
            if destination and destination in named:
                add(
                    relpath=relpath, original=original, offset=match.start(), form="sref",
                    raw=raw, visible=visible, discriminator=label + "|" + item,
                    target_label_value=label, classification="explicit_same_reader_reference",
                    status="applied_local_link", basis="exact active local aux label",
                    pdf_destination=destination,
                )
            else:
                add(
                    relpath=relpath, original=original, offset=match.start(), form="sref",
                    raw=raw, visible=visible, discriminator=label + "|" + item,
                    target_label_value=label, classification="external_or_unavailable_volume_reference",
                    status="reviewed_positive_residual",
                    basis="explicit reference target is outside this standalone reader",
                )
            spans.append((match.start(), end))

        # hyperref: explicit target and balanced visible group.
        hyper_start = re.compile(r"\\hyperref\[([^]]+)\]\s*\{")
        for match in hyper_start.finditer(text):
            label = match.group(1)
            brace = text.find("{", match.start(), match.end() + 1)
            visible, end = group_content(original, brace)
            raw = original[match.start() : end]
            destination = aux_labels.get(label, {}).get("pdf_destination", label if label in named else "")
            if not destination or destination not in named:
                errors.append(f"unresolved active hyperref {reader}:{relpath}:{label}")
                status = "reviewed_positive_residual"
                classification = "unresolved_explicit_hyperref"
                basis = "active hyperref has no delivered named destination"
            else:
                status = "applied_local_link"
                classification = "explicit_same_reader_reference"
                basis = "exact active local aux label or named destination"
            add(
                relpath=relpath, original=original, offset=match.start(), form="hyperref",
                raw=raw, visible=visible, discriminator=label, target_label_value=label,
                classification=classification, status=status, basis=basis,
                pdf_destination=destination if status == "applied_local_link" else "",
            )
            spans.append((match.start(), end))

        for form in ("eref", "ref", "eqref", "pageref"):
            regex = re.compile(rf"\\{form}\{{([^}}]+)\}}")
            for match in regex.finditer(text):
                label = match.group(1)
                raw = original[match.start() : match.end()]
                destination = aux_labels.get(label, {}).get("pdf_destination", "")
                if destination and destination in named:
                    status = "applied_local_link"
                    classification = "explicit_same_reader_reference"
                    basis = "exact active local aux label"
                else:
                    status = "reviewed_positive_residual"
                    classification = "external_or_unavailable_volume_reference"
                    basis = "explicit reference target is outside this standalone reader"
                add(
                    relpath=relpath, original=original, offset=match.start(), form=form,
                    raw=raw, visible=label, discriminator=label,
                    target_label_value=label, classification=classification,
                    status=status, basis=basis,
                    pdf_destination=destination if status == "applied_local_link" else "",
                )
                spans.append((match.start(), match.end()))

        cite_regex = re.compile(r"\\cite(?:\[[^]]*\])?\{([^}]+)\}")
        for match in cite_regex.finditer(text):
            raw = original[match.start() : match.end()]
            for index, key in enumerate(item.strip() for item in match.group(1).split(",")):
                destination = f"cite.{key}"
                if destination in named:
                    status = "applied_local_link"
                    classification = "compiled_bibliography_citation"
                    basis = "compiled bibliography named destination"
                else:
                    status = "reviewed_positive_residual"
                    classification = "unresolved_bibliography_citation"
                    basis = "citation has no delivered bibliography destination"
                    errors.append(f"unresolved citation {reader}:{relpath}:{key}")
                add(
                    relpath=relpath, original=original, offset=match.start(), form="cite",
                    raw=raw, visible=key, discriminator=f"{key}|{index}",
                    target_label_value=key, classification=classification,
                    status=status, basis=basis,
                    pdf_destination=destination if status == "applied_local_link" else "",
                )
            spans.append((match.start(), match.end()))

        # Structural and non-visible command spans are outside the candidate universe.
        structural_patterns = (
            r"\\(?:label|tag|oldpage|nocite)(?:\[[^]]*\])?\{[^}]*\}",
            rf"\\begin\{{(?:{STRUCTURAL_ENVS})\}}\[[^]]*\]",
        )
        for pattern in structural_patterns:
            spans.extend((m.start(), m.end()) for m in re.finditer(pattern, text))

        def covered(offset: int) -> bool:
            return any(start <= offset < end for start, end in spans)

        dotted = re.compile(r"(?<![A-Za-z0-9.])((?:\d+\.){1,5}\d+)(?![A-Za-z0-9])")
        for match in dotted.finditer(text):
            if covered(match.start()):
                continue
            token = match.group(1)
            context = line_context(original, match.start())
            possible = [
                f"{prefix}.{token}",
                f"subsection:{prefix}.{token}",
                f"section:{prefix}.{token}",
            ]
            local = [label for label in possible if label in aux_labels]
            if structural_context(context):
                classification = "structural_heading_number"
                basis = "number repeats the visible source structural heading and is not a use edge"
            elif external_context(context):
                classification = "external_work_or_cross_volume_locator"
                basis = "same-line source syntax explicitly identifies an external work or volume"
            elif local:
                classification = "unwrapped_same_reader_reference"
                basis = "plain locator has an exact same-reader target but is not wrapped"
                errors.append(
                    f"unwrapped same-reader locator {reader}:{relpath}:"
                    f"{line_col(original, match.start())[0]}:{token}->{local[0]}"
                )
            elif relpath == "ega3.tex" and token in {"13.4", "13.7"}:
                classification = "cross_reader_ega0_range_locator"
                basis = "introductory parenthesis explicitly assigns this range to EGA 0"
            else:
                classification = "nonlocal_or_nonsymbolic_numeric_locator"
                basis = "no exact same-reader declaration exists; no target is guessed"
            target_label_value = local[0] if local else ""
            add(
                relpath=relpath, original=original, offset=match.start(), form="plain_dotted_locator",
                raw=token, visible=token, discriminator=token,
                target_label_value=target_label_value, classification=classification,
                status="reviewed_positive_residual", basis=basis,
            )

        section_patterns = (
            ("textsection_locator", re.compile(r"\\textsection\s*(?:\{)?(\d+)")),
            ("named_section_locator", re.compile(r"\b(?:Section|Sections)~?(\d+)")),
            ("named_chapter_locator", re.compile(r"\b(?:Chapter|Chapters)~?([IVX]+)")),
        )
        for form, regex in section_patterns:
            for match in regex.finditer(text):
                if covered(match.start()):
                    continue
                token = match.group(1)
                context = line_context(original, match.start())
                nearby_context = " ".join(
                    original[max(0, match.start() - 300) : min(len(original), match.end() + 300)].split()
                )
                if form == "named_chapter_locator":
                    local_label = "section:ega3" if reader == "ega3" and token == "III" else ""
                else:
                    local_label = f"section:{prefix}.{token}"
                    if local_label not in aux_labels:
                        local_label = ""
                if structural_context(context):
                    classification = "structural_section_heading"
                    basis = "number is the visible source structural heading and is not a use edge"
                elif external_context(context) or external_context(nearby_context):
                    classification = "external_work_or_cross_volume_section"
                    basis = "same-line source syntax explicitly identifies an external work or volume"
                elif local_label:
                    classification = "unwrapped_same_reader_section_reference"
                    basis = "plain section/chapter locator has an exact same-reader target but is not wrapped"
                    errors.append(
                        f"unwrapped same-reader section {reader}:{relpath}:"
                        f"{line_col(original, match.start())[0]}:{token}->{local_label}"
                    )
                else:
                    classification = "unpublished_or_nonlocal_section_locator"
                    basis = "no exact same-reader published section target exists"
                add(
                    relpath=relpath, original=original, offset=match.start(), form=form,
                    raw=original[match.start() : match.end()], visible=token,
                    discriminator=token, target_label_value=local_label,
                    classification=classification, status="reviewed_positive_residual",
                    basis=basis,
                )

    return candidates, applications, residuals, errors


def goto_actions(reader: PdfReader) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for page_number, page in enumerate(reader.pages, 1):
        for annotation_index, ref in enumerate(page.get("/Annots") or []):
            annotation = ref.get_object()
            action = annotation.get("/A")
            if not action or action.get("/S") != "/GoTo":
                continue
            rect = tuple(round(float(value), 3) for value in annotation.get("/Rect"))
            rows.append(
                {
                    "pdf_page": page_number,
                    "annotation_index": annotation_index,
                    "rect": rect,
                    "destination": str(action.get("/D")),
                }
            )
    return rows


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: build_reference_v2_delivery.py WORK_ROOT")
    root = Path(sys.argv[1]).resolve()
    source = root / "source"
    controls = root / "controls"
    specs = {
        "ega0": {
            "master": "ega0.tex",
            "prefix": "0",
            "final_pdf": root / "build/reference_v2_full_r3_ega0/ega0.pdf",
            "final_aux": root / "build/reference_v2_full_r3_ega0/ega0.aux",
            "baseline_pdf": root / "build/reference_repairs_r1_ega0/ega0.pdf",
        },
        "ega3": {
            "master": "ega3.tex",
            "prefix": "III",
            "final_pdf": root / "build/reference_v2_full_r4_ega3/ega3.pdf",
            "final_aux": root / "build/reference_v2_full_r4_ega3/ega3.aux",
            "baseline_pdf": root / "build/reference_repairs_r1_ega3/ega3.pdf",
        },
    }
    errors: list[str] = []
    source_rows: dict[str, dict[str, object]] = {}
    target_rows: list[dict[str, object]] = []
    alias_rows: list[dict[str, object]] = []
    candidate_rows: list[dict[str, object]] = []
    application_rows: list[dict[str, object]] = []
    residual_rows: list[dict[str, object]] = []
    edge_rows: list[dict[str, object]] = []
    per_reader: dict[str, dict[str, object]] = {}

    for reader_name, spec in specs.items():
        closure = active_closure(source, str(spec["master"]))
        for order, relpath in enumerate(closure, 1):
            path = source / relpath
            row = source_rows.setdefault(
                relpath,
                {
                    "source_relpath": relpath,
                    "bytes": path.stat().st_size,
                    "sha256": file_sha(path),
                    "ega0_member": "no",
                    "ega3_member": "no",
                    "ega0_order": "",
                    "ega3_order": "",
                },
            )
            row[f"{reader_name}_member"] = "yes"
            row[f"{reader_name}_order"] = order

        aux_labels = parse_newlabels(Path(spec["final_aux"]))
        source_positions, label_errors = source_label_positions(source, closure)
        errors.extend(f"{reader_name}: {item}" for item in label_errors)
        pdf = PdfReader(str(spec["final_pdf"]))
        named = pdf.named_destinations
        aliases_by_destination: dict[str, list[str]] = defaultdict(list)
        for label, values in aux_labels.items():
            destination = values["pdf_destination"]
            if destination:
                aliases_by_destination[destination].append(label)

        target_by_destination: dict[str, str] = {}
        for destination, named_value in sorted(named.items()):
            tid = target_id(reader_name, destination)
            target_by_destination[destination] = tid
            pdf_page = pdf.get_destination_page_number(named_value) + 1
            labels = sorted(aliases_by_destination.get(destination, []))
            positions = [source_positions[label] for label in labels if label in source_positions]
            representative = positions[0] if positions else {}
            target_rows.append(
                {
                    "target_id": tid,
                    "reader": reader_name,
                    "pdf_destination": destination,
                    "pdf_page": pdf_page,
                    "destination_kind": destination.split(".", 1)[0],
                    "source_labels": "|".join(labels),
                    "source_relpath": representative.get("source_relpath", ""),
                    "source_line": representative.get("source_line", ""),
                    "source_sha256": representative.get("source_sha256", ""),
                    "status": "resolved_unique_pdf_destination",
                }
            )
        for label, values in sorted(aux_labels.items()):
            destination = values["pdf_destination"]
            if not destination:
                continue
            if destination not in target_by_destination:
                errors.append(f"{reader_name}: aux label destination absent from PDF: {label}->{destination}")
                continue
            position = source_positions.get(label, {})
            alias_rows.append(
                {
                    "reader": reader_name,
                    "source_label": label,
                    "target_id": target_by_destination[destination],
                    "pdf_destination": destination,
                    "printed_value": values["printed_value"],
                    "printed_page": values["printed_page"],
                    "source_relpath": position.get("source_relpath", ""),
                    "source_line": position.get("source_line", ""),
                    "source_sha256": position.get("source_sha256", ""),
                    "status": "active_aux_alias",
                }
            )

        candidates, applications, residuals, candidate_errors = extract_candidates(
            reader=reader_name,
            prefix=str(spec["prefix"]),
            source=source,
            closure=closure,
            aux_labels=aux_labels,
            named=named,
            target_by_destination=target_by_destination,
        )
        errors.extend(candidate_errors)
        candidate_rows.extend(candidates)
        application_rows.extend(applications)
        residual_rows.extend(residuals)

        baseline = PdfReader(str(spec["baseline_pdf"]))
        baseline_actions = goto_actions(baseline)
        final_actions = goto_actions(pdf)
        baseline_counter = Counter(
            (row["pdf_page"], row["rect"], row["destination"])
            for row in baseline_actions
        )
        new_count = 0
        for row in final_actions:
            key = (row["pdf_page"], row["rect"], row["destination"])
            if baseline_counter[key]:
                baseline_counter[key] -= 1
                origin = "inherited_internal_pdf_link"
            else:
                origin = "reviewed_reference_only_application"
                new_count += 1
            destination = str(row["destination"])
            if destination not in target_by_destination:
                errors.append(f"{reader_name}: broken PDF GoTo {destination}")
                tid = ""
                target_page = ""
            else:
                tid = target_by_destination[destination]
                target_page = pdf.get_destination_page_number(named[destination]) + 1
            identity = "|".join(
                (
                    reader_name,
                    str(row["pdf_page"]),
                    str(row["annotation_index"]),
                    ",".join(f"{value:.3f}" for value in row["rect"]),
                    destination,
                )
            )
            edge_rows.append(
                {
                    "edge_id": f"ega3.{reader_name}.edge.sha256." + hashlib.sha256(identity.encode()).hexdigest(),
                    "reader": reader_name,
                    "pdf_page": row["pdf_page"],
                    "annotation_index": row["annotation_index"],
                    "rect_x0": f"{row['rect'][0]:.3f}",
                    "rect_y0": f"{row['rect'][1]:.3f}",
                    "rect_x1": f"{row['rect'][2]:.3f}",
                    "rect_y1": f"{row['rect'][3]:.3f}",
                    "pdf_destination": destination,
                    "target_id": tid,
                    "target_pdf_page": target_page,
                    "origin_class": origin,
                    "status": "resolved_internal_goto" if tid else "broken_goto",
                }
            )
        old_text_equal = sum(
            (baseline.pages[index].extract_text() or "") == (pdf.pages[index].extract_text() or "")
            for index in range(min(len(baseline.pages), len(pdf.pages)))
        )
        if len(baseline.pages) != len(pdf.pages):
            errors.append(f"{reader_name}: baseline/final page count changed")
        if old_text_equal != len(pdf.pages):
            errors.append(f"{reader_name}: reference-only build changed extracted text")
        expected_new = 29 if reader_name == "ega0" else 61
        if new_count != expected_new:
            errors.append(f"{reader_name}: new PDF edge count {new_count} != {expected_new}")
        per_reader[reader_name] = {
            "source_closure": len(closure),
            "aux_labels": len(aux_labels),
            "named_destinations": len(named),
            "pdf_pages": len(pdf.pages),
            "pdf_goto_actions": len(final_actions),
            "baseline_goto_actions": len(baseline_actions),
            "reviewed_new_goto_actions": new_count,
            "baseline_to_final_extracted_text_pages_equal": old_text_equal,
            "candidates": len(candidates),
            "applications": len(applications),
            "residuals": len(residuals),
            "pdf_bytes": Path(spec["final_pdf"]).stat().st_size,
            "pdf_sha256": file_sha(Path(spec["final_pdf"])),
        }

    candidate_ids = {str(row["candidate_id"]) for row in candidate_rows}
    application_ids = {str(row["candidate_id"]) for row in application_rows}
    residual_ids = {str(row["candidate_id"]) for row in residual_rows}
    if application_ids & residual_ids:
        errors.append("candidate partition overlap")
    if application_ids | residual_ids != candidate_ids:
        errors.append("candidate partition incomplete")
    if len(candidate_ids) != len(candidate_rows):
        errors.append("duplicate candidate IDs")
    if len({row["target_id"] for row in target_rows}) != len(target_rows):
        errors.append("duplicate target IDs")
    if len({row["edge_id"] for row in edge_rows}) != len(edge_rows):
        errors.append("duplicate edge IDs")

    source_path = controls / "SOURCE_CLOSURE.csv"
    target_path = controls / "REFERENCE_TARGETS.csv"
    alias_path = controls / "REFERENCE_TARGET_ALIASES.csv"
    candidate_path = controls / "REFERENCE_CANDIDATES.csv"
    application_path = controls / "REFERENCE_APPLICATIONS.csv"
    residual_path = controls / "REFERENCE_RESIDUALS.csv"
    edge_path = controls / "REFERENCE_EDGES.csv"
    write_csv(source_path, [
        "source_relpath", "bytes", "sha256", "ega0_member", "ega0_order",
        "ega3_member", "ega3_order",
    ], sorted(source_rows.values(), key=lambda row: str(row["source_relpath"])))
    write_csv(target_path, [
        "target_id", "reader", "pdf_destination", "pdf_page", "destination_kind",
        "source_labels", "source_relpath", "source_line", "source_sha256", "status",
    ], target_rows)
    write_csv(alias_path, [
        "reader", "source_label", "target_id", "pdf_destination", "printed_value",
        "printed_page", "source_relpath", "source_line", "source_sha256", "status",
    ], alias_rows)
    common_candidate_fields = [
        "candidate_id", "reader", "reference_form", "source_relpath", "source_line",
        "source_column", "visible_text", "raw_tex", "context", "source_sha256",
        "target_label", "pdf_destination", "target_id", "classification", "status",
        "resolution_basis",
    ]
    write_csv(candidate_path, common_candidate_fields, candidate_rows)
    write_csv(application_path, ["application_id", *common_candidate_fields], application_rows)
    write_csv(residual_path, ["residual_id", *common_candidate_fields], residual_rows)
    write_csv(edge_path, [
        "edge_id", "reader", "pdf_page", "annotation_index", "rect_x0", "rect_y0",
        "rect_x1", "rect_y1", "pdf_destination", "target_id", "target_pdf_page",
        "origin_class", "status",
    ], edge_rows)

    unsafe_cells: list[str] = []
    for path in (source_path, target_path, alias_path, candidate_path, application_path, residual_path, edge_path):
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            for row_number, row in enumerate(csv.DictReader(handle), 2):
                for column, value in row.items():
                    if value.startswith(UNSAFE_PREFIXES):
                        unsafe_cells.append(f"{path.name}:{row_number}:{column}")
    if unsafe_cells:
        errors.append(f"formula-unsafe CSV cells: {unsafe_cells[:20]}")

    validation = {
        "schema": "ega3-two-reader-reference-v2-delivery-validation-1.0",
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "set_relation": {
            "candidates": len(candidate_rows),
            "applications": len(application_rows),
            "residuals": len(residual_rows),
            "formula": "REFERENCE_CANDIDATES = REFERENCE_APPLICATIONS disjoint-union REFERENCE_RESIDUALS",
            "partition_overlap": len(application_ids & residual_ids),
            "partition_missing": len(candidate_ids - (application_ids | residual_ids)),
            "pdf_edges": len(edge_rows),
            "edge_explanation": "REFERENCE_EDGES is the complete delivered-PDF GoTo graph and is separate from the source-candidate partition.",
        },
        "counts": {
            "source_files": len(source_rows),
            "targets": len(target_rows),
            "target_aliases": len(alias_rows),
            "candidates": len(candidate_rows),
            "applications": len(application_rows),
            "residuals": len(residual_rows),
            "pdf_edges": len(edge_rows),
            "reviewed_new_pdf_edges": len([row for row in edge_rows if row["origin_class"] == "reviewed_reference_only_application"]),
        },
        "per_reader": per_reader,
        "csv_formula_unsafe_cells": unsafe_cells,
        "files": {
            path.name: {"bytes": path.stat().st_size, "sha256": file_sha(path)}
            for path in (source_path, target_path, alias_path, candidate_path, application_path, residual_path, edge_path)
        },
    }
    validation_path = controls / "REFERENCE_GRAPH_VALIDATION.json"
    validation_path.write_text(json.dumps(validation, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": validation["status"],
        "errors": errors,
        "counts": validation["counts"],
        "per_reader": per_reader,
        "validation": str(validation_path),
        "validation_sha256": file_sha(validation_path),
    }, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
