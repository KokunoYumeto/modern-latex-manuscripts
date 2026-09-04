"""Nonpatching complete semantic and every-page lossless transport validation."""
from pathlib import Path
import collections, gc, hashlib, io, json, os, platform, shutil, struct, subprocess, sys, time, zlib
ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent
sys.path.insert(0, str(BASE))
from inspect_transport import filehash
from verify_transport import accepted_inputs_unchanged, compare_structure, digest
from pypdf import PdfReader
from pypdf.generic import ArrayObject, DictionaryObject, IndirectObject, StreamObject
from PIL import Image
import pypdf, PIL
import verify_transport as legacy_verifier


def exact_native_gray(obj):
    """Decode exact grayscale pixels with zlib/libpng; never resample or re-encode."""
    if str(obj.get('/Filter')) != '/FlateDecode' or str(obj.get('/ColorSpace')) != '/DeviceGray' or int(obj.get('/BitsPerComponent', 0)) != 8:
        raise RuntimeError('native decoder requires Flate DeviceGray 8-bit image')
    if '/Mask' in obj or '/SMask' in obj or obj.get('/ImageMask'):
        raise RuntimeError('native decoder does not admit masks')
    width, height = int(obj['/Width']), int(obj['/Height'])
    params = obj.get('/DecodeParms') or {}
    if isinstance(params, IndirectObject):
        params = params.get_object()
    predictor = int(params.get('/Predictor', 1))
    raw = zlib.decompress(obj._data)
    if predictor == 1:
        if len(raw) != width * height:
            raise RuntimeError('plain grayscale decoded byte count')
        return raw
    if not 10 <= predictor <= 15 or int(params.get('/Colors', 1)) != 1 or int(params.get('/Columns', 1)) != width or int(params.get('/BitsPerComponent', 8)) != 8:
        raise RuntimeError('unsupported image predictor parameters')
    if len(raw) != height * (width + 1) or any(raw[y * (width + 1)] > 4 for y in range(height)):
        raise RuntimeError('PNG predictor row dimensions or filter invalid')
    def chunk(kind, data):
        return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data) & 0xffffffff)
    png = (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 0, 0, 0, 0))
           + chunk(b'IDAT', obj._data) + chunk(b'IEND', b''))
    with Image.open(io.BytesIO(png)) as image:
        if image.mode != 'L' or image.size != (width, height):
            raise RuntimeError('native PNG decoder altered image properties')
        result = image.tobytes()
    if len(result) != width * height:
        raise RuntimeError('native PNG decoder byte count')
    return result


legacy_verifier.decoded_image = exact_native_gray


def dump(path, value):
    temporary = path.with_name(path.name + '.writing')
    temporary.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)


def identity(path):
    return {'path': path.relative_to(BASE).as_posix(), 'bytes': path.stat().st_size, 'sha256': filehash(path)}


