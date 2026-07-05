import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_CONSTRUCTION_SEED_START_INDEX_20260703T070000Z';
const noteId = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_CONSTRUCTION_SEED_START_INDEX_NOTE_20260703T070100Z';
const generatedUtc = '2026-07-03T07:00:00Z';
const noteGeneratedUtc = '2026-07-03T07:01:00Z';
const packageOrder = 147;
const queueCandidateId = 'OTCQ-SEMI-CONSTRUCTED-RELATION-FUNCTION-REVIEW-ONLY-CONSTRUCTION-SEED-START-INDEX-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const catalogStem = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_TRANSLATION_CANDIDATE_CATALOG_20260701T180000Z';
const routeSheetStem = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_CANDIDATE_REVIEWER_ROUTE_SHEET_20260701T183000Z';
const dispatchTaxonomyStem = 'SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_CANDIDATE_DISPATCH_EVIDENCE_CRITERIA_AND_ROUTE_LABEL_TAXONOMY_20260701T213000Z';
const parentArtifacts = [
  catalogStem,
  routeSheetStem,
  dispatchTaxonomyStem,
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_CANDIDATE_ROUTE_DISPATCH_READINESS_CHECKLIST_20260701T200000Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_DMOI_METADATA_SOURCE_COORDINATE_RETURN_REQUEST_PACKET_20260701T170000Z'
];

const openSeedIds = new Set(['DMOI-RF-CAT-01', 'DMOI-RF-CAT-02', 'DMOI-RF-CAT-03', 'DMOI-RF-CAT-06']);
const supportOnlyIds = new Set(['DMOI-RF-CAT-08']);

const slotEnvelopes = {
  'DMOI-RF-CAT-01': [
    'relation_like_statement_slot',
    'ordered_pair_membership_slot',
    'function_like_mapping_slot',
    'graph_of_function_slot',
    'non_function_relation_counter_slot'
  ],
  'DMOI-RF-CAT-02': [
    'domain_slot',
    'codomain_slot',
    'range_or_image_slot',
    'outside_domain_boundary_slot'
  ],
  'DMOI-RF-CAT-03': [
    'injective_property_slot',
    'surjective_property_slot',
    'bijective_property_slot',
    'many_to_one_counterexample_slot'
  ],
  'DMOI-RF-CAT-06': [
    'arrow_reading_slot',
    'maps_to_reading_slot',
    'input_output_reading_slot',
    'function_name_application_slot'
  ]
};

const packetShapes = {
  'DMOI-RF-CAT-01': 'set_function_packet_boundary_review_seed',
  'DMOI-RF-CAT-02': 'set_function_packet_domain_codomain_range_seed',
  'DMOI-RF-CAT-03': 'proof_literacy_micro_packet_function_property_seed',
  'DMOI-RF-CAT-04': 'held_equivalence_order_packet_after_relation_boundary_return',
  'DMOI-RF-CAT-05': 'held_operation_language_packet_after_example_route_return',
  'DMOI-RF-CAT-06': 'notation_accessibility_sidecar_seed',
  'DMOI-RF-CAT-07': 'held_relation_property_packet_after_boundary_and_order_returns',
  'DMOI-RF-CAT-08': 'source_authority_reader_packet_support_shelf'
};

