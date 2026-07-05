import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_LEDGER_TEMPLATE_20260703T030000Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_LEDGER_TEMPLATE_NOTE_20260703T030100Z';
const generatedUtc = '2026-07-03T03:00:00Z';
const noteGeneratedUtc = '2026-07-03T03:01:00Z';
const packageOrder = 131;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-REVIEWER-SCOPE-LINE-SPAN-PERMISSION-EVIDENCE-DECISION-PRECONDITION-BLOCKER-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentPreconditionChecklist = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_CHECKLIST_TEMPLATE_20260703T024500Z';
const parentArtifacts = [
  parentPreconditionChecklist,
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_20260703T023000Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_INTAKE_LEDGER_TEMPLATE_20260703T021500Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_RETURN_TEMPLATE_20260703T020000Z'
];

const preconditionNames = [
  'decision_row_linkage_validated',
  'all_decision_fields_filled',
  'all_criteria_decisions_recorded',
  'evidence_value_reviewed_or_explicitly_absent',
  'permission_return_and_scope_verified',
  'line_span_and_source_text_permissions_bounded',
  'source_text_guardrail_confirmed',
  'downstream_surface_translation_gates_separate'
];

const requiredFutureResolutionByPrecondition = {
  decision_row_linkage_validated: 'Validate that the package-130 checklist row links to the exact package-129 permission-evidence criteria-decision row and all inherited lineage rows.',
  all_decision_fields_filled: 'Fill every required decision field in the parent criteria-decision row before any promotion or permission-dependent action.',
  all_criteria_decisions_recorded: 'Record explicit pass/fail decisions for every required criterion without relying on blank or implied decisions.',
  evidence_value_reviewed_or_explicitly_absent: 'Review the evidence value or record a dated explicit absence result before treating the criterion as reviewed.',
  permission_return_and_scope_verified: 'Verify the dated non-personal permission return and its scope before any line-span, source-text, excerpt, surface, or translation step.',
  line_span_and_source_text_permissions_bounded: 'Record bounded line-span and source-text capture permissions before selecting exact spans or copying any source prose.',
  source_text_guardrail_confirmed: 'Confirm the source-text guardrail keeps prose, examples, passages, and excerpts absent until permission and attribution gates are separately satisfied.',
  downstream_surface_translation_gates_separate: 'Keep local surface, bridge surface, semi-constructed surface, translation, publication, and pilot gates separate until their own reviewer requirements are satisfied.'
};

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

function groupBy(rows, keyFn) {
  const map = new Map();
  for (const row of rows) {
    const key = keyFn(row);
    if (!map.has(key)) map.set(key, []);
    map.get(key).push(row);
  }
  return map;
}

function falsePreconditionNames(row) {
  return Object.entries(row.boolean_preconditions || {})
    .filter(([, value]) => value === false)
    .map(([name]) => name);
}

