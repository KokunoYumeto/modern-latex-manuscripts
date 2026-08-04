import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, "..");
const edPath = "C:\\Users\\Floris\\Documents\\interlanguage\\03_projects\\noether\\07_german_canon_control\\candidates\\ED0002\\noether.tex";
const logPath = "C:\\Users\\Floris\\Documents\\interlanguage\\03_projects\\language_management\\cjk\\00_lane_control\\CJK_DECISION_LOGBOOK_20260718.md";
const categories = {
  manifest: [],
  structural: [],
  difficulty: [],
  visual: []
};
const add = (category, code, detail) => categories[category].push({ code, detail });
const check = (category, condition, code, detail) => {
  if (!condition) add(category, code, detail);
};
const shaBuffer = (buffer) => crypto.createHash("sha256").update(buffer).digest("hex").toUpperCase();
const fileInfo = (file) => {
  const bytes = fs.readFileSync(file);
  return { bytes: bytes.length, sha256: shaBuffer(bytes) };
};
const readJson = (file) => JSON.parse(fs.readFileSync(file, "utf8"));
const readJsonl = (file) => {
  const text = fs.readFileSync(file, "utf8");
  if (text.length === 0) return [];
  return text.trim().split("\n").filter(Boolean).map((line, index) => {
    try {
      return JSON.parse(line);
    } catch (error) {
      throw new Error(file + " line " + (index + 1) + ": " + error.message);
    }
  });
};
const norm = (text) => text.replace(/\r\n/g, "\n").replace(/\r/g, "\n");
const edLines = norm(fs.readFileSync(edPath, "utf8")).split("\n");
const sourceSlice = (start, end) => Buffer.from(edLines.slice(start - 1, end).join("\n") + "\n", "utf8");
const unitId = (number) => "U" + String(number).padStart(2, "0");
const trancheId = (number) => "T" + String(number).padStart(2, "0");
const isSha = (value) => typeof value === "string" && /^[A-F0-9]{64}$/.test(value);
const relResolve = (relative) => path.resolve(root, relative.replaceAll("/", path.sep));
const insideRoot = (absolute) => absolute === root || absolute.startsWith(root + path.sep);
const csvRows = (file) => {
  const text = fs.readFileSync(file, "utf8");
  return text.length === 0 ? 0 : text.replace(/\n$/, "").split("\n").length - 1;
};
const countBy = (records, field) => {
  const result = {};
  for (const record of records) result[record[field]] = (result[record[field]] || 0) + 1;
  return Object.fromEntries(Object.entries(result).sort(([a], [b]) => a.localeCompare(b)));
};

const manifestPath = path.join(root, "manifest.json");
const manifestCsvPath = path.join(root, "manifest.csv");
const structuralDir = path.join(here, "structural_index");
const structuralPath = path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX.jsonl");
const structuralCsvPath = path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX.csv");
const structuralSchemaPath = path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX.schema.json");
const difficultyDir = path.join(here, "difficulty_ledger");
const difficultyPath = path.join(difficultyDir, "DIFFICULTY_LEDGER.jsonl");
const difficultyCsvPath = path.join(difficultyDir, "DIFFICULTY_LEDGER.csv");
const difficultySchemaPath = path.join(difficultyDir, "DIFFICULTY_LEDGER.schema.json");
const visualDir = path.join(here, "visual_evidence");
const visualPath = path.join(visualDir, "VISUAL_EVIDENCE_INDEX.jsonl");
const visualCsvPath = path.join(visualDir, "VISUAL_EVIDENCE_INDEX.csv");
const visualSchemaPath = path.join(visualDir, "VISUAL_EVIDENCE_INDEX.schema.json");
const freezePath = path.join(here, "prefix_freezes", "P06_T03_EVIDENCE_PREFIX_FREEZE_20260804.json");
const validatorPath = path.join(here, "validate.mjs");

const manifest = readJson(manifestPath);
const structuralSchema = readJson(structuralSchemaPath);
const difficultySchema = readJson(difficultySchemaPath);
const visualSchema = readJson(visualSchemaPath);
const structural = readJsonl(structuralPath);
const difficulty = readJsonl(difficultyPath);
const visual = readJsonl(visualPath);
const freeze = readJson(freezePath);
const laneLog = fs.readFileSync(logPath, "utf8");

