# Contributing

This repository prefers skill-driven maintenance to keep metadata and indexing consistent.

External pull requests are supported for both new resources and updates.

## External PR Flow

1. Fork the repository.
2. Create a branch for your change.
3. Choose one contribution path:
	- **Publish-ready**: use the ingest-resource skill, then update resources/ and catalog/resource-index.yaml.
	- **Review-first**: use the ingest-resource skill to stage candidate content in intake/normalized/.
	- **Raw drop**: add your source files to intake/raw/ and open a PR — a maintainer will run the ingest-resource skill on your files.
4. Open a pull request using the repository PR template.

The ingest-resource skill generates the governance manifest for you.
For raw-drop PRs, the maintainer generates it during processing.

## Preferred Workflow

1. Place source material in intake/raw/.
2. Run the ingest-resource skill — it interviews you and generates the governance manifest.
3. Run the validate-catalog skill to check metadata and policy gates.
4. Publish validated resources to resources/ and update catalog/resource-index.yaml.

Note for external contributors: intake/raw/ is optional and usually local-only because
raw payloads are ignored by default.

## Manual Edits

Manual edits are allowed only for urgent fixes.

If manual edits are used:

- Preserve metadata contract compliance.
- Update last_reviewed fields.
- Update catalog/resource-index.yaml when adding or moving resources.

## Pull Request Checklist

- Required metadata fields exist for each new resource.
- Non-markdown resources include matching .meta.yaml sidecar metadata.
- Risk gate rules were applied.
- Intake manifest exists for the batch.
- Resource index includes new published entries.
- Changed files are limited to relevant paths (resources/, catalog/, intake/manifests/,
	intake/normalized/, docs/).

## Maintainer Review Notes

- High-risk submissions require explicit manual approval.
- Reviewers may request publication to intake/normalized/ first when metadata or risk
	classification is unclear.
