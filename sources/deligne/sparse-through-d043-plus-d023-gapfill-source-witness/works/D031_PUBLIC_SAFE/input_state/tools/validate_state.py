#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import pathlib
import re
import sys
from collections import defaultdict

ROOT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
AUTH = '20_AUTHORITY_DELIGNE_D031_SHIMURA_CANONICAL_MODELS_IAS_43PP.pdf'
COMP = '21_COMPARATOR_DELIGNE_D031_SHIMURA_CANONICAL_MODELS_COLLECTED_43PP.pdf'
SALV = '30_ZERO_ACCEPTED_DEDUP_PRIOR_WORK_DELIGNE_D031.zip'
AUTH_SHA = '591EE837C4C87E5263B76427B393742E111D615C6E098C940F132519A0861922'
COMP_SHA = '5A8B592C4A1BF21CBA5403B4CE8584D772CD7E907DD8B6EC7FCF9FE8E03605AC'
SALV_SHA = 'E51133164653E75BC950A79C30E75307BCABEF945E65A36258160BAEEFFB4EA8'
RANGES = [(1, 6), (7, 12), (13, 18), (19, 24), (25, 30), (31, 36), (37, 42), (43, 43)]
CUMULATIVE = [0, 6, 12, 18, 24, 30, 36, 42, 43]
ALLOWED_STATES = {'IN_PROGRESS', 'COMPLETE'}


def sha(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest().upper()


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def rows(path: pathlib.Path) -> list[dict[str, str]]:
    with path.open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def page_records(path: pathlib.Path) -> dict[int, tuple[int, bytes]]:
    text = path.read_text(encoding='utf-8')
    pat = re.compile(
        r'<!-- BEGIN_PAGE physical=(\d+) printed=(\d+) -->\n.*?\n'
        r'<!-- END_PAGE physical=\1 printed=\2 -->',
        re.S,
    )
    found: dict[int, tuple[int, bytes]] = {}
    for m in pat.finditer(text):
        p = int(m.group(1))
        printed = int(m.group(2))
        assert p not in found
        found[p] = (printed, m.group(0).encode('utf-8'))
    return found


required = {
    'README.md', 'state.json', 'source_hierarchy.json', 'page_map.tsv', 'session_plan.tsv',
    'instructions/governing.md', 'instructions/prompts.md',
    'editions/french_diplomatic.md', 'editions/english_translation.md',
    'apparatus/apparatus.tsv', 'coverage/coverage.tsv',
    'provenance/salvage_ledger.tsv', 'provenance/public_inventory.tsv',
    'provenance/evidence_inventory.tsv', 'provenance/faults.tsv',
    f'seed/{AUTH}', f'seed/{COMP}', f'seed/{SALV}',
    'tools/package_state.py', 'tools/validate_state.py',
}
files = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()}
assert files == required and len(files) == 20

state = json.loads((ROOT / 'state.json').read_text(encoding='utf-8'))
assert state['schema'] == 'deligne-d031-cumulative-state-v1'
assert state['work_id'] == 'DELIGNE_D031_SHIMURA_CANONICAL_MODELS'
assert state['physical_pages'] == state['article_pages'] == 43
assert state['prompt_count'] == 8
assert state['printed_span'] == '247-289'
assert state['publication_header_claim'] == '247-290'
assert state['page_290'] == 'ABSENT_DO_NOT_INVENT'
assert state['accepted_salvage_members'] == state['salvage']['accepted_members'] == 0
assert state['salvage']['trust_class'] == 'ZERO_ACCEPTED'
assert state['source_freeze_rule'] == 'FRENCH_BEFORE_CANDIDATE_COMPARISON_OR_ENGLISH_TRANSLATION'

completed_prompts = int(state['completed_prompts'])
accepted_units = int(state['accepted_units'])
assert 0 <= completed_prompts <= 8
assert accepted_units == CUMULATIVE[completed_prompts]
assert state['session'] == f'S{completed_prompts:02d}'
assert state['session_status'] == 'COMPLETE'
expected_status = 'COMPLETE' if accepted_units == 43 else 'IN_PROGRESS'
assert state['status'] == state['workflow_status'] == expected_status
expected_next = 'NONE_PROJECT_COMPLETE' if completed_prompts == 8 else f'P{completed_prompts + 1:02d}'
assert state['next_prompt'] == expected_next
if completed_prompts:
    assert state['last_completed_prompt'] == f'P{completed_prompts:02d}'
    assert state['owned_range']['prompt_id'] == f'P{completed_prompts:02d}'
    assert state['owned_range']['status'] == 'COMPLETE'
    start, end = RANGES[completed_prompts - 1]
    assert state['owned_range']['physical_start'] == start
    assert state['owned_range']['physical_end'] == end
    assert state['owned_range']['printed_start'] == 246 + start
    assert state['owned_range']['printed_end'] == 246 + end
