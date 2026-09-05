#!/usr/bin/env python3
"""Run one harmless non-TeX Python check in a fail-closed 256 MiB Job."""
from __future__ import annotations

import argparse
import ctypes
from ctypes import wintypes
import json
import os
import pathlib
import subprocess
import sys
import time


sys.dont_write_bytecode = True

JOB_MEMORY_LIMIT_BYTES = 268_435_456
JOB_OBJECT_LIMIT_JOB_MEMORY = 0x00000200
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x00002000
REQUIRED_LIMIT_FLAGS = JOB_OBJECT_LIMIT_JOB_MEMORY | JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
CREATE_SUSPENDED = 0x00000004
CREATE_NO_WINDOW = 0x08000000
CREATE_UNICODE_ENVIRONMENT = 0x00000400
CREATE_BREAKAWAY_FROM_JOB = 0x01000000
PROCESS_CREATION_FLAGS = CREATE_SUSPENDED | CREATE_NO_WINDOW | CREATE_UNICODE_ENVIRONMENT
WAIT_OBJECT_0 = 0x00000000
WAIT_TIMEOUT = 0x00000102
STILL_ACTIVE = 259
JOB_OBJECT_BASIC_ACCOUNTING_INFORMATION_CLASS = 1
JOB_OBJECT_EXTENDED_LIMIT_INFORMATION_CLASS = 9


if os.name != "nt":
    raise RuntimeError("this fail-closed launcher requires Windows Job Objects")


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
kernel32.SetInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, wintypes.LPVOID, wintypes.DWORD]
kernel32.SetInformationJobObject.restype = wintypes.BOOL
kernel32.QueryInformationJobObject.argtypes = [wintypes.HANDLE, ctypes.c_int, wintypes.LPVOID, wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)]
kernel32.QueryInformationJobObject.restype = wintypes.BOOL
kernel32.CreateProcessW.argtypes = [wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.LPVOID, wintypes.LPVOID, wintypes.BOOL, wintypes.DWORD, wintypes.LPVOID, wintypes.LPCWSTR, ctypes.POINTER(STARTUPINFOW), ctypes.POINTER(PROCESS_INFORMATION)]
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


def win_error(context: str) -> OSError:
    return ctypes.WinError(ctypes.get_last_error(), context)


def close_handle(handle) -> None:
    if handle:
        kernel32.CloseHandle(handle)


def query_job(job) -> dict:
    limits = JOBOBJECT_EXTENDED_LIMIT_INFORMATION()
    accounting = JOBOBJECT_BASIC_ACCOUNTING_INFORMATION()
    returned = wintypes.DWORD()
    if not kernel32.QueryInformationJobObject(job, JOB_OBJECT_EXTENDED_LIMIT_INFORMATION_CLASS, ctypes.byref(limits), ctypes.sizeof(limits), ctypes.byref(returned)):
        raise win_error("QueryInformationJobObject(extended)")
    if not kernel32.QueryInformationJobObject(job, JOB_OBJECT_BASIC_ACCOUNTING_INFORMATION_CLASS, ctypes.byref(accounting), ctypes.sizeof(accounting), ctypes.byref(returned)):
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


def wait_job_empty(job, timeout_ms: int) -> dict | None:
    deadline = time.monotonic() + timeout_ms / 1000
    while True:
        stats = query_job(job)
        if stats["active_processes"] == 0:
            return stats
        if time.monotonic() >= deadline:
            return None
        time.sleep(0.05)


def ensure_process_stopped(process, exit_code: int) -> None:
    state = kernel32.WaitForSingleObject(process, 0)
    if state == WAIT_OBJECT_0:
        return
    if state != WAIT_TIMEOUT:
        raise RuntimeError(f"unexpected unassigned-process wait result {state}")
    if not kernel32.TerminateProcess(process, exit_code):
        raise win_error("TerminateProcess(unassigned)")
    if kernel32.WaitForSingleObject(process, 30_000) != WAIT_OBJECT_0:
        raise RuntimeError("unassigned process did not terminate within bounded cleanup")


def terminate_job_and_confirm_empty(job, exit_code: int) -> dict:
    if not kernel32.TerminateJobObject(job, exit_code):
        raise win_error("TerminateJobObject")
    stats = wait_job_empty(job, 30_000)
    if stats is None or stats["active_processes"] != 0:
        raise RuntimeError("Job did not reach zero active processes within bounded cleanup")
    return stats


def environment_block(environment: dict[str, str]):
    pairs = [f"{key}={value}" for key, value in sorted(environment.items(), key=lambda item: item[0].upper())]
    return ctypes.create_unicode_buffer("\0".join(pairs) + "\0\0")


