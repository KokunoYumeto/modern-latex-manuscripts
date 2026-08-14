#!/usr/bin/env python3
"""Deterministic, dependency-backed verifier for the public sidecar."""

from __future__ import annotations

import csv
import datetime as dt
import hashlib
import importlib.metadata
import io
import ipaddress
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlparse

import yaml
from jsonschema import Draft202012Validator, FormatChecker

sys.dont_write_bytecode = True

from pkg import (
    MANIFEST,
    ROOT,
    PackageError,
    canonical_manifest_bytes,
    digest,
    inventory,
    manifest_rows,
    parse_manifest,
)


TITLE = "Interlanguage CJK Mathematical Notation Backend"
VERSION = "1.0.0"
RELEASE_DATE = "2026-08-15"
REPOSITORY = "https://github.com/KokunoYumeto/modern-latex-manuscripts"
ZENODO_RECORD_ID = 21940307
ZENODO_CONCEPT_RECORD_ID = 21124403
VERSION_DOI = "10.5281/zenodo.21940307"
CONCEPT_DOI = "10.5281/zenodo.21124403"
CONTAINING_TITLE = "Interlanguage and Mathematical Translation Methodology Sidecar"
EXPECTED_AUTHORS = [
    "Manuscript Typesetting Project",
    "OpenAI Codex (GPT-5.6 Sol, Ultra)",
]
EXPECTED_KEYWORDS = [
    "mathematical notation",
    "Chinese",
    "Japanese",
    "Korean",
    "TeX",
    "Unicode",
    "terminology",
]
LICENSE_SHA256 = "A2010F343487D3F7618AFFE54F789F5487602331C0A8D03F49E9A7C547CF0499"
REQUIRED = {
    ".gitattributes",
    ".gitignore",
    "CITATION.cff",
    "LICENSE",
    "METHOD.md",
    "README.md",
    "RECOVERY.md",
    "RIGHTS.md",
    "SOURCES.md",
    "STANDARD.md",
    "THIRD_PARTY_NOTICES.md",
    "VERSION",
    "adverse.tsv",
    "archive.py",
    "doi.json",
    "doi.schema.json",
    "evidence.jsonl",
    "fixture_runner.py",
    "make_manifest.py",
    "pkg.py",
    "registry.json",
    "report.schema.json",
    "requirements.txt",
    "rights.json",
    "schema.json",
    "term.example.json",
    "term.schema.json",
    "tests.json",
    "tests.schema.json",
    "verify.py",
}
LOCKED_DEPENDENCIES = {
    "attrs": "26.1.0",
    "jsonschema": "4.26.0",
    "jsonschema-specifications": "2025.9.1",
    "PyYAML": "6.0.3",
    "referencing": "0.37.0",
    "rpds-py": "2026.5.1",
    "typing-extensions": "4.15.0",
}
RUNTIME_DEPENDENCIES = dict(LOCKED_DEPENDENCIES)
if sys.version_info >= (3, 13):
    RUNTIME_DEPENDENCIES.pop("typing-extensions")
