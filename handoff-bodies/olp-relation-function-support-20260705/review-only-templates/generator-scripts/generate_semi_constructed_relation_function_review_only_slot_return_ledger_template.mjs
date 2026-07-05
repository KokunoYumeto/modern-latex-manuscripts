import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SLOT_RETURN_LEDGER_TEMPLATE_20260703T071500Z';
const noteId = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SLOT_RETURN_LEDGER_TEMPLATE_NOTE_20260703T071600Z';
const generatedUtc = '2026-07-03T07:15:00Z';
const noteGeneratedUtc = '2026-07-03T07:16:00Z';
const packageOrder = 148;
const queueCandidateId = 'OTCQ-SEMI-CONSTRUCTED-RELATION-FUNCTION-REVIEW-ONLY-SLOT-RETURN-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentSeedIndex = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_CONSTRUCTION_SEED_START_INDEX_20260703T070000Z';
const parentArtifacts = [
  parentSeedIndex,
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_TRANSLATION_CANDIDATE_CATALOG_20260701T180000Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_CANDIDATE_REVIEWER_ROUTE_SHEET_20260701T183000Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_CANDIDATE_DISPATCH_EVIDENCE_CRITERIA_AND_ROUTE_LABEL_TAXONOMY_20260701T213000Z'
];

const blankReturnFields = [
  'return_date',
  'reviewer_route_label',
  'slot_boundary_status',
  'local_standard_required_before_surface',
  'source_file_hint_rank',
  'exact_passage_request_allowed_boolean_only',
  'bridge_surface_sidecar_required_boolean_only',
  'no_construction_trigger',
  'next_gate_recommendation',
  'return_note'
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

function openSeedRows(parent) {
  return parent.review_only_construction_seed_rows.filter((row) => row.slot_envelope_opened);
}

function buildSlotReturnRows(parent) {
  const rows = [];
  for (const seedRow of openSeedRows(parent)) {
    seedRow.abstract_semantic_slot_envelope.forEach((slotName, slotIndex) => {
      const index = rows.length + 1;
      rows.push({
        slot_return_row_id: `DMOI-RF-ROCSI-SRET-${String(index).padStart(3, '0')}`,
        parent_seed_row_id: seedRow.seed_row_id,
        parent_catalog_row_id: seedRow.parent_catalog_row_id,
        parent_route_row_id: seedRow.parent_route_row_id,
        candidate_area: seedRow.candidate_area,
        selected_packet_shape: seedRow.selected_packet_shape,
        reviewer_role_route_label: seedRow.reviewer_role_route_label,
        slot_name: slotName,
        slot_index_within_seed: slotIndex + 1,
        linked_routes: seedRow.linked_routes,
        linked_term_families: seedRow.linked_term_families,
        source_file_hints_for_ranking_only: seedRow.source_file_hints_for_ranking_only,
        coordinate_rows_available_for_parent_area: seedRow.coordinate_rows_available,
        allowed_return_fields: blankReturnFields,
        return_date: null,
        reviewer_route_label: null,
        slot_boundary_status: null,
        local_standard_required_before_surface: null,
        source_file_hint_rank: null,
        exact_passage_request_allowed_boolean_only: null,
        bridge_surface_sidecar_required_boolean_only: null,
        no_construction_trigger: null,
        next_gate_recommendation: null,
        return_note: null,
        return_fields_filled: 0,
        dated_return_present: false,
        reviewer_return_ingested: false,
        slot_boundary_confirmed: false,
        slot_approved_for_surface_sidecar: false,
        slot_held_for_more_evidence: false,
        no_construction_decision_recorded: false,
        source_text_or_excerpt_allowed_after_return: false,
        exact_span_allowed_after_return: false,
        bridge_surface_proposal_allowed_after_return: false,
        translation_allowed_after_return: false,
        still_locked_reason: 'missing_dated_slot_return_local_standard_gate_license_attribution_gate_surface_sidecar_and_completion_audit'
      });
    });
  }
  return rows;
}

function buildSeedSummaryRows(parent, slotReturnRows) {
  return openSeedRows(parent).map((seedRow, index) => {
    const linked = slotReturnRows.filter((row) => row.parent_seed_row_id === seedRow.seed_row_id);
    return {
      slot_return_seed_summary_row_id: `DMOI-RF-ROCSI-SRET-SEED-${String(index + 1).padStart(2, '0')}`,
      parent_seed_row_id: seedRow.seed_row_id,
      parent_catalog_row_id: seedRow.parent_catalog_row_id,
      candidate_area: seedRow.candidate_area,
      selected_packet_shape: seedRow.selected_packet_shape,
      slot_return_rows_required: linked.length,
      return_fields_filled: 0,
      dated_returns_present: 0,
      reviewer_returns_ingested: 0,
      slots_confirmed: 0,
      slots_approved_for_surface_sidecar: 0,
      slots_held_for_more_evidence: 0,
      no_construction_decisions_recorded: 0,
      linked_slot_return_row_ids: linked.map((row) => row.slot_return_row_id)
    };
  });
}

function buildPacketShapeSummaryRows(slotReturnRows) {
  const shapes = [...new Set(slotReturnRows.map((row) => row.selected_packet_shape))];
  return shapes.map((shape, index) => {
    const linked = slotReturnRows.filter((row) => row.selected_packet_shape === shape);
    return {
      slot_return_packet_shape_summary_row_id: `DMOI-RF-ROCSI-SRET-PACKET-${String(index + 1).padStart(2, '0')}`,
      selected_packet_shape: shape,
      slot_return_rows_required: linked.length,
      return_fields_filled: 0,
      dated_returns_present: 0,
      reviewer_returns_ingested: 0,
      source_text_or_excerpt_allowed: false,
      bridge_surface_proposal_allowed: false,
      translation_allowed: false,
      linked_slot_return_row_ids: linked.map((row) => row.slot_return_row_id)
    };
  });
}

function buildArtifact(parent) {
  const slotReturnRows = buildSlotReturnRows(parent);
  const seedSummaryRows = buildSeedSummaryRows(parent, slotReturnRows);
  const packetShapeSummaryRows = buildPacketShapeSummaryRows(slotReturnRows);
  const blankReturnCells = slotReturnRows.length * blankReturnFields.length;
  const parentGate = parent.gate_state || {};
  const openParentRows = openSeedRows(parent);
  const parentCoordinateRows = openParentRows.reduce((sum, row) => sum + row.coordinate_rows_available, 0);
  const parentSourceFileHints = openParentRows.reduce((sum, row) => sum + row.source_file_hints_for_ranking_only.length, 0);
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'review_only_slot_return_ledger_template_blank_no_returns_no_forms_no_source_text_no_excerpts_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Allocate blank return rows for each P147 review-only abstract semantic slot so future reviewers can confirm, hold, redirect, or trigger no-construction decisions without proposing forms, copying source text, selecting excerpts, dispatching packets, or drafting translations.',
    parent_artifacts: parentArtifacts,
    slot_return_boundary: {
      ledger_is: 'blank return ledger template for abstract review-only semantic slots',
      ledger_is_not: [
        'received reviewer return',
        'ingested reviewer return',
        'surface sidecar',
        'bridge lexeme proposal',
        'bridge morpheme proposal',
        'accepted local-language term',
        'source excerpt request fulfilled',
        'source text copy',
        'translation draft',
        'pilot or publication claim'
      ],
      allowed_now: [
        'allocate return rows for each abstract slot',
        'state what a future return may decide',
        'keep all source, form, surface, translation, and readiness gates closed'
      ],
      promotion_requires: [
        'dated reviewer return',
        'local-standard gate note',
        'license/attribution gate note before exact source passage use',
        'separate blank surface sidecar before any proposed form',
        'explicit no-construction decision where a slot should remain closed'
      ]
    },
    blank_return_fields: blankReturnFields,
    review_only_slot_return_rows: slotReturnRows,
    seed_slot_return_summary_rows: seedSummaryRows,
    packet_shape_slot_return_summary_rows: packetShapeSummaryRows,
    gate_state: {
      review_only_slot_return_rows: slotReturnRows.length,
      parent_review_only_seed_rows_opened: openParentRows.length,
      parent_review_only_slots_named: parentGate.construction_slots_named_for_review_only || slotReturnRows.length,
      seed_slot_return_summary_rows: seedSummaryRows.length,
      packet_shape_slot_return_summary_rows: packetShapeSummaryRows.length,
      blank_return_fields_per_row: blankReturnFields.length,
      blank_return_field_cells_allocated: blankReturnCells,
      parent_source_coordinate_rows_referenced_as_metadata: parentCoordinateRows,
      parent_source_file_hints_referenced_as_metadata: parentSourceFileHints,
      return_fields_filled: 0,
      dated_returns_present: 0,
      reviewer_returns_ingested: 0,
      slot_boundaries_confirmed: 0,
      slots_approved_for_surface_sidecar: 0,
      slots_held_for_more_evidence: 0,
      no_construction_decisions_recorded: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_definitions_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      exact_line_spans_selected: 0,
      candidate_line_ranges_selected: 0,
      proposed_bridge_lexemes: 0,
      proposed_bridge_morphemes: 0,
      proposed_bridge_grammar_rules: 0,
      accepted_bridge_surfaces: 0,
      accepted_local_language_terms: 0,
      local_language_surfaces_filled: 0,
      translated_passages: 0,
      publication_ready: false,
      translation_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      expected_slot_return_rows: 17,
      expected_parent_seed_rows_opened: 4,
      expected_blank_return_fields_per_row: blankReturnFields.length,
      expected_blank_return_field_cells_allocated: blankReturnCells,
      zero_gate_assertions: [
        'return_fields_filled',
        'dated_returns_present',
        'reviewer_returns_ingested',
        'slot_boundaries_confirmed',
        'slots_approved_for_surface_sidecar',
        'slots_held_for_more_evidence',
        'no_construction_decisions_recorded',
        'source_text_or_excerpt_files_created',
        'source_text_copied',
        'source_definitions_copied',
        'source_examples_copied',
        'source_passages_selected',
        'exact_line_spans_selected',
        'candidate_line_ranges_selected',
        'proposed_bridge_lexemes',
        'proposed_bridge_morphemes',
        'proposed_bridge_grammar_rules',
        'accepted_bridge_surfaces',
        'accepted_local_language_terms',
        'local_language_surfaces_filled',
        'translated_passages'
      ],
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SURFACE_SIDECAR_TEMPLATE_BLANK_<timestamp>',
      'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SLOT_RETURN_LEDGER_WITH_RETURNS_<timestamp>',
      'SEMI_CONSTRUCTED_RELATION_FUNCTION_NO_CONSTRUCTION_DECISION_LEDGER_<timestamp>'
    ],
    decision: 'Package 148 allocates blank slot-return rows only. It does not approve any slot for surface work, does not propose any forms, and does not open source-text, excerpt, translation, pilot, or publication gates.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const rows = artifact.review_only_slot_return_rows.map((row) => `| ${row.slot_return_row_id} | ${row.parent_seed_row_id} | ${row.slot_name} | ${row.candidate_area} | ${row.return_fields_filled} |`).join('\n');
  const seedRows = artifact.seed_slot_return_summary_rows.map((row) => `| ${row.slot_return_seed_summary_row_id} | ${row.parent_seed_row_id} | ${row.candidate_area} | ${row.slot_return_rows_required} | ${row.dated_returns_present} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Slot-return rows: \`${g.review_only_slot_return_rows}\`
- Parent opened seed rows: \`${g.parent_review_only_seed_rows_opened}\`
- Parent slots named: \`${g.parent_review_only_slots_named}\`
- Blank return fields per row: \`${g.blank_return_fields_per_row}\`
- Blank return-field cells: \`${g.blank_return_field_cells_allocated}\`
- Parent source-coordinate rows referenced as metadata: \`${g.parent_source_coordinate_rows_referenced_as_metadata}\`
- Parent source-file hints referenced as metadata: \`${g.parent_source_file_hints_referenced_as_metadata}\`

## Slot Rows

| Row | Parent seed | Slot | Candidate area | Filled fields |
| --- | --- | --- | --- | ---: |
${rows}

## Seed Summary

| Row | Parent seed | Candidate area | Slot returns required | Dated returns present |
| --- | --- | --- | ---: | ---: |
${seedRows}

## Zero Gates

- Dated returns / ingested returns: \`0 / 0\`
- Slot boundaries confirmed / slots approved for sidecar: \`0 / 0\`
- No-construction decisions recorded: \`0\`
- Source text/excerpt files: \`0\`
- Source text/definitions/examples copied: \`0 / 0 / 0\`
- Exact spans / candidate line ranges: \`0 / 0\`
- Proposed bridge lexemes/morphemes/grammar rules: \`0 / 0 / 0\`
- Accepted bridge/local surfaces: \`0 / 0\`
- Translated passages: \`0\`
- Readiness: \`publication=false, translation=false, constructed_surface=false, pilot=false\`

Boundary: this is a blank slot-return ledger template only. It is not a reviewer return, surface sidecar, proposed form, accepted term, source excerpt, translation, dispatch, pilot, or publication artifact.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'parent_seed_row_id', 'slot_or_packet', 'candidate_area', 'blank_fields', 'filled_fields', 'gate_open'].map(csvCell).join(','));
  for (const row of artifact.review_only_slot_return_rows) {
    rows.push([
      'slot_return_row',
      row.slot_return_row_id,
      row.parent_seed_row_id,
      row.slot_name,
      row.candidate_area,
      row.allowed_return_fields.length,
      row.return_fields_filled,
      row.bridge_surface_proposal_allowed_after_return || row.translation_allowed_after_return
    ].map(csvCell).join(','));
  }
  for (const row of artifact.seed_slot_return_summary_rows) {
    rows.push([
      'seed_summary',
      row.slot_return_seed_summary_row_id,
      row.parent_seed_row_id,
      row.selected_packet_shape,
      row.candidate_area,
      row.slot_return_rows_required,
      row.return_fields_filled,
      false
    ].map(csvCell).join(','));
  }
  for (const row of artifact.packet_shape_slot_return_summary_rows) {
    rows.push([
      'packet_shape_summary',
      row.slot_return_packet_shape_summary_row_id,
      '',
      row.selected_packet_shape,
      '',
      row.slot_return_rows_required,
      row.return_fields_filled,
      row.bridge_surface_proposal_allowed || row.translation_allowed
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
    status: 'pointer_only_package148_slot_return_ledger_template_note_no_upload_coordination_no_source_text_no_translation_no_readiness',
    summary: 'Package 148 queues a blank return ledger template for the 17 P147 review-only semantic slots.',
    counts: {
      review_only_slot_return_rows: g.review_only_slot_return_rows,
      parent_review_only_seed_rows_opened: g.parent_review_only_seed_rows_opened,
      parent_review_only_slots_named: g.parent_review_only_slots_named,
      blank_return_fields_per_row: g.blank_return_fields_per_row,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated
    },
    zero_gates: {
      dated_returns_present: 0,
      reviewer_returns_ingested: 0,
      slots_approved_for_surface_sidecar: 0,
      source_text_or_excerpt_files_created: 0,
      proposed_bridge_lexemes: 0,
      proposed_bridge_morphemes: 0,
      accepted_bridge_surfaces: 0,
      accepted_local_language_terms: 0,
      translated_passages: 0,
      readiness_claims: 0
    },
    no_remote_action_by_this_note: true
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 148 Slot-Return Ledger Template Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 148 creates \`${g.review_only_slot_return_rows}\` blank slot-return rows for the \`${g.parent_review_only_slots_named}\` abstract review-only slots opened by P147. It allocates \`${g.blank_return_fields_per_row}\` blank fields per row and \`${g.blank_return_field_cells_allocated}\` blank return-field cells.

Zero gates: \`0\` dated returns, \`0\` ingested returns, \`0\` slots approved for surface sidecars, \`0\` source-text/excerpt files, \`0\` proposed bridge lexemes, \`0\` proposed bridge morphemes, \`0\` accepted bridge or local surfaces, \`0\` translations, \`0\` readiness claims.

Boundary: slot-return ledger template only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
  if (!order.some((row) => row?.artifact === artifactId)) {
    order.push({
      order: packageOrder,
      role: 'semi_constructed_relation_function_review_only_slot_return_ledger_template_support',
      artifact: artifactId,
      current_use: '17 blank slot-return rows; 10 return fields per row; 170 blank return-field cells; 0 returns, 0 source text, 0 forms, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_semi_constructed_relation_function_review_only_slot_return_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_relation_function_review_only_slot_return_rows: g.review_only_slot_return_rows,
    current_relation_function_review_only_slot_return_blank_cells: g.blank_return_field_cells_allocated,
    current_relation_function_review_only_slot_returns_ingested: 0,
    current_relation_function_review_only_slot_source_text_or_excerpt_files: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_blank_surface_sidecar_or_slot_returns_only_after_dated_return_no_source_text_no_excerpts_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Semi-constructed relation/function review-only slot-return ledger template',
    route: artifactId,
    license_status_to_recheck: 'blank_return_template_only_no_source_text_no_excerpts_recheck_exact_source_before_any_passage_or_adaptation',
    best_translation_use: 'review-only return capture for abstract relation/function slots before surface sidecar or translation work',
    candidate_lanes: [
      'relation_function_bridge_register',
      'set_function_packet',
      'proof_literacy_micro_packet',
      'review_only_construction_seed',
      'slot_return_ledger'
    ],
    priority: 1,
    status: 'slot_return_ledger_template_no_returns_no_source_text_no_forms_no_translation_no_pilot',
    gate_state: {
      review_only_slot_return_rows: g.review_only_slot_return_rows,
      blank_return_field_cells_allocated: g.blank_return_field_cells_allocated,
      dated_returns_present: 0,
      reviewer_returns_ingested: 0,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      source_text_or_excerpt_files_created: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_semi_constructed_relation_function_review_only_slot_return_ledger_template: ${artifactId}_17_blank_return_rows_170_blank_cells_0_returns_0_forms_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_semi_constructed_relation_function_review_only_slot_return_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_semi_constructed_relation_function_review_only_slot_return_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_relation_function_review_only_slot_return_rows: g.review_only_slot_return_rows,
    current_relation_function_review_only_slot_return_blank_cells: g.blank_return_field_cells_allocated,
    current_relation_function_review_only_slot_returns_ingested: 0,
    current_relation_function_review_only_slot_source_text_or_excerpt_files: 0,
    current_relation_function_review_only_slot_surfaces: 0,
    current_relation_function_review_only_slot_translations: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_semi_constructed_relation_function_review_only_slot_return_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_semi_constructed_relation_function_review_only_slot_return_ledger_template: ${artifactId}_blank_slot_returns_no_forms_no_source_text_no_excerpts_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_semi_constructed_relation_function_review_only_slot_return_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 17 blank return rows for P147 abstract relation/function semantic slots and 170 blank return-field cells; 0 returns, 0 source text, 0 excerpts, 0 bridge lexemes, 0 morphemes, 0 accepted surfaces, 0 local-language terms, 0 translations, 0 readiness; local upload queue should preserve it as substantive construction-method material.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - Semi-constructed relation/function review-only slot-return ledger template; 17 blank return rows, 170 blank cells, 0 returns, 0 source text, 0 excerpts, 0 bridge lexemes, 0 morphemes, 0 accepted surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 148: review-only semi-constructed relation/function slot-return ledger template. It allocates 17 blank return rows and 170 blank return-field cells for P147 abstract slots while keeping 0 returns, 0 source text, 0 excerpts, 0 proposed forms, 0 accepted surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Semi-constructed relation/function review-only slot-return ledger template | ${artifactId} | Blank slot-return scaffold; 17 return rows, 170 blank cells, 0 returns, 0 source text, 0 excerpts, 0 proposed forms, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_semi_constructed_relation_function_review_only_slot_return_ledger_template_artifact: \`${artifactId}\` (17 blank slot-return rows; 170 blank cells; 0 returns; 0 source text; 0 excerpts; no surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_semi_constructed_relation_function_review_only_slot_return_ledger_template: \`${artifactId}\`; blank slot-return ledger only, no returns, source text, excerpts, proposed bridge forms, accepted local terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: creates blank return rows for the DMOI relation/function review-only abstract slots; rows are not reviewer returns, proposed forms, accepted local-language terms, source excerpts, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'semi_constructed_relation_function_review_only_slot_return_ledger_template' },
    { filename: `${artifactId}.md`, class: 'semi_constructed_relation_function_review_only_slot_return_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'semi_constructed_relation_function_review_only_slot_return_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'semi_constructed_relation_function_package148_coordination_note' },
    { filename: `${noteId}.md`, class: 'semi_constructed_relation_function_package148_coordination_note' },
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
  upload.obj.package148_upload_queue_update = {
    captured_utc: '2026-07-03T07:17:00Z',
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
  const step = 'Stage package 148 semi-constructed relation/function review-only slot-return ledger template artifacts with this queue as substantive construction-method material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  const rows = artifact.review_only_slot_return_rows;
  if (rows.length !== artifact.validation_snapshot.expected_slot_return_rows) failures.push(`slot_return_rows_mismatch_${rows.length}`);
  if (g.parent_review_only_seed_rows_opened !== artifact.validation_snapshot.expected_parent_seed_rows_opened) failures.push(`parent_seed_rows_mismatch_${g.parent_review_only_seed_rows_opened}`);
  if (g.blank_return_fields_per_row !== artifact.validation_snapshot.expected_blank_return_fields_per_row) failures.push(`blank_return_fields_mismatch_${g.blank_return_fields_per_row}`);
  if (g.blank_return_field_cells_allocated !== artifact.validation_snapshot.expected_blank_return_field_cells_allocated) failures.push(`blank_return_cells_mismatch_${g.blank_return_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of rows) {
    const filled = blankReturnFields.some((field) => row[field] !== null);
    if (filled || row.return_fields_filled !== 0 || row.dated_return_present || row.reviewer_return_ingested || row.slot_boundary_confirmed || row.slot_approved_for_surface_sidecar || row.no_construction_decision_recorded || row.source_text_or_excerpt_allowed_after_return || row.exact_span_allowed_after_return || row.bridge_surface_proposal_allowed_after_return || row.translation_allowed_after_return) {
      failures.push(`nonblank_or_open_slot_return_row_${row.slot_return_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentSeedIndex)).obj;
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
  source_text_or_excerpt_files: upload.summary?.source_text_or_excerpt_files,
  review_only_slot_return_rows: artifact.gate_state.review_only_slot_return_rows,
  parent_review_only_seed_rows_opened: artifact.gate_state.parent_review_only_seed_rows_opened,
  parent_review_only_slots_named: artifact.gate_state.parent_review_only_slots_named,
  blank_return_fields_per_row: artifact.gate_state.blank_return_fields_per_row,
  blank_return_field_cells_allocated: artifact.gate_state.blank_return_field_cells_allocated,
  parent_source_coordinate_rows_referenced_as_metadata: artifact.gate_state.parent_source_coordinate_rows_referenced_as_metadata,
  parent_source_file_hints_referenced_as_metadata: artifact.gate_state.parent_source_file_hints_referenced_as_metadata,
  return_fields_filled: artifact.gate_state.return_fields_filled,
  dated_returns_present: artifact.gate_state.dated_returns_present,
  reviewer_returns_ingested: artifact.gate_state.reviewer_returns_ingested,
  slots_approved_for_surface_sidecar: artifact.gate_state.slots_approved_for_surface_sidecar,
  source_text_or_excerpt_files_created: artifact.gate_state.source_text_or_excerpt_files_created,
  source_text_copied: artifact.gate_state.source_text_copied,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