def semantic_graph(original, candidate):
    readers = [PdfReader(original), PdfReader(candidate)]
    page_lists = [list(reader.pages) for reader in readers]
    if len(page_lists[0]) != len(page_lists[1]):
        raise RuntimeError('ordered page count changed')
    page_maps = [{(p.indirect_reference.idnum, p.indirect_reference.generation): n for n, p in enumerate(pages)} for pages in page_lists]
    visited, left_map, right_map = set(), {}, {}
    stats = collections.Counter()

    def walk(a, b, location):
        if isinstance(a, IndirectObject) and isinstance(b, IndirectObject):
            ka, kb = (a.idnum, a.generation), (b.idnum, b.generation)
            if ka in page_maps[0] or kb in page_maps[1]:
                if page_maps[0].get(ka) != page_maps[1].get(kb):
                    raise RuntimeError('page destination/reference changed at ' + location)
                stats['normalized_page_references'] += 1
                return
            if ka in left_map and left_map[ka] != kb or kb in right_map and right_map[kb] != ka:
                raise RuntimeError('indirect-object alias correspondence changed at ' + location)
            left_map[ka], right_map[kb] = kb, ka
            pair = (ka, kb)
            if pair in visited:
                return
            visited.add(pair)
            stats['indirect_object_pairs'] += 1
            return walk(a.get_object(), b.get_object(), location)
        if isinstance(a, IndirectObject) or isinstance(b, IndirectObject):
            raise RuntimeError('indirect/direct object topology changed at ' + location)
        if isinstance(a, StreamObject) or isinstance(b, StreamObject):
            if not isinstance(a, StreamObject) or not isinstance(b, StreamObject):
                raise RuntimeError('stream object type changed at ' + location)
            aa = exact_native_gray(a) if a.get('/Subtype') == '/Image' else a.get_data()
            bb = exact_native_gray(b) if b.get('/Subtype') == '/Image' else b.get_data()
            if aa != bb:
                raise RuntimeError('decoded stream changed at ' + location)
            stats['decoded_stream_pairs'] += 1
            stats['decoded_stream_bytes_per_pdf'] += len(aa)
            if a.get('/Subtype') == '/Image':
                stats['image_stream_pairs'] += 1
            for obj in (a, b):
                if hasattr(obj, 'decoded_self'):
                    obj.decoded_self = None
            del aa, bb
            excluded = {'/Length', '/Filter', '/DecodeParms'}
            ad, bd = ({str(k): v for k, v in x.items() if k not in excluded} for x in (a, b))
            return walk(ad, bd, location + '/stream_dictionary')
        if isinstance(a, (dict, DictionaryObject)) or isinstance(b, (dict, DictionaryObject)):
            if not isinstance(a, (dict, DictionaryObject)) or not isinstance(b, (dict, DictionaryObject)) or set(a) != set(b):
                raise RuntimeError('dictionary keys changed at ' + location)
            stats['dictionary_pairs'] += 1
            for key in sorted(a):
                if key == '/Pages' and a.get('/Type') == '/Catalog' and b.get('/Type') == '/Catalog':
                    continue
                if key == '/Parent' and a.get('/Type') == '/Page' and b.get('/Type') == '/Page':
                    continue
                av = a.raw_get(key) if isinstance(a, DictionaryObject) else a[key]
                bv = b.raw_get(key) if isinstance(b, DictionaryObject) else b[key]
                walk(av, bv, location + '/' + str(key))
            return
        if isinstance(a, (list, tuple, ArrayObject)) or isinstance(b, (list, tuple, ArrayObject)):
            if not isinstance(a, (list, tuple, ArrayObject)) or not isinstance(b, (list, tuple, ArrayObject)) or len(a) != len(b):
                raise RuntimeError('array changed at ' + location)
            for n, (x, y) in enumerate(zip(a, b)):
                walk(x, y, location + '/' + str(n))
            return
        numeric_equivalence = isinstance(a, (int, float)) and not isinstance(a, bool) and isinstance(b, (int, float)) and not isinstance(b, bool)
        if type(a) is not type(b) and not numeric_equivalence:
            raise RuntimeError('PDF primitive type changed at ' + location)
        if a != b:
            raise RuntimeError('semantic value changed at ' + location)

    for key in ['/Root', '/Info', '/ID']:
        if (key in readers[0].trailer) != (key in readers[1].trailer):
            raise RuntimeError('trailer semantic key presence differs ' + key)
        if key in readers[0].trailer:
            walk(readers[0].trailer.raw_get(key), readers[1].trailer.raw_get(key), key)
    for n, (a, b) in enumerate(zip(*page_lists), 1):
        walk(a, b, 'OrderedPage/' + str(n))
    if stats['image_stream_pairs'] != 144:
        raise RuntimeError('complete catalog graph image coverage is not 144')
    all_images = []
    for reader in readers:
        references = {(number, generation) for generation, group in reader.xref.items() for number in group if number != 0}
        references.update((number, 0) for number in reader.xref_objStm)
        image_objects = []
        for number, generation in sorted(references):
            obj = reader.get_object(IndirectObject(number, generation, reader))
            if isinstance(obj, StreamObject) and obj.get('/Subtype') == '/Image':
                raw = exact_native_gray(obj)
                image_objects.append((int(obj['/Width']), int(obj['/Height']), len(raw), digest(raw)))
                if hasattr(obj, 'decoded_self'):
                    obj.decoded_self = None
        all_images.append(sorted(image_objects))
    if all_images[0] != all_images[1] or len(all_images[0]) != 144:
        raise RuntimeError('entire cross-reference inventory image mismatch')
    return {'status': 'PASS', 'coverage': 'Root, Info and ID semantic graphs plus every ordered Page, including resources, annotations and catalog data; all xref image objects inventoried.',
            'page_tree_normalization': 'PdfWriter flattens physical Pages grouping. Catalog Pages hierarchy and Page Parent links are replaced by the exact ordered page list; all page-reference destinations compare by ordered page index.',
            'allowed_encoding_fields': ['/Length', '/Filter', '/DecodeParms'], 'counts': dict(stats),
            'all_xref_images_per_pdf': len(all_images[0]), 'native_image_inventory_sha256': digest(json.dumps(all_images[0]).encode())}


