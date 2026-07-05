import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_PACKET_BLANK_20260702T140000Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_PACKET_BLANK_NOTE_20260702T140100Z';
const generatedUtc = '2026-07-02T14:00:00Z';
const noteGeneratedUtc = '2026-07-02T14:01:00Z';
const packageOrder = 114;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-REVIEWER-SCOPE-PACKET-BLANK-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentArtifacts = [
  'OLP_DMOI_RELATION_FUNCTION_ATTRIBUTION_SCOPE_GAP_CHECK_20260702T134500Z',
  'OLP_DMOI_RELATION_FUNCTION_SOURCE_POINTER_PACKET_20260702T133000Z',
  'OPEN_RELATION_FUNCTION_TRANSLATION_SOURCE_CANDIDATE_SHELF_20260702T131500Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_SCOPE_REVIEWER_SHEET_BLANK_20260701T120000Z'
];

const allowedReturnFields = [
  'dated_non_personal_return_present',
  'reviewer_role_or_authority_class',
  'packet_unit_scope_decision',
  'source_system_decision_olp_dmoi_or_split',
  'selected_source_route_scope_note',
  'mixed_license_scope_note',
  'dmoi_nc_sa_handling_note_if_dmoi_used',
  'line_span_candidate_allowed_boolean_only',
  'source_text_capture_allowed_boolean_only',
  'local_register_review_required_boolean_only',
  'bridge_or_semi_constructed_surface_review_required_boolean_only',
  'translation_owner_review_required_boolean_only',
  'defer_split_or_include_recommendation',
  'remaining_blocker_note',
  'next_gate_recommendation',
  'confidence_and_scope_note'
];

const forbiddenReturnContent = [
  'personal_contact_details',
  'copied_olp_or_dmoi_source_prose',
  'copied_definitions_examples_or_exercises',
  'exact_source_excerpts',
  'translated_passages',
  'proposed_local_terms',
  'proposed_bridge_lexemes',
  'accepted_morphemes_or_grammar_rules',
  'accepted_display_surfaces',
  'publication_or_pilot_claim'
];

const promptByPacketUnit = {
  proof_reading_and_definition_use: {
    reviewer_role: 'construction_governance_reviewer',
    decision_prompt: 'Confirm whether proof-reading and definition-use support should be a preliminary source-scope packet, and whether OLP and DMOI must be separated before any excerpt candidate register.',
    required_return: 'include/defer/split decision with source-system scope; no source prose or surface forms'
  },
  sets_membership_subset_equality: {
    reviewer_role: 'domain_mathematics_reviewer',
    decision_prompt: 'Decide whether set membership, subset, and equality language may be scoped together with relation/function boundary material, or whether it needs a separate first packet.',
    required_return: 'scope decision with prerequisite route notes; no local terms accepted'
  },
  domain_codomain_range: {
    reviewer_role: 'domain_mathematics_reviewer',
    decision_prompt: 'Classify whether domain, codomain, range/image, and mapping-arrow reading belong in one reviewer packet or must be split across source-system and local-register reviews.',
    required_return: 'include/split/defer decision with source-system and local-register gates'
  },
  function_as_relation_boundary: {
    reviewer_role: 'domain_mathematics_reviewer',
    decision_prompt: 'Decide whether function-as-relation boundary language is starter material, comparator material, or advanced deferred material for the relation/function lane.',
    required_return: 'boundary decision with source-route constraints; no excerpt or wording'
  },
  injective_surjective_bijective: {
    reviewer_role: 'domain_mathematics_reviewer',
    decision_prompt: 'Decide whether injective, surjective, and bijective language is allowed in the first source-aware packet or should wait for a function-property packet.',
    required_return: 'property-family scope decision and next-gate recommendation'
  },
  relation_properties: {
    reviewer_role: 'domain_mathematics_reviewer',
    decision_prompt: 'Decide whether reflexive, symmetric, antisymmetric, and transitive relation properties should be scoped as a separate relation-property packet.',
    required_return: 'relation-property packet decision with line-span and local-register prerequisites'
  },
  equivalence_order_poset: {
    reviewer_role: 'advanced_scope_reviewer',
    decision_prompt: 'Decide whether equivalence relations, orders, and posets are advanced deferred material or eligible as a later source-aware bridge packet.',
    required_return: 'advanced/defer decision with no surface forms'
  },
  composition_inverse: {
    reviewer_role: 'domain_mathematics_reviewer',
    decision_prompt: 'Decide whether composition and inverse language belongs with core function vocabulary or should wait for an operation-specific sidecar.',
    required_return: 'operation-scope decision and next-gate recommendation'
  },
  finite_infinite_equinumerosity: {
    reviewer_role: 'advanced_scope_reviewer',
    decision_prompt: 'Decide whether finite/infinite and same-size-by-bijection language should remain outside the first relation/function undercoverage packet.',
    required_return: 'finite/infinite scope decision; no local terms or source excerpts'
  },
  high_density_source_shelf_selection: {
    reviewer_role: 'source_selection_reviewer',
    decision_prompt: 'Decide which high-density OLP/DMOI shelves may feed a later exact line-span candidate register, and whether OLP/DMOI must remain separate by license posture.',
    required_return: 'source-selection scope decision and exact-line-span preconditions only'
  }
};

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

