#!/usr/bin/env python3
"""Rewrite a PDF with stable metadata and trailer identifiers."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, ByteStringObject, NameObject


def normalize(source: Path, destination: Path) -> None:
    reader = PdfReader(source)
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    writer.metadata = None
    writer.add_metadata(
        {
            "/Producer": "Pierre Deligne corpus deterministic build",
            "/Creator": "LaTeX; normalized with pypdf",
            "/CreationDate": "D:20260822000000Z",
            "/ModDate": "D:20260822000000Z",
        }
    )
    fingerprint = hashlib.sha256()
    fingerprint.update(str(len(reader.pages)).encode("ascii"))
    for page in reader.pages:
        fingerprint.update(str(page.mediabox).encode("ascii"))
        contents = page.get_contents()
        if contents is not None:
            fingerprint.update(contents.get_data())
    fixed_id = fingerprint.digest()[:16]
    writer._ID = ArrayObject([ByteStringObject(fixed_id), ByteStringObject(fixed_id)])
    writer._root_object.pop(NameObject("/Metadata"), None)
    with destination.open("wb") as stream:
        writer.write(stream)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    normalize(args.source, args.destination)


if __name__ == "__main__":
    main()