function buildBlockerRows(parent) {
  const rows = [];
  let index = 0;
  for (const parentRow of parent.permission_evidence_decision_precondition_checklist_rows) {
    for (const preconditionName of falsePreconditionNames(parentRow)) {
      index += 1;
      rows.push({
        permission_evidence_decision_precondition_blocker_row_id: `ODRF-RSCOPE-LSPAN-PEVID-DPCB-${String(index).padStart(5, '0')}`,
        parent_permission_evidence_decision_precondition_checklist_row_id: parentRow.permission_evidence_decision_precondition_checklist_row_id,
        parent_permission_evidence_criteria_decision_row_id: parentRow.parent_permission_evidence_criteria_decision_row_id,
        parent_permission_evidence_intake_row_id: parentRow.parent_permission_evidence_intake_row_id,
        parent_line_span_permission_return_row_id: parentRow.parent_line_span_permission_return_row_id,
        parent_line_span_candidate_row_id: parentRow.parent_line_span_candidate_row_id,
        parent_criteria_decision_row_id: parentRow.parent_criteria_decision_row_id,
        parent_resolution_return_evidence_intake_row_id: parentRow.parent_resolution_return_evidence_intake_row_id,
        parent_criterion_row_id: parentRow.parent_criterion_row_id,
        parent_decision_precondition_blocker_resolution_return_evidence_criteria_row_id: parentRow.parent_decision_precondition_blocker_resolution_return_evidence_criteria_row_id,
        parent_decision_precondition_blocker_resolution_return_row_id: parentRow.parent_decision_precondition_blocker_resolution_return_row_id,
        parent_decision_precondition_blocker_resolution_request_row_id: parentRow.parent_decision_precondition_blocker_resolution_request_row_id,
        parent_decision_precondition_blocker_row_id: parentRow.parent_decision_precondition_blocker_row_id,
        parent_decision_precondition_checklist_row_id: parentRow.parent_decision_precondition_checklist_row_id,
        parent_reviewer_scope_criteria_decision_row_id: parentRow.parent_reviewer_scope_criteria_decision_row_id,
        parent_reviewer_scope_evidence_intake_row_id: parentRow.parent_reviewer_scope_evidence_intake_row_id,
        parent_ledger_row_id: parentRow.parent_ledger_row_id,
        parent_reviewer_scope_row_id: parentRow.parent_reviewer_scope_row_id,
        parent_gap_check_row_id: parentRow.parent_gap_check_row_id,
        parent_pointer_row_id: parentRow.parent_pointer_row_id,
        packet_unit: parentRow.packet_unit,
        reviewer_role: parentRow.reviewer_role,
        source_systems_implicated: parentRow.source_systems_implicated,
        parent_criterion_type: parentRow.parent_criterion_type,
        parent_permission_evidence_criteria_decision_precondition_name: parentRow.precondition_name,
        criterion_type: parentRow.criterion_type,
        criterion_requirement: parentRow.criterion_requirement,
        required_future_evidence_class: parentRow.required_future_evidence_class,
        blocker_precondition_name: preconditionName,
        precondition_name: preconditionName,
        parent_precondition_value: false,
        blocker_reason: `precondition_${preconditionName}_is_false_in_package_130`,
        required_future_resolution: requiredFutureResolutionByPrecondition[preconditionName],
        blocker_status: 'unresolved_blank_permission_evidence_decision_precondition_blocker_row_only',
        blocker_resolved: false,
        resolution_evidence_filled: false,
        decision_fields_filled: 0,
        criteria_decision_recorded: false,
        criterion_passed: false,
        criterion_failed: false,
        evidence_value_reviewed: false,
        permission_return_verified: false,
        line_span_candidate_permission_verified: false,
        source_text_capture_permission_verified: false,
        exact_line_span_selection_allowed_after_resolution: false,
        source_text_capture_allowed_after_resolution: false,
        excerpt_selection_allowed_after_resolution: false,
        local_language_surface_allowed_after_resolution: false,
        precondition_can_be_set_true_after_resolution: false,
        decision_promotion_allowed_after_resolution: false,
        surface_gate_opened: false,
        translation_gate_opened: false,
        publication_gate_opened: false,
        pilot_gate_opened: false
      });
    }
  }
  return rows;
}

function summarizeLinkedBlockers(linked, base) {
  return {
    ...base,
    linked_permission_evidence_decision_precondition_blocker_row_ids: linked.map((row) => row.permission_evidence_decision_precondition_blocker_row_id),
    checklist_rows_required: new Set(linked.map((row) => row.parent_permission_evidence_decision_precondition_checklist_row_id)).size,
    blocker_rows_required: linked.length,
    blocker_rows_resolved: 0,
    blocker_rows_unresolved: linked.length,
    true_precondition_cells_after_resolution: 0,
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
    translated_passages: 0
  };
}

function buildPreconditionNameSummaries(blockerRows) {
  const byPrecondition = groupBy(blockerRows, (row) => row.blocker_precondition_name);
  return preconditionNames.map((preconditionName, index) => {
    const linked = byPrecondition.get(preconditionName) || [];
    return summarizeLinkedBlockers(linked, {
      permission_evidence_decision_precondition_blocker_precondition_name_summary_row_id: `ODRF-RSCOPE-LSPAN-PEVID-DPCB-PRECOND-${String(index + 1).padStart(2, '0')}`,
      blocker_precondition_name: preconditionName,
      precondition_name: preconditionName,
      required_future_resolution: requiredFutureResolutionByPrecondition[preconditionName]
    });
  });
}

