import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_CRITERIA_RUBRIC_20260703T010000Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_CRITERIA_RUBRIC_NOTE_20260703T010100Z';
const generatedUtc = '2026-07-03T01:00:00Z';
const noteGeneratedUtc = '2026-07-03T01:01:00Z';
const packageOrder = 123;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-REVIEWER-SCOPE-DECISION-PRECONDITION-BLOCKER-RESOLUTION-RETURN-EVIDENCE-CRITERIA-RUBRIC-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentReturnLedger = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_LEDGER_TEMPLATE_20260703T004500Z';
const parentArtifacts = [
  parentReturnLedger,
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_REQUEST_TEMPLATE_20260703T003000Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_DECISION_PRECONDITION_BLOCKER_LEDGER_TEMPLATE_20260703T001500Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_DECISION_PRECONDITION_CHECKLIST_TEMPLATE_20260703T000000Z'
];

const criteriaSpecs = [
  {
    criterion_type: 'dated_non_personal_return_identity',
    requirement: 'Future evidence must identify a dated non-personal return route, reviewer or owner role, and the exact package-122 return row; personal contact details are not evidence.',
    evidence_class: 'dated_non_personal_return_metadata'
  },
  {
    criterion_type: 'request_return_scope_match',
    requirement: 'Future evidence must explicitly match the package-121 request row, package-120 blocker row, package-119 checklist row, packet unit, criterion type, and precondition name; broad route or language-family evidence does not count.',
    evidence_class: 'row_linkage_and_scope_match_metadata'
  },
  {
    criterion_type: 'resolution_evidence_pointer_metadata_only',
    requirement: 'Future resolution-evidence pointers must be non-personal metadata only and must not copy source prose, definitions, examples, corpus passages, service-result bodies, tokens, excerpts, or personal details.',
    evidence_class: 'resolution_evidence_pointer_metadata_only'
  },
  {
    criterion_type: 'source_text_and_downstream_gate_limits_confirmed',
    requirement: 'Future evidence must keep source text, exact line spans, local/bridge/semi-constructed surfaces, translation, publication, and pilot gates separate and closed unless later artifacts independently open them.',
    evidence_class: 'source_text_surface_translation_gate_limit_metadata'
  }
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

function groupBy(rows, keyFn) {
  const map = new Map();
  for (const row of rows) {
    const key = keyFn(row);
    if (!map.has(key)) map.set(key, []);
    map.get(key).push(row);
  }
  return map;
}

function buildCriteriaGroups(parent) {
  return parent.decision_precondition_blocker_resolution_return_rows.map((row, index) => ({
    decision_precondition_blocker_resolution_return_evidence_criteria_row_id: `ODRF-RSCOPE-DPCBRT-ECR-${String(index + 1).padStart(4, '0')}`,
    parent_decision_precondition_blocker_resolution_return_row_id: row.decision_precondition_blocker_resolution_return_row_id,
    parent_decision_precondition_blocker_resolution_request_row_id: row.parent_decision_precondition_blocker_resolution_request_row_id,
    parent_decision_precondition_blocker_row_id: row.parent_decision_precondition_blocker_row_id,
    parent_decision_precondition_checklist_row_id: row.parent_decision_precondition_checklist_row_id,
    parent_criteria_decision_row_id: row.parent_criteria_decision_row_id,
    parent_evidence_intake_row_id: row.parent_evidence_intake_row_id,
    parent_criterion_row_id: row.parent_criterion_row_id,
    parent_return_evidence_criteria_row_id: row.parent_return_evidence_criteria_row_id,
    parent_ledger_row_id: row.parent_ledger_row_id,
    parent_reviewer_scope_row_id: row.parent_reviewer_scope_row_id,
    parent_gap_check_row_id: row.parent_gap_check_row_id,
    parent_pointer_row_id: row.parent_pointer_row_id,
    packet_unit: row.packet_unit,
    reviewer_role: row.reviewer_role,
    source_systems_implicated: row.source_systems_implicated,
    criterion_type: row.criterion_type,
    required_future_evidence_class: row.required_future_evidence_class,
    precondition_name: row.precondition_name,
    criteria_types_required: criteriaSpecs.map((spec) => spec.criterion_type),
    linked_criterion_row_ids: criteriaSpecs.map((_, criterionIndex) => `ODRF-RSCOPE-DPCBRT-ECR-CRIT-${String(index * criteriaSpecs.length + criterionIndex + 1).padStart(5, '0')}`),
    criteria_rows_required: criteriaSpecs.length,
    criteria_rows_passed: 0,
    criteria_rows_failed: 0,
    criteria_rows_unfilled: criteriaSpecs.length,
    return_received: false,
    return_evidence_reviewed: false,
    blocker_resolution_allowed_now: false,
    true_precondition_update_allowed_now: false,
    source_system_decision_allowed_now: false,
    scope_decision_allowed_now: false,
    line_span_candidate_register_allowed_now: false,
    source_text_capture_allowed_now: false,
    surface_gate_opened: false,
    translation_gate_opened: false,
    return_evidence_criteria_status: 'blank_resolution_return_evidence_criteria_only'
  }));
}

function buildCriterionRows(groups) {
  return groups.flatMap((group, groupIndex) => criteriaSpecs.map((spec, specIndex) => ({
    criterion_row_id: `ODRF-RSCOPE-DPCBRT-ECR-CRIT-${String(groupIndex * criteriaSpecs.length + specIndex + 1).padStart(5, '0')}`,
    parent_decision_precondition_blocker_resolution_return_evidence_criteria_row_id: group.decision_precondition_blocker_resolution_return_evidence_criteria_row_id,
    parent_decision_precondition_blocker_resolution_return_row_id: group.parent_decision_precondition_blocker_resolution_return_row_id,
    parent_decision_precondition_blocker_resolution_request_row_id: group.parent_decision_precondition_blocker_resolution_request_row_id,
    parent_decision_precondition_blocker_row_id: group.parent_decision_precondition_blocker_row_id,
    parent_decision_precondition_checklist_row_id: group.parent_decision_precondition_checklist_row_id,
    parent_criteria_decision_row_id: group.parent_criteria_decision_row_id,
    parent_evidence_intake_row_id: group.parent_evidence_intake_row_id,
    parent_criterion_row_id: group.parent_criterion_row_id,
    parent_ledger_row_id: group.parent_ledger_row_id,
    parent_reviewer_scope_row_id: group.parent_reviewer_scope_row_id,
    parent_gap_check_row_id: group.parent_gap_check_row_id,
    parent_pointer_row_id: group.parent_pointer_row_id,
    packet_unit: group.packet_unit,
    reviewer_role: group.reviewer_role,
    source_systems_implicated: group.source_systems_implicated,
    parent_criterion_type: group.criterion_type,
    precondition_name: group.precondition_name,
    criterion_type: spec.criterion_type,
    criterion_requirement: spec.requirement,
    required_future_evidence_class: spec.evidence_class,
    evidence_value: null,
    evidence_source_pointer: null,
    evidence_date: null,
    criterion_passed: false,
    criterion_failed: false,
    criterion_unfilled: true,
    blocker_resolution_allowed_after_pass: false,
    true_precondition_update_allowed_after_pass: false,
    source_system_decision_allowed_after_pass: false,
    scope_decision_allowed_after_pass: false,
    line_span_candidate_register_allowed_after_pass: false,
    source_text_capture_allowed_after_pass: false,
    surface_gate_opened: false,
    translation_gate_opened: false
  })));
}

function summarizeLinkedCriteria(linked, base) {
  return {
    ...base,
    return_rows_required: new Set(linked.map((row) => row.parent_decision_precondition_blocker_resolution_return_row_id)).size,
    criteria_rows_required: linked.length,
    criteria_rows_passed: 0,
    criteria_rows_failed: 0,
    criteria_rows_unfilled: linked.length,
    returns_received: 0,
    evidence_values_filled: 0,
    evidence_source_pointers_filled: 0,
    blockers_resolved: 0,
    true_precondition_cells: 0,
    source_system_decisions_recorded: 0,
    line_span_candidate_permissions_recorded: 0,
    source_text_capture_permissions_recorded: 0,
    surface_gate_opened: false,
    translation_gate_opened: false
  };
}

function buildPreconditionNameSummaries(parent, criterionRows) {
  const criteriaByReturn = groupBy(criterionRows, (row) => row.parent_decision_precondition_blocker_resolution_return_row_id);
  return parent.precondition_name_resolution_return_summary_rows.map((row, index) => {
    const linked = (row.linked_decision_precondition_blocker_resolution_return_row_ids || []).flatMap((id) => criteriaByReturn.get(id) || []);
    return summarizeLinkedCriteria(linked, {
      decision_precondition_blocker_resolution_return_evidence_criteria_precondition_name_summary_row_id: `ODRF-RSCOPE-DPCBRT-ECR-PRECOND-${String(index + 1).padStart(2, '0')}`,
      parent_decision_precondition_blocker_resolution_return_precondition_name_summary_row_id: row.decision_precondition_blocker_resolution_return_precondition_name_summary_row_id,
      precondition_name: row.precondition_name,
      linked_criterion_row_ids: linked.map((criterion) => criterion.criterion_row_id),
      parent_checklist_row_count: row.parent_checklist_row_count
    });
  });
}

function buildReturnCriterionTypeSummaries(criterionRows) {
  return criteriaSpecs.map((spec, index) => {
    const linked = criterionRows.filter((row) => row.criterion_type === spec.criterion_type);
    return summarizeLinkedCriteria(linked, {
      decision_precondition_blocker_resolution_return_evidence_criteria_type_summary_row_id: `ODRF-RSCOPE-DPCBRT-ECR-CTYPE-${String(index + 1).padStart(2, '0')}`,
      criterion_type: spec.criterion_type,
      required_future_evidence_class: spec.evidence_class,
      linked_criterion_row_ids: linked.map((criterion) => criterion.criterion_row_id)
    });
  });
}

function buildParentCriterionTypeSummaries(parent, criterionRows) {
  const criteriaByReturn = groupBy(criterionRows, (row) => row.parent_decision_precondition_blocker_resolution_return_row_id);
  return parent.criterion_type_resolution_return_summary_rows.map((row, index) => {
    const linked = (row.linked_decision_precondition_blocker_resolution_return_row_ids || []).flatMap((id) => criteriaByReturn.get(id) || []);
    return summarizeLinkedCriteria(linked, {
      decision_precondition_blocker_resolution_return_evidence_parent_criterion_type_summary_row_id: `ODRF-RSCOPE-DPCBRT-ECR-PTYPE-${String(index + 1).padStart(2, '0')}`,
      parent_decision_precondition_blocker_resolution_return_criterion_type_summary_row_id: row.decision_precondition_blocker_resolution_return_criterion_type_summary_row_id,
      parent_criterion_type: row.criterion_type,
      linked_criterion_row_ids: linked.map((criterion) => criterion.criterion_row_id),
      criteria_rows_unfilled_from_parent: row.criteria_rows_unfilled
    });
  });
}

function buildPacketUnitSummaries(parent, criterionRows) {
  const criteriaByReturn = groupBy(criterionRows, (row) => row.parent_decision_precondition_blocker_resolution_return_row_id);
  return parent.packet_unit_resolution_return_summary_rows.map((row, index) => {
    const linked = (row.linked_decision_precondition_blocker_resolution_return_row_ids || []).flatMap((id) => criteriaByReturn.get(id) || []);
    return summarizeLinkedCriteria(linked, {
      decision_precondition_blocker_resolution_return_evidence_criteria_packet_unit_summary_row_id: `ODRF-RSCOPE-DPCBRT-ECR-UNIT-${String(index + 1).padStart(2, '0')}`,
      parent_decision_precondition_blocker_resolution_return_packet_unit_summary_row_id: row.decision_precondition_blocker_resolution_return_packet_unit_summary_row_id,
      packet_unit: row.packet_unit,
      parent_ledger_row_id: row.parent_ledger_row_id,
      parent_pointer_row_id: row.parent_pointer_row_id,
      linked_criterion_row_ids: linked.map((criterion) => criterion.criterion_row_id),
      criteria_rows_unfilled_from_parent: row.criteria_rows_unfilled
    });
  });
}

function buildArtifact(parent) {
  const groups = buildCriteriaGroups(parent);
  const criterionRows = buildCriterionRows(groups);
  const preconditionNameSummaries = buildPreconditionNameSummaries(parent, criterionRows);
  const returnCriterionTypeSummaries = buildReturnCriterionTypeSummaries(criterionRows);
  const parentCriterionTypeSummaries = buildParentCriterionTypeSummaries(parent, criterionRows);
  const packetUnitSummaries = buildPacketUnitSummaries(parent, criterionRows);
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric_blank_no_evidence_no_returns_no_resolutions_no_source_text_no_surfaces_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Define blank evidence criteria that future package-122 resolution-return rows must satisfy before any blocker can be resolved, any precondition can be set true, or any source-system, line-span, source-text, surface, translation, publication, or pilot gate can be considered.',
    parent_artifacts: parentArtifacts,
    criteria_boundary: {
      rubric_is: 'blank evidence-criteria rubric for future review of package-122 resolution-return rows',
      rubric_is_not: [
        'received return',
        'filled evidence value',
        'reviewer decision',
        'blocker resolution',
        'true precondition update',
        'source-system decision',
        'scope decision',
        'line-span register',
        'source text or excerpt',
        'surface proposal',
        'translation draft',
        'publication or pilot claim'
      ],
      allowed_now: [
        'state criterion requirements',
        'link criteria to package-122 return rows',
        'preserve metadata-only evidence and downstream-gate guardrails',
        'queue substantive small-text artifacts for upload when a staging path exists'
      ],
      blocked_now: [
        'filling evidence values or source pointers',
        'passing or failing criteria',
        'counting received returns',
        'resolving blockers',
        'setting preconditions true',
        'opening source text, surface, translation, publication, or readiness gates'
      ]
    },
    criteria_specs: criteriaSpecs,
    decision_precondition_blocker_resolution_return_evidence_criteria_rows: groups,
    criterion_rows: criterionRows,
    precondition_name_resolution_return_evidence_criteria_summary_rows: preconditionNameSummaries,
    return_criterion_type_summary_rows: returnCriterionTypeSummaries,
    parent_criterion_type_resolution_return_evidence_criteria_summary_rows: parentCriterionTypeSummaries,
    packet_unit_resolution_return_evidence_criteria_summary_rows: packetUnitSummaries,
    gate_state: {
      decision_precondition_blocker_resolution_return_evidence_criteria_rows: groups.length,
      criterion_rows: criterionRows.length,
      precondition_name_resolution_return_evidence_criteria_summary_rows: preconditionNameSummaries.length,
      return_criterion_type_summary_rows: returnCriterionTypeSummaries.length,
      parent_criterion_type_resolution_return_evidence_criteria_summary_rows: parentCriterionTypeSummaries.length,
      packet_unit_resolution_return_evidence_criteria_summary_rows: packetUnitSummaries.length,
      criteria_types_per_return_row: criteriaSpecs.length,
      inherited_decision_precondition_blocker_resolution_return_rows: parent.gate_state.decision_precondition_blocker_resolution_return_rows,
      inherited_blank_resolution_return_field_cells: parent.gate_state.blank_resolution_return_field_cells_allocated,
      inherited_blockers_unresolved: parent.gate_state.blockers_unresolved,
      criteria_rows_passed: 0,
      criteria_rows_failed: 0,
      criteria_rows_unfilled: criterionRows.length,
      evidence_values_reviewed: 0,
      evidence_values_filled: 0,
      evidence_source_pointers_filled: 0,
      returns_received: 0,
      returns_ingested: 0,
      return_fields_filled: 0,
      request_fields_filled: 0,
      request_packets_started: 0,
      requests_dispatched: 0,
      blockers_resolved: 0,
      blockers_unresolved: groups.length,
      blocker_rows_resolved: 0,
      blocker_rows_remaining: groups.length,
      true_precondition_cells: 0,
      true_precondition_updates_allowed: 0,
      false_precondition_cells: groups.length,
      decision_fields_filled: 0,
      criteria_decisions_recorded: 0,
      source_system_decisions_recorded: 0,
      scope_decisions_recorded: 0,
      route_scope_notes_recorded: 0,
      line_span_candidate_permissions_recorded: 0,
      source_text_capture_permissions_recorded: 0,
      local_register_review_requirements_recorded: 0,
      bridge_surface_review_requirements_recorded: 0,
      translation_owner_review_requirements_recorded: 0,
      rows_promoted: 0,
      exact_line_spans_selected: 0,
      source_prose_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      excerpts_selected: 0,
      selected_excerpt_attribution_notices_filled: 0,
      local_language_surfaces_filled: 0,
      bridge_surfaces_accepted: 0,
      semi_constructed_surfaces_accepted: 0,
      translated_passages: 0,
      publication_ready: false,
      translation_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      package_order_expected: packageOrder,
      return_evidence_criteria_rows_expected: 640,
      criterion_rows_expected: 2560,
      criteria_types_per_return_row_expected: criteriaSpecs.length,
      precondition_name_summary_rows_expected: 8,
      return_criterion_type_summary_rows_expected: 4,
      parent_criterion_type_summary_rows_expected: 8,
      packet_unit_summary_rows_expected: 10,
      zero_gate_assertions: [
        'criteria_rows_passed',
        'criteria_rows_failed',
        'evidence_values_reviewed',
        'evidence_values_filled',
        'evidence_source_pointers_filled',
        'returns_received',
        'returns_ingested',
        'return_fields_filled',
        'request_fields_filled',
        'request_packets_started',
        'requests_dispatched',
        'blockers_resolved',
        'blocker_rows_resolved',
        'true_precondition_cells',
        'true_precondition_updates_allowed',
        'decision_fields_filled',
        'criteria_decisions_recorded',
        'source_system_decisions_recorded',
        'scope_decisions_recorded',
        'route_scope_notes_recorded',
        'line_span_candidate_permissions_recorded',
        'source_text_capture_permissions_recorded',
        'local_register_review_requirements_recorded',
        'bridge_surface_review_requirements_recorded',
        'translation_owner_review_requirements_recorded',
        'rows_promoted',
        'exact_line_spans_selected',
        'source_prose_copied',
        'source_examples_copied',
        'source_passages_selected',
        'excerpts_selected',
        'selected_excerpt_attribution_notices_filled',
        'local_language_surfaces_filled',
        'bridge_surfaces_accepted',
        'semi_constructed_surfaces_accepted',
        'translated_passages'
      ]
    },
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_DECISION_PRECONDITION_BLOCKER_RESOLUTION_RETURN_EVIDENCE_INTAKE_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_EXACT_LINE_SPAN_CANDIDATE_REGISTER_BLANK_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_<timestamp>'
    ],
    decision: 'Package 123 defines blank evidence criteria for package-122 return rows. It does not fill evidence, receive returns, pass criteria, resolve blockers, set true preconditions, select exact line spans, copy source text, accept surfaces, draft translations, or claim readiness.'
  };
}

