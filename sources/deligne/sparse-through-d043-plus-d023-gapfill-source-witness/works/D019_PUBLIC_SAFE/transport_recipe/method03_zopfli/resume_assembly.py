"""Resume only missing PDF assemblies from all 144 verified completed caches."""
from pathlib import Path
import gc, json, os, sys, time, zlib
import produce_zopfli as production
from pypdf import PdfReader
from verify_transport import accepted_inputs_unchanged

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent


def main():
    cursor = json.loads((BASE / 'TRANSPORT_CURSOR.json').read_text())
    marker = cursor['pdf_skill_operation_mark']
    if not (marker['completed'] and marker['exit_code'] == 0 and marker['operation'] == 'edit'
            and marker['expected_output_count'] == 2 and marker['output_format'] == 'pdf'):
        raise RuntimeError('existing successful PDF authoring marker required')
    accepted = accepted_inputs_unchanged()
    progress = json.loads((ROOT / 'PROGRESS.json').read_text())
    records = {row['pixel_sha256']: row for row in progress['images']}
    if len(progress['images']) != 144 or len(records) != 144:
        raise RuntimeError('completed unique cache inventory required')
    for key, row in records.items():
        payload = ROOT / row['path']
        raw = zlib.decompress(payload.read_bytes())
        if (production.filehash(payload) != row['sha256'] or payload.stat().st_size != row['bytes']
                or production.hashlib.sha256(raw).hexdigest().upper() != key
                or len(raw) != row['decoded_bytes'] or len(raw) != row['width'] * row['height']):
            raise RuntimeError('completed cache identity mismatch')
    del raw
    existing = {d['original']['path']: d for d in progress.get('documents', [])}
    progress['resumption'] = {'started_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                              'process_id': os.getpid(), 'completed_compression_reused': True,
                              'existing_authoring_marker_verified': marker, 'original_assembly_pid_not_live': True}
    progress['status'] = 'RESUMING_MISSING_ASSEMBLIES_FROM_VERIFIED_CACHE'
    progress['next_action'] = 'Complete only missing English assembly and replay, then all-page lossless verification.'
    production.dump(ROOT / 'PROGRESS.json', progress)
    documents = []
    for original in cursor['original_pdfs']:
        if original['path'] in existing:
            row = existing[original['path']]
            for item in (row, row['deterministic_replay']):
                pdf = BASE / item['path']
                if production.filehash(pdf) != item['sha256'] or pdf.stat().st_size != item['bytes']:
                    raise RuntimeError('completed PDF or replay changed')
                if len(PdfReader(pdf).pages) != original['pages']:
                    raise RuntimeError('completed PDF page count differs')
            if (row['sha256'], row['bytes']) != (row['deterministic_replay']['sha256'], row['deterministic_replay']['bytes']):
                raise RuntimeError('existing replay is not byte identical')
            documents.append(row)
            print(json.dumps({'reused_completed_document': row['path'], 'bytes': row['bytes']}), flush=True)
            continue
        row = production.build_document(original, records)
        progress['assembly_checkpoint'] = row
        production.dump(ROOT / 'PROGRESS.json', progress)
        print(json.dumps({'assembled': row['path'], 'bytes': row['bytes']}), flush=True)
        gc.collect()
        replay = production.build_document(original, records, replay=True)
        if (row['bytes'], row['sha256']) != (replay['bytes'], replay['sha256']):
            raise RuntimeError('deterministic replay PDF differs')
        documents.append({**row, 'deterministic_replay': replay})
        progress['documents'] = documents
        production.dump(ROOT / 'PROGRESS.json', progress)
        print(json.dumps({'replayed': replay['path'], 'bytes': replay['bytes'], 'sha256': replay['sha256']}), flush=True)
        gc.collect()
    accepted_inputs_unchanged()
    progress['documents'] = documents
    progress['status'] = 'COMPRESSION_AND_DETERMINISTIC_REPLAY_PASS__INDEPENDENT_VERIFICATION_PENDING'
    progress['next_action'] = 'Run method03_zopfli/verify_zopfli.py; validate native structure, text and all 309 raster pages.'
    production.dump(ROOT / 'PROGRESS.json', progress)
    production.dump(ROOT / 'METHOD_RECEIPT.json', {
        'schema': 'd019-zopfli-transport-method-v1', 'status': progress['status'], 'documents': documents,
        'encoded_streams': progress['images'], 'original_gate_inputs_unchanged': True,
        'accepted_inputs': accepted, 'resumption': progress['resumption'],
        'assembly_script_sha256': production.filehash(ROOT / 'resume_assembly.py'),
        'compression_and_build_script_sha256': production.filehash(ROOT / 'produce_zopfli.py')})


if __name__ == '__main__':
    main()
