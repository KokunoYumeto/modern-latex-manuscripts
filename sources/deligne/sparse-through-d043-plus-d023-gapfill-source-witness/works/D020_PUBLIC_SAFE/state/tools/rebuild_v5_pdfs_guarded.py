#!/usr/bin/env python3
"""One-shot, mutex-serialized, 2 GiB Job-guarded D020 V5 PDF rebuild."""

from __future__ import annotations

import argparse
import ctypes
from ctypes import wintypes
import hashlib
import json
import os
import pathlib
import shutil
import subprocess
import sys
import time


sys.dont_write_bytecode = True

MUTEX_NAME = r"Global\InterlanguageTeXSlotV1"
JOB_MEMORY_LIMIT_BYTES = 2_147_483_648
JOB_OBJECT_LIMIT_JOB_MEMORY = 0x00000200
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x00002000
REQUIRED_LIMIT_FLAGS = JOB_OBJECT_LIMIT_JOB_MEMORY | JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
CREATE_SUSPENDED = 0x00000004
CREATE_NO_WINDOW = 0x08000000
CREATE_UNICODE_ENVIRONMENT = 0x00000400
CREATE_BREAKAWAY_FROM_JOB = 0x01000000
PROCESS_CREATION_FLAGS = CREATE_SUSPENDED | CREATE_NO_WINDOW | CREATE_UNICODE_ENVIRONMENT
WAIT_OBJECT_0 = 0x00000000
WAIT_ABANDONED_0 = 0x00000080
WAIT_TIMEOUT = 0x00000102
MAX_BOUNDED_WAIT_MS = 0xFFFFFFFE
STILL_ACTIVE = 259
JOB_OBJECT_BASIC_ACCOUNTING_INFORMATION_CLASS = 1
JOB_OBJECT_EXTENDED_LIMIT_INFORMATION_CLASS = 9
LAYERS = {
    "source_language": 35,
    "english_standalone": 35,
    "apparatus": 36,
}


if os.name != "nt":
    raise RuntimeError("This fail-closed launcher requires Windows Job Objects")


kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)


class STARTUPINFOW(ctypes.Structure):
    _fields_ = [
        ("cb", wintypes.DWORD),
        ("lpReserved", wintypes.LPWSTR),
        ("lpDesktop", wintypes.LPWSTR),
        ("lpTitle", wintypes.LPWSTR),
        ("dwX", wintypes.DWORD),
        ("dwY", wintypes.DWORD),
        ("dwXSize", wintypes.DWORD),
        ("dwYSize", wintypes.DWORD),
        ("dwXCountChars", wintypes.DWORD),
        ("dwYCountChars", wintypes.DWORD),
        ("dwFillAttribute", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("wShowWindow", wintypes.WORD),
        ("cbReserved2", wintypes.WORD),
        ("lpReserved2", ctypes.POINTER(ctypes.c_ubyte)),
        ("hStdInput", wintypes.HANDLE),
        ("hStdOutput", wintypes.HANDLE),
        ("hStdError", wintypes.HANDLE),
    ]


class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("hProcess", wintypes.HANDLE),
        ("hThread", wintypes.HANDLE),
        ("dwProcessId", wintypes.DWORD),
        ("dwThreadId", wintypes.DWORD),
    ]


class JOBOBJECT_BASIC_LIMIT_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("PerProcessUserTimeLimit", ctypes.c_longlong),
        ("PerJobUserTimeLimit", ctypes.c_longlong),
        ("LimitFlags", wintypes.DWORD),
        ("MinimumWorkingSetSize", ctypes.c_size_t),
        ("MaximumWorkingSetSize", ctypes.c_size_t),
        ("ActiveProcessLimit", wintypes.DWORD),
        ("Affinity", ctypes.c_size_t),
        ("PriorityClass", wintypes.DWORD),
        ("SchedulingClass", wintypes.DWORD),
    ]


class IO_COUNTERS(ctypes.Structure):
    _fields_ = [
        ("ReadOperationCount", ctypes.c_ulonglong),
        ("WriteOperationCount", ctypes.c_ulonglong),
        ("OtherOperationCount", ctypes.c_ulonglong),
        ("ReadTransferCount", ctypes.c_ulonglong),
        ("WriteTransferCount", ctypes.c_ulonglong),
        ("OtherTransferCount", ctypes.c_ulonglong),
    ]


