import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_REVIEW_ONLY_SOURCE_COORDINATE_SCAN_ROUTER_20260703T081500Z';
const noteId = 'OPEN_TRANSLATION_REVIEW_ONLY_SOURCE_COORDINATE_SCAN_ROUTER_NOTE_20260703T081600Z';
const generatedUtc = '2026-07-03T08:15:00Z';
const noteGeneratedUtc = '2026-07-03T08:16:00Z';
const packageOrder = 152;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-REVIEW-ONLY-SOURCE-COORDINATE-SCAN-ROUTER-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentShelfFile = 'OPEN_TRANSLATION_REVIEW_ONLY_PACKET_SOURCE_SHELF_REFRESH_20260703T080000Z';

const scanReviewFields = [
  'scan_date',
  'scanner_route_or_reviewer_role',
  'exact_commit_or_version_confirmed',
  'license_recheck_result',
  'attribution_sidecar_decision',
  'coordinate_scope_approved',
  'source_file_inventory_result',
  'line_or_page_coordinate_policy',
  'excerpt_selection_decision',
  'next_required_artifact'
];

const zeroGateKeys = [
  'coordinate_scans_started',
  'route_tasks_completed',
  'scan_results_recorded',
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

function routerActionFor(row) {
  if (row.shelf_role === 'construction_method_support_not_source_text') {
    return 'method_lane_no_source_scan_wait_for_dated_returns_or_no_construction_decisions';
  }
  if (row.shelf_role?.includes('modality_authority')) {
    return 'modality_authority_router_video_first_no_text_excerpt';
  }
  if (row.shelf_role?.includes('language_authority') || row.shelf_role?.includes('language_register')) {
    return 'authority_or_register_support_router_not_direct_translation_scan';
  }
  if (row.source_family?.includes('DMOI')) {
    return 'reuse_existing_relation_function_coordinate_metadata_and_open_new_scans_only_by_scope_decision';
  }
  return 'coordinate_scan_candidate_after_license_and_attribution_recheck';
}

function scanPriorityFor(row) {
  const family = row.source_family || '';
  if (family.includes('Open Logic') || family.includes('Book of Proof')) return 1;
  if (family.includes('DMOI')) return 1;
  if (family.includes('FCLA') || family.includes('AATA')) return 2;
  if (family.includes('OpenIntro')) return 2;
  return 3;
}

function buildRoutingRows(parent) {
  return parent.source_shelf_rows.map((row, index) => ({
    coordinate_router_row_id: `OTCS-RTR-${String(index + 1).padStart(3, '0')}`,
    parent_source_shelf_row_id: row.source_shelf_row_id,
    source_family: row.source_family,
    shelf_role: row.shelf_role,
    local_route_kind: row.local_route_kind,
    local_route_paths_present: row.local_route_paths_present,
    candidate_queue_matches: row.candidate_queue_matches,
    packet_start_shapes: row.packet_start_shapes,
    router_action: routerActionFor(row),
    scan_priority: scanPriorityFor(row),
    allowed_now: [
      'metadata_inventory',
      'route_identity_check',
      'license_attribution_question_routing',
      'coordinate_policy_question',
      'blank_return_field_allocation'
    ],
    forbidden_now: [
      'source prose copying',
      'definition or example copying',
      'source excerpt selection',
      'line-span promotion',
      'translation drafting',
      'constructed surface proposal',
      'accepted local-language term',
      'pilot or publication readiness claim'
    ],
    scan_started: false,
    scan_result_recorded: false,
    source_text_or_excerpt_allowed: false,
    translation_allowed: false,
    constructed_surface_allowed: false
  }));
}

function buildRouteTaskRows(parent, routingRows) {
  const rows = [];
  for (const sourceRow of parent.source_shelf_rows) {
    const router = routingRows.find((row) => row.parent_source_shelf_row_id === sourceRow.source_shelf_row_id);
    const presentRoutes = sourceRow.local_route_paths.filter((route) => route.exists);
    for (const route of presentRoutes) {
      const index = rows.length + 1;
      rows.push({
        coordinate_route_task_row_id: `OTCS-TASK-${String(index).padStart(3, '0')}`,
        coordinate_router_row_id: router.coordinate_router_row_id,
        parent_source_shelf_row_id: sourceRow.source_shelf_row_id,
        source_family: sourceRow.source_family,
        route_path: route.path,
        route_type: route.type,
        route_bytes: route.bytes,
        task_kind: sourceRow.shelf_role?.includes('open_oer')
          ? 'metadata_inventory_scan_candidate'
          : sourceRow.shelf_role === 'construction_method_support_not_source_text'
            ? 'local_artifact_dependency_check'
            : 'authority_support_route_audit_candidate',
        blank_scan_review_fields: scanReviewFields,
        scan_date: null,
        scanner_route_or_reviewer_role: null,
        exact_commit_or_version_confirmed: null,
        license_recheck_result: null,
        attribution_sidecar_decision: null,
        coordinate_scope_approved: null,
        source_file_inventory_result: null,
        line_or_page_coordinate_policy: null,
        excerpt_selection_decision: null,
        next_required_artifact: null,
        scan_review_fields_filled: 0,
        route_task_completed: false,
        coordinate_scan_started: false,
        coordinate_scan_result_recorded: false,
        source_text_or_excerpt_files_created: 0,
        source_text_copied: 0,
        source_passages_selected: 0,
        translated_passages: 0,
        still_locked_reason: 'blank_router_task_no_scan_result_no_license_recheck_no_excerpt_decision'
      });
    }
  }
  return rows;
}

function buildLaneRouterRows(parent) {
  return parent.next_start_rows.map((row, index) => ({
    packet_lane_router_row_id: `OTCS-LANE-${String(index + 1).padStart(2, '0')}`,
    parent_next_start_row_id: row.next_start_row_id,
    lane: row.lane,
    useful_next_artifact: row.useful_next_artifact,
    reason_from_parent_shelf: row.why,
    allowed_next_action_class: row.useful_next_artifact.includes('return')
      ? 'return_ingest_only_when_dated_return_exists'
      : 'metadata_or_coordinate_router_only',
    source_text_or_excerpt_allowed: false,
    translation_allowed: false,
    pilot_ready: false
  }));
}

function buildProtocolRows() {
  const protocols = [
    ['license_recheck_before_scan', 'No source route may become an excerpt or adaptation source before exact license, edition, and attribution sidecar requirements are checked.'],
    ['metadata_inventory_only_first', 'First pass may count files, identify route type, and record coordinate policy only; it may not copy source prose.'],
    ['coordinate_identifier_not_text', 'Coordinates can name source paths, ids, pages, line ranges, or categories, but not source definitions, examples, or passages.'],
    ['attribution_sidecar_before_excerpt', 'Any later selected excerpt requires an attribution or modification notice sidecar before translation or adaptation.'],
    ['reviewer_return_gate', 'Language-specific or modality-specific promotion requires a dated route/reviewer return.'],
    ['modality_specific_access_gate', 'Signed-language rows remain video-first and cannot be treated as ordinary text-term substitutions.'],
    ['no_construction_path_preserved', 'The semi-constructed lane must preserve no-construction and hold decisions as valid outcomes.']
  ];
  return protocols.map(([protocol, description], index) => ({
    scan_protocol_row_id: `OTCS-PROTOCOL-${String(index + 1).padStart(2, '0')}`,
    protocol,
    description,
    scan_results_recorded: 0,
    violations_recorded: 0
  }));
}

function buildArtifact(parent) {
  const routingRows = buildRoutingRows(parent);
  const routeTaskRows = buildRouteTaskRows(parent, routingRows);
  const laneRouterRows = buildLaneRouterRows(parent);
  const protocolRows = buildProtocolRows();
  const blankScanReviewCells = routeTaskRows.length * scanReviewFields.length;
  const scanCandidateRows = routingRows.filter((row) => row.router_action.includes('coordinate_scan_candidate') || row.router_action.includes('reuse_existing')).length;

  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'review_only_source_coordinate_scan_router_no_scans_no_source_text_no_excerpts_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Convert the package 151 source shelf into a source-coordinate scan router: assign review-only routing actions and blank scan-review task rows for local route paths while recording no scan results, selecting no excerpts, copying no source text, and starting no translations or constructed surfaces.',
    parent_artifacts: [
      parentShelfFile,
      'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z',
      'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z'
    ],
    boundary: {
      artifact_is: [
        'coordinate-scan router',
        'blank scan-review task allocator',
        'next-artifact discriminator after package 151'
      ],
      artifact_is_not: [
        'coordinate scan result',
        'source file inventory result',
        'license recheck result',
        'source excerpt selection',
        'source text or definition copy',
        'translation draft',
        'constructed-language form proposal',
        'pilot or publication readiness claim'
      ],
      promotion_requires: [
        'separate coordinate scan artifact',
        'separate license/attribution decision',
        'separate selected-excerpt sidecar if excerpts are ever chosen',
        'dated reviewer route for target-language or modality promotion'
      ]
    },
    inherited_parent_counts: {
      parent_source_shelf_rows: parent.gate_state.source_shelf_rows,
      parent_packet_summary_rows: parent.gate_state.packet_summary_rows,
      parent_next_start_rows: parent.gate_state.next_start_rows,
      parent_local_route_paths_present: parent.gate_state.local_route_paths_present
    },
    coordinate_router_rows: routingRows,
    coordinate_route_task_rows: routeTaskRows,
    packet_lane_router_rows: laneRouterRows,
    scan_protocol_rows: protocolRows,
    gate_state: {
      coordinate_router_rows: routingRows.length,
      scan_candidate_router_rows: scanCandidateRows,
      support_or_method_router_rows: routingRows.length - scanCandidateRows,
      coordinate_route_task_rows: routeTaskRows.length,
      packet_lane_router_rows: laneRouterRows.length,
      scan_protocol_rows: protocolRows.length,
      blank_scan_review_fields_per_task: scanReviewFields.length,
      blank_scan_review_cells_allocated: blankScanReviewCells,
      coordinate_scans_started: 0,
      route_tasks_completed: 0,
      scan_results_recorded: 0,
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
      expected_coordinate_router_rows: parent.gate_state.source_shelf_rows,
      expected_coordinate_route_task_rows: parent.gate_state.local_route_paths_present,
      expected_packet_lane_router_rows: parent.gate_state.next_start_rows,
      expected_blank_scan_review_fields_per_task: scanReviewFields.length,
      expected_blank_scan_review_cells_allocated: blankScanReviewCells,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OPEN_TRANSLATION_PROOF_LITERACY_SOURCE_COORDINATE_SCAN_ROUTER_<timestamp>',
      'OPEN_TRANSLATION_ALGEBRA_SOURCE_COORDINATE_SCAN_QUEUE_<timestamp>',
      'OPENINTRO_NUMERACY_PACKET_ROUTE_SHEET_<timestamp>',
      'SIGNED_LANGUAGE_VIDEO_FIRST_DEFINITION_PACKET_ROUTER_<timestamp>',
      'SEMI_CONSTRUCTED_RELATION_FUNCTION_RETURN_OR_NO_CONSTRUCTION_DECISION_INGEST_<timestamp>_only_after_dated_return'
    ],
    decision: 'Package 152 routes package 151 source families into coordinate-scan or support-audit paths. It deliberately records no scan results, no license decisions, no source text, no excerpts, no translations, no constructed forms, and no readiness claims.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const routeRows = artifact.coordinate_router_rows.map((row) => `| ${row.coordinate_router_row_id} | ${row.source_family} | ${row.router_action} | ${row.scan_priority} | ${row.local_route_paths_present} |`).join('\n');
  const taskRows = artifact.coordinate_route_task_rows.map((row) => `| ${row.coordinate_route_task_row_id} | ${row.coordinate_router_row_id} | ${row.task_kind} | ${row.route_type} | ${row.scan_review_fields_filled} |`).join('\n');
  const laneRows = artifact.packet_lane_router_rows.map((row) => `| ${row.packet_lane_router_row_id} | ${row.lane} | ${row.useful_next_artifact} | ${row.allowed_next_action_class} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Coordinate router rows: \`${g.coordinate_router_rows}\`
- Scan-candidate router rows: \`${g.scan_candidate_router_rows}\`
- Support/method router rows: \`${g.support_or_method_router_rows}\`
- Coordinate route task rows: \`${g.coordinate_route_task_rows}\`
- Packet lane router rows: \`${g.packet_lane_router_rows}\`
- Scan protocol rows: \`${g.scan_protocol_rows}\`
- Blank scan-review fields per task: \`${g.blank_scan_review_fields_per_task}\`
- Blank scan-review cells: \`${g.blank_scan_review_cells_allocated}\`

## Router Rows

| Row | Source family | Router action | Priority | Local routes |
| --- | --- | --- | ---: | ---: |
${routeRows}

## Route Task Rows

| Row | Router | Task kind | Route type | Filled review fields |
| --- | --- | --- | --- | ---: |
${taskRows}

## Lane Router Rows

| Row | Lane | Useful next artifact | Allowed action class |
| --- | --- | --- | --- |
${laneRows}

## Zero Gates

- Coordinate scans / route tasks / scan results: \`0 / 0 / 0\`
- Source text/excerpt files: \`0\`
- Source text/definitions/examples copied: \`0 / 0 / 0\`
- Source passages selected: \`0\`
- Exact spans / candidate line ranges: \`0 / 0\`
- Translated passages: \`0\`
- Proposed bridge lexemes / morphemes / syntax / displays: \`0 / 0 / 0 / 0\`
- Accepted bridge surfaces / local-language terms: \`0 / 0\`
- Reviewer returns / license rechecks completed: \`0 / 0\`
- Readiness: \`publication=false, translation=false, constructed_surface=false, pilot=false\`

Boundary: this is a router and blank task allocator only. It performs no coordinate scan, no remote upload, no commit, no push, no PR update, no source-text copying, no excerpt selection, no translation, no constructed surface, and no readiness claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'parent_or_router', 'source_or_lane', 'action_or_task', 'route_type', 'blank_fields', 'filled_fields'].map(csvCell).join(','));
  for (const row of artifact.coordinate_router_rows) {
    rows.push([
      'coordinate_router_row',
      row.coordinate_router_row_id,
      row.parent_source_shelf_row_id,
      row.source_family,
      row.router_action,
      row.local_route_kind,
      '',
      ''
    ].map(csvCell).join(','));
  }
  for (const row of artifact.coordinate_route_task_rows) {
    rows.push([
      'coordinate_route_task_row',
      row.coordinate_route_task_row_id,
      row.coordinate_router_row_id,
      row.source_family,
      row.task_kind,
      row.route_type,
      row.blank_scan_review_fields.length,
      row.scan_review_fields_filled
    ].map(csvCell).join(','));
  }
  for (const row of artifact.packet_lane_router_rows) {
    rows.push([
      'packet_lane_router_row',
      row.packet_lane_router_row_id,
      row.parent_next_start_row_id,
      row.lane,
      row.allowed_next_action_class,
      '',
      '',
      ''
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
    status: 'pointer_only_package152_source_coordinate_scan_router_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: 'Package 152 queues a source-coordinate scan router and blank route-task allocator derived from package 151.',
    counts: {
      coordinate_router_rows: g.coordinate_router_rows,
      coordinate_route_task_rows: g.coordinate_route_task_rows,
      packet_lane_router_rows: g.packet_lane_router_rows,
      scan_protocol_rows: g.scan_protocol_rows,
      blank_scan_review_cells_allocated: g.blank_scan_review_cells_allocated
    },
    zero_gates: {
      coordinate_scans_started: 0,
      scan_results_recorded: 0,
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
  return `# Package 152 Source Coordinate Scan Router Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 152 creates \`${g.coordinate_router_rows}\` coordinate-router rows, \`${g.coordinate_route_task_rows}\` blank route-task rows, and \`${g.packet_lane_router_rows}\` packet-lane router rows. It is substantive catalog/control work and is queued for upload when a valid staging path exists.

Zero gates: \`0\` coordinate scans started, \`0\` scan results recorded, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` source passages selected, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` reviewer returns ingested, \`0\` readiness claims.

Boundary: source-coordinate scan router only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, scan result, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_review_only_source_coordinate_scan_router',
    artifact: artifactId,
    current_use: `${g.coordinate_router_rows} coordinate-router rows; ${g.coordinate_route_task_rows} blank route-task rows; ${g.blank_scan_review_cells_allocated} blank scan-review cells; 0 scans, 0 source text, 0 excerpts, 0 translations, 0 forms, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_review_only_source_coordinate_scan_router = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_open_translation_coordinate_router_rows: g.coordinate_router_rows,
    current_open_translation_coordinate_route_task_rows: g.coordinate_route_task_rows,
    current_open_translation_blank_scan_review_cells: g.blank_scan_review_cells_allocated,
    current_open_translation_coordinate_scans_started: 0,
    current_open_translation_source_text_or_excerpt_files: 0,
    current_open_translation_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_source_specific_coordinate_scan_artifact_only_no_source_text_no_excerpts_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation review-only source coordinate scan router',
    route: artifactId,
    license_status_to_recheck: 'router_only_recheck_exact_license_edition_attribution_and_coordinate_policy_before_any_scan_result_excerpt_adaptation_or_translation',
    best_translation_use: 'blank route-task allocator after package 151 for proof literacy, set/function, algebra, statistics/numeracy, signed-language access, authority-support, and semi-constructed method lanes',
    candidate_lanes: [
      'proof_literacy_coordinate_router',
      'set_function_coordinate_router',
      'linear_algebra_coordinate_router',
      'abstract_algebra_coordinate_router',
      'statistics_public_numeracy_route_sheet',
      'signed_language_video_first_router',
      'semi_constructed_relation_function_method'
    ],
    priority: 1,
    status: 'review_only_source_coordinate_scan_router_no_scans_no_source_text_no_excerpts_no_translation_no_forms_no_pilot',
    gate_state: {
      coordinate_router_rows: g.coordinate_router_rows,
      coordinate_route_task_rows: g.coordinate_route_task_rows,
      blank_scan_review_cells_allocated: g.blank_scan_review_cells_allocated,
      coordinate_scans_started: 0,
      source_text_or_excerpt_files_created: 0,
      translated_passages: 0,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_review_only_source_coordinate_scan_router: ${artifactId}_${g.coordinate_router_rows}_router_rows_${g.coordinate_route_task_rows}_blank_route_tasks_0_scans_0_source_text_0_excerpts_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_review_only_source_coordinate_scan_router_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_review_only_source_coordinate_scan_router_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_open_translation_coordinate_router_rows: g.coordinate_router_rows,
    current_open_translation_coordinate_route_task_rows: g.coordinate_route_task_rows,
    current_open_translation_source_text_or_excerpt_files: 0,
    current_open_translation_translated_passages: 0,
    current_open_translation_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_review_only_source_coordinate_scan_router = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_review_only_source_coordinate_scan_router: ${artifactId}_blank_route_tasks_before_any_scan_results_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_review_only_source_coordinate_scan_router = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: routes package 151 source/support/method rows into ${g.coordinate_router_rows} coordinate-router rows and ${g.coordinate_route_task_rows} blank route-task rows; substantive upload-bound artifact; 0 scans, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - Open translation review-only source coordinate scan router; ${g.coordinate_router_rows} router rows, ${g.coordinate_route_task_rows} blank route tasks, ${g.blank_scan_review_cells_allocated} blank scan-review cells, 0 scans, 0 source text, 0 excerpts, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 152: review-only source-coordinate scan router after package 151. It creates ${g.coordinate_router_rows} router rows and ${g.coordinate_route_task_rows} blank route-task rows while keeping 0 coordinate scans, 0 scan results, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation review-only source coordinate scan router | ${artifactId} | Blank source-coordinate router after package 151; ${g.coordinate_router_rows} router rows, ${g.coordinate_route_task_rows} route tasks, 0 scans, 0 source text, 0 excerpts, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_review_only_source_coordinate_scan_router_artifact: \`${artifactId}\` (${g.coordinate_router_rows} router rows; ${g.coordinate_route_task_rows} blank route-task rows; 0 scans; 0 source text; 0 excerpts; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_review_only_source_coordinate_scan_router: \`${artifactId}\`; review-only coordinate router and blank route-task allocator, no scan results, source text, excerpts, accepted terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: routes package 151 source/support/method rows into coordinate-scan and support-audit task lanes; substantive and upload-bound, but not a scan result, source excerpt, translation, constructed form, license clearance, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_review_only_source_coordinate_scan_router' },
    { filename: `${artifactId}.md`, class: 'open_translation_review_only_source_coordinate_scan_router' },
    { filename: `${artifactId}.csv`, class: 'open_translation_review_only_source_coordinate_scan_router' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package152_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package152_coordination_note' },
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
  upload.obj.package152_upload_queue_update = {
    captured_utc: '2026-07-03T08:17:00Z',
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
  const step = 'Stage package 152 open translation review-only source coordinate scan router artifacts as substantive beyond-core translation/construction catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.coordinate_router_rows !== artifact.validation_snapshot.expected_coordinate_router_rows) failures.push(`router_rows_mismatch_${g.coordinate_router_rows}`);
  if (g.coordinate_route_task_rows !== artifact.validation_snapshot.expected_coordinate_route_task_rows) failures.push(`route_task_rows_mismatch_${g.coordinate_route_task_rows}`);
  if (g.packet_lane_router_rows !== artifact.validation_snapshot.expected_packet_lane_router_rows) failures.push(`lane_rows_mismatch_${g.packet_lane_router_rows}`);
  if (g.blank_scan_review_fields_per_task !== artifact.validation_snapshot.expected_blank_scan_review_fields_per_task) failures.push(`blank_fields_mismatch_${g.blank_scan_review_fields_per_task}`);
  if (g.blank_scan_review_cells_allocated !== artifact.validation_snapshot.expected_blank_scan_review_cells_allocated) failures.push(`blank_cells_mismatch_${g.blank_scan_review_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.coordinate_route_task_rows) {
    const filled = scanReviewFields.some((field) => row[field] !== null);
    if (filled || row.scan_review_fields_filled !== 0 || row.route_task_completed || row.coordinate_scan_started || row.coordinate_scan_result_recorded || row.source_text_or_excerpt_files_created || row.source_text_copied || row.source_passages_selected || row.translated_passages) {
      failures.push(`nonblank_or_open_route_task_${row.coordinate_route_task_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentShelfFile)).obj;
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
  coordinate_router_rows: artifact.gate_state.coordinate_router_rows,
  scan_candidate_router_rows: artifact.gate_state.scan_candidate_router_rows,
  support_or_method_router_rows: artifact.gate_state.support_or_method_router_rows,
  coordinate_route_task_rows: artifact.gate_state.coordinate_route_task_rows,
  packet_lane_router_rows: artifact.gate_state.packet_lane_router_rows,
  scan_protocol_rows: artifact.gate_state.scan_protocol_rows,
  blank_scan_review_cells_allocated: artifact.gate_state.blank_scan_review_cells_allocated,
  coordinate_scans_started: artifact.gate_state.coordinate_scans_started,
  scan_results_recorded: artifact.gate_state.scan_results_recorded,
  source_text_copied: artifact.gate_state.source_text_copied,
  translated_passages: artifact.gate_state.translated_passages,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