check("manifest", manifest.schema_version === "1.0", "MANIFEST_SCHEMA", manifest.schema_version);
check("manifest", manifest.work_id === "NOE-P06" && manifest.language === "ko", "MANIFEST_WORK_LANGUAGE", manifest.work_id + "/" + manifest.language);
check("manifest", manifest.pointer_id === "NOETH-DE-AUTH-v009-20260804", "MANIFEST_POINTER", manifest.pointer_id);
check("manifest", manifest.pointer_sha256 === "B06BE3530D9CF2E82B56FDBA7FE41D5D044DF2425DFA2A059D4939EAA2F7A6C2", "MANIFEST_POINTER_SHA", manifest.pointer_sha256);
check("manifest", manifest.authority_id === "NOETH-DE-ED-0002", "MANIFEST_AUTHORITY", manifest.authority_id);
check("manifest", manifest.authority_sha256 === "C9A125167ACB33D914EE4374B65AE7CDF0052F568371B8B77B720EA178ABF0E3", "MANIFEST_AUTHORITY_SHA", manifest.authority_sha256);
check("manifest", JSON.stringify(manifest.source_content_lines) === "[4576,5828]", "MANIFEST_SOURCE_LINES", JSON.stringify(manifest.source_content_lines));
check("manifest", manifest.source_content_sha256 === shaBuffer(sourceSlice(4576, 5828)), "MANIFEST_SOURCE_SHA", manifest.source_content_sha256);
check("manifest", manifest.target_count === 228 && manifest.entries.length === 228, "MANIFEST_TARGET_COUNT", manifest.target_count + "/" + manifest.entries.length);
check("manifest", Array.isArray(manifest.missing_units) && manifest.missing_units.length === 0, "MANIFEST_MISSING", JSON.stringify(manifest.missing_units));
check("manifest", Array.isArray(manifest.duplicate_units) && manifest.duplicate_units.length === 0, "MANIFEST_DUPLICATES", JSON.stringify(manifest.duplicate_units));
check("manifest", manifest.completion_state === "complete_producer_draft_text_coverage", "MANIFEST_COMPLETION_STATE", manifest.completion_state);
check("manifest", manifest.review_state === "unchecked" && manifest.build_state === "not_built" && manifest.render_state === "not_rendered" && manifest.visual_state === "zero_records", "MANIFEST_GATE_STATE", JSON.stringify({ review_state: manifest.review_state, build_state: manifest.build_state, render_state: manifest.render_state, visual_state: manifest.visual_state }));

