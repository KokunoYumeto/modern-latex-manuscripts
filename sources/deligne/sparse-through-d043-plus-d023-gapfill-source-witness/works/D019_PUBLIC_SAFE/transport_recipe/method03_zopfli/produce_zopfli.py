"""Bounded resumable exact-pixel Flate transport; never edits accepted sources."""
from pathlib import Path
import concurrent.futures, hashlib, json, os, sys, time, zlib

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent
sys.path.insert(0, str(ROOT / 'vendor'))
sys.path.insert(0, str(BASE))
from inspect_transport import filehash
from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject
import zopfli.zlib


def dump(path, value):
    data = json.dumps(value, sort_keys=True, indent=2) + '\n'
    temporary = path.with_name(path.name + '.writing')
    temporary.write_text(data, encoding='utf-8')
    temporary.replace(path)


def compress_row(row):
    start = time.monotonic()
    encoded = BASE / row['encoded_stream_path']
    if filehash(encoded) != row['encoded_sha256']:
        raise RuntimeError('method01 encoded stream identity mismatch')
    if row['params']:
        raise RuntimeError('unexpected predictor on method01 stream')
    raw = zlib.decompress(encoded.read_bytes())
    pixel_sha = hashlib.sha256(raw).hexdigest().upper()
    if pixel_sha != row['pixel_sha256'] or len(raw) != row['width'] * row['height']:
        raise RuntimeError('method01 decoded pixels mismatch')
    target = ROOT / 'encoded_streams' / (pixel_sha + '.flate')
    sidecar = target.with_suffix('.json')
    if sidecar.exists() and target.exists():
        record = json.loads(sidecar.read_text())
        candidate = target.read_bytes()
        if record['pixel_sha256'] != pixel_sha or filehash(target) != record['sha256'] or zlib.decompress(candidate) != raw:
            raise RuntimeError('resumption cache mismatch')
        return {**record, 'reused': True}
    if target.exists() or sidecar.exists():
        raise RuntimeError('incomplete cache pair preserved; choose separate derivative directory')
    candidate = zopfli.zlib.compress(raw, numiterations=1)
    if zlib.decompress(candidate) != raw:
        raise RuntimeError('Zopfli native decoded pixel mismatch')
    if len(candidate) >= encoded.stat().st_size:
        candidate = encoded.read_bytes()
        choice = 'verified_method01_flate'
    else:
        choice = 'zopfli_deflate_one_iteration'
    target.write_bytes(candidate)
    record = {'pixel_sha256': pixel_sha, 'width': row['width'], 'height': row['height'],
              'decoded_bytes': len(raw), 'original_encoded_bytes': row['bytes'],
              'bytes': len(candidate), 'sha256': filehash(target), 'choice': choice,
              'path': target.relative_to(ROOT).as_posix(), 'elapsed_seconds': round(time.monotonic()-start, 3)}
    dump(sidecar, record)
    return record


