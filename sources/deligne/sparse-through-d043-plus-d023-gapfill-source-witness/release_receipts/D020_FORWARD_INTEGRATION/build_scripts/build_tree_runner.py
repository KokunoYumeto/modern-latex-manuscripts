"""Fail-closed outer Windows Job runner for D020 build and QA stages.

The production CLI accepts only allowlisted D020 stages and constructs the exact
allowlisted child command itself. Command output and environment values are
never written to its receipt. Imported code launches nothing.
"""
from __future__ import annotations

import argparse
import ctypes
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

from d020_contract import Failure, TASK, identity, reject_reparse, require

OUTER_JOB_MEMORY_LIMIT_BYTES = 1_342_177_280
JOB_OBJECT_LIMIT_JOB_MEMORY = 0x00000200
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x00002000
JOB_OBJECT_LIMIT_ACTIVE_PROCESS = 0x00000008
ACTIVE_PROCESS_LIMIT = 10
CREATE_SUSPENDED = 0x00000004
CREATE_NO_WINDOW = 0x08000000
BUILD_TIMEOUT_SECONDS = 21_600
QA_TIMEOUT_SECONDS = 7_200
PREPARE_TIMEOUT_SECONDS = 3_600
FINALIZE_TIMEOUT_SECONDS = 14_400
PACKAGE_TIMEOUT_SECONDS = 43_200
BUNDLED_PYTHON_SHA256 = "7679E53FA969789309E81FDAD0D52B8CDA5F83C9ABF7CB31A3C58BF24B31E264"

SCRIPTS = Path(__file__).resolve().parent
BUILD_SCRIPT = SCRIPTS / "build_d020_integration.py"
FINALIZE_SCRIPT = SCRIPTS / "finalize_manifest_nonregression.py"
PACKAGE_SCRIPT = SCRIPTS / "package_d020_release.py"
SANITIZE_SCRIPT = SCRIPTS / "sanitize_d020_public_receipts.py"
PROBE_CHILD = SCRIPTS / "outer_job_probe_child.py"


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def bundled_python():
    path = reject_reparse(Path(os.environ["USERPROFILE"]) / "miniconda3/python.exe").resolve(strict=True)
    require(sha256(path) == BUNDLED_PYTHON_SHA256, "bundled Python identity mismatch")
    return path


def outer_job_policy():
    return {
        "mechanism": "WINDOWS_JOB_OBJECT_AGGREGATE_COMMIT_LIMIT",
        "job_memory_limit_bytes": OUTER_JOB_MEMORY_LIMIT_BYTES,
        "job_memory_limit_gib": 1.25,
        "active_process_limit": ACTIVE_PROCESS_LIMIT,
        "kill_on_job_close": True,
        "target_created_suspended": True,
        "assigned_before_resume": True,
        "child_breakaway_allowed": False,
    }


def production_receipt(stage):
    require(stage in ("preflight", "prepare", "build", "qa", "qa_retry01", "qa_retry02", "qa_retry03", "sanitize", "sanitize_retry01", "finalize", "finalize_retry01", "finalize_retry02", "finalize_retry03", "package"), "outer runner stage is not allowlisted")
    public_stage = {
        "qa_retry01": "QA_RETRY01",
        "qa_retry02": "QA_RETRY02",
        "qa_retry03": "QA_RETRY03",
        "finalize_retry01": "FINALIZE_RETRY01",
        "finalize_retry02": "FINALIZE_RETRY02",
        "finalize_retry03": "FINALIZE_RETRY03",
        "sanitize_retry01": "SANITIZE_RETRY01",
    }.get(stage, stage.upper())
    return TASK / "build/cumulative/audit" / f"D020_OUTER_{public_stage}_JOB_RECEIPT.json"


