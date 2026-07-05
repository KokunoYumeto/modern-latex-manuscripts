import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_INTAKE_LEDGER_TEMPLATE_20260703T021500Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_INTAKE_LEDGER_TEMPLATE_NOTE_20260703T021600Z';
const generatedUtc = '2026-07-03T02:15:00Z';
const noteGeneratedUtc = '2026-07-03T02:16:00Z';
const packageOrder = 128;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-REVIEWER-SCOPE-LINE-SPAN-PERMISSION-EVIDENCE-INTAKE-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentPermissionReturnTemplate = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_RETURN_TEMPLATE_20260703T020000Z';
const parentArtifacts = [
  parentPermissionReturnTemplate,
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_LINE_SPAN_CANDIDATE_REGISTER_BLANK_20260703T014500Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_20260703T013000Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_INTAKE_LEDGER_TEMPLATE_20260703T011500Z'
];

const blankEvidenceFields = [
  'evidence_value',
  'evidence_source_pointer',
  'evidence_date',
  'non_personal_return_route_label',
  'reviewer_role_or_authority_class',
  'permission_evidence_review_note',
  'permission_decision',
  'downstream_gate_note'
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

function linkedRows(rowByReturnId, returnIds) {
  return (returnIds || []).map((id) => rowByReturnId.get(id)).filter(Boolean);
}

function buildEvidenceRows(parent) {
  return parent.line_span_permission_return_rows.map((row, index) => ({
    permission_evidence_intake_row_id: `ODRF-RSCOPE-LSPAN-PEVID-${String(index + 1).padStart(5, '0')}`,
    parent_line_span_permission_return_row_id: row.line_span_permission_return_row_id,
    parent_line_span_candidate_row_id: row.parent_line_span_candidate_row_id,
    parent_criteria_decision_row_id: row.parent_criteria_decision_row_id,
    parent_resolution_return_evidence_intake_row_id: row.parent_resolution_return_evidence_intake_row_id,
    parent_criterion_row_id: row.parent_criterion_row_id,
    parent_decision_precondition_blocker_resolution_return_evidence_criteria_row_id: row.parent_decision_precondition_blocker_resolution_return_evidence_criteria_row_id,
    parent_decision_precondition_blocker_resolution_return_row_id: row.parent_decision_precondition_blocker_resolution_return_row_id,
    parent_decision_precondition_blocker_resolution_request_row_id: row.parent_decision_precondition_blocker_resolution_request_row_id,
    parent_decision_precondition_blocker_row_id: row.parent_decision_precondition_blocker_row_id,
    parent_decision_precondition_checklist_row_id: row.parent_decision_precondition_checklist_row_id,
    parent_reviewer_scope_criteria_decision_row_id: row.parent_reviewer_scope_criteria_decision_row_id,
    parent_reviewer_scope_evidence_intake_row_id: row.parent_reviewer_scope_evidence_intake_row_id,
    parent_ledger_row_id: row.parent_ledger_row_id,
    parent_reviewer_scope_row_id: row.parent_reviewer_scope_row_id,
    parent_gap_check_row_id: row.parent_gap_check_row_id,
    parent_pointer_row_id: row.parent_pointer_row_id,
    packet_unit: row.packet_unit,
    reviewer_role: row.reviewer_role,
    source_systems_implicated: row.source_systems_implicated,
    parent_criterion_type: row.parent_criterion_type,
    precondition_name: row.precondition_name,
    criterion_type: row.criterion_type,
    criterion_requirement: row.criterion_requirement,
    required_future_evidence_class: row.required_future_evidence_class,
    parent_permission_return_received: row.permission_return_received,
    parent_line_span_candidate_permission_recorded: row.line_span_candidate_permission_recorded,
    parent_source_text_capture_permission_recorded: row.source_text_capture_permission_recorded,
    parent_exact_line_span_selected_after_return: row.exact_line_span_selected_after_return,
    blank_evidence_fields: blankEvidenceFields,
    evidence_value: null,
    evidence_source_pointer: null,
    evidence_date: null,
    non_personal_return_route_label: null,
    reviewer_role_or_authority_class: null,
    permission_evidence_review_note: null,
    permission_decision: null,
    downstream_gate_note: null,
    evidence_fields_filled: 0,
    evidence_value_filled: false,
    evidence_source_pointer_filled: false,
    evidence_row_filled: false,
    evidence_reviewed: false,
    permission_return_received_after_evidence: false,
    line_span_candidate_permission_recorded_after_evidence: false,
    source_text_capture_permission_recorded_after_evidence: false,
    exact_line_span_selected_after_evidence: false,
    source_passage_selected_after_evidence: false,
    source_text_copied_after_evidence: false,
    excerpt_selected_after_evidence: false,
    selected_excerpt_attribution_notice_allowed_after_evidence: false,
    local_language_surface_allowed_after_evidence: false,
    surface_gate_opened: false,
    translation_gate_opened: false,
    permission_evidence_intake_status: 'blank_permission_evidence_intake_row_only'
  }));
}

function summarizeLinkedEvidence(linked, base) {
  return {
    ...base,
    evidence_intake_rows_required: linked.length,
    evidence_intake_rows_filled: 0,
    blank_evidence_field_cells_allocated: linked.length * blankEvidenceFields.length,
    evidence_fields_filled: 0,
    evidence_values_filled: 0,
    evidence_source_pointers_filled: 0,
    evidence_values_reviewed: 0,
    permission_returns_received: 0,
    returns_received: 0,
    line_span_candidate_permissions_recorded: 0,
    source_text_capture_permissions_recorded: 0,
    exact_line_spans_selected: 0,
    source_passages_selected: 0,
    excerpts_selected: 0,
    selected_excerpt_attribution_notices_filled: 0,
    source_prose_copied: 0,
    source_examples_copied: 0,
    local_language_surfaces_filled: 0,
    translated_passages: 0
  };
}

function buildPreconditionNameSummaries(parent, evidenceRows) {
  const rowByReturnId = new Map(evidenceRows.map((row) => [row.parent_line_span_permission_return_row_id, row]));
  return parent.precondition_name_permission_return_summary_rows.map((row, index) => {
    const linked = linkedRows(rowByReturnId, row.linked_permission_return_row_ids);
    return summarizeLinkedEvidence(linked, {
      permission_evidence_precondition_name_summary_row_id: `ODRF-RSCOPE-LSPAN-PEVID-PRECOND-${String(index + 1).padStart(2, '0')}`,
      parent_permission_return_precondition_name_summary_row_id: row.permission_return_precondition_name_summary_row_id,
      precondition_name: row.precondition_name,
      linked_permission_return_row_ids: row.linked_permission_return_row_ids,
      linked_permission_evidence_intake_row_ids: linked.map((linkedRow) => linkedRow.permission_evidence_intake_row_id)
    });
  });
}

function buildReturnCriterionTypeSummaries(parent, evidenceRows) {
  const rowByReturnId = new Map(evidenceRows.map((row) => [row.parent_line_span_permission_return_row_id, row]));
  return parent.return_criterion_type_permission_return_summary_rows.map((row, index) => {
    const linked = linkedRows(rowByReturnId, row.linked_permission_return_row_ids);
    return summarizeLinkedEvidence(linked, {
      permission_evidence_criterion_type_summary_row_id: `ODRF-RSCOPE-LSPAN-PEVID-CTYPE-${String(index + 1).padStart(2, '0')}`,
      parent_permission_return_criterion_type_summary_row_id: row.permission_return_criterion_type_summary_row_id,
      criterion_type: row.criterion_type,
      required_future_evidence_class: row.required_future_evidence_class,
      linked_permission_return_row_ids: row.linked_permission_return_row_ids,
      linked_permission_evidence_intake_row_ids: linked.map((linkedRow) => linkedRow.permission_evidence_intake_row_id)
    });
  });
}

function buildParentCriterionTypeSummaries(parent, evidenceRows) {
  const rowByReturnId = new Map(evidenceRows.map((row) => [row.parent_line_span_permission_return_row_id, row]));
  return parent.parent_criterion_type_permission_return_summary_rows.map((row, index) => {
    const linked = linkedRows(rowByReturnId, row.linked_permission_return_row_ids);
    return summarizeLinkedEvidence(linked, {
      permission_evidence_parent_criterion_type_summary_row_id: `ODRF-RSCOPE-LSPAN-PEVID-PTYPE-${String(index + 1).padStart(2, '0')}`,
      parent_permission_return_parent_criterion_type_summary_row_id: row.permission_return_parent_criterion_type_summary_row_id,
      parent_criterion_type: row.parent_criterion_type,
      linked_permission_return_row_ids: row.linked_permission_return_row_ids,
      linked_permission_evidence_intake_row_ids: linked.map((linkedRow) => linkedRow.permission_evidence_intake_row_id)
    });
  });
}

function buildPacketUnitSummaries(parent, evidenceRows) {
  const rowByReturnId = new Map(evidenceRows.map((row) => [row.parent_line_span_permission_return_row_id, row]));
  return parent.packet_unit_permission_return_summary_rows.map((row, index) => {
    const linked = linkedRows(rowByReturnId, row.linked_permission_return_row_ids);
    return summarizeLinkedEvidence(linked, {
      permission_evidence_packet_unit_summary_row_id: `ODRF-RSCOPE-LSPAN-PEVID-UNIT-${String(index + 1).padStart(2, '0')}`,
      parent_permission_return_packet_unit_summary_row_id: row.permission_return_packet_unit_summary_row_id,
      packet_unit: row.packet_unit,
      parent_ledger_row_id: row.parent_ledger_row_id,
      parent_pointer_row_id: row.parent_pointer_row_id,
      linked_permission_return_row_ids: row.linked_permission_return_row_ids,
      linked_permission_evidence_intake_row_ids: linked.map((linkedRow) => linkedRow.permission_evidence_intake_row_id)
    });
  });
}

function buildArtifact(parent) {
  const evidenceRows = buildEvidenceRows(parent);
  const preconditionNameSummaries = buildPreconditionNameSummaries(parent, evidenceRows);
  const returnCriterionTypeSummaries = buildReturnCriterionTypeSummaries(parent, evidenceRows);
  const parentCriterionTypeSummaries = buildParentCriterionTypeSummaries(parent, evidenceRows);
  const packetUnitSummaries = buildPacketUnitSummaries(parent, evidenceRows);
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template_blank_no_evidence_no_returns_no_permissions_no_source_text_no_excerpts_no_surfaces_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Create blank evidence-intake rows for future non-personal line-span permission return evidence without filling evidence, receiving returns, recording permission, selecting spans, copying source text, creating excerpts, accepting surfaces, translating, publishing, or claiming pilot readiness.',
    parent_artifacts: parentArtifacts,
    evidence_intake_boundary: {
      ledger_is: 'blank evidence-intake ledger linked to package-127 permission-return rows',
      ledger_is_not: [
        'received evidence',
        'permission return',
        'permission grant',
        'source locator ledger',
        'line-span selection',
        'source text capture permission',
        'source prose cache',
        'selected excerpt',
        'attribution notice',
        'surface proposal',
        'translation draft',
        'publication or pilot claim'
      ],
      allowed_now: [
        'allocate blank evidence-intake rows',
        'link blank rows to package-127 permission-return rows',
        'summarize missing evidence by precondition, criterion type, and packet unit',
        'queue substantive small-text artifacts for upload when a staging path exists'
      ],
      blocked_now: [
        'filling evidence values or source pointers',
        'marking evidence reviewed',
        'marking permission returns received',
        'recording line-span or source-text permissions',
        'selecting exact line spans',
        'copying source prose, examples, passages, or excerpts',
        'opening surface, translation, publication, or readiness gates'
      ]
    },
    blank_evidence_fields: blankEvidenceFields,
    permission_evidence_intake_rows: evidenceRows,
    precondition_name_permission_evidence_intake_summary_rows: preconditionNameSummaries,
    return_criterion_type_permission_evidence_intake_summary_rows: returnCriterionTypeSummaries,
    parent_criterion_type_permission_evidence_intake_summary_rows: parentCriterionTypeSummaries,
    packet_unit_permission_evidence_intake_summary_rows: packetUnitSummaries,
    gate_state: {
      permission_evidence_intake_rows: evidenceRows.length,
      precondition_name_permission_evidence_intake_summary_rows: preconditionNameSummaries.length,
      return_criterion_type_permission_evidence_intake_summary_rows: returnCriterionTypeSummaries.length,
      parent_criterion_type_permission_evidence_intake_summary_rows: parentCriterionTypeSummaries.length,
      packet_unit_permission_evidence_intake_summary_rows: packetUnitSummaries.length,
      blank_evidence_fields_per_row: blankEvidenceFields.length,
      blank_evidence_field_cells_allocated: evidenceRows.length * blankEvidenceFields.length,
      inherited_line_span_permission_return_rows: parent.gate_state.line_span_permission_return_rows,
      inherited_permission_returns_received: parent.gate_state.permission_returns_received,
      evidence_fields_filled: 0,
      evidence_values_filled: 0,
      evidence_source_pointers_filled: 0,
      evidence_values_reviewed: 0,
      evidence_source_pointers_reviewed: 0,
      evidence_rows_filled: 0,
      evidence_intake_rows_filled: 0,
      permission_returns_received: 0,
      permission_return_fields_filled: 0,
      return_fields_filled: 0,
      returns_received: 0,
      returns_ingested: 0,
      line_span_candidate_permissions_recorded: 0,
      source_text_capture_permissions_recorded: 0,
      source_locator_permissions_granted: 0,
      line_span_selection_permissions_granted: 0,
      source_text_capture_permissions_granted: 0,
      excerpt_permissions_granted: 0,
      exact_line_spans_selected: 0,
      source_passages_selected: 0,
      excerpts_selected: 0,
      selected_excerpt_attribution_notices_filled: 0,
      source_prose_copied: 0,
      source_examples_copied: 0,
      translated_passages: 0,
      local_language_surfaces_filled: 0,
      bridge_surfaces_accepted: 0,
      semi_constructed_surfaces_accepted: 0,
      line_span_candidate_fields_filled: 0,
      line_span_candidate_rows_filled: 0,
      source_locators_filled: 0,
      source_page_or_section_hints_filled: 0,
      candidate_line_ranges_filled: 0,
      decision_fields_filled: 0,
      criteria_decisions_recorded: 0,
      criteria_rows_passed: 0,
      criteria_rows_failed: 0,
      criteria_rows_unfilled: evidenceRows.length,
      request_fields_filled: 0,
      request_packets_started: 0,
      requests_dispatched: 0,
      blockers_resolved: 0,
      blockers_unresolved: parent.gate_state.blockers_unresolved,
      blocker_rows_resolved: 0,
      blocker_rows_remaining: parent.gate_state.blocker_rows_remaining,
      true_precondition_cells: 0,
      true_precondition_updates_allowed: 0,
      false_precondition_cells: parent.gate_state.false_precondition_cells,
      source_system_decisions_recorded: 0,
      scope_decisions_recorded: 0,
      route_scope_notes_recorded: 0,
      local_register_review_requirements_recorded: 0,
      bridge_surface_review_requirements_recorded: 0,
      translation_owner_review_requirements_recorded: 0,
      rows_promoted: 0,
      publication_ready: false,
      translation_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      package_order_expected: packageOrder,
      permission_evidence_intake_rows_expected: 2560,
      blank_evidence_fields_per_row_expected: 8,
      blank_evidence_field_cells_expected: 20480,
      precondition_name_summary_rows_expected: 8,
      return_criterion_type_summary_rows_expected: 4,
      parent_criterion_type_summary_rows_expected: 8,
      packet_unit_summary_rows_expected: 10,
      zero_gate_assertions: [
        'evidence_fields_filled',
        'evidence_values_filled',
        'evidence_source_pointers_filled',
        'evidence_values_reviewed',
        'evidence_source_pointers_reviewed',
        'evidence_rows_filled',
        'evidence_intake_rows_filled',
        'permission_returns_received',
        'permission_return_fields_filled',
        'return_fields_filled',
        'returns_received',
        'returns_ingested',
        'line_span_candidate_permissions_recorded',
        'source_text_capture_permissions_recorded',
        'source_locator_permissions_granted',
        'line_span_selection_permissions_granted',
        'source_text_capture_permissions_granted',
        'excerpt_permissions_granted',
        'exact_line_spans_selected',
        'source_passages_selected',
        'excerpts_selected',
        'selected_excerpt_attribution_notices_filled',
        'source_prose_copied',
        'source_examples_copied',
        'translated_passages',
        'local_language_surfaces_filled',
        'bridge_surfaces_accepted',
        'semi_constructed_surfaces_accepted',
        'line_span_candidate_fields_filled',
        'line_span_candidate_rows_filled',
        'source_locators_filled',
        'source_page_or_section_hints_filled',
        'candidate_line_ranges_filled',
        'decision_fields_filled',
        'criteria_decisions_recorded',
        'criteria_rows_passed',
        'criteria_rows_failed',
        'request_fields_filled',
        'request_packets_started',
        'requests_dispatched',
        'blockers_resolved',
        'blocker_rows_resolved',
        'true_precondition_cells',
        'true_precondition_updates_allowed',
        'source_system_decisions_recorded',
        'scope_decisions_recorded',
        'route_scope_notes_recorded',
        'local_register_review_requirements_recorded',
        'bridge_surface_review_requirements_recorded',
        'translation_owner_review_requirements_recorded',
        'rows_promoted'
      ]
    },
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SOURCE_TEXT_CAPTURE_POLICY_RETURN_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_<timestamp>'
    ],
    decision: 'Package 128 allocates blank evidence-intake rows for package-127 line-span permission return rows. It does not fill evidence, receive returns, record permissions, select exact spans, copy source text, create excerpts, accept surfaces, draft translations, or claim readiness.'
  };
}

