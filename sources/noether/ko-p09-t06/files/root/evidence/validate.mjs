import { readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';

const root = new URL('../', import.meta.url);
const sha = data => createHash('sha256').update(data).digest('hex').toUpperCase();
const errors = [];
const route = JSON.parse(await readFile(new URL('route.json', root), 'utf8'));
const manifest = JSON.parse(await readFile(new URL('manifest.json', root), 'utf8'));
const allUnits = [...route.tranche.units, ...route.tranche2.units, ...route.tranche3.units, ...route.tranche4.units, ...route.tranche5.units, ...route.tranche6.units];
const authorityRaw = await readFile('C:/Users/Floris/Documents/interlanguage/03_projects/noether/07_german_canon_control/candidates/ED0002/noether.tex');
const lines = authorityRaw.toString('utf8').replaceAll('\r\n', '\n').split('\n');
const lineBytes = (start, end) => Buffer.from(`${lines.slice(start - 1, end).join('\n')}\n`, 'utf8');
const targetMap = new Map();

if (authorityRaw.length !== 2153554 || sha(authorityRaw) !== route.authority.whole_sha256) errors.push('authority identity');
const paper = lineBytes(6348, 7679);
if (paper.length !== route.authority.paper_bytes || sha(paper) !== route.authority.paper_sha256) errors.push('paper slice');
const tranche = lineBytes(6348, 6491);
if (tranche.length !== route.tranche.bytes || sha(tranche) !== route.tranche.sha256) errors.push('tranche slice');
for (const gap of route.tranche.excluded_blank_lines) if (lines[gap - 1] !== '') errors.push(`nonblank gap ${gap}`);
const tranche2 = lineBytes(6492, 6523);
if (tranche2.length !== route.tranche2.bytes || sha(tranche2) !== route.tranche2.sha256) errors.push('tranche2 slice');
for (const gap of route.tranche2.excluded_blank_lines) if (lines[gap - 1] !== '') errors.push(`nonblank gap ${gap}`);
const tranche3 = lineBytes(6524, 6599);
if (tranche3.length !== route.tranche3.bytes || sha(tranche3) !== route.tranche3.sha256) errors.push('tranche3 slice');
for (const gap of route.tranche3.excluded_blank_lines) if (lines[gap - 1] !== '') errors.push(`nonblank gap ${gap}`);
const tranche4 = lineBytes(6600, 6725);
if (tranche4.length !== route.tranche4.bytes || sha(tranche4) !== route.tranche4.sha256) errors.push('tranche4 slice');
for (const gap of route.tranche4.excluded_blank_lines) if (lines[gap - 1] !== '') errors.push(`nonblank gap ${gap}`);
const tranche5 = lineBytes(6726, 6913);
if (tranche5.length !== route.tranche5.bytes || sha(tranche5) !== route.tranche5.sha256) errors.push('tranche5 slice');
for (const gap of route.tranche5.excluded_blank_lines) if (lines[gap - 1] !== '') errors.push(`nonblank gap ${gap}`);
const tranche6 = lineBytes(6914, 7022);
if (tranche6.length !== route.tranche6.bytes || sha(tranche6) !== route.tranche6.sha256) errors.push('tranche6 slice');
for (const gap of route.tranche6.excluded_blank_lines) if (lines[gap - 1] !== '') errors.push(`nonblank gap ${gap}`);

for (const unit of allUnits) {
  const entry = manifest.targets.find(target => target.path === `targets/${unit.id}.tex`);
  if (!entry) { errors.push(`manifest missing ${unit.id}`); continue; }
  const data = await readFile(new URL(entry.path, root));
  const text = data.toString('utf8');
  if (data.length !== entry.bytes || sha(data) !== entry.sha256) errors.push(`target identity ${unit.id}`);
  if (data.includes(0x0D) || data.includes(0x1B) || !text.endsWith('\n') || (data[0] === 0xEF && data[1] === 0xBB && data[2] === 0xBF)) errors.push(`target controls ${unit.id}`);
  const source = lineBytes(unit.lines[0], unit.lines[1]);
  if (source.length !== unit.bytes || sha(source) !== unit.sha256) errors.push(`unit source ${unit.id}`);
  const begins = [...text.matchAll(/\\begin\{([^}]+)\}/g)].map(match => match[1]);
  const ends = [...text.matchAll(/\\end\{([^}]+)\}/g)].map(match => match[1]);
  if (JSON.stringify(begins) !== JSON.stringify(ends)) errors.push(`environment sequence ${unit.id}`);
  targetMap.set(entry.path, { data, text, entry });
}

