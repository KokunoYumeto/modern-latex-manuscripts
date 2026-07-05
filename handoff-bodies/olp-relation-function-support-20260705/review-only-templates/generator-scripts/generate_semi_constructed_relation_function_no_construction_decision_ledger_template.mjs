import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_NO_CONSTRUCTION_DECISION_LEDGER_TEMPLATE_20260703T074500Z';
const noteId = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_NO_CONSTRUCTION_DECISION_LEDGER_TEMPLATE_NOTE_20260703T074600Z';
const generatedUtc = '2026-07-03T07:45:00Z';
const noteGeneratedUtc = '2026-07-03T07:46:00Z';
const packageOrder = 150;
const queueCandidateId = 'OTCQ-SEMI-CONSTRUCTED-RELATION-FUNCTION-NO-CONSTRUCTION-DECISION-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentSurfaceSidecar = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SURFACE_SIDECAR_TEMPLATE_BLANK_20260703T073000Z';
const parentArtifacts = [
  parentSurfaceSidecar,
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SLOT_RETURN_LEDGER_TEMPLATE_20260703T071500Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_CONSTRUCTION_SEED_START_INDEX_20260703T070000Z',
  'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z'
];

const blankDecisionFields = [
  'decision_date',
  'reviewer_route_label',
  'decision_scope',
  'no_construction_reason_class',
  'local_authority_conflict_note',
  'source_evidence_gap_note',
  'bridge_harm_or_erasure_risk_note',
  'fallback_action',
  'held_until_artifact',
  'decision_note',
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

function buildDecisionRows(parent) {
  return parent.review_only_surface_sidecar_rows.map((row, index) => ({
    no_construction_decision_row_id: `DMOI-RF-ROCSI-NOCON-${String(index + 1).padStart(3, '0')}`,
    parent_surface_sidecar_row_id: row.surface_sidecar_row_id,
    parent_slot_return_row_id: row.parent_slot_return_row_id,
    parent_seed_row_id: row.parent_seed_row_id,
    parent_catalog_row_id: row.parent_catalog_row_id,
    parent_route_row_id: row.parent_route_row_id,
    candidate_area: row.candidate_area,
    selected_packet_shape: row.selected_packet_shape,
    slot_name: row.slot_name,
    inherited_surface_fields_filled: row.surface_fields_filled,
    inherited_surface_sidecar_approved: row.surface_sidecar_approved,
    inherited_bridge_surface_accepted: row.bridge_surface_accepted,
    inherited_local_language_term_accepted: row.local_language_term_accepted,
    blank_decision_fields: blankDecisionFields,
    decision_date: null,
    reviewer_route_label: null,
    decision_scope: null,
    no_construction_reason_class: null,
    local_authority_conflict_note: null,
    source_evidence_gap_note: null,
    bridge_harm_or_erasure_risk_note: null,
    fallback_action: null,
    held_until_artifact: null,
    decision_note: null,
    next_gate_recommendation: null,
    decision_fields_filled: 0,
    no_construction_decision_recorded: false,
    local_authority_conflict_flagged: false,
    source_evidence_gap_flagged: false,
    bridge_harm_or_erasure_risk_flagged: false,
    fallback_action_selected: false,
    slot_closed_for_construction: false,
    surface_sidecar_blocked_by_decision: false,
    source_text_or_excerpt_allowed_after_decision: false,
    translation_allowed_after_decision: false,
    still_locked_reason: 'missing_dated_no_construction_decision_and_reviewer_route_evidence'
  }));
}

function buildSeedSummaryRows(parent, decisionRows) {
  const seedIds = [...new Set(decisionRows.map((row) => row.parent_seed_row_id))];
  return seedIds.map((seedId, index) => {
    const linked = decisionRows.filter((row) => row.parent_seed_row_id === seedId);
    const parentSummary = (parent.seed_surface_sidecar_summary_rows || []).find((row) => row.parent_seed_row_id === seedId) || {};
    return {
      no_construction_seed_summary_row_id: `DMOI-RF-ROCSI-NOCON-SEED-${String(index + 1).padStart(2, '0')}`,
      parent_seed_row_id: seedId,
      candidate_area: linked[0]?.candidate_area,
      selected_packet_shape: linked[0]?.selected_packet_shape,
      parent_surface_sidecar_rows_allocated: parentSummary.surface_sidecar_rows_allocated || linked.length,
      no_construction_rows_allocated: linked.length,
      no_construction_decisions_recorded: 0,
      local_authority_conflicts_flagged: 0,
      source_evidence_gaps_flagged: 0,
      bridge_harm_or_erasure_risks_flagged: 0,
      fallback_actions_selected: 0,
      linked_no_construction_decision_row_ids: linked.map((row) => row.no_construction_decision_row_id)
    };
  });
}

function buildReasonClassRows() {
  const reasonClasses = [
    'local_authority_conflict',
    'source_evidence_gap',
    'bridge_harm_or_erasure_risk',
    'script_or_accessibility_mismatch',
    'prefer_local_standard_only',
    'hold_for_later_review'
  ];
  return reasonClasses.map((reasonClass, index) => ({
    no_construction_reason_class_row_id: `DMOI-RF-ROCSI-NOCON-CLASS-${String(index + 1).padStart(2, '0')}`,
    no_construction_reason_class: reasonClass,
    class_description: {
      local_authority_conflict: 'construction would override or obscure a local authority route or named language standard',
      source_evidence_gap: 'source or terminology evidence is too weak to support a construction slot',
      bridge_harm_or_erasure_risk: 'bridge form could erase local distinction, minority authority, or reader access',
      script_or_accessibility_mismatch: 'proposed path would fail script, notation, signed, or accessibility constraints',
      prefer_local_standard_only: 'local-standard terminology should be maintained without bridge construction',
      hold_for_later_review: 'slot remains open only as a question and should not proceed without more review'
    }[reasonClass],
    decisions_recorded: 0,
    linked_decision_row_ids: []
  }));
}

function buildArtifact(parent) {
  const decisionRows = buildDecisionRows(parent);
  const seedSummaryRows = buildSeedSummaryRows(parent, decisionRows);
  const reasonClassRows = buildReasonClassRows();
  const blankDecisionCells = decisionRows.length * blankDecisionFields.length;
  const parentGate = parent.gate_state || {};
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'no_construction_decision_ledger_template_blank_no_decisions_no_forms_no_source_text_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Make no-construction a first-class review outcome for P149 relation/function surface sidecar rows, without recording any actual no-construction decisions, proposing forms, copying source text, selecting excerpts, or drafting translations.',
    parent_artifacts: parentArtifacts,
    no_construction_boundary: {
      ledger_is: 'blank no-construction decision ledger template for review-only abstract slots',
      ledger_is_not: [
        'actual no-construction decision',
        'surface proposal',
        'accepted local-language term',
        'bridge form rejection based on a received return',
        'source excerpt',
        'source text copy',
        'translation draft',
        'pilot or publication claim'
      ],
      why_now: 'The review-only surface sidecar exists but has zero approvals or forms; a parallel no-construction ledger preserves refusal/hold paths before any form can be invented.',
      promotion_requires: [
        'dated reviewer return',
        'reviewer route label',
        'reason class evidence',
        'local-standard or authority note where relevant',
        'explicit fallback action'
      ]
    },
    blank_decision_fields: blankDecisionFields,
    no_construction_decision_rows: decisionRows,
    seed_no_construction_summary_rows: seedSummaryRows,
    no_construction_reason_class_rows: reasonClassRows,
    gate_state: {
      no_construction_decision_rows: decisionRows.length,
      parent_surface_sidecar_rows: parentGate.review_only_surface_sidecar_rows || decisionRows.length,
      parent_surface_sidecars_approved: parentGate.surface_sidecars_approved || 0,
      seed_no_construction_summary_rows: seedSummaryRows.length,
      no_construction_reason_class_rows: reasonClassRows.length,
      blank_decision_fields_per_row: blankDecisionFields.length,
      blank_decision_field_cells_allocated: blankDecisionCells,
      decision_fields_filled: 0,
      no_construction_decisions_recorded: 0,
      local_authority_conflicts_flagged: 0,
      source_evidence_gaps_flagged: 0,
      bridge_harm_or_erasure_risks_flagged: 0,
      fallback_actions_selected: 0,
      slots_closed_for_construction: 0,
      surface_sidecars_blocked_by_decision: 0,
      proposed_bridge_lexemes: 0,
      proposed_bridge_morphemes: 0,
      proposed_bridge_syntax_rules: 0,
      proposed_bridge_display_surfaces: 0,
      proposed_local_language_terms: 0,
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
      expected_no_construction_decision_rows: 17,
      expected_parent_surface_sidecar_rows: 17,
      expected_blank_decision_fields_per_row: blankDecisionFields.length,
      expected_blank_decision_field_cells_allocated: blankDecisionCells,
      zero_gate_assertions: [
        'parent_surface_sidecars_approved',
        'decision_fields_filled',
        'no_construction_decisions_recorded',
        'local_authority_conflicts_flagged',
        'source_evidence_gaps_flagged',
        'bridge_harm_or_erasure_risks_flagged',
        'fallback_actions_selected',
        'slots_closed_for_construction',
        'surface_sidecars_blocked_by_decision',
        'proposed_bridge_lexemes',
        'proposed_bridge_morphemes',
        'proposed_bridge_syntax_rules',
        'proposed_bridge_display_surfaces',
        'proposed_local_language_terms',
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
      'SEMI_CONSTRUCTED_RELATION_FUNCTION_NO_CONSTRUCTION_DECISION_LEDGER_WITH_DECISIONS_<timestamp>',
      'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SLOT_RETURN_LEDGER_WITH_RETURNS_<timestamp>',
      'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SURFACE_SIDECAR_WITH_RETURNS_AND_PROPOSALS_<timestamp>'
    ],
    decision: 'Package 150 allocates blank no-construction decision rows only. It records no decisions, rejects no slots, proposes no forms, and opens no source-text, excerpt, translation, pilot, or publication gates.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const rows = artifact.no_construction_decision_rows.map((row) => `| ${row.no_construction_decision_row_id} | ${row.parent_surface_sidecar_row_id} | ${row.slot_name} | ${row.candidate_area} | ${row.decision_fields_filled} |`).join('\n');
  const classes = artifact.no_construction_reason_class_rows.map((row) => `| ${row.no_construction_reason_class_row_id} | ${row.no_construction_reason_class} | ${row.decisions_recorded} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- No-construction decision rows: \`${g.no_construction_decision_rows}\`
- Parent surface sidecar rows: \`${g.parent_surface_sidecar_rows}\`
- Parent surface sidecars approved: \`${g.parent_surface_sidecars_approved}\`
- Reason classes: \`${g.no_construction_reason_class_rows}\`
- Blank decision fields per row: \`${g.blank_decision_fields_per_row}\`
- Blank decision-field cells: \`${g.blank_decision_field_cells_allocated}\`

## Decision Rows

| Row | Parent surface sidecar | Slot | Candidate area | Filled fields |
| --- | --- | --- | --- | ---: |
${rows}

## Reason Classes

| Row | Reason class | Decisions recorded |
| --- | --- | ---: |
${classes}

## Zero Gates

- No-construction decisions / closed slots: \`0 / 0\`
- Local authority conflicts / source gaps / harm risks flagged: \`0 / 0 / 0\`
- Fallback actions selected: \`0\`
- Proposed bridge forms / accepted surfaces: \`0 / 0\`
- Source text/excerpt files: \`0\`
- Source text/definitions/examples copied: \`0 / 0 / 0\`
- Exact spans / candidate line ranges: \`0 / 0\`
- Translated passages: \`0\`
- Readiness: \`publication=false, translation=false, constructed_surface=false, pilot=false\`

Boundary: this is a blank no-construction decision ledger template only. It is not a decision, not a rejection, not a surface proposal, not a source excerpt, not a translation, and not a readiness claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'parent_surface_sidecar_row_id', 'slot_name', 'candidate_area', 'blank_fields', 'filled_fields', 'decision_recorded'].map(csvCell).join(','));
  for (const row of artifact.no_construction_decision_rows) {
    rows.push([
      'no_construction_decision_row',
      row.no_construction_decision_row_id,
      row.parent_surface_sidecar_row_id,
      row.slot_name,
      row.candidate_area,
      row.blank_decision_fields.length,
      row.decision_fields_filled,
      row.no_construction_decision_recorded
    ].map(csvCell).join(','));
  }
  for (const row of artifact.no_construction_reason_class_rows) {
    rows.push([
      'reason_class',
      row.no_construction_reason_class_row_id,
      '',
      row.no_construction_reason_class,
      row.class_description,
      '',
      '',
      row.decisions_recorded
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
    status: 'pointer_only_package150_no_construction_decision_ledger_template_note_no_upload_coordination_no_source_text_no_translation_no_readiness',
    summary: 'Package 150 queues a blank no-construction decision ledger template for the 17 P149 surface sidecar rows.',
    counts: {
      no_construction_decision_rows: g.no_construction_decision_rows,
      blank_decision_fields_per_row: g.blank_decision_fields_per_row,
      blank_decision_field_cells_allocated: g.blank_decision_field_cells_allocated,
      no_construction_reason_class_rows: g.no_construction_reason_class_rows
    },
    zero_gates: {
      no_construction_decisions_recorded: 0,
      local_authority_conflicts_flagged: 0,
      bridge_harm_or_erasure_risks_flagged: 0,
      fallback_actions_selected: 0,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      source_text_or_excerpt_files_created: 0,
      translated_passages: 0,
      readiness_claims: 0
    },
    no_remote_action_by_this_note: true
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 150 No-Construction Decision Ledger Template Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 150 creates \`${g.no_construction_decision_rows}\` blank no-construction decision rows with \`${g.blank_decision_fields_per_row}\` blank fields per row. It records \`0\` actual no-construction decisions.

Zero gates: \`0\` decisions recorded, \`0\` local authority conflicts flagged, \`0\` bridge harm risks flagged, \`0\` fallback actions selected, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` source-text/excerpt files, \`0\` translations, \`0\` readiness claims.

Boundary: blank no-construction decision ledger template only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
      role: 'semi_constructed_relation_function_no_construction_decision_ledger_template_support',
      artifact: artifactId,
      current_use: '17 blank no-construction decision rows; 11 decision fields per row; 187 blank cells; 0 decisions, 0 forms, 0 source text, 0 translation, 0 readiness'
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_semi_constructed_relation_function_no_construction_decision_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_relation_function_no_construction_decision_rows: g.no_construction_decision_rows,
    current_relation_function_no_construction_blank_cells: g.blank_decision_field_cells_allocated,
    current_relation_function_no_construction_decisions_recorded: 0,
    current_relation_function_no_construction_source_text_or_excerpt_files: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_decision_returns_or_slot_returns_only_after_dated_review_no_source_text_no_excerpts_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Semi-constructed relation/function no-construction decision ledger template',
    route: artifactId,
    license_status_to_recheck: 'blank_no_construction_template_only_no_source_text_no_excerpts_recheck_exact_source_before_any_passage_or_adaptation',
    best_translation_use: 'first-class refusal/hold ledger for review-only construction slots before any forms or translations',
    candidate_lanes: [
      'relation_function_bridge_register',
      'review_only_construction_seed',
      'no_construction_decision_ledger',
      'local_standard_first'
    ],
    priority: 1,
    status: 'blank_no_construction_decision_ledger_no_decisions_no_forms_no_source_text_no_translation_no_pilot',
    gate_state: {
      no_construction_decision_rows: g.no_construction_decision_rows,
      blank_decision_field_cells_allocated: g.blank_decision_field_cells_allocated,
      no_construction_decisions_recorded: 0,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      source_text_or_excerpt_files_created: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_semi_constructed_relation_function_no_construction_decision_ledger_template: ${artifactId}_17_blank_decision_rows_187_blank_cells_0_decisions_0_forms_0_source_text_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_semi_constructed_relation_function_no_construction_decision_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_semi_constructed_relation_function_no_construction_decision_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_relation_function_no_construction_decision_rows: g.no_construction_decision_rows,
    current_relation_function_no_construction_blank_cells: g.blank_decision_field_cells_allocated,
    current_relation_function_no_construction_decisions_recorded: 0,
    current_relation_function_no_construction_source_text_or_excerpt_files: 0,
    current_relation_function_no_construction_surfaces: 0,
    current_relation_function_no_construction_translations: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_semi_constructed_relation_function_no_construction_decision_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_semi_constructed_relation_function_no_construction_decision_ledger_template: ${artifactId}_blank_decisions_no_forms_no_source_text_no_excerpts_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_semi_constructed_relation_function_no_construction_decision_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 17 blank no-construction decision rows and 187 blank decision-field cells for P149 relation/function surface sidecar rows; 0 decisions, 0 local authority conflicts flagged, 0 harm risks flagged, 0 fallback actions, 0 proposed forms, 0 accepted surfaces, 0 source text, 0 excerpts, 0 translations, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - Semi-constructed relation/function no-construction decision ledger template; 17 blank decision rows, 187 blank cells, 0 decisions, 0 proposed forms, 0 accepted surfaces, 0 source text, 0 excerpts, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 150: blank no-construction decision ledger template. It allocates 17 blank no-construction rows and 187 blank decision-field cells while keeping 0 decisions, 0 proposed forms, 0 accepted surfaces, 0 source text, 0 excerpts, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Semi-constructed relation/function no-construction decision ledger template | ${artifactId} | Blank no-construction decision scaffold; 17 rows, 187 blank cells, 0 decisions, 0 forms, 0 accepted surfaces, 0 source text, no excerpt, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_semi_constructed_relation_function_no_construction_decision_ledger_template_artifact: \`${artifactId}\` (17 blank decision rows; 187 blank cells; 0 decisions; 0 source text; 0 excerpts; no accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_semi_constructed_relation_function_no_construction_decision_ledger_template: \`${artifactId}\`; blank no-construction decision ledger only, no decisions, forms, source text, excerpts, accepted local terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: creates blank no-construction decision rows for the DMOI relation/function review-only slots; rows are not actual decisions, proposed forms, accepted surfaces, local-language term decisions, source excerpts, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'semi_constructed_relation_function_no_construction_decision_ledger_template' },
    { filename: `${artifactId}.md`, class: 'semi_constructed_relation_function_no_construction_decision_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'semi_constructed_relation_function_no_construction_decision_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'semi_constructed_relation_function_package150_coordination_note' },
    { filename: `${noteId}.md`, class: 'semi_constructed_relation_function_package150_coordination_note' },
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
  upload.obj.package150_upload_queue_update = {
    captured_utc: '2026-07-03T07:47:00Z',
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
  const step = 'Stage package 150 semi-constructed relation/function no-construction decision ledger template artifacts with this queue as substantive construction-method material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  const rows = artifact.no_construction_decision_rows;
  if (rows.length !== artifact.validation_snapshot.expected_no_construction_decision_rows) failures.push(`decision_rows_mismatch_${rows.length}`);
  if (g.parent_surface_sidecar_rows !== artifact.validation_snapshot.expected_parent_surface_sidecar_rows) failures.push(`parent_surface_rows_mismatch_${g.parent_surface_sidecar_rows}`);
  if (g.blank_decision_fields_per_row !== artifact.validation_snapshot.expected_blank_decision_fields_per_row) failures.push(`blank_decision_fields_mismatch_${g.blank_decision_fields_per_row}`);
  if (g.blank_decision_field_cells_allocated !== artifact.validation_snapshot.expected_blank_decision_field_cells_allocated) failures.push(`blank_decision_cells_mismatch_${g.blank_decision_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of rows) {
    const filled = blankDecisionFields.some((field) => row[field] !== null);
    if (filled || row.decision_fields_filled !== 0 || row.no_construction_decision_recorded || row.local_authority_conflict_flagged || row.source_evidence_gap_flagged || row.bridge_harm_or_erasure_risk_flagged || row.fallback_action_selected || row.slot_closed_for_construction || row.surface_sidecar_blocked_by_decision || row.source_text_or_excerpt_allowed_after_decision || row.translation_allowed_after_decision) {
      failures.push(`nonblank_or_open_no_construction_row_${row.no_construction_decision_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parent = (await readJson(parentSurfaceSidecar)).obj;
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
  no_construction_decision_rows: artifact.gate_state.no_construction_decision_rows,
  parent_surface_sidecar_rows: artifact.gate_state.parent_surface_sidecar_rows,
  parent_surface_sidecars_approved: artifact.gate_state.parent_surface_sidecars_approved,
  no_construction_reason_class_rows: artifact.gate_state.no_construction_reason_class_rows,
  blank_decision_fields_per_row: artifact.gate_state.blank_decision_fields_per_row,
  blank_decision_field_cells_allocated: artifact.gate_state.blank_decision_field_cells_allocated,
  decision_fields_filled: artifact.gate_state.decision_fields_filled,
  no_construction_decisions_recorded: artifact.gate_state.no_construction_decisions_recorded,
  local_authority_conflicts_flagged: artifact.gate_state.local_authority_conflicts_flagged,
  bridge_harm_or_erasure_risks_flagged: artifact.gate_state.bridge_harm_or_erasure_risks_flagged,
  fallback_actions_selected: artifact.gate_state.fallback_actions_selected,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  source_text_or_excerpt_files_created: artifact.gate_state.source_text_or_excerpt_files_created,
  source_text_copied: artifact.gate_state.source_text_copied,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
