import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_RETURN_LEDGER_TEMPLATE_20260703T063000Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_RETURN_LEDGER_TEMPLATE_NOTE_20260703T063100Z';
const generatedUtc = '2026-07-03T06:30:00Z';
const noteGeneratedUtc = '2026-07-03T06:31:00Z';
const packageOrder = 145;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-SELECTED-EXCERPT-ATTRIBUTION-NOTICE-TEMPLATE-REVIEW-RETURN-EVIDENCE-CRITERIA-DECISION-REVIEW-RETURN-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentReviewPacket = 'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_PACKET_20260703T061500Z';
const parentArtifacts = [
  parentReviewPacket,
  'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_20260703T060000Z',
  'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_INTAKE_LEDGER_TEMPLATE_20260703T054500Z'
];

const blankReturnFields = [
  'return_date',
  'reviewer_role',
  'return_route_or_owner_id',
  'parent_review_packet_row_match',
  'decision_row_identity_confirmation',
  'blank_review_field_preservation',
  'criteria_decision_absence_confirmation',
  'source_text_absence_confirmation',
  'downstream_gate_limit_confirmation',
  'return_note'
];

function parseJson(text) {
  return JSON.parse(text.charCodeAt(0) === 0xFEFF ? text.slice(1) : text);
}

async function readJson(stem) {
  const text = await readFile(path.join(outputs, `${stem}.json`), 'utf8');
  return { text, obj: parseJson(text) };
}

function sha256(data) {
  return crypto.createHash('sha256').update(data).digest('hex');
}

function sha256Upper(data) {
  return sha256(data).toUpperCase();
}

async function writeShaForJson(stem) {
  const filename = `${stem}.json`;
  const data = await readFile(path.join(outputs, filename));
  await writeFile(path.join(outputs, `${stem}.sha256`), `${sha256(data)}  ${filename}\n`, 'utf8');
}

async function writeJson(stem, obj) {
  await writeFile(path.join(outputs, `${stem}.json`), `${JSON.stringify(obj, null, 2)}\n`, 'utf8');
  await writeShaForJson(stem);
}

function ensureArray(obj, key) {
  if (!Array.isArray(obj[key])) obj[key] = [];
  return obj[key];
}

function addUnique(array, value) {
  if (!array.includes(value)) array.push(value);
}

function upsertById(array, keys, id, row) {
  const index = array.findIndex((candidate) => keys.some((key) => candidate?.[key] === id));
  if (index >= 0) array[index] = { ...array[index], ...row };
  else array.push(row);
}

function csvCell(value) {
  if (value === undefined || value === null) return '';
  const text = Array.isArray(value) ? value.join('; ') : typeof value === 'object' ? JSON.stringify(value) : String(value);
  return /[",\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

async function appendMdIfMissing(filename, marker, text) {
  const file = path.join(outputs, filename);
  let current = '';
  try {
    current = await readFile(file, 'utf8');
  } catch {
    current = '';
  }
  if (!current.includes(marker)) {
    const separator = current.endsWith('\n') || current.length === 0 ? '' : '\n';
    await writeFile(file, `${current}${separator}${text}\n`, 'utf8');
  }
}

async function countJsonFilesRecursive(dir) {
  let count = 0;
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) count += await countJsonFilesRecursive(full);
    else if (entry.name.endsWith('.json')) count += 1;
  }
  return count;
}

function titleClass(value) {
  return String(value).split('_').map((part) => (part ? `${part[0].toUpperCase()}${part.slice(1)}` : part)).join(' ');
}

function formatNumber(value) {
  return new Intl.NumberFormat('en-US').format(value);
}

