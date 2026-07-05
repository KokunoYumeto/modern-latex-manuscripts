import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OLP_DMOI_RELATION_FUNCTION_SOURCE_POINTER_PACKET_20260702T133000Z';
const noteId = 'OLP_DMOI_RELATION_FUNCTION_SOURCE_POINTER_PACKET_NOTE_20260702T133100Z';
const generatedUtc = '2026-07-02T13:30:00Z';
const noteGeneratedUtc = '2026-07-02T13:31:00Z';
const packageOrder = 112;
const queueCandidateId = 'OTCQ-OLP-DMOI-RELATION-FUNCTION-SOURCE-POINTER-PACKET-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentArtifacts = [
  'OPEN_RELATION_FUNCTION_TRANSLATION_SOURCE_CANDIDATE_SHELF_20260702T131500Z',
  'OLP_PROOF_LITERACY_SOURCE_MINI_SHELF_20260629T175544Z',
  'OLP_FIRST_PROOF_EXCERPT_CANDIDATE_SIDECAR_20260630T215627Z',
  'OLP_FIRST_PROOF_PACKET_ATTRIBUTION_FILLED_BLANK_20260630T073304Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_TRANSLATION_CANDIDATE_CATALOG_20260701T180000Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_SEMANTIC_SLOT_SOURCE_REQUEST_PACKET_20260701T233000Z'
];

const olpShelves = {
  'OLP-METHODS-PROOFS-READING-01': [
    'content/methods/proofs/reading-proofs.tex',
    'content/methods/proofs/starting-proofs.tex',
    'content/methods/proofs/inference-patterns.tex'
  ],
  'OLP-METHODS-USING-DEFINITIONS-01': [
    'content/methods/proofs/using-definitions.tex',
    'content/methods/proofs/example-1.tex',
    'content/methods/proofs/example-2.tex'
  ],
  'OLP-SFR-SETS-BASICS-01': [
    'content/sets-functions-relations/sets/basics.tex',
    'content/sets-functions-relations/sets/subsets.tex',
    'content/sets-functions-relations/sets/proofs-about-sets.tex',
    'content/sets-functions-relations/sets/unions-and-intersections.tex',
    'content/sets-functions-relations/sets/pairs-and-products.tex'
  ],
  'OLP-SFR-FUNCTIONS-BASICS-01': [
    'content/sets-functions-relations/functions/function-basics.tex',
    'content/sets-functions-relations/functions/functions-relations.tex',
    'content/sets-functions-relations/functions/function-kinds.tex',
    'content/sets-functions-relations/functions/composition.tex',
    'content/sets-functions-relations/functions/inverses.tex'
  ],
  'OLP-SFR-RELATIONS-01': [
    'content/sets-functions-relations/relations/relations-as-sets.tex',
    'content/sets-functions-relations/relations/special-properties.tex',
    'content/sets-functions-relations/relations/equivalence-relations.tex',
    'content/sets-functions-relations/relations/orders.tex'
  ],
  'OLP-SFR-SIZE-OF-SETS-01': [
    'content/sets-functions-relations/size-of-sets/equinumerous-sets.tex',
    'content/sets-functions-relations/size-of-sets/comparing-size.tex',
    'content/sets-functions-relations/size-of-sets/enumerability.tex',
    'content/sets-functions-relations/size-of-sets/schroder-bernstein.tex'
  ]
};

