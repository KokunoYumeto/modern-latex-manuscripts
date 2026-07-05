import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_REQUEST_TEMPLATE_20260703T031500Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_REQUEST_TEMPLATE_NOTE_20260703T031600Z';
const generatedUtc = '2026-07-03T03:15:00Z';
const noteGeneratedUtc = '2026-07-03T03:16:00Z';
const packageOrder = 132;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-REVIEWER-SCOPE-LINE-SPAN-PERMISSION-EVIDENCE-DECISION-PRECONDITION-BLOCKER-RESOLUTION-REQUEST-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentBlockerLedger = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_LEDGER_TEMPLATE_20260703T030000Z';
const parentArtifacts = [
  parentBlockerLedger,
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_CHECKLIST_TEMPLATE_20260703T024500Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_20260703T023000Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_INTAKE_LEDGER_TEMPLATE_20260703T021500Z'
];

const blankRequestFields = [
  'request_packet_id',
  'request_route_label',
  'non_personal_reviewer_or_owner_role',
  'request_scope_statement',
  'requested_resolution_action',
  'required_resolution_evidence_pointer',
  'requested_true_precondition_update_scope',
  'source_text_prohibition_clause',
  'downstream_line_span_gate_limit',
  'downstream_surface_translation_gate_limit',
  'request_date',
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

function requestId(index) {
  return `ODRF-RSCOPE-LSPAN-PEVID-DPCBRR-${String(index + 1).padStart(5, '0')}`;
}

function buildRequestRows(parent) {
  return parent.permission_evidence_decision_precondition_blocker_rows.map((row, index) => ({
    permission_evidence_decision_precondition_blocker_resolution_request_row_id: requestId(index),
    parent_permission_evidence_decision_precondition_blocker_row_id: row.permission_evidence_decision_precondition_blocker_row_id,
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
    blank_request_fields: blankRequestFields,
    request_packet_id: null,
    request_route_label: null,
    non_personal_reviewer_or_owner_role: null,
    request_scope_statement: null,
    requested_resolution_action: null,
    required_resolution_evidence_pointer: null,
    requested_true_precondition_update_scope: null,
    source_text_prohibition_clause: null,
    downstream_line_span_gate_limit: null,
    downstream_surface_translation_gate_limit: null,
    request_date: null,
    reviewer_note: null,
    request_fields_filled: 0,
    request_packet_started: false,
    request_dispatched: false,
    return_received: false,
    return_ingested: false,
    blocker_resolved_after_return: false,
    true_precondition_update_allowed_after_return: false,
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
    pilot_gate_opened: false
  }));
}

function requestRowsByParentBlocker(requestRows) {
  return new Map(requestRows.map((row) => [row.parent_permission_evidence_decision_precondition_blocker_row_id, row]));
}

function linkedRequests(requestsByBlocker, blockerIds) {
  return (blockerIds || []).map((id) => requestsByBlocker.get(id)).filter(Boolean);
}

function summarizeLinked(linked, base) {
  return {
    ...base,
    request_rows_required: linked.length,
    blank_request_field_cells_allocated: linked.length * blankRequestFields.length,
    request_rows_filled: 0,
    request_packets_started: 0,
    requests_dispatched: 0,
    returns_received: 0,
    returns_ingested: 0,
    blockers_resolved: 0,
    blockers_remaining: linked.length,
    true_precondition_cells: 0,
    false_precondition_cells_remaining: linked.length,
    decisions_recorded: 0,
    evidence_values_reviewed: 0,
    permission_returns_received: 0,
    line_span_candidate_permissions_recorded: 0,
    source_text_capture_permissions_recorded: 0,
    exact_line_spans_selected: 0,
    source_passages_selected: 0,
    excerpts_selected: 0,
    source_prose_copied: 0,
    local_language_surfaces_filled: 0,
    translated_passages: 0,
    linked_permission_evidence_decision_precondition_blocker_resolution_request_row_ids: linked.map((row) => row.permission_evidence_decision_precondition_blocker_resolution_request_row_id)
  };
}

function buildPreconditionNameSummaries(parent, requestRows) {
  const byBlocker = requestRowsByParentBlocker(requestRows);
  return parent.precondition_name_permission_evidence_decision_precondition_blocker_summary_rows.map((row, index) => {
    const linked = linkedRequests(byBlocker, row.linked_permission_evidence_decision_precondition_blocker_row_ids);
    return summarizeLinked(linked, {
      permission_evidence_decision_precondition_blocker_resolution_request_precondition_name_summary_row_id: `ODRF-RSCOPE-LSPAN-PEVID-DPCBRR-PRECOND-${String(index + 1).padStart(2, '0')}`,
      parent_permission_evidence_decision_precondition_blocker_precondition_name_summary_row_id: row.permission_evidence_decision_precondition_blocker_precondition_name_summary_row_id,
      blocker_precondition_name: row.blocker_precondition_name,
      precondition_name: row.precondition_name,
      required_future_resolution: row.required_future_resolution
    });
  });
}

function buildReturnCriterionTypeSummaries(parent, requestRows) {
  const byBlocker = requestRowsByParentBlocker(requestRows);
  return parent.return_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows.map((row, index) => {
    const linked = linkedRequests(byBlocker, row.linked_permission_evidence_decision_precondition_blocker_row_ids);
    return summarizeLinked(linked, {
      permission_evidence_decision_precondition_blocker_resolution_request_return_criterion_type_summary_row_id: `ODRF-RSCOPE-LSPAN-PEVID-DPCBRR-CTYPE-${String(index + 1).padStart(2, '0')}`,
      parent_permission_evidence_decision_precondition_blocker_return_criterion_type_summary_row_id: row.permission_evidence_decision_precondition_blocker_return_criterion_type_summary_row_id,
      criterion_type: row.criterion_type,
      required_future_evidence_class: row.required_future_evidence_class
    });
  });
}

function buildParentCriterionTypeSummaries(parent, requestRows) {
  const byBlocker = requestRowsByParentBlocker(requestRows);
  return parent.parent_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows.map((row, index) => {
    const linked = linkedRequests(byBlocker, row.linked_permission_evidence_decision_precondition_blocker_row_ids);
    return summarizeLinked(linked, {
      permission_evidence_decision_precondition_blocker_resolution_request_parent_criterion_type_summary_row_id: `ODRF-RSCOPE-LSPAN-PEVID-DPCBRR-PTYPE-${String(index + 1).padStart(2, '0')}`,
      parent_permission_evidence_decision_precondition_blocker_parent_criterion_type_summary_row_id: row.permission_evidence_decision_precondition_blocker_parent_criterion_type_summary_row_id,
      parent_criterion_type: row.parent_criterion_type
    });
  });
}

function buildPacketUnitSummaries(parent, requestRows) {
  const byBlocker = requestRowsByParentBlocker(requestRows);
  return parent.packet_unit_permission_evidence_decision_precondition_blocker_summary_rows.map((row, index) => {
    const linked = linkedRequests(byBlocker, row.linked_permission_evidence_decision_precondition_blocker_row_ids);
    return summarizeLinked(linked, {
      permission_evidence_decision_precondition_blocker_resolution_request_packet_unit_summary_row_id: `ODRF-RSCOPE-LSPAN-PEVID-DPCBRR-UNIT-${String(index + 1).padStart(2, '0')}`,
      parent_permission_evidence_decision_precondition_blocker_packet_unit_summary_row_id: row.permission_evidence_decision_precondition_blocker_packet_unit_summary_row_id,
      packet_unit: row.packet_unit,
      parent_ledger_row_id: row.parent_ledger_row_id,
      parent_pointer_row_id: row.parent_pointer_row_id
    });
  });
}

function buildArtifact(parent) {
  const requestRows = buildRequestRows(parent);
  const preconditionNameSummaries = buildPreconditionNameSummaries(parent, requestRows);
  const returnCriterionTypeSummaries = buildReturnCriterionTypeSummaries(parent, requestRows);
  const parentCriterionTypeSummaries = buildParentCriterionTypeSummaries(parent, requestRows);
  const packetUnitSummaries = buildPacketUnitSummaries(parent, requestRows);
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template_blank_no_dispatches_no_returns_no_resolutions_no_permissions_no_source_text_no_excerpts_no_surfaces_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Create blank request rows for future non-personal review of package-131 unresolved line-span permission evidence decision-precondition blockers while keeping all permission, source-text, excerpt, surface, translation, publication, and pilot gates closed.',
    parent_artifacts: parentArtifacts,
    resolution_request_boundary: {
      template_is: 'blank resolution-request template for unresolved package-131 line-span permission evidence decision-precondition blockers',
      template_is_not: [
        'dispatched request packet',
        'reviewer return',
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
        'allocate blank request rows for every unresolved package-131 blocker row',
        'allocate twelve blank request fields per blocker row',
        'summarize blank request coverage by blocker precondition, return criterion type, parent criterion type, and packet unit',
        'queue substantive artifacts for upload when a staging path exists'
      ],
      blocked_now: [
        'filling request fields',
        'starting request packets',
        'dispatching requests',
        'ingesting returns',
        'resolving blockers',
        'setting preconditions true',
        'reviewing evidence',
        'recording line-span or source-text permissions',
        'selecting exact line spans',
        'copying source prose, examples, passages, or excerpts',
        'opening local, bridge, semi-constructed surface, translation, publication, or pilot gates'
      ]
    },
    blank_request_fields: blankRequestFields,
    permission_evidence_decision_precondition_blocker_resolution_request_rows: requestRows,
    precondition_name_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows: preconditionNameSummaries,
    return_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows: returnCriterionTypeSummaries,
    parent_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows: parentCriterionTypeSummaries,
    packet_unit_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows: packetUnitSummaries,
    gate_state: {
      permission_evidence_decision_precondition_blocker_resolution_request_rows: requestRows.length,
      precondition_name_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows: preconditionNameSummaries.length,
      return_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows: returnCriterionTypeSummaries.length,
      parent_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows: parentCriterionTypeSummaries.length,
      packet_unit_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows: packetUnitSummaries.length,
      blank_request_fields_per_row: blankRequestFields.length,
      blank_resolution_request_field_cells_allocated: requestRows.length * blankRequestFields.length,
      inherited_permission_evidence_decision_precondition_blocker_rows: parent.gate_state.permission_evidence_decision_precondition_blocker_rows,
      inherited_blockers_unresolved: parent.gate_state.blockers_unresolved,
      inherited_blockers_resolved: parent.gate_state.blockers_resolved,
      inherited_false_precondition_cells: parent.gate_state.false_precondition_cells,
      inherited_true_precondition_cells: parent.gate_state.true_precondition_cells,
      inherited_criteria_rows_unfilled: parent.gate_state.criteria_rows_unfilled,
      request_fields_filled: 0,
      request_packets_started: 0,
      requests_dispatched: 0,
      returns_received: 0,
      returns_ingested: 0,
      blockers_resolved: 0,
      blockers_unresolved: requestRows.length,
      blocker_rows_resolved: 0,
      blocker_rows_remaining: requestRows.length,
      true_precondition_cells: 0,
      false_precondition_cells: requestRows.length,
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
      return_fields_filled: 0,
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
      permission_evidence_decision_precondition_blocker_resolution_request_rows_expected: 20480,
      blank_request_fields_per_row_expected: 12,
      blank_resolution_request_field_cells_expected: 245760,
      precondition_name_resolution_request_summary_rows_expected: 8,
      return_criterion_type_resolution_request_summary_rows_expected: 4,
      parent_criterion_type_resolution_request_summary_rows_expected: 8,
      packet_unit_resolution_request_summary_rows_expected: 10,
      inherited_permission_evidence_decision_precondition_blocker_rows_expected: 20480,
      zero_gate_assertions: [
        'request_fields_filled',
        'request_packets_started',
        'requests_dispatched',
        'returns_received',
        'returns_ingested',
        'blockers_resolved',
        'blocker_rows_resolved',
        'true_precondition_cells',
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
        'return_fields_filled',
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
      'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SOURCE_TEXT_CAPTURE_POLICY_RETURN_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_<timestamp>'
    ],
    decision: 'Package 132 allocates blank request rows for every package-131 unresolved blocker. It does not fill request fields, start or dispatch request packets, ingest returns, resolve blockers, set true preconditions, review evidence, record permissions, select exact spans, copy source text, create excerpts, accept surfaces, draft translations, or claim readiness.'
  };
}

function buildArtifactMd(artifact) {
  const sampleRows = artifact.permission_evidence_decision_precondition_blocker_resolution_request_rows.slice(0, 20).map((row) => `| \`${row.permission_evidence_decision_precondition_blocker_resolution_request_row_id}\` | \`${row.parent_permission_evidence_decision_precondition_blocker_row_id}\` | ${row.packet_unit} | ${row.blocker_precondition_name} | ${row.criterion_type} | \`${row.request_fields_filled}\` |`).join('\n');
  const preconditionRows = artifact.precondition_name_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows.map((row) => `| ${row.blocker_precondition_name} | \`${row.request_rows_required}\` | \`${row.blank_request_field_cells_allocated}\` | \`${row.requests_dispatched}\` | \`${row.returns_received}\` |`).join('\n');
  const typeRows = artifact.return_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows.map((row) => `| ${row.criterion_type} | \`${row.request_rows_required}\` | \`${row.blank_request_field_cells_allocated}\` | \`${row.requests_dispatched}\` | \`${row.returns_received}\` |`).join('\n');
  const parentTypeRows = artifact.parent_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows.map((row) => `| ${row.parent_criterion_type} | \`${row.request_rows_required}\` | \`${row.blank_request_field_cells_allocated}\` | \`${row.requests_dispatched}\` | \`${row.returns_received}\` |`).join('\n');
  const unitRows = artifact.packet_unit_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows.map((row) => `| ${row.packet_unit} | \`${row.request_rows_required}\` | \`${row.blank_request_field_cells_allocated}\` | \`${row.requests_dispatched}\` | \`${row.returns_received}\` |`).join('\n');
  const gateRows = Object.entries(artifact.gate_state).map(([key, value]) => `| ${key} | \`${Array.isArray(value) ? value.length : value}\` |`).join('\n');
  return `# OLP/DMOI Relation-Function Reviewer Scope Line-Span Permission Evidence Decision Precondition Blocker Resolution Request Template

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Request Rows

Showing first 20 of \`${artifact.permission_evidence_decision_precondition_blocker_resolution_request_rows.length}\` blank request rows.

| Request row | Parent blocker row | Packet unit | Blocker precondition | Criterion type | Filled fields |
| --- | --- | --- | --- | --- | ---: |
${sampleRows}

## Precondition Summary

| Blocker precondition | Request rows | Blank request cells | Dispatches | Returns |
| --- | ---: | ---: | ---: | ---: |
${preconditionRows}

## Return Criterion Type Summary

| Criterion type | Request rows | Blank request cells | Dispatches | Returns |
| --- | ---: | ---: | ---: | ---: |
${typeRows}

## Parent Criterion Type Summary

| Parent criterion type | Request rows | Blank request cells | Dispatches | Returns |
| --- | ---: | ---: | ---: | ---: |
${parentTypeRows}

## Packet Unit Summary

| Packet unit | Request rows | Blank request cells | Dispatches | Returns |
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
    'permission_evidence_decision_precondition_blocker_resolution_request_row_id',
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
    'blank_request_fields',
    'request_fields_filled',
    'request_packet_started',
    'request_dispatched',
    'return_received',
    'return_ingested',
    'blocker_resolved_after_return',
    'source_text_capture_allowed_after_return',
    'excerpt_selection_allowed_after_return',
    'surface_gate_opened',
    'translation_gate_opened'
  ];
  const rows = artifact.permission_evidence_decision_precondition_blocker_resolution_request_rows.map((row) => columns.map((column) => csvCell(row[column])).join(','));
  return `${columns.join(',')}\n${rows.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    source_artifact: artifact.artifact_id,
    package_order: packageOrder,
    status: 'pointer_only_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-132 OLP/DMOI reviewer-scope line-span permission evidence decision-precondition blocker resolution-request template continuation while preserving no-dispatch/no-return/no-resolution/no-permission/no-source-text/no-excerpt/no-translation boundaries.',
    counts: {
      permission_evidence_decision_precondition_blocker_resolution_request_rows: g.permission_evidence_decision_precondition_blocker_resolution_request_rows,
      blank_request_fields_per_row: g.blank_request_fields_per_row,
      blank_resolution_request_field_cells_allocated: g.blank_resolution_request_field_cells_allocated,
      inherited_permission_evidence_decision_precondition_blocker_rows: g.inherited_permission_evidence_decision_precondition_blocker_rows,
      inherited_blockers_unresolved: g.inherited_blockers_unresolved,
      precondition_name_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows: g.precondition_name_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows,
      return_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows: g.return_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows,
      parent_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows: g.parent_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows,
      packet_unit_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows: g.packet_unit_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows
    },
    zero_gates: {
      request_fields_filled: 0,
      request_packets_started: 0,
      requests_dispatched: 0,
      returns_received: 0,
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
    upload_intent: 'Queue the package-132 JSON/MD/CSV/checksum and this note for the existing Noether upload path as substantive coordination material; do not defer because of mobile-plan or bandwidth wording.',
    no_remote_action_by_this_note: true,
    message_template: `Package 132 added ${artifactId}: blank OLP/DMOI reviewer-scope line-span permission evidence decision-precondition blocker resolution-request template. Counts: ${g.permission_evidence_decision_precondition_blocker_resolution_request_rows} request rows, ${g.blank_request_fields_per_row} blank fields per row, ${g.blank_resolution_request_field_cells_allocated} blank request-field cells; 0 request fields filled, 0 packets, 0 dispatches, 0 returns, 0 blockers resolved, 0 true preconditions, 0 evidence reviewed, 0 permissions, 0 source text/excerpts, 0 surfaces, 0 translations, 0 readiness.`
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 132 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 132 creates an OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker resolution-request template with \`${g.permission_evidence_decision_precondition_blocker_resolution_request_rows}\` blank request rows, \`${g.blank_request_fields_per_row}\` blank fields per row, and \`${g.blank_resolution_request_field_cells_allocated}\` blank request-field cells.

Zero gates: \`0\` request fields filled, \`0\` request packets, \`0\` dispatches, \`0\` returns, \`0\` blockers resolved, \`0\` true preconditions, \`0\` criteria decisions, \`0\` evidence values reviewed, \`0\` permission returns received, \`0\` line-span permissions, \`0\` source-text capture permissions, \`0\` exact line spans, \`0\` source prose, \`0\` examples, \`0\` excerpts, \`0\` selected-excerpt attribution notices, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Upload intent: ${note.upload_intent}

Boundary: resolution-request template only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, translation, publication, pilot, legal-advice, or remote-state claim.
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
      role: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template_support',
      artifact: artifactId,
      current_use: '20,480 blank line-span permission evidence decision-precondition blocker resolution-request rows from package-131 unresolved blockers; 12 blank request fields per row; 245,760 blank request-field cells; 8 precondition-name summaries; 4 return-criterion-type summaries; 8 parent-criterion-type summaries; 10 packet-unit summaries; 0 request fields filled, 0 packets, 0 dispatches, 0 returns, 0 blockers resolved, 0 true preconditions, 0 source prose, 0 excerpts, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  packageIndex.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_rows: artifact.gate_state.permission_evidence_decision_precondition_blocker_resolution_request_rows,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_blank_cells: artifact.gate_state.blank_resolution_request_field_cells_allocated,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_fields_filled: 0,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_packets: 0,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_dispatches: 0,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_returns: 0,
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
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_resolution_return_ledger_template_or_source_text_capture_policy_return_ledger_blank_only_no_source_text_no_surfaces_no_translation`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker resolution-request template',
    route: artifactId,
    license_status_to_recheck: 'line_span_permission_evidence_decision_precondition_blocker_resolution_request_template_only_no_dispatches_no_returns_no_resolutions_no_permissions_no_source_text_no_surfaces_no_translation',
    best_translation_use: 'future reviewer-scope permission-evidence blocker-resolution request planning before source-text capture, excerpt, local/bridge surface, and translation-owner gates',
    candidate_lanes: ['semi_constructed_relation_function_source_request_lane', 'open_source_candidate_catalog', 'reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template', 'review_only_construction_scaffold'],
    priority: 1,
    status: 'reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template_no_dispatches_no_returns_no_resolutions_no_permissions_no_source_text_no_excerpts_no_surfaces_no_translation_no_pilot',
    gate_state: {
      permission_evidence_decision_precondition_blocker_resolution_request_rows: artifact.gate_state.permission_evidence_decision_precondition_blocker_resolution_request_rows,
      blank_resolution_request_field_cells_allocated: artifact.gate_state.blank_resolution_request_field_cells_allocated,
      request_fields_filled: 0,
      requests_dispatched: 0,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template: ${artifactId}_20480_blank_requests_245760_blank_cells_0_dispatches_0_returns_0_resolutions_0_permissions_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_rows: artifact.gate_state.permission_evidence_decision_precondition_blocker_resolution_request_rows,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_blank_cells: artifact.gate_state.blank_resolution_request_field_cells_allocated,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_dispatches: 0,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_returns: 0,
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
  program.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template: ${artifactId}_blank_requests_only_no_dispatches_no_returns_no_permissions_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 20,480 blank line-span permission evidence decision-precondition blocker resolution-request rows from package-131 unresolved blockers, with 12 blank request fields per row and 245,760 blank request-field cells; 0 request fields filled, 0 request packets, 0 dispatches, 0 returns, 0 blockers resolved, 0 true preconditions, 0 permissions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be queued for upload when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker resolution-request template; 20,480 blank request rows, 245,760 blank request-field cells, 0 dispatches, 0 returns, 0 blockers resolved, 0 permissions, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 132: OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker resolution-request template after package 131. It records 20,480 blank request rows and 245,760 blank request-field cells while keeping 0 request fields filled, 0 request packets, 0 dispatches, 0 returns, 0 blockers resolved, 0 true preconditions, 0 permissions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker resolution-request template | ${artifactId} | Resolution-request template; 20,480 blank request rows, 245,760 blank cells, 0 dispatches, 0 returns, 0 blockers resolved, 0 permissions, 0 source prose, 0 excerpts, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template_artifact: \`${artifactId}\` (20,480 blank request rows; 245,760 blank request cells; 0 dispatches; 0 returns; 0 permissions; 0 source prose; 0 excerpts; no surfaces, no translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template: \`${artifactId}\`; request template only, no dispatches, returns, resolved blockers, permissions, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI reviewer-scope line-span permission evidence decision-precondition blocker resolution-request template; blank request rows are not dispatches, returns, evidence review, permission grants, exact excerpt authorization, source text, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_resolution_request_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package132_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package132_coordination_note' },
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
  upload.obj.package132_upload_queue_update = {
    captured_utc: '2026-07-03T03:17:00Z',
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
  const step = 'Stage package 132 OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker resolution-request artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.permission_evidence_decision_precondition_blocker_resolution_request_rows.length !== 20480) failures.push('request_rows_not_20480');
  if (artifact.precondition_name_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows.length !== 8) failures.push('precondition_name_summary_rows_not_8');
  if (artifact.return_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows.length !== 4) failures.push('return_criterion_type_summary_rows_not_4');
  if (artifact.parent_criterion_type_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows.length !== 8) failures.push('parent_criterion_type_summary_rows_not_8');
  if (artifact.packet_unit_permission_evidence_decision_precondition_blocker_resolution_request_summary_rows.length !== 10) failures.push('packet_unit_summary_rows_not_10');
  if (g.blank_request_fields_per_row !== 12) failures.push(`blank_request_fields_per_row_not_12_${g.blank_request_fields_per_row}`);
  if (g.blank_resolution_request_field_cells_allocated !== 245760) failures.push(`blank_request_cells_not_245760_${g.blank_resolution_request_field_cells_allocated}`);
  if (g.inherited_permission_evidence_decision_precondition_blocker_rows !== 20480) failures.push(`inherited_blocker_rows_not_20480_${g.inherited_permission_evidence_decision_precondition_blocker_rows}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.permission_evidence_decision_precondition_blocker_resolution_request_rows) {
    const filled = blankRequestFields.some((field) => row[field] !== null);
    if (filled ||
      row.request_fields_filled !== 0 ||
      row.request_packet_started ||
      row.request_dispatched ||
      row.return_received ||
      row.return_ingested ||
      row.blocker_resolved_after_return ||
      row.true_precondition_update_allowed_after_return ||
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
      failures.push(`unsafe_request_row_${row.permission_evidence_decision_precondition_blocker_resolution_request_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  return failures;
}

const parent = (await readJson(parentBlockerLedger)).obj;
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
  request_rows: artifact.gate_state.permission_evidence_decision_precondition_blocker_resolution_request_rows,
  blank_request_fields_per_row: artifact.gate_state.blank_request_fields_per_row,
  blank_resolution_request_field_cells_allocated: artifact.gate_state.blank_resolution_request_field_cells_allocated,
  inherited_blocker_rows: artifact.gate_state.inherited_permission_evidence_decision_precondition_blocker_rows,
  request_fields_filled: artifact.gate_state.request_fields_filled,
  request_packets_started: artifact.gate_state.request_packets_started,
  requests_dispatched: artifact.gate_state.requests_dispatched,
  returns_received: artifact.gate_state.returns_received,
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
