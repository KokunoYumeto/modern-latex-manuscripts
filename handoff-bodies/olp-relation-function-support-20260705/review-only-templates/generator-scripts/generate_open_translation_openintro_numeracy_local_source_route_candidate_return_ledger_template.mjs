import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_CANDIDATE_RETURN_LEDGER_TEMPLATE_20260703T114500Z';
const noteId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_CANDIDATE_RETURN_LEDGER_TEMPLATE_NOTE_20260703T114600Z';
const generatedUtc = '2026-07-03T11:45:00Z';
const noteGeneratedUtc = '2026-07-03T11:46:00Z';
const packageOrder = 166;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-OPENINTRO-NUMERACY-LOCAL-SOURCE-ROUTE-CANDIDATE-RETURN-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentCandidateFile = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_CANDIDATE_SHELF_TEMPLATE_20260703T113000Z';
const parentAlignmentFile = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_LANGUAGE_SOURCE_ALIGNMENT_TEMPLATE_20260703T111500Z';

const blankReturnFields = [
  'return_date',
  'reviewer_route_or_role',
  'parent_candidate_row_id_confirmed',
  'candidate_type_decision',
  'actual_route_exists_decision',
  'candidate_source_title_or_route_decision',
  'source_owner_or_steward_decision',
  'license_or_permission_route_decision',
  'terminology_authority_route_decision',
  'modality_route_decision',
  'local_relevance_decision',
  'source_text_capture_decision',
  'next_allowed_artifact',
  'comments_without_source_prose'
];

