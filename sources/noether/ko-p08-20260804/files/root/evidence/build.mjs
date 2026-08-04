import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

const root = path.resolve(import.meta.dirname, '..');
const outDir = import.meta.dirname;
const sourcePath = path.join(root, 'source.tex');
const authorityPath = 'C:\\Users\\Floris\\Documents\\interlanguage\\03_projects\\noether\\07_german_canon_control\\candidates\\ED0002\\noether.tex';
const authoritySha = 'C9A125167ACB33D914EE4374B65AE7CDF0052F568371B8B77B720EA178ABF0E3';
const sourceBase = 5957;

function sha(bytes) {
  return crypto.createHash('sha256').update(bytes).digest('hex').toUpperCase();
}

function linesOf(file) {
  const text = fs.readFileSync(file, 'utf8');
  const lines = text.split('\n');
  if (lines.at(-1) === '') lines.pop();
  return lines;
}

const sourceLines = linesOf(sourcePath);

function sliceLines(lines, start, end, base) {
  const text = lines.slice(start - base, end - base + 1).join('\n') + '\n';
  return Buffer.from(text, 'utf8');
}

function csvCell(value) {
  const text = value === null || value === undefined ? '' : String(value);
  return '"' + text.replaceAll('"', '""') + '"';
}

const defs = [
  ['CJK-KO-P08-STR-0001','work',null,1,5957,6025,null,null,null,'partial',[]],
  ['CJK-KO-P08-STR-0002','tranche','CJK-KO-P08-STR-0001',1,5957,5977,null,null,null,'draft_complete',[]],
  ['CJK-KO-P08-STR-0003','unit','CJK-KO-P08-STR-0002',1,5957,5969,'targets/T01_U01.tex',1,18,'draft_complete',[]],
  ['CJK-KO-P08-STR-0004','section_title','CJK-KO-P08-STR-0003',1,5957,5957,'targets/T01_U01.tex',6,6,'draft_complete',[]],
  ['CJK-KO-P08-STR-0005','publication_note','CJK-KO-P08-STR-0003',2,5958,5960,'targets/T01_U01.tex',7,9,'draft_complete',[]],
  ['CJK-KO-P08-STR-0006','title_block','CJK-KO-P08-STR-0003',3,5962,5969,'targets/T01_U01.tex',11,18,'draft_complete',[]],
  ['CJK-KO-P08-STR-0007','unit','CJK-KO-P08-STR-0002',2,5971,5973,'targets/T01_U02.tex',1,8,'draft_complete',[]],
  ['CJK-KO-P08-STR-0008','prose','CJK-KO-P08-STR-0007',1,5971,5971,'targets/T01_U02.tex',6,6,'draft_complete',[]],
  ['CJK-KO-P08-STR-0009','theorem_statement','CJK-KO-P08-STR-0007',2,5973,5973,'targets/T01_U02.tex',8,8,'draft_complete',[]],
  ['CJK-KO-P08-STR-0010','source_note','CJK-KO-P08-STR-0009',1,5973,5973,'targets/T01_U02.tex',8,8,'draft_complete',[]],
  ['CJK-KO-P08-STR-0011','bibliography_item','CJK-KO-P08-STR-0010',1,5973,5973,'targets/T01_U02.tex',8,8,'draft_complete',[]],
  ['CJK-KO-P08-STR-0012','bibliography_item','CJK-KO-P08-STR-0010',2,5973,5973,'targets/T01_U02.tex',8,8,'draft_complete',[]],
  ['CJK-KO-P08-STR-0013','bibliography_item','CJK-KO-P08-STR-0010',3,5973,5973,'targets/T01_U02.tex',8,8,'draft_complete',[]],
  ['CJK-KO-P08-STR-0014','bibliography_item','CJK-KO-P08-STR-0010',4,5973,5973,'targets/T01_U02.tex',8,8,'draft_complete',[]],
  ['CJK-KO-P08-STR-0015','unit','CJK-KO-P08-STR-0002',3,5975,5977,'targets/T01_U03.tex',1,8,'draft_complete',[]],
  ['CJK-KO-P08-STR-0016','prose','CJK-KO-P08-STR-0015',1,5975,5975,'targets/T01_U03.tex',6,6,'draft_complete',[]],
  ['CJK-KO-P08-STR-0017','source_note','CJK-KO-P08-STR-0016',1,5975,5975,'targets/T01_U03.tex',6,6,'draft_complete',[]],
  ['CJK-KO-P08-STR-0018','bibliography_item','CJK-KO-P08-STR-0017',1,5975,5975,'targets/T01_U03.tex',6,6,'draft_complete',[]],
  ['CJK-KO-P08-STR-0019','prose','CJK-KO-P08-STR-0015',2,5977,5977,'targets/T01_U03.tex',8,8,'draft_complete',[]],
  ['CJK-KO-P08-STR-0020','tranche','CJK-KO-P08-STR-0001',2,5979,6025,null,null,null,'draft_complete',[]],
  ['CJK-KO-P08-STR-0021','unit','CJK-KO-P08-STR-0020',1,5979,5996,'targets/T02_U04.tex',1,23,'draft_complete',[]],
  ['CJK-KO-P08-STR-0022','section_heading','CJK-KO-P08-STR-0021',1,5979,5979,'targets/T02_U04.tex',6,6,'draft_complete',[]],
  ['CJK-KO-P08-STR-0023','prose','CJK-KO-P08-STR-0021',2,5980,5980,'targets/T02_U04.tex',7,7,'draft_complete',[]],
  ['CJK-KO-P08-STR-0024','display','CJK-KO-P08-STR-0021',3,5981,5983,'targets/T02_U04.tex',8,10,'draft_complete',[]],
  ['CJK-KO-P08-STR-0025','prose','CJK-KO-P08-STR-0021',4,5984,5984,'targets/T02_U04.tex',11,11,'draft_complete',[]],
  ['CJK-KO-P08-STR-0026','display','CJK-KO-P08-STR-0021',5,5985,5987,'targets/T02_U04.tex',12,14,'draft_complete',[]],
  ['CJK-KO-P08-STR-0027','definition','CJK-KO-P08-STR-0021',6,5988,5988,'targets/T02_U04.tex',15,15,'draft_complete',[]],
  ['CJK-KO-P08-STR-0028','equation_display','CJK-KO-P08-STR-0021',7,5989,5995,'targets/T02_U04.tex',16,22,'draft_complete',[]],
  ['CJK-KO-P08-STR-0029','prose','CJK-KO-P08-STR-0021',8,5996,5996,'targets/T02_U04.tex',23,23,'draft_complete',[]],
  ['CJK-KO-P08-STR-0030','unit','CJK-KO-P08-STR-0020',2,5998,6007,'targets/T02_U05.tex',1,15,'draft_complete',[]],
  ['CJK-KO-P08-STR-0031','theorem_statement','CJK-KO-P08-STR-0030',1,5998,5998,'targets/T02_U05.tex',6,6,'draft_complete',[['contains','CJK-KO-P08-STR-0032'],['continued_by','CJK-KO-P08-STR-0033']]],
  ['CJK-KO-P08-STR-0032','equation','CJK-KO-P08-STR-0030',2,5999,6002,'targets/T02_U05.tex',7,10,'draft_complete',[['referenced_by','CJK-KO-P08-STR-0042']]],
  ['CJK-KO-P08-STR-0033','prose','CJK-KO-P08-STR-0030',3,6003,6007,'targets/T02_U05.tex',11,15,'draft_complete',[]],
  ['CJK-KO-P08-STR-0034','display','CJK-KO-P08-STR-0033',1,6004,6006,'targets/T02_U05.tex',12,14,'draft_complete',[]],
  ['CJK-KO-P08-STR-0035','unit','CJK-KO-P08-STR-0020',3,6009,6017,'targets/T02_U06.tex',1,14,'draft_complete',[]],
  ['CJK-KO-P08-STR-0036','prose','CJK-KO-P08-STR-0035',1,6009,6009,'targets/T02_U06.tex',6,6,'draft_complete',[]],
  ['CJK-KO-P08-STR-0037','display','CJK-KO-P08-STR-0035',2,6010,6012,'targets/T02_U06.tex',7,9,'draft_complete',[]],
  ['CJK-KO-P08-STR-0038','prose','CJK-KO-P08-STR-0035',3,6013,6013,'targets/T02_U06.tex',10,10,'draft_complete',[]],
  ['CJK-KO-P08-STR-0039','display','CJK-KO-P08-STR-0035',4,6014,6016,'targets/T02_U06.tex',11,13,'draft_complete',[]],
  ['CJK-KO-P08-STR-0040','theorem_statement','CJK-KO-P08-STR-0035',5,6017,6017,'targets/T02_U06.tex',14,14,'draft_complete',[]],
  ['CJK-KO-P08-STR-0041','unit','CJK-KO-P08-STR-0020',4,6019,6025,'targets/T02_U07.tex',1,12,'draft_complete',[]],
  ['CJK-KO-P08-STR-0042','proof','CJK-KO-P08-STR-0041',1,6019,6021,'targets/T02_U07.tex',6,8,'draft_complete',[['references','CJK-KO-P08-STR-0032']]],
  ['CJK-KO-P08-STR-0043','equation_display','CJK-KO-P08-STR-0041',2,6022,6024,'targets/T02_U07.tex',9,11,'draft_complete',[]],
  ['CJK-KO-P08-STR-0044','proof','CJK-KO-P08-STR-0041',3,6025,6025,'targets/T02_U07.tex',12,12,'draft_complete',[['concludes','CJK-KO-P08-STR-0040']]],
  ['CJK-KO-P08-STR-0045','tranche','CJK-KO-P08-STR-0001',3,6027,6097,null,null,null,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0046','unit','CJK-KO-P08-STR-0045',1,6027,6028,'targets/T03_U08.tex',1,7,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0047','section_heading','CJK-KO-P08-STR-0046',1,6027,6027,'targets/T03_U08.tex',6,6,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0048','definition','CJK-KO-P08-STR-0046',2,6028,6028,'targets/T03_U08.tex',7,7,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0049','source_note','CJK-KO-P08-STR-0048',1,6028,6028,'targets/T03_U08.tex',7,7,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0050','proposition','CJK-KO-P08-STR-0046',3,6028,6028,'targets/T03_U08.tex',7,7,'draft_complete',[['used_by','CJK-KO-P08-STR-0054']],6099],
  ['CJK-KO-P08-STR-0051','unit','CJK-KO-P08-STR-0045',2,6030,6034,'targets/T03_U09.tex',1,10,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0052','prose','CJK-KO-P08-STR-0051',1,6030,6030,'targets/T03_U09.tex',6,6,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0053','equation_display','CJK-KO-P08-STR-0051',2,6031,6033,'targets/T03_U09.tex',7,9,'draft_complete',[['same_formula_as','CJK-KO-P08-STR-0032']],6099],
  ['CJK-KO-P08-STR-0054','proposition','CJK-KO-P08-STR-0051',3,6034,6034,'targets/T03_U09.tex',10,10,'draft_complete',[['uses','CJK-KO-P08-STR-0050']],6099],
  ['CJK-KO-P08-STR-0055','unit','CJK-KO-P08-STR-0045',3,6036,6040,'targets/T03_U10.tex',1,10,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0056','prose','CJK-KO-P08-STR-0055',1,6036,6036,'targets/T03_U10.tex',6,6,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0057','display','CJK-KO-P08-STR-0055',2,6037,6039,'targets/T03_U10.tex',7,9,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0058','prose','CJK-KO-P08-STR-0055',3,6040,6040,'targets/T03_U10.tex',10,10,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0059','unit','CJK-KO-P08-STR-0045',4,6042,6042,'targets/T03_U11.tex',1,7,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0060','definition','CJK-KO-P08-STR-0059',1,6042,6042,'targets/T03_U11.tex',7,7,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0061','unit','CJK-KO-P08-STR-0045',5,6044,6080,'targets/T03_U12.tex',1,43,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0062','definition','CJK-KO-P08-STR-0061',1,6044,6044,'targets/T03_U12.tex',7,7,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0063','equation_display','CJK-KO-P08-STR-0061',2,6045,6047,'targets/T03_U12.tex',8,10,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0064','equation_display','CJK-KO-P08-STR-0061',3,6049,6055,'targets/T03_U12.tex',12,18,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0065','equation_display','CJK-KO-P08-STR-0061',4,6057,6061,'targets/T03_U12.tex',20,24,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0066','source_note','CJK-KO-P08-STR-0061',5,6062,6079,'targets/T03_U12.tex',25,42,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0067','equation_display','CJK-KO-P08-STR-0066',1,6063,6065,'targets/T03_U12.tex',26,28,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0068','equation_display','CJK-KO-P08-STR-0066',2,6067,6071,'targets/T03_U12.tex',30,34,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0069','equation_display','CJK-KO-P08-STR-0066',3,6072,6079,'targets/T03_U12.tex',35,42,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0070','prose','CJK-KO-P08-STR-0061',6,6080,6080,'targets/T03_U12.tex',43,43,'draft_complete',[['relates_to','CJK-KO-P08-STR-0032']],6099],
  ['CJK-KO-P08-STR-0071','unit','CJK-KO-P08-STR-0045',6,6082,6097,'targets/T03_U13.tex',1,22,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0072','definition','CJK-KO-P08-STR-0071',1,6082,6082,'targets/T03_U13.tex',7,7,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0073','equation_display','CJK-KO-P08-STR-0071',2,6083,6090,'targets/T03_U13.tex',8,15,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0074','equation_display','CJK-KO-P08-STR-0071',3,6092,6096,'targets/T03_U13.tex',17,21,'draft_complete',[],6099],
  ['CJK-KO-P08-STR-0075','prose','CJK-KO-P08-STR-0071',4,6097,6097,'targets/T03_U13.tex',22,22,'draft_complete',[['relates_to','CJK-KO-P08-STR-0032']],6099]
];

let autoNumber = 76;
function nextStructureId() {
  const id = 'CJK-KO-P08-STR-' + String(autoNumber).padStart(4, '0');
  autoNumber += 1;
  return id;
}

function displaySpans(lines, start, end, base) {
  const spans = [];
  let open = null;
  let kind = null;
  for (let line = start; line <= end; line += 1) {
    const text = lines[line - base].trim();
    if (open === null && text === '\\[') {
      open = line;
      kind = 'equation_display';
    } else if (open === null && text === '\\begin{equation}') {
      open = line;
      kind = 'equation';
    } else if (open !== null && kind === 'equation_display' && /^\\\](?:})?$/.test(text)) {
      spans.push([open, line, kind]);
      open = null;
      kind = null;
    } else if (open !== null && kind === 'equation' && text === '\\end{equation}') {
      spans.push([open, line, kind]);
      open = null;
      kind = null;
    }
  }
  if (open !== null) throw new Error('Unclosed display at line ' + String(open));
  return spans;
}

function noteSpans(lines, start, end, base) {
  const spans = [];
  let open = null;
  let depth = 0;
  for (let line = start; line <= end; line += 1) {
    const text = lines[line - base];
    if (open === null && text.includes('\\srcfntext{')) {
      open = line;
      depth = 0;
    }
    if (open !== null) {
      for (const char of text) {
        if (char === '{') depth += 1;
        if (char === '}') depth -= 1;
      }
      if (depth === 0) {
        spans.push([open, line]);
        open = null;
      }
    }
  }
  if (open !== null) throw new Error('Unclosed source note at line ' + String(open));
  return spans;
}

function bodyBlocks(lines, start, end, base) {
  const spans = [];
  let open = null;
  for (let line = start; line <= end; line += 1) {
    const text = lines[line - base];
    if (text.trim() && open === null) open = line;
    if ((!text.trim() || line === end) && open !== null) {
      const close = text.trim() && line === end ? line : line - 1;
      spans.push([open, close]);
      open = null;
    }
  }
  return spans;
}

const completeWorkId = nextStructureId();
defs.push([
  completeWorkId,'work_complete',null,2,5957,6347,null,null,null,'draft_complete',
  [['supersedes','CJK-KO-P08-STR-0001'],['includes','CJK-KO-P08-STR-0002'],['includes','CJK-KO-P08-STR-0020'],['includes','CJK-KO-P08-STR-0045']],6348
]);

const autoTranches = [
  {id:'T04', order:4, start:6099, end:6129, next:6131, units:[
    ['U14',6099,6099],['U15',6101,6110],['U16',6112,6120],['U17',6121,6129]
  ]},
  {id:'T05', order:5, start:6131, end:6181, next:6183, units:[
    ['U18',6131,6138],['U19',6139,6159],['U20',6160,6179],['U21',6181,6181]
  ]},
  {id:'T06', order:6, start:6183, end:6226, next:6228, units:[
    ['U22',6183,6187],['U23',6189,6191],['U24',6193,6203],['U25',6205,6220],['U26',6222,6226]
  ]},
  {id:'T07', order:7, start:6228, end:6288, next:6290, units:[
    ['U27',6228,6235],['U28',6237,6239],['U29',6241,6254],['U30',6256,6256],['U31',6258,6288]
  ]},
  {id:'T08', order:8, start:6290, end:6347, next:6348, units:[
    ['U32',6290,6308],['U33',6310,6326],['U34',6327,6332],['U35',6334,6339],['U36',6341,6347]
  ]}
];

for (const tranche of autoTranches) {
  const trancheRecordId = nextStructureId();
  defs.push([trancheRecordId,'tranche',completeWorkId,tranche.order,tranche.start,tranche.end,null,null,null,'draft_complete',[],tranche.next]);
  let unitOrder = 0;
  for (const unit of tranche.units) {
    unitOrder += 1;
    const targetRelative = 'targets/' + tranche.id + '_' + unit[0] + '.tex';
    const targetLines = linesOf(path.join(root, targetRelative));
    const unitRecordId = nextStructureId();
    defs.push([unitRecordId,'unit',trancheRecordId,unitOrder,unit[1],unit[2],targetRelative,1,targetLines.length,'draft_complete',[],tranche.next]);

    let childOrder = 0;
    const targetBlocks = bodyBlocks(targetLines, 6, targetLines.length, 1);
    for (const block of targetBlocks) {
      const blockText = targetLines.slice(block[0] - 1, block[1]).join('\n');
      if (!/[가-힣]/.test(blockText)) continue;
      childOrder += 1;
      let type = 'prose';
      if (blockText.includes('보조정리')) type = 'lemma';
      if (/에를랑겐,/.test(blockText)) type = 'publication_note';
      defs.push([nextStructureId(),type,unitRecordId,childOrder,unit[1],unit[2],targetRelative,block[0],block[1],'draft_complete',[['bounded_by',unitRecordId]],tranche.next]);
    }

    const sourceDisplays = displaySpans(sourceLines, unit[1], unit[2], sourceBase);
    const targetDisplays = displaySpans(targetLines, 6, targetLines.length, 1);
    if (sourceDisplays.length !== targetDisplays.length) {
      throw new Error(targetRelative + ' display count differs from source: ' + String(sourceDisplays.length) + '/' + String(targetDisplays.length));
    }
    for (let index = 0; index < sourceDisplays.length; index += 1) {
      childOrder += 1;
      defs.push([
        nextStructureId(),sourceDisplays[index][2],unitRecordId,childOrder,
        sourceDisplays[index][0],sourceDisplays[index][1],targetRelative,
        targetDisplays[index][0],targetDisplays[index][1],'draft_complete',[],tranche.next
      ]);
    }

    const sourceNotes = noteSpans(sourceLines, unit[1], unit[2], sourceBase);
    const targetNotes = noteSpans(targetLines, 6, targetLines.length, 1);
    if (sourceNotes.length !== targetNotes.length) {
      throw new Error(targetRelative + ' source-note count differs from source: ' + String(sourceNotes.length) + '/' + String(targetNotes.length));
    }
    for (let index = 0; index < sourceNotes.length; index += 1) {
      childOrder += 1;
      defs.push([
        nextStructureId(),'source_note',unitRecordId,childOrder,
        sourceNotes[index][0],sourceNotes[index][1],targetRelative,
        targetNotes[index][0],targetNotes[index][1],'draft_complete',[],tranche.next
      ]);
    }

    const sourceControls = [];
    for (let line = unit[1]; line <= unit[2]; line += 1) {
      if (/^\\(?:clearpage|setcounter)/.test(sourceLines[line - sourceBase].trim())) sourceControls.push(line);
    }
    const targetControls = [];
    for (let line = 6; line <= targetLines.length; line += 1) {
      if (/^\\(?:clearpage|setcounter)/.test(targetLines[line - 1].trim())) targetControls.push(line);
    }
    if (sourceControls.length !== targetControls.length) {
      throw new Error(targetRelative + ' terminal control count differs from source');
    }
    for (let index = 0; index < sourceControls.length; index += 1) {
      childOrder += 1;
      defs.push([
        nextStructureId(),'control_line',unitRecordId,childOrder,
        sourceControls[index],sourceControls[index],targetRelative,
        targetControls[index],targetControls[index],'draft_complete',[],tranche.next
      ]);
    }
  }
}

const records = defs.map(function (d) {
  const sourceBytes = sliceLines(sourceLines, d[4], d[5], sourceBase);
  let target = null;
  if (d[6]) {
    const targetPath = path.join(root, d[6]);
    const targetLines = linesOf(targetPath);
    const targetBytes = sliceLines(targetLines, d[7], d[8], 1);
    target = {
      path: d[6],
      line_start: d[7],
      line_end: d[8],
      bytes: targetBytes.length,
      sha256: sha(targetBytes)
    };
  }
  const record = {
    id: d[0],
    type: d[1],
    parent_id: d[2],
    order: d[3],
    authority: {
      edition_id: 'NOETH-DE-ED-0002',
      whole_path: authorityPath,
      whole_sha256: authoritySha,
      snapshot_path: 'source.tex',
      line_start: d[4],
      line_end: d[5],
      bytes: sourceBytes.length,
      sha256: sha(sourceBytes)
    },
    target: target,
    relations: d[10].map(function (r) { return {type:r[0], target_id:r[1]}; }),
    language: 'ko',
    state: {
      translation: d[9],
      review: 'unchecked',
      build: 'not_run',
      render: 'not_run',
      publication: 'not_handed_off'
    },
    continuation: {
      next_authority_line: d.length > 11 ? d[11] : 6027
    }
  };
  record.evidence_sha256 = sha(Buffer.from(JSON.stringify(record), 'utf8'));
  return record;
});

const jsonl = records.map(function (r) { return JSON.stringify(r); }).join('\n') + '\n';
fs.writeFileSync(path.join(outDir, 'structure.jsonl'), jsonl, 'utf8');

const header = ['id','type','parent_id','order','authority_lines','authority_bytes','authority_sha256','target_path','target_lines','target_bytes','target_sha256','language','translation_state','review_state','publication_state','next_authority_line','evidence_sha256'];
const rows = records.map(function (r) {
  return [
    r.id,r.type,r.parent_id,r.order,
    String(r.authority.line_start) + '-' + String(r.authority.line_end),
    r.authority.bytes,r.authority.sha256,
    r.target ? r.target.path : '',
    r.target ? String(r.target.line_start) + '-' + String(r.target.line_end) : '',
    r.target ? r.target.bytes : '',
    r.target ? r.target.sha256 : '',
    r.language,r.state.translation,r.state.review,r.state.publication,
    r.continuation.next_authority_line,r.evidence_sha256
  ].map(csvCell).join(',');
});
fs.writeFileSync(path.join(outDir, 'structure.csv'), header.map(csvCell).join(',') + '\n' + rows.join('\n') + '\n', 'utf8');

const manifest = {
  generated_by: 'evidence/build.mjs',
  scope: 'complete P08 T01-U01 through T08-U36',
  record_count: records.length,
  first_id: records[0].id,
  last_id: records.at(-1).id,
  next_authority_line: 6348,
  source: {
    path: 'source.tex',
    bytes: fs.readFileSync(sourcePath).length,
    sha256: sha(fs.readFileSync(sourcePath)),
    line_start: 5957,
    line_end: 6347
  },
  status: 'COMPLETE_UNCHECKED_TRANSLATION_PRODUCER_EVIDENCE'
};
fs.writeFileSync(path.join(outDir, 'struct_manifest.json'), JSON.stringify(manifest, null, 2) + '\n', 'utf8');

const unitRecords = records.filter(function (r) { return r.type === 'unit'; }).sort(function (a, b) { return a.target.path.localeCompare(b.target.path, 'en'); });
const targetIdentities = unitRecords.map(function (r) {
  const bytes = fs.readFileSync(path.join(root, r.target.path));
  return {path:r.target.path, bytes:bytes.length, sha256:sha(bytes)};
});
const treeStream = targetIdentities.map(function (item) {
  return item.path + '\0' + String(item.bytes) + '\0' + item.sha256 + '\n';
}).join('');
const coveredLines = new Set();
for (const r of unitRecords) for (let line = r.authority.line_start; line <= r.authority.line_end; line += 1) coveredLines.add(line);
const gapLines = [];
for (let line = 5957; line <= 6347; line += 1) {
  if (!coveredLines.has(line)) {
    if (sourceLines[line - sourceBase] !== '') throw new Error('Nonblank source line omitted from unit coverage: ' + String(line));
    gapLines.push(line);
  }
}
const targetManifest = {
  work: 'Noether P08 Korean',
  authority: {
    edition_id: 'NOETH-DE-ED-0002',
    whole_path: authorityPath,
    whole_sha256: authoritySha,
    interval_lines: [5957,6347],
    interval_bytes: fs.readFileSync(sourcePath).length,
    interval_sha256: sha(fs.readFileSync(sourcePath))
  },
  state: {
    translation: 'complete_producer_draft_text_and_tex_control_coverage',
    review: 'unchecked',
    source_check: 'not_performed',
    formula_check: 'not_performed',
    build: 'not_run',
    render: 'not_run',
    visual_qa: 'not_run',
    assembly: 'not_run',
    approval: 'not_approved'
  },
  target_count: targetIdentities.length,
  target_bytes: targetIdentities.reduce(function (sum, item) { return sum + item.bytes; }, 0),
  target_tree_stream_bytes: Buffer.byteLength(treeStream, 'utf8'),
  target_tree_sha256: sha(Buffer.from(treeStream, 'utf8')),
  targets: targetIdentities,
  source_covered_lines: coveredLines.size,
  source_gap_lines: gapLines,
  source_gap_rule: 'all excluded lines are exact blank separators inside the complete interval',
  next_authority_line: 6348
};
fs.writeFileSync(path.join(root, 'manifest.json'), JSON.stringify(targetManifest, null, 2) + '\n', 'utf8');
