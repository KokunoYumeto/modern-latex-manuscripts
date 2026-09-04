"""Seal only the independently verified selected transport method; no canonical writes."""
from pathlib import Path
import json, sys
ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent
sys.path.insert(0, str(BASE))
from inspect_transport import filehash
from verify_transport import accepted_inputs_unchanged
from pypdf import PdfReader


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def identity(path):
    return {'path': path.relative_to(BASE).as_posix(), 'bytes': path.stat().st_size, 'sha256': filehash(path)}


def check(record):
    path = BASE / record['path']
    if identity(path) != record:
        raise RuntimeError('verified artifact identity changed: ' + record['path'])
    return path


def dump(path, value):
    temporary = path.with_name(path.name + '.writing')
    temporary.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)


def page_tree_profile(pdf):
    reader = PdfReader(pdf)
    ordered = [(page.indirect_reference.idnum, page.indirect_reference.generation) for page in reader.pages]
    observed, internal, visited = [], [], set()
    def walk(reference):
        key = (reference.idnum, reference.generation)
        if key in visited:
            raise RuntimeError('cycle or duplicate page-tree node')
        visited.add(key)
        obj = reference.get_object()
        if obj.get('/Type') == '/Page':
            observed.append(key)
            return 1
        if obj.get('/Type') != '/Pages' or not set(obj).issubset({'/Type', '/Count', '/Kids', '/Parent'}):
            raise RuntimeError('page-tree grouping has nonstructural keys')
        count = sum(walk(child) for child in obj['/Kids'])
        if count != int(obj['/Count']):
            raise RuntimeError('page-tree count differs from descendants')
        internal.append({'keys': sorted(str(k) for k in obj), 'descendant_pages': count})
        return count
    count = walk(reader.trailer['/Root'].raw_get('/Pages'))
    if observed != ordered or len(set(observed)) != count:
        raise RuntimeError('page-tree ordered leaf inventory differs')
    return {'status': 'PASS', 'pages': count, 'internal_nodes': internal,
            'all_internal_keys_are_only_structural': True, 'ordered_page_references_unique': True}


