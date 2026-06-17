---
name: validate-catalog
description: Validate resource metadata, catalog consistency, and risk-gate compliance before publication.
---

# validate-catalog

Use this skill to verify that repository content remains machine-retrievable and policy-aligned.

## Validation Scope

- resources/
- catalog/resource-index.yaml
- catalog/metadata-contract.md
- intake/manifests/

## Required Checks

1. Metadata contract checks:
   - id, title, summary, tool, task_tags, last_reviewed exist and are non-empty
   - task_tags is a non-empty list
   - last_reviewed matches YYYY-MM-DD
2. Uniqueness checks:
   - resource id values are unique
3. Index checks:
   - each published resource appears in catalog/resource-index.yaml
   - each index path exists
4. Risk gate checks:
   - verify high-risk rules were applied
   - confirm manual approval evidence when required

## Severity Model

- error: required metadata missing, malformed fields, broken index path
- warning: missing optional bilingual fields or non-blocking quality hints

## Output

- Validation report with:
  - pass_fail
  - errors
  - warnings
  - recommended_fixes

## Guardrails

- Fail validation on required metadata issues.
- Warn, do not fail, on optional metadata issues.
- Never auto-fix by deleting content.
