import { readFile, writeFile, readdir, stat } from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';

const root = process.cwd();
const outputs = path.join(root, 'outputs');

const artifactId = 'OPEN_TRANSLATION_REVIEW_ONLY_PACKET_SOURCE_SHELF_REFRESH_20260703T080000Z';
const noteId = 'OPEN_TRANSLATION_REVIEW_ONLY_PACKET_SOURCE_SHELF_REFRESH_NOTE_20260703T080100Z';
const generatedUtc = '2026-07-03T08:00:00Z';
const noteGeneratedUtc = '2026-07-03T08:01:00Z';
const packageOrder = 151;
const queueCandidateId = 'OTCQ-OPEN-TRANSLATION-REVIEW-ONLY-PACKET-SOURCE-SHELF-REFRESH-01';

const packageIndexFile = 'MALAY_INDONESIAN_BRUNEI_SINGAPORE_REVIEW_PACKAGE_INDEX_V2_20260630T180000Z';
const queueFile = 'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z';
const satqFile = 'SOURCE_AWARE_TRANSLATION_PACKET_START_QUEUE_20260630T215341Z';
const programFile = 'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z';
const charterFile = 'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z';
const uploadQueueFile = 'NOETHER_POST_MANIFEST_COORDINATION_UPLOAD_QUEUE_20260702';

const parentArtifacts = [
  'OPEN_TRANSLATION_CANDIDATE_QUEUE_20260629T151455Z',
  'WORLD_FAMILY_TRANSLATION_AND_CONSTRUCTION_WORKING_CHARTER_20260629T151455Z',
  'SEMI_CONSTRUCTED_ACCESS_PROGRAM_INDEX_20260629T120831Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_CONSTRUCTION_SEED_START_INDEX_20260703T070000Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SLOT_RETURN_LEDGER_TEMPLATE_20260703T071500Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SURFACE_SIDECAR_TEMPLATE_BLANK_20260703T073000Z',
  'SEMI_CONSTRUCTED_RELATION_FUNCTION_NO_CONSTRUCTION_DECISION_LEDGER_TEMPLATE_20260703T074500Z'
];