ADVERSE_HEADER = [
    "issue_id",
    "lane",
    "proposal",
    "observed_failure",
    "disposition",
    "evidence_id",
]
ADVERSE_LANES = {
    "shared",
    "Chinese",
    "zh-Hans-CN",
    "zh-Hans-SG",
    "zh-Hant-generic",
    "zh-Hant-TW",
    "zh-Hant-HK",
    "zh-Hant-MO",
    "ja",
    "ko",
    "ko-KR",
    "ko-KP",
}
ALLOWED_TEXT_CONTROLS = {"\n", "\t"}
FORBIDDEN_CODEPOINTS = {
    0x7F,
    0xFEFF,
    0xFFFD,
    *range(0x80, 0xA0),
    *range(0x200B, 0x2010),
    *range(0x202A, 0x202F),
    *range(0x2060, 0x2065),
    *range(0x2066, 0x206A),
}
TASK_ID_RE = re.compile(r"\b019f[0-9a-f]{4}-[0-9a-f-]{20,}\b", re.I)
EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
PHONE_RE = re.compile(
    r"(?<![\w.])(?:\+?\d{1,3}[ -])?(?:\(?\d{2,4}\)?[ -]){2,}\d{2,4}(?![\w.])"
)
ABS_PATH_RES = (
    re.compile(r"(?<![A-Za-z])[A-Za-z]:[\\/]"),
    re.compile(
        r"(?<![\\\w])\\\\[A-Za-z0-9][A-Za-z0-9_.-]{1,62}\\"
        r"(?:Users|home|Documents|Desktop|Downloads|AppData|share)(?:\\|$)",
        re.I,
    ),
    re.compile(r"/(?:home|Users)/[^/\s]+/"),
    re.compile(r"(?:^|[\s\"'(])\.\.[\\/]"),
    re.compile(re.escape("file" + "://"), re.I),
    re.compile(r"(?:^|[\\/])\.codex(?:[\\/]|$)", re.I),
    re.compile(r"\bDownloads[\\/]", re.I),
)
SECRET_RES = (
    re.compile("git" + r"hub_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),
    re.compile("-----BEGIN " + r"(?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(
        r"(?:authorization|bearer|access[_-]?token|api[_-]?key|client[_-]?secret|password)"
        r"[ \t]*[:=][ \t]*[\"']?[A-Za-z0-9_./+-]{16,}",
        re.I,
    ),
)
URL_RE = re.compile(r"https://[^\s<>\]\[)\"']+")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


checks: list[dict[str, object]] = []


def add(name: str, passed: bool, detail: object) -> None:
    checks.append({"name": name, "passed": bool(passed), "detail": detail})


def strict_pairs(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key: {key}")
        result[key] = value
    return result


def reject_constant(value: str) -> None:
    raise ValueError(f"non-finite number: {value}")


def strict_json(text: str) -> object:
    return json.loads(
        text,
        object_pairs_hook=strict_pairs,
        parse_constant=reject_constant,
    )


class UniqueKeyLoader(yaml.SafeLoader):
    pass


def yaml_mapping(loader: UniqueKeyLoader, node: yaml.Node, deep: bool = False) -> dict[object, object]:
    pairs = loader.construct_pairs(node, deep=deep)
    result: dict[object, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = value
    return result


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    yaml_mapping,
)


def yaml_dates(value: object) -> object:
    if isinstance(value, (dt.date, dt.datetime)):
        return value.isoformat()
    if isinstance(value, list):
        return [yaml_dates(item) for item in value]
    if isinstance(value, dict):
        return {key: yaml_dates(item) for key, item in value.items()}
    return value


format_checker = FormatChecker()


@format_checker.checks("date")
def valid_date(value: object) -> bool:
    if not isinstance(value, str):
        return True
    try:
        return dt.date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


@format_checker.checks("uri")
def valid_uri(value: object) -> bool:
    if not isinstance(value, str):
        return True
    parsed = urlparse(value)
    return bool(parsed.scheme and parsed.netloc and not parsed.username and not parsed.password)


try:
    snapshots = inventory(ROOT)
except PackageError as exc:
    result = {
        "schema": "cjk-notation-verification-v2",
        "version": VERSION,
        "result": "FAIL",
        "checks_total": 1,
        "checks_passed": 0,
        "checks_failed": 1,
        "failed_checks": ["safe_inventory"],
        "checks": [{"name": "safe_inventory", "passed": False, "detail": str(exc)}],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    raise SystemExit(1)

files = set(snapshots)
add("required_files", REQUIRED <= files, sorted(REQUIRED - files))
add("shallow_payload", all("/" not in name and "\\" not in name for name in files), len(files))

manifest_data = (ROOT / MANIFEST).read_bytes() if (ROOT / MANIFEST).is_file() else b""
try:
    parsed_manifest = parse_manifest(manifest_data)
    manifest_error = None
except (PackageError, OSError) as exc:
    parsed_manifest = []
    manifest_error = str(exc)
expected_rows = manifest_rows(snapshots)
add("manifest_parse", manifest_error is None, manifest_error)
add(
    "manifest_exact",
    parsed_manifest == expected_rows,
    {
        "manifest_members": len(parsed_manifest),
        "live_members": len(expected_rows),
        "missing": sorted(set(name for name, _, _ in expected_rows) - set(name for name, _, _ in parsed_manifest)),
        "extra": sorted(set(name for name, _, _ in parsed_manifest) - set(name for name, _, _ in expected_rows)),
    },
)

texts: dict[str, str] = {}
text_errors: list[str] = []
for name, snapshot in snapshots.items():
    data = snapshot.data
    try:
        text = data.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        text_errors.append(f"{name}:utf8:{exc.start}")
        continue
    texts[name] = text
    if data.startswith(b"\xef\xbb\xbf"):
        text_errors.append(f"{name}:BOM")
    if "\r" in text:
        text_errors.append(f"{name}:CR")
    if not text.endswith("\n") or text.endswith("\n\n"):
        text_errors.append(f"{name}:terminal-LF")
    if unicodedata.normalize("NFC", text) != text:
        text_errors.append(f"{name}:NFC")
    for index, char in enumerate(text):
        code = ord(char)
        if (
            (code < 32 and char not in ALLOWED_TEXT_CONTROLS)
            or code in FORBIDDEN_CODEPOINTS
            or 0xD800 <= code <= 0xDFFF
        ):
            text_errors.append(f"{name}:U+{code:04X}@{index}")
            break
    if any(line.endswith((" ", "\t")) for line in text.splitlines()):
        text_errors.append(f"{name}:trailing-whitespace")
add("canonical_text", not text_errors, text_errors)

schema_errors: list[str] = []
json_docs: dict[str, object] = {}
for name in (
    "schema.json",
    "doi.schema.json",
    "report.schema.json",
    "term.schema.json",
    "tests.schema.json",
    "doi.json",
    "rights.json",
    "registry.json",
    "tests.json",
    "term.example.json",
):
    try:
        json_docs[name] = strict_json(texts[name])
    except (KeyError, ValueError, json.JSONDecodeError) as exc:
        schema_errors.append(f"{name}:{exc}")

for name in ("schema.json", "doi.schema.json", "report.schema.json", "term.schema.json", "tests.schema.json"):
    if name not in json_docs:
        continue
    try:
        Draft202012Validator.check_schema(json_docs[name])
    except Exception as exc:
        schema_errors.append(f"{name}:invalid-schema:{exc}")
add("json_schema_documents", not schema_errors, schema_errors)

records: list[dict[str, object]] = []
evidence_errors: list[str] = []
evidence_text = texts.get("evidence.jsonl", "")
evidence_lines = evidence_text.splitlines()
if not evidence_lines or any(not line for line in evidence_lines):
    evidence_errors.append("blank-or-empty JSONL line")
evidence_schema = json_docs.get("schema.json", {})
evidence_validator = Draft202012Validator(evidence_schema, format_checker=format_checker)
for line_no, line in enumerate(evidence_lines, 1):
    try:
        record = strict_json(line)
    except (ValueError, json.JSONDecodeError) as exc:
        evidence_errors.append(f"line {line_no}:{exc}")
        continue
    if not isinstance(record, dict):
        evidence_errors.append(f"line {line_no}:not-object")
        continue
    records.append(record)
    for error in sorted(evidence_validator.iter_errors(record), key=lambda item: (list(item.absolute_path), item.message)):
        evidence_errors.append(f"{record.get('id', line_no)}:{error.json_path}:{error.message}")
ids = [str(record.get("id")) for record in records]
expected_ids = [f"CJK-NOT-E{number:03d}" for number in range(1, len(records) + 1)]
if ids != expected_ids:
    evidence_errors.append("evidence IDs not unique/contiguous/in order")
add("evidence_schema", not evidence_errors, evidence_errors)

source_identity: dict[str, tuple[object, ...]] = {}
source_conflicts: list[str] = []
source_occurrences = 0
for record in records:
    for source in record.get("sources", []):
        if not isinstance(source, dict):
            continue
        source_occurrences += 1
        source_id = str(source.get("source_id"))
        identity = tuple(
            source.get(key)
            for key in (
                "class",
                "availability",
                "artifact",
                "bytes",
                "sha256",
                "url",
                "accessed",
                "version",
            )
        )
        prior = source_identity.setdefault(source_id, identity)
        if prior != identity:
            source_conflicts.append(source_id)
add("source_identity_consistency", not source_conflicts, sorted(set(source_conflicts)))

adverse_errors: list[str] = []
try:
    adverse_reader = csv.DictReader(io.StringIO(texts["adverse.tsv"], newline=""), delimiter="\t")
    adverse_rows = list(adverse_reader)
    if adverse_reader.fieldnames != ADVERSE_HEADER:
        adverse_errors.append("header")
except Exception as exc:
    adverse_rows = []
    adverse_errors.append(str(exc))
adverse_ids: list[str] = []
adverse_refs: set[str] = set()
for index, row in enumerate(adverse_rows, 1):
    issue = row.get("issue_id", "")
    adverse_ids.append(issue)
    if issue != f"CJK-NOT-A{index:03d}":
        adverse_errors.append(f"row {index}:issue-id")
    if row.get("lane") not in ADVERSE_LANES:
        adverse_errors.append(f"row {index}:lane")
    for key in ADVERSE_HEADER:
        value = row.get(key, "")
        if not value or value != value.strip():
            adverse_errors.append(f"row {index}:{key}")
    refs = row.get("evidence_id", "").split(";")
    if any(not ref or ref != ref.strip() for ref in refs) or len(refs) != len(set(refs)):
        adverse_errors.append(f"row {index}:references")
    adverse_refs.update(refs)
if len(adverse_ids) != len(set(adverse_ids)):
    adverse_errors.append("duplicate adverse ID")
unknown_refs = adverse_refs - set(ids)
unreferenced_support = {
    str(record["id"])
    for record in records
    if record.get("kind") == "adverse_support"
} - adverse_refs
if unknown_refs:
    adverse_errors.append("unknown refs:" + ",".join(sorted(unknown_refs)))
if unreferenced_support:
    adverse_errors.append("unreferenced support:" + ",".join(sorted(unreferenced_support)))
add("adverse_ledger", not adverse_errors, adverse_errors)

tests_errors: list[str] = []
tests_doc = json_docs.get("tests.json", {})
tests_schema = json_docs.get("tests.schema.json", {})
test_rows = tests_doc.get("tests", []) if isinstance(tests_doc, dict) else []
if not isinstance(tests_doc, dict) or not isinstance(tests_schema, dict) or not isinstance(test_rows, list):
    tests_errors.append("top-level")
else:
    tests_validator = Draft202012Validator(tests_schema, format_checker=format_checker)
    for error in sorted(tests_validator.iter_errors(tests_doc), key=lambda item: (list(item.absolute_path), item.message)):
        tests_errors.append(f"{error.json_path}:{error.message}")
    test_ids = []
    for index, test in enumerate(test_rows, 1):
        if not isinstance(test, dict):
            tests_errors.append(f"row {index}:not-object")
            continue
        test_ids.append(test.get("id"))
        if test.get("id") != f"CJK-NOT-T{index:03d}":
            tests_errors.append(f"row {index}:id")
        refs = test.get("evidence_ids", [])
        if not isinstance(refs, list) or any(ref not in set(ids) for ref in refs):
            tests_errors.append(f"row {index}:evidence")
    if len(test_ids) != len(set(test_ids)):
        tests_errors.append("duplicate IDs")

fixture_stdout = b""
if not tests_errors:
    fixture_runs = []
    for _ in range(2):
        completed = subprocess.run(
            [sys.executable, "-B", str(ROOT / "fixture_runner.py")],
            cwd=ROOT,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        fixture_runs.append(completed)
    if any(run.returncode != 0 or run.stderr for run in fixture_runs):
        tests_errors.append("runner-exit")
    elif fixture_runs[0].stdout != fixture_runs[1].stdout:
        tests_errors.append("runner-not-byte-stable")
    else:
        fixture_stdout = fixture_runs[0].stdout
        try:
            fixture_result = strict_json(fixture_stdout.decode("utf-8"))
        except (UnicodeDecodeError, ValueError, json.JSONDecodeError) as exc:
            tests_errors.append(f"runner-output:{exc}")
        else:
            if (
                not isinstance(fixture_result, dict)
                or fixture_result.get("result") != "PASS"
                or fixture_result.get("tests_total") != len(test_rows)
                or fixture_result.get("tests_failed") != 0
            ):
                tests_errors.append("runner-result")
add("conformance_fixtures", not tests_errors, tests_errors)

term_errors: list[str] = []
term_example = json_docs.get("term.example.json", {})
term_schema = json_docs.get("term.schema.json", {})
if isinstance(term_example, dict) and isinstance(term_schema, dict):
    term_validator = Draft202012Validator(term_schema, format_checker=format_checker)
    term_errors.extend(
        f"{error.json_path}:{error.message}"
        for error in sorted(term_validator.iter_errors(term_example), key=lambda item: (list(item.absolute_path), item.message))
    )
    channel_refs = {
        ref
        for values in term_example.get("channels", {}).values()
        if isinstance(values, list)
        for ref in values
    }
    if not channel_refs <= set(ids):
        term_errors.append("unknown evidence channel reference")
else:
    term_errors.append("unparsed")
add("term_decision_example", not term_errors, term_errors)

doi_errors: list[str] = []
doi = json_docs.get("doi.json", {})
doi_schema = json_docs.get("doi.schema.json", {})
if isinstance(doi, dict) and isinstance(doi_schema, dict):
    validator = Draft202012Validator(doi_schema, format_checker=format_checker)
    doi_errors.extend(f"{error.json_path}:{error.message}" for error in sorted(validator.iter_errors(doi), key=lambda item: (list(item.absolute_path), item.message)))
    containing = doi.get("containing_record", {})
    if not isinstance(containing, dict):
        containing = {}
        doi_errors.append("containing record")
    if containing.get("version_doi") != f"10.5281/zenodo.{containing.get('zenodo_record_id')}":
        doi_errors.append("version DOI/id")
    if containing.get("concept_doi") != f"10.5281/zenodo.{containing.get('zenodo_concept_record_id')}":
        doi_errors.append("concept DOI/id")
    expected_identity = {
        "schema": "cjk-notation-component-publication-identity-v1",
        "title": TITLE,
        "version": VERSION,
        "publication_date": RELEASE_DATE,
        "publication_role": "component_of_existing_interlanguage_sidecar",
        "repository": REPOSITORY,
        "resource_type": "dataset",
        "access_right": "open",
        "record_license": "cc-zero",
        "creators": EXPECTED_AUTHORS,
        "keywords": EXPECTED_KEYWORDS,
        "exclusive_component_doi_claim": False,
    }
    for field, expected in expected_identity.items():
        if doi.get(field) != expected:
            doi_errors.append(f"identity:{field}")
    expected_containing = {
        "title": CONTAINING_TITLE,
        "zenodo_record_id": ZENODO_RECORD_ID,
        "zenodo_concept_record_id": ZENODO_CONCEPT_RECORD_ID,
        "version_doi": VERSION_DOI,
        "concept_doi": CONCEPT_DOI,
    }
    if containing != expected_containing:
        doi_errors.append("containing identity")
    expected_relations = {(REPOSITORY, "IsSupplementedBy", "software")}
    observed_relations = {
        (row.get("identifier"), row.get("relation"), row.get("resource_type"))
        for row in doi.get("relations", [])
        if isinstance(row, dict)
    }
    if observed_relations != expected_relations:
        doi_errors.append("relations")
else:
    doi_errors.append("unparsed")
add("doi_metadata", not doi_errors, doi_errors)

cff_errors: list[str] = []
try:
    cff = yaml.load(texts["CITATION.cff"], Loader=UniqueKeyLoader)
    cff = yaml_dates(cff)
except Exception as exc:
    cff = {}
    cff_errors.append(str(exc))
authors = [row.get("name") for row in cff.get("authors", [])] if isinstance(cff, dict) else []
concept_ids = {
    row.get("value")
    for row in cff.get("identifiers", [])
    if isinstance(row, dict) and row.get("type") == "doi"
} if isinstance(cff, dict) else set()
if not isinstance(cff, dict) or any((
    cff.get("cff-version") != "1.2.0",
    cff.get("title") != TITLE,
    cff.get("type") != "dataset",
    cff.get("version") != VERSION,
    cff.get("date-released") != RELEASE_DATE,
    cff.get("doi") != VERSION_DOI,
    cff.get("repository-code") != REPOSITORY,
    cff.get("license") != "CC0-1.0",
    authors != EXPECTED_AUTHORS,
    cff.get("keywords") != EXPECTED_KEYWORDS,
    concept_ids != {CONCEPT_DOI},
)):
    cff_errors.append("cross-field identity")
if isinstance(doi, dict) and doi.get("creators") != authors:
    cff_errors.append("DOI/CFF creator crosswalk")
add("citation_cff", not cff_errors, cff_errors)

rights_errors: list[str] = []
rights = json_docs.get("rights.json", {})
if not isinstance(rights, dict):
    rights_errors.append("unparsed")
else:
    if rights.get("record_license") != "cc-zero" or rights.get("default_license") != "CC0-1.0":
        rights_errors.append("license classes")
    exceptions = rights.get("exceptions")
    if exceptions != []:
        rights_errors.append("bundled exception set")
    references = rights.get("development_references")
    if not isinstance(references, list) or len(references) != 1:
        rights_errors.append("development reference count")
    else:
        reference = references[0]
        if (
            reference.get("name") != "Citation File Format 1.2.0 schema"
            or reference.get("license") != "CC-BY-4.0"
            or reference.get("bytes") != 63763
            or reference.get("sha256") != "0B8D22140DA702D766DF318DCFF3A91AF2F39521298DCF36D76315FD99CC169B"
            or reference.get("bundled") is not False
            or reference.get("source") != "https://github.com/citation-file-format/citation-file-format/blob/1.2.0/schema.json"
        ):
            rights_errors.append("CFF development reference identity")
if snapshots.get("LICENSE").sha256 != LICENSE_SHA256:
    rights_errors.append("CC0 legal-code identity")
if "cff.schema.json" in snapshots:
    rights_errors.append("unbundled CFF schema present")
for record in records:
    for source in record.get("sources", []):
        if isinstance(source, dict) and source.get("availability") in {"hash_only", "restricted"}:
            artifact = source.get("artifact")
            if artifact in snapshots:
                rights_errors.append(f"source artifact bundled:{artifact}")
add("rights_and_nonredistribution", not rights_errors, rights_errors)

markdown_errors: list[str] = []
for name, text in texts.items():
    if not name.endswith(".md"):
        continue
    for target in LINK_RE.findall(text):
        target = target.strip()
        parsed = urlparse(target)
        if parsed.scheme:
            if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
                markdown_errors.append(f"{name}:{target}")
            continue
        decoded = unquote(target.split("#", 1)[0])
        path = PurePosixPath(decoded)
        if (
            not decoded
            or path.is_absolute()
            or len(path.parts) != 1
            or path.parts[0] in {".", ".."}
            or "\\" in decoded
            or ":" in decoded
            or decoded not in snapshots
        ):
            markdown_errors.append(f"{name}:{target}")
add("markdown_links", not markdown_errors, markdown_errors)

security_errors: list[str] = []
for name, text in texts.items():
    if name == "cff.schema.json":
        continue
    for pattern in ABS_PATH_RES:
        if pattern.search(text):
            security_errors.append(f"{name}:path:{pattern.pattern}")
    for pattern in SECRET_RES:
        if pattern.search(text):
            security_errors.append(f"{name}:secret")
    if TASK_ID_RE.search(text):
        security_errors.append(f"{name}:task-id")
    if EMAIL_RE.search(text):
        security_errors.append(f"{name}:email")
    for match in PHONE_RE.finditer(text):
        digit_count = sum(char.isdigit() for char in match.group())
        if 9 <= digit_count <= 15:
            security_errors.append(f"{name}:phone")
    for url in URL_RE.findall(text):
        parsed = urlparse(url.rstrip(".,;"))
        if parsed.username or parsed.password:
            security_errors.append(f"{name}:URL-userinfo")
        if re.search(r"(?:^|&)(?:token|access_token|api_key|key|secret)=", parsed.query, re.I):
            security_errors.append(f"{name}:URL-secret-query")
        try:
            host = parsed.hostname
            if host and ipaddress.ip_address(host).is_private:
                security_errors.append(f"{name}:private-IP")
        except ValueError:
            pass
add("privacy_and_credentials", not security_errors, sorted(set(security_errors)))

content = "\n".join(
    text
    for name, text in texts.items()
    if name not in {"verify.py", "cff.schema.json"}
)
placeholder_hits = sorted(set(re.findall(r"\b(?:TODO|TKTK|FIXME|CHANGEME)\b", content, re.I)))
add("no_placeholders", not placeholder_hits, placeholder_hits)

dependency_errors: list[str] = []
for distribution, expected in RUNTIME_DEPENDENCIES.items():
    try:
        observed = importlib.metadata.version(distribution)
    except importlib.metadata.PackageNotFoundError:
        dependency_errors.append(f"{distribution}:missing")
        continue
    if observed != expected:
        dependency_errors.append(f"{distribution}:{observed}!={expected}")
requirements = texts.get("requirements.txt", "")
locked_blocks: dict[str, dict[str, object]] = {}
current_requirement: str | None = None
for line in requirements.splitlines():
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        continue
    if not line[:1].isspace() and "==" in stripped:
        header = stripped.removesuffix("\\").strip()
        requirement = header.split(";", 1)[0].strip()
        name, version = requirement.split("==", 1)
        normalized = name.replace("_", "-").lower()
        if normalized in locked_blocks:
            dependency_errors.append(f"{normalized}:duplicate-lock")
        locked_blocks[normalized] = {"version": version.strip(), "hashes": []}
        current_requirement = normalized
        continue
    if stripped.startswith("--hash=sha256:") and current_requirement is not None:
        value = stripped.removesuffix("\\").strip().removeprefix("--hash=sha256:")
        if not re.fullmatch(r"[a-f0-9]{64}", value):
            dependency_errors.append(f"{current_requirement}:bad-hash")
        locked_blocks[current_requirement]["hashes"].append(value)
        continue
    dependency_errors.append(f"unparsed requirement line:{stripped}")
expected_locks = {name.replace("_", "-").lower(): version for name, version in LOCKED_DEPENDENCIES.items()}
if set(locked_blocks) != set(expected_locks):
    dependency_errors.append("locked package set mismatch")
for distribution, version in expected_locks.items():
    block = locked_blocks.get(distribution, {})
    if block.get("version") != version:
        dependency_errors.append(f"{distribution}:not-locked")
    if not block.get("hashes"):
        dependency_errors.append(f"{distribution}:missing-hash")
add("dependency_lock", not dependency_errors, dependency_errors)

readme = texts.get("README.md", "")
standard = texts.get("STANDARD.md", "")
method = texts.get("METHOD.md", "")
identity_errors = []
if texts.get("VERSION", "").strip() != VERSION:
    identity_errors.append("VERSION")
for token in (TITLE, VERSION_DOI, CONCEPT_DOI, REPOSITORY):
    if token not in readme:
        identity_errors.append(f"README:{token}")
if "not a pan-CJK mathematical language" not in standard:
    identity_errors.append("scope")
if not all(token in method for token in ("independent state vector", "never emits one aggregate readiness score", "locale layer")):
    identity_errors.append("positive adoption method")
if not all(token in readme for token in ("optional", "never a publication gate", "not redistributed", "no competing Zenodo concept")):
    identity_errors.append("review/rights policy")
add("release_identity_and_scope", not identity_errors, identity_errors)

registry_errors = []
registry = json_docs.get("registry.json", {})
queries = registry.get("queries", []) if isinstance(registry, dict) else []
if len(queries) < 5 or not all(
    entry.get("github_repositories") == 0
    and entry.get("zenodo_records") == 0
    and entry.get("datacite_dois") == 0
    for entry in queries
    if isinstance(entry, dict)
):
    registry_errors.append("bounded search record")
if registry.get("exact_repository", {}) != {
    "url": REPOSITORY,
    "state": "existing_public_interlanguage_repository",
}:
    registry_errors.append("repository state")
if registry.get("existing_interlanguage_host", {}) != {
    "title": CONTAINING_TITLE,
    "concept_doi": CONCEPT_DOI,
    "observed_current_record": 21810835,
    "observed_file_count": 100,
    "disposition": "use additively; no separate CJK concept DOI",
}:
    registry_errors.append("existing host")
add("registry_search_record", not registry_errors, registry_errors)

try:
    final_snapshots = inventory(ROOT)
    stable = {
        name: (item.size, item.sha256, item.stat_key)
        for name, item in snapshots.items()
    } == {
        name: (item.size, item.sha256, item.stat_key)
        for name, item in final_snapshots.items()
    }
except PackageError:
    stable = False
add("tree_stable_during_verification", stable, len(snapshots))

failed = [check["name"] for check in checks if not check["passed"]]
manifest_sha256 = digest(manifest_data) if manifest_data else None
tree_sha256 = digest(canonical_manifest_bytes(expected_rows))
result = {
    "schema": "cjk-notation-verification-v2",
    "version": VERSION,
    "result": "PASS" if not failed else "FAIL",
    "checks_total": len(checks),
    "checks_passed": len(checks) - len(failed),
    "checks_failed": len(failed),
    "failed_checks": failed,
    "manifest_members": len(parsed_manifest),
    "manifest_sha256": manifest_sha256,
    "tree_sha256": tree_sha256,
    "verifier_sha256": snapshots["verify.py"].sha256,
    "evidence_records": len(records),
    "source_occurrences": source_occurrences,
    "unique_sources": len(source_identity),
    "adverse_records": len(adverse_rows),
    "test_records": len(test_rows),
    "checks": checks,
}
print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
raise SystemExit(0 if not failed else 1)