function buildReturnRows(parent) {
  return parent.review_return_evidence_criteria_decision_review_packet_rows.map((row, index) => ({
    review_return_evidence_criteria_decision_review_return_ledger_row_id: `ODRF-SEL-EXC-ATTR-RRET-EVID-DEC-REVIEW-RETURN-${String(index + 1).padStart(3, '0')}`,
    parent_review_return_evidence_criteria_decision_review_packet_row_id: row.review_return_evidence_criteria_decision_review_packet_row_id,
    parent_review_return_evidence_criteria_decision_row_id: row.parent_review_return_evidence_criteria_decision_row_id,
    parent_review_return_evidence_intake_row_id: row.parent_review_return_evidence_intake_row_id,
    parent_review_return_evidence_criterion_row_id: row.parent_review_return_evidence_criterion_row_id,
    parent_review_return_ledger_row_id: row.parent_review_return_ledger_row_id,
    parent_review_packet_row_id: row.parent_review_packet_row_id,
    parent_notice_template_row_id: row.parent_notice_template_row_id,
    parent_source_text_capture_policy_return_row_id: row.parent_source_text_capture_policy_return_row_id,
    parent_packet_unit: row.parent_packet_unit,
    criterion_type: row.criterion_type,
    criterion_label: row.criterion_label,
    required_evidence: row.required_evidence,
    inherited_review_fields_filled: row.review_fields_filled,
    inherited_review_packet_dispatched: row.review_packet_dispatched,
    inherited_review_return_received: row.review_return_received,
    inherited_review_passed: row.review_passed,
    inherited_review_failed: row.review_failed,
    inherited_criteria_decision_approved_after_review: row.criteria_decision_approved_after_review,
    blank_return_fields: blankReturnFields,
    return_date: null,
    reviewer_role: null,
    return_route_or_owner_id: null,
    parent_review_packet_row_match: null,
    decision_row_identity_confirmation: null,
    blank_review_field_preservation: null,
    criteria_decision_absence_confirmation: null,
    source_text_absence_confirmation: null,
    downstream_gate_limit_confirmation: null,
    return_note: null,
    return_fields_filled: 0,
    review_return_received: false,
    review_return_ingested: false,
    review_passed: false,
    review_failed: false,
    criteria_decision_approved_after_return: false,
    notice_template_approval_allowed_after_return: false,
    source_text_or_excerpt_allowed_after_return: false,
    surface_gate_opened: false,
    translation_gate_opened: false,
    still_locked_reason: 'missing_review_dispatch_return_evidence_values_criteria_decisions_notice_approval_exact_span_and_source_text_permission'
  }));
}

function buildCriterionClassReturnSummaryRows(parent, returnRows) {
  return parent.criterion_class_review_return_evidence_criteria_decision_review_summary_rows.map((row, index) => {
    const linked = returnRows.filter((entry) => entry.criterion_type === row.criterion_type);
    return {
      review_return_evidence_criteria_decision_review_return_criterion_class_summary_row_id: `ODRF-SEL-EXC-ATTR-RRET-EVID-DEC-REVIEW-RETURN-CLASS-${String(index + 1).padStart(2, '0')}`,
      parent_review_return_evidence_criteria_decision_review_packet_criterion_class_summary_row_id: row.review_return_evidence_criteria_decision_review_packet_criterion_class_summary_row_id,
      criterion_type: row.criterion_type,
      criterion_label: row.criterion_label,
      linked_review_return_ledger_row_ids: linked.map((entry) => entry.review_return_evidence_criteria_decision_review_return_ledger_row_id),
      return_rows_required: linked.length,
      return_fields_filled: 0,
      review_returns_received: 0,
      review_returns_ingested: 0,
      review_rows_passed: 0,
      review_rows_failed: 0,
      return_rows_unfilled: linked.length,
      decisions_recorded: 0,
      evidence_values_reviewed: 0,
      class_ready_for_return_review: false
    };
  });
}

function buildPacketUnitReturnSummaryRows(parent, returnRows) {
  return parent.packet_unit_review_return_evidence_criteria_decision_review_summary_rows.map((row, index) => {
    const linked = returnRows.filter((entry) => entry.parent_review_return_ledger_row_id === row.parent_review_return_ledger_row_id);
    return {
      review_return_evidence_criteria_decision_review_return_packet_summary_row_id: `ODRF-SEL-EXC-ATTR-RRET-EVID-DEC-REVIEW-RETURN-PACKET-${String(index + 1).padStart(2, '0')}`,
      parent_review_return_evidence_criteria_decision_review_packet_summary_row_id: row.review_return_evidence_criteria_decision_review_packet_summary_row_id,
      parent_packet_unit: row.parent_packet_unit,
      parent_review_return_ledger_row_id: row.parent_review_return_ledger_row_id,
      linked_review_return_ledger_row_ids: linked.map((entry) => entry.review_return_evidence_criteria_decision_review_return_ledger_row_id),
      return_rows_required: linked.length,
      return_fields_filled: 0,
      review_returns_received: 0,
      review_returns_ingested: 0,
      review_rows_passed: 0,
      review_rows_failed: 0,
      return_rows_unfilled: linked.length,
      decisions_recorded: 0,
      evidence_values_reviewed: 0,
      notice_template_approved_for_fill: false,
      source_text_or_excerpt_allowed: false,
      packet_ready_for_return_review: false
    };
  });
}

