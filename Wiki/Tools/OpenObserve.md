---
title: OpenObserve
type: Tool
cover: "[[Wiki/Tools/_covers/openobserve.png]]"
sources:
  - InfraKeeper
related:
  - "[[Docker Compose]]"
  - "[[PostgreSQL]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

OpenObserve is a lightweight, OpenTelemetry-native observability platform for logs, metrics, and traces. It offers a significantly lower resource footprint compared to Elasticsearch or Datadog stacks, making it ideal for homelabs and small teams that want full observability without the operational overhead.

## Use Cases

- **Log aggregation** — Centralize logs from all services with full-text search and structured field extraction
- **Metrics collection** — Ingest and visualize Prometheus-compatible metrics with built-in dashboards
- **Distributed tracing** — Receive traces via OTLP/gRPC for end-to-end request visibility across services
- **Lightweight Elasticsearch alternative** — 140x lower storage cost claimed, with a familiar query interface
- **Alerting** — Define alert rules on logs and metrics with notification channels (Slack, email, webhook)

## Examples

### Docker Compose setup

```yaml
services:
  openobserve:
    image: public.ecr.aws/zinclabs/openobserve:latest
    container_name: openobserve
    restart: unless-stopped
    ports:
      - "5080:5080"    # Web UI and API
      - "5081:5081"    # OTLP gRPC endpoint
    environment:
      ZO_ROOT_USER_EMAIL: admin@example.com
      ZO_ROOT_USER_PASSWORD: ChangeMeNow
      ZO_DATA_DIR: /data
    volumes:
      - o2data:/data

volumes:
  o2data:
```

### OTLP gRPC endpoint configuration

Point your OpenTelemetry Collector or SDK to the gRPC endpoint:

```yaml
# otel-collector-config.yaml
exporters:
  otlp:
    endpoint: "openobserve:5081"
    tls:
      insecure: true
    headers:
      organization: default
      stream-name: default
      Authorization: "Basic <base64(email:password)>"
```

### CORS settings for development

```yaml
environment:
  ZO_HTTP_CORS_ALLOW_ORIGIN: "*"
  ZO_HTTP_CORS_ALLOW_METHODS: "GET,POST,PUT,DELETE,OPTIONS"
  ZO_HTTP_CORS_ALLOW_HEADERS: "Content-Type,Authorization"
```

## Links

- **Official site:** https://openobserve.ai
- **Repository:** https://github.com/openobserve/openobserve
- **Documentation:** https://openobserve.ai/docs/