assert state['completed_physical_pages'] == list(range(1, accepted_units + 1))
assert state['completed_printed_pages'] == list(range(247, 247 + accepted_units))
if accepted_units < 43:
    assert state['next_physical_page'] == accepted_units + 1
    assert state['next_printed_page'] == 247 + accepted_units

for key, value in state.items():
    if key.endswith('_status') and isinstance(value, str):
        assert value in ALLOWED_STATES
for layer in state['layers'].values():
    for key, value in layer.items():
        if key.endswith('_status'):
            assert value in ALLOWED_STATES
for value in state['order_receipt'].values():
    assert value in ALLOWED_STATES

assert sha(ROOT / 'seed' / AUTH) == AUTH_SHA
assert sha(ROOT / 'seed' / COMP) == COMP_SHA
assert sha(ROOT / 'seed' / SALV) == SALV_SHA
assert state['authority']['sha256'] == AUTH_SHA
assert state['comparator']['sha256'] == COMP_SHA
assert state['salvage']['sha256'] == SALV_SHA

mapping = rows(ROOT / 'page_map.tsv')
assert len(mapping) == 43
assert [int(r['physical_page']) for r in mapping] == list(range(1, 44))
assert [int(r['printed_page']) for r in mapping] == list(range(247, 290))
assert not any(r['printed_page'] == '290' for r in mapping)
assert all(r['source_language'] == 'FRENCH' for r in mapping)

plan = rows(ROOT / 'session_plan.tsv')
assert len(plan) == 8
assert [(int(r['physical_start']), int(r['physical_end'])) for r in plan] == RANGES
assert [int(r['cumulative_units_on_complete']) for r in plan] == CUMULATIVE[1:]
assert plan[-1]['mode'].endswith('FRESH_FULL_NONPATCHING_COLD_AUDIT')

prompts = (ROOT / 'instructions/prompts.md').read_text(encoding='utf-8')
assert len(re.findall(r'^<!-- BEGIN_LITERAL_PROMPT P\d{2} -->$', prompts, re.M)) == 8
assert len(re.findall(r'^<!-- END_LITERAL_PROMPT P\d{2} -->$', prompts, re.M)) == 8
assert 'French is replayed and frozen before inherited comparison or English translation' in prompts
assert 'Never invent a page 290' in prompts

hier = json.loads((ROOT / 'source_hierarchy.json').read_text(encoding='utf-8'))
assert hier['pagination_discrepancy']['page_290'] == 'ABSENT_DO_NOT_INVENT'
assert hier['layer_order'] == ['authority_pixels', 'frozen_french_diplomatic', 'english_translation', 'restrained_apparatus']

salvage_rows = rows(ROOT / 'provenance/salvage_ledger.tsv')
public_rows = rows(ROOT / 'provenance/public_inventory.tsv')
evidence_rows = rows(ROOT / 'provenance/evidence_inventory.tsv')
fault_rows = rows(ROOT / 'provenance/faults.tsv')
assert len(salvage_rows) == 215 and all(r['accepted_state'] == 'ZERO_ACCEPTED' for r in salvage_rows)
assert len(public_rows) == 42
assert len(evidence_rows) == 61 and all(r['accepted_state'] == 'ZERO_ACCEPTED' for r in evidence_rows)
assert len(fault_rows) == 4 and all(r['accepted_state'] == 'ZERO_ACCEPTED' for r in fault_rows)

french_records = page_records(ROOT / 'editions/french_diplomatic.md')
english_records = page_records(ROOT / 'editions/english_translation.md')
expected_pages = set(range(1, accepted_units + 1))
assert set(french_records) == set(english_records) == expected_pages
for p in expected_pages:
    assert french_records[p][0] == english_records[p][0] == 246 + p

# Apparatus record hashes use the exact raw TSV row bytes for each page, excluding the header.
raw_apparatus = (ROOT / 'apparatus/apparatus.tsv').read_bytes().splitlines(keepends=True)
assert raw_apparatus
apparatus_by_page: dict[int, bytearray] = defaultdict(bytearray)
for raw in raw_apparatus[1:]:
    fields = next(csv.reader([raw.decode('utf-8').rstrip('\r\n')], delimiter='\t'))
    assert len(fields) == 8
    p = int(fields[1])
    assert p in expected_pages
    assert fields[7] == 'COMPLETE'
    apparatus_by_page[p].extend(raw)
assert set(apparatus_by_page) == expected_pages

coverage = rows(ROOT / 'coverage/coverage.tsv')
assert len(coverage) == 43
for row in coverage:
    p = int(row['physical_page'])
    assert int(row['printed_page']) == 246 + p
    assert row['freeze_order'] == 'FRENCH_THEN_COMPARISON_THEN_ENGLISH_THEN_APPARATUS'
    if p <= accepted_units:
        assert row['french_status'] == row['english_status'] == row['apparatus_status'] == 'COMPLETE'
        assert row['french_record_sha256'] == sha_bytes(french_records[p][1])
        assert row['english_record_sha256'] == sha_bytes(english_records[p][1])
        assert row['apparatus_record_sha256'] == sha_bytes(bytes(apparatus_by_page[p]))
    else:
        assert row['french_status'] == row['english_status'] == row['apparatus_status'] == 'IN_PROGRESS'
        assert not row['french_record_sha256'] and not row['english_record_sha256'] and not row['apparatus_record_sha256']