const pointerRows = [
  {
    pointer_row_id: 'ODRF-PTR-01',
    packet_unit: 'proof_reading_and_definition_use',
    olp_shelf_ids: ['OLP-METHODS-PROOFS-READING-01', 'OLP-METHODS-USING-DEFINITIONS-01'],
    dmoi_catalog_row_ids: ['DMOI-RF-CAT-01'],
    packet_use: 'orient future relation/function packet around proof reading, unpacking definitions, and relation/function boundary questions',
    next_gate: 'attribution and reviewer-scope sidecar before any excerpt or surface'
  },
  {
    pointer_row_id: 'ODRF-PTR-02',
    packet_unit: 'sets_membership_subset_equality',
    olp_shelf_ids: ['OLP-SFR-SETS-BASICS-01'],
    dmoi_catalog_row_ids: ['DMOI-RF-CAT-01'],
    packet_use: 'pair OLP set basics with DMOI relation/function boundary coordinates before local membership or subset surfaces',
    next_gate: 'local terminology authority return and exact-line sidecar'
  },
  {
    pointer_row_id: 'ODRF-PTR-03',
    packet_unit: 'domain_codomain_range',
    olp_shelf_ids: ['OLP-SFR-FUNCTIONS-BASICS-01'],
    dmoi_catalog_row_ids: ['DMOI-RF-CAT-02', 'DMOI-RF-CAT-06'],
    packet_use: 'source-pointer basis for domain/codomain/range language plus mapping notation and arrow-reading conventions across proof and school-to-university function packets',
    next_gate: 'reviewer route decision and local register split'
  },
  {
    pointer_row_id: 'ODRF-PTR-04',
    packet_unit: 'function_as_relation_boundary',
    olp_shelf_ids: ['OLP-SFR-FUNCTIONS-BASICS-01', 'OLP-SFR-RELATIONS-01'],
    dmoi_catalog_row_ids: ['DMOI-RF-CAT-01'],
    packet_use: 'support the distinction between relation and function without importing any English source prose',
    next_gate: 'scope sidecar deciding whether relation-as-set language belongs in first packet'
  },
  {
    pointer_row_id: 'ODRF-PTR-05',
    packet_unit: 'injective_surjective_bijective',
    olp_shelf_ids: ['OLP-SFR-FUNCTIONS-BASICS-01'],
    dmoi_catalog_row_ids: ['DMOI-RF-CAT-03'],
    packet_use: 'function property source pointers for one-to-one/onto/bijective terminology before any algebra extension',
    next_gate: 'property-family reviewer return'
  },
  {
    pointer_row_id: 'ODRF-PTR-06',
    packet_unit: 'relation_properties',
    olp_shelf_ids: ['OLP-SFR-RELATIONS-01'],
    dmoi_catalog_row_ids: ['DMOI-RF-CAT-07'],
    packet_use: 'reflexive/symmetric/antisymmetric/transitive source pointers for later relation-property packets',
    next_gate: 'relation-property reviewer route and local-standard check'
  },
  {
    pointer_row_id: 'ODRF-PTR-07',
    packet_unit: 'equivalence_order_poset',
    olp_shelf_ids: ['OLP-SFR-RELATIONS-01'],
    dmoi_catalog_row_ids: ['DMOI-RF-CAT-04'],
    packet_use: 'equivalence relation, partial order, and poset source-pointer bridge for quotient/order language',
    next_gate: 'advanced scope decision; not first undercoverage packet by default'
  },
  {
    pointer_row_id: 'ODRF-PTR-08',
    packet_unit: 'composition_inverse',
    olp_shelf_ids: ['OLP-SFR-FUNCTIONS-BASICS-01'],
    dmoi_catalog_row_ids: ['DMOI-RF-CAT-05'],
    packet_use: 'composition and inverse operation pointers for function-operation sidecar',
    next_gate: 'defer unless first packet explicitly includes operation language'
  },
  {
    pointer_row_id: 'ODRF-PTR-09',
    packet_unit: 'finite_infinite_equinumerosity',
    olp_shelf_ids: ['OLP-SFR-SIZE-OF-SETS-01'],
    dmoi_catalog_row_ids: ['DMOI-RF-CAT-03', 'DMOI-RF-CAT-08'],
    packet_use: 'later finite/infinite and same-size-by-bijection source pointers, not first-packet core',
    next_gate: 'separate finite/infinite scope sidecar'
  },
  {
    pointer_row_id: 'ODRF-PTR-10',
    packet_unit: 'high_density_source_shelf_selection',
    olp_shelf_ids: ['OLP-SFR-SETS-BASICS-01', 'OLP-SFR-FUNCTIONS-BASICS-01', 'OLP-SFR-RELATIONS-01'],
    dmoi_catalog_row_ids: ['DMOI-RF-CAT-08'],
    packet_use: 'use high-density DMOI source-file summary rows plus OLP SFR shelves to choose future exact excerpt candidates',
    next_gate: 'source-shelf selection matrix with exact path/line reasons, still no source prose'
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
  return value.split('_').map((part) => (part ? `${part[0].toUpperCase()}${part.slice(1)}` : part)).join(' ');
}

function formatNumber(value) {
  return new Intl.NumberFormat('en-US').format(value);
}

function uniqueFlat(values) {
  return [...new Set(values.flat())];
}

function buildExpandedPointerRows(catalogById) {
  return pointerRows.map((row) => {
    const dmoiRows = row.dmoi_catalog_row_ids.map((id) => catalogById.get(id)).filter(Boolean);
    return {
      ...row,
      olp_source_routes: uniqueFlat(row.olp_shelf_ids.map((id) => olpShelves[id] || [])),
      dmoi_source_file_hints: uniqueFlat(dmoiRows.map((entry) => entry.source_file_hints || [])),
      dmoi_coordinate_rows_available_nonunique_sum: dmoiRows.reduce((sum, entry) => sum + (entry.coordinate_rows_available || 0), 0),
      pointer_status: 'source_pointer_only_no_excerpts_no_source_text_no_surfaces_no_translation'
    };
  });
}

function buildArtifact(p111, olpShelf, olpSidecar, olpAttribution, dmoiCatalog, dmoiFileSummaries) {
  const catalogById = new Map(dmoiCatalog.catalog_rows.map((row) => [row.catalog_row_id, row]));
  const expandedRows = buildExpandedPointerRows(catalogById);
  const olpShelfIds = [...new Set(expandedRows.flatMap((row) => row.olp_shelf_ids))];
  const olpRoutes = [...new Set(expandedRows.flatMap((row) => row.olp_source_routes))];
  const dmoiCatalogIds = [...new Set(expandedRows.flatMap((row) => row.dmoi_catalog_row_ids))];
  const topDmoiFileSummaryRows = dmoiFileSummaries.slice(0, 8);
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'olp_dmoi_relation_function_source_pointer_packet_no_excerpts_no_source_text_no_surfaces_no_translation_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Turn package-111 source-candidate shelf sequence 1 into a concrete OLP plus DMOI relation/function source-pointer packet without copying prose, selecting excerpts, proposing surfaces, or starting translation.',
    parent_artifacts: parentArtifacts,
    source_identity: {
      olp_repository: olpShelf.olp_repository,
      olp_inspected_commit: olpShelf.olp_inspected_commit,
      olp_license_class: olpAttribution.source_evidence.license_class,
      dmoi_repo: dmoiCatalog.source_identity.repo,
      dmoi_branch: dmoiCatalog.source_identity.branch,
      dmoi_commit: dmoiCatalog.source_identity.commit,
      dmoi_coordinate_rows_file: dmoiCatalog.source_identity.coordinate_rows_file,
      dmoi_coordinate_file_summaries_file: dmoiCatalog.source_identity.coordinate_file_summaries_file,
      dmoi_exact_coordinate_rows_total: 1438
    },
    packet_boundary: {
      packet_is: 'source-pointer matrix for future relation/function packet selection',
      packet_is_not: [
        'exact excerpt selection',
        'line-span authorization',
        'source-prose cache',
        'translation draft',
        'local-language surface',
        'constructed or semi-constructed surface',
        'publication or pilot claim'
      ],
      allowed_now: [
        'link OLP shelf IDs and file paths to DMOI catalog rows and file hints',
        'identify future packet units and gate conditions',
        'preserve license/attribution and reviewer gates before any adaptation'
      ],
      blocked_now: [
        'copying OLP or DMOI source prose',
        'selecting exact excerpts',
        'filling attribution notices for selected excerpts',
        'filling local or bridge surfaces',
        'translating passages',
        'claiming readiness'
      ]
    },
    source_pointer_rows: expandedRows,
    olp_source_shelf_summary: {
      shelf_rows_referenced: olpShelfIds.length,
      shelf_ids_referenced: olpShelfIds,
      source_routes_referenced: olpRoutes.length,
      route_paths: olpRoutes
    },
    dmoi_source_shelf_summary: {
      catalog_rows_referenced: dmoiCatalogIds.length,
      catalog_row_ids_referenced: dmoiCatalogIds,
      exact_coordinate_rows_total: 1438,
      top_file_summary_rows_selected: topDmoiFileSummaryRows.length,
      top_file_summary_rows: topDmoiFileSummaryRows
    },
    packet_sequence_position: p111.recommended_packet_sequence.find((row) => row.sequence === 1),
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_SOURCE_POINTER_ATTRIBUTION_GAP_CHECK_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_EXACT_LINE_SPAN_CANDIDATE_REGISTER_<timestamp>',
      'OLP_DMOI_RELATION_FUNCTION_REVIEWER_SCOPE_PACKET_BLANK_<timestamp>',
      'OPENSTAX_FUNCTION_LANGUAGE_BOOK_SPECIFIC_LICENSE_CAPTURE_<timestamp>'
    ],
    gate_state: {
      source_pointer_rows: expandedRows.length,
      olp_shelf_rows_referenced: olpShelfIds.length,
      olp_source_routes_referenced: olpRoutes.length,
      dmoi_catalog_rows_referenced: dmoiCatalogIds.length,
      dmoi_top_file_summary_rows_selected: topDmoiFileSummaryRows.length,
      dmoi_exact_coordinate_rows_total: 1438,
      olp_candidate_rows_selected: 0,
      dmoi_coordinate_rows_selected_for_excerpt: 0,
      exact_line_spans_selected: 0,
      source_prose_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      excerpts_selected: 0,
      attribution_rows_filled_for_selected_excerpts: 0,
      reviewer_returns_ingested: 0,
      local_language_surfaces_filled: 0,
      bridge_surfaces_accepted: 0,
      translated_passages: 0,
      publication_ready: false,
      translation_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    validation_snapshot: {
      package_order_expected: packageOrder,
      source_pointer_rows_expected: 10,
      olp_shelf_rows_referenced_expected: 6,
      olp_source_routes_referenced_expected: 24,
      dmoi_catalog_rows_referenced_expected: 8,
      dmoi_top_file_summary_rows_selected_expected: 8,
      zero_gate_assertions: [
        'olp_candidate_rows_selected',
        'dmoi_coordinate_rows_selected_for_excerpt',
        'exact_line_spans_selected',
        'source_prose_copied',
        'source_examples_copied',
        'source_passages_selected',
        'excerpts_selected',
        'attribution_rows_filled_for_selected_excerpts',
        'reviewer_returns_ingested',
        'local_language_surfaces_filled',
        'bridge_surfaces_accepted',
        'translated_passages'
      ]
    },
    decision: 'Use this as the first concrete OLP plus DMOI source-pointer packet matrix after package 111. It is closer to packet construction than a route catalog, but it still carries no excerpts, source prose, surfaces, translations, publication state, or pilot readiness.'
  };
}

