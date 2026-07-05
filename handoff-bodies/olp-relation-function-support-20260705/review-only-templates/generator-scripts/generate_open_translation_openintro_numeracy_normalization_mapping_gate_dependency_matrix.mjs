import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_NORMALIZATION_MAPPING_GATE_DEPENDENCY_MATRIX_20260703T143000Z';
const noteId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_NORMALIZATION_MAPPING_GATE_DEPENDENCY_MATRIX_NOTE_20260703T143100Z';
const generatedUtc = '2026-07-03T14:30:00Z';
const noteGeneratedUtc = '2026-07-03T14:31:00Z';
const packageOrder = 177;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-OPENINTRO-NUMERACY-NORMALIZATION-MAPPING-GATE-DEPENDENCY-MATRIX-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentFile = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_NORMALIZATION_MAPPING_GATE_FRONTIER_INDEX_20260703T141500Z';

const blockedFutureActions = [
  {
    future_action: 'mapping_decision_review_return_intake',
    future_artifact_pattern: 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_NORMALIZATION_MAPPING_DECISION_REVIEW_RETURN_LEDGER_WITH_RETURNS_<timestamp>',
    current_blocker: 'completed_mapping_preconditions_and_dated_review_returns_absent'
  },
  {
    future_action: 'normalization_mapping_decision_activation',
    future_artifact_pattern: 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_NORMALIZATION_MAPPING_DECISION_LEDGER_WITH_DECISIONS_<timestamp>',
    current_blocker: 'completed_mapping_preconditions_absent'
  },
  {
    future_action: 'normalization_taxonomy_with_mappings',
    future_artifact_pattern: 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_REVIEW_RETURN_INTAKE_NORMALIZATION_TAXONOMY_WITH_MAPPINGS_<timestamp>',
    current_blocker: 'completed_mapping_preconditions_absent'
  },
  {
    future_action: 'local_source_route_acceptance_decision',
    future_artifact_pattern: 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_ACCEPTANCE_DECISION_LEDGER_TEMPLATE_<timestamp>',
    current_blocker: 'completed_precondition_checks_and_source_route_returns_absent'
  }
];

const dependencyTypes = [
  'dated_nonpersonal_return',
  'parent_row_identity_match',
  'nonprose_evidence_pointer',
  'nonprose_evidence_value',
  'boundary_or_permission_review',
  'source_text_absence_confirmation',
  'downstream_gate_limit_confirmation',
  'later_artifact_authorization'
];

const zeroGateKeys = [
  'dependency_cells_filled',
  'dependency_reviews_completed',
  'future_actions_unblocked',
  'mapping_decision_review_returns_received',
  'mapping_decision_review_returns_ingested',
  'mapping_decision_rows_reviewed',
  'mapping_decision_rows_completed',
  'normalization_mapping_authorizations_recorded',
  'normalization_mapping_decisions_recorded',
  'normalization_status_codes_activated',
  'mapping_precondition_returns_received',
  'mapping_precondition_returns_ingested',
  'mapping_precondition_checks_completed',
  'taxonomy_review_returns_received',
  'taxonomy_review_returns_ingested',
  'review_returns_received',
  'review_returns_ingested',
  'evidence_values_recorded',
  'evidence_source_pointers_recorded',
  'actual_source_routes_confirmed',
  'candidate_source_routes_recorded',
  'candidate_source_urls_recorded',
  'candidate_source_owners_recorded',
  'candidate_source_owners_contacted',
  'source_scans_completed',
  'source_text_or_excerpt_files_created',
  'source_text_copied',
  'source_excerpts_copied',
  'source_tables_copied',
  'source_figures_copied',
  'source_datasets_copied',
  'translated_passages',
  'proposed_bridge_lexemes',
  'accepted_bridge_surfaces'
];

function parseJson(text) {
  return JSON.parse(text.charCodeAt(0) === 0xFEFF ? text.slice(1) : text);
}

