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

const trancheText = `${lines.slice(6348 - 1, 6491).join('\n')}\n`;
const trancheData = Buffer.from(trancheText, 'utf8');
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
};
await writeFile(new URL('./route.json', import.meta.url), `${JSON.stringify(route, null, 2)}\n`, 'utf8');
process.stdout.write(`${JSON.stringify(route, null, 2)}\n`);
