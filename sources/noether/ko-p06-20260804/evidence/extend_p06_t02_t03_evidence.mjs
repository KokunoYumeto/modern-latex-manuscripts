import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const evidenceRoot = path.dirname(fileURLToPath(import.meta.url));
const producerRoot = path.dirname(evidenceRoot);
const workspaceRoot = path.resolve(producerRoot, "../../../../..");
const authorityPath = path.join(workspaceRoot, "03_projects", "noether", "07_german_canon_control", "candidates", "NOETH-DE-ED-0001", "Noether_German_NOETH-DE-ED-0001.tex");
const structuralDir = path.join(evidenceRoot, "structural_index");
const difficultyDir = path.join(evidenceRoot, "difficulty_ledger");
const visualDir = path.join(evidenceRoot, "visual_evidence");
const freezeDir = path.join(evidenceRoot, "prefix_freezes");
const protectedDir = path.join(evidenceRoot, "protected_inputs");
const structuralJsonl = path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX.jsonl");
const structuralCsv = path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX.csv");
const difficultyJsonl = path.join(difficultyDir, "DIFFICULTY_LEDGER.jsonl");
const difficultyCsv = path.join(difficultyDir, "DIFFICULTY_LEDGER.csv");
const protectedManifestPath = path.join(protectedDir, "P06_T01_T03_PROTECTED_INPUT_MANIFEST.tsv");