function buildArtifactMd(artifact) {
  const rows = artifact.source_pointer_rows.map((row) => `| \`${row.pointer_row_id}\` | ${row.packet_unit} | ${row.olp_shelf_ids.map((id) => `\`${id}\``).join(', ')} | ${row.dmoi_catalog_row_ids.map((id) => `\`${id}\``).join(', ')} | ${row.next_gate} |`).join('\n');
  const gateRows = Object.entries(artifact.gate_state).map(([key, value]) => `| ${key} | \`${Array.isArray(value) ? value.length : value}\` |`).join('\n');
  return `# OLP/DMOI Relation-Function Source Pointer Packet

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Boundary

This is a source-pointer matrix only. It is not an exact excerpt selection, source-prose cache, attribution notice for selected excerpts, translation draft, local-language surface, bridge-surface decision, publication claim, or pilot claim.

## Pointer Rows

| Row | Packet unit | OLP shelf rows | DMOI catalog rows | Next gate |
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
    'pointer_row_id',
    'packet_unit',
    'olp_shelf_ids',
    'dmoi_catalog_row_ids',
    'olp_source_routes',
    'dmoi_source_file_hints',
    'packet_use',
    'next_gate',
    'pointer_status'
  ];
  const rows = artifact.source_pointer_rows.map((row) => columns.map((column) => csvCell(row[column])).join(','));
  return `${columns.join(',')}\n${rows.join('\n')}\n`;
}

function buildNote(artifact) {
  const g = artifact.gate_state;
  return {
    artifact_id: noteId,
    generated_utc: noteGeneratedUtc,
    source_artifact: artifact.artifact_id,
    package_order: packageOrder,
    status: 'pointer_only_coordination_note_no_upload_claim_no_remote_state_claim',
    purpose: 'Record package-112 OLP/DMOI source-pointer packet continuation while preserving no-excerpt/no-translation boundaries.',
    counts: {
      source_pointer_rows: g.source_pointer_rows,
      olp_shelf_rows_referenced: g.olp_shelf_rows_referenced,
      olp_source_routes_referenced: g.olp_source_routes_referenced,
      dmoi_catalog_rows_referenced: g.dmoi_catalog_rows_referenced,
      dmoi_top_file_summary_rows_selected: g.dmoi_top_file_summary_rows_selected,
      dmoi_exact_coordinate_rows_total: g.dmoi_exact_coordinate_rows_total
    },
    zero_gates: {
      exact_line_spans_selected: 0,
      source_prose_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      excerpts_selected: 0,
      attribution_rows_filled_for_selected_excerpts: 0,
      reviewer_returns_ingested: 0,
      surfaces_filled: 0,
      translated_passages: 0,
      readiness_claims: 0
    },
    no_remote_action_by_this_note: true
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 112 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 112 creates an OLP/DMOI relation-function source-pointer packet with \`${g.source_pointer_rows}\` pointer rows, \`${g.olp_shelf_rows_referenced}\` OLP shelf rows, \`${g.olp_source_routes_referenced}\` OLP source routes, \`${g.dmoi_catalog_rows_referenced}\` DMOI catalog rows, and \`${g.dmoi_top_file_summary_rows_selected}\` DMOI high-density file summary rows.

Zero gates: \`0\` exact line spans, \`0\` source prose, \`0\` examples, \`0\` excerpts, \`0\` attribution rows for selected excerpts, \`0\` reviewer returns, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Boundary: source-pointer packet only. This note makes no commit, push, PR, Zenodo, source-text, translation, publication, pilot, or remote-state claim.
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
      role: 'olp_dmoi_relation_function_source_pointer_packet_support',
      artifact: artifactId,
      current_use: '10 OLP/DMOI source-pointer rows; 6 OLP shelf rows, 24 OLP source routes, 8 DMOI catalog rows, 8 DMOI file summary rows; 0 line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  packageIndex.obj.current_olp_dmoi_relation_function_source_pointer_packet = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    olp_dmoi_relation_function_source_pointer_rows: artifact.gate_state.source_pointer_rows,
    olp_dmoi_relation_function_olp_source_routes: artifact.gate_state.olp_source_routes_referenced,
    olp_dmoi_relation_function_dmoi_catalog_rows: artifact.gate_state.dmoi_catalog_rows_referenced,
    olp_dmoi_relation_function_source_prose_copied: 0,
    olp_dmoi_relation_function_excerpts_selected: 0,
    olp_dmoi_relation_function_surfaces_filled: 0,
    olp_dmoi_relation_function_translations_filled: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_attribution_gap_check_or_exact_line_span_candidate_register_only_no_source_text_no_surfaces_no_translation`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'OLP/DMOI relation-function source pointer packet',
    route: artifactId,
    license_status_to_recheck: 'source_pointer_packet_only_exact_line_spans_attribution_and_license_compatibility_required_before_adaptation_no_source_prose_no_excerpts_no_translation',
    best_translation_use: 'future proof/set/function primer packet selection linking OLP source shelves to DMOI relation/function coordinate shelves',
    candidate_lanes: ['semi_constructed_relation_function_source_request_lane', 'open_source_candidate_catalog', 'source_pointer_packet', 'review_only_construction_scaffold'],
    priority: 1,
    status: 'source_pointer_packet_no_excerpts_no_source_text_no_surfaces_no_translation_no_pilot',
    gate_state: {
      source_pointer_rows: artifact.gate_state.source_pointer_rows,
      olp_source_routes_referenced: artifact.gate_state.olp_source_routes_referenced,
      dmoi_catalog_rows_referenced: artifact.gate_state.dmoi_catalog_rows_referenced,
      source_prose_copied: 0,
      excerpts_selected: 0,
      translated_passages: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_source_pointer_packet: ${artifactId}_10_rows_24_olp_routes_8_dmoi_catalog_rows_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_olp_dmoi_relation_function_source_pointer_packet_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_olp_dmoi_relation_function_source_pointer_packet_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_olp_dmoi_relation_function_source_pointer_rows: artifact.gate_state.source_pointer_rows,
    current_olp_dmoi_relation_function_source_prose_copied: 0,
    current_olp_dmoi_relation_function_excerpts_selected: 0,
    current_olp_dmoi_relation_function_translations: 0,
    current_olp_dmoi_relation_function_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_olp_dmoi_relation_function_source_pointer_packet = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_olp_dmoi_relation_function_source_pointer_packet: ${artifactId}_source_pointer_only_no_excerpts_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_olp_dmoi_relation_function_source_pointer_packet = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: creates 10 OLP/DMOI source-pointer rows linking 6 OLP shelf rows, 24 OLP source routes, 8 DMOI catalog rows, and 8 DMOI high-density file summary rows; 0 exact line spans, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be queued for upload when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - OLP/DMOI relation-function source-pointer packet; 10 pointer rows, 6 OLP shelf rows, 24 OLP source routes, 8 DMOI catalog rows, 8 DMOI file summary rows, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 112: OLP/DMOI relation-function source-pointer packet after package 111. It links OLP proof/set/function shelves to DMOI relation/function coordinate shelves while keeping 0 exact line spans, 0 source prose, 0 excerpts, 0 reviewer returns, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | OLP/DMOI relation-function source pointer packet | ${artifactId} | Source-pointer packet; 10 rows, 24 OLP routes, 8 DMOI catalog rows, 0 source prose, 0 excerpts, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_olp_dmoi_relation_function_source_pointer_packet_artifact: \`${artifactId}\` (10 source-pointer rows; 0 source prose; 0 excerpts; no surfaces, no translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_olp_dmoi_relation_function_source_pointer_packet: \`${artifactId}\`; source-pointer packet only, no accepted surfaces or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: first concrete OLP/DMOI relation-function source-pointer packet; pointers are not exact excerpt authorization, source text, surfaces, translations, or readiness.`);
}

