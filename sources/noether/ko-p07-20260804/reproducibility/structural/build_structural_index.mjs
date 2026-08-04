import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(scriptDir, "..", "..");
const authorityPath = path.normalize("C:/Users/Floris/Documents/interlanguage/03_projects/noether/07_german_canon_control/candidates/NOETH-DE-ED-0001/Noether_German_NOETH-DE-ED-0001.tex");
const authoritySha = "D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB";
const pointerId = "NOETH-DE-AUTH-v003-20260804";
const pointerSha = "932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197";
const intervalSha = "8C5D6E8DDF24B33C5AF719F59C4CEFA0B9CEABB61960E2AC30F888CB1206AFBC";

const units = {
  U01: { local: [1, 14], sourceSha: "E0A011C29D5634C9ED07D99E0027F3E01513A4DDB58924119BC729D40AAA3705", targetSha: "96327E3C4C558450D56D62F2433EACFD8CD4ACFBBB8F648506BE939B01105507" },
  U02: { local: [16, 26], sourceSha: "046B6E95E7DA1493157055ED0848F4FC0639DD2DE2CF7FFCD43784B8A7251114", targetSha: "813E2586E4FE975C51E21C74F8399CEEEA60139A9FDD833FF2C44888A6649177" },
  U03: { local: [28, 46], sourceSha: "FF490BF1734E6072971A10A71ABF27D4D9F37583C5FE3B022A5E23420638235C", targetSha: "7E12CEC2A1FB8A73AD5D9ADBD025B7B142B575FA064FC5671ED24E3C43F994A5" },
  U04: { local: [48, 63], sourceSha: "BA53F3A4E875320E336B2756713DF8141B9EE28A6232C4ECCAD7096460877A3A", targetSha: "5387865AFD79A4C0B46930896944B0F8AD425715A177274EF51EA160CD2DC377" },
  U05: { local: [64, 89], sourceSha: "E72BA9C64A16088969ED13D342FF6881F7DD0A45A299790958CA60331ABD1B7D", targetSha: "A1B345CAD00CD9FC8BCB8A443A0917FFCDFA9707E006A5417B136822820F24CA" },
  U06: { local: [91, 91], sourceSha: "259F6AF8F5291DF1E69522664C6283722076A4E0FD9E97909707C9033E3C0B04", targetSha: "896E625D41FEE52847CABFE77CE7426ADFE18CB8169EE8CB463D0765B5AA4AB3" },
  U07: { local: [93, 108], sourceSha: "94D233D263CAF89160FD9675AD42A4A095F6BD12F5B3B1E639C08D24C0E161E0", targetSha: "B0AE4C26E0AE0C79111820868B09049AF18A894944CCD46EF098197A9E9BCA9C" },
  U08: { local: [110, 113], sourceSha: "C45D1343EB1A2930C97B1101C8A3AB19F5684CA045951D7C98274A2D94AA699D", targetSha: "DE8AD783FF83DC27A2568D4DD47A42DA55127A912F8FDEC57BF0F50DBDE38971" }
};

function sha(data) {
  return crypto.createHash("sha256").update(data).digest("hex").toUpperCase();
}

function normalizedLines(filePath) {
  return fs.readFileSync(filePath, "utf8").replace(/\r\n/g, "\n").replace(/\r/g, "\n").split("\n");
}

function sliceBytes(lines, start, end) {
  return Buffer.from(lines.slice(start - 1, end).join("\n") + "\n", "utf8");
}

function targetPath(unit) {
  return path.join(root, "targets", "Noether_P07_Korean_" + unit + "_UNCHECKED.tex");
}

function item(id, unit, kind, title, sourceStart, sourceEnd, targetStart, targetEnd, parentId, refs) {
  return {
    structural_id: "NOE-P07-KO-STR-" + String(id).padStart(3, "0"),
    unit_id: unit,
    kind,
    title,
    sourceStart,
    sourceEnd,
    targetStart,
    targetEnd,
    parent_id: parentId,
    cross_references: refs || []
  };
}

