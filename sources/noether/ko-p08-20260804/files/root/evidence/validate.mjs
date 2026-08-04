import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const root = path.resolve(import.meta.dirname, '..');
const sourceBase = 5957;

function sha(bytes) {
  return crypto.createHash('sha256').update(bytes).digest('hex').toUpperCase();
}

function linesOf(file) {
  const text = fs.readFileSync(file, 'utf8');
  const lines = text.split('\n');
  if (lines.at(-1) === '') lines.pop();
  return lines;
}

function sliceLines(lines, start, end, base) {
  return Buffer.from(lines.slice(start - base, end - base + 1).join('\n') + '\n', 'utf8');
}

function fileIdentity(file) {
  const bytes = fs.readFileSync(file);
  return {path:path.relative(root, file).replaceAll('\\','/'), bytes:bytes.length, sha256:sha(bytes)};
}

const errors = [];
const sourceLines = linesOf(path.join(root, 'source.tex'));
const structPath = path.join(import.meta.dirname, 'structure.jsonl');
const structLines = fs.readFileSync(structPath, 'utf8').trim().split('\n').filter(Boolean);
const records = structLines.map(function (line, i) {
  try { return JSON.parse(line); } catch (e) { errors.push('structure JSON line ' + String(i + 1)); return null; }
}).filter(Boolean);
const ids = new Set();
for (const r of records) {
  if (ids.has(r.id)) errors.push('duplicate structure id ' + r.id);
  ids.add(r.id);
  const sourceBytes = sliceLines(sourceLines, r.authority.line_start, r.authority.line_end, sourceBase);
  if (sourceBytes.length !== r.authority.bytes || sha(sourceBytes) !== r.authority.sha256) errors.push('authority mismatch ' + r.id);
  if (r.target) {
    const targetLines = linesOf(path.join(root, r.target.path));
    const targetBytes = sliceLines(targetLines, r.target.line_start, r.target.line_end, 1);
    if (targetBytes.length !== r.target.bytes || sha(targetBytes) !== r.target.sha256) errors.push('target mismatch ' + r.id);
  }
  const copy = JSON.parse(JSON.stringify(r));
  delete copy.evidence_sha256;
  if (sha(Buffer.from(JSON.stringify(copy), 'utf8')) !== r.evidence_sha256) errors.push('evidence hash mismatch ' + r.id);
}
for (const r of records) {
  if (r.parent_id && !ids.has(r.parent_id)) errors.push('missing parent ' + r.id);
  for (const rel of r.relations) if (!ids.has(rel.target_id)) errors.push('missing relation target ' + r.id);
}

const diffPath = path.join(import.meta.dirname, 'diff.jsonl');
const diffLines = fs.readFileSync(diffPath, 'utf8').trim().split('\n').filter(Boolean);
const diffIds = new Set();
for (let i = 0; i < diffLines.length; i++) {
  let r;
  try { r = JSON.parse(diffLines[i]); } catch (e) { errors.push('difficulty JSON line ' + String(i + 1)); continue; }
  if (diffIds.has(r.id)) errors.push('duplicate difficulty id ' + r.id);
  diffIds.add(r.id);
  for (const sid of r.structural_ids) if (!ids.has(sid)) errors.push('difficulty missing structural id ' + r.id + ' ' + sid);
}

const visualPath = path.join(import.meta.dirname, 'visual.jsonl');
const visualText = fs.readFileSync(visualPath, 'utf8');
const visualLines = visualText.trim() ? visualText.trim().split('\n') : [];
for (let i = 0; i < visualLines.length; i++) {
  try { JSON.parse(visualLines[i]); } catch (e) { errors.push('visual JSON line ' + String(i + 1)); }
}

const targetFiles = fs.readdirSync(path.join(root, 'targets')).filter(function (n) { return n.endsWith('.tex'); }).sort();
const indexedTargets = new Set(records.filter(function (r) { return r.type === 'unit' && r.target; }).map(function (r) { return path.basename(r.target.path); }));
for (const name of targetFiles) if (!indexedTargets.has(name)) errors.push('target missing unit index ' + name);
const controls = {bom:0, cr:0, esc:0, missing_terminal_lf:0};
for (const name of targetFiles) {
  const bytes = fs.readFileSync(path.join(root, 'targets', name));
  if (bytes.length >= 3 && bytes[0] === 239 && bytes[1] === 187 && bytes[2] === 191) controls.bom++;
  if (bytes.includes(13)) controls.cr++;
  if (bytes.includes(27)) controls.esc++;
  if (!bytes.length || bytes.at(-1) !== 10) controls.missing_terminal_lf++;
}
if (Object.values(controls).some(function (n) { return n !== 0; })) errors.push('target encoding controls');

const targetIdentities = targetFiles.map(function (name) {
  const bytes = fs.readFileSync(path.join(root, 'targets', name));
  return {path:'targets/' + name, bytes:bytes.length, sha256:sha(bytes)};
});
const treeStream = targetIdentities.map(function (item) {
  return item.path + '\0' + String(item.bytes) + '\0' + item.sha256 + '\n';
}).join('');
const manifestPath = path.join(root, 'manifest.json');
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
if (manifest.target_count !== targetIdentities.length) errors.push('manifest target count');
if (manifest.target_bytes !== targetIdentities.reduce(function (sum, item) { return sum + item.bytes; }, 0)) errors.push('manifest target bytes');
if (manifest.target_tree_sha256 !== sha(Buffer.from(treeStream, 'utf8'))) errors.push('manifest target tree');
if (manifest.source_gap_lines.some(function (line) { return sourceLines[line - sourceBase] !== ''; })) errors.push('manifest nonblank source gap');

const report = {
  result: errors.length ? 'FAIL' : 'PASS',
  errors: errors,
  scope: 'complete P08 T01-U01 through T08-U36',
  structure_records: records.length,
  difficulty_records: diffLines.length,
  visual_records: visualLines.length,
  target_files: targetFiles.length,
  target_bytes: targetIdentities.reduce(function (sum, item) { return sum + item.bytes; }, 0),
  target_tree_stream_bytes: Buffer.byteLength(treeStream, 'utf8'),
  target_tree_sha256: sha(Buffer.from(treeStream, 'utf8')),
  target_controls: controls,
  next_authority_line: 6348,
  artifacts: [
    fileIdentity(structPath),
    fileIdentity(path.join(import.meta.dirname, 'structure.csv')),
    fileIdentity(path.join(import.meta.dirname, 'struct.schema.json')),
    fileIdentity(diffPath),
    fileIdentity(path.join(import.meta.dirname, 'diff.schema.json')),
    fileIdentity(visualPath),
    fileIdentity(path.join(import.meta.dirname, 'visual.csv')),
    fileIdentity(path.join(import.meta.dirname, 'visual.schema.json')),
    fileIdentity(path.join(import.meta.dirname, 'visual_status.json')),
    fileIdentity(manifestPath)
  ]
};
fs.writeFileSync(path.join(import.meta.dirname, 'validate.json'), JSON.stringify(report, null, 2) + '\n', 'utf8');
if (errors.length) {
  console.error(JSON.stringify(report, null, 2));
  process.exit(1);
}
console.log(JSON.stringify(report, null, 2));
