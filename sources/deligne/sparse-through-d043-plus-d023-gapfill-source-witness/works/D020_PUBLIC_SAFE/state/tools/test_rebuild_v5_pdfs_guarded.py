#!/usr/bin/env python3
"""Harmless non-TeX tests for the D020 V5 guarded rebuild launcher."""

import importlib.util
import json
import os
import pathlib
import sys
import tempfile


sys.dont_write_bytecode = True
ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "rebuild_v5_pdfs_guarded.py"
spec = importlib.util.spec_from_file_location("d020_v5_guard", SCRIPT)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


assert guard.JOB_MEMORY_LIMIT_BYTES == 2_147_483_648
assert guard.PROCESS_CREATION_FLAGS & guard.CREATE_SUSPENDED
assert not guard.PROCESS_CREATION_FLAGS & guard.CREATE_BREAKAWAY_FROM_JOB
assert guard.REQUIRED_LIMIT_FLAGS & guard.JOB_OBJECT_LIMIT_JOB_MEMORY
assert guard.REQUIRED_LIMIT_FLAGS & guard.JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE

preflight = guard.preflight(ROOT)
assert preflight["counts"]["source_language"] == {"includegraphics": 1, "asset_mentions": 1}
assert preflight["counts"]["english_standalone"] == {"includegraphics": 1, "asset_mentions": 1}
assert preflight["counts"]["apparatus"] == {"includegraphics": 0, "asset_mentions": 0}

results = []
with tempfile.TemporaryDirectory(prefix="d020_v5_guard_test_") as temporary:
    cwd = pathlib.Path(temporary)
    simple = guard.run_guarded_tree(
        [sys.executable, "-B", "-c", "raise SystemExit(0)"],
        cwd=cwd,
        timeout_ms=30_000,
    )
    results.append(simple)

    nested_code = (
        "import subprocess,sys; "
        "raise SystemExit(subprocess.run([sys.executable,'-B','-c','raise SystemExit(0)']).returncode)"
    )
    nested = guard.run_guarded_tree(
        [sys.executable, "-B", "-c", nested_code],
        cwd=cwd,
        timeout_ms=30_000,
    )
    results.append(nested)

    nonzero = guard.run_guarded_tree(
        [sys.executable, "-B", "-c", "raise SystemExit(7)"],
        cwd=cwd,
        timeout_ms=30_000,
    )
    results.append(nonzero)

    timed_out = guard.run_guarded_tree(
        [sys.executable, "-B", "-c", "import time; time.sleep(60)"],
        cwd=cwd,
        timeout_ms=200,
    )

for result in results:
    assert result["created_suspended"] is True
    assert result["assigned_before_resume"] is True
    assert result["breakaway_enabled"] is False
    assert result["kill_on_close"] is True
    assert result["job_memory_limit_enabled"] is True
    assert result["queried_job_memory_limit_bytes"] == 2_147_483_648
    assert result["peak_job_memory_used_bytes"] > 0
    assert result["active_processes_after_wait"] == 0
    assert result["tree_empty"] is True
    assert result["timed_out"] is False

assert timed_out["created_suspended"] is True
assert timed_out["assigned_before_resume"] is True
assert timed_out["breakaway_enabled"] is False
assert timed_out["kill_on_close"] is True
assert timed_out["job_memory_limit_enabled"] is True
assert timed_out["queried_job_memory_limit_bytes"] == 2_147_483_648
assert timed_out["active_processes_after_wait"] == 0
assert timed_out["tree_empty"] is True
assert timed_out["timed_out"] is True

assert simple["exit_code"] == 0
assert simple["captured_processes"] >= 1
assert nested["exit_code"] == 0
assert nested["captured_processes"] >= 2
assert nonzero["exit_code"] == 7
for invalid_timeout in (0, 0xFFFFFFFF, 0x100000000):
    for callable_with_invalid_timeout in (
        lambda value=invalid_timeout: guard.run_guarded_tree(
            [sys.executable, "-B", "-c", "raise SystemExit(0)"],
            cwd=pathlib.Path.cwd(),
            timeout_ms=value,
        ),
        lambda value=invalid_timeout: guard.NamedMutex("Global\\D020V5InvalidWaitTest", value),
        lambda value=invalid_timeout: guard.production_main(ROOT, value, 1),
        lambda value=invalid_timeout: guard.production_main(ROOT, 1, value),
    ):
        try:
            callable_with_invalid_timeout()
        except ValueError:
            pass
        else:
            raise AssertionError(f"unbounded/invalid timeout was accepted: {invalid_timeout}")

