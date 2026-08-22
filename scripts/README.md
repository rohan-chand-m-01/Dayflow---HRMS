# Dayflow HRMS — Developer Environment Guide

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/rohan-chand-m-01/Dayflow---HRMS.git
cd Dayflow---HRMS

# 2. Create your local environment file
cp .env.example .env
# Edit .env and set POSTGRES_PASSWORD and ODOO_MASTER_PASSWORD

# 3. Start the environment
docker compose up -d

# 4. Wait for Odoo to be ready (~30-60 s on first start)
docker compose logs -f odoo

# 5. Open Odoo
#    http://localhost:8069
#    Create a database and install 'Dayflow HRMS'
```

## Services

| Service | Image              | Port (default) |
|---------|--------------------|----------------|
| odoo    | odoo:18.0          | 8069           |
| db      | postgres:16-alpine | internal only  |

## Useful Commands

```bash
# Tail Odoo logs
docker compose logs -f odoo

# Stop all services
docker compose down

# Stop and remove volumes (DESTROYS database — use with care)
docker compose down -v

# Restart Odoo only (after changing addons)
docker compose restart odoo

# Update a module from the CLI
docker compose exec odoo odoo -u dayflow_hrms -d <db_name> --stop-after-init

# Open a psql shell
docker compose exec db psql -U odoo dayflow_dev
```

## Addons Path

Custom addons live in `addons/`. The Odoo container mounts this directory at
`/mnt/extra-addons` and it is included in `addons_path` via `config/odoo.conf`.

## Environment Variables

See `.env.example` for required variables. Copy to `.env` and fill in values.
Never commit `.env`.