class JOBOBJECT_EXTENDED_LIMIT_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("BasicLimitInformation", JOBOBJECT_BASIC_LIMIT_INFORMATION),
        ("IoInfo", IO_COUNTERS),
        ("ProcessMemoryLimit", ctypes.c_size_t),
        ("JobMemoryLimit", ctypes.c_size_t),
        ("PeakProcessMemoryUsed", ctypes.c_size_t),
        ("PeakJobMemoryUsed", ctypes.c_size_t),
    ]


class JOBOBJECT_BASIC_ACCOUNTING_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("TotalUserTime", ctypes.c_longlong),
        ("TotalKernelTime", ctypes.c_longlong),
        ("ThisPeriodTotalUserTime", ctypes.c_longlong),
        ("ThisPeriodTotalKernelTime", ctypes.c_longlong),
        ("TotalPageFaultCount", wintypes.DWORD),
        ("TotalProcesses", wintypes.DWORD),
        ("ActiveProcesses", wintypes.DWORD),
        ("TotalTerminatedProcesses", wintypes.DWORD),
    ]


kernel32.CreateJobObjectW.argtypes = [wintypes.LPVOID, wintypes.LPCWSTR]
kernel32.CreateJobObjectW.restype = wintypes.HANDLE
kernel32.SetInformationJobObject.argtypes = [
    wintypes.HANDLE,
    ctypes.c_int,
    wintypes.LPVOID,
    wintypes.DWORD,
]
kernel32.SetInformationJobObject.restype = wintypes.BOOL
kernel32.QueryInformationJobObject.argtypes = [
    wintypes.HANDLE,
    ctypes.c_int,
    wintypes.LPVOID,
    wintypes.DWORD,
    ctypes.POINTER(wintypes.DWORD),
]
kernel32.QueryInformationJobObject.restype = wintypes.BOOL
kernel32.CreateProcessW.argtypes = [
    wintypes.LPCWSTR,
    wintypes.LPWSTR,
    wintypes.LPVOID,
    wintypes.LPVOID,
    wintypes.BOOL,
    wintypes.DWORD,
    wintypes.LPVOID,
    wintypes.LPCWSTR,
    ctypes.POINTER(STARTUPINFOW),
    ctypes.POINTER(PROCESS_INFORMATION),
]
kernel32.CreateProcessW.restype = wintypes.BOOL
kernel32.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
kernel32.AssignProcessToJobObject.restype = wintypes.BOOL
kernel32.ResumeThread.argtypes = [wintypes.HANDLE]
kernel32.ResumeThread.restype = wintypes.DWORD
kernel32.WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]
kernel32.WaitForSingleObject.restype = wintypes.DWORD
kernel32.GetExitCodeProcess.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
kernel32.GetExitCodeProcess.restype = wintypes.BOOL
kernel32.TerminateJobObject.argtypes = [wintypes.HANDLE, wintypes.UINT]
kernel32.TerminateJobObject.restype = wintypes.BOOL
kernel32.TerminateProcess.argtypes = [wintypes.HANDLE, wintypes.UINT]
kernel32.TerminateProcess.restype = wintypes.BOOL
kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
kernel32.CloseHandle.restype = wintypes.BOOL
kernel32.CreateMutexW.argtypes = [wintypes.LPVOID, wintypes.BOOL, wintypes.LPCWSTR]
kernel32.CreateMutexW.restype = wintypes.HANDLE
kernel32.ReleaseMutex.argtypes = [wintypes.HANDLE]
kernel32.ReleaseMutex.restype = wintypes.BOOL


class GuardedLaunchError(RuntimeError):
    pass


class MutexTimeoutError(RuntimeError):
    pass


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def win_error(context: str) -> OSError:
    return ctypes.WinError(ctypes.get_last_error(), context)


def close_handle(handle: wintypes.HANDLE | None) -> None:
    if handle:
        kernel32.CloseHandle(handle)