isolated_mutex = guard.NamedMutex(f"Global\\D020V5GuardSelfTest_{os.getpid()}", 5_000)
with isolated_mutex:
    assert isolated_mutex.acquired is True
    assert isolated_mutex.abandoned is False
assert isolated_mutex.released is True

source = SCRIPT.read_text(encoding="utf-8")
mutex_scope_start = source.index("with mutex:")
first_production_launch = source.index("result = run_guarded_tree(", mutex_scope_start)
last_log_check = source.index('"Emergency stop" in log_text', first_production_launch)
mutex_scope_end = source.index('receipt["mutex"]["released"]', last_log_check)
assert mutex_scope_start < first_production_launch < last_log_check < mutex_scope_end
pass_status = source.index('receipt["status"] = "PASS_REBUILD_NOT_AUDITED"', mutex_scope_end)
assert pass_status > mutex_scope_end
in_mutex_claim = source.index("control_paths = [", mutex_scope_start)
assert mutex_scope_start < in_mutex_claim < first_production_launch


def make_promotion_fixture(base: pathlib.Path) -> tuple[pathlib.Path, pathlib.Path, list[dict]]:
    root = base
    stage = root / "build" / "V5_GUARDED_REBUILD"
    destination = root / "readers" / "pdf"
    stage.mkdir(parents=True)
    destination.mkdir(parents=True)
    (destination / "old-placeholder.pdf").write_bytes(b"old")
    outputs = []
    for layer in guard.LAYERS:
        pdf = stage / f"{layer}.pdf"
        pdf.write_bytes((layer + "-new").encode("ascii"))
        outputs.append(
            {
                "path": pdf.relative_to(root).as_posix(),
                "bytes": pdf.stat().st_size,
                "sha256": guard.sha256(pdf),
            }
        )
    (stage / "private.log").write_text("must stay private", encoding="utf-8")
    return root, stage, outputs


with tempfile.TemporaryDirectory(prefix="d020_v5_promotion_test_") as temporary:
    promotion_root, promotion_stage, promotion_outputs = make_promotion_fixture(pathlib.Path(temporary))
    promotion_result = guard.promote_pdf_set(promotion_root, promotion_stage, promotion_outputs)
    destination = promotion_root / "readers" / "pdf"
    assert sorted(path.name for path in destination.iterdir()) == sorted(
        f"{layer}.pdf" for layer in guard.LAYERS
    )
    assert not (destination / "private.log").exists()
    assert (promotion_root / "build" / "V4_PDF_PLACEHOLDER_BACKUP" / "old-placeholder.pdf").is_file()
    assert promotion_result["method"] == "same-volume_directory_swap"

with tempfile.TemporaryDirectory(prefix="d020_v5_rollback_test_") as temporary:
    rollback_root, rollback_stage, rollback_outputs = make_promotion_fixture(pathlib.Path(temporary))
    original_replace = guard.os.replace
    replace_calls = 0

    def fail_second_replace(source_path, destination_path):
        global replace_calls
        replace_calls += 1
        if replace_calls == 2:
            raise OSError("injected second-swap failure")
        return original_replace(source_path, destination_path)

    guard.os.replace = fail_second_replace
    try:
        try:
            guard.promote_pdf_set(rollback_root, rollback_stage, rollback_outputs)
        except OSError as error:
            assert "injected" in str(error)
        else:
            raise AssertionError("injected promotion failure was not propagated")
    finally:
        guard.os.replace = original_replace
    restored = rollback_root / "readers" / "pdf" / "old-placeholder.pdf"
    assert restored.read_bytes() == b"old"

print(
    json.dumps(
        {
            "result": "PASS",
            "tests": 13,
            "harmless_process_trees": 4,
            "nested_captured_processes": nested["captured_processes"],
            "peak_job_memory_used_bytes_max": max(
                result["peak_job_memory_used_bytes"] for result in [*results, timed_out]
            ),
            "queried_job_memory_limit_bytes": simple["queried_job_memory_limit_bytes"],
            "timeout_tree_empty": timed_out["tree_empty"],
            "isolated_mutex_api_test": "PASS",
            "live_mutex_invoked": False,
            "transactional_pdf_set_promotion": "PASS",
            "injected_second_swap_rollback": "PASS",
            "invalid_waits_rejected_without_mutex_api": [0, 4294967295, 4294967296],
            "tex_engine_launched": False,
        },
        sort_keys=True,
    )
)