function buildSummaryFromChecklistLinks(parentRows, blockerRows, idField, idPrefix, baseBuilder) {
  const blockersByChecklist = groupBy(blockerRows, (row) => row.parent_permission_evidence_decision_precondition_checklist_row_id);
  return parentRows.map((row, index) => {
    const linked = (row.linked_permission_evidence_decision_precondition_checklist_row_ids || [])
      .flatMap((id) => blockersByChecklist.get(id) || []);
    return summarizeLinkedBlockers(linked, {
      [idField]: `${idPrefix}-${String(index + 1).padStart(2, '0')}`,
      ...baseBuilder(row)
    });
  });
}

function buildReturnCriterionTypeSummaries(parent, blockerRows) {
  return buildSummaryFromChecklistLinks(
    parent.return_criterion_type_permission_evidence_decision_precondition_summary_rows,
    blockerRows,
    'permission_evidence_decision_precondition_blocker_return_criterion_type_summary_row_id',
    'ODRF-RSCOPE-LSPAN-PEVID-DPCB-CTYPE',
    (row) => ({
      parent_permission_evidence_decision_precondition_criterion_type_summary_row_id: row.permission_evidence_decision_precondition_criterion_type_summary_row_id,
      criterion_type: row.criterion_type,
      required_future_evidence_class: row.required_future_evidence_class,
      linked_permission_evidence_decision_precondition_checklist_row_ids: row.linked_permission_evidence_decision_precondition_checklist_row_ids
    })
  );
}

function buildParentCriterionTypeSummaries(parent, blockerRows) {
  return buildSummaryFromChecklistLinks(
    parent.parent_criterion_type_permission_evidence_decision_precondition_summary_rows,
    blockerRows,
    'permission_evidence_decision_precondition_blocker_parent_criterion_type_summary_row_id',
    'ODRF-RSCOPE-LSPAN-PEVID-DPCB-PTYPE',
    (row) => ({
      parent_permission_evidence_decision_precondition_parent_criterion_type_summary_row_id: row.permission_evidence_decision_precondition_parent_criterion_type_summary_row_id,
      parent_criterion_type: row.parent_criterion_type,
      linked_permission_evidence_decision_precondition_checklist_row_ids: row.linked_permission_evidence_decision_precondition_checklist_row_ids
    })
  );
}

function buildPacketUnitSummaries(parent, blockerRows) {
  return buildSummaryFromChecklistLinks(
    parent.packet_unit_permission_evidence_decision_precondition_summary_rows,
    blockerRows,
    'permission_evidence_decision_precondition_blocker_packet_unit_summary_row_id',
    'ODRF-RSCOPE-LSPAN-PEVID-DPCB-UNIT',
    (row) => ({
      parent_permission_evidence_decision_precondition_packet_unit_summary_row_id: row.permission_evidence_decision_precondition_packet_unit_summary_row_id,
      packet_unit: row.packet_unit,
      parent_ledger_row_id: row.parent_ledger_row_id,
      parent_pointer_row_id: row.parent_pointer_row_id,
      linked_permission_evidence_decision_precondition_checklist_row_ids: row.linked_permission_evidence_decision_precondition_checklist_row_ids
    })
  );
}

