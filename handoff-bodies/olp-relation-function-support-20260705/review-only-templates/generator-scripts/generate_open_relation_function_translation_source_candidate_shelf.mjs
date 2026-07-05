import { readFile, writeFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_RELATION_FUNCTION_TRANSLATION_SOURCE_CANDIDATE_SHELF_20260702T131500Z';
const noteId = 'OPEN_RELATION_FUNCTION_SOURCE_CANDIDATE_SHELF_NOTE_20260702T131600Z';
const generatedUtc = '2026-07-02T13:15:00Z';
const noteGeneratedUtc = '2026-07-02T13:16:00Z';
const packageOrder = 111;
const queueCandidateId = 'OTCQ-OPEN-RELATION-FUNCTION-SOURCE-CANDIDATE-SHELF-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentArtifacts = [
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_BEYOND_CORE_TRANSLATION_CANDIDATE_CATALOG_20260701T180000Z',
  'OPEN_TRANSLATION_SOURCE_LICENSE_PACKET_MATCH_AUDIT_20260629T175128Z',
  'OPEN_MATH_TRANSLATION_CANDIDATE_EXPANSION_20260630T064921Z',
  'OPEN_MATH_SOURCE_LICENSE_COMPATIBILITY_MATRIX_20260630T072532Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_P110_RESOLUTION_RETURN_EVIDENCE_INTAKE_LEDGER_TEMPLATE_20260702T130000Z'
];

