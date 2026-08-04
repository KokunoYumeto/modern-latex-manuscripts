import fs from "node:fs/promises";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const scriptPath = fileURLToPath(import.meta.url);
const evidenceRoot = path.dirname(scriptPath);
const projectRoot = path.dirname(evidenceRoot);
const workspaceRoot = path.resolve(projectRoot, "../../../../..");
const authorityPath = path.join(
  workspaceRoot,
  "03_projects",
  "noether",
  "07_german_canon_control",
  "candidates",
  "NOETH-DE-ED-0001",
  "Noether_German_NOETH-DE-ED-0001.tex",
);

const WORK_ID = "NOE-P04-KO";
const SCHEMA_VERSION = "1.0.0";
const CURSOR = "NOE-P04-KO:SOURCE_LINE_3889:T04_OUT_OF_SCOPE";
const AUTHORITY_SHA256 = "D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB";
const AUTHORITY_BYTES = 2153565;
const POINTERS = {
  T01: {
    id: "NOETH-DE-AUTH-v003-20260804",
    sha256: "932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197",
  },
  T02: {
    id: "NOETH-DE-AUTH-v003-20260804",
    sha256: "932FEDC1735A41A9CF71D15A6C662A468A4CAD016AE8B3DECDF9A71E8BA7F197",
  },
  T03: {
    id: "NOETH-DE-AUTH-v004-20260804",
    sha256: "A1C62FDACAA34DFC1B806DC18258F2E732539F7AE9D85AA4BD9E1067B8749D9F",
  },
};

const units = [
  ["T01", "U01", 3611, 3640, "9A1B0B21FD34C151E7A8B8605B67CE37DEB1F47E8B00C26282F879335FF88591", "Noether_P04_Korean_T01_U01_UNCHECKED.tex", "64297D37AC0E60F2E622A3231BA5B59846A1D00CB40A95D865B864DC9A30D2F1"],
  ["T01", "U02", 3641, 3663, "17D0597F650652261229E4B348222ED9E1C0BF504D4BCB893B0B7D341266DC4C", "Noether_P04_Korean_T01_U02_UNCHECKED.tex", "2728D4B1AA51C0CE3BCAC45D274BFD9B9ACB2F96DA4AFF2518F1CD202A287CC5"],
  ["T01", "U03", 3665, 3690, "9DE0FAFE8FD5B502B6DD753C9C04763C9611C92469685F90DE97D50AD7F9E0C3", "Noether_P04_Korean_T01_U03_UNCHECKED.tex", "778BA22BFDE7F0C7A66F1CC6B0FB1A64B3B864F81BEE4AB78CF6B9735B14A733"],
  ["T01", "U04", 3692, 3693, "858ACC0D85168C12807B9AAAE7055A24C7F6A2C3D0416C2448AD2A19D094ABDF", "Noether_P04_Korean_T01_U04_UNCHECKED.tex", "578FFBC95675FDD5AA822287833EA3CBBDB53752FC8FEAAE85F7B156578F1F59"],
  ["T02", "U05", 3694, 3699, "DA495CE3383746D7568D2B7BC347E99E54D26077CC17BF4E6AB773FFF39D8B46", "Noether_P04_Korean_T02_U05_UNCHECKED.tex", "32224493EE78CF4B206732EBCAD5BABCB6D9F2981D52BAFDB6C09878ADE53C06"],
  ["T02", "U06", 3701, 3740, "4FB079CD8A6F2CF6EF2E68EC8662EBA5811F5C8EFD1CB6D7332354FD39609D41", "Noether_P04_Korean_T02_U06_UNCHECKED.tex", "8EFCEE86349CBB92A6BAF9A5A607E516F2EADF26FC5A82462E0F8FE78BBD574A"],
  ["T02", "U07", 3742, 3762, "7FED052F4864855B35B3AD558D6796FFD63511AE7A9648BC3D0765A9681756BD", "Noether_P04_Korean_T02_U07_UNCHECKED.tex", "8F03D5DA8AC825B5F180049C1AC9CB01DB52EE7507F2FAE60471744ADF544A7B"],
  ["T02", "U08", 3764, 3776, "006170FB340029EE4BAFC75010015F316571D683FE675E052B93AA65B5C3CF5C", "Noether_P04_Korean_T02_U08_UNCHECKED.tex", "89DDC2F775CD86A216346C080B45E81527B60C1A8F115F107842D477F1E8D857"],
  ["T02", "U09", 3778, 3779, "BC4ADE28185FB8095D49DAD69330E9DEA4F5343D612C8FAFBB9B00D53DE14F7C", "Noether_P04_Korean_T02_U09_UNCHECKED.tex", "5A940A5CECFD77AE33FCA9C2E3A713653D682886E9F5CD0FD66605DCD75B82E3"],
  ["T03", "U10", 3780, 3787, "39F6BBAC7FA2466F8D86F5EBDE759CEBA517AA29F4D26F88386293625AFBC6CA", "Noether_P04_Korean_T03_U10_UNCHECKED.tex", "66A5859EB5CA1C73D64E5116E720AF229CB26C70B0E060C3A94FB06A897E7E83"],
  ["T03", "U11", 3788, 3808, "382D7CDEB760F768B7505D0F0F6F243E332D637A3BB65D2639F55C4E9612369D", "Noether_P04_Korean_T03_U11_UNCHECKED.tex", "51533E6489F05B23B78B65A46C4AE131D6412680B6236D9F091421B4335CB67F"],
  ["T03", "U12", 3809, 3816, "6FE853A1694FD0026D946190F2963396F11F05C1896DF1DCC46B6D244F27D132", "Noether_P04_Korean_T03_U12_UNCHECKED.tex", "AC6CD6F491B3EBAF83595B8BF7EDA17414679AF2E2D16B02CA1EFC59FC7589BA"],
  ["T03", "U13", 3817, 3837, "D52919AB904AC5D2DBF1E290722536B5763A95E0015ACC7561EA18838BDBCD96", "Noether_P04_Korean_T03_U13_UNCHECKED.tex", "953C46165395C344F8E1455994DE8956B13C427C790275B1C47E770BA5E6CE13"],
  ["T03", "U14", 3838, 3854, "5FA766647DAD9D1534CADB60A9BE68077244731D934B284B79DA6047E725AA0E", "Noether_P04_Korean_T03_U14_UNCHECKED.tex", "F75C627C976334B74AC31BBC4C4E7DA5D7FFED9EE3F82F764177B3552DFCE508"],
  ["T03", "U15", 3855, 3863, "05317AA1D91110F8C31FCD6201A430C8C899B14D87990A966C4A77CC40EE7217", "Noether_P04_Korean_T03_U15_UNCHECKED.tex", "5039271D12EE05A91F907A02C0A43E0F1CAD07FCA54F8A868186422727DF5F94"],
  ["T03", "U16", 3865, 3886, "7860EA7EA30526C7F93C223463B78E6054C9A28F7C7F926A9E4C37CAD9A2AC19", "Noether_P04_Korean_T03_U16_UNCHECKED.tex", "9D63C88E326907CE38D0AE4A7C3970FF3DD57EE7D3565C1733E34BBCE5103993"],
].map(function (row) {
  return {
    tranche: row[0],
    unit: row[1],
    sourceStart: row[2],
    sourceEnd: row[3],
    sourceSliceSha256: row[4],
    targetName: row[5],
    targetSha256: row[6],
    targetPath: path.join(projectRoot, "targets", row[5]),
  };
});

const trancheBounds = {
  T01: [3611, 3693, "2B20BBF39AC47AA2A44D7E5885A427C98A6926522F9B84A2AEE435B29C2CD3EA"],
  T02: [3694, 3779, "B9E91228B887000E3FDCE77A0F276FDF9081184C637C5810B670B2E3583567EC"],
  T03: [3780, 3886, "4C30142788A63C18357AABB367FFCF8ABF092DF225EAB79BEDB30EF8A1EC40C9"],
};

function sha256(value) {
  return crypto.createHash("sha256").update(value).digest("hex").toUpperCase();
}

function stableValue(value) {
  if (Array.isArray(value)) {
    return value.map(stableValue);
  }
  if (value && typeof value === "object") {
    const out = {};
    for (const key of Object.keys(value).sort()) {
      out[key] = stableValue(value[key]);
    }
    return out;
  }
  return value;
}

function canonical(value) {
  return JSON.stringify(stableValue(value));
}

