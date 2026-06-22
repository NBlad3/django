# AGENTS.md — Django Monorepo

## Repo structure

5 independent Django projects in one repo (no monorepo tooling). Each has its own `manage.py`, `settings.py`, `venv/`, and `db.sqlite3`.

```
diyblog/        # Blog with Post/Category/Comment + comment form
health_app/     # INCOMPLETE — scaffold only, `app` not in INSTALLED_APPS
my_students/    # Student CRUD with form (name/email/gender/age)
practice/       # URL parameter exercises, no models
showcase/       # Instagram-like clone (Profile with following, Post)
```

## Dev commands

Each project is independent; run commands inside its directory:

```bash
# Run server for a specific project
cd my_students && python manage.py runserver

# Run migrations
cd diyblog && python manage.py makemigrations && python manage.py migrate
```

No shared lint/test/format commands exist. No CI. No pre-commit.

## Testing

Tests exist as empty stubs (`from django.test import TestCase` only). Run via:

```bash
cd <project> && python manage.py test
```

No pytest, no custom test config.

## Environment

- Python 3.14.3 (PyCharm SDK)
- Django versions vary per project: 5.2 (diyblog, my_students), 5.2.12 (showcase), 6.0.4 (practice), 6.0.6 (health_app)
- Each project has its own venv/ — activate before working in that project
- `requirements.txt` files exist in `diyblog/` and `practice/` but contain raw `pip freeze` output with `.dist-info` entries (not directly installable)

## Known issues

1. **health_app** is a scaffold: `app` not in INSTALLED_APPS, no models/views/URLs
2. **showcase** URL routing bug: root `"myhome"` (no trailing slash) only matches `/myhome`, not `/myhome/`; app route `"/profile"` leading slash gets stripped by Django
3. **showcase** `admin.py` imports Profile/Post but never registers them
4. `db.sqlite3` files committed despite `.gitignore` rule (grandfathered in)
5. No `DEFAULT_AUTO_FIELD` set in `health_app` or `practice` settings
6. **diyblog** uses `TIME_ZONE = 'Europe/Berlin'` (not UTC like the others)
7. **my_students** is the PyCharm project root / Django facet target

## Style notes

- All views are function-based (no class-based views)
- No type hints in any codebase
- Templates: diyblog has a base template; other projects use standalone HTML
- Form styling via raw CSS in my_students (`form.css`), SimpleCSS CDN in diyblog, Bootstrap 5.3.3 in showcase