def write_json_atomic(path: pathlib.Path, payload: dict) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def run_guarded(argv: list[str], cwd: pathlib.Path, timeout_ms: int) -> dict:
    if not argv:
        raise ValueError("empty argv")
    if not 1 <= timeout_ms <= 300_000:
        raise ValueError("timeout_ms must be bounded to 1..300000")
    if PROCESS_CREATION_FLAGS & CREATE_BREAKAWAY_FROM_JOB:
        raise RuntimeError("breakaway must remain disabled")
    executable = pathlib.Path(argv[0]).resolve(strict=True)
    cwd = cwd.resolve(strict=True)
    job = kernel32.CreateJobObjectW(None, None)
    if not job:
        raise win_error("CreateJobObjectW")
    process_info = PROCESS_INFORMATION()
    startup = STARTUPINFOW()
    startup.cb = ctypes.sizeof(startup)
    created = assigned = resumed = tree_empty = False
    start = time.monotonic()
    try:
        limits = JOBOBJECT_EXTENDED_LIMIT_INFORMATION()
        limits.BasicLimitInformation.LimitFlags = REQUIRED_LIMIT_FLAGS
        limits.JobMemoryLimit = JOB_MEMORY_LIMIT_BYTES
        if not kernel32.SetInformationJobObject(job, JOB_OBJECT_EXTENDED_LIMIT_INFORMATION_CLASS, ctypes.byref(limits), ctypes.sizeof(limits)):
            raise win_error("SetInformationJobObject")
        initial = query_job(job)
        if initial["job_memory_limit_bytes"] != JOB_MEMORY_LIMIT_BYTES or initial["limit_flags"] & REQUIRED_LIMIT_FLAGS != REQUIRED_LIMIT_FLAGS:
            raise RuntimeError("low-memory Job contract was not installed")

        command_line = ctypes.create_unicode_buffer(subprocess.list2cmdline([str(executable), *argv[1:]]))
        environment = dict(os.environ)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        environment["PYTHONHASHSEED"] = "0"
        env_buffer = environment_block(environment)
        if not kernel32.CreateProcessW(str(executable), command_line, None, None, False, PROCESS_CREATION_FLAGS, env_buffer, str(cwd), ctypes.byref(startup), ctypes.byref(process_info)):
            raise win_error("CreateProcessW")
        created = True
        if not kernel32.AssignProcessToJobObject(job, process_info.hProcess):
            assignment_error = ctypes.get_last_error()
            ensure_process_stopped(process_info.hProcess, 0xE1000001)
            tree_empty = True
            ctypes.set_last_error(assignment_error)
            raise win_error("AssignProcessToJobObject")
        assigned = True
        if kernel32.ResumeThread(process_info.hThread) == 0xFFFFFFFF:
            resume_error = ctypes.get_last_error()
            terminate_job_and_confirm_empty(job, 0xE1000002)
            tree_empty = True
            ctypes.set_last_error(resume_error)
            raise win_error("ResumeThread")
        resumed = True
        close_handle(process_info.hThread)
        process_info.hThread = None

        wait_result = kernel32.WaitForSingleObject(process_info.hProcess, timeout_ms)
        timed_out = wait_result == WAIT_TIMEOUT
        if timed_out:
            terminate_job_and_confirm_empty(job, 0xE1000003)
            if kernel32.WaitForSingleObject(process_info.hProcess, 30_000) != WAIT_OBJECT_0:
                raise RuntimeError("root process did not signal after Job timeout cleanup")
        elif wait_result != WAIT_OBJECT_0:
            terminate_job_and_confirm_empty(job, 0xE1000004)
            tree_empty = True
            raise RuntimeError(f"unexpected process wait result {wait_result}")
        stats = wait_job_empty(job, 30_000)
        if stats is None:
            stats = terminate_job_and_confirm_empty(job, 0xE1000005)
        if stats["active_processes"] != 0:
            raise RuntimeError("guarded tree failed to reach zero active processes")
        tree_empty = True
        exit_code = wintypes.DWORD(STILL_ACTIVE)
        if not kernel32.GetExitCodeProcess(process_info.hProcess, ctypes.byref(exit_code)):
            raise win_error("GetExitCodeProcess")
        return {
            "exit_code": int(exit_code.value),
            "timed_out": timed_out,
            "elapsed_ms": round((time.monotonic() - start) * 1000),
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
        primary_exception = sys.exc_info()[1]
        cleanup_error = None
        try:
            if process_info.hThread:
                close_handle(process_info.hThread)
        except BaseException as exc:
            cleanup_error = exc
        try:
            if created and process_info.hProcess:
                try:
                    if not tree_empty:
                        if assigned:
                            terminate_job_and_confirm_empty(job, 0xE1000006)
                        else:
                            ensure_process_stopped(process_info.hProcess, 0xE1000007)
                finally:
                    close_handle(process_info.hProcess)
        except BaseException as exc:
            if cleanup_error is None:
                cleanup_error = exc
        try:
            close_handle(job)
        except BaseException as exc:
            if cleanup_error is None:
                cleanup_error = exc
        if cleanup_error is not None:
            if primary_exception is not None:
                raise cleanup_error from primary_exception
            raise cleanup_error


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", type=pathlib.Path, required=True)
    parser.add_argument("--timeout-ms", type=int, default=120_000)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.command and args.command[0] == "--":
        args.command = args.command[1:]
    if not args.command:
        parser.error("a child command is required after --")
    return args


def main() -> int:
    args = parse_args()
    cwd = pathlib.Path.cwd()
    result = run_guarded(args.command, cwd, args.timeout_ms)
    payload = {
        "schema": "D020_LOW_MEMORY_JOB_GUARD_RECEIPT_V1",
        "status": "PASS" if result["exit_code"] == 0 and not result["timed_out"] and result["tree_empty"] else "FAIL",
        "contract": {
            "aggregate_job_memory_limit_bytes": JOB_MEMORY_LIMIT_BYTES,
            "created_suspended": True,
            "assigned_before_resume": True,
            "breakaway_enabled": False,
            "kill_on_close": True,
            "timeout_ms": args.timeout_ms,
        },
        "command": ["<PYTHON>" if index == 0 else value for index, value in enumerate(args.command)],
        "result": result,
    }
    write_json_atomic(args.receipt, payload)
    if payload["status"] != "PASS":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
