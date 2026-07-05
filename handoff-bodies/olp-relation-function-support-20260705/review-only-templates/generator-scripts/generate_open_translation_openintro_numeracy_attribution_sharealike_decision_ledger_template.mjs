import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_ATTRIBUTION_SHAREALIKE_DECISION_LEDGER_TEMPLATE_20260703T104500Z';
const noteId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_ATTRIBUTION_SHAREALIKE_DECISION_LEDGER_TEMPLATE_NOTE_20260703T104600Z';
const generatedUtc = '2026-07-03T10:45:00Z';
const noteGeneratedUtc = '2026-07-03T10:46:00Z';
const packageOrder = 162;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-OPENINTRO-NUMERACY-ATTRIBUTION-SHAREALIKE-DECISION-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentReturnFile = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_POLICY_REVIEW_RETURN_LEDGER_TEMPLATE_20260703T103000Z';
const parentPolicyFile = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SOURCE_COORDINATE_POLICY_SHEET_20260703T101500Z';

const blankDecisionFields = [
  'decision_date',
  'reviewer_route_or_role',
  'parent_return_row_id_confirmed',
  'source_route_identity_decision',
  'license_route_decision',
  'attribution_credit_decision',
  'change_notice_decision',
  'share_alike_compatibility_decision',
  'table_figure_dataset_reuse_decision',
  'translation_adaptation_notice_decision',
  'next_allowed_artifact',
  'comments_without_source_prose'
];

