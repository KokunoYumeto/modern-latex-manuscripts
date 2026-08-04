import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const evidenceRoot = path.dirname(fileURLToPath(import.meta.url));
const producerRoot = path.dirname(evidenceRoot);
const workspaceRoot = path.resolve(producerRoot, "../../../../..");
const authorityPath = path.join(workspaceRoot, "03_projects", "noether", "07_german_canon_control", "candidates", "NOETH-DE-ED-0001", "Noether_German_NOETH-DE-ED-0001.tex");
const structuralDir = path.join(evidenceRoot, "structural_index");
const difficultyDir = path.join(evidenceRoot, "difficulty_ledger");
const visualDir = path.join(evidenceRoot, "visual_evidence");
const freezeDir = path.join(evidenceRoot, "prefix_freezes");
const protectedManifestPath = path.join(evidenceRoot, "protected_inputs", "P06_T01_T03_PROTECTED_INPUT_MANIFEST.tsv");
const structuralJsonl = path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX.jsonl");
const structuralCsv = path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX.csv");
const difficultyJsonl = path.join(difficultyDir, "DIFFICULTY_LEDGER.jsonl");
const difficultyCsv = path.join(difficultyDir, "DIFFICULTY_LEDGER.csv");
const visualJsonl = path.join(visualDir, "VISUAL_EVIDENCE_INDEX.jsonl");
const visualCsv = path.join(visualDir, "VISUAL_EVIDENCE_INDEX.csv");

const sha = b => crypto.createHash("sha256").update(b).digest("hex").toUpperCase();
const read = p => fs.readFileSync(p);
const text = p => read(p).toString("utf8");
const identity = p => ({ bytes: read(p).length, sha256: sha(read(p)) });
const assert = (ok, message) => { if (!ok) throw new Error(message); };
const parseJsonl = p => {
  const s = text(p);
  if (s.length === 0) return [];
  return s.split(/\r?\n/).filter(Boolean).map((line, i) => {
    try { return JSON.parse(line); }
    catch (e) { throw new Error(path.basename(p) + " line " + (i + 1) + ": " + e.message); }
  });
};
const parseCsv = s => {
  const rows = [];
  let row = [], field = "", quoted = false;
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (quoted) {
      if (c === '"' && s[i + 1] === '"') { field += '"'; i++; }
      else if (c === '"') quoted = false;
      else field += c;
    } else {
      if (c === '"') quoted = true;
      else if (c === ",") { row.push(field); field = ""; }
      else if (c === "\n") { row.push(field.replace(/\r$/, "")); rows.push(row); row = []; field = ""; }
      else field += c;
    }
  }
  if (field.length || row.length) { row.push(field); rows.push(row); }
  return rows;
};
const normalizeLf = b => b.toString("utf8").replace(/\r\n/g, "\n").replace(/\r/g, "\n");
const sourceLines = normalizeLf(read(authorityPath)).split("\n");
const sourceSlice = (start, end) => Buffer.from(sourceLines.slice(start - 1, end).join("\n") + "\n", "utf8");
const prefixIdentity = (p, bytes) => ({ bytes, sha256: sha(read(p).subarray(0, bytes)) });

const expectedT01Prefix = {
  structural_jsonl: { bytes: 70119, sha256: "43C36F91081F8EDAE7B00E7426B570B4D6A6667937BEA0CC005923893155E61A" },
  structural_csv: { bytes: 24595, sha256: "1A05372CDF95EB9236349A658F4BD98930755BCAF42FBA201C22FB7BDA0600C9" },
  difficulty_jsonl: { bytes: 28167, sha256: "430B121D56A078ABA7B9CC09E2B7C494092359DC13F4E526AA700A0A38AD8662" },
  difficulty_csv: { bytes: 10462, sha256: "4384B3D67405702A645C31CD4FD65F8004C6E572388AD6BD9FB687864810D00E" }
};
const currentEvidenceIdentity = () => ({
  structural_jsonl: identity(structuralJsonl),
  structural_csv: identity(structuralCsv),
  difficulty_jsonl: identity(difficultyJsonl),
  difficulty_csv: identity(difficultyCsv)
});

