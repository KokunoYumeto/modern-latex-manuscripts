import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_POLICY_REVIEW_RETURN_LEDGER_TEMPLATE_20260703T103000Z';
const noteId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_POLICY_REVIEW_RETURN_LEDGER_TEMPLATE_NOTE_20260703T103100Z';
const generatedUtc = '2026-07-03T10:30:00Z';
const noteGeneratedUtc = '2026-07-03T10:31:00Z';
const packageOrder = 161;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-OPENINTRO-NUMERACY-POLICY-REVIEW-RETURN-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentPolicyFile = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SOURCE_COORDINATE_POLICY_SHEET_20260703T101500Z';

const blankReturnFields = [
  'return_date',
  'reviewer_route_or_role',
  'parent_policy_row_id_confirmed',
  'policy_class_decision',
  'coordinate_scan_scope_decision',
  'license_attribution_share_alike_decision',
  'table_figure_dataset_policy_decision',
  'source_text_capture_decision',
  'excerpt_selection_decision',
  'packet_or_lane_scope_decision',
  'next_allowed_artifact',
  'local_language_reviewer_route_needed',
  'comments_without_source_prose'
];

const zeroGateKeys = [
  'policy_review_returns_received',
  'return_fields_filled',
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

function parentPolicyRows(parent) {
  return [
    ...(parent.route_class_policy_rows || []),
    ...(parent.exact_route_use_policy_rows || []),
    ...(parent.extension_policy_rows || []),
    ...(parent.packet_slot_policy_rows || []),
    ...(parent.lane_fit_policy_rows || [])
  ];
}

function buildReturnRows(parent) {
  return parentPolicyRows(parent).map((row, index) => ({
    openintro_policy_review_return_row_id: `OI-SCP-RETURN-${String(index + 1).padStart(3, '0')}`,
    parent_policy_row_id: row.policy_row_id,
    parent_summary_row_id: row.parent_summary_row_id || null,
    parent_packet_slot_row_id: row.parent_packet_slot_row_id || null,
    parent_lane_fit_row_id: row.parent_lane_fit_row_id || null,
    source_family: row.source_family,
    source_group: row.source_group,
    group_type: row.group_type,
    policy_class: row.policy_class,
    inherited_coordinate_scan_scope: row.coordinate_scan_scope,
    inherited_coordinate_scan_candidate_after_review: row.coordinate_scan_candidate_after_review,
    inherited_license_or_permission_gate_required: row.license_or_permission_gate_required,
    inherited_attribution_sidecar_required: row.attribution_sidecar_required,
    inherited_table_figure_dataset_policy_required: row.table_figure_dataset_policy_required,
    inherited_metadata_rows: row.metadata_rows,
    inherited_metadata_bytes: row.metadata_bytes,
    inherited_policy_reason: row.why_this_policy_class,
    blank_return_fields: blankReturnFields,
    return_date: null,
    reviewer_route_or_role: null,
    parent_policy_row_id_confirmed: null,
    policy_class_decision: null,
    coordinate_scan_scope_decision: null,
    license_attribution_share_alike_decision: null,
    table_figure_dataset_policy_decision: null,
    source_text_capture_decision: null,
    excerpt_selection_decision: null,
    packet_or_lane_scope_decision: null,
    next_allowed_artifact: null,
    local_language_reviewer_route_needed: null,
    comments_without_source_prose: null,
    return_fields_filled: 0,
    return_received: false,
    policy_review_completed: false,
    coordinate_scan_authorized_after_return: false,
    source_text_capture_authorized_after_return: false,
    excerpt_selection_authorized_after_return: false,
    translation_authorized_after_return: false,
    constructed_surface_authorized_after_return: false,
    still_locked_reason: 'blank_openintro_numeracy_policy_review_return_row_no_dated_return_no_license_decision_no_scan_authorization'
  }));
}

function buildPolicyClassReturnSummaryRows(returnRows) {
  const map = new Map();
  for (const row of returnRows) {
    if (!map.has(row.policy_class)) {
      map.set(row.policy_class, {
        openintro_policy_class_return_summary_row_id: `OI-SCP-RETURN-CLASS-${String(map.size + 1).padStart(2, '0')}`,
        policy_class: row.policy_class,
        return_rows_allocated: 0,
        inherited_metadata_rows: 0,
        inherited_candidate_after_review_rows: 0,
        inherited_license_gate_rows: 0,
        inherited_attribution_sidecar_rows: 0,
        inherited_table_figure_dataset_policy_rows: 0,
        policy_review_returns_received: 0,
        policy_reviews_completed: 0,
        coordinate_scans_authorized: 0,
        source_text_capture_authorized: 0,
        excerpt_selections_authorized: 0
      });
    }
    const entry = map.get(row.policy_class);
    entry.return_rows_allocated += 1;
    entry.inherited_metadata_rows += row.inherited_metadata_rows || 0;
    if (row.inherited_coordinate_scan_candidate_after_review) entry.inherited_candidate_after_review_rows += 1;
    if (row.inherited_license_or_permission_gate_required) entry.inherited_license_gate_rows += 1;
    if (row.inherited_attribution_sidecar_required) entry.inherited_attribution_sidecar_rows += 1;
    if (row.inherited_table_figure_dataset_policy_required) entry.inherited_table_figure_dataset_policy_rows += 1;
  }
  return [...map.values()].sort((a, b) => b.return_rows_allocated - a.return_rows_allocated || a.policy_class.localeCompare(b.policy_class));
}

function buildLaneReturnSummaryRows(parent, returnRows) {
  const lanes = parent.next_policy_artifact_rows || [];
  return lanes.map((lane, index) => ({
    openintro_lane_return_summary_row_id: `OI-SCP-RETURN-LANE-${String(index + 1).padStart(2, '0')}`,
    parent_next_policy_artifact_row_id: lane.next_policy_artifact_row_id,
    lane: lane.lane,
    useful_next_artifact: lane.useful_next_artifact,
    allowed_action_class: lane.allowed_action_class,
    linked_return_rows: returnRows
      .filter((row) => {
        if (lane.lane === 'policy_review_return') return true;
        if (lane.lane === 'license_attribution_share_alike') return row.inherited_license_or_permission_gate_required || row.inherited_attribution_sidecar_required;
        if (lane.lane === 'selected_excerpt_sidecar') return row.inherited_coordinate_scan_candidate_after_review;
        if (lane.lane === 'packet_scope_review') return row.group_type === 'numeracy_packet_slot' || row.group_type === 'numeracy_lane_fit' || row.policy_class.includes('packet');
        if (lane.lane === 'local_language_source_alignment') return row.group_type === 'numeracy_lane_fit' || row.policy_class.includes('lane');
        return false;
      })
      .map((row) => row.openintro_policy_review_return_row_id),
    policy_review_returns_received: 0,
    coordinate_scans_authorized: 0,
    excerpt_selections_authorized: 0,
    source_text_or_excerpt_allowed_now: false,
    translation_allowed_now: false,
    constructed_surface_allowed_now: false
  }));
}

function buildArtifact(parent) {
  const returnRows = buildReturnRows(parent);
  const classSummaryRows = buildPolicyClassReturnSummaryRows(returnRows);
  const laneSummaryRows = buildLaneReturnSummaryRows(parent, returnRows);
  const blankReturnCells = returnRows.length * blankReturnFields.length;

  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'openintro_numeracy_policy_review_return_ledger_template_blank_no_returns_no_scans_no_source_text_no_excerpts_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Create a blank policy-review return ledger for every package 160 OpenIntro IMS numeracy source-coordinate policy row, allowing future dated license, attribution, share-alike, file-policy, packet-scope, and local-review decisions to be ingested separately while keeping all scan, source-text, excerpt, translation, and constructed-surface gates closed.',
    parent_artifacts: [
      parentPolicyFile,
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_METADATA_INVENTORY_SCAN_START_20260703T100000Z',
      'OPEN_TRANSLATION_REVIEW_ONLY_SOURCE_COORDINATE_SCAN_ROUTER_20260703T081500Z',
      'OPENINTRO_NUMERACY_PUBLIC_SERVICE_SOURCE_MINI_SHELF_20260629T194849Z',
      'OPENINTRO_NUMERACY_EXACT_EDITION_CAPTURE_20260629T200225Z',
      'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z'
    ],
    boundary: {
      artifact_is: [
        'blank OpenIntro numeracy policy-review return ledger template',
        'one return row per package 160 policy row',
        'future dated-return intake scaffold for license, attribution, share-alike, file-policy, packet-scope, and local-review decisions'
      ],
      artifact_is_not: [
        'policy return',
        'policy decision',
        'license, attribution, or share-alike clearance',
        'coordinate scan authorization',
        'source text capture authorization',
        'source excerpt selection',
        'table, figure, dataset, definition, or example extraction',
        'translation draft',
        'constructed-language form proposal',
        'pilot or publication readiness claim'
      ],
      fill_rule: 'No return fields are filled here. Future returns must be dated, route-labeled, and ingested in a separate artifact without source prose unless a later policy explicitly allows it.',
      promotion_requires: [
        'dated policy review return',
        'license, attribution, change-note, and share-alike decision',
        'file-level table, figure, dataset, and image policy where needed',
        'separate coordinate scan artifact',
        'separate selected-excerpt sidecar before any translation or adaptation',
        'local-language source alignment or reviewer return before any bridge-language surface'
      ]
    },
    inherited_parent_counts: {
      parent_openintro_numeracy_source_coordinate_policy_rows: parent.gate_state.openintro_numeracy_source_coordinate_policy_rows,
      parent_candidate_after_review_rows: parent.gate_state.coordinate_scan_candidate_after_review_rows,
      parent_license_or_permission_gate_required_rows: parent.gate_state.license_or_permission_gate_required_rows,
      parent_attribution_sidecar_required_rows: parent.gate_state.attribution_sidecar_required_rows,
      parent_table_figure_dataset_policy_required_rows: parent.gate_state.table_figure_dataset_policy_required_rows,
      parent_policy_reviews_completed: parent.gate_state.policy_reviews_completed,
      parent_coordinate_scans_authorized: parent.gate_state.coordinate_scans_authorized
    },
    blank_return_fields: blankReturnFields,
    openintro_policy_review_return_rows: returnRows,
    openintro_policy_class_return_summary_rows: classSummaryRows,
    openintro_lane_return_summary_rows: laneSummaryRows,
    gate_state: {
      openintro_policy_review_return_rows: returnRows.length,
      parent_openintro_numeracy_source_coordinate_policy_rows: parent.gate_state.openintro_numeracy_source_coordinate_policy_rows,
      openintro_policy_class_return_summary_rows: classSummaryRows.length,
      openintro_lane_return_summary_rows: laneSummaryRows.length,
      blank_return_fields_per_row: blankReturnFields.length,
      blank_return_field_cells_allocated: blankReturnCells,
      policy_review_returns_received: 0,
      return_fields_filled: 0,
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
      pilot_ready_claims: 0,
      publication_ready: false,
      translation_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      expected_openintro_policy_review_return_rows: parent.gate_state.openintro_numeracy_source_coordinate_policy_rows,
      expected_blank_return_fields_per_row: blankReturnFields.length,
      expected_blank_return_field_cells_allocated: blankReturnCells,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_POLICY_REVIEW_RETURN_LEDGER_WITH_RETURNS_<timestamp>_only_after_dated_returns',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_ATTRIBUTION_SHAREALIKE_DECISION_LEDGER_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SELECTED_EXCERPT_SIDECAR_TEMPLATE_<timestamp>_only_after_policy_returns',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_PACKET_SCOPE_REVIEW_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_LANGUAGE_SOURCE_ALIGNMENT_TEMPLATE_<timestamp>'
    ],
    decision: 'Package 161 allocates blank OpenIntro numeracy policy-review return rows only. It records no returns, no policy decisions, no scan authorizations, no source text, no excerpts, no translations, no constructed forms, and no readiness claims.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const returnRows = artifact.openintro_policy_review_return_rows.map((row) => `| ${row.openintro_policy_review_return_row_id} | ${row.parent_policy_row_id} | ${row.source_group} | ${row.policy_class} | ${row.return_fields_filled} |`).join('\n');
  const classRows = artifact.openintro_policy_class_return_summary_rows.map((row) => `| ${row.openintro_policy_class_return_summary_row_id} | ${row.policy_class} | ${row.return_rows_allocated} | ${row.inherited_candidate_after_review_rows} | ${row.inherited_license_gate_rows} | ${row.inherited_table_figure_dataset_policy_rows} |`).join('\n');
  const laneRows = artifact.openintro_lane_return_summary_rows.map((row) => `| ${row.openintro_lane_return_summary_row_id} | ${row.lane} | ${row.linked_return_rows.length} | ${row.allowed_action_class} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- OpenIntro policy-review return rows: \`${g.openintro_policy_review_return_rows}\`
- Parent policy rows: \`${g.parent_openintro_numeracy_source_coordinate_policy_rows}\`
- Policy-class return summary rows: \`${g.openintro_policy_class_return_summary_rows}\`
- Lane return summary rows: \`${g.openintro_lane_return_summary_rows}\`
- Blank return fields per row: \`${g.blank_return_fields_per_row}\`
- Blank return-field cells: \`${g.blank_return_field_cells_allocated}\`

## Return Rows

| Return row | Parent policy row | Source group | Policy class | Filled fields |
| --- | --- | --- | --- | ---: |
${returnRows}

## Policy-Class Summary

| Row | Policy class | Return rows | Candidate rows | License rows | File-policy rows |
| --- | --- | ---: | ---: | ---: | ---: |
${classRows}

## Lane Summary

| Row | Lane | Linked return rows | Allowed action class |
| --- | --- | ---: | --- |
${laneRows}

## Zero Gates

\`0\` return fields filled, \`0\` policy-review returns received, \`0\` policy reviews completed, \`0\` coordinate scans authorized, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` tables/figures/datasets copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: blank return-ledger template only. This artifact is not a policy return, source authorization, excerpt selection, source text capture, translation, constructed-language proposal, license clearance, share-alike clearance, publication claim, or pilot claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [
    ['section', 'return_row_id', 'parent_policy_row_id', 'source_group', 'group_type', 'policy_class', 'candidate_after_review', 'license_gate', 'attribution_gate', 'file_policy_gate', 'return_fields_filled', 'return_received'].map(csvCell).join(',')
  ];
  for (const row of artifact.openintro_policy_review_return_rows) {
    rows.push([
      'openintro_policy_review_return_row',
      row.openintro_policy_review_return_row_id,
      row.parent_policy_row_id,
      row.source_group,
      row.group_type,
      row.policy_class,
      row.inherited_coordinate_scan_candidate_after_review,
      row.inherited_license_or_permission_gate_required,
      row.inherited_attribution_sidecar_required,
      row.inherited_table_figure_dataset_policy_required,
      row.return_fields_filled,
      row.return_received
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
    status: 'pointer_only_package161_openintro_numeracy_policy_review_return_ledger_template_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: 'Package 161 records a blank OpenIntro IMS numeracy policy-review return ledger template derived from package 160 policy rows.',
    counts: {
      openintro_policy_review_return_rows: g.openintro_policy_review_return_rows,
      blank_return_fields_per_row: g.blank_return_fields_per_row,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated,
      openintro_policy_class_return_summary_rows: g.openintro_policy_class_return_summary_rows,
      openintro_lane_return_summary_rows: g.openintro_lane_return_summary_rows
    },
    zero_gates: {
      policy_review_returns_received: 0,
      return_fields_filled: 0,
      policy_reviews_completed: 0,
      coordinate_scans_authorized: 0,
      excerpt_selections_authorized: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_tables_copied: 0,
      source_figures_copied: 0,
      source_datasets_copied: 0,
      translated_passages: 0,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      reviewer_returns_ingested: 0,
      readiness_claims: 0
    },
    no_remote_action_by_this_note: true
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 161 OpenIntro Numeracy Policy-Review Return Ledger Template Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 161 records \`${g.openintro_policy_review_return_rows}\` blank policy-review return rows and \`${g.blank_return_field_cells_allocated}\` blank return-field cells for OpenIntro IMS statistics/public numeracy.

Zero gates: \`0\` return fields filled, \`0\` policy-review returns received, \`0\` coordinate scans authorized, \`0\` excerpt selections authorized, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` tables/figures/datasets copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` reviewer returns ingested, \`0\` readiness claims.

Boundary: blank return-ledger template only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_openintro_numeracy_policy_review_return_ledger_template',
    artifact: artifactId,
    current_use: `${g.openintro_policy_review_return_rows} blank OpenIntro numeracy policy-review return rows; ${g.blank_return_field_cells_allocated} blank return-field cells; 0 returns, 0 scans authorized, 0 source text, 0 excerpts, 0 tables/figures/datasets copied, 0 translations, 0 forms, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_openintro_numeracy_policy_review_return_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_openintro_numeracy_policy_review_return_rows: g.openintro_policy_review_return_rows,
    current_openintro_numeracy_policy_review_return_cells: g.blank_return_field_cells_allocated,
    current_openintro_numeracy_policy_review_returns_received: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_openintro_numeracy_attribution_sharealike_decision_template_or_selected_excerpt_sidecar_template_only_after_returns_no_source_text_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation OpenIntro numeracy policy-review return ledger template',
    route: artifactId,
    license_status_to_recheck: 'blank_return_ledger_only_recheck_OpenIntro_IMS_CC_BY_SA_attribution_change_share_alike_and_file_policy_returns_before_any_coordinate_scan_excerpt_adaptation_or_translation',
    best_translation_use: 'statistics/public numeracy policy-review return intake scaffold before any selected-excerpt sidecar, attribution/change notice, local-language reviewer decision, translation, or constructed surface',
    candidate_lanes: [
      'statistics_public_numeracy',
      'OpenIntro_IMS',
      'data_literacy',
      'public_service_numeracy',
      'policy_review_return_template',
      'share_alike_attribution_review'
    ],
    priority: 1,
    status: 'blank_policy_review_return_ledger_template_no_returns_no_scans_no_source_text_no_excerpts_no_tables_figures_datasets_no_translation_no_forms_no_pilot',
    gate_state: {
      openintro_policy_review_return_rows: g.openintro_policy_review_return_rows,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated,
      policy_review_returns_received: 0,
      return_fields_filled: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_tables_copied: 0,
      source_figures_copied: 0,
      source_datasets_copied: 0,
      translated_passages: 0,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_policy_review_return_ledger_template: ${artifactId}_${g.openintro_policy_review_return_rows}_blank_return_rows_0_source_text_0_excerpts_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_openintro_numeracy_policy_review_return_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_policy_review_return_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_openintro_numeracy_policy_review_return_rows: g.openintro_policy_review_return_rows,
    current_openintro_numeracy_policy_review_returns_received: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    current_openintro_numeracy_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_openintro_numeracy_policy_review_return_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_openintro_numeracy_policy_review_return_ledger_template: ${artifactId}_blank_returns_before_any_policy_returns_coordinate_scan_results_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_openintro_numeracy_policy_review_return_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: records ${g.openintro_policy_review_return_rows} blank OpenIntro IMS numeracy policy-review return rows and ${g.blank_return_field_cells_allocated} blank return-field cells; substantive upload-bound artifact; 0 returns, 0 source text, 0 excerpts, 0 tables/figures/datasets copied, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OpenIntro numeracy policy-review return ledger template; ${g.openintro_policy_review_return_rows} blank return rows, ${g.blank_return_field_cells_allocated} blank return-field cells, 0 source text, 0 excerpts, 0 tables/figures/datasets, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 161: OpenIntro numeracy policy-review return ledger template. It records ${g.openintro_policy_review_return_rows} blank return rows and ${g.blank_return_field_cells_allocated} blank return-field cells while keeping 0 returns, 0 source text, 0 excerpts, 0 tables/figures/datasets copied, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation OpenIntro numeracy policy-review return ledger template | ${artifactId} | Blank return-ledger template; ${g.openintro_policy_review_return_rows} rows, 0 source text, 0 excerpts, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_policy_review_return_ledger_template_artifact: \`${artifactId}\` (${g.openintro_policy_review_return_rows} blank return rows; 0 source text; 0 excerpts; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_policy_review_return_ledger_template: \`${artifactId}\`; blank OpenIntro IMS numeracy policy-review return ledger, no source text, excerpts, accepted terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OpenIntro IMS public numeracy policy-review return ledger template; substantive and upload-bound, but not a source excerpt, table, figure, dataset, translation, constructed form, license clearance, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_openintro_numeracy_policy_review_return_ledger_template' },
    { filename: `${artifactId}.md`, class: 'open_translation_openintro_numeracy_policy_review_return_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'open_translation_openintro_numeracy_policy_review_return_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package161_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package161_coordination_note' },
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
  upload.obj.package161_upload_queue_update = {
    captured_utc: '2026-07-03T10:32:00Z',
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
  const step = 'Stage package 161 OpenIntro numeracy policy-review return ledger template artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.openintro_policy_review_return_rows !== artifact.validation_snapshot.expected_openintro_policy_review_return_rows) failures.push(`return_rows_mismatch_${g.openintro_policy_review_return_rows}`);
  if (g.blank_return_fields_per_row !== artifact.validation_snapshot.expected_blank_return_fields_per_row) failures.push(`blank_return_fields_mismatch_${g.blank_return_fields_per_row}`);
  if (g.blank_return_field_cells_allocated !== artifact.validation_snapshot.expected_blank_return_field_cells_allocated) failures.push(`blank_return_cells_mismatch_${g.blank_return_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.openintro_policy_review_return_rows) {
    const filled = blankReturnFields.some((field) => row[field] !== null);
    if (filled || row.return_fields_filled !== 0 || row.return_received || row.policy_review_completed || row.coordinate_scan_authorized_after_return || row.source_text_capture_authorized_after_return || row.excerpt_selection_authorized_after_return || row.translation_authorized_after_return || row.constructed_surface_authorized_after_return) {
      failures.push(`nonblank_or_open_return_row_${row.openintro_policy_review_return_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentPolicyFile)).obj;
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
  openintro_policy_review_return_rows: artifact.gate_state.openintro_policy_review_return_rows,
  blank_return_fields_per_row: artifact.gate_state.blank_return_fields_per_row,
  blank_return_field_cells_allocated: artifact.gate_state.blank_return_field_cells_allocated,
  policy_review_returns_received: artifact.gate_state.policy_review_returns_received,
  return_fields_filled: artifact.gate_state.return_fields_filled,
  policy_reviews_completed: artifact.gate_state.policy_reviews_completed,
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
