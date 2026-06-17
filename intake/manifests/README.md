# intake/manifests

Governance manifests are generated automatically by the ingest-resource skill.
Do not create them manually.

## Required Manifest Fields

- batch_id
- submitted_at
- submitted_by
- source_description
- file_names
- file_hashes_sha256
- sensitivity_classification
- license_status
- intended_audience
- review_decision
- reviewer

## Example

```yaml
batch_id: 2026-06-17-copilot-guides-001
submitted_at: "2026-06-17T14:30:00Z"
submitted_by: repo-admin
source_description: Internal guidance and public references for Copilot usage.

file_names:
  - guide-1.md
  - guide-2.pdf

file_hashes_sha256:
  guide-1.md: "<sha256>"
  guide-2.pdf: "<sha256>"

sensitivity_classification: public
license_status: verified
intended_audience:
  - gc-ai-users
  - platform-admins

review_decision: approved
reviewer: maintainer-name
```
