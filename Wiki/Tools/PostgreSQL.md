---
title: PostgreSQL
type: Tool
cover: "[[Wiki/Tools/_covers/postgresql.svg]]"
sources:
  - InfraKeeper
related:
  - "[[Docker Compose]]"
created: 2026-04-13
updated: 2026-06-01
confidence: high
---

PostgreSQL is an advanced open-source relational database known for its extensibility, standards compliance, and reliability. It supports JSONB for document-style storage, full-text search, and extensions like PostGIS — making it versatile enough to serve as the single database for most homelab and production applications.

## Use Cases

- **Primary application database** — ACID-compliant relational storage for web apps, APIs, and services
- **JSONB document storage** — Store and query semi-structured data without sacrificing relational capabilities
- **Full-text search** — Built-in tsvector/tsquery for search without an external engine
- **Geospatial data (PostGIS)** — Geographic queries, spatial indexing, and location-based features
- **Data warehousing** — Window functions, CTEs, materialized views, and partitioning for analytical workloads

## Examples

### Role and database creation

```sql
CREATE ROLE app_user WITH LOGIN PASSWORD 'secure_password';
CREATE DATABASE myapp OWNER app_user;

-- Connect to the new database
\c myapp

-- Create schema
CREATE SCHEMA app AUTHORIZATION app_user;
```

### Security hardening

```sql
-- Revoke default public access
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON DATABASE myapp FROM PUBLIC;

-- Grant specific permissions
GRANT CONNECT ON DATABASE myapp TO app_user;
GRANT USAGE ON SCHEMA app TO app_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA app TO app_user;
```

### Performance tuning for SSD-based systems

```ini
# postgresql.conf adjustments for SSD
random_page_cost = 1.1
effective_io_concurrency = 200
shared_buffers = 2GB           # ~25% of RAM
work_mem = 64MB
maintenance_work_mem = 512MB

# Enable pg_stat_statements
shared_preload_libraries = 'pg_stat_statements'
pg_stat_statements.track = all
```

### Query top slow queries with pg_stat_statements

```sql
SELECT
  calls,
  round(total_exec_time::numeric, 2) AS total_ms,
  round(mean_exec_time::numeric, 2) AS avg_ms,
  query
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;
```

## Links

- **Official site:** https://www.postgresql.org
- **Repository:** https://github.com/postgres/postgres
- **Documentation:** https://www.postgresql.org/docs/