function buildReviewerRows(gapCheck) {
  return gapCheck.attribution_scope_gap_rows.map((row, index) => {
    const prompt = promptByPacketUnit[row.packet_unit] || {
      reviewer_role: 'construction_governance_reviewer',
      decision_prompt: 'Confirm scope, source-system handling, and next gate before any source text, surface, or translation work.',
      required_return: 'scope decision only'
    };
    return {
      reviewer_scope_row_id: `ODRF-RSCOPE-${String(index + 1).padStart(2, '0')}`,
      parent_gap_check_row_id: row.gap_check_row_id,
      parent_pointer_row_id: row.parent_pointer_row_id,
      packet_unit: row.packet_unit,
      reviewer_role: prompt.reviewer_role,
      decision_prompt: prompt.decision_prompt,
      required_return: prompt.required_return,
      allowed_return_fields: allowedReturnFields,
      forbidden_return_content: forbiddenReturnContent,
      source_systems_implicated: row.source_systems_implicated,
      olp_shelf_ids: row.olp_shelf_ids,
      dmoi_catalog_row_ids: row.dmoi_catalog_row_ids,
      source_or_gate_pointer: `${row.parent_pointer_row_id}; ${row.gap_check_row_id}`,
      open_gap_fields_referenced: row.required_gap_fields,
      open_gap_field_count_referenced: row.open_required_gap_field_count,
      no_surface_gate: true,
      no_source_text_gate: true,
      no_translation_gate: true,
      status: 'blank_waiting_for_non_personal_scope_return'
    };
  });
}

function buildReturnTemplateRows(reviewerRows) {
  return reviewerRows.map((row) => ({
    reviewer_scope_return_row_id: row.reviewer_scope_row_id.replace('ODRF-RSCOPE', 'ODRF-RSCOPE-RET'),
    reviewer_scope_row_id: row.reviewer_scope_row_id,
    parent_gap_check_row_id: row.parent_gap_check_row_id,
    parent_pointer_row_id: row.parent_pointer_row_id,
    packet_unit: row.packet_unit,
    allowed_return_fields: allowedReturnFields,
    dated_non_personal_return_present: null,
    reviewer_role_or_authority_class: null,
    packet_unit_scope_decision: null,
    source_system_decision_olp_dmoi_or_split: null,
    selected_source_route_scope_note: null,
    mixed_license_scope_note: null,
    dmoi_nc_sa_handling_note_if_dmoi_used: null,
    line_span_candidate_allowed_boolean_only: null,
    source_text_capture_allowed_boolean_only: null,
    local_register_review_required_boolean_only: null,
    bridge_or_semi_constructed_surface_review_required_boolean_only: null,
    translation_owner_review_required_boolean_only: null,
    defer_split_or_include_recommendation: null,
    remaining_blocker_note: null,
    next_gate_recommendation: null,
    confidence_and_scope_note: null,
    return_fields_filled: 0,
    return_ingested: false,
    gates_opened_by_this_blank: 0,
    status: 'blank_return_template_row_only'
  }));
}

