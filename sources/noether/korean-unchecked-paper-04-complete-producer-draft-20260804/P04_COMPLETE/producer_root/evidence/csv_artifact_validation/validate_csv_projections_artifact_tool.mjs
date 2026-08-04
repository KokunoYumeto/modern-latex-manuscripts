import fs from "node:fs/promises";
import path from "node:path";
import crypto from "node:crypto";
import { createRequire } from "node:module";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const artifactTool = require("@oai/artifact-tool");
const Workbook = artifactTool.Workbook;
if (!Workbook) {
  throw new Error("@oai/artifact-tool did not expose Workbook");
}

const scriptPath = fileURLToPath(import.meta.url);
const validationDir = path.dirname(scriptPath);
const evidenceRoot = path.dirname(validationDir);
const reportPath = path.join(validationDir, "CSV_PROJECTIONS_ARTIFACT_TOOL_VALIDATION_REPORT.json");

function sha256(value) {
  return crypto.createHash("sha256").update(value).digest("hex").toUpperCase();
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function columnName(number) {
  let value = number;
  let out = "";
  while (value > 0) {
    value -= 1;
    out = String.fromCharCode(65 + (value % 26)) + out;
    value = Math.floor(value / 26);
  }
  return out;
}

const specs = [
  {
    name: "structural_index",
    csv: path.join(evidenceRoot, "structural_index", "PRODUCER_STRUCTURAL_INDEX.csv"),
    schema: path.join(evidenceRoot, "structural_index", "PRODUCER_STRUCTURAL_INDEX.schema.json"),
    report: path.join(evidenceRoot, "structural_index", "PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json"),
  },
  {
    name: "difficulty_ledger",
    csv: path.join(evidenceRoot, "difficulty_ledger", "DIFFICULTY_LEDGER.csv"),
    schema: path.join(evidenceRoot, "difficulty_ledger", "DIFFICULTY_LEDGER.schema.json"),
    report: path.join(evidenceRoot, "difficulty_ledger", "DIFFICULTY_LEDGER_VALIDATION_REPORT.json"),
  },
  {
    name: "visual_evidence",
    csv: path.join(evidenceRoot, "visual_evidence", "VISUAL_EVIDENCE_INDEX.csv"),
    schema: path.join(evidenceRoot, "visual_evidence", "VISUAL_EVIDENCE_INDEX.schema.json"),
    report: path.join(evidenceRoot, "visual_evidence", "VISUAL_EVIDENCE_INDEX_VALIDATION_REPORT.json"),
  },
];

const results = [];
const errors = [];
for (const spec of specs) {
  try {
    const csvBytes = await fs.readFile(spec.csv);
    const csvText = csvBytes.toString("utf8");
    const schema = JSON.parse(await fs.readFile(spec.schema, "utf8"));
    const mechanicalReport = JSON.parse(await fs.readFile(spec.report, "utf8"));
    assert(mechanicalReport.status === "PASS", spec.name + " mechanical report is not PASS");
    const headers = schema["x-csv-projection"].headers;
    const expectedDataRows = mechanicalReport.record_count;
    const sheetName = spec.name.slice(0, 31);
    const workbook = await Workbook.fromCSV(csvText, { sheetName: sheetName });
    const sheet = workbook.worksheets.getItemAt(0);
    const usedRange = sheet.getUsedRange(true);
    assert(Boolean(usedRange), spec.name + " has no used range after import");
    const values = usedRange.values;
    assert(Array.isArray(values), spec.name + " used range values are unavailable");
    assert(values.length === expectedDataRows + 1, spec.name + " imported row count mismatch");
    assert(values[0].length === headers.length, spec.name + " imported column count mismatch");
    const importedHeaders = values[0].map(function (value) { return String(value); });
    assert(JSON.stringify(importedHeaders) === JSON.stringify(headers), spec.name + " imported headers differ from schema");
    const range = "A1:" + columnName(headers.length) + String(Math.min(expectedDataRows + 1, 4));
    const inspection = await workbook.inspect({
      kind: "table",
      sheetId: sheetName,
      range: range,
      maxChars: 4000,
      tableMaxRows: 4,
      tableMaxCols: Math.min(headers.length, 10),
      tableMaxCellChars: 96,
    });
    const ndjson = inspection && inspection.ndjson ? inspection.ndjson : "";
    assert(ndjson.length > 0, spec.name + " table inspection returned no NDJSON");
    results.push({
      name: spec.name,
      csv_path: path.relative(evidenceRoot, spec.csv).replace(/\\/g, "/"),
      csv_bytes: csvBytes.length,
      csv_sha256: sha256(csvBytes),
      schema_path: path.relative(evidenceRoot, spec.schema).replace(/\\/g, "/"),
      expected_data_rows: expectedDataRows,
      imported_used_rows: values.length,
      imported_used_columns: values[0].length,
      imported_header_match: true,
      inspected_range: range,
      inspection_kind: "table",
      inspection_ndjson_bytes: Buffer.byteLength(ndjson, "utf8"),
      inspection_ndjson_sha256: sha256(Buffer.from(ndjson, "utf8")),
      inspection_excerpt: ndjson.slice(0, 500),
      render_calls: 0,
      status: "PASS",
    });
  } catch (error) {
    errors.push(spec.name + ": " + error.message);
    results.push({
      name: spec.name,
      status: "FAIL",
      error: error.message,
      render_calls: 0,
    });
  }
}

const runtimeBytes = await fs.readFile(process.execPath);
const dependencyRealPath = process.env.NODE_PATH ? await fs.realpath(process.env.NODE_PATH) : "";
const report = {
  schema_version: "1.0.0",
  status: errors.length === 0 ? "PASS" : "FAIL",
  errors: errors,
  validator: path.basename(scriptPath),
  validator_sha256: sha256(await fs.readFile(scriptPath)),
  evidence_date: "2026-08-04",
  runtime: {
    node_path: process.execPath.replace(/\\/g, "/"),
    node_bytes: runtimeBytes.length,
    node_sha256: sha256(runtimeBytes),
    node_version: process.version,
    dependency_node_path: (process.env.NODE_PATH || "").replace(/\\/g, "/"),
    dependency_realpath: dependencyRealPath.replace(/\\/g, "/"),
    artifact_tool_contract_version: "2.8.6+",
  },
  csv_count: specs.length,
  imported_csv_count: results.filter(function (result) { return result.status === "PASS"; }).length,
  total_data_rows: results.reduce(function (sum, result) { return sum + (result.expected_data_rows || 0); }, 0),
  render_calls: 0,
  projections: results,
  validation_scope: "@oai/artifact-tool Workbook.fromCSV import, used-range/header inspection, and bounded table inspect for all three CSV projections.",
  excluded_scope: "No render, workbook export, source/Korean/formula review, compilation, publication, certification, or approval.",
};
await fs.mkdir(validationDir, { recursive: true });
await fs.writeFile(reportPath, JSON.stringify(report, null, 2) + "\n", "utf8");
if (report.status !== "PASS") {
  throw new Error("Artifact-tool CSV validation failed: " + errors.join("; "));
}
console.log(JSON.stringify({
  status: report.status,
  imported_csv_count: report.imported_csv_count,
  total_data_rows: report.total_data_rows,
  render_calls: report.render_calls,
}, null, 2));
