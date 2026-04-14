---
title: Database Hardening
type: Concept
sources:
  - "[[Products/InfraKeeper/InfraKeeper]]"
related:
  - "[[PostgreSQL]]"
  - "[[Infrastructure as Code]]"
created: 2026-04-13
updated: 2026-04-13
confidence: high
---

Database hardening is the practice of reducing a database's attack surface by restricting default permissions, isolating access per application, and enforcing the principle of least privilege. Most databases ship with permissive defaults that prioritize ease of setup over security — hardening closes those gaps.

## Why It Matters

- **Blast radius containment** — A compromised application can only access its own database, not the entire server
- **Prevent accidental damage** — Developers can't accidentally drop tables in the wrong database
- **Audit clarity** — Per-application roles make it clear which service is responsible for which queries
- **Compliance baseline** — Even in a homelab, good habits transfer to production

## PostgreSQL Hardening Checklist

### 1. Revoke public schema defaults

By default, any authenticated user can create objects in the `public` schema of any database:

```sql
-- Remove default CREATE privilege on public schema
REVOKE CREATE ON SCHEMA public FROM PUBLIC;

-- Remove default CONNECT privilege on all databases
REVOKE ALL ON DATABASE mydb FROM PUBLIC;
```

### 2. One role per application

Each application gets its own role and database. The role owns its database and has no access to others:

```sql
CREATE ROLE myapp WITH LOGIN PASSWORD 'strong_password';
CREATE DATABASE myapp_db OWNER myapp;

-- Only the owner can connect
REVOKE ALL ON DATABASE myapp_db FROM PUBLIC;
```

### 3. Superuser discipline

- Never use the superuser role in application connection strings
- Use superuser only for administrative tasks (role creation, extension loading, backups)
- Consider a separate admin role with limited superuser-like privileges

### 4. Connection and logging controls

```sql
-- Limit total connections
ALTER SYSTEM SET max_connections = 200;

-- Log slow queries (>250ms)
ALTER SYSTEM SET log_min_duration_statement = 250;

-- Log connection lifecycle
ALTER SYSTEM SET log_connections = on;
ALTER SYSTEM SET log_disconnections = on;

-- Log lock waits
ALTER SYSTEM SET log_lock_waits = on;
```

### 5. Network-level controls

- Restrict `pg_hba.conf` to specific IPs/subnets
- Use `scram-sha-256` authentication (not `md5` or `trust`)
- Bind to specific interfaces, not `0.0.0.0`, unless required

## Beyond PostgreSQL

These principles apply broadly:

| Database | Equivalent hardening |
|----------|---------------------|
| MySQL/MariaDB | Revoke global privileges, per-app users, `mysql_secure_installation` |
| MongoDB | Enable auth, bind to localhost, per-db users, disable scripting |
| Redis | Require password (`requirepass`), rename dangerous commands, bind to localhost |
