# AGENTS.md

Cross-agent entrypoint for repository automation behavior.

## Mission

Help users find, contribute, and maintain Government of Canada AI resources using the
repository workflow and skills.

## Canonical Skills

- ingest-resource: skills/ingest-resource/SKILL.md
- validate-catalog: skills/validate-catalog/SKILL.md

## Required Order for Content Changes

1. Run ingest-resource workflow first.
2. Run validate-catalog workflow second.
3. Ensure intake/manifests/ and catalog/resource-index.yaml are updated.

## Retrieval Strategy

1. Start with catalog/resource-index.yaml for discovery.
2. Match user intent to task_tags, then refine by tool and audience.
3. Prefer published resources in resources/ for final answers.
4. Use intake/normalized/ as candidate content only, not canonical guidance.

## Contribution Strategy

When users want to add or update content:

1. Use skills/ingest-resource/SKILL.md first for add or update operations.
2. Use skills/validate-catalog/SKILL.md before proposing publication.
3. Ensure governance manifest exists in intake/manifests/.
4. Ensure catalog/resource-index.yaml is updated for published changes.
5. If a requested workflow bypasses skills, explain the policy and continue only for
   emergency fixes.

## Enforcement

The repository CI checks enforce the required outputs for the two workflows on pull
requests. If outputs are missing, the PR must fail.

- PRs that change resources/ must also include intake/manifests/ updates.
- PRs that change resources/ must update catalog/resource-index.yaml.
- Required metadata checks run in CI for changed resources.

## PR Support Rules

- External pull requests are supported.
- Contributors may submit publish-ready updates directly in resources/.
- Contributors may drop raw files in intake/raw/ and open a PR for maintainer processing.
- Raw payloads in intake/raw/ are tracked and committable in contributor PRs.
- High-risk submissions require manual approval.

## Risk Gate Rules

Require manual approval if any are true:

- sensitivity_classification is not public
- license status is missing or unclear
- gc_policy_tags includes privacy, security, procurement, or legal
- source is not trusted per catalog/trusted-sources.yaml

## Metadata Rules

- Enforce required fields: id, title, summary, tool, task_tags, last_reviewed.
- For markdown resources, use YAML frontmatter.
- For non-markdown resources, use sidecar .meta.yaml files.
- Warn on missing optional bilingual fields; do not block for now.

## Answering Users

- Explain recommendations with concrete resource links.
- Prefer concise, actionable steps.
- If source material is ambiguous, request clarification or route to review-first path.
