import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_EVIDENCE_CRITERIA_TEMPLATE_20260703T120000Z';
const noteId = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_EVIDENCE_CRITERIA_TEMPLATE_NOTE_20260703T120100Z';
const generatedUtc = '2026-07-03T12:00:00Z';
const noteGeneratedUtc = '2026-07-03T12:01:00Z';
const packageOrder = 167;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-OPENINTRO-NUMERACY-LOCAL-SOURCE-ROUTE-EVIDENCE-CRITERIA-TEMPLATE-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';
const parentReturnFile = 'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_CANDIDATE_RETURN_LEDGER_TEMPLATE_20260703T114500Z';

const evidenceCriteria = [
  {
    criterion_class: 'dated_return_identity',
    criterion_question: 'does_a_future_return_have_a_date_reviewer_route_and_nonpersonal_role_label',
    required_before_promotion: 'dated_nonpersonal_return_identity'
  },
  {
    criterion_class: 'parent_candidate_and_alignment_match',
    criterion_question: 'does_a_future_return_match_the_parent_candidate_row_packet_lane_and_candidate_type',
    required_before_promotion: 'parent_candidate_and_alignment_match'
  },
  {
    criterion_class: 'actual_route_evidence_presence',
    criterion_question: 'does_a_future_return_supply_an_actual_route_or_owner_evidence_pointer_without_source_prose',
    required_before_promotion: 'actual_route_or_owner_pointer'
  },
  {
    criterion_class: 'owner_permission_terminology_modality_evidence',
    criterion_question: 'does_a_future_return_identify_owner_permission_terminology_or_modality_review_routes_where_needed',
    required_before_promotion: 'owner_permission_terminology_modality_review_routes'
  },
  {
    criterion_class: 'source_text_absence_confirmation',
    criterion_question: 'does_a_future_return_preserve_zero_source_text_zero_excerpts_zero_tables_figures_datasets',
    required_before_promotion: 'source_text_absence_confirmed'
  },
  {
    criterion_class: 'downstream_gate_limit_confirmation',
    criterion_question: 'does_a_future_return_keep_translation_surface_and_readiness_gates_closed_until_later_artifacts',
    required_before_promotion: 'downstream_gate_limit_confirmed'
  }
];

const criteriaFields = [
  'criterion_review_date',
  'reviewer_route_or_role',
  'parent_return_row_confirmed',
  'criterion_class_confirmed',
  'evidence_pointer_or_route',
  'evidence_value_without_source_prose',
  'criterion_pass_fail_decision',
  'blocker_or_next_action',
  'comments_without_source_prose'
];

