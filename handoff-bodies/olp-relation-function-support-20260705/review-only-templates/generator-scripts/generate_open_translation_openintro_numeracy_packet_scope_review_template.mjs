import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_PACKET_SCOPE_REVIEW_TEMPLATE_20260703T110000Z';
const noteId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_PACKET_SCOPE_REVIEW_TEMPLATE_NOTE_20260703T110100Z';
const generatedUtc = '2026-07-03T11:00:00Z';
const noteGeneratedUtc = '2026-07-03T11:01:00Z';
const packageOrder = 163;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-OPENINTRO-NUMERACY-PACKET-SCOPE-REVIEW-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentInventoryFile = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_METADATA_INVENTORY_SCAN_START_20260703T100000Z';
const parentPolicyFile = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SOURCE_COORDINATE_POLICY_SHEET_20260703T101500Z';
const parentDecisionFile = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_ATTRIBUTION_SHAREALIKE_DECISION_LEDGER_TEMPLATE_20260703T104500Z';

const packetReviewFields = [
  'review_date',
  'reviewer_route_or_role',
  'packet_slot_confirmed',
  'target_audience_decision',
  'public_service_use_case_decision',
  'local_language_or_community_route_needed',
  'native_or_local_source_needed',
  'openintro_source_use_scope_decision',
  'exact_source_route_decision',
  'attribution_sharealike_dependency_decision',
  'table_figure_dataset_policy_decision',
  'first_packet_priority_decision',
  'next_allowed_artifact',
  'comments_without_source_prose'
];

const laneAlignmentFields = [
  'alignment_review_date',
  'reviewer_route_or_role',
  'lane_group_confirmed',
  'local_source_route_needed',
  'local_authority_needed',
  'written_or_video_modality_decision',
  'packet_slot_priority_decision',
  'translation_or_surface_not_allowed_reason',
  'next_allowed_artifact',
  'comments_without_source_prose'
];

