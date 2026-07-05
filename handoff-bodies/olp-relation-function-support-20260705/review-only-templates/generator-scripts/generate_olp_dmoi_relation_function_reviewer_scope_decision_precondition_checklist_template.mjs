import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_DECISION_PRECONDITION_CHECKLIST_TEMPLATE_20260703T000000Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_DECISION_PRECONDITION_CHECKLIST_TEMPLATE_NOTE_20260703T000100Z';
const generatedUtc = '2026-07-03T00:00:00Z';
const noteGeneratedUtc = '2026-07-03T00:01:00Z';
const packageOrder = 119;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-REVIEWER-SCOPE-DECISION-PRECONDITION-CHECKLIST-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentArtifacts = [
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_20260702T150000Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_RETURN_EVIDENCE_INTAKE_LEDGER_TEMPLATE_20260702T144500Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_RETURN_EVIDENCE_CRITERIA_RUBRIC_20260702T143000Z',
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_RETURN_LEDGER_TEMPLATE_20260702T141500Z'
];

const preconditionNames = [
  'decision_row_linkage_validated',
  'all_decision_fields_filled',
  'all_criteria_decisions_recorded',
  'evidence_value_reviewed_or_explicitly_absent',
  'source_text_prohibition_confirmed',
  'source_system_scope_decision_bounded',
  'downstream_line_span_gate_separate',
  'downstream_surface_translation_gates_separate'
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

function falsePreconditions() {
  return Object.fromEntries(preconditionNames.map((name) => [name, false]));
}

function buildChecklistRows(parent) {
  return parent.criteria_decision_rows.map((row, index) => ({
    decision_precondition_checklist_row_id: `ODRF-RSCOPE-DPC-${String(index + 1).padStart(3, '0')}`,
    parent_criteria_decision_row_id: row.criteria_decision_row_id,
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
    required_boolean_preconditions: preconditionNames,
    boolean_preconditions: falsePreconditions(),
    true_precondition_cells: 0,
    false_precondition_cells: preconditionNames.length,
    decision_fields_filled: 0,
    criteria_decision_recorded: false,
    criterion_passed: false,
    criterion_failed: false,
    criterion_unfilled: true,
    evidence_value_reviewed: false,
    source_system_decision_allowed_now: false,
    scope_decision_allowed_now: false,
    line_span_candidate_register_allowed_now: false,
    source_text_capture_allowed_now: false,
    surface_gate_opened: false,
    translation_gate_opened: false,
    checklist_status: 'blank_precondition_checklist_row_only'
  }));
}

function buildCriterionTypeSummaries(parent, checklistRows) {
  return parent.criterion_type_criteria_decision_summary_rows.map((row, index) => {
    const linked = checklistRows.filter((checklist) => checklist.criterion_type === row.criterion_type);
    return {
      decision_precondition_criterion_type_summary_row_id: `ODRF-RSCOPE-DPC-TYPE-${String(index + 1).padStart(2, '0')}`,
      parent_criteria_decision_criterion_type_summary_row_id: row.criteria_decision_criterion_type_summary_row_id,
      criterion_type: row.criterion_type,
      required_future_evidence_class: row.required_future_evidence_class,
      linked_decision_precondition_checklist_row_ids: linked.map((checklist) => checklist.decision_precondition_checklist_row_id),
      checklist_rows_required: linked.length,
      checklist_rows_ready: 0,
      true_precondition_cells: 0,
      false_precondition_cells: linked.length * preconditionNames.length,
      decisions_recorded: 0,
      criteria_rows_passed: 0,
      criteria_rows_failed: 0,
      criteria_rows_unfilled: linked.length,
      type_ready_for_promotion_review: false
    };
  });
}

function buildPacketUnitSummaries(parent, checklistRows) {
  return parent.packet_unit_criteria_decision_summary_rows.map((row, index) => {
    const linked = checklistRows.filter((checklist) => checklist.packet_unit === row.packet_unit);
    return {
      decision_precondition_packet_unit_summary_row_id: `ODRF-RSCOPE-DPC-UNIT-${String(index + 1).padStart(2, '0')}`,
      parent_criteria_decision_packet_unit_summary_row_id: row.criteria_decision_packet_unit_summary_row_id,
      packet_unit: row.packet_unit,
      parent_ledger_row_id: row.parent_ledger_row_id,
      parent_pointer_row_id: row.parent_pointer_row_id,
      linked_decision_precondition_checklist_row_ids: linked.map((checklist) => checklist.decision_precondition_checklist_row_id),
      checklist_rows_required: linked.length,
      checklist_rows_ready: 0,
      true_precondition_cells: 0,
      false_precondition_cells: linked.length * preconditionNames.length,
      decisions_recorded: 0,
      criteria_rows_passed: 0,
      criteria_rows_failed: 0,
      criteria_rows_unfilled: linked.length,
      row_promoted: false
    };
  });
}

function buildArtifact(parent) {
  const checklistRows = buildChecklistRows(parent);
  const criterionTypeSummaries = buildCriterionTypeSummaries(parent, checklistRows);
  const packetUnitSummaries = buildPacketUnitSummaries(parent, checklistRows);
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template_no_true_preconditions_no_decisions_no_returns_no_source_text_no_surfaces_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Create a blank decision-precondition checklist for package-118 criteria-decision rows so future evidence review cannot promote source-system, scope, line-span, source-text, surface, translation, publication, or pilot gates without explicit preconditions.',
    parent_artifacts: parentArtifacts,
    checklist_boundary: {
      checklist_is: 'blank boolean precondition checklist for future criteria-decision promotion review',
      checklist_is_not: [
        'filled decision checklist',
        'evidence review result',
        'reviewer return',
        'source-system decision',
        'scope decision',
        'line-span register',
        'source-prose cache',
        'local-language term decision',
        'semi-constructed surface acceptance',
        'translation draft',
        'publication or pilot claim'
      ],
      allowed_now: [
        'allocate false boolean preconditions',
        'link preconditions to package-118 decision rows',
        'summarize unresolved preconditions by criterion type and packet unit'
      ],
      blocked_now: [
        'setting preconditions true',
        'recording criteria decisions',
        'passing or failing criteria',
        'opening source text, surface, translation, or readiness gates'
      ]
    },
    precondition_names: preconditionNames,
    decision_precondition_checklist_rows: checklistRows,
    criterion_type_decision_precondition_summary_rows: criterionTypeSummaries,
    packet_unit_decision_precondition_summary_rows: packetUnitSummaries,
    gate_state: {
      decision_precondition_checklist_rows: checklistRows.length,
      criterion_type_decision_precondition_summary_rows: criterionTypeSummaries.length,
      packet_unit_decision_precondition_summary_rows: packetUnitSummaries.length,
      boolean_preconditions_per_row: preconditionNames.length,
      true_precondition_cells: 0,
      false_precondition_cells: checklistRows.length * preconditionNames.length,
      inherited_criteria_decision_rows: parent.gate_state.criteria_decision_rows,
      inherited_evidence_intake_rows: parent.gate_state.inherited_evidence_intake_rows,
      inherited_parent_ledger_rows: parent.gate_state.inherited_parent_ledger_rows,
      decision_fields_filled: 0,
      criteria_decisions_recorded: 0,
      criteria_rows_passed: 0,
      criteria_rows_failed: 0,
      criteria_rows_unfilled: checklistRows.length,
      evidence_values_reviewed: 0,
      evidence_values_filled: 0,
      evidence_rows_filled: 0,
      returns_ingested: 0,
      return_fields_filled: 0,
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
      decision_precondition_checklist_rows_expected: 80,
      criterion_type_summary_rows_expected: 8,
      packet_unit_summary_rows_expected: 10,
      boolean_preconditions_per_row_expected: 8,
      false_precondition_cells_expected: 640,
      zero_gate_assertions: [
        'true_precondition_cells',
        'decision_fields_filled',
        'criteria_decisions_recorded',
        'criteria_rows_passed',
        'criteria_rows_failed',
        'evidence_values_reviewed',
        'evidence_values_filled',
        'evidence_rows_filled',
        'returns_ingested',
        'return_fields_filled',
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
      'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_DECISION_PRECONDITION_BLOCKER_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_EXACT_LINE_SPAN_CANDIDATE_REGISTER_BLANK_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_<timestamp>'
    ],
    decision: 'Package 119 allocates false precondition cells after package 118. It does not set preconditions true, review evidence, decide criteria, ingest returns, or open any source-text, surface, translation, publication, or pilot gate.'
  };
}

function buildArtifactMd(artifact) {
  const rows = artifact.decision_precondition_checklist_rows.slice(0, 20).map((row) => `| \`${row.decision_precondition_checklist_row_id}\` | \`${row.parent_criteria_decision_row_id}\` | ${row.packet_unit} | ${row.criterion_type} | \`${row.true_precondition_cells}\` | \`${row.false_precondition_cells}\` |`).join('\n');
  const typeRows = artifact.criterion_type_decision_precondition_summary_rows.map((row) => `| ${row.criterion_type} | \`${row.checklist_rows_required}\` | \`${row.false_precondition_cells}\` |`).join('\n');
  const gateRows = Object.entries(artifact.gate_state).map(([key, value]) => `| ${key} | \`${Array.isArray(value) ? value.length : value}\` |`).join('\n');
  return `# OLP/DMOI Relation-Function Reviewer Scope Decision Precondition Checklist Template

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Checklist Rows

Showing first 20 of \`${artifact.decision_precondition_checklist_rows.length}\` blank checklist rows.

| Checklist row | Parent decision row | Packet unit | Criterion type | True cells | False cells |
| --- | --- | --- | --- | ---: | ---: |
${rows}

## Criterion Type Summary

| Criterion type | Checklist rows | False precondition cells |
| --- | ---: | ---: |
${typeRows}

## Gate State

| Gate | State |
| --- | ---: |
${gateRows}

Decision: ${artifact.decision}
`;
}

function buildArtifactCsv(artifact) {
  const columns = [
    'decision_precondition_checklist_row_id',
    'parent_criteria_decision_row_id',
    'parent_evidence_intake_row_id',
    'parent_criterion_row_id',
    'parent_ledger_row_id',
    'parent_reviewer_scope_row_id',
    'parent_gap_check_row_id',
    'parent_pointer_row_id',
    'packet_unit',
    'reviewer_role',
    'criterion_type',
    'source_systems_implicated',
    'true_precondition_cells',
    'false_precondition_cells',
    'criteria_decision_recorded',
    'checklist_status'
  ];
  const rows = artifact.decision_precondition_checklist_rows.map((row) => columns.map((column) => csvCell(row[column])).join(','));
  return `${columns.join(',')}\n${rows.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    source_artifact: artifact.artifact_id,
    package_order: packageOrder,
    status: 'pointer_only_reviewer_scope_decision_precondition_checklist_template_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-119 OLP/DMOI reviewer-scope decision-precondition checklist continuation while preserving no-true-precondition/no-decision/no-return/no-excerpt/no-translation boundaries.',
    counts: {
      decision_precondition_checklist_rows: g.decision_precondition_checklist_rows,
      criterion_type_decision_precondition_summary_rows: g.criterion_type_decision_precondition_summary_rows,
      packet_unit_decision_precondition_summary_rows: g.packet_unit_decision_precondition_summary_rows,
      boolean_preconditions_per_row: g.boolean_preconditions_per_row,
      false_precondition_cells: g.false_precondition_cells,
      inherited_criteria_decision_rows: g.inherited_criteria_decision_rows
    },
    zero_gates: {
      true_precondition_cells: 0,
      decision_fields_filled: 0,
      criteria_decisions_recorded: 0,
      criteria_rows_passed: 0,
      criteria_rows_failed: 0,
      evidence_values_reviewed: 0,
      returns_ingested: 0,
      source_system_decisions_recorded: 0,
      scope_decisions_recorded: 0,
      exact_line_spans_selected: 0,
      source_prose_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      excerpts_selected: 0,
      selected_excerpt_attribution_notices_filled: 0,
      surfaces_filled: 0,
      translated_passages: 0,
      readiness_claims: 0
    },
    no_remote_action_by_this_note: true
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 119 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 119 creates an OLP/DMOI relation-function reviewer-scope decision-precondition checklist template with \`${g.decision_precondition_checklist_rows}\` blank checklist rows, \`${g.boolean_preconditions_per_row}\` boolean preconditions per row, and \`${g.false_precondition_cells}\` false precondition cells.

Zero gates: \`0\` true preconditions, \`0\` filled decision fields, \`0\` criteria decisions, \`0\` passed/failed criteria, \`0\` evidence values reviewed, \`0\` returns, \`0\` source-system decisions, \`0\` scope decisions, \`0\` exact line spans, \`0\` source prose, \`0\` examples, \`0\` excerpts, \`0\` selected-excerpt attribution notices, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Boundary: decision-precondition checklist template only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, translation, publication, pilot, legal-advice, or remote-state claim.
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
      role: 'olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template_support',
      artifact: artifactId,
      current_use: '80 blank decision-precondition checklist rows for package-118 decision rows; 8 false boolean preconditions per row; 640 false precondition cells; 0 true preconditions, 0 decisions, 0 evidence reviewed, 0 returns, 0 source-system decisions, 0 line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  packageIndex.obj.current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_rows: artifact.gate_state.decision_precondition_checklist_rows,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_false_cells: artifact.gate_state.false_precondition_cells,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_true_cells: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_decisions_recorded: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_returns_ingested: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_source_system_decisions: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_source_prose_copied: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_excerpts_selected: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_surfaces_filled: 0,
    olp_dmoi_relation_function_reviewer_scope_decision_precondition_translations_filled: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_decision_precondition_blocker_ledger_or_exact_line_span_candidate_register_blank_only_no_source_text_no_surfaces_no_translation`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function reviewer-scope decision-precondition checklist template',
    route: artifactId,
    license_status_to_recheck: 'decision_precondition_checklist_only_no_true_preconditions_no_decisions_no_returns_no_line_span_selection_no_source_text_no_surfaces_no_translation',
    best_translation_use: 'future reviewer-scope decision precondition review before source-system, scope, line-span, source-text, local/bridge, and translation-owner gates',
    candidate_lanes: ['semi_constructed_relation_function_source_request_lane', 'open_source_candidate_catalog', 'reviewer_scope_decision_precondition_checklist', 'review_only_construction_scaffold'],
    priority: 1,
    status: 'reviewer_scope_decision_precondition_checklist_template_no_true_preconditions_no_decisions_no_returns_no_excerpts_no_source_text_no_surfaces_no_translation_no_pilot',
    gate_state: {
      decision_precondition_checklist_rows: artifact.gate_state.decision_precondition_checklist_rows,
      false_precondition_cells: artifact.gate_state.false_precondition_cells,
      true_precondition_cells: 0,
      criteria_decisions_recorded: 0,
      returns_ingested: 0,
      source_system_decisions_recorded: 0,
      source_prose_copied: 0,
      excerpts_selected: 0,
      translated_passages: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template: ${artifactId}_80_rows_640_false_precondition_cells_0_true_0_decisions_0_returns_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_rows: artifact.gate_state.decision_precondition_checklist_rows,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_false_cells: artifact.gate_state.false_precondition_cells,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_true_cells: 0,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_returns: 0,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_source_prose_copied: 0,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_excerpts_selected: 0,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_translations: 0,
    current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template: ${artifactId}_blank_only_no_true_preconditions_no_decisions_no_returns_no_excerpts_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 80 blank decision-precondition checklist rows and 640 false precondition cells over package-118 decision rows; 0 true preconditions, 0 decisions, 0 evidence reviewed, 0 returns, 0 source-system decisions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be queued for upload when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function reviewer-scope decision-precondition checklist template; 80 blank checklist rows, 640 false precondition cells, 0 true preconditions, 0 decisions, 0 evidence reviewed, 0 returns, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 119: OLP/DMOI relation-function reviewer-scope decision-precondition checklist template after package 118. It records 80 blank checklist rows and 640 false precondition cells while keeping 0 true preconditions, 0 decisions, 0 evidence reviewed, 0 returns, 0 source-system decisions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function reviewer-scope decision-precondition checklist template | ${artifactId} | Decision-precondition checklist; 80 rows, 640 false precondition cells, 0 true preconditions, 0 decisions, 0 evidence reviewed, 0 returns, 0 source decisions, 0 source prose, 0 excerpts, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template_artifact: \`${artifactId}\` (80 blank checklist rows; 640 false precondition cells; 0 true preconditions; 0 returns; 0 source prose; 0 excerpts; no surfaces, no translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template: \`${artifactId}\`; decision-precondition checklist only, no true preconditions, decisions, returns, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI reviewer-scope decision-precondition checklist template; false checklist cells are not evidence review, dispatches, returns, exact excerpt authorization, source text, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_reviewer_scope_decision_precondition_checklist_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package119_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package119_coordination_note' },
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
  upload.obj.user_upload_clarification = '2026-07-02: user clarified that substantive artifacts should always be queued/uploaded when a staging path exists; do not suppress them because of mobile-plan or bandwidth wording.';
  upload.obj.package119_upload_queue_update = {
    captured_utc: '2026-07-03T00:02:00Z',
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
  const step = 'Stage package 119 OLP/DMOI relation-function reviewer-scope decision-precondition checklist artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.decision_precondition_checklist_rows.length !== 80) failures.push('decision_precondition_checklist_rows_not_80');
  if (artifact.criterion_type_decision_precondition_summary_rows.length !== 8) failures.push('criterion_type_summary_rows_not_8');
  if (artifact.packet_unit_decision_precondition_summary_rows.length !== 10) failures.push('packet_unit_summary_rows_not_10');
  if (g.boolean_preconditions_per_row !== 8) failures.push(`boolean_preconditions_per_row_not_8_${g.boolean_preconditions_per_row}`);
  if (g.false_precondition_cells !== 640) failures.push(`false_precondition_cells_not_640_${g.false_precondition_cells}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  return failures;
}

const parent = (await readJson('OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_RETURN_EVIDENCE_CRITERIA_DECISION_LEDGER_TEMPLATE_20260702T150000Z')).obj;
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
  decision_precondition_checklist_rows: artifact.gate_state.decision_precondition_checklist_rows,
  criterion_type_summary_rows: artifact.gate_state.criterion_type_decision_precondition_summary_rows,
  packet_unit_summary_rows: artifact.gate_state.packet_unit_decision_precondition_summary_rows,
  boolean_preconditions_per_row: artifact.gate_state.boolean_preconditions_per_row,
  true_precondition_cells: artifact.gate_state.true_precondition_cells,
  false_precondition_cells: artifact.gate_state.false_precondition_cells,
  criteria_decisions_recorded: artifact.gate_state.criteria_decisions_recorded,
  returns_ingested: artifact.gate_state.returns_ingested,
  source_system_decisions_recorded: artifact.gate_state.source_system_decisions_recorded,
  exact_line_spans_selected: artifact.gate_state.exact_line_spans_selected,
  source_prose_copied: artifact.gate_state.source_prose_copied,
  excerpts_selected: artifact.gate_state.excerpts_selected,
  local_language_surfaces_filled: artifact.gate_state.local_language_surfaces_filled,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
