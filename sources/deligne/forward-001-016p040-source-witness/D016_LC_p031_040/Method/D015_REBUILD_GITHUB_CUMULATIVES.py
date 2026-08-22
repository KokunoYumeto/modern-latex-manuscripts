#!/usr/bin/env python3
"""Deterministically splice audited D015 editions into pinned GitHub cumulatives.

The program is deliberately staging-only: ``--output-root`` must be disjoint
from ``--repo-root``.  With no mode flag it performs a dry run, builds and
validates the proposed PDFs in memory, and prints the JSON receipt to stdout.
Pass ``--write`` to materialize the three PDFs and receipt under the explicit
output root.  A write always performs the two-build determinism gate; a dry run
can request the same gate with ``--verify-determinism``.

One-based, inclusive legacy D015 ranges in the pinned 001--016p040 witnesses are:

* English: 211--216 (six pages; D016 resumes at page 217)
* French:  212--217 (six pages; D016 resumes at page 218)
* Scan:    300--312 (thirteen pages; D016 resumes at page 313)

The audited replacements have seven English pages, thirteen French pages, and
thirteen scan pages.  Consequently the untouched D016 English and French tails
move forward by one and seven pages respectively.  Every page outside the
legacy ranges is fingerprinted before and after the rebuild.
The scan replacement must be the exact 13-page IAS Number14 authority, not the
lower-resolution collected split or a comparator.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import io
import json
import os
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

try:
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import (
        ArrayObject,
        ByteStringObject,
        DictionaryObject,
        IndirectObject,
        StreamObject,
    )
except ImportError as exc:  # pragma: no cover - dependency error is explicit
    raise SystemExit("pypdf is required to rebuild the cumulative PDFs") from exc


SCHEMA = "deligne-d015-github-cumulative-rebuild-v2"
RECEIPT_NAME = "REBUILD_GITHUB_CUMULATIVES_RECEIPT.json"
IAS_D015_SHA256 = "22BD33F5D00EA962BA24996703CDDF74C4DCB09BF91050F0463036B5B38803CB"


@dataclass(frozen=True)
class Pin:
    key: str
    baseline_relative: Path
    public_mirror_relative: Path | None
    expected_sha256: str
    expected_pages: int
    splice_first: int
    splice_last: int
    replacement_pages: int
    output_name: str
    title: str

    @property
    def splice_count(self) -> int:
        return self.splice_last - self.splice_first + 1

    @property
    def d016_first_page(self) -> int:
        return self.splice_last + 1

    @property
    def output_pages(self) -> int:
        return self.expected_pages - self.splice_count + self.replacement_pages

    @property
    def output_splice_last(self) -> int:
        return self.splice_first + self.replacement_pages - 1

    @property
    def output_d016_first_page(self) -> int:
        return self.output_splice_last + 1


WITNESS_ROOT = Path(
    "sources/deligne/forward-001-016p040-source-witness/"
    "D016_LC_p031_040/SEQ_CUM/ALL_001_016p040"
)

PINS: Mapping[str, Pin] = {
    "en": Pin(
        key="en",
        baseline_relative=WITNESS_ROOT / "PDF/ALL_001_016p040_EN.pdf",
        public_mirror_relative=Path(
            "reader-pdfs/deligne/"
            "00-000 Deligne - Sequential Cumulative Papers 001-016p040 - "
            "English Translation.pdf"
        ),
        expected_sha256="6803B030362C4659F82FE29E1F6C625B3ABB201F9E1C44514E302317795826F4",
        expected_pages=237,
        splice_first=211,
        splice_last=216,
        replacement_pages=7,
        output_name="ALL_001_016p040_EN.pdf",
        title="Deligne Sequential Cumulative Papers 001-016p040 - English",
    ),
    "fr": Pin(
        key="fr",
        baseline_relative=WITNESS_ROOT / "PDF/ALL_001_016p040_FR.pdf",
        public_mirror_relative=Path(
            "reader-pdfs/deligne/"
            "01-000 Deligne - Sequential Cumulative Papers 001-016p040 - "
            "French Working PDF.pdf"
        ),
        expected_sha256="AB2763076BC208F1449300421615B530DB80038839F6FDED1314DF127AACA9D9",
        expected_pages=238,
        splice_first=212,
        splice_last=217,
        replacement_pages=13,
        output_name="ALL_001_016p040_FR.pdf",
        title="Deligne Sequential Cumulative Papers 001-016p040 - French",
    ),
    "scan": Pin(
        key="scan",
        baseline_relative=WITNESS_ROOT / "SCAN/ALL_001_016p040_SCAN.pdf",
        public_mirror_relative=None,
        expected_sha256="DDAD59B15BB729A8ACC69BAD55538E72242552338FA62E625C0B07A461F9FA5B",
        expected_pages=352,
        splice_first=300,
        splice_last=312,
        replacement_pages=13,
        output_name="ALL_001_016p040_SCAN.pdf",
        title="Deligne Sequential Cumulative Papers 001-016p040 - Authority Scans",
    ),
}


class ContractError(RuntimeError):
    """A pinned input, splice, output, or determinism contract failed."""


@dataclass(frozen=True)
class PdfBlob:
    path: Path
    data: bytes
    sha256: str
    pages: int


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def sequence_sha256(values: Iterable[str]) -> str:
    material = "\n".join(values).encode("ascii")
    return sha256_bytes(material)


def read_pdf_blob(path: Path) -> PdfBlob:
    resolved = path.expanduser().resolve(strict=True)
    if not resolved.is_file():
        raise ContractError(f"PDF input is not a regular file: {resolved}")
    data = resolved.read_bytes()
    try:
        pages = len(PdfReader(io.BytesIO(data), strict=False).pages)
    except Exception as exc:
        raise ContractError(f"Cannot parse PDF {resolved}: {exc}") from exc
    return PdfBlob(resolved, data, sha256_bytes(data), pages)


def verify_pinned_blob(blob: PdfBlob, pin: Pin, role: str) -> None:
    if blob.sha256 != pin.expected_sha256:
        raise ContractError(
            f"{pin.key} {role} SHA-256 mismatch: expected "
            f"{pin.expected_sha256}, got {blob.sha256} ({blob.path})"
        )
    if blob.pages != pin.expected_pages:
        raise ContractError(
            f"{pin.key} {role} page-count mismatch: expected "
            f"{pin.expected_pages}, got {blob.pages} ({blob.path})"
        )


def is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def validate_roots(repo_root_arg: str, output_root_arg: str) -> tuple[Path, Path]:
    repo_root = Path(repo_root_arg).expanduser().resolve(strict=True)
    if not repo_root.is_dir():
        raise ContractError(f"Repository root is not a directory: {repo_root}")
    output_root = Path(output_root_arg).expanduser().resolve(strict=False)

    # Avoid both direct repository writes and an overly broad ancestor target.
    if is_relative_to(output_root, repo_root) or is_relative_to(repo_root, output_root):
        raise ContractError(
            "--output-root must be disjoint from --repo-root; rebuild in a "
            "separate staging directory"
        )
    if output_root.exists() and not output_root.is_dir():
        raise ContractError(f"Output root exists but is not a directory: {output_root}")
    return repo_root, output_root


def canonical_pdf_object(value: Any, active: set[tuple[int, int, int]] | None = None) -> Any:
    """Return an object-number-independent representation of a PDF object.

    Page fingerprints use this for geometry, contents, and resources.  Indirect
    references are dereferenced, streams are represented by decoded-data hashes,
    and parent/back-reference keys are omitted to avoid document-tree cycles.
    """

    if active is None:
        active = set()
    if value is None:
        return None
    if isinstance(value, IndirectObject):
        pdf_identity = id(getattr(value, "pdf", None))
        identity = (pdf_identity, int(value.idnum), int(value.generation))
        if identity in active:
            return {"cycle": True}
        active.add(identity)
        try:
            return canonical_pdf_object(value.get_object(), active)
        finally:
            active.remove(identity)
    if isinstance(value, StreamObject):
        attributes = {
            str(key): canonical_pdf_object(item, active)
            for key, item in sorted(value.items(), key=lambda pair: str(pair[0]))
            if str(key) not in {"/Length", "/Parent", "/P"}
        }
        stream_representation = "decoded"
        try:
            stream_data = value.get_data()
        except Exception as exc:
            # IAS and collected scan witnesses contain JBIG2 streams.  pypdf
            # correctly preserves those encoded streams, but decoding them is
            # optional and depends on an external jbig2dec binary.  Hashing the
            # original encoded payload together with /Filter and /DecodeParms
            # (already present in ``attributes``) is equally exact for proving
            # page identity before and after this lossless splice.
            stream_data = getattr(value, "_data", None)
            if stream_data is None:
                raise ContractError(f"Unable to fingerprint a PDF stream: {exc}") from exc
            stream_representation = "encoded"
        return {
            "stream_attributes": attributes,
            "stream_representation": stream_representation,
            "stream_sha256": sha256_bytes(stream_data),
        }
    if isinstance(value, DictionaryObject):
        return {
            str(key): canonical_pdf_object(item, active)
            for key, item in sorted(value.items(), key=lambda pair: str(pair[0]))
            if str(key) not in {"/Length", "/Parent", "/P"}
        }
    if isinstance(value, (ArrayObject, list, tuple)):
        return [canonical_pdf_object(item, active) for item in value]
    if isinstance(value, bytes):
        return {"bytes_base64": base64.b64encode(value).decode("ascii")}
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return format(value, ".17g")
    return str(value)


def page_fingerprint(page: Any) -> str:
    # /Annots is intentionally excluded: link destinations can contain page
    # back-references. PdfWriter.add_page still clones annotations; the stable
    # visual/content identity needed for splice validation is captured below.
    payload = {
        key: canonical_pdf_object(page.get(key))
        for key in (
            "/MediaBox",
            "/CropBox",
            "/TrimBox",
            "/BleedBox",
            "/ArtBox",
            "/Rotate",
            "/UserUnit",
            "/Contents",
            "/Resources",
        )
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256_bytes(encoded)


def copy_outline(reader: PdfReader, writer: PdfWriter, pin: Pin) -> None:
    """Recreate resolvable bookmarks, shifting destinations after D015."""

    try:
        outline = reader.outline
    except Exception:
        return

    def walk(items: Sequence[Any], parent: Any = None) -> None:
        preceding_node: Any = None
        for item in items:
            if isinstance(item, list):
                if preceding_node is not None:
                    walk(item, preceding_node)
                continue
            try:
                page_number = reader.get_destination_page_number(item)
            except Exception:
                preceding_node = None
                continue
            if page_number is None or page_number < 0 or page_number >= len(reader.pages):
                preceding_node = None
                continue
            first_index = pin.splice_first - 1
            last_exclusive = pin.splice_last
            if page_number < first_index:
                output_page_number = page_number
            elif page_number < last_exclusive:
                # Preserve a bookmark into legacy D015 at the corresponding
                # replacement page, clamping only if the replacement is shorter.
                output_page_number = first_index + min(
                    page_number - first_index, pin.replacement_pages - 1
                )
            else:
                output_page_number = page_number + (
                    pin.replacement_pages - pin.splice_count
                )
            title = str(getattr(item, "title", item))
            preceding_node = writer.add_outline_item(
                title, output_page_number, parent=parent
            )

    if isinstance(outline, list):
        walk(outline)


def deterministic_document_id(pin: Pin, baseline: PdfBlob, replacement: PdfBlob) -> bytes:
    seed = (
        f"{SCHEMA}\n{pin.key}\n{baseline.sha256}\n{replacement.sha256}\n"
        f"{pin.splice_first}-{pin.splice_last}\n"
    ).encode("ascii")
    return hashlib.sha256(seed).digest()[:16]


def build_pdf(pin: Pin, baseline: PdfBlob, replacement: PdfBlob) -> bytes:
    baseline_reader = PdfReader(io.BytesIO(baseline.data), strict=False)
    replacement_reader = PdfReader(io.BytesIO(replacement.data), strict=False)
    writer = PdfWriter()

    first_index = pin.splice_first - 1
    last_exclusive = pin.splice_last
    for page in baseline_reader.pages[:first_index]:
        writer.add_page(page)
    for page in replacement_reader.pages:
        writer.add_page(page)
    for page in baseline_reader.pages[last_exclusive:]:
        writer.add_page(page)

    copy_outline(baseline_reader, writer, pin)
    writer.add_metadata(
        {
            "/Title": pin.title,
            "/Author": "Pierre Deligne",
            "/Subject": "Sequential cumulative corpus through D016 page 40; audited D015 splice",
            "/Creator": "rebuild_github_cumulatives.py",
            "/Producer": "pypdf deterministic cumulative rebuild",
            "/CreationDate": "D:20000101000000Z",
            "/ModDate": "D:20000101000000Z",
        }
    )
    document_id = deterministic_document_id(pin, baseline, replacement)
    writer._ID = ArrayObject([ByteStringObject(document_id), ByteStringObject(document_id)])

    output = io.BytesIO()
    writer.write(output)
    return output.getvalue()


def verify_page_sequence(
    pin: Pin, baseline: PdfBlob, replacement: PdfBlob, output_data: bytes
) -> dict[str, Any]:
    baseline_reader = PdfReader(io.BytesIO(baseline.data), strict=False)
    replacement_reader = PdfReader(io.BytesIO(replacement.data), strict=False)
    output_reader = PdfReader(io.BytesIO(output_data), strict=False)

    if len(output_reader.pages) != pin.output_pages:
        raise ContractError(
            f"{pin.key} rebuilt page count mismatch: expected {pin.output_pages}, "
            f"got {len(output_reader.pages)}"
        )

    baseline_fingerprints = [page_fingerprint(page) for page in baseline_reader.pages]
    replacement_fingerprints = [page_fingerprint(page) for page in replacement_reader.pages]
    output_fingerprints = [page_fingerprint(page) for page in output_reader.pages]

    first_index = pin.splice_first - 1
    last_exclusive = pin.splice_last
    expected_fingerprints = (
        baseline_fingerprints[:first_index]
        + replacement_fingerprints
        + baseline_fingerprints[last_exclusive:]
    )
    if len(expected_fingerprints) != pin.output_pages:
        raise ContractError(f"{pin.key} internal splice topology produced the wrong length")

    mismatches = [
        index + 1
        for index, (expected, actual) in enumerate(
            zip(expected_fingerprints, output_fingerprints, strict=True)
        )
        if expected != actual
    ]
    if mismatches:
        preview = ", ".join(str(page) for page in mismatches[:12])
        raise ContractError(f"{pin.key} rebuilt page fingerprints differ at pages: {preview}")

    prefix = baseline_fingerprints[:first_index]
    suffix = baseline_fingerprints[last_exclusive:]
    output_last_exclusive = first_index + pin.replacement_pages
    inserted = output_fingerprints[first_index:output_last_exclusive]
    return {
        "status": "PASS",
        "baseline_splice_pages_1_based_inclusive": [pin.splice_first, pin.splice_last],
        "output_splice_pages_1_based_inclusive": [
            pin.splice_first,
            pin.output_splice_last,
        ],
        "inserted_page_count": len(inserted),
        "inserted_sequence_sha256": sequence_sha256(inserted),
        "preserved_prefix_page_count": len(prefix),
        "preserved_prefix_sequence_sha256": sequence_sha256(prefix),
        "preserved_suffix_page_count": len(suffix),
        "preserved_suffix_sequence_sha256": sequence_sha256(suffix),
        "d016_remainder_baseline_first_page": pin.d016_first_page,
        "d016_remainder_output_first_page": pin.output_d016_first_page,
        "d016_remainder_page_count": len(suffix),
        "all_output_pages_sequence_sha256": sequence_sha256(output_fingerprints),
        "mismatched_pages": [],
    }


def blob_receipt(blob: PdfBlob) -> dict[str, Any]:
    return {
        "path": str(blob.path),
        "bytes": len(blob.data),
        "pages": blob.pages,
        "sha256": blob.sha256,
    }


def output_receipt(path: Path, data: bytes, pages: int) -> dict[str, Any]:
    return {
        "path": str(path),
        "bytes": len(data),
        "pages": pages,
        "sha256": sha256_bytes(data),
    }


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_name: str | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", prefix=f".{path.name}.", suffix=".tmp", dir=path.parent, delete=False
        ) as handle:
            temporary_name = handle.name
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary_name, path)
        temporary_name = None
    finally:
        if temporary_name is not None:
            try:
                Path(temporary_name).unlink()
            except FileNotFoundError:
                pass


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--en-pdf", required=True, help="audited seven-page standalone D015 English PDF")
    parser.add_argument("--fr-pdf", required=True, help="audited thirteen-page standalone D015 French PDF")
    parser.add_argument(
        "--scan-pdf", required=True, help="exact 13-page IAS Number14 [~300dpi] D015 authority PDF"
    )
    parser.add_argument("--repo-root", required=True, help="Git repository root containing the pinned witnesses")
    parser.add_argument("--output-root", required=True, help="separate staging directory for all generated files")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="validate and build in memory only (default)")
    mode.add_argument("--write", action="store_true", help="write validated outputs and JSON receipt")
    parser.add_argument(
        "--verify-determinism",
        action="store_true",
        help="build each proposed output twice and require exact byte identity (automatic with --write)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="with --write, replace differing files already present under output-root",
    )
    args = parser.parse_args(argv)
    if args.overwrite and not args.write:
        parser.error("--overwrite is valid only with --write")
    return args


def run(args: argparse.Namespace) -> dict[str, Any]:
    repo_root, output_root = validate_roots(args.repo_root, args.output_root)
    replacement_paths = {
        "en": Path(args.en_pdf),
        "fr": Path(args.fr_pdf),
        "scan": Path(args.scan_pdf),
    }

    baselines: dict[str, PdfBlob] = {}
    mirrors: dict[str, PdfBlob] = {}
    replacements: dict[str, PdfBlob] = {}
    for key, pin in PINS.items():
        if pin.splice_count < 1 or pin.replacement_pages < 1:
            raise ContractError(f"{key} pin has an empty splice or replacement")
        baseline = read_pdf_blob(repo_root / pin.baseline_relative)
        verify_pinned_blob(baseline, pin, "baseline")
        baselines[key] = baseline

        if pin.public_mirror_relative is not None:
            mirror = read_pdf_blob(repo_root / pin.public_mirror_relative)
            verify_pinned_blob(mirror, pin, "public reader mirror")
            if mirror.data != baseline.data:
                raise ContractError(f"{key} public reader mirror is not byte-identical to its pinned witness")
            mirrors[key] = mirror

        replacement = read_pdf_blob(replacement_paths[key])
        if replacement.pages != pin.replacement_pages:
            raise ContractError(
                f"{key} D015 replacement must have {pin.replacement_pages} pages; "
                f"got {replacement.pages} ({replacement.path})"
            )
        if key == "scan" and replacement.sha256 != IAS_D015_SHA256:
            raise ContractError(
                "D015 scan replacement is not the controlling IAS Number14 [~300dpi] "
                f"authority: expected {IAS_D015_SHA256}, got {replacement.sha256}"
            )
        replacements[key] = replacement

    enforce_determinism = bool(args.verify_determinism or args.write)
    generated: dict[str, bytes] = {}
    validations: dict[str, dict[str, Any]] = {}
    determinism: dict[str, dict[str, Any]] = {}
    for key, pin in PINS.items():
        first = build_pdf(pin, baselines[key], replacements[key])
        first_sha = sha256_bytes(first)
        second_sha: str | None = None
        if enforce_determinism:
            second = build_pdf(pin, baselines[key], replacements[key])
            second_sha = sha256_bytes(second)
            if first != second:
                raise ContractError(
                    f"{key} determinism gate failed: first {first_sha}, second {second_sha}"
                )
        generated[key] = first
        validations[key] = verify_page_sequence(pin, baselines[key], replacements[key], first)
        determinism[key] = {
            "gate_enforced": enforce_determinism,
            "status": "PASS" if enforce_determinism else "NOT_REQUESTED",
            "first_build_sha256": first_sha,
            "second_build_sha256": second_sha,
            "byte_identical": True if enforce_determinism else None,
        }

    outputs = {
        key: output_receipt(output_root / pin.output_name, generated[key], pin.output_pages)
        for key, pin in PINS.items()
    }
    receipt: dict[str, Any] = {
        "schema": SCHEMA,
        "status": "PASS",
        "mode": "write" if args.write else "dry-run",
        "repo_root": str(repo_root),
        "output_root": str(output_root),
        "write_boundary": "output-root-only; repository and supplied inputs read-only",
        "pinned_baselines": {key: blob_receipt(blob) for key, blob in baselines.items()},
        "pinned_public_reader_mirrors": {key: blob_receipt(blob) for key, blob in mirrors.items()},
        "d015_replacements": {key: blob_receipt(blob) for key, blob in replacements.items()},
        "outputs": outputs,
        "page_sequence_validation": validations,
        "determinism": determinism,
        "receipt_path": str(output_root / RECEIPT_NAME) if args.write else None,
    }

    if args.write:
        output_root.mkdir(parents=True, exist_ok=True)
        # Preflight every destination before any PDF is changed.
        for key, pin in PINS.items():
            destination = output_root / pin.output_name
            if destination.exists():
                if not destination.is_file():
                    raise ContractError(f"Output destination is not a file: {destination}")
                existing_sha = sha256_bytes(destination.read_bytes())
                proposed_sha = sha256_bytes(generated[key])
                if existing_sha != proposed_sha and not args.overwrite:
                    raise ContractError(
                        f"Refusing to replace differing output without --overwrite: {destination}"
                    )
        for key, pin in PINS.items():
            destination = output_root / pin.output_name
            proposed = generated[key]
            if not destination.exists() or sha256_bytes(destination.read_bytes()) != sha256_bytes(proposed):
                atomic_write(destination, proposed)

        receipt_bytes = (
            json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        ).encode("utf-8")
        atomic_write(output_root / RECEIPT_NAME, receipt_bytes)

    return receipt


def main(argv: Sequence[str] | None = None) -> int:
    try:
        args = parse_args(argv)
        receipt = run(args)
    except (ContractError, FileNotFoundError, OSError, ValueError) as exc:
        error = {"schema": SCHEMA, "status": "FAIL", "error": str(exc)}
        print(json.dumps(error, indent=2, sort_keys=True), file=sys.stderr)
        return 2
    print(json.dumps(receipt, indent=2, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
