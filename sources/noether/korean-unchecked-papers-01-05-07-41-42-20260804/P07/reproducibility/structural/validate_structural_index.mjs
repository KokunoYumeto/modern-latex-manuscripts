import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const dir = path.dirname(fileURLToPath(import.meta.url));
const jsonlPath = path.join(dir, "STRUCTURAL_INDEX.jsonl");
const csvPath = path.join(dir, "STRUCTURAL_INDEX.csv");
const errors = [];

function sha(data) {
  return crypto.createHash("sha256").update(data).digest("hex").toUpperCase();
}
function lines(filePath) {
  return fs.readFileSync(filePath, "utf8").replace(/\r\n/g, "\n").replace(/\r/g, "\n").split("\n");
}
function sliceBytes(a, start, end) {
  return Buffer.from(a.slice(start - 1, end).join("\n") + "\n", "utf8");
}

const rawLines = fs.readFileSync(jsonlPath, "utf8").trimEnd().split("\n");
const records = rawLines.map((line, i) => {
  try {
    return JSON.parse(line);
  } catch (e) {
    errors.push("JSON parse failure at record " + (i + 1) + ": " + e.message);
    return null;
  }
}).filter(Boolean);

const ids = new Set();
const requiredKinds = new Set(["section", "publication_metadata", "title", "byline", "prose", "note", "bibliography_item", "display", "definition", "theorem", "remark", "proof", "date"]);
const foundKinds = new Set();
const sourceCache = new Map();
const targetCache = new Map();

for (let i = 0; i < records.length; i += 1) {
  const r = records[i];
  const required = ["structural_id", "work_id", "unit_id", "kind", "title", "authority", "source_locator", "source_unit_sha256", "source_slice_sha256", "target", "parent_id", "order", "cross_references", "language", "completion_state", "review_state", "publication_state", "continuation_cursor"];
  for (const key of required) {
    if (!(key in r)) errors.push(r.structural_id + " missing " + key);
  }
  if (ids.has(r.structural_id)) errors.push("Duplicate structural ID " + r.structural_id);
  ids.add(r.structural_id);
  foundKinds.add(r.kind);
  if (r.order !== i + 1) errors.push(r.structural_id + " nonsequential order");
  if (r.language !== "ko" || r.review_state !== "unchecked" || r.publication_state !== "not_ready" || r.completion_state !== "draft_text_complete") {
    errors.push(r.structural_id + " invalid state control");
  }
  if (r.continuation_cursor !== "independent_korean_checker") errors.push(r.structural_id + " invalid continuation cursor");
  if (r.source_locator.whole_start !== 5841 + r.source_locator.local_start || r.source_locator.whole_end !== 5841 + r.source_locator.local_end) {
    errors.push(r.structural_id + " source locator mapping failure");
  }
  if (!sourceCache.has(r.authority.path)) sourceCache.set(r.authority.path, lines(r.authority.path));
  const sLines = sourceCache.get(r.authority.path);
  const sourceHash = sha(sliceBytes(sLines, r.source_locator.whole_start, r.source_locator.whole_end));
  if (sourceHash !== r.source_slice_sha256) errors.push(r.structural_id + " source slice hash mismatch");
  if (!targetCache.has(r.target.path)) {
    const buffer = fs.readFileSync(r.target.path);
    targetCache.set(r.target.path, { lines: lines(r.target.path), sha: sha(buffer) });
  }
  const target = targetCache.get(r.target.path);
  if (target.sha !== r.target.file_sha256) errors.push(r.structural_id + " target file hash mismatch");
  const targetHash = sha(sliceBytes(target.lines, r.target.line_start, r.target.line_end));
  if (targetHash !== r.target.slice_sha256) errors.push(r.structural_id + " target slice hash mismatch");
}

for (const r of records) {
  if (r.parent_id !== null && !ids.has(r.parent_id)) errors.push(r.structural_id + " missing parent " + r.parent_id);
  for (const ref of r.cross_references) if (!ids.has(ref)) errors.push(r.structural_id + " missing cross-reference " + ref);
}
for (const kind of requiredKinds) if (!foundKinds.has(kind)) errors.push("Required kind absent: " + kind);
if (records.length !== 59) errors.push("Expected 59 records, found " + records.length);
if (records.length && records[records.length - 1].structural_id !== "NOE-P07-KO-STR-059") errors.push("Latest structural ID mismatch");

const csvText = fs.readFileSync(csvPath, "utf8").replace(/\r\n/g, "\n").trimEnd();
const csvRowCount = csvText.split("\n").length - 1;
if (csvRowCount !== records.length) errors.push("CSV row count mismatch");
const expectedHeader = "structural_id,work_id,unit_id,kind,title,authority_pointer_id,authority_sha256,paper_interval_sha256,source_local_start,source_local_end,source_whole_start,source_whole_end,source_unit_sha256,source_slice_sha256,target_language,target_path,target_sha256,target_line_start,target_line_end,target_slice_sha256,parent_id,order,cross_references,completion_state,review_state,publication_state,continuation_cursor";
if (csvText.split("\n")[0] !== expectedHeader) errors.push("CSV header mismatch");

const report = {
  validated_at: new Date().toISOString(),
  operation: "mechanical structural validation; not linguistic or formula review",
  pass: errors.length === 0,
  record_count: records.length,
  csv_data_row_count: csvRowCount,
  latest_structural_id: records.length ? records[records.length - 1].structural_id : null,
  unique_target_files: targetCache.size,
  kind_count: foundKinds.size,
  errors
};
fs.writeFileSync(path.join(dir, "VALIDATION_REPORT.json"), JSON.stringify(report, null, 2) + "\n", "utf8");
console.log(JSON.stringify(report));
if (errors.length) process.exitCode = 1;
