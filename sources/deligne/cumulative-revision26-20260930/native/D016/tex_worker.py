"""Serialized captured Windows TeX worker. Imported code never launches TeX.

Adapted from the hash-bound D019 worker; the caller holds one mutex through
every pass, deterministic replica and immediate log/convergence check.
"""
from __future__ import annotations

import ctypes
import os
import re
import subprocess
import time
from pathlib import Path

from d020_contract import Failure, require

MUTEX_NAME = "Global\\InterlanguageTeXSlotV1"
JOB_MEMORY_LIMIT_BYTES = 1_073_741_824
JOB_OBJECT_LIMIT_JOB_MEMORY = 0x00000200
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE = 0x00002000
JOB_OBJECT_LIMIT_ACTIVE_PROCESS = 0x00000008
ACTIVE_PROCESS_LIMIT = 6
CREATE_SUSPENDED = 0x00000004
CREATE_NO_WINDOW = 0x08000000


def job_memory_policy():
    """Stable receipt form of the fail-closed aggregate tree limit."""
    return {
        "mechanism": "WINDOWS_JOB_OBJECT_AGGREGATE_COMMIT_LIMIT",
        "job_memory_limit_bytes": JOB_MEMORY_LIMIT_BYTES,
        "job_memory_limit_gib": 1,
        "active_process_limit": ACTIVE_PROCESS_LIMIT,
        "kill_on_job_close": True,
        "root_created_suspended": True,
        "assigned_before_resume": True,
        "child_breakaway_allowed": False,
    }


class Mutex:
    def __init__(self, timeout_ms=600000):
        self.timeout_ms = timeout_ms
        self.acquired = False
        self.capture_state = "EMPTY"

    def __enter__(self):
        require(os.name == "nt", "Windows named mutex required")
        k = ctypes.windll.kernel32
        k.CreateMutexW.argtypes = [ctypes.c_void_p, ctypes.c_bool, ctypes.c_wchar_p]
        k.CreateMutexW.restype = ctypes.c_void_p
        k.WaitForSingleObject.argtypes = [ctypes.c_void_p, ctypes.c_uint32]
        k.WaitForSingleObject.restype = ctypes.c_uint32
        k.ReleaseMutex.argtypes = [ctypes.c_void_p]
        k.CloseHandle.argtypes = [ctypes.c_void_p]
        self.handle = k.CreateMutexW(None, False, MUTEX_NAME)
        require(bool(self.handle), "CreateMutex failed")
        started = time.monotonic()
        code = k.WaitForSingleObject(self.handle, self.timeout_ms)
        if code not in (0, 0x80):
            k.CloseHandle(self.handle)
            raise Failure("bounded TeX mutex acquisition failed")
        self.acquired = True
        self.abandoned = code == 0x80
        self.wait_ms = round((time.monotonic() - started) * 1000)
        return self

    def __exit__(self, *args):
        if self.acquired:
            # Never report an ordinary release after failed tree observation.
            # Retain the owned handle on the failing process; no second launch
            # can run in this worker. Process teardown is an abandoned recovery,
            # not a successful release. The private job remains kill-on-close.
            if self.capture_state != "EMPTY":
                _UNSAFE_OWNED_MUTEXES.append(self)
                raise Failure("captured-tree state unknown: ordinary TeX mutex release suppressed")
            ctypes.windll.kernel32.ReleaseMutex(self.handle)
            ctypes.windll.kernel32.CloseHandle(self.handle)
            self.acquired = False


_UNSAFE_OWNED_MUTEXES = []
_UNSAFE_CAPTURED_JOBS = []


def log_anomalies(text):
    patterns = {"errors": r"^!", "missing_glyphs": r"Missing character:", "overfull": r"Overfull ", "fatal": r"fatal error", "emergency": r"emergency stop"}
    return {key: len(re.findall(pattern, text, re.MULTILINE | re.IGNORECASE)) for key, pattern in patterns.items()}