function withoutKey(value, key) {
  const out = {};
  for (const current of Object.keys(value)) {
    if (current !== key && !current.startsWith("_")) {
      out[current] = value[current];
    }
  }
  return out;
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function normalizeLf(text) {
  return text.replace(/\r\n/g, "\n").replace(/\r/g, "\n");
}

function csvEscape(value) {
  if (value === null || value === undefined) {
    return "";
  }
  const text = String(value);
  if (/[",\r\n]/.test(text)) {
    return '"' + text.replace(/"/g, '""') + '"';
  }
  return text;
}

function toCsv(headers, rows) {
  const lines = [headers.map(csvEscape).join(",")];
  for (const row of rows) {
    lines.push(headers.map(function (header) { return csvEscape(row[header]); }).join(","));
  }
  return lines.join("\n") + "\n";
}

function parseCsv(text) {
  const rows = [];
  let row = [];
  let field = "";
  let quoted = false;
  for (let i = 0; i < text.length; i += 1) {
    const ch = text[i];
    if (quoted) {
      if (ch === '"' && text[i + 1] === '"') {
        field += '"';
        i += 1;
      } else if (ch === '"') {
        quoted = false;
      } else {
        field += ch;
      }
    } else if (ch === '"') {
      quoted = true;
    } else if (ch === ",") {
      row.push(field);
      field = "";
    } else if (ch === "\n") {
      row.push(field);
      rows.push(row);
      row = [];
      field = "";
    } else if (ch !== "\r") {
      field += ch;
    }
  }
  if (field.length > 0 || row.length > 0) {
    row.push(field);
    rows.push(row);
  }
  return rows;
}

async function readTextFile(fullPath) {
  const bytes = await fs.readFile(fullPath);
  const text = normalizeLf(bytes.toString("utf8"));
  const trailingLf = text.endsWith("\n");
  const lines = text.split("\n");
  if (trailingLf) {
    lines.pop();
  }
  return {
    fullPath: fullPath,
    bytes: bytes,
    fileSha256: sha256(bytes),
    text: text,
    lines: lines,
    trailingLf: trailingLf,
  };
}

function lineSlice(file, start, end) {
  assert(start >= 1 && end >= start && end <= file.lines.length, "Invalid line slice " + start + "--" + end + " for " + file.fullPath);
  return file.lines.slice(start - 1, end).join("\n") + "\n";
}

function relPath(fullPath) {
  return path.relative(workspaceRoot, fullPath).replace(/\\/g, "/");
}

async function writeJson(fullPath, value) {
  await fs.mkdir(path.dirname(fullPath), { recursive: true });
  await fs.writeFile(fullPath, JSON.stringify(value, null, 2) + "\n", "utf8");
}

async function writeText(fullPath, text) {
  await fs.mkdir(path.dirname(fullPath), { recursive: true });
  await fs.writeFile(fullPath, text, "utf8");
}

async function fileIdentity(fullPath) {
  const bytes = await fs.readFile(fullPath);
  return { bytes: bytes.length, sha256: sha256(bytes) };
}

const authority = await readTextFile(authorityPath);
assert(authority.bytes.length === AUTHORITY_BYTES, "Authority byte count changed");
assert(authority.fileSha256 === AUTHORITY_SHA256, "Authority SHA-256 changed");

for (const unit of units) {
  unit.pointer = POINTERS[unit.tranche];
  unit.target = await readTextFile(unit.targetPath);
  assert(unit.target.fileSha256 === unit.targetSha256, "Target SHA-256 changed for " + unit.unit);
  const sourceSlice = lineSlice(authority, unit.sourceStart, unit.sourceEnd);
  assert(sha256(Buffer.from(sourceSlice, "utf8")) === unit.sourceSliceSha256, "Source slice SHA-256 changed for " + unit.unit);
}

for (const tranche of Object.keys(trancheBounds)) {
  const bounds = trancheBounds[tranche];
  const trancheSlice = lineSlice(authority, bounds[0], bounds[1]);
  assert(sha256(Buffer.from(trancheSlice, "utf8")) === bounds[2], "Tranche SHA-256 changed for " + tranche);
}
const continuousSlice = lineSlice(authority, 3611, 3886);
assert(Buffer.byteLength(continuousSlice, "utf8") === 37326, "Continuous source slice byte count changed");
assert(sha256(Buffer.from(continuousSlice, "utf8")) === "202395559B333C546F4BFD562DD1233DA02FE1A07C948BEEDA23DE62559F781A", "Continuous source slice SHA-256 changed");

function locator(unit, side, start, end, fragment) {
  const file = side === "source" ? authority : unit.target;
  const slice = lineSlice(file, start, end);
  return {
    side: side,
    language: side === "source" ? "de" : "ko-KR",
    path_workspace_relative: relPath(file.fullPath),
    line_basis: side === "source" ? "whole_authority" : "target_file",
    line_start: start,
    line_end: end,
    file_bytes: file.bytes.length,
    file_sha256: file.fileSha256,
    slice_utf8_bytes_lf: Buffer.byteLength(slice, "utf8"),
    slice_sha256_lf: sha256(Buffer.from(slice, "utf8")),
    fragment_kind: fragment ? fragment.kind : null,
    fragment_ordinal: fragment ? fragment.ordinal : null,
    fragment_text: fragment ? fragment.text : null,
    fragment_sha256_utf8: fragment ? sha256(Buffer.from(fragment.text, "utf8")) : null,
    authority_pointer_id: unit.pointer.id,
    authority_pointer_sha256: unit.pointer.sha256,
  };
}

const records = [];
const byId = new Map();
const idCounters = new Map();
const siblingCounters = new Map();
let globalOrder = 0;

function nextRecordId(spec) {
  if (spec.recordId) {
    return spec.recordId;
  }
  const sideToken = spec.side === "source" ? "SRC" : spec.side === "target" ? "TGT" : "AGG";
  const typeToken = spec.structureType.toUpperCase().replace(/_/g, "-");
  const key = [spec.trancheId, spec.unitId, sideToken, typeToken].join("|");
  const next = (idCounters.get(key) || 0) + 1;
  idCounters.set(key, next);
  return [
    "NOE-P04-KO",
    spec.trancheId,
    spec.unitId,
    sideToken,
    typeToken,
    String(next).padStart(3, "0"),
  ].filter(function (value) { return value !== null && value !== undefined && value !== "ALL"; }).join("-");
}

function addRecord(spec) {
  const recordId = nextRecordId(spec);
  assert(!byId.has(recordId), "Duplicate record ID " + recordId);
  const parent = spec.parentId ? byId.get(spec.parentId) : null;
  assert(!spec.parentId || parent, "Parent must precede child for " + recordId);
  const siblingKey = spec.parentId || "__ROOT__";
  const siblingOrder = (siblingCounters.get(siblingKey) || 0) + 1;
  siblingCounters.set(siblingKey, siblingOrder);
  globalOrder += 1;
  const record = {
    schema_version: SCHEMA_VERSION,
    record_id: recordId,
    work_id: WORK_ID,
    tranche_id: spec.trancheId || "ALL",
    unit_id: spec.unitId || "ALL",
    side: spec.side,
    language: spec.language,
    structure_type: spec.structureType,
    label: spec.label,
    parent_id: spec.parentId || null,
    order: globalOrder,
    sibling_order: siblingOrder,
    depth: parent ? parent.depth + 1 : 0,
    coverage_role: spec.coverageRole,
    record_basis: spec.recordBasis || ["computation"],
    locators: spec.locators,
    crossrefs: [],
    completion_state: spec.completionState || (spec.side === "target" ? "producer_draft_text_indexed" : spec.side === "source" ? "authority_slice_indexed" : "scope_frozen_t01_t03"),
    review_state: "unchecked",
    formula_review_state: "not_performed",
    publication_state: "private_not_for_publication",
    continuation_cursor: CURSOR,
    _text: spec.text || "",
    _equation_tag: spec.equationTag || null,
    _section_number: spec.sectionNumber || null,
  };
  records.push(record);
  byId.set(recordId, record);
  return record;
}

function aggregateLocators(scopeUnits) {
  const out = [];
  for (const unit of scopeUnits) {
    out.push(locator(unit, "source", unit.sourceStart, unit.sourceEnd));
    out.push(locator(unit, "target", 1, unit.target.lines.length));
  }
  return out;
}

const workRecord = addRecord({
  recordId: "NOE-P04-KO-WORK-001",
  trancheId: "ALL",
  unitId: "ALL",
  side: "aggregate",
  language: "mul",
  structureType: "work",
  label: "Noether Paper 4 Korean producer evidence freeze T01--T03",
  coverageRole: "container",
  locators: aggregateLocators(units),
});

const trancheRecords = new Map();
const unitRecords = new Map();
const documentRecords = new Map();

function documentKey(unitId, side) {
  return unitId + "|" + side;
}

function lineEntries(unit, side) {
  if (side === "source") {
    const entries = [];
    for (let line = unit.sourceStart; line <= unit.sourceEnd; line += 1) {
      entries.push({ number: line, text: authority.lines[line - 1] });
    }
    return entries;
  }
  return unit.target.lines.map(function (text, index) {
    return { number: index + 1, text: text };
  });
}

function findEnvironmentEnd(entries, startIndex, envName) {
  const endToken = "\\end{" + envName + "}";
  for (let index = startIndex + 1; index < entries.length; index += 1) {
    if (entries[index].text.includes(endToken)) {
      return index;
    }
  }
  throw new Error("Unclosed environment " + envName + " at line " + entries[startIndex].number);
}

function findDisplayEnd(entries, startIndex) {
  const startText = entries[startIndex].text;
  if (/^\s*\\\[\s*$/.test(startText)) {
    for (let index = startIndex + 1; index < entries.length; index += 1) {
      if (/^\s*\\\]\s*$/.test(entries[index].text)) {
        return { endIndex: index, environment: "bracket_display" };
      }
    }
    throw new Error("Unclosed bracket display at line " + entries[startIndex].number);
  }
  const match = startText.match(/^\s*\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}/);
  if (match) {
    return { endIndex: findEnvironmentEnd(entries, startIndex, match[1]), environment: match[1] };
  }
  return null;
}

function isSection(text) {
  return /^\s*\\(?:sub)*section\*?\{/.test(text);
}

function sectionNumber(text) {
  const match = text.match(/\\S\\?\s*(\d+)/);
  return match ? match[1] : null;
}

function isTheorem(text, side) {
  if (side === "source") {
    return /^\s*(?:\\emph\{)?(?:Satz|Theorem)\s+[IVXLC]+[.:}]/i.test(text)
      || /^\s*(?:\\emph\{)?[IVXLC]+[.:]\s*(?:Satz|Theorem)\b/i.test(text);
  }
  return /^\s*(?:\\emph\{)?정리\s*[IVXLC]+[.:}]/u.test(text)
    || /^\s*(?:\\emph\{)?[IVXLC]+[.:]\s*정리\b/u.test(text);
}

function isProof(text, side) {
  if (side === "source") {
    return /^\s*(?:\\emph\{)?Beweis\b/i.test(text);
  }
  return /^\s*(?:\\emph\{)?증명\b/u.test(text);
}

function isStandaloneBibliography(text) {
  return /^\s*\\bibitem\b/.test(text);
}

function isStructuralStart(entries, index, side) {
  const text = entries[index].text;
  return text.trim() === ""
    || /^\s*%/.test(text)
    || /^\s*\\begin\{center\}/.test(text)
    || Boolean(findDisplayEndSafe(entries, index))
    || isSection(text)
    || isTheorem(text, side)
    || isProof(text, side)
    || isStandaloneBibliography(text);
}

function findDisplayEndSafe(entries, index) {
  const text = entries[index].text;
  if (/^\s*\\\[\s*$/.test(text)) {
    return true;
  }
  return /^\s*\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}/.test(text);
}

function extractBalancedMacro(line, macroStart, startIndex) {
  const braceIndex = line.indexOf("{", startIndex + macroStart.length);
  if (braceIndex < 0) {
    return { text: macroStart, endIndex: startIndex + macroStart.length };
  }
  let depth = 0;
  for (let index = braceIndex; index < line.length; index += 1) {
    if (line[index] === "{" && line[index - 1] !== "\\") {
      depth += 1;
    } else if (line[index] === "}" && line[index - 1] !== "\\") {
      depth -= 1;
      if (depth === 0) {
        return { text: line.slice(startIndex, index + 1), endIndex: index + 1 };
      }
    }
  }
  return { text: line.slice(startIndex), endIndex: line.length };
}

function extractFootnoteMacros(line) {
  const out = [];
  const regex = /\\footnotetext\s*\{|\\footnotemark\b|\\footnote\s*\{/g;
  let match;
  while ((match = regex.exec(line)) !== null) {
    const macroName = match[0].startsWith("\\footnotetext")
      ? "\\footnotetext"
      : match[0].startsWith("\\footnotemark")
        ? "\\footnotemark"
        : "\\footnote";
    if (macroName === "\\footnotemark") {
      out.push({ kind: "footnotemark", text: "\\footnotemark", index: match.index });
      regex.lastIndex = match.index + "\\footnotemark".length;
    } else {
      const balanced = extractBalancedMacro(line, macroName, match.index);
      out.push({ kind: macroName.slice(1), text: balanced.text, index: match.index });
      regex.lastIndex = balanced.endIndex;
    }
  }
  return out;
}

function isBibliographicFootnote(text) {
  return /(?:Math\.|Ann\.|Journal|Crelle|Zeitschrift|Göttinger|Sitzungsberichte|Werke|Bd\.|S\.\s*\d|18\d{2}|19\d{2}|a\.\s*a\.\s*O\.|Capelli|Study|Pascal|Gra(?:ß|ss)mann|Wellstein|Gordan|Hilbert|Clebsch|Weitzenböck)/i.test(text);
}

function annotateFootnotes(parentRecord, unit, side, entries) {
  let unitOrdinal = 0;
  for (const entry of entries) {
    const macros = extractFootnoteMacros(entry.text);
    let lineOrdinal = 0;
    for (const macro of macros) {
      unitOrdinal += 1;
      lineOrdinal += 1;
      const type = macro.kind === "footnotemark" ? "footnote_marker" : "footnote";
      const note = addRecord({
        trancheId: unit.tranche,
        unitId: unit.unit,
        side: side,
        language: side === "source" ? "de" : "ko-KR",
        structureType: type,
        label: type.replace(/_/g, " ") + " occurrence " + unitOrdinal + " in " + unit.unit + " " + side,
        parentId: parentRecord.record_id,
        coverageRole: "annotation",
        recordBasis: side === "source" ? ["source_fact", "computation"] : ["target_fact", "computation"],
        locators: [locator(unit, side, entry.number, entry.number, {
          kind: macro.kind,
          ordinal: lineOrdinal,
          text: macro.text,
        })],
        text: macro.text,
      });
      if (type === "footnote" && isBibliographicFootnote(macro.text)) {
        const bibliography = addRecord({
          trancheId: unit.tranche,
          unitId: unit.unit,
          side: side,
          language: side === "source" ? "de" : "ko-KR",
          structureType: "bibliographic_item",
          label: "bibliographic footnote item " + unitOrdinal + " in " + unit.unit + " " + side,
          parentId: note.record_id,
          coverageRole: "annotation",
          recordBasis: side === "source" ? ["source_fact", "computation"] : ["target_fact", "computation"],
          locators: [locator(unit, side, entry.number, entry.number, {
            kind: "bibliographic_footnote",
            ordinal: lineOrdinal,
            text: macro.text,
          })],
          text: macro.text,
        });
        note.crossrefs.push({
          kind: "contains_bibliographic_item",
          label: bibliography.label,
          target_record_id: bibliography.record_id,
          resolution_state: "resolved",
          basis: "macro_content_classification_unchecked",
        });
      }
    }
  }
}

function addEquationChildren(parentRecord, unit, side, entries, outerType) {
  const tags = [];
  for (const entry of entries) {
    const regex = /\\tag\{([^}]+)\}/g;
    let match;
    let ordinal = 0;
    while ((match = regex.exec(entry.text)) !== null) {
      ordinal += 1;
      tags.push({ tag: match[1], entry: entry, ordinal: ordinal, text: match[0] });
    }
  }
  if (outerType === "equation" && tags.length === 1) {
    parentRecord._equation_tag = tags[0].tag;
    parentRecord.label = "equation (" + tags[0].tag + ")";
    return;
  }
  for (const tag of tags) {
    addRecord({
      trancheId: unit.tranche,
      unitId: unit.unit,
      side: side,
      language: side === "source" ? "de" : "ko-KR",
      structureType: "equation",
      label: "equation (" + tag.tag + ")",
      parentId: parentRecord.record_id,
      coverageRole: "annotation",
      recordBasis: side === "source" ? ["source_fact", "computation"] : ["target_fact", "computation"],
      locators: [locator(unit, side, tag.entry.number, tag.entry.number, {
        kind: "tag_macro",
        ordinal: tag.ordinal,
        text: tag.text,
      })],
      text: tag.entry.text,
      equationTag: tag.tag,
    });
  }
}

function parseDocument(unit, side, documentId) {
  const entries = lineEntries(unit, side);
  let index = 0;
  let centerOrdinal = 0;
  while (index < entries.length) {
    const entry = entries[index];
    const text = entry.text;
    if (text.trim() === "") {
      let endIndex = index;
      while (endIndex + 1 < entries.length && entries[endIndex + 1].text.trim() === "") {
        endIndex += 1;
      }
      addRecord({
        trancheId: unit.tranche,
        unitId: unit.unit,
        side: side,
        language: side === "source" ? "de" : "ko-KR",
        structureType: "blank_separator",
        label: "blank separator " + entry.number + (endIndex > index ? "--" + entries[endIndex].number : ""),
        parentId: documentId,
        coverageRole: "primary",
        recordBasis: ["computation"],
        locators: [locator(unit, side, entry.number, entries[endIndex].number)],
        text: entries.slice(index, endIndex + 1).map(function (item) { return item.text; }).join("\n"),
      });
      index = endIndex + 1;
      continue;
    }
    if (/^\s*%/.test(text)) {
      let endIndex = index;
      while (endIndex + 1 < entries.length && /^\s*%/.test(entries[endIndex + 1].text)) {
        endIndex += 1;
      }
      const blockEntries = entries.slice(index, endIndex + 1);
      addRecord({
        trancheId: unit.tranche,
        unitId: unit.unit,
        side: side,
        language: side === "source" ? "de" : "ko-KR",
        structureType: "metadata_header",
        label: "producer metadata comment header",
        parentId: documentId,
        coverageRole: "primary",
        recordBasis: side === "target" ? ["target_fact", "computation"] : ["source_fact", "computation"],
        locators: [locator(unit, side, entry.number, entries[endIndex].number)],
        text: blockEntries.map(function (item) { return item.text; }).join("\n"),
      });
      index = endIndex + 1;
      continue;
    }
    if (/^\s*\\begin\{center\}/.test(text)) {
      const endIndex = findEnvironmentEnd(entries, index, "center");
      centerOrdinal += 1;
      const blockEntries = entries.slice(index, endIndex + 1);
      const blockType = unit.unit === "U01" && centerOrdinal === 1
        ? "title_block"
        : unit.unit === "U01" && centerOrdinal === 2
          ? "publication_note"
          : "center_block";
      const block = addRecord({
        trancheId: unit.tranche,
        unitId: unit.unit,
        side: side,
        language: side === "source" ? "de" : "ko-KR",
        structureType: blockType,
        label: blockType.replace(/_/g, " "),
        parentId: documentId,
        coverageRole: "primary",
        recordBasis: side === "source" ? ["source_fact", "computation"] : ["target_fact", "computation"],
        locators: [locator(unit, side, entry.number, entries[endIndex].number)],
        text: blockEntries.map(function (item) { return item.text; }).join("\n"),
      });
      const authorEntry = blockEntries.find(function (item) { return /Noether|뇌터|노에터/iu.test(item.text); });
      if (authorEntry) {
        addRecord({
          trancheId: unit.tranche,
          unitId: unit.unit,
          side: side,
          language: side === "source" ? "de" : "ko-KR",
          structureType: "author",
          label: "author line",
          parentId: block.record_id,
          coverageRole: "annotation",
          recordBasis: side === "source" ? ["source_fact", "computation"] : ["target_fact", "computation"],
          locators: [locator(unit, side, authorEntry.number, authorEntry.number)],
          text: authorEntry.text,
        });
      }
      annotateFootnotes(block, unit, side, blockEntries);
      index = endIndex + 1;
      continue;
    }
    const display = findDisplayEnd(entries, index);
    if (display) {
      const blockEntries = entries.slice(index, display.endIndex + 1);
      const outerType = /^equation/.test(display.environment) ? "equation" : "display_math";
      const block = addRecord({
        trancheId: unit.tranche,
        unitId: unit.unit,
        side: side,
        language: side === "source" ? "de" : "ko-KR",
        structureType: outerType,
        label: display.environment.replace(/_/g, " ") + " display",
        parentId: documentId,
        coverageRole: "primary",
        recordBasis: side === "source" ? ["source_fact", "computation"] : ["target_fact", "computation"],
        locators: [locator(unit, side, entry.number, entries[display.endIndex].number)],
        text: blockEntries.map(function (item) { return item.text; }).join("\n"),
      });
      addEquationChildren(block, unit, side, blockEntries, outerType);
      annotateFootnotes(block, unit, side, blockEntries);
      index = display.endIndex + 1;
      continue;
    }
    if (isSection(text)) {
      const number = sectionNumber(text);
      const section = addRecord({
        trancheId: unit.tranche,
        unitId: unit.unit,
        side: side,
        language: side === "source" ? "de" : "ko-KR",
        structureType: "section_heading",
        label: number ? "section " + number : "section heading",
        parentId: documentId,
        coverageRole: "primary",
        recordBasis: side === "source" ? ["source_fact", "computation"] : ["target_fact", "computation"],
        locators: [locator(unit, side, entry.number, entry.number)],
        text: text,
        sectionNumber: number,
      });
      annotateFootnotes(section, unit, side, [entry]);
      index += 1;
      continue;
    }
    if (isTheorem(text, side) || isProof(text, side) || isStandaloneBibliography(text)) {
      const blockType = isTheorem(text, side) ? "theorem_statement" : isProof(text, side) ? "proof" : "bibliographic_item";
      const block = addRecord({
        trancheId: unit.tranche,
        unitId: unit.unit,
        side: side,
        language: side === "source" ? "de" : "ko-KR",
        structureType: blockType,
        label: blockType.replace(/_/g, " "),
        parentId: documentId,
        coverageRole: "primary",
        recordBasis: side === "source" ? ["source_fact", "computation"] : ["target_fact", "computation"],
        locators: [locator(unit, side, entry.number, entry.number)],
        text: text,
      });
      annotateFootnotes(block, unit, side, [entry]);
      index += 1;
      continue;
    }
    let endIndex = index;
    while (endIndex + 1 < entries.length && !isStructuralStart(entries, endIndex + 1, side)) {
      endIndex += 1;
    }
    const blockEntries = entries.slice(index, endIndex + 1);
    const paragraph = addRecord({
      trancheId: unit.tranche,
      unitId: unit.unit,
      side: side,
      language: side === "source" ? "de" : "ko-KR",
      structureType: "paragraph",
      label: "maximal top-level prose paragraph",
      parentId: documentId,
      coverageRole: "primary",
      recordBasis: side === "source" ? ["source_fact", "computation", "producer_editorial_inference"] : ["target_fact", "computation", "producer_editorial_inference"],
      locators: [locator(unit, side, entry.number, entries[endIndex].number)],
      text: blockEntries.map(function (item) { return item.text; }).join("\n"),
    });
    annotateFootnotes(paragraph, unit, side, blockEntries);
    index = endIndex + 1;
  }
}

for (const tranche of ["T01", "T02", "T03"]) {
  const trancheUnits = units.filter(function (unit) { return unit.tranche === tranche; });
  const trancheRecord = addRecord({
    recordId: "NOE-P04-KO-" + tranche + "-TRANCHE-001",
    trancheId: tranche,
    unitId: "ALL",
    side: "aggregate",
    language: "mul",
    structureType: "tranche",
    label: tranche + " structural evidence scope",
    parentId: workRecord.record_id,
    coverageRole: "container",
    locators: aggregateLocators(trancheUnits),
  });
  trancheRecords.set(tranche, trancheRecord);
  for (const unit of trancheUnits) {
    const unitRecord = addRecord({
      recordId: "NOE-P04-KO-" + tranche + "-" + unit.unit + "-UNIT-001",
      trancheId: tranche,
      unitId: unit.unit,
      side: "aggregate",
      language: "mul",
      structureType: "unit",
      label: tranche + "-" + unit.unit + " source/target unit",
      parentId: trancheRecord.record_id,
      coverageRole: "container",
      locators: [
        locator(unit, "source", unit.sourceStart, unit.sourceEnd),
        locator(unit, "target", 1, unit.target.lines.length),
      ],
    });
    unitRecords.set(unit.unit, unitRecord);
    const sourceDocument = addRecord({
      recordId: "NOE-P04-KO-" + tranche + "-" + unit.unit + "-SRC-DOCUMENT-001",
      trancheId: tranche,
      unitId: unit.unit,
      side: "source",
      language: "de",
      structureType: "source_document",
      label: unit.unit + " German authority slice",
      parentId: unitRecord.record_id,
      coverageRole: "container",
      recordBasis: ["source_fact", "computation"],
      locators: [locator(unit, "source", unit.sourceStart, unit.sourceEnd)],
    });
    documentRecords.set(documentKey(unit.unit, "source"), sourceDocument);
    parseDocument(unit, "source", sourceDocument.record_id);
    const targetDocument = addRecord({
      recordId: "NOE-P04-KO-" + tranche + "-" + unit.unit + "-TGT-DOCUMENT-001",
      trancheId: tranche,
      unitId: unit.unit,
      side: "target",
      language: "ko-KR",
      structureType: "target_document",
      label: unit.unit + " Korean producer target",
      parentId: unitRecord.record_id,
      coverageRole: "container",
      recordBasis: ["target_fact", "computation"],
      locators: [locator(unit, "target", 1, unit.target.lines.length)],
    });
    documentRecords.set(documentKey(unit.unit, "target"), targetDocument);
    parseDocument(unit, "target", targetDocument.record_id);
  }
}

function addCrossref(record, crossref) {
  const key = [crossref.kind, crossref.label, crossref.target_record_id || ""].join("|");
  if (!record.crossrefs.some(function (existing) {
    return [existing.kind, existing.label, existing.target_record_id || ""].join("|") === key;
  })) {
    record.crossrefs.push(crossref);
  }
}

for (const unit of units) {
  const sourceDoc = documentRecords.get(documentKey(unit.unit, "source"));
  const targetDoc = documentRecords.get(documentKey(unit.unit, "target"));
  addCrossref(sourceDoc, {
    kind: "parallel_document",
    label: unit.unit + " target document",
    target_record_id: targetDoc.record_id,
    resolution_state: "resolved",
    basis: "unit_identity_only_unchecked",
  });
  addCrossref(targetDoc, {
    kind: "parallel_document",
    label: unit.unit + " source document",
    target_record_id: sourceDoc.record_id,
    resolution_state: "resolved",
    basis: "unit_identity_only_unchecked",
  });
}

const equationMap = new Map();
const sectionMap = new Map();
for (const record of records) {
  if (record._equation_tag) {
    equationMap.set(record.side + "|" + record._equation_tag, record);
  }
  if (record._section_number) {
    sectionMap.set(record.side + "|" + record._section_number, record);
  }
}

for (const [key, sourceEquation] of equationMap.entries()) {
  if (!key.startsWith("source|")) {
    continue;
  }
  const tag = key.slice("source|".length);
  const targetEquation = equationMap.get("target|" + tag);
  if (targetEquation) {
    addCrossref(sourceEquation, {
      kind: "parallel_equation_tag",
      label: tag,
      target_record_id: targetEquation.record_id,
      resolution_state: "resolved",
      basis: "same_explicit_tag_unchecked",
    });
    addCrossref(targetEquation, {
      kind: "parallel_equation_tag",
      label: tag,
      target_record_id: sourceEquation.record_id,
      resolution_state: "resolved",
      basis: "same_explicit_tag_unchecked",
    });
  }
}

for (const [key, sourceSection] of sectionMap.entries()) {
  if (!key.startsWith("source|")) {
    continue;
  }
  const number = key.slice("source|".length);
  const targetSection = sectionMap.get("target|" + number);
  if (targetSection) {
    addCrossref(sourceSection, {
      kind: "parallel_section_number",
      label: number,
      target_record_id: targetSection.record_id,
      resolution_state: "resolved",
      basis: "same_explicit_section_number_unchecked",
    });
    addCrossref(targetSection, {
      kind: "parallel_section_number",
      label: number,
      target_record_id: sourceSection.record_id,
      resolution_state: "resolved",
      basis: "same_explicit_section_number_unchecked",
    });
  }
}

const pairableTypes = [
  "title_block",
  "publication_note",
  "author",
  "section_heading",
  "paragraph",
  "theorem_statement",
  "proof",
  "display_math",
  "footnote",
  "footnote_marker",
  "bibliographic_item",
];
for (const unit of units) {
  for (const type of pairableTypes) {
    const sourceItems = records.filter(function (record) {
      return record.unit_id === unit.unit && record.side === "source" && record.structure_type === type;
    });
    const targetItems = records.filter(function (record) {
      return record.unit_id === unit.unit && record.side === "target" && record.structure_type === type;
    });
    if (sourceItems.length > 0 && sourceItems.length === targetItems.length) {
      for (let index = 0; index < sourceItems.length; index += 1) {
        addCrossref(sourceItems[index], {
          kind: "parallel_structure_occurrence",
          label: type + " " + (index + 1),
          target_record_id: targetItems[index].record_id,
          resolution_state: "resolved",
          basis: "same_type_count_and_occurrence_within_unit_unchecked",
        });
        addCrossref(targetItems[index], {
          kind: "parallel_structure_occurrence",
          label: type + " " + (index + 1),
          target_record_id: sourceItems[index].record_id,
          resolution_state: "resolved",
          basis: "same_type_count_and_occurrence_within_unit_unchecked",
        });
      }
    }
  }
}

for (const record of records) {
  if (!record._text || record.structure_type === "equation") {
    continue;
  }
  const textWithoutTags = record._text.replace(/\\tag\{[^}]+\}/g, "");
  const equationRegex = /\((\d+[a-z]?)\.\)/gi;
  let equationMatch;
  const seenEquationLabels = new Set();
  while ((equationMatch = equationRegex.exec(textWithoutTags)) !== null) {
    const label = equationMatch[1];
    if (seenEquationLabels.has(label)) {
      continue;
    }
    seenEquationLabels.add(label);
    const target = equationMap.get(record.side + "|" + label) || null;
    addCrossref(record, {
      kind: "equation_reference",
      label: label,
      target_record_id: target ? target.record_id : null,
      resolution_state: target ? "resolved" : "out_of_scope_or_unresolved",
      basis: "lexical_reference_only_unchecked",
    });
  }
  const sectionRegex = /\\S\\?\s*(\d+)/g;
  let sectionMatch;
  const seenSectionLabels = new Set();
  while ((sectionMatch = sectionRegex.exec(record._text)) !== null) {
    const label = sectionMatch[1];
    if (seenSectionLabels.has(label)) {
      continue;
    }
    seenSectionLabels.add(label);
    const target = sectionMap.get(record.side + "|" + label) || null;
    addCrossref(record, {
      kind: "section_reference",
      label: label,
      target_record_id: target ? target.record_id : null,
      resolution_state: target ? "resolved" : "out_of_scope_or_unresolved",
      basis: "lexical_reference_only_unchecked",
    });
  }
}

for (const record of records) {
  record.crossrefs.sort(function (left, right) {
    return [left.kind, left.label, left.target_record_id || ""].join("|")
      .localeCompare([right.kind, right.label, right.target_record_id || ""].join("|"));
  });
  const clean = withoutKey(record, "__none__");
  for (const key of Object.keys(clean)) {
    if (key.startsWith("_")) {
      delete clean[key];
    }
  }
  Object.assign(record, clean);
  delete record._text;
  delete record._equation_tag;
  delete record._section_number;
  record.record_sha256 = sha256(Buffer.from(canonical(withoutKey(record, "record_sha256")), "utf8"));
}

const structureTypes = [
  "work",
  "tranche",
  "unit",
  "source_document",
  "target_document",
  "metadata_header",
  "title_block",
  "author",
  "publication_note",
  "center_block",
  "section_heading",
  "paragraph",
  "theorem_statement",
  "proof",
  "display_math",
  "equation",
  "note",
  "footnote",
  "footnote_marker",
  "bibliographic_item",
  "blank_separator",
  "other",
];
const structuralHeaders = [
  "schema_version",
  "record_id",
  "work_id",
  "tranche_id",
  "unit_id",
  "side",
  "language",
  "structure_type",
  "label",
  "parent_id",
  "order",
  "sibling_order",
  "depth",
  "coverage_role",
  "record_basis_json",
  "locators_json",
  "crossrefs_json",
  "completion_state",
  "review_state",
  "formula_review_state",
  "publication_state",
  "continuation_cursor",
  "record_sha256",
];

const structuralSchema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:interlanguage:noether:p04:ko:structural-index:1.0.0",
  title: "Noether Paper 4 Korean T01--T03 producer structural record",
  description: "Hierarchical, mechanically located source/target structure. Parallel links are occurrence/tag links only and do not perform source, Korean, formula, build, render, publication, certification, or approval review.",
  type: "object",
  required: [
    "schema_version", "record_id", "work_id", "tranche_id", "unit_id", "side", "language",
    "structure_type", "label", "parent_id", "order", "sibling_order", "depth", "coverage_role",
    "record_basis", "locators", "crossrefs", "completion_state", "review_state",
    "formula_review_state", "publication_state", "continuation_cursor", "record_sha256",
  ],
  properties: {
    schema_version: { const: SCHEMA_VERSION, description: "Structural schema version." },
    record_id: { type: "string", pattern: "^NOE-P04-KO-[A-Z0-9-]+$", description: "Stable hierarchy/type/occurrence identifier." },
    work_id: { const: WORK_ID, description: "Stable work identifier." },
    tranche_id: { enum: ["ALL", "T01", "T02", "T03"], description: "Frozen tranche scope; later tranches are prohibited." },
    unit_id: { enum: ["ALL"].concat(units.map(function (unit) { return unit.unit; })), description: "Scoped producer unit identifier." },
    side: { enum: ["aggregate", "source", "target"], description: "Aggregate container, German source, or Korean target side." },
    language: { enum: ["mul", "de", "ko-KR"], description: "BCP-47 language, with mul used only for aggregate containers." },
    structure_type: { enum: structureTypes, description: "Mechanically classified structural role." },
    label: { type: "string", minLength: 1, description: "Non-authoritative structural label." },
    parent_id: { type: ["string", "null"], description: "Immediate hierarchy parent; null only for the work root." },
    order: { type: "integer", minimum: 1, description: "Global deterministic preorder." },
    sibling_order: { type: "integer", minimum: 1, description: "One-based order among records sharing a parent." },
    depth: { type: "integer", minimum: 0, description: "Hierarchy depth from work root." },
    coverage_role: { enum: ["container", "primary", "annotation"], description: "Primary records partition physical lines; annotations may overlap; containers aggregate." },
    record_basis: {
      type: "array",
      minItems: 1,
      uniqueItems: true,
      items: { enum: ["source_fact", "target_fact", "computation", "producer_editorial_inference"] },
      description: "Distinguishes explicit bytes, computation, and producer structural inference.",
    },
    locators: {
      type: "array",
      minItems: 1,
      items: { "$ref": "#/$defs/locator" },
      description: "One or more hash-bound physical locators.",
    },
    crossrefs: {
      type: "array",
      items: { "$ref": "#/$defs/crossref" },
      description: "Resolved or explicitly unresolved lexical/parallel cross-references.",
    },
    completion_state: { enum: ["scope_frozen_t01_t03", "authority_slice_indexed", "producer_draft_text_indexed"], description: "Producer evidence completion state only." },
    review_state: { const: "unchecked", description: "No source or Korean review was performed." },
    formula_review_state: { const: "not_performed", description: "No formula review was performed." },
    publication_state: { const: "private_not_for_publication", description: "No publication eligibility claim." },
    continuation_cursor: { const: CURSOR, description: "First later source line; T04 remains out of this evidence freeze." },
    record_sha256: { type: "string", pattern: "^[A-F0-9]{64}$", description: "SHA-256 of canonical record JSON excluding this field." },
  },
  "$defs": {
    locator: {
      type: "object",
      additionalProperties: false,
      required: [
        "side", "language", "path_workspace_relative", "line_basis", "line_start", "line_end",
        "file_bytes", "file_sha256", "slice_utf8_bytes_lf", "slice_sha256_lf", "fragment_kind",
        "fragment_ordinal", "fragment_text", "fragment_sha256_utf8", "authority_pointer_id",
        "authority_pointer_sha256",
      ],
      properties: {
        side: { enum: ["source", "target"], description: "Physical side." },
        language: { enum: ["de", "ko-KR"], description: "Locator language." },
        path_workspace_relative: { type: "string", minLength: 1, description: "Forward-slash path relative to the workspace root." },
        line_basis: { enum: ["whole_authority", "target_file"], description: "Line-number coordinate system." },
        line_start: { type: "integer", minimum: 1, description: "Inclusive line start." },
        line_end: { type: "integer", minimum: 1, description: "Inclusive line end." },
        file_bytes: { type: "integer", minimum: 0, description: "Raw file byte count." },
        file_sha256: { type: "string", pattern: "^[A-F0-9]{64}$", description: "Raw file SHA-256." },
        slice_utf8_bytes_lf: { type: "integer", minimum: 1, description: "LF-normalized UTF-8 slice byte count." },
        slice_sha256_lf: { type: "string", pattern: "^[A-F0-9]{64}$", description: "LF-normalized UTF-8 line-slice SHA-256." },
        fragment_kind: { type: ["string", "null"], description: "Optional macro/tag fragment selector." },
        fragment_ordinal: { type: ["integer", "null"], minimum: 1, description: "One-based same-line fragment occurrence." },
        fragment_text: { type: ["string", "null"], description: "Exact optional fragment used for re-identification." },
        fragment_sha256_utf8: { type: ["string", "null"], pattern: "^[A-F0-9]{64}$", description: "UTF-8 SHA-256 of fragment_text." },
        authority_pointer_id: { enum: ["NOETH-DE-AUTH-v003-20260804", "NOETH-DE-AUTH-v004-20260804"], description: "Unit custody pointer." },
        authority_pointer_sha256: { type: "string", pattern: "^[A-F0-9]{64}$", description: "Custody pointer SHA-256." },
      },
    },
    crossref: {
      type: "object",
      additionalProperties: false,
      required: ["kind", "label", "target_record_id", "resolution_state", "basis"],
      properties: {
        kind: { enum: ["parallel_document", "parallel_equation_tag", "parallel_section_number", "parallel_structure_occurrence", "equation_reference", "section_reference", "contains_bibliographic_item"], description: "Cross-reference kind." },
        label: { type: "string", minLength: 1, description: "Reference label." },
        target_record_id: { type: ["string", "null"], description: "Resolved record ID, or null when outside scope/unresolved." },
        resolution_state: { enum: ["resolved", "out_of_scope_or_unresolved"], description: "Mechanical resolution result." },
        basis: { type: "string", minLength: 1, description: "Explicit non-semantic link basis." },
      },
    },
  },
  additionalProperties: false,
  "x-csv-projection": {
    headers: structuralHeaders,
    nested_json_columns: ["record_basis_json", "locators_json", "crossrefs_json"],
    description: "CSV is a flat projection; arrays and objects are canonical compact JSON strings.",
  },
};

const structuralDir = path.join(evidenceRoot, "structural_index");
const structuralSchemaPath = path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX.schema.json");
const structuralJsonlPath = path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX.jsonl");
const structuralCsvPath = path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX.csv");
const structuralReportPath = path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json");
await writeJson(structuralSchemaPath, structuralSchema);
const structuralJsonl = records.map(function (record) { return JSON.stringify(record); }).join("\n") + "\n";
await writeText(structuralJsonlPath, structuralJsonl);
const structuralRows = records.map(function (record) {
  return {
    schema_version: record.schema_version,
    record_id: record.record_id,
    work_id: record.work_id,
    tranche_id: record.tranche_id,
    unit_id: record.unit_id,
    side: record.side,
    language: record.language,
    structure_type: record.structure_type,
    label: record.label,
    parent_id: record.parent_id,
    order: record.order,
    sibling_order: record.sibling_order,
    depth: record.depth,
    coverage_role: record.coverage_role,
    record_basis_json: canonical(record.record_basis),
    locators_json: canonical(record.locators),
    crossrefs_json: canonical(record.crossrefs),
    completion_state: record.completion_state,
    review_state: record.review_state,
    formula_review_state: record.formula_review_state,
    publication_state: record.publication_state,
    continuation_cursor: record.continuation_cursor,
    record_sha256: record.record_sha256,
  };
});
const structuralCsv = toCsv(structuralHeaders, structuralRows);
await writeText(structuralCsvPath, structuralCsv);

const structuralErrors = [];
function validationCheck(condition, message) {
  if (!condition) {
    structuralErrors.push(message);
  }
}

const structuralParsed = normalizeLf(await fs.readFile(structuralJsonlPath, "utf8")).trimEnd().split("\n").filter(Boolean).map(JSON.parse);
validationCheck(structuralParsed.length === records.length, "JSONL record count mismatch");
validationCheck(new Set(structuralParsed.map(function (record) { return record.record_id; })).size === structuralParsed.length, "Record IDs are not unique");
for (let index = 0; index < structuralParsed.length; index += 1) {
  const record = structuralParsed[index];
  validationCheck(record.order === index + 1, "Non-sequential order at " + record.record_id);
  validationCheck(record.record_sha256 === sha256(Buffer.from(canonical(withoutKey(record, "record_sha256")), "utf8")), "Record hash mismatch at " + record.record_id);
  if (record.parent_id !== null) {
    const parent = structuralParsed.find(function (candidate) { return candidate.record_id === record.parent_id; });
    validationCheck(Boolean(parent), "Missing parent for " + record.record_id);
    if (parent) {
      validationCheck(record.depth === parent.depth + 1, "Depth mismatch at " + record.record_id);
    }
  } else {
    validationCheck(record.record_id === workRecord.record_id, "Unexpected root record " + record.record_id);
  }
  validationCheck(!record.tranche_id.match(/^T0[456]$/), "Later tranche leaked into " + record.record_id);
  for (const loc of record.locators) {
    const fullPath = path.join(workspaceRoot, loc.path_workspace_relative.replace(/\//g, path.sep));
    const file = fullPath === authority.fullPath ? authority : units.map(function (unit) { return unit.target; }).find(function (candidate) { return candidate.fullPath === fullPath; });
    validationCheck(Boolean(file), "Locator path outside frozen inputs at " + record.record_id);
    if (!file) {
      continue;
    }
    validationCheck(file.fileSha256 === loc.file_sha256, "Locator file hash mismatch at " + record.record_id);
    const slice = lineSlice(file, loc.line_start, loc.line_end);
    validationCheck(Buffer.byteLength(slice, "utf8") === loc.slice_utf8_bytes_lf, "Locator slice bytes mismatch at " + record.record_id);
    validationCheck(sha256(Buffer.from(slice, "utf8")) === loc.slice_sha256_lf, "Locator slice hash mismatch at " + record.record_id);
    if (loc.fragment_text !== null) {
      validationCheck(sha256(Buffer.from(loc.fragment_text, "utf8")) === loc.fragment_sha256_utf8, "Fragment hash mismatch at " + record.record_id);
      validationCheck(slice.includes(loc.fragment_text), "Fragment missing from locator slice at " + record.record_id);
    } else {
      validationCheck(loc.fragment_kind === null && loc.fragment_ordinal === null && loc.fragment_sha256_utf8 === null, "Partial null fragment selector at " + record.record_id);
    }
  }
  for (const crossref of record.crossrefs) {
    if (crossref.target_record_id !== null) {
      validationCheck(structuralParsed.some(function (candidate) { return candidate.record_id === crossref.target_record_id; }), "Crossref target missing at " + record.record_id);
      validationCheck(crossref.resolution_state === "resolved", "Resolved crossref state mismatch at " + record.record_id);
    }
  }
}

let sourcePrimaryLines = 0;
let targetPrimaryLines = 0;
for (const unit of units) {
  for (const side of ["source", "target"]) {
    const expectedStart = side === "source" ? unit.sourceStart : 1;
    const expectedEnd = side === "source" ? unit.sourceEnd : unit.target.lines.length;
    const counts = new Map();
    for (let line = expectedStart; line <= expectedEnd; line += 1) {
      counts.set(line, 0);
    }
    const primary = structuralParsed.filter(function (record) {
      return record.unit_id === unit.unit && record.side === side && record.coverage_role === "primary";
    });
    for (const record of primary) {
      validationCheck(record.locators.length === 1, "Primary record must have one locator at " + record.record_id);
      const loc = record.locators[0];
      for (let line = loc.line_start; line <= loc.line_end; line += 1) {
        counts.set(line, (counts.get(line) || 0) + 1);
      }
    }
    for (const [line, count] of counts.entries()) {
      validationCheck(count === 1, "Primary coverage count " + count + " for " + unit.unit + " " + side + " line " + line);
    }
    if (side === "source") {
      sourcePrimaryLines += counts.size;
    } else {
      targetPrimaryLines += counts.size;
    }
  }
}

const parsedStructuralCsv = parseCsv(structuralCsv);
validationCheck(canonical(parsedStructuralCsv[0]) === canonical(structuralHeaders), "Structural CSV header mismatch");
validationCheck(parsedStructuralCsv.length === structuralParsed.length + 1, "Structural CSV row count mismatch");
for (let index = 0; index < structuralRows.length; index += 1) {
  const projected = structuralHeaders.map(function (header) {
    const value = structuralRows[index][header];
    return value === null || value === undefined ? "" : String(value);
  });
  validationCheck(canonical(parsedStructuralCsv[index + 1]) === canonical(projected), "Structural CSV projection mismatch at row " + (index + 2));
}

const typeCounts = {};
for (const type of structureTypes) {
  typeCounts[type] = structuralParsed.filter(function (record) { return record.structure_type === type; }).length;
}
const sideCounts = {
  aggregate: structuralParsed.filter(function (record) { return record.side === "aggregate"; }).length,
  source: structuralParsed.filter(function (record) { return record.side === "source"; }).length,
  target: structuralParsed.filter(function (record) { return record.side === "target"; }).length,
};
const sourceUnitHashes = {};
const targetFileHashes = {};
for (const unit of units) {
  sourceUnitHashes[unit.unit] = unit.sourceSliceSha256;
  targetFileHashes[unit.unit] = unit.targetSha256;
}
const structuralSchemaIdentity = await fileIdentity(structuralSchemaPath);
const structuralJsonlIdentity = await fileIdentity(structuralJsonlPath);
const structuralCsvIdentity = await fileIdentity(structuralCsvPath);
const builderIdentity = await fileIdentity(scriptPath);
const structuralReport = {
  schema_version: SCHEMA_VERSION,
  status: structuralErrors.length === 0 ? "PASS" : "FAIL",
  errors: structuralErrors,
  validator: path.basename(scriptPath),
  builder_sha256: builderIdentity.sha256,
  evidence_date: "2026-08-04",
  scope: {
    tranches: ["T01", "T02", "T03"],
    units: units.map(function (unit) { return unit.unit; }),
    later_tranches_excluded: ["T04", "T05", "T06"],
    source_unit_line_count: sourcePrimaryLines,
    target_file_line_count: targetPrimaryLines,
    primary_line_coverage_uncovered: 0,
    primary_line_coverage_overlap: 0,
    source_excluded_separator_lines: [3664, 3691, 3700, 3741, 3763, 3777, 3864],
    next_cursor: CURSOR,
  },
  record_count: structuralParsed.length,
  unique_record_count: new Set(structuralParsed.map(function (record) { return record.record_id; })).size,
  latest_record_id: structuralParsed[structuralParsed.length - 1].record_id,
  side_counts: sideCounts,
  type_counts_including_zero: typeCounts,
  authority: {
    path_workspace_relative: relPath(authorityPath),
    bytes: authority.bytes.length,
    sha256: authority.fileSha256,
    continuous_interval: "3611--3886",
    continuous_interval_lf_utf8_bytes: Buffer.byteLength(continuousSlice, "utf8"),
    continuous_interval_sha256_lf: sha256(Buffer.from(continuousSlice, "utf8")),
  },
  source_unit_hashes_verified: sourceUnitHashes,
  target_file_hashes_verified: targetFileHashes,
  structural_definition: {
    paragraph: "Maximal contiguous top-level nonblank prose lines outside comments, headings, center blocks, theorem/proof heads, bibliography commands, and display environments.",
    equation_display: "Outer equation environments are equation records; bracket/starred displays are display_math; each explicit tag inside a multi-equation display has an equation annotation.",
    note_bibliography: "Every footnote, footnotetext, and footnotemark macro is annotated; a bibliographic_item child is created when a footnote contains a mechanical bibliographic cue.",
    parallel_links: "Same explicit equation/section tag or equal same-type occurrence count within a unit; all are unchecked and non-semantic.",
  },
  schema: { path: path.basename(structuralSchemaPath), bytes: structuralSchemaIdentity.bytes, sha256: structuralSchemaIdentity.sha256 },
  jsonl: { path: path.basename(structuralJsonlPath), bytes: structuralJsonlIdentity.bytes, sha256: structuralJsonlIdentity.sha256 },
  csv: { path: path.basename(structuralCsvPath), bytes: structuralCsvIdentity.bytes, sha256: structuralCsvIdentity.sha256 },
  review_boundary: "Mechanical producer reproducibility evidence only; no source, Korean, formula, compilation, rendering, assembly, packaging, certification, approval, German patch, scan, or SGA operation.",
};
await writeJson(structuralReportPath, structuralReport);
assert(structuralReport.status === "PASS", "Structural validation failed: " + structuralErrors.join("; "));

const difficultyHeaders = [
  "schema_version",
  "record_id",
  "recorded_at",
  "time_precision",
  "timezone",
  "append_sequence",
  "previous_record_sha256",
  "work_id",
  "tranche_ids_json",
  "unit_ids_json",
  "category",
  "sense_window",
  "symptom",
  "cause_evidence_json",
  "attempted_approaches_json",
  "resolution_state",
  "resolution",
  "artifact_effect",
  "related_paths_json",
  "related_structural_ids_json",
  "review_state",
  "supersession_state",
  "revisit_condition",
  "record_sha256",
];

const difficultySchema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:interlanguage:noether:p04:ko:difficulty-ledger:1.0.0",
  title: "Noether Paper 4 Korean T01--T03 append-only producer difficulty record",
  description: "Hash-chained operational/metadata difficulty history. It records only observed events and makes no source, Korean, formula, build, render, publication, certification, or approval judgment.",
  type: "object",
  required: difficultyHeaders.filter(function (header) { return !header.endsWith("_json"); }).concat([
    "tranche_ids", "unit_ids", "cause_evidence", "attempted_approaches", "related_paths", "related_structural_ids",
  ]),
  properties: {
    schema_version: { const: SCHEMA_VERSION, description: "Difficulty schema version." },
    record_id: { type: "string", pattern: "^CJK-KO-P04-HARD-[0-9]{3}$", description: "Stable append-only difficulty ID." },
    recorded_at: { type: "string", minLength: 10, description: "Observed time at stated precision." },
    time_precision: { enum: ["day", "minute_approximate", "second"], description: "No false precision is added." },
    timezone: { const: "Europe/Berlin", description: "IANA timezone for recorded_at." },
    append_sequence: { type: "integer", minimum: 1, description: "Contiguous append order." },
    previous_record_sha256: { type: ["string", "null"], pattern: "^[A-F0-9]{64}$", description: "Prior record hash, null only for sequence 1." },
    work_id: { const: WORK_ID, description: "Stable work identifier." },
    tranche_ids: { type: "array", items: { enum: ["T01", "T02", "T03"] }, uniqueItems: true, description: "Affected frozen tranches." },
    unit_ids: { type: "array", items: { enum: units.map(function (unit) { return unit.unit; }) }, uniqueItems: true, description: "Affected frozen units." },
    category: { enum: ["metadata_wording_failure", "routing_boundary_failure", "tooling_failure"], description: "Observed event category." },
    sense_window: { type: "string", minLength: 1, description: "Exact ambiguity or operational window." },
    symptom: { type: "string", minLength: 1, description: "Observed symptom without invented interpretation." },
    cause_evidence: {
      type: "array",
      minItems: 1,
      items: {
        type: "object",
        additionalProperties: false,
        required: ["kind", "detail", "path_workspace_relative", "sha256"],
        properties: {
          kind: { type: "string", minLength: 1, description: "Evidence kind." },
          detail: { type: "string", minLength: 1, description: "Observed fact or computation." },
          path_workspace_relative: { type: ["string", "null"], description: "Optional supporting path." },
          sha256: { type: ["string", "null"], pattern: "^[A-F0-9]{64}$", description: "Optional frozen supporting hash." },
        },
      },
      description: "Evidence supporting the event record.",
    },
    attempted_approaches: {
      type: "array",
      minItems: 1,
      items: {
        type: "object",
        additionalProperties: false,
        required: ["approach", "outcome", "status"],
        properties: {
          approach: { type: "string", minLength: 1, description: "Attempted syntax or wording." },
          outcome: { type: "string", minLength: 1, description: "Observed outcome." },
          status: { enum: ["failed", "accepted", "rejected", "specified"], description: "Attempt status; specified does not claim execution." },
        },
      },
      description: "Preserved failed and accepted approaches.",
    },
    resolution_state: { enum: ["resolved", "retry_specified"], description: "Resolved event or a failure whose exact corrective retry syntax is specified without claiming execution." },
    resolution: { type: "string", minLength: 1, description: "Observed resolution." },
    artifact_effect: { type: "string", minLength: 1, description: "Explicit file/output effect." },
    related_paths: { type: "array", items: { type: "string" }, uniqueItems: true, description: "Related workspace-relative paths." },
    related_structural_ids: { type: "array", items: { type: "string" }, uniqueItems: true, description: "Related structural IDs." },
    review_state: { const: "producer_metadata_unchecked", description: "Operational producer record only." },
    supersession_state: { const: "current", description: "Current append record." },
    revisit_condition: { type: "string", minLength: 1, description: "Trigger for future appended evidence." },
    record_sha256: { type: "string", pattern: "^[A-F0-9]{64}$", description: "SHA-256 of canonical record JSON excluding this field." },
  },
  additionalProperties: false,
  "x-csv-projection": {
    headers: difficultyHeaders,
    nested_json_columns: ["tranche_ids_json", "unit_ids_json", "cause_evidence_json", "attempted_approaches_json", "related_paths_json", "related_structural_ids_json"],
    description: "CSV is a flat projection of the authoritative chained JSONL.",
  },
};

const display3644 = records.find(function (record) {
  return record.unit_id === "U02"
    && record.side === "source"
    && record.coverage_role === "primary"
    && record.structure_type === "display_math"
    && record.locators[0].line_start <= 3644
    && record.locators[0].line_end >= 3644;
});
assert(Boolean(display3644), "Could not identify the line-3644 source display record");

const difficultyRecords = [
  {
    schema_version: SCHEMA_VERSION,
    record_id: "CJK-KO-P04-HARD-001",
    recorded_at: "2026-08-04",
    time_precision: "day",
    timezone: "Europe/Berlin",
    append_sequence: 1,
    previous_record_sha256: null,
    work_id: WORK_ID,
    tranche_ids: ["T01"],
    unit_ids: ["U02"],
    category: "metadata_wording_failure",
    sense_window: "Blank-line topology in producer custody wording versus the actual role of whole-authority line 3644.",
    symptom: "The initial custody sentence incorrectly named whole line 3644 as a blank separator; line 3644 is part of the determinant display.",
    cause_evidence: [
      {
        kind: "producer_choices_record",
        detail: "TRANSLATION_CHOICES records the incorrect first wording and its correction before the first frozen metadata hash.",
        path_workspace_relative: relPath(path.join(projectRoot, "TRANSLATION_CHOICES_T01_U01_U04.md")),
        sha256: "89326A4A8D315AED699F820EDEECF0A3B5DAD4C7F92376F8D41A26C12F8EA507",
      },
      {
        kind: "mechanical_line_locator",
        detail: "The structural primary display spans whole-authority lines 3643--3651 and therefore contains line 3644.",
        path_workspace_relative: relPath(authorityPath),
        sha256: AUTHORITY_SHA256,
      },
    ],
    attempted_approaches: [
      {
        approach: "Describe whole-authority line 3644 as a blank separator in custody metadata.",
        outcome: "Rejected because line 3644 belongs to the determinant display.",
        status: "failed",
      },
      {
        approach: "State the actual topology: retained blanks 3640 and 3693; excluded separators 3664 and 3691.",
        outcome: "Accepted before the first frozen metadata hash.",
        status: "accepted",
      },
    ],
    resolution_state: "resolved",
    resolution: "The custody wording was corrected before its first frozen metadata hash; no source slice or target identity changed.",
    artifact_effect: "Metadata wording only; no source, target, formula, or generated-output bytes changed.",
    related_paths: [
      relPath(path.join(projectRoot, "TRANSLATION_CHOICES_T01_U01_U04.md")),
      relPath(path.join(projectRoot, "SOURCE_CUSTODY_T01.md")),
    ],
    related_structural_ids: [display3644.record_id],
    review_state: "producer_metadata_unchecked",
    supersession_state: "current",
    revisit_condition: "Append only if a future custody statement misidentifies a scoped physical line or blank separator.",
  },
  {
    schema_version: SCHEMA_VERSION,
    record_id: "CJK-KO-P04-HARD-002",
    recorded_at: "2026-08-04T06:06:00+02:00",
    time_precision: "minute_approximate",
    timezone: "Europe/Berlin",
    append_sequence: 2,
    previous_record_sha256: null,
    work_id: WORK_ID,
    tranche_ids: ["T01", "T02", "T03"],
    unit_ids: units.map(function (unit) { return unit.unit; }),
    category: "tooling_failure",
    sense_window: "PowerShell foreach grammar during the source-hash loop, before any output or file write.",
    symptom: "PowerShell raised ParserError for foreach($x in$units): Missing 'in' after variable in foreach loop.",
    cause_evidence: [
      {
        kind: "observed_parser_error",
        detail: "At approximately 2026-08-04 06:06 Europe/Berlin, the token sequence foreach($x in$units) was rejected with Missing 'in' after variable in foreach loop.",
        path_workspace_relative: null,
        sha256: null,
      },
      {
        kind: "artifact_effect_observation",
        detail: "Parsing aborted before execution; no output was produced and no files were changed.",
        path_workspace_relative: null,
        sha256: null,
      },
    ],
    attempted_approaches: [
      {
        approach: "Use foreach($x in$units) in the PowerShell source-hash command.",
        outcome: "ParserError: Missing 'in' after variable in foreach loop.",
        status: "failed",
      },
      {
        approach: "Retry with foreach ($x in $units).",
        outcome: "Accepted; the source-hash loop ran successfully.",
        status: "accepted",
      },
    ],
    resolution_state: "resolved",
    resolution: "The retry inserted the required token-separating whitespace: foreach ($x in $units).",
    artifact_effect: "Failed parse changed no output or file; the successful retry was read-only hashing.",
    related_paths: [],
    related_structural_ids: [workRecord.record_id],
    review_state: "producer_metadata_unchecked",
    supersession_state: "current",
    revisit_condition: "Append only if a future PowerShell loop reproduces this exact grammar failure or a distinct observed tooling event occurs.",
  },
  {
    schema_version: SCHEMA_VERSION,
    record_id: "CJK-KO-P04-HARD-003",
    recorded_at: "2026-08-04T06:50:26+02:00",
    time_precision: "second",
    timezone: "Europe/Berlin",
    append_sequence: 3,
    previous_record_sha256: null,
    work_id: WORK_ID,
    tranche_ids: [],
    unit_ids: [],
    category: "tooling_failure",
    sense_window: "PowerShell command-token whitespace in a read-only hash command for adjacent later-tranche human documents, outside the T01--T03 structural freeze.",
    symptom: "The first hash command failed repeatedly: Join-Path$r$n was not recognized, and Get-Item -LiteralPath$p plus Get-FileHash -LiteralPath$p produced parameter errors.",
    cause_evidence: [
      {
        kind: "observed_command_token_errors",
        detail: "At 2026-08-04T06:50:26+02:00, missing spaces joined cmdlet names or parameter names to variables in Join-Path$r$n, -LiteralPath$p, and related command tokens.",
        path_workspace_relative: null,
        sha256: null,
      },
      {
        kind: "artifact_effect_observation",
        detail: "No files changed; only the requested hash output failed.",
        path_workspace_relative: null,
        sha256: null,
      },
    ],
    attempted_approaches: [
      {
        approach: "Use Join-Path$r$n and pass -LiteralPath$p to Get-Item and Get-FileHash.",
        outcome: "PowerShell command recognition and parameter-binding errors; no hash output.",
        status: "failed",
      },
      {
        approach: "Retry with Join-Path $r $n and -LiteralPath $p.",
        outcome: "Corrective syntax specified; successful execution is not claimed by this record.",
        status: "specified",
      },
    ],
    resolution_state: "retry_specified",
    resolution: "Use token-separating whitespace in the read-only retry: Join-Path $r $n and -LiteralPath $p.",
    artifact_effect: "No files changed; only hash output failed.",
    related_paths: [],
    related_structural_ids: [],
    review_state: "producer_metadata_unchecked",
    supersession_state: "current",
    revisit_condition: "Append a resolving successor only after the corrected read-only hash command is actually observed to succeed.",
  },
  {
    schema_version: SCHEMA_VERSION,
    record_id: "CJK-KO-P04-HARD-004",
    recorded_at: "2026-08-04T06:51:00+02:00",
    time_precision: "minute_approximate",
    timezone: "Europe/Berlin",
    append_sequence: 4,
    previous_record_sha256: null,
    work_id: WORK_ID,
    tranche_ids: [],
    unit_ids: [],
    category: "tooling_failure",
    sense_window: "Recurrence of missing PowerShell whitespace during a log-rehash attempt, outside the T01--T03 structural freeze.",
    symptom: "The log rehash used Get-Item -LiteralPath$p and Get-FileHash -LiteralPath$p, producing parameter-not-found errors and no identity output.",
    cause_evidence: [
      {
        kind: "observed_recurrence",
        detail: "At approximately 06:51 Europe/Berlin, the -LiteralPath$p token repeated the missing-whitespace fault observed in HARD-003.",
        path_workspace_relative: null,
        sha256: null,
      },
      {
        kind: "artifact_effect_observation",
        detail: "No file changed and no identity output was produced.",
        path_workspace_relative: null,
        sha256: null,
      },
    ],
    attempted_approaches: [
      {
        approach: "Use Get-Item -LiteralPath$p and Get-FileHash -LiteralPath$p in the log-rehash command.",
        outcome: "Parameter-not-found errors; no identity output.",
        status: "failed",
      },
      {
        approach: "Retry both cmdlets with -LiteralPath $p.",
        outcome: "Corrective syntax specified; successful execution is not claimed by this record.",
        status: "specified",
      },
    ],
    resolution_state: "retry_specified",
    resolution: "Use a separating space in every parameter binding: -LiteralPath $p.",
    artifact_effect: "No file changed and no identity output was produced.",
    related_paths: [],
    related_structural_ids: [],
    review_state: "producer_metadata_unchecked",
    supersession_state: "current",
    revisit_condition: "Append a resolving successor only after the corrected read-only rehash is actually observed to succeed.",
  },
  {
    schema_version: SCHEMA_VERSION,
    record_id: "CJK-KO-P04-HARD-005",
    recorded_at: "2026-08-04T06:55:00+02:00",
    time_precision: "minute_approximate",
    timezone: "Europe/Berlin",
    append_sequence: 5,
    previous_record_sha256: null,
    work_id: WORK_ID,
    tranche_ids: [],
    unit_ids: [],
    category: "tooling_failure",
    sense_window: "Further recurrence of the HARD-003/HARD-004 PowerShell token-spacing family during a read-only evidence progress query.",
    symptom: "Test-Path -LiteralPath$p caused a parameter-not-found error; the progress query returned no output.",
    cause_evidence: [
      {
        kind: "observed_recurrence",
        detail: "At approximately 06:55 Europe/Berlin, -LiteralPath$p again omitted the required separating space, now with Test-Path; this is recurrence evidence for the existing token-spacing failure family, not a new root cause.",
        path_workspace_relative: null,
        sha256: null,
      },
      {
        kind: "artifact_effect_observation",
        detail: "No output was returned and no file changed.",
        path_workspace_relative: null,
        sha256: null,
      },
    ],
    attempted_approaches: [
      {
        approach: "Use Test-Path -LiteralPath$p in the read-only evidence progress query.",
        outcome: "Parameter-not-found error and no query output.",
        status: "failed",
      },
      {
        approach: "Retry with Test-Path -LiteralPath $p.",
        outcome: "Corrective syntax specified; successful execution is not claimed by this record.",
        status: "specified",
      },
    ],
    resolution_state: "retry_specified",
    resolution: "Apply the existing token-spacing correction: -LiteralPath $p.",
    artifact_effect: "No output was returned and no file changed.",
    related_paths: [],
    related_structural_ids: [],
    review_state: "producer_metadata_unchecked",
    supersession_state: "current",
    revisit_condition: "Append a resolving successor only after the corrected read-only progress query is actually observed to succeed.",
  },
  {
    schema_version: SCHEMA_VERSION,
    record_id: "CJK-KO-P04-HARD-006",
    recorded_at: "2026-08-04",
    time_precision: "day",
    timezone: "Europe/Berlin",
    append_sequence: 6,
    previous_record_sha256: null,
    work_id: WORK_ID,
    tranche_ids: [],
    unit_ids: [],
    category: "routing_boundary_failure",
    sense_window: "Later T08 route construction outside the T01--T03 structural freeze: a source unit must retain its opening TeX container boundary.",
    symptom: "The initial T08 route specified U39 as whole-authority lines 4306--4331, mechanically omitting line 4305 \\begin{center}.",
    cause_evidence: [
      {
        kind: "observed_route_boundary_mismatch",
        detail: "Mechanical boundary inspection showed that line 4305 opens the center environment consumed by the proposed U39 route.",
        path_workspace_relative: null,
        sha256: null,
      },
      {
        kind: "artifact_effect_observation",
        detail: "The route was corrected before target freeze; no target was harmed or changed by the rejected boundary.",
        path_workspace_relative: null,
        sha256: null,
      },
    ],
    attempted_approaches: [
      {
        approach: "Route T08-U39 as whole-authority lines 4306--4331.",
        outcome: "Rejected because it omitted the opening \\begin{center} at line 4305.",
        status: "failed",
      },
      {
        approach: "Route T08-U39 as whole-authority lines 4305--4331.",
        outcome: "Accepted before target freeze with the container boundary retained.",
        status: "accepted",
      },
    ],
    resolution_state: "resolved",
    resolution: "The route was corrected to lines 4305--4331 before any target freeze.",
    artifact_effect: "No target was harmed or changed; the rejected route existed only as pre-freeze routing metadata.",
    related_paths: [],
    related_structural_ids: [],
    review_state: "producer_metadata_unchecked",
    supersession_state: "current",
    revisit_condition: "Append only if a future route begins inside an open TeX environment or drops a required container boundary.",
  },
  {
    schema_version: SCHEMA_VERSION,
    record_id: "CJK-KO-P04-HARD-007",
    recorded_at: "2026-08-04",
    time_precision: "day",
    timezone: "Europe/Berlin",
    append_sequence: 7,
    previous_record_sha256: null,
    work_id: WORK_ID,
    tranche_ids: [],
    unit_ids: [],
    category: "tooling_failure",
    sense_window: "PowerShell pipeline grammar in the first read-only T07 metadata hash command, outside the T01--T03 structural freeze.",
    symptom: "Piping directly from a foreach (...) {} statement failed with ParserError: An empty pipe element is not allowed.",
    cause_evidence: [
      {
        kind: "observed_parser_error",
        detail: "The first command placed a pipe immediately after the foreach statement rather than materializing its output.",
        path_workspace_relative: null,
        sha256: null,
      },
      {
        kind: "artifact_effect_observation",
        detail: "Parsing failed before execution and caused no file mutation.",
        path_workspace_relative: null,
        sha256: null,
      },
    ],
    attempted_approaches: [
      {
        approach: "Pipe directly from foreach (...) {} into the next command.",
        outcome: "ParserError: An empty pipe element is not allowed.",
        status: "failed",
      },
      {
        approach: "Assign $rows = foreach (...) {...}, then pipe $rows.",
        outcome: "Accepted; the corrected read-only metadata hash command completed without file mutation.",
        status: "accepted",
      },
    ],
    resolution_state: "resolved",
    resolution: "Materialize the foreach output in $rows before applying the pipeline.",
    artifact_effect: "No file mutation occurred; the failed command produced no identity output.",
    related_paths: [],
    related_structural_ids: [],
    review_state: "producer_metadata_unchecked",
    supersession_state: "current",
    revisit_condition: "Append only if a future PowerShell pipeline again treats a foreach statement as a direct pipeline expression.",
  },
];
for (let index = 0; index < difficultyRecords.length; index += 1) {
  if (index > 0) {
    difficultyRecords[index].previous_record_sha256 = difficultyRecords[index - 1].record_sha256;
  }
  difficultyRecords[index].record_sha256 = sha256(Buffer.from(canonical(withoutKey(difficultyRecords[index], "record_sha256")), "utf8"));
}

const difficultyDir = path.join(evidenceRoot, "difficulty_ledger");
const difficultySchemaPath = path.join(difficultyDir, "DIFFICULTY_LEDGER.schema.json");
const difficultyJsonlPath = path.join(difficultyDir, "DIFFICULTY_LEDGER.jsonl");
const difficultyCsvPath = path.join(difficultyDir, "DIFFICULTY_LEDGER.csv");
const difficultyReportPath = path.join(difficultyDir, "DIFFICULTY_LEDGER_VALIDATION_REPORT.json");
await writeJson(difficultySchemaPath, difficultySchema);
const difficultyJsonl = difficultyRecords.map(function (record) { return JSON.stringify(record); }).join("\n") + "\n";
try {
  const existingDifficulty = await fs.readFile(difficultyJsonlPath, "utf8");
  const normalizedExisting = normalizeLf(existingDifficulty);
  if (normalizedExisting !== difficultyJsonl) {
    let matchedPrefixCount = 0;
    for (let count = 1; count < difficultyRecords.length; count += 1) {
      const prefix = difficultyRecords.slice(0, count).map(function (record) { return JSON.stringify(record); }).join("\n") + "\n";
      if (normalizedExisting === prefix) {
        matchedPrefixCount = count;
        break;
      }
    }
    assert(matchedPrefixCount > 0, "Append-only difficulty JSONL already exists with different bytes; refusing overwrite");
    const suffix = difficultyRecords.slice(matchedPrefixCount).map(function (record) { return JSON.stringify(record); }).join("\n") + "\n";
    await fs.appendFile(difficultyJsonlPath, suffix, "utf8");
  }
} catch (error) {
  if (error && error.code === "ENOENT") {
    await writeText(difficultyJsonlPath, difficultyJsonl);
  } else {
    throw error;
  }
}
const difficultyRows = difficultyRecords.map(function (record) {
  return {
    schema_version: record.schema_version,
    record_id: record.record_id,
    recorded_at: record.recorded_at,
    time_precision: record.time_precision,
    timezone: record.timezone,
    append_sequence: record.append_sequence,
    previous_record_sha256: record.previous_record_sha256,
    work_id: record.work_id,
    tranche_ids_json: canonical(record.tranche_ids),
    unit_ids_json: canonical(record.unit_ids),
    category: record.category,
    sense_window: record.sense_window,
    symptom: record.symptom,
    cause_evidence_json: canonical(record.cause_evidence),
    attempted_approaches_json: canonical(record.attempted_approaches),
    resolution_state: record.resolution_state,
    resolution: record.resolution,
    artifact_effect: record.artifact_effect,
    related_paths_json: canonical(record.related_paths),
    related_structural_ids_json: canonical(record.related_structural_ids),
    review_state: record.review_state,
    supersession_state: record.supersession_state,
    revisit_condition: record.revisit_condition,
    record_sha256: record.record_sha256,
  };
});
const difficultyCsv = toCsv(difficultyHeaders, difficultyRows);
await writeText(difficultyCsvPath, difficultyCsv);

const difficultyErrors = [];
const parsedDifficulty = normalizeLf(await fs.readFile(difficultyJsonlPath, "utf8")).trimEnd().split("\n").filter(Boolean).map(JSON.parse);
if (parsedDifficulty.length !== 7) {
  difficultyErrors.push("Expected exactly seven observed difficulty records");
}
for (let index = 0; index < parsedDifficulty.length; index += 1) {
  const record = parsedDifficulty[index];
  if (record.append_sequence !== index + 1) {
    difficultyErrors.push("Non-contiguous append sequence at " + record.record_id);
  }
  const expectedPrevious = index === 0 ? null : parsedDifficulty[index - 1].record_sha256;
  if (record.previous_record_sha256 !== expectedPrevious) {
    difficultyErrors.push("Chain mismatch at " + record.record_id);
  }
  if (record.record_sha256 !== sha256(Buffer.from(canonical(withoutKey(record, "record_sha256")), "utf8"))) {
    difficultyErrors.push("Record hash mismatch at " + record.record_id);
  }
}
if (!parsedDifficulty[0].symptom.includes("whole line 3644") || !parsedDifficulty[0].symptom.includes("determinant display")) {
  difficultyErrors.push("HARD-001 does not preserve the blank-line wording failure");
}
if (!parsedDifficulty[1].symptom.includes("foreach($x in$units)") || !parsedDifficulty[1].symptom.includes("Missing 'in' after variable in foreach loop")) {
  difficultyErrors.push("HARD-002 does not preserve the observed ParserError");
}
if (!parsedDifficulty[1].attempted_approaches.some(function (attempt) {
  return attempt.status === "accepted" && attempt.approach.includes("foreach ($x in $units)");
})) {
  difficultyErrors.push("HARD-002 does not preserve the successful retry");
}
if (!parsedDifficulty[1].artifact_effect.includes("changed no output or file")) {
  difficultyErrors.push("HARD-002 does not preserve the no-change effect");
}
if (!parsedDifficulty[2].symptom.includes("Join-Path$r$n") || !parsedDifficulty[2].symptom.includes("-LiteralPath$p")) {
  difficultyErrors.push("HARD-003 does not preserve the observed command-token whitespace errors");
}
if (!parsedDifficulty[2].attempted_approaches.some(function (attempt) {
  return attempt.status === "specified" && attempt.approach.includes("Join-Path $r $n") && attempt.approach.includes("-LiteralPath $p");
})) {
  difficultyErrors.push("HARD-003 does not preserve the specified corrected retry syntax");
}
if (parsedDifficulty[2].resolution_state !== "retry_specified" || !parsedDifficulty[2].artifact_effect.includes("No files changed")) {
  difficultyErrors.push("HARD-003 overclaims resolution or omits the no-change effect");
}
if (!parsedDifficulty[3].symptom.includes("Get-Item -LiteralPath$p") || !parsedDifficulty[3].symptom.includes("Get-FileHash -LiteralPath$p")) {
  difficultyErrors.push("HARD-004 does not preserve the observed log-rehash recurrence");
}
if (!parsedDifficulty[3].attempted_approaches.some(function (attempt) {
  return attempt.status === "specified" && attempt.approach.includes("-LiteralPath $p");
})) {
  difficultyErrors.push("HARD-004 does not preserve the specified corrected retry syntax");
}
if (parsedDifficulty[3].resolution_state !== "retry_specified" || !parsedDifficulty[3].artifact_effect.includes("No file changed")) {
  difficultyErrors.push("HARD-004 overclaims resolution or omits the no-change effect");
}
if (!parsedDifficulty[4].symptom.includes("Test-Path -LiteralPath$p") || !parsedDifficulty[4].symptom.includes("no output")) {
  difficultyErrors.push("HARD-005 does not preserve the observed progress-query recurrence");
}
if (!parsedDifficulty[4].attempted_approaches.some(function (attempt) {
  return attempt.status === "specified" && attempt.approach.includes("Test-Path -LiteralPath $p");
})) {
  difficultyErrors.push("HARD-005 does not preserve the specified corrected retry syntax");
}
if (parsedDifficulty[4].resolution_state !== "retry_specified" || !parsedDifficulty[4].cause_evidence.some(function (evidence) {
  return evidence.detail.includes("not a new root cause");
})) {
  difficultyErrors.push("HARD-005 fails to preserve recurrence-family scope");
}
if (!parsedDifficulty[5].symptom.includes("4306--4331") || !parsedDifficulty[5].symptom.includes("4305 \\begin{center}")) {
  difficultyErrors.push("HARD-006 does not preserve the omitted route boundary");
}
if (!parsedDifficulty[5].attempted_approaches.some(function (attempt) {
  return attempt.status === "accepted" && attempt.approach.includes("4305--4331");
})) {
  difficultyErrors.push("HARD-006 does not preserve the corrected route");
}
if (parsedDifficulty[5].resolution_state !== "resolved" || !parsedDifficulty[5].artifact_effect.includes("No target was harmed")) {
  difficultyErrors.push("HARD-006 omits the pre-freeze no-harm resolution");
}
if (!parsedDifficulty[6].symptom.includes("An empty pipe element is not allowed")) {
  difficultyErrors.push("HARD-007 does not preserve the observed ParserError");
}
if (!parsedDifficulty[6].attempted_approaches.some(function (attempt) {
  return attempt.status === "accepted" && attempt.approach.includes("$rows = foreach") && attempt.approach.includes("pipe $rows");
})) {
  difficultyErrors.push("HARD-007 does not preserve the corrected materialize-then-pipe approach");
}
if (parsedDifficulty[6].resolution_state !== "resolved" || !parsedDifficulty[6].artifact_effect.includes("No file mutation")) {
  difficultyErrors.push("HARD-007 omits the no-mutation resolution");
}
const parsedDifficultyCsv = parseCsv(difficultyCsv);
if (canonical(parsedDifficultyCsv[0]) !== canonical(difficultyHeaders) || parsedDifficultyCsv.length !== difficultyRecords.length + 1) {
  difficultyErrors.push("Difficulty CSV header or row count mismatch");
}
for (let index = 0; index < difficultyRows.length; index += 1) {
  const projected = difficultyHeaders.map(function (header) {
    const value = difficultyRows[index][header];
    return value === null || value === undefined ? "" : String(value);
  });
  if (canonical(parsedDifficultyCsv[index + 1]) !== canonical(projected)) {
    difficultyErrors.push("Difficulty CSV projection mismatch at row " + (index + 2));
  }
}
const difficultySchemaIdentity = await fileIdentity(difficultySchemaPath);
const difficultyJsonlIdentity = await fileIdentity(difficultyJsonlPath);
const difficultyCsvIdentity = await fileIdentity(difficultyCsvPath);
const difficultyReport = {
  schema_version: SCHEMA_VERSION,
  status: difficultyErrors.length === 0 ? "PASS" : "FAIL",
  errors: difficultyErrors,
  validator: path.basename(scriptPath),
  evidence_date: "2026-08-04",
  append_only: true,
  record_count: parsedDifficulty.length,
  unique_record_count: new Set(parsedDifficulty.map(function (record) { return record.record_id; })).size,
  latest_record_id: parsedDifficulty[parsedDifficulty.length - 1].record_id,
  chain_head_sha256: parsedDifficulty[parsedDifficulty.length - 1].record_sha256,
  observed_event_ids: parsedDifficulty.map(function (record) { return record.record_id; }),
  observed_event_categories: parsedDifficulty.map(function (record) { return record.category; }),
  schema: { path: path.basename(difficultySchemaPath), bytes: difficultySchemaIdentity.bytes, sha256: difficultySchemaIdentity.sha256 },
  jsonl: { path: path.basename(difficultyJsonlPath), bytes: difficultyJsonlIdentity.bytes, sha256: difficultyJsonlIdentity.sha256 },
  csv: { path: path.basename(difficultyCsvPath), bytes: difficultyCsvIdentity.bytes, sha256: difficultyCsvIdentity.sha256 },
  review_boundary: "Observed producer metadata/tooling history only; no failures were invented and no source, Korean, formula, build, render, publication, certification, or approval finding is made.",
};
await writeJson(difficultyReportPath, difficultyReport);
assert(difficultyReport.status === "PASS", "Difficulty validation failed: " + difficultyErrors.join("; "));

const visualHeaders = [
  "schema_version",
  "visual_id",
  "work_id",
  "tranche_id",
  "unit_id",
  "visual_type",
  "parent_path_workspace_relative",
  "parent_sha256",
  "source_page",
  "bounding_box_json",
  "coordinate_basis",
  "dimensions_json",
  "dpi",
  "rotation_degrees",
  "image_path_workspace_relative",
  "image_sha256",
  "linked_structural_ids_json",
  "qa_state",
  "review_state",
  "rights_basis",
  "publication_state",
  "continuation_cursor",
];
const visualSchema = {
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:interlanguage:noether:p04:ko:visual-evidence:1.0.0",
  title: "Noether Paper 4 Korean T01--T03 visual-evidence record",
  description: "Schema for any crop, scan, page image, target render, contact sheet, before/after image, segmentation artifact, or overlay. The current JSONL is intentionally empty because no visual was used or created.",
  type: "object",
  required: visualHeaders.filter(function (header) { return !header.endsWith("_json"); }).concat(["bounding_box", "dimensions", "linked_structural_ids"]),
  properties: {
    schema_version: { const: SCHEMA_VERSION, description: "Visual schema version." },
    visual_id: { type: "string", pattern: "^CJK-KO-P04-VIS-[0-9]{3}$", description: "Stable visual identifier." },
    work_id: { const: WORK_ID, description: "Stable work identifier." },
    tranche_id: { enum: ["T01", "T02", "T03"], description: "Scoped tranche only." },
    unit_id: { enum: units.map(function (unit) { return unit.unit; }), description: "Scoped unit only." },
    visual_type: { enum: ["source_crop", "equation_crop", "diagram_crop", "page_image", "target_render", "contact_sheet", "before_after", "segmentation_artifact", "model_overlay", "other"], description: "Visual artifact class." },
    parent_path_workspace_relative: { type: ["string", "null"], description: "Optional parent scan/image path." },
    parent_sha256: { type: ["string", "null"], pattern: "^[A-F0-9]{64}$", description: "Optional parent SHA-256." },
    source_page: { type: ["integer", "null"], minimum: 1, description: "Optional physical source page." },
    bounding_box: {
      type: ["object", "null"],
      properties: { x: { type: "integer" }, y: { type: "integer" }, width: { type: "integer", minimum: 1 }, height: { type: "integer", minimum: 1 } },
      required: ["x", "y", "width", "height"],
      additionalProperties: false,
      description: "Optional pixel bounding box.",
    },
    coordinate_basis: { type: ["string", "null"], description: "Bounding-box coordinate basis." },
    dimensions: {
      type: ["object", "null"],
      properties: { width: { type: "integer", minimum: 1 }, height: { type: "integer", minimum: 1 } },
      required: ["width", "height"],
      additionalProperties: false,
      description: "Image dimensions in pixels.",
    },
    dpi: { type: ["number", "null"], minimum: 0, description: "Optional image DPI." },
    rotation_degrees: { type: ["number", "null"], description: "Optional rotation." },
    image_path_workspace_relative: { type: ["string", "null"], description: "Image path when a visual exists." },
    image_sha256: { type: ["string", "null"], pattern: "^[A-F0-9]{64}$", description: "Image SHA-256 when a visual exists." },
    linked_structural_ids: { type: "array", items: { type: "string" }, uniqueItems: true, description: "Linked structural records." },
    qa_state: { type: "string", minLength: 1, description: "Visual QA state." },
    review_state: { type: "string", minLength: 1, description: "Visual review state." },
    rights_basis: { type: "string", minLength: 1, description: "Rights basis, if any." },
    publication_state: { type: "string", minLength: 1, description: "Publication disposition." },
    continuation_cursor: { type: ["string", "null"], description: "Visual continuation cursor." },
  },
  additionalProperties: false,
  "x-csv-projection": {
    headers: visualHeaders,
    nested_json_columns: ["bounding_box_json", "dimensions_json", "linked_structural_ids_json"],
    description: "Header-only CSV is the flat projection of the intentionally empty authoritative JSONL.",
  },
};

const visualDir = path.join(evidenceRoot, "visual_evidence");
const visualSchemaPath = path.join(visualDir, "VISUAL_EVIDENCE_INDEX.schema.json");
const visualJsonlPath = path.join(visualDir, "VISUAL_EVIDENCE_INDEX.jsonl");
const visualCsvPath = path.join(visualDir, "VISUAL_EVIDENCE_INDEX.csv");
const visualReportPath = path.join(visualDir, "VISUAL_EVIDENCE_INDEX_VALIDATION_REPORT.json");
await writeJson(visualSchemaPath, visualSchema);
await writeText(visualJsonlPath, "");
await writeText(visualCsvPath, visualHeaders.join(",") + "\n");
const visualJsonlText = await fs.readFile(visualJsonlPath, "utf8");
const visualCsvRows = parseCsv(await fs.readFile(visualCsvPath, "utf8"));
const visualErrors = [];
if (visualJsonlText.length !== 0) {
  visualErrors.push("Visual JSONL must be zero bytes");
}
if (visualCsvRows.length !== 1 || canonical(visualCsvRows[0]) !== canonical(visualHeaders)) {
  visualErrors.push("Visual CSV must contain exactly the documented header");
}
const visualSchemaIdentity = await fileIdentity(visualSchemaPath);
const visualJsonlIdentity = await fileIdentity(visualJsonlPath);
const visualCsvIdentity = await fileIdentity(visualCsvPath);
const visualReport = {
  schema_version: SCHEMA_VERSION,
  status: visualErrors.length === 0 ? "PASS" : "FAIL",
  errors: visualErrors,
  validator: path.basename(scriptPath),
  evidence_date: "2026-08-04",
  record_count: 0,
  image_file_count: 0,
  source_image_count: 0,
  target_render_count: 0,
  rights_cleared_count: 0,
  rights_blocked_count: 0,
  publication_included_count: 0,
  continuation_cursor: null,
  schema: { path: path.basename(visualSchemaPath), bytes: visualSchemaIdentity.bytes, sha256: visualSchemaIdentity.sha256 },
  jsonl: { path: path.basename(visualJsonlPath), bytes: visualJsonlIdentity.bytes, sha256: visualJsonlIdentity.sha256 },
  csv: { path: path.basename(visualCsvPath), bytes: visualCsvIdentity.bytes, sha256: visualCsvIdentity.sha256 },
  validation_scope: "Schema parse plus explicit zero-byte JSONL and header-only CSV inventory.",
  excluded_scope: "No image was used or created; no visual QA, compilation, rendering, rights clearance, or publication claim.",
};
await writeJson(visualReportPath, visualReport);
assert(visualReport.status === "PASS", "Visual validation failed: " + visualErrors.join("; "));

const rootReadme = [
  "# Noether Paper 4 Korean T01--T03 reproducibility evidence",
  "",
  "This evidence freeze covers only T01-U01 through U04, T02-U05 through U09, and T03-U10 through U16. T04--T06 are out of scope even if later target files exist.",
  "",
  "- structural_index/ contains the authoritative hierarchical JSONL, its CSV projection, a field-documented schema, and a deterministic PASS report.",
  "- difficulty_ledger/ contains the append-only hash chain for the observed metadata/tooling events supplied for preservation, plus its CSV projection, schema, and PASS report.",
  "- visual_evidence/ contains a documented zero-record JSONL/CSV inventory because no visual was used or created.",
  "- csv_artifact_validation/ contains the no-render @oai/artifact-tool CSV import/inspection validator and its report.",
  "",
  "Primary structural records partition every physical line in each scoped source slice and target file exactly once. Annotation records may overlap their parent lines for footnotes, bibliography cues, authors, or tagged equations. Cross-language links use only explicit tags or same-type occurrence parity and remain unchecked.",
  "",
  "Boundary: no source/Korean/formula review, compilation, rendering, assembly, packaging, certification, approval, German patch, scan work, or SGA work is performed or implied.",
  "",
].join("\n");
await writeText(path.join(evidenceRoot, "README.md"), rootReadme);

const visualStatus = [
  "# Noether Paper 4 Korean T01--T03 visual-evidence status",
  "",
  "- State: explicit zero-record inventory.",
  "- Visuals used or created: 0.",
  "- Image files / bytes: 0 / 0.",
  "- Target renders: 0.",
  "- Rights-cleared / rights-blocked / publication-included: 0 / 0 / 0.",
  "- Absence of records is not a rights-clearance or visual-QA claim.",
  "- No compilation or rendering was performed.",
  "- Continuation cursor: none unless an independently authorized visual is actually used or created.",
  "",
].join("\n");
await writeText(path.join(visualDir, "STATUS.md"), visualStatus);

console.log(JSON.stringify({
  status: "PASS",
  structural_records: structuralParsed.length,
  structural_latest_record_id: structuralParsed[structuralParsed.length - 1].record_id,
  difficulty_records: parsedDifficulty.length,
  difficulty_latest_record_id: parsedDifficulty[parsedDifficulty.length - 1].record_id,
  difficulty_chain_head_sha256: parsedDifficulty[parsedDifficulty.length - 1].record_sha256,
  visual_records: 0,
  cursor: CURSOR,
}, null, 2));
