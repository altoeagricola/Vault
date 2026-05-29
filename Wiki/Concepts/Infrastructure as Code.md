---
title: Infrastructure as Code
type: Concept
sources:
  - "InfraKeeper"
related:
  - "[[Docker Compose]]"
  - "[[Docker]]"
  - "[[Proxmox VE]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

Infrastructure as Code (IaC) is the practice of defining and managing infrastructure through machine-readable configuration files rather than manual processes. Instead of clicking through UIs or running ad-hoc commands, you declare the desired state in code — version-controlled, reviewable, and reproducible.

## Why It Matters

- **Reproducibility** — Rebuild an entire environment from scratch by running the same configs
- **Version control** — Track every change to infrastructure in git, with history and rollback
- **Consistency** — Eliminate configuration drift between environments (dev, staging, prod)
- **Documentation as code** — The config files *are* the documentation of what's deployed and how

## Spectrum of IaC

IaC exists on a spectrum from simple scripts to full declarative systems:

| Level | Example | Approach |
|-------|---------|----------|
| Scripts | Bash, Python | Imperative — "run these commands" |
| Config files | [[Docker Compose]], Caddyfile | Declarative — "here's what I want" |
| Provisioning | Terraform, Pulumi | Declarative with state tracking |
| Configuration management | Ansible, Chef, Salt | Declarative system configuration |
| GitOps | ArgoCD, Flux | Git as the source of truth for cluster state |

## Declarative vs. Imperative

- **Declarative** — You describe the desired end state; the tool figures out how to get there. Idempotent by nature. (Terraform, Docker Compose, Kubernetes manifests)
- **Imperative** — You describe the steps to execute. Simpler for one-off tasks but harder to make idempotent. (Bash scripts, Ansible ad-hoc commands)

Most modern IaC tools are declarative, but pragmatic setups often mix both — declarative for service definitions, imperative scripts for backup, migration, and bootstrapping.

## Homelab IaC Patterns

In a homelab context like InfraKeeper, IaC manifests as:

- **Docker Compose files** — Declarative service definitions with volumes, networks, environment
- **SQL init scripts** — Database schema and security hardening applied on first boot
- **Shell scripts** — Terminal setup, backup procedures, certificate builds
- **Caddyfile** — Reverse proxy routing and TLS configuration
- **Backup scripts** — Capture config files from remote hosts for disaster recovery