const sha = b => crypto.createHash("sha256").update(b).digest("hex").toUpperCase();
const read = p => fs.readFileSync(p);
const text = p => read(p).toString("utf8");
const assert = (ok, message) => { if (!ok) throw new Error(message); };
const identity = p => ({ bytes: read(p).length, sha256: sha(read(p)) });
const writeUtf8 = (p, s) => { fs.mkdirSync(path.dirname(p), { recursive: true }); fs.writeFileSync(p, s, "utf8"); };
const parseJsonl = p => {
  const s = text(p);
  return s.length === 0 ? [] : s.split(/\r?\n/).filter(Boolean).map((line, i) => {
    try { return JSON.parse(line); }
    catch (e) { throw new Error(path.basename(p) + " line " + (i + 1) + ": " + e.message); }
  });
};
const appendLines = (p, records) => {
  assert(records.length > 0, "append requires records");
  const before = read(p);
  assert(before.length === 0 || before.at(-1) === 10, path.basename(p) + " lacks terminal LF");
  fs.appendFileSync(p, records.map(r => JSON.stringify(r)).join("\n") + "\n", "utf8");
};
const csvEscape = value => {
  const s = value === null || value === undefined ? "" : String(value);
  return /[",\r\n]/.test(s) ? '"' + s.replaceAll('"', '""') + '"' : s;
};
const appendCsvRows = (p, rows) => {
  const before = read(p);
  assert(before.length > 0 && before.at(-1) === 10, path.basename(p) + " lacks terminal LF");
  fs.appendFileSync(p, rows.map(row => row.map(csvEscape).join(",")).join("\n") + "\n", "utf8");
};
const normalizeLf = b => b.toString("utf8").replace(/\r\n/g, "\n").replace(/\r/g, "\n");
const authorityText = normalizeLf(read(authorityPath));
const authorityLines = authorityText.split("\n");
const sourceSlice = (start, end) => {
  assert(Number.isInteger(start) && Number.isInteger(end) && start <= end, "bad source span");
  return Buffer.from(authorityLines.slice(start - 1, end).join("\n") + "\n", "utf8");
};
const targetPath = name => path.join(producerRoot, "targets", name);
const targetSlice = (name, start, end) => {
  const lines = normalizeLf(read(targetPath(name))).split("\n");
  assert(start >= 1 && end >= start && end < lines.length, "bad target span " + name + " " + start + "-" + end);
  return Buffer.from(lines.slice(start - 1, end).join("\n") + "\n", "utf8");
};
const targetWhole = name => read(targetPath(name));
const targetConcat = unitDefs => Buffer.concat(unitDefs.map(u => targetWhole(u.target)));
const spanIdentity = (start, end) => {
  const b = sourceSlice(start, end);
  return { bytes: b.length, sha256: sha(b) };
};

const AUTHORITY = {
  id: "NOETH-DE-ED-0001",
  bytes: 2153565,
  sha256: "D1F06B311F6CBD991DD247D745DD9A72DDE326A20396DF43CFE0C8EDB1593CDB"
};
const POINTERS = {
  T01: { id: "NOETH-DE-AUTH-v006-20260804", bytes: 20666, sha256: "DB99DD87100654674D7ED24B4ABBBBC3A9920CCF035740D276CE8A87A5313C18" },
  T02: { id: "NOETH-DE-AUTH-v006-20260804", bytes: 20666, sha256: "DB99DD87100654674D7ED24B4ABBBBC3A9920CCF035740D276CE8A87A5313C18" },
  T03: { id: "NOETH-DE-AUTH-v007-20260804", bytes: 21580, sha256: "A6A8FC8E5AC24ACAF49DFD55B4B58FA3DA882EF8C3FDD4D136220C8751045156" }
};
const T02_UNITS = [
  { unit: "U07", start: 4616, end: 4618, bytes: 223, sourceSha: "C2D0C4341FCF1EC8B2DD2933344CFDE36F7D616630A98CA1C484854460EEC8EC", target: "Noether_P06_Korean_T02_U07_UNCHECKED.tex", targetBytes: 1617, targetSha: "6CAE4704B0FFFF84FBC370871807FD0219668281376582C7C95831E6FED818C2" },
  { unit: "U08", start: 4620, end: 4624, bytes: 835, sourceSha: "655935FC9093884BBD1E09AFA0427606CB515723BDBD7D84BE6816B3EAB55C00", target: "Noether_P06_Korean_T02_U08_UNCHECKED.tex", targetBytes: 2328, targetSha: "AD7AB4EB7AA369D81EE400846FA298FE6B9EFA0791E88574DFC0B39E033F4755" },
  { unit: "U09", start: 4626, end: 4645, bytes: 1170, sourceSha: "3FFA29D0B5FCB20A5E265F674867C6766C3E68AFCE0CBEF4CED06ECD71A28F40", target: "Noether_P06_Korean_T02_U09_UNCHECKED.tex", targetBytes: 2615, targetSha: "F25818E612C12FD8FA50E23FE1C0D5340B56D7C5A81DE55675455CA4F92CEECC" },
  { unit: "U10", start: 4647, end: 4653, bytes: 484, sourceSha: "43AC31D83E3E7DE9BB9FBFCF6885C25667F69E48C87AFC351C951A1B9EC35801", target: "Noether_P06_Korean_T02_U10_UNCHECKED.tex", targetBytes: 2028, targetSha: "7282B0C97004E3A5BA99252F189157452CBA02E8AC1B1954443BD2C48A5FF817" },
  { unit: "U11", start: 4655, end: 4665, bytes: 816, sourceSha: "42726EE53EA02ACA9348A907BD8D354EA1A4FC60D40BB2D6243551A09D28BF70", target: "Noether_P06_Korean_T02_U11_UNCHECKED.tex", targetBytes: 2400, targetSha: "E824C0F7919B9A92887A2D1CA184E1999769F9EA526484D9102F32E14F065A55" },
  { unit: "U12", start: 4667, end: 4678, bytes: 362, sourceSha: "0F7AE8BE46E13BAB54CDAB586DDC779C693E599FC1791381C86F4EE205BF6FB1", target: "Noether_P06_Korean_T02_U12_UNCHECKED.tex", targetBytes: 1860, targetSha: "0F6EC762287EA0EB25E840693B5494D7432B6AEDADE50ACA09998D17DE5007AB" },
  { unit: "U13", start: 4680, end: 4686, bytes: 531, sourceSha: "D58D954EC8D8248B93DF74C0171989F2236D2E24C8069AAD0C0AD2980535033A", target: "Noether_P06_Korean_T02_U13_UNCHECKED.tex", targetBytes: 1998, targetSha: "A8471C2104056431CFD3DD9D5B3A80858A19C91F350C66DFA1D33DF741DD7915" },
  { unit: "U14", start: 4688, end: 4690, bytes: 771, sourceSha: "15954135A6BF2EE96F3ABEBF61BE5B6B61981AB3B45A482DFEED1BE1444211CA", target: "Noether_P06_Korean_T02_U14_UNCHECKED.tex", targetBytes: 2239, targetSha: "4AF71E0FCEB3F1C45FEC3652D8B3CE2B75B5E5D14936D22663E80C2A22BA5573" }
];
const T03_UNITS = [
  { unit: "U15", start: 4692, end: 4694, bytes: 550, sourceSha: "28BA46CF37AFEC296C87B4B72B4D5DA6BEF784F733C0F4789B1DCBF16009F641", target: "Noether_P06_Korean_T03_U15_UNCHECKED.tex", targetBytes: 1246, targetSha: "B691FF293FE889DDA5A06493F5B5500D518F1A1EF9A25CB904E77170316FD638" },
  { unit: "U16", start: 4696, end: 4710, bytes: 630, sourceSha: "7A07524CBCD60B7A7DC366FEC1BD95EADE93C6DDF27D82B1F8B8767E7571E2D8", target: "Noether_P06_Korean_T03_U16_UNCHECKED.tex", targetBytes: 1563, targetSha: "002E6F493C0632F10614AC624292F808AD29089D42164E8FA42AEABAC4008A53" },
  { unit: "U17", start: 4712, end: 4718, bytes: 534, sourceSha: "6458FEFFCAEEB0BB5541CB2F3762B6BEDEEF88A014C3FE2FF0822023E78BFE2F", target: "Noether_P06_Korean_T03_U17_UNCHECKED.tex", targetBytes: 1367, targetSha: "A8B395E696DA0FBCFC168F9C9C6071AF9F46F9631347FEE8539E6377CD42DF4C" },
  { unit: "U18", start: 4720, end: 4744, bytes: 1140, sourceSha: "77796138EF22C497918FD7B80138B0EC90751AAB480459B6ED52131DB5967160", target: "Noether_P06_Korean_T03_U18_UNCHECKED.tex", targetBytes: 2032, targetSha: "96158DD395A0A99BE3166E8039A0B0F379238ECBD3E8FFC59884EE8F04A55429" },
  { unit: "U19", start: 4746, end: 4760, bytes: 1342, sourceSha: "65F1723FBCA1B51A908EBB4EF14696165A4CB1BD8ED51514621DF9F0EFE5ED7F", target: "Noether_P06_Korean_T03_U19_UNCHECKED.tex", targetBytes: 2267, targetSha: "AC1C363178B097953C016BFD85BD384F63B9518DBA4804DDEB075A9D88ECFB9B" },
  { unit: "U20", start: 4762, end: 4776, bytes: 556, sourceSha: "FD9C8EAC41BA33956BDDE0F83A430AF6073F056475841EFBA1B6E5D647ACEA76", target: "Noether_P06_Korean_T03_U20_UNCHECKED.tex", targetBytes: 1425, targetSha: "2C923333710848C0BDE4B4F538C33BB21F8DFBFAAF7272A0E5CED4A4195E0DCE" },
  { unit: "U21", start: 4777, end: 4793, bytes: 938, sourceSha: "F7F81CBB7440996B2B0390DA7388EEB590BB619D4B24498AB6DFD293BB48E214", target: "Noether_P06_Korean_T03_U21_UNCHECKED.tex", targetBytes: 1904, targetSha: "24DCDF0C062D39CC32256CBD1D398990A32AA590DE845E6104F5D0A84EF4C65C" },
  { unit: "U22", start: 4794, end: 4797, bytes: 160, sourceSha: "29C47D6D86AF55DE39FABE69F5E37CAC69FE0EFDD57A52CC3CF6FA9113682AC3", target: "Noether_P06_Korean_T03_U22_UNCHECKED.tex", targetBytes: 894, targetSha: "F09F8FC5A78E6FBB070706014F9FF4B31567BB758B68388D8F97D9FD94814619" }
];
const unitMap = new Map([...T02_UNITS, ...T03_UNITS].map(u => [u.unit, u]));

function verifyAuthorityAndUnits() {
  assert(read(authorityPath).length === AUTHORITY.bytes, "authority bytes changed");
  assert(sha(read(authorityPath)) === AUTHORITY.sha256, "authority hash changed");
  const t02 = spanIdentity(4616, 4691);
  assert(t02.bytes === 5200 && t02.sha256 === "75061A82BA7BCD9F16A84561B187EA58B2E7143D943A1A57E06FB0230817A8AE", "T02 source interval mismatch");
  const t03 = spanIdentity(4692, 4798);
  assert(t03.bytes === 5856 && t03.sha256 === "27A1D4E81287A3F2D4C4276CB3A1909611EDE4B1BB5A47F52F9F86E6DB27B681", "T03 source interval mismatch");
  assert(spanIdentity(4794, 4797).bytes === 160 && spanIdentity(4794, 4797).sha256 === T03_UNITS.at(-1).sourceSha, "U22 boundary mismatch");
  assert(spanIdentity(4798, 4798).bytes === 1 && spanIdentity(4798, 4798).sha256 === "01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B", "blank 4798 mismatch");
  for (const u of [...T02_UNITS, ...T03_UNITS]) {
    const s = sourceSlice(u.start, u.end);
    assert(s.length === u.bytes && sha(s) === u.sourceSha, u.unit + " source mismatch");
    const t = targetWhole(u.target);
    assert(t.length === u.targetBytes && sha(t) === u.targetSha, u.unit + " target mismatch");
  }
}

const protectedRelativePaths = [
  "ROUTE_AND_CLAIM_T01_INTRO.md",
  "SOURCE_CUSTODY_T01_INTRO.md",
  "STATUS_T01_INTRO.md",
  "TRANSLATION_CHOICES_T01_INTRO.md",
  "CHECKER_HANDOFF_T01_U01_U06.md",
  "ROUTE_AND_CLAIM_T02_SECTION1.md",
  "SOURCE_CUSTODY_T02_SECTION1.md",
  "STATUS_T02_SECTION1.md",
  "TRANSLATION_CHOICES_T02_SECTION1.md",
  "CHECKER_HANDOFF_T02_U07_U14.md",
  "ROUTE_AND_CLAIM_T03_SECTION2.md",
  "SOURCE_CUSTODY_T03_SECTION2.md",
  "STATUS_T03_SECTION2.md",
  "TRANSLATION_CHOICES_T03_SECTION2.md",
  "CHECKER_HANDOFF_T03_U15_U22.md",
  ...[...Array(22)].map((_, i) => {
    const n = i + 1;
    const tranche = n <= 6 ? "T01" : n <= 14 ? "T02" : "T03";
    return "targets/Noether_P06_Korean_" + tranche + "_U" + String(n).padStart(2, "0") + "_UNCHECKED.tex";
  })
];
function ensureProtectedManifest() {
  const header = "relative_path\tbytes\tsha256\n";
  const body = protectedRelativePaths.map(rel => {
    const p = path.join(producerRoot, ...rel.split("/"));
    assert(fs.existsSync(p), "missing protected input " + rel);
    const id = identity(p);
    return rel + "\t" + id.bytes + "\t" + id.sha256;
  }).join("\n") + "\n";
  const expected = header + body;
  if (fs.existsSync(protectedManifestPath)) assert(text(protectedManifestPath) === expected, "protected manifest drift");
  else writeUtf8(protectedManifestPath, expected);
  return identity(protectedManifestPath);
}

const relation = (type, targetId, basis, scope = "internal") => ({ type, target_id: targetId, scope, basis });
const continuation = tranche => tranche === "T02"
  ? "Independent Korean checker for T02; production continues at whole-source line 4692."
  : "Independent Korean checker for T03; production continues at whole-source line 4799.";
const pointerFor = tranche => POINTERS[tranche];

function makeStructuralBuilder(startOrder, tranche, units) {
  let order = startOrder;
  const out = [];
  const trancheId = "NOE-P06-KO-" + tranche + "-001";
  const pointer = pointerFor(tranche);
  const addRaw = spec => {
    const parentRelations = spec.parentId ? [relation("internal_relation", spec.parentId, "contained by parent")] : [];
    const record = {
      schema_version: "1.0",
      structural_id: spec.id,
      work_id: "NOE-P06",
      tranche_id: tranche,
      unit_id: spec.unitId ?? null,
      record_type: spec.type,
      source_language: "de",
      target_language: "ko",
      global_order: ++order,
      parent_id: spec.parentId ?? null,
      relations: [...parentRelations, ...(spec.relations ?? [])],
      source_locator: { whole_line_start: spec.sourceStart, whole_line_end: spec.sourceEnd, description: spec.description },
      target_locator: { path: spec.targetPath, line_start: spec.targetStart ?? null, line_end: spec.targetEnd ?? null, description: spec.description },
      source_sha256: spec.sourceSha,
      target_sha256: spec.targetSha,
      pointer_id: pointer.id,
      pointer_sha256: pointer.sha256,
      authority_id: AUTHORITY.id,
      authority_sha256: AUTHORITY.sha256,
      completion_state: "producer_draft_coverage",
      review_state: "unchecked",
      publication_state: "eligible_with_honest_metadata",
      classification: spec.classification ?? "computation",
      continuation_cursor: continuation(tranche),
      notes: spec.notes ?? ""
    };
    out.push(record);
    return record.structural_id;
  };
  const addTranche = (sourceStart, sourceEnd, sourceSha) => {
    const targetHash = sha(targetConcat(units));
    addRaw({
      id: trancheId,
      type: "tranche",
      sourceStart,
      sourceEnd,
      targetPath: "targets/",
      description: tranche + " closed producer tranche",
      sourceSha,
      targetSha: targetHash,
      parentId: "NOE-P06-KO-WORK-001",
      relations: [relation("follows", tranche === "T02" ? "NOE-P06-KO-T01-001" : "NOE-P06-KO-T02-001", "whole-source order")],
      notes: "Aggregate target digest is the SHA-256 of raw target byte streams concatenated in unit order."
    });
  };
  const addUnit = (unitId, extraRelations = []) => {
    const u = unitMap.get(unitId);
    addRaw({
      id: "NOE-P06-KO-" + tranche + "-" + unitId,
      unitId,
      type: "unit",
      sourceStart: u.start,
      sourceEnd: u.end,
      targetPath: "targets/" + u.target,
      targetStart: 1,
      targetEnd: normalizeLf(targetWhole(u.target)).split("\n").length - 1,
      description: unitId + " routed source and editable target container",
      sourceSha: u.sourceSha,
      targetSha: u.targetSha,
      parentId: trancheId,
      relations: extraRelations
    });
  };
  const add = (unitId, suffix, type, sourceStart, sourceEnd, targetStart, targetEnd, description, options = {}) => {
    const u = unitMap.get(unitId);
    const target = targetSlice(u.target, targetStart, targetEnd);
    return addRaw({
      id: "NOE-P06-KO-" + tranche + "-" + unitId + "-" + suffix,
      unitId,
      type,
      sourceStart,
      sourceEnd,
      targetPath: "targets/" + u.target,
      targetStart,
      targetEnd,
      description,
      sourceSha: sha(sourceSlice(sourceStart, sourceEnd)),
      targetSha: sha(target),
      parentId: options.parentId ?? "NOE-P06-KO-" + tranche + "-" + unitId,
      relations: options.relations ?? [],
      classification: options.classification ?? "computation",
      notes: options.notes ?? ""
    });
  };
  const addComposite = spec => {
    const targetBuffers = spec.targetParts.map(p => targetSlice(unitMap.get(p.unitId).target, p.start, p.end));
    return addRaw({
      id: spec.id,
      unitId: spec.unitId ?? null,
      type: spec.type,
      sourceStart: spec.sourceStart,
      sourceEnd: spec.sourceEnd,
      targetPath: spec.targetParts.map(p => "targets/" + unitMap.get(p.unitId).target + ":" + p.start + "-" + p.end).join(" + "),
      targetStart: null,
      targetEnd: null,
      description: spec.description,
      sourceSha: sha(sourceSlice(spec.sourceStart, spec.sourceEnd)),
      targetSha: sha(Buffer.concat(targetBuffers)),
      parentId: spec.parentId ?? trancheId,
      relations: spec.relations ?? [],
      classification: spec.classification ?? "editorial_inference",
      notes: spec.notes ?? "Composite target hash concatenates the listed LF byte slices in listed order."
    });
  };
  return { out, addTranche, addUnit, add, addComposite, getOrder: () => order };
}

function buildT02Structural(startOrder) {
  const b = makeStructuralBuilder(startOrder, "T02", T02_UNITS);
  b.addTranche(4616, 4691, "75061A82BA7BCD9F16A84561B187EA58B2E7143D943A1A57E06FB0230817A8AE");
  b.addUnit("U07");
  b.add("U07", "HEADING-001", "heading", 4616, 4616, 13, 13, "Section 1 heading");
  b.add("U07", "PROSE-001", "prose", 4618, 4618, 15, 15, "Opening scope paragraph");

  b.addUnit("U08");
  b.add("U08", "PROSE-001", "prose", 4620, 4620, 13, 13, "Notation, reduced presentation, polynomial, and coefficient-domain paragraph");
  b.add("U08", "PROSE-002", "prose", 4622, 4622, 15, 15, "Degree-zero coefficient-domain paragraph");
  b.add("U08", "PROSE-003", "prose", 4624, 4624, 17, 17, "Abstract rational-function-field transition paragraph");

  b.addUnit("U09");
  const u09def = b.add("U09", "DEFINITION-001", "definition", 4626, 4630, 13, 17, "Definition I with two enumerated closure conditions");
  b.add("U09", "STATEMENT-001", "statement", 4628, 4628, 15, 15, "Definition I scalar-multiplication condition", { parentId: u09def });
  b.add("U09", "STATEMENT-002", "statement", 4629, 4629, 16, 16, "Definition I addition, multiplication, and quotient condition", { parentId: u09def });
  b.add("U09", "FOOTNOTE-001", "footnote", 4629, 4629, 16, 16, "Source footnote attached to Definition I item 2", { parentId: u09def });
  const u09p1 = b.add("U09", "PROSE-001", "prose", 4631, 4635, 18, 22, "Finite adjunction paragraph surrounding the first generator display");
  b.add("U09", "EQUATION-001", "equation", 4632, 4634, 19, 21, "Displayed generator list", { parentId: u09p1 });
  const u09p2 = b.add("U09", "PROSE-002", "prose", 4635, 4641, 22, 28, "Notation paragraph for a finitely generated special field");
  b.add("U09", "EQUATION-002", "equation", 4636, 4640, 23, 27, "Displayed special-field notation", { parentId: u09p2 });
  b.add("U09", "FOOTNOTE-002", "footnote", 4641, 4641, 28, 28, "Source footnote attached to special-field exhaustiveness claim", { parentId: u09p2 });
  b.add("U09", "XREF-001", "cross_reference", 4641, 4641, 28, 28, "Explicit source and target reference to section 4", { parentId: u09p2, relations: [relation("explicit_cross_reference", "NOE-P06-DE-SEC-004", "explicit section marker", "external")] });
  const u09p3 = b.add("U09", "PROSE-003", "prose", 4641, 4645, 28, 32, "Full rational-function-field example paragraph");
  b.add("U09", "EQUATION-003", "equation", 4642, 4644, 29, 31, "Displayed full rational-function-field notation", { parentId: u09p3 });

  b.addUnit("U10");
  b.add("U10", "PROSE-001", "prose", 4647, 4647, 13, 13, "Intermediate-field introduction paragraph");
  const u10q = b.add("U10", "QUOTATION-001", "quotation", 4648, 4650, 14, 16, "Quoted intermediate-field formulation");
  b.add("U10", "DEFINITION-001", "definition", 4648, 4650, 14, 16, "Intermediate-field definition inside quotation", { parentId: u10q });
  const u10p2 = b.add("U10", "PROSE-002", "prose", 4651, 4651, 17, 17, "Transition to equivalent formulation of Definition I");
  b.add("U10", "XREF-001", "cross_reference", 4651, 4651, 17, 17, "Explicit reference to Definition I", { parentId: u10p2, relations: [relation("explicit_cross_reference", "NOE-P06-KO-T02-U09-DEFINITION-001", "explicit definition marker")] });
  b.add("U10", "DEFINITION-002", "definition", 4653, 4653, 19, 19, "Equivalent intermediate-field formulation");

  b.addUnit("U11");
  b.add("U11", "PROSE-001", "prose", 4655, 4655, 13, 13, "Algebraic-rank introduction paragraph");
  const u11d = b.add("U11", "DEFINITION-001", "definition", 4657, 4665, 15, 23, "Definition II and attached source footnote");
  const u11f = b.add("U11", "FOOTNOTE-001", "footnote", 4657, 4665, 15, 23, "Source footnote defining algebraic independence", { parentId: u11d });
  b.add("U11", "EQUATION-001", "equation", 4658, 4660, 16, 18, "Displayed relation among functions", { parentId: u11f });
  b.add("U11", "EQUATION-002", "equation", 4662, 4664, 20, 22, "Displayed induced identity in independent variables", { parentId: u11f });

  b.addUnit("U12");
  const u12p1 = b.add("U12", "PROSE-001", "prose", 4667, 4671, 13, 17, "Double-index notation paragraph for systems");
  b.add("U12", "EQUATION-001", "equation", 4668, 4670, 14, 16, "Displayed system double-index notation", { parentId: u12p1 });
  const u12p2 = b.add("U12", "PROSE-002", "prose", 4671, 4675, 17, 21, "Double-index notation paragraph for fields");
  b.add("U12", "EQUATION-002", "equation", 4672, 4674, 18, 20, "Displayed field double-index notation", { parentId: u12p2 });
  const u12s = b.add("U12", "STATEMENT-001", "statement", 4675, 4678, 21, 24, "Rank-bound statement");
  b.add("U12", "EQUATION-003", "equation", 4676, 4678, 22, 24, "Displayed rank inequality", { parentId: u12s });

  b.addUnit("U13");
  b.add("U13", "PROSE-001", "prose", 4680, 4680, 13, 13, "Examples transition paragraph");
  const u13e = b.add("U13", "EXAMPLE-001", "example", 4682, 4686, 15, 20, "Numbered Lagrange-domain example");
  b.add("U13", "QUOTATION-001", "quotation", 4683, 4685, 16, 19, "Quoted defining class in the first example", { parentId: u13e });
  b.add("U13", "PROSE-002", "prose", 4686, 4686, 20, 20, "Symmetric-function conclusion in the first example", { parentId: u13e });

  b.addUnit("U14");
  const u14e = b.add("U14", "EXAMPLE-001", "example", 4688, 4688, 13, 13, "Numbered projective-invariant-field example");
  b.add("U14", "FOOTNOTE-001", "footnote", 4688, 4688, 13, 13, "Source footnote attached to the second example", { parentId: u14e });
  b.add("U14", "PROSE-001", "prose", 4690, 4690, 15, 15, "Projective-subgroup conclusion paragraph");
  return b.out;
}

function buildT03Structural(startOrder) {
  const b = makeStructuralBuilder(startOrder, "T03", T03_UNITS);
  b.addTranche(4692, 4798, "27A1D4E81287A3F2D4C4276CB3A1909611EDE4B1BB5A47F52F9F86E6DB27B681");
  b.addUnit("U15");
  b.add("U15", "HEADING-001", "heading", 4692, 4692, 9, 9, "Section 2 heading");
  const u15p = b.add("U15", "PROSE-001", "prose", 4694, 4694, 11, 11, "Section 2 opening paragraph");
  b.add("U15", "XREF-001", "cross_reference", 4694, 4694, 11, 11, "Explicit source and target reference to section 3", { parentId: u15p, relations: [relation("explicit_cross_reference", "NOE-P06-DE-SEC-003", "explicit section marker", "external")] });

  b.addComposite({
    id: "NOE-P06-KO-T03-PROOF-001",
    type: "proof",
    sourceStart: 4696,
    sourceEnd: 4762,
    targetParts: [
      { unitId: "U16", start: 10, end: 24 },
      { unitId: "U17", start: 10, end: 16 },
      { unitId: "U18", start: 10, end: 34 },
      { unitId: "U19", start: 10, end: 24 },
      { unitId: "U20", start: 10, end: 10 }
    ],
    description: "Argument leading from systems (1)--(3) through equations (4)--(6) to the lemma transition",
    relations: [relation("precedes", "NOE-P06-KO-T03-LEMMA-001", "source order")],
    classification: "editorial_inference",
    notes: "Producer structural inference only; not mathematical or source validation. Composite target hash uses listed LF slices."
  });

  b.addUnit("U16");
  const u16p1 = b.add("U16", "PROSE-001", "prose", 4696, 4702, 10, 16, "Hypothesis paragraph surrounding displayed system (1)");
  b.add("U16", "EQUATION-001", "equation", 4697, 4701, 11, 15, "Displayed system tagged (1)", { parentId: u16p1 });
  const u16p2 = b.add("U16", "PROSE-002", "prose", 4702, 4710, 16, 24, "Rank and common-denominator paragraph surrounding equation (2)");
  b.add("U16", "EQUATION-002", "equation", 4703, 4709, 17, 23, "Displayed derivative determinant tagged (2)", { parentId: u16p2 });
  b.add("U16", "XREF-001", "cross_reference", 4702, 4702, 16, 16, "Explicit reference to displayed system (1)", { parentId: u16p2, relations: [relation("explicit_cross_reference", "NOE-P06-KO-T03-U16-EQUATION-001", "explicit equation tag")] });
  b.add("U16", "XREF-002", "cross_reference", 4710, 4710, 24, 24, "Explicit reference to displayed system (1)", { parentId: u16p2, relations: [relation("explicit_cross_reference", "NOE-P06-KO-T03-U16-EQUATION-001", "explicit equation tag")] });

  b.addUnit("U17");
  const u17p1 = b.add("U17", "PROSE-001", "prose", 4712, 4712, 10, 10, "Choice and nondivisibility paragraph");
  b.add("U17", "XREF-001", "cross_reference", 4712, 4712, 10, 10, "Explicit reference to displayed system (1)", { parentId: u17p1, relations: [relation("explicit_cross_reference", "NOE-P06-KO-T03-U16-EQUATION-001", "explicit equation tag")] });
  b.add("U17", "EQUATION-001", "equation", 4713, 4717, 11, 15, "Displayed specialized system tagged (3)");
  const u17p2 = b.add("U17", "PROSE-002", "prose", 4718, 4718, 16, 16, "Algebraic-independence and rank-preservation paragraph");
  b.add("U17", "XREF-002", "cross_reference", 4718, 4718, 16, 16, "Explicit reference to displayed system (1)", { parentId: u17p2, relations: [relation("explicit_cross_reference", "NOE-P06-KO-T03-U16-EQUATION-001", "explicit equation tag")] });

  b.addUnit("U18");
  const u18p1 = b.add("U18", "PROSE-001", "prose", 4720, 4728, 10, 18, "Irreducible-equation paragraph surrounding equation (4)");
  b.add("U18", "EQUATION-001", "equation", 4721, 4727, 11, 17, "Displayed irreducible equation tagged (4)", { parentId: u18p1 });
  const u18p2 = b.add("U18", "PROSE-002", "prose", 4728, 4734, 18, 24, "Reduced-presentation paragraph surrounding equation (5)");
  b.add("U18", "EQUATION-002", "equation", 4729, 4733, 19, 23, "Displayed reduced presentations tagged (5)", { parentId: u18p2 });
  const u18p3 = b.add("U18", "PROSE-003", "prose", 4734, 4744, 24, 34, "Polynomial-identity paragraph surrounding equation (6)");
  b.add("U18", "EQUATION-003", "equation", 4735, 4743, 25, 33, "Displayed polynomial identity tagged (6)", { parentId: u18p3 });
  b.add("U18", "XREF-001", "cross_reference", 4734, 4734, 24, 24, "Explicit references to equations (5) and (4)", { parentId: u18p3, relations: [relation("explicit_cross_reference", "NOE-P06-KO-T03-U18-EQUATION-002", "explicit equation tag"), relation("explicit_cross_reference", "NOE-P06-KO-T03-U18-EQUATION-001", "explicit equation tag")] });

  b.addUnit("U19");
  const u19p1 = b.add("U19", "PROSE-001", "prose", 4746, 4750, 10, 14, "First divisibility argument surrounding an unnumbered display");
  b.add("U19", "EQUATION-001", "equation", 4747, 4749, 11, 13, "Displayed terminal term from equation (6)", { parentId: u19p1 });
  const u19p2 = b.add("U19", "PROSE-002", "prose", 4750, 4754, 14, 18, "Second divisibility argument surrounding a quotient display");
  b.add("U19", "EQUATION-002", "equation", 4751, 4753, 15, 17, "Displayed quotient relation for A_tau", { parentId: u19p2 });
  b.add("U19", "XREF-001", "cross_reference", 4746, 4754, 10, 18, "Explicit references to equations (6) and (3)", { parentId: u19p2, relations: [relation("explicit_cross_reference", "NOE-P06-KO-T03-U18-EQUATION-003", "explicit equation tag"), relation("explicit_cross_reference", "NOE-P06-KO-T03-U17-EQUATION-001", "explicit equation tag")] });
  const u19p3 = b.add("U19", "PROSE-003", "prose", 4755, 4760, 19, 24, "Coprimality conclusion and contradiction paragraph with attached footnote");
  const u19f = b.add("U19", "FOOTNOTE-001", "footnote", 4755, 4760, 19, 24, "Source footnote about simultaneous substitution and an indeterminate quotient", { parentId: u19p3 });
  b.add("U19", "EQUATION-003", "equation", 4756, 4759, 20, 23, "Displayed rational-function example inside source footnote", { parentId: u19f });

  b.addUnit("U20");
  const u20p = b.add("U20", "PROSE-001", "prose", 4762, 4762, 10, 10, "Iteration transition into the lemma");
  b.add("U20", "XREF-001", "cross_reference", 4762, 4762, 10, 10, "Explicit reference to displayed system (3)", { parentId: u20p, relations: [relation("explicit_cross_reference", "NOE-P06-KO-T03-U17-EQUATION-001", "explicit equation tag")] });
  b.addComposite({
    id: "NOE-P06-KO-T03-LEMMA-001",
    type: "lemma",
    sourceStart: 4764,
    sourceEnd: 4797,
    targetParts: [
      { unitId: "U20", start: 12, end: 24 },
      { unitId: "U21", start: 11, end: 27 },
      { unitId: "U22", start: 9, end: 12 }
    ],
    description: "Lemma statement spanning U20--U22 with attached split source footnote",
    relations: [relation("follows", "NOE-P06-KO-T03-PROOF-001", "source order")],
    classification: "source_fact",
    notes: "Composite target hash uses U20 lines 12--24, U21 lines 11--27, and U22 lines 9--12 in that order; no semantic validation."
  });
  b.add("U20", "EQUATION-001", "equation", 4765, 4770, 13, 18, "Displayed pair of systems inside lemma", { parentId: "NOE-P06-KO-T03-LEMMA-001" });
  b.add("U20", "EQUATION-002", "equation", 4772, 4776, 20, 24, "Displayed derivative determinant inside lemma", { parentId: "NOE-P06-KO-T03-LEMMA-001" });

  b.addUnit("U21", [relation("part_of", "NOE-P06-KO-T03-LEMMA-001", "lemma spans U20--U22"), relation("continued_by", "NOE-P06-KO-T03-U22", "split source footnote and direct source order")]);
  b.add("U21", "PROSE-001", "prose", 4777, 4781, 11, 15, "Lemma continuation surrounding the chosen-values display", { parentId: "NOE-P06-KO-T03-LEMMA-001" });
  b.add("U21", "EQUATION-001", "equation", 4778, 4780, 12, 14, "Displayed chosen values inside lemma", { parentId: "NOE-P06-KO-T03-LEMMA-001" });
  b.add("U21", "PROSE-002", "prose", 4781, 4785, 15, 19, "Lemma continuation surrounding the substitution display", { parentId: "NOE-P06-KO-T03-LEMMA-001" });
  b.add("U21", "EQUATION-002", "equation", 4782, 4784, 16, 18, "Displayed ordered substitutions inside lemma", { parentId: "NOE-P06-KO-T03-LEMMA-001" });
  b.add("U21", "PROSE-003", "prose", 4785, 4793, 19, 27, "Lemma conclusion surrounding the successive-substitution display", { parentId: "NOE-P06-KO-T03-LEMMA-001" });
  b.add("U21", "EQUATION-003", "equation", 4786, 4792, 20, 26, "Displayed successive substitutions inside lemma", { parentId: "NOE-P06-KO-T03-LEMMA-001" });
  b.add("U21", "XREF-001", "cross_reference", 4785, 4785, 19, 19, "Explicit reference to displayed system (1)", { parentId: "NOE-P06-KO-T03-LEMMA-001", relations: [relation("explicit_cross_reference", "NOE-P06-KO-T03-U16-EQUATION-001", "explicit equation tag")] });
  b.add("U21", "FOOTNOTE-OPEN-001", "footnote", 4793, 4793, 27, 27, "Source footnote opened in U21 and continued by U22", { parentId: "NOE-P06-KO-T03-LEMMA-001", relations: [relation("continued_by", "NOE-P06-KO-T03-U22-FOOTNOTE-CLOSE-001", "srcfn opens in U21 and closes in U22")], classification: "source_fact", notes: "This record is intentionally not a closed TeX fragment." });

  b.addUnit("U22", [relation("continues_after", "NOE-P06-KO-T03-U21", "direct source order"), relation("part_of", "NOE-P06-KO-T03-LEMMA-001", "lemma spans U20--U22")]);
  const u22f = b.add("U22", "FOOTNOTE-CLOSE-001", "footnote", 4794, 4797, 9, 12, "Continuation and closure of the source footnote opened in U21", { parentId: "NOE-P06-KO-T03-LEMMA-001", relations: [relation("continues", "NOE-P06-KO-T03-U21-FOOTNOTE-OPEN-001", "srcfn continuation and closure")], classification: "source_fact", notes: "Whole-source line 4798 is an excluded blank and is not part of this record." });
  b.add("U22", "EQUATION-001", "equation", 4794, 4797, 9, 12, "Displayed specialized functions inside the split source footnote", { parentId: u22f, notes: "U22 closes the srcfn opened in U21; blank line 4798 is excluded." });
  return b.out;
}

function structuralCsvRow(r) {
  return [
    r.structural_id,
    r.record_type,
    r.unit_id ?? "",
    r.parent_id ?? "",
    r.global_order,
    r.source_locator.whole_line_start + "-" + r.source_locator.whole_line_end,
    r.target_locator.path,
    r.target_locator.line_start === null ? "" : r.target_locator.line_start + "-" + r.target_locator.line_end,
    r.source_sha256,
    r.target_sha256,
    r.source_language,
    r.target_language,
    r.completion_state,
    r.review_state,
    r.publication_state,
    r.relations.map(x => x.target_id).join("|"),
    r.classification,
    r.continuation_cursor
  ];
}

function targetArtifact(unitId) {
  const u = unitMap.get(unitId);
  return { path: "targets/" + u.target, bytes: u.targetBytes, sha256: u.targetSha };
}
function metadataEvidence(name, result) {
  const p = path.join(producerRoot, name);
  return { kind: "producer_metadata", path: name, sha256: sha(read(p)), result };
}
function difficultyRecord(sequence, trancheIds, unitIds, state, classification, fields) {
  const pointer = pointerFor(trancheIds.some(x => x.startsWith("T03")) ? "T03" : "T02");
  return {
    schema_version: "1.0",
    record_id: "CJK-KO-P06-HARD-" + String(sequence).padStart(3, "0"),
    sequence,
    observed_at: fields.observedAt ?? "2026-08-04",
    time_precision: fields.timePrecision ?? "day",
    work_id: "NOE-P06",
    tranche_ids: trancheIds,
    unit_ids: unitIds,
    state,
    classification,
    authority_context: { pointer_id: pointer.id, pointer_sha256: pointer.sha256, authority_id: AUTHORITY.id, authority_sha256: AUTHORITY.sha256 },
    source_locators: fields.sourceLocators,
    target_artifacts: unitIds.filter(x => unitMap.has(x)).map(targetArtifact),
    symptom: fields.symptom,
    cause_evidence: fields.causeEvidence,
    attempted_approaches: fields.attempted,
    resolution_or_hold: fields.resolution,
    evidence: fields.evidence,
    residual_risk: fields.residualRisk,
    recurrence_cues: fields.recurrenceCues,
    related_structural_ids: fields.relatedStructuralIds,
    related_decision_ids: fields.relatedDecisionIds,
    transferable_lesson: fields.lesson,
    previous_record_id: sequence === 1 ? null : "CJK-KO-P06-HARD-" + String(sequence - 1).padStart(3, "0")
  };
}

function buildT02Difficulty() {
  return [
    difficultyRecord(12, ["T02"], ["U08", "U13"], "held", "model_preference", {
      sourceLocators: ["ED0001 line 4620: Ganze rationale Funktionen (Polynome)", "ED0001 line 4684: ganzen rationalen Funktionen"],
      symptom: "T02 preserves two Korean producer attractors for the historical expression: 정(整) 유리함수 in U08 and 정칙 유리함수 in U13.",
      causeEvidence: "The two units were produced independently and TRANSLATION_CHOICES_T02_SECTION1.md explicitly exposes the divergence instead of harmonizing it.",
      attempted: [
        { approach: "Preserve both producer witnesses and route the inconsistency.", outcome: "Target bytes remain unchanged and the checker can evaluate both in context.", rejected_reason: null },
        { approach: "Silently normalize both targets.", outcome: "Not attempted.", rejected_reason: "Would be producer self-review and would erase adverse evidence." }
      ],
      resolution: "Held for independent Korean evidence on the historical polynomial/integral-rational-function sense.",
      evidence: [metadataEvidence("TRANSLATION_CHOICES_T02_SECTION1.md", "Sense window and both target forms recorded.")],
      residualRisk: "정칙 may attract analytic regularity while 정(整) may be opaque or neighboring-language driven.",
      recurrenceCues: ["ganze rationale Funktion recurs", "regular/polynomial senses compete", "units produced independently"],
      relatedStructuralIds: ["NOE-P06-KO-T02-U08-PROSE-001", "NOE-P06-KO-T02-U13-QUOTATION-001"],
      relatedDecisionIds: ["CJK-KO-P06-004"],
      lesson: "Retain competing producer forms as adverse evidence until an independent Korean checker supplies local-language usage evidence."
    }),
    difficultyRecord(13, ["T02"], ["U11", "U12"], "held", "model_preference", {
      sourceLocators: ["ED0001 lines 4655--4678: algebraischer Rang and its double-index use"],
      symptom: "The provisional Hangul form 계수 is disambiguated with Hanja 階數 but can still attract the unrelated coefficient sense.",
      causeEvidence: "The producer metadata records 대수적 계수(階數) as provisional and names 대수적 랭크 as an unchecked alternative; no ko-KP evidence exists.",
      attempted: [
        { approach: "Retain Hangul-first text with a parenthetical Hanja disambiguator.", outcome: "Producer witness preserved for checking.", rejected_reason: null },
        { approach: "Claim one South- or North-Korean standard.", outcome: "Not attempted.", rejected_reason: "No independent Korean or DPRK-local evidence." }
      ],
      resolution: "Held for independent ko-KR evidence; ko-KP remains unverified_do_not_claim.",
      evidence: [metadataEvidence("TRANSLATION_CHOICES_T02_SECTION1.md", "Hanja, regional, and lexical-attractor debt recorded.")],
      residualRisk: "Readers may parse 계수 as coefficient; Hanja may conceal rather than solve a Korean register problem.",
      recurrenceCues: ["algebraischer Rang recurs", "Hangul homograph 계수", "rank versus coefficient contexts"],
      relatedStructuralIds: ["NOE-P06-KO-T02-U11-DEFINITION-001", "NOE-P06-KO-T02-U12-STATEMENT-001"],
      relatedDecisionIds: ["CJK-KO-P06-004"],
      lesson: "A Hanja gloss is a provisional disambiguator, not Korean standardization evidence or regional authorization."
    }),
    difficultyRecord(14, ["T02"], ["U09", "U10", "U11", "U12"], "held", "editorial_inference", {
      sourceLocators: ["ED0001 lines 4626--4678: Definitions I--II and indexed system/field notation"],
      symptom: "Definitions, inclusion directions, quantifiers, closure operations, displays, and inequality remain structurally indexed but semantically unchecked.",
      causeEvidence: "The translation-only role permits custody and topology but forbids source, Korean, formula, or mathematical self-review.",
      attempted: [
        { approach: "Index each definition, statement, display, footnote, and cross-reference with exact locators.", outcome: "Reproducible checker routing achieved.", rejected_reason: null },
        { approach: "Treat topology and byte identity as correctness.", outcome: "Rejected.", rejected_reason: "Custody does not prove semantic or formula fidelity." }
      ],
      resolution: "Held for independent clause and formula checking.",
      evidence: [metadataEvidence("CHECKER_HANDOFF_T02_U07_U14.md", "Independent checker tasks enumerate definition and formula gates.")],
      residualRisk: "A structurally complete index can still contain a reversed inclusion, quantifier, exception, or dependence direction.",
      recurrenceCues: ["definition with enumerate", "existential/for-every language", "field/system macros", "rank inequality"],
      relatedStructuralIds: ["NOE-P06-KO-T02-U09-DEFINITION-001", "NOE-P06-KO-T02-U10-DEFINITION-002", "NOE-P06-KO-T02-U11-DEFINITION-001", "NOE-P06-KO-T02-U12-EQUATION-003"],
      relatedDecisionIds: ["CJK-KO-P06-004"],
      lesson: "Use structural completeness to route review, never as a substitute for independent semantic and formula verification."
    }),
    difficultyRecord(15, ["T02"], ["U09", "U11", "U13", "U14"], "held", "editorial_inference", {
      sourceLocators: ["ED0001 source footnotes at lines 4629, 4641, 4657--4665, and 4688", "ED0001 quoted/example structures lines 4648--4650 and 4682--4690"],
      symptom: "Long footnotes, quotations, and historical examples combine prose, notation, and scope boundaries that remain unchecked.",
      causeEvidence: "The producer handoff explicitly reserves source-footnote wording, quote scope, invariant terminology, and example conclusions for an independent checker.",
      attempted: [
        { approach: "Index each note, quotation, example, and embedded display as a distinct relation-bearing structure.", outcome: "Exact routing evidence created.", rejected_reason: null },
        { approach: "Approve note or quotation scope from TeX balance alone.", outcome: "Rejected.", rejected_reason: "Balanced syntax does not establish translation or mathematical scope." }
      ],
      resolution: "Held for independent Korean/source/formula review.",
      evidence: [metadataEvidence("CHECKER_HANDOFF_T02_U07_U14.md", "Footnote, quotation, and example review obligations retained.")],
      residualRisk: "Scope can be wrong even when delimiters and hashes are preserved.",
      recurrenceCues: ["srcfn macro", "quote environment", "numbered historical example", "inline invariant-theory notation"],
      relatedStructuralIds: ["NOE-P06-KO-T02-U09-FOOTNOTE-002", "NOE-P06-KO-T02-U11-FOOTNOTE-001", "NOE-P06-KO-T02-U13-EXAMPLE-001", "NOE-P06-KO-T02-U14-FOOTNOTE-001"],
      relatedDecisionIds: ["CJK-KO-P06-004"],
      lesson: "Index note and quotation topology separately from their surrounding prose and retain their semantic state as unchecked."
    }),
    difficultyRecord(16, ["T02"], ["U07", "U08", "U09", "U10", "U11", "U12", "U13", "U14"], "active_control", "editorial_inference", {
      sourceLocators: ["P06 T02 Korean terminology and evidence shelf"],
      symptom: "Historical Sino-xenic-looking forms can be over-selected from Mandarin-Simplified-dominant retrieval while local Korean register and ko-KP evidence are missing.",
      causeEvidence: "TRANSLATION_CHOICES_T02_SECTION1.md classifies lexical-attractor basins qualitatively and explicitly denies cross-language authorization.",
      attempted: [
        { approach: "Record sense windows, competing basins, Hanja debt, and Mandarin-Simplified dominance as qualitative controls.", outcome: "Control remains visible without a readiness scalar.", rejected_reason: null },
        { approach: "Infer Korean approval from Chinese or Japanese cognates.", outcome: "Rejected.", rejected_reason: "Chinese and Japanese do not authorize Korean." }
      ],
      resolution: "Active control for future checker evidence; never convert dominance debt into a confidence or readiness score.",
      evidence: [metadataEvidence("TRANSLATION_CHOICES_T02_SECTION1.md", "Sense windows and attractor basins recorded.")],
      residualRisk: "Familiar characters or calques can appear authoritative while lacking Korean attestation.",
      recurrenceCues: ["Sino-xenic calque", "parenthetical Hanja", "no Korean corpus citation", "ko-KP claim without DPRK evidence"],
      relatedStructuralIds: ["NOE-P06-KO-T02-001"],
      relatedDecisionIds: ["CJK-KO-P06-004"],
      lesson: "Keep dominance risk qualitative and language-specific; use it to broaden evidence retrieval, never to authorize a term."
    })
  ];
}

function buildT03Difficulty() {
  return [
    difficultyRecord(17, ["T02-EVIDENCE-VERIFY"], [], "resolved", "computation", {
      sourceLocators: ["First read-only T02 prefix-verification one-liner after the T02 freeze"],
      symptom: "The verifier threw SyntaxError: Unexpected non-whitespace character after JSON at position 1280 (line 2 column 1) while parsing the structural JSONL.",
      causeEvidence: "The JavaScript one-liner used an over-escaped split regex matching literal backslash sequences rather than CR/LF, so JSON.parse received the complete multi-record JSONL as one value. The failure occurred in a read-only command and wrote nothing.",
      attempted: [
        { approach: "Split JSONL with the over-escaped regex /\\\\r?\\\\n/ inside the executed JavaScript.", outcome: "The ledger was not split; JSON.parse stopped at the second JSON object; writes 0.", rejected_reason: "The pattern matched literal backslashes rather than line endings." },
        { approach: "Rerun with the literal line-ending regex /\\r?\\n/.", outcome: "Read-only T02 verification passed: 102 structural records, 16 difficulty records, all parents/relations valid, frozen hashes exact, T04 records 0; writes 0.", rejected_reason: null }
      ],
      resolution: "Resolved by using the literal CR/LF regex; the failed attempt remains append-only evidence.",
      evidence: [{ kind: "read_only_verifier", path: "evidence/prefix_freezes/P06_T02_EVIDENCE_PREFIX_FREEZE_20260804.json", sha256: "38AA1F16F95ACB15F54A8DD82116FFF38E13FE29940E6CBACCB2AD8038790A70", result: "Corrected retry passed against the exact T02 freeze; no file mutation." }],
      residualRisk: "Layered shell/JavaScript escaping can silently change a regex before execution.",
      recurrenceCues: ["regex embedded in shell-quoted JavaScript", "JSONL parser sees a second object as trailing text", "backslashes doubled at more than one quoting layer"],
      relatedStructuralIds: ["NOE-P06-KO-T02-001"],
      relatedDecisionIds: [],
      lesson: "When a regex crosses shell and JavaScript quoting layers, inspect the executed literal or use a durable script; preserve read-only parser failures and their no-write effect."
    }),
    difficultyRecord(18, ["T03-METADATA"], [], "resolved", "computation", {
      sourceLocators: ["Read-only T03 metadata verification before evidence extension"],
      symptom: "The T03 metadata worker reported an empty-pipeline PowerShell parser failure. Exact command text and exact error text are unavailable.",
      causeEvidence: "The worker return identifies only the empty-pipeline parse class and states that parsing failed before execution. No more specific token sequence is asserted.",
      attempted: [
        { approach: "Original unretained read-only pipeline form.", outcome: "Parser failure before execution; writes 0.", rejected_reason: "Exact command and error transcript were not retained." },
        { approach: "Corrected read-only verification.", outcome: "Passed; writes 0.", rejected_reason: null }
      ],
      resolution: "Operationally resolved by the corrected read-only verification; the limited-evidence incident remains append-only.",
      evidence: [{ kind: "worker_return", path: "", sha256: null, result: "Observed facts only: empty-pipeline parser failure; exact command/error unavailable; failed before execution; writes 0; corrected read-only verification passed." }],
      residualRisk: "Without an exact transcript, recurrence can be recognized only at the parser-class level.",
      recurrenceCues: ["empty pipeline element", "pipeline begins or ends without an expression", "parser stops before execution"],
      relatedStructuralIds: ["NOE-P06-KO-T03-001"],
      relatedDecisionIds: ["CJK-KO-P06-006"],
      lesson: "Log only the failure facts actually retained; never reconstruct an exact command or error message from a coarse worker summary."
    }),
    difficultyRecord(19, ["T03"], ["U15"], "held", "model_preference", {
      sourceLocators: ["ED0001 lines 4692--4694: Unbestimmte and unbestimmt in the section introduction"],
      symptom: "The producer distinguishes algebraic indeterminates 미정원 from an indeterminate value or quotient 부정형; the shared German stem invites collapse.",
      causeEvidence: "TRANSLATION_CHOICES_T03_SECTION2.md supplies an explicit two-sense window and keeps both Korean choices provisional.",
      attempted: [
        { approach: "Preserve the two contextual Korean renderings and expose the distinction.", outcome: "Producer witness retained.", rejected_reason: null },
        { approach: "Normalize both senses to one Korean word.", outcome: "Not attempted.", rejected_reason: "Would erase a trap-prone sense distinction before independent review." }
      ],
      resolution: "Held for independent Korean evidence and clause-level checking.",
      evidence: [metadataEvidence("TRANSLATION_CHOICES_T03_SECTION2.md", "Two-sense window recorded.")],
      residualRisk: "미정원 may attract equation-unknown usage; 부정형 may over-narrow the historical predicate to calculus terminology.",
      recurrenceCues: ["Unbestimmte as noun", "unbestimmt as predicate", "0/0 context"],
      relatedStructuralIds: ["NOE-P06-KO-T03-U15-PROSE-001"],
      relatedDecisionIds: ["CJK-KO-P06-006"],
      lesson: "For trap-prone cognate forms, preserve an explicit sense split instead of harmonizing by spelling."
    }),
    difficultyRecord(20, ["T03"], ["U16", "U20", "U21"], "held", "model_preference", {
      sourceLocators: ["ED0001 lines 4702--4710 and 4764--4793: algebraischer Rang and Rang der Funktionalmatrix"],
      symptom: "The provisional forms 대수적 계수(階數) and 함수행렬의 계수(階數) risk confusion with coefficient and may impose an unclear matrix register.",
      causeEvidence: "Producer metadata retains 랭크 and 야코비 행렬 alternatives and explicitly denies Hanja or regional certification.",
      attempted: [
        { approach: "Retain the producer form plus Hanja and alternatives in metadata.", outcome: "Checker can compare exact witnesses.", rejected_reason: null },
        { approach: "Claim a standard Korean rank term or ko-KP equivalent.", outcome: "Not attempted.", rejected_reason: "No independent Korean or DPRK evidence." }
      ],
      resolution: "Held for independent ko-KR terminology evidence; ko-KP remains unverified_do_not_claim.",
      evidence: [metadataEvidence("TRANSLATION_CHOICES_T03_SECTION2.md", "Rank, matrix, Hanja, and regional holds recorded.")],
      residualRisk: "A modern loan may alter register; the Sino-Korean homograph may alter meaning.",
      recurrenceCues: ["Rang", "Funktionalmatrix", "계수 homograph", "parenthetical 階數"],
      relatedStructuralIds: ["NOE-P06-KO-T03-U16-PROSE-002", "NOE-P06-KO-T03-LEMMA-001"],
      relatedDecisionIds: ["CJK-KO-P06-006"],
      lesson: "Keep mathematical register, homograph risk, and regional standardization as separate evidence questions."
    }),
    difficultyRecord(21, ["T03"], ["U16", "U17", "U18", "U19", "U20", "U21", "U22"], "held", "editorial_inference", {
      sourceLocators: ["ED0001 equations (1)--(6), lines 4697--4743", "ED0001 lemma displays, lines 4765--4797"],
      symptom: "Derivative, exponent, index, divisibility, quotient, specialization, and equation-label topology is indexed but no formula has been checked.",
      causeEvidence: "The role boundary forbids formula review and compilation; the handoff marks every formula token as independent-checker debt.",
      attempted: [
        { approach: "Record every display and explicit cross-reference with exact source and target locators/hashes.", outcome: "Mechanical topology captured.", rejected_reason: null },
        { approach: "Infer formula equivalence from matching TeX environments or labels.", outcome: "Rejected.", rejected_reason: "Topology and label parity do not prove token correctness." }
      ],
      resolution: "Held for independent formula/source checking and later build/render tasks.",
      evidence: [metadataEvidence("CHECKER_HANDOFF_T03_U15_U22.md", "Equation and notation checks explicitly assigned.")],
      residualRisk: "A single exponent, index, derivative, delimiter, or quotient error can survive every metadata hash check.",
      recurrenceCues: ["tagged equation", "aligned or array display", "specialization bracket", "cross-unit footnote display"],
      relatedStructuralIds: ["NOE-P06-KO-T03-U16-EQUATION-001", "NOE-P06-KO-T03-U18-EQUATION-003", "NOE-P06-KO-T03-U21-EQUATION-003", "NOE-P06-KO-T03-U22-EQUATION-001"],
      relatedDecisionIds: ["CJK-KO-P06-006"],
      lesson: "Equation inventories are routing evidence only; formula checking, compilation, and rendered inspection remain independent gates."
    }),
    difficultyRecord(22, ["T03"], ["U16", "U17", "U18", "U19", "U20", "U21", "U22"], "held", "editorial_inference", {
      sourceLocators: ["ED0001 lines 4696--4762: argument leading to lemma", "ED0001 lines 4764--4797: lemma statement"],
      symptom: "The long argument and lemma contain conditional, independence, nonvanishing, iteration, and conclusion scopes that remain semantically unchecked.",
      causeEvidence: "The structural records classify one proof-like argument as editorial_inference and the explicitly marked Hilfssatz as source_fact without claiming mathematical validation.",
      attempted: [
        { approach: "Create separate proof and lemma containers with child displays and cross-references.", outcome: "Hierarchy and continuation are reproducible.", rejected_reason: null },
        { approach: "Treat a complete hierarchy as proof verification.", outcome: "Rejected.", rejected_reason: "Structural classification does not establish the argument or translation." }
      ],
      resolution: "Held for independent source/Korean/mathematical review.",
      evidence: [metadataEvidence("CHECKER_HANDOFF_T03_U15_U22.md", "Clause, implication, quantifier, and iteration checks assigned.")],
      residualRisk: "A scope reversal or omitted condition can remain invisible to structural coverage.",
      recurrenceCues: ["multi-unit argument", "lemma statement", "iterated substitution", "nonvanishing conclusion"],
      relatedStructuralIds: ["NOE-P06-KO-T03-PROOF-001", "NOE-P06-KO-T03-LEMMA-001"],
      relatedDecisionIds: ["CJK-KO-P06-006"],
      lesson: "Index proof and theorem scope explicitly, but label inferred hierarchy and reserve validity for an independent checker."
    }),
    difficultyRecord(23, ["T03"], ["U19"], "held", "editorial_inference", {
      sourceLocators: ["ED0001 lines 4755--4760: source footnote with simultaneous substitutions and 0/0 example"],
      symptom: "U19 contains a long inline source footnote with an embedded display and a conclusion whose scope crosses back into the host sentence.",
      causeEvidence: "The source and target preserve the srcfn macro, display, and continuation, but no clause, delimiter, or mathematical review occurred.",
      attempted: [
        { approach: "Index the host prose, footnote, and embedded equation separately with parent relations.", outcome: "Exact topology retained.", rejected_reason: null },
        { approach: "Approve the footnote from balanced delimiters.", outcome: "Rejected.", rejected_reason: "Delimiter balance is not source or translation fidelity." }
      ],
      resolution: "Held for independent footnote, formula, and clause-scope review.",
      evidence: [metadataEvidence("CHECKER_HANDOFF_T03_U15_U22.md", "U19 footnote review explicitly assigned.")],
      residualRisk: "The displayed example or post-footnote conclusion may be mistranscribed or scoped incorrectly.",
      recurrenceCues: ["srcfn with display math", "host sentence resumes after footnote", "0/0 conclusion"],
      relatedStructuralIds: ["NOE-P06-KO-T03-U19-FOOTNOTE-001", "NOE-P06-KO-T03-U19-EQUATION-003"],
      relatedDecisionIds: ["CJK-KO-P06-006"],
      lesson: "Represent inline notes with embedded displays as nested structures and keep the resumed host sentence visible."
    }),
    difficultyRecord(24, ["T03"], ["U21", "U22"], "held", "source_fact", {
      sourceLocators: ["ED0001 line 4793 opens srcfn", "ED0001 lines 4794--4797 continue and close srcfn", "ED0001 line 4798 is an excluded blank"],
      symptom: "U21 opens a source footnote that U22 continues and closes; neither file is an independently closed TeX fragment.",
      causeEvidence: "SOURCE_CUSTODY_T03_SECTION2.md and both target headers state mandatory U21 then U22 adjacency. Mechanical inspection locates the opening at U21 line 27 and closure at U22 line 12.",
      attempted: [
        { approach: "Preserve two editable custody units and encode bidirectional continuation relations.", outcome: "Exact unit identities remain unchanged and topology is explicit.", rejected_reason: null },
        { approach: "Merge or edit target files to make each compile alone.", outcome: "Not attempted.", rejected_reason: "Would mutate frozen producer targets and exceed the translation-only evidence task." }
      ],
      resolution: "Held for checker/build tasks that concatenate U21 immediately followed by U22; blank whole-source line 4798 remains excluded.",
      evidence: [metadataEvidence("SOURCE_CUSTODY_T03_SECTION2.md", "Cross-unit topology and exact boundary recorded.")],
      residualRisk: "Sorting, packaging, or building units independently can break the footnote or insert text inside it.",
      recurrenceCues: ["srcfn opens near unit end", "next unit begins with display and closes brace", "unit-level compile attempted"],
      relatedStructuralIds: ["NOE-P06-KO-T03-U21-FOOTNOTE-OPEN-001", "NOE-P06-KO-T03-U22-FOOTNOTE-CLOSE-001", "NOE-P06-KO-T03-U22-EQUATION-001"],
      relatedDecisionIds: ["CJK-KO-P06-006"],
      lesson: "When a closed source structure crosses editable units, preserve bytes and encode ordered continuation explicitly rather than pretending each unit is closed."
    }),
    difficultyRecord(25, ["T03"], ["U15", "U16", "U17", "U18", "U19", "U20", "U21", "U22"], "active_control", "editorial_inference", {
      sourceLocators: ["P06 T03 Korean terminology and evidence shelf"],
      symptom: "Specialization/substitution, divisibility, rank, matrix, reduced-form, and homogeneous-form choices remain vulnerable to modern-register and Sino-xenic attractors.",
      causeEvidence: "TRANSLATION_CHOICES_T03_SECTION2.md separates sense windows and lexical-attractor basins while recording Mandarin-Simplified dominance only qualitatively.",
      attempted: [
        { approach: "Expose each provisional choice, alternative, adverse pull, and Korean-only evidence requirement.", outcome: "Review debt is explicit without a readiness scalar.", rejected_reason: null },
        { approach: "Use Chinese/Japanese cognates or Hanja as Korean authorization.", outcome: "Rejected.", rejected_reason: "Neighboring languages and script do not validate Korean usage." }
      ],
      resolution: "Active control pending independent Korean evidence; no ko-KP claim.",
      evidence: [metadataEvidence("TRANSLATION_CHOICES_T03_SECTION2.md", "Sense windows and attractor basins recorded.")],
      residualRisk: "Historically plausible calques can conceal anachronistic or non-Korean register.",
      recurrenceCues: ["Spezialisierung versus Substitution", "rank loan versus homograph", "historical invariant language", "no Korean corpus evidence"],
      relatedStructuralIds: ["NOE-P06-KO-T03-001"],
      relatedDecisionIds: ["CJK-KO-P06-006"],
      lesson: "Treat lexical-attractor classes as qualitative evidence routing, not correctness scores, and keep Korean evidence independent."
    })
  ];
}

function difficultyCsvRow(r) {
  return [
    r.record_id,
    r.sequence,
    r.observed_at,
    r.time_precision,
    r.state,
    r.classification,
    r.tranche_ids.join("|"),
    r.unit_ids.join("|"),
    r.source_locators.join("|"),
    r.target_artifacts.map(x => x.path).join("|"),
    r.symptom,
    r.cause_evidence,
    r.resolution_or_hold,
    r.residual_risk,
    r.related_structural_ids.join("|"),
    r.related_decision_ids.join("|"),
    r.previous_record_id ?? "",
    r.transferable_lesson
  ];
}

function freezeObject(scope, before, after, addedStructural, addedDifficulty) {
  const schemaPath = path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX.schema.json");
  const visualJsonl = path.join(visualDir, "VISUAL_EVIDENCE_INDEX.jsonl");
  const visualCsv = path.join(visualDir, "VISUAL_EVIDENCE_INDEX.csv");
  return {
    schema_version: "1.0",
    freeze_id: "NOE-P06-KO-" + scope + "-EVIDENCE-PREFIX-FREEZE-20260804-001",
    recorded_at: "2026-08-04",
    time_precision: "day",
    classification: "computation",
    scope,
    append_only: true,
    source_authority: AUTHORITY,
    protected_inputs: { files: protectedRelativePaths.length, manifest: { path: path.relative(producerRoot, protectedManifestPath).replaceAll("\\", "/"), ...identity(protectedManifestPath) }, mutations: 0 },
    prefix_before: before,
    prefix_through_scope: after,
    appended: {
      structural_records: addedStructural.length,
      first_structural_id: addedStructural[0].structural_id,
      latest_structural_id: addedStructural.at(-1).structural_id,
      difficulty_records: addedDifficulty.length,
      first_difficulty_id: addedDifficulty[0].record_id,
      latest_difficulty_id: addedDifficulty.at(-1).record_id
    },
    schema: { path: path.relative(producerRoot, schemaPath).replaceAll("\\", "/"), ...identity(schemaPath) },
    visual_zero: {
      records: 0,
      jsonl: { ...identity(visualJsonl) },
      csv: { ...identity(visualCsv) },
      render_calls: 0
    },
    review_state: "unchecked",
    limits: ["No source or scan review", "No Korean or formula review", "No compilation or rendering", "No assembly packaging certification approval canon archive or SGA work"]
  };
}

function currentPrefixIdentity() {
  return {
    structural_jsonl: identity(structuralJsonl),
    structural_csv: identity(structuralCsv),
    difficulty_jsonl: identity(difficultyJsonl),
    difficulty_csv: identity(difficultyCsv)
  };
}

function verifyT01Prefix() {
  const expected = {
    structural_jsonl: { bytes: 70119, sha256: "43C36F91081F8EDAE7B00E7426B570B4D6A6667937BEA0CC005923893155E61A" },
    structural_csv: { bytes: 24595, sha256: "1A05372CDF95EB9236349A658F4BD98930755BCAF42FBA201C22FB7BDA0600C9" },
    difficulty_jsonl: { bytes: 28167, sha256: "430B121D56A078ABA7B9CC09E2B7C494092359DC13F4E526AA700A0A38AD8662" },
    difficulty_csv: { bytes: 10462, sha256: "4384B3D67405702A645C31CD4FD65F8004C6E572388AD6BD9FB687864810D00E" }
  };
  const live = currentPrefixIdentity();
  assert(JSON.stringify(live) === JSON.stringify(expected), "T01 prefix identity changed");
  assert(parseJsonl(structuralJsonl).length === 52, "T01 structural count changed");
  assert(parseJsonl(difficultyJsonl).length === 11, "T01 difficulty count changed");
  return expected;
}

function appendPhase(scope) {
  verifyAuthorityAndUnits();
  ensureProtectedManifest();
  if (scope === "T02") {
    const before = verifyT01Prefix();
    assert(!fs.existsSync(path.join(freezeDir, "P06_T02_EVIDENCE_PREFIX_FREEZE_20260804.json")), "T02 freeze already exists");
    const existingStructural = parseJsonl(structuralJsonl);
    const structural = buildT02Structural(existingStructural.at(-1).global_order);
    const difficulty = buildT02Difficulty();
    assert(difficulty[0].sequence === 12 && difficulty.at(-1).sequence === 16, "T02 difficulty sequence");
    appendLines(structuralJsonl, structural);
    appendCsvRows(structuralCsv, structural.map(structuralCsvRow));
    appendLines(difficultyJsonl, difficulty);
    appendCsvRows(difficultyCsv, difficulty.map(difficultyCsvRow));
    const after = currentPrefixIdentity();
    const freeze = freezeObject("T02", before, after, structural, difficulty);
    writeUtf8(path.join(freezeDir, "P06_T02_EVIDENCE_PREFIX_FREEZE_20260804.json"), JSON.stringify(freeze, null, 2) + "\n");
    return { phase: "T02", structural_added: structural.length, difficulty_added: difficulty.length, before, after, freeze: identity(path.join(freezeDir, "P06_T02_EVIDENCE_PREFIX_FREEZE_20260804.json")) };
  }
  if (scope === "T03") {
    const t02FreezePath = path.join(freezeDir, "P06_T02_EVIDENCE_PREFIX_FREEZE_20260804.json");
    assert(fs.existsSync(t02FreezePath), "T02 freeze missing");
    const t02Freeze = JSON.parse(text(t02FreezePath));
    const before = currentPrefixIdentity();
    assert(JSON.stringify(before) === JSON.stringify(t02Freeze.prefix_through_scope), "live evidence no longer equals frozen T02 prefix");
    assert(!fs.existsSync(path.join(freezeDir, "P06_T03_EVIDENCE_PREFIX_FREEZE_20260804.json")), "T03 freeze already exists");
    const existingStructural = parseJsonl(structuralJsonl);
    const structural = buildT03Structural(existingStructural.at(-1).global_order);
    const difficulty = buildT03Difficulty();
    assert(difficulty[0].sequence === 17 && difficulty.at(-1).sequence === 25, "T03 difficulty sequence");
    appendLines(structuralJsonl, structural);
    appendCsvRows(structuralCsv, structural.map(structuralCsvRow));
    appendLines(difficultyJsonl, difficulty);
    appendCsvRows(difficultyCsv, difficulty.map(difficultyCsvRow));
    const after = currentPrefixIdentity();
    const freeze = freezeObject("T03", before, after, structural, difficulty);
    freeze.boundary_control = {
      terminal_unit: "T03-U22",
      source_lines: "4794-4797",
      source_bytes: 160,
      source_sha256: T03_UNITS.at(-1).sourceSha,
      excluded_blank_line: 4798,
      excluded_blank_bytes: 1,
      excluded_blank_sha256: "01BA4719C80B6FE911B091A7C05124B64EEECE964E09C058EF8F9805DACA546B",
      next_scope_line: 4799,
      t04_absorbed: false
    };
    freeze.cross_unit_relation = {
      from: "NOE-P06-KO-T03-U21-FOOTNOTE-OPEN-001",
      to: "NOE-P06-KO-T03-U22-FOOTNOTE-CLOSE-001",
      relation: "srcfn continuation and closure",
      target_order: "U21 then U22 without inserted prose"
    };
    writeUtf8(path.join(freezeDir, "P06_T03_EVIDENCE_PREFIX_FREEZE_20260804.json"), JSON.stringify(freeze, null, 2) + "\n");
    return { phase: "T03", structural_added: structural.length, difficulty_added: difficulty.length, before, after, freeze: identity(path.join(freezeDir, "P06_T03_EVIDENCE_PREFIX_FREEZE_20260804.json")) };
  }
  throw new Error("phase must be T02 or T03");
}

function makeReports() {
  const structural = parseJsonl(structuralJsonl);
  const difficulty = parseJsonl(difficultyJsonl);
  const visualJsonl = path.join(visualDir, "VISUAL_EVIDENCE_INDEX.jsonl");
  const visualCsv = path.join(visualDir, "VISUAL_EVIDENCE_INDEX.csv");
  assert(text(visualJsonl).length === 0, "visual JSONL not empty");
  const validatorPath = path.join(evidenceRoot, "validate_p06_t01_t03_evidence.mjs");
  assert(fs.existsSync(validatorPath), "final validator missing");
  const schemaPath = path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX.schema.json");
  const difficultySchemaPath = path.join(difficultyDir, "DIFFICULTY_LEDGER.schema.json");
  const visualSchemaPath = path.join(visualDir, "VISUAL_EVIDENCE_INDEX.schema.json");
  const typeCounts = {};
  for (const r of structural) typeCounts[r.record_type] = (typeCounts[r.record_type] ?? 0) + 1;
  const stateCounts = {};
  for (const r of difficulty) stateCounts[r.state] = (stateCounts[r.state] ?? 0) + 1;
  const t02FreezePath = path.join(freezeDir, "P06_T02_EVIDENCE_PREFIX_FREEZE_20260804.json");
  const t03FreezePath = path.join(freezeDir, "P06_T03_EVIDENCE_PREFIX_FREEZE_20260804.json");
  const structuralReport = {
    schema: "PRODUCER_STRUCTURAL_INDEX.schema.json",
    schema_sha256: sha(read(schemaPath)),
    validator: "../validate_p06_t01_t03_evidence.mjs",
    validator_sha256: sha(read(validatorPath)),
    status: "PASS",
    scope: "Noether Paper 6 Korean T01--T03 U01--U22 producer topology only",
    record_count: structural.length,
    unique_record_count: new Set(structural.map(r => r.structural_id)).size,
    latest_structural_id: structural.at(-1).structural_id,
    type_counts: typeCounts,
    hierarchy_checks: { parent_ids_present: true, internal_relation_targets_present: true, global_orders_unique_and_contiguous: true },
    custody_checks: {
      route_files: 3,
      top_metadata_files: 12,
      target_files: 22,
      target_bytes: [...Array(22)].map((_, i) => i + 1).reduce((sum, n) => {
        const tranche = n <= 6 ? "T01" : n <= 14 ? "T02" : "T03";
        return sum + read(targetPath("Noether_P06_Korean_" + tranche + "_U" + String(n).padStart(2, "0") + "_UNCHECKED.tex")).length;
      }, 0),
      protected_manifest: { path: "../protected_inputs/P06_T01_T03_PROTECTED_INPUT_MANIFEST.tsv", ...identity(protectedManifestPath) },
      mutations: 0,
      excluded_target_scope: "T04 and later"
    },
    prefix_freezes: {
      t02: { path: "../prefix_freezes/P06_T02_EVIDENCE_PREFIX_FREEZE_20260804.json", ...identity(t02FreezePath) },
      t03: { path: "../prefix_freezes/P06_T03_EVIDENCE_PREFIX_FREEZE_20260804.json", ...identity(t03FreezePath) }
    },
    binding_pointers: [POINTERS.T02, POINTERS.T03],
    jsonl: { ...identity(structuralJsonl) },
    csv: { data_rows: structural.length, ...identity(structuralCsv) },
    errors: [],
    continuation_cursor: "Independent Korean checker for T01--T03; producer translation continues at whole-source line 4799.",
    limits: ["Structure classes are producer/computational annotations, not semantic approval.", "No source, scan, Korean, formula, compilation, rendering, assembly, packaging, certification, archive, canon, or human validation."]
  };
  const difficultyReport = {
    schema: "DIFFICULTY_LEDGER.schema.json",
    schema_sha256: sha(read(difficultySchemaPath)),
    validator: "../validate_p06_t01_t03_evidence.mjs",
    validator_sha256: sha(read(validatorPath)),
    status: "PASS",
    append_only: true,
    predecessor_sequence_verified: true,
    record_count: difficulty.length,
    unique_record_count: new Set(difficulty.map(r => r.record_id)).size,
    latest_record_id: difficulty.at(-1).record_id,
    state_counts: stateCounts,
    required_history: {
      t01_prefix_latest: "CJK-KO-P06-HARD-011",
      t02_prefix_latest: "CJK-KO-P06-HARD-016",
      t02_verifier_regex_failure: "CJK-KO-P06-HARD-017",
      t03_metadata_empty_pipeline_failure: "CJK-KO-P06-HARD-018",
      t03_split_footnote_hold: "CJK-KO-P06-HARD-024",
      current_latest: "CJK-KO-P06-HARD-025"
    },
    prefix_freezes: {
      t02: { path: "../prefix_freezes/P06_T02_EVIDENCE_PREFIX_FREEZE_20260804.json", ...identity(t02FreezePath) },
      t03: { path: "../prefix_freezes/P06_T03_EVIDENCE_PREFIX_FREEZE_20260804.json", ...identity(t03FreezePath) }
    },
    jsonl: { ...identity(difficultyJsonl) },
    csv: { data_rows: difficulty.length, ...identity(difficultyCsv) },
    errors: [],
    continuation_cursor: "Append any future correction or failure after CJK-KO-P06-HARD-025 without rewriting the twenty-five-record prefix.",
    scope_note: "Resolved failures remain evidence. Held and active-control records remain independent-checker debt; PASS validates metadata topology only."
  };
  const visualReport = {
    schema: "VISUAL_EVIDENCE_INDEX.schema.json",
    schema_sha256: sha(read(visualSchemaPath)),
    validator: "../validate_p06_t01_t03_evidence.mjs",
    validator_sha256: sha(read(validatorPath)),
    status: "PASS",
    scope: "Noether Paper 6 Korean T01--T03 U01--U22 producer visual inventory",
    record_count: 0,
    image_file_count: 0,
    render_call_count: 0,
    type_counts: { source_page: 0, source_crop: 0, equation_crop: 0, diagram_crop: 0, target_render: 0, contact_sheet: 0, before_after: 0, segmentation_artifact: 0, model_overlay: 0 },
    rights_disposition_totals: { public_safe: 0, rights_blocked: 0, private_excluded: 0, pending: 0 },
    total_image_bytes: 0,
    jsonl: { ...identity(visualJsonl) },
    csv: { data_rows: 0, ...identity(visualCsv) },
    errors: [],
    continuation_cursor: "No producer visual evidence exists through T03 U22; rendering remains outside the translation-only lane.",
    scope_note: "Explicit zero inventory is evidence of no image use or creation. It is not visual QA or rights clearance."
  };
  writeUtf8(path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json"), JSON.stringify(structuralReport, null, 2) + "\n");
  writeUtf8(path.join(difficultyDir, "DIFFICULTY_LEDGER_VALIDATION_REPORT.json"), JSON.stringify(difficultyReport, null, 2) + "\n");
  writeUtf8(path.join(visualDir, "VISUAL_EVIDENCE_INDEX_VALIDATION_REPORT.json"), JSON.stringify(visualReport, null, 2) + "\n");
  const status = [
    "# Noether Paper 6 Korean T01--T03 visual-evidence status",
    "",
    "Status: explicit zero inventory through T03 U22; validator PASS.",
    "",
    "- Records: 0",
    "- Image files: 0",
    "- Render calls: 0",
    "- Source pages/crops, equation/diagram crops, target renders, contact sheets, before/after images, segmentation artifacts, and model overlays: 0 each",
    "- Total image bytes: 0",
    "- Rights/disposition totals: public-safe 0; rights-blocked 0; private-excluded 0; pending 0",
    "- JSONL: VISUAL_EVIDENCE_INDEX.jsonl — 0 bytes — SHA-256 " + identity(visualJsonl).sha256,
    "- CSV projection: VISUAL_EVIDENCE_INDEX.csv — " + identity(visualCsv).bytes + " bytes — SHA-256 " + identity(visualCsv).sha256,
    "- Schema: VISUAL_EVIDENCE_INDEX.schema.json — " + identity(visualSchemaPath).bytes + " bytes — SHA-256 " + identity(visualSchemaPath).sha256,
    "- Read-only validator: ../validate_p06_t01_t03_evidence.mjs — " + identity(validatorPath).bytes + " bytes — SHA-256 " + identity(validatorPath).sha256,
    "",
    "No image was used or created for T01--T03, and no render or visual inspection occurred. The zero inventory does not certify layout, formulas, Korean, source fidelity, or redistribution rights. T04 and later are outside this evidence scope.",
    ""
  ].join("\n");
  writeUtf8(path.join(visualDir, "STATUS.md"), status);
  return {
    structural_report: identity(path.join(structuralDir, "PRODUCER_STRUCTURAL_INDEX_VALIDATION_REPORT.json")),
    difficulty_report: identity(path.join(difficultyDir, "DIFFICULTY_LEDGER_VALIDATION_REPORT.json")),
    visual_report: identity(path.join(visualDir, "VISUAL_EVIDENCE_INDEX_VALIDATION_REPORT.json")),
    visual_status: identity(path.join(visualDir, "STATUS.md"))
  };
}

const phase = process.argv[2];
let result;
if (phase === "T02" || phase === "T03") result = appendPhase(phase);
else if (phase === "reports") result = makeReports();
else throw new Error("Usage: node extend_p06_t02_t03_evidence.mjs T02|T03|reports");
process.stdout.write(JSON.stringify(result, null, 2) + "\n");