function buildArtifact(gapCheck, pointerPacket, oldScopeSheet) {
  const reviewerRows = buildReviewerRows(gapCheck);
  const returnRows = buildReturnTemplateRows(reviewerRows);
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_reviewer_scope_packet_blank_no_returns_no_excerpts_no_source_text_no_surfaces_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Create the non-personal reviewer-scope blank packet required by package 113 before any OLP/DMOI relation-function exact line-span, source-text, local-register, bridge-surface, semi-constructed-surface, or translation work.',
    parent_artifacts: parentArtifacts,
    continuity_with_prior_scope_sheet: {
      prior_scope_sheet: oldScopeSheet.artifact_id,
      prior_scope_reviewer_rows: oldScopeSheet.gate_state.reviewer_sheet_rows,
      prior_scope_source_gate_rows: oldScopeSheet.gate_state.source_gate_rows,
      reuse_decision: 'reuse blank reviewer-sheet discipline but bind rows to package-112 source pointers and package-113 attribution/scope gaps'
    },
    packet_boundary: {
      packet_is: 'blank reviewer-scope request packet and blank return template',
      packet_is_not: [
        'dispatch record',
        'reviewer return',
        'exact source-line selection',
        'source-prose cache',
        'translation draft',
        'local-language term decision',
        'semi-constructed surface acceptance',
        'publication or pilot claim'
      ],
      allowed_now: [
        'ask non-personal reviewer-scope questions',
        'name allowed and forbidden return fields',
        'carry OLP/DMOI source-system and attribution-gap pointers forward'
      ],
      blocked_now: [
        'copying OLP or DMOI source prose',
        'choosing exact line spans',
        'filling return rows',
        'accepting source-system decisions',
        'proposing local or bridge terms',
        'translating passages',
        'claiming readiness'
      ]
    },
    allowed_return_fields: allowedReturnFields,
    forbidden_return_content: forbiddenReturnContent,
    reviewer_scope_rows: reviewerRows,
    return_template_rows: returnRows,
    source_pointer_summary: {
      source_pointer_rows_referenced: pointerPacket.gate_state.source_pointer_rows,
      olp_source_routes_referenced: pointerPacket.gate_state.olp_source_routes_referenced,
      dmoi_catalog_rows_referenced: pointerPacket.gate_state.dmoi_catalog_rows_referenced,
      attribution_scope_gap_rows_referenced: gapCheck.gate_state.attribution_scope_gap_rows,
      open_gap_cells_referenced: gapCheck.gate_state.open_required_gap_cells
    },
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_RETURN_LEDGER_TEMPLATE_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_EXACT_LINE_SPAN_CANDIDATE_REGISTER_BLANK_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_<timestamp>'
    ],
    gate_state: {
      reviewer_scope_rows: reviewerRows.length,
      return_template_rows: returnRows.length,
      allowed_return_fields: allowedReturnFields.length,
      blank_return_cells: returnRows.length * allowedReturnFields.length,
      returns_ingested: 0,
      dated_non_personal_returns_present: 0,
      source_system_decisions_recorded: 0,
      scope_decisions_recorded: 0,
      route_scope_notes_recorded: 0,
      line_span_candidate_permissions_recorded: 0,
      source_text_capture_permissions_recorded: 0,
      local_register_review_requirements_recorded: 0,
      bridge_surface_review_requirements_recorded: 0,
      translation_owner_review_requirements_recorded: 0,
      exact_line_spans_selected: 0,
      source_prose_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      excerpts_selected: 0,
      selected_excerpt_attribution_notices_filled: 0,
      local_language_surfaces_filled: 0,
      bridge_surfaces_accepted: 0,
      semi_constructed_surfaces_accepted: 0,
      translated_passages: 0,
      publication_ready: false,
      translation_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      package_order_expected: packageOrder,
      reviewer_scope_rows_expected: 10,
      return_template_rows_expected: 10,
      allowed_return_fields_expected: 16,
      blank_return_cells_expected: 160,
      zero_gate_assertions: [
        'returns_ingested',
        'dated_non_personal_returns_present',
        'source_system_decisions_recorded',
        'scope_decisions_recorded',
        'route_scope_notes_recorded',
        'line_span_candidate_permissions_recorded',
        'source_text_capture_permissions_recorded',
        'local_register_review_requirements_recorded',
        'bridge_surface_review_requirements_recorded',
        'translation_owner_review_requirements_recorded',
        'exact_line_spans_selected',
        'source_prose_copied',
        'source_examples_copied',
        'source_passages_selected',
        'excerpts_selected',
        'selected_excerpt_attribution_notices_filled',
        'local_language_surfaces_filled',
        'bridge_surfaces_accepted',
        'semi_constructed_surfaces_accepted',
        'translated_passages'
      ]
    },
    decision: 'Package 114 starts the reviewer-scope path made clear by packages 112 and 113, but only as a blank non-personal scope packet. It asks the decisions needed before source-line, local-register, bridge-surface, semi-constructed-surface, or translation work; it records none of those decisions itself.'
  };
}

