from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
FIXED_DOCUMENT_TIME = b"2026-07-18T00:00:00Z"


def normalize_core_properties(data: bytes) -> bytes:
    return re.sub(
        rb"(<dcterms:(?:created|modified)\b[^>]*>)[^<]*(</dcterms:(?:created|modified)>)",
        lambda match: match.group(1) + FIXED_DOCUMENT_TIME + match.group(2),
        data,
    )


def normalize(path: Path) -> None:
    temporary = path.with_suffix(path.suffix + ".normalizing")
    with ZipFile(path, "r") as source, ZipFile(
        temporary,
        "w",
        compression=ZIP_DEFLATED,
        compresslevel=9,
        strict_timestamps=False,
    ) as target:
        for name in sorted(source.namelist()):
            data = source.read(name)
            if name == "docProps/core.xml":
                data = normalize_core_properties(data)
            info = ZipInfo(filename=name, date_time=FIXED_ZIP_TIME)
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o600 << 16
            target.writestr(info, data, compress_type=ZIP_DEFLATED, compresslevel=9)
        target.comment = b""
    temporary.replace(path)


if __name__ == "__main__":
    workbook = Path(sys.argv[1] if len(sys.argv) > 1 else "ROMANCE_CORPUS_METADATA_v1.xlsx")
    normalize(workbook)
    print(hashlib.sha256(workbook.read_bytes()).hexdigest().upper())
