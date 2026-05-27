from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
from datetime import date
from pathlib import Path
from typing import Any
from urllib.parse import quote

import requests


BASE_URL = os.environ.get("ZENODO_BASE_URL", "https://zenodo.org").rstrip("/")
TOKEN_ENV = "ZENODO_ACCESS_TOKEN"
FIFTY_GB = 50_000_000_000
MAX_FILES = 100


def require_token() -> str:
    token = os.environ.get(TOKEN_ENV)
    if not token:
        raise SystemExit(f"{TOKEN_ENV} is not set.")
    return token


def headers(content_type: str | None = None) -> dict[str, str]:
    result = {"Authorization": f"Bearer {require_token()}"}
    if content_type:
        result["Content-Type"] = content_type
    return result


def api(method: str, path_or_url: str, *, payload: Any | None = None) -> Any:
    url = path_or_url if path_or_url.startswith("http") else f"{BASE_URL}{path_or_url}"
    response = requests.request(method, url, headers=headers("application/json") if payload is not None else headers(), json=payload)
    if response.status_code >= 400:
        raise SystemExit(f"HTTP {response.status_code} on {method} {url}\n{response.text}")
    if response.text:
        return response.json()
    return None


def read_json(path: str | None) -> Any:
    if not path:
        return None
    return json.loads(Path(path).read_text(encoding="utf-8"))


def normalized_metadata(metadata: dict[str, Any]) -> dict[str, Any]:
    cleaned = dict(metadata)
    prereserve = cleaned.get("prereserve_doi")
    if isinstance(prereserve, dict) and prereserve.get("doi"):
        cleaned["doi"] = prereserve["doi"]
    cleaned.setdefault("publication_date", date.today().isoformat())
    cleaned.setdefault("access_right", "open")
    return cleaned


def deposition_url(deposition_id: int) -> str:
    return f"/api/deposit/depositions/{deposition_id}"


def get_deposition(deposition_id: int) -> dict[str, Any]:
    return api("GET", deposition_url(deposition_id))


def get_bucket_url(deposition_id: int) -> str:
    deposition = get_deposition(deposition_id)
    bucket = deposition.get("links", {}).get("bucket")
    if not bucket:
        raise SystemExit(f"Deposition {deposition_id} has no links.bucket. Is it an editable draft?")
    return bucket.rstrip("/")


def local_file_stats(paths: list[Path]) -> dict[str, Any]:
    missing = [str(path) for path in paths if not path.exists()]
    if missing:
        raise SystemExit("Missing files:\n" + "\n".join(missing))
    total = sum(path.stat().st_size for path in paths)
    return {
        "count": len(paths),
        "total_bytes": total,
        "over_file_limit": len(paths) > MAX_FILES,
        "over_default_record_quota": total > FIFTY_GB,
    }


def list_depositions(args: argparse.Namespace) -> int:
    query = f"page={args.page}&size={args.size}"
    print(json.dumps(api("GET", f"/api/deposit/depositions?{query}"), indent=2, ensure_ascii=False))
    return 0


def get_cmd(args: argparse.Namespace) -> int:
    print(json.dumps(get_deposition(args.id), indent=2, ensure_ascii=False))
    return 0


def create_draft(args: argparse.Namespace) -> int:
    root = api("POST", "/api/deposit/depositions", payload={})
    deposition_id = int(root["id"])
    metadata = read_json(args.metadata_json)
    if metadata:
        api("PUT", deposition_url(deposition_id), payload={"metadata": normalized_metadata(metadata)})
    print(json.dumps(get_deposition(deposition_id), indent=2, ensure_ascii=False))
    return 0


def update_metadata(args: argparse.Namespace) -> int:
    metadata = read_json(args.metadata_json)
    if not isinstance(metadata, dict):
        raise SystemExit("metadata-json must contain an object.")
    print(json.dumps(api("PUT", deposition_url(args.id), payload={"metadata": normalized_metadata(metadata)}), indent=2, ensure_ascii=False))
    return 0


