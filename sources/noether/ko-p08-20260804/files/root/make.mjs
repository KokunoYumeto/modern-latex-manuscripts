import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";

const root = path.dirname(fileURLToPath(import.meta.url));
const authority = "C:\\Users\\Floris\\Documents\\interlanguage\\03_projects\\noether\\07_german_canon_control\\candidates\\ED0002\\noether.tex";
const authoritySha = "C9A125167ACB33D914EE4374B65AE7CDF0052F568371B8B77B720EA178ABF0E3";
const sha = (bytes) => crypto.createHash("sha256").update(bytes).digest("hex").toUpperCase();
const raw = fs.readFileSync(authority);
if (sha(raw) !== authoritySha) throw new Error("ED0002 identity changed");
const lines = raw.toString("utf8").replace(/\r\n/g, "\n").replace(/\r/g, "\n").split("\n");
const slice = Buffer.from(lines.slice(5956, 6347).join("\n") + "\n", "utf8");
if (slice.length !== 25408 || sha(slice) !== "A93B840B48790DFCFB356C648C46FEC16586BBE3A17CCB98026C63F54B8DDE15") {
  throw new Error("P08 interval identity mismatch");
}
fs.writeFileSync(path.join(root, "source.tex"), slice);
const first = lines[5956];
const last = lines[6346];
const next = lines[6347];
console.log(JSON.stringify({
  authority_bytes: raw.length,
  authority_sha256: sha(raw),
  source_lines: [5957, 6347],
  source_bytes: slice.length,
  source_sha256: sha(slice),
  first,
  last,
  next
}, null, 2));