async function readJson(stem) {
  return { obj: parseJson(await readFile(path.join(outputs, `${stem}.json`), 'utf8')) };
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

function buildRows(parent) {
  const rows = [];
  let index = 1;
  for (const action of blockedFutureActions) {
    for (const dependency_type of dependencyTypes) {
      rows.push({
        openintro_numeracy_mapping_gate_dependency_row_id: `OI-NUM-MAPPING-DEPENDENCY-${String(index).padStart(3, '0')}`,
        parent_frontier_index: parent.artifact_id,
        future_action: action.future_action,
        future_artifact_pattern: action.future_artifact_pattern,
        dependency_type,
        current_blocker: action.current_blocker,
        dependency_status: 'blocked_no_current_evidence_or_review_return',
        current_evidence_count: 0,
        current_source_text_files: 0,
        current_mapping_decisions: 0,
        current_translations: 0,
        allowed_now: false,
        future_allowed_after: 'later_dated_returns_completed_preconditions_and_no_source_prose_boundary_review',
        comments_without_source_prose: null,
        dependency_cells_filled: 0,
        dependency_review_completed: false,
        future_action_unblocked: false,
        source_text_or_excerpt_allowed_now: false,
        translation_allowed_now: false,
        local_surface_allowed_now: false,
        pilot_ready: false
      });
      index += 1;
    }
  }
  return rows;
}

function summaryRows(rows, groupKey, idPrefix) {
  const map = new Map();
  for (const row of rows) {
    const key = row[groupKey];
    if (!map.has(key)) {
      map.set(key, {
        group_key: key,
        dependency_rows: 0,
        allowed_now: 0,
        dependency_reviews_completed: 0,
        future_actions_unblocked: 0,
        evidence_values_recorded: 0,
        mappings_recorded: 0,
        source_text_or_excerpt_files_created: 0,
        translated_passages: 0,
        readiness_claim: false
      });
    }
    map.get(key).dependency_rows += 1;
  }
  return [...map.values()].sort((a, b) => String(a.group_key).localeCompare(String(b.group_key))).map((item, index) => ({
    [`${idPrefix}_summary_row_id`]: `${idPrefix.toUpperCase()}-${String(index + 1).padStart(3, '0')}`,
    ...item
  }));
}

function buildArtifact(parent) {
  const rows = buildRows(parent);
  const actionRows = summaryRows(rows, 'future_action', 'oi_num_mapping_dependency_action');
  const dependencyRows = summaryRows(rows, 'dependency_type', 'oi_num_mapping_dependency_type');
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'gate_dependency_matrix_only_no_returns_no_decisions_no_mappings_no_evidence_no_source_text_no_translation_no_readiness',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Record the blocked dependency matrix for the OpenIntro IMS numeracy normalization-mapping lane so future sessions can see which later actions require dated returns and completed preconditions, without recording evidence, decisions, mappings, source text, translation, constructed forms, or readiness.',
    parent_artifacts: {
      normalization_mapping_gate_frontier_index: parent.artifact_id,
      package_order_parent: 176,
      package_order_current: packageOrder
    },
    boundary: {
      source_text_included: false,
      source_excerpts_included: false,
      source_tables_included: false,
      source_figures_included: false,
      source_datasets_included: false,
      source_urls_included: false,
      translations_included: false,
      proposed_constructed_forms_included: false,
      accepted_constructed_surfaces_included: false,
      evidence_values_included: false,
      evidence_pointers_included: false,
      mapping_authorizations_included: false,
      mapping_decisions_included: false,
      status_code_activations_included: false,
      remote_actions_included: false,
      legal_advice_included: false
    },
    inherited_parent_counts: {
      parent_frontier_package_rows: parent.gate_state.openintro_numeracy_frontier_package_rows,
      parent_frontier_gate_profile_rows: parent.gate_state.openintro_numeracy_frontier_gate_profile_rows,
      parent_mapping_decision_review_returns_received: parent.gate_state.mapping_decision_review_returns_received,
      parent_mapping_decisions_recorded: parent.gate_state.normalization_mapping_decisions_recorded,
      parent_evidence_values_recorded: parent.gate_state.evidence_values_recorded,
      parent_source_text_copied: parent.gate_state.source_text_copied,
      parent_pilot_ready: parent.gate_state.pilot_ready
    },
    blocked_future_actions: blockedFutureActions,
    dependency_types: dependencyTypes,
    openintro_numeracy_mapping_gate_dependency_rows: rows,
    openintro_numeracy_mapping_gate_dependency_action_summary_rows: actionRows,
    openintro_numeracy_mapping_gate_dependency_type_summary_rows: dependencyRows,
    gate_state: {
      openintro_numeracy_mapping_gate_dependency_rows: rows.length,
      mapping_gate_dependency_action_summary_rows: actionRows.length,
      mapping_gate_dependency_type_summary_rows: dependencyRows.length,
      dependency_cells_filled: 0,
      dependency_reviews_completed: 0,
      future_actions_unblocked: 0,
      mapping_decision_review_returns_received: 0,
      mapping_decision_review_returns_ingested: 0,
      mapping_decision_rows_reviewed: 0,
      mapping_decision_rows_completed: 0,
      normalization_mapping_authorizations_recorded: 0,
      normalization_mapping_decisions_recorded: 0,
      normalization_status_codes_activated: 0,
      mapping_precondition_returns_received: 0,
      mapping_precondition_returns_ingested: 0,
      mapping_precondition_checks_completed: 0,
      taxonomy_review_returns_received: 0,
      taxonomy_review_returns_ingested: 0,
      review_returns_received: 0,
      review_returns_ingested: 0,
      evidence_values_recorded: 0,
      evidence_source_pointers_recorded: 0,
      actual_source_routes_confirmed: 0,
      candidate_source_routes_recorded: 0,
      candidate_source_urls_recorded: 0,
      candidate_source_owners_recorded: 0,
      candidate_source_owners_contacted: 0,
      source_scans_completed: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_excerpts_copied: 0,
      source_tables_copied: 0,
      source_figures_copied: 0,
      source_datasets_copied: 0,
      translated_passages: 0,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      publication_ready: false,
      translation_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      expected_dependency_rows: blockedFutureActions.length * dependencyTypes.length,
      expected_action_summary_rows: blockedFutureActions.length,
      expected_dependency_type_summary_rows: dependencyTypes.length,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_NORMALIZATION_MAPPING_DECISION_REVIEW_RETURN_LEDGER_WITH_RETURNS_<timestamp>_only_after_completed_mapping_preconditions',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_NORMALIZATION_MAPPING_DECISION_LEDGER_WITH_DECISIONS_<timestamp>_only_after_completed_mapping_preconditions',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_REVIEW_RETURN_INTAKE_NORMALIZATION_TAXONOMY_WITH_MAPPINGS_<timestamp>_only_after_completed_mapping_preconditions'
    ],
    decision: 'Package 177 is a gate dependency matrix only. It records blocked future-action dependencies, but no review returns, no decisions, no mapping authorizations, no active mappings, no evidence pointers, no evidence values, no source text, no excerpts, no translations, no constructed forms, and no readiness claims.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const actionRows = artifact.openintro_numeracy_mapping_gate_dependency_action_summary_rows.map((row) => `| ${row.oi_num_mapping_dependency_action_summary_row_id} | ${row.group_key} | ${row.dependency_rows} | ${row.allowed_now} | ${row.future_actions_unblocked} |`).join('\n');
  const dependencyRows = artifact.openintro_numeracy_mapping_gate_dependency_type_summary_rows.map((row) => `| ${row.oi_num_mapping_dependency_type_summary_row_id} | ${row.group_key} | ${row.dependency_rows} | ${row.dependency_reviews_completed} |`).join('\n');
  return `# Package 177 OpenIntro Numeracy Normalization Mapping Gate Dependency Matrix

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Parent frontier index: \`${artifact.parent_artifacts.normalization_mapping_gate_frontier_index}\`

## Purpose

This is a blocked-dependency matrix for the OpenIntro IMS numeracy normalization-mapping lane. It records \`${g.openintro_numeracy_mapping_gate_dependency_rows}\` dependency rows and keeps every future action blocked until later dated returns and completed preconditions exist.

## Gate State

- Dependency rows: \`${g.openintro_numeracy_mapping_gate_dependency_rows}\`
- Dependency reviews / unblocked future actions: \`0 / 0\`
- Mapping review returns / decisions / authorizations / activations: \`0 / 0 / 0 / 0\`
- Evidence pointers/values recorded: \`0 / 0\`
- Actual source routes confirmed: \`0\`
- Source text or excerpt files: \`0\`
- Source text/excerpts/tables/figures/datasets copied: \`0\`
- Translations/proposed forms/accepted surfaces: \`0 / 0 / 0\`
- Translation/publication/constructed-surface/pilot ready: \`false / false / false / false\`

## Future Action Summary

| Row | Future action | Dependency rows | Allowed now | Unblocked |
| --- | --- | ---: | ---: | ---: |
${actionRows}

## Dependency Type Summary

| Row | Dependency type | Dependency rows | Reviews completed |
| --- | --- | ---: | ---: |
${dependencyRows}

## Boundary

This artifact contains no source prose, source excerpts, source tables, figures, datasets, source URLs, translations, proposed constructed-language forms, accepted surfaces, owner contacts, actual route confirmations, return intake, mapping authorizations, active mappings, remote actions, legal advice, or readiness claims.
`;
}

function buildArtifactCsv(artifact) {
  const columns = [
    'openintro_numeracy_mapping_gate_dependency_row_id',
    'future_action',
    'future_artifact_pattern',
    'dependency_type',
    'current_blocker',
    'dependency_status',
    'current_evidence_count',
    'current_source_text_files',
    'current_mapping_decisions',
    'current_translations',
    'allowed_now',
    'future_allowed_after',
    'comments_without_source_prose',
    'dependency_cells_filled',
    'dependency_review_completed',
    'future_action_unblocked',
    'source_text_or_excerpt_allowed_now',
    'translation_allowed_now',
    'local_surface_allowed_now',
    'pilot_ready'
  ];
  const lines = [columns.join(',')];
  for (const row of artifact.openintro_numeracy_mapping_gate_dependency_rows) {
    lines.push(columns.map((column) => csvCell(row[column])).join(','));
  }
  return `${lines.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    note_type: 'open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix_note',
    source_artifact: artifactId,
    parent_artifact: parentFile,
    package_order: packageOrder,
    status: 'pointer_only_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: `Package 177 records ${g.openintro_numeracy_mapping_gate_dependency_rows} blocked dependency rows for OpenIntro IMS numeracy normalization mapping.`,
    gate_state: {
      dependency_cells_filled: 0,
      dependency_reviews_completed: 0,
      future_actions_unblocked: 0,
      normalization_mapping_decisions_recorded: 0,
      evidence_values_recorded: 0,
      evidence_source_pointers_recorded: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_excerpts_copied: 0,
      translated_passages: 0,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      readiness_claims: 0
    },
    no_remote_action_by_this_note: true
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 177 OpenIntro Numeracy Normalization Mapping Gate Dependency Matrix Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 177 records \`${g.openintro_numeracy_mapping_gate_dependency_rows}\` blocked dependency rows for future OpenIntro IMS numeracy normalization-mapping work.

Zero gates: \`0\` dependency reviews completed, \`0\` future actions unblocked, \`0\` review returns, \`0\` decisions, \`0\` mapping authorizations, \`0\` active mappings, \`0\` evidence values or pointers recorded, \`0\` actual source routes confirmed, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: dependency matrix only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, active mapping, actual route record, source-owner contact, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
  const packageRow = {
    order: packageOrder,
    role: 'open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix',
    artifact: artifactId,
    current_use: `${g.openintro_numeracy_mapping_gate_dependency_rows} dependency rows; ${g.mapping_gate_dependency_action_summary_rows} action summaries; 0 unblocked actions, 0 decisions, 0 mappings, 0 evidence, 0 source text, 0 translations, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_openintro_numeracy_normalization_mapping_gate_dependency_rows: g.openintro_numeracy_mapping_gate_dependency_rows,
    current_openintro_numeracy_future_actions_unblocked: 0,
    current_openintro_numeracy_normalization_mapping_decisions_recorded: 0,
    current_openintro_numeracy_evidence_values_recorded: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_using_dependency_matrix_only_no_returns_no_decisions_no_mappings_no_evidence_no_source_text_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation OpenIntro numeracy normalization mapping gate dependency matrix',
    route: artifactId,
    license_status_to_recheck: 'dependency_matrix_only_recheck_completed_mapping_preconditions_and_dated_returns_before_any_return_intake_mapping_authorization_mapping_decision_evidence_pointer_evidence_value_excerpt_adaptation_translation_or_surface',
    best_translation_use: 'blocked dependency matrix for coordination before any active mapping, evidence return ingestion, source-route acceptance, selected excerpt, local term, translation, or constructed-surface decision',
    candidate_lanes: ['statistics_public_numeracy', 'OpenIntro_IMS', 'data_literacy', 'public_service_numeracy', 'normalization_mapping_dependency_matrix', 'world_family_lane_alignment'],
    priority: 1,
    status: 'dependency_matrix_no_returns_no_decisions_no_authorizations_no_mappings_no_evidence_no_source_text_no_translation_no_forms_no_pilot',
    gate_state: {
      openintro_numeracy_mapping_gate_dependency_rows: g.openintro_numeracy_mapping_gate_dependency_rows,
      future_actions_unblocked: 0,
      normalization_mapping_decisions_recorded: 0,
      evidence_values_recorded: 0,
      evidence_source_pointers_recorded: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      translated_passages: 0,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix: ${artifactId}_${g.openintro_numeracy_mapping_gate_dependency_rows}_dependency_rows_0_unblocked_0_decisions_0_mappings_0_evidence_0_source_text_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_openintro_numeracy_normalization_mapping_gate_dependency_rows: g.openintro_numeracy_mapping_gate_dependency_rows,
    current_openintro_numeracy_future_actions_unblocked: 0,
    current_openintro_numeracy_normalization_mapping_decisions_recorded: 0,
    current_openintro_numeracy_evidence_values_recorded: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    current_openintro_numeracy_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix: ${artifactId}_dependency_matrix_before_any_evidence_returns_actual_routes_terms_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: records ${g.openintro_numeracy_mapping_gate_dependency_rows} blocked OpenIntro IMS numeracy normalization-mapping dependency rows; substantive upload-bound artifact; 0 unblocked actions, 0 decisions, 0 mappings, 0 evidence, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OpenIntro numeracy normalization mapping gate dependency matrix; ${g.openintro_numeracy_mapping_gate_dependency_rows} blocked dependency rows, 0 unblocked actions, 0 decisions, 0 mappings, 0 evidence, 0 source text, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 177: OpenIntro numeracy normalization mapping gate dependency matrix. It records ${g.openintro_numeracy_mapping_gate_dependency_rows} blocked dependency rows while keeping 0 unblocked future actions, 0 returns, 0 decisions, 0 mapping authorizations, 0 active mappings, 0 evidence values, 0 evidence pointers, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation OpenIntro numeracy normalization mapping gate dependency matrix | ${artifactId} | Dependency matrix; ${g.openintro_numeracy_mapping_gate_dependency_rows} rows, 0 unblocked actions, 0 mappings, 0 evidence, 0 source text, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix_artifact: \`${artifactId}\` (${g.openintro_numeracy_mapping_gate_dependency_rows} dependency rows; 0 unblocked actions; 0 decisions; 0 mappings; 0 evidence; 0 source text; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix: \`${artifactId}\`; OpenIntro IMS numeracy dependency matrix, no evidence, source text, excerpts, local terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OpenIntro IMS public numeracy normalization mapping gate dependency matrix; substantive and upload-bound, but not evidence review intake, actual source discovery, source text, translation, constructed form, local authority review, source-owner contact, local term decision, mapping activation, or readiness claim.`);
}

async function rebuildUploadQueueMd(queue) {
  const rows = (queue.queued_items || []).map((item) => `| \`${item.filename}\` | ${titleClass(item.class)} | ${formatNumber(item.bytes)} | \`${item.sha256}\` |`).join('\n');
  const sourcePdfFiles = (queue.summary.source_pdf_files || 0) + (queue.summary.source_image_files || 0);
  const stagingOrder = Array.isArray(queue.staging_order) ? queue.staging_order : [];
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

${stagingOrder.map((step, index) => `${index + 1}. ${step}`).join('\n')}

## Boundary

This is not a manifest update, payload validator update, Git commit claim, remote branch claim, PR update, Zenodo publication, canonical-readiness claim, translation-readiness claim, or secret-storage artifact.
`;
  await writeFile(path.join(outputs, `${uploadQueueFile}.md`), md, 'utf8');
}

async function updateUploadQueue() {
  const upload = await readJson(uploadQueueFile);
  const files = [
    { filename: `${artifactId}.json`, class: 'open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix' },
    { filename: `${artifactId}.md`, class: 'open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix' },
    { filename: `${artifactId}.csv`, class: 'open_translation_openintro_numeracy_normalization_mapping_gate_dependency_matrix' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package177_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package177_coordination_note' },
    { filename: `${noteId}.sha256`, class: 'checksum_sidecar' }
  ];
  const destination = upload.obj.recommended_destination_in_checkout || 'noether-slavic-handoff/20260629/cross-session-coordination/20260702';
  const byFilename = new Map((upload.obj.queued_items || []).map((item) => [item.filename, item]));
  for (const file of files) {
    byFilename.set(file.filename, { filename: file.filename, class: file.class, bytes: 0, sha256: '', future_destination: `${destination}/${file.filename}` });
  }
  const refreshed = [];
  for (const item of byFilename.values()) {
    const data = await readFile(path.join(outputs, item.filename));
    refreshed.push({ ...item, bytes: data.length, sha256: sha256Upper(data), future_destination: item.future_destination || `${destination}/${item.filename}` });
  }
  upload.obj.queued_items = refreshed;
  upload.obj.bandwidth_mode = 'upload_substantive_artifacts_when_checkout_available_no_mobile_plan_deferral';
  upload.obj.user_upload_clarification = '2026-07-03: user clarified that substantive artifacts should always be queued/uploaded when a staging path exists; do not suppress them because of mobile-plan or bandwidth wording.';
  upload.obj.package177_upload_queue_update = {
    captured_utc: '2026-07-03T14:32:00Z',
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
  const step = 'Stage package 177 OpenIntro numeracy normalization mapping gate dependency matrix artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.openintro_numeracy_mapping_gate_dependency_rows !== artifact.validation_snapshot.expected_dependency_rows) failures.push('dependency_rows_mismatch');
  if (g.mapping_gate_dependency_action_summary_rows !== artifact.validation_snapshot.expected_action_summary_rows) failures.push('action_summary_rows_mismatch');
  if (g.mapping_gate_dependency_type_summary_rows !== artifact.validation_snapshot.expected_dependency_type_summary_rows) failures.push('dependency_type_summary_rows_mismatch');
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.openintro_numeracy_mapping_gate_dependency_rows) {
    if (
      row.current_evidence_count !== 0 ||
      row.current_source_text_files !== 0 ||
      row.current_mapping_decisions !== 0 ||
      row.current_translations !== 0 ||
      row.allowed_now ||
      row.comments_without_source_prose !== null ||
      row.dependency_cells_filled !== 0 ||
      row.dependency_review_completed ||
      row.future_action_unblocked ||
      row.source_text_or_excerpt_allowed_now ||
      row.translation_allowed_now ||
      row.local_surface_allowed_now ||
      row.pilot_ready
    ) {
      failures.push(`open_dependency_row_${row.openintro_numeracy_mapping_gate_dependency_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentFile)).obj;
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
  bandwidth_mode: upload.bandwidth_mode,
  source_text_or_excerpt_files: upload.summary?.source_text_or_excerpt_files,
  openintro_numeracy_mapping_gate_dependency_rows: artifact.gate_state.openintro_numeracy_mapping_gate_dependency_rows,
  mapping_gate_dependency_action_summary_rows: artifact.gate_state.mapping_gate_dependency_action_summary_rows,
  mapping_gate_dependency_type_summary_rows: artifact.gate_state.mapping_gate_dependency_type_summary_rows,
  future_actions_unblocked: artifact.gate_state.future_actions_unblocked,
  normalization_mapping_decisions_recorded: artifact.gate_state.normalization_mapping_decisions_recorded,
  evidence_values_recorded: artifact.gate_state.evidence_values_recorded,
  source_text_copied: artifact.gate_state.source_text_copied,
  translated_passages: artifact.gate_state.translated_passages,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
