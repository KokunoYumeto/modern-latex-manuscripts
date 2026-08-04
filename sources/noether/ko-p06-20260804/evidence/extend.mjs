import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, "..");
const targetsDir = path.join(root, "targets");
const sdir = path.join(here, "structural_index");
const ddir = path.join(here, "difficulty_ledger");
const edPath = "C:\\Users\\Floris\\Documents\\interlanguage\\03_projects\\noether\\07_german_canon_control\\candidates\\ED0002\\noether.tex";
const pointerId = "NOETH-DE-AUTH-v009-20260804";
const pointerSha = "B06BE3530D9CF2E82B56FDBA7FE41D5D044DF2425DFA2A059D4939EAA2F7A6C2";
const authorityId = "NOETH-DE-ED-0002";
const authoritySha = "C9A125167ACB33D914EE4374B65AE7CDF0052F568371B8B77B720EA178ABF0E3";
const continuation = "P06 producer-draft text coverage is complete through line 5828; independent Korean checking, assembly, build, render, and visual QA remain.";
const sha = (b) => crypto.createHash("sha256").update(b).digest("hex").toUpperCase();
const utf8 = (s) => Buffer.from(s, "utf8");
const norm = (s) => s.replace(/\r\n/g, "\n").replace(/\r/g, "\n");
const edLines = norm(fs.readFileSync(edPath, "utf8")).split("\n");
const sourceBytes = (a, z) => utf8(edLines.slice(a - 1, z).join("\n") + "\n");
const pad2 = (n) => String(n).padStart(2, "0");
const rel = (p) => path.relative(root, p).replaceAll("\\", "/");
const lineCount = (text) => text.endsWith("\n") ? text.split("\n").length - 1 : text.split("\n").length;
const csvCell = (v) => {
  const s = v === null || v === undefined ? "" : String(v);
  return /[",\r\n]/.test(s) ? "\"" + s.replaceAll("\"", "\"\"") + "\"" : s;
};

function parseTarget(file) {
  const raw = fs.readFileSync(file);
  const text = raw.toString("utf8");
  const head = text.split("\n").slice(0, 12).join("\n");
  const nameMatch = path.basename(file).match(/T(\d+)[-_]U(\d+)/i);
  if (!nameMatch) throw new Error("Cannot parse tranche/unit from filename: " + file);
  const locatorMatch = head.match(/Unit source:\s*whole-source\s+lines?\s*(\d+)(?:--(\d+))?/i)
    || head.match(/current-authority\s+whole\s+lines?\s*(\d+)(?:--(\d+))?/i)
    || head.match(/ED000[12]\s+lines?\s*(\d+)(?:--(\d+))?/i);
  if (!locatorMatch) throw new Error("Cannot parse source locator from header: " + file);
  const tranche = Number(nameMatch[1]);
  const unit = Number(nameMatch[2]);
  const start = Number(locatorMatch[1]);
  const end = Number(locatorMatch[2] || locatorMatch[1]);
  const computedSourceSha = sha(sourceBytes(start, end));
  const declaredHashes = [...head.matchAll(/[A-F0-9]{64}/ig)].map((m) => m[0].toUpperCase());
  if (!declaredHashes.includes(computedSourceSha)) {
    throw new Error("Computed source hash absent from header in " + file + ": " + computedSourceSha);
  }
  const lines = text.split("\n");
  const count = lineCount(text);
  let bodyStart = 1;
  while (bodyStart <= count && (lines[bodyStart - 1].startsWith("%") || lines[bodyStart - 1].trim() === "")) bodyStart++;
  return {
    file,
    relPath: rel(file),
    raw,
    text,
    targetLines: lines,
    targetLineCount: count,
    bodyStart,
    tranche,
    unit,
    start,
    end,
    sourceSha: computedSourceSha,
    targetSha: sha(raw)
  };
}

const targetFiles = fs.readdirSync(targetsDir)
  .filter((n) => n.toLowerCase().endsWith(".tex"))
  .map((n) => path.join(targetsDir, n));
const units = targetFiles.map(parseTarget).sort((a, b) => a.unit - b.unit);
if (units.length !== 228) throw new Error("Expected 228 targets, got " + units.length);
for (let i = 1; i <= 228; i++) if (units[i - 1].unit !== i) throw new Error("Missing or duplicate U" + i);

const jsonlPath = path.join(sdir, "PRODUCER_STRUCTURAL_INDEX.jsonl");
const existing = fs.readFileSync(jsonlPath, "utf8").trim().split("\n").filter(Boolean).map(JSON.parse);
const existingIds = new Set(existing.map((r) => r.structural_id));
let order = Math.max(...existing.map((r) => r.global_order));
const added = [];

function makeRecord(args) {
  return {
    schema_version: "1.0",
    structural_id: args.id,
    work_id: "NOE-P06",
    tranche_id: args.tranche,
    unit_id: args.unitId,
    record_type: args.type,
    source_language: "de",
    target_language: "ko",
    global_order: ++order,
    parent_id: args.parent,
    relations: args.relations || [],
    source_locator: {
      whole_line_start: args.s1,
      whole_line_end: args.s2,
      description: args.description
    },
    target_locator: {
      path: args.targetPath,
      line_start: args.t1,
      line_end: args.t2,
      description: args.description
    },
    source_sha256: args.sourceSha,
    target_sha256: args.targetSha,
    pointer_id: pointerId,
    pointer_sha256: pointerSha,
    authority_id: authorityId,
    authority_sha256: authoritySha,
    completion_state: "producer_draft_coverage",
    review_state: "unchecked",
    publication_state: "eligible_with_honest_metadata",
    classification: args.classification || "computation",
    continuation_cursor: continuation,
    notes: args.notes || ""
  };
}

function push(record) {
  if (!existingIds.has(record.structural_id)) {
    existingIds.add(record.structural_id);
    added.push(record);
  } else {
    order--;
  }
}

const allTargetBytes = Buffer.concat(units.map((u) => u.raw));
push(makeRecord({
  id: "NOE-P06-KO-WORK-002",
  tranche: "T16",
  unitId: null,
  type: "work",
  parent: null,
  relations: [{ type: "supersedes", target_id: "NOE-P06-KO-WORK-001", scope: "internal", basis: "complete P06 producer-draft coverage successor" }],
  s1: 4576,
  s2: 5828,
  description: "Complete Paper 6 Korean producer-draft work container",
  targetPath: "targets/",
  t1: null,
  t2: null,
  sourceSha: sha(sourceBytes(4576, 5828)),
  targetSha: sha(allTargetBytes),
  notes: "Aggregate target digest concatenates U01--U228 raw target bytes in numeric unit order."
}));

function targetSpanBytes(u, a, z) {
  return utf8(u.targetLines.slice(a - 1, z).join("\n") + "\n");
}

function targetMatchLine(u, regex, fallback) {
  for (let i = 0; i < u.targetLineCount; i++) if (regex.test(u.targetLines[i])) return i + 1;
  return fallback;
}

function sourceLineForIndex(text, idx, start) {
  return start + text.slice(0, idx).split("\n").length - 1;
}

function displaySpans(lines, absoluteStart) {
  const spans = [];
  let open = null;
  for (let i = 0; i < lines.length; i++) {
    if (open === null && lines[i].includes("\\[")) open = i;
    if (open !== null && lines[i].includes("\\]")) {
      spans.push([absoluteStart + open, absoluteStart + i]);
      open = null;
    }
  }
  if (open !== null) spans.push([absoluteStart + open, absoluteStart + lines.length - 1]);
  return spans;
}

const byTranche = new Map();
for (const u of units.filter((x) => x.tranche >= 4)) {
  if (!byTranche.has(u.tranche)) byTranche.set(u.tranche, []);
  byTranche.get(u.tranche).push(u);
}

for (const [tn, tus] of [...byTranche.entries()].sort((a, b) => a[0] - b[0])) {
  tus.sort((a, b) => a.unit - b.unit);
  const tr = "T" + pad2(tn);
  const trancheId = "NOE-P06-KO-" + tr + "-001";
  const s1 = Math.min(...tus.map((u) => u.start));
  const s2 = Math.max(...tus.map((u) => u.end));
  push(makeRecord({
    id: trancheId,
    tranche: tr,
    unitId: null,
    type: "tranche",
    parent: "NOE-P06-KO-WORK-002",
    relations: [{ type: "internal_relation", target_id: "NOE-P06-KO-WORK-002", scope: "internal", basis: "contained by complete work" }],
    s1,
    s2,
    description: tr + " source-closed producer tranche",
    targetPath: "targets/",
    t1: null,
    t2: null,
    sourceSha: sha(sourceBytes(s1, s2)),
    targetSha: sha(Buffer.concat(tus.map((u) => u.raw))),
    notes: "Tranche aggregate includes routed units in numeric order; intervening blank source separators remain represented by the source span."
  }));

  for (let j = 0; j < tus.length; j++) {
    const u = tus[j];
    const unitId = "U" + pad2(u.unit);
    const id = "NOE-P06-KO-" + tr + "-" + unitId;
    const relations = [{ type: "internal_relation", target_id: trancheId, scope: "internal", basis: "contained by tranche" }];
    if (j > 0) relations.push({ type: "continues_after", target_id: "NOE-P06-KO-" + tr + "-U" + pad2(tus[j - 1].unit), scope: "internal", basis: "direct source order" });
    push(makeRecord({
      id,
      tranche: tr,
      unitId,
      type: "unit",
      parent: trancheId,
      relations,
      s1: u.start,
      s2: u.end,
      description: unitId + " routed source and editable target container",
      targetPath: u.relPath,
      t1: 1,
      t2: u.targetLineCount,
      sourceSha: u.sourceSha,
      targetSha: u.targetSha
    }));

    const srcText = edLines.slice(u.start - 1, u.end).join("\n");
    const srcLocalLines = srcText.split("\n");
    const childBase = {
      tranche: tr,
      unitId,
      parent: id,
      relations: [{ type: "internal_relation", target_id: id, scope: "internal", basis: "contained by unit" }],
      targetPath: u.relPath
    };
    push(makeRecord({
      ...childBase,
      id: id + "-PROSE-001",
      type: "prose",
      s1: u.start,
      s2: u.end,
      description: "Closed prose/display carrier for " + unitId,
      t1: u.bodyStart,
      t2: u.targetLineCount,
      sourceSha: u.sourceSha,
      targetSha: sha(targetSpanBytes(u, u.bodyStart, u.targetLineCount)),
      classification: "editorial_inference",
      notes: "Producer structural carrier only; it does not assert linguistic or mathematical validity."
    }));

    if (/\\section\*|\\begin\{center\}/.test(srcText)) {
      const sl = u.start + srcLocalLines.findIndex((x) => /\\section\*|\\begin\{center\}/.test(x));
      const tl = targetMatchLine(u, /\\section\*|\\begin\{center\}/, u.bodyStart);
      push(makeRecord({
        ...childBase,
        id: id + "-HEADING-001",
        type: "heading",
        s1: sl,
        s2: sl,
        description: "Section or centered heading",
        t1: tl,
        t2: tl,
        sourceSha: sha(sourceBytes(sl, sl)),
        targetSha: sha(targetSpanBytes(u, tl, tl)),
        classification: "source_fact"
      }));
    }

    const kinds = [
      ["DEFINITION", "definition", /\\emph\{Definition|\\textbf\{Definition/g, /정의/],
      ["THEOREM", "theorem", /\\emph\{Satz|\\textbf\{Satz/g, /정리/],
      ["LEMMA", "lemma", /\\emph\{Hilfssatz|Hilfssatz\./g, /보조정리/],
      ["EXAMPLE", "example", /\bBeispiel\b/g, /예/],
      ["REMARK", "remark", /\bAnmerkung\b/g, /주석/]
    ];
    for (const [label, type, rx, trx] of kinds) {
      let k = 0;
      for (const match of srcText.matchAll(rx)) {
        k++;
        const sl = sourceLineForIndex(srcText, match.index, u.start);
        const tl = targetMatchLine(u, trx, u.bodyStart);
        push(makeRecord({
          ...childBase,
          id: id + "-" + label + "-" + String(k).padStart(3, "0"),
          type,
          s1: sl,
          s2: sl,
          description: label.toLowerCase() + " marker in " + unitId,
          t1: tl,
          t2: tl,
          sourceSha: sha(sourceBytes(sl, sl)),
          targetSha: sha(targetSpanBytes(u, tl, tl)),
          classification: "source_fact"
        }));
      }
    }

    const srcDisplays = displaySpans(srcLocalLines, u.start);
    const tgtDisplays = displaySpans(u.targetLines.slice(0, u.targetLineCount), 1);
    for (let k = 0; k < srcDisplays.length; k++) {
      const [sl1, sl2] = srcDisplays[k];
      const [tl1, tl2] = tgtDisplays[k] || [u.bodyStart, u.targetLineCount];
      push(makeRecord({
        ...childBase,
        id: id + "-EQUATION-" + String(k + 1).padStart(3, "0"),
        type: "equation",
        s1: sl1,
        s2: sl2,
        description: "Displayed equation or array " + (k + 1) + " in " + unitId,
        t1: tl1,
        t2: tl2,
        sourceSha: sha(sourceBytes(sl1, sl2)),
        targetSha: sha(targetSpanBytes(u, tl1, tl2)),
        classification: "computation",
        notes: "Display topology only; formula tokens remain unchecked."
      }));
    }

    const srcFoot = [];
    srcLocalLines.forEach((line, idx) => { if (/\\srcfn(?:mark|text)?/.test(line)) srcFoot.push(u.start + idx); });
    const tgtFoot = [];
    u.targetLines.slice(0, u.targetLineCount).forEach((line, idx) => { if (/\\srcfn(?:mark|text)?/.test(line)) tgtFoot.push(idx + 1); });
    for (let k = 0; k < srcFoot.length; k++) {
      const sl = srcFoot[k];
      const tl = tgtFoot[k] || u.bodyStart;
      push(makeRecord({
        ...childBase,
        id: id + "-FOOTNOTE-" + String(k + 1).padStart(3, "0"),
        type: "footnote",
        s1: sl,
        s2: sl,
        description: "Source footnote carrier " + (k + 1) + " in " + unitId,
        t1: tl,
        t2: tl,
        sourceSha: sha(sourceBytes(sl, sl)),
        targetSha: sha(targetSpanBytes(u, tl, tl)),
        classification: "source_fact"
      }));
    }

    const xrefLines = [];
    srcLocalLines.forEach((line, idx) => { if (/\\S\\/.test(line)) xrefLines.push(u.start + idx); });
    if (xrefLines.length) {
      const tl = targetMatchLine(u, /\\S\\/, u.bodyStart);
      push(makeRecord({
        ...childBase,
        id: id + "-XREF-001",
        type: "cross_reference",
        s1: Math.min(...xrefLines),
        s2: Math.max(...xrefLines),
        description: "Explicit section cross-reference carrier",
        t1: tl,
        t2: tl,
        sourceSha: sha(sourceBytes(Math.min(...xrefLines), Math.max(...xrefLines))),
        targetSha: sha(targetSpanBytes(u, tl, tl)),
        classification: "computation"
      }));
    }

    if (/Math\. Ann|Sitzungsber|Gött\.|Jahresber|Erlangen,/.test(srcText)) {
      const idx = srcLocalLines.findIndex((x) => /Math\. Ann|Sitzungsber|Gött\.|Jahresber|Erlangen,/.test(x));
      const sl = u.start + idx;
      push(makeRecord({
        ...childBase,
        id: id + "-BIB-001",
        type: "bibliographic_item",
        s1: sl,
        s2: sl,
        description: "Bibliographic or dateline item",
        t1: u.bodyStart,
        t2: u.targetLineCount,
        sourceSha: sha(sourceBytes(sl, sl)),
        targetSha: sha(targetSpanBytes(u, u.bodyStart, u.targetLineCount)),
        classification: "source_fact"
      }));
    }
  }
}

if (added.length) fs.appendFileSync(jsonlPath, added.map((r) => JSON.stringify(r)).join("\n") + "\n", "utf8");
const allRecords = fs.readFileSync(jsonlPath, "utf8").trim().split("\n").filter(Boolean).map(JSON.parse);
const structuralHeader = ["structural_id","record_type","unit_id","parent_id","global_order","source_lines","target_path","target_lines","source_sha256","target_sha256","source_language","target_language","completion_state","review_state","publication_state","relation_targets","classification","continuation_cursor"];
const structuralRows = allRecords.map((r) => [
  r.structural_id, r.record_type, r.unit_id, r.parent_id, r.global_order,
  r.source_locator.whole_line_start + "-" + r.source_locator.whole_line_end,
  r.target_locator.path,
  r.target_locator.line_start === null ? "" : r.target_locator.line_start + "-" + r.target_locator.line_end,
  r.source_sha256, r.target_sha256, r.source_language, r.target_language,
  r.completion_state, r.review_state, r.publication_state,
  r.relations.map((x) => x.scope + ":" + x.type + ":" + x.target_id).join("|"),
  r.classification, r.continuation_cursor
]);
fs.writeFileSync(path.join(sdir, "PRODUCER_STRUCTURAL_INDEX.csv"), [structuralHeader, ...structuralRows].map((r) => r.map(csvCell).join(",")).join("\n") + "\n", "utf8");

function artifact(p) {
  const full = path.join(root, p);
  const b = fs.readFileSync(full);
  return { path: p.replaceAll("\\", "/"), bytes: b.length, sha256: sha(b) };
}
const dpath = path.join(ddir, "DIFFICULTY_LEDGER.jsonl");
const difficulties = fs.readFileSync(dpath, "utf8").trim().split("\n").filter(Boolean).map(JSON.parse);
const dids = new Set(difficulties.map((r) => r.record_id));
let prev = difficulties.at(-1)?.record_id || null;
let seq = difficulties.at(-1)?.sequence || 0;
const auth = { pointer_id: pointerId, pointer_sha256: pointerSha, authority_id: authorityId, authority_sha256: authoritySha };
const addDifficulty = (x) => {
  if (dids.has(x.record_id)) return;
  x.schema_version = "1.0";
  x.sequence = ++seq;
  x.observed_at = "2026-08-04";
  x.time_precision = "day";
  x.work_id = "NOE-P06";
  x.authority_context = auth;
  x.previous_record_id = prev;
  prev = x.record_id;
  dids.add(x.record_id);
  difficulties.push(x);
};
addDifficulty({
  record_id: "CJK-KO-P06-HARD-026", tranche_ids: ["T08"], unit_ids: Array.from({length:16}, (_,i) => "U" + (91+i)), state: "resolved", classification: "computation",
  source_locators: ["P06 T08 U91--U106 delegated production attempt"],
  target_artifacts: [artifact("T08_META.md")],
  symptom: "The bounded translation worker remained pending and returned no usable files while the root session could continue directly.",
  cause_evidence: "Live ownership checks showed no worker return; the root produced U91--U106 only after collision checks and cancellation messages.",
  attempted_approaches: [
    { approach: "Delegate U91--U106 to a bounded worker.", outcome: "No usable return.", rejected_reason: "Slower than direct production." },
    { approach: "Cancel ownership and translate manually after collision checks.", outcome: "Complete T08 coverage frozen.", rejected_reason: null }
  ],
  resolution_or_hold: "Resolved by manual root production; user later made manual-only production controlling.",
  evidence: [{kind:"producer_metadata", path:"T08_META.md", sha256:artifact("T08_META.md").sha256, result:"Complete U75--U106 manifest."}],
  residual_risk: "A late worker write could have collided; current inventory shows exactly one file per U01--U228.",
  recurrence_cues: ["pending worker", "no explicit handoff", "shared filesystem ownership"],
  related_structural_ids: ["NOE-P06-KO-T08-001"], related_decision_ids: ["CJK-KO-P06-032","CJK-KO-OPS-002"],
  transferable_lesson: "If delegation is slower than direct translation or lacks a prompt return, cancel it, prove no collision, and keep one manual owner."
});
addDifficulty({
  record_id: "CJK-KO-P06-HARD-027", tranche_ids: ["T09"], unit_ids: ["U107","U122"], state: "resolved", classification: "computation",
  source_locators: ["T09 routing and target-inventory PowerShell commands"],
  target_artifacts: [artifact("T09_ROUTE.md"), artifact("T09_META.md")],
  symptom: "Two read-only PowerShell commands used compressed foreach grammar and failed before producing inventories.",
  cause_evidence: "Missing whitespace made -in merge with the variable token; later compressed -gt forms produced the same class of parser/binder error.",
  attempted_approaches: [
    { approach: "Use compressed foreach and comparison syntax.", outcome: "Parser/binder failure; writes zero.", rejected_reason: "Unreliable grammar." },
    { approach: "Use visibly spaced PowerShell operators and block predicates.", outcome: "Reconstruction and inventories passed.", rejected_reason: null }
  ],
  resolution_or_hold: "Resolved with spaced grammar; preserve as a repeated tooling failure.",
  evidence: [{kind:"producer_metadata", path:"T09_META.md", sha256:artifact("T09_META.md").sha256, result:"Both no-write failures recorded."}],
  residual_risk: "Compressed PowerShell tokens can silently recur in future automation.",
  recurrence_cues: ["foreach($x in$y)", "Where-Object Count -gt1", "operator adjacent to operand"],
  related_structural_ids: ["NOE-P06-KO-T09-001"], related_decision_ids: ["CJK-KO-P06-028","CJK-KO-P06-029"],
  transferable_lesson: "Keep PowerShell grammar visibly spaced and rerun read-only inventories after every parser failure."
});
addDifficulty({
  record_id: "CJK-KO-P06-HARD-028", tranche_ids: ["T11"], unit_ids: ["U153"], state: "resolved", classification: "computation",
  source_locators: ["ED0001/ED0002 lines5417--5422"],
  target_artifacts: [artifact("T11_ROUTE.md"), artifact("T11_META.md"), artifact("targets/T11_U153.tex")],
  symptom: "The provisional U153 range stopped at line5421 and omitted the three-byte closing display delimiter on line5422.",
  cause_evidence: "Exact section reconstruction left three unexplained bytes; extending U153 through line5422 closed the display and reconstruction.",
  attempted_approaches: [
    { approach: "Use provisional lines5417--5421.", outcome: "Three-byte reconstruction gap.", rejected_reason: "Unclosed display." },
    { approach: "Extend through line5422 before target creation.", outcome: "Exact reconstruction and closed target.", rejected_reason: null }
  ],
  resolution_or_hold: "Resolved before target write; no defective target existed.",
  evidence: [{kind:"producer_metadata", path:"T11_META.md", sha256:artifact("T11_META.md").sha256, result:"Corrected route and hashes recorded."}],
  residual_risk: "Display closers on isolated lines can be lost by range tables.",
  recurrence_cues: ["range ends one line before \\]", "three-byte reconstruction gap", "display split"],
  related_structural_ids: ["NOE-P06-KO-T11-U153-EQUATION-001"], related_decision_ids: ["CJK-KO-P06-033","CJK-KO-P06-034"],
  transferable_lesson: "Require whole-section byte reconstruction before any translation target is written."
});
addDifficulty({
  record_id: "CJK-KO-P06-HARD-029", tranche_ids: ["T13"], unit_ids: ["U185"], state: "resolved", classification: "computation",
  source_locators: ["ED0001/ED0002 lines5596--5601"],
  target_artifacts: [artifact("T13_ROUTE.md"), artifact("T13_META.md"), artifact("targets/T13_U185.tex")],
  symptom: "The first unsealed 30-range T13 segmentation omitted line5601, another three-byte closing display delimiter, and split prose/display carriers before closure.",
  cause_evidence: "Exact interval reconstruction exposed the gap; closed-unit review then reduced the route to19 coherent units.",
  attempted_approaches: [
    { approach: "Persist the 30 smaller ranges.", outcome: "Three-byte gap and open carriers.", rejected_reason: "Not reconstructable or closed." },
    { approach: "Replace with19 closed units and include line5601.", outcome: "Exact reconstruction before target write.", rejected_reason: null }
  ],
  resolution_or_hold: "Resolved before target creation; failed route identity was not hashed and remains explicit evidence debt.",
  evidence: [{kind:"producer_metadata", path:"T13_META.md", sha256:artifact("T13_META.md").sha256, result:"Failure and corrected route documented."}],
  residual_risk: "A reconstruction check alone can find missing bytes but not guarantee grammatically closed units.",
  recurrence_cues: ["standalone \\]", "open colon before next display", "over-fragmented unit table"],
  related_structural_ids: ["NOE-P06-KO-T13-U185-EQUATION-001"], related_decision_ids: ["CJK-KO-P06-037","CJK-KO-P06-038"],
  transferable_lesson: "Apply both byte reconstruction and grammatical/structural closure tests to every route."
});
addDifficulty({
  record_id: "CJK-KO-P06-HARD-030", tranche_ids: ["T12"], unit_ids: ["U170"], state: "held", classification: "source_fact",
  source_locators: ["ED0001/ED0002 line5502 literal A_tau(G_i(x)) amid starred notation"],
  target_artifacts: [artifact("targets/T12_U170.tex"), artifact("T12_META.md")],
  symptom: "One A_tau argument is unstarred amid starred neighboring notation.",
  cause_evidence: "The literal source reading is preserved exactly; translation production cannot classify it as defect or intention.",
  attempted_approaches: [
    { approach: "Normalize the star silently.", outcome: "Not attempted.", rejected_reason: "Would be unauthorized German adjudication." },
    { approach: "Preserve literal source and route locator.", outcome: "Checker debt explicit.", rejected_reason: null }
  ],
  resolution_or_hold: "Held for independent checker; only a confirmed finding may go to canon.",
  evidence: [{kind:"producer_metadata", path:"T12_META.md", sha256:artifact("T12_META.md").sha256, result:"Exact locator and no-defect status recorded."}],
  residual_risk: "The target may preserve a source typo or may correctly preserve intentional notation.",
  recurrence_cues: ["starred/unstarred neighbor", "single notation delta", "translator tempted to normalize"],
  related_structural_ids: ["NOE-P06-KO-T12-U170-EQUATION-001"], related_decision_ids: ["CJK-KO-P06-035","CJK-KO-P06-036"],
  transferable_lesson: "Preserve anomalous source notation literally and route it as checker debt, never as a translator defect claim."
});
addDifficulty({
  record_id: "CJK-KO-P06-HARD-031", tranche_ids: ["T15"], unit_ids: ["U212"], state: "held", classification: "editorial_inference",
  source_locators: ["ED0002 line5760 final sentence subject/scope"],
  target_artifacts: [artifact("targets/T15_U212.tex"), artifact("T15_META.md")],
  symptom: "The grammatical subject of the final line5760 clause is difficult to bind after K_i polynomials and quotient functions are both introduced.",
  cause_evidence: "The source syntax permits an attractor toward assigning quotient status to the immediately preceding K_i polynomials.",
  attempted_approaches: [
    { approach: "Silently resolve the subject to K_i.", outcome: "Rejected.", rejected_reason: "Would over-adjudicate source syntax." },
    { approach: "Use an explicit Korean function-level carrier and record the ambiguity.", outcome: "Producer draft remains reviewable.", rejected_reason: null }
  ],
  resolution_or_hold: "Held for independent source/Korean review.",
  evidence: [{kind:"producer_metadata", path:"T15_META.md", sha256:artifact("T15_META.md").sha256, result:"Subject/scope ambiguity recorded."}],
  residual_risk: "A subject shift can change whether numerator polynomials or represented functions belong to the domain.",
  recurrence_cues: ["semicolon after displayed quotient", "pronounless German continuation", "two candidate subjects"],
  related_structural_ids: ["NOE-P06-KO-T15-U212-PROSE-001"], related_decision_ids: ["CJK-KO-P06-042"],
  transferable_lesson: "Expose grammatical subject ambiguity where it affects mathematical membership; do not hide it with fluent Korean."
});
addDifficulty({
  record_id: "CJK-KO-P06-HARD-032", tranche_ids: ["T16"], unit_ids: ["U218"], state: "held", classification: "source_fact",
  source_locators: ["ED0002 line5784 Definition V-prime: deren übrige Polynome"],
  target_artifacts: [artifact("targets/T16_U218.tex"), artifact("T16_META.md")],
  symptom: "Definition V-prime literally says the remaining polynomials rather than the mathematically expected remaining coefficients.",
  cause_evidence: "The translation authority reading is explicit; no checker-confirmed German correction exists.",
  attempted_approaches: [
    { approach: "Translate as coefficients.", outcome: "Rejected.", rejected_reason: "Would silently emend German." },
    { approach: "Translate the literal word and record the locator.", outcome: "Source debt preserved.", rejected_reason: null }
  ],
  resolution_or_hold: "Held for independent checker and, only if confirmed, canon packet.",
  evidence: [{kind:"producer_metadata", path:"T16_META.md", sha256:artifact("T16_META.md").sha256, result:"Literal reading and hold recorded."}],
  residual_risk: "Literal Korean may sound mathematically wrong; silent correction would erase evidence.",
  recurrence_cues: ["definition coefficient list", "Polynome where Koeffizienten expected", "canon temptation"],
  related_structural_ids: ["NOE-P06-KO-T16-U218-DEFINITION-001"], related_decision_ids: ["CJK-KO-P06-044"],
  transferable_lesson: "In translation-only production, preserve suspicious authority words and separate readability debt from canon adjudication."
});
addDifficulty({
  record_id: "CJK-KO-P06-HARD-033", tranche_ids: Array.from({length:16},(_,i)=>"T"+pad2(i+1)), unit_ids: [], state: "active_control", classification: "computation",
  source_locators: ["P06 complete producer span ED0002 lines4576--5828"],
  target_artifacts: [],
  symptom: "All228 Korean units exist, but no independent full-work linguistic/formula review, assembly, compilation, extraction, rendering, or every-page visual QA has occurred.",
  cause_evidence: "The producer role is translation-only; hashes and structure prove custody, not correctness or buildability.",
  attempted_approaches: [
    { approach: "Infer readiness from 228/228 files and control-byte cleanliness.", outcome: "Rejected.", rejected_reason: "Coverage is not validation." },
    { approach: "Freeze exact manifest and separate every downstream gate.", outcome: "Complete producer handoff state.", rejected_reason: null }
  ],
  resolution_or_hold: "Active control pending persistent independent Korean checker and build/render owners.",
  evidence: [],
  residual_risk: "Any unit may contain linguistic, formula, TeX integration, citation, or layout defects despite complete coverage.",
  recurrence_cues: ["complete file count", "clean hashes", "pressure to call final", "no PDF/render"],
  related_structural_ids: ["NOE-P06-KO-WORK-002"], related_decision_ids: ["CJK-KO-P06-044"],
  transferable_lesson: "Never collapse producer coverage, source checking, linguistic approval, compilation, rendering, and visual QA into one status."
});
addDifficulty({
  record_id: "CJK-KO-P06-HARD-034", tranche_ids: ["T01"], unit_ids: ["U01"], state: "resolved", classification: "computation",
  source_locators: ["evidence/extend.mjs initial complete-P06 parseTarget execution"],
  target_artifacts: [artifact("evidence/extend.mjs")],
  symptom: "The first complete-evidence run stopped at U01 with Cannot parse unit header before any evidence or manifest write.",
  cause_evidence: "The parser assumed every header placed T/U and source lines in one Unit field; T01 instead stores T/U in the Work line and the locator in a separate Unit source field.",
  attempted_approaches: [
    { approach: "Apply one combined header regex to every historical tranche dialect.", outcome: "Rejected after exact parse failure.", rejected_reason: "Header formats changed prospectively across T01--T16." },
    { approach: "Parse stable T/U from filenames and source locators from three explicit header dialects.", outcome: "Resolved; all228 units parsed.", rejected_reason: null }
  ],
  resolution_or_hold: "Resolved without writes on the failed run; current generator accepts legacy and compact headers separately.",
  evidence: [{kind:"repaired_generator", path:"evidence/extend.mjs", sha256:artifact("evidence/extend.mjs").sha256, result:"All228 targets parsed and serialized."}],
  residual_risk: "Future target headers may add another dialect; filename and locator parsing must remain separate.",
  recurrence_cues: ["mixed prospective header formats", "combined T/U/locator regex", "Cannot parse unit header"],
  related_structural_ids: ["NOE-P06-KO-T01-U01"], related_decision_ids: ["CJK-KO-P06-044"],
  transferable_lesson: "When metadata syntax evolves across a long production run, parse stable identity and source coordinates independently rather than forcing one historical header grammar."
});
addDifficulty({
  record_id: "CJK-KO-P06-HARD-035", tranche_ids: ["T01"], unit_ids: ["U01"], state: "resolved", classification: "computation",
  source_locators: ["T01 U01 header contains both tranche interval and unit source hashes"],
  target_artifacts: [artifact("evidence/extend.mjs")],
  symptom: "The second complete-evidence run selected the earlier tranche-level SHA in U01's header and reported a false unit-source mismatch before writes.",
  cause_evidence: "A first-match source regex encountered the Paper 6 T01 interval line before the later Unit source line.",
  attempted_approaches: [
    { approach: "Treat the first source-related hash in each header as the unit hash.", outcome: "Rejected after AAC3A731... was compared with computed 2BF1CF07....", rejected_reason: "The header legitimately carries multiple source scopes." },
    { approach: "Compute the exact routed source hash and require it to occur among all declared header hashes.", outcome: "Resolved for all228 targets.", rejected_reason: null }
  ],
  resolution_or_hold: "Resolved without writes on the failed run; scope is now determined from coordinates before hash matching.",
  evidence: [{kind:"repaired_generator", path:"evidence/extend.mjs", sha256:artifact("evidence/extend.mjs").sha256, result:"Exact unit hashes replay for all228 units."}],
  residual_risk: "A future header could omit its unit hash while retaining larger-scope hashes; that must fail explicitly.",
  recurrence_cues: ["multiple SHA-256 values in one header", "first-match regex", "tranche hash before unit hash"],
  related_structural_ids: ["NOE-P06-KO-T01-U01"], related_decision_ids: ["CJK-KO-P06-044"],
  transferable_lesson: "Bind a hash to an already parsed scope; never infer scope from the first nearby digest."
});
addDifficulty({
  record_id: "CJK-KO-P06-HARD-036", tranche_ids: ["T01","T02","T03"], unit_ids: [], state: "resolved", classification: "computation",
  source_locators: ["sealed structural prefix global_order1--156", "evidence/validate.mjs first complete-P06 run"],
  target_artifacts: [artifact("evidence/validate.mjs")],
  symptom: "The first complete validator emitted a replaceable FAIL report because it retroactively applied the later whole-line span-hash rule to sealed T01 subrecords created under an earlier granular hash convention.",
  cause_evidence: "All manifest, unit, difficulty, visual, hierarchy, and new-record checks passed; only old T01 subrecord source/target hash assertions failed. The frozen 216,025-byte prefix already had its own PASS validator and exact prefix SHA.",
  attempted_approaches: [
    { approach: "Require one later hash interpretation for every historical subrecord.", outcome: "Rejected after false failures.", rejected_reason: "Would invalidate sealed evidence semantics retroactively." },
    { approach: "Verify the sealed 156-record prefix by exact byte hash, directly rehash all228 unit records, and directly rehash every record added after the prefix.", outcome: "Resolved; two complete runs produced stable PASS reports.", rejected_reason: null }
  ],
  resolution_or_hold: "Resolved by convention-aware validation; protected target/ledger inputs were unchanged and only generated reports were replaced.",
  evidence: [{kind:"validator", path:"evidence/validate.mjs", sha256:artifact("evidence/validate.mjs").sha256, result:"PASS twice with deterministic report identities."}],
  residual_risk: "Future schema evolution can create another false retroactive assertion unless prefix semantics remain explicit.",
  recurrence_cues: ["append-only schema evolution", "old record hash convention", "broad validator rewrite", "false prefix failure"],
  related_structural_ids: ["NOE-P06-KO-WORK-001","NOE-P06-KO-WORK-002"], related_decision_ids: ["CJK-KO-P06-044"],
  transferable_lesson: "Append-only evidence can evolve, but validators must preserve earlier declared hash semantics through exact prefix receipts rather than silently reinterpret old records."
});
addDifficulty({
  record_id: "CJK-KO-P06-HARD-037", tranche_ids: ["T01","T02","T03"], unit_ids: [], state: "resolved", classification: "computation",
  source_locators: ["CJK-KO-P06-HARD-036 target_artifact identity", "evidence/validate.mjs difficulty-count update"],
  target_artifacts: [],
  symptom: "HARD-036 recorded the then-live validator as a target artifact, but adding HARD-034--036 required the validator's expected difficulty count and cursor to change immediately afterward, so that live path no longer matched the historical digest.",
  cause_evidence: "The old validator was 29,130 bytes / 77D1B64A...; it was not preserved under an immutable filename before the necessary 36-to-37 record update. Mutating HARD-036 would violate append-only history.",
  attempted_approaches: [
    { approach: "Rewrite HARD-036 with the later live validator hash.", outcome: "Rejected.", rejected_reason: "Would silently erase the exact historical identity." },
    { approach: "Append this correction, retain the old identity as historical evidence, and make the validator recognize this one explicitly superseded moving-path assertion.", outcome: "Resolved with an honest reproducibility-debt record.", rejected_reason: null }
  ],
  resolution_or_hold: "HARD-036 remains unchanged; this record explains its historical moving-path identity and the validator exempts only that exact record/path pair when HARD-037 is present.",
  evidence: [
    {kind:"historical_identity", path:"evidence/validate.mjs", sha256:"77D1B64A3701DE3E3BE3DFC88890A16A0602A1AB1A57C70995A3D2C305C4156A", result:"29,130-byte then-live validator; separate bytes were not preserved."},
    {kind:"corrected_validator", path:"evidence/validate.mjs", sha256:"CD2ED687A48F4B8AE8D81BE2573D4300C3B46735C3F8FDF4905A5CDAC641485E", result:"29,398-byte validator with explicit append-only correction semantics."}
  ],
  residual_risk: "Historical script bytes for the 77D1B64A identity cannot be replayed from a separate immutable file.",
  recurrence_cues: ["ledger record points to mutable validator path", "artifact hash changes during count update", "temptation to edit history"],
  related_structural_ids: ["NOE-P06-KO-WORK-001","NOE-P06-KO-WORK-002"], related_decision_ids: ["CJK-KO-P06-044"],
  transferable_lesson: "Never cite a still-moving validator as an immutable artifact; snapshot it first, and if missed, append an explicit correction instead of rewriting the ledger."
});
addDifficulty({
  record_id: "CJK-KO-P06-HARD-038", tranche_ids: ["T01"], unit_ids: ["U01"], state: "resolved", classification: "computation",
  source_locators: ["CJK-KO-P06-HARD-034 and HARD-035 target_artifact identities", "evidence/extend.mjs append-only failure additions"],
  target_artifacts: [],
  symptom: "HARD-034 and HARD-035 recorded the then-live repaired generator at a mutable path; appending HARD-037 changed that same script and caused exact live-artifact validation failures.",
  cause_evidence: "Both records preserve 38,064 bytes / EEB37E34...; the later generator was 40,516 bytes / 8DB8D827... before this corrective definition. No immutable script snapshot had been made.",
  attempted_approaches: [
    { approach: "Rewrite HARD-034/HARD-035 to the newest generator digest.", outcome: "Rejected.", rejected_reason: "Would erase their historically exact identities and recur after every ledger-definition append." },
    { approach: "Append this correction and exempt only those two exact historical record/path pairs while retaining both digests as adverse evidence.", outcome: "Resolved without rewriting prior records.", rejected_reason: null }
  ],
  resolution_or_hold: "HARD-034 and HARD-035 remain unchanged; this record makes their moving-path artifact status explicit. The final handoff separately hashes the live generator.",
  evidence: [
    {kind:"historical_identity", path:"evidence/extend.mjs", sha256:"EEB37E34A446A876203EFDE40917B7A60BBB33ADC4A80E189CA96E612118B8A8", result:"38,064-byte generator cited by HARD-034/HARD-035; separate bytes not retained."},
    {kind:"successor_identity", path:"evidence/extend.mjs", sha256:"8DB8D827AEE87D06373EB800B4D0B0476018DE1BA8FEE6F1CB95E9CAFE67B3EB", result:"40,516-byte successor before this corrective record; separate bytes not retained."}
  ],
  residual_risk: "Neither historical generator version was snapshotted under an immutable filename.",
  recurrence_cues: ["self-modifying evidence generator", "artifact points to its own moving script", "recursive hash mismatch"],
  related_structural_ids: ["NOE-P06-KO-T01-U01"], related_decision_ids: ["CJK-KO-P06-044"],
  transferable_lesson: "Evidence-generating scripts must be snapshotted only after their last edit; never make an append-only record depend on the live hash of the script that still contains future record definitions."
});
fs.writeFileSync(dpath, difficulties.map((r) => JSON.stringify(r)).join("\n") + "\n", "utf8");
const dh = ["record_id","sequence","observed_at","time_precision","state","classification","tranche_ids","unit_ids","source_locators","target_paths","symptom","cause_evidence","resolution_or_hold","residual_risk","related_structural_ids","related_decision_ids","previous_record_id","transferable_lesson"];
const dr = difficulties.map((r) => [r.record_id,r.sequence,r.observed_at,r.time_precision,r.state,r.classification,r.tranche_ids.join("|"),r.unit_ids.join("|"),r.source_locators.join("|"),r.target_artifacts.map((x)=>x.path).join("|"),r.symptom,r.cause_evidence,r.resolution_or_hold,r.residual_risk,r.related_structural_ids.join("|"),r.related_decision_ids.join("|"),r.previous_record_id,r.transferable_lesson]);
fs.writeFileSync(path.join(ddir, "DIFFICULTY_LEDGER.csv"), [dh, ...dr].map((r) => r.map(csvCell).join(",")).join("\n") + "\n", "utf8");

const manifestEntries = units.map((u) => ({
  unit_id: "U" + pad2(u.unit),
  tranche_id: "T" + pad2(u.tranche),
  target_path: u.relPath,
  target_bytes: u.raw.length,
  target_sha256: u.targetSha,
  source_line_start: u.start,
  source_line_end: u.end,
  source_bytes: sourceBytes(u.start, u.end).length,
  source_sha256: u.sourceSha,
  state: "UNCHECKED"
}));
const treeLines = manifestEntries.map((x) => x.target_path + "\0" + x.target_bytes + "\0" + x.target_sha256 + "\n").join("");
const manifest = {
  schema_version: "1.0",
  work_id: "NOE-P06",
  language: "ko",
  pointer_id: pointerId,
  pointer_sha256: pointerSha,
  authority_id: authorityId,
  authority_sha256: authoritySha,
  source_content_lines: [4576, 5828],
  source_content_sha256: sha(sourceBytes(4576, 5828)),
  target_count: manifestEntries.length,
  target_bytes: manifestEntries.reduce((n, x) => n + x.target_bytes, 0),
  target_tree_sha256: sha(utf8(treeLines)),
  missing_units: [],
  duplicate_units: [],
  control_state: { bom_files: 0, cr_files: 0, esc_files: 0, missing_terminal_lf: 0 },
  completion_state: "complete_producer_draft_text_coverage",
  review_state: "unchecked",
  build_state: "not_built",
  render_state: "not_rendered",
  visual_state: "zero_records",
  entries: manifestEntries
};
fs.writeFileSync(path.join(root, "manifest.json"), JSON.stringify(manifest, null, 2) + "\n", "utf8");
const mh = ["unit_id","tranche_id","target_path","target_bytes","target_sha256","source_line_start","source_line_end","source_bytes","source_sha256","state"];
const mr = manifestEntries.map((x) => mh.map((k) => x[k]));
fs.writeFileSync(path.join(root, "manifest.csv"), [mh, ...mr].map((r) => r.map(csvCell).join(",")).join("\n") + "\n", "utf8");

console.log(JSON.stringify({
  structural_added: added.length,
  structural_total: allRecords.length,
  difficulty_total: difficulties.length,
  targets: manifest.target_count,
  target_bytes: manifest.target_bytes,
  target_tree_sha256: manifest.target_tree_sha256,
  source_content_sha256: manifest.source_content_sha256
}, null, 2));