let totalTargetBytes = 0;
const treeLines = [];
const manifestUnits = new Set();
for (let index = 0; index < manifest.entries.length; index++) {
  const entry = manifest.entries[index];
  const expectedUnit = unitId(index + 1);
  check("manifest", entry.unit_id === expectedUnit, "MANIFEST_UNIT_ORDER", index + ":" + entry.unit_id + " expected " + expectedUnit);
  check("manifest", /^T(0[1-9]|1[0-6])$/.test(entry.tranche_id), "MANIFEST_TRANCHE", entry.unit_id + ":" + entry.tranche_id);
  check("manifest", !manifestUnits.has(entry.unit_id), "MANIFEST_UNIT_DUPLICATE", entry.unit_id);
  manifestUnits.add(entry.unit_id);
  const target = relResolve(entry.target_path);
  check("manifest", insideRoot(target), "MANIFEST_PATH_ESCAPE", entry.target_path);
  if (!insideRoot(target) || !fs.existsSync(target)) {
    add("manifest", "MANIFEST_TARGET_MISSING", entry.target_path);
    continue;
  }
  const raw = fs.readFileSync(target);
  const actualSha = shaBuffer(raw);
  totalTargetBytes += raw.length;
  treeLines.push(entry.target_path + "\0" + raw.length + "\0" + actualSha + "\n");
  check("manifest", raw.length === entry.target_bytes, "MANIFEST_TARGET_BYTES", entry.unit_id + ":" + raw.length + " != " + entry.target_bytes);
  check("manifest", actualSha === entry.target_sha256, "MANIFEST_TARGET_SHA", entry.unit_id + ":" + actualSha + " != " + entry.target_sha256);
  check("manifest", raw.length > 0 && raw[raw.length - 1] === 10, "MANIFEST_TERMINAL_LF", entry.unit_id);
  check("manifest", !(raw.length >= 3 && raw[0] === 239 && raw[1] === 187 && raw[2] === 191), "MANIFEST_BOM", entry.unit_id);
  check("manifest", !raw.includes(13), "MANIFEST_CR", entry.unit_id);
  check("manifest", !raw.includes(27), "MANIFEST_ESC", entry.unit_id);
  const source = sourceSlice(entry.source_line_start, entry.source_line_end);
  check("manifest", source.length === entry.source_bytes, "MANIFEST_SOURCE_BYTES", entry.unit_id + ":" + source.length + " != " + entry.source_bytes);
  check("manifest", shaBuffer(source) === entry.source_sha256, "MANIFEST_UNIT_SOURCE_SHA", entry.unit_id);
  check("manifest", entry.state === "UNCHECKED", "MANIFEST_UNIT_STATE", entry.unit_id + ":" + entry.state);
}
check("manifest", totalTargetBytes === 239507 && manifest.target_bytes === totalTargetBytes, "MANIFEST_TOTAL_BYTES", totalTargetBytes + "/" + manifest.target_bytes);
check("manifest", shaBuffer(Buffer.from(treeLines.join(""), "utf8")) === manifest.target_tree_sha256, "MANIFEST_TREE_SHA", manifest.target_tree_sha256);
check("manifest", manifest.target_tree_sha256 === "934C11A3B61073DCE56F659103611006CB9747D09FDD31964A39969972C0FD19", "MANIFEST_TREE_EXPECTED", manifest.target_tree_sha256);
check("manifest", Object.values(manifest.control_state).every((value) => value === 0), "MANIFEST_CONTROL_STATE", JSON.stringify(manifest.control_state));
check("manifest", csvRows(manifestCsvPath) === 228, "MANIFEST_CSV_ROWS", csvRows(manifestCsvPath));

