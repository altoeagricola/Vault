---
title: Split-Horizon DNS
type: Concept
sources:
  - "[[Products/InfraKeeper/InfraKeeper]]"
related:
  - "[[AdGuard Home]]"
  - "[[OPNsense]]"
  - "[[Caddy]]"
  - "[[Reverse Proxy]]"
  - "[[DNS-01 ACME Challenge]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

Split-horizon DNS (also called split-brain DNS) is a configuration where the same domain name resolves to different IP addresses depending on where the query originates. Internal clients get pointed to internal IPs, while external clients get public IPs — or different internal addresses depending on the access pattern.

## Why It Matters

- **Clean URLs for internal services** — Access `grafana.example.com` from inside the network without hairpin NAT or public routing
- **Separation of access patterns** — Browser traffic routes through a [[Reverse Proxy]] for TLS, while terminal traffic goes directly to service IPs
- **No hardcoded IPs** — Users and scripts reference hostnames, and DNS handles the routing
- **Security** — Internal topology is never exposed to public DNS

## InfraKeeper's Two-Domain Variant

InfraKeeper uses a practical variant with two domain suffixes instead of splitting a single domain:

| Domain | Resolves to | Purpose |
|--------|-------------|---------|
| `*.xlean.net` | Caddy reverse proxy (10.0.1.4) | Browser access with TLS |
| `*.lab` | Actual host IPs | Direct access (SSH, psql, APIs) |

```
# Browser access — goes through Caddy for HTTPS
grafana.xlean.net → AdGuard → 10.0.1.4 (Caddy) → 10.0.1.136:3000

# Terminal access — direct to host
psql -h postgres → appends .lab → postgres.lab → AdGuard → 10.0.1.136
```

Search domains (`lab`, `xlean.net`) are distributed via DHCP option 119, with `lab` first so bare hostnames resolve to direct IPs in terminal contexts.

## Implementation Approaches

| Method | How |
|--------|-----|
| **DNS rewrites** ([[AdGuard Home]]) | Map domains to internal IPs before upstream resolution |
| **Unbound views** | Return different answers based on client subnet |
| **CoreDNS/dnsmasq** | Conditional forwarding or static entries per zone |
| **Cloud DNS + local override** | Public DNS for external, local DNS server overrides for internal |

## Common Pitfall: DNS Rebind Protection

Some DNS resolvers (e.g., Unbound in [[OPNsense]]) block responses that map public domains to private IPs as a rebind attack protection. This breaks split-horizon setups where `grafana.example.com` should resolve to `10.0.1.x` internally. Solutions:

- Use a dedicated local DNS server ([[AdGuard Home]]) that doesn't enforce rebind protection
- Whitelist specific domains in the resolver's rebind exceptions
- Use a separate internal-only domain (`.lab`, `.local`) for direct access
