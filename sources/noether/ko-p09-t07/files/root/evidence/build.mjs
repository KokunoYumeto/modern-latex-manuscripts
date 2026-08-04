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

const allUnits = [...route.tranche.units, ...route.tranche2.units, ...route.tranche3.units, ...route.tranche4.units, ...route.tranche5.units, ...route.tranche6.units, ...route.tranche7.units];
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
  T05_U30: [['section_title', 6726, 6727, 6, 6]],
  T05_U31: [
    ['definition', 6729, 6735, 6, 6],
    ['source_note', 6733, 6735, 6, 6],
  ],
  T05_U32: [
    ['definition', 6737, 6742, 6, 9],
    ['enumeration', 6739, 6742, 7, 9],
    ['list_item', 6740, 6741, 8, 8],
  ],
  T05_U33: [['proof', 6744, 6750, 6, 6]],
  T05_U34: [['proof', 6752, 6757, 6, 6]],
  T05_U35: [['definition', 6759, 6762, 6, 6]],
  T05_U36: [['statement', 6764, 6771, 6, 6]],
  T05_U37: [['proof', 6773, 6785, 6, 6]],
  T05_U38: [
    ['closed_prose', 6787, 6802, 6, 6],
    ['definition', 6790, 6795, 6, 6],
    ['definition', 6795, 6800, 6, 6],
    ['source_note', 6801, 6801, 6, 6],
  ],
  T05_U39: [
    ['proof', 6804, 6834, 6, 23],
    ['equation', 6807, 6809, 7, 9],
    ['equation', 6812, 6818, 11, 17],
    ['equation', 6821, 6824, 19, 22],
    ['source_note', 6827, 6834, 23, 23],
  ],
  T05_U40: [['proof', 6836, 6844, 6, 6]],
  T05_U41: [['statement', 6846, 6848, 6, 6]],
  T05_U42: [
    ['definition', 6850, 6868, 6, 8],
    ['statement', 6862, 6865, 8, 8],
    ['source_note', 6865, 6868, 8, 8],
  ],
  T05_U43: [
    ['proof', 6870, 6884, 6, 7],
    ['source_note', 6881, 6884, 7, 7],
  ],
  T05_U44: [['closed_prose', 6886, 6890, 6, 6]],
  T05_U45: [
    ['enumeration', 6891, 6909, 6, 9],
    ['list_item', 6892, 6895, 7, 7],
    ['list_item', 6896, 6908, 8, 8],
    ['source_note', 6899, 6908, 8, 8],
  ],
  T06_U46: [['section_title', 6914, 6914, 6, 6]],
  T06_U47: [['closed_prose', 6916, 6921, 6, 6]],
  T06_U48: [['closed_prose', 6923, 6929, 6, 6]],
  T06_U49: [
    ['definition', 6931, 6941, 6, 12],
    ['equation', 6933, 6937, 7, 11],
  ],
  T06_U50: [['closed_prose', 6943, 6945, 6, 6]],
  T06_U51: [
    ['proof', 6946, 6970, 6, 22],
    ['equation', 6950, 6954, 7, 11],
    ['equation', 6959, 6963, 13, 17],
    ['equation', 6968, 6970, 19, 21],
  ],
  T06_U52: [
    ['proof', 6971, 6991, 6, 21],
    ['equation', 6972, 6974, 7, 9],
    ['equation', 6976, 6979, 11, 14],
    ['equation', 6986, 6990, 16, 20],
  ],
  T06_U53: [['statement', 6993, 6995, 6, 6]],
  T06_U54: [['statement', 6997, 7000, 6, 6]],
  T06_U55: [
    ['closed_prose', 7002, 7021, 6, 6],
    ['source_note', 7010, 7011, 6, 6],
    ['source_note', 7014, 7015, 6, 6],
  ],
  T07_U56: [['section_title', 7023, 7025, 6, 7]],
  T07_U57: [
    ['definition', 7027, 7042, 6, 6],
    ['source_note', 7030, 7036, 6, 6],
    ['source_note', 7039, 7042, 6, 6],
  ],
  T07_U58: [
    ['closed_prose', 7044, 7050, 6, 6],
    ['equation', 7047, 7050, 6, 6],
  ],
  T07_U59: [
    ['proof', 7051, 7073, 6, 6],
    ['source_note', 7054, 7055, 6, 6],
    ['source_note', 7066, 7069, 6, 6],
    ['statement', 7070, 7073, 6, 6],
  ],
  T07_U60: [['closed_prose', 7075, 7082, 6, 6]],
  T07_U61: [
    ['proof', 7084, 7094, 6, 6],
    ['statement', 7087, 7092, 6, 6],
  ],
  T07_U62: [
    ['closed_prose', 7096, 7108, 6, 6],
    ['definition', 7096, 7104, 6, 6],
    ['converse', 7104, 7108, 6, 6],
  ],
  T07_U63: [
    ['enumeration', 7109, 7121, 6, 9],
    ['list_item', 7110, 7113, 7, 7],
    ['list_item', 7114, 7120, 8, 8],
    ['source_note', 7118, 7120, 8, 8],
  ],
  T07_U64: [['remark', 7123, 7132, 6, 6]],
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