async function rebuildUploadQueueMd(queue) {
  const rows = queue.queued_items.map((item) => `| \`${item.filename}\` | ${titleClass(item.class)} | ${formatNumber(item.bytes)} | \`${item.sha256}\` |`).join('\n');
  const md = `# NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702

Status: local post-manifest upload queue, not a remote sync, commit, push, PR update, Zenodo action, or completion claim.

## Purpose

This queue preserves new coordination and translation-access artifacts created after the current indexed payload manifest. The indexed payload still lives at:

\`${queue.relationship_to_indexed_payload.indexed_payload_manifest}\`

Substantive artifacts are queued for upload when a valid checkout/staging path exists; mobile-plan or bandwidth wording should not suppress them.

## Queue Summary

- Queued files: \`${queue.summary.queued_files}\`
- Queued bytes: \`${formatNumber(queue.summary.queued_bytes)}\`
- Raw token files: \`${queue.summary.raw_token_files}\`
- Source PDF/image files: \`${queue.summary.source_pdf_files + queue.summary.source_image_files}\`
- Source excerpt/source-text files: \`${queue.summary.source_text_or_excerpt_files}\`
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
    { filename: `${artifactId}.json`, class: 'olp_dmoi_relation_function_source_pointer_packet' },
    { filename: `${artifactId}.md`, class: 'olp_dmoi_relation_function_source_pointer_packet' },
    { filename: `${artifactId}.csv`, class: 'olp_dmoi_relation_function_source_pointer_packet' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'olp_dmoi_relation_function_package112_coordination_note' },
    { filename: `${noteId}.md`, class: 'olp_dmoi_relation_function_package112_coordination_note' },
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
  upload.obj.package112_upload_queue_update = {
    captured_utc: '2026-07-02T13:32:00Z',
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
  const step = 'Stage package 112 OLP/DMOI relation-function source-pointer packet artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.source_pointer_rows.length !== 10) failures.push('pointer_rows_not_10');
  if (g.olp_shelf_rows_referenced !== 6) failures.push(`olp_shelf_rows_not_6_${g.olp_shelf_rows_referenced}`);
  if (g.olp_source_routes_referenced !== 24) failures.push(`olp_routes_not_24_${g.olp_source_routes_referenced}`);
  if (g.dmoi_catalog_rows_referenced !== 8) failures.push(`dmoi_catalog_rows_not_8_${g.dmoi_catalog_rows_referenced}`);
  if (g.dmoi_top_file_summary_rows_selected !== 8) failures.push(`dmoi_summary_rows_not_8_${g.dmoi_top_file_summary_rows_selected}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  return failures;
}