function buildArtifactMd(artifact) {
  const sampleRows = artifact.criterion_rows.slice(0, 20).map((row) => `| \`${row.criterion_row_id}\` | \`${row.parent_decision_precondition_blocker_resolution_return_row_id}\` | ${row.packet_unit} | ${row.precondition_name} | ${row.criterion_type} | \`${row.criterion_unfilled}\` |`).join('\n');
  const preconditionRows = artifact.precondition_name_resolution_return_evidence_criteria_summary_rows.map((row) => `| ${row.precondition_name} | \`${row.return_rows_required}\` | \`${row.criteria_rows_required}\` | \`${row.criteria_rows_unfilled}\` |`).join('\n');
  const typeRows = artifact.return_criterion_type_summary_rows.map((row) => `| ${row.criterion_type} | ${row.required_future_evidence_class} | \`${row.criteria_rows_required}\` | \`${row.criteria_rows_unfilled}\` |`).join('\n');
  const unitRows = artifact.packet_unit_resolution_return_evidence_criteria_summary_rows.map((row) => `| ${row.packet_unit} | \`${row.return_rows_required}\` | \`${row.criteria_rows_required}\` | \`${row.criteria_rows_unfilled}\` |`).join('\n');
  const gateRows = Object.entries(artifact.gate_state).map(([key, value]) => `| ${key} | \`${Array.isArray(value) ? value.length : value}\` |`).join('\n');
  return `# OLP/DMOI Relation-Function Reviewer Scope Decision Precondition Blocker Resolution Return Evidence Criteria Rubric

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Criterion Rows

Showing first 20 of \`${artifact.criterion_rows.length}\` blank criterion rows.

| Criterion row | Parent return row | Packet unit | Precondition | Criterion type | Unfilled |
| --- | --- | --- | --- | --- | --- |
${sampleRows}

## Precondition Summary

| Precondition | Return rows | Criterion rows | Unfilled |
| --- | ---: | ---: | ---: |
${preconditionRows}

## Return Criterion Type Summary

| Criterion type | Evidence class | Criterion rows | Unfilled |
| --- | --- | ---: | ---: |
${typeRows}

## Packet Unit Summary

| Packet unit | Return rows | Criterion rows | Unfilled |
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
    'criterion_row_id',
    'parent_decision_precondition_blocker_resolution_return_evidence_criteria_row_id',
    'parent_decision_precondition_blocker_resolution_return_row_id',
    'parent_decision_precondition_blocker_resolution_request_row_id',
    'parent_decision_precondition_blocker_row_id',
    'parent_decision_precondition_checklist_row_id',
    'parent_criteria_decision_row_id',
    'parent_evidence_intake_row_id',
    'parent_criterion_row_id',
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
    'evidence_value',
    'evidence_source_pointer',
    'evidence_date',
    'criterion_passed',
    'criterion_failed',
    'criterion_unfilled',
    'source_text_capture_allowed_after_pass',
    'surface_gate_opened',
    'translation_gate_opened'
  ];
  const rows = artifact.criterion_rows.map((row) => columns.map((column) => csvCell(row[column])).join(','));
  return `${columns.join(',')}\n${rows.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    source_artifact: artifact.artifact_id,
    package_order: packageOrder,
    status: 'pointer_only_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-123 OLP/DMOI reviewer-scope decision-precondition blocker resolution-return evidence criteria rubric continuation while preserving no-evidence/no-return/no-resolution/no-excerpt/no-translation boundaries.',
    counts: {
      decision_precondition_blocker_resolution_return_evidence_criteria_rows: g.decision_precondition_blocker_resolution_return_evidence_criteria_rows,
      criterion_rows: g.criterion_rows,
      criteria_types_per_return_row: g.criteria_types_per_return_row,
      criteria_rows_unfilled: g.criteria_rows_unfilled,
      precondition_name_resolution_return_evidence_criteria_summary_rows: g.precondition_name_resolution_return_evidence_criteria_summary_rows,
      return_criterion_type_summary_rows: g.return_criterion_type_summary_rows,
      parent_criterion_type_resolution_return_evidence_criteria_summary_rows: g.parent_criterion_type_resolution_return_evidence_criteria_summary_rows,
      packet_unit_resolution_return_evidence_criteria_summary_rows: g.packet_unit_resolution_return_evidence_criteria_summary_rows
    },
    zero_gates: {
      criteria_rows_passed: 0,
      criteria_rows_failed: 0,
      evidence_values_reviewed: 0,
      evidence_values_filled: 0,
      returns_received: 0,
      blockers_resolved: 0,
      true_precondition_cells: 0,
      source_system_decisions_recorded: 0,
      exact_line_spans_selected: 0,
      source_prose_copied: 0,
      excerpts_selected: 0,
      surfaces_filled: 0,
      translated_passages: 0,
      readiness_claims: 0
    },
    upload_intent: 'Queue the package-123 JSON/MD/CSV/checksum and this note for the existing Noether upload path as substantive coordination material; do not defer because of mobile-plan or bandwidth wording.',
    no_remote_action_by_this_note: true,
    message_template: `Package 123 added ${artifactId}: blank OLP/DMOI reviewer-scope decision-precondition blocker resolution-return evidence criteria rubric. Counts: ${g.decision_precondition_blocker_resolution_return_evidence_criteria_rows} criteria groups, ${g.criterion_rows} criterion rows, ${g.criteria_types_per_return_row} criteria types per return row, ${g.criteria_rows_unfilled} unfilled criterion rows; 0 evidence values, 0 passed/failed criteria, 0 returns received, 0 blockers resolved, 0 true preconditions, 0 source text/excerpts, 0 surfaces, 0 translations, 0 readiness.`
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 123 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 123 creates an OLP/DMOI relation-function reviewer-scope decision-precondition blocker resolution-return evidence criteria rubric with \`${g.decision_precondition_blocker_resolution_return_evidence_criteria_rows}\` criteria group rows, \`${g.criterion_rows}\` criterion rows, and \`${g.criteria_types_per_return_row}\` criteria types per package-122 return row.

Zero gates: \`0\` evidence values, \`0\` evidence pointers, \`0\` passed criteria, \`0\` failed criteria, \`0\` returns received, \`0\` blockers resolved, \`0\` true preconditions, \`0\` criteria decisions, \`0\` source-system decisions, \`0\` exact line spans, \`0\` source prose, \`0\` examples, \`0\` excerpts, \`0\` selected-excerpt attribution notices, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Upload intent: ${note.upload_intent}

Boundary: resolution-return evidence criteria rubric only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, translation, publication, pilot, legal-advice, or remote-state claim.
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
      role: 'olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric_support',
      artifact: artifactId,
      current_use: '640 blank decision-precondition blocker resolution-return evidence criteria groups from package-122 return rows; 2,560 unfilled criterion rows; 4 criteria types per return row; 8 precondition-name summaries; 4 return-criterion-type summaries; 8 parent-criterion-type summaries; 10 packet-unit summaries; 0 evidence values, 0 passed/failed criteria, 0 returns received, 0 blockers resolved, 0 source prose, 0 excerpts, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  packageIndex.obj.current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_groups: artifact.gate_state.decision_precondition_blocker_resolution_return_evidence_criteria_rows,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criterion_rows: artifact.gate_state.criterion_rows,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_passed: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_failed: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_values_filled: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_returns_received: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_rows_resolved: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_true_cells: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_source_prose_copied: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_excerpts_selected: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_surfaces_filled: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_translations_filled: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_return_evidence_intake_ledger_or_exact_line_span_candidate_register_blank_only_no_source_text_no_surfaces_no_translation`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function reviewer-scope decision-precondition blocker resolution-return evidence criteria rubric',
    route: artifactId,
    license_status_to_recheck: 'resolution_return_evidence_criteria_rubric_only_no_evidence_values_no_returns_received_no_resolutions_no_line_span_selection_no_source_text_no_surfaces_no_translation',
    best_translation_use: 'future reviewer-scope blocker-resolution return evidence review before source-system, scope, line-span, source-text, local/bridge, and translation-owner gates',
    candidate_lanes: ['semi_constructed_relation_function_source_request_lane', 'open_source_candidate_catalog', 'reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric', 'review_only_construction_scaffold'],
    priority: 1,
    status: 'reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric_no_evidence_no_returns_no_resolutions_no_excerpts_no_source_text_no_surfaces_no_translation_no_pilot',
    gate_state: {
      criterion_rows: artifact.gate_state.criterion_rows,
      criteria_rows_passed: 0,
      criteria_rows_failed: 0,
      evidence_values_filled: 0,
      returns_received: 0,
      blockers_resolved: 0,
      true_precondition_cells: 0,
      source_prose_copied: 0,
      excerpts_selected: 0,
      translated_passages: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric: ${artifactId}_640_groups_2560_criteria_0_evidence_0_returns_0_resolutions_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_groups: artifact.gate_state.decision_precondition_blocker_resolution_return_evidence_criteria_rows,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criterion_rows: artifact.gate_state.criterion_rows,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_returns_received: 0,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_blockers_resolved: 0,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_true_cells: 0,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_source_prose_copied: 0,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_excerpts_selected: 0,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_translations: 0,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric: ${artifactId}_blank_criteria_only_no_evidence_no_returns_no_resolutions_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 640 resolution-return evidence criteria groups and 2,560 unfilled criterion rows from package-122 return rows; 4 criteria types per return row; 0 evidence values, 0 passed/failed criteria, 0 returns received, 0 blockers resolved, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be queued for upload when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function reviewer-scope decision-precondition blocker resolution-return evidence criteria rubric; 640 criteria groups, 2,560 unfilled criterion rows, 0 evidence values, 0 passed/failed criteria, 0 returns received, 0 blockers resolved, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 123: OLP/DMOI relation-function reviewer-scope decision-precondition blocker resolution-return evidence criteria rubric after package 122. It records 640 criteria group rows and 2,560 unfilled criterion rows while keeping 0 evidence values, 0 passed/failed criteria, 0 returns received, 0 blockers resolved, 0 true preconditions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function reviewer-scope decision-precondition blocker resolution-return evidence criteria rubric | ${artifactId} | Resolution-return evidence criteria rubric; 640 criteria groups, 2,560 unfilled criterion rows, 0 evidence values, 0 returns received, 0 blockers resolved, 0 source prose, 0 excerpts, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric_artifact: \`${artifactId}\` (640 criteria groups; 2,560 unfilled criterion rows; 0 evidence values; 0 returns received; 0 source prose; 0 excerpts; no surfaces, no translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric: \`${artifactId}\`; criteria rubric only, no evidence values, received returns, resolved blockers, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI reviewer-scope decision-precondition blocker resolution-return evidence criteria rubric; blank criteria are not evidence review, received returns, exact excerpt authorization, source text, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_reviewer_scope_decision_precondition_blocker_resolution_return_evidence_criteria_rubric' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package123_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package123_coordination_note' },
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
  upload.obj.user_upload_clarification = '2026-07-03: user clarified again that substantive artifacts should always be queued/uploaded when a staging path exists; do not suppress them because of mobile-plan or bandwidth wording.';
  upload.obj.package123_upload_queue_update = {
    captured_utc: '2026-07-03T01:02:00Z',
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
  const step = 'Stage package 123 OLP/DMOI relation-function reviewer-scope decision-precondition blocker resolution-return evidence-criteria artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.decision_precondition_blocker_resolution_return_evidence_criteria_rows.length !== 640) failures.push('return_evidence_criteria_rows_not_640');
  if (artifact.criterion_rows.length !== 2560) failures.push('criterion_rows_not_2560');
  if (artifact.precondition_name_resolution_return_evidence_criteria_summary_rows.length !== 8) failures.push('precondition_name_summary_rows_not_8');
  if (artifact.return_criterion_type_summary_rows.length !== 4) failures.push('return_criterion_type_summary_rows_not_4');
  if (artifact.parent_criterion_type_resolution_return_evidence_criteria_summary_rows.length !== 8) failures.push('parent_criterion_type_summary_rows_not_8');
  if (artifact.packet_unit_resolution_return_evidence_criteria_summary_rows.length !== 10) failures.push('packet_unit_summary_rows_not_10');
  if (g.criteria_types_per_return_row !== 4) failures.push(`criteria_types_per_return_row_not_4_${g.criteria_types_per_return_row}`);
  if (g.criteria_rows_unfilled !== 2560) failures.push(`criteria_rows_unfilled_not_2560_${g.criteria_rows_unfilled}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.criterion_rows) {
    if (row.evidence_value !== null || row.evidence_source_pointer !== null || row.evidence_date !== null || row.criterion_passed || row.criterion_failed || !row.criterion_unfilled || row.source_text_capture_allowed_after_pass || row.surface_gate_opened || row.translation_gate_opened) {
      failures.push(`nonblank_criterion_row_${row.criterion_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  return failures;
}

const parent = (await readJson(parentReturnLedger)).obj;
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
  return_evidence_criteria_rows: artifact.gate_state.decision_precondition_blocker_resolution_return_evidence_criteria_rows,
  criterion_rows: artifact.gate_state.criterion_rows,
  criteria_types_per_return_row: artifact.gate_state.criteria_types_per_return_row,
  criteria_rows_passed: artifact.gate_state.criteria_rows_passed,
  criteria_rows_failed: artifact.gate_state.criteria_rows_failed,
  criteria_rows_unfilled: artifact.gate_state.criteria_rows_unfilled,
  evidence_values_filled: artifact.gate_state.evidence_values_filled,
  returns_received: artifact.gate_state.returns_received,
  blockers_resolved: artifact.gate_state.blockers_resolved,
  true_precondition_cells: artifact.gate_state.true_precondition_cells,
  source_prose_copied: artifact.gate_state.source_prose_copied,
  excerpts_selected: artifact.gate_state.excerpts_selected,
  local_language_surfaces_filled: artifact.gate_state.local_language_surfaces_filled,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