function buildArtifact(parent) {
  const returnRows = buildReturnRows(parent);
  const criterionClassRows = buildCriterionClassReturnSummaryRows(parent, returnRows);
  const packetSummaryRows = buildPacketUnitReturnSummaryRows(parent, returnRows);
  const blankReturnCells = returnRows.length * blankReturnFields.length;
  const parentGate = parent.gate_state || {};
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template_blank_no_returns_no_ingestion_no_decisions_no_evidence_review_no_approvals_no_excerpts_no_source_text_no_notice_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Allocate blank review-return ledger rows for each package-144 review-packet row, without receiving or ingesting returns, recording decisions, reviewing evidence, approving notice fills, selecting excerpts, copying source text, opening surfaces, or drafting translations.',
    parent_artifacts: parentArtifacts,
    review_return_boundary: {
      ledger_template_is: 'blank review-return ledger template for future returns against P144 criteria-decision review-packet rows',
      ledger_template_is_not: [
        'review dispatch',
        'received review return',
        'ingested review return',
        'criteria decision',
        'evidence review result',
        'notice-template approval',
        'attribution notice text',
        'source-text capture permission',
        'candidate line-range selection',
        'exact line span selection',
        'source-text cache',
        'selected excerpt',
        'source-text or excerpt sidecar file',
        'local-language surface',
        'translation draft',
        'publication or pilot claim'
      ],
      downstream_gate_policy: 'return rows are allocated only; all received-return, evidence-review, source-text, excerpt, notice-fill, surface, translation, publication, and pilot gates remain closed'
    },
    blank_return_fields: blankReturnFields,
    review_return_evidence_criteria_decision_review_return_ledger_rows: returnRows,
    criterion_class_review_return_evidence_criteria_decision_review_return_summary_rows: criterionClassRows,
    packet_unit_review_return_evidence_criteria_decision_review_return_summary_rows: packetSummaryRows,
    gate_state: {
      review_return_evidence_criteria_decision_review_return_ledger_rows: returnRows.length,
      criterion_class_review_return_evidence_criteria_decision_review_return_summary_rows: criterionClassRows.length,
      packet_unit_review_return_evidence_criteria_decision_review_return_summary_rows: packetSummaryRows.length,
      blank_return_fields_per_row: blankReturnFields.length,
      blank_return_field_cells_allocated: blankReturnCells,
      inherited_review_packet_rows: parentGate.review_return_evidence_criteria_decision_review_packet_rows || 0,
      inherited_review_fields_filled: parentGate.review_fields_filled || 0,
      inherited_review_packets_dispatched: parentGate.review_packets_dispatched || 0,
      inherited_review_returns_received: parentGate.review_returns_received || 0,
      inherited_criteria_decisions_recorded: parentGate.criteria_decisions_recorded || 0,
      return_fields_filled: 0,
      review_return_rows_filled: 0,
      review_returns_received: 0,
      review_returns_ingested: 0,
      review_rows_passed: 0,
      review_rows_failed: 0,
      review_return_rows_unfilled: returnRows.length,
      criteria_decisions_recorded: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      criteria_unfilled: returnRows.length,
      evidence_values_reviewed: 0,
      evidence_source_pointers_reviewed: 0,
      notice_template_rows_approved_for_fill: 0,
      selected_excerpt_attribution_notices_filled: 0,
      attribution_notice_files_created: 0,
      source_text_or_excerpt_files_created: 0,
      source_locators_selected: 0,
      candidate_line_ranges_selected: 0,
      exact_line_spans_selected: 0,
      source_passages_selected: 0,
      source_text_copied: 0,
      source_prose_copied: 0,
      source_examples_copied: 0,
      excerpts_selected: 0,
      local_language_surfaces_filled: 0,
      translated_passages: 0,
      translation_ready: false,
      publication_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      expected_return_rows: 50,
      expected_criterion_class_summary_rows: 5,
      expected_packet_unit_summary_rows: 10,
      expected_blank_return_fields_per_row: blankReturnFields.length,
      expected_blank_return_field_cells_allocated: blankReturnCells,
      zero_gate_assertions: [
        'inherited_review_fields_filled',
        'inherited_review_packets_dispatched',
        'inherited_review_returns_received',
        'inherited_criteria_decisions_recorded',
        'return_fields_filled',
        'review_return_rows_filled',
        'review_returns_received',
        'review_returns_ingested',
        'review_rows_passed',
        'review_rows_failed',
        'criteria_decisions_recorded',
        'criteria_passed',
        'criteria_failed',
        'evidence_values_reviewed',
        'evidence_source_pointers_reviewed',
        'notice_template_rows_approved_for_fill',
        'selected_excerpt_attribution_notices_filled',
        'attribution_notice_files_created',
        'source_text_or_excerpt_files_created',
        'source_locators_selected',
        'candidate_line_ranges_selected',
        'exact_line_spans_selected',
        'source_passages_selected',
        'source_text_copied',
        'source_prose_copied',
        'source_examples_copied',
        'excerpts_selected',
        'local_language_surfaces_filled',
        'translated_passages'
      ],
      source_text_or_excerpt_files_created: 0,
      copied_source_text_or_excerpts: false,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_RETURN_EVIDENCE_CRITERIA_RUBRIC_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_REVIEW_RETURN_LEDGER_WITH_RETURNS_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_REVIEW_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_WITH_DECISIONS_<timestamp>'
    ],
    decision: {
      review_returns_received: false,
      review_returns_ingested: false,
      criteria_decisions_recorded: false,
      notice_template_rows_approved_for_fill: false,
      source_text_or_excerpt_allowed: false,
      surface_or_translation_allowed: false,
      publication_or_pilot_allowed: false
    }
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const classRows = artifact.criterion_class_review_return_evidence_criteria_decision_review_return_summary_rows.map((row) => `| ${row.review_return_evidence_criteria_decision_review_return_criterion_class_summary_row_id} | ${row.criterion_type} | ${row.return_rows_required} | ${row.review_returns_received} | ${row.return_rows_unfilled} |`).join('\n');
  const packetRows = artifact.packet_unit_review_return_evidence_criteria_decision_review_return_summary_rows.map((row) => `| ${row.review_return_evidence_criteria_decision_review_return_packet_summary_row_id} | ${row.parent_packet_unit} | ${row.parent_review_return_ledger_row_id} | ${row.return_rows_required} | ${row.review_returns_received} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

Purpose: ${artifact.purpose}

## Counts

- Review-return ledger rows: \`${g.review_return_evidence_criteria_decision_review_return_ledger_rows}\`
- Criterion-class return summary rows: \`${g.criterion_class_review_return_evidence_criteria_decision_review_return_summary_rows}\`
- Packet-unit return summary rows: \`${g.packet_unit_review_return_evidence_criteria_decision_review_return_summary_rows}\`
- Blank return fields per row: \`${g.blank_return_fields_per_row}\`
- Blank return-field cells: \`${g.blank_return_field_cells_allocated}\`

## Zero Gates

- Return fields filled: \`0\`
- Review returns received/ingested: \`0 / 0\`
- Review rows passed/failed: \`0 / 0\`
- Criteria decisions recorded: \`0\`
- Evidence values/source pointers reviewed: \`0 / 0\`
- Notice-template approvals: \`0\`
- Attribution notices/files: \`0 / 0\`
- Source-text/excerpt files: \`0\`
- Source locators/candidate line ranges/exact spans: \`0 / 0 / 0\`
- Source text/prose/examples copied: \`0 / 0 / 0\`
- Excerpts selected: \`0\`
- Surfaces/translations/readiness: \`0 / 0 / false\`

## Criterion-Class Summary

| Row | Criterion type | Return rows required | Returns received | Return rows unfilled |
| --- | --- | ---: | ---: | ---: |
${classRows}

## Packet Summary

| Row | Packet unit | Parent review-return row | Return rows required | Returns received |
| --- | --- | --- | ---: | ---: |
${packetRows}

Boundary: this is a blank review-return ledger template only. It is not a received return, ingested return, criteria decision, evidence review, notice approval, source-text capture, excerpt selection, attribution notice text, a source-text/excerpt sidecar, a surface, a translation, or a readiness claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'packet_or_criterion', 'parent_id', 'required_or_blank_count', 'filled_or_received_count', 'gate_open'].map(csvCell).join(','));
  for (const row of artifact.review_return_evidence_criteria_decision_review_return_ledger_rows) {
    rows.push([
      'review_return_ledger_row',
      row.review_return_evidence_criteria_decision_review_return_ledger_row_id,
      row.criterion_type,
      row.parent_review_return_evidence_criteria_decision_review_packet_row_id,
      row.blank_return_fields.length,
      row.return_fields_filled,
      row.source_text_or_excerpt_allowed_after_return || row.surface_gate_opened || row.translation_gate_opened
    ].map(csvCell).join(','));
  }
  for (const row of artifact.criterion_class_review_return_evidence_criteria_decision_review_return_summary_rows) {
    rows.push([
      'criterion_class_return_summary',
      row.review_return_evidence_criteria_decision_review_return_criterion_class_summary_row_id,
      row.criterion_type,
      row.parent_review_return_evidence_criteria_decision_review_packet_criterion_class_summary_row_id,
      row.return_rows_required,
      row.review_returns_received,
      row.class_ready_for_return_review
    ].map(csvCell).join(','));
  }
  for (const row of artifact.packet_unit_review_return_evidence_criteria_decision_review_return_summary_rows) {
    rows.push([
      'packet_unit_return_summary',
      row.review_return_evidence_criteria_decision_review_return_packet_summary_row_id,
      row.parent_packet_unit,
      row.parent_review_return_ledger_row_id,
      row.return_rows_required,
      row.review_returns_received,
      row.source_text_or_excerpt_allowed
    ].map(csvCell).join(','));
  }
  return `${rows.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    source_artifact_id: artifact.artifact_id,
    status: 'pointer_only_package145_coordination_note_no_remote_action_no_source_text_no_excerpt_no_translation_no_readiness',
    summary: 'Package 145 queues a blank selected-excerpt attribution notice template review-return evidence criteria-decision review-return ledger template derived from package 144 review-packet rows.',
    counts: {
      review_return_evidence_criteria_decision_review_return_ledger_rows: g.review_return_evidence_criteria_decision_review_return_ledger_rows,
      criterion_class_review_return_evidence_criteria_decision_review_return_summary_rows: g.criterion_class_review_return_evidence_criteria_decision_review_return_summary_rows,
      packet_unit_review_return_evidence_criteria_decision_review_return_summary_rows: g.packet_unit_review_return_evidence_criteria_decision_review_return_summary_rows,
      blank_return_fields_per_row: g.blank_return_fields_per_row,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated,
      inherited_review_packet_rows: g.inherited_review_packet_rows
    },
    zero_gates: {
      return_fields_filled: 0,
      review_returns_received: 0,
      review_returns_ingested: 0,
      review_rows_passed: 0,
      review_rows_failed: 0,
      criteria_decisions_recorded: 0,
      evidence_values_reviewed: 0,
      evidence_source_pointers_reviewed: 0,
      notice_template_rows_approved_for_fill: 0,
      source_text_or_excerpt_files_created: 0,
      exact_line_spans_selected: 0,
      source_text_copied: 0,
      excerpts_selected: 0,
      surfaces_filled: 0,
      translated_passages: 0,
      readiness_claims: 0
    },
    no_remote_action_by_this_note: true
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 145 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 145 creates an OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return ledger template with \`${g.review_return_evidence_criteria_decision_review_return_ledger_rows}\` blank return rows, \`${g.blank_return_fields_per_row}\` blank return fields per row, and \`${g.blank_return_field_cells_allocated}\` blank return-field cells.

Zero gates: \`0\` filled return fields, \`0\` review returns received/ingested, \`0\` review rows passed/failed, \`0\` criteria decisions, \`0\` evidence values or source pointers reviewed, \`0\` notice approvals, \`0\` exact line spans, \`0\` source text/prose/examples copied, \`0\` excerpts, \`0\` attribution notices or files, \`0\` source-text/excerpt files, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Boundary: review-return ledger template only. This note makes no commit, push, PR, Zenodo, dispatch, return receipt, return ingestion, evidence review, source-text, excerpt, attribution notice fill, translation, publication, pilot, legal-advice, or remote-state claim.
`;
}

async function writeArtifactAndNote(artifact, note) {
  await writeFile(path.join(outputs, `${artifactId}.json`), `${JSON.stringify(artifact, null, 2)}\n`, 'utf8');
  await writeFile(path.join(outputs, `${artifactId}.md`), buildArtifactMd(artifact), 'utf8');
  await writeFile(path.join(outputs, `${artifactId}.csv`), buildArtifactCsv(artifact), 'utf8');
  await writeShaForJson(artifactId);

  await writeFile(path.join(outputs, `${noteId}.json`), `${JSON.stringify(note, null, 2)}\n`, 'utf8');
  await writeFile(path.join(outputs, `${noteId}.md`), buildNoteMd(note, artifact), 'utf8');
  await writeShaForJson(noteId);
}

async function updateRegistrations(artifact) {
  const g = artifact.gate_state;
  const packageIndex = await readJson(packageIndexFile);
  const order = ensureArray(packageIndex.obj, 'current_package_order');
  if (!order.some((row) => row?.artifact === artifactId)) {
    order.push({
      order: packageOrder,
      role: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template_support',
      artifact: artifactId,
      current_use: '50 blank selected-excerpt attribution notice template review-return evidence criteria-decision review-return ledger rows; 10 return fields per row; 500 blank return-field cells; 5 criterion-class summaries; 10 packet-unit summaries; 0 returns, 0 ingestion, 0 decisions, 0 evidence review, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_rows: g.review_return_evidence_criteria_decision_review_return_ledger_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_blank_cells: g.blank_return_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_returns_received: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_returns_ingested: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_source_text_or_excerpt_files: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_return_evidence_criteria_rubric_or_returns_only_after_external_return_no_source_text_no_excerpt_no_surfaces_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return ledger template',
    route: artifactId,
    license_status_to_recheck: 'blank_review_return_ledger_only_no_returns_no_ingestion_no_decisions_no_evidence_review_no_approvals_no_exact_spans_no_source_text_no_excerpts_no_notices_no_translation',
    best_translation_use: 'future return ledger for selected-excerpt attribution notice template review-return evidence criteria-decision review before evidence criteria, approval, notice fill, source-text/excerpt sidecar, surface, or translation',
    candidate_lanes: [
      'olp_dmoi_relation_function_attribution_notice_lane',
      'blank_review_return_evidence_criteria_decision_review_return_ledger',
      'review_only_construction_scaffold',
      'source_aware_excerpt_governance'
    ],
    priority: 1,
    status: 'blank_review_return_evidence_criteria_decision_review_return_ledger_no_returns_no_ingestion_no_decisions_no_evidence_review_no_source_text_no_excerpts_no_translation',
    gate_state: {
      review_return_evidence_criteria_decision_review_return_ledger_rows: g.review_return_evidence_criteria_decision_review_return_ledger_rows,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated,
      review_returns_received: 0,
      review_returns_ingested: 0,
      criteria_decisions_recorded: 0,
      evidence_values_reviewed: 0,
      notice_template_rows_approved_for_fill: 0,
      source_text_or_excerpt_files_created: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template: ${artifactId}_50_blank_return_rows_500_blank_cells_0_returns_0_ingestion_0_decisions_0_evidence_review_0_approvals_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_rows: g.review_return_evidence_criteria_decision_review_return_ledger_rows,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_blank_cells: g.blank_return_field_cells_allocated,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_returns_received: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_returns_ingested: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_source_text_or_excerpt_files: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_surfaces: 0,
    current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_translations: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template: ${artifactId}_blank_return_ledger_only_no_returns_no_ingestion_no_decisions_no_evidence_review_no_approvals_no_source_text_no_excerpts_no_notices_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 50 blank selected-excerpt attribution notice template review-return evidence criteria-decision review-return ledger rows and 500 blank return-field cells after package 144; 0 returns, 0 ingestion, 0 decisions, 0 evidence review, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be uploaded when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return ledger template; 50 blank return rows, 500 blank cells, 0 returns, 0 ingestion, 0 decisions, 0 evidence review, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 145: OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return ledger template after package 144. It records 50 blank return rows, 5 criterion-class summaries, 10 packet-unit summaries, and 500 blank return-field cells while keeping 0 returns, 0 ingestion, 0 decisions, 0 evidence review, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, 0 source-text/excerpt files, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return ledger template | ${artifactId} | Review-return ledger scaffold; 50 blank return rows, 500 blank cells, 0 returns, 0 ingestion, 0 decisions, 0 evidence review, 0 approvals, 0 exact spans, 0 source text, 0 excerpts, 0 notices, no source-text/excerpt files, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template_artifact: \`${artifactId}\` (50 blank return rows; 500 blank return cells; 0 returns; 0 ingestion; 0 decisions; 0 evidence review; 0 approvals; 0 exact spans; 0 source text; 0 excerpts; no notices, surfaces, or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template: \`${artifactId}\`; blank return ledger only, no returns, ingestion, decisions, evidence review, approvals, exact spans, source text, excerpts, notices, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return ledger template; blank return rows are not received returns, ingested returns, criteria decisions, evidence review, approvals, exact spans, copied source text, selected excerpts, attribution notices, source-text/excerpt sidecars, surfaces, translations, or readiness.`);
}

async function rebuildUploadQueueMd(queue) {
  const rows = queue.queued_items.map((item) => `| \`${item.filename}\` | ${titleClass(item.class)} | ${formatNumber(item.bytes)} | \`${item.sha256}\` |`).join('\n');
  const sourcePdfFiles = (queue.summary.source_pdf_files || 0) + (queue.summary.source_image_files || 0);
  const md = `# NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702

Status: local post-manifest upload queue, not a remote sync, commit, push, PR update, Zenodo action, or completion claim.

## Purpose

This queue preserves new coordination and translation-access artifacts created after the current indexed payload manifest. The indexed payload still lives at:

\`${queue.relationship_to_indexed_payload.indexed_payload_manifest}\`

Substantive artifacts are queued for upload when a valid checkout/staging path exists; mobile-plan or bandwidth wording should not suppress them.

## Queue Summary

- Queued files: \`${queue.summary.queued_files}\`
- Queued bytes: \`${formatNumber(queue.summary.queued_bytes)}\`
- Raw token files: \`${queue.summary.raw_token_files || 0}\`
- Source PDF/image files: \`${sourcePdfFiles}\`
- Source excerpt/source-text files: \`${queue.summary.source_text_or_excerpt_files || 0}\`
- Network actions performed now: \`0\`
- Git commits/pushes/PR updates performed now: \`0\`
- Recommended future checkout destination: \`${queue.recommended_destination_in_checkout}\`

## Queued Files

| File | Class | Bytes | SHA-256 |
| --- | --- | ---: | --- |
${rows}

## Future Staging Order

${queue.staging_order.map((step, index) => `${index + 1}. ${step}`).join('\n')}

## Boundary

This is not a manifest update, payload validator update, Git commit claim, remote branch claim, PR update, Zenodo publication, canonical-readiness claim, translation-readiness claim, or secret-storage artifact.
`;
  await writeFile(path.join(outputs, `${uploadQueueFile}.md`), md, 'utf8');
}

async function updateUploadQueue() {
  const upload = await readJson(uploadQueueFile);
  const files = [
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_selected_excerpt_attribution_notice_template_review_return_evidence_criteria_decision_review_return_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package145_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package145_coordination_note' },
    { filename: `${noteId}.sha256`, class: 'checksum_sidecar' }
  ];
  const destination = upload.obj.recommended_destination_in_checkout || 'noether-slavic-handoff/20260629/cross-session-coordination/20260702';
  const byFilename = new Map((upload.obj.queued_items || []).map((item) => [item.filename, item]));
  for (const file of files) {
    byFilename.set(file.filename, {
      filename: file.filename,
      class: file.class,
      bytes: 0,
      sha256: '',
      future_destination: `${destination}/${file.filename}`
    });
  }
  const refreshed = [];
  for (const item of byFilename.values()) {
    const data = await readFile(path.join(outputs, item.filename));
    refreshed.push({
      ...item,
      bytes: data.length,
      sha256: sha256Upper(data),
      future_destination: item.future_destination || `${destination}/${item.filename}`
    });
  }
  upload.obj.queued_items = refreshed;
  upload.obj.bandwidth_mode = 'upload_substantive_artifacts_when_checkout_available_no_mobile_plan_deferral';
  upload.obj.user_upload_clarification = '2026-07-03: user clarified that substantive artifacts should always be queued/uploaded when a staging path exists; do not suppress them because of mobile-plan or bandwidth wording.';
  upload.obj.package145_upload_queue_update = {
    captured_utc: '2026-07-03T06:32:00Z',
    substantive_artifacts_added_or_refreshed: files.length,
    artifact: artifactId,
    coordination_note: noteId,
    network_actions_performed_by_this_update: 0,
    commit_created: false,
    push_performed: false,
    pr_updated: false
  };
  upload.obj.summary.queued_files = upload.obj.queued_items.length;
  upload.obj.summary.queued_bytes = upload.obj.queued_items.reduce((sum, item) => sum + item.bytes, 0);
  upload.obj.summary.source_text_or_excerpt_files = 0;
  upload.obj.summary.network_actions_required_to_stage = 0;
  upload.obj.summary.network_actions_required_to_push = 1;
  upload.obj.staging_order = Array.isArray(upload.obj.staging_order) ? upload.obj.staging_order : [];
  const step = 'Stage package 145 OLP/DMOI relation-function selected-excerpt attribution notice template review-return evidence criteria-decision review-return ledger artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.review_return_evidence_criteria_decision_review_return_ledger_rows.length !== 50) failures.push(`return_rows_not_50_${artifact.review_return_evidence_criteria_decision_review_return_ledger_rows.length}`);
  if (artifact.criterion_class_review_return_evidence_criteria_decision_review_return_summary_rows.length !== 5) failures.push(`criterion_class_rows_not_5_${artifact.criterion_class_review_return_evidence_criteria_decision_review_return_summary_rows.length}`);
  if (artifact.packet_unit_review_return_evidence_criteria_decision_review_return_summary_rows.length !== 10) failures.push(`packet_summary_rows_not_10_${artifact.packet_unit_review_return_evidence_criteria_decision_review_return_summary_rows.length}`);
  if (g.blank_return_fields_per_row !== blankReturnFields.length) failures.push(`blank_return_fields_per_row_not_${blankReturnFields.length}_${g.blank_return_fields_per_row}`);
  if (g.blank_return_field_cells_allocated !== 50 * blankReturnFields.length) failures.push(`blank_return_cells_mismatch_${g.blank_return_field_cells_allocated}`);
  if (g.review_return_rows_unfilled !== 50) failures.push(`return_rows_unfilled_not_50_${g.review_return_rows_unfilled}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.review_return_evidence_criteria_decision_review_return_ledger_rows) {
    const filled = blankReturnFields.some((field) => row[field] !== null);
    if (filled || row.return_fields_filled !== 0 || row.review_return_received || row.review_return_ingested || row.review_passed || row.review_failed || row.criteria_decision_approved_after_return || row.notice_template_approval_allowed_after_return || row.source_text_or_excerpt_allowed_after_return || row.surface_gate_opened || row.translation_gate_opened) {
      failures.push(`nonblank_return_ledger_row_${row.review_return_evidence_criteria_decision_review_return_ledger_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentReviewPacket)).obj;
const artifact = buildArtifact(parent);
const failures = validateGenerated(artifact);
if (failures.length) {
  console.error(JSON.stringify({ ok: false, failures }, null, 2));
  process.exit(1);
}

const note = buildNote(artifact);
await writeArtifactAndNote(artifact, note);
await updateRegistrations(artifact);
await updateUploadQueue();

const rootJsonFiles = (await readdir(outputs)).filter((name) => name.endsWith('.json')).length;
const recursiveJsonFiles = await countJsonFilesRecursive(outputs);
const packageIndex = (await readJson(packageIndexFile)).obj;
const queue = (await readJson(queueFile)).obj;
const upload = (await readJson(uploadQueueFile)).obj;

console.log(JSON.stringify({
  ok: true,
  artifact_id: artifactId,
  note_id: noteId,
  package_order_length: packageIndex.current_package_order?.length,
  queue_candidate_sources: queue.candidate_sources?.length,
  upload_queue_files: upload.summary?.queued_files,
  upload_queue_bytes: upload.summary?.queued_bytes,
  source_text_or_excerpt_files: upload.summary?.source_text_or_excerpt_files,
  review_return_evidence_criteria_decision_review_return_ledger_rows: artifact.gate_state.review_return_evidence_criteria_decision_review_return_ledger_rows,
  criterion_class_review_return_evidence_criteria_decision_review_return_summary_rows: artifact.gate_state.criterion_class_review_return_evidence_criteria_decision_review_return_summary_rows,
  packet_unit_review_return_evidence_criteria_decision_review_return_summary_rows: artifact.gate_state.packet_unit_review_return_evidence_criteria_decision_review_return_summary_rows,
  blank_return_fields_per_row: artifact.gate_state.blank_return_fields_per_row,
  blank_return_field_cells_allocated: artifact.gate_state.blank_return_field_cells_allocated,
  return_fields_filled: artifact.gate_state.return_fields_filled,
  review_returns_received: artifact.gate_state.review_returns_received,
  review_returns_ingested: artifact.gate_state.review_returns_ingested,
  review_rows_passed: artifact.gate_state.review_rows_passed,
  review_rows_failed: artifact.gate_state.review_rows_failed,
  criteria_decisions_recorded: artifact.gate_state.criteria_decisions_recorded,
  evidence_values_reviewed: artifact.gate_state.evidence_values_reviewed,
  notice_template_rows_approved_for_fill: artifact.gate_state.notice_template_rows_approved_for_fill,
  selected_excerpt_attribution_notices_filled: artifact.gate_state.selected_excerpt_attribution_notices_filled,
  source_text_or_excerpt_files_created: artifact.gate_state.source_text_or_excerpt_files_created,
  exact_line_spans_selected: artifact.gate_state.exact_line_spans_selected,
  source_text_copied: artifact.gate_state.source_text_copied,
  excerpts_selected: artifact.gate_state.excerpts_selected,
  local_language_surfaces_filled: artifact.gate_state.local_language_surfaces_filled,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
