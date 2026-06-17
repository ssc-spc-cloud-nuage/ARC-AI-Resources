---
id: gc-secure-artifacts-overview
title: GC Secure Artifacts — Centralized Artifact Management for the Government of Canada
summary: >
  SSC-hosted centralized artifact registry built on JFrog Enterprise+, available to all
  federal departments. Provides secure container images via Chainguard, vulnerability
  scanning via JFrog Xray, and CI/CD integration for Python, Java, Node.js, .NET, and
  PowerShell stacks.
tool: GC Secure Artifacts
task_tags:
  - artifact-management
  - container-security
  - devsecops
  - software-supply-chain
  - chainguard
  - jfrog
last_reviewed: '2026-06-17'
audience:
  - gc-developers
  - platform-admins
  - gc-ai-users
source_urls:
  - https://github.com/gccloudone/artifacts-artefacts/
  - https://artifacts-artefacts.devops.cloud-nuage.canada.ca/
maturity: stable
---

# GC Secure Artifacts

GC Secure Artifacts is an SSC pilot initiative providing a centralized, secure artifact
management service to all Government of Canada federal departments and agencies.

Service URL: **https://artifacts-artefacts.devops.cloud-nuage.canada.ca/**

## What it offers

### JFrog Enterprise+ Platform

A centralized registry for internal builds and deployments, supporting multiple package types:

- Docker / container images
- Maven (Java)
- NPM (Node.js)
- NuGet (.NET)
- Helm charts
- Python packages

Built-in capabilities include:

- Vulnerability scanning via JFrog Xray
- Advanced access controls and repository segmentation
- Frogbot pull request security scanning
- Dependency auditing (`jf audit`)

### Chainguard Secure Base Images

Distroless, minimal, CVE-free container images pulled through to GC Artifactory.
Available to all GC teams without external registry access.

| Image | Pull path |
|-------|-----------|
| Python 3.13 | `artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/python:3.13.3` |
| OpenJDK JRE 21 | `artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/jre:openjdk-21` |
| Node.js 24 | `artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/node:24.1.0` |
| PowerShell | `artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/powershell` |
| ASP.NET Runtime | `artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/aspnet-runtime` |
| .NET Runtime | `artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/dotnet-runtime` |
| .NET SDK | `artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/dotnet-sdk` |

## Getting Access

Request access via the GC Onboarding Form:
**https://forms-formulaires.alpha.canada.ca/en/id/cmavw8p4l006eyi01cx1qtxxd**

## Quick Start

### Replace base images in Dockerfiles

```dockerfile
# Python
FROM artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/python:3.13.3

# Java
FROM artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/jre:openjdk-21

# Node.js
FROM artifacts-artefacts.devops.cloud-nuage.canada.ca/docker-chainguard-remote/ssc-spc.gc.ca/node:24.1.0
```

### Add JFrog CLI to GitHub Actions

```yaml
- name: Setup JFrog CLI
  uses: jfrog/setup-jfrog-cli@v4
  env:
    JF_URL: https://artifacts-artefacts.devops.cloud-nuage.canada.ca
    JF_USER: ${{ secrets.JFROG_USERNAME }}
    JF_ACCESS_TOKEN: ${{ secrets.JFROG_JWT_TOKEN }}

- name: Scan Dependencies
  run: jf audit --format=table

- name: Scan Container
  run: jf docker scan $IMAGE_TAG
```

### Configure JFrog CLI locally

```bash
jf config add --url=https://artifacts-artefacts.devops.cloud-nuage.canada.ca
jf rt ping
jf audit
```

### Required secrets

- `JFROG_USERNAME` — your Artifactory username
- `JFROG_JWT_TOKEN` — your Artifactory access token

## Working Examples

The source repository includes complete CI/CD examples:

```
examples/
├── java-app/          # Java + JFrog + Chainguard
├── python-app/        # Python application
├── node-app/          # Node.js application
└── .github/workflows/ # CI/CD workflow templates
```

## Additional Documentation

- [Artifactory Standards](https://github.com/gccloudone/artifacts-artefacts/blob/main/docs/artifactory-standards.md)
- [Chainguard Images](https://github.com/gccloudone/artifacts-artefacts/blob/main/docs/chainguard-images.md)
- [Quick Start Guide](https://github.com/gccloudone/artifacts-artefacts/blob/main/docs/quickstart.md)
- [FAQ](https://github.com/gccloudone/artifacts-artefacts/blob/main/docs/frequently-asked-questions.md)
- [GC Secure Artifacts Presentation (unclassified)](https://gccloudone.blob.core.windows.net/artifacts-artefacts/unclassified/gc-secure-artifacts.pptx)

## Contact

Email: devops.artifacts-artefacts.devops@ssc-spc.gc.ca
