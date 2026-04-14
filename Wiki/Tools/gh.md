---
title: gh
type: Tool
cover: "[[Wiki/Tools/_covers/gh.png]]"
sources:
related:
  - "[[lazygit]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

gh is GitHub's official command-line tool that brings pull requests, issues, Actions, repositories, and the GitHub API directly to the terminal. It eliminates context-switching to the browser for most GitHub operations and is highly scriptable for automation workflows.

## Use Cases

- **Create and review pull requests** — Open, review, merge, and check out PRs without leaving the terminal
- **Manage issues** — Create, list, filter, and close issues from the CLI
- **Trigger and monitor Actions** — View workflow runs, trigger dispatches, and download artifacts
- **API queries** — Access any GitHub API endpoint with automatic authentication
- **Repository management** — Create, clone, fork, and configure repos

## Examples

### Pull request workflow

```bash
# Create a pull request
gh pr create --title "Add feature" --body "Description"

# List open PRs
gh pr list

# Check out a PR locally
gh pr checkout 42

# Merge a PR
gh pr merge 42 --squash
```

### Issues and Actions

```bash
# Create an issue
gh issue create --title "Bug report" --label bug

# List recent workflow runs
gh run list --limit 5

# View a specific run
gh run view 12345 --log
```

### API access

```bash
# Query the API directly
gh api repos/owner/repo/releases/latest --jq '.tag_name'

# Paginated listing
gh api --paginate repos/owner/repo/issues
```

## Links

- **Official site:** https://cli.github.com
- **Repository:** https://github.com/cli/cli
- **Documentation:** https://cli.github.com/manual/