def scan_log_anomalies(path):
    """Count TeX anomalies without retaining a full log in memory."""
    patterns = {key: re.compile(pattern, re.IGNORECASE) for key, pattern in {
        "errors": r"^!",
        "missing_glyphs": r"Missing character:",
        "overfull": r"Overfull ",
        "fatal": r"fatal error",
        "emergency": r"emergency stop",
    }.items()}
    counts = {key: 0 for key in patterns}
    with Path(path).open("r", encoding="utf-8", errors="replace") as stream:
        for line in stream:
            for key, pattern in patterns.items():
                counts[key] += bool(pattern.search(line))
    return counts


def tex_pass(mutex, engine, slot, name, environment, stdout_path, timeout_seconds=900):
    """Return only after the capped tree is empty; stdout streams to disk."""
    require(mutex.acquired, "TeX launch without continuously held mutex")
    require(Path(name).name == name and name in ("Deligne_EN.tex", "Deligne_FR.tex"), "unexpected TeX entrypoint")
    from ctypes import wintypes as w

    class Basic(ctypes.Structure):
        _fields_ = [("ProcessUserTimeLimit", ctypes.c_int64), ("JobUserTimeLimit", ctypes.c_int64), ("LimitFlags", w.DWORD), ("MinimumWorkingSetSize", ctypes.c_size_t), ("MaximumWorkingSetSize", ctypes.c_size_t), ("ActiveProcessLimit", w.DWORD), ("Affinity", ctypes.c_size_t), ("PriorityClass", w.DWORD), ("SchedulingClass", w.DWORD)]

    class IO(ctypes.Structure):
        _fields_ = [(x, ctypes.c_uint64) for x in ("ReadOperationCount", "WriteOperationCount", "OtherOperationCount", "ReadTransferCount", "WriteTransferCount", "OtherTransferCount")]

    class Extended(ctypes.Structure):
        _fields_ = [("BasicLimitInformation", Basic), ("IoInfo", IO), ("ProcessMemoryLimit", ctypes.c_size_t), ("JobMemoryLimit", ctypes.c_size_t), ("PeakProcessMemoryUsed", ctypes.c_size_t), ("PeakJobMemoryUsed", ctypes.c_size_t)]

    class Accounting(ctypes.Structure):
        _fields_ = [(x, ctypes.c_int64) for x in ("TotalUserTime", "TotalKernelTime", "ThisPeriodTotalUserTime", "ThisPeriodTotalKernelTime")] + [(x, w.DWORD) for x in ("TotalPageFaultCount", "TotalProcesses", "ActiveProcesses", "TotalTerminatedProcesses")]

    k, n = ctypes.windll.kernel32, ctypes.windll.ntdll
    k.CreateJobObjectW.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p]
    k.CreateJobObjectW.restype = ctypes.c_void_p
    k.SetInformationJobObject.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, w.DWORD]
    k.SetInformationJobObject.restype = w.BOOL
    k.AssignProcessToJobObject.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    k.AssignProcessToJobObject.restype = w.BOOL
    k.QueryInformationJobObject.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, w.DWORD, ctypes.c_void_p]
    k.QueryInformationJobObject.restype = w.BOOL
    k.TerminateJobObject.argtypes = [ctypes.c_void_p, w.UINT]
    k.TerminateJobObject.restype = w.BOOL
    k.CloseHandle.argtypes = [ctypes.c_void_p]
    n.NtResumeProcess.argtypes = [ctypes.c_void_p]
    n.NtResumeProcess.restype = ctypes.c_long
    job = k.CreateJobObjectW(None, None)
    require(bool(job), "CreateJobObject failed")
    proc = None
    assigned = False
    started = time.monotonic()

    def empty_job(timeout=30):
        deadline = time.monotonic() + timeout
        while True:
            accounting = Accounting()
            require(k.QueryInformationJobObject(job, 1, ctypes.byref(accounting), ctypes.sizeof(accounting), None), "captured-tree observation failure")
            if accounting.ActiveProcesses == 0:
                return accounting
            require(time.monotonic() < deadline, "captured descendants remain active")
            time.sleep(0.1)

    def memory_snapshot():
        limits = Extended()
        require(k.QueryInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits), None), "captured job memory observation failure")
        require(limits.JobMemoryLimit == JOB_MEMORY_LIMIT_BYTES, "captured job memory policy changed")
        require(limits.BasicLimitInformation.ActiveProcessLimit == ACTIVE_PROCESS_LIMIT, "captured job process policy changed")
        require(limits.BasicLimitInformation.LimitFlags & JOB_OBJECT_LIMIT_ACTIVE_PROCESS, "captured job process limit disabled")
        return int(limits.PeakJobMemoryUsed)

    try:
        limits = Extended()
        limits.BasicLimitInformation.LimitFlags = JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE | JOB_OBJECT_LIMIT_JOB_MEMORY | JOB_OBJECT_LIMIT_ACTIVE_PROCESS
        limits.BasicLimitInformation.ActiveProcessLimit = ACTIVE_PROCESS_LIMIT
        limits.JobMemoryLimit = JOB_MEMORY_LIMIT_BYTES
        require(k.SetInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits)), "captured job memory/cleanup policy failed")
        env = os.environ.copy()
        env.update(environment)
        # Arm mutex fail-closure before process creation. CREATE_SUSPENDED means
        # neither the root nor any descendant can execute before assignment.
        mutex.capture_state = "ARMED"
        stdout_path = Path(stdout_path)
        require(not stdout_path.exists(), "TeX stdout destination already exists")
        with stdout_path.open("xb") as capture:
            proc = subprocess.Popen([str(engine), "-no-shell-escape", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", name], cwd=slot, env=env, stdin=subprocess.DEVNULL, stdout=capture, stderr=subprocess.STDOUT, creationflags=CREATE_SUSPENDED | CREATE_NO_WINDOW)
            assigned = bool(k.AssignProcessToJobObject(job, ctypes.c_void_p(int(proc._handle))))
            require(assigned, "captured-tree assignment failed before resume")
            mutex.capture_state = "ACTIVE"
            require(n.NtResumeProcess(ctypes.c_void_p(int(proc._handle))) == 0, "captured process resume failed")
            proc.wait(timeout=timeout_seconds)
        accounting = empty_job()
        peak_job_memory = memory_snapshot()
        require(peak_job_memory <= JOB_MEMORY_LIMIT_BYTES, "captured job exceeded enforced memory limit")
        require(accounting.TotalProcesses <= ACTIVE_PROCESS_LIMIT, "captured process count exceeded limit")
        return {"return_code": proc.returncode, "captured_processes": accounting.TotalProcesses, "active_descendants_at_return": 0, "elapsed_seconds": round(time.monotonic()-started, 3), "memory_policy": job_memory_policy(), "peak_job_memory_bytes": peak_job_memory, "stdout_anomalies": scan_log_anomalies(stdout_path)}
    finally:
        cleanup_confirmed = False
        try:
            if assigned:
                require(k.TerminateJobObject(job, 1), "captured job termination failed")
                empty_job()
            if proc is not None:
                if proc.poll() is None:
                    # This can only be our suspended unassigned process or root.
                    proc.kill()
                proc.wait(timeout=30)
            cleanup_confirmed = True
            mutex.capture_state = "EMPTY"
        finally:
            if cleanup_confirmed:
                k.CloseHandle(job)
            else:
                mutex.capture_state = "UNKNOWN"
                # Do not discard the only captured-tree/slot ownership state.
                # This worker must terminate as failed; no normal release or
                # retry occurs. Kill-on-close also applies at process teardown.
                _UNSAFE_CAPTURED_JOBS.append(job)