function buildArtifactMd(artifact) {
  const rows = artifact.reviewer_scope_rows.map((row) => `| \`${row.reviewer_scope_row_id}\` | \`${row.parent_gap_check_row_id}\` | ${row.packet_unit} | ${row.reviewer_role} | ${row.required_return} |`).join('\n');
  const gateRows = Object.entries(artifact.gate_state).map(([key, value]) => `| ${key} | \`${Array.isArray(value) ? value.length : value}\` |`).join('\n');
  return `# OLP/DMOI Relation-Function Reviewer Scope Packet Blank

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Boundary

This is a blank reviewer-scope packet and blank return template. It is not a dispatch, return, exact line-span register, source-prose cache, selected-excerpt attribution notice, translation draft, local-language term decision, semi-constructed surface, publication claim, or pilot claim.

## Reviewer Scope Rows

| Row | Parent gap | Packet unit | Reviewer role | Required return |
| --- | --- | --- | --- | --- |
${rows}

## Gate State

| Gate | State |
| --- | ---: |
${gateRows}

Decision: ${artifact.decision}
`;
}

function buildArtifactCsv(artifact) {
  const columns = [
    'reviewer_scope_row_id',
    'parent_gap_check_row_id',
    'parent_pointer_row_id',
    'packet_unit',
    'reviewer_role',
    'decision_prompt',
    'required_return',
    'source_systems_implicated',
    'olp_shelf_ids',
    'dmoi_catalog_row_ids',
    'open_gap_field_count_referenced',
    'no_surface_gate',
    'no_source_text_gate',
    'no_translation_gate',
    'status'
  ];
  const rows = artifact.reviewer_scope_rows.map((row) => columns.map((column) => csvCell(row[column])).join(','));
  return `${columns.join(',')}\n${rows.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    source_artifact: artifact.artifact_id,
    package_order: packageOrder,
    status: 'pointer_only_reviewer_scope_packet_blank_coordination_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-114 OLP/DMOI reviewer-scope blank continuation while preserving no-return/no-excerpt/no-translation boundaries.',
    counts: {
      reviewer_scope_rows: g.reviewer_scope_rows,
      return_template_rows: g.return_template_rows,
      allowed_return_fields: g.allowed_return_fields,
      blank_return_cells: g.blank_return_cells,
      source_pointer_rows_referenced: artifact.source_pointer_summary.source_pointer_rows_referenced,
      open_gap_cells_referenced: artifact.source_pointer_summary.open_gap_cells_referenced
    },
    zero_gates: {
      returns_ingested: 0,
      dated_non_personal_returns_present: 0,
      source_system_decisions_recorded: 0,
      scope_decisions_recorded: 0,
      exact_line_spans_selected: 0,
      source_prose_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      excerpts_selected: 0,
      selected_excerpt_attribution_notices_filled: 0,
      surfaces_filled: 0,
      translated_passages: 0,
      readiness_claims: 0
    },
    no_remote_action_by_this_note: true
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 114 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 114 creates an OLP/DMOI relation-function reviewer-scope blank packet with \`${g.reviewer_scope_rows}\` reviewer rows, \`${g.return_template_rows}\` blank return-template rows, \`${g.allowed_return_fields}\` allowed return fields, and \`${g.blank_return_cells}\` blank return cells.

Zero gates: \`0\` returns, \`0\` source-system decisions, \`0\` scope decisions, \`0\` exact line spans, \`0\` source prose, \`0\` examples, \`0\` excerpts, \`0\` selected-excerpt attribution notices, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Boundary: reviewer-scope blank only. This note makes no commit, push, PR, Zenodo, dispatch, return, source-text, translation, publication, pilot, legal-advice, or remote-state claim.
`;
}

