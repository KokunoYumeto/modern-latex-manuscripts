import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_EVIDENCE_CRITERIA_REVIEW_RETURN_LEDGER_TEMPLATE_20260703T121500Z';
const noteId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_EVIDENCE_CRITERIA_REVIEW_RETURN_LEDGER_TEMPLATE_NOTE_20260703T121600Z';
const generatedUtc = '2026-07-03T12:15:00Z';
const noteGeneratedUtc = '2026-07-03T12:16:00Z';
const packageOrder = 168;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-OPENINTRO-NUMERACY-LOCAL-SOURCE-ROUTE-EVIDENCE-CRITERIA-REVIEW-RETURN-LEDGER-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentCriteriaFile = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_EVIDENCE_CRITERIA_TEMPLATE_20260703T120000Z';

const blankReviewReturnFields = [
  'return_date',
  'reviewer_route_or_role',
  'parent_evidence_criterion_row_id_confirmed',
  'parent_candidate_return_row_id_confirmed',
  'criterion_class_decision',
  'evidence_pointer_or_route_decision',
  'evidence_value_without_source_prose_decision',
  'criterion_pass_fail_decision',
  'downstream_gate_limit_decision',
  'next_allowed_artifact',
  'comments_without_source_prose'
];

const zeroGateKeys = [
  'review_return_fields_filled',
  'evidence_criteria_review_returns_received',
  'evidence_criteria_review_returns_ingested',
  'evidence_values_recorded',
  'evidence_source_pointers_recorded',
  'criteria_passed',
  'criteria_failed',
  'candidate_returns_received',
  'candidate_returns_ingested',
  'actual_source_routes_confirmed',
  'candidate_source_routes_recorded',
  'candidate_source_urls_recorded',
  'candidate_source_owners_recorded',
  'candidate_source_owners_contacted',
  'local_route_acceptances_recorded',
  'local_source_acceptances_recorded',
  'local_permission_acceptances_recorded',
  'local_terminology_acceptances_recorded',
  'local_modality_acceptances_recorded',
  'local_language_routes_accepted',
  'local_source_routes_accepted',
  'native_or_local_sources_accepted',
  'local_license_routes_accepted',
  'local_terminology_authority_routes_accepted',
  'modality_routes_accepted',
  'source_scans_completed',
  'local_source_alignment_reviews_completed',
  'policy_review_returns_received',
  'attribution_sharealike_decisions_recorded',
  'coordinate_scans_authorized',
  'source_text_capture_authorized',
  'excerpt_selections_authorized',
  'source_text_or_excerpt_files_created',
  'source_text_copied',
  'source_excerpts_copied',
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

function buildReviewReturnRows(parentCriteria) {
  return parentCriteria.openintro_local_source_route_evidence_criterion_rows.map((row, index) => ({
    openintro_local_source_route_evidence_criteria_review_return_row_id: `OI-LOCAL-ROUTE-CRITERIA-REVIEW-RETURN-${String(index + 1).padStart(4, '0')}`,
    parent_evidence_criterion_row_id: row.openintro_local_source_route_evidence_criterion_row_id,
    parent_candidate_return_row_id: row.parent_return_row_id,
    parent_candidate_row_id: row.parent_candidate_row_id,
    neutral_packet_slot: row.neutral_packet_slot,
    lane_group: row.lane_group,
    candidate_type: row.candidate_type,
    criterion_class: row.criterion_class,
    criterion_question: row.criterion_question,
    required_before_promotion: row.required_before_promotion,
    inherited_source_route_question: row.inherited_source_route_question,
    inherited_authority_dependency: row.inherited_authority_dependency,
    inherited_modality_dependency: row.inherited_modality_dependency,
    blank_review_return_fields: blankReviewReturnFields,
    return_date: null,
    reviewer_route_or_role: null,
    parent_evidence_criterion_row_id_confirmed: null,
    parent_candidate_return_row_id_confirmed: null,
    criterion_class_decision: null,
    evidence_pointer_or_route_decision: null,
    evidence_value_without_source_prose_decision: null,
    criterion_pass_fail_decision: null,
    downstream_gate_limit_decision: null,
    next_allowed_artifact: null,
    comments_without_source_prose: null,
    review_return_fields_filled: 0,
    evidence_criteria_review_return_received: false,
    evidence_criteria_review_return_ingested: false,
    evidence_value_recorded: false,
    evidence_source_pointer_recorded: false,
    criterion_passed: false,
    criterion_failed: false,
    source_text_or_excerpt_allowed_now: false,
    translation_allowed_now: false,
    local_surface_allowed_now: false,
    pilot_ready: false,
    still_locked_reason: 'blank_evidence_criteria_review_return_row_no_return_no_evidence_pointer_no_evidence_value_no_pass_fail_no_source_text_no_translation'
  }));
}

function summaryRows(rows, groupKey, idPrefix) {
  const map = new Map();
  for (const row of rows) {
    const key = row[groupKey];
    if (!map.has(key)) {
      map.set(key, {
        group_key: key,
        review_return_rows_allocated: 0,
        blank_review_return_field_cells_allocated: 0,
        review_returns_received: 0,
        evidence_values_recorded: 0,
        evidence_source_pointers_recorded: 0,
        criteria_passed: 0,
        criteria_failed: 0,
        source_text_or_excerpt_files_created: 0,
        translated_passages: 0,
        proposed_bridge_lexemes: 0,
        accepted_bridge_surfaces: 0,
        pilot_ready: false
      });
    }
    const item = map.get(key);
    item.review_return_rows_allocated += 1;
    item.blank_review_return_field_cells_allocated += blankReviewReturnFields.length;
  }
  return [...map.values()].sort((a, b) => String(a.group_key).localeCompare(String(b.group_key))).map((item, index) => ({
    [`${idPrefix}_summary_row_id`]: `${idPrefix.toUpperCase()}-${String(index + 1).padStart(3, '0')}`,
    ...item
  }));
}

function buildArtifact(parentCriteria) {
  const reviewRows = buildReviewReturnRows(parentCriteria);
  const classSummaryRows = summaryRows(reviewRows, 'criterion_class', 'oi_local_route_criteria_review_class');
  const typeSummaryRows = summaryRows(reviewRows, 'candidate_type', 'oi_local_route_criteria_review_type');
  const packetSummaryRows = summaryRows(reviewRows, 'neutral_packet_slot', 'oi_local_route_criteria_review_packet');
  const laneSummaryRows = summaryRows(reviewRows, 'lane_group', 'oi_local_route_criteria_review_lane');
  const parentReturnSummaryRows = summaryRows(reviewRows, 'parent_candidate_return_row_id', 'oi_local_route_criteria_review_parent_return');
  const blankReviewReturnCells = reviewRows.length * blankReviewReturnFields.length;

  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'blank_review_return_ledger_template_only_no_returns_no_evidence_no_source_text_no_translation_no_readiness',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Allocate blank evidence-criteria review return rows for the OpenIntro IMS numeracy local source-route evidence criteria scaffold, without recording any reviewer return, evidence pointer, evidence value, pass/fail decision, source text, translation, constructed form, or readiness claim.',
    parent_artifacts: {
      evidence_criteria_template: parentCriteria.artifact_id,
      package_order_parent: 167,
      package_order_current: packageOrder
    },
    boundary: {
      source_text_included: false,
      source_excerpts_included: false,
      source_tables_included: false,
      source_figures_included: false,
      source_datasets_included: false,
      translations_included: false,
      proposed_constructed_forms_included: false,
      accepted_constructed_surfaces_included: false,
      actual_source_routes_included: false,
      evidence_values_included: false,
      evidence_pointers_included: false,
      remote_actions_included: false,
      legal_advice_included: false
    },
    inherited_parent_counts: {
      parent_criteria_rows: parentCriteria.gate_state.openintro_local_source_route_evidence_criterion_rows,
      parent_criteria_classes: parentCriteria.gate_state.evidence_criteria_class_rows,
      parent_blank_criteria_cells: parentCriteria.gate_state.blank_criteria_field_cells_allocated,
      parent_evidence_values_recorded: parentCriteria.gate_state.evidence_values_recorded,
      parent_evidence_source_pointers_recorded: parentCriteria.gate_state.evidence_source_pointers_recorded,
      parent_criteria_passed: parentCriteria.gate_state.criteria_passed,
      parent_criteria_failed: parentCriteria.gate_state.criteria_failed,
      parent_pilot_ready: parentCriteria.gate_state.pilot_ready
    },
    review_return_fields: blankReviewReturnFields,
    openintro_local_source_route_evidence_criteria_review_return_rows: reviewRows,
    openintro_local_route_criteria_review_class_summary_rows: classSummaryRows,
    openintro_local_route_criteria_review_type_summary_rows: typeSummaryRows,
    openintro_local_route_criteria_review_packet_summary_rows: packetSummaryRows,
    openintro_local_route_criteria_review_lane_summary_rows: laneSummaryRows,
    openintro_local_route_criteria_review_parent_return_summary_rows: parentReturnSummaryRows,
    gate_state: {
      openintro_local_source_route_evidence_criteria_review_return_rows: reviewRows.length,
      evidence_criteria_review_class_summary_rows: classSummaryRows.length,
      evidence_criteria_review_type_summary_rows: typeSummaryRows.length,
      evidence_criteria_review_packet_summary_rows: packetSummaryRows.length,
      evidence_criteria_review_lane_summary_rows: laneSummaryRows.length,
      evidence_criteria_review_parent_return_summary_rows: parentReturnSummaryRows.length,
      blank_review_return_fields_per_row: blankReviewReturnFields.length,
      blank_review_return_field_cells_allocated: blankReviewReturnCells,
      review_return_fields_filled: 0,
      evidence_criteria_review_returns_received: 0,
      evidence_criteria_review_returns_ingested: 0,
      evidence_values_recorded: 0,
      evidence_source_pointers_recorded: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      candidate_returns_received: 0,
      candidate_returns_ingested: 0,
      actual_source_routes_confirmed: 0,
      candidate_source_routes_recorded: 0,
      candidate_source_urls_recorded: 0,
      candidate_source_owners_recorded: 0,
      candidate_source_owners_contacted: 0,
      local_route_acceptances_recorded: 0,
      local_source_acceptances_recorded: 0,
      local_permission_acceptances_recorded: 0,
      local_terminology_acceptances_recorded: 0,
      local_modality_acceptances_recorded: 0,
      local_language_routes_accepted: 0,
      local_source_routes_accepted: 0,
      native_or_local_sources_accepted: 0,
      local_license_routes_accepted: 0,
      local_terminology_authority_routes_accepted: 0,
      modality_routes_accepted: 0,
      source_scans_completed: 0,
      local_source_alignment_reviews_completed: 0,
      policy_review_returns_received: 0,
      attribution_sharealike_decisions_recorded: 0,
      coordinate_scans_authorized: 0,
      source_text_capture_authorized: 0,
      excerpt_selections_authorized: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_excerpts_copied: 0,
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
      expected_review_return_rows: parentCriteria.gate_state.openintro_local_source_route_evidence_criterion_rows,
      expected_class_summary_rows: parentCriteria.gate_state.evidence_criteria_class_rows,
      expected_type_summary_rows: parentCriteria.gate_state.local_route_criteria_type_summary_rows,
      expected_packet_summary_rows: parentCriteria.gate_state.local_route_criteria_packet_summary_rows,
      expected_lane_summary_rows: parentCriteria.gate_state.local_route_criteria_lane_summary_rows,
      expected_parent_return_summary_rows: 125,
      expected_blank_review_return_fields_per_row: blankReviewReturnFields.length,
      expected_blank_review_return_field_cells_allocated: blankReviewReturnCells,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_EVIDENCE_CRITERIA_REVIEW_RETURN_LEDGER_WITH_RETURNS_<timestamp>_only_after_dated_reviews',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_ACCEPTANCE_DECISION_LEDGER_TEMPLATE_<timestamp>_only_after_review_returns',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SELECTED_EXCERPT_SIDECAR_TEMPLATE_<timestamp>_only_after_policy_attribution_packet_local_source_route_and_evidence_returns'
    ],
    decision: 'Package 168 allocates blank evidence-criteria review return rows only. It records no review returns, no evidence pointers, no evidence values, no criteria pass/fail decisions, no actual source routes, no source-owner contacts, no local terms, no source text, no excerpts, no translations, no constructed forms, and no readiness claims.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const classRows = artifact.openintro_local_route_criteria_review_class_summary_rows.map((row) => `| ${row.oi_local_route_criteria_review_class_summary_row_id} | ${row.group_key} | ${row.review_return_rows_allocated} | ${row.review_returns_received} | ${row.evidence_values_recorded} | ${row.criteria_passed} |`).join('\n');
  const typeRows = artifact.openintro_local_route_criteria_review_type_summary_rows.map((row) => `| ${row.oi_local_route_criteria_review_type_summary_row_id} | ${row.group_key} | ${row.review_return_rows_allocated} | ${row.evidence_source_pointers_recorded} |`).join('\n');
  const packetRows = artifact.openintro_local_route_criteria_review_packet_summary_rows.map((row) => `| ${row.oi_local_route_criteria_review_packet_summary_row_id} | ${row.group_key} | ${row.review_return_rows_allocated} | ${row.evidence_values_recorded} |`).join('\n');
  const laneRows = artifact.openintro_local_route_criteria_review_lane_summary_rows.map((row) => `| ${row.oi_local_route_criteria_review_lane_summary_row_id} | ${row.group_key} | ${row.review_return_rows_allocated} | ${row.review_returns_received} |`).join('\n');
  return `# Package 168 OpenIntro Numeracy Evidence-Criteria Review Return Ledger Template

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Parent criteria template: \`${artifact.parent_artifacts.evidence_criteria_template}\`

## Purpose

This is a blank review-return ledger template for OpenIntro IMS statistics/public-numeracy local source-route evidence criteria. It allocates \`${g.openintro_local_source_route_evidence_criteria_review_return_rows}\` blank review-return rows and \`${g.blank_review_return_field_cells_allocated}\` blank return-field cells.

## Gate State

- Review-return rows: \`${g.openintro_local_source_route_evidence_criteria_review_return_rows}\`
- Review returns received/ingested: \`0 / 0\`
- Evidence pointers/values recorded: \`0 / 0\`
- Criteria passed/failed: \`0 / 0\`
- Actual source routes confirmed: \`0\`
- Source text or excerpt files: \`0\`
- Source text/excerpts/tables/figures/datasets copied: \`0\`
- Translations/proposed forms/accepted surfaces: \`0 / 0 / 0\`
- Translation/publication/constructed-surface/pilot ready: \`false / false / false / false\`

## Criteria Class Summary

| Row | Criteria class | Review-return rows | Returns received | Evidence values | Criteria passed |
| --- | --- | ---: | ---: | ---: | ---: |
${classRows}

## Candidate Type Summary

| Row | Candidate type | Review-return rows | Evidence pointers |
| --- | --- | ---: | ---: |
${typeRows}

## Packet Slot Summary

| Row | Packet slot | Review-return rows | Evidence values |
| --- | --- | ---: | ---: |
${packetRows}

## Lane Summary

| Row | Lane group | Review-return rows | Returns received |
| --- | --- | ---: | ---: |
${laneRows}

## Boundary

This artifact contains no source prose, source excerpts, source tables, figures, datasets, translations, proposed constructed-language forms, accepted surfaces, owner contacts, actual route confirmations, remote actions, legal advice, or readiness claims.
`;
}

function buildArtifactCsv(artifact) {
  const columns = [
    'openintro_local_source_route_evidence_criteria_review_return_row_id',
    'parent_evidence_criterion_row_id',
    'parent_candidate_return_row_id',
    'parent_candidate_row_id',
    'neutral_packet_slot',
    'lane_group',
    'candidate_type',
    'criterion_class',
    'criterion_question',
    'required_before_promotion',
    ...blankReviewReturnFields,
    'review_return_fields_filled',
    'evidence_criteria_review_return_received',
    'evidence_criteria_review_return_ingested',
    'evidence_value_recorded',
    'evidence_source_pointer_recorded',
    'criterion_passed',
    'criterion_failed',
    'source_text_or_excerpt_allowed_now',
    'translation_allowed_now',
    'local_surface_allowed_now',
    'pilot_ready',
    'still_locked_reason'
  ];
  const lines = [columns.join(',')];
  for (const row of artifact.openintro_local_source_route_evidence_criteria_review_return_rows) {
    lines.push(columns.map((column) => csvCell(row[column])).join(','));
  }
  return `${lines.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    note_type: 'open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template_note',
    source_artifact: artifactId,
    parent_artifact: parentCriteriaFile,
    package_order: packageOrder,
    status: 'pointer_only_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: `Package 168 adds ${g.openintro_local_source_route_evidence_criteria_review_return_rows} blank evidence-criteria review return rows and ${g.blank_review_return_field_cells_allocated} blank return-field cells.`,
    gate_state: {
      review_return_fields_filled: 0,
      evidence_criteria_review_returns_received: 0,
      evidence_criteria_review_returns_ingested: 0,
      evidence_values_recorded: 0,
      evidence_source_pointers_recorded: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      actual_source_routes_confirmed: 0,
      candidate_source_routes_recorded: 0,
      candidate_source_urls_recorded: 0,
      candidate_source_owners_contacted: 0,
      local_source_routes_accepted: 0,
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_excerpts_copied: 0,
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
  return `# Package 168 OpenIntro Numeracy Evidence-Criteria Review Return Ledger Template Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 168 records \`${g.openintro_local_source_route_evidence_criteria_review_return_rows}\` blank evidence-criteria review return rows and \`${g.blank_review_return_field_cells_allocated}\` blank review-return field cells for OpenIntro IMS statistics/public numeracy.

Zero gates: \`0\` review-return fields filled, \`0\` review returns received or ingested, \`0\` evidence values or pointers recorded, \`0\` criteria passed/failed, \`0\` actual source routes confirmed, \`0\` source routes/URLs/owners recorded, \`0\` owner contacts, \`0\` local routes accepted, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: blank review-return ledger template only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, actual route record, source-owner contact, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template',
    artifact: artifactId,
    current_use: `${g.openintro_local_source_route_evidence_criteria_review_return_rows} blank evidence-criteria review return rows; ${g.blank_review_return_field_cells_allocated} blank review-return cells; 0 review returns, 0 evidence, 0 actual routes, 0 source text, 0 translations, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_openintro_numeracy_local_source_route_evidence_criteria_review_return_rows: g.openintro_local_source_route_evidence_criteria_review_return_rows,
    current_openintro_numeracy_evidence_criteria_review_returns_received: 0,
    current_openintro_numeracy_evidence_values_recorded: 0,
    current_openintro_numeracy_actual_source_routes_confirmed: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_review_return_intake_only_after_dated_reviews_no_evidence_no_actual_routes_no_source_text_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation OpenIntro numeracy local source-route evidence criteria review return ledger template',
    route: artifactId,
    license_status_to_recheck: 'blank_review_return_ledger_template_only_recheck_dated_reviews_evidence_pointer_policy_owner_permission_terminology_modality_and_source_text_absence_before_any_excerpt_adaptation_translation_or_surface',
    best_translation_use: 'blank evidence-criteria review return scaffold before any source-route acceptance, selected excerpt, local term, translation, or constructed-surface decision',
    candidate_lanes: [
      'statistics_public_numeracy',
      'OpenIntro_IMS',
      'data_literacy',
      'public_service_numeracy',
      'evidence_criteria_review_return_template',
      'world_family_lane_alignment'
    ],
    priority: 1,
    status: 'blank_evidence_criteria_review_return_ledger_template_no_returns_no_evidence_no_actual_routes_no_source_text_no_translation_no_forms_no_pilot',
    gate_state: {
      openintro_local_source_route_evidence_criteria_review_return_rows: g.openintro_local_source_route_evidence_criteria_review_return_rows,
      blank_review_return_field_cells_allocated: g.blank_review_return_field_cells_allocated,
      evidence_criteria_review_returns_received: 0,
      evidence_values_recorded: 0,
      evidence_source_pointers_recorded: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      actual_source_routes_confirmed: 0,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template: ${artifactId}_${g.openintro_local_source_route_evidence_criteria_review_return_rows}_blank_review_return_rows_0_evidence_0_source_text_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_openintro_numeracy_local_source_route_evidence_criteria_review_return_rows: g.openintro_local_source_route_evidence_criteria_review_return_rows,
    current_openintro_numeracy_evidence_criteria_review_returns_received: 0,
    current_openintro_numeracy_evidence_values_recorded: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    current_openintro_numeracy_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template: ${artifactId}_blank_review_return_template_before_any_evidence_returns_actual_routes_terms_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: records ${g.openintro_local_source_route_evidence_criteria_review_return_rows} blank OpenIntro IMS numeracy evidence-criteria review return rows; substantive upload-bound artifact; 0 review returns, 0 evidence, 0 actual routes, 0 URLs, 0 owners, 0 contacts, 0 local terms, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OpenIntro numeracy evidence-criteria review return ledger template; ${g.openintro_local_source_route_evidence_criteria_review_return_rows} blank review-return rows, ${g.blank_review_return_field_cells_allocated} blank cells, 0 evidence, 0 returns received, 0 source text, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 168: OpenIntro numeracy evidence-criteria review return ledger template. It records ${g.openintro_local_source_route_evidence_criteria_review_return_rows} blank review-return rows while keeping 0 review returns received, 0 evidence values, 0 evidence pointers, 0 criteria passed/failed, 0 actual routes, 0 URLs, 0 owners, 0 source-owner contacts, 0 local terms, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation OpenIntro numeracy local source-route evidence criteria review return ledger template | ${artifactId} | Blank review-return ledger template; ${g.openintro_local_source_route_evidence_criteria_review_return_rows} rows, 0 evidence, 0 source text, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template_artifact: \`${artifactId}\` (${g.openintro_local_source_route_evidence_criteria_review_return_rows} blank review-return rows; 0 evidence; 0 source text; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template: \`${artifactId}\`; blank OpenIntro IMS numeracy evidence-criteria review return ledger template, no evidence, returns received, source text, excerpts, local terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OpenIntro IMS public numeracy evidence-criteria review return ledger template; substantive and upload-bound, but not evidence review intake, actual source discovery, source text, translation, constructed form, local authority review, source-owner contact, local term decision, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template' },
    { filename: `${artifactId}.md`, class: 'open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template' },
    { filename: `${artifactId}.csv`, class: 'open_translation_openintro_numeracy_local_source_route_evidence_criteria_review_return_ledger_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package168_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package168_coordination_note' },
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
  upload.obj.package168_upload_queue_update = {
    captured_utc: '2026-07-03T12:17:00Z',
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
  const step = 'Stage package 168 OpenIntro numeracy evidence-criteria review return ledger template artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.openintro_local_source_route_evidence_criteria_review_return_rows !== artifact.validation_snapshot.expected_review_return_rows) failures.push(`review_rows_mismatch_${g.openintro_local_source_route_evidence_criteria_review_return_rows}`);
  if (g.evidence_criteria_review_class_summary_rows !== artifact.validation_snapshot.expected_class_summary_rows) failures.push(`class_summary_rows_mismatch_${g.evidence_criteria_review_class_summary_rows}`);
  if (g.evidence_criteria_review_type_summary_rows !== artifact.validation_snapshot.expected_type_summary_rows) failures.push(`type_summary_rows_mismatch_${g.evidence_criteria_review_type_summary_rows}`);
  if (g.evidence_criteria_review_packet_summary_rows !== artifact.validation_snapshot.expected_packet_summary_rows) failures.push(`packet_summary_rows_mismatch_${g.evidence_criteria_review_packet_summary_rows}`);
  if (g.evidence_criteria_review_lane_summary_rows !== artifact.validation_snapshot.expected_lane_summary_rows) failures.push(`lane_summary_rows_mismatch_${g.evidence_criteria_review_lane_summary_rows}`);
  if (g.evidence_criteria_review_parent_return_summary_rows !== artifact.validation_snapshot.expected_parent_return_summary_rows) failures.push(`parent_return_summary_rows_mismatch_${g.evidence_criteria_review_parent_return_summary_rows}`);
  if (g.blank_review_return_fields_per_row !== artifact.validation_snapshot.expected_blank_review_return_fields_per_row) failures.push(`blank_fields_mismatch_${g.blank_review_return_fields_per_row}`);
  if (g.blank_review_return_field_cells_allocated !== artifact.validation_snapshot.expected_blank_review_return_field_cells_allocated) failures.push(`blank_cells_mismatch_${g.blank_review_return_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.openintro_local_source_route_evidence_criteria_review_return_rows) {
    const filled = blankReviewReturnFields.some((field) => row[field] !== null);
    if (
      filled ||
      row.review_return_fields_filled !== 0 ||
      row.evidence_criteria_review_return_received ||
      row.evidence_criteria_review_return_ingested ||
      row.evidence_value_recorded ||
      row.evidence_source_pointer_recorded ||
      row.criterion_passed ||
      row.criterion_failed ||
      row.source_text_or_excerpt_allowed_now ||
      row.translation_allowed_now ||
      row.local_surface_allowed_now ||
      row.pilot_ready
    ) {
      failures.push(`nonblank_or_open_review_return_row_${row.openintro_local_source_route_evidence_criteria_review_return_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parentCriteria = (await readJson(parentCriteriaFile)).obj;
const artifact = buildArtifact(parentCriteria);
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
  openintro_local_source_route_evidence_criteria_review_return_rows: artifact.gate_state.openintro_local_source_route_evidence_criteria_review_return_rows,
  evidence_criteria_review_class_summary_rows: artifact.gate_state.evidence_criteria_review_class_summary_rows,
  evidence_criteria_review_parent_return_summary_rows: artifact.gate_state.evidence_criteria_review_parent_return_summary_rows,
  blank_review_return_field_cells_allocated: artifact.gate_state.blank_review_return_field_cells_allocated,
  review_return_fields_filled: artifact.gate_state.review_return_fields_filled,
  evidence_criteria_review_returns_received: artifact.gate_state.evidence_criteria_review_returns_received,
  evidence_values_recorded: artifact.gate_state.evidence_values_recorded,
  evidence_source_pointers_recorded: artifact.gate_state.evidence_source_pointers_recorded,
  criteria_passed: artifact.gate_state.criteria_passed,
  criteria_failed: artifact.gate_state.criteria_failed,
  actual_source_routes_confirmed: artifact.gate_state.actual_source_routes_confirmed,
  candidate_source_routes_recorded: artifact.gate_state.candidate_source_routes_recorded,
  candidate_source_owners_contacted: artifact.gate_state.candidate_source_owners_contacted,
  source_text_copied: artifact.gate_state.source_text_copied,
  translated_passages: artifact.gate_state.translated_passages,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
