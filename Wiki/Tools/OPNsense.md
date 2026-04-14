---
title: OPNsense
type: Tool
cover: "[[Wiki/Tools/_covers/opnsense.png]]"
sources:
related:
  - "[[AdGuard Home]]"
  - "[[Caddy]]"
  - "[[Proxmox VE]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

OPNsense is an open-source firewall and routing platform based on FreeBSD, forked from pfSense. It provides enterprise-grade networking features — firewalling, DHCP, VPN, traffic shaping, and intrusion detection — through a clean web UI, making it a cornerstone of any serious homelab network.

## Use Cases

- **LAN/WAN firewall** — Stateful packet filtering with alias groups, floating rules, and per-interface policies
- **DHCP server via dnsmasq** — Static mappings, search domain distribution, and PXE boot support
- **VPN gateway** — WireGuard and OpenVPN for remote access and site-to-site tunnels
- **Traffic shaping** — QoS policies to prioritize latency-sensitive traffic (VoIP, gaming)
- **Intrusion detection/prevention** — Suricata IDS/IPS with community rulesets

## Examples

### DHCP static mapping (via dnsmasq)

In the OPNsense UI under Services > DHCPv4 > [Interface], add a static mapping:

| Field       | Value              |
|-------------|--------------------|
| MAC Address | `aa:bb:cc:dd:ee:ff` |
| IP Address  | `10.0.1.50`        |
| Hostname    | `server01`         |

### Distribute search domain (option 119) via dnsmasq

Under Services > Dnsmasq DNS > Settings, add advanced option:

```
dhcp-option=119,home.lab
```

### Restart dnsmasq via SSH

```bash
# Restart the dnsmasq service
configctl dns restart
```

## Links

- **Official site:** https://opnsense.org
- **Repository:** https://github.com/opnsense/core
- **Documentation:** https://docs.opnsense.org
