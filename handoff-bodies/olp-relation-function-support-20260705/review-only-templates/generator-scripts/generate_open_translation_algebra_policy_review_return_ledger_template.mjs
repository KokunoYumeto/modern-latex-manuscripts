import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_ALGEBRA_POLICY_REVIEW_RETURN_LEDGER_TEMPLATE_20260703T094500Z';
const noteId = 'OPEN_TRANSLATION_ALGEBRA_POLICY_REVIEW_RETURN_LEDGER_TEMPLATE_NOTE_20260703T094600Z';
const generatedUtc = '2026-07-03T09:45:00Z';
const noteGeneratedUtc = '2026-07-03T09:46:00Z';
const packageOrder = 158;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-ALGEBRA-POLICY-REVIEW-RETURN-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentPolicyFile = 'OPEN_TRANSLATION_ALGEBRA_SOURCE_COORDINATE_POLICY_SHEET_20260703T093000Z';

const blankReturnFields = [
  'return_date',
  'reviewer_route_or_role',
  'policy_row_id_confirmed',
  'policy_class_decision',
  'coordinate_scan_scope_decision',
  'license_or_permission_gate_decision',
  'attribution_sidecar_requirement',
  'support_only_route_confirmation',
  'source_text_capture_decision',
  'excerpt_selection_decision',
  'next_allowed_artifact',
  'comments_without_source_prose'
];

const zeroGateKeys = [
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
    ...(parent.source_class_policy_rows || []),
    ...(parent.route_use_policy_rows || []),
    ...(parent.contents_extension_policy_rows || []),
    ...(parent.contents_type_policy_rows || []),
    ...(parent.packet_policy_rows || [])
  ];
}

function buildReturnRows(parent) {
  return parentPolicyRows(parent).map((row, index) => ({
    algebra_policy_review_return_row_id: `ALG-SCP-RETURN-${String(index + 1).padStart(3, '0')}`,
    parent_policy_row_id: row.policy_row_id,
    parent_summary_row_id: row.parent_summary_row_id || null,
    parent_packet_candidate_row_id: row.parent_packet_candidate_row_id || null,
    source_family: row.source_family,
    source_group: row.source_group,
    summary_kind: row.summary_kind,
    policy_class: row.policy_class,
    inherited_coordinate_scan_candidate_after_review: row.coordinate_scan_candidate_after_review,
    inherited_license_or_permission_gate_required: row.license_or_permission_gate_required,
    inherited_metadata_rows: row.metadata_rows,
    inherited_metadata_bytes: row.metadata_bytes,
    inherited_policy_reason_metadata_only: row.policy_reason_metadata_only,
    blank_return_fields: blankReturnFields,
    return_date: null,
    reviewer_route_or_role: null,
    policy_row_id_confirmed: null,
    policy_class_decision: null,
    coordinate_scan_scope_decision: null,
    license_or_permission_gate_decision: null,
    attribution_sidecar_requirement: null,
    support_only_route_confirmation: null,
    source_text_capture_decision: null,
    excerpt_selection_decision: null,
    next_allowed_artifact: null,
    comments_without_source_prose: null,
    return_fields_filled: 0,
    return_received: false,
    policy_review_completed: false,
    coordinate_scan_authorized_after_return: false,
    source_text_capture_authorized_after_return: false,
    excerpt_selection_authorized_after_return: false,
    translation_authorized_after_return: false,
    constructed_surface_authorized_after_return: false,
    still_locked_reason: 'blank_algebra_policy_review_return_row_no_dated_return_no_permission_decision_no_scan_authorization'
  }));
}