def _write_receipt(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    reject_reparse(path.parent)
    path.write_text(json.dumps(value, ensure_ascii=True, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _validate_command(command, profile, probe_receipt=None):
    python = bundled_python()
    build = reject_reparse(BUILD_SCRIPT).resolve(strict=True)
    resolved = [str(Path(command[0]).resolve()), str(Path(command[1]).resolve()), *command[2:]]
    if profile in ("preflight", "prepare", "build", "qa", "qa_retry01", "qa_retry02", "qa_retry03"):
        expected = [str(python), str(build), "qa" if profile.startswith("qa_retry") else profile]
    elif profile in ("sanitize", "sanitize_retry01"):
        build = reject_reparse(SANITIZE_SCRIPT).resolve(strict=True)
        expected = [str(python), str(build)]
    elif profile in ("finalize", "finalize_retry01", "finalize_retry02", "finalize_retry03"):
        build = reject_reparse(FINALIZE_SCRIPT).resolve(strict=True)
        expected = [str(python), str(build)]
    elif profile == "package":
        build = reject_reparse(PACKAGE_SCRIPT).resolve(strict=True)
        cumulative = TASK / "build/cumulative"
        expected = [
            str(python), str(build),
            "--source-tree", str((cumulative / "source_tree").resolve()),
            "--provenance-tree", str((cumulative / "provenance_tree").resolve()),
            "--inherited-d033-provenance", str((cumulative / "provenance_tree/inherited/DELIGNE_PROVENANCE_AUDIT_D033_GAPFILL.zip").resolve()),
            "--release-directory", str((cumulative / "release").resolve()),
            "--payload-manifest", str((cumulative / "D020_RELEASE_PAYLOAD_MANIFEST.json").resolve()),
        ]
    elif profile == "nested_job_probe":
        require(probe_receipt is not None, "probe receipt is required")
        probe = reject_reparse(PROBE_CHILD).resolve(strict=True)
        expected = [str(python), str(probe), str(Path(probe_receipt).resolve())]
    else:
        raise Failure("unknown outer Job allowlist profile")
    require(resolved == expected, "outer Job command does not match exact allowlist")
    return python, Path(resolved[1])


def _failure_code(exc):
    if isinstance(exc, subprocess.TimeoutExpired):
        return "BOUNDED_WALL_TIMEOUT"
    if isinstance(exc, Failure):
        return "FAIL_CLOSED_CONTRACT"
    return "RUNNER_OPERATION_FAILED"


def _run_allowlisted(command, receipt_path, profile, timeout_seconds, probe_receipt=None):
    """Run one exact command in an outer 1.25 GiB Job and write a sanitized receipt."""
    require(os.name == "nt", "outer Windows Job runner requires Windows")
    require(isinstance(timeout_seconds, int) and 0 < timeout_seconds <= PACKAGE_TIMEOUT_SECONDS, "invalid bounded wall timeout")
    receipt_path = Path(receipt_path).absolute()
    require(not receipt_path.exists(), "outer Job receipt destination must be absent")
    python, target = _validate_command(command, profile, probe_receipt)
    policy = outer_job_policy()
    receipt = {
        "schema": "d020-outer-process-tree-job-v1",
        "status": "RUNNING",
        "started_utc": now(),
        "allowlist_profile": profile,
        "stage": profile if profile in ("preflight", "prepare", "build", "qa", "qa_retry01", "qa_retry02", "qa_retry03", "sanitize", "sanitize_retry01", "finalize", "finalize_retry01", "finalize_retry02", "finalize_retry03", "package") else "NON_TEX_NESTED_JOB_PROBE",
        "wall_timeout_seconds": timeout_seconds,
        "memory_policy": policy,
        "interpreter": {"name": python.name, **identity(python)},
        "target_script": {"name": target.name, **identity(target)},
        "command_output_recorded": False,
        "environment_recorded": False,
        "tree_empty": False,
        "zero_descendants_remain": False,
    }
    _write_receipt(receipt_path, receipt)

    from ctypes import wintypes as w

    class Basic(ctypes.Structure):
        _fields_ = [("ProcessUserTimeLimit", ctypes.c_int64), ("JobUserTimeLimit", ctypes.c_int64), ("LimitFlags", w.DWORD), ("MinimumWorkingSetSize", ctypes.c_size_t), ("MaximumWorkingSetSize", ctypes.c_size_t), ("ActiveProcessLimit", w.DWORD), ("Affinity", ctypes.c_size_t), ("PriorityClass", w.DWORD), ("SchedulingClass", w.DWORD)]

    class IO(ctypes.Structure):
        _fields_ = [(name, ctypes.c_uint64) for name in ("ReadOperationCount", "WriteOperationCount", "OtherOperationCount", "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]

    class Extended(ctypes.Structure):
        _fields_ = [("BasicLimitInformation", Basic), ("IoInfo", IO), ("ProcessMemoryLimit", ctypes.c_size_t), ("JobMemoryLimit", ctypes.c_size_t), ("PeakProcessMemoryUsed", ctypes.c_size_t), ("PeakJobMemoryUsed", ctypes.c_size_t)]

    class Accounting(ctypes.Structure):
        _fields_ = [(name, ctypes.c_int64) for name in ("TotalUserTime", "TotalKernelTime", "ThisPeriodTotalUserTime", "ThisPeriodTotalKernelTime")] + [(name, w.DWORD) for name in ("TotalPageFaultCount", "TotalProcesses", "ActiveProcesses", "TotalTerminatedProcesses")]

    kernel, ntdll = ctypes.windll.kernel32, ctypes.windll.ntdll
    kernel.CreateJobObjectW.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p]
    kernel.CreateJobObjectW.restype = ctypes.c_void_p
    kernel.SetInformationJobObject.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, w.DWORD]
    kernel.SetInformationJobObject.restype = w.BOOL
    kernel.AssignProcessToJobObject.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    kernel.AssignProcessToJobObject.restype = w.BOOL
    kernel.QueryInformationJobObject.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, w.DWORD, ctypes.c_void_p]
    kernel.QueryInformationJobObject.restype = w.BOOL
    kernel.TerminateJobObject.argtypes = [ctypes.c_void_p, w.UINT]
    kernel.TerminateJobObject.restype = w.BOOL
    kernel.CloseHandle.argtypes = [ctypes.c_void_p]
    kernel.CloseHandle.restype = w.BOOL
    ntdll.NtResumeProcess.argtypes = [ctypes.c_void_p]
    ntdll.NtResumeProcess.restype = ctypes.c_long

    job = None
    proc = None
    assigned = False
    natural_empty = False
    cleanup_empty = False
    peak = None
    captured = None
    observed_limit = None
    operation_error = None
    cleanup_error = None

    def query_accounting():
        value = Accounting()
        require(kernel.QueryInformationJobObject(job, 1, ctypes.byref(value), ctypes.sizeof(value), None), "outer Job accounting query failed")
        return value

    def wait_empty(seconds):
        deadline = time.monotonic() + seconds
        while True:
            value = query_accounting()
            if value.ActiveProcesses == 0:
                return value
            require(time.monotonic() < deadline, "outer Job descendants did not become empty")
            time.sleep(0.05)

    def query_memory():
        value = Extended()
        require(kernel.QueryInformationJobObject(job, 9, ctypes.byref(value), ctypes.sizeof(value), None), "outer Job memory query failed")
        return value

    try:
        job = kernel.CreateJobObjectW(None, None)
        require(bool(job), "outer CreateJobObject failed")
        limits = Extended()
        limits.BasicLimitInformation.LimitFlags = JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE | JOB_OBJECT_LIMIT_JOB_MEMORY | JOB_OBJECT_LIMIT_ACTIVE_PROCESS
        limits.BasicLimitInformation.ActiveProcessLimit = ACTIVE_PROCESS_LIMIT
        limits.JobMemoryLimit = OUTER_JOB_MEMORY_LIMIT_BYTES
        require(kernel.SetInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits)), "outer Job memory/cleanup policy failed")
        proc = subprocess.Popen(command, cwd=SCRIPTS, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, creationflags=CREATE_SUSPENDED | CREATE_NO_WINDOW)
        assigned = bool(kernel.AssignProcessToJobObject(job, ctypes.c_void_p(int(proc._handle))))
        require(assigned, "outer Job assignment failed before resume")
        require(ntdll.NtResumeProcess(ctypes.c_void_p(int(proc._handle))) == 0, "outer target resume failed")
        proc.communicate(timeout=timeout_seconds)
        accounting = wait_empty(30)
        natural_empty = True
        captured = int(accounting.TotalProcesses)
    except Exception as exc:
        operation_error = exc
    finally:
        try:
            if assigned:
                require(kernel.TerminateJobObject(job, 1), "outer Job termination failed")
                accounting = wait_empty(30)
                cleanup_empty = accounting.ActiveProcesses == 0
                captured = int(accounting.TotalProcesses)
            elif proc is not None:
                if proc.poll() is None:
                    proc.kill()
                proc.wait(timeout=30)
                cleanup_empty = True
            elif job is not None:
                cleanup_empty = query_accounting().ActiveProcesses == 0
            if job is not None:
                memory = query_memory()
                observed_limit = int(memory.JobMemoryLimit)
                peak = int(memory.PeakJobMemoryUsed)
                require(observed_limit == OUTER_JOB_MEMORY_LIMIT_BYTES, "outer queried memory limit differs")
                require(memory.BasicLimitInformation.ActiveProcessLimit == ACTIVE_PROCESS_LIMIT, "outer queried process limit differs")
                require(memory.BasicLimitInformation.LimitFlags & JOB_OBJECT_LIMIT_ACTIVE_PROCESS, "outer process limit disabled")
                require(peak <= OUTER_JOB_MEMORY_LIMIT_BYTES, "outer observed peak exceeds enforced limit")
        except Exception as exc:
            cleanup_error = exc
        finally:
            if job is not None:
                if not kernel.CloseHandle(job) and cleanup_error is None:
                    cleanup_error = Failure("outer Job handle close failed")
            if proc is not None and proc.poll() is None:
                try:
                    proc.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait(timeout=30)

    success = operation_error is None and cleanup_error is None and proc is not None and proc.returncode == 0 and natural_empty and cleanup_empty
    receipt.update(
        status="PASS" if success else "FAIL",
        completed_utc=now(),
        target_exit_code=None if proc is None else proc.returncode,
        queried_job_memory_limit_bytes=observed_limit,
        peak_job_memory_bytes=peak,
        captured_processes=captured,
        tree_empty=natural_empty,
        zero_descendants_remain=cleanup_empty,
        cleanup_status="PASS" if cleanup_error is None and cleanup_empty else "FAIL",
    )
    if not success:
        failure = operation_error or cleanup_error or Failure("allowlisted target returned nonzero")
        receipt.update(failure_code=_failure_code(failure), failure_type=type(failure).__name__)
    _write_receipt(receipt_path, receipt)
    return receipt


