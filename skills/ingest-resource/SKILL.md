---
name: ingest-resource
description: Ingest new source material into the repository using a standardized metadata-first workflow.
---

# ingest-resource

Use this skill to transform raw intake materials into normalized, publishable resources.

## Goals

- Keep ingestion consistent and repeatable.
- Ensure required metadata is present.
- Route high-risk items to manual approval.

## Inputs

Support both modes:

- Interactive mode: ask guided questions (default for humans).
- Structured mode: accept a YAML or JSON input payload (for automation).

## Workflow

### Step 1 — Scan raw intake

List files present in intake/raw/. If none, ask the human to drop source files there first.

### Step 2 — Interview the human

Ask the following questions in order. Provide a recommended answer for each.
Do not proceed to the next question until the current one is answered.

1. What is the title of this resource?
2. Write a 1–3 sentence summary.
3. Which tool or platform does this resource apply to?
   (suggest based on file content if possible)
4. What task tags describe what a user would be trying to do?
   (suggest based on file content; comma-separated list)
5. What is the sensitivity classification?
   (recommend: public; flag if anything else)
6. What is the license or copyright status?
   (recommend: verify before answering; flag if unknown)
7. Who is the intended audience?
   (recommend: gc-ai-users)
8. Do any of these apply?
   - Contains privacy-related guidance
   - Contains security controls or policies
   - Relates to procurement or legal matters
   (recommend: none; flag any that apply)
9. What are the source URLs, if any?

### Step 3 — Generate the governance manifest

Using answers from the interview:

- Generate a batch_id in the form YYYY-MM-DD-<slugified-title>-001.
- Set submitted_at to current date/time.
- Set submitted_by to the GitHub username or name provided.
- Compute SHA-256 hashes for each file in intake/raw/.
- Set review_decision to pending; set reviewer to TBD.
- Write the manifest to intake/manifests/<batch_id>.yaml.

Do not ask the human to create this file manually.

### Step 4 — Normalize content

Normalize raw files into markdown or structured files in intake/normalized/.
Apply required metadata frontmatter based on interview answers.

### Step 5 — Run risk gate checks

- sensitivity_classification not public
- license_status is unknown or unclear
- gc_policy_tags includes privacy, security, procurement, or legal
- source not in catalog/trusted-sources.yaml

If any condition is true, set publication_recommendation to approval_required.
If none, set to approved_low_risk.

### Step 6 — Update catalog draft

If approved_low_risk, add a draft entry to catalog/resource-index.yaml with the
target path in resources/.

### Step 7 — Clean up transitory files

Delete all files in intake/raw/ that were processed in this batch.
Delete all files in intake/normalized/ once they have been published to resources/
or marked approval_required (they are superseded by either the published resource
or the pending review state).

Do not delete intake/manifests/ entries — they are the permanent audit record.

## Output

- Committed manifest at intake/manifests/<batch_id>.yaml
- Published or staged resource files
- Updated catalog/resource-index.yaml (draft or final)
- intake/raw/ and intake/normalized/ cleared of processed files
- Publication recommendation: approved_low_risk or approval_required
- Validation notes for follow-up

## Guardrails

- Always generate the manifest; never ask the human to write it.
- Always clean up intake/raw/ and intake/normalized/ after processing.
- Do not delete intake/manifests/ entries.
- Do not publish directly when approval is required.
- Do not bypass required metadata fields.
- Do not commit raw payloads from intake/raw/.