def build_document(original, records, replay=False):
    source = (BASE / original['path']).resolve()
    if source.stat().st_size != original['bytes'] or filehash(source) != original['sha256']:
        raise RuntimeError('canonical original changed')
    reader = PdfReader(source)
    writer = PdfWriter(clone_from=reader)
    images = []
    for obj in writer._objects:
        if obj is None or not hasattr(obj, 'get') or obj.get('/Subtype') != '/Image':
            continue
        if str(obj.get('/ColorSpace')) != '/DeviceGray' or int(obj.get('/BitsPerComponent', 0)) != 8 or '/SMask' in obj or '/Mask' in obj:
            raise RuntimeError('unexpected canonical image properties')
        raw = obj.get_data()
        key = hashlib.sha256(raw).hexdigest().upper()
        record = records[key]
        if len(raw) != record['decoded_bytes'] or int(obj['/Width']) != record['width'] or int(obj['/Height']) != record['height']:
            raise RuntimeError('native pixel dimensions changed')
        payload = ROOT / record['path']
        encoded = payload.read_bytes()
        if filehash(payload) != record['sha256'] or zlib.decompress(encoded) != raw:
            raise RuntimeError('final assembly decoded image mismatch')
        obj._data = encoded
        if hasattr(obj, 'decoded_self'):
            obj.decoded_self = None
        obj[NameObject('/Filter')] = NameObject('/FlateDecode')
        obj.pop('/DecodeParms', None)
        images.append(key)
    if len(images) != 144 or len(set(images)) != 144:
        raise RuntimeError('144 exact image identities required')
    folder = ROOT / ('replay' if replay else 'pdf')
    folder.mkdir(exist_ok=True)
    target = folder / source.name.replace('_CANONICAL.pdf', '_LOSSLESS_TRANSPORT.pdf')
    if target.exists():
        raise RuntimeError('refuse to overwrite existing derivative PDF')
    with target.open('wb') as stream:
        writer.write(stream)
    row = {'original': original, 'path': target.relative_to(BASE).as_posix(), 'bytes': target.stat().st_size,
           'sha256': filehash(target), 'pages': len(reader.pages), 'below_100000000_bytes': target.stat().st_size < 100000000,
           'image_count': len(images)}
    if not row['below_100000000_bytes']:
        raise RuntimeError('transport size target not met; preserve derivative')
    return row


def main():
    cursor = json.loads((BASE / 'TRANSPORT_CURSOR.json').read_text())
    from verify_transport import accepted_inputs_unchanged
    accepted = accepted_inputs_unchanged()
    if filehash(BASE.parent / 'receipts/D019_CANONICAL_FINAL_GATE.json') != cursor['accepted_content_gate_sha256']:
        raise RuntimeError('content gate identity mismatch')
    old = json.loads((BASE / 'method01_flate/METHOD_RECEIPT.json').read_text())
    rows = old['documents'][0]['image_streams']
    if len(rows) != 144:
        raise RuntimeError('method01 complete stream inventory required')
    (ROOT / 'encoded_streams').mkdir(exist_ok=True)
    progress = {'schema': 'd019-zopfli-transport-progress-v1', 'status': 'COMPRESSING', 'process_id': os.getpid(),
                'workers': 2, 'started_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                'accepted_inputs': accepted, 'recipe': 'Deterministic Zopfli zlib, one iteration, exact native grayscale pixels; retain method01 stream when smaller.',
                'prior_partial_caches_preserved': True, 'images': []}
    dump(ROOT / 'PROGRESS.json', progress)
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as pool:
        for record in pool.map(compress_row, rows, chunksize=1):
            progress['images'].append(record)
            dump(ROOT / 'PROGRESS.json', progress)
            print(json.dumps({'completed_images': len(progress['images']), 'of': 144, 'old': record['original_encoded_bytes'], 'new': record['bytes']}), flush=True)
    records = {row['pixel_sha256']: row for row in progress['images']}
    documents = []
    for original in cursor['original_pdfs']:
        row = build_document(original, records)
        replay = build_document(original, records, replay=True)
        if (row['bytes'], row['sha256']) != (replay['bytes'], replay['sha256']):
            raise RuntimeError('deterministic replay PDF differs')
        documents.append({**row, 'deterministic_replay': replay})
        progress['documents'] = documents
        dump(ROOT / 'PROGRESS.json', progress)
        print(json.dumps(row), flush=True)
    accepted_inputs_unchanged()
    progress['status'] = 'COMPRESSION_AND_DETERMINISTIC_REPLAY_PASS__INDEPENDENT_VERIFICATION_PENDING'
    progress['next_action'] = 'Run verify_zopfli.py nonpatchingly for all pages, all text and all native images.'
    dump(ROOT / 'PROGRESS.json', progress)
    dump(ROOT / 'METHOD_RECEIPT.json', {'schema': 'd019-zopfli-transport-method-v1', 'status': progress['status'], 'documents': documents,
                                     'encoded_streams': progress['images'], 'original_gate_inputs_unchanged': True})


if __name__ == '__main__':
    main()