def run_stage(stage):
    require(Path(sys.executable).resolve() == bundled_python(), "outer runner itself must use bundled Python")
    require(stage in ("preflight", "prepare", "build", "qa", "qa_retry01", "qa_retry02", "qa_retry03", "sanitize", "sanitize_retry01", "finalize", "finalize_retry01", "finalize_retry02", "finalize_retry03", "package"), "outer runner stage is not allowlisted")
    timeout = {
        "preflight": PREPARE_TIMEOUT_SECONDS,
        "prepare": PREPARE_TIMEOUT_SECONDS,
        "build": BUILD_TIMEOUT_SECONDS,
        "qa": QA_TIMEOUT_SECONDS,
        "qa_retry01": QA_TIMEOUT_SECONDS,
        "qa_retry02": QA_TIMEOUT_SECONDS,
        "qa_retry03": QA_TIMEOUT_SECONDS,
        "sanitize": PREPARE_TIMEOUT_SECONDS,
        "sanitize_retry01": PREPARE_TIMEOUT_SECONDS,
        "finalize": FINALIZE_TIMEOUT_SECONDS,
        "finalize_retry01": FINALIZE_TIMEOUT_SECONDS,
        "finalize_retry02": FINALIZE_TIMEOUT_SECONDS,
        "finalize_retry03": FINALIZE_TIMEOUT_SECONDS,
        "package": PACKAGE_TIMEOUT_SECONDS,
    }[stage]
    if stage in ("preflight", "prepare", "build", "qa", "qa_retry01", "qa_retry02", "qa_retry03"):
        command = [str(bundled_python()), str(BUILD_SCRIPT.resolve()), "qa" if stage.startswith("qa_retry") else stage]
    elif stage in ("sanitize", "sanitize_retry01"):
        command = [str(bundled_python()), str(SANITIZE_SCRIPT.resolve())]
    elif stage in ("finalize", "finalize_retry01", "finalize_retry02", "finalize_retry03"):
        command = [str(bundled_python()), str(FINALIZE_SCRIPT.resolve())]
    else:
        cumulative = TASK / "build/cumulative"
        command = [
            str(bundled_python()), str(PACKAGE_SCRIPT.resolve()),
            "--source-tree", str((cumulative / "source_tree").resolve()),
            "--provenance-tree", str((cumulative / "provenance_tree").resolve()),
            "--inherited-d033-provenance", str((cumulative / "provenance_tree/inherited/DELIGNE_PROVENANCE_AUDIT_D033_GAPFILL.zip").resolve()),
            "--release-directory", str((cumulative / "release").resolve()),
            "--payload-manifest", str((cumulative / "D020_RELEASE_PAYLOAD_MANIFEST.json").resolve()),
        ]
    return _run_allowlisted(command, production_receipt(stage), stage, timeout)


def run_nested_probe(probe_root):
    """Test-only Windows nested-Job probe; never acquires the TeX mutex."""
    require(Path(sys.executable).resolve() == bundled_python(), "nested probe must use bundled Python")
    probe_root = Path(probe_root).absolute()
    require(probe_root.is_dir() and not any(probe_root.iterdir()), "probe root must be an empty existing directory")
    outer_receipt = probe_root / "outer_probe_receipt.json"
    inner_receipt = probe_root / "inner_probe_receipt.json"
    command = [str(bundled_python()), str(PROBE_CHILD.resolve()), str(inner_receipt.resolve())]
    outer = _run_allowlisted(command, outer_receipt, "nested_job_probe", 60, inner_receipt)
    require(inner_receipt.is_file(), "nested probe child receipt missing")
    inner = json.loads(inner_receipt.read_text(encoding="utf-8"))
    return {"outer": outer, "inner": inner}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=("preflight", "prepare", "build", "qa", "qa_retry01", "qa_retry02", "qa_retry03", "sanitize", "sanitize_retry01", "finalize", "finalize_retry01", "finalize_retry02", "finalize_retry03", "package"))
    args = parser.parse_args()
    result = run_stage(args.stage)
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
