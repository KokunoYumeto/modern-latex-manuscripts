import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SURFACE_SIDECAR_TEMPLATE_BLANK_20260703T073000Z';
const noteId = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SURFACE_SIDECAR_TEMPLATE_BLANK_NOTE_20260703T073100Z';
const generatedUtc = '2026-07-03T07:30:00Z';
const noteGeneratedUtc = '2026-07-03T07:31:00Z';
const packageOrder = 149;
const queueCandidateId = 'OTCQ-SEMI-CONSTRUCTED-RELATION-FUNCTION-REVIEW-ONLY-SURFACE-SIDECAR-TEMPLATE-BLANK-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentSlotReturnLedger = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SLOT_RETURN_LEDGER_TEMPLATE_20260703T071500Z';
const parentArtifacts = [
  parentSlotReturnLedger,
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_CONSTRUCTION_SEED_START_INDEX_20260703T070000Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_TRANSLATION_CANDIDATE_CATALOG_20260701T180000Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_CANDIDATE_REVIEWER_ROUTE_SHEET_20260701T183000Z'
];

const blankSurfaceFields = [
  'bridge_lexeme_candidate',
  'bridge_morpheme_candidate',
  'bridge_syntax_rule_candidate',
  'bridge_display_surface_candidate',
  'local_language_term_candidate',
  'script_or_notation_sidecar_candidate',
  'accessibility_note',
  'source_scope_note',
  'attribution_notice_requirement',
  'reviewer_route_label',
  'surface_decision_note',
  'next_gate_recommendation'
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

function buildSurfaceRows(parent) {
  return parent.review_only_slot_return_rows.map((row, index) => ({
    surface_sidecar_row_id: `DMOI-RF-ROCSI-SURF-${String(index + 1).padStart(3, '0')}`,
    parent_slot_return_row_id: row.slot_return_row_id,
    parent_seed_row_id: row.parent_seed_row_id,
    parent_catalog_row_id: row.parent_catalog_row_id,
    parent_route_row_id: row.parent_route_row_id,
    candidate_area: row.candidate_area,
    selected_packet_shape: row.selected_packet_shape,
    slot_name: row.slot_name,
    reviewer_role_route_label: row.reviewer_role_route_label,
    inherited_dated_return_present: row.dated_return_present,
    inherited_slot_boundary_confirmed: row.slot_boundary_confirmed,
    inherited_slot_approved_for_surface_sidecar: row.slot_approved_for_surface_sidecar,
    inherited_source_text_or_excerpt_allowed: row.source_text_or_excerpt_allowed_after_return,
    blank_surface_fields: blankSurfaceFields,
    bridge_lexeme_candidate: null,
    bridge_morpheme_candidate: null,
    bridge_syntax_rule_candidate: null,
    bridge_display_surface_candidate: null,
    local_language_term_candidate: null,
    script_or_notation_sidecar_candidate: null,
    accessibility_note: null,
    source_scope_note: null,
    attribution_notice_requirement: null,
    reviewer_route_label: null,
    surface_decision_note: null,
    next_gate_recommendation: null,
    surface_fields_filled: 0,
    proposed_bridge_lexeme_filled: false,
    proposed_bridge_morpheme_filled: false,
    proposed_bridge_syntax_rule_filled: false,
    proposed_bridge_display_surface_filled: false,
    proposed_local_language_term_filled: false,
    script_or_notation_sidecar_filled: false,
    surface_sidecar_approved: false,
    bridge_surface_accepted: false,
    local_language_term_accepted: false,
    source_text_or_excerpt_allowed_after_sidecar: false,
    translation_allowed_after_sidecar: false,
    still_locked_reason: 'missing_dated_slot_return_slot_boundary_confirmation_surface_sidecar_approval_local_standard_review_and_source_attribution_gate'
  }));
}

function buildSeedSummaryRows(parent, surfaceRows) {
  const seedIds = [...new Set(surfaceRows.map((row) => row.parent_seed_row_id))];
  return seedIds.map((seedId, index) => {
    const linked = surfaceRows.filter((row) => row.parent_seed_row_id === seedId);
    const parentSummary = (parent.seed_slot_return_summary_rows || []).find((row) => row.parent_seed_row_id === seedId) || {};
    return {
      surface_sidecar_seed_summary_row_id: `DMOI-RF-ROCSI-SURF-SEED-${String(index + 1).padStart(2, '0')}`,
      parent_seed_row_id: seedId,
      candidate_area: linked[0]?.candidate_area,
      selected_packet_shape: linked[0]?.selected_packet_shape,
      parent_slot_return_rows_required: parentSummary.slot_return_rows_required || linked.length,
      surface_sidecar_rows_allocated: linked.length,
      surface_fields_filled: 0,
      surface_sidecars_approved: 0,
      bridge_surfaces_accepted: 0,
      local_language_terms_accepted: 0,
      translations_allowed: 0,
      linked_surface_sidecar_row_ids: linked.map((row) => row.surface_sidecar_row_id)
    };
  });
}

function buildPacketShapeSummaryRows(surfaceRows) {
  const shapes = [...new Set(surfaceRows.map((row) => row.selected_packet_shape))];
  return shapes.map((shape, index) => {
    const linked = surfaceRows.filter((row) => row.selected_packet_shape === shape);
    return {
      surface_sidecar_packet_shape_summary_row_id: `DMOI-RF-ROCSI-SURF-PACKET-${String(index + 1).padStart(2, '0')}`,
      selected_packet_shape: shape,
      surface_sidecar_rows_allocated: linked.length,
      surface_fields_filled: 0,
      surface_sidecars_approved: 0,
      bridge_surfaces_accepted: 0,
      local_language_terms_accepted: 0,
      translations_allowed: 0,
      linked_surface_sidecar_row_ids: linked.map((row) => row.surface_sidecar_row_id)
    };
  });
}

function buildArtifact(parent) {
  const surfaceRows = buildSurfaceRows(parent);
  const seedSummaryRows = buildSeedSummaryRows(parent, surfaceRows);
  const packetShapeSummaryRows = buildPacketShapeSummaryRows(surfaceRows);
  const blankSurfaceCells = surfaceRows.length * blankSurfaceFields.length;
  const parentGate = parent.gate_state || {};
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'review_only_surface_sidecar_template_blank_no_forms_no_approvals_no_source_text_no_excerpts_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Allocate blank surface sidecar rows for P148 review-only slot-return rows, without proposing bridge lexemes, morphemes, syntax rules, display surfaces, local-language terms, source passages, excerpts, translations, or readiness.',
    parent_artifacts: parentArtifacts,
    surface_sidecar_boundary: {
      sidecar_is: 'blank review-only surface sidecar template for future post-return form review',
      sidecar_is_not: [
        'surface proposal',
        'accepted constructed-language form',
        'bridge lexeme',
        'bridge morpheme',
        'grammar rule',
        'local-language term decision',
        'source excerpt',
        'source text sidecar',
        'translation draft',
        'pilot or publication claim'
      ],
      inherited_gate_note: 'P148 has zero slot approvals; this template allocates rows only and does not override that gate.',
      promotion_requires: [
        'dated slot return',
        'slot boundary confirmation',
        'local-standard review',
        'license/attribution gate note before source passage use',
        'explicit sidecar approval before any surface proposal can be filled'
      ]
    },
    blank_surface_fields: blankSurfaceFields,
    review_only_surface_sidecar_rows: surfaceRows,
    seed_surface_sidecar_summary_rows: seedSummaryRows,
    packet_shape_surface_sidecar_summary_rows: packetShapeSummaryRows,
    gate_state: {
      review_only_surface_sidecar_rows: surfaceRows.length,
      parent_slot_return_rows: parentGate.review_only_slot_return_rows || surfaceRows.length,
      parent_slots_approved_for_surface_sidecar: parentGate.slots_approved_for_surface_sidecar || 0,
      seed_surface_sidecar_summary_rows: seedSummaryRows.length,
      packet_shape_surface_sidecar_summary_rows: packetShapeSummaryRows.length,
      blank_surface_fields_per_row: blankSurfaceFields.length,
      blank_surface_field_cells_allocated: blankSurfaceCells,
      surface_fields_filled: 0,
      surface_sidecars_approved: 0,
      proposed_bridge_lexemes: 0,
      proposed_bridge_morphemes: 0,
      proposed_bridge_syntax_rules: 0,
      proposed_bridge_display_surfaces: 0,
      proposed_local_language_terms: 0,
      script_or_notation_sidecars_filled: 0,
      bridge_surfaces_accepted: 0,
      local_language_terms_accepted: 0,
      accepted_bridge_surfaces: 0,
      accepted_local_language_terms: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_definitions_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      exact_line_spans_selected: 0,
      candidate_line_ranges_selected: 0,
      translated_passages: 0,
      publication_ready: false,
      translation_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      expected_surface_sidecar_rows: 17,
      expected_parent_slot_return_rows: 17,
      expected_blank_surface_fields_per_row: blankSurfaceFields.length,
      expected_blank_surface_field_cells_allocated: blankSurfaceCells,
      zero_gate_assertions: [
        'parent_slots_approved_for_surface_sidecar',
        'surface_fields_filled',
        'surface_sidecars_approved',
        'proposed_bridge_lexemes',
        'proposed_bridge_morphemes',
        'proposed_bridge_syntax_rules',
        'proposed_bridge_display_surfaces',
        'proposed_local_language_terms',
        'script_or_notation_sidecars_filled',
        'bridge_surfaces_accepted',
        'local_language_terms_accepted',
        'accepted_bridge_surfaces',
        'accepted_local_language_terms',
        'source_text_or_excerpt_files_created',
        'source_text_copied',
        'source_definitions_copied',
        'source_examples_copied',
        'source_passages_selected',
        'exact_line_spans_selected',
        'candidate_line_ranges_selected',
        'translated_passages'
      ],
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SURFACE_SIDECAR_WITH_RETURNS_AND_PROPOSALS_<timestamp>',
      'SEMI_CONSTRUCTED_RELATION_FUNCTION_NO_CONSTRUCTION_DECISION_LEDGER_<timestamp>',
      'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SLOT_RETURN_LEDGER_WITH_RETURNS_<timestamp>'
    ],
    decision: 'Package 149 allocates a blank surface sidecar template only. It does not propose, approve, or accept forms and does not open source-text, excerpt, translation, pilot, or publication gates.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const rows = artifact.review_only_surface_sidecar_rows.map((row) => `| ${row.surface_sidecar_row_id} | ${row.parent_slot_return_row_id} | ${row.slot_name} | ${row.candidate_area} | ${row.surface_fields_filled} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Surface sidecar rows: \`${g.review_only_surface_sidecar_rows}\`
- Parent slot-return rows: \`${g.parent_slot_return_rows}\`
- Parent slots approved for surface sidecar: \`${g.parent_slots_approved_for_surface_sidecar}\`
- Blank surface fields per row: \`${g.blank_surface_fields_per_row}\`
- Blank surface-field cells: \`${g.blank_surface_field_cells_allocated}\`

## Surface Sidecar Rows

| Row | Parent slot-return row | Slot | Candidate area | Filled fields |
| --- | --- | --- | --- | ---: |
${rows}

## Zero Gates

- Surface fields filled / sidecars approved: \`0 / 0\`
- Proposed bridge lexemes/morphemes/syntax/display surfaces: \`0 / 0 / 0 / 0\`
- Proposed local-language terms / script sidecars: \`0 / 0\`
- Accepted bridge/local surfaces: \`0 / 0\`
- Source text/excerpt files: \`0\`
- Source text/definitions/examples copied: \`0 / 0 / 0\`
- Exact spans / candidate line ranges: \`0 / 0\`
- Translated passages: \`0\`
- Readiness: \`publication=false, translation=false, constructed_surface=false, pilot=false\`

Boundary: this is a blank surface sidecar template only. It is not a proposed form, accepted form, local-language term decision, source excerpt, translation, dispatch, pilot, or publication artifact.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'parent_slot_return_row_id', 'slot_name', 'candidate_area', 'blank_fields', 'filled_fields', 'surface_gate_open'].map(csvCell).join(','));
  for (const row of artifact.review_only_surface_sidecar_rows) {
    rows.push([
      'surface_sidecar_row',
      row.surface_sidecar_row_id,
      row.parent_slot_return_row_id,
      row.slot_name,
      row.candidate_area,
      row.blank_surface_fields.length,
      row.surface_fields_filled,
      row.surface_sidecar_approved || row.bridge_surface_accepted || row.local_language_term_accepted
    ].map(csvCell).join(','));
  }
  for (const row of artifact.seed_surface_sidecar_summary_rows) {
    rows.push([
      'seed_summary',
      row.surface_sidecar_seed_summary_row_id,
      row.parent_seed_row_id,
      row.selected_packet_shape,
      row.candidate_area,
      row.surface_sidecar_rows_allocated,
      row.surface_fields_filled,
      row.surface_sidecars_approved > 0
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
    status: 'pointer_only_package149_surface_sidecar_template_blank_note_no_upload_coordination_no_source_text_no_translation_no_readiness',
    summary: 'Package 149 queues a blank review-only surface sidecar template for the 17 P148 slot-return rows.',
    counts: {
      review_only_surface_sidecar_rows: g.review_only_surface_sidecar_rows,
      blank_surface_fields_per_row: g.blank_surface_fields_per_row,
      blank_surface_field_cells_allocated: g.blank_surface_field_cells_allocated,
      parent_slots_approved_for_surface_sidecar: g.parent_slots_approved_for_surface_sidecar
    },
    zero_gates: {
      surface_fields_filled: 0,
      proposed_bridge_lexemes: 0,
      proposed_bridge_morphemes: 0,
      proposed_bridge_display_surfaces: 0,
      proposed_local_language_terms: 0,
      accepted_bridge_surfaces: 0,
      accepted_local_language_terms: 0,
      source_text_or_excerpt_files_created: 0,
      translated_passages: 0,
      readiness_claims: 0
    },
    no_remote_action_by_this_note: true
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 149 Blank Surface Sidecar Template Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 149 creates \`${g.review_only_surface_sidecar_rows}\` blank surface sidecar rows with \`${g.blank_surface_fields_per_row}\` blank future-surface fields per row. It inherits \`${g.parent_slots_approved_for_surface_sidecar}\` approved slots, so this is allocation only.

Zero gates: \`0\` surface fields filled, \`0\` proposed bridge lexemes, \`0\` proposed bridge morphemes, \`0\` proposed display surfaces, \`0\` proposed local terms, \`0\` accepted bridge or local surfaces, \`0\` source-text/excerpt files, \`0\` translations, \`0\` readiness claims.

Boundary: blank surface sidecar template only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
      role: 'semi_constructed_relation_function_review_only_surface_sidecar_template_blank_support',
      artifact: artifactId,
      current_use: '17 blank surface sidecar rows; 12 future-surface fields per row; 204 blank cells; 0 proposed forms, 0 accepted surfaces, 0 source text, 0 translation, 0 readiness'
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_semi_constructed_relation_function_review_only_surface_sidecar_template_blank = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_relation_function_review_only_surface_sidecar_rows: g.review_only_surface_sidecar_rows,
    current_relation_function_review_only_surface_sidecar_blank_cells: g.blank_surface_field_cells_allocated,
    current_relation_function_review_only_surface_sidecars_approved: 0,
    current_relation_function_review_only_surface_source_text_or_excerpt_files: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_no_construction_ledger_or_surface_proposals_only_after_dated_returns_no_source_text_no_excerpts_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Semi-constructed relation/function review-only blank surface sidecar template',
    route: artifactId,
    license_status_to_recheck: 'blank_surface_template_only_no_source_text_no_excerpts_recheck_exact_source_before_any_passage_or_adaptation',
    best_translation_use: 'future review-only surface sidecar shell after dated returns; no translation or forms yet',
    candidate_lanes: [
      'relation_function_bridge_register',
      'review_only_construction_seed',
      'surface_sidecar_template',
      'set_function_packet',
      'proof_literacy_micro_packet'
    ],
    priority: 1,
    status: 'blank_surface_sidecar_template_no_forms_no_source_text_no_translation_no_pilot',
    gate_state: {
      review_only_surface_sidecar_rows: g.review_only_surface_sidecar_rows,
      blank_surface_field_cells_allocated: g.blank_surface_field_cells_allocated,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      source_text_or_excerpt_files_created: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_semi_constructed_relation_function_review_only_surface_sidecar_template_blank: ${artifactId}_17_blank_surface_rows_204_blank_cells_0_forms_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_semi_constructed_relation_function_review_only_surface_sidecar_template_blank_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_semi_constructed_relation_function_review_only_surface_sidecar_template_blank_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_relation_function_review_only_surface_sidecar_rows: g.review_only_surface_sidecar_rows,
    current_relation_function_review_only_surface_sidecar_blank_cells: g.blank_surface_field_cells_allocated,
    current_relation_function_review_only_surface_sidecars_approved: 0,
    current_relation_function_review_only_surface_source_text_or_excerpt_files: 0,
    current_relation_function_review_only_surfaces: 0,
    current_relation_function_review_only_translations: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_semi_constructed_relation_function_review_only_surface_sidecar_template_blank = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_semi_constructed_relation_function_review_only_surface_sidecar_template_blank: ${artifactId}_blank_surface_sidecar_no_forms_no_source_text_no_excerpts_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_semi_constructed_relation_function_review_only_surface_sidecar_template_blank = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 17 blank surface sidecar rows and 204 blank future-surface cells for P148 abstract relation/function slots; 0 proposed bridge lexemes, 0 morphemes, 0 grammar rules, 0 display surfaces, 0 local-language terms, 0 accepted surfaces, 0 source text, 0 excerpts, 0 translations, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - Semi-constructed relation/function review-only blank surface sidecar template; 17 blank rows, 204 blank cells, 0 proposed forms, 0 accepted surfaces, 0 source text, 0 excerpts, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 149: review-only semi-constructed relation/function blank surface sidecar template. It allocates 17 blank sidecar rows and 204 blank future-surface cells while keeping 0 proposed forms, 0 accepted surfaces, 0 source text, 0 excerpts, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Semi-constructed relation/function review-only blank surface sidecar template | ${artifactId} | Blank surface sidecar scaffold; 17 rows, 204 blank cells, 0 forms, 0 accepted surfaces, 0 source text, no excerpt, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_semi_constructed_relation_function_review_only_surface_sidecar_template_blank_artifact: \`${artifactId}\` (17 blank surface sidecar rows; 204 blank cells; 0 forms; 0 source text; 0 excerpts; no accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_semi_constructed_relation_function_review_only_surface_sidecar_template_blank: \`${artifactId}\`; blank surface sidecar template only, no forms, source text, excerpts, accepted local terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: creates blank surface sidecar rows for the DMOI relation/function review-only abstract slots; rows are not proposed forms, accepted surfaces, local-language term decisions, source excerpts, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'semi_constructed_relation_function_review_only_surface_sidecar_template_blank' },
    { filename: `${artifactId}.md`, class: 'semi_constructed_relation_function_review_only_surface_sidecar_template_blank' },
    { filename: `${artifactId}.csv`, class: 'semi_constructed_relation_function_review_only_surface_sidecar_template_blank' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'semi_constructed_relation_function_package149_coordination_note' },
    { filename: `${noteId}.md`, class: 'semi_constructed_relation_function_package149_coordination_note' },
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
  upload.obj.package149_upload_queue_update = {
    captured_utc: '2026-07-03T07:32:00Z',
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
  const step = 'Stage package 149 semi-constructed relation/function blank surface sidecar template artifacts with this queue as substantive construction-method material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  const rows = artifact.review_only_surface_sidecar_rows;
  if (rows.length !== artifact.validation_snapshot.expected_surface_sidecar_rows) failures.push(`surface_rows_mismatch_${rows.length}`);
  if (g.parent_slot_return_rows !== artifact.validation_snapshot.expected_parent_slot_return_rows) failures.push(`parent_slot_return_rows_mismatch_${g.parent_slot_return_rows}`);
  if (g.blank_surface_fields_per_row !== artifact.validation_snapshot.expected_blank_surface_fields_per_row) failures.push(`blank_surface_fields_mismatch_${g.blank_surface_fields_per_row}`);
  if (g.blank_surface_field_cells_allocated !== artifact.validation_snapshot.expected_blank_surface_field_cells_allocated) failures.push(`blank_surface_cells_mismatch_${g.blank_surface_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of rows) {
    const filled = blankSurfaceFields.some((field) => row[field] !== null);
    if (filled || row.surface_fields_filled !== 0 || row.proposed_bridge_lexeme_filled || row.proposed_bridge_morpheme_filled || row.proposed_bridge_syntax_rule_filled || row.proposed_bridge_display_surface_filled || row.proposed_local_language_term_filled || row.script_or_notation_sidecar_filled || row.surface_sidecar_approved || row.bridge_surface_accepted || row.local_language_term_accepted || row.source_text_or_excerpt_allowed_after_sidecar || row.translation_allowed_after_sidecar) {
      failures.push(`nonblank_or_open_surface_sidecar_row_${row.surface_sidecar_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentSlotReturnLedger)).obj;
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
  review_only_surface_sidecar_rows: artifact.gate_state.review_only_surface_sidecar_rows,
  parent_slot_return_rows: artifact.gate_state.parent_slot_return_rows,
  parent_slots_approved_for_surface_sidecar: artifact.gate_state.parent_slots_approved_for_surface_sidecar,
  blank_surface_fields_per_row: artifact.gate_state.blank_surface_fields_per_row,
  blank_surface_field_cells_allocated: artifact.gate_state.blank_surface_field_cells_allocated,
  surface_fields_filled: artifact.gate_state.surface_fields_filled,
  surface_sidecars_approved: artifact.gate_state.surface_sidecars_approved,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  proposed_bridge_morphemes: artifact.gate_state.proposed_bridge_morphemes,
  proposed_bridge_display_surfaces: artifact.gate_state.proposed_bridge_display_surfaces,
  proposed_local_language_terms: artifact.gate_state.proposed_local_language_terms,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  source_text_or_excerpt_files_created: artifact.gate_state.source_text_or_excerpt_files_created,
  source_text_copied: artifact.gate_state.source_text_copied,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