function buildArtifact(parent) {
  const blockerRows = buildBlockerRows(parent);
  const preconditionNameSummaries = buildPreconditionNameSummaries(blockerRows);
  const returnCriterionTypeSummaries = buildReturnCriterionTypeSummaries(parent, blockerRows);
  const parentCriterionTypeSummaries = buildParentCriterionTypeSummaries(parent, blockerRows);
  const packetUnitSummaries = buildPacketUnitSummaries(parent, blockerRows);
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template_unresolved_no_resolutions_no_true_preconditions_no_decisions_no_evidence_review_no_returns_no_permissions_no_source_text_no_excerpts_no_surfaces_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Convert every false package-130 line-span permission evidence decision-precondition cell into an explicit unresolved blocker row without resolving blockers, setting true preconditions, reviewing evidence, receiving returns, granting permissions, selecting spans, copying source text, creating excerpts, accepting surfaces, translating, publishing, or claiming pilot readiness.',
    parent_artifacts: parentArtifacts,
    blocker_ledger_boundary: {
      ledger_is: 'blank unresolved blocker ledger for false package-130 permission-evidence decision-precondition cells',
      ledger_is_not: [
        'resolved blocker ledger',
        'true precondition update',
        'evidence review result',
        'permission return',
        'permission grant',
        'source locator ledger',
        'line-span selection',
        'source text capture permission',
        'source prose cache',
        'selected excerpt',
        'surface proposal',
        'translation draft',
        'publication or pilot claim'
      ],
      allowed_now: [
        'allocate one unresolved blocker row for every false package-130 decision-precondition cell',
        'link blocker rows to parent checklist, permission-evidence decision, evidence, permission return, line-span candidate, reviewer-scope, gap-check, and pointer rows',
        'summarize unresolved blockers by blocker precondition name, return criterion type, parent criterion type, and packet unit',
        'queue substantive small-text artifacts for upload when a staging path exists'
      ],
      blocked_now: [
        'resolving blocker rows',
        'marking preconditions true',
        'recording decisions or evidence review',
        'ingesting permission returns',
        'recording line-span or source-text permissions',
        'selecting exact line spans',
        'copying source prose, examples, passages, or excerpts',
        'opening local, bridge, semi-constructed surface, translation, publication, or pilot gates'
      ]
    },
    precondition_names: preconditionNames,
    permission_evidence_decision_precondition_blocker_rows: blockerRows,
    precondition_name_permission_evidence_decision_precondition_blocker_summary_rows: preconditionNameSummaries,
    return_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows: returnCriterionTypeSummaries,
    parent_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows: parentCriterionTypeSummaries,
    packet_unit_permission_evidence_decision_precondition_blocker_summary_rows: packetUnitSummaries,
    gate_state: {
      permission_evidence_decision_precondition_blocker_rows: blockerRows.length,
      precondition_name_permission_evidence_decision_precondition_blocker_summary_rows: preconditionNameSummaries.length,
      return_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows: returnCriterionTypeSummaries.length,
      parent_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows: parentCriterionTypeSummaries.length,
      packet_unit_permission_evidence_decision_precondition_blocker_summary_rows: packetUnitSummaries.length,
      inherited_permission_evidence_decision_precondition_checklist_rows: parent.gate_state.permission_evidence_decision_precondition_checklist_rows,
      inherited_false_precondition_cells: parent.gate_state.false_precondition_cells,
      inherited_true_precondition_cells: parent.gate_state.true_precondition_cells,
      blockers_resolved: 0,
      blockers_unresolved: blockerRows.length,
      blocker_rows_resolved: 0,
      blocker_rows_remaining: blockerRows.length,
      true_precondition_cells: 0,
      false_precondition_cells: blockerRows.length,
      checklist_rows_ready: 0,
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
      request_fields_filled: 0,
      request_packets_started: 0,
      requests_dispatched: 0,
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
      permission_evidence_decision_precondition_blocker_rows_expected: 20480,
      inherited_permission_evidence_decision_precondition_checklist_rows_expected: 2560,
      inherited_false_precondition_cells_expected: 20480,
      inherited_true_precondition_cells_expected: 0,
      precondition_name_blocker_summary_rows_expected: 8,
      return_criterion_type_blocker_summary_rows_expected: 4,
      parent_criterion_type_blocker_summary_rows_expected: 8,
      packet_unit_blocker_summary_rows_expected: 10,
      zero_gate_assertions: [
        'blockers_resolved',
        'blocker_rows_resolved',
        'true_precondition_cells',
        'checklist_rows_ready',
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
        'request_fields_filled',
        'request_packets_started',
        'requests_dispatched',
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
      'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_LINE_SPAN_PERMISSION_EVIDENCE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_REQUEST_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SOURCE_TEXT_CAPTURE_POLICY_RETURN_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_<timestamp>'
    ],
    decision: 'Package 131 allocates unresolved blocker rows for every package-130 false line-span permission evidence decision-precondition cell. It does not resolve blockers, set true preconditions, review evidence, receive returns, record permissions, select exact spans, copy source text, create excerpts, accept surfaces, draft translations, or claim readiness.'
  };
}