const zeroGateKeys = [
  'candidate_return_fields_filled',
  'candidate_returns_received',
  'candidate_returns_ingested',
  'actual_source_routes_confirmed',
  'candidate_source_routes_recorded',
  'candidate_source_urls_recorded',
  'candidate_source_owners_recorded',
  'candidate_source_owners_contacted',
  'local_language_routes_accepted',
  'local_source_routes_accepted',
  'native_or_local_sources_accepted',
  'local_license_routes_accepted',
  'local_terminology_authority_routes_accepted',
  'modality_routes_accepted',
  'local_source_alignment_reviews_completed',
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

function buildReturnRows(parentCandidate) {
  return parentCandidate.openintro_local_source_route_candidate_rows.map((row, index) => ({
    openintro_local_source_route_candidate_return_row_id: `OI-LOCAL-ROUTE-RETURN-${String(index + 1).padStart(3, '0')}`,
    parent_candidate_row_id: row.openintro_local_source_route_candidate_row_id,
    parent_local_language_source_alignment_row_id: row.parent_local_language_source_alignment_row_id,
    parent_packet_lane_alignment_row_id: row.parent_packet_lane_alignment_row_id,
    parent_packet_scope_review_row_id: row.parent_packet_scope_review_row_id,
    neutral_packet_slot: row.neutral_packet_slot,
    lane_group: row.lane_group,
    candidate_type: row.candidate_type,
    inherited_source_route_question: row.source_route_question,
    inherited_authority_dependency: row.authority_dependency,
    inherited_modality_dependency: row.modality_dependency,
    inherited_lane_gate: row.inherited_lane_gate,
    blank_return_fields: blankReturnFields,
    return_date: null,
    reviewer_route_or_role: null,
    parent_candidate_row_id_confirmed: null,
    candidate_type_decision: null,
    actual_route_exists_decision: null,
    candidate_source_title_or_route_decision: null,
    source_owner_or_steward_decision: null,
    license_or_permission_route_decision: null,
    terminology_authority_route_decision: null,
    modality_route_decision: null,
    local_relevance_decision: null,
    source_text_capture_decision: null,
    next_allowed_artifact: null,
    comments_without_source_prose: null,
    candidate_return_fields_filled: 0,
    candidate_return_received: false,
    candidate_return_ingested: false,
    actual_source_route_confirmed: false,
    candidate_source_route_recorded: false,
    candidate_source_url_recorded: false,
    candidate_source_owner_recorded: false,
    candidate_source_owner_contacted: false,
    local_language_route_accepted: false,
    local_source_route_accepted: false,
    native_or_local_source_accepted: false,
    local_license_route_accepted: false,
    local_terminology_authority_route_accepted: false,
    modality_route_accepted: false,
    source_text_or_excerpt_allowed_now: false,
    translation_allowed_now: false,
    local_surface_allowed_now: false,
    pilot_ready: false,
    still_locked_reason: 'blank_candidate_return_row_no_return_no_actual_route_no_url_no_owner_no_terms_no_translation'
  }));
}

function summaryRows(rows, groupKey, idPrefix) {
  const map = new Map();
  for (const row of rows) {
    const key = row[groupKey];
    if (!map.has(key)) {
      map.set(key, {
        [`${idPrefix}_summary_row_id`]: `${idPrefix.toUpperCase().replaceAll('_', '-')}-${String(map.size + 1).padStart(2, '0')}`,
        group_key: key,
        return_rows_allocated: 0,
        candidate_returns_received: 0,
        actual_source_routes_confirmed: 0,
        candidate_source_owners_contacted: 0,
        local_source_routes_accepted: 0,
        translated_passages: 0,
        accepted_bridge_surfaces: 0
      });
    }
    map.get(key).return_rows_allocated += 1;
  }
  return [...map.values()].sort((a, b) => a.group_key.localeCompare(b.group_key));
}

function buildArtifact(parentCandidate, parentAlignment) {
  const returnRows = buildReturnRows(parentCandidate);
  const typeSummaryRows = summaryRows(returnRows, 'candidate_type', 'oi_local_route_return_type');
  const packetSummaryRows = summaryRows(returnRows, 'neutral_packet_slot', 'oi_local_route_return_packet');
  const laneSummaryRows = summaryRows(returnRows, 'lane_group', 'oi_local_route_return_lane');
  const blankReturnCells = returnRows.length * blankReturnFields.length;

  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'openintro_numeracy_local_source_route_candidate_return_ledger_template_blank_no_returns_no_actual_routes_no_source_text_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Create a blank return ledger template for every package 165 OpenIntro IMS local source-route candidate row, so future reviewers can record whether actual local routes, owners, permissions, terminology authorities, and modality routes exist without this artifact recording any route, URL, owner, source text, local term, translation, surface, or readiness claim.',
    parent_artifacts: [
      parentCandidateFile,
      parentAlignmentFile,
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_PACKET_SCOPE_REVIEW_TEMPLATE_20260703T110000Z',
      'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z'
    ],
    boundary: {
      artifact_is: [
        'blank local source-route candidate return ledger template',
        'one return row per package 165 candidate row',
        'future intake scaffold for actual local route, owner, permission, terminology, and modality decisions'
      ],
      artifact_is_not: [
        'actual local source shelf',
        'source route return',
        'URL or owner record',
        'source-owner contact',
        'local source acceptance',
        'local terminology authority decision',
        'source text capture',
        'source excerpt selection',
        'translation draft',
        'constructed-language form proposal',
        'pilot or publication readiness claim'
      ],
      fill_rule: 'No return fields are filled here. Future candidate returns must be dated, route-labeled, and must not copy source prose unless a later policy explicitly allows it.',
      promotion_requires: [
        'dated local source route candidate return',
        'actual source route or owner evidence',
        'local license or permission route where required',
        'local terminology authority route where local terms are involved',
        'modality route decision for video/audio/visual/signed-language routes',
        'separate selected-excerpt sidecar before any translation or adaptation'
      ]
    },
    inherited_parent_counts: {
      parent_local_source_route_candidate_rows: parentCandidate.gate_state.openintro_local_source_route_candidate_rows,
      parent_local_language_source_alignment_rows: parentAlignment.gate_state.openintro_local_language_source_alignment_rows,
      parent_candidate_type_rows: parentCandidate.gate_state.source_route_candidate_type_rows
    },
    blank_return_fields: blankReturnFields,
    openintro_local_source_route_candidate_return_rows: returnRows,
    openintro_local_route_return_type_summary_rows: typeSummaryRows,
    openintro_local_route_return_packet_summary_rows: packetSummaryRows,
    openintro_local_route_return_lane_summary_rows: laneSummaryRows,
    gate_state: {
      openintro_local_source_route_candidate_return_rows: returnRows.length,
      local_route_return_type_summary_rows: typeSummaryRows.length,
      local_route_return_packet_summary_rows: packetSummaryRows.length,
      local_route_return_lane_summary_rows: laneSummaryRows.length,
      blank_return_fields_per_row: blankReturnFields.length,
      blank_return_field_cells_allocated: blankReturnCells,
      candidate_return_fields_filled: 0,
      candidate_returns_received: 0,
      candidate_returns_ingested: 0,
      actual_source_routes_confirmed: 0,
      candidate_source_routes_recorded: 0,
      candidate_source_urls_recorded: 0,
      candidate_source_owners_recorded: 0,
      candidate_source_owners_contacted: 0,
      local_language_routes_accepted: 0,
      local_source_routes_accepted: 0,
      native_or_local_sources_accepted: 0,
      local_license_routes_accepted: 0,
      local_terminology_authority_routes_accepted: 0,
      modality_routes_accepted: 0,
      local_source_alignment_reviews_completed: 0,
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
      expected_local_source_route_candidate_return_rows: parentCandidate.gate_state.openintro_local_source_route_candidate_rows,
      expected_type_summary_rows: parentCandidate.gate_state.source_route_candidate_type_rows,
      expected_packet_summary_rows: parentCandidate.gate_state.local_route_packet_summary_rows,
      expected_lane_summary_rows: parentCandidate.gate_state.local_route_lane_summary_rows,
      expected_blank_return_fields_per_row: blankReturnFields.length,
      expected_blank_return_field_cells_allocated: blankReturnCells,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_CANDIDATE_RETURN_LEDGER_WITH_RETURNS_<timestamp>_only_after_dated_returns',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_EVIDENCE_CRITERIA_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SELECTED_EXCERPT_SIDECAR_TEMPLATE_<timestamp>_only_after_policy_attribution_packet_local_source_and_route_returns'
    ],
    decision: 'Package 166 allocates blank local source-route candidate return rows only. It records no actual source routes, no URLs, no owners, no contacts, no local terms, no source text, no excerpts, no translations, no constructed forms, and no readiness claims.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const typeRows = artifact.openintro_local_route_return_type_summary_rows.map((row) => `| ${row.oi_local_route_return_type_summary_row_id} | ${row.group_key} | ${row.return_rows_allocated} | ${row.candidate_returns_received} | ${row.actual_source_routes_confirmed} |`).join('\n');
  const packetRows = artifact.openintro_local_route_return_packet_summary_rows.map((row) => `| ${row.oi_local_route_return_packet_summary_row_id} | ${row.group_key} | ${row.return_rows_allocated} | ${row.local_source_routes_accepted} |`).join('\n');
  const laneRows = artifact.openintro_local_route_return_lane_summary_rows.map((row) => `| ${row.oi_local_route_return_lane_summary_row_id} | ${row.group_key} | ${row.return_rows_allocated} | ${row.local_source_routes_accepted} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Local source-route candidate return rows: \`${g.openintro_local_source_route_candidate_return_rows}\`
- Blank return fields per row: \`${g.blank_return_fields_per_row}\`
- Blank return-field cells: \`${g.blank_return_field_cells_allocated}\`

## Candidate-Type Summary

| Row | Candidate type | Return rows | Returns received | Actual routes confirmed |
| --- | --- | ---: | ---: | ---: |
${typeRows}

## Packet Summary

| Row | Packet slot | Return rows | Local source routes accepted |
| --- | --- | ---: | ---: |
${packetRows}

## Lane Summary

| Row | Lane group | Return rows | Local source routes accepted |
| --- | --- | ---: | ---: |
${laneRows}

## Zero Gates

\`0\` return fields filled, \`0\` candidate returns received, \`0\` actual source routes confirmed, \`0\` source routes/URLs/owners recorded, \`0\` owner contacts, \`0\` local routes accepted, \`0\` local terms accepted, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: blank local source-route candidate return ledger template only. This artifact is not source discovery, source-route evidence, source-owner contact, source authorization, translation, constructed-language proposal, publication claim, or pilot claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [
    ['section', 'return_row_id', 'parent_candidate_row_id', 'packet_slot', 'lane_group', 'candidate_type', 'fields_filled', 'return_received', 'actual_route_confirmed', 'source_owner_contacted'].map(csvCell).join(',')
  ];
  for (const row of artifact.openintro_local_source_route_candidate_return_rows) {
    rows.push([
      'openintro_local_source_route_candidate_return_row',
      row.openintro_local_source_route_candidate_return_row_id,
      row.parent_candidate_row_id,
      row.neutral_packet_slot,
      row.lane_group,
      row.candidate_type,
      row.candidate_return_fields_filled,
      row.candidate_return_received,
      row.actual_source_route_confirmed,
      row.candidate_source_owner_contacted
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
    status: 'pointer_only_package166_openintro_numeracy_local_source_route_candidate_return_ledger_template_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: 'Package 166 records a blank OpenIntro IMS numeracy local source-route candidate return ledger template derived from package 165 candidate rows.',
    counts: {
      openintro_local_source_route_candidate_return_rows: g.openintro_local_source_route_candidate_return_rows,
      blank_return_fields_per_row: g.blank_return_fields_per_row,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated
    },
    zero_gates: {
      candidate_return_fields_filled: 0,
      candidate_returns_received: 0,
      actual_source_routes_confirmed: 0,
      candidate_source_routes_recorded: 0,
      candidate_source_urls_recorded: 0,
      candidate_source_owners_contacted: 0,
      local_source_routes_accepted: 0,
      accepted_local_language_terms: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
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
  return `# Package 166 OpenIntro Numeracy Local Source-Route Candidate Return Ledger Template Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 166 records \`${g.openintro_local_source_route_candidate_return_rows}\` blank local source-route candidate return rows and \`${g.blank_return_field_cells_allocated}\` blank return-field cells for OpenIntro IMS statistics/public numeracy.

Zero gates: \`0\` return fields filled, \`0\` candidate returns received, \`0\` actual source routes confirmed, \`0\` source routes/URLs/owners recorded, \`0\` owner contacts, \`0\` local routes accepted, \`0\` local terms accepted, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: blank local source-route candidate return ledger template only. This note makes no commit, push, PR, Zenodo, dispatch, return, actual route record, source-owner contact, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_openintro_numeracy_local_source_route_candidate_return_ledger_template',
    artifact: artifactId,
    current_use: `${g.openintro_local_source_route_candidate_return_rows} blank local source-route candidate return rows; ${g.blank_return_field_cells_allocated} blank return-field cells; 0 returns, 0 actual routes, 0 URLs, 0 owners, 0 contacts, 0 source text, 0 translations, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_openintro_numeracy_local_source_route_candidate_return_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_openintro_numeracy_local_source_route_candidate_return_rows: g.openintro_local_source_route_candidate_return_rows,
    current_openintro_numeracy_candidate_returns_received: 0,
    current_openintro_numeracy_actual_source_routes_confirmed: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_local_source_route_evidence_criteria_template_only_no_returns_no_actual_routes_no_source_text_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation OpenIntro numeracy local source-route candidate return ledger template',
    route: artifactId,
    license_status_to_recheck: 'blank_candidate_return_ledger_only_recheck_actual_local_source_routes_owners_permissions_terminology_authority_and_modality_returns_before_any_excerpt_adaptation_translation_or_surface',
    best_translation_use: 'blank return scaffold for local source-route candidate review before source route evidence, selected excerpt, local terms, translation, or constructed-surface decisions',
    candidate_lanes: [
      'statistics_public_numeracy',
      'OpenIntro_IMS',
      'data_literacy',
      'public_service_numeracy',
      'local_source_route_candidate_return_template',
      'world_family_lane_alignment'
    ],
    priority: 1,
    status: 'blank_local_source_route_candidate_return_ledger_template_no_returns_no_actual_routes_no_urls_no_source_owners_no_terms_no_source_text_no_translation_no_forms_no_pilot',
    gate_state: {
      openintro_local_source_route_candidate_return_rows: g.openintro_local_source_route_candidate_return_rows,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated,
      candidate_returns_received: 0,
      actual_source_routes_confirmed: 0,
      candidate_source_routes_recorded: 0,
      candidate_source_urls_recorded: 0,
      candidate_source_owners_contacted: 0,
      accepted_local_language_terms: 0,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_local_source_route_candidate_return_ledger_template: ${artifactId}_${g.openintro_local_source_route_candidate_return_rows}_blank_return_rows_0_actual_routes_0_source_text_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_openintro_numeracy_local_source_route_candidate_return_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_local_source_route_candidate_return_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_openintro_numeracy_local_source_route_candidate_return_rows: g.openintro_local_source_route_candidate_return_rows,
    current_openintro_numeracy_actual_source_routes_confirmed: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    current_openintro_numeracy_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_openintro_numeracy_local_source_route_candidate_return_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_openintro_numeracy_local_source_route_candidate_return_ledger_template: ${artifactId}_blank_return_ledger_before_any_returns_actual_routes_terms_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_openintro_numeracy_local_source_route_candidate_return_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: records ${g.openintro_local_source_route_candidate_return_rows} blank OpenIntro IMS numeracy local source-route candidate return rows; substantive upload-bound artifact; 0 returns, 0 actual routes, 0 URLs, 0 owners, 0 contacts, 0 local terms, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OpenIntro numeracy local source-route candidate return ledger template; ${g.openintro_local_source_route_candidate_return_rows} blank return rows, ${g.blank_return_field_cells_allocated} blank cells, 0 returns, 0 actual routes, 0 source text, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 166: OpenIntro numeracy local source-route candidate return ledger template. It records ${g.openintro_local_source_route_candidate_return_rows} blank return rows while keeping 0 returns received, 0 actual routes, 0 URLs, 0 owners, 0 source-owner contacts, 0 local terms, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation OpenIntro numeracy local source-route candidate return ledger template | ${artifactId} | Blank local source-route candidate return ledger; ${g.openintro_local_source_route_candidate_return_rows} rows, 0 returns, 0 actual routes, 0 source text, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_local_source_route_candidate_return_ledger_template_artifact: \`${artifactId}\` (${g.openintro_local_source_route_candidate_return_rows} blank return rows; 0 actual routes; 0 source text; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_local_source_route_candidate_return_ledger_template: \`${artifactId}\`; blank OpenIntro IMS numeracy local source-route candidate return ledger template, no returns, actual routes, source text, excerpts, local terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OpenIntro IMS public numeracy local source-route candidate return ledger template; substantive and upload-bound, but not actual source discovery, source text, translation, constructed form, local authority review, source-owner contact, local term decision, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_openintro_numeracy_local_source_route_candidate_return_ledger_template' },
    { filename: `${artifactId}.md`, class: 'open_translation_openintro_numeracy_local_source_route_candidate_return_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'open_translation_openintro_numeracy_local_source_route_candidate_return_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package166_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package166_coordination_note' },
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
  upload.obj.package166_upload_queue_update = {
    captured_utc: '2026-07-03T11:47:00Z',
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
  const step = 'Stage package 166 OpenIntro numeracy local source-route candidate return ledger template artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.openintro_local_source_route_candidate_return_rows !== artifact.validation_snapshot.expected_local_source_route_candidate_return_rows) failures.push(`return_rows_mismatch_${g.openintro_local_source_route_candidate_return_rows}`);
  if (g.local_route_return_type_summary_rows !== artifact.validation_snapshot.expected_type_summary_rows) failures.push(`type_summary_rows_mismatch_${g.local_route_return_type_summary_rows}`);
  if (g.local_route_return_packet_summary_rows !== artifact.validation_snapshot.expected_packet_summary_rows) failures.push(`packet_summary_rows_mismatch_${g.local_route_return_packet_summary_rows}`);
  if (g.local_route_return_lane_summary_rows !== artifact.validation_snapshot.expected_lane_summary_rows) failures.push(`lane_summary_rows_mismatch_${g.local_route_return_lane_summary_rows}`);
  if (g.blank_return_fields_per_row !== artifact.validation_snapshot.expected_blank_return_fields_per_row) failures.push(`blank_fields_mismatch_${g.blank_return_fields_per_row}`);
  if (g.blank_return_field_cells_allocated !== artifact.validation_snapshot.expected_blank_return_field_cells_allocated) failures.push(`blank_cells_mismatch_${g.blank_return_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.openintro_local_source_route_candidate_return_rows) {
    const filled = blankReturnFields.some((field) => row[field] !== null);
    if (
      filled ||
      row.candidate_return_fields_filled !== 0 ||
      row.candidate_return_received ||
      row.candidate_return_ingested ||
      row.actual_source_route_confirmed ||
      row.candidate_source_route_recorded ||
      row.candidate_source_url_recorded ||
      row.candidate_source_owner_recorded ||
      row.candidate_source_owner_contacted ||
      row.local_language_route_accepted ||
      row.local_source_route_accepted ||
      row.native_or_local_source_accepted ||
      row.local_license_route_accepted ||
      row.local_terminology_authority_route_accepted ||
      row.modality_route_accepted ||
      row.source_text_or_excerpt_allowed_now ||
      row.translation_allowed_now ||
      row.local_surface_allowed_now ||
      row.pilot_ready
    ) {
      failures.push(`nonblank_or_open_return_row_${row.openintro_local_source_route_candidate_return_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parentCandidate = (await readJson(parentCandidateFile)).obj;
const parentAlignment = (await readJson(parentAlignmentFile)).obj;
const artifact = buildArtifact(parentCandidate, parentAlignment);
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
  openintro_local_source_route_candidate_return_rows: artifact.gate_state.openintro_local_source_route_candidate_return_rows,
  blank_return_field_cells_allocated: artifact.gate_state.blank_return_field_cells_allocated,
  candidate_returns_received: artifact.gate_state.candidate_returns_received,
  actual_source_routes_confirmed: artifact.gate_state.actual_source_routes_confirmed,
  candidate_source_routes_recorded: artifact.gate_state.candidate_source_routes_recorded,
  candidate_source_urls_recorded: artifact.gate_state.candidate_source_urls_recorded,
  candidate_source_owners_contacted: artifact.gate_state.candidate_source_owners_contacted,
  local_source_routes_accepted: artifact.gate_state.local_source_routes_accepted,
  accepted_local_language_terms: artifact.gate_state.accepted_local_language_terms,
  source_text_copied: artifact.gate_state.source_text_copied,
  translated_passages: artifact.gate_state.translated_passages,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
