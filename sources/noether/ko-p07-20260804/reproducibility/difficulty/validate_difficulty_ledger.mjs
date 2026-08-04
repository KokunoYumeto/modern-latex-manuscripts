import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const dir = path.dirname(fileURLToPath(import.meta.url));
const ledgerPath = path.join(dir, "DIFFICULTY_LEDGER.jsonl");
const structuralPath = path.join(dir, "..", "structural", "STRUCTURAL_INDEX.jsonl");
const csvPath = path.join(dir, "DIFFICULTY_LEDGER.csv");
const errors = [];
const rawLines = fs.readFileSync(ledgerPath, "utf8").trimEnd().split("\n").filter(Boolean);
const records = [];

for (let i = 0; i < rawLines.length; i += 1) {
  try {
    records.push(JSON.parse(rawLines[i]));
  } catch (e) {
    errors.push("JSON parse failure at line " + (i + 1) + ": " + e.message);
  }
}
const structuralIds = new Set(fs.readFileSync(structuralPath, "utf8").trimEnd().split("\n").filter(Boolean).map((line) => JSON.parse(line).structural_id));
const seen = new Set();
let previous = null;
let humanValidationRecords = 0;
let writeOrToolFailureRecords = 0;
const stateCounts = {};

for (let i = 0; i < records.length; i += 1) {
  const r = records[i];
  const expectedId = "NOE-P07-KO-HARD-" + String(i + 1).padStart(3, "0");
  if (r.difficulty_id !== expectedId) errors.push("Nonsequential ID at record " + (i + 1));
  if (seen.has(r.difficulty_id)) errors.push("Duplicate ID " + r.difficulty_id);
  seen.add(r.difficulty_id);
  if (r.previous_record_sha256 !== previous) errors.push(r.difficulty_id + " previous hash mismatch");
  const copy = { ...r, record_sha256: null };
  const digest = crypto.createHash("sha256").update(JSON.stringify(copy), "utf8").digest("hex").toUpperCase();
  if (digest !== r.record_sha256) errors.push(r.difficulty_id + " record hash mismatch");
  previous = r.record_sha256;
  if (r.review_state !== "unchecked") errors.push(r.difficulty_id + " review state is not unchecked");
  if (r.evidence_classes.includes("human_validation") || r.evidence_classes.includes("external_validation")) humanValidationRecords += 1;
  if (r.category === "tool_failure_recovery" || r.category === "write_failure") writeOrToolFailureRecords += 1;
  stateCounts[r.resolution_state] = (stateCounts[r.resolution_state] || 0) + 1;
  for (const id of r.related_structural_ids) if (!structuralIds.has(id)) errors.push(r.difficulty_id + " missing structural ID " + id);
  const requiredArrays = ["alternatives_considered", "evidence_classes", "uncertainty_adverse_evidence", "attempted_approaches", "rejected_approaches", "consequences", "changed_artifacts", "recurrence_cues", "related_decision_ids", "related_structural_ids"];
  for (const key of requiredArrays) if (!Array.isArray(r[key])) errors.push(r.difficulty_id + " invalid array field " + key);
}

const csvText = fs.readFileSync(csvPath, "utf8").replace(/\r\n/g, "\n").trimEnd();
const csvRows = csvText.split("\n").length - 1;
if (csvRows !== records.length) errors.push("CSV row count mismatch");
const expectedHeader = "difficulty_id,recorded_at,time_precision,work_unit,category,stable_symptom,choice_or_control,evidence_classes,resolution_state,residual_risk,related_decision_ids,related_structural_ids,supersession_state,review_state,next_cursor,previous_record_sha256,record_sha256";
if (csvText.split("\n")[0] !== expectedHeader) errors.push("CSV header mismatch");
if (humanValidationRecords !== 0) errors.push("Unexpected external or human validation claim");

const report = {
  validated_at: new Date().toISOString(),
  operation: "append-only chain and schema-control validation; not linguistic or formula review",
  pass: errors.length === 0,
  record_count: records.length,
  csv_data_row_count: csvRows,
  latest_difficulty_id: records.length ? records[records.length - 1].difficulty_id : null,
  chain_head_sha256: previous,
  resolution_state_counts: stateCounts,
  external_or_human_validation_records: humanValidationRecords,
  actual_p07_write_or_tool_failure_records: writeOrToolFailureRecords,
  errors
};
fs.writeFileSync(path.join(dir, "VALIDATION_REPORT.json"), JSON.stringify(report, null, 2) + "\n", "utf8");
console.log(JSON.stringify(report));
if (errors.length) process.exitCode = 1;
