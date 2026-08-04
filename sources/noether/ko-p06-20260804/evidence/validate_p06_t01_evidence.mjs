import fs from "node:fs";
import path from "node:path";
import crypto from "node:crypto";
import { fileURLToPath } from "node:url";
const evidenceRoot = path.dirname(fileURLToPath(import.meta.url));
const producerRoot = path.dirname(evidenceRoot);
const workspaceRoot = path.resolve(producerRoot, "../../../../..");
const sha = b => crypto.createHash("sha256").update(b).digest("hex").toUpperCase();
const read = p => fs.readFileSync(p);
const text = p => read(p).toString("utf8");
const assert = (ok, message) => { if (!ok) throw new Error(message); };
const parseJsonl = p => {
  const s = text(p);
  if (s.length === 0) return [];
  return s.split(/\r?\n/).filter(Boolean).map((line, i) => {
    try { return JSON.parse(line); } catch (e) { throw new Error(path.basename(p) + " line " + (i + 1) + ": " + e.message); }
  });
};
const parseCsv = s => {
  const rows=[]; let row=[], field="", quoted=false;
  for(let i=0;i<s.length;i++){
    const c=s[i];
    if(quoted){
      if(c === '"' && s[i+1] === '"'){ field+='"'; i++; }
      else if(c === '"'){ quoted=false; }
      else field+=c;
    } else {
      if(c === '"') quoted=true;
      else if(c === ','){ row.push(field); field=""; }
      else if(c === '\n'){ row.push(field.replace(/\r$/,"")); rows.push(row); row=[]; field=""; }
      else field+=c;
    }
  }
  if(field.length || row.length){ row.push(field); rows.push(row); }
  return rows;
};
const expectedTargets = [
  ["Noether_P06_Korean_T01_U01_UNCHECKED.tex",2267,"E1BD1A9780B04F63B2D2DC6971CCDDC4E4BD130BFE19E9CB8F71E9000F15A147"],
  ["Noether_P06_Korean_T01_U02_UNCHECKED.tex",2976,"1C3DA0C8E5AB2A375A0D488D6CA5E03D5DC19115D98FC005281367D4D7E6A087"],
  ["Noether_P06_Korean_T01_U03_UNCHECKED.tex",1325,"90A6AACB82FE50298AA2867932F8058AF9F90A3632AF14DFBB36F0B852564613"],
  ["Noether_P06_Korean_T01_U04_UNCHECKED.tex",2047,"B56032995438B4F8E770FDCA748EAC2234328E788CE30C616E3C732B2A412E66"],
  ["Noether_P06_Korean_T01_U05_UNCHECKED.tex",1900,"E0E949C08BA55DD02705CB9A1911968993F4434826216DD08A2F039C3133942C"],
  ["Noether_P06_Korean_T01_U06_UNCHECKED.tex",1190,"2B0768AF051C7C58662E2021E878F1B15B6ED5B56C594D4A4AE5C5EEAB994B82"]
];
let total=0; const concatenated=[];
for(const [name,bytes,digest] of expectedTargets){
  const b=read(path.join(producerRoot,"targets",name));
  assert(b.length===bytes,name+" byte mismatch");
  assert(sha(b)===digest,name+" hash mismatch");
  total+=b.length; concatenated.push(b);
}
assert(total===11705,"target total bytes mismatch");
assert(sha(Buffer.concat(concatenated))==="9F290D1306FE6E389D39736D6FE6918B214FB369D20363EB219EC6D951FAE9EE","target concatenation digest mismatch");
const route=read(path.join(producerRoot,"ROUTE_AND_CLAIM_T01_INTRO.md"));
assert(route.length===2231,"route bytes mismatch");
assert(sha(route)==="5C5448ED2F53B5FDB1E2A772CB9DECF14EA7E4C58FDD26F1A376221F0A4EC3D2","route hash mismatch");
const structuralPath=path.join(evidenceRoot,"structural_index","PRODUCER_STRUCTURAL_INDEX.jsonl");
const structural=parseJsonl(structuralPath);
assert(structural.length===52,"structural count mismatch");
const ids=new Set(structural.map(r=>r.structural_id));
assert(ids.size===52,"duplicate structural ID");
const expectedTypes={work:1,tranche:1,unit:6,heading:1,bibliographic_item:3,prose:12,definition:9,equation:2,footnote:2,cross_reference:14,statement:1};
const types={};
for(const r of structural){
  types[r.record_type]=(types[r.record_type]||0)+1;
  assert(r.review_state==="unchecked","non-unchecked structural record");
  assert(/^[A-F0-9]{64}$/.test(r.source_sha256),"bad source hash "+r.structural_id);
  assert(/^[A-F0-9]{64}$/.test(r.target_sha256),"bad target hash "+r.structural_id);
  if(r.parent_id!==null) assert(ids.has(r.parent_id),"missing parent "+r.parent_id);
  for(const rel of r.relations) if(rel.scope==="internal") assert(ids.has(rel.target_id),"missing internal relation "+rel.target_id);
}
assert(Object.entries(expectedTypes).every(([k,v])=>types[k]===v) && Object.keys(types).length===Object.keys(expectedTypes).length,"structural type counts mismatch: "+JSON.stringify(types));
const sCsv=parseCsv(text(path.join(evidenceRoot,"structural_index","PRODUCER_STRUCTURAL_INDEX.csv")));
assert(sCsv.length===53,"structural CSV row count mismatch");
assert(new Set(sCsv.slice(1).map(r=>r[0])).size===52,"structural CSV ID mismatch");
const difficultyPath=path.join(evidenceRoot,"difficulty_ledger","DIFFICULTY_LEDGER.jsonl");
const difficulty=parseJsonl(difficultyPath);
assert(difficulty.length===11,"difficulty count mismatch");
const dids=new Set(difficulty.map(r=>r.record_id));
assert(dids.size===difficulty.length,"duplicate difficulty ID");
for(let i=0;i<difficulty.length;i++){
  const r=difficulty[i];
  assert(r.sequence===i+1,"difficulty sequence mismatch");
  assert(r.previous_record_id===(i===0?null:difficulty[i-1].record_id),"difficulty predecessor mismatch");
}
const dCsv=parseCsv(text(path.join(evidenceRoot,"difficulty_ledger","DIFFICULTY_LEDGER.csv")));
assert(dCsv.length===difficulty.length+1,"difficulty CSV row count mismatch");
assert(new Set(dCsv.slice(1).map(r=>r[0])).size===difficulty.length,"difficulty CSV ID mismatch");
const stateCounts=difficulty.reduce((a,r)=>(a[r.state]=(a[r.state]||0)+1,a),{});
assert(stateCounts.resolved===7 && stateCounts.held===3 && stateCounts.active_control===1,"difficulty state counts mismatch");
const visualPath=path.join(evidenceRoot,"visual_evidence","VISUAL_EVIDENCE_INDEX.jsonl");
const visual=parseJsonl(visualPath);
assert(visual.length===0,"visual index must be empty");
const vCsv=parseCsv(text(path.join(evidenceRoot,"visual_evidence","VISUAL_EVIDENCE_INDEX.csv")));
assert(vCsv.length===1,"visual CSV must be header-only");
const images=[];
const walk=dir=>{for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=path.join(dir,e.name);if(e.isDirectory())walk(p);else if(/\.(png|jpe?g|gif|tiff?|webp|bmp)$/i.test(e.name))images.push(p);}};
walk(producerRoot);
assert(images.length===0,"unexpected image evidence file");
const pointer=read(path.join(workspaceRoot,"03_projects","noether","07_german_canon_control","pointers","NOETH_DE_AUTHORITY_POINTER_v006_20260804.json"));
assert(pointer.length===20666,"pointer bytes mismatch");
assert(sha(pointer)==="DB99DD87100654674D7ED24B4ABBBBC3A9920CCF035740D276CE8A87A5313C18","pointer hash mismatch");
const livePointer=read(path.join(workspaceRoot,"03_projects","noether","07_german_canon_control","CURRENT_GERMAN_AUTHORITY_POINTER.json"));
const result={
  status:"PASS",
  scope:"P06 T01 U01--U06 producer metadata integrity only",
  structural:{records:52,unique_ids:52,type_counts:types,jsonl_sha256:sha(read(structuralPath)),csv_sha256:sha(read(path.join(evidenceRoot,"structural_index","PRODUCER_STRUCTURAL_INDEX.csv")))},
  difficulty:{records:difficulty.length,unique_ids:dids.size,states:stateCounts,latest_record_id:difficulty.at(-1).record_id,jsonl_sha256:sha(read(difficultyPath)),csv_sha256:sha(read(path.join(evidenceRoot,"difficulty_ledger","DIFFICULTY_LEDGER.csv")))},
  visual:{records:0,image_files:0,render_calls:0,jsonl_sha256:sha(read(visualPath)),csv_sha256:sha(read(path.join(evidenceRoot,"visual_evidence","VISUAL_EVIDENCE_INDEX.csv")))},
  protected_inputs:{route_files:1,target_files:6,target_bytes:11705,target_concat_sha256:"9F290D1306FE6E389D39736D6FE6918B214FB369D20363EB219EC6D951FAE9EE",mutations:0},
  binding_pointer:{id:"NOETH-DE-AUTH-v006-20260804",bytes:20666,sha256:"DB99DD87100654674D7ED24B4ABBBBC3A9920CCF035740D276CE8A87A5313C18"},
  live_pointer_observation:{bytes:livePointer.length,sha256:sha(livePointer),binding_changed:false},
  limits:["No source or scan adjudication","No Korean or formula review","No compilation or rendering","No assembly packaging certification or approval"]
};
process.stdout.write(JSON.stringify(result,null,2)+"\n");
