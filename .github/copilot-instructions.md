# Copilot Repository Instructions

This repository uses skill-driven maintenance for content updates.

## Required Skills

- skills/ingest-resource/SKILL.md
- skills/validate-catalog/SKILL.md

## Required Sequence

1. Ingest and normalize content.
2. Validate metadata, index integrity, and policy gates.

## Required Outputs in PRs

- intake/manifests/ updated
- catalog/resource-index.yaml updated when resources/ changes
- required metadata fields present for changed resources

For complete behavior and guardrails, follow AGENTS.md.
