"""Reserve a small Windows Job cap before importing PDF/image libraries."""
import ctypes
from ctypes import wintypes as w

class Basic(ctypes.Structure):
    _fields_ = [('times', ctypes.c_int64 * 2), ('flags', w.DWORD),
                ('minimum', ctypes.c_size_t), ('maximum', ctypes.c_size_t),
                ('processes', w.DWORD), ('affinity', ctypes.c_size_t),
                ('priority', w.DWORD), ('scheduling', w.DWORD)]

class Limits(ctypes.Structure):
    _fields_ = [('basic', Basic), ('io', ctypes.c_uint64 * 6),
                ('process_memory', ctypes.c_size_t), ('job_memory', ctypes.c_size_t),
                ('peak_process', ctypes.c_size_t), ('peak_job', ctypes.c_size_t)]

k = ctypes.windll.kernel32
k.CreateJobObjectW.argtypes = [ctypes.c_void_p, ctypes.c_wchar_p]
k.CreateJobObjectW.restype = ctypes.c_void_p
k.GetCurrentProcess.restype = ctypes.c_void_p
k.SetInformationJobObject.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, w.DWORD]
k.AssignProcessToJobObject.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
k.QueryInformationJobObject.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, w.DWORD, ctypes.c_void_p]

def reserve(limit=402653184):
    job = k.CreateJobObjectW(None, None); limits = Limits()
    limits.basic.flags = 0x200 | 0x2000; limits.job_memory = limit
    assert job and k.SetInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits))
    assert k.AssignProcessToJobObject(job, k.GetCurrentProcess()), 'fail closed before library imports'
    return job

def observed(job):
    value = Limits()
    assert k.QueryInformationJobObject(job,9,ctypes.byref(value),ctypes.sizeof(value),None)
    assert value.peak_job <= value.job_memory
    return {'job_memory_limit_bytes':value.job_memory, 'peak_job_memory_bytes':value.peak_job,
            'assigned_before_pdf_imports':True, 'subprocesses_launched':0}
