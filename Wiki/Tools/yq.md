---
title: yq
type: Tool
cover: "[[Wiki/Tools/_covers/yq.png]]"
sources:
related:
  - "[[jq]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

yq is a portable command-line processor for YAML, JSON, XML, and TOML files, using a jq-like syntax. It fills the gap that jq leaves for YAML-heavy workflows — particularly common in Kubernetes, Docker Compose, and CI/CD configuration management.

## Use Cases

- **Extract YAML values** — Query nested YAML structures using path expressions
- **Modify YAML in-place** — Update fields directly in YAML files without manual editing
- **Convert between formats** — Transform YAML to JSON, JSON to YAML, XML to YAML, etc.
- **Merge YAML files** — Combine multiple YAML files with merge strategies
- **Script Kubernetes manifests** — Programmatically modify Kubernetes resources in CI/CD pipelines

## Examples

### Basic extraction

```bash
# Read a value
yq '.metadata.name' deployment.yaml

# Read from a specific document in multi-doc YAML
yq 'select(documentIndex == 1)' multi.yaml

# Output as JSON
yq -o json '.' config.yaml
```

### In-place modification

```bash
# Update a field
yq -i '.spec.replicas = 3' deployment.yaml

# Add an element to an array
yq -i '.spec.containers[0].env += [{"name": "DEBUG", "value": "true"}]' pod.yaml

# Delete a field
yq -i 'del(.metadata.annotations)' service.yaml
```

### Format conversion and merge

```bash
# YAML to JSON
yq -o json '.' config.yaml > config.json

# JSON to YAML
yq -P '.' data.json > data.yaml

# Merge two YAML files (second overrides first)
yq eval-all 'select(fileIndex == 0) * select(fileIndex == 1)' base.yaml override.yaml
```

## Links

- **Repository:** https://github.com/mikefarah/yq
- **Documentation:** https://mikefarah.gitbook.io/yq/
