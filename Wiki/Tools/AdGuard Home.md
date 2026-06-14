---
title: AdGuard Home
type: Tool
cover: "[[Wiki/Tools/_covers/adguard-home.png]]"
sources:
  - InfraKeeper
related:
  - "[[OPNsense]]"
  - "[[Caddy]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

AdGuard Home is a network-wide DNS filtering server that blocks ads and trackers at the DNS level. Beyond ad blocking, it provides local DNS rewrite capabilities, making it essential for homelab setups where internal services need friendly hostnames without running a full DNS server.

## Use Cases

- **Network-wide ad blocking** — Filter ads and trackers for all devices on the network via DNS sinkholing
- **Local DNS rewrites** — Map custom hostnames to internal IPs for homelab services
- **DNS-level parental controls** — Block categories of content across the network without per-device configuration
- **DNS query logging and analytics** — Monitor which devices query which domains, identify suspicious traffic
- **Custom filter lists** — Add community-maintained or custom blocklists for fine-grained control

## Examples

### DNS rewrite via YAML configuration

```yaml
dns:
  rewrites:
    - domain: grafana.home.lab
      answer: 10.0.1.50
    - domain: "*.home.lab"
      answer: 10.0.1.50
```

### Add a DNS rewrite via API

```bash
curl -s -X POST 'http://adguard.local/control/rewrite/add' \
  -H 'Content-Type: application/json' \
  -u 'admin:password' \
  -d '{"domain":"app.home.lab","answer":"10.0.1.50"}'
```

### Filter list management via API

```bash
# List current filters
curl -s 'http://adguard.local/control/filtering/status' \
  -u 'admin:password' | jq '.filters[]'

# Refresh all filters
curl -s -X POST 'http://adguard.local/control/filtering/refresh' \
  -u 'admin:password' \
  -d '{"whitelist": false}'
```

## Links

- **Official site:** https://adguard.com/adguard-home.html
- **Repository:** https://github.com/AdguardTeam/AdGuardHome
- **Documentation:** https://github.com/AdguardTeam/AdGuardHome/wiki