const sourceRows = [
  {
    row_id: 'ORF-SRC-01',
    source_name: 'Open Logic Project / Open Logic Text',
    official_routes_checked: [
      'https://openlogicproject.org/olp-license/',
      'https://openlogicproject.org/download/',
      'https://github.com/OpenLogicProject/OpenLogic/'
    ],
    live_route_evidence_summary: 'official pages and repository identify OLP/Open Logic Text material as Creative Commons Attribution 4.0 / CC BY 4.0, with attribution required',
    license_posture: 'CC_BY_4_0_route_verified_exact_file_and_attribution_rows_still_required',
    relation_function_use: 'proof-literacy, set/function preliminaries, relations, definitions, theorem/proof reading, symbolic-language scaffolding',
    best_packet_role: 'first proof and set/function primer source shelf before local reviewer surfaces',
    target_lane_fit: ['proof_literacy_micro_packet', 'Malay_Indonesian_relation_function', 'Pan_Romance_review_only', 'UC12_source_bridge', 'signed_language_source_script_support'],
    priority_hint: 1,
    allowed_next_step: 'exact-file attribution sidecar or source-pointer packet; no excerpt adaptation until attribution and reviewer gates are filled',
    blocked_now: ['copying source prose', 'selecting excerpts', 'translation drafting', 'accepting bridge/local surfaces', 'pilot claim']
  },
  {
    row_id: 'ORF-SRC-02',
    source_name: 'Discrete Mathematics: An Open Introduction',
    official_routes_checked: [
      'https://discrete.openmathbooks.org/',
      'local:DMOI_EXACT_EDITION_AND_LICENSE_CAPTURE_20260630T070010Z',
      'local:DMOI_LICENSE_RECONCILIATION_AND_ATTRIBUTION_SIDECAR_20260630T070542Z'
    ],
    live_route_evidence_summary: 'current official route describes the textbook as free/open source and Creative Commons with a NonCommercial addition; local exact-edition artifacts already pin the DMOI relation/function source shelf',
    license_posture: 'conservative_CC_BY_NC_SA_style_until_exact_edition_license_reconciliation_rows_are_rechecked',
    relation_function_use: 'direct relation/function source shelf: domain, codomain, relation properties, equivalence relations, order relations, composition, inverse language',
    best_packet_role: 'discrete relation/function packet shelf after license reconciliation and reviewer returns',
    target_lane_fit: ['Malay_Indonesian_relation_function', 'Pan_Romance_discrete_math', 'Maori_Hawaiian_review_only', 'UC12_discrete_structures'],
    priority_hint: 1,
    allowed_next_step: 'source-pointer shelf or reviewer route packet using existing exact coordinates; no excerpt selection until license and attribution rows are closed',
    blocked_now: ['source prose copying', 'exercise/example adaptation', 'translation drafting', 'surface acceptance', 'pilot claim']
  },
  {
    row_id: 'ORF-SRC-03',
    source_name: 'OpenStax Precalculus 2e',
    official_routes_checked: [
      'https://openstax.org/books/precalculus-2e/pages/preface',
      'https://openstax.org/details/books/precalculus-2e'
    ],
    live_route_evidence_summary: 'official OpenStax preface identifies Precalculus 2e as CC BY-NC-SA 4.0 and suitable for redistribution/remix under attribution, noncommercial, and share-alike terms',
    license_posture: 'CC_BY_NC_SA_4_0_route_verified_book_specific_edition_capture_required',
    relation_function_use: 'function families, graphs, transformations, inverse functions, composition, modeling language before calculus',
    best_packet_role: 'function-reading and modeling-language shelf for broad access lanes after book-specific attribution capture',
    target_lane_fit: ['Malay_Indonesian_function_language', 'Pan_Romance_calculus_bridge', 'Arabic_Persianate_after_review', 'Pacific_numeracy_to_functions'],
    priority_hint: 2,
    allowed_next_step: 'book-specific license/edition capture and function-chapter source-pointer sidecar',
    blocked_now: ['commercial reuse planning', 'mixing into CC_BY packets without compatibility note', 'source prose copying', 'translation drafting', 'pilot claim']
  },
  {
    row_id: 'ORF-SRC-04',
    source_name: 'OpenStax Algebra and Trigonometry 2e',
    official_routes_checked: [
      'https://openstax.org/books/algebra-and-trigonometry-2e/pages/preface',
      'https://openstax.org/details/books/algebra-and-trigonometry-2e'
    ],
    live_route_evidence_summary: 'official OpenStax preface identifies Algebra and Trigonometry 2e as CC BY-NC-SA 4.0 with attribution, noncommercial, and share-alike constraints',
    license_posture: 'CC_BY_NC_SA_4_0_route_verified_book_specific_edition_capture_required',
    relation_function_use: 'introductory function vocabulary, equations as relations, transformations, inverse/composition, symbolic reading practice',
    best_packet_role: 'early algebra/function bridge shelf for lanes needing school-to-undergraduate transition material',
    target_lane_fit: ['Malay_Indonesian_school_to_university_bridge', 'Pan_Romance_function_bridge', 'West_African_STEM_access', 'Horn_Cushitic_STEM_access'],
    priority_hint: 2,
    allowed_next_step: 'book-specific function unit source-pointer sidecar with NC-SA warning',
    blocked_now: ['source prose copying', 'unmixed CC_BY reuse assumption', 'translation drafting', 'surface acceptance', 'pilot claim']
  },
  {
    row_id: 'ORF-SRC-05',
    source_name: 'A First Course in Linear Algebra',
    official_routes_checked: [
      'https://github.com/rbeezer/fcla',
      'local:FCLA_GFDL_COMPATIBILITY_AND_EXACT_COMMIT_SIDECAR_20260630T070951Z'
    ],
    live_route_evidence_summary: 'official repository describes FCLA as a free open-source introductory linear algebra textbook with a GFDL license; local sidecar records exact-commit compatibility evidence',
    license_posture: 'GFDL_1_2_or_later_family_exact_commit_sidecar_exists_GFDL_packet_separation_required',
    relation_function_use: 'linear transformations as functions, matrices as maps, domain/codomain analogues, basis/dimension language',
    best_packet_role: 'linear-map and vector-space relation/function extension shelf, separate from CC packets unless compatibility is reviewed',
    target_lane_fit: ['Pan_Romance_linear_algebra', 'Malay_Indonesian_linear_map_terms', 'UC12_source_slot_planning', 'Noether_adjacent_linear_language'],
    priority_hint: 2,
    allowed_next_step: 'GFDL-only source-pointer packet or compatibility table before any mixed-source adaptation',
    blocked_now: ['mixing into CC_BY_NC_SA packet without GFDL table', 'source prose copying', 'translation drafting', 'surface acceptance', 'pilot claim']
  },
  {
    row_id: 'ORF-SRC-06',
    source_name: 'Abstract Algebra: Theory and Applications',
    official_routes_checked: [
      'https://github.com/twjudson/aata',
      'https://judsonbooks.org/abstract-algebra-theory-and-applications/',
      'local:AATA_GFDL_COMPATIBILITY_AND_EXACT_COMMIT_SIDECAR_20260630T071615Z'
    ],
    live_route_evidence_summary: 'official repository describes AATA as GFDL-licensed source covering groups, rings, fields, and more; the book site describes group theory through rings, integral domains, vector spaces, fields, and Galois theory',
    license_posture: 'GFDL_1_3_or_later_family_exact_commit_sidecar_exists_GFDL_packet_separation_required',
    relation_function_use: 'homomorphism, quotient, kernel/image, isomorphism, operations, rings/fields/ideals as higher relation/function vocabulary',
    best_packet_role: 'abstract algebra extension shelf after relation/function core and linear-map language stabilize',
    target_lane_fit: ['Noether_adjacent_algebra', 'Pan_Romance_abstract_algebra', 'Malay_Indonesian_higher_algebra', 'Arabic_Persianate_after_review', 'Pan_Turkic_after_review'],
    priority_hint: 3,
    allowed_next_step: 'GFDL-only algebra source-pointer packet or FCLA/AATA compatibility table',
    blocked_now: ['early undercoverage sprint use', 'mixed-license adaptation without review', 'source prose copying', 'translation drafting', 'pilot claim']
  },
  {
    row_id: 'ORF-SRC-07',
    source_name: 'OpenIntro Statistics resources',
    official_routes_checked: [
      'https://www.openintro.org/license/',
      'https://github.com/OpenIntroStat/openintro-statistics/blob/master/LICENSE.md'
    ],
    live_route_evidence_summary: 'official OpenIntro license page says most resources including Statistics textbooks are CC BY-SA 3.0; repository license route confirms OpenIntro Statistics under CC BY-SA 3.0',
    license_posture: 'CC_BY_SA_3_0_route_verified_sharealike_packet_plan_required',
    relation_function_use: 'data-to-model language, variables, tables/graphs, functions as quantitative relationships, public-service numeracy bridge',
    best_packet_role: 'numeracy-to-function bridge for public-service translation lanes, separate from pure proof packets',
    target_lane_fit: ['creole_contact_public_service', 'West_African_STEM_access', 'Horn_Cushitic_STEM_access', 'Pacific_numeracy'],
    priority_hint: 3,
    allowed_next_step: 'share-alike attribution plan and local numeracy reviewer packet',
    blocked_now: ['mixing with incompatible license packets', 'source prose copying', 'translation drafting', 'surface acceptance', 'pilot claim']
  },
  {
    row_id: 'ORF-SRC-08',
    source_name: 'Stacks Project',
    official_routes_checked: [
      'https://stacks.math.columbia.edu/',
      'https://stacks.math.columbia.edu/browse',
      'https://github.com/stacks/stacks-project/blob/master/COPYING'
    ],
    live_route_evidence_summary: 'official project page identifies Stacks as an open-source textbook/reference in algebraic geometry; table of contents includes a GNU Free Documentation License chapter; repository COPYING carries the GFDL text',
    license_posture: 'GFDL_style_route_verified_advanced_reference_only_exact_chapter_license_capture_required',
    relation_function_use: 'advanced reference for morphism, fiber product, sheaf, scheme, stack language; not a starter relation/function packet',
    best_packet_role: 'advanced comparator/reference shelf for Noether-adjacent algebraic geometry terminology after domain-review return',
    target_lane_fit: ['Noether_advanced_reference', 'Pan_Romance_advanced', 'Malay_Indonesian_advanced', 'Arabic_Persianate_advanced_after_review'],
    priority_hint: 4,
    allowed_next_step: 'advanced-reference sidecar and exact chapter/license capture only',
    blocked_now: ['starter classroom packet use', 'source prose copying', 'translation drafting', 'surface acceptance', 'pilot claim']
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

function buildArtifact() {
  return {
    artifact_id: artifactId,
    generated_utc: generatedUtc,
    status: 'open_relation_function_translation_source_candidate_shelf_route_verified_no_excerpts_no_translation_no_surfaces_no_pilot',
    pilot_ready_claim: false,
    translation_ready_claim: false,
    publication_ready_claim: false,
    constructed_surface_ready_claim: false,
    purpose: 'Extend the translation-access project with a live route-verified open-source candidate shelf for relation/function and adjacent technical-language packets beyond the current DMOI core.',
    parent_artifacts: parentArtifacts,
    catalog_boundary: {
      catalog_is: 'route-level source candidate shelf and packet-fit map',
      catalog_is_not: [
        'exact excerpt selection',
        'source-prose cache',
        'translation draft',
        'accepted local-language term list',
        'accepted constructed or semi-constructed surface',
        'license legal opinion',
        'publication or pilot claim'
      ],
      allowed_now: [
        'record official source routes and license posture',
        'rank packet fit for future source-aware translation work',
        'identify required license/attribution/reviewer gates',
        'queue substantive catalog artifacts when a staging path exists'
      ],
      blocked_now: [
        'copying source prose or examples',
        'selecting exact excerpts',
        'filling local-language or bridge surfaces',
        'declaring translation, publication, or pilot readiness'
      ]
    },
    route_verification_rows: sourceRows,
    recommended_packet_sequence: [
      {
        sequence: 1,
        packet_family: 'proof_and_set_function_primer',
        primary_source_rows: ['ORF-SRC-01', 'ORF-SRC-02'],
        why_now: 'best fit for relation/function literacy with existing local DMOI coordinates and OLP source-pointer machinery',
        required_next_artifact: 'exact-file attribution sidecar or source-pointer shelf; reviewer surfaces remain blank'
      },
      {
        sequence: 2,
        packet_family: 'function_language_school_to_undergraduate_bridge',
        primary_source_rows: ['ORF-SRC-03', 'ORF-SRC-04'],
        why_now: 'broad function vocabulary and graph/model language useful across large target lanes',
        required_next_artifact: 'OpenStax book-specific edition/license capture with NC-SA compatibility note'
      },
      {
        sequence: 3,
        packet_family: 'linear_map_and_abstract_algebra_extension',
        primary_source_rows: ['ORF-SRC-05', 'ORF-SRC-06'],
        why_now: 'connects function/relation language to Noether-adjacent algebra after core packet stabilization',
        required_next_artifact: 'GFDL-only packet plan or FCLA/AATA compatibility table'
      },
      {
        sequence: 4,
        packet_family: 'public_numeracy_to_function_bridge',
        primary_source_rows: ['ORF-SRC-07'],
        why_now: 'useful for public-service translation lanes where functions appear as data/model relationships',
        required_next_artifact: 'share-alike attribution plan and local numeracy reviewer packet'
      },
      {
        sequence: 5,
        packet_family: 'advanced_noether_reference',
        primary_source_rows: ['ORF-SRC-08'],
        why_now: 'valuable advanced terminology comparator only after domain-review gating',
        required_next_artifact: 'advanced-reference sidecar and exact chapter/license capture'
      }
    ],
    gate_state: {
      route_verification_rows: sourceRows.length,
      official_routes_checked: sourceRows.reduce((sum, row) => sum + row.official_routes_checked.filter((route) => route.startsWith('http')).length, 0),
      local_evidence_artifacts_referenced: sourceRows.reduce((sum, row) => sum + row.official_routes_checked.filter((route) => route.startsWith('local:')).length, 0),
      packet_sequence_rows: 5,
      exact_editions_captured_by_this_artifact: 0,
      source_files_cached_by_this_artifact: 0,
      source_prose_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      excerpts_selected: 0,
      attribution_rows_filled: 0,
      reviewer_returns_ingested: 0,
      local_language_surfaces_filled: 0,
      bridge_surfaces_accepted: 0,
      translated_passages: 0,
      publication_ready: false,
      translation_ready: false,
      constructed_surface_ready: false,
      pilot_ready: false
    },
    next_valid_artifacts: [
      'OLP_DMOI_RELATION_FUNCTION_SOURCE_POINTER_PACKET_<timestamp>',
      'OPENSTAX_FUNCTION_LANGUAGE_BOOK_SPECIFIC_LICENSE_CAPTURE_<timestamp>',
      'FCLA_AATA_GFDL_RELATION_FUNCTION_EXTENSION_PACKET_PLAN_<timestamp>',
      'OPENINTRO_NUMERACY_TO_FUNCTION_SHAREALIKE_PACKET_PLAN_<timestamp>',
      'STACKS_ADVANCED_REFERENCE_SIDECAR_<timestamp>'
    ],
    decision: 'Use this shelf to choose future translation candidates beyond core notes. It verifies routes and packet fit only; it does not select excerpts, copy source text, create surfaces, translate, publish, or claim pilot readiness.'
  };
}

function buildArtifactMd(artifact) {
  const rows = artifact.route_verification_rows.map((row) => `| \`${row.row_id}\` | ${row.source_name} | ${row.license_posture} | ${row.priority_hint} | ${row.best_packet_role} |`).join('\n');
  const sequenceRows = artifact.recommended_packet_sequence.map((row) => `| ${row.sequence} | ${row.packet_family} | ${row.primary_source_rows.map((id) => `\`${id}\``).join(', ')} | ${row.required_next_artifact} |`).join('\n');
  const gateRows = Object.entries(artifact.gate_state).map(([key, value]) => `| ${key} | \`${value}\` |`).join('\n');
  return `# Open Relation/Function Translation Source Candidate Shelf

Artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Boundary

This is a route-level source candidate shelf. It is not an excerpt selection, source-prose cache, translation draft, accepted local-language surface, accepted bridge surface, publication claim, or pilot claim.

## Source Rows

| Row | Source | License posture | Priority | Best packet role |
| --- | --- | --- | ---: | --- |
${rows}

## Recommended Packet Sequence

| Sequence | Packet family | Source rows | Required next artifact |
| ---: | --- | --- | --- |
${sequenceRows}

## Gate State

| Gate | State |
| --- | ---: |
${gateRows}

Decision: ${artifact.decision}
`;
}

