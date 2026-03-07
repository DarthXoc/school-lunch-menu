# CLAUDE.md — School Lunch Menu

## Project Overview

A Python/Flask web app that fetches and displays school lunch menus from the SchoolCafe API in a weekly calendar view. Deployed to Azure App Service (`slm-ai-xoc-dev`) via GitHub Actions on push to `main`.

## Tech Stack

- **Backend**: Python 3.12, Flask
- **Frontend**: Vanilla HTML/CSS/JS inside Jinja2 templates (no build step)
- **API**: SchoolCafe (`webapis.schoolcafe.com`)
- **Deployment**: Azure App Service via `.github/workflows/main_slm-ai-xoc-dev.yml`
- **Dev environment**: VSCode Dev Container (`.devcontainer/`) or local venv

## Project Structure

```
app.py                  # Flask app — routes, API proxy, config helpers
requirements.txt        # flask, requests
templates/
  base.html             # Shared layout, nav, CSS variables (light + dark mode)
  index.html            # Weekly calendar view + JS fetch logic
  settings.html         # Settings form + dynamic school/meal/serving-line loaders
config.json             # Runtime config, auto-created on first save (git-ignored)
.github/workflows/      # Azure deploy workflow (triggers on push to main)
.devcontainer/          # VSCode Dev Container config
```

## Running Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
# Open http://localhost:8080
```

Or open in VSCode and use **Reopen in Container** + **F5**.

## Key Architecture Notes

- **Config** is stored in `config.json` (git-ignored). Defaults live in `DEFAULT_CONFIG` in `app.py`. The settings page saves/resets this file.
- **API proxy**: All SchoolCafe requests go through Flask routes (`/api/menu`, `/api/schools`, `/api/meal-types`, `/api/serving-lines`) to avoid CORS issues on the client.
- **`PERSON_ID`** is hardcoded as the zero UUID — SchoolCafe doesn't require auth for anonymous menu access.
- **CSS** lives inline in each template's `{% block styles %}` block; CSS custom properties (`--clr-*`) in `base.html` handle light/dark theming.
- **Week navigation** is offset-based (`?offset=N`, clamped to ±4 weeks). Week bounds are always Sun–Sat; only Mon–Fri are rendered.

## Adding a District

In `app.py`, add to `DISTRICT_OPTIONS`:

```python
DISTRICT_OPTIONS = [
    ("4585", "Celina ISD"),
    ("1611", "Frisco ISD"),
    ("<district_id>", "My District"),
]
```

Find the district ID by inspecting SchoolCafe API traffic for your district.

## Deployment

Push to `main` triggers the GitHub Actions workflow, which builds a Python 3.12 venv, then deploys to Azure App Service `slm-ai-xoc-dev` (Production slot) using OIDC federation (no stored passwords).

## Do Not

- Do not commit `config.json` — it's git-ignored and contains user-specific school settings.
- Do not add a frontend build system; templates are plain HTML/CSS/JS intentionally.
- Do not use worktrees — work directly on the active branch.
