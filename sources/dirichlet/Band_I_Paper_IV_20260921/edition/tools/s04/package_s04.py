#!/usr/bin/env python3
"""Freeze, deterministically package and verify the complete S04 handoff.

Run only after the actual independent source collation, repairs, clean builds,
and individual visual review are complete. This tool verifies their recorded
bindings; it does not perform or substitute for source reading.

All current and historical member bytes are embedded. External checkpoint and
manifest are deliberately not archive members, avoiding circular self-hashes.
"""
from __future__ import annotations
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import argparse, collections, csv, hashlib, json, os, re, shutil, stat, tempfile, zipfile
from verify_handoff_s04 import verify, safe, filehash

ROOT = Path(__file__).resolve().parents[2]
PREFIX = 'DIRICHLET_P04_S04'
DATE = (2026, 9, 21, 0, 0, 0)
COLUMNS = ['path', 'bytes', 'sha256', 'role', 'acceptance', 'printed_page_range', 'provenance']
LIMIT = 350_000_000


def load(p: Path):
    return json.loads(p.read_text(encoding='utf-8'))


def atomic_bytes(path: Path, data: bytes) -> None:
    tmp = path.with_name(path.name + '.tmp')
    with tmp.open('wb') as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    tmp.replace(path)


def write_json(path: Path, data: dict) -> None:
    atomic_bytes(path, (json.dumps(data, ensure_ascii=False, indent=2) + '\n').encode('utf-8'))


def binding(p: Path) -> dict:
    return {'file': p.name, 'bytes': p.stat().st_size, 'sha256': filehash(p)}


