---
title: Portainer
type: Tool
cover: "[[Wiki/Tools/_covers/portainer.png]]"
sources:
related:
  - "[[Docker]]"
  - "[[Docker Compose]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

Portainer is a web-based container management UI that simplifies Docker and Kubernetes operations through a visual interface. It provides real-time visibility into containers, images, volumes, and networks — useful for quick inspection and management without dropping to the CLI every time.

## Use Cases

- **Visual container management** — Start, stop, restart, and inspect containers through a clean web UI
- **Image and volume administration** — Pull images, manage registries, and browse volume contents
- **Real-time logs and console** — View container logs and attach to running containers from the browser
- **Stack deployment** — Deploy Docker Compose stacks directly from the UI or from a git repository
- **Multi-environment management** — Manage multiple Docker hosts and Kubernetes clusters from a single Portainer instance

## Examples

### Deploy Portainer via Docker

```bash
docker volume create portainer_data

docker run -d \
  --name portainer \
  -p 9443:9443 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  --restart always \
  portainer/portainer-ce:latest
```

Access at `https://localhost:9443` and create an admin account on first launch.

### Deploy a stack from the UI

1. Navigate to Stacks > Add Stack
2. Paste a `docker-compose.yml` or point to a git repository
3. Set environment variables
4. Click Deploy

### API: List running containers

```bash
curl -s -H "X-API-Key: $PORTAINER_API_KEY" \
  "https://portainer.local:9443/api/endpoints/1/docker/containers/json" | jq '.[].Names'
```

## Links

- **Official site:** https://www.portainer.io
- **Repository:** https://github.com/portainer/portainer
- **Documentation:** https://docs.portainer.io
