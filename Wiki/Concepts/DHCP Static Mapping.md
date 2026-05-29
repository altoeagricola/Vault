---
title: DHCP Static Mapping
type: Concept
sources:
  - "InfraKeeper"
related:
  - "[[OPNsense]]"
  - "[[Split-Horizon DNS]]"
  - "[[AdGuard Home]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

DHCP static mapping (also called DHCP reservation) assigns a fixed IP address to a specific device based on its MAC address. The device still uses DHCP to obtain its address — it just always gets the same one. This combines the convenience of DHCP (automatic DNS, gateway, search domains) with the predictability of static IPs.

## Why It Matters

- **Deterministic addressing** — Infrastructure hosts (firewalls, DNS servers, containers) always get the same IP without manual configuration on each device
- **DHCP options still apply** — Devices receive DNS servers, search domains, NTP, and gateway settings automatically via DHCP options
- **Easier management** — All IP assignments are centralized in the DHCP server rather than scattered across individual host configs
- **Survives reimaging** — Rebuild a host from scratch and it gets the same IP on first boot, as long as the MAC stays the same

## How It Works

```
1. Device sends DHCP DISCOVER with its MAC address
2. DHCP server checks static mappings table
3. If MAC matches → assign the reserved IP
4. If no match → assign from the dynamic pool
5. Device receives IP + all DHCP options (DNS, gateway, search domains)
```

## DHCP Options Worth Knowing

| Option | Name | Purpose |
|--------|------|---------|
| 6 | DNS Server | Override default DNS — e.g., point all clients to [[AdGuard Home]] |
| 119 | Search Domains | Append domain suffixes for bare hostname resolution (e.g., `lab`, `xlean.net`) |
| 3 | Default Gateway | Network gateway address |
| 42 | NTP Server | Time server address |

## Static Mapping vs. Static IP

| Approach | Config location | DHCP options | Central management |
|----------|----------------|--------------|-------------------|
| **Static mapping** | DHCP server | Yes — automatic | Yes — one place |
| **Static IP** | Each device | No — manual | No — per-device |

Static mappings are almost always preferable for homelabs. Reserve the first portion of the subnet for infrastructure (e.g., 10.0.1.1-99 for static mappings) and use the rest for the dynamic pool (e.g., 10.0.1.100-199).
