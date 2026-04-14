---
title: Docker
type: Tool
cover: "[[Wiki/Tools/_covers/docker.png]]"
sources:
related:
  - "[[Docker Compose]]"
  - "[[Portainer]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

Docker is a container runtime that packages applications and their dependencies into isolated, portable units called containers. It standardizes how software is built, shipped, and run — making it the foundational layer for most homelab services and modern deployment workflows.

## Use Cases

- **Containerized services** — Run homelab applications (databases, dashboards, monitoring) in isolated containers
- **Development environments** — Reproducible dev setups that match production without polluting the host
- **Microservices architecture** — Package each service independently with its own dependencies and lifecycle
- **CI/CD pipelines** — Build and test in containers for consistent, reproducible builds

## Examples

### Run a container

```bash
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=secret \
  -v pgdata:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:16
```

### Build from a Dockerfile

```dockerfile
FROM node:20-slim
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

```bash
docker build -t myapp:latest .
docker run -d -p 3000:3000 myapp:latest
```

### Volume mounts and networking

```bash
# Named volume
docker volume create app_data

# Host bind mount
docker run -d -v /host/path:/container/path myapp

# Custom network
docker network create backend
docker run -d --network backend --name api myapi
docker run -d --network backend --name db postgres:16
```

## Links

- **Official site:** https://www.docker.com
- **Repository:** https://github.com/moby/moby
- **Documentation:** https://docs.docker.com
