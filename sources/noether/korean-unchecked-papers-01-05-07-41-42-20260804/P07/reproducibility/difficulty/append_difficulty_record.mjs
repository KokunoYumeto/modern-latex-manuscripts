import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
import { projectDifficultyCsv } from "./project_difficulty_csv.mjs";

const dir = path.dirname(fileURLToPath(import.meta.url));
const ledgerPath = path.join(dir, "DIFFICULTY_LEDGER.jsonl");
const candidatePath = process.argv[2];
if (!candidatePath) throw new Error("Provide a candidate JSON file path");

const existingLines = fs.readFileSync(ledgerPath, "utf8").trimEnd().split("\n").filter(Boolean);
const previous = JSON.parse(existingLines[existingLines.length - 1]);
const candidate = JSON.parse(fs.readFileSync(path.resolve(candidatePath), "utf8"));
if (candidate.previous_record_sha256 !== undefined || candidate.record_sha256 !== undefined) {
  throw new Error("Candidate must omit chain fields; the append utility controls them");
}
candidate.previous_record_sha256 = previous.record_sha256;
candidate.record_sha256 = null;
const digest = crypto.createHash("sha256").update(JSON.stringify(candidate), "utf8").digest("hex").toUpperCase();
candidate.record_sha256 = digest;
fs.appendFileSync(ledgerPath, JSON.stringify(candidate) + "\n", "utf8");
const projected = projectDifficultyCsv();
console.log(JSON.stringify({ appended: candidate.difficulty_id, record_sha256: digest, csv_projected_records: projected }));
