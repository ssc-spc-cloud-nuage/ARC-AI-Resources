#!/usr/bin/env python3
"""PR guardrail checks for catalog and resource workflow consistency."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from typing import Iterable

REQUIRED_KEYS = [
    "id",
    "title",
    "summary",
    "tool",
    "task_tags",
    "last_reviewed",
]


def run(cmd: list[str]) -> str:
    proc = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return proc.stdout.strip()


def changed_files(base_ref: str) -> list[str]:
    diff_range = f"origin/{base_ref}...HEAD"
    output = run(["git", "diff", "--name-only", diff_range])
    if not output:
        return []
    return [line.strip() for line in output.splitlines() if line.strip()]


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def extract_frontmatter(md_text: str) -> str:
    if not md_text.startswith("---\n"):
        return ""
    end = md_text.find("\n---\n", 4)
    if end == -1:
        return ""
    return md_text[4:end]


def has_key(yaml_text: str, key: str) -> bool:
    pattern = rf"(?m)^\s*{re.escape(key)}\s*:"
    return bool(re.search(pattern, yaml_text))


def validate_metadata_block(block: str, source: str) -> list[str]:
    errors: list[str] = []
    for key in REQUIRED_KEYS:
        if not has_key(block, key):
            errors.append(f"{source}: missing required metadata key '{key}'")
    return errors


def iter_changed_resources(paths: Iterable[str]) -> Iterable[str]:
    for path in paths:
        if path.startswith("resources/"):
            yield path


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: validate_pr_changes.py <base_ref>")
        return 2

    base_ref = sys.argv[1]

    try:
        paths = changed_files(base_ref)
    except subprocess.CalledProcessError as exc:
        print("ERROR: failed to calculate changed files")
        print(exc)
        return 2

    changed = set(paths)
    resources_changed = [p for p in iter_changed_resources(paths)]
    errors: list[str] = []

    if resources_changed:
        if not any(p.startswith("intake/manifests/") for p in changed):
            errors.append(
                "resources/ changed but no intake/manifests/ file was updated; "
                "run ingest-resource workflow and include a governance manifest"
            )
        if "catalog/resource-index.yaml" not in changed:
            errors.append(
                "resources/ changed but catalog/resource-index.yaml was not updated"
            )

    for path in resources_changed:
        # Skip deleted files and directories.
        if not os.path.isfile(path):
            continue

        if path.endswith(".meta.yaml"):
            block = read_text(path)
            errors.extend(validate_metadata_block(block, path))
            continue

        if path.endswith(".md"):
            text = read_text(path)
            frontmatter = extract_frontmatter(text)
            if not frontmatter:
                errors.append(f"{path}: missing YAML frontmatter")
                continue
            errors.extend(validate_metadata_block(frontmatter, path))
            continue

        sidecar = f"{path}.meta.yaml"
        if not os.path.isfile(sidecar):
            errors.append(
                f"{path}: non-markdown resource requires sidecar metadata file {sidecar}"
            )
            continue

        sidecar_block = read_text(sidecar)
        errors.extend(validate_metadata_block(sidecar_block, sidecar))

    if errors:
        print("PR guardrail validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("PR guardrail validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