function buildPolicyClassReturnSummaryRows(returnRows) {
  const map = new Map();
  for (const row of returnRows) {
    if (!map.has(row.policy_class)) {
      map.set(row.policy_class, {
        algebra_policy_class_return_summary_row_id: `ALG-SCP-RETURN-CLASS-${String(map.size + 1).padStart(2, '0')}`,
        policy_class: row.policy_class,
        return_rows_allocated: 0,
        inherited_metadata_rows: 0,
        inherited_candidate_after_review_rows: 0,
        inherited_license_gate_rows: 0,
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
  }
  return [...map.values()].sort((a, b) => b.return_rows_allocated - a.return_rows_allocated || a.policy_class.localeCompare(b.policy_class));
}

function buildLaneReturnSummaryRows(parent, returnRows) {
  const lanes = parent.next_policy_artifact_rows || [];
  return lanes.map((lane, index) => ({
    algebra_lane_return_summary_row_id: `ALG-SCP-RETURN-LANE-${String(index + 1).padStart(2, '0')}`,
    parent_next_policy_artifact_row_id: lane.next_policy_artifact_row_id,
    lane: lane.lane,
    useful_next_artifact: lane.useful_next_artifact,
    allowed_action_class: lane.allowed_action_class,
    linked_return_rows: returnRows
      .filter((row) => {
        if (lane.lane === 'source_markup_policy') {
          return row.inherited_coordinate_scan_candidate_after_review || row.policy_class.includes('markup') || row.policy_class.includes('source_tree');
        }
        if (lane.lane === 'fcla_license_attribution_gate') {
          return row.source_family.includes('FCLA') || row.policy_class.includes('linear_algebra') || row.inherited_license_or_permission_gate_required;
        }
        if (lane.lane === 'aata_license_attribution_gate') {
          return row.source_family.includes('AATA') || row.policy_class.includes('abstract_algebra') || row.inherited_license_or_permission_gate_required;
        }
        if (lane.lane === 'algebra_metadata_review') return true;
        return false;
      })
      .map((row) => row.algebra_policy_review_return_row_id),
    policy_review_returns_received: 0,
    coordinate_scans_authorized: 0,
    excerpt_selections_authorized: 0,
    source_text_or_excerpt_allowed_now: false
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
    status: 'algebra_policy_review_return_ledger_template_blank_no_returns_no_scans_no_source_text_no_excerpts_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Create a blank policy-review return ledger for every package 157 algebra source-coordinate policy row, allowing future dated review/permission decisions to be ingested separately while keeping all scan, source-text, excerpt, translation, and constructed-surface gates closed.',
    parent_artifacts: [
      parentPolicyFile,
      'OPEN_TRANSLATION_ALGEBRA_METADATA_INVENTORY_SCAN_START_20260703T091500Z',
      'OPEN_TRANSLATION_REVIEW_ONLY_SOURCE_COORDINATE_SCAN_ROUTER_20260703T081500Z',
      'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z'
    ],
    boundary: {
      artifact_is: [
        'blank algebra policy-review return ledger template',
        'one return row per package 157 policy row',
        'future dated-return intake scaffold'
      ],
      artifact_is_not: [
        'policy return',
        'policy decision',
        'permission or license clearance',
        'coordinate scan authorization',
        'source text capture authorization',
        'source excerpt selection',
        'translation draft',
        'constructed-language form proposal',
        'pilot or publication readiness claim'
      ],
      fill_rule: 'No return fields are filled here. Future returns must be dated, route-labeled, and ingested in a separate artifact without source prose unless a later policy explicitly allows it.',
      promotion_requires: [
        'dated policy review return',
        'permission or license gate decision where required',
        'attribution sidecar decision',
        'separate coordinate scan artifact',
        'separate selected-excerpt sidecar before any translation or adaptation'
      ]
    },
    inherited_parent_counts: {
      parent_algebra_source_coordinate_policy_rows: parent.gate_state.algebra_source_coordinate_policy_rows,
      parent_candidate_after_review_rows: parent.gate_state.coordinate_scan_candidate_after_review_rows,
      parent_license_or_permission_gate_required_rows: parent.gate_state.license_or_permission_gate_required_rows,
      parent_policy_reviews_completed: parent.gate_state.policy_reviews_completed,
      parent_coordinate_scans_authorized: parent.gate_state.coordinate_scans_authorized
    },
    blank_return_fields: blankReturnFields,
    algebra_policy_review_return_rows: returnRows,
    algebra_policy_class_return_summary_rows: classSummaryRows,
    algebra_lane_return_summary_rows: laneSummaryRows,
    gate_state: {
      algebra_policy_review_return_rows: returnRows.length,
      parent_algebra_source_coordinate_policy_rows: parent.gate_state.algebra_source_coordinate_policy_rows,
      algebra_policy_class_return_summary_rows: classSummaryRows.length,
      algebra_lane_return_summary_rows: laneSummaryRows.length,
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
      expected_algebra_policy_review_return_rows: parent.gate_state.algebra_source_coordinate_policy_rows,
      expected_blank_return_fields_per_row: blankReturnFields.length,
      expected_blank_return_field_cells_allocated: blankReturnCells,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OPEN_TRANSLATION_ALGEBRA_POLICY_REVIEW_RETURN_LEDGER_WITH_RETURNS_<timestamp>_only_after_dated_returns',
      'OPEN_TRANSLATION_LINEAR_ALGEBRA_FCLA_PERMISSION_ATTRIBUTION_DECISION_LEDGER_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_ABSTRACT_ALGEBRA_AATA_PERMISSION_ATTRIBUTION_DECISION_LEDGER_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_ALGEBRA_SOURCE_MARKUP_COORDINATE_POLICY_RETURN_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_ALGEBRA_SELECTED_EXCERPT_SIDECAR_<timestamp>_only_after_policy_returns_and_permission_decisions'
    ],
    decision: 'Package 158 allocates blank algebra policy-review return rows only. It records no returns, no policy decisions, no scan authorizations, no source text, no excerpts, no translations, no constructed forms, and no readiness claims.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const returnRows = artifact.algebra_policy_review_return_rows.map((row) => `| ${row.algebra_policy_review_return_row_id} | ${row.parent_policy_row_id} | ${row.source_family} | ${row.policy_class} | ${row.return_fields_filled} |`).join('\n');
  const classRows = artifact.algebra_policy_class_return_summary_rows.map((row) => `| ${row.algebra_policy_class_return_summary_row_id} | ${row.policy_class} | ${row.return_rows_allocated} | ${row.inherited_candidate_after_review_rows} | ${row.inherited_license_gate_rows} |`).join('\n');
  const laneRows = artifact.algebra_lane_return_summary_rows.map((row) => `| ${row.algebra_lane_return_summary_row_id} | ${row.lane} | ${row.linked_return_rows.length} | ${row.allowed_action_class} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Algebra policy-review return rows: \`${g.algebra_policy_review_return_rows}\`
- Parent algebra source-coordinate policy rows: \`${g.parent_algebra_source_coordinate_policy_rows}\`
- Policy-class summary rows: \`${g.algebra_policy_class_return_summary_rows}\`
- Lane summary rows: \`${g.algebra_lane_return_summary_rows}\`
- Blank return fields per row: \`${g.blank_return_fields_per_row}\`
- Blank return-field cells: \`${g.blank_return_field_cells_allocated}\`

## Return Rows

| Row | Parent policy row | Source family | Policy class | Filled fields |
| --- | --- | --- | --- | ---: |
${returnRows}

## Policy-Class Summaries

| Row | Policy class | Return rows | Candidate-after-review rows | License-gate rows |
| --- | --- | ---: | ---: | ---: |
${classRows}

## Lane Summaries

| Row | Lane | Linked return rows | Allowed action class |
| --- | --- | ---: | --- |
${laneRows}

## Zero Gates

- Policy-review returns received / policy reviews completed: \`0 / 0\`
- Coordinate scans / source-text capture / excerpt selections authorized: \`0 / 0 / 0\`
- Source text/excerpt files: \`0\`
- Source text/definitions/examples copied: \`0 / 0 / 0\`
- Source passages selected: \`0\`
- Exact spans / candidate line ranges: \`0 / 0\`
- Translated passages: \`0\`
- Proposed bridge lexemes / morphemes / syntax / displays: \`0 / 0 / 0 / 0\`
- Accepted bridge surfaces / local-language terms: \`0 / 0\`
- Reviewer returns / license rechecks completed: \`0 / 0\`
- Readiness: \`publication=false, translation=false, constructed_surface=false, pilot=false\`

Boundary: blank return ledger template only. This artifact is not a policy decision, permission clearance, scan authorization, source excerpt, translation, constructed form, or readiness claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'parent_policy_row_id', 'source_family', 'policy_class', 'blank_fields', 'filled_fields', 'return_received'].map(csvCell).join(','));
  for (const row of artifact.algebra_policy_review_return_rows) {
    rows.push([
      'algebra_policy_review_return_row',
      row.algebra_policy_review_return_row_id,
      row.parent_policy_row_id,
      row.source_family,
      row.policy_class,
      row.blank_return_fields.length,
      row.return_fields_filled,
      row.return_received
    ].map(csvCell).join(','));
  }
  for (const row of artifact.algebra_policy_class_return_summary_rows) {
    rows.push([
      'algebra_policy_class_return_summary',
      row.algebra_policy_class_return_summary_row_id,
      '',
      '',
      row.policy_class,
      '',
      '',
      row.policy_review_returns_received
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
    status: 'pointer_only_package158_algebra_policy_review_return_ledger_template_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: 'Package 158 queues a blank algebra policy-review return ledger template for all package 157 source-coordinate policy rows.',
    counts: {
      algebra_policy_review_return_rows: g.algebra_policy_review_return_rows,
      blank_return_fields_per_row: g.blank_return_fields_per_row,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated,
      algebra_policy_class_return_summary_rows: g.algebra_policy_class_return_summary_rows,
      algebra_lane_return_summary_rows: g.algebra_lane_return_summary_rows
    },
    zero_gates: {
      policy_review_returns_received: 0,
      policy_reviews_completed: 0,
      coordinate_scans_authorized: 0,
      source_text_capture_authorized: 0,
      excerpt_selections_authorized: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_passages_selected: 0,
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
  return `# Package 158 Algebra Policy Review Return Ledger Template Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 158 creates \`${g.algebra_policy_review_return_rows}\` blank algebra policy-review return rows with \`${g.blank_return_fields_per_row}\` blank fields per row and \`${g.blank_return_field_cells_allocated}\` blank return-field cells.

Zero gates: \`0\` returns received, \`0\` policy reviews completed, \`0\` coordinate scans authorized, \`0\` source-text capture authorized, \`0\` excerpt selections authorized, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: blank return ledger template only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_algebra_policy_review_return_ledger_template',
    artifact: artifactId,
    current_use: `${g.algebra_policy_review_return_rows} blank algebra policy-review return rows; ${g.blank_return_field_cells_allocated} blank return-field cells; 0 returns, 0 scans authorized, 0 source text, 0 excerpts, 0 translations, 0 forms, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_algebra_policy_review_return_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_algebra_policy_review_return_rows: g.algebra_policy_review_return_rows,
    current_algebra_blank_return_cells: g.blank_return_field_cells_allocated,
    current_algebra_policy_review_returns_received: 0,
    current_algebra_source_text_or_excerpt_files: 0,
    current_algebra_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_dated_algebra_policy_returns_or_permission_attribution_template_only_no_source_text_no_excerpts_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation algebra policy review return ledger template',
    route: artifactId,
    license_status_to_recheck: 'blank_return_ledger_only_recheck_FCLA_and_AATA_license_permission_routes_before_any_policy_return_scan_excerpt_adaptation_or_translation',
    best_translation_use: 'future dated algebra policy-review return intake for FCLA and AATA source-coordinate policy rows',
    candidate_lanes: [
      'linear_algebra',
      'abstract_algebra',
      'source_coordinate_policy_return',
      'FCLA',
      'AATA',
      'permission_gate_review'
    ],
    priority: 1,
    status: 'blank_algebra_policy_review_return_ledger_template_no_returns_no_scans_no_source_text_no_excerpts_no_translation_no_forms_no_pilot',
    gate_state: {
      algebra_policy_review_return_rows: g.algebra_policy_review_return_rows,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated,
      policy_review_returns_received: 0,
      coordinate_scans_authorized: 0,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_algebra_policy_review_return_ledger_template: ${artifactId}_${g.algebra_policy_review_return_rows}_blank_return_rows_${g.blank_return_field_cells_allocated}_blank_cells_0_returns_0_scans_0_source_text_0_excerpts_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_algebra_policy_review_return_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_algebra_policy_review_return_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_algebra_policy_review_return_rows: g.algebra_policy_review_return_rows,
    current_algebra_policy_review_returns_received: 0,
    current_algebra_source_text_or_excerpt_files: 0,
    current_algebra_translated_passages: 0,
    current_algebra_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_algebra_policy_review_return_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_algebra_policy_review_return_ledger_template: ${artifactId}_blank_return_rows_before_any_policy_returns_coordinate_scans_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_algebra_policy_review_return_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates ${g.algebra_policy_review_return_rows} blank algebra policy-review return rows and ${g.blank_return_field_cells_allocated} blank return-field cells for package 157 algebra policy rows; substantive upload-bound artifact; 0 returns, 0 scans authorized, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - Algebra policy-review return ledger template; ${g.algebra_policy_review_return_rows} blank return rows, ${g.blank_return_field_cells_allocated} blank cells, 0 returns, 0 scans authorized, 0 source text, 0 excerpts, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 158: algebra policy-review return ledger template. It creates ${g.algebra_policy_review_return_rows} blank return rows and ${g.blank_return_field_cells_allocated} blank return-field cells while keeping 0 returns, 0 policy reviews completed, 0 coordinate scans authorized, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation algebra policy review return ledger template | ${artifactId} | Blank algebra policy-review return ledger; ${g.algebra_policy_review_return_rows} rows, 0 returns, 0 scans authorized, 0 source text, 0 excerpts, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_algebra_policy_review_return_ledger_template_artifact: \`${artifactId}\` (${g.algebra_policy_review_return_rows} blank return rows; 0 returns; 0 scans authorized; 0 source text; 0 excerpts; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_algebra_policy_review_return_ledger_template: \`${artifactId}\`; blank policy-review return ledger over algebra source-coordinate policy rows, no returns, scans authorized, source text, excerpts, accepted terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: algebra blank policy-review return ledger for FCLA and AATA route policy rows; substantive and upload-bound, but not a return, policy decision, scan authorization, source excerpt, translation, constructed form, license clearance, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_algebra_policy_review_return_ledger_template' },
    { filename: `${artifactId}.md`, class: 'open_translation_algebra_policy_review_return_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'open_translation_algebra_policy_review_return_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package158_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package158_coordination_note' },
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
  upload.obj.package158_upload_queue_update = {
    captured_utc: '2026-07-03T09:47:00Z',
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
  const step = 'Stage package 158 algebra policy-review return ledger template artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.algebra_policy_review_return_rows !== artifact.validation_snapshot.expected_algebra_policy_review_return_rows) failures.push(`return_rows_mismatch_${g.algebra_policy_review_return_rows}`);
  if (g.blank_return_fields_per_row !== artifact.validation_snapshot.expected_blank_return_fields_per_row) failures.push(`blank_return_fields_mismatch_${g.blank_return_fields_per_row}`);
  if (g.blank_return_field_cells_allocated !== artifact.validation_snapshot.expected_blank_return_field_cells_allocated) failures.push(`blank_return_cells_mismatch_${g.blank_return_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.algebra_policy_review_return_rows) {
    const filled = blankReturnFields.some((field) => row[field] !== null);
    if (filled || row.return_fields_filled !== 0 || row.return_received || row.policy_review_completed || row.coordinate_scan_authorized_after_return || row.source_text_capture_authorized_after_return || row.excerpt_selection_authorized_after_return || row.translation_authorized_after_return || row.constructed_surface_authorized_after_return) {
      failures.push(`nonblank_or_open_return_row_${row.algebra_policy_review_return_row_id}`);
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
  algebra_policy_review_return_rows: artifact.gate_state.algebra_policy_review_return_rows,
  blank_return_field_cells_allocated: artifact.gate_state.blank_return_field_cells_allocated,
  policy_review_returns_received: artifact.gate_state.policy_review_returns_received,
  policy_reviews_completed: artifact.gate_state.policy_reviews_completed,
  coordinate_scans_authorized: artifact.gate_state.coordinate_scans_authorized,
  source_text_capture_authorized: artifact.gate_state.source_text_capture_authorized,
  excerpt_selections_authorized: artifact.gate_state.excerpt_selections_authorized,
  source_text_copied: artifact.gate_state.source_text_copied,
  translated_passages: artifact.gate_state.translated_passages,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