assert(read(authorityPath).length === 2153565, "authority byte mismatch");
assert(sha(read(authorityPath)) === "D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB", "authority hash mismatch");
const sourceSpans = [
  [4576, 4615, 6610, "AAC3A731B874B46063BB680B3488ED71B1D7A270406E15432E17F47CBA65E8AE"],
  [4616, 4691, 5200, "75061A82BA7BCD9F16A84561B187EA58B2E7143D943A1A57E06FB0230817A8AE"],
  [4692, 4798, 5856, "27A1D4E81287A3F2D4C4276CB3A1909611EDE4B1BB5A47F52F9F86E6DB27B681"],
  [4794, 4797, 160, "29C47D6D86AF55DE39FABE69F5E37CAC69FE0EFDD57A52CC3CF6FA9113682AC3"],
  [4798, 4798, 1, "01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B"]
];
for (const [start, end, bytes, digest] of sourceSpans) {
  const b = sourceSlice(start, end);
  assert(b.length === bytes && sha(b) === digest, "source span mismatch " + start + "-" + end);
}

const pointerFiles = [
  ["NOETH_DE_AUTHORITY_POINTER_v006_20260804.json", 20666, "DB99DD87100654674D7ED24B4ABBBBC3A9920CCF035740D276CE8A87A5313C18"],
  ["NOETH_DE_AUTHORITY_POINTER_v007_20260804.json", 21580, "A6A8FC8E5AC24ACAF49DFD55B4B58FA3DA882EF8C3FDD4D136220C8751045156"]
];
for (const [name, bytes, digest] of pointerFiles) {
  const p = path.join(workspaceRoot, "03_projects", "noether", "07_german_canon_control", "pointers", name);
  assert(read(p).length === bytes && sha(read(p)) === digest, "pointer mismatch " + name);
}

assert(fs.existsSync(protectedManifestPath), "protected input manifest missing");
const manifestLines = text(protectedManifestPath).trimEnd().split("\n");
assert(manifestLines[0] === "relative_path\tbytes\tsha256", "protected manifest header");
assert(manifestLines.length === 38, "protected manifest must contain 37 files");
let protectedBytes = 0;
for (const line of manifestLines.slice(1)) {
  const parts = line.replace(/\r$/, "").split("\t");
  assert(parts.length === 3, "bad protected manifest row");
  const [rel, bytesText, digest] = parts;
  assert(!rel.includes("T04") && !rel.includes("_U23_"), "T04 absorbed into protected scope");
  const p = path.join(producerRoot, ...rel.split("/"));
  const b = read(p);
  assert(b.length === Number(bytesText), "protected bytes mismatch " + rel);
  assert(sha(b) === digest, "protected hash mismatch " + rel);
  protectedBytes += b.length;
}
const targetManifestRows = manifestLines.slice(1).filter(line => line.split("\t")[0].startsWith("targets/"));
assert(targetManifestRows.length === 22, "protected target count");
const targetBytes = targetManifestRows.reduce((sum, line) => sum + Number(line.split("\t")[1]), 0);
assert(targetBytes === 41488, "protected target byte total");

const t02FreezePath = path.join(freezeDir, "P06_T02_EVIDENCE_PREFIX_FREEZE_20260804.json");
const t03FreezePath = path.join(freezeDir, "P06_T03_EVIDENCE_PREFIX_FREEZE_20260804.json");
const t02Freeze = JSON.parse(text(t02FreezePath));
const t03Freeze = JSON.parse(text(t03FreezePath));
assert(JSON.stringify(t02Freeze.prefix_before) === JSON.stringify(expectedT01Prefix), "T01 prefix freeze mismatch");
assert(JSON.stringify(t03Freeze.prefix_before) === JSON.stringify(t02Freeze.prefix_through_scope), "T02 prefix handoff mismatch");
assert(JSON.stringify(currentEvidenceIdentity()) === JSON.stringify(t03Freeze.prefix_through_scope), "current evidence differs from T03 freeze");
for (const [key, p] of Object.entries({ structural_jsonl: structuralJsonl, structural_csv: structuralCsv, difficulty_jsonl: difficultyJsonl, difficulty_csv: difficultyCsv })) {
  assert(JSON.stringify(prefixIdentity(p, expectedT01Prefix[key].bytes)) === JSON.stringify(expectedT01Prefix[key]), "T01 prefix bytes changed in " + key);
  assert(JSON.stringify(prefixIdentity(p, t02Freeze.prefix_through_scope[key].bytes)) === JSON.stringify(t02Freeze.prefix_through_scope[key]), "T02 prefix bytes changed in " + key);
}
assert(t03Freeze.boundary_control.terminal_unit === "T03-U22", "terminal unit freeze");
assert(t03Freeze.boundary_control.source_lines === "4794-4797", "terminal source lines");
assert(t03Freeze.boundary_control.excluded_blank_line === 4798, "blank 4798 control");
assert(t03Freeze.boundary_control.t04_absorbed === false, "T04 scope flag");

