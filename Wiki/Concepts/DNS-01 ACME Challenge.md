---
title: DNS-01 ACME Challenge
type: Concept
sources:
  - "InfraKeeper"
related:
  - "[[Caddy]]"
  - "[[Reverse Proxy]]"
  - "[[Split-Horizon DNS]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
shared with: Altoe
---

DNS-01 is a method of proving domain ownership to a Certificate Authority (CA) during the ACME (Automatic Certificate Management Environment) protocol. Instead of serving a file over HTTP, the domain owner creates a specific TXT record in DNS. This makes it the only ACME challenge type that supports **wildcard certificates** and works for services that are **not publicly accessible**.

## Why It Matters

- **Internal services get valid TLS certs** — Services behind a firewall with no public HTTP endpoint can still obtain Let's Encrypt certificates
- **Wildcard support** — A single `*.example.com` certificate covers all subdomains without individual validation
- **Private topology stays private** — No need to expose internal IPs or services to the internet; only temporary DNS TXT records are created
- **Automated renewal** — Tools like [[Caddy]] handle the entire flow: create TXT record via DNS provider API, verify, obtain cert, clean up

## How It Works

```
1. Client (Caddy) requests cert for *.xlean.net from Let's Encrypt
2. Let's Encrypt responds: "prove you own xlean.net — create TXT record
   _acme-challenge.xlean.net = <random-token>"
3. Caddy calls Cloudflare API to create the TXT record
4. Let's Encrypt queries public DNS, finds the TXT record
5. Certificate issued → Caddy stores and serves it
6. Caddy deletes the temporary TXT record
7. Auto-renews ~30 days before expiry
```

## ACME Challenge Types Compared

| Type | Mechanism | Wildcard | Works offline |
|------|-----------|----------|---------------|
| **HTTP-01** | Serve file at `/.well-known/acme-challenge/` | No | No — requires port 80 open |
| **DNS-01** | Create TXT record in DNS | Yes | Yes — only DNS API needed |
| **TLS-ALPN-01** | Respond on TLS handshake | No | No — requires port 443 open |

## DNS Provider API Integration

DNS-01 requires programmatic access to your DNS provider. Common integrations:

- **Cloudflare** — Scoped API tokens per zone (used in InfraKeeper)
- **Route53** — AWS IAM credentials
- **Google Cloud DNS** — Service account
- **DigitalOcean** — API token

## Security Considerations

- Scope API tokens to the minimum permissions (single zone, TXT records only)
- The DNS provider sees only temporary TXT records — no A records or internal IPs are exposed
- Store API tokens securely (e.g., environment files with mode 600)