def metadata(name: str, current_readers: set[str]) -> tuple[str, str, str, str]:
    page = re.search(r'(?:^|/)p(0\d{2})(?:[._/]|$)', name)
    extent = str(int(page.group(1))) if page else '63-98'
    if name.startswith(('history/', 'prior_evidence/')):
        return ('PRESERVED_HISTORICAL_EVIDENCE', 'HISTORICAL_NOT_CURRENT_ACCEPTANCE', extent,
                'Earlier-stage bytes and claims retained unchanged; current S04 cursor and cold-audit evidence govern.')
    if name.startswith('inherited/'):
        region = '65-74' if name.startswith('inherited/R27/') else '75-80'
        return ('UNVERIFIED_INHERITED_ORIGINAL_MEMBER', 'PRESERVED_NOT_AUTHORITY', region + ' witnesses; other content excluded',
                'Unchanged R27/R28 original member; cumulative earlier-paper readers are out-of-scope evidence only.')
    if name.startswith('input/'):
        base = Path(name).name
        if base.startswith('10_'):
            return ('CONTROLLING_AUTHORITY_PROJECTION', 'IMMUTABLE_SOURCE', '63-98',
                    'Exact original 36-leaf projection; full-PDF80-115; independently replayed against fixed map in S04.')
        if base.startswith('11_'):
            return ('FULL_VOLUME_PROVENANCE_AUTHORITY', 'IMMUTABLE_SOURCE_SCOPE_RESTRICTED', '63-98; PDF116 exclusion boundary only',
                    'Unchanged 657-page original; only PDF80-115 edited, PDF116 inspected solely for exclusion boundary.')
        if base.startswith(('12_', '13_')):
            return ('UNVERIFIED_INHERITED_ARCHIVE_ORIGINAL', 'IMMUTABLE_SALVAGE_NOT_AUTHORITY', '65-80 witnesses; other content excluded',
                    'Original R27/R28 archive retained byte-for-byte; CRC and all unpacked member bytes revalidated in S04.')
        return ('IMMUTABLE_INPUT_CONTROL_OR_RECEIPT', 'PRESERVED_ORIGINAL_CONTROL', '63-98',
                'Original input-package control, map, prompt, inventory or receipt; historical initial-state labels are not current acceptance.')
    if name.startswith('qa/s04/'):
        if 'boundary_pdf116' in name:
            return ('PAPER_V_EXCLUSION_BOUNDARY_IMAGE', 'INSPECTION_ONLY_NOT_INGESTED', 'OUT_OF_SCOPE_BOUNDARY_ONLY',
                    'Fresh rendering of full-PDF116 solely to prove Paper IV exclusion boundary; not author text.')
        if name.startswith('qa/s04/source/'):
            return ('FRESH_COLD_AUDIT_SOURCE_RENDER_OR_DETAIL', 'AUTHORITY_BOUND_EVIDENCE', extent,
                    'Fresh exact-scope rendering or enlarged detail; actual source-image reading recorded in MANUAL_COLD_COLLATION.json.')
        if name.startswith('qa/s04/repair_snapshots/'):
            return ('IMMEDIATE_BEFORE_REPAIR_SNAPSHOT', 'SUPERSEDED_TEXT_NOT_CURRENT', extent,
                    'Exact pre-repair bytes; correction and authority locator in REPAIRS.json and cumulative source-backed diff.')
        if name.startswith('qa/s04/build/'):
            return ('FINAL_CLEAN_BUILD_FILE_OR_LOG', 'BUILD_EVIDENCE_NOT_SOURCE_FIDELITY', '65-98',
                    'Initially empty build directory; initialization notices preserved; two subsequent clean acceptance passes per reader.')
        if name.startswith(('qa/s04/visual/', 'qa/s04/poppler/')):
            return ('FINAL_READER_RENDER_OR_RENDERER_LOG', 'OUTPUT_REVIEW_EVIDENCE', '65-98',
                    'Final reader rendering; individual review bindings in MANUAL_OUTPUT_REVIEW.json; Poppler provides supplemental parity evidence.')
        return ('S04_COLD_AUDIT_LEDGER_OR_QA_EVIDENCE', 'CURRENT_AUDIT_EVIDENCE', extent,
                'Fresh Prompt04 collation, structural, preservation, repair, build or visual evidence; counts alone do not establish fidelity.')
    if name.startswith('qa/'):
        return ('PRESERVED_PRIOR_QA_EVIDENCE', 'HISTORICAL_NOT_CURRENT_ACCEPTANCE', extent,
                'Earlier-stage source, build or visual evidence preserved unchanged; independently rechecked in S04 where required.')
    if name.startswith('editions/fr/'):
        return ('CURRENT_EDITABLE_DIPLOMATIC_FRENCH', 'COLD_AUDIT_ACCEPTED_S04', extent if page else '65-98',
                'Independently collated against exact-scope authority; printed anomalies literal; S04 source-backed repairs integrated.')
    if name.startswith('editions/en/'):
        return ('CURRENT_EDITABLE_FAITHFUL_ENGLISH', 'COLD_AUDIT_ACCEPTED_S04', extent if page else '65-98',
                'Independent full structural correspondence audit to French authority; mathematical tokens and source issues retained.')
    if name.startswith('apparatus/'):
        return ('CURRENT_SEPARATE_EDITABLE_APPARATUS', 'COLD_AUDIT_ACCEPTED_S04_EDITORIAL', extent if page else '65-98',
                'Separate restrained editorial explanation; contextual inferences distinguished from literal author readings.')
    if name in current_readers:
        return ('CURRENT_FINAL_READER', 'COLD_AUDIT_ACCEPTED_S04', '65-98',
                'Built from final independent source; two clean acceptance passes; every final page individually rendered and reviewed.')
    if name.startswith('readers/'):
        return ('PRESERVED_PRIOR_READER', 'HISTORICAL_NOT_CURRENT_ACCEPTANCE', '65-98 partial earlier extent',
                'Earlier-stage reader retained unchanged, not the current final reader; current paths are in state/CURSOR.json.')
    if name.startswith('copy_matter/'):
        return ('COPY_MATTER_RECORD', 'COLD_REPLAYED_COPY_ONLY', extent,
                'Reprint title63 or blank64; excluded from author readers and not counted as author prose.')
    if name.startswith('state/'):
        return ('CURRENT_CURSOR_OR_PAGE_RECORD', 'COMPLETE_S04_BOUND_STATE', extent,
                'Final exact accepted sets and fresh authority/editable/apparatus/reader/render bindings; no further project prompt pending.')
    if name.startswith('ledgers/'):
        return ('CURRENT_TOPOLOGY_OR_SESSION_LEDGER', 'COLD_AUDIT_ACCEPTED_S04', '63-98',
                'All36 leaves exact-once: title63, blank64 and34 author pages; source furniture and completion separately recorded.')
    if name.startswith('tools/s04/'):
        return ('S04_REPRODUCIBILITY_TOOL', 'TOOL_NOT_AUTHOR_TEXT', 'NOT_APPLICABLE',
                'Current intake, audit-binding, build, preflight, packaging or verification script; no tool replaces actual source reading.')
    if name.startswith('tools/'):
        return ('PRESERVED_PRIOR_STAGE_TOOL', 'HISTORICAL_DO_NOT_RUN_ON_FINAL_SOURCES', 'NOT_APPLICABLE',
                'Earlier-stage script preserved unchanged for evidence; use tools/s04 for current final-state workflows.')
    if name == 'SOURCE_BACKED_DIFF.tsv':
        return ('CUMULATIVE_SOURCE_BACKED_DIFF', 'AUTHORITY_BACKED_CORRECTIONS', '63-98',
                'Canonical72-row S03 byte prefix plus21 concrete S04 rows,93 total; exact before/after and attached-authority locators.')
    if name == 'README.md':
        return ('CURRENT_FINAL_HANDOFF_DOCUMENTATION', 'CURRENT_INFORMATION', '63-98',
                'Current COMPLETE extent, cold-audit evidence, build/review results, preservation and stage-specific handoff contract.')
    raise ValueError(f'Unclassified current archive member: {name}')