async function writeArtifactAndNote(artifact, note) {
  await writeJson(artifactId, artifact);
  await writeFile(path.join(outputs, `${artifactId}.md`), buildArtifactMd(artifact), 'utf8');
  await writeFile(path.join(outputs, `${artifactId}.csv`), buildArtifactCsv(artifact), 'utf8');
  await writeJson(noteId, note);
  await writeFile(path.join(outputs, `${noteId}.md`), buildNoteMd(note, artifact), 'utf8');
}

async function updateRegistrations(artifact) {
  const packageIndex = await readJson(packageIndexFile);
  const order = ensureArray(packageIndex.obj, 'current_package_order');
  if (!order.some((row) => row?.artifact === artifactId)) {
    order.push({
      order: packageOrder,
      role: 'olp_dmoi_relation_function_reviewer_scope_packet_blank_support',
      artifact: artifactId,
      current_use: '10 reviewer-scope blank rows and 10 blank return-template rows; 16 allowed return fields, 160 blank return cells; 0 returns, 0 source-system decisions, 0 scope decisions, 0 line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  packageIndex.obj.current_olp_dmoi_relation_function_reviewer_scope_packet_blank = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    olp_dmoi_relation_function_reviewer_scope_rows: artifact.gate_state.reviewer_scope_rows,
    olp_dmoi_relation_function_reviewer_scope_return_template_rows: artifact.gate_state.return_template_rows,
    olp_dmoi_relation_function_reviewer_scope_blank_return_cells: artifact.gate_state.blank_return_cells,
    olp_dmoi_relation_function_reviewer_scope_returns_ingested: 0,
    olp_dmoi_relation_function_reviewer_scope_source_system_decisions: 0,
    olp_dmoi_relation_function_reviewer_scope_source_prose_copied: 0,
    olp_dmoi_relation_function_reviewer_scope_excerpts_selected: 0,
    olp_dmoi_relation_function_reviewer_scope_surfaces_filled: 0,
    olp_dmoi_relation_function_reviewer_scope_translations_filled: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_return_ledger_template_or_exact_line_span_candidate_register_blank_only_no_source_text_no_surfaces_no_translation`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function reviewer-scope packet blank',
    route: artifactId,
    license_status_to_recheck: 'reviewer_scope_blank_only_no_dispatch_no_returns_exact_line_span_selection_still_blocked_until_scope_returns_and_attribution_gaps_are_closed',
    best_translation_use: 'future proof/set/function primer packet gating; asks source-system, license-scope, line-span, local-register, bridge-surface, and translation-owner questions without recording answers',
    candidate_lanes: ['semi_constructed_relation_function_source_request_lane', 'open_source_candidate_catalog', 'reviewer_scope_blank', 'review_only_construction_scaffold'],
    priority: 1,
    status: 'reviewer_scope_packet_blank_no_returns_no_excerpts_no_source_text_no_surfaces_no_translation_no_pilot',
    gate_state: {
      reviewer_scope_rows: artifact.gate_state.reviewer_scope_rows,
      return_template_rows: artifact.gate_state.return_template_rows,
      blank_return_cells: artifact.gate_state.blank_return_cells,
      returns_ingested: 0,
      source_system_decisions_recorded: 0,
      source_prose_copied: 0,
      excerpts_selected: 0,
      translated_passages: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_packet_blank: ${artifactId}_10_rows_160_blank_return_cells_0_returns_0_source_decisions_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_reviewer_scope_packet_blank_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_packet_blank_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_reviewer_scope_rows: artifact.gate_state.reviewer_scope_rows,
    current_olp_dmoi_relation_function_reviewer_scope_blank_return_cells: artifact.gate_state.blank_return_cells,
    current_olp_dmoi_relation_function_reviewer_scope_returns: 0,
    current_olp_dmoi_relation_function_reviewer_scope_source_prose_copied: 0,
    current_olp_dmoi_relation_function_reviewer_scope_excerpts_selected: 0,
    current_olp_dmoi_relation_function_reviewer_scope_translations: 0,
    current_olp_dmoi_relation_function_reviewer_scope_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_reviewer_scope_packet_blank = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_packet_blank: ${artifactId}_blank_only_no_returns_no_excerpts_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_reviewer_scope_packet_blank = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 10 reviewer-scope blank rows and 10 blank return-template rows over package-113 gaps, 16 allowed return fields, 160 blank return cells, 0 returns, 0 source-system decisions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be queued for upload when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function reviewer-scope blank packet; 10 reviewer rows, 10 blank return-template rows, 160 blank return cells, 0 returns, 0 source-system decisions, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 114: OLP/DMOI relation-function reviewer-scope blank packet after package 113. It records 10 reviewer-scope rows and 10 blank return-template rows with 160 blank return cells while keeping 0 returns, 0 source-system decisions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function reviewer-scope packet blank | ${artifactId} | Blank reviewer-scope packet; 10 rows, 10 blank return rows, 160 blank return cells, 0 returns, 0 source decisions, 0 source prose, 0 excerpts, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_packet_blank_artifact: \`${artifactId}\` (10 reviewer-scope rows; 160 blank return cells; 0 returns; 0 source prose; 0 excerpts; no surfaces, no translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_packet_blank: \`${artifactId}\`; reviewer-scope blank only, no returns, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI reviewer-scope blank packet; blank prompts are not dispatches, returns, exact excerpt authorization, source text, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_reviewer_scope_packet_blank' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_reviewer_scope_packet_blank' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_reviewer_scope_packet_blank' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package114_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package114_coordination_note' },
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
  upload.obj.user_upload_clarification = '2026-07-02: user clarified that substantive artifacts should always be queued/uploaded when a staging path exists; do not suppress them because of mobile-plan or bandwidth wording.';
  upload.obj.package114_upload_queue_update = {
    captured_utc: '2026-07-02T14:02:00Z',
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
  upload.obj.summary.network_actions_required_to_stage = 0;
  upload.obj.summary.network_actions_required_to_push = 1;
  upload.obj.staging_order = Array.isArray(upload.obj.staging_order) ? upload.obj.staging_order : [];
  const step = 'Stage package 114 OLP/DMOI relation-function reviewer-scope blank artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.reviewer_scope_rows.length !== 10) failures.push('reviewer_scope_rows_not_10');
  if (artifact.return_template_rows.length !== 10) failures.push('return_template_rows_not_10');
  if (g.allowed_return_fields !== 16) failures.push(`allowed_return_fields_not_16_${g.allowed_return_fields}`);
  if (g.blank_return_cells !== 160) failures.push(`blank_return_cells_not_160_${g.blank_return_cells}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  return failures;
}

const gapCheck = (await readJson('OLP_DMOI_RELATION_FUNCTION_ATTRIBUTION_SCOPE_GAP_CHECK_20260702T134500Z')).obj;
const pointerPacket = (await readJson('OLP_DMOI_RELATION_FUNCTION_SOURCE_POINTER_PACKET_20260702T133000Z')).obj;
const oldScopeSheet = (await readJson('SEMI_CONSTRUCTED_RELATION_FUNCTION_SCOPE_REVIEWER_SHEET_BLANK_20260701T120000Z')).obj;

const artifact = buildArtifact(gapCheck, pointerPacket, oldScopeSheet);
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
  reviewer_scope_rows: artifact.gate_state.reviewer_scope_rows,
  return_template_rows: artifact.gate_state.return_template_rows,
  allowed_return_fields: artifact.gate_state.allowed_return_fields,
  blank_return_cells: artifact.gate_state.blank_return_cells,
  returns_ingested: artifact.gate_state.returns_ingested,
  source_system_decisions_recorded: artifact.gate_state.source_system_decisions_recorded,
  exact_line_spans_selected: artifact.gate_state.exact_line_spans_selected,
  source_prose_copied: artifact.gate_state.source_prose_copied,
  excerpts_selected: artifact.gate_state.excerpts_selected,
  local_language_surfaces_filled: artifact.gate_state.local_language_surfaces_filled,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
