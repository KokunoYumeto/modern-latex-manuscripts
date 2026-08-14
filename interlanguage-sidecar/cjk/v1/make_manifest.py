#!/usr/bin/env python3
"""Create the deterministic non-self-referential release manifest."""

from __future__ import annotations

import json
import sys

sys.dont_write_bytecode = True

from pkg import PackageError, write_manifest


try:
    count, member_bytes, manifest_sha256 = write_manifest()
except PackageError as exc:
    raise SystemExit(f"manifest failure: {exc}") from exc

print(json.dumps({
    "files": count,
    "member_bytes": member_bytes,
    "manifest_sha256": manifest_sha256,
}, sort_keys=True))