def delete_all_files(deposition_id: int) -> list[dict[str, Any]]:
    files = api("GET", f"/api/deposit/depositions/{deposition_id}/files") or []
    deleted: list[dict[str, Any]] = []
    for item in files:
        api("DELETE", f"/api/deposit/depositions/{deposition_id}/files/{item['id']}")
        deleted.append({"filename": item.get("filename"), "id": item.get("id")})
    return deleted


def upload_one(bucket_url: str, path: Path, remote_name: str | None = None) -> dict[str, Any]:
    filename = remote_name or path.name
    target = f"{bucket_url}/{quote(filename)}"
    with path.open("rb") as handle:
        response = requests.put(target, data=handle, headers=headers("application/octet-stream"))
    if response.status_code >= 400:
        raise SystemExit(f"HTTP {response.status_code} while uploading {path} to {target}\n{response.text}")
    return response.json()


def upload_files(args: argparse.Namespace) -> int:
    paths = [Path(raw).resolve() for raw in args.files]
    stats = local_file_stats(paths)
    if stats["over_file_limit"] and not args.allow_over_limits:
        raise SystemExit(f"Refusing to upload {stats['count']} files; package into <= {MAX_FILES} files or pass --allow-over-limits.")
    if stats["over_default_record_quota"] and not args.allow_over_limits:
        raise SystemExit(f"Refusing to upload {stats['total_bytes']} bytes; default record quota is {FIFTY_GB} bytes.")

    deleted = delete_all_files(args.id) if args.replace else []
    bucket = get_bucket_url(args.id)
    uploaded = []
    for path in paths:
        uploaded.append(upload_one(bucket, path))
    result = {"deposition_id": args.id, "deleted": deleted, "uploaded": uploaded, "local_stats": stats}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


def new_version(args: argparse.Namespace) -> int:
    result = api("POST", f"/api/deposit/depositions/{args.id}/actions/newversion")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


def edit(args: argparse.Namespace) -> int:
    result = api("POST", f"/api/deposit/depositions/{args.id}/actions/edit")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


def publish(args: argparse.Namespace) -> int:
    if not args.yes_publish:
        raise SystemExit("Publishing is irreversible for files. Re-run with --yes-publish.")
    current = get_deposition(args.id)
    metadata = normalized_metadata(current.get("metadata", {}))
    api("PUT", deposition_url(args.id), payload={"metadata": metadata})
    print(json.dumps(api("POST", f"/api/deposit/depositions/{args.id}/actions/publish"), indent=2, ensure_ascii=False))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Zenodo helper for the old-manuscript corpus release workflow.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("list")
    p.add_argument("--page", type=int, default=1)
    p.add_argument("--size", type=int, default=25)
    p.set_defaults(func=list_depositions)

    p = sub.add_parser("get")
    p.add_argument("id", type=int)
    p.set_defaults(func=get_cmd)

    p = sub.add_parser("create-draft")
    p.add_argument("--metadata-json", required=True)
    p.set_defaults(func=create_draft)

    p = sub.add_parser("update-metadata")
    p.add_argument("id", type=int)
    p.add_argument("--metadata-json", required=True)
    p.set_defaults(func=update_metadata)

    p = sub.add_parser("upload")
    p.add_argument("id", type=int)
    p.add_argument("files", nargs="+")
    p.add_argument("--replace", action="store_true", help="Delete existing draft files before upload.")
    p.add_argument("--allow-over-limits", action="store_true", help="Bypass local file-count/size guardrails.")
    p.set_defaults(func=upload_files)

    p = sub.add_parser("new-version")
    p.add_argument("id", type=int, help="Latest deposition id, not concept id.")
    p.set_defaults(func=new_version)

    p = sub.add_parser("edit")
    p.add_argument("id", type=int, help="Published deposition id to open for metadata editing.")
    p.set_defaults(func=edit)

    p = sub.add_parser("publish")
    p.add_argument("id", type=int)
    p.add_argument("--yes-publish", action="store_true")
    p.set_defaults(func=publish)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
