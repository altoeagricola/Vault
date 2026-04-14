---
title: Caddy
type: Tool
cover: "[[Wiki/Tools/_covers/caddy.png]]"
sources:
related:
  - "[[AdGuard Home]]"
  - "[[OPNsense]]"
  - "[[Docker Compose]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

Caddy is a powerful, extensible web server and reverse proxy written in Go. Its standout feature is automatic HTTPS — it provisions and renews TLS certificates from Let's Encrypt (or ZeroSSL) out of the box, eliminating the manual certificate management burden that plagues most homelab and production setups.

## Use Cases

- **Reverse proxy for internal services** — Route traffic to backend containers by hostname with automatic TLS termination
- **Automatic TLS certificates** — Zero-config HTTPS via ACME protocol, including DNS-01 challenges for wildcard certs
- **Static file serving** — Serve static sites with minimal configuration
- **Load balancing** — Distribute requests across multiple upstreams with health checks
- **API gateway** — Combine reverse proxy, rate limiting, and header manipulation for API routing

## Examples

### Basic Caddyfile with reverse proxy

```caddyfile
grafana.example.com {
    reverse_proxy localhost:3000
}

portainer.example.com {
    reverse_proxy localhost:9000
}
```

### Static file server

```caddyfile
docs.example.com {
    root * /srv/docs
    file_server
}
```

### ACME DNS-01 with Cloudflare (for wildcard certs)

```caddyfile
{
    acme_dns cloudflare {env.CF_API_TOKEN}
}

*.home.example.com {
    tls {
        dns cloudflare {env.CF_API_TOKEN}
    }

    @grafana host grafana.home.example.com
    handle @grafana {
        reverse_proxy 10.0.1.50:3000
    }

    handle {
        abort
    }
}
```

## Links

- **Official site:** https://caddyserver.com
- **Repository:** https://github.com/caddyserver/caddy
- **Documentation:** https://caddyserver.com/docs/