french = (ROOT / 'editions/french_diplomatic.md').read_text(encoding='utf-8')
english = (ROOT / 'editions/english_translation.md').read_text(encoding='utf-8')
assert 'printed=290' not in french and 'printed=290' not in english
if accepted_units >= 3:
    assert r'N_{F/E}' in french and r'N_{F/E}' in english
    assert r'\begin{tikzcd}' in french and r'\begin{tikzcd}' in english
    assert r'\rho\widetilde G(A)' in french and r'\rho\widetilde G(A)' in english
if accepted_units >= 6:
    for text in (french, english):
        assert r'h^{-1}' in text
        assert r'\mathscr C' in text
        assert r'\operatorname{pr}' in text
        assert r'\pi_0 A_E^*/E^*' in text
        assert r'\tag{1.1.1.1}' in text
    assert r'H^1(A,\mathbf Z)' in french
if accepted_units >= 16:
    for text in (french, english):
        assert r'r(\varphi(\gamma))' in text
        assert r'\operatorname{int}_\gamma' in text
        assert r'G/\operatorname{Ker}(\varphi)' in text
        assert r'\tag{2.0.1.1}' in text
        assert r'\tag{2.0.1.2}' in text
    assert r'r(g\varphi(\gamma))' not in french
    assert r'r(g\varphi(\gamma))' not in english
if accepted_units >= 38:
    for records in (french_records, english_records):
        p38 = records[38][1].decode('utf-8')
        assert r'r_{G,X}(\sigma)' in p38
        assert r'\pi_0N_{E/\mathbf Q}q_M' in p38
        assert r'r_{G,X}(\sigma)^{-1}' not in p38
        assert r'r_{G,X}(\sigma)^{ -1}' not in p38
if accepted_units >= 40:
    for records in (french_records, english_records):
        p40 = records[40][1].decode('utf-8')
        assert r'\sigma\cdot x=x\cdot r(\sigma)' in p40
        assert r'(\gamma K\gamma^{-1}\cap\Delta)\backslash T' in p40
        assert r'\mathscr E' in p40
if accepted_units >= 42:
    for records in (french_records, english_records):
        p41 = records[41][1].decode('utf-8')
        p42 = records[42][1].decode('utf-8')
        assert r'M^0_{\overline{\mathbf Q}}' in p41
        assert r'G_1(\mathbf R)^0' in p42
        assert '2.7.20' in p42
    if accepted_units == 42:
        assert 'printed=289' not in french and 'printed=289' not in english


if accepted_units >= 43:
    assert state['full_cold_audit_status'] == 'COMPLETE'
    assert state['layers']['french_diplomatic']['cumulative_status'] == 'COMPLETE'
    assert state['layers']['english_translation']['cumulative_status'] == 'COMPLETE'
    assert state['layers']['apparatus']['cumulative_status'] == 'COMPLETE'
    assert state['cold_audit']['mode'] == 'FRESH_FULL_NONPATCHING_COLD_AUDIT'
    assert all(v == 'COMPLETE' for v in state['cold_audit']['fault_gates'].values())
    for records in (french_records, english_records):
        p43 = records[43][1].decode('utf-8')
        assert '2.7.21' in p43
        assert r'D^{\mathbf R}' in p43 and r'D^{\mathbf H}' in p43
        assert r'M(G,X)' in p43
        assert 'Exposé 389' in p43
        assert 'Exposé 339' not in p43
        assert r'SGA4^{1/2}' in p43
        assert 'INSTITUT HAUTES ETUDES SCIENTIFIQUES, BURES-SUR-YVETTE' in p43
    p41e = english_records[41][1].decode('utf-8')
    assert r'\pi_0(M^0_{\overline{\mathbf Q}}(G,X))=\pi_0(M_{\mathbf C}(G,X))' in p41e
    assert r'projection of $M_{\overline{\mathbf Q}}(G,X)$' in p41e
    assert 'printed=290' not in french and 'printed=290' not in english

for path in [p for p in ROOT.rglob('*') if p.is_file() and p.suffix.lower() in ('.md', '.tsv', '.json', '.py')]:
    text = path.read_text(encoding='utf-8', errors='replace')
    assert 'C:\\Users\\[LOCAL_ACCOUNT]' not in text

print(json.dumps({
    'accepted_units': accepted_units,
    'completed_prompts': completed_prompts,
    'files': 20,
    'next_prompt': expected_next,
    'physical_pages': 43,
    'result': 'PASS',
    'status': expected_status,
}, sort_keys=True))
