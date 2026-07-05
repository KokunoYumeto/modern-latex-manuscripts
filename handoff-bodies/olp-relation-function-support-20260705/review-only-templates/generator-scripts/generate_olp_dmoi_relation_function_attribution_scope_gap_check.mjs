import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_ATTRIBUTION_SCOPE_GAP_CHECK_20260702T134500Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_ATTRIBUTION_SCOPE_GAP_CHECK_NOTE_20260702T134600Z';
const generatedUtc = '2026-07-02T13:45:00Z';
const noteGeneratedUtc = '2026-07-02T13:46:00Z';
const packageOrder = 113;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-ATTRIBUTION-SCOPE-GAP-CHECK-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentArtifacts = [
  'OLP_DMOI_RELATION_FUNCTION_SOURCE_POINTER_PACKET_20260702T133000Z',
  'OPEN_RELATION_FUNCTION_TRANSLATION_SOURCE_CANDIDATE_SHELF_20260702T131500Z',
  'OLP_FIRST_PROOF_PACKET_ATTRIBUTION_FILLED_BLANK_20260630T073304Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_TRANSLATION_CANDIDATE_CATALOG_20260701T180000Z'
];

const gapFieldDefinitions = [
  {
    field_id: 'selected_source_system',
    required_before: 'any exact excerpt or adaptation',
    why_required: 'prevents mixing OLP and DMOI obligations without a row-level source decision'
  },
  {
    field_id: 'selected_source_file_or_route',
    required_before: 'line-span candidate selection',
    why_required: 'turns shelf-level routes into an auditable file-level target'
  },
  {
    field_id: 'exact_line_span',
    required_before: 'source text capture',
    why_required: 'keeps future excerpts tied to exact paths and line boundaries'
  },
  {
    field_id: 'selected_excerpt_id',
    required_before: 'attribution notice fill',
    why_required: 'gives every future source passage a stable local identifier'
  },
  {
    field_id: 'source_title_or_edition',
    required_before: 'attribution notice fill',
    why_required: 'records the exact title or edition used for the selected excerpt'
  },
  {
    field_id: 'source_author_or_project_attribution',
    required_before: 'attribution notice fill',
    why_required: 'keeps attribution separate from later translation or surface choices'
  },
  {
    field_id: 'source_url_or_repository_route',
    required_before: 'attribution notice fill',
    why_required: 'preserves the public source route for reviewer and upload audit'
  },
  {
    field_id: 'license_url_or_license_file_route',
    required_before: 'attribution notice fill',
    why_required: 'pins the license route used for the selected excerpt'
  },
  {
    field_id: 'license_compatibility_note',
    required_before: 'mixed-source packet assembly',
    why_required: 'separates OLP CC BY 4.0 handling from the conservative DMOI NC/SA posture'
  },
  {
    field_id: 'noncommercial_sharealike_handling_if_dmoi_used',
    required_before: 'any DMOI-derived adaptation',
    why_required: 'keeps DMOI constraints visible before reuse or publication planning'
  },
  {
    field_id: 'modification_or_adaptation_notice',
    required_before: 'any adapted passage',
    why_required: 'records whether future material is quoted, adapted, summarized, or newly authored'
  },
  {
    field_id: 'reviewer_scope_return_id',
    required_before: 'local or bridge surface proposal',
    why_required: 'blocks source-driven wording until a non-personal scope return exists'
  },
  {
    field_id: 'local_register_decision',
    required_before: 'local-language surface acceptance',
    why_required: 'prevents mathematical source evidence from pretending to be local authority'
  },
  {
    field_id: 'translation_or_surface_owner_acceptance',
    required_before: 'translation drafting or semi-constructed surface acceptance',
    why_required: 'keeps packet construction separate from language-owner acceptance'
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

function buildGapRows(pointerPacket) {
  return pointerPacket.source_pointer_rows.map((row, index) => {
    const usesOlp = row.olp_shelf_ids.length > 0;
    const usesDmoi = row.dmoi_catalog_row_ids.length > 0;
    return {
      gap_check_row_id: `ODRF-ATTR-GAP-${String(index + 1).padStart(2, '0')}`,
      parent_pointer_row_id: row.pointer_row_id,
      packet_unit: row.packet_unit,
      olp_shelf_ids: row.olp_shelf_ids,
      dmoi_catalog_row_ids: row.dmoi_catalog_row_ids,
      source_systems_implicated: [
        ...(usesOlp ? ['OLP_CC_BY_4_0'] : []),
        ...(usesDmoi ? ['DMOI_CONSERVATIVE_NC_SA_RECHECK_REQUIRED'] : [])
      ],
      olp_routes_available_count: row.olp_source_routes.length,
      dmoi_file_hints_available_count: row.dmoi_source_file_hints.length,
      exact_excerpt_selection_status: 'not_started',
      required_gap_fields: gapFieldDefinitions.map((field) => field.field_id),
      required_gap_field_count: gapFieldDefinitions.length,
      open_required_gap_field_count: gapFieldDefinitions.length,
      closed_required_gap_field_count: 0,
      reviewer_scope_return_required: true,
      mixed_license_scope_review_required: usesOlp && usesDmoi,
      adaptation_notice_required_if_source_text_used: true,
      allowed_next_step_after_this_check: 'create reviewer-scope blank or exact line-span candidate register without copying source prose',
      blocked_until_closed: [
        'exact excerpt selection',
        'source-prose cache',
        'attribution notice for selected excerpt',
        'local-language surface',
        'bridge or semi-constructed surface',
        'translation draft',
        'publication or pilot readiness claim'
      ],
      row_status: 'open_gap_check_only_no_excerpts_no_source_text_no_surfaces_no_translation'
    };
  });
}

function findDmoiRoute(p111) {
  return p111.route_verification_rows.find((row) => row.source_name === 'Discrete Mathematics: An Open Introduction');
}

function buildArtifact(pointerPacket, p111, olpAttribution, dmoiCatalog) {
  const dmoiRoute = findDmoiRoute(p111);
  const gapRows = buildGapRows(pointerPacket);
  const openGapCells = gapRows.reduce((sum, row) => sum + row.open_required_gap_field_count, 0);
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_attribution_scope_gap_check_no_excerpts_no_source_text_no_surfaces_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Convert package-112 OLP/DMOI source pointers into row-level attribution and scope gaps required before any exact excerpt, source-text capture, local surface, bridge surface, translation, or publication/pilot claim.',
    parent_artifacts: parentArtifacts,
    source_identity_summary: {
      olp_repository: pointerPacket.source_identity.olp_repository,
      olp_inspected_commit: pointerPacket.source_identity.olp_inspected_commit,
      olp_license_class: olpAttribution.source_evidence.license_class,
      olp_license_url: olpAttribution.source_evidence.license_url,
      olp_attribution_name: olpAttribution.source_evidence.source_author_attribution_name,
      dmoi_repo: dmoiCatalog.source_identity.repo,
      dmoi_branch: dmoiCatalog.source_identity.branch,
      dmoi_commit: dmoiCatalog.source_identity.commit,
      dmoi_license_posture_from_route_shelf: dmoiRoute?.license_posture || 'not_found_in_p111_route_shelf',
      dmoi_route_checked: dmoiRoute?.official_routes_checked || [],
      source_identity_systems_pinned: 2,
      license_postures_recorded: 2
    },
    boundary: {
      packet_is: 'attribution and reviewer-scope gap check for future OLP/DMOI relation-function packets',
      packet_is_not: [
        'license legal advice',
        'exact excerpt selection',
        'source-prose cache',
        'translation draft',
        'local-language terminology decision',
        'semi-constructed surface acceptance',
        'publication or pilot readiness claim'
      ],
      allowed_now: [
        'record row-level missing attribution and scope fields',
        'carry source identity and license posture pointers forward',
        'define prerequisites for future line-span and reviewer-scope packets'
      ],
      blocked_now: [
        'copying OLP or DMOI source prose',
        'selecting exact line spans',
        'filling selected-excerpt attribution notices',
        'accepting local or bridge surfaces',
        'translating passages',
        'claiming readiness'
      ]
    },
    gap_field_definitions: gapFieldDefinitions,
    attribution_scope_gap_rows: gapRows,
    gap_totals: {
      rows: gapRows.length,
      required_gap_fields_per_row: gapFieldDefinitions.length,
      open_required_gap_cells: openGapCells,
      closed_required_gap_cells: 0,
      reviewer_scope_returns_required: gapRows.length,
      mixed_license_scope_reviews_required: gapRows.filter((row) => row.mixed_license_scope_review_required).length
    },
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_PACKET_BLANK_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_EXACT_LINE_SPAN_CANDIDATE_REGISTER_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_SELECTED_EXCERPT_ATTRIBUTION_NOTICE_TEMPLATE_<timestamp>'
    ],
    gate_state: {
      attribution_scope_gap_rows: gapRows.length,
      source_pointer_rows_checked: pointerPacket.source_pointer_rows.length,
      source_identity_systems_pinned: 2,
      license_postures_recorded: 2,
      required_gap_fields_per_row: gapFieldDefinitions.length,
      open_required_gap_cells: openGapCells,
      closed_required_gap_cells: 0,
      reviewer_scope_returns_ingested: 0,
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
      attribution_scope_gap_rows_expected: 10,
      required_gap_fields_per_row_expected: 14,
      open_required_gap_cells_expected: 140,
      source_identity_systems_pinned_expected: 2,
      license_postures_recorded_expected: 2,
      zero_gate_assertions: [
        'closed_required_gap_cells',
        'reviewer_scope_returns_ingested',
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
    decision: 'Package 113 is the attribution/scope runway after package 112. It closes no gaps and authorizes no excerpts; it makes the missing selected-excerpt, license-compatibility, reviewer-scope, local-register, and owner-acceptance fields explicit before any construction or translation step.'
  };
}

function buildArtifactMd(artifact) {
  const rows = artifact.attribution_scope_gap_rows.map((row) => `| \`${row.gap_check_row_id}\` | \`${row.parent_pointer_row_id}\` | ${row.packet_unit} | ${row.source_systems_implicated.join(', ')} | \`${row.open_required_gap_field_count}\` |`).join('\n');
  const gateRows = Object.entries(artifact.gate_state).map(([key, value]) => `| ${key} | \`${Array.isArray(value) ? value.length : value}\` |`).join('\n');
  return `# OLP/DMOI Relation-Function Attribution Scope Gap Check

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Boundary

This is an attribution and reviewer-scope gap check only. It is not legal advice, an exact excerpt selection, source-prose cache, selected-excerpt attribution notice, translation draft, local-language surface, semi-constructed surface, publication claim, or pilot claim.

## Gap Rows

| Gap row | Parent pointer | Packet unit | Source systems | Open required gap fields |
| --- | --- | --- | --- | ---: |
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
    'gap_check_row_id',
    'parent_pointer_row_id',
    'packet_unit',
    'olp_shelf_ids',
    'dmoi_catalog_row_ids',
    'source_systems_implicated',
    'olp_routes_available_count',
    'dmoi_file_hints_available_count',
    'required_gap_field_count',
    'open_required_gap_field_count',
    'closed_required_gap_field_count',
    'reviewer_scope_return_required',
    'mixed_license_scope_review_required',
    'row_status'
  ];
  const rows = artifact.attribution_scope_gap_rows.map((row) => columns.map((column) => csvCell(row[column])).join(','));
  return `${columns.join(',')}\n${rows.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    source_artifact: artifact.artifact_id,
    package_order: packageOrder,
    status: 'pointer_only_attribution_scope_gap_check_coordination_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-113 OLP/DMOI attribution-scope gap check continuation while preserving no-excerpt/no-translation boundaries.',
    counts: {
      attribution_scope_gap_rows: g.attribution_scope_gap_rows,
      source_pointer_rows_checked: g.source_pointer_rows_checked,
      required_gap_fields_per_row: g.required_gap_fields_per_row,
      open_required_gap_cells: g.open_required_gap_cells,
      closed_required_gap_cells: g.closed_required_gap_cells,
      source_identity_systems_pinned: g.source_identity_systems_pinned,
      license_postures_recorded: g.license_postures_recorded
    },
    zero_gates: {
      reviewer_scope_returns_ingested: 0,
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
  return `# Package 113 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 113 creates an OLP/DMOI relation-function attribution-scope gap check with \`${g.attribution_scope_gap_rows}\` rows, \`${g.source_pointer_rows_checked}\` source-pointer rows checked, \`${g.required_gap_fields_per_row}\` required gap fields per row, and \`${g.open_required_gap_cells}\` open required gap cells.

Zero gates: \`0\` closed gap cells, \`0\` reviewer returns, \`0\` exact line spans, \`0\` source prose, \`0\` examples, \`0\` excerpts, \`0\` selected-excerpt attribution notices, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Boundary: attribution/scope gap check only. This note makes no commit, push, PR, Zenodo, source-text, translation, publication, pilot, legal-advice, or remote-state claim.
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
      role: 'olp_dmoi_relation_function_attribution_scope_gap_check_support',
      artifact: artifactId,
      current_use: '10 attribution-scope gap rows; 14 required gap fields per row; 140 open required gap cells; 0 closed gaps, 0 line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  packageIndex.obj.current_olp_dmoi_relation_function_attribution_scope_gap_check = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    olp_dmoi_relation_function_attribution_scope_gap_rows: artifact.gate_state.attribution_scope_gap_rows,
    olp_dmoi_relation_function_attribution_open_gap_cells: artifact.gate_state.open_required_gap_cells,
    olp_dmoi_relation_function_attribution_closed_gap_cells: 0,
    olp_dmoi_relation_function_attribution_source_prose_copied: 0,
    olp_dmoi_relation_function_attribution_excerpts_selected: 0,
    olp_dmoi_relation_function_attribution_surfaces_filled: 0,
    olp_dmoi_relation_function_attribution_translations_filled: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_reviewer_scope_blank_or_exact_line_span_candidate_register_only_no_source_text_no_surfaces_no_translation`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function attribution-scope gap check',
    route: artifactId,
    license_status_to_recheck: 'gap_check_only_exact_line_spans_selected_excerpt_attribution_license_compatibility_and_reviewer_scope_required_before_any_adaptation',
    best_translation_use: 'future proof/set/function primer packet gating; records missing attribution, license-compatibility, reviewer-scope, local-register, and owner-acceptance fields before construction',
    candidate_lanes: ['semi_constructed_relation_function_source_request_lane', 'open_source_candidate_catalog', 'attribution_scope_gap_check', 'review_only_construction_scaffold'],
    priority: 1,
    status: 'attribution_scope_gap_check_no_excerpts_no_source_text_no_surfaces_no_translation_no_pilot',
    gate_state: {
      attribution_scope_gap_rows: artifact.gate_state.attribution_scope_gap_rows,
      open_required_gap_cells: artifact.gate_state.open_required_gap_cells,
      closed_required_gap_cells: 0,
      source_prose_copied: 0,
      excerpts_selected: 0,
      translated_passages: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_attribution_scope_gap_check: ${artifactId}_10_rows_140_open_gap_cells_0_closed_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_attribution_scope_gap_check_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_attribution_scope_gap_check_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_attribution_scope_gap_rows: artifact.gate_state.attribution_scope_gap_rows,
    current_olp_dmoi_relation_function_attribution_open_gap_cells: artifact.gate_state.open_required_gap_cells,
    current_olp_dmoi_relation_function_attribution_source_prose_copied: 0,
    current_olp_dmoi_relation_function_attribution_excerpts_selected: 0,
    current_olp_dmoi_relation_function_attribution_translations: 0,
    current_olp_dmoi_relation_function_attribution_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_attribution_scope_gap_check = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_attribution_scope_gap_check: ${artifactId}_gap_check_only_no_excerpts_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_attribution_scope_gap_check = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 10 attribution-scope gap rows over package-112 OLP/DMOI source pointers, 14 required gap fields per row, 140 open required gap cells, 0 closed gaps, 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be queued for upload when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function attribution-scope gap check; 10 rows, 14 required gap fields per row, 140 open required gap cells, 0 closed gaps, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 113: OLP/DMOI relation-function attribution-scope gap check after package 112. It records 10 row-level attribution/scope gaps and 140 open required gap cells while keeping 0 closed gaps, 0 exact line spans, 0 source prose, 0 excerpts, 0 reviewer returns, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function attribution-scope gap check | ${artifactId} | Gap check; 10 rows, 140 open required gap cells, 0 closed, 0 source prose, 0 excerpts, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_attribution_scope_gap_check_artifact: \`${artifactId}\` (10 gap rows; 140 open gap cells; 0 source prose; 0 excerpts; no surfaces, no translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_attribution_scope_gap_check: \`${artifactId}\`; attribution/scope gap check only, no accepted surfaces or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: OLP/DMOI attribution-scope gap check; gaps are not exact excerpt authorization, source text, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_attribution_scope_gap_check' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_attribution_scope_gap_check' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_attribution_scope_gap_check' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package113_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package113_coordination_note' },
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
  upload.obj.package113_upload_queue_update = {
    captured_utc: '2026-07-02T13:47:00Z',
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
  const step = 'Stage package 113 OLP/DMOI relation-function attribution-scope gap-check artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.attribution_scope_gap_rows.length !== 10) failures.push('gap_rows_not_10');
  if (g.source_pointer_rows_checked !== 10) failures.push(`source_pointer_rows_not_10_${g.source_pointer_rows_checked}`);
  if (g.required_gap_fields_per_row !== 14) failures.push(`gap_fields_per_row_not_14_${g.required_gap_fields_per_row}`);
  if (g.open_required_gap_cells !== 140) failures.push(`open_gap_cells_not_140_${g.open_required_gap_cells}`);
  if (g.source_identity_systems_pinned !== 2) failures.push(`source_identity_systems_not_2_${g.source_identity_systems_pinned}`);
  if (g.license_postures_recorded !== 2) failures.push(`license_postures_not_2_${g.license_postures_recorded}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  return failures;
}

const pointerPacket = (await readJson('OLP_DMOI_RELATION_FUNCTION_SOURCE_POINTER_PACKET_20260702T133000Z')).obj;
const p111 = (await readJson('OPEN_RELATION_FUNCTION_TRANSLATION_SOURCE_CANDIDATE_SHELF_20260702T131500Z')).obj;
const olpAttribution = (await readJson('OLP_FIRST_PROOF_PACKET_ATTRIBUTION_FILLED_BLANK_20260630T073304Z')).obj;
const dmoiCatalog = (await readJson('SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_TRANSLATION_CANDIDATE_CATALOG_20260701T180000Z')).obj;

const artifact = buildArtifact(pointerPacket, p111, olpAttribution, dmoiCatalog);
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
  attribution_scope_gap_rows: artifact.gate_state.attribution_scope_gap_rows,
  source_pointer_rows_checked: artifact.gate_state.source_pointer_rows_checked,
  required_gap_fields_per_row: artifact.gate_state.required_gap_fields_per_row,
  open_required_gap_cells: artifact.gate_state.open_required_gap_cells,
  closed_required_gap_cells: artifact.gate_state.closed_required_gap_cells,
  exact_line_spans_selected: artifact.gate_state.exact_line_spans_selected,
  source_prose_copied: artifact.gate_state.source_prose_copied,
  excerpts_selected: artifact.gate_state.excerpts_selected,
  local_language_surfaces_filled: artifact.gate_state.local_language_surfaces_filled,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