const p111 = (await readJson('OPEN_RELATION_FUNCTION_TRANSLATION_SOURCE_CANDIDATE_SHELF_20260702T131500Z')).obj;
const olpShelf = (await readJson('OLP_PROOF_LITERACY_SOURCE_MINI_SHELF_20260629T175544Z')).obj;
const olpSidecar = (await readJson('OLP_FIRST_PROOF_EXCERPT_CANDIDATE_SIDECAR_20260630T215627Z')).obj;
const olpAttribution = (await readJson('OLP_FIRST_PROOF_PACKET_ATTRIBUTION_FILLED_BLANK_20260630T073304Z')).obj;
const dmoiCatalog = (await readJson('SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_TRANSLATION_CANDIDATE_CATALOG_20260701T180000Z')).obj;
const dmoiFileSummaries = parseJson(await readFile(path.join(outputs, 'source_cache/dmoi_exact_edition_license_20260630T070010Z/edition_source_82336dc87d77c3f18d2cdbc8ec1e74eb3ba38799/relation_function_coordinate_file_summaries_20260701T151500Z.json'), 'utf8'));

const artifact = buildArtifact(p111, olpShelf, olpSidecar, olpAttribution, dmoiCatalog, dmoiFileSummaries);
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
  source_pointer_rows: artifact.gate_state.source_pointer_rows,
  olp_shelf_rows_referenced: artifact.gate_state.olp_shelf_rows_referenced,
  olp_source_routes_referenced: artifact.gate_state.olp_source_routes_referenced,
  dmoi_catalog_rows_referenced: artifact.gate_state.dmoi_catalog_rows_referenced,
  dmoi_top_file_summary_rows_selected: artifact.gate_state.dmoi_top_file_summary_rows_selected,
  source_prose_copied: artifact.gate_state.source_prose_copied,
  excerpts_selected: artifact.gate_state.excerpts_selected,
  local_language_surfaces_filled: artifact.gate_state.local_language_surfaces_filled,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
