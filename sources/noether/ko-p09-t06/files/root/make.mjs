import { readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';

const authority = 'C:/Users/Floris/Documents/interlanguage/03_projects/noether/07_german_canon_control/candidates/ED0002/noether.tex';
const raw = await readFile(authority);
const rawSha = createHash('sha256').update(raw).digest('hex').toUpperCase();
if (raw.length !== 2153554 || rawSha !== 'C9A125167ACB33D914EE4374B65AE7CDF0052F568371B8B77B720EA178ABF0E3') {
  throw new Error(`authority mismatch: ${raw.length} ${rawSha}`);
}

const lf = raw.toString('utf8').replaceAll('\r\n', '\n');
const lines = lf.split('\n');
const lineStart = 6348;
const lineEnd = 7679;
const slice = `${lines.slice(lineStart - 1, lineEnd).join('\n')}\n`;
const bytes = Buffer.from(slice, 'utf8');
const sha256 = createHash('sha256').update(bytes).digest('hex').toUpperCase();

await writeFile(new URL('./source.tex', import.meta.url), bytes);

const units = [
  ['T01_U01', 6348, 6355],
  ['T01_U02', 6357, 6368],
  ['T01_U03', 6370, 6383],
  ['T01_U04', 6385, 6404],
  ['T01_U05', 6406, 6414],
  ['T01_U06', 6416, 6429],
  ['T01_U07', 6431, 6446],
  ['T01_U08', 6448, 6452],
  ['T01_U09', 6454, 6475],
  ['T01_U10', 6477, 6483],
  ['T01_U11', 6485, 6490],
].map(([id, start, end]) => {
  const text = `${lines.slice(start - 1, end).join('\n')}\n`;
  const data = Buffer.from(text, 'utf8');
  return {
    id,
    lines: [start, end],
    bytes: data.length,
    sha256: createHash('sha256').update(data).digest('hex').toUpperCase(),
  };
});

const units2 = [
  ['T02_U12', 6492, 6493],
  ['T02_U13', 6495, 6511],
  ['T02_U14', 6513, 6522],
].map(([id, start, end]) => {
  const text = `${lines.slice(start - 1, end).join('\n')}\n`;
  const data = Buffer.from(text, 'utf8');
  return {
    id,
    lines: [start, end],
    bytes: data.length,
    sha256: createHash('sha256').update(data).digest('hex').toUpperCase(),
  };
});

const units3 = [
  ['T03_U15', 6524, 6524],
  ['T03_U16', 6526, 6529],
  ['T03_U17', 6531, 6546],
  ['T03_U18', 6548, 6552],
  ['T03_U19', 6554, 6571],
  ['T03_U20', 6573, 6594],
  ['T03_U21', 6596, 6598],
].map(([id, start, end]) => {
  const text = `${lines.slice(start - 1, end).join('\n')}\n`;
  const data = Buffer.from(text, 'utf8');
  return { id, lines: [start, end], bytes: data.length, sha256: createHash('sha256').update(data).digest('hex').toUpperCase() };
});

const units4 = [
  ['T04_U22', 6600, 6600],
  ['T04_U23', 6602, 6611],
  ['T04_U24', 6613, 6623],
  ['T04_U25', 6625, 6648],
  ['T04_U26', 6650, 6659],
  ['T04_U27', 6661, 6684],
  ['T04_U28', 6685, 6710],
  ['T04_U29', 6712, 6724],
].map(([id, start, end]) => {
  const text = `${lines.slice(start - 1, end).join('\n')}\n`;
  const data = Buffer.from(text, 'utf8');
  return { id, lines: [start, end], bytes: data.length, sha256: createHash('sha256').update(data).digest('hex').toUpperCase() };
});

const units5 = [
  ['T05_U30', 6726, 6727],
  ['T05_U31', 6729, 6735],
  ['T05_U32', 6737, 6742],
  ['T05_U33', 6744, 6750],
  ['T05_U34', 6752, 6757],
  ['T05_U35', 6759, 6762],
  ['T05_U36', 6764, 6771],
  ['T05_U37', 6773, 6785],
  ['T05_U38', 6787, 6802],
  ['T05_U39', 6804, 6834],
  ['T05_U40', 6836, 6844],
  ['T05_U41', 6846, 6848],
  ['T05_U42', 6850, 6868],
  ['T05_U43', 6870, 6884],
  ['T05_U44', 6886, 6890],
  ['T05_U45', 6891, 6909],
].map(([id, start, end]) => {
  const text = `${lines.slice(start - 1, end).join('\n')}\n`;
  const data = Buffer.from(text, 'utf8');
  return { id, lines: [start, end], bytes: data.length, sha256: createHash('sha256').update(data).digest('hex').toUpperCase() };
});

const units6 = [
  ['T06_U46', 6914, 6914],
  ['T06_U47', 6916, 6921],
  ['T06_U48', 6923, 6929],
  ['T06_U49', 6931, 6941],
  ['T06_U50', 6943, 6945],
  ['T06_U51', 6946, 6970],
  ['T06_U52', 6971, 6991],
  ['T06_U53', 6993, 6995],
  ['T06_U54', 6997, 7000],
  ['T06_U55', 7002, 7021],
].map(([id, start, end]) => {
  const text = `${lines.slice(start - 1, end).join('\n')}\n`;
  const data = Buffer.from(text, 'utf8');
  return { id, lines: [start, end], bytes: data.length, sha256: createHash('sha256').update(data).digest('hex').toUpperCase() };
});

const trancheText = `${lines.slice(6348 - 1, 6491).join('\n')}\n`;
const trancheData = Buffer.from(trancheText, 'utf8');
const tranche2Text = `${lines.slice(6492 - 1, 6523).join('\n')}\n`;
const tranche2Data = Buffer.from(tranche2Text, 'utf8');
const tranche3Text = `${lines.slice(6524 - 1, 6599).join('\n')}\n`;
const tranche3Data = Buffer.from(tranche3Text, 'utf8');
const tranche4Text = `${lines.slice(6600 - 1, 6725).join('\n')}\n`;
const tranche4Data = Buffer.from(tranche4Text, 'utf8');
const tranche5Text = `${lines.slice(6726 - 1, 6913).join('\n')}\n`;
const tranche5Data = Buffer.from(tranche5Text, 'utf8');
const tranche6Text = `${lines.slice(6914 - 1, 7022).join('\n')}\n`;
const tranche6Data = Buffer.from(tranche6Text, 'utf8');
const route = {
  authority: {
    edition: 'NOETH-DE-ED-0002',
    whole_bytes: raw.length,
    whole_sha256: rawSha,
    paper_lines: [lineStart, lineEnd],
    paper_bytes: bytes.length,
    paper_sha256: sha256,
  },
  tranche: {
    id: 'T01',
    lines: [6348, 6491],
    bytes: trancheData.length,
    sha256: createHash('sha256').update(trancheData).digest('hex').toUpperCase(),
    units,
    excluded_blank_lines: [6356, 6369, 6384, 6405, 6415, 6430, 6447, 6453, 6476, 6484, 6491],
    next_line: 6492,
  },
  tranche2: {
    id: 'T02',
    lines: [6492, 6523],
    bytes: tranche2Data.length,
    sha256: createHash('sha256').update(tranche2Data).digest('hex').toUpperCase(),
    units: units2,
    excluded_blank_lines: [6494, 6512, 6523],
    next_line: 6524,
  },
  tranche3: {
    id: 'T03',
    lines: [6524, 6599],
    bytes: tranche3Data.length,
    sha256: createHash('sha256').update(tranche3Data).digest('hex').toUpperCase(),
    units: units3,
    excluded_blank_lines: [6525, 6530, 6547, 6553, 6572, 6595, 6599],
    next_line: 6600,
  },
  tranche4: {
    id: 'T04',
    lines: [6600, 6725],
    bytes: tranche4Data.length,
    sha256: createHash('sha256').update(tranche4Data).digest('hex').toUpperCase(),
    units: units4,
    excluded_blank_lines: [6601, 6612, 6624, 6649, 6660, 6711, 6725],
    next_line: 6726,
  },
  tranche5: {
    id: 'T05',
    lines: [6726, 6913],
    bytes: tranche5Data.length,
    sha256: createHash('sha256').update(tranche5Data).digest('hex').toUpperCase(),
    units: units5,
    excluded_blank_lines: [6728, 6736, 6743, 6751, 6758, 6763, 6772, 6786, 6803, 6835, 6845, 6849, 6869, 6885, 6910, 6911, 6912, 6913],
    next_line: 6914,
  },
  tranche6: {
    id: 'T06',
    lines: [6914, 7022],
    bytes: tranche6Data.length,
    sha256: createHash('sha256').update(tranche6Data).digest('hex').toUpperCase(),
    units: units6,
    excluded_blank_lines: [6915, 6922, 6930, 6942, 6992, 6996, 7001, 7022],
    next_line: 7023,
  },
};
await writeFile(new URL('./route.json', import.meta.url), `${JSON.stringify(route, null, 2)}\n`, 'utf8');
process.stdout.write(`${JSON.stringify(route, null, 2)}\n`);