const tranche5Id = addRecord({
  type: 'tranche', parent_id: workId, order: 5,
  authority: authorityObject(6726, 6913), target: null, relations: [{ type: 'part_of', target_id: workId }], language: 'ko',
  state: recordState('draft_complete'), continuation: { next_authority_line: 6914 },
});
for (const [unitOrder, unit] of route.tranche5.units.entries()) {
  const target = targets.get(unit.id);
  const unitId = addRecord({
    type: 'unit', parent_id: tranche5Id, order: unitOrder + 1,
    authority: authorityObject(unit.lines[0], unit.lines[1]),
    target: { path: target.path, line_start: 1, line_end: target.text.trimEnd().split('\n').length, bytes: target.bytes, sha256: target.sha256 },
    relations: [{ type: 'part_of', target_id: tranche5Id }], language: 'ko',
    state: recordState('draft_complete'), continuation: { next_authority_line: 6914 },
  });
  unitRecordIds.set(unit.id, unitId);
  let childOrder = 0;
  for (const [type, sourceStart, sourceEnd, targetStart, targetEnd] of childSpecs[unit.id]) {
    childOrder += 1;
    addRecord({
      type, parent_id: unitId, order: childOrder,
      authority: authorityObject(sourceStart, sourceEnd), target: targetObject(unit.id, targetStart, targetEnd),
      relations: [{ type: 'contained_in', target_id: unitId }], language: 'ko',
      state: recordState('draft_complete'), continuation: { next_authority_line: 6914 },
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
      state: recordState('draft_complete'), continuation: { next_authority_line: 6914 },
    });
  }
}

const tranche6Id = addRecord({
  type: 'tranche', parent_id: workId, order: 6,
  authority: authorityObject(6914, 7022), target: null, relations: [{ type: 'part_of', target_id: workId }], language: 'ko',
  state: recordState('draft_complete'), continuation: { next_authority_line: 7023 },
});
for (const [unitOrder, unit] of route.tranche6.units.entries()) {
  const target = targets.get(unit.id);
  const unitId = addRecord({
    type: 'unit', parent_id: tranche6Id, order: unitOrder + 1,
    authority: authorityObject(unit.lines[0], unit.lines[1]),
    target: { path: target.path, line_start: 1, line_end: target.text.trimEnd().split('\n').length, bytes: target.bytes, sha256: target.sha256 },
    relations: [{ type: 'part_of', target_id: tranche6Id }], language: 'ko',
    state: recordState('draft_complete'), continuation: { next_authority_line: 7023 },
  });
  unitRecordIds.set(unit.id, unitId);
  let childOrder = 0;
  for (const [type, sourceStart, sourceEnd, targetStart, targetEnd] of childSpecs[unit.id]) {
    childOrder += 1;
    addRecord({
      type, parent_id: unitId, order: childOrder,
      authority: authorityObject(sourceStart, sourceEnd), target: targetObject(unit.id, targetStart, targetEnd),
      relations: [{ type: 'contained_in', target_id: unitId }], language: 'ko',
      state: recordState('draft_complete'), continuation: { next_authority_line: 7023 },
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
      state: recordState('draft_complete'), continuation: { next_authority_line: 7023 },
    });
  }
}

