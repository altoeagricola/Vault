---
title: Reverse Proxy
type: Concept
sources:
  - "InfraKeeper"
related:
  - "[[Caddy]]"
  - "[[OPNsense]]"
  - "[[Split-Horizon DNS]]"
  - "[[DNS-01 ACME Challenge]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

A reverse proxy sits between clients and backend servers, forwarding client requests to the appropriate upstream service. Unlike a forward proxy (which acts on behalf of clients), a reverse proxy acts on behalf of servers — clients interact with the proxy without knowing the backend topology.

## Why It Matters

- **TLS termination** — Centralize certificate management in one place instead of configuring HTTPS on every backend service
- **Single entry point** — Route traffic to different services based on hostname or path, even when backends run on different hosts/ports
- **Security boundary** — Backend services never face the network directly; the proxy can enforce rate limits, IP filtering, and header policies
- **Transparent upgrades** — Swap or migrate backends without clients noticing, since they only talk to the proxy address

## How It Works

```
Client → reverse proxy (TLS termination, routing) → backend service
```

In a homelab context, a single reverse proxy (e.g., [[Caddy]] at 10.0.1.4) handles all `*.xlean.net` requests. DNS resolves every service domain to the proxy IP. The proxy inspects the `Host` header and forwards to the correct backend:

```
grafana.xlean.net → Caddy → 10.0.1.136:3000
portainer.xlean.net → Caddy → 10.0.1.136:9000
```

## Key Patterns

- **Host-based routing** — Match the `Host` header to select the upstream (most common in homelabs)
- **Path-based routing** — Route `/api` to one backend and `/app` to another
- **TLS passthrough** — Forward encrypted traffic without terminating, when the backend must handle its own TLS
- **Load balancing** — Distribute requests across multiple instances of the same backend

## Reverse Proxy vs. Load Balancer

A load balancer distributes traffic across replicas of the *same* service. A reverse proxy routes traffic to *different* services. Many tools (Caddy, Nginx, HAProxy, Traefik) do both.

## Common Implementations

| Tool | Strength |
|------|----------|
| [[Caddy]] | Automatic HTTPS, minimal config |
| Nginx | Battle-tested, high performance |
| Traefik | Docker-native auto-discovery |
| HAProxy | Advanced load balancing, TCP proxying |
| Envoy | Service mesh, gRPC-native |
