#!/usr/bin/env python3
"""Validate repository structure, cross-references, and evidence coverage.

This validator intentionally does not hard-code model IDs, prices, or token limits.
It verifies that canonical records are internally coherent and are backed by
field-level claims tied to official provider sources. Remote sources are reviewed
by the sync workflow; this offline validator never claims to re-fetch them.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from urllib.parse import urlparse
import json
import os
import re
import sys
from typing import Any, Iterable

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_ROOT
TODAY = date.fromisoformat(os.environ.get("VALIDATION_DATE", "2026-07-14"))

errors: list[str] = []
warnings: list[str] = []


def err(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


CANONICAL_KINDS = {
    "text-chat",
    "multimodal-chat",
    "image-generation",
    "speech-generation",
    "transcription",
    "realtime-audio",
    "music-generation",
    "video-generation",
}

PROVIDER_DOMAINS: dict[str, set[str]] = {
    "openai": {"developers.openai.com"},
    "gemini": {"ai.google.dev"},
    "deepseek": {"api-docs.deepseek.com"},
    "aliyun-bailian-cn": {"help.aliyun.com"},
    "aliyun-bailian-intl": {"www.alibabacloud.com"},
    "minimax-cn": {"platform.minimaxi.com"},
    "minimax-intl": {"platform.minimax.io"},
}

CATALOG_HEADER = [
    "Request Kind", "API Model", "Display Name", "Primary API Surface",
    "Provider Lifecycle", "Provider Shutdown At", "Provider Earliest Retirement At",
    "Local Selection", "Selection Reason", "Is Default", "Verification State",
    "Review Freshness", "Last Verified At", "Official Context Display",
    "Exact Context Tokens", "Official Max Input Display", "Exact Max Input Tokens",
    "Official Max Output Display", "Exact Max Output Tokens",
    "Recommended Max Output Tokens", "Limit Unit Convention", "Is Moving Alias",
    "Alias Target At Verification", "Alias Mode", "Alias Target Verified At",
    "Replacement Model", "Evidence Refs",
]
CAPABILITY_HEADER = [
    "Request Kind", "API Model", "API Surface", "API Version",
    "Supports Non-Stream", "Supports Stream", "Thinking Mode", "Thinking Default",
    "Thinking Budget Field", "Thinking Budget Default", "Temperature Mode",
    "Temperature Defaults", "Json Object Mode", "Json Schema Mode",
    "Tool Calling Mode", "Strict Tool Schema Mode", "Parallel Tool Calls",
    "Tool Choice When Thinking", "Required Tool-History Fields",
    "Reasoning Effort Field", "Reasoning Effort Values", "Reasoning Summary Field",
    "Reasoning Output Visibility", "Supports Image Input", "Supports Seed",
    "Supports Image Size", "Supports Image Count", "Supports Duration Seconds",
    "Evidence Refs", "Notes",
]
URL_HEADER = [
    "Request Kind", "Model Scope", "API Surface", "API Version", "Endpoint Kind",
    "HTTP Method", "Base URL", "Request Path Template", "Request URL Template",
    "Stream Variant", "Request URL Status", "Last Verified At", "Evidence Refs", "Notes",
]
PRICING_HEADER = [
    "Request Kind", "API Model", "API Surface", "API Version", "Billing Region",
    "Deployment Scope", "Serving Region", "Service Tier", "Price Currency",
    "Price Unit", "Metered Side", "Metered Item", "Price Condition", "Unit Price",
    "Effective At", "Expires At", "Pricing Status", "Last Verified At",
    "Evidence Refs", "Notes",
]
PROFILE_HEADER = [
    "Profile Key", "Display Name", "Provider", "Purpose", "Profile Status",
    "Endpoint Kind", "Base URL", "API Key Ref", "API Key Source", "Default Text Model",
    "Default Multimodal Model", "Default Image Model", "Default Music Model",
    "Allowed Request Kinds", "Default Route Map", "Allowed Surface Versions",
    "Model Allowlist", "Capability Restrictions", "Billing Region", "Deployment Scope",
    "Serving Region", "Last Verified At", "Evidence Refs", "Notes",
]
ROLE_HEADER = [
    "Provider", "API Surface", "API Version", "Accepted Roles", "Developer Role",
    "System Role", "Assistant Tool History", "Normalization Policy", "Last Verified At",
    "Evidence Refs", "Notes",
]

EXPECTED_HEADERS = {
    "model-catalog.md": CATALOG_HEADER,
    "capability-matrix.md": CAPABILITY_HEADER,
    "request-urls.md": URL_HEADER,
    "pricing-matrix.md": PRICING_HEADER,
    "connection-profiles.md": PROFILE_HEADER,
    "role-support-matrix.md": ROLE_HEADER,
}
FIRST_COLUMN = {
    "model-catalog.md": "Request Kind",
    "capability-matrix.md": "Request Kind",
    "request-urls.md": "Request Kind",
    "pricing-matrix.md": "Request Kind",
    "connection-profiles.md": "Profile Key",
    "role-support-matrix.md": "Provider",
}
KEY_FIELDS = {
    "model-catalog.md": ["Request Kind", "API Model"],
    "capability-matrix.md": ["Request Kind", "API Model", "API Surface", "API Version"],
    "request-urls.md": ["Request Kind", "Model Scope", "API Surface", "API Version"],
    "pricing-matrix.md": [
        "Request Kind", "API Model", "API Surface", "API Version", "Billing Region",
        "Deployment Scope", "Serving Region", "Service Tier", "Metered Side",
        "Metered Item", "Price Condition",
    ],
    "connection-profiles.md": ["Profile Key"],
    "role-support-matrix.md": ["Provider", "API Surface", "API Version"],
}
EXTERNAL_FIELDS = {
    "model-catalog.md": {
        "API Model", "Primary API Surface", "Provider Lifecycle", "Provider Shutdown At",
        "Provider Earliest Retirement At", "Official Context Display", "Exact Context Tokens",
        "Official Max Input Display", "Exact Max Input Tokens", "Official Max Output Display",
        "Exact Max Output Tokens", "Recommended Max Output Tokens", "Limit Unit Convention",
        "Is Moving Alias", "Alias Target At Verification", "Alias Mode",
        "Alias Target Verified At",
    },
    "capability-matrix.md": set(CAPABILITY_HEADER[1:28]),
    "request-urls.md": {
        "Model Scope", "API Surface", "API Version", "Endpoint Kind", "HTTP Method",
        "Base URL", "Request Path Template", "Request URL Template", "Stream Variant",
    },
    "pricing-matrix.md": {
        "API Model", "API Surface", "API Version", "Billing Region", "Deployment Scope",
        "Serving Region", "Service Tier", "Price Currency", "Price Unit", "Metered Side",
        "Metered Item", "Price Condition", "Unit Price", "Effective At", "Expires At",
    },
    "connection-profiles.md": {
        "Endpoint Kind", "Base URL", "Billing Region", "Deployment Scope", "Serving Region",
    },
    "role-support-matrix.md": {
        "API Surface", "API Version", "Accepted Roles", "Developer Role", "System Role",
        "Assistant Tool History", "Normalization Policy",
    },
}


# ---------- Markdown parsing ----------

def split_md_row(line: str) -> list[str]:
    s = line.strip()
    if not s.startswith("|"):
        return []
    s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    cells: list[str] = []
    cur: list[str] = []
    escaped = False
    for ch in s:
        if escaped:
            cur.append(ch)
            escaped = False
        elif ch == "\\":
            escaped = True
        elif ch == "|":
            cells.append("".join(cur).strip().strip("`"))
            cur = []
        else:
            cur.append(ch)
    if escaped:
        cur.append("\\")
    cells.append("".join(cur).strip().strip("`"))
    return cells


def is_separator_row(line: str) -> bool:
    cells = split_md_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c.strip()) for c in cells)


def scan_tables(path: Path) -> list[tuple[int, list[str], list[dict[str, str]]]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    found: list[tuple[int, list[str], list[dict[str, str]]]] = []
    i = 0
    while i < len(lines) - 1:
        if lines[i].lstrip().startswith("|") and is_separator_row(lines[i + 1]):
            header = split_md_row(lines[i])
            separator = split_md_row(lines[i + 1])
            if len(separator) != len(header):
                err(f"{path.relative_to(ROOT)}:{i+2}: table separator has {len(separator)} columns; expected {len(header)}")
            rows: list[dict[str, str]] = []
            j = i + 2
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                values = split_md_row(lines[j])
                if len(values) != len(header):
                    err(f"{path.relative_to(ROOT)}:{j+1}: table row has {len(values)} columns; expected {len(header)}")
                else:
                    row = dict(zip(header, values))
                    row["__line__"] = str(j + 1)
                    rows.append(row)
                j += 1
            found.append((i + 1, header, rows))
            i = j
        else:
            i += 1
    return found


def canonical_table(path: Path, expected_header: list[str]) -> list[dict[str, str]]:
    matches = [(line, h, rows) for line, h, rows in scan_tables(path) if h and h[0] == expected_header[0] and "Evidence Refs" in h]
    if len(matches) != 1:
        err(f"{path.relative_to(ROOT)}: expected exactly one canonical table, found {len(matches)}")
        return []
    line, header, rows = matches[0]
    if header != expected_header:
        err(f"{path.relative_to(ROOT)}:{line}: canonical header differs from schema\n  got: {header}\n  expected: {expected_header}")
    return rows


def row_key(row: dict[str, str], fields: Iterable[str]) -> tuple[str, ...]:
    return tuple(row.get(f, "") for f in fields)


def ref_ids(cell: str) -> list[str]:
    return [x.strip() for x in cell.split(",") if x.strip()]


# ---------- Generic helpers ----------

def parse_dateish(value: str) -> date | None:
    if value in {"", "none", "unknown", "n/a", "unverified"}:
        return None
    try:
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            return date.fromisoformat(value)
        normalized = value.replace("Z", "+00:00")
        return datetime.fromisoformat(normalized).astimezone(timezone.utc).date()
    except ValueError:
        return None


def require_date(value: str, label: str, *, allow_sentinels: set[str] | None = None) -> date | None:
    sentinels = allow_sentinels or set()
    if value in sentinels:
        return None
    parsed = parse_dateish(value)
    if parsed is None:
        err(f"{label}: invalid date/timestamp {value!r}")
    return parsed


def parse_decimal(value: str) -> Decimal | None:
    if value in {"unknown", "n/a", "none", ""}:
        return None
    try:
        return Decimal(value)
    except InvalidOperation:
        return None


def scope_covers(scope: str, model: str, selected_models: set[str], reviewed_models: set[str]) -> bool:
    if scope in {"all-selected", "catalog-selected"}:
        return model in selected_models
    if scope == "all-reviewed":
        return model in reviewed_models
    return model in {x.strip() for x in scope.split(",") if x.strip()}


def list_items(value: str) -> list[str]:
    if value in {"", "none", "n/a"}:
        return []
    return [x.strip() for x in value.split(",") if x.strip()]


def parse_route_map(value: str, label: str) -> dict[str, tuple[str, str]]:
    if value in {"", "none"}:
        return {}
    routes: dict[str, tuple[str, str]] = {}
    for part in value.split(";"):
        if not part.strip():
            continue
        if "=" not in part:
            err(f"{label}: malformed route {part!r}")
            continue
        kind, target = (x.strip() for x in part.split("=", 1))
        if "@" not in target:
            err(f"{label}: route lacks @version: {part!r}")
            continue
        surface, version = target.rsplit("@", 1)
        if kind in routes:
            err(f"{label}: duplicate route for {kind}")
        routes[kind] = (surface, version)
    return routes


def parse_surface_versions(value: str, label: str) -> set[tuple[str, str]]:
    if value in {"", "none"}:
        return set()
    out: set[tuple[str, str]] = set()
    for item in value.split(","):
        item = item.strip()
        if "@" not in item:
            err(f"{label}: malformed surface@version {item!r}")
            continue
        surface, version = item.rsplit("@", 1)
        if not surface or not version:
            err(f"{label}: malformed surface@version {item!r}")
            continue
        out.add((surface, version))
    return out


# ---------- Basic file hygiene ----------
if not ROOT.exists():
    err(f"repository root does not exist: {ROOT}")

for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or ".git" in path.parts:
        continue
    data = path.read_bytes()
    if path.suffix.lower() in {".md", ".yaml", ".yml", ".json", ".py", ".txt"} or path.name == ".gitattributes":
        if b"\r\n" in data:
            err(f"CRLF found: {path.relative_to(ROOT)}")
        try:
            data.decode("utf-8")
        except UnicodeDecodeError as exc:
            err(f"not UTF-8: {path.relative_to(ROOT)}: {exc}")

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None

for path in sorted(list(ROOT.rglob("*.yaml")) + list(ROOT.rglob("*.yml"))):
    if ".git" in path.parts:
        continue
    if yaml is None:
        err("PyYAML is required to validate YAML files")
        break
    try:
        yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - dependent on parser details
        err(f"invalid YAML {path.relative_to(ROOT)}: {exc}")

# Parse every Markdown table once for shape checking.
for path in sorted(ROOT.rglob("*.md")):
    if ".git" not in path.parts:
        scan_tables(path)

# Relative Markdown links must resolve. Image links and anchors are included.
link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
for path in sorted(ROOT.rglob("*.md")):
    if ".git" in path.parts:
        continue
    for raw in link_pattern.findall(path.read_text(encoding="utf-8")):
        target = raw.strip().split("#", 1)[0].strip()
        if not target or re.match(r"^[a-z][a-z0-9+.-]*://", target, re.I) or target.startswith("mailto:"):
            continue
        resolved = (path.parent / target).resolve()
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            err(f"{path.relative_to(ROOT)}: relative link escapes repository: {target}")
            continue
        if not resolved.exists():
            err(f"{path.relative_to(ROOT)}: missing relative link target: {target}")

# Path-like code spans are also contracts in this repository. Validate only
# unambiguous root-relative or explicit/provider-relative paths; ordinary code
# snippets and illustrative bare filenames are intentionally excluded.
code_path_pattern = re.compile(r"`([^`\n]+(?:\.md|\.json|\.yaml|\.yml|\.py))`")
for path in sorted(ROOT.rglob("*.md")):
    if ".git" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    in_provider_skill = any(part.startswith("skill-llm-") for part in path.parts)
    for raw in code_path_pattern.findall(text):
        target = raw.strip().split("#", 1)[0].strip()
        if (
            not target
            or re.search(r"\s", target)
            or re.match(r"^[a-z][a-z0-9+.-]*://", target, re.I)
            or any(ch in target for ch in "*<>{}")
        ):
            continue
        if target.startswith(("LLM/", "tools/")):
            resolved = (ROOT / target).resolve()
        elif target.startswith(("./", "../")):
            resolved = (path.parent / target).resolve()
        elif in_provider_skill and target.startswith(("references/", "agents/")):
            # Provider SKILL.md files use paths relative to the provider root;
            # reference documents normally use explicit ../ paths instead.
            provider_root = next(parent for parent in [path.parent, *path.parents] if parent.name.startswith("skill-llm-"))
            resolved = (provider_root / target).resolve()
        else:
            continue
        try:
            resolved.relative_to(ROOT)
        except ValueError:
            err(f"{path.relative_to(ROOT)}: code-span path escapes repository: {target}")
            continue
        if not resolved.exists():
            err(f"{path.relative_to(ROOT)}: missing code-span path target: {target}")

# No generated/cache artifacts belong in the package.
for path in ROOT.rglob("*"):
    if ".git" in path.parts:
        continue
    if path.name == "__pycache__" or path.suffix == ".pyc" or path.name == "catalog-data.json":
        err(f"temporary/generated artifact must not be shipped: {path.relative_to(ROOT)}")


# ---------- Load provider tables ----------
provider_dirs = sorted(ROOT.glob("LLM/skill-llm-*"))
if not provider_dirs:
    err("no provider skill directories found")

provider_data: dict[str, dict[str, Any]] = {}
required_provider_files = {
    "SKILL.md",
    "agents/openai.yaml",
    "references/model-catalog.md",
    "references/capability-matrix.md",
    "references/request-urls.md",
    "references/pricing-matrix.md",
    "references/connection-profiles.md",
    "references/role-support-matrix.md",
    "references/model-sync.md",
}

all_canonical_rows: dict[tuple[str, str, tuple[str, ...]], dict[str, str]] = {}
row_locations: dict[tuple[str, str, tuple[str, ...]], str] = {}
referenced_sets: Counter[str] = Counter()

for provider_dir in provider_dirs:
    provider = provider_dir.name.removeprefix("skill-llm-")
    missing = [str(provider_dir / f) for f in required_provider_files if not (provider_dir / f).exists()]
    for item in missing:
        err(f"missing required provider file: {Path(item).relative_to(ROOT)}")

    # Every skill entrypoint must have parseable YAML frontmatter whose name is
    # the exact directory name. This catches routing drift before packaging.
    skill_path = provider_dir / "SKILL.md"
    if skill_path.exists():
        skill_text = skill_path.read_text(encoding="utf-8")
        skill_lines = skill_text.splitlines()
        if not skill_lines or skill_lines[0].strip() != "---":
            err(f"{skill_path.relative_to(ROOT)}: missing opening YAML frontmatter delimiter")
        else:
            try:
                closing = next(i for i, line in enumerate(skill_lines[1:], start=1) if line.strip() == "---")
            except StopIteration:
                err(f"{skill_path.relative_to(ROOT)}: missing closing YAML frontmatter delimiter")
            else:
                if yaml is None:
                    err("PyYAML is required to validate SKILL.md frontmatter")
                else:
                    try:
                        frontmatter = yaml.safe_load("\n".join(skill_lines[1:closing]))
                    except Exception as exc:  # pragma: no cover - parser-dependent
                        err(f"invalid SKILL.md frontmatter {skill_path.relative_to(ROOT)}: {exc}")
                        frontmatter = None
                    if not isinstance(frontmatter, dict):
                        err(f"{skill_path.relative_to(ROOT)}: frontmatter must be a mapping")
                    else:
                        expected_name = provider_dir.name
                        if frontmatter.get("name") != expected_name:
                            err(f"{skill_path.relative_to(ROOT)}: frontmatter name must be {expected_name!r}")
                        description = frontmatter.get("description")
                        if not isinstance(description, str) or not description.strip():
                            err(f"{skill_path.relative_to(ROOT)}: frontmatter description must be a non-empty string")

    # Validate the installed-agent descriptor rather than merely parsing YAML.
    agent_path = provider_dir / "agents/openai.yaml"
    if agent_path.exists() and yaml is not None:
        try:
            agent_doc = yaml.safe_load(agent_path.read_text(encoding="utf-8"))
        except Exception:
            agent_doc = None  # The generic YAML pass already reports syntax details.
        if isinstance(agent_doc, dict):
            interface = agent_doc.get("interface")
            policy = agent_doc.get("policy")
            if not isinstance(interface, dict):
                err(f"{agent_path.relative_to(ROOT)}: interface must be a mapping")
            else:
                for field in ("display_name", "short_description", "default_prompt"):
                    value = interface.get(field)
                    if not isinstance(value, str) or not value.strip():
                        err(f"{agent_path.relative_to(ROOT)}: interface.{field} must be a non-empty string")
                default_prompt = interface.get("default_prompt")
                expected_token = f"${provider_dir.name}"
                if isinstance(default_prompt, str) and expected_token not in default_prompt:
                    err(f"{agent_path.relative_to(ROOT)}: default_prompt must reference {expected_token}")
            if not isinstance(policy, dict):
                err(f"{agent_path.relative_to(ROOT)}: policy must be a mapping")
            elif not isinstance(policy.get("allow_implicit_invocation"), bool):
                err(f"{agent_path.relative_to(ROOT)}: policy.allow_implicit_invocation must be boolean")
        elif agent_doc is not None:
            err(f"{agent_path.relative_to(ROOT)}: agent descriptor must be a mapping")

    tables: dict[str, list[dict[str, str]]] = {}
    for doc, header in EXPECTED_HEADERS.items():
        path = provider_dir / "references" / doc
        tables[doc] = canonical_table(path, header) if path.exists() else []
        keys = KEY_FIELDS[doc]
        seen: set[tuple[str, ...]] = set()
        for row in tables[doc]:
            key = row_key(row, keys)
            label = f"{path.relative_to(ROOT)}:{row.get('__line__')}"
            if key in seen:
                err(f"{label}: duplicate canonical key {key}")
            seen.add(key)
            global_key = (provider, doc, key)
            if global_key in all_canonical_rows:
                err(f"{label}: duplicate global canonical record {global_key}")
            all_canonical_rows[global_key] = row
            row_locations[global_key] = label
            refs = ref_ids(row.get("Evidence Refs", ""))
            if not refs:
                err(f"{label}: Evidence Refs is empty")
            for ref in refs:
                referenced_sets[ref] += 1
    provider_data[provider] = {"dir": provider_dir, "tables": tables}

unknown_provider_keys = set(provider_data) - set(PROVIDER_DOMAINS)
for provider in sorted(unknown_provider_keys):
    err(f"no official-domain allowlist configured for provider {provider}")


# ---------- Evidence manifest ----------
manifest_path = ROOT / "LLM/_evidence/evidence.json"
manifest: dict[str, Any] = {}
if not manifest_path.exists():
    err("missing LLM/_evidence/evidence.json")
else:
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        err(f"invalid evidence manifest JSON: {exc}")

sets_by_id: dict[str, dict[str, Any]] = {}
claims_by_id: dict[str, dict[str, Any]] = {}
claim_membership: Counter[str] = Counter()

if manifest:
    if manifest.get("schema_version") != 2:
        err(f"evidence manifest schema_version must be 2, got {manifest.get('schema_version')!r}")
    if manifest.get("coverage_mode") != "curated-allowlist":
        err(f"evidence manifest coverage_mode must be curated-allowlist, got {manifest.get('coverage_mode')!r}")
    generated = require_date(str(manifest.get("generated_at", "")), "evidence.generated_at")
    if generated and generated > TODAY:
        err(f"evidence.generated_at is in the future: {generated}")
    evidence_sets = manifest.get("evidence_sets")
    claims = manifest.get("claims")
    if not isinstance(evidence_sets, list):
        err("evidence_sets must be a list")
        evidence_sets = []
    if not isinstance(claims, list):
        err("claims must be a list")
        claims = []

    for item in evidence_sets:
        if not isinstance(item, dict):
            err("evidence set must be an object")
            continue
        sid = item.get("evidence_set_id")
        if not isinstance(sid, str) or not sid.startswith("evset-"):
            err(f"invalid evidence_set_id: {sid!r}")
            continue
        if sid in sets_by_id:
            err(f"duplicate evidence_set_id: {sid}")
        sets_by_id[sid] = item
        if not isinstance(item.get("record_key"), dict):
            err(f"{sid}: record_key must be an object")
        ids = item.get("claim_ids")
        if not isinstance(ids, list) or not ids or not all(isinstance(x, str) for x in ids):
            err(f"{sid}: claim_ids must be a non-empty string list")
        else:
            for cid in ids:
                claim_membership[cid] += 1

    allowed_source_types = {
        "model-card", "endpoint-reference", "pricing", "lifecycle", "release-notes",
        "official-index", "derived",
    }
    for claim in claims:
        if not isinstance(claim, dict):
            err("claim must be an object")
            continue
        cid = claim.get("claim_id")
        if not isinstance(cid, str) or not cid.startswith("evset-"):
            err(f"invalid claim_id: {cid!r}")
            continue
        if cid in claims_by_id:
            err(f"duplicate claim_id: {cid}")
        claims_by_id[cid] = claim
        provider = claim.get("provider")
        if provider not in provider_data:
            err(f"{cid}: unknown provider {provider!r}")
        value = claim.get("value")
        if isinstance(value, (dict, list)) or value is None:
            err(f"{cid}: claim value must be a scalar string/number/bool")
        source_url = claim.get("source_url")
        if not isinstance(source_url, str) or not source_url.startswith("https://"):
            err(f"{cid}: source_url must be official HTTPS URL")
        else:
            host = (urlparse(source_url).hostname or "").lower()
            allowed_hosts = PROVIDER_DOMAINS.get(str(provider), set())
            if host not in allowed_hosts:
                err(f"{cid}: source host {host!r} is not allowed for {provider}")
        if claim.get("source_type") not in allowed_source_types:
            err(f"{cid}: invalid source_type {claim.get('source_type')!r}")
        if not isinstance(claim.get("source_locator"), str) or not claim.get("source_locator", "").strip():
            err(f"{cid}: source_locator is required")
        verified = require_date(str(claim.get("verified_at", "")), f"{cid}.verified_at")
        if verified and verified > TODAY:
            err(f"{cid}: verified_at is in the future: {verified}")
        for field_name in ("effective_at", "expires_at"):
            raw = str(claim.get(field_name, ""))
            require_date(raw, f"{cid}.{field_name}", allow_sentinels={"unknown", "none", "n/a"})
        if claim.get("conflict_state") not in {"none", "open", "resolved"}:
            err(f"{cid}: invalid conflict_state {claim.get('conflict_state')!r}")
        if claim.get("conflict_state") == "open":
            err(f"{cid}: open evidence conflict must fail closed before release")
        deps = claim.get("depends_on")
        if not isinstance(deps, list) or not all(isinstance(x, str) for x in deps):
            err(f"{cid}: depends_on must be a string list")
            deps = []
        if claim.get("source_type") == "derived":
            if not deps:
                err(f"{cid}: derived claim requires dependencies")
            if claim.get("derivation") in {None, "", "none"}:
                err(f"{cid}: derived claim requires a derivation description")
        elif claim.get("derivation") not in {None, "", "none"}:
            warn(f"{cid}: non-derived claim has derivation text")

    for sid, item in sets_by_id.items():
        provider = item.get("provider")
        doc_path = item.get("document_path")
        key_obj = item.get("record_key")
        if provider not in provider_data:
            err(f"{sid}: unknown provider {provider!r}")
            continue
        if not isinstance(doc_path, str) or not (ROOT / doc_path).is_file():
            err(f"{sid}: document_path does not exist: {doc_path!r}")
            continue
        doc = Path(doc_path).name
        if doc not in KEY_FIELDS:
            err(f"{sid}: unsupported canonical document {doc}")
            continue
        if not isinstance(key_obj, dict):
            continue
        expected_fields = KEY_FIELDS[doc]
        if list(key_obj.keys()) != expected_fields:
            err(f"{sid}: record_key fields must be {expected_fields}, got {list(key_obj.keys())}")
        key = tuple(str(key_obj.get(k, "")) for k in expected_fields)
        record = all_canonical_rows.get((provider, doc, key))
        if record is None:
            err(f"{sid}: no matching canonical row for {provider}/{doc}/{key}")
            continue
        if sid not in ref_ids(record.get("Evidence Refs", "")):
            err(f"{sid}: matching row does not reference this evidence set")
        for cid in item.get("claim_ids", []):
            claim = claims_by_id.get(cid)
            if claim is None:
                err(f"{sid}: missing claim {cid}")
                continue
            if claim.get("provider") != provider or claim.get("document_path") != doc_path or claim.get("record_key") != key_obj:
                err(f"{cid}: claim identity differs from containing evidence set {sid}")
            field = claim.get("field")
            if field not in record:
                err(f"{cid}: field {field!r} not present in canonical row")
            elif str(claim.get("value")) != record[field]:
                err(f"{cid}: claim value {claim.get('value')!r} != row value {record[field]!r}")

        # Every non-sentinel external field in a row must have a matching claim.
        claims_for_field = {claims_by_id[cid].get("field") for cid in item.get("claim_ids", []) if cid in claims_by_id}
        for field in EXTERNAL_FIELDS[doc]:
            value = record.get(field, "")
            skip = value in {"", "unknown", "n/a", "unverified"}
            skip |= field in {"API Surface", "API Version"} and value in {
                "all-documented-surfaces", "all-documented-versions", "provider-default"
            }
            skip |= field in {"Provider Shutdown At", "Provider Earliest Retirement At"} and value == "none"
            skip |= field == "Is Moving Alias" and value == "no"
            skip |= field in {"Alias Target At Verification", "Alias Mode", "Alias Target Verified At"} and record.get("Is Moving Alias") != "yes"
            if not skip and field not in claims_for_field:
                err(f"{sid}: row field {field!r}={value!r} lacks a field-level claim")

    for ref, count in referenced_sets.items():
        if ref not in sets_by_id:
            err(f"canonical row references missing evidence set {ref}")
        if count != 1:
            err(f"evidence set {ref} is referenced by {count} canonical rows; expected exactly 1")
    for sid in sets_by_id:
        if referenced_sets[sid] == 0:
            err(f"unreferenced evidence set: {sid}")
    for cid in claims_by_id:
        if claim_membership[cid] == 0:
            err(f"claim is not included in any evidence set: {cid}")
        elif claim_membership[cid] != 1:
            err(f"claim belongs to {claim_membership[cid]} evidence sets: {cid}")
    for cid, claim in claims_by_id.items():
        for dep in claim.get("depends_on", []):
            if dep not in claims_by_id:
                err(f"{cid}: missing dependency {dep}")

    # Dependency cycles.
    visiting: set[str] = set()
    visited: set[str] = set()
    def visit(cid: str, stack: list[str]) -> None:
        if cid in visited:
            return
        if cid in visiting:
            err(f"evidence dependency cycle: {' -> '.join(stack + [cid])}")
            return
        visiting.add(cid)
        for dep in claims_by_id.get(cid, {}).get("depends_on", []):
            visit(dep, stack + [cid])
        visiting.remove(cid)
        visited.add(cid)
    for cid in claims_by_id:
        visit(cid, [])


# ---------- Provider-level semantic and cross-reference validation ----------
for provider, info in provider_data.items():
    tables = info["tables"]
    catalog = tables["model-catalog.md"]
    caps = tables["capability-matrix.md"]
    urls = tables["request-urls.md"]
    prices = tables["pricing-matrix.md"]
    profiles = tables["connection-profiles.md"]
    roles = tables["role-support-matrix.md"]

    catalog_by_key = {(r["Request Kind"], r["API Model"]): r for r in catalog}
    selected_by_kind: dict[str, set[str]] = defaultdict(set)
    reviewed_by_kind: dict[str, set[str]] = defaultdict(set)
    defaults_by_kind: dict[str, list[str]] = defaultdict(list)

    lifecycle_allowed = {"stable", "preview", "scheduled-deprecated", "deprecated", "shutdown", "removed", "unknown"}
    selection_allowed = {"selected", "not-selected", "unreviewed"}
    verification_allowed = {"verified", "inherited", "conflicted", "unknown"}
    freshness_allowed = {"current", "stale", "unreviewed"}
    unit_allowed = {"exact-integer", "decimal", "binary", "provider-unspecified", "n/a"}

    for row in catalog:
        loc = row_locations[(provider, "model-catalog.md", row_key(row, KEY_FIELDS["model-catalog.md"]))]
        kind = row["Request Kind"]
        model = row["API Model"]
        if kind not in CANONICAL_KINDS:
            err(f"{loc}: non-canonical Request Kind {kind!r}")
        if not model or "," in model:
            err(f"{loc}: API Model must be one exact non-empty ID")
        if "," in row["Primary API Surface"]:
            err(f"{loc}: Primary API Surface must be one exact surface")
        if row["Provider Lifecycle"] not in lifecycle_allowed:
            err(f"{loc}: invalid Provider Lifecycle {row['Provider Lifecycle']!r}")
        if row["Local Selection"] not in selection_allowed:
            err(f"{loc}: invalid Local Selection {row['Local Selection']!r}")
        if row["Verification State"] not in verification_allowed:
            err(f"{loc}: invalid Verification State {row['Verification State']!r}")
        if row["Review Freshness"] not in freshness_allowed:
            err(f"{loc}: invalid Review Freshness {row['Review Freshness']!r}")
        if row["Limit Unit Convention"] not in unit_allowed:
            err(f"{loc}: invalid Limit Unit Convention {row['Limit Unit Convention']!r}")
        if row["Is Default"] not in {"yes", "no"}:
            err(f"{loc}: Is Default must be yes/no")
        if row["Is Moving Alias"] not in {"yes", "no"}:
            err(f"{loc}: Is Moving Alias must be yes/no")
        verified_at = require_date(row["Last Verified At"], f"{loc} Last Verified At", allow_sentinels={"unverified"})
        if verified_at and verified_at > TODAY:
            err(f"{loc}: Last Verified At is in the future")
        if row["Local Selection"] == "selected":
            selected_by_kind[kind].add(model)
            if row["Provider Lifecycle"] not in {"stable", "preview", "scheduled-deprecated"}:
                err(f"{loc}: selected model has non-callable lifecycle {row['Provider Lifecycle']}")
            if row["Verification State"] != "verified" or row["Review Freshness"] != "current":
                err(f"{loc}: selected model must be verified and current")
            if row["Is Default"] == "yes":
                defaults_by_kind[kind].append(model)
        else:
            if not row["Selection Reason"].strip():
                err(f"{loc}: non-selected row requires Selection Reason")
            if row["Is Default"] == "yes":
                err(f"{loc}: non-selected row cannot be default")
        if row["Verification State"] == "verified":
            reviewed_by_kind[kind].add(model)

        shutdown = require_date(row["Provider Shutdown At"], f"{loc} Provider Shutdown At", allow_sentinels={"none", "unknown"})
        earliest = require_date(row["Provider Earliest Retirement At"], f"{loc} Provider Earliest Retirement At", allow_sentinels={"none", "unknown"})
        lifecycle = row["Provider Lifecycle"]
        if lifecycle == "scheduled-deprecated" and not shutdown and not earliest:
            err(f"{loc}: scheduled-deprecated requires exact shutdown or earliest retirement")
        if lifecycle == "shutdown":
            if not shutdown:
                err(f"{loc}: shutdown lifecycle requires Provider Shutdown At")
            elif shutdown > TODAY:
                err(f"{loc}: shutdown lifecycle date is still in the future")
            if row["Local Selection"] == "selected":
                err(f"{loc}: shutdown model cannot be selected")
        if lifecycle in {"stable", "preview"} and shutdown:
            err(f"{loc}: {lifecycle} model cannot have exact Provider Shutdown At")
        if shutdown and earliest and earliest > shutdown:
            err(f"{loc}: earliest retirement is after exact shutdown")
        if lifecycle == "scheduled-deprecated" and row["Local Selection"] == "selected" and row["Replacement Model"] in {"none", "unknown", ""}:
            err(f"{loc}: selected scheduled-deprecated row requires Replacement Model")

        moving = row["Is Moving Alias"] == "yes"
        if moving:
            if row["Alias Target At Verification"] in {"none", "unknown", ""}:
                err(f"{loc}: moving alias requires exact Alias Target At Verification")
            if row["Alias Mode"] in {"n/a", "unknown", ""}:
                err(f"{loc}: moving alias requires Alias Mode")
            alias_date = require_date(row["Alias Target Verified At"], f"{loc} Alias Target Verified At", allow_sentinels={"unverified", "n/a"})
            if alias_date and alias_date > TODAY:
                err(f"{loc}: Alias Target Verified At is in the future")
        else:
            if row["Alias Target At Verification"] not in {"none", "n/a"}:
                err(f"{loc}: non-alias row must not carry alias target")
            if row["Alias Mode"] != "n/a" or row["Alias Target Verified At"] != "n/a":
                err(f"{loc}: non-alias row must use n/a alias mode/date")

        # Token display/exact consistency.
        pairs = [
            ("Official Context Display", "Exact Context Tokens"),
            ("Official Max Input Display", "Exact Max Input Tokens"),
            ("Official Max Output Display", "Exact Max Output Tokens"),
        ]
        convention = row["Limit Unit Convention"]
        exact_values: dict[str, int | None] = {}
        for display_field, exact_field in pairs:
            display = row[display_field]
            exact = row[exact_field]
            if exact not in {"unknown", "n/a"} and not exact.isdigit():
                err(f"{loc}: {exact_field} must be integer, unknown, or n/a")
                exact_num = None
            else:
                exact_num = int(exact) if exact.isdigit() else None
            exact_values[exact_field] = exact_num
            if exact_num is not None and exact_num <= 0:
                err(f"{loc}: {exact_field} must be positive")
            compact = display.replace(",", "")
            if convention == "exact-integer" and re.fullmatch(r"\d+", compact):
                if exact_num != int(compact):
                    err(f"{loc}: {exact_field} does not match exact official display {display}")
            if convention == "decimal" and re.fullmatch(r"\d+(?:\.\d+)?[KM]", compact, re.I):
                multiplier = Decimal(1000 if compact[-1].upper() == "K" else 1_000_000)
                expected = Decimal(compact[:-1]) * multiplier
                if expected != expected.to_integral_value() or exact_num != int(expected):
                    err(f"{loc}: {exact_field} does not match decimal expansion of {display}")
            if convention == "provider-unspecified" and re.fullmatch(r"\d+(?:\.\d+)?[KM]", compact, re.I) and exact != "unknown":
                err(f"{loc}: ambiguous provider display {display} must keep {exact_field}=unknown")
        recommended = row["Recommended Max Output Tokens"]
        if recommended not in {"unknown", "n/a"} and not recommended.isdigit():
            err(f"{loc}: Recommended Max Output Tokens must be integer, unknown, or n/a")
        if recommended.isdigit() and exact_values["Exact Max Output Tokens"] is not None:
            if int(recommended) > int(exact_values["Exact Max Output Tokens"]):
                err(f"{loc}: recommended max output exceeds exact maximum")

    for kind, models in selected_by_kind.items():
        if len(defaults_by_kind[kind]) != 1:
            err(f"{provider}: selected request kind {kind} must have exactly one default; got {defaults_by_kind[kind]}")

    # Capability rows.
    cap_keys: set[tuple[str, str, str, str]] = set()
    for row in caps:
        key = (row["Request Kind"], row["API Model"], row["API Surface"], row["API Version"])
        loc = row_locations[(provider, "capability-matrix.md", key)]
        cap_keys.add(key)
        if row["Request Kind"] not in CANONICAL_KINDS:
            err(f"{loc}: non-canonical Request Kind")
        if (row["Request Kind"], row["API Model"]) not in catalog_by_key:
            err(f"{loc}: capability model missing from catalog")
        if not row["API Surface"] or "," in row["API Surface"]:
            err(f"{loc}: API Surface must be one exact value")
        if not row["API Version"] or "," in row["API Version"]:
            err(f"{loc}: API Version must be one exact value")
        if row["Strict Tool Schema Mode"] == "verified":
            beta_like = "beta" in row["API Surface"].lower() or "beta" in row["API Version"].lower()
            if provider == "deepseek" and not beta_like:
                err(f"{loc}: DeepSeek strict tool schema is verified only on beta surface/version")
        thinking_capable = row["Thinking Mode"] in {"mixed", "always-on"}
        if provider == "deepseek" and thinking_capable:
            if row["Tool Choice When Thinking"] != "unsupported":
                err(f"{loc}: DeepSeek thinking rows must reject tool_choice")
            history = row["Required Tool-History Fields"].lower()
            for required in ("reasoning_content", "assistant.content(non-null)"):
                if required not in history:
                    err(f"{loc}: DeepSeek thinking row missing required history field {required}")

        selected_models = selected_by_kind.get(row["Request Kind"], set())
        reviewed_models = reviewed_by_kind.get(row["Request Kind"], set())
        matching_urls = [u for u in urls if u["Request Kind"] == row["Request Kind"] and u["API Surface"] == row["API Surface"] and u["API Version"] == row["API Version"] and scope_covers(u["Model Scope"], row["API Model"], selected_models, reviewed_models)]
        if not matching_urls:
            err(f"{loc}: no request URL row covers exact model/surface/version")
        if row["Request Kind"] in {"text-chat", "multimodal-chat"}:
            if not any(r["API Surface"] == row["API Surface"] and r["API Version"] == row["API Version"] for r in roles):
                err(f"{loc}: message-based capability lacks exact role-support row")

    # URL rows.
    url_keys = {(r["Request Kind"], r["API Surface"], r["API Version"]): r for r in urls}
    for row in urls:
        key = row_key(row, KEY_FIELDS["request-urls.md"])
        loc = row_locations[(provider, "request-urls.md", key)]
        if row["Request Kind"] not in CANONICAL_KINDS:
            err(f"{loc}: non-canonical Request Kind")
        if not row["API Surface"] or "," in row["API Surface"] or not row["API Version"] or "," in row["API Version"]:
            err(f"{loc}: URL row must use one exact surface and version")
        if row["HTTP Method"] not in {"GET", "POST", "PUT", "PATCH", "DELETE"}:
            err(f"{loc}: unsupported HTTP method {row['HTTP Method']!r}")
        if row["Request URL Status"] not in {"verified", "unknown"}:
            err(f"{loc}: invalid Request URL Status")
        if row["Request URL Status"] == "verified":
            if row["Request Path Template"] in {"unknown", "", "n/a"} or row["Request URL Template"] in {"unknown", "", "n/a"}:
                err(f"{loc}: verified URL row must have path and URL templates")
            if not (row["Request Path Template"].startswith("/") or row["Request Path Template"].startswith("http")):
                err(f"{loc}: Request Path Template must start with / or be an absolute URL")
        if row["Base URL"] not in {"{Profile.Base URL}", "unknown"} and not row["Base URL"].startswith("https://"):
            err(f"{loc}: Base URL must be HTTPS, profile placeholder, or unknown")
        if "api_key=" in row["Request URL Template"].lower() or "key=" in row["Request URL Template"].lower():
            err(f"{loc}: URL template must not embed credential query parameters")
        # Scope must refer to at least one catalog model unless it is a documented sentinel.
        scope = row["Model Scope"]
        if scope not in {"all-selected", "all-reviewed", "catalog-selected"}:
            models = list_items(scope)
            if not models:
                err(f"{loc}: Model Scope is empty")
            for model in models:
                if (row["Request Kind"], model) not in catalog_by_key:
                    err(f"{loc}: scoped model missing from catalog: {model}")

    # Role rows.
    role_keys: set[tuple[str, str]] = set()
    for row in roles:
        key = row_key(row, KEY_FIELDS["role-support-matrix.md"])
        loc = row_locations[(provider, "role-support-matrix.md", key)]
        if row["Provider"] != provider:
            err(f"{loc}: Provider cell must equal directory provider {provider}")
        sv = (row["API Surface"], row["API Version"])
        if sv in role_keys:
            err(f"{loc}: duplicate role surface/version")
        role_keys.add(sv)
        if "," in row["API Surface"] or "," in row["API Version"]:
            err(f"{loc}: role row must use exact surface/version")
        accepted = list_items(row["Accepted Roles"])
        if not accepted and row["Accepted Roles"] != "n/a":
            err(f"{loc}: Accepted Roles must be explicit or n/a")
        if row["Developer Role"] not in {"verified", "unsupported", "unknown", "n/a"}:
            err(f"{loc}: invalid Developer Role state")
        if row["System Role"] not in {"verified", "unsupported", "unknown", "n/a"}:
            err(f"{loc}: invalid System Role state")

    # Pricing rows.
    for row in prices:
        key = row_key(row, KEY_FIELDS["pricing-matrix.md"])
        loc = row_locations[(provider, "pricing-matrix.md", key)]
        if row["Request Kind"] not in CANONICAL_KINDS:
            err(f"{loc}: non-canonical Request Kind")
        if (row["Request Kind"], row["API Model"]) not in catalog_by_key:
            err(f"{loc}: pricing model missing from catalog")
        if row["Pricing Status"] not in {"current", "unknown"}:
            err(f"{loc}: invalid Pricing Status")
        if row["Pricing Status"] == "current":
            for f in ("Billing Region", "Deployment Scope", "Serving Region", "Service Tier", "Price Currency", "Price Unit"):
                if row[f] in {"", "unknown", "n/a"}:
                    err(f"{loc}: current pricing requires exact {f}")
            if parse_decimal(row["Unit Price"]) is None:
                err(f"{loc}: current Unit Price must be numeric")
            effective = require_date(row["Effective At"], f"{loc} Effective At", allow_sentinels={"unknown", "none"})
            expires = require_date(row["Expires At"], f"{loc} Expires At", allow_sentinels={"unknown", "none"})
            if effective and effective > TODAY:
                err(f"{loc}: current price is not yet effective")
            if expires and expires < TODAY:
                err(f"{loc}: expired price cannot remain current")
            if effective and expires and effective > expires:
                err(f"{loc}: Effective At is after Expires At")
        if provider == "aliyun-bailian-intl" and row["Pricing Status"] == "current":
            if row["Billing Region"] == "international" or row["Serving Region"] == "international":
                err(f"{loc}: Aliyun International current price requires exact billing/serving region")

    # Profiles.
    defaults_field = {
        "text-chat": "Default Text Model",
        "multimodal-chat": "Default Multimodal Model",
        "image-generation": "Default Image Model",
        "music-generation": "Default Music Model",
    }
    for row in profiles:
        key = row_key(row, KEY_FIELDS["connection-profiles.md"])
        loc = row_locations[(provider, "connection-profiles.md", key)]
        if row["Provider"] != provider:
            err(f"{loc}: profile Provider must equal {provider}")
        if row["Profile Status"] not in {"active", "template", "disabled"}:
            err(f"{loc}: invalid Profile Status")
        if row["Base URL"].startswith("http://"):
            err(f"{loc}: profile Base URL must use HTTPS")
        if re.search(r"(sk-|api[_-]?key\s*=|bearer\s+)[A-Za-z0-9]", row["Base URL"], re.I):
            err(f"{loc}: profile Base URL appears to contain a secret")
        allowed_kinds = set(list_items(row["Allowed Request Kinds"]))
        if row["Allowed Request Kinds"] == "none":
            allowed_kinds = set()
        invalid_kinds = allowed_kinds - CANONICAL_KINDS
        if invalid_kinds:
            err(f"{loc}: non-canonical allowed request kinds {sorted(invalid_kinds)}")
        routes = parse_route_map(row["Default Route Map"], loc)
        allowed_sv = parse_surface_versions(row["Allowed Surface Versions"], loc)
        if row["Profile Status"] == "disabled":
            if allowed_kinds or routes or allowed_sv:
                err(f"{loc}: disabled profile must not enable kinds, routes, or surface versions")
        for kind, (surface, version) in routes.items():
            if kind not in allowed_kinds:
                err(f"{loc}: route kind {kind} is not in Allowed Request Kinds")
            if (surface, version) not in allowed_sv:
                err(f"{loc}: default route {surface}@{version} is not allowed")
            model_field = defaults_field.get(kind)
            model = row.get(model_field, "none") if model_field else "none"
            if model == "none":
                err(f"{loc}: default route for {kind} has no default model field")
            elif model not in selected_by_kind.get(kind, set()):
                err(f"{loc}: default model {model} is not selected for {kind}")
            if not any(c[0] == kind and c[1] == model and c[2] == surface and c[3] == version for c in cap_keys):
                err(f"{loc}: default route lacks exact capability row for {kind}/{model}/{surface}@{version}")
            selected_models = selected_by_kind.get(kind, set())
            reviewed_models = reviewed_by_kind.get(kind, set())
            if not any(u["Request Kind"] == kind and u["API Surface"] == surface and u["API Version"] == version and scope_covers(u["Model Scope"], model, selected_models, reviewed_models) and u["Request URL Status"] == "verified" for u in urls):
                err(f"{loc}: default route lacks verified URL row")
        for kind, field in defaults_field.items():
            model = row[field]
            if model != "none":
                if kind not in allowed_kinds:
                    err(f"{loc}: {field} is set but {kind} is not allowed")
                if model not in selected_by_kind.get(kind, set()):
                    err(f"{loc}: {field} {model} is not selected for {kind}")
                if kind not in routes:
                    err(f"{loc}: {field} is set but no default route exists for {kind}")
        for kind in routes:
            if kind not in defaults_field:
                warn(f"{loc}: no standard default-model column exists for routed kind {kind}")
        for surface, version in allowed_sv:
            if not any(u["API Surface"] == surface and u["API Version"] == version for u in urls):
                err(f"{loc}: allowed surface/version has no URL row: {surface}@{version}")
        allowlist = row["Model Allowlist"]
        if allowlist not in {"catalog-selected", "none"}:
            selected_all = set().union(*selected_by_kind.values()) if selected_by_kind else set()
            for model in list_items(allowlist):
                if model not in selected_all:
                    err(f"{loc}: allowlisted model is not selected: {model}")
        if row["Profile Status"] != "disabled":
            for field in ("Billing Region", "Deployment Scope", "Serving Region"):
                if row[field] in {"", "unknown", "n/a"}:
                    err(f"{loc}: enabled/template profile requires exact {field}")

    # Selected catalog models need at least one capability row; selected kinds need a usable profile.
    for kind, models in selected_by_kind.items():
        for model in models:
            if not any(c[0] == kind and c[1] == model for c in cap_keys):
                err(f"{provider}: selected model lacks capability rows: {kind}/{model}")
        if not any(kind in set(list_items(p["Allowed Request Kinds"])) and p["Profile Status"] != "disabled" for p in profiles):
            err(f"{provider}: selected request kind {kind} has no enabled/template profile")

    # Primary surface of every selected model must be represented in capability rows.
    for row in catalog:
        if row["Local Selection"] == "selected":
            if not any(c[0] == row["Request Kind"] and c[1] == row["API Model"] and c[2] == row["Primary API Surface"] for c in cap_keys):
                err(f"{provider}: selected model primary surface lacks capability row: {row['Request Kind']}/{row['API Model']}/{row['Primary API Surface']}")


# ---------- Legacy compatibility views ----------
legacy_kind = {
    "text-chat": "chat",
    "multimodal-chat": "vision",
    "image-generation": "imaging",
    "music-generation": "music",
}
for provider, info in provider_data.items():
    provider_dir = info["dir"]
    catalog_path = provider_dir / "references/model-catalog.md"
    tables = scan_tables(catalog_path)
    legacy_tables = [(h, rows) for _, h, rows in tables if h and h[0] == "Model Type" and "Catalog Status" in h]
    if len(legacy_tables) != 1:
        err(f"{catalog_path.relative_to(ROOT)}: expected one Legacy Compatibility View")
    else:
        _, legacy_rows = legacy_tables[0]
        canonical = info["tables"]["model-catalog.md"]
        expected_keys = {(legacy_kind[r["Request Kind"]], r["API Model"]) for r in canonical if r["Request Kind"] in legacy_kind}
        got_keys = {(r["Model Type"], r["API Model"]) for r in legacy_rows}
        if expected_keys != got_keys:
            err(f"{catalog_path.relative_to(ROOT)}: legacy model keys differ from canonical registry")
        canonical_map = {(legacy_kind[r["Request Kind"]], r["API Model"]): r for r in canonical if r["Request Kind"] in legacy_kind}
        for row in legacy_rows:
            c = canonical_map.get((row["Model Type"], row["API Model"]))
            if not c:
                continue
            checks = {
                "Selection Status": c["Local Selection"],
                "Is Default": c["Is Default"],
                "Verification State": c["Verification State"],
                "Last Verified At": c["Last Verified At"],
                "Context Window Tokens": c["Exact Context Tokens"],
                "Max Input Tokens": c["Exact Max Input Tokens"],
                "Max Output Tokens": c["Exact Max Output Tokens"],
            }
            for field, expected in checks.items():
                if row.get(field) != expected:
                    err(f"{catalog_path.relative_to(ROOT)}:{row.get('__line__')}: legacy {field}={row.get(field)!r}, expected {expected!r}")
            if c["Provider Lifecycle"] in {"stable", "preview"}:
                expected_status = "active"
            elif c["Provider Lifecycle"] in {"shutdown", "removed"}:
                expected_status = "removed"
            else:
                expected_status = "deprecated"
            if row.get("Catalog Status") != expected_status:
                err(f"{catalog_path.relative_to(ROOT)}:{row.get('__line__')}: legacy Catalog Status must derive from provider lifecycle")

    profile_path = provider_dir / "references/connection-profiles.md"
    tables = scan_tables(profile_path)
    legacy_profiles = [(h, rows) for _, h, rows in tables if h and h[0] == "Profile Key" and "Default Chat Model" in h and "Evidence Refs" not in h]
    if len(legacy_profiles) != 1:
        err(f"{profile_path.relative_to(ROOT)}: expected one legacy profile table")
    else:
        _, legacy_rows = legacy_profiles[0]
        canonical = {r["Profile Key"]: r for r in info["tables"]["connection-profiles.md"]}
        if set(canonical) != {r["Profile Key"] for r in legacy_rows}:
            err(f"{profile_path.relative_to(ROOT)}: legacy profile keys differ from canonical profiles")
        for row in legacy_rows:
            c = canonical.get(row["Profile Key"])
            if not c:
                continue
            direct = {
                "Provider": c["Provider"], "Purpose": c["Purpose"], "Profile Status": c["Profile Status"],
                "Endpoint Kind": c["Endpoint Kind"], "Base URL": c["Base URL"], "API Key Ref": c["API Key Ref"],
                "API Key Source": c["API Key Source"], "Default Chat Model": c["Default Text Model"],
                "Default Vision Model": c["Default Multimodal Model"], "Default Imaging Model": c["Default Image Model"],
                "Default Music Model": c["Default Music Model"], "Model Allowlist": c["Model Allowlist"],
                "Capability Restrictions": c["Capability Restrictions"], "Last Verified At": c["Last Verified At"],
            }
            for field, expected in direct.items():
                if row.get(field) != expected:
                    err(f"{profile_path.relative_to(ROOT)}:{row.get('__line__')}: legacy {field} differs from canonical")
            expected_kinds = ",".join(legacy_kind[k] for k in list_items(c["Allowed Request Kinds"]) if k in legacy_kind) or "none"
            if row.get("Allowed Request Kinds") != expected_kinds:
                err(f"{profile_path.relative_to(ROOT)}:{row.get('__line__')}: legacy Allowed Request Kinds differs from canonical")
            expected_surfaces = ",".join(item.rsplit("@", 1)[0] for item in list_items(c["Allowed Surface Versions"])) or "none"
            if row.get("Allowed API Surfaces") != expected_surfaces:
                err(f"{profile_path.relative_to(ROOT)}:{row.get('__line__')}: legacy Allowed API Surfaces differs from canonical")


# ---------- Repository-level semantic scans ----------
text_files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts and p.suffix.lower() in {".md", ".yaml", ".yml", ".py", ".json"}]
for path in text_files:
    if path.resolve() == Path(__file__).resolve():
        continue
    text = path.read_text(encoding="utf-8")
    if "music-generation-generation" in text:
        err(f"{path.relative_to(ROOT)}: duplicated request-kind suffix")
    if "shared RequestKind adds video" in text:
        err(f"{path.relative_to(ROOT)}: stale video/request-kind wording")
    if "MODEL-MIGRATION-2026-07-13" in text or "VALIDATION-2026-07-13" in text:
        err(f"{path.relative_to(ROOT)}: stale dated document reference")
    if "developers.openai.com/api/reference/chat/create-chat-completion" in text:
        err(f"{path.relative_to(ROOT)}: stale OpenAI API reference URL")
    if re.search(r"must not use scripts|do not use scripts|禁止.{0,12}脚本", text, re.I):
        err(f"{path.relative_to(ROOT)}: blanket automation ban conflicts with sync policy")

for stale in (ROOT / "MODEL-MIGRATION-2026-07-13.md", ROOT / "VALIDATION-2026-07-13.md"):
    if stale.exists():
        err(f"stale superseded file still exists: {stale.relative_to(ROOT)}")

# Required root documentation and versioned shared schemas.
for rel in [
    "README.md", "QUICKSTART.md", "COMMANDS.md", "MODEL-MIGRATION-2026-07-14.md",
    "VALIDATION-2026-07-14.md", "LLM/_shared/model-catalog-schema.md",
    "LLM/_shared/capability-matrix-schema.md", "LLM/_shared/pricing-matrix-schema.md",
    "LLM/_shared/request-url-matrix-schema.md", "LLM/_shared/connection-profile-schema.md",
    "LLM/_shared/evidence-manifest-schema.md", "LLM/_shared/role-support-matrix-schema.md",
]:
    if not (ROOT / rel).is_file():
        err(f"missing required repository document: {rel}")

# Stable deterministic summary for CI and humans.
for message in sorted(set(errors)):
    print(f"ERROR: {message}")
for message in sorted(set(warnings)):
    print(f"WARNING: {message}")
print(f"errors={len(set(errors))} warnings={len(set(warnings))}")
sys.exit(1 if errors else 0)
