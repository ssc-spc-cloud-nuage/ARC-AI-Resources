# AGENTS.md

Cross-agent entrypoint for repository automation behavior.

## Canonical Skills

- ingest-resource: skills/ingest-resource/SKILL.md
- validate-catalog: skills/validate-catalog/SKILL.md

## Required Order for Content Changes

1. Run ingest-resource workflow first.
2. Run validate-catalog workflow second.
3. Ensure intake/manifests/ and catalog/resource-index.yaml are updated.

## Enforcement

The repository CI checks enforce the required outputs for the two workflows on pull
requests. If outputs are missing, the PR must fail.

## Additional Guidance

For detailed behavior and guardrails, read AGENT.md.