function buildArtifactMd(artifact) {
  const sampleRows = artifact.permission_evidence_intake_rows.slice(0, 20).map((row) => `| \`${row.permission_evidence_intake_row_id}\` | \`${row.parent_line_span_permission_return_row_id}\` | ${row.packet_unit} | ${row.precondition_name} | ${row.criterion_type} | \`${row.evidence_fields_filled}\` |`).join('\n');
  const preconditionRows = artifact.precondition_name_permission_evidence_intake_summary_rows.map((row) => `| ${row.precondition_name} | \`${row.evidence_intake_rows_required}\` | \`${row.blank_evidence_field_cells_allocated}\` | \`${row.evidence_values_filled}\` |`).join('\n');
  const typeRows = artifact.return_criterion_type_permission_evidence_intake_summary_rows.map((row) => `| ${row.criterion_type} | \`${row.evidence_intake_rows_required}\` | \`${row.blank_evidence_field_cells_allocated}\` | \`${row.evidence_values_filled}\` |`).join('\n');
  const parentTypeRows = artifact.parent_criterion_type_permission_evidence_intake_summary_rows.map((row) => `| ${row.parent_criterion_type} | \`${row.evidence_intake_rows_required}\` | \`${row.blank_evidence_field_cells_allocated}\` | \`${row.evidence_values_filled}\` |`).join('\n');
  const unitRows = artifact.packet_unit_permission_evidence_intake_summary_rows.map((row) => `| ${row.packet_unit} | \`${row.evidence_intake_rows_required}\` | \`${row.blank_evidence_field_cells_allocated}\` | \`${row.evidence_values_filled}\` |`).join('\n');
  const gateRows = Object.entries(artifact.gate_state).map(([key, value]) => `| ${key} | \`${Array.isArray(value) ? value.length : value}\` |`).join('\n');
  return `# OLP/DMOI Relation-Function Reviewer Scope Line-Span Permission Evidence Intake Ledger Template

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Evidence Intake Rows

Showing first 20 of \`${artifact.permission_evidence_intake_rows.length}\` blank evidence-intake rows.

| Evidence row | Parent permission return row | Packet unit | Precondition | Criterion type | Filled fields |
| --- | --- | --- | --- | --- | ---: |
${sampleRows}

## Precondition Summary

| Precondition | Evidence rows | Blank evidence cells | Evidence values filled |
| --- | ---: | ---: | ---: |
${preconditionRows}

## Return Criterion Type Summary

| Criterion type | Evidence rows | Blank evidence cells | Evidence values filled |
| --- | ---: | ---: | ---: |
${typeRows}

## Parent Criterion Type Summary

| Parent criterion type | Evidence rows | Blank evidence cells | Evidence values filled |
| --- | ---: | ---: | ---: |
${parentTypeRows}

## Packet Unit Summary

| Packet unit | Evidence rows | Blank evidence cells | Evidence values filled |
| --- | ---: | ---: | ---: |
${unitRows}

## Gate State

| Gate | State |
| --- | ---: |
${gateRows}

Decision: ${artifact.decision}
`;
}