const structural = parseJsonl(structuralJsonl);
const structuralRows = parseCsv(text(structuralCsv));
assert(structuralRows[0][0] === "structural_id", "structural CSV header");
assert(structuralRows.length === structural.length + 1, "structural CSV cardinality");
const structuralIds = new Set(structural.map(r => r.structural_id));
assert(structuralIds.size === structural.length, "duplicate structural IDs");
for (let i = 0; i < structural.length; i++) {
  const r = structural[i];
  assert(r.global_order === i + 1, "noncontiguous structural order " + r.structural_id);
  assert(["T01", "T02", "T03"].includes(r.tranche_id), "out-of-scope tranche " + r.structural_id);
  assert(!r.structural_id.includes("-T04-"), "T04 structural ID");
  assert(r.source_locator.whole_line_start >= 4576 && r.source_locator.whole_line_end <= 4798, "source locator outside scope " + r.structural_id);
  if (r.unit_id !== null) {
    const n = Number(r.unit_id.slice(1));
    assert(n >= 1 && n <= 22, "unit outside U01--U22 " + r.structural_id);
  }
  if (r.parent_id !== null) assert(structuralIds.has(r.parent_id), "missing parent " + r.structural_id);
  for (const rel of r.relations) if (rel.scope === "internal") assert(structuralIds.has(rel.target_id), "missing internal relation " + r.structural_id + " -> " + rel.target_id);
  assert(r.review_state === "unchecked", "non-unchecked structural record");
  assert(r.completion_state === "producer_draft_coverage", "bad completion state");
  assert(/^[A-F0-9]{64}$/.test(r.source_sha256) && /^[A-F0-9]{64}$/.test(r.target_sha256), "bad structural hash");
}
assert(!text(structuralJsonl).includes("Noether_P06_Korean_T04_"), "T04 target path in structural JSONL");
assert(!text(structuralCsv).includes("Noether_P06_Korean_T04_"), "T04 target path in structural CSV");
const u22 = structural.find(r => r.structural_id === "NOE-P06-KO-T03-U22");
assert(u22.source_locator.whole_line_start === 4794 && u22.source_locator.whole_line_end === 4797, "U22 locator");
const openNote = structural.find(r => r.structural_id === "NOE-P06-KO-T03-U21-FOOTNOTE-OPEN-001");
const closeNote = structural.find(r => r.structural_id === "NOE-P06-KO-T03-U22-FOOTNOTE-CLOSE-001");
assert(openNote.relations.some(r => r.target_id === closeNote.structural_id && r.type === "continued_by"), "missing U21 to U22 footnote relation");
assert(closeNote.relations.some(r => r.target_id === openNote.structural_id && r.type === "continues"), "missing U22 to U21 footnote relation");
assert(closeNote.source_locator.whole_line_end === 4797, "split footnote must exclude blank 4798");

const difficulty = parseJsonl(difficultyJsonl);
const difficultyRows = parseCsv(text(difficultyCsv));
assert(difficultyRows[0][0] === "record_id", "difficulty CSV header");
assert(difficultyRows.length === difficulty.length + 1, "difficulty CSV cardinality");
const difficultyIds = new Set(difficulty.map(r => r.record_id));
assert(difficultyIds.size === difficulty.length, "duplicate difficulty IDs");
for (let i = 0; i < difficulty.length; i++) {
  const r = difficulty[i];
  assert(r.sequence === i + 1, "difficulty sequence mismatch");
  assert(r.previous_record_id === (i === 0 ? null : difficulty[i - 1].record_id), "difficulty predecessor mismatch " + r.record_id);
  assert(!r.tranche_ids.some(x => String(x).startsWith("T04")), "T04 difficulty scope");
  for (const id of r.related_structural_ids) assert(structuralIds.has(id), "missing difficulty structural link " + r.record_id + " -> " + id);
}
assert(difficulty.length === 25, "difficulty count");
assert(difficulty.at(-1).record_id === "CJK-KO-P06-HARD-025", "latest difficulty ID");
const regexFailure = difficulty.find(r => r.record_id === "CJK-KO-P06-HARD-017");
assert(regexFailure.state === "resolved" && regexFailure.symptom.includes("Unexpected non-whitespace character after JSON"), "T02 verifier regex failure missing");
assert(regexFailure.attempted_approaches.some(x => x.outcome.includes("102 structural records") && x.outcome.includes("writes 0")), "T02 verifier corrected retry evidence missing");
const parserFailure = difficulty.find(r => r.record_id === "CJK-KO-P06-HARD-018");
assert(parserFailure.state === "resolved" && parserFailure.classification === "computation", "T03 parser failure state");
assert(parserFailure.symptom.includes("Exact command text and exact error text are unavailable"), "limited evidence statement missing");
assert(parserFailure.cause_evidence.includes("No more specific token sequence is asserted"), "non-invention control missing");
assert(parserFailure.attempted_approaches.some(x => x.outcome.includes("writes 0")), "write-zero evidence missing");
assert(parserFailure.attempted_approaches.some(x => x.outcome.includes("Passed; writes 0")), "corrected verification evidence missing");