const m = [
  item(1, "U01", "section", "Paper 7 main section", 1, 1, 11, 11, null),
  item(2, "U01", "publication_metadata", "Math. Ann. publication line", 3, 3, 13, 13, "NOE-P07-KO-STR-001"),
  item(3, "U01", "title", "Displayed article title", 7, 7, 17, 17, "NOE-P07-KO-STR-001"),
  item(4, "U01", "byline", "Author and Erlangen affiliation", 9, 11, 19, 21, "NOE-P07-KO-STR-001"),
  item(5, "U01", "prose", "Purpose and contrast with Hilbert proof", 14, 14, 24, 24, "NOE-P07-KO-STR-001"),
  item(6, "U01", "note", "Weber reference note", 14, 14, 24, 24, "NOE-P07-KO-STR-005"),
  item(7, "U01", "bibliography_item", "Weber Lehrbuch der Algebra citation", 14, 14, 24, 24, "NOE-P07-KO-STR-006"),
  item(8, "U02", "prose", "Finite group action and invariant definition setup", 16, 21, 11, 16, "NOE-P07-KO-STR-001", ["NOE-P07-KO-STR-009", "NOE-P07-KO-STR-010", "NOE-P07-KO-STR-011"]),
  item(9, "U02", "display", "Linear transformation display", 17, 20, 12, 15, "NOE-P07-KO-STR-008"),
  item(10, "U02", "definition", "Polynomial absolute invariant definition", 21, 21, 16, 16, "NOE-P07-KO-STR-008"),
  item(11, "U02", "display", "Invariant averaging equation (1)", 22, 26, 17, 21, "NOE-P07-KO-STR-008"),
  item(12, "U03", "section", "Subsection 1", 28, 28, 11, 11, "NOE-P07-KO-STR-001"),
  item(13, "U03", "prose", "Multisymmetric single-row case", 29, 29, 12, 12, "NOE-P07-KO-STR-012", ["NOE-P07-KO-STR-011", "NOE-P07-KO-STR-014", "NOE-P07-KO-STR-015"]),
  item(14, "U03", "note", "Cross-reference to subsection 2 note", 29, 29, 12, 12, "NOE-P07-KO-STR-013", ["NOE-P07-KO-STR-021"]),
  item(15, "U03", "display", "Galois resolvent product and coefficient conditions", 30, 43, 13, 26, "NOE-P07-KO-STR-013"),
  item(16, "U03", "prose", "Degree of the G coefficients", 44, 44, 27, 27, "NOE-P07-KO-STR-012", ["NOE-P07-KO-STR-015", "NOE-P07-KO-STR-017"]),
  item(17, "U03", "theorem", "First complete invariant system theorem", 46, 46, 29, 29, "NOE-P07-KO-STR-012", ["NOE-P07-KO-STR-015"]),
  item(18, "U04", "section", "Subsection 2", 48, 48, 11, 11, "NOE-P07-KO-STR-001"),
  item(19, "U04", "prose", "Second elementary argument introduction", 49, 49, 12, 12, "NOE-P07-KO-STR-018", ["NOE-P07-KO-STR-011", "NOE-P07-KO-STR-020"]),
  item(20, "U04", "note", "Single-row symmetric-function proof note", 49, 49, 12, 12, "NOE-P07-KO-STR-019", ["NOE-P07-KO-STR-014"]),
  item(21, "U04", "display", "Polynomial expansion of f", 50, 53, 13, 16, "NOE-P07-KO-STR-019"),
  item(22, "U04", "prose", "Constants and invocation of equation (1)", 54, 54, 17, 17, "NOE-P07-KO-STR-018", ["NOE-P07-KO-STR-011", "NOE-P07-KO-STR-023"]),
  item(23, "U04", "display", "Averaged expansion in J invariants", 55, 63, 18, 26, "NOE-P07-KO-STR-022"),
  item(24, "U05", "prose", "Reduction to the special J invariants", 64, 69, 11, 16, "NOE-P07-KO-STR-018", ["NOE-P07-KO-STR-025"]),
  item(25, "U05", "display", "Definition of J invariant", 65, 68, 12, 15, "NOE-P07-KO-STR-024"),
  item(26, "U05", "prose", "J as a coefficient of a power sum", 69, 74, 16, 21, "NOE-P07-KO-STR-018", ["NOE-P07-KO-STR-027"]),
  item(27, "U05", "display", "Definition of S_mu", 70, 73, 17, 20, "NOE-P07-KO-STR-026"),
  item(28, "U05", "prose", "Power sum of h linear forms", 74, 79, 21, 26, "NOE-P07-KO-STR-018", ["NOE-P07-KO-STR-029"]),
  item(29, "U05", "display", "The h linear forms xi", 75, 78, 22, 25, "NOE-P07-KO-STR-028"),
  item(30, "U05", "prose", "Reduction of all power sums to the first h", 79, 83, 26, 30, "NOE-P07-KO-STR-018", ["NOE-P07-KO-STR-031"]),
  item(31, "U05", "display", "First h power sums", 80, 82, 27, 29, "NOE-P07-KO-STR-030"),
  item(32, "U05", "prose", "Coefficient bound and second complete system", 83, 87, 30, 34, "NOE-P07-KO-STR-018", ["NOE-P07-KO-STR-033", "NOE-P07-KO-STR-034"]),
  item(33, "U05", "display", "Bounded-index J invariants", 84, 86, 31, 33, "NOE-P07-KO-STR-032"),
  item(34, "U05", "theorem", "Second complete invariant system theorem", 89, 89, 36, 36, "NOE-P07-KO-STR-018", ["NOE-P07-KO-STR-025", "NOE-P07-KO-STR-033"]),
  item(35, "U06", "remark", "Equivalence of the two systems and degree bound", 91, 91, 11, 11, "NOE-P07-KO-STR-018", ["NOE-P07-KO-STR-015", "NOE-P07-KO-STR-017", "NOE-P07-KO-STR-031", "NOE-P07-KO-STR-034"]),
  item(36, "U07", "section", "Subsection 3", 93, 93, 11, 11, "NOE-P07-KO-STR-001"),
  item(37, "U07", "prose", "Rational representation consequence", 94, 94, 12, 12, "NOE-P07-KO-STR-036", ["NOE-P07-KO-STR-015", "NOE-P07-KO-STR-038", "NOE-P07-KO-STR-039"]),
  item(38, "U07", "bibliography_item", "Weber II section 58 citation", 94, 94, 12, 12, "NOE-P07-KO-STR-037"),
  item(39, "U07", "note", "Repair of the cited Weber proof", 94, 108, 12, 26, "NOE-P07-KO-STR-037", ["NOE-P07-KO-STR-040", "NOE-P07-KO-STR-041", "NOE-P07-KO-STR-042", "NOE-P07-KO-STR-043"]),
  item(40, "U07", "display", "Differentiated resolvent identity", 95, 98, 13, 16, "NOE-P07-KO-STR-039"),
  item(41, "U07", "prose", "Replacement for Weber formulas (7) and (8)", 99, 99, 17, 17, "NOE-P07-KO-STR-039", ["NOE-P07-KO-STR-042"]),
  item(42, "U07", "display", "Differential expression for omega", 100, 107, 18, 25, "NOE-P07-KO-STR-039"),
  item(43, "U07", "prose", "Summation gives the desired representation", 108, 108, 26, 26, "NOE-P07-KO-STR-039", ["NOE-P07-KO-STR-042"]),
  item(44, "U08", "section", "Subsection 4", 110, 110, 11, 11, "NOE-P07-KO-STR-001"),
  item(45, "U08", "prose", "Earlier paper, theorem locations, and Fischer attribution", 111, 111, 12, 12, "NOE-P07-KO-STR-044", ["NOE-P07-KO-STR-046", "NOE-P07-KO-STR-047", "NOE-P07-KO-STR-048", "NOE-P07-KO-STR-049", "NOE-P07-KO-STR-050"]),
  item(46, "U08", "bibliography_item", "Körper und Systeme rationaler Funktionen", 111, 111, 12, 12, "NOE-P07-KO-STR-045"),
  item(47, "U08", "note", "Math. Ann. 76 publication note", 111, 111, 12, 12, "NOE-P07-KO-STR-045", ["NOE-P07-KO-STR-048"]),
  item(48, "U08", "bibliography_item", "Math. Ann. 76, page 161 (1915)", 111, 111, 12, 12, "NOE-P07-KO-STR-047"),
  item(49, "U08", "note", "Relative-invariant finiteness note", 111, 111, 12, 12, "NOE-P07-KO-STR-045"),
  item(50, "U08", "remark", "E. Fischer attribution", 111, 111, 12, 12, "NOE-P07-KO-STR-045"),
  item(51, "U08", "date", "Erlangen, May 1915", 113, 113, 14, 14, "NOE-P07-KO-STR-044"),
  item(52, "U03", "proof", "First complete-system proof", 29, 46, 12, 29, "NOE-P07-KO-STR-012", ["NOE-P07-KO-STR-013", "NOE-P07-KO-STR-015", "NOE-P07-KO-STR-016", "NOE-P07-KO-STR-017"]),
  item(53, "U04", "proof", "Second proof setup", 49, 63, 12, 26, "NOE-P07-KO-STR-018", ["NOE-P07-KO-STR-019", "NOE-P07-KO-STR-021", "NOE-P07-KO-STR-022", "NOE-P07-KO-STR-023"]),
  item(54, "U05", "proof", "Second proof construction and theorem", 64, 89, 11, 36, "NOE-P07-KO-STR-018", ["NOE-P07-KO-STR-024", "NOE-P07-KO-STR-034"]),
  item(55, "U06", "proof", "Equivalence and degree-bound conclusion", 91, 91, 11, 11, "NOE-P07-KO-STR-018", ["NOE-P07-KO-STR-035"]),
  item(56, "U07", "proof", "Rational representation argument and source note", 94, 108, 12, 26, "NOE-P07-KO-STR-036", ["NOE-P07-KO-STR-037", "NOE-P07-KO-STR-039", "NOE-P07-KO-STR-043"]),
  item(57, "U05", "definition", "Definition of J_mu1...mun", 65, 68, 12, 15, "NOE-P07-KO-STR-025"),
  item(58, "U05", "definition", "Definition of S_mu", 70, 73, 17, 20, "NOE-P07-KO-STR-027"),
  item(59, "U05", "definition", "Definition of the xi linear forms", 75, 78, 22, 25, "NOE-P07-KO-STR-029")
];

