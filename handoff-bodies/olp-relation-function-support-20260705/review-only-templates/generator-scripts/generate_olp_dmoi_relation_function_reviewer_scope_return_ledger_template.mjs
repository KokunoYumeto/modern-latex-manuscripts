import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_RETURN_LEDGER_TEMPLATE_20260702T141500Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_RETURN_LEDGER_TEMPLATE_NOTE_20260702T141600Z';
const generatedUtc = '2026-07-02T14:15:00Z';
const noteGeneratedUtc = '2026-07-02T14:16:00Z';
const packageOrder = 115;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-REVIEWER-SCOPE-RETURN-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentArtifacts = [
  'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_PACKET_BLANK_20260702T140000Z',
  'OLP_DMOI_RELATION_FUNCTION_ATTRIBUTION_SCOPE_GAP_CHECK_20260702T134500Z',
  'OLP_DMOI_RELATION_FUNCTION_SOURCE_POINTER_PACKET_20260702T133000Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_RETURN_LEDGER_TEMPLATE_20260701T121500Z'
];

const returnFieldColumns = [
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

const ledgerColumns = [
  'ledger_row_id',
  'reviewer_scope_row_id',
  'parent_gap_check_row_id',
  'parent_pointer_row_id',
  'packet_unit',
  'reviewer_role',
  'source_systems_implicated',
  ...returnFieldColumns,
  'return_fields_filled',
  'return_complete_for_scope_decision',
  'line_span_register_may_start_after_review',
  'source_text_capture_may_start_after_review',
  'local_or_bridge_surface_may_start_after_review',
  'translation_may_start_after_review',
  'ledger_row_status'
];

const promotionRules = [
  {
    promotion_rule_id: 'ODRF-RSCOPE-LEDGER-RULE-01',
    gate: 'scope_return_completeness',
    requirement: 'A ledger row cannot promote unless dated_non_personal_return_present, reviewer_role_or_authority_class, packet_unit_scope_decision, and confidence_and_scope_note are filled.',
    opens_gate_now: false
  },
  {
    promotion_rule_id: 'ODRF-RSCOPE-LEDGER-RULE-02',
    gate: 'source_system_decision',
    requirement: 'A source-system decision must choose OLP, DMOI, split, or defer; blank or mixed-language guesses do not count.',
    opens_gate_now: false
  },
  {
    promotion_rule_id: 'ODRF-RSCOPE-LEDGER-RULE-03',
    gate: 'license_scope_decision',
    requirement: 'Any DMOI or mixed OLP/DMOI decision must include a license-scope note and DMOI NC/SA handling note before adaptation planning.',
    opens_gate_now: false
  },
  {
    promotion_rule_id: 'ODRF-RSCOPE-LEDGER-RULE-04',
    gate: 'line_span_candidate_register',
    requirement: 'Line-span candidate work can only start after the row explicitly allows line-span candidates and still must avoid copying source prose.',
    opens_gate_now: false
  },
  {
    promotion_rule_id: 'ODRF-RSCOPE-LEDGER-RULE-05',
    gate: 'source_text_capture',
    requirement: 'Source-text capture remains separately blocked unless source_text_capture_allowed_boolean_only is true and selected-excerpt attribution prerequisites are complete.',
    opens_gate_now: false
  },
  {
    promotion_rule_id: 'ODRF-RSCOPE-LEDGER-RULE-06',
    gate: 'local_register_or_bridge_surface',
    requirement: 'Local, bridge, or semi-constructed surfaces cannot start from this ledger unless explicit local/register or bridge/surface review requirements are filled and a later artifact opens that gate.',
    opens_gate_now: false
  },
  {
    promotion_rule_id: 'ODRF-RSCOPE-LEDGER-RULE-07',
    gate: 'translation_owner_review',
    requirement: 'Translation cannot start unless translation-owner review requirement is filled and a later artifact records acceptance.',
    opens_gate_now: false
  },
  {
    promotion_rule_id: 'ODRF-RSCOPE-LEDGER-RULE-08',
    gate: 'personal_data_and_source_text_exclusion',
    requirement: 'Any row containing personal contact details, source prose, examples, excerpts, local terms, bridge forms, translations, or readiness claims is invalid for promotion.',
    opens_gate_now: false
  }
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

function buildLedgerRows(scopePacket) {
  return scopePacket.reviewer_scope_rows.map((row, index) => {
    const base = {
      ledger_row_id: `ODRF-RSCOPE-LEDGER-${String(index + 1).padStart(2, '0')}`,
      reviewer_scope_row_id: row.reviewer_scope_row_id,
      parent_gap_check_row_id: row.parent_gap_check_row_id,
      parent_pointer_row_id: row.parent_pointer_row_id,
      packet_unit: row.packet_unit,
      reviewer_role: row.reviewer_role,
      source_systems_implicated: row.source_systems_implicated
    };
    for (const field of returnFieldColumns) base[field] = null;
    return {
      ...base,
      return_fields_filled: 0,
      return_complete_for_scope_decision: false,
      line_span_register_may_start_after_review: false,
      source_text_capture_may_start_after_review: false,
      local_or_bridge_surface_may_start_after_review: false,
      translation_may_start_after_review: false,
      ledger_row_status: 'blank_return_ledger_row_only'
    };
  });
}

function buildArtifact(scopePacket, gapCheck, priorLedger) {
  const ledgerRows = buildLedgerRows(scopePacket);
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_reviewer_scope_return_ledger_template_no_returns_no_excerpts_no_source_text_no_surfaces_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Create a blank return-ledger template for future non-personal reviewer-scope returns from package 114 without counting any return, source-system decision, scope decision, line-span permission, source-text permission, local/bridge surface permission, translation permission, or readiness claim.',
    parent_artifacts: parentArtifacts,
    continuity_with_prior_relation_function_ledger: {
      prior_return_ledger: priorLedger.artifact_id,
      prior_ledger_rows: priorLedger.gate_state.ledger_rows,
      prior_ledger_columns: priorLedger.gate_state.ledger_columns,
      reuse_decision: 'reuse blank return-ledger discipline but bind ledger rows to package-114 reviewer-scope rows and package-113 attribution/scope gaps'
    },
    packet_boundary: {
      packet_is: 'blank return-ledger template for non-personal reviewer-scope returns',
      packet_is_not: [
        'reviewer return',
        'dispatch record',
        'source-system decision',
        'scope decision',
        'exact line-span register',
        'source-prose cache',
        'translation draft',
        'local-language term decision',
        'semi-constructed surface acceptance',
        'publication or pilot claim'
      ],
      allowed_now: [
        'define return columns',
        'define promotion rules',
        'preserve row links to package-114 reviewer prompts and package-113 gap rows'
      ],
      blocked_now: [
        'filling ledger fields',
        'counting returns',
        'opening line-span or source-text gates',
        'accepting local or bridge surfaces',
        'translating passages',
        'claiming readiness'
      ]
    },
    ledger_columns: ledgerColumns,
    return_field_columns: returnFieldColumns,
    ledger_rows: ledgerRows,
    promotion_rules: promotionRules,
    gate_state: {
      ledger_rows: ledgerRows.length,
      ledger_columns: ledgerColumns.length,
      parent_reviewer_scope_rows: scopePacket.gate_state.reviewer_scope_rows,
      parent_open_gap_cells: gapCheck.gate_state.open_required_gap_cells,
      return_field_columns: returnFieldColumns.length,
      blank_return_field_cells: ledgerRows.length * returnFieldColumns.length,
      promotion_rules: promotionRules.length,
      returns_ingested: 0,
      dated_non_personal_returns_present: 0,
      return_fields_filled: 0,
      source_system_decisions_recorded: 0,
      scope_decisions_recorded: 0,
      route_scope_notes_recorded: 0,
      line_span_candidate_permissions_recorded: 0,
      source_text_capture_permissions_recorded: 0,
      local_register_review_requirements_recorded: 0,
      bridge_surface_review_requirements_recorded: 0,
      translation_owner_review_requirements_recorded: 0,
      rows_promoted: 0,
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
      ledger_rows_expected: 10,
      return_field_columns_expected: 16,
      blank_return_field_cells_expected: 160,
      promotion_rules_expected: 8,
      zero_gate_assertions: [
        'returns_ingested',
        'dated_non_personal_returns_present',
        'return_fields_filled',
        'source_system_decisions_recorded',
        'scope_decisions_recorded',
        'route_scope_notes_recorded',
        'line_span_candidate_permissions_recorded',
        'source_text_capture_permissions_recorded',
        'local_register_review_requirements_recorded',
        'bridge_surface_review_requirements_recorded',
        'translation_owner_review_requirements_recorded',
        'rows_promoted',
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
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_RETURN_EVIDENCE_CRITERIA_RUBRIC_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_EXACT_LINE_SPAN_CANDIDATE_REGISTER_BLANK_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_<timestamp>'
    ],
    decision: 'Package 115 prepares the intake ledger for future package-114 reviewer-scope returns. It records no returns and opens no downstream gates; it only defines columns and promotion rules for later non-personal evidence.'
  };
}

function buildArtifactMd(artifact) {
  const rows = artifact.ledger_rows.map((row) => `| \`${row.ledger_row_id}\` | \`${row.reviewer_scope_row_id}\` | ${row.packet_unit} | ${row.reviewer_role} | \`${row.return_fields_filled}\` |`).join('\n');
  const ruleRows = artifact.promotion_rules.map((row) => `| \`${row.promotion_rule_id}\` | ${row.gate} | ${row.requirement} | \`${row.opens_gate_now}\` |`).join('\n');
  const gateRows = Object.entries(artifact.gate_state).map(([key, value]) => `| ${key} | \`${Array.isArray(value) ? value.length : value}\` |`).join('\n');
  return `# OLP/DMOI Relation-Function Reviewer Scope Return Ledger Template

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Ledger Rows

| Ledger row | Reviewer scope row | Packet unit | Reviewer role | Fields filled |
| --- | --- | --- | --- | ---: |
${rows}

## Promotion Rules

| Rule | Gate | Requirement | Opens now |
| --- | --- | --- | --- |
${ruleRows}

## Gate State

| Gate | State |
| --- | ---: |
${gateRows}

Decision: ${artifact.decision}
`;
}

function buildArtifactCsv(artifact) {
  const rows = artifact.ledger_rows.map((row) => ledgerColumns.map((column) => csvCell(row[column])).join(','));
  return `${ledgerColumns.join(',')}\n${rows.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    source_artifact: artifact.artifact_id,
    package_order: packageOrder,
    status: 'pointer_only_reviewer_scope_return_ledger_template_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-115 OLP/DMOI reviewer-scope return-ledger template continuation while preserving no-return/no-excerpt/no-translation boundaries.',
    counts: {
      ledger_rows: g.ledger_rows,
      ledger_columns: g.ledger_columns,
      return_field_columns: g.return_field_columns,
      blank_return_field_cells: g.blank_return_field_cells,
      promotion_rules: g.promotion_rules,
      parent_reviewer_scope_rows: g.parent_reviewer_scope_rows,
      parent_open_gap_cells: g.parent_open_gap_cells
    },
    zero_gates: {
      returns_ingested: 0,
      return_fields_filled: 0,
      source_system_decisions_recorded: 0,
      scope_decisions_recorded: 0,
      rows_promoted: 0,
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
  return `# Package 115 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 115 creates an OLP/DMOI relation-function reviewer-scope return-ledger template with \`${g.ledger_rows}\` ledger rows, \`${g.return_field_columns}\` return-field columns, \`${g.blank_return_field_cells}\` blank return-field cells, and \`${g.promotion_rules}\` promotion rules.

Zero gates: \`0\` returns, \`0\` filled return fields, \`0\` source-system decisions, \`0\` scope decisions, \`0\` promoted rows, \`0\` exact line spans, \`0\` source prose, \`0\` examples, \`0\` excerpts, \`0\` selected-excerpt attribution notices, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Boundary: return-ledger template only. This note makes no commit, push, PR, Zenodo, dispatch, return, source-text, translation, publication, pilot, legal-advice, or remote-state claim.
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
      role: 'olp_dmoi_relation_function_reviewer_scope_return_ledger_template_support',
      artifact: artifactId,
      current_use: '10 blank reviewer-scope return-ledger rows; 16 return-field columns, 160 blank return-field cells; 8 promotion rules; 0 returns, 0 filled fields, 0 source-system decisions, 0 scope decisions, 0 line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  packageIndex.obj.current_olp_dmoi_relation_function_reviewer_scope_return_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    olp_dmoi_relation_function_reviewer_scope_return_ledger_rows: artifact.gate_state.ledger_rows,
    olp_dmoi_relation_function_reviewer_scope_return_field_columns: artifact.gate_state.return_field_columns,
    olp_dmoi_relation_function_reviewer_scope_blank_return_field_cells: artifact.gate_state.blank_return_field_cells,
    olp_dmoi_relation_function_reviewer_scope_return_ledger_returns_ingested: 0,
    olp_dmoi_relation_function_reviewer_scope_return_ledger_source_system_decisions: 0,
    olp_dmoi_relation_function_reviewer_scope_return_ledger_source_prose_copied: 0,
    olp_dmoi_relation_function_reviewer_scope_return_ledger_excerpts_selected: 0,
    olp_dmoi_relation_function_reviewer_scope_return_ledger_surfaces_filled: 0,
    olp_dmoi_relation_function_reviewer_scope_return_ledger_translations_filled: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_return_evidence_criteria_rubric_or_exact_line_span_candidate_register_blank_only_no_source_text_no_surfaces_no_translation`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function reviewer-scope return ledger template',
    route: artifactId,
    license_status_to_recheck: 'return_ledger_template_only_no_returns_no_decisions_no_line_span_selection_no_source_text_no_surfaces_no_translation',
    best_translation_use: 'future non-personal reviewer-scope return intake for source-system, license-scope, local-register, bridge-surface, and translation-owner gates',
    candidate_lanes: ['semi_constructed_relation_function_source_request_lane', 'open_source_candidate_catalog', 'reviewer_scope_return_ledger_template', 'review_only_construction_scaffold'],
    priority: 1,
    status: 'reviewer_scope_return_ledger_template_no_returns_no_excerpts_no_source_text_no_surfaces_no_translation_no_pilot',
    gate_state: {
      ledger_rows: artifact.gate_state.ledger_rows,
      blank_return_field_cells: artifact.gate_state.blank_return_field_cells,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_return_ledger_template: ${artifactId}_10_rows_160_blank_return_field_cells_0_returns_0_source_decisions_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_reviewer_scope_return_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_return_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_reviewer_scope_return_ledger_rows: artifact.gate_state.ledger_rows,
    current_olp_dmoi_relation_function_reviewer_scope_blank_return_field_cells: artifact.gate_state.blank_return_field_cells,
    current_olp_dmoi_relation_function_reviewer_scope_return_ledger_returns: 0,
    current_olp_dmoi_relation_function_reviewer_scope_return_ledger_source_prose_copied: 0,
    current_olp_dmoi_relation_function_reviewer_scope_return_ledger_excerpts_selected: 0,
    current_olp_dmoi_relation_function_reviewer_scope_return_ledger_translations: 0,
    current_olp_dmoi_relation_function_reviewer_scope_return_ledger_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_reviewer_scope_return_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_reviewer_scope_return_ledger_template: ${artifactId}_blank_only_no_returns_no_excerpts_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_reviewer_scope_return_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 10 blank reviewer-scope return-ledger rows, 16 return fields, 160 blank return-field cells, and 8 promotion rules; 0 returns, 0 source-system decisions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be queued for upload when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function reviewer-scope return-ledger template; 10 blank ledger rows, 160 blank return-field cells, 8 promotion rules, 0 returns, 0 source-system decisions, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 115: OLP/DMOI relation-function reviewer-scope return-ledger template after package 114. It records 10 blank ledger rows, 16 return fields, 160 blank return-field cells, and 8 promotion rules while keeping 0 returns, 0 source-system decisions, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function reviewer-scope return-ledger template | ${artifactId} | Blank return-ledger template; 10 rows, 160 blank return-field cells, 8 promotion rules, 0 returns, 0 source decisions, 0 source prose, 0 excerpts, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_return_ledger_template_artifact: \`${artifactId}\` (10 blank ledger rows; 160 blank return-field cells; 0 returns; 0 source prose; 0 excerpts; no surfaces, no translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_reviewer_scope_return_ledger_template: \`${artifactId}\`; return-ledger template only, no returns, accepted surfaces, or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI reviewer-scope return-ledger template; blank ledger rows are not dispatches, returns, exact excerpt authorization, source text, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_reviewer_scope_return_ledger_template' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_reviewer_scope_return_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_reviewer_scope_return_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package115_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package115_coordination_note' },
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
  upload.obj.package115_upload_queue_update = {
    captured_utc: '2026-07-02T14:17:00Z',
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
  const step = 'Stage package 115 OLP/DMOI relation-function reviewer-scope return-ledger template artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.ledger_rows.length !== 10) failures.push('ledger_rows_not_10');
  if (g.return_field_columns !== 16) failures.push(`return_field_columns_not_16_${g.return_field_columns}`);
  if (g.blank_return_field_cells !== 160) failures.push(`blank_return_field_cells_not_160_${g.blank_return_field_cells}`);
  if (g.promotion_rules !== 8) failures.push(`promotion_rules_not_8_${g.promotion_rules}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  return failures;
}

const scopePacket = (await readJson('OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_PACKET_BLANK_20260702T140000Z')).obj;
const gapCheck = (await readJson('OLP_DMOI_RELATION_FUNCTION_ATTRIBUTION_SCOPE_GAP_CHECK_20260702T134500Z')).obj;
const priorLedger = (await readJson('SEMI_CONSTRUCTED_RELATION_FUNCTION_RETURN_LEDGER_TEMPLATE_20260701T121500Z')).obj;

const artifact = buildArtifact(scopePacket, gapCheck, priorLedger);
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
  ledger_rows: artifact.gate_state.ledger_rows,
  ledger_columns: artifact.gate_state.ledger_columns,
  return_field_columns: artifact.gate_state.return_field_columns,
  blank_return_field_cells: artifact.gate_state.blank_return_field_cells,
  promotion_rules: artifact.gate_state.promotion_rules,
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