def main():
    cursor = read(BASE / 'TRANSPORT_CURSOR.json')
    accepted = accepted_inputs_unchanged()
    gate = BASE.parent / 'receipts/D019_CANONICAL_FINAL_GATE.json'
    if filehash(gate) != cursor['accepted_content_gate_sha256']:
        raise RuntimeError('accepted canonical gate changed')
    proof = read(ROOT / 'LOSSLESS_VERIFICATION.json')
    if proof['status'] != 'PASS' or proof['method'] != 3:
        raise RuntimeError('method03 lossless verification not complete')
    check(proof['verification_script'])
    check(proof['method_receipt'])
    expected = {row['path']: row for row in cursor['original_pdfs']}
    if len(proof['documents']) != 2 or {d['original']['path'] for d in proof['documents']} != set(expected):
        raise RuntimeError('exact pair of required documents missing')
    selected, tree_profiles, expected_visual = [], [], []
    for document in proof['documents']:
        original = expected[document['original']['path']]
        if document['original'] != original:
            raise RuntimeError('original identity changed in proof')
        candidate = check({k: document[k] for k in ('path', 'bytes', 'sha256')})
        replay = document['deterministic_replay']
        replay_path = check({k: replay[k] for k in ('path', 'bytes', 'sha256')})
        if filehash(candidate) != filehash(replay_path) or candidate.stat().st_size >= 100000000:
            raise RuntimeError('replay or transport-size failure')
        structure = read(check(document['structural_identity']))
        graph = read(check(document['semantic_graph']))
        raster = read(check(document['raster_equality']))
        if (structure['status'] != 'PASS' or structure['page_count'] != original['pages']
                or len(structure['pages']) != original['pages'] or structure['unique_image_pixel_identities'] != 144
                or graph['status'] != 'PASS' or graph['all_xref_images_per_pdf'] != 144
                or raster['status'] != 'PASS' or raster['inputs']['pages'] != original['pages']
                or [r['page'] for r in raster['rows']] != list(range(1, original['pages'] + 1))
                or raster['inputs']['original_sha256'] != original['sha256']
                or raster['inputs']['candidate_sha256'] != document['sha256']
                or raster['inputs']['verifier_sha256'] != proof['verification_script']['sha256']):
            raise RuntimeError('full native and raster coverage failure')
        for retained in raster['retained_pngs']:
            check(retained)
        expected_visual.extend(p for p in raster['retained_pngs'] if p['path'].endswith('-transport.png'))
        tree_profiles.append({'original': original['path'], 'candidate': document['path'],
                              'original_tree': page_tree_profile((BASE / original['path']).resolve()),
                              'transport_tree': page_tree_profile(candidate)})
        selected.append({**identity(candidate), 'pages': original['pages'], 'below_100000000_bytes': True,
                         'headroom_bytes': 100000000 - candidate.stat().st_size,
                         'bytes_saved': original['bytes'] - candidate.stat().st_size,
                         'original': original, 'assembly_replay': identity(replay_path)})
    visual_path = ROOT / 'VISUAL_SPOTCHECK.json'
    visual = read(visual_path)
    if visual['status'] != 'PASS' or visual['method'] != 3:
        raise RuntimeError('representative latest-render visual check missing')
    if len(expected_visual) != 6 or sorted(visual['checked_rasters'], key=lambda p: p['path']) != sorted(expected_visual, key=lambda p: p['path']):
        raise RuntimeError('exact six retained transport samples must be visually checked')
    for checked in visual['checked_rasters']:
        check(checked)
    tree_path = ROOT / 'PAGE_TREE_NORMALIZATION_AUDIT.json'
    dump(tree_path, {'status': 'PASS', 'documents': tree_profiles,
                     'finding': 'Only physical Pages grouping differs; all grouping nodes have exclusively structural keys, exact descendant counts, and unique ordered page references.'})
    result = {'schema': 'd019-method03-lossless-transport-result-v1', 'status': 'PASS', 'work_id': 'D019',
              'scope': 'Separately validated lossless PDF transport derivatives only; original accepted content and canonical gate immutable.',
              'content_gate_sha256': filehash(gate), 'accepted_gate_bound_files_unchanged': accepted,
              'strict_transport_limit_bytes': 100000000, 'selected_method': 3,
              'transport_finding': 'BOTH_PDFS_BELOW_LIMIT', 'selected_pdfs': selected,
              'recipe': 'Zopfli one-iteration lossless Flate on exact native grayscale pixels, retaining prior Flate if smaller; no image dimension, bit depth, content, font or geometry changes.',
              'compression_reused_without_rerun': True,
              'deterministic_replay_scope': 'Each PDF is byte-identical to an independent assembly from the same verified completed encoded-stream cache. Zopfli compression was not rerun.',
              'validation': {'all_144_native_images_per_pdf_exact': True, 'all_image_noncompression_dictionaries_equal': True,
                             'all_page_content_font_streams_text_geometry_equal': True, 'complete_catalog_and_resource_graph_equal': True,
                             'all_309_page_rasters_pixel_identical_at_200dpi': True,
                             'lossless_verification': identity(ROOT / 'LOSSLESS_VERIFICATION.json'), 'visual_spotcheck': identity(visual_path),
                             'page_tree_normalization_audit': identity(tree_path)},
              'reproduction_files': [identity(ROOT / name) for name in ('produce_zopfli.py', 'resume_assembly.py', 'verify_zopfli.py', 'finalize_zopfli.py', 'METHOD_RECEIPT.json')],
              'legacy_verification_dependencies': [identity(BASE / name) for name in ('verify_transport.py', 'inspect_transport.py')],
              'no_canonical_gate_shared_state_git_or_public_endpoint_changes': True,
              'remaining_transport_issues': [],
              'next_action': 'Parent: use these two verified sub-100000000-byte transport PDFs for the already authorized delivery; retain canonical originals and bind this transport receipt to their unchanged canonical gate.'}
    dump(BASE / 'TRANSPORT_RESULT.json', result)
    for run in cursor['method_runs']:
        if run.get('status') == 'RUNNING':
            run.setdefault('prior_cursor_status', run['status'])
            run['status'] = 'NOT_SELECTED_SUPERSEDED_BY_VERIFIED_METHOD03'
    cursor.setdefault('prior_method_limit_before_explicit_method03_resumption', cursor.get('max_optimization_methods'))
    cursor['max_optimization_methods'] = 3
    cursor['status'] = 'COMPLETE'
    cursor['selected_method'] = 3
    cursor['method_runs'] = [run for run in cursor['method_runs'] if run['method'] != 3] + [{
        'method': 3, 'directory': 'method03_zopfli', 'status': 'COMPLETE', 'verification': 'PASS', 'both_below_limit': True,
        'recipe': result['recipe'], 'receipt_path': 'method03_zopfli/METHOD_RECEIPT.json',
        'verification_receipt': 'method03_zopfli/LOSSLESS_VERIFICATION.json', 'documents': selected}]
    cursor['result_receipt'] = identity(BASE / 'TRANSPORT_RESULT.json')
    cursor['next_action'] = result['next_action']
    dump(BASE / 'TRANSPORT_CURSOR.json', cursor)
    progress = read(ROOT / 'PROGRESS.json')
    progress['status'] = 'COMPLETE_LOSSLESS_TRANSPORT_VERIFIED'
    progress['next_action'] = result['next_action']
    progress['result_receipt'] = cursor['result_receipt']
    dump(ROOT / 'PROGRESS.json', progress)
    print(json.dumps({'status': 'PASS', 'selected_pdfs': selected, 'result_receipt': cursor['result_receipt']}), flush=True)


if __name__ == '__main__':
    main()
