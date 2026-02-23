# School Lunch Menu

A Python/Flask web app that fetches and displays your school's daily lunch (or breakfast) menu from the SchoolCafe API, organized in a weekly calendar view.

## Features

- Weekly calendar view with prev/next navigation
- Fetches live menu data from the SchoolCafe API
- Configurable school, grade, and meal type via a Settings page
- Serving line auto-set based on meal type (Breakfast → Hot Breakfast, Lunch → Main (Trayline))
- Grade options automatically scoped to the selected school type (Elementary, Middle, High)
- Expandable per-day details (sides, grains, fruits, milk, condiments, allergens)

## Requirements

- Python 3.12+
- Flask
- requests

## Getting Started

### Option 1: VSCode Dev Container (Recommended)

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and the [VSCode Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
2. Open this folder in VSCode.
3. When prompted, click **Reopen in Container** (or run the command `Dev Containers: Reopen in Container`).
4. Once the container is ready, press **F5** to launch the app in debug mode.
5. Open your browser to [http://localhost:8080](http://localhost:8080).

### Option 2: Local Development

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open [http://localhost:8080](http://localhost:8080).

## Configuration

On first launch the app uses built-in defaults (Miller Elementary, Lunch, Grade 1). Visit **/settings** to change:

| Setting | Description |
|---|---|
| School | Dropdown of configured schools |
| Grade | Grades scoped to the selected school type |
| Meal Type | Breakfast or Lunch |
| Serving Line | Auto-filled based on meal type (read-only) |

Settings are saved to `config.json` in the project root (git-ignored). If the file doesn't exist, defaults are used.

## Adding a School

In `app.py`, add an entry to `SCHOOL_OPTIONS`:

```python
SCHOOL_OPTIONS = [
    ("d7bd7613-a7ac-4508-b50f-fd713b8b9bba", "Miller Elementary", "Elementary"),
    ("<uuid>", "My Middle School", "Middle"),
]
```

The third value must be `"Elementary"`, `"Middle"`, or `"High"` — this controls which grade range is shown in Settings.

## Project Structure

```
.
├── .devcontainer/        # VSCode Dev Container configuration
├── .vscode/              # VSCode editor settings and launch configs
├── templates/
│   ├── base.html         # Shared layout, nav, and CSS variables
│   ├── index.html        # Weekly calendar view
│   └── settings.html     # Settings form
├── app.py                # Flask app, API proxy, config helpers
├── requirements.txt      # Python dependencies (flask, requests)
├── config.json           # Runtime config, auto-created on first save (git-ignored)
└── README.md             # This file
```