const zeroGateKeys = [
  'attribution_sharealike_decisions_recorded',
  'decision_fields_filled',
  'policy_review_returns_received',
  'policy_reviews_completed',
  'coordinate_scans_authorized',
  'source_text_capture_authorized',
  'excerpt_selections_authorized',
  'source_text_or_excerpt_files_created',
  'source_text_copied',
  'source_definitions_copied',
  'source_examples_copied',
  'source_passages_selected',
  'source_tables_copied',
  'source_figures_copied',
  'source_datasets_copied',
  'exact_line_spans_selected',
  'candidate_line_ranges_selected',
  'translated_passages',
  'proposed_bridge_lexemes',
  'proposed_bridge_morphemes',
  'proposed_bridge_syntax_rules',
  'proposed_bridge_display_surfaces',
  'accepted_bridge_surfaces',
  'accepted_local_language_terms',
  'reviewer_returns_ingested',
  'license_rechecks_completed',
  'attribution_sidecars_created',
  'change_notices_created',
  'sharealike_adaptation_notices_created',
  'pilot_ready_claims'
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

function buildDecisionRows(parentReturn) {
  return parentReturn.openintro_policy_review_return_rows.map((row, index) => ({
    openintro_attribution_sharealike_decision_row_id: `OI-ATTR-SA-DECISION-${String(index + 1).padStart(3, '0')}`,
    parent_return_row_id: row.openintro_policy_review_return_row_id,
    parent_policy_row_id: row.parent_policy_row_id,
    source_family: row.source_family,
    source_group: row.source_group,
    group_type: row.group_type,
    policy_class: row.policy_class,
    inherited_license_or_permission_gate_required: row.inherited_license_or_permission_gate_required,
    inherited_attribution_sidecar_required: row.inherited_attribution_sidecar_required,
    inherited_table_figure_dataset_policy_required: row.inherited_table_figure_dataset_policy_required,
    inherited_coordinate_scan_candidate_after_review: row.inherited_coordinate_scan_candidate_after_review,
    blank_decision_fields: blankDecisionFields,
    decision_date: null,
    reviewer_route_or_role: null,
    parent_return_row_id_confirmed: null,
    source_route_identity_decision: null,
    license_route_decision: null,
    attribution_credit_decision: null,
    change_notice_decision: null,
    share_alike_compatibility_decision: null,
    table_figure_dataset_reuse_decision: null,
    translation_adaptation_notice_decision: null,
    next_allowed_artifact: null,
    comments_without_source_prose: null,
    decision_fields_filled: 0,
    attribution_sharealike_decision_recorded: false,
    source_route_identity_accepted_after_decision: false,
    license_route_accepted_after_decision: false,
    attribution_sidecar_authorized_after_decision: false,
    change_notice_authorized_after_decision: false,
    sharealike_adaptation_notice_authorized_after_decision: false,
    table_figure_dataset_reuse_authorized_after_decision: false,
    coordinate_scan_authorized_after_decision: false,
    source_text_capture_authorized_after_decision: false,
    excerpt_selection_authorized_after_decision: false,
    translation_authorized_after_decision: false,
    constructed_surface_authorized_after_decision: false,
    still_locked_reason: 'blank_attribution_sharealike_decision_template_no_decision_no_notice_no_scan_no_source_text'
  }));
}

function buildDecisionClassSummaryRows(decisionRows) {
  const map = new Map();
  for (const row of decisionRows) {
    if (!map.has(row.policy_class)) {
      map.set(row.policy_class, {
        openintro_attribution_sharealike_class_summary_row_id: `OI-ATTR-SA-CLASS-${String(map.size + 1).padStart(2, '0')}`,
        policy_class: row.policy_class,
        decision_rows_allocated: 0,
        inherited_license_gate_rows: 0,
        inherited_attribution_sidecar_rows: 0,
        inherited_table_figure_dataset_policy_rows: 0,
        inherited_candidate_after_review_rows: 0,
        attribution_sharealike_decisions_recorded: 0,
        attribution_sidecars_created: 0,
        change_notices_created: 0,
        coordinate_scans_authorized: 0,
        source_text_capture_authorized: 0,
        excerpt_selections_authorized: 0
      });
    }
    const entry = map.get(row.policy_class);
    entry.decision_rows_allocated += 1;
    if (row.inherited_license_or_permission_gate_required) entry.inherited_license_gate_rows += 1;
    if (row.inherited_attribution_sidecar_required) entry.inherited_attribution_sidecar_rows += 1;
    if (row.inherited_table_figure_dataset_policy_required) entry.inherited_table_figure_dataset_policy_rows += 1;
    if (row.inherited_coordinate_scan_candidate_after_review) entry.inherited_candidate_after_review_rows += 1;
  }
  return [...map.values()].sort((a, b) => b.decision_rows_allocated - a.decision_rows_allocated || a.policy_class.localeCompare(b.policy_class));
}

function buildArtifact(parentReturn, parentPolicy) {
  const decisionRows = buildDecisionRows(parentReturn);
  const classSummaryRows = buildDecisionClassSummaryRows(decisionRows);
  const blankDecisionCells = decisionRows.length * blankDecisionFields.length;

  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'openintro_numeracy_attribution_sharealike_decision_ledger_template_blank_no_decisions_no_notices_no_scans_no_source_text_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Create a blank attribution/share-alike decision ledger template for OpenIntro IMS numeracy policy rows, preserving the places where source-route identity, license route, attribution, change notice, share-alike compatibility, table/figure/dataset reuse, and translation/adaptation notices would be decided later without recording any decisions or authorizing source text, excerpts, translations, or constructed forms.',
    parent_artifacts: [
      parentReturnFile,
      parentPolicyFile,
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_METADATA_INVENTORY_SCAN_START_20260703T100000Z',
      'OPENINTRO_NUMERACY_PUBLIC_SERVICE_SOURCE_MINI_SHELF_20260629T194849Z',
      'OPENINTRO_NUMERACY_EXACT_EDITION_CAPTURE_20260629T200225Z',
      'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z'
    ],
    boundary: {
      artifact_is: [
        'blank attribution/share-alike decision ledger template',
        'one decision row per package 161 return row',
        'future source-route, license, attribution, change-notice, share-alike, and file-policy decision scaffold'
      ],
      artifact_is_not: [
        'license decision',
        'attribution sidecar',
        'change notice',
        'share-alike adaptation notice',
        'source-route acceptance',
        'coordinate scan authorization',
        'source text capture authorization',
        'source excerpt selection',
        'translation draft',
        'constructed-language form proposal',
        'pilot or publication readiness claim'
      ],
      fill_rule: 'No decision fields are filled here. Any future decision must be dated, route-labeled, and recorded in a separate return or decision artifact without copying source prose.',
      promotion_requires: [
        'dated attribution/share-alike decision return',
        'source-route identity decision',
        'license, attribution, change-note, and share-alike decision',
        'file-level table, figure, dataset, and image policy where needed',
        'separate coordinate scan artifact',
        'separate selected-excerpt sidecar before any translation or adaptation'
      ]
    },
    inherited_parent_counts: {
      parent_policy_review_return_rows: parentReturn.gate_state.openintro_policy_review_return_rows,
      parent_source_coordinate_policy_rows: parentPolicy.gate_state.openintro_numeracy_source_coordinate_policy_rows,
      parent_license_or_permission_gate_required_rows: parentPolicy.gate_state.license_or_permission_gate_required_rows,
      parent_attribution_sidecar_required_rows: parentPolicy.gate_state.attribution_sidecar_required_rows,
      parent_table_figure_dataset_policy_required_rows: parentPolicy.gate_state.table_figure_dataset_policy_required_rows,
      parent_candidate_after_review_rows: parentPolicy.gate_state.coordinate_scan_candidate_after_review_rows
    },
    blank_decision_fields: blankDecisionFields,
    openintro_attribution_sharealike_decision_rows: decisionRows,
    openintro_attribution_sharealike_class_summary_rows: classSummaryRows,
    gate_state: {
      openintro_attribution_sharealike_decision_rows: decisionRows.length,
      parent_policy_review_return_rows: parentReturn.gate_state.openintro_policy_review_return_rows,
      openintro_attribution_sharealike_class_summary_rows: classSummaryRows.length,
      blank_decision_fields_per_row: blankDecisionFields.length,
      blank_decision_field_cells_allocated: blankDecisionCells,
      attribution_sharealike_decisions_recorded: 0,
      decision_fields_filled: 0,
      policy_review_returns_received: 0,
      policy_reviews_completed: 0,
      coordinate_scans_authorized: 0,
      source_text_capture_authorized: 0,
      excerpt_selections_authorized: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_definitions_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      source_tables_copied: 0,
      source_figures_copied: 0,
      source_datasets_copied: 0,
      exact_line_spans_selected: 0,
      candidate_line_ranges_selected: 0,
      translated_passages: 0,
      proposed_bridge_lexemes: 0,
      proposed_bridge_morphemes: 0,
      proposed_bridge_syntax_rules: 0,
      proposed_bridge_display_surfaces: 0,
      accepted_bridge_surfaces: 0,
      accepted_local_language_terms: 0,
      reviewer_returns_ingested: 0,
      license_rechecks_completed: 0,
      attribution_sidecars_created: 0,
      change_notices_created: 0,
      sharealike_adaptation_notices_created: 0,
      pilot_ready_claims: 0,
      publication_ready: false,
      translation_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      expected_openintro_attribution_sharealike_decision_rows: parentReturn.gate_state.openintro_policy_review_return_rows,
      expected_blank_decision_fields_per_row: blankDecisionFields.length,
      expected_blank_decision_field_cells_allocated: blankDecisionCells,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_ATTRIBUTION_SHAREALIKE_DECISION_LEDGER_WITH_RETURNS_<timestamp>_only_after_dated_decisions',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SELECTED_EXCERPT_SIDECAR_TEMPLATE_<timestamp>_only_after_policy_and_attribution_returns',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_PACKET_SCOPE_REVIEW_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_LANGUAGE_SOURCE_ALIGNMENT_TEMPLATE_<timestamp>'
    ],
    decision: 'Package 162 allocates blank attribution/share-alike decision rows only. It records no decisions, no attribution sidecars, no change notices, no share-alike notices, no scan authorizations, no source text, no excerpts, no translations, no constructed forms, and no readiness claims.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const decisionRows = artifact.openintro_attribution_sharealike_decision_rows.map((row) => `| ${row.openintro_attribution_sharealike_decision_row_id} | ${row.parent_return_row_id} | ${row.source_group} | ${row.policy_class} | ${row.decision_fields_filled} |`).join('\n');
  const classRows = artifact.openintro_attribution_sharealike_class_summary_rows.map((row) => `| ${row.openintro_attribution_sharealike_class_summary_row_id} | ${row.policy_class} | ${row.decision_rows_allocated} | ${row.inherited_license_gate_rows} | ${row.inherited_attribution_sidecar_rows} | ${row.inherited_table_figure_dataset_policy_rows} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Attribution/share-alike decision rows: \`${g.openintro_attribution_sharealike_decision_rows}\`
- Blank decision fields per row: \`${g.blank_decision_fields_per_row}\`
- Blank decision-field cells: \`${g.blank_decision_field_cells_allocated}\`
- Policy-class summary rows: \`${g.openintro_attribution_sharealike_class_summary_rows}\`

## Decision Rows

| Decision row | Parent return row | Source group | Policy class | Filled fields |
| --- | --- | --- | --- | ---: |
${decisionRows}

## Policy-Class Summary

| Row | Policy class | Decision rows | License rows | Attribution rows | File-policy rows |
| --- | --- | ---: | ---: | ---: | ---: |
${classRows}

## Zero Gates

\`0\` decision fields filled, \`0\` attribution/share-alike decisions recorded, \`0\` attribution sidecars created, \`0\` change notices created, \`0\` share-alike adaptation notices created, \`0\` coordinate scans authorized, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` tables/figures/datasets copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: blank decision-ledger template only. This artifact is not a license decision, attribution sidecar, change notice, share-alike notice, source authorization, excerpt selection, source text capture, translation, constructed-language proposal, publication claim, or pilot claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [
    ['section', 'decision_row_id', 'parent_return_row_id', 'parent_policy_row_id', 'source_group', 'group_type', 'policy_class', 'license_gate', 'attribution_gate', 'file_policy_gate', 'candidate_after_review', 'decision_fields_filled', 'decision_recorded'].map(csvCell).join(',')
  ];
  for (const row of artifact.openintro_attribution_sharealike_decision_rows) {
    rows.push([
      'openintro_attribution_sharealike_decision_row',
      row.openintro_attribution_sharealike_decision_row_id,
      row.parent_return_row_id,
      row.parent_policy_row_id,
      row.source_group,
      row.group_type,
      row.policy_class,
      row.inherited_license_or_permission_gate_required,
      row.inherited_attribution_sidecar_required,
      row.inherited_table_figure_dataset_policy_required,
      row.inherited_coordinate_scan_candidate_after_review,
      row.decision_fields_filled,
      row.attribution_sharealike_decision_recorded
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
    status: 'pointer_only_package162_openintro_numeracy_attribution_sharealike_decision_template_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: 'Package 162 records a blank OpenIntro IMS numeracy attribution/share-alike decision ledger template derived from package 161 return rows.',
    counts: {
      openintro_attribution_sharealike_decision_rows: g.openintro_attribution_sharealike_decision_rows,
      blank_decision_fields_per_row: g.blank_decision_fields_per_row,
      blank_decision_field_cells_allocated: g.blank_decision_field_cells_allocated,
      openintro_attribution_sharealike_class_summary_rows: g.openintro_attribution_sharealike_class_summary_rows
    },
    zero_gates: {
      attribution_sharealike_decisions_recorded: 0,
      decision_fields_filled: 0,
      attribution_sidecars_created: 0,
      change_notices_created: 0,
      sharealike_adaptation_notices_created: 0,
      coordinate_scans_authorized: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_tables_copied: 0,
      source_figures_copied: 0,
      source_datasets_copied: 0,
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
  return `# Package 162 OpenIntro Numeracy Attribution/Share-Alike Decision Template Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 162 records \`${g.openintro_attribution_sharealike_decision_rows}\` blank attribution/share-alike decision rows and \`${g.blank_decision_field_cells_allocated}\` blank decision-field cells for OpenIntro IMS statistics/public numeracy.

Zero gates: \`0\` decision fields filled, \`0\` attribution/share-alike decisions recorded, \`0\` attribution sidecars, \`0\` change notices, \`0\` share-alike notices, \`0\` coordinate scans, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` tables/figures/datasets copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: blank decision-ledger template only. This note makes no commit, push, PR, Zenodo, dispatch, return, decision, notice, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_openintro_numeracy_attribution_sharealike_decision_ledger_template',
    artifact: artifactId,
    current_use: `${g.openintro_attribution_sharealike_decision_rows} blank OpenIntro numeracy attribution/share-alike decision rows; ${g.blank_decision_field_cells_allocated} blank decision-field cells; 0 decisions, 0 notices, 0 source text, 0 excerpts, 0 translations, 0 forms, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_openintro_numeracy_attribution_sharealike_decision_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_openintro_numeracy_attribution_sharealike_decision_rows: g.openintro_attribution_sharealike_decision_rows,
    current_openintro_numeracy_attribution_sharealike_decisions_recorded: 0,
    current_openintro_numeracy_attribution_sidecars_created: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_openintro_numeracy_selected_excerpt_sidecar_or_packet_scope_review_template_only_after_returns_no_source_text_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation OpenIntro numeracy attribution/share-alike decision ledger template',
    route: artifactId,
    license_status_to_recheck: 'blank_decision_template_only_recheck_OpenIntro_IMS_CC_BY_SA_attribution_change_share_alike_file_policy_and_adaptation_notice_returns_before_any_coordinate_scan_excerpt_adaptation_or_translation',
    best_translation_use: 'statistics/public numeracy attribution and share-alike decision scaffold before any selected-excerpt sidecar, packet scope review, local-language reviewer decision, translation, or constructed surface',
    candidate_lanes: [
      'statistics_public_numeracy',
      'OpenIntro_IMS',
      'data_literacy',
      'public_service_numeracy',
      'attribution_share_alike_decision_template',
      'source_coordinate_policy'
    ],
    priority: 1,
    status: 'blank_attribution_sharealike_decision_template_no_decisions_no_notices_no_source_text_no_excerpts_no_translation_no_forms_no_pilot',
    gate_state: {
      openintro_attribution_sharealike_decision_rows: g.openintro_attribution_sharealike_decision_rows,
      blank_decision_field_cells_allocated: g.blank_decision_field_cells_allocated,
      attribution_sharealike_decisions_recorded: 0,
      decision_fields_filled: 0,
      attribution_sidecars_created: 0,
      change_notices_created: 0,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_attribution_sharealike_decision_ledger_template: ${artifactId}_${g.openintro_attribution_sharealike_decision_rows}_blank_decision_rows_0_source_text_0_excerpts_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_openintro_numeracy_attribution_sharealike_decision_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_attribution_sharealike_decision_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_openintro_numeracy_attribution_sharealike_decision_rows: g.openintro_attribution_sharealike_decision_rows,
    current_openintro_numeracy_attribution_sharealike_decisions_recorded: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    current_openintro_numeracy_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_openintro_numeracy_attribution_sharealike_decision_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_openintro_numeracy_attribution_sharealike_decision_ledger_template: ${artifactId}_blank_decision_template_before_any_decisions_notices_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_openintro_numeracy_attribution_sharealike_decision_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: records ${g.openintro_attribution_sharealike_decision_rows} blank OpenIntro IMS numeracy attribution/share-alike decision rows and ${g.blank_decision_field_cells_allocated} blank decision-field cells; substantive upload-bound artifact; 0 decisions, 0 notices, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OpenIntro numeracy attribution/share-alike decision ledger template; ${g.openintro_attribution_sharealike_decision_rows} blank decision rows, ${g.blank_decision_field_cells_allocated} blank decision-field cells, 0 source text, 0 excerpts, 0 notices, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 162: OpenIntro numeracy attribution/share-alike decision ledger template. It records ${g.openintro_attribution_sharealike_decision_rows} blank decision rows and ${g.blank_decision_field_cells_allocated} blank decision-field cells while keeping 0 decisions, 0 notices, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation OpenIntro numeracy attribution/share-alike decision ledger template | ${artifactId} | Blank attribution/share-alike decision template; ${g.openintro_attribution_sharealike_decision_rows} rows, 0 source text, 0 excerpts, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_attribution_sharealike_decision_ledger_template_artifact: \`${artifactId}\` (${g.openintro_attribution_sharealike_decision_rows} blank decision rows; 0 source text; 0 excerpts; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_attribution_sharealike_decision_ledger_template: \`${artifactId}\`; blank OpenIntro IMS numeracy attribution/share-alike decision template, no source text, excerpts, notices, accepted terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OpenIntro IMS public numeracy attribution/share-alike decision ledger template; substantive and upload-bound, but not a source excerpt, table, figure, dataset, translation, constructed form, license clearance, notice, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_openintro_numeracy_attribution_sharealike_decision_ledger_template' },
    { filename: `${artifactId}.md`, class: 'open_translation_openintro_numeracy_attribution_sharealike_decision_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'open_translation_openintro_numeracy_attribution_sharealike_decision_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package162_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package162_coordination_note' },
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
  upload.obj.package162_upload_queue_update = {
    captured_utc: '2026-07-03T10:47:00Z',
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
  const step = 'Stage package 162 OpenIntro numeracy attribution/share-alike decision ledger template artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.openintro_attribution_sharealike_decision_rows !== artifact.validation_snapshot.expected_openintro_attribution_sharealike_decision_rows) failures.push(`decision_rows_mismatch_${g.openintro_attribution_sharealike_decision_rows}`);
  if (g.blank_decision_fields_per_row !== artifact.validation_snapshot.expected_blank_decision_fields_per_row) failures.push(`blank_decision_fields_mismatch_${g.blank_decision_fields_per_row}`);
  if (g.blank_decision_field_cells_allocated !== artifact.validation_snapshot.expected_blank_decision_field_cells_allocated) failures.push(`blank_decision_cells_mismatch_${g.blank_decision_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.openintro_attribution_sharealike_decision_rows) {
    const filled = blankDecisionFields.some((field) => row[field] !== null);
    if (
      filled ||
      row.decision_fields_filled !== 0 ||
      row.attribution_sharealike_decision_recorded ||
      row.source_route_identity_accepted_after_decision ||
      row.license_route_accepted_after_decision ||
      row.attribution_sidecar_authorized_after_decision ||
      row.change_notice_authorized_after_decision ||
      row.sharealike_adaptation_notice_authorized_after_decision ||
      row.table_figure_dataset_reuse_authorized_after_decision ||
      row.coordinate_scan_authorized_after_decision ||
      row.source_text_capture_authorized_after_decision ||
      row.excerpt_selection_authorized_after_decision ||
      row.translation_authorized_after_decision ||
      row.constructed_surface_authorized_after_decision
    ) {
      failures.push(`nonblank_or_open_decision_row_${row.openintro_attribution_sharealike_decision_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parentReturn = (await readJson(parentReturnFile)).obj;
const parentPolicy = (await readJson(parentPolicyFile)).obj;
const artifact = buildArtifact(parentReturn, parentPolicy);
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
  openintro_attribution_sharealike_decision_rows: artifact.gate_state.openintro_attribution_sharealike_decision_rows,
  blank_decision_fields_per_row: artifact.gate_state.blank_decision_fields_per_row,
  blank_decision_field_cells_allocated: artifact.gate_state.blank_decision_field_cells_allocated,
  attribution_sharealike_decisions_recorded: artifact.gate_state.attribution_sharealike_decisions_recorded,
  decision_fields_filled: artifact.gate_state.decision_fields_filled,
  attribution_sidecars_created: artifact.gate_state.attribution_sidecars_created,
  change_notices_created: artifact.gate_state.change_notices_created,
  sharealike_adaptation_notices_created: artifact.gate_state.sharealike_adaptation_notices_created,
  coordinate_scans_authorized: artifact.gate_state.coordinate_scans_authorized,
  source_text_capture_authorized: artifact.gate_state.source_text_capture_authorized,
  excerpt_selections_authorized: artifact.gate_state.excerpt_selections_authorized,
  source_text_copied: artifact.gate_state.source_text_copied,
  source_tables_copied: artifact.gate_state.source_tables_copied,
  source_figures_copied: artifact.gate_state.source_figures_copied,
  source_datasets_copied: artifact.gate_state.source_datasets_copied,
  translated_passages: artifact.gate_state.translated_passages,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