const structuralRequired = structuralSchema.required;
const structuralAllowed = new Set(Object.keys(structuralSchema.properties));
const structuralIds = new Set();
const structuralOrders = new Set();
const pointerPairs = new Map([
  ["NOETH-DE-AUTH-v006-20260804", "DB99DD87100654674D7ED24B4ABBBBC3A9920CCF035740D276CE8A87A5313C18"],
  ["NOETH-DE-AUTH-v007-20260804", "A6A8FC8E5AC24ACAF49DFD55B4B58FA3DA882EF8C3FDD4D136220C8751045156"],
  ["NOETH-DE-AUTH-v008-20260804", "F13E6D896DE6403829FE902609668AB3E3FCA8C3C7FAA07BE5F7A7A72A4C33D8"],
  ["NOETH-DE-AUTH-v009-20260804", "B06BE3530D9CF2E82B56FDBA7FE41D5D044DF2425DFA2A059D4939EAA2F7A6C2"]
]);
const authorityPairs = new Map([
  ["NOETH-DE-ED-0001", "D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB"],
  ["NOETH-DE-ED-0002", "C9A125167ACB33D914EE4374B65AE7CDF0052F568371B8B77B720EA178ABF0E3"]
]);
const recordTypes = new Set(structuralSchema.properties.record_type.enum);
const classifications = new Set(structuralSchema.properties.classification.enum);
for (const record of structural) {
  for (const key of structuralRequired) check("structural", Object.prototype.hasOwnProperty.call(record, key), "STRUCT_REQUIRED", record.structural_id + ":" + key);
  for (const key of Object.keys(record)) check("structural", structuralAllowed.has(key), "STRUCT_EXTRA_KEY", record.structural_id + ":" + key);
  check("structural", typeof record.structural_id === "string" && record.structural_id.startsWith("NOE-P06-KO-"), "STRUCT_ID_FORMAT", record.structural_id);
  check("structural", !structuralIds.has(record.structural_id), "STRUCT_ID_DUPLICATE", record.structural_id);
  structuralIds.add(record.structural_id);
  check("structural", Number.isInteger(record.global_order) && record.global_order >= 1, "STRUCT_ORDER_FORMAT", record.structural_id);
  check("structural", !structuralOrders.has(record.global_order), "STRUCT_ORDER_DUPLICATE", String(record.global_order));
  structuralOrders.add(record.global_order);
  check("structural", record.work_id === "NOE-P06" && record.source_language === "de" && record.target_language === "ko", "STRUCT_WORK_LANGUAGE", record.structural_id);
  check("structural", /^T(0[1-9]|1[0-6])$/.test(record.tranche_id), "STRUCT_TRANCHE", record.structural_id + ":" + record.tranche_id);
  check("structural", record.unit_id === null || /^U(0[1-9]|[1-9][0-9]|1[0-9]{2}|2[0-1][0-9]|22[0-8])$/.test(record.unit_id), "STRUCT_UNIT", record.structural_id + ":" + record.unit_id);
  check("structural", recordTypes.has(record.record_type), "STRUCT_TYPE", record.structural_id + ":" + record.record_type);
  check("structural", classifications.has(record.classification), "STRUCT_CLASS", record.structural_id + ":" + record.classification);
  check("structural", record.completion_state === "producer_draft_coverage" && record.review_state === "unchecked" && record.publication_state === "eligible_with_honest_metadata", "STRUCT_STATE", record.structural_id);
  check("structural", pointerPairs.get(record.pointer_id) === record.pointer_sha256, "STRUCT_POINTER_PAIR", record.structural_id);
  check("structural", authorityPairs.get(record.authority_id) === record.authority_sha256, "STRUCT_AUTHORITY_PAIR", record.structural_id);
  check("structural", isSha(record.source_sha256) && isSha(record.target_sha256), "STRUCT_SHA_FORMAT", record.structural_id);
  const start = record.source_locator && record.source_locator.whole_line_start;
  const end = record.source_locator && record.source_locator.whole_line_end;
  const directSpanHash = record.record_type === "unit" || record.global_order > 156;
  check("structural", Number.isInteger(start) && Number.isInteger(end) && start >= 4576 && end <= 5828 && start <= end, "STRUCT_SOURCE_RANGE", record.structural_id + ":" + start + "-" + end);
  if (directSpanHash && Number.isInteger(start) && Number.isInteger(end) && start >= 4576 && end <= 5828 && start <= end) {
    check("structural", shaBuffer(sourceSlice(start, end)) === record.source_sha256, "STRUCT_SOURCE_SHA", record.structural_id);
  }
  if (record.target_locator && record.target_locator.path && record.target_locator.line_start !== null && record.target_locator.line_end !== null) {
    const target = relResolve(record.target_locator.path);
    check("structural", insideRoot(target), "STRUCT_TARGET_PATH_ESCAPE", record.structural_id + ":" + record.target_locator.path);
    if (insideRoot(target) && fs.existsSync(target) && fs.statSync(target).isFile()) {
      const text = fs.readFileSync(target, "utf8");
      const lines = text.split("\n");
      const lineCount = text.endsWith("\n") ? lines.length - 1 : lines.length;
      const lineStart = record.target_locator.line_start;
      const lineEnd = record.target_locator.line_end;
      check("structural", Number.isInteger(lineStart) && Number.isInteger(lineEnd) && lineStart >= 1 && lineEnd >= lineStart && lineEnd <= lineCount, "STRUCT_TARGET_RANGE", record.structural_id + ":" + lineStart + "-" + lineEnd + "/" + lineCount);
      if (Number.isInteger(lineStart) && Number.isInteger(lineEnd) && lineStart >= 1 && lineEnd >= lineStart && lineEnd <= lineCount) {
        const span = Buffer.from(lines.slice(lineStart - 1, lineEnd).join("\n") + "\n", "utf8");
        if (directSpanHash) check("structural", shaBuffer(span) === record.target_sha256, "STRUCT_TARGET_SHA", record.structural_id);
      }
    } else {
      add("structural", "STRUCT_TARGET_MISSING", record.structural_id + ":" + record.target_locator.path);
    }
  }
}
for (let index = 0; index < structural.length; index++) {
  check("structural", structural[index].global_order === index + 1, "STRUCT_ORDER_CONTIGUOUS", structural[index].structural_id + ":" + structural[index].global_order + " expected " + (index + 1));
}
for (const record of structural) {
  if (record.parent_id !== null) check("structural", structuralIds.has(record.parent_id), "STRUCT_PARENT_MISSING", record.structural_id + ":" + record.parent_id);
  for (const relation of record.relations) {
    check("structural", typeof relation.type === "string" && typeof relation.target_id === "string" && (relation.scope === "internal" || relation.scope === "external") && typeof relation.basis === "string", "STRUCT_RELATION_SHAPE", record.structural_id);
    if (relation.scope === "internal") check("structural", structuralIds.has(relation.target_id), "STRUCT_RELATION_TARGET", record.structural_id + ":" + relation.target_id);
  }
}
const structuralUnitRecords = structural.filter((record) => record.record_type === "unit");
const structuralTrancheRecords = structural.filter((record) => record.record_type === "tranche");
check("structural", structural.length === 833, "STRUCT_COUNT", String(structural.length));
check("structural", structuralUnitRecords.length === 228, "STRUCT_UNIT_COUNT", String(structuralUnitRecords.length));
check("structural", structuralTrancheRecords.length === 16, "STRUCT_TRANCHE_COUNT", String(structuralTrancheRecords.length));
for (let number = 1; number <= 228; number++) {
  const id = unitId(number);
  const records = structuralUnitRecords.filter((record) => record.unit_id === id);
  check("structural", records.length === 1, "STRUCT_UNIT_COVERAGE", id + ":" + records.length);
  const manifestEntry = manifest.entries[number - 1];
  if (records.length === 1) {
    check("structural", records[0].target_sha256 === manifestEntry.target_sha256, "STRUCT_UNIT_MANIFEST_TARGET", id);
    check("structural", records[0].source_sha256 === manifestEntry.source_sha256, "STRUCT_UNIT_MANIFEST_SOURCE", id);
  }
}
for (let number = 1; number <= 16; number++) {
  const id = trancheId(number);
  check("structural", structuralTrancheRecords.filter((record) => record.tranche_id === id).length === 1, "STRUCT_TRANCHE_COVERAGE", id);
}
const currentWork = structural.find((record) => record.structural_id === "NOE-P06-KO-WORK-002");
check("structural", Boolean(currentWork), "STRUCT_CURRENT_WORK", "NOE-P06-KO-WORK-002");
if (currentWork) {
  check("structural", currentWork.source_locator.whole_line_start === 4576 && currentWork.source_locator.whole_line_end === 5828, "STRUCT_CURRENT_WORK_RANGE", JSON.stringify(currentWork.source_locator));
  check("structural", currentWork.source_sha256 === manifest.source_content_sha256, "STRUCT_CURRENT_WORK_SHA", currentWork.source_sha256);
}
check("structural", csvRows(structuralCsvPath) === structural.length, "STRUCT_CSV_ROWS", csvRows(structuralCsvPath) + "/" + structural.length);
const structuralPrefix = fs.readFileSync(structuralPath).subarray(0, freeze.prefix_through_scope.structural_jsonl.bytes);
check("structural", structuralPrefix.length === freeze.prefix_through_scope.structural_jsonl.bytes && shaBuffer(structuralPrefix) === freeze.prefix_through_scope.structural_jsonl.sha256, "STRUCT_PREFIX_FREEZE", shaBuffer(structuralPrefix));

