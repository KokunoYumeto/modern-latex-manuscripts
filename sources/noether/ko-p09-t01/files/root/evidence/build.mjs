import { readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';

const root = new URL('../', import.meta.url);
const authorityPath = 'C:/Users/Floris/Documents/interlanguage/03_projects/noether/07_german_canon_control/candidates/ED0002/noether.tex';
const pointerSha = 'B06BE3530D9CF2E82B56FDBA7FE41D5D044DF2425DFA2A059D4939EAA2F7A6C2';
const editionSha = 'C9A125167ACB33D914EE4374B65AE7CDF0052F568371B8B77B720EA178ABF0E3';
const sha = data => createHash('sha256').update(data).digest('hex').toUpperCase();
const stable = value => JSON.stringify(value, Object.keys(value).sort());
const info = data => ({ bytes: data.length, sha256: sha(data) });

const authorityRaw = await readFile(authorityPath);
if (authorityRaw.length !== 2153554 || sha(authorityRaw) !== editionSha) throw new Error('ED0002 identity mismatch');
const authorityLines = authorityRaw.toString('utf8').replaceAll('\r\n', '\n').split('\n');
const route = JSON.parse(await readFile(new URL('route.json', root), 'utf8'));
const sourceSnapshot = await readFile(new URL('source.tex', root));
if (sourceSnapshot.length !== 77798 || sha(sourceSnapshot) !== '7C9C4970145A374552E0D68C5A5C8B5614447086737D808E2235805E38217FA7') throw new Error('source snapshot mismatch');

const lineBytes = (lines, start, end) => Buffer.from(`${lines.slice(start - 1, end).join('\n')}\n`, 'utf8');
const targetLineBytes = (text, start, end) => {
  const lines = text.split('\n');
  return Buffer.from(`${lines.slice(start - 1, end).join('\n')}\n`, 'utf8');
};

const targets = new Map();
for (const unit of route.tranche.units) {
  const path = `targets/${unit.id}.tex`;
  const data = await readFile(new URL(path, root));
  const text = data.toString('utf8');
  if (data[0] === 0xEF && data[1] === 0xBB && data[2] === 0xBF) throw new Error(`${path}: BOM`);
  if (data.includes(0x0D) || data.includes(0x1B) || !text.endsWith('\n')) throw new Error(`${path}: control-byte failure`);
  if (!text.includes(`ED0002 lines${unit.lines[0]}--${unit.lines[1]}`)) throw new Error(`${path}: locator header mismatch`);
  if (!text.includes(pointerSha) || !text.includes(editionSha) || !text.includes('UNCHECKED')) throw new Error(`${path}: custody header mismatch`);
  const source = lineBytes(authorityLines, unit.lines[0], unit.lines[1]);
  if (source.length !== unit.bytes || sha(source) !== unit.sha256) throw new Error(`${path}: source unit mismatch`);
  targets.set(unit.id, { path, data, text, ...info(data) });
}

const childSpecs = {
  T01_U01: [
    ['section_title', 6348, 6348, 6, 6],
    ['publication_header', 6349, 6355, 7, 13],
  ],
  T01_U02: [
    ['closed_prose', 6357, 6359, 6, 6],
    ['enumeration', 6360, 6368, 7, 12],
    ['list_item', 6361, 6362, 8, 8],
    ['list_item', 6363, 6363, 9, 9],
    ['list_item', 6364, 6364, 10, 10],
    ['list_item', 6365, 6367, 11, 11],
    ['source_note', 6366, 6367, 11, 11],
  ],
  T01_U03: [
    ['closed_prose', 6370, 6383, 6, 6],
    ['definition', 6370, 6374, 6, 6],
    ['definition', 6375, 6380, 6, 6],
    ['source_note', 6377, 6380, 6, 6],
  ],
  T01_U04: [
    ['closed_prose', 6385, 6385, 6, 6],
    ['enumeration', 6386, 6397, 7, 11],
    ['list_item', 6387, 6387, 8, 8],
    ['list_item', 6388, 6394, 9, 9],
    ['source_note', 6388, 6393, 9, 9],
    ['list_item', 6395, 6396, 10, 10],
    ['closed_prose', 6398, 6398, 12, 12],
    ['enumeration', 6399, 6404, 13, 16],
    ['list_item', 6400, 6401, 14, 14],
    ['list_item', 6402, 6403, 15, 15],
    ['source_note', 6403, 6403, 15, 15],
  ],
  T01_U05: [['closed_prose', 6406, 6414, 6, 6]],
  T01_U06: [
    ['closed_prose', 6416, 6425, 6, 6],
    ['enumeration', 6426, 6429, 7, 9],
    ['list_item', 6427, 6428, 8, 8],
  ],
  T01_U07: [
    ['closed_prose', 6431, 6434, 6, 6],
    ['enumeration', 6435, 6446, 7, 10],
    ['list_item', 6436, 6440, 8, 8],
    ['list_item', 6441, 6445, 9, 9],
    ['source_note', 6442, 6442, 9, 9],
  ],
  T01_U08: [['closed_prose', 6448, 6452, 6, 6]],
  T01_U09: [
    ['closed_prose', 6454, 6465, 6, 6],
    ['definition', 6454, 6462, 6, 6],
    ['enumeration', 6466, 6475, 7, 10],
    ['list_item', 6467, 6470, 8, 8],
    ['list_item', 6471, 6474, 9, 9],
  ],
  T01_U10: [['closed_prose', 6477, 6483, 6, 6]],
  T01_U11: [['closed_prose', 6485, 6490, 6, 6]],
};

let seq = 0;
const records = [];
const unitRecordIds = new Map();
const recordState = translation => ({
  translation,
  review: 'unchecked',
  source_check: 'not_performed',
  formula_check: 'not_performed',
  build: 'not_run',
  render: 'not_run',
  visual_qa: 'not_run',
  publication: 'not_handed_off',
});
const addRecord = record => {
  seq += 1;
  const withId = { id: `CJK-KO-P09-STR-${String(seq).padStart(4, '0')}`, ...record };
  const evidence_sha256 = sha(Buffer.from(JSON.stringify(withId), 'utf8'));
  const final = { ...withId, evidence_sha256 };
  records.push(final);
  return final.id;
};
const authorityObject = (start, end) => {
  const data = lineBytes(authorityLines, start, end);
  return {
    edition_id: 'NOETH-DE-ED-0002',
    whole_path: authorityPath.replaceAll('/', '\\'),
    whole_sha256: editionSha,
    snapshot_path: 'source.tex',
    line_start: start,
    line_end: end,
    ...info(data),
  };
};
const targetObject = (unitId, start, end) => {
  const target = targets.get(unitId);
  const data = targetLineBytes(target.text, start, end);
  return { path: target.path, line_start: start, line_end: end, ...info(data) };
};

const workId = addRecord({
  type: 'work', parent_id: null, order: 1,
  authority: authorityObject(6348, 7679), target: null, relations: [], language: 'ko',
  state: recordState('partial_producer_draft'), continuation: { next_authority_line: 6492 },
});
const trancheId = addRecord({
  type: 'tranche', parent_id: workId, order: 1,
  authority: authorityObject(6348, 6491), target: null, relations: [{ type: 'part_of', target_id: workId }], language: 'ko',
  state: recordState('draft_complete'), continuation: { next_authority_line: 6492 },
});

for (const [unitOrder, unit] of route.tranche.units.entries()) {
  const target = targets.get(unit.id);
  const unitId = addRecord({
    type: 'unit', parent_id: trancheId, order: unitOrder + 1,
    authority: authorityObject(unit.lines[0], unit.lines[1]),
    target: { path: target.path, line_start: 1, line_end: target.text.trimEnd().split('\n').length, bytes: target.bytes, sha256: target.sha256 },
    relations: [{ type: 'part_of', target_id: trancheId }], language: 'ko',
    state: recordState('draft_complete'), continuation: { next_authority_line: 6492 },
  });
  unitRecordIds.set(unit.id, unitId);
  let childOrder = 0;
  for (const [type, sourceStart, sourceEnd, targetStart, targetEnd] of childSpecs[unit.id]) {
    childOrder += 1;
    addRecord({
      type, parent_id: unitId, order: childOrder,
      authority: authorityObject(sourceStart, sourceEnd), target: targetObject(unit.id, targetStart, targetEnd),
      relations: [{ type: 'contained_in', target_id: unitId }], language: 'ko',
      state: recordState('draft_complete'), continuation: { next_authority_line: 6492 },
    });
  }
  const targetLines = target.text.split('\n');
  for (let i = 5; i < targetLines.length; i += 1) {
    if (!targetLines[i].includes('§')) continue;
    childOrder += 1;
    addRecord({
      type: 'cross_reference', parent_id: unitId, order: childOrder,
      authority: { ...authorityObject(unit.lines[0], unit.lines[1]), locator_precision: 'unit_bounded' },
      target: targetObject(unit.id, i + 1, i + 1),
      relations: [{ type: 'bounded_by', target_id: unitId }], language: 'ko',
      state: recordState('draft_complete'), continuation: { next_authority_line: 6492 },
    });
  }
}

const structureJsonl = Buffer.from(`${records.map(record => JSON.stringify(record)).join('\n')}\n`, 'utf8');
const csvEscape = value => `"${String(value ?? '').replaceAll('"', '""')}"`;
const structureHeader = ['id','type','parent_id','order','source_start','source_end','source_bytes','source_sha256','target_path','target_start','target_end','target_bytes','target_sha256','relations','language','translation','review','next_authority_line','evidence_sha256'];
const structureRows = records.map(record => [
  record.id, record.type, record.parent_id, record.order,
  record.authority?.line_start, record.authority?.line_end, record.authority?.bytes, record.authority?.sha256,
  record.target?.path, record.target?.line_start, record.target?.line_end, record.target?.bytes, record.target?.sha256,
  JSON.stringify(record.relations), record.language, record.state.translation, record.state.review,
  record.continuation.next_authority_line, record.evidence_sha256,
].map(csvEscape).join(','));
const structureCsv = Buffer.from(`${structureHeader.map(csvEscape).join(',')}\n${structureRows.join('\n')}\n`, 'utf8');

const structureSchema = {
  $schema: 'https://json-schema.org/draft/2020-12/schema',
  title: 'Korean Noether structural JSONL record', type: 'object', additionalProperties: false,
  required: ['id','type','parent_id','order','authority','target','relations','language','state','continuation','evidence_sha256'],
  properties: {
    id: { type: 'string', pattern: '^CJK-KO-P09-STR-[0-9]{4}$' }, type: { type: 'string' }, parent_id: { type: ['string','null'] }, order: { type: 'integer', minimum: 1 },
    authority: { type: 'object' }, target: { type: ['object','null'] }, relations: { type: 'array' }, language: { const: 'ko' }, state: { type: 'object' }, continuation: { type: 'object' }, evidence_sha256: { type: 'string', pattern: '^[A-F0-9]{64}$' },
  },
};

const unitRef = id => unitRecordIds.get(id);
const hard = [
  {
    id: 'CJK-KO-P09-HARD-001', locator: 'P09 title and throughout T01', symptom: 'ganze transzendente Zahlen can be mistranslated as ordinary integer transcendental numbers',
    cause_evidence: 'The domain contains transcendental elements satisfying integral-style closure conditions; ganze is historical algebraic integrality vocabulary.',
    attempts: ['Rejected 정수 초월수 as too readily read as integer plus transcendental.'], resolution: 'held_provisional: 정수적 초월수', residual_risk: 'Independent Korean mathematical review may prefer a different established historical term.', recurrence_cues: ['ganze Zahl','ganz algebraisch','ganz rational'], related_structural_ids: [unitRef('T01_U01'), unitRef('T01_U02')], lexical_basin: 'mixed/contested', sense_window: 'integral-style transcendental elements, not ordinary integers', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-002', locator: 'ED0002 lines6370-6375 and later algebraische Basis', symptom: 'Literal 대수적 기저 conflicts with the defined algebraically independent generating system.',
    cause_evidence: 'The source immediately defines algebraic independence and algebraic generation of all remaining numbers, the modern transcendence-basis sense.',
    attempts: ['Rejected literal 대수적 기저.','Did not consult Chinese P09 as Korean authority.'], resolution: 'held_provisional: 초월기저', residual_risk: 'Historical terminology and Steinitz usage require independent Korean review.', recurrence_cues: ['algebraische Basis','Basis H','Basiszahlen eta'], related_structural_ids: [unitRef('T01_U03'), unitRef('T01_U08')], lexical_basin: 'modern Sino-xenic coinage/calque', sense_window: 'maximal algebraically independent system over which all numbers are algebraic', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-003', locator: 'ED0002 lines6388-6403', symptom: 'ganzzahlig, ganze algebraische Funktion, rational-gebrochen, and algebraisch-gebrochen form a dense false-friend cluster.',
    cause_evidence: 'The source note defines ganzzahlig by coefficients in the ring [K] of algebraic integers and contrasts contained with excluded function classes.',
    attempts: ['Rejected a uniform 정수 translation without local qualifiers.'], resolution: 'held_provisional: 정수적인 계수 / 정수적 대수함수 / 분수형 유리함수 / 분수형 대수함수', residual_risk: 'Function-class terminology needs source and Korean formula review.', recurrence_cues: ['ganzzahlig','ganze Funktion','gebrochene Funktion'], related_structural_ids: [unitRef('T01_U04')], lexical_basin: 'mixed/contested', sense_window: 'integrality and fractional-function classes relative to [K]', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-004', locator: 'ED0002 lines6423-6428', symptom: 'algebraisch-ganze Abgeschlossenheit and algebraisch-ganz und ganzzahlig abhängig resist a clean one-to-one Korean calque.',
    cause_evidence: 'Property V combines algebraic-integrality and integral-dependence language in a historical formulation.',
    attempts: ['Rejected a silent modernization to standard integral closure because the exact dependency scope is not independently checked.'], resolution: 'held: 대수적 정수성에 대한 폐쇄성; clause remains checker debt', residual_risk: 'The Korean clause may over-separate two linked source modifiers.', recurrence_cues: ['algebraisch-ganz','ganzzahlig abhängig','Abgeschlossenheit'], related_structural_ids: [unitRef('T01_U06')], lexical_basin: 'mixed/contested', sense_window: 'closure under historically formulated integral algebraic dependence', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-005', locator: 'ED0002 lines6454-6474', symptom: 'rationale Basis and rational-ganz are historical technical pairs, not generic rationality adjectives.',
    cause_evidence: 'The source defines the basis by rational generation plus a well-order restriction and uses rational-ganz for the associated adjunction/domain class.',
    attempts: ['Rejected paper-wide lexical normalization before later contexts are read.'], resolution: 'held_provisional: 유리기저 / 유리적으로 정수인', residual_risk: 'Independent checker may choose 유리적 기저 or another established expression.', recurrence_cues: ['rationale Basis','rational-ganz','ganze rationale Funktion'], related_structural_ids: [unitRef('T01_U09')], lexical_basin: 'modern Sino-xenic coinage/calque', sense_window: 'source-defined rational generating basis and associated integrality class', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-006', locator: 'targets/T01_U04.tex line3', symptom: 'The first written custody header omitted characters from the v009 pointer digest.',
    cause_evidence: 'Manual header transcription produced a shortened digest while all other unit headers carried the exact pointer hash.',
    attempts: ['Initial file retained as adverse identity: 1,297 bytes / 0095413CE1A4C34CA0AC2B7656083D2B790DBAB351602DCC4E2C381426030F94.','A bounded one-line patch restored the full pointer digest.'], resolution: 'resolved_metadata_only', residual_risk: 'Manual digest transcription can recur in future target headers.', recurrence_cues: ['hand-copied SHA-256','target custody header'], related_structural_ids: [unitRef('T01_U04')], lexical_basin: 'not_applicable', sense_window: 'metadata identity only', claim_type: 'computation',
  },
  {
    id: 'CJK-KO-P09-HARD-007', locator: 'P09 T01 regional terminology control', symptom: 'South- and North-Korean standards and Hanja disambiguation are not interchangeable.',
    cause_evidence: 'No ko-KP terminology evidence has been gathered; Hangul forms can hide distinct Hanja senses such as integrality and basis terminology.',
    attempts: ['Did not infer ko-KP forms from ko-KR.','Did not use Chinese or Japanese target text as Korean evidence.'], resolution: 'held: provisional ko-KR; Hangul primary; Hanja explanatory metadata only; ko-KP unverified', residual_risk: 'A later regional edition requires separate local evidence.', recurrence_cues: ['계수 homographs','정수적','기저','영역'], related_structural_ids: [workId], lexical_basin: 'mixed/contested', sense_window: 'regional standard and script policy', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-008', locator: 'P09 T01 evidence shelf', symptom: 'Mandarin-Simplified materials can dominate retrieval for Sino-xenic-looking terms without authorizing Korean.',
    cause_evidence: 'A complete Chinese P09 exists in a target-disjoint lane, but local-language authority remains required.',
    attempts: ['Chinese P09 target was not opened or used.'], resolution: 'held qualitative dominance-risk debt; never a scalar', residual_risk: 'Future evidence searches may over-weight Chinese lexical attractors.', recurrence_cues: ['Sino-xenic cognate','search-result dominance','cross-language target reuse'], related_structural_ids: [workId], lexical_basin: 'unresolved', sense_window: 'evidence provenance control, not readiness', claim_type: 'source_fact',
  },
  {
    id: 'CJK-KO-P09-HARD-009', locator: 'evidence/validate.mjs zero-record JSONL predicate', symptom: 'The first validator run reported visual.jsonl terminal LF even though the archival zero-record authority is intentionally a zero-byte file.',
    cause_evidence: 'The shared JSONL reader applied the nonempty-ledger terminal-LF invariant before checking whether the file length was zero.',
    attempts: ['Failed report preserved as evidence/validate.json at 775 bytes / 4E154F525EBF6C0EA1A4219EA655C586124009BDCA8C276757EC43037424651E.','Pre-fix validator was 7,100 bytes / 24DFC2AF61EBB7F7FE9DF2748BD0B71314BD882346D49270E0ED4C2D7E6FAE09.'], resolution: 'resolved: require terminal LF only when JSONL length is nonzero', residual_risk: 'Future validators can accidentally conflate an empty ledger with a malformed nonempty ledger.', recurrence_cues: ['zero-record JSONL','terminal LF invariant','empty visual index'], related_structural_ids: [workId], lexical_basin: 'not_applicable', sense_window: 'validator semantics only', claim_type: 'computation',
  },
].map((entry, index) => {
  const unit = route.tranche.units.find(item => entry.related_structural_ids.includes(unitRecordIds.get(item.id)));
  const target = unit ? targets.get(unit.id) : null;
  return {
    ...entry, recorded_time: '2026-08-04', time_precision: 'day', work_unit: 'Noether P09 Korean T01', authority: { edition_id: 'NOETH-DE-ED-0002', whole_sha256: editionSha, pointer_sha256: pointerSha },
    evidence: target ? { target_path: target.path, target_bytes: target.bytes, target_sha256: target.sha256, source_bytes: unit.bytes, source_sha256: unit.sha256 } : { paper_source_bytes: 77798, paper_source_sha256: route.authority.paper_sha256 },
    related_decision_ids: ['CJK-KO-P09-001'], review_state: entry.resolution.startsWith('resolved') ? 'resolved_not_reviewed' : 'held_for_independent_checker', supersession: null,
    next_revisit: 'independent Korean checker or recurrence in later P09 context', language: 'ko', ko_standard: 'ko-KR_provisional; ko-KP_unverified', mandarin_simplified_dominance_risk: 'qualitative_debt_only', order: index + 1,
  };
});

const diffJsonl = Buffer.from(`${hard.map(record => JSON.stringify(record)).join('\n')}\n`, 'utf8');
const diffSchema = {
  $schema: 'https://json-schema.org/draft/2020-12/schema', title: 'Korean Noether difficulty/failure record', type: 'object', additionalProperties: true,
  required: ['id','recorded_time','time_precision','work_unit','authority','locator','symptom','cause_evidence','attempts','resolution','evidence','residual_risk','recurrence_cues','related_decision_ids','related_structural_ids','review_state','next_revisit','lexical_basin','sense_window','claim_type'],
  properties: { id: { type: 'string', pattern: '^CJK-KO-P09-HARD-[0-9]{3}$' }, recorded_time: { type: 'string' }, time_precision: { enum: ['second','minute','day','unknown'] }, attempts: { type: 'array' }, related_structural_ids: { type: 'array' } },
};

const visualSchema = {
  $schema: 'https://json-schema.org/draft/2020-12/schema', title: 'Korean Noether visual-evidence record', type: 'object', additionalProperties: false,
  required: ['id','kind','parent_scan_path','parent_scan_sha256','page','bbox','width_px','height_px','dpi','rotation_deg','image_path','image_sha256','structural_ids','tex_units','qa_state','review_state','rights_basis','publication_disposition'],
  properties: {
    id: { type: 'string' }, kind: { type: 'string' }, parent_scan_path: { type: ['string','null'] }, parent_scan_sha256: { type: ['string','null'] }, page: { type: ['integer','null'] }, bbox: { type: ['array','null'] }, width_px: { type: ['integer','null'] }, height_px: { type: ['integer','null'] }, dpi: { type: ['number','null'] }, rotation_deg: { type: ['number','null'] }, image_path: { type: ['string','null'] }, image_sha256: { type: ['string','null'] }, structural_ids: { type: 'array' }, tex_units: { type: 'array' }, qa_state: { type: 'string' }, review_state: { type: 'string' }, rights_basis: { type: 'string' }, publication_disposition: { type: 'string' },
  },
};
const visualCsv = Buffer.from('id,kind,parent_scan_path,parent_scan_sha256,page,bbox,width_px,height_px,dpi,rotation_deg,image_path,image_sha256,structural_ids,tex_units,qa_state,review_state,rights_basis,publication_disposition\n', 'utf8');
const visualStatus = {
  scope: 'Korean Noether P09 T01 producer translation', records: 0, files: 0, bytes: 0, render_calls: 0,
  reason: 'Translation-only producer created and used no visual artifacts; zero is not visual QA.',
  rights_disposition: { project_generated: 0, rights_cleared: 0, rights_blocked: 0 }, next_authority_line: 6492,
};

await writeFile(new URL('structure.jsonl', import.meta.url), structureJsonl);
await writeFile(new URL('structure.csv', import.meta.url), structureCsv);
await writeFile(new URL('struct.schema.json', import.meta.url), `${JSON.stringify(structureSchema, null, 2)}\n`, 'utf8');
await writeFile(new URL('diff.jsonl', import.meta.url), diffJsonl);
await writeFile(new URL('diff.schema.json', import.meta.url), `${JSON.stringify(diffSchema, null, 2)}\n`, 'utf8');
await writeFile(new URL('visual.jsonl', import.meta.url), Buffer.alloc(0));
await writeFile(new URL('visual.csv', import.meta.url), visualCsv);
await writeFile(new URL('visual.schema.json', import.meta.url), `${JSON.stringify(visualSchema, null, 2)}\n`, 'utf8');
await writeFile(new URL('visual_status.json', import.meta.url), `${JSON.stringify(visualStatus, null, 2)}\n`, 'utf8');

const sortedTargets = [...targets.values()].sort((a, b) => Buffer.compare(Buffer.from(a.path), Buffer.from(b.path)));
const treeStream = Buffer.from(sortedTargets.map(target => `${target.path}\t${target.bytes}\t${target.sha256}\n`).join(''), 'utf8');
const artifactPath = name => new URL(name, import.meta.url);
const artifactInfo = async name => {
  const data = await readFile(artifactPath(name));
  return { path: `evidence/${name}`, ...info(data) };
};
const manifest = {
  work: 'Noether P09 Korean', authority: route.authority,
  scope: { tranche: 'T01', lines: route.tranche.lines, bytes: route.tranche.bytes, sha256: route.tranche.sha256, next_line: 6492 },
  state: { translation: 'T01_complete_producer_draft', review: 'unchecked', source_check: 'not_performed', formula_check: 'not_performed', build: 'not_run', render: 'not_run', visual_qa: 'not_run', assembly: 'not_run', approval: 'not_approved' },
  target_count: sortedTargets.length, target_bytes: sortedTargets.reduce((sum, target) => sum + target.bytes, 0), target_tree_stream_bytes: treeStream.length, target_tree_sha256: sha(treeStream),
  targets: sortedTargets.map(({ path, bytes, sha256 }) => ({ path, bytes, sha256 })),
  excluded_blank_lines: route.tranche.excluded_blank_lines,
  evidence: await Promise.all(['structure.jsonl','structure.csv','struct.schema.json','diff.jsonl','diff.schema.json','visual.jsonl','visual.csv','visual.schema.json','visual_status.json'].map(artifactInfo)),
};
await writeFile(new URL('manifest.json', root), `${JSON.stringify(manifest, null, 2)}\n`, 'utf8');

const report = {
  result: 'GENERATED', records: { structure: records.length, difficulty: hard.length, visual: 0 },
  latest_ids: { structure: records.at(-1).id, difficulty: hard.at(-1).id }, target_count: manifest.target_count, target_bytes: manifest.target_bytes,
  target_tree_stream_bytes: manifest.target_tree_stream_bytes, target_tree_sha256: manifest.target_tree_sha256, next_authority_line: 6492,
};
await writeFile(new URL('build.json', import.meta.url), `${JSON.stringify(report, null, 2)}\n`, 'utf8');
process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
