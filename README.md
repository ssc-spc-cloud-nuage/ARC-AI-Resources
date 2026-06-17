# ARC-AI-Resources

Resources for Government of Canada AI users.

## Available Resources

### GitHub Copilot — Coding Instructions

Instruction files that guide GitHub Copilot behaviour for specific languages and tools.
Drop them into your `.github/instructions/` folder to activate them.

| Resource | Task tags |
|----------|-----------|
| [PowerShell Cmdlet Development Guidelines](resources/GitHub%20Copilot/Instructions/powershell.instructions.md) | powershell, code-quality |
| [Markdown Documentation and Formatting Guide](resources/GitHub%20Copilot/Instructions/markdown.instructions.md) | markdown, documentation |
| [Containerization and Docker Best Practices](resources/GitHub%20Copilot/Instructions/dockerfile.instructions.md) | docker, containerization |
| [PowerShell Pester v5 Testing Guidelines](resources/GitHub%20Copilot/Instructions/pester.instructions.md) | powershell, testing |

### VS Code — Project Settings

Ready-to-use workspace configuration files for VS Code projects.

| Resource | Task tags |
|----------|-----------|
| [VS Code Settings for PowerShell Projects](resources/GitHub%20Copilot/VS%20Code%20complementary%20settings/PowerShell%20Projects/settings.json) | editor-setup, powershell |
| [VS Code Extension Recommendations for PowerShell Projects](resources/GitHub%20Copilot/VS%20Code%20complementary%20settings/PowerShell%20Projects/extensions.json) | extensions, powershell |

### GC Secure Artifacts — Platform Services

| Resource | Task tags |
|----------|-----------|
| [GC Secure Artifacts Overview](resources/GC%20Secure%20Artifacts/gc-secure-artifacts-overview.md) | artifact-management, container-security, devsecops, software-supply-chain |

### CANChat — SSC Generative AI Chatbot

SSC's GC-approved AI chatbot for everyday unclassified work. Hosted within the GC/SSC environment, aligned with Canadian data sovereignty and GC policy requirements.

| Resource | Task tags |
|----------|-----------|
| [CANChat Overview](resources/CANChat/canchat-overview.md) | ai-assistant, generative-ai, drafting, summarization, research, productivity, responsible-ai |

## Contributing

Want to add or update a resource? See [docs/contributing.md](docs/contributing.md).

Three paths are supported:

1. **Raw drop** — add source files to `intake/raw/` and open a PR. A maintainer runs the ingest-resource skill to process them.
2. **Publish-ready PR** — add files to `resources/` with required metadata and update `catalog/resource-index.yaml`.
3. **Review-first PR** — add candidate files to `intake/normalized/` for maintainer review before publication.

The ingest-resource skill generates the governance manifest automatically when you run it.
See [.github/pull_request_template.md](.github/pull_request_template.md) for the PR checklist.

---

## For AI Agents

AI agents should start with [AGENTS.md](AGENTS.md).

Use `catalog/resource-index.yaml` for machine-readable discovery.
Use `skills/ingest-resource/SKILL.md` and `skills/validate-catalog/SKILL.md` for content workflows.

## Purpose

- Provide practical AI usage resources for Government of Canada contexts.
- Standardize ingestion so new resources are added consistently.
- Improve retrieval quality for AI agents via explicit metadata and index files.

## Repository Structure

```text
/
|- README.md
|- AGENTS.md
|- .gitignore
|- .well-known/
|  |- agent-skills.json        # machine-readable discovery entrypoint
|- .github/
|  |- copilot-instructions.md  # Copilot-specific guidance
|- resources/                  # Published resources (tool-first organization)
|- catalog/                    # Machine-readable indexes and metadata contract
|- intake/
|  |- raw/                     # Unprocessed source drops (ignored by git by default)
|  |- normalized/              # Candidate resources ready for validation/review
|  |- manifests/               # Committed governance manifests for each intake batch
|- skills/                     # Repo maintenance skills for agents
|  |- registry.yaml            # canonical skill registry
|- docs/                       # Governance and workflow documentation
```

## Agent Discovery

The same two canonical skills are exposed through multiple discovery entrypoints:

- AGENTS.md
- .github/copilot-instructions.md
- skills/registry.yaml
- .well-known/agent-skills.json

## Authoring Model

- Preferred: use skills in this repo to ingest and validate content.
- Exception: manual edits are allowed for emergency fixes.
- Goal: avoid ad hoc markdown edits that bypass metadata and validation rules.

## Pull Request Guardrails

Repository CI enforces:

- `resources/` changes require `intake/manifests/` updates
- `resources/` changes require `catalog/resource-index.yaml` updates
- Required metadata fields must be present for changed resources

## Metadata Contract

Published markdown resources should include frontmatter.
Published non-markdown resources should include sidecar metadata files named
`<filename>.meta.yaml`.

Required fields: `id`, `title`, `summary`, `tool`, `task_tags`, `last_reviewed`.

See [catalog/metadata-contract.md](catalog/metadata-contract.md) for full details.

## Risk-Based Approval Gate

Manual approval is required if any condition is true:

- `sensitivity_classification` is not `public`
- license status is missing or unclear
- `gc_policy_tags` includes `privacy`, `security`, `procurement`, or `legal`
- external source is not in `catalog/trusted-sources.yaml`

## Bilingual Approach

English metadata is required now. French metadata fields are optional and planned to
become required later.

## References

- https://github.com/ScottSyms/CANAgent
- https://github.com/gccloudone/artifacts-artefacts/
- https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
