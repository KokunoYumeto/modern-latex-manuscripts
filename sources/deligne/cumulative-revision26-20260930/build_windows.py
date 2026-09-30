"""Bounded fresh build; preserve old attempts, without retry or installation.

Hold the TeX mutex through all passes, postprocessing and log checks. Compare
canonical PDFs, not uninitialized bilevel padding in raw engine output.
Repair: OpenAI Codex, GPT-6.1 Sol, Ultra effort.
"""
from pathlib import Path
import datetime as dt
import hashlib, json, shutil, subprocess, sys
from tex_worker import Mutex, tex_pass, scan_log_anomalies

MAX_PASSES = 4

def identity(path):
    with path.open('rb') as stream:
        sha = hashlib.file_digest(stream, 'sha256').hexdigest().upper()
    return {'bytes': path.stat().st_size, 'sha256': sha}

def postprocess(root, source, destination=None):
    command = [sys.executable, str(root / 'pdf_postprocess.py'), str(source)]
    if destination is not None:
        command.append(str(destination))
    result = subprocess.run(command, cwd=root, stdin=subprocess.DEVNULL,
                            capture_output=True, text=True, timeout=120,
                            creationflags=subprocess.CREATE_NO_WINDOW)
    if result.returncode:
        raise RuntimeError('Capped PDF postprocessor failed: ' + result.stderr[-2000:])
    return json.loads(result.stdout)

def run_build(root, lanes, engine, runner=tex_pass, normalizer=postprocess,
              mutex_factory=Mutex, log_check=scan_log_anomalies):
    receipt_path = root / 'BUILD_RECEIPT.json'
    if receipt_path.exists():
        raise RuntimeError('Preserve the prior attempt; use a fresh extraction.')
    if not lanes or len(lanes) != len(set(lanes)) or not set(lanes) <= {'EN', 'FR'}:
        raise ValueError('Select each of EN and FR at most once.')
    receipt = {'schema': 'deligne-portable-build-v2', 'status': 'BUILD_RUNNING',
               'started_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
               'maximum_passes_per_lane': MAX_PASSES, 'documents': [],
               'mutex_released': False,
               'postprocessor_source': identity(root / 'canonicalize_bilevel_padding.py')}
    def save():
        receipt_path.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    save()
    mutex = None
    try:
        if not engine:
            raise RuntimeError('XeLaTeX is unavailable; no installation attempted.')
        for lane in lanes:
            for suffix in ('.aux', '.toc', '.out', '.log', '.pdf', '_deterministic.pdf'):
                if (root / f'Deligne_{lane}{suffix}').exists():
                    raise RuntimeError('Use a fresh output directory: inherited engine output '
                                       f'Deligne_{lane}{suffix} must remain preserved.')
        mutex = mutex_factory(timeout_ms=30000)
        with mutex:
            receipt['mutex'] = {'name': 'Global\\InterlanguageTeXSlotV1',
                                'wait_ms': mutex.wait_ms, 'abandoned': mutex.abandoned}
            save()
            for lane in lanes:
                record = {'lane': lane, 'passes': []}
                receipt['documents'].append(record)
                for number in range(1, MAX_PASSES + 1):
                    result = runner(mutex, engine, root, f'Deligne_{lane}.tex',
                                    {'SOURCE_DATE_EPOCH': '946684800',
                                     'FORCE_SOURCE_DATE': '1', 'TZ': 'UTC',
                                     'MIKTEX_ENABLE_INSTALLER': '0'},
                                    root / f'build_{lane}_{number}.stdout', 900)
                    record['passes'].append(result)
                    save()
                    if result['return_code'] != 0:
                        raise RuntimeError(f'Engine failed in {lane} pass {number}.')
                    result['raw_pdf'] = identity(root / f'Deligne_{lane}.pdf')
                    result['toc'] = identity(root / f'Deligne_{lane}.toc')
                    result['canonical_pdf'] = normalizer(root, root / f'Deligne_{lane}.pdf')
                    save()
                    if number >= 3:
                        previous = record['passes'][-2]
                        current_pdf, old_pdf = result['canonical_pdf'], previous['canonical_pdf']
                        if (current_pdf['bytes'], current_pdf['sha256'], result['toc']) == \
                                (old_pdf['bytes'], old_pdf['sha256'], previous['toc']):
                            break
                else:
                    raise RuntimeError(f'{lane} did not converge within {MAX_PASSES} passes.')
                record['log_anomalies'] = log_check(root / f'Deligne_{lane}.log')
                if any(record['log_anomalies'][key] for key in
                       ('errors', 'missing_glyphs', 'fatal', 'emergency')):
                    raise RuntimeError(f'{lane} log quality gate failed.')
                target = root / f'Deligne_{lane}_deterministic.pdf'
                final = normalizer(root, root / f'Deligne_{lane}.pdf', target)
                if (final['bytes'], final['sha256']) != \
                        (result['canonical_pdf']['bytes'], result['canonical_pdf']['sha256']):
                    raise RuntimeError('Final serialization differs from the convergence check.')
                record['accepted_pdf'] = {'path': target.name, **identity(target)}
                save()
        receipt['mutex_released'] = True
        receipt['status'] = 'CONVERGED_BUILD_PASS'
    except BaseException as error:
        if mutex is not None and 'mutex' in receipt and not mutex.acquired:
            receipt['mutex_released'] = True
        receipt['status'] = 'BUILD_FAILED_NO_ACCEPTANCE'
        receipt['failure'] = {'type': type(error).__name__, 'detail': str(error)[:2000]}
        save()
        raise
    finally:
        receipt['ended_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
        save()
    return receipt

if __name__ == '__main__':
    run_build(Path(__file__).resolve().parent, sys.argv[1:] or ['EN', 'FR'],
              shutil.which('xelatex'))