def write_archive(path: Path, files: list[tuple[str, Path]], expected: dict[str, dict]) -> None:
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as z:
        z.comment = b''
        for name, p in files:
            data = p.read_bytes()
            assert len(data) == expected[name]['bytes'] and hashlib.sha256(data).hexdigest().upper() == expected[name]['sha256'], ('changed after freeze', name)
            info = zipfile.ZipInfo(name, date_time=DATE)
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            info.extra = b''
            info.comment = b''
            z.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=6)


def main(out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    assert out.resolve() != ROOT and ROOT not in out.resolve().parents, 'Release must be outside the frozen state tree.'
    current = load(ROOT / 'state/CURSOR.json')
    gates = load(ROOT / 'qa/s04/FINAL_COLD_AUDIT_GATES.json')
    assert current['status'] == current['next_cursor'] == gates['next_cursor'] == 'COMPLETE'
    assert gates['known_author_content_defects'] == gates['unresolved_source_ambiguities'] == []
    files = sorted((safe(p.relative_to(ROOT).as_posix()), p) for p in ROOT.rglob('*') if p.is_file())
    assert all(not p.is_symlink() for _, p in files)
    names = [n for n, _ in files]
    assert len({n.casefold() for n in names}) == len(names)
    assert not any('CUMULATIVE_FULL_STATE.zip' in n for n in names)
    assert not any(Path(n).suffix.lower() in {'.pyc', '.ttf', '.otf', '.ttc', '.woff', '.woff2'} for n in names)
    expected = {n: {'bytes': p.stat().st_size, 'sha256': filehash(p)} for n, p in files}
    readers = {a['path'] for a in current['current_readers'].values()}
    zp = out / (PREFIX + '_CUMULATIVE_FULL_STATE.zip')
    cp = out / (PREFIX + '_CHECKPOINT.json')
    mp = out / (PREFIX + '_MANIFEST.tsv')
    dp = out / (PREFIX + '_SOURCE_BACKED_DIFF.tsv')
    with tempfile.TemporaryDirectory(prefix='dirichlet-s04-release-', dir=out) as tmpname:
        tmp = Path(tmpname)
        mt = tmp / mp.name
        with mt.open('w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, delimiter='\t', fieldnames=COLUMNS, lineterminator='\n')
            w.writeheader()
            for name, _ in files:
                role, acceptance, extent, provenance = metadata(name, readers)
                w.writerow({'path': name, **expected[name], 'role': role, 'acceptance': acceptance,
                            'printed_page_range': extent, 'provenance': provenance})
        a, b = tmp / 'archive-first.zip', tmp / 'archive-second.zip'
        write_archive(a, files, expected)
        write_archive(b, files, expected)
        ah, bh = filehash(a), filehash(b)
        assert a.stat().st_size == b.stat().st_size and ah == bh
        # Byte comparison is additional to size and SHA256 equality.
        with a.open('rb') as fa, b.open('rb') as fb:
            while True:
                ba, bb = fa.read(1 << 20), fb.read(1 << 20)
                assert ba == bb
                if not ba:
                    break
        os.replace(a, zp)
        os.replace(mt, mp)
        atomic_bytes(dp, (ROOT / 'SOURCE_BACKED_DIFF.tsv').read_bytes())
    checkpoint = dict(current)
    checkpoint.update({
        'schema': 'dirichlet-paper-iv-checkpoint-v3', 'schema_version': 3,
        'release_date': '2026-09-21', 'checkpoint_file': cp.name,
        'archive_member_count': len(files), 'archive_members': expected,
        'release_artifacts': {'cumulative_zip': binding(zp), 'manifest': binding(mp), 'source_backed_diff': binding(dp)},
        'source_backed_difference_rows': {'cumulative': 93, 'canonical_preserved_S03': 72, 'new_S04': 21},
        'final_cold_audit_gates': gates,
        'preservation': {'S03_original_member_sequences': 793, 'S02_original_member_sequences': 517,
                         'S01_original_member_sequences': 240, 'S03_same_path_originals': 696,
                         'S03_originals_relocated_without_alteration': 97, 'immutable_originals_embedded': 21,
                         'unpacked_inherited_original_members': 97,
                         'all_prior_resolution_map': 'qa/s04/ALL_PRIOR_MEMBER_PRESERVATION.tsv',
                         'nested_previous_cumulative_zips': False},
        'deterministic_archive_build': {'builds': 2, 'byte_identical': True, 'sha256_each': ah,
                                        'fixed_zip_datetime': list(DATE), 'sorted_normalized_paths': True,
                                        'compression': 'DEFLATE level6', 'unix_regular_mode': '0644'},
        'transport': {'mode': 'COMPLETE_SELF_CONTAINED', 'external_immutable_references': [],
                      'part_threshold_bytes': LIMIT, 'parts_required': zp.stat().st_size > LIMIT,
                      'stage_specific_sidecars': True,
                      'canonical_diff_source': 'SOURCE_BACKED_DIFF.tsv inside this final ZIP',
                      'stale_browser_diff_preserved_only_as_historical_evidence': True},
        'hash_binding_policy': 'This external checkpoint binds the ZIP, external manifest, stage-specific standalone diff, every ZIP member and current internal cursor. The checkpoint does not claim its own circular self-hash. The manifest is an exact inventory of ZIP members, not itself a ZIP member. Internal historical checkpoints retain their original stage meanings.',
        'archive_validation': {'status': 'PENDING_ACTUAL_REOPEN'}
    })
    if checkpoint['transport']['parts_required']:
        parts = []
        with zp.open('rb') as f:
            offset = 0
            number = 1
            while block := f.read(LIMIT):
                pp = out / f'{PREFIX}_CUMULATIVE_FULL_STATE.zip.part{number:03}'
                atomic_bytes(pp, block)
                parts.append({'number': number, 'offset': offset, 'length': len(block), **binding(pp)})
                offset += len(block)
                number += 1
        checkpoint['transport']['ordered_parts'] = parts
        assert offset == zp.stat().st_size
    else:
        checkpoint['transport']['ordered_parts'] = []
    write_json(cp, checkpoint)
    report = verify(zp, cp, mp, dp)
    checkpoint['archive_validation'] = report
    checkpoint['linked_artifact_check'] = {
        'actual_stage_specific_paths_reopened': True,
        'standalone_diff_byte_identical_to_final_zip_member': True,
        'manifest_and_diff_match_checkpoint_hashes': True,
        'checkpoint_reread_and_bound_to_internal_cursor_and_all_members': True
    }
    write_json(cp, checkpoint)
    final_report = verify(zp, cp, mp, dp)
    assert final_report == report
    assert load(cp) == checkpoint
    # No current member may have changed while packaging or verification ran.
    for name, p in files:
        assert p.stat().st_size == expected[name]['bytes'] and filehash(p) == expected[name]['sha256']
    assert sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()) == names
    result = {'status': 'COMPLETE', 'next_cursor': 'COMPLETE', 'verified_archive': final_report,
              'linked_files': {k: binding(p) for k, p in [('zip', zp), ('checkpoint', cp), ('manifest', mp), ('diff', dp)]},
              'split_parts_required': checkpoint['transport']['parts_required']}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT.parent)
    main(parser.parse_args().output_dir)
