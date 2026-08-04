import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const dir = path.dirname(fileURLToPath(import.meta.url));
const jsonlPath = path.join(dir, "VISUAL_EVIDENCE.jsonl");
const csvPath = path.join(dir, "VISUAL_EVIDENCE.csv");
if (fs.existsSync(jsonlPath) || fs.existsSync(csvPath)) throw new Error("Visual index already exists; initializer refuses to overwrite it");
fs.writeFileSync(jsonlPath, Buffer.alloc(0), { flag: "wx" });
const headers = [
  "visual_id", "kind", "path", "image_sha256", "parent_scan_path",
  "parent_scan_sha256", "parent_page", "page_coordinates", "bbox_x", "bbox_y",
  "bbox_width", "bbox_height", "bbox_units", "width_px", "height_px", "dpi",
  "rotation_degrees", "linked_structural_ids", "linked_tex_units", "language",
  "qa_status", "review_status", "rights_basis", "publication_disposition",
  "supersession_state", "continuation_cursor"
];
fs.writeFileSync(csvPath, headers.join(",") + "\n", { encoding: "utf8", flag: "wx" });
const report = {
  initialized_at: new Date().toISOString(),
  record_count: 0,
  image_file_count: 0,
  image_bytes: 0,
  operation: "zero visual-evidence inventory; no render or visual QA performed"
};
fs.writeFileSync(path.join(dir, "INITIALIZATION_REPORT.json"), JSON.stringify(report, null, 2) + "\n", "utf8");
console.log(JSON.stringify(report));
