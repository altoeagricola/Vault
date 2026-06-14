---
title: tldr
type: Tool
cover: "[[Wiki/Tools/_covers/tldr.png]]"
sources:
  - InfraKeeper
related:
  - "[[Homebrew]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

tldr is a collection of community-maintained help pages that provide simplified, example-driven alternatives to traditional man pages. Instead of dense reference documentation, each tldr page shows the most common use cases with practical, copy-paste-ready examples.

## Use Cases

- **Quick command reference** — Get the 5-10 most common uses of a command instantly
- **Learn new commands** — Understand unfamiliar tools through concrete examples rather than abstract descriptions
- **Find examples for common tasks** — Skip the man page and go straight to what you need
- **Offline reference** — Pages are cached locally after first fetch

## Examples

### Basic usage

```bash
# Show common examples for a command
tldr tar

# Show tldr page for a subcommand
tldr docker run

# Show platform-specific page
tldr --os linux systemctl
```

### Management

```bash
# Update the local cache
tldr --update

# List all available pages
tldr --list

# Search for a topic
tldr --list | grep network
```

### Example output

```bash
$ tldr tar
# tar - Archiving utility

# Create an archive from files
tar cf target.tar file1 file2 file3

# Extract an archive in the current directory
tar xf source.tar

# Create a gzipped archive
tar czf target.tar.gz file1 file2 file3

# Extract a gzipped archive in the current directory
tar xzf source.tar.gz
```

## Links

- **Official site:** https://tldr.sh
- **Repository:** https://github.com/tldr-pages/tldr
- **Documentation:** https://github.com/tldr-pages/tldr#how-do-i-use-it