const tranche7Id = addRecord({
  type: 'tranche', parent_id: workId, order: 7,
  authority: authorityObject(7023, 7133), target: null, relations: [{ type: 'part_of', target_id: workId }], language: 'ko',
  state: recordState('draft_complete'), continuation: { next_authority_line: 7134 },
});
for (const [unitOrder, unit] of route.tranche7.units.entries()) {
  const target = targets.get(unit.id);
  const unitId = addRecord({
    type: 'unit', parent_id: tranche7Id, order: unitOrder + 1,
    authority: authorityObject(unit.lines[0], unit.lines[1]),
    target: { path: target.path, line_start: 1, line_end: target.text.trimEnd().split('\n').length, bytes: target.bytes, sha256: target.sha256 },
    relations: [{ type: 'part_of', target_id: tranche7Id }], language: 'ko',
    state: recordState('draft_complete'), continuation: { next_authority_line: 7134 },
  });
  unitRecordIds.set(unit.id, unitId);
  let childOrder = 0;
  for (const [type, sourceStart, sourceEnd, targetStart, targetEnd] of childSpecs[unit.id]) {
    childOrder += 1;
    addRecord({
      type, parent_id: unitId, order: childOrder,
      authority: authorityObject(sourceStart, sourceEnd), target: targetObject(unit.id, targetStart, targetEnd),
      relations: [{ type: 'contained_in', target_id: unitId }], language: 'ko',
      state: recordState('draft_complete'), continuation: { next_authority_line: 7134 },
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
      state: recordState('draft_complete'), continuation: { next_authority_line: 7134 },
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
  {
    id: 'CJK-KO-P09-HARD-022', locator: 'ED0002 lines6729-6762 and throughout §4, targets T05_U31--T05_U35', symptom: 'algebraisch-ganz abhängig, algebraisch-ganz abgeschlossen, and algebraisch-ganze transzendente Zahlen form a historical integrality cluster that is awkward if forced into one Korean adjective.',
    cause_evidence: 'The source gives a monic-equation definition, then separately names closure property V and the subclass of domains satisfying it.',
    attempts: ['Defined 대수적으로 정수이다 first, rendered closure as 대수적 정수성에 관하여 닫혀 있다, and kept the class name analytic.','Rejected a single opaque calque and did not import modern normal-domain terminology.'], resolution: 'held_for_checker', residual_risk: 'The analytic Korean may be longer than established algebra terminology and could blur element-over-domain versus domain-closure scope.', recurrence_cues: ['algebraisch-ganz abhängig','abgeschlossen','Eigenschaft V'], related_structural_ids: [unitRef('T05_U31'),unitRef('T05_U32'),unitRef('T05_U35')], lexical_basin: 'mixed/contested', sense_window: 'integral dependence by a monic equation and closure under such dependence', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-023', locator: 'ED0002 lines6790-6800 and 6850-6857, targets T05_U38/T05_U42', symptom: 'rational-ganze Adjunktion looks like generic rational adjunction although the source immediately defines a polynomial ring.',
    cause_evidence: 'The resulting [G,psi] is explicitly all polynomials in psi with coefficients in G; the independent P06 checker also confirmed ganze rationale Funktionen (Polynome) as polynomial expressions.',
    attempts: ['Rendered rational-ganze Adjunktion as 다항식적 첨가 and algebraisch-ganze Adjunktion separately as 대수적 정수 첨가.','Rejected 유리적 첨가 and did not make a paper-wide substitution outside matching definition windows.'], resolution: 'held_for_checker', residual_risk: 'Historical Korean literature may preserve a different paired term for rational-ganz/algebraisch-ganz.', recurrence_cues: ['rational-ganze Adjunktion','Polynome von psi','algebraisch-ganze Adjunktion'], related_structural_ids: [unitRef('T05_U38'),unitRef('T05_U42')], lexical_basin: 'mixed/contested', sense_window: 'polynomial-ring adjunction versus integral algebraic closure', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-024', locator: 'ED0002 lines6764-6785 and 6870-6880, targets T05_U36/T05_U37/T05_U43', symptom: 'Teiler, größter gemeinsamer Teiler, and teilbar encode a containment lattice, not arithmetic divisibility.',
    cause_evidence: 'The source equates the greatest common divisor with the intersection and proves equality by mutual containment.',
    attempts: ['Used 부분정역 for Teiler and 최대 공통 부분정역, 곧 교집합 for the lattice meet.','Rejected 약수/인수 and made both containments explicit in the converse.'], resolution: 'held_for_checker', residual_risk: 'The historical order convention may be clearer with a dedicated lattice-theoretic gloss.', recurrence_cues: ['Teiler','größter gemeinsamer Teiler','durch H teilbar','Durchschnitt'], related_structural_ids: [unitRef('T05_U36'),unitRef('T05_U37'),unitRef('T05_U43')], lexical_basin: 'mixed/contested', sense_window: 'subdomain containment and intersection lattice', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-025', locator: 'ED0002 lines6804-6834, target T05_U39', symptom: 'The closure proof nests three displays, a product over every root combination, and a long note distinguishing arbitrary from irreducible equations.',
    cause_evidence: 'Dropping any conjugate family, monicity claim, or note scope changes the proof of V and the separate status of IV.',
    attempts: ['Retained all three displays and the source note as separate structural children.','Did not simplify root superscripts or merge the irreducibility discussion into prose outside the note.'], resolution: 'held_for_formula_checker', residual_risk: 'No formula, quantifier, or Korean logical-scope review has occurred.', recurrence_cues: ['product over conjugates','all combinations of roots','arbitrary equation','irreducible equation'], related_structural_ids: [unitRef('T05_U39')], lexical_basin: 'not_applicable', sense_window: 'integral-closure proof by symmetric product over conjugate roots', claim_type: 'source_fact',
  },
  {
    id: 'CJK-KO-P09-HARD-026', locator: 'ED0002 lines6836-6848, targets T05_U40/T05_U41', symptom: 'The three psi examples differ by one factor placement but have opposite consequences for property IV.',
    cause_evidence: 'psi=1/(n eta) brings 1/n into the domain, whereas psi=1/eta and psi=eta/n satisfy IV by the cited/specialization arguments.',
    attempts: ['Preserved all three fractions and restricted the explicit eta=0 argument to the latter case psi=eta/n.','Rejected compressing the examples into a generic denominator statement.'], resolution: 'held_for_formula_checker', residual_risk: 'The cited §2 support for 1/eta and the specialization logic remain independently unchecked.', recurrence_cues: ['1/(n eta)','1/eta','eta/n','latter case'], related_structural_ids: [unitRef('T05_U40'),unitRef('T05_U41')], lexical_basin: 'not_applicable', sense_window: 'property-IV admissibility examples distinguished by factor placement', claim_type: 'source_fact',
  },
  {
    id: 'CJK-KO-P09-HARD-027', locator: 'ED0002 lines6870-6884, target T05_U43', symptom: 'The converse uses set difference L=H-G_eta and two opposite divisibility statements whose direction is easy to reverse.',
    cause_evidence: 'The proof first puts {G,L} inside H by V, then puts H inside {G,L} because it contains both disjoint pieces, yielding equality.',
    attempts: ['Spelled out both 부분정역 containments and the union step.','Rejected a literal passive teilbar rendering that hides the subject of containment.'], resolution: 'held_for_checker', residual_risk: 'The source phrase kein gemeinsames Element and the set-union reconstruction may require a more formal Korean formulation.', recurrence_cues: ['H-G_eta','enthält als Teiler','durch H teilbar','kein gemeinsames Element'], related_structural_ids: [unitRef('T05_U43')], lexical_basin: 'not_applicable', sense_window: 'mutual containment proof for the adjunction converse', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-028', locator: 'ED0002 lines6891-6909, target T05_U45', symptom: 'The final admissible-system note combines a well-order, an exclusion predicate depending on all prior accepted functions, and arbitrary stopping points.',
    cause_evidence: 'All three scopes are needed for the claim that every admissible system is exhausted.',
    attempts: ['Kept the note inside list item b and named the candidate function as the subject of each conditional adjunction.','Rejected flattening the algorithm into an unordered filter.'], resolution: 'held_for_checker', residual_risk: 'The recurrence and stopping quantifiers remain linguistically and logically unchecked.', recurrence_cues: ['Wohlordnung Omega','vorangehenden aufgenommenen','an jeder beliebigen Stelle abgebrochen','erschöpft'], related_structural_ids: [unitRef('T05_U45')], lexical_basin: 'not_applicable', sense_window: 'transfinite construction of admissible systems with optional stopping', claim_type: 'source_fact',
  },
  {
    id: 'CJK-KO-P09-HARD-029', locator: 'ED0002 lines6916-6929 and 6997-7000, targets T06_U47/T06_U48/T06_U54', symptom: 'The fixed-basis family M(G), the containment order called Teiler, and the final intersection claim must stay distinct from membership and arithmetic divisibility.',
    cause_evidence: 'Every member domain contains H and [H], but [H] is itself excluded from the class even though it is later proved to be the intersection of all members.',
    attempts: ['Rendered Teiler through 부분정역 containment and Durchschnitt through 교집합.','Kept the statement that [H] is not a member domain separate from its role as the intersection.','Rejected divisor language and rejected silently adding [H] to the family.'], resolution: 'held_for_checker', residual_risk: 'The provisional 영역/정역 distinction and lattice phrasing remain linguistically unchecked.', recurrence_cues: ['M(G)','zum Teiler','größter gemeinsamer Teiler','Durchschnitt','selbst kein Bereich'], related_structural_ids: [unitRef('T06_U47'),unitRef('T06_U48'),unitRef('T06_U54')], lexical_basin: 'mixed/contested', sense_window: 'fixed-basis family of domains, subdomain containment, and set-theoretic intersection', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-030', locator: 'ED0002 lines6931-6941, target T06_U49', symptom: 'The countable family G_nu combines a power-indexed basis expression with independent coefficient choices for every fixed combination.',
    cause_evidence: 'The quantifiers range over fixed nu, all integer polynomials f, all finite basis selections, and independently varying whole algebraic functions g_i.',
    attempts: ['Preserved equation (1), fixed-nu scope, the basis-power combination, and independent variation of every g_i.','Rejected compressing the definition to a generic module-domain formula.'], resolution: 'held_for_formula_checker', residual_risk: 'The Korean quantifier order and the source abbreviation in inf. remain unchecked.', recurrence_cues: ['für jedes feste nu','jede feste Kombination','einzeln alle','eta_i^nu'], related_structural_ids: [unitRef('T06_U49')], lexical_basin: 'not_applicable', sense_window: 'countable family of generalized module domains indexed by positive integers', claim_type: 'source_fact',
  },
  {
    id: 'CJK-KO-P09-HARD-031', locator: 'ED0002 lines6946-6991, targets T06_U51/T06_U52', symptom: 'The contradiction proof alternates polynomial degree, lowest homogeneous dimension, irreducible equations, and a Tschirnhaus-style shift; literal Dimension as 차원 would obscure the operative degree comparison.',
    cause_evidence: 'The proof compares lower dimensions nu,2nu,... with the upper polynomial bound chi lambda, then chooses nu greater than chi lambda to force the shifted equation to collapse.',
    attempts: ['Used 차수 for the operative Dimension/Grad comparison while preserving chi, lambda, and every displayed equation.','Rejected geometric 차원 and did not simplify the shift xi=z+a_1/chi.'], resolution: 'held_for_formula_checker', residual_risk: 'Historical Dimension versus Grad and the logical step from vanishing c_i to rationality remain independently unchecked.', recurrence_cues: ['Glieder niedrigster Dimension','Gradzahlen','chi lambda','xi=z+a_1/chi'], related_structural_ids: [unitRef('T06_U51'),unitRef('T06_U52')], lexical_basin: 'mixed/contested', sense_window: 'homogeneous polynomial degree bounds in the exclusion proof', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-032', locator: 'ED0002 lines6971-6990, target T06_U52', symptom: 'Numbered displays (4) and (5) combine a shifted polynomial, a congruence modulo b_1/chi, and a terminal three-part vanishing display whose punctuation and scope are easy to damage.',
    cause_evidence: 'The source uses custom numbered-display macros and later cites (5) to derive both c_i=0 and the collapsed chi-th power.',
    attempts: ['Retained srcnumdisplay for (4) and (5), the semicolon, congruence modulus, and final alternatives.','Rejected rewriting the congruence as prose or merging the displays.'], resolution: 'held_for_formula_checker', residual_risk: 'No formula-token or rendered-display review has occurred.', recurrence_cues: ['srcnumdisplay','mod. b_1/chi','c_i=0','xi^chi=0'], related_structural_ids: [unitRef('T06_U52')], lexical_basin: 'not_applicable', sense_window: 'formula topology and congruence in the shifted-equation proof', claim_type: 'source_fact',
  },
  {
    id: 'CJK-KO-P09-HARD-033', locator: 'ED0002 lines7002-7021, target T06_U55', symptom: 'The classification paragraph nests properties I--IV, polynomial adjunction, two field extensions, a primitive-element condition, a converse, two source notes, and forward/backward section references on one target line.',
    cause_evidence: 'Omitting the relative field scopes K over (H) and L over K or detaching either note changes the stated necessary condition and its citation.',
    attempts: ['Kept both source notes in source order, made both relative extension scopes explicit, and retained the primitive-element condition.','Used the construction-defined 다항식적으로 첨가 from §4 rather than a generic rational adjunction.','Rejected splitting notes away from their anchors.'], resolution: 'held_for_checker', residual_risk: 'Korean antecedents, extension direction, and primitive-element wording remain unchecked; one-line TeX topology may be hard to review.', recurrence_cues: ['endlicher Körper K über (H)','Körper L über K','primitives Element','Vgl. § 7','Sätze des § 4'], related_structural_ids: [unitRef('T06_U55')], lexical_basin: 'mixed/contested', sense_window: 'field-extension condition on systems adjoined polynomially to [H]', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-034', locator: 'initial T06 segmentation at ED0002 lines6943-6970, targets T06_U50/T06_U51', symptom: 'The first mechanical split ended U50 at line6946 and began U51 at line6947, cutting one German sentence and moving its final phrase semantically into the preceding target unit.',
    cause_evidence: 'Line6946 ends with außer den Polynomen and line6947 continues f(eta) aus [H] kein weiteres Element gemein haben before the proof begins.',
    attempts: ['Initial unsealed targets were U50 754 B / DFDBBD9DEA032938D2EA8DF72691622C3B5EC38BD9ADBEEF4D281DA2BE57A49C and U51 1,337 B / E852A3F63D93375E52186CF94AB8FD42E641B2DE5DBEB2CB22DBF5FF810803E5.','Before evidence sealing, moved the boundary to U50 lines6943-6945 and U51 lines6946-6970 and moved the already-translated Korean sentence with it.','Rejected retaining a non-closed locator merely because cumulative prose coverage was complete.'], resolution: 'resolved_before_seal', residual_risk: 'Future mechanical paragraph splits can still follow physical lines instead of closed syntax.', recurrence_cues: ['source line ends mid-sentence','unit target contains next unit source meaning','closed-unit boundary'], related_structural_ids: [unitRef('T06_U50'),unitRef('T06_U51')], lexical_basin: 'not_applicable', sense_window: 'segmentation and locator integrity only', claim_type: 'computation',
  },
  {
    id: 'CJK-KO-P09-HARD-035', locator: 'ED0002 lines7027-7042, target T07_U57', symptom: 'The rational-basis definition depends on one well-order, coefficient field K, two long notes, and an order-sensitive radical example; a short cognate label cannot carry these constraints by itself.',
    cause_evidence: 'The first note explains why algebraic-number coefficients occur and how to replace K by Q, while the second distinguishes the basis from linear and transcendence bases through the order eta, root_nu(eta).',
    attempts: ['Retained 유리기저 only together with the complete definition and both notes.','Used 정렬 provisionally for the order condition and kept the forward/reverse radical example.','Rejected treating the basis as an unordered generating set.'], resolution: 'held_for_checker', residual_risk: 'Established Korean terminology for Wohlordnung and rationale Basis, plus the note’s counterfactual coefficient policy, remain unchecked.', recurrence_cues: ['rationale Basis','mindestens einer Wohlordnung','Koeffizienten aus K','Anordnung der Elemente'], related_structural_ids: [unitRef('T07_U57')], lexical_basin: 'modern Sino-xenic coinage/calque', sense_window: 'order-sensitive rational generating basis over algebraic-number coefficients', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-036', locator: 'ED0002 lines7044-7060, targets T07_U58/T07_U59', symptom: 'The transfinite-style induction removes every element rationally expressible from finitely many predecessors and proves the remaining theta system generates all prior relations; antecedent direction is easy to reverse.',
    cause_evidence: 'The contradiction chooses the first z_0 not expressible through theta even though each preceding xi is already a rational function of theta.',
    attempts: ['Separated the initial eliminable-element description from the remaining-system proof at a closed paragraph boundary.','Named z_0, the preceding xi, and the theta expressions explicitly.','Rejected compressing the argument to a generic induction claim.'], resolution: 'held_for_checker', residual_risk: 'The well-order induction, rational independence clause, and relation direction remain linguistically and logically unchecked.', recurrence_cues: ['Induktionsschluß','erstes Element z_0','vorangehenden xi','rational unabhängig'], related_structural_ids: [unitRef('T07_U58'),unitRef('T07_U59')], lexical_basin: 'not_applicable', sense_window: 'well-order induction proving the residual system is a rational basis', claim_type: 'source_fact',
  },
  {
    id: 'CJK-KO-P09-HARD-037', locator: 'ED0002 lines7060-7073, target T07_U59', symptom: 'The Nebenbedingung is not an arbitrary extra condition: it specifically excludes algebraically fractional numbers from [Theta], with a factor-sensitive admissibility example.',
    cause_evidence: 'The source contrasts eta with 1/(2 sqrt eta), which is inadmissible, against eta with 1/sqrt eta, which is admissible.',
    attempts: ['Rendered the defined phrase consistently as 부가조건을 만족하는 유리기저 and repeated the exact exclusion predicate.','Preserved both near-identical pairs and their factor 2.','Rejected a generic 조건부 기저 label detached from the predicate.'], resolution: 'held_for_checker', residual_risk: 'The provisional 분수형 대수수 and 부가조건 terminology, and the example’s algebraic justification, remain unchecked.', recurrence_cues: ['rationale Basis mit Nebenbedingung','keine algebraisch-gebrochene Zahl','1/(2 sqrt eta)','1/sqrt eta'], related_structural_ids: [unitRef('T07_U59')], lexical_basin: 'mixed/contested', sense_window: 'side condition excluding algebraically fractional constants from the polynomial domain', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-038', locator: 'ED0002 lines7075-7094, targets T07_U60/T07_U61', symptom: 'Unlike §5, [Theta] is itself a member domain here, so the intersection family N(G) is closed under arbitrary subsystem intersections; carrying over the earlier exclusion would reverse the theorem.',
    cause_evidence: 'The source proves [Theta] satisfies I, III, IV and uses it as the contained subdomain establishing II and III for each intersection.',
    attempts: ['Kept M(G) and N(G) distinct and explicitly stated that [Theta] itself is a domain G.','Rendered Teiler again through subdomain containment and retained the separate proof of IV.','Rejected mechanically copying the §5 conclusion that the family is not closed.'], resolution: 'held_for_checker', residual_risk: 'The lattice directions and the proof that arbitrary subsystem intersections remain in N(G) require independent logical review.', recurrence_cues: ['N(G)','[Theta] selbst ein Bereich','abgeschlossen in bezug auf Durchschnittbildung','Teiler'], related_structural_ids: [unitRef('T07_U60'),unitRef('T07_U61')], lexical_basin: 'mixed/contested', sense_window: 'fixed-rational-basis family closed under subsystem intersections', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-039', locator: 'ED0002 lines7096-7121, targets T07_U62/T07_U63', symptom: 'rational-ganze Adjunktion, zulässiges System, and Restsystem define a polynomial adjunction classification whose admissibility is exactly the non-entry of algebraically fractional numbers.',
    cause_evidence: 'The resulting [Theta,S] is an integral domain satisfying I--III, and the converse chooses S=G-[Theta].',
    attempts: ['Reused construction-defined 다항식적 첨가 from §4/§5 and rendered zulässiges System as 허용 가능한 계.','Kept the remainder system G-[Theta] explicit and preserved the a/b enumeration plus source note.','Rejected generic rational adjunction and a paper-wide replacement beyond this definition window.'], resolution: 'held_for_checker', residual_risk: 'The historical rational-ganz label, set-difference system, and admissibility predicate remain unchecked.', recurrence_cues: ['rational-ganze Adjunktion','zulässiges System','Restsystem','G-[Theta]'], related_structural_ids: [unitRef('T07_U62'),unitRef('T07_U63')], lexical_basin: 'mixed/contested', sense_window: 'polynomial adjunction of a permissible residual system to [Theta]', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-040', locator: 'ED0002 lines7123-7132, target T07_U64', symptom: 'The closing remark relates an algebraische Basis H inside Theta, extension to a rational basis, and a decomposition S=S_1 union S_2; the two adjunction stages have different roles.',
    cause_evidence: 'S_1 extends H to a rational basis with side condition, whereas S_2 is subsequently adjoined polynomially as an admissible system.',
    attempts: ['Rendered historical algebraische Basis as 초월기저 within its already-defined sense window.','Kept S_1 and S_2 separate and named the two stages explicitly.','Rejected collapsing both stages into one adjunction.'], resolution: 'held_for_checker', residual_risk: 'The basis-extension equivalence and subsystem roles remain unchecked.', recurrence_cues: ['H aus Theta herausgreifen','zu einer rationalen ergänzen','S_1 und S_2','noch adjungiert'], related_structural_ids: [unitRef('T07_U64')], lexical_basin: 'mixed/contested', sense_window: 'decomposition of the algebraic-basis construction through a rational-basis extension', claim_type: 'editorial_inference',
  },
  {
    id: 'CJK-KO-P09-HARD-041', locator: 'T07 target creation transport and targets/T07_U60.tex', symptom: 'Two initial patch transports failed before writing because TeX backslashes and TeX grave-accent quotes conflicted with JavaScript string syntax; a later bounded phrase patch temporarily dropped the opening math delimiter in U60.',
    cause_evidence: 'A standard JavaScript string parsed backslash-xi as an invalid hexadecimal escape; a raw tagged template was terminated by TeX double grave accents; the subsequent line patch omitted the first dollar byte.',
    attempts: ['Both failed add-file patches wrote zero files.','Reissued smaller raw-template patches after replacing TeX grave-accent quotes with glqq/grqq.','Detected the U60 delimiter loss on immediate readback; intermediate identity was 996 B / 3C462841FEFE89E741054F0E77268892ECACED9671B06F020B2C85156215C43F, then restored the opening dollar before evidence generation.'], resolution: 'resolved_before_seal', residual_risk: 'Large TeX patches can still collide with orchestration-language quoting or lose one-byte delimiters during manual line replacement.', recurrence_cues: ['Invalid hexadecimal escape','String.raw is not a function','leading math delimiter missing','large TeX patch'], related_structural_ids: [unitRef('T07_U60')], lexical_basin: 'not_applicable', sense_window: 'tooling and TeX transport only', claim_type: 'computation',
  },
].map((entry, index) => {
  const unit = allUnits.find(item => entry.related_structural_ids.includes(unitRecordIds.get(item.id)));
  const target = unit ? targets.get(unit.id) : null;
  return {
    ...entry, recorded_time: '2026-08-04', time_precision: 'day', work_unit: Number(entry.id.slice(-3)) >= 35 ? 'Noether P09 Korean T07' : Number(entry.id.slice(-3)) >= 29 ? 'Noether P09 Korean T06' : Number(entry.id.slice(-3)) >= 22 ? 'Noether P09 Korean T05' : Number(entry.id.slice(-3)) >= 18 ? 'Noether P09 Korean T04' : 'Noether P09 Korean T01', authority: { edition_id: 'NOETH-DE-ED-0002', whole_sha256: editionSha, pointer_sha256: pointerSha },
    evidence: target ? { target_path: target.path, target_bytes: target.bytes, target_sha256: target.sha256, source_bytes: unit.bytes, source_sha256: unit.sha256 } : { paper_source_bytes: 77798, paper_source_sha256: route.authority.paper_sha256 },
    related_decision_ids: Number(entry.id.slice(-3)) >= 35 ? ['CJK-KO-P09-007'] : Number(entry.id.slice(-3)) >= 29 ? ['CJK-KO-P09-006'] : Number(entry.id.slice(-3)) >= 22 ? ['CJK-KO-P09-005'] : Number(entry.id.slice(-3)) >= 18 ? ['CJK-KO-P09-004'] : ['CJK-KO-P09-001'], review_state: entry.resolution.startsWith('resolved') ? 'resolved_not_reviewed' : 'held_for_independent_checker', supersession: null,
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
  scope: 'Korean Noether P09 T01--T07 producer translation', records: 0, files: 0, bytes: 0, render_calls: 0,
  reason: 'Translation-only producer created and used no visual artifacts; zero is not visual QA.',
  rights_disposition: { project_generated: 0, rights_cleared: 0, rights_blocked: 0 }, next_authority_line: 7134,
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
  scope: { tranches: ['T01','T02','T03','T04','T05','T06','T07'], lines: [6348,7133], bytes: lineBytes(authorityLines,6348,7133).length, sha256: sha(lineBytes(authorityLines,6348,7133)), next_line: 7134 },
  state: { translation: 'T01_T07_complete_producer_draft', review: 'unchecked', source_check: 'not_performed', formula_check: 'not_performed', build: 'not_run', render: 'not_run', visual_qa: 'not_run', assembly: 'not_run', approval: 'not_approved' },
  target_count: sortedTargets.length, target_bytes: sortedTargets.reduce((sum, target) => sum + target.bytes, 0), target_tree_stream_bytes: treeStream.length, target_tree_sha256: sha(treeStream),
  targets: sortedTargets.map(({ path, bytes, sha256 }) => ({ path, bytes, sha256 })),
  excluded_blank_lines: [...route.tranche.excluded_blank_lines, ...route.tranche2.excluded_blank_lines, ...route.tranche3.excluded_blank_lines, ...route.tranche4.excluded_blank_lines, ...route.tranche5.excluded_blank_lines, ...route.tranche6.excluded_blank_lines, ...route.tranche7.excluded_blank_lines],
  evidence: await Promise.all(['structure.jsonl','structure.csv','struct.schema.json','diff.jsonl','diff.schema.json','visual.jsonl','visual.csv','visual.schema.json','visual_status.json'].map(artifactInfo)),
};
await writeFile(new URL('manifest.json', root), `${JSON.stringify(manifest, null, 2)}\n`, 'utf8');

const report = {
  result: 'GENERATED', records: { structure: records.length, difficulty: hard.length, visual: 0 },
  latest_ids: { structure: records.at(-1).id, difficulty: hard.at(-1).id }, target_count: manifest.target_count, target_bytes: manifest.target_bytes,
  target_tree_stream_bytes: manifest.target_tree_stream_bytes, target_tree_sha256: manifest.target_tree_sha256, next_authority_line: 7134,
};
await writeFile(new URL('build.json', import.meta.url), `${JSON.stringify(report, null, 2)}\n`, 'utf8');
process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
