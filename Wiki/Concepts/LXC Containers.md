---
title: LXC Containers
type: Concept
sources:
  - "[[Products/InfraKeeper/InfraKeeper]]"
related:
  - "[[Proxmox VE]]"
  - "[[Docker]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

LXC (Linux Containers) provides OS-level virtualization — lightweight containers that share the host kernel but have their own isolated filesystem, networking, and process space. Unlike application containers ([[Docker]]), LXC containers behave like full Linux systems with init, systemd, and persistent state.

## Why It Matters

- **Near-native performance** — No hypervisor overhead; containers share the host kernel directly
- **Lower resource usage than VMs** — No separate kernel, BIOS, or virtual hardware per instance
- **Full OS experience** — Run systemd, install packages, SSH in — feels like a VM but lighter
- **Ideal for infrastructure services** — DNS servers, reverse proxies, and similar single-purpose services that need persistence but not a full VM

## LXC vs. Docker vs. VMs

| Aspect | LXC | Docker | VM (KVM/QEMU) |
|--------|-----|--------|----------------|
| Isolation | OS-level (namespaces, cgroups) | OS-level (namespaces, cgroups) | Hardware-level (hypervisor) |
| Kernel | Shared with host | Shared with host | Own kernel |
| Init system | Full (systemd) | None (single process) | Full (systemd) |
| Persistence | Persistent by default | Ephemeral by default | Persistent |
| Startup time | Seconds | Sub-second | 10-30 seconds |
| Overhead | Minimal | Minimal | Moderate (RAM, CPU) |
| Use case | Infrastructure services | Application workloads | Full OS isolation, different kernels |

## Proxmox + LXC

[[Proxmox VE]] provides first-class LXC support alongside KVM virtual machines. In InfraKeeper's setup:

- **LXC 101: AdGuard Home** — 1 core, 512MB RAM, 2GB disk — runs the DNS server
- **LXC 102: Caddy** — 1 core, 512MB RAM, 8GB disk — runs the reverse proxy

These services are lightweight, need persistence, and benefit from direct network access — a perfect LXC use case. Docker would add unnecessary layering; a full VM would waste resources.

## Key Concepts

- **Unprivileged containers** — Run without root on the host; stronger security boundary (Proxmox default)
- **Templates** — Pre-built OS images (Debian, Ubuntu, Alpine) downloaded from repositories
- **Bind mounts** — Share host directories into the container filesystem
- **Network bridge** — Containers connect to the host's network bridge (e.g., `vmbr5`) for LAN access
