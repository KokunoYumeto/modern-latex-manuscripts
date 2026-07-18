import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { spawn } from "node:child_process";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";


const here = path.dirname(fileURLToPath(import.meta.url));
const files = {
  corpus: "ROMANCE_CORPUS_METADATA_v1.csv",
  routes: "ROMANCE_BRANCH_ROUTES_v1.csv",
  language: "ROMANCE_LANGUAGE_COVERAGE_v1.csv",
  variety: "ROMANCE_VARIETY_COVERAGE_v1.csv",
  rejected: "ROMANCE_REJECTED_EVIDENCE_METADATA_v1.csv",
};
const previewDir = path.join(here, "qa", "workbook_previews_v1");
await fs.mkdir(previewDir, { recursive: true });


function columnLetter(index) {
  let value = index;
  let output = "";
  while (value > 0) {
    value -= 1;
    output = String.fromCharCode(65 + (value % 26)) + output;
    value = Math.floor(value / 26);
  }
  return output;
}


function headers(csvText) {
  return csvText.split(/\r?\n/, 1)[0].replace(/^\uFEFF/, "").split(",");
}


function widthFor(header) {
  if (header === "logical_source_id") return 42;
  if (header === "record_id") return 30;
  if (/sha256|hash/i.test(header)) return 19;
  if (/locator|url/i.test(header)) return 34;
  if (/reason|notes|signal|status|domains|title|query/i.test(header)) return 30;
  if (/bytes|count|records|pages/i.test(header)) return 13;
  if (/eligible|generated|native|official/i.test(header)) return 14;
  if (/id$|_id|code/i.test(header)) return 20;
  return 16;
}


function styleDataSheet(sheet, headerNames, rowCount, tableName) {
  const colCount = headerNames.length;
  const lastCol = columnLetter(colCount);
  const used = sheet.getRange(`A1:${lastCol}${rowCount}`);
  used.format.font = { name: "Aptos", size: 9, color: "#1F2937" };
  used.format.verticalAlignment = "top";
  const header = sheet.getRange(`A1:${lastCol}1`);
  header.format = {
    fill: "#19324D",
    font: { name: "Aptos Display", size: 10, bold: true, color: "#FFFFFF" },
    wrapText: true,
    verticalAlignment: "center",
  };
  header.format.rowHeight = 32;
  sheet.freezePanes.freezeRows(1);
  sheet.freezePanes.freezeColumns(2);
  sheet.showGridLines = false;
  for (let index = 0; index < colCount; index += 1) {
    const col = sheet.getRangeByIndexes(0, index, rowCount, 1);
    col.format.columnWidth = widthFor(headerNames[index]);
    if (/reason|notes|signal|status|domains|title|query|locator|id$|_id/i.test(headerNames[index])) {
      col.format.wrapText = true;
    }
    if (/retrieved_at/i.test(headerNames[index])) {
      col.format.numberFormat = "yyyy-mm-dd hh:mm";
    }
    if (/bytes|count|records|pages/i.test(headerNames[index])) {
      col.format.numberFormat = "#,##0";
      col.format.horizontalAlignment = "right";
    }
  }
  if (rowCount > 1) {
    sheet.getRange(`A2:${lastCol}${rowCount}`).format.rowHeight = 28;
  }
  const table = sheet.tables.add(`A1:${lastCol}${rowCount}`, true, tableName);
  table.style = "TableStyleMedium2";
  table.showBandedColumns = false;
  table.showFilterButton = true;
}


const csv = {};
for (const [key, filename] of Object.entries(files)) {
  csv[key] = await fs.readFile(path.join(here, filename), "utf8");
}

const workbook = await Workbook.fromCSV(csv.corpus, { sheetName: "Corpus" });
await workbook.fromCSV(csv.routes, { sheetName: "Routes" });
await workbook.fromCSV(csv.language, { sheetName: "Language Coverage" });
await workbook.fromCSV(csv.variety, { sheetName: "Variety Coverage" });
await workbook.fromCSV(csv.rejected, { sheetName: "Rejected Evidence" });

const specs = [
  ["Corpus", headers(csv.corpus), csv.corpus.trimEnd().split(/\r?\n/).length, "CorpusMetadata"],
  ["Routes", headers(csv.routes), csv.routes.trimEnd().split(/\r?\n/).length, "BranchRoutes"],
  ["Language Coverage", headers(csv.language), csv.language.trimEnd().split(/\r?\n/).length, "LanguageCoverage"],
  ["Variety Coverage", headers(csv.variety), csv.variety.trimEnd().split(/\r?\n/).length, "VarietyCoverage"],
  ["Rejected Evidence", headers(csv.rejected), csv.rejected.trimEnd().split(/\r?\n/).length, "RejectedEvidence"],
];
for (const [sheetName, headerNames, rows, tableName] of specs) {
  styleDataSheet(workbook.worksheets.getItem(sheetName), headerNames, rows, tableName);
}