function buildArtifactCsv(artifact) {
  const columns = [
    'permission_evidence_intake_row_id',
    'parent_line_span_permission_return_row_id',
    'parent_line_span_candidate_row_id',
    'parent_criteria_decision_row_id',
    'parent_resolution_return_evidence_intake_row_id',
    'parent_criterion_row_id',
    'parent_decision_precondition_blocker_resolution_return_evidence_criteria_row_id',
    'parent_decision_precondition_blocker_resolution_return_row_id',
    'parent_decision_precondition_blocker_resolution_request_row_id',
    'parent_decision_precondition_blocker_row_id',
    'parent_decision_precondition_checklist_row_id',
    'parent_reviewer_scope_criteria_decision_row_id',
    'parent_reviewer_scope_evidence_intake_row_id',
    'parent_ledger_row_id',
    'parent_reviewer_scope_row_id',
    'parent_gap_check_row_id',
    'parent_pointer_row_id',
    'packet_unit',
    'reviewer_role',
    'parent_criterion_type',
    'precondition_name',
    'criterion_type',
    'required_future_evidence_class',
    'blank_evidence_fields',
    'evidence_value',
    'evidence_source_pointer',
    'evidence_date',
    'non_personal_return_route_label',
    'reviewer_role_or_authority_class',
    'permission_evidence_review_note',
    'permission_decision',
    'evidence_fields_filled',
    'evidence_reviewed',
    'permission_return_received_after_evidence',
    'line_span_candidate_permission_recorded_after_evidence',
    'source_text_capture_permission_recorded_after_evidence',
    'exact_line_span_selected_after_evidence',
    'source_text_copied_after_evidence',
    'excerpt_selected_after_evidence',
    'surface_gate_opened',
    'translation_gate_opened'
  ];
  const rows = artifact.permission_evidence_intake_rows.map((row) => columns.map((column) => csvCell(row[column])).join(','));
  return `${columns.join(',')}\n${rows.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    source_artifact: artifact.artifact_id,
    package_order: packageOrder,
    status: 'pointer_only_reviewer_scope_line_span_permission_evidence_intake_ledger_template_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-128 OLP/DMOI reviewer-scope line-span permission evidence-intake continuation while preserving no-evidence/no-return/no-permission/no-source-text/no-excerpt/no-translation boundaries.',
    counts: {
      permission_evidence_intake_rows: g.permission_evidence_intake_rows,
      blank_evidence_fields_per_row: g.blank_evidence_fields_per_row,
      blank_evidence_field_cells_allocated: g.blank_evidence_field_cells_allocated,
      inherited_line_span_permission_return_rows: g.inherited_line_span_permission_return_rows,
      precondition_name_permission_evidence_intake_summary_rows: g.precondition_name_permission_evidence_intake_summary_rows,
      return_criterion_type_permission_evidence_intake_summary_rows: g.return_criterion_type_permission_evidence_intake_summary_rows,
      parent_criterion_type_permission_evidence_intake_summary_rows: g.parent_criterion_type_permission_evidence_intake_summary_rows,
      packet_unit_permission_evidence_intake_summary_rows: g.packet_unit_permission_evidence_intake_summary_rows
    },
    zero_gates: {
      evidence_fields_filled: 0,
      evidence_values_filled: 0,
      evidence_source_pointers_filled: 0,
      evidence_values_reviewed: 0,
      permission_returns_received: 0,
      line_span_candidate_permissions_recorded: 0,
      source_text_capture_permissions_recorded: 0,
      exact_line_spans_selected: 0,
      source_passages_selected: 0,
      source_prose_copied: 0,
      excerpts_selected: 0,
      selected_excerpt_attribution_notices_filled: 0,
      surfaces_filled: 0,
      translated_passages: 0,
      readiness_claims: 0
    },
    upload_intent: 'Queue the package-128 JSON/MD/CSV/checksum and this note for the existing Noether upload path as substantive coordination material; do not defer because of mobile-plan or bandwidth wording.',
    no_remote_action_by_this_note: true,
    message_template: `Package 128 added ${artifactId}: blank OLP/DMOI reviewer-scope line-span permission evidence-intake ledger. Counts: ${g.permission_evidence_intake_rows} evidence rows, ${g.blank_evidence_fields_per_row} blank fields per row, ${g.blank_evidence_field_cells_allocated} blank evidence-field cells; 0 evidence, 0 returns, 0 permissions, 0 exact spans, 0 source text/excerpts, 0 surfaces, 0 translations, 0 readiness.`
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 128 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 128 creates an OLP/DMOI relation-function reviewer-scope line-span permission evidence-intake ledger with \`${g.permission_evidence_intake_rows}\` blank evidence rows, \`${g.blank_evidence_fields_per_row}\` blank fields per row, and \`${g.blank_evidence_field_cells_allocated}\` blank evidence-field cells.

Zero gates: \`0\` evidence fields filled, \`0\` evidence values, \`0\` evidence source pointers, \`0\` evidence reviewed, \`0\` permission returns received, \`0\` line-span permissions, \`0\` source-text capture permissions, \`0\` exact line spans, \`0\` source passages, \`0\` source prose, \`0\` examples, \`0\` excerpts, \`0\` selected-excerpt attribution notices, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Upload intent: ${note.upload_intent}

Boundary: line-span permission evidence-intake ledger only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, translation, publication, pilot, legal-advice, or remote-state claim.
`;
}

