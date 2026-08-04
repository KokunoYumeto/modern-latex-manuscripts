import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const dir = path.dirname(fileURLToPath(import.meta.url));
const ledgerPath = path.join(dir, "DIFFICULTY_LEDGER.jsonl");
const csvPath = path.join(dir, "DIFFICULTY_LEDGER.csv");

function csv(value) {
  const s = value === null || value === undefined ? "" : String(value);
  return /[",\r\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
}

export function projectDifficultyCsv() {
  const records = fs.readFileSync(ledgerPath, "utf8").trimEnd().split("\n").filter(Boolean).map((line) => JSON.parse(line));
  const headers = [
    "difficulty_id", "recorded_at", "time_precision", "work_unit", "category",
    "stable_symptom", "choice_or_control", "evidence_classes", "resolution_state",
    "residual_risk", "related_decision_ids", "related_structural_ids",
    "supersession_state", "review_state", "next_cursor", "previous_record_sha256",
    "record_sha256"
  ];
  const rows = records.map((r) => [
    r.difficulty_id, r.recorded_at, r.time_precision, r.work_unit, r.category,
    r.stable_symptom, r.choice_or_control, r.evidence_classes.join("|"),
    r.resolution_state, r.residual_risk, r.related_decision_ids.join("|"),
    r.related_structural_ids.join("|"), r.supersession_state, r.review_state,
    r.next_cursor, r.previous_record_sha256, r.record_sha256
  ].map(csv).join(","));
  fs.writeFileSync(csvPath, headers.join(",") + "\n" + rows.join("\n") + "\n", "utf8");
  return records.length;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  console.log(JSON.stringify({ projected_records: projectDifficultyCsv() }));
}
