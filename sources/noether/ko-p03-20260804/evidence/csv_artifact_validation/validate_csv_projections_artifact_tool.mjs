import fs from "node:fs/promises";
import crypto from "node:crypto";
import path from "node:path";
import { Workbook } from "@oai/artifact-tool";

const [outputPath, ...inputPaths] = process.argv.slice(2);
if (!outputPath || inputPaths.length === 0) {
  throw new Error(
    "usage: node validate_csv_projections_artifact_tool.mjs OUTPUT_REPORT INPUT_CSV...",
  );
}

function sha256(buffer) {
  return crypto.createHash("sha256").update(buffer).digest("hex").toUpperCase();
}

function columnName(count) {
  let n = count;
  let result = "";
  while (n > 0) {
    n -= 1;
    result = String.fromCharCode(65 + (n % 26)) + result;
    n = Math.floor(n / 26);
  }
  return result;
}

const results = [];
const errors = [];
for (const inputPath of inputPaths) {
  const bytes = await fs.readFile(inputPath);
  const csvText = bytes.toString("utf8");
  const sheetName = path.basename(inputPath, ".csv").slice(0, 31) || "Projection";
  const workbook = await Workbook.fromCSV(csvText, { sheetName });
  const sheet = workbook.worksheets.getItem(sheetName);
  const used = sheet.getUsedRange();
  const values = used?.values ?? [];
  const rowCount = values.length;
  const columnCount = rowCount > 0
    ? Math.max(...values.map((row) => row.length))
    : 0;
  const rectangular = values.every((row) => row.length === columnCount);
  const header = rowCount > 0
    ? values[0].map((value) => String(value ?? ""))
    : [];
  const duplicateHeaders = header.filter(
    (value, index) => header.indexOf(value) !== index,
  );
  const blankHeaders = header.filter((value) => value.trim() === "").length;
  const range = rowCount && columnCount
    ? `A1:${columnName(columnCount)}${Math.min(rowCount, 6)}`
    : "A1:A1";
  const inspection = await workbook.inspect({
    kind: "region",
    sheetId: sheetName,
    range,
    maxChars: 2400,
    tableMaxRows: 6,
    tableMaxCols: Math.min(columnCount || 1, 26),
    tableMaxCellChars: 120,
  });
  const formulaErrors = await workbook.inspect({
    kind: "match",
    sheetId: sheetName,
    searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
    options: { useRegex: true, maxResults: 20 },
    summary: "CSV projection formula-error scan",
    maxChars: 1200,
  });
  const entryErrors = [];
  if (!rectangular) entryErrors.push("nonrectangular imported matrix");
  if (blankHeaders) entryErrors.push(`${blankHeaders} blank header cells`);
  if (duplicateHeaders.length) {
    entryErrors.push(`duplicate headers: ${duplicateHeaders.join(", ")}`);
  }
  if (entryErrors.length) {
    errors.push(`${inputPath}: ${entryErrors.join("; ")}`);
  }
  results.push({
    path: inputPath,
    bytes: bytes.length,
    sha256: sha256(bytes),
    imported_rows_including_header: rowCount,
    imported_data_rows: Math.max(0, rowCount - 1),
    imported_columns: columnCount,
    rectangular,
    blank_header_count: blankHeaders,
    duplicate_headers: duplicateHeaders,
    compact_inspection_sha256: sha256(
      Buffer.from(inspection.ndjson ?? "", "utf8"),
    ),
    formula_error_scan_sha256: sha256(
      Buffer.from(formulaErrors.ndjson ?? "", "utf8"),
    ),
    errors: entryErrors,
  });
}

const report = {
  tool: "@oai/artifact-tool",
  validator: "validate_csv_projections_artifact_tool.mjs",
  validation_scope:
    "CSV import, rectangularity, header uniqueness, bounded region inspection, and formula-error scan",
  generated_at: new Date().toISOString(),
  status: errors.length ? "fail" : "pass",
  files: results,
  errors,
  render_state:
    "skipped: controlling Korean translation-only role forbids rendering; no translation or spreadsheet visual approval claimed",
  publication_state: "private producer metadata only",
};
await fs.mkdir(path.dirname(outputPath), { recursive: true });
await fs.writeFile(outputPath, JSON.stringify(report, null, 2), "utf8");
if (errors.length) throw new Error(errors.join(" | "));
process.stdout.write(JSON.stringify(report));