function buildArtifactCsv(artifact) {
  const columns = [
    'row_id',
    'source_name',
    'official_routes_checked',
    'license_posture',
    'relation_function_use',
    'best_packet_role',
    'target_lane_fit',
    'priority_hint',
    'allowed_next_step'
  ];
  const rows = artifact.route_verification_rows.map((row) => columns.map((column) => csvCell(row[column])).join(','));
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
    purpose: 'Record package-111 source-candidate shelf continuation for sibling sessions while preserving no-excerpt/no-translation boundaries.',
    counts: {
      route_verification_rows: g.route_verification_rows,
      official_routes_checked: g.official_routes_checked,
      local_evidence_artifacts_referenced: g.local_evidence_artifacts_referenced,
      packet_sequence_rows: g.packet_sequence_rows
    },
    zero_gates: {
      exact_editions_captured_by_this_artifact: 0,
      source_files_cached_by_this_artifact: 0,
      source_prose_copied: 0,
      source_examples_copied: 0,
      source_passages_selected: 0,
      excerpts_selected: 0,
      attribution_rows_filled: 0,
      reviewer_returns_ingested: 0,
      local_language_surfaces_filled: 0,
      bridge_surfaces_accepted: 0,
      translated_passages: 0,
      readiness_claims: 0
    },
    boundary: 'Use as a route-level open-source candidate shelf only. Do not import source prose, excerpts, translations, surfaces, or readiness claims into sibling decisions.',
    no_remote_action_by_this_note: true
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 111 Coordination Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only update: package 111 adds a route-level open relation/function source candidate shelf with \`${g.route_verification_rows}\` source rows, \`${g.official_routes_checked}\` official web routes checked, and \`${g.local_evidence_artifacts_referenced}\` local evidence artifacts referenced.

Zero gates: \`0\` exact editions captured by this artifact, \`0\` source files cached by this artifact, \`0\` source prose, \`0\` examples, \`0\` excerpts, \`0\` attribution rows filled, \`0\` reviewer returns, \`0\` surfaces, \`0\` translations, \`0\` readiness claims.

Boundary: route-level candidate shelf only. This note makes no commit, push, PR, Zenodo, source-text, translation, publication, pilot, or remote-state claim.
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
      role: 'open_relation_function_translation_source_candidate_shelf_support',
      artifact: artifactId,
      current_use: '8 route-level open source candidate rows, 16 official routes checked, 4 local evidence artifacts referenced; 0 exact editions captured by this artifact, 0 source prose, 0 excerpts, 0 surfaces, 0 translation, 0 readiness'
    });
  }
  packageIndex.obj.current_open_relation_function_translation_source_candidate_shelf = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    open_relation_function_translation_source_candidate_shelf_rows: artifact.gate_state.route_verification_rows,
    open_relation_function_translation_source_candidate_shelf_official_routes_checked: artifact.gate_state.official_routes_checked,
    open_relation_function_translation_source_candidate_shelf_local_evidence_referenced: artifact.gate_state.local_evidence_artifacts_referenced,
    open_relation_function_translation_source_candidate_shelf_source_prose_copied: 0,
    open_relation_function_translation_source_candidate_shelf_excerpts_selected: 0,
    open_relation_function_translation_source_candidate_shelf_surfaces_filled: 0,
    open_relation_function_translation_source_candidate_shelf_translations_filled: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_source_pointer_or_license_capture_only_no_excerpts_no_source_text_no_surfaces_no_translation`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open relation/function translation source candidate shelf',
    route: artifactId,
    license_status_to_recheck: 'route_level_candidate_shelf_only_recheck_exact_book_file_license_before_adaptation_no_source_prose_no_excerpts_no_translation',
    best_translation_use: 'future source-aware candidate selection for relation/function, function-language bridge, linear-map, abstract algebra, public numeracy-to-function, and advanced Noether-adjacent reference packets',
    candidate_lanes: ['semi_constructed_relation_function_source_request_lane', 'open_source_candidate_catalog', 'license_attribution_planning', 'review_only_construction_scaffold'],
    priority: 1,
    status: 'source_candidate_shelf_no_excerpts_no_source_text_no_surfaces_no_translation_no_pilot',
    gate_state: {
      route_verification_rows: artifact.gate_state.route_verification_rows,
      official_routes_checked: artifact.gate_state.official_routes_checked,
      source_prose_copied: 0,
      excerpts_selected: 0,
      translated_passages: 0,
      translation_ready_claim: false,
      pilot_ready_claim: false,
      publication_ready_claim: false
    }
  });
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_relation_function_translation_source_candidate_shelf: ${artifactId}_8_rows_16_routes_0_excerpts_0_translation_upload_when_path_exists`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_relation_function_translation_source_candidate_shelf_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_relation_function_translation_source_candidate_shelf_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_open_relation_function_source_candidate_rows: artifact.gate_state.route_verification_rows,
    current_open_relation_function_source_candidate_source_prose_copied: 0,
    current_open_relation_function_source_candidate_excerpts_selected: 0,
    current_open_relation_function_source_candidate_translations: 0,
    current_open_relation_function_source_candidate_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_relation_function_translation_source_candidate_shelf = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_relation_function_translation_source_candidate_shelf: ${artifactId}_route_level_only_no_excerpts_no_surfaces_no_translation`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_relation_function_translation_source_candidate_shelf = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: adds 8 route-level open source candidate rows for relation/function translation-access work; OLP/DMOI/OpenStax/FCLA/AATA/OpenIntro/Stacks roles recorded; 0 source prose, 0 excerpts, 0 attribution rows filled, 0 surfaces, 0 translations, 0 readiness; substantive artifacts should be queued for upload when a staging path exists.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - route-level open relation/function translation source candidate shelf; 8 source rows, 16 official routes checked, 4 local evidence artifacts referenced, 0 source prose, 0 excerpts, 0 surfaces, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 111: open relation/function translation source candidate shelf. It records 8 route-level source candidates and 5 packet-sequence rows while keeping 0 source prose, 0 excerpts, 0 reviewer returns, 0 surfaces, 0 translations, and all readiness gates closed.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open relation/function translation source candidate shelf | ${artifactId} | Route-level source candidate shelf; 8 source rows, 16 official routes checked, 0 source prose, 0 excerpts, no surface, no translation. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_relation_function_translation_source_candidate_shelf_artifact: \`${artifactId}\` (8 route-level source rows; 0 source prose; 0 excerpts; no surfaces, no translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_relation_function_translation_source_candidate_shelf: \`${artifactId}\`; route-level candidate shelf only, no accepted surfaces or translation.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: preserves a beyond-core source candidate shelf for relation/function translation-access work; route checks are not exact excerpt authorization, source text, surfaces, translations, or readiness.`);
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
    { filename: `${artifactId}.json`, class: 'open_relation_function_translation_source_candidate_shelf' },
    { filename: `${artifactId}.md`, class: 'open_relation_function_translation_source_candidate_shelf' },
    { filename: `${artifactId}.csv`, class: 'open_relation_function_translation_source_candidate_shelf' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_relation_function_package111_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_relation_function_package111_coordination_note' },
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
  upload.obj.package111_upload_queue_update = {
    captured_utc: '2026-07-02T13:17:00Z',
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
  const step = 'Stage package 111 open relation/function source-candidate shelf artifacts with this queue as substantive coordination material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.route_verification_rows.length !== 8) failures.push('source_rows_not_8');
  if (artifact.recommended_packet_sequence.length !== 5) failures.push('packet_sequence_not_5');
  if (g.official_routes_checked !== 16) failures.push(`official_routes_checked_not_16_${g.official_routes_checked}`);
  if (g.local_evidence_artifacts_referenced !== 4) failures.push(`local_evidence_not_4_${g.local_evidence_artifacts_referenced}`);
  for (const key of ['exact_editions_captured_by_this_artifact', 'source_files_cached_by_this_artifact', 'source_prose_copied', 'source_examples_copied', 'source_passages_selected', 'excerpts_selected', 'attribution_rows_filled', 'reviewer_returns_ingested', 'local_language_surfaces_filled', 'bridge_surfaces_accepted', 'translated_passages']) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  return failures;
}

const artifact = buildArtifact();
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
  route_verification_rows: artifact.gate_state.route_verification_rows,
  official_routes_checked: artifact.gate_state.official_routes_checked,
  local_evidence_artifacts_referenced: artifact.gate_state.local_evidence_artifacts_referenced,
  packet_sequence_rows: artifact.gate_state.packet_sequence_rows,
  source_prose_copied: artifact.gate_state.source_prose_copied,
  excerpts_selected: artifact.gate_state.excerpts_selected,
  local_language_surfaces_filled: artifact.gate_state.local_language_surfaces_filled,
  translated_passages: artifact.gate_state.translated_passages,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