const holdReasons = {
  'DMOI-RF-CAT-04': 'equivalence and order terms are high-transfer but need local-standard and relation-boundary returns before any bridge slot opens',
  'DMOI-RF-CAT-05': 'composition and inverse language needs example-route review to avoid algebra/function ambiguity before slot opening',
  'DMOI-RF-CAT-07': 'relation-property terms should wait for relation/function boundary and equivalence/order route evidence'
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

function buildSeedRows(catalog, routeSheet) {
  const routesByCatalog = new Map((routeSheet.route_rows || []).map((row) => [row.parent_catalog_row_id, row]));
  let openOrder = 0;
  return catalog.catalog_rows.map((row, index) => {
    const route = routesByCatalog.get(row.catalog_row_id) || {};
    const seedOpen = openSeedIds.has(row.catalog_row_id);
    const supportOnly = supportOnlyIds.has(row.catalog_row_id);
    if (seedOpen) openOrder += 1;
    const seedState = seedOpen
      ? 'review_only_semantic_slot_envelope_opened_no_surfaces'
      : supportOnly
        ? 'source_shelf_support_row_no_construction_slot'
        : 'held_for_more_route_evidence_no_construction_slot';
    const slots = slotEnvelopes[row.catalog_row_id] || [];
    return {
      seed_row_id: `DMOI-RF-ROCSI-${String(index + 1).padStart(2, '0')}`,
      parent_catalog_row_id: row.catalog_row_id,
      parent_route_row_id: route.route_row_id || null,
      candidate_area: row.candidate_area,
      candidate_kind: row.candidate_kind,
      review_only_start_order: seedOpen ? openOrder : null,
      seed_state: seedState,
      selected_packet_shape: packetShapes[row.catalog_row_id] || 'defer_until_review_return',
      linked_routes: row.linked_routes,
      linked_term_families: row.linked_term_families,
      coordinate_rows_available: row.coordinate_rows_available,
      source_file_hints_for_ranking_only: row.source_file_hints,
      reviewer_role_route_label: route.reviewer_role || null,
      inherited_reviewer_questions: route.reviewer_questions || [],
      allowed_return_fields: route.allowed_return_fields || [],
      abstract_semantic_slot_envelope: slots,
      slot_envelope_opened: seedOpen,
      source_shelf_support_only: supportOnly,
      held_reason: seedOpen || supportOnly ? null : holdReasons[row.catalog_row_id] || 'held until dated reviewer return and local-standard route evidence exist',
      allowed_now: seedOpen
        ? [
          'name abstract semantic slots for reviewer discussion',
          'rank source file hints without selecting exact source passages',
          'prepare return fields for local-standard and bridge-boundary review'
        ]
        : [
          'preserve candidate source coordinates',
          'keep source file hints available for future ranking',
          'wait for reviewer route evidence before opening slots'
        ],
      blocked_now: [
        'copied_source_prose',
        'copied_definitions_or_examples',
        'source_excerpt_text',
        'source_text_or_excerpt_sidecar',
        'proposed_bridge_lexeme',
        'proposed_bridge_morpheme',
        'accepted_bridge_surface',
        'accepted_local_language_term',
        'translated_passage',
        'pilot_or_publication_claim'
      ],
      next_required_evidence: seedOpen
        ? [
          'dated reviewer return for source-file ranking',
          'local-standard-required-before-bridge-slot note',
          'license/attribution gate note before any exact passage request',
          'surface sidecar template before any proposed form'
        ]
        : [
          'route evidence sufficient to open a review-only slot envelope',
          'dated reviewer return or explicit no-construction decision'
        ],
      proposed_bridge_lexemes: [],
      proposed_bridge_morphemes: [],
      accepted_bridge_surfaces: [],
      accepted_local_language_terms: [],
      translated_passages: []
    };
  });
}

function buildArtifact(catalog, routeSheet, dispatchTaxonomy) {
  const seedRows = buildSeedRows(catalog, routeSheet);
  const openRows = seedRows.filter((row) => row.slot_envelope_opened);
  const supportRows = seedRows.filter((row) => row.source_shelf_support_only);
  const heldRows = seedRows.filter((row) => !row.slot_envelope_opened && !row.source_shelf_support_only);
  const constructionSlotsNamed = openRows.reduce((sum, row) => sum + row.abstract_semantic_slot_envelope.length, 0);
  const sourceCoordinateRowsReferenced = seedRows.reduce((sum, row) => sum + row.coordinate_rows_available, 0);
  const sourceFileHintsReferenced = seedRows.reduce((sum, row) => sum + row.source_file_hints_for_ranking_only.length, 0);
  const routeLabelClassesReferenced = new Set((dispatchTaxonomy.route_label_taxonomy || []).map((row) => row.route_label_class)).size;
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'review_only_construction_seed_start_index_no_forms_no_source_text_no_excerpts_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Start the obvious review-only semi-constructed relation/function path by opening abstract semantic slot envelopes for source-grounded DMOI candidate areas, while keeping all actual language forms, source passages, excerpts, surfaces, translations, dispatches, returns, and readiness claims closed.',
    parent_artifacts: parentArtifacts,
    source_identity: catalog.source_identity,
    seed_boundary: {
      seed_is: 'review-only construction seed start index for abstract semantic slots',
      seed_is_not: [
        'accepted constructed language form',
        'bridge lexeme proposal',
        'bridge morpheme proposal',
        'grammar rule acceptance',
        'local-language term decision',
        'source excerpt selection',
        'source text copy',
        'translation draft',
        'reviewer return',
        'dispatch log',
        'pilot or publication claim'
      ],
      why_now: 'The catalog and route sheet already identify source-coordinate grounded relation/function candidate areas and reviewer questions; the safe constructive action is to open abstract slots only, not surfaces.',
      promotion_requires: [
        'dated reviewer returns',
        'local-standard gate note',
        'license/attribution note before exact passages',
        'surface sidecar before any proposed form',
        'separate completion audit before any readiness claim'
      ]
    },
    review_only_construction_seed_rows: seedRows,
    gate_state: {
      review_only_construction_seed_rows: seedRows.length,
      review_only_semantic_slot_envelopes_opened: openRows.length,
      source_shelf_support_rows: supportRows.length,
      rows_held_for_more_route_evidence: heldRows.length,
      construction_slots_named_for_review_only: constructionSlotsNamed,
      source_coordinate_rows_referenced_as_metadata: sourceCoordinateRowsReferenced,
      source_file_hints_referenced_as_metadata: sourceFileHintsReferenced,
      route_label_classes_referenced_as_taxonomy: routeLabelClassesReferenced,
      source_text_copied: 0,
      source_definitions_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      source_text_or_excerpt_files_created: 0,
      exact_line_spans_selected: 0,
      candidate_line_ranges_selected: 0,
      reviewer_returns_ingested: 0,
      dispatch_log_entries: 0,
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
      expected_seed_rows: 8,
      expected_open_slot_envelopes: 4,
      expected_support_rows: 1,
      expected_held_rows: 3,
      expected_construction_slots_named_for_review_only: 17,
      zero_gate_assertions: [
        'source_text_copied',
        'source_definitions_copied',
        'source_examples_copied',
        'source_passages_selected',
        'source_text_or_excerpt_files_created',
        'exact_line_spans_selected',
        'candidate_line_ranges_selected',
        'reviewer_returns_ingested',
        'dispatch_log_entries',
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
      'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SLOT_RETURN_LEDGER_TEMPLATE_<timestamp>',
      'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SURFACE_SIDECAR_TEMPLATE_BLANK_<timestamp>',
      'SEMI_CONSTRUCTED_RELATION_FUNCTION_NO_CONSTRUCTION_DECISION_LEDGER_<timestamp>'
    ],
    decision: 'Start four review-only semantic slot envelopes and hold three candidate areas plus one support shelf without proposing or accepting any language forms.'
  };
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const rows = artifact.review_only_construction_seed_rows.map((row) => `| ${row.seed_row_id} | ${row.parent_catalog_row_id} | ${row.candidate_area} | ${row.seed_state} | ${row.coordinate_rows_available} | ${row.abstract_semantic_slot_envelope.length} | ${row.selected_packet_shape} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Seed rows: \`${g.review_only_construction_seed_rows}\`
- Review-only semantic slot envelopes opened: \`${g.review_only_semantic_slot_envelopes_opened}\`
- Source-shelf support rows: \`${g.source_shelf_support_rows}\`
- Rows held for more route evidence: \`${g.rows_held_for_more_route_evidence}\`
- Construction slots named for review only: \`${g.construction_slots_named_for_review_only}\`
- Source-coordinate rows referenced as metadata: \`${g.source_coordinate_rows_referenced_as_metadata}\`
- Source-file hints referenced as metadata: \`${g.source_file_hints_referenced_as_metadata}\`

## Seed Rows

| Row | Parent catalog row | Candidate area | State | Coordinate rows | Review-only slots | Packet shape |
| --- | --- | --- | --- | ---: | ---: | --- |
${rows}

## Zero Gates

- Source text/definitions/examples copied: \`0 / 0 / 0\`
- Source passages/exact spans/candidate line ranges selected: \`0 / 0 / 0\`
- Source-text/excerpt files created: \`0\`
- Reviewer returns ingested / dispatch log entries: \`0 / 0\`
- Proposed bridge lexemes/morphemes/grammar rules: \`0 / 0 / 0\`
- Accepted bridge/local surfaces: \`0 / 0\`
- Translated passages: \`0\`
- Readiness: \`publication=false, translation=false, constructed_surface=false, pilot=false\`

Boundary: this starts abstract review-only semantic slot envelopes only. It is not a source excerpt, not a translation, not an accepted bridge form, not a local-language term decision, not a dispatch, not a return, and not a readiness claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['seed_row_id', 'parent_catalog_row_id', 'candidate_area', 'seed_state', 'start_order', 'coordinate_rows_available', 'slot_count', 'selected_packet_shape', 'held_reason'].map(csvCell).join(','));
  for (const row of artifact.review_only_construction_seed_rows) {
    rows.push([
      row.seed_row_id,
      row.parent_catalog_row_id,
      row.candidate_area,
      row.seed_state,
      row.review_only_start_order,
      row.coordinate_rows_available,
      row.abstract_semantic_slot_envelope.length,
      row.selected_packet_shape,
      row.held_reason
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
    status: 'pointer_only_package147_review_only_construction_seed_note_no_upload_coordination_no_source_text_no_translation_no_readiness',
    summary: 'Package 147 starts a review-only semi-constructed relation/function seed index with abstract semantic slot envelopes only.',
    counts: {
      review_only_construction_seed_rows: g.review_only_construction_seed_rows,
      review_only_semantic_slot_envelopes_opened: g.review_only_semantic_slot_envelopes_opened,
      construction_slots_named_for_review_only: g.construction_slots_named_for_review_only,
      source_coordinate_rows_referenced_as_metadata: g.source_coordinate_rows_referenced_as_metadata,
      rows_held_for_more_route_evidence: g.rows_held_for_more_route_evidence
    },
    zero_gates: {
      source_text_copied: 0,
      source_text_or_excerpt_files_created: 0,
      reviewer_returns_ingested: 0,
      dispatch_log_entries: 0,
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
  return `# Package 147 Review-Only Construction Seed Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 147 starts \`${g.review_only_semantic_slot_envelopes_opened}\` review-only semantic slot envelopes with \`${g.construction_slots_named_for_review_only}\` abstract slots from DMOI relation/function metadata. It references \`${g.source_coordinate_rows_referenced_as_metadata}\` source-coordinate rows as metadata only.

Zero gates: \`0\` source text copied, \`0\` exact spans selected, \`0\` source-text/excerpt files, \`0\` reviewer returns ingested, \`0\` dispatch logs, \`0\` proposed bridge lexemes, \`0\` proposed bridge morphemes, \`0\` accepted bridge or local surfaces, \`0\` translations, \`0\` readiness claims.

Boundary: review-only seed index only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, excerpt, attribution notice fill, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
      role: 'semi_constructed_relation_function_review_only_construction_seed_start_index_support',
      artifact: artifactId,
      current_use: 'review-only construction seed start index; 8 seed rows; 4 semantic slot envelopes opened; 17 abstract slots named; 0 source text, 0 excerpts, 0 forms, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_semi_constructed_relation_function_review_only_construction_seed_start_index = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_relation_function_review_only_seed_rows: g.review_only_construction_seed_rows,
    current_relation_function_review_only_slot_envelopes_opened: g.review_only_semantic_slot_envelopes_opened,
    current_relation_function_review_only_slots_named: g.construction_slots_named_for_review_only,
    current_relation_function_review_only_source_text_or_excerpt_files: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_return_ledger_or_blank_surface_sidecar_only_after_review_returns_no_source_text_no_excerpts_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Semi-constructed relation/function review-only construction seed start index',
    route: artifactId,
    license_status_to_recheck: 'metadata_only_from_cached_DMOI_coordinate_catalog_no_source_text_no_excerpts_recheck_exact_source_before_any_passage_or_adaptation',
    best_translation_use: 'abstract slot planning for future set/function and proof-literacy micro-packets, before surfaces or translations',
    candidate_lanes: [
      'relation_function_bridge_register',
      'set_function_packet',
      'proof_literacy_micro_packet',
      'notation_accessibility_sidecar',
      'review_only_construction_seed'
    ],
    priority: 1,
    status: 'review_only_seed_index_no_source_text_no_excerpts_no_surfaces_no_translation_no_pilot',
    gate_state: {
      review_only_construction_seed_rows: g.review_only_construction_seed_rows,
      review_only_semantic_slot_envelopes_opened: g.review_only_semantic_slot_envelopes_opened,
      construction_slots_named_for_review_only: g.construction_slots_named_for_review_only,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      source_text_or_excerpt_files_created: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_semi_constructed_relation_function_review_only_construction_seed_start_index: ${artifactId}_4_review_only_slot_envelopes_17_abstract_slots_0_source_text_0_excerpts_0_surfaces_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_semi_constructed_relation_function_review_only_construction_seed_start_index_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_semi_constructed_relation_function_review_only_construction_seed_start_index_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_relation_function_review_only_seed_rows: g.review_only_construction_seed_rows,
    current_relation_function_review_only_slot_envelopes_opened: g.review_only_semantic_slot_envelopes_opened,
    current_relation_function_review_only_slots_named: g.construction_slots_named_for_review_only,
    current_relation_function_review_only_source_text_or_excerpt_files: 0,
    current_relation_function_review_only_surfaces: 0,
    current_relation_function_review_only_translations: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_semi_constructed_relation_function_review_only_construction_seed_start_index = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_semi_constructed_relation_function_review_only_construction_seed_start_index: ${artifactId}_review_only_slots_no_forms_no_source_text_no_excerpts_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_semi_constructed_relation_function_review_only_construction_seed_start_index = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: starts four review-only DMOI relation/function abstract semantic slot envelopes with 17 named slots from cached source-coordinate metadata; 0 source text, 0 excerpts, 0 bridge lexemes, 0 morphemes, 0 accepted surfaces, 0 local-language terms, 0 translations, 0 readiness; local upload queue should preserve it as substantive construction-method material.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - Semi-constructed relation/function review-only construction seed start index; 8 seed rows, 4 abstract semantic slot envelopes opened, 17 slots named for review only, 0 source text, 0 excerpts, 0 bridge lexemes, 0 morphemes, 0 accepted surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 147: review-only semi-constructed relation/function construction seed start index. It opens 4 abstract semantic slot envelopes and names 17 slots for review only while keeping 0 source text, 0 excerpts, 0 bridge forms, 0 accepted surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Semi-constructed relation/function review-only construction seed start index | ${artifactId} | Review-only seed scaffold; 8 rows, 4 semantic slot envelopes, 17 abstract slots, 0 source text, 0 excerpts, 0 proposed forms, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_semi_constructed_relation_function_review_only_construction_seed_start_index_artifact: \`${artifactId}\` (8 seed rows; 4 review-only slot envelopes; 17 abstract slots; 0 source text; 0 excerpts; no surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_semi_constructed_relation_function_review_only_construction_seed_start_index: \`${artifactId}\`; review-only construction seed only, no source text, excerpts, proposed bridge forms, accepted local terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: starts the DMOI relation/function review-only construction seed by opening abstract semantic slot envelopes only; slots are not lexemes, morphemes, accepted forms, local-language terms, source excerpts, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'semi_constructed_relation_function_review_only_construction_seed_start_index' },
    { filename: `${artifactId}.md`, class: 'semi_constructed_relation_function_review_only_construction_seed_start_index' },
    { filename: `${artifactId}.csv`, class: 'semi_constructed_relation_function_review_only_construction_seed_start_index' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'semi_constructed_relation_function_package147_coordination_note' },
    { filename: `${noteId}.md`, class: 'semi_constructed_relation_function_package147_coordination_note' },
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
  upload.obj.package147_upload_queue_update = {
    captured_utc: '2026-07-03T07:02:00Z',
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
  const step = 'Stage package 147 semi-constructed relation/function review-only construction seed start index artifacts with this queue as substantive construction-method material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  const rows = artifact.review_only_construction_seed_rows;
  if (rows.length !== artifact.validation_snapshot.expected_seed_rows) failures.push(`seed_rows_mismatch_${rows.length}`);
  if (g.review_only_semantic_slot_envelopes_opened !== artifact.validation_snapshot.expected_open_slot_envelopes) failures.push(`open_slot_envelopes_mismatch_${g.review_only_semantic_slot_envelopes_opened}`);
  if (g.source_shelf_support_rows !== artifact.validation_snapshot.expected_support_rows) failures.push(`support_rows_mismatch_${g.source_shelf_support_rows}`);
  if (g.rows_held_for_more_route_evidence !== artifact.validation_snapshot.expected_held_rows) failures.push(`held_rows_mismatch_${g.rows_held_for_more_route_evidence}`);
  if (g.construction_slots_named_for_review_only !== artifact.validation_snapshot.expected_construction_slots_named_for_review_only) failures.push(`slot_count_mismatch_${g.construction_slots_named_for_review_only}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of rows) {
    if (row.proposed_bridge_lexemes.length || row.proposed_bridge_morphemes.length || row.accepted_bridge_surfaces.length || row.accepted_local_language_terms.length || row.translated_passages.length) {
      failures.push(`row_contains_surface_or_translation_${row.seed_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const catalog = (await readJson(catalogStem)).obj;
const routeSheet = (await readJson(routeSheetStem)).obj;
const dispatchTaxonomy = (await readJson(dispatchTaxonomyStem)).obj;
const artifact = buildArtifact(catalog, routeSheet, dispatchTaxonomy);
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
  review_only_construction_seed_rows: artifact.gate_state.review_only_construction_seed_rows,
  review_only_semantic_slot_envelopes_opened: artifact.gate_state.review_only_semantic_slot_envelopes_opened,
  source_shelf_support_rows: artifact.gate_state.source_shelf_support_rows,
  rows_held_for_more_route_evidence: artifact.gate_state.rows_held_for_more_route_evidence,
  construction_slots_named_for_review_only: artifact.gate_state.construction_slots_named_for_review_only,
  source_coordinate_rows_referenced_as_metadata: artifact.gate_state.source_coordinate_rows_referenced_as_metadata,
  source_file_hints_referenced_as_metadata: artifact.gate_state.source_file_hints_referenced_as_metadata,
  source_text_copied: artifact.gate_state.source_text_copied,
  source_text_or_excerpt_files_created: artifact.gate_state.source_text_or_excerpt_files_created,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  accepted_local_language_terms: artifact.gate_state.accepted_local_language_terms,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