const zeroGateKeys = [
  'packet_scope_reviews_completed',
  'packet_lane_alignment_reviews_completed',
  'packet_priority_decisions_recorded',
  'local_language_routes_accepted',
  'native_or_local_sources_accepted',
  'policy_review_returns_received',
  'attribution_sharealike_decisions_recorded',
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

function packetPolicyRows(parentPolicy, packetSlot) {
  return (parentPolicy.packet_slot_policy_rows || []).filter((row) => row.source_group === packetSlot.neutral_packet_slot);
}

function packetDecisionRows(parentDecision, packetSlot) {
  return (parentDecision.openintro_attribution_sharealike_decision_rows || []).filter((row) => row.source_group === packetSlot.neutral_packet_slot || row.group_type === 'numeracy_packet_slot');
}

function buildPacketScopeReviewRows(parentInventory, parentPolicy, parentDecision) {
  return parentInventory.numeracy_packet_slot_rows.map((slot, index) => {
    const policyRows = packetPolicyRows(parentPolicy, slot);
    const decisionRows = packetDecisionRows(parentDecision, slot);
    return {
      openintro_packet_scope_review_row_id: `OI-PACKET-SCOPE-${String(index + 1).padStart(3, '0')}`,
      parent_packet_slot_row_id: slot.numeracy_packet_slot_row_id,
      neutral_packet_slot: slot.neutral_packet_slot,
      source_fit: slot.source_fit,
      still_required_before_use: slot.still_required,
      useful_translation_candidate_note: 'public_numeracy_packet_candidate_only_no_source_text_no_translation_no_local_surface',
      linked_policy_row_ids: policyRows.map((row) => row.policy_row_id),
      linked_attribution_sharealike_decision_row_ids: decisionRows.map((row) => row.openintro_attribution_sharealike_decision_row_id),
      inherited_table_figure_dataset_policy_required: policyRows.some((row) => row.table_figure_dataset_policy_required),
      inherited_license_or_permission_gate_required: policyRows.some((row) => row.license_or_permission_gate_required),
      inherited_attribution_sidecar_required: policyRows.some((row) => row.attribution_sidecar_required),
      blank_packet_review_fields: packetReviewFields,
      review_date: null,
      reviewer_route_or_role: null,
      packet_slot_confirmed: null,
      target_audience_decision: null,
      public_service_use_case_decision: null,
      local_language_or_community_route_needed: null,
      native_or_local_source_needed: null,
      openintro_source_use_scope_decision: null,
      exact_source_route_decision: null,
      attribution_sharealike_dependency_decision: null,
      table_figure_dataset_policy_decision: null,
      first_packet_priority_decision: null,
      next_allowed_artifact: null,
      comments_without_source_prose: null,
      packet_review_fields_filled: 0,
      packet_scope_review_completed: false,
      packet_priority_decision_recorded: false,
      source_text_or_excerpt_allowed_now: false,
      translation_allowed_now: false,
      local_surface_allowed_now: false,
      still_locked_reason: 'blank_packet_scope_review_no_local_source_route_no_attribution_decision_no_excerpt_no_translation'
    };
  });
}

function buildPacketLaneAlignmentRows(packetRows, lanes) {
  const rows = [];
  for (const packet of packetRows) {
    for (const lane of lanes) {
      rows.push({
        openintro_packet_lane_alignment_row_id: `OI-PACKET-LANE-${String(rows.length + 1).padStart(3, '0')}`,
        parent_packet_scope_review_row_id: packet.openintro_packet_scope_review_row_id,
        parent_lane_fit_row_id: lane.numeracy_lane_fit_row_id,
        neutral_packet_slot: packet.neutral_packet_slot,
        lane_group: lane.lane_group,
        inherited_lane_first_use: lane.first_use,
        inherited_lane_gate: lane.gate,
        useful_alignment_note: 'possible_future_packet_lane_alignment_only_no_language_authority_no_surface_no_translation',
        blank_lane_alignment_fields: laneAlignmentFields,
        alignment_review_date: null,
        reviewer_route_or_role: null,
        lane_group_confirmed: null,
        local_source_route_needed: null,
        local_authority_needed: null,
        written_or_video_modality_decision: null,
        packet_slot_priority_decision: null,
        translation_or_surface_not_allowed_reason: null,
        next_allowed_artifact: null,
        comments_without_source_prose: null,
        lane_alignment_fields_filled: 0,
        packet_lane_alignment_review_completed: false,
        local_language_route_accepted: false,
        native_or_local_source_accepted: false,
        translation_allowed_now: false,
        local_surface_allowed_now: false,
        pilot_ready: false
      });
    }
  }
  return rows;
}

function buildLaneGroupSummaryRows(alignmentRows) {
  const map = new Map();
  for (const row of alignmentRows) {
    if (!map.has(row.lane_group)) {
      map.set(row.lane_group, {
        openintro_packet_lane_summary_row_id: `OI-PACKET-LANE-SUMMARY-${String(map.size + 1).padStart(2, '0')}`,
        lane_group: row.lane_group,
        packet_alignment_rows: 0,
        packet_lane_alignment_reviews_completed: 0,
        local_language_routes_accepted: 0,
        native_or_local_sources_accepted: 0,
        translations_allowed: 0,
        local_surfaces_allowed: 0,
        pilot_ready_claims: 0
      });
    }
    map.get(row.lane_group).packet_alignment_rows += 1;
  }
  return [...map.values()].sort((a, b) => a.lane_group.localeCompare(b.lane_group));
}

function buildArtifact(parentInventory, parentPolicy, parentDecision) {
  const packetRows = buildPacketScopeReviewRows(parentInventory, parentPolicy, parentDecision);
  const alignmentRows = buildPacketLaneAlignmentRows(packetRows, parentInventory.numeracy_lane_fit_rows);
  const laneSummaryRows = buildLaneGroupSummaryRows(alignmentRows);
  const blankPacketReviewCells = packetRows.length * packetReviewFields.length;
  const blankLaneAlignmentCells = alignmentRows.length * laneAlignmentFields.length;

  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'openintro_numeracy_packet_scope_review_template_blank_no_reviews_no_source_text_no_excerpts_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Create a blank packet-scope review template for OpenIntro IMS public numeracy candidates, preserving useful translation-candidate categories and world-family lane alignment questions while keeping all source, local authority, excerpt, translation, constructed-surface, and readiness gates closed.',
    parent_artifacts: [
      parentInventoryFile,
      parentPolicyFile,
      parentDecisionFile,
      'OPENINTRO_NUMERACY_PUBLIC_SERVICE_SOURCE_MINI_SHELF_20260629T194849Z',
      'OPENINTRO_NUMERACY_EXACT_EDITION_CAPTURE_20260629T200225Z',
      'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z'
    ],
    boundary: {
      artifact_is: [
        'blank OpenIntro numeracy packet-scope review template',
        'useful translation-candidate catalog without source text',
        'world-family packet-by-lane alignment scaffold',
        'local-source and local-authority question allocator'
      ],
      artifact_is_not: [
        'packet approval',
        'local language authority review',
        'native source acceptance',
        'source excerpt sidecar',
        'source text capture',
        'translation draft',
        'constructed-language form proposal',
        'pilot or publication readiness claim'
      ],
      fill_rule: 'No packet or lane alignment fields are filled here. Future packet scope reviews must be dated, route-labeled, and must not copy source prose unless a later policy explicitly allows it.',
      promotion_requires: [
        'dated packet-scope review return',
        'local-language or community route review',
        'native/local source route decision where needed',
        'attribution/share-alike decision return',
        'separate selected-excerpt sidecar before any translation or adaptation',
        'local reviewer authority before any bridge-language surface'
      ]
    },
    inherited_parent_counts: {
      parent_packet_slot_rows: parentInventory.gate_state.numeracy_packet_slot_rows,
      parent_lane_fit_rows: parentInventory.gate_state.numeracy_lane_fit_rows,
      parent_attribution_sharealike_decision_rows: parentDecision.gate_state.openintro_attribution_sharealike_decision_rows,
      parent_source_coordinate_policy_rows: parentPolicy.gate_state.openintro_numeracy_source_coordinate_policy_rows
    },
    packet_review_fields: packetReviewFields,
    lane_alignment_fields: laneAlignmentFields,
    openintro_packet_scope_review_rows: packetRows,
    openintro_packet_lane_alignment_rows: alignmentRows,
    openintro_packet_lane_group_summary_rows: laneSummaryRows,
    gate_state: {
      openintro_packet_scope_review_rows: packetRows.length,
      openintro_packet_lane_alignment_rows: alignmentRows.length,
      openintro_packet_lane_group_summary_rows: laneSummaryRows.length,
      blank_packet_review_fields_per_row: packetReviewFields.length,
      blank_lane_alignment_fields_per_row: laneAlignmentFields.length,
      blank_packet_review_cells_allocated: blankPacketReviewCells,
      blank_lane_alignment_cells_allocated: blankLaneAlignmentCells,
      blank_review_cells_allocated_total: blankPacketReviewCells + blankLaneAlignmentCells,
      packet_scope_reviews_completed: 0,
      packet_lane_alignment_reviews_completed: 0,
      packet_priority_decisions_recorded: 0,
      local_language_routes_accepted: 0,
      native_or_local_sources_accepted: 0,
      policy_review_returns_received: 0,
      attribution_sharealike_decisions_recorded: 0,
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
      pilot_ready_claims: 0,
      publication_ready: false,
      translation_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      expected_packet_scope_review_rows: parentInventory.gate_state.numeracy_packet_slot_rows,
      expected_packet_lane_alignment_rows: parentInventory.gate_state.numeracy_packet_slot_rows * parentInventory.gate_state.numeracy_lane_fit_rows,
      expected_blank_packet_review_fields_per_row: packetReviewFields.length,
      expected_blank_lane_alignment_fields_per_row: laneAlignmentFields.length,
      expected_blank_review_cells_allocated_total: blankPacketReviewCells + blankLaneAlignmentCells,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_PACKET_SCOPE_REVIEW_RETURN_LEDGER_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_LANGUAGE_SOURCE_ALIGNMENT_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SELECTED_EXCERPT_SIDECAR_TEMPLATE_<timestamp>_only_after_policy_attribution_and_packet_scope_returns'
    ],
    decision: 'Package 163 allocates blank OpenIntro numeracy packet-scope and packet-by-lane review rows only. It records no packet approvals, no local authority returns, no source text, no excerpts, no translations, no constructed forms, and no readiness claims.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const packetRows = artifact.openintro_packet_scope_review_rows.map((row) => `| ${row.openintro_packet_scope_review_row_id} | ${row.neutral_packet_slot} | ${row.source_fit} | ${row.inherited_table_figure_dataset_policy_required} | ${row.packet_review_fields_filled} |`).join('\n');
  const laneRows = artifact.openintro_packet_lane_group_summary_rows.map((row) => `| ${row.openintro_packet_lane_summary_row_id} | ${row.lane_group} | ${row.packet_alignment_rows} | ${row.local_language_routes_accepted} | ${row.translations_allowed} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Packet-scope review rows: \`${g.openintro_packet_scope_review_rows}\`
- Packet-by-lane alignment rows: \`${g.openintro_packet_lane_alignment_rows}\`
- Lane group summary rows: \`${g.openintro_packet_lane_group_summary_rows}\`
- Blank packet review fields per row: \`${g.blank_packet_review_fields_per_row}\`
- Blank lane alignment fields per row: \`${g.blank_lane_alignment_fields_per_row}\`
- Blank review cells total: \`${g.blank_review_cells_allocated_total}\`

## Packet Rows

| Row | Packet slot | Source fit | File-policy gate | Filled fields |
| --- | --- | --- | --- | ---: |
${packetRows}

## Lane Summaries

| Row | Lane group | Packet alignments | Local routes accepted | Translations allowed |
| --- | --- | ---: | ---: | ---: |
${laneRows}

## Zero Gates

\`0\` packet reviews completed, \`0\` packet-lane reviews completed, \`0\` priority decisions, \`0\` local-language routes accepted, \`0\` native/local sources accepted, \`0\` coordinate scans authorized, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` tables/figures/datasets copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: blank packet-scope review only. This artifact is not source authorization, excerpt selection, source text capture, translation, constructed-language proposal, local authority review, publication claim, or pilot claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [
    ['section', 'row_id', 'packet_slot', 'lane_group', 'source_fit_or_first_use', 'gate_or_still_required', 'fields_filled', 'translation_allowed_now', 'local_surface_allowed_now'].map(csvCell).join(',')
  ];
  for (const row of artifact.openintro_packet_scope_review_rows) {
    rows.push([
      'openintro_packet_scope_review_row',
      row.openintro_packet_scope_review_row_id,
      row.neutral_packet_slot,
      '',
      row.source_fit,
      row.still_required_before_use,
      row.packet_review_fields_filled,
      row.translation_allowed_now,
      row.local_surface_allowed_now
    ].map(csvCell).join(','));
  }
  for (const row of artifact.openintro_packet_lane_alignment_rows) {
    rows.push([
      'openintro_packet_lane_alignment_row',
      row.openintro_packet_lane_alignment_row_id,
      row.neutral_packet_slot,
      row.lane_group,
      row.inherited_lane_first_use,
      row.inherited_lane_gate,
      row.lane_alignment_fields_filled,
      row.translation_allowed_now,
      row.local_surface_allowed_now
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
    status: 'pointer_only_package163_openintro_numeracy_packet_scope_review_template_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: 'Package 163 records a blank OpenIntro IMS numeracy packet-scope review template and packet-by-lane alignment scaffold.',
    counts: {
      openintro_packet_scope_review_rows: g.openintro_packet_scope_review_rows,
      openintro_packet_lane_alignment_rows: g.openintro_packet_lane_alignment_rows,
      blank_review_cells_allocated_total: g.blank_review_cells_allocated_total
    },
    zero_gates: {
      packet_scope_reviews_completed: 0,
      packet_lane_alignment_reviews_completed: 0,
      local_language_routes_accepted: 0,
      native_or_local_sources_accepted: 0,
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
  return `# Package 163 OpenIntro Numeracy Packet-Scope Review Template Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 163 records \`${g.openintro_packet_scope_review_rows}\` blank packet-scope rows, \`${g.openintro_packet_lane_alignment_rows}\` blank packet-by-lane alignment rows, and \`${g.blank_review_cells_allocated_total}\` blank review cells for OpenIntro IMS statistics/public numeracy.

Zero gates: \`0\` packet reviews completed, \`0\` lane alignments completed, \`0\` local routes accepted, \`0\` native/local sources accepted, \`0\` coordinate scans, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` tables/figures/datasets copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: blank packet-scope review template only. This note makes no commit, push, PR, Zenodo, dispatch, return, decision, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_openintro_numeracy_packet_scope_review_template',
    artifact: artifactId,
    current_use: `${g.openintro_packet_scope_review_rows} blank packet-scope review rows; ${g.openintro_packet_lane_alignment_rows} blank packet-lane alignment rows; ${g.blank_review_cells_allocated_total} blank review cells; 0 packet approvals, 0 local routes, 0 source text, 0 excerpts, 0 translations, 0 forms, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_openintro_numeracy_packet_scope_review_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_openintro_numeracy_packet_scope_review_rows: g.openintro_packet_scope_review_rows,
    current_openintro_numeracy_packet_lane_alignment_rows: g.openintro_packet_lane_alignment_rows,
    current_openintro_numeracy_local_language_routes_accepted: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_openintro_numeracy_packet_scope_review_return_or_local_language_source_alignment_template_only_no_source_text_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation OpenIntro numeracy packet-scope review template',
    route: artifactId,
    license_status_to_recheck: 'blank_packet_scope_review_template_only_recheck_OpenIntro_IMS_source_use_attribution_share_alike_local_source_and_local_authority_returns_before_any_excerpt_adaptation_translation_or_surface',
    best_translation_use: 'public numeracy packet candidate catalog and world-family lane alignment scaffold before selected excerpt, local source, local authority, translation, or constructed-surface decisions',
    candidate_lanes: [
      'statistics_public_numeracy',
      'OpenIntro_IMS',
      'data_literacy',
      'public_service_numeracy',
      'packet_scope_review_template',
      'world_family_lane_alignment'
    ],
    priority: 1,
    status: 'blank_packet_scope_review_template_no_reviews_no_local_routes_no_source_text_no_excerpts_no_translation_no_forms_no_pilot',
    gate_state: {
      openintro_packet_scope_review_rows: g.openintro_packet_scope_review_rows,
      openintro_packet_lane_alignment_rows: g.openintro_packet_lane_alignment_rows,
      blank_review_cells_allocated_total: g.blank_review_cells_allocated_total,
      local_language_routes_accepted: 0,
      native_or_local_sources_accepted: 0,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_packet_scope_review_template: ${artifactId}_${g.openintro_packet_scope_review_rows}_packet_rows_${g.openintro_packet_lane_alignment_rows}_lane_rows_0_source_text_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_openintro_numeracy_packet_scope_review_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_packet_scope_review_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_openintro_numeracy_packet_scope_review_rows: g.openintro_packet_scope_review_rows,
    current_openintro_numeracy_packet_lane_alignment_rows: g.openintro_packet_lane_alignment_rows,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    current_openintro_numeracy_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_openintro_numeracy_packet_scope_review_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_openintro_numeracy_packet_scope_review_template: ${artifactId}_blank_packet_scope_before_any_local_routes_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_openintro_numeracy_packet_scope_review_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: records ${g.openintro_packet_scope_review_rows} blank OpenIntro IMS numeracy packet-scope rows and ${g.openintro_packet_lane_alignment_rows} blank packet-by-lane alignment rows; substantive upload-bound artifact; 0 packet approvals, 0 local routes, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OpenIntro numeracy packet-scope review template; ${g.openintro_packet_scope_review_rows} packet rows, ${g.openintro_packet_lane_alignment_rows} packet-lane rows, ${g.blank_review_cells_allocated_total} blank review cells, 0 source text, 0 excerpts, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 163: OpenIntro numeracy packet-scope review template. It records ${g.openintro_packet_scope_review_rows} blank packet-scope rows and ${g.openintro_packet_lane_alignment_rows} blank packet-by-lane alignment rows while keeping 0 packet approvals, 0 local routes, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation OpenIntro numeracy packet-scope review template | ${artifactId} | Blank packet-scope and lane-alignment review template; ${g.openintro_packet_scope_review_rows} packet rows, ${g.openintro_packet_lane_alignment_rows} lane rows, 0 source text, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_packet_scope_review_template_artifact: \`${artifactId}\` (${g.openintro_packet_scope_review_rows} packet rows; ${g.openintro_packet_lane_alignment_rows} packet-lane rows; 0 source text; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_packet_scope_review_template: \`${artifactId}\`; blank OpenIntro IMS numeracy packet-scope review template, no source text, excerpts, local routes, accepted terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OpenIntro IMS public numeracy packet-scope review template; substantive and upload-bound, but not a source excerpt, table, figure, dataset, translation, constructed form, local authority review, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_openintro_numeracy_packet_scope_review_template' },
    { filename: `${artifactId}.md`, class: 'open_translation_openintro_numeracy_packet_scope_review_template' },
    { filename: `${artifactId}.csv`, class: 'open_translation_openintro_numeracy_packet_scope_review_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package163_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package163_coordination_note' },
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
  upload.obj.package163_upload_queue_update = {
    captured_utc: '2026-07-03T11:02:00Z',
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
  const step = 'Stage package 163 OpenIntro numeracy packet-scope review template artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.openintro_packet_scope_review_rows !== artifact.validation_snapshot.expected_packet_scope_review_rows) failures.push(`packet_rows_mismatch_${g.openintro_packet_scope_review_rows}`);
  if (g.openintro_packet_lane_alignment_rows !== artifact.validation_snapshot.expected_packet_lane_alignment_rows) failures.push(`alignment_rows_mismatch_${g.openintro_packet_lane_alignment_rows}`);
  if (g.blank_packet_review_fields_per_row !== artifact.validation_snapshot.expected_blank_packet_review_fields_per_row) failures.push(`packet_fields_mismatch_${g.blank_packet_review_fields_per_row}`);
  if (g.blank_lane_alignment_fields_per_row !== artifact.validation_snapshot.expected_blank_lane_alignment_fields_per_row) failures.push(`lane_fields_mismatch_${g.blank_lane_alignment_fields_per_row}`);
  if (g.blank_review_cells_allocated_total !== artifact.validation_snapshot.expected_blank_review_cells_allocated_total) failures.push(`blank_cells_mismatch_${g.blank_review_cells_allocated_total}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.openintro_packet_scope_review_rows) {
    const filled = packetReviewFields.some((field) => row[field] !== null);
    if (filled || row.packet_review_fields_filled !== 0 || row.packet_scope_review_completed || row.packet_priority_decision_recorded || row.source_text_or_excerpt_allowed_now || row.translation_allowed_now || row.local_surface_allowed_now) {
      failures.push(`nonblank_or_open_packet_row_${row.openintro_packet_scope_review_row_id}`);
      break;
    }
  }
  for (const row of artifact.openintro_packet_lane_alignment_rows) {
    const filled = laneAlignmentFields.some((field) => row[field] !== null);
    if (filled || row.lane_alignment_fields_filled !== 0 || row.packet_lane_alignment_review_completed || row.local_language_route_accepted || row.native_or_local_source_accepted || row.translation_allowed_now || row.local_surface_allowed_now || row.pilot_ready) {
      failures.push(`nonblank_or_open_lane_row_${row.openintro_packet_lane_alignment_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parentInventory = (await readJson(parentInventoryFile)).obj;
const parentPolicy = (await readJson(parentPolicyFile)).obj;
const parentDecision = (await readJson(parentDecisionFile)).obj;
const artifact = buildArtifact(parentInventory, parentPolicy, parentDecision);
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
  openintro_packet_scope_review_rows: artifact.gate_state.openintro_packet_scope_review_rows,
  openintro_packet_lane_alignment_rows: artifact.gate_state.openintro_packet_lane_alignment_rows,
  blank_review_cells_allocated_total: artifact.gate_state.blank_review_cells_allocated_total,
  packet_scope_reviews_completed: artifact.gate_state.packet_scope_reviews_completed,
  local_language_routes_accepted: artifact.gate_state.local_language_routes_accepted,
  native_or_local_sources_accepted: artifact.gate_state.native_or_local_sources_accepted,
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