const sortedTargets = [...targetMap.values()].sort((a, b) => Buffer.compare(Buffer.from(a.entry.path), Buffer.from(b.entry.path)));
const tree = Buffer.from(sortedTargets.map(({ entry }) => `${entry.path}\t${entry.bytes}\t${entry.sha256}\n`).join(''), 'utf8');
if (manifest.target_count !== 55 || manifest.target_bytes !== sortedTargets.reduce((sum, item) => sum + item.data.length, 0) || manifest.target_tree_stream_bytes !== tree.length || manifest.target_tree_sha256 !== sha(tree)) errors.push('target aggregate');

const jsonl = async name => {
  const text = await readFile(new URL(name, import.meta.url), 'utf8');
  if (text.length > 0 && !text.endsWith('\n')) errors.push(`${name} terminal LF`);
  return text.trim() ? text.trimEnd().split('\n').map((line, index) => {
    try { return JSON.parse(line); } catch { errors.push(`${name} JSON ${index + 1}`); return null; }
  }).filter(Boolean) : [];
};
const structure = await jsonl('structure.jsonl');
const difficulty = await jsonl('diff.jsonl');
const visual = await jsonl('visual.jsonl');
const structureIds = new Set(structure.map(record => record.id));
if (structure.length !== 229 || structure.at(-1)?.id !== 'CJK-KO-P09-STR-0229') errors.push('structure count/head');
for (const [index, record] of structure.entries()) {
  if (record.id !== `CJK-KO-P09-STR-${String(index + 1).padStart(4, '0')}`) errors.push(`structure sequence ${record.id}`);
  if (record.parent_id && !structureIds.has(record.parent_id)) errors.push(`structure parent ${record.id}`);
  for (const relation of record.relations) if (!structureIds.has(relation.target_id)) errors.push(`structure relation ${record.id}`);
  if (record.authority) {
    const data = lineBytes(record.authority.line_start, record.authority.line_end);
    if (data.length !== record.authority.bytes || sha(data) !== record.authority.sha256) errors.push(`structure source ${record.id}`);
  }
  if (record.target) {
    const target = targetMap.get(record.target.path);
    if (!target) { errors.push(`structure target path ${record.id}`); continue; }
    const targetLines = target.text.split('\n');
    const data = Buffer.from(`${targetLines.slice(record.target.line_start - 1, record.target.line_end).join('\n')}\n`, 'utf8');
    if (data.length !== record.target.bytes || sha(data) !== record.target.sha256) errors.push(`structure target ${record.id}`);
  }
}
for (const unit of allUnits) {
  const matches = structure.filter(record => record.type === 'unit' && record.target?.path === `targets/${unit.id}.tex`);
  if (matches.length !== 1) errors.push(`unit structure ${unit.id}`);
}
if (difficulty.length !== 34 || difficulty.at(-1)?.id !== 'CJK-KO-P09-HARD-034') errors.push('difficulty count/head');
for (const [index, record] of difficulty.entries()) {
  if (record.id !== `CJK-KO-P09-HARD-${String(index + 1).padStart(3, '0')}`) errors.push(`difficulty sequence ${record.id}`);
  for (const id of record.related_structural_ids) if (!structureIds.has(id)) errors.push(`difficulty relation ${record.id}`);
}
if (visual.length !== 0) errors.push('visual not zero');
const visualStatus = JSON.parse(await readFile(new URL('visual_status.json', import.meta.url), 'utf8'));
if (visualStatus.records !== 0 || visualStatus.files !== 0 || visualStatus.bytes !== 0 || visualStatus.render_calls !== 0 || visualStatus.next_authority_line !== 7023) errors.push('visual status');
for (const name of ['struct.schema.json','diff.schema.json','visual.schema.json']) {
  try { JSON.parse(await readFile(new URL(name, import.meta.url), 'utf8')); } catch { errors.push(`${name} parse`); }
}
for (const artifact of manifest.evidence) {
  const data = await readFile(new URL(artifact.path, root));
  if (data.length !== artifact.bytes || sha(data) !== artifact.sha256) errors.push(`manifest evidence ${artifact.path}`);
}

const report = {
  result: errors.length ? 'FAIL' : 'PASS', errors,
  scope: 'Korean Noether P09 T01-U01 through T06-U55',
  authority: { lines: [6348, 7022], bytes: manifest.scope.bytes, sha256: manifest.scope.sha256 },
  target_files: manifest.target_count, target_bytes: manifest.target_bytes, target_tree_stream_bytes: tree.length, target_tree_sha256: sha(tree),
  structure_records: structure.length, latest_structural_id: structure.at(-1)?.id,
  difficulty_records: difficulty.length, latest_difficulty_id: difficulty.at(-1)?.id,
  visual_records: visual.length,
  target_controls: { bom: 0, cr: 0, esc: 0, missing_terminal_lf: 0 },
  next_authority_line: 7023,
};
await writeFile(new URL('validate.json', import.meta.url), `${JSON.stringify(report, null, 2)}\n`, 'utf8');
process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
if (errors.length) process.exitCode = 1;
