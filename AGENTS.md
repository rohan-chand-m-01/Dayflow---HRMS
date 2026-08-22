# AGENTS.md — Dayflow HRMS

This file governs all agent and developer behaviour for the Dayflow HRMS project.
**Every agent MUST read this file before performing any task.**

---

## 1. Project Overview

Dayflow is an Odoo custom module implementing a Human Resource Management System.

- **Repository:** `Dayflow---HRMS`
- **Module technical name:** `dayflow_hrms` *(to be created in Phase 1)*
- **Context:** Odoo × NMIT Bengaluru online screening hackathon

---

## 2. Project Architecture

### Permitted Stack

| Layer        | Technology                          |
|--------------|-------------------------------------|
| Backend      | Python + Odoo ORM                   |
| UI           | Odoo XML views                      |
| Database     | PostgreSQL through Odoo ORM         |
| Security     | Odoo security framework             |
| JavaScript   | OWL — only when explicitly required |

### Never Introduce

- React
- Next.js
- FastAPI
- Express
- Flask
- Django
- Separate frontend applications
- Unnecessary REST APIs
- Raw SQL (unless explicitly approved per-task)

---

## 3. No Hardcoding

Never hardcode:

- Database record IDs
- User IDs / employee IDs / company IDs
- Security decisions based on IDs
- Credentials, passwords, API keys, tokens, secrets
- Environment-specific paths
- Production URLs
- Configuration values that belong in Odoo data/configuration records

Always prefer:

- XML IDs (`ref()`, `browse()` via XMLID)
- Odoo relational fields
- Configuration records
- Environment variables (where appropriate and Odoo-idiomatic)
- Odoo ORM
- Odoo security groups + record rules

---

## 4. Odoo First

Before creating any custom model or field, verify:

1. Does Odoo already provide the required model?
2. Can the requirement be satisfied by model inheritance (`_inherit`)?
3. Can native Odoo functionality be reused directly?
4. Does the requirement only need Dayflow-specific additions?

**Do not recreate from scratch:**

- `res.users` / authentication
- `hr.employee` / employee profiles
- `hr.attendance` / attendance
- `hr.leave` / `hr.leave.type` / time off
- `hr.payslip` / payroll

Use `_inherit` to extend native models only where business logic requires it.

---

## 5. Database

- Use Odoo ORM exclusively.
- Do not use raw SQL unless explicitly approved for a specific task.
- Do not bypass Odoo ORM security mechanisms.
- Never directly query `ir_model_access`, `res_groups`, or security tables from Python.

---

## 6. Security

Security must be enforced using Odoo mechanisms:

- `res.groups` security groups
- `ir.model.access.csv` model-level access rights
- Record rules (`ir.rule`) for row-level security
- Field-level access via `groups=` attribute in model definitions and views

Do not rely solely on:
- Hidden menus
- Invisible fields/buttons
- Client-side checks

---

## 7. Git Collaboration Rules

### Branches

| Branch                     | Purpose                        | Owner    |
|----------------------------|--------------------------------|----------|
| `main`                     | Stable, reviewed code only     | Shared   |
| `feature/employee-attendance` | Employee, Attendance, Security | Member 1 |
| `feature/leave-payroll`    | Leave, Payroll, HR Dashboard   | Member 2 |

**Never commit directly to `main` during feature development.**
**Never force-push.**
**Never rewrite shared branch history.**

### File Ownership

**Member 1 owns:**

```
models/employee.py
models/attendance.py
views/employee_views.xml
views/attendance_views.xml
views/employee_dashboard.xml
security/*
tests/test_employee.py
tests/test_attendance.py
```

**Member 2 owns:**

```
models/leave.py
models/salary.py
views/leave_views.xml
views/salary_views.xml
views/hr_dashboard.xml
data/*
demo/*
tests/test_leave.py
tests/test_salary.py
README.md
```

Do not modify another member's owned feature files without explicit coordination and agreement.

### Shared / Protected Files

These files are shared — treat them with extra caution:

```
__manifest__.py
__init__.py
models/__init__.py
```

When modifying a shared file:
- Make the smallest possible change.
- Comment in the PR/commit exactly why the change is required.
- Never refactor unrelated code in the same commit.

### Merge Discipline

- Open a Pull Request for every feature branch merge into `main`.
- Both members must review PRs touching shared files.
- Resolve all conflicts explicitly; never auto-accept `theirs` or `ours` blindly.

---

## 8. Change Discipline

Before modifying any file:

1. Read the file.
2. Understand its purpose.
3. Understand its downstream dependencies.
4. Make the smallest necessary change.
5. Do not refactor unrelated code.
6. Do not create speculative / future-proofing architecture.

---

## 9. Phase Discipline

Dayflow development is divided into phases.
**Only implement the current phase.**
**Never implement future phases automatically.**

If a future-phase dependency is discovered during the current phase:

- STOP.
- Report the dependency clearly.
- Do not create unrelated code to pre-solve it.
- Wait for an explicit instruction to proceed.

### Phases (reference)

| Phase | Scope                                          |
|-------|------------------------------------------------|
| 0     | Repository governance, environment audit       |
| 1     | Odoo module skeleton (`dayflow_hrms`)          |
| 2     | Employee profile management                    |
| 3     | Attendance                                     |
| 4     | Leave / time-off                               |
| 5     | Approval workflows                             |
| 6     | Payroll / salary visibility                    |
| 7     | Dashboards                                     |
| 8     | Testing, polish, demo data                     |

---

## 10. Validation Requirements

After every meaningful change:

- Validate Python syntax: `python -m py_compile <file>`
- Validate XML: use `xmllint` or equivalent
- Validate Odoo module loading where possible
- Run relevant tests: `python -m pytest tests/` or `odoo-bin -i dayflow_hrms --test-enable`
- Run `git diff --check` (whitespace / merge conflict markers)
- Inspect `git diff` before committing

**Never claim a test passed unless it was actually executed and the output confirmed.**

---

## 11. Agent Behaviour Protocol

At the start of every task, an agent MUST:

1. Read `AGENTS.md` (this file).
2. Identify the current phase.
3. Identify which files are permitted to change in this phase.
4. Inspect existing code before writing anything.
5. Make minimal changes.
6. Validate changes.
7. Report exactly what changed, why, and what was deliberately left untouched.

Agents must NEVER:

- Silently modify unrelated files.
- Create files outside the current phase scope.
- Commit business logic before it has been validated.
- Assume environment details without checking.

---

## 12. Odoo Version Note

The Odoo version was **NOT DETECTED** during Phase 0 environment audit (no local Odoo installation found).

Phase 1 must resolve the Odoo version before creating any code that depends on version-specific APIs.

Detected environment as of Phase 0:

- Python: 3.11.9
- pip: 24.0
- Odoo executable: NOT FOUND
- Odoo Python package: NOT INSTALLED
- PostgreSQL (psql): NOT FOUND in PATH
- Docker: 29.2.1
- Docker Compose: v5.1.0

---

*Last updated: Phase 0 — Repository Governance*