def validate_bounded_wait(value: int, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= MAX_BOUNDED_WAIT_MS:
        raise ValueError(f"{label} must be a bounded Windows wait in 1..0xFFFFFFFE")
    return value


def configure_job(job: wintypes.HANDLE) -> None:
    limits = JOBOBJECT_EXTENDED_LIMIT_INFORMATION()
    limits.BasicLimitInformation.LimitFlags = REQUIRED_LIMIT_FLAGS
    limits.JobMemoryLimit = JOB_MEMORY_LIMIT_BYTES
    if not kernel32.SetInformationJobObject(
        job,
        JOB_OBJECT_EXTENDED_LIMIT_INFORMATION_CLASS,
        ctypes.byref(limits),
        ctypes.sizeof(limits),
    ):
        raise win_error("SetInformationJobObject")


def query_job(job: wintypes.HANDLE) -> dict:
    limits = JOBOBJECT_EXTENDED_LIMIT_INFORMATION()
    returned = wintypes.DWORD()
    if not kernel32.QueryInformationJobObject(
        job,
        JOB_OBJECT_EXTENDED_LIMIT_INFORMATION_CLASS,
        ctypes.byref(limits),
        ctypes.sizeof(limits),
        ctypes.byref(returned),
    ):
        raise win_error("QueryInformationJobObject(extended)")
    accounting = JOBOBJECT_BASIC_ACCOUNTING_INFORMATION()
    if not kernel32.QueryInformationJobObject(
        job,
        JOB_OBJECT_BASIC_ACCOUNTING_INFORMATION_CLASS,
        ctypes.byref(accounting),
        ctypes.sizeof(accounting),
        ctypes.byref(returned),
    ):
        raise win_error("QueryInformationJobObject(accounting)")
    return {
        "limit_flags": int(limits.BasicLimitInformation.LimitFlags),
        "job_memory_limit_bytes": int(limits.JobMemoryLimit),
        "peak_job_memory_used_bytes": int(limits.PeakJobMemoryUsed),
        "peak_process_memory_used_bytes": int(limits.PeakProcessMemoryUsed),
        "total_processes": int(accounting.TotalProcesses),
        "active_processes": int(accounting.ActiveProcesses),
        "terminated_processes": int(accounting.TotalTerminatedProcesses),
    }


def wait_for_job_empty(job: wintypes.HANDLE, timeout_ms: int) -> dict | None:
    """Poll exact Job accounting until every captured descendant has exited."""
    deadline = time.monotonic() + timeout_ms / 1000
    while True:
        stats = query_job(job)
        if stats["active_processes"] == 0:
            return stats
        if time.monotonic() >= deadline:
            return None
        time.sleep(0.05)


def ensure_process_stopped(process: wintypes.HANDLE, exit_code: int) -> None:
    """Fail closed for a created process that was never assigned to the Job."""
    state = kernel32.WaitForSingleObject(process, 0)
    if state == WAIT_OBJECT_0:
        return
    if state != WAIT_TIMEOUT:
        raise GuardedLaunchError(f"unexpected unassigned-process wait result {state}")
    terminated = bool(kernel32.TerminateProcess(process, exit_code))
    state = kernel32.WaitForSingleObject(process, 30_000)
    if state != WAIT_OBJECT_0:
        detail = "TerminateProcess failed" if not terminated else "termination wait timed out"
        raise GuardedLaunchError(f"unassigned suspended process cleanup failed: {detail}")


def terminate_job_and_confirm_empty(job: wintypes.HANDLE, exit_code: int) -> dict:
    """Terminate an assigned tree and prove that Job accounting reaches zero."""
    terminated = bool(kernel32.TerminateJobObject(job, exit_code))
    stats = wait_for_job_empty(job, 30_000)
    if stats is None:
        detail = "TerminateJobObject failed" if not terminated else "termination accounting timed out"
        raise GuardedLaunchError(f"assigned Job cleanup failed: {detail}")
    return stats


def environment_block(environment: dict[str, str]) -> ctypes.Array:
    pairs = [f"{key}={value}" for key, value in sorted(environment.items(), key=lambda item: item[0].upper())]
    return ctypes.create_unicode_buffer("\0".join(pairs) + "\0\0")


def run_guarded_tree(
    argv: list[str],
    *,
    cwd: pathlib.Path,
    timeout_ms: int,
    environment: dict[str, str] | None = None,
) -> dict:
    """Launch suspended, assign before resume, and wait for the entire Job tree."""
    if not argv:
        raise ValueError("empty argv")
    timeout_ms = validate_bounded_wait(timeout_ms, "timeout_ms")
    executable = pathlib.Path(argv[0]).resolve(strict=True)
    if not executable.is_file():
        raise GuardedLaunchError("executable is not a regular file")
    if PROCESS_CREATION_FLAGS & CREATE_BREAKAWAY_FROM_JOB:
        raise GuardedLaunchError("breakaway flag must remain disabled")
    cwd = cwd.resolve(strict=True)
    if not cwd.is_dir():
        raise GuardedLaunchError("working directory is not a directory")

    job = kernel32.CreateJobObjectW(None, None)
    if not job:
        raise win_error("CreateJobObjectW")
    process_info = PROCESS_INFORMATION()
    startup_info = STARTUPINFOW()
    startup_info.cb = ctypes.sizeof(startup_info)
    process_created = False
    assigned = False
    resumed = False
    timed_out = False
    tree_empty = False
    start = time.monotonic()
    try:
        configure_job(job)
        initial = query_job(job)
        if initial["job_memory_limit_bytes"] != JOB_MEMORY_LIMIT_BYTES:
            raise GuardedLaunchError("queried Job memory limit differs from required 2 GiB")
        if initial["limit_flags"] & REQUIRED_LIMIT_FLAGS != REQUIRED_LIMIT_FLAGS:
            raise GuardedLaunchError("queried Job flags omit a required fail-closed limit")

        command_line = ctypes.create_unicode_buffer(subprocess.list2cmdline([str(executable), *argv[1:]]))
        env = dict(os.environ if environment is None else environment)
        env_buffer = environment_block(env)
        if not kernel32.CreateProcessW(
            str(executable),
            command_line,
            None,
            None,
            False,
            PROCESS_CREATION_FLAGS,
            env_buffer,
            str(cwd),
            ctypes.byref(startup_info),
            ctypes.byref(process_info),
        ):
            raise win_error("CreateProcessW")
        process_created = True
        if not kernel32.AssignProcessToJobObject(job, process_info.hProcess):
            assignment_error = ctypes.get_last_error()
            ensure_process_stopped(process_info.hProcess, 0xE0000001)
            ctypes.set_last_error(assignment_error)
            raise win_error("AssignProcessToJobObject")
        assigned = True
        if kernel32.ResumeThread(process_info.hThread) == 0xFFFFFFFF:
            resume_error = ctypes.get_last_error()
            terminate_job_and_confirm_empty(job, 0xE0000002)
            ctypes.set_last_error(resume_error)
            raise win_error("ResumeThread")
        resumed = True
        close_handle(process_info.hThread)
        process_info.hThread = None

        wait_result = kernel32.WaitForSingleObject(process_info.hProcess, timeout_ms)
        if wait_result == WAIT_TIMEOUT:
            timed_out = True
            terminate_job_and_confirm_empty(job, 0xE0000003)
            if kernel32.WaitForSingleObject(process_info.hProcess, 30_000) != WAIT_OBJECT_0:
                raise GuardedLaunchError("root process did not signal after Job timeout termination")
        elif wait_result != WAIT_OBJECT_0:
            terminate_job_and_confirm_empty(job, 0xE0000004)
            raise GuardedLaunchError(f"unexpected process wait result {wait_result}")

        stats = wait_for_job_empty(job, 30_000)
        if stats is None:
            stats = terminate_job_and_confirm_empty(job, 0xE0000005)
        tree_empty = stats["active_processes"] == 0
        if not tree_empty:
            terminate_job_and_confirm_empty(job, 0xE0000007)
            raise GuardedLaunchError("Job still has active descendants after bounded shutdown")

        exit_code = wintypes.DWORD(STILL_ACTIVE)
        if not kernel32.GetExitCodeProcess(process_info.hProcess, ctypes.byref(exit_code)):
            raise win_error("GetExitCodeProcess")
        return {
            "exit_code": int(exit_code.value),
            "timed_out": timed_out,
            "elapsed_ms": round((time.monotonic() - start) * 1000),
            "creation_flags": PROCESS_CREATION_FLAGS,
            "created_suspended": bool(PROCESS_CREATION_FLAGS & CREATE_SUSPENDED),
            "assigned_before_resume": assigned and resumed,
            "breakaway_enabled": bool(PROCESS_CREATION_FLAGS & CREATE_BREAKAWAY_FROM_JOB),
            "kill_on_close": bool(stats["limit_flags"] & JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE),
            "job_memory_limit_enabled": bool(stats["limit_flags"] & JOB_OBJECT_LIMIT_JOB_MEMORY),
            "queried_job_memory_limit_bytes": stats["job_memory_limit_bytes"],
            "peak_job_memory_used_bytes": stats["peak_job_memory_used_bytes"],
            "peak_process_memory_used_bytes": stats["peak_process_memory_used_bytes"],
            "captured_processes": stats["total_processes"],
            "terminated_processes": stats["terminated_processes"],
            "active_processes_after_wait": stats["active_processes"],
            "tree_empty": tree_empty,
        }
    finally:
        if process_info.hThread:
            close_handle(process_info.hThread)
        if process_created and process_info.hProcess:
            if not tree_empty:
                if assigned:
                    terminate_job_and_confirm_empty(job, 0xE0000008)
                else:
                    ensure_process_stopped(process_info.hProcess, 0xE0000009)
            close_handle(process_info.hProcess)
        close_handle(job)


class NamedMutex:
    def __init__(self, name: str, timeout_ms: int):
        self.name = name
        self.timeout_ms = validate_bounded_wait(timeout_ms, "mutex timeout_ms")
        self.handle = None
        self.acquired = False
        self.abandoned = False
        self.released = False
        self.wait_ms = None

    def __enter__(self) -> "NamedMutex":
        self.handle = kernel32.CreateMutexW(None, False, self.name)
        if not self.handle:
            raise win_error("CreateMutexW")
        start = time.monotonic()
        result = kernel32.WaitForSingleObject(self.handle, self.timeout_ms)
        self.wait_ms = round((time.monotonic() - start) * 1000)
        if result == WAIT_TIMEOUT:
            close_handle(self.handle)
            self.handle = None
            raise MutexTimeoutError("bounded global TeX mutex acquisition timed out")
        if result not in (WAIT_OBJECT_0, WAIT_ABANDONED_0):
            close_handle(self.handle)
            self.handle = None
            raise GuardedLaunchError(f"unexpected mutex wait result {result}")
        self.acquired = True
        self.abandoned = result == WAIT_ABANDONED_0
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        if self.handle and self.acquired:
            if not kernel32.ReleaseMutex(self.handle):
                close_handle(self.handle)
                self.handle = None
                raise win_error("ReleaseMutex")
            self.released = True
        close_handle(self.handle)
        self.handle = None


def write_json_atomic(path: pathlib.Path, payload: dict) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def relative_file(path: pathlib.Path, root: pathlib.Path) -> dict:
    return {
        "path": path.relative_to(root).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": sha256(path),
    }


def count_pdf_images(pdf_path: pathlib.Path, page_index: int) -> int:
    from pypdf import PdfReader

    page = PdfReader(pdf_path).pages[page_index]

    def images_in_resources(resources, seen: set[tuple[int, int]]) -> int:
        if resources is None:
            return 0
        resources = resources.get_object()
        xobjects = resources.get("/XObject")
        if xobjects is None:
            return 0
        count = 0
        for reference in xobjects.get_object().values():
            identity = getattr(reference, "idnum", None), getattr(reference, "generation", None)
            if identity != (None, None) and identity in seen:
                continue
            if identity != (None, None):
                seen.add(identity)
            item = reference.get_object()
            subtype = item.get("/Subtype")
            if subtype == "/Image":
                count += 1
            elif subtype == "/Form":
                count += images_in_resources(item.get("/Resources"), seen)
        return count

    return images_in_resources(page.get("/Resources"), set())


def preflight(root: pathlib.Path) -> dict:
    expected_root = pathlib.Path(__file__).resolve().parents[1]
    if root.resolve() != expected_root:
        raise GuardedLaunchError("root must be this script's exact V5 workspace")
    counts = {}
    for layer in LAYERS:
        tex = root / "tex" / f"{layer}.tex"
        if not tex.is_file():
            raise GuardedLaunchError(f"missing TeX source for {layer}")
        text = tex.read_text(encoding="utf-8")
        counts[layer] = {
            "includegraphics": text.count(r"\includegraphics"),
            "asset_mentions": text.count("P0019-A01"),
        }
    if counts["source_language"] != {"includegraphics": 1, "asset_mentions": 1}:
        raise GuardedLaunchError("source-language lacets preflight failed")
    if counts["english_standalone"] != {"includegraphics": 1, "asset_mentions": 1}:
        raise GuardedLaunchError("English lacets preflight failed")
    if counts["apparatus"] != {"includegraphics": 0, "asset_mentions": 0}:
        raise GuardedLaunchError("apparatus asset exclusion preflight failed")
    assets = [
        root / "assets" / "raw_crops" / "P0019-A01_lacets_authority_raw.png",
        root / "assets" / "presentation_derivatives" / "P0019-A01_lacets_presentation.png",
    ]
    expected_hashes = [
        "EC8CF48C3C7A63EB7D3F0CF0B25C2D5B5FF0BA2FFF363FFA2718AAD65AA1FFE9",
        "CF35BC4099060AAD082618E35244F9560A0969AECE082F9770777F4EA4A6E6D9",
    ]
    for path, expected in zip(assets, expected_hashes):
        if not path.is_file() or sha256(path) != expected:
            raise GuardedLaunchError("P0019-A01 asset identity preflight failed")
    return {
        "tex": [relative_file(root / "tex" / f"{layer}.tex", root) for layer in LAYERS],
        "counts": counts,
        "assets": [relative_file(path, root) for path in assets],
    }


def verify_pdf_set(directory: pathlib.Path, expected: dict[str, str]) -> list[dict]:
    actual = sorted(path.name for path in directory.iterdir() if path.is_file())
    if actual != sorted(expected):
        raise GuardedLaunchError("promoted PDF directory has an unexpected file inventory")
    records = []
    for name in sorted(expected):
        path = directory / name
        digest = sha256(path)
        if digest != expected[name]:
            raise GuardedLaunchError(f"promoted byte identity differs for {name}")
        records.append({"name": name, "bytes": path.stat().st_size, "sha256": digest})
    return records


def promote_pdf_set(root: pathlib.Path, stage: pathlib.Path, staged_outputs: list[dict]) -> dict:
    """Promote all three PDFs by directory swap; preserve the prior set for recovery."""
    destination = root / "readers" / "pdf"
    promotion = root / "build" / "V5_PDF_PROMOTION"
    backup = root / "build" / "V4_PDF_PLACEHOLDER_BACKUP"
    failed = root / "build" / "V5_FAILED_PDF_PROMOTION"
    if not destination.is_dir():
        raise GuardedLaunchError("reader PDF destination is absent or not a directory")
    for path in (promotion, backup, failed):
        if path.exists():
            raise GuardedLaunchError(f"promotion control path already exists: {path.name}")
    expected = {pathlib.Path(item["path"]).name: item["sha256"] for item in staged_outputs}
    if sorted(expected) != sorted(f"{layer}.pdf" for layer in LAYERS):
        raise GuardedLaunchError("staged PDF promotion inventory is incomplete")

    promotion.mkdir(parents=True, exist_ok=False)
    for name in expected:
        shutil.copy2(stage / name, promotion / name)
    verify_pdf_set(promotion, expected)

    os.replace(destination, backup)
    try:
        os.replace(promotion, destination)
    except Exception:
        if not destination.exists() and backup.exists():
            os.replace(backup, destination)
        raise
    try:
        verified = verify_pdf_set(destination, expected)
    except Exception:
        if destination.exists() and not failed.exists():
            os.replace(destination, failed)
        if backup.exists() and not destination.exists():
            os.replace(backup, destination)
        raise
    return {
        "method": "same-volume_directory_swap",
        "mixed_set_window": False,
        "prior_set_preserved": backup.relative_to(root).as_posix(),
        "private_build_material": stage.relative_to(root).as_posix(),
        "promoted_files": verified,
    }


def production_main(root: pathlib.Path, mutex_timeout_ms: int, process_timeout_ms: int) -> int:
    mutex_timeout_ms = validate_bounded_wait(mutex_timeout_ms, "mutex_timeout_ms")
    process_timeout_ms = validate_bounded_wait(process_timeout_ms, "process_timeout_ms")
    root = root.resolve()
    receipt_path = root / "audit" / "V5_TEX_REBUILD_RECEIPT.json"
    stage = root / "build" / "V5_GUARDED_REBUILD"
    before = preflight(root)
    xelatex_text = shutil.which("xelatex")
    if not xelatex_text:
        raise GuardedLaunchError("xelatex executable not found")
    xelatex = pathlib.Path(xelatex_text).resolve(strict=True)
    if xelatex.name.lower() not in ("xelatex.exe", "xelatex"):
        raise GuardedLaunchError("resolved executable is not XeLaTeX")

    receipt = {
        "schema": "D020_V5_GUARDED_TEX_REBUILD_V1",
        "status": "PREPARED",
        "workspace": "work/S06_math_v5",
        "mutex": {
            "name": MUTEX_NAME,
            "timeout_ms": mutex_timeout_ms,
            "acquired": False,
            "abandoned_recovery": False,
            "released": False,
        },
        "job_contract": {
            "aggregate_job_memory_limit_bytes": JOB_MEMORY_LIMIT_BYTES,
            "job_memory_limit": True,
            "kill_on_close": True,
            "created_suspended": True,
            "assigned_before_resume": True,
            "breakaway_enabled": False,
            "process_timeout_ms": process_timeout_ms,
        },
        "xelatex": {
            "name": xelatex.name,
            "bytes": xelatex.stat().st_size,
            "sha256": sha256(xelatex),
        },
        "preflight": before,
        "passes": [],
        "outputs": [],
    }
    mutex = NamedMutex(MUTEX_NAME, mutex_timeout_ms)
    claimed = False
    try:
        with mutex:
            # This in-mutex claim is the authoritative one-shot check.  A
            # second invocation may have started earlier, but after waiting it
            # cannot clobber the first invocation's receipt or output state.
            control_paths = [
                receipt_path,
                stage,
                root / "build" / "V5_PDF_PROMOTION",
                root / "build" / "V4_PDF_PLACEHOLDER_BACKUP",
                root / "build" / "V5_FAILED_PDF_PROMOTION",
            ]
            existing = [path.name for path in control_paths if path.exists()]
            if existing:
                raise GuardedLaunchError("one-shot control path already exists: " + ",".join(existing))
            receipt["status"] = "RUNNING"
            receipt["mutex"].update(
                {
                    "acquired": mutex.acquired,
                    "abandoned_recovery": mutex.abandoned,
                    "wait_ms": mutex.wait_ms,
                }
            )
            stage.mkdir(parents=True, exist_ok=False)
            write_json_atomic(receipt_path, receipt)
            claimed = True
            environment = dict(os.environ)
            environment.update(
                {
                    "SOURCE_DATE_EPOCH": "0",
                    "FORCE_SOURCE_DATE": "1",
                    "TZ": "UTC",
                }
            )
            for layer in LAYERS:
                for pass_number in (1, 2):
                    argv = [
                        str(xelatex),
                        "-interaction=nonstopmode",
                        "-halt-on-error",
                        "-file-line-error",
                        "-no-shell-escape",
                        f"-output-directory={stage}",
                        f"{layer}.tex",
                    ]
                    result = run_guarded_tree(
                        argv,
                        cwd=root / "tex",
                        timeout_ms=process_timeout_ms,
                        environment=environment,
                    )
                    pass_receipt = {
                        "layer": layer,
                        "pass": pass_number,
                        "argv": [
                            "xelatex",
                            "-interaction=nonstopmode",
                            "-halt-on-error",
                            "-file-line-error",
                            "-no-shell-escape",
                            "-output-directory=<V5_STAGE>",
                            f"{layer}.tex",
                        ],
                        **result,
                    }
                    receipt["passes"].append(pass_receipt)
                    write_json_atomic(receipt_path, receipt)
                    if result["timed_out"] or result["exit_code"] != 0 or not result["tree_empty"]:
                        raise GuardedLaunchError(f"guarded XeLaTeX pass failed for {layer} pass {pass_number}")

            from pypdf import PdfReader

            staged_outputs = []
            for layer, expected_pages in LAYERS.items():
                pdf = stage / f"{layer}.pdf"
                log = stage / f"{layer}.log"
                if not pdf.is_file() or not log.is_file():
                    raise GuardedLaunchError(f"missing staged PDF or log for {layer}")
                pages = len(PdfReader(pdf).pages)
                if pages != expected_pages:
                    raise GuardedLaunchError(f"unexpected page count for {layer}: {pages}")
                log_text = log.read_text(encoding="utf-8", errors="replace")
                if "Output written on" not in log_text or "Emergency stop" in log_text:
                    raise GuardedLaunchError(f"immediate TeX log check failed for {layer}")
                images_on_lacets_page = count_pdf_images(pdf, 17) if layer != "apparatus" else 0
                if layer != "apparatus" and images_on_lacets_page < 1:
                    raise GuardedLaunchError(f"lacets image XObject absent on {layer} PDF page 18")
                staged_outputs.append(
                    {
                        **relative_file(pdf, root),
                        "pages": pages,
                        "page_18_image_xobjects": images_on_lacets_page,
                    }
                )
            promotion = promote_pdf_set(root, stage, staged_outputs)
            destination = root / "readers" / "pdf"
            receipt["outputs"] = [
                {
                    **relative_file(destination / f"{layer}.pdf", root),
                    "pages": expected_pages,
                    "page_18_image_xobjects": (
                        count_pdf_images(destination / f"{layer}.pdf", 17) if layer != "apparatus" else 0
                    ),
                }
                for layer, expected_pages in LAYERS.items()
            ]
            receipt["staged_outputs"] = staged_outputs
            receipt["promotion"] = promotion
            receipt["status"] = "BUILT_AND_PROMOTED_MUTEX_HELD"
            write_json_atomic(receipt_path, receipt)
        receipt["mutex"]["released"] = mutex.released
        if not mutex.released:
            raise GuardedLaunchError("global TeX mutex release was not confirmed")
        receipt["status"] = "PASS_REBUILD_NOT_AUDITED"
        write_json_atomic(receipt_path, receipt)
        print(json.dumps({"result": receipt["status"], "receipt": receipt_path.name}, sort_keys=True))
        return 0
    except Exception as error:
        if claimed:
            receipt["status"] = "FAIL"
            receipt["mutex"].update(
                {
                    "acquired": mutex.acquired,
                    "abandoned_recovery": mutex.abandoned,
                    "released": mutex.released,
                    "wait_ms": mutex.wait_ms,
                }
            )
            message = str(error).replace(str(root), "<V5_ROOT>").replace(str(xelatex), xelatex.name)
            receipt["failure"] = {"type": type(error).__name__, "message": message}
            write_json_atomic(receipt_path, receipt)
        raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1])
    parser.add_argument("--mutex-timeout-ms", type=int, default=1_200_000)
    parser.add_argument("--process-timeout-ms", type=int, default=1_200_000)
    args = parser.parse_args()
    try:
        validate_bounded_wait(args.mutex_timeout_ms, "mutex timeout")
        validate_bounded_wait(args.process_timeout_ms, "process timeout")
    except ValueError as error:
        parser.error(str(error))
    return args


if __name__ == "__main__":
    arguments = parse_args()
    raise SystemExit(
        production_main(arguments.root, arguments.mutex_timeout_ms, arguments.process_timeout_ms)
    )