const zeroGateKeys = [
  'source_text_or_excerpt_files_created',
  'source_text_copied',
  'source_definitions_copied',
  'source_examples_copied',
  'source_passages_selected',
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
  'license_rechecks_completed',
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

async function statRoutePath(relativePath) {
  const normalized = relativePath.replaceAll('\\', '/');
  try {
    const info = await stat(path.join(root, normalized));
    return {
      path: normalized,
      exists: true,
      type: info.isDirectory() ? 'directory' : 'file',
      bytes: info.isFile() ? info.size : null
    };
  } catch {
    return {
      path: normalized,
      exists: false,
      type: 'missing',
      bytes: null
    };
  }
}

function findCandidateIds(queue, terms, limit = 14) {
  const candidates = Array.isArray(queue.candidate_sources) ? queue.candidate_sources : [];
  const loweredTerms = terms.map((term) => term.toLowerCase());
  return candidates
    .filter((candidate) => {
      const haystack = [
        candidate.id,
        candidate.source,
        candidate.route,
        candidate.best_translation_use,
        candidate.license_status_to_recheck
      ].filter(Boolean).join(' ').toLowerCase();
      return loweredTerms.some((term) => haystack.includes(term));
    })
    .map((candidate) => candidate.id || candidate.source_id || candidate.candidate_id || candidate.source)
    .filter(Boolean)
    .slice(0, limit);
}

async function buildShelfRow(queue, spec, index) {
  const routeFiles = await Promise.all(spec.local_route_paths.map(statRoutePath));
  const present = routeFiles.filter((item) => item.exists);
  const fileBytes = routeFiles.reduce((sum, item) => sum + (typeof item.bytes === 'number' ? item.bytes : 0), 0);
  const candidateQueueMatchIds = findCandidateIds(queue, spec.candidate_terms);
  return {
    source_shelf_row_id: `OTRSS-${String(index + 1).padStart(3, '0')}`,
    source_family: spec.source_family,
    shelf_role: spec.shelf_role,
    local_route_kind: spec.local_route_kind,
    packet_start_shapes: spec.packet_start_shapes,
    candidate_lanes: spec.candidate_lanes,
    source_route_terms_used_for_queue_match: spec.candidate_terms,
    candidate_queue_match_ids: candidateQueueMatchIds,
    candidate_queue_matches: candidateQueueMatchIds.length,
    local_route_paths: routeFiles,
    local_route_paths_present: present.length,
    local_route_file_bytes: fileBytes,
    selected_use_without_source_text: spec.selected_use_without_source_text,
    why_useful_beyond_core: spec.why_useful_beyond_core,
    review_only_start_state: spec.review_only_start_state,
    blocked_until: [
      'license_recheck_for_exact_edition_or_route',
      'attribution_or_modification_notice_sidecar_when_adaptation_is_selected',
      'source_coordinate_scan_before_any_excerpt_selection',
      'reviewer_route_for_language_or_modality_specific_terms',
      'explicit promotion_decision_before_any_translation_or_surface'
    ],
    source_text_or_excerpt_files_created: 0,
    source_text_copied: 0,
    source_definitions_copied: 0,
    source_examples_copied: 0,
    source_passages_selected: 0,
    exact_line_spans_selected: 0,
    candidate_line_ranges_selected: 0,
    translated_passages: 0,
    proposed_bridge_lexemes: 0,
    accepted_bridge_surfaces: 0,
    accepted_local_language_terms: 0,
    packet_ready: false,
    translation_ready: false,
    pilot_ready: false
  };
}

async function buildShelfRows(queue) {
  const specs = [
    {
      source_family: 'Open Logic Project proof and set/function shelf',
      shelf_role: 'open_oer_translation_source',
      local_route_kind: 'candidate_queue_plus_local_checkout_route',
      candidate_terms: ['open logic', 'olp', 'proof-literacy'],
      local_route_paths: ['work/OpenLogic'],
      packet_start_shapes: ['proof_literacy_micro_packet', 'set_function_packet', 'source_authority_reader_packet'],
      candidate_lanes: ['proof_literacy', 'logic', 'set_function', 'world_family_bridge_review', 'semi_constructed_control_layer'],
      selected_use_without_source_text: 'proof-reading and set/function packet starts by file pointer, attribution sidecar, and neutral prompt architecture only',
      why_useful_beyond_core: 'supports proof literacy and relation/function vocabulary across multiple target lanes before language-specific surface work',
      review_only_start_state: 'candidate_queue_routes_exist_and_local_checkout_path_exists_no_excerpts_selected'
    },
    {
      source_family: 'Book of Proof permission-reference shelf',
      shelf_role: 'open_oer_translation_source',
      local_route_kind: 'local_cache_manifest_route',
      candidate_terms: ['book of proof'],
      local_route_paths: ['outputs/source_cache/book_of_proof_permission_reference_20260630T072056Z/cache_manifest.json'],
      packet_start_shapes: ['proof_literacy_micro_packet', 'set_function_packet'],
      candidate_lanes: ['proof_literacy', 'set_function', 'source_authority_reader_packet'],
      selected_use_without_source_text: 'alternate proof-literacy source route for later attribution and coordinate scanning',
      why_useful_beyond_core: 'gives a second proof-literacy source family when OLP alone would be too narrow',
      review_only_start_state: 'cache_manifest_present_no_source_passages_selected'
    },
    {
      source_family: 'DMOI exact-edition relation/function shelf',
      shelf_role: 'open_oer_translation_source_and_construction_seed_parent',
      local_route_kind: 'exact_edition_license_and_ptx_manifest_route',
      candidate_terms: ['dmoi', 'discrete mathematics', 'relation/function', 'relation function'],
      local_route_paths: [
        'outputs/source_cache/dmoi_exact_edition_license_20260630T070010Z/github_LICENSE_at_edition.txt',
        'outputs/source_cache/dmoi_exact_edition_license_20260630T070010Z/edition_source_82336dc87d77c3f18d2cdbc8ec1e74eb3ba38799/source_ptx_cache_manifest_20260701T150000Z.json'
      ],
      packet_start_shapes: ['set_function_packet', 'relation_function_bridge_register', 'review_only_construction_seed'],
      candidate_lanes: ['relation_function', 'DMOI', 'semi_constructed_bridge_register', 'local_standard_first'],
      selected_use_without_source_text: 'coordinate-driven relation/function seed already opened in packages 147-150 with no copied source text',
      why_useful_beyond_core: 'anchors the current constructed-language method lane in a precise source route and coordinate register',
      review_only_start_state: 'exact_edition_license_and_source_ptx_manifest_present_parent_seed_started_no_surfaces'
    },
    {
      source_family: 'FCLA linear algebra shelf',
      shelf_role: 'open_oer_translation_source',
      local_route_kind: 'local_cache_manifest_route',
      candidate_terms: ['fcla', 'linear algebra'],
      local_route_paths: ['outputs/source_cache/fcla_gfdl_exact_commit_20260630T070951Z/cache_manifest.json'],
      packet_start_shapes: ['linear_algebra_packet', 'source_authority_reader_packet'],
      candidate_lanes: ['linear_algebra', 'matrix_language', 'vector_space_language', 'beyond_core_translation_candidate'],
      selected_use_without_source_text: 'linear algebra packet candidate route for future coordinate scan and attribution decision',
      why_useful_beyond_core: 'adds higher-math technical vocabulary beyond proof literacy and relation/function',
      review_only_start_state: 'exact_commit_cache_manifest_present_no_coordinate_scan_started_here'
    },
    {
      source_family: 'AATA abstract algebra shelf',
      shelf_role: 'open_oer_translation_source',
      local_route_kind: 'local_cache_manifest_route',
      candidate_terms: ['aata', 'abstract algebra'],
      local_route_paths: ['outputs/source_cache/aata_gfdl_exact_commit_20260630T071615Z/cache_manifest.json'],
      packet_start_shapes: ['abstract_algebra_packet', 'source_authority_reader_packet'],
      candidate_lanes: ['abstract_algebra', 'operation_structure_language', 'beyond_core_translation_candidate'],
      selected_use_without_source_text: 'abstract algebra packet candidate route for later exact-source coordinate scan',
      why_useful_beyond_core: 'opens terminology for operations, structures, and algebraic examples after the set/function base',
      review_only_start_state: 'exact_commit_cache_manifest_present_no_coordinate_scan_started_here'
    },
    {
      source_family: 'OpenIntro IMS statistics and numeracy shelf',
      shelf_role: 'open_oer_translation_source',
      local_route_kind: 'local_readme_and_license_route',
      candidate_terms: ['openintro', 'ims', 'statistics', 'numeracy'],
      local_route_paths: [
        'outputs/source_cache/openintro_ims2/github_ims_README.md',
        'outputs/source_cache/openintro_ims2/github_ims_README_at_b88f367a.md',
        'outputs/source_cache/openintro_ims2/openintro_license_page.html'
      ],
      packet_start_shapes: ['numeracy_public_service_packet', 'statistics_reader_packet'],
      candidate_lanes: ['statistics', 'public_numeracy', 'data_literacy', 'beyond_core_translation_candidate'],
      selected_use_without_source_text: 'statistics and public numeracy source route for later license and excerpt selection review',
      why_useful_beyond_core: 'brings translation access to quantitative public-service material, not just pure mathematics',
      review_only_start_state: 'local_route_files_present_no_excerpts_or_statistical_examples_selected'
    },
    {
      source_family: 'Malay-Indonesian set/function authority support shelf',
      shelf_role: 'language_authority_support_not_translation_source',
      local_route_kind: 'metadata_manifest_route',
      candidate_terms: ['malay-indonesian', 'set/function', 'malay', 'indonesian'],
      local_route_paths: ['outputs/source_cache/malay_indonesian_set_function_source_retry_20260630T074520Z/metadata_manifest.json'],
      packet_start_shapes: ['local_standard_support_packet', 'set_function_packet_review_support'],
      candidate_lanes: ['Malay_Indonesian', 'Brunei', 'Singapore', 'local_standard_first', 'reviewer_route_support'],
      selected_use_without_source_text: 'authority-route support for term questions and switch-card review blanks, not direct source translation',
      why_useful_beyond_core: 'prevents accidental inheritance across Malay/Indonesian/Brunei/Singapore authority contexts',
      review_only_start_state: 'metadata_manifest_present_authority_support_only_zero_surfaces_accepted'
    },
    {
      source_family: 'Sign-language video-first review shelf',
      shelf_role: 'modality_authority_support_not_text_translation_source',
      local_route_kind: 'cache_manifest_route',
      candidate_terms: ['sign language', 'video-first', 'auslan', 'bsl', 'ssc'],
      local_route_paths: [
        'outputs/source_cache/uc04_sign_language_video_first_review_packet/cache_manifest.json',
        'outputs/source_cache/uc04_auslan_signbank_exact_page_audit/cache_manifest.json',
        'outputs/source_cache/uc04_bsl_ssc_exact_term_page_audit/cache_manifest.json'
      ],
      packet_start_shapes: ['signed_language_definition_support_packet', 'video_first_review_packet'],
      candidate_lanes: ['signed_languages', 'Auslan', 'BSL', 'video_first_review', 'accessibility'],
      selected_use_without_source_text: 'video-first and exact-term audit support for future definition or notation access packets',
      why_useful_beyond_core: 'keeps modality-specific access in the translation program rather than treating signs as word substitutions',
      review_only_start_state: 'cache_manifests_present_video_first_review_only_no_surfaces_accepted'
    },
    {
      source_family: 'Pan-Romance Galician and Occitan register shelf',
      shelf_role: 'language_register_support_not_direct_translation_source',
      local_route_kind: 'cache_and_metadata_manifest_routes',
      candidate_terms: ['pan-romance', 'galician', 'occitan', 'romance'],
      local_route_paths: [
        'outputs/source_cache/pan_romance_native_math_register_shelf_20260629T223000Z/cache_manifest.json',
        'outputs/source_cache/pan_romance_galician_occitan_source_retry_20260629T224000Z/cache_manifest.json',
        'outputs/source_cache/pan_romance_occitan_algebra_proof_prose_retry_20260629T225804Z/cache_manifest.json',
        'outputs/source_cache/pan_romance_galician_abstract_algebra_source_retry_20260630T054358Z/cache_manifest.json'
      ],
      packet_start_shapes: ['romance_technical_register_support_packet', 'abstract_algebra_packet_review_support'],
      candidate_lanes: ['Pan_Romance', 'Galician', 'Occitan', 'technical_register_review', 'beyond_core_translation_candidate'],
      selected_use_without_source_text: 'register and authority support for later Romance-language technical packet routing',
      why_useful_beyond_core: 'makes French/Spanish-adjacent Romance work less likely to flatten smaller Romance authority routes',
      review_only_start_state: 'multiple_cache_manifest_routes_present_no_reference_prose_copied_here'
    },
    {
      source_family: 'Semi-constructed relation/function method shelf',
      shelf_role: 'construction_method_support_not_source_text',
      local_route_kind: 'local_artifact_parent_route',
      candidate_terms: ['semi-constructed', 'relation/function', 'construction seed', 'surface sidecar'],
      local_route_paths: [
        'outputs/SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_CONSTRUCTION_SEED_START_INDEX_20260703T070000Z.json',
        'outputs/SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SLOT_RETURN_LEDGER_TEMPLATE_20260703T071500Z.json',
        'outputs/SEMI_CONSTRUCTED_RELATION_FUNCTION_REVIEW_ONLY_SURFACE_SIDECAR_TEMPLATE_BLANK_20260703T073000Z.json',
        'outputs/SEMI_CONSTRUCTED_RELATION_FUNCTION_NO_CONSTRUCTION_DECISION_LEDGER_TEMPLATE_20260703T074500Z.json'
      ],
      packet_start_shapes: ['review_only_construction_seed', 'slot_return_ledger', 'surface_sidecar_blank', 'no_construction_decision_ledger'],
      candidate_lanes: ['semi_constructed_language_design', 'relation_function', 'review_only_method', 'no_construction_path'],
      selected_use_without_source_text: 'method scaffold for when a constructive-language path becomes clear and reviewed enough to start',
      why_useful_beyond_core: 'turns constructed-language work into a documented review system rather than ad hoc invention',
      review_only_start_state: 'parent_artifacts_present_zero_returns_zero_surfaces_zero_decisions'
    }
  ];
  return Promise.all(specs.map((spec, index) => buildShelfRow(queue, spec, index)));
}

function buildPacketSummaryRows(sourceShelfRows) {
  const packetMap = new Map();
  for (const row of sourceShelfRows) {
    for (const packet of row.packet_start_shapes) {
      if (!packetMap.has(packet)) {
        packetMap.set(packet, {
          packet_shape: packet,
          linked_source_shelf_row_ids: [],
          source_families: [],
          packet_ready_rows: 0,
          source_text_or_excerpt_files_created: 0,
          translations_started: 0
        });
      }
      const entry = packetMap.get(packet);
      entry.linked_source_shelf_row_ids.push(row.source_shelf_row_id);
      entry.source_families.push(row.source_family);
    }
  }
  return [...packetMap.values()].map((entry, index) => ({
    packet_summary_row_id: `OTRSS-PACKET-${String(index + 1).padStart(2, '0')}`,
    ...entry,
    source_families: [...new Set(entry.source_families)],
    linked_source_shelf_row_ids: [...new Set(entry.linked_source_shelf_row_ids)],
    review_only_status: 'candidate_packet_shape_only_no_excerpt_no_translation_no_surface'
  }));
}

function buildNextStartRows() {
  return [
    {
      next_start_row_id: 'OTRSS-NEXT-01',
      lane: 'proof_literacy',
      useful_next_artifact: 'proof_literacy_source_coordinate_scan_router',
      why: 'OLP and Book of Proof routes are both present; the next non-destructive step is coordinate scanning and attribution routing, not translation.'
    },
    {
      next_start_row_id: 'OTRSS-NEXT-02',
      lane: 'linear_and_abstract_algebra',
      useful_next_artifact: 'algebra_source_coordinate_scan_queue',
      why: 'FCLA and AATA exact-commit cache manifests are present and can support later packet routing after license/attribution checks.'
    },
    {
      next_start_row_id: 'OTRSS-NEXT-03',
      lane: 'statistics_and_public_numeracy',
      useful_next_artifact: 'openintro_numeracy_packet_route_sheet',
      why: 'OpenIntro IMS gives a path to public numeracy and data literacy, expanding translation access beyond proof-heavy material.'
    },
    {
      next_start_row_id: 'OTRSS-NEXT-04',
      lane: 'semi_constructed_relation_function',
      useful_next_artifact: 'reviewer_return_or_no_construction_decision_ingest_only_when_dated_return_exists',
      why: 'Packages 147-150 opened the construction method lane; promotion still waits on returns, evidence, or explicit no-construction decisions.'
    },
    {
      next_start_row_id: 'OTRSS-NEXT-05',
      lane: 'signed_language_and_accessibility',
      useful_next_artifact: 'video_first_definition_packet_router',
      why: 'Existing UC04 cache manifests make modality-aware review possible without reducing signed-language work to text-term substitution.'
    }
  ];
}

function buildArtifact(queue) {
  return buildShelfRows(queue).then((sourceShelfRows) => {
    const packetSummaryRows = buildPacketSummaryRows(sourceShelfRows);
    const nextStartRows = buildNextStartRows();
    const localRoutePathsPresent = sourceShelfRows.reduce((sum, row) => sum + row.local_route_paths_present, 0);
    const candidateQueueMatches = sourceShelfRows.reduce((sum, row) => sum + row.candidate_queue_matches, 0);
    const openOerRows = sourceShelfRows.filter((row) => row.shelf_role.includes('open_oer')).length;
    const supportRows = sourceShelfRows.length - openOerRows;

    return {
      artifact_id: artifactId,
      generated_utc: generatedUtc,
      status: 'review_only_packet_source_shelf_refresh_no_source_text_no_excerpts_no_forms_no_translation_no_pilot',
      pilot_ready_claim: false,
      translation_ready_claim: false,
      publication_ready_claim: false,
      constructed_surface_ready_claim: false,
      purpose: 'Refresh the open-translation and semi-constructed-language source shelf by mapping already-cached or already-cataloged source routes to review-only packet starts beyond the current core noteser/memoser pilot, without copying source text, selecting excerpts, proposing forms, or claiming readiness.',
      parent_artifacts: parentArtifacts,
      upload_policy: {
        substantive_artifact: true,
        local_queue_default: 'upload_when_valid_checkout_or_staging_path_exists',
        no_mobile_plan_deferral: true,
        remote_action_performed_by_this_artifact: false
      },
      boundary: {
        artifact_is: [
          'source-route and packet-start catalog refresh',
          'review-only beyond-core translation candidate shelf',
          'semi-constructed construction-method continuation pointer'
        ],
        artifact_is_not: [
          'source excerpt file',
          'translated passage',
          'accepted terminology list',
          'constructed-language lexicon',
          'pilot readiness claim',
          'publication readiness claim',
          'license clearance decision',
          'remote upload or GitHub operation'
        ],
        promotion_requires: [
          'exact license and edition recheck',
          'attribution or modification notice sidecar when needed',
          'source coordinate scan before excerpt selection',
          'reviewer route for target language or modality',
          'explicit promotion decision before any translation or constructed surface'
        ]
      },
      source_shelf_rows: sourceShelfRows,
      packet_summary_rows: packetSummaryRows,
      next_start_rows: nextStartRows,
      gap_notes: [
        'Chinese, French, and Spanish lanes are not promoted here unless a checked local source route appears in this artifact row set.',
        'Pan-Romance rows here are register/support rows for Galician and Occitan routes, not a general French or Spanish packet.',
        'Malay-Indonesian rows remain authority-support rows and do not license inheritance across Brunei, Singapore, Malaysian Malay, and Indonesian contexts.',
        'The semi-constructed lane remains review-only until returns or explicit no-construction decisions exist.'
      ],
      gate_state: {
        source_shelf_rows: sourceShelfRows.length,
        open_oer_translation_source_rows: openOerRows,
        support_or_method_rows: supportRows,
        packet_summary_rows: packetSummaryRows.length,
        next_start_rows: nextStartRows.length,
        local_route_paths_present: localRoutePathsPresent,
        candidate_queue_matches: candidateQueueMatches,
        source_text_or_excerpt_files_created: 0,
        source_text_copied: 0,
        source_definitions_copied: 0,
        source_examples_copied: 0,
        source_passages_selected: 0,
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
        license_rechecks_completed: 0,
        pilot_ready_claims: 0,
        publication_ready: false,
        translation_ready: false,
        constructed_surface_ready: false,
        pilot_ready: false
      },
      validation_snapshot: {
        expected_source_shelf_rows: 10,
        expected_min_local_route_paths_present: 10,
        expected_min_candidate_queue_matches: 1,
        zero_gate_assertions: zeroGateKeys,
        readiness_claims: 0
      },
      decision: 'Package 151 is a substantive upload-bound source-shelf refresh. It broadens the translation/construction candidate map while keeping all source-text, excerpt, translation, surface, license-clearance, pilot, and publication gates closed.'
    };
  });
}

function buildArtifactMd(artifact) {
  const g = artifact.gate_state;
  const rows = artifact.source_shelf_rows.map((row) => `| ${row.source_shelf_row_id} | ${row.source_family} | ${row.shelf_role} | ${row.packet_start_shapes.join('<br>')} | ${row.local_route_paths_present} | ${row.candidate_queue_matches} |`).join('\n');
  const packetRows = artifact.packet_summary_rows.map((row) => `| ${row.packet_summary_row_id} | ${row.packet_shape} | ${row.linked_source_shelf_row_ids.join(', ')} | ${row.packet_ready_rows} |`).join('\n');
  const nextRows = artifact.next_start_rows.map((row) => `| ${row.next_start_row_id} | ${row.lane} | ${row.useful_next_artifact} |`).join('\n');
  return `# ${artifact.artifact_id}

Generated UTC: \`${artifact.generated_utc}\`

Status: \`${artifact.status}\`

## Purpose

${artifact.purpose}

## Counts

- Source shelf rows: \`${g.source_shelf_rows}\`
- Open OER translation-source rows: \`${g.open_oer_translation_source_rows}\`
- Support or method rows: \`${g.support_or_method_rows}\`
- Packet summary rows: \`${g.packet_summary_rows}\`
- Next-start rows: \`${g.next_start_rows}\`
- Local route paths present: \`${g.local_route_paths_present}\`
- Candidate queue matches: \`${g.candidate_queue_matches}\`

## Source Shelf Rows

| Row | Source family | Role | Packet starts | Local routes present | Queue matches |
| --- | --- | --- | --- | ---: | ---: |
${rows}

## Packet Summary

| Row | Packet shape | Source rows | Ready rows |
| --- | --- | --- | ---: |
${packetRows}

## Useful Next Starts

| Row | Lane | Useful next artifact |
| --- | --- | --- |
${nextRows}

## Zero Gates

- Source text/excerpt files: \`0\`
- Source text/definitions/examples copied: \`0 / 0 / 0\`
- Source passages selected: \`0\`
- Exact spans / candidate line ranges: \`0 / 0\`
- Translated passages: \`0\`
- Proposed bridge lexemes / morphemes / syntax / displays: \`0 / 0 / 0 / 0\`
- Accepted bridge surfaces / local-language terms: \`0 / 0\`
- Reviewer returns ingested / license rechecks completed: \`0 / 0\`
- Readiness: \`publication=false, translation=false, constructed_surface=false, pilot=false\`

Boundary: this is a source-route and packet-start shelf refresh only. It queues substantive catalog work for upload when a valid staging path exists, but it performs no remote upload, commit, push, PR update, Zenodo action, source-text copying, excerpt selection, translation, proposed surface, or readiness claim.
`;
}

function buildArtifactCsv(artifact) {
  const rows = [];
  rows.push(['section', 'row_id', 'source_family_or_packet', 'role_or_packet_shape', 'packet_starts_or_source_rows', 'local_routes_present', 'queue_matches', 'ready'].map(csvCell).join(','));
  for (const row of artifact.source_shelf_rows) {
    rows.push([
      'source_shelf_row',
      row.source_shelf_row_id,
      row.source_family,
      row.shelf_role,
      row.packet_start_shapes,
      row.local_route_paths_present,
      row.candidate_queue_matches,
      row.packet_ready
    ].map(csvCell).join(','));
  }
  for (const row of artifact.packet_summary_rows) {
    rows.push([
      'packet_summary_row',
      row.packet_summary_row_id,
      row.packet_shape,
      row.review_only_status,
      row.linked_source_shelf_row_ids,
      '',
      '',
      row.packet_ready_rows
    ].map(csvCell).join(','));
  }
  for (const row of artifact.next_start_rows) {
    rows.push([
      'next_start_row',
      row.next_start_row_id,
      row.lane,
      row.useful_next_artifact,
      row.why,
      '',
      '',
      false
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
    status: 'pointer_only_package151_source_shelf_refresh_note_upload_bound_no_remote_action_no_source_text_no_translation_no_readiness',
    summary: 'Package 151 queues a review-only source-shelf refresh mapping cached/open source routes and support lanes to beyond-core translation and semi-constructed packet starts.',
    counts: {
      source_shelf_rows: g.source_shelf_rows,
      open_oer_translation_source_rows: g.open_oer_translation_source_rows,
      support_or_method_rows: g.support_or_method_rows,
      packet_summary_rows: g.packet_summary_rows,
      next_start_rows: g.next_start_rows,
      local_route_paths_present: g.local_route_paths_present,
      candidate_queue_matches: g.candidate_queue_matches
    },
    zero_gates: {
      source_text_or_excerpt_files_created: 0,
      source_text_copied: 0,
      source_passages_selected: 0,
      translated_passages: 0,
      proposed_bridge_lexemes: 0,
      accepted_bridge_surfaces: 0,
      reviewer_returns_ingested: 0,
      readiness_claims: 0
    },
    upload_policy: artifact.upload_policy,
    no_remote_action_by_this_note: true
  };
}

function buildNoteMd(note, artifact) {
  const g = artifact.gate_state;
  return `# Package 151 Source Shelf Refresh Note

Artifact: \`${note.artifact_id}\`

Source artifact: \`${artifact.artifact_id}\`

Generated UTC: \`${note.generated_utc}\`

Pointer-only local note: package 151 creates \`${g.source_shelf_rows}\` source-shelf rows, \`${g.packet_summary_rows}\` packet-summary rows, and \`${g.next_start_rows}\` next-start rows. It is substantive catalog work and is queued for upload when a valid staging path exists.

Zero gates: \`0\` source-text/excerpt files, \`0\` source text copied, \`0\` source passages selected, \`0\` translations, \`0\` proposed bridge forms, \`0\` accepted surfaces, \`0\` reviewer returns ingested, \`0\` readiness claims.

Boundary: source-route and packet-start shelf refresh only. This note makes no commit, push, PR, Zenodo, dispatch, return, evidence review, source-text, excerpt, proposed form, accepted surface, translation, publication, pilot, legal-advice, or remote-state claim.
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
    role: 'open_translation_review_only_packet_source_shelf_refresh',
    artifact: artifactId,
    current_use: `10 source-shelf rows; ${g.local_route_paths_present} local route paths present; cross-source review-only packet starts; 0 source text, 0 excerpts, 0 translations, 0 forms, 0 readiness`
  };
  const existingPackageRowIndex = order.findIndex((row) => row?.artifact === artifactId);
  if (existingPackageRowIndex >= 0) {
    order[existingPackageRowIndex] = { ...order[existingPackageRowIndex], ...packageRow };
  } else {
    order.push({
      ...packageRow
    });
  }
  order.sort((a, b) => a.order - b.order);
  order.forEach((row, index) => { row.order = index + 1; });
  packageIndex.obj.current_open_translation_review_only_packet_source_shelf_refresh = artifactId;
  packageIndex.obj.gate_state ??= {};
  Object.assign(packageIndex.obj.gate_state, {
    current_open_translation_source_shelf_rows: g.source_shelf_rows,
    current_open_translation_packet_summary_rows: g.packet_summary_rows,
    current_open_translation_local_route_paths_present: g.local_route_paths_present,
    current_open_translation_source_text_or_excerpt_files: 0,
    current_open_translation_translated_passages: 0,
    package_artifacts_ordered: order.length
  });
  addUnique(ensureArray(packageIndex.obj, 'immediate_next_actions'), `continue_from_${artifactId}_with_coordinate_scan_router_or_packet_route_sheet_only_no_source_text_no_excerpts_no_translation_upload_when_path_exists`);
  await writeJson(packageIndexFile, packageIndex.obj);

  const queue = await readJson(queueFile);
  const candidates = ensureArray(queue.obj, 'candidate_sources');
  upsertById(candidates, ['id', 'source_id', 'candidate_id'], queueCandidateId, {
    id: queueCandidateId,
    source: 'Open translation review-only packet source shelf refresh',
    route: artifactId,
    license_status_to_recheck: 'source_shelf_refresh_only_recheck_exact_license_edition_and_attribution_before_any_excerpt_adaptation_or_translation',
    best_translation_use: 'broad beyond-core source-route shelf for proof literacy, set/function, linear algebra, abstract algebra, statistics/numeracy, signed-language access, Malay-Indonesian authority support, Pan-Romance register support, and semi-constructed relation/function method work',
    candidate_lanes: [
      'proof_literacy',
      'set_function',
      'linear_algebra',
      'abstract_algebra',
      'statistics_public_numeracy',
      'signed_language_access',
      'Malay_Indonesian_authority_support',
      'Pan_Romance_register_support',
      'semi_constructed_relation_function'
    ],
    priority: 1,
    status: 'review_only_source_shelf_refresh_no_source_text_no_excerpts_no_translation_no_forms_no_pilot',
    upload_policy: artifact.upload_policy,
    gate_state: {
      source_shelf_rows: g.source_shelf_rows,
      packet_summary_rows: g.packet_summary_rows,
      local_route_paths_present: g.local_route_paths_present,
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
  addUnique(ensureArray(queue.obj, 'immediate_next_actions'), `current_open_translation_review_only_packet_source_shelf_refresh: ${artifactId}_10_source_rows_${g.packet_summary_rows}_packet_shapes_0_source_text_0_excerpts_0_translation_upload_when_path_exists_no_mobile_plan_deferral`);
  await writeJson(queueFile, queue.obj);

  const satq = await readJson(satqFile);
  satq.obj.current_open_translation_review_only_packet_source_shelf_refresh_artifact = artifactId;
  addUnique(ensureArray(satq.obj, 'immediate_next_actions'), `current_open_translation_review_only_packet_source_shelf_refresh_artifact: ${artifactId}`);
  satq.obj.gate_state ??= {};
  Object.assign(satq.obj.gate_state, {
    current_open_translation_source_shelf_rows: g.source_shelf_rows,
    current_open_translation_packet_summary_rows: g.packet_summary_rows,
    current_open_translation_source_text_or_excerpt_files: 0,
    current_open_translation_translated_passages: 0,
    current_open_translation_surfaces: 0
  });
  await writeJson(satqFile, satq.obj);

  const program = await readJson(programFile);
  program.obj.current_open_translation_review_only_packet_source_shelf_refresh = artifactId;
  addUnique(ensureArray(program.obj, 'next_actions'), `current_open_translation_review_only_packet_source_shelf_refresh: ${artifactId}_source_route_catalog_refresh_before_any_excerpts_translations_surfaces_or_pilot_claims`);
  await writeJson(programFile, program.obj);

  const charter = await readJson(charterFile);
  charter.obj.current_open_translation_review_only_packet_source_shelf_refresh = artifactId;
  addUnique(ensureArray(charter.obj, 'small_points_to_preserve'), `${artifactId}: broadens beyond-core translation/construction shelf with 10 source/support/method rows and ${g.packet_summary_rows} packet-shape summary rows; substantive upload-bound artifact; 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, 0 readiness.`);
  await writeJson(charterFile, charter.obj);

  await appendMdIfMissing('README.md', artifactId, `- \`${artifactId}.md/json/csv\` - Open translation review-only packet source shelf refresh; 10 source/support/method rows, ${g.packet_summary_rows} packet-shape summaries, ${g.local_route_paths_present} local route paths present, 0 source text, 0 excerpts, 0 translations, no readiness claim.`);
  await appendMdIfMissing(`${packageIndexFile}.md`, artifactId, `## ${artifactId}\n\nAdded as package order 151: review-only open translation packet source shelf refresh. It maps existing source/cache/support/method routes into 10 source-shelf rows and ${g.packet_summary_rows} packet-shape summary rows while keeping 0 source text, 0 excerpts, 0 translations, 0 proposed forms, 0 accepted surfaces, and all readiness gates closed. It is upload-bound as substantive catalog work when a valid staging path exists.`);
  await appendMdIfMissing(`${queueFile}.md`, queueCandidateId, `| ${queueCandidateId} | Open translation review-only packet source shelf refresh | ${artifactId} | Broad source-route and packet-start shelf; 10 rows, ${g.packet_summary_rows} packet shapes, ${g.local_route_paths_present} local route paths present, 0 source text, 0 excerpts, 0 translation, upload when path exists. | false | false | |`);
  await appendMdIfMissing(`${satqFile}.md`, artifactId, `- current_open_translation_review_only_packet_source_shelf_refresh_artifact: \`${artifactId}\` (10 source/support/method rows; ${g.packet_summary_rows} packet-shape summary rows; 0 source text; 0 excerpts; 0 accepted surfaces or translation).`);
  await appendMdIfMissing(`${programFile}.md`, artifactId, `- current_open_translation_review_only_packet_source_shelf_refresh: \`${artifactId}\`; broad review-only source-route shelf for beyond-core translation and semi-constructed method work, no source text, excerpts, accepted terms, surfaces, translation, or pilot.`);
  await appendMdIfMissing(`${charterFile}.md`, artifactId, `- \`${artifactId}\`: source-route and packet-start shelf refresh across open OER, language authority/support, modality support, Pan-Romance register support, and semi-constructed relation/function method work; substantive and upload-bound, but not a source excerpt, translation, constructed form, license clearance, or readiness claim.`);
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
    { filename: `${artifactId}.json`, class: 'open_translation_review_only_packet_source_shelf_refresh' },
    { filename: `${artifactId}.md`, class: 'open_translation_review_only_packet_source_shelf_refresh' },
    { filename: `${artifactId}.csv`, class: 'open_translation_review_only_packet_source_shelf_refresh' },
    { filename: `${artifactId}.sha256`, class: 'checksum_sidecar' },
    { filename: `${noteId}.json`, class: 'open_translation_package151_coordination_note' },
    { filename: `${noteId}.md`, class: 'open_translation_package151_coordination_note' },
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
  upload.obj.package151_upload_queue_update = {
    captured_utc: '2026-07-03T08:02:00Z',
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
  const step = 'Stage package 151 open translation review-only packet source shelf refresh artifacts as substantive beyond-core translation/construction catalog material; do not defer them because of mobile-plan or bandwidth wording.';
  if (!upload.obj.staging_order.includes(step)) upload.obj.staging_order.splice(Math.max(0, upload.obj.staging_order.length - 3), 0, step);
  await writeJson(uploadQueueFile, upload.obj);
  await rebuildUploadQueueMd(upload.obj);
}

function validateGenerated(artifact) {
  const failures = [];
  const g = artifact.gate_state;
  if (artifact.source_shelf_rows.length !== artifact.validation_snapshot.expected_source_shelf_rows) failures.push(`source_shelf_rows_mismatch_${artifact.source_shelf_rows.length}`);
  if (g.source_shelf_rows !== artifact.validation_snapshot.expected_source_shelf_rows) failures.push(`gate_source_shelf_rows_mismatch_${g.source_shelf_rows}`);
  if (g.local_route_paths_present < artifact.validation_snapshot.expected_min_local_route_paths_present) failures.push(`too_few_local_routes_present_${g.local_route_paths_present}`);
  if (g.candidate_queue_matches < artifact.validation_snapshot.expected_min_candidate_queue_matches) failures.push(`too_few_candidate_queue_matches_${g.candidate_queue_matches}`);
  for (const key of artifact.validation_snapshot.zero_gate_assertions) {
    if (g[key] !== 0) failures.push(`nonzero_gate_${key}_${g[key]}`);
  }
  for (const row of artifact.source_shelf_rows) {
    if (row.source_text_or_excerpt_files_created || row.source_text_copied || row.source_definitions_copied || row.source_examples_copied || row.source_passages_selected || row.exact_line_spans_selected || row.candidate_line_ranges_selected || row.translated_passages || row.proposed_bridge_lexemes || row.accepted_bridge_surfaces || row.accepted_local_language_terms || row.packet_ready || row.translation_ready || row.pilot_ready) {
      failures.push(`nonzero_or_ready_source_shelf_row_${row.source_shelf_row_id}`);
      break;
    }
  }
  if (g.translation_ready || g.publication_ready || g.constructed_surface_ready || g.pilot_ready) failures.push('readiness_gate_open');
  if (artifact.pilot_ready_claim || artifact.translation_ready_claim || artifact.publication_ready_claim || artifact.constructed_surface_ready_claim) failures.push('artifact_ready_claim_open');
  return failures;
}

const queue = (await readJson(queueFile)).obj;
const artifact = await buildArtifact(queue);
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
const refreshedQueue = (await readJson(queueFile)).obj;
const upload = (await readJson(uploadQueueFile)).obj;

console.log(JSON.stringify({
  ok: true,
  artifact_id: artifactId,
  note_id: noteId,
  package_order_length: packageIndex.current_package_order?.length,
  queue_candidate_sources: refreshedQueue.candidate_sources?.length,
  upload_queue_files: upload.summary?.queued_files,
  upload_queue_bytes: upload.summary?.queued_bytes,
  bandwidth_mode: upload.bandwidth_mode,
  source_text_or_excerpt_files: upload.summary?.source_text_or_excerpt_files,
  source_shelf_rows: artifact.gate_state.source_shelf_rows,
  open_oer_translation_source_rows: artifact.gate_state.open_oer_translation_source_rows,
  support_or_method_rows: artifact.gate_state.support_or_method_rows,
  packet_summary_rows: artifact.gate_state.packet_summary_rows,
  next_start_rows: artifact.gate_state.next_start_rows,
  local_route_paths_present: artifact.gate_state.local_route_paths_present,
  candidate_queue_matches: artifact.gate_state.candidate_queue_matches,
  source_text_copied: artifact.gate_state.source_text_copied,
  translated_passages: artifact.gate_state.translated_passages,
  proposed_bridge_lexemes: artifact.gate_state.proposed_bridge_lexemes,
  accepted_bridge_surfaces: artifact.gate_state.accepted_bridge_surfaces,
  pilot_ready: artifact.gate_state.pilot_ready,
  root_output_json_files: rootJsonFiles,
  recursive_output_json_files: recursiveJsonFiles
}, null, 2));