def rendered_equality(renderer, original, candidate, pages, stem):
    folder = ROOT / 'raster_checks' / stem
    folder.mkdir(parents=True, exist_ok=True)
    receipt_path = folder / 'RASTER_EQUALITY.json'
    expected = {'original_sha256': filehash(original), 'candidate_sha256': filehash(candidate),
                'renderer_sha256': filehash(renderer), 'dpi': 200, 'pages': pages,
                'verifier_sha256': filehash(Path(__file__)),
                'pixel_comparison': 'exact RGB bytes, mode and dimensions'}
    if receipt_path.exists():
        receipt = json.loads(receipt_path.read_text())
        if receipt['inputs'] != expected:
            raise RuntimeError('raster receipt provenance mismatch')
        if not 0 <= len(receipt['rows']) <= pages or [r['page'] for r in receipt['rows']] != list(range(1, len(receipt['rows']) + 1)):
            raise RuntimeError('raster receipt page inventory is not contiguous')
        expected_retained = {(folder / ('page-%03d-%s.png' % (n, label))).relative_to(BASE).as_posix()
                             for n in {1, 50, pages} if n <= len(receipt['rows']) for label in ('original', 'transport')}
        if {r['path'] for r in receipt.get('retained_pngs', [])} != expected_retained or len(receipt.get('retained_pngs', [])) != len(expected_retained):
            raise RuntimeError('retained page PNG coverage mismatch')
        for item in receipt.get('retained_pngs', []):
            p = BASE / item['path']
            if identity(p) != item:
                raise RuntimeError('retained page PNG evidence changed')
            page_number, label = p.stem.split('-')[1:]
            if item['sha256'] != receipt['rows'][int(page_number) - 1][label + '_png_sha256']:
                raise RuntimeError('retained PNG is not bound to raster equality row')
    else:
        receipt = {'schema': 'd019-method03-every-page-raster-equality-v1', 'status': 'IN_PROGRESS',
                   'inputs': expected, 'rows': [], 'retained_pngs': []}
        dump(receipt_path, receipt)
    for page in range(len(receipt['rows']) + 1, pages + 1):
        paths = []
        for label, pdf in [('original', original), ('transport', candidate)]:
            prefix = folder / ('page-%03d-%s' % (page, label))
            png = prefix.with_suffix('.png')
            if png.exists():
                raise RuntimeError('unproven partial page render preserved; use explicit recovery')
            subprocess.run([str(renderer), '-f', str(page), '-l', str(page), '-singlefile', '-r', '200', '-png',
                            str(pdf), str(prefix)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            paths.append(png)
        with Image.open(paths[0]) as a, Image.open(paths[1]) as b:
            if a.mode != b.mode or a.size != b.size or a.tobytes() != b.tobytes():
                raise RuntimeError('200dpi raster differs at page ' + str(page))
            row = {'page': page, 'mode': a.mode, 'dimensions': list(a.size), 'pixel_sha256': digest(a.tobytes()),
                   'original_png_sha256': filehash(paths[0]), 'transport_png_sha256': filehash(paths[1])}
        row['png_bytes_identical'] = row['original_png_sha256'] == row['transport_png_sha256']
        receipt['rows'].append(row)
        retained = page in {1, 50, pages}
        if retained:
            receipt['retained_pngs'].extend(identity(p) for p in paths)
        dump(receipt_path, receipt)
        if not retained:
            for p in paths:
                if p.parent != folder or not p.name.startswith('page-%03d-' % page):
                    raise RuntimeError('temporary-file removal boundary failure')
                p.unlink()
        if page == 1 or page % 10 == 0 or page == pages:
            print(json.dumps({'document': stem, 'raster_pages_equal': page, 'of': pages}), flush=True)
    if len(receipt['rows']) != pages:
        raise RuntimeError('exact per-document raster page count required')
    receipt['status'] = 'PASS'
    dump(receipt_path, receipt)
    return receipt_path, receipt


def main():
    accepted = accepted_inputs_unchanged()
    cursor = json.loads((BASE / 'TRANSPORT_CURSOR.json').read_text())
    method = json.loads((ROOT / 'METHOD_RECEIPT.json').read_text())
    expected = {row['path']: row for row in cursor['original_pdfs']}
    if len(method['documents']) != 2 or {d['original']['path'] for d in method['documents']} != set(expected):
        raise RuntimeError('exactly source-language and English documents required')
    renderer = Path(shutil.which('pdftoppm')).resolve()
    extractor = Path(shutil.which('pdftotext')).resolve()
    results = []
    checkpoint = ROOT / 'VERIFICATION_PROGRESS.json'
    for row in method['documents']:
        source_row = expected[row['original']['path']]
        if row['original'] != source_row:
            raise RuntimeError('canonical original identity differs')
        original = (BASE / source_row['path']).resolve()
        candidate, replay = (BASE / row['path']), (BASE / row['deterministic_replay']['path'])
        if identity(candidate) != {k: row[k] for k in ('path', 'bytes', 'sha256')}:
            raise RuntimeError('candidate file identity differs')
        if (candidate.stat().st_size, filehash(candidate)) != (replay.stat().st_size, filehash(replay)):
            raise RuntimeError('PDF assembly replay bytes differ')
        if not candidate.stat().st_size < 100000000 or row['pages'] != source_row['pages']:
            raise RuntimeError('strict transport size or page count not met')
        stem = candidate.stem
        graph = semantic_graph(original, candidate)
        graph_path = ROOT / (stem + '_SEMANTIC_GRAPH.json')
        dump(graph_path, graph)
        gc.collect()
        structure = compare_structure(original, candidate)
        structure_path = ROOT / (stem + '_STRUCTURAL_IDENTITY.json')
        dump(structure_path, structure)
        gc.collect()
        print(json.dumps({'document': stem, 'semantic_graph_and_all_structure': 'PASS'}), flush=True)
        texts = [ROOT / (stem + '_ORIGINAL.txt'), ROOT / (stem + '_TRANSPORT.txt')]
        for pdf, target in zip([original, candidate], texts):
            subprocess.run([str(extractor), '-layout', str(pdf), str(target)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if texts[0].read_bytes() != texts[1].read_bytes():
            raise RuntimeError('extracted text differs')
        raster_path, raster = rendered_equality(renderer, original, candidate, row['pages'], stem)
        result = {**row, 'below_100000000_bytes': candidate.stat().st_size < 100000000,
                  'semantic_graph': identity(graph_path), 'structural_identity': identity(structure_path),
                  'raster_equality': identity(raster_path), 'raster_pages': len(raster['rows']),
                  'all_page_raster_pixels_equal': True, 'all_page_png_bytes_equal': all(p['png_bytes_identical'] for p in raster['rows']),
                  'exact_extracted_text_sha256': filehash(texts[0]), 'extracted_text_bytes': texts[0].stat().st_size,
                  'deterministic_replay_scope': 'Byte-identical PDF assembly from verified completed encoded-stream cache; compression was not rerun.'}
        results.append(result)
        dump(checkpoint, {'status': 'IN_PROGRESS', 'documents': results, 'next_action': 'Continue remaining document comparison.'})
    accepted_inputs_unchanged()
    if sum(d['raster_pages'] for d in results) != 309:
        raise RuntimeError('309-page raster coverage required')
    receipt = {'schema': 'd019-method03-zopfli-lossless-verification-v1', 'status': 'PASS', 'method': 3,
               'documents': results, 'accepted_gate_bound_files_unchanged': accepted, 'content_gate_unchanged': True,
               'both_below_100000000_bytes': True, 'transport_finding': 'BOTH_PDFS_BELOW_LIMIT',
               'all_309_page_rasters_pixel_identical_at_200dpi': True,
               'tools': {'renderer': renderer.name, 'renderer_sha256': filehash(renderer), 'extractor': extractor.name,
                         'extractor_sha256': filehash(extractor), 'python': platform.python_version(), 'pypdf': pypdf.__version__, 'pillow': PIL.__version__},
               'verification_script': identity(Path(__file__)), 'method_receipt': identity(ROOT / 'METHOD_RECEIPT.json'),
               'next_action': 'Inspect retained representative transport rasters; seal transport-only result receipt and return exact identities to parent.'}
    dump(ROOT / 'LOSSLESS_VERIFICATION.json', receipt)
    dump(checkpoint, {'status': 'PASS', 'verification_receipt': identity(ROOT / 'LOSSLESS_VERIFICATION.json'), 'next_action': receipt['next_action']})
    print(json.dumps({'status': 'PASS', 'documents': [{k: d[k] for k in ('path', 'bytes', 'sha256', 'raster_pages')} for d in results],
                      'verification_receipt': identity(ROOT / 'LOSSLESS_VERIFICATION.json')}), flush=True)


if __name__ == '__main__':
    main()