const authorityBuffer = fs.readFileSync(authorityPath);
if (sha(authorityBuffer) !== authoritySha) {
  throw new Error("Authority file SHA-256 mismatch");
}
const sourceLines = normalizedLines(authorityPath);
const intervalBytes = sliceBytes(sourceLines, 5842, 5954);
if (intervalBytes.length !== 8511 || sha(intervalBytes) !== intervalSha) {
  throw new Error("Paper 7 interval identity mismatch");
}

const targetLinesByUnit = {};
for (const [unit, meta] of Object.entries(units)) {
  const filePath = targetPath(unit);
  const fileBuffer = fs.readFileSync(filePath);
  if (sha(fileBuffer) !== meta.targetSha) {
    throw new Error("Frozen target SHA-256 mismatch for " + unit);
  }
  targetLinesByUnit[unit] = normalizedLines(filePath);
}

const records = m.map((x, index) => {
  const unit = units[x.unit_id];
  const tPath = targetPath(x.unit_id);
  return {
    structural_id: x.structural_id,
    work_id: "NOETH-P07",
    unit_id: x.unit_id,
    kind: x.kind,
    title: x.title,
    authority: {
      pointer_id: pointerId,
      pointer_sha256: pointerSha,
      path: authorityPath,
      file_sha256: authoritySha,
      paper_interval_sha256: intervalSha
    },
    source_locator: {
      local_start: x.sourceStart,
      local_end: x.sourceEnd,
      whole_start: 5841 + x.sourceStart,
      whole_end: 5841 + x.sourceEnd
    },
    source_unit_sha256: unit.sourceSha,
    source_slice_sha256: sha(sliceBytes(sourceLines, 5841 + x.sourceStart, 5841 + x.sourceEnd)),
    target: {
      path: tPath,
      file_sha256: unit.targetSha,
      line_start: x.targetStart,
      line_end: x.targetEnd,
      slice_sha256: sha(sliceBytes(targetLinesByUnit[x.unit_id], x.targetStart, x.targetEnd))
    },
    parent_id: x.parent_id,
    order: index + 1,
    cross_references: x.cross_references,
    language: "ko",
    completion_state: "draft_text_complete",
    review_state: "unchecked",
    publication_state: "not_ready",
    continuation_cursor: "independent_korean_checker"
  };
});

