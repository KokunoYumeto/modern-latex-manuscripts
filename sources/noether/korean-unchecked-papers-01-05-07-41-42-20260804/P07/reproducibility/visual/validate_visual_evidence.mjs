import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const dir = path.dirname(fileURLToPath(import.meta.url));
const jsonlPath = path.join(dir, "VISUAL_EVIDENCE.jsonl");
const csvPath = path.join(dir, "VISUAL_EVIDENCE.csv");
const errors = [];
const jsonl = fs.readFileSync(jsonlPath);
const csv = fs.readFileSync(csvPath, "utf8").replace(/\r\n/g, "\n");
const expectedHeader = "visual_id,kind,path,image_sha256,parent_scan_path,parent_scan_sha256,parent_page,page_coordinates,bbox_x,bbox_y,bbox_width,bbox_height,bbox_units,width_px,height_px,dpi,rotation_degrees,linked_structural_ids,linked_tex_units,language,qa_status,review_status,rights_basis,publication_disposition,supersession_state,continuation_cursor\n";
if (jsonl.length !== 0) errors.push("Expected zero-byte JSONL for zero-record inventory");
if (csv !== expectedHeader) errors.push("CSV is not the exact zero-record header projection");

const report = {
  validated_at: new Date().toISOString(),
  operation: "zero visual-evidence inventory validation; not visual QA",
  pass: errors.length === 0,
  record_count: 0,
  image_file_count: 0,
  image_bytes: 0,
  jsonl_sha256: crypto.createHash("sha256").update(jsonl).digest("hex").toUpperCase(),
  rights_basis_totals: {
    project_generated: 0,
    public_domain: 0,
    licensed: 0,
    fair_use_research: 0,
    unresolved: 0
  },
  publication_disposition_totals: {
    public_safe: 0,
    rights_blocked: 0,
    private_only: 0,
    excluded: 0,
    pending: 0
  },
  qa_status_totals: {
    uninspected: 0,
    producer_inventory_only: 0,
    qa_pass: 0,
    qa_fail: 0
  },
  continuation_cursor: "No visual cursor until a separately authorized source-check or render role creates evidence",
  errors
};
fs.writeFileSync(path.join(dir, "VALIDATION_REPORT.json"), JSON.stringify(report, null, 2) + "\n", "utf8");
console.log(JSON.stringify(report));
if (errors.length) process.exitCode = 1;
