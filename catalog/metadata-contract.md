# Resource Metadata Contract

This document defines the metadata fields used by this repository so AI agents can
find and rank resources consistently.

## Frontmatter Requirement

Published markdown resources in resources/ should include YAML frontmatter.

For non-markdown published resources (for example .json), provide a sidecar metadata file
named <filename>.meta.yaml in the same directory.

## Required Fields

- id: stable lowercase identifier, kebab-case preferred
- title: human-readable resource name in English
- summary: concise summary in English (1 to 3 sentences)
- tool: primary tool or platform name
- task_tags: list of task-focused tags used for retrieval
- last_reviewed: date in ISO format (YYYY-MM-DD)

## Optional Fields

- title_fr: French title
- summary_fr: French summary
- audience: list, such as beginner, practitioner, admin
- gc_policy_tags: list, such as privacy, security, legal, procurement
- language: language code(s), such as en or en,fr
- maturity: draft, stable, deprecated
- owner: team or maintainer
- source_urls: list of canonical source URLs

## Validation Rules

- Required fields must exist and be non-empty.
- task_tags must be a list with at least one item.
- last_reviewed must match YYYY-MM-DD.
- id values must be unique across the repository.
- Non-markdown resources must have a matching sidecar metadata file.

## Bilingual Policy

Current policy is phased bilingual support:

- English fields are required now.
- French fields are optional now and may become required later.