const rejectedSheet = workbook.worksheets.getItem("Rejected Evidence");
rejectedSheet.getRange("A:A").format.columnWidth = 30;
rejectedSheet.getRange("C:C").format.columnWidth = 28;
rejectedSheet.getRange("D2:D10").format.columnWidth = 58;
rejectedSheet.getRange("A2:D10").format.rowHeight = 54;
workbook.worksheets.getItem("Corpus").getRange("A2:AQ154").format.rowHeight = 44;
workbook.worksheets.getItem("Routes").getRange("A2:AI62").format.rowHeight = 46;

const corpusHeaders = headers(csv.corpus);
const routeHeaders = headers(csv.routes);
const c = (name) => columnLetter(corpusHeaders.indexOf(name) + 1);
const r = (name) => columnLetter(routeHeaders.indexOf(name) + 1);

const overview = workbook.worksheets.add("Overview");
overview.showGridLines = false;
overview.getRange("A1:H2").merge();
overview.getRange("A1").values = [["Romance corpus metadata checkpoint v1"]];
overview.getRange("A1:H2").format = {
  fill: "#19324D",
  font: { name: "Aptos Display", size: 20, bold: true, color: "#FFFFFF" },
  horizontalAlignment: "left",
  verticalAlignment: "center",
};
overview.getRange("A3:H3").merge();
overview.getRange("A3").values = [["Publication-safe metadata projection · corpus v5 · branch routes v4 · 2026-07-18"]];
overview.getRange("A3:H3").format = {
  fill: "#DCE8F2",
  font: { size: 10, italic: true, color: "#334155" },
  verticalAlignment: "center",
};

overview.getRange("A5:B5").values = [["Coverage metric", "Recomputed value"]];
overview.getRange("A6:A13").values = [
  ["Corpus records"],
  ["Primary unique"],
  ["Representation aliases"],
  ["Counting eligible"],
  ["Active bodies"],
  ["Explicit branch routes"],
  ["Active routes"],
  ["Zero-body routes"],
];
overview.getRange("B6:B13").formulas = [
  ["=COUNTA('Corpus'!$A$2:$A$154)"],
  [`=COUNTIF('Corpus'!$${c("dedupe_status")}$2:$${c("dedupe_status")}$154,"primary_unique")`],
  [`=COUNTA('Corpus'!$A$2:$A$154)-COUNTIF('Corpus'!$${c("dedupe_status")}$2:$${c("dedupe_status")}$154,"primary_unique")`],
  [`=COUNTIF('Corpus'!$${c("counting_eligible")}$2:$${c("counting_eligible")}$154,"true")`],
  [`=COUNTIF('Corpus'!$${c("active_body_eligible")}$2:$${c("active_body_eligible")}$154,"true")`],
  ["=COUNTA('Routes'!$A$2:$A$62)"],
  [`=COUNTIF('Routes'!$${r("current_active_body_count")}$2:$${r("current_active_body_count")}$62,">0")`],
  [`=COUNTIF('Routes'!$${r("current_active_body_count")}$2:$${r("current_active_body_count")}$62,0)`],
];
overview.getRange("A5:B13").format.borders = { preset: "outside", style: "thin", color: "#94A3B8" };
overview.getRange("A5:B5").format = {
  fill: "#2A7F74",
  font: { bold: true, color: "#FFFFFF" },
};
overview.getRange("B6:B13").format.numberFormat = "#,##0";
overview.getRange("B6:B13").format.horizontalAlignment = "right";

