import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_LEDGER_TEMPLATE_20260703T033000Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_LEDGER_TEMPLATE_NOTE_20260703T033100Z';
const generatedUtc = '2026-07-03T03:30:00Z';
const noteGeneratedUtc = '2026-07-03T03:31:00Z';
const packageOrder = 133;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-REVIEWER-SCOPE-LINE-SPAN-PERMISSION-EVIDENCE-DECISION-PRECONDITION-BLOCKER-RESOLUTION-RETURN-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentRequestTemplate = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_REQUEST_TEMPLATE_20260703T031500Z';
const parentArtifacts = [
  parentRequestTemplate,
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_LEDGER_TEMPLATE_20260703T030000Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_CHECKLIST_TEMPLATE_20260703T024500Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_20260703T023000Z'
];

const blankReturnFields = [
  'return_packet_id',
  'return_route_label',
  'non_personal_reviewer_or_owner_role',
  'return_scope_statement',
  'resolution_evidence_pointer',
  'returned_precondition_truth_value',
  'returned_resolution_decision',
  'source_text_prohibition_attestation',
  'downstream_line_span_gate_statement',
  'downstream_surface_translation_gate_statement',
  'return_date',
  'reviewer_note'
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

function returnId(index) {
  return `ODRF-RSCOPE-LSPAN-PEVID-DPCBRT-${String(index + 1).padStart(5, '0')}`;
}

function buildReturnRows(parent) {
  return parent.permission_evidence_decision_precondition_blocker_resolution_request_rows.map((row, index) => ({
    permission_evidence_decision_precondition_blocker_resolution_return_row_id: returnId(index),
    parent_permission_evidence_decision_precondition_blocker_resolution_request_row_id: row.permission_evidence_decision_precondition_blocker_resolution_request_row_id,
    parent_permission_evidence_decision_precondition_blocker_row_id: row.parent_permission_evidence_decision_precondition_blocker_row_id,
    parent_permission_evidence_decision_precondition_checklist_row_id: row.parent_permission_evidence_decision_precondition_checklist_row_id,
    parent_permission_evidence_criteria_decision_row_id: row.parent_permission_evidence_criteria_decision_row_id,
    parent_permission_evidence_intake_row_id: row.parent_permission_evidence_intake_row_id,
    parent_line_span_permission_return_row_id: row.parent_line_span_permission_return_row_id,
    parent_line_span_candidate_row_id: row.parent_line_span_candidate_row_id,
    parent_criteria_decision_row_id: row.parent_criteria_decision_row_id,
    parent_criterion_row_id: row.parent_criterion_row_id,
    parent_ledger_row_id: row.parent_ledger_row_id,
    parent_reviewer_scope_row_id: row.parent_reviewer_scope_row_id,
    parent_gap_check_row_id: row.parent_gap_check_row_id,
    parent_pointer_row_id: row.parent_pointer_row_id,
    packet_unit: row.packet_unit,
    reviewer_role: row.reviewer_role,
    source_systems_implicated: row.source_systems_implicated,
    parent_criterion_type: row.parent_criterion_type,
    parent_permission_evidence_criteria_decision_precondition_name: row.parent_permission_evidence_criteria_decision_precondition_name,
    criterion_type: row.criterion_type,
    required_future_evidence_class: row.required_future_evidence_class,
    blocker_precondition_name: row.blocker_precondition_name,
    blocker_reason: row.blocker_reason,
    required_future_resolution: row.required_future_resolution,
    blank_return_fields: blankReturnFields,
    return_packet_id: null,
    return_route_label: null,
    non_personal_reviewer_or_owner_role: null,
    return_scope_statement: null,
    resolution_evidence_pointer: null,
    returned_precondition_truth_value: null,
    returned_resolution_decision: null,
    source_text_prohibition_attestation: null,
    downstream_line_span_gate_statement: null,
    downstream_surface_translation_gate_statement: null,
    return_date: null,
    reviewer_note: null,
    return_fields_filled: 0,
    return_received: false,
    return_ingested: false,
    resolution_evidence_pointer_reviewed: false,
    source_text_prohibition_confirmed: false,
    true_precondition_update_allowed_after_return: false,
    blocker_resolved_after_return: false,
    permission_evidence_decision_precondition_ready_after_return: false,
    line_span_candidate_permission_allowed_after_return: false,
    source_text_capture_permission_allowed_after_return: false,
    exact_line_span_selection_allowed_after_return: false,
    source_text_capture_allowed_after_return: false,
    excerpt_selection_allowed_after_return: false,
    local_language_surface_allowed_after_return: false,
    surface_gate_opened: false,
    translation_gate_opened: false,
    publication_gate_opened: false,
    pilot_gate_opened: false,
    return_status: 'blank_return_template_only'
  }));
}

function returnRowsByParentRequest(returnRows) {
  return new Map(returnRows.map((row) => [row.parent_permission_evidence_decision_precondition_blocker_resolution_request_row_id, row]));
}

function linkedReturns(returnsByRequest, requestIds) {
  return (requestIds || []).map((id) => returnsByRequest.get(id)).filter(Boolean);
}

function summarizeLinked(linked, base) {
  return {
    ...base,
    return_rows_required: linked.length,
    blank_return_field_cells_allocated: linked.length * blankReturnFields.length,
    return_rows_filled: 0,
    return_fields_filled: 0,
    returns_received: 0,
    returns_ingested: 0,
    blockers_resolved: 0,
    blockers_remaining: linked.length,
    true_precondition_cells: 0,
    true_precondition_updates_allowed: 0,
    false_precondition_cells_remaining: linked.length,
    decisions_recorded: 0,
    evidence_values_reviewed: 0,
    resolution_evidence_pointers_reviewed: 0,
    permission_returns_received: 0,
    line_span_candidate_permissions_recorded: 0,
    source_text_capture_permissions_recorded: 0,
    exact_line_spans_selected: 0,
    source_passages_selected: 0,
    excerpts_selected: 0,
    source_prose_copied: 0,
    local_language_surfaces_filled: 0,
    translated_passages: 0,
    linked_permission_evidence_decision_precondition_blocker_resolution_return_row_ids: linked.map((row) => row.permission_evidence_decision_precondition_blocker_resolution_return_row_id)
  };
}

function buildPreconditionNameSummaries(parent, returnRows) {
  const byRequest = returnRowsByParentRequest(returnRows);
  return parent.precondition_name_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows.map((row, index) => {
    const linked = linkedReturns(byRequest, row.linked_permission_evidence_decision_precondition_blocker_resolution_request_row_ids);
    return summarizeLinked(linked, {
      permission_evidence_decision_precondition_blocker_resolution_return_precondition_name_summary_row_id: `ODRF-RSCOPE-LSPAN-PEVID-DPCBRT-PRECOND-${String(index + 1).padStart(2, '0')}`,
      parent_permission_evidence_decision_precondition_blocker_resolution_request_precondition_name_summary_row_id: row.permission_evidence_decision_precondition_blocker_resolution_request_precondition_name_summary_row_id,
      blocker_precondition_name: row.blocker_precondition_name,
      precondition_name: row.precondition_name,
      required_future_resolution: row.required_future_resolution
    });
  });
}

function buildReturnCriterionTypeSummaries(parent, returnRows) {
  const byRequest = returnRowsByParentRequest(returnRows);
  return parent.return_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows.map((row, index) => {
    const linked = linkedReturns(byRequest, row.linked_permission_evidence_decision_precondition_blocker_resolution_request_row_ids);
    return summarizeLinked(linked, {
      permission_evidence_decision_precondition_blocker_resolution_return_return_criterion_type_summary_row_id: `ODRF-RSCOPE-LSPAN-PEVID-DPCBRT-CTYPE-${String(index + 1).padStart(2, '0')}`,
      parent_permission_evidence_decision_precondition_blocker_resolution_request_return_criterion_type_summary_row_id: row.permission_evidence_decision_precondition_blocker_resolution_request_return_criterion_type_summary_row_id,
      criterion_type: row.criterion_type,
      required_future_evidence_class: row.required_future_evidence_class
    });
  });
}

function buildParentCriterionTypeSummaries(parent, returnRows) {
  const byRequest = returnRowsByParentRequest(returnRows);
  return parent.parent_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows.map((row, index) => {
    const linked = linkedReturns(byRequest, row.linked_permission_evidence_decision_precondition_blocker_resolution_request_row_ids);
    return summarizeLinked(linked, {
      permission_evidence_decision_precondition_blocker_resolution_return_parent_criterion_type_summary_row_id: `ODRF-RSCOPE-LSPAN-PEVID-DPCBRT-PTYPE-${String(index + 1).padStart(2, '0')}`,
      parent_permission_evidence_decision_precondition_blocker_resolution_request_parent_criterion_type_summary_row_id: row.permission_evidence_decision_precondition_blocker_resolution_request_parent_criterion_type_summary_row_id,
      parent_criterion_type: row.parent_criterion_type
    });
  });
}

function buildPacketUnitSummaries(parent, returnRows) {
  const byRequest = returnRowsByParentRequest(returnRows);
  return parent.packet_unit_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows.map((row, index) => {
    const linked = linkedReturns(byRequest, row.linked_permission_evidence_decision_precondition_blocker_resolution_request_row_ids);
    return summarizeLinked(linked, {
      permission_evidence_decision_precondition_blocker_resolution_return_packet_unit_summary_row_id: `ODRF-RSCOPE-LSPAN-PEVID-DPCBRT-UNIT-${String(index + 1).padStart(2, '0')}`,
      parent_permission_evidence_decision_precondition_blocker_resolution_request_packet_unit_summary_row_id: row.permission_evidence_decision_precondition_blocker_resolution_request_packet_unit_summary_row_id,
      packet_unit: row.packet_unit,
      parent_ledger_row_id: row.parent_ledger_row_id,
      parent_pointer_row_id: row.parent_pointer_row_id
    });
  });
}

function buildArtifact(parent) {
  const returnRows = buildReturnRows(parent);
  const preconditionNameSummaries = buildPreconditionNameSummaries(parent, returnRows);
  const returnCriterionTypeSummaries = buildReturnCriterionTypeSummaries(parent, returnRows);
  const parentCriterionTypeSummaries = buildParentCriterionTypeSummaries(parent, returnRows);
  const packetUnitSummaries = buildPacketUnitSummaries(parent, returnRows);
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template_blank_no_returns_no_resolutions_no_permissions_no_source_text_no_excerpts_no_surfaces_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Create blank return-ledger rows for future non-personal responses to package-132 resolution-request rows while preserving no-return, no-resolution, no-permission, no-source-text, no-excerpt, no-surface, no-translation, no-publication, and no-pilot boundaries now.',
    parent_artifacts: parentArtifacts,
    resolution_return_boundary: {
      ledger_is: 'blank return ledger for future responses to package-132 line-span permission evidence decision-precondition blocker resolution requests',
      ledger_is_not: [
        'received return',
        'filled return ledger',
        'blocker resolution',
        'true precondition update',
        'evidence review result',
        'permission grant',
        'source locator ledger',
        'line-span selection',
        'source text or excerpt',
        'surface proposal',
        'translation draft',
        'publication or pilot claim'
      ],
      allowed_now: [
        'allocate one blank return row for every package-132 request row',
        'allocate twelve blank return fields per request row',
        'summarize blank return coverage by blocker precondition, return criterion type, parent criterion type, and packet unit',
        'queue substantive artifacts for upload when a staging path exists'
      ],
      blocked_now: [
        'filling return fields',
        'marking returns received',
        'reviewing resolution evidence',
        'resolving blockers',
        'setting preconditions true',
        'recording permission grants',
        'selecting exact line spans',
        'copying source prose, examples, passages, or excerpts',
        'opening local, bridge, semi-constructed surface, translation, publication, or pilot gates'
      ]
    },
    blank_return_fields: blankReturnFields,
    permission_evidence_decision_precondition_blocker_resolution_return_rows: returnRows,
    precondition_name_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows: preconditionNameSummaries,
    return_criterion_type_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows: returnCriterionTypeSummaries,
    parent_criterion_type_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows: parentCriterionTypeSummaries,
    packet_unit_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows: packetUnitSummaries,
    gate_state: {
      permission_evidence_decision_precondition_blocker_resolution_return_rows: returnRows.length,
      precondition_name_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows: preconditionNameSummaries.length,
      return_criterion_type_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows: returnCriterionTypeSummaries.length,
      parent_criterion_type_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows: parentCriterionTypeSummaries.length,
      packet_unit_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows: packetUnitSummaries.length,
      blank_return_fields_per_row: blankReturnFields.length,
      blank_resolution_return_field_cells_allocated: returnRows.length * blankReturnFields.length,
      inherited_permission_evidence_decision_precondition_blocker_resolution_request_rows: parent.gate_state.permission_evidence_decision_precondition_blocker_resolution_request_rows,
      inherited_blank_resolution_request_field_cells: parent.gate_state.blank_resolution_request_field_cells_allocated,
      inherited_request_fields_filled: parent.gate_state.request_fields_filled,
      inherited_requests_dispatched: parent.gate_state.requests_dispatched,
      inherited_blockers_unresolved: parent.gate_state.blockers_unresolved,
      return_fields_filled: 0,
      returns_received: 0,
      returns_ingested: 0,
      request_fields_filled: 0,
      request_packets_started: 0,
      requests_dispatched: 0,
      blockers_resolved: 0,
      blockers_unresolved: returnRows.length,
      blocker_rows_resolved: 0,
      blocker_rows_remaining: returnRows.length,
      true_precondition_cells: 0,
      true_precondition_updates_allowed: 0,
      false_precondition_cells: returnRows.length,
      decision_fields_filled: 0,
      criteria_decisions_recorded: 0,
      criteria_rows_passed: 0,
      criteria_rows_failed: 0,
      criteria_rows_unfilled: parent.gate_state.criteria_rows_unfilled,
      evidence_values_reviewed: 0,
      evidence_source_pointers_reviewed: 0,
      evidence_values_filled: 0,
      evidence_source_pointers_filled: 0,
      evidence_rows_filled: 0,
      evidence_intake_rows_filled: 0,
      evidence_fields_filled: 0,
      permission_returns_received: 0,
      permission_return_fields_filled: 0,
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
      permission_evidence_decision_precondition_blocker_resolution_return_rows_expected: 20480,
      blank_return_fields_per_row_expected: 12,
      blank_resolution_return_field_cells_expected: 245760,
      precondition_name_resolution_return_summary_rows_expected: 8,
      return_criterion_type_resolution_return_summary_rows_expected: 4,
      parent_criterion_type_resolution_return_summary_rows_expected: 8,
      packet_unit_resolution_return_summary_rows_expected: 10,
      inherited_permission_evidence_decision_precondition_blocker_resolution_request_rows_expected: 20480,
      zero_gate_assertions: [
        'return_fields_filled',
        'returns_received',
        'returns_ingested',
        'request_fields_filled',
        'request_packets_started',
        'requests_dispatched',
        'blockers_resolved',
        'blocker_rows_resolved',
        'true_precondition_cells',
        'true_precondition_updates_allowed',
        'decision_fields_filled',
        'criteria_decisions_recorded',
        'criteria_rows_passed',
        'criteria_rows_failed',
        'evidence_values_reviewed',
        'evidence_source_pointers_reviewed',
        'evidence_values_filled',
        'evidence_source_pointers_filled',
        'evidence_rows_filled',
        'evidence_intake_rows_filled',
        'evidence_fields_filled',
        'permission_returns_received',
        'permission_return_fields_filled',
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
      'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_CRITERIA_RUBRIC_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SOURCE_TEXT_CAPTURE_POLICY_RETURN_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_<timestamp>'
    ],
    decision: 'Package 133 allocates blank return-ledger rows for every package-132 request row. It does not fill return fields, receive or ingest returns, resolve blockers, set true preconditions, review evidence, record permissions, select exact spans, copy source text, create excerpts, accept surfaces, draft translations, or claim readiness.'
  };
}

function buildArtifactMd(artifact) {
  const sampleRows = artifact.permission_evidence_decision_precondition_blocker_resolution_return_rows.slice(0, 20).map((row) => `| \`${row.permission_evidence_decision_precondition_blocker_resolution_return_row_id}\` | \`${row.parent_permission_evidence_decision_precondition_blocker_resolution_request_row_id}\` | ${row.packet_unit} | ${row.blocker_precondition_name} | ${row.criterion_type} | \`${row.return_fields_filled}\` |`).join('\n');
  const preconditionRows = artifact.precondition_name_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows.map((row) => `| ${row.blocker_precondition_name} | \`${row.return_rows_required}\` | \`${row.blank_return_field_cells_allocated}\` | \`${row.returns_received}\` | \`${row.blockers_resolved}\` |`).join('\n');
  const typeRows = artifact.return_criterion_type_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows.map((row) => `| ${row.criterion_type} | \`${row.return_rows_required}\` | \`${row.blank_return_field_cells_allocated}\` | \`${row.returns_received}\` | \`${row.blockers_resolved}\` |`).join('\n');
  const parentTypeRows = artifact.parent_criterion_type_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows.map((row) => `| ${row.parent_criterion_type} | \`${row.return_rows_required}\` | \`${row.blank_return_field_cells_allocated}\` | \`${row.returns_received}\` | \`${row.blockers_resolved}\` |`).join('\n');
  const unitRows = artifact.packet_unit_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows.map((row) => `| ${row.packet_unit} | \`${row.return_rows_required}\` | \`${row.blank_return_field_cells_allocated}\` | \`${row.returns_received}\` | \`${row.blockers_resolved}\` |`).join('\n');
  const gateRows = Object.entries(artifact.gate_state).map(([key, value]) => `| ${key} | \`${Array.isArray(value) ? value.length : value}\` |`).join('\n');
  return `# OLP/DMOI Relation-Function Reviewer Scope Line-Span Permission Evidence Decision Precondition Blocker Resolution Return Ledger Template

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Return Rows

Showing first 20 of \`${artifact.permission_evidence_decision_precondition_blocker_resolution_return_rows.length}\` blank return rows.

| Return row | Parent request row | Packet unit | Blocker precondition | Criterion type | Filled fields |
| --- | --- | --- | --- | --- | ---: |
${sampleRows}

## Precondition Summary

| Blocker precondition | Return rows | Blank return cells | Returns received | Blockers resolved |
| --- | ---: | ---: | ---: | ---: |
${preconditionRows}

## Return Criterion Type Summary

| Criterion type | Return rows | Blank return cells | Returns received | Blockers resolved |
| --- | ---: | ---: | ---: | ---: |
${typeRows}

## Parent Criterion Type Summary

| Parent criterion type | Return rows | Blank return cells | Returns received | Blockers resolved |
| --- | ---: | ---: | ---: | ---: |
${parentTypeRows}

## Packet Unit Summary

| Packet unit | Return rows | Blank return cells | Returns received | Blockers resolved |
| --- | ---: | ---: | ---: | ---: |
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
    'permission_evidence_decision_precondition_blocker_resolution_return_row_id',
    'parent_permission_evidence_decision_precondition_blocker_resolution_request_row_id',
    'parent_permission_evidence_decision_precondition_blocker_row_id',
    'parent_permission_evidence_decision_precondition_checklist_row_id',
    'parent_permission_evidence_criteria_decision_row_id',
    'parent_permission_evidence_intake_row_id',
    'parent_line_span_permission_return_row_id',
    'parent_line_span_candidate_row_id',
    'parent_criteria_decision_row_id',
    'parent_criterion_row_id',
    'parent_ledger_row_id',
    'parent_reviewer_scope_row_id',
    'parent_gap_check_row_id',
    'parent_pointer_row_id',
    'packet_unit',
    'reviewer_role',
    'parent_criterion_type',
    'criterion_type',
    'source_systems_implicated',
    'blocker_precondition_name',
    'blank_return_fields',
    'return_fields_filled',
    'return_received',
    'return_ingested',
    'blocker_resolved_after_return',
    'source_text_capture_allowed_after_return',
    'excerpt_selection_allowed_after_return',
    'surface_gate_opened',
    'translation_gate_opened',
    'return_status'
  ];
  const rows = artifact.permission_evidence_decision_precondition_blocker_resolution_return_rows.map((row) => columns.map((column) => csvCell(row[column])).join(','));
  return `${columns.join(',')}\n${rows.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    source_artifact: artifact.artifact_id,
    package_order: packageOrder,
    status: 'pointer_only_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-133 OLP/DMOI reviewer-scope line-span permission evidence decision-precondition blocker resolution-return ledger template continuation while preserving no-return/no-resolution/no-permission/no-source-text/no-excerpt/no-translation boundaries.',
    counts: {
      permission_evidence_decision_precondition_blocker_resolution_return_rows: g.permission_evidence_decision_precondition_blocker_resolution_return_rows,
      blank_return_fields_per_row: g.blank_return_fields_per_row,
      blank_resolution_return_field_cells_allocated: g.blank_resolution_return_field_cells_allocated,
      inherited_permission_evidence_decision_precondition_blocker_resolution_request_rows: g.inherited_permission_evidence_decision_precondition_blocker_resolution_request_rows,
      inherited_blank_resolution_request_field_cells: g.inherited_blank_resolution_request_field_cells,
      precondition_name_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows: g.precondition_name_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows,
      return_criterion_type_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows: g.return_criterion_type_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows,
      parent_criterion_type_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows: g.parent_criterion_type_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows,
      packet_unit_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows: g.packet_unit_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows
    },
    zero_gates: {
      return_fields_filled: 0,
      returns_received: 0,
      returns_ingested: 0,
      request_fields_filled: 0,
      requests_dispatched: 0,
      blockers_resolved: 0,
      true_precondition_cells: 0,
      decisions_recorded: 0,
      evidence_values_reviewed: 0,
      permission_returns_received: 0,
      line_span_candidate_permissions_recorded: 0,
      source_text_capture_permissions_recorded: 0,
      exact_line_spans_selected: 0,
      source_prose_copied: 0,
      excerpts_selected: 0,
      surfaces_filled: 0,
      translated_passages: 0,
      readiness_claims: 0
    },
    upload_intent: 'Queue the package-133 JSON/MD/CSV/checksum and this note for the existing Noether upload path as substantive coordination material; do not defer because of mobile-plan or bandwidth wording.',
    no_remote_action_by_this_note: true,
    message_template: `Package 133 added ${artifactId}: blank OLP/DMOI reviewer-scope line-span permission evidence decision-precondition blocker resolution-return ledger template. Counts: ${g.permission_evidence_decision_precondition_blocker_resolution_return_rows} return rows, ${g.blank_return_fields_per_row} blank fields per row, ${g.blank_resolution_return_field_cells_allocated} blank return-field cells; 0 return fields filled, 0 returns, 0 blockers resolved, 0 true preconditions, 0 evidence reviewed, 0 permissions, 0 source text/excerpts, 0 surfaces, 0 translations, 0 readiness.`
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 133 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 133 creates an OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker resolution-return ledger template with \`${g.permission_evidence_decision_precondition_blocker_resolution_return_rows}\` blank return rows, \`${g.blank_return_fields_per_row}\` blank fields per row, and \`${g.blank_resolution_return_field_cells_allocated}\` blank return-field cells.

Zero gates: \`0\` return fields filled, \`0\` returns received/ingested, \`0\` request fields filled, \`0\` dispatches, \`0\` blockers resolved, \`0\` true preconditions, \`0\` criteria decisions, \`0\` evidence values reviewed, \`0\` permission returns received, \`0\` line-span permissions, \`0\` source-text capture permissions, \`0\` exact line spans, \`0\` source prose, \`0\` examples, \`0\` excerpts, \`0\` selected-excerpt attribution notices, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Upload intent: ${note.upload_intent}

Boundary: resolution-return ledger template only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, translation, publication, pilot, legal-advice, or remote-state claim.
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
      role: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template_support',
      artifact: artifactId,
      current_use: '20,480 blank line-span permission evidence decision-precondition blocker resolution-return rows from package-132 request rows; 12 blank return fields per row; 245,760 blank return-field cells; 8 precondition-name summaries; 4 return-criterion-type summaries; 8 parent-criterion-type summaries; 10 packet-unit summaries; 0 returns, 0 blockers resolved, 0 true preconditions, 0 permissions, 0 source prose, 0 excerpts, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  packageIndex.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_rows: artifact.gate_state.permission_evidence_decision_precondition_blocker_resolution_return_rows,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_blank_cells: artifact.gate_state.blank_resolution_return_field_cells_allocated,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_fields_filled: 0,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_returns_received: 0,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blockers_resolved: 0,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_true_cells: 0,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_returns_received: 0,
    olp_dmoi_relation_function_reviewer_scope_line_span_candidate_permissions_recorded: 0,
    olp_dmoi_relation_function_reviewer_scope_source_text_capture_permissions_recorded: 0,
    olp_dmoi_relation_function_reviewer_scope_source_prose_copied: 0,
    olp_dmoi_relation_function_reviewer_scope_excerpts_selected: 0,
    olp_dmoi_relation_function_reviewer_scope_surfaces_filled: 0,
    olp_dmoi_relation_function_reviewer_scope_translations_filled: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_return_evidence_criteria_rubric_or_source_text_capture_policy_return_ledger_blank_only_no_source_text_no_surfaces_no_translation`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker resolution-return ledger template',
    route: artifactId,
    license_status_to_recheck: 'line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template_only_no_returns_no_resolutions_no_permissions_no_source_text_no_surfaces_no_translation',
    best_translation_use: 'future reviewer-scope permission-evidence blocker-resolution return planning before source-text capture, excerpt, local/bridge surface, and translation-owner gates',
    candidate_lanes: ['semi_constructed_relation_function_source_request_lane', 'open_source_candidate_catalog', 'reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template', 'review_only_construction_scaffold'],
    priority: 1,
    status: 'reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template_no_returns_no_resolutions_no_permissions_no_source_text_no_excerpts_no_surfaces_no_translation_no_pilot',
    gate_state: {
      permission_evidence_decision_precondition_blocker_resolution_return_rows: artifact.gate_state.permission_evidence_decision_precondition_blocker_resolution_return_rows,
      blank_resolution_return_field_cells_allocated: artifact.gate_state.blank_resolution_return_field_cells_allocated,
      return_fields_filled: 0,
      returns_received: 0,
      blockers_resolved: 0,
      true_precondition_cells: 0,
      permission_returns_received: 0,
      source_prose_copied: 0,
      excerpts_selected: 0,
      translated_passages: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template: ${artifactId}_20480_blank_returns_245760_blank_cells_0_returns_0_resolutions_0_permissions_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_rows: artifact.gate_state.permission_evidence_decision_precondition_blocker_resolution_return_rows,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_blank_cells: artifact.gate_state.blank_resolution_return_field_cells_allocated,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_returns_received: 0,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blockers_resolved: 0,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_true_cells: 0,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_returns_received: 0,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_candidate_permissions: 0,
    current_olp_dmoi_relation_function_reviewer_scope_source_text_capture_permissions: 0,
    current_olp_dmoi_relation_function_reviewer_scope_source_prose_copied: 0,
    current_olp_dmoi_relation_function_reviewer_scope_excerpts_selected: 0,
    current_olp_dmoi_relation_function_reviewer_scope_translations: 0,
    current_olp_dmoi_relation_function_reviewer_scope_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template: ${artifactId}_blank_returns_only_no_returns_no_resolutions_no_permissions_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 20,480 blank line-span permission evidence decision-precondition blocker resolution-return rows from package-132 request rows, with 12 blank return fields per row and 245,760 blank return-field cells; 0 return fields filled, 0 returns received, 0 blockers resolved, 0 true preconditions, 0 permissions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be queued for upload when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker resolution-return ledger template; 20,480 blank return rows, 245,760 blank return-field cells, 0 returns, 0 blockers resolved, 0 permissions, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 133: OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker resolution-return ledger template after package 132. It records 20,480 blank return rows and 245,760 blank return-field cells while keeping 0 return fields filled, 0 returns received/ingested, 0 blockers resolved, 0 true preconditions, 0 permissions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker resolution-return ledger template | ${artifactId} | Resolution-return ledger template; 20,480 blank return rows, 245,760 blank cells, 0 returns, 0 blockers resolved, 0 permissions, 0 source prose, 0 excerpts, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template_artifact: \`${artifactId}\` (20,480 blank return rows; 245,760 blank return cells; 0 returns; 0 blockers resolved; 0 permissions; 0 source prose; 0 excerpts; no surfaces, no translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template: \`${artifactId}\`; return ledger template only, no returns, resolved blockers, permissions, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI reviewer-scope line-span permission evidence decision-precondition blocker resolution-return ledger template; blank return rows are not returns, evidence review, permission grants, exact excerpt authorization, source text, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_return_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package133_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package133_coordination_note' },
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
  upload.obj.package133_upload_queue_update = {
    captured_utc: '2026-07-03T03:32:00Z',
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
  const step = 'Stage package 133 OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker resolution-return ledger artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.permission_evidence_decision_precondition_blocker_resolution_return_rows.length !== 20480) failures.push('return_rows_not_20480');
  if (artifact.precondition_name_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows.length !== 8) failures.push('precondition_name_summary_rows_not_8');
  if (artifact.return_criterion_type_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows.length !== 4) failures.push('return_criterion_type_summary_rows_not_4');
  if (artifact.parent_criterion_type_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows.length !== 8) failures.push('parent_criterion_type_summary_rows_not_8');
  if (artifact.packet_unit_permission_evidence_decision_precondition_blocker_resolution_return_summary_rows.length !== 10) failures.push('packet_unit_summary_rows_not_10');
  if (g.blank_return_fields_per_row !== 12) failures.push(`blank_return_fields_per_row_not_12_${g.blank_return_fields_per_row}`);
  if (g.blank_resolution_return_field_cells_allocated !== 245760) failures.push(`blank_return_cells_not_245760_${g.blank_resolution_return_field_cells_allocated}`);
  if (g.inherited_permission_evidence_decision_precondition_blocker_resolution_request_rows !== 20480) failures.push(`inherited_request_rows_not_20480_${g.inherited_permission_evidence_decision_precondition_blocker_resolution_request_rows}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.permission_evidence_decision_precondition_blocker_resolution_return_rows) {
    const filled = blankReturnFields.some((field) => row[field] !== null);
    if (filled ||
      row.return_fields_filled !== 0 ||
      row.return_received ||
      row.return_ingested ||
      row.resolution_evidence_pointer_reviewed ||
      row.source_text_prohibition_confirmed ||
      row.true_precondition_update_allowed_after_return ||
      row.blocker_resolved_after_return ||
      row.permission_evidence_decision_precondition_ready_after_return ||
      row.line_span_candidate_permission_allowed_after_return ||
      row.source_text_capture_permission_allowed_after_return ||
      row.exact_line_span_selection_allowed_after_return ||
      row.source_text_capture_allowed_after_return ||
      row.excerpt_selection_allowed_after_return ||
      row.local_language_surface_allowed_after_return ||
      row.surface_gate_opened ||
      row.translation_gate_opened ||
      row.publication_gate_opened ||
      row.pilot_gate_opened) {
      failures.push(`unsafe_return_row_${row.permission_evidence_decision_precondition_blocker_resolution_return_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  return failures;
}

const parent = (await readJson(parentRequestTemplate)).obj;
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
  return_rows: artifact.gate_state.permission_evidence_decision_precondition_blocker_resolution_return_rows,
  blank_return_fields_per_row: artifact.gate_state.blank_return_fields_per_row,
  blank_resolution_return_field_cells_allocated: artifact.gate_state.blank_resolution_return_field_cells_allocated,
  inherited_request_rows: artifact.gate_state.inherited_permission_evidence_decision_precondition_blocker_resolution_request_rows,
  return_fields_filled: artifact.gate_state.return_fields_filled,
  returns_received: artifact.gate_state.returns_received,
  returns_ingested: artifact.gate_state.returns_ingested,
  blockers_resolved: artifact.gate_state.blockers_resolved,
  true_precondition_cells: artifact.gate_state.true_precondition_cells,
  permission_returns_received: artifact.gate_state.permission_returns_received,
  exact_line_spans_selected: artifact.gate_state.exact_line_spans_selected,
  source_prose_copied: artifact.gate_state.source_prose_copied,
  excerpts_selected: artifact.gate_state.excerpts_selected,
  local_language_surfaces_filled: artifact.gate_state.local_language_surfaces_filled,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
