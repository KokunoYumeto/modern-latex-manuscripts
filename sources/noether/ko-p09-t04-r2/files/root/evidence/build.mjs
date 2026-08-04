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

const allUnits = [...route.tranche.units, ...route.tranche2.units, ...route.tranche3.units, ...route.tranche4.units];
const targets = new Map();
for (const unit of allUnits) {
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
  T02_U12: [['section_title', 6492, 6493, 6, 6]],
  T02_U13: [
    ['closed_prose', 6495, 6511, 6, 6],
    ['proof', 6495, 6511, 6, 6],
  ],
  T02_U14: [
    ['remark', 6513, 6522, 6, 6],
    ['example', 6516, 6522, 6, 6],
  ],
  T03_U15: [['section_title', 6524, 6524, 6, 6]],
  T03_U16: [['closed_prose', 6526, 6529, 6, 6]],
  T03_U17: [
    ['definition', 6531, 6546, 6, 11],
    ['source_note', 6531, 6532, 6, 6],
    ['equation', 6535, 6538, 7, 10],
    ['closed_prose', 6539, 6546, 11, 11],
  ],
  T03_U18: [['definition', 6548, 6552, 6, 6]],
  T03_U19: [
    ['proof', 6554, 6571, 6, 6],
    ['source_note', 6560, 6561, 6, 6],
    ['source_note', 6562, 6563, 6, 6],
    ['lemma', 6563, 6566, 6, 6],
    ['source_note', 6566, 6566, 6, 6],
    ['lemma', 6566, 6569, 6, 6],
  ],
  T03_U20: [
    ['proof', 6573, 6594, 6, 14],
    ['statement', 6573, 6575, 6, 6],
    ['equation', 6578, 6580, 7, 9],
    ['equation', 6582, 6584, 11, 13],
    ['source_note', 6587, 6592, 14, 14],
  ],
  T03_U21: [['remark', 6596, 6598, 6, 6]],
  T04_U22: [['section_title', 6600, 6600, 6, 6]],
  T04_U23: [
    ['closed_prose', 6602, 6611, 6, 6],
    ['source_note', 6605, 6610, 6, 6],
  ],
  T04_U24: [
    ['definition', 6613, 6623, 6, 12],
    ['equation', 6614, 6618, 7, 11],
    ['source_note', 6622, 6623, 12, 12],
  ],
  T04_U25: [
    ['proof', 6625, 6648, 6, 14],
    ['equation', 6636, 6638, 7, 9],
    ['equation', 6640, 6642, 11, 13],
    ['source_note', 6645, 6647, 14, 14],
  ],
  T04_U26: [
    ['statement', 6650, 6659, 6, 10],
    ['equation', 6655, 6657, 7, 9],
  ],
  T04_U27: [
    ['proof', 6661, 6684, 6, 21],
    ['equation', 6663, 6666, 7, 10],
    ['equation', 6675, 6678, 12, 15],
    ['equation', 6681, 6684, 17, 20],
  ],
  T04_U28: [
    ['proof', 6685, 6710, 6, 18],
    ['equation', 6686, 6688, 7, 9],
    ['equation', 6694, 6696, 11, 13],
    ['equation', 6701, 6703, 15, 17],
    ['statement', 6707, 6710, 18, 18],
  ],
  T04_U29: [
    ['remark', 6712, 6724, 6, 11],
    ['equation', 6715, 6718, 7, 10],
  ],
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

const tranche2Id = addRecord({
  type: 'tranche', parent_id: workId, order: 2,
  authority: authorityObject(6492, 6523), target: null, relations: [{ type: 'part_of', target_id: workId }], language: 'ko',
  state: recordState('draft_complete'), continuation: { next_authority_line: 6524 },
});
for (const [unitOrder, unit] of route.tranche2.units.entries()) {
  const target = targets.get(unit.id);
  const unitId = addRecord({
    type: 'unit', parent_id: tranche2Id, order: unitOrder + 1,
    authority: authorityObject(unit.lines[0], unit.lines[1]),
    target: { path: target.path, line_start: 1, line_end: target.text.trimEnd().split('\n').length, bytes: target.bytes, sha256: target.sha256 },
    relations: [{ type: 'part_of', target_id: tranche2Id }], language: 'ko',
    state: recordState('draft_complete'), continuation: { next_authority_line: 6524 },
  });
  unitRecordIds.set(unit.id, unitId);
  let childOrder = 0;
  for (const [type, sourceStart, sourceEnd, targetStart, targetEnd] of childSpecs[unit.id]) {
    childOrder += 1;
    addRecord({
      type, parent_id: unitId, order: childOrder,
      authority: authorityObject(sourceStart, sourceEnd), target: targetObject(unit.id, targetStart, targetEnd),
      relations: [{ type: 'contained_in', target_id: unitId }], language: 'ko',
      state: recordState('draft_complete'), continuation: { next_authority_line: 6524 },
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
      state: recordState('draft_complete'), continuation: { next_authority_line: 6524 },
    });
  }
}

const tranche3Id = addRecord({
  type: 'tranche', parent_id: workId, order: 3,
  authority: authorityObject(6524, 6599), target: null, relations: [{ type: 'part_of', target_id: workId }], language: 'ko',
  state: recordState('draft_complete'), continuation: { next_authority_line: 6600 },
});
for (const [unitOrder, unit] of route.tranche3.units.entries()) {
  const target = targets.get(unit.id);
  const unitId = addRecord({
    type: 'unit', parent_id: tranche3Id, order: unitOrder + 1,
    authority: authorityObject(unit.lines[0], unit.lines[1]),
    target: { path: target.path, line_start: 1, line_end: target.text.trimEnd().split('\n').length, bytes: target.bytes, sha256: target.sha256 },
    relations: [{ type: 'part_of', target_id: tranche3Id }], language: 'ko',
    state: recordState('draft_complete'), continuation: { next_authority_line: 6600 },
  });
  unitRecordIds.set(unit.id, unitId);
  let childOrder = 0;
  for (const [type, sourceStart, sourceEnd, targetStart, targetEnd] of childSpecs[unit.id]) {
    childOrder += 1;
    addRecord({
      type, parent_id: unitId, order: childOrder,
      authority: authorityObject(sourceStart, sourceEnd), target: targetObject(unit.id, targetStart, targetEnd),
      relations: [{ type: 'contained_in', target_id: unitId }], language: 'ko',
      state: recordState('draft_complete'), continuation: { next_authority_line: 6600 },
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
      state: recordState('draft_complete'), continuation: { next_authority_line: 6600 },
    });
  }
}

const tranche4Id = addRecord({
  type: 'tranche', parent_id: workId, order: 4,
  authority: authorityObject(6600, 6725), target: null, relations: [{ type: 'part_of', target_id: workId }], language: 'ko',
  state: recordState('draft_complete'), continuation: { next_authority_line: 6726 },
});
for (const [unitOrder, unit] of route.tranche4.units.entries()) {
  const target = targets.get(unit.id);
  const unitId = addRecord({
    type: 'unit', parent_id: tranche4Id, order: unitOrder + 1,
    authority: authorityObject(unit.lines[0], unit.lines[1]),
    target: { path: target.path, line_start: 1, line_end: target.text.trimEnd().split('\n').length, bytes: target.bytes, sha256: target.sha256 },
    relations: [{ type: 'part_of', target_id: tranche4Id }], language: 'ko',
    state: recordState('draft_complete'), continuation: { next_authority_line: 6726 },
  });
  unitRecordIds.set(unit.id, unitId);
  let childOrder = 0;
  for (const [type, sourceStart, sourceEnd, targetStart, targetEnd] of childSpecs[unit.id]) {
    childOrder += 1;
    addRecord({
      type, parent_id: unitId, order: childOrder,
      authority: authorityObject(sourceStart, sourceEnd), target: targetObject(unit.id, targetStart, targetEnd),
      relations: [{ type: 'contained_in', target_id: unitId }], language: 'ko',
      state: recordState('draft_complete'), continuation: { next_authority_line: 6726 },
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
      state: recordState('draft_complete'), continuation: { next_authority_line: 6726 },
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
  {
    id: 'CJK-KO-P09-HARD-010', locator: 'ED0002 lines6508-6511, target T02_U13', symptom: 'Teiler can attract the ordinary divisor/factor sense even though the sentence states a containment relation between domains.',
    cause_evidence: 'The source says G contains the integral domain [H] as Teiler after proving closure under its polynomials.',
    attempts: ['Rejected 인수 and 약수 as misleading in the sentence.'], resolution: 'held_provisional: 정역 [H]를 부분정역으로 포함한다', residual_risk: 'Historical ring-theory usage may require a more exact Korean term.', recurrence_cues: ['als Teiler enthalten','Teiler eines Bereichs'], related_structural_ids: [unitRef('T02_U13')], lexical_basin: 'mixed/contested', sense_window: 'domain containment, not an arithmetic divisor', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-011', locator: 'ED0002 lines6513-6522, target T02_U14', symptom: 'The basis-replacement remark compresses a change of distinguished basis and a new domain into one example.',
    cause_evidence: 'Replacing eta by f(eta) removes eta and [H] from G-prime, while replacing eta by xi=f(eta) in H yields a new transcendence basis H-prime relative to which properties 1 and 2 hold.',
    attempts: ['Kept G-prime and H-prime distinct and retained both negative containments.'], resolution: 'held_for_checker: exact logical scope preserved provisionally', residual_risk: 'Korean antecedents may still blur which replacement acts on the construction versus the basis.', recurrence_cues: ['ersetzt man','in der ganzen Konstruktion','in der Basis'], related_structural_ids: [unitRef('T02_U14')], lexical_basin: 'not_applicable', sense_window: 'basis-change example and logical scope', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-012', locator: 'ED0002 lines6529-6546 and throughout §2', symptom: 'rationales Funktional can be mistaken for a functional in the modern functional-analysis sense.',
    cause_evidence: 'Weber defines it here as a uniquely normalized rational function a E1/E2 with primitive coprime integer polynomials.',
    attempts: ['Rejected 범함수 and 기능적 표현.'], resolution: 'held_provisional: 유리 함수식; ganzes/gebrochenes rationales Funktional becomes 정수적/분수형 유리 함수식', residual_risk: 'An established Korean history-of-algebra term may differ.', recurrence_cues: ['Funktional','Funktionalbereich','ganze Funktionale'], related_structural_ids: [unitRef('T03_U16'),unitRef('T03_U17'),unitRef('T03_U18')], lexical_basin: 'mixed/contested', sense_window: 'normalized rational-function expression in Weber terminology', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-013', locator: 'ED0002 lines6539-6542, target T03_U17', symptom: 'Betrag von A may denote the positive rational content/factor, while modern 절댓값 suggests pointwise absolute value.',
    cause_evidence: 'The source defines a as the positive rational factor in the normalized expression and parenthetically calls it the absolute Betrag of A.',
    attempts: ['Retained source-near 절댓값 but marked the content sense for checker review.'], resolution: 'held_for_checker', residual_risk: 'The provisional Korean may obscure the Gauss-content interpretation.', recurrence_cues: ['Betrag von A','primitive Polynome','positive rationale Zahl'], related_structural_ids: [unitRef('T03_U17')], lexical_basin: 'mixed/contested', sense_window: 'positive rational normalization factor/content', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-014', locator: 'ED0002 lines6554-6571, target T03_U19', symptom: 'Three nested source notes and two quoted lemmas occupy one physical Korean line and can lose scope or citation attachment.',
    cause_evidence: 'The source attaches separate Weber references to the domain argument, extended Gauss theorem, and first irreducibility lemma.',
    attempts: ['Retained all three srcfn macros in source order and indexed each note and lemma separately.'], resolution: 'held_for_checker: topology preserved mechanically', residual_risk: 'Linguistic attachment and lemma equivalence remain unreviewed.', recurrence_cues: ['multiple srcfn on one paragraph','quoted Hilfssätze'], related_structural_ids: [unitRef('T03_U19')], lexical_basin: 'not_applicable', sense_window: 'citation and lemma scope', claim_type: 'source_fact',
  },
  {
    id: 'CJK-KO-P09-HARD-015', locator: 'ED0002 lines6573-6594, target T03_U20', symptom: 'The exclusion proof depends on preserving both displayed equations and the sequence a_k/z, a_k/sqrt(z), a_k/cuberoot(z).',
    cause_evidence: 'Those elements show that any proposed basis element forces forbidden fractional functions into G.',
    attempts: ['Kept the formulas and universal-well-order scope explicit; did not simplify the radicals.'], resolution: 'held_for_formula_checker', residual_risk: 'No formula or logical verification has been performed by the producer.', recurrence_cues: ['a_k/z','root tower','Basiseigenschaften 4 und 5'], related_structural_ids: [unitRef('T03_U20')], lexical_basin: 'not_applicable', sense_window: 'formula-driven exclusion argument', claim_type: 'source_fact',
  },
  {
    id: 'CJK-KO-P09-HARD-016', locator: 'read-only T03 target enumeration command', symptom: 'Get-ChildItem -LiteralPath with a wildcard treated T03_*.tex literally and failed before reading any target.',
    cause_evidence: 'PowerShell -LiteralPath intentionally disables wildcard expansion.',
    attempts: ['Failed command wrote zero files.','Corrected command used -LiteralPath on the directory plus -Filter T03_*.tex and succeeded read-only.'], resolution: 'resolved_operational', residual_risk: 'LiteralPath/glob confusion can recur in evidence enumeration.', recurrence_cues: ['-LiteralPath with *','Get-ChildItem wildcard'], related_structural_ids: [workId], lexical_basin: 'not_applicable', sense_window: 'tooling only', claim_type: 'computation',
  },
  {
    id: 'CJK-KO-P09-HARD-017', locator: 'targets/T03_U15.tex line2 and evidence builder locator predicate', symptom: 'The first T03 build stopped because the single-line header said ED0002 line6524 while the structured predicate required lines6524--6524.',
    cause_evidence: 'Human-readable singular-line metadata and the machine-normalized inclusive-range grammar diverged despite identifying the same source line.',
    attempts: ['Pre-fix target identity preserved as 430 bytes / 3A909626CD279465178A8BDA0262C120B893CE271183018B7AF215B6CCD57FA5.','Failed build stopped before generating or overwriting evidence outputs.','One metadata-only patch normalized the header to lines6524--6524.'], resolution: 'resolved_metadata_only', residual_risk: 'Future one-line units may alternate between singular and inclusive-range header grammars.', recurrence_cues: ['single-line source unit','locator header mismatch'], related_structural_ids: [unitRef('T03_U15')], lexical_basin: 'not_applicable', sense_window: 'metadata grammar only', claim_type: 'computation',
  },
  {
    id: 'CJK-KO-P09-HARD-018', locator: 'ED0002 lines6602-6611 and 6719-6724, targets T04_U23/T04_U29', symptom: 'ganz, ganzzahlig, ganze algebraische Funktion, and algebraisch-ganz distinguish coefficient and integrality senses that a single Korean 정수적 label can collapse.',
    cause_evidence: 'The opening footnote explicitly defines whole algebraic functions through monic equations with [H]-polynomial coefficients, while the closing remark permits algebraically integral but not necessarily ganzzahlig functions.',
    attempts: ['Retained 정수적 대수함수 for the defined class and expanded the closing contrast as 대수적으로 정수이되 반드시 정수적인 계수를 갖지는 않는.','Rejected a silent paper-wide normalization because later sections may use the cognates differently.'], resolution: 'held_for_checker', residual_risk: 'The Korean expansion may still over-specify coefficient language at line6719.', recurrence_cues: ['ganze algebraische Funktionen','ganzzahligen Koeffizienten','algebraisch-ganzen','nicht notwendig ganzzahligen'], related_structural_ids: [unitRef('T04_U23'),unitRef('T04_U29')], lexical_basin: 'mixed/contested', sense_window: 'historical integrality of algebraic functions versus integral coefficients', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-019', locator: 'ED0002 lines6602-6623, targets T04_U23/T04_U24', symptom: 'Modulbereich and Moduleigenschaft can attract a modern module-over-a-ring reading not fully specified in this local construction.',
    cause_evidence: 'The source itself defines the domain by expressions z=alpha+sum g_i eta_i and says the module property belongs to z-alpha.',
    attempts: ['Used source-near 모듈 영역 and 모듈 성질 while retaining the defining formula and note verbatim in TeX topology.','Applied the P06 independent checker’s same-language Modulbasis correction to 가군 기저, without extending that decision to Bereich or Eigenschaft.','Rejected importing a modern module definition absent from the source.'], resolution: 'held_for_checker', residual_risk: 'An established Korean historical-algebra label may differ for Bereich and Eigenschaft.', recurrence_cues: ['Modulbereich','Modulbasis','Moduleigenschaft','z-alpha'], related_structural_ids: [unitRef('T04_U23'),unitRef('T04_U24')], lexical_basin: 'modern Sino-xenic coinage/calque', sense_window: 'domain defined by an additive module-like expression over algebraic-function coefficients', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-020', locator: 'ED0002 lines6685-6710, target T04_U28', symptom: 'homogene Form nu-ter Dimension is used in a degree argument and literal 차원 can obscure the polynomial degree role.',
    cause_evidence: 'The next sentences compare the form with polynomial Grad lambda and derive lambda >= nu chi.',
    attempts: ['Rendered the two occurrences as nu차 and nu chi차 동차형식 to preserve the operative degree argument.','Rejected a literal nu차원 rendering.'], resolution: 'held_for_formula_checker', residual_risk: 'Historical invariant-theory terminology may distinguish Dimension and Grad more sharply than the provisional Korean.', recurrence_cues: ['Form nu-ter Dimension','Grad lambda','homogene Form'], related_structural_ids: [unitRef('T04_U28')], lexical_basin: 'mixed/contested', sense_window: 'homogeneous polynomial degree in the basis quantities', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-021', locator: 'evidence validator discovery after T04 target creation', symptom: 'The first read-only validator lookup assumed validate.mjs was in the P09 root although it is stored under evidence/.',
    cause_evidence: 'The lookup returned path-not-found and the directory listing immediately located evidence/validate.mjs; no write occurred.',
    attempts: ['Failed read-only lookup wrote zero files.','Corrected all subsequent calls to evidence/validate.mjs.'], resolution: 'resolved_operational', residual_risk: 'Root/evidence script-location assumptions can recur when tranche builders are extended.', recurrence_cues: ['validate.mjs path','root versus evidence directory'], related_structural_ids: [workId], lexical_basin: 'not_applicable', sense_window: 'tooling only', claim_type: 'computation',
  },
].map((entry, index) => {
  const unit = allUnits.find(item => entry.related_structural_ids.includes(unitRecordIds.get(item.id)));
  const target = unit ? targets.get(unit.id) : null;
  return {
    ...entry, recorded_time: '2026-08-04', time_precision: 'day', work_unit: Number(entry.id.slice(-3)) >= 18 ? 'Noether P09 Korean T04' : 'Noether P09 Korean T01', authority: { edition_id: 'NOETH-DE-ED-0002', whole_sha256: editionSha, pointer_sha256: pointerSha },
    evidence: target ? { target_path: target.path, target_bytes: target.bytes, target_sha256: target.sha256, source_bytes: unit.bytes, source_sha256: unit.sha256 } : { paper_source_bytes: 77798, paper_source_sha256: route.authority.paper_sha256 },
    related_decision_ids: Number(entry.id.slice(-3)) >= 18 ? ['CJK-KO-P09-004'] : ['CJK-KO-P09-001'], review_state: entry.resolution.startsWith('resolved') ? 'resolved_not_reviewed' : 'held_for_independent_checker', supersession: null,
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
  scope: 'Korean Noether P09 T01--T04 producer translation', records: 0, files: 0, bytes: 0, render_calls: 0,
  reason: 'Translation-only producer created and used no visual artifacts; zero is not visual QA.',
  rights_disposition: { project_generated: 0, rights_cleared: 0, rights_blocked: 0 }, next_authority_line: 6726,
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
  scope: { tranches: ['T01','T02','T03','T04'], lines: [6348,6725], bytes: lineBytes(authorityLines,6348,6725).length, sha256: sha(lineBytes(authorityLines,6348,6725)), next_line: 6726 },
  state: { translation: 'T01_T04_complete_producer_draft', review: 'unchecked', source_check: 'not_performed', formula_check: 'not_performed', build: 'not_run', render: 'not_run', visual_qa: 'not_run', assembly: 'not_run', approval: 'not_approved' },
  target_count: sortedTargets.length, target_bytes: sortedTargets.reduce((sum, target) => sum + target.bytes, 0), target_tree_stream_bytes: treeStream.length, target_tree_sha256: sha(treeStream),
  targets: sortedTargets.map(({ path, bytes, sha256 }) => ({ path, bytes, sha256 })),
  excluded_blank_lines: [...route.tranche.excluded_blank_lines, ...route.tranche2.excluded_blank_lines, ...route.tranche3.excluded_blank_lines, ...route.tranche4.excluded_blank_lines],
  evidence: await Promise.all(['structure.jsonl','structure.csv','struct.schema.json','diff.jsonl','diff.schema.json','visual.jsonl','visual.csv','visual.schema.json','visual_status.json'].map(artifactInfo)),
};
await writeFile(new URL('manifest.json', root), `${JSON.stringify(manifest, null, 2)}\n`, 'utf8');

const report = {
  result: 'GENERATED', records: { structure: records.length, difficulty: hard.length, visual: 0 },
  latest_ids: { structure: records.at(-1).id, difficulty: hard.at(-1).id }, target_count: manifest.target_count, target_bytes: manifest.target_bytes,
  target_tree_stream_bytes: manifest.target_tree_stream_bytes, target_tree_sha256: manifest.target_tree_sha256, next_authority_line: 6726,
};
await writeFile(new URL('build.json', import.meta.url), `${JSON.stringify(report, null, 2)}\n`, 'utf8');
process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
