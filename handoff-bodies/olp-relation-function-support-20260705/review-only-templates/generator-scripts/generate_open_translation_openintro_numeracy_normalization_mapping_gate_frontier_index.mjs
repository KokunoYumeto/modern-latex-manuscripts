import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_NORMALIZATION_MAPPING_GATE_FRONTIER_INDEX_20260703T141500Z';
const noteId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_NORMALIZATION_MAPPING_GATE_FRONTIER_INDEX_NOTE_20260703T141600Z';
const generatedUtc = '2026-07-03T14:15:00Z';
const noteGeneratedUtc = '2026-07-03T14:16:00Z';
const packageOrder = 176;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-OPENINTRO-NUMERACY-NORMALIZATION-MAPPING-GATE-FRONTIER-INDEX-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentFile = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_NORMALIZATION_MAPPING_DECISION_REVIEW_RETURN_LEDGER_TEMPLATE_20260703T140000Z';

const frontierMinOrder = 159;
const frontierMaxOrder = 175;

const zeroGateKeys = [
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

function buildFrontierPackageRows(packageIndex) {
  return (packageIndex.current_package_order || [])
    .filter((row) => row.order >= frontierMinOrder && row.order <= frontierMaxOrder)
    .map((row) => ({
      openintro_numeracy_frontier_package_row_id: `OI-NUM-FRONTIER-PKG-${String(row.order).padStart(3, '0')}`,
      package_order: row.order,
      role: row.role,
      artifact: row.artifact,
      current_use_without_source_prose: row.current_use,
      frontier_status: row.order === frontierMaxOrder ? 'current_frontier_parent' : 'upstream_control_package',
      source_text_included: false,
      evidence_values_recorded: 0,
      mappings_recorded: 0,
      translations_recorded: 0,
      readiness_claim: false
    }));
}

function buildGateProfileRows(parent) {
  return [
    ['mapping_decision_review_returns', parent.gate_state.mapping_decision_review_returns_received, 'blocked_until_completed_mapping_preconditions_and_dated_returns'],
    ['mapping_decisions', parent.gate_state.normalization_mapping_decisions_recorded, 'blocked_until_completed_mapping_preconditions'],
    ['mapping_authorizations', parent.gate_state.normalization_mapping_authorizations_recorded, 'blocked_until_completed_mapping_preconditions'],
    ['status_code_activations', parent.gate_state.normalization_status_codes_activated, 'blocked_until_later_mapping_artifact'],
    ['evidence_values_or_pointers', parent.gate_state.evidence_values_recorded + parent.gate_state.evidence_source_pointers_recorded, 'blocked_until_valid_return_intake_without_source_prose'],
    ['source_text_or_excerpts', parent.gate_state.source_text_copied + parent.gate_state.source_excerpts_copied, 'not_present_and_not_allowed_in_this_frontier_index'],
    ['translation_or_surfaces', parent.gate_state.translated_passages + parent.gate_state.proposed_bridge_lexemes + parent.gate_state.accepted_bridge_surfaces, 'blocked_until_later_source_and_language_artifacts'],
    ['readiness', parent.gate_state.pilot_ready ? 1 : 0, 'false_no_pilot_publication_translation_or_constructed_surface_readiness']
  ].map(([gate_name, current_count, gate_status], index) => ({
    openintro_numeracy_frontier_gate_profile_row_id: `OI-NUM-FRONTIER-GATE-${String(index + 1).padStart(3, '0')}`,
    gate_name,
    current_count,
    gate_status,
    source_text_included: false,
    readiness_claim: false
  }));
}

function buildArtifact(packageIndex, parent, upload) {
  const packageRows = buildFrontierPackageRows(packageIndex);
  const gateRows = buildGateProfileRows(parent);
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'frontier_index_only_no_returns_no_decisions_no_mappings_no_evidence_no_source_text_no_translation_no_readiness',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Index the current OpenIntro IMS numeracy normalization-mapping frontier so other sessions can find the latest gated state without duplicating work or crossing into returns, mapping decisions, evidence, source text, translation, constructed surfaces, or readiness claims.',
    parent_artifacts: {
      current_frontier_parent: parent.artifact_id,
      package_order_parent: frontierMaxOrder,
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
      parent_mapping_decision_review_return_rows: parent.gate_state.openintro_numeracy_normalization_mapping_decision_review_return_rows,
      parent_mapping_decision_review_returns_received: parent.gate_state.mapping_decision_review_returns_received,
      parent_mapping_decision_rows_reviewed: parent.gate_state.mapping_decision_rows_reviewed,
      parent_mapping_authorizations_recorded: parent.gate_state.normalization_mapping_authorizations_recorded,
      parent_mapping_decisions_recorded: parent.gate_state.normalization_mapping_decisions_recorded,
      parent_evidence_values_recorded: parent.gate_state.evidence_values_recorded,
      parent_source_text_copied: parent.gate_state.source_text_copied,
      parent_pilot_ready: parent.gate_state.pilot_ready
    },
    upload_queue_snapshot_before_package176: {
      queued_files: upload.summary?.queued_files,
      queued_bytes: upload.summary?.queued_bytes,
      bandwidth_mode: upload.bandwidth_mode,
      source_text_or_excerpt_files: upload.summary?.source_text_or_excerpt_files
    },
    openintro_numeracy_frontier_package_rows: packageRows,
    openintro_numeracy_frontier_gate_profile_rows: gateRows,
    gate_state: {
      openintro_numeracy_frontier_package_rows: packageRows.length,
      openintro_numeracy_frontier_gate_profile_rows: gateRows.length,
      frontier_package_order_min: frontierMinOrder,
      frontier_package_order_max_parent: frontierMaxOrder,
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
      expected_frontier_package_rows: frontierMaxOrder - frontierMinOrder + 1,
      expected_frontier_gate_profile_rows: 8,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_NORMALIZATION_MAPPING_DECISION_REVIEW_RETURN_LEDGER_WITH_RETURNS_<timestamp>_only_after_completed_mapping_preconditions',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_NORMALIZATION_MAPPING_DECISION_LEDGER_WITH_DECISIONS_<timestamp>_only_after_completed_mapping_preconditions',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_REVIEW_RETURN_INTAKE_NORMALIZATION_TAXONOMY_WITH_MAPPINGS_<timestamp>_only_after_completed_mapping_preconditions'
    ],
    decision: 'Package 176 is a frontier index only. It records package/gate metadata and queue placement, but no review returns, no decisions, no mapping authorizations, no active mappings, no evidence pointers, no evidence values, no source text, no excerpts, no translations, no constructed forms, and no readiness claims.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const packageRows = artifact.openintro_numeracy_frontier_package_rows.map((row) => `| ${row.package_order} | \`${row.artifact}\` | ${row.role} | ${row.frontier_status} |`).join('\n');
  const gateRows = artifact.openintro_numeracy_frontier_gate_profile_rows.map((row) => `| ${row.gate_name} | ${row.current_count} | ${row.gate_status} |`).join('\n');
  return `# Package 176 OpenIntro Numeracy Normalization Mapping Gate Frontier Index

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Current frontier parent: \`${artifact.parent_artifacts.current_frontier_parent}\`

## Purpose

This is a frontier index for the OpenIntro IMS numeracy normalization-mapping lane. It records package and gate metadata only, so other sessions can locate the current state without duplicating work or crossing into review returns, mapping decisions, source evidence, source text, translation, constructed surfaces, or readiness claims.

## Gate State

- Frontier package rows: \`${g.openintro_numeracy_frontier_package_rows}\`
- Gate profile rows: \`${g.openintro_numeracy_frontier_gate_profile_rows}\`
- Mapping review returns / decisions / authorizations / activations: \`0 / 0 / 0 / 0\`
- Evidence pointers/values recorded: \`0 / 0\`
- Actual source routes confirmed: \`0\`
- Source text or excerpt files: \`0\`
- Source text/excerpts/tables/figures/datasets copied: \`0\`
- Translations/proposed forms/accepted surfaces: \`0 / 0 / 0\`
- Translation/publication/constructed-surface/pilot ready: \`false / false / false / false\`

## Frontier Packages

| Order | Artifact | Role | Status |
| ---: | --- | --- | --- |
${packageRows}

## Gate Profile

| Gate | Current count | Status |
| --- | ---: | --- |
${gateRows}

## Boundary

This artifact contains no source prose, source excerpts, source tables, figures, datasets, source URLs, translations, proposed constructed-language forms, accepted surfaces, owner contacts, actual route confirmations, return intake, mapping authorizations, active mappings, remote actions, legal advice, or readiness claims.
`;
}

function buildArtifactCsv(artifact) {
  const columns = [
    'openintro_numeracy_frontier_package_row_id',
    'package_order',
    'role',
    'artifact',
    'current_use_without_source_prose',
    'frontier_status',
    'source_text_included',
    'evidence_values_recorded',
    'mappings_recorded',
    'translations_recorded',
    'readiness_claim'
  ];
  const lines = [columns.join(',')];
  for (const row of artifact.openintro_numeracy_frontier_package_rows) {
    lines.push(columns.map((column) => csvCell(row[column])).join(','));
  }
  return `${lines.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    note_type: 'open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index_note',
    source_artifact: artifactId,
    parent_artifact: parentFile,
    package_order: packageOrder,
    status: 'pointer_only_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: `Package 176 indexes ${g.openintro_numeracy_frontier_package_rows} frontier package rows and ${g.openintro_numeracy_frontier_gate_profile_rows} gate profile rows.`,
    gate_state: {
      mapping_decision_review_returns_received: 0,
      normalization_mapping_decisions_recorded: 0,
      normalization_mapping_authorizations_recorded: 0,
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
  return `# Package 176 OpenIntro Numeracy Normalization Mapping Gate Frontier Index Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 176 records \`${g.openintro_numeracy_frontier_package_rows}\` frontier package rows and \`${g.openintro_numeracy_frontier_gate_profile_rows}\` gate profile rows for the OpenIntro IMS numeracy normalization-mapping lane.

Zero gates: \`0\` review returns, \`0\` decisions, \`0\` mapping authorizations, \`0\` active mappings, \`0\` evidence values or pointers recorded, \`0\` actual source routes confirmed, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: frontier index only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, active mapping, actual route record, source-owner contact, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index',
    artifact: artifactId,
    current_use: `${g.openintro_numeracy_frontier_package_rows} frontier package rows; ${g.openintro_numeracy_frontier_gate_profile_rows} gate profile rows; 0 returns, 0 decisions, 0 mappings, 0 evidence, 0 source text, 0 translations, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_openintro_numeracy_normalization_mapping_gate_frontier_index_rows: g.openintro_numeracy_frontier_package_rows,
    current_openintro_numeracy_normalization_mapping_decisions_recorded: 0,
    current_openintro_numeracy_evidence_values_recorded: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_using_frontier_index_only_no_returns_no_decisions_no_mappings_no_evidence_no_source_text_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation OpenIntro numeracy normalization mapping gate frontier index',
    route: artifactId,
    license_status_to_recheck: 'frontier_index_only_recheck_completed_mapping_preconditions_before_any_return_intake_mapping_authorization_mapping_decision_evidence_pointer_evidence_value_excerpt_adaptation_translation_or_surface',
    best_translation_use: 'frontier index for coordination before any active mapping, evidence return ingestion, source-route acceptance, selected excerpt, local term, translation, or constructed-surface decision',
    candidate_lanes: ['statistics_public_numeracy', 'OpenIntro_IMS', 'data_literacy', 'public_service_numeracy', 'normalization_mapping_frontier_index', 'world_family_lane_alignment'],
    priority: 1,
    status: 'frontier_index_no_returns_no_decisions_no_authorizations_no_mappings_no_evidence_no_source_text_no_translation_no_forms_no_pilot',
    gate_state: {
      openintro_numeracy_frontier_package_rows: g.openintro_numeracy_frontier_package_rows,
      openintro_numeracy_frontier_gate_profile_rows: g.openintro_numeracy_frontier_gate_profile_rows,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index: ${artifactId}_${g.openintro_numeracy_frontier_package_rows}_frontier_rows_0_decisions_0_mappings_0_evidence_0_source_text_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_openintro_numeracy_normalization_mapping_gate_frontier_index_rows: g.openintro_numeracy_frontier_package_rows,
    current_openintro_numeracy_normalization_mapping_decisions_recorded: 0,
    current_openintro_numeracy_evidence_values_recorded: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    current_openintro_numeracy_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index: ${artifactId}_frontier_index_before_any_evidence_returns_actual_routes_terms_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: indexes ${g.openintro_numeracy_frontier_package_rows} OpenIntro IMS numeracy normalization-mapping frontier package rows; substantive upload-bound artifact; 0 returns, 0 decisions, 0 mappings, 0 evidence, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OpenIntro numeracy normalization mapping gate frontier index; ${g.openintro_numeracy_frontier_package_rows} frontier package rows, ${g.openintro_numeracy_frontier_gate_profile_rows} gate profile rows, 0 decisions, 0 mappings, 0 evidence, 0 source text, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 176: OpenIntro numeracy normalization mapping gate frontier index. It records ${g.openintro_numeracy_frontier_package_rows} frontier package rows and ${g.openintro_numeracy_frontier_gate_profile_rows} gate profile rows while keeping 0 returns, 0 decisions, 0 mapping authorizations, 0 active mappings, 0 evidence values, 0 evidence pointers, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation OpenIntro numeracy normalization mapping gate frontier index | ${artifactId} | Frontier index; ${g.openintro_numeracy_frontier_package_rows} package rows, 0 mappings, 0 evidence, 0 source text, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index_artifact: \`${artifactId}\` (${g.openintro_numeracy_frontier_package_rows} frontier package rows; 0 decisions; 0 mappings; 0 evidence; 0 source text; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index: \`${artifactId}\`; OpenIntro IMS numeracy frontier index, no evidence, source text, excerpts, local terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OpenIntro IMS public numeracy normalization mapping gate frontier index; substantive and upload-bound, but not evidence review intake, actual source discovery, source text, translation, constructed form, local authority review, source-owner contact, local term decision, mapping activation, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index' },
    { filename: `${artifactId}.md`, class: 'open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index' },
    { filename: `${artifactId}.csv`, class: 'open_translation_openintro_numeracy_normalization_mapping_gate_frontier_index' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package176_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package176_coordination_note' },
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
  upload.obj.package176_upload_queue_update = {
    captured_utc: '2026-07-03T14:17:00Z',
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
  const step = 'Stage package 176 OpenIntro numeracy normalization mapping gate frontier index artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.openintro_numeracy_frontier_package_rows !== artifact.validation_snapshot.expected_frontier_package_rows) failures.push('frontier_package_rows_mismatch');
  if (g.openintro_numeracy_frontier_gate_profile_rows !== artifact.validation_snapshot.expected_frontier_gate_profile_rows) failures.push('frontier_gate_rows_mismatch');
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.openintro_numeracy_frontier_package_rows) {
    if (row.source_text_included || row.evidence_values_recorded !== 0 || row.mappings_recorded !== 0 || row.translations_recorded !== 0 || row.readiness_claim) {
      failures.push(`frontier_row_open_${row.openintro_numeracy_frontier_package_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const packageIndex = (await readJson(packageIndexFile)).obj;
const parent = (await readJson(parentFile)).obj;
const upload = (await readJson(uploadQueueFile)).obj;
const artifact = buildArtifact(packageIndex, parent, upload);
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
const updatedPackageIndex = (await readJson(packageIndexFile)).obj;
const queue = (await readJson(queueFile)).obj;
const updatedUpload = (await readJson(uploadQueueFile)).obj;

console.log(JSON.stringify({
  ok: true,
  artifact_id: artifactId,
  note_id: noteId,
  package_order_length: updatedPackageIndex.current_package_order?.length,
  queue_candidate_sources: queue.candidate_sources?.length,
  upload_queue_files: updatedUpload.summary?.queued_files,
  upload_queue_bytes: updatedUpload.summary?.queued_bytes,
  bandwidth_mode: updatedUpload.bandwidth_mode,
  source_text_or_excerpt_files: updatedUpload.summary?.source_text_or_excerpt_files,
  openintro_numeracy_frontier_package_rows: artifact.gate_state.openintro_numeracy_frontier_package_rows,
  openintro_numeracy_frontier_gate_profile_rows: artifact.gate_state.openintro_numeracy_frontier_gate_profile_rows,
  mapping_decision_review_returns_received: artifact.gate_state.mapping_decision_review_returns_received,
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
