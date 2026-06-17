# intake/raw

Drop unprocessed source artifacts here before ingestion.

## Git Tracking Policy

- Raw payloads are ignored by git by default.
- This folder exists in git only to preserve structure and policy.
- Do not commit sensitive or proprietary payloads.

## Expected Usage

1. Add your source files to this folder.
2. Run the **ingest-resource** skill — it will ask you a few questions and handle everything else, including cleanup.
