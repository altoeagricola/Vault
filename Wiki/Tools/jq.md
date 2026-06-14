---
title: jq
type: Tool
cover: "[[Wiki/Tools/_covers/jq.png]]"
sources:
  - InfraKeeper
related:
  - "[[yq]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

jq is a lightweight, portable command-line JSON processor with a powerful functional query language. It can slice, filter, map, and transform structured JSON data with the same ease that sed, awk, and grep handle text — making it indispensable for working with APIs and configuration files.

## Use Cases

- **Extract fields from JSON** — Pull specific values from nested JSON structures
- **Filter arrays** — Select elements matching conditions from JSON arrays
- **Transform JSON structure** — Reshape data by constructing new objects and arrays
- **Pretty-print JSON** — Format raw JSON output for readability
- **API scripting** — Pipe curl output through jq for automated data extraction

## Examples

### Basic extraction

```bash
# Extract a top-level field
echo '{"name": "Edgar", "age": 30}' | jq '.name'

# Nested field access
jq '.metadata.labels' manifest.json

# Raw string output (no quotes)
jq -r '.version' package.json
```

### Array filtering

```bash
# Select from array by condition
jq '.[] | select(.status == "running")' containers.json

# Map over array elements
jq '[.items[] | {name: .metadata.name, ns: .metadata.namespace}]' pods.json

# Count array elements
jq '.results | length' response.json
```

### API integration

```bash
# Pipe curl output through jq
curl -s https://api.github.com/repos/jqlang/jq | jq '{stars: .stargazers_count, forks: .forks_count}'

# Process paginated results
gh api --paginate repos/owner/repo/issues | jq '.[].title'
```

## Links

- **Official site:** https://jqlang.github.io/jq/
- **Repository:** https://github.com/jqlang/jq
- **Documentation:** https://jqlang.github.io/jq/manual/
