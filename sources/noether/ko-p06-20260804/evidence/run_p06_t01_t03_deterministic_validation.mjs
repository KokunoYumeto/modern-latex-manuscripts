import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const evidenceRoot = path.dirname(fileURLToPath(import.meta.url));
const validatorPath = path.join(evidenceRoot, "validate_p06_t01_t03_evidence.mjs");
const validationReportPath = path.join(evidenceRoot, "P06_T01_T03_VALIDATION_REPORT.json");
const deterministicReportPath = path.join(evidenceRoot, "P06_T01_T03_DETERMINISTIC_VALIDATION_REPORT.json");
const sha = b => crypto.createHash("sha256").update(b).digest("hex").toUpperCase();
const read = p => fs.readFileSync(p);
const identity = p => ({ bytes: read(p).length, sha256: sha(read(p)) });
const run = () => {
  const result = spawnSync(process.execPath, [validatorPath], { cwd: path.dirname(evidenceRoot), encoding: "utf8" });
  if (result.error) throw result.error;
  if (result.status !== 0) throw new Error("validator exit " + result.status + "\n" + result.stderr);
  if (result.stderr !== "") throw new Error("validator stderr was not empty");
  const parsed = JSON.parse(result.stdout);
  if (parsed.status !== "PASS") throw new Error("validator did not return PASS");
  return { stdout: result.stdout, bytes: Buffer.byteLength(result.stdout, "utf8"), sha256: sha(Buffer.from(result.stdout, "utf8")) };
};
const first = run();
const second = run();
if (first.stdout !== second.stdout) throw new Error("read-only validator output changed between runs");
fs.writeFileSync(validationReportPath, first.stdout, "utf8");
const report = {
  schema_version: "1.0",
  report_id: "NOE-P06-KO-T01-T03-DETERMINISTIC-VALIDATION-20260804-001",
  recorded_at: "2026-08-04",
  time_precision: "day",
  status: "PASS",
  validator: { path: "validate_p06_t01_t03_evidence.mjs", ...identity(validatorPath) },
  runs: [
    { sequence: 1, exit_code: 0, stderr_bytes: 0, stdout_bytes: first.bytes, stdout_sha256: first.sha256 },
    { sequence: 2, exit_code: 0, stderr_bytes: 0, stdout_bytes: second.bytes, stdout_sha256: second.sha256 }
  ],
  outputs_identical: true,
  filesystem_writes_by_validator: 0,
  validation_report: { path: "P06_T01_T03_VALIDATION_REPORT.json", ...identity(validationReportPath) },
  scope: "P06 T01--T03 U01--U22 producer metadata only",
  limits: ["No source or scan review", "No Korean or formula review", "No compilation or rendering", "No assembly packaging certification approval canon archive or SGA work"]
};
fs.writeFileSync(deterministicReportPath, JSON.stringify(report, null, 2) + "\n", "utf8");
process.stdout.write(JSON.stringify({
  status: "PASS",
  output_runs_identical: true,
  validator: identity(validatorPath),
  validation_report: identity(validationReportPath),
  deterministic_report: identity(deterministicReportPath)
}, null, 2) + "\n");