const jsonlPath = path.join(scriptDir, "STRUCTURAL_INDEX.jsonl");
fs.writeFileSync(jsonlPath, records.map((r) => JSON.stringify(r)).join("\n") + "\n", "utf8");

const headers = [
  "structural_id", "work_id", "unit_id", "kind", "title", "authority_pointer_id",
  "authority_sha256", "paper_interval_sha256", "source_local_start", "source_local_end",
  "source_whole_start", "source_whole_end", "source_unit_sha256", "source_slice_sha256",
  "target_language", "target_path", "target_sha256", "target_line_start", "target_line_end",
  "target_slice_sha256", "parent_id", "order", "cross_references", "completion_state",
  "review_state", "publication_state", "continuation_cursor"
];
function csv(value) {
  const s = value === null || value === undefined ? "" : String(value);
  return /[",\r\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
}
const rows = records.map((r) => [
  r.structural_id, r.work_id, r.unit_id, r.kind, r.title, r.authority.pointer_id,
  r.authority.file_sha256, r.authority.paper_interval_sha256,
  r.source_locator.local_start, r.source_locator.local_end,
  r.source_locator.whole_start, r.source_locator.whole_end,
  r.source_unit_sha256, r.source_slice_sha256, r.language,
  r.target.path, r.target.file_sha256, r.target.line_start, r.target.line_end,
  r.target.slice_sha256, r.parent_id, r.order, r.cross_references.join("|"),
  r.completion_state, r.review_state, r.publication_state, r.continuation_cursor
].map(csv).join(","));
fs.writeFileSync(path.join(scriptDir, "STRUCTURAL_INDEX.csv"), headers.join(",") + "\n" + rows.join("\n") + "\n", "utf8");

const kindCounts = {};
for (const r of records) {
  kindCounts[r.kind] = (kindCounts[r.kind] || 0) + 1;
}
const report = {
  generated_at: new Date().toISOString(),
  operation: "mechanical structural projection build; not linguistic or formula review",
  pass: true,
  record_count: records.length,
  latest_structural_id: records[records.length - 1].structural_id,
  kind_counts: kindCounts,
  authority_sha256_verified: authoritySha,
  paper_interval_sha256_verified: intervalSha,
  target_units_verified: Object.keys(units),
  errors: []
};
fs.writeFileSync(path.join(scriptDir, "BUILD_REPORT.json"), JSON.stringify(report, null, 2) + "\n", "utf8");
console.log(JSON.stringify(report));