const difficultyRequired = difficultySchema.required;
const difficultyAllowed = new Set(Object.keys(difficultySchema.properties));
const difficultyIds = new Set();
const correctedHistoricalArtifacts = new Set([
  ...(difficulty.some((record) => record.record_id === "CJK-KO-P06-HARD-037")
    ? ["CJK-KO-P06-HARD-036:evidence/validate.mjs"]
    : []),
  ...(difficulty.some((record) => record.record_id === "CJK-KO-P06-HARD-038")
    ? ["CJK-KO-P06-HARD-034:evidence/extend.mjs", "CJK-KO-P06-HARD-035:evidence/extend.mjs"]
    : [])
]);
for (let index = 0; index < difficulty.length; index++) {
  const record = difficulty[index];
  for (const key of difficultyRequired) check("difficulty", Object.prototype.hasOwnProperty.call(record, key), "DIFF_REQUIRED", record.record_id + ":" + key);
  for (const key of Object.keys(record)) check("difficulty", difficultyAllowed.has(key), "DIFF_EXTRA_KEY", record.record_id + ":" + key);
  const expectedId = "CJK-KO-P06-HARD-" + String(index + 1).padStart(3, "0");
  check("difficulty", record.record_id === expectedId, "DIFF_ID_SEQUENCE", record.record_id + " expected " + expectedId);
  check("difficulty", record.sequence === index + 1, "DIFF_SEQUENCE", record.record_id + ":" + record.sequence);
  check("difficulty", !difficultyIds.has(record.record_id), "DIFF_ID_DUPLICATE", record.record_id);
  difficultyIds.add(record.record_id);
  const expectedPrevious = index === 0 ? null : difficulty[index - 1].record_id;
  check("difficulty", record.previous_record_id === expectedPrevious, "DIFF_PREVIOUS", record.record_id + ":" + record.previous_record_id + " expected " + expectedPrevious);
  check("difficulty", record.work_id === "NOE-P06", "DIFF_WORK", record.record_id);
  check("difficulty", ["resolved", "held", "active_control", "retry_specified"].includes(record.state), "DIFF_STATE", record.record_id + ":" + record.state);
  check("difficulty", ["source_fact", "computation", "editorial_inference", "model_preference", "external_validation", "human_validation"].includes(record.classification), "DIFF_CLASS", record.record_id + ":" + record.classification);
  check("difficulty", Array.isArray(record.attempted_approaches) && record.attempted_approaches.length > 0, "DIFF_ATTEMPTS", record.record_id);
  for (const artifact of record.target_artifacts) {
    const target = relResolve(artifact.path);
    check("difficulty", insideRoot(target), "DIFF_ARTIFACT_PATH_ESCAPE", record.record_id + ":" + artifact.path);
    if (insideRoot(target) && fs.existsSync(target) && fs.statSync(target).isFile()) {
      const info = fileInfo(target);
      const artifactKey = record.record_id + ":" + artifact.path;
      if (!correctedHistoricalArtifacts.has(artifactKey)) {
        check("difficulty", info.bytes === artifact.bytes, "DIFF_ARTIFACT_BYTES", artifactKey);
        check("difficulty", info.sha256 === artifact.sha256, "DIFF_ARTIFACT_SHA", artifactKey);
      }
    } else {
      add("difficulty", "DIFF_ARTIFACT_MISSING", record.record_id + ":" + artifact.path);
    }
  }
  for (const structuralId of record.related_structural_ids) check("difficulty", structuralIds.has(structuralId), "DIFF_STRUCTURAL_LINK", record.record_id + ":" + structuralId);
  for (const decisionId of record.related_decision_ids) check("difficulty", laneLog.includes(decisionId), "DIFF_DECISION_LINK", record.record_id + ":" + decisionId);
}
check("difficulty", difficulty.length === 38, "DIFF_COUNT", String(difficulty.length));
check("difficulty", csvRows(difficultyCsvPath) === difficulty.length, "DIFF_CSV_ROWS", csvRows(difficultyCsvPath) + "/" + difficulty.length);
const difficultyPrefix = fs.readFileSync(difficultyPath).subarray(0, freeze.prefix_through_scope.difficulty_jsonl.bytes);
check("difficulty", difficultyPrefix.length === freeze.prefix_through_scope.difficulty_jsonl.bytes && shaBuffer(difficultyPrefix) === freeze.prefix_through_scope.difficulty_jsonl.sha256, "DIFF_PREFIX_FREEZE", shaBuffer(difficultyPrefix));

