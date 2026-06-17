# intake/raw

Drop unprocessed source artifacts here before ingestion.

## Contribution Paths

### Path A — Let the maintainer process it

1. Add your source files to this folder.
2. Commit them and open a PR.
3. A maintainer runs the ingest-resource skill on your files and handles normalization,
   manifest generation, and publication.

This is the lowest-friction path for external contributors.

### Path B — Process it yourself with the skill

1. Add your source files to this folder.
2. Run the **ingest-resource** skill — it will ask you a few questions and handle
   everything else, including cleanup.

## Git Tracking Policy

- Raw files are tracked and may be committed in contributor PRs.
- Local users who prefer not to commit raw files can add a personal exclusion:
  `echo 'intake/raw/**' >> .git/info/exclude`
- Sensitive or proprietary payloads should never be committed.
