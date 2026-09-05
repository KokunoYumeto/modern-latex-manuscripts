#!/usr/bin/env python3
"""Memory-bounded primitives for D020 candidate copy and cold-audit checks.

Large files are never materialized as a whole and no quadratic edit-distance
comparison is permitted.  The module is intentionally
standard-library only so its memory contract can be tested in isolation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import secrets
import tempfile


DEFAULT_CHUNK_BYTES = 64 * 1024
MAX_CHUNK_BYTES = 1024 * 1024


def checked_chunk_bytes(value: int) -> int:
    if isinstance(value, bool) or not 1 <= value <= MAX_CHUNK_BYTES:
        raise ValueError(f"chunk_bytes must be in 1..{MAX_CHUNK_BYTES}")
    return value


def stream_sha256(path: pathlib.Path, chunk_bytes: int = DEFAULT_CHUNK_BYTES) -> str:
    chunk_bytes = checked_chunk_bytes(chunk_bytes)
    digest = hashlib.sha256()
    with path.open("rb", buffering=0) as handle:
        while True:
            block = handle.read(chunk_bytes)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest().upper()


def files_equal_streaming(
    left: pathlib.Path,
    right: pathlib.Path,
    chunk_bytes: int = DEFAULT_CHUNK_BYTES,
) -> bool:
    """Return exact byte equality using at most two bounded data blocks."""
    chunk_bytes = checked_chunk_bytes(chunk_bytes)
    if left.stat().st_size != right.stat().st_size:
        return False
    with left.open("rb", buffering=0) as left_handle, right.open("rb", buffering=0) as right_handle:
        while True:
            left_block = left_handle.read(chunk_bytes)
            right_block = right_handle.read(chunk_bytes)
            if left_block != right_block:
                return False
            if not left_block:
                return True


def count_term_streaming(
    path: pathlib.Path,
    term: bytes,
    *,
    case_insensitive_ascii: bool = False,
    chunk_bytes: int = DEFAULT_CHUNK_BYTES,
) -> int:
    """Count possibly boundary-crossing byte terms without whole-file reads."""
    chunk_bytes = checked_chunk_bytes(chunk_bytes)
    if not term:
        raise ValueError("term must be nonempty")
    if len(term) > MAX_CHUNK_BYTES:
        raise ValueError("term is larger than the maximum supported audit chunk")
    needle = term.lower() if case_insensitive_ascii else term
    tail = b""
    consumed_before = 0
    count = 0
    with path.open("rb", buffering=0) as handle:
        while True:
            block = handle.read(chunk_bytes)
            if not block:
                break
            window = tail + block
            if case_insensitive_ascii:
                window = window.lower()
            base = consumed_before - len(tail)
            start = 0
            while True:
                index = window.find(needle, start)
                if index < 0:
                    break
                absolute_end = base + index + len(needle)
                # Matches wholly contained in the carried tail were counted in
                # the previous iteration; matches touching new bytes are new.
                if absolute_end > consumed_before:
                    count += 1
                start = index + 1
            keep = min(len(term) - 1, len(window))
            tail = window[-keep:] if keep else b""
            consumed_before += len(block)
    return count


def copy_file_streaming(
    source: pathlib.Path,
    destination: pathlib.Path,
    chunk_bytes: int = DEFAULT_CHUNK_BYTES,
) -> dict:
    """Copy one file atomically with bounded buffers and three-way hashing."""
    chunk_bytes = checked_chunk_bytes(chunk_bytes)
    destination.parent.mkdir(parents=True, exist_ok=True)
    source_hash = hashlib.sha256()
    destination_hash = hashlib.sha256()
    copied = 0
    temporary = destination.with_name(destination.name + f".{os.getpid()}.{secrets.token_hex(8)}.partial")
    temporary_created = False
    if destination.exists():
        raise FileExistsError("destination already exists")
    source_size_before = source.stat().st_size
    source_digest_before = stream_sha256(source, chunk_bytes)
    try:
        with source.open("rb", buffering=0) as src:
            with temporary.open("xb", buffering=0) as dst:
                temporary_created = True
                while True:
                    block = src.read(chunk_bytes)
                    if not block:
                        break
                    source_hash.update(block)
                    dst.write(block)
                    copied += len(block)
        with temporary.open("rb", buffering=0) as dst:
            while True:
                block = dst.read(chunk_bytes)
                if not block:
                    break
                destination_hash.update(block)
        source_digest_during = source_hash.hexdigest().upper()
        destination_digest = destination_hash.hexdigest().upper()
        source_size_after = source.stat().st_size
        source_digest_after = stream_sha256(source, chunk_bytes)
        if not (
            source_size_before
            == copied
            == source_size_after
            == temporary.stat().st_size
        ):
            raise RuntimeError("bounded copy size verification failed")
        if not (
            source_digest_before
            == source_digest_during
            == source_digest_after
            == destination_digest
        ):
            raise RuntimeError("source stability or bounded copy hash verification failed")
        # On Windows os.rename does not overwrite an existing destination. The
        # partial and final path share a directory/volume, so promotion is atomic.
        os.rename(temporary, destination)
        return {"bytes": copied, "sha256": source_digest_after}
    except BaseException:
        if temporary_created and temporary.exists():
            temporary.unlink()
        raise


def write_json_atomic(path: pathlib.Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def run_self_test(output: pathlib.Path) -> int:
    chunk_bytes = DEFAULT_CHUNK_BYTES
    pattern = bytes(range(256)) * 256
    with tempfile.TemporaryDirectory(prefix="d020_bounded_audit_") as temporary:
        root = pathlib.Path(temporary)
        left = root / "left.bin"
        equal = root / "equal.bin"
        unequal = root / "unequal.bin"
        with left.open("xb", buffering=0) as handle:
            for _ in range(48):
                handle.write(pattern)
            handle.write(b"terminal")
        copy_result = copy_file_streaming(left, equal, chunk_bytes)
        copy_file_streaming(left, unequal, chunk_bytes)
        with unequal.open("r+b", buffering=0) as handle:
            handle.seek(chunk_bytes - 1)
            original = handle.read(1)
            handle.seek(chunk_bytes - 1)
            handle.write(bytes([original[0] ^ 0xFF]))

        term_file = root / "term.bin"
        term = b"needle-boundary"
        with term_file.open("xb", buffering=0) as handle:
            handle.write(b"x" * (chunk_bytes - 7))
            handle.write(term)
            handle.write(b"y" * chunk_bytes)
            handle.write(term.upper())
            handle.write(b"z")

        result = {
            "schema": "D020_BOUNDED_STREAMING_AUDIT_SELFTEST_V1",
            "status": "PASS",
            "contract": {
                "algorithm": "fixed-size streaming blocks",
                "default_chunk_bytes": DEFAULT_CHUNK_BYTES,
                "maximum_chunk_bytes": MAX_CHUNK_BYTES,
                "whole_large_file_reads": False,
                "edit_distance_or_sequence_matcher": False,
            },
            "tested_tools": {
                "bounded_streaming_audit.py": stream_sha256(pathlib.Path(__file__)),
                "run_low_memory_guard.py": stream_sha256(pathlib.Path(__file__).with_name("run_low_memory_guard.py")),
            },
            "fixture": {
                "bytes": left.stat().st_size,
                "copy": copy_result,
                "equal_file_matches": files_equal_streaming(left, equal, chunk_bytes),
                "same_size_one_byte_difference_rejected": not files_equal_streaming(left, unequal, chunk_bytes),
                "existing_destination_refused_without_change": False,
                "source_hash": stream_sha256(left, chunk_bytes),
                "equal_hash": stream_sha256(equal, chunk_bytes),
                "unequal_hash": stream_sha256(unequal, chunk_bytes),
                "boundary_term_case_insensitive_count": count_term_streaming(
                    term_file,
                    term,
                    case_insensitive_ascii=True,
                    chunk_bytes=chunk_bytes,
                ),
            },
        }
        equal_hash_before_refusal = stream_sha256(equal, chunk_bytes)
        try:
            copy_file_streaming(left, equal, chunk_bytes)
        except FileExistsError:
            result["fixture"]["existing_destination_refused_without_change"] = (
                stream_sha256(equal, chunk_bytes) == equal_hash_before_refusal
                and not equal.with_name(equal.name + ".partial").exists()
            )
        collision_destination = root / "collision.bin"
        collision_token = "00" * 8
        collision_partial = collision_destination.with_name(
            collision_destination.name + f".{os.getpid()}.{collision_token}.partial"
        )
        collision_sentinel = b"foreign-preexisting-partial"
        collision_partial.write_bytes(collision_sentinel)
        original_token_hex = secrets.token_hex
        result["fixture"]["partial_collision_refused_without_deleting_foreign_path"] = False
        try:
            secrets.token_hex = lambda _size: collision_token
            copy_file_streaming(left, collision_destination, chunk_bytes)
        except FileExistsError:
            result["fixture"]["partial_collision_refused_without_deleting_foreign_path"] = (
                collision_partial.read_bytes() == collision_sentinel
                and not collision_destination.exists()
            )
        finally:
            secrets.token_hex = original_token_hex
        assert result["fixture"]["equal_file_matches"]
        assert result["fixture"]["same_size_one_byte_difference_rejected"]
        assert result["fixture"]["existing_destination_refused_without_change"]
        assert result["fixture"]["partial_collision_refused_without_deleting_foreign_path"]
        assert result["fixture"]["source_hash"] == result["fixture"]["equal_hash"]
        assert result["fixture"]["source_hash"] != result["fixture"]["unequal_hash"]
        assert result["fixture"]["boundary_term_case_insensitive_count"] == 2
        write_json_atomic(output, result)
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()
    if not args.self_test:
        parser.error("only the bounded self-test is enabled in this preauthorization tool")
    return args


def main() -> int:
    args = parse_args()
    return run_self_test(args.output)


if __name__ == "__main__":
    raise SystemExit(main())
