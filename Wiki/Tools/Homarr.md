---
title: Homarr
type: Tool
cover: "[[Wiki/Tools/_covers/homarr.png]]"
sources:
  - InfraKeeper
related:
  - "[[Docker Compose]]"
  - "[[Portainer]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

Homarr is a self-hosted dashboard for organizing and monitoring homelab services. It provides a customizable homepage with service bookmarks, status indicators, and integration widgets — giving a single entry point to everything running in the lab.

## Use Cases

- **Central service homepage** — One-click access to all homelab services organized by category
- **Docker container monitoring** — Real-time status of running containers via Docker socket integration
- **Bookmark organization** — Group services by function (networking, media, monitoring) with icons and descriptions
- **Status widgets** — Health checks and ping indicators for each service at a glance

## Examples

### Docker Compose setup

```yaml
services:
  homarr:
    image: ghcr.io/homarr-labs/homarr:latest
    container_name: homarr
    restart: unless-stopped
    ports:
      - "7575:7575"
    volumes:
      - homarr_appdata:/appdata
      - /var/run/docker.sock:/var/run/docker.sock:ro
    environment:
      - TZ=America/Sao_Paulo

volumes:
  homarr_appdata:
```

### Docker socket integration

Mount the Docker socket as read-only to enable container status monitoring:

```yaml
volumes:
  - /var/run/docker.sock:/var/run/docker.sock:ro
```

This allows Homarr to display which containers are running, stopped, or unhealthy directly on the dashboard.

## Links

- **Official site:** https://homarr.dev
- **Repository:** https://github.com/homarr-labs/homarr
- **Documentation:** https://homarr.dev/docs/getting-started/installation