async function writeArtifactAndNote(artifact, note) {
  await writeJson(artifactId, artifact);
  await writeFile(path.join(outputs, `${artifactId}.md`), buildArtifactMd(artifact), 'utf8');
  await writeFile(path.join(outputs, `${artifactId}.csv`), buildArtifactCsv(artifact), 'utf8');
  await writeJson(noteId, note);
  await writeFile(path.join(outputs, `${noteId}.md`), buildNoteMd(note, artifact), 'utf8');
}

async function updateRegistrations(artifact) {
  const packageIndex = await readJson(packageIndexFile);
  const order = ensureArray(packageIndex.obj, 'current_package_order');
  if (!order.some((row) => row?.artifact === artifactId)) {
    order.push({
      order: packageOrder,
      role: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template_support',
      artifact: artifactId,
      current_use: '2,560 blank line-span permission evidence-intake rows from package-127 permission return rows; 8 blank evidence fields per row; 20,480 blank evidence-field cells; 8 precondition-name summaries; 4 return-criterion-type summaries; 8 parent-criterion-type summaries; 10 packet-unit summaries; 0 evidence, 0 returns, 0 permissions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  packageIndex.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_rows: artifact.gate_state.permission_evidence_intake_rows,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_blank_cells: artifact.gate_state.blank_evidence_field_cells_allocated,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_values_filled: 0,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_returns_received: 0,
    olp_dmoi_relation_function_reviewer_scope_line_span_candidate_permissions_recorded: 0,
    olp_dmoi_relation_function_reviewer_scope_source_text_capture_permissions_recorded: 0,
    olp_dmoi_relation_function_reviewer_scope_exact_line_spans_selected: 0,
    olp_dmoi_relation_function_reviewer_scope_source_prose_copied: 0,
    olp_dmoi_relation_function_reviewer_scope_excerpts_selected: 0,
    olp_dmoi_relation_function_reviewer_scope_surfaces_filled: 0,
    olp_dmoi_relation_function_reviewer_scope_translations_filled: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_permission_evidence_criteria_decision_or_source_text_capture_policy_return_ledger_blank_only_no_source_text_no_surfaces_no_translation`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function reviewer-scope line-span permission evidence-intake ledger template',
    route: artifactId,
    license_status_to_recheck: 'line_span_permission_evidence_intake_ledger_only_no_evidence_no_returns_no_permissions_no_source_text_no_surfaces_no_translation',
    best_translation_use: 'future reviewer-scope permission-return evidence intake before source-text capture, excerpt, local/bridge surface, and translation-owner gates',
    candidate_lanes: ['semi_constructed_relation_function_source_request_lane', 'open_source_candidate_catalog', 'reviewer_scope_line_span_permission_evidence_intake_ledger_template', 'review_only_construction_scaffold'],
    priority: 1,
    status: 'reviewer_scope_line_span_permission_evidence_intake_ledger_template_no_evidence_no_returns_no_permissions_no_source_text_no_excerpts_no_surfaces_no_translation_no_pilot',
    gate_state: {
      permission_evidence_intake_rows: artifact.gate_state.permission_evidence_intake_rows,
      blank_evidence_field_cells_allocated: artifact.gate_state.blank_evidence_field_cells_allocated,
      evidence_values_filled: 0,
      permission_returns_received: 0,
      line_span_candidate_permissions_recorded: 0,
      source_text_capture_permissions_recorded: 0,
      exact_line_spans_selected: 0,
      source_prose_copied: 0,
      excerpts_selected: 0,
      translated_passages: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template: ${artifactId}_2560_blank_evidence_rows_20480_blank_cells_0_evidence_0_returns_0_permissions_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_rows: artifact.gate_state.permission_evidence_intake_rows,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_blank_cells: artifact.gate_state.blank_evidence_field_cells_allocated,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_values_filled: 0,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_returns_received: 0,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_candidate_permissions: 0,
    current_olp_dmoi_relation_function_reviewer_scope_source_text_capture_permissions: 0,
    current_olp_dmoi_relation_function_reviewer_scope_exact_line_spans: 0,
    current_olp_dmoi_relation_function_reviewer_scope_source_prose_copied: 0,
    current_olp_dmoi_relation_function_reviewer_scope_excerpts_selected: 0,
    current_olp_dmoi_relation_function_reviewer_scope_translations: 0,
    current_olp_dmoi_relation_function_reviewer_scope_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template: ${artifactId}_blank_only_no_evidence_no_returns_no_permissions_no_source_text_no_excerpts_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 2,560 blank line-span permission evidence-intake rows and 20,480 blank evidence-field cells from package-127 permission return rows; 0 evidence values, 0 permission returns received, 0 line-span permissions, 0 source-text permissions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be queued for upload when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function reviewer-scope line-span permission evidence-intake ledger template; 2,560 blank evidence rows, 20,480 blank evidence-field cells, 0 evidence, 0 returns, 0 permissions, 0 exact spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 128: OLP/DMOI relation-function reviewer-scope line-span permission evidence-intake ledger template after package 127. It records 2,560 blank evidence rows and 20,480 blank evidence-field cells while keeping 0 evidence values, 0 permission returns received, 0 line-span permissions, 0 source-text capture permissions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function reviewer-scope line-span permission evidence-intake ledger template | ${artifactId} | Permission evidence-intake ledger; 2,560 blank evidence rows, 20,480 blank cells, 0 evidence, 0 returns, 0 permissions, 0 exact spans, 0 source prose, 0 excerpts, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template_artifact: \`${artifactId}\` (2,560 blank evidence rows; 20,480 blank evidence cells; 0 evidence; 0 returns; 0 permissions; 0 source prose; 0 excerpts; no surfaces, no translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template: \`${artifactId}\`; evidence intake only, no evidence values, received returns, permissions, source text, excerpts, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI reviewer-scope line-span permission evidence-intake ledger template; blank evidence rows are not received evidence, permission returns, source-text permission, exact span selection, source text, excerpts, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_intake_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package128_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package128_coordination_note' },
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
  upload.obj.package128_upload_queue_update = {
    captured_utc: '2026-07-03T02:17:00Z',
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
  upload.obj.summary.network_actions_required_to_stage = 0;
  upload.obj.summary.network_actions_required_to_push = 1;
  upload.obj.staging_order = Array.isArray(upload.obj.staging_order) ? upload.obj.staging_order : [];
  const step = 'Stage package 128 OLP/DMOI relation-function reviewer-scope line-span permission evidence-intake artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.permission_evidence_intake_rows.length !== 2560) failures.push('permission_evidence_intake_rows_not_2560');
  if (artifact.precondition_name_permission_evidence_intake_summary_rows.length !== 8) failures.push('precondition_name_summary_rows_not_8');
  if (artifact.return_criterion_type_permission_evidence_intake_summary_rows.length !== 4) failures.push('return_criterion_type_summary_rows_not_4');
  if (artifact.parent_criterion_type_permission_evidence_intake_summary_rows.length !== 8) failures.push('parent_criterion_type_summary_rows_not_8');
  if (artifact.packet_unit_permission_evidence_intake_summary_rows.length !== 10) failures.push('packet_unit_summary_rows_not_10');
  if (g.blank_evidence_fields_per_row !== 8) failures.push(`blank_evidence_fields_per_row_not_8_${g.blank_evidence_fields_per_row}`);
  if (g.blank_evidence_field_cells_allocated !== 20480) failures.push(`blank_evidence_cells_not_20480_${g.blank_evidence_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.permission_evidence_intake_rows) {
    const filled = blankEvidenceFields.some((field) => row[field] !== null);
    if (filled || row.evidence_fields_filled !== 0 || row.evidence_value_filled || row.evidence_source_pointer_filled || row.evidence_reviewed || row.permission_return_received_after_evidence || row.line_span_candidate_permission_recorded_after_evidence || row.source_text_capture_permission_recorded_after_evidence || row.exact_line_span_selected_after_evidence || row.source_text_copied_after_evidence || row.excerpt_selected_after_evidence || row.surface_gate_opened || row.translation_gate_opened) {
      failures.push(`nonblank_permission_evidence_intake_row_${row.permission_evidence_intake_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  return failures;
}

const parent = (await readJson(parentPermissionReturnTemplate)).obj;
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
  permission_evidence_intake_rows: artifact.gate_state.permission_evidence_intake_rows,
  blank_evidence_fields_per_row: artifact.gate_state.blank_evidence_fields_per_row,
  blank_evidence_field_cells_allocated: artifact.gate_state.blank_evidence_field_cells_allocated,
  evidence_values_filled: artifact.gate_state.evidence_values_filled,
  permission_returns_received: artifact.gate_state.permission_returns_received,
  line_span_candidate_permissions_recorded: artifact.gate_state.line_span_candidate_permissions_recorded,
  source_text_capture_permissions_recorded: artifact.gate_state.source_text_capture_permissions_recorded,
  exact_line_spans_selected: artifact.gate_state.exact_line_spans_selected,
  source_prose_copied: artifact.gate_state.source_prose_copied,
  excerpts_selected: artifact.gate_state.excerpts_selected,
  local_language_surfaces_filled: artifact.gate_state.local_language_surfaces_filled,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