overview.getRange("D5:H5").merge();
overview.getRange("D5").values = [["Rights and evidence boundary"]];
overview.getRange("D5:H5").format = {
  fill: "#B45309",
  font: { bold: true, color: "#FFFFFF" },
};
overview.getRange("D6:H9").merge();
overview.getRange("D6").values = [[
  "Metadata only. Source PDFs, extracted text, quotations, and quotation-bearing workbooks are excluded. A public URL is not a reuse grant; rights-unresolved bodies remain outside this payload.",
]];
overview.getRange("D6:H9").format = {
  fill: "#FFF3CD",
  font: { color: "#713F12" },
  wrapText: true,
  verticalAlignment: "top",
  borders: { preset: "outside", style: "thin", color: "#D6A85F" },
};
overview.getRange("D11:H11").merge();
overview.getRange("D11").values = [["Open coverage gaps"]];
overview.getRange("D11:H11").format = {
  fill: "#7F1D1D",
  font: { bold: true, color: "#FFFFFF" },
};
overview.getRange("D12:H15").merge();
overview.getRange("D12").values = [[
  "Romansh has seven active general-school bodies but zero specialist-algebra bodies. Surmiran and Sutsilvan remain explicit zero-body routes. Fifty of 61 named branch routes remain zero-body. No dominant standard is used as a proxy.",
]];
overview.getRange("D12:H15").format = {
  fill: "#FEE2E2",
  font: { color: "#7F1D1D" },
  wrapText: true,
  verticalAlignment: "top",
  borders: { preset: "outside", style: "thin", color: "#E9A0A0" },
};
overview.getRange("A16:H16").merge();
overview.getRange("A16").values = [[
  "Claim boundary: 0 human observations · 0 native validations · 0 term promotions · no intelligibility or lane-completion claim",
]];
overview.getRange("A16:H16").format = {
  fill: "#E2E8F0",
  font: { bold: true, color: "#334155" },
  wrapText: true,
  verticalAlignment: "center",
};
overview.getRange("A1:H16").format.font = { name: "Aptos", size: 10, color: "#1F2937" };
overview.getRange("A1:H2").format.font = { name: "Aptos Display", size: 20, bold: true, color: "#FFFFFF" };
overview.getRange("A3:H3").format.font = { name: "Aptos", size: 10, italic: true, color: "#334155" };
overview.getRange("A5:B5").format.font = { bold: true, color: "#FFFFFF" };
overview.getRange("D5:H5").format.font = { bold: true, color: "#FFFFFF" };
overview.getRange("D11:H11").format.font = { bold: true, color: "#FFFFFF" };
overview.getRange("A16:H16").format.font = { bold: true, color: "#334155" };
overview.getRange("A:A").format.columnWidth = 27;
overview.getRange("B:B").format.columnWidth = 16;
overview.getRange("C:C").format.columnWidth = 3;
overview.getRange("D:H").format.columnWidth = 15;
overview.getRange("A1:H2").format.rowHeight = 30;
overview.getRange("A3:H3").format.rowHeight = 24;
overview.getRange("D6:H9").format.rowHeight = 26;
overview.getRange("D12:H15").format.rowHeight = 26;
overview.getRange("A16:H16").format.rowHeight = 32;
overview.freezePanes.freezeRows(3);

const overviewInspect = await workbook.inspect({
  kind: "table",
  range: "Overview!A1:H16",
  include: "values,formulas",
  tableMaxRows: 20,
  tableMaxCols: 10,
  maxChars: 8000,
});
const formulaErrors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
  maxChars: 4000,
});
await fs.writeFile(
  path.join(here, "qa", "WORKBOOK_MACHINE_QA_v1.ndjson"),
  `${overviewInspect.ndjson}\n${formulaErrors.ndjson}\n`,
  "utf8",
);

const renderSpecs = [
  ["Overview", "A1:H16", "overview.png"],
  ["Corpus", "A1:H12", "corpus.png"],
  ["Routes", "A1:L15", "routes.png"],
  ["Language Coverage", "A1:L10", "language_coverage.png"],
  ["Variety Coverage", "A1:L14", "variety_coverage.png"],
  ["Rejected Evidence", "A1:D10", "rejected_evidence.png"],
];
for (const [sheetName, range, filename] of renderSpecs) {
  const preview = await workbook.render({ sheetName, range, scale: 1, format: "png" });
  await fs.writeFile(path.join(previewDir, filename), new Uint8Array(await preview.arrayBuffer()));
}

const output = await SpreadsheetFile.exportXlsx(workbook);
const workbookPath = path.join(here, "ROMANCE_CORPUS_METADATA_v1.xlsx");
await output.save(workbookPath);
await new Promise((resolve, reject) => {
  const child = spawn(
    process.env.PYTHON || "python",
    [path.join(here, "normalize_xlsx_deterministic_v1.py"), workbookPath],
    { cwd: here, stdio: "inherit" },
  );
  child.on("error", reject);
  child.on("exit", (code) => code === 0 ? resolve() : reject(new Error(`XLSX normalization failed: ${code}`)));
});