function buildArtifactMd(artifact) {
  const sampleRows = artifact.permission_evidence_decision_precondition_blocker_rows.slice(0, 20).map((row) => `| \`${row.permission_evidence_decision_precondition_blocker_row_id}\` | \`${row.parent_permission_evidence_decision_precondition_checklist_row_id}\` | ${row.packet_unit} | ${row.blocker_precondition_name} | ${row.criterion_type} | ${row.blocker_status} |`).join('\n');
  const preconditionRows = artifact.precondition_name_permission_evidence_decision_precondition_blocker_summary_rows.map((row) => `| ${row.blocker_precondition_name} | \`${row.blocker_rows_required}\` | \`${row.blocker_rows_resolved}\` | \`${row.blocker_rows_unresolved}\` |`).join('\n');
  const typeRows = artifact.return_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows.map((row) => `| ${row.criterion_type} | \`${row.blocker_rows_required}\` | \`${row.blocker_rows_resolved}\` | \`${row.blocker_rows_unresolved}\` |`).join('\n');
  const parentTypeRows = artifact.parent_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows.map((row) => `| ${row.parent_criterion_type} | \`${row.blocker_rows_required}\` | \`${row.blocker_rows_resolved}\` | \`${row.blocker_rows_unresolved}\` |`).join('\n');
  const unitRows = artifact.packet_unit_permission_evidence_decision_precondition_blocker_summary_rows.map((row) => `| ${row.packet_unit} | \`${row.blocker_rows_required}\` | \`${row.blocker_rows_resolved}\` | \`${row.blocker_rows_unresolved}\` |`).join('\n');
  const gateRows = Object.entries(artifact.gate_state).map(([key, value]) => `| ${key} | \`${Array.isArray(value) ? value.length : value}\` |`).join('\n');
  return `# OLP/DMOI Relation-Function Reviewer Scope Line-Span Permission Evidence Decision Precondition Blocker Ledger Template

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Blocker Rows

Showing first 20 of \`${artifact.permission_evidence_decision_precondition_blocker_rows.length}\` unresolved blocker rows.

| Blocker row | Parent checklist row | Packet unit | Blocker precondition | Criterion type | Status |
| --- | --- | --- | --- | --- | --- |
${sampleRows}

## Precondition Summary

| Blocker precondition | Required blockers | Resolved | Unresolved |
| --- | ---: | ---: | ---: |
${preconditionRows}

## Return Criterion Type Summary

| Criterion type | Required blockers | Resolved | Unresolved |
| --- | ---: | ---: | ---: |
${typeRows}

## Parent Criterion Type Summary

| Parent criterion type | Required blockers | Resolved | Unresolved |
| --- | ---: | ---: | ---: |
${parentTypeRows}

## Packet Unit Summary

| Packet unit | Required blockers | Resolved | Unresolved |
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
    'permission_evidence_decision_precondition_blocker_row_id',
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
    'parent_permission_evidence_criteria_decision_precondition_name',
    'criterion_type',
    'required_future_evidence_class',
    'blocker_precondition_name',
    'parent_precondition_value',
    'blocker_status',
    'blocker_resolved',
    'resolution_evidence_filled',
    'required_future_resolution',
    'source_text_capture_allowed_after_resolution',
    'excerpt_selection_allowed_after_resolution',
    'surface_gate_opened',
    'translation_gate_opened'
  ];
  const rows = artifact.permission_evidence_decision_precondition_blocker_rows.map((row) => columns.map((column) => csvCell(row[column])).join(','));
  return `${columns.join(',')}\n${rows.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    source_artifact: artifact.artifact_id,
    package_order: packageOrder,
    status: 'pointer_only_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-131 OLP/DMOI reviewer-scope line-span permission evidence decision-precondition blocker-ledger continuation while preserving no-resolution/no-true-precondition/no-decision/no-evidence-review/no-return/no-permission/no-source-text/no-excerpt/no-translation boundaries.',
    counts: {
      permission_evidence_decision_precondition_blocker_rows: g.permission_evidence_decision_precondition_blocker_rows,
      inherited_permission_evidence_decision_precondition_checklist_rows: g.inherited_permission_evidence_decision_precondition_checklist_rows,
      inherited_false_precondition_cells: g.inherited_false_precondition_cells,
      inherited_true_precondition_cells: g.inherited_true_precondition_cells,
      blockers_resolved: g.blockers_resolved,
      blockers_unresolved: g.blockers_unresolved,
      precondition_name_permission_evidence_decision_precondition_blocker_summary_rows: g.precondition_name_permission_evidence_decision_precondition_blocker_summary_rows,
      return_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows: g.return_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows,
      parent_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows: g.parent_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows,
      packet_unit_permission_evidence_decision_precondition_blocker_summary_rows: g.packet_unit_permission_evidence_decision_precondition_blocker_summary_rows
    },
    zero_gates: {
      true_precondition_cells: 0,
      blocker_rows_resolved: 0,
      decisions_recorded: 0,
      evidence_values_reviewed: 0,
      permission_returns_received: 0,
      line_span_candidate_permissions_recorded: 0,
      source_text_capture_permissions_recorded: 0,
      exact_line_spans_selected: 0,
      source_passages_selected: 0,
      source_prose_copied: 0,
      excerpts_selected: 0,
      surfaces_filled: 0,
      translated_passages: 0,
      readiness_claims: 0
    },
    upload_intent: 'Queue the package-131 JSON/MD/CSV/checksum and this note for the existing Noether upload path as substantive coordination material; do not defer because of mobile-plan or bandwidth wording.',
    no_remote_action_by_this_note: true,
    message_template: `Package 131 added ${artifactId}: unresolved OLP/DMOI reviewer-scope line-span permission evidence decision-precondition blocker ledger. Counts: ${g.permission_evidence_decision_precondition_blocker_rows} unresolved blocker rows from ${g.inherited_permission_evidence_decision_precondition_checklist_rows} checklist rows and ${g.inherited_false_precondition_cells} false precondition cells; 0 blockers resolved, 0 true preconditions, 0 decisions, 0 evidence reviewed, 0 returns, 0 permissions, 0 source text/excerpts, 0 surfaces, 0 translations, 0 readiness.`
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 131 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 131 creates an OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker ledger template with \`${g.permission_evidence_decision_precondition_blocker_rows}\` unresolved blocker rows from \`${g.inherited_permission_evidence_decision_precondition_checklist_rows}\` checklist rows and \`${g.inherited_false_precondition_cells}\` inherited false precondition cells.

Zero gates: \`0\` blockers resolved, \`0\` true preconditions, \`0\` filled decision fields, \`0\` criteria decisions, \`0\` passed/failed criteria, \`0\` evidence values reviewed, \`0\` permission returns, \`0\` line-span permissions, \`0\` source-text capture permissions, \`0\` exact line spans, \`0\` source passages, \`0\` source prose, \`0\` examples, \`0\` excerpts, \`0\` selected-excerpt attribution notices, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Upload intent: ${note.upload_intent}

Boundary: line-span permission evidence decision-precondition blocker ledger template only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, translation, publication, pilot, legal-advice, or remote-state claim.
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
      role: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template_support',
      artifact: artifactId,
      current_use: '20,480 unresolved line-span permission evidence decision-precondition blocker rows from package-130 false precondition cells; 8 precondition-name summaries; 4 return-criterion-type summaries; 8 parent-criterion-type summaries; 10 packet-unit summaries; 0 blockers resolved, 0 true preconditions, 0 decisions, 0 evidence reviewed, 0 returns, 0 permissions, 0 source prose, 0 excerpts, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  packageIndex.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_rows: artifact.gate_state.permission_evidence_decision_precondition_blocker_rows,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blockers_resolved: 0,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blockers_unresolved: artifact.gate_state.blockers_unresolved,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_false_cells: artifact.gate_state.false_precondition_cells,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_true_cells: 0,
    olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decisions_recorded: 0,
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
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_blocker_resolution_request_template_or_source_text_capture_policy_return_ledger_blank_only_no_source_text_no_surfaces_no_translation`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker ledger template',
    route: artifactId,
    license_status_to_recheck: 'line_span_permission_evidence_decision_precondition_blocker_ledger_only_no_resolutions_no_true_preconditions_no_decisions_no_evidence_review_no_returns_no_permissions_no_source_text_no_surfaces_no_translation',
    best_translation_use: 'future reviewer-scope permission-evidence blocker resolution planning before source-text capture, excerpt, local/bridge surface, and translation-owner gates',
    candidate_lanes: ['semi_constructed_relation_function_source_request_lane', 'open_source_candidate_catalog', 'reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template', 'review_only_construction_scaffold'],
    priority: 1,
    status: 'reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template_no_resolutions_no_true_preconditions_no_decisions_no_evidence_review_no_returns_no_permissions_no_source_text_no_excerpts_no_surfaces_no_translation_no_pilot',
    gate_state: {
      permission_evidence_decision_precondition_blocker_rows: artifact.gate_state.permission_evidence_decision_precondition_blocker_rows,
      blockers_resolved: 0,
      blockers_unresolved: artifact.gate_state.blockers_unresolved,
      true_precondition_cells: 0,
      criteria_decisions_recorded: 0,
      evidence_values_reviewed: 0,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template: ${artifactId}_20480_unresolved_blockers_0_resolved_0_true_0_decisions_0_evidence_review_0_returns_0_permissions_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_rows: artifact.gate_state.permission_evidence_decision_precondition_blocker_rows,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blockers_resolved: 0,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blockers_unresolved: artifact.gate_state.blockers_unresolved,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_true_cells: 0,
    current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decisions_recorded: 0,
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
  program.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template: ${artifactId}_unresolved_only_no_true_preconditions_no_decisions_no_evidence_review_no_returns_no_permissions_no_source_text_no_excerpts_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 20,480 unresolved line-span permission evidence decision-precondition blocker rows from package-130 false precondition cells; 8 precondition-name summaries; 4 return-criterion-type summaries; 8 parent-criterion-type summaries; 10 packet-unit summaries; 0 blockers resolved, 0 true preconditions, 0 criteria decisions, 0 evidence reviewed, 0 permission returns received, 0 line-span permissions, 0 source-text permissions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be queued for upload when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker ledger template; 20,480 unresolved blocker rows from package-130 false precondition cells, 0 resolved blockers, 0 true preconditions, 0 decisions, 0 evidence reviewed, 0 returns, 0 permissions, 0 exact spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 131: OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker ledger template after package 130. It records 20,480 unresolved blocker rows from 20,480 false precondition cells while keeping 0 resolved blockers, 0 true preconditions, 0 criteria decisions, 0 evidence reviewed, 0 permission returns received, 0 line-span permissions, 0 source-text capture permissions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker ledger template | ${artifactId} | Permission evidence decision-precondition blocker ledger; 20,480 unresolved blocker rows, 0 resolved blockers, 0 true preconditions, 0 decisions, 0 evidence reviewed, 0 returns, 0 permissions, 0 source prose, 0 excerpts, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template_artifact: \`${artifactId}\` (20,480 unresolved blocker rows; 0 resolved; 0 true preconditions; 0 decisions; 0 evidence reviewed; 0 returns; 0 permissions; 0 source prose; 0 excerpts; no surfaces, no translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template: \`${artifactId}\`; unresolved blocker ledger only, no true preconditions, decisions, evidence review, returns, permissions, source text, excerpts, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI reviewer-scope line-span permission evidence decision-precondition blocker ledger template; unresolved blocker rows are not true preconditions, evidence review, permission returns, source-text permission, exact span selection, source text, excerpts, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_reviewer_scope_line_span_permission_evidence_decision_precondition_blocker_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package131_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package131_coordination_note' },
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
  upload.obj.package131_upload_queue_update = {
    captured_utc: '2026-07-03T03:02:00Z',
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
  const step = 'Stage package 131 OLP/DMOI relation-function reviewer-scope line-span permission evidence decision-precondition blocker-ledger artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.permission_evidence_decision_precondition_blocker_rows.length !== 20480) failures.push('blocker_rows_not_20480');
  if (artifact.precondition_name_permission_evidence_decision_precondition_blocker_summary_rows.length !== 8) failures.push('precondition_name_summary_rows_not_8');
  if (artifact.return_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows.length !== 4) failures.push('return_criterion_type_summary_rows_not_4');
  if (artifact.parent_criterion_type_permission_evidence_decision_precondition_blocker_summary_rows.length !== 8) failures.push('parent_criterion_type_summary_rows_not_8');
  if (artifact.packet_unit_permission_evidence_decision_precondition_blocker_summary_rows.length !== 10) failures.push('packet_unit_summary_rows_not_10');
  if (g.inherited_permission_evidence_decision_precondition_checklist_rows !== 2560) failures.push(`inherited_checklist_rows_not_2560_${g.inherited_permission_evidence_decision_precondition_checklist_rows}`);
  if (g.inherited_false_precondition_cells !== 20480) failures.push(`inherited_false_cells_not_20480_${g.inherited_false_precondition_cells}`);
  if (g.inherited_true_precondition_cells !== 0) failures.push(`inherited_true_cells_not_0_${g.inherited_true_precondition_cells}`);
  if (g.blockers_unresolved !== 20480 || g.blocker_rows_remaining !== 20480 || g.false_precondition_cells !== 20480) failures.push('unresolved_or_false_cell_count_not_20480');
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.permission_evidence_decision_precondition_blocker_rows) {
    if (row.parent_precondition_value !== false ||
      row.blocker_resolved ||
      row.resolution_evidence_filled ||
      row.decision_fields_filled !== 0 ||
      row.criteria_decision_recorded ||
      row.criterion_passed ||
      row.criterion_failed ||
      row.evidence_value_reviewed ||
      row.permission_return_verified ||
      row.line_span_candidate_permission_verified ||
      row.source_text_capture_permission_verified ||
      row.exact_line_span_selection_allowed_after_resolution ||
      row.source_text_capture_allowed_after_resolution ||
      row.excerpt_selection_allowed_after_resolution ||
      row.local_language_surface_allowed_after_resolution ||
      row.precondition_can_be_set_true_after_resolution ||
      row.decision_promotion_allowed_after_resolution ||
      row.surface_gate_opened ||
      row.translation_gate_opened ||
      row.publication_gate_opened ||
      row.pilot_gate_opened) {
      failures.push(`unsafe_blocker_row_${row.permission_evidence_decision_precondition_blocker_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  return failures;
}

const parent = (await readJson(parentPreconditionChecklist)).obj;
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
  blocker_rows: artifact.gate_state.permission_evidence_decision_precondition_blocker_rows,
  inherited_checklist_rows: artifact.gate_state.inherited_permission_evidence_decision_precondition_checklist_rows,
  inherited_false_precondition_cells: artifact.gate_state.inherited_false_precondition_cells,
  inherited_true_precondition_cells: artifact.gate_state.inherited_true_precondition_cells,
  blockers_resolved: artifact.gate_state.blockers_resolved,
  blockers_unresolved: artifact.gate_state.blockers_unresolved,
  true_precondition_cells: artifact.gate_state.true_precondition_cells,
  criteria_decisions_recorded: artifact.gate_state.criteria_decisions_recorded,
  evidence_values_reviewed: artifact.gate_state.evidence_values_reviewed,
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