const zeroGateKeys = [
  'criteria_fields_filled',
  'evidence_criteria_reviews_completed',
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

function buildCriteriaRows(parentReturn) {
  const rows = [];
  for (const parentRow of parentReturn.openintro_local_source_route_candidate_return_rows) {
    for (const criterion of evidenceCriteria) {
      rows.push({
        openintro_local_source_route_evidence_criterion_row_id: `OI-LOCAL-ROUTE-CRITERION-${String(rows.length + 1).padStart(4, '0')}`,
        parent_return_row_id: parentRow.openintro_local_source_route_candidate_return_row_id,
        parent_candidate_row_id: parentRow.parent_candidate_row_id,
        neutral_packet_slot: parentRow.neutral_packet_slot,
        lane_group: parentRow.lane_group,
        candidate_type: parentRow.candidate_type,
        criterion_class: criterion.criterion_class,
        criterion_question: criterion.criterion_question,
        required_before_promotion: criterion.required_before_promotion,
        inherited_source_route_question: parentRow.inherited_source_route_question,
        inherited_authority_dependency: parentRow.inherited_authority_dependency,
        inherited_modality_dependency: parentRow.inherited_modality_dependency,
        blank_criteria_fields: criteriaFields,
        criterion_review_date: null,
        reviewer_route_or_role: null,
        parent_return_row_confirmed: null,
        criterion_class_confirmed: null,
        evidence_pointer_or_route: null,
        evidence_value_without_source_prose: null,
        criterion_pass_fail_decision: null,
        blocker_or_next_action: null,
        comments_without_source_prose: null,
        criteria_fields_filled: 0,
        evidence_criterion_review_completed: false,
        evidence_value_recorded: false,
        evidence_source_pointer_recorded: false,
        criterion_passed: false,
        criterion_failed: false,
        source_text_or_excerpt_allowed_now: false,
        translation_allowed_now: false,
        local_surface_allowed_now: false,
        pilot_ready: false,
        still_locked_reason: 'blank_evidence_criterion_no_return_no_evidence_no_pass_fail_no_source_text_no_translation'
      });
    }
  }
  return rows;
}

function summaryRows(rows, groupKey, idPrefix) {
  const map = new Map();
  for (const row of rows) {
    const key = row[groupKey];
    if (!map.has(key)) {
      map.set(key, {
        [`${idPrefix}_summary_row_id`]: `${idPrefix.toUpperCase().replaceAll('_', '-')}-${String(map.size + 1).padStart(2, '0')}`,
        group_key: key,
        criteria_rows_allocated: 0,
        evidence_criteria_reviews_completed: 0,
        evidence_values_recorded: 0,
        evidence_source_pointers_recorded: 0,
        criteria_passed: 0,
        criteria_failed: 0,
        translated_passages: 0,
        accepted_bridge_surfaces: 0
      });
    }
    map.get(key).criteria_rows_allocated += 1;
  }
  return [...map.values()].sort((a, b) => a.group_key.localeCompare(b.group_key));
}

function buildArtifact(parentReturn) {
  const criteriaRows = buildCriteriaRows(parentReturn);
  const classSummaryRows = summaryRows(criteriaRows, 'criterion_class', 'oi_local_route_criteria_class');
  const typeSummaryRows = summaryRows(criteriaRows, 'candidate_type', 'oi_local_route_criteria_type');
  const packetSummaryRows = summaryRows(criteriaRows, 'neutral_packet_slot', 'oi_local_route_criteria_packet');
  const laneSummaryRows = summaryRows(criteriaRows, 'lane_group', 'oi_local_route_criteria_lane');
  const blankCriteriaCells = criteriaRows.length * criteriaFields.length;

  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'openintro_numeracy_local_source_route_evidence_criteria_template_blank_no_evidence_no_returns_no_actual_routes_no_source_text_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Create a blank evidence-criteria template for every package 166 OpenIntro IMS local source-route candidate return row, defining the checks future reviewers must satisfy before any local route, source owner, permission path, terminology authority, modality route, source text, translation, or constructed surface can be promoted.',
    parent_artifacts: [
      parentReturnFile,
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_CANDIDATE_SHELF_TEMPLATE_20260703T113000Z',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_LANGUAGE_SOURCE_ALIGNMENT_TEMPLATE_20260703T111500Z',
      'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z'
    ],
    boundary: {
      artifact_is: [
        'blank local source-route evidence criteria template',
        'six criteria rows per package 166 return row',
        'future evidence review scaffold before route promotion'
      ],
      artifact_is_not: [
        'evidence review',
        'source route return',
        'actual source shelf',
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
      fill_rule: 'No criteria fields are filled here. Future evidence criteria reviews must be dated, route-labeled, and must not copy source prose unless a later policy explicitly allows it.',
      promotion_requires: [
        'dated candidate return',
        'dated evidence criteria review',
        'actual source route or owner evidence pointer',
        'owner, permission, terminology, and modality evidence where needed',
        'source text absence confirmation',
        'downstream gate limit confirmation'
      ]
    },
    inherited_parent_counts: {
      parent_local_source_route_candidate_return_rows: parentReturn.gate_state.openintro_local_source_route_candidate_return_rows,
      parent_candidate_returns_received: parentReturn.gate_state.candidate_returns_received,
      parent_actual_source_routes_confirmed: parentReturn.gate_state.actual_source_routes_confirmed,
      criteria_classes_per_return: evidenceCriteria.length
    },
    evidence_criteria_classes: evidenceCriteria,
    criteria_fields: criteriaFields,
    openintro_local_source_route_evidence_criterion_rows: criteriaRows,
    openintro_local_route_criteria_class_summary_rows: classSummaryRows,
    openintro_local_route_criteria_type_summary_rows: typeSummaryRows,
    openintro_local_route_criteria_packet_summary_rows: packetSummaryRows,
    openintro_local_route_criteria_lane_summary_rows: laneSummaryRows,
    gate_state: {
      openintro_local_source_route_evidence_criterion_rows: criteriaRows.length,
      evidence_criteria_class_rows: evidenceCriteria.length,
      local_route_criteria_class_summary_rows: classSummaryRows.length,
      local_route_criteria_type_summary_rows: typeSummaryRows.length,
      local_route_criteria_packet_summary_rows: packetSummaryRows.length,
      local_route_criteria_lane_summary_rows: laneSummaryRows.length,
      blank_criteria_fields_per_row: criteriaFields.length,
      blank_criteria_field_cells_allocated: blankCriteriaCells,
      criteria_fields_filled: 0,
      evidence_criteria_reviews_completed: 0,
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
      expected_local_source_route_evidence_criterion_rows: parentReturn.gate_state.openintro_local_source_route_candidate_return_rows * evidenceCriteria.length,
      expected_criteria_class_rows: evidenceCriteria.length,
      expected_type_summary_rows: parentReturn.gate_state.local_route_return_type_summary_rows,
      expected_packet_summary_rows: parentReturn.gate_state.local_route_return_packet_summary_rows,
      expected_lane_summary_rows: parentReturn.gate_state.local_route_return_lane_summary_rows,
      expected_blank_criteria_fields_per_row: criteriaFields.length,
      expected_blank_criteria_field_cells_allocated: blankCriteriaCells,
      zero_gate_assertions: zeroGateKeys,
      readiness_claims: 0
    },
    next_valid_artifacts: [
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_EVIDENCE_CRITERIA_REVIEW_RETURN_LEDGER_TEMPLATE_<timestamp>',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_LOCAL_SOURCE_ROUTE_CANDIDATE_RETURN_LEDGER_WITH_RETURNS_<timestamp>_only_after_dated_returns',
      'OPEN_TRANSLATION_OPENINTRO_NUMERACY_SELECTED_EXCERPT_SIDECAR_TEMPLATE_<timestamp>_only_after_policy_attribution_packet_local_source_route_and_evidence_returns'
    ],
    decision: 'Package 167 allocates blank local source-route evidence criteria rows only. It records no evidence, no returns, no actual source routes, no URLs, no owners, no contacts, no local terms, no source text, no excerpts, no translations, no constructed forms, and no readiness claims.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const classRows = artifact.openintro_local_route_criteria_class_summary_rows.map((row) => `| ${row.oi_local_route_criteria_class_summary_row_id} | ${row.group_key} | ${row.criteria_rows_allocated} | ${row.evidence_values_recorded} | ${row.criteria_passed} |`).join('\n');
  const typeRows = artifact.openintro_local_route_criteria_type_summary_rows.map((row) => `| ${row.oi_local_route_criteria_type_summary_row_id} | ${row.group_key} | ${row.criteria_rows_allocated} | ${row.evidence_source_pointers_recorded} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Local source-route evidence criterion rows: \`${g.openintro_local_source_route_evidence_criterion_rows}\`
- Evidence criteria classes: \`${g.evidence_criteria_class_rows}\`
- Blank criteria fields per row: \`${g.blank_criteria_fields_per_row}\`
- Blank criteria-field cells: \`${g.blank_criteria_field_cells_allocated}\`

## Criteria Classes

| Row | Criterion class | Criteria rows | Evidence values | Passed |
| --- | --- | ---: | ---: | ---: |
${classRows}

## Candidate-Type Summary

| Row | Candidate type | Criteria rows | Evidence pointers |
| --- | --- | ---: | ---: |
${typeRows}

## Zero Gates

\`0\` criteria fields filled, \`0\` evidence criteria reviews completed, \`0\` evidence values recorded, \`0\` evidence pointers recorded, \`0\` criteria passed/failed, \`0\` candidate returns received, \`0\` actual routes confirmed, \`0\` source routes/URLs/owners recorded, \`0\` owner contacts, \`0\` local routes accepted, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: blank local source-route evidence criteria template only. This artifact is not evidence review, source-route evidence, source-owner contact, source authorization, translation, constructed-language proposal, publication claim, or pilot claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [
    ['section', 'criterion_row_id', 'parent_return_row_id', 'packet_slot', 'lane_group', 'candidate_type', 'criterion_class', 'fields_filled', 'evidence_recorded', 'criterion_passed'].map(csvCell).join(',')
  ];
  for (const row of artifact.openintro_local_source_route_evidence_criterion_rows) {
    rows.push([
      'openintro_local_source_route_evidence_criterion_row',
      row.openintro_local_source_route_evidence_criterion_row_id,
      row.parent_return_row_id,
      row.neutral_packet_slot,
      row.lane_group,
      row.candidate_type,
      row.criterion_class,
      row.criteria_fields_filled,
      row.evidence_value_recorded,
      row.criterion_passed
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
    status: 'pointer_only_package167_openintro_numeracy_local_source_route_evidence_criteria_template_note_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: 'Package 167 records a blank OpenIntro IMS numeracy local source-route evidence criteria template derived from package 166 candidate return rows.',
    counts: {
      openintro_local_source_route_evidence_criterion_rows: g.openintro_local_source_route_evidence_criterion_rows,
      evidence_criteria_class_rows: g.evidence_criteria_class_rows,
      blank_criteria_fields_per_row: g.blank_criteria_fields_per_row,
      blank_criteria_field_cells_allocated: g.blank_criteria_field_cells_allocated
    },
    zero_gates: {
      criteria_fields_filled: 0,
      evidence_values_recorded: 0,
      evidence_source_pointers_recorded: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      candidate_returns_received: 0,
      actual_source_routes_confirmed: 0,
      candidate_source_routes_recorded: 0,
      candidate_source_urls_recorded: 0,
      candidate_source_owners_contacted: 0,
      local_source_routes_accepted: 0,
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
  return `# Package 167 OpenIntro Numeracy Local Source-Route Evidence Criteria Template Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 167 records \`${g.openintro_local_source_route_evidence_criterion_rows}\` blank local source-route evidence criterion rows and \`${g.blank_criteria_field_cells_allocated}\` blank criteria-field cells for OpenIntro IMS statistics/public numeracy.

Zero gates: \`0\` criteria fields filled, \`0\` evidence values or pointers recorded, \`0\` criteria passed/failed, \`0\` candidate returns received, \`0\` actual source routes confirmed, \`0\` source routes/URLs/owners recorded, \`0\` owner contacts, \`0\` local routes accepted, \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` readiness claims.

Boundary: blank local source-route evidence criteria template only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, actual route record, source-owner contact, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_openintro_numeracy_local_source_route_evidence_criteria_template',
    artifact: artifactId,
    current_use: `${g.openintro_local_source_route_evidence_criterion_rows} blank local source-route evidence criteria rows; ${g.blank_criteria_field_cells_allocated} blank criteria cells; 0 evidence, 0 returns, 0 actual routes, 0 owners, 0 source text, 0 translations, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  else order.push(packageRow);
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_template = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_openintro_numeracy_local_source_route_evidence_criteria_rows: g.openintro_local_source_route_evidence_criterion_rows,
    current_openintro_numeracy_evidence_values_recorded: 0,
    current_openintro_numeracy_actual_source_routes_confirmed: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_evidence_criteria_review_return_template_only_no_evidence_no_returns_no_actual_routes_no_source_text_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation OpenIntro numeracy local source-route evidence criteria template',
    route: artifactId,
    license_status_to_recheck: 'blank_evidence_criteria_template_only_recheck_candidate_returns_route_evidence_owner_permission_terminology_modality_and_source_text_absence_before_any_excerpt_adaptation_translation_or_surface',
    best_translation_use: 'blank evidence criteria scaffold before source route evidence review, local route acceptance, selected excerpt, local terms, translation, or constructed-surface decisions',
    candidate_lanes: [
      'statistics_public_numeracy',
      'OpenIntro_IMS',
      'data_literacy',
      'public_service_numeracy',
      'local_source_route_evidence_criteria_template',
      'world_family_lane_alignment'
    ],
    priority: 1,
    status: 'blank_local_source_route_evidence_criteria_template_no_evidence_no_returns_no_actual_routes_no_source_text_no_translation_no_forms_no_pilot',
    gate_state: {
      openintro_local_source_route_evidence_criterion_rows: g.openintro_local_source_route_evidence_criterion_rows,
      blank_criteria_field_cells_allocated: g.blank_criteria_field_cells_allocated,
      evidence_values_recorded: 0,
      evidence_source_pointers_recorded: 0,
      criteria_passed: 0,
      criteria_failed: 0,
      candidate_returns_received: 0,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_template: ${artifactId}_${g.openintro_local_source_route_evidence_criterion_rows}_blank_criteria_rows_0_evidence_0_source_text_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_template_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_template_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_openintro_numeracy_local_source_route_evidence_criteria_rows: g.openintro_local_source_route_evidence_criterion_rows,
    current_openintro_numeracy_evidence_values_recorded: 0,
    current_openintro_numeracy_source_text_or_excerpt_files: 0,
    current_openintro_numeracy_translated_passages: 0,
    current_openintro_numeracy_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_template = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_template: ${artifactId}_blank_criteria_template_before_any_evidence_returns_actual_routes_terms_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_template = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: records ${g.openintro_local_source_route_evidence_criterion_rows} blank OpenIntro IMS numeracy local source-route evidence criteria rows; substantive upload-bound artifact; 0 evidence, 0 returns, 0 actual routes, 0 URLs, 0 owners, 0 contacts, 0 local terms, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OpenIntro numeracy local source-route evidence criteria template; ${g.openintro_local_source_route_evidence_criterion_rows} blank criteria rows, ${g.blank_criteria_field_cells_allocated} blank cells, 0 evidence, 0 returns, 0 source text, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 167: OpenIntro numeracy local source-route evidence criteria template. It records ${g.openintro_local_source_route_evidence_criterion_rows} blank evidence criteria rows while keeping 0 evidence values, 0 evidence pointers, 0 returns received, 0 actual routes, 0 URLs, 0 owners, 0 source-owner contacts, 0 local terms, 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog/control work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation OpenIntro numeracy local source-route evidence criteria template | ${artifactId} | Blank local source-route evidence criteria template; ${g.openintro_local_source_route_evidence_criterion_rows} rows, 0 evidence, 0 source text, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_template_artifact: \`${artifactId}\` (${g.openintro_local_source_route_evidence_criterion_rows} blank criteria rows; 0 evidence; 0 source text; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_openintro_numeracy_local_source_route_evidence_criteria_template: \`${artifactId}\`; blank OpenIntro IMS numeracy local source-route evidence criteria template, no evidence, returns, source text, excerpts, local terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OpenIntro IMS public numeracy local source-route evidence criteria template; substantive and upload-bound, but not evidence review, actual source discovery, source text, translation, constructed form, local authority review, source-owner contact, local term decision, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_openintro_numeracy_local_source_route_evidence_criteria_template' },
    { filename: `${artifactId}.md`, class: 'open_translation_openintro_numeracy_local_source_route_evidence_criteria_template' },
    { filename: `${artifactId}.csv`, class: 'open_translation_openintro_numeracy_local_source_route_evidence_criteria_template' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package167_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package167_coordination_note' },
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
  upload.obj.package167_upload_queue_update = {
    captured_utc: '2026-07-03T12:02:00Z',
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
  const step = 'Stage package 167 OpenIntro numeracy local source-route evidence criteria template artifacts as substantive beyond-core translation/source-route catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (g.openintro_local_source_route_evidence_criterion_rows !== artifact.validation_snapshot.expected_local_source_route_evidence_criterion_rows) failures.push(`criteria_rows_mismatch_${g.openintro_local_source_route_evidence_criterion_rows}`);
  if (g.evidence_criteria_class_rows !== artifact.validation_snapshot.expected_criteria_class_rows) failures.push(`criteria_class_rows_mismatch_${g.evidence_criteria_class_rows}`);
  if (g.local_route_criteria_type_summary_rows !== artifact.validation_snapshot.expected_type_summary_rows) failures.push(`type_summary_rows_mismatch_${g.local_route_criteria_type_summary_rows}`);
  if (g.local_route_criteria_packet_summary_rows !== artifact.validation_snapshot.expected_packet_summary_rows) failures.push(`packet_summary_rows_mismatch_${g.local_route_criteria_packet_summary_rows}`);
  if (g.local_route_criteria_lane_summary_rows !== artifact.validation_snapshot.expected_lane_summary_rows) failures.push(`lane_summary_rows_mismatch_${g.local_route_criteria_lane_summary_rows}`);
  if (g.blank_criteria_fields_per_row !== artifact.validation_snapshot.expected_blank_criteria_fields_per_row) failures.push(`blank_fields_mismatch_${g.blank_criteria_fields_per_row}`);
  if (g.blank_criteria_field_cells_allocated !== artifact.validation_snapshot.expected_blank_criteria_field_cells_allocated) failures.push(`blank_cells_mismatch_${g.blank_criteria_field_cells_allocated}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.openintro_local_source_route_evidence_criterion_rows) {
    const filled = criteriaFields.some((field) => row[field] !== null);
    if (
      filled ||
      row.criteria_fields_filled !== 0 ||
      row.evidence_criterion_review_completed ||
      row.evidence_value_recorded ||
      row.evidence_source_pointer_recorded ||
      row.criterion_passed ||
      row.criterion_failed ||
      row.source_text_or_excerpt_allowed_now ||
      row.translation_allowed_now ||
      row.local_surface_allowed_now ||
      row.pilot_ready
    ) {
      failures.push(`nonblank_or_open_criteria_row_${row.openintro_local_source_route_evidence_criterion_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const parentReturn = (await readJson(parentReturnFile)).obj;
const artifact = buildArtifact(parentReturn);
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
  openintro_local_source_route_evidence_criterion_rows: artifact.gate_state.openintro_local_source_route_evidence_criterion_rows,
  evidence_criteria_class_rows: artifact.gate_state.evidence_criteria_class_rows,
  blank_criteria_field_cells_allocated: artifact.gate_state.blank_criteria_field_cells_allocated,
  criteria_fields_filled: artifact.gate_state.criteria_fields_filled,
  evidence_values_recorded: artifact.gate_state.evidence_values_recorded,
  evidence_source_pointers_recorded: artifact.gate_state.evidence_source_pointers_recorded,
  criteria_passed: artifact.gate_state.criteria_passed,
  criteria_failed: artifact.gate_state.criteria_failed,
  candidate_returns_received: artifact.gate_state.candidate_returns_received,
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
