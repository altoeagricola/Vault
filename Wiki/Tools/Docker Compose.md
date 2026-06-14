---
title: Docker Compose
type: Tool
cover: "[[Wiki/Tools/_covers/docker-compose.png]]"
sources:
  - InfraKeeper
related:
  - "[[Docker]]"
  - "[[Portainer]]"
  - "[[PostgreSQL]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

Docker Compose is a tool for defining and running multi-container Docker applications using a declarative YAML file. It turns complex `docker run` commands into version-controlled, reproducible stack definitions — making it the standard way to manage homelab service stacks.

## Use Cases

- **Multi-service stacks** — Define an entire application (app + database + cache + proxy) in a single file
- **Development environments** — Spin up full local stacks with `docker compose up` and tear them down just as easily
- **Service orchestration** — Control startup order, health checks, restart policies, and dependency chains
- **Dependency management** — Pin image versions, manage environment variables, and share volumes between services
- **Reproducible deployments** — Check compose files into git for consistent deployments across environments

## Examples

### Basic compose file with app and database

```yaml
services:
  app:
    image: myapp:latest
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgres://app:secret@db:5432/myapp
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:16
    environment:
      POSTGRES_USER: app
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: myapp
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U app"]
      interval: 5s
      retries: 5

volumes:
  pgdata:
```

### Using environment files

```yaml
services:
  app:
    image: myapp:latest
    env_file:
      - .env
```

### Common commands

```bash
# Start all services in detached mode
docker compose up -d

# View logs
docker compose logs -f app

# Recreate a single service
docker compose up -d --force-recreate app

# Stop and remove everything
docker compose down -v
```

## Links

- **Official site:** https://docs.docker.com/compose/
- **Repository:** https://github.com/docker/compose
- **Documentation:** https://docs.docker.com/compose/