assert(read(visualJsonl).length === 0, "visual JSONL must remain zero bytes");
const visualRows = parseCsv(text(visualCsv));
assert(visualRows.length === 1 && visualRows[0][0] === "visual_id", "visual CSV must remain header only");
const images = [];
const walk = dir => {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p);
    else if (/\.(png|jpe?g|gif|tiff?|webp|bmp)$/i.test(e.name)) images.push(p);
  }
};
walk(producerRoot);
assert(images.length === 0, "unexpected image evidence file");

const selfSha = sha(read(fileURLToPath(import.meta.url)));
const structuralReport = JSON.parse(text(path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json")));
const difficultyReport = JSON.parse(text(path.join(difficultyDir, "DIFFICULTY_LEDGER_VALIDATION_REPORT.json")));
const visualReport = JSON.parse(text(path.join(visualDir, "VISUAL_EVIDENCE_INDEX_VALIDATION_REPORT.json")));
assert(structuralReport.status === "PASS" && structuralReport.record_count === structural.length && structuralReport.validator_sha256 === selfSha, "structural report mismatch");
assert(difficultyReport.status === "PASS" && difficultyReport.record_count === difficulty.length && difficultyReport.validator_sha256 === selfSha, "difficulty report mismatch");
assert(visualReport.status === "PASS" && visualReport.record_count === 0 && visualReport.validator_sha256 === selfSha, "visual report mismatch");

const typeCounts = {};
for (const r of structural) typeCounts[r.record_type] = (typeCounts[r.record_type] ?? 0) + 1;
const stateCounts = {};
for (const r of difficulty) stateCounts[r.state] = (stateCounts[r.state] ?? 0) + 1;
const result = {
  status: "PASS",
  scope: "P06 T01--T03 U01--U22 producer metadata integrity only",
  structural: {
    records: structural.length,
    unique_ids: structuralIds.size,
    latest_structural_id: structural.at(-1).structural_id,
    type_counts: typeCounts,
    jsonl: identity(structuralJsonl),
    csv: identity(structuralCsv)
  },
  difficulty: {
    records: difficulty.length,
    unique_ids: difficultyIds.size,
    latest_record_id: difficulty.at(-1).record_id,
    state_counts: stateCounts,
    jsonl: identity(difficultyJsonl),
    csv: identity(difficultyCsv)
  },
  visual: {
    records: 0,
    image_files: 0,
    render_calls: 0,
    jsonl: identity(visualJsonl),
    csv: identity(visualCsv)
  },
  protected_inputs: {
    files: 37,
    bytes: protectedBytes,
    targets: 22,
    target_bytes: targetBytes,
    manifest: identity(protectedManifestPath),
    mutations: 0
  },
  prefix_integrity: {
    t01: expectedT01Prefix,
    t02: t02Freeze.prefix_through_scope,
    t03: t03Freeze.prefix_through_scope
  },
  boundary: {
    u22_source_lines: "4794-4797",
    blank_4798_excluded: true,
    next_cursor: 4799,
    t04_absorbed: false,
    u21_to_u22_srcfn_relation: "PASS"
  },
  pointer_bindings: [
    { id: "NOETH-DE-AUTH-v006-20260804", bytes: 20666, sha256: "DB99DD87100654674D7ED24B4ABBBBC3A9920CCF035740D276CE8A87A5313C18" },
    { id: "NOETH-DE-AUTH-v007-20260804", bytes: 21580, sha256: "A6A8FC8E5AC24ACAF49DFD55B4B58FA3DA882EF8C3FDD4D136220C8751045156" }
  ],
  limits: ["No source or scan adjudication", "No Korean or formula review", "No compilation or rendering", "No assembly packaging certification approval canon archive or SGA work"]
};
process.stdout.write(JSON.stringify(result, null, 2) + "\n");