check("visual", visualSchema.title === "Noether Paper 6 Korean visual-evidence record", "VISUAL_SCHEMA", visualSchema.title);
check("visual", visual.length === 0, "VISUAL_RECORD_COUNT", String(visual.length));
check("visual", fileInfo(visualPath).bytes === 0 && fileInfo(visualPath).sha256 === "E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855", "VISUAL_JSONL_ZERO", JSON.stringify(fileInfo(visualPath)));
check("visual", csvRows(visualCsvPath) === 0, "VISUAL_CSV_ROWS", String(csvRows(visualCsvPath)));
const imageExtensions = new Set([".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp", ".gif", ".pdf"]);
const visualFiles = fs.readdirSync(visualDir, { withFileTypes: true }).filter((entry) => entry.isFile() && imageExtensions.has(path.extname(entry.name).toLowerCase()));
check("visual", visualFiles.length === 0, "VISUAL_IMAGE_FILES", visualFiles.map((entry) => entry.name).join(","));

const validatorInfo = fileInfo(validatorPath);
const structuralInfo = fileInfo(structuralPath);
const structuralCsvInfo = fileInfo(structuralCsvPath);
const difficultyInfo = fileInfo(difficultyPath);
const difficultyCsvInfo = fileInfo(difficultyCsvPath);
const manifestInfo = fileInfo(manifestPath);
const manifestCsvInfo = fileInfo(manifestCsvPath);
const visualInfo = fileInfo(visualPath);
const visualCsvInfo = fileInfo(visualCsvPath);
const structuralReport = {
  schema: path.basename(structuralSchemaPath),
  schema_sha256: fileInfo(structuralSchemaPath).sha256,
  validator: "../validate.mjs",
  validator_sha256: validatorInfo.sha256,
  status: categories.structural.length === 0 ? "PASS" : "FAIL",
  scope: "Noether Paper 6 Korean T01--T16 U01--U228 complete producer topology",
  record_count: structural.length,
  unique_record_count: structuralIds.size,
  latest_structural_id: structural.at(-1)?.structural_id || null,
  type_counts: countBy(structural, "record_type"),
  hierarchy_checks: {
    parent_ids_present: !categories.structural.some((error) => error.code === "STRUCT_PARENT_MISSING"),
    internal_relation_targets_present: !categories.structural.some((error) => error.code === "STRUCT_RELATION_TARGET"),
    global_orders_unique_and_contiguous: !categories.structural.some((error) => error.code.startsWith("STRUCT_ORDER"))
  },
  coverage: {
    tranches: structuralTrancheRecords.length,
    units: structuralUnitRecords.length,
    source_lines: [4576, 5828],
    target_files: manifest.target_count,
    target_bytes: manifest.target_bytes,
    target_tree_sha256: manifest.target_tree_sha256
  },
  append_only_prefix: {
    bytes: freeze.prefix_through_scope.structural_jsonl.bytes,
    sha256: freeze.prefix_through_scope.structural_jsonl.sha256,
    verified: !categories.structural.some((error) => error.code === "STRUCT_PREFIX_FREEZE")
  },
  jsonl: { bytes: structuralInfo.bytes, sha256: structuralInfo.sha256 },
  csv: { data_rows: csvRows(structuralCsvPath), bytes: structuralCsvInfo.bytes, sha256: structuralCsvInfo.sha256 },
  errors: categories.structural,
  continuation_cursor: "Independent Korean checker and full-work assembly/build/render/visual QA; producer moves to the next missing Noether paper.",
  limits: [
    "Structure classes are producer/computational annotations, not semantic approval.",
    "No source, Korean, formula, compilation, rendering, assembly, certification, or human validation is inferred."
  ]
};
const difficultyReport = {
  schema: path.basename(difficultySchemaPath),
  schema_sha256: fileInfo(difficultySchemaPath).sha256,
  validator: "../validate.mjs",
  validator_sha256: validatorInfo.sha256,
  status: categories.difficulty.length === 0 ? "PASS" : "FAIL",
  append_only: true,
  predecessor_sequence_verified: !categories.difficulty.some((error) => error.code === "DIFF_PREVIOUS" || error.code === "DIFF_PREFIX_FREEZE"),
  record_count: difficulty.length,
  unique_record_count: difficultyIds.size,
  latest_record_id: difficulty.at(-1)?.record_id || null,
  state_counts: countBy(difficulty, "state"),
  append_only_prefix: {
    bytes: freeze.prefix_through_scope.difficulty_jsonl.bytes,
    sha256: freeze.prefix_through_scope.difficulty_jsonl.sha256,
    verified: !categories.difficulty.some((error) => error.code === "DIFF_PREFIX_FREEZE")
  },
  jsonl: { bytes: difficultyInfo.bytes, sha256: difficultyInfo.sha256 },
  csv: { data_rows: csvRows(difficultyCsvPath), bytes: difficultyCsvInfo.bytes, sha256: difficultyCsvInfo.sha256 },
  errors: categories.difficulty,
  continuation_cursor: "Append after CJK-KO-P06-HARD-038; never rewrite resolved failures.",
  scope_note: "Resolved failures remain evidence; held and active-control records remain checker debt."
};
const visualReport = {
  schema: path.basename(visualSchemaPath),
  schema_sha256: fileInfo(visualSchemaPath).sha256,
  validator: "../validate.mjs",
  validator_sha256: validatorInfo.sha256,
  status: categories.visual.length === 0 ? "PASS" : "FAIL",
  scope: "Noether Paper 6 Korean T01--T16 U01--U228 producer visual inventory",
  record_count: visual.length,
  image_file_count: visualFiles.length,
  render_call_count: 0,
  type_counts: {
    source_page: 0,
    source_crop: 0,
    equation_crop: 0,
    diagram_crop: 0,
    target_render: 0,
    contact_sheet: 0,
    before_after: 0,
    segmentation_artifact: 0,
    model_overlay: 0
  },
  rights_disposition_totals: {
    public_safe: 0,
    rights_blocked: 0,
    private_excluded: 0,
    pending: 0
  },
  total_image_bytes: 0,
  jsonl: { bytes: visualInfo.bytes, sha256: visualInfo.sha256 },
  csv: { data_rows: csvRows(visualCsvPath), bytes: visualCsvInfo.bytes, sha256: visualCsvInfo.sha256 },
  errors: categories.visual,
  continuation_cursor: "No producer visual evidence exists; rendering and visual QA remain downstream gates.",
  scope_note: "Explicit zero inventory proves no image use or creation; it is not visual QA."
};
fs.writeFileSync(path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json"), JSON.stringify(structuralReport, null, 2) + "\n", "utf8");
fs.writeFileSync(path.join(difficultyDir, "DIFFICULTY_LEDGER_VALIDATION_REPORT.json"), JSON.stringify(difficultyReport, null, 2) + "\n", "utf8");
fs.writeFileSync(path.join(visualDir, "VISUAL_EVIDENCE_INDEX_VALIDATION_REPORT.json"), JSON.stringify(visualReport, null, 2) + "\n", "utf8");

const allErrors = Object.values(categories).flat();
const overall = {
  validator: "validate.mjs",
  validator_sha256: validatorInfo.sha256,
  status: allErrors.length === 0 ? "PASS" : "FAIL",
  scope: "Noether Paper 6 Korean complete producer-draft custody and evidence",
  manifest: { bytes: manifestInfo.bytes, sha256: manifestInfo.sha256, csv_bytes: manifestCsvInfo.bytes, csv_sha256: manifestCsvInfo.sha256 },
  target_count: manifest.target_count,
  target_bytes: manifest.target_bytes,
  target_tree_sha256: manifest.target_tree_sha256,
  source_content_sha256: manifest.source_content_sha256,
  structural: { records: structural.length, status: structuralReport.status },
  difficulty: { records: difficulty.length, latest_id: difficulty.at(-1)?.record_id || null, status: difficultyReport.status },
  visual: { records: visual.length, status: visualReport.status },
  state: {
    producer_text_coverage: "complete",
    review: "unchecked",
    assembly: "not_assembled",
    compilation: "not_built",
    rendering: "not_rendered",
    visual_qa: "not_performed",
    certification: "not_certified"
  },
  errors: allErrors
};
fs.writeFileSync(path.join(here, "P06_VALIDATION.json"), JSON.stringify(overall, null, 2) + "\n", "utf8");
console.log(JSON.stringify(overall, null, 2));
if (allErrors.length) process.exitCode = 1;
